"""Per-session navigation for the Shiny frontline."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any

from shiny import reactive

from app.publish_scope import published_page


class Page(
        str,
        Enum,
        ):
    """Frontline destinations, named for the Atlas surface they expose."""

    HOME = "home"
    ACTOR_LUDI_PLAYER = "character"
    ACTOR_LUDI_ALUSORIS = "npc"
    ACTOR_LUDI_ALUSORIS_LIST = "npclist"
    MAGISTRATUM = "dm"


def resolve_page(
        value: Page | str | None,
        ) -> Page:
    try:
        return Page(
                value
                )
    except (
            TypeError,
            ValueError,
            ):
        return Page.HOME


@dataclass(
        slots=True,
        )
class Navigator:
    """Own one session's current frontline destination."""

    _current: Any

    @classmethod
    def create(
            cls,
            ) -> "Navigator":
        return cls(
                _current=reactive.value(
                        Page.HOME.value
                        ),
                )

    def show(
            self,
            page: Page | str,
            ) -> None:
        destination = resolve_page(
                published_page(
                        resolve_page(
                                page
                                ).value
                        )
                )
        self._current.set(
                destination.value
                )

    def current(
            self,
            ) -> Page:
        return resolve_page(
                self._current()
                )


__all__ = (
        "Navigator",
        "Page",
        "resolve_page",
        )
