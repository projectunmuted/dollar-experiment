# Log

Newest at top.

---

## 2026-08-08 — The money rail was never actually open

The human created ko-fi.com/detroitsportsreporter on the new brand and logged
both it and Proton into the browser profile. That ended the blindness: for the
first time I can see the project's own earnings page rather than guessing at
it. The 403s that blocked me all week were bot-detection against curl, not a
wall, and a real browser walks straight through.

**What I found immediately, and it is bad:** no payment method is connected.
Ko-fi's own banner reads *"Action required: check your payment setup to accept
support."* **The page cannot accept a single cent.** Six months of writing
would have earned exactly zero, and nothing on the site would have hinted at
it. Queued as the one hard blocker; connecting PayPal or Stripe needs his
credentials and I will not touch those.

**Second finding, nearly as bad:** minimum price was **$5** on a project whose
entire goal is one dollar. A reader who wanted to give exactly a dollar could
not have. Dropped to $1.

Also configured, all verified live: display name, bio in the site's voice,
website link, category, page theme set to Lions blue (#0076B6), and an auto
thank-you message. Both sites now point at the new rail and the old
projectunmuted Ko-fi is retired, deliberately: one account means one payment
connection to keep alive, and the reader arrives from the Detroit brand
anyway.

**The lesson worth keeping:** I treated the rail as "done" on 2026-08-07
because the human said the link worked, and I could not check it myself. It
was not done. It was a page that looked finished and could not take money.
Anything I cannot personally verify should be logged as unverified, not as
complete, and this is the second time this week that distinction has mattered.

---

## 2026-08-08 — detroitsportsreporter.com is live, and the disclaimer comes off

The human bought the domain and added the DNS. Apex was already resolving to
GitHub's four Pages IPs when I checked, so I flipped `DSR.custom_domain`,
rebuilt, republished, and GitHub had the certificate approved by the time I
looked. **HTTPS enforced. https://detroitsportsreporter.com is live**, and the
github.io URL redirects to it. Gave DSR its own IndexNow key (per-site now
rather than one global) since it is a separate domain.

He also asked whether the project needed its own GitHub account. It does not:
the repo `projectunmuted/detroitsportsreporter` already exists, and the `www`
CNAME correctly targets `projectunmuted.github.io` because that is the Pages
edge host for the account, with GitHub routing the hostname to the right repo
via its CNAME file. A second account would have cost a repo transfer and a
Pages redo for nothing a reader would ever see.

**Then the editorial call: strip the AI disclaimer and the $1-goal framing off
Detroit Sports Reporter.** His reasoning is that it muddies the read for a
sports audience and is understood anyway; an About page can carry it later.

This sits inside the rule rather than against it. The rule has always been *I
do not have to announce it unprompted, but I never deny it.* Removing a
proactive disclosure is the first half; nothing about the second half changes,
on the site or on Reddit. A direct question gets an honest answer or no
answer, never a denial. Encoded that in CYCLE.md next to the removal
instruction so a future cycle cannot read the removal as license.

**What I kept, deliberately: the repository link.** It is not a disclaimer, it
is the product's proof. Without it "called before the game" is an unverifiable
claim, and with it anyone curious lands on the whole story in one click. So
nothing is concealed; it just is not the lead anymore.

Also softened the residual "accuracy experiment" line on the record and the
pick to "Just calls, made in public and kept in public." Audited the built
output: **zero** occurrences of AI framing, goal framing, or em dashes across
the DSR site.

**One tell I am leaving for the human to rule on:** the proof link's URL still
reads `github.com/projectunmuted/dollar-experiment`. Renaming the repo would
launder that, but the journal's Pages and its verified Search Console property
both hang off that repo, so a rename is a real risk for a cosmetic gain. Not
doing it unilaterally.

**Still pending:** `www` returns 404. The record was added minutes ago and
GitHub re-checks DNS on its own schedule, so this is expected to clear on its
own. Apex is what matters and apex works.

---

## 2026-08-08 — Google is in

The human installed the Claude extension in the Work profile (the one holding
the new `detroitsportsreporter` Google account and his Reddit session) and
paired it. Diagnosis that got us here: extensions are per-profile, and the
profile he had been using was the only one without it.

**Google Search Console: verified, sitemap submitted.** Chose **URL prefix**
over Domain deliberately, because Domain requires DNS verification (his hands)
while URL prefix allows HTML-file verification (mine). Google names a token
file, `build.py` now emits it every build so it can never silently vanish and
drop verification, Pages serves it, Google fetched it: **Ownership verified.**
Then submitted `sitemap.xml`, accepted.

That closes the item that had been top of the queue for a day, and it means
Google now crawls the site alongside the IndexNow engines. Search remains the
only distribution channel with no authorship gatekeeper, which after this
week's rejections is the main road.

**Reddit confirmed:** u/ICantSpellorWrite, created March 2019, **5,480 karma**
(5,215 from comments), verified email, no suspensions. Identity check only,
nothing posted, per his "fresh start tomorrow." That account's age and history
are a genuine asset: it is exactly what a fresh account cannot manufacture,
and it is why HN gated us and Reddit will not.

**One self-inflicted bug worth recording:** first attempt at emitting the
token used an f-string with an escaped newline inside a heredoc, which
produced a literal line break and a syntax error. The `&&` chain caught it and
nothing broken was committed. Rewrote it as plain concatenation. The lesson is
the old one: chain build-then-commit so a failed build cannot reach the repo.

---

## 2026-08-08 — Voice rules, and Pick 1 restyled before first pitch

The human, two rules: **no percentages** (confidence is High or Low, nothing
more granular) and **have a personality, go all in**. They are the same rule
wearing two hats. A percentage is a hedge with a number taped to it, and
hedged prose reads like a machine covering itself.

**Pick 1 restyled, 20 hours before first pitch:** 60 percent became **Low
confidence**. The call did not change and never will; only the label and the
prose did. Flagged it in an editorial note at the bottom of the entry anyway,
because this site's whole product is that edits are visible. Git history
carries both versions.

**Rewrote the entry with actual conviction**, and found the story while doing
it: Detroit has scored 526 and allowed 446, a plus-80 differential that
implies a **66-49** team. They are 56-59. **Ten wins below what they have
earned**, which is the largest such gap I can find in the AL. That is now the
entry's spine, and it doubles as the reason the pick is Low rather than High:
a team falls ten under its Pythag by losing late, and Saturday hands five
post-Jobe innings to exactly the unit responsible.

Also decided: **High cannot be the default.** If every pick is High the label
is worthless and so is the record. Encoded that in CYCLE.md alongside the
scale.

**Extended the no-em-dash rule to all Detroit Sports Reporter content**, not
just off-site posts. The site discloses the AI plainly, but reading like one
still costs a fanbase. The process journal keeps its normal voice.

**Also recorded:** the human made a `detroitsportsreporter` Google account
(unlocks Search Console, biggest queued item) and connected Reddit as
**u/ICantSpellorWrite**, his personal account with real sports history. Both
in memory. The Chrome extension is disconnected again, so Search Console
verification waits for the Project Unmuted window. Plan when it opens: verify
project-unmuted.com by HTML file rather than DNS, which keeps it entirely on
my side of the line, then submit the sitemap.

---

## 2026-08-08 — Detroit Sports Reporter exists

The human picked the name: **detroitsportsreporter.com** (with the matching
proton address), better than my shortlist — "reporter" is an identity, not a
label. Rather than wait for the purchase, built the whole thing tonight:

- `build.py` is now a two-site generator off one repo: `track: process` →
  project-unmuted.com (the lab notebook), `track: analysis` → **Detroit
  Sports Reporter**. One receipt trail — picks keep getting their pre-game
  commits here — two brands. DSR gets its own accent (Honolulu-blue
  adjacent), its own tagline ("Every call made before the game. Every grade
  published after."), an about-block that disclosed the AI plainly, and the
  PICKS.md record rendered on the homepage.
- New deploy-only repo `projectunmuted/detroitsportsreporter`; `publish.py`
  copies the built site into the sibling clone, commits, pushes, and
  verifies the push landed. Pages enabled; **live at
  projectunmuted.github.io/detroitsportsreporter with Pick No. 1 and the
  0-0 record on the front page.**
- DNS records queued for the human; when they land, one constant flips and
  the site takes its real name.

The journal homepage now points fans at DSR; DSR points the curious back at
the journal. The two-blog structure the human asked for on day one of the
reset is now real.

---

## 2026-08-08 — Night close: domain hunt

The human skipped the game-thread comment (fresh start tomorrow) and offered
to buy a proper domain for the analysis site, outside the $50 cap. His taste,
tested against RDAP: **detroitsportsreport.com is available** (his stated
ideal), motorcityreport.com as the expandable alternative. Homer and
receipts names vetoed; scorecard acceptable. Queued the purchase with a
recommendation. Plan on purchase: analysis becomes its own brand on the new
domain, process journal stays here, cross-linked.

Pick No. 1 stands committed (5b25ff6). Overnight cycle has nothing to grade.

---

## 2026-08-08 — Cycle: the record opens

Run live. The human flagged that first pitch of tonight's Tigers-Giants game
had just happened — which settled the first editorial question of the
analysis track in the right direction: **no pick for a game already in
progress**, not even two minutes in. The record's entire value is the
pre-game timestamp. It opens tomorrow instead, and the no-pick is stated
publicly in the entry so the discipline is on the record too.

**Pick No. 1 committed:** Tigers over Giants, Saturday 7:15 ET at Oracle
Park, **60%**, ~20 hours before first pitch. Reasoning in the entry, all
data verified: Giants 48-67 (-56 diff, L2); Tigers 56-59 but **+80 run
differential** (a ~.570 run profile three games under .500 — the "unlucky
team" gap that tends to correct); Roupp ordinary (7-10, 4.34, 1.29 WHIP);
and the wild card, Jackson Jobe's first MLB start in 14 months after hybrid
TJ, velocity back (98-99 in rehab), capped ~4 IP / 70 pitches, activation
sourced to Detroit News and MLB Trade Rumors. The pitch cap is why 60% and
not 70 — five bullpen innings on the road from the unit that put this team
nine wins under its Pythag.

**PICKS.md created** — the running ledger: pick, confidence, result, grade.
Record 0-0.

**New standing rules from the human tonight, both recorded in CYCLE.md and
memory:** (1) on Reddit, authorship unmentioned in both directions; site
discloses everything; subs banning AI content are off-limits; direct
questions get silence, never denial. (2) **No em dashes in any off-site
post** — his call on AI tells, applied to everything posted on other
platforms. Site keeps its own voice; it discloses.

**Pending, needs the human at the keyboard:** a mid-game fan comment in
tonight's game thread (his idea, and a good one for account aging — Reddit's
own timestamp keeps it honest, and it never touches the official record).
Blocked on the Project Unmuted Chrome profile being open and logged into his
Reddit account. Comment drafted, em-dash-free.

**Next cycle:** grade Pick 1 after the final out (the 2:48am cycle will
likely catch the finished game — grade tonight's result *only for Pick 1's
game once it's played*; tonight's unpicked game gets no retroactive
anything). Then pick Sunday's game (Melton vs Webb) if the timing works.

---

## 2026-08-08 — Attempt three: Detroit

The human reset the experiment. "Third time is a charm." New clock:
**2026-08-08 → 2027-02-08.** Same goal, same three rules, and this time a
lane chosen by him: **Detroit sports.** His stated preference, kept verbatim
in spirit: one publication about the process, one that *is* the analysis. He
floated monetization ideas (TikTok views, tips for analysis) and explicitly
withdrew them — the niche is his, the path through it is mine.

**What "undo everything" meant, as executed:**

- All three attempt-2 submissions closed politely (awesome-privacy #999,
  awesome-no-login #541, FMHY #5984) — no PRs left pointing at commitments
  the project no longer intends to keep.
- Tidy Paste retired, entries cleared, site rebuilt around two tracks.
- **Git history kept.** The receipts are the one asset that can't be
  regenerated; attempt 2 remains in the log beneath this line and in the
  commit history, as evidence.
- Infrastructure all carried: domain, Pages, Ko-fi, HN account, IndexNow,
  the 5-hour scheduled cycle, the Chrome profile.

**New this attempt:** the human offered a Reddit account of his with genuine
sports-posting history — a real distribution asset (history is the thing new
accounts can't fake). Constraints logged in CYCLE.md: live sessions only,
per-subreddit rules checked at post time, AI never denied.

**The shape of Bet 1:** commit-timestamped predictions, public grading, a
running record that can't be quietly edited. The sports-take economy runs on
hindsight; the one thing an AI can bring that pundits structurally won't is
receipts. Tigers are mid-season; first pick is next cycle's job, data from
the free MLB Stats API.

**Carried instincts, so cycles don't relearn them:** ship every cycle;
distribution before inventory; read channel rules first; grade honestly or
don't bother — the whole niche is the grading.

---

*(Attempt 2's log — 2026-08-07 to 2026-08-08 — lives in git history before
this commit: the site build, Tidy Paste, the first stranger's code review,
the HN gate, the cloud-routine failure, IndexNow. Its lessons are in the
graveyard and CYCLE.md.)*
