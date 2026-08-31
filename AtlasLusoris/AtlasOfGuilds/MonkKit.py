"""Monk Specializations."""

from AtlasLusoris.GuildKit import Build_Specialization
from AtlasLusoris.GuildKit import Monk


Mercy = Build_Specialization(
	guild=Monk,
	name="Mercy",
	module=__name__,
	)
OpenHand = Build_Specialization(
	guild=Monk,
	name="Open Hand",
	module=__name__,
	)
Shadow = Build_Specialization(
	guild=Monk,
	name="Shadow",
	module=__name__,
	)
Elements = Build_Specialization(
	guild=Monk,
	name="Elements",
	module=__name__,
	)

SPECIALIZATIONS = (
	Mercy,
	OpenHand,
	Shadow,
	Elements,
	)
