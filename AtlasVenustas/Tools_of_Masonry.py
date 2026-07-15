"""Masonry packing for box grids (QST-0021.4).

The packer itself lives in `app/static/js/masonry.js`; this Kit only serves
the script tag. It packs `.npc-grid` and `.spellcaster-box` — the NPC sheet
left the grid with QST-0008, so today its clients are the spellcaster boxes
(retire the Kit when QST-0026 moves those to prose).
"""

from __future__ import annotations

from pathlib import Path

from shiny import ui

SCRIPT_PATH = Path(__file__).resolve().parents[1] / "app" / "static" / "js" / "masonry.js"
SCRIPT_URL = "/static/js/masonry.js"


def masonry_head_tags() -> list[ui.Tag]:
    """Script tag(s) to enable grid masonry, served from static assets."""
    return [ui.tags.script(src=SCRIPT_URL)]


if __name__ == "__main__":
    # Self-test / usage demo. Run:  python AtlasVenustas/Tools_of_Masonry.py
    assert SCRIPT_PATH.exists(), f"missing {SCRIPT_PATH}"
    script = SCRIPT_PATH.read_text(encoding="utf-8")
    assert ".spellcaster-box" in script, "expected the grid selector"
    assert "data-masonry" in script, "expected the masonry marker attribute"
    tags = masonry_head_tags()
    assert len(tags) == 1
    print(f"Tools_of_Masonry: serves {SCRIPT_URL} ({len(script)} chars) — ok")
