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


---

## Entries — 2026-07-29 (second batch)

### 11. A launch is an event, not a channel

**The pain.** The traffic graph is the same every time. A tall green spike on day one, a slow slide
for a fortnight, a flatline by day thirty. You did the thing everyone told you to do, and a month
later there is nothing left to show for it except a badge in your footer.

**The struggle.** A solo founder went looking at recent launch data and found the shape repeating
across product after product. What made it worse was the economy that has grown around that shape:
founders paying agencies anywhere from a hundred to over a thousand dollars to "optimise" a directory
launch, people buying upvotes, launch managers hired to run a single day. His summary of the trade is
hard to argue with — you are renting someone else's homepage for twenty-four hours, and a one-day
vanity badge does not pay server costs. The one reply the thread drew put the mechanism plainly: the
spike is "borrowed attention with a hangover."

**What worked.** The reframe is to stop grading a launch on its peak and start grading it on residue.
What is still working thirty days later? Indexed pages, backlinks from the directories that allow
real ones, an email list of people who arrived on the spike day and stayed, a search term you now
rank for. Those compound; the spike does not. The founder's own conclusion — durable discovery over
fleeting attention — is what pushed him into experimenting with a launch board built around lasting
SEO value rather than a single day of placement. Worth noting that he has a product interest in that
conclusion, which does not make the traffic graphs wrong.

**The lesson.** Treat a launch as a one-off distribution event and budget for it accordingly. It is
useful for feedback, for a burst of first users, and sometimes for a link that keeps paying. It is
not an acquisition channel, and no amount of money spent optimising the spike converts it into one.
Before you launch, write down what you want to still have in thirty days. If the honest answer is "a
badge," skip it. *(via a founder thread on r/SaaS)*

### 12. Segment by the shape of the deal, not the age of the company

**The pain.** You have built something you genuinely believe in and you cannot answer the only
question that matters next: who do I sell this to first? Every candidate segment sounds plausible for
about ten minutes, and then the other one does.

**The struggle.** A marketer at a bootstrapped startup laid the dilemma out precisely. Their product
is a sales workspace with an AI agent as the primary interface, built for high-ticket B2B where
preparation wins the deal. One instinct said go after young companies: no CRM data locked in another
tool, no migration pain, switching costs near zero. The other said company age is the wrong lens
entirely, and the real filter is how someone sells — long cycles, big deals, heavy research before
every call — which could describe a five-person agency or a twenty-year-old consulting firm. Both
arguments are coherent, which is exactly why the founder had been going back and forth instead of
selling.

**What worked.** The thread converged on the second instinct, and the sentence that settles it is
that "easy to switch" isn't the same as "needs this now." Absence of switching cost is a convenience
argument; hours currently burned preparing for a handful of expensive deals is a pain argument, and
pain is what moves a workflow. The same reply supplied the diagnostic: show it to someone who just
worked a long, high-value deal and watch which part they use without needing an explanation. Another
commenter narrowed it further — not just "people who sell big deals," but teams that already hold a
Monday pipeline review, because the ritual the product feeds already exists and nothing new has to be
invented. And the hardest number in the thread came from a founder who had run the same experiment
eight months earlier: they tried selling to three segments at once and closed nobody for a full
quarter.

**The lesson.** Segment on the shape of the problem, not the shape of the org chart. Company size and
company age are proxies you reach for because they are easy to filter on in a lead tool; deal shape,
research burden, and existing rituals are what actually predict whether someone will change how they
work. And whatever you choose, choose one. Three segments at once is not three times the pipeline, it
is one message that fits none of them. *(via a founder thread on r/SaaS)*

### 13. Selling against a capital purchase means selling to the budget line

**The pain.** Your buyer already has a solution to the problem. It costs them a fortune, it is bolted
to the ground, and someone senior signed off on it, which means proposing an alternative is also
proposing that a past decision was wrong.

**The struggle.** A founder selling gate-management software into shipping ports described the shape
of it: the industry buys heavy, expensive hardware, and he is asking terminals to solve the same
problems in software instead. He sent more than 150 messages before anything came back. That number
is the part worth sitting with — not because volume is the strategy, but because it is the honest
denominator for cold outreach into a conservative industry with a small number of buyers.

**What worked.** Two things. First, the positioning is a budget line rather than a feature list: zero
capex to the customer. Against a capital purchase, that is not a discount, it is a different approval
path — no committee, no depreciation schedule, no fight about next year's equipment budget. The
outcome framing is similarly concrete: fewer gate bottlenecks, less legal exposure, faster turnover
times. Second, and less obvious, is what the replies came back with: charge on value and savings
rather than seats, and talk to a lawyer with sector experience *before* the first contract, not
after. In a regulated, liability-heavy industry, contract structure is part of the product. Two ports
in different regions eventually surfaced, each with a different problem, and both are still described
as close rather than closed — which is the accurate way to hold it.

**The lesson.** When your competitor is a capital expenditure, your advantage is rarely that you are
better; it is that you are a smaller, faster decision. Sell the approval path. And when two buyers in
different regions arrive with different problems, that is information about the category, not
confirmation of your feature set — it tells you the pain is general and the configuration is going to
have to flex. *(via a founder thread on r/startups)*

### 14. What $0 actually buys you

**The pain.** You have a working product, no budget, no audience, no investors, and no appetite for
another article telling you to post on social media.

**The struggle.** That was the exact framing of the question, and the reason it drew sixty replies is
that most founders in this position have already done the useless version of every suggestion. Posted
into a void. Joined the communities. Bought nothing, gained nothing, and concluded that free
acquisition is a myth people describe after the fact.

**What worked.** The replies that carried specifics fell into two very different bets. The first is
manual and narrow: pick one customer type, go where those people already ask for help, and solve one
concrete problem by hand before pitching anything. Several founders described cold calling, with the
important correction attached — the constraint is list quality, not call volume, because "ten relevant
conversations usually teach you more than a hundred random calls." One person put the discipline in
plain terms: fifteen to thirty minutes a day in each place their audience gathers, posting and
replying, no selling unless someone asks. The second bet is an asset that compounds. One founder
building a rhyming app made a free rhyming dictionary covering 5.8 million words across 22 languages,
published it programmatically, and after a few months was seeing around 500,000 daily search
impressions and roughly 100 new users a day. Two very different time signatures — one pays this week,
the other pays in the second quarter — and the thread's sharpest question sits underneath both: if you
have no audience at all, how do you know you have something worth buying?

**The lesson.** With no money, time is the only currency, and there are exactly two good ways to spend
it. Point it at a list so narrow that every conversation is with someone who has the problem today, or
point it at an asset that keeps working after you stop touching it. What kills founders in this
position is the middle: broad, effortful activity that neither reaches a qualified person nor
accumulates into anything. Pick the fast one or the compounding one, and if you can only do one, do
the one that also teaches you what to build. *(via a founder thread on r/startups)*

### 15. Free is not a price, it is a missing decision

**The pain.** You are trying to validate without theatre. No landing page, no waitlist, no fake door —
you want to put a real thing in front of a real user and watch what happens.

**The struggle.** An engineer with twelve years in healthcare systems proposed the most generous
version of that: find one medical practice with a genuinely awful document workflow, build the tool
for free, let them keep it, and take nothing in return but a thirty-minute walkthrough and blunt
feedback. No patient data, no credentials to any system, no money now or later, no signup, no email
list. It is a serious offer made in good faith, and the thread found the hole in it immediately.

**What worked.** Three corrections, in ascending order of usefulness. The compliance one came first
and loudest: in healthcare the paperwork does not care that you asked for redacted documents, and a
security review can end the conversation regardless of what you promised not to collect. The second
was about scope — one clinic's awful workflow may be that clinic's, not the market's, so confirm the
pain exists across several practices before you build around one. The third is the one that
generalises past healthcare. As one reply put it, the part that breaks "isn't your list of what you
won't take, it's free itself." A free build needs an exit condition defined before it starts: pick a
single workflow, baseline the staff minutes and the rework it currently costs, and name the number
that converts the pilot into a paid rollout. Without that, "they used it" is the outcome, and "they
used it" is not validation — it is a custom project you now maintain for nothing.

**The lesson.** Free removes the buyer's risk and, along with it, the only signal you were trying to
buy. If you are going to give the first build away, give away the money and keep the measurement:
agree the metric, the baseline, and the threshold up front, in writing, with the person who would sign
the eventual contract. Otherwise you have not run a pilot, you have volunteered. *(via a founder
thread on r/Entrepreneur)*

### 16. The deal is not done when they sign, it is done when they pay

**The pain.** You closed the enterprise logo. It is on the site, it is in the deck, it is in your MRR
number. Ninety days later the money still has not arrived and you are drafting an email you do not
want to send.

**The struggle.** The default collections process is a ladder everyone builds and nobody questions: a
polite reminder at thirty days overdue, a firmer one at sixty, an uncomfortable phone call at ninety.
An operator who had compared companies that actually shortened their cash cycles pointed out that the
ones who fixed it were doing almost nothing at the overdue end and quite a lot earlier — escalation
terms written into the contract rather than just "net 30", the accounts-payable contact captured at
signing, and reminders sent two days *before* the due date, which read as helpful admin rather than as
a collections call.

**What worked.** The replies both sharpened and partly overruled that. Enterprise legal will redline a
late-fee clause on sight, and large buyers run on their own batch cycle that no escalation language
bypasses. Vendors often get set up on net 90 automatically under standard corporate terms, so the
terms you negotiated are not necessarily the terms in their system — you have to ask them to change
it. But the correction that reframes the whole problem came from someone who had spent years on the
buying side: enterprises almost never decide not to pay you. The invoice fails a silent validation
step — no purchase order, a PO value that does not match, the wrong cost centre, a vendor record never
finished on the master file — and, as they put it, "the invoice just drops out of the run and nobody
tells you." Which makes the highest-leverage item on the original list the least dramatic one: getting
the right AP contact, because everything else only works once the invoice is landing in an inbox
where a human sees it.

**The lesson.** Late payment is usually a data problem wearing the costume of a relationship problem.
Before you chase, verify the boring things: correct PO, matching value, right cost centre, completed
vendor record, invoice addressed to accounts payable rather than to the person who liked your demo.
And treat payment behaviour as part of qualification — a buyer who fights hard over what happens on
day thirty-one is telling you something about day thirty-one. *(via a founder thread on r/Entrepreneur)*

### 17. Referral growth hides the absence of a marketing engine

**The pain.** The company has grown steadily for years without ever really marketing. Then growth
flattens, nobody can say precisely why, and the fix everyone reaches for is to hire someone.

**The struggle.** A newly appointed fractional CMO walked into exactly that: a B2B professional
services firm making its first real marketing investment, with one marketing support person, a rotating
cast of contractors on the website, and staff members who had inherited the podcast and the CRM
alongside their actual jobs. Everything to do, strategic and operational, and no established
definition of what the role even covers.

**What worked.** Two observations from the thread are worth more than the org chart discussion. The
first explains the plateau: trust-based businesses grow through referrals and network for as long as
that wave lasts, then stall — because the growth never required them to build trust with anyone who
had not already met them, so no engine exists for the people who have not. The work is not campaigns;
it is becoming legible and credible to strangers who have the exact problem you solve. The second is
operational and applies to any founder making a first marketing hire. With one support person and a
handful of contractors, every piece of work routes through the new hire to be briefed and approved,
and nothing moves on the days they are not there — which, for a part-time or stretched hire, is most
days. The recommended fix is uncomfortable and early: push the support person into owning intake and
contractor briefs sooner than feels safe, and keep the senior person on the review end. Skip it and
"the small team quietly turns you into a coordinator," and the strategic half of the role never gets
any hours at all.

**The lesson.** Referral-led growth is real growth, but it is not evidence that you can acquire
customers — it is evidence that people who already know you will vouch for you. When it plateaus, the
job is not more of the same activity, it is building the first channel that reaches people with no
prior connection to you. And when you hire for that, design the approval path before the first
project, or you will have bought strategy time and spent it on briefs. *(via a founder thread on
r/marketing)*

### 18. The platform optimises for whatever event you report

**The pain.** The leads are arriving, the bookings are getting made, and the calendar still looks
empty on the day. You are paying for every step of a funnel that quietly falls apart at the last one.

**The struggle.** A marketer at a med spa put real numbers to it: roughly 100 leads produced about 40
bookings and only 10 to 12 arrivals. The obvious diagnosis — nobody is reminding them — did not apply.
They had a call centre phoning every lead, an SMS at booking, another two days before, and a call on
the morning of the appointment. The apparatus was complete and the arrival rate was still under a
third of bookings. Commitment devices were the natural next move, but the CEO would not implement
deposits, and this is a business where half of revenue already comes from offers and discounts on a
ticket that still runs into the thousands.

**What worked.** The thread's most useful answer was not about reminders at all. The ad platform is
optimising toward the last event you report to it, and they were reporting leads — so it was
faithfully finding them people who fill in forms. Sending offline conversions back, so the campaign
optimises for arrivals rather than form fills, changes what the algorithm is hunting for. Two
supporting moves came with it. Raise commitment in a way the CEO will accept: if a deposit is off the
table, test a prepay-for-the-first-visit offer and frame it internally as a test rather than a policy.
And check the top of the funnel for fake bookings from click-fraud bots — they had added one-time-code
verification, which is the right instinct, because a no-show that was never a person cannot be
reminded into the building.

**The lesson.** Every step you fail to report back is a step the platform cannot learn from. If your
conversion event is a form submission, you are buying form submissions, and no amount of SMS at the
bottom fixes a target set at the top. Report the event that makes you money — the arrival, the
qualified call, the closed deal — even when the plumbing to send it back is annoying to build.
*(via a founder thread on r/marketing)*

### 19. A new ad platform is not arbitrage until someone proves the audience

**The pain.** A new ad channel opens. The pitch writes itself — get in early, before the auction gets
expensive — and the fear of missing the cheap window is doing most of the persuading.

**The struggle.** A marketer testing OpenAI's ad product on a broad topic reported a $47 CPM over a
month and was already planning to shut it down. The replies were bleaker than the post. One advertiser
spent around $8,000 and said flatly that "the leads were awful", with the campaign as well set up as
it could be. Another ran a three-week pilot, judged the traffic questionable, and stopped. A recurring
theme was mismatch rather than mechanics: several advertisers in blue-collar and B2B categories saw
poor results and suspected the surface skews consumer, and one made the point from their own usage —
the ads they get rarely relate to the conversation they are having. Underneath all of it ran open
suspicion about how many of the clicks were real.

**What worked.** The people handling it sensibly were not the ones who avoided the channel; they were
the ones who bounded it. Budget treated explicitly as test dollars rather than as spend expected to
return. A fixed pilot length agreed in advance. UTM tagging on everything, so that when a sale did
appear they could actually attribute it instead of arguing about it. And asking for cost per click
alongside CPM, because a headline CPM tells you what impressions cost and nothing about whether
anyone moved.

**The lesson.** Early does not mean cheap. It means unmeasured, and unmeasured is a cost you pay in
budget while someone else's data matures. Test new channels — you should be running a small experiment
somewhere at all times — but write down the stopping rule before the first dollar goes in: how long,
how much, and which number ends it. A channel with no proven audience for your category is not an
opportunity you are early to, it is a hypothesis you are funding. *(via a thread on r/marketing)*

### 20. If you cannot reach a human, you are renting the channel

**The pain.** Your largest source of traffic switches off overnight, for a reason nobody will explain,
and there is no one to call.

**The struggle.** A marketer described two weeks inside that situation after their Meta ads account was
restricted for a supposed security breach. Two different restriction notices on two different pages
giving two different reasons. No appeal button where every guide said one would be. More than five
support tickets, each eventually abandoned and marked "Resolved". A chat system too broken to show
conversation history. One agent said the account was restricted for a payment failure and asked to take
payment over the phone; when pushed back on, the response was "oh, you're right, my bad." One agent
promised reinstatement within 24 hours; the next said issues like this take four to eight weeks, and
suggested spinning up a second ads account to keep running — which is a direct breach of the platform's
own terms, and which the agent walked back the moment it was named. A request to escalate was met with
the claim that there was no supervisor. The only thing that produced progress was subscribing to paid
verification for priority support, on top of an annual ad spend already in the tens or hundreds of
thousands.

**What worked.** Partially, two things. Operationally, their agency moved spend to Google and started
running Pinterest while the main account stayed frozen — revenue kept moving because there was
somewhere else to move it to. Procedurally, another marketer in the thread had been restored in fifteen
minutes after being transferred five times, purely by continuing to ask for a specialist rather than
accepting the first-line answer; persistence at the routing layer beat every ticket they had filed.

**The lesson.** Concentration is the risk, not the platform. Any channel where you cannot reach an
accountable human is one you rent, and the rent can be called at any time for reasons you will not be
told. Keep a second paid channel warm enough that it can absorb budget in a day rather than a month,
and keep building the assets nobody can restrict — your list, your site, your search presence, your
direct relationships. And never take the workaround: opening a parallel account to escape a suspension
converts a temporary problem into a permanent one. *(via a marketer's thread on r/marketing)*


---

## Entries — 2026-07-30

### 21. The painkiller test is a search for an existing workaround

**The pain.** You have built something people compliment and nobody urgently needs. Every demo ends
warmly. No demo ends with a signature. Somewhere in the back of your mind you already know the word
for what you have made, and it is "vitamin."

**The struggle.** A founder thread asked the question directly: how do you get from nice-to-have to
can't-live-without, and if you started with a vitamin, what told you? The answers that were no help
were the ones about asking customers what they want — as one reply pointed out, people will list a
million things they would like and never mention the one they are actually paying to work around. The
answers that were useful all described the same failure mode from the inside. One founder knew they
had built a vitamin when leads kept saying "looks cool, but we don't need it right now." Not a
rejection, not an objection you can handle. Just a sentence that means the problem is real enough to
recognise and not expensive enough to fix.

**What worked.** The sharpest test in the thread has nothing to do with enthusiasm. Look for whether
someone is already paying for a bad version of the fix: a spreadsheet somebody rebuilds every Monday,
a contractor doing the job by hand, a step in the process that exists only because the problem does.
That workaround *is* the pain, and it has a cost you can point at in a proposal. Where there is no
workaround at all, people have quietly decided they can live without it, and no amount of explaining
the value moves them. Two variants of the same signal came up repeatedly — someone ranting unprompted
about how a thing sucks, and the budget-review version: the painkiller is whatever keeps somebody from
being paged at two in the morning, and everything else gets cut. The founder who had lived through it
fixed it by switching from a general capability to automating one manual bottleneck their buyers hit
every single day.

**The lesson.** Do not score demand on how interested people sound. Score it on evidence of spend —
hours, headcount, contractors, subscriptions to something worse. And when you find no workaround
anywhere, take the thread's best piece of advice seriously: change who you are selling to before you
change what you have built. The same product often becomes a painkiller one segment over.
*(via a founder thread on r/Entrepreneur)*

### 22. The first thousand dollars is a signal, not permission to scale

**The pain.** You finally have money in the account. Real strangers paid you. And now every instinct
you have is screaming to pour everything into more traffic, right now, before the moment passes.

**The struggle.** A team described the month before that moment honestly: no users, no sales, a
landing page, a raw pitch, no polished product. They spent roughly two weeks turning the idea into
something usable, listed it on an early-stage software marketplace, and crossed a thousand dollars in
sales about two weeks after that. What is worth copying is not the marketplace. It is that they ran 64
async and live conversations — founders, operators, go-to-market people, developers — before trying to
scale anything, and the interviews were about specific daily work rather than "productivity": what
interrupts you, where you lose the thread, how you recover today, which tools your workflow is
scattered across, what still feels unresolved. Distribution was entirely manual: Reddit, X, LinkedIn,
one-to-one conversations inside their own network. No cold email, no automation, no audience. The first
purchases came from conversations, not from reach.

**What worked.** The decision they made next is the reason the story is here. They already had more
channels prepared and chose not to open them, because pushing traffic into weak retention just
multiplies the leaks. Instead they stopped on activation, first-session value, repeat usage, product
accuracy, and friction. The launch had also quietly changed the questions they were asking themselves.
Before it, the question was always "what else should we build?" After it, the questions became why
this specific person bought, why that one stopped coming back, and where the product fails to create
value fast enough. Those are answerable questions, and answering them is cheaper than buying traffic.

**The lesson.** First revenue tells you the pitch can land. It does not tell you the product holds.
Those are separate proofs, and they fail for different reasons, so treat a first thousand as a signal
worth investigating rather than a mandate to spend. And do the interviews before you need them — sixty
conversations about how people actually spend their Tuesday will hand you positioning, priorities, and
your first buyers, all from the same effort. *(via a founder thread on r/startups)*

### 23. A launch to the wrong crowd is not a verdict on your product

**The pain.** You launch on the site everyone launches on. Forty-three people visit. Nobody signs up.
You open your landing page and start rewriting the headline.

**The struggle.** A founder posted exactly those numbers — a launch, 43 visitors, zero signups — and
then did the more valuable thing of explaining why the number was meaningless. Their users are
WordPress plugin developers. The audience on the platform they chose is founders and early adopters.
Almost no overlap. They picked it, in their own words, because it is the default thing you do, not
because their people were there. Two structural problems compounded it: no audience going in, and no
votes in the first hours, which means never surfacing in the feed at all, which means the launch may
as well not have happened.

**What worked.** The founder ran the arithmetic before touching anything. At a normal signup rate of
one to three percent, 43 visitors predicts under one signup. Zero is the boring outcome, not a
finding. Rewriting the landing page off that data would have been optimising against noise. There was
a second, sharper catch. A flattering comment praised how the tool handled annotation placement on a
messy dashboard screenshot; the founder checked the database and that person had never registered, so
they could not have used it — they were reacting to the gallery images. Their conclusion is a rule
worth stealing: "Check your own data before you believe a compliment." The plan that replaced the
launch is unglamorous and correct — go where plugin developers actually gather, and use the tool on
their own plugin so there is something real to show instead of a pitch. One reply supplied a
comparable data point from a single well-chosen community post: several thousand impressions, over a
hundred clicks, three signups.

**The lesson.** Section 11 argued that a launch is an event rather than a channel. This is the finer
version: a launch to the wrong crowd is not even an event, it is a null experiment, and null
experiments cannot be interpreted. Before you change anything in response to a bad launch, check two
denominators — how many of the right people saw it, and how many visitors a real conclusion would
require. Absence of evidence and evidence of absence look identical on a dashboard and mean opposite
things. *(via a founder thread on r/micro_saas)*

### 24. Traffic is not a funnel, it is the top of one

**The pain.** The numbers finally move. Hundreds of visits, thousands of requests, the graph pointing
the right way. Then you open the registrations table and the honest total is single digits.

**The struggle.** A founder nine days into a launch had 159 unique visitors and nearly four thousand
requests in one day, and eight registrations to show for it. The first thought was the one everybody
has in that seat: maybe nobody wants this. The default response to that thought is to go build another
feature, which is both more comfortable than the alternative and completely unrelated to the problem.

**What worked.** Instead of building, they spent an evening reading logs, and found two things. The
signup flow asked founders a pile of questions before letting them do anything — as they put it, the
product was optimised for collecting context instead of delivering value. And a registration bug was
outright blocking some users from finishing. Both were fixed the same evening. Their own summary is
the load-bearing sentence: "traffic doesn't matter if your onboarding leaks users." Worth noting the
thread also surfaced a live risk in their setup — the product is free while they watch usage, with
pricing deferred, and a commenter pointed out that a free tool with credits or model calls behind it
needs limits in place before abuse finds it, not after.

**The lesson.** When conversion is bad, resist the two most attractive explanations — no demand, or
not enough features — until you have watched the path yourself. Every question you ask before the
user has felt anything is a toll gate on a road they have no reason to trust yet. Reading the logs for
one evening is unglamorous work that regularly beats a week of building, because it tells you where
people stopped rather than what you wish they had wanted. *(via a founder thread on r/micro_saas)*

### 25. Do not buy demand you cannot serve

**The pain.** The product is live, the store listing is approved, and the only advice anyone has for
you is to start advertising. You also happen to know that if the advertising works, the whole thing
falls over.

**The struggle.** A solo founder shipped a news-aggregation app that assembles a personalised audio
briefing, after about three weeks in app review — a fortnight for the first pass, then 24-to-48-hour
turnarounds on minor fixes. Their plan was a development-story blog to a professional network of
around 1,200 connections, some paid advertising later, and a target of roughly 500 trial users
converting to 100-200 paid within two to three months. But they were candid about a hard ceiling:
the infrastructure is compute-heavy, and past about a thousand daily users it needs somewhere between
ten and twenty thousand dollars of hardware. They did not want to explode.

**What worked.** The most useful reply in the thread refused the framing entirely: this is not an
advertising problem yet, because paid ads buy volume and volume is exactly the thing the hardware
cannot serve. The lever that pays off first at this stage is creative quality and audience precision,
not spend. A second reply went after the number that actually decides the outcome — what is the moment
someone realises this is what they wanted? — and the founder's own answer named the real constraint:
about five minutes from first launch to the first briefing arriving, because the audio takes two to
three minutes to generate. That is the conversion problem. No ad budget survives a five-minute wait
for first value. Two other corrections landed alongside it: the app had been live less than a day, so
there was nothing to conclude yet, and if a few hundred people did land on the listing and nobody
started a trial, that would be a messaging problem on the listing rather than an acquisition problem.
And the 500-trials target is funnel arithmetic, not motivation — work backwards through it or it is
just a wish with a deadline.

**The lesson.** Capacity is part of go-to-market strategy, not an engineering detail downstream of it.
If your unit economics or your servers cap you at a thousand users, precision beats volume and every
dollar belongs in the first-run experience rather than the ad auction. Find the exact moment a user
first feels the product work, measure how long it takes to arrive, and treat that number as your
growth constraint — because it is. *(via a founder thread on r/Entrepreneur)*

### 26. The first customer paid, then cancelled the same afternoon

**The pain.** Months of wondering whether anyone will ever pay, and then someone does. A few hours
later, before you have finished telling anybody, the cancellation email arrives.

**The struggle.** That is a real sequence, described by a founder whose browser extension pulls
colours, fonts, shadows and variables off any site and exports them as design tokens. First ever
subscriber. Cancelled hours later. The reason given was that it was too expensive — for a price under
four euros a month, less than a coffee. Taken at face value, that reason makes no sense, and taking it
at face value is how founders end up cutting a price that was never the problem.

**What worked.** The founder's reading is more interesting than the churn. This is a tool you open for
thirty seconds, take what you need, and close. A recurring monthly charge sits badly against that
rhythm, not because the number is large but because next month you are paying for a month in which you
may not open it at all. "Too expensive" was probably a proxy for "I do not want a subscription to
this." So the response was not a price cut but a change in which option gets promoted: push the
lifetime licence for an intermittent-use tool and let the subscription be the side door. Worth being
precise about the epistemic status here, because the founder was — this is one customer. It is a
hypothesis with a sample size of one, and they said explicitly they were not changing pricing off a
single data point. What it earns is a test, not a rewrite.

**The lesson.** Price the shape of the usage, not the size of the number. Software people open once a
quarter, or once per project, fights a monthly bill no matter how small it is, because every renewal
is a fresh decision about a thing they are not currently using. Lifetime deals, credit packs, and
per-project pricing exist for that pattern. And when a customer gives you a reason, treat it as a
pointer rather than a diagnosis — the stated objection is rarely the real one, and the useful move is
to ask what the price is being compared against. *(via a founder thread on r/micro_saas)*

### 27. In B2C there is no list to buy

**The pain.** Every piece of go-to-market advice you can find assumes you are selling to companies.
You are not. Your users are individual people, and none of them are on a sales prospecting platform.

**The struggle.** A founder building a consumer micro-SaaS named the asymmetry precisely: LinkedIn
outreach, prospecting tools, cold email and networking all make sense when the buyer is a business,
and none of them translate when the buyer is a person deciding something small about their own life.
The B2B playbook is well documented because it is mechanical — a list, a message, a follow-up
sequence. Consumer acquisition has no equivalent object to work through, which is why founders in this
position often end up doing the B2B motions badly instead of doing something else well.

**What worked.** The replies converged on the same substitution: where B2B uses a list, B2C uses a
surface. Show the product working, in public, in the places where the behaviour already happens. One
founder said their first thousand customers came from Reddit — posting the actual interface and what
it does, rather than a pitch — then reused the same material on short-video platforms, summed up as
create one video and use that everywhere. Others pointed at the same mechanic from different angles:
study what competitors are already doing on those platforms and replicate the format; identify where
your specific user gathers and show up there daily rather than broadly. And a developer-tool founder
in the thread found their users in a developer community on X, which is the same rule applied to a
narrower audience. Underneath all of it sits the definition that makes any of it work — one founder
described their audience not by demographic but by behaviour: people who struggle with impulse buying.
That is a targetable description. "Consumers" is not.

**The lesson.** In consumer software, the artefact that does the work is a demonstration, not a
message. Make one honest piece of material that shows the product solving the thing, put it where the
behaviour already occurs, and repost it across every surface that will carry it — the cost of the
second placement is nearly zero. And define your user by what they do, not who they are; "people who
rebuild the same spreadsheet every Monday" can be found, and "small business owners" cannot.
*(via a founder thread on r/micro_saas)*

### 28. Security arrives before the demo is even useful

**The pain.** You are deep in a good conversation about the workflow, the integration, the thing their
team wants changed. Then somebody in the room asks where their data goes, and you hear yourself
improvising.

**The struggle.** A founder selling into larger software companies described the pattern: the security
review starts far earlier than founders expect, and a fuzzy answer can end the opportunity while you
still think you are in the product discussion. It is worse for anything with AI attached, because the
genuinely useful version of the product needs context from the customer's own system — which endpoints
exist, what fields they return, which roles can see which objects, which workflows the buyer wants to
change. The buyer hears "AI" and pictures their customer records being copied into somebody else's
platform. As the post concedes, they are sometimes right to worry, because plenty of tools are vague
on exactly this point.

**What worked.** The move is to replace reassurance with a boundary specific enough to be inspected.
In their case: the tool reads API shapes and schemas rather than records; whatever it generates runs
under the customer's own permissions; customer data never leaves the customer's environment; the model
never needs to see the records in order to build the mapping. Four claims, each one either true or
false, each one something a security team can actually evaluate. Their summary of why that changes the
conversation is the line to remember — "Security can review an architecture boundary." Vibes are not
reviewable. Two replies added the commercial half of it: if you touch customer data at all, raise the
boundary before you are asked, because volunteering it reads as confidence while waiting to be asked
reads as something you were hoping to avoid.

**The lesson.** Treat the data boundary as positioning material, not compliance paperwork. Write the
four or five sentences that describe exactly what your system reads, what it stores, where it runs and
under whose permissions, and put them in the deck, the docs and the second call — before the security
questionnaire arrives. In enterprise software the reviewable answer beats the reassuring one every
time, and specificity given voluntarily is one of the cheapest forms of credibility available to a
small company. *(via a founder thread on r/startups)*

### 29. Every buyer wants their own version of the same screen

**The pain.** The reporting screen was finished months ago. Now every larger deal arrives with a
polite list of changes to it, and each one is small enough that saying no feels unreasonable.

**The struggle.** A founder laid out how it creeps up. The first dashboard is obvious and works for
the first few customers. Then bigger buyers start asking for their version: split this by country and
city, let the account manager see only their own accounts, save a view for the Monday meeting, put the
fields finance cares about in the export, hide the parts their team will never use. None of these is a
large feature. Collectively they turn the default dashboard into a guess the product team made six
months ago. Both obvious responses fail. Letting every request become a one-off report buries customer
success in small changes and leaves product with no idea which asks repeat. Answering "wait for the
roadmap" keeps the product clean and leaves the buyer without the view they need to run the workflow
they are paying you for.

**What worked.** The thread produced an unusually clean operating rule, and it is not about customer
size. Let the customer-facing team create saved, customer-specific views — but log the request
underneath, so that five customers asking for the same split becomes a product decision instead of
five tickets. Then draw the line by cost of change rather than by who asked: anything that is a
filter, a saved view, or an export becomes a configuration option even if only one customer wanted it,
because configuration is cheap to carry. Anything that needs an engineer to touch code — a new data
source, a new join, an external system, a genuinely different workflow — gets scoped and priced as its
own integration and tracked separately from the roadmap. As one commenter put it, mixing those two
categories is what turns customisation into technical debt, not the customisation itself. Several
people also advocated the blunt version for anyone who is not selling a reporting product: one
dashboard for everybody plus a very good export, and let the customer slice it in the tool they
already use.

**The lesson.** Customisation requests are not a nuisance to be minimised; they are the highest-quality
demand signal you will ever receive, arriving pre-attached to a buyer with money. The discipline is
sorting them: cheap-to-clone stays a saved view forever, engineer-required graduates to product or
becomes a priced integration, and repeated requests always beat loud ones. Track the underlying ask,
not the ticket. *(via a founder thread on r/startups)*

### 30. The temporary feature needs an expiry date before it needs code

**The pain.** A deal is sitting on one missing capability. Building it properly is a quarter of work.
Building a version that gets you through this one account is a week, and everyone in the room can see
it.

**The struggle.** A founder asked whether people build a temporary feature to buy roadmap time, and
the answers were near-unanimous in a way that is worth noticing: nobody thought the code was the
problem. The failure is always governance. One operator described maintaining exactly such a feature
for years because the account was large and nobody wanted to risk it, with the corollary that
customers form their workflows around your product's limitations, so the thing you built as a bridge
becomes load-bearing for someone. Another named the deeper trap plainly — far more B2B startups get
stuck maintaining custom work they convinced themselves was temporary than are ever hurt by saying no,
and "sales wants sales" is not a reason to commit engineering to something outside the roadmap.

**What worked.** Section 7 covered how to sell a capability you have not built yet. This is the other
half: how to build one without it quietly becoming permanent. The thread's conditions, in order of how
often they came up. Give it an expiry date and a named owner *before* anyone promises it to a customer.
Write down what gets reused, what stays manual, what the support ceiling is, and the date on which it
either folds into the core product or gets switched off. Contain the blast radius: one feature flag,
one customer identifier, a thin adapter — never a customer-specific branch, and never let it touch
shared onboarding, billing or reporting until a second customer asks for the same thing. Keep it
commercially separate, as a paid pilot with an acceptance test and an explicit support limit, and never
let it appear in the standard product commitments. Two tells that it has stopped being temporary: sales
starts demonstrating it as a normal feature, and nobody owns the decision to promote it or kill it.
One commenter's summary is the whole section in a line: the smell is not temporary code, it is
temporary code with no exit condition.

**The lesson.** "Temporary" is a claim about the future, so it needs a date, an owner and a kill
switch, or it is just a word you said in a meeting. Charge enough that the workaround is visible in
somebody's budget, keep it structurally easy to remove, and decide up front what evidence would earn
it a place in the product. Do that and the occasional bridge is a legitimate sales tool. Skip it and
your roadmap slowly becomes a maintenance contract for deals you closed two years ago.
*(via a founder thread on r/startups)*
