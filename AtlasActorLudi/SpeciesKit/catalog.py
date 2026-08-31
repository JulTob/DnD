"""Derive production catalogues from imported Species declaration Pins.

The imports are Python's explicit module-loading boundary. They execute each
Species declaration once; the public collections below come from Pin Fields.
"""

from AtlasActorLudi.SpeciesKit.Aasimar import Aasimar
from AtlasActorLudi.SpeciesKit.Dragonborn import Dragonborn
from AtlasActorLudi.SpeciesKit.Dwarves import Dwarf
from AtlasActorLudi.SpeciesKit.Elves import Elf
from AtlasActorLudi.SpeciesKit.Gnomes import Gnome
from AtlasActorLudi.SpeciesKit.Goliaths import Goliath
from AtlasActorLudi.SpeciesKit.Halflings import Halfling
from AtlasActorLudi.SpeciesKit.Humans import Human
from AtlasActorLudi.SpeciesKit.NonPlayer import Aven
from AtlasActorLudi.SpeciesKit.NonPlayer import Beastfolk
from AtlasActorLudi.SpeciesKit.NonPlayer import Catfolk
from AtlasActorLudi.SpeciesKit.NonPlayer import Goblin
from AtlasActorLudi.SpeciesKit.NonPlayer import Kobold
from AtlasActorLudi.SpeciesKit.NonPlayer import Lizardfolk
from AtlasActorLudi.SpeciesKit.NonPlayer import Snakefolk
from AtlasActorLudi.SpeciesKit.Orcs import Orc
from AtlasActorLudi.SpeciesKit.Tieflings import Tiefling
from AtlasActorLudi.SpeciesKit.declarations import Available
from AtlasActorLudi.SpeciesKit.declarations import Declared_Species
from AtlasActorLudi.SpeciesKit.declarations import NonPlayer_Only


def Playable_Species() -> tuple:
	"""Read the current Player Species Field."""
	return tuple(Available[:])


def NonPlayer_Species() -> tuple:
	"""Read the current interim NonPlayer Species Field."""
	return tuple(NonPlayer_Only[:])


def Known_Species() -> tuple:
	"""Read every currently declared Species."""
	return tuple(Declared_Species[:])


def Species_Choices() -> tuple[str, ...]:
	"""Project current Species labels for production boundaries."""
	return tuple(tag.__name__
		for tag in Playable_Species()
		)


def Species_Weights() -> dict[str, int]:
	"""Project current generation weights by Species label."""
	return {tag.__name__: tag.WEIGHT
		for tag in Playable_Species()
		}


def Heritages_By_Species() -> dict:
	"""Project each declared Species to its owned Heritages."""
	return {
		tag: tuple(
			tag.HERITAGES
			)
		for tag in Playable_Species()
		if tag.HERITAGES
		}


def All_Heritages() -> tuple:
	"""Read every Heritage attached to a Species declaration."""
	return tuple(
		heritage
		for heritages in Heritages_By_Species().values()
		for heritage in heritages
		)


def Heritage_Choices() -> tuple[str, ...]:
	"""Project current Heritage labels for production boundaries."""
	return tuple(
		tag.__name__.replace(
			"_",
			" ",
			)
		for tag in All_Heritages()
		)


# The snapshots below are read once, at import. Call the functions above
# for a live view after later Pin edits.
PLAYABLE_SPECIES = Playable_Species()
NONPLAYER_SPECIES = NonPlayer_Species()
KNOWN_SPECIES = Known_Species()
SPECIES_CHOICES = Species_Choices()
SPECIES_WEIGHTS = Species_Weights()
HERITAGES_BY_SPECIES = Heritages_By_Species()
ALL_HERITAGES = All_Heritages()
HERITAGE_CHOICES = Heritage_Choices()

def Resolve_Species(
	requested,
	):
	"""Resolve a canonical Species key or Tag."""
	known_species = Known_Species()

	if requested in known_species:
		return requested

	key = str(requested).strip().replace(
		" ",
		"_",
		)

	for tag in known_species:
		if tag.__name__.casefold() == key.casefold():
			return tag

	raise ValueError(
		f"Unknown Species: {requested!r}."
		)


def Current_Species(
	target,
	):
	"""Return the one canonical Species currently carried."""
	carried = tuple(
		tag
		for tag in Known_Species()
		if target in tag
		)

	if len(carried) > 1:
		raise ValueError(
			"A Character carries conflicting Species: "
			+ ", ".join(
				tag.__name__
				for tag in carried
				)
			+ "."
			)

	return (
		carried[0]
		if carried
		else None
		)


def Resolve_Heritage(
	requested,
	):
	"""Resolve a canonical Heritage key or Tag."""
	all_heritages = All_Heritages()

	if requested in all_heritages:
		return requested

	key = str(requested).strip().replace(
		" ",
		"_",
		)

	for tag in all_heritages:
		if tag.__name__.casefold() == key.casefold():
			return tag

	raise ValueError(
		f"Unknown Heritage: {requested!r}."
		)


def Species_For_Heritage(
	requested,
	):
	"""Return the Species that owns one concrete Heritage."""
	heritage = Resolve_Heritage(requested)

	for species, heritages in Heritages_By_Species().items():
		if heritage in heritages:
			return species

	raise ValueError(
		f"Heritage {heritage.__name__!r} has no owning Species."
		)


def Current_Heritage(
	target,
	):
	"""Return the one concrete Heritage currently carried."""
	carried = tuple(
		tag
		for tag in All_Heritages()
		if target in tag
		)

	if len(carried) > 1:
		raise ValueError(
			"A Character carries conflicting Heritages: "
			+ ", ".join(
				tag.__name__
				for tag in carried
				)
			+ "."
			)

	return (
		carried[0]
		if carried
		else None
		)
