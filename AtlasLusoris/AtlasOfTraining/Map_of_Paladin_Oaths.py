"""
The Oath a Paladin actually says.

The Guild text says a principle is held. This is the principle spoken, and it
is the one place on a whole sheet where the Character talks instead of being
talked about. Everything else on the page is the sheet addressing the player.
Six lines in the middle of it are the player's own mouth, and they are written
to be read aloud at a table.

**The shape is the knight's code**: six short declaratives, each giving one
part of the person a duty. The form is old and public rather than private and
confessional, which is why it takes the first person without becoming a diary:
a code is recited, not confided.

**It is assembled, never chosen.** Six slots draw from six pools, each pool
keyed to a different thing the Character already is, exactly the way an
Aasimar's aureola takes its form from one Ideal, its gem from another and its
tell from either. No Paladin is handed a finished oath out of a list, and two
Paladins of the same Oath will share a line or two and never the whole.

	1. THE VOW     the Oath itself, and the only slot that names it
	2. THE HEART   the people they come from
	3. THE BLADE   the Oath again, turned toward what it is for
	4. THE WORD    the life they had before this one
	5. THE REFUSAL the culture keys, the network gear titles already use
	6. THE CLOSE   the Oath a third time, and the line that has to land

Three of six sit on the Oath so that an Oath of Vengeance never sounds like an
Oath of Glory. The other three sit on species, background and culture, so that
two Vengeance Paladins from different peoples and different lives do not
recite the same thing.

**Nothing here hands the Character a past.** A line may name what they were,
because the sheet already says that out loud, and never what happened to them.
The day they swore, the wrong they saw and the face they remember belong to
the player, and a generator that supplied those would be writing somebody
else's character.
"""

from __future__ import annotations


DEVOTION = "Devotion"
ANCIENTS = "Ancients"
GLORY = "Glory"
VENGEANCE = "Vengeance"


# ---------------------------------------------------------------------------
# 1. The vow. Keyed to the Oath, and the only slot that says what was sworn.
# ---------------------------------------------------------------------------


VOWS = {
	DEVOTION: (
		"I am sworn to the thing that does not bend.",
		"I am sworn to do it right when doing it wrong would be easier.",
		"I am sworn to a way of standing, and I have stood that way since.",
		),
	ANCIENTS: (
		"I am sworn to the green that comes back.",
		"I am sworn to what was here first and will be here after.",
		"I am sworn to the light, and to the hour before it returns.",
		),
	GLORY: (
		"I am sworn to be worth the telling.",
		"I am sworn to the deed that makes the next one braver.",
		"I am sworn to leave the story better than I found it.",
		),
	VENGEANCE: (
		"I am sworn against.",
		"I am sworn to the ledger, and the ledger closes.",
		"I am sworn to the answer, and I am the answer.",
		),
	}


# ---------------------------------------------------------------------------
# 2. The heart. Keyed to the people, never to what happened to the person.
# ---------------------------------------------------------------------------


HEARTS = {
	"Human": (
		"My heart is short-lived and it is not spending that on nothing.",
		"My heart was born late to a long argument and it has picked a side.",
		),
	"Dwarf": (
		"My heart was made in a forge and it keeps its shape under heat.",
		"My heart is worked metal, and worked metal remembers the hammer.",
		),
	"Elf": (
		"My heart has time, and it is spending the time on this.",
		"My heart is older than the grievance and it has not forgotten it.",
		),
	"Orc": (
		"My heart is open country and it was fenced without being asked.",
		"My heart rides, and it does not ride away from things.",
		),
	"Goliath": (
		"My heart came down off a mountain that fell, and remembers the height.",
		"My heart keeps what was made, because keeping it is the duty.",
		),
	"Halfling": (
		"My heart knows a place where nobody ever needed guarding.",
		"My heart is small and it is standing here anyway.",
		),
	"Dragonborn": (
		"My heart was raised in a hall where a word given was a deed done.",
		"My heart knows which hand takes the cup, and it knows why.",
		),
	"Tiefling": (
		"My heart has been read wrong my whole life and it is still mine.",
		"My heart was named a warning. I have made it a promise.",
		),
	"Gnome": (
		"My heart keeps its ways in small things and the small things hold.",
		"My heart was handed down, and I am not the one who drops it.",
		),
	"Aasimar": (
		"My heart carries a spark it did not ask for and has chosen anyway.",
		"My heart cannot compromise, and has stopped apologising for that.",
		),
	}

DEFAULT_HEARTS = (
	"My heart is the part of me that did not get a vote.",
	"My heart was not consulted and has never once complained.",
	)


# ---------------------------------------------------------------------------
# 3. The blade. The Oath again, turned toward what the hand is for.
# ---------------------------------------------------------------------------


BLADES = {
	DEVOTION: (
		"My blade is bright, so that nothing I do is done in the dark.",
		"My blade is honest, and it has never once been quick about it.",
		"My blade does what I said it would do, in front of whoever is looking.",
		),
	ANCIENTS: (
		"My blade is for the winter, and the winter is patient.",
		"My blade stands between the small green thing and the frost.",
		"My blade is a young thing serving a very old one.",
		),
	GLORY: (
		"My blade is for the moment the song will need.",
		"My blade goes first, because someone has to and it may as well be seen.",
		"My blade is the part of this that people will describe afterwards.",
		),
	VENGEANCE: (
		"My blade carries one name at a time, and it finishes.",
		"My blade is not angry. Anger runs out.",
		"My blade is the shortest distance between a wrong and its end.",
		),
	}


# ---------------------------------------------------------------------------
# 4. The word. Keyed to the life before this one.
#
# Backgrounds cluster rather than each taking a line: forty-six lines would be
# forty-six chances to write a weak one, and the clusters are what the oath
# actually cares about, which is what a person's word was worth before they
# gave this one.
# ---------------------------------------------------------------------------


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

WORDS = {
	"sworn": (
		"My word was spoken once before, to a smaller thing, and I kept that too.",
		"My word has been given to men who did not deserve it. This one is mine.",
		),
	"held": (
		"My word was the only thing about me that nobody else owned.",
		"My word was worth nothing to the people above me, and everything to me.",
		),
	"outside": (
		"My word was cheap for years. It is not cheap now.",
		"My word is the one thing I never sold, and I sold a great deal.",
		),
	"learned": (
		"My word is checked before it is given, and then it is not checked again.",
		"My word is the one claim I have never needed a source for.",
		),
	"wandering": (
		"My word travels ahead of me and arrives before I do.",
		"My word is all a stranger has, so I made sure mine was good.",
		),
	"marked": (
		"My word is mine, whatever else about me was decided elsewhere.",
		"My word is the part of my fate I got to write.",
		),
	"alone": (
		"My word was given where nobody could hear it, which is when it counts.",
		"My word is kept the same whether there is anyone there or not.",
		),
	"watched": (
		"My word is given in front of people, and that is the point of it.",
		"My word has an audience now, and the audience is not why I keep it.",
		),
	"lost": (
		"My word is what I have left, so I have made it enough.",
		"My word outlived everything else I had. It will outlive me too.",
		),
	}

DEFAULT_WORDS = (
	"My word is the whole of my estate.",
	"My word costs me something every time, which is how I know it is real.",
	)


# ---------------------------------------------------------------------------
# 5. The refusal. Keyed to the culture network gear titles and Cleric prayers
# already use, so a Paladin's oath sounds like the rest of their sheet.
# ---------------------------------------------------------------------------


REFUSALS = {
	"iberia": (
		"I will not serve a bad lord well and call it honour.",
		),
	"andalus": (
		"I will not burn the library to win the argument.",
		),
	"rome": (
		"I will not obey an order that the road was not built for.",
		),
	"sparta": (
		"I will not count them before I decide.",
		),
	"homeric": (
		"I will not choose the long life. I have been offered it.",
		),
	"athens": (
		"I will not be argued out of it by a better speaker.",
		),
	"vatican": (
		"I will not mistake the vestment for the thing it stands for.",
		),
	"sangha": (
		"I will not pretend the wanting has stopped. I will act anyway.",
		),
	"carthage": (
		"I will not forget it. I was young and I have not forgotten it.",
		),
	"norse": (
		"I will not be told the ending and behave differently.",
		),
	"celt": (
		"I will not break it for a king, and I have been asked by one.",
		),
	"mongol": (
		"I will not stop at the edge of the map.",
		),
	"japan": (
		"I will not outlive the keeping of it by very long.",
		),
	"china": (
		"I will not do to them what I would not have done to mine.",
		),
	"egypt": (
		"I will not be weighed and found wanting.",
		),
	"persia": (
		"I will not be consoled by this too shall pass.",
		),
	# Every Paladin carries this key from the Guild, so it needs depth the
	# species keys do not: an Orc has no other entry in the culture map, and
	# with one line here it answered for three Orc Paladins in four. The
	# register is the aftermath stratum, the garrison that outlived its
	# reason, which is the Guild's own legend register.
	"arthuriana": (
		"I will not be the one who put it down.",
		"I will not ask first whether the kingdom deserves it.",
		"I will not stop keeping it because the keeping has gone out of fashion.",
		"I will not hand it to somebody better. Nobody better is coming.",
		"I will not wait for the order. The order is not coming either.",
		),
	"crusader": (
		"I will not need the banner. The banner needs me.",
		),
	"grimdark": (
		"I will not become the thing. I have watched it happen to better.",
		),
	}

DEFAULT_REFUSALS = (
	"I will not be talked out of it by anyone who was not standing there.",
	"I will not be told what I am by people who have not tried it.",
	"I will not make my peace with it, and I have been given every chance.",
	)


# A refusal the Character's own cultures unlock beats a default by this much.
# Same number and the same reasoning as AFFINITY_WEIGHT in Map_of_Familiars:
# high enough that the keyed line is what a table usually hears, low enough
# that the defaults are not dead entries.
CULTURE_AFFINITY_WEIGHT = 8

# The Guild grants this key to every Paladin, so it is not a distinguishing
# mark and must not be weighted like one. Measured: with arthuriana weighted
# as a species key, its five lines answered for most Paladins of every people
# and the Dwarf stopped refusing like a Dwarf. It keeps a weight above the
# defaults, because it is still the Guild's own register, and below the
# species keys, because those are the ones that say who this Paladin is.
GUILD_KEY = "arthuriana"
GUILD_AFFINITY_WEIGHT = 3


# ---------------------------------------------------------------------------
# 6. The close. The line that has to land, and the Oath's third and last slot.
# ---------------------------------------------------------------------------


CLOSES = {
	DEVOTION: (
		"And if I am the last one keeping it, it is still kept.",
		"There is no finishing this. There is only tomorrow, and I will be there.",
		"Ask me again in thirty years. The answer is already written.",
		),
	ANCIENTS: (
		"The light is older than the dark, and it is coming back.",
		"Let it go out everywhere else. It will not go out in me.",
		"I am a short season in a very long spring, and I am this season.",
		),
	GLORY: (
		"Say it after me, and say it right.",
		"They will tell it wrong. Tell it wrong in my favour.",
		"I would rather be the story they need than the man I was.",
		),
	VENGEANCE: (
		"Let them run. It changes nothing.",
		"It ends. I have decided that it ends.",
		"I am not owed this. They are.",
		),
	}


# ---------------------------------------------------------------------------
# The frame: what the oath was sworn to, and how it was said
#
# A circumstance describes the SAYING and never the reason. "Whispered to
# yourself" is a fact about the oath; "with your hand on a dying friend" would
# be a fact about the Character's life, and that is the player's to write. The
# line between them is the same one the Guild text holds: the sheet may say
# what this person is, never what happened to them.
# ---------------------------------------------------------------------------


OATH_OBJECTS = {
	DEVOTION: "Devotion, which has no enemy and so can never be finished",
	ANCIENTS: "the Ancients, who were here before anything had a word for them",
	GLORY: "Glory, which is not winning and never was",
	VENGEANCE: "Vengeance, which is a debt and not a mood",
	}


CIRCUMSTANCES = {
	"sworn": (
		"You swore it a second time, over one you had already given.",
		"You said it in the form the service uses, and meant it another way.",
		),
	"held": (
		"You said it where nobody important was listening.",
		"You said it at the end of a long day, which is when people mean things.",
		),
	"outside": (
		"You said it in a room you had no business being in.",
		"You said it to the one witness who would never repeat it.",
		),
	"learned": (
		"You wrote it out first, said it once, and then burned the paper.",
		"You said it in a language you had chosen on purpose.",
		),
	"wandering": (
		"You said it on a road, in a country that was not yours.",
		"You said it at a border, facing the way you were going.",
		),
	"marked": (
		"You said it back to the thing that had already claimed you.",
		"You said it as an answer, and it was the first word you chose yourself.",
		),
	"alone": (
		"You said it to the weather.",
		"You said it aloud with nobody in earshot, which is the hardest way.",
		),
	"watched": (
		"You said it in front of a crowd who thought it was part of the act.",
		"You said it to an audience, and not for them.",
		),
	"lost": (
		"You said it into the quiet afterwards.",
		"You said it once and have not needed to say it again.",
		),
	}

DEFAULT_CIRCUMSTANCES = (
	"You said it out loud, to the gods, whoever they turned out to be.",
	"You whispered it to yourself, where nobody could possibly hear.",
	"You said it in front of witnesses, every one of them still living.",
	"You said it alone, to nobody at all.",
	"You said it twice, because the first time your voice went.",
	"You said it without meaning to, and then again on purpose.",
	"You said it in the old words, which you had to be taught.",
	"You said it in your own words, because the old ones did not fit.",
	"You said it kneeling, which you have not done since.",
	"You said it quietly, the way a person says a thing already decided.",
	"You have never written it down, and neither has anyone else.",
	"You said it with your eyes open.",
	)


# ---------------------------------------------------------------------------
# Reading the Character
# ---------------------------------------------------------------------------


def _oath_of(
		char,
		) -> str | None:
	"""Which Oath this Paladin swore, by name, or None before it is chosen."""
	for attribute in (
			"specialization",
			"Specialization",
			"subclass",
			"Subclass",
			):
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


def _species_of(
		char,
		) -> str | None:
	"""The people this Paladin comes from, by name."""
	for attribute in (
			"species",
			"Species",
			"race",
			"Race",
			):
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


def _background_of(
		char,
		) -> str | None:
	"""The life this Paladin had before the Oath, by name."""
	for attribute in (
			"background",
			"Background",
			):
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


def _cultures_of(
		char,
		) -> tuple[str, ...]:
	"""
	The culture keys this Character answers to.

	Same network as gear titles and Cleric prayers, so an oath, a sword's
	name and a prayer all come out of one vocabulary. A failure here costs
	the refusal its keyed line and nothing else, so it is swallowed.
	"""
	try:
		from AtlasInventarium.Map_of_Gear_Titles import cultures_of
	except Exception:
		return ()

	try:
		found = cultures_of(
			char
			)
	except Exception:
		return ()

	return tuple(
		found or ()
		)


def _cluster_of_background(
		background: str | None,
		) -> str | None:
	"""Which word-cluster a background belongs to, or None if unlisted."""
	if not background:
		return None

	for cluster, members in WORD_CLUSTERS.items():
		if background in members:
			return cluster

	return None


# ---------------------------------------------------------------------------
# Assembling the six lines
# ---------------------------------------------------------------------------


def _draw(
		char,
		pool,
		purpose: str,
		) -> str | None:
	"""One line from a pool, against a named Dice Bag. Empty pool draws none."""
	options = [
		line
		for line in pool
		if line
		]
	if not options:
		return None

	return char.Pick(
			options,
			dice=char.Dice_Bag(
				purpose,
				version="1",
				namespace="GenLegendLusoris",
				),
			)


def _draw_weighted(
		char,
		weighted,
		purpose: str,
		) -> str | None:
	"""One line from a pool of (line, weight) pairs, against a named Bag."""
	entries = [
		pair
		for pair in weighted
		if pair[0]
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
				version="1",
				namespace="GenLegendLusoris",
				),
			)


def _keyed_pool(
		ledger,
		key: str | None,
		fallback,
		):
	"""The pool for a key, or the fallback when the key has no entry."""
	if key is None:
		return fallback

	return ledger.get(
			key,
			fallback,
			)


def _culture_refusals(
		char,
		) -> tuple[tuple[str, int], ...]:
	"""
	Every refusal open to this Character, each with its weight.

	A line one of their own culture keys unlocks outweighs a default, so a
	Dwarf usually refuses like a Dwarf. Nothing is excluded: the defaults
	stay drawable, because a Paladin who refuses in nobody's accent in
	particular is a person too.

	Keys are read in the order gear titles return them, so the pool is the
	same on every generation of the same Character.
	"""
	weighted: list[tuple[str, int]] = []
	seen: set[str] = set()

	for key in _cultures_of(
			char
			):
		weight = (
			GUILD_AFFINITY_WEIGHT
			if key == GUILD_KEY
			else CULTURE_AFFINITY_WEIGHT
			)
		for line in REFUSALS.get(
				key,
				(),
				):
			if line in seen:
				continue
			seen.add(
				line
				)
			weighted.append(
				(
					line,
					weight,
					)
				)

	for line in DEFAULT_REFUSALS:
		if line in seen:
			continue
		seen.add(
			line
			)
		weighted.append(
			(
				line,
				1,
				)
			)

	return tuple(
		weighted
		)


def Compose_Oath(
		char,
		) -> tuple[str, ...]:
	"""
	The six lines, in order, for this Character.

	Pure assembly: it draws but decides nothing that outlives the call, so
	``Draw_Oath`` owns the settling and this owns the shape.
	"""
	oath = _oath_of(
			char
			)
	cluster = _cluster_of_background(
			_background_of(
				char
				)
			)

	slots = (
		(
			"paladin.oath.vow",
			_keyed_pool(
				VOWS,
				oath,
				VOWS[DEVOTION],
				),
			),
		(
			"paladin.oath.heart",
			_keyed_pool(
				HEARTS,
				_species_of(
					char
					),
				DEFAULT_HEARTS,
				),
			),
		(
			"paladin.oath.blade",
			_keyed_pool(
				BLADES,
				oath,
				BLADES[DEVOTION],
				),
			),
		(
			"paladin.oath.word",
			_keyed_pool(
				WORDS,
				cluster,
				DEFAULT_WORDS,
				),
			),
		(
			"paladin.oath.refusal",
			None,
			),
		(
			"paladin.oath.close",
			_keyed_pool(
				CLOSES,
				oath,
				CLOSES[DEVOTION],
				),
			),
		)

	lines = []
	for purpose, pool in slots:
		if pool is None:
			line = _draw_weighted(
					char,
					_culture_refusals(
						char
						),
					purpose,
					)
		else:
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


def _circumstances_of(
		char,
		) -> tuple[tuple[str, int], ...]:
	"""
	Every way this Paladin might have said it, each with its weight.

	A circumstance the life before the Oath unlocks outweighs a default, so
	a Squire's swearing sounds like a Squire's. The defaults stay drawable:
	most people say a thing in no particular manner at all.
	"""
	cluster = _cluster_of_background(
			_background_of(
				char
				)
			)
	weighted: list[tuple[str, int]] = []
	seen: set[str] = set()

	for line in CIRCUMSTANCES.get(
			cluster,
			(),
			):
		seen.add(
			line
			)
		weighted.append(
			(
				line,
				CULTURE_AFFINITY_WEIGHT,
				)
			)

	for line in DEFAULT_CIRCUMSTANCES:
		if line in seen:
			continue
		seen.add(
			line
			)
		weighted.append(
			(
				line,
				1,
				)
			)

	return tuple(
		weighted
		)


def Draw_Oath(
		char,
		) -> tuple[str, ...]:
	"""
	Settle what this Paladin swore and how they said it, once.

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
	char.paladin_oath_circumstance = _draw_weighted(
			char,
			_circumstances_of(
				char
				),
			"paladin.oath.circumstance",
			)

	return lines


def Oath_Entry(
		char,
		) -> str:
	"""
	The whole oath block: what it was sworn to, how it was said, and the words.

	Set roman rather than italic, one line to a line, so it reads as a code
	carved somewhere rather than as a quotation. Breaks are written and never
	inferred, per Canon/Feature-Text, so every line after the first carries
	its own ``<br>`` from here, in the source.
	"""
	lines = getattr(
			char,
			"paladin_oath_lines",
			None,
			) or ()

	if not lines:
		return ""

	sworn_to = OATH_OBJECTS.get(
			_oath_of(
				char
				),
			)
	circumstance = getattr(
			char,
			"paladin_oath_circumstance",
			None,
			)

	opening = (
		f"You swore an oath to {sworn_to}."
		if sworn_to
		else "You swore an oath."
		)
	frame = [
		opening,
		f"{circumstance} It said:"
		if circumstance
		else "It said:",
		]

	return "<br>".join(
			(
				*frame,
				*lines,
				)
			)


__all__ = (
	"VOWS",
	"HEARTS",
	"BLADES",
	"WORDS",
	"WORD_CLUSTERS",
	"REFUSALS",
	"OATH_OBJECTS",
	"CIRCUMSTANCES",
	"CULTURE_AFFINITY_WEIGHT",
	"GUILD_AFFINITY_WEIGHT",
	"GUILD_KEY",
	"CLOSES",
	"Compose_Oath",
	"Draw_Oath",
	"Oath_Entry",
	)
