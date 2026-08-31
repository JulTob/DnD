"""The extensible 2024 Tiefling Species Atlas."""

from AtlasActorLudi.SpeciesKit.Tieflings.Abyssal import Abyssal
from AtlasActorLudi.SpeciesKit.Tieflings.base import Tiefling
from AtlasActorLudi.SpeciesKit.Tieflings.Chthonic import Chthonic
from AtlasActorLudi.SpeciesKit.Tieflings.Infernal import Infernal
from AtlasActorLudi.SpeciesKit.Tieflings.traits import Fiendish_Legacy
from AtlasActorLudi.SpeciesKit.Tieflings.traits import Otherworldly_Presence
from AtlasActorLudi.SpeciesKit.declarations import Player_Handbook_2024


TIEFLING_HERITAGES = (
	Abyssal,
	Chthonic,
	Infernal,
	)

Player_Handbook_2024(
	Tiefling,
	weight=75,
	size_options=(
		"Medium",
		"Small",
		),
	speed=30,
	heritages=TIEFLING_HERITAGES,
	description=(
		"""Nobody teaches you what you are. There is no homeland where everyone has horns. You were born to ordinary parents, but the midwife went quiet, and that was how it began.

Your blood runs down to the Lower Planes, and everyone can see it. So the rate at the inn goes up, and the guard walks you to the edge of town to be sure, and once in a while somebody takes a swing in a crowded square and not one hand moves to stop it. You have never done anything. That has never been relevant.

And then somebody like you finds you. They pay the fine, or they feed you, or they simply say the word, but not as the insult it is: Tiefling. That is how it works. Some of us can pass under a hood, and the ones who cannot are never left alone. Children in that house are nobody's, and they are ours. Somebody there will tell you the horns are crowns that used to hold a shining flame, and that we were the chosen, long before. It's a beautiful fantasy. Others say we should claim our place in the Nine Hells, and hit back harder. We carry fire, that's certain, but it can be used for a warm home or for a burning inferno.

Think about how your experiences as a Tiefling have shaped your path, and how {name} would approach new people during the campaign."""
		),
	)


from AtlasActorLudi.SpeciesKit.Tieflings.resolution import (
	Resolve_Tiefling_Features,
	)


__all__ = (
	"Abyssal",
	"Chthonic",
	"Fiendish_Legacy",
	"Infernal",
	"Otherworldly_Presence",
	"Resolve_Tiefling_Features",
	"TIEFLING_HERITAGES",
	"Tiefling",
	)
