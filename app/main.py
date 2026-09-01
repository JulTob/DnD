"""Compose the Shiny frontline from pages, components, and Atlas APIs."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from shiny import App
from shiny import reactive
from shiny import render
from shiny import ui

from AtlasActorLudi import character_choices
from AtlasActorLudi import summon_player
from AtlasActorLudi.AtlasAlusoris import nonplayer_choices
from AtlasActorLudi.AtlasAlusoris import summon_nonplayer
from AtlasActorLudi.AtlasAlusoris import summon_nonplayer_list
from AtlasPugna.Map_of_Legendary_Actions import Lair
from AtlasPugna.Map_of_Legendary_Actions import Legendary
from AtlasPugna.Map_of_Legendary_Actions import Region
from app.client import Client_Messages
from app.components.shared import safe_int
from app.navigation import Navigator
from app.navigation import Page
from app.pages import alusoris_list_page_ui
from app.pages import alusoris_page_ui
from app.pages import home_page_ui
from app.pages import magistratum_page_ui
from app.pages import mount_alusoris_list_page
from app.pages import mount_alusoris_page
from app.pages import mount_magistratum_page
from app.pages import mount_player_page
from app.pages import player_page_ui
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
NONPLAYER_GUILD_CHOICES = (
        "Random",
        *_nonplayer_choices.guilds,
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
                NONPLAYER_GUILD_CHOICES,
                NONPLAYER_BACKGROUND_CHOICES,
                ),
        Page.ACTOR_LUDI_PLAYER: player_page_ui(
                SPECIES_CHOICES,
                GUILD_CHOICES,
                BACKGROUND_CHOICES,
                ),
        Page.ACTOR_LUDI_ALUSORIS: alusoris_page_ui(
                RACE_CHOICES,
                NONPLAYER_GUILD_CHOICES,
                NONPLAYER_BACKGROUND_CHOICES,
                ),
        Page.ACTOR_LUDI_ALUSORIS_LIST: alusoris_list_page_ui(),
        Page.MAGISTRATUM: magistratum_page_ui(),
        }


def server(
        input,
        output,
        session,
        ) -> None:
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
            specialization_choices=_character_choices.specializations,
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
            input.go_home
            )
    def open_home(
            ) -> None:
        navigator.show(
                Page.HOME
                )

    @output
    @render.ui
    def active_page(
            ):
        return _PAGE_VIEWS.get(
                navigator.current(),
                _PAGE_VIEWS[Page.HOME],
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
