"""Paladin Specializations."""

from AtlasLusoris.GuildKit import Build_Specialization
from AtlasLusoris.GuildKit import Paladin


Ancients = Build_Specialization(
	guild=Paladin,
	name="Ancients",
	module=__name__,
	)
Devotion = Build_Specialization(
	guild=Paladin,
	name="Devotion",
	module=__name__,
	)
Glory = Build_Specialization(
	guild=Paladin,
	name="Glory",
	module=__name__,
	)
Vengeance = Build_Specialization(
	guild=Paladin,
	name="Vengeance",
	module=__name__,
	)

SPECIALIZATIONS = (
	Ancients,
	Devotion,
	Glory,
	Vengeance,
	)
