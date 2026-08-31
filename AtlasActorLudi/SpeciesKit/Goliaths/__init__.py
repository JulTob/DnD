"""Extensible 2024 Goliath Species Atlas."""

from AtlasActorLudi.SpeciesKit.Goliaths.base import Goliath
from AtlasActorLudi.SpeciesKit.Goliaths.Giant_Heritages import Clouds_Jaunt
from AtlasActorLudi.SpeciesKit.Goliaths.Giant_Heritages import Current_Giant_Heritage
from AtlasActorLudi.SpeciesKit.Goliaths.Giant_Heritages import Fires_Burn
from AtlasActorLudi.SpeciesKit.Goliaths.Giant_Heritages import Frosts_Chill
from AtlasActorLudi.SpeciesKit.Goliaths.Giant_Heritages import Giant_Heritage
from AtlasActorLudi.SpeciesKit.Goliaths.Giant_Heritages import GOLIATH_GIANT_HERITAGES
from AtlasActorLudi.SpeciesKit.Goliaths.Giant_Heritages import Hills_Tumble
from AtlasActorLudi.SpeciesKit.Goliaths.Giant_Heritages import Stones_Endurance
from AtlasActorLudi.SpeciesKit.Goliaths.Giant_Heritages import Storms_Thunder
from AtlasActorLudi.SpeciesKit.Goliaths.traits import Large_Form
from AtlasActorLudi.SpeciesKit.Goliaths.traits import Powerful_Build
from AtlasActorLudi.SpeciesKit.declarations import Player_Handbook_2024


Goliath.GIANT_HERITAGES = GOLIATH_GIANT_HERITAGES
Player_Handbook_2024(
	Goliath,
	weight=75,
	size_options=(
		"Medium",
		),
	speed=35,
	description=(
		"""Giants manifested before the first things. And Giants are your ancestors. Before anyone had a word for Winter, she had a name and a temper. Your ancestors did not command the avalanche. They were the avalanche, and the mountain, and the thunder. The gods took the heavens and the songs. The First Ones kept the world, having never stopped being it. They are still here, if you know how to look at a mountain.

Some of them turned and made something much smaller, and gave it life, and many favors. Each Goliath carries one, and knows which giant it came from the way other people know a surname. We tend the world, and everything they made, for that is our duty as Goliaths. Remember, young one: we are part of this world, part of The Order of Things, from the breathing sky to the living earth. We are part of them, and we wander to see them, and everything they made, with respect and awe. We are not static. We grow. And our strength is not our might, but our duty.

Think of why {name} would leave their community, and what your responsibilities are to The Order of Things. Do you respect and protect the land? Do you rage with the storm? Or do you observe the cycles of the night sky?"""
		),
	)


from AtlasActorLudi.SpeciesKit.Goliaths.resolution import Resolve_Goliath_Features


__all__ = (
	"Clouds_Jaunt",
	"Current_Giant_Heritage",
	"Fires_Burn",
	"Frosts_Chill",
	"Giant_Heritage",
	"GOLIATH_GIANT_HERITAGES",
	"Goliath",
	"Hills_Tumble",
	"Large_Form",
	"Powerful_Build",
	"Resolve_Goliath_Features",
	"Stones_Endurance",
	"Storms_Thunder",
	)
