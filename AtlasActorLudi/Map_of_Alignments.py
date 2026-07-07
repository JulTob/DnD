### Alignment Utilities ###

import app.random as random
from enum import Enum

class Alignments(Enum):
	CHAOTIC_EVIL = "Chaotic Evil"
	NEUTRAL_EVIL = "True Evil"
	LAWFUL_EVIL = "Legal Evil"
	CHAOTIC_NEUTRAL = "True Chaotic"
	TRUE_NEUTRAL = "True Neutral"
	LAWFUL_NEUTRAL = "True Legal"
	CHAOTIC_GOOD = "Chaotic Good"
	NEUTRAL_GOOD = "True Good"
	LAWFUL_GOOD = "Legal Good"

	def __str__(self):
		return self.value

	@classmethod
	def random(cls, seed=None):
		return random.choice(list(cls))

	def __call__(self):
		return

def Alignment():
	# ✅ Factory function
	return Alignments.random()
