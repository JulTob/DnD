"""Rogue Specializations."""

from AtlasLusoris.GuildKit import Build_Specialization
from AtlasLusoris.GuildKit import Rogue


ArcaneTrickster = Build_Specialization(
	guild=Rogue,
	name="Arcane Trickster",
	module=__name__,
	)
Assassin = Build_Specialization(
	guild=Rogue,
	name="Assassin",
	module=__name__,
	)
Soulknife = Build_Specialization(
	guild=Rogue,
	name="Soulknife",
	module=__name__,
	)
Thief = Build_Specialization(
	guild=Rogue,
	name="Thief",
	module=__name__,
	)

SPECIALIZATIONS = (
	ArcaneTrickster,
	Assassin,
	Soulknife,
	Thief,
	)
