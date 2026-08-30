"""
Cleric prayers — short faith-lines for Domain voice.

The Guild's theme is **faith**: not necessarily a named god, but what the
Character puts their trust in.  A Domain is a take on that faith.  A prayer is
one sentence that names the take.

Assembly
	1. start from ``DEFAULT_PRAYERS`` (every Cleric);
	2. add ``DOMAIN_PRAYERS`` for the Domain they carry;
	3. add ``SPECIES_PRAYERS`` / ``SPECIES_DOMAIN_PRAYERS`` for their people;
	4. add ``CULTURE_PRAYERS`` reached through ``cultures_of`` (same network as
	   gear titles);
	5. ``Pick`` one line from the assembled ledger.

Rendering (caller's job, usually a Domain ``extends``):

	"{prayer}, that's the wisdom of the {Domain} Domain."
"""

from __future__ import annotations


# ---------------------------------------------------------------------------
# Ledgers
# ---------------------------------------------------------------------------


DEFAULT_PRAYERS = (
	"Something answers when you call. You may not understand it, but you can trust it.",
	"Faith is a door you keep opening, even when you don't know what's on the other side.",
	"Faith is a window you keep opening. Even dark clouds can let the light in.",
	"Heavens do not shout. They shine.",
	"A vow is mightier than a bow. It weights less, and carries further.",
	"You are the miracle.",
	"You can be the miracle. Just try.",
	"If you can’t be a good example, then you’ll just have to serve as a horrible warning.",
	)


DOMAIN_PRAYERS = {
	"Life": (
		"Life finds a way.",
		""
		"While I breathe, I hope.",
		"Sufficient unto the day.",
		"What is bent may still drink the rain.",
		),
	"Light": (
		"A candle loses nothing by lighting another.",
		"Even a little is enough to walk by.",
		"The dark is patient. So is the dawn.",
		"What you warm, you keep.",
		"Looking for the light around us, we find it on our own.",
		"In a world of darkness, we find our own light.",
		"In a cold world, we set the fires.",
		"The night hides a world, but reveals a universe.",
		),
	"Trickery": (
		"By indirections, find the way.",
		"Not every closed door is locked.",
		"A smile can be a key.",
		"The watched road is the emptiest.",
		"Normal is an illusion. What is normal for the spider is chaos for the fly.",
		),
	"War": (
		"If you would have peace, keep watch.",
		"The drawn blade has already chosen.",
		"No one returns the same.",
		"Stand where you said you would.",
		"Never interrupt an enemy making a mistake.",
		"A long dispute means that both parties are wrong.",
		"The person who masters himself through self-control and discipline is ultimately undefeatable.",
		
		),
	"Grave": (
		"From dust we come, to dust we return.",
		"If you can't rest in peace, rest in power.",
		"Two coins for the ferryman. One word for the grave.",
		"Life's pains end in the grave.",
        "Our actions may echo in eternity.",
		"Different in life, all men are equal in death.",
		),
	"Knowledge": (
		"Know thyself.",
		"I know that I know nothing.",
		"Ask, and the asking changes you.",
		"What is written outlives the hand.",
		"Knowledge is a mirror, not a book.",
		"You have to study a lot to know very little.",
		"The wise man knows he knows nothing.",
		"When senses fail us, reason must step in.",
		"The believer is happy; the doubter is wise.",
		"Men and books share their enemies: Fire, water, time, and their own contents.",

		),
	}


SPECIES_PRAYERS = {
	"Human": (
		"Ask the gods, but trust yourself.",
		),
	"Tiefling": (
		"Ash remembers the flame.",
		),
	"Goliath": (
		"The winds are fast, but they do not hurry.",
		"Each snowflake is small, but it is part of the avalanche.",
		),
	"Dwarf": (
		"Metal shapes in the forge. People in the challenges.",
		"A saint is a sinner trying to be better.",
		"Forgetting is hard, but harder is forgiving.",
		),
	"Dragonborn": (
		"Clan. Honor. Duty.",
		"Your word is your bond.",
		),
	"Elf": (
		"Dreams are made to be lived.",
		"May the dream guide your way.",
		),
	"Aasimar": (
		"Greatness is a gift. Greatness is a burden.",
		),
	"Halfling": (
		"Rush not. Small feet, steady pace.",
		"One can simply walk into the world.",
		""
		),
	"Gnome": (
		"Wonder is a practice.",
		),
	"Orc": (
		"If it cannot bleed, it cannot bind.",
		),
	}


# Species × Domain — a hint of the people in the Domain's mouth, not a lecture.
SPECIES_DOMAIN_PRAYERS = {
	(
		"Tiefling",
		"Grave",
		): (
		"I show the door. I do not push.",
		"For the last two coins, I will wait.",
		),
	(
		"Tiefling",
		"Life",
		): (
		"Even from the pit, a pulse.",
		),
	(
		"Tiefling",
		"War",
		): (
		"If wrath is mine, let it stand guard.",
		),
	(
		"Goliath",
		"War",
		): (
		"Stand tall enough that others can find you.",
		),
	(
		"Goliath",
		"Light",
		): (
		"First light on the peak. Then the valley.",
		),
	(
		"Dwarf",
		"Life",
		): (
		"Gold is cold until it buys breath.",
		),
	(
		"Dwarf",
		"Knowledge",
		): (
		"Stamp it in. Soft words wash away.",
		),
	(
		"Dragonborn",
		"War",
		): (
		"The name is the banner. Keep the meter.",
		),
	(
		"Dragonborn",
		"Light",
		): (
		"Fire gathers as well as it spends.",
		),
	(
		"Aasimar",
		"Light",
		): (
		"I did not invent it. I only refuse to hide it.",
		),
	(	"Elf", "Light",
		): (
		"Of a small spark a great fire.", # Celtic proverb 
		),

	(
		"Halfling",
		"Life",
		): (
		"Life is precious.",
		"Life is a journey..",
		),

	}


# Culture keys from ``cultures_of`` — one key, one culture. Never fuse.
# Sayings that could be overheard; the culture is felt, not announced.
CULTURE_PRAYERS = {
	"greece": (
		"Know the measure.",
		"Fate cuts. Answer anyway.",
		),
	"rome": (
		"Many mouths, one law.",
		),
	"japan": (
		"Purity is practice.",
		),
	"aztec": (
		"The sun is hungry. So are we.",
		),
	"china": (
		"Right relation, not loud harmony.",
		),
	"korea": (
		"Keep your own rite intact.",
		),
	"iberia": (
		"Gold calls. Answer slower.",
		),
	"andalus": (
		"Garden and blade, one courtyard.",
		),
	"norse": (
		"Hold one root. Climb.",
		),
	"rus": (
		"Winter keeps the honest lessons.",
		),
	"mongol": (
		"The horizon is a road.",
		),
	"celt": (
		"Mist hides. It does not lie.",
		),
	"persia": (
		"Light and shadow were twins first.",
		),
	"levante": (
		"Old roads still take new feet.",
		),
	"africa": (
		"The first hearth still warms.",
		),
	"egypt": (
		"What is weighed endures.",
		),
	"maghreb": (
		"Desert and sea teach the same.",
		),
	"carthage": (
		"Break the treaty, meet the war.",
		),
	"italy": (
		"Beauty is a discipline.",
		),
	"germany": (
		"The hands keep the vow.",
		),
	"switzerland": (
		"Hold the pass. Hold both.",
		),
	"india": (
		"Many names is not confusion.",
		),
	"oceania": (
		"Speak carefully on deep water.",
		),
	"ninja": (
		"Unseen is not unsworn.",
		),
	# Fiction registers — separate keys, not merges of the above.
	"wyrm_myth": (
		"Walk the ridge. Do not name the coil.",
		),
	"grimdark": (
		"Hope costs. Pay it.",
		"Answer to another name.",
		),
	"arthuriana": (
		"No one sits alone in power.",
		),
	"fairytale_fae": (
		"Keep your name close.",
		),
	}




# ---------------------------------------------------------------------------
# Resolution
# ---------------------------------------------------------------------------


def _domain_of(
		character,
		domain: str | None,
		) -> str | None:
	if domain:
		return domain

	for attr in (
			"specialization",
			"subclass",
			"domain",
			"path",
			):
		value = getattr(
			character,
			attr,
			None,
			)
		if isinstance(
				value,
				str,
				) and value:
			# "Life Domain" → "Life"
			return value.removesuffix(
				" Domain"
				)

	return None


# Legacy race labels sometimes surface where Species should.
_RACE_TO_SPECIES = {
	"Fiend": "Tiefling",
	"Giant": "Goliath",
	"Dragon": "Dragonborn",
	}


def _species_of(
		character,
		) -> str | None:
	species = getattr(
		character,
		"species",
		None,
		)
	if isinstance(
			species,
			str,
			) and species:
		return species

	race = getattr(
		character,
		"race",
		None,
		)
	if isinstance(
			race,
			str,
			) and race:
		return _RACE_TO_SPECIES.get(
			race,
			race,
			)

	return None


def _cultures_of(
		character,
		) -> tuple[str, ...]:
	try:
		from AtlasInventarium.Map_of_Gear_Titles import (
				cultures_of,
				)
	except Exception:
		return ()

	try:
		found = cultures_of(
			character
			)
	except Exception:
		return ()

	if not found:
		return ()

	return tuple(
		found
		)


def prayer_ledger(
		character,
		domain: str | None = None,
		) -> tuple[str, ...]:
	"""
	Assemble the prayer pool for this Character.

	Order is stable; duplicates are dropped while preserving first sighting.
	"""
	resolved_domain = _domain_of(
		character,
		domain,
		)
	species = _species_of(
		character
		)

	pool: list[str] = []
	seen: set[str] = set()

	def _extend(
			lines,
			):
		for line in lines:
			if line in seen:
				continue
			seen.add(
				line
				)
			pool.append(
				line
				)

	_extend(
		DEFAULT_PRAYERS
		)

	if resolved_domain in DOMAIN_PRAYERS:
		_extend(
			DOMAIN_PRAYERS[
				resolved_domain
				]
			)

	if species in SPECIES_PRAYERS:
		_extend(
			SPECIES_PRAYERS[
				species
				]
			)

	if species and resolved_domain:
		_extend(
			SPECIES_DOMAIN_PRAYERS.get(
				(
					species,
					resolved_domain,
					),
				(),
				)
			)

	for culture in _cultures_of(
			character
			):
		_extend(
			CULTURE_PRAYERS.get(
				culture,
				(),
				)
			)

	return tuple(
		pool
		)


def pick_prayer(
		character,
		domain: str | None = None,
		) -> str:
	"""Draw one prayer from the assembled ledger (seeded, deterministic)."""
	ledger = prayer_ledger(
		character,
		domain=domain,
		)

	if not ledger:
		return DEFAULT_PRAYERS[
			0
			]

	dice = character.Dice_Bag(
		"cleric.prayer",
		version="1",
		namespace="GenLegendClass",
		)

	return character.Pick(
		ledger,
		dice=dice,
		)


def domain_wisdom(
		character,
		domain: str | None = None,
		) -> str:
	"""
	The closing line for a Domain description.

	"{prayer}, that's the wisdom of the {Domain} Domain."
	"""
	resolved = _domain_of(
		character,
		domain,
		) or "Cleric"

	prayer = pick_prayer(
		character,
		domain=resolved,
		)

	return (
		f"{prayer}, "
		f"that's the wisdom of the {resolved} Domain."
		)


__all__ = (
	"DEFAULT_PRAYERS",
	"DOMAIN_PRAYERS",
	"SPECIES_PRAYERS",
	"SPECIES_DOMAIN_PRAYERS",
	"CULTURE_PRAYERS",
	"prayer_ledger",
	"pick_prayer",
	"domain_wisdom",
	)
