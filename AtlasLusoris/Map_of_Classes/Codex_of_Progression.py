'''Atlas Lusoris : Map of Classes:  Codex of Progression '''

''' Cartography '''
from typing import List
from AtlasActorLudi.Map_of_Scores import Modifier
from AtlasLusoris.Grimoire_of_Features import Feature




class Progression:
	def __init__(self, character):
		self.char = character

	def features(self) -> List[Feature]:
		raise NotImplementedError


def get_class_progression(character):
	"""
	Return a Progression instance bound to this character.
	"""
	class_name = character.character_class
	from .  import (  # local import avoids circulars during top-level load
			Barbarian, Bard, Cleric, Druid, Fighter, Monk,
			Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard
			)
	mapping = {
		"Fighter": 	Fighter,
		"Wizard":  	Wizard,
		"Barbarian": Barbarian,
		"Rogue": 	Rogue,
		"Paladin": 	Paladin,
		"Bard": 	Bard,
		"Druid": 	Druid,
		'Warlock': 	Warlock,
		'Monk': 	Monk,
		'Ranger': 	Ranger,
		'Sorcerer': 	Sorcerer,
		# Artificer?
		}
	prog_cls = mapping.get(class_name)
	return prog_cls(character)

def GetFeatures(character) -> List[Feature]:
	progression = get_class_progression(character)
	if progression:
		return progression.features()  # ✅ only one argument
	return []

def get_features(character):
	return GetFeatures(character)

# ── Starting equipment & proficiencies ────────────────────────
def apply_class_proficiencies(character):
	"""
	Give the character the armour / weapon proficiencies and initial
	equipment that PHB indica para su clase.  Add cases per class.
	"""
	from AtlasInventarium.Grimoire_of_Objects import Weapon, Object, choose_melee_weapon
	from AtlasActorLudi.Map_of_Scores import Modifier

	cls = character.character_class
	lvl = character.Level
	equip = character.equipment
	AS = character.abilities

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
			armor = equip.HeavyArmor()
			equip.buy_item(armor)
			equip.equip_defense(armor)
			sword = choose_melee_weapon(character.skills, AS)
			equip.buy_item(sword)
			equip.equip_right(sword)

			shield = Object(
					name="Shield",
					value=10,
					weight=6,
					description="+2 AC",
			)
			equip.buy_item(shield)
			equip.equip_left(shield)

	elif cls == "Wizard":
				character.skills.Simple_Weapons.set_proficiency()
				if lvl == 1:
						staff = choose_melee_weapon(character.skills, AS)
						equip.buy_item(staff)
						equip.equip_right(staff)

						book = Object(
								name="Spellbook",
								value=50,
								weight=3,
								description="Arcane writings",
								)
						equip.buy_item(book)
	elif cls == "Rogue":
				character.skills.Light.set_proficiency()
				character.skills.Simple_Weapons.set_proficiency()
				character.skills.Finesse.set_proficiency()
				character.skills.Thieves_Tools.set_proficiency()

				if lvl == 1:
					armor = equip.LightArmor(Modifier(AS.DEX))
					equip.buy_item(armor)
					equip.equip_defense(armor)

					dagger = choose_melee_weapon(character.skills, AS)

					equip.buy_item(dagger)
					equip.equip_right(dagger)

					tools = Object(
							name="Thieves' Tools",
							value=25,
							weight=1,
							)
					equip.buy_item(tools)
	elif cls == "Cleric":
		character.skills.Light.set_proficiency()
		character.skills.Medium.set_proficiency()
		character.skills.Shields.set_proficiency()
		character.skills.Simple_Weapons.set_proficiency()

		if lvl == 1:
			armor = equip.MediumArmor(Modifier(AS.DEX))
			equip.buy_item(armor)
			equip.equip_defense(armor)

			mace = choose_melee_weapon(character.skills, AS)
			equip.buy_item(mace)
			equip.equip_right(mace)

			shield = Object(
					name="Shield",
					value=10,
					weight=6,
					description="+2 AC",
					)
			equip.buy_item(shield)
			equip.equip_left(shield)
	elif cls == "Paladin":
				character.skills.Light.set_proficiency()
				character.skills.Medium.set_proficiency()
				character.skills.Shields.set_proficiency()
				character.skills.Simple_Weapons.set_proficiency()

				if lvl == 1:
						armor = equip.MediumArmor(Modifier(AS.DEX))
						equip.buy_item(armor)
						equip.equip_defense(armor)

						mace = Weapon(
								name="Mace",
								value=5,
								weight=4,
								N=1,
								D=6,
								Mod=Modifier(AS.STR),
								dmg="bludgeoning",
								weapon_type="Simple",
						)
						equip.buy_item(mace)
						equip.equip_right(mace)

						shield = Object(
								name="Shield",
								value=10,
								weight=6,
								description="+2 AC",
						)
						equip.buy_item(shield)
						equip.equip_left(shield)
	elif cls == "Druid":
		chosen = character.choose_skills(
			options=["Arcana","Animal Handling","Insight",
					 "Medicine","Nature","Perception",
					 "Religion","Survival"],
			count=2
			)
		for skill in chosen:
			getattr(character.skills, skill.replace(" ", "_")).set_proficiency()

		# — Weapon, Tool & Armor —
		character.skills.Simple_Weapons.set_proficiency()
		character.skills.Herbalism_Kit.set_proficiency()
		character.skills.Light.set_proficiency()
		character.skills.Shields.set_proficiency()
