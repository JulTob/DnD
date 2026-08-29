"""Routes Character requests through the current Player production line.

This Map is the stable boundary used by the Shiny frontline while the legacy
Grimoire is progressively decomposed into Character Tags.
"""

from __future__ import annotations

from dataclasses import dataclass
from os import environ
from secrets import randbits
from typing import Any

from Minion import chronicler, minion

from AtlasActorLudi.CharactersKit import Player
from AtlasActorLudi.Tools_of_Legacy_RNG import Isolated_Legacy_RNG
from AtlasLusoris.Grimoire_of_Characters import (
    Character,
    awaken_player,
    )
from AtlasLusoris.BackgroundKit import PLAYER_BACKGROUNDS
from AtlasLusoris.GuildKit import GUILDS
from AtlasLusoris.Map_of_Species import species as species_map


@dataclass(
        frozen=True,
        slots=True,
        )
class Character_Choices:
    """Selectable Character dimensions exposed to a frontline."""

    species: tuple[str, ...]
    guilds: tuple[str, ...]
    backgrounds: tuple[str, ...]


def choices() -> Character_Choices:
    """Return sorted immutable choices without presentation placeholders."""
    return Character_Choices(
            species=tuple(
                sorted(
                    species_map.keys()
                    )
                ),
            guilds=tuple(
                sorted(
                    GUILDS
                    )
                ),
            backgrounds=tuple(
                sorted(
                    PLAYER_BACKGROUNDS
                    )
                ),
            )


def _validate_choice(
        dimension: str,
        requested: str | None,
        available,
        ) -> str | None:
    if (
        requested is None
        or requested == "Random"
        ):
        return None

    valid_values = tuple(
            available
            )

    if requested not in valid_values:
        raise ValueError(
                f"Unknown Character {dimension}: {requested!r}."
                )

    return requested


@minion
def _attempt_player(
        **request: Any,
        ) -> Character:
    """Perform one generation attempt through the transitional Grimoire."""
    seed = request.pop(
            "seed",
            -1,
            )
    level = request.pop(
            "level",
            1,
            )

    with Isolated_Legacy_RNG(
            seed
            ):
        character = Character(
                seed=seed,
                level=level,
                )

        Player(
                character
                )

        return awaken_player(
                character,
                level=level,
                **request,
                )


@chronicler
def summon_player(
        species: str | None = None,
        guild: str | None = None,
        background: str | None = None,
        level: int = 1,
        gender: str | None = None,
        seed: int | None = None,
        ) -> Character:
    """Generate one Player Character, retrying with fresh deterministic seeds."""
    selected_species = _validate_choice(
            "Species",
            species,
            species_map.keys(),
            )
    selected_guild = _validate_choice(
            "Guild",
            guild,
            GUILDS,
            )
    selected_background = _validate_choice(
            "Background",
            background,
            PLAYER_BACKGROUNDS,
            )
    requested_level = max(
            1,
            min(
                20,
                int(
                    level
                    ),
                ),
            )
    current_seed = (
        int(
                seed
                )
        if seed is not None
        else randbits(
                64
                )
        )

    if current_seed < 0:
        raise ValueError(
                "A Player generation seed must be zero or greater."
                )
    last_error: Exception | None = None

    # Retrying re-rolls the seed, which hides real bugs and breaks determinism.
    # STRICT_GENERATION=1 (tests, verification harnesses) surfaces the first
    # failure instead of masking it behind four more attempts.
    attempts = (
        1
        if environ.get(
                "STRICT_GENERATION",
                )
        else 5
        )

    for _ in range(
            attempts
            ):
        try:
            return _attempt_player(
                    species=selected_species,
                    char_class=selected_guild,
                    background=selected_background,
                    level=requested_level,
                    gender=gender,
                    seed=current_seed,
                    )
        except Exception as error:
            last_error = error
            current_seed += 1

    if attempts == 1:
        raise last_error

    raise RuntimeError(
            "Unable to summon a Player Character after five attempts."
            ) from last_error


__all__ = (
    "Character_Choices",
    "choices",
    "summon_player",
    )
