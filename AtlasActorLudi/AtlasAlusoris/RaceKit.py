"""
RaceKit

NonPlayer boundary from legacy Race choices into shared Species and canonical
Creature Type Tags.

Race is a generator request, not a mixed TOP Geometry. A Dwarf request applies
the shared Dwarf Species Shape; an Aberration request applies the Aberration
Creature Type. The ``race`` string remains only as a compatibility projection
for the legacy Alusoris maps and Nomina providers.
"""

from AtlasActorLudi.AtlasAlusoris.Map_of_Races import Creature_Type_For_Race
from AtlasActorLudi.AtlasAlusoris.Map_of_Races import race_weights
from AtlasActorLudi.SpeciesKit import Apply_Creature_Type
from AtlasActorLudi.SpeciesKit import Apply_Species
from AtlasActorLudi.SpeciesKit import Resolve_Creature_Type
from AtlasActorLudi.SpeciesKit import Resolve_Species
from AtlasActorLudi.SpeciesKit import Undead
from AtlasActorLudi.SpeciesKit import Vampire


RACE_CHOICES = (
		"Aberration",
		"Aven",
		"Beast",
		"Beastfolk",
		"Catfolk",
		"Celestial",
		"Construct",
		"Dragon",
		"Dwarf",
		"Elemental",
		"Elf",
		"Fey",
		"Fiend",
		"Giant",
		"Gnome",
		"Goblin",
		"Halfling",
		"Human",
		"Kobold",
		"Lizardfolk",
		"Monstrosity",
		"Ooze",
		"Orc",
		"Plant",
		"Snakefolk",
		"Undead",
		"Vampire",
		)


def _random_race(
		character,
		) -> str:
	dice_bag = character.Dice_Bag(
			"identity.nonplayer.race",
			version="1",
			namespace="GenLegendActor",
			)
	return dice_bag.choices(
			RACE_CHOICES,
			weights=tuple(
					race_weights[race]
					for race in RACE_CHOICES
					),
			k=1,
			)[0]


def _species_for(
		race,
		):
	try:
		return Resolve_Species(
				race
				)
	except ValueError:
		return None


def Apply_Race(
		character,
		race=None,
		creature_type=None,
		):
	"""Resolve one NonPlayer Race request into shared semantic Tags."""
	is_random = race is None or (
			isinstance(
					race,
					str,
					)
			and race.strip().casefold() == "random"
			)
	if is_random:
		selected_race = _random_race(
				character
				)
	else:
		selected_race = str(
				race
				).strip()
	expected_type = Resolve_Creature_Type(
			Creature_Type_For_Race(
					selected_race
					)
			)
	if creature_type is None:
		selected_type = expected_type
	else:
		selected_type = Resolve_Creature_Type(
				creature_type
				)
	if selected_type is not expected_type:
		raise ValueError(
				f"{selected_race!r} requires Creature Type {expected_type.__name__!r}, not {selected_type.__name__!r}."
				)
	current_race = getattr(
			character,
			"race",
			None,
			)
	if current_race is not None and current_race != selected_race:
		raise ValueError(
				f"A Character cannot carry two NonPlayer Race requests: {current_race!r} and {selected_race!r}."
				)
	species = _species_for(
			selected_race
			)
	if species is not None:
		identity_tag = Apply_Species(
				character,
				species,
				)
	elif selected_race == "Vampire":
		Apply_Creature_Type(
				character,
				Undead,
				)
		if character not in Vampire:
			Vampire(
					character
					)
		identity_tag = Vampire
	else:
		identity_tag = Apply_Creature_Type(
				character,
				selected_race,
				)
	Apply_Creature_Type(
			character,
			selected_type,
			)
	character.race = selected_race
	character.creature_type = selected_type.__name__
	return identity_tag


def _test_species_race(
		) -> None:
	from AtlasActorLudi.CharactersKit import Character
	from AtlasActorLudi.SpeciesKit import Dwarf
	from AtlasActorLudi.SpeciesKit import Humanoid

	character = Character(
			seed=401
			)
	tag = Apply_Race(
			character,
			"Dwarf",
			)
	assert tag is Dwarf
	assert character in Dwarf
	assert character in Humanoid
	assert character.race == "Dwarf"
	assert character.creature_type == "Humanoid"


def _test_monster_race(
		) -> None:
	from AtlasActorLudi.CharactersKit import Character

	character = Character(
			seed=409
			)
	tag = Apply_Race(
			character,
			"Vampire",
			)
	assert tag is Vampire
	assert character in Vampire
	assert character in Undead
	assert character.race == "Vampire"
	assert character.creature_type == "Undead"


def _self_test(
		) -> None:
	_test_species_race()
	_test_monster_race()
	print(
			"OK — Alusoris RaceKit self-test"
			)


if __name__ == "__main__":
	_self_test()
