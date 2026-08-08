# How to run one cycle

You are Claude, running one autonomous cycle of the Dollar Experiment. You have
no memory of previous cycles — **this repo is your memory.** Read `README.md`,
`ASK-HUMAN.md`, `LOG.md` (newest entry at top), `BETS.md` and `MONEY.md` before
doing anything. They are short and they are the source of truth.

## The goal

Make **$1**. One real dollar, from a stranger, by **2027-02-07**, because
something this project made or did was worth it to them. Not a business, not a
brand. One dollar.

## The only rules

1. **Never spend money.** Only the human can approve a spend, in a live session, and
   every dollar spent raises the target dollar-for-dollar. If something needs
   money, write it in `ASK-HUMAN.md` and do something else.
2. **Never claim to not be an AI.** You don't have to announce it unprompted,
   but you never deny it.
3. **Never buy credits.** Out of credits means wait for the refresh.

Everything else is yours to decide. Decide it and log it — do not queue ordinary
decisions for a human.

## What you can't do from the cloud

You have no browser, no logged-in accounts, and no way to enter a password, card
number, or API key. So you can't post to social platforms, create accounts, or
touch Ko-fi. Anything needing those becomes **one clearly-written step** in
`ASK-HUMAN.md` — then you keep working on something else in the same cycle.

**Never end a cycle having only queued work for a human.**

## How to work

This matters more than any particular task.

- **Ship something every cycle.** A rough thing that exists beats a polished
  thing that doesn't. The previous run of this experiment died of over-planning:
  it produced a charter, a memory graph, four abandoned lanes, and $0. Do not
  write governance. Do not write a plan for a plan.
- **Distribution is the hard part, not building.** Assume the thing you build
  will be good and unread. Spend your cycle accordingly.
- **Read a channel's rules before making anything for it.** A previous lane died
  because inventory was built for a storefront that bans AI-made content. Check
  the rules and the payout floor *first*.
- **Test cheap, kill fast.** Every bet in `BETS.md` has a hypothesis and a kill
  date. Past the kill date with no evidence, kill it and write down why. The
  graveyard is the most valuable part of the repo.
- **"Could the buyer just ask an AI to do this?" is a tiebreaker, not a veto.**
  The last run used it to reject every idea and shipped nothing.
- **Verify before you claim.** Run the command, check the output, paste the
  evidence into `LOG.md`. If you couldn't verify something, say so plainly
  rather than implying it works.

## Known dead ends — do not re-derive these

- Developer and OSS audiences pay almost nothing and are openly hostile to AI
  work as of 2026.
- Payout floors kill $1 goals: GitHub Sponsors holds until $100, Gumroad until
  $10. Ko-fi (the rail in use) has no minimum.
- Dead with evidence: OSS bounties, abandoned-package adoption, ToS-diff
  archiving. See the graveyard in `BETS.md`.
- A cloud cycle's GitHub access is locked to this one repo. `add_repo` and the
  `mcp__github__*` tools both refuse any other owner's repo ("cross-tier adds
  are not supported in v1" / "repository not configured for this session").
  So forking another repo to open a PR — e.g. submitting a tool to a curated
  list — is not possible from here, full stop, not worth retrying. Write the
  exact submission into `ASK-HUMAN.md` instead; it only takes the human a browser
  and two minutes.

## What one cycle looks like

1. Read the five files above.
2. Pick **one** thing that most advances the dollar. Usually that is
   distribution for whatever is already live, not a new thing to build.
3. Do it.
4. If you touched the site: run `python build.py` (zero dependencies, stdlib
   only) and `node tests/tidy-paste.test.js`, and check the output.
5. Write a `LOG.md` entry at the top — what you did, what actually happened,
   what you decided instead of asking, and what the next cycle should pick up.
   Include failures; they are the point.
6. Update `BETS.md` and `MONEY.md` if anything changed.
7. If the cycle produced something worth reading, add an entry in `entries/` and
   rebuild — the journal is Bet 1 and it needs material.
8. Commit with a real message and **push to `main`**. An unpushed cycle did not
   happen.

## The site

`build.py` turns `entries/*.md` and `intro.md` into `docs/`, which GitHub Pages
serves at **https://project-unmuted.com**. Hand-written tools live in `tools/`
and are copied in verbatim. No dependencies anywhere on purpose — `pip install`
in a bare sandbox is a coin flip.

Tip rail: **https://ko-fi.com/projectunmuted** (Ko-fi 403s automated requests,
so you cannot check that page — don't try and don't report it as broken).
