#!/bin/bash
# Launches the Shiny app for the preview pane from whichever checkout this
# script lives in (main checkout or a worktree), so the sandbox never has to
# reach outside it. The interpreter runs with -S (no automatic site
# processing, which would read .venv/pyvenv.cfg and trip the sandbox's
# dotfile restriction); site-packages are added by hand via PYTHONPATH.
#
# A checkout with its own .venv uses it; a worktree without one borrows the
# main checkout's venv, which `make setup` creates.
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VENV="${ROOT}/.venv"
if [[ ! -x "${VENV}/bin/python3" ]]; then
	VENV="$(git -C "${ROOT}" rev-parse --path-format=absolute --git-common-dir 2>/dev/null | sed 's#/\.git$##')/.venv"
fi
SITE="$(ls -d "${VENV}"/lib/python3.*/site-packages 2>/dev/null | head -1)"
cd "${ROOT}"
export PYTHONPATH="${ROOT}:${SITE}"
exec "${VENV}/bin/python3" -S -m shiny run app.main:app --port "${PORT:-8000}"
