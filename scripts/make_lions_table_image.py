"""Render the two preseason-signal tables as one PNG for attaching to a post.

Numbers come straight from `preseason_signal.py`, which reads the cached ESPN
schedule pull in `preseason_cache.json`. Re-run that script and paste its output
into the DATA blocks below if the arithmetic ever needs refreshing.

    python make_lions_table_image.py

Writes ../drafts/2026-08-08-lions-preseason-tables.png
"""

import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import make_table_image as mti

# --- DATA (from `python preseason_signal.py`, 2026-08-08) -------------------

T1_TITLE = "Every NFL team, every preseason, 2015 to 2025"
T1_COLS = ["Preseason", "Team-seasons", "Regular season", "vs .500"]
T1_ALIGN = ["left", "right", "right", "right"]
T1_ROWS = [
    ["Won every preseason game", "39", ".466", "-.034"],
    ["Winning preseason", "93", ".561", "+.061"],
    ["Even preseason", "62", ".525", "+.025"],
    ["Losing preseason", "90", ".461", "-.039"],
    ["Lost every preseason game", "36", ".475", "-.025"],
]
T1_HILITE = {"Won every preseason game", "Lost every preseason game"}

T2_TITLE = "Detroit's own August receipts"
T2_COLS = ["Season", "Preseason", "Regular season"]
T2_ALIGN = ["left", "right", "right"]
T2_ROWS = [
    ["2015", "3-1", "7-9"],
    ["2016", "2-2", "9-7"],
    ["2017", "2-2", "9-7"],
    ["2018", "1-3", "6-10"],
    ["2019", "0-4", "3-12-1"],
    ["2021", "0-3", "3-13-1"],
    ["2022", "1-2", "9-8"],
    ["2023", "2-1", "12-5"],
    ["2024", "2-1", "15-2"],
    ["2025", "1-3", "9-8"],
]
T2_HILITE = {"2024"}

FOOTER = ("ESPN public schedule endpoint. 320 team-seasons; 2020 excluded, "
          "no preseason was played. Ties count as half a win.")

# ---------------------------------------------------------------------------


def main():
    total_h = (mti.PAD_TOP + mti.block_height(T1_ROWS) + mti.GAP
               + mti.block_height(T2_ROWS) + mti.PAD_BOTTOM)
    fig = plt.figure(figsize=(mti.FIG_W, total_h), dpi=200,
                     facecolor=mti.SURFACE)

    y = mti.PAD_TOP
    y = mti.draw_block(fig, y, T1_TITLE, T1_COLS, T1_ALIGN, T1_ROWS,
                       weights=[2.6, 1.2, 1.2, 1.0], span_frac=0.92,
                       hilite=T1_HILITE)
    y += mti.GAP
    y = mti.draw_block(fig, y, T2_TITLE, T2_COLS, T2_ALIGN, T2_ROWS,
                       weights=[1.2, 1.0, 1.4], span_frac=0.56,
                       hilite=T2_HILITE)

    fig.text(mti.SIDE / mti.FIG_W, 1.0 - (y + 0.26) / total_h, FOOTER,
             fontsize=mti.FS_FOOT, color=mti.MUTED, ha="left", va="baseline")

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                       "drafts", "2026-08-08-lions-preseason-tables.png")
    fig.savefig(out, dpi=200, facecolor=mti.SURFACE)
    print("wrote", os.path.normpath(out), "at",
          int(mti.FIG_W * 200), "x", int(total_h * 200), "px")


if __name__ == "__main__":
    main()
