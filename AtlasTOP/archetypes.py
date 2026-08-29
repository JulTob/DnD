from __future__ import annotations

from TagKit import Tag

from AtlasAlusoris.Map_of_Archetypes import Archetypes as ARCHETYPES

from ._helpers import build_identity_tag


class Archetype(Tag):
    """Semantic TOP tags for NPC archetypes."""


_USED_NAMES: set[str] = set()
_TAGS_BY_VALUE: dict[str, type[Tag]] = {}


def _register(
                value: str,
                ) -> type[Tag]:
        tag = build_identity_tag(
                base=Archetype,
                family="archetype",
                value=value,
                module_name=__name__,
                used_names=_USED_NAMES,
                )
        _TAGS_BY_VALUE[value] = tag
        globals()[tag.__name__] = tag

        return tag


for _archetype_name in ARCHETYPES:
        _register(
                _archetype_name,
                )


def tag_for_archetype(
        value: str,
        ) -> type[Tag]:
    tag = _TAGS_BY_VALUE.get(
            value,
            )

    if tag is not None:
        return tag

    return _register(
            value,
            )


__all__ = [
        "Archetype",
        "tag_for_archetype",
        *sorted(tag.__name__ for tag in _TAGS_BY_VALUE.values()),
        ]
