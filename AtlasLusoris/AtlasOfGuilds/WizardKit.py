"""Wizard Specializations."""

from AtlasLusoris.GuildKit import Build_Specialization
from AtlasLusoris.GuildKit import Wizard


Abjurer = Build_Specialization(
	guild=Wizard,
	name="Abjurer",
	module=__name__,
	)
Diviner = Build_Specialization(
	guild=Wizard,
	name="Diviner",
	module=__name__,
	)
Evoker = Build_Specialization(
	guild=Wizard,
	name="Evoker",
	module=__name__,
	)
Illusionist = Build_Specialization(
	guild=Wizard,
	name="Illusionist",
	module=__name__,
	)

# Bladesinger rides in from Tasha's: the one shelf guest beside the PHB four.

Bladesinger = Build_Specialization(
	guild=Wizard,
	name="Bladesinger",
	module=__name__,
	)

SPECIALIZATIONS = Wizard.SPECIALIZATIONS
