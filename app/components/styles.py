"""Read the application's stylesheet from its single static source."""

from __future__ import annotations

from pathlib import Path

from shiny import ui


STYLE_PATH = (
        Path(
                __file__
                ).resolve().parents[1]
        / "static"
        / "style.css"
        )


def read_styles(
        ) -> str:
    if not STYLE_PATH.exists():
        return ""
    return STYLE_PATH.read_text(
            encoding="utf-8"
            )


def style_tag(
        ) -> ui.Tag:
    return ui.tags.style(
            read_styles()
            )


__all__ = [
        "STYLE_PATH",
        "read_styles",
        "style_tag",
        ]
