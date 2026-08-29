"""
Cleric Training Tags — 2024 PHB core + all Domains.

Thought pattern
	1. Core lessons belong to the Cleric Guild (no Domain).
	2. Domain lessons set ``path=…`` and awaken only for that Domain.
	3. Domain Spells are a single Training entry per Domain listing spells.
	4. ASI / Epic Boon picks stay on legacy Progression.
"""

from __future__ import annotations

import random

from AtlasLusoris.TrainingKit import Build_Training


GUILD = "Cleric"
CORE_SOURCE = "Training: Cleric"
LIFE = "Life"
LIGHT = "Light"
TRICKERY = "Trickery"
WAR = "War"


def _rank(
		char,
		) -> int:
	from AtlasLusoris.TrainingKit import level_in_guild
	return level_in_guild(
			char,
			GUILD,
			)


def _channel_uses(
		char,
		) -> int:
	level = _rank(
			char
			)
	if level >= 6:
		return 3
	return 2


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
			source=f"Training: {path_name} Domain",
			)


def _life(
		*,
		name: str,
		min_level: int,
		description,
		chips=(),
		):
	return _path(
			LIFE,
			name=name,
			min_level=min_level,
			description=description,
			chips=chips,
			)


def _light(
		*,
		name: str,
		min_level: int,
		description,
		chips=(),
		):
	return _path(
			LIGHT,
			name=name,
			min_level=min_level,
			description=description,
			chips=chips,
			)


def _trickery(
		*,
		name: str,
		min_level: int,
		description,
		chips=(),
		):
	return _path(
			TRICKERY,
			name=name,
			min_level=min_level,
			description=description,
			chips=chips,
			)


def _war(
		*,
		name: str,
		min_level: int,
		description,
		chips=(),
		):
	return _path(
			WAR,
			name=name,
			min_level=min_level,
			description=description,
			chips=chips,
			)


# ---------------------------------------------------------------------------
# Callable entries (level-sensitive text)
# ---------------------------------------------------------------------------


def _channel_entry(
		char,
		) -> str:
	uses = _channel_uses(
			char
			)
	return (
		"You can channel divine energy to fuel magical effects. "
		f"You have <b>{uses} uses</b> of Channel Divinity. "
		"You regain all expended uses when you finish a Short Rest. "
		"<br>Standard Channel Divinity options include:"
		"<ul>"
		"<li><b>Divine Spark.</b> Choose a creature you can see within 30 feet. "
		"Roll a number of d8s equal to your Wisdom modifier (minimum 1). "
		"The creature either regains Hit Points equal to the total or takes "
		"Radiant or Necrotic damage equal to the total (your choice).</li>"
		"<li><b>Turn Undead.</b> Each Undead that can see or hear you within "
		"30 feet must make a Wisdom saving throw against your spell save DC. "
		"On a failed save, the creature has the Frightened and Incapacitated "
		"conditions for 1 minute.</li>"
		"</ul>"
		"<br>If a Channel Divinity effect requires a saving throw, the DC equals "
		"your Cleric spell save DC."
		)


# ---------------------------------------------------------------------------
# Divine Order & Blessed Strikes — forks the generator resolves to one option
# ---------------------------------------------------------------------------


def _fork_rng(char, salt):
	"""Per-character, per-choice RNG — deterministic, leaves char.dices untouched."""
	seed = getattr(char, "seed", None)
	if seed is None:
		seed = getattr(char, "name", "") or 0
	return random.Random(f"{seed}:{salt}")


def _apply_divine_order(char):
	"""Pick one Divine Order and instantiate its mechanics — not a menu."""
	order = getattr(char, "divine_order", None)
	if order not in ("Protector", "Thaumaturge"):
		order = _fork_rng(char, "divine_order").choice(("Protector", "Thaumaturge"))
		char.divine_order = order
	if order == "Protector":
		skills = getattr(char, "skills", None)
		if skills is not None:
			skills.Martial_Weapons.set_proficiency()
			skills.Heavy.set_proficiency()
	# Thaumaturge's extra cantrip is instantiated by the Cleric spellcaster,
	# which reads char.divine_order as it prepares spells.


def _divine_order_entry(char):
	"""Only the chosen Order reaches the sheet."""
	if getattr(char, "divine_order", None) == "Protector":
		return (
			"<b>Protector.</b> Trained for battle, you have proficiency with "
			"Martial weapons and Heavy armor."
			)
	return (
		"<b>Thaumaturge.</b> You know one extra cantrip from the Cleric "
		"spell list."
		)


def _apply_blessed_strikes(char):
	"""Pick one Blessed Strikes option — Divine Strike or Potent Spellcasting."""
	if getattr(char, "blessed_strikes", None) not in (
			"Divine Strike",
			"Potent Spellcasting",
			):
		char.blessed_strikes = _fork_rng(char, "blessed_strikes").choice(
				("Divine Strike", "Potent Spellcasting")
				)


def _blessed_strikes_entry(char):
	if getattr(char, "blessed_strikes", None) == "Potent Spellcasting":
		return (
			"<b>Potent Spellcasting.</b> You add your Wisdom modifier to the "
			"damage you deal with any Cleric cantrip."
			)
	return (
		"<b>Divine Strike.</b> Once per turn, when you hit a creature with an "
		"attack roll using a weapon, you can deal an extra <b>1d8</b> Necrotic "
		"or Radiant damage (your choice)."
		)


def _improved_blessed_strikes_entry(char):
	if getattr(char, "blessed_strikes", None) == "Potent Spellcasting":
		return (
			"<b>Potent Spellcasting improves.</b> When you cast a Cleric cantrip "
			"and miss or the target succeeds on its saving throw, you deal half "
			"your Wisdom modifier in Radiant or Necrotic damage (minimum 1)."
			)
	return (
		"<b>Divine Strike improves.</b> The extra damage of your Divine Strike "
		"increases to <b>2d8</b>."
		)


# ---------------------------------------------------------------------------
# Core Guild lessons
# ---------------------------------------------------------------------------


Spellcasting = _core(
		name="Spellcasting",
		min_level=1,
		description=(
			"You cast Cleric spells through prayer and devotion. "
			"<b>Wisdom</b> is your spellcasting ability. "
			"You prepare a number of Cleric spells chosen from the Cleric spell list "
			"equal to your Wisdom modifier + your Cleric level (minimum of one spell). "
			"You can change your prepared list when you finish a Long Rest."
			),
		)

Divine_Order = _core(
		name="Divine Order",
		min_level=1,
		description=_divine_order_entry,
		apply=_apply_divine_order,
		)

Channel_Divinity = _core(
		name="Channel Divinity",
		min_level=2,
		description=_channel_entry,
		chips=(
				("Channel Divinity Uses", _channel_uses, "🕊️"),
				),
		)

Sear_Undead = _core(
		name="Sear Undead",
		min_level=5,
		description=(
			"Whenever you use Turn Undead, you can roll a number of d8s equal to "
			"your Wisdom modifier and deal that much Radiant damage to each Undead "
			"that fails its saving throw. "
			"The damage can't reduce an Undead to fewer than 1 Hit Point."
			),
		)

Blessed_Strikes = _core(
		name="Blessed Strikes",
		min_level=7,
		description=_blessed_strikes_entry,
		apply=_apply_blessed_strikes,
		)

Divine_Intervention = _core(
		name="Divine Intervention",
		min_level=10,
		description=(
			"You can call on your deity to intervene on your behalf when your need "
			"is great. "
			"<b>Magic action:</b> describe the assistance you seek and roll a d100. "
			"If you roll a number equal to or lower than your Cleric level, your "
			"deity intervenes. The DM chooses the nature of the intervention; the "
			"effect of any Cleric spell or Cleric Domain spell would be appropriate. "
			"<br>If your deity intervenes, you can't use this feature again for "
			"7 days. Otherwise, you can use it again after a Long Rest."
			),
		)

Improved_Blessed_Strikes = _core(
		name="Improved Blessed Strikes",
		min_level=14,
		description=_improved_blessed_strikes_entry,
		)

Greater_Divine_Intervention = _core(
		name="Greater Divine Intervention",
		min_level=20,
		description=(
			"Your call for intervention succeeds automatically — no roll required. "
			"The effect duplicates any Cleric spell of level 8 or lower without "
			"needing a spell slot. "
			"<br>Once you use this feature, you can't use it again until you "
			"finish 2d4 days of prayer and meditation."
			),
		)


# ---------------------------------------------------------------------------
# Life Domain
# ---------------------------------------------------------------------------


Life_Domain_Spells = _life(
		name="Domain Spells",
		min_level=3,
		description=(
			"You always have the following spells prepared:"
			"<ul>"
			"<li><b>3rd:</b> <em>Aid, Bless</em></li>"
			"<li><b>5th:</b> <em>Lesser Restoration, Prayer of Healing</em></li>"
			"<li><b>9th:</b> <em>Mass Healing Word, Revivify</em></li>"
			"<li><b>13th:</b> <em>Aura of Life, Death Ward</em></li>"
			"<li><b>17th:</b> <em>Greater Restoration, Raise Dead</em></li>"
			"</ul>"
			),
		)

Disciple_of_Life = _life(
		name="Disciple of Life",
		min_level=3,
		description=(
			"Your healing spells are more effective. Whenever you use a spell of "
			"level 1 or higher to restore Hit Points to a creature, the creature "
			"regains additional Hit Points equal to <b>2 + the spell's level</b>."
			),
		)

Preserve_Life = _life(
		name="Preserve Life",
		min_level=3,
		description=(
			"<b>Channel Divinity — Magic action.</b> "
			"You evoke healing energy that restores Hit Points equal to "
			"<b>5 × your Cleric level</b> among any creatures of your choice "
			"that you can see within 30 feet. "
			"You can't restore an individual creature beyond half its Hit Point maximum."
			),
		)

Blessed_Healer = _life(
		name="Blessed Healer",
		min_level=6,
		description=(
			"The healing spells you cast on others heal you as well. "
			"When you cast a spell of level 1 or higher that restores Hit Points "
			"to another creature, you regain Hit Points equal to "
			"<b>2 + the spell's level</b>."
			),
		)

Supreme_Healing = _life(
		name="Supreme Healing",
		min_level=17,
		description=(
			"When you would normally roll one or more dice to restore Hit Points "
			"with a spell, you instead use the highest number possible for each die. "
			"For example, instead of restoring 2d6 Hit Points to a creature, "
			"you restore 12."
			),
		)


# ---------------------------------------------------------------------------
# Light Domain
# ---------------------------------------------------------------------------


Light_Domain_Spells = _light(
		name="Domain Spells",
		min_level=3,
		description=(
			"You always have the following spells prepared:"
			"<ul>"
			"<li><b>3rd:</b> <em>Burning Hands, Faerie Fire</em></li>"
			"<li><b>5th:</b> <em>Scorching Ray, See Invisibility</em></li>"
			"<li><b>9th:</b> <em>Daylight, Fireball</em></li>"
			"<li><b>13th:</b> <em>Arcane Eye, Wall of Fire</em></li>"
			"<li><b>17th:</b> <em>Flame Strike, Scrying</em></li>"
			"</ul>"
			),
		)

Radiance_of_the_Dawn = _light(
		name="Radiance of the Dawn",
		min_level=3,
		description=(
			"<b>Channel Divinity — Magic action.</b> "
			"You present your holy symbol, and any magical darkness within "
			"30 feet of you is dispelled. Additionally, each hostile creature "
			"within 30 feet must make a Constitution saving throw against your "
			"spell save DC. A creature takes <b>2d10 + your Cleric level</b> "
			"Radiant damage on a failed save, or half as much on a success. "
			"A creature that has Total Cover from you is not affected."
			),
		)

Warding_Flare = _light(
		name="Warding Flare",
		min_level=3,
		description=(
			"<b>Reaction:</b> when a creature you can see within 30 feet attacks "
			"you, you interpose divine light. The attacker has Disadvantage on the "
			"attack roll. "
			"<br>You can use this feature a number of times equal to your Wisdom "
			"modifier (minimum once). You regain all expended uses when you finish "
			"a Long Rest."
			),
		)

Improved_Warding_Flare = _light(
		name="Improved Warding Flare",
		min_level=6,
		description=(
			"You can now use Warding Flare when a creature within 30 feet attacks "
			"<em>any</em> creature, not just you. "
			"When you do so, the attacked creature can see the flare of light."
			),
		)

Corona_of_Light = _light(
		name="Corona of Light",
		min_level=17,
		description=(
			"<b>Magic action:</b> you cause yourself to emanate an aura of sunlight "
			"for 1 minute or until you end it (no action required). "
			"You emit bright light in a 60-foot radius and dim light for an "
			"additional 30 feet. "
			"<br>Your enemies in the bright light have Disadvantage on saving throws "
			"against your spells that deal Fire or Radiant damage."
			),
		)


# ---------------------------------------------------------------------------
# Trickery Domain
# ---------------------------------------------------------------------------


Trickery_Domain_Spells = _trickery(
		name="Domain Spells",
		min_level=3,
		description=(
			"You always have the following spells prepared:"
			"<ul>"
			"<li><b>3rd:</b> <em>Charm Person, Disguise Self</em></li>"
			"<li><b>5th:</b> <em>Invisibility, Pass without Trace</em></li>"
			"<li><b>9th:</b> <em>Hypnotic Pattern, Nondetection</em></li>"
			"<li><b>13th:</b> <em>Confusion, Dimension Door</em></li>"
			"<li><b>17th:</b> <em>Dominate Person, Modify Memory</em></li>"
			"</ul>"
			),
		)

Blessing_of_the_Trickster = _trickery(
		name="Blessing of the Trickster",
		min_level=3,
		description=(
			"<b>Action:</b> you can give a creature other than yourself (including "
			"yourself if that creature fails and you are the one touching) Advantage "
			"on Dexterity (Stealth) checks. "
			"This blessing lasts for 1 hour or until you use this feature again."
			),
		)

Invoke_Duplicity = _trickery(
		name="Invoke Duplicity",
		min_level=3,
		description=(
			"<b>Channel Divinity — Bonus Action.</b> "
			"You create a perfect illusory duplicate of yourself in an unoccupied "
			"space you can see within 30 feet. The illusion lasts for 1 minute or "
			"until you lose Concentration. "
			"<br>On each of your turns, you can use a Bonus Action to move the "
			"illusion up to 30 feet to a space you can see. "
			"<br>You can cast spells as though you were in the illusion's space, "
			"and you have Advantage on attack rolls against any creature within "
			"5 feet of the illusion."
			),
		)

Tricksters_Transposition = _trickery(
		name="Trickster's Transposition",
		min_level=6,
		description=(
			"When you use Bonus Action to move your Invoke Duplicity illusion, "
			"you can teleport, swapping places with the illusion. "
			"After swapping, the illusion reappears at your original location."
			),
		)

Improved_Duplicity = _trickery(
		name="Improved Duplicity",
		min_level=17,
		description=(
			"The power of your Invoke Duplicity improves in two ways: "
			"<br><b>Four Duplicates.</b> When you use Invoke Duplicity, you can "
			"create up to four duplicates of yourself instead of one. "
			"<br><b>Shared Distraction.</b> Whenever you or an ally makes an attack "
			"against a creature, if a duplicate is within 5 feet of the creature, "
			"the attack roll has Advantage."
			),
		)


# ---------------------------------------------------------------------------
# War Domain
# ---------------------------------------------------------------------------


War_Domain_Spells = _war(
		name="Domain Spells",
		min_level=3,
		description=(
			"You always have the following spells prepared:"
			"<ul>"
			"<li><b>3rd:</b> <em>Divine Favor, Shield of Faith</em></li>"
			"<li><b>5th:</b> <em>Magic Weapon, Spiritual Weapon</em></li>"
			"<li><b>9th:</b> <em>Crusader's Mantle, Spirit Guardians</em></li>"
			"<li><b>13th:</b> <em>Fire Shield, Freedom of Movement</em></li>"
			"<li><b>17th:</b> <em>Flame Strike, Hold Monster</em></li>"
			"</ul>"
			),
		)

Guided_Strike = _war(
		name="Guided Strike",
		min_level=3,
		description=(
			"<b>Channel Divinity — Reaction.</b> "
			"When you or a creature within 30 feet of you misses with an attack roll, "
			"you grant a <b>+10 bonus</b> to the attack roll, potentially turning the "
			"miss into a hit. "
			"You can use this feature before or after making the attack roll, but "
			"before any effects of the roll are applied."
			),
		)

War_Priest = _war(
		name="War Priest",
		min_level=3,
		description=(
			"Your deity blesses you with minor miracles. "
			"When you take the Attack action, you can use a Bonus Action to make "
			"an extra attack with a weapon or Unarmed Strike. "
			"<br>You can use this feature a number of times equal to your Wisdom "
			"modifier (minimum once). You regain all expended uses when you finish "
			"a Long Rest."
			),
		)

War_Gods_Blessing = _war(
		name="War God's Blessing",
		min_level=6,
		description=(
			"You can use your Guided Strike Channel Divinity to grant the +10 "
			"attack roll bonus to any ally you can see within 30 feet, "
			"not just yourself."
			),
		)

Avatar_of_Battle = _war(
		name="Avatar of Battle",
		min_level=17,
		description=(
			"You gain Resistance to Bludgeoning, Piercing, and Slashing damage "
			"from nonmagical attacks."
			),
		)
