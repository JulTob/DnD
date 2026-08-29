"""The shared 2024 Dwarf Species Shape."""

from TagKit import Imprint

from AtlasActorLudi.SpeciesKit.bases import Humanoid
from AtlasActorLudi.SpeciesKit.bases import Species
from AtlasActorLudi.SpeciesKit.Dwarves.traits import Darkvision
from AtlasActorLudi.SpeciesKit.Dwarves.traits import Dwarven_Resilience
from AtlasActorLudi.SpeciesKit.Dwarves.traits import Dwarven_Toughness
from AtlasActorLudi.SpeciesKit.Dwarves.traits import Stonecunning
from AtlasActorLudi.SpeciesKit.physiology import Imprint_Species


class Dwarf(
	Species,
	Humanoid,
	Darkvision,
	Dwarven_Resilience,
	Dwarven_Toughness,
	Stonecunning,
	):
	"""A resilient Humanoid with an affinity for stone."""

	@Imprint
	def Set_Physiology(
		target,
		size=None,
		):
		Imprint_Species(
			target,
			Dwarf,
			size,
			)
