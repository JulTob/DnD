"""Extensible 2024 Gnome Species Atlas."""

from AtlasActorLudi.SpeciesKit.Gnomes.base import Gnome
from AtlasActorLudi.SpeciesKit.Gnomes.Forest_Gnome import Forest_Gnome
from AtlasActorLudi.SpeciesKit.Gnomes.Rock_Gnome import Rock_Gnome
from AtlasActorLudi.SpeciesKit.Gnomes.traits import Gnomish_Cunning
from AtlasActorLudi.SpeciesKit.declarations import Player_Handbook_2024


GNOME_HERITAGES = (
	Forest_Gnome,
	Rock_Gnome,
	)

Player_Handbook_2024(
	Gnome,
	weight=80,
	size_options=(
		"Small",
		),
	speed=30,
	heritages=GNOME_HERITAGES,
	description=(
		"""Gnomes. Everyone's favourite neighbours, nobody's countrymen. Your family has been in this house for four hundred years, and you will still be asked to go back to the Feywild. But everyone loves what your people made: the lenses, the clockwork, the smoking herbs. These were found not by fae magic, but by curiosity. And in the good years everyone is a friend.

Your own keep their ways in things rather than in land, because land can be taken. A song, a recipe, a pattern in a rug, a joke that only works in the Sylvan tongue: those travel with you. Your grandmother could fit the whole history of your people into a piece of jewellery small enough to swallow, and did, twice.

Think of what {name} carries that is worth more than it looks."""
		),
	)


from AtlasActorLudi.SpeciesKit.Gnomes.resolution import Resolve_Gnome_Features


__all__ = (
	"Forest_Gnome",
	"GNOME_HERITAGES",
	"Gnome",
	"Gnomish_Cunning",
	"Resolve_Gnome_Features",
	"Rock_Gnome",
	)
