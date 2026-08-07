# Things only Stan can do

Newest at top. I add items here and keep working on something else — I don't
stall waiting. Strike through when done.

---

## Open

- [ ] **2026-08-07 — Connect your GitHub account at https://claude.ai/settings
  (or the prompt at https://claude.ai/code/routines).** — The 6-hourly cloud
  routine can't be saved until claude.ai can see the repo it's supposed to
  work in. API returned: *"Connect your GitHub account before saving a routine
  that uses a GitHub repository."* Until this is done, work only happens in
  live sessions with you. — **~30 seconds, one OAuth click.**

- [ ] **2026-08-07 — Create a Ko-fi account and link a payout method.**
  **&larr; this is now the one that matters most.** As of cycle 2 there is a
  working free tool and two journal entries, so there is finally something worth
  tipping for — and no way whatsoever to tip. Until this exists, the project
  cannot receive money even if someone wants to give it. Ko-fi's shop also does
  digital downloads at 5% on the free tier, so this same account covers selling
  something later; no second account needed. — This
  is the rail the dollar actually arrives on. Ko-fi takes 0% on donations and
  pays straight through to PayPal or Stripe with **no minimum payout
  threshold**, which is the whole reason I picked it — Gumroad holds until $10
  and GitHub Sponsors until $100, so neither can ever deliver a single dollar.
  Use `projectunmuted@proton.me`. I can't do this myself: it needs email
  verification and then payment credentials, both of which I'm not able to
  enter. Once the account exists, tell me the page URL and I'll do the rest of
  the setup and wire it into everything. — **~5 minutes.**

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
