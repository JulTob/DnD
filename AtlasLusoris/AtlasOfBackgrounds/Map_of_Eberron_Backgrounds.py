"""Official 2024-format Background records from Eberron."""

from AtlasLusoris.AtlasOfBackgrounds.OfficialBackgroundsKit import (
	Register_Backgrounds,
	)
from AtlasLusoris.Grimoire_of_Backgrounds import (
	Background,
	)
from AtlasVenustas import Entry


SOURCE_TITLE = "Eberron: Forge of the Artificer"
SOURCE_URL = "https://www.dndbeyond.com/sources/dnd/efota"
SOURCE_LOCATOR = "Chapter 2: Character Options — Backgrounds"

RECORDS = (
	Background(
		name="Aberrant Mutant",
		abilities=(
			"STR",
			"CON",
			"CHA",
			),
		skills=(
			"History",
			"Intimidation",
			),
		tool="Disguise_Kit",
		origin_feat="Wild Blood",
		description=(
			"""It is not a gift, and nobody has ever called it one. It came from nowhere anyone can name: no bloodline, no bargain, no book. It was simply in you the way a fault is in stone, and one day it showed. You remember the moment it showed. You remember the faces changing. Since then you have kept a discipline nobody taught you: hands in sight, sleeves long, nothing on your skin that invites a second look. You can change your face, your walk, and the way you hold a cup, and you have done all three in one afternoon. You are pleasant, forgettable, and always aware of the door. When hiding fails you have one thing left, which is that people are afraid of you. You learned to use it, and to hate how well it works. You know your own history better than any scholar, because you went looking: which cities keep a register, which temples call it a sickness and which call it a sin, what the word for you is in six languages, and the names of the ones who were taken. Almost none of them came back. The worst of it is that they are not entirely wrong about you. When it moves it does not always go where you send it, and somebody standing too close pays for that. You have seen it happen. It is the one accusation you cannot argue with, and the one thing you would give anything to fix."""
			),
		hook=Entry(
			title="Who Keeps the List",
			definition="Somebody in every town keeps a list, and you have learned how to find them. The people who collect your kind are organised, and organisation leaves marks: a sign chalked at chest height by a door, a courier who always walks the same round, a house with too few windows and too many visitors, a clerk at the gate who asks one question too many. You can read all of it. Arriving anywhere, you can tell whether they work that town, how heavily, and where they keep their premises and their papers. Those papers are worth far more than the fear that made them. A register of people like you is still a register of people like you: names, streets, families, who was taken and who is out there passing. It is the only map of your own kind that exists, and the people who want you gone are the ones who drew it. The cost is symmetry. The same signs that let you find them mean you are standing where they work. Read a wall wrong, stay too long, or let what is in you show where somebody can see, and the list gains a line. And the list travels. A description written down in one city is a description read aloud in the next.",
			),
		),
	Background(
		name="Archaeologist",
		abilities=(
			"DEX",
			"INT",
			"WIS",
			),
		skills=(
			"History",
			"Survival",
			),
		tool="Cartographer_Tools",
		origin_feat="Skilled",
		description=(
			"You learned to reach old sites, read their remains, and bring "
			"their stories safely back to the present."
			),
		),
	Background(
		name="House Agent",
		abilities=(
			"STR",
			"INT",
			"CHA",
			),
		skills=(
			"Investigation",
			"Persuasion",
			),
		tool=(),
		origin_feat="Lucky",
		description=(
			"You served a dragonmarked house where practical craft, inquiry, "
			"and negotiation advanced its interests."
			),
		),
	Background(
		name="Inquisitive",
		abilities=(
			"CON",
			"INT",
			"CHA",
			),
		skills=(
			"Insight",
			"Investigation",
			),
		tool="Thieves_Tools",
		origin_feat="Alert",
		description=(
			"You built a life from difficult questions, close observation, "
			"and the persistence to follow evidence."
			),
		),
	)


def Register_Eberron_Backgrounds(
		**routes,
		) -> tuple[type, ...]:
	return Register_Backgrounds(
		records=RECORDS,
		source_title=SOURCE_TITLE,
		source_url=SOURCE_URL,
		source_locator=SOURCE_LOCATOR,
		**routes,
		)


__all__ = (
	"Register_Eberron_Backgrounds",
	)
