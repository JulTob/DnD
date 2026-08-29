from ..Grimoire_of_Health import roll_health
from ..Codex_of_Progression import Progression

from AtlasLusoris.Grimoire_of_Features import (
	Feature,
	ApplyRandomFeats,
	ApplyEpicBoon,
	)
from AtlasActorLudi.Map_of_Scores import Modifier

import app.random as random


# Each wizard tradition is a hunt for True Names of a different kind.
# To know the name is to understand the thing, and to understand it
# is to stand in relation to it — a door, never the whole of the Way.

TRADITION_ALIASES = {
	"Evoker": "Evoker",
	"Evocation": "Evoker",
	"Illusionist": "Illusionist",
	"Illusion": "Illusionist",
	"Necromancer": "Necromancer",
	"Necromancy": "Necromancer",
	"Diviner": "Diviner",
	"Divination": "Diviner",
	"Abjurer": "Abjurer",
	"Abjuration": "Abjurer",
	"Bladesinger": "Bladesinger",
	"Bladesinging": "Bladesinger",
	}

TRADITIONS = {
	"Evoker": {
		"title": "Namer of Storms",
		"school": "Evocation",
		"sought_names": [
			"Fire", "Lightning", "Thunder", "the Wind", "the Sun",
			"Wildfire", "the First Spark", "the Forge-Heart",
			"the Breaking Wave", "the Shout that Splits Stone",
			"the Summer Heat", "the Unmaking Flame", "the Open Sky",
			],
		},
	"Illusionist": {
		"title": "Namer of Seeming",
		"school": "Illusion",
		"sought_names": [
			"Shadow", "Mirror", "Fog", "Dream", "the Face", "Memory",
			"the Veil", "Moonlight-on-Water", "the Echo", "the False Dawn",
			"the Mask", "the Name that Is Not",
			],
		},
	"Necromancer": {
		"title": "Namer of Silence",
		"school": "Necromancy",
		"sought_names": [
			"Dust", "the Last Breath", "Bone", "the Grave", "the Quiet",
			"the Hollow Name", "the River of Ending", "Ash",
			"the Unspoken Farewell", "the Cold that Remains",
			"the Name that Outlives the Body",
			],
		},
	"Diviner": {
		"title": "Namer of the Unseen",
		"school": "Divination",
		"sought_names": [
			"Fate", "Tomorrow", "the Hidden Thread", "the Unspoken",
			"the Pattern", "the Forking Path", "the Eye Behind Sleep",
			"the Name Before It Is Spoken", "the Still Water that Shows",
			"the Ten Thousand Things",
			],
		},
	"Abjurer": {
		"title": "Namer of Binding",
		"school": "Abjuration",
		"sought_names": [
			"Threshold", "the Closed Door",
			"the Circle", "Iron", "the Ward", "the Name that Holds",
			"the Center", "the Unbroken Line", "the Gate",
			"the Name of No",
			],
		},
	"Bladesinger": {
		"title": "Namer of the Road",
		"school": None,
		"sought_names": [
			"the Road", "the Step", "the Blade", "the Song",
			"the Turning", "the Open Mile", "Wind-in-Grass",
			"the Name You Learn by Walking",
			],
		},
	}

# Spells whose True Names sit inside each tradition (by spell level).
# Used to actually write savant names into the generated spellbook.
SAVANT_NAMES = {
	"Evoker": {
		1: ["Magic Missile", "Thunderwave", "Burning Hands", "Chromatic Orb", "Witch Bolt"],
		2: ["Scorching Ray", "Shatter", "Gust of Wind", "Flaming Sphere"],
		3: ["Fireball", "Lightning Bolt", "Tiny Hut"],
		4: ["Ice Storm", "Wall of Fire", "Fire Shield", "Vitriolic Sphere"],
		5: ["Cone of Cold", "Bigby's Hand", "Wall of Force"],
		6: ["Chain Lightning", "Sunbeam", "Otiluke's Freezing Sphere"],
		7: ["Delayed Blast Fireball", "Crown of Stars", "Whirlwind"],
		8: ["Incendiary Cloud", "Sunburst"],
		9: ["Meteor Swarm"],
		},
	"Illusionist": {
		1: ["Silent Image", "Disguise Self", "Color Spray", "Illusory Script"],
		2: ["Invisibility", "Mirror Image", "Phantasmal Force", "Blur", "Magic Mouth"],
		3: ["Major Image", "Hypnotic Pattern", "Fear", "Phantom Steed"],
		4: ["Greater Invisibility", "Phantasmal Killer", "Hallucinatory Terrain"],
		5: ["Mislead", "Seeming", "Dream"],
		6: ["Programmed Illusion", "Mental Prison"],
		7: ["Simulacrum", "Project Image", "Mirage Arcane"],
		8: ["Illusory Dragon"],
		9: ["Weird"],
		},
	"Necromancer": {
		1: ["False Life", "Ray of Sickness", "Cause Fear"],
		2: ["Blindness/Deafness", "Gentle Repose", "Ray of Enfeeblement"],
		3: ["Animate Dead", "Vampiric Touch", "Bestow Curse", "Speak with Dead", "Feign Death", "Summon Undead"],
		4: ["Blight", "Shadow of Moil"],
		5: ["Danse Macabre", "Enervation", "Negative Energy Flood"],
		6: ["Circle of Death", "Create Undead", "Eyebite", "Magic Jar"],
		7: ["Finger of Death"],
		8: ["Clone", "Abi-Dalzim's Horrid Wilting"],
		9: ["Power Word Kill", "Astral Projection"],
		},
	"Diviner": {
		1: ["Detect Magic", "Identify", "Comprehend Languages"],
		2: ["Detect Thoughts", "See Invisibility", "Augury", "Locate Object", "Mind Spike"],
		3: ["Clairvoyance", "Tongues", "Nondetection"],
		4: ["Arcane Eye", "Divination", "Locate Creature"],
		5: ["Scrying", "Legend Lore", "Rary's Telepathic Bond", "Contact Other Plane"],
		6: ["True Seeing"],
		7: ["Etherealness"],
		8: ["Telepathy"],
		9: ["Foresight"],
		},
	"Abjurer": {
		1: ["Mage Armor", "Shield", "Protection from Evil and Good", "Alarm"],
		2: ["Arcane Lock", "Mind Spike"],
		3: ["Counterspell", "Dispel Magic", "Magic Circle", "Protection from Energy", "Remove Curse", "Glyph of Warding", "Nondetection"],
		4: ["Banishment", "Stoneskin", "Private Sanctum"],
		5: ["Circle of Power", "Wall of Force"],
		6: ["Globe of Invulnerability", "Guards and Wards"],
		7: ["Symbol", "Forcecage"],
		8: ["Antimagic Field", "Mind Blank"],
		9: ["Imprisonment", "Prismatic Wall"],
		},
	}

SCHOLAR_SKILLS = [
	"Arcana", "History", "Investigation", "Medicine", "Nature", "Religion",
	]

BOOK_BINDINGS = [
	"a gilt-edged tome",
	"vellum bound with twine",
	"covers of pale bone",
	"boards of river-stone",
	]

BOOK_MARKS = [
	"A pressed leaf marks a page you have not copied yet.",
	"The spine is worn from a pack, not a lectern.",
	"A stranger's notes fill the margin, then stop mid-sentence.",
	"Rain wrinkled the first gathering of pages.",
	"A ribbon the color of old rust keeps your place.",
	"You mended the clasp with wire from a camp kettle.",
	]

BLADESINGER_SKILLS = [
	"Acrobatics", "Performance", "Athletics", "Stealth",
	]


def skill_training_level(character, name):
	skills = getattr(character, "skills", None)
	if skills is None:
		return 0
	attr = str(name).replace(" ", "_")
	skill = getattr(skills, attr, None)
	try:
		return int(getattr(skill, "proficiency_level", 0) or 0)
	except (TypeError, ValueError):
		return 0


def pick_unlearned_skill(character, options, need_level=1):
	"""Pick a skill the character does not already have at this training level."""
	fresh = [
		name for name in options
		if skill_training_level(character, name) < need_level
		]
	pool = fresh or list(options)
	return random.choice(pool) if pool else None


def resolve_tradition(subclass):
	if not subclass:
		return "Evoker"
	return TRADITION_ALIASES.get(str(subclass).strip(), "Evoker")


def describe_wizard_book(character):
	"""Pick one lived-in book. A seed, not a sentence the player must keep."""
	existing = getattr(character, "wizard_book", None)
	if existing:
		return existing
	from AtlasLusoris.Compass_of_Learned_Spells import caster_rng
	rng = caster_rng(character, 0xB00) if character is not None else random
	binding = rng.choice(BOOK_BINDINGS)
	mark = rng.choice(BOOK_MARKS)
	book = {
		"binding": binding,
		"mark": mark,
		"line": f"{binding}. {mark}",
		}
	if character is not None:
		character.wizard_book = book
	return book


def wizard_feature(name, text, level=1):
	"""Player-facing class feature. Description must be the body text."""
	return Feature(name, text.strip(), source="Class: Wizard", level=level)


def intelligence_modifier(character):
	score = getattr(character.AS, "INT", 10)
	return Modifier(score)


def wizard_spell_index():
	"""Map stripped spell names to Lodge objects, without requiring the full caster tables."""
	index = {}
	try:
		import AtlasMagia.Lodge_of_Spells as lodge
		for value in vars(lodge).values():
			name = getattr(value, "name", None)
			if not name:
				continue
			index[str(name).strip()] = value
	except Exception:
		pass
	try:
		from AtlasLusoris.Grimoire_of_Spellcasters import SPELL_LISTS
		for spells in SPELL_LISTS.get("Wizard", {}).values():
			for spell in spells:
				index[spell.name.strip()] = spell
	except Exception:
		pass
	return index


def add_spells_to_book(character, spells):
	"""Write extra names into the granted catalog. Does not spend class-known slots."""
	from AtlasLusoris.Compass_of_Learned_Spells import catalog_keys, know_spell, spell_key
	caster = getattr(character, "spellcaster", None)
	if caster is None:
		return []
	have = catalog_keys(caster)
	added = []
	for spell in spells:
		if spell is None:
			continue
		try:
			int(getattr(spell, "level", 0))
		except (TypeError, ValueError):
			continue
		key = spell_key(spell)
		if not key or key in have:
			continue
		know_spell(character, spell, always_prepared=False)
		have.add(key)
		added.append(key)
	return added


def pick_savant_spells(tradition, wizard_level, character=None):
	"""Savant: two school names of level 1–2, plus one per later slot level. Grows; does not reshuffle."""
	from AtlasLusoris.Compass_of_Learned_Spells import catalog_keys, caster_rng
	catalog = SAVANT_NAMES.get(tradition, {})
	traditions = list(TRADITIONS.keys())
	salt = 0x5A1 ^ (traditions.index(tradition) if tradition in traditions else 0)
	rng = caster_rng(character, salt) if character is not None else random
	owned = catalog_keys(getattr(character, "spellcaster", None)) if character is not None else set()
	picks = []
	if wizard_level >= 3:
		starter = [
			name for name in list(catalog.get(1, [])) + list(catalog.get(2, []))
			if name not in owned
			]
		rng.shuffle(starter)
		picks.extend(starter[:2])
	slot_unlocks = [
		(5, 3), (7, 4), (9, 5), (11, 6), (13, 7), (15, 8), (17, 9),
		]
	for req_level, slot_level in slot_unlocks:
		if wizard_level < req_level:
			continue
		options = [
			name for name in catalog.get(slot_level, [])
			if name not in picks and name not in owned
			]
		rng.shuffle(options)
		if options:
			picks.append(options[0])
	index = wizard_spell_index()
	return [index[name] for name in picks if name in index], picks


def find_spells(names):
	index = wizard_spell_index()
	found = []
	for name in names:
		spell = index.get(name)
		if spell is not None:
			found.append(spell)
	return found


class Wizard(Progression):
	HIT_DIE = 6

	def __init__(self, character):
		self.char = character

	def features(self, character=None):
		if character is None:
			character = self.char
		else:
			self.char = character

		if hasattr(character, "set"):
			character.set()

		level = character.Level
		tradition = resolve_tradition(character.Subclass)
		lore = TRADITIONS[tradition]
		sought_name = random.choice(lore["sought_names"])
		int_bonus = intelligence_modifier(character)
		features = []

		if level >= 1:
			features.extend(self._level_one(level, tradition, lore, sought_name))
		if level >= 2:
			roll_health(character)
			features.append(self._scholar(character))
		if level >= 3:
			features.extend(self._tradition_features(
				character, tradition, lore, sought_name, level, int_bonus))
		if level >= 4:
			features.extend(ApplyRandomFeats(character, n=1))
		if level >= 5:
			features.append(wizard_feature("Memorize Spell", f"""
				After a Short Rest you may open the book and trade one prepared
				Wizard spell of level 1 or higher for another spell already
				written there. The new spell must be of a level you can prepare.
				""", 5))
		if level >= 6:
			features.extend(self._tradition_level_six(
				character, tradition, lore, sought_name, level, int_bonus))
		if level >= 8:
			features.extend(ApplyRandomFeats(character, n=1))
		if level >= 10:
			features.extend(self._tradition_level_ten(
				character, tradition, lore, sought_name, level, int_bonus))
		if level >= 12:
			features.extend(ApplyRandomFeats(character, n=1))
		if level >= 14:
			features.extend(self._tradition_level_fourteen(
				character, tradition, lore, sought_name, level, int_bonus))
		if level >= 16:
			features.extend(ApplyRandomFeats(character, n=1))
		if level >= 18:
			features.append(wizard_feature("Spell Mastery", """
				Choose one level 1 spell and one level 2 spell in your book
				that have a casting time of an action. You always have them
				prepared, and you can cast each at its lowest level without
				a spell slot. A higher level still costs a slot.
				<br>When you finish a Long Rest, you may trade one of those
				mastered spells for another eligible spell of the same level
				from the book.
				""", 18))
		if level >= 19:
			features.extend(ApplyEpicBoon(character, n=1))
		if level >= 20:
			features.append(wizard_feature("Signature Spells", """
				Choose two level 3 spells in your book as signature spells.
				You always have them prepared. You can cast each once at
				level 3 without a spell slot, and you regain that use when
				you finish a Short or Long Rest. A higher level still costs
				a slot.
				""", 20))
		return features

	def _level_one(self, level, tradition, lore, sought_name):
		recovery = (level + 1) // 2
		book = describe_wizard_book(self.char)
		return [
			wizard_feature("The Way of Names", f"""
				Wizards are not born with power. They hunt names: they write
				them, they walk toward them, they speak them only when the
				world will answer.
				<br>
				But a map is irrelevant to someone who has never walked the
				road. A map is not a country. So you went out there, a long
				way from any library, walking towards the names you wanted
				to learn. Wonder is what happens to you in the world. The
				book is only how you carry the memory of it along.
				<br>
				You are a <b>{tradition}</b>, a <i>{lore['title']}</i>.
				The name you hunt is <b>{sought_name}</b>.
				If another name is calling, take that one instead — this is
				only a first step.
				""", 1),
			wizard_feature("Ritual Adept", """
				If a spell in your book has the Ritual tag, you can cast it
				as a Ritual even when it is not prepared. You must read from
				the book. Some names will not be rushed.
				""", 1),
			wizard_feature("Spellbook", f"""
				Your apprenticeship ended when you bound a book that only you
				can read — unless someone casts <b>Identify</b> upon it.
				It is a Tiny object, three pounds, a hundred pages.
				<br>
				This one is {book['line']}
				You can change how it looks; this is only how it found you.
				<br>
				It begins with six level 1 Wizard spells. Each Wizard level
				after 1, you add two Wizard spells of a level you can slot.
				""", 1),
			wizard_feature("Expanding the Book", """
				The rest of the book is still out there.
				<br><b>Copying a new name.</b> When you find a level 1+ Wizard
				spell you can prepare, you may transcribe it. Each level of
				the spell takes 2 hours and 50 GP. Afterward you can prepare
				it like any other spell in the book.
				<br><b>Copying your own book.</b> A name you already know
				copies faster: 1 hour and 10 GP per spell level.
				If the book is lost, you may write your currently prepared
				spells into a new one this way. The rest must be found again.
				Wise wizards keep a spare.
				""", 1),
			wizard_feature("Arcane Recovery", f"""
				When you finish a Short Rest, you may study the book and
				recover expended spell slots whose combined level is no more
				than <b>{recovery}</b> (half your Wizard level, rounded up).
				None of those slots can be level 6 or higher. Once you do
				this, you cannot do so again until you finish a Long Rest.
				""", 1),
			]

	def _scholar(self, character):
		skill = pick_unlearned_skill(character, SCHOLAR_SKILLS, need_level=2)
		try:
			if skill:
				character.skills.activate_expertise(1, [skill])
		except Exception:
			pass
		return wizard_feature("Scholar", f"""
			While hunting names you also specialized in another field of
			study. You have Expertise in <b>{skill}</b>.
			You can change which field, if this one is not yours.
			""", 2)

	def _bladesinger_three(self, character, lore, sought_name, int_bonus):
		song_uses = max(1, int_bonus)
		skill = pick_unlearned_skill(character, BLADESINGER_SKILLS, need_level=1)
		try:
			character.skills.Martial_Weapons.set_proficiency()
		except Exception:
			pass
		try:
			if skill:
				character.skills.activate_proficiencies(1, [skill])
		except Exception:
			try:
				getattr(character.skills, skill).set_proficiency()
			except Exception:
				pass
		return [
			wizard_feature("Bladesinger", f"""
				You left the library. The names you wanted were not only on
				the shelf; they were in the way a blade turns, in the length
				of a step, in the song that keeps a body honest while it
				thinks. You learn names with your feet as much as with the
				page.
				<br>
				You are a <b>Bladesinger</b>, a <i>{lore['title']}</i>.
				The name you hunt is <b>{sought_name}</b>.
				""", 3),
			wizard_feature("Training in War and Song", f"""
				You have proficiency with Martial melee weapons that are
				not two-handed or Heavy. You can use a melee weapon as a
				Spellcasting Focus for your Wizard spells.
				You also have proficiency in <b>{skill}</b>
				(change it if another skill is more yours).
				""", 3),
			wizard_feature("Bladesong", f"""
				If you are not wearing armor or a Shield, you can start
				the Bladesong as a Bonus Action. It lasts 1 minute, and
				ends early if you wear armor, use a two-handed weapon,
				become Incapacitated, or choose to end it (no action).
				<br>While it lasts: add your Intelligence modifier to AC;
				gain +10 feet of speed; use Intelligence for melee weapon
				attack and damage rolls; add your Intelligence modifier
				to Constitution saving throws to maintain Concentration.
				<br>You can use this <b>{song_uses}</b> times (Intelligence
				modifier, minimum once). You regain one use when you use
				Arcane Recovery, and all uses when you finish a Long Rest.
				""", 3),
			]

	def _tradition_features(self, character, tradition, lore, sought_name, level, int_bonus):
		if tradition == "Bladesinger":
			return self._bladesinger_three(character, lore, sought_name, int_bonus)
		school = lore["school"]
		added_spells, pick_names = pick_savant_spells(tradition, level, character)
		written = add_spells_to_book(character, added_spells)
		written_line = ", ".join(written or pick_names[:2]) or f"two {school} spells"
		savant = wizard_feature(f"{school} Savant", f"""
			Spells of the {school} school come cheaper to your hand.
			You add the following spells to your book without the usual
			time or gold: <b>{written_line}</b>.
			<br>Whenever you gain a new level of spell slots in this class,
			you may add one Wizard spell of the {school} school to the book
			for free, of a level you can slot.
			""", 3)
		if tradition == "Evoker":
			return [
				wizard_feature("Namer of Storms", f"""
					You hunt names of what moves: flame, thunder, the bright
					edge of force. To name the storm is not to own it — it is
					to stand inside it and remain yourself.
					The name you hunt is <b>{sought_name}</b>.
					""", 3),
				savant,
				wizard_feature("Potent Cantrip", """
					When you cast a damaging cantrip and miss, or the target
					succeeds on its save, the target still takes half the
					cantrip's damage (if any) and suffers no other effect.
					""", 3),
				]
		if tradition == "Illusionist":
			add_spells_to_book(character, find_spells(["Minor Illusion"]))
			from AtlasLusoris.Compass_of_Learned_Spells import grant_spell
			for spell in find_spells(["Minor Illusion"]):
				grant_spell(character, spell)
			return [
				wizard_feature("Namer of Seeming", f"""
					You hunt names of shadow, mirror, and mask — not to lie,
					but to show how thin the veil is between is and seems.
					The name you hunt is <b>{sought_name}</b>.
					""", 3),
				savant,
				wizard_feature("Improved Illusions", """
					You always know <i>Minor Illusion</i>, and you can cast
					it as a Bonus Action. When you do, the illusion may
					include both a sound and an image. You can see through
					your own illusions, and Illusion spells you cast no
					longer require Verbal components. See Spells.
					""", 3),
				]
		if tradition == "Necromancer":
			return [
				wizard_feature("Namer of Silence", f"""
					You hunt last names: dust, the breath leaving, the
					hollow that remains. To name death is not to worship it.
					It is to know where the river goes.
					The name you hunt is <b>{sought_name}</b>.
					""", 3),
				savant,
				wizard_feature("Grim Harvest", """
					Once per turn, when you kill a creature that is not a
					Construct or Undead with a spell of level 1 or higher,
					you regain Hit Points equal to twice the spell's level,
					or three times the level if the spell is Necromancy.
					""", 3),
				]
		if tradition == "Diviner":
			dice_count = 3 if level >= 14 else 2
			portent = [random.randint(1, 20) for _ in range(dice_count)]
			portent_text = " and ".join(f"<b>{roll}</b>" for roll in portent)
			return [
				wizard_feature("Namer of the Unseen", f"""
					You hunt names that have not yet been spoken: fate,
					the hidden thread, tomorrow. You do not command the
					future. You recognize its name when it leans toward you.
					The name you hunt is <b>{sought_name}</b>.
					""", 3),
				savant,
				wizard_feature("Portent", f"""
					When you finish a Long Rest, you roll {dice_count} d20s
					and keep the numbers. You may replace any attack roll,
					saving throw, or ability check made by you or a creature
					you can see with one of those numbers. You choose before
					the roll. Each number is spent when you use it, and any
					unused numbers fade when you finish a Long Rest.
					<br>Today the unseen leans toward: {portent_text}.
					""", 3),
				]
		# Abjurer
		ward_hp = 2 * level + int_bonus
		return [
			wizard_feature("Namer of Binding", f"""
				You hunt names that hold: threshold, circle, iron, the
				center that does not move. Power is not only what you send
				out. It is what you refuse, what you keep.
				The name you hunt is <b>{sought_name}</b>.
				""", 3),
			savant,
			wizard_feature("Arcane Ward", f"""
				When you cast an Abjuration spell with a spell slot, you
				may create a ward around yourself. The ward lasts until
				you finish a Long Rest. It has a Hit Point maximum of
				<b>{ward_hp}</b> (twice your Wizard level plus your
				Intelligence modifier).
				<br>Whenever you take damage, the ward takes it first.
				If the ward drops to 0 Hit Points, you take the rest.
				While it has 0 Hit Points it cannot absorb, but it remains.
				Each time you cast an Abjuration spell with a slot, the
				ward regains Hit Points equal to twice that slot's level.
				You can create the ward only once per Long Rest.
				""", 3),
			]

	def _tradition_level_six(self, character, tradition, lore, sought_name, level, int_bonus):
		if tradition == "Bladesinger":
			return [wizard_feature("Extra Attack", """
				You can attack twice, instead of once, whenever you take
				the Attack action. You may replace one of those attacks
				with a Wizard cantrip that has a casting time of an action.
				""", 6)]
		if tradition == "Evoker":
			return [wizard_feature("Sculpt Spells", f"""
				When you cast an Evocation spell that other creatures you
				can see would suffer, you may choose a number of them equal
				to 1 plus the spell's level. Those creatures automatically
				succeed on their saving throws against the spell, and they
				take no damage if they would normally take half on a success.
				""", 6)]
		if tradition == "Illusionist":
			add_spells_to_book(character, find_spells(["Summon Beast", "Summon Fey"]))
			from AtlasLusoris.Compass_of_Learned_Spells import grant_spell
			for spell in find_spells(["Summon Beast", "Summon Fey"]):
				grant_spell(character, spell)
			return [wizard_feature("Phantasmal Creatures", """
				You always have <i>Summon Beast</i> and <i>Summon Fey</i>
				prepared. Once per Long Rest you can cast one of them
				without a spell slot; the summoned creature is slightly
				translucent. When you cast either spell with a spell slot,
				it does not require Concentration. See Spells.
				""", 6)]
		if tradition == "Necromancer":
			add_spells_to_book(character, find_spells(["Animate Dead"]))
			from AtlasLusoris.Compass_of_Learned_Spells import grant_spell
			for spell in find_spells(["Animate Dead"]):
				grant_spell(character, spell)
			thrall_hp = level
			return [wizard_feature("Undead Thralls", f"""
				You always have <i>Animate Dead</i> prepared. When you cast
				it, you can target one additional corpse or pile of bones.
				Undead you create with a Necromancy spell add your Wizard
				level (<b>+{thrall_hp}</b> Hit Points) to their Hit Point
				maximum, and they add your Proficiency Bonus to the damage
				of their weapon attacks. See Spells.
				""", 6)]
		if tradition == "Diviner":
			return [wizard_feature("Expert Divination", """
				When you cast a Divination spell using a spell slot of
				level 2 or higher, you regain one expended spell slot.
				The regained slot must be of a lower level than the one
				you spent, and it cannot be level 6 or higher.
				""", 6)]
		return [wizard_feature("Projected Ward", """
			When a creature you can see within 30 feet takes damage, you
			can take a Reaction to let your Arcane Ward take that damage
			instead. If the ward drops to 0 Hit Points, the creature takes
			the rest.
			""", 6)]

	def _tradition_level_ten(self, character, tradition, lore, sought_name, level, int_bonus):
		if tradition == "Bladesinger":
			return [wizard_feature("Song of Defense", """
				While your Bladesong is active and you take damage, you can
				take a Reaction to expend a spell slot and reduce that
				damage by an amount equal to five times the slot's level.
				""", 10)]
		if tradition == "Evoker":
			bonus = max(1, int_bonus)
			return [wizard_feature("Empowered Evocation", f"""
				Whenever you cast a Wizard spell from the Evocation school,
				you can add your Intelligence modifier (<b>+{bonus}</b>)
				to one damage roll of that spell.
				""", 10)]
		if tradition == "Illusionist":
			return [wizard_feature("Illusory Self", """
				When a creature hits you with an attack roll, you can take
				a Reaction to interpose a duplicate of yourself. The attack
				misses. Once you do this, you cannot do so again until you
				finish a Short or Long Rest, unless you expend a spell slot
				of level 2 or higher (no action) to restore the use.
				""", 10)]
		if tradition == "Necromancer":
			return [wizard_feature("Inured to Undeath", """
				You have Resistance to Necrotic damage, and your Hit Point
				maximum cannot be reduced.
				""", 10)]
		if tradition == "Diviner":
			uses = max(1, int_bonus)
			return [wizard_feature("The Third Eye", f"""
				As a Bonus Action you may open a third way of seeing, lasting
				10 minutes. Choose one:
				<ul>
				<li><b>Darkvision</b> out to 120 feet.</li>
				<li><b>Greater Comprehension.</b> You can read any language.</li>
				<li><b>See Invisibility.</b> You see Invisible creatures and
				objects, and you can see into the Ethereal Plane, out to
				10 feet.</li>
				</ul>
				You can do this <b>{uses}</b> times (your Intelligence
				modifier, minimum once), and you regain all uses when you
				finish a Long Rest.
				""", 10)]
		add_spells_to_book(character, find_spells(["Counterspell", "Dispel Magic"]))
		from AtlasLusoris.Compass_of_Learned_Spells import grant_spell
		for spell in find_spells(["Counterspell", "Dispel Magic"]):
			grant_spell(character, spell)
		return [wizard_feature("Spell Breaker", """
			You always have <i>Counterspell</i> and <i>Dispel Magic</i>
			prepared. You can cast Dispel Magic as a Bonus Action, and you
			add your Proficiency Bonus to its ability check.
			When you cast either spell this way, your Arcane Ward regains
			Hit Points equal to the spell's level. See Spells.
			""", 10)]

	def _tradition_level_fourteen(self, character, tradition, lore, sought_name, level, int_bonus):
		if tradition == "Bladesinger":
			return [wizard_feature("Song of Victory", """
				When you cast a spell with a casting time of an action,
				you can make a melee weapon attack as a Bonus Action.
				""", 14)]
		if tradition == "Evoker":
			return [wizard_feature("Overchannel", f"""
				When you cast a Wizard spell with a spell slot of levels
				1–5 that deals damage, you can deal maximum damage with
				that spell on the turn you cast it.
				<br>The first time you do so, you suffer no adverse effect.
				If you use this feature again before you finish a Long Rest,
				you take <b>2d12 Necrotic damage</b> per level of the spell
				slot immediately after you cast it. This damage ignores
				Resistance and Immunity. Each further use before a Long Rest
				increases that Necrotic damage by <b>1d12</b> per spell level.
				""", 14)]
		if tradition == "Illusionist":
			return [wizard_feature("Illusory Reality", """
				When you cast an Illusion spell with a spell slot, you can
				choose one inanimate, nonmagical object that is part of the
				illusion and make that object real for 1 minute. The object
				cannot deal damage or otherwise directly harm anyone.
				""", 14)]
		if tradition == "Necromancer":
			return [wizard_feature("Command Undead", """
				As an Action, choose one Undead you can see within 60 feet.
				It must succeed on a Charisma saving throw against your
				spell save DC or obey your commands until you use this
				feature again. Intelligent Undead (Intelligence 8 or higher)
				have Advantage, and if they succeed they are immune to
				your Command Undead for 24 hours. If it is already under
				another creature's control, you steal that control on a
				failure.
				""", 14)]
		if tradition == "Diviner":
			return [wizard_feature("Greater Portent", """
				The unseen now offers three numbers instead of two when
				you finish a Long Rest.
				""", 14)]
		return [wizard_feature("Spell Resistance", """
			You have Advantage on saving throws against spells, and you
			have Resistance to the damage of spells.
			""", 14)]
