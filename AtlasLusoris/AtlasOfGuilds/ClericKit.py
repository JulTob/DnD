"""Cleric Specializations."""

from AtlasLusoris.GuildKit import Build_Specialization
from AtlasLusoris.GuildKit import Cleric


Life = Build_Specialization(
	guild=Cleric,
	name="Life",
	module=__name__,
	)
Light = Build_Specialization(
	guild=Cleric,
	name="Light",
	module=__name__,
	)
Trickery = Build_Specialization(
	guild=Cleric,
	name="Trickery",
	module=__name__,
	)
War = Build_Specialization(
	guild=Cleric,
	name="War",
	module=__name__,
	)

SPECIALIZATIONS = Cleric.SPECIALIZATIONS
