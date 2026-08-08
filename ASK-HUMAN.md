# Things only the human can do

Newest at top. I add items here and keep working on something else — I don't
stall waiting.

---

## Open

### Log this Chrome profile into Ko-fi (~1 minute) and Proton (~1 minute)

The single highest-value thing left, and it is two logins.

**Ko-fi.** Confirmed 2026-08-08 that a real browser loads ko-fi.com fine; the
403s all week were bot-detection against curl, not a wall. So with a session
in this profile I can finally **see whether anyone has tipped**, which is the
one number that defines this project and the one I am currently blind to.
I could also fix the page: it is still Ko-fi's default placeholder ("Welcome
to my page! If you enjoy what I do...") with **no Detroit branding and a $5
default tip** on a project whose goal is one dollar.

**Proton** (projectunmuted@proton.me). Ko-fi tip notifications, Search Console
alerts and any replies land in email. Without a session I only learn things by
polling.

### Buy nothing else, and keep these three things human

Recorded so no future cycle asks: I do not want typed passwords, card numbers
or API keys, spend approval stays yours, and Reddit posting stays a live
session with your go-ahead. That last one protects **your** 2019 account with
5,480 karma from an automated misstep that could get it shadowbanned.

### Hacker News — parked, revisit in a few weeks

`projectunmuted` exists but HN gates Show HNs from new accounts. The journal
gets its shot once the account has history. Reading and commenting yourself,
when you genuinely feel like it, is the only legitimate accelerant.

## Done

### 2026-08-08 — detroitsportsreporter.com live, repo renamed to newsroom

Domain flipped, HTTPS enforced, own IndexNow key. Source repo renamed
dollar-experiment -> newsroom so the proof link stopped announcing the
framing we removed from the page; old URL 301s, Pages and Search Console
both survived. Note: the rename silently broke Pages' auto-build trigger
(status said "built" at a stale commit), fixed with a forced rebuild.

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
