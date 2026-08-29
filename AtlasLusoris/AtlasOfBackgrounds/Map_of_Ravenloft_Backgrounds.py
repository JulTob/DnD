"""Official 2024-format Background records from Ravenloft."""

from AtlasLusoris.AtlasOfBackgrounds.OfficialBackgroundsKit import (
	Register_Backgrounds,
	)
from AtlasLusoris.Grimoire_of_Backgrounds import (
	Background,
	)
from AtlasVenustas import Entry


SOURCE_TITLE = "Ravenloft: The Horrors Within"
SOURCE_URL = "https://www.dndbeyond.com/sources/dnd/rthw"
SOURCE_LOCATOR = "Chapter 1: Character Options — Backgrounds"

RECORDS = (
	Background(
		name="Survivor",
		abilities=(
			"CON",
			"WIS",
			"CHA",
			),
		skills=(
			"Arcana",
			"Survival",
			),
		tool="Gaming_Set",
		origin_feat="Spared",
		origin_feat_options=(
			"Spared",
			"Dark Gift",
			),
		# The archetype is the conversion, not the wound: the trauma made an
		# adventurer, and that works for any class.  The Gaming Set is earned in
		# the hook, not here: the thing stops for a Game, so you carry one.
		description=(
			"""You should not be alive. Everyone agrees on that, including you. Something came, it took the others, and for reasons nobody has ever explained it did not take you. You crawled out of that with your life and nothing else: not your house, not your people, not the version of yourself who could hear a floorboard in the night and go back to sleep.

You were told to put it behind you, kindly, by people who meant well and had not been there. You tried. You lasted a season. Then you understood what separates you from every one of them: they get to live in a world where such things happen to someone else. You do not. You know exactly what is out there, because it had you in its hands and let go.

So you went back. For revenge, and something more. Because you are the one who will. Because sitting still is worse. Because it will happen again to someone else. And because you need to. It has cost you everything it was ever going to cost. You do not sleep. You are frightened almost all the time. You go anyway, and that is not bravery. Bravery is for people who still have something to lose. And this time you are ready for it."""
			),
		hook=Entry(
			title="The Long Acquaintance",
			definition="""It let you go. You have had years to find another explanation and there is none. You did not escape. You were released. Nobody gets out of that by being quick. So you know something nobody else alive has seen. You carry the only expertise of its kind. A mark cut into a door, a particular manner of dying, a smell in a cellar that everybody else walks past. You can tell whether it was left for you, or by something that merely learned from the same teacher. You know what it wants, what it will not do, and the one thing that ever made it stop: the Game. It is playing with you. You can sense it. Smell it. Never see it. And it is still out there, and it is in no hurry at all. It has your face. It has your habits. By now it has the faces of everyone who travels beside you. Every time you have come close it was because you were allowed to. One day you will be allowed all the way in.""",
			),
		),
	Background(
		name="Investigator",
		abilities=(
			"INT",
			"WIS",
			"CHA",
			),
		skills=(
			"Insight",
			"Investigation",
			),
		tool="Disguise_Kit",
		origin_feat="Sharp Eye",
		# The method is never the casualty: the world stopped obeying its
		# premises, and the character kept the method anyway.  Nothing here
		# says what they do with what they find, so alignment stays open.
		description=(
			"""You have an infallible method: Observe. Record. Eliminate. Whatever remains, however unwelcome, is the truth. You have carried that principle into every room you were ever called to, and you have come out with an answer every time: the heir with the candelabra, the butler in the living room, the ice knife the fire melted away. You found them all. You always find them. You marked the position. You dusted the floor, questioned the witnesses, and fixed the hour of the crime; every one of them held. You were correct. Then the remains rose and took their revenge on their killer. It was a rude interruption of your detailed explanation, and it ruined the moment, the mystery, and the whole process of revelation. A complete lack of etiquette!

You did not abandon the method. You went home, you sat up until light, and you began the long and disagreeable work of admitting a new column into the ledger: one for things that are impossible, and that happen, and that must therefore be catalogued like anything else. It has since grown a great deal longer than you would like.

You remain the finest reasoner in any room you enter. It is simply that the world has become a bit unreasonable."""
			),
		hook=Entry(
			title="The Practice",
			definition="""You keep a practice. In a city that is a door with your name on it and a room behind it with two chairs; on the road it is a table at the back of an inn and a word to a boy who knows everybody. It is never difficult to arrange. There is no shortage of people carrying something they cannot say aloud and still be taken seriously. You take them seriously, and word of that travels. So the work arrives without being sought: a client with a retainer and a rehearsed story, a servant sent ahead to ask your terms, an unsigned letter containing a very exact description of a house. And sometimes somebody arrives who is not a client at all, and observes, most pleasantly, that the matter is better left alone. Such callers always come too early. You have learned to take great pleasure in it. Nothing so reliably confirms that a thing wants looking into as a stranger arriving to say that it does not. A practice is somewhere anybody at all may find you seated. And you cannot let a good case alone. The dull you solve on the spot without effort; the interesting own you from the first sentence, and you will follow one into a swamp, a crypt, or somebody else's war, and those travelling with you will not always have been consulted.""",
			),
		),
	Background(
		name="Mist Wanderer",
		abilities=(
			"DEX",
			"CON",
			"WIS",
			),
		skills=(
			"Survival",
			"Stealth",
			),
		tool=(),
		origin_feat="Mist Walker",
		origin_feat_options=(
			"Mist Walker",
			"Other Dark Gift",
			),
		description=(
			"You crossed the Mists and learned to travel quietly through lands "
			"where direction and certainty can both betray you."
			),
		),
	Background(
		name="Spirit Medium",
		abilities=(
			"CON",
			"INT",
			"WIS",
			),
		skills=(
			"Insight",
			"Religion",
			),
		tool="Gaming_Set",
		origin_feat="Gathered Whispers",
		origin_feat_options=(
			"Gathered Whispers",
			"Other Dark Gift",
			),
		# Not "it was done to you": the gift found a listener, not a subject.
		# Fortune Teller looks forward and performs; this one looks back and
		# absorbs.  Grief runs on both sides of the veil.
		description=(
			"""There has been no silence in a long, long time. So long you cannot remember how it started. Faces in the dark. Voices. First you noticed them; then they noticed you. They gathered around you. They needed someone to listen. They speak all at once. They repeat themselves. But you learnt to focus. A board with the letters laid out, a deck gone soft at the corners, a music box with one cracked tooth: give them something to move and one will come forward to use it, and for a while there is a single voice instead of the crowd. An hour of close attention may yield a name, a direction, or a debt owed. What they bring is an apology delivered too late, the place where the second will was put, the name of the last face they saw in the dark. One thing concluded, and then they want to go.

You were chosen because you listen. You have sat with the bereaved through the refusal, the bargaining, and the anger that comes out sideways at whoever is nearest. The dead pass through the very same stages, in the very same order, and are far worse at it, having nothing else to do."""
			),
		hook=Entry(
			title="The Chorus",
			definition="""Wherever people have died, which is everywhere, there is testimony to be had. Set out the board or the cards, and wait. One will come forward. What they offer is not knowledge but grievance. They will name who was in the house because they resented them, tell you where a thing was buried because they worry about it, and describe the eyes in exhaustive detail while being quite unable to put a name to them. Everything they say is bent by what was done to them and by pure feeling, and they are frequently and confidently wrong. But they were present, which no living witness can claim, and they have no reason whatever to protect anybody still breathing. The price is that they notice. When one of them finally passes on, the others see it happen. By morning there is a queue. They follow you out of the house and into the next dungeon. Nobody but you can settle the thing they need settled before they can let go. You cannot decline: you have tried, and found that a spirit has nothing but time, grief, and fury.""",
			),
		),
	)


def Register_Ravenloft_Backgrounds(
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
	"Register_Ravenloft_Backgrounds",
	)
