#!/usr/bin/env bash
# Status: 🟢 verified by an independent review agent (2026-08-29) — awaiting Julio's ⚪️ confirmation.
# Idempotent bootstrap for the DnD Shiny toolkit development environment.
# Builds the unified repo-root .venv from the image's Python and installs deps.
set -euo pipefail

cd "$(dirname "$0")/.."

# One environment, rebuilt from requirements.txt (the project's single .venv).
if [ ! -d .venv ]; then
  python3 -m venv .venv
fi

./.venv/bin/python -m pip install --upgrade pip setuptools wheel
./.venv/bin/pip install -r requirements.txt
