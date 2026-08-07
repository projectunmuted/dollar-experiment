# Things only Stan can do

Newest at top. I add items here and keep working on something else — I don't
stall waiting. Strike through when done.

---

## Open

- [x] ~~**2026-08-07 — Connect your GitHub account at https://claude.ai/settings
  (or the prompt at https://claude.ai/code/routines).** — The 6-hourly cloud
  routine can't be saved until claude.ai can see the repo it's supposed to
  work in. API returned: *"Connect your GitHub account before saving a routine
  that uses a GitHub repository."* Until this is done, work only happens in
  live sessions with you. — **~30 seconds, one OAuth click.**~~ **Done
  2026-08-07.** The cloud routine can be set up now.

- [x] **2026-08-07 — Create a Ko-fi account and link a payout method.** —
  **Done 2026-08-07:** https://ko-fi.com/projectunmuted. Wired into the site the
  same day — footer on every page, a tip block on the homepage, and a link on the
  tool itself. Ko-fi takes 0% on donations and pays through to PayPal/Stripe with
  no minimum payout, which is why it was picked: Gumroad holds until $10 and
  GitHub Sponsors until $100, so neither could ever deliver a one-dollar target.
  There is now, for the first time, a way for the experiment to actually receive
  money.

  *One thing to check when you have a second:* Ko-fi blocks automated requests,
  so I can't load the page to confirm it renders. Click the link once and make
  sure it shows your page and a working support button rather than a 404.

- [ ] **2026-08-07 — Point `project-unmuted.com` at GitHub Pages in
  Cloudflare.** — The domain still resolves to Vercel from the abandoned
  project (`216.198.79.1`, and `www` CNAMEs to `vercel-dns-017.com`). The site
  is live and readable right now at
  https://projectunmuted.github.io/dollar-experiment/ — this just moves it to
  the real domain. In Cloudflare DNS, delete the existing `A` record for the
  root and the `www` CNAME, then add, all with the **proxy turned off**
  (grey cloud, not orange — Cloudflare's proxy breaks GitHub's certificate
  issuance):

  | Type | Name | Value |
  |---|---|---|
  | A | @ | 185.199.108.153 |
  | A | @ | 185.199.109.153 |
  | A | @ | 185.199.110.153 |
  | A | @ | 185.199.111.153 |
  | CNAME | www | projectunmuted.github.io |

  Tell me when it's done and I'll flip `CUSTOM_DOMAIN` in `build.py`, rebuild,
  and turn on HTTPS. — **~5 minutes.**

## Done

*(nothing yet)*
