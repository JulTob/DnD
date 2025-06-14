import random
from Minion import Initialized, Alert, Inform, Warning, News, Ends, Fail, Catched, FailureError
import AtlasAlusoris.Map_of_NPC as NPC

def select1(options, weights= None):
	"""
	Selects one item from options using weights if provided.
	"""
	if not weights:
		return random.choice(options)
	if weights:
		try:
			result = random.choices(options, weights=weights, k=1)[0]
		except (ValueError, TypeError) as e:
			Fail("Error!", e)
			if len(options) > len(weights):
				weigts.append(weights[-1:])
				return select1(options,weights)
			if len(options) < len(weights):
				options.append(options[-1:])
				return select1(options,weights)

	return result

def Probability(N = 1, out_of = 6):
	"""
	Calculates the probability of N specific outcomes occurring out of a total number of possible outcomes.

	Parameters:
	N (int): The number of desired outcomes (default is 1).
	out_of (int): The total number of possible outcomes (default is 6).

	Returns:
	float: The probability as a decimal between 0 and 1.
	"""
	# Step 1: Ensure inputs are valid.
	if N < 0 or out_of <= 0:
		raise ValueError("N must be non-negative and out_of must be a positive number.")

	if N > out_of:
		raise ValueError("N cannot exceed the total number of outcomes.")

	# Step 2: Calculate probability.
	probability = N / out_of

	# Step 3: Return the result.
	return probability

def flip_coin():
	return roll_check(1,2)

def check(N=1, out_of=6):
	return roll_check(N,out_of)


def roll_check(N=1, out_of=6):
	"""
	Simulates a dice roll and returns True with a probability of N/out_of.

	Parameters:
	N (int): The number of favorable outcomes (default is 1).
	out_of (int): The total number of possible outcomes (default is 6).

	Returns:
	bool: True with a probability of Probability(N,out_of), False otherwise.
	"""
	# Step 1: Validate inputs.
	if N < 0 or out_of <= 0:
		raise ValueError("N must be non-negative and out_of must be a positive number.")

	if N > out_of:
		raise ValueError("N cannot exceed the total number of outcomes.")

	# Step 2: Generate a random number between 0 and 1.
	random_number = random.uniform(0, 1)

	# Step 3: Compare the random number to the probability.
	result = random_number < Probability(N = N, out_of = out_of)

	return result

def round5s(n):
	return (n//5) * 5

def distance(n):
	result = n
	if n<=5: return 5
	elif n<=10: return 10
	elif n<=20: return 20
	elif n<=30: return 30
	elif n<=60: return 60
	elif n<=100: return 100
	elif n<=120: return 120
	elif n<=200: return 200
	elif n<=240: return 240
	return round5s(result)


def getGenus(lusor):
	"""
	Process the input to determine and initialize the genus.

	Args:
		lusor (Genus, NPC or PC): Input object.

	Returns:
		genus [list]: Genus data.
	"""
	if hasattr(lusor, "genus"):  # Assuming Lusor is a class
		genus = lusor.genus
	elif isinstance(lusor, list):  # Assuming Genus is a class or list
		genus = lusor
	else:
		raise TypeError("Input must be a list or a NPC/PC object.")

	return genus
