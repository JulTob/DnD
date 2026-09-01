"""Project Species semantics onto completed Character sheet ledgers."""

from AtlasActorLudi.SpeciesKit.Humans import Resolve_Human_Features
from AtlasActorLudi.SpeciesKit.presentation import Project_Species_Feature
from AtlasLusoris.FeaturesKit import Resolve_Feature_Mechanics


def Name_Slots(
	char,
	) -> dict:
	"""
	What ``{name}`` and ``{full_name}`` mean in authored prose.

	``{name}`` is what you would call the Character to their face, so it is the
	first name alone.  ``{full_name}`` is the whole thing, for the rare line
	that wants the formality.  Defined once because both the Species entry and
	the Guild entry substitute into prose and must not drift apart.
	"""
	whole = str(
		getattr(
			char,
			"name",
			"",
			)
		or ""
		).strip()

	if not whole:
		return {
			"name": "them",
			"full_name": "them",
			}

	return {
		"name": whole.split()[ 0 ],
		"full_name": whole,
		}


def Project_Species_Description(
	character,
	) -> None:
	"""
	Head the Species section with what this people *is*.

	The Species entry comes first and carries no rule: it is the fixed half of
	the sheet's identity, the part every member of the people shares.  What
	follows is the generated half, and then the rules as written.

	The text may address the Character by ``{name}``, and a name is settled
	*after* features are resolved, so ``New_Player`` calls this a second time
	once naming is done.  Project_Species_Feature refreshes the existing Entry
	rather than adding a second one.
	"""
	from AtlasActorLudi.SpeciesKit.catalog import Current_Species

	species = Current_Species(
		character,
		)
	if species is None:
		return

	description = str(
		getattr(
			species,
			"DESCRIPTION",
			"",
			)
		or ""
		)
	if not description.strip():
		return

	slots = Name_Slots(
		character,
		)
	Project_Species_Feature(
		character,
		species.__name__.replace(
			"_",
			" ",
			),
		description.format(
			**slots
			),
		level=0,
		narrative=True,
		)

	from AtlasActorLudi.SpeciesKit.catalog import Current_Heritage

	heritage = Current_Heritage(
		character,
		)
	if heritage is None:
		return

	branch = str(
		getattr(
			heritage,
			"HERITAGE_DESCRIPTION",
			"",
			)
		or ""
		)
	if not branch.strip():
		return

	Project_Species_Feature(
		character,
		heritage.__name__.replace(
			"_",
			" ",
			),
		branch.format(
			**Name_Slots(
				character,
				)
			),
		level=0,
		narrative=True,
		)


def Resolve_Species_Features(
	character,
	) -> None:
	"""Resolve choices that require skills, hit points, or spell ledgers."""
	from AtlasActorLudi.SpeciesKit.Aasimar import Resolve_Aasimar_Features
	from AtlasActorLudi.SpeciesKit.Dragonborn import (
		Resolve_Dragonborn_Features,
		)
	from AtlasActorLudi.SpeciesKit.Dwarves import Resolve_Dwarf_Features
	from AtlasActorLudi.SpeciesKit.Elves import Resolve_Elf_Features
	from AtlasActorLudi.SpeciesKit.Gnomes import Resolve_Gnome_Features
	from AtlasActorLudi.SpeciesKit.Goliaths import Resolve_Goliath_Features
	from AtlasActorLudi.SpeciesKit.Halflings import (
		Resolve_Halfling_Features,
		)
	from AtlasActorLudi.SpeciesKit.Orcs import Resolve_Orc_Features
	from AtlasActorLudi.SpeciesKit.Tieflings import (
		Resolve_Tiefling_Features,
		)

	Project_Species_Description(
		character,
		)
	Resolve_Aasimar_Features(
		character,
		)
	Resolve_Dragonborn_Features(
		character,
		)
	Resolve_Dwarf_Features(
		character,
		)
	Resolve_Goliath_Features(
		character,
		)
	Resolve_Halfling_Features(
		character,
		)
	Resolve_Orc_Features(
		character,
		)
	Resolve_Tiefling_Features(
		character,
		)
	Resolve_Human_Features(
		character,
		)
	Resolve_Elf_Features(
		character,
		)
	Resolve_Gnome_Features(
		character,
		)
	Resolve_Feature_Mechanics(
		character,
		)
