"""The application's stylesheet, read from its one true source (QST-0021.3).

`app/static/style.css` holds every rule — the old EXTRA_STYLE block from
shiny_app.py is folded at its foot, preserving the original cascade order.
This Scroll only reads and serves it; it never defines styles of its own.
"""

from __future__ import annotations

from pathlib import Path

from shiny import ui

STYLE_PATH = Path(__file__).resolve().parents[1] / "app" / "static" / "style.css"


def read_styles() -> str:
    """Return the full application stylesheet text ("" if the file is missing)."""
    if not STYLE_PATH.exists():
        return ""
    return STYLE_PATH.read_text(encoding="utf-8")


def style_tag() -> ui.Tag:
    """The single <style> head tag for the app."""
    return ui.tags.style(read_styles())


if __name__ == "__main__":
    # Self-test / usage demo. Run:  python AtlasVenustas/Scroll_of_Styles.py
    css = read_styles()
    assert css, f"stylesheet missing or empty at {STYLE_PATH}"
    assert ".npc-box" in css, "expected a known rule from the base sheet"
    assert "Folded from shiny_app.py EXTRA_STYLE" in css, "expected the folded block"
    print(f"Scroll_of_Styles: {len(css)} chars from {STYLE_PATH.name} — ok")
