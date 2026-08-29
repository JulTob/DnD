"""
Map_of_Gear_Proficiency — what a Character's training means for their gear.

Per Convention (Curia/Canon/Conventions.md): a ``Map_of_X`` is "data plus the
route or algorithm that resolves a task." This one does not own a Tag family —
it ROUTES between two that already have their own canonical Kit:
``AtlasLusoris.GuildKit``'s training Tags (``HeavilyArmored``, ``MartialArms``,
``FinesseArms``, …) on one side, and ``AtlasInventarium.ItemKit``'s gear Tags
(``Weapon``, ``Melee``, ``Ranged``, …) on the other.

Split out of ``GearKit`` (2026-07-31, Julio's request) because "who may use
what" is a different question from "what does this Character end up with" —
independent axes per ``Canon/TagKit-Doctrine.md``, even though one answers the
other.
"""

from __future__ import annotations

from AtlasInventarium.ItemKit import Item
from AtlasInventarium.Ledger_of_Weapons import (
		MARTIAL_MELEE,
		MARTIAL_RANGED,
		SIMPLE_MELEE,
		SIMPLE_RANGED,
		)


def _modifier(
		score,
		) -> int:
	return (
		int(
				score
				) - 10
		) // 2


def armour_allowance(
		char,
		) -> tuple[str, ...]:
	"""Which armour kinds this Character was trained to wear."""
	from AtlasLusoris.GuildKit import (
			HeavilyArmored,
			LightlyArmored,
			ModeratelyArmored,
			)

	if char in HeavilyArmored:
		return (
				"Light",
				"Medium",
				"Heavy",
				)
	if char in ModeratelyArmored:
		return (
				"Light",
				"Medium",
				)
	if char in LightlyArmored:
		return (
				"Light",
				)
	return ()


def has_unarmoured_defence(
		char,
		) -> bool:
	"""True when the Character's AC comes from a body-discipline formula."""
	skills = getattr(
			char,
			"skills",
			None,
			)
	if skills is None:
		return False
	return bool(
			skills.Unarmed_Monk.is_proficient()
			or skills.Unarmed_Barb.is_proficient()
			)


def unarmoured_formula(
		char,
		) -> int:
	"""
	The Character's own no-armour AC.

	Monk adds Wisdom, Barbarian adds Constitution; everyone else is the plain
	10 + Dexterity. Returned as a number so ``armour_class`` can simply take
	the better of it and any worn armour — no special-casing downstream.
	"""
	scores = getattr(
			char,
			"AS",
			None,
			)
	dexterity = _modifier(
			getattr(
					scores,
					"DEX",
					10,
					)
			)
	base = 10 + dexterity

	skills = getattr(
			char,
			"skills",
			None,
			)
	if skills is None:
		return base

	if skills.Unarmed_Monk.is_proficient():
		base = max(
				base,
				10 + dexterity + _modifier(
						getattr(
								scores,
								"WIS",
								10,
								)
						),
				)
	if skills.Unarmed_Barb.is_proficient():
		base = max(
				base,
				10 + dexterity + _modifier(
						getattr(
								scores,
								"CON",
								10,
								)
						),
				)
	return base


def may_use_shield(
		char,
		) -> bool:
	"""
	Shield training, tempered by whether a shield suits the build.

	A Monk's Unarmored Defence is void while holding a shield, so the
	generator does not hand one over; a Barbarian's is not, so it does.
	"""
	from AtlasLusoris.GuildKit import HeavilyArmored, ModeratelyArmored

	skills = getattr(
			char,
			"skills",
			None,
			)
	if skills is not None and skills.Unarmed_Monk.is_proficient():
		return False

	return (
		char in HeavilyArmored
		or char in ModeratelyArmored
		)


def weapon_pool(
		char,
		) -> tuple[Item, ...]:
	"""
	Every weapon this Character may wield, from their Guild's arms training.

	Firearms are excluded everywhere: they are DMG-optional and no 2024 Guild
	trains them by default.
	"""
	from AtlasLusoris.GuildKit import (
			FinesseArms,
			LightMartialArms,
			MartialArms,
			)

	simple = SIMPLE_MELEE + SIMPLE_RANGED
	martial = MARTIAL_MELEE + MARTIAL_RANGED

	if char in MartialArms:
		return simple + martial

	if char in FinesseArms:
		return simple + tuple(
				weapon
				for weapon in martial
				if "Finesse" in weapon.properties
				or "Light" in weapon.properties
				)

	if char in LightMartialArms:
		return simple + tuple(
				weapon
				for weapon in martial
				if "Light" in weapon.properties
				)

	return simple


def trained_for(
		char,
		weapon: Item,
		) -> bool:
	"""
	May this Character wield THIS weapon?

	``weapon_pool`` answers the shopping question — what is there to buy —
	and is necessarily a catalogue. This answers the proficiency question,
	and does it by Tag, so anything built with ``Build_Weapon`` gets a
	truthful answer whether or not it lives in ``Ledger_of_Weapons``.
	(Implements in ``Ledger_of_Wonders`` are the case that forced the split:
	they are Simple weapons, and a Simple-trained caster is trained in them.)
	"""
	from AtlasInventarium.ItemKit import Firearm, Simple

	if weapon in Firearm:
		return False
	# Simple arms are every Guild's floor — ``weapon_pool`` returns them
	# unconditionally, so this agrees with it by construction.
	if weapon in Simple:
		return True
	# Martial and anything uncategorised must earn it from the catalogue,
	# which is where the Guild's actual training is expressed.
	return any(
			record.name == weapon.name
			for record in weapon_pool(
					char
					)
			)


__all__ = (
		"armour_allowance",
		"has_unarmoured_defence",
		"may_use_shield",
		"trained_for",
		"unarmoured_formula",
		"weapon_pool",
		)


def _self_test():
	class Scores:
		DEX = 14
		CON = 16
		WIS = 12

	class Skill:
		def __init__(
				self,
				proficient=False,
				):
			self._p = proficient

		def is_proficient(
				self,
				):
			return self._p

	class Skills:
		def __init__(
				self,
				*,
				unarmed_monk=False,
				unarmed_barb=False,
				):
			self.Unarmed_Monk = Skill(
					unarmed_monk
					)
			self.Unarmed_Barb = Skill(
					unarmed_barb
					)

	class Dummy:
		def __init__(
				self,
				**kw,
				):
			self.AS = Scores()
			self.skills = Skills(
					**kw
					)

	# --- unarmoured_formula: everyone else is plain 10 + Dex --------------
	plain = Dummy()
	assert unarmoured_formula(
			plain
			) == 12, unarmoured_formula(
			plain
			)

	# --- Monk adds Wisdom, Barbarian adds Constitution ---------------------
	monk = Dummy(
			unarmed_monk=True,
			)
	assert unarmoured_formula(
			monk
			) == 13, unarmoured_formula(
			monk
			)
	assert has_unarmoured_defence(
			monk
			)
	assert may_use_shield(
			monk
			) is False, "a shield voids Monk Unarmored Defence"

	barb = Dummy(
			unarmed_barb=True,
			)
	assert unarmoured_formula(
			barb
			) == 15, unarmoured_formula(
			barb
			)
	assert has_unarmoured_defence(
			barb
			)

	# --- untrained Character: no armour allowance, no weapons beyond none --
	naked = Dummy()
	assert armour_allowance(
			naked
			) == ()
	assert weapon_pool(
			naked
			) == SIMPLE_MELEE + SIMPLE_RANGED, (
			"untrained defaults to the Simple pool"
			)

	print(
			"OK — Map_of_Gear_Proficiency self-test "
			"(armour allowance, weapon pool, Unarmored Defence formulas)"
			)


if __name__ == "__main__":
	_self_test()
