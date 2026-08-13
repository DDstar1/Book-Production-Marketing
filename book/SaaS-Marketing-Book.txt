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

## Entries — 2026-07-30 (second batch)

### 31. The client asks for a channel, but nobody wants a channel

**The pain.** They arrive knowing exactly what they want to buy. They want SEO. They want paid social.
You can see within twenty minutes that it is the wrong instrument for their problem, and when you say
so, they go somewhere that will just do it.

**The struggle.** An agency owner described the loop in almost exactly those terms, and the
frustration in the post is the useful part: they are technically strong, they can see the mistake
coming, and telling the truth costs them the account. The two available moves both end badly. Refuse,
and lose the work to whoever will nod. Comply, and run a campaign you already know will underperform —
at which point the failure is filed under your name anyway, because you were the marketer in the room.
Being right and unhired is not a strategy, and being paid for work you predicted would fail is not one
either.

**What worked.** The thread's best reply reframed the whole problem in two sentences: "Clients don't
actually want SEO or Meta ads. They want more customers." The channel was never the purchase. It is a
guess the buyer made about how to reach the outcome, and guesses can be discussed without anyone being
contradicted. So you stop arguing about the instrument and start agreeing loudly about the destination
— restate what they are actually trying to achieve, get them to confirm it, and only then put their
channel and your channel side by side as two routes to that same agreed number. Two commenters added
the practical constraint. Education has a ceiling: past a certain point, correcting a buyer's
understanding of marketing reads as an attack on their judgement or as evidence you have misunderstood
their business. So frame it at the level they are at now, in their vocabulary, and let the first
month's data make the argument you were not allowed to make out loud. Bring numbers, not opinions —
back the claim with why this route reaches the outcome and their route probably does not.

**The lesson.** Never negotiate about the channel. Negotiate about the outcome, then treat every
channel — theirs and yours — as a testable hypothesis about how to get there. It converts a
disagreement about your expertise, which you can only lose, into a shared question about evidence,
which you can win in four weeks. This is the same discipline the whole book keeps circling: sell the
result, describe the mechanism only as far as the buyer needs it.
*(via a founder thread on r/marketing)*

### 32. Two channels, five hours a week

**The pain.** You have a full-time job and a product on the side. Every credible source says do
content and do ads, and you have enough hours in the week to do roughly one of them badly.

**The struggle.** A founder building a sports-travel site while employed full time took the question
to a government-backed business consultant, who advised running paid ads and posting on social at the
same time. Reasonable advice in the abstract, useless against the actual constraint. Their instinct was
ads-only, and the reasoning was honest: ads run while you sleep, so the hours go into the site
instead. Content has no such property — it expands to fill whatever time exists, and for someone with
five or six spare hours a week it can consume the entire allocation and still look unfinished.

**What worked.** The replies split, which is itself informative, but they converged on a sequence
rather than a split. The sharpest line in the thread is the one to keep: "Don't pay to amplify a
message you haven't validated organically yet." Ads buy speed, not judgement — they cannot tell you
which message deserves scaling, and if the landing page is not already converting, a bigger budget
just moves more people past the same broken page. So the practical shape most commenters landed on was
a time-boxed loop: one batch of sixty to ninety minutes a week producing two or three posts around a
single question or destination, then take whatever language actually earned replies, saves or email
signups and put *that* into the ad copy. Keep a small paid test running only if you can track
something beyond clicks, and review both channels at four weeks. One commenter reframed the whole
thing around demand shape rather than channel choice — this is a market where interest spikes when
fixtures and schedules are announced and again a few weeks before the date, so spend belongs in those
windows and the quiet weeks belong to content. The rest of the year, ads mostly burn budget.

**The lesson.** With severely limited hours, do not choose between channels — order them. Organic is
where you find out what to say, paid is where you pay to say it more often, and doing them in that
order costs less than doing both at once. Then look at your category's calendar before your own: if
demand arrives in bursts, a flat annual spend is the most expensive way to buy it.
*(via a founder thread on r/startups)*

### 33. Priced so low that nobody believes you

**The pain.** You have found a genuine cost advantage and priced accordingly. You expected the price
to be the reason people said yes. It has become the reason they say no.

**The struggle.** A developer offering a resale route to well-known AI models posted an offer built
entirely on price — the same named models at roughly a fifth of the published rates, plus free trial
credit and no card required. Everything about the post is designed to remove risk. The first reply was
"20% of price. Scam alert." The second reply was the same objection, phrased politely: at that price,
how is this sustainable without cutting corners? Both commenters had skipped straight past the offer
to reverse-engineer the margin, and neither of them was hostile — they were doing exactly what a
competent buyer does. The founder's answers were reasonable and did nothing, because by then the
conversation was about their credibility rather than their product.

**What worked.** What is worth extracting here is the mechanism, not a fix, because the thread does
not contain one. In a category with a public reference price, a number far below it is not read as a
discount — it is read as evidence of a hidden substitution. The buyer's question is never "is this
cheap?" but "what did they take out?" That is why the post's most-repeated defensive line, a promise
that the routes are not quietly downgraded to smaller models, appears at all: the founder had already
met the objection before, and answering it in advance still did not defuse it, because a claim about
your own honesty is not inspectable. Contrast that with section 28, where four checkable statements
about a data boundary did the work that reassurance could not. The one substantive comment in the
thread points at the same gap from the buyer's side: cost per task was never what stopped them, it was
a route quietly queueing under load while their job sat there timing out. That is the real question
behind "scam alert" — not the margin, but which dimension of service was traded away to fund the
price.

**The lesson.** When price is your entire differentiator, price becomes your credibility problem. A
number the market cannot explain gets explained for you, and the explanation is always that something
was removed. So publish the reason the price is possible in terms a buyer can verify, and compete
explicitly on the dimension they actually fear losing — publish the concurrency behaviour, the latency
under load, the failure modes. Free credit lets someone test whether it works. It never tells them
whether it will keep working, and that is the objection you have to answer.
*(via a founder thread on r/micro_saas)*

### 34. Selling against a free workaround people are already using

**The pain.** Your product does something the buyer can already do for nothing. They know it, you know
it, and every pitch that leads with the capability walks straight into "I already do that with tools I
have."

**The struggle.** A founder shipping a browser extension that summarises YouTube videos in bulk was in
exactly that position, and the post is unusually honest about it. The free path is well known — general
AI assistants, notebook tools, raw transcripts — and they had used it themselves for months. The
capability was not scarce. Two other things in the post matter more than the product. First, the volume:
this was described as one of hundreds of tools they had launched and tested, most of which failed, and
the reason to look at this one is that it got noticeably more traffic. Second, the milestone is $100
MRR, which is small enough that the founder calls it tiny — worth stating plainly, because this is not
a scaling story, it is a story about finding the one attempt that got traction.

**What worked.** The pitch does not sell summarisation. It sells the removal of "the constant copying,
pasting, uploading, and switching between tabs" — the friction of the free workflow, described in the
sequence a user actually experiences it. Then the differentiator is a job the free path cannot do at
all: not summarising one video, but running twenty search results or an entire playlist into one
structured report of recurring points, disagreements and recommendations. That is the whole move.
Where the free tool is merely inconvenient, you compete on friction. Where it stops working entirely
— at volume, in this case — you compete on capability, and that is where the pricing lives. The other
transferable detail is that the winning positioning was found by launching many small things and
watching which one drew traffic, not by reasoning about it up front.

**The lesson.** A free alternative does not disqualify your product; it defines your pitch. Write down
the exact steps someone performs today with the free path, and sell either the compression of those
steps or the thing that becomes impossible when the job gets ten times bigger. Never sell the
capability itself — that is the part they already have.
*(via a founder thread on r/micro_saas)*

### 35. The free tier is the product when one person cannot use it alone

**The pain.** Your product only works when a group uses it. One person signing up and paying achieves
nothing, because the value does not exist until four other people join them.

**The struggle.** A solo developer building a coordination tool for groups planning trips together
named the problem in one line: "traditional PLG assumes single-player value first." Every standard
growth playbook assumes an individual can adopt the product, get value alone, and expand from there.
Here the unit of adoption is a group, and the organiser — the person who would pay — gets nothing at
all until their friends are inside it. The competition makes it harder. There is no incumbent to
displace, only a working assembly of a shared document, a bill-splitting app, a group chat and
somebody's camera roll. Nobody is unhappy enough to switch, but everyone who has organised a group
trip recognises the pain immediately.

**What worked.** The decision the founder made is the interesting one, and it runs against instinct:
make the free tier genuinely useful rather than a crippled trial — two full active trips with generous
photo and document limits, enough for most casual users to finish a real trip inside it. The reasoning
is exactly right for this shape of product. If the free tier is restricted enough to force an upgrade,
it is also restricted enough to stop the group forming, and no group means no value for anyone,
including the person who would have paid. So the free tier stops being a lead-generation trick and
becomes the distribution mechanism itself: the organiser's job is to get four people in, and every
limit you put in their way is friction on your own acquisition. Payment then lands where the repeat
use is — unlimited trips and export, which only matter to someone on their third trip, i.e. the
organiser who has already recruited a group twice. Worth noting what the founder did not claim: iOS is
unbuilt with no promised date, and they said so rather than announcing it.

**The lesson.** When adoption is collective, the free tier is not marketing spend, it is the product's
delivery mechanism, and crippling it costs you the group rather than converting the individual. Charge
for the second and third use, not the first, and identify the one person in the group whose repeat
behaviour you can actually bill — build the paid tier for them and let everyone else in for free.
*(via a founder thread on r/micro_saas)*

### 36. The loss leader whose cost floor somebody else controls

**The pain.** The thing customers want to buy from you is not the thing you make money on. So you
consider selling the popular thing at cost, purely to get the customer in front of the profitable
service.

**The struggle.** A vehicle-repair operator laid this out plainly: demand is for the parts, the money
is in fitting them, and the plan was to resell parts at or below what competitors charge with
installation attached. Every marketer recognises the shape — a loss leader, the free tier, the cheap
hardware that sells the subscription. What the thread supplied was the list of ways it goes wrong for
a small operator, and it is worth reading as a checklist for anyone about to run a free or at-cost
tier. The version that fails is specifically the one described in the post: buying from your
competitors and reselling at their price.

**What worked.** Several commenters converged on the same rule — the store is a customer acquisition
channel, not a profit centre — and then attached conditions. Zero margin is not zero cost: payment
processing fees, returns, warranty exposure and the admin of stock all sit underneath the "no profit"
price, so the loss is larger than the discount and the service margin has to cover the difference,
not merely exist. Inventory is the second trap: at zero markup, dead stock is pure loss, so stock only
what turns over fast and make everything slow a special order or a drop-ship. Third, and the sharpest
point in the thread: if you buy from competitors, your supply chain is controlled by people whose
customers you are taking. "They set your cost floor." The moment they notice, they can price you out
or cut you off entirely, which means the whole acquisition channel exists at a rival's discretion. One
commenter asked the question that reframes it as a product problem rather than a pricing one: what
happens to the warranty when a part you bought at retail fails a month after you fitted it? And the
recommended sequence was to test one narrow category first and confirm people actually take the
upsell, before building the whole storefront.

**The lesson.** A loss leader is a channel, so price it like one and audit it like one: know the true
fully-loaded cost of the free thing, know the attach rate that makes it pay, and prove that attach
rate on a small category before you scale it. Above all, check who controls your cost floor. If the
input to your acquisition channel is bought from a competitor — or resold from a supplier who can
reprice you at will — you do not own the channel, and the day they notice is the day it closes.
*(via a founder thread on r/Entrepreneur)*

### 37. They copied the winning ad, not the forty that failed

**The pain.** A competitor has taken your product, and now the same creative you spent months honing
is running against you in the same ad auction, on the same platform, to the same audience.

**The struggle.** A founder posted from the middle of exactly that, angry and specific: a digital
product and its accompanying tool duplicated, and near-identical Meta ads launched to promote the
copy. The instinct is to make it stop. The thread's experienced voices were consistent that this is
mostly not available — copying arrives the moment you show traction, sometimes from a competitor,
sometimes from a company you were working with, and in one case from an investor who entered due
diligence and launched a rival. What makes it worse than ordinary competition is that your marketing
is public by construction. The ad you are running is visible to anyone who wants to look, which means
your best-performing creative is the most exposed asset you have.

**What worked.** The comment that reframes the whole problem is about what is actually visible: they
"copied the winning ad but not the 40 dead ones" that taught you why it wins. What a competitor can
take is a snapshot. What they cannot take is the process that produced it — the failed variants, the
audience tests, the reasons each one died. So they are stuck maintaining your last good answer while
you move to the next one, and the only way to lose that race is to stop shipping and start defending.
Several people added the same point from other angles: copying is a position behind you, it validates
that the market is real, and if the copycat does something you are not doing, take it back. The
practical instruction in the thread was blunt — ship something they cannot match, then point your own
ads at what is new, because a copycat can only compete on price and price loses to whoever moves
faster. One reply named the durable advantage: talk to your users. They will tell you what they
actually do, which is information a copycat does not have because they have your interface but not
your customers. And an honest caveat, because someone raised it: this all assumes you have the capacity
to keep out-shipping them, which is not universal.

**The lesson.** Your creative is copyable and your test history is not. Treat the winning ad as a
perishable asset rather than an achievement, keep a queue of things a copyist has no way to anticipate,
and put your energy into the two things that do not transfer — the rate at which you learn and the
relationship with the people paying you. Being copied is expensive and infuriating, but it is also the
first solid evidence that what you built is worth having.
*(via a founder thread on r/Entrepreneur)*

### 38. "Ready to sell" is a promise, not a feature list

**The pain.** The demo is beautiful. Customers click through it and nod. And you cannot tell whether
you have a product or a very convincing prototype that will fall over the first time somebody depends
on it.

**The struggle.** A founder building with coding agents described the state precisely: the interface
came together, the flows look right, everyone feels close — and underneath it the architecture
decisions were rushed, the tests are thin, edge cases are guesses, and nobody quite owns the generated
parts, because the agent wrote them. The go-to-market question sitting inside that engineering
question is the one this book cares about: keep selling and clean up later, or stop selling until the
debt is paid. Both answers are wrong as stated, because "ready" is being treated as a property of the
codebase when it is actually a property of what you are willing to promise.

**What worked.** The thread produced two tests far more useful than any completeness checklist. The
first is operational: "Ask whether it can run for a week without anyone watching it." If something
breaks at three in the morning, do you hear it from an alarm or from a customer, and can anyone roll
it back without waking the person who prompted that part into existence? That gap — not feature
coverage — is what separates a demo from a product, and most of it is operational rather than
architectural. The second test is commercial, and it is the one to write on the wall: the line is the
promise you are willing to put in front of a paying user. Which means a thin product can be sold today
provided the promise is scoped to match it — one supported workflow, a recovery path that does not
silently destroy their work, and stated hours when a human will answer. Anything outside that scope is
experimental even though the screen exists. Other commenters supplied the boundaries. Manual onboarding
and production held up by people's goodwill means you are not there yet. Infrastructure is where the
money actually burns, so that is the part worth designing properly while the rest stays scrappy. And
one voice argued there is no line at all, only risk — document it, rank it against the feature backlog,
fix the worst now.

**The lesson.** Do not ask whether the product is finished. Ask what you can promise and still keep,
then sell exactly that and nothing more. A narrow promise honoured beats a broad one improvised, and
the honest scope is also your best qualification tool — the customers who need more than you can
promise today are the ones who would have churned loudly and told everyone why.
*(via a founder thread on r/startups)*

### 39. Distribution first is a real advantage, and it does not set the schedule

**The pain.** Most founders have a product and no way to reach anyone. Occasionally it is the other way
round — you have the relationships, the field engineers and the industry standing, and what frightens
you is everything between "it works on the bench" and "we can ship, install, support and warranty it."

**The struggle.** A founder described that inversion in detail. They already run a company in the
sector that installs and services competing systems, hold granted patent claims, have relationships
with hundreds of potential customer sites, several willing to host beta installations, and technicians
already trained on rivals' equipment. Demand is not the question. Their fear is capital burned in the
gap: tooling, first inventory runs, certification, consultants — all of it potentially spent just
before a hardware revision makes it worthless. They listed the pieces themselves and then named the
actual problem, which is the sentence worth keeping: "knowing the names of all these pieces" is not the
same as knowing their order, their owner, or when it becomes correct to spend seriously on each. The
post drew no replies at all, which is its own small lesson about where to take a question this
specific.

**What worked.** What this story contributes is a market-timing insight the founder states almost in
passing, and it deserves to be the headline. They do not expect customers to rip out working
equipment. They expect them to convert when the incumbent system breaks, becomes obsolete or reaches
replacement age. That single observation determines everything commercial about this business. The
buying window is set by the failure curve of hardware somebody else installed, which means the sales
calendar is not something the company chooses — it is inherited, roughly predictable, and mostly
already visible to a firm that services those units for a living. It also explains why the beta
installations are the highest-value asset in the plan and worth more than any consultant: they are
simultaneously the engineering test that de-risks the tooling spend and the reference sites that make
the replacement conversation easy when each window opens. And the existing service organisation is not
a nice-to-have, it is the moat — it means the switching cost for a customer is nearly zero, because the
people who already maintain their current system would be maintaining the new one.

**The lesson.** Existing distribution is the most undervalued asset in early-stage go-to-market, and it
buys you the one thing money cannot: permission to talk to real buyers before the product is finished.
But it does not compress the sales cycle. When you are replacing installed equipment, work out what
governs the replacement moment — contract end, failure rate, obsolescence, a compliance deadline — and
build the plan around that calendar instead of your launch date. Then use pilots to do double duty:
each one should retire a technical risk and create a reference at the same time.
*(via a founder thread on r/startups)*

### 40. Ask the network for perspective, not for introductions

**The pain.** You have a list of people who might genuinely help — old classmates, former colleagues,
an alumni directory. You draft the message asking for an introduction to a buyer, and it sits there,
because you can feel how much you are asking for.

**The struggle.** A founder working an alumni network for customer access and early pitch feedback
asked what else it is good for, and the replies were more sceptical than encouraging. Shared
institution is a weak tie: unless the school was very small or unusually tight-knit, few people feel
any urgency to help a stranger who happens to share it. One commenter noted that at large public
universities the network barely functions. Another said outreach through alumni channels can read as
the move of someone who could not get traction outside them. And a third raised the constraint that
actually stops most of these messages being answered — in a nervous job market, people are
disinclined to raise their heads for anything that carries risk. An introduction carries risk. It
spends the introducer's credibility on you.

**What worked.** The founder's own reply is the technique, and it is the most useful thing in the
thread. Asking someone to buy, or to introduce you to a buyer, creates pressure; "asking for
perspective usually doesn't." So invert the ask. Instead of requesting access, request their read:
how would you evaluate this pitch, where does the argument fall apart, how does this actually get
bought in your industry. That request costs the recipient nothing they cannot afford, which is why it
gets answered, and it returns something a forced introduction usually does not — the vocabulary buyers
in that sector actually use, the objection you were not expecting, and an honest read on whether your
pitch survives contact with someone who knows the field. Introductions then arrive as a by-product,
offered rather than extracted, from people who have already engaged with the substance and can
therefore vouch for it without risk. One reply asked the right sceptical question, and it is worth
holding onto: how many actually reply? Nobody in the thread knew, which is the honest state of the
evidence.

**The lesson.** Weak ties will spend attention on you but not credibility. Ask for the cheap thing —
their opinion, their read on your pitch, how their industry buys — and let the expensive thing follow
if it earns it. The perspective is frequently worth more than the introduction anyway: an early pitch
usually fails on its framing rather than its access, and a stranger who owes you nothing is the
cheapest place to find that out.
*(via a founder thread on r/startups)*

## Entries — 2026-07-30 (third batch)

### 41. The accidental A/B test between a demo and a signup form

**The pain.** Fifty demos in six weeks, warm feedback on nearly all of them, two closed. The same
product on the website, given a proper run of cold traffic: ten signups, zero cards. It is easy to read
that as a traffic problem, and almost everyone does.

**The struggle.** A founder posted the whole funnel with the numbers attached, which is rare enough to
be worth studying. A directory listing came with ad credit, and the credit bought roughly 234 clicks
onto the site — cheap-looking traffic that was actually running at about $6.78 a click, so the credit
was gone in around 72 of them. Ten people signed up. None paid. The first assumption was the obvious
one: the product is not compelling. Then they looked at where the ten actually stopped, and the shape
was nothing like the assumption. Two left at the first step. One left mid-setup. Five completed the
entire onboarding — source, angle, a written brief about themselves and their voice — and then stopped
dead at the payment screen. Nobody who finished the work entered a card. Those five were not
unconvinced. They had done everything asked of them. They were simply being asked to pay before the
product had done the one impressive thing it does.

**What worked.** The founder named the defect precisely: the aha moment was sitting behind the paywall
instead of in front of it, so the funnel ran do work, do more work, pay, then finally see value. Cold
traffic will not take that trade — you are "converting on faith, and cold traffic has none." The fix
was to let a user run one real project and see actual output before any payment ask, then move the card
to the moment they try to act on that output — schedule it, export it, publish it — which is the point
of peak desire rather than the point of peak effort. The setup brief stayed, but reframed as something
that improves the very next thing you see rather than a toll booth in front of the reveal. And the
detail that turns this from a tactic into a principle is the comparison the founder made by accident.
Why did fifty demos convert and self-serve convert nobody? Because in a demo, the magic is shown before
anyone mentions money. A demo is value-first by construction; that signup flow was its exact inverse.
Same product, same price, same paywall — the only variable that changed was whether value landed before
or after the ask. Two honest caveats from the founder, both worth keeping: at ten signups the
conversion rate is meaningless, and on inspection most of those signups were testers, bots or randoms,
with exactly one real lead in the batch — someone who had seen the product mentioned on LinkedIn.

**The lesson.** If your demo converts and your signup flow does not, stop blaming the traffic and
compare the order of events. A salesperson naturally shows value first and asks for money second; a
signup form, left to itself, does the opposite. Find the single moment your product becomes obviously
worth having, put nothing in front of it, and place the card exactly where the user tries to keep, send
or act on what they just made.
*(via a founder thread on r/startups)*

### 42. Cut the price from $180 to $29 and nothing moved

**The pain.** Sales are zero, so you assume it is too expensive. You discount. Still zero. You discount
again, hard enough that it should be an impulse buy, and it is still zero — and now you have no idea
what you are even testing.

**The struggle.** A web developer took over marketing for a client's single-product physical store and
posted the whole ladder. About $1,500 spent across Meta, Reddit and TikTok over three and a half
months. Real diligence on targeting: interest audiences built around specific buyer types, stacked and
then narrowed from tens of millions down to one or two million with AND conditions, automatic
placements overridden to force feeds rather than Reels. No lookalike audience was possible, because a
lookalike needs seed buyers and the store had none. And the price went from $360 struck through, to
$180, all the way down to $29. Almost nothing moved. At $29 people would not add it to the cart. Their
own conclusion was that the targeting was broken.

**What worked.** The thread's replies moved the diagnosis somewhere more useful, and so did the
founder's own tracking, which is the most valuable thing in the post. Roughly a third of organic
visitors scrolled deep into the page; with paid it was about one in twenty. "Cheap clicks, wrong
people." That single comparison says the traffic was not merely unconverted, it was uninterested — the
paid audience never even read the page. Meanwhile four sales had arrived in three and a half months,
every one traceable to a handful of honest, unpitched posts written in places where the product's
actual users hang out, and one of those produced a sale within a day or two. The commenters were
blunter than the founder wanted. One refused to let the product off the hook — with results like that,
a product problem cannot be ruled out. Another argued the campaign construction, not the targeting, was
the fault: narrowing with AND conditions, forcing placements and laddering the price down were all the
wrong levers, and a small test that lets the platform find the buyers often beats hand-drilled
audiences precisely when you have no customer data to drill with. The price ladder is the real evidence
here, though, and it points one way. If dropping the price by 84% does not move the cart, price was
never the objection. Nobody wanted it at any price, or nobody who saw it was a buyer.

**The lesson.** Discounting is a test, so read it like one. When a large price cut produces no change in
behaviour, you have proved that price is not the constraint, and every further cut just destroys margin
while you look for a problem that lives somewhere else — the audience, the offer or the product. Before
spending on paid, get the engagement signal from a channel that already works: if a third of organic
visitors read your page and one in twenty paid visitors do, that ratio, not the cost per click, is the
number telling you whether you have bought attention or just impressions.
*(via a founder thread on r/marketing)*

### 43. Sixty stores, one customer

**The pain.** You have the thing everyone says is impossible. Your product is on the shelf in a national
chain, in dozens of locations, in two countries. And you are still, in the only sense that matters, a
one-customer business.

**The struggle.** A family running a premium home-fragrance brand described exactly that position: 60+
locations of a major grocery chain plus a few independent boutiques, and that chain is their biggest
customer by an enormous margin. The plan was to expand into other retail — the large lifestyle and
homeware chains — and outreach to those buyers had produced nothing at all. Direct sales through their
own store were possible but structurally worse: domestic shipping costs made them far less profitable
per unit than wholesale, which pushes the business back towards the very concentration it is trying to
escape. The economics themselves are healthy at the unit level, around $10 of margin on a $15 retail
price. The risk is not the margin. It is the denominator.

**What worked.** The thread's most-upvoted replies were unusually direct and they converge on one
diagnosis. First, the concentration itself: a business whose revenue depends on a single buyer is worth
much less than its revenue suggests, because the day that buyer delists you is the day the business is
worth close to nothing — one commenter's conclusion was that if the goal is retirement money, selling
now is the honest option. Second, and more useful for anyone earlier in the story, several people
pointed out that landing the whale first sets a false expectation about how the rest of the market
works. It looks like the hard part is over. It is not; the remaining chains are each a long, individual
acquisition, and there is no strategy in waiting for more whales. Start smaller, where the decision
cycle is short. Third, the sharpest reframe: a buyer's fear is not whether your product is good, it is
whether it will sit on their shelf, so to get stocked "you need to demonstrate that they'd be stocking
a product they won't be stuck with." That turns the whole problem from a pitching exercise into an
evidence exercise, and it explains why the direct-to-consumer channel matters even at thinner margins —
online demand and sell-through data in specific regions is precisely the proof a new buyer wants. One
commenter described a brand that could not get picked up anywhere without an online presence, and was
eventually taken online-first with in-store placement held back pending sales volume. That is the
sequence, and it also answers the shipping-cost complaint: the direct channel's job is to produce
evidence and a customer list, not only per-unit profit.

**The lesson.** Distribution is not the same thing as demand, and one retailer is not a channel — it is
a client with a termination clause. Treat every large account as concentration risk from the day you
win it, and spend the good years buying independence: a second and third route to the same customer, a
direct channel you own, and above all sell-through data. Shelf space is granted by buyers who fear dead
stock, so the asset that opens the next chain is not a better pitch deck, it is proof that your product
leaves the shelf on its own.
*(via a founder thread on r/marketing)*

### 44. The producer needed a calendar, not your story

**The pain.** Press coverage feels like a lottery run by people who never reply. You write to a
journalist about how interesting your company is, and nothing happens, and the conclusion you draw is
that you need a bigger budget or a connection.

**The struggle.** A publicist posted the mechanics behind a free television segment — their fortieth
placement for a client — and what makes it useful is that the client's story was, on paper, no easier to
sell than anyone else's. A non-profit whose founder appears in costume as a comic-book hero, raffles
themed cars, and gives the proceeds to a charity that sends costumed visitors to sick children. That is
either a great segment or an unanswered email, and the difference is not the story's quality. It is
whether it arrives as a finished thing a producer can put on air.

**What worked.** Four things did the work, and they generalise past PR entirely. First, timing: the
segment ran close to a major comics convention, and the local stations were already running related
stories, which the reporter mentioned as a positive. The story did not have to create interest; it
attached to interest that already existed on somebody else's calendar. Second, the pitch was built like
a product rather than a request — a headline framed as a story idea, a summary, images, links, contact
details, all in one place. Third, the reach was systematic rather than hopeful: a press release issued
nationwide and a purpose-built list of media contacts covering that theme, which will keep producing
placements after this one. Fourth, and the step commenters singled out as the one most people skip, the
response to the reporter was immediate and consisted of asking exactly what she needed for the segment
and then supplying precisely that. A commenter put the underlying principle better than the post did:
the story was already halfway built before the pitch went out. Another added the working constraint
from the producer's side — the reliable pickups pair a calendar beat with something visual, because
producers need both, quickly. And one asked the fair sceptical question, which nobody answered: how
often does the timing hook carry it versus the pitch simply being good?

**The lesson.** Earned media is not a favour you request, it is a piece of work you deliver to someone on
a deadline. Find the beat already in their calendar — a season, an event, a regulation, an anniversary —
and attach to it rather than competing with it. Then hand over a complete, visual, ready-to-use package
and answer follow-ups within minutes with exactly what was asked for and nothing else. The same
instinct works far outside journalism: newsletters, podcasts and conference organisers are all people
with a slot to fill and no time to build your story for you.
*(via a founder thread on r/Entrepreneur)*

### 45. Twenty users, none of them evidence

**The pain.** You are paying for your users. Every month the bill for their usage lands on your card,
and every month you tell yourself it is buying traction — but you cannot say which of those people
would still be there if the meter were running on them instead.

**The struggle.** A founder running a private beta laid the situation out plainly: about twenty users on
an AI product, model usage given away free, roughly $350 a month burned. The access has not been
pointless — two conversations about larger pilots came out of it, which is a real result and the reason
they were reluctant to change anything. The question they asked was whether to charge at least the cost
of usage and watch who leaves. What makes this a marketing problem rather than a finance one is what
the free access is doing to the information: with nobody paying, twenty active users tell you nothing
about demand, and the burn buys attention rather than evidence.

**What worked.** The thread was close to unanimous — charge now, at least at cost — and the reasoning
was consistently about signal rather than revenue. The best statement of it: charging the token cost
will not make money, but it "tells you who's actually using it vs who signed up because it was free,"
and the worst case is losing people who were never going to pay. The corollary matters just as much:
those two pilot conversations are the real signal, and eighteen free accounts are not. Several people
supplied the mechanics for doing it without torching goodwill. Set an end date for free usage rather
than changing terms overnight, and before it arrives show each user what their own last seven days
actually cost — which converts an abstract price into a number they have already consumed, and is far
more persuasive than any pricing page. Offer a paid month with a hard usage cap so nobody fears an
unbounded bill. Keep the large pilot conversations on separate written budgets, so one heavy pilot
cannot eat the allowance meant for self-serve users. On the cost side, the suggestions were to reduce
the exposure structurally — cheaper or local models where quality permits, or letting customers bring
their own key so usage stops being your liability at all. One dissent deserves recording, because it is
legitimate: unsustainable pricing is a defensible way to buy early customers if someone is funding the
burn deliberately and there is a real plan for reaching the price you eventually need. The failure mode
is not subsidy, it is subsidy without an end date. And one commenter suggested passing off a cheaper
model as an expensive one, which is worth naming only to reject: the moment your pricing depends on the
customer not knowing what they are getting, you have a fraud rather than a business model.

**The lesson.** Free users are a cost centre that produces no information. The first price you set is not
mainly a revenue decision, it is the cheapest market-research instrument you will ever own — it sorts
the people with the problem from the people with an account. Charge at cost if you must, but charge
something, put an end date on any subsidy from the day you start it, and remember that a small number
of buyers is a stronger result than a large number of guests.
*(via a founder thread on r/startups)*

### 46. When a weekend can rebuild your product, the product is not the moat

**The pain.** A year ago there were a handful of competitors and they charged real money. Now five new
tools launch in your space every day, the ones charging hundreds a month have cut their prices or
pivoted, and somebody can approximate your app in a weekend. Every conversation turns into a price
conversation.

**The struggle.** A founder eleven months in described exactly that collapse and its effect on plans:
the original sequence was to onboard a few clients and then launch a platform, and the industry caught
up while they were still working through step one. The thread agreed on the diagnosis without much
sympathy for the framing. The blunt version, and the most-upvoted comment: if somebody can rebuild your
product in a weekend, you never had a moat. Another pushed back on the premise itself — a race to the
bottom is what happens to products shipped without a market, and the real problem is more often a
founder unwilling to put a value proposition in front of a customer than an oversupplied category.
Both are right in a way that matters commercially: cheap and copyable is a positioning outcome, not a
market condition you were handed.

**What worked.** The founder's own answer is the interesting part, and it emerged from the one activity
they said had been a cheat code all year — talking to customers, who "write their pitch for you."
Repeated contact with buyers had shown them where the durable ground was: the moat is knowing the
customer's business better than any dashboard can show, which is a form of value that cannot be
regenerated from a screenshot. That leads to a concrete commercial position — serve customers at agency
prices with software-shaped costs — and to a deliberate preference the founder stated as a trade they
would happily make: one client worth twenty subscriptions, embedded in their operation, over two
hundred subscribers who churn the moment somebody launches the same thing for $10 less. Commenters
extended it the same direction from different angles: the sell is the outcome and the workflow you own
alongside the client, not the capability; and in the enterprise segment the differentiator becomes the
ability to sell rather than the feature list. Worth stating the cost honestly, because the thread did
not: this position is slower, less leveraged, and much harder to scale than self-serve subscriptions.
It is a choice about which kind of business you are running, not a growth hack.

**The lesson.** When your category commoditises, the defensible thing is never the software — it is the
depth of your understanding of one customer's operation, and the outcome you are accountable for.
Price against the value of the outcome rather than against the cheapest tool that looks like yours, and
build the relationship that a copycat cannot obtain by cloning your interface. If a weekend of work can
reproduce your product, your job is not to build faster. It is to sell something that is not the
product.
*(via a founder thread on r/startups)*

### 47. Three people promised, one signed up

**The pain.** You launch. Several people had told you, enthusiastically, that they would sign up the
moment it was live. It is live. One person did. And you cannot tell whether that is a catastrophe or a
Tuesday.

**The struggle.** A founder four days past launch posted the whole embarrassing arithmetic, including
the detail that makes it human: the second account on the site was "just me pretending to be another
person." Of the people who had said they would join, most had not. The one who did was using it every
day and loved it. The panic in the post is about the gap between the promises and the behaviour, and
the thread's most valuable contribution was to refuse the framing entirely. Nobody is cooked at four
days. But the reason the promises evaporated is worth stating plainly, and one commenter did: people
make cheap declarations of support, and the way to find out whether they meant it is to have asked for
something with a cost attached — a pre-launch payment, a commitment, skin in the game — because
enthusiasm without a price is not a forecast of anything.

**What worked.** The consensus response was the opposite of what the founder expected, and it is the
part to remember: one person who returns every day for four days is a far stronger result than fifty
signups who poke the product once and vanish. The advice that followed was uniformly qualitative,
because at n=1 there is nothing quantitative to say. Treat the coming week as a full-time job serving
that one user. Interview them — not about features, but about the specific problem the product is
solving and what they were doing before it existed. Then use that description to define who else has
the same problem, and go find those people, because the person who already has the problem is the only
reliable description of the market you have. Ask them for referrals and introductions, since a genuinely
delighted user is the cheapest distribution available at this stage. And separately, ask the people who
promised and never arrived why they did not — those answers are usually more informative than the happy
user's, and much more uncomfortable. Two comments supplied the broader calibration: nobody caring is
the normal outcome for the overwhelming majority of launches, and launch day is the start line rather
than the finish — building was the easy half.

**The lesson.** Stated intent is not demand; only behaviour is. Count users who came back, never users
who said they would come. And when you have exactly one real user, that is not a small failure, it is a
small sample of something real — so stop optimising the funnel, go and learn everything about why that
one person stayed, and use their words to find the next ten.
*(via a founder thread on r/startups)*

### 48. Optimising for a crowd that never showed

**The pain.** Months in, you look back and realise almost all the anxiety went into questions nobody
ever asked you about — the name, the logo, the framework, whether the thing was polished enough to be
seen.

**The struggle.** A founder a few months into building asked the room a good question: what did you
stress over at the start that turned out not to matter? The answers arrived with unusual consistency,
and they were all versions of the same shape. The name and the visual polish moved nothing. The colour
scheme and logo were redone several times anyway, so the early agonising was wasted twice over. Nobody
who used the product ever asked what it was built with. The business plan mattered far less than doing
anything at all. And the single best line in the thread came from someone who had worried whether their
system would hold up at ten thousand users while sitting at zero: they had "optimized for a crowd that
never showed," and getting one person to care was always the actual problem.

**What worked.** What lifts this above a list of regrets is the explanation one commenter gave for why
smart people do this so reliably: customer acquisition is always the real problem, and we busy
ourselves with other problems to hide from that one. That is the mechanism. Every item on the list —
the naming, the polish, the stack, the scalability, the plan — is legible, controllable, and produces a
visible sense of progress, whereas talking to a stranger who might not care is none of those things.
Two people added a sharper correction that keeps this from becoming a platitude. The founder's own
stated fix was to seek honest feedback, and one experienced reply gently pushed back on it: people are
poor at explaining why they will not use something, and the most talkative respondents are frequently
the least likely to ever pay. What was more informative was watching behaviour without being in the
room — where people stopped, what they never clicked, whether they returned. So the correction is not
merely "talk to users instead of polishing"; it is to prefer observed behaviour over reported opinion,
and to treat an unfinished product in front of a real person as the instrument that generates it.

**The lesson.** Rank your early work by how much fear it removes rather than how much progress it
displays. The tasks that feel productive are usually the ones with no other human in them, and the
things founders retrospectively call wasted effort are almost always exactly those. Ship it ugly, put
it in front of someone who has the problem today, and if you are ever unsure which task matters, pick
the one you have been quietly avoiding — it is almost certainly the one that touches a customer.
*(via a founder thread on r/startups)*

### 49. The comfort zone did not contain the revenue

**The pain.** You are working hard and the number is not moving. The activities you are willing to do —
posting, building, tweaking, planning — are all done to a decent standard, and the revenue still sits
where it was.

**The struggle.** A founder wrote about getting stuck before the first few thousand in revenue, and was
honest about the reason in a way most posts are not. It was not the market or the product. It was that
they had a fear of cold calling and cold emailing, and had been quietly routing around both. The result
was months of effort inside the comfortable set of tasks, and no revenue, because — in their own words —
"the stuff within my comfort level didn't get me to $3k." Once they accepted that and started making
calls and sending the emails, that first milestone arrived fairly quickly. The next one, to $5k, felt
like nothing by comparison, and the path beyond it looked clear enough that the fear had gone out of it
entirely.

**What worked.** The post's stated lesson is about milestones — that "0 to 1" is an unhelpfully abstract
frame, and breaking the climb into tangible steps you can actually picture makes it far less
intimidating. That is true and worth doing, but the thread's readers were sharper about what actually
changed, and several said the same thing independently: the milestone framing was not the mechanism,
picking up the phone was. You could keep the neat numeric ladder and remain exactly as stuck if you
never do the uncomfortable part; what breaking it down really bought was permission to attempt the
scary thing at a small enough scale to survive it. The most practical refinement in the thread turns
this into something you can run weekly: set milestones on activities rather than outcomes, because you
cannot control when revenue arrives but you can control whether the calls were made, the emails were
sent and the follow-ups happened today. Another commenter named the compounding effect that makes the
second milestone easier than the first — the early wins are not really revenue, they are evidence to
yourself that the avoided actions move the number. Two useful corrections also surfaced. Several people
noted the original phrase comes from a book about building genuinely novel companies and means
something closer to product-market fit than to your first dollar. And one warned against the implied
promise that it gets easy afterwards: the next stage is a different problem — rebuilding operations so
the business does not collapse under its own weight — which kills plenty of companies that had no
trouble finding customers.

**The lesson.** When revenue is flat despite real effort, audit which activities you are actually
avoiding rather than which ones you are doing badly. Set your targets on the things you control — calls
made, emails sent, follow-ups completed this week — and let revenue be the lagging report it is. The
first sales are worth more as proof than as money: they tell you that the uncomfortable activity works,
which is the only thing that makes the second attempt cheap.
*(via a founder thread on r/Entrepreneur)*

### 50. Everyone knows to follow up

**The pain.** Nothing on your marketing list is a mystery. Follow up with leads. Ask happy customers for
a review. Publish something regularly. You know all of it, none of it is contentious, and in a busy week
none of it happens.

**The struggle.** An operator made this observation and it drew a large, argumentative thread — worth
noting that several readers were sceptical of the post itself, and one dismissed it as the sort of
frictionless wisdom that fills professional feeds. The scepticism is fair and the observation still
holds, because the failure it describes is the most common one in small-company marketing. Businesses
with simple systems and unglamorous discipline outgrow businesses with better tools and larger plans,
and the difference is not insight. It is whether the fifth week of doing an unremarkable thing actually
happens once everything else starts demanding attention.

**What worked.** The comments were more useful than the post, and between them they form something like
an operating manual. Start with the highest-value habit anyone named: speed of follow-up. One
commenter's experience was that replying within about five minutes rather than an hour changed
conversion substantially, and that most businesses lose leads to slow response rather than to a weak
product. Then the mechanics of making a habit survive a bad week. Put the recurring activity on the
calendar as a specific block — follow-ups Tuesday morning, marketing planning Thursday before you log
off — so the decision is made before the willpower is needed. Weld new habits to something already in
your routine, because anything that requires a separate task on a future day quietly gets dropped.
Attach external stakes where you can: a date promised to a client gets done, which is unglamorous but
effective. And the correction that makes all of it workable: consistency usually fails because people
set the bar at doing it well rather than doing it at all. Two commenters supplied the measurement half.
Log a real number after every sales call — an actual probability and a next date, not "went well" —
which turns a pipeline from a feeling into something you can act on. And check monthly where good
enquiries actually came from, since that single review is what stops effort accumulating in channels
that never produced anything.

**The lesson.** Most marketing plans do not fail on strategy, they fail on the fifth week. Choose fewer
activities than you think you can sustain, put them in the calendar attached to something you already
do, and set the standard at done rather than done well. Then measure two things only: how fast you
respond to a new lead, and where the good ones came from. A small system executed every week beats a
better one executed in bursts, and the gap between the two is most of the difference you see between
similar companies.
*(via a founder thread on r/Entrepreneur)*

## Entries — 2026-07-31

### 51. Seven months building, two months reading about launching

**The pain.** The product is done. You have been a competent engineer for a decade and this is the
first thing you have built that nobody assigned to you. And now it sits there, finished, because you
do not know how to do the next part and cannot find the instruction manual.

**The struggle.** A founder with ten years of software behind them described exactly that: seven months
of development, then a refusal to launch because they did not know how, then two more months reading
books about product launches without being able to apply any of it. Everything the books recommended —
build an email list, grow a following — looked like it would take longer than the build had. The thread
was blunt and nearly unanimous about what had gone wrong, and it was not a marketing problem. They had
skipped validation and were now trying to buy it back with tactics. One reply refused the premise of
the post outright: a product is never finished until it is dead, and what they had was an MVP with a
misleading label. Another pointed out the tell in the founder's own words, because they volunteered it
themselves when someone asked what the product did — it had accumulated a long list of features that
nobody had asked for, since nothing in it had ever been checked against a person. That is the shape of
the build trap. It produces visible progress, it feels like work, and it postpones the only conversation
that could have told you whether any of it was worth building.

**What worked.** The most useful reply in the thread was also the most concrete, and it dismantles the
word that was causing the paralysis: stop thinking in terms of a launch at all. Pick one narrow customer
type, find twenty places where those people already complain about the problem, and open conversations
with a paid pilot offer attached. There is no event to organise there, no audience to accumulate first,
and no book required — just a list and a sequence you can start on a Tuesday. Others filled in the same
picture from different directions. Trade access for time: offer the product free in exchange for a
fifteen-minute feedback call, which teaches you to articulate your own value proposition faster than
any launch methodology. Let a handful of people in the space trial it, collect open-ended reactions,
and repeat until somebody asks what the minimum is to keep using it — that question is the first real
price signal you will get. And do not just ask whether people like it; ask what they are doing today
and what would make them switch, because the incumbent in almost every deal is the workaround the
customer already has. Two commenters also argued for launching in the plain sense of putting it online
regardless, on the grounds that nothing gets indexed or discovered until it exists in public. Both
things are true, and they resolve neatly: publish it this week because the clock on discoverability
should already be running, but do not confuse that with distribution.

**The lesson.** "Launch" is a word that makes founders wait. There is no launch when nobody knows you
exist — there is only the first twenty conversations, and they are available today. If you have built
something without ever having those conversations, the correct next move is not a better launch plan;
it is to go and have them late, accept what they tell you about the features nobody requested, and
treat the first person who asks about price as the beginning of the business.
*(via a founder thread on r/startups)*

### 52. For sale: everything except the customers

**The pain.** You built the thing. It works, it renders, the pipeline runs end to end, and after months
of it being live you have made a couple of hundred dollars. And you have started to suspect the missing
piece is not something you can code.

**The struggle.** A founder put a finished micro-SaaS up for sale and led with numbers most listings
would bury: roughly $220 in all-time revenue, about fifty users, no recurring revenue because the
pricing was one-time. The asking price was $2,800 — explicitly framed as less than it would cost to
build the same thing from scratch. What is being sold, in other words, is the build: the codebase, the
render pipeline, dozens of custom motion components, the tooling that keeps the output from looking
templated, and a list of fifty existing users the buyer can email. The reason given for selling is the
part worth stopping on, because the founder said it plainly rather than dressing it up as a strategic
pivot: they would rather hand it to someone who is good at distribution than sit on it. The single
comment on the listing agreed, noting that most builders in this situation pretend that part does not
exist.

**What worked.** Read the listing as a valuation exercise and it becomes unusually clear. A working
product with fifty users and $220 of lifetime revenue is priced at roughly the replacement cost of the
engineering, which is the market saying that the software is the cheap half. Everything expensive — an
audience, a repeatable channel, a reason for anyone to arrive — is what the seller is asking the buyer
to supply, and the listing says so directly: this is for someone who can do distribution, ideally
someone who already has an audience of founders they can put it in front of. That is an honest and
slightly brutal description of what a built-but-undistributed product is worth. It is also the correct
diagnosis of why the revenue is $220 rather than $2,200: one-time pricing on a tool with no recurring
demand means every dollar has to be re-earned by finding a new stranger, so the business was always
going to be a distribution business, and the founder was running it as a build business. The
constructive version of this for anyone not selling: if the honest pitch for your product is "someone
with an audience should take this over," you have identified your actual constraint, and you can either
go and acquire that audience deliberately — one narrow group, one channel, sustained past the point of
boredom — or partner with somebody who already holds it, on terms agreed while you still own the asset.

**The lesson.** The market prices a codebase at what a codebase costs, and it is not much. The scarce
asset is a route to the people who have the problem, and if you do not own one, you are always going to
be selling to the person who does. Notice when your own description of the business has become "great
product, needs distribution" — that is not a gap in the plan, that is the plan you never made.
*(via a founder listing on r/micro_saas)*

### 53. The rejections were the most useful reply you got

**The pain.** You have contacted a long list of investors. Most said nothing at all. A few replied to
say they do not invest at your stage, or in your region. You are outside the obvious startup hubs, you
cannot afford to fly to conferences, and it has started to feel like the whole thing turns on a warm
introduction you have no way of getting.

**The struggle.** A founder with a built and tested enterprise product described that exact position,
along with the reason they had gone looking for capital in the first place: enterprises do not readily
buy from startups, so users were hard to get. The thread was sympathetic about the warm-intro problem
and then dismantled the sequence completely. The most direct objection was the simplest: you are asking
people to fund a company whose pitch includes the sentence that customers are very difficult to get, and
nobody invests on that. Several pointed out that the enterprise motion is not affordable pre-revenue
anyway — an eighteen-month sales cycle is not something a startup with no money can complete, and in
many cases could not service the account if it closed. And the sharpest reply reframed the rejections
themselves as the useful data in the whole exercise: the funds that answered told you they do not do
pre-seed in your region, which means "your list is wrong not the outreach." That is a targeting result,
not a verdict on the company.

**What worked.** The rebuild that follows is mechanical rather than mystical. Construct the list out of
funds that have already wired money into a company in your country at your stage, because past behaviour
is the only qualification criterion available to you from the outside — the same discipline you would
apply to a sales prospect list, and the same failure if you skip it. Then fix the order of operations.
The thread's consistent advice was to get commercial evidence before capital: a couple of paid pilots,
or signed letters of intent, on the grounds that the first question in a pre-seed enterprise meeting is
about design partners and signed pilots rather than about the finished product. One commenter suggested
going down-market first — sell to startups and SMBs, get the product battle-tested in production, and
come back to enterprise buyers with proof it does not break, since what the enterprise is really
refusing is not your pitch but your operational risk. Another named the credibility shortcut that
actually works in these categories: find an industry veteran to act as an advisor, someone whose name
does the vouching your company cannot yet do for itself. And there was one genuinely practical trick
for manufacturing warm introductions from nothing — approach founders who have recently raised, ask
for fifteen minutes on your deck rather than for an introduction, and let the relationship produce the
referral as a by-product.

**The lesson.** A no that tells you why is worth more than silence, and worth more than most yeses,
because it is the only free audit of your targeting you will ever be handed. When the rejections cluster
around stage, region or segment, the list is broken and no amount of better outreach will fix it. And
when you find yourself raising money because customers are hard to get, invert it: the customers are the
thing that makes the money easy to get, so go and buy the smallest possible version of that evidence
first.
*(via a founder thread on r/startups)*

### 54. Renting the relationship you do not have

**The pain.** Your buyers are in an industry that runs on relationships. Cold email does not get you a
demo, cold calls do not get you a callback, and the people who do buy your category appear to be doing
it on the recommendation of someone they already trust. You are not that person and cannot become them
this quarter.

**The struggle.** A founder selling into the architecture and engineering trades — specifically the
mechanical, electrical and plumbing firms inside it — asked the room whether bringing on an industry
veteran as an advisor was a legitimate way to get warm introductions that become customers. It is a
question worth taking seriously rather than treating as a shortcut, because the underlying observation
is correct: in relationship-driven sectors, the barrier is not that your message is bad, it is that
unknown vendors are filtered before the message is read. Cold outreach into that kind of market does not
fail on copy. It fails on standing.

**What worked.** The reply that came back was short and experienced. In several industries — utilities
and pharmaceuticals were the examples given — an advisor of this kind is not a growth tactic but a
requirement, and startups selling into them routinely have one. On finding them, the practical advice
was unglamorous: cold outreach is the honest answer if you know nobody, but there are warmer routes.
Universities are a good hunting ground for credible people connected to a trade. So are professional
communities, provided you enter them asking for feedback on the product rather than for a sale, because
the request for perspective costs the veteran nothing and starts a relationship on the correct footing.
Investors are another source of these people, with the caveat that this route only opens once you are
far enough along to want them. Two things are worth adding that the thread did not, and both are about
keeping this honest. An advisor is not a distribution channel you can install — they hold a limited
stock of credibility and spend it one introduction at a time, so the arrangement works when you have
something you genuinely believe will make their contact's life better, and burns out fast when you use
them as a mailing list. And the terms matter: a small equity grant vesting over time, with a clear
expectation of what the advisor is actually agreeing to do, is a normal structure and a much better
foundation than a vague promise of upside.

**The lesson.** In a market where trust is the gating factor, you can either spend years earning
standing or borrow it from someone who already has it — and borrowing is legitimate, common, and
frequently the only route in. Just be clear about what you are borrowing. You are not buying a list, you
are renting a reputation, and every introduction spends a little of it. Bring the veteran something
worth their name being attached to, and the channel keeps working.
*(via a founder thread on r/startups)*

### 55. Two clients in the pipeline and a ceiling nobody mentioned

**The pain.** You have a website, intake forms, spreadsheets, and your first customer lined up before
you have officially started. The plan looks sound on the page. And the thing that will cap the business
two years from now is a decision you are making right now without noticing you are making it.

**The struggle.** A pair starting a cleaning business posted the whole setup for review: one partner
with three years of professional cleaning experience and a non-compete now expired, the other keeping a
full-time job and handling the back office, a website and client forms already built, and two short-term
rental clients in the pipeline. The first paying customer wanted the property turned over five to eight
times a month at $225-400 per clean depending on the guest's stay. It is a genuinely good start, and the
thread's most-upvoted response was not congratulations. It was a redirection of the entire customer
segment: go after commercial contracts instead, because the money is better and — the part that actually
explains it — commercial clients are not emotionally attached to the property. That single sentence is
the whole argument for the segment. Homeowners are buying a feeling about their own house and will
litigate the details of it; a facilities manager is buying a completed job on a schedule.

**What worked.** The operators in the thread filled in what the short-term-rental segment actually costs
you, and it is the kind of detail you only get from someone who has run it. Those turnovers cluster in a
narrow window between checkout and check-in, roughly late morning to mid-afternoon, so a handful of
clients on opposite sides of a city means a day spent driving rather than cleaning. Laundry, if you take
it on, is another hour and a half of machine time per property. And guests dispute cleanliness to obtain
discounts, which lands back on the cleaner — one commenter had left the platform entirely over it, and
the defensive habit that survives from their experience is photographing everything, before and after,
every time. Commercial work inverts most of that: it is scheduled after hours, it is repeatable, and it
is not adjudicated by a stranger looking for a refund. On the marketing side the advice was narrow and
correct for a local service business, which is a distribution problem rather than an advertising one:
optimise the Google Business Profile, name the areas you serve in the service descriptions and again in
your replies to reviews, and collect reviews obsessively from the earliest jobs — offer small
inducements to the first clients for them and stop once you have a solid base. Build the checklists and
standard procedures from day one, because a service business sells reliability and reliability is a
document. And do not compete on price; a cleaner who reliably turns up is worth paying for, which is the
only durable position available in a trade with no barriers to entry. The sharpest warning in the thread
was structural: if the revenue stops when you go on holiday, it is "more job than business" — a test
worth applying to the segment choice, since commercial contracts survive a staffing change and a
personal relationship with a homeowner often does not.

**The lesson.** Your first customers feel like luck, so you take the ones that arrive — and the segment
you accidentally standardise on decides your margins, your working hours, your churn and whether the
thing can ever run without you. Choose it deliberately in month one, while switching costs nothing.
Then build the two assets that compound in any local market: a review profile that ranks, and a
documented standard of service that lets someone other than you deliver it.
*(via a founder thread on r/Entrepreneur)*

### 56. The audience does not want to leave the app

**The pain.** You have done what the advice says. Instagram sends people to YouTube, YouTube sends them
to LinkedIn, everything points at everything else. And the funnel between platforms leaks so completely
that you cannot find evidence any of it moves a single person.

**The struggle.** An operator questioned the whole cross-platform playbook and gave the honest reason it
fails, which is not a tactical one: every platform wants users to stay, and viewers do not enjoy leaving
an app because a creator told them to. The thread's replies were unusually consistent for a marketing
question, and several supplied the mechanism the advice always omits. An outbound click is a worse
outcome for the platform than a viewer staying, so anything shaped like an off-ramp gets suppressed —
you are not imagining the reach penalty, you are being charged for it. Beyond distribution, the strategy
is expensive to run: several people described the multi-platform funnel as an energy drain that only
works with a team, and one named the failure mode precisely — when every post has to feed every other
post, the system becomes heavy enough that you stop publishing at all. Which is the real cost, since the
only thing that reliably kills a content channel is the founder quietly abandoning it.

**What worked.** The replacement strategy the thread converged on has three parts and is easier to
sustain than the thing it replaces. First, treat each platform as its own channel with its own job —
one commenter running an agency described exactly that split: professional authority in one place,
depth and long-form in another, quick and immediately useful in a third. The content is one idea in
different packaging, made native to how people consume in that place, rather than one asset reposted
four times. Second, stop asking anyone to move sideways. Let the overlap happen on its own; people who
want more of you will go looking. Several described running links only in the profile and in the first
reply beneath a post, never in the post itself, precisely because an off-platform ask inside the content
reads as an advertisement in the middle of someone's scroll. Third — and this is the only exception
worth making — ask people to move exactly once, to something you own. An email list, with a real payoff
attached: early access, a tool, a resource actually worth having. The reasoning given was not
sentimental. A social account can be removed at any time and for no stated reason, so a business built
on rented land carries a risk you cannot price; and email is the only layer where you can see what
someone clicked, what they bought and whether they came back, which is the difference between an
audience and a broadcast. One commenter added the correction that keeps this from becoming another rule
to follow badly: audiences do not want to follow you everywhere. Being genuinely valuable in the one
place someone found you beats persuading them to consume you in three.

**The lesson.** Platforms are discovery; the list is the relationship. Make content native to each place
and let people arrive where they arrive. Spend your one off-platform ask on moving them somewhere you
own, with a payoff that justifies the click — and if you are choosing between a cross-platform strategy
you can barely sustain and one platform you can post to every week for a year, choose the one you will
still be doing in November.
*(via an operator thread on r/Entrepreneur)*

### 57. The free tier stopped being free

**The pain.** Your free plan used to cost you disk space and a rounding error of bandwidth. Now every
free session bills you in inference, the invoice arrives monthly whether or not anyone converts, and the
number has stopped looking like marketing spend and started looking like a leak.

**The struggle.** A founder laid out the arithmetic. An average free user on a product with AI features
runs ten to twelve sessions a month and costs somewhere around $2.80; heavy free users can cost an order
of magnitude more than that. Set against a conversion rate of about five percent into a $20-50 plan, the
model stops working, because the paying minority is now subsidising a genuinely expensive majority
rather than a nearly free one. Their honest assessment of the available fixes was that none of them is
good. Downgrade free users to cheaper models and you are "demoing a dumber product" — the trial now
under-represents what you sell. Meter it with credits, which is what most of the market did, and you
have capped the bleeding while teaching people to use the product as little as possible. Let users bring
their own API key and the economics resolve completely, at the cost of every casual signup you would
have had.

**What worked.** The thread would not let the conclusion stand unchallenged, and the objection is the
one that matters commercially: at least one buyer said flatly that they will not try a product without a
free tier, and will therefore never pay for one. That is the trap in full — the demo is now a real cost
per prospect, and removing it removes the trial that produces the customer. The most useful reply came
from someone who had already made the call on a product with genuinely expensive inference, and their
reasoning is the transferable part. They dropped the free tier for credit packs, on the grounds that the
usual objection to credits only applies when usage is the value; where the product is outcome-based —
the user spends a credit, gets the result and leaves satisfied — the meter matches what was delivered
and nobody feels rationed. The cost of that choice was named honestly: with no free trial, the landing
page has to do all of the convincing, so they put real before-and-after outputs on it rather than paying
inference for tourists. That is the actual design principle. When the demonstration is expensive, move
as much of the persuasion as possible to the parts that cost nothing to serve — visible output, worked
examples, a video of the thing running — and reserve the metered experience for people who have already
been convinced by the page. Others in the thread pointed the same way from the finance side: whether a
free tier is affordable is not a philosophical question but a comparison between lifetime value and the
fully loaded cost of the free users required to produce one customer, which means you need to know both
numbers before defending either position.

**The lesson.** A free tier was always an acquisition cost; it just used to be invisible. Price it
explicitly — cost per free user, multiplied by how many free users a paying one requires, set against
what that customer is worth — and design around the answer rather than around the convention. If the
demo is expensive, make the landing page carry the persuasion and let the product deliver outcomes
people pay for. And whichever way you go, decide it from your own arithmetic; a rule about free tiers
that was true when a session cost nothing is not evidence about a product where a session costs a
quarter.
*(via a founder thread on r/micro_saas)*

### 58. They will forgive a rough version; they will not forgive silence

**The pain.** The product is not what you want it to be yet. So you go quiet, and work, and plan to
speak again when there is something worth announcing. The users you already have hear nothing for six
weeks and quietly conclude the thing is abandoned.

**The struggle.** A founder five years into building a combined hardware and software product — a
muscle-stimulation device with a phone app, started in a college dorm, now fifteen people and $2.2M
raised — wrote up the unglamorous mechanics of shipping updates, which is a category of post almost
nobody writes because there is no announcement in it. The constraint they described is severe: every
app decision is also a firmware decision, and firmware attached to a human body cannot move fast and
break things, so a user-interface change that looks like two days of work can touch Bluetooth behaviour
and safety limits and take six or seven. Their process is deliberately slow and deliberately physical —
changes sketched on paper against tester feedback, worked into designs, built, and then personally
tested on every build by the founder wearing the device, on the reasoning that if the founder will not
strap the product on, nobody else should be asked to trust it.

**What worked.** Two of their conclusions are marketing lessons wearing engineering clothes. The first
is the one to take: "Your update cadence is a feature." People will forgive a rough first version if
improvements arrive on a rhythm, and they will not forgive silence — which reframes the release notes,
the changelog and the short update post as retention mechanisms rather than administrative overhead.
What a user is actually deciding during a gap is not whether the current version is good enough, but
whether anyone is still working on it, and a visible rhythm answers that question before it gets asked.
It also inverts the instinct that produces the silence in the first place: the founder waiting for
something impressive to announce is optimising for the wrong audience, because existing users want
evidence of motion far more than they want a headline. The second conclusion is about where durability
comes from — more than fifty versions of one component before it worked properly, none of which is
visible in a demo. A competitor can copy the finished shape, and copying it does not transfer the fifty
attempts that taught you which shapes fail. Worth stating the limit honestly, since the thread did not
test it: cadence only earns forgiveness while the improvements are real. A weekly note about nothing is
noise, and the compounding effect depends on users being able to recognise their own reported problem
in the update.

**The lesson.** Shipping on a rhythm is a marketing channel you already own and probably do not use.
Publish the small improvements, name the fix that came from a user's complaint, and keep the interval
short enough that nobody has to wonder whether the product is alive. Rough and moving beats polished and
silent, every time — and the pile of failed attempts behind a working version is the part of your
product that nobody can copy.
*(via a founder thread on r/Entrepreneur)*

### 59. Fluent in unhinged

**The pain.** You write the post the way the category writes posts. It is professional, it is
appropriate, it is indistinguishable from the forty others on the page, and it produces nothing. So you
conclude that the channel does not work.

**The struggle.** A startup team needed people to make short-form video for their first marketing push
and went looking the ordinary way. Every listing in the field read the same — variations on "content
marketing associate" and "social media coordinator" — which is exactly what you get when everyone writes
to be taken seriously by the same imagined reader. So they wrote a listing for a "brainrot specialist"
instead, with requirements phrased in the dialect of the people they actually wanted: "fluent in
unhinged," able to spot a dying meme format before it dies, able to explain why a video does four
million views for no discernible reason. They posted it and went to bed. They woke up to hundreds of
applications, ran roughly thirty interviews, and hired three people — including, improbably, a
quantitative finance student who had read up on the company and was there for the product rather than
the joke.

**What worked.** The mechanism is worth separating from the stunt, because the stunt is not repeatable
and the mechanism is. The listing was written in the reader's own language rather than the category's,
which did two things at once: it was legible as unusual in a feed of identical items, and it described
the work in terms the right person recognised as their actual skill instead of a euphemism for it.
Applicants told them directly that they had never seen a listing like it, and that the strangeness made
them ask who the company was — attention converted into curiosity about the business, which is precisely
what a piece of marketing copy is supposed to do. The founder's own summary is the general form:
standing out is often worth more than being professional. The thread supplied two corrections that keep
this usable. The first is a sceptical one, from the most-upvoted reply: it was probably the pay, and no
amount of clever wording rescues an offer nobody wants. That is the right objection and it generalises —
novel copy gets a bad offer looked at, then rejected faster. The second is in the numbers the founders
published without comment. Hundreds of applications produced about thirty interviews and three hires,
which is the honest arithmetic of writing for attention: the volume arrives, and most of it is people
responding to the tone rather than to the job. Somebody had to read all of it. Novelty buys reach, not
qualification, and you pay for the difference in screening time.

**The lesson.** Whatever you are posting — a job listing, a landing page, a cold email — the default
version is written in the language of your category and reaches nobody, because it looks like everything
else and describes the reader in terms they would never use about themselves. Write it in your reader's
own words instead, including the ones that sound unserious, and accept the trade: you will get more
attention than the offer deserves, so make sure the offer underneath it is real, and budget for the
sorting.
*(via a founder thread on r/Entrepreneur)*

## Entries — 2026-08-04

### 60. Distribution for people who hate being seen

**The pain.** You have been able to build since you were a child. Give you an idea and a week and there
is a working product at the end of it. And every piece of advice about the part that comes after
assumes you are willing to become someone who posts daily, networks, and talks about themselves in
public. You are not that person, you have known it for years, and so the products sit there.

**The struggle.** A founder who had been coding since fifth grade laid this out plainly: years spent
improving at building, almost none spent learning distribution, and an honest admission that the
obstacle was temperament rather than ignorance. The thread that followed was one of the more useful
ones on the subject, mostly because the first reply reframed the problem instead of answering it.
Technical founders treat distribution as marketing, when at the start it is closer to research. Before
reaching thousands of people you need enough conversations to know who has the problem, how they solve
it today, and what would make them switch — and the messaging that feels impossible to write becomes
almost mechanical once you can answer those three. The founder's own reply is the sentence to keep:
they had been thinking about it as promotion instead of learning. That single substitution changes what
the activity is. Promotion requires you to be interesting; learning only requires you to be curious,
which is a much easier thing to ask of someone who dislikes attention.

**What worked.** The most concrete answer came from another introvert and it is the least painful
version of distribution available: they got their first users from commenting rather than posting. A
week spent answering questions in founder communities where they genuinely knew the answer, no links
and no pitching, until people started asking what they were building. The generalised form arrived in
another reply — find the questions people already type about your problem and answer them properly, one
a day, under your own name. That works for this personality because it is written and asynchronous, it
inverts the direction of the ask, and it never requires you to interrupt anyone. Several others
converged on the low-volume version of the same thing: pick ten or twenty people who already have the
problem, ask how they handle it today, and let the answers tell you who buys and where they gather.
One reply supplied the correction that keeps this honest, and it is the part most threads leave out.
Commenting has a ceiling: it is a personal writing habit, you cannot sustain much past a couple of hours
a day, and that caps how many people you can reach in a week. So it is the right first channel and the
wrong only channel — the move is to reuse the same ideas in more durable formats once the answers start
repeating, which they will, because most people ask the same six questions.

**The lesson.** If you are not built for broadcast, do not fight it and do not wait to be cured of it.
Choose the channel that matches your temperament — written, asynchronous, answering rather than
announcing — and start with learning rather than promotion, because twenty conversations will hand you
the messaging you cannot currently write. Then respect the ceiling: a habit that depends entirely on
your own hours is a start, not a system.
*(via a founder thread on r/startups)*

### 61. If it takes ten minutes to explain, it is a feature list

**The pain.** You are genuinely better than the incumbent and you can prove it, item by item. But the
reaction you keep getting is "so it's like [big competitor] but worse at [the one thing you are worse
at]" — and by the time you have drawn breath to answer, the moment has gone.

**The struggle.** A founder building on-device meeting transcription described this exactly. Their
reactions split into two camps: the people who immediately understood and converted, and the people who
filed them under a competitor's name with a deduction attached. They had tested nearly every app in the
category, believed honestly that they were better in most of the ways that matter, and were candid
about where they were not — and none of that was reaching anyone, because the comparison was over
before it started. Their instinct was to build more comparison pages. The thread's most-upvoted reply
refused the framing: the problem is not attention, it is that if you need time to explain what makes
you different, you do not have a position yet, you have a feature list. A second reply named the
mechanism underneath it, and it is the sharper observation of the two — when you accept the "like X but
worse at Y" comparison and start defending Y, you have already conceded that Y is the axis the decision
turns on. The incumbent chose that axis. Arguing on it is playing an away game.

**What worked.** The advice converged on subtraction. Pick the single use case where your architecture
is undeniably better and sell only that; for on-device transcription the thread's suggestion was
privacy, and specifically the meetings that legally cannot touch someone else's server — legal,
medical. One sentence a person instantly understands beats a ten-minute demo, because markets do not
reward the product with the most features, they reward the one that is easiest to understand. The
narrowing can also be by customer rather than by capability: become the transcription tool for one
substantial industry rather than a general tool with an industry page, narrow enough to be the obvious
choice and not so narrow that the market is a rounding error. And the most practical suggestion was a
research one, because the position is not something you invent at a whiteboard. Interview a handful of
people who converted and a handful who dismissed you as another recorder, and ask two questions: what
was happening in the meeting, and what proof changed their mind. The answer that repeats becomes the
first line on your site. Everything else — the hundred honest advantages, the full comparison — stays,
but it moves to where buyers who have already engaged will go looking for it. That is the actual
sequence: one claim to get in the door, the feature list for people who are already evaluating.

**The lesson.** In a crowded category, being better is a claim your buyer has heard from everyone and
cannot evaluate. Being instantly comprehensible is rarer and does more work. Find the one use case
where your difference is structural rather than incremental, lead with only that, and let the depth
you are proud of live one click further in — and when someone frames you against the incumbent, change
the axis rather than defending theirs.
*(via a founder thread on r/startups)*

### 62. Stop improving the pitch; remove the asks

**The pain.** You are selling to an organisation whose staff are rewarded for not taking risks. Better
deck, better demo, more follow-up — and the answer is still a polite version of no, delivered on a
timeline you cannot afford.

**The struggle.** A founder selling into exactly that kind of buyer — institutions whose default answer
to anything new is no, and who had already refused far more polished companies — described treating it
as a persuasion problem for a long time and getting nowhere. Then they went back through the offer
itself and found something structural. Every version of the pitch had asked the buyer for something:
install this, change that, put our equipment near the expensive asset you are personally responsible
for. Each of those asks carried cost and risk to the person being asked, which meant each was an
independent reason to say no. It did not matter how good the argument was; the argument was competing
against a list of small, concrete, career-relevant downsides. So they rebuilt both the product and the
offer to ask for nothing — no installation, no hardware on the customer's side, no capital cost, no
exposure to the thing the buyer is paid to protect — and then made sure the yes came with things the
buyer wanted and had never had: a revenue line they did not have to build, and data about their own
operation they could not previously collect.

**What worked.** The conversations changed, and the founder's own account of why is the transferable
part: not that they became more persuasive, but that refusing now meant turning down upside with
nothing attached to it. A cautious buyer can resist a pitch indefinitely; resisting a free incentive
requires an argument they do not have. The thread supplied two corrections worth carrying, because the
principle is narrower than it first appears. The first is that removing cost removes only one kind of
risk. Enterprise buyers still carry implementation risk and career risk, and neither is priced in money
— someone still has to sponsor the thing internally and be associated with it if it goes badly. The
second came out of a follow-up exchange and applies to anyone selling to individuals rather than
institutions: consumer buyers stall on effort more than on price, so free removes the objection you can
see and leaves the one you cannot. The advice there was specific and testable — watch where people drop
off before the first useful moment, count the steps and taps it takes to reach it, and cut two of them.
That will usually beat another rewrite of the messaging. There was also a fair amount of scepticism in
the thread that the whole thing was a rediscovery of the free trial, and the objection is worth
answering rather than dismissing: a free trial removes price from an offer whose shape is unchanged.
This is the harder version — changing what the offer asks the buyer to do, not what it costs them.

**The lesson.** When a buyer is structurally resistant to change, enumerate every ask in your offer and
treat each one as an independent reason for no. Then remove them rather than out-arguing them. Price is
only one of the asks, usually not the largest, and never the last one standing — after money comes
effort, then internal risk, and the offer is not finished until you have looked at all three.
*(via a founder thread on r/startups)*

### 63. The buyer is whoever screenshots the bill

**The pain.** You have written down an ideal customer profile and it is composed of adjectives.
Post-MVP. Real production traffic. Growing fast. Accumulating technical debt. Every one of them is true
of your buyer and none of them tells you who to email on Monday.

**The struggle.** A team building a developer tool posted their go-to-market thinking for review. The
product was genuinely well-specified — it reads production traces, finds the repeated workflows that
account for most of the traffic, and turns them into cheaper deterministic implementations while
leaving the open-ended work alone. Their planned motion was founder-led: a free audit of production
traces, replay the historical traffic, quantify the savings, then sell an implementation sprint if the
numbers justify it. And their stated ideal customer was "AI startups at or near product-market fit,"
qualified by four characteristics, all of them internal states of the company. Which is the trap: those
are things you can only confirm after a conversation, so they cannot generate the list of companies you
need in order to have the conversations.

**What worked.** The thread's best replies did two separate jobs, and both are worth stealing. The
first was to move the wedge from the interesting problem to the boring one: sell against infrastructure
spend, not against technical debt. An audit that concludes "this workflow costs a specific amount per
month and we can make it cost less" is a purchase a finance-minded person can approve; "we reduce
prompt technical debt" is a conversation. The follow-on from the same commenter is the honest test —
if the product does not eat the messy part itself, the messy part becomes a person, and you have
reinvented consulting with better typography. The second job was replacing the adjectives with an
observable signal, and one reply did it in a sentence: the buyer is not defined by funding stage, it is
whoever already has an internal thread where someone posts a screenshot of the monthly model bill.
That is a real trigger event, it implies a rough spend threshold you can estimate from outside, and it
points at a specific person with a specific irritation rather than at a category. The rest of the
thread tightened the motion itself. A free diagnostic attracts teams who cannot legally let an outside
vendor near production data, so qualify for trace access early: ask for a redacted sample, find out who
owns security approval, and confirm there is budget this quarter before spending engineering time.
Better still, charge for the diagnostic and credit it against implementation — which filters curiosity
from urgency and prevents the failure mode a separate reply named, where the customer takes your
findings and fixes it in-house. That risk is real but smaller than it looks, and one commenter with a
decade of experience explained why: almost nobody ever finds time for non-critical technical debt. Your
job is to make the value obvious and the effort small enough that the comparison stops being close.

**The lesson.** An ideal customer profile made of internal states is unusable. Convert it into something
you can observe from outside — a visible trigger, a spend threshold, a person whose specific job is
being made worse — and the prospecting list writes itself. Lead with the number rather than the
concept, and charge something for the diagnostic, because a free assessment fills your calendar with
people who are interested and empties it of people who are ready.
*(via a founder thread on r/startups)*

### 64. Build for the user, charge the person who can pay next week

**The pain.** Every single person who uses the product loves it. None of them can buy it. The people
who can buy it are an institution with a procurement cycle measured in quarters, a budget that was
allocated last year, and a committee.

**The struggle.** A founder built an assessment tool for children's oral reading fluency — the thing
teachers currently do one child at a time with a photocopied passage and a stopwatch, where the
accuracy depends on the teacher's ear and their training. They had spent six months building and
piloting it in a real classroom of about ninety students, the feedback was uniformly positive, and they
came to the thread asking about marketing. The replies went straight past the marketing question to the
structural one. Positive feedback is not product-market fit; the test is whether anyone adopts and pays.
And in this market the person using it and the person paying are different people, with the buyer
sitting behind a six-to-twelve month sales cycle that requires a pilot before any money moves. The
founder confirmed it from inside the pilot: it had gone well, but the school was small, education
technology sales cycles were brutal, and budget cuts had made the outlook worse. This is the position
a lot of founders end up in without noticing — building enthusiastically for a user who has no
authority to spend.

**What worked.** The most useful reply proposed a split rather than a choice: build for the teacher,
charge the parent, and use classroom usage as the proof you eventually carry into a district. Parents
can pay next week. That gives you revenue now and, more importantly, it converts the slow channel from
a dependency into an asset — the pilot stops being a stalled sale and becomes evidence. The founder had
half-arrived at the same conclusion themselves, noting that the pilot had been invaluable for building
the product and that the studies would lend credibility to later sales efforts whether or not those
happened inside schools. Two other pieces of advice in the thread generalise well beyond education.
First: whatever number your buyers will quietly worry about, publish it. For a speech-recognition
product that is the error rate on real children's speech, because that single figure is the whole
objection and volunteering it converts the doubt into a specification. The founder had a defensible
answer and had not been leading with it. Second: sell the time saved, not the technology. Teachers are
already carrying more tools than they want; "this saves ten minutes per student" is a purchase, "our
speech recognition is better" is a comparison they have no way to check. And the friction bar in a
market like this is unforgiving — more than two clicks between opening the tool and getting a result is
too many, which is a product constraint that exists entirely for distribution reasons.

**The lesson.** Find out who signs before you build the go-to-market, because user and payer are
frequently different people on very different clocks. If the institution is slow, do not wait for it —
find the individual version of the same buyer, charge them now, and let the institutional pilot run in
parallel as proof rather than as revenue. And whatever the one number is that your buyer secretly
doubts, publish it before they ask.
*(via a founder thread on r/Entrepreneur)*

### 65. He bought more customers than he earned

**The pain.** You are grinding for customer one hundred. It has taken years. Meanwhile somebody two
towns over has four hundred of exactly your customers, is tired, and would sell the whole book tomorrow
if anyone asked.

**The struggle.** A founder who started a web hosting business in 2017 and sold it last week posted the
full accounting, which is rare enough to be worth reading closely. Total sales over the life of the
business, $2,356,315. Income to the owner, $677,708. Sale price, $425,000. Four hundred and thirty-five
clients, average lifetime of three and a half years, retention just under sixty percent, average
lifetime value of $4,870. The revenue curve is the ordinary shape — $14,311 in the first year, $42,417
in the second, and then a long climb to $472,546 in 2024. But the line that reframes the whole thing is
the breakdown of where the clients came from. Organic acquisition produced 133 clients and $892,666.
Buying other hosting companies produced 262 clients and $1,032,236. Partnerships produced 40 more.

**What worked.** The thread's top reply put it correctly: most people will skim past the acquisition
number, and it is the most important number on the page. More than half the customers and nearly half
the lifetime revenue were bought rather than earned, in a business where the alternative was competing
for search traffic against enormous incumbents. Acquiring a small competitor's customer book is a
distribution channel, and in mature, fragmented, subscription-shaped markets — hosting, agencies,
bookkeeping, maintenance contracts, local services — it is often a cheaper one than marketing, because
what you are buying is a set of recurring relationships whose economics you can already measure rather
than a promise about a funnel. The founder's answer on how those deals were found is the part to
notice: one came off a business-for-sale marketplace and the other three approached him directly. That
is not an M&A programme, it is the natural result of being a visible acquirer in a small industry for
several years. Two cautions sit in the data, and the thread found both. The margins tell a story the
revenue line hides: 2020 converted about sixty-four percent of sales into income, 2022 converted around
twenty, and it never fully recovered even as revenue kept climbing — the arithmetic of integrating
other people's customers on other people's infrastructure, or of a mix shifting toward cheaper
accounts. And the exit priced at roughly one times the most recent year's sales, against a soft final
year, which is a reminder that a book of business assembled by acquisition is valued the same way you
valued the books you bought.

**The lesson.** In a fragmented recurring-revenue market, treat acquisition as a channel and put it on
the same page as your marketing spend. You are comparing cost per customer either way, and the bought
version arrives with proven payment behaviour and a measurable retention curve attached. Be honest
about what it costs on the other side of the ledger — integration compresses margin, and buyers will
eventually price your business the way you priced theirs.
*(via a founder thread on r/Entrepreneur)*

### 66. You have hired four people to say a sentence that does not work

**The pain.** You have paid for outreach four separate times. You have paid the rush fee. You have
changed contractors. Somewhere in there you have started to suspect that the problem is not the person
holding the phone, and you would rather not follow that thought where it goes.

**The struggle.** A founder described exactly this sequence. An outreach assistant hired four times
since early May, producing a little signal and no bookings at all; the last engagement delivered two
weeks late, with the contractor asking for another two-week extension on the day it was due, after the
founder had paid extra for the faster turnaround. So they found a replacement who charges half as much
and works twice as fast — and still no bookings, though they were reasonable enough to say it was early.
The question they brought to the thread was whether they should be making the calls themselves. The
replies were close to unanimous and several of them made the same arithmetic point, which is the
uncomfortable one: four hires into the same role with the same outcome, and the variable that keeps
changing is the person. Two different callers and zero bookings is a strong indication that the problem
is the pitch or the list, not the dialling. Delegating a process that has never worked does not save
you time; it spends your money more slowly while hiding the reason.

**What worked.** The consensus prescription was to make the calls yourself for a few weeks — not
permanently, and not because founders are better on the phone. The reasoning given repeatedly was
informational. Early calls are research wearing a sales costume: they tell you which objection arrives
first, at what point in the sentence people lose interest, what language they use for the problem, and
whether the list you are calling contains anyone with the problem at all. None of that comes back
accurately through a contractor, even a good one with a good script, because a contractor is measured
on bookings and will report on bookings. One reply framed the sequencing plainly — you outsource after
you have made it work, not in order to make it work — and another put a number on it: keep the calls
until you have closed a couple of dozen deals, because until then you cannot train anyone, cannot
evaluate their calls, and have nothing to hand over but a hypothesis. The cheap partial version, for
anyone who genuinely cannot take the calls, also came up: record them, review them, and build the
objection list from the recordings. It is worse than being on the call and much better than reading a
weekly summary.

**The lesson.** You cannot delegate a sales process you have never run. A contractor executes a
message; they do not discover one, and they cannot tell you that your list is wrong. Do the calls
yourself until you have a repeatable sequence with the common objections written down and answered —
then hire, and hand over something that works. If you have hired for the same role several times and
gotten the same result, stop changing the person. The person is not the variable.
*(via a founder thread on r/Entrepreneur)*

### 67. Seven years of assets and no business

**The pain.** Seven years in. Two websites, real branding, proposal tooling, partnership agreements
with firms in several countries. Revenue close to zero. And now you are trying to work out whether to
push once more, sell the whole thing, or leave it — and the honest answer to what you have built is
harder to say than any of those.

**The struggle.** A founder in the citizenship- and residency-by-investment space wrote it up with
unusual candour, including the sentence that the thread kept returning to: they had put far more effort
into building than into selling. Client acquisition never worked, over seven years. They asked whether
anyone had sold a business like theirs — a niche service business whose value sat in the brand, the
website, the systems and the relationships rather than in revenue — and floated a price of $25,000.
The replies were blunt and mostly correct. If it never got off the ground, an acquirer does not
consider it a business; businesses are valued on revenue, and there was none. One reply pushed on the
number itself in a way worth repeating to yourself before any negotiation: if the figure is not derived
from a method, then it is arbitrary, and an arbitrary $25,000 has no more support than an arbitrary
$250,000. Another made the observation that stings most — if you could not sell the service, selling
the company is a strictly harder sale, and there is no broker coming for something this small.

**What worked.** The genuinely useful replies separated the operating business from the assets, and
that distinction is the whole of the practical advice. Nobody will buy a service model whose
acquisition never worked. But domains, content and rankings, drafted partner agreements, the quote
tooling, documented processes and any real inbound history can be worth something to a specific kind of
buyer — a firm already closing clients in that exact market who can plug your partner network in
tomorrow and skip a year of setup. Which dictates the process: not a listing on a marketplace, but
direct approaches to two or three named firms who already have the demand you never built. And the best
reply in the thread offered one thing to do before any of that, which is the part that applies whether
you sell or stay. Run a short, deliberately manual sales sprint and try to land five customers by hand.
If it works, you have a repeatable path and the thing you were about to sell for the price of a used
car has a value; if it does not, you have your answer, cleanly, after a week instead of an eighth year.
Either way the sprint is the cheapest information available to you, and it is information nobody can
produce on your behalf.

**The lesson.** Build and sell are not sequential, and the years you can spend proving that are
unbounded. If revenue never arrived, be precise about what you own: assets have buyers, businesses have
multiples, and confusing the two guarantees a disappointing conversation. Before you decide anything,
spend one week doing the manual selling you avoided for years — five customers by hand is the test the
brand, the website and the collateral were always standing in for.
*(via a founder thread on r/Entrepreneur, with a companion thread from the same founder)*

### 68. Price against what they do today, not against nothing

**The pain.** There is no direct competitor. You thought that was the good news. Now you have to write
a number on the page and there is nothing anywhere to check it against, so every price you consider
feels equally invented.

**The struggle.** A founder in exactly that position opened with a good observation — price is a proxy
for value, but people are poor at judging value in isolation and generally need a comparison to decide
what a thing should cost — and then drew the wrong conclusion from it. If buyers need a comparison,
they reasoned, the move is to position so that they cannot make one, which preserves your freedom on
margin. The thread's best reply cut that off immediately, and it is the correction most worth having:
removing every anchor does not free the buyer's judgement, it stalls the decision. With nothing to
compare against, the default is not "I'll pay whatever this is worth," it is "I'll think about it."
Meanwhile most of the thread's other advice was cost-plus — overhead, expected losses, desired margin —
which is a floor rather than a price, and one reply said so directly: profitability tells you what you
can survive, not what anyone will pay.

**What worked.** The resolution the thread converged on is to supply the anchor yourself rather than
removing it, and to choose one that flatters you. Price against the cost of doing nothing, or against
what the buyer currently pays a person to do the job manually. In a category with no direct competitor
the real comparison was never another product anyway — it is whatever your buyer is doing right now
without you, which always has a cost even when nobody has written it down. That reframing does two
things at once: it gives the buyer the reference point they need in order to decide at all, and it
puts the reference point on ground where you win. The other concrete piece was about the early-adopter
discount the founder was already running and did not know how to end. Tie the window to a number rather
than to a date — pricing for the first fifty customers, not pricing until the end of the month. It
never looks arbitrary, it does not expire embarrassingly during a slow month, and it gives you a clean
public reason for the price going up. One further caution came from someone who had watched founders
do this badly: "no direct competitor" is usually a research failure rather than a fact, and the founder
in the thread half-conceded it, describing plenty of adjacent offerings that bundled things differently.
Adjacent products are anchors whether you acknowledge them or not, because your buyer will use them.

**The lesson.** You cannot price in a vacuum and neither can your buyer. When there is no competitor to
compare against, name the alternative yourself — the manual process, the person currently doing it, the
cost of the problem continuing — and price against that. Use cost-plus to find the floor you cannot go
below, never as the method. And if you are discounting to get started, expire the discount on a
customer count rather than a calendar date.
*(via a founder thread on r/Entrepreneur)*

### 69. The cost per order fell because the customer got worse

**The pain.** You raised the budget and your cost per acquisition improved. Substantially. And instead
of relief you have a feeling you cannot yet justify — that the platform has not found you more of your
customer, it has found you a cheaper kind of person.

**The struggle.** An operator running a direct-to-consumer brand in India described the scenario with
enough detail to be genuinely useful. A herbal shampoo powder priced between ₹300 and ₹500, sold
through a custom site with proper conversion tracking on both the pixel and the server side, purchase
values passed correctly through both. Cost per acquisition had been sitting at ₹100–120, which fitted
the unit economics. They raised the daily budget from ₹1,000 to ₹1,600 and the cost per acquisition
fell to about ₹70. The problem was the composition of what arrived: almost all of the new orders were
cash on delivery. Every one of those requires an OTP verification and a phone call before dispatch —
they were already calling each customer personally — and carries a real risk of being returned to
origin, unpaid, after the shipping has been spent in both directions.

**What worked.** The thread was small but the top substantive reply supplied the discipline the
situation needs, and it generalises to any channel that optimises toward a cheap conversion event.
Before celebrating the lower number, compute the effective cost per acquisition: include the returns,
the failed-delivery and pickup costs, and the founder's own time on the verification calls. A ₹70
acquisition with heavy returns is worse than a ₹120 one that arrives paid, and the reported metric will
never tell you that, because the platform is optimising for the event you reported — an order — and an
unpaid order that comes back is still an order. The founder's own proposed fix was the interesting
part, and it is the right instinct handled carefully: report a lower purchase value for cash-on-delivery
orders than for prepaid ones, so the optimiser gradually learns which customer is worth more, while the
true values stay intact in the database. That is value-based optimisation used as intended — teaching
the machine your margin rather than your revenue. The caution raised in the thread is the one to
respect: you are deliberately feeding the system numbers that differ from your books, so if you do it,
do it as a single deliberate rule, write it down, keep your analytics separate and clean, and expect a
relearning period rather than an immediate improvement. The alternative on offer — a checkout feature
that hides the cash option from risky-looking customers — was rejected by the founder for a sound
reason: it also hides it from genuine buyers, and in that market the payment method is often the reason
the order exists at all.

**The lesson.** An advertising platform optimises toward the event you report, so the event you report
had better be the one that makes you money. When a cost per acquisition improves sharply during a scale
up, assume the audience changed and go and look at what changed about it. Then close the loop: send
back a value that reflects margin rather than revenue, so cheaper-to-acquire and worse-to-serve stop
looking the same from the outside.
*(via an operator thread on r/marketing)*

## Entries — 2026-08-04 (second batch)

### 70. Eight months of a comfortable explanation

**The pain.** There is no traffic. You have a reason for that, and the reason is reassuring — it is the
off-season, the algorithm is still deciding about you, the idea might be wrong. Whatever it is, it lets
you close the tab and go back to building, which is the part you are good at.

**The struggle.** A software engineer who left a full-time job to found alone posted the full accounting
of what that costs, and it is the most instructive kind of failure because nothing about it was
dramatic. The plan was sound: build a beach discovery site for Greece in September, get indexed over
the winter, ride the search season that ramps in May and peaks through August, monetise once the traffic
arrived. Winter came with no traffic, which was explained by nobody searching for beaches in January.
Spring came with no traffic, which was explained by a possible penalty, or by the hypothesis being
wrong about whether people research beaches online at all. Both explanations were plausible. Neither
was ever checked. The founder's own summary of the eight months is the line worth carrying: they had a
comfortable explanation and never tested it. Meanwhile the time went into rebuilding the product,
because that was the familiar surface, and because if the idea is the problem then working on the idea
is legitimate work.

**What worked.** At the end of May it became too suspicious to keep dismissing, and one full day of
auditing the site found it. Everything rendered in JavaScript in the browser; the crawler was being
served an empty skeleton with no indication of what any page was about. The fix took a day and a half.
The numbers on either side of it are worth writing down, because they are the argument for the day
itself: on the first of June, zero clicks, 266 impressions, average position 48 — page five. Two months
later, 65 clicks, roughly 5,000 impressions, average position 12.1, and still climbing weekly. Page
five to page two for thirty-six hours of work, against eight months of building. The bill arrived
anyway. It is now August, the season has one month left, rankings take weeks to build, and by the time
the site is genuinely competitive the tourists will have flown home. The runway is thin enough that the
founder is moving into a shared flat to reach next season.

**The lesson.** Write down the explanation you are currently using for why nothing is working, then ask
when you last checked it. An untested explanation is not an analysis, it is permission — permission to
keep working on the part you enjoy. Diagnosis is cheap and almost always cheaper than you assume: a day
of looking, against months of building. And if your business has a season, the audit is not a task you
schedule when it becomes suspicious. Missing a diagnosis by six weeks costs you six weeks; missing it by
eight months can cost you the only window in the year.
*(via a founder thread on r/Entrepreneur)*

### 71. Five thousand people used the broken version

**The pain.** You abandoned it. It was too big, you were overwhelmed, and it sat dormant. Then you
opened it up to make the repository public and found thousands of people had signed up and were posting
into a half-finished product — for something adjacent to, but not actually, the thing you built.

**The struggle.** That is close to the literal sequence a founder described. An AI fitness site built
about two years ago analysed physiques and gave feedback against training goals, with routine sharing
and progress photos. It was abandoned early. Returning to it recently, they found around five thousand
signups, most verified through email, arriving purely from search — the product's name had in the
interim become a popular term in the appearance-optimisation subculture. The revealing part was not the
number. It was that the public posts showed people asking how to improve their looks rather than their
physique. The users had quietly redefined the product. The founder took the signal and, in about a
month, rebuilt the pipeline around selfie-based feedback plus a self-care routine built on ingredients
with actual evidence behind them rather than the folk remedies the subculture trades in. That brought
roughly a thousand signups in the following month, and zero revenue. Amazon affiliate links on the
recommended products converted essentially not at all, and ads were awkward because everything sits
behind a signup wall.

**What worked.** The thread's most useful replies all pushed against the instinct to monetise the
traffic, and each named a different asset. One argued the audience is not the valuable thing; the intent
is — people arriving daily to ask how to look better constitute a demand signal that grooming and
skincare brands already pay real money to reach, and that is worth understanding before you attach a
commission link to it. Another pointed out the obvious research asset going unused: the site holds
stated goals and self-described problems from thousands of people, which is the input to a paid product
rather than a by-product of a free one. Several converged on the same next action, which is the one to
take: talk to the returning users before pricing anything, because the product was repurposed by its
users and the founder does not yet know what they value. One reply put the trap precisely — do not force
a revenue model until you know what people would actually pay for. A cautionary note came from someone
with experience in the same category: a thousand free fitness users is meaningfully more than zero and
still a long way from a business, in a space where a good share of an audience will tell you plainly
they would never pay a subscription. The affiliate result already said as much. Recommendation revenue
depends on the reader treating you as the authority they buy through, and a free tool they use in
thirty seconds has not earned that position.

**The lesson.** When users repurpose your product, they have run a market experiment you did not design
and cannot repeat. Read the result before you monetise: what they came for, what they typed, and which
ones came back. Traffic is the least valuable layer of what you now own — the intent behind it, and the
recorded evidence of it, is the part with a buyer. And an audience assembled by accident does not
convert just because you put a link on it; you have to find the thing they were already willing to pay
someone for.
*(via a founder thread on r/startups)*

### 72. A good business that will never be a big one

**The pain.** It works. It grows. Customers write to say it made their week easier and you like reading
those messages. It also takes money out of your pocket every year, and the arithmetic says it will never
be large enough to matter next to your career. You are not looking for a growth tactic. You want a way
to think about it that lets you sleep.

**The struggle.** A founder five years into a side-project SaaS laid the numbers out honestly: about
$40,000 in annual recurring revenue, growing around twenty percent a year net of churn for three years,
with roughly $25,000 of their own money going in annually to fund development. The product is complex
and sits in a non-technical niche. Their own ceiling estimate is about $1 million of recurring revenue
given the addressable market and an entrenched, fragmented competitive field — an outcome that would
merely match what they already earn in their main career. The question was not how to grow it. It was
which framework to use when a business is simultaneously a genuine success and, by the only metric
they'd been applying, not worth continuing.

**What worked.** The thread produced three moves and one question, and the question is the important
part. Someone did the arithmetic the founder had left implicit: at twenty percent compounding from
$40,000, the theoretical ceiling is more than a decade away, so the decision is not about the ceiling at
all — it is about whether running roughly this business, at roughly this scale, for the next ten years
is a good use of an hour a day. Deciding on the realistic version rather than the modelled maximum
changes most people's answer, in both directions. The three practical options were laid out cleanly.
Maintenance mode: stop funding new development, let it pay you instead of costing you, and treat it as
the thing that funds whatever comes next. Sell: the reflexive objection — too small to be noticeable
next to competitors ten to fifty times larger — was met with the correct counter, which is that small
profitable products get bought all the time by companies that want the customers rather than the code.
The sharper caveat came from a reply that named the actual test: whether it can run without the founder.
A business that needs its author is a job, and a job is worth a fraction of what a business is. Raise:
if growth is capital-constrained rather than demand-constrained, money aimed at marketing changes the
slope. That one deserved more scrutiny than it got, because nothing in the founder's account suggested
demand was waiting on spend. The cost structure is where the framework becomes concrete. Roughly
$15,000 a year of infrastructure that is hard to reduce, and roughly $45,000 for a developer to
maintain the code, with an expectation of ending that engagement within six to twelve months. Ending it
converts a business that consumes $25,000 a year into one that produces cash — and that single change
turns the whole question from an exit decision into a scheduling decision.

**The lesson.** Before you decide whether to keep a small business, price the version you would actually
run. Model the realistic growth rate over a realistic horizon, not the addressable market. Separate the
spending that buys growth from the spending that merely keeps the thing alive, because a product that
funds you and one that you fund are different businesses wearing the same revenue number. And if you
lean towards selling, ask first whether it runs without you — that answer sets the multiple long before
any buyer does.
*(via a founder thread on r/startups)*

### 73. Nobody in your market answers the phone

**The pain.** You have been told the market is saturated and that you need an edge — a better product,
a sharper offer, a real differentiator. Meanwhile every business in that market has a phone number
printed on its van, and nobody picks it up.

**The struggle.** A founder spent two months cold calling local home-service businesses and expected the
takeaway to be about sales technique. It was not. They kept a tally, calling from a local number in the
area they live in, and the tally is the story: eight companies called before a junk removal firm
answered. Thirteen before a landscaper. Eleven before a roofer. Six before a pressure washing company.
All nine residential and holiday lighting companies in the market, and not one answer. The founder's
conclusion is aimed at anyone starting a service business, and it is uncomfortable precisely because it
is not clever — the barrier to entry is low and the standard set by the competition is close to
non-existent. The marketing prescription that followed is deliberately unglamorous: flood the area with
door hangers, direct mail, local ads, yard signs, flyers, cards in cafés, knocking on doors, and route
the resulting calls to every device you own so one never rings out. Then do the work competently. That
is the whole strategy.

**What worked.** The thread's replies did the more valuable job of extending the finding past the first
ring, and this is where it becomes transferable to businesses that are not local services. The top reply
moved it one step later: answering gets you the lead, but most of that market will quote a number and
then go quiet for a week, so reliable follow-up beats the competition before you have done any of the
work. Another moved it a step further still, into the part almost nobody handles. A customer who called
eight companies has to compare eight quotes, and frequently has to show them to somebody else — a
partner, a property manager, whoever signs. Most businesses say a number out loud on the phone and
expect it to be remembered. The one that sends something the buyer can forward wins by default, because
it is the only quote still in the room when the decision gets made. A dissenting reply is worth keeping
too, since it prevents the wrong generalisation: one service-business owner said they no longer answer
their phone at all because it is only ever salespeople, and their actual customers book online. That is
the honest boundary on this. The advantage is not the telephone. It is being reachable through whatever
channel your customers actually use, and answering faster than anyone else does.

**The lesson.** In an operationally sloppy market, responsiveness is positioning, and it is available
today at no cost. Before you look for a differentiator, measure the incumbents on the boring dimensions
— how many attempts to reach a human, how long to a quote, whether the quote arrives in a form the
buyer can forward. Where those numbers are bad, being easy to deal with is the whole offer, and it is
one competitors find surprisingly hard to copy, because it is not a decision they can make once. It is
a process they have to run every day.
*(via a founder thread on r/Entrepreneur)*

### 74. The model recommends your competitor, and more blog posts will not fix it

**The pain.** Prospects keep telling you they asked an assistant for tools in your category and got
three to five names, none of them yours. Support hears it. Sales hears it. And the reflex — we need
more content — starts up again, which is how the last two quarters went.

**The struggle.** A founder in exactly that position stopped guessing and measured instead, which makes
this one of the few genuinely evidence-based accounts of the problem available. They logged forty buyer
prompts — not brand searches, but the real shapes people use: best tool for a given audience,
alternatives to a named product, one product versus another, cheapest option for a three-person team.
They ran them on ChatGPT and Perplexity repeatedly over a couple of weeks and recorded every brand
named and every URL cited. The expectation was that their newer posts would begin appearing if the
posts were decent. What actually happened is that the cited URL set barely moved. Out of roughly 180
citations, most of the weight sat on a small recurring set of third-party pages — the same roundups,
the same "best tools" articles, the same two competitor documents. Their own pages appeared almost
never, unless the prompt effectively contained their brand name. They also checked the unglamorous
technical layer across a couple of sites in the same position and found two distinct failures wearing
the same symptom: one site was blocking the AI crawlers while Googlebot passed fine, and another had
clean crawl access and still lost, because the engines kept retrieving the same trusted articles
regardless.

**What worked.** The reframe is the deliverable, and it is worth stating carefully. For a small
product, these answers behave less like a search ranking to climb and more like a small citation market
in which a handful of pages already own the answer. If those pages name your competitors, publishing
your twelfth post on your own domain is the slow path — you are adding supply to a market that is not
buying. Three faster and more measurable moves follow from that. Check the access layer before blaming
the message, since a broken crawler rule is a cheap fix and invisible until you look. Get named on the
pages the engines already reuse, rather than trying to displace them. And publish one primary-source
asset those pages can quote: clear pricing, a comparison that admits real limits, a small benchmark with
its sources shown — the kind of page a roundup author cites because it saves them work. A practitioner
reply added the detail that makes this worth doing at all: the trusted URL set is largely frozen, but
which brands get pulled from those pages churns considerably, sometimes within a day. So the entrenched
list is not a wall, it is a queue — get onto the pages and the churn starts working for you instead of
against you. The founder's framing of the cost is the right one for anyone with five spare hours a week:
logging twenty to forty prompts once tells you which of three problems you have — access, absence from
the trusted set, or a category currently owned by the big directories — and you cannot choose a response
without knowing which.

**The lesson.** When a recommendation engine keeps naming somebody else, treat it as a distribution
diagnosis, not a content deficit. Spend one afternoon logging the prompts your buyers actually type and
recording which pages get cited; the answer set will be narrower and more repetitive than you expect.
Then work the citation market rather than your own blog: fix crawler access, get onto the pages that
already own the answer, and give those pages something specific and checkable worth quoting.
*(via a founder thread on r/micro_saas)*

### 75. Sort by impressions, not by clicks

**The pain.** You look at the search analytics, see almost no clicks, conclude your search presence is
broadly bad, and close it. That conclusion is comforting in its way — a broad problem needs a broad
solution, and the broad solution is always "write more," which is next quarter's problem.

**The struggle.** A founder running a small tool for freelancers described the moment this broke. They
had written a post about warning signs to watch for in freelance clients — a topic adjacent to the
product rather than about it — published it and forgotten about it. Months later they opened Search
Console and, for the first time, sorted by impressions rather than clicks. That post was averaging
position 10.2 for its target term: fifty-three impressions over three months, and zero clicks. Their own
diagnosis of the number is exactly right. Position ten is the worst place to be, because it is not
page one and it is close enough that the fix is not more writing. It is a title and a couple of internal
links.

**What worked.** The change was in the sort order, which is a smaller thing than it sounds and explains
a common blind spot. Clicks measure results, and a page that is nearly ranking produces the same result
as a page nobody will ever find — zero. Impressions measure whether the engine is willing to show you
at all, which is the earlier and more actionable signal. Sorting by them separates two failures that
look identical in the click column: pages nobody wants, and pages at the edge of visibility that need a
nudge. The founder's response was the correct one, and rarer than it should be: spend the week on that
one existing page instead of writing anything new. That is the leverage in a nutshell. A page at
position ten has already done the hard part — it has been judged relevant by the engine and merely
loses the click to nine better-presented alternatives above it. Moving it up a few places changes a
zero into a stream. A new post starts from nothing and needs months to reach the position this page has
already earned.

**The lesson.** Before writing anything new, look at what you have already published and sort it by
impressions. Anything ranking around the bottom of page one is an asset that is almost working, and
almost working is a fundamentally different problem from not working — usually a title, an intro, or a
few internal links rather than a new piece of content. The metric you sort by decides which
opportunities you are able to see at all, and clicks hide the exact set of pages that are cheapest to
fix.
*(via a founder thread on r/micro_saas)*

### 76. Two kinds of buyer, and only one of them asks about revenue

**The pain.** You are trying to sell the thing you built. Every conversation opens the same way — what
is the revenue, what is the price — and you have been slowly revising your number downwards to match
the temperature of those questions.

**The struggle.** A founder narrating a live sale process day by day wrote up the moment the pattern
broke. Every buyer so far had asked the same two questions and nothing else; none had shown interest in
the idea or where it could go, which the founder came to read as simply how buyers are. Then a message
arrived from someone who opened by saying they were not the sort of people who care about revenue and
asked to hear about the platform instead. So the founder explained it — the concept, the direction, the
users, and the fact that acquiring all twelve hundred of them had cost nothing. Then gave the same
price they had been giving everyone else. The reply is the entire lesson, and it stung enough to make
the post: the buyer had expected the number to be substantially higher. The price had been set to
survive a conversation with a buyer type who was never going to buy anyway.

**What worked.** The useful separation, drawn out in the thread, is between buyers pricing an asset
class and buyers pricing a specific thing. One group is buying cash flow and will value what you built
on a multiple of what it currently earns, which for a pre-revenue product is a small number no amount of
explanation will change. The other is buying evidence that something works and can be plugged into a
distribution engine they already own, and for them twelve hundred users acquired at no cost is the
headline rather than a footnote — because it is the part they cannot manufacture. Both are legitimate.
They are not the same market, and quoting one price into both guarantees you are either wasting the
first group's time or underselling to the second. The practical implications are small and immediate.
Which questions a buyer opens with tells you which group they are in, before you name a number. Organic
acquisition at zero cost is a claim you should be able to evidence with the channel, the time period and
the retention behind it, because it is the specific thing the second group is paying for. And a price
that has been dragged down by a run of conversations with the wrong buyers is not market feedback — it
is a sampling error. The founder was still in the negotiation as they wrote, so this is a lesson
observed rather than a lesson closed, and it is worth reading as such.

**The lesson.** Whoever you spend your conversations with sets your price, so notice which market you
have been talking to. Buyers who lead with revenue are valuing an asset class; buyers who lead with the
product are valuing evidence, and evidence of cheap distribution is the rarest thing you can put in
front of them. Find out which one you are talking to before you say a number — and do not let the
questions you have been hearing most often quietly become your valuation method.
*(via a founder thread on r/micro_saas)*

### 77. Getting testers is not the problem; getting them to finish is

**The pain.** You lined up a pilot. People volunteered — genuinely interested, right profile, hands in
the air. Then almost none of them completed even the setup, and the pilot you had been planning around
quietly stopped existing.

**The struggle.** A team building an app for families with children in a narrow age band wrote up how
theirs fell over, and the sequence generalises well beyond children's software. Recruiting the right
testers was understood to be hard from the start — the profile was specific enough that posting broadly
was never going to work — and that part they had planned for. What they had not planned for was the
conversion from interested to active, which was close to zero. They offered every level of assistance
they could think of, from fully contactless onboarding through to one-to-one calls walking people
through it, and attached a financial reward for completing the pilot. Neither the help nor the money
moved it. Then the structural problem surfaced, and it is the kind that only shows up in contact with
reality: the beta distribution channel they were relying on is deliberately hardened against under-13
accounts, so any child on a device with age restrictions and an accurate birthdate had no route
into the app at all. Not a difficult route — none. The pilot was rebuilt around a full store submission
with limited distribution, at the cost of the delay and of most of the testers they had worked so hard
to find.

**What worked.** The single reply in the thread is worth more than the length of it suggests, and it
reframes the recruitment problem correctly: one gatekeeper who already has twenty families beats twenty
individual signups, whether that is a school, a club, or one active parents' group. The reasoning is
about obligation rather than convenience. People recruited one at a time have no reason to finish, and
a payment does not create one — it prices the task, which is a weaker force than a commitment made
somewhere their name is known. Recruit through a group and completion becomes social rather than
transactional. The other lesson the team drew is the platform one, and the transferable version of it is
about sequencing: verify that your intended distribution channel will physically deliver the product to
the exact person you are testing, before you spend weeks recruiting them. Age gates, corporate device
management, procurement rules, app store review policies and network restrictions all quietly decide
who can receive your software, and each one is a five-minute check beforehand and a dead pilot
afterwards.

**The lesson.** A pilot has two funnels, and the second one is the one that kills you — getting the
right people to say yes is a marketing problem, and getting them to finish is a commitment problem. Pay
does not fix commitment; belonging does, so recruit through a group that already exists rather than
assembling one participant at a time. And before any of it, check that your delivery channel actually
reaches your test population, because the constraints that block you are usually policies rather than
bugs, and no amount of onboarding help will route around one.
*(via a founder thread on r/startups)*

### 78. You have two failures, and you keep adjusting the price

**The pain.** The site looks better than every competitor's. The ads look better too, and you know how
to run them — this was your profession. The free demo gets booked and the bookings do not show up. The
few who do show up do not buy. You are thousands of dollars down and convinced you are missing something
obvious.

**The struggle.** A founder with a decade of conversion and paid-media experience described precisely
that, three months into an online language school. They had built the course and a companion app, hired
and paid a teacher to be available for demo bookings, checked the market, and then experimented with
price in every direction — below the market, at it, and above it. They tried a free demo, and people
booked and did not attend. They put a nominal charge on the first class to filter for intent, and the
bookings dried up. Across the whole period, one adult and four children actually attended, and none
converted. The instinct on display is a common and expensive one: when you cannot see the cause, adjust
the variable you know how to adjust. For someone from a performance-marketing background that variable
is price and creative, so those got tuned repeatedly while the thing actually breaking went unmeasured.

**What worked.** The best reply in the thread refused to answer the pricing question and separated the
problem instead, which is the correct move. There are two distinct failures here — most people never
attend, and the few who attend do not buy — and they have nothing to do with each other. One is about
whether the promise and the reminder are strong enough to survive the gap between booking and the
appointment. The other is about whether the lesson delivered what the promise implied. Changing price
affects both at once and tells you nothing about either, which is why three months of price experiments
produced no information. The prescribed instrument was refreshingly manual: for the next twenty
bookings, record where each one came from, whether the person confirmed the day before, and whether they
attended. Call the no-shows within twenty-four hours and ask what they did instead of coming. Ask the
attendees what outcome they were expecting and what stopped them buying. Then fix the larger drop-off
first. The sentence that ends the reply is one to keep near any polished landing page: a better-looking
site cannot tell you whether the promise or the lesson is the weak one. Both failures also have
different cheap fixes worth knowing in advance — no-shows usually respond to confirmation friction and
reminder timing rather than to price, and non-conversion after attendance is nearly always about what
happened in the session itself.

**The lesson.** When two stages of your funnel are both failing, stop tuning anything that moves both
of them. Instrument them separately, in whatever crude way is available — a spreadsheet and twenty phone
calls will do — and fix the bigger leak first. Craft skill in one discipline becomes a liability when it
lets you keep working on the thing you are good at while the actual failure sits unmeasured somewhere
you have never looked. And when nobody buys, the fastest information available is not another
experiment. It is a phone call to the people who did not.
*(via a founder thread on r/startups)*

## Entries — 2026-08-05

### 79. Half the posts in that room were read by nobody

**The pain.** You pick a community, write something honest about what you are building, post it, and get
nothing back. No replies, no votes, no signups. The obvious conclusion is that the writing was weak or
the idea is boring, so you go away to improve both.

**The struggle.** A founder who wanted to know which communities were worth writing for stopped guessing
and counted instead. They pulled listings from four founder-heavy subreddits and measured 402 posts. The
first finding reorders your expectations on its own: about half of all posts scored zero or one. Not
below average — zero, meaning nobody voted at all beyond the author's own automatic upvote. The
distribution is not a bell curve you land somewhere on. It is a handful of posts absorbing nearly all
the attention, sitting on a long flat floor of posts read by essentially no one, and anyone estimating
their odds from the front page is looking only at survivors. The second finding inverts a signal most
founders read as good news. On a lot of posts, comments outnumbered upvotes — and the expensive action
happening more often than the cheap one is a bad sign, not a good one. Voting takes a second;
commenting takes a minute. The likeliest explanation, which the founder was careful to flag as inference
rather than proof, is reciprocity: people commenting so that somebody comments back. Either way the
practical effect is identical. You will get replies in those places, and they will come from other
founders trading engagement rather than from anyone who would ever pay you.

**What worked.** The third finding is the one that actually cost them, and it is the reason to run this
before writing anything else. Removals are invisible. Browsing a community only ever shows you what
survived, so measuring how much gets taken down meant snapshotting the new listing, storing the post
IDs, refetching them later, and seeing which ones came back deleted or had quietly dropped out. Worse,
on most of these communities a removed post still looks completely normal to its own author while
logged in. Their phrasing for the consequence is exact: "people writing thoughtful posts nobody ever
saw," and then concluding from the silence that the idea was boring. The routine they ended up with is
cheap and mechanical. Rank a community by unique authors per hundred posts — a low number means a small
pool of repeat posters using it as a distribution channel rather than a community. Check whether votes
track comments. Ignore subscriber count entirely. Write properly for one place instead of copy-pasting
into five. And log out to confirm your last post is actually visible before deciding the writing was the
problem. They were also straight about the limits, which is worth copying too: 402 posts over a short
window is a rough shape rather than a measurement, vote counts are fuzzed near zero, an automated
removal is indistinguishable from a human one, and posts removed before capture are invisible, so the
removal rate they measured is a floor rather than a figure.

**The lesson.** Before concluding that your message is wrong, confirm that your message was delivered. A
community is a channel like any other and it can be measured before you spend three months writing for
it: who posts, whether attention is concentrated in a few hands, whether the engagement is reciprocal
trade, and whether your own posts survive moderation at all. Subscriber count tells you the size of a
room, not whether anyone in it is listening. And the most expensive failure in content marketing is not
a bad post — it is a good post nobody was shown, while you quietly revised your opinion of your own
idea.
*(via a founder thread on r/startups)*

### 80. Outreach that arrives with the work already done

**The pain.** You send the message. You are specific, polite, and clear about exactly what you could do
for them. Nothing comes back. Not a no — nothing. So you send more of them, slightly better written each
time, and the silence scales with you.

**The struggle.** A developer with four years of production experience described exactly this shape while
trying to reach early-stage startups. They worked the obvious channels — the startup job boards, the
professional network, direct email and chat — and the replies fell into three buckets: not hiring, no
budget, or no answer at all. They had already taken the step most people skip, and started including
specific suggestions about how they could improve a founder's site or product. Still nothing. The
failure is worth naming precisely, because it is neither laziness nor a bad list. Two replies in the
thread landed on the same diagnosis from different directions: the message was asking whether the
company needed a developer rather than demonstrating that it did, and an offer to help — however
specific — is still an offer, which means it is still a request for the recipient's time made before
they know anything about you.

**What worked.** The prescription was concrete enough to run tomorrow. Lead with a piece of work already
done, small enough that the recipient can verify it in about five minutes: a ninety-second teardown of
their onboarding, a prioritised list of bugs, a mocked-up fix, a small pull request against a public
repository. Pick twenty companies you genuinely like, find one real problem in each, fix it or draft the
fix, and send that instead of a pitch. The mechanism is not generosity, it is evidence — you arrive
having already produced something, which puts you in a different category from everyone whose message is
a claim about future value. Then follow up once with the artifact rather than with more claims. The
second half of the advice is about the list rather than the message, and it is the part most people
never reach: the companies worth contacting are usually the ones with a half-finished product and a
developer who has left, and they never post a role. You find them by noticing observable symptoms — a
product that stopped shipping, a changelog dead for four months, a founder complaining in public about
their agency. The open-roles route is the most competitive path available, where you are one of four
hundred applications being compared on the same axis by people who have never seen your work.

**The lesson.** This is founder-led sales wearing a different hat, and both rules survive the change of
costume. First, do the work before you ask, in a form the buyer can check in five minutes, because one
completed small thing outranks any description of a large one. Second, stop prospecting from the list of
people advertising that they want you — that list is exactly where all the competition already is.
Prospect instead from the observable symptoms of the problem you solve: the stalled product, the dead
changelog, the public complaint. Whoever has announced the need is being pitched by everybody; whoever
is visibly living with it is being pitched by nobody.
*(via a founder thread on r/startups)*

### 81. Nobody even clicked to see the price

**The pain.** You launch properly this time. Real traffic arrives — hundreds of people across several
days — and not one of them buys. The instinct is immediate and almost always wrong: the price must be
too high.

**The struggle.** A founder writing up fifteen months of taking a side project from nothing to around
thirteen thousand dollars had the numbers to show why that instinct misleads. Their proper launch drew
481 visitors over five days and produced zero sales, which is common enough. What made it useful is what
they checked next: not one of those visitors clicked through to look at the price. That single fact, by
their own account, taught them more than every good day since, because it eliminates an entire family of
explanations at once. Nobody rejected the number. Nobody weighed it against a competitor. Nobody reached
the point on the page where a number would have mattered. Their compact version of it is worth keeping:
"if people will not check your price, you do not have a pricing problem." The rest of that run reads as
a list of things measured too late. Two thousand people on a waitlist produced five paying customers,
and the size of the list kept them comfortable for months because it felt like having customers. Thirty
properly optimised blog posts all sat around position seventy to ninety with no clicks, and the only
term the site ranked for was its own name. Eleven months went into making the product nicer for zero
users.

**What worked.** The turn was to start reading behaviour at the step before the one they were worried
about. Once they knew the pricing page was not being reached, the work moved to the part of the page
that decides whether anyone gets that far — and the price itself turned out to have room they had
assumed away. They started at forty-nine dollars, convinced nobody would pay more, moved to seventy-nine,
then to a hundred and twenty-nine, and sales did not dip at any step, because no customer ever tells you
the number is too low. Two other observations from the same fifteen months are worth carrying. A
screenshot of real payments outperformed anything they wrote about the product: one such post drew
hundreds of votes with an empty body and no link in it, while their proper launch post the same day drew
two. And answering people directly in comment threads sold more than everything they ever published,
which is boring, does not feel like marketing, and is probably why it works. The moment that reframed
the whole problem was finding a stranger recommending their product in a thread they were not part of,
to somebody they had never spoken to — evidence that the product was fine and the distribution was
broken, which are very different things to fix and are constantly mistaken for each other.

**The lesson.** Before you change a price, find out whether anybody looked at it. Instrument the stage
before the failure you assume you have, because conversion problems are routinely diagnosed one step
downstream of where they actually happen, and the step you are staring at is usually the one you already
know how to change. Traffic that never reaches your pricing page is not price resistance — it is a
message that did not land. And when you finally do test the number, expect to be under it: the market
will tell you loudly when a price is too high, and it will never once tell you when it is too low.
*(via a founder thread on r/micro_saas)*

### 82. A three-kilobyte advantage nobody is measuring

**The pain.** You found the flaw. It is real, it is measurable, and every competitor in the category has
it. You build the version without the flaw, put it in front of people, and what comes back is polite
indifference.

**The struggle.** A developer building an exit-intent popup tool for online stores described the flaw
precisely, and the diagnosis is correct on its own terms. Store owners spend real money optimising page
speed and then load a third-party popup script weighing over a hundred kilobytes, which adds a second or
two of blocking time on mobile and undoes the thing they just paid for. So the tool was built the other
way: plain JavaScript, isolated in a shadow DOM, a compressed bundle of about three kilobytes, installed
with a single line, with a live editor, coupon and email capture, a countdown and CSV export. The
engineering is not in question. The reply that mattered was one friendly line — good luck, sounds
interesting, but I do not think this is a problem anyone has. That reaction is the whole lesson, and it
is not about whether the bloat is real. It is about who is holding the ruler. A hundred kilobytes of
blocking script is intolerable to the person who reads waterfall charts. To the person who owns the
store, the popup is a line in a revenue report, and the only question it answers is how many carts it
recovered last month.

**What worked.** The transferable move is to translate the advantage into the buyer's own accounting, or
to accept that it is not an advantage to them. Page weight is not a benefit, it is a mechanism; the
benefit sits one step further along, in whatever the buyer already tracks and already worries about. The
conversion rate that dips on mobile and nowhere else. The page-speed score a platform penalises them
for. The revenue lost between an ad click and a page that renders too slowly to keep it. Stated that
way, the same three kilobytes stop being a technical curiosity and become a number the buyer can put
next to the subscription price. The test to run before writing another line of copy is blunt: name the
metric your buyer already reports to somebody else, and show your advantage moving it. If you cannot
connect the two, you have found something true about the category that nobody is paying to fix — which
is worth discovering early rather than late, because it is a positioning problem and not a distribution
one, and no amount of channel work repairs it.

**The lesson.** A differentiator only counts if it is measured on an axis your buyer already cares about.
Technical founders are unusually good at finding genuine defects in a category and unusually likely to
price them in units nobody else uses — bundle size, query counts, architectural cleanliness — and then
to read the resulting indifference as a marketing failure. It usually is not. Convert the advantage into
a number that already appears on the buyer's dashboard, and if no such number exists, treat that silence
as the answer rather than as an obstacle to be out-marketed.
*(via a founder thread on r/micro_saas)*

### 83. A brand is a promise somebody can trace back to you

**The pain.** Somebody tells you that you need to work on your brand, and what you hear is a logo, a
palette and a font you cannot afford yet. So you file it under things to do once there is money, and
carry on.

**The struggle.** An operator who builds and runs consumer brands in-house wrote up a long argument that
a brand is a mechanism rather than a decoration, and it holds up. Strip away the modern usage and a
brand does three unglamorous jobs. Traceability: you can tell where a thing came from and who made it,
which is the foundation everything else sits on. Reputation: the general opinion held about you,
accumulated over time, which is why one phone manufacturer became shorthand for durability without ever
having to claim it out loud. Accountability: larger brands are trusted partly because they have more to
lose, and a public failure costs them in a way it does not cost an unknown seller. The framing most
likely to change how a small company behaves is the one about self-set standards. The example given is a
fast-food chain whose standard is not tasting the best but tasting the same everywhere — consistency as
the actual product, and a deliberate positioning decision rather than an absence of ambition. Most small
brands never grasp it, because they are chasing best while their customers are buying predictable.

**What worked.** The most useful contribution in the thread was not about strategy at all. It was about
where traceability actually breaks, and it breaks in boring places. The card statement shows a payment
processor's name the customer does not recognise. The emails arrive from a different domain than the
site they bought from. And now somebody is filing a chargeback because they believe they have been
scammed. Nothing in that failure has anything to do with design; it is the same brand job — can this be
traced back to you — failing at two touchpoints founders almost never audit. The rest of the practical
stack follows the same pattern of doing rather than declaring. Transparency means publishing the
unflattering reviews too, and letting the known-quantity effect work the way it works for the budget
airline everybody complains about and everybody still books, because expectations that are met beat
expectations that are flattering. Goodwill means demonstrating the position instead of asserting it: the
operator's own example is producing literature reviews of scientific papers and publishing them to a
research repository, one of which was picked up by a significant platform in their industry, which
established a science-forward position precisely because it was proof rather than an advertisement. And
the sharpest line in the replies belongs above a founder's desk — customers do not remember what you
said, they remember whether you met or missed their expectations, and "every customer interaction either
adds to your future CAC or reduces it."

**The lesson.** Treat brand as three operational questions rather than an aesthetic project. Can a
customer trace this purchase back to you at every point they will encounter it — the statement line, the
sending domain, the packaging, the support reply? Do you have a reputation for one specific thing, and
is it something you can deliver every single time rather than at your best? And are you visibly
accountable when you fail, since accountability is what an unknown seller has least of and can build
fastest? Design matters, but it is the last of the three rather than the first — and the cheapest brand
work available to most founders this week is fixing the two places where their own name does not
currently appear.
*(via a founder thread on r/Entrepreneur)*

### 84. The person who benefits is not the person who signs

**The pain.** You have costed the equipment, checked that nobody local offers the service, and priced the
job. What you have not done is name the person who will actually hand you money, and everything
downstream of that omission is a guess wearing the clothes of a plan.

**The struggle.** A developer out of steady work described a careful plan to start a hydroseeding
business — spraying seed and mulch slurry for lawns, erosion control and construction sites — beginning
with a cheap self-built rig to test on a few jobs before committing to a commercial unit. The plan was
sound in every respect except the one that decides whether the business exists. Their mental image of the
customer was a homeowner with a bare lawn, because that is who visibly benefits from the work. The
correction came from somebody who had run one: in roughly nine cases out of ten the buyer is an
excavation contractor or an estimator, because hydroseed already appears as a line item in the bids they
submit. A second operator in the same trade confirmed it and added a warning about equipment bought
before the relationships existed. The consumer-shaped picture was wrong in the expensive direction —
homeowners are one job each, a drive out and a haggle, while the recurring money sits with a small number
of contractors who need the service repeatedly and have already budgeted for it.

**What worked.** The second half of the correction is what changes the marketing plan entirely, and it
generalises far beyond slurry. Those buyers, in the words of the reply, "already know a guy and will not
be googling" — which means every channel built around being findable is aimed at the wrong behaviour.
The recommended approach was literally to walk onto construction sites and introduce yourself:
unglamorous, and correct, because the only route into a relationship-held market is proximity and
repetition. The rest of the thread filled in what to measure before spending. Build the cheap rig first,
not primarily to save money but to learn which jobs are miserable and which are worth a Saturday.
Establish two numbers before committing to equipment — what a reasonable competitor charges for an
average job, and how long each job actually takes — because the seasonality question only becomes
answerable once you know the margin per job. Pair the seasonal residential work with erosion control and
construction work that runs on a different calendar. And expect quoting and selling to consume far more
time than the work itself, which is the detail every trade estimate omits.

**The lesson.** Before anything else, separate the person who benefits from the person who signs, because
they are frequently not the same person and only one of them has a budget line. Then ask how that buyer
currently solves the problem. If the answer is that they already know somebody, you are not in a search
market and no website will get you in — you are in a relationship market, where the entry cost is showing
up where they already are, repeatedly, until you become the somebody that somebody knows. A service that
looks consumer-facing but is really business-to-business punishes the confusion twice over: the wrong
customers are the ones who find you, and they are the least profitable ones you could possibly serve.
*(via a founder thread on r/Entrepreneur)*

### 85. The middle of the market went first

**The pain.** Sales that used to arrive have stopped arriving. Existing clients are trimming their
budgets. Nothing you can point to has changed about the quality of your work, so the explanation you
reach for is the economy — and the economy is not something you can act on.

**The struggle.** Somebody at an agency serving home-services businesses laid this out and asked whether
everyone else was seeing it too. Their situation carried a specific and troubling detail: their clients
were in a vertical that is supposed to boom over the summer, and no boom arrived. The replies did not
agree that this was simply the economy, and the shape of the disagreement is the useful part. Several
people in the same vertical confirmed the stalled pipeline. Others reported the opposite — one small
agency owner said business was better than ever and turnover had always been low, a four-person shop
described staying afloat across a wide spread of services, and someone working mainly with government,
business-to-business and non-profit clients called their year normal. Meanwhile a full-service agency of
around thirty people had shed roughly a third of its staff over two years through cuts and unfilled
roles. The pattern named in the thread accounts for both halves at once: the two groups doing well are
the very large agencies with scale on their side and the small specialised boutiques, and everyone in
between is being squeezed. The second force is the one that will not reverse when the economy does —
clients are bringing the work in-house, and the tooling has made that genuinely manageable with one to
three people. One person who works with small and mid-market companies added the detail that stings:
plenty of founders actually enjoy running the ad platforms themselves.

**What worked.** The reframe is to stop treating this as a demand question and start treating it as a
positioning one. A general offer of managed websites, ads and search work is precisely the bundle a
capable in-house hire can now assemble, which means the thing being sold is convenience — and
convenience is the first line cut when budgets tighten. What survives at the small end is not being
cheaper but being specific: a defensible niche, a vertical whose operational details take years to
learn, or a service where the client's own attempt fails visibly and quickly. Three diagnostic questions
follow, and they are worth running against any service business right now. Would a competent generalist
inside your client's company produce eighty per cent of your result — because if so, you are selling
hours rather than outcomes. Are your losses concentrated in one vertical, which is a market problem, or
spread evenly across all of them, which is a positioning problem. And is the pipeline stalling at first
contact, which is demand, or at the proposal, which is a value argument that has stopped landing.

**The lesson.** When a market contracts it does not contract evenly — it hollows out the middle, and the
middle is defined by generality rather than by size. Being the biggest is a position and being the most
specialised is a position; being a competent full-service option is a convenience, and convenience is
what a client replaces with an internal hire the moment the budget is questioned. If your revenue is
softening, resist accepting the economy as the explanation, because it is the one diagnosis that implies
no action. Ask instead what specifically your client would have to give up by doing this themselves, and
if the honest answer is not much, that is the thing to go and fix before the next renewal.
*(via a founder thread on r/marketing)*

### 86. You already have the distribution; the problem is what happens next

**The pain.** Traffic is not your problem. Something you built years ago still brings people in every
day, reliably, for free — and almost none of them stay. So you plan a rebuild, and the rebuild is aimed
at everything except the reason they leave.

**The struggle.** A founder posted about an Android voice assistant they had built seven or eight years
earlier while learning the platform. It still takes around four hundred organic installs a day from the
app store, entirely without spend, the result of store optimisation compounding quietly over years.
Retention is poor, because the product is the older style of fixed buttons and voice commands. The plan
was to rebuild it as a modern assistant with tool calling, memory and device automation, and the open
question was how to monetise the result. What is worth noticing is what those numbers already prove and
what they do not. Four hundred installs a day is a distribution asset most founders would trade a year
for, and it is not a hypothesis — it is running. Retention is the only unproven part of the business, and
it is what the rebuild is meant to address. But a rebuild is also the fastest available way to break the
listing signals that produce the installs in the first place, and that cost does not appear on any plan.

**What worked.** The replies pushed in the right order, which is retention before monetisation: get the
core experience fast and reliable first, expand capability second, charge third — because a subscription
attached to a product people abandon in the first week converts a retention problem into a refund
problem. The most useful caution was about the existing users rather than the prospective ones. Make new
behaviour optional rather than replacing what people already use, since a portion of any established
base has strong feelings about being moved onto something they did not ask for, and churning them costs
you the very retention the rebuild was supposed to buy. The sharpest question in the thread was the
positioning one, asked by somebody trying to understand where the installs come from at all: what does
yours do that the assistant already built into the phone does not? That needs an answer before the
rebuild starts, because rebuilding towards a general-purpose assistant means competing with the one
preinstalled on the device, on its terms, with its distribution. The founder's own reply was honest
about it — the new version would essentially be the built-in assistant, which the current one is not.
The existing product's advantage is that it is different, and the plan quietly proposed removing it.

**The lesson.** When you already own a channel, treat it as an asset with a balance rather than a fact of
nature. Every rebuild spends some of it, and the spend is invisible until the installs drop. Fix the
stage that is actually failing, in the smallest version that tests the fix, and keep whatever your
current users chose you for available while you do it. Above all, work out what you have that the
default option does not before rebuilding yourself into a slightly worse copy of it — because the
version of the product that earned the distribution and the version you are excited to build next are
not automatically the same product.
*(via founder threads on r/startups)*

### 87. Every question except the one that matters

**The pain.** The product works. The site is up. And the thing standing between you and a real company
appears to be a stack of decisions about entities, jurisdictions, co-founders and investors — none of
which you know how to make, all of which feel like the responsible next step.

**The struggle.** A first-time technical founder building an authentication and authorisation product for
AI agents, intending to sell internationally, laid out exactly that stack. Where to incorporate, and
whether the answer changes for international sales. Which firm should handle the paperwork. Whether to
raise now or wait for pilots and usage. Whether a co-founder is needed at this stage, and what they
should bring. The list is thorough, honest, asked in good faith, and every question on it is real. It is
also, taken as a whole, a description of a business that has no users yet. Two replies made that point
without much cushioning: one observed they were working on step one hundred before steps one and two,
another that the incorporation question resolves itself once you can see where the first customers
actually are. The trap here is not laziness. Legal and structural questions have the enormous advantage
of being answerable — there is a correct-sounding answer to each, arrived at by reading rather than by
exposure, and not one of them can reject you.

**What worked.** The advice converged on inverting the order, and on a single question that reframes the
rest: is anybody using the prototype right now? Everything else is downstream of that answer. Find
design partners and pilot customers first and validate that the problem is real, that the product fits
how they actually work, and that the price is defensible. A pilot can generally run before there is a
company at all, and the jurisdiction question answers itself once you can see where your first five
users sit rather than where you imagine your market to be. Incorporate around the point of the first
sale, so that you are selling as a business rather than as a person. Approach investors with pilots and
usage rather than with a prototype and a plan, because for a security product sold to technical buyers
the pilot is the evidence and the deck is only a description of it. And treat the co-founder question the
same way: it is really a question about which work is not getting done, which you cannot know until you
have tried to sell something and watched where it stalled.

**The lesson.** When you are stuck, look at which questions you have been working on and check whether
any of them could be answered by a stranger telling you no. Entity type, jurisdiction, agency selection
and fundraising sequence are all real questions, and all of them can be researched indefinitely from a
chair, which is exactly why they expand to fill the time you are avoiding customer contact. Order the
work by what is unproven rather than by what is unresolved. For almost every product before its first
users, precisely one thing is unproven — that somebody with a budget has this problem badly enough to
let you near it — and most of the questions you settle before that one will have to be settled again
once the answer arrives.
*(via a founder thread on r/startups)*

## Entries — 2026-08-06

### 88. The ten seconds you asked for before you gave anything

**The pain.** Half the people who click your main button never come back from the page you send them
to next. Not a paywall, not a price — just a form asking who they are, before they have seen the
thing work.

**The struggle.** A founder spent several days watching session replays rather than dashboards, and
the recordings showed the same shape over and over: homepage, action button, sign-up screen, gone.
The drop at that one step was around fifty per cent. What makes this worth sitting with is how
invisible the problem was from the metrics side. There was no paywall on this product and there
never had been — no trial, no card, no upgrade prompt. The founder had reasoned that since the thing
was free, asking for an account first was a trivial request: ten seconds of typing in exchange for
something that costs nothing. Every part of that reasoning is correct except the part that matters,
which is that the visitor at that moment has no evidence the product does anything at all. They are
not weighing ten seconds against a free tool. They are weighing ten seconds against the possibility
that the next screen is also a form.

**What worked.** The change was one of sequence rather than of product: homepage, action button,
actually perform the action, then ask for an account to see the results. Same steps, same fields, one
reordering. The bounce at the sign-up step fell from around fifty per cent to twenty-two. Two
mechanisms are doing that work and they are worth naming separately, because only one of them is
honourable. The first is evidence — by the time the account request arrives, the visitor has watched
the product do the job, and the ask has become a small price for something they can now see. The
second is sunk cost: they have spent five minutes filling in a form, and abandoning now feels like
waste. The founder was uneasy about the second and said so, drawing the line at a paywall. This
pattern is manipulative when the thing behind the door costs money and the user did not know that
going in; it is simply good sequencing when it does not.

**The lesson.** Every field you ask for before the product has demonstrated anything is priced by the
visitor in units of risk, not units of time. Move the demonstration in front of the ask and the same
ask stops being expensive. Then run the ordering test across the rest of it — the signup, the pricing
page, the demo request — and find every place where you are asking for something before you have
shown anything. And if the reorder only works because leaving would now feel like wasted effort, be
honest that you have built a trap rather than a case, and make sure there is nothing waiting behind
the door that the person would have refused up front.
*(via a founder thread on r/startups)*

### 89. The one user who depends on you is not a market

**The pain.** Your co-founder uses the product every day and could not do their job without it now.
So you launch it publicly, with a free trial, and nothing happens. No traffic, no trials, no users.
The proof you thought you had does not seem to transfer to anybody else.

**The struggle.** A software engineer built a patient-management and clinical-notes tool together
with a relative who is a cardiologist. The doctor used it daily. The engineer refined it around what
the doctor asked for. Over months the doctor came to depend on it for actual patient work, which is a
real signal and a rare one. Then they opened it to the public and struggled to get any traffic at
all, seven-day free trial included. The replies took the proof apart politely but clearly. The
cardiologist shaped the product, which means the fit being celebrated is fit with one workflow —
whether other cardiologists have the same problem, in the same shape, without months of
customisation, is entirely untested. One reply noted that no alpha or beta had run with anybody
outside the pair. Another pointed out what nobody in the thread had raised at all: not one person had
said a word about who else already sells this.

**What worked.** The strongest advice inverted the channel rather than improving it. Stop marketing
to strangers. In medicine, practitioners do not buy from advertising or cold software pitches; they
buy from other practitioners. So the cardiologist should approach his immediate peers — and approach
them for advice rather than for a sale, because the request that gets a meeting from a busy
specialist is whether this is wrong, not whether they will buy it. His daily dependence on the tool
becomes the credential: this is not a demo, it is the thing running his own practice. From there the
sequence is concrete. Get three practices using it. Ask each for a review once there is real usage
behind it, and put those on the site, because in this market the testimonial is the marketing. And
use those same three to test procurement alongside product fit — before any pilot, establish who
approves software that touches patient data and what evidence that person requires, then agree on one
workflow and one measure of success.

**The lesson.** A single delighted user who helped you build the thing is evidence that the problem
is real and no evidence at all that the product is general. What has been proved is that this
workflow, for this person, is worth depending on; the distance between that and a market is the
entire job. In any field where buyers trust each other more than they trust vendors — medicine, law,
trades, education — the founder's own network is not a shortcut to distribution, it *is* the
distribution, and it stays that way far longer than any marketing plan assumes. Sell through your
power user's peers, ask for their judgement rather than their money, and find out who signs the
contract before you find out whether they like the software.
*(via a founder thread on r/startups)*

### 90. Somebody wants to sell you credibility

**The pain.** A magazine messages you: they are compiling a list of the most promising companies in
your category this year, and yours could be on it for a fee. Your first instinct is that this is
pay-to-play. Your second is that every company you admire seems to have a strip of logos.

**The struggle.** A founder did what almost nobody does with those emails, which was proper
diligence. They checked the publication's following, its reviews, its social presence and its
readership, and it held up — a real outlet with a niche audience, publishing business and startup
content rather than running a pure award mill. They went further and contacted founders featured in
earlier editions, and the reports came back positive. Then the catch surfaced: the feature required a
recorded on-camera interview with no audio-only substitute, and the founder is camera shy. While
researching, they mapped the wider landscape into three tiers — the famous titles with enormous fees,
heavy vetting and genuine prestige; a middle tier with modest fees, decent reach and demanding
requirements; and a long tail with almost no requirements, negligible readership and low prices,
which sells you a cover with your face on it that photographs well and does nothing else. The
question they were stuck on was whether the video requirement was a reason to walk away or a sign of
quality.

**What worked.** The thread produced two lines of response, and only one of them addresses the actual
decision. The first was operational: practise beforehand, ask for the questions in advance, record
yourself and watch it back, and treat this as low-stakes — a solo founder will have to be
public-facing eventually, and this is a mild place to start. The second reframed the whole thing, and
it is the one worth keeping. Does being featured help you *right now*, and do the people you are
trying to reach read this publication? If the goal this quarter is user growth and your buyers have
never heard of the outlet, the feature is a purchase of self-image rather than of distribution. Note
also what the diligence did and did not establish. It confirmed the publication is real. It did not
establish that a feature moves anything, because the previously featured founders were asked about
the process, and a good process is not a result. The unasked question is the only one with a number
attached: did anybody who was featured see a single customer arrive from it?

**The lesson.** Paid credibility is a real product with real buyers, and the question is never
whether it is legitimate but what job you are hiring it to do. Logos on a landing page shorten a
conversation with a cautious enterprise buyer; they do nothing for a self-serve product whose users
will never see the article. Before you pay, write down the specific place the credential will be used
and the specific person whose objection it answers. If you cannot name that person, what you are
buying is reassurance — a legitimate purchase, but a different one, and available much more cheaply
elsewhere. The camera, meanwhile, is a separate question, and you will have to answer it either way.
*(via a founder thread on r/startups)*

### 91. Fifteen strangers already paid you

**The pain.** Six months live on both app stores with no marketing at all, and five hundred
downloads. Small numbers by any measure. But fifteen of those people are paying subscribers — six
monthly, nine annual — and not one of them knows you.

**The struggle.** A founder built a time-management app after searching the stores for something that
solved a particular problem, finding nothing, and being surprised enough by that to build it
themselves. Six months in, the numbers above, achieved with virtually no marketing. The audience it
resonates with most turned out to be people with ADHD and executive dysfunction, though it is useful
more broadly. The founder's framing of their crossroads is the interesting part: they are not a
marketer, they do not want to throw money at ad platforms and hope, and they want to do acquisition
properly — tracked sources, measured channel conversion, tested messaging and creative. Which led
them to the question of whether to raise a small pre-seed specifically to fund acquisition
experiments and establish what a customer costs against what one is worth, and whether an angel would
even look at five hundred downloads and fifteen subscribers.

**What worked.** The replies did not so much answer the fundraising question as dissolve it. You can
run those experiments now, yourself, starting at fifty dollars a day on one ad platform. That is not
a smaller version of the plan — it is the plan, and money was never the constraint on it. What
raising would actually buy is permission to skip the uncomfortable part, and the uncomfortable part
is where the answer lives. There is a second thing hiding in these numbers that matters more than the
budget. Three per cent of downloads converted to paid with no onboarding funnel, no email sequence
and no marketing at all, and nine of the fifteen chose the annual plan — people do not pay a year up
front for something they are unsure about. Meanwhile the audience selected itself: a specific group
with a specific condition found this product without ever being targeted. That is the advertisement,
and it was handed over for free. So the first fifty-dollar test is not "which channel works" in the
abstract. It is whether spend aimed at exactly that group behaves better than the accident that
produced the current fifteen.

**The lesson.** When you have paying strangers and no marketing, the missing input is almost never
capital. Investors price the risk you have already removed, so raising money before you can state
what a customer costs is asking somebody else to fund the very experiment that would have made the
raise straightforward. Run it at the smallest scale that produces a real number, and let the number
decide. And when a niche selects you unprompted, treat it as the most expensive piece of research you
will ever be given for nothing, because targeting the group that already found you is the one test
that starts with evidence behind it.
*(via a founder thread on r/startups)*

### 92. Marketing money you had not been paid yet

**The pain.** A six-figure deal you spent weeks on dies. You had not merely been counting on the
money — you had already assigned it, to the one activity that reliably converts spend into customers.
The plan is still the plan, at a third of the size, out of your own pocket.

**The struggle.** A founder about a month past launch, with steady adoption and growing recurring
revenue, was deliberately building a small profitable business rather than a venture-scale one; the
stated target was the revenue at which they could leave their job for the same income, which they
considered very doable. Then somebody approached wanting to license the technology on a
non-exclusive basis for several years, low six figures. Weeks of due diligence followed. It did not
close. The founder was candid about having counted on it, because they had reached the position where
money spent on marketing turns directly into paying customers — a lovely place to be and a dangerous
one to plan around with funds that have not arrived. The same plan now runs on personal money at
roughly a third of the budget, with six to twelve months before those contributions come back. And
underneath the disappointment sits a sharper worry: the diligence process handed the other side a
detailed view of the unique thing that made the technology worth licensing, and they may now simply
build their own version of it.

**What worked.** The most useful replies separated the emotional loss from the state of the business,
which is unchanged and fine. Someone facing the same situation that week said they intended to get
the contract signed before showing the demo, which is the practical lesson stated as a rule: stage
what you disclose against what has been committed, because diligence before signature is a free
education for the buyer. Others pushed on the founder's own finances — reinvesting every pound is
admirable until a failure takes personal assets with it, and paying yourself something early is risk
management rather than a reward. One reply pointed at a channel the founder was better placed to use
than they realised: people who have just received a large bill from an incumbent are a far
higher-intent audience than any launch spike, and that intent is targetable. And one asked the
question the founder had not — was there any feedback on why the deal died, or was it silence,
because those are different situations and only one of them is recoverable.

**The lesson.** A deal is revenue when the money is in the account, and treating it as budget any
earlier converts an ordinary disappointment into a stalled plan. Keep the version of the roadmap that
runs on money you already have, and let anything larger be the accelerant rather than the engine.
Then, separately, remember that an evaluation process is disclosure, and disclosure is permanent.
Decide in advance which parts of how it works you will show at which stage of commitment, because the
value in a small technology business is usually one or two specific things, and there is no way to
un-show them.
*(via a founder thread on r/startups)*

### 93. The badge does not fix the problem you have

**The pain.** You are about to start documenting the build in public — short videos, consistent
posting, an audience that carries over into whatever you do next. And the first question you find
yourself asking is whether you need to pay for the verification badge to be seen at all.

**The struggle.** A founder asked exactly that, framing it as visibility and reach, and adding that
the goal was also to connect with investors and other founders. The most useful reply granted the
premise and then took it apart. The paid tier does help mechanically — replies rank higher, longer
posts become possible — but it does nothing about the actual constraint, which is that nobody follows
you yet. Boosting a reply that no one would have engaged with only places it higher in a thread
nobody is reading. That is worth sitting with, because it describes an entire class of marketing
spend: buying amplification for content that has not yet earned attention multiplies zero. The thread
got blunter from there. Several people argued that building in public mostly serves people who want
to be seen as founders rather than to have customers, on the grounds that the audience watching
founders build is other inexperienced founders and not buyers. Another asked the question that
actually decides it — for every minute spent on this, what is not getting done, and why is this the
most important thing?

**What worked.** The advice that survived scrutiny was about specificity rather than platform.
"Build a network and increase visibility" is not a goal, because nothing can be measured against it
and any activity at all satisfies it. The workable version is knowing precisely where your niche
sits and aiming at it deliberately. One reply added a reframe that costs nothing to adopt: talk about
the problem you are solving rather than the thing you are building, because people with that problem
will read the first and only other builders will read the second. And on the investor question the
correction was flat — the choice of social platform has no bearing on it, and there are several
stages between an idea and that conversation which content does not shorten.

**The lesson.** Before paying to amplify a channel, establish that the channel produces anything at
zero cost, because paid reach is a multiplier and the thing being multiplied is usually the number in
question. Then check who is on the other end of it. An audience of people doing exactly what you do
is pleasant, useful for morale, and very frequently mistaken for a market — it will not buy, and the
hours spent building it are hours not spent in front of people who would. If you cannot say which
specific person you are trying to reach and which problem of theirs you are addressing, no amount of
consistency or verification will fix it, because the reach was never the broken part.
*(via a founder thread on r/startups)*

### 94. Every detail vanished when somebody asked

**The pain.** You keep reading that people are making a million a year alone with AI. You have gone
looking for one concrete example — what they sell, to whom, how the first customers arrived — and
every trail ends in somebody's cousin's roommate.

**The struggle.** Somebody posted that frustration plainly, asked for real numbers rather than
theory, and got one of the more useful pieces of free market research you can read. Three
explanations came back. The first is measurement: annual recurring revenue is quoted where profit is
meant, and it is trivially inflated — make a few thousand in sales on launch day, multiply, announce
a figure. Several people described that as the standard move, and several more pointed out that
revenue without costs beside it says nothing at all. The second explanation is that the business
model behind the claim is frequently the claim itself, since the person explaining how to make a
million alone often makes their money from people who want to make a million alone. The third came
from the handful of people in the thread who actually had numbers, and it is the part nobody repeats.
One described a solo AI product at two million a year. Another was doing three and a half million
with two people in e-commerce. A third had a six-month, fifty-thousand-dollar advisory contract for a
few hours a week doing deeply unglamorous back-office automation — tax, legal, finance — and
reckoned it could scale considerably if they left their day job.

**What worked.** The single best observation in the thread explains why the search kept failing. The
people quietly making this money are not selling AI at all. They are doing the same done-for-you work
they were already doing, with the delivery time collapsed by tooling and the old price left intact,
and their websites say they do bookkeeping or product photography with the word AI appearing nowhere.
As one reply put it, you are "searching for a label the people actually making money have no reason
to use." Everything follows from that. The customer does not want the technology, they want the
outcome, and naming the technology invites a conversation about whether the job could be done more
cheaply without you. The label is worth using for exactly one audience — investors and other founders
— which happens to be precisely the crowd generating the unverifiable stories in the first place.

**The lesson.** When a category is loud and its examples are unverifiable, check whether the
successful version of it is simply unlabelled. Positioning around a capability attracts people
shopping for that capability, and they are usually the ones least willing to pay for it; positioning
around the outcome attracts people who have the problem and do not care how it gets solved. Then take
the same care with your own numbers. If the way you describe your business would be uninteresting to
a stranger without the technology named in it, you may have a marketing narrative where you need a
market — and if the only people who find your framing impressive are other founders, you have built
an audience rather than a pipeline.
*(via a founder thread on r/startups)*

### 95. Your best channel selects for people who will never pay

**The pain.** The thing that gets you found is the free version. It is why people trust you, why they
star the repository, why they turn up at all. It is also, structurally, the reason a large share of
them will never send you money.

**The struggle.** A founder open-sourced a scheduling assistant — a self-hostable alternative to the
booking tools everybody knows — and is running it as a small business. The model is deliberate and
stated plainly: everything open, nothing held back, the AI included rather than paywalled, on the
explicit reasoning that trust and distribution come from exactly that. Revenue comes from a managed
hosted tier, priced per seat, for teams who would rather not run infrastructure. Distribution so far
has been the repository, self-hosted software directories, and communities of people who build
things. The founder's own question was whether the hosted tier is worth building out or whether
staying pure and monetising later is the smarter early move. The thread answered it by accident. The
first substantive reply was warm and genuinely useful — somebody liked what they saw, starred the
repository, could picture themselves using it — and then named their deployment: self-hosted, on a
small crowded server of their own. That is a fine outcome for the project and a non-event for the
business, and it is the modal outcome of that channel.

**What worked.** Two things are worth separating here, because the founder was treating them as a
single decision. The open project is a marketing asset and it is working: it produces trust,
attention and contributions at a cost per person no advertising channel can approach. The hosted tier
is a product for a different person entirely — somebody whose time is worth more than the
infrastructure, who has teammates, and who would rather pay per seat than maintain anything. The
mistake would be to measure the second against the traffic produced by the first, conclude the
conversion rate is dreadful, and start withholding features to fix it, which breaks the asset that
was working. The right instrument is to go and find where the paying person already is, since
directories and builder communities are full of people who self-host by preference. Notice, too, what
happened when a real constraint surfaced in the thread: the commenter needed a lighter deployment,
and the founder committed on the spot to building it. That is the free tier's roadmap being set by
somebody who will never buy the paid one — which is perfectly fine, as long as you know that is what
is happening.

**The lesson.** Every acquisition channel selects for a type of person, not merely a quantity of
them, and free-and-self-hostable selects hard for the person who would rather do it themselves. That
is not a flaw in the model; it is the price of the trust and reach the model buys, and the two cannot
be pulled apart. So do not judge an audience by its conversion rate to a product it was never the
audience for. Keep the open project as the reason people know you exist, and go and find the buyer of
the paid version somewhere else, carrying the credibility the open one earned you.
*(via a founder thread on r/micro_saas)*

### 96. Making the new thing measurable before you can measure it

**The pain.** Every monthly client call now contains the same question: how do we look inside the AI
assistants? You have rankings and organic traffic and neither of them answers it, and "we are working
on it" is not a slide.

**The struggle.** Somebody running client reporting laid out the bind precisely. The existing metrics
do not fit — forcing AI visibility into keyword rankings and session counts is the wrong shape — but
the alternative on offer felt worse: running five prompts by hand once a month and calling it a
methodology. Clients accustomed to proper dashboards will not accept that as evidence, and they are
right not to. The underlying difficulty is real rather than a reporting failure. There is no ranking
slot to own inside a generated answer, no stable position to track, and the same question asked twice
may not produce the same response. The thing being measured genuinely does not have the property the
old metrics assumed it had.

**What worked.** The practice that came back from people actually doing this is modest and
defensible. Keep it entirely separate from the organic report rather than blending it in. Choose ten
core questions the client's buyers actually ask — real buying questions, not keywords. Run them once
a month and record two things: whether the brand is mentioned, and whether it is cited. It is
tedious, and the reason it works anyway is that clients understand it, which is most of the job. One
person added the framing that makes the slide legible: report visibility as whether you are cited,
traffic as referrals arriving from AI tools, and business impact as enquiries or leads that mention
one — three separate lines rather than a composite score nobody can interrogate. The reframe to hand
the client alongside the numbers is that this is about being part of the answer rather than owning a
position, which sets the expectation correctly before the first month where the trend moves the wrong
way for no visible reason.

**The lesson.** When a channel appears that your existing measurement cannot describe, the failure
mode is not having no number — it is quietly continuing to report the old numbers as though they
covered it. Build the crude, transparent instrument early: a fixed set of real buyer questions, a
consistent schedule, and a binary result you can defend line by line. A small honest methodology a
client can follow beats an automated score they cannot question, and it establishes the baseline you
will need in six months when somebody asks whether any of this is improving. Do it before you are
asked, because the version you invent under pressure on a call is the version you will be stuck
defending.
*(via a founder thread on r/marketing)*

### 97. Which side of your market is the hard side

**The pain.** The idea is genuinely clever and the technical part is entirely doable. You have
already worked out how the matching would function. What you have not worked out is which specific
people would need to show up — or why the second group would.

**The struggle.** A founder proposed a dating app that matches people on their code-hosting profiles:
contribution frequency, languages, similar repositories. The questions asked were how feasible it
was, which audience to target, and which countries would adopt it first. Every one of those is
downstream of the question the thread kept returning to. Somebody asked how women would be persuaded
to sign up, and to stay. The founder answered honestly that this was the part they had no idea about.
Somebody who had tried to build a dating app the previous year replied that this is the only thing
that matters, and described paid acquisition delivering the wrong side of the market no matter how
the targeting was configured. Others pointed out that acquisition for any dating product is brutally
expensive before you add a constraint narrowing the audience to a single profession, and that this is
why so many products in the category end up padded with fake accounts. Meanwhile the founder's own
targeting questions — which country, which audience — quietly assume the hard problem is choosing
among people who already want it.

**What worked.** The reframing on offer is simple and reaches well beyond dating. Every two-sided
product has a hard side and an easy side, and the business is almost entirely a question of the hard
side, because the easy side arrives on its own once the hard side is present. Building for the group
you personally belong to feels like founder-market fit and is frequently the opposite: you are
optimising for the side you already understand and can reach, which is the side that was never the
constraint. The concrete advice in the thread was to pick a market where money already changes hands
and compete there, which the founder found frustrating — they said they had heard it many times and
felt overwhelmed about what would and would not work. The honest resolution, in a marketplace, is
that you do not find out by choosing more carefully. You find out by trying to recruit twenty people
from the hard side by hand, before writing any code, and watching how that goes. It is a cheap
experiment, and it is the entire business.

**The lesson.** In any product where one group's presence is what makes it valuable to another, name
the hard side out loud on day one and treat every plan that does not address it as unfinished.
Feasibility, technology, geography and targeting are all answerable questions and none of them is the
constraint. Be especially suspicious when the audience you are designing for is exactly the audience
you belong to — the ease you feel is the ease of reaching the side that was always going to be easy.
*(via a founder thread on r/micro_saas)*

## Entries — 2026-08-07

### 98. The growth tool that could not grow itself

**The pain.** You have built the thing that is supposed to solve distribution, and you are on a forum
asking strangers how to get customers for it. Somebody is about to point that out, and they will not
be kind about it.

**The struggle.** A founder posted a platform that builds and manages a company's whole content
estate automatically — guides, glossaries, comparison pages, internal linking, schema, publishing
schedule, the lot — with the honest question attached: is this a business anybody would pay for? The
credentials were real and specific. The same workflow, run on the founder's own sites, had produced
twenty million search impressions in three months, a million clicks, and by their own count something
close to a hundred thousand citations inside AI answers. They posted it twice, minutes apart, in the
same subreddit. The reply that landed was the obvious one and it still stings: if the tool genuinely
worked, you would point it at your own landing page and let it do the selling. The founder answered
that topical authority takes time and that this is a side project built on the engine behind their
main venture, which is all true and none of it lands, because the commenter had already moved on to
the sharper version — "if it was working you wouldn't have to spend time spamming about this."

**What worked.** There is a real defence available here and the founder did not reach for it. A tool
that compounds over months cannot demonstrate itself in the window a sceptic is willing to watch, and
the twenty million impressions are exactly the demonstration that closes that gap — they just have to
be shown as a case, not cited as a credential in a comment. The more useful observation is buried in
the founder's own follow-up, where they describe the product as a done-for-you service disguised as
software. That sentence is the positioning, and it is being hidden rather than sold. Every question
they asked the room — is this worth paying for, would you trust software over an agency, what would
make you leave the site — is a question the room cannot answer, because the room is not the buyer.
The person who can answer it is the marketing lead who is currently paying an agency, and there is a
list of them: the businesses whose content the tool would replace are findable by the exact search
footprint the tool is built to analyse.

**The lesson.** When your product's job is acquisition, your own acquisition is the demo, and every
month you spend asking instead of showing is evidence being offered against you. If the mechanism is
slow, publish the run you already have — the numbers, the timeline, the site — so the proof exists
somewhere a stranger can inspect it in two minutes. And when you catch yourself asking a general
audience whether a business is viable, notice that you have swapped a hard question with a specific
person for an easy one with a crowd. Nobody in a forum is going to buy this. Twenty of the people
currently writing agency cheques might, and they will tell you more in one call than a hundred
comments will.
*(via a founder thread on r/startups)*

### 99. The hard part was never the screens

**The pain.** There is an obvious gap in a hot category and you can see it clearly: the tools that
build pretty pages do not build the boring working software that small businesses actually run on. It
looks like an opening. It is also, unfortunately, the idea everybody has.

**The struggle.** A founder asked whether it was a dumb idea to build an app builder aimed at small
businesses — customer records, booking forms, client portals, spreadsheet automation, driven by
plain-language instructions in the local language, in a market where hiring a developer is expensive.
The thread was blunt to the point of rudeness. Several people said they had watched this exact pitch
go past many times. One asked the only questions that matter and got no answer: "Who is going to use
it? Why can't they just use Lovable?" Another suggested skipping the product entirely and simply
building small businesses their software using the existing tools, which is a real business available
today and requires no platform at all. The word that came up repeatedly was willingness to pay, and
the room's collective verdict was that it is low — small businesses that have not bought software
this year did not skip it because the builder was too hard to use.

**What worked.** One reply reframed the whole thing and it is worth carrying well beyond app
builders. The difficult part of this problem is not generating screens. It is deciding what
*customer*, *job*, *appointment* and *paid* mean inside one specific business, and that definition
does not come out of a prompt — it comes out of an onboarding conversation, which is to say it is
already a service. The commenter then closed the loop: if one industry keeps asking for the same
intake form, that repeated form is the wedge. That is a concrete, testable instruction. Go and build
the thing by hand for a handful of businesses in one trade, charge for it, and watch which parts
recur. Another reply arrived at the same place from the other direction, advising the founder to pick
one painful workflow — booking, say, or the customer list — and find a few real businesses who would
pay for that alone before building any platform. Meanwhile the one genuinely differentiated element
in the original post, working in the customer's own language, was the thing a commenter singled out
as the part most builders never think about, and it was buried under a list of features.

**The lesson.** When you find yourself proposing a general tool for a category of buyer, check
whether the expensive part of their problem is the tool or the definitions. Software that has to be
configured to mean something is sold as a service the first several times, no matter what you intend
it to become, and the repetition across those engagements is the only reliable map of what the
product should be. Build the map before the platform. And when the room says willingness to pay is
low, do not argue with the room — go and ask five of the actual buyers for money and let their
answers settle it.
*(via a founder thread on r/startups)*

### 100. The classifier does not care what you actually do

**The pain.** Every campaign you submit is disapproved. Not for the copy, not for the landing page —
for what the system has decided you are. You are not that thing, you can explain exactly why you are
not, and there is nobody to explain it to.

**The struggle.** A founder built a search engine for pharmacy stock: type in a medication, see which
nearby pharmacies have it, useful mainly during shortages. Nothing is sold, dispensed or prescribed;
the drug catalogue is pulled from a public regulator database. Google Ads categorises the whole thing
as pharmaceutical services and rejects every campaign. Their post asks the practical questions —
whether certification actually unblocks paid ads and whether the cost and the wait are worth it, what
channels worked instead for people building in healthcare, finance, cannabis or supplements, and
which regulatory landmines they should find before the landmines find them. Buried in the middle is
the sentence that matters most, offered almost as an aside: they are starting to think paid ads may
simply not be their channel. The one substantive reply came from somebody running a locksmith
platform, a category restricted for its own unrelated reasons, who confirmed the same wall and the
same hunt for a way round it.

**What worked.** The reframe available here is that the classification is not a bug to be appealed
but a fact about the channel, and it points at a better channel. The founder had already worked out
why, and again treated it as a passing thought: people search for a specific medication near them in
an emergency. That is the highest-intent, most local, most repeatable search behaviour a product of
this kind could ask for, and it is served by exactly the surface that paid search is closed on — the
organic result, the map listing, the page per drug and per area that answers the question at the
moment it is asked. The restriction that blocks the ad does not block the page. It is also worth
noticing what the review process actually costs. Certification in a restricted vertical is not one
form; it is a queue, a document trail, and an outcome you cannot schedule, which makes it a poor
first bet for a company that needs users this quarter. The disciplined order is to build the channel
nobody can switch off, and pursue the certification in the background as an unblocking of a second
channel rather than a precondition for having one.

**The lesson.** When a platform's classifier decides what business you are in, it is describing a
risk category, not your company, and it will not be talked out of it at your scale. Read the
rejection as information: this channel is expensive or closed for anyone shaped like you, which means
your competitors face the same wall, which means the channel that remains open is where the market
is actually contested. Ask what your buyer does in the ten seconds when the need appears, and go and
be there. Regulated categories punish the founder who spends six months arguing about eligibility and
reward the one who owns the answer at the moment of the search.
*(via a founder thread on r/startups)*

### 101. Choosing the model before you have chosen the buyer

**The pain.** Two of you, both good at the work, and one clear goal: money soon, from a handful of
clients, with no investors and no empire. So you sit down to pick the business model, and you cannot
get past it.

**The struggle.** A two-person team who build workflow automation posted an unusually well-specified
version of this. The target is five to seven thousand a month at high margin, which where they live
is a good living, and they were explicit that product-market fit, scale and funding are not what they
are chasing. The choice was between a straightforward agency — take clients in any industry, build
custom each time, charge a build fee plus a retainer — and a narrower model where they pick one
customer type or one recurring workflow, build on a platform they own, and reuse most of it for the
next client. They had already reasoned their way to the second one's economics: after two or three
clients, roughly seventy per cent carries over. And then they had talked themselves out of it, on the
grounds that reuse makes it secretly a product business, and a product business means hunting for fit
— which was the thing they had ruled out on the first line.

**What worked.** The worry is a naming problem dressed as a strategic one. Reuse across clients is
not product-market fit; it is margin, and margin is precisely what a business with a small client
count needs, because seven thousand a month from five clients only works if delivery does not consume
every hour. The genuine difference between the two models is not custom versus reusable code — it is
that the second one requires choosing a customer, and that choice is the thing being avoided. This is
visible in the post itself, which spends a great deal of care on pricing structure and none at all on
who the client is. The only reply that engaged with the substance went straight there: income from a
handful of clients comes from finding people already voicing the pain you solve, and for workflow
automation those people are visible right now, describing the manual process that is ruining their
week, in public. Prospecting from a stated symptom is a different activity from cold outreach, and it
is available before either model is chosen. The reuse then answers itself — build custom for the
first two clients in one niche, and let the overlap tell you what the platform is.

**The lesson.** When you are stuck between two business models, check whether the models actually
differ in what you would do on Monday. Often they do not, and the deliberation is standing in for a
decision about which customer to go after, which is harder because it can be wrong in public. Pick
the narrowest group whose pain you can already see being described, sell to them by hand, and let the
repeated parts of the work become the asset. The model is an outcome of the first few clients, not an
input to them.
*(via a founder thread on r/startups)*

### 102. Your buyer arrives with the wrong diagnosis

**The pain.** A prospect describes their problem in detail and asks you, directly, for the thing you
sell. It should be the easiest sale of the month. It is also, quite often, a sale into a problem they
have misidentified — and the peers in the room will say so before you can.

**The struggle.** An operator posted that labour had reached thirty-seven per cent of sales and was
climbing, that they were guessing at staffing without real numbers, and that their current app just
sends shift messages with no forecasting. The ask was explicit: which software connects the till data
to a demand forecast so they can stop overstaffing dead shifts. What came back was instructive for
anyone selling into that market. The single most upvoted reply was a jeer. The second accused the
post of being a vendor advertisement in disguise. Several people said the number itself was not
obviously bad — that it depends entirely on the format and the margin, and that a business bleeding
profit elsewhere would find nothing at the end of this hunt. Others turned it into a values argument
about staff as an expense. The founder spent the thread defending an intention nobody had accused
them of, which is what happens when a request for a tool is heard as a request for permission.

**What worked.** Two replies were worth the whole thread and they said the same thing from different
ends. One operator described timing their crew for a week and finding roughly thirty per cent of paid
hours going to rework, waiting, and redoing quotes and schedules by hand — and that fixing those
moved the labour percentage further than any staffing cut would have. Their instruction was to track
what each hour actually produces for a week before touching headcount, because that is what tells you
where the leak is. The other put the same point in one line: "Bad data fed into great software is
still bad planning." And a third completed it — plenty of these businesses already have the numbers
in the till and simply never look, and the tool only helps if somebody actually cuts the shift when
it says to. The named products in the thread came up almost as an afterthought, from people who had
switched and found the forecasting worth it. Notice the order. The recommendation arrives only after
the problem has been re-diagnosed, and it arrives from a peer.

**The lesson.** If you sell software, the pain your buyer describes is a symptom they have already
interpreted, and their interpretation is part of what you are being asked to buy into. Selling
straight into a stated diagnosis is fast and it is how you acquire the customers who churn, because
the tool works exactly as promised and the number does not move. The stronger position, and the one
the room rewards, is to help them measure before you sell: a week of real observation, a baseline
they collected themselves, and a comparison against what is normal for their kind of business. You
lose a few deals you would have lost later anyway, and you gain the only thing that makes retention
possible, which is a customer whose problem was actually the one you solve.
*(via a founder thread on r/Entrepreneur)*

### 103. Automating the leak

**The pain.** Everyone around you is adding the new technology to everything, and the fear of being
the last one to do it is doing your planning for you.

**The struggle.** Somebody who builds and runs consumer brands wrote a long piece on when a business
should adopt AI at all, and the useful part was the section on when not to. Their list is short and
unsentimental: when you have not found fit, when the product is not an AI product, when the
technology adds nothing material to what you do, and when the sales process does not work. The
example is drawn from their own trade. In direct-to-consumer, you build a landing page matched to a
specific advertisement so the message and the page agree; once you have found a version that
converts, automating its production is obvious and correct. But if the page does not convert, the
automation does not fix it — in their phrasing, "you are automating lighting money on fire at scale."
Fix the bucket first. They set all of this against opportunity cost, which is the argument business
owners are worst at making, along with the costs nobody itemises: the specialists you have to pay,
the usage fees, the licences, and the person whose job becomes maintaining the thing.

**What worked.** The historical analogy the author reaches for is the one worth keeping. When the
steam engine arrived, plenty of firms bolted it onto the machinery they already had, gained a little
efficiency, and were later beaten by the ones who rearranged the factory around it. The marketing
version of that is exact. Adding generation to a funnel that leaks produces more of what was already
not working, faster, and the metrics improve in every place except revenue — more pages, more posts,
more variants, same sales. The prior question is which stage is actually broken, and it is answerable
with data you already have. Worth noting too what happened to the post itself: a long, careful,
free piece of writing was met first with a two-word dismissal calling it machine-written, and the
author's reply that length is not evidence of authorship did not change any minds. That is now the
default reception for long-form content from an unknown name, and it is a distribution fact rather
than a quality one — the same words carry differently when the reader already knows who you are.

**The lesson.** Before you automate any part of your marketing, find out whether that part works
manually, because automation multiplies whatever is already there, including the failures. The
honest sequence is to fix the conversion, prove it by hand, and only then spend money making it
repeatable. And price the whole cost when you decide — the expertise, the ongoing fees, and the
attention, measured against what the same resources would earn in the least glamorous alternative
available to you. Most of the time the boring alternative wins, which is exactly why it is worth
writing the comparison down instead of holding it in your head.
*(via a founder thread on r/Entrepreneur)*

### 104. When marketing is expected to be a switch

**The pain.** You are not lazy and you are not bad at this. You are tired of being the person who has
to prove, every quarter, that the function you run should exist.

**The struggle.** A marketer of ten years wrote that she was burned out across agency, startup, tech
and non-profit roles, and asked whether the problem was the field or the teams. The thread that
followed is the single most useful piece of reading a founder could do before hiring their first
marketer, because a hundred people in the job described the same machine from the inside. The line
that everybody agreed on was that the work becomes "justifying why someone should pay you a salary."
Several described the shape of the blame: leads are short, so marketing; nothing converts, so
marketing; the new product is not landing, so marketing. One added the part that makes it
unwinnable — it is also the only function where everyone else in the business believes themselves an
expert, so the strategy is negotiated against opinions about the colour of a font. Another laid out
the consequence with unusual honesty: when leadership expects a switch that produces leads on
demand, the people in the role learn to inflate, and the inflation is then passed downwards as
targets.

**What worked.** Two ideas in the thread are worth extracting and keeping. The first is a warning
about attribution. Several experienced people named the demand that every pound spent be traceable to
a transaction as the thing that has broken the work, not because measurement is bad but because the
demand is applied selectively — it arrives for the brand and content spend and never for the
relationship-building the sales team does, so the measurable half of the business is held to a
standard the unmeasurable half is not, and the budget moves accordingly. The second is a piece of
practical diagnosis offered to the original poster and applicable to any founder reading it: it did
not sound like she had stopped caring about the work, it sounded like she had spent years doing it in
environments that made the work feel unsafe. Underneath both is the structural fact a founder can
act on. Marketing is the function that goes first in a downturn and comes back last, which several
people who had lived through earlier recessions confirmed. That is not a judgement on its value; it
is a description of how easy it is to cut something whose contribution is deferred.

**The lesson.** If you are about to hire your first marketer, decide in advance what you will hold
them to and what you will not, and write it down while nobody is under pressure. Agree which
activities are expected to pay back this quarter and which are investments in something slower, and
apply the same evidential standard to your sales spend that you apply to theirs. Then resist the
switch model — a marketer given three months, a clear customer and a decision they are allowed to
make will out-produce the same person given a lead target and a hundred opinions. And if you are the
marketer in that thread, note what half the replies had in common: the good outcomes came from people
who changed the conditions of the work rather than their feelings about it.
*(via a founder thread on r/marketing)*

### 105. The rudest reply was the only free QA you got

**The pain.** You post your launch, ask politely for feedback, and get a comment that calls the whole
thing an abomination. The instinct is to defend it. The instinct is wrong, and this is the one
comment worth more than every congratulation in the thread.

**The struggle.** A founder launched a tool that takes your existing landing page, reads the brand,
copy, calls to action, sections and layout, and produces a redesigned version you can refine by chat
and export as code, with framework exports, templates, version history and a trial. Seventy-five
users, sixty designs generated. The first reply accused them of having simply prompted a mainstream
model into building it, and dragged on. The second was savage: the redesigns were an abomination, the
tool was contributing to bad design, and the landing page itself was a generic example of the thing
it claimed to fix. The founder's response is the part to study. They thanked the commenter and asked
which specific part was wrong. What came back was a proper defect list — every template looks
identical, the redesign is effectively the old content dropped into the template, there is no pass
that makes it feel human, and the output carries the visible tells of generated layout. The founder
explained, accurately, that the system is instructed to rebuild the hierarchy from scratch and not to
reuse the original layout, that templates are opt-in, and then conceded the only thing that mattered:
"Instructions not matching output is exactly the gap I care about closing." They asked for the worst
example. The commenter sent a project reference.

**What worked.** Three things happened there that most founders never get. A hostile stranger
performed a free evaluation of the product's core promise; the promise was tested against its actual
output rather than its description; and a reproducible failing case was handed over. That is a paid
research engagement conducted in public, and it cost one non-defensive question. The wider point is
about what the tool is being judged on. The founder is measuring signups and designs generated —
seventy-five and sixty — while the market is judging one thing, whether the result looks
distinguishable from every other generated page, and that is also the buying decision. Any metric
that does not track it is going to look healthy right up until nobody renews. Note as well that the
critic never disputed the value of the problem; they disputed the delivery. That is the good version
of harsh feedback, and it is a very different signal from indifference.

**The lesson.** When someone attacks your product in public, the reply that pays is a specific
question, asked without defence, followed by a request for the worst example they have. You will get
either a defect list you can act on or silence that tells you it was noise. And keep your eye on the
gap the founder named, because it generalises past software: what your system is instructed to do is
not evidence of what it does, and your buyer only ever sees the second one. Go and look at your own
output as a stranger would, in bulk, before a stranger does it for you in a thread.
*(via a founder thread on r/micro_saas)*

### 106. They told him what he was actually selling

**The pain.** You spent a month solving the unglamorous problem in the middle of a market, you have
the supply side signed up, and now you need somebody to be the first buyer. Nobody wants to be first.

**The struggle.** A founder built a licensing layer for using a real person's likeness in generated
advertising. The premise is a genuine gap: agencies do this with long contracts and everybody else
either avoids it or does it and hopes nobody notices. On the platform, a creator lists their face
with scoped terms — the permitted uses, territories, duration and price — a brand buys that exact
scope, and the executed licence gets a public identifier anybody can verify without an account. The
company generates nothing; it is the paperwork. Twenty-six creators between five and a hundred
thousand followers had signed. The other side of the market was empty, and the post was an open
request for one or two founders to run a pilot, cheaply, with the founder producing the advertisement
himself — explicitly because the case study was worth more than the fee. He also asked the room
whether anybody would actually click a "licensed, verify here" caption, or whether nobody cares.

**What worked.** The most valuable reply did not answer the question he asked. It told him what he
had built: "the verifiable licence feels more valuable than the AI angle itself", because usage scope
and brand safety are the real blockers. That is a positioning correction arriving unrequested. The
company had been framed around the generated-advertising trend, which is the loud part and the part
every competitor is also shouting about, when the defensible asset is a verifiable permission record
— which is worth something to a brand whether the advertisement is generated or filmed, and worth
more the more nervous the legal team is. The founder then did the right thing with the reply, and it
is worth copying: rather than pitching back, he asked the commenter, who serves brands running
campaigns, what those brands do today when they want a recognisable face — go to an agency, skip it,
or do it and not think about it. That question sizes the market from somebody with better data than
he has, and it costs nothing. The pilot offer is sound too. Trading price for a public case study is
the correct move when the blocker is that nobody has gone first, as long as the case study is the
contracted deliverable rather than a hope.

**The lesson.** Listen for the moment somebody describes your product back to you in different words
from the ones you use, because that is your market telling you which half of the thing it values.
Nine times out of ten the trend word is what got you attention and the boring word is what gets you
paid — and the boring word usually survives the trend. Then check which side of your market is
actually short. Recruiting the supply that likes being listed is not proof of a business; the first
buyer is, and buying that first proof with a discount is money well spent, provided you leave with
something you can show the second one.
*(via a founder thread on r/micro_saas)*

### 107. Validation that belongs to somebody else's market

**The pain.** The model is proven. It works elsewhere, it makes money elsewhere, and there is nothing
like it where you are. That gap looks like the safest bet you will ever take, right up until you have
to find the first customer.

**The struggle.** A developer of fifteen years went full-time on their own product: a platform of the
kind that is enormous in other countries but has no equivalent in theirs. Their framing of it was
that the idea is already validated and has great potential, because it is successful elsewhere and
solves a real problem. Their stated worries were tax, company administration, and marketing, in that
order — all the things a fifteen-year technical career does not teach. The thread was warm and mostly
about nerve; the most upvoted advice was not to make the business your identity, and a founder
twenty-seven years into running their own company gave the reassuring and correct answer that you
learn each part as it becomes necessary and pay professionals where mistakes are expensive. The
founder's own follow-up is the revealing one. Alone, with no partner, they were worried that shipping
a half-finished version would leave no time to build out their vision, because support, bugs,
features and company business would eat the calendar.

**What worked.** One short reply cut across all of it: "Build less, talk to customers more." It is
worth spelling out why that is the right correction for this specific situation rather than generic
advice. The validation being relied on is somebody else's, from a market with different buying
habits, different payment infrastructure, a different competitive default and a different reason the
product caught on. That another country adopted it proves the category can exist; it proves nothing
about whether the merchants down the road will switch, what they use today, or what they would pay.
And the absence of a local alternative is genuinely ambiguous — sometimes it is an opening, and
sometimes it is the market having already answered a question nobody wrote down. The way to tell them
apart takes a week, not a year: talk to twenty of the businesses who would have to adopt it and find
out what they use now and what it costs them. Notice also the order of the founder's worries.
Incorporation and tax are researchable, finite and comfortable; the customer conversation is neither,
and it is the only one whose answer changes what gets built.

**The lesson.** A proven model is a hypothesis with a good pedigree, not evidence about your market.
Import the mechanism if you like, but re-validate the demand locally and cheaply before you spend a
year building the port, because the thing that made it work over there — a habit, a regulation, a
rail, a competitor's absence — may be the one thing that does not travel. And when your list of fears
is dominated by the parts you can research alone, take that as a signal rather than a plan. The
frightening item is usually the informative one.
*(via a founder thread on r/Entrepreneur)*

## Entries — 2026-08-10

### 108. The side of the market with nothing to gain yet

**The pain.** You are walking into your fortieth café of the month to ask an owner to join something
that, honestly, does very little for them today. You know it. They know it within about nine seconds.
And you still have to keep the door-to-door rhythm going, because the alternative is a product with
nothing on the supply side at all.

**The struggle.** A founder posted the day their app crossed a thousand dollars in revenue, nearly
nine months after the first line of code. The product lets a customer pre-purchase coffee at a
discount — a loyalty card run backwards, money up front instead of a free tenth cup at the end. The
team spent multiple days a week walking into cafés, trying to reach an owner, and pitching a place in
a network that had almost no customers in it yet. Their own description of the offer is the most
honest thing in the post: at this stage of its life the app has "not too much benefit for a cafe
owner" to consider joining. That is the cold-start problem stated without any of the usual
decoration. Every reason to sign up is in a future the owner has to take on faith, and the founder is
explicitly relying on goodwill and on the owner seeing what the founder sees. Between that and the
first sale sat eight months of late nights, coding errors, marketing mistakes, developer problems,
and rejection after rejection.

**What worked.** Two things, and neither of them was persuasion. The first is that they kept the
grind physical and geographic instead of broad. Doors, in person, in one area, repeatedly — which
means that when the customer side finally showed up, it showed up in the same few streets as the
cafés, and the network was dense enough to be usable rather than spread across a city in a way that
would look like nothing to everyone. The second is what happened on launch day. Over two hundred cups
sold and a spot in the top hundred of the store's food and drink category, with bugs in the release
and one payment method broken for the first day. A week later there were repeat customers from that
first cohort. Look at the order of proof there. The founder could not honestly promise a café owner
traffic in month three; by month nine they could describe a launch day, a volume of cups, and people
coming back — and that is now the opening line of every conversation with café number forty-one. The
early sign-ups were bought with goodwill; the next ones get bought with evidence, and the evidence
only existed because somebody sold the unsellable version first.

**The lesson.** When one side of your market has no reason to join yet, stop trying to write a better
argument and start trying to shorten the period in which the argument is needed. Concentrate the
early supply somewhere small enough that demand can actually land on it, sell the first cohort on
belief and be candid that that is what you are doing, then move fast to convert the launch into
numbers you can carry to the next door. And do not read the eight months of rejection as evidence you
were wrong. In a business where the first customers get nothing but a promise, rejection is the
market's normal response, and the only thing that changes it is a fact you do not have yet.
*(via a founder thread on r/startups)*

### 109. The gap on the competitor grid is not a customer

**The pain.** You did the analysis properly. You mapped the competitors, you found the space nobody
was covering, you built into the space. Almost nobody is using it, and the worst part is that you
cannot see where the reasoning went wrong, because every step of it looked like the responsible thing
to do.

**The struggle.** A founder built a tool for creators chasing brand deals: it tracks the deal
pipeline, connects the creator's actual Instagram or YouTube so that the reach, engagement and
best-performing formats in a pitch are real rather than claimed, and drafts the pitch itself. They
came to a forum not to promote it but to be corrected, which is the right instinct. Their account of
why they built this is the part worth reading twice — the gap identified in their competitor platform
analysis was that the space was fragmented, so they built the unfragmented thing. That is the whole
justification, and it contains no customer. The first reply was blunt about the delivery: a language
model wired into two social accounts is not yet a product. To the founder's credit they did not
argue, conceding that the current version is thin and that they are trying to work out what creators
actually want. Then a second commenter reframed the problem entirely and, in doing so, took away the
comfortable version of it. The founder had been thinking about a marketplace with a supply side and a
demand side and a chicken-and-egg problem between them. The commenter's correction was that with
nobody on either side there is no chicken-and-egg problem at all, only "a nothing problem", and that
trying to start both sides at once is precisely how you stay at zero.

**What worked.** The most useful thing in the thread is the shift the founder made by the end of it.
Instead of building more of the tool, they landed on the idea of sourcing real campaigns from
outside, walking a creator through applying to one, and helping them actually land it. That is not a
feature; it is doing the job manually for one person until it works once. It is also the only version
of this business where you learn something true, because a creator who lands a sponsorship with your
help will tell you exactly which part of the help mattered — and it is rarely the part you built.
Note also what the whitespace analysis could never have told them. Fragmentation is a description of
the vendor landscape, not a complaint anybody has. Nobody wakes up wanting a consolidated category;
they want the deal they did not get. A market can be fragmented because it is underserved, or because
the work is bespoke enough that consolidation has been tried and did not hold, and a competitor grid
does not distinguish between those two cases.

**The lesson.** Competitor analysis tells you what exists. It cannot tell you what anybody wants,
because every square on the grid describes a supplier and none of them describes a buyer. If your
best answer to "why this?" is a gap on a chart, you have a hypothesis about the market's structure,
not evidence about its appetite — and structure is exactly what a founder can research alone, which
is why it is so appealing. Go and produce one outcome for one person by hand. It is slower than
building, it does not scale, and it is the only thing that turns a nothing problem into a business.
*(via a founder thread on r/startups)*

### 110. Two tests that kill every idea before it can be tested

**The pain.** You can build anything. That is not the boast it sounds like — it is the problem. Every
idea you generate, you research, and every one dies on contact with the same two facts: somebody
large is already doing it, or most of it could be had for almost nothing. So you build nothing, and
the ability you spent years acquiring sits idle.

**The struggle.** A developer who had been building since childhood, and had spent the years since
college building a fully automated trading system now running with real money in a real market,
described this exact block. They wanted to make something useful to other people rather than
something a lot better only for themselves, and they were disqualifying idea after idea on two
criteria: a big company already occupies the space, or eighty to ninety per cent of the functionality
is available from a cheap model. Both filters sound like rigour. Applied together, they eliminate
essentially the entire universe of software a solo founder could actually ship.

**What worked.** The thread dismantled both tests, and the arguments are worth keeping. On the first:
an incumbent in the space is proof of demand, and empty markets are usually empty for a reason, so
the founder had inverted the signal — treating evidence that people pay for this as a reason not to
build, and treating the absence of anyone as the safe ground. The better filter is reach: can you get
to one narrow slice of that proven market cheaply. On the second: the part a model does for nothing
is not the part anyone pays for. Several people building today made the same observation — the model
does the obvious work, and the business is everything around it, getting it inside the tool the
person already has open and deciding what it is not allowed to do unsupervised. Nobody pays for the
prompt. Then the structural advice, which points at the real gap. Repeatedly, in different words,
people told this founder to go and acquire a domain — through a job at a company where finding and
executing on opportunities is the actual work, through an industry learned deeply enough to see its
problems, through volunteering, through life. The blockage was never idea generation. It was that
ideas come from proximity to somebody else's frustration, and a decade spent alone with a trading
system is proximity to exactly one person's problems. The sharpest instruction in the thread was to
stop the generating entirely: "Stop generating ideas. Start collecting complaints."

**The lesson.** If you can build anything and want for something to build, you do not have an
imagination problem, you have an exposure problem, and no amount of thinking harder in the same room
will fix it. Retire both of the tests that are doing the killing — a large competitor is a demand
signal and a cheap commodity capability is a component, not a verdict — and replace them with one
question you cannot answer from a desk: whose complaints do I hear often enough to recognise a
pattern? Then go somewhere those complaints are said out loud. Also worth noticing: the founder's own
running system, with real money in a real market, is a source of specific operational pain nobody
else in the thread had access to. The domain was already there. It just did not feel like an idea
because it was familiar.
*(via a founder thread on r/startups)*

### 111. Three launches measuring the same thing

**The pain.** You have launched the same product three times. Twenty upvotes, then eight, then you
stop looking. You are excellent at the building part and you have never once been good at the part
that comes after, and you are starting to suspect that the reason you keep polishing the first part
is that it is the part where you feel competent.

**The struggle.** A designer of ten years posted exactly that diagnosis about themselves, with
unusual clarity. They can take an idea to something that works and looks right, and they trust that
completely. Getting a person who was not already looking to notice and then care enough to try it,
they had never got right, in any launch. Their description of the pattern is the giveaway:
distribution was treated as a formality that happens after the real work, so the routine was post it,
wait, watch the number. Nearly two years in on the current product, they had also spent money on ads
— global, weighted towards two large markets — got no clear result, and paused. The product itself
checks a founder's idea against real competitors and then hands the specification to their coding
tool, and the most uncomfortable moment in the thread arrives when a commenter puts a finger on
exactly that: this is work a founder is already doing themselves, so the burden is being very clear
about what you add that they cannot do alone. The founder's answer was disarmingly honest — the early
version did what anybody could do with fifty spreadsheets open and enough time, and they were
essentially selling that time. After that launch failed, they moved to something harder to replicate.

**What worked.** Two replies in that thread are worth more than the rest of the advice combined. The
first reframes what a launch even is: a repeatable channel is never the launch, it is "the narrow
place you keep showing up" long after the launch is forgotten. Three launches are not three
experiments; they are the same measurement taken three times, and what they measure is how many
people happened to be in that feed on that day. That is why the numbers went down and told the
founder nothing. The second reply supplies the replacement metric. Instead of counting upvotes, count
conversations — get ten people who genuinely have the problem onto a call and watch them use it. The
commenter who did this reported that half of them never got past the first screen, which is a fact
that will never appear in a launch post, at any upvote count, ever. Note also the sequencing failure
underneath the ad spend. Money went to traffic across two continents before anyone had established
that a visitor who arrives can get through the first screen, which means the ads were buying
impressions of an unproven flow, and the "no clear results" outcome was determined before the budget
was set.

**The lesson.** Launching is an event, and distribution is a place you keep turning up; if you only
do events, you will keep re-running one test with a decreasing sample. Pick the narrow room where
your buyer already is, plan to be a fixture in it for months rather than a visitor for a day, and
before you buy a single click, put ten real users in front of the thing and watch where they stop. If
you are builder-first, the honest thing to accept is not that you must become a marketer, but that
the discomfort you feel doing this is not evidence that it is going badly — it is evidence you have
finally left the part you were already good at.
*(via a founder thread on r/startups)*

### 112. Changing the price to fix a distribution problem

**The pain.** Sales are far too low, so you do the thing you swore you would never do: you put adverts
into a product for children, in three of the four apps, and you feel bad about it every day. The
monetisation change is at least something you control. The reason nobody is buying is not.

**The struggle.** A studio making mobile games for children with speech delay and autism posted this
exactly. One app runs on in-app purchases and subscriptions; low sales pushed them to advertising on
the other three, in products where they do not believe adverts belong. When someone asked the obvious
question — what is your acquisition channel — the answer explained the whole situation. It was
essentially one channel: a co-founder's social account with around thirty-two thousand followers, and
posts about the app going out to it. The thread quickly established two things that reframed the
problem. First, the buyer is not the user: children with a speech delay are not going to seek out a
developmental app and pay for it, and every part of the funnel is therefore aimed at a parent. Second,
and more usefully, at roughly a hundred and fifty visitors a day the site already has enough traffic
to diagnose conversion, and a commenter said the sensible thing directly — with that following and
sales still very low, "look at the funnel before spending money on ads." Adverts and paid acquisition
would both have poured resource into the top of something that was demonstrably leaking further down.

**What worked.** The strongest suggestions in the thread all replaced the channel rather than the
price. A speech or occupational therapist who already works with a family and recommends the app
carries a level of trust no social post can manufacture, because the recommendation arrives from
someone the parent already pays for judgement, at the exact moment the parent is looking for
something to do at home. Clinics and school districts extend the same logic and solve the founders'
actual grievance as a side effect: a professional or institutional licence tier, sold to the
organisation, funds the product without a single advert appearing in front of a child, and a district
can be offered the same terms for the parents of the children it serves. One commenter added the
detail that turns this from a discount into a product — build in enough reporting that a school or
therapist can track progress, because that is what the institutional buyer is actually purchasing,
not the game. The founders had already started reaching out to therapists and clinics, and were
exploring partnerships in education, which is the right direction; the thing to protect is that this
work is slow and will feel less productive than shipping an advert integration, right up until it
compounds.

**The lesson.** Before you change what you charge, check whether you have a demand problem or a route
problem. Reaching for monetisation is tempting because it is entirely within your control, but a
price change cannot rescue a product that the right people never encounter — and if your existing
audience is large and your sales are small, the traffic you already have is a free diagnosis waiting
to be read. Then ask who your buyer already trusts on this exact question, and go and be recommended
by them. Where the user cannot buy and the buyer needs reassurance, distribution belongs to the
professional in the room, and the price you charge them is a different, easier conversation.
*(via a founder thread on r/startups)*

### 113. The mess is the product

**The pain.** You assumed the hard part would be making the software good enough. It was not. The
hard part is that the process you are automating does not exist in any single, documented form, and
every customer is holding a different version of it together with people who simply know what to do.

**The struggle.** A founder automating administrative work in healthcare — pre-authorisations, claim
follow-ups, calls to payers, document handling — wrote a clear-eyed account of expecting accuracy to
be the challenge and finding something else. One insurer wants a portal submission, another wants a
fax, another wants a phone call. A portal can report a request as pending while the person on the
phone says it was never received, and both answers count as valid. There is no workflow; there are
hundreds of slight variants held together by experienced people. Their automation regularly completed
most of a task correctly and then stopped, because a payer gave a vague answer or asked something
unexpected, and the last stretch needed a human. The founder's conclusion was that full automation
was the wrong target, and that the better goal is removing the repetitive work without the operator
losing sight of what is happening.

**What worked.** The thread converged, from several directions, on the same reframing. Domain
expertise is the moat — not as a slogan, but because the mapping of that chaos is the expensive
artefact and the model is the cheap part. People with experience in other regulated and legacy-heavy
environments confirmed that half of any such project is discovering how messy the reality is, which
is precisely why the incumbent consultancies and platform vendors can charge what they charge. And a
final comment named the structural limit: the last mile is not a technical problem, it is "political",
because somebody has to own the ambiguity and organisations want that somebody to be a person. That
is not a gap waiting to be closed by a better model; it is a permanent property of the work. The
commercial consequences are the useful part for a founder. If the mapping is the value, then the
discovery work is not pre-sales overhead to be minimised — it is the product, and it should be
scoped, sold and paid for as such. If the human stays in the loop by design, then the honest promise
is hours returned and control retained rather than headcount removed, which is also a far easier
promise to survive a pilot. And if the variance is per-payer, the first version should be narrow —
one payer, one procedure, one clinic — because a system that handles one branch reliably is worth
more than one that half-handles all of them.

**The lesson.** In an industry where the process is genuinely broken, the broken process is your
moat, and the time you spend understanding it is not a delay before the real work. Sell the map, not
the magic. Be explicit about which exceptions stay human and why — vagueness from the other side,
anything touching money or care, anything the system has not seen before — because a clear boundary
is what makes a cautious buyer able to say yes. And treat the demand for full automation, wherever it
comes from, as the thing that will make your product fail its first serious test in front of a
customer who knows the work better than you do.
*(via a founder thread on r/Entrepreneur)*

### 114. The subscription label on the same hours

**The pain.** You build the thing, you get paid, you deliver, and then you are at zero again looking
for the next client. Two years of that and the arithmetic is obvious: to grow you either charge much
more per project or run more projects at once, and both of those have a ceiling you can feel.

**The struggle.** A founder running an agency that builds early product versions for clients laid this
out and proposed the fix that everybody in that position proposes. Rather than disappearing after
launch and leaving the client to hire developers, stay on as their outsourced engineering team for a
monthly fee — ongoing development, new features, maintenance, technical decisions, no equity. They
asked the right question about it, which was whether they were missing something or just putting a
subscription label on an agency.

**What worked.** The replies were unusually specific, and three of them constitute a complete answer.
The first is about who can pay. A retainer at the level this requires only survives with clients who
have revenue or funding; early-stage companies typically cannot sustain it once the initial build
budget is spent, which means the model quietly changes the customer even if the founder does not
intend it to. One person who had run operations at a custom development company that reached
substantial annual revenue put it more bluntly: selling to startups as your primary market is full of
landmines, they are price-sensitive, they push for more within the same fee, and some will try to
recruit your team. The second is about which retainers renew. The ones that survived, in a
practitioner's direct experience, were the boring ones — uptime, fixes, small changes — because that
worry never goes away and the renewal happens without a conversation. Retainers sold as a stream of
new features tend to die around the third month, when the client runs out of things they are certain
they want and starts feeling they are paying for nothing. The third dismantles the premise: "Recurring
revenue and scalable aren't the same thing." A retainer smooths the lumpiness of project work, which
is a genuine benefit, but you still add revenue by adding people, so the ceiling has not moved. If the
target really is a much larger monthly number, the lever is detaching revenue from hours — and the
suggestion that follows is the good one, that two years of client work is a pattern library nobody
else has, and that turning it into something ownable should be funded by the agency rather than
swapping the agency for it.

**The lesson.** Predictable is not the same as scalable, and a subscription that bills for
availability is still selling hours in a nicer wrapper. If you go that way, do it deliberately: sell
the boring, anxiety-shaped work that renews itself, write the scope down so ongoing development does
not become unlimited support at a flat fee, and choose clients whose funding outlasts their build
budget. And if what you actually want is a ceiling that moves, keep the services business running as
the thing that pays for the search, then build the asset out of the patterns you have already been
paid to discover.
*(via a founder thread on r/Entrepreneur)*

### 115. Forty-three people arrived and nobody paid

**The pain.** Six months in, forty-three people have signed up, an article has been written about
you, strangers have made videos about your product, and you have spent nothing on advertising. Your
monthly recurring revenue is zero. The part everybody says is hard turned out to be the part that
worked.

**The struggle.** A software engineer described the whole arc without flinching. It began well: they
were paying for an outreach tool, it worked, and inside a few weeks it had produced a client, a
developer they now contract work to, and a referral partnership. That is a genuine, specific result,
and it is the origin of the mistake — being an engineer, the next thought was why pay for this when I
could build it. So they built their own, aiming to be different by reading what people were actually
saying, pulling out the pain point, judging intent, and helping with the outreach. Then, in their own
words, they went down the path of adding features nobody had requested, on the theory that if the
product kept getting better people would eventually pay. Six months later: forty-three signups, no
paid marketing, organic coverage, an agency being onboarded that might push it to its members,
another business owner intending to use it — and zero revenue. Their summary is the honest one:
"Building software is the easy part", and building the business apparently is not.

**What worked.** The turn came at the end and it is the whole point of the story. The founder stopped
spending their time deciding what to build next and started spending it on why the people who arrive
do not convert. That is the correct move, and it is worth being precise about why this particular
founder was so well placed to make it earlier. They had been a customer of the category. They knew
the exact sequence that produced value for them — a real client, a real hire, a real partnership,
within weeks — which means they knew what the first successful session has to look like. Forty-three
people signed up and, presumably, did not reach that moment. That gap is a specific, answerable
question, and no feature added on intuition was ever going to touch it. There is a second asset in
here that is easy to miss: unpaid coverage and organic videos mean the positioning is legible to
strangers and the top of the funnel is not the problem. Most founders would trade a great deal for
that and would be right to. The bottleneck is entirely between signup and value, which is the
cheapest part of the funnel to fix, because the people are already inside and can be asked.

**The lesson.** "If I keep making it better, they will eventually pay" is not a strategy, it is the
comfortable job disguised as one — and it is most tempting precisely when building is the thing you
are best at. When you have arrivals and no revenue, the next feature is never the answer; the answer
is in the first session, and you find it by watching people take it. If you built this because you
were once the customer, write down the sequence that made it valuable to you, then check how many of
your signups ever reached it. And treat free coverage as evidence that the market understands the
promise. That is the hard half. The half you have left is the one you can actually observe.
*(via a founder thread on r/micro_saas)*

### 116. The record breaks where a human retypes it

**The pain.** You know where every lead came from. You know exactly which deals closed and for how
much. What you cannot do, at any price, is join the two, because somewhere in the middle a person
retypes the information into another system and the connection is lost forever.

**The struggle.** A marketer moving from execution work — content, search, website management — into
an analytics and attribution role described the architecture of that break with real precision, and
it is the most common shape in business-to-business software. A lead arrives through a form in the
marketing platform, engages with marketing, requests a quote. Then a salesperson or engineer manually
enters that quote into a separate, internally built operations system, and everything that follows —
the quoting, the negotiation, the close — happens over there. The marketing platform knows the source
and the campaign history. The operations system knows whether money changed hands and how much. The
two never reconnect, so the company can report activity or it can report revenue, but never one
explained by the other. Their brief was to fix this and, in the memorable phrase from the post, help
the team "stop marketing on vibes". The honest difficulty was that they did not yet know enough to
brief their own developers: what data should flow back, and which identifiers should tie the records
together.

**What worked.** The most valuable reply in the thread was not the architectural one, and this is
worth noticing, because the architecture is the easy part. Yes, an interface between the two systems
is needed, and yes it is sensible to pair the in-house developers with someone who knows the
marketing platform properly. But the reply that saves the project points at where the data actually
dies: source information is recorded against the person, and if only the quote or the deal is passed
downstream while the person's record is left behind, the origin is severed at that exact moment, no
matter how good the integration is afterwards. The fix is unglamorous and cheap — make sure the
source is copied onto the related records and that people, companies, deals and quotes are correctly
associated before any of it is sent anywhere. That is a configuration afternoon, and it determines
whether a year of reporting is possible at all. The strategic version of this, for a founder: your
attribution is only ever as good as the least automated step in the chain, and the least automated
step is nearly always a human moving information between two tools that were bought years apart.

**The lesson.** If you cannot connect marketing spend to revenue, do not start by choosing tools.
Start by drawing the actual path a customer takes through your systems and marking every point where
a person retypes something, because that is where your evidence is being destroyed. Fix the identity
first — one identifier that survives the whole journey and is attached to the person, not just the
deal — and only then argue about dashboards. A founder who does this early gets to answer the only
marketing question that matters, which channel produced money rather than motion, and a founder who
does not will be running on opinion for as long as the handoff stays manual.
*(via a founder thread on r/marketing)*

### 117. The expert you could not afford to hire

**The pain.** You are halfway through building the second one, and you already know. Not a vague
worry — the specific, named knowledge that you are missing is the same knowledge you were missing
when the first one failed. And you keep going anyway, because stopping means admitting the months
were spent for nothing.

**The struggle.** A founder wrote this up with a candour that is rare. The first product failed, and
the post-mortem was clear: a major assumption had been made without talking to enough people who had
real experience of the industry. On the second product, they recognised the same gap halfway through.
They needed somebody with deep domain experience involved, they could not afford to hire that person,
and so the choice presented itself as stop and wait until the money exists, or continue with what
they knew. They continued. The sentences they told themselves are the ones every founder will
recognise: this is still a good direction, "I'll learn by building this", perhaps these extra features
will make it work. Their own reading, afterwards, was that they were assembling reasons to keep going
because they liked the direction and could not accept what they were already seeing. It failed again.
The one substantive reply named it as sunk cost and suggested the denial might still be running.

**What worked.** The most useful correction is not the sunk-cost label, though that is accurate. It
is that the problem was framed as a hiring problem when it was an access problem. Domain expertise is
being treated here as a thing with a salary attached, which makes it unaffordable and therefore makes
continuing without it feel like the only realistic option. But the founder did not need to employ an
expert; they needed to be wrong in front of one, repeatedly, for an hour at a time. Fifteen or twenty
conversations with people who have worked in that industry cost nothing but the discomfort of asking,
and they would have tested the assumption before it became a product. That is the whole gap between
the two framings — one costs a salary you do not have, the other costs a week and some awkwardness.
There is also a practical rule hiding in the founder's own account of the second failure. They knew
at the halfway point. The signal existed, was noticed, and was overridden by narrative. The
difference between persistence and sunk cost is not a matter of temperament or courage; it is whether
you wrote down in advance what would count as evidence that you are wrong, at a moment when you had
nothing invested. Persistence in the face of a hard month is a virtue. Persistence past a condition
you set yourself is just a decision made by the version of you with the most to lose.

**The lesson.** When you identify missing expertise, ask what the cheapest form of that expertise is
before concluding you cannot afford it — nearly always it is a conversation, not a contract, and
nearly always the reason it does not happen is that the conversation might end the project. Then set
your kill criteria while you are still calm and cheap to disappoint: what has to be true by which
date, and what you will do if it is not. The failure in this story was not building without an
expert. It was carrying the doubt privately for months instead of spending a week finding out.
*(via a founder thread on r/startups)*

---

## Entries — 2026-08-10 (second batch)

### 118. Three months of silence from a market that answers in years

**The pain.** You have done everything the advice tells you to do. Cold emails to a curated list.
Compliance people added on professional networks. A post nearly every day. You even built a live
demonstration showing a real system failing in exactly the way your product prevents. Warm replies,
technical questions, a few people saying let us keep in touch. Twelve months of building and three
months of selling, and not one pilot, not one invoice.

**The struggle.** A founder building a compliance layer for AI assistants — it inspects what the
assistant is about to say and flags anything that would breach a privacy, financial or sanctions
rule — laid this out and explicitly asked for the hard version rather than the kind one. Their
evidence that the category was real was that new rules keep appearing and that a well-known
accelerator had publicly listed this exact space as something it wanted people to build. Their
target list was federal contractors and partnership opportunities. The thread did not go easy on
them. The most upvoted replies all landed on the same place: a year of building came before any
conversation with a buyer, and when someone asked directly what potential customers had said during
that year, the answer was that there had been no such conversations. The founder pushed back that
most of the year went into defining the problem rather than writing code, which is a real
distinction and also not the same as being told no by someone with a budget.

**What worked.** Three replies do the actual diagnostic work, and none of them is the sunk-cost
lecture. The first is about the clock. Federal contracting runs on a twelve to eighteen month cycle,
which means three months of quiet is not a rejection and not a signal — it is simply too early to
contain information. As one commenter put it, you have "no data yet, only fatigue," and the
exhaustion is being misread as a verdict. The second is about the gate. Buyers in that world
maintain vendor minimum requirements, and a category of certification has to be on your roadmap
before a procurement team will look at you at all. A founder who does not know which certification
their buyer requires is not early in a sales process; they are outside it. The third is the
commercial one, and it is the sharpest. The people who supply these companies with AI assistants
already claim their own guardrails, so the customer believes this is a feature they have already
paid for. Selling against that is not a matter of a better demo — it is the whole positioning
problem, and it decides whether you sell to the enterprise buying assistants or to the vendors
building them. The founder also produced, later in the thread, the one piece of genuine demand
evidence they had: four public requests for proposal in a single state in a single month. That
number is worth more than the accelerator's wishlist, and it should have been the thing the year was
organised around.

**The lesson.** Before you conclude that nobody wants it, find out how long a yes takes in the
market you chose, because a sales cycle longer than your patience will look exactly like failure
while telling you nothing. Then check whether you are even eligible — certifications, approved
vendor lists, procurement portals — since in regulated buying those are not obstacles that come
later, they are the price of being considered. And notice when an authoritative third party naming
your category is doing the job that a customer conversation should have done. A list of things
somebody wishes existed is not a list of people who will pay.
*(via a founder thread on r/startups)*

### 119. The budget that would not have saved you

**The pain.** You are marketing a small product on a small budget, and the arithmetic feels rigged.
Money makes money, you do not have any, and so you start daydreaming about the kind of spend the
film studios have — the billboard in a famous intersection, the one campaign that lands and changes
everything overnight.

**The struggle.** A founder with a fitness app posted that daydream honestly and asked what people
would do with two hundred thousand dollars: one big experiential campaign, all of it into paid
social and search, influencers, traditional media, or a split across all of them. Their own instinct
was the split, on the reasoning that you never know what will hit. They also offered the theory that
one well-placed billboard or one commercial in the right slot can launch a product almost instantly.
The thread's answer was not about allocation at all.

**What worked.** The top reply reframed the question completely: before you have proof that the
product sells, you should be spending as little as possible across many experiments, looking for one
that repeats. The founder pushed back with a reasonable-sounding hypothetical — what if you already
know people want it, like an established studio releasing a new title? The response was blunt and is
the whole section: "You are overestimating your product-market fit." That is worth sitting with,
because the hypothetical was not idle. It revealed the actual belief underneath the daydream, which
is that the product is finished and only visibility is missing. The rest of the thread filled in the
practical version. Avoid anything large and go for sustained visibility to a specific niche, and
when the founder asked where, the answer was that this is precisely the thing the money cannot buy
you — talk to a real sample of your customers and ask where they already spend their time, online
and offline, then spend there. Another practitioner added the part nobody enjoys: it takes a long
time to learn whether customers acquired through paid channels spend and stay like the ones who
arrive on their own, so a large budget bought early does not just risk wasting money, it produces
numbers you cannot yet interpret. The comparison to a film studio also breaks in a way worth naming.
A studio spends enormously because it has a hard release date, a fixed window and no chance to
iterate. A software product has the opposite shape — it can run a small test on Tuesday and a
different one on Thursday — so copying the tactics of a business with no second chance is copying a
constraint you do not have.

**The lesson.** A big budget does not solve an unproven message; it buys the same wrong message a
much larger audience. The founders who eventually spend heavily are the ones who first found a
channel that returned more than it cost at small scale, and their spending is not a gamble but a
multiplier applied to a known result. Until then, treat a lack of money as a schedule rather than a
handicap: it forces the cheap experiments in the correct order. And when you catch yourself
believing that only exposure is missing, test that belief before you fund it, because it is the most
expensive assumption in marketing and the easiest one to check.
*(via a founder thread on r/startups)*

### 120. What we have works fine

**The pain.** You have spoken to a large number of prospects. Some are already using a competitor.
The rest are doing it by hand, in spreadsheets and messages, and when you show them something
better, they say the sentence that ends the conversation without any argument in it: what we have
works fine. Now you cannot tell whether you are selling badly or building the wrong thing.

**The struggle.** Two founders building business software for small local service companies posted
this question with unusual discipline. They were already doing founder-led sales. They had already
noticed the pattern and already changed their process in response — from pitching, demonstrating and
following up, to qualifying, understanding the current workflow, identifying an actual reason to
change, and only then demonstrating. That is the correct sequence, arrived at without being told.
And it had not fixed the problem, which is why they were asking whether to change the positioning or
change the customer, how narrow to make the target before doing more outreach, and what they should
want to learn from the next hundred conversations. Nobody in the thread answered that last question,
which is a shame, because it was the best one asked.

**What worked.** The replies that did land point at two things. The first is that a prospect already
running a competitor and a prospect doing everything manually are not one market with one message —
they are two different sales, and averaging them produces a diagnosis of neither. Selling against
installed software means dealing with the contract, the switching cost and the internal person who
chose it, none of which appear when you sell to someone doing it by hand. The second is that value
has to be named in the buyer's currency rather than demonstrated and left to be inferred: time,
money or labour, said explicitly, and if it is said explicitly and they still decline, that is
information about them rather than about your pitch. The deeper point, though, is about the sentence
itself. "What we have works fine" is not an objection and should not be treated as one, because it
is the honest answer to the question the buyer thinks you asked, which is whether their business is
currently on fire. It is not. Businesses survive inefficiency indefinitely. The question that gets a
different answer is not about the software at all — it is about the last time the current way failed
and what that cost, in a specific week, to a specific person. If the founders cannot find such a
week, the process is genuinely not painful enough and the honest move is to change who they sell to
rather than how they say it. And there is a way to settle this without months of guessing, which is
the answer to their unanswered question: from the next hundred conversations, do not try to learn
whether people like the product. Try to learn who has already spent money or hours trying to solve
this themselves, because that group is the market and everyone else is scenery.

**The lesson.** When prospects agree that their process is inefficient and still will not move, you
have not found a positioning problem or a sales problem — you have found people for whom the problem
is real but not expensive. Sort your conversations by evidence of prior spending rather than by
expressed interest, and let that sorting redefine your customer. And stop measuring two different
buyers with one funnel: the people switching from a competitor and the people switching from nothing
fail for opposite reasons, and combining them guarantees you fix neither.
*(via a founder thread on r/startups)*

### 121. They tested the aggressive paywall and the free plan won

**The pain.** Thousands of people use your product. Almost nobody pays. Everyone tells you the same
thing — your free plan is too generous, make them hit a wall — and it is a satisfying explanation
because it means the fix is a switch you control.

**The struggle.** A founder with a student productivity app had posted two months earlier with 3,080
users, two trials and a single one-off sale, and had heard exactly that advice. Rather than adopting
it, they ran it as a real experiment, splitting new users three ways: the existing free plan; a
version giving everyone premium for fourteen days and then turning the app read-only; and a
usage-based version that went read-only after eighty hours of tracked study time. They expected one
of the aggressive versions to win. The plain free version performed best. So they kept the free
experience intact and worked on everything around it instead — reshaped onboarding, moved premium
prompts from generic buttons to the moments where a user repeatedly hits a feature premium would
actually improve, widened the price ladder to a monthly plan, a one-off pass covering an exam
period, a lifetime option and a shared plan for three people, added a seven-day trial with no card
required, and introduced regional pricing. The results two months on: users grew from 3,080 to
5,561, around 1,500 active monthly, and trials went from 2 to 59. Of those 59, five converted and
forty-eight lapsed. Total revenue to date, around one hundred and eighty-five euros. Acquisition,
meanwhile, had stopped being the hard part — most growth was arriving organically from search.

**What worked.** The thread's opening verdict was that this is a value problem, and it was
immediately and correctly complicated. Students are a segment with famously little money, so weak
conversion may be a fact about the audience rather than about the product. Another founder running a
freemium service added a genuinely useful observation from their own users: they advertised only the
free version, but when they asked customers what they liked, roughly four in five talked about
premium features rather than free ones — meaning the paid tier was doing persuasion work that the
marketing was not claiming. But the reply that reframes the whole situation is the smallest one in
the thread. Before concluding anything about value, price or the paywall, check how many of these
users can pay at all. A student audience meeting a card form is its own funnel with its own drop-off,
and in that commenter's experience conversion moved more from adding a payment method than from
anything done to the paywall itself. That single observation explains the failed experiment
perfectly. Forcing an audience through a wall does not raise conversion if what stops them is on the
other side of the wall. It also explains why 48 of 59 trials lapsed without a decision: a lapsed
trial that nobody had to actively cancel is usually not a rejection of the offer, it is an offer
that was never actually reached. The instrumentation advice further down the thread points the same
way — track, per cohort, whether users reach a repeat habit, which premium limit they encounter, and
what happens after, so you can tell weak value from bad timing from an audience that likes the free
utility and was never going to pay.

**The lesson.** Test the advice you are given before you build your business around it, because a
paywall experiment that fails is worth more than a paywall assumption that succeeds in your head.
And when conversion is low, walk the payment path yourself before you touch the offer: whether the
customer can physically hand you money, in their country, with the instrument they own, at the
moment they decide, is not a detail beneath pricing strategy — it sits underneath all of it. A
segment that cannot pay does not become a paying segment when you take more away from them.
*(via a founder thread on r/startups)*

### 122. The feature list is the safe answer

**The pain.** You know what you want built and you have written it all down, and the list is long
because leaving something off feels like a risk you cannot justify. Every item has a reason. And
somewhere inside it is the one thing a customer would pay for this month, buried under twenty things
they would not.

**The struggle.** Somebody who builds first versions for founders posted the pattern from two recent
projects, at roughly nine and fourteen thousand dollars. Both clients arrived wanting substantially
more than they needed — more features, more complexity, more time before anything shipped. Cutting
each down to its core made the work faster and cheaper and got real users involved sooner: one went
from an entire platform to a focused booking system, the other from a complex mobile application to
a scanning function and a basic flow around it. Their summary was that most people do not have a
building problem, they have a scoping problem, and that this is where the time and money disappear.

**What worked.** The thread turned that observation into something usable from several directions.
The most practical is a single question one commenter uses to find the real product: ask what breaks
if only one screen ships. The answer almost always names the thing the customer actually buys, and
it works because it forces a choice instead of a list. A second reply corrects the underlying
misconception — a first version is not a cheap edition of the finished product, it is an experiment,
and anything that neither tests the core assumption nor moves a user to the outcome does not belong
in it. A third comment names the failure that survives good scoping, and it is the one founders
never see coming: a booking system built in two weeks then sat unused for a month, because nobody
had agreed who was going to enter the existing customers. Nothing outside the software was ever in
scope, so the launch failed on a data question rather than a feature question. Naming who owns the
data belongs in the plan before naming the features. And running underneath the whole thread is a
commercial lesson that has nothing to do with scoping and everything to do with selling. One
commenter observed that a founder who arrives already scoped is rarer and cheaper to work with,
which makes scoping a sales skill for the builder rather than merely a blind spot in the buyer. The
proof is in the thread itself, from the buyer's side: someone described how they chose their
development partner, and the reasons were that the firm asked intelligent questions, did not promise
everything, said plainly what they were confident about and where they would need input — and
steered them to a lower tier than they had been prepared to buy. Declining to sell the larger
package is what won the work.

**The lesson.** The scope is the strategy. If you cannot say what breaks when only one screen ships,
you have a wish list rather than a product, and you will pay a builder to discover that for you at
their hourly rate. Write down who is responsible for the data and the process around the software
before you write down the features, because that is where a well-built first version most often dies
quietly. And if you are the one selling the work, understand what the buyer in this thread was
telling you: the vendor who talked them down a tier is the one who got paid.
*(via a founder thread on r/Entrepreneur)*

### 123. Ready is not a property of the software

**The pain.** You have built a pile of things over the years, for the pleasure of building them, and
now you would like one of them to make money. So you think about buying traffic, and you stop,
because you have no way of telling whether any of these projects deserves it. You can click through
your own signup and checkout, but you built them, so you will miss whatever a stranger would trip
over first.

**The struggle.** A developer with a collection of side projects and public repositories posted this
honestly, and then did the thing that the whole section is about: they converted the question into
an engineering problem. Their proposed answer was a ruthless automated reviewer that drives a real
browser through the site, exercises login and checkout, and returns a verdict — not ready for paid
traffic, fix these three things first. They asked whether other people would use such a thing or
whether they were overthinking it. The single substantive reply drew the line precisely: services
exist that will confirm a product is functionally free of defects, and that is a different claim
from being ready to advertise, which depends on the campaign and the service rather than on whether
the buttons work.

**What worked.** The useful reframing is that readiness for paid traffic is arithmetic, not quality
assurance. Before spending, you need three things, and none of them is a working checkout. You need
a conversion event you can actually observe and attribute, so that money spent produces evidence
rather than a feeling. You need a rough idea of what one customer is worth over a plausible
lifetime, because that number, not your comfort, sets the maximum you can pay to acquire one. And
you need enough budget to survive the period during which the platform is learning and the numbers
are meaningless, or you will switch it off mid-experiment and conclude something false. A product
whose flows are technically perfect and whose customer is worth eleven dollars is not ready for
advertising; a rough product with a customer worth six hundred often is. There is also a second
question hiding in the post that ads will not answer. The founder has several dormant projects and
is implicitly asking which one to back. Paid traffic is an expensive way to run that comparison,
because it will fail on any product that has never converted anyone organically and tell you nothing
about why. The cheaper test is the one the post is trying to avoid: put each project in front of a
handful of real people, watch where they stop, and see which one produces anybody who wants it
without being paid to arrive. And it is worth noticing the shape of what happened next — the
frustration immediately became a new product idea. That is the same instinct that produced the pile
of dormant projects in the first place, and turning it into another build is how the question gets
postponed one more time.

**The lesson.** When a marketing question feels unanswerable, check whether you have quietly
replaced it with a technical one because that is the part you are good at. Ads are not a test of
whether your product works; they are a multiplier on an economic relationship you have to already
understand. Know what a customer is worth and how you will see the conversion happen, and get at
least one person to want the thing without paying to put it in front of them. Then buy traffic, and
you will be buying more of a known outcome rather than an answer.
*(via a founder thread on r/micro_saas)*

### 124. The first thing you asked a stranger to do was pay

**The pain.** You launched. You need to know the payment flow works for real people in other
countries, not just for you in test mode. So you ask the room to try it — and the silence that
follows is not indifference, it is something more specific that nobody says out loud.

**The struggle.** A founder with a transcription and translation tool posted a friendly, modest
request for feedback. The product charges as you go through a payment provider, and the sequence was
that a user picks a plan, pays through a link, and then receives a verification code that activates
their account. What they asked for was volunteers to test that the payment process worked and to
confirm it behaved correctly for international users. They were candid about the product's limits,
said they were not claiming to match established competitors, and noted from their own testing that
recording audio in the app worked better than uploading a file, particularly for larger files.

**What worked.** One reply did the founder more good than a hundred polite ones. The commenter said
plainly that they were not going to hand over card details to verify a code flow for a stranger, but
that they had looked around the site anyway — that the gap between recording and upload usually
points at how uploaded files are being split for processing — and, crucially, that more people would
help if there were a mode where the flow could be verified without anyone actually paying. That is
the whole lesson delivered in three sentences, and it is worth being precise about the mistake,
because it is not carelessness. The founder inverted the order of trust. The request began at the
highest-commitment action a stranger can take, entering payment details with an unknown vendor, and
offered in return the opportunity to do unpaid quality assurance. Every step of that ladder that
normally comes first — using the thing once, seeing it work, deciding it is worth money — was
skipped. The activation sequence compounds it: paying and then waiting for a code to unlock the
account inserts a gate at the exact moment the customer has committed, which is the worst possible
place to put a pause. And the volunteered defect cuts both ways. Naming the weaker upload path was
honest, and honesty is the right instinct, but it was placed inside the same request that asked for
money, so it functions as a reason to hesitate rather than as evidence of a trustworthy operator. A
known defect belongs in the changelog and the roadmap, where it reads as competence, not in the
sentence immediately before the payment link.

**The lesson.** Ask people for the smallest thing that produces the information you need, and never
ask a stranger to start at the most expensive rung of the ladder. If you need to prove that payments
work internationally, build the path that lets someone prove it without spending — a sandbox, a
free trial with no card, a single test transaction you refund — because the cost of that path is one
afternoon and the cost of not having it is a launch post that everyone reads and nobody acts on. And
put your remaining rough edges where they signal that you are on top of your product, rather than
directly in front of the thing you want people to do.
*(via a founder thread on r/micro_saas)*

### 125. Your page is not the unit that gets read

**The pain.** You wrote the pages. They are accurate, they are well designed, and they say what the
product does. And when a buyer asks an assistant about your category, your competitor gets named and
you do not, and nothing in your analytics explains why.

**The struggle.** A team posted the results of running an automated audit across fifty software
company websites, and the findings describe a failure mode almost nobody is watching for. Roughly a
third of the sites were effectively never read at all, because their pages are empty until scripts
run in the browser and most assistant crawlers do not run scripts — so what arrives is a blank
shell. Beyond that, the problems were structural rather than technical. More than half of all
sections were under forty words, with a median around thirty-five, against a retrieval process that
hands the model one passage at a time in the range of a hundred to three hundred words. Only around
a quarter of sections contained a number, a quotation or a link. Three in five buried the answer
below the first two hundred words. And more than nine in ten kept content on subdomains that the
main site's crawler instructions never covered.

**What worked.** The reframing that makes all of this actionable is a single shift in the unit of
composition. The thing that gets retrieved and quoted is not your page, it is one passage inside it,
lifted out of context and asked to stand alone. That changes what good writing means in a way that
runs against a decade of habit. A section too short to contain a complete thought will be handed to
a model with nothing to say; an answer placed after a warm-up paragraph will be missing from the
chunk that gets taken; and the material that survives extraction is specific — figures, named
things, quotations, links — while the adjectives that make marketing copy feel finished are exactly
what gets dropped. The audit cites published research finding that adding statistics, quotations and
citations were the strongest of nine tested content changes, which is consistent with what anyone
who has watched an assistant assemble an answer would guess. The practical checklist is short and
mostly unglamorous: serve real content in the initial response rather than after scripts run, answer
the question in the first paragraph of the section that promises it, make each section long enough
to be independently useful, put a concrete number or source in it, and check that every subdomain
carrying documentation or a blog has its own crawler instructions rather than assuming the main
site's apply. It is also worth naming what this post is, because it is the strategy demonstrating
itself. A study of fifty sites, dense with percentages, published by the people selling the audit
tool, ending with a link to it — this is precisely the number-carrying, quotable artefact the
findings say gets cited, and it was produced in order to be. Treat the specific figures as a
vendor's account of their own market, and treat the method as the transferable part.

**The lesson.** Write for the passage, not the page. Every section should answer one question,
early, in enough words to stand on its own, with at least one specific thing in it that a machine
could carry away. Check what a crawler actually receives before you invest in what a browser
displays, and check it on every subdomain, not just the one you think of as the website. And notice
the second lesson sitting inside the first: the most effective marketing asset in that thread was
the study itself. Being the source of a number is how you get quoted, by people and by machines
alike.
*(via a founder thread on r/micro_saas)*

### 126. Fifty thousand of something

**The pain.** You have been publishing every day for two months with no advertising budget, and
finally there is a number to show for it — a big, round, gratifying one. You post it. Other founders
congratulate you. And nowhere in the celebration is any indication of whether it produced a single
customer.

**The struggle.** A founder posted, with genuine and understandable delight, that their landing page
had reached fifty thousand impressions in two months. The body of the post was two words: without
advertising. The thread that followed is the interesting part. Another founder replied with their
own comparable figure from a fresh domain, in the same congratulatory register. Someone asked what
had been done for search, and the answer was three blog posts a day — a real and impressive input,
sustained over two months. Someone else asked whether publishing that volume is harmful, and got a
reasonable answer about quality mattering more than count, with a link to the search engine's own
guidance. Someone asked where the leads came from and was told organic traffic through blog posts.
At no point did anybody, including the founder, mention clicks, signups, trials or revenue.

**What worked.** There is nothing wrong with celebrating an early number, and there is a lot right
with three posts a day for two months, which is more consistency than most founders manage. But the
number chosen for celebration is the one the reporting tool hands you first, and it is the one
furthest from money. Impressions measure how often a link was displayed. They are compatible with
zero clicks and are frequently accompanied by very few, because the same volume strategy that
produces a large impression count also produces pages that rank in the positions where nobody looks.
The chain that matters is impressions, then clicks, then people who arrive and do something, then
people who pay — and each of those is available in the same dashboard, for free, and none of them
was mentioned. The founder is one screen away from knowing which of roughly a hundred and eighty
published posts brought anyone at all, which would convert two months of undirected effort into a
direction. What makes this hard to see from the inside is the reception. A two-word post reporting
an impression count drew far more approval in that community than the detailed, numbers-heavy posts
around it. That is a real signal about the audience, and a founder can easily mistake the applause of
other founders for evidence that the strategy is working. It is evidence that the metric is
relatable, which is not the same thing.

**The lesson.** Celebrate the input, not the vanity output — three posts a day sustained for two
months is the achievement, and it is the thing that compounds. But choose one number downstream of
attention as the one you actually report to yourself: clicks at minimum, signups if you have them.
Sort your pages by that number rather than by impressions, and you will discover within an hour
which handful of the hundreds are doing the work, at which point the next two months can be spent on
those instead of on all of them. And be careful whose applause you are measuring against. Other
founders will cheer for the metric they also track; customers only ever respond to the one you have
not looked at yet.
*(via a founder thread on r/micro_saas)*

### 127. Closest to the complaint, farthest from the buyer

**The pain.** You built the thing because you heard the problem out loud, every day, from someone
standing next to you. It is on the store now. A few people have signed up and every one of them is
still on the free trial. So you make videos, post them everywhere, and feel completely lost.

**The struggle.** An eighteen-year-old working in landscaping wrote this up plainly. Their boss kept
complaining about the established management tools in that trade, so they built their own, shipped
it to the app store, and got a handful of users — all of them still in trial. The marketing effort
was short-form video posted to three social platforms, described honestly as minor success. The
replies split into two kinds. One was a genuinely useful, concrete account of app store optimisation
from someone running their own apps: find keywords with low competition and real volume and use them
in the title and description, work hard for reviews because the store rewards them, never buy
reviews or trade them because the platform detects it and penalises the app, register a domain and
build a simple site so search can send traffic too, and engage a user with the product before
showing them a paywall. The other kind was less useful and more revealing: another founder saying
they were also trying to figure it out, and someone advising to post daily and improve.

**What worked.** The store advice is correct and worth doing, but it is second, and treating it as
first is what has this founder feeling lost. Look at what they already have that almost nobody
building for a trade possesses. They work in the industry. They have a named prospect who articulated
the problem unprompted and repeatedly — their own boss — and behind that person is a crew, a
network of other operators, suppliers, and every yard within driving distance. That is a warm,
concentrated, physically reachable market that understands the problem without being educated into
it. Instead, the effort is going into short-form video, which broadcasts to a general audience in
the hope of finding a landscaping business owner by accident. The single highest-value action
available is not a marketing action at all: sit down with the boss whose complaints created the
product, watch them use it for a week, and either convert them into the first paying customer or
find out precisely why they will not. Everything follows from that. If the person who described the
problem out loud will not pay, no amount of store optimisation fixes it and you have learned
something enormous for the price of one conversation. If they will, you have a named local reference
in an industry that runs on word of mouth, which is worth more than every keyword in the store
listing. The trial detail points the same way. Users sitting in a trial indefinitely is not
patience, it is an absent decision — nobody has asked them to make one, and nobody has watched what
they did or failed to do in the first session.

**The lesson.** When you build from inside an industry, your advantage is access, and broadcasting
throws it away. Start with the person whose complaint became the product and work outward through
the people they know, in the places that trade already gathers, before you optimise a listing or
post another video. Get the first paying customer face to face, where you can watch the software
being used and hear the objection in the room. Store optimisation compounds and is worth building in
parallel — but it is how strangers find you later, not how the first five customers happen.
*(via a founder thread on r/micro_saas)*

## Entries — 2026-08-11

### 128. The same loss, three times

**The pain.** You go back through the deals you lost and every one of them has a story. This one
wanted to build it internally. This one panicked. This one handed you to a colleague who was never
going to say yes. Individually each is bad luck. You add them up, get a number, and take the number
to a forum to ask whether it is normal.

**The struggle.** A founder running an outsourced sales agency posted a careful accounting of a
single cohort. Eight months in, twenty to thirty thousand a month in recurring revenue, everything
sourced by cold email with no calling, selling into manufacturing at around six and a half thousand
a month. In July the campaign produced two to six meetings a day, which was enough volume that
operations stopped keeping up — follow-up slipped, the pipeline records slipped — so they stopped
the campaign for most of a month to fix that side properly. Later they went back through the
twenty-eight meetings that batch had produced. One closed. Two more looked genuinely live. Call it
two or three out of twenty-eight. The feedback on the pitch itself had been consistently good;
nobody said the offer was confusing. The question they brought to the thread was whether that ratio
was bad.

**What worked.** Most of the replies answered the question asked and said the ratio was fine, that
twenty-eight is too small a sample to optimise against, and that the whole thing is meaningless
without knowing the product. Fair enough. But two replies ignored the ratio and looked at the
column beside it, which is where the actual information was sitting. The first pointed out that the
losses were not scattered: "they're the same loss three times." Three of the named deaths were some
version of deciding to build it in house. That is not four unrelated misfortunes, it is one
objection appearing repeatedly, and an objection that consistent was almost certainly present at the
first meeting — it simply does not get said out loud until somebody has to sign. The second reply
was even more deflating and more useful: the campaign was paused for the better part of a month in
the middle of this batch. A deal at that price does not sit patiently for four weeks. Some unknown
share of those twenty-eight did not decide against the seller at all; they went quiet because
nobody was chasing them, and that is an operations failure being read as a conversion failure. From
there the fixes are specific rather than philosophical. Ask on the second meeting who else can veto
this, and get them into the room before a proposal exists rather than discovering them afterwards.
Quantify what staying put costs, because "build it in house" is what a buyer says when the cost of
doing nothing has never been made concrete. And split the funnel into stages — meeting to
qualified, qualified to proposal, proposal to closed — so that a single blended number stops hiding
which stage is actually leaking.

**The lesson.** A close rate is one number and it tells you almost nothing. The reasons attached to
your losses are a list, and lists have patterns. Before you conclude you need more volume, sort the
lost deals by stated reason and see whether the same sentence appears three times — if it does, you
do not have a conversion problem, you have one unhandled objection that you are paying to discover
at the end of every cycle instead of the beginning. And be honest about which losses were decisions
and which were just silence you caused.
*(via a founder thread on r/Entrepreneur)*

### 129. Attention is free, which is exactly what makes it useless

**The pain.** The market looks busy. There are company websites, industry reports, search results,
people posting about the problem constantly. You go deeper expecting the picture to sharpen and it
does the opposite — the loudest companies do not seem to be the ones doing the most, and a couple
of quiet ones you almost missed seem to be where things are actually happening.

**The struggle.** A founder researching a new market described exactly that disorientation and
asked which signals people trust before committing time or money. The thread is unusually good, and
the first thing worth noting is a complication several people raised: a growing share of what looks
like market signal is content generated to look like market signal, which then gets read by research
tools that produce audience predictions from it. One commenter described the loop of machine-written
posts reinforcing machine-written posts and called it devolving to the mean. Whatever you think of
that as a trend, it has a practical consequence — the cheaper it becomes to manufacture the
appearance of a conversation, the less any volume-based signal is worth.

**What worked.** Three replies each supplied a different instrument, and together they make a
usable method. The first is the commitment test, stated bluntly: everyone in the thread, including
the person asking, is in observation mode, reading the market from outside, and no amount of
competitor ad spend or job postings tells you that someone will hand *you* money. "Interest is free
so people give it away endlessly." So put something on the line — a pre-order, a deposit, a paid
pilot, a signed letter of intent, anything that costs the other person more than a nod. Twenty
direct messages asking for a small commitment will teach you in a week what six months of desk
research will not, and if nobody will commit anything at all, that is also an answer. The second
instrument is subtler and I have not seen it written down before: look at whether pricing has
converged. Not what companies claim to charge, but what the going rate actually is where real
listings and real platforms enforce it. A market where prices cluster tightly is one where
transactions are genuinely happening and both sides have settled on what the thing is worth. Prices
scattered all over the place alongside heavy visibility usually means hype that has not yet
resolved into a market. The third is a filter you can apply in ten minutes: look at *who* is making
the noise. Buyers complaining about tools they already pay for is demand. Founders, agencies and
vendors talking to each other about the opportunity is a supply-side conversation that can run at
full volume with no buyers in it at all.

**The lesson.** Separate the market's noise from the market's behaviour, and only trust the
behaviour. Ask whether prices have settled, whether the people talking are buyers or sellers, and
whether anyone will commit something that costs them. A loud presence often means a company that
needs attention; the quiet ones frequently do not have to perform because the business is already
working. And note the practical order this implies — the commitment test is cheaper and faster than
the research you were about to do, so run it first and let it tell you whether the research is even
worth commissioning.
*(via a founder thread on r/Entrepreneur)*

### 130. One job advert with four jobs inside it

**The pain.** A client has given you a deadline with a threat attached. Eight months to fix their
sales or they leave. You start writing a job description for the person who will save the account,
and by the third bullet point you have described somebody who does not exist.

**The struggle.** A small agency posted this to a marketing community, asking whether to hire
in-house, use a white-label partner, or find a freelancer. The requirement list included writing,
design, growth strategy and account management, held by one person, aimed at fixing an e-commerce
business's sales within the window. The replies were not gentle and they were almost entirely
right. Several people pointed out that those are four separate professions and the search would be
for a unicorn; one suggested two or three people is the realistic shape. Someone did the calendar
arithmetic — hiring alone eats a month or more of the eight, before anybody learns the account.
Somebody else noticed the contradiction inside the brief itself: the client's stated problem was
burning cash, but the plan being discussed was expanding social presence and ad spend, so money
would be going out faster while the leak stayed unfound. And the single sharpest reply compared the
client's expectations with the agency's own description of itself and concluded: "you've got the
wrong type of client."

**What worked.** That last comment is the one to sit with, because it reframes a staffing question
as a positioning question, which is what it actually is. An account that requires capabilities you
do not have and have never sold is not an opportunity to grow into, it is a mismatch you agreed to
because of the invoice. The tell is in the brief. If a client is asking you to do analytics and
sales growth and you have nobody who does that, then either the work you have been delivering was
never measured against revenue, or the client has changed what they are buying without changing who
they are buying it from. One commenter said this in an uncomfortable way that is worth repeating:
being surprised by the request makes them wonder whether the rest of the deliverables rest on
judgement rather than data. There is also a concrete diagnostic buried in the thread that costs
nothing and should precede every hiring decision. Ask whether the store gets plenty of items added
to carts that never become purchases, because that specific shape has specific causes — including
fraudulent ad clicks, which is a solved problem rather than a marketing one. Find the leak first.
Whether the fix is then a part-time analyst plus a performance specialist, or a white-label partner,
or two freelancers, is a question you can only answer once you know what is broken, and the honest
answer to which of the three is best is that all of them work when correctly scoped and all of them
fail when they are being used to avoid admitting the account does not fit.

**The lesson.** When a brief requires a person who does not exist, the brief is wrong, not the
labour market. Split it into the roles it actually contains and you will usually find that one or
two of them are urgent and the rest were aspiration. Diagnose before you staff — a month spent
finding the actual failure point is cheaper than a month spent recruiting for the wrong one, and
you only have eight. And when a client asks you for work you have never sold, treat it as
information about the relationship rather than a compliment about your range.
*(via a founder thread on r/marketing)*

### 131. A list of people waiting for a thing that does not exist

**The pain.** The standard opening move is a landing page with a waitlist. You build it. Then you
realise nobody has told you how anyone is supposed to find the page — search is a long game, cold
outreach eats the hours you need for building, and the communities where your buyers actually are
will remove you for promoting.

**The struggle.** A solo founder laid out that trap precisely and asked for ideas. The product is a
competitor intelligence subscription: pick a company, and each month you get a briefing on what it
is doing, what it appears to be planning, and what its customers and investors are saying, all
assembled from publicly available material. Most of the replies confirmed the walls rather than
finding a way through — post here (you will be banned), search plus cold outreach plus your own
professional network, which is the list they had already written, with the observation that this is
why early founders work sixteen-hour days. Another founder replied to say they were stuck in the
same place and had discovered that this community, too, is crowded and restricted.

**What worked.** One reply refused the question and was worth all the others combined. Skip the
waitlist entirely and do the thing by hand. Competitor intelligence is one of the rare products you
can deliver before you have built anything: choose ten companies, write the briefing yourself, send
it to someone who competes with them, and ask whether it was worth reading. The reasoning attached
was the part that generalises. "A list of emails waiting on a future product tells you close to
nothing" — whereas one person who read your report and asked when the next one is coming has told
you the product works, the format is right, the frequency matters to them, and that they are the
buyer. A waitlist converts a hard question into an easy one and then measures the easy one. Signing
up costs nothing, so the number that comes back is a measure of curiosity and of how well the page
was written, and it can be large while the underlying demand is zero. It also postpones every
genuinely useful discovery until after you have finished building, which is the most expensive
possible moment to find out that the briefing should have been weekly, or should have covered
suppliers rather than competitors, or that people wanted the raw sources more than the synthesis.
The manual version inverts all of that: it is slow, it does not scale, and it answers the real
questions immediately. And it dissolves the distribution problem that started the thread, because
you no longer need a channel that delivers strangers to a page — you need ten specific companies
and one interested reader, which is a research task you can complete this week.

**The lesson.** Before you market a waitlist, ask whether you can simply deliver the first version
by hand to a handful of people. If the answer is yes, the waitlist is a way of avoiding the
conversation, not a route to it. Judge early demand by what people do after they have received
something, not by what they typed into a form before anything existed. One reader who asks for the
next issue is worth more than a thousand addresses, and unlike the thousand addresses, you can get
that reader on Tuesday.
*(via a founder thread on r/Entrepreneur)*

### 132. The pain was already worded for you

**The pain.** You are inside an industry, watching the same money leak out of it every month in a
way nobody quite names, because it never arrives as a complaint. People simply stop showing up.

**The struggle.** A founder who owns a martial arts school described this with unusual precision.
Students do not cancel; they drift. A child misses one class, then a second, then quietly does not
rebook for the next term, and by the time the empty space on the mat registers, they left mentally
weeks ago. The numbers they attached make the case better than any argument: roughly three quarters
of beginners never reach the next belt, most departures happen inside the first ninety days, and a
school with a hundred students paying a hundred and fifty a month that loses five of them a month is
losing around nine thousand a year — which they point out is not a rounding error but a second
instructor's salary walking out of the door in silence. So they built a tool that flags which
students are slipping before they quit. The post was mostly about what building inside your own
industry changed, and it was honest about the downside: a small total market, incumbent billing
tools every school already pays for, and open uncertainty about whether doing the one thing those
tools do not do is a wedge or a ceiling.

**What worked.** Three observations from that post are worth taking whole. First, the pain arrived
pre-worded — school owners already say students "just stopped showing up" and use the word drifting
unprompted, so there was no pitch to invent, only language to repeat back. That is a marketing
advantage most founders spend a year and a lot of copywriting trying to manufacture. Second, the
person who pays is not the person who decides: the owner buys, but whether a child stays is settled
by a parent, and building for the buyer alone would have produced the wrong feature set entirely.
Third, and most useful, the constraint is the moat. You cannot ask someone teaching on the mat six
days a week to open a dashboard and read reports; anything that takes more than a couple of seconds
to record simply will not be recorded. That single limit shapes the product more than any competitor
does — and it is exactly the sort of limit a horizontal tool built by people who have never stood on
a mat will not respect. Then a commenter supplied the test that answers the founder's own open
question, and it is a good one for anyone in a narrow vertical. The small market is rarely what
kills these companies. The ceiling appears when the thing the incumbents do not do turns out to be a
feature request rather than a different shape of product. So ask directly: could the incumbent ship
your capability as one more tab, without changing how their product fundamentally works? If yes,
the market size was never the risk. If no — if honouring the two-second constraint means reports
cannot exist anywhere in your data model — then you are not a missing feature, you are a different
thing, and that is defensible.

**The lesson.** Building where you already work hands you three assets at once: the customer's own
vocabulary, knowledge of who actually influences the decision, and the operational constraints that
outsiders design straight past. Use all three deliberately rather than treating them as background.
And when you go narrow, stop worrying about the size of the market and start pressure-testing the
shape of the product — the question that decides your future is not how many schools exist, it is
whether your advantage survives being copied as a tab.
*(via a founder thread on r/startups)*

### 133. The first three were free and two of them paid twice

**The pain.** You have read the standard list. Publish constantly, go viral, automate, send
hundreds of emails, build a waiting list. You do it for months, it keeps you extremely busy, and
you have nothing you can point at.

**The struggle.** A founder with experience across a business-to-business software company, a
professional services business, and now advising other founders wrote up why they think that list
sends people the wrong way — and the diagnosis is sharper than the usual "do things that don't
scale." Early on, three things are unvalidated simultaneously: who your customer is, what you are
offering them, and how you describe it. Content and cold email are one-way channels. When they do
not land, the failure gives you no way to tell which of those three was wrong, so you tune all of
them at once, forever, on no information. That is the real reason those tactics feel like a void —
not that they never work, but that they are the wrong instrument while your basic assumptions are
still unproven.

**What worked.** Their sequence had three steps, and the second one is the interesting one. First,
form an explicit hypothesis about the problem and about exactly who has it, then talk to as many
people who fit that description as possible — and this was done without cold outreach at all. They
went to people already in their network who matched the profile, and for everyone else they used one
question, asked repeatedly: do you know anyone who fits this description, and would you introduce
me? That produced the first ten conversations quickly. Second, the offer. When launching the
consulting business they went back to the people they had spoken with, named a real price of a
thousand euros, and said the first three could have it free in exchange for a case study and honest
feedback. Five replied, three were chosen, a fourth paid a reduced rate, and the fifth disappeared
at the end. Two of the three free ones later sent referrals that became paying work. The framing
they use for this matters: "it's not free work, you are getting credibility and proof" — the price
is stated and held, and what is exchanged is a discount for evidence, not a cheap product. That
distinction is what stops a free tier from repricing you permanently downward. Third, once the proof
exists, the constraint changes. Early on your problem is not only that nobody has heard of you but
that nobody has any reason to believe you, and a specific account of what you did for a named
similar business collapses that scepticism faster than any amount of copy. After that the work is
genuinely simple, if not easy: keep appearing in front of more people who match the profile from
step one, carrying the proof from step two.

**The lesson.** Do not use one-way channels to test assumptions, because they cannot tell you which
assumption failed. Have conversations while your offer and your customer are still in question, and
get to those conversations through introductions rather than strangers — asking your network who
they know is faster than any list you can buy. When you need the first customers, keep your price
and trade it for proof, explicitly and in writing. Content and campaigns are not wrong; they are
just what you do after you know who is listening and why they believe you.
*(via a founder thread on r/Entrepreneur)*

### 134. You told them what it cost you to make

**The pain.** Someone larger than you wants to carry your product. This is the moment you have been
working towards. Then the numbers arrive and the deal is worth less than picking up extra shifts,
and you cannot tell whether you are being cheated or simply do not understand how this works.

**The struggle.** A founder who owns several self-service car washes and does electronics and
software work on the side built a timer for that industry. Competing units sell for between two
hundred and seventy-five and three hundred and fifty; theirs is listed at two hundred and
twenty-five and, by their account, is not comparable in quality — "It's like comparing a Nintendo to
a Nintendo 64." A manufacturer approached them wanting to private label it and hold exclusive rights
to sell through their distributor network. The founder offered a hundred and fifty per unit. The
manufacturer held firm at a hundred and twenty-five, targeting a retail price of three hundred and
thirty. Parts cost fifty-six, plus assembly and testing time. Two things about how this was
negotiated are stated plainly in the post: they told the other side what the parts cost, and they
named their own number first, immediately, because they dislike haggling and do not consider
themselves a salesperson.

**What worked.** The instinct to walk away is correct, and the reasoning behind it is worth making
explicit because it generalises far beyond hardware. At a hundred and twenty-five against
fifty-six in parts, the margin has to absorb assembly, testing, packaging, warranty, and every hour
of the founder's own labour, under exclusivity — which means simultaneously giving up the direct
channel where they currently keep the difference between fifty-six and two hundred and twenty-five.
That is not a distribution deal, it is becoming a contract manufacturer for someone else's brand at
a wage, and their own summary of it is exact: they would be better off taking more shifts. The
negotiation errors are equally instructive and both are extremely common among technical founders.
Disclosing input cost reframes the entire conversation around your costs rather than the buyer's
value, and once the other side knows the parts are fifty-six, every number you name is measured
against that instead of against the three hundred and thirty they intend to charge. Opening with
your own price, before understanding their volumes, their exclusivity requirements or their
timeline, throws away everything you might have learned by asking first. And the deeper point sits
underneath both: pricing a channel is not the same problem as pricing a product. What the
manufacturer is really buying is access to distributors, and the right question is what that access
is worth in units per year and over how long — because exclusivity without a volume commitment is a
one-sided option, and any version of this deal worth signing has minimum quantities and a term in
it. The founder's stated reluctance to continue even at their own asking price is also sound
judgement rather than sulking. A partner who anchors that hard at the opening is telling you what
every later conversation about warranty claims and revisions will feel like.

**The lesson.** Selling through someone else's channel is a different product with different
economics, and you have to price the access rather than the object. Never volunteer your input
costs, never name your number until you know their volume and terms, and never grant exclusivity
without a minimum commitment attached. The most valuable thing in this whole episode is the number
the founder now knows: their partner intends to retail it at three hundred and thirty. That is a
free, verified read on what the market will bear, and it says the direct price of two hundred and
twenty-five is probably too low.
*(via a founder thread on r/Entrepreneur)*

### 135. Being good at a channel is not the same as the channel working

**The pain.** You have customers. You can explain exactly how each one arrived. And when somebody
asks whether you have found a repeatable way into the market, you cannot honestly say yes, because
what you have is two stories rather than a process.

**The struggle.** A founder posted this cleanly. Two customers: one from an industry event, one
referred by a friend. If they keep the first, that customer has already offered introductions to
similar businesses. Events are working in the sense that they produce customers, but the arithmetic
does not — around eight thousand spent on one event to acquire two customers, which costs more than
those customers currently bring in. Their question was what an early investor would accept as
evidence of a repeatable route to market. The thread was mostly unkind, largely because of the
opening line about funding stages, which is a shame, because the question underneath is a good one
and one reply answered it properly.

**What worked.** That reply reframed the whole thing: most founders answer this with a number, and
it is the wrong number. Landing forty customers through cold email is not repeatability — "it's you
being good at cold email for 40 customers." The distinction is between an outcome you produced and a
mechanism that will produce more without you. That is the useful test, and it makes the founder's
own situation legible. Two customers from two different routes is not one channel with a sample of
two; it is two separate mechanisms with a sample of one each, which is why nothing about it feels
repeatable — it is not. The event channel has a real number attached and the number is bad, but it
is bad in a way that is diagnosable rather than fatal: eight thousand for two customers only fails
because of what those customers are currently worth, so the questions are how long they stay, what
they expand to, and whether the same event with a specific pre-booked meeting list produces six
instead of two. The referral route is the more interesting one and it is being undervalued in the
post. A customer who has offered to introduce you to similar businesses is not a nice gesture, it is
the beginning of a mechanism, and it becomes evidence the moment you can describe it as a process
somebody else could run — which introductions were asked for, at what point in the relationship, how
many converted. That is what turns "our customer likes us" into a channel. And there is an ordering
mistake worth naming: the founder is trying to prove a channel to investors before it has been made
to work for the business, which is backwards. The economics do not have to be good yet, but you must
be able to say what would make them good.

**The lesson.** A repeatable channel is a described mechanism with a sample large enough to have a
rate, not a count of customers who arrived. Write yours down as steps somebody else could follow,
attach a conversion rate and a cost to each step, and you will immediately see whether you have one
channel, several accidents, or a skill you happen to possess. Until then you have not found
repeatability, and the honest version of that — here is the mechanism, here is what it costs, here
is the part I have not yet proven — is far more convincing than a number presented as though it were
a process.
*(via a founder thread on r/startups)*

### 136. Eight channels is a quarter with nothing learned

**The pain.** You have written the list. Professional network outreach, contact-finding tools,
sending platforms, paid social, search, downloadable guides, cold email. It is comprehensive, it is
accurate, and it has left you completely unable to start.

**The struggle.** A founder new to business-to-business services posted exactly that list — eight or
nine options, each with named tools — and said they had some traction but no idea how to generate
sales consistently. They had already read that focusing on two or three channels beats trying
everything, and were asking which two or three. It is a reasonable question and the thread gave it
an unreasonably good set of answers, because almost nobody answered it directly.

**What worked.** The first reply was a question back, and it is the one that should always be asked
first: how did the customers you already have actually find you? A business with traction already
has a channel; it is simply not being counted as one because it happened without a tool attached.
The second reply made that concrete from experience — a lot of cold email that went nowhere, while
every piece of services work actually won came from somebody who had already seen something the
founder had finished. Which points at the cheapest available action: go back to your existing
customers and ask who else has the same problem. The third reply supplied a method with numbers. Do
not build a list of thousands; pick twenty companies you can explain in one sentence why they would
want this. Find the specific human who owns that problem rather than a general company address.
Verify each contact is real and still in that role before writing anything, because in their
experience dead and wrong contacts wrecked early campaigns far more than bad copy did. Then send
twenty messages whose first line is about the recipient rather than the sender: "20 good ones beats
2000 blasted." You learn more from who replies than from any open rate. The fourth reply made the
structural point about the list itself — those eight items are eight different motions, and running
three at once is how a quarter disappears with nothing learned. Pick the single channel where your
buyer already answers and commit to it for six to eight weeks before judging it. And it added the
operational detail that decides whether cold email works at all, which no tool comparison will tell
you: send from a separate domain, never your main one, because a burned primary domain will put your
invoices in the spam folder along with everything else. Two or three inboxes on it, warmed for about
a month before real volume, addresses verified the same week you send. Skip that and the choice of
sending platform is irrelevant, because you will be in spam regardless.

**The lesson.** A long list of channels is not a strategy problem, it is a symptom of not having
looked at what already worked. Start with how your existing customers found you and do more of
that on purpose. Pick one channel, run it for six to eight weeks at a scale small enough that every
message can be good, and judge it on replies from named people rather than on aggregate rates. And
whatever you choose, get the boring infrastructure right first — the founders who conclude that
cold email is dead are frequently the ones who never learned that it lives or dies on domain
hygiene.
*(via a founder thread on r/startups)*

### 137. The decisions that were free to change

**The pain.** You have spent three weeks on something that felt existential — the name, the logo,
the pricing tiers — and you cannot honestly say the business is any further forward than when you
started.

**The struggle.** Someone asked a simple question in a founder community: what is the one decision
you overthought that turned out not to matter, and what did you barely consider that turned out to
be important? The answers are more useful than most structured advice, because they are all
retrospective and nobody was selling anything. The most upvoted was branding — name, logo, identity
— which matters, but matters very little in the first months, and which the commenter eventually
redid entirely two years in, once they finally understood what the company actually was. A useful
disagreement followed: logo and visual identity are cheap to change later, but a name is sticky
because it is what any awareness you have accumulated is attached to, so it deserves some thought
even if the rest does not. Another founder said the decision they overthought was starting at all —
continually finding one more thing to resolve first. A third named the pricing page: weeks spent on
tiers, and the first ten customers all landed on "a number I said out loud on a call" anyway. A
fourth described agonising over scope on a data product, worried that launching with ten fields
instead of thirty would look unfinished, shipping the thin version out of frustration rather than
conviction, and discovering that the ten were the ones people used while every field they had
stressed about drew no engagement for months.

**What worked.** There is a single test running underneath all four answers, and it is worth
extracting because it turns this into something you can use on Monday rather than a set of
anecdotes. Ask what it will cost to change this decision after you have customers. Logos, tier
structures and feature scope are all cheap to revise later — and, more importantly, all of them get
*better* information from customers than from you, so deliberating in advance is not just slow, it
is answering with the worst available data. The genuinely expensive-to-reverse decisions are a
small set: your name once awareness accrues to it, your legal and equity structure, and any
commitment that binds you contractually. That is roughly where the care belongs. The pricing example
deserves particular attention from anyone currently rebuilding a pricing page, because it points at
something structural: price is discovered in conversation with buyers, so the weeks spent designing
tiers in advance were spent guessing at an answer that the first ten sales conversations were going
to supply for free. The scope story is the same shape — the founder was guessing at what looked
complete, and five conversations would have replaced the guess. Both are avoidance dressed as
diligence, and the tell is consistent: the deliberation is about how the product will be perceived,
and it is being conducted entirely without the people who will perceive it.

**The lesson.** Sort your open decisions by what reversing them will cost once you have customers,
and spend your deliberation only on the expensive end. For everything else, ship a version and let
buyers correct it — they will do it faster and more accurately than you will. And when you notice
yourself in week three of a decision, check whether the question you are struggling with is one that
five conversations would settle, because a decision you can only make by guessing is one you should
be making out loud with somebody who might pay you.
*(via a founder thread on r/startups)*

## Entries — 2026-08-13

### 138. Three years of people liking it

**The pain.** Everybody you show it to says something warm. Nobody has ever said no. And after three
years there is not a single signature, the bank balance is falling, and the thing you cannot work
out is not what you did wrong but what you are supposed to do at all.

**The struggle.** A bootstrapped founder posted this twice on the same day, which tells you
something about the state they were in. They have a business intelligence product. Three years, no
contract. They have had conversations at worker level, at chief-information-security-officer level,
and with peers in the field. The response is uniform: people like it, nobody has negative feedback,
and every conversation produces a few more feature requests that must be satisfied before purchase
— and then, once satisfied, the target moves again. Their own framing is the honest one: this is
less "what am I doing wrong" and more "I clearly don't know how to do this part." Elsewhere in the
thread they add the detail that makes it worse. They lost roughly six months of development to
feedback from one company, whose compliance team appeared at the meeting; the same shape repeated at
another company, where a network architecture team was produced instead. Both times, they now
suspect, executives were being helpful by asking for a solution to their own use case rather than
buying the one in front of them.

**What worked.** The thread supplied one question and one diagnosis, and between them they cover the
whole problem. The question, asked kindly, was how many times in three years the founder had put a
number in front of someone and asked them to sign. Nobody had made them say no properly, so what had
accumulated was not a body of evidence but a supply of encouragement — "collecting encouragement
instead of information." That is the mechanism behind the whole three years. A conversation where
nothing is asked for cannot fail, which is exactly why it teaches you nothing, and a founder
frightened of the answer can hold hundreds of them and call it market research. The diagnosis
underneath was that the people in these rooms are users rather than buyers. A user enjoys a demo. A
buyer has a budget line and a problem someone above them is asking about this quarter. Which
reframes the feature requests entirely: they are almost never the blocker, and the proof is already
in the founder's own account — the requests were met and the target moved, because "not yet" is
politer than "no." Several commenters converged on the same missing ingredient from different
directions. One put it as consequence: for a deal to exist, someone in that conversation has to be
worse off if nothing changes, and nobody currently is. Another put it as organisational reality —
business intelligence touches everything, so it requires a change to how a company works, which
requires a champion who controls a budget rather than an admirer who controls nothing. The founder
supplied the last piece themselves without quite registering it: large companies told them they want
mature software, not something that may need an iteration, and the value they are selling is risk
management, which many firms ignore entirely and the rest treat as a regulatory checkbox. That is
not a sales problem. That is a product being sold into a category where the buyer feels no pain and
the personal cost of signing for a new vendor is real. Two concrete moves were offered. Run a small
paid pilot, because a small amount of money converts polite interest into an actual decision and
does it in weeks rather than quarters. And ask every friendly executive the only two questions that
matter: who else has to say yes, and what breaks for them personally if they do nothing this
quarter. If the second has no answer, there is no deal there, however much they like you.

**The lesson.** Enthusiasm is not evidence, and a conversation that cannot end in rejection is not
research. Ask for the order, name a price, and let people decline — the no arrives with a reason
attached, which is the thing you are actually short of. Then check who is in the room: if nobody
present owns a budget and nobody is personally worse off for doing nothing, you are being managed
politely rather than sold to, and no number of delivered features will change that. When the target
moves right after you hit it, stop building and start looking for the person who is bleeding.
*(via a founder thread on r/startups)*

### 139. Everything you fixed was upstream of the problem

**The pain.** The campaign worked. The leads tripled. And somehow the business feels worse than it
did before — you are answering the same basic questions all day, things are slipping, and the growth
you spent months chasing has made your week unmanageable.

**The struggle.** A founder who works with small businesses laid out the pattern they kept running
into. Their instinct, for a long time, was that the obvious problem was always customer acquisition:
more leads, more calls, more enquiries. What they observed instead was that adding customers rarely
creates problems — it exposes ones that were already there and were being hidden by low volume. If
follow-ups are inconsistent, more leads simply means more things to chase badly. If onboarding is
undefined, more customers means the same questions arriving more often. If nobody owns the next
step, every step routes to the owner. They gave one concrete case: a local service business went
from roughly twenty leads a month to more than sixty after changes to their ads and their Google
listing. Same team, same owner. Follow-ups started slipping, onboarding calls were delayed, and the
owner spent the day answering emails asking what happens next. The marketing had worked exactly as
intended, and the business was in a worse position for it.

**What worked.** The reframing the founder landed on is a single substituted question — not "how do
we get more business" but whether the current process can absorb more business without everything
returning to the owner. The thread then supplied the specifics that turn that into work. The most
useful came from someone who had chased new logos while quietly losing existing ones, and who
started calling cancelled customers personally to ask one question: what did they expect that did
not happen? Two of the first three said onboarding had confused them and they never got a first
win, so they drifted off. Fixing that one flow reduced churn noticeably, and by their account cost
less than any acquisition push. Their conclusion is the sharpest thing in the thread: the first
thirty days after somebody says yes decide everything. A second commenter explained why follow-up
in particular is the piece that fails, and the reasoning generalises to any process you own.
Delivery has a date attached and a customer waiting, so it is defended; follow-up has no deadline
and no owner unless you assign one, so it never fails loudly — it just slows down until it is not
happening, and no one ever decided that. A third gave the fix, which is unglamorous and works: write
out what should happen after a yes, put a named person on each step, and add a default action that
fires if nothing has happened within a day. Two more comments are worth carrying. One noted that the
same amplification applies to money — more customers can make revenue look healthier while
multiplying bad unit economics underneath. And one dissented usefully: "fix your process before you
grow" is also how businesses spend six months building systems for volume that never arrives. Both
are right, and the resolution is sequencing rather than choosing. You do not build for imagined
scale; you fix the specific thing that broke at the volume you actually reached.

**The lesson.** Marketing amplifies whatever your business already does, including the parts that
are broken, so a channel that works will find your weakest process faster than any audit. Before
spending more on the top of the funnel, look at what happens in the thirty days after someone says
yes, and check each step for a named owner and a deadline. And when customers leave, call them and
ask what they expected that did not happen — it is the cheapest research available, and the answers
usually describe a fixable moment in the first week rather than a missing feature.
*(via a founder thread on r/Entrepreneur)*

### 140. Twenty to forty-four, and no idea which thing did it

**The pain.** The numbers are finally moving, which is a relief after months of nothing. Then
someone asks the obvious question — which channel is producing this? — and you realise you cannot
answer, so you cannot do more of whatever is working.

**The struggle.** A solo developer shared a genuinely modest, genuinely useful update. They built a
productivity app in February with journaling, habit tracking, routines and to-dos. Marketing on
Reddit and X did not work. Blogging did not work either. Life intervened and the project sat idle.
Recently they picked it back up and went at distribution from several directions at once, and went
from twenty users the previous month to forty-four within about three weeks. Their own assessment is
appropriately unglamorous — the number is not impressive, but it is finally moving.

**What worked.** Four things ran in parallel, and the specifics matter more than the total. The
first was the app store listing, which is the piece most often left alone because it does not feel
like marketing. The title had been nothing but the app's name. They researched what better-performing
apps in the category do, and found most of them append a plain description to the title — the
category words a person would actually type. They rewrote the title that way, rewrote the
description around researched keywords for the niche, and replaced the listing images. One commenter
named exactly why this is the highest-leverage item on the list: "nobody searches for just an app
name unless they already know it." A store listing keyed to your brand name is only discoverable by
people you already reached through some other channel, which means every other marketing effort was
being taxed by it. The second was TikTok — about twenty short videos, no viral hit, the best around
seven hundred views, and a trickle of people arriving from it. Asked for detail, they described the
format: two to three videos a day, roughly twenty seconds, opening with a short reaction clip framed
as a moment of discovery, then a screen demo. Instagram, run alongside, produced nothing. The third
was Threads, which they found more receptive than X specifically because it is less saturated and
people there will still follow a link. The fourth was the blog, restarted and slowly picking up. And
then the honest gap, surfaced by a commenter asking how they knew which channel was responsible:
they do not. There is no attribution beyond what the Play Console and Search Console infer, and they
said plainly that they are assuming. Their reason is not laziness and is worth respecting — all
available effort went into standing the channels up, and only now that they are running is there
room to think about measurement. That is a real trade-off rather than a mistake, but it has a cost
that arrives on a schedule: with four channels live and one aggregate number, the next decision
about where to spend time has to be made blind. Note also what the listing rewrite implies about
the earlier failures. Reddit, X and blogging were tried and abandoned as ineffective back when the
store page they pointed at was not findable and did not explain itself. Some of those channels may
have been fine.

**The lesson.** Fix the page that converts before you spend months driving people to it, because a
store listing or a landing page keyed to your own brand name quietly taxes every other channel you
run. When you cannot afford full attribution, you can still afford sequencing — stagger your
channels, or at minimum write down what you changed and when, so the graph has something to be
compared against. And treat a doubling from twenty to forty-four as what it is: not a rounding error
and not a breakthrough, but the first evidence that something in the stack is load-bearing, which is
worth identifying before you add a fifth thing.
*(via a founder thread on r/micro_saas)*

### 141. It was not an ad, so people watched it

**The pain.** You have no audience and no budget for ads, so you do the obvious thing and make
videos showing your product. You post them. They are competent, they are clear, and nobody watches
them, because a demo is an advertisement and people are on that app specifically to avoid
advertisements.

**The struggle.** A founder described exactly this arc. They wanted attention for their app, had no
following, and did not want to buy it. So they started posting short videos, and at first these were
straightforwardly what you would expect — normal videos showing the app. Their summary of the result
is two words long and familiar to anyone who has tried it: nobody cared. The failure is not a
production-quality failure, which is the trap. Making the demo prettier would not have fixed it,
because the problem was that the video announced itself as marketing in the first second and the
viewer's thumb was already moving.

**What worked.** The change was structural rather than cosmetic. They collected a large number of
short reaction clips — bought footage, and they say so explicitly, noting the person in the videos
is not them — and assembled videos that open with a reaction interesting enough to interrupt a
scroll, then bring the app in afterwards. The product is still there, but it arrives as part of
something a person was already watching rather than as the reason the video exists. Views moved from
a few hundred to videos hitting ten thousand, fifty thousand, and past a hundred thousand. The
detail that keeps this from being a vanity story is that the traffic converted: people arriving from
those videos signed up and used the app. And the second structural decision is the one most founders
get wrong. Rather than trying to produce one excellent video, they made many variations of the
format that worked — different reactions, different hooks, different features shown, different
edits. Plenty failed. The point is that the unit of work became the variation rather than the
artefact, which is what lets a channel like this compound: you are not trying to guess which video
will land, you are running enough attempts that the platform tells you. Their own summary of the
lesson is the clearest line in the post: "you don't necessarily need to make an ad to advertise your
app." Two cautions belong alongside this, because the post is honest enough to invite them. Bought
reaction footage of a person who is not you is a real disclosure question, and the founder handled it
by saying so plainly in the post; carrying the same disclosure onto the content itself is the
version that survives scrutiny. And a format that depends on a hook someone else performs is
borrowed rather than owned — it works until the format saturates, which is why the variation habit
matters more than the specific template. It is also worth putting this next to the previous story,
where another founder reported the same tactic at a much smaller scale, roughly seven hundred views
at best. Same channel, same format family, two orders of magnitude apart in outcome. The difference
is not luck alone; it is volume of attempts and the quality of the first two seconds.

**The lesson.** On a feed, you are not competing with other advertisements, you are competing with
entertainment, and a product demo loses that competition by default. Lead with something worth
watching and let the product arrive inside it. Then stop polishing single pieces: find the format
that works and produce variations of it, because the channel rewards attempts rather than
craftsmanship. And if the thing carrying your hook is not yours — bought footage, a borrowed
format, someone else's face — say so, and start building the version that is.
*(via a founder thread on r/micro_saas)*

### 142. The rehearsal was worse than the conversation

**The pain.** The product is built. The next step is to be visible — to post, to pitch, to put your
name against it in public — and you have been finding other work to do for weeks, because the
building was hard in a way you knew how to be good at and this is hard in a way that feels like
exposure.

**The struggle.** A founder asked the question directly: how do people get over the fear of
judgement that comes with putting yourself and your startup in public view, given that so many
builders reach the selling stage and stall there because it is a completely different kind of
challenge. It is a soft question that usually attracts soft answers, and the thread mostly avoided
them. Another commenter described being in the middle of exactly this — far more time spent building
than being seen, and a dawning recognition that the thing has no chance unless they get comfortable
talking to people.

**What worked.** Three answers in the thread do real work, and they operate at different levels.
The first is empirical and slightly deflating. Someone described staring at a post button for three
hours, convinced their landing page would be torn apart, publishing it, and then getting nothing at
all for two days. The fear assumes an audience that does not exist yet. Early on you are not being
judged harshly; you are not being noticed, and that is a more useful thing to know because it
reframes the first hundred posts as practice rather than as a verdict. A commenter who had gone
through it with LinkedIn arrived at the same place from the other direction: the fear of the idea is
considerably worse than the act, and the discovery on the far side is that nobody cares much either
way. The second answer is a method rather than a sentiment, and it is the most portable thing in the
thread. Notice that the fear mostly appears when you are alone with your own head, not while you are
actually talking to someone — the rehearsal is harsher than any real conversation ends up being. So
adopt a rule: you are not allowed to worry about a pitch until you have said it out loud to at least
one real person. That cuts the loop, because anxiety runs on imagined scenarios and starves on
actual data, and the actual data is usually boring — people are busy thinking about themselves. The
third answer attacks the premise. The first months of a startup should be spent trying to kill the
business, and one of the things you should be actively attempting is "trying to prove that nobody
will buy it." Whatever you have built is not a delicate thing growing out of your ego that requires
protection; it is a proposition that probably does not work, and should be treated as unwanted and
unsellable until proven otherwise. That inverts the emotional load of every sales conversation. If
you are seeking validation, each call is a referendum on you and rejection is a wound. If you are
attempting to disprove your own idea, a no is a successful experiment and a yes is a surprising
result, and you will make the call this week rather than next month. One more comment is worth
keeping for its ordering advice: start the journey with sales and visibility, because for a founder
with a technical background the building is the comparatively easy part, and doing it first means
doing the difficult thing last and under time pressure.

**The lesson.** The fear of being judged in public is mostly a scheduling problem disguised as a
character problem, and it resolves faster through repetition than through resolve. Set the rule that
you may only worry about a pitch after saying it to a real human, and take the first ones expecting
silence rather than criticism, because silence is what you will get. Then change the job: you are
not seeking approval for your product, you are trying to establish whether anybody will pay for it,
and the fastest route to that answer is a stream of people telling you no.
*(via a founder thread on r/startups)*

### 143. The prototype was made of spreadsheets and duct tape

**The pain.** You are about to start again, and you have enough scar tissue to know that the last
build was the wrong thing, but not enough method to be sure this one is different. So you are
looking for a rule rather than a pep talk.

**The struggle.** A founder posed the question in a usefully constrained form: if you had to begin a
software business again as a solo founder with between nothing and five hundred dollars, what would
you do differently? They listed the standard candidates — validate before writing code, find
potential customers before building, launch a small version quickly, pick a narrow niche, spend more
time selling than developing — and then asked for the part that is usually missing, which is what
actually produced the first five to ten paying customers rather than general advice.

**What worked.** The best answer in the thread was specific about both halves. On validation: skip
code entirely until five people are asking to pay for a prototype made of spreadsheets and duct
tape. Their first attempt had gone the other way — three months polishing something nobody wanted,
followed by a pivot severe enough that it amounted to starting over. The threshold they set is the
important part, and it is deliberately behavioural rather than verbal. Not five people saying it is
a good idea, but five saying "shut up and take my money" at something visibly held together with
tape. A janky prototype is the better instrument precisely because it is ugly: enthusiasm for a
polished thing can be enthusiasm for the polish, whereas anyone excited by a spreadsheet is
responding to the outcome. On acquisition, their answer was blunter than any channel strategy — the
first paying users came from messaging people who were already complaining about the problem in
public, not from a launch. That distinction is doing more work than it appears. A launch is an
attempt to persuade an undifferentiated audience that they have a problem; a message to someone who
just described the problem in their own words skips persuasion entirely and skips the hardest step
in early sales, which is finding out who is in pain right now. A second commenter added the framing
that makes this repeatable rather than anecdotal: treat your idea, your ideal customer and your
offer as three separate hypotheses, work out what it would take to test each one, and then work
through them — while refusing to add features for which no demand has been demonstrated. That
separation is what most validation efforts lack. A failed test tells you nothing if the idea, the
audience and the price were all being tested at once, which is how founders conclude that "it didn't
work" and rebuild the wrong component. A dissent in the thread deserves an answer. One commenter
asked why everyone hunts for a novel idea when there are millions of proven business models
available to replicate with a different approach — a fair challenge, and the original poster
conceded they may have over-indexed on novelty. The reconciliation is that the hypotheses above do
not require a new idea. Copying a proven model still leaves the audience and the offer genuinely
open, and those are the two that usually decide the outcome.

**The lesson.** Set your validation threshold as a behaviour rather than an opinion, and set it
before you start: some specific number of people trying to pay for something visibly unfinished.
Find those people where they are already describing the problem publicly, in their own words,
instead of assembling an audience and explaining the problem to them. And keep your idea, your
buyer and your offer as separate hypotheses tested separately, so that when something fails you
learn which one it was rather than rebuilding all three.
*(via a founder thread on r/micro_saas)*

### 144. Priced between praying and paying an agency

**The pain.** You shipped. The interface works, checkout works, you announced it. A week later the
sinking realisation arrives that the parts nobody demos — keys, auth, webhooks — were never done,
and the two available options both look wrong: ignore it, or pay thousands for a proper audit you
cannot justify at zero revenue.

**The struggle.** A founder built a product directly out of this pattern, and the launch post is
worth studying as a positioning artefact rather than only as a story. Their observation: people
build real products with assisted coding tools, the interface works, payment works, they announce
that they are live — and then a week later there is a live payment key committed to source, or a
privileged database key sitting in client code, or a webhook that never verifies signatures. Their
line for it is the whole thesis in six words: "The demo was the easy part." The market gap they
identified is not technical but economic. The people making this class of mistake are precisely the
ones who cannot buy the existing remedy, because a security engagement is priced for companies with
revenue and these are projects with none.

**What worked.** The positioning is built almost entirely from constraints, which is what makes it
convincing. They name the wedge explicitly: a middle option between ignoring the problem and hoping,
and paying an agency several thousand dollars. Everything else follows from occupying that gap. The
scope is a checklist of the specific, boring, recurring failures rather than an open-ended promise —
committed secrets, missing server-side authorisation, wildcard cross-origin settings, vulnerable
dependencies, unverified payment webhooks, absent password reset, missing privacy page, unhandled
failed payments. That list is a positioning statement in disguise, because every item is one the
buyer has either already hit or can immediately imagine hitting. The disqualifications are stated as
loudly as the claims: not a security firm, not a replacement for a real audit, will not find every
bug, will not open a pull request, and deepest coverage only on one specific stack. Naming what you
are not is usually treated as weakness in a launch post; here it is the mechanism that makes the
rest credible, and it pre-empts the review that would otherwise arrive from the first user with
different expectations. The product design carries the same logic. Every finding ships with a
ready-to-paste fix prompt for the assistant the user is already coding with, and the score should
only improve if the issue genuinely stopped firing — which means the deliverable is a resolved
problem rather than a report, and the re-scan converts a one-off purchase into a loop with a reason
to return. The pricing follows the buyer rather than the cost: a free tier that is a real scan with
a real score, then twenty-nine dollars once for a single project or twenty a month for someone
shipping several. That is the correct shape for this audience, because a solo builder with one
project will not sign up for a subscription, and the person with a portfolio will. Two moves at the
end are worth copying regardless of what you sell. The call to action is tied to the moment of
maximum fear — scan it before you put real users on it — rather than to a generic invitation. And
the post closes by inviting a roasting and asking readers for the dumbest production hole they found
after thinking they were finished, which turns a promotional post into a thread people can
contribute to, and collects the exact examples that will make the next version of the pitch better.

**The lesson.** The strongest positioning is usually a gap between two options your buyer already
knows they are choosing between, so name both and stand in the middle. Say what you do not do, in
detail — the disqualifications are what make the claims believable, and they filter out the users
who would have churned angrily. Price for the buyer's shape rather than your costs, put the call to
action at the moment the fear is real, and end by asking a question only your actual users can
answer.
*(via a founder thread on r/micro_saas)*

### 145. Twenty founders described themselves in one line

**The pain.** You need to be visible in the places your buyers gather, but every route in either
costs money you do not have or reads as self-promotion and gets you ignored, so you post nothing and
stay invisible.

**The struggle.** Someone building a tool for generating short-form video posted an offer in a
founder community: drop your product and a sentence about what it does, and they would make one
short vertical video for a few of them, free. They stated the terms with unusual clarity — no
signup, no purchase, no testimonial required, and the finished video is yours to use anywhere. It
worked. Around twenty founders replied, each with a product and a one-line description.

**What worked.** Two separate lessons sit in this thread and both are useful. The first is the
structure of the offer itself, which is a well-built piece of go-to-market disguised as generosity.
The person building a video tool needs three things: examples to show, evidence that the output is
good enough that strangers want it, and contact with the exact people who would eventually pay. The
offer produces all three at once, and it does so without a single conversion barrier — the explicit
absence of signup, payment and testimonial is what makes it credible, because each of those would
have converted a gift into a transaction and suppressed replies. Note that the scarcity is real
rather than manufactured: they will pick a few, which means everyone answering is applying, and the
selection step is what makes the free work sustainable instead of unbounded. Compare this to the
usual founder-community promotion, which asks for attention and offers nothing, and the difference
in response is not surprising. The second lesson is what the replies themselves demonstrate. Twenty
founders, forced into one sentence each, produce a natural experiment in positioning that is worth
reading closely. The ones that land describe a recognisable moment: a bookmark manager framed as the
"I saved this somewhere but can't find it now" problem; an alarm clock that cannot be switched off
until you complete a task, aimed at people who snooze; a tool for pausing before impulse purchases,
explained by its mechanism — save the item, wait, come back and decide. Each of those puts the
reader inside a situation they have been in. The ones that disappear describe a category instead —
an all-in-one suite, a platform, a way to get more traffic — and could be almost anything, which
means the reader has nothing to attach them to. Nobody in the thread was writing a positioning
statement, which is exactly why the contrast is so clean. And a commenter with production experience
supplied the operational detail: keep the videos to twenty or thirty seconds, show the product
early, and give each video a single problem — and, counter-intuitively, flashy products are easier
to film but "boring tools with a clear problem can make better content," because the problem does
the work that the visuals cannot.

**The lesson.** If you need to be visible to a community without a budget, build an offer that gives
away the thing you are best at, remove every barrier from accepting it, and cap it by selecting a
few — you will collect examples, proof and a list of interested buyers in one motion. And when you
get your own sentence, spend it on a moment rather than a category: name the situation your buyer
was in the last time they needed you, in the words they would use, and let them recognise
themselves. A description that could belong to a hundred products belongs to none of them.
*(via a founder thread on r/micro_saas)*

### 146. Working backwards from the number you want

**The pain.** You have customers, pilots and demos, and a vague sense that this should be worth
something eventually. What you do not have is any idea whether the number in your head is achievable
or fantasy, or what this year's decisions have to do with it.

**The struggle.** A bootstrapped founder building a business-to-business software product with a
cofounder asked the question plainly. They are not aiming at a unicorn. They want a modest
acquisition in three or four years that pays each founder a seven-figure sum, so that the next
company can be started without financial anxiety. Was that realistic — and would taking venture
money, largely for the name and the credibility, help or hurt? The thread answered both parts
concretely, and it is one of the more numerically specific discussions to appear in these
communities.

**What worked.** The financing answer arrived first and was close to unanimous. Venture funds are
not built for a business whose founders intend to sell modestly; their returns require outliers, so
a stated plan to exit small is disqualifying — "no VC will touch you if your stated goal is a 7
figure exit." More practically, taking the money changes what is permitted afterwards: a board seat,
lost ownership, and pressure toward further rounds and faster growth. One commenter put the
mechanism in numbers — raise at a twenty-five million valuation and it becomes difficult to sell
below roughly three times that, and by a Series A the preferred holders may be able to block a sale
outright. A counterargument ran alongside and is worth holding: control depends on your cap table
and veto rights, exits through acquisition are far more common than exits through public listing,
and a founder weighing a high probability of a few million against a small probability of much more
after another five to eight years will often reasonably prefer the first. The disagreement is real,
but both sides agree on the practical point — the financing decision has to be made backwards from
the outcome you actually want, not forwards from what is available. The valuation arithmetic was
supplied several times and converged. Acquirers pay a multiple of revenue or profit, so the target
translates into a revenue figure: roughly a million in annual recurring revenue puts a company in
range of a five to ten million sale depending on margins and product quality, while a business
throwing off around twenty thousand a month in profit without founder involvement is worth something
like four to eight times annual profit. One commenter, working from this founder's stated high
margins, put the requirement at roughly a quarter to three hundred thousand in annual revenue
sustained for several years to clear a million-dollar valuation. The condition attached to all of
these is the part with marketing consequences: the multiple depends on the business running without
the founders in it. Which produced the most useful comment in the thread for anyone reading this
book. Working from that revenue target, the same commenter estimated a marketing budget around
twenty per cent of revenue — fifty to sixty thousand — and named it as the real challenge, along
with finding someone who can turn that spend into several times its value. That is the whole chain
made visible. An exit number implies a revenue number, which implies an acquisition budget, which
implies a channel that works at that scale and a person who can run it. Another commenter added the
diligence view: show recurring revenue quality and retention, disclose customer concentration
separately, and be explicit about how much delivery depends on the founders — all three are
go-to-market facts before they are finance facts, since concentration is a distribution failure and
founder-dependency is usually a sales process that was never written down.

**The lesson.** An exit target is only useful once you have run it backwards into this year's
operating plan: the price implies a revenue level, the revenue implies an acquisition spend and a
channel that scales to it, and the multiple applied depends on whether the company works without
you. Decide your financing from the outcome you want rather than the money on offer, because
accepting the wrong kind removes the ending you were aiming for. And treat the unglamorous
distribution work — retention, spreading customer concentration, a sales process someone else can
run — as the thing being valued, since that is precisely what a buyer is paying a multiple for.
*(via a founder thread on r/startups)*

### 147. Using the product every day was the marketing

**The pain.** You have shipped something decent and now you face the second job, which is producing
a steady supply of content and outreach forever, on top of building. It is a separate full-time
role, you are one person, and every week you do not do it the product sits still.

**The struggle.** A solo founder described how they arrived at a different arrangement, and the
useful part is that they started from a failure. Earlier in the year they sold a job-hunting tool
for under ten thousand dollars — recurring revenue had begun to decline, a job offer arrived, and
they took both. Their diagnosis of that product was structural rather than about effort: it was
never a natural fit for any self-feeding growth mechanism, and by the time you learn the term for
what you are missing, you usually already have an idea that cannot support it. So they made the
mechanism a selection criterion for the next thing rather than something to be bolted on later. The
requirement was set before the idea: whatever they built next had to have some growth loop they
could run repeatedly and mostly automate.

**What worked.** The product came from their own irritation. Watching long videos — lectures,
podcasts, founder interviews — to extract one specific thing, which in their case was always the
same thing: which distribution channels a company used and how they started, not the technology
stack, not the founder's background, not the company's size. So they built a tool that watches a
video and returns a summary, a clickable table of contents, and a chat you can interrogate for the
part you actually wanted. The loop is where this becomes worth studying, because the product and the
marketing are the same activity. Every day they use their own tool on videos of founders explaining
how they grew their companies, extract the summaries and transcripts in bulk, feed those into an
assistant, and turn them into posts and articles about distribution channels. Those posts go on X,
attributed to the tool that produced them. The audience for writing about how founders get
customers overlaps almost exactly with the audience that wants to pull information out of long
videos, so a proportion of readers try the tool on their own material, and the ones who want
unlimited use upgrade. They ran the same loop against trending releases and model announcements,
which supplies a second content stream on the same machinery. The result is one hundred dollars in
monthly recurring revenue — their fourteenth product, five months in, with most of the growth
arriving in the last couple of weeks, once the loop started rather than when the product launched.
That timing detail is the most important number in the post. The build was not the constraint and
neither was the product's quality; the distribution mechanism was, and revenue moved when the
mechanism did. Three further things are worth taking. They put real work into a landing page that
reads as though a funded team is behind it when it is one person, which is worth noting honestly:
presenting a solo project as a company is a positioning choice with a limit, and it becomes a
problem the moment a buyer's expectations about support and longevity are set by it. Second, their
next step is a genuinely clever extension of the same asset — summarise entire playlists in bulk to
produce search-indexed articles from material that no blog contains because it exists only inside
videos. That is arbitrage on a format boundary, and it lasts exactly as long as the boundary does.
Third, they have an exit number, and they have done the arithmetic out loud: not chasing a large
business, but building toward roughly five thousand a month and selling at what they estimate as
sixty thousand of annual revenue against a multiple of around four — about two hundred and forty
thousand dollars, which they describe as four or five years of living costs before building the
next one with what they learned. The most valuable line in the discussion is the caveat that
followed a commenter's endorsement of the whole approach: "not every product can do this." Which
returns you to the founder's opening point. This is a filter applied before the idea, not a tactic
applied after it.

**The lesson.** The best distribution is a by-product of using your own product, so ask before you
build whether daily use of the thing would generate something worth publishing — and if it would
not, know that you are signing up for marketing as a permanent second job. Where a loop does exist,
look for the overlap that makes it work: the audience for the content your tool produces has to be
the audience that wants the tool. And watch the timing in stories like this one, because it repeats
— revenue moved five months in, not at launch, and it moved when the loop started, which means the
months of building were not the thing that was missing.
*(via a founder thread on r/micro_saas)*
