""" Grimoire of Character Skills """
"""
This Grimoire endows the bearer with skillful mastery across diverse domains,
enhancing natural abilities and trained proficiencies.
"""

from AtlasMechanica.Map_of_Scores import Modifier
from AtlasMechanica.Map_of_Dice import Dice
import random



class Skill:
	def __init__(skill,
		name,
		ability_score,
		ProficiencyBonus=2,
		proficiency_level=0,
		jack_of_all_trades=False):

		"""
		Initialize a Skill.

		Parameters:
		- name: Name of the skill (string).
		- ability_score: The ability score associated with the skill (integer).
		- proficiency_level: 0 = not proficient, 1 = proficient, 2 = expertise.
		"""

		skill.name = name
		skill.ability_score = ability_score
		skill.proficiency_level = proficiency_level
		skill.ProficiencyBonus = ProficiencyBonus
		skill.jack = jack_of_all_trades

	def set_proficiency(skill):
		"""Set the skill as proficient."""
		if skill.proficiency_level < 1:
			skill.proficiency_level = 1

	def set_expertise(skill):
		"""Set the skill as having expertise."""
		skill.proficiency_level = 2

	def remove_proficiency(skill):
		"""Remove proficiency or expertise from the skill."""
		skill.proficiency_level = 0

	def calculate_modifier(skill, proficiency_bonus):
		"""
		Calculate the total skill modifier.

		Parameters:
		- proficiency_bonus: The character's proficiency bonus (integer).

		Returns:
		- Total skill modifier (integer).
		"""
		base_modifier = skill.calculate_ability_modifier()
		if skill.proficiency_level == 1:
			return base_modifier + skill.ProficiencyBonus
		elif skill.proficiency_level == 2:
			return base_modifier + 2 * skill.ProficiencyBonus
		else:
			if skill.jack:
				# If Jack of All Trades is active and the skill is not proficient, add half PB
				return base_modifier + (skill.ProficiencyBonus//2)
			return base_modifier

	def calculate_ability_modifier(skill):
		"""Calculate the ability modifier from the ability score."""
		return (skill.ability_score - 10) // 2

	def modifier(skill):
		return skill.calculate_modifier(proficiency_bonus)

	def is_proficient(skill):
		if skill.proficiency_level > 0:
			return True
		else:
			return False

	def __repr__(skill):
		"""String representation of the Skill."""
		return (f"{skill.name}: Ability Score = {skill.ability_score}, "
				f"Proficiency Level = {skill.proficiency_level}")

class Tool(Skill):
	def __init__(tool, name, proficiency_level=0):
		"""
		Initialize a Tool.

		Parameters:
		- name: Name of the tool (string).
		- ability_score: The ability score associated with the tool (integer).
		- proficiency_level:
			0 = not proficient,
			1 = proficient,
			2 = expertise.
		"""
		super().__init__(name, ability_score=0, proficiency_level=proficiency_level)

	def modifier(tool,ProficiencyBonus):
		if tool.proficiency_level == 1:
			return 1
		elif tool.proficiency_level == 2:
			return 2
		else:
			return 0
		return

	def calculate_modifier(tool, proficiency_bonus):
		return modifier(proficiency_bonus)


class Weapon(Tool):
	def __init__(weapon, name, proficiency_level=0):
		"""
		Initialize a Weapon proficiency, inheriting from Tool.
		"""
		super().__init__(name, proficiency_level)

class Armor(Tool):
	def __init__(armor, name, proficiency_level=0):
		"""
		Initialize an Armor proficiency, inheriting from Tool.
		"""
		super().__init__(name, proficiency_level)



class Training:
	def __init__(training, AS, ProficiencyBonus, proficient_skills=None):
		"""
		Initialize Character Training
		sets Skills, Tool proficiency, weapons, armors...
		with
		Ability Scores (AS),
		Proficiency Bonus (ProficiencyBonus),
		and optional lists of proficient and expertise skills.

		Parameters:
		- 	AS: An AbilityScores instance with attributes STR, DEX, CON, INT, WIS, CHA.
		- 	PB: Proficiency Bonus [integer].
		- 	proficient_skills: List of skill names the character is proficient in.
		"""
		training.ProficiencyBonus = ProficiencyBonus
		training.AS = AS

		training.Set_Skill_Training()
		training.Set_Tool_Training()
		training.Set_Weapon_Training()
		training.Set_Armor_Training()


	def Set_Skill_Training(training):
		# STR
		training.Athletics = Skill('Athletics', training.AS.STR, ProficiencyBonus)

		# DEX
		training.Acrobatics = Skill('Acrobatics', training.AS.DEX, ProficiencyBonus)
		training.Sleight_of_Hand = Skill('Sleight of Hand', training.AS.DEX, ProficiencyBonus)
		training.Stealth = Skill('Stealth', training.AS.DEX, ProficiencyBonus)
		# CON
		# INT
		training.Arcana = Skill('Arcana', training.AS.INT, ProficiencyBonus)
		training.History = Skill('History', training.AS.INT, ProficiencyBonus)
		training.Investigation = Skill('Investigation', training.AS.INT, ProficiencyBonus)
		training.Nature = Skill('Nature', training.AS.INT, ProficiencyBonus)
		training.Religion = Skill('Religion', training.AS.INT, ProficiencyBonus)

		# WIS
		training.Animal_Handling = Skill('Animal Handling', training.AS.WIS, ProficiencyBonus)
		training.Insight = Skill('Insight', training.AS.WIS, ProficiencyBonus)
		training.Medicine = Skill('Medicine', training.AS.WIS, ProficiencyBonus)
		training.Perception = Skill('Perception', training.AS.WIS, ProficiencyBonus)
		training.Survival = Skill('Survival', training.AS.WIS, ProficiencyBonus)
		# CHA
		training.Deception = Skill('Deception', training.AS.CHA, ProficiencyBonus)
		training.Intimidation = Skill('Intimidation', training.AS.CHA, ProficiencyBonus)
		training.Performance = Skill('Performance', training.AS.CHA, ProficiencyBonus)
		training.Persuasion = Skill('Persuasion', tr.CHA, ProficiencyBonus)

	def Set_Tool_Training(training):
		# Tools
		training.Thieves_Tools = Tool("Thieves' Tools")
		training.Disguise_Kit = Tool("Disguise Kit")
		training.Forgery_Kit = Tool("Forgery Kit")

		training.Musical_Instrument = Tool("Musical Instrument")
		training.Gaming_Set = Tool("Gaming Set")

		training.Herbalism_Kit = Tool("Herbalism Kit")

		training.Navigator_Tools = Tool("Navigator's Tools")

		# ARTISAN TOOLS
		training.Alchemist_Supplies = Tool("Alchemist's Supplies")
		training.Brewer_Supplies = Tool("Brewer's Supplies")
		training.Calligrapher_Supplies = Tool("Calligrapher's Supplies")
		training.Carpenter_Tools = Tool("Carpenter's Tools")
		training.Cartographer_Tools = Tool("Cartographer's Tools")
		training.Cobbler_Tools = Tool("Cobbler's Tools")
		training.Cook_Utensils = Tool("Cook's Utensils")
		training.Glassblower_Tools = Tool("Glassblower's Tools")
		training.Jeweler_Tools = Tool("Jeweler's Tools")
		training.Leatherworker_Tools = Tool("Leatherworker's Tools")
		training.Mason_Tools = Tool("Mason's Tools")
		training.Painter_Supplies = Tool("Painter's Supplies")
		training.Potter_Tools = Tool("Potter's Tools")
		training.Smith_Tools = Tool("Smith's Tools")
		training.Tinker_Tools = Tool("Tinker's Tools")
		training.Weaver_Tools = Tool("Weaver's Tools")
		training.Woodcarver_Tools = Tool("Woodcarver's Tools")


	def Set_Weapon_Training(training):
		training.Simple_Weapons = Weapon('Simple Weapons')
		training.Martial_Weapons = Weapon('Martial Weapons')
		training.Hand_Crossbow = Weapon('Hand Crossbow')
		training.Rapier = Weapon('Rapier')
		training.Shortsword = Weapon('Shortsword')
		training.Finesse = Weapon('Finesse Weapons')
		training.Light_Weapons = Weapon('Light Weapons')


	def Set_Armor_Training(training):
		training.Shields = Armor('Shields')
		training.Light = Armor('Light Armor')
		training.Medium = Armor('Medium Armor')
		training.Heavy = Armor('Heavy Armor')
		training.Unarmed_Monk = Armor('Unarmed Defense')
		training.Unarmed_Barb = Armor('Unarmed Defense')

	def get_all_weapons(training):
		return [
			training.Simple_Weapons,
			training.Martial_Weapons,
			training.Hand_Crossbow,
			training.Rapier,
			training.Shortsword,
			training.Finesse,
			training.Light_Weapons,
			# Add other weapons here...
		]

	def get_proficient_weapons(training):
		"""
		Returns a list of proficient weapons only.
		"""
		all_weapons = training.get_all_weapons()

		return [weapon for weapon in all_weapons if weapon.proficiency_level > 0]

	def get_all_armors(training):
		return [
			training.Shields,
			training.Light,
			training.Medium,
			training.Heavy,
			training.Unarmed_Monk,
			training.Unarmed_Barb,
			]

	def get_proficient_armors(training):
		"""
		Returns a list of proficient armors only.
		"""
		all_armors = training.get_all_armors()

		return [armor for armor in all_armors if armor.proficiency_level > 0]

	def set_proficient(training, skill_name):
		"""Set a skill as proficient."""
		skill = training._get_skill(skill_name)
		skill.set_proficiency()

	def set_expertise(training, skill_name):
		"""Set a skill as having expertise."""
		skill = training._get_skill(skill_name)
		skill.set_expertise()

	def remove_proficiency(training, skill_name):
		"""Remove proficiency or expertise from a skill."""
		skill = training._get_skill(skill_name)
		skill.remove_proficiency()

	def get_skill_modifier(training, skill_name):
		"""
		Get the total modifier for a given skill.

		Parameters:
		- skill_name: Name of the skill (string).

		Returns:
		- Total skill modifier (integer).
		"""
		skill = training._get_skill(skill_name)
		return skill.calculate_modifier(training.ProficiencyBonus)

	def passive(training, skill_name):
		"""
		Calculate the passive score for a given skill.

		Parameters:
		- skill_name: Name of the skill (string).

		Returns:
		- Passive score (integer).
		"""
		return 10 + training.get_skill_modifier(skill_name)

	def _get_skill(training, skill_name):
		"""Retrieve a Skill instance by name."""
		if not hasattr(training, skill_name):
			raise ValueError(f"Skill '{skill_name}' does not exist.")
		return getattr(training, skill_name)

	def __repr__(training):
		"""String representation of all skills and their states."""
		skills = [
			training.Athletics, training.Acrobatics, training.Sleight_of_Hand, training.Stealth,
			training.Arcana, training.History, training.Investigation, training.Nature, training.Religion,
			training.Animal_Handling, training.Insight, training.Medicine, training.Perception,
			training.Survival, training.Deception, training.Intimidation, training.Performance, training.Persuasion
		]
		return '\n'.join([str(skill) for skill in skills])

	def Passive(training,skill,ProficiencyBonus):
		return 10+skill.modifier(ProficiencyBonus)


	def activate_proficiencies(training, n, skill_names):
		"""
		Activates proficiency in `n` skills from the provided skill_list.

		Args:
		- n: The number of skills to activate.
		- skill_list: A list of skill names (strings).
		"""

		# Randomly pick a skill from the list
		s = random.choice(skill_names)

		if n>0 and skill_names:
			if s == "Athletics":
				if training.Athletics.proficiency_level < 1:
					training.Athletics.proficiency_level = 1  # Or call training.Athletics.set_proficient()
					skill_names.remove(s)
					return training.activate_proficiencies(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_proficiencies(n,skill_names)


			elif s == "Acrobatics":
				if training.Acrobatics.proficiency_level < 1:
					training.Acrobatics.proficiency_level = 1
					skill_names.remove(s)
					return training.activate_proficiencies(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_proficiencies(n,skill_names)

			elif s == "Sleight of Hand":
				if training.Sleight_of_Hand.proficiency_level < 1:
					training.Sleight_of_Hand.proficiency_level = 1
					skill_names.remove(s)
					return training.activate_proficiencies(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_proficiencies(n,skill_names)

			elif s == "Stealth":
				if training.Stealth.proficiency_level < 1:
					training.Stealth.proficiency_level = 1
					skill_names.remove(s)
					return training.activate_proficiencies(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_proficiencies(n,skill_names)

			elif s == "Arcana":
				if training.Arcana.proficiency_level < 1:
					training.Arcana.proficiency_level = 1
					skill_names.remove(s)
					return training.activate_proficiencies(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_proficiencies(n,skill_names)

			elif s == "History":
				if training.History.proficiency_level < 1:
					training.History.proficiency_level = 1
					skill_names.remove(s)
					return training.activate_proficiencies(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_proficiencies(n,skill_names)

			elif s == "Investigation":
				if training.Investigation.proficiency_level < 1:
					training.Investigation.proficiency_level = 1
					skill_names.remove(s)
					return training.activate_proficiencies(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_proficiencies(n,skill_names)

			elif s == "Nature":
				if training.Nature.proficiency_level < 1:
					training.Nature.proficiency_level = 1
					skill_names.remove(s)
					return training.activate_proficiencies(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_proficiencies(n,skill_names)

			elif s == "Religion":
				if training.Religion.proficiency_level < 1:
					training.Religion.proficiency_level = 1
					skill_names.remove(s)
					return training.activate_proficiencies(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_proficiencies(n,skill_names)

			elif s == "Animal Handling":
				if training.Survival.proficiency_level < 1:
					training.Survival.proficiency_level = 1
					skill_names.remove(s)
					return training.activate_proficiencies(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_proficiencies(n,skill_names)

			elif s == "Insight":
				if training.Insight.proficiency_level < 1:
					training.Insight.proficiency_level = 1
					skill_names.remove(s)
					return training.activate_proficiencies(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_proficiencies(n,skill_names)

			elif s == "Medicine":
				if training.Medicine.proficiency_level < 1:
					training.Medicine.proficiency_level = 1
					skill_names.remove(s)
					return training.activate_proficiencies(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_proficiencies(n,skill_names)

			elif s == "Survival":
				if training.Survival.proficiency_level < 1:
					training.Survival.proficiency_level = 1
					skill_names.remove(s)
					return training.activate_proficiencies(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_proficiencies(n,skill_names)

			elif s == "Perception":
				if training.Perception.proficiency_level < 1:
					training.Perception.proficiency_level = 1
					skill_names.remove(s)
					return training.activate_proficiencies(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_proficiencies(n,skill_names)

			elif s == "Deception":
				if training.Deception.proficiency_level < 1:
					training.Deception.proficiency_level = 1
					skill_names.remove(s)
					return training.activate_proficiencies(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_proficiencies(n,skill_names)

			elif s == "Intimidation":
				if training.Intimidation.proficiency_level < 1:
					training.Intimidation.proficiency_level = 1
					skill_names.remove(s)
					return training.activate_proficiencies(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_proficiencies(n,skill_names)
			elif s == "Persuasion":
				if training.Persuasion.proficiency_level < 1:
					training.Persuasion.proficiency_level = 1
					skill_names.remove(s)
					return training.activate_proficiencies(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_proficiencies(n,skill_names)
			elif s == "Performance":
				if training.Performance.proficiency_level < 1:
					training.Performance.proficiency_level = 1
					skill_names.remove(s)
					return training.activate_proficiencies(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_proficiencies(n,skill_names)


			elif s == "Thieves' Tools":
				if training.Thieves_Tools.proficiency_level < 1:
					training.Thieves_Tools.proficiency_level = 1
					skill_names.remove(s)
					return training.activate_proficiencies(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_proficiencies(n,skill_names)
			elif s == "Disguise Kit":
				if training.Disguise_Kit.proficiency_level < 1:
					training.Disguise_Kit.proficiency_level = 1
					skill_names.remove(s)
					return training.activate_proficiencies(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_proficiencies(n,skill_names)

			elif s == "Alchemist's Supplies":
				if training.Alchemist_Supplies.proficiency_level < 1:
					training.Alchemist_Supplies.proficiency_level = 1
					skill_names.remove(s)
					return training.activate_proficiencies(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_proficiencies(n,skill_names)
			elif s == "Brewer's Supplies":
				if training.Brewer_Supplies.proficiency_level < 1:
					training.Brewer_Supplies.proficiency_level = 1
					skill_names.remove(s)
					return training.activate_proficiencies(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_proficiencies(n,skill_names)
			elif s == "Calligrapher's Supplies":
				if training.Calligrapher_Supplies.proficiency_level < 1:
					training.Calligrapher_Supplies.proficiency_level = 1
					skill_names.remove(s)
					return training.activate_proficiencies(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_proficiencies(n,skill_names)

			elif s == "Cartographer's Supplies":
				if training.Cartographer_Supplies.proficiency_level < 1:
					training.Cartographer_Supplies.proficiency_level = 1
					skill_names.remove(s)
					return training.activate_proficiencies(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_proficiencies(n,skill_names)


			skill_names.remove(s)
			n -= 1
			training.activate_proficiencies(n, skill_names)


	def activate_expertise(training, n, skill_names):
		# Randomly pick a skill from the list
		s = random.choice(skill_names)

		if n>0 and skill_names:
			if s == "Athletics":
				if training.Athletics.proficiency_level < 2:
					training.Athletics.proficiency_level = 2  # Or call training.Athletics.set_proficient()
					skill_names.remove(s)
					return training.activate_expertise(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_expertise(n,skill_names)


			elif s == "Acrobatics":
				if training.Acrobatics.proficiency_level < 2:
					training.Acrobatics.proficiency_level = 2
					skill_names.remove(s)
					return training.activate_expertise(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_expertise(n,skill_names)

			elif s == "Sleight of Hand":
				if training.Sleight_of_Hand.proficiency_level < 2:
					training.Sleight_of_Hand.proficiency_level = 2
					skill_names.remove(s)
					return training.activate_expertise(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_expertise(n,skill_names)

			elif s == "Stealth":
				if training.Stealth.proficiency_level < 2:
					training.Stealth.proficiency_level = 2
					skill_names.remove(s)
					return training.activate_expertise(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_expertise(n,skill_names)

			elif s == "Arcana":
				if training.Arcana.proficiency_level < 2:
					training.Arcana.proficiency_level = 2
					skill_names.remove(s)
					return training.activate_expertise(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_expertise(n,skill_names)

			elif s == "History":
				if training.History.proficiency_level < 2:
					training.History.proficiency_level = 2
					skill_names.remove(s)
					return training.activate_expertise(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_expertise(n,skill_names)

			elif s == "Investigation":
				if training.Investigation.proficiency_level < 2:
					training.Investigation.proficiency_level = 2
					skill_names.remove(s)
					return training.activate_expertise(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_expertise(n,skill_names)

			elif s == "Nature":
				if training.Nature.proficiency_level < 2:
					training.Nature.proficiency_level = 2
					skill_names.remove(s)
					return training.activate_expertise(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_expertise(n,skill_names)

			elif s == "Religion":
				if training.Religion.proficiency_level < 2:
					training.Religion.proficiency_level = 2
					skill_names.remove(s)
					return training.activate_expertise(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_expertise(n,skill_names)

			elif s == "Animal Handling":
				if training.Survival.proficiency_level < 2:
					training.Survival.proficiency_level = 2
					skill_names.remove(s)
					return training.activate_expertise(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_expertise(n,skill_names)

			elif s == "Insight":
				if training.Insight.proficiency_level < 2:
					training.Insight.proficiency_level = 2
					skill_names.remove(s)
					return training.activate_expertise(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_expertise(n,skill_names)

			elif s == "Medicine":
				if training.Medicine.proficiency_level < 2:
					training.Medicine.proficiency_level = 2
					skill_names.remove(s)
					return training.activate_expertise(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_expertise(n,skill_names)

			elif s == "Survival":
				if training.Survival.proficiency_level < 2:
					training.Survival.proficiency_level = 2
					skill_names.remove(s)
					return training.activate_expertise(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_expertise(n,skill_names)

			elif s == "Perception":
				if training.Perception.proficiency_level < 2:
					training.Perception.proficiency_level = 2
					skill_names.remove(s)
					return training.activate_expertise(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_expertise(n,skill_names)

			elif s == "Deception":
				if training.Deception.proficiency_level < 2:
					training.Deception.proficiency_level = 2
					skill_names.remove(s)
					return training.activate_expertise(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_expertise(n,skill_names)

			elif s == "Intimidation":
				if training.Intimidation.proficiency_level < 2:
					training.Intimidation.proficiency_level = 2
					skill_names.remove(s)
					return training.activate_expertise(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_expertise(n,skill_names)
			elif s == "Persuasion":
				if training.Persuasion.proficiency_level < 2:
					training.Persuasion.proficiency_level = 2
					skill_names.remove(s)
					return training.activate_expertise(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_expertise(n,skill_names)
			elif s == "Performance":
				if training.Performance.proficiency_level < 2:
					training.Performance.proficiency_level = 2
					skill_names.remove(s)
					return training.activate_expertise(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_expertise(n,skill_names)


			elif s == "Thieves' Tools":
				if training.Thieves_Tools.proficiency_level < 2:
					training.Thieves_Tools.proficiency_level = 2
					skill_names.remove(s)
					return training.activate_expertise(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_expertise(n,skill_names)
			elif s == "Disguise Kit":
				if training.Disguise_Kit.proficiency_level < 2:
					training.Disguise_Kit.proficiency_level = 2
					skill_names.remove(s)
					return training.activate_expertise(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_expertise(n,skill_names)

			elif s == "Alchemist's Supplies":
				if training.Alchemist_Supplies.proficiency_level < 2:
					training.Alchemist_Supplies.proficiency_level = 2
					skill_names.remove(s)
					return training.activate_expertise(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_expertise(n,skill_names)
			elif s == "Brewer's Supplies":
				if training.Brewer_Supplies.proficiency_level < 2:
					training.Brewer_Supplies.proficiency_level = 2
					skill_names.remove(s)
					return training.activate_expertise(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_expertise(n,skill_names)
			elif s == "Calligrapher's Supplies":
				if training.Calligrapher_Supplies.proficiency_level < 2:
					training.Calligrapher_Supplies.proficiency_level = 2
					skill_names.remove(s)
					return training.activate_expertise(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_expertise(n,skill_names)

			elif s == "Cartographer's Supplies":
				if training.Cartographer_Supplies.proficiency_level < 2:
					training.Cartographer_Supplies.proficiency_level = 2
					skill_names.remove(s)
					return training.activate_expertise(n-1,skill_names)
				else:
					skill_names.remove(s)
					return training.activate_expertise(n,skill_names)


			skill_names.remove(s)
			n -= 1
			training.activate_expertise(n, skill_names)


	def get_proficient_skills(training):
		"""
		Return a list of skill names (the actual name attribute) where proficiency_level is 1 or greater.
		"""
		proficient_skills = []

		# Loop through all attributes of Char_Skills
		for skill_obj in vars(training).values():
			# Check if it's a Skill object and has proficiency level >= 1
			if isinstance(skill_obj, Skill) and skill_obj.proficiency_level == 1:
				if not isinstance(skill_obj, Tool):
					proficient_skills.append(skill_obj.name)  # Use the skill's actual name attribute

		return proficient_skills


	def activate_jack_of_all_trades(training):
		"""
		Activate Jack of All Trades for all skills by setting the `jack` attribute to True
		in skills that are not proficient.
		"""
		for skill in training.get_all_skills():
			if skill.proficiency_level == 0:  # Only apply to non-proficient skills
				skill.jack = True

	def get_all_skills(training):
		"""
		Return a list of all skill objects.
		"""
		return [
			training.Athletics,
			training.Acrobatics ,
			training.Sleight_of_Hand ,
			training.Stealth,
			training.Arcana ,
			training.History ,
			training.Investigation ,
			training.Nature,
			training.Religion,
			training.Animal_Handling,
			training.Insight,
			training.Medicine,
			training.Perception,
			training.Survival,
			training.Deception,
			training.Intimidation ,
			training.Performance,
			training.Persuasion ,
		]
