"""
Bard Training Tags — 2024 PHB core + all Colleges.

Thought pattern
        1. Core lessons belong to the Bard Guild (no College).
        2. College lessons set ``path=…`` and awaken only for that College.
        3. Bardic Inspiration die is a Chip + callable Entry — not separate.
        4. ASI / Epic Boon picks stay on legacy Progression.
"""

from __future__ import annotations

from AtlasLusoris.TrainingKit import Build_Training


GUILD = "Bard"
CORE_SOURCE = "Training: Bard"
DANCE = "Dance"
GLAMOUR = "Glamour"
LORE = "Lore"
VALOR = "Valor"


def _rank(
		char,
		) -> int:
	from AtlasLusoris.TrainingKit import level_in_guild
	return level_in_guild(
			char,
			GUILD,
			)


def _bardic_die(
		char,
		) -> str:
	level = _rank(
			char
			)
	if level >= 15:
		return "d12"
	if level >= 10:
		return "d10"
	if level >= 5:
		return "d8"
	return "d6"


def _bardic_uses(
		char,
		) -> int:
	from AtlasActorLudi.Map_of_Scores import Modifier
	cha = getattr(
			getattr(
					char,
					"abilities",
					None,
					),
			"CHA",
			10,
			)
	return max(
			1,
			Modifier(
					cha
					),
			)


def _core(
		*,
		name: str,
		min_level: int,
		description,
		chips=(),
		apply=None,
		):
	return Build_Training(
			name=name,
			guild_name=GUILD,
			min_level=min_level,
			description=description,
			chips=chips,
			apply=apply,
			source=CORE_SOURCE,
			)


def _path(
		path_name: str,
		*,
		name: str,
		min_level: int,
		description,
		chips=(),
		):
	return Build_Training(
			name=name,
			guild_name=GUILD,
			min_level=min_level,
			description=description,
			chips=chips,
			path=path_name,
			source=f"Training: College of {path_name}",
			)


def _dance(
		*,
		name: str,
		min_level: int,
		description,
		chips=(),
		):
	return _path(
			DANCE,
			name=name,
			min_level=min_level,
			description=description,
			chips=chips,
			)


def _glamour(
		*,
		name: str,
		min_level: int,
		description,
		chips=(),
		):
	return _path(
			GLAMOUR,
			name=name,
			min_level=min_level,
			description=description,
			chips=chips,
			)


def _lore(
		*,
		name: str,
		min_level: int,
		description,
		chips=(),
		):
	return _path(
			LORE,
			name=name,
			min_level=min_level,
			description=description,
			chips=chips,
			)


def _valor(
		*,
		name: str,
		min_level: int,
		description,
		chips=(),
		):
	return _path(
			VALOR,
			name=name,
			min_level=min_level,
			description=description,
			chips=chips,
			)


# ---------------------------------------------------------------------------
# Callable entries (level-sensitive text)
# ---------------------------------------------------------------------------


def _bardic_entry(
		char,
		) -> str:
	die = _bardic_die(
			char
			)
	uses = _bardic_uses(
			char
			)
	level = _rank(
			char
			)
	rest = "Short or Long" if level >= 5 else "Long"
	return (
		f"Your Bardic Inspiration die is a <b>{die}</b>. "
		"<br><b>Bonus Action:</b> inspire a creature within 60 feet that can "
		"see or hear you. That creature gains one Bardic Inspiration die. "
		"A creature can have only one Bardic Inspiration die at a time. "
		"<br>Once within the next hour, when the creature fails a D20 Test, "
		"it can roll the die and add the number to the d20, potentially "
		"turning failure into success. The die is expended when rolled. "
		f"<br>You can confer a total of <b>{uses} Bardic Inspiration dice</b>. "
		f"You regain all expended uses when you finish a <b>{rest} Rest</b>."
		)


# ---------------------------------------------------------------------------
# Core Guild lessons
# ---------------------------------------------------------------------------


Bardic_Inspiration = _core(
		name="Bardic Inspiration",
		min_level=1,
		description=_bardic_entry,
		chips=(
				("Bardic Die", _bardic_die),
				("Bardic Uses", _bardic_uses),
				),
		)

Spellcasting = _core(
		name="Spellcasting",
		min_level=1,
		description=(
			"You cast Bard spells through performance and wit. "
			"<b>Charisma</b> is your spellcasting ability. "
			"You know a selection of Bard spells from the Bard spell list."
			),
		)

Expertise = _core(
		name="Expertise",
		min_level=2,
		description=(
			"Choose two skills you are proficient in. Your proficiency "
			"bonus is doubled for any ability check you make "
			"using either of those skills."
			),
		)

Jack_of_All_Trades = _core(
		name="Jack of All Trades",
		min_level=2,
		description=(
			"You can add half your proficiency bonus (rounded down) to any "
			"ability check you make that doesn't already use your proficiency bonus."
			),
		)

Font_of_Inspiration = _core(
		name="Font of Inspiration",
		min_level=5,
		description=(
			"You regain all your expended Bardic Inspiration uses when you "
			"finish a Short or Long Rest."
			),
		)

Countercharm = _core(
		name="Countercharm",
		min_level=7,
		description=(
			"<b>Action:</b> you begin a performance that lasts until the "
			"end of your next turn. During that time, you and any friendly "
			"creature within 30 feet that can hear you have Advantage on "
			"saving throws against the Charmed and Frightened conditions. "
			"A creature must be able to hear you at the start of its turn to gain "
			"this benefit."
			),
		)


Expertise_II = _core(
		name="Expertise (II)",
		min_level=9,
		description=(
			"Choose two more skills you are proficient in. Your "
			"proficiency bonus is doubled for any ability check you make "
			"using either of those skills."
			),
		)

Magical_Secrets = _core(
		name="Magical Secrets",
		min_level=10,
		description=(
			"You have plundered magical knowledge from a wide spectrum of "
			"disciplines. Choose two spells from any class's spell list. "
			"The chosen spells count as Bard spells for you and are always prepared."
			),
		)

Superior_Inspiration = _core(
		name="Superior Inspiration",
		min_level=18,
		description=(
			"When you roll Initiative and have no Bardic Inspiration uses remaining, "
			"you regain <b>one</b> expended use."
			),
		)

Words_of_Creation = _core(
		name="Words of Creation",
		min_level=20,
		description=(
			"You have mastered two of the Words of Creation: "
			"<em>Power Word Heal</em> and <em>Power Word Kill</em>. "
			"These spells are always prepared for you and don't count "
			"against your number of prepared spells. <br>When you "
			"cast either spell, you can target a second creature with "
			"the spell if that creature is within 10 feet of the first target."
			),
		)


# ---------------------------------------------------------------------------
# College of Dance
# ---------------------------------------------------------------------------


Dazzling_Footwork = _dance(
		name="Dazzling Footwork",
		min_level=3,
		description=(
			"While you aren't wearing armor or wielding a Shield, you gain:"
			"<ul><li><b>Unarmored Defense.</b> Your base AC equals 10 "
			"+ your Dexterity modifier + your Charisma modifier.</li>"
			"<li><b>Agile Strikes.</b> When you expend a use of your "
			"Bardic Inspiration as part of an action, Bonus Action, "
			"or Reaction, you can make one Unarmed Strike as part "
			"of that same action, Bonus Action, or Reaction.</li>"
			"<li><b>Bardic Damage.</b> You can use Dexterity "
			"instead of Strength for Unarmed Strike attack rolls. "
			"When you deal damage with an Unarmed Strike, you "
			"can deal Bludgeoning damage equal to a roll of "
			"your Bardic Inspiration die plus your Dexterity "
			"modifier (this roll doesn't expend the die).</li>"
			"</ul>"
			),
		)

Inspiring_Movement = _dance(
		name="Inspiring Movement",
		min_level=6,
		description=(
			"When an enemy you can see ends its turn within 5 feet "
			"of you, you can take a Reaction and expend one use of "
			"your Bardic Inspiration to move up to half your Speed. "
			"One ally of your choice within 30 feet can then also "
			"move up to half their Speed using their Reaction. "
			"None of this movement provokes Opportunity Attacks."
			),
		)

Tandem_Footwork = _dance(
		name="Tandem Footwork",
		min_level=6,
		description=(
			"When you roll Initiative (and don't have the Incapacitated condition), "
			"you can expend one use of your Bardic Inspiration. When you do, "
			"roll your Bardic Inspiration die; you and each ally within 30 "
			"feet that can see or hear you gain a bonus to Initiative equal to "
			"the number rolled."
			),
		)

Leading_Evasion = _dance(
		name="Leading Evasion",
		min_level=14,
		description=(
			"When you are subjected to an effect that allows you to make a "
			"Dexterity saving throw to take only half damage, you instead "
			"take no damage on a success and only half damage on a failure. "
			"<br>If any creatures within 5 feet of you are making the same Dexterity "
			"saving throw, you can share this benefit with them for that save. "
			"You can't use this feature if you have the Incapacitated condition."
			),
		)


# ---------------------------------------------------------------------------
# College of Glamour
# ---------------------------------------------------------------------------


Beguiling_Magic = _glamour(
		name="Beguiling Magic",
		min_level=3,
		description=(
			"You always have the <em>Charm Person</em> and <em>Mirror "
			"Image</em> spells prepared. <br>Immediately after you cast "
			"an Enchantment or Illusion spell using a spell slot, you "
			"can cause a creature you can see within 60 feet to make "
			"a Wisdom saving throw (DC equals your spell save DC). "
			"On a failed save, the target has the Charmed or Frightened "
			"condition (your choice) for 1 minute. The target repeats the "
			"save at the end of each of its turns. <br>Once you use this "
			"benefit, you can't use it again until you finish a Long Rest. "
			"You can also restore it by expending one use of your "
			"Bardic Inspiration (no action required)."
			),
		)

Mantle_of_Inspiration = _glamour(
		name="Mantle of Inspiration",
		min_level=3,
		description=(
			"<b>Bonus Action:</b> expend a use of Bardic Inspiration and roll the die. "
			"Choose a number of other creatures within 60 feet, up to your Charisma "
			"modifier (minimum one). Each chosen creature gains Temporary Hit Points "
			"equal to <b>2 × the number rolled</b> and can use its Reaction to move "
			"up to its Speed without provoking Opportunity Attacks."
			),
		)

Mantle_of_Majesty = _glamour(
		name="Mantle of Majesty",
		min_level=6,
		description=(
			"You always have the <em>Command</em> spell prepared. <br><b>"
			"Bonus Action:</b> cast <em>Command</em> without expending a "
			"spell slot and assume an unearthly appearance for 1 minute or "
			"until your Concentration ends. While this lasts, you can cast "
			"Command as a Bonus Action on each turn (no slot required). "
			"<br>Any creature Charmed by you automatically fails its saving "
			"throw against the Command you cast with this feature. <br>"
			"Once used, you can't use it again until you finish a Long Rest, "
			"or until you expend a level-3+ spell slot (no action required)."
			),
		)

Unbreakable_Majesty = _glamour(
		name="Unbreakable Majesty",
		min_level=14,
		description=(
			"<b>Bonus Action:</b> assume a magically majestic presence "
			"for 1 minute or until you have the Incapacitated condition. "
			"<br>For the duration, the first time each turn any creature "
			"hits you with an attack roll, the attacker must succeed on a "
			"Charisma saving throw against your spell save DC or the attack "
			"misses instead, as the creature recoils from your majesty. "
			"<br>Once used, you can't use it again until you finish a Short or Long Rest."
			),
		)


# ---------------------------------------------------------------------------
# College of Lore
# ---------------------------------------------------------------------------


Bonus_Proficiencies = _lore(
		name="Bonus Proficiencies",
		min_level=3,
		description=(
			"You gain proficiency in three skills of your choice."
			),
		)

Cutting_Words = _lore(
		name="Cutting Words",
		min_level=3,
		description=(
			"<b>Reaction:</b> when a creature you can see within 60 feet makes "
			"a damage roll or succeeds on an ability check or attack roll, "
			"you can expend one use of Bardic Inspiration and roll the die. "
			"Subtract the number rolled from the creature's roll, potentially "
			"turning success into failure or reducing damage."
			),
		)

Magical_Discoveries = _lore(
		name="Magical Discoveries",
		min_level=6,
		description=(
			"You learn two spells of your choice from the Cleric, Druid, "
			"or Wizard spell list (or any combination). A chosen spell "
			"must be a cantrip or a spell for which you have spell slots. "
			"<br>These spells are always prepared and don't count against your "
			"number of prepared spells."
			),
		)

Peerless_Skill = _lore(
		name="Peerless Skill",
		min_level=14,
		description=(
			"When you make an ability check or attack roll and fail, you can expend "
			"one use of Bardic Inspiration. Roll the Bardic Inspiration die and add "
			"the number rolled to your d20, potentially turning a failure into a "
			"success. On a failure, the Bardic Inspiration use is not expended."
			),
		)


# ---------------------------------------------------------------------------
# College of Valor
# ---------------------------------------------------------------------------


Combat_Inspiration = _valor(
		name="Combat Inspiration",
		min_level=3,
		description=(
			"A creature that has a Bardic Inspiration die from "
			"you can use it for one of the following effects:<ul>"
			"<li><b>Defense.</b> When the creature is hit by an "
			"attack roll, it can use its Reaction to roll the die "
			"and add the number to its AC against that attack, "
			"potentially causing the attack to miss.</li><li><b>"
			"Offense.</b> Immediately after the creature hits a target "
			"with an attack roll, it can roll the die and add the "
			"number to the attack's damage against the target.</li>"
			"</ul>"
			),
		)

Martial_Training = _valor(
		name="Martial Training",
		min_level=3,
		description=(
			"You gain proficiency with Martial weapons and "
			"training with Medium Armor and Shields. <br>In "
			"addition, you can use a Simple or Martial weapon as a "
			"Spellcasting Focus to cast spells from your Bard spell list."
			),
		)


Valor_Extra_Attack = _valor(
		name="Extra Attack",
		min_level=6,
		description=(
			"You can attack twice instead of once whenever you "
			"take the Attack action on your turn. <br>In addition, "
			"you can cast one of your cantrips that has a "
			"casting time of an action in place of one of those attacks."
			),
		)

Battle_Magic = _valor(
		name="Battle Magic",
		min_level=14,
		description=(
			"After you cast a spell that has a casting time of an action, "
			"you can make one attack with a weapon or Unarmed Strike as a Bonus Action."
			),
		)
