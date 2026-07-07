.PHONY: run setup

PORT ?= 8080
VENV := .venv
SHINY := $(VENV)/bin/shiny
PIP := $(VENV)/bin/pip
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
