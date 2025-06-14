# Compass_of_Damages.py

from enum import Enum, auto
from AtlasLudus.Map_of_Useful_Functions import select1

class DamageType(Enum):
	SLASHING = "Slashing"
	PIERCING = "Piercing"
	BLUDGEONING = "Bludgeoning"
	POISON = "Poison"
	ACID = "Acid"
	FIRE = "Fire"
	COLD = "Cold"
	RADIANT = "Radiant"
	NECROTIC = "Necrotic"
	LIGHTNING = "Lightning"
	FORCE = "Force"
	PSYCHIC = "Psychic"
	THUNDER = "Thunder"

	def __str__(self):
		"""
		Returns a string representation of the MagicDamageType value.
		"""
		return self.value

	def is_magic(self) -> bool:
		"""
		Determine if the damage type is magical.
		"""
		return self in MagicDamageType

	@classmethod
	def get_random(cls) -> 'DamageType':
		"""
		Returns a random DamageType.

		Returns:
		DamageType: A randomly selected DamageType Enum member.
		"""
		return random.choice(list(cls))

	@classmethod
	def list(cls):
		"""
		Returns a list of all DamageType members.
		"""
		return list(cls)

class MagicDamageType(Enum):
	POISON = DamageType.POISON
	ACID = DamageType.ACID
	FIRE = DamageType.FIRE
	COLD = DamageType.COLD
	RADIANT = DamageType.RADIANT
	NECROTIC = DamageType.NECROTIC
	LIGHTNING = DamageType.LIGHTNING
	FORCE = DamageType.FORCE
	PSYCHIC = DamageType.PSYCHIC
	THUNDER = DamageType.THUNDER

	def __str__(self):
		"""
		Returns a string representation of the MagicDamageType value.
		"""
		return f'{self.value}'

	@classmethod
	def get_random(cls) -> 'MagicDamageType':
		"""
		Returns a random MagicDamageType.

		Returns:
		MagicDamageType: A randomly selected MagicDamageType Enum member.
		"""
		return random.choice(list(cls))

	@classmethod
	def list(cls):
		"""
		Returns a list of all Magic DamageType members.
		"""
		return list(cls)

class PhysicalDamageType(Enum):
	SLASHING = DamageType.SLASHING
	PIERCING = DamageType.PIERCING
	BLUDGEONING = DamageType.BLUDGEONING

	def __str__(self):
		"""
		Returns a string representation of the MagicDamageType value.
		"""
		return self.value

	@property
	def value(self):
		"""
		Returns the string value of the associated DamageType.
		"""
		return self.value

	@classmethod
	def get_random(cls) -> 'PhysicalDamageType':
		"""
		Returns a random PhysicalDamageType.

		Returns:
		PhysicalDamageType: A randomly selected PhysicalDamageType Enum member.
		"""
		return random.choice(list(cls))

class NaturalDamageType(Enum):
	SLASHING = DamageType.SLASHING
	PIERCING = DamageType.PIERCING
	BLUDGEONING = 	DamageType.BLUDGEONING
	ACID = DamageType.ACID
	FIRE = DamageType.FIRE
	COLD = DamageType.COLD
	LIGHTNING = DamageType.LIGHTNING
	THUNDER = DamageType.THUNDER

	def __str__(self):
		"""
		Returns a string representation of the MagicDamageType value.
		"""
		return self.value


	@classmethod
	def get_random(cls) -> 'NaturalDamageType':
		"""
		Returns a random NaturalDamageType.

		Returns:
		NaturalDamageType: A randomly selected NaturalDamageType Enum member.
		"""
		return random.choice(list(cls))

class SupernaturalDamageType(Enum):
	RADIANT = DamageType.RADIANT
	NECROTIC = DamageType.NECROTIC
	PSYCHIC = DamageType.PSYCHIC
	FORCE = DamageType.FORCE

	def __str__(self):
		"""
		Returns a string representation of the MagicDamageType value.
		"""
		return self.value

	@classmethod
	def get_random(cls) -> 'SupernaturalDamageType':
		"""
		Returns a random SupernaturalDamageType.

		Returns:
		SupernaturalDamageType: A randomly selected SupernaturalDamageType Enum member.
		"""
		return random.choice(list(cls))

class HolyDamageType(Enum):
	FIRE = DamageType.FIRE
	RADIANT = DamageType.RADIANT
	LIGHTNING = DamageType.LIGHTNING
	THUNDER = DamageType.THUNDER

	def __str__(self):
		"""
		Returns a string representation of the MagicDamageType value.
		"""
		return self.value


	@classmethod
	def get_random(cls) -> 'HolyDamageType':
		"""
		Returns a random HolyDamageType.

		Returns:
		HolyDamageType: A randomly selected HolyDamageType Enum member.
		"""
		return random.choice(list(cls))

class UnholyDamageType(Enum):
	POISON = DamageType.POISON
	FIRE = DamageType.FIRE
	COLD = DamageType.COLD
	NECROTIC = DamageType.NECROTIC

	def __str__(self):
		"""
		Returns a string representation of the MagicDamageType value.
		"""
		return self.value

	@classmethod
	def get_random(cls) -> 'UnholyDamageType':
		"""
		Returns a random UnholyDamageType.

		Returns:
		UnholyDamageType: A randomly selected UnholyDamageType Enum member.
		"""
		return random.choice(list(cls))

class ElementalDamageType(Enum):
	FIRE =	DamageType.FIRE
	COLD = 	DamageType.COLD
	LIGHTNING = DamageType.LIGHTNING
	THUNDER = 	DamageType.THUNDER
	BLUDGEONING = 	DamageType.BLUDGEONING

	def __str__(self):
		"""
		Returns a string representation of the MagicDamageType value.
		"""
		return self.value


Magic_Damage_Types = list(MagicDamageType)

Damage_Types = list(DamageType)

def Damage():
	return str(select1(Damage_Types).value)

def MagicDamage():
	return str(select1(Magic_Damage_Types).value)

def ElementalDamage():
	return str(select1(list(ElementalDamageType)).value)
