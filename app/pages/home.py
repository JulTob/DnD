"""Home generator page layout."""

from shiny import ui


def page_ui(
        species_choices,
        class_choices,
        background_choices,
        race_choices,
        nonplayer_guild_choices,
        nonplayer_background_choices,
        ):
    """Build the home page from choices supplied by the app composition root."""
    return ui.div(
            {"class": "main-content"},
            ui.h2(
                    "Welcome to Gen Legend"
                    ),
            ui.p(
                    "Generate legendary Characters and Non-Player "
                    "Characters for your next adventure."
                    ),
            ui.div(
                    {
                        "id": "generator-tablet",
                        "class": "tablet-wrapper",
                        },
                    ui.div(
                            {"class": "tablet-controls"},
                            ui.tags.button(
                                    {
                                        "class": "tablet-nav prev fantasy-button",
                                        "type": "button",
                                        "aria-label": "Previous generator",
                                        "style": (
                                            "min-width:2.2em; "
                                            "min-height:2.2em; "
                                            "width:2.2em; "
                                            "height:2.2em; "
                                            "font-size:1.3em; "
                                            "line-height:1em; "
                                            "padding:0; "
                                            "display:inline-flex; "
                                            "align-items:center; "
                                            "justify-content:center;"
                                            ),
                                        },
                                    ui.HTML(
                                            "<span aria-hidden='true' "
                                            "style='display:block;'>"
                                            "&#x2039;</span>"
                                            ),
                                    ),
                            ui.h3(
                                    {
                                        "id": "tablet-title",
                                        "class": "tablet-title",
                                        },
                                    "NPC Generator",
                                    ),
                            ui.tags.button(
                                    {
                                        "class": "tablet-nav next fantasy-button",
                                        "type": "button",
                                        "aria-label": "Next generator",
                                        "style": (
                                            "min-width:2.2em; "
                                            "min-height:2.2em; "
                                            "width:2.2em; "
                                            "height:2.2em; "
                                            "font-size:1.3em; "
                                            "line-height:1em; "
                                            "padding:0; "
                                            "display:inline-flex; "
                                            "align-items:center; "
                                            "justify-content:center;"
                                            ),
                                        },
                                    ui.HTML(
                                            "<span aria-hidden='true' "
                                            "style='display:block;'>"
                                            "&#x203A;</span>"
                                            ),
                                    ),
                            ),
                    ui.div(
                            {"class": "tablet-viewport"},
                            ui.div(
                                    {"class": "tablet-rotator"},
                                    ui.tags.section(
                                            {
                                                "class": "generator-panel",
                                                "data-title": "Character Generator",
                                                },
                                            ui.h3(
                                                    "Generate Character"
                                                    ),
                                            ui.input_select(
                                                    "char_species",
                                                    "Species",
                                                    species_choices,
                                                    ),
                                            ui.input_select(
                                                    "char_class",
                                                    "Class",
                                                    class_choices,
                                                    ),
                                            ui.input_select(
                                                    "char_background",
                                                    "Background",
                                                    background_choices,
                                                    ),
                                            ui.div(
                                                    {"class": "tablet-actions"},
                                                    ui.input_action_button(
                                                            "btn_gen_char",
                                                            "Generate Character",
                                                            class_="fantasy-button",
                                                            ),
                                                    ),
                                            ),
                                    ui.tags.section(
                                            {
                                                "class": (
                                                    "generator-panel is-active"
                                                    ),
                                                "data-title": "NPC Generator",
                                                },
                                            ui.h3(
                                                    "Generate a Non Player Character"
                                                    ),
                                            ui.input_select(
                                                    "npc_race",
                                                    "Race",
                                                    race_choices,
                                                    ),
                                            ui.input_select(
                                                    "npc_class",
                                                    "Class",
                                                    nonplayer_guild_choices,
                                                    ),
                                            ui.input_select(
                                                    "npc_background",
                                                    "Background",
                                                    nonplayer_background_choices,
                                                    ),
                                            ui.div(
                                                    {"class": "tablet-actions"},
                                                    ui.input_action_button(
                                                            "btn_gen_npc",
                                                            "Generate NPC",
                                                            class_="fantasy-button",
                                                            ),
                                                    ui.input_action_button(
                                                            "btn_gen_list",
                                                            "Generate 5 NPCs",
                                                            class_="fantasy-button",
                                                            ),
                                                    ),
                                            ),
                                    ),
                            ),
                    ui.div(
                            {
                                "class": "tablet-dots",
                                "aria-label": "Generator navigation",
                                },
                            ),
                    ),
            )
