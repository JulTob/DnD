"""The Necrotic Shroud Revelation Shape."""

from TagKit import Imprint

from AtlasActorLudi.SpeciesKit.Aasimar.Revelations.base import (
	Celestial_Revelation,
	)
from AtlasActorLudi.SpeciesKit.Aasimar.Revelations.base import (
	Imprint_Revelation,
	)


class Necrotic_Shroud(Celestial_Revelation):
	"""A necrotic Revelation carrying a frightening shroud."""

	DAMAGE_TYPE = "Necrotic"
	RADIUS = 10
	SAVE_ABILITY = "CHA"
	CONDITION = "Frightened"
	EXCLUDES_ALLIES = True

	@Imprint
	def Set_Revelation(
		target,
		):
		Imprint_Revelation(
			target,
			Necrotic_Shroud,
			)
