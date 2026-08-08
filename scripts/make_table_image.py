"""Render the two AL Central tables as one PNG for attaching to a post.

Numbers come from the MLB Stats API pull of 2026-08-08 (standings) and the
remaining-schedule script in the newsroom repo. Edit the DATA blocks and re-run.

    python make_table_image.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

INK = "#1a1a1a"
MUTED = "#666666"
RULE = "#cccccc"
BAND = "#eceff1"
SURFACE = "#ffffff"

HILITE = "Tigers"

T1_TITLE = "AL Central, record vs expected"
T1_COLS = ["Team", "Record", "Run diff", "xW-L"]
T1_ALIGN = ["left", "right", "right", "right"]
T1_ROWS = [
    ["White Sox", "59-56", "+32", "61-54"],
    ["Guardians", "58-59", "-22", "56-61"],
    ["Twins", "58-59", "-33", "55-62"],
    ["Tigers", "56-60", "+77", "66-50"],
    ["Royals", "48-69", "-105", "48-69"],
]

T2_TITLE = "What is left on the schedule"
T2_COLS = ["Team", "Games left", "Opp win pct", "Home", "Away",
           "In division", "Vs winning teams"]
T2_ALIGN = ["left", "right", "right", "right", "right", "right", "right"]
# Same order as the table above: standings order, so a reader can track one team
# down through both tables.
T2_ROWS = [
    ["White Sox", "47", ".486", "25", "22", "21", "8"],
    ["Guardians", "45", ".460", "22", "23", "21", "11"],
    ["Twins", "45", ".495", "24", "21", "15", "20"],
    ["Tigers", "46", ".492", "24", "22", "23", "13"],
    ["Royals", "45", ".493", "24", "21", "12", "17"],
]

FOOTER = "MLB Stats API, 2026-08-08. xW-L is the Pythagorean expectation at the 1.83 exponent."

FIG_W = 8.0          # inches
ROW_H = 0.30         # inches per data row
HEAD_H = 0.34
TITLE_H = 0.40
GAP = 0.34
PAD_TOP = 0.18
PAD_BOTTOM = 0.42
SIDE = 0.30

FS_TITLE = 12.5
FS_HEAD = 9.5
FS_CELL = 10.5
FS_FOOT = 8.0


def block_height(rows):
    return TITLE_H + HEAD_H + ROW_H * len(rows)


def draw_block(fig, y_top, title, cols, aligns, rows, weights, span_frac=1.0):
    """Draw one table. y_top is in inches from the top of the figure.

    span_frac narrows the table without narrowing the figure, so a four column
    table does not get stretched to the same width as a seven column one.
    """
    h = fig.get_figheight()

    def yf(inches_from_top):
        return 1.0 - inches_from_top / h

    x_left = SIDE / FIG_W
    x_right = x_left + (1.0 - 2 * SIDE / FIG_W) * span_frac
    span = x_right - x_left

    # column x positions: first column left-aligned, rest right-aligned and
    # spread evenly across the remaining width
    first_w = weights[0]
    rest = weights[1:]
    rest_total = sum(rest)
    xs = []
    cursor = x_left
    for i, w in enumerate(weights):
        frac = (w / sum(weights)) * span
        if aligns[i] == "left":
            xs.append(cursor)
        else:
            xs.append(cursor + frac)
        cursor += frac

    y = y_top
    fig.text(x_left, yf(y + 0.20), title, fontsize=FS_TITLE, color=INK,
             fontweight="bold", ha="left", va="baseline")
    y += TITLE_H

    for i, c in enumerate(cols):
        fig.text(xs[i], yf(y + 0.20), c, fontsize=FS_HEAD, color=MUTED,
                 ha=aligns[i], va="baseline")
    y += HEAD_H

    fig.add_artist(plt.Line2D([x_left, x_right], [yf(y - 0.06)] * 2,
                              color=RULE, linewidth=1.0,
                              transform=fig.transFigure))

    for r in rows:
        bold = r[0] == HILITE
        if bold:
            fig.add_artist(Rectangle(
                (x_left - 0.008, yf(y + ROW_H - 0.02)),
                (x_right - x_left) + 0.016,
                ROW_H / h,
                transform=fig.transFigure, facecolor=BAND,
                edgecolor="none", zorder=0))
        for i, cell in enumerate(r):
            fig.text(xs[i], yf(y + 0.21), cell, fontsize=FS_CELL, color=INK,
                     ha=aligns[i], va="baseline", zorder=2,
                     fontweight="bold" if bold else "normal")
        y += ROW_H

    fig.add_artist(plt.Line2D([x_left, x_right], [yf(y - 0.05)] * 2,
                              color=RULE, linewidth=1.0,
                              transform=fig.transFigure))
    return y


def main():
    total_h = (PAD_TOP + block_height(T1_ROWS) + GAP
               + block_height(T2_ROWS) + PAD_BOTTOM)
    fig = plt.figure(figsize=(FIG_W, total_h), dpi=200, facecolor=SURFACE)

    y = PAD_TOP
    y = draw_block(fig, y, T1_TITLE, T1_COLS, T1_ALIGN, T1_ROWS,
                   weights=[1.6, 1.0, 1.0, 1.0], span_frac=0.62)
    y += GAP
    y = draw_block(fig, y, T2_TITLE, T2_COLS, T2_ALIGN, T2_ROWS,
                   weights=[1.7, 1.15, 1.2, 0.8, 0.8, 1.15, 1.5])

    fig.text(SIDE / FIG_W, 1.0 - (y + 0.26) / total_h, FOOTER,
             fontsize=FS_FOOT, color=MUTED, ha="left", va="baseline")

    out = "2026-08-08-tigers-al-central-tables.png"
    fig.savefig(out, dpi=200, facecolor=SURFACE)
    print("wrote", out, "at", int(FIG_W * 200), "x", int(total_h * 200), "px")


if __name__ == "__main__":
    main()
