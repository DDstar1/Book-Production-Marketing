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
