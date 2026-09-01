"""Shiny frontline for an Alusoris NonPlayer list."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from shiny import reactive
from shiny import render
from shiny import ui

from app.client import Client_Messages
from app.components.shared import safe_str
from app.navigation import Navigator
from app.navigation import Page
from app.session import Session_State


LIST_SIZE = 5
Summon_NonPlayer_List = Callable[..., list[Any]]
Open_NonPlayer = Callable[[Any], None]


def page_ui(
        ):
    """Build the NPC list page."""
    return ui.div(
            {"class": "main-content"},
            ui.h2(
                    {"class": "page-title"},
                    "Legendary NPC List",
                    ),
            ui.output_ui(
                    "npc_list_result"
                    ),
            ui.tags.br(),
            ui.input_action_button(
                    "btn_gen_list_again",
                    "5 New NPCs",
                    class_="fantasy-button",
                    ),
            )


def _selection_or_none(
        value: Any,
        ) -> str | None:
    if not value or value == "Random":
        return None
    return value


def _identity_summary(
        character: Any,
        ) -> str:
    fields = (
            "race",
            "char_class",
            "background",
            )
    return " · ".join(
            safe_str(
                    getattr(
                            character,
                            field,
                            "-",
                            )
                    )
            for field in fields
            )


def mount_page(
        input: Any,
        output: Any,
        *,
        state: Session_State,
        navigator: Navigator,
        client: Client_Messages,
        summon_nonplayer_list: Summon_NonPlayer_List,
        open_nonplayer: Open_NonPlayer,
        ) -> None:
    """Bind list controls to the Alusoris batch production route."""

    def generate(
            *,
            race,
            guild,
            background,
            ) -> None:
        client.set_loader(
                "show"
                )
        try:
            try:
                characters = summon_nonplayer_list(
                        race=race,
                        guild=guild,
                        background=background,
                        count=LIST_SIZE,
                        )
                state.nonplayer_list.set(
                        characters
                        )
                state.nonplayer_list_error.set(
                        None
                        )
                navigator.show(
                        Page.ACTOR_LUDI_ALUSORIS_LIST
                        )
            except Exception as error:
                state.nonplayer_list_error.set(
                        str(
                                error
                                )
                        )
                navigator.show(
                        Page.ACTOR_LUDI_ALUSORIS_LIST
                        )
        finally:
            client.set_loader(
                    "hide"
                    )

    @reactive.effect
    @reactive.event(
            input.go_npclist
            )
    def open_page(
            ) -> None:
        navigator.show(
                Page.ACTOR_LUDI_ALUSORIS_LIST
                )

    @reactive.effect
    @reactive.event(
            input.btn_gen_list
            )
    def generate_from_home(
            ) -> None:
        race = _selection_or_none(
                input.npc_race()
                )
        guild = _selection_or_none(
                input.npc_class()
                )
        background = _selection_or_none(
                input.npc_background()
                )
        state.nonplayer_race.set(
                race
                )
        state.nonplayer_background.set(
                background
                )
        state.nonplayer_guild.set(
                guild
                )
        generate(
                race=race,
                guild=guild,
                background=background,
                )

    @reactive.effect
    @reactive.event(
            input.btn_gen_list_again
            )
    def generate_again(
            ) -> None:
        generate(
                race=state.nonplayer_race(),
                guild=state.nonplayer_guild(),
                background=state.nonplayer_background(),
                )

    def open_from_list(
            index: int,
            ) -> None:
        characters = state.nonplayer_list()
        if not characters or index >= len(
                characters
                ):
            return
        open_nonplayer(
                characters[index]
                )

    for list_index in range(
            LIST_SIZE
            ):
        @reactive.effect
        @reactive.event(
                getattr(
                        input,
                        f"npc_list_open_{list_index}",
                        )
                )
        def open_listed_nonplayer(
                index=list_index,
                ) -> None:
            open_from_list(
                    index
                    )

    @output
    @render.ui
    def npc_list_result(
            ):
        error = state.nonplayer_list_error()
        if error:
            return ui.div(
                    {"class": "fallback-card"},
                    ui.h3(
                            "NPC list generation failed"
                            ),
                    ui.p(
                            error
                            ),
                    )
        characters = state.nonplayer_list()
        if not characters:
            return ui.div(
                    {"class": "fallback-card"},
                    ui.p(
                            "Generate 5 NPCs from Home."
                            ),
                    )
        rows = []
        for index, character in enumerate(
                characters[:LIST_SIZE]
                ):
            rows.append(
                    ui.input_action_link(
                            f"npc_list_open_{index}",
                            ui.TagList(
                                    ui.h1(
                                            ui.tags.i(
                                                    safe_str(
                                                            getattr(
                                                                    character,
                                                                    "name",
                                                                    "Unknown",
                                                                    )
                                                            )
                                                    )
                                            ),
                                    ui.h2(
                                            safe_str(
                                                    getattr(
                                                            character,
                                                            "title",
                                                            "",
                                                            )
                                                    )
                                            ),
                                    ui.h3(
                                            _identity_summary(
                                                    character
                                                    )
                                            ),
                                    ),
                            style="color: inherit; text-decoration: none;",
                            )
                    )
        return ui.div(
                {
                    "class": "npc-list",
                    "style": (
                        "display: flex; flex-direction: column; "
                        "gap: 1.3em; font-size: 1.1em; padding-top: 1em;"
                        ),
                    },
                *rows,
                )


__all__ = (
        "LIST_SIZE",
        "mount_page",
        "page_ui",
        )
