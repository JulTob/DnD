# Map_of_Conditions.py

'''...༼Cartography of the Map of Conditions༽...'''
import random
from AtlasLudus.Compass_of_Conditions import ConditionType
from AtlasLudus.Compass_of_Damages import DamageType 
from typing import List, Dict


Conditions = list(ConditionType)

damage_to_conditions: Dict[DamageType, List[ConditionType]] = {
	DamageType.SLASHING: [
		ConditionType.EXHAUSTION,
		ConditionType.INCAPACITATED,
		ConditionType.POISONED,
		ConditionType.PRONE
	],
	DamageType.PIERCING: [
		ConditionType.BLINDED,
		ConditionType.EXHAUSTION,
		ConditionType.INCAPACITATED,
		ConditionType.POISONED,
		ConditionType.GRAPPLED
	],
	DamageType.BLUDGEONING: [
		ConditionType.BLINDED,
		ConditionType.DEAFENED,
		ConditionType.EXHAUSTION,
		ConditionType.INCAPACITATED,
		ConditionType.PRONE,
		ConditionType.STUNNED,
		ConditionType.UNCONSCIOUS,
		ConditionType.GRAPPLED,
		ConditionType.RESTRAINED
	],
	DamageType.POISON: [
		ConditionType.BLINDED,
		ConditionType.CHARMED,
		ConditionType.EXHAUSTION,
		ConditionType.FRIGHTENED,
		ConditionType.INCAPACITATED,
		ConditionType.PARALYZED,
		ConditionType.PETRIFIED,
		ConditionType.POISONED,
		ConditionType.RESTRAINED,
		ConditionType.UNCONSCIOUS
	],
	DamageType.ACID: [
		ConditionType.BLINDED,
		ConditionType.EXHAUSTION,
		ConditionType.INCAPACITATED,
		ConditionType.PARALYZED,
		ConditionType.PETRIFIED,
		ConditionType.POISONED,
		ConditionType.RESTRAINED,
		ConditionType.UNCONSCIOUS
	],
	DamageType.FIRE: [
		ConditionType.BLINDED,
		ConditionType.CHARMED,
		ConditionType.INCAPACITATED,
		ConditionType.PARALYZED,
		ConditionType.STUNNED,
		ConditionType.UNCONSCIOUS
	],
	DamageType.COLD: [
		ConditionType.EXHAUSTION,
		ConditionType.INCAPACITATED,
		ConditionType.PARALYZED,
		ConditionType.PETRIFIED,
		ConditionType.RESTRAINED,
		ConditionType.GRAPPLED
	],
	DamageType.RADIANT: [
		ConditionType.BLINDED,
		ConditionType.CHARMED,
		ConditionType.DEAFENED,
		ConditionType.FRIGHTENED,
		ConditionType.INCAPACITATED,
		ConditionType.PARALYZED,
		ConditionType.PRONE,
		ConditionType.STUNNED,
		ConditionType.UNCONSCIOUS
	],
	DamageType.NECROTIC: [
		ConditionType.EXHAUSTION,
		ConditionType.FRIGHTENED,
		ConditionType.INCAPACITATED,
		ConditionType.PARALYZED,
		ConditionType.POISONED,
		ConditionType.PRONE,
		ConditionType.RESTRAINED,
		ConditionType.STUNNED,
		ConditionType.UNCONSCIOUS
	],
	DamageType.LIGHTNING: [
		ConditionType.BLINDED,
		ConditionType.CHARMED,
		ConditionType.DEAFENED,
		ConditionType.EXHAUSTION,
		ConditionType.FRIGHTENED,
		ConditionType.GRAPPLED,
		ConditionType.INCAPACITATED,
		ConditionType.PARALYZED,
		ConditionType.PETRIFIED,
		ConditionType.PRONE,
		ConditionType.RESTRAINED,
		ConditionType.STUNNED,
		ConditionType.UNCONSCIOUS
	],
	DamageType.FORCE: [
		ConditionType.BLINDED,
		ConditionType.DEAFENED,
		ConditionType.EXHAUSTION,
		ConditionType.INCAPACITATED,
		ConditionType.PRONE,
		ConditionType.STUNNED,
		ConditionType.UNCONSCIOUS,
		ConditionType.GRAPPLED
	],
	DamageType.PSYCHIC: [
		ConditionType.BLINDED,
		ConditionType.CHARMED,
		ConditionType.DEAFENED,
		ConditionType.EXHAUSTION,
		ConditionType.FRIGHTENED,
		ConditionType.INCAPACITATED,
		ConditionType.PARALYZED,
		ConditionType.PETRIFIED,
		ConditionType.POISONED,
		ConditionType.PRONE,
		ConditionType.RESTRAINED,
		ConditionType.STUNNED,
		ConditionType.UNCONSCIOUS
	],
	DamageType.THUNDER: [
		ConditionType.BLINDED,
		ConditionType.DEAFENED,
		ConditionType.EXHAUSTION,
		ConditionType.INCAPACITATED,
		ConditionType.PARALYZED,
		ConditionType.PRONE,
		ConditionType.STUNNED
	],
	}

# Mapping from ConditionType to possible Saving Throws
condition_to_saving_throws: Dict[ConditionType, List[str]] = {
	ConditionType.BLINDED: ["CON", "INT", "WIS", "CHA"],
	ConditionType.CHARMED: ["CHA", "WIS"],
	ConditionType.DEAFENED: ["STR", "CON", "WIS"],
	ConditionType.EXHAUSTION: ["STR", "CON", "CHA"],
	ConditionType.FRIGHTENED: ["CON", "INT", "WIS", "CHA"],
	ConditionType.GRAPPLED: ["STR", "DEX"],
	ConditionType.INCAPACITATED: ["STR", "CON", "WIS", "CHA"],
	ConditionType.INVISIBLE: ["CON", "INT", "WIS", "CHA"],
	ConditionType.PARALYZED: ["STR", "CON", "WIS", "CHA"],
	ConditionType.PETRIFIED: ["STR", "CON", "INT", "WIS", "CHA"],
	ConditionType.POISONED: ["CON", "WIS"],
	ConditionType.PRONE: ["STR", "DEX", "CON"],
	ConditionType.RESTRAINED: ["STR", "DEX", "CON"],
	ConditionType.STUNNED: ["CON", "INT", "WIS", "CHA"],
	ConditionType.UNCONSCIOUS: ["CON", "INT", "WIS", "CHA"],
}

condition_to_recovery: Dict[ConditionType, List[str]] = {
	ConditionType.UNCONSCIOUS: ["CON", "INT", "WIS", "CHA"],
	ConditionType.STUNNED: ["CON", "INT", "WIS", "CHA"],
	ConditionType.RESTRAINED: ["STR", "DEX", "CON"],
	ConditionType.POISONED: ["CON", "WIS"],
	ConditionType.PRONE: ["STR", "DEX", "CON"],
	ConditionType.PETRIFIED: ["STR", "CON", "INT", "WIS", "CHA"],
	ConditionType.PARALYZED: ["STR", "CON", "WIS", "CHA"],
	ConditionType.INVISIBLE: ["CON", "INT", "WIS", "CHA"],
	ConditionType.INCAPACITATED: ["STR", "CON", "WIS", "CHA"],
	ConditionType.GRAPPLED: ["STR", "DEX"],
	ConditionType.BLINDED: ["CON", "INT", "WIS", "CHA"],
	ConditionType.FRIGHTENED: ["CON", "INT", "WIS", "CHA"],
	ConditionType.EXHAUSTION: ["STR", "CON", "CHA"],
	ConditionType.DEAFENED: ["STR", "CON", "WIS"],
	ConditionType.CHARMED: ["CHA", "WIS"],
}


def Condition(dmg: DamageType) -> ConditionType:
	"""
	Returns a random Condition based on the given DamageType.

	Args:
		dmg (DamageType): The type of damage inflicted.

	Returns:
		ConditionType: A randomly selected Condition Enum member.

	Raises:
		TypeError: If input is not DamageType or output is not ConditionType.
	"""
	conditions = damage_to_conditions.get(dmg, [])
	if conditions:
		return random.choice(conditions)
	else:
		# Fallback to a random condition if no specific conditions are mapped
		return random.choice(list(ConditionType))


def SavingThrow(cond: ConditionType) -> str:
	"""
	Returns a random Saving Throw based on the given ConditionType.

	Args:
		cond [ConditionType]: The type of damage inflicted.

	Returns:
		[str]: A randomly selected Saving Throw string.

	Raises:
		TypeError: If input is not DamageType or output is not str.
	"""
	saving_throws = condition_to_saving_throws.get(cond, ["DEX"])
	return random.choice(saving_throws)





def Recovery(cond: ConditionType) -> str:
	"""
	Returns a random Recovery Method based on the given Condition.

	Args:
		cond [ConditionType]: The condition inflicted.

	Returns:
		str: A randomly selected Recovery Method string.

	Raises:
		TypeError: If input is not ConditionType or output is not str.
	"""
	recovery_options = condition_to_recovery_methods.get(condition, ["CON"])
	return random.choice(recovery_options)
