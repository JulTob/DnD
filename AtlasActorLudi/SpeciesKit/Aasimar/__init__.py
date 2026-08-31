"""Extensible 2024 Aasimar Species Atlas."""

from AtlasActorLudi.SpeciesKit.Aasimar.base import Aasimar
from AtlasActorLudi.SpeciesKit.Aasimar.Revelations import AASIMAR_REVELATIONS
from AtlasActorLudi.SpeciesKit.Aasimar.Revelations import Celestial_Revelation
from AtlasActorLudi.SpeciesKit.Aasimar.Revelations import Current_Revelation
from AtlasActorLudi.SpeciesKit.Aasimar.Revelations import Talarian_Wings
from AtlasActorLudi.SpeciesKit.Aasimar.Revelations import Inner_Radiance
from AtlasActorLudi.SpeciesKit.Aasimar.Revelations import Necrotic_Shroud
from AtlasActorLudi.SpeciesKit.Aasimar.traits import Celestial_Resistance
from AtlasActorLudi.SpeciesKit.Aasimar.traits import Healing_Hands
from AtlasActorLudi.SpeciesKit.Aasimar.traits import Light_Bearer
from AtlasActorLudi.SpeciesKit.declarations import Player_Handbook_2024


Aasimar.REVELATIONS = AASIMAR_REVELATIONS
Player_Handbook_2024(
	Aasimar,
	weight=75,
	size_options=(
		"Medium",
		"Small",
		),
	speed=30,
	description=(
		"""Angels, Muses, Constellations, Celestials... different cultures call your people by different names. Truth is, you never lived among them. You are mortal, and you are part of one of the many cultures of the world. But you also have something in you from the Higher Planes. Your aspect resembles your mortal side, but you also have tells from your heavenly origin: Talaria, small vestigial wings, and Aureola, a barely perceptible shining halo around your head. You can hide them or empower them depending on your emotional state.

All Celestials are inclined towards a higher ideal: Justice, Sacrifice, Freedom... Think about which ideal can inspire {name} and guide their path as an adventurer."""
		),
	)


from AtlasActorLudi.SpeciesKit.Aasimar.resolution import (
	Resolve_Aasimar_Features,
	)


__all__ = (
	"AASIMAR_REVELATIONS",
	"Aasimar",
	"Celestial_Resistance",
	"Celestial_Revelation",
	"Current_Revelation",
	"Healing_Hands",
	"Talarian_Wings",
	"Inner_Radiance",
	"Light_Bearer",
	"Necrotic_Shroud",
	"Resolve_Aasimar_Features",
	)
