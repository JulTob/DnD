"""Druid Specializations."""

from AtlasLusoris.GuildKit import Build_Specialization
from AtlasLusoris.GuildKit import Druid


Land = Build_Specialization(
	guild=Druid,
	name="Land",
	module=__name__,
	)
Moon = Build_Specialization(
	guild=Druid,
	name="Moon",
	module=__name__,
	)
Sea = Build_Specialization(
	guild=Druid,
	name="Sea",
	module=__name__,
	)
Stars = Build_Specialization(
	guild=Druid,
	name="Stars",
	module=__name__,
	)

SPECIALIZATIONS = (
	Land,
	Moon,
	Sea,
	Stars,
	)
