# AtlasLudus/Map_of_dice.py

from Minion import Initialized, Alert, Inform, Warning, News, Ends, Fail, Catched, FailureError

# Define a custom error class for Map_of_dice.py
class DiceError(Exception):
    """Base exception for Dice-related errors."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

### Dice and Rolling Functions ###
import random
import re



def Dice(D: int = 6, N: int = 1, modifier: int = 0) -> int:
	'''	Cartography '''
	"""
	Rolls N dices with D sides each.
	If D is 0, simulates a coin flip.
	Adds the base modifier to the result.

	Preconditions:
	-	D >= 0 (Number of sides on each die)
	-	N > 0 (Number of dice)
	-	modifier is an integer.

	Postconditions:
	-	Returns the sum of the rolls plus the modifier.
	"""
	if N<1: 	N = 1
	roll = 0

	for _ in range(N):
		if D >= 1:
			throwing = random.randint(1, D)
		else:
			throwing = random.randint(D, 1)
		roll += throwing
	#print(f"Rolling {N}d{D}: {roll}")
	result = roll + modifier

	if not isinstance(result, int):
		raise DiceError(f"Unexpected result type: {type(result)}. Expected int.\n{e}")
	return result

def Roll(text: str = "1d20") -> int:
	"""	Interprets a dice roll string (e.g., '2d6 + 3')
	and executes the roll.
	Preconditions:
	-	Text is a string in 'NdM + X' format.
	Postconditions:
	-	Returns the result of the roll.
	"""
	if not isinstance(text, str): raise DiceError("Input must be a string.")

	match = re.match(r'(\d+)d(\d+)(?:\s*\+\s*(\d+))?', text)
	if not match:
		raise DiceError(f"Invalid dice roll format: {text}")

	# Extracting the values
	num_dice = int(match.group(1))
	num_sides = int(match.group(2))
	modifier = int(match.group(3))

	if modifier:
		modifier = int(modifier)
	else:
		modifier = 0


	result = Dice(D = num_sides, N = num_dice, modifier = modifier)
	if not isinstance(result, int): raise DiceError("Dice result not an integer.")
	return result

def Dizero(D: int = 6, N: int = 1) -> int:
	"""	Rolls a dice with sides 0 to D.
	Preconditions:
	-	D and N are integers
	- 	N is positive.
	Postconditions:
	-	Returns the sum of the rolls.
	"""
	if not isinstance(D, int): raise DiceError("D must be an integer.")
	if not isinstance(N, int) and N > 0: raise DiceError("N must be a positive integer.")

	roll = 0
	for m in range(N):
		if D < 0:
			throwing = random.randint(D, 0)
		else:
			throwing = random.randint(0, D)
		roll += throwing
	result = roll
	if not isinstance(result, int): raise DiceError("Output must be an integer.")
	return result

def SelectDx(d=0, pb=2):
	if d == 0:
		result = random.choice(
			["D4",	"D6",	"D8",	"D10"]
			)
		return result
	return f"D{d}"

def New_Stat():
	rolls = [Dice(6) for _ in range(4)]
	return sum(sorted(rolls)[1:])
