""" Grimoire of Saving Throws """
"""
	This Grimoire enables the bearer to resist and endure adversities
	through the powers of:
	Strength, Dexterity, Constitution,
	Intelligence, Wisdom, and Charisma.
	Each score has a saving throw proficiency that can increase one's
	resilience.
"""
import random
from Minion import Initialized, Alert, Inform, Warning, News
try: # Cartography:
	from AtlasActorLudi.Map_of_Scores 	import Modifier
	from AtlasLudus.Map_of_Dice 		import Dice
	News("Every Atlas for Saving Throws have been procured. \nWe can start our Resistance.")
except ImportError as e:
	Alert(f"The Atlases to Saving Throws have not been found:\n {e}", e)

class SavingThrows:
	def __init__(ST, AS, PB):
		"""	Initialize saving throws
			for each ability score
			with proficiency adjustments.	"""
		Initialized("[SavingThrows]")
		# Core saving throw modifiers
		ST.STR = Modifier(AS.STR)
		ST.DEX = Modifier(AS.DEX)
		ST.CON = Modifier(AS.CON)
		ST.INT = Modifier(AS.INT)
		ST.WIS = Modifier(AS.WIS)
		ST.CHA = Modifier(AS.CHA)

		# Determine proficiency bonuses for each saving throw
		ST.proficiency = ST.assign_proficiencies()

		# Apply proficiency bonus if proficient
		ST.apply_proficiency_bonus(PB)

	def assign_proficiencies(ST):
		"""
        Randomly assign proficiency to at least two saving throws.
        Ensures that the character has strengths across varied saving throws.
        """
		Initialized("[Saving Throws]assign proficiencies<>")
		ST.proficiency = {
			'STR': False,
			'DEX': False,
			'CON': False,
			'INT': False,
			'WIS': False,
			'CHA': False
			}

		# Ensure a minimum of two proficiencies
		how_many_proficiencies = 0
		while how_many_proficiencies < 2:
			ability = random.choice(list(ST.proficiency.keys()))
			ST.proficiency[ability] = True
			how_many_proficiencies = list(ST.proficiency.values()).count(True)

		return ST.proficiency

	def apply_proficiency_bonus(ST,PB):
		"""
		Apply proficiency bonus to proficient saving throws.
		"""
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
		  f"STR: {ST.STR:+}  <br>" +
		  f"DEX: {ST.DEX:+}  <br>" +
		  f"CON: {ST.CON:+}  <br>" +
		  f"INT: {ST.INT:+}  <br>" +
		  f"WIS: {ST.WIS:+}  <br>" +
		  f"CHA: {ST.CHA:+}  <br>")
		return str
