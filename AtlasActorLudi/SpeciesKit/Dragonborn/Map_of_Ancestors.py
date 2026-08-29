"""
The Draconic Ancestors, and what each one breathes.

Ten dragons, five damage types.  The table is the whole of the rule: an
ancestor is chosen, and every other draconic trait reads its damage type from
here.  Nothing else about the dragon is mechanical.
"""

from __future__ import annotations


# Ancestor to damage type, exactly as the Draconic Ancestors table gives it.
DRACONIC_ANCESTORS = {
	"Black": "Acid",
	"Blue": "Lightning",
	"Brass": "Fire",
	"Bronze": "Lightning",
	"Copper": "Acid",
	"Gold": "Fire",
	"Green": "Poison",
	"Red": "Fire",
	"Silver": "Cold",
	"White": "Cold",
	}


def draconic_ancestor(
		char,
		) -> tuple[str, str]:
	"""
	This Character's ancestor and its damage type, drawn once and kept.

	The bag is named and level-free, so a Dragonborn does not change colour on
	levelling up any more than a familiar changes species.
	"""
	standing = getattr(
		char,
		"draconic_ancestor",
		None,
		)

	if standing:
		return (
			standing,
			DRACONIC_ANCESTORS[
				standing
				],
			)

	dice = char.Dice_Bag(
		"dragonborn.ancestor",
		version="1",
		namespace="GenLegendActor",
		)
	ancestor = char.Pick(
		list(
			DRACONIC_ANCESTORS
			),
		dice=dice,
		)
	char.draconic_ancestor = ancestor
	char.draconic_damage = DRACONIC_ANCESTORS[
		ancestor
		]

	return (
		ancestor,
		char.draconic_damage,
		)


__all__ = (
	"DRACONIC_ANCESTORS",
	"draconic_ancestor",
	)
