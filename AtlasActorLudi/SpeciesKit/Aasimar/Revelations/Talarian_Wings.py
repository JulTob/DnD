"""The Talarian Wings Revelation Shape."""

from TagKit import Imprint

from AtlasActorLudi.SpeciesKit.Aasimar.Revelations.base import (
	Celestial_Revelation,
	)
from AtlasActorLudi.SpeciesKit.Aasimar.Revelations.base import (
	Imprint_Revelation,
	)


class Talarian_Wings(Celestial_Revelation):
	"""A radiant Revelation carrying spectral flight."""

	DAMAGE_TYPE = "Radiant"
	FLY_SPEED = "Speed"

	@Imprint
	def Set_Revelation(
		target,
		):
		Imprint_Revelation(
			target,
			Talarian_Wings,
			)
