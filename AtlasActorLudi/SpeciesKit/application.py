"""Public Species application routes."""

from AtlasActorLudi.SpeciesKit.bases import Current_Creature_Type
from AtlasActorLudi.SpeciesKit.catalog import Current_Heritage
from AtlasActorLudi.SpeciesKit.catalog import Current_Species
from AtlasActorLudi.SpeciesKit.catalog import Heritages_By_Species
from AtlasActorLudi.SpeciesKit.catalog import Playable_Species
from AtlasActorLudi.SpeciesKit.catalog import Resolve_Heritage
from AtlasActorLudi.SpeciesKit.catalog import Resolve_Species
from AtlasActorLudi.SpeciesKit.catalog import Species_For_Heritage


def _random_species(
	character,
	):
	available = Playable_Species()
	dice_bag = character.Dice_Bag(
		"identity.species",
		version="2024",
		namespace="GenLegendActor",
		)
	return character.Pick(
		available,
		weights=tuple(
			tag.WEIGHT
			for tag in available
			),
		dice=dice_bag,
		)


def _random_heritage(
	character,
	species,
	available,
	size=None,
	):
	dice_bag = character.Dice_Bag(
		f"identity.species.{species.__name__}.heritage",
		version="2024",
		namespace="GenLegendActor",
		)

	def imprint(
		tag,
		):
		if character not in tag:
			if size is None:
				tag(
					character,
					)
			else:
				tag(
					character,
					size=size,
					)

	return character.Accept(
		available,
		dice=dice_bag,
		imprint=imprint,
		)


def Apply_Species(
	character,
	species=None,
	*,
	heritage=None,
	size=None,
	):
	if heritage is None:
		requested_heritage = None
	elif (
		isinstance(
			heritage,
			str,
			)
		and heritage.strip().casefold() == "random"
		):
		requested_heritage = None
	else:
		requested_heritage = Resolve_Heritage(
			heritage,
			)

	is_random = (
		species is None
		or (
			isinstance(
				species,
				str,
				)
			and species.strip().casefold() == "random"
			)
		)

	if is_random:
		if requested_heritage is not None:
			selected = Species_For_Heritage(
				requested_heritage,
				)
		else:
			selected = _random_species(
				character,
				)
	else:
		selected = Resolve_Species(
			species,
			)

	current = Current_Species(
		character,
		)
	if (
		current is not None
		and current is not selected
		):
		raise ValueError(
			"A Character cannot carry two Species: "
			f"{current.__name__!r} and {selected.__name__!r}."
			)

	current_heritage = Current_Heritage(
		character,
		)
	available_heritages = Heritages_By_Species().get(
		selected,
		(),
		)

	if available_heritages:
		if (
			requested_heritage is not None
			and requested_heritage not in available_heritages
			):
			owner = Species_For_Heritage(
				requested_heritage,
				)
			raise ValueError(
				f"Heritage {requested_heritage.__name__!r} requires Species "
				f"{owner.__name__!r}, not {selected.__name__!r}."
				)
		selected_heritage = (
			requested_heritage
			or current_heritage
			or _random_heritage(
				character,
				selected,
				available_heritages,
				size=size,
				)
			)
		shape = selected_heritage
	else:
		if requested_heritage is not None:
			owner = Species_For_Heritage(
				requested_heritage,
				)
			raise ValueError(
				f"Heritage {requested_heritage.__name__!r} requires Species "
				f"{owner.__name__!r}, not {selected.__name__!r}."
				)
		selected_heritage = None
		shape = selected

	if (
		current_heritage is not None
		and current_heritage is not selected_heritage
		):
		raise ValueError(
			"A Character cannot carry two Heritages: "
			f"{current_heritage.__name__!r} and "
			f"{selected_heritage.__name__!r}."
			)

	if character not in shape:
		shape(
			character,
			size=size,
			)

	character.species = selected.__name__.replace(
		"_",
		" ",
		)
	if selected_heritage is not None:
		character.heritage = selected_heritage.__name__.replace(
			"_",
			" ",
			)

	creature_type = Current_Creature_Type(
		character,
		)
	if creature_type is not None:
		character.creature_type = creature_type.__name__

	return selected
