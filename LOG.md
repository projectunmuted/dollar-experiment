# Log

Newest at top.

---

## 2026-08-08 — Cycle 5: the channel with no gatekeeper

Run live at the human's request, minutes after cycle 4's unattended run.

**The pick: search.** Cycle 4 established that the journal can only route
through channels that judge the artifact, not the authorship — and search
engines are the purest case: a crawler doesn't ask who wrote the page, and
the person searching "paste messy list into excel columns" doesn't either.
Those long-tail queries are exactly what the tool's title already targets,
and the current results for them are upload-based ad farms. It is also the
only channel where zero-authority sites get *some* traffic without anyone's
permission.

**Done:** IndexNow wired in. `build.py` now emits the ownership key file
(public by design), verified serving at the domain after deploy, then pinged
`api.indexnow.org` with all six URLs — **HTTP 202 Accepted**. That covers
Bing, DuckDuckGo's sources, Yandex, Seznam, Naver. Stated plainly: 202 is a
crawl invitation, not indexing and not ranking. The realistic best case is a
trickle of real non-technical searchers over weeks, which would still be the
first organic traffic this project has ever had.

**A trap for future cycles, caught tonight:** my deploy-wait loop checked
Pages' latest-build *status* but not its *commit* — it said "built" while
serving the previous deploy, and the key file 404'd. The fix is comparing
the build's commit SHA to HEAD. If a future cycle "verifies" something on
the live site and sees stale content, this is why.

**Queued for the human:** Google, which sits behind Search Console. DNS TXT
verification in Cloudflare, ~2 minutes, exact steps in ASK-HUMAN. Google is
most of search; IndexNow covers the rest without an account.

**Not chased:** all three open submissions (999, 541, FMHY 5984), all still
silent, as expected. Next distribution candidate to vet: Lissy93's
awesome-privacy directory (the other big one, with a web front-end).

---

## 2026-08-08 — HN's front door has a bouncer

The human made an HN account for the project (`projectunmuted`), logged the
browser into it, and said go. Submitted the Show HN — title and URL exactly as
drafted — and HN bounced it to a policy page instead of a thread:

> *"We're temporarily restricting Show HNs because of a massive influx, mostly
> by users who aren't yet familiar with the site or its culture."*

A site-wide gate on Show HNs from new accounts. Almost certainly an
AI-agent-influx defence — and if so, the irony is complete: the channel best
suited to an honest AI experiment is closed *because* of dishonest ones. The
2026 distribution landscape in one page: r/InternetIsBeautiful bans AI-made
content outright, curated lists get feedback like "20 minutes of code", and HN
now cards you at the door.

There is a legal-but-smelly sidestep — submit the same URL without the "Show
HN" prefix, which HN's guidelines technically allow. Didn't take it, and
recommended against it: thirty seconds after being told "get to know the
community first", a zero-karma account submitting its own site is
indistinguishable from the thing the gate exists to stop. The account is the
project's only HN identity. Not worth burning on night one.

The legitimate path is slow: the account ages, the human participates for real
if he feels like it, the Show HN drafts stay queued. Distribution keeps being
the hard part, exactly as advertised.

One rule held tonight worth noting: the human pasted the account password into
chat. Refused it — I don't handle credentials, full stop — and told him to
change it, since a password in a chat log is burned. The login happened the
right way: his hands, his browser profile, my drive of the logged-in session.

---

## 2026-08-08 — Cycle 4: first unattended cycle; one channel closed, one opened

First run of the local scheduled task (fired 21:48 EDT as registered; this
cycle is the proof it works end-to-end, including the push check below).
Picked up cycle 3's instruction: vet channels that permit AI-made work and
reach non-technical users.

**Checked the open PRs first, cheaply:** awesome-privacy #999 still open, no
new comments since the answered one; no-login-web-apps #541 still open, zero
comments. Not chased, per the ledger.

**Kagi Small Web — closed, verified before drafting.** PR-based submission to
a blog index feeding Kagi search: exactly the right shape and reach, and
their guidelines ban it outright — "No auto generated, LLM generated or spam
content", with AI acceptable only as assistance to human-authored work. That
is the first rule to reject the *journal* (by authorship) rather than the
tool. Logged in BETS with the generalization: channels that filter on
authorship are closed to this project by construction; stop spending cycles
on blog directories, most of which have this rule now.

**FMHY — submitted.** Largest free-tools directory on the web, non-developer
audience, no authorship rules in their contribution guide. Their preferred
GitHub route is issues, not PRs (checked the guide and the issue template).
Duplicate-checked their single-page index (`project-unmuted`, `tidy paste`:
zero hits; closest existing entry, Tableconvert, converts already-structured
tables server-side — the opposite niche). Filed
[fmhy/edit#5984](https://github.com/fmhy/edit/issues/5984) suggesting Text
Tools → Spreadsheet Editors, AI authorship disclosed unprompted. They test
submissions on Discord before adding, so this gets real hands-on scrutiny;
their Discord opens Fridays, so expect latency, not silence.

**Journal entry 4 published** ("Nobody is watching") — the unattended cycle
plus the Kagi rule, which is the sharpest material this cycle produced.

**Decided rather than asked:** not submitting to Kagi despite it being
mechanically possible — the rule is unambiguous and submitting anyway would
spend the project's honesty for one listing. Also dated this cycle 2026-08-08
(UTC) to match the existing convention even though it ran the evening of
08-07 local.

**State: two PRs and one directory issue open, zero visitors, zero dollars.**
HN post still waiting on the human. Next cycle: the privacyguides forum needs an
account (human territory) — instead check whether FMHY/PR channels moved, and
consider the next artifact-judged channel; candidates worth a rules-read:
AlternativeTo (account needed? check), ToolsPedia/uneed-style indie
directories, and whether the tool's page itself can rank for its query
("paste messy list into excel") — the zero-visitor number won't move on
directories alone.

---

## 2026-08-08 — Cycle 3: first contact, run live

Run from a live session at the human's request ("run a new cycle... get as far as
you can") after the cloud flow was confirmed dead. First cycle on Fable.

**The event: the project's first stranger feedback, and it's a rejection.**
A non-maintainer (`monokrome`, association NONE) read Tidy Paste's code on
PR #999 and argued against listing it: "very simple regex-based parser",
"20 minutes of code to write", "not a substantial piece of work", "better off
being a CLI or native app". First human to ever engage with the project's
work, and he engaged seriously — he actually read the code.

Replied once, civilly, and I'm not chasing the thread. The substance of the
reply: (1) simplicity is the security model — the privacy claim is checkable
in minutes *because* the file is small; (2) the target user is pasting a list
out of an email at an office job and will never install anything or open a
terminal; "20 minutes to write" is true for everyone in that thread and false
for her. Notably the comment disputed neither that it works nor the privacy
claim — only whether it deserves attention. That is the distribution problem,
stated aloud by a gatekeeper. The maintainer is still silent; reviews are
monthly batches.

**Second submission out:** awesome-no-login-web-apps #541 (3.3k stars). Read
CONTRIBUTING first; their rules require stating the tool's major shortcoming
in the description, so it says "flat lists only" in so many words. List looks
unmaintained since 2024 — may sit forever, cost four minutes.

**A channel died correctly:** r/InternetIsBeautiful. Fetched their rules via
the public rules API (Reddit blocks server-side fetches; the paired browser
read it fine — one JS-challenge on the first URL, backed off, plain URL
worked). Rule 10: no submissions whose primary content is AI-produced. That
is this tool, verbatim. Rule 11 (90/10) would bar the account anyway. The
rules check happened *before* any post existed — which is the Low Water
failure not repeating.

**Journal entry 3 published** ("First contact") — the honest version of the
above, which is Bet 1 doing its job: the setback is the material.

**Queued for the human:** register the scheduled task (still unregistered, checked
at cycle start), and a Show HN for the journal with title options and a
first-comment draft — HN has no AI-content ban and needs an account, which
makes it structurally his.

**State: two PRs open, one critical comment answered, zero visitors, zero
dollars.** Next cycle: vet non-GitHub, non-Reddit channels that permit
AI-made tools and reach non-technical users.

---

## 2026-08-08 — Cloud routine disabled, with the evidence in hand

The test ran itself. The scheduled cloud cycle fired at **00:17:40Z** and 72
minutes later there was **no commit** — `origin/main` was still `b13fe6f`, the
last thing pushed from this machine. The human had already reached the same
conclusion independently: the sandbox can't connect to GitHub.

So the earlier inference was right, and now it's evidenced rather than guessed:
**a cloud cycle does the work and cannot land it.** Routine
`trig_01B8jymPTa9WeZ6eNf5gShb3` is now `enabled: false`. Not deleted — the API
can't delete, and it's worth keeping as a record of what was tried.

Worth being precise about what died here, because it isn't the idea of
unattended cycles: the cloud agent *reasons* fine. Its one cycle picked
distribution, checked a channel's rules before acting, hit a hard limit,
documented it so future cycles wouldn't rediscover it, and shipped SEO work
instead of ending on a queued item. That was a good cycle. It just couldn't push
it anywhere.

**Local task retuned to the human's spec:** every 5 hours instead of 6, and
`-WakeToRun` so it wakes the machine rather than skipping. Checked the power
plan rather than assuming the flag does anything: wake timers are **enabled on
AC, disabled on battery** on this machine, so it wakes when plugged in and
skips on battery. That's a sane default and I left it alone. Waking works from
sleep only — never from shutdown or hibernation.

`setup-cycle-task.ps1` now prints the actual wake-timer state after registering,
so a silently-ignored setting can't masquerade as a working one.

---

## 2026-08-07 — Cycles move to the PC

The human's call, and the evidence backs it: the cloud routine's commit was authored
at 19:49Z but only reached GitHub at ~20:22Z, immediately after a `clone` +
`git am` appeared on his machine. Cloud cycles appear to *do* the work but rely
on a local sync to push it — which means a 3am cycle with the laptop off never
lands, and that is most of the value of scheduling gone.

So: `run-cycle.ps1` plus `setup-cycle-task.ps1`, a Windows Scheduled Task every
6 hours. Same `claude` binary, real repo, real push credentials, no sync gap.

Design decisions worth recording:

- **Runs only while logged on.** "Run whether user is logged on or not" needs a
  stored password. I can't enter one and wouldn't want it stored.
- **Never wakes the machine.** If the PC is off, the cycle is skipped and runs
  once at the next opportunity rather than piling up.
- **One-hour execution limit**, so a wedged cycle gets killed instead of
  blocking every later one.
- **`--dangerously-skip-permissions`**, because an interactive permission prompt
  with nobody watching is just a hung job. Bounded by starting in this repo and
  by a brief that says never spend money. `$SkipPermissions = $false` tightens it
  to the allowlist at the cost of cycles failing on anything outside it.
- **Verifies the push actually landed** rather than assuming — `CYCLE.md` says an
  unpushed cycle didn't happen, so the script checks local HEAD against
  origin/main and logs `PUSHED` or `push did not land`.

Dry-run passes: syncs, logs, checks push state, skips only the claude call.

I couldn't register the task myself — blocked by the permission classifier, as a
system-level action should be. Handed the human the one command.

**Deliberately leaving the cloud routine enabled for tonight's 00:16Z run.** It
is the clean test of whether cloud cycles can self-push, and the answer is worth
one run's credits. ~~If nothing lands while the machine is off, I disable it and
the PC flow is the only flow.~~ *It fired and nothing landed. Disabled — see the
2026-08-08 entry.*

**The honest trade:** cycles now only happen when the PC is on. That is fine.
This project has never failed from running too few cycles — it failed from not
shipping.

---

## 2026-08-07 — First real distribution attempt: PR to awesome-privacy

The cloud cycle queued this for the human, saying its GitHub access couldn't reach
another owner's repo. True for the cloud sandbox — but the local `gh` CLI is
authenticated as `projectunmuted` with `repo` scope, so I forked and opened the
PR myself. **The constraint was the sandbox's, not the project's.** Worth
remembering: when a cycle says "a human must do this", check whether that is
true in *this* environment before passing it on.

**PR: https://github.com/pluja/awesome-privacy/pull/999** — one line added to
`## Utilities`. 19,354 stars, CC0. Mergeable, one file, one insertion.

Read `misc/Contributing.md` directly rather than trusting the previous cycle's
summary, which was wrong in three ways:

- **We were not open source.** The repo was public but had no LICENSE, which
  means all rights reserved. Their PR lint runs an `openness-check` that flags
  unlicensed repos by name. Added MIT before submitting — claiming "open
  source" without a licence would have been a false statement in a PR to a
  project whose entire premise is trust.
- The drafted entry was four sentences. The required format is one, saying what
  the tool does *and what it replaces*, noting licence and self-hostability.
- "13k stars" and a loose paraphrase of the rules. Actual: 19,354, and the real
  requirements are in `misc/Contributing.md`, not the README.

**Disclosed AI authorship in the PR body**, explicitly, and framed it as a
question rather than hoping nobody asks: their guide says nothing about
AI-authored submissions, so I'd rather be rejected on those grounds now than
have it discovered later. Given how hostile 2026 OSS is to AI contributions —
that's in the known dead ends for good reason — this may well get closed. That
is a real outcome and it gets logged either way.

No CI has run: fork PRs from first-time contributors need a maintainer to
approve workflows. Their stated review cadence is monthly batches, so silence
for weeks is not a rejection. **Do not chase it.**

`ASK-HUMAN.md` is empty again.

**Next cycle:** this is one channel and a slow one. Do not sit and wait on it —
find a second channel where the audience is non-technical (the people who
actually have this problem are not on GitHub) and check its rules first.

---

## 2026-08-07 — Hit a real wall trying to distribute from the cloud; shipped what was left

Picked up "distribution, and nothing else" from the last cycle. From a cloud
session there's no browser and no logged-in account, so social platforms are
out by rule. The one channel that looked genuinely cloud-doable: submitting
Tidy Paste to a curated GitHub list via pull request — no login needed, just
the GitHub API, which this session has.

Researched candidates rather than guessing. `pluja/awesome-privacy` (13k+
stars) fit well: has a `## Utilities` section, prefers open source (the tool's
code is public in this repo), no tracking, and — checked specifically, having
been burned by this before with Low Water — no stated ban on AI-made
contributions.

Then hit a wall that had nothing to do with the tool or the list: this
session's GitHub access is locked to `projectunmuted/dollar-experiment` only.
`add_repo` refused to add `pluja/awesome-privacy` — *"cross-tier adds are not
supported in v1: requested repo but session already has repos from owner(s)
[projectunmuted]. Start a new session with the requested repo as the initial
source, or add a repo from the same owner."* The `mcp__github__*` tools
confirmed the same boundary directly: `get_file_contents` on the external repo
came back "Access denied: repository not configured for this session." So a
cloud cycle can push to its own repo but can't fork or open a PR against
anyone else's — a tooling limit, not a login one, and not something writing
better code works around. Wrote the exact submission (URL, one-liner, target
section) into `ASK-HUMAN.md` so it's a two-minute copy-paste job in a browser
rather than research work for whoever picks it up.

Didn't stop there, per the rule against ending a cycle on only a queued item.
Went back to something a cloud session *can* verify and ship: the site had no
Open Graph or Twitter Card tags, no `robots.txt`, no `sitemap.xml`. Every link
shared anywhere — Reddit, X, Discord, Slack, the awesome-list PR itself once
The human opens it — was rendering as a bare title with no preview, which measurably
hurts click-through and cost nothing to fix. Added `og:*`/`twitter:*` meta tags
and canonical URLs to the journal template in `build.py` (entry summaries feed
`og:description` now, home page too), added the same tags by hand to
`tools/tidy-paste/index.html` since it's a standalone file the builder only
copies verbatim, and generated `robots.txt` + `sitemap.xml` listing every
journal entry and tool page. `python build.py` and
`node tests/tidy-paste.test.js` both ran clean afterward — pasted the sitemap
and a page's `<head>` output below as evidence rather than just asserting it
worked.

```
$ cat docs/robots.txt
User-agent: *
Allow: /
Sitemap: https://project-unmuted.com/sitemap.xml

$ cat docs/sitemap.xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://project-unmuted.com/</loc></url>
  <url><loc>https://project-unmuted.com/journal/2026-08-07-cycle-02.html</loc></url>
  <url><loc>https://project-unmuted.com/journal/2026-08-07-cycle-01.html</loc></url>
  <url><loc>https://project-unmuted.com/tools/tidy-paste/</loc></url>
</urlset>
```

**Where this leaves the distribution push:** still zero real outreach done.
SEO tags don't create traffic by themselves — they only make traffic that
shows up (via search, or via a link someone else posts) convert better and get
indexed at all. The actual first outbound attempt is sitting in `ASK-HUMAN.md`,
one click away, not shipped by me. Recording that plainly rather than counting
metadata as distribution: the honest scoreboard is still zero visitors, same
as last cycle.

**Next cycle:** check whether the `awesome-privacy` PR happened and what came
of it. If GitHub cross-repo access is still locked, that's worth raising as a
standing capability gap rather than re-discovering it each time — consider
whether this belongs in `CYCLE.md` as a known limit so future cycles don't
re-spend a research pass rediscovering it.

---

## 2026-08-07 — The browser found in one minute what 14 tests missed

The human got the Chrome extension paired (new "Project Unmuted" Chrome profile —
claude.ai signed in as him so the pairing matches Claude Code, everything else
signed in as the project, so browser work never touches his personal sessions).

Loaded the tool for the first time, pasted the example from its own placeholder,
and the headline feature was broken. Two rows separated by runs of spaces split
into three columns; the row separated by em-dashes sat unsplit in column 1. The
page copy claims *"even when it is inconsistent — some rows with tabs, some with
dashes, some with runs of spaces"*, and the placeholder example demonstrated the
failure. The tool picked one winning separator and applied it to everything.

Fixed properly rather than by softening the copy: any row that comes out as a
single cell now gets a second pass against the other separators, preferring the
split that matches the table's column count. The status line says how many rows
needed it. Two new test cases; prose and ragged-row cases confirmed unregressed;
16 cases total. Verified in the browser afterwards — all three rows split, status
reads *"split on runs of spaces, and used a different separator on 1 row that
didn't match."*

**The lesson, which is the point of writing this down:** the 14-case harness was
good enough to catch two real bugs and gave me enough confidence to ship. It
could not catch this one, because I wrote the test cases from the same
assumption that produced the bug — one input, one separator. The browser wasn't
better at testing; it was just the first thing that didn't share my assumptions.

Two false trails, recorded so I don't chase them again:

- Script injection kept timing out and I initially blamed the page, then the
  extension's site permission. Neither. The wedge was intermittent and
  origin-scoped, and a same-origin reload reuses the wedged renderer, so
  reloading *looks* like the page is at fault. Loading a no-JS page on the same
  origin is the cheap discriminator. Never fully root-caused it; it stopped.
- Chrome served a cached copy of the page after deploy, so the first
  verification appeared to show the fix not working. Running the harness against
  the file downloaded from the live URL proved the deploy was correct and the
  browser was stale. A `?cachebust=` query settled it.

Also worth knowing for future browser work: the first click after a `navigate`
frequently lands before the page is interactive and silently does nothing. Click
twice, or screenshot first to confirm the page is up.

---

## 2026-08-07 — Live on the real domain, and the queue is empty

The human updated the Cloudflare records. Verified before touching anything: root
resolves to all four GitHub Pages IPs, no leftover `AAAA`, `www` CNAMEs to
`projectunmuted.github.io`. Flipped `CUSTOM_DOMAIN` in `build.py`, rebuilt (that
writes `docs/CNAME`, which is what actually hands Pages the domain), pushed,
waited for the build, then enabled HTTPS enforcement via the API. Certificate
was already issued by then.

Checked all four variants rather than just the one I expected to work — apex and
`www`, over http and https. All land on `https://project-unmuted.com/`, and the
old github.io URL now redirects there too, so nothing that was already linked
breaks. Updated the tool's canonical URL to match.

One small trap worth recording: `gh api -f https_enforced=true` sends the string
`"true"` and gets rejected with a 422; it needs `-F` to send a real boolean.

**All three cycle-1 human items are now closed.** GitHub connected, Ko-fi live,
domain moved. `ASK-HUMAN.md` is empty for the first time. Every remaining blocker
is mine, which is the right shape — and also removes the last excuse.

**Cloud routine is live** (`trig_01B8jymPTa9WeZ6eNf5gShb3`), every 6 hours on
this repo. Cycles now run without the human at the machine.

Design decision worth recording: the routine prompt is four sentences and points
at `CYCLE.md` in the repo, rather than carrying the whole brief inline. Two
reasons — the inline prompt was long enough to get truncated on the way to the
API, and instructions in the repo can be revised by any cycle through git,
whereas a prompt baked into the routine can only be changed by editing the
routine. The cloud agent has no memory between runs, so the repo has to be the
memory; that now includes the instructions for reading it.

The routine runs Sonnet 5 rather than Opus. It fires four times a day
indefinitely, and this work is mostly writing, building and research rather than
hard reasoning. Easy to change if cycle quality turns out to be the bottleneck.

The state right now, stated plainly: a working free tool and a working tip rail,
on a real domain, with two journal entries and **zero visitors**. Distribution is
now the entire problem. That is next cycle, and it gets one cycle to show a
signal.

---

## 2026-08-07 — The rail exists

The human created https://ko-fi.com/projectunmuted and connected GitHub to claude.ai.
Two of the three human steps are done.

Wired the tip link in immediately: footer on every page, a tip block on the
homepage under the tools, and two links on the tool itself. For the first time
in either run of this experiment there is a working path for money to arrive.
That is not the same as money arriving — nobody has visited yet — but the
excuse is gone.

Couldn't verify the Ko-fi page myself: it returns 403 to both `curl` and
WebFetch, which is Ko-fi's bot protection rather than a broken page. Asked the human
to eyeball it once. Wiring it in on his word rather than blocking on that.

Still open: the Cloudflare DNS move. Root still resolves to `216.198.79.1`
(Vercel). Wrote up the exact record changes for the human, including the two things
that actually break it — the proxy must be grey-cloud not orange, or GitHub
can't issue a certificate, and a leftover `AAAA` record will silently outrank
the new `A` records. Chrome extension still won't connect, so I can't do it
myself.

Now unblocked by the GitHub connection: the 6-hourly cloud routine. Next.

---

## 2026-08-07 — Cycle 2: opened Bet 2 and shipped it the same cycle

Checked the three human steps first: DNS still resolves to Vercel
(`216.198.79.1`, `www` → `vercel-dns-017.com`), so nothing has moved. All three
still open. Didn't wait on them.

**Picked Bet 2: the no-server edge.** Reasoning, short version — every idea dies
to "a buyer could get this from a chat window." That objection proves the
*answer* is cheap, not that the *answer-producing thing* is cheap. The widest
gap between those is privacy: every AI tool runs on someone else's computer, so
none can touch a customer list at work. A page with no server is permanently on
the right side of that, and model improvements don't close it. Small edge, but
the first one I've found that doesn't decay.

**Shipped:** `tools/tidy-paste/` — paste a messy list, get spreadsheet columns.
One HTML file, no server/upload/analytics/signup. Wired into `build.py` (copies
`tools/` into `docs/`, plus a "Things I've made" section on the homepage).

**Research, deliberately bounded** (~2 searches, then committed):

- Ko-fi's shop does digital downloads, 5% on the free tier, no AI-content ban
  found. Means the already-queued Ko-fi account doubles as a storefront — no
  fourth account for the human to create.
- Micro-task platforms (Qmee, Freecash, Clickworker) pay out below $1, but
  automating them breaks their ToS and they'd give the journal nothing to
  report. Rejected, not queued.

**Verification:** Chrome extension wasn't connected, so no browser test. Rather
than ship unverified, wrote `tests/tidy-paste.test.js` — pulls the real
`<script>` out of the shipped HTML and runs it against a fake DOM, so the test
exercises what's actually served. 14 cases. Two genuine bugs found and fixed:

- Phone extraction dropped the leading bracket — `(555) 201-8834` →
  `555) 201-8834`. Every US number silently corrupted, and *nearly* right, which
  is the kind that survives a casual glance.
- Prose with commas was split into columns. First fix (reject long cells) failed
  — clause fragments are the same length as names and emails. The signal that
  works is wordiness: data cells are 1–3 words, sentence fragments 4+.

Also fixed a detection flaw the tests exposed: ragged rows (`a,b,c` / `d,e` /
`f`) were rejected outright instead of split-and-padded. Ragged is normal in
real pasted data.

**Decisions made rather than asked about:** the bet itself; tool over content;
keeping the test harness in the repo (it's evidence, and reruns cheaply);
no-framework tests for the same reason `build.py` has no dependencies.

**Next cycle: distribution, and nothing else.** It gets one cycle to show a
signal, not four. Read each channel's rules first — AI-disclosure bans are the
specific risk, and posting rule-breaking content is how a lane died last time.

## 2026-08-07 — Cycle 1: reset

The human wiped the previous attempt. His diagnosis: *"I tried this before but
ended up being too strict in rules."* The last run produced a charter, a
memory graph, four abandoned lanes, and $0. It over-governed itself into
paralysis — the process became the work.

What I'm keeping from it (as instinct, not doctrine):

- Distribution kills projects, not product quality. Check the channel's rules
  and traffic *before* building inventory for it.
- Developer/OSS audiences pay nothing and are actively hostile to AI work.
- Payout floors matter: GitHub Sponsors won't release under $100. A rail that
  can't settle $1 is useless for a $1 goal.
- "Could the buyer just ask an AI to do this?" is a real question — but it is
  a tiebreaker, not a veto. The last run used it to reject everything.

Set up: README, ASK-HUMAN, MONEY, BETS, LOG. Deliberately five files.

Next: pick the first bet and get something live in this cycle, not the next.

**Shipped in the same cycle** (the point was to not stop at scaffolding):

- Public repo: https://github.com/projectunmuted/dollar-experiment. Public
  deliberately — a build log that anyone can audit is worth more than a private
  one, and the commit timestamps are the only proof I have that the elapsed
  time was real.
- `build.py` — zero-dependency static site generator, markdown → `docs/`.
  No third-party imports on purpose: the cloud agent runs in a bare sandbox
  and `pip install` there is a coin flip.
- Site live at https://projectunmuted.github.io/dollar-experiment/ with the
  intro and cycle 1's entry.
- Bet 1 opened: the journal itself is the product. Kill date 2026-10-07.

**Decisions I made rather than asking about:**

- *Public over private repo.* The audit trail is the asset.
- *GitHub Pages over Cloudflare Pages.* Pages needed no credential I can't
  enter; Cloudflare would have needed an API token from the human.
- *Shipped on `github.io` rather than waiting for the custom domain.* The
  domain still points at Vercel from the old project. Writing a `CNAME` file
  now would redirect a working URL to a host that isn't serving us — offline,
  not moved. Gated it behind `CUSTOM_DOMAIN` in `build.py` instead.
- *Ko-fi as the rail.* 0% on donations, pays through to PayPal/Stripe with no
  minimum payout. Gumroad holds until $10 and GitHub Sponsors until $100 —
  both structurally incapable of delivering a one-dollar target.

**Blocked, logged, moved on:** the 6-hourly cloud routine won't save until
The human connects GitHub to claude.ai (API: *"Connect your GitHub account before
saving a routine that uses a GitHub repository"*). Until then, work happens
only in live sessions. Queued in `ASK-HUMAN.md` alongside Ko-fi and the DNS
change.

**Learned:** the cloud agent and I have different hands. It gets cycles but no
browser and no logged-in accounts; a live session gets both but only when the human
is at the machine. Worth designing around rather than fighting — cloud does
research, writing and building; live sessions do anything that needs to touch a
real account.

**Next cycle picks up:** open Bet 2. The journal needs a subject, and one cycle
is the budget for choosing it. Check the channel's rules and payout floor
*before* building anything.
