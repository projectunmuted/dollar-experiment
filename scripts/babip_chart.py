#!/usr/bin/env python3
"""Emit an inline SVG: BABIP distance from the league median, starting pitchers.

Batting average on balls in play is the cleanest single measure of how much a
pitcher's run prevention is being helped by what happens after contact. The
population median is the reference line, so a bar reading left means balls in
play are finding gloves at a rate the pitcher does not control.

    python scripts/babip_chart.py > /tmp/chart.svg
    python scripts/babip_chart.py --highlight 675512 --also 657277 --n 8

Live data every time, never hand-drawn, so a published number cannot drift
from the number behind it. Colors are the site's --chart-pos / --chart-neg
tokens, already validated for colorblind separation and contrast on both
surfaces.
"""

from __future__ import annotations

import argparse
import json
import statistics
import urllib.request

from pythag_chart import bar_path

SEASON = 2026
MIN_IP = 70.0
MIN_GS = 10
PAD_L, PAD_R = 138, 44
BAR_H, ROW_GAP = 22, 12
TOP, BOTTOM = 46, 34
API = "https://statsapi.mlb.com/api/v1/stats"


def _ip(text: str) -> float:
    """MLB writes thirds of an inning as .1 and .2, which are not decimals."""
    whole, _, part = text.partition(".")
    return int(whole) + {"": 0, "0": 0, "1": 1 / 3, "2": 2 / 3}[part]


def _avg(value: float) -> str:
    """Baseball prints averages without the leading zero: 0.191 -> .191"""
    return f"{value:.3f}".lstrip("0")


def _get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def fetch() -> list[dict]:
    """Every starter with enough work to have a meaningful BABIP."""
    base = f"&group=pitching&season={SEASON}&sportId=1&limit=2000&playerPool=All"
    season = _get(f"{API}?stats=season{base}")
    advanced = _get(f"{API}?stats=seasonAdvanced{base}")

    workload = {}
    for split in season["stats"][0]["splits"]:
        stat = split["stat"]
        workload[split["player"]["id"]] = {
            "ip": _ip(stat["inningsPitched"]),
            "gs": stat["gamesStarted"],
            "era": stat["era"],
        }

    rows = []
    for split in advanced["stats"][0]["splits"]:
        pid = split["player"]["id"]
        work = workload.get(pid)
        babip = split["stat"].get("babip")
        if not work or not babip:
            continue
        if work["ip"] < MIN_IP or work["gs"] < MIN_GS:
            continue
        rows.append({
            "id": pid, "name": split["player"]["fullName"],
            "babip": float(babip), "ip": work["ip"], "era": work["era"],
        })
    return sorted(rows, key=lambda r: r["babip"])


def build(rows: list[dict], median: float, total: int,
          highlight: int | None, width: int = 640) -> str:
    span_max = max(abs(r["babip"] - median) for r in rows) + 0.012
    plot_w = width - PAD_L - PAD_R
    to_x = lambda v: PAD_L + (v + span_max) / (2 * span_max) * plot_w
    zero = to_x(0)

    height = TOP + len(rows) * (BAR_H + ROW_GAP) - ROW_GAP + BOTTOM
    out = [
        f'<svg viewBox="0 0 {width} {height}" width="100%" role="img" '
        f'aria-labelledby="babip-title" style="max-width:{width}px;height:auto;'
        f'font-family:ui-sans-serif,system-ui,-apple-system,\'Segoe UI\','
        f'Roboto,sans-serif">',
        '<title id="babip-title">Batting average on balls in play, distance '
        'from the median starting pitcher</title>',
        '<text x="0" y="16" fill="var(--fg)" font-size="13" font-weight="600">'
        'Batting average on balls in play, vs the median starter</text>',
        f'<text x="0" y="34" fill="var(--muted)" font-size="11">'
        f'{total} pitchers with {MIN_IP:.0f}+ innings and {MIN_GS}+ starts in '
        f'{SEASON}. The line is the median, {_avg(median)}. '
        f'Left of it, balls in play are finding gloves.</text>',
    ]
    out.append(f'<line x1="{zero:.1f}" y1="{TOP-6}" x2="{zero:.1f}" '
               f'y2="{height-BOTTOM+6:.1f}" stroke="var(--rule)" '
               f'stroke-width="2"/>')

    for i, r in enumerate(rows):
        y = TOP + i * (BAR_H + ROW_GAP)
        gap = r["babip"] - median
        x_end = to_x(gap)
        x_start = zero + (2 if gap >= 0 else -2)
        color = "var(--chart-neg)" if gap >= 0 else "var(--chart-pos)"
        weight = ' font-weight="700"' if r["id"] == highlight else ""
        label = _avg(r["babip"])
        dim = ' opacity="0.55"' if highlight and r["id"] != highlight else ""

        out.append(f'<text x="{PAD_L-12}" y="{y+BAR_H/2+4:.1f}" '
                   f'text-anchor="end" fill="var(--fg)" font-size="12.5"'
                   f'{weight}>{r["name"]}</text>')
        out.append(
            f'<path d="{bar_path(x_start, x_end, y, BAR_H)}" fill="{color}"'
            f'{dim}>'
            f'<title>{r["name"]}: BABIP {label} over {r["ip"]:.1f} innings, '
            f'ERA {r["era"]}. Median is {_avg(median)}.</title></path>'
        )
        anchor, dx = ("start", 8) if gap >= 0 else ("end", -8)
        out.append(f'<text x="{x_end+dx:.1f}" y="{y+BAR_H/2+4:.1f}" '
                   f'text-anchor="{anchor}" fill="var(--muted)" font-size="12" '
                   f'font-variant-numeric="tabular-nums"{weight}>{label}</text>')

    out.append("</svg>")
    return "\n".join(out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=6, help="lowest N to chart")
    ap.add_argument("--highlight", type=int, help="player id to emphasize")
    ap.add_argument("--also", type=int, action="append", default=[],
                    help="player id to append for comparison, wherever he ranks")
    args = ap.parse_args()

    everyone = fetch()
    median = statistics.median(r["babip"] for r in everyone)
    chosen = everyone[:args.n]
    ids = {r["id"] for r in chosen}
    for pid in args.also:
        extra = next((r for r in everyone if r["id"] == pid), None)
        if extra and extra["id"] not in ids:
            chosen.append(extra)

    for rank, r in enumerate(everyone, 1):
        if r["id"] == args.highlight or r["id"] in args.also:
            print(f"# {r['name']}: {_avg(r['babip'])}, rank {rank} of "
                  f"{len(everyone)}, {r['ip']:.1f} IP, ERA {r['era']}")
    print(build(chosen, median, len(everyone), args.highlight))
