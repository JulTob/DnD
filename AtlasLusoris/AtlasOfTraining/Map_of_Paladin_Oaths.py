"""
The Oath a Paladin actually says.

The Guild text says a principle is held. This is the principle spoken, and it
is the one place on a whole sheet where the Character talks instead of being
talked about. Six lines in the middle of the page are the player's own mouth,
written to be read aloud at a table, and written to make the reader a
believer.

**Each Oath consults its own poet.** The Cleric reads prayers; the Paladin is
the one Guild tied to a poem, so its four Oaths are written in four registers,
chosen by Julio, and nothing in a Devotion oath sounds like a Vengeance oath:

	Devotion    the Psalms, the reverence of the King James
	Ancients    Shakespeare, the touch and the wonder, the green
	Glory       Twain and Espronceda, Moore and Gaiman: the swagger of the told
	Vengeance   Byron, the midnight and the storm

**It is assembled, never chosen.** Six slots, six pools, the way an Aasimar's
aureola takes form, gem and tell from different Ideals. Every pool is written
in the Oath's own register, so the six lines cohere as one poem. Exactly two
lines are then personal, on Julio's ruling that the personalization should be
small: the heart comes from the people, the word from the life before, each
drawn with preference from a small pool where every line had to earn its
place. Nothing else varies by tag. The culture keys are not an axis here; the
poets who wrote the species lines were told to use them as inspiration for
diction, never as a list to fill. Where no line sings for a people, the
Oath's own voice carries.

**Death of the author.** No line here hands the Character a past. A line may
say what they are, because the sheet already says so, and never what happened
to them. The day they swore, the wrong they saw and the face they remember are
the player's, and the lines are left open enough to hold whatever the player
puts in them. Dragonheart in the epic, not in the structure.
"""

from __future__ import annotations

from dataclasses import dataclass


DEVOTION = "Devotion"
ANCIENTS = "Ancients"
GLORY = "Glory"
VENGEANCE = "Vengeance"
CREATION = "Creation"


@dataclass(
	frozen=True,
	slots=True,
	)
class Oath_Register:
	"""One Oath's poet, and every pool written in that poet's voice."""

	name: str
	# How the Oath is named in "You swore an oath to ...": the Ancients take
	# their article, the others do not.
	sworn_to: str
	# Completes "To be a paragon of ...", the line that opens the recital.
	paragon: str
	poets: str
	vows: tuple[str, ...]
	hearts: tuple[str, ...]
	arms: tuple[str, ...]
	words: tuple[str, ...]
	refusals: tuple[str, ...]
	closes: tuple[str, ...]


# ---------------------------------------------------------------------------
# The four registers
# ---------------------------------------------------------------------------


REGISTERS = {
	DEVOTION: Oath_Register(
		name=DEVOTION,
		sworn_to="Devotion",
		paragon="constancy and truth",
		poets="the Psalms; the King James",
		vows=(
			"I am sworn to the Eternal Truth.",
			"I am sworn to stand unbent and unbroken.",
			"I am sworn unto the Truth; it is my rock and my high tower.",
			"I am sworn to walk uprightly, though the whole earth be moved.",
			),
		hearts=(
			"My heart is set as a flint, and it shall not be turned.",
			"My heart is a lamp that goeth not out by night.",
			"My heart hath one law, and keepeth it, and seeketh no other.",
			"My heart is a stronghold, and the gates of it stand open.",
			),
		arms=(
			"My blade is bright. Nothing I do is done in the dark.",
			"My arm is lifted in the daylight, and my hand knoweth no secret work.",
			"My sword is girded on before all eyes, and it is a clean sword.",
			"My blade hath never once been drawn in secret.",
			),
		words=(
			"My word is yea, and my word is nay, and there is no third word in me.",
			"My word is given once; heaven and earth shall pass before it is taken back.",
			"My word hath been given to the unworthy, and kept. This word is kept likewise.",
			"My word standeth. Let the mountains be removed; my word standeth.",
			),
		refusals=(
			"I will not bow, though the seven hills bow down.",
			"I will not stand in the way of the crooked, nor sit where the mockers sit.",
			"I will not lie, though the lie would save me, nor flee, though the truth would slay me.",
			"I will not bend, not for the friend who begs, not for the king who commands.",
			),
		closes=(
			"And if I am the last one keeping it, it is still kept.",
			"Though all the world forsake it, it shall not be forsaken.",
			"This is my portion, and I shall not want another.",
			"So it standeth, and so I stand.",
			),
		),
	ANCIENTS: Oath_Register(
		name=ANCIENTS,
		sworn_to="the Ancients",
		paragon="the green and the returning light",
		poets="Shakespeare; the Green Knight",
		vows=(
			"I am sworn to what was and what will be.",
			"I am sworn to the light. Even the night has stars.",
			"I am sworn to the green, which has outlasted every fire.",
			"I am sworn to the spring, that comes though no one bid it come.",
			"I am sworn to the sweet o' the year, and to its keeping.",
			),
		hearts=(
			"My heart is a wood in winter, and knows the green sleeps and is not dead.",
			"My heart keeps a garden no frost has ever taken.",
			"My heart is old as the oak and light as the leaf upon it.",
			"My heart is made of such stuff as springs are made on.",
			),
		arms=(
			"My blade is for the winter, and the winter is patient.",
			"My blade stands between the small green thing and the frost.",
			"My sword is a bough of the old tree, and it remembers the root.",
			"My blade is a young thing, and it serves a very old one.",
			),
		words=(
			"My word is kept as the year is kept: the spring comes because it was promised.",
			"My word is given as the oak gives shade, to whoever stands beneath.",
			"My word was whispered to the wood, and the wood has not forgotten.",
			"My word is a seed. Bury it, and see what comes up.",
			),
		refusals=(
			"I will not let the light go out, though the night be long as winter.",
			"I will not curse the frost. I will outlast it.",
			"I will not mistake one felled tree for the end of the forest.",
			"I will not weep for the fallen leaf while the bough still lives.",
			),
		closes=(
			"My sorrow will not stop the grass.",
			"Let it go out everywhere else. It will not go out in me.",
			"The green comes back. It always has. I am here to see that it does.",
			"Winter is a season. I am the one after.",
			),
		),
	GLORY: Oath_Register(
		name=GLORY,
		sworn_to="Glory",
		paragon="valour and renown",
		poets="Twain and Espronceda; Moore and Gaiman",
		vows=(
			"I am sworn to valour.",
			"I am sworn to be worth the song.",
			"I am sworn to the deed that outlives the doer.",
			"I am sworn to the story, and the story is not finished with me.",
			),
		hearts=(
			"My heart is a ship, my treasure the horizon, my only country the sea.",
			"My heart was built for a story bigger than a life, and has grown to fit it.",
			"My heart laughs at the odds. The odds have never once laughed back.",
			"My heart is the drum they march to, and it has never missed a beat.",
			),
		arms=(
			"My blade goes first. It has always gone first.",
			"My blade is for the moment the song will need.",
			"My blade writes the verse they will sing loudest.",
			"My sword is my law and the wind, and I answer to no other.",
			),
		words=(
			"My word is my name, and my name is not for sale.",
			"My word is the one thing I never sold, and I sold a great deal.",
			"My word is a promise to the poets: I will give them something worth the rhyme.",
			"My word travels ahead of me, and arrives before I do.",
			),
		refusals=(
			"I will not die in bed. I have been offered it.",
			"I will not be the footnote. I will be the chapter.",
			"I will not choose the long life. I have been offered it.",
			"I will not fold. I have never once folded.",
			),
		closes=(
			"If I fall, that is the life I chose. Nothing lost, but me.",
			"Say it after me, and say it right.",
			"They will tell it wrong. Tell it wrong in my favour.",
			"I would rather be the story than the one who lived it.",
			),
		),
	# Sworn to Creation. The maker's register: Lorca's short line that cuts,
	# Neruda's odes to elemental things, Scheherazade's creation by telling.
	# Physics for the mortal winks, Genesis for the divine ones. The dark edge
	# is the demiurge's: you answer for everything you make and unmake none of
	# it, and the text never says the maker is good.
	CREATION: Oath_Register(
		name=CREATION,
		sworn_to="Creation",
		paragon="making",
		poets="Lorca; Neruda's Odas elementales; Scheherazade",
		vows=(
			"I am sworn to what is not yet, and to making it so.",
			"I am sworn to the four elements, and to the fifth, the word.",
			"I am sworn to the first light, the one that came before the sun.",
			"I am sworn to make, and to answer for the made.",
			),
		hearts=(
			"My heart is a forge with no smith in it but me.",
			"My heart is the salt in the sea and the salt on the bread. It made both.",
			"My heart is clay that remembers the hands, and the hands were mine.",
			"My heart holds a word no page can hold. I say it.",
			),
		arms=(
			"My blade is earth, then air, then fire, then water, as I say.",
			"My sword was the first thing I made, and it is not finished yet.",
			"My arm moves the world. Give it a place to stand.",
			"My blade writes in four elements what no ink can write.",
			),
		words=(
			"My word is spoken, never written, and the world leans toward it.",
			"My word is the lamp and the light. I say it, and there is.",
			"My word is a seed dropped in the dark. It does not ask leave to grow.",
			"My word was the first mover. Everything since has been moved.",
			),
		refusals=(
			"I will not unmake what I have made. I will answer for it.",
			"I will not wait for a god to say it first.",
			"I will not leave the world as I found it.",
			"I will not call it finished. Nothing I have made is finished.",
			),
		closes=(
			"Let there be. And there was.",
			"I made this. Look at it.",
			"The seventh day is not for me. There is more to make.",
			"Say the word after me. Now watch the world.",
			),
		),
	VENGEANCE: Oath_Register(
		name=VENGEANCE,
		sworn_to="Vengeance",
		paragon="retribution and justice",
		poets="Byron",
		vows=(
			"I am sworn against the perpetrators of injustice.",
			"I am sworn to the reckoning, and the reckoning wears my face.",
			"I am sworn to be the storm they prayed would never break.",
			"I am sworn to hunt what the law forgave.",
			),
		hearts=(
			"My heart rides the storm, and my arm wields the thunder.",
			"My heart is a midnight that keeps one lamp burning.",
			"My heart was broken once, and what remained of it is iron.",
			"My heart keeps a ledger, written in a hand that does not shake.",
			),
		arms=(
			"My blade carries the names and balances their crimes.",
			"My blade is the last argument, and I have never lost it.",
			"My blade does not hate. Hatred tires. My blade remembers.",
			"My blade comes down like the wolf upon the fold.",
			),
		words=(
			"My word is fair, but never kind. It is strong, and it never negotiates.",
			"My word was given to the dead, and the dead do not release you.",
			"My word is the one debt I have never let run past its day.",
			"My word is a sentence passed, and I am its executioner.",
			),
		refusals=(
			"I will not be the one who put down my shield or my word.",
			"I will not forgive what was never confessed.",
			"I will not sleep while the guilty sleep soundly.",
			"I will not be told that it was long ago.",
			),
		closes=(
			"I am the rider that brings the storm.",
			"Let them run. The storm runs faster.",
			"It ends. I have decided that it ends.",
			"They made me. Let them look upon what they made.",
			),
		),
	}


# ---------------------------------------------------------------------------
# Grace notes: the people, and the life before
#
# Sparse on purpose. A line lives here only where the tag gave the poem
# something, and a people with no line simply speaks in the Oath's own voice.
# Each empowers the species fantasy rather than arguing with it: the Aasimar
# owns being chosen, because the Paladin is the one Aasimar who chooses back.
# ---------------------------------------------------------------------------


SPECIES_HEARTS = {
	"Aasimar": (
		"My heart carries a spark of greatness. I was chosen.",
		"I was chosen. I chose back, and mine was the louder yes.",
		"My heart holds the stars. My arm carries the might.",
		),
	"Dwarf": (
		"My soul is golden, and gold never corrupts.",
		"My heart was made in the forge of my clan.",
		),
	"Orc": (
		"My heart rides the storm, and the winds will carry me.",
		"My heart is the heart of a rider, and a rider does not turn back.",
		),
	"Halfling": (
		"My heart is small, and there is no room in it for fear.",
		"My heart carries the homeland, and the stories I will tell.",
		),
	"Tiefling": (
		"My heart was alone. No more.",
		"My heart protects the ones like me: born alone.",
		),
	"Human": (
		"My heart is true, and my friends are my rest.",
		"My heart is brief, and burns the brighter for it.",
		),
	"Elf": (
		"My heart has all the time there is, and spends it here.",
		),
	"Goliath": (
		"My heart carries the weight of the world, and is not bent by it.",
		"My heart came down from a fallen height, and kept the height.",
		),
	"Dragonborn": (
		"My heart keeps the old courtesies, and keeps them to the death.",
		),
	"Gnome": (
		"My heart is astonished by the world, and always was.",
		),
	}


# Backgrounds cluster by what a person's word was worth before this one.
WORD_CLUSTERS = {
	"sworn": (
		"Acolyte", "Bailiff", "Guard", "Herald", "Inquisitor",
		"Noble", "Soldier", "Squire",
		),
	"held": (
		"Artisan", "Farmer", "Merchant", "Servant",
		),
	"outside": (
		"Charlatan", "Criminal", "Gambler", "Renegade", "Revolutionary",
		"Sellsword", "Shadow",
		),
	"learned": (
		"Archaeologist", "Debunker", "Hermeticist", "Investigator",
		"Naturalist", "Sage", "Scribe",
		),
	"wandering": (
		"Guide", "Ice Nomad", "Sailor", "Stranger", "Survivalist",
		"Tomb Raider", "Vagabond", "Wayfarer",
		),
	"marked": (
		"Aberrant Mutant", "Arcane Mutant", "Destined", "Dragon Cultist",
		"Exorcist", "Fated", "Fortune Teller", "Spirit Medium",
		),
	"alone": (
		"Hermit", "Wildkeeper",
		),
	"watched": (
		"Entertainer",
		),
	"lost": (
		"Survivor",
		),
	}

BACKGROUND_WORDS = {
	"sworn": (
		"My word was given before, to lesser things, and kept.",
		),
	"held": (
		"My word was the only thing about me that nobody else owned.",
		),
	"outside": (
		"My word is the one thing I never sold, and I sold a great deal.",
		),
	"wandering": (
		"My word travels ahead of me, and arrives before I do.",
		),
	"marked": (
		"My word is the part of my fate I got to write.",
		),
	"alone": (
		"My word was given where nobody could hear it.",
		),
	"lost": (
		"My word outlived everything else I had. It will outlive me too.",
		),
	}


# A personal line outweighs one line of the Oath's own pool by this much. Kept
# low so the Oath's register carries the poem and the personal lines land as
# grace notes rather than as a second voice.
GRACE_WEIGHT = 3


# ---------------------------------------------------------------------------
# Reading the Character
# ---------------------------------------------------------------------------


def _first_string(
		char,
		*attributes,
		) -> str | None:
	"""The first named attribute that holds a non-empty string."""
	for attribute in attributes:
		value = getattr(
				char,
				attribute,
				None,
				)
		if isinstance(
				value,
				str,
				) and value:
			return value
	return None


def _oath_of(
		char,
		) -> str | None:
	return _first_string(
			char,
			"specialization",
			"Specialization",
			"subclass",
			"Subclass",
			)


def _species_of(
		char,
		) -> str | None:
	return _first_string(
			char,
			"species",
			"Species",
			"race",
			"Race",
			)


def _background_of(
		char,
		) -> str | None:
	return _first_string(
			char,
			"background",
			"Background",
			)
def _cluster_of(
		background: str | None,
		) -> str | None:
	if not background:
		return None
	for cluster, members in WORD_CLUSTERS.items():
		if background in members:
			return cluster
	return None


def _register_of(
		char,
		) -> Oath_Register:
	"""The Oath's register, or Devotion's before an Oath is sworn."""
	return REGISTERS.get(
			_oath_of(
				char
				),
			REGISTERS[ DEVOTION ],
			)


# ---------------------------------------------------------------------------
# Assembling the six lines
# ---------------------------------------------------------------------------


def _weighted(
		own,
		grace,
		) -> tuple[tuple[str, int], ...]:
	"""The Oath's own lines at one, the grace notes at GRACE_WEIGHT, no repeats."""
	seen: set[str] = set()
	pool: list[tuple[str, int]] = []

	for line, weight in grace:
		if line in seen:
			continue
		seen.add(
			line
			)
		pool.append(
			(
				line,
				weight,
				)
			)

	for line in own:
		if line in seen:
			continue
		seen.add(
			line
			)
		pool.append(
			(
				line,
				1,
				)
			)

	return tuple(
		pool
		)


def _draw(
		char,
		pool,
		purpose: str,
		) -> str | None:
	"""One line from a weighted pool, against a named Dice Bag."""
	entries = [
		pair
		for pair in pool
		if pair[ 0 ]
		]
	if not entries:
		return None

	return char.Pick(
			[
				line
				for line, _ in entries
				],
			[
				weight
				for _, weight in entries
				],
			dice=char.Dice_Bag(
				purpose,
				version="2",
				namespace="GenLegendLusoris",
				),
			)


def _species_grace(
		char,
		):
	return tuple(
		(
			line,
			GRACE_WEIGHT,
			)
		for line in SPECIES_HEARTS.get(
			_species_of(
				char
				),
			(),
			)
		)


def _background_grace(
		char,
		):
	return tuple(
		(
			line,
			GRACE_WEIGHT,
			)
		for line in BACKGROUND_WORDS.get(
			_cluster_of(
				_background_of(
					char
					)
				),
			(),
			)
		)
def Compose_Oath(
		char,
		) -> tuple[str, ...]:
	"""
	The six lines, in order, for this Character.

	Pure assembly: it draws but decides nothing that outlives the call.
	``Draw_Oath`` owns the settling and this owns the shape.
	"""
	voice = _register_of(
			char
			)

	slots = (
		(
			"paladin.oath.vow",
			_weighted(
				voice.vows,
				(),
				),
			),
		(
			"paladin.oath.heart",
			_weighted(
				voice.hearts,
				_species_grace(
					char
					),
				),
			),
		(
			"paladin.oath.arm",
			_weighted(
				voice.arms,
				(),
				),
			),
		(
			"paladin.oath.word",
			_weighted(
				voice.words,
				_background_grace(
					char
					),
				),
			),
		(
			"paladin.oath.refusal",
			_weighted(
				voice.refusals,
				(),
				),
			),
		(
			"paladin.oath.close",
			_weighted(
				voice.closes,
				(),
				),
			),
		)

	lines = []
	for purpose, pool in slots:
		line = _draw(
				char,
				pool,
				purpose,
				)
		if line:
			lines.append(
				line
				)

	return tuple(
		lines
		)


def Draw_Oath(
		char,
		) -> tuple[str, ...]:
	"""
	Settle what this Paladin swore, once.

	Called from a lesson's ``apply``, never from its Entry. An Entry that
	draws re-draws on every read of the sheet, which is the Primal Order
	mistake recorded in Canon/Feature-Text.
	"""
	standing = getattr(
			char,
			"paladin_oath_lines",
			None,
			)
	if standing:
		return tuple(
			standing
			)

	lines = Compose_Oath(
			char,
			)
	char.paladin_oath_lines = lines

	return lines


def Oath_Entry(
		char,
		) -> str:
	"""
	The recital as one block: what was sworn, and the words.

		You swore an oath to Vengeance. To be a paragon of retribution and justice:
		I am sworn against the perpetrators of injustice.
		...

	Set roman, one line to a line, so it reads as a code carved somewhere
	rather than as a quotation. Breaks are written and never inferred, per
	Canon/Feature-Text, so every line after the first carries its own ``<br>``
	from here, in the source.
	"""
	lines = getattr(
			char,
			"paladin_oath_lines",
			None,
			) or ()
	if not lines:
		return ""

	voice = _register_of(
			char
			)
	opening = (
		f"You swore an oath to {voice.sworn_to}. "
		f"To be a paragon of {voice.paragon}:"
		)

	return "<br>".join(
			(
				opening,
				*lines,
				)
			)


__all__ = (
	"Oath_Register",
	"REGISTERS",
	"SPECIES_HEARTS",
	"WORD_CLUSTERS",
	"BACKGROUND_WORDS",
	"GRACE_WEIGHT",
	"Compose_Oath",
	"Draw_Oath",
	"Oath_Entry",
	)
