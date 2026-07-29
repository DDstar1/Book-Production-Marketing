# The Hard Part Is Getting Anyone to Care

*A practical, story-driven book about SaaS marketing and the go-to-market struggles of early-stage founders.*

---

## About this manuscript

This manuscript is assembled incrementally. Each batch of entries synthesizes real founder-challenge
threads into original sections — the pain, the failed attempt, the turn, and the transferable lesson.

Every section follows the same four-beat framework:

1. **Pain-point hook** — the moment of frustration, in the reader's own terms.
2. **The struggle** — what the founder actually tried, and why it failed.
3. **What worked** — the turn, with concrete specifics: channel, numbers, sequence.
4. **The lesson** — a transferable principle, stated plainly.

Sourcing rules that govern every entry:

- Sections are synthesis, never transcription. No pasted source text.
- At most one short quote per section, under ~15 words, in quotation marks.
- Light attribution only — e.g. *(via a founder thread on r/SaaS)*. No usernames, no personal details.
- Nothing is invented. No fabricated threads, URLs, quotes, or metrics.

Every source consulted is logged in `sources-used.md`, which is also the deduplication ledger for
subsequent batches.

---

## Entries — 2026-07-29

### 1. The tool you built for yourself is not the tool other people need

**The pain.** You are answering messages at three in the morning to keep revenue from sliding. The
work is not hard, it is just endless, and every hour of it is an hour you are renting out at a rate
you would never quote a client. Nobody is going to fix this for you.

**The struggle.** So you fix it yourself. One founder running a creator page built a chat automation
tool for exactly one problem: their own unmanageable DM volume. They used it privately for about
three months. It did not occur to them that anyone else would want it — the thing felt too specific,
too welded to one workflow, to be a product. That instinct is where most internal tools die.

**What worked.** Other creators kept asking what they were using, and the founder eventually opened
it up. It has since done over $100k in revenue for the people using it, most of that in the last two
months. Being customer zero paid off three ways: they never had to guess whether a change was an
improvement, because they saw it in their own revenue within a week; they killed features fast,
because "I built this and then never used it" is a far cleaner signal than a user politely saying
they like something; and pricing was settled by knowing exactly what they would have paid to stop
doing the job by hand.

**The lesson.** Being your own customer is a fast start and a slow trap. It got this founder to a
working product in three months and became a liability by month five — settings hardcoded to one
person's habits, defaults that made sense for one page, and a certainty that the problem was fully
understood when what was fully understood was one version of it. Some of the most valuable features
now are ones the founder had no personal need for and initially argued against. And on the fear that
kept the tool in a drawer for three months: "specific is why people want it." The generic version
already exists and nobody uses it. *(via a founder thread on r/SaaS)*

### 2. You are not bad at marketing, you are talking to everyone at once

**The pain.** For months the building felt like the hard part, and you were good at it. Every day was
hyper-focused, solving a pain you personally ran into, convinced the existing tools were clunky and
missing the point. Then you shipped, and now you are looking at a dashboard with roughly zero users,
wondering whether you burned months on something nobody gives a damn about.

**The struggle.** The founder in this thread had no audience, no social following, and no marketing
background. They hated feeling like a spammy salesman. Cold outreach, in their words, felt like
shouting into a void — and that phrasing is the diagnosis, not the complaint. The void is what you
get when the message is aimed at everyone: nothing about it is addressed to any particular person, so
no particular person answers.

**What worked.** Two things surfaced from founders who had climbed out of the same ditch. First,
narrow hard: pick the one group who feels this pain the worst, go where they already gather, and show
the thing actually solving the problem rather than describing it. As one put it, "one real room beats
a hundred cold DMs into nothing." Second, and more concretely: another founder spent a month lurking
in the Facebook groups for their niche, answering questions without ever mentioning their tool. That
is where their first ten users came from.

**The lesson.** Before you buy reach, earn standing. The founders who cross the gap from built to
used almost never do it by broadcasting wider — they do it by getting narrow enough that one room of
people recognizes their own problem in what you are saying. Answer questions in that room for a month
without selling. The first ten users come from being useful in public, not from volume.
*(via a founder thread on r/SaaS)*

### 3. Separate the product problem from the go-to-market problem before you quit

**The pain.** You have posted the content, messaged the creators, DM'd hundreds of business owners,
tried every strategy you read about. The app is live. Traction is close to nothing. And the thought
arrives that you should stop, finish the degree, get the stable career, and let this go.

**The struggle.** A 20-year-old accounting student and bookkeeper had built an AI bookkeeping app for
small business owners and was, by their own account, completely exhausted from trying to get users.
Money and months were already in it. They still believed the product could help people. What was
burning them out was not building — it was marketing into silence, which is a very different
exhaustion, and much easier to mistake for a verdict on the product.

**What worked.** The most useful reply in the thread refused to answer the question as asked and
split it in two: "the burnout is coming from marketing, not from the product." Those are separate
problems and they deserve separate decisions. Another founder who had been in the same spot described
narrowing the audience instead of broadening it, and learning more from 20 focused conversations than
from hundreds of cold messages — which is what finally told them whether to keep building or pivot. A
third asked the question that actually locates the failure: where in the funnel is it leaking? Getting
people to the site, getting them to sign up, or getting them to connect a bank and start using it?
Each of those has a different fix, and "no traction" hides which one you have.

**The lesson.** Exhaustion is not evidence. Before you decide the product is wrong, find out which
stage is failing and whether you have ever run a narrow, high-intent version of the pitch at all.
Hundreds of cold messages that go nowhere is one experiment repeated hundreds of times, not hundreds
of experiments. Twenty real conversations will tell you more, and they will tell you faster.
*(via a founder thread on r/SaaS)*

### 4. The churn you can fix without talking to anyone

**The pain.** You are pouring everything into acquisition — new traffic, new signups, new logos —
while revenue you already earned quietly falls out the bottom. Nobody cancelled. A card just failed.

**The struggle.** Involuntary churn is invisible in the way that matters: it produces no angry email,
no exit survey, no conversation. It looks like a number that is slightly lower than it should be, and
because there is no story attached, it never makes it onto the roadmap. One SaaS operator described
spending time improving how failed subscription payments were handled and recovering more revenue
than expected — with no changes to pricing and no changes to marketing.

**What worked.** The thread's replies sharpened it into something more useful than "turn on dunning."
The first caution: if the customer was already leaving, "recovering a payment just delays the
cancellation" — you have bought a month, not saved an account. The second is the part that actually
pays: find out *why* payments are failing. One founder discovered their payment provider was
malfunctioning on international payments from certain countries. Switching providers recovered a
meaningful amount of revenue, and no amount of retry logic would have found that, because the failure
was never on the customer's side at all.

**The lesson.** Split churn into two buckets before you treat it. Voluntary churn is a value problem
and you fix it by talking to people. Involuntary churn is a plumbing problem and you fix it by
reading logs. Recovery tooling on top of a broken payment path just retries a request that was never
going to succeed. Check the pipe before you optimize the pump. *(via a founder thread on r/SaaS)*

### 5. The most expensive thing in your funnel is the waiting

**The pain.** Someone read your pricing page, checked your integrations, opened your docs, spent real
minutes deciding whether you were the right fit, and clicked "Book a Demo." And then your product
said: thanks, someone will get back to you.

**The struggle.** A team watching session recordings noticed their landing page was not the problem.
Visitors were not bouncing — they were doing everything the page was designed to make them do. The
drop was after the form. Nobody on the team had ever questioned that flow, because it is simply how
B2B SaaS works: form, SDR reply, scheduled call, everyone moves on. Watched from the buyer's side, the
founder points out, it looks absurd — like walking into a store, asking for help, and being told
someone will call you tomorrow.

**What worked.** They did not optimize the form, rewrite the emails, or test another headline. They
removed the wait. When someone wanted to talk, the conversation started then, while the problem was
still live in the person's head. The ones who were ready moved forward; the ones who were not left
with an actual answer instead of a confirmation email. That single change altered how people
interacted with them — and changed how the team thought about inbound generally.

**The lesson.** Every hour between peak intent and human contact is decay you are choosing to accept.
Traffic, click-through rate, and form conversion all get obsessive attention because they are easy to
measure, but none of them survive a funnel whose highest-intent moment ends in a queue. Look for the
place where a motivated buyer is told to wait, and delete it. *(via a founder thread on r/SaaS)*

### 6. Fake the backend, not the frontend

**The pain.** Everyone says validate before you build. Nobody tells you what that actually looks
like. A landing page and a waitlist tell you people are curious. They do not tell you whether anyone
understood the product, or would use it twice.

**The struggle.** A founder with several failed attempts behind them named the real problem: they had
been doing the easiest part first, which is building. The available alternatives all felt like
theater. Waitlists measure curiosity. A full interactive Figma flow can cost nearly as much work as
the MVP it was supposed to save you from. So the validation step gets skipped, and the code gets
written, and the cycle repeats.

**What worked.** The most upvoted answer in the thread inverts the usual instinct: "Fake the backend,
not the frontend." Deliver the real output manually to 20 or 30 people before building anything. A
landing page tests curiosity; manual delivery tests whether the value actually lands. Several founders
described running exactly this — the concierge MVP, where the outcome is produced by hand to learn
what people value. One refined it further: fake only the moment where the user makes the decision.
Whatever the product's "oh, I need this" step is — upload a CSV, pick a template, invite a teammate —
put that one step behind a single ugly hosted page and produce the result manually from a spreadsheet.
Watching where someone hesitates on that one screen teaches you more than a polished demo. Another
made the exchange concrete: ask for the same real file or request they would use in production, commit
to a clear manual turnaround, and hand back the result in the format the finished product would
produce.

**The lesson.** Validation is not asking people whether they would use it. It is delivering the
outcome and watching what happens next — whether they come back, whether they send a second one,
whether they ask what it costs. Do that by hand, for twenty people, before you write the system that
does it automatically. *(via a founder thread on r/startups)*

### 7. Selling the thing you have not built yet, without lying

**The pain.** The buyer wants something you do not have. It is close — the product can technically
support it, the workflow just is not packaged — and everyone on your side has already started
mentally counting the revenue.

**The struggle.** The thread describes the messy middle precisely, and both failure modes. One is the
demo that quietly implies the feature already exists: it buys you a great call and an implementation
that everyone regrets. The other is rigidity, treating every customer-specific request as scope creep
even when the request is the market telling you something clearly. Engineering says a sprint or two.
Sales believes the buyer walks if you say "not today." Neither instinct is trustworthy on its own.

**What worked.** The cleanest handling described is a sequence: show the current product exactly as it
is, name the missing piece plainly, and then keep two things apart that founders routinely blur —
"we can prototype this for your workflow" and "this is now part of the core product." One reply made
that operational. Put the missing feature into a separate pilot schedule *before* the contract closes.
Write down the prototype milestone and its acceptance test. Specify who supplies the sample data and
what happens if the feature misses that test. And start the normal subscription only once the current
product is useful on its own.

**The lesson.** A roadmap promise is not a lie if it is dated, scoped, and separable from what the
customer is paying for today. The discipline is structural, not verbal: if the deal only works when
the unbuilt feature ships, you have not sold your product — you have sold a custom build with a
subscription stapled to it. Make the current product stand on its own first, then let the pilot
either earn its place on the roadmap or fail its acceptance test cheaply. *(via a founder thread on
r/startups)*

### 8. Two customers is a workflow, not a market

**The pain.** Two former freelance clients each ask you for an application. You are a developer, so
you see the obvious efficiency: do not build two apps, build one platform with a module per vertical.
Veterinary today, dental tomorrow, restaurants after that.

**The struggle.** The founder in this thread was days from an MVP and asking a reasonable question —
how long does $1k MRR actually take? — with a lot of faith in the plan. The trap is hiding inside the
efficiency. Two clients who asked for something bespoke prove the workflow is painful enough to pay
someone to fix. They do not prove that a veterinary clinic and a dentist want the same product, and
the white-label architecture quietly assumes they do before anyone has checked.

**What worked.** The most useful reply reframed the target as "a customer-count problem, not a
calendar prediction." At $100/month, $1k MRR is ten retained customers. At $250, it is four. Stated
that way it stops being a motivational milestone and becomes a sales plan you can actually work. The
same reply laid out the sequence: get both existing clients paying, watch which parts they actually
use, and then try to sell the same core setup to a third customer *without custom work*. That third
sale is the real test. A second founder added the sorting rule that makes the first two clients pay
for themselves as research: document every request both of them make — the requests that overlap are
your core product, the one-offs are better handled as paid custom work.

**The lesson.** Revenue targets are arithmetic; convert them into a customer count and a price and
they become tractable. And build the broad platform only after one narrow version has sold twice
without modification. Otherwise you are not building a product with vertical modules, you are building
two consultancies that share a database. *(via a founder thread on r/startups)*

### 9. The market will tell you who your product is for, if you let it

**The pain.** You have been certain about your customer since the beginning. You built the thing for
them. Years in, the traction that was supposed to arrive has not, and the certainty is starting to
look like the problem.

**The struggle.** One founder documented six years and roughly $90,400 spent building a wearable that
combines kinesiology tape with wireless muscle stimulation — starting as a college freshman with no
engineering experience. The log is a catalogue of brute force: 300 cold LinkedIn messages to find a
technical co-founder, 11 national pitch competitions, a freelance engineer who became pure sunk cost,
cold emails to 150 investors a day for eight months, a 14-hour drive and a night sleeping in a
parking lot for a $10,000 check, a $19,000 patent bill paid with the last dollars in the account, and
a February where the product could not be built at cost and the whole thing nearly ended. Over
$265,000 raised eventually — and none of that is the part that made it work.

**What worked.** The hybrid fitness world exploded, HYROX with it, and that turned out to be exactly
where the product belonged: athletes who train savagely hard and care intensely about recovering
between sessions. The founder noticed and went all in on that one world — breaking down the sport,
ranking the stations, arguing about which one hurts most, building a community of people who actually
get it. The product stopped being pitched and started riding along inside content those people
already wanted to watch.

**The lesson.** Their own summary is the transferable part: you can spend years certain you know who
your product is for, and the market will still surprise you — your job is to notice when it is trying
to tell you something, then sprint at it. Persistence keeps you alive long enough to receive that
signal, but persistence is not what converts. Segment discovery is a live input, not a decision you
made at the start and now have to defend. *(via a founder thread on r/Entrepreneur)*

### 10. Cost per lead means nothing until you know what a lead is

**The pain.** You are paying an agency real money every day and the leads are not coming. You suspect
you could do better yourself, but you are the videographer who inherited the marketing, and you are
not sure whether your doubt is judgment or ego.

**The struggle.** The in-house marketer at a small solar company watched an outside firm run Meta for
four weeks at $50/day and produce four leads — roughly $350 per lead, none of which appeared to
convert. So he ran his own campaign alongside theirs for two and a half weeks at $30/day and got 19
leads at roughly $27 each. When the numbers came up, the firm's explanation was that the two campaigns
were competing in Meta's auction, suppressing delivery and inflating costs, and proposed consolidating
everything into one campaign — which would also mean more months and more money before anyone could
tell whose ads were actually working.

**What worked.** What made this legible at all was running a cheap parallel test instead of arguing
about it. That is the reusable move: a $30/day control campaign bought a real comparison that no
status call would have produced. But the thread also refuses to let the comparison off the hook. The
sharpest replies went straight at lead quality — both campaigns were using Meta instant forms, which
attract click-fraud bots submitting real-looking fake leads, and phone verification does not reliably
stop them. Both were also targeting cold audiences with no interest or behavior targeting, leaning
entirely on the algorithm. So the honest reading is not "in-house beat the agency." It is that a
20x gap in cost per lead is a question, and the answer depends on how many of those 19 leads were
people.

**The lesson.** Cost per lead is a ratio with an undefined denominator until you have verified what
counts as a lead. Cheap leads that never answer the phone are more expensive than expensive ones that
do. Run the parallel test — it is the fastest way to turn a vendor disagreement into data — then
insist that both sides of the comparison be measured on something further down the funnel than a form
submission. *(via a founder thread on r/marketing)*
