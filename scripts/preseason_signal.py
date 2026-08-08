#!/usr/bin/env python3
"""Does an NFL team's preseason record tell you anything about its season?

Pulls every team's preseason and regular season results from ESPN's public
schedule endpoint, season by season, and measures whether the first predicts
the second. Nothing is hand-entered: the cache file is the receipt.

    python scripts/preseason_signal.py            # analysis to stdout
    python scripts/preseason_signal.py --chart    # inline SVG to stdout

2020 is skipped because the preseason was cancelled for COVID. Ties count as
half a win on both sides of the ledger.

Colors come from the site's --chart-pos / --chart-neg CSS tokens, which were
validated for colorblind separation and contrast in light and dark mode.
"""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.request

SEASONS = [s for s in range(2015, 2026) if s != 2020]
CACHE = os.path.join(os.path.dirname(__file__), "preseason_cache.json")
API = ("https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/"
       "{team}/schedule?season={season}&seasontype={st}")

TEAMS = [
    "ari", "atl", "bal", "buf", "car", "chi", "cin", "cle", "dal", "den",
    "det", "gb", "hou", "ind", "jax", "kc", "lac", "lar", "lv", "mia",
    "min", "ne", "no", "nyg", "nyj", "phi", "pit", "sea", "sf", "tb",
    "ten", "wsh",
]

PAD_L, PAD_R, TOP, BOTTOM = 52, 22, 52, 46


def fetch(team: str, season: int, st: int) -> tuple[float, float]:
    """Return (wins, games) for one team-season-phase. A tie is half a win."""
    url = API.format(team=team, season=season, st=st)
    # ESPN throws intermittent 502s under a long sweep; back off and keep going.
    for attempt in range(8):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                data = json.load(r)
            break
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
            if attempt == 7:
                raise
            time.sleep(2.0 * (attempt + 1))

    wins = games = 0.0
    for event in data.get("events", []):
        comp = event["competitions"][0]
        sides = comp.get("competitors", [])
        if len(sides) != 2:
            continue
        scores = [s.get("score", {}).get("value") for s in sides]
        if any(v is None for v in scores):
            continue                                   # unplayed or cancelled
        mine = next((s for s in sides
                     if s["team"]["abbreviation"].lower() == team), None)
        if mine is None:                               # relocations, odd abbrs
            mine = sides[0]
        games += 1
        if scores[0] == scores[1]:
            wins += 0.5
        elif mine.get("winner"):
            wins += 1
    return wins, games


def collect() -> list[dict]:
    """One row per team-season, cached to disk so a rerun costs nothing."""
    if os.path.exists(CACHE):
        with open(CACHE, encoding="utf-8") as fh:
            return json.load(fh)

    # Partial file lets an interrupted sweep resume instead of refetching.
    partial = CACHE + ".partial"
    rows = []
    if os.path.exists(partial):
        with open(partial, encoding="utf-8") as fh:
            rows = json.load(fh)
    done = {(r["team"], r["season"]) for r in rows}

    for season in SEASONS:
        for team in TEAMS:
            if (team, season) in done:
                continue
            pre_w, pre_g = fetch(team, season, 1)
            reg_w, reg_g = fetch(team, season, 2)
            if pre_g < 2 or reg_g < 10:                # incomplete, skip
                continue
            rows.append({
                "team": team, "season": season,
                "pre_w": pre_w, "pre_g": pre_g,
                "reg_w": reg_w, "reg_g": reg_g,
                "pre_pct": pre_w / pre_g, "reg_pct": reg_w / reg_g,
            })
        with open(partial, "w", encoding="utf-8") as fh:
            json.dump(rows, fh, indent=1)
        print(f"  {season}: {len(rows)} rows", file=sys.stderr)

    with open(CACHE, "w", encoding="utf-8") as fh:
        json.dump(rows, fh, indent=1)
    os.remove(partial)
    return rows


def correlation(xs: list[float], ys: list[float]) -> float:
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = sum((x - mx) ** 2 for x in xs) ** 0.5
    dy = sum((y - my) ** 2 for y in ys) ** 0.5
    return num / (dx * dy)


def buckets(rows: list[dict]) -> list[dict]:
    """Group team-seasons by preseason record, report how the season went."""
    order = [
        ("Won every preseason game", lambda r: r["pre_pct"] == 1.0),
        ("Winning preseason", lambda r: 0.5 < r["pre_pct"] < 1.0),
        ("Even preseason", lambda r: r["pre_pct"] == 0.5),
        ("Losing preseason", lambda r: 0.0 < r["pre_pct"] < 0.5),
        ("Lost every preseason game", lambda r: r["pre_pct"] == 0.0),
    ]
    out = []
    for label, test in order:
        group = [r for r in rows if test(r)]
        if not group:
            continue
        reg = sum(r["reg_pct"] for r in group) / len(group)
        out.append({"label": label, "n": len(group), "reg_pct": reg,
                    "gap": reg - 0.5})
    return out


def bar_path(x0: float, x1: float, y: float, h: float, r: float = 4.0) -> str:
    """Rect with only the data end rounded, so the bar reads as anchored to the
    baseline rather than floating. Same idiom as the Pythagorean chart."""
    if abs(x1 - x0) < r:
        return f"M{x0},{y}H{x1}V{y+h}H{x0}Z"
    if x1 > x0:
        return (f"M{x0},{y}H{x1-r}A{r},{r} 0 0 1 {x1},{y+r}"
                f"V{y+h-r}A{r},{r} 0 0 1 {x1-r},{y+h}H{x0}Z")
    return (f"M{x0},{y}H{x1+r}A{r},{r} 0 0 0 {x1},{y+r}"
            f"V{y+h-r}A{r},{r} 0 0 0 {x1+r},{y+h}H{x0}Z")


def build_chart(rows: list[dict], width: int = 640) -> str:
    """Bars: how each preseason group actually did, measured against .500.

    A scatter was the obvious choice and the wrong one: preseason win rate
    takes about seven distinct values, so 320 dots collapse into overlapping
    columns that hide the very thing being shown. Grouped bars against a .500
    baseline say it plainly.
    """
    bars = buckets(rows)
    bar_h, gap = 26, 14
    label_w = 196
    plot_w = width - label_w - 56
    span = 0.09                                   # +/- around .500, in win pct
    to_x = lambda v: label_w + (v + span) / (2 * span) * plot_w
    zero = to_x(0.0)

    height = TOP + len(bars) * (bar_h + gap) - gap + BOTTOM
    out = [
        f'<svg viewBox="0 0 {width} {height}" width="100%" '
        f'role="img" aria-labelledby="pre-title" '
        f'style="max-width:{width}px;height:auto;font-family:ui-sans-serif,'
        f"system-ui,-apple-system,'Segoe UI',Roboto,sans-serif\">",
        '<title id="pre-title">Regular season winning percentage by preseason '
        'record, all 32 NFL teams, 2015 to 2025</title>',
        '<text x="0" y="16" fill="var(--fg)" font-size="13" '
        'font-weight="600">How each preseason group actually did</text>',
        '<text x="0" y="34" fill="var(--muted)" font-size="11">Regular season '
        'winning percentage against .500. 320 team-seasons, 2015 to 2025.'
        '</text>',
    ]
    out.append(f'<line x1="{zero:.1f}" y1="{TOP-6}" x2="{zero:.1f}" '
               f'y2="{height-BOTTOM+6:.1f}" stroke="var(--rule)" '
               f'stroke-width="2"/>')

    for i, b in enumerate(bars):
        y = TOP + i * (bar_h + gap)
        x_end = to_x(b["gap"])
        pos = b["gap"] >= 0
        x_start = zero + (2 if pos else -2)
        color = "var(--chart-pos)" if pos else "var(--chart-neg)"
        out.append(
            f'<text x="{label_w-12}" y="{y+bar_h/2+4:.1f}" text-anchor="end" '
            f'fill="var(--fg)" font-size="12.5">{b["label"]}</text>'
        )
        out.append(
            f'<path d="{bar_path(x_start, x_end, y, bar_h)}" fill="{color}">'
            f'<title>{b["label"]}: {b["n"]} team-seasons, regular season '
            f'{b["reg_pct"]:.3f}</title></path>'
        )
        anchor, dx = ("start", 8) if pos else ("end", -8)
        out.append(
            f'<text x="{x_end+dx:.1f}" y="{y+bar_h/2+4:.1f}" '
            f'text-anchor="{anchor}" fill="var(--muted)" font-size="12" '
            f'font-variant-numeric="tabular-nums">'
            f'{b["reg_pct"]:.3f} (n={b["n"]})</text>'
        )

    out.append(f'<text x="0" y="{height-10}" fill="var(--muted)" '
               f'font-size="11">Bars right of the line beat .500, left of it '
               f'missed. Nothing here is far from the line.</text>')
    out.append("</svg>")
    return "\n".join(out)


def main() -> None:
    rows = collect()
    if "--chart" in sys.argv:
        print(build_chart(rows))
        return

    xs = [r["pre_pct"] for r in rows]
    ys = [r["reg_pct"] for r in rows]
    r_val = correlation(xs, ys)
    print(f"team-seasons: {len(rows)}  seasons: {min(SEASONS)}-{max(SEASONS)}")
    print(f"correlation(preseason win rate, regular season win rate) = "
          f"{r_val:+.3f}")
    print(f"variance explained: {r_val ** 2 * 100:.1f}%")
    print()
    for b in buckets(rows):
        print(f"{b['label']:<28} n={b['n']:<4} "
              f"regular season {b['reg_pct']:.3f} ({b['gap']:+.3f})")
    print()
    lions = sorted([r for r in rows if r["team"] == "det"],
                   key=lambda r: r["season"])
    for r in lions:
        print(f"DET {r['season']}: preseason {r['pre_w']:g}-"
              f"{r['pre_g']-r['pre_w']:g}  regular {r['reg_w']:g}-"
              f"{r['reg_g']-r['reg_w']:g}")


if __name__ == "__main__":
    main()
