"""Small shared Imprint helpers for concrete Species Shapes."""


def _selected_size(
	target,
	species,
	requested,
	) -> str | None:
	options = tuple(
		getattr(
			species,
			"SIZE_OPTIONS",
			(),
			)
		)

	if not options:
		return requested

	selected = (
		requested
		or getattr(
			target,
			"size",
			None,
			)
		)

	if selected is None:
		if len(options) == 1:
			selected = options[0]
		else:
			weights = getattr(
				species,
				"SIZE_WEIGHTS",
				None,
				)
			dice_bag = target.Dice_Bag(
				f"identity.species.{species.__name__}.size",
				version="2024",
				namespace="GenLegendActor",
				)
			selected = dice_bag.choices(
				options,
				weights=weights,
				k=1,
				)[
				0
				]

	if selected not in options:
		raise ValueError(
			f"{species.__name__} Size must be one of "
			f"{options!r}; received {selected!r}."
			)

	return selected


def Imprint_Species(
	target,
	species,
	size=None,
	) -> None:
	"""Imprint resolved physiology while membership remains transactional."""
	from AtlasActorLudi.SpeciesKit.bases import (
		CREATURE_TYPES,
		Current_Creature_Type,
		)
	from AtlasActorLudi.SpeciesKit.catalog import Current_Species

	current_species = Current_Species(target)

	if (
		current_species is not None
		and current_species is not species
		):
		raise ValueError(
			"A Character cannot carry two Species: "
			f"{current_species.__name__!r} and {species.__name__!r}."
			)

	expected_type = next(
		(
			creature_type
			for creature_type in CREATURE_TYPES
			if issubclass(
				species,
				creature_type,
				)
			),
		None,
		)
	current_type = Current_Creature_Type(target)

	if (
		expected_type is not None
		and current_type is not None
		and current_type is not expected_type
		):
		raise ValueError(
			f"{species.__name__} requires Creature Type "
			f"{expected_type.__name__!r}, not {current_type.__name__!r}."
			)

	target.species = species.__name__.replace(
		"_",
		" ",
		)

	selected_size = _selected_size(
		target,
		species,
		size,
		)

	if selected_size is not None:
		target.size = selected_size

	speed = getattr(
		species,
		"SPEED",
		None,
		)

	if speed is not None:
		target.speed = speed


def Imprint_Heritage(
	target,
	heritage,
	) -> None:
	"""Imprint one concrete Heritage while its Tagging remains atomic."""
	from AtlasActorLudi.SpeciesKit.catalog import Current_Heritage

	current = Current_Heritage(target)

	if (
		current is not None
		and current is not heritage
		):
		raise ValueError(
			"A Character cannot carry two Heritages: "
			f"{current.__name__!r} and {heritage.__name__!r}."
			)

	target.heritage = heritage.__name__.replace(
		"_",
		" ",
		)
