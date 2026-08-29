"""Serve number spinner (+/-) behavior for pages outside the home tablet."""

from __future__ import annotations

from pathlib import Path

from shiny import ui


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "static"
    / "js"
    / "number-input.js"
    )
SCRIPT_URL = "/static/js/number-input.js"


def number_input_head_tags() -> list[ui.Tag]:
    """Return the script tag for the standalone number spinner."""
    return [
        ui.tags.script(
                src=SCRIPT_URL,
                ),
        ]


__all__ = [
    "SCRIPT_PATH",
    "SCRIPT_URL",
    "number_input_head_tags",
    ]
