"""
Structured tactical Feature contracts for NonPlayer Characters.

The generator stores resolved grants.  The Shiny app only projects those
grants as Entries and optional Chips; it performs no tactical selection.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from TagKit import Imprint
from TagKit import Pre
from TagKit import Tag

from AtlasActorLudi.CharactersKit import NonPlayer
from AtlasActorLudi.Map_of_Scores import PB


class Activation(Enum):
	"""Where a tactical Feature belongs in a creature's action economy."""

	TRAIT = "Trait"
	ACTION = "Action"
	BONUS_ACTION = "Bonus Action"
	REACTION = "Reaction"


class Tactical_Role(Enum):
	"""The battlefield purpose served by a tactical Feature."""

	OFFENSE = "Offense"
	DEFENSE = "Defense"
	CONTROL = "Control"
	MOBILITY = "Mobility"
	DISRUPTION = "Disruption"
	SUPPORT = "Support"
	COMMAND = "Command"
	SUSTAIN = "Sustain"
	UTILITY = "Utility"


@dataclass(frozen=True, slots=True)
class Provenance:
	"""Rights and review record for one catalogue entry."""

	rights_basis: str
	license_expression: str
	source_title: str
	source_version: str = ""
	source_url: str = ""
	source_locator: str = ""
	adaptation_note: str = ""


PROJECT_ORIGINAL = Provenance(
		rights_basis="project-original",
		license_expression="NOASSERTION",
		source_title="Gen Legend original tactical catalogue",
		)


@dataclass(frozen=True, slots=True)
class Chip_Spec:
	"""Optional brief sheet value contributed by a tactical Feature."""

	key: str
	label: str
	value_template: str
	icon: str = "⚙️"


@dataclass(frozen=True, slots=True)
class Chip_Grant:
	"""Resolved Chip projected by the sheet without further calculation."""

	key: str
	label: str
	value: str
	icon: str
	source_feature: str


@dataclass(frozen=True, slots=True)
class Feature_Grant:
	"""One selected and fully resolved NPC sheet Entry."""

	key: str
	name: str
	description: str
	activation: Activation
	tactical_roles: tuple[Tactical_Role, ...]
	source: str
	level: int
	contributing_tags: tuple[str, ...]
	chips: tuple[Chip_Grant, ...]
	provenance: Provenance


@dataclass(frozen=True, slots=True)
class Feature_Spec:
	"""Immutable catalogue entry resolved only after selection."""

	key: str
	title: str
	activation: Activation
	tactical_roles: tuple[Tactical_Role, ...]
	description_template: str
	affinities: tuple[str, ...] = ()
	requires_any: tuple[str, ...] = ()
	excludes_any: tuple[str, ...] = ()
	uniqueness_group: str = ""
	minimum_level: int = 1
	chips: tuple[Chip_Spec, ...] = ()
	provenance: Provenance = PROJECT_ORIGINAL

	def __post_init__(
			self,
			) -> None:
		if (
			not self.key
			or self.key.casefold() != self.key
			or " " in self.key
			):
			raise ValueError(
					f"Feature key must be stable lower snake case: {self.key!r}."
					)
		if not self.tactical_roles:
			raise ValueError(
					f"Feature {self.key!r} requires a tactical role."
					)
		if self.minimum_level < 1:
			raise ValueError(
					f"Feature {self.key!r} has an invalid minimum level."
					)

	def resolve(
			self,
			character,
			contributing_tags: tuple[str, ...],
			) -> Feature_Grant:
		"""Resolve PB and level placeholders after this spec is selected."""
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
		proficiency_bonus = PB(
				level
				)
		values = {
				"level": level,
				"pb": proficiency_bonus,
				}
		chips = tuple(
				Chip_Grant(
						key=chip.key,
						label=chip.label,
						value=chip.value_template.format(
								**values
								),
						icon=chip.icon,
						source_feature=self.key,
						)
				for chip in self.chips
				)
		return Feature_Grant(
				key=self.key,
				name=self.title,
				description=self.description_template.format(
						**values
						),
				activation=self.activation,
				tactical_roles=self.tactical_roles,
				source=self.provenance.source_title,
				level=level,
				contributing_tags=contributing_tags,
				chips=chips,
				provenance=self.provenance,
				)


class Tactical_Feature(Tag):
	"""Root Tag for selected tactical Features on NonPlayer Characters."""

	NAME = "NPC Tactical Feature"
	SPEC = None

	@Pre
	def Requires_NonPlayer(
			target,
			):
		return target in NonPlayer

	@Imprint
	def Ensure_Feature_Bags(
			target,
			):
		if getattr(
				target,
				"features",
				None,
				) is None:
			target.features = []
		if getattr(
				target,
				"npc_features",
				None,
				) is None:
			target.npc_features = []


def Build_Feature_Tag(
		spec: Feature_Spec,
		) -> type[Tactical_Feature]:
	"""Build one concrete TOP Tag around an immutable catalogue entry."""

	@Imprint
	def Carry_Resolved_Grant(
			target,
			contributing_tags=(),
			) -> None:
		Carry_Feature_Grant(
				target,
				spec.resolve(
						target,
						tuple(
								contributing_tags
								),
						),
				)

	class_name = "NPC_Feature_" + "".join(
			part.title()
			for part in spec.key.split(
					"_"
					)
			)
	return type(
			class_name,
			(
					Tactical_Feature,
					),
			{
					"NAME": spec.title,
					"SPEC": spec,
					"__doc__": f"Tactical Feature Tag for {spec.title}.",
					"__module__": __name__,
					"Carry_Resolved_Grant": Carry_Resolved_Grant,
					},
			)


def Carry_Feature_Grant(
		character,
		grant: Feature_Grant,
		) -> None:
	"""Persist one resolved grant once, preserving catalogue order."""
	if getattr(
			character,
			"features",
			None,
			) is None:
		character.features = []
	if getattr(
			character,
			"npc_features",
			None,
			) is None:
		character.npc_features = []
	if any(
			current.key == grant.key
			for current in character.npc_features
			):
		return
	character.npc_features.append(
			grant
			)
	character.features.append(
			grant
			)


__all__ = (
		"Activation",
		"Build_Feature_Tag",
		"Carry_Feature_Grant",
		"Chip_Grant",
		"Chip_Spec",
		"Feature_Grant",
		"Feature_Spec",
		"PROJECT_ORIGINAL",
		"Provenance",
		"Tactical_Feature",
		"Tactical_Role",
		)
