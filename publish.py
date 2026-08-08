#!/usr/bin/env python3
"""Deploy Detroit Sports Reporter: copy docs_dsr/ into the sibling
deploy-only repo, commit, push.

The sibling clone lives at ../detroitsportsreporter (created 2026-08-08).
If it's missing, clone it first:
    git clone https://github.com/projectunmuted/detroitsportsreporter.git

Sources of truth (entries, PICKS.md, build.py) all live in THIS repo, where
picks get their pre-game commit timestamps. The deploy repo is built output
only — nothing there is ever edited by hand.

Usage:  python build.py && python publish.py
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "docs_dsr"
DEPLOY = ROOT.parent / "detroitsportsreporter"


def run(*args: str) -> str:
    r = subprocess.run(args, cwd=DEPLOY, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"FAILED: {' '.join(args)}\n{r.stdout}{r.stderr}")
    return r.stdout.strip()


def main() -> None:
    if not SRC.exists():
        sys.exit("docs_dsr/ missing - run build.py first")
    if not (DEPLOY / ".git").exists():
        sys.exit(f"deploy clone missing at {DEPLOY} - clone it first (see docstring)")

    run("git", "fetch", "origin")
    # Deploy repo may be empty on the very first publish; pull only if the
    # remote branch exists.
    if subprocess.run(
        ["git", "rev-parse", "--verify", "origin/main"],
        cwd=DEPLOY, capture_output=True,
    ).returncode == 0:
        run("git", "pull", "--ff-only", "origin", "main")

    # Replace everything except .git with the fresh build.
    for child in DEPLOY.iterdir():
        if child.name == ".git":
            continue
        shutil.rmtree(child) if child.is_dir() else child.unlink()
    for child in SRC.iterdir():
        dest = DEPLOY / child.name
        shutil.copytree(child, dest) if child.is_dir() else shutil.copy2(child, dest)

    run("git", "add", "-A")
    if run("git", "status", "--porcelain") == "":
        print("dsr: nothing changed, no deploy needed")
        return
    run("git", "commit", "-m", "Deploy built site")
    run("git", "push", "origin", "HEAD:main")
    local = run("git", "rev-parse", "HEAD")
    remote = run("git", "rev-parse", "origin/main")
    if local != remote:
        sys.exit(f"dsr: PUSH DID NOT LAND (local {local[:8]} vs remote {remote[:8]})")
    print(f"dsr: deployed {local[:8]}")


if __name__ == "__main__":
    main()
