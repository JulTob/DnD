"""Stable path representation for one generated NonPlayer Character."""

from __future__ import annotations

from typing import Any
from urllib.parse import quote, unquote, urlparse


def _decode_label(
        value: str,
        ) -> str:
    return str(
            value
            ).replace(
            "_",
            " ",
            )


def _encode_label(
        value: Any,
        ) -> str:
    return quote(
            str(
                    value
                    ).replace(
                    " ",
                    "_",
                    ),
            safe="_",
            )


def parse_nonplayer_path(
        raw: str | None,
        ) -> dict[str, Any] | None:
    """Parse current or legacy NonPlayer paths from a path, URL, or hash."""
    text = str(
            raw
            or ""
            ).strip()

    if not text:
        return None

    if text.startswith(
            (
                "http://",
                "https://",
                )
            ):
        parsed_url = urlparse(
                text
                )
        text = (
            parsed_url.fragment
            or parsed_url.path
            )

    text = text.lstrip(
            "#"
            )
    parts = [
        _decode_label(
                unquote(
                        part
                        )
                )
        for part in text.split(
                "/"
                )
        if part
        ]

    try:
        npc_index = next(
                index
                for index, part in enumerate(
                        parts
                        )
                if part.casefold() == "npc"
                )
    except StopIteration:
        return None

    try:
        values = parts[
            npc_index + 1:
            ]

        if len(
                values
                ) >= 6:
            (
                race,
                guild,
                former_background,
                former_profile,
                level,
                seed,
                ) = values[:6]

            return {
                "race": race,
                "guild": guild,
                "background": former_profile,
                "legacy_background": former_background,
                "level": max(
                        1,
                        int(
                                level
                                ),
                        ),
                "seed": int(
                        seed
                        ),
                }

        if len(
                values
                ) >= 5:
            race, guild, background, level, seed = values[:5]

            return {
                "race": race,
                "guild": guild,
                "background": background,
                "level": max(
                        1,
                        int(
                                level
                                ),
                        ),
                "seed": int(
                        seed
                        ),
                }

        if len(
                values
                ) >= 4:
            race, archetype, level, seed = values[:4]

            return {
                "race": race,
                "guild": None,
                "background": None,
                "archetype": archetype,
                "level": max(
                        1,
                        int(
                                level
                                ),
                        ),
                "seed": int(
                        seed
                        ),
                }

        return None
    except (
        TypeError,
        ValueError,
        ):
        return None


def nonplayer_hash(
        *,
        race: str,
        level: int,
        seed: int,
        guild: str | None = None,
        background: str | None = None,
        profile: str | None = None,
        archetype: str | None = None,
        ) -> str:
    """Build a full identity path, retaining the former compact form."""
    if (
        profile
        and background
        and profile != background
        ):
        raise ValueError(
                "NonPlayer Background and legacy Profile disagree: "
                f"{background!r} != {profile!r}."
                )

    resolved_background = background or profile

    if (
        guild
        and resolved_background
        ):
        return (
            "npc/"
            f"{_encode_label(race)}/"
            f"{_encode_label(guild)}/"
            f"{_encode_label(resolved_background)}/"
            f"{max(1, int(level))}/"
            f"{int(seed)}"
            )

    if (
        guild is not None
        or resolved_background is not None
        ):
        raise ValueError(
                "A canonical NonPlayer path requires Guild and Background "
                "together."
                )

    legacy = archetype

    if not legacy:
        raise ValueError(
                "A legacy NonPlayer path requires an Archetype."
                )

    return (
        "npc/"
        f"{_encode_label(race)}/"
        f"{_encode_label(legacy)}/"
        f"{max(1, int(level))}/"
        f"{int(seed)}"
        )


__all__ = (
    "nonplayer_hash",
    "parse_nonplayer_path",
    )
