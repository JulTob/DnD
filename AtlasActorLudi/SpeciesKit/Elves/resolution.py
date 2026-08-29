"""Resolve Elf rule choices onto a completed Character sheet."""

from AtlasActorLudi.SpeciesKit.Elves.traits import Darkvision
from AtlasActorLudi.SpeciesKit.Elves.traits import Keen_Senses
from AtlasActorLudi.SpeciesKit.magic import ABILITY_LABELS
from AtlasActorLudi.SpeciesKit.magic import Resolve_Species_Spells
from AtlasActorLudi.SpeciesKit.Elves.traits import Elven_Lineage
from AtlasActorLudi.SpeciesKit.magic import Align_Lineage_Ability
from AtlasActorLudi.SpeciesKit.magic import Species_Spellcasting_Chips
from AtlasActorLudi.SpeciesKit.magic import Spell_Progression
from AtlasActorLudi.SpeciesKit.presentation import Project_Species_Feature


def _resolve_keen_senses(
	target,
	):
	skills = getattr(
		target,
		"skills",
		None,
		)

	if skills is None:
		return None

	selected = getattr(
		target,
		"keen_senses_skill",
		None,
		)

	if selected is None:
		available = tuple(
			name
			for name in Keen_Senses.SKILLS
			if getattr(
				getattr(
					skills,
					name,
					None,
					),
				"proficiency_level",
				0,
				) < 1
			)
		pool = (
			available
			or Keen_Senses.SKILLS
			)
		dice_bag = target.Dice_Bag(
			"identity.species.Elf.keen_senses",
			version="2024",
			namespace="GenLegendActor",
			)
		selected = target.Pick(
			pool,
			dice=dice_bag,
			)
		target.keen_senses_skill = selected

	skill = getattr(
		skills,
		selected,
		None,
		)

	if (
		skill is not None
		and hasattr(
			skill,
			"set_proficiency",
			)
		):
		skill.set_proficiency()

	return selected


# One line per lineage, echoing what that Heritage's own description already
# established rather than restating it. Never a bloodline: elves drift as a
# people over centuries (Documenta/Canon/Elves-and-the-Dreaming.md), so these
# speak about what was taught or brought home, not what was passed down.
_LINEAGE_LINES = {
	"High_Elf": (
		"Your people traded with more than merchants, and not "
		"everything you brought home was cargo."
		),
	"Wood_Elf": (
		"The woods have always answered your people, and some of "
		"that answer stayed with you."
		),
	"Dark_Elf": (
		"The dark taught your people how to survive it, and some "
		"of that lesson still answers when you call."
		),
	"Fae_Elf": (
		"The crossing into the Feywild left more on you than long "
		"ears."
		),
	"Shadow_Elf": (
		"Telling dream from thought took practice, and the "
		"practice became a kind of magic."
		),
	}


def _lineage_description(
	heritage,
	ability,
	):
	ability_label = ABILITY_LABELS.get(
		ability,
		ability,
		)
	spell_progression = Spell_Progression(
		heritage.SPELLS
		)
	line = _LINEAGE_LINES.get(
		heritage.__name__,
		"",
		)
	description = (
		f"{line} "
		f"<b>Spellcasting Ability.</b> {ability_label}. "
		f"<b>Lineage Spells.</b> {spell_progression}. "
		"You always have the leveled spells prepared. "
		"You can cast each of them once without a spell slot, "
		"regaining that use when you finish a Long Rest, "
		"and can also cast them with spell slots."
		).strip()

	from AtlasActorLudi.SpeciesKit.Elves import High_Elf

	if heritage is High_Elf:
		description += (
			" After a Long Rest, Prestidigitation can be replaced "
			"with another Wizard cantrip."
			)

	return description


def Resolve_Elf_Features(
	target,
	) -> None:
	"""Project Elf Tags into readable Entries and mechanical ledgers."""
	from AtlasActorLudi.SpeciesKit.Elves.base import Elf
	from AtlasActorLudi.SpeciesKit.catalog import Current_Heritage

	if target not in Elf:
		return

	keen_sense = _resolve_keen_senses( target )
	darkvision_range = int(
		getattr(
			target,
			"darkvision",
			Darkvision.RANGE,
			)
		)
	Project_Species_Feature(
		target,
		"Darkvision",
		(
			"*Your elven eyes are sharp and your attention focused.*\n\n"
			"You can see in Dim Light within "
			f"{darkvision_range} feet as if it were Bright Light, "
			"and in Darkness as if it were Dim Light."
			),
		level=1,
		)
	Project_Species_Feature(
		target,
		"Fey Ancestry",
		(
			"*The echoes of the Fae still linger in you, letting you see "
			"through trickery and deception.*\n\n"
			"You have Advantage on saving "
			"throws you make to avoid or end the Charmed condition."
			),
		level=1,
		)

	if keen_sense is not None:
		Project_Species_Feature(
			target,
			"Keen Senses",
			(
				"Centuries of long peace taught your people to notice "
				f"what almost went wrong. You have proficiency in "
				f"{keen_sense}."
				),
			level=1,
			)

	Project_Species_Feature(
		target,
		"Trance",
		(
			"You never fully wake from wherever your dreams first "
			"came from. You don't need to sleep, and magic can't put "
			"you to sleep. You can finish a Long Rest in 4 hours by "
			"meditating."
			),
		level=1,
		)
	heritage = Current_Heritage( target )

	if heritage is None:
		return

	unlocked = Resolve_Species_Spells(
		target,
		heritage.SPELLS,
		)
	target.species_spell_free_casts = {
		spell.name: 1
		for spell in unlocked
		if int(
			spell.level
			) > 0
		}
	# Settled here rather than when the Heritage landed, because the Guild did
	# not exist yet and this follows whatever the Character casts with.
	ability = Align_Lineage_Ability(
		target,
		Elven_Lineage.SPELLCASTING_ABILITIES,
		)
	Project_Species_Feature(
		target,
		f"{heritage.__name__.replace('_', ' ')} Lineage",
		_lineage_description(
			heritage,
			ability,
			),
		chips=Species_Spellcasting_Chips(
			target
			),
		level=1,
		)
