# AtlasLusoris/Grimoire_of_Features.py
# from AtlasLusoris.Grimoire_of_Features import Feature
from dataclasses import dataclass
import app.random as random

ABILITY_NAMES = {
	"STR": "Strength",  "DEX": "Dexterity", "CON": "Constitution",
	"INT": "Intelligence", "WIS": "Wisdom", "CHA": "Charisma",
	}


class Feature:
	def __init__(self, name, description="", apply=None, source=None, level=0):
		self.name = name
		self.description = description
		self.source = source
		self.level = level
		self.apply = apply  # Optional

	def __call__(self, char):
		if self.apply:
			self.apply(char)

	def __str__(self):
		return self.html()

	def html(self) -> str:
		return f"""
		<div class="npc-textbox" style="grid-column: span 1;">
			<h4 style="font-family: 'Manufacturing Consent' ; font-size:	2.1em;">
			{self.name}</h4>
		<i>{self.description}</i>
		</div>
		"""

	def to_html(self) -> str:
		return self.html()

	def to_dict(self) -> dict:
		return {
			"name": self.name,
			"source": self.source,
			"level": self.level,
			"description": self.description,
			}

class Feat(Feature):
	def __init__(self, name, apply,  description, condition=None, source="Feat", level=0):
		super().__init__(name=name, description=description, level=level, source=source)
		self.apply = apply            # Mutation function(char)
		self.condition = condition    # Predicate(char) -> bool

	def is_valid_for(self, char):
		return self.condition(char) if self.condition else True

	def __call__(self, char):
		print(f"Applying feat: {self.name}")
		self.apply(char)

	def __str__(self):
		return self.html()

	def html(self) -> str:
		return f"""
		<div class="npc-textbox" style="grid-column: span 1;">
			<h4 style="font-family: 'Manufacturing Consent' ; font-size:	2.1em;">
			{self.name}</h4>
		<i>{self.description}</i>
		</div>
		"""

	def to_dict(self):
		return {
			"name": self.name,
			"description": self.description,
			}

# ── Stat boosters ──
def all_ability_scores(char):
	return {
		"STR": char.abilities.STR,
		"DEX": char.abilities.DEX,
		"CON": char.abilities.CON,
		"INT": char.abilities.INT,
		"WIS": char.abilities.WIS,
		"CHA": char.abilities.CHA,
		}

def increase_two_highest_below_20(char):
	"""
	Raise two scores < 20.  Favour rounding odds first so each bump
	is more likely to change a modifier.
	"""
	stats = all_ability_scores(char)

	# Get all stats strictly below 20
	candidates = {k: v for k, v in stats.items() if v < 20}
	if not candidates:
		return  # nothing to increase
	# Sort by value descending, take up to 2
	best = sorted(
			candidates.items(),
			key=lambda kv: (kv[1] % 2 == 0, -kv[1])  # odds first, high→low
			)[:2]
	for key, _ in best:
		raise_stat(char, key, 1, cap=20)

def _ability_to_increase(char, cap: int = 30):
	"""
	Pick an ability to raise: prefer the *highest* one that is still < 30,
	break ties randomly.
	"""
	scores = all_ability_scores(char)

	# Filter out scores already at (or over) the cap
	candidates = {k: v for k, v in scores.items() if v < cap}
	if not candidates:
		raise ValueError("All six abilities have reached the cap")

	# ---------- 1. Look for the best *odd* score ----------
	odd_max = max((v for v in candidates.values() if v % 2), default=None)
	if odd_max is not None:
		bucket = [k for k, v in candidates.items() if v == odd_max and v % 2]
		return random.choice(bucket)

	# ---------- 2. No odd numbers?  Use the highest score ----------
	even_max = max(candidates.values())                    # guaranteed to exist
	bucket = [k for k, v in candidates.items() if v == even_max]
	return random.choice(bucket)

def raise_stat( char, key: str,	amount: int = 1, cap: int = 30):
	"""
	Increase char.abilities.<KEY> by <amount>, but not past <cap>.
	Keeps char.stats (in many sheets a plain-text dict) in sync.
	"""
	new_val = min(getattr(char.abilities, key) + amount, cap)
	setattr(char.abilities, key, new_val)

	# if the character keeps a parallel stats dict, sync it
	if hasattr(char, "stats"):
		full = {
			"STR": "Strength", "DEX": "Dexterity", "CON": "Constitution",
			"INT": "Intelligence", "WIS": "Wisdom", "CHA": "Charisma",
		}[key]
		char.stats[full] = new_val

def _inc(stat_key, char, amount=2):
	# raise the ability score …
	setattr(char.abilities, stat_key, getattr(char.abilities, stat_key) + amount)
	# …and keep char.stats (if it exists) in sync
	if hasattr(char, "stats"):
		full_name = {
			"STR":"Strength", "DEX":"Dexterity", "CON":"Constitution",
			"INT":"Intelligence", "WIS":"Wisdom", "CHA":"Charisma"
		}[stat_key]
		char.stats[full_name] += amount

def raise_to_25(char, key, amount):
	raise_stat(char, key, amount, cap=25)

#add_strength     = lambda c: _inc("STR", c)
#add_dexterity    = lambda c: _inc("DEX", c)
#add_constitution = lambda c: _inc("CON", c)
#add_intelligence = lambda c: _inc("INT", c)
#add_wisdom       = lambda c: _inc("WIS", c)
#add_charisma     = lambda c: _inc("CHA", c)

def add_intelligence(char):	char.abilities.INT += 2
def add_strength(char):		char.abilities.STR += 2
def add_charisma(char):		char.abilities.CHA += 2
def add_wisdom(char):		char.abilities.WIS += 2
def add_constitution(char):	char.abilities.CON += 2
def add_dexterity(char):	char.abilities.DEX += 2

# ---------- Skill boosters --------- #
def add_proficiency_in_stealth(char):
	if "Stealth" not in char.skills.proficiencies:
		char.skills.proficiencies.append("Stealth")

def grant_all_skill_proficiency(char):
	for skill in char.skills.get_all_skills():
		skill.set_proficiency()

def grant_expertise_in_one_skill(char):
	candidates = [skill for skill in char.skills.get_all_skills() if skill.proficiency_level == 1]
	if candidates:
		random.choice(candidates).set_expertise()

# -------- Spell Granting ----------------#

def grant_spell(spell_name, at_will=False, times_per_day=None):
	def _apply(c):
		if hasattr(c, "spells_known"):
			c.spells_known.append(find_spell_by_name(spell_name, c))
	return _apply

# -------- Species' Features ----------------#
def Darkvision( n=60):
	def apply(char):
		if not hasattr(char, "senses"):
			char.senses = {}
		char.senses["darkvision"] = max(char.senses.get("darkvision", 0), n)

	return Feature(
			name= f"Darkvision ({n} ft)",
			apply=apply,
			description=f"You can see in darkness within {n} feet as if it were dim light.",
			source="Species Feature"
			)

def CelestialResistance():
		return Feature(
			name="Celestial Resistance",
			description="You have resistance to radiant and necrotic damage.",
			source="Species Feature"
			)

def HealingHands():
	return Feat(
		name="Healing Hands",
		apply=apply,
		description="You can heal a creature you touch by an amount equal to your level (once per long rest).",
		source="Species Feature"
		)

def LightBearer():
		return Feature(
			name="Light Bearer",
			description="You know the Light cantrip. Charisma is your spellcasting ability for it.",
			source="Species Feature"
		)

#--------- More Feats and Boons ----------#


def set_UnarmoredDefense(char, bonus_stat="CON", isArmor=False, isShield=False):
	from AtlasActorLudi.Map_of_Scores import Modifier
	if char.equipment.get_worn_armor():
		return

	dex_mod   = Modifier(char.abilities.DEX)
	bonus_mod = Modifier(getattr(char.abilities, bonus_stat))

	ac = 10 + dex_mod + bonus_mod
	if char.equipment.is_wearing_shield():
		ac += 2

	char.AC = ac

def UnarmoredDefense(bonus_stat: str, cls_name: str):
	return Feat(
		name="Unarmored Defense",
		apply=lambda c: set_UnarmoredDefense(c, bonus_stat),
		description=f"While not wearing armour, your AC is 10 + DEX mod + "
					f"{bonus_stat} mod. You can still use a shield.",
		source=f"Class: {cls_name}",
		level=1,
		)

def BoonSpellRecall(char):
		stats = {
			"INT": char.abilities.INT,
			"WIS": char.abilities.WIS,
			"CHA": char.abilities.CHA,
			}
		# Get all stats strictly below 20
		candidates = {k: v for k, v in stats.items() if v < 30}
		if not candidates:
			return  # nothing to increase
		# Sort by value descending, take up to 2
		best = sorted(candidates.items(), key=lambda x: -x[1])[:2]
		for key, _ in best:
			setattr(char.abilities, key, getattr(char.abilities, key) + 1)
			# If you keep a .stats dict in sync, also do:
			fullname = {
				"STR":"Strength", "DEX":"Dexterity", "CON":"Constitution",
				"INT":"Intelligence", "WIS":"Wisdom", "CHA":"Charisma"
			}[key]
			if hasattr(char, "stats"):
				char.stats[fullname] += 1

def BoonIrresistibleOffense():
	"""
	Epic boon (PHB ’24 p211).
	"""
	def _apply(char):
		# Pick the higher of STR/DEX that is still < 30; break ties with STR.
		key = "STR" if char.abilities.STR >= char.abilities.DEX else "DEX"
		if getattr(char.abilities, key) < 30:
			raise_stat(char, key, 1, cap=30)

	return Feat(
		name="Boon of Irresistible Offense",
		apply=_apply,
		description=(
			"<b>Ability Score Increase.</b> Increase your Strength or Dexterity "
			"by 1, to a maximum of 30.<br>"
			"<b>Overcome Defenses.</b> Your bludgeoning, piercing, and slashing "
			"damage ignores Resistance.<br>"
			"<b>Overwhelming Strike.</b> When you roll a 20 on an attack roll, "
			"deal extra damage equal to the ability score increased by this boon."
		),
		source="Epic Boon",
		level=19,   # prerequisite
	)

def BuildAvailableFeats(char):
	#if "Elf" in char:
	#	yield Feat("Elvish Precision", ..., ...)
	#if "Monk" in char:
	#	yield Feat("Shadow Walker", ..., ...)
	IsIntelligent = "Wizard" in char or "Eldritch Knight" in char
	IsStrong = "Barbarian" in char or "Fighter" in char or "Paladin" in char or "Ranger" in char
	IsCharismatic = "Warlock" in char or "Sorcerer" in char or "Paladin" in char or "Bard" in char
	IsWise = "Druid" in char or "Monk" in char or "Ranger" in char
	IsDextrous = "Rogue" in char or "Monk" in char or "Fighter" in char or "Ranger" in char

	if char.abilities.STR < 19 and (IsStrong):
		yield Feat("Increased Strength", 		add_strength, 		"You gain +2 Strength.")
	if char.abilities.INT < 19 and (IsIntelligent):
		yield Feat("Increased Intellicence", 	add_intelligence, 	"You gain +2 Intelligence.")
	if char.abilities.CHA < 19 and IsCharismatic:
		yield Feat("Increased Charisma", 		add_charisma, 		"You gain +2 Charisma.")
	if char.abilities.WIS < 19 and IsWise:
		yield Feat("Increased Wisdom", 			add_wisdom, 		"You gain +2 Wisdom.")
	if char.abilities.CON < 19:
		yield Feat("Increased Constitution", 	add_constitution, 	"You gain +2 Constitution.")
	if char.abilities.DEX < 19 and IsDextrous:
		yield Feat("Increased Dexterity", 		add_dexterity, 		"You gain +2 Dexterity.")
	yield Feat("Increased Scores", 		increase_two_highest_below_20, 		"You gain +1 to two Ability Scores.")

def BoonCombatProwess():
	def _apply(c):
		key = _ability_to_increase(c)
		raise_stat(c, key, 1, cap=30)
	return Feat(
		name="Boon of Combat Prowess",
		apply=_apply,
		description=(
			"<b>Ability Score Increase.</b> +1 to any ability (max 30).<br>"
			"<b>Peerless Aim.</b> When you miss with an attack roll, you can "
			"choose to hit instead (usable again at the start of your next turn)."
		),
		source="Epic Boon",
		level=19,
	)

def BoonDimensionalTravel():
	def _apply(c):
		key = _ability_to_increase(c)
		raise_stat(c, key, 1, cap=30)
	return Feat(
		name="Boon of Dimensional Travel",
		apply=_apply,
		description=(
			"<b>Ability Score Increase.</b> +1 to any ability (max 30).<br>"
			"<b>Blink Steps.</b> Immediately after you take the Attack or "
			"Magic action, you can teleport 30 ft to a space you can see."
		),
		source="Epic Boon",
		level=19,
	)

def BoonEnergyResistance():
	def Damages():
		dmg_types = [
		"Acid", "Cold", "Fire", "Lightning", "Necrotic",
		"Poison", "Psychic", "Radiant", "Thunder",
		]
		chosen = random.sample(dmg_types, 2)
		return chosen[1], chosen[0]

	def _apply(c):
		key = _ability_to_increase(c)
		raise_stat(c, key, 1, cap=30)



		# store them so the damage-handling layer can look them up

	dmg1, dmg2 = Damages()
	return Feat(
		name="Boon of Energy Resistance",
		apply=_apply,
		description=(
			"<b>Ability Score Increase.</b> +1 to any ability (max 30).<br>"
			f"<b>Resistances.</b> You have resistance to {dmg1} and {dmg2} damage "
			"you can change the damage type you are resistant to during each Long Rest.<br>"
			"<b>Energy Redirection.</b> When you take one of those damage "
			"types, you can use a Reaction to force a Dex save (DC 8 + CON mod + PB) "
			"on a creature within 60 ft; it takes 2d12 + CON mod damage on a fail."
		),
		source="Epic Boon",
		level=19,
	)

def BoonFate():
	def _apply(c):
		key = _ability_to_increase(c)
		raise_stat(c, key, 1, cap=30)
	return Feat(
		name="Boon of Fate",
		apply=_apply,
		description=(
			"<b>Ability Score Increase.</b> +1 to any ability (max 30).<br>"
			"<b>Improve Fate.</b> When a d20 test succeeds or fails within 60 ft, "
			"roll 2d4 as bonus/penalty. Re-charges on initiative or Short Rest."
		),
		source="Epic Boon",
		level=19,
	)

def BoonFortitude():
	def _apply(char):
		key = _ability_to_increase(char)
		raise_stat(char, key, 1, cap=30)
		# Add +40 to maximum health
		print(char.base_health)
		char.base_health += 40
		print(char.base_health)
	return Feat(
		name="Boon of Fortitude",
		apply=_apply,
		description=(
			"<b>Ability Score Increase.</b> +1 to any ability (max 30).<br>"
			"<b>Fortified Health.</b> HP maximum +40. Whenever you regain HP, "
			"you also regain extra HP equal to your CON modifier "
			"(once per turn)."
		),
		source="Epic Boon",
		level=19,
	)

def BoonSpellRecall():
	def _apply(c):
		# caster gate is enforced by BuildAvailableBoon
		key = random.choice(["INT", "WIS", "CHA"])
		raise_stat(c, key, 1, cap=30)

	return Feat(
		name="Boon of Spell Recall",
		apply=_apply,
		description=(
			"<b>Ability Score Increase.</b> +1 to Int/Wis/Cha (max 30).<br>"
			"<b>Free Casting.</b> When you cast a spell with a 1-4 slot, roll 1d4; "
			"on a match you don’t expend the slot."
		),
		source="Epic Boon",
		level=19,
	)

def BoonRecovery():
	def _apply(c):
		key = _ability_to_increase(c)
		raise_stat(c, key, 1, cap=30)

	return Feat(
		name="Boon of Recovery",
		apply=_apply,
		description=(
			"<b>Ability Score Increase.</b> Increase one ability score of your choice by 1, to a maximum of 30.<br>"
			"<b>Last Stand.</b> When you would be reduced to 0 Hit Points, you can drop to 1 Hit Point instead and regain a number of Hit Points equal to half your Hit Point maximum. Once you use this benefit. "
			"(once per Long Rest).<br>"
			"<b>Recover Vitality.</b> You have a pool of ten d10s. As a Bonus Action, you can expend dice from the pool, roll those dice, and regain a number of Hit Points equal to the roll's total. You regain all the expended dice when you finish a Long Rest."
		),
		source="Epic Boon",
		level=19,
	)

def BoonSkill():
	def _apply(char):
		grant_all_skill_proficiency(char)
		grant_expertise_in_one_skill(char)
		key = _ability_to_increase(char)
		raise_stat(char, key, 1, cap=30)

	return Feat(
		name="Boon of Skill",
		apply=_apply,
		description=(
			"<b>Ability Score Increase.</b> +1 to any ability (max 30).<br>"
			"<b>All-Around Adept.</b> You gain proficiency in all skills.<br>"
			"<b>Expertise.</b> Gain Expertise in one skill of your choice."
		),
		source="Epic Boon",
		level=19,
	)

def BoonSpeed():
	def _apply(c):
		key = _ability_to_increase(c)
		raise_stat(c, key, 1, cap=30)

		c.speed += 30                      # assumes `char.speed` holds walk speed

	return Feat(
		name="Boon of Speed",
		apply=_apply,
		description=(
			"<b>Ability Score Increase.</b> +1 to any ability (max 30).<br>"
			"<b>Escape Artist.</b> As a Bonus Action, you can take the Disengage action, which also ends the Grappled condition on you.<br>"
			"<b>Quickness.</b> Your Speed increases by 30 feet."
		),
		source="Epic Boon",
		level=19,
	)

def BoonNightSpirit():
	def _apply(c):
		key = _ability_to_increase(c)
		raise_stat(c, key, 1, cap=30)

	return Feat(
		name="Boon of the Night Spirit",
		apply=_apply,
		description=(
			"<b>Ability Score Increase.</b> +1 to any ability (max 30).<br>"
			"<b>Merge with Shadows.</b> While within Dim Light or Darkness, you can give yourself the Invisible condition as a Bonus Action. The condition ends on you immediately after you take an action, a Bonus Action, or a Reaction.<br>"
			"<b>Shadowy Form.</b> While within Dim Light or Darkness, you have Resistance to all damage except Psychic and Radiant."
		),
		source="Epic Boon",
		level=19,
	)

def BoonTruesight():
	def _apply(c):
		key = _ability_to_increase(c)
		raise_stat(c, key, 1, cap=30)
		#c.senses.truesight = max(getattr(c.senses, "truesight", 0), 60)
	return Feat(
		name="Boon of Truesight",
		apply=_apply,
		description=(
			"<b>Ability Score Increase.</b> +1 to any ability (max 30).<br>"
			"<b>Truesight.</b> You have Truesight out to 60 ft."
		),
		source="Epic Boon",
		level=19,
	)

# ------------- Selector ------------
def ApplyRandomFeats(char, n=1):
	print("Random Feat!")
	available = list(BuildAvailableFeats(char))
	chosen = random.sample(available, n)
	for feat in chosen:
		feat(char)   # apply .apply() mutation
	return chosen

def BuildAvailableBoon(char):
	"""Yield every epic boon the character is eligible for."""
	# Spell-casters keep their old special-case
	if "Wizard" in char:
		yield BoonSpellRecall()
		yield BoonDimensionalTravel()
	if "Fighter" in char:
		yield BoonIrresistibleOffense()
		yield BoonCombatProwess()
		yield BoonEnergyResistance()
		yield BoonFortitude()
		yield BoonRecovery()
		yield BoonNightSpirit()
		if "Eldritch Knight" in char:
			yield BoonSpellRecall()
			yield BoonDimensionalTravel()
	if 'Rogue' in char:
		yield BoonIrresistibleOffense()
		yield BoonCombatProwess()
		yield BoonDimensionalTravel()
		yield BoonNightSpirit()
	if 'Cleric' in char:
		yield BoonIrresistibleOffense()
		yield BoonCombatProwess()
		yield BoonFortitude()
		yield BoonRecovery()
		yield BoonSpellRecall()
		yield BoonNightSpirit()
	if 'Ranger' in char:
		yield BoonIrresistibleOffense()
		yield BoonCombatProwess()
		yield BoonDimensionalTravel()
		yield BoonRecovery()
		yield BoonNightSpirit()
	if 'Paladin' in char:
		yield BoonIrresistibleOffense()
		yield BoonCombatProwess()
		yield BoonEnergyResistance()
		yield BoonFortitude()
		yield BoonRecovery()
		yield BoonSpellRecall()
		yield BoonNightSpirit()
	if 'Bard' in char:
		yield BoonCombatProwess()
		yield BoonDimensionalTravel()
		yield BoonSpellRecall()
		yield BoonNightSpirit()
	if 'Monk' in char:
		yield BoonIrresistibleOffense()
		yield BoonCombatProwess()
		yield BoonDimensionalTravel()
		yield BoonEnergyResistance()
		yield BoonFortitude()
		yield BoonRecovery()
		yield BoonNightSpirit()
	if 'Druid' in char:
		yield BoonCombatProwess()
		yield BoonDimensionalTravel()
		yield BoonEnergyResistance()
		yield BoonRecovery()
		yield BoonSpellRecall()
		yield BoonNightSpirit()
	if 'Warlock' in char:
		yield BoonCombatProwess()
		yield BoonDimensionalTravel()
		yield BoonEnergyResistance()
		yield BoonRecovery()
		yield BoonNightSpirit()
	if 'Sorcerer' in char:
		yield BoonDimensionalTravel()
		yield BoonSpellRecall()
		yield BoonNightSpirit()
	if 'Barbarian' in char:
		yield BoonIrresistibleOffense()
		yield BoonEnergyResistance()
		yield BoonFortitude()
		yield BoonRecovery()
		yield BoonNightSpirit()

	yield BoonFate()
	yield BoonSkill()
	yield BoonSpeed()
	yield BoonTruesight()

def ApplyEpicBoon(char, n=1):
	print("Epic Boom!")
	available = list(BuildAvailableBoon(char))
	chosen = random.sample(available, n)
	for boon in chosen:
		boon(char)
		char.features.append(boon)
	return chosen

def Fighting_Styles(char=None):

	styles = {
	"Archery":
		"You gain a +2 bonus to attack rolls you make with Ranged weapons.",
	"Blind Fighting":
		"You have Blindsight with a range of 10 feet.",
	"Defense":
		"While you're wearing Light, Medium, or Heavy armor, you gain a +1 bonus to Armor Class.",
	"Dueling":
		"When you're holding a Melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.",
	"Great Weapon Fighting":
		"When you roll damage for an attack you make with a Melee weapon that you are holding with two hands, you can treat any 1 or 2 on a damage die as a 3. The weapon must have the Two-Handed or Versatile property to gain this benefit.",
	"Interception":
		"When a creature you can see hits another creature within 5 feet of you with an attack roll, you can take a Reaction to reduce the damage dealt to the target by 1d10 plus your Proficiency Bonus. You must be holding a Shield or a Simple or Martial weapon to use this Reaction.",
	"Protection":
		"When a creature you can see attacks a target other than you that is within 5 feet of you, you can take a Reaction to interpose your Shield if you're holding one. You impose Disadvantage on the triggering attack roll and all other attack rolls against the target until the start of your next turn if you remain within 5 feet of the target.",
	"Thrown Weapon Fighting":
		"When you hit with a ranged attack roll using a weapon that has the Thrown property, you gain a +2 bonus to the damage roll.",
	"Two-Weapon Fighting":
		"When you make an extra attack as a result of using a weapon that has the Light property, you can add your ability modifier to the damage of that attack if you aren't already adding it to the damage.",
	"Unarmed Fighting":
		"When you hit with your Unarmed Strike and deal damage, you can deal Bludgeoning damage equal to 1d6 plus your Strength modifier instead of the normal damage of an Unarmed Strike. If you aren't holding any weapons or a Shield when you make the attack roll, the d6 becomes a d8. At the start of each of your turns, you can deal 1d4 Bludgeoning damage to one creature Grappled by you."
		}
	# Only Rangers get access to Druidic Warrior:
	if char and "Ranger" in char:
		from AtlasLusoris.Grimoire_of_Spellcasters import SPELL_LISTS
		# pick two distinct druid cantrips:
		druid_cantrips = SPELL_LISTS["Druid"][0]
		chosen = random.sample(druid_cantrips, k=2)

		# render them as HTML blocks:
		cantrip_html = "".join(f"<div class='npc-textbox'>{c}</div>" for c in chosen)

		styles["Druidic Warrior"] = (
			"You learn two cantrips of your choice from the druid spell list. "
			"They count as Ranger spells for you, and Wisdom is your spellcasting ability for them."
			+ cantrip_html
			)
		if char.level >= 18: styles.pop("Blind Fighting", None)

	return styles


	if char and "Ranger" in char:
		print("ENTER RANGER DRUIDIC WARRIOR")

		druid_cantrips: list[Spell] = SPELL_LISTS["Druid"][0][:]
		chosen: list[Spell] = random.sample(druid_cantrips, 2)

		if hasattr(char, "spells_known"):
			for sp in chosen:
				if sp not in char.spells_known:
					char.spells_known.append(sp)

		# Build pretty HTML blocks for the sheet
		html_blocks = "".join(f"<div class='npc-textbox'>{sp}</div>" for sp in chosen)

		result["Druidic Warrior"] = (
			"You learn two druid cantrips (shown below). They count as Ranger "
			"spells for you, and Wisdom is your spell-casting ability for them."
			f"{html_blocks}"
		)

	return result

def character_fighting_styles(char):
	"""Return a set of fighting style names the character already has."""
	style_names = set()
	for feat in getattr(char, "features", []):
		if getattr(feat, "name", "") in Fighting_Styles(char):
			style_names.add(feat.name)
	return style_names

def add_new_fighting_style(char):
	# Find styles not possessed yet
	owned = character_fighting_styles(char)
	available = [name for name in Fighting_Styles(char) if name not in owned]
	if not available:
		print("No new fighting styles to grant!")
		return None
	chosen = random.choice(available)
	feat = Feat(
		name=chosen,
		apply=lambda c: None,  # No mutation needed, pure feature
		description=Fighting_Styles(char)[chosen],
		source="Fighting Style"
	)
	# Add to features list
	char.features.append(feat)
	print(f"Gained Fighting Style: {chosen}")
	return feat


# ── Weapon-Mastery properties (PHB ’24, p. 214) ───────────────────────────
def Weapon_Masteries():
	return {
		"Weapon Mastery: Cleave":
			"""After you hit, you may make one extra melee attack
			against a second creature
			within 5 ft of the first (once per turn, no ability-mod
			to damage).""",
		"Weapon Mastery: Graze":
			"""If your attack roll misses, the target still
			takes damage equal to the
			ability modifier you used for the attack.""",
		"Weapon Mastery: Nick":
			"""The Light-property extra attack can be made
			during the Attack action instead
			of as a Bonus Action (once per turn).""",
		"Weapon Mastery: Push":
			"""On a hit you may push the target
			(Large or smaller) up to 10 ft
			 straight away.""",
		"Weapon Mastery: Sap":
			"""On a hit the target has
			Disadvantage on its next attack
			roll before your next turn.""",
		"Weapon Mastery: Slow":
			"""On a hit the target’s speed
			is reduced by 10 ft until the
			 start of your next turn.""",
		"Weapon Mastery: Topple":
			"""On a hit you may force a CON save
			(DC 8 + ability-mod + PB);
			on a fail the target falls Prone.""",
		"Weapon Mastery: Vex":
			"""On a hit you have Advantage on your next attack roll
			against that creature before the end of your next turn.""",
	}

def character_weapon_masteries(char):
	"""Return the set of Weapon-Mastery names the character already has."""
	owned = set()
	for feat in getattr(char, "features", []):
		if feat.name in Weapon_Masteries():
			owned.add(feat.name)
	return owned

def add_new_weapon_mastery(char):
	"""
	Give the character ONE random Weapon-Mastery property they don’t yet own.
	Returns the `Feat` object, or `None` if no masteries remain.
	"""
	owned     = character_weapon_masteries(char)
	available = [name for name in Weapon_Masteries() if name not in owned]
	if not available:
		print("No new weapon masteries to grant!")
		return None

	name = random.choice(available)
	feat = Feat(
		name=name,
		apply=lambda c: None,                          # pure feature, no mutation
		description=Weapon_Masteries()[name],
		source="Weapon Mastery",
	)
	char.features.append(feat)
	print(f"Gained Weapon Mastery: {name}")
	return feat

def _raise_stat(char, key: str, amount: int = 4):
	"""Increase char.abilities.KEY by <amount>, capping at 25."""
	new_val = min(getattr(char.abilities, key) + amount, 25)
	setattr(char.abilities, key, new_val)

	# keep char.stats dict (if present) in sync
	if hasattr(char, "stats"):
		full = {
			"STR": "Strength",
			"DEX": "Dexterity",
			"CON": "Constitution",
			"INT": "Intelligence",
			"WIS": "Wisdom",
			"CHA": "Charisma",
		}[key]
		char.stats[full] = new_val

def PrimalChampionFeat():
	return Feat(
		name="Primal Champion",
		apply=lambda c: (_raise_stat(c, "STR"), _raise_stat(c, "CON")),
		description="Strength and Constitution each increase by 4, up to a maximum of 25.",
		source="Class: Barbarian",
		level=20,
	)

def BodyAndMindFeat():
	"""
	Monk 20th-level capstone: Increase Dexterity and Wisdom by 4, to a maximum of 25.
	"""
	def _apply(char):
		print(f"Before Body and Mind: DEX={char.abilities.DEX}, WIS={char.abilities.WIS}")
		raise_stat(char, "DEX", 4, cap=25)
		raise_stat(char, "WIS", 4, cap=25)
		print(f"After Body and Mind: DEX={char.abilities.DEX}, WIS={char.abilities.WIS}")
	return Feat(
		name="Body and Mind",
		apply=_apply,
		description="You have developed your body and mind to new heights. "
					"Your Dexterity and Wisdom scores increase by 4, to a maximum of 25.",
		source="Class: Monk",
		level=20,
	)

# Ratial Features
def HealingHands():
	def apply(char):
		def heal():
			amount = char.level  # or use Proficiency Bonus if using new rules
			print(f"{char.name} uses Healing Hands to heal for {amount} HP.")
			return amount
		char.healing_hands = heal

	return Feat(
		name="Healing Hands",
		apply=apply,
		description="You can heal a creature for an amount equal to your level. Usable once per long rest.",
		source="Species Feature"
	)

def CelestialResistance():
	def apply(char):
		if not hasattr(char, "resistances"):
			char.resistances = set()
		char.resistances.update(["radiant", "necrotic"])

	return Feat(
		name="Celestial Resistance",
		apply=apply,
		description="You have resistance to radiant and necrotic damage.",
		source="Species Feature"
	)

def LightBearer():
	def apply(char):
		if not hasattr(char, "cantrips"):
			char.cantrips = []
		char.cantrips.append({
			"name": "Light",
			"casting_stat": "CHA",
			"source": "Species Feature"
		})

	return Feat(
		name="Light Bearer",
		apply=apply,
		description="You know the *Light* cantrip. Charisma is your spellcasting ability.",
		source="Species Feature"
	)


from dataclasses import dataclass, field
from typing import Callable, Optional, Any

@dataclass
class Invocation(Feature):
	condition: Optional[Callable[[Any], bool]] = None
	pact_required: Optional[str] = None
	apply: Callable[[Any], None] = field(default_factory=lambda: (lambda c: None))  # Always a no-op by default

	def __init__(
		self,
		name: str,
		level: int = 2,
		description: str = "",
		source: str = "Warlock Invocation",
		condition: Optional[Callable[[Any], bool]] = None,
		pact_required: Optional[str] = None,
		apply: Optional[Callable[[Any], None]] = None,
	):
		super().__init__(name, level, description, source)
		self.condition = condition
		self.pact_required = pact_required
		# Always a callable; avoids bugs!
		self.apply = apply if apply is not None else (lambda c: None)

	def is_valid_for(self, character) -> bool:
		if self.condition and not self.condition(character):
			return False
		if self.pact_required and self.pact_required != getattr(character, "pact", None):
			return False
		return True

	def __call__(self, character):
		# Will never crash: always a callable!
		self.apply(character)

	def __str__(self):
		return self.html()

	def html(self):
		s = f"""<div class="npc-textbox" style="grid-column: span 1;">"""
		s += f"""<h2 style="font-family: 'Iglesia'; font-size: 2.1em;">{self.name}</h2>"""
		#s += f" <sub>{self.source}</sub>" if self.source else ""
		s += f"<br><i>{self.description}</i>"
		s = f"""</div>"""
		return s

def InvAgonizingBlast():
	return Invocation(
		name="Agonizing Blast",
		level=2,
		description=(
			"Choose one of your known Warlock cantrips that deals damage. "
			"You can add your Charisma modifier to that spell's damage rolls."
		),
		condition=lambda c: getattr(c, "level", 0) >= 2 and "Warlock" in c.char_class,
		apply=None  # Just a feature for the sheet
	)

def InvArmorOfShadows():
	from AtlasMagia.Lodge_of_Spells import MageArmor
	return Invocation(
		name="Armor of Shadows",
		level=2,
		description= f"""
			You can cast Mage Armor on yourself at will, without expending a spell slot.
			<div class="npc-textbox">{MageArmor}</div>
			""",
		condition=lambda c: "Warlock" in c.char_class,
		apply=grant_spell("Mage Armor", at_will=True)
	)

def InvAscendantStep():
	from AtlasMagia.Lodge_of_Spells import Levitate
	return Invocation(
		name="Ascendant Step",
		level=5,
		description=f"""You can cast Levitate on yourself at will, no slot. <div class="npc-textbox">{Levitate}</div>""",
		condition=lambda c: getattr(c, "level", 0) >= 5 and "Warlock" in c.char_class,
		apply=lambda c: None
	)

def InvDevilsSight():
	def apply(c):
		# For printout, set the character's darkvision/range if relevant
		if hasattr(c, "senses"):
			pass
	return Invocation(
		name="Devil's Sight",
		level=2,
		description=(
			"You can see normally in darkness (magical and nonmagical) to a range of 120 feet."
		),
		condition=lambda c: getattr(c, "level", 0) >= 2 and "Warlock" in c.char_class,
		apply=apply,
	)

def InvFiendishVigor():
	from AtlasMagia.Lodge_of_Spells import FalseLife
	return Invocation(
		name="Fiendish Vigor",
		level=2,
		description= f"""
			You can cast False Life on yourself at will. Always max HP on False Life.<br> <div class="npc-textbox">{FalseLife}</div>
			""",
		condition=lambda c: getattr(c, "level", 0) >= 2 and "Warlock" in c.char_class,
		apply=lambda c: None
	)

def InvEldritchMind():
	return Invocation(
		name="Eldritch Mind",
		level=2,
		description="You have advantage on Constitution saving throws you make to maintain concentration on a spell.",
		condition=lambda c: "Warlock" in c.char_class,
		apply=lambda c: None,  # No mutation, just a sheet feature
	)

def InvPactOfTheBlade():
	return Invocation(
		name="Pact of the Blade",
		level=2,
		description="Conjure/bond a pact weapon as a bonus action; use CHA for attack/damage.",
		condition=lambda c: "Warlock" in c.char_class,
		pact_required="Blade",
		apply=lambda c: None
	)

def InvPactOfTheChain():
	return Invocation(
		name="Pact of the Chain",
		level=2,
		description="Learn Find Familiar; cast at will; access special forms.",
		condition=lambda c: "Warlock" in c.char_class,
		pact_required="Chain",
		apply=lambda c: None
	)

def InvPactOfTheTome():
	return Invocation(
		name="Pact of the Tome",
		level=2,
		description="Book of Shadows (3 cantrips + 2 ritual spells from any list, not already prepared).",
		condition=lambda c: "Warlock" in c.char_class,
		pact_required="Tome",
		apply=lambda c: None
	)


def BuildAvailableInvocations(char):
	# Return all invocations char qualifies for
	invocations = [
		InvAgonizingBlast(),
		InvArmorOfShadows(),
		InvAscendantStep(),
		InvDevilsSight(),
		InvFiendishVigor(),
		InvEldritchMind(),
		InvPactOfTheBlade(),
		InvPactOfTheChain(),
		InvPactOfTheTome(),
		]
	for inv in invocations:
		if inv.is_valid_for(char):
			yield inv






# Blueprints
# ---- General Pattern for Features/Boons ----
def generic_stat_boost_boon(name, desc):
	def _apply(char):
		key = _ability_to_increase(char)
		raise_stat(char, key, 1, cap=30)
	return Feat(
		name=name,
		apply=_apply,
		description=desc,
		source="Epic Boon",
		level=19,
	)


def Lucky():
	def apply(char):
		char.luck_points = char.proficiency_bonus

		def regain_luck():
			char.luck_points = char.proficiency_bonus
			Inform(f"{char.name} regains Luck Points ({char.luck_points}) after a Long Rest.")

		char.regain_luck = regain_luck

		def use_luck_for_advantage():
			if char.luck_points > 0:
				char.luck_points -= 1
				Inform(f"{char.name} uses a Luck Point for Advantage. ({char.luck_points} left)")
				return True
			Warning(f"{char.name} has no Luck Points left!")
			return False

		def use_luck_for_disadvantage():
			if char.luck_points > 0:
				char.luck_points -= 1
				Inform(f"{char.name} uses a Luck Point to impose Disadvantage. ({char.luck_points} left)")
				return True
			Warning(f"{char.name} has no Luck Points left!")
			return False

		# Attach methods to the character object
		char.use_luck_for_advantage = use_luck_for_advantage
		char.use_luck_for_disadvantage = use_luck_for_disadvantage

	return Feat(
		name="Lucky",
		apply=apply,
		description=(
			"You have inexplicable luck that seems to kick in at just the right moment.<br>"
			"<b>Luck Points.</b> You have Luck Points equal to your Proficiency Bonus. "
			"You regain expended Luck Points after a Long Rest.<br>"
			"<b>Advantage.</b> When you roll a d20 Test, spend 1 Luck Point to roll with Advantage.<br>"
			"<b>Disadvantage.</b> When a creature rolls an attack against you, spend 1 Luck Point to impose Disadvantage."
		),
		source="Background",
		level=1,
	)


def DwarvenResilience():
	return Feat(
		name="Dwarven Resilience",
		description="You have resistance to poison damage and advantage on saving throws against poison.",
		apply=lambda c: (
			c.resistances.add("poison"),
			c.saving_throws.add_advantage_against("poison") if hasattr(c.saving_throws, "add_advantage_against") else None
		),
		source="Species Feature"
	)

def DwarvenToughness():
	return Feature(
		name="Dwarven Toughness",
		description="Your hit point maximum increases by 1, and it increases by 1 every time you gain a level.",
		apply=lambda c: setattr(c, "dwarven_toughness", True),  # Track for level-ups
		source="Species Feature"
	)

def DwarvenWeaponTraining():
	return Feature(
		name="Dwarven Weapon Training",
		description="You have proficiency with the battleaxe, handaxe, light hammer, and warhammer.",
		apply=lambda c: [
			c.skills.Battleaxe.set_proficiency(),
			c.skills.Handaxe.set_proficiency(),
			c.skills.Light_Hammer.set_proficiency(),
			c.skills.Warhammer.set_proficiency()
		],
		source="Species Feature"
	)

def GnomishCunning():
	return Feature(
		name="Gnomish Cunning",
		description="You have advantage on INT, WIS, and CHA saving throws.",
		source="Species Feature"
		)

def ForestGnomeLineage():
	def apply(char):
		if not hasattr(char, "cantrips"):
			char.cantrips = []
		if not hasattr(char, "spells_known"):
			char.spells_known = []
		char.cantrips.append({
			"name": "Minor Illusion",
			"casting_stat": "INT",
			"source": "Species Feature"
		})
		char.spells_known.append({
			"name": "Speak with Animals",
			"casting_stat": "INT",
			"uses_per_day": char.proficiency_bonus,
			"source": "Species Feature"
		})

	return Feature(
		name="Forest Gnome Lineage",
		apply=apply,
		description="You know the <b>Minor Illusion</b> cantrip. You can cast <b>Speak with Animals</b> a number of times per long rest equal to your proficiency bonus. You can cast it without a spell slot a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest. You can also use any spell slots you have to cast the spell.",
		source="Species Lineage"
	)

def RockGnomeLineage():
	def apply(char):
		if not hasattr(char, "cantrips"):
			char.cantrips = []
		char.cantrips.extend([
			{"name": "Mending", "casting_stat": "INT", "source": "Species Feature"},
			{"name": "Prestidigitation", "casting_stat": "INT", "source": "Species Feature"}
		])
		char.features.append(Feature(
			name="Tinker",
			description="You can craft tiny clockwork devices with magical effects (e.g., music box, lighter, toy).",
			source="Species Feature"
		))

	return Feature(
		name="Rock Gnome Lineage",
		apply=apply,
		description="You know the *Mending* and *Prestidigitation* cantrips. You can create magical clockwork devices. Intelligence is your spellcasting ability.",
		source="Species Lineage"
	)
