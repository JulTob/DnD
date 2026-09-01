"""Deterministically select and persist an NPC tactical feature loadout."""

from __future__ import annotations

from collections import Counter
from collections.abc import Iterable as Iterable_Collection
from collections.abc import Mapping
from random import Random
from re import split
from typing import Iterable

from TagKit import Tags

from AtlasActorLudi.CharactersKit import NonPlayer
from AtlasActorLudi.Map_of_Scores import PB
from AtlasActorLudi.AtlasAlusoris.FeaturesKit import Activation
from AtlasActorLudi.AtlasAlusoris.FeaturesKit import Feature_Grant
from AtlasActorLudi.AtlasAlusoris.FeaturesKit import Feature_Spec
from AtlasActorLudi.AtlasAlusoris.Lodge_of_NonPlayer_Features import CATALOG_VERSION
from AtlasActorLudi.AtlasAlusoris.Lodge_of_NonPlayer_Features import FEATURE_SPECS
from AtlasActorLudi.AtlasAlusoris.Lodge_of_NonPlayer_Features import FEATURE_TAGS


_SPELLCASTING_IDENTITIES = frozenset(
		{
				"bard",
				"cleric",
				"druid",
				"mage",
				"paladin",
				"priest",
				"ranger",
				"shaman",
				"sorcerer",
				"warlock",
				"witch",
				"wizard",
				}
		)

_POWER_SOURCE_IDENTITIES = {
		"arcane": frozenset(
				{
						"bard",
						"mage",
						"sorcerer",
						"wizard",
						}
				),
		"divine": frozenset(
				{
						"cleric",
						"paladin",
						"priest",
						}
				),
		"occult": frozenset(
				{
						"cultist",
						"warlock",
						"witch",
						}
				),
		"primal": frozenset(
				{
						"druid",
						"ranger",
						"shaman",
						}
				),
		}

_SPELL_BAGS = (
		"known_spells",
		"prepared_spells",
		"spell_list",
		)


def Dice_Bag(
		character,
		purpose: str,
		*,
		catalog_version: str = "npc-tactics-2",
		) -> Random:
	"""Open the Character Dice Bag for one versioned NPC purpose."""
	return character.Dice_Bag(
			purpose,
			version=catalog_version,
			namespace="GenLegendNPC",
			)


def Feature_Count(
		character,
		) -> int:
	"""Use level-based PB with an explicit readable three-to-five clamp."""
	level = max(
			1,
			int(
					getattr(
							character,
							"level",
							1,
							)
					),
			)
	return max(
			3,
			min(
					5,
					PB(
							level
							),
					),
			)


def _tag_names(
		character,
		) -> Iterable[str]:
	"""Yield each active Tag's explicit domain name once."""
	seen = set()
	for leaf in Tags(
			character
			):
		for tag in leaf.Form():
			if tag in seen:
				continue
			seen.add(
					tag
					)
			name = getattr(
					tag,
					"NAME",
					tag.__name__,
					)
			if isinstance(
					name,
					str,
					) and name:
				yield name


def _spell_records(
		value,
		) -> Iterable[object]:
	if value is None:
		return
	if isinstance(
			value,
			Mapping,
			):
		for nested in value.values():
			yield from _spell_records(
					nested
					)
		return
	if isinstance(
			value,
			Iterable_Collection,
			) and not isinstance(
			value,
			(
					str,
					bytes,
					),
			):
		for nested in value:
			yield from _spell_records(
					nested
					)
		return
	yield value


def _structured_spell_values(
		character,
		) -> Iterable[str]:
	fields = getattr(
			character,
			"__dict__",
			{},
			)
	for bag_name in _SPELL_BAGS:
		for spell in _spell_records(
				fields.get(
						bag_name
						)
				):
			if isinstance(
					spell,
					str,
					):
				yield spell
				continue
			for attribute in (
					"name",
					"school",
					"damage_type",
					"tradition",
					):
				value = getattr(
						spell,
						attribute,
						None,
						)
				if isinstance(
						value,
						str,
						):
					yield value
			yield from _tag_names(
					spell
					)


def Semantic_Keys(
		character,
		) -> tuple[str, ...]:
	"""Collect canonical Tag names and compatibility identity fields."""
	values = list(
			_tag_names(
					character
					)
			)
	values.extend(
			_structured_spell_values(
					character
					)
			)
	for attribute in (
			"race",
			"species",
			"subrace",
			"char_class",
			"background",
			):
		value = getattr(
				character,
				attribute,
				None,
				)
		if isinstance(
				value,
				str,
				):
			values.append(
					value
					)
	normalized = set()
	for value in values:
		if not value:
			continue
		canonical = value.strip().casefold()
		normalized.add(
				canonical
				)
		normalized.update(
				token
				for token in split(
						"[^a-z0-9]+",
						canonical,
						)
				if token
				)
	if normalized.intersection(
			_SPELLCASTING_IDENTITIES
			):
		normalized.update(
				{
						"magic",
						"spellcaster",
						}
				)
	for power_source, identities in _POWER_SOURCE_IDENTITIES.items():
		matches = normalized.intersection(
				identities
				)
		if not matches:
			continue
		normalized.add(
				power_source
				)
		normalized.add(
				f"{power_source} magic"
				)
		for identity in matches:
			normalized.add(
					f"{identity} spell list"
					)
	return tuple(
			sorted(
					normalized
					)
			)


def _normalized(
		values: Iterable[str],
		) -> frozenset[str]:
	return frozenset(
			value.casefold()
			for value in values
			)


def _eligible(
		spec: Feature_Spec,
		*,
		level: int,
		semantic_keys: frozenset[str],
		) -> bool:
	required = _normalized(
			spec.requires_any
			)
	excluded = _normalized(
			spec.excludes_any
			)
	if spec.minimum_level > level:
		return False
	if required and not required.intersection(
			semantic_keys
			):
		return False
	return not excluded.intersection(
			semantic_keys
			)


def _affinity_matches(
		spec: Feature_Spec,
		semantic_keys: frozenset[str],
		) -> tuple[str, ...]:
	return tuple(
			sorted(
					_normalized(
							spec.affinities
							).intersection(
							semantic_keys
							)
					)
			)


def _weight(
		spec: Feature_Spec,
		semantic_keys: frozenset[str],
		) -> int:
	return 1 + 8 * len(
			_affinity_matches(
					spec,
					semantic_keys,
					)
			)


def _weighted_pick(
		candidates: list[Feature_Spec],
		*,
		semantic_keys: frozenset[str],
		dice: Random,
		) -> Feature_Spec:
	return dice.choices(
			candidates,
			weights=[
					_weight(
							spec,
							semantic_keys,
							)
					for spec in candidates
					],
			k=1,
			)[0]


def _available(
		candidates: list[Feature_Spec],
		selected: list[Feature_Spec],
		) -> list[Feature_Spec]:
	selected_keys = {
			spec.key
			for spec in selected
			}
	uniqueness_groups = {
			spec.uniqueness_group
			for spec in selected
			if spec.uniqueness_group
			}
	return [
			spec
			for spec in candidates
			if spec.key not in selected_keys
			and (
					not spec.uniqueness_group
					or spec.uniqueness_group not in uniqueness_groups
					)
			]


def Select_Feature_Specs(
		character,
		catalogue: Iterable[Feature_Spec] = FEATURE_SPECS,
		) -> tuple[Feature_Spec, ...]:
	"""Select unique, varied specs without consuming any global RNG."""
	semantic_keys = frozenset(
			Semantic_Keys(
					character
					)
			)
	level = max(
			1,
			int(
					getattr(
							character,
							"level",
							1,
							)
					),
			)
	candidates = sorted(
			(
					spec
					for spec in catalogue
					if _eligible(
							spec,
							level=level,
							semantic_keys=semantic_keys,
							)
					),
			key=lambda spec: spec.key,
			)
	target = min(
			Feature_Count(
					character
					),
			len(
					candidates
					),
			)
	if target == 0:
		return ()
	dice = Dice_Bag(
			character,
			"npc.features",
			)
	selected = []
	influenced = [
			spec
			for spec in candidates
			if _affinity_matches(
					spec,
					semantic_keys,
					)
			]
	if influenced:
		selected.append(
				_weighted_pick(
						influenced,
						semantic_keys=semantic_keys,
						dice=dice,
						)
				)
	if len(selected) < target and not any(
			spec.activation == Activation.ACTION
			for spec in selected
			):
		action_candidates = [
				spec
				for spec in _available(
						candidates,
						selected,
						)
				if spec.activation == Activation.ACTION
				]
		if action_candidates:
			selected.append(
					_weighted_pick(
							action_candidates,
							semantic_keys=semantic_keys,
							dice=dice,
							)
					)
	while len(selected) < target:
		remaining = _available(
				candidates,
				selected,
				)
		if not remaining:
			break
		roles = {
				role
				for spec in selected
				for role in spec.tactical_roles
				}
		varied = [
				spec
				for spec in remaining
				if any(
						role not in roles
						for role in spec.tactical_roles
						)
				]
		activation_counts = Counter(
				spec.activation
				for spec in selected
				)
		lightly_used = [
				spec
				for spec in (
						varied or remaining
						)
				if activation_counts[spec.activation] < 2
				]
		pool = lightly_used or varied or remaining
		selected.append(
				_weighted_pick(
						pool,
						semantic_keys=semantic_keys,
						dice=dice,
						)
				)
	return tuple(
			selected
			)


def Apply_NonPlayer_Features(
		character,
		) -> tuple[Feature_Grant, ...]:
	"""Select once, apply semantic Feature Tags, and freeze resolved grants."""
	if character not in NonPlayer:
		raise ValueError(
				"NPC tactical Features require the NonPlayer role."
				)
	existing = getattr(
			character,
			"npc_features",
			None,
			)
	if existing:
		return tuple(
				existing
				)
	character.npc_features = []
	semantic_keys = frozenset(
			Semantic_Keys(
					character
					)
			)
	for spec in Select_Feature_Specs(
			character
			):
		contributing_tags = _affinity_matches(
				spec,
				semantic_keys,
				)
		tag = FEATURE_TAGS[spec.key]
		if character not in tag:
			tag(
					character,
					contributing_tags=contributing_tags,
					)
	character.npc_features = tuple(
			character.npc_features
			)
	character.npc_feature_catalog_version = CATALOG_VERSION
	return character.npc_features


__all__ = (
		"Apply_NonPlayer_Features",
		"Feature_Count",
		"Dice_Bag",
		"Select_Feature_Specs",
		"Semantic_Keys",
		)
