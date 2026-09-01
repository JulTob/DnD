"""The Inner Radiance Revelation Shape."""

from TagKit import Imprint

from AtlasActorLudi.SpeciesKit.Aasimar.Revelations.base import (
	Celestial_Revelation,
	)
from AtlasActorLudi.SpeciesKit.Aasimar.Revelations.base import (
	Imprint_Revelation,
	)


class Inner_Radiance(Celestial_Revelation):
	"""A radiant Revelation carrying a searing aura."""

	DAMAGE_TYPE = "Radiant"
	BRIGHT_LIGHT_RADIUS = 10
	DIM_LIGHT_ADDITIONAL_RADIUS = 10
	AURA_RADIUS = 10

	@Imprint
	def Set_Revelation(
		target,
		):
		Imprint_Revelation(
			target,
			Inner_Radiance,
			)
