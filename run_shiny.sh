#!/usr/bin/env bash
set -euo pipefail

# Pick a Python interpreter.
# Prefer newer versions first; Python >=3.10 is required by project syntax.
PYTHON_BIN="${PYTHON_BIN:-}"

# If user passed PYTHON_BIN explicitly, validate it early.
if [[ -n "${PYTHON_BIN}" ]] && ! command -v "${PYTHON_BIN}" >/dev/null 2>&1; then
  echo "Requested interpreter not found: ${PYTHON_BIN}"
  echo "Install Python 3.10+ (recommended: 3.14), then rerun."
  echo "Example: brew install python@3.14"
  exit 1
fi

if [[ -z "${PYTHON_BIN}" ]]; then
  for candidate in python3.14 python3.13 python3.12 python3.11 python3.10 python3; do
    if command -v "${candidate}" >/dev/null 2>&1; then
      PYTHON_BIN="${candidate}"
      break
    fi
  done
fi

if [[ -z "${PYTHON_BIN}" ]]; then
  echo "No Python interpreter found. Install Python 3.10+ (recommended: 3.14)."
  exit 1
fi

PYTHON_OK="$("${PYTHON_BIN}" - <<'PY'
import sys
print("ok" if sys.version_info >= (3, 10) else "bad")
PY
)"

if [[ "${PYTHON_OK}" != "ok" ]]; then
  echo "Selected interpreter (${PYTHON_BIN}) is too old."
  "${PYTHON_BIN}" --version || true
  echo "Install Python 3.10+ (recommended: 3.14), then rerun."
  exit 1
fi

# If an existing venv is too old, ask for recreation.
if [[ -d ".venv" ]]; then
  VENV_OK="$("./.venv/bin/python" - <<'PY'
import sys
print("ok" if sys.version_info >= (3, 10) else "bad")
PY
  )"
  if [[ "${VENV_OK}" != "ok" ]]; then
    echo ".venv uses an older Python:"
    ./.venv/bin/python --version || true
    echo "Run: rm -rf .venv && ./run_shiny.sh"
    exit 1
  fi
fi

# Install dependencies if not present.
if [[ ! -d ".venv" ]]; then
  "${PYTHON_BIN}" -m venv .venv
fi

# Help source builds (e.g. Pillow) find Homebrew headers/libs on Apple Silicon.
if [[ -d "/opt/homebrew/include" ]] && [[ -d "/opt/homebrew/lib" ]]; then
  export CPPFLAGS="${CPPFLAGS:-} -I/opt/homebrew/include"
  export LDFLAGS="${LDFLAGS:-} -L/opt/homebrew/lib"
fi

./.venv/bin/python -m pip install --upgrade pip setuptools wheel || \
  echo "pip/setuptools/wheel upgrade skipped (continuing with existing versions)."
./.venv/bin/pip install -r requirements.txt

# Run the Shiny app. Use PORT=8081 (or any free port) if 8080 is in use.
SHINY_PORT="${PORT:-8080}"
./.venv/bin/shiny run --reload --port "$SHINY_PORT" shiny_app.py
