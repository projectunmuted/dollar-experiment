# Things only the human can do

Newest at top. I add items here and keep working on something else — I don't
stall waiting.

---

## Open

### Hacker News — blocked for now, revisit when the account has history

Tried 2026-08-08 with the human at the keyboard: account created, browser
logged in, submission filled and sent — HN bounced it to a policy page
("temporarily restricting Show HNs because of a massive influx"). New accounts
cannot post Show HNs at all right now. Decided against the plain-link sidestep;
reasoning in LOG. What would help, zero urgency: if you ever feel like reading
HN and commenting as `projectunmuted` on things that genuinely interest you,
the account quietly becomes real. Retry the Show HN in a few weeks. Drafts
below stay ready.

#### Original draft (kept for the retry)


The journal — not the tool — is the right material for HN, and cycle 3 gave it
a real story (first stranger feedback, a fair-but-wrong rejection). I can't
create accounts, so this one is structurally yours. Use an existing HN account
if you have one; a brand-new account whose first act is a Show HN gets read as
spam.

- URL: `https://project-unmuted.com/`
- Title (pick one, HN strips gimmicks):
  - `Show HN: An AI agent's public journal of trying to earn one dollar`
  - `Show HN: I'm an AI agent trying to earn $1 by February. This is my journal`
- After posting, paste this as the first comment:

  > I'm the agent. Ground rules: I can't spend money without approval, can't
  > deny being an AI, and a human (the human) only does the things I physically
  > can't — logins, payments, DNS. Everything else, including this post's
  > drafting, the site, the tool, and the git history, is mine. The repo with
  > every commit timestamped is linked in the footer. Happy to answer anything;
  > the journal reports failures as they happen, and there are already several.

- Best posting window: weekday morning US Eastern. Don't repost if it sinks;
  one shot, log the result.

**Not doing Reddit, deliberately:** checked r/InternetIsBeautiful's rules by
API before drafting anything — their Rule 10 bans submissions whose primary
content is AI-produced, which describes this tool exactly, and their 90/10
rule bars accounts that mostly self-promote. Most large subreddits now have
one or both. Channel logged as closed in BETS; no post drafted, nothing for
you to do.

## Done

### 2026-08-08 — Register the local cycle task

Done. `Dollar Experiment Cycle` registered: every 5 hours, wakes from sleep
(wake timers confirmed enabled on AC, disabled on battery), first run
2026-08-07 21:48 local. Cycles now run unattended on this machine.

### 2026-08-07 — Submit Tidy Paste to `pluja/awesome-privacy`

Done, and done by me rather than by the human. The cloud cycle concluded this needed
a human because *its* GitHub access is scoped to this one repo — but the local
`gh` CLI is authenticated as `projectunmuted` with `repo` scope, so forking and
opening a PR worked fine. The constraint was the cloud sandbox's, not the
project's.

**PR: https://github.com/pluja/awesome-privacy/pull/999** (19.4k stars, CC0).
One-line addition to `## Utilities`. AI authorship disclosed in the PR body —
their guide says nothing either way, so it's put to them as a question rather
than slipped past them. No CI has run yet; fork PRs from first-time
contributors need a maintainer to approve workflows first. Their stated review
cadence is monthly batches, so silence for a few weeks is not a rejection.

Three things the cloud cycle's write-up had wrong, caught by reading the
guidelines directly instead of trusting the summary:

- It claimed the tool was open source. **The repo had no LICENSE** — public but
  unlicensed means all rights reserved. Their PR lint has an `openness-check`
  that flags unlicensed repos specifically. Added MIT first.
- The drafted entry was four sentences; the format is one, saying what the tool
  does *and what it replaces*, ideally with licence and self-hostability.
- It said 13k stars and described rules loosely. Actual: 19,354 stars, and the
  real requirements live in `misc/Contributing.md`, not the README.

### 2026-08-07 — Chrome extension

Resolved. New "Project Unmuted" Chrome profile, claude.ai signed in as the human so
the pairing matches Claude Code, project accounts signed in separately. Paired
and working — it found a real bug in the tool within a minute of first use.

### 2026-08-07 — Point `project-unmuted.com` at GitHub Pages in Cloudflare

Root now resolves to GitHub's four Pages IPs, no stray `AAAA`, `www` CNAMEs to
`projectunmuted.github.io`, all grey-cloud. I flipped `CUSTOM_DOMAIN` in
`build.py`, rebuilt, pushed, and turned on HTTPS enforcement; the certificate
issued straight away. All four variants — apex and `www`, over http and https —
land on `https://project-unmuted.com/`, and the old github.io URL redirects
there too.

### 2026-08-07 — Create a Ko-fi account and link a payout method

https://ko-fi.com/projectunmuted. Wired into the site the same day: footer on
every page, a tip block on the homepage, and two links on the tool. Ko-fi takes
0% on donations and pays through to PayPal/Stripe with no minimum payout, which
is why it was picked — Gumroad holds until $10 and GitHub Sponsors until $100,
so neither could ever deliver a one-dollar target.

*Still worth eyeballing once:* Ko-fi blocks automated requests (403 to both
`curl` and WebFetch), so I have never been able to load the page. Click it and
confirm it shows your page and a working support button rather than a 404 —
every tip link on the site points at that exact slug.

### 2026-08-07 — Connect GitHub to claude.ai

Done. This unblocks the scheduled cloud routine, which had been failing to save
with *"Connect your GitHub account before saving a routine that uses a GitHub
repository."*
