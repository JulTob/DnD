"""Shiny frontline for the Dungeon Master Companion."""

from __future__ import annotations

from typing import Any, Callable, Protocol

from shiny import reactive, render, ui

from AtlasMagistratum import (
        bind_dm_character,
        briefing_for,
        dm_session_hash,
        draw_inspiration,
        parse_npc_or_dm_path,
        )


ShowPage = Callable[[str], None]
SetLoader = Callable[[str], None]
SendUrlHash = Callable[[str], None]
OpenNonplayer = Callable[[Any], None]
SafeInt = Callable[[Any, int], int]


class SummonNonplayer(Protocol):
    """Application callback used to produce one NonPlayer Character."""

    def __call__(
            self,
            *,
            race: str | None,
            guild: str | None = None,
            background: str | None,
            archetype: str | None = None,
            level: int,
            seed: int | None = None,
            ) -> Any:
        ...


def page_ui() -> ui.Tag:
    """Build the Dungeon Master Companion page."""
    return ui.div(
            {"class": "main-content"},
            ui.h2(
                    {"class": "page-title"},
                    "Dungeon Master Companion",
                    ),
            ui.p(
                    {"class": "dm-companion-lede"},
                    "Set a DM Character — Area and Lair lock from their Tags. They may be a villain, a Quest Master, a contested guardian, or another role you choose. Generate one inspiration card at a time. Presentation only; the table owns the rest.",
                    ),
            ui.div(
                    {"class": "npc-button-selectors"},
                    ui.input_numeric(
                            "dm_level",
                            "DM Character level",
                            value=5,
                            min=1,
                            max=20,
                            ),
                    ui.input_action_button(
                            "btn_gen_dm_character",
                            "Generate DM Character",
                            class_="fantasy-button",
                            ),
                    ui.input_action_button(
                            "btn_regen_dm_character",
                            "Regenerate DM Character",
                            class_="fantasy-button",
                            ),
                    ),
            ui.div(
                    {
                        "class": "npc-button-selectors",
                        "style": "margin-top: 0.75em;",
                        },
                    ui.input_text(
                            "dm_character_url",
                            "Import DM Character from NPC URL",
                            placeholder="/npc/Race/Class/Background/level/seed or full GenLegend NPC URL",
                            ),
                    ui.input_action_button(
                            "btn_import_dm_character",
                            "Import DM Character",
                            class_="fantasy-button",
                            ),
                    ui.input_action_button(
                            "btn_dm_open_character",
                            "Open DM Character sheet",
                            class_="fantasy-button",
                            ),
                    ),
            ui.div(
                    {
                        "class": "npc-button-selectors",
                        "style": "margin-top: 0.75em;",
                        },
                    ui.input_action_button(
                            "btn_gen_scene",
                            "Generate scene",
                            class_="fantasy-button",
                            ),
                    ),
            ui.hr(),
            ui.output_ui(
                    "dm_result"
                    ),
            )


def _links_to_dm_character(occupant: Any) -> bool:
    return bool(
            getattr(
                    occupant,
                    "link_dm_character",
                    False,
                    )
            or getattr(
                    occupant,
                    "link_bbeg",
                    False,
                    )
            or getattr(
                    occupant,
                    "link_master",
                    False,
                    )
            )


def _render_companion_result(
        *,
        error: str | None,
        briefing: str | None,
        scene: Any | None,
        path_url: str = "",
        ) -> ui.Tag:
    """Render the briefing, session URL, scene, and occupant links."""
    if error:
        return ui.div(
                {"class": "fallback-card"},
                ui.h3(
                        "DM Companion note"
                        ),
                ui.p(
                        error
                        ),
                )

    if not briefing:
        return ui.div(
                {"class": "fallback-card"},
                ui.p(
                        "Generate or import a DM Character to lock Area and Lair, then Generate scene."
                        ),
                )

    briefing_bits = [
            ui.p(
                    line
                    )
            if line.strip()
            else ui.br()
            for line in briefing.split(
                    "\n"
                    )
            ]

    blocks = [
            ui.div(
                    {"class": "dm-briefing prose-section"},
                    *briefing_bits,
                    )
            ]

    if path_url:
        blocks.append(
                ui.p(
                        {"class": "dm-path-url"},
                        "Session (share / bookmark): ",
                        ui.tags.code(
                                path_url
                                ),
                        )
                )

    if scene is not None:
        scene_bits = [
                ui.p(
                        line
                        )
                if line.strip()
                else ui.br()
                for line in scene.prose.split(
                        "\n"
                        )
                ]

        blocks.append(
                ui.hr()
                )
        blocks.append(
                ui.h3(
                        scene.title or "Inspiration"
                        )
                )
        blocks.append(
                ui.div(
                        {"class": "dm-passage prose-section"},
                        *scene_bits,
                        )
                )

        if scene.occupants:
            occupant_blocks = []

            for index, occupant in enumerate(
                    scene.occupants
                    ):
                occupant_bits = [
                        ui.p(
                                f"{occupant.kind}: {occupant.name}"
                                ),
                        ui.p(
                                {"style": "opacity: 0.95;"},
                                occupant.why_here,
                                ),
                        ui.p(
                                {
                                    "style": "font-size: 0.9em; opacity: 0.8;",
                                    },
                                "Trait, hook, and stats live on their sheet — open it; join threads yourself.",
                                ),
                        ]

                has_sheet = (
                    _links_to_dm_character(
                            occupant
                            )
                    or getattr(
                            occupant,
                            "npc_seed",
                            None,
                            )
                    is not None
                    )

                if has_sheet:
                    occupant_bits.append(
                            ui.input_action_button(
                                    f"dm_open_occ_{index}",
                                    f"Open {occupant.name}'s NPC sheet",
                                    class_="fantasy-button",
                                    )
                            )

                npc_url = getattr(
                        occupant,
                        "npc_url",
                        None,
                        )

                if npc_url:
                    occupant_bits.append(
                            ui.p(
                                    ui.tags.code(
                                            npc_url
                                            )
                                    )
                            )

                occupant_blocks.append(
                        ui.div(
                                {
                                    "class": "dm-occupant",
                                    "style": "margin: 0.8em 0;",
                                    },
                                *occupant_bits,
                                )
                        )

            blocks.append(
                    ui.h4(
                            "In this scene"
                            )
                    )
            blocks.append(
                    ui.div(
                            {"class": "dm-occupants"},
                            *occupant_blocks,
                            )
                    )

    return ui.div(
            {"class": "dm-result"},
            *blocks,
            )


def mount_page(
        input: Any,
        output: Any,
        session: Any,
        *,
        show_page: ShowPage,
        set_loader: SetLoader,
        send_url_hash: SendUrlHash,
        summon_nonplayer: SummonNonplayer,
        open_nonplayer: OpenNonplayer,
        safe_int: SafeInt,
        ) -> None:
    """Mount the Companion state, handlers, URL import, and result output."""
    briefing_state = reactive.value(
            None
            )
    scene_state = reactive.value(
            None
            )
    adventure_state = reactive.value(
            None
            )
    character_state = reactive.value(
            None
            )
    path_url_state = reactive.value(
            ""
            )
    error_state = reactive.value(
            None
            )
    initial_url_processed = reactive.value(
            False
            )

    def push_url(
            level: int,
            seed: int,
            ) -> None:
        path = dm_session_hash(
                level,
                seed,
                )
        path_url_state.set(
                "/" + path
                )
        send_url_hash(
                path
                )

    def set_dm_character(
            nonplayer: Any,
            *,
            level: int | None = None,
            ) -> None:
        adventure = bind_dm_character(
                nonplayer,
                level=level,
                )
        adventure_state.set(
                adventure
                )
        character_state.set(
                nonplayer
                )
        briefing_state.set(
                briefing_for(
                        adventure
                        )
                )
        scene_state.set(
                None
                )
        error_state.set(
                None
                )
        push_url(
                adventure.level,
                adventure.seed,
                )

    @reactive.effect
    @reactive.event(
            input.go_dm
            )
    def go_dm() -> None:
        show_page(
                "dm"
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
            if callable(pathname_source)
            else None
            )
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
        raw = pathname or ""

        if hash_value:
            raw = str(
                    hash_value
                    ).lstrip(
                    "#"
                    )
            if not raw.startswith(
                    "/"
                    ):
                raw = "/" + raw

        parsed = (
            parse_npc_or_dm_path(
                    raw
                    )
            or parse_npc_or_dm_path(
                    pathname or ""
                    )
            )

        initial_url_processed.set(
                True
                )

        if (
            parsed is None
            or parsed.get("seed") is None
            or parsed.get("race") is not None
            ):
            return

        set_loader(
                "show"
                )
        try:
            level = max(
                    1,
                    min(
                            20,
                            safe_int(
                                    parsed.get(
                                            "level"
                                            ),
                                    5,
                                    ),
                            ),
                    )
            ui.update_numeric(
                    "dm_level",
                    value=level,
                    )
            nonplayer = summon_nonplayer(
                    race=parsed.get(
                            "race"
                            ),
                    guild=parsed.get(
                            "guild"
                            ),
                    background=parsed.get(
                            "background"
                            ),
                    archetype=parsed.get(
                            "archetype"
                            ),
                    level=level,
                    seed=int(
                            parsed[
                                "seed"
                                ]
                            ),
                    )
            set_dm_character(
                    nonplayer,
                    level=level,
                    )
            show_page(
                    "dm"
                    )
        except Exception as error:
            error_state.set(
                    str(
                        error
                        )
                    )
            show_page(
                    "dm"
                    )
        finally:
            set_loader(
                    "hide"
                    )

    def generate_dm_character() -> None:
        set_loader(
                "show"
                )
        try:
            level = max(
                    1,
                    min(
                            20,
                            safe_int(
                                    input.dm_level(),
                                    5,
                                    ),
                            ),
                    )
            nonplayer = summon_nonplayer(
                    race=None,
                    background=None,
                    level=level,
                    seed=None,
                    )
            set_dm_character(
                    nonplayer,
                    level=level,
                    )
            show_page(
                    "dm"
                    )
        except Exception as error:
            error_state.set(
                    str(
                        error
                        )
                    )
            briefing_state.set(
                    None
                    )
            scene_state.set(
                    None
                    )
            adventure_state.set(
                    None
                    )
            character_state.set(
                    None
                    )
            show_page(
                    "dm"
                    )
        finally:
            set_loader(
                    "hide"
                    )

    @reactive.effect
    @reactive.event(
            input.btn_gen_dm_character
            )
    def generate_character_from_button() -> None:
        generate_dm_character()

    @reactive.effect
    @reactive.event(
            input.btn_regen_dm_character
            )
    def regenerate_character_from_button() -> None:
        generate_dm_character()

    @reactive.effect
    @reactive.event(
            input.btn_import_dm_character
            )
    def import_character_from_url() -> None:
        raw = (
            input.dm_character_url() or ""
            ).strip()
        parsed = parse_npc_or_dm_path(
                raw
                )

        if (
            parsed is None
            or parsed.get("seed") is None
            ):
            error_state.set(
                    "Could not parse an NPC URL. Use /npc/Race/Class/Background/level/seed."
                    )
            return

        set_loader(
                "show"
                )
        try:
            level = max(
                    1,
                    min(
                            20,
                            safe_int(
                                    parsed.get(
                                            "level"
                                            ),
                                    input.dm_level() or 5,
                                    ),
                            ),
                    )
            ui.update_numeric(
                    "dm_level",
                    value=level,
                    )
            nonplayer = summon_nonplayer(
                    race=parsed.get(
                            "race"
                            ),
                    guild=parsed.get(
                            "guild"
                            ),
                    background=parsed.get(
                            "background"
                            ),
                    archetype=parsed.get(
                            "archetype"
                            ),
                    level=level,
                    seed=int(
                            parsed[
                                "seed"
                                ]
                            ),
                    )
            set_dm_character(
                    nonplayer,
                    level=level,
                    )
            show_page(
                    "dm"
                    )
        except Exception as error:
            error_state.set(
                    str(
                        error
                        )
                    )
            show_page(
                    "dm"
                    )
        finally:
            set_loader(
                    "hide"
                    )

    @reactive.effect
    @reactive.event(
            input.btn_gen_scene
            )
    def generate_scene() -> None:
        adventure = adventure_state()

        if (
            adventure is None
            or adventure.dm_character is None
            ):
            error_state.set(
                    "Generate or import a DM Character first."
                    )
            return

        try:
            scene_state.set(
                    draw_inspiration(
                            adventure
                            )
                    )
            adventure_state.set(
                    adventure
                    )
            error_state.set(
                    None
                    )
        except Exception as error:
            error_state.set(
                    str(
                        error
                        )
                    )

    for occupant_index in range(
            0,
            4,
            ):
        @reactive.effect
        @reactive.event(
                getattr(
                        input,
                        f"dm_open_occ_{occupant_index}",
                        )
                )
        def open_occupant(
                index: int = occupant_index,
                ) -> None:
            scene = scene_state()

            if (
                scene is None
                or index >= len(
                        scene.occupants
                        )
                ):
                return

            occupant = scene.occupants[
                index
                ]

            if _links_to_dm_character(
                    occupant
                    ):
                host = character_state()
                if host is None:
                    error_state.set(
                            "No DM Character on this session."
                            )
                    return
                open_nonplayer(
                        host
                        )
                return

            if getattr(
                    occupant,
                    "npc_seed",
                    None,
                    ) is None:
                error_state.set(
                        "This occupant has no NPC sheet."
                        )
                return

            try:
                occupant_guild = getattr(
                        occupant,
                        "npc_guild",
                        None,
                        ) or None
                occupant_background = getattr(
                        occupant,
                        "npc_background",
                        None,
                        ) or None
                has_canonical_identity = all(
                        (
                            occupant_guild,
                            occupant_background,
                            )
                        )
                nonplayer = summon_nonplayer(
                        race=occupant.npc_race,
                        archetype=(
                            None
                            if has_canonical_identity
                            else occupant_background or "Commoner"
                            ),
                        guild=occupant_guild,
                        background=occupant_background,
                        level=int(
                                occupant.npc_level or 1
                                ),
                        seed=int(
                                occupant.npc_seed
                                ),
                        )
                open_nonplayer(
                        nonplayer
                        )
            except Exception as error:
                error_state.set(
                        str(
                            error
                            )
                        )

    @reactive.effect
    @reactive.event(
            input.btn_dm_open_character
            )
    def open_dm_character() -> None:
        host = character_state()
        if host is None:
            error_state.set(
                    "Generate or import a DM Character first."
                    )
            return
        open_nonplayer(
                host
                )

    @output
    @render.ui
    def dm_result() -> ui.Tag:
        return _render_companion_result(
                error=error_state(),
                briefing=briefing_state(),
                scene=scene_state(),
                path_url=path_url_state() or "",
                )


__all__ = (
    "mount_page",
    "page_ui",
    )
