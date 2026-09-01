"""Artificer Specializations."""

from AtlasLusoris.GuildKit import Artificer
from AtlasLusoris.GuildKit import Build_Specialization


Alchemist = Build_Specialization(
	guild=Artificer,
	name="Alchemist",
	module=__name__,
	)
Armorer = Build_Specialization(
	guild=Artificer,
	name="Armorer",
	module=__name__,
	)
Artillerist = Build_Specialization(
	guild=Artificer,
	name="Artillerist",
	module=__name__,
	)
BattleSmith = Build_Specialization(
	guild=Artificer,
	name="Battle Smith",
	module=__name__,
	)

SPECIALIZATIONS = (
	Alchemist,
	Armorer,
	Artillerist,
	BattleSmith,
	)
