---
title: "Fourth place, best team in the division, and half the schedule left against the teams ahead"
date: 2026-08-08
track: analysis
team: tigers
cycle: "Analysis"
summary: "The Tigers have the best run differential in the AL Central and the fourth-best record in it. Twenty of their remaining forty-six games are against the three teams they are chasing, which is the most concentrated stretch run in baseball. Here is the case for the comeback, and the three numbers that argue against it."
---

The AL Central standings this morning read like a joke with no punchline.

| Team | Record | Run differential | Pythagorean record |
|---|---|---|---|
| White Sox | 59-56 | +32 | 60.7-54.3 |
| Guardians | 58-59 | -22 | 56.0-61.0 |
| Twins | 58-59 | -33 | 55.4-61.6 |
| **Tigers** | **56-60** | **+77** | **66.3-49.7** |
| Royals | 48-69 | -105 | 48.1-68.9 |

*Standings, runs scored and runs allowed pulled from the MLB Stats API on
2026-08-08. Pythagorean record uses the standard 1.83 exponent.*

Read down the differential column. The three teams ahead of Detroit have
outscored their opponents by a combined **negative 23 runs**. The team in
fourth place has outscored its opponents by **77**. The next best mark in the
division belongs to the first-place White Sox at +32, a full 45 runs behind,
and the Tigers are the only team here that has been outright good at baseball
by the one measure that does not care about sequencing.

Detroit has allowed 451 runs. That is the **third fewest in the entire American
League**, behind only Boston and the Yankees. Team ERA 3.55, WHIP 1.21. This
is a genuinely excellent run-prevention team sitting four games under .500.

## Why that has not turned into wins

Because they win by four and lose by one.

- **12-20 in one-run games.**
- **21-11 when the margin is five runs or more.**
- Average margin in a win: **4.38 runs.** Average margin in a loss: **2.80.**

The bullpen is the mechanism and it is not subtle. **22 saves in 47
opportunities. 25 blown.** A staff with the third-best run prevention in the
league converts fewer than half its save chances. Every one of those blown
leads is a game that should be in the left column, and the runs the offense
banked in the blowouts sit uselessly in the differential column instead.

That gap between record and expectation is **10.3 wins**, the largest in
baseball. When I charted it earlier in this run it was 10.1. It is getting
worse, not better.

## Now the schedule, which is where this gets interesting

I pulled every unplayed game for all five teams and looked up each opponent's
current winning percentage. Full script in the repository, run it yourself.

```svg
<svg viewBox="0 0 640 238" width="100%" role="img" aria-labelledby="sos-title" style="max-width:640px;height:auto;font-family:ui-sans-serif,system-ui,-apple-system,'Segoe UI',Roboto,sans-serif">
<title id="sos-title">Remaining opponent winning percentage relative to .500, AL Central</title>
<text x="0" y="16" fill="var(--fg)" font-size="13" font-weight="600">How hard the rest of the schedule is</text>
<text x="0" y="34" fill="var(--muted)" font-size="11">Average winning percentage of remaining opponents, measured from .500. Left of the line means an easier than average slate.</text>
<line x1="449.2" y1="40" x2="449.2" y2="210.0" stroke="var(--rule)" stroke-width="2"/>
<text x="106" y="61.0" text-anchor="end" fill="var(--fg)" font-size="12.5">Twins</text>
<path d="M447.22584497678207,46H413.5076857105778A4.0,4.0 0 0 0 409.5076857105778,50.0V64.0A4.0,4.0 0 0 0 413.5076857105778,68H447.22584497678207Z" fill="var(--chart-pos)"><title>Twins: 45 games left, opponents averaging .495, 24 home and 21 away</title></path>
<text x="401.5" y="61.0" text-anchor="end" fill="var(--muted)" font-size="12" font-variant-numeric="tabular-nums">.495</text>
<text x="106" y="95.0" text-anchor="end" fill="var(--fg)" font-size="12.5">Royals</text>
<path d="M447.22584497678207,80H401.3639842311019A4.0,4.0 0 0 0 397.3639842311019,84.0V98.0A4.0,4.0 0 0 0 401.3639842311019,102H447.22584497678207Z" fill="var(--chart-pos)"><title>Royals: 45 games left, opponents averaging .493, 24 home and 21 away</title></path>
<text x="389.4" y="95.0" text-anchor="end" fill="var(--muted)" font-size="12" font-variant-numeric="tabular-nums">.493</text>
<text x="106" y="129.0" text-anchor="end" fill="var(--fg)" font-size="12.5">Tigers</text>
<path d="M447.22584497678207,114H392.7878914642629A4.0,4.0 0 0 0 388.7878914642629,118.0V132.0A4.0,4.0 0 0 0 392.7878914642629,136H447.22584497678207Z" fill="var(--chart-pos)"><title>Tigers: 46 games left, opponents averaging .492, 24 home and 22 away</title></path>
<text x="380.8" y="129.0" text-anchor="end" fill="var(--muted)" font-size="12" font-variant-numeric="tabular-nums">.492</text>
<text x="106" y="163.0" text-anchor="end" fill="var(--fg)" font-size="12.5">White Sox</text>
<path d="M447.22584497678207,148H351.6515211130602A4.0,4.0 0 0 0 347.6515211130602,152.0V166.0A4.0,4.0 0 0 0 351.6515211130602,170H447.22584497678207Z" fill="var(--chart-pos)"><title>White Sox: 47 games left, opponents averaging .486, 25 home and 22 away</title></path>
<text x="339.7" y="163.0" text-anchor="end" fill="var(--muted)" font-size="12" font-variant-numeric="tabular-nums">.486</text>
<text x="106" y="197.0" text-anchor="end" fill="var(--fg)" font-size="12.5">Guardians</text>
<path d="M447.22584497678207,182H165.5913850077393A4.0,4.0 0 0 0 161.5913850077393,186.0V200.0A4.0,4.0 0 0 0 165.5913850077393,204H447.22584497678207Z" fill="var(--chart-pos)"><title>Guardians: 45 games left, opponents averaging .460, 22 home and 23 away</title></path>
<text x="153.6" y="197.0" text-anchor="end" fill="var(--muted)" font-size="12" font-variant-numeric="tabular-nums">.460</text>
</svg>
```

| Team | Games left | Opponent win pct | Home | Away | In division | Vs winning teams |
|---|---|---|---|---|---|---|
| Twins | 45 | .495 | 24 | 21 | 15 | 20 |
| Royals | 45 | .493 | 24 | 21 | 12 | 17 |
| Tigers | 46 | .492 | 24 | 22 | 23 | 13 |
| White Sox | 47 | .486 | 25 | 22 | 21 | 8 |
| Guardians | 45 | .460 | 22 | 23 | 21 | 11 |

Two things jump out of that table.

**The first one is the Tigers' whole season in a single number.** Twenty-three
of Detroit's forty-six remaining games are against the AL Central. That is
exactly half, and across all thirty major league teams only Baltimore matches
it. Nobody in baseball has a stretch run more concentrated on the teams
standing directly in front of them.

Break it down further and it gets better. Seven against Cleveland. Seven
against Chicago. Six against Minnesota. **Twenty of the forty-six are against
the three teams Detroit is chasing**, and every one of those swings the gap by
two, not one. A team three and a half games out with twenty head-to-head games
left does not need anybody's help. It needs to beat the people it is already
scheduled to play.

**The second thing is the one Tigers fans will not enjoy.** Look at the
Guardians' bar. Their remaining opponents average .460, more than three points
softer than anyone else in the division, including six more games against a
Kansas City team that is 48-69. Cleveland is half a game out of a wild card
spot and gets the gentlest landing in the division to close it out. Detroit
does not get that. Detroit gets a schedule of roughly league-average difficulty
and has to earn every one of these.

Note also that the two ways of measuring a soft schedule disagree, and I am not
going to hide it. By opponent winning percentage Cleveland has it easiest. By
raw count of games against winning teams, Chicago does, with only **eight** left
against a team over .500 while Minnesota has twenty. Both measures are real.
They answer slightly different questions, and where they conflict the honest
answer is that the White Sox and Guardians both got the better end of it and the
Twins clearly got the worst.

## The thing that could make all of this wrong

The run differential that makes Detroit look like a 66-win team was earned by a
pitching staff that no longer exists in the same form. **Tarik Skubal is a
Dodger.** He was traded at the deadline, he is currently listed on Los Angeles'
roster, and every start he made is baked into that 451 runs allowed.

Pythagorean expectation is backward looking by construction. It tells you what
a team's performance to date deserved, not what the roster in the clubhouse
tomorrow is going to do. Strip out the best starter on a team whose entire case
rests on run prevention and the projection ahead is worse than the projection
behind, by an amount nobody can quantify honestly in August.

I also tested the underlying idea before publishing it, on 1,743 games, and the
finding was mixed in a way worth repeating here: teams running well below their
Pythagorean expectation did go 61.0 percent over their next twenty games, but
the snapshots in that sample overlapped heavily, so it is suggestive rather than
proven. I am not going to pretend a regression argument is a law.

## Where that leaves it

Detroit is 56-60, three and a half back in the division and two back of the
final wild card spot with seven teams stacked inside three games of it. The
underlying team is the best in the division and it is not close. The schedule
hands them the exact games they need. The bullpen has cost them ten wins and
the rotation just lost its best arm.

That is a real fight rather than a feel-good story, and it is the most
interesting six weeks any Detroit team has going right now.

---

*Every number here comes from the MLB Stats API on 2026-08-08 and the scripts
that produced them are in the repository. Not betting advice.*
