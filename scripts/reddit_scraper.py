"""
Scrape the latest discussion threads from one or more subreddits and dump them to JSON.

Uses www.reddit.com (the current Reddit UI) via Playwright, reading the
`shreddit-post` / `shreddit-comment` custom elements directly (they carry clean
data attributes — real score, comment count, permalink, timestamp — no fuzzed
display-only numbers like old.reddit.com shows to logged-out users).

Polite by design: honest user-agent, delay between requests, no CAPTCHA/bot-check
bypassing. If Reddit serves a CAPTCHA or block page, the script stops rather than
trying to get around it.

Usage:
    python scripts/reddit_scraper.py --subreddits SaaS startups Entrepreneur \
        --limit 15 --sort new --comments 5 --out reddit_dump.json

Requires: pip install playwright && playwright install chromium
"""

import argparse
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright, TimeoutError as PWTimeoutError

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36 "
    "(personal research scraper; contact via reddit account owner)"
)

BLOCK_MARKERS = [
    "you've been blocked by network security",
    "are you a human",
    "hcaptcha",
    "please verify you are a human",
]

# Safety ceiling when --comments -1 ("all") is requested, so a viral thread
# can't turn into an unbounded click/scroll loop.
COMMENT_SAFETY_CAP = 500


def slugify(text: str, max_len: int = 80) -> str:
    text = (text or "untitled").strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-") or "untitled"
    return text[:max_len].rstrip("-")


REDDIT_ID_RE = re.compile(r"reddit\.com/r/[^/\s]+/comments/([a-z0-9]+)", re.IGNORECASE)


def extract_reddit_ids(text: str) -> set:
    return {m.lower() for m in REDDIT_ID_RE.findall(text or "")}


def load_excluded_ids(exclude_files, posts_dir) -> set:
    """Build a set of Reddit post IDs already present in this project, so the
    scraper skips posts we've already gathered/used instead of re-fetching them."""
    ids = set()

    for f in exclude_files or []:
        p = Path(f)
        if p.exists():
            ids |= extract_reddit_ids(p.read_text(encoding="utf-8", errors="ignore"))

    if posts_dir:
        pd = Path(posts_dir)
        if pd.exists():
            for jf in pd.glob("*.json"):
                try:
                    data = json.loads(jf.read_text(encoding="utf-8"))
                except Exception:
                    continue
                pid = (data.get("id") or "").replace("t3_", "").lower()
                if pid:
                    ids.add(pid)
                ids |= extract_reddit_ids(data.get("permalink") or "")

    return ids


def is_blocked(page) -> bool:
    body_text = page.inner_text("body").lower()
    return any(marker in body_text for marker in BLOCK_MARKERS)


def handle_if_blocked(page, label: str, headed: bool, captcha_wait: float, poll_interval: float = 3.0) -> bool:
    """Returns True if the page is clear to proceed, False if it's blocked and
    couldn't be resolved. In headed mode, a real browser window is visible on
    screen — this polls for you to solve any CAPTCHA in it by hand rather than
    attempting to solve or bypass anything itself."""
    if not is_blocked(page):
        return True

    if not headed:
        print(f"  [!] Blocked/CAPTCHA on {label} — run with --headed to solve it by hand next time.", file=sys.stderr)
        return False

    print(f"  [!] Blocked/CAPTCHA on {label}.", file=sys.stderr)
    print(f"      A browser window is open on your screen — please solve it there.", file=sys.stderr)
    print(f"      Waiting up to {int(captcha_wait)}s for it to clear...", file=sys.stderr)

    waited = 0.0
    while waited < captcha_wait:
        page.wait_for_timeout(int(poll_interval * 1000))
        waited += poll_interval
        if not is_blocked(page):
            print(f"      Cleared after {int(waited)}s — continuing.", file=sys.stderr)
            return True

    print(f"      Still blocked after {int(captcha_wait)}s — giving up on {label}.", file=sys.stderr)
    return False


def int_attr(el, name):
    raw = el.get_attribute(name)
    if raw is None:
        return None
    try:
        return int(raw)
    except ValueError:
        return None


def expand_more_comments(page, max_comments: int, max_clicks: int, delay: float):
    """Click 'X more replies' / 'X more comments' controls (same as a human browsing
    would) until the tree is fully expanded, the comment cap is hit, or we run out
    of clickable controls / stop making progress."""
    clicks = 0
    while clicks < max_clicks:
        current_count = len(page.query_selector_all("shreddit-comment"))
        if max_comments and current_count >= max_comments:
            break

        target = None
        for b in page.query_selector_all("button"):
            try:
                if not b.is_visible():
                    continue
                txt = b.inner_text().strip().lower()
            except Exception:
                continue
            if "more repl" in txt or "more comment" in txt:
                target = b
                break

        if not target:
            break

        try:
            target.scroll_into_view_if_needed(timeout=5000)
            target.click(timeout=5000)
        except Exception:
            break

        clicks += 1
        page.wait_for_timeout(int(delay * 1000))

        new_count = len(page.query_selector_all("shreddit-comment"))
        if new_count <= current_count:
            break


def collect_comments_flat(page, max_comments: int):
    flat = []
    for c in page.query_selector_all("shreddit-comment"):
        body_el = c.query_selector("[slot='comment'] p")
        text = body_el.inner_text().strip() if body_el else ""
        if not text or text.lower() in ("[deleted]", "[removed]"):
            continue
        flat.append({
            "id": c.get_attribute("thingid"),
            "parent_id": c.get_attribute("parentid"),
            "depth": int_attr(c, "depth"),
            "author": c.get_attribute("author"),
            "score": int_attr(c, "score"),
            "text": text,
        })
        if max_comments and len(flat) >= max_comments:
            break
    return flat


def build_comment_tree(flat_comments):
    """Reassemble parent/child hierarchy from the flat, document-ordered comment
    list. Document order already matches Reddit's threaded reply order, so
    appending children in that order preserves reply order within each branch."""
    by_id = {c["id"]: {**c, "replies": []} for c in flat_comments if c["id"]}
    roots = []
    for c in flat_comments:
        node = by_id.get(c["id"])
        if node is None:
            continue
        parent_id = c.get("parent_id")
        parent = by_id.get(parent_id) if parent_id else None
        if parent is not None:
            parent["replies"].append(node)
        else:
            roots.append(node)
    return roots


def scrape_subreddit(
    page, subreddit: str, sort: str, limit: int, comment_limit: int, delay: float,
    fetch_full_text: bool = True, headed: bool = False, captcha_wait: float = 180.0,
    excluded_ids: set = None,
):
    excluded_ids = excluded_ids or set()
    url = f"https://www.reddit.com/r/{subreddit}/{sort}/"
    posts = []
    seen_ids = set()
    skipped_known = 0

    page.goto(url, wait_until="domcontentloaded", timeout=30000)
    if not handle_if_blocked(page, f"r/{subreddit}", headed, captcha_wait):
        return posts

    # New Reddit is an infinite-scroll feed — scroll until we have enough NEW
    # posts (excluding ones already in the project) or stop making progress.
    stalls = 0
    while len(posts) < limit and stalls < 4:
        post_els = page.query_selector_all("shreddit-post")
        for p in post_els:
            if len(posts) >= limit:
                break
            post_id = p.get_attribute("id")
            if not post_id or post_id in seen_ids:
                continue
            seen_ids.add(post_id)
            short_id = post_id.replace("t3_", "").lower()
            if short_id in excluded_ids:
                skipped_known += 1
                continue
            try:
                permalink = p.get_attribute("permalink") or ""
                full_permalink = f"https://www.reddit.com{permalink}" if permalink else None
                posts.append({
                    "id": post_id,
                    "subreddit": subreddit,
                    "title": p.get_attribute("post-title"),
                    "author": p.get_attribute("author"),
                    "score": int_attr(p, "score"),
                    "num_comments": int_attr(p, "comment-count"),
                    "domain": p.get_attribute("domain"),
                    "post_type": p.get_attribute("post-type"),
                    "created_at": p.get_attribute("created-timestamp"),
                    "permalink": full_permalink,
                    "scraped_at": datetime.now(timezone.utc).isoformat(),
                    "selftext": None,
                    "comments": [],
                })
            except Exception as e:
                print(f"  [!] Skipped a post on r/{subreddit}: {e}", file=sys.stderr)

        if len(posts) >= limit:
            break

        before = len(seen_ids)
        page.mouse.wheel(0, 4000)
        page.wait_for_timeout(int(delay * 1000))
        after_els = page.query_selector_all("shreddit-post")
        stalls = stalls + 1 if len(after_els) <= before else 0

    # Visit each post's page to grab the full post body (selftext) and, optionally, top comments.
    if fetch_full_text or comment_limit > 0:
        for post in posts:
            if not post["permalink"]:
                continue
            try:
                page.goto(post["permalink"], wait_until="domcontentloaded", timeout=30000)
                page.wait_for_timeout(1000)
                if not handle_if_blocked(page, post["permalink"], headed, captcha_wait):
                    time.sleep(delay)
                    continue

                if fetch_full_text:
                    post_el = page.query_selector("shreddit-post")
                    text_el = post_el.query_selector("div[slot='text-body']") if post_el else None
                    if text_el:
                        selftext = text_el.inner_text().strip()
                        # Strip the "Read more"/"Read less" collapse-toggle label Reddit
                        # appends to the same text node on long posts.
                        for suffix in ("Read more", "Read less"):
                            if selftext.endswith(suffix):
                                selftext = selftext[: -len(suffix)].rstrip()
                        post["selftext"] = selftext or None

                if comment_limit != 0:
                    max_comments = comment_limit if comment_limit > 0 else COMMENT_SAFETY_CAP
                    expand_more_comments(page, max_comments, max_clicks=max(20, max_comments // 5), delay=delay)
                    flat = collect_comments_flat(page, max_comments)
                    post["comments"] = build_comment_tree(flat)
                    post["comments_fetched"] = len(flat)
            except PWTimeoutError:
                print(f"  [!] Timeout fetching {post['permalink']}", file=sys.stderr)
            except Exception as e:
                print(f"  [!] Error fetching {post['permalink']}: {e}", file=sys.stderr)
            time.sleep(delay)

    if skipped_known:
        print(f"  (skipped {skipped_known} already-known post(s) on r/{subreddit})")

    return posts


def main():
    ap = argparse.ArgumentParser(description="Scrape latest Reddit discussions into JSON.")
    ap.add_argument("--subreddits", nargs="+", required=True, help="Subreddit names, no r/ prefix")
    ap.add_argument("--sort", default="new", choices=["new", "hot", "top", "rising"])
    ap.add_argument("--limit", type=int, default=15, help="Posts per subreddit")
    ap.add_argument(
        "--comments", type=int, default=5,
        help="Max total comments to fetch per post, nested with full reply hierarchy "
             "(0 to skip, -1 for all, capped at %d as a safety ceiling)" % COMMENT_SAFETY_CAP,
    )
    ap.add_argument("--delay", type=float, default=2.0, help="Seconds to wait between page loads")
    ap.add_argument("--out", default="reddit_dump.json", help="Combined output JSON file path")
    ap.add_argument("--no-full-text", action="store_true", help="Skip fetching full post body text (selftext)")
    ap.add_argument(
        "--posts-dir", default="scraped_posts",
        help="Folder to also dump each post as its own JSON file, named "
             "<title-slug>_<created-date>.json (empty string to disable)",
    )
    ap.add_argument(
        "--headed", action="store_true",
        help="Show the browser window instead of running headless. If Reddit shows a "
             "CAPTCHA/block page, the script pauses and waits for you to solve it by "
             "hand in the visible window, then resumes automatically.",
    )
    ap.add_argument(
        "--captcha-wait", type=float, default=180.0,
        help="Seconds to wait for a manually-solved CAPTCHA to clear before giving up "
             "(only relevant with --headed)",
    )
    ap.add_argument(
        "--exclude-urls-file", nargs="+", default=[],
        help="Path(s) to files (e.g. sources-used.md, manuscript.md) to scan for Reddit "
             "post IDs already used in this project — matching posts are skipped entirely. "
             "--posts-dir is always scanned this way too, so already-dumped posts are never "
             "re-fetched.",
    )
    args = ap.parse_args()

    excluded_ids = load_excluded_ids(args.exclude_urls_file, args.posts_dir)
    if excluded_ids:
        print(f"Excluding {len(excluded_ids)} already-known post(s) from this run.")

    all_posts = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=not args.headed)
        context = browser.new_context(user_agent=USER_AGENT)
        page = context.new_page()

        for sub in args.subreddits:
            print(f"Scraping r/{sub} ({args.sort}, limit {args.limit})...")
            posts = scrape_subreddit(
                page, sub, args.sort, args.limit, args.comments, args.delay,
                fetch_full_text=not args.no_full_text,
                headed=args.headed, captcha_wait=args.captcha_wait,
                excluded_ids=excluded_ids,
            )
            print(f"  -> {len(posts)} posts")
            all_posts.extend(posts)
            time.sleep(args.delay)

        browser.close()

    out_path = Path(args.out)
    out_path.write_text(json.dumps(all_posts, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nWrote {len(all_posts)} posts to {out_path.resolve()}")

    if args.posts_dir:
        posts_dir = Path(args.posts_dir)
        posts_dir.mkdir(parents=True, exist_ok=True)
        used_names = set()
        for post in all_posts:
            created_day = (post.get("created_at") or "")[:10] or "unknown-date"
            base_name = f"{slugify(post.get('title'))}_{created_day}"
            file_name = f"{base_name}.json"
            n = 2
            while file_name in used_names:
                file_name = f"{base_name}-{n}.json"
                n += 1
            used_names.add(file_name)
            (posts_dir / file_name).write_text(
                json.dumps(post, indent=2, ensure_ascii=False), encoding="utf-8"
            )
        print(f"Wrote {len(all_posts)} individual post files to {posts_dir.resolve()}")


if __name__ == "__main__":
    main()
