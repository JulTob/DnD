.PHONY: run setup smoke-player safepoint install-hooks loss-check

PORT ?= 8080
VENV := .venv
SHINY := $(VENV)/bin/shiny
PIP := $(VENV)/bin/pip
VENV_PYTHON := $(VENV)/bin/python
PYTHON := $(PYTHON_BIN)

ifeq ($(PYTHON),)
PYTHON := $(shell command -v python3.14 2>/dev/null || command -v python3.13 2>/dev/null || command -v python3.12 2>/dev/null || command -v python3.11 2>/dev/null || command -v python3.10 2>/dev/null || command -v python3 2>/dev/null)
endif

run: setup
	$(SHINY) run --port $(PORT) shiny_app.py

setup: $(SHINY)

$(SHINY):
	@test -n "$(PYTHON)" || (echo "Python 3.10+ not found." && exit 1)
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip setuptools wheel
	$(PIP) install -r requirements.txt

smoke-player: setup
	$(VENV_PYTHON) -c "import shiny_app; from AtlasActorLudi.Map_of_Character_Generation import summon_player; p = summon_player(seed=42, level=1); print('smoke-player OK', getattr(p, 'name', p))"

safepoint:
	@chmod +x scripts/safepoint.sh
	@./scripts/safepoint.sh

install-hooks:
	@chmod +x scripts/install-git-hooks.sh scripts/git-hooks/pre-commit scripts/git-hooks/pre-push
	@./scripts/install-git-hooks.sh

loss-check:
	$(VENV_PYTHON) scripts/loss_detector.py --staged
