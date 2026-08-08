# Things only the human can do

Newest at top. I add items here and keep working on something else — I don't
stall waiting.

---

## Open

### Buy detroitsportsreporter.com and point it at GitHub Pages (~$10/yr + 3 minutes)

You picked the name 2026-08-08 (with detroitsportsreporter@proton.me to
match). The site is already built and live at
https://projectunmuted.github.io/detroitsportsreporter/ so this just gives it
its real name:

1. Buy `detroitsportsreporter.com` at Cloudflare Registrar (at-cost; DNS
   lands next to the other domain automatically).
2. In Cloudflare DNS for the new domain, add — all **grey cloud / DNS only**
   (orange breaks GitHub's certificate):

   | Type | Name | Value |
   |---|---|---|
   | A | @ | 185.199.108.153 |
   | A | @ | 185.199.109.153 |
   | A | @ | 185.199.110.153 |
   | A | @ | 185.199.111.153 |
   | CNAME | www | projectunmuted.github.io |

3. Tell me. I flip `DSR.custom_domain` in build.py, republish, set the domain
   on the deploy repo, enforce HTTPS, and add its own Search Console property
   plus IndexNow key. Same playbook that moved project-unmuted.com, minutes.

### Hacker News — parked, revisit in a few weeks

`projectunmuted` exists but HN gates Show HNs from new accounts. The journal
(now with the Detroit arc) gets its shot once the account has history.
Reading and commenting there yourself, when you genuinely feel like it, is
the only legitimate accelerant.

## Done

### 2026-08-08 — Google Search Console verified, sitemap submitted

Done end to end from the browser, no DNS needed. Property added as **URL
prefix** rather than Domain specifically because Domain requires DNS
verification (your hands) while URL prefix allows HTML-file verification
(mine): Google names a token file, `build.py` emits it every build so it can
never silently vanish, Pages serves it, Google fetched it. Ownership
verified, `sitemap.xml` submitted and accepted. Google now crawls alongside
the IndexNow engines. This had been the top queued item for a day.

### 2026-08-08 — Browser and accounts connected

Claude extension installed in the Work profile and paired. The diagnosis that
unstuck it: Chrome extensions are per-profile, and the profile you had moved
to was the only one without it. Reddit confirmed as **u/ICantSpellorWrite**
(created 2019, 5,480 karma, verified email, no suspensions) — a genuinely
aged account, which is the one thing a new account cannot fake. Nothing
posted.

### 2026-08-08 — Attempt 2 closeout

All three tool submissions closed politely; see LOG. Ko-fi, domain, HN
account, scheduled task, Chrome profile all carried into attempt 3.
