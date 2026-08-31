"""Bard Specializations."""

from AtlasLusoris.GuildKit import Bard
from AtlasLusoris.GuildKit import Build_Specialization


Dance = Build_Specialization(
	guild=Bard,
	name="Dance",
	module=__name__,
	)
Glamour = Build_Specialization(
	guild=Bard,
	name="Glamour",
	module=__name__,
	)
Lore = Build_Specialization(
	guild=Bard,
	name="Lore",
	module=__name__,
	)
Valor = Build_Specialization(
	guild=Bard,
	name="Valor",
	module=__name__,
	)

SPECIALIZATIONS = Bard.SPECIALIZATIONS
