### Alignment Utilities ###

import random

	
def Alignment(alignment: str = "") -> str:
	"""
	Generate a character alignment
	or
	pick a random one if not specified.
	Preconditions:
	-	<alignment> is an optional string.
	Postconditions:
	-	Returns a valid alignment string.

	"""

	if alignment == 'LG':
		result = "Lawful Good"
	elif alignment == 'NG':
		result = "Neutral Good"
	elif alignment == 'CG':
		result = "Chaotic Good"
	if alignment == 'LN':
		result = "Lawful Neutral"
	elif alignment == 'NN' or alignment == 'N':
		result = "True Neutral"
	elif alignment == 'CN':
		result = "Chaotic Neutral"
	if alignment == 'LE':
		result = "Lawful Evil"
	elif alignment == 'NE':
		result = "Neutral Evil"
	elif alignment == 'CE':
		result = "Chaotic Evil"
	else:
		Alignments = [
			"Lawful Good",          "Neutral Good",        "Chaotic Good",
			"Lawful Neutral",       "True Neutral",        "Chaotic Neutral",
			"Lawful Evil",          "Neutral Evil",        "Chaotic Evil",
			#"Unaligned",            ""
			]
		result = random.choice(Alignments)
	assert isinstance(result, str), "Alignment output must be a string."
	return result
