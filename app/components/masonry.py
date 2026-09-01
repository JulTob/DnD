"""Serve the masonry helper from the application's static assets."""

from __future__ import annotations

from pathlib import Path

from shiny import ui


SCRIPT_PATH = (
        Path(
                __file__
                ).resolve().parents[1]
        / "static"
        / "js"
        / "masonry.js"
        )
SCRIPT_URL = "/static/js/masonry.js"


def masonry_head_tags(
        ) -> list[ui.Tag]:
    return [
            ui.tags.script(
                    src=SCRIPT_URL
                    ),
            ]


__all__ = [
        "SCRIPT_PATH",
        "SCRIPT_URL",
        "masonry_head_tags",
        ]
