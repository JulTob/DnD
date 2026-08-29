"""Shiny frontline for an Alusoris NonPlayer sheet."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from shiny import reactive, render, ui

from AtlasActorLudi.AtlasAlusoris import parse_nonplayer_path
from app.client import Client_Messages
from app.components import build_npc_sheet
from app.components.shared import safe_int
from app.navigation import Navigator, Page
from app.session import Session_State


Summon_NonPlayer = Callable[..., Any]
Optional_Renderer = Callable[[Any], Any]


def page_ui(
        race_choices,
        nonplayer_background_choices,
        ):
    """Build the NPC sheet page."""
    return ui.div(
            ui.h2(
                    {"class": "page-title"},
                    "NPC Sheet",
                    ),
            ui.div(
                    {"class": "npc-sheet-controls"},
                    ui.div(
                            {"class": "character-level-box npc-level-box"},
                            ui.div(
                                    {"class": "character-level-value"},
                                    ui.output_text(
                                            "npc_level_display",
                                            inline=True,
                                            ),
                                    ),
                            ui.tags.div(
                                    {"class": "character-level-controls"},
                                    ui.input_action_button(
                                            "btn_npc_level_down",
                                            "-",
                                            class_=(
                                                "minus fantasy-button "
                                                "fantasy-input"
                                                ),
                                            title="Level Down",
                                            aria_label="Level Down",
                                            ),
                                    ui.input_action_button(
                                            "btn_npc_level_up",
                                            "+",
                                            class_=(
                                                "plus fantasy-button "
                                                "fantasy-input"
                                                ),
                                            title="Level Up",
                                            aria_label="Level Up",
                                            ),
                                    ),
                            ),
                    ui.input_select(
                            "npc_sheet_race",
                            "Creature Type",
                            race_choices,
                            ),
                    ui.input_select(
                            "npc_sheet_archetype",
                            "Archetype",
                            nonplayer_background_choices,
                            ),
                    ui.input_action_button(
                            "btn_gen_npc_again",
                            "Reroll NPC",
                            class_="fantasy-button",
                            ),
                    ),
            ui.hr(),
            ui.output_ui(
                    "npc_result"
                    ),
            )


def _selection_or_none(
        value: str | None,
        ) -> str | None:
    if (
        not value
        or value == "Random"
        ):
        return None

    return value


def mount_page(
        input: Any,
        output: Any,
        session: Any,
        *,
        state: Session_State,
        navigator: Navigator,
        client: Client_Messages,
        summon_nonplayer: Summon_NonPlayer,
        legendary_renderer: Optional_Renderer | None = None,
        lair_renderer: Optional_Renderer | None = None,
        region_renderer: Optional_Renderer | None = None,
        ) -> None:
    """Bind Alusoris sheet controls to its public production route."""
    initial_url_processed = reactive.value(
            False
            )
    npc_level = reactive.value(
            1
            )

    def generate(
            *,
            race: str | None,
            background: str | None,
            level: int,
            seed: int | None = None,
            ) -> None:
        client.set_loader(
                "show"
                )

        try:
            character = summon_nonplayer(
                    race=race,
                    background=background,
                    level=level,
                    seed=seed,
                    )
            state.nonplayer.set(
                    character
                    )
            state.nonplayer_error.set(
                    None
                    )
            navigator.show(
                    Page.ACTOR_LUDI_ALUSORIS
                    )
        except Exception as error:
            state.nonplayer_error.set(
                    str(
                        error
                        )
                    )
            navigator.show(
                    Page.ACTOR_LUDI_ALUSORIS
                    )
        finally:
            client.set_loader(
                    "hide"
                    )

    @reactive.effect
    def initialize_from_url() -> None:
        if initial_url_processed():
            return

        pathname_source = getattr(
                session.clientdata,
                "url_pathname",
                None,
                )
        pathname = (
            pathname_source()
            if callable(
                pathname_source
                )
            else None
            )
        hash_source = getattr(
                session.clientdata,
                "url_hash",
                None,
                )
        hash_value = (
            hash_source()
            if callable(
                hash_source
                )
            else None
            )
        parameters = (
            parse_nonplayer_path(
                    hash_value
                    )
            or parse_nonplayer_path(
                    pathname
                    )
            )

        initial_url_processed.set(
                True
                )

        if parameters is None:
            return

        state.nonplayer_race.set(
                parameters[
                    "race"
                    ]
                )
        state.nonplayer_background.set(
                parameters[
                    "archetype"
                    ]
                )
        generate(
                race=parameters[
                    "race"
                    ],
                background=parameters[
                    "archetype"
                    ],
                level=parameters[
                    "level"
                    ],
                seed=parameters[
                    "seed"
                    ],
                )

    @reactive.effect
    @reactive.event(
            input.go_npc
            )
    def open_page() -> None:
        state.nonplayer_race.set(
                None
                )
        state.nonplayer_background.set(
                None
                )
        generate(
                race=None,
                background=None,
                level=5,
                )

    @reactive.effect
    @reactive.event(
            input.btn_gen_npc
            )
    def generate_from_home() -> None:
        race = _selection_or_none(
                input.npc_race()
                )
        background = _selection_or_none(
                input.npc_archetype()
                )

        state.nonplayer_race.set(
                race
                )
        state.nonplayer_background.set(
                background
                )

        generate(
                race=race,
                background=background,
                level=max(
                    1,
                    safe_int(
                        input.npc_level(),
                        5,
                        ),
                    ),
                )

    @reactive.effect
    @reactive.event(
            input.btn_gen_npc_again
            )
    def generate_again() -> None:
        race = _selection_or_none(
                input.npc_sheet_race()
                )
        background = _selection_or_none(
                input.npc_sheet_archetype()
                )

        state.nonplayer_race.set(
                race
                )
        state.nonplayer_background.set(
                background
                )

        generate(
                race=race,
                background=background,
                level=max(
                    1,
                    safe_int(
                        input.npc_sheet_level(),
                        5,
                        ),
                    ),
                )

    @output
    @render.ui
    def npc_result() -> ui.Tag:
        error = state.nonplayer_error()

        if error:
            return ui.div(
                    {"class": "fallback-card"},
                    ui.h3(
                            "NPC generation failed"
                            ),
                    ui.p(
                            error
                            ),
                    )

        character = state.nonplayer()

        if character is None:
            return ui.div(
                    {"class": "fallback-card"},
                    ui.p(
                            "Generate an NPC from Home."
                            ),
                    )

        return build_npc_sheet(
                character,
                legendary_renderer=legendary_renderer,
                lair_renderer=lair_renderer,
                region_renderer=region_renderer,
                )


__all__ = (
    "mount_page",
    "page_ui",
    )
