#!/usr/bin/env python3
"""Remaining strength of schedule for one division, from live MLB data.

For every team in a division, walk the games it has left, look up each
opponent's current winning percentage, and average them weighted by how many
times the matchup recurs. Also reports the home/away split of what is left and
how many of those games are against divisional rivals, because those are the
games that move two teams at once.

    python scripts/remaining_sos.py 202              # table to stdout
    python scripts/remaining_sos.py 202 --svg        # chart to stdout

Division ids: 200 AL West, 201 AL East, 202 AL Central,
              203 NL West, 204 NL East, 205 NL Central

Colors are the site's validated --chart-pos / --chart-neg tokens. Generated
from data every time, so a published number cannot drift from its source.
"""

from __future__ import annotations

import json
import sys
import urllib.request
from datetime import date

API = "https://statsapi.mlb.com/api/v1"
SEASON = 2026
PAD_L, PAD_R = 118, 60
BAR_H, ROW_GAP = 22, 12
TOP, BOTTOM = 46, 34


def get(url: str) -> dict:
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.load(r)


def records() -> dict[int, dict]:
    """teamId -> current record. Every team, both leagues."""
    data = get(f"{API}/standings?leagueId=103,104&season={SEASON}"
               f"&standingsTypes=regularSeason")
    out = {}
    for record in data["records"]:
        for t in record["teamRecords"]:
            w, l = t["wins"], t["losses"]
            out[t["team"]["id"]] = {
                "name": t["team"]["name"], "w": w, "l": l,
                "pct": w / (w + l) if w + l else 0.0,
                "division": record.get("division", {}).get("id"),
            }
    return out


def remaining(team_id: int, start: str) -> list[dict]:
    """Unplayed regular-season games for one team, from `start` forward."""
    data = get(f"{API}/schedule?sportId=1&teamId={team_id}&season={SEASON}"
               f"&startDate={start}&endDate={SEASON}-11-15&gameType=R")
    games = []
    for d in data.get("dates", []):
        for g in d["games"]:
            if g["status"]["abstractGameState"] == "Final":
                continue
            home = g["teams"]["home"]["team"]["id"]
            away = g["teams"]["away"]["team"]["id"]
            games.append({
                "gamePk": g["gamePk"],
                "date": g["gameDate"],
                "opp": away if home == team_id else home,
                "at_home": home == team_id,
            })
    return games


def analyse(division: int, start: str | None = None) -> list[dict]:
    start = start or date.today().isoformat()
    recs = records()
    rows = []
    for team_id, r in recs.items():
        if r["division"] != division:
            continue
        games = remaining(team_id, start)
        if not games:
            continue
        opp_pcts = [recs[g["opp"]]["pct"] for g in games if g["opp"] in recs]
        rows.append({
            "id": team_id,
            "name": r["name"],
            "w": r["w"], "l": r["l"], "pct": r["pct"],
            "left": len(games),
            "sos": sum(opp_pcts) / len(opp_pcts),
            "home": sum(1 for g in games if g["at_home"]),
            "away": sum(1 for g in games if not g["at_home"]),
            "in_div": sum(1 for g in games
                          if recs.get(g["opp"], {}).get("division") == division),
            "over_500": sum(1 for g in games
                            if recs.get(g["opp"], {}).get("pct", 0) > 0.5),
        })
    return sorted(rows, key=lambda t: -t["sos"])


def bar_path(x0: float, x1: float, y: float, h: float, r: float = 4.0) -> str:
    """Only the data end is rounded; the baseline end stays square so the bar
    reads as anchored rather than floating."""
    if abs(x1 - x0) < r:
        return f"M{x0},{y}H{x1}V{y+h}H{x0}Z"
    if x1 > x0:
        return (f"M{x0},{y}H{x1-r}A{r},{r} 0 0 1 {x1},{y+r}"
                f"V{y+h-r}A{r},{r} 0 0 1 {x1-r},{y+h}H{x0}Z")
    return (f"M{x0},{y}H{x1+r}A{r},{r} 0 0 0 {x1},{y+r}"
            f"V{y+h-r}A{r},{r} 0 0 0 {x1+r},{y+h}H{x0}Z")


def build_svg(rows: list[dict], width: int = 640) -> str:
    """Bars are opponent winning percentage measured from .500, because .500 is
    the only number on that axis that means anything: above it the remaining
    schedule is harder than average, below it easier."""
    gaps = [r["sos"] - 0.5 for r in rows]
    lo = min(-0.012, min(gaps)) - 0.006
    hi = max(0.012, max(gaps)) + 0.006
    plot_w = width - PAD_L - PAD_R
    span = hi - lo
    to_x = lambda v: PAD_L + (v - lo) / span * plot_w
    zero = to_x(0)

    height = TOP + len(rows) * (BAR_H + ROW_GAP) - ROW_GAP + BOTTOM
    out = [
        f'<svg viewBox="0 0 {width} {height}" width="100%" role="img" '
        f'aria-labelledby="sos-title" style="max-width:{width}px;height:auto;'
        f'font-family:ui-sans-serif,system-ui,-apple-system,\'Segoe UI\','
        f'Roboto,sans-serif">',
        '<title id="sos-title">Remaining opponent winning percentage relative '
        'to .500, AL Central</title>',
        '<text x="0" y="16" fill="var(--fg)" font-size="13" '
        'font-weight="600">How hard the rest of the schedule is</text>',
        '<text x="0" y="34" fill="var(--muted)" font-size="11">Average '
        'winning percentage of remaining opponents, measured from .500. '
        'Left of the line means an easier than average slate.</text>',
    ]
    out.append(f'<line x1="{zero:.1f}" y1="{TOP-6}" x2="{zero:.1f}" '
               f'y2="{height-BOTTOM+6:.1f}" stroke="var(--rule)" '
               f'stroke-width="2"/>')

    for i, r in enumerate(rows):
        y = TOP + i * (BAR_H + ROW_GAP)
        gap = r["sos"] - 0.5
        x_end = to_x(gap)
        # Harder is the adverse direction, so harder takes the negative hue.
        color = "var(--chart-neg)" if gap >= 0 else "var(--chart-pos)"
        x_start = zero + (2 if gap >= 0 else -2)
        label = f'{r["sos"]:.3f}'.lstrip("0")

        out.append(f'<text x="{PAD_L-12}" y="{y+BAR_H/2+4:.1f}" '
                   f'text-anchor="end" fill="var(--fg)" font-size="12.5">'
                   f'{r["name"]}</text>')
        out.append(f'<path d="{bar_path(x_start, x_end, y, BAR_H)}" '
                   f'fill="{color}"><title>{r["name"]}: {r["left"]} games '
                   f'left, opponents averaging {label}, {r["home"]} home and '
                   f'{r["away"]} away</title></path>')
        anchor, dx = ("start", 8) if gap >= 0 else ("end", -8)
        out.append(f'<text x="{x_end+dx:.1f}" y="{y+BAR_H/2+4:.1f}" '
                   f'text-anchor="{anchor}" fill="var(--muted)" '
                   f'font-size="12" font-variant-numeric="tabular-nums">'
                   f'{label}</text>')

    out.append("</svg>")
    return "\n".join(out)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    division = int(args[0]) if args else 202
    rows = analyse(division)
    if "--svg" in sys.argv:
        print(build_svg(rows))
    else:
        print(f"{'team':<24}{'rec':>8}{'left':>6}{'SOS':>7}"
              f"{'home':>6}{'away':>6}{'div':>5}{'>.500':>7}")
        for r in rows:
            print(f"{r['name']:<24}{r['w']}-{r['l']:>4}{r['left']:>6}"
                  f"{r['sos']:>7.3f}{r['home']:>6}{r['away']:>6}"
                  f"{r['in_div']:>5}{r['over_500']:>7}")
