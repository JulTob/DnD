"""Extensible 2024 Elf Species Atlas."""

from AtlasActorLudi.SpeciesKit.Elves.base import Elf
from AtlasActorLudi.SpeciesKit.Elves.Dark_Elf import Dark_Elf
from AtlasActorLudi.SpeciesKit.Elves.Fae_Elf import Fae_Elf
from AtlasActorLudi.SpeciesKit.Elves.High_Elf import High_Elf
from AtlasActorLudi.SpeciesKit.Elves.Shadow_Elf import Shadow_Elf
from AtlasActorLudi.SpeciesKit.Elves.Wood_Elf import Wood_Elf
from AtlasActorLudi.SpeciesKit.Elves.traits import Darkvision
from AtlasActorLudi.SpeciesKit.Elves.traits import Fey_Ancestry
from AtlasActorLudi.SpeciesKit.Elves.traits import Keen_Senses
from AtlasActorLudi.SpeciesKit.Elves.traits import Trance
from AtlasActorLudi.SpeciesKit.declarations import Player_Handbook_2024


ELF_HERITAGES = (
	Dark_Elf,
	Fae_Elf,
	High_Elf,
	Shadow_Elf,
	Wood_Elf,
	)

Player_Handbook_2024(
	Elf,
	weight=100,
	size_options=(
		"Medium",
		),
	speed=30,
	heritages=ELF_HERITAGES,
	description=(
		"""The Other People. That's us, the elves. The pointed ears, the white pupils, and the dreamy beauty. Our people came out of the Fae so long ago that it is myth instead of history: painted faces hunting intruders in the woods, icy ships conquering seas, ambushers who came from below. War after war, we fought each other, but now one word unites us: Elvenkind. Those centuries of war are forgotten, even by the ones who shoot the arrows.

Today a long peace holds, and it holds because nobody is counting grudges any more. But peace also needs arrow and spell to defend it. You belong to your nature, the elders say, but civilization brought us a higher purpose, skillful magic, and allies. Warmongers, Dark Lords and Separatists still try to bring war back to elven shores. But we also have adventurers among us! Adventurers like yourself! All you need against them is patience and a full quiver. You have seven hundred years to be patient in, and you only need one second to shoot.

Think about your life before leaving your elven home. What was your young first century like? What values did you adopt? The old grudges, or the new peace?"""
		),
	)


from AtlasActorLudi.SpeciesKit.Elves.resolution import Resolve_Elf_Features


__all__ = (
	"Darkvision",
	"Dark_Elf",
	"ELF_HERITAGES",
	"Fae_Elf",
	"Elf",
	"Fey_Ancestry",
	"High_Elf",
	"Keen_Senses",
	"Resolve_Elf_Features",
	"Shadow_Elf",
	"Trance",
	"Wood_Elf",
	)
