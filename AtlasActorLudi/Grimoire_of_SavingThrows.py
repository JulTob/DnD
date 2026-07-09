""" Grimoire of Saving Throws """
"""
	This Grimoire enables the bearer to resist and endure adversities
	through the powers of:
	Strength, Dexterity, Constitution,
	Intelligence, Wisdom, and Charisma.
	Each score has a saving throw proficiency that can increase one's
	resilience.
"""
import app.random as random
try:
	from AtlasActorLudi.Map_of_Scores import Modifier
	from AtlasLudus.Map_of_Dice import Dice
except ImportError:
	raise

class SavingThrows:
	def __init__(ST, AS, PB, proficiencies=None, is_character=False):
		"""	Initialize saving throws
			for each ability score
			with proficiency adjustments.	"""
		#Initialized("[SavingThrows]")
		# Core saving throw modifiers
		ST.STR = Modifier(AS.STR)
		ST.DEX = Modifier(AS.DEX)
		ST.CON = Modifier(AS.CON)
		ST.INT = Modifier(AS.INT)
		ST.WIS = Modifier(AS.WIS)
		ST.CHA = Modifier(AS.CHA)

		# Determine proficiency bonuses for each saving throw
		ST.proficiency = ST.assign_proficiencies(proficiencies)

		# Apply proficiency bonus if proficient
		ST.apply_proficiency_bonus(PB, is_character)

	def assign_proficiencies(ST, given_proficiencies=None, is_character=False):
		"""
		Randomly assign proficiency to at least two saving throws.
		Ensures that the character has strengths across varied saving throws.
		"""
		#Initialized(f"[Saving Throws]assign proficiencies<{given_proficiencies}>")
		ST.proficiency = {
			'STR': False,
			'DEX': False,
			'CON': False,
			'INT': False,
			'WIS': False,
			'CHA': False
			}

		if given_proficiencies:
			for prof in given_proficiencies:
				ST.proficiency[prof.upper()] = True
		else:
			# Ensure a minimum of two proficiencies
			how_many_proficiencies = 0
			while how_many_proficiencies < 2:
				ability = random.choice(list(ST.proficiency.keys()))
				ST.proficiency[ability] = True
				how_many_proficiencies = list(ST.proficiency.values()).count(True)
		return ST.proficiency

	def apply_proficiency_bonus(ST,PB, is_character=False):
		"""
		Apply proficiency bonus to proficient saving throws.
		"""
		if is_character:
			if ST.proficiency['STR']: ST.STR += PB
			if ST.proficiency['DEX']: ST.DEX += PB
			if ST.proficiency['CON']: ST.CON += PB
			if ST.proficiency['INT']: ST.INT += PB
			if ST.proficiency['WIS']: ST.WIS += PB
			if ST.proficiency['CHA']: ST.CHA += PB
		else:
			if ST.proficiency['STR']: ST.STR += Dice(PB)
			if ST.proficiency['DEX']: ST.DEX += Dice(PB)
			if ST.proficiency['CON']: ST.CON += Dice(PB)
			if ST.proficiency['INT']: ST.INT += Dice(PB)
			if ST.proficiency['WIS']: ST.WIS += Dice(PB)
			if ST.proficiency['CHA']: ST.CHA += Dice(PB)

	@property
	def string(ST):
		"""
		Generate formatted [string] for each saving throw,
		showing all ability modifiers.
		"""

		str =(
		  f"STR: {ST.STR:+}\n" +
		  f"DEX: {ST.DEX:+}\n" +
		  f"CON: {ST.CON:+}\n" +
		  f"INT: {ST.INT:+}\n" +
		  f"WIS: {ST.WIS:+}\n" +
		  f"CHA: {ST.CHA:+}\n")
		return str
