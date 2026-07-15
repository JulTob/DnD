"""Client wiring for character share links (QST-0021.6).

The logic lives in `app/static/js/shareable-links.js`: canonical paths,
hash sync via Shiny custom messages, copy-to-clipboard, share status UI.
This Kit only serves the script tag.

The boundary (per the ticket): hash encode/decode algorithms and the
`/character/...` ASGI redirect stay server-side in `app/character_url.py`
and `shiny_app.py` — never here.
"""

from __future__ import annotations

from pathlib import Path

from shiny import ui

SCRIPT_PATH = Path(__file__).resolve().parents[1] / "app" / "static" / "js" / "shareable-links.js"
SCRIPT_URL = "/static/js/shareable-links.js"


def shareable_links_head_tags() -> list[ui.Tag]:
    """Script tag(s) for character hash URLs and copy-to-clipboard."""
    return [ui.tags.script(src=SCRIPT_URL)]


if __name__ == "__main__":
    # Self-test / usage demo. Run:  python AtlasVenustas/Tools_of_ShareableLinks.py
    assert SCRIPT_PATH.exists(), f"missing {SCRIPT_PATH}"
    script = SCRIPT_PATH.read_text(encoding="utf-8")
    assert "canonicalPath" in script, "expected the canonical path helper"
    assert "clipboard" in script.lower(), "expected the clipboard logic"
    tags = shareable_links_head_tags()
    assert len(tags) == 1
    print(f"Tools_of_ShareableLinks: serves {SCRIPT_URL} ({len(script)} chars) — ok")
