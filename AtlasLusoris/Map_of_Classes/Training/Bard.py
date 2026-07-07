from ..Grimoire_of_Health  import roll_health, HIT_DIE_TABLE
from ..Codex_of_Progression import Progression

from AtlasActorLudi.Map_of_Scores import PB, Modifier
try:
	from AtlasLusoris.Map_of_Classes import subclasses
except ImportError:
	subclasses = {"Bard": ["Lore"]}   # graceful fallback
from AtlasLusoris.Grimoire_of_Features import (
	Feature,
	SilentFeature,
	ApplyRandomFeats,
	ApplyEpicBoon)

sc = {"Dance",	"Glamour",		"Lore",	 "Valor"}

class Bard(Progression):
	HIT_DIE = 8

	@staticmethod
	def bardic_die_for_level(lvl: int) -> str:
		"""Return the Bardic Inspiration die string for the given level."""
		if lvl >= 15:
			return "d12"
		if lvl >= 10:
			return "d10"
		if lvl >= 5:
			return "d8"
		return "d6"

	def features(self, character):
		level = character.level
		lvl = level

		if not character.subclass:
			character.subclass = choice(subclasses.get("Bard", ["Lore"]))
		college = character.subclass

		cha_mod    = Modifier(character.abilities.CHA)

		feats = []

		def _grant_expertise(n:int):
			return lambda c: c.skills.activate_expertise(
				n, c.skills.get_proficient_skills()
				)

		def _jack_of_all_trades(c):
			c.skills.activate_jack_of_all_trades()

		# Level 1
		bardic_rest = "Long"
		if level >= 15:
			bardic_die = "d12"
		elif level >= 10:
			bardic_die = "d10"
		elif level >= 5:
			bardic_die = "d8"
			bardic_rest = "Short"
		else:
			bardic_die = "d6"
		N_Dice = max(1,Modifier(character.abilities.CHA))

		if "Dance" in college:
			if level >= 3:
				feats.append(Feature("College of Dance",
					"""
					Bards of the College of Dance know that the Words of Creation can't be contained within speech or song; the words are uttered by the movements of celestial bodies and flow through the motions of the smallest creatures. These Bards practice a way of being in harmony with the whirling cosmos that emphasizes agility, speed, and grace.
					"""
					))
				feats.append(Feature("Dazzling Footwork",
					"""
					While you aren't wearing armor or wielding a Shield, you gain the following benefits.
					 <ul style="list-style-type: '🪭'; text-align: left; ">
						<li> <b>Dance Virtuoso.</b> You have Advantage on any Charisma (Performance) check you make that involves you dancing.</li>
						<li> <b> Unarmored Defense.</b> Your base Armor Class equals 10 plus your Dexterity and Charisma modifiers.</li>
						<li> <b> Agile Strikes.</b> When you expend a use of your Bardic Inspiration as part of an action, a Bonus Action, or a Reaction, you can make one Unarmed Strike as part of that action, Bonus Action, or Reaction.</li>
						<li> <b> Bardic Damage.</b> You can use Dexterity instead of Strength for the attack rolls of your Unarmed Strikes. When you deal damage with an Unarmed Strike, you can deal Bludgeoning damage equal to a roll of your Bardic Inspiration die plus your Dexterity modifier, instead of the strike's normal damage. This roll doesn't expend the die.</li>
						</ul>
					"""
					))
				dex = Modifier(character.abilities.DEX)
				cha = Modifier(character.abilities.CHA)
				character.AC = 10 + dex + cha
				character.no_shield = True
				character.no_armor = True
			if level >= 6:
				feats.append(Feature("Inspiring Movement",
					"""
					When an enemy you can see ends its turn within 5 feet of you,
					you can take a Reaction and expend one use of your
					Bardic Inspiration to move up to half your Speed. Then
					one ally of your choice within 30 feet of you can also
					move up to half their Speed using their Reaction.
					<br>
					None of this feature's movement provokes Opportunity Attacks.
					"""
					))
				feats.append(Feature("Tandem Footwork",
					"""
					When you roll Initiative, you can expend one use of your
					Bardic Inspiration if you don't have the Incapacitated
					condition. When you do so, roll your Bardic Inspiration
					die; you and each ally within 30 feet of you who can
					see or hear you gains a bonus to Initiative equal to
					the number rolled.
					"""
					))
			if level >= 14:
				feats.append(Feature("Leading Evasion",
					"""<p>
					When you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw and only half damage if you fail. If any creatures within 5 feet of you are making the same Dexterity saving throw, you can share this benefit with them for that save.
					<br>
					You can't use this feature if you have the Incapacitated condition.
					</p>"""
					))
		if "Glamour" in college:
			if level >= 3:
				feats.append(Feature("College of Glamour",
					"""
					The College of Glamour traces its origins to the beguiling magic of
					the Feywild. Bards who study this magic weave threads of beauty and
					terror into their songs and stories, and the mightiest among them
					can cloak themselves in otherworldly majesty. Their performances
					stir up wistful longing for forgotten innocence, evoke unconscious
					memories of long-held fears, and tug at the emotions of even the
					most hard-hearted listeners.
					"""
					))
				from AtlasMagia.Lodge_of_Spells import CharmPerson, MirrorImage
				feats.append(Feature("Beguiling Magic",
					f"""
You always have the Charm Person and Mirror Image spells prepared.
<br>
In addition, immediately after you cast an Enchantment or Illusion spell
using a spell slot, you can cause a creature you can see within 60 feet
of yourself to make a Wisdom saving throw against your spell save DC. On
a failed save, the target has the Charmed or Frightened condition (your
choice) for 1 minute. The target repeats the save at the end of each of
its turns, ending the effect on itself on a success.
<br>
Once you use this benefit, you can't use it again until you finish a
Long Rest. You can also restore your use of it by expending one use
of your Bardic Inspiration (no action required).
<div class="npc-textbox">{CharmPerson}</div>
<div class="npc-textbox">{MirrorImage}</div>
					"""
					))
				feats.append(Feature("Mantle of Inspiration",
					f"""
You can weave fey magic into a song or dance to fill others with vigor.
As a Bonus Action, you can expend a use of Bardic Inspiration, rolling
a Bardic Inspiration die. When you do so, choose a number of other
creatures within 60 feet of yourself, up to a number equal to your
Charisma modifier (minimum of one creature). Each of those creatures
gains a number of Temporary Hit Points equal to two times the number
rolled on the Bardic Inspiration die, and then each can use its
Reaction to move up to its Speed without provoking Opportunity Attacks.
					"""
					))
			if level >= 6:
				from AtlasMagia.Lodge_of_Spells import Command
				feats.append(Feature("Mantle of Majesty",
					f"""
You always have the Command spell prepared.
<div class="npc-textbox">{Command}</div>
As a Bonus Action, you cast Command without expending a spell slot, and
you take on an unearthly appearance for 1 minute or until your
Concentration ends. During this time, you can cast Command as a
Bonus Action without expending a spell slot.
<br>
Any creature Charmed by you automatically fails its saving throw
against the Command you cast with this feature.
<br>
Once you use this feature, you can't use it again until you finish a
Long Rest. You can also restore your use of it by expending a level
3+ spell slot (no action required).
					"""
					))
			if level >= 14:
				feats.append(Feature("Unbreakable Majesty",
					f"""
As a Bonus Action, you can assume a magically majestic presence for
1 minute or until you have the Incapacitated condition. For the
duration, whenever any creature hits you with an attack roll for the
first time on a turn, the attacker must succeed on a Charisma saving
throw against your spell save DC, or the attack misses instead, as
the creature recoils from your majesty.
<br>
Once you assume this majestic presence, you can't do so again until
you finish a Short or Long Rest.
					"""
					))
		if "Lore" in college:
			if level >= 3:
				feats.append(Feature("College of Lore",
					"""
Bards of the College of Lore collect spells and secrets from diverse sources, such as scholarly tomes, mystical rites, and peasant tales. The college's members gather in libraries and universities to share their lore with one another. They also meet at festivals or affairs of state, where they can expose corruption, unravel lies, and poke fun at self-important figures of authority.
					"""
					))
				character.skills.activate_proficiencies(3, character.skills.get_all_skills())
				feats.append(Feature("Cutting Words",
					"""
You learn to use your wit to supernaturally distract, confuse, and otherwise sap the confidence and competence of others. When a creature that you can see within 60 feet of yourself makes a damage roll or succeeds on an ability check or attack roll, you can take a Reaction to expend one use of your Bardic Inspiration; roll your Bardic Inspiration die, and subtract the number rolled from the creature's roll, reducing the damage or potentially turning the success into a failure.
					"""
					))
			if level >= 6:
				feats.append(Feature("Magical Discoveries",
					"""
You learn two spells of your choice. These spells can come from the Cleric, Druid, or Wizard spell list or any combination thereof (see a class's section for its spell list). A spell you choose must be a cantrip or a spell for which you have spell slots, as shown in the Bard Features table.
<br>
You always have the chosen spells prepared, and whenever you gain a Bard level, you can replace one of the spells with another spell that meets these requirements.
					"""
					))
			if level >= 14:
				feats.append(Feature("Peerless Skill",
					"""
When you make an ability check or attack roll and fail, you can expend one use of Bardic Inspiration; roll the Bardic Inspiration die, and add the number rolled to the d20, potentially turning a failure into a success. On a failure, the Bardic Inspiration isn't expended.
					"""
					))
		if "Valor" in college:
			if level >= 3:
				feats.append(Feature("College of Valor",
					"""
Bards of the College of Valor are daring storytellers whose tales preserve the memory of the great heroes of the past. These Bards sing the deeds of the mighty in vaulted halls or to crowds gathered around great bonfires. They travel to witness great events firsthand and to ensure that the memory of these events doesn't pass away. With their songs, they inspire new generations to reach the same heights of accomplishment as the heroes of old.
					"""
					))
				feats.append(Feature("Combat Inspiration",
					"""
You can use your wit to turn the tide of battle. A creature that has a Bardic Inspiration die from you can use it for one of the following effects.
<br>
<b>Defense.</b> When the creature is hit by an attack roll, that creature can use its Reaction to roll the Bardic Inspiration die and add the number rolled to its AC against that attack, potentially causing the attack to miss.
<br>
<b>Offense.</b>  Immediately after the creature hits a target with an attack roll, the creature can roll the Bardic Inspiration die and add the number rolled to the attack's damage against the target.
					"""
					))
				feats.append(Feature("Martial Training",
					"""
					You gain proficiency with Martial weapons and training with Medium armor and Shields.

					In addition, you can use a Simple or Martial weapon as a Spellcasting Focus to cast spells from your Bard spell list.
					"""
					))
				character.skills.Medium.set_proficiency()
				character.skills.Shields.set_proficiency()
				character.skills.Martial_Weapons.set_proficiency()
			if level >= 6:
				feats.append(Feature("College of Valor",
					"""
You can attack twice instead of once whenever you take the Attack action on your turn.
<br>
In addition, you can cast one of your cantrips that has a casting time of an action in place of one of those attacks.
					"""
					))
			if level >= 6:
				feats.append(Feature("Battle Magic",
					"""
After you cast a spell that has a casting time of an action, you can make one attack with a weapon as a Bonus Action.
					"""
					))

		if level >= 1:
			die  = self.bardic_die_for_level(lvl)
			uses = max(1, cha_mod)
			feats.append(Feature(
				"Bardic Inspiration",
				f"""You can supernaturally inspire others through your art.
				This inspiration is represented by your Bardic Inspiration die, which is a {bardic_die}. <br>
				<b>Using Bardic Inspiration.</b> As a Bonus Action, you can inspire another creature within 60 feet of yourself who can see or hear you.
				That creature gains one of your Bardic Inspiration dice.
				A creature can have only one Bardic Inspiration die at a time. <br>
				Once within the next hour when the creature fails a D20 Test, the creature
				can roll the Bardic Inspiration die and add the number rolled to the d20,
				potentially turning the failure into a success. A Bardic Inspiration die is
				expended when it's rolled. <br>
				<b>Number of Uses: {uses}</b> You can confer a total of <b>{uses}</b> Bardic Inspiration die.
				You regain all expended uses when you finish a {bardic_rest} Rest.
				""",
				apply=lambda c: (
					setattr(c, "bardic_inspiration_die", bardic_die),
					setattr(c, "bardic_inspiration_uses", uses)
					)))

		# Level 2
		if level >= 2:
			roll_health(self.char)

			f = SilentFeature(
				"Expertise",
				"Choose two proficient skills; your proficiency bonus is doubled.",
				apply=_grant_expertise(2)
				)
			feats.append(f)

			f = SilentFeature(
				"Jack of All Trades",
				"Add half your proficiency bonus to any ability check you’re not proficient in.",
				apply=_jack_of_all_trades
				)
			feats.append(f)

		# ────────────────────────────────
		# Level 4, 8, 12, 16, 19: Your normal ASI/Feat progression
		# ────────────────────────────────
		if lvl >= 4:	feats.extend(ApplyRandomFeats(character, n=1))
		if lvl >= 8:	feats.extend(ApplyRandomFeats(character, n=1))
		if lvl >= 12:	feats.extend(ApplyRandomFeats(character, n=1))
		if lvl >= 16:	feats.extend(ApplyRandomFeats(character, n=1))
		if lvl >= 19:	feats.extend(ApplyRandomFeats(character, n=1))

		if lvl >= 5:
			feats.append(SilentFeature(
				"Font of Inspiration",
				"You regain all Bardic Inspiration uses when you finish a Short or Long Rest.",
				apply=lambda c: setattr(c, "bardic_inspiration_font", True)
				))

		if lvl >= 7:
			feats.append(Feature(
				"Countercharm",
				"Action: perform to give allies advantage on saves vs. being frightened or charmed (within 30 ft)."
				))

		if lvl >= 9:
			feats.append(Feature("Song of Rest d8", "Healed allies regain an extra 1d8 HP on a Short Rest."))
			f = SilentFeature(
				"Expertise",
				"Choose two proficient skills; your proficiency bonus is doubled.",
				apply=_grant_expertise(2)
				)
			f.__str__ = lambda self=f: ""
			feats.append(f)

		if lvl >= 19:
			feats.append(Feature(
				"Superior Inspiration",
				"If you roll initiative with no Bardic Inspiration dice left, you regain **one die**."
				))

		# Level 20
		if level >= 20:	feats.extend(ApplyEpicBoon(character, n=1))



		return feats
