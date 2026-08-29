"""Canonical typed Skill definitions used by Character training."""

from __future__ import annotations

from dataclasses import dataclass

from AtlasActorLudi.ProficiencyKit import Capability_Definition


@dataclass(
		frozen=True,
		slots=True,
		)
class Skill_Definition(Capability_Definition):
	"""One D20 Skill and its usual governing ability."""

	ability: str


def _Skill(
		key: str,
		name: str,
		ability: str,
		) -> Skill_Definition:
	return Skill_Definition(
		key=key,
		name=name,
		legacy_attribute=key,
		ability=ability,
		)


Athletics = _Skill(
	"Athletics",
	"Athletics",
	"STR",
	)

Acrobatics = _Skill(
	"Acrobatics",
	"Acrobatics",
	"DEX",
	)
Sleight_of_Hand = _Skill(
	"Sleight_of_Hand",
	"Sleight of Hand",
	"DEX",
	)
Stealth = _Skill(
	"Stealth",
	"Stealth",
	"DEX",
	)

Arcana = _Skill(
	"Arcana",
	"Arcana",
	"INT",
	)
History = _Skill(
	"History",
	"History",
	"INT",
	)
Investigation = _Skill(
	"Investigation",
	"Investigation",
	"INT",
	)
Nature = _Skill(
	"Nature",
	"Nature",
	"INT",
	)
Religion = _Skill(
	"Religion",
	"Religion",
	"INT",
	)

Animal_Handling = _Skill(
	"Animal_Handling",
	"Animal Handling",
	"WIS",
	)
Insight = _Skill(
	"Insight",
	"Insight",
	"WIS",
	)
Medicine = _Skill(
	"Medicine",
	"Medicine",
	"WIS",
	)
Perception = _Skill(
	"Perception",
	"Perception",
	"WIS",
	)
Survival = _Skill(
	"Survival",
	"Survival",
	"WIS",
	)

Deception = _Skill(
	"Deception",
	"Deception",
	"CHA",
	)
Intimidation = _Skill(
	"Intimidation",
	"Intimidation",
	"CHA",
	)
Performance = _Skill(
	"Performance",
	"Performance",
	"CHA",
	)
Persuasion = _Skill(
	"Persuasion",
	"Persuasion",
	"CHA",
	)


SKILLS: tuple[Skill_Definition, ...] = (
	Athletics,
	Acrobatics,
	Sleight_of_Hand,
	Stealth,
	Arcana,
	History,
	Investigation,
	Nature,
	Religion,
	Animal_Handling,
	Insight,
	Medicine,
	Perception,
	Survival,
	Deception,
	Intimidation,
	Performance,
	Persuasion,
	)

SKILLS_BY_KEY = {
	skill.key: skill
	for skill in SKILLS
	}


def _self_test() -> None:
	assert len(
		SKILLS
		) == 18
	assert len(
		SKILLS_BY_KEY
		) == len(
			SKILLS
			)
	assert Medicine.ability == "WIS"

	print(
		"OK — SkillsKit self-test"
		)


if __name__ == "__main__":
	_self_test()
