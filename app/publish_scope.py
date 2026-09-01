"""First-publish frontline scope (Decree 0004).

The Atlas code for NonPlayer Characters, NPC lists, and the Dungeon Master
Companion stays in the tree. This module only parks their *chrome*.

Flip ``PLAYER_ONLY_PUBLISH`` to ``False`` to restore the NPC tablet face,
the NPC / NPC List / DM header buttons, and navigation to those pages.
"""

PLAYER_ONLY_PUBLISH = True

PARKED_PAGE_NAMES = frozenset(
        (
            "npc",
            "npclist",
            "dm",
            )
        )


def fantasy_button_class(
        *,
        parked: bool = False,
        ) -> str:
    if parked and PLAYER_ONLY_PUBLISH:
        return "fantasy-button is-parked"
    return "fantasy-button"


def tablet_wrapper_attrs() -> dict[str, str]:
    attrs = {
            "id": "generator-tablet",
            "class": "tablet-wrapper",
            }
    if PLAYER_ONLY_PUBLISH:
        attrs["class"] = "tablet-wrapper player-only-publish"
        attrs["data-player-only"] = "true"
    return attrs


def character_panel_class() -> str:
    if PLAYER_ONLY_PUBLISH:
        return "generator-panel is-active"
    return "generator-panel"


def npc_panel_class() -> str:
    if PLAYER_ONLY_PUBLISH:
        return "generator-panel is-parked"
    return "generator-panel is-active"


def home_welcome() -> str:
    if PLAYER_ONLY_PUBLISH:
        return (
            "Generate a legendary Character "
            "for your next adventure."
            )
    return (
        "Generate legendary Characters and Non-Player "
        "Characters for your next adventure."
        )


def tablet_title() -> str:
    if PLAYER_ONLY_PUBLISH:
        return "Character Generator"
    return "NPC Generator"


def published_page(
        page: str,
        ) -> str:
    """Keep parked destinations off the first-publish frontline."""
    if PLAYER_ONLY_PUBLISH and page in PARKED_PAGE_NAMES:
        return "home"
    return page


__all__ = (
        "PLAYER_ONLY_PUBLISH",
        "PARKED_PAGE_NAMES",
        "character_panel_class",
        "fantasy_button_class",
        "home_welcome",
        "npc_panel_class",
        "published_page",
        "tablet_title",
        "tablet_wrapper_attrs",
        )
