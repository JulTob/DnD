"""
Species, Heritage, and Creature Type.

These are Tags. The Character is the Target. Membership is Field
membership (`agent in Elf`), not a string kind check and not a
replaced `__contains__`.

Find_* project a display name from the Tag the Character currently
carries. Apply_Creature_Type is the single Creature Type Imprint.
"""

from TagKit import Pre
from TagKit import Tag

from AtlasActorLudi.CharactersKit import Character


def _display_tag_name(
	tag,
	) -> str:
	return tag.__name__.replace(
		"_",
		" ",
		)


def Find_Species(
	target,
	) -> str:
	from AtlasActorLudi.SpeciesKit.catalog import Current_Species

	species = Current_Species(
		target,
		)
	if species is None:
		return ""

	return _display_tag_name(
		species,
		)


def Find_Heritage(
	target,
	) -> str:
	from AtlasActorLudi.SpeciesKit.catalog import Current_Heritage

	heritage = Current_Heritage(
		target,
		)
	if heritage is None:
		return ""

	return _display_tag_name(
		heritage,
		)


def Find_Subspecies(
	target,
	) -> str:
	return Find_Heritage(
		target,
		)


class Species(Tag):
	"""A Character's lineage and physical form."""

	@Pre
	def Character_Only(
		target,
		):
		return isinstance(
			target,
			Character,
			)


class Heritage(Species):
	"""A more-specific lineage Shape beneath a Species."""


class Creature_Type(Tag):
	"""Canonical rules classification, independent from Species."""


class Aberration(Creature_Type):
	"""An aberration."""


class Beast(Creature_Type):
	"""A beast."""


class Celestial(Creature_Type):
	"""A celestial creature."""


class Construct(Creature_Type):
	"""A constructed creature."""


class Dragon(Creature_Type):
	"""A dragon."""


class Elemental(Creature_Type):
	"""An elemental creature."""


class Fey(Creature_Type):
	"""A fey creature."""


class Fiend(Creature_Type):
	"""A fiend."""


class Giant(Creature_Type):
	"""A giant."""


class Humanoid(Creature_Type):
	"""A humanoid creature."""


class Monstrosity(Creature_Type):
	"""A monstrosity."""


class Ooze(Creature_Type):
	"""An ooze."""


class Plant(Creature_Type):
	"""A plant creature."""


class Undead(Creature_Type):
	"""An undead creature."""


class Vampire(Undead):
	"""An Undead creature with vampiric context."""


CREATURE_TYPES = (
	Aberration,
	Beast,
	Celestial,
	Construct,
	Dragon,
	Elemental,
	Fey,
	Fiend,
	Giant,
	Humanoid,
	Monstrosity,
	Ooze,
	Plant,
	Undead,
	)

CREATURE_TYPE_TAGS = {
	tag.__name__: tag
	for tag in CREATURE_TYPES
	}


def Resolve_Creature_Type(
	requested,
	):
	if (
		isinstance(
			requested,
			type,
			)
		and issubclass(
			requested,
			Creature_Type,
			)
		):
		if requested is Vampire:
			return Undead

		if requested in CREATURE_TYPES:
			return requested

	key = str(
		requested,
		).strip().replace(
		" ",
		"_",
		)

	for name, tag in CREATURE_TYPE_TAGS.items():
		if name.casefold() == key.casefold():
			return tag

	raise ValueError(
		f"Unknown Creature Type: {requested!r}."
		)


def Current_Creature_Type(
	target,
	):
	carried = tuple(
		tag
		for tag in CREATURE_TYPES
		if target in tag
		)

	if len(
		carried,
		) > 1:
		raise ValueError(
			"A Character carries conflicting Creature Types: "
			+ ", ".join(
				tag.__name__
				for tag in carried
				)
			+ "."
			)

	if carried:
		return carried[ 0 ]

	return None


def Apply_Creature_Type(
	target,
	requested,
	):
	"""Apply one canonical Creature Type and project its display key."""
	selected = Resolve_Creature_Type(
		requested,
		)
	current = Current_Creature_Type(
		target,
		)

	if (
		current is not None
		and current is not selected
		):
		raise ValueError(
			"A Character cannot carry two Creature Types: "
			f"{current.__name__!r} and {selected.__name__!r}."
			)

	if target not in selected:
		selected(
			target,
			)

	target.creature_type = selected.__name__
	return selected
