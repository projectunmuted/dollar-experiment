# Things only the human can do

Newest at top. I add items here and keep working on something else — I don't
stall waiting.

---

## Open

### Buy detroitsportsreporter.com and point it at GitHub Pages (~$10/yr + 3 minutes)

You picked it 2026-08-08 (and detroitsportsreporter@proton.me to match; both
confirmed available). The site is already built and live at
https://projectunmuted.github.io/detroitsportsreporter/ so this just gives it
its real name:

1. Buy `detroitsportsreporter.com` at Cloudflare Registrar (at-cost; DNS
   lands next to the other domain automatically).
2. Create the Proton address `detroitsportsreporter@proton.me` if you want
   the matching email (optional, no urgency).
3. In Cloudflare DNS for the new domain, add — all **grey cloud / DNS
   only** (orange breaks GitHub's certificate):

   | Type | Name | Value |
   |---|---|---|
   | A | @ | 185.199.108.153 |
   | A | @ | 185.199.109.153 |
   | A | @ | 185.199.110.153 |
   | A | @ | 185.199.111.153 |
   | CNAME | www | projectunmuted.github.io |

4. Tell me. I flip `DSR.custom_domain` in build.py, republish, set the
   domain on the deploy repo, and enforce HTTPS — same playbook that moved
   project-unmuted.com, which took minutes.

### Log the Project Unmuted Chrome profile into your sports Reddit account (~1 minute)

You offered the account on 2026-08-08 (real sports-posting history, nothing
tying it to you personally). For me to drive it in live sessions, the session
has to exist in the **Project Unmuted** Chrome profile: open reddit.com
there, log in, stay logged in. No urgency — nothing gets posted except in a
live session with your go-ahead, after checking the target subreddit's rules.

### Add the site to Google Search Console (~2 minutes) — carried from attempt 2

Still the highest-leverage two minutes available; search is the one channel
with no authorship gatekeeper, and the new Detroit content will live or die
by it. Steps: https://search.google.com/search-console → Add property →
Domain → `project-unmuted.com` → copy the TXT record into Cloudflare DNS →
Verify → tell me. I'll submit the sitemap and track indexing.

### Hacker News — parked, revisit in a few weeks

`projectunmuted` exists but HN gates Show HNs from new accounts. The journal
(now with the Detroit arc) gets its shot once the account has some history.
Reading and commenting there as yourself, when you genuinely feel like it, is
the only legitimate accelerant.

## Done

### 2026-08-08 — Attempt 2 closeout

All three tool submissions closed politely; see LOG. Ko-fi, domain, HN
account, scheduled task, Chrome profile all carried into attempt 3.
