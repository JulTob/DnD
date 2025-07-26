from ..Grimoire_of_Health  import roll_health, HIT_DIE_TABLE
from ..Codex_of_Progression import Progression

from AtlasLusoris.Grimoire_of_Features import Feature, ApplyRandomFeats
import random


class Druid(Progression):
	HIT_DIE = 8

	def features(self, character):
		feats: List[Feature] = []
		level = character.Level
		pb = character.proficiency_bonus
		subclass = character.Subclass or choice(subclasses["Druid"])
		if level >= 2:
			roll_health(self.char)

		if level >= 1:
			feats.append(Feature("Druidic",
				"""You know Druidic, the secret language of Druids. While learning this ancient tongue, you also unlocked the magic of communicating with animals; you always have the Speak with Animals spell prepared.

You can use Druidic to leave hidden messages. You and others who know Druidic automatically spot such a message. Others spot the message's presence with a successful DC 15 Intelligence (Investigation) check but can't decipher it without magic.""",
				"Class: Druid"))
			feats.append(Feature("Spellcasting",
				"""Prepare and cast spells; Wisdom is your spellcasting ability. <br>
				<h5>Cantrips: </h5>
				🍀 Druidcraft <br>
				🍀 Produce Flame <br>
				""",
				"Class: Druid"))
			if random.choice([True,False]):
				feats.append(Feature("Primal Order: Magician",
					"""You know one extra cantrip from the Druid spell list. In addition, your mystical connection to nature gives you a bonus to your Intelligence (Arcana or Nature) checks. The bonus equals your Wisdom modifier (minimum bonus of +1).""",
					"Class: Druid"))
			else:
				feats.append(Feature("Primal Order: Warden",
					"Trained for battle, you gain proficiency with Martial weapons and training with Medium armor.",
					"Class: Druid"))
		if level >= 2:
			feats.append(Feature("Wild Companion",
				f"""You can summon a nature spirit that assumes an animal form to aid you. As a Magic action, you can expend a spell slot or a use of Wild Shape to cast the <i>Find Familiar</i> spell without Material components. <br>
				<br>
				When you cast the spell in this way, the familiar is Fey and disappears when you finish a Long Rest. """,
				"Class: Druid"))

			times = 2
			cr = "1:4"
			fly = "lacks"
			noSpellBeast = """<b>No Spellcasting.</b> You can't cast spells, but shape-shifting doesn't break your Concentration or otherwise interfere with a spell you've already cast.<br>"""
			if level >= 4: cr = "1:2"
			if level >= 6: times += 1
			if level >= 8:
				cr = "1"
				fly = "may have"
			if level >= 17: times += 1
			if level >= 18: noSpellBeast = ""

			feats.append(Feature("Wild Shape",
				f"""The power of nature allows you to assume the form of an animal. As a Bonus Action, you shape-shift into a Beast form that you have learned for this feature. You stay in that form for a number of hours equal to half your Druid level or until you use Wild Shape again, have the Incapacitated condition, or die. You can also leave the form early as a Bonus Action. <br>
				<b>Number of Uses.</b> You can use Wild Shape {times} times. You regain one expended use when you finish a Short Rest, and you regain all expended uses when you finish a Long Rest. <br>
				<b>Known Forms.</b> You know four Beast forms for this feature, chosen from among Beast stat blocks that have a maximum Challenge Rating of {cr}. Starting at level 8, you can adopt a form that has a Fly Speed.. Whenever you finish a Long Rest, you can replace one of your known forms with another eligible form.
				<b>Rules While Transformed.</b> While in a form, you retain your personality, memories, and ability to speak, and the following rules apply:<br>
				<b>Temporary Hit Points.</b> When you assume a Wild Shape form, you gain a number of Temporary Hit Points equal to your Druid level.<br>
				<b>Game Statistics.</b> Your game statistics are replaced by the Beast's stat block, but you retain your creature type; Hit Points; Hit Point Dice; Intelligence, Wisdom, and Charisma scores; class features; languages; and feats. You also retain your skill and saving throw proficiencies and use your Proficiency Bonus for them, in addition to gaining the proficiencies of the creature. If a skill or saving throw modifier in the Beast's stat block is higher than yours, use the one in the stat block.<br> {noSpellBeast}
				<b>Objects.</b> Your ability to handle objects is determined by the form's limbs rather than your own. In addition, you choose whether your equipment falls in your space, merges into your new form, or is worn by it. Worn equipment functions as normal, but the DM decides whether it's practical for the new form to wear a piece of equipment based on the creature's size and shape. Your equipment doesn't change size or shape to match the new form, and any equipment that the new form can't wear must either fall to the ground or merge with the form. Equipment that merges with the form has no effect while you're in that form.
				""",
				"Class: Druid"))

		if level >= 3:
			if subclass == "Sea":
				feats.append(Feature(f"Circle of the Sea: Wrath of the Sea",
					f"""Druids of the Circle of the Sea draw on the tempestuous forces of oceans and storms. <br>
					As a Bonus Action, you can expend a use of your Wild Shape to manifest a 5-foot Emanation that takes the form of ocean spray that surrounds you for 10 minutes. It ends early if you dismiss it (no action required), manifest it again, or have the Incapacitated condition. <br>
					When you manifest the Emanation and as a Bonus Action on your subsequent turns, you can choose another creature you can see in the Emanation. The target must succeed on a Constitution saving throw against your spell save DC or take Cold damage and, if the creature is Large or smaller, be pushed up to 15 feet away from you. To determine this damage, roll a number of d6s equal to your Wisdom modifier (minimum of one die).
					""",
					"Class: Druid"))
				spells = 	"""<br>🌊 <i>Fog Cloud</i> <br> 🌊 <i>Gust of Wind</i><br> 🌊 <i>Ray of Frost</i><br> 🌊 <i>Shatter</i><br> 🌊 <i>Thunderwave</i>"""
				if level >= 5: spells += """<br> <i>🌊 Lightning Bolt </i><br> <i>🌊 Water Breathing</i>"""
				if level >= 7: spells += """<br><i> 🌊 Control Water </i><br><i> 🌊 Ice Storm Bolt</i>"""
				if level >= 9: spells += """<br><i> 🌊 Conjure Elemental </i><br><i> 🌊 Hold Monster</i>"""
				feats.append(Feature(f"Circle of the Sea Spells",
					f"""When you reach a Druid level specified in the Circle of the Sea Spells table, you thereafter always have the listed spells prepared.
					{spells}""",
					"Class: Druid"))
			else:
				feats.append(Feature(f"Circle of the {subclass}",
					f"You gain the subclass features of the Circle of the {subclass}.",
					"Class: Druid"))
		if level >= 4:
			feats = ApplyRandomFeats(character, n=1)
			feats.append(Feature("Wild Shape Improvement",
				"You can transform into a Beast of CR 1/2 or lower with a Swim speed.",
				"Class: Druid"))
			feats.append(Feature("Ability Score Improvement",
				"Increase ability scores or take a feat.",
				"Class: Druid"))

		if level >= 6:
			feats.append(Feature(f"{subclass} Feature",
				f"You gain the 6th-level feature of the Circle of the {subclass}.",
				"Class: Druid"))

		if level >= 8:
			feats.append(Feature("Wild Shape Improvement",
				"You can transform into a Beast of CR 1 with no movement limitations.",
				"Class: Druid"))
			feats.append(Feature("Ability Score Improvement",
				"Increase ability scores or take a feat.",
				"Class: Druid"))

		if level >= 10:
			feats.append(Feature(f"{subclass} Feature",
				f"You gain the 10th-level feature of the Circle of the {subclass}.",
				"Class: Druid"))

		if level >= 11:
			feats.append(Feature("Wild Shape Improvement",
				"You can now transform into a Beast of CR 1 with a Flying speed.",
				"Class: Druid"))

		if level >= 12:
			feats.append(Feature("Ability Score Improvement",
				"Increase ability scores or take a feat.",
				"Class: Druid"))

		if level >= 14:
			feats.append(Feature("Nature’s Sanctuary",
				"Beasts and Fey have difficulty attacking you; they must succeed on a Wisdom saving throw.",
				"Class: Druid"))

		if level >= 16:
			feats.append(Feature("Ability Score Improvement",
				"Increase ability scores or take a feat.",
				"Class: Druid"))

		if level >= 18:
			feats.append(Feature("Timeless Body",
				"You age at 1/10th the normal rate and suffer none of the frailty of old age.",
				"Class: Druid"))
			feats.append(Feature("Beast Spells",
				"You can cast spells in Wild Shape form, ignoring verbal/somatic components.",
				"Class: Druid"))

		if level >= 19:
			feats.append(Feature("Ability Score Improvement",
				"Increase ability scores or take a feat.",
				"Class: Druid"))

		if level >= 20:
			feats.append(Feature("Archdruid", 
				"You can Wild Shape an unlimited number of times and regain Channel Nature on short rests.",
				"Class: Druid"))

		return feats
