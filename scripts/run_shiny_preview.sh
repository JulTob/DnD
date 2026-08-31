#!/bin/bash
# Launches the Shiny app via the venv's interpreter with -S (skips automatic
# site processing, which is what tries to read .venv/pyvenv.cfg and trips the
# preview sandbox's dotfile restriction). Site-packages are added by hand via
# PYTHONPATH instead.
cd /Users/tbs/Desktop/DnD
export PYTHONPATH="/Users/tbs/Desktop/DnD:/Users/tbs/Desktop/DnD/.venv/lib/python3.14/site-packages"
exec /Users/tbs/Desktop/DnD/.venv/bin/python3 -S -m shiny run shiny_app:app --port "${PORT:-8000}"
