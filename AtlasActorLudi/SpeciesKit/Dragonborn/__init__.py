"""The modular 2024 Dragonborn Species Atlas."""

from AtlasActorLudi.SpeciesKit.Dragonborn.base import Dragonborn
from AtlasActorLudi.SpeciesKit.Dragonborn.Map_of_Ancestors import DRACONIC_ANCESTORS


from AtlasActorLudi.SpeciesKit.Dragonborn.traits import Breath_Weapon
from AtlasActorLudi.SpeciesKit.Dragonborn.traits import Darkvision
from AtlasActorLudi.SpeciesKit.Dragonborn.traits import Draconic_Ancestry
from AtlasActorLudi.SpeciesKit.Dragonborn.traits import Draconic_Flight
from AtlasActorLudi.SpeciesKit.declarations import Player_Handbook_2024


Player_Handbook_2024(
	Dragonborn,
	weight=100,
	size_options=(
		"Medium",
		),
	speed=30,
	description=(
		"""The children of dragons. Nobody agrees what that means, or where we come from. The children of dragons, and none the wiser for it. Some of us follow them as our rulers, and some of us as masters, and some of us don't follow them anymore. Dragons speak in riddles and proverbs, and we cannot be wasting our lives translating their so-called wisdom. A dragon has no rules.

We have a duty to our clans. We know how to show honor and respect: how to greet a superior and how to greet an equal, which hand takes the cup, what is owed to a house that shelters you and what is owed to one that does not. We learned it from dragons, but we do it for ourselves, to keep the clan ordered and stable. It is our duty. We owe it to each other, to protect our own and the beauty of our ways. We may not be mighty alone, but we are together. We warriors will stand together to watch a new era blossom, a garden for all Dragonborn. From the ashes of dragons, a new flame.

Dragonborn are quite isolated, and rare to find outside their lands. Think of why {name} left home, and which observance you have kept, and which one you have quietly stopped keeping."""
		),
	)


from AtlasActorLudi.SpeciesKit.Dragonborn.resolution import Resolve_Dragonborn_Features


__all__ = (
	"Breath_Weapon",
	"DRACONIC_ANCESTORS",
	"Darkvision",
	"Draconic_Ancestry",
	"Draconic_Flight",
	"Dragonborn",
	"Resolve_Dragonborn_Features",
	)
