""" Grimoire of Ability Scores """
"""
	This Grimoire allows the holder to invoke the underlying powers
	of any creature:
	Strength:
		* 	The Might from your physical body
	Dexterity:
		* 	The precision on speedy tasks. Essential for tasks requiring
			quick reflexes and fine motor skills.
		* 	Reflects agility, balance, and precision in swift movements.
	Constitution:
		*	The hability to Resist harmful influences.
		* 	Denotes resilience and endurance.
	Intelligence:
		*	The knowledge you can remember and extract quickly
		* 	Represents memory, logic, and the capacity to learn quickly.
	Wisdom:
		*	The understandment of the world, yourself, and hidden relationships.
		* 	Signifies perceptiveness and the understanding of subtle connections.
		* 	Vital for insight, self-awareness, and intuition about the world.

	Charisma:
		*	The intrinsic Will of Power and your ability of imposing this Will
		* 	Embodies inner resolve and the ability to assert one's will.
		* 	Important for influence, presence, and leadership in social contexts.
"""
from Minion import Initialized, Alert, Inform, Warning, News, Ends, Fail, Catched, FailureError

try: # Cartography:
	from AtlasLudus.Map_of_Dice import Dice
	from AtlasActorLudi.Map_of_Scores import Modifier, NewAbilityScore
except ImportError as e:
	Alert(f"The Atlases to Routes have not been found:\n {e}", e)

import random

def RandomAbilityScore():
	""" Rolls a new ability score using 4d6 drop lowest. """
	return NewAbilityScore()

class AbilityScores:
	""" Represents a set of ability scores for a character. """

	def __init__(AS, STR=10, DEX=10, CON=10, INT=10, WIS=10, CHA=10):
		"""	Initialize ability scores for a character.	"""
		AS.STR = STR
		AS.DEX = DEX
		AS.CON = CON
		AS.INT = INT
		AS.WIS = WIS
		AS.CHA = CHA

	def RandomAbilityScores(AS):
		""" Assigns random scores to each ability. """
		AS.STR = RandomAbilityScore()
		AS.DEX = RandomAbilityScore()
		AS.CON = RandomAbilityScore()
		AS.INT = RandomAbilityScore()
		AS.WIS = RandomAbilityScore()
		AS.CHA = RandomAbilityScore()

	@property
	def modifiers(AS):
		""" Returns modifiers for each score. """
		return {
			'Strength': 	AS.mod(AS.STR),
			'Dexterity': 	AS.mod(AS.DEX),
			'Constitution': AS.mod(AS.CON),
			'Intelligence': AS.mod(AS.INT),
			'Wisdom': 		AS.mod(AS.WIS),
			'Charisma': 	AS.mod(AS.CHA),
		}

	def StandardArray(AS):
		""" Uses standard array
			[15, 14, 13, 12, 10, 8]
			and shuffles it across abilities.
		"""
		scores = [15, 14, 13, 12, 10, 8]
		random.shuffle(scores)
		AS.STR=scores[0]
		AS.DEX=scores[1]
		AS.CON=scores[2]
		AS.INT=scores[3]
		AS.WIS=scores[4]
		AS.CHA=scores[5]

	def mod(AS, score):
		"""Calculate the modifier for a given ability score."""
		return Modifier(score)

	@property
	def str_mod(AS):
		return AS.mod(AS.STR)

	@property
	def dex_mod(AS):
		return AS.mod(AS.DEX)

	@property
	def con_mod(AS):
		return AS.mod(AS.CON)

	@property
	def int_mod(AS):
		return AS.mod(AS.INT)

	@property
	def wis_mod(AS):
		return AS.mod(AS.WIS)

	@property
	def cha_mod(AS):
		return AS.mod(AS.CHA)



def AbilityScoresPlus(npc):
	from AtlasOfLore.Map_of_Backgrounds import AS_background_modifier
	from AtlasOfLore.Map_of_Races import AS_racial_modifier
	rc = npc.race

	creature_type = npc.race + ' ' + npc.subrace + ' ' + npc.background

	AS_background_modifier(npc)
	AS_racial_modifier(npc)
