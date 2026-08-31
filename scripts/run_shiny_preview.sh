#!/bin/bash
# Launches the Shiny app via the venv's interpreter with -S (skips automatic
# site processing, which is what tries to read .venv/pyvenv.cfg and trips the
# preview sandbox's dotfile restriction). Site-packages are added by hand via
# PYTHONPATH instead.
#
# The repo root is wherever this script lives (main checkout or a worktree),
# so a recovery worktree previews its own tree, never its neighbour's.
# Beta root: shiny_app (Decree 0006, QST-0073). app.main returns with QST-0074.
REPO="$(cd "$(dirname "$0")/.." && pwd)"
VENV="/Users/tbs/Desktop/DnD/.venv"
cd "$REPO"
export PYTHONPATH="$REPO:$VENV/lib/python3.14/site-packages"
# Minion reports go to a plain-text log (QST-0079); the console stays for uvicorn.
export MINION_LOG="${MINION_LOG:-$REPO/minion_app.log}"
exec "$VENV/bin/python3" -S -m shiny run shiny_app:app --port "${PORT:-8000}"
