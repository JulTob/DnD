from enum import Enum, auto


class ConditionType(Enum):
	BLINDED = "Blinded"
	CHARMED = "Charmed"
	DEAFENED = "Deafened"
	EXHAUSTION = "Exhaustion"
	FRIGHTENED = "Frightened"
	GRAPPLED = "Grappled"
	INCAPACITATED = "Incapacitated"
	INVISIBLE = "Invisible"
	PARALYZED = "Paralyzed"
	PETRIFIED = "Petrified"
	POISONED = "Poisoned"
	PRONE = 	"Prone"
	RESTRAINED = "Restrained"
	STUNNED = 	"Stunned"
	UNCONSCIOUS = "Unconscious"

	def __str__(self):
		return self.value

	@classmethod
	def get_random(cls) -> 'DamageType':
		"""
		Returns a random DamageType.

		Returns:
			DamageType: A randomly selected DamageType Enum member.
		"""
		import random
		return random.choice(list(cls))
