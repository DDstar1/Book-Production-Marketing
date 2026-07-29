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
