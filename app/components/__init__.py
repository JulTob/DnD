"""Stable presentation API for the Shiny application shell.

The loader, masonry, styles, symbols, and shareable-links helpers moved to
``AtlasVenustas`` (QST-0021); import them from there. ``npc_sheet`` is
accident-damaged and stays off this surface until QST-0075 restores the
NonPlayer wing.
"""

from app.components.character_sheet import build_character_sheet
from app.components.eldritch import eldritch_head_tags
from app.components.number_input import number_input_head_tags
from app.components.spellbook import known_spells_rail_box
from app.components.spellbook import spellcasting_chips
from app.components.tablet import tablet_head_tags


__all__ = [
    "build_character_sheet",
    "eldritch_head_tags",
    "known_spells_rail_box",
    "number_input_head_tags",
    "spellcasting_chips",
    "tablet_head_tags",
    ]
