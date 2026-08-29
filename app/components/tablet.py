"""Serve the home generator tablet behavior from static assets."""

from __future__ import annotations

from pathlib import Path

from shiny import ui


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "static"
    / "js"
    / "tablet.js"
    )
SCRIPT_URL = "/static/js/tablet.js"


def tablet_head_tags() -> list[ui.Tag]:
    """Return the script tag for the generator tablet carousel."""
    return [
        ui.tags.script(
                src=SCRIPT_URL,
                ),
        ]


__all__ = [
    "SCRIPT_PATH",
    "SCRIPT_URL",
    "tablet_head_tags",
    ]
