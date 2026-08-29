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
			"Threshold", "the Closed Door", "the Uncarved Block",
			"the Circle", "Iron", "the Ward", "the Name that Holds",
			"the Center", "the Unbroken Line", "the Gate",
			"the Name of No",
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


def resolve_tradition(subclass):
	if not subclass:
		return "Evoker"
	return TRADITION_ALIASES.get(str(subclass).strip(), "Evoker")


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
	caster = getattr(character, "spellcaster", None)
	if caster is None or getattr(caster, "spells_known", None) is None:
		return []
	known = {spell.name.strip() for spell in caster.spells_known}
	added = []
	for spell in spells:
		if spell is None:
			continue
		try:
			int(getattr(spell, "level", 0))
		except (TypeError, ValueError):
			continue
		key = spell.name.strip()
		if key not in known:
			caster.spells_known.append(spell)
			known.add(key)
			added.append(key)
	return added


def pick_savant_spells(tradition, wizard_level):
	"""Savant: two school names of level 1–2, plus one per later slot level."""
	catalog = SAVANT_NAMES.get(tradition, {})
	picks = []
	starter = list(catalog.get(1, [])) + list(catalog.get(2, []))
	random.shuffle(starter)
	picks.extend(starter[:2])
	slot_levels = []
	if wizard_level >= 5:
		slot_levels.append(3)
	if wizard_level >= 7:
		slot_levels.append(4)
	if wizard_level >= 9:
		slot_levels.append(5)
	if wizard_level >= 11:
		slot_levels.append(6)
	if wizard_level >= 13:
		slot_levels.append(7)
	if wizard_level >= 15:
		slot_levels.append(8)
	if wizard_level >= 17:
		slot_levels.append(9)
	for slot_level in slot_levels:
		options = [name for name in catalog.get(slot_level, []) if name not in picks]
		if options:
			picks.append(random.choice(options))
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
				Wizard spell of level 1 or higher for another name already written there.
				The new spell must be of a level you can prepare.
				<br><i>A name held in the mouth can be set down. Another can be taken up.
				The book remembers what you do not.</i>
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
				that have a casting time of an action. Those names live on your
				tongue: you always have them prepared, and you can speak each
				at its lowest level without a spell slot. A higher level still
				costs a slot.
				<br>When you finish a Long Rest, you may trade one of those
				mastered names for another eligible spell of the same level
				from the book.
				<br><i>Some names, spoken often enough, stop being study
				and become breath.</i>
				""", 18))
		if level >= 19:
			features.extend(ApplyEpicBoon(character, n=1))
		if level >= 20:
			features.append(wizard_feature("Signature Spells", """
				Choose two level 3 spells in your book as signature names.
				You always have them prepared. You can cast each once at
				level 3 without a spell slot, and you regain that use when
				you finish a Short or Long Rest. A higher level still costs
				a slot.
				<br><i>These are the names that have learned you back.</i>
				""", 20))
		return features

	def _level_one(self, level, tradition, lore, sought_name):
		recovery = (level + 1) // 2
		return [
			wizard_feature("The Way of Names", f"""
				To know a thing's True Name is to understand it, and to
				understand it is to be able to connect with it. Wizards are
				not born with power; they hunt names. They write them, taste
				them, and speak them only when the world will answer.
				<br>The named is never the whole of the Way — the name that
				can be written is not the eternal name. Still, a true name
				is a door.
				<br>You are a <b>{tradition}</b>, a <i>{lore['title']}</i>.
				The name you hunt is <b>{sought_name}</b>.
				""", 1),
			wizard_feature("Ritual Adept", """
				If a spell in your book has the Ritual tag, you can speak it
				as a Ritual even when it is not prepared. You must read from
				the book. Some names will not be rushed; they want the long
				voice, the unhurried breath.
				""", 1),
			wizard_feature("Spellbook", """
				Your apprenticeship ended when you bound a book that only you
				can read — unless someone casts <b>Identify</b> upon it.
				It is a Tiny object, three pounds, a hundred pages. You choose
				its skin: gilt-edge, twine and vellum, bone, or river-stone.
				<br>It begins with six level 1 Wizard spells. Each Wizard level
				after 1, you add two Wizard spells of a level you can slot.
				These are names you research, dream, or wrestle into ink.
				""", 1),
			wizard_feature("Expanding the Book", """
				Adventure yields names other wizards have already caught.
				<b>Copying a new name.</b> When you find a level 1+ Wizard
				spell you can prepare, you may transcribe it. Each level of
				the spell takes 2 hours and 50 GP — ink, rare salts, the
				quiet of copying a name without waking it wrong. Afterward
				you can prepare it like any other name in the book.
				<br><b>Copying your own book.</b> A name you already know
				copies faster: 1 hour and 10 GP per spell level.
				If the book is lost, you may write your currently prepared
				spells into a new one this way. The rest of the book must
				be found again. Wise namers keep a spare.
				""", 1),
			wizard_feature("Arcane Recovery", f"""
				When you finish a Short Rest, you may study the book and
				recover expended spell slots whose combined level is no more
				than <b>{recovery}</b> (half your Wizard level, rounded up).
				None of those slots can be level 6 or higher. Once you do
				this, you cannot do so again until you finish a Long Rest.
				<br><i>The names recede when they are spent. Reading them
				again is how you call them home.</i>
				""", 1),
			]

	def _scholar(self, character):
		skill = random.choice(SCHOLAR_SKILLS)
		try:
			character.skills.activate_expertise(1, [skill])
		except Exception:
			pass
		return wizard_feature("Scholar", f"""
			While hunting names you also specialized in another field of
			study. You have Expertise in <b>{skill}</b>.
			<br><i>A true name sits in a web of lesser names. Scholarship
			is learning which threads to pull.</i>
			""", 2)

	def _tradition_features(self, character, tradition, lore, sought_name, level, int_bonus):
		school = lore["school"]
		added_spells, pick_names = pick_savant_spells(tradition, level)
		written = add_spells_to_book(character, added_spells)
		written_line = ", ".join(written or pick_names[:2]) or f"two {school} spells"
		savant = wizard_feature(f"{school} Savant", f"""
			The True Names of {school.lower()} come cheaper to your hand.
			You add the following names to your book without the usual
			time or gold: <b>{written_line}</b>.
			<br>Whenever you gain a new level of spell slots in this class,
			you may add one Wizard spell of the {school} school to the book
			for free, of a level you can slot.
			""", 3)
		if tradition == "Evoker":
			return [
				wizard_feature("Namer of Storms", f"""
					You hunt the True Names of what moves: flame, thunder,
					the bright edge of force. Yang. To name the storm is
					not to own it — it is to stand inside it and remain
					yourself. The name you hunt is <b>{sought_name}</b>.
					""", 3),
				savant,
				wizard_feature("Potent Cantrip", """
					Even a glancing name leaves a mark. When you cast a
					damaging cantrip and miss, or the target succeeds on
					its save, the target still takes half the cantrip's
					damage (if any) and suffers no other effect.
					""", 3),
				]
		if tradition == "Illusionist":
			add_spells_to_book(character, find_spells(["Minor Illusion"]))
			return [
				wizard_feature("Namer of Seeming", f"""
					The named is not the thing. You hunt names of shadow,
					mirror, and mask — not to lie, but to show how thin
					the veil is between is and seems. Do not force the eye;
					name what it is already willing to believe.
					The name you hunt is <b>{sought_name}</b>.
					""", 3),
				savant,
				wizard_feature("Improved Illusions", """
					You always know <i>Minor Illusion</i>, and you can cast
					it as a Bonus Action. When you do, the illusion may
					include both a sound and an image. You can see through
					your own illusions, and Illusion spells you cast no
					longer require Verbal components.
					<br><i>A name of seeming should not need to be shouted.</i>
					""", 3),
				]
		if tradition == "Necromancer":
			return [
				wizard_feature("Namer of Silence", f"""
					Yin. Return. The valley spirit that does not die.
					You hunt last names: dust, the breath leaving, the
					hollow that remains. To name death is not to worship
					it. It is to know where the river goes, and to speak
					with what the river keeps. The name you hunt is
					<b>{sought_name}</b>.
					""", 3),
				savant,
				wizard_feature("Grim Harvest", """
					Once per turn, when you kill a creature that is not a
					Construct or Undead with a spell of level 1 or higher,
					you regain Hit Points equal to twice the spell's level,
					or three times the level if the spell is Necromancy.
					<br><i>A little of the last name returns to you as breath.</i>
					""", 3),
				]
		if tradition == "Diviner":
			dice_count = 3 if level >= 14 else 2
			portent = [random.randint(1, 20) for _ in range(dice_count)]
			portent_text = " and ".join(f"<b>{roll}</b>" for roll in portent)
			return [
				wizard_feature("Namer of the Unseen", f"""
					You hunt names that have not yet been spoken: fate,
					the hidden thread, tomorrow. The ten thousand things
					announce themselves before they arrive, if you know
					how to listen. You do not command the future. You
					recognize its name when it leans toward you.
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
				The uncarved block. The closed door. You hunt names that
				hold: threshold, circle, iron, the center that does not
				move. Power is not only what you send out. It is what you
				refuse, what you keep, what you name as not-yet-broken.
				The name you hunt is <b>{sought_name}</b>.
				""", 3),
			savant,
			wizard_feature("Arcane Ward", f"""
				When you cast an Abjuration spell with a spell slot, you
				may write the Name of Binding around yourself. The ward
				lasts until you finish a Long Rest. It has a Hit Point
				maximum of <b>{ward_hp}</b> (twice your Wizard level plus
				your Intelligence modifier).
				<br>Whenever you take damage, the ward takes it first.
				If the ward drops to 0 Hit Points, you take the rest.
				While it has 0 Hit Points it cannot absorb, but the
				writing remains. Each time you cast an Abjuration spell
				with a slot, the ward regains Hit Points equal to twice
				that slot's level. You can create the ward only once
				per Long Rest.
				""", 3),
			]

	def _tradition_level_six(self, character, tradition, lore, sought_name, level, int_bonus):
		if tradition == "Evoker":
			return [wizard_feature("Sculpt Spells", f"""
				When you cast an Evocation spell that other creatures you
				can see would suffer, you may name a number of them equal
				to 1 plus the spell's level as <i>not-this-fire</i>. Those
				creatures automatically succeed on their saving throws
				against the spell, and they take no damage if they would
				normally take half on a success.
				<br><i>The Name of {sought_name} does not strike what you
				have named as kin.</i>
				""", 6)]
		if tradition == "Illusionist":
			add_spells_to_book(character, find_spells(["Summon Beast", "Summon Fey"]))
			return [wizard_feature("Phantasmal Creatures", """
				You always have <i>Summon Beast</i> and <i>Summon Fey</i>
				prepared. Once per Long Rest you can cast one of them
				without a spell slot; the summoned creature is slightly
				translucent — a true-seeming, not a true body. When you
				cast either spell with a spell slot, it does not require
				Concentration.
				<br><i>A name of seeming, spoken carefully, will wear a shape
				until the shape remembers it is fog.</i>
				""", 6)]
		if tradition == "Necromancer":
			add_spells_to_book(character, find_spells(["Animate Dead"]))
			thrall_hp = level
			return [wizard_feature("Undead Thralls", f"""
				You always have <i>Animate Dead</i> prepared. When you cast
				it, you can target one additional corpse or pile of bones.
				Undead you create with a Necromancy spell add your Wizard
				level (<b>+{thrall_hp}</b> Hit Points) to their Hit Point
				maximum, and they add your Proficiency Bonus to the damage
				of their weapon attacks.
				<br><i>A last name, spoken kindly or not, will stand up
				if you know how to hold it.</i>
				""", 6)]
		if tradition == "Diviner":
			return [wizard_feature("Expert Divination", """
				When you cast a Divination spell using a spell slot of
				level 2 or higher, you regain one expended spell slot.
				The regained slot must be of a lower level than the one
				you spent, and it cannot be level 6 or higher.
				<br><i>To see a name before it arrives is to spend less
				breath when it does.</i>
				""", 6)]
		return [wizard_feature("Projected Ward", """
			When a creature you can see within 30 feet takes damage, you
			can take a Reaction to let your Arcane Ward drink that damage
			instead. If the ward drops to 0 Hit Points, the creature takes
			the rest.
			<br><i>The Name of Binding can be spoken over someone else.
			The center holds, even at a step's distance.</i>
			""", 6)]

	def _tradition_level_ten(self, character, tradition, lore, sought_name, level, int_bonus):
		if tradition == "Evoker":
			bonus = max(1, int_bonus)
			return [wizard_feature("Empowered Evocation", f"""
				Whenever you cast a Wizard spell from the Evocation school,
				you can add your Intelligence modifier (<b>+{bonus}</b>)
				to one damage roll of that spell.
				<br><i>You no longer borrow {sought_name}. It answers in
				your own voice.</i>
				""", 10)]
		if tradition == "Illusionist":
			return [wizard_feature("Illusory Self", """
				When a creature hits you with an attack roll, you can take
				a Reaction to interpose a duplicate of yourself. The attack
				misses. Once you do this, you cannot do so again until you
				finish a Short or Long Rest, unless you expend a spell slot
				of level 2 or higher (no action) to restore the use.
				<br><i>The name of you, and the you that is named, are not
				always in the same place.</i>
				""", 10)]
		if tradition == "Necromancer":
			return [wizard_feature("Inured to Undeath", """
				You have Resistance to Necrotic damage, and your Hit Point
				maximum cannot be reduced.
				<br><i>You have heard the Name of Silence so often it no
				longer startles your body.</i>
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
		return [wizard_feature("Spell Breaker", """
			You always have <i>Counterspell</i> and <i>Dispel Magic</i>
			prepared. You can cast Dispel Magic as a Bonus Action, and you
			add your Proficiency Bonus to its ability check.
			When you cast either spell this way, your Arcane Ward regains
			Hit Points equal to the spell's level.
			<br><i>To unname a working is also a name. The ward drinks
			what you take apart.</i>
			""", 10)]

	def _tradition_level_fourteen(self, character, tradition, lore, sought_name, level, int_bonus):
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
				<br><i>Speak a name too completely and the unnamed Way takes
				its due. {sought_name} is not a tool. It is a relationship,
				and relationships burn.</i>
				""", 14)]
		if tradition == "Illusionist":
			return [wizard_feature("Illusory Reality", """
				When you cast an Illusion spell with a spell slot, you can
				choose one inanimate, nonmagical object that is part of the
				illusion and make that object real for 1 minute. The object
				cannot deal damage or otherwise directly harm anyone.
				<br><i>Seeming, held long enough in a true name, forgets
				that it was only seeming. For a minute, the world agrees.</i>
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
				<br><i>A last name, once learned, can be spoken by more
				than one throat. You make sure it is yours.</i>
				""", 14)]
		if tradition == "Diviner":
			return [wizard_feature("Greater Portent", """
				The unseen now offers three numbers instead of two when
				you finish a Long Rest.
				<br><i>The Pattern is not a chain. It is a braid, and you
				have learned to hold a third strand.</i>
				""", 14)]
		return [wizard_feature("Spell Resistance", """
			You have Advantage on saving throws against spells, and you
			have Resistance to the damage of spells.
			<br><i>Other people's names slide off the uncarved block.
			You are harder to rewrite.</i>
			""", 14)]
