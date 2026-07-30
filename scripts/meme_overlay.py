"""
Overlay bold, meme-style text captions onto a local image and save the result.

You supply the base image yourself (e.g. a blank meme template you downloaded
from Imgflip/Kapwing, or your own photo) — this script does not fetch or store
any images itself. Point it at a file and a list of captions with rough
positions, and it renders bold white text with a black outline, sized to fit.

Usage (one caption per --text, format "x_frac,y_frac,text" — fractions 0-1 of
image width/height for the text's vertical center; x is always centered):
    python scripts/meme_overlay.py --image template.png \
        --text "0.25,I built a great product" \
        --text "0.75,so clients will come, right?" \
        --out memes/output.png

For a 4-panel template like the classic Anakin/Padme reaction format, pass
one --text per panel in reading order (top-left, top-right, bottom-left,
bottom-right) with --layout 2x2, and it places each caption in its panel.

Requires: pip install pillow
"""

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FONT_CANDIDATES = [
    r"C:\Windows\Fonts\impact.ttf",
    r"C:\Windows\Fonts\arialbd.ttf",
]


def load_font(size: int):
    for path in FONT_CANDIDATES:
        if Path(path).exists():
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()


def wrap_text(draw, text, font, max_width):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        trial = f"{current} {word}".strip()
        bbox = draw.textbbox((0, 0), trial, font=font)
        if bbox[2] - bbox[0] <= max_width or not current:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_caption(draw, text, center_x, center_y, box_width, font_size, stroke_width):
    font = load_font(font_size)
    lines = wrap_text(draw, text.upper(), font, box_width)

    line_heights = []
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font, stroke_width=stroke_width)
        line_heights.append(bbox[3] - bbox[1])
    total_height = sum(line_heights) + (len(lines) - 1) * 6

    y = center_y - total_height / 2
    for line, lh in zip(lines, line_heights):
        bbox = draw.textbbox((0, 0), line, font=font, stroke_width=stroke_width)
        line_width = bbox[2] - bbox[0]
        x = center_x - line_width / 2
        draw.text(
            (x, y), line, font=font, fill="white",
            stroke_width=stroke_width, stroke_fill="black",
        )
        y += lh + 6


def main():
    ap = argparse.ArgumentParser(description="Overlay meme-style text captions on a local image.")
    ap.add_argument("--image", required=True, help="Path to the base image (you supply this)")
    ap.add_argument(
        "--text", action="append", required=True,
        help='One caption, format "y_frac,caption text" (y_frac 0-1 = vertical center position). '
             "Repeat --text for multiple captions/panels.",
    )
    ap.add_argument(
        "--layout", choices=["free", "2x2"], default="free",
        help="'free' places each caption at its given y_frac across the full width. "
             "'2x2' treats the image as a 4-panel grid and places one caption per panel "
             "in reading order (ignores the y_frac you pass, uses each panel's own center).",
    )
    ap.add_argument("--font-size", type=int, default=0, help="0 = auto-scale to image size")
    ap.add_argument("--out", required=True, help="Output file path")
    args = ap.parse_args()

    img = Image.open(args.image).convert("RGB")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    font_size = args.font_size or max(18, w // 18)
    stroke_width = max(2, font_size // 14)

    captions = []
    for t in args.text:
        y_frac_str, _, caption = t.partition(",")
        captions.append((float(y_frac_str), caption.strip()))

    if args.layout == "2x2":
        panel_w, panel_h = w // 2, h // 2
        centers = [
            (panel_w // 2, int(panel_h * 0.82)),
            (panel_w + panel_w // 2, int(panel_h * 0.82)),
            (panel_w // 2, panel_h + int(panel_h * 0.82)),
            (panel_w + panel_w // 2, panel_h + int(panel_h * 0.82)),
        ]
        for (_, caption), (cx, cy) in zip(captions, centers):
            draw_caption(draw, caption, cx, cy, panel_w * 0.85, font_size, stroke_width)
    else:
        for y_frac, caption in captions:
            draw_caption(draw, caption, w / 2, h * y_frac, w * 0.9, font_size, stroke_width)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path)
    print(f"Saved {out_path.resolve()}")


if __name__ == "__main__":
    main()
