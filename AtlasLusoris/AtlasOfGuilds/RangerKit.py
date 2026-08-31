"""Ranger Specializations."""

from AtlasLusoris.GuildKit import Build_Specialization
from AtlasLusoris.GuildKit import Ranger


BeastMaster = Build_Specialization(
	guild=Ranger,
	name="Beast Master",
	module=__name__,
	)
FeyWanderer = Build_Specialization(
	guild=Ranger,
	name="Fey Wanderer",
	module=__name__,
	)
GloomStalker = Build_Specialization(
	guild=Ranger,
	name="Gloom Stalker",
	module=__name__,
	)
Hunter = Build_Specialization(
	guild=Ranger,
	name="Hunter",
	module=__name__,
	)

SPECIALIZATIONS = Ranger.SPECIALIZATIONS
