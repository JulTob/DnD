"""Epic Boon feats — 2024 PHB catalogue."""

from __future__ import annotations

from AtlasLusoris.FeatKit import Build_Epic_Boon


BoonOfCombatProwess = Build_Epic_Boon(
	name='Boon of Combat Prowess',
	description=(
		'Increase one ability score by 1, to a maximum of 30. '
		'Once per turn when you miss with an attack roll, you can hit instead.'
		),
	)

BoonOfDimensionalTravel = Build_Epic_Boon(
	name='Boon of Dimensional Travel',
	description=(
		'Increase one ability score by 1, to a maximum of 30. '
		'Immediately after you take the Attack action or the Magic action, '
		'you can teleport up to 30 feet to an unoccupied space you can see.'
		),
	)

BoonOfEnergyResistance = Build_Epic_Boon(
	name='Boon of Energy Resistance',
	description=(
		'Increase one ability score by 1, to a maximum of 30. '
		'You gain Resistance to two damage types of your choice from Acid, '
		'Cold, Fire, Lightning, Necrotic, Poison, Psychic, Radiant, and '
		'Thunder. You can change the types when you finish a Long Rest.'
		),
	)

BoonOfFate = Build_Epic_Boon(
	name='Boon of Fate',
	description=(
		'Increase one ability score by 1, to a maximum of 30. '
		'When you or a creature within 60 feet of you succeeds or fails a '
		'D20 Test, you can roll 2d4 and apply the total as a bonus or '
		'penalty to the roll. Once you use this Boon, you can\'t use it '
		'again until you finish a Short or Long Rest.'
		),
	)

BoonOfFortitude = Build_Epic_Boon(
	name='Boon of Fortitude',
	description=(
		'Increase one ability score by 1, to a maximum of 30. '
		'Your Hit Point maximum increases by 40. Whenever you regain Hit '
		'Points, you can regain extra Hit Points equal to your Constitution '
		'modifier (minimum of 1). You can gain this extra healing only '
		'once per turn.'
		),
	)

BoonOfIrresistibleOffense = Build_Epic_Boon(
	name='Boon of Irresistible Offense',
	description=(
		'Increase your Strength or Dexterity by 1, to a maximum of 30. '
		'The Bludgeoning, Piercing, and Slashing damage you deal ignores '
		'Resistance. When you roll a 20 on an attack roll, the target takes '
		'extra damage of the attack\'s type equal to the ability score you '
		'increased with this Boon.'
		),
	asi=(
		'STR',
		'DEX',
		),
	)

BoonOfRecovery = Build_Epic_Boon(
	name='Boon of Recovery',
	description=(
		'Increase one ability score by 1, to a maximum of 30. '
		'You have a pool of ten d10s. As a Bonus Action, you can expend '
		'dice from the pool and regain Hit Points equal to the total. You '
		'also regain all expended dice when you finish a Long Rest. If you '
		'are reduced to 0 Hit Points but not killed outright, you can drop '
		'to 1 Hit Point instead and regain Hit Points equal to half your '
		'Hit Point maximum (once per Long Rest).'
		),
	)

BoonOfSkill = Build_Epic_Boon(
	name='Boon of Skill',
	description=(
		'Increase one ability score by 1, to a maximum of 30. '
		'You gain proficiency in all skills. Choose one skill in which you '
		'have proficiency; you gain Expertise in it.'
		),
	)

BoonOfSpeed = Build_Epic_Boon(
	name='Boon of Speed',
	description=(
		'Increase one ability score by 1, to a maximum of 30. '
		'Your Speed increases by 30 feet. As a Bonus Action, you can take '
		'the Disengage action, which also ends the Grappled condition on you.'
		),
	)

BoonOfSpellRecall = Build_Epic_Boon(
	name='Boon of Spell Recall',
	description=(
		'Increase your Intelligence, Wisdom, or Charisma by 1, to a '
		'maximum of 30. Whenever you cast a spell with a spell slot of '
		'levels 1–4, roll a d4. If you roll the slot\'s level, the spell '
		'is cast without expending the slot.'
		),
	asi=(
		'INT',
		'WIS',
		'CHA',
		),
	requires_spellcasting=True,
	)

BoonOfTheNightSpirit = Build_Epic_Boon(
	name='Boon of the Night Spirit',
	description=(
		'Increase one ability score by 1, to a maximum of 30. '
		'While you are in Dim Light or Darkness, you have Resistance to '
		'all damage except Force, Psychic, and Radiant, and you can take '
		'a Bonus Action to become Invisible. The Invisibility ends early '
		'after you take an action, Bonus Action, or Reaction.'
		),
	)

BoonOfTruesight = Build_Epic_Boon(
	name='Boon of Truesight',
	description=(
		'Increase one ability score by 1, to a maximum of 30. '
		'You have Truesight with a range of 60 feet.'
		),
	)
