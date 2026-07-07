# Compass_of_Damages.py

from enum import Enum
from Compass_of_Damages import *

import random
from Compass_of_Damages import DamageType, MagicDamageType

def get_random_damage_type() -> DamageType:
    """
    Returns a random DamageType.

    Returns:
        DamageType: A randomly selected DamageType Enum member.
    """
    return random.choice(list(DamageType))

def get_random_magic_damage_type() -> MagicDamageType:
    """
    Returns a random MagicDamageType.

    Returns:
        MagicDamageType: A randomly selected MagicDamageType Enum member.
    """
    return random.choice(list(MagicDamageType))

def get_random_physical_damage_type() -> PhysicalDamageType:
    """
    Returns a random PhysicalDamageType.

    Returns:
        PhysicalDamageType: A randomly selected PhysicalDamageType Enum member.
    """
    return random.choice(list(PhysicalDamageType))

def get_random_natural_damage_type() -> NaturalDamageType:
    """
    Returns a random NaturalDamageType.

    Returns:
        NaturalDamageType: A randomly selected NaturalDamageType Enum member.
    """
    return random.choice(list(NaturalDamageType))

def get_random_supernatural_damage_type() -> SupernaturalDamageType:
    """
    Returns a random SupernaturalDamageType.

    Returns:
        SupernaturalDamageType: A randomly selected SupernaturalDamageType Enum member.
    """
    return random.choice(list(SupernaturalDamageType))

def get_random_holy_damage_type() -> HolyDamageType:
    """
    Returns a random SupernaturalDamageType.

    Returns:
        SupernaturalDamageType: A randomly selected SupernaturalDamageType Enum member.
    """
    return random.choice(list(HolyDamageType))

def get_random_unholy_damage_type() -> UnholyDamageType:
    """
    Returns a random SupernaturalDamageType.

    Returns:
        SupernaturalDamageType: A randomly selected SupernaturalDamageType Enum member.
    """
    return random.choice(list(UnholyDamageType))
