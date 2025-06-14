### Character Scores Utilities ###
from Minion import Initialized, Alert, Inform, Warning, News, Ends, Fail, Catched, FailureError

try: # Cartography
	from AtlasLudus.Map_of_Dice 	import Dice, Dizero
	News("Atlas for Character Scores Utilities (Scores) procured")
except ModuleNotFoundError as e:
	Alert(f"The Atlases for Character Scores Utilities have not been found:\n {e}", e)


def PB(level: int) -> int:
	"""
	Calculate the proficiency bonus based on character level.
	Preconditions:
	-	<level> is a positive integer.
	Postconditions:
	- Returns an integer value representing the proficiency bonus.
	"""
	assert isinstance(level, int) and level > 0, "Level must be a positive integer."

	if level < 5:
		bonus = 2
	else:
		bonus = 2 + (level - 1) // 4

	return bonus

def Modifier(score: int) -> int:
	"""
	Calculate the ability modifier for a given score.
	Preconditions:
	-	<score> is an integer >= 1 (Ability Score)
	Postconditions:
	-	Returns the calculated modifier.
	"""
	try:
		assert isinstance(score, int), "Score must be an integer."
	except AssertionError as e:
		Fail(f"Score must be an integer. <score>: [{score}]",e)
		try:
			score = int(score)
			Inform(f"Score set to: {score}, [{score.type}]")
		except:
			FailureError("Modifier error assignation")

	modifier = (score - 10) // 2
	assert isinstance(modifier, int), "Modifier must be an integer."

	return modifier

def Proficiency(AS: int) -> int:
	"""
	Example function to calculate proficiency based on ability score.
	Preconditions:
	- 	AS is an integer.
	Postconditions:
	-	Returns a random number based on the calculated modifier.
	- 	This number represents a skill level averaging PB for
		Proficiency but going as up as an expertise
	"""
	assert isinstance(AS, int), "Ability score must be an integer."
	modifier = Modifier(AS)
	proficiency_value = Dice(modifier * 2)

	return proficiency_value

def NewAbilityScore() -> int:
	"""
	Generate a new ability score
		by rolling 4d6
		and dropping the lowest roll.
	Postconditions:
	-	Returns an integer between 3 and 18.
	"""

	d1 = Dice()
	d2 = Dice()
	d3 = Dice()
	d4 = Dice()
	score = d1+d2+d3+d4 - min(d1, d2, d3, d4)

	# Enforce the postcondition: if out of bounds, adjust
	if score < 3:
		score = 3
	elif score > 18:
		score = 18

	assert 3 <= score <= 18, "Generated ability score out of expected range."
	return score

def generate_stats() -> dict:
	""" Generate a dictionary
	with standard D&D ability scores. """
	stats = {
		'Strength': roll_stat(),
		'Dexterity': roll_stat(),
		'Constitution': roll_stat(),
		'Intelligence': roll_stat(),
		'Wisdom': roll_stat(),
		'Charisma': roll_stat(),
		}
	return stats

def roll_stat():
    rolls = [random.randint(1, 6) for _ in range(4)]
    return sum(sorted(rolls)[1:])

def generate_stats():
    stats = {
        'Strength': roll_stat(),
        'Dexterity': roll_stat(),
        'Constitution': roll_stat(),
        'Intelligence': roll_stat(),
        'Wisdom': roll_stat(),
        'Charisma': roll_stat(),
	    }
    return stats
