"""Compose the Shiny frontline from pages, components, and Atlas APIs."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from shiny import App, reactive, render, ui

from AtlasActorLudi import (
    character_choices,
    summon_player,
    )
from AtlasActorLudi.AtlasAlusoris import (
    nonplayer_choices,
    summon_nonplayer,
    summon_nonplayer_list,
    )
from AtlasPugna.Map_of_Legendary_Actions import (
    Lair,
    Legendary,
    Region,
    )
from app.client import Client_Messages
from app.components.shared import safe_int
from app.navigation import Navigator, Page
from app.pages import (
    alusoris_list_page_ui,
    alusoris_page_ui,
    home_page_ui,
    magistratum_page_ui,
    mount_alusoris_list_page,
    mount_alusoris_page,
    mount_magistratum_page,
    mount_player_page,
    player_page_ui,
    )
from app.routing import Shareable_Path_Redirect
from app.session import Session_State
from app.shell import app_ui


_character_choices = character_choices()
_nonplayer_choices = nonplayer_choices()

SPECIES_CHOICES = (
    "Random",
    *_character_choices.species,
    )
GUILD_CHOICES = (
    "Random",
    *_character_choices.guilds,
    )
BACKGROUND_CHOICES = (
    "Random",
    *_character_choices.backgrounds,
    )
RACE_CHOICES = (
    "Random",
    *_nonplayer_choices.races,
    )
NONPLAYER_BACKGROUND_CHOICES = (
    "Random",
    *_nonplayer_choices.backgrounds,
    )


_PAGE_VIEWS = {
    Page.HOME: home_page_ui(
            SPECIES_CHOICES,
            GUILD_CHOICES,
            BACKGROUND_CHOICES,
            RACE_CHOICES,
            NONPLAYER_BACKGROUND_CHOICES,
            ),
    Page.ACTOR_LUDI_PLAYER: player_page_ui(
            SPECIES_CHOICES,
            GUILD_CHOICES,
            BACKGROUND_CHOICES,
            ),
    Page.ACTOR_LUDI_ALUSORIS: alusoris_page_ui(
            RACE_CHOICES,
            NONPLAYER_BACKGROUND_CHOICES,
            ),
    Page.ACTOR_LUDI_ALUSORIS_LIST: alusoris_list_page_ui(),
    Page.MAGISTRATUM: magistratum_page_ui(),
    }


def server(
        input: Any,
        output: Any,
        session: Any,
        ) -> None:
    """Wire one browser session to public Atlas production routes."""
    state = Session_State.create()
    navigator = Navigator.create()
    client = Client_Messages(
            session
            )

    def open_nonplayer(
            character: Any,
            ) -> None:
        state.nonplayer.set(
                character
                )
        state.nonplayer_error.set(
                None
                )
        navigator.show(
                Page.ACTOR_LUDI_ALUSORIS
                )

    def send_url_hash(
            url_hash: str,
            ) -> None:
        client.send(
                "update_character_url",
                {
                    "hash": url_hash,
                    },
                )

    mount_player_page(
            input,
            output,
            session,
            state=state,
            navigator=navigator,
            client=client,
            summon_player=summon_player,
            species_choices=SPECIES_CHOICES,
            guild_choices=GUILD_CHOICES,
            background_choices=BACKGROUND_CHOICES,
            )
    mount_alusoris_page(
            input,
            output,
            session,
            state=state,
            navigator=navigator,
            client=client,
            summon_nonplayer=summon_nonplayer,
            legendary_renderer=Legendary,
            lair_renderer=Lair,
            region_renderer=Region,
            )
    mount_alusoris_list_page(
            input,
            output,
            state=state,
            navigator=navigator,
            client=client,
            summon_nonplayer_list=summon_nonplayer_list,
            open_nonplayer=open_nonplayer,
            )
    mount_magistratum_page(
            input,
            output,
            session,
            show_page=navigator.show,
            set_loader=client.set_loader,
            send_url_hash=send_url_hash,
            summon_nonplayer=summon_nonplayer,
            open_nonplayer=open_nonplayer,
            safe_int=safe_int,
            )

    @reactive.effect
    @reactive.event(
            input.go_home,
            )
    def open_home() -> None:
        navigator.show(
                Page.HOME
                )

    @output
    @render.ui
    def active_page() -> ui.Tag:
        return _PAGE_VIEWS.get(
                navigator.current(),
                _PAGE_VIEWS[
                    Page.HOME
                    ],
                )


_shiny_app = App(
        app_ui(),
        server,
        static_assets={
            "/static": Path(
                __file__
                ).resolve().parent / "static",
            },
        )

app = Shareable_Path_Redirect(
        _shiny_app
        )


__all__ = (
    "app",
    "server",
    )
