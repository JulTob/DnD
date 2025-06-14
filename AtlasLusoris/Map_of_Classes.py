'''Atlas Lusoris : Map of Classes '''


''' Cartography '''
from collections import defaultdict
from dataclasses import dataclass
from typing import List, Optional

from AtlasLudus.Map_of_Dice import Dice


classes = [
	'Fighter',	'Wizard',	'Rogue',	'Cleric',
	'Ranger',	'Paladin',	'Bard',		'Monk',
	'Druid',	'Warlock',	'Sorcerer',	'Barbarian',
	]

subclasses = {
	'Fighter': [
		"Champion", "Battle Master", "Eldritch Knight", "Samurai"],
	'Wizard': [
		"Evocation", "Illusion", "Necromancy", "Divination",
		"Abjuration" ],
	'Rogue': [
		"Assassin",	 "Arcane Trickster", "Thief", "Swashbuckler",	],
	'Cleric': [
		"Knowledge", "War", "Tempest", "Life",
		"Light", "Trickery", "Nature", "Forge",
		"Grave", ],
	'Ranger': [
		"Hunter", "Beast Master", "Gloom Stalker",	"Horizon Walker" ],
	'Paladin': [
		"Devotion", "Oathbreaker", "Ancients",	 "Vengeance", ],
	'Bard': [
		"Lore",	 "Valor", "Glamour", "Swords", ],
	'Monk': [
		"Elements", "Open Hand", "Shadow", "Long Death", ],
	'Druid': [
		"Moon", "Land", "Shepherd",	"Spores", ],
	'Warlock': [
		"Great Old One", "Fiend", "Archfey", "Celestial", ],
	'Sorcerer': [
		"Draconic",	"Wild Magic", "Divine Soul", "Shadow Magic", ],
	'Barbarian': [
		"Berserker", "Wild Heart", "Storm Herald", ],
	}


_HIT_DIE_TABLE = {
	"Barbarian": 12,
	"Fighter":   10, "Paladin": 10, "Ranger": 10,
	"Bard": 8,  "Cleric": 8,  "Druid": 8,  "Monk": 8,
	"Rogue": 8, "Warlock": 8,
	"Sorcerer": 6, "Wizard": 6,          # 6 is correct per 5e SRD
	}

def health_dice(class_name: str) -> int:
	"""
	Return the size of this class’s hit die (e.g. 10 → d10).
	If class not found, roll 6d2 (value 6–12) as a fallback.
	"""
	die = _HIT_DIE_TABLE.get(class_name.title())
	if die is None:
		die = Dice(D=2, N=6)             # keeps your quirky fallback
	return die

@dataclass
class Feature:
	name: str
	level: int
	description: str

	def __str__(self):
		return f"<b>{self.name} (Lv {self.level})</b><br>{self.description}"

	def to_html(self) -> str:
		return f"""
		<div class='class-feature'>
			<h4>{self.name} <span class='level'>(Level {self.level})</span></h4>
			<p>{self.description}</p>
			</div>
		"""


class Progression:
	def features(self, level: int, subclass: Optional[str] = None) -> List[Feature]:
		raise NotImplementedError

FIGHTING_STYLES = {
	"Archery"   : " +2 bonus to attack rolls you make with ranged weapons.",
	"Defense"   : " +1 bonus to AC while wearing armor.",
	"Dueling"   : " +2 bonus to damage rolls when wielding a single one-handed weapon.",
	"Great Weapon Fighting":
				 " Re-roll 1s and 2s on damage dice with two-handed or versatile weapons.",
	"Protection": " Use a reaction to impose disadvantage on an attack that targets an ally within 5 ft.",
	"Two-Weapon Fighting":
				 " Add ability modifier to damage of your off-hand attack.",
}

class FighterProgression(Progression):
	def features(self, level: int, subclass: Optional[str] = None,
				 context: Optional[object] = None) -> List[Feature]:
		features = []
		if level >= 1:
			features.append(Feature("Second Wind", 1, "Bonus action to regain 1d10 + level HP."))
			features.append(Feature("Fighting Style", 1, "Choose specialty: Archery, Defense, etc."))
		if level >= 2:
			features.append(Feature("Action Surge", 2, "Take an extra action once per short rest."))
		if level >= 3 and subclass == "Champion":
			features.append(Feature("Improved Critical", 3, "Crit on 19-20."))
		if level >= 5:
			features.append(Feature("Extra Attack", 5, "Attack twice instead of once."))
		return features


class WizardProgression(Progression):
	def features(self, level: int, subclass: Optional[str] = None) -> List[Feature]:
		features = []
		if level >= 1:
			features.append(Feature("Spellcasting", 1, "Cast spells using Intelligence."))
			features.append(Feature("Arcane Recovery", 1, "Recover spell slots on short rest."))
		if level >= 2:
			features.append(Feature("Arcane Tradition", 2, "Choose magic school."))
			if subclass == "Evocation":
				features.append(Feature("Sculpt Spells", 2, "Protect allies from evocation spells."))
		if level >= 6 and subclass == "Evocation":
			features.append(Feature("Potent Cantrip", 6, "Cantrips deal damage on save."))
		if level >= 18:
			features.append(Feature("Spell Mastery", 18, "Cast a 1st or 2nd level spell at will."))
		if level >= 20:
			features.append(Feature("Signature Spells", 20, "Use signature spells freely."))
		return features

class MulticlassProgression(Progression):
	def __init__(self, class1: Progression, level1: int, class2: Progression, level2: int):
		self.class1 = class1
		self.level1 = level1
		self.class2 = class2
		self.level2 = level2

def features(self, level: int = None, subclass: str = None) -> List[Feature]:
		return self.class1.features(self.level1) + self.class2.features(self.level2)

def get_class_progression(class_name: str) -> Optional[Progression]:
	mapping = {
		"Fighter": FighterProgression(),
		"Wizard": WizardProgression(),
		# Add more classes as needed...
	}
	return mapping.get(class_name)

def GetFeatures(character) -> List[Feature]:
	class_name = getattr(character, "Class", "")
	level = getattr(character, "Level", 1)
	subclass = getattr(character, "Subclass", None)
	progression = get_class_progression(class_name)
	if progression:
		return progression.features(level, subclass)
	return []

# ── Starting equipment & proficiencies ────────────────────────
def apply_class_proficiencies(character):
	"""
	Give the character the armour / weapon proficiencies and initial
	equipment that PHB indica para su clase.  Add cases per class.
	"""
	cls = character.character_class
	lvl = character.Level

	if cls == "Fighter":
		# register proficiencies (you may store them in character.proficiencies)
		character.skills.Light.set_proficiency()
		character.skills.Medium.set_proficiency()
		character.skills.Heavy.set_proficiency()
		character.skills.Shields.set_proficiency()
		character.skills.Simple_Weapons.set_proficiency()
		character.skills.Martial_Weapons.set_proficiency()

		# level-1 starting gear (only if Inventory object supports .equip())
		if lvl == 1:
			character.equipment.equip("Chain Mail")
			character.equipment.equip("Longsword")
			character.equipment.equip("Shield")

	elif cls == "Wizard":
		character.skills.Simple_Weapons.set_proficiency()
		if lvl == 1:
			character.equipment.equip("Quarterstaff")
			character.equipment.equip("Spellbook")

	# …añade el resto de clases cuando quieras
