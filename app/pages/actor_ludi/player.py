"""Shiny frontline for the Actor Ludi Player sheet."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from shiny import reactive
from shiny import render
from shiny import ui

from app.character_url import character_params_to_hash
from app.character_url import parse_character_params_from_url
from app.client import Client_Messages
from app.components import build_character_sheet
from app.components.shared import safe_int
from app.navigation import Navigator
from app.navigation import Page
from app.session import Session_State


Summon_Player = Callable[..., Any]


def page_ui(
        species_choices,
        class_choices,
        background_choices,
        ):
    """Build the character page from choices supplied by the app."""
    return ui.div(
            ui.h2(
                    {"class": "page-title"},
                    "Character Sheet",
                    ),
            ui.div(
                    {"class": "character-reforge"},
                    ui.div(
                            {
                                    "class": (
                                        "character-reforge-field "
                                        "character-reforge-field--species"
                                        )
                                    },
                            ui.input_select(
                                    "char_sheet_species",
                                    "",
                                    species_choices,
                                    selected="Random",
                                    ),
                            ),
                    ui.div(
                            {
                                    "class": (
                                        "character-reforge-field "
                                        "character-reforge-field--background"
                                        )
                                    },
                            ui.input_select(
                                    "char_sheet_background",
                                    "",
                                    background_choices,
                                    selected="Random",
                                    ),
                            ),
                    ui.div(
                            {
                                    "class": (
                                        "character-reforge-field "
                                        "character-reforge-field--class"
                                        )
                                    },
                            ui.input_select(
                                    "char_sheet_class",
                                    "",
                                    class_choices,
                                    selected="Random",
                                    ),
                            ui.input_select(
                                    "char_sheet_specialization",
                                    "",
                                    ("Random",),
                                    selected="Random",
                                    ),
                            ),
                    ui.div(
                            {"class": "character-level-box"},
                            ui.div(
                                    {"class": "character-level-value"},
                                    ui.output_text(
                                            "char_level_display",
                                            inline=True,
                                            ),
                                    ),
                            ui.tags.div(
                                    {"class": "character-level-controls"},
                                    ui.input_action_button(
                                            "btn_char_level_down",
                                            "-",
                                            class_="minus fantasy-button fantasy-input",
                                            title="Level Down",
                                            aria_label="Level Down",
                                            ),
                                    ui.input_action_button(
                                            "btn_char_level_up",
                                            "+",
                                            class_="plus fantasy-button fantasy-input",
                                            title="Level Up",
                                            aria_label="Level Up",
                                            ),
                                    ),
                            ),
                    ui.div(
                            {"class": "character-generate-wrap"},
                            ui.input_action_button(
                                    "btn_char_apply_selectors",
                                    "Generate",
                                    class_="fantasy-button",
                                    ),
                            ),
                    ui.div(
                            {"class": "character-share-wrap"},
                            ui.input_action_button(
                                    "btn_copy_char_link",
                                    "Share",
                                    class_="fantasy-button share-button",
                                    ),
                            ),
                    ui.tags.span(
                            {
                                    "id": "share-copy-status",
                                    "class": (
                                        "share-copy-status "
                                        "character-reforge-status"
                                        ),
                                    "aria-live": "polite",
                                    },
                            ),
                    ),
            ui.hr(),
            ui.output_ui(
                    "character_result",
                    ),
            )


def _selection_or_none(
        value: Any,
        ) -> str | None:
    if not value or value == "Random":
        return None
    return value


def _clean_parameter(
        value: Any,
        ) -> str | None:
    if value is None:
        return None
    return _selection_or_none(
            str(value).strip()
            )


def _specialization_options(
        catalogue,
        guild,
        ):
    return tuple(
            ["Random"]
            + list(
                    catalogue.get(
                            guild,
                            (),
                            )
                    )
            )


def _specialization_selection(
        current,
        selected_guild,
        available,
        ):
    if current.get("char_class") != selected_guild:
        return "Random"
    specialization = current.get("specialization")
    if specialization in available:
        return specialization
    return "Random"


def _parameters_from_data(
        data,
        fallback=None,
        ):
    base = fallback or {}
    payload = data or {}
    level = max(
            1,
            min(
                    20,
                    safe_int(
                            payload.get(
                                    "Level",
                                    base.get("level", 1),
                                    ),
                            1,
                            ),
                    ),
            )
    seed_value = payload.get(
            "Seed",
            payload.get(
                    "seed",
                    base.get("seed"),
                    ),
            )
    try:
        seed = (
                int(seed_value)
                if seed_value is not None
                else None
                )
    except (
            TypeError,
            ValueError,
            ):
        seed = None
    return {
            "species": _clean_parameter(
                    payload.get(
                            "Species",
                            base.get("species"),
                            )
                    ),
            "char_class": _clean_parameter(
                    payload.get(
                            "Class",
                            base.get("char_class"),
                            )
                    ),
            "specialization": _clean_parameter(
                    payload.get(
                            "Specialization",
                            base.get("specialization"),
                            )
                    ),
            "background": _clean_parameter(
                    payload.get(
                            "Background",
                            base.get("background"),
                            )
                    ),
            "level": level,
            "gender": _clean_parameter(
                    payload.get(
                            "Gender",
                            base.get("gender"),
                            )
                    ),
            "seed": seed,
            }


def mount_page(
        input: Any,
        output: Any,
        session: Any,
        *,
        state: Session_State,
        navigator: Navigator,
        client: Client_Messages,
        summon_player: Summon_Player,
        species_choices,
        guild_choices,
        specialization_choices,
        background_choices,
        ) -> None:
    """Bind Player inputs and outputs to the Actor Ludi production API."""
    valid_species = set(species_choices)
    valid_guilds = set(guild_choices)
    valid_backgrounds = set(background_choices)

    def selected_or_random(
            value,
            valid_values,
            ):
        if value in valid_values:
            return value
        return "Random"

    def apply_sheet_defaults(
            parameters,
            ):
        ui.update_select(
                "char_sheet_species",
                selected=selected_or_random(
                        parameters.get("species"),
                        valid_species,
                        ),
                )
        ui.update_select(
                "char_sheet_class",
                selected=selected_or_random(
                        parameters.get("char_class"),
                        valid_guilds,
                        ),
                )
        selected_guild = _selection_or_none(
                selected_or_random(
                        parameters.get("char_class"),
                        valid_guilds,
                        )
                )
        available_specializations = _specialization_options(
                specialization_choices,
                selected_guild,
                )
        ui.update_select(
                "char_sheet_specialization",
                choices=available_specializations,
                selected=selected_or_random(
                        parameters.get("specialization"),
                        set(available_specializations),
                        ),
                )
        ui.update_select(
                "char_sheet_background",
                selected=selected_or_random(
                        parameters.get("background"),
                        valid_backgrounds,
                        ),
                )

    def apply_home_defaults(
            parameters,
            ):
        ui.update_select(
                "char_species",
                selected=selected_or_random(
                        parameters.get("species"),
                        valid_species,
                        ),
                )
        ui.update_select(
                "char_class",
                selected=selected_or_random(
                        parameters.get("char_class"),
                        valid_guilds,
                        ),
                )
        ui.update_select(
                "char_background",
                selected=selected_or_random(
                        parameters.get("background"),
                        valid_backgrounds,
                        ),
                )
        apply_sheet_defaults(parameters)

    def push_url(
            parameters,
            ):
        if parameters.get("seed") is None:
            return None
        url_hash = character_params_to_hash(parameters)
        if url_hash:
            client.set_character_hash(url_hash)

    def generate(
            parameters,
            *,
            show_page=True,
            sync_home=False,
            ):
        try:
            character = summon_player(
                    species=parameters.get("species"),
                    guild=parameters.get("char_class"),
                    specialization=parameters.get("specialization"),
                    background=parameters.get("background"),
                    level=max(
                            1,
                            min(
                                    20,
                                    safe_int(
                                            parameters.get("level"),
                                            1,
                                            ),
                                    ),
                            ),
                    gender=parameters.get("gender"),
                    seed=parameters.get("seed"),
                    )
            data = character.to_dict()
            canonical = _parameters_from_data(
                    data,
                    fallback=parameters,
                    )
            state.player.set(data)
            state.player_parameters.set(canonical)
            state.player_error.set(None)
            apply_sheet_defaults(canonical)
            if sync_home:
                apply_home_defaults(canonical)
            push_url(canonical)
            if show_page:
                navigator.show(Page.ACTOR_LUDI_PLAYER)
        except Exception as error:
            state.player_error.set(str(error))
            if show_page:
                navigator.show(Page.ACTOR_LUDI_PLAYER)
        finally:
            client.set_loader("hide")

    @reactive.effect
    def update_specialization_selector(
            ):
        selected_guild = _selection_or_none(
                input.char_sheet_class()
                )
        available = _specialization_options(
                specialization_choices,
                selected_guild,
                )
        current = state.player_parameters() or {}
        selected = _specialization_selection(
                current,
                selected_guild,
                available,
                )
        ui.update_select(
                "char_sheet_specialization",
                choices=available,
                selected=selected_or_random(
                        selected,
                        set(available),
                        ),
                )

    @reactive.effect
    def initialize_from_url(
            ):
        if state.player_url_processed():
            return None
        pathname_source = getattr(
                session.clientdata,
                "url_pathname",
                None,
                )
        pathname = (
                pathname_source()
                if callable(pathname_source)
                else None
                )
        search = session.clientdata.url_search()
        hash_source = getattr(
                session.clientdata,
                "url_hash",
                None,
                )
        hash_value = (
                hash_source()
                if callable(hash_source)
                else None
                )
        parameters = parse_character_params_from_url(
                pathname,
                search,
                hash_value,
                )
        state.player_url_processed.set(True)
        if parameters is None:
            return None
        client.set_loader("show")
        generate(
                parameters,
                show_page=True,
                sync_home=True,
                )

    @reactive.effect
    @reactive.event(input.go_character)
    def open_fresh_player(
            ):
        state.player_url_processed.set(True)
        client.set_loader("show")
        generate(
                {"level": 1}
                )

    @reactive.effect
    @reactive.event(input.btn_gen_char)
    def generate_from_home(
            ):
        state.player_url_processed.set(True)
        client.set_loader("show")
        generate(
                {
                        "species": _selection_or_none(
                                input.char_species()
                                ),
                        "char_class": _selection_or_none(
                                input.char_class()
                                ),
                        "background": _selection_or_none(
                                input.char_background()
                                ),
                        "level": 1,
                        }
                )

    def change_level(
            difference,
            ):
        current = (
                state.player_parameters()
                or _parameters_from_data(
                        state.player()
                        )
                )
        current_level = max(
                1,
                min(
                        20,
                        safe_int(
                                current.get("level"),
                                1,
                                ),
                        ),
                )
        next_level = max(
                1,
                min(
                        20,
                        current_level + difference,
                        ),
                )
        if next_level == current_level or current.get("seed") is None:
            client.set_loader("hide")
            return None
        next_parameters = dict(current)
        next_parameters["level"] = next_level
        client.set_loader("show")
        generate(
                next_parameters,
                show_page=False,
                )

    @reactive.effect
    @reactive.event(input.btn_char_level_down)
    def level_down(
            ):
        change_level(-1)

    @reactive.effect
    @reactive.event(input.btn_char_level_up)
    def level_up(
            ):
        change_level(1)

    @reactive.effect
    @reactive.event(input.btn_char_apply_selectors)
    def apply_selectors(
            ):
        current = (
                state.player_parameters()
                or _parameters_from_data(
                        state.player()
                        )
                )
        client.set_loader("show")
        generate(
                {
                        "species": _selection_or_none(
                                input.char_sheet_species()
                                ),
                        "char_class": _selection_or_none(
                                input.char_sheet_class()
                                ),
                        "specialization": _selection_or_none(
                                input.char_sheet_specialization()
                                ),
                        "background": _selection_or_none(
                                input.char_sheet_background()
                                ),
                        "gender": current.get("gender"),
                        "level": max(
                                1,
                                min(
                                        20,
                                        safe_int(
                                                current.get("level"),
                                                1,
                                                ),
                                        ),
                                ),
                        }
                )

    @output
    @render.text
    def char_level_display(
            ):
        current = (
                state.player_parameters()
                or _parameters_from_data(
                        state.player()
                        )
                )
        lvl = max(
                1,
                min(
                        20,
                        safe_int(
                                current.get("level"),
                                1,
                                ),
                        ),
                )
        return f"Level {lvl}"

    @output
    @render.ui
    def character_result(
            ):
        error = state.player_error()
        if error:
            return ui.div(
                    {"class": "fallback-card"},
                    ui.h3("Character generation failed"),
                    ui.p(error),
                    )
        data = state.player()
        if not data:
            return ui.div(
                    {"class": "fallback-card"},
                    ui.p("Generate a character from Home."),
                    )
        return build_character_sheet(data)


__all__ = (
        "mount_page",
        "page_ui",
        )
