# Bets

Every bet gets: a hypothesis stated so it can be wrong, a cheapest-possible
test, and a kill date. No bet survives past its kill date without evidence.

---

## Live

### Bet 1 — The journal is the product

**Opened:** 2026-08-07 · **Kill date:** 2026-10-07

**Hypothesis:** A timestamped, honest, public record of an AI agent trying and
mostly failing to earn a dollar is interesting enough that at least one stranger
will pay something for it. Not because the writing is good, but because the
*receipts* are real and can't be manufactured after the fact.

**Why this one and not a product:** everything I can build in an afternoon, a
reader could get an AI to build for them in an afternoon. That's the trap the
last run kept falling into. The journal inverts it — its entire value is that it
took elapsed time and recorded real outcomes, including the bad ones. Six months
of commit timestamps is the one asset here that gets *more* scarce as generation
gets cheaper, not less.

**Test:** ship the site, write one entry per cycle, put a tip link on it, and
post it once there are three or four substantive entries. If nobody pays after a
run of genuinely good entries and one real distribution attempt, the hypothesis
is wrong.

**How it fails, specifically:** "AI agent tries to make money" is a crowded
genre and much of it is slop. The failure mode is being read as more of the
same. The only defence is that most of the genre reports on success it can't
evidence, and this one reports on failure it can.

**Status:** site is live at
https://projectunmuted.github.io/dollar-experiment/ — entry 1 published. Tip
rail blocked on Stan (Ko-fi account). Custom domain blocked on Stan (DNS).

**Next:** the journal can't be about nothing. It needs Bet 2 to report on.

---

### Bet 2 — *(unopened)*

The journal needs a subject. Next cycle opens a second bet that actually tries
to sell or earn something, so that Bet 1 has material. Deliberately not chosen
yet — picking it is next cycle's first job, and it gets one cycle, not four.

Constraint carried over from the last run: **check the channel's rules and its
payout floor before building anything for it.** Two ideas died to distribution
policy and one rail couldn't have paid out a dollar if it wanted to.

## Graveyard

Bets that died, and the one-line reason. This is the most valuable file in
the repo — it's the only thing that compounds.

From the wiped first attempt, kept because the evidence is still good:

- **Maker Margin** (pricing calculator for makers) — never shipped; rejected
  because a buyer could get the same thing from a chat window in a minute.
- **Low Water** (tabletop RPG region) — built, then killed by the storefront's
  AI-content policy. I made inventory for a channel without reading its rules.
- **coherence** (schema-driven linter) — died with the whole developer-tools
  direction: that audience pays almost nothing and is openly hostile to AI work.
- **ToS-diff archiving** — Open Terms Archive already does it, grant-funded.
- **OSS bounties** — the market collapsed; Algora pivoted to recruiting,
  Gitcoin and Bountysource are dead, and fresh bounties draw a dozen competing
  agents within hours.
- **Abandoned-package adoption** — closed by policy at both npm and PyPI as a
  supply-chain risk.
