"""Sorcerer Specializations."""

from AtlasLusoris.GuildKit import Build_Specialization
from AtlasLusoris.GuildKit import Sorcerer


AberrantSorcery = Build_Specialization(
	guild=Sorcerer,
	name="Aberrant Sorcery",
	module=__name__,
	)
ClockworkSorcery = Build_Specialization(
	guild=Sorcerer,
	name="Clockwork Sorcery",
	module=__name__,
	)
DraconicSorcery = Build_Specialization(
	guild=Sorcerer,
	name="Draconic Sorcery",
	module=__name__,
	)
WildMagicSorcery = Build_Specialization(
	guild=Sorcerer,
	name="Wild Magic Sorcery",
	module=__name__,
	)

SPECIALIZATIONS = (
	AberrantSorcery,
	ClockworkSorcery,
	DraconicSorcery,
	WildMagicSorcery,
	)
