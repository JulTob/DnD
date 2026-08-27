#!/usr/bin/env bash
# Idempotent bootstrap for the DnD Shiny toolkit development environment.
# Creates the unified repo-root virtual environment and installs dependencies.
set -euo pipefail

cd "$(dirname "$0")/.."

# The base image ships python3.12 but omits the venv/ensurepip module.
if ! python3 -c "import ensurepip" >/dev/null 2>&1; then
  sudo apt-get update -qq
  sudo apt-get install -y python3.12-venv
fi

# Unified repo-root virtual environment (QST-0004 / Decree 0001).
if [ ! -d .venv ]; then
  python3 -m venv .venv
fi

./.venv/bin/python -m pip install --upgrade pip setuptools wheel
./.venv/bin/pip install -r requirements.txt
