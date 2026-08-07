# Things only Stan can do

Newest at top. I add items here and keep working on something else — I don't
stall waiting.

---

## Open

*Nothing. Every remaining blocker is mine.*

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
