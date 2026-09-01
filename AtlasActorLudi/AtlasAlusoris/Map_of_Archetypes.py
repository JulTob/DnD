"""Decode former Archetype names into Guild or Background compatibility axes."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from AtlasLusoris.BackgroundKit import BACKGROUNDS
from AtlasLusoris.BackgroundKit import NONPLAYER_ONLY_BACKGROUND_NAMES
from AtlasLusoris.GuildKit import GUILDS


LEGACY_ARCHETYPE_NAMES = (
		"Artist",
		"Bandit",
		"Barbarian",
		"Bard",
		"Berserker",
		"Charlatan",
		"Cleric",
		"Commoner",
		"Crafter",
		"Criminal",
		"Cultist",
		"Druid",
		"Expert",
		"Explorer",
		"Fighter",
		"Guardian",
		"Healer",
		"Hero",
		"Hunter",
		"Knight",
		"Mage",
		"Mentor",
		"Merchant",
		"Monk",
		"Ninja",
		"Noble",
		"Paladin",
		"Pirate",
		"Priest",
		"Ranger",
		"Rogue",
		"Scholar",
		"Shaman",
		"Soldier",
		"Sorcerer",
		"Spy",
		"Trickster",
		"Traveler",
		"Warlock",
		"Warrior",
		"Witch",
		"Wizard",
		)

LEGACY_GUILD_NAMES = tuple(
		name
		for name in LEGACY_ARCHETYPE_NAMES
		if name in GUILDS
		)

LEGACY_BACKGROUND_NAMES = tuple(
		name
		for name in LEGACY_ARCHETYPE_NAMES
		if name in BACKGROUNDS
		)

LEGACY_PROFILE_NAMES = tuple(
		name
		for name in LEGACY_ARCHETYPE_NAMES
		if name in NONPLAYER_ONLY_BACKGROUND_NAMES
		)

Archetypes = list(
		LEGACY_ARCHETYPE_NAMES
		)


class Identity_Axis(str, Enum):
	"""Independent Character identity axes used by the compatibility route."""

	GUILD = "guild"
	BACKGROUND = "background"


@dataclass(frozen=True, slots=True)
class Legacy_Identity:
	"""One former Archetype name routed to its canonical axis."""

	axis: Identity_Axis
	name: str


def Identity_Names(
		character,
		) -> tuple[str, ...]:
	"""Return canonical Guild and Background names once each."""
	result = []
	for attribute in (
			"char_class",
			"background",
			):
		value = getattr(
				character,
				attribute,
				None,
				)
		if isinstance(
				value,
				str,
				) and value and value not in result:
			result.append(
					value
					)
	return tuple(
			result
			)


def Identity_Text(
		character,
		) -> str:
	"""Return the canonical identity view expected by transitional Maps."""
	return " ".join(
			Identity_Names(
					character
					)
			)


def Classify_Archetype(
		name: str,
		) -> Legacy_Identity:
	"""Route an exact legacy name without inventing semantic aliases."""
	if name in GUILDS:
		return Legacy_Identity(
				Identity_Axis.GUILD,
				name,
				)
	if name in BACKGROUNDS:
		return Legacy_Identity(
				Identity_Axis.BACKGROUND,
				name,
				)
	raise ValueError(
			f"Unknown legacy NonPlayer Archetype: {name!r}."
			)


def Archetype(
		character,
		*,
		dice=None,
		) -> str:
	"""Select a compatibility Archetype through the Character."""
	return character.Pick(
			LEGACY_ARCHETYPE_NAMES,
			dice=dice,
			)


def _identity_modifiers(
		*,
		STR: int = 0,
		DEX: int = 0,
		CON: int = 0,
		INT: int = 0,
		WIS: int = 0,
		CHA: int = 0,
		) -> dict[str, int]:
	return {
			"Barbarian": CON,
			"Berserker": CON + STR,
			"Charlatan": CHA,
			"Cleric": WIS,
			"Crafter": INT,
			"Criminal": INT,
			"Cultist": WIS,
			"Druid": WIS + CON,
			"Expert": INT + WIS + CHA,
			"Explorer": WIS,
			"Fighter": DEX + STR,
			"Guardian": STR,
			"Hero": STR,
			"Hunter": DEX,
			"Knight": STR + CON,
			"Mage": INT,
			"Monk": DEX + WIS,
			"Ninja": DEX + INT,
			"Noble": DEX,
			"Paladin": STR + CHA,
			"Pirate": DEX,
			"Priest": WIS,
			"Ranger": WIS,
			"Rogue": DEX,
			"Shaman": WIS,
			"Soldier": STR,
			"Sorcerer": CHA,
			"Spy": DEX,
			"Warlock": CHA,
			"Warrior": STR,
			"Witch": WIS,
			"Wizard": INT,
			}


def AC_Identity_modifier(
		name: str | None,
		**abilities: int,
		) -> int:
	"""Return one identity's legacy AC contribution."""
	if not name:
		return 0
	return _identity_modifiers(
			**abilities
			).get(
			name,
			0,
			)


def AC_Archetype_modifier(
		archetype: str = "",
		**abilities: int,
		) -> int:
	"""Compatibility name for callers that still have one mixed identity."""
	return AC_Identity_modifier(
			archetype,
			**abilities,
			)


def AS_Archetype_modifier(
		npc,
		):
	"""Retired compatibility hook; canonical axes now own score influences."""
	return npc


__all__ = (
		"AC_Archetype_modifier",
		"AC_Identity_modifier",
		"AS_Archetype_modifier",
		"Archetype",
		"Archetypes",
		"Classify_Archetype",
		"Identity_Axis",
		"LEGACY_ARCHETYPE_NAMES",
		"LEGACY_BACKGROUND_NAMES",
		"LEGACY_GUILD_NAMES",
		"LEGACY_PROFILE_NAMES",
		"Legacy_Identity",
		)
