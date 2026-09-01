"""Serve character share-link behavior from the static assets."""

from __future__ import annotations

from pathlib import Path

from shiny import ui


SCRIPT_PATH = (
        Path(
                __file__
                ).resolve().parents[1]
        / "static"
        / "js"
        / "shareable-links.js"
        )
SCRIPT_URL = "/static/js/shareable-links.js"


def shareable_links_head_tags(
        ) -> list[ui.Tag]:
    version = int(
            SCRIPT_PATH.stat().st_mtime
            ) if SCRIPT_PATH.exists() else 0
    return [
            ui.tags.script(
                    src=f"{SCRIPT_URL}?v={version}"
                    ),
            ]


__all__ = [
        "SCRIPT_PATH",
        "SCRIPT_URL",
        "shareable_links_head_tags",
        ]
