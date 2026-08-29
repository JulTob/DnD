"""
ProficiencyKit

The Character-owned relation between capabilities and their sources.

Skills and Tools are typed definitions. Feature Tags keep semantic identity.
This Kit records what each Feature granted without turning every proficiency
into another Tag or maintaining parallel writable lists.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum
from weakref import ReferenceType, ref


@dataclass(
		frozen=True,
		slots=True,
		)
class Capability_Definition:
	"""One canonical Skill or Tool that a Character may learn."""

	key: str
	name: str
	legacy_attribute: str

	def __post_init__(
			definition,
			) -> None:
		if not definition.key.strip():
			raise ValueError(
				"A capability requires a stable key."
				)

		if not definition.name.strip():
			raise ValueError(
				"A capability requires a display name."
				)


class Training_Rank(IntEnum):
	"""The effective rules rank of one capability."""

	PROFICIENT = 1
	EXPERTISE = 2


@dataclass(
		frozen=True,
		slots=True,
		)
class Training_Grant:
	"""One resolved capability and the rank a source granted."""

	capability: Capability_Definition
	rank: Training_Rank = Training_Rank.PROFICIENT

	def __post_init__(
			training_grant,
			) -> None:
		if not isinstance(
				training_grant.capability,
				Capability_Definition,
				):
			raise TypeError(
				"Training grants require a Capability_Definition."
				)

		if not isinstance(
				training_grant.rank,
				Training_Rank,
				):
			raise TypeError(
				"Training grants require a Training_Rank."
				)


@dataclass(
		frozen=True,
		slots=True,
		)
class Provenance:
	"""Where one immutable training batch came from."""

	source: str
	locator: str = ""
	edition: str = "2024"

	def __post_init__(
			provenance,
			) -> None:
		if not provenance.source.strip():
			raise ValueError(
				"Training provenance requires a source."
				)


@dataclass(
		frozen=True,
		slots=True,
		)
class Training_Batch:
	"""One atomic Feature acquisition and all capability gains it resolved."""

	grant_id: str
	feature: type
	grants: tuple[Training_Grant, ...]
	provenance: Provenance

	def __post_init__(
			batch,
			) -> None:
		object.__setattr__(
			batch,
			"grants",
			tuple(
				batch.grants
				),
			)

		if not batch.grant_id.strip():
			raise ValueError(
				"A training batch requires a stable grant ID."
				)

		if not isinstance(
				batch.feature,
				type,
				):
			raise TypeError(
				"A training batch requires its Feature Tag."
				)

		if not batch.grants:
			raise ValueError(
				"A training batch must grant at least one capability."
				)

		capabilities = tuple(
			grant.capability
			for grant in batch.grants
			)

		if len(set(capabilities)) != len(capabilities):
			raise ValueError(
				"A training batch cannot repeat one capability."
				)


@dataclass(
		frozen=True,
		slots=True,
		)
class Training_Record:
	"""The sole writable history of Feature-granted Character training."""

	gains: tuple[Training_Batch, ...] = ()


@dataclass(
		frozen=True,
		slots=True,
		)
class Feature_Training_Record:
	"""A Tag-owned, read-only view over one Feature's training batches."""

	character: ReferenceType[object]
	feature: type

	@property
	def gains(
			record,
			) -> tuple[Training_Batch, ...]:
		character = record.character()

		if character is None:
			return ()

		training = getattr(
			character,
			"training",
			Training_Record(),
			)

		return tuple(
			batch
			for batch in training.gains
			if batch.feature is record.feature
			)

	@property
	def grants(
			record,
			) -> tuple[Training_Grant, ...]:
		return tuple(
			grant
			for batch in record.gains
			for grant in batch.grants
			)


def New_Feature_Training_Record(
		character,
		feature: type,
		) -> Feature_Training_Record:
	"""Build the read-only Record contributed by one Feature Tag."""
	return Feature_Training_Record(
		character=ref(
			character
			),
		feature=feature,
		)


def Ensure_Training_Record(
		character,
		) -> Training_Record:
	"""Return a Character's ledger, creating it for pre-migration Characters."""
	training = getattr(
		character,
		"training",
		None,
		)

	if training is None:
		training = Training_Record()
		character.training = training

	if not isinstance(
			training,
			Training_Record,
			):
		raise TypeError(
			"character.training must be a Training_Record."
			)

	return training


def Add_Training_Gain(
		record: Training_Record,
		gain: Training_Batch,
		) -> Training_Record:
	"""Return the immutable ledger with one validated gain appended."""
	if not isinstance(
			record,
			Training_Record,
			):
		raise TypeError(
			"Add_Training_Gain requires a Training_Record."
			)

	if not isinstance(
			gain,
			Training_Batch,
			):
		raise TypeError(
			"Add_Training_Gain requires a Training_Batch."
			)

	for existing in record.gains:
		if existing.grant_id != gain.grant_id:
			continue

		if existing == gain:
			return record

		raise ValueError(
			"Training grant ID conflict: "
			f"{gain.grant_id!r} already identifies another gain."
			)

	return Training_Record(
		gains=(
			*record.gains,
			gain,
			),
		)


def Find_Training_Gains(
		character,
		capability: Capability_Definition,
		) -> tuple[Training_Batch, ...]:
	"""Find every recorded source that granted one capability."""
	training = Ensure_Training_Record(
		character
		)

	return tuple(
		batch
		for batch in training.gains
		if any(
			grant.capability == capability
			for grant in batch.grants
			)
		)


def _Legacy_Training_Rank(
		character,
		capability: Capability_Definition,
		) -> Training_Rank | None:
	"""Read the old mutable sheet while its remaining producers migrate."""
	if capability.legacy_attribute != capability.key:
		return None

	skills = getattr(
		character,
		"skills",
		None,
		)
	legacy = getattr(
		skills,
		capability.legacy_attribute,
		None,
		) if skills is not None else None
	level = int(
		getattr(
			legacy,
			"proficiency_level",
			0,
			) or 0
		)

	if level >= Training_Rank.EXPERTISE:
		return Training_Rank.EXPERTISE

	if level >= Training_Rank.PROFICIENT:
		return Training_Rank.PROFICIENT

	return None


def Find_Training_Rank(
		character,
		capability: Capability_Definition,
		) -> Training_Rank | None:
	"""Find the effective rank, including the temporary legacy projection."""
	ranks = [
		grant.rank
		for batch in Ensure_Training_Record(
			character
			).gains
		for grant in batch.grants
		if grant.capability == capability
		]
	legacy = _Legacy_Training_Rank(
		character,
		capability,
		)

	if legacy is not None:
		ranks.append(legacy)

	return max(
		ranks,
		default=None,
		)


def Is_Trained(
		character,
		capability: Capability_Definition,
		) -> bool:
	"""Canonical query for whether a Character knows one capability."""
	return Find_Training_Rank(
		character,
		capability,
		) is not None


def Apply_Training_Record(
		character,
		) -> None:
	"""Project the immutable ledger onto the old sheet during migration."""
	skills = getattr(
		character,
		"skills",
		None,
		)

	if skills is None:
		return

	best: dict[Capability_Definition, Training_Rank] = {}

	for batch in Ensure_Training_Record(
			character
			).gains:
		for gain in batch.grants:
			best[gain.capability] = max(
				best.get(
					gain.capability,
					Training_Rank.PROFICIENT,
					),
				gain.rank,
				)

	for capability, rank in best.items():
		legacy = getattr(
			skills,
			capability.legacy_attribute,
			None,
			)

		if legacy is None:
			continue

		if rank is Training_Rank.EXPERTISE:
			legacy.set_expertise()
		else:
			legacy.set_proficiency()


def Commit_Training_Gain(
		character,
		gain: Training_Batch,
		) -> Training_Batch:
	"""Commit one preflighted batch, then refresh the legacy sheet projection."""
	next_training = Add_Training_Gain(
		Ensure_Training_Record(
			character
			),
		gain,
		)

	character.training = next_training
	Apply_Training_Record(character)

	return gain


def _self_test() -> None:
	class Example_Feature:
		pass

	class Probe:
		pass

	capability = Capability_Definition(
		key="example",
		name="Example",
		legacy_attribute="example",
		)
	batch = Training_Batch(
		grant_id="Example:1",
		feature=Example_Feature,
		grants=(
			Training_Grant(
				capability
				),
			),
		provenance=Provenance(
			source="Self-test"
			),
		)
	probe = Probe()
	probe.training = Add_Training_Gain(
		Training_Record(),
		batch,
		)
	view = New_Feature_Training_Record(
		probe,
		Example_Feature,
		)

	assert Is_Trained(
		probe,
		capability,
		)
	assert view.gains == (
		batch,
		)
	assert Add_Training_Gain(
		probe.training,
		batch,
		) is probe.training

	second_source = Training_Batch(
		grant_id="Example:2",
		feature=Example_Feature,
		grants=(
			Training_Grant(
				capability
				),
			),
		provenance=Provenance(
			source="Another source"
			),
		)
	probe.training = Add_Training_Gain(
		probe.training,
		second_source,
		)

	assert len(
		Find_Training_Gains(
			probe,
			capability,
			)
		) == 2
	assert Find_Training_Rank(
		probe,
		capability,
		) is Training_Rank.PROFICIENT

	class Legacy_Training:
		proficiency_level = 1

	class Legacy_Skills:
		Shared_Category = Legacy_Training()

	ambiguous = Capability_Definition(
		key="Specific_Choice",
		name="Specific Choice",
		legacy_attribute="Shared_Category",
		)
	legacy_probe = Probe()
	legacy_probe.training = Training_Record()
	legacy_probe.skills = Legacy_Skills()

	assert not Is_Trained(
		legacy_probe,
		ambiguous,
		)

	conflict = Training_Batch(
		grant_id="Example:1",
		feature=Example_Feature,
		grants=(
			Training_Grant(
				capability,
				Training_Rank.EXPERTISE,
				),
			),
		provenance=Provenance(
			source="Self-test"
			),
		)

	try:
		Add_Training_Gain(
			probe.training,
			conflict,
			)
	except ValueError:
		pass
	else:
		raise AssertionError(
			"A reused grant ID with another payload must conflict."
			)

	print("OK — ProficiencyKit self-test")


if __name__ == "__main__":
	_self_test()
