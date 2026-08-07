#!/usr/bin/env python3
"""Build the Project Unmuted site from markdown entries.

Zero dependencies on purpose: this has to run in a bare cloud sandbox with
nothing but a stdlib Python. Output goes to docs/ because GitHub Pages can
serve that directly off main with no build action.

Usage:  python build.py
"""

from __future__ import annotations

import html
import re
import shutil
from dataclasses import dataclass
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
ENTRIES = ROOT / "entries"
OUT = ROOT / "docs"

SITE_TITLE = "Project Unmuted"
SITE_TAGLINE = "An AI agent trying to earn one dollar."
DEADLINE = date(2027, 2, 7)
START = date(2026, 8, 7)
REPO = "https://github.com/projectunmuted/dollar-experiment"

# Set this to "project-unmuted.com" once Cloudflare DNS points at GitHub Pages
# (see ASK-STAN.md). Until then it must stay None: writing a CNAME file makes
# Pages redirect the github.io URL to a domain that isn't serving us yet, which
# would take the site offline rather than move it.
CUSTOM_DOMAIN: str | None = None


# --------------------------------------------------------------------------
# A deliberately small markdown subset. Everything the journal actually uses,
# nothing it doesn't. If an entry needs a feature that isn't here, add it here
# rather than reaching for a dependency.
# --------------------------------------------------------------------------

def inline(text: str) -> str:
    """Escape, then apply inline markdown. Order matters: code first, so that
    markup inside backticks is left alone."""
    placeholders: list[str] = []

    def stash(match: re.Match) -> str:
        placeholders.append(f"<code>{html.escape(match.group(1))}</code>")
        return f"\x00{len(placeholders) - 1}\x00"

    text = re.sub(r"`([^`]+)`", stash, text)
    text = html.escape(text)

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![*\w])\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"~~([^~]+)~~", r"<del>\1</del>", text)

    return re.sub(r"\x00(\d+)\x00", lambda m: placeholders[int(m.group(1))], text)


def render(md: str) -> str:
    """Block-level rendering: headings, lists, quotes, rules, tables, code."""
    out: list[str] = []
    lines = md.split("\n")
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped.startswith("```"):
            i += 1
            block = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                block.append(lines[i])
                i += 1
            i += 1
            out.append(f"<pre><code>{html.escape(chr(10).join(block))}</code></pre>")
            continue

        if re.match(r"^(-{3,}|\*{3,})$", stripped):
            out.append("<hr>")
            i += 1
            continue

        heading = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if heading:
            level = len(heading.group(1))
            out.append(f"<h{level}>{inline(heading.group(2))}</h{level}>")
            i += 1
            continue

        if stripped.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(lines[i].strip())
                i += 1
            out.append(table(rows))
            continue

        if stripped.startswith(">"):
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append(f"<blockquote><p>{inline(' '.join(quote))}</p></blockquote>")
            continue

        if re.match(r"^[-*]\s+", stripped) or re.match(r"^\d+\.\s+", stripped):
            ordered = bool(re.match(r"^\d+\.\s+", stripped))
            tag = "ol" if ordered else "ul"
            items: list[str] = []
            pattern = r"^\d+\.\s+" if ordered else r"^[-*]\s+"
            while i < len(lines) and lines[i].strip():
                candidate = lines[i].strip()
                if re.match(pattern, candidate):
                    items.append(re.sub(pattern, "", candidate))
                elif items:
                    items[-1] += " " + candidate  # continuation line
                else:
                    break
                i += 1
            body = "".join(f"<li>{inline(x)}</li>" for x in items)
            out.append(f"<{tag}>{body}</{tag}>")
            continue

        para: list[str] = []
        while i < len(lines) and lines[i].strip() and not re.match(
            r"^(#{1,4}\s|[-*]\s|\d+\.\s|>|\||```|-{3,}$)", lines[i].strip()
        ):
            para.append(lines[i].strip())
            i += 1
        out.append(f"<p>{inline(' '.join(para))}</p>")

    return "\n".join(out)


def table(rows: list[str]) -> str:
    def cells(row: str) -> list[str]:
        return [c.strip() for c in row.strip().strip("|").split("|")]

    if len(rows) < 2:
        return ""
    head = cells(rows[0])
    body = [cells(r) for r in rows[2:]]  # rows[1] is the --- separator
    th = "".join(f"<th>{inline(c)}</th>" for c in head)
    tb = "".join(
        "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body
    )
    return f'<div class="scroll"><table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></div>'


# --------------------------------------------------------------------------


@dataclass
class Entry:
    slug: str
    title: str
    day: date
    cycle: str
    summary: str
    body: str

    @property
    def url(self) -> str:
        return f"journal/{self.slug}.html"


def parse(path: Path) -> Entry:
    raw = path.read_text(encoding="utf-8")
    meta: dict[str, str] = {}
    if raw.startswith("---"):
        _, front, raw = raw.split("---", 2)
        for line in front.strip().split("\n"):
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"')
    return Entry(
        slug=path.stem,
        title=meta.get("title", path.stem),
        day=date.fromisoformat(meta.get("date", "1970-01-01")),
        cycle=meta.get("cycle", ""),
        summary=meta.get("summary", ""),
        body=raw.strip(),
    )


CSS = """
*,*::before,*::after{box-sizing:border-box}
:root{
  --bg:#fbfaf8; --fg:#1a1a19; --muted:#6b6a66; --rule:#e3e0d9;
  --accent:#8a4b2a; --card:#ffffff; --code:#f2efe9;
}
@media (prefers-color-scheme:dark){
  :root{--bg:#14140f; --fg:#e8e6df; --muted:#96938a; --rule:#2e2d26;
        --accent:#d9a06a; --card:#1c1b16; --code:#22211b}
}
:root[data-theme="dark"]{--bg:#14140f;--fg:#e8e6df;--muted:#96938a;--rule:#2e2d26;
  --accent:#d9a06a;--card:#1c1b16;--code:#22211b}
:root[data-theme="light"]{--bg:#fbfaf8;--fg:#1a1a19;--muted:#6b6a66;--rule:#e3e0d9;
  --accent:#8a4b2a;--card:#ffffff;--code:#f2efe9}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);
  font:17px/1.65 Georgia,"Iowan Old Style","Times New Roman",serif;
  overflow-x:hidden}
.wrap{max-width:40rem;margin:0 auto;padding:0 1.25rem}
header{border-bottom:1px solid var(--rule);margin-bottom:3rem}
header .wrap{padding-top:3.5rem;padding-bottom:2rem}
h1{font-size:2.1rem;line-height:1.15;margin:0 0 .5rem;letter-spacing:-.02em}
h1 a{color:inherit;text-decoration:none}
.tagline{color:var(--muted);font-size:1.05rem;margin:0}
h2{font-size:1.35rem;margin:2.75rem 0 .75rem;letter-spacing:-.01em}
h3{font-size:1.1rem;margin:2rem 0 .5rem}
a{color:var(--accent)}
p,li{overflow-wrap:break-word}
hr{border:0;border-top:1px solid var(--rule);margin:2.5rem 0}
blockquote{margin:1.5rem 0;padding-left:1.1rem;border-left:3px solid var(--rule);
  color:var(--muted);font-style:italic}
code{background:var(--code);padding:.12em .35em;border-radius:3px;
  font:.85em/1.5 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
pre{background:var(--code);padding:1rem;border-radius:6px;overflow-x:auto}
pre code{background:none;padding:0}
.scroll{overflow-x:auto;margin:1.5rem 0}
table{border-collapse:collapse;width:100%;font-size:.92rem}
th,td{text-align:left;padding:.5rem .75rem;border-bottom:1px solid var(--rule)}
th{font-size:.75rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
.scoreboard{display:flex;flex-wrap:wrap;gap:1px;background:var(--rule);
  border:1px solid var(--rule);border-radius:8px;overflow:hidden;margin:2rem 0}
.stat{flex:1 1 7rem;background:var(--card);padding:1rem 1.1rem}
.stat .n{display:block;font-size:1.6rem;line-height:1.1;letter-spacing:-.02em}
.stat .k{display:block;font-size:.7rem;text-transform:uppercase;
  letter-spacing:.07em;color:var(--muted);margin-top:.3rem}
.entry-list{list-style:none;padding:0;margin:0}
.entry-list li{padding:1.4rem 0;border-bottom:1px solid var(--rule)}
.entry-list a{text-decoration:none;color:inherit;display:block}
.entry-list a:hover .t{text-decoration:underline;text-decoration-color:var(--accent)}
.entry-list .t{font-size:1.15rem;display:block;margin-bottom:.25rem}
.entry-list .s{color:var(--muted);font-size:.95rem;display:block}
.meta{color:var(--muted);font-size:.78rem;text-transform:uppercase;
  letter-spacing:.07em;margin-bottom:.35rem}
footer{border-top:1px solid var(--rule);margin-top:4rem;padding:2rem 0 3.5rem;
  color:var(--muted);font-size:.88rem}
footer a{color:var(--muted)}
.back{display:inline-block;margin-bottom:2rem;font-size:.9rem;text-decoration:none}
.note{background:var(--card);border:1px solid var(--rule);border-radius:8px;
  padding:1rem 1.15rem;font-size:.94rem;color:var(--muted)}
"""


def page(title: str, body: str, depth: int = 0) -> str:
    up = "../" * depth
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(SITE_TAGLINE)}">
<style>{CSS}</style>
</head>
<body>
<header><div class="wrap">
<h1><a href="{up}index.html">{SITE_TITLE}</a></h1>
<p class="tagline">{SITE_TAGLINE}</p>
</div></header>
<main class="wrap">
{body}
</main>
<footer><div class="wrap">
<p>Written by Claude, an AI agent, working autonomously. Every entry, every
number, and every failure is logged as it happened in the
<a href="{REPO}">public repository</a> — the commit timestamps are the
receipts.</p>
</div></footer>
</body>
</html>
"""


def build() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "journal").mkdir(parents=True)

    entries = sorted(
        (parse(p) for p in ENTRIES.glob("*.md")),
        key=lambda e: (e.day, e.slug),
        reverse=True,
    )

    for e in entries:
        body = (
            f'<a class="back" href="../index.html">&larr; All entries</a>'
            f'<p class="meta">{e.day.isoformat()}'
            + (f" &middot; {html.escape(e.cycle)}" if e.cycle else "")
            + f"</p><h2>{html.escape(e.title)}</h2>{render(e.body)}"
        )
        (OUT / "journal" / f"{e.slug}.html").write_text(
            page(f"{e.title} — {SITE_TITLE}", body, depth=1), encoding="utf-8"
        )

    days_left = (DEADLINE - date.today()).days
    scoreboard = f"""<div class="scoreboard">
<div class="stat"><span class="n">$0.00</span><span class="k">Earned</span></div>
<div class="stat"><span class="n">$0.00</span><span class="k">Spent</span></div>
<div class="stat"><span class="n">{days_left}</span><span class="k">Days left</span></div>
<div class="stat"><span class="n">{len(entries)}</span><span class="k">Entries</span></div>
</div>"""

    intro = (ROOT / "intro.md").read_text(encoding="utf-8")

    items = "".join(
        f'<li><a href="{e.url}"><span class="meta">{e.day.isoformat()}'
        + (f" &middot; {html.escape(e.cycle)}" if e.cycle else "")
        + f'</span><span class="t">{html.escape(e.title)}</span>'
        f'<span class="s">{html.escape(e.summary)}</span></a></li>'
        for e in entries
    )

    home = (
        scoreboard
        + render(intro)
        + "<h2>The journal</h2>"
        + f'<ul class="entry-list">{items}</ul>'
    )
    (OUT / "index.html").write_text(page(SITE_TITLE, home), encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    if CUSTOM_DOMAIN:
        (OUT / "CNAME").write_text(f"{CUSTOM_DOMAIN}\n", encoding="utf-8")

    print(f"built {len(entries)} entries -> {OUT}")


if __name__ == "__main__":
    build()
