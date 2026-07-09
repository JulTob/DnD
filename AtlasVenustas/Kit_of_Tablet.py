"""The home generator tablet carousel (QST-0021.5).

The carousel logic lives in `app/static/js/tablet.js`; this Kit only serves
the script tag for the head. Markup stays with the home panel in the app.
"""

from __future__ import annotations

from pathlib import Path

from shiny import ui

SCRIPT_PATH = Path(__file__).resolve().parents[1] / "app" / "static" / "js" / "tablet.js"
SCRIPT_URL = "/static/js/tablet.js"


def tablet_head_tags() -> list[ui.Tag]:
    """Script tag(s) for the home generator tablet carousel."""
    return [ui.tags.script(src=SCRIPT_URL)]


if __name__ == "__main__":
    # Self-test / usage demo. Run:  python AtlasVenustas/Kit_of_Tablet.py
    assert SCRIPT_PATH.exists(), f"missing {SCRIPT_PATH}"
    script = SCRIPT_PATH.read_text(encoding="utf-8")
    assert "generator-tablet" in script, "expected the tablet wrapper id"
    tags = tablet_head_tags()
    assert len(tags) == 1
    print(f"Kit_of_Tablet: serves {SCRIPT_URL} ({len(script)} chars) — ok")
