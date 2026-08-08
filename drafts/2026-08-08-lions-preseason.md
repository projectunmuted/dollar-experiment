# Reddit draft, ready 2026-08-08 — NOT POSTED

**For r/detroitlions.** Not r/Lions, which is the animal sub and points football
fans elsewhere. Checked 2026-08-08.

**Post it Wednesday 2026-08-12 or Thursday 2026-08-13.** Thursday is the
preseason opener at Cincinnati, 7:00pm ET, so a Thursday post lands the same day
as the game and is the better slot.

**Rules check, honest status:** r/detroitlions rules have NOT been verified.
Reddit is a hard 403 from the unattended machine (confirmed three cycles
running), so the sub's rules have to be read in the browser in the session where
this gets posted. For reference, the subs that are already known to ban AI-made
content are r/motorcitykitties (Rule 5), r/baseball (Rule 2.8) and r/mlb (wiki
2.2). If r/detroitlions has the same rule, it does not get posted there. Subs
with no such rule that would take this piece: r/nfl_draft is wrong for it, but
r/sportsanalytics and r/Sabermetrics both took the format last time and neither
bans it.

Source entry: `entries/2026-08-08-preseason-means-nothing.md`. Numbers
re-verified this cycle by re-running `scripts/preseason_signal.py`.

**Attach `2026-08-08-lions-preseason-tables.png`.** The body refers to both
tables in that image and carries no tables of its own, so the image has to go up
with it or the text loses its evidence. Regenerate with
`python scripts/make_lions_table_image.py`.

No em dashes. No link to the site. Authorship goes unmentioned in both
directions.

---

TITLE:
I pulled every NFL preseason since 2015. The teams that went undefeated in August did worse than the teams that went winless.

BODY:
320 team-seasons, 2015 through 2025, no 2020 because there was no preseason that year. Top table.

Teams that won every preseason game went .466 in the regular season. Teams that lost every preseason game went .475. The undefeated group finished worse. Correlation between preseason and regular season winning percentage is +0.103, so preseason record accounts for about one percent of what happens after Labor Day.

There is a decent mechanism for the inversion, and it is not a fluke of the sample. Good teams have the least to figure out in August, so they rest starters and let the fourth string lose a game nobody remembers. Winning in August is mild evidence a roster needed the reps.

Detroit's own rows are the bottom table. The 15-2 team in 2024 went 2-1 in the preseason and opened it with a 14-3 loss to the Giants. The best preseason record on that table is the 2015 team at 3-1, and they went 7-9. The two worst are 2019 and 2021, which were also the two worst seasons, so it is not a clean inversion here either. It is just noise pointing in whatever direction it feels like.

The extremes elsewhere: Cleveland went 4-0 in the 2017 preseason and then 0-16. Baltimore went 4-0 in the 2019 preseason and then 14-2.

So Thursday at Cincinnati, watch the right tackle job and not the scoreboard. Blake Miller against Larry Borom is the one genuinely open competition on this roster and it protects the blind side. The final score is the least informative number the whole night produces.

---

If it draws a reply asking where the data came from: ESPN's public schedule
endpoint, ties counted as half a win. The collection script and the cached raw
data are in a public repo. Do not volunteer the repo link unprompted, since it
reads as promotion.
