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
try:
	from AtlasLudus.Map_of_Dice import Dice
	from AtlasActorLudi.Map_of_Scores import Modifier, NewAbilityScore
except ImportError:
	raise

import app.random as random

def RandomAbilityScore():
	""" Rolls a new ability score using 4d6 drop lowest. """
	return NewAbilityScore()

class AbilityScores:
	""" Represents a set of ability scores for a character. """

	# RECOVERY NOTE 2026-08-31: vault NPC / FeaturesKit callers pass
	# character=. AbilityScoresKit already has (target, *, character);
	# this Grimoire is the class those callers still import. First
	# positional stays STR so recovered Grimoire_of_NPC(10,10,...,character=)
	# does not bind the first 10 as a target. See QST-0050.4.
	def __init__(
			AS,
			STR=10,
			DEX=10,
			CON=10,
			INT=10,
			WIS=10,
			CHA=10,
			*,
			character=None,
			):
		"""	Initialize ability scores for a character.	"""
		AS.STR = STR
		AS.DEX = DEX
		AS.CON = CON
		AS.INT = INT
		AS.WIS = WIS
		AS.CHA = CHA
		AS.character = character

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


class AttackRolls:
	"""To-hit per ability: proficient (mod+PB) and base (mod only).

	Display convention (string, for plain-text fallbacks):
		STR	+5⚜️	+2🔰
	⚜️ — proficient attack (matches Proficiency Bonus chip)
	🔰 — without proficiency (off-hand, improvised, etc.)
	"""

	ABILITIES = ("STR", "DEX", "CON", "INT", "WIS", "CHA")

	def __init__(rolls, AS, proficiency_bonus):
		pb = int(proficiency_bonus)
		mods = {
			"STR": Modifier(AS.STR),
			"DEX": Modifier(AS.DEX),
			"CON": Modifier(AS.CON),
			"INT": Modifier(AS.INT),
			"WIS": Modifier(AS.WIS),
			"CHA": Modifier(AS.CHA),
		}
		for abbr in rolls.ABILITIES:
			setattr(rolls, f"{abbr}_base", mods[abbr])
			setattr(rolls, f"{abbr}_prof", mods[abbr] + pb)

	def _line(rolls, abbr: str) -> str:
		base = getattr(rolls, f"{abbr}_base")
		prof = getattr(rolls, f"{abbr}_prof")
		return f"{abbr}\t{prof:+}⚜️\t{base:+}🔰"

	@property
	def string(rolls):
		return "\n".join(rolls._line(abbr) for abbr in rolls.ABILITIES)


def AbilityScoresPlus(AS, proficiency_bonus) -> AttackRolls:
	"""Ability modifier + proficiency for each score — the attack-roll reference."""
	return AttackRolls(AS, proficiency_bonus)


def apply_creature_ability_modifiers(creature) -> None:
	"""Apply racial and background tweaks to creature.AS (NPC path)."""
	from AtlasAlusoris.Map_of_Races import AS_racial_modifier

	AS_racial_modifier(creature)
