"""Resolve Dwarf rules onto a completed Character sheet."""

from AtlasActorLudi.SpeciesKit.presentation import Project_Species_Feature


def _proficiency_bonus(
	target,
	) -> int:
	return int(
		getattr(
			target,
			"proficiency_bonus",
			2,
			)
		)


def _project_darkvision(
	target,
	) -> None:
	from AtlasActorLudi.SpeciesKit.Dwarves import Darkvision

	darkvision_range = int(
		getattr(
			target,
			"darkvision",
			Darkvision.RANGE,
			)
		)
	Project_Species_Feature(
		target,
		"Darkvision",
		(
			"<b>Gained at Level 1.</b> Dwarven senses granted Darkvision "
			f"with a range of {darkvision_range} feet."
			),
		chips=(
			(
				"Darkvision",
				f"{darkvision_range} ft",
				"👁️",
				),
			),
		level=1,
		)


def _project_dwarven_resilience(
	target,
	) -> None:
	from AtlasActorLudi.SpeciesKit.Dwarves import Dwarven_Resilience

	Project_Species_Feature(
		target,
		"Dwarven Resilience",
		(
			"<b>Gained at Level 1.</b> Dwarven stock granted Resistance to "
			f"{Dwarven_Resilience.RESISTANCE} damage, and Advantage on "
			"saving throws made to avoid or end the "
			f"{Dwarven_Resilience.SAVE_ADVANTAGE_CONDITION} condition."
			),
		chips=(
			(
				"Poison Resistance",
				"Resistant",
				"🧪",
				),
			),
		level=1,
		)


def _project_dwarven_toughness(
	target,
	) -> None:
	from AtlasActorLudi.SpeciesKit.Dwarves import Dwarven_Toughness

	level = int(
		getattr(
			target,
			"level",
			1,
			)
		)
	gained = level * Dwarven_Toughness.HIT_POINTS_PER_LEVEL
	Project_Species_Feature(
		target,
		"Dwarven Toughness",
		(
			"<b>Gained at Level 1.</b> Dwarven stock granted one extra Hit "
			"Point, and one more at every level after: "
			f"{gained} in total at Level {level}."
			),
		chips=(
			(
				"Toughness HP",
				f"+{gained}",
				"❤️",
				),
			),
		level=1,
		)


def _project_stonecunning(
	target,
	) -> None:
	from AtlasActorLudi.SpeciesKit.Dwarves import Stonecunning

	proficiency = _proficiency_bonus( target )
	target.stonecunning_uses = proficiency
	Project_Species_Feature(
		target,
		"Stonecunning",
		(
			f"<b>Gained at Level 1.</b> <b>{Stonecunning.ACTION}.</b> Gain "
			f"{Stonecunning.SENSE} with a range of {Stonecunning.RANGE} feet "
			f"for {Stonecunning.DURATION_MINUTES} minutes while on or "
			"touching a stone surface, natural or worked. The trait carries "
			f"{proficiency} uses per {Stonecunning.RECOVERY}."
			),
		chips=(
			(
				"Stonecunning Uses",
				proficiency,
				"🪨",
				),
			(
				"Tremorsense",
				f"{Stonecunning.RANGE} ft",
				"📿",
				),
			),
		level=1,
		)


def Resolve_Dwarf_Features(
	target,
	) -> None:
	"""Project the Dwarf Tags into readable Entries and Chips."""
	from AtlasActorLudi.SpeciesKit.Dwarves import Dwarf

	if target not in Dwarf:
		return

	_project_darkvision( target )
	_project_dwarven_resilience( target )
	_project_dwarven_toughness( target )
	_project_stonecunning( target )
