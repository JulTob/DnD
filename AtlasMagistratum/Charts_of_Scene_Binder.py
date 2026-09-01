"""
Bind a DM Character to Epica and shape Companion scene data.

Attach the framing Character to an Adventure, draw an inspiration card, and
return presentation-neutral scene records. The Shiny frontline renders them.

Philosophy: the DM Character is morally open — villain, Quest Master, contested
guardian, or any figure whose will frames the session. Cards pressure the table
around that will; they do not assume evil.
"""

from __future__ import annotations

from types import SimpleNamespace
from typing import Any

from AtlasActorLudi.CharactersKit import Character
from AtlasEpica.Grimoire_of_Adventure import Forge_Oracle
from AtlasEpica.Map_of_Scenes import frame_briefing
from AtlasEpica.Map_of_Scenes import inspiration_card


def bind_dm_character(
		dm_character: Character,
		*,
		level: int | None = None,
		) -> Any:
	"""Collapse Area/Lair for this DM Character — returns the Adventure Target."""
	lvl = int(
			level
			if level is not None
			else getattr(
					dm_character,
					"level",
					5,
					)
			or 5
			)
	return Forge_Oracle(
			dm_character,
			seed=int(
					getattr(
							dm_character,
							"seed",
							0,
							)
					),
			level=lvl,
			)


bind_bbeg = bind_dm_character


def briefing_for(
		adventure: Any,
		) -> str:
	return frame_briefing(
			adventure
			)


def draw_inspiration(
		adventure: Any,
		) -> SimpleNamespace:
	"""One inspiration card as a namespace the Companion UI can render."""
	return card_as_namespace(
			inspiration_card(
					adventure
					)
			)


def card_as_namespace(
		card: dict[str, Any],
		) -> SimpleNamespace:
	occupants = [
			SimpleNamespace(
					**occ
					)
			for occ in card.get(
					"occupants",
					[],
					)
			]
	return SimpleNamespace(
			title=card.get(
					"title",
					"",
					),
			prose=card.get(
					"prose",
					"",
					),
			kind=card.get(
					"kind",
					"",
					),
			occupants=occupants,
			area=card.get(
					"area"
					),
			lair=card.get(
					"lair"
					),
			hooks=card.get(
					"hooks",
					[],
					),
			)
