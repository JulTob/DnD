"""Reactive state owned by one connected Shiny session."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from shiny import reactive


@dataclass(
        slots=True,
        )
class Session_State:
    """Frontend state only; generated objects remain Actor Ludi products."""

    player: Any
    player_parameters: Any
    player_error: Any
    player_url_processed: Any
    nonplayer: Any
    nonplayer_error: Any
    nonplayer_list: Any
    nonplayer_list_error: Any
    nonplayer_race: Any
    nonplayer_guild: Any
    nonplayer_background: Any

    @classmethod
    def create(
            cls,
            ) -> "Session_State":
        return cls(
                player=reactive.value(
                        None
                        ),
                player_parameters=reactive.value(
                        None
                        ),
                player_error=reactive.value(
                        None
                        ),
                player_url_processed=reactive.value(
                        False
                        ),
                nonplayer=reactive.value(
                        None
                        ),
                nonplayer_error=reactive.value(
                        None
                        ),
                nonplayer_list=reactive.value(
                        []
                        ),
                nonplayer_list_error=reactive.value(
                        None
                        ),
                nonplayer_race=reactive.value(
                        None
                        ),
                nonplayer_guild=reactive.value(
                        None
                        ),
                nonplayer_background=reactive.value(
                        None
                        ),
                )


__all__ = (
        "Session_State",
        )
