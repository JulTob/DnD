"""Extensible 2024 Dwarf Species Atlas."""

from AtlasActorLudi.SpeciesKit.Dwarves.base import Dwarf
from AtlasActorLudi.SpeciesKit.Dwarves.traits import Darkvision
from AtlasActorLudi.SpeciesKit.Dwarves.traits import Dwarven_Resilience
from AtlasActorLudi.SpeciesKit.Dwarves.traits import Dwarven_Toughness
from AtlasActorLudi.SpeciesKit.Dwarves.traits import Stonecunning
from AtlasActorLudi.SpeciesKit.declarations import Player_Handbook_2024


Player_Handbook_2024(
	Dwarf,
	weight=100,
	size_options=(
		"Medium",
		),
	speed=30,
	description=(
		"""Dwarves. They remember. Your people ruled the world once. Then the Great Mountain fell, the Guilded Era ended with it, and the dwarves spread out across the world instead, carrying their ledgers and their grudges.

Metal is holy to your people. Everything the dwarves ever built, they built while chasing it: the mines, the bank-cathedrals, the fleets, and the long terrible expeditions. Others call it greed. Greed is not the only reason. Gold never corrupts. A gilded prayer to your Saints and Ancestors will never weaken.

What holds now is the clan. Come back home with enough gold, and your clan will hail you as a hero, no matter your past transgressions.

Think, adventurer: what will you do with the gold you carry home? Raise a shrine to a Saint? Open a Bank Temple? Or spend it on spices and mead?"""
		),
	)


from AtlasActorLudi.SpeciesKit.Dwarves.resolution import Resolve_Dwarf_Features


__all__ = (
	"Darkvision",
	"Dwarf",
	"Dwarven_Resilience",
	"Dwarven_Toughness",
	"Resolve_Dwarf_Features",
	"Stonecunning",
	)
