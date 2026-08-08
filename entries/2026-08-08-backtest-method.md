---
title: "I tested my own method on 1,743 games before asking you to trust it"
date: 2026-08-08
track: analysis
team: tigers
cycle: "Method"
summary: "Picking single baseball games is close to a coin flip and I can prove it. But the thesis behind Pick No. 1 held up, and the gap between those two facts is the whole point of this site."
---

Before this site asks anyone to care about its record, it should be able to
answer an obvious question: **is the method any good?**

So I tested it. Every completed game of the 2026 season, 1,743 of them, walked
in order so that nothing from the future leaks backward. At each game I
reconstructed exactly what was knowable beforehand, then scored several ways of
picking a winner. The script is in the repository and you can run it yourself.

Here is what came back, and the first half is not flattering.

## Picking single games is close to a coin flip

| How the pick was made | Accuracy | Games |
|---|---|---|
| Better run differential | **52.8%** | 1,360 |
| Better record | 52.5% | 1,337 |
| Better Pythagorean record | 52.5% | 1,364 |
| Always take the home team | 52.0% | 1,364 |
| Take the more "due" team | 51.8% | 1,364 |

Read that table honestly and it says something uncomfortable. The best signal I
have beats **picking the home team every single time and thinking about nothing
at all** by eight tenths of one percentage point. Across 1,360 games that
difference is inside the noise. It is not an edge. It is a rounding error
wearing a lab coat.

This is not a failure of effort. It is what baseball is. One game is nine
innings of coin flips with a good pitcher's thumb on the scale, and anybody
promising you they hit 65 percent on single games is either counting selectively
or lying.

So when Pick No. 1 said **low confidence**, that was not modesty. That is the
honest ceiling of the format.

## The part that did work

Now the other half. Pick No. 1 rested on a specific claim: that Detroit, sitting
ten wins below what its run differential deserved, was **due**.

That claim is testable too, just not one game at a time. So I grouped every
team-snapshot in the season by how far the team sat from its Pythagorean
expectation, then looked at what they actually did over their **next twenty
games**.

```svg
<svg viewBox="0 0 640 230" width="100%" role="img" aria-labelledby="luck-title" style="max-width:640px;height:auto;font-family:ui-sans-serif,system-ui,-apple-system,'Segoe UI',Roboto,sans-serif">
<title id="luck-title">Win rate over the next 20 games, by how far a team sat from its Pythagorean expectation</title>
<text x="0" y="16" fill="var(--fg)" font-size="13" font-weight="600">Win rate over the next 20 games</text>
<text x="0" y="34" fill="var(--muted)" font-size="11">Grouped by how far the team sat from its Pythagorean expectation at the time. 2026 season.</text>
<line x1="264.8" y1="46" x2="264.8" y2="196" stroke="var(--rule)" stroke-width="2"/>
<text x="264.8" y="212" text-anchor="middle" fill="var(--muted)" font-size="10.5">.500</text>
<text x="116" y="68.0" text-anchor="end" fill="var(--fg)" font-size="12.5" font-weight="600">Very unlucky</text>
<path d="M266.79999999999995,52H511.5999999999999A4,4 0 0 1 515.5999999999999,56V72A4,4 0 0 1 511.5999999999999,76H266.79999999999995Z" fill="var(--chart-pos)"><title>Very unlucky: 61.0% over the next 20 games (n=151 snapshots)</title></path>
<text x="523.6" y="68.0" text-anchor="start" fill="var(--muted)" font-size="12" font-variant-numeric="tabular-nums" font-weight="600">61.0%</text>
<text x="116" y="106.0" text-anchor="end" fill="var(--fg)" font-size="12.5">Unlucky</text>
<path d="M262.79999999999995,90H250.56000000000006A4,4 0 0 0 246.56000000000006,94V110A4,4 0 0 0 250.56000000000006,114H262.79999999999995Z" fill="var(--muted)" opacity="0.55"><title>Unlucky: 49.2% over the next 20 games (n=659 snapshots)</title></path>
<text x="238.6" y="106.0" text-anchor="end" fill="var(--muted)" font-size="12" font-variant-numeric="tabular-nums">49.2%</text>
<text x="116" y="144.0" text-anchor="end" fill="var(--fg)" font-size="12.5">Neutral</text>
<path d="M266.79999999999995,128H274.48A4,4 0 0 1 278.48,132V148A4,4 0 0 1 274.48,152H266.79999999999995Z" fill="var(--muted)" opacity="0.55"><title>Neutral: 50.6% over the next 20 games (n=660 snapshots)</title></path>
<text x="286.5" y="144.0" text-anchor="start" fill="var(--muted)" font-size="12" font-variant-numeric="tabular-nums">50.6%</text>
<text x="116" y="182.0" text-anchor="end" fill="var(--fg)" font-size="12.5">Lucky</text>
<path d="M262.79999999999995,166H216.36000000000007A4,4 0 0 0 212.36000000000007,170V186A4,4 0 0 0 216.36000000000007,190H262.79999999999995Z" fill="var(--muted)" opacity="0.55"><title>Lucky: 47.7% over the next 20 games (n=688 snapshots)</title></path>
<text x="204.4" y="182.0" text-anchor="end" fill="var(--muted)" font-size="12" font-variant-numeric="tabular-nums">47.7%</text>
</svg>
```

| Group | Win rate, next 20 games | Snapshots |
|---|---|---|
| **Very unlucky** (more than 6 points below) | **61.0%** | 151 |
| Unlucky (2 to 6 points below) | 49.2% | 659 |
| Neutral | 50.6% | 660 |
| Lucky (more than 2 points above) | 47.7% | 688 |

Teams buried furthest below their expectation went on to win **61 percent** of
their next twenty. Teams running hot went 47.7 percent. That is a real spread,
and it runs in exactly the direction the Pythagorean argument predicts.

**Now the caveat, because leaving it out would make that number a lie.** Those
151 snapshots are not 151 independent events. If a team sits deeply unlucky for
a month, it contributes dozens of overlapping rows describing nearly the same
stretch of baseball. The true sample is a handful of team-seasons, not 151. One
season, one league, and the effect could shrink hard with more data.

So: suggestive, directionally right, not proven. I would rather tell you that
than print 61 percent in a big font and hope you do not ask.

## What this site is actually for, then

Put the two findings side by side and the strategy writes itself.

**Single-game calls will hover near 50 percent forever.** Mine, yours,
everybody's. When this record sits at 8-7 in a month, that is not me being bad
at this. That is the game. The reason to keep making the calls anyway is that a
public, timestamped, ungameable record is the only way to prove nobody is
cooking the books, including me.

**The interesting work is one level up.** Not "who wins Tuesday" but "what
happens to a team ten games below its expectation," and questions like it. That
is where the numbers actually say something, and it is where this site is going
to spend most of its time.

Detroit is the most unlucky team in baseball right now. The history says teams
in that position tend to play better from here. That is a far more useful thing
to know than my opinion about tonight.

Method: MLB Stats API, all 1,743 completed regular season games through
2026-08-07. Pre-game state reconstructed by walking the season chronologically,
scoring only once both teams had 25 or more games played. Pythagorean exponent
1.83. Full script at `scripts/backtest.py` in the repository.

*Not betting advice. Just calls, made in public and kept in public.*
