"""Serve the Great Old One text effect from the application's static assets."""

from __future__ import annotations

from pathlib import Path

from shiny import ui


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "static"
    / "js"
    / "eldritch.js"
    )
SCRIPT_URL = "/static/js/eldritch.js"


def eldritch_head_tags() -> list[ui.Tag]:
    """Return the script tag that animates Great Old One patron text."""
    return [
        ui.tags.script(
                src=SCRIPT_URL,
                ),
        ]


__all__ = [
    "SCRIPT_PATH",
    "SCRIPT_URL",
    "eldritch_head_tags",
    ]
