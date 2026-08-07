# Things only Stan can do

Newest at top. I add items here and keep working on something else — I don't
stall waiting.

---

## Open

### Submit Tidy Paste to `pluja/awesome-privacy` (~2 minutes, needs your GitHub login)

Tried to do this myself this cycle — the cloud session's GitHub access is
locked to this one repo (`projectunmuted/dollar-experiment`) and can't fork or
open a PR against a different owner's repo (tried; got "cross-tier adds are
not supported"). That's a tooling limit, not a login/password one, so it's
yours by elimination rather than by rule.

`pluja/awesome-privacy` (13k+ stars) is a curated list of privacy-respecting
tools/services. Checked its contribution rules first (learned that lesson from
Low Water): open-source preferred, no tracking, one-line format, no stated ban
on AI-made tools. It has a `## Utilities` section that fits Tidy Paste exactly.

Steps:
1. Go to https://github.com/pluja/awesome-privacy/edit/main/README.md (this
   forks it and opens the file for editing in one click if you're logged in).
2. Find the `## Utilities` section and add, in alphabetical order:
   `- [Tidy Paste](https://project-unmuted.com/tools/tidy-paste/) - Free, open-source, in-browser tool that turns a messy pasted list (names, emails, phone numbers) into clean spreadsheet columns. No server, no upload, no signup — nothing you paste ever leaves the browser.`
3. Commit straight to a new branch, then click "Create pull request." Default
   title/description are fine.

If it gets rejected or ignored, that's useful data either way — note the
outcome (or lack of one) back in `LOG.md` next time you're at the machine, or
I'll check the PR status next cycle if GitHub gives cross-repo access by then.

One standing item, for whenever you happen to be at the machine: the **Chrome
extension won't connect** (`tabs_context_mcp` reports "Browser extension is not
connected"). Not blocking anything today — I worked around it by testing the
tool headlessly — but it's the difference between me being able to check a page
renders and having to ask you to look. Worth a Chrome restart at some point.

## Done

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
