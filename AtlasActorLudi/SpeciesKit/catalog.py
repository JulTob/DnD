"""
Species catalogs as Pin Fields.

Playable, non-player, and known Species are not parallel registries.
They are the Fields of Available, NonPlayer_Only, and Declared_Species.
Importing each Species package applies its Player_Handbook_2024 Pin
before those Fields are read.
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


def Playable_Species():
	return tuple(
		Available[ : ]
		)


def NonPlayer_Species():
	return tuple(
		NonPlayer_Only[ : ]
		)


def Known_Species():
	return tuple(
		Declared_Species[ : ]
		)


def Species_Choices() -> tuple[ str, ... ]:
	return tuple(
		tag.__name__
		for tag in Playable_Species()
		)


def Species_Weights():
	return {
		tag.__name__: tag.WEIGHT
		for tag in Playable_Species()
		}


def Heritages_By_Species():
	return {
		tag: tuple(
			tag.HERITAGES
			)
		for tag in Playable_Species()
		if tag.HERITAGES
		}


def All_Heritages():
	return tuple(
		heritage
		for heritages in Heritages_By_Species().values()
		for heritage in heritages
		)


def Heritage_Choices() -> tuple[ str, ... ]:
	return tuple(
		tag.__name__.replace(
			"_",
			" ",
			)
		for tag in All_Heritages()
		)


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
	known = Known_Species()

	if requested in known:
		return requested

	key = str(
		requested,
		).strip().replace(
		" ",
		"_",
		).casefold()

	for tag in known:
		if tag.__name__.casefold() == key:
			return tag

	raise ValueError(
		f"Unknown Species: {requested!r}."
		)


def Resolve_Heritage(
	requested,
	):
	all_heritages = All_Heritages()

	if requested in all_heritages:
		return requested

	key = str(
		requested,
		).strip().replace(
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
	heritage = Resolve_Heritage(
		requested,
		)

	for species, heritages in Heritages_By_Species().items():
		if heritage in heritages:
			return species

	raise ValueError(
		f"Heritage {heritage.__name__!r} has no owning Species."
		)


def Current_Species(
	target,
	):
	carried = tuple(
		tag
		for tag in Known_Species()
		if target in tag
		)

	if len(
		carried,
		) > 1:
		raise ValueError(
			"A Character carries conflicting Species: "
			+ ", ".join(
				tag.__name__
				for tag in carried
				)
			+ "."
			)

	if carried:
		return carried[ 0 ]

	return None


def Current_Heritage(
	target,
	):
	carried = tuple(
		tag
		for tag in All_Heritages()
		if target in tag
		)

	if len(
		carried,
		) > 1:
		raise ValueError(
			"A Character carries conflicting Heritages: "
			+ ", ".join(
				tag.__name__
				for tag in carried
				)
			+ "."
			)

	if carried:
		return carried[ 0 ]

	return None
