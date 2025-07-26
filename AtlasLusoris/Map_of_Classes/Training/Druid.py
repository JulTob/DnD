from ..Grimoire_of_Health  import roll_health, HIT_DIE_TABLE
from ..Codex_of_Progression import Progression

from AtlasLusoris.Grimoire_of_Features import *
from random import choice, sample
from typing import List
from AtlasLusoris.Map_of_Classes.Scroll_of_Constants import SUBCLASSES

class Druid(Progression):
	HIT_DIE = 8

	def features(self, character):
		feats: List[Feature] = []
		level = character.Level
		pb = character.proficiency_bonus
		subclass = character.Subclass or choice(SUBCLASSES["Druid"])
		if level >= 2:
			roll_health(character)

		if level >= 1:

			if random.choice([True,False]):
				feats.append(Feature("Primal Order: Magician",
					"""You learnt one extra cantrip.
					Your Wisdom modifier (min +1) is added to Arcana or Nature checks.""",
					"Class: Druid"))
				character.Primal_Order = "Magician"
				character.abilities.Nature += max(1,character.AS.WIS)
				character.abilities.Arcana += max(1,character.AS.WIS)

			else:
				feats.append(Feature("Primal Order: Warden",
					"Trained for battle, you gain proficiency with Martial weapons and training with Medium armor.",
					"Class: Druid"))
				character.skills.Martial_Weapons.set_proficiency()
				character.skills.MediumArmor.set_proficiency()
				character.Primal_Order = "Warden"

		if level >= 2:
			feats.append(Feature("Wild Companion",
				f"""You can summon a nature spirit that assumes an animal form to aid you.
				As a Magic action, you can expend a spell slot or a use of Wild Shape
				to cast the <i>Find Familiar</i> spell without Material components. <br>
				<br>
				When you cast the spell in this way, the familiar is Fey and
				disappears when you finish a Long Rest. """,
				"Class: Druid"))

			uses = 2 + (1 if level >= 6 else 0) + (1 if level >= 17 else 0)

			cr = "1:4"
			fly = False
			if level >= 4:
				known_forms = 6
				cr = "1/2"
			if level >= 8:
				known_forms = 8
				cr = "1"
				fly = True
			canSpells = "can't"
			if level >= 18: canSpells = "can"
			feats.append(Feature("Wild Shape",
				f""" The power of nature allows you to assume the form of an animal.
				As a Bonus Action, you shape-shift into a Beast form that
				you have learned for this feature.
				You stay in that form for a number of hours equal to half
				your Druid level or until you use Wild Shape again, have the
				Incapacitated condition, or die.
				You can also leave the form early as a Bonus Action. <br>
				"""))
			feats.append(Feature("Number of Wild Shape",
				f"""
				You can use Wild Shape {uses} times.
				You regain one expended use when you finish a Short Rest,
				and you regain all expended uses when you finish a Long Rest. <br>
				"""))
			feats.append(Feature("Known Forms of Wild Shape",
				f"""
				You know four Beast forms for Wild Shapes
				chosen from among Beast stat blocks that have a
				maximum Challenge Rating of {cr}.
				{'You can adopt a form that has a Fly Speed.' if fly else ''}
				Whenever you finish a
				Long Rest, you can replace one of your known forms with another
				eligible form.
				"""))
			feats.append(Feature("Wild Shape: Rules While Transformed",
				f"""
				While in a Wildshape form, you retain your
				personality, memories,
				and ability to speak.<br>
				"""))
			feats.append(Feature("Wild Shape Temporary Hit Points.",
				f"""
				When you assume a Wild Shape form, you gain a number of
				Temporary Hit Points equal to your Druid level.<br>
				"""))
			feats.append(Feature("Wild Shape Game Statistics",
				f"""
				Your game statistics are replaced by the Beast's stat
				block, but you retain your creature type;
				Hit Points; Hit Point Dice; Intelligence, Wisdom,
				and Charisma scores; class features; languages; and feats.
				You also retain your skill and saving throw proficiencies
				and use your Proficiency Bonus for them, in addition to
				gaining the proficiencies of the creature. If a skill or
				saving throw modifier in the Beast's stat block is higher
				than yours, use the one in the Beast's stat block.<br>
				"""))
			feats.append(Feature("Wild Shape Spellcasting",
				f"""
				You {canSpells} cast spells while in Wild Shape. You can
				maintain concentration on spells casted before your transformation.
				"""))
			feats.append(Feature("Wild Shape Equipment.",
				f"""
				Your ability to handle objects is determined by the
				form's limbs rather than your own. In addition, you choose
				whether your equipment falls in your space, merges into your
				new form, or is worn by it. Worn equipment functions as
				normal, but the DM decides whether it's practical for the new
				form to wear a piece of equipment based on the creature's
				size and shape. Your equipment doesn't change size or
				shape to match the new form, and any equipment that
				the new form can't wear must either fall to the ground
				or merge with the form. Equipment that merges with the
				form has no effect while you're in that form.
				"""))

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
			if subclass == "Stars":
				nD = 1
				flight= ""
				extra = ""
				if level >= 10:
					nD = 2
					flight= "You have a Fly Speed of 20 feet and can hover."
					extra = "At the start of each of your turns while in your Starry Form, you can change which constellation glimmers on your body."
				feats.append(Feature(f"Circle of the Stars",
					f"""
					The Circle of the Stars has tracked heavenly patterns
					since time immemorial, discovering secrets hidden
					amid the constellations. By understanding these
					secrets, the Druids of this circle seek to harness the
					powers of the cosmos.
					""",
					"Class: Druid"))
				MapForm = random.choice([
					"A scroll bearing depictions of constellations.",
					"A stone tablet with fine holes drilled through it.",
					"An owlbear hide tooled with stellar symbols.",
					"A collection of maps bound in an ebony cover.",
					"A crystal engraved with starry patterns.",
					"A glass disk etched with constellations.",
					])
				feats.append(Feature(f"Star Map",
					f"""
					You've created a star chart as part of your heavenly
					studies. {MapForm} It is a Tiny object, and you can use it as
					a Spellcasting Focus for your Druid spells.
					<br>
					While holding the map, you have the Guidance and
					Guiding Bolt spells prepared, and you can cast Guiding Bolt
					without expending a spell slot. You can cast it in that
					way a number of times equal to your Wisdom modifier
					(minimum of once), and you regain all expended uses when
					you finish a Long Rest.
					<br>
					If you lose the map, you can perform a 1-hour ceremony to
					magically create a replacement. This ceremony can be
					performed during a Short or Long Rest, and it destroys the
					previous map.
					""",
					"Class: Druid"))
				feats.append(Feature(f"Starry Form",
					f"""
					As a Bonus Action, you can expend a use of your Wild Shape
					feature to take on a starry form rather than shape-shifting.
					<br>
					While in your starry form, you retain your game statistics,
					but your body becomes luminous, your joints glimmer like
					stars, and glowing lines connect them as on a star chart.
					This form sheds Bright Light in a 10-foot radius and
					Dim Light for an additional 10 feet. The form lasts for
					10 minutes. It ends early if you dismiss it (no action
					required), have the Incapacitated condition, or use this
					feature again.
					<br>
					Whenever you assume your starry form, choose which
					constellations glimmers on your body; your
					choice gives you certain benefits while in the form.
					<br> {extra}
					""",
					"Class: Druid"))
				feats.append(Feature(f"Starry Form: Archer.",
					f"""
					A constellation of an archer appears on you.
					When you activate this form and as a Bonus Action on
					your subsequent turns while it lasts, you can make a
					ranged spell attack, hurling a luminous arrow that
					targets one creature within 60 feet of yourself. On a
					hit, the attack deals Radiant damage equal to {nD}d8 plus
					your Wisdom modifier.
					""",
					"Class: Druid"))
				feats.append(Feature(f"Starry Form: Chalice.",
					f"""
					A constellation of a life-giving goblet appears on you.
					Whenever you cast a spell using a spell slot that restores
					Hit Points to a creature, you or another creature within
					30 feet of you can regain Hit Points equal to {nD}d8 plus
					your Wisdom modifier.
					""",
					"Class: Druid"))
				feats.append(Feature(f"Starry Form: Dragon.",
					f"""
					A constellation of a wise dragon appears on you.
					When you make an Intelligence or a Wisdom check or
					a Constitution saving throw to maintain Concentration,
					you can treat a roll of 9 or lower on the d20 as a 10.
					<br>{flight}
					""",
					"Class: Druid"))
				if level >= 6:
					feats.append(Feature(f"Cosmic Omen",
						f"""
						Whenever you finish a Long Rest, you can consult your Star Map for omens and roll a die. Until you finish your next Long Rest, you gain access to a special Reaction based on whether you rolled an even or an odd number on the die:
						<br>
						You can use this Reaction a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.
						""",
						"Class: Druid"))
					if random.choice([True, False]):
						feats.append(Feature(f"Cosmic Omen: Weal (even).",
							f"""
							Whenever a creature you can see within 30 feet of you is about to make a D20 Test, you can take a Reaction to roll 1d6 and add the number rolled to the total.
							""",
							"Class: Druid"))
					else:
						feats.append(Feature(f"Cosmic Omen: Woe (odd).",
							f"""
							Whenever a creature you can see within 30 feet of you is about to make a D20 Test, you can take a Reaction to roll 1d6 and subtract the number rolled from the total.
							""",
							"Class: Druid"))
				if level >= 14:
					feats.append(Feature(f"Full of Stars",
					f"""
					While in your Starry Form, you become partially incorporeal, giving you Resistance to Bludgeoning, Piercing, and Slashing damage.
					""",
					"Class: Druid"))

			else: #
				feats.append(Feature(f"Circle of the {subclass}",
					f"You gain the subclass features of the Circle of the {subclass}.",
					"Class: Druid"))
		if level >= 4:
			feats += ApplyRandomFeats(character, n=1)
		if level >= 5:
			feats.append(Feature(f"Wild Resurgence",
				f"""
				Once on each of your turns, if you have no uses of Wild Shape
				left, you can give yourself one use by expending a
				spell slot (no action required).
				<br>
				In addition, you can expend one use of Wild Shape
				(no action required) to give yourself a level 1 spell slot,
				but you can't do so again until you finish a Long Rest.
				""",
				"Class: Druid"))
		if level >= 7:
			if random.choice([True, False]):
				feats.append(Feature(f"Elemental Fury: Potent Spellcasting.",
				f"""
				The might of the elements flows through you.
				Add your Wisdom modifier to the damage you deal with any Druid cantrip.
				""",
				"Class: Druid"))
				if level >= 15:
					feats.append(Feature(f"Elemental Fury: Potent Spellcasting.",
						f"""
						The might of the elements flows through you.
						Add your Wisdom modifier to the damage you deal with any Druid cantrip.
						""",
						"Class: Druid"))
			else:
				nd = 1
				if level >= 15: nd = 2
				feats.append(Feature(f"Elemental Fury: Primal Strike.",
					f"""
					Once on each of your turns when you hit a creature with an attack roll using a weapon or a Beast form's attack in Wild Shape, you can cause the target to take an extra {nd}d8 Cold, Fire, Lightning, or Thunder damage (choose when you hit).
					""",
					"Class: Druid"))

		if level >= 8:
			feats += ApplyRandomFeats(character, n=1)
		if level >= 12:
			feats += ApplyRandomFeats(character, n=1)
		if level >= 16:
			feats += ApplyRandomFeats(character, n=1)
		if level >= 19:
			feats = ApplyEpicBoon(self.char,)
		if level >= 20:
			feats.append(Feature("Archdruid",
				"""
				The title of Archdruid has been bestowed upon you.
				Other Druids respect your opinions and experience with
				authority,
				but are not bound to obey your wishes.
				""",
				"Class: Druid"))
			feats.append(Feature("Evergreen Wild Shape",
				"""
				Whenever you roll Initiative and have no uses of Wild Shape left, you regain one expended use of it.
				""",
				"Class: Druid"))
			feats.append(Feature(" Nature Magician",
				"""
				You can convert uses of Wild Shape into a spell slot (no action required). Choose a number of your unexpended uses of Wild Shape and convert them into a single spell slot, with each use contributing 2 spell levels. For example, if you convert two uses of Wild Shape, you produce a level 4 spell slot. Once you use this benefit, you can't do so again until you finish a Long Rest.
				""",
				"Class: Druid"))
			feats.append(Feature(" Longevity",
				"""
				The primal magic that you wield causes you to age more slowly.
				For every ten years that pass, your body ages only one year.
				""",
				"Class: Druid"))
		return feats
