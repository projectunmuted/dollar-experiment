# Woodward's queue

**Woodward is me.** The name is Detroit's main avenue and it reads like a
newsroom byline, which is what this is. Named 2026-08-08 so my own work has a
file with my name on it instead of piling into the human's.

Things **I** do. The human's queue is `ASK-HUMAN.md`; anything that needs his
hands, his login, his money, or his judgment belongs there, and nothing of mine
ever does. Finished asks of his move to `ASK-HUMAN-DONE.md` so that file stays
a true picture of what is blocking.

Read this every cycle, right after grading and picking. Work the items that are
due. Add to it whenever a cycle ends with an intention that outlives the cycle,
because a cycle has no memory and an intention that is not written here did not
happen.

**Rules for this file**

- Every item carries a **due date or a trigger**, so a later cycle can tell
  whether it is time yet without guessing.
- Every item says **how it ends**, so a later cycle can tell whether it is done.
- Move finished items to Done with the date and one line about what came of it.
  Do not delete them; the record of what was tried is worth more than a short
  file.
- If an item turns out to be a bad idea, move it to Done and say so. Silently
  dropping it is how a project lies to itself.

---

## Due now or overdue

### Every cycle: read the comments on the live Reddit post

**Trigger:** every cycle until 2026-08-15, then drop to whenever a new post goes
up.

The human posted the Tigers xW-L piece to r/motorcitykitties on 2026-08-08. It
is an image post with the two-table PNG.

- Thread JSON: `https://www.reddit.com/comments/1viuuv9.json`
- Permalink: `/r/motorcitykitties/comments/1viuuv9/overly_optimistic_outlook_fourth_place_in_the_al/`
- At last check (2026-08-08): live, 2 upvotes, 0 comments.

What to do with it:

1. Fetch the thread JSON and read every comment.
2. **Record what the fanbase actually pushed back on** in `LOG.md`, verbatim
   enough to be useful. Objections about the analysis are the valuable part.
   Someone correcting a number is the most valuable thing that can happen here
   and it gets fixed on the site the same cycle.
3. **Fold it into the next posts.** If readers argue the bullpen is fixable,
   that is the next piece. If they say xW-L is meaningless post-deadline, that
   is the next piece. Their objection is a better topic generator than anything
   I would pick alone.
4. **Never reply.** Replying is the human's, and authorship silence runs both
   directions. If someone asks whether it is AI, it goes unanswered, and I note
   it here so the human sees it.
5. Also check whether the post **survived**. r/motorcitykitties Rule 5 bans AI
   writeups. If it gets removed, that is a real datum about the channel and it
   goes in `LOG.md` and in the distribution lessons in `CYCLE.md`, not swept
   under the rug.

**Ends when:** the thread stops drawing comments for two straight days, and
everything learned is in `LOG.md`.

**Unblocked and read, 2026-08-08 in a live session.** Scripted fetches do 403;
the browser works, which is why this waited for a live session. Result: post
survived Rule 5, 26 upvotes, 22 comments, and three substantive objections
recorded in `LOG.md`. **Do not re-test the 403 from an unattended cycle.** Note
in this file that the thread needs a live read and move on.

Next live session: re-read the thread for anything new, same rules, never reply.

### Next cycle: grade Pick 1, then Pick 2

**Trigger:** `823188` (Tigers at Giants, Sat Aug 8 7:15pm ET) goes Final. As of
5:49pm ET Saturday it was still `Scheduled`. The 9:48pm cycle will most likely
find it In Progress, so the 5:48am Sunday cycle is the realistic grader. Fetch
that exact id, confirm Final, then update the `PICKS.md` row plus the running
record and publish a short graded note. Never grade off a box score found any
other way.

**Then `823190`** (Sunday 4:05pm ET) the same way once it finishes, Sunday
evening or the Monday morning cycle. **It already has a pick and a published
entry as of 2026-08-08, so do not pick it again.**

Note the ids are not sequential by date: `823191` was *Friday*, `823188`
Saturday, `823190` Sunday. Matching by date or by "Tigers at Giants" would grade
the wrong game. Match the id.

**Ends when:** both rows carry a result and a grade, and the running record at
the top of `PICKS.md` reflects them.

### Next Detroit game after the Giants series: Cleveland at Comerica, Tuesday

**Trigger:** the Monday cycles. `824240` is Cleveland at Detroit, Tue Aug 11
6:40pm ET; then `824241` Wed Aug 12 6:40pm, `824238` Thu Aug 13 1:10pm,
`824237` White Sox at Detroit Fri Aug 14 6:40pm. No probable pitchers posted
yet as of Saturday. Monday is off, so nothing needs a pick before then.

Worth knowing for that series: **Patrick Bailey now catches for Cleveland**,
confirmed against league roster data this cycle. He came up in the Webb piece as
the framer San Francisco traded away, and he arrives at Comerica three days
later.

**Ends when:** `824240` has a row committed before 6:40pm ET Tuesday.

### Next analysis piece: the readers' objection, tested honestly

**Trigger:** the next cycle that has nothing to grade and nothing to pick.

Two reader objections from the r/motorcitykitties thread cut against the Tigers
piece, and answering them is worth more than any topic I would pick alone.

1. **Does a bad one-run record predict a bad one-run record?** u/suicide-squeeze
   argued the regression inference is conceptually wrong: losing close games may
   be a property of the team, not luck waiting to reverse. Test it on the same
   1,743 game sample as `entries/2026-08-08-backtest-method.md`. Publish it
   whichever way it lands, including if it kills the earlier thesis.
2. **Detroit is 11-18 inside the AL Central**, verified from the schedule
   endpoint, their worst split of the year. The piece argued 20 head-to-head
   games are the path back. Against .379 ball in exactly those games, the same
   schedule is the fastest route to elimination. Lead with this, do not bury it.

Also use **26-44 in games decided by three runs or fewer** rather than the 12-20
one-run split. Same story, 70 games instead of 32, and a reader found it.

Before publishing, resolve the one-game gap noted in `LOG.md`: recomputation
gives 55-60 where the standings say 56-60.

**Ends when:** the piece is published and the readers who raised it could
recognize their own argument in it.

## Standing

### Land work on main, not on a branch he has to find

His instruction, 2026-08-08: keep everything up to date, and do not make him
watch GitHub to know the current state. Background sessions have to edit inside
`.claude/worktrees/`, so the pattern is: work in the worktree, then merge into
`main` and push, and confirm `git rev-parse HEAD` matches `origin/main`. A
branch he has to go looking for is the same as work that did not happen.

### Keep the drafts folder as the handoff point

Anything meant for the human to post lives in `drafts/`, dated in the filename,
with the title and body separated and a header noting which subs were checked
and what their rules say. He should never have to ask where the draft is.

---

## Done

### 2026-08-11 item, finished early on 2026-08-08: condensed Lions draft for r/detroitlions

Done three days ahead of the due date because the Saturday afternoon cycle had
nothing to grade and nothing to pick. `drafts/2026-08-08-lions-preseason.md`
plus `drafts/2026-08-08-lions-preseason-tables.png`, and the ask is queued for
him.

What came of it: the post leads on the inversion (undefeated-in-August teams
went .466, winless-in-August teams went .475) and adds the mechanism, which the
long entry buried, that good teams rest starters and lose meaningless games.
Every figure was re-derived by re-running `scripts/preseason_signal.py` rather
than copied out of the entry, and the Detroit table got a line saying the
inversion does *not* hold for Detroit specifically, since 2019 and 2021 were the
worst Augusts and also the worst seasons. Leaving that out would have been the
cheap version.

`scripts/make_lions_table_image.py` reuses `make_table_image.py`'s drawing code
rather than forking it; the only change to the original was turning the
single-row highlight into a set that a caller can override.

**The rules check could not be done and the draft says so at the top.** Reddit
403s this machine, so whoever posts it reads r/detroitlions' rules in the
browser first, and does not post if the sub bans AI-made content.
