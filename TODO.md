# My queue

Things **I** do. The human's queue is `ASK-HUMAN.md`; anything that needs his
hands, his login, or his money belongs there, not here.

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

### By Tuesday 2026-08-11: condensed Lions draft ready for r/lions

**Trigger:** due end of the Tuesday cycles. The human posts it Wednesday
2026-08-12 or Thursday 2026-08-13. Thursday is the preseason opener at
Cincinnati, 7:00pm ET, so a Thursday post lands the same day as the game.

Source: `entries/2026-08-08-preseason-means-nothing.md`, the eleven-year
preseason backtest. The human likes it and wants a short version.

- Condense the way the Tigers post was condensed: the finding, the number, the
  point. Preseason record explains about one percent of the regular season, and
  the teams that went undefeated in August did worse than the teams that went
  winless. That inversion is the whole post.
- Consider the table-as-image treatment again; it worked
  (`make_table_image.py` pattern, drafts folder).
- **Do not post it.** Leave it in `drafts/` and tell the human it is ready.
- **Check r/lions rules in the session where it gets posted, not from memory.**
  r/motorcitykitties, r/baseball and r/mlb all ban AI-written posts; r/lions has
  not been checked yet. If it bans them too, say so plainly and name the subs
  that do not.
- No em dashes, no percentages as confidence, no link to the site.

**Ends when:** a dated draft file exists in `drafts/` and the human has been
told.

## Standing

### Keep the drafts folder as the handoff point

Anything meant for the human to post lives in `drafts/`, dated in the filename,
with the title and body separated and a header noting which subs were checked
and what their rules say. He should never have to ask where the draft is.

---

## Done

*(nothing yet; first items above were created 2026-08-08)*
