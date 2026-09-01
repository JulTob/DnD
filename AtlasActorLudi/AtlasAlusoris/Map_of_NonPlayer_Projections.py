"""Deterministic adapters for legacy NonPlayer sheet projections.

New TOP Features are already persisted grants.  This Map isolates the few
remaining legacy generators so Shiny can project each result repeatedly
without rerolling it or sharing RNG state between sessions.
"""

from __future__ import annotations

from collections.abc import Callable

from AtlasActorLudi.AtlasAlusoris.Map_of_NonPlayer_Features import Dice_Bag


Legacy_Renderer = Callable[[object], object]

_PROJECTION_VERSION = "legacy-sheet-2"
_MISSING = object()

_ATTRIBUTE_ACTIONS = {
		"ideal": "ResolveIdeal",
		"languages": "ResolveLanguages",
		"passive_perception": "ResolvePassivePerception",
		"plothook": "ResolvePlotHook",
		"resistances": "ResolveResistances",
		"senses": "ResolveSenses",
		"simple_attacks": "SimpleAttack",
		"special_attack": "SpecialAttack",
		"spells": "Magic",
		"story": "SetMyStory",
		"trait": "ResolveTrait",
		}


def Resolve_Legacy_Section(
		character,
		section: str,
		renderer: Legacy_Renderer,
		) -> object:
	"""Resolve and cache one transitional sheet section from its Dice Bag."""
	if not section:
		raise ValueError(
				"A legacy NonPlayer section requires a stable name."
				)
	if not callable(
			renderer
			):
		raise TypeError(
				f"Renderer for {section!r} must be callable."
				)
	cache = getattr(
			character,
			"_legacy_sheet_sections",
			None,
			)
	if cache is None:
		cache = {}
		character._legacy_sheet_sections = cache
	if section in cache:
		return cache[section]
	dice_bag = Dice_Bag(
			character,
			f"npc.sheet.{section}",
			catalog_version=_PROJECTION_VERSION,
			)
	character_dice = getattr(
			character,
			"dices",
			None,
			)
	character_dice_state = (
			character_dice.getstate()
			if character_dice is not None
			else None
			)
	try:
		character.dices = dice_bag
		if section in cache:
			return cache[section]
		result = renderer(
				character
				)
	finally:
		character.dices = character_dice
		if character_dice is not None and character_dice_state is not None:
			character_dice.setstate(
					character_dice_state
					)
	cache[section] = result
	return result


def Resolve_Legacy_Attribute(
		character,
		attribute: str,
		default: object = "-",
		) -> object:
	"""Read a Record or materialize one through its explicit Agent Action."""
	current = getattr(
			character,
			attribute,
			_MISSING,
			)
	if current is not _MISSING and not callable(
			current
			):
		return current
	action_name = _ATTRIBUTE_ACTIONS.get(
			attribute
			)
	if action_name is None:
		return default
	action = getattr(
			character,
			action_name,
			None,
			)
	if not callable(
			action
			):
		return default
	result = Resolve_Legacy_Section(
			character,
			f"attribute.{attribute}",
			lambda _: action(),
			)
	setattr(
			character,
			attribute,
			result,
			)
	return result


def _self_test(
		):
	from AtlasActorLudi.CharactersKit import Character

	character = Character(
			seed=41
			)
	original_state = character.dices.getstate()
	first = Resolve_Legacy_Section(
			character,
			"test",
			lambda target: target.Roll(
					20
					),
			)
	second = Resolve_Legacy_Section(
			character,
			"test",
			lambda target: target.Roll(
					20
					),
			)
	assert first == second
	assert character.dices.getstate() == original_state
	print(
			"OK — NonPlayer projections use isolated Character Dice Bags"
			)


__all__ = (
		"Resolve_Legacy_Attribute",
		"Resolve_Legacy_Section",
		)


if __name__ == "__main__":
	_self_test()
