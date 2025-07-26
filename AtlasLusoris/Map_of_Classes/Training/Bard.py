from ..Grimoire_of_Health  import roll_health, HIT_DIE_TABLE
from ..Codex_of_Progression import Progression

from AtlasActorLudi.Map_of_Scores import PB, Modifier
from AtlasLusoris.Grimoire_of_Features import Feature
from AtlasLusoris.Grimoire_of_Features import ApplyRandomFeats

class Bard(Progression):
	HIT_DIE = 8

	def features(self, character):
		level = character.level
		if not character.subclass:
			character.subclass = choice(subclasses.get("Bard", ["Lore"]))
		subclass = character.subclass
		feats = []
		# Level 1
		if level >= 15:
			bardic_die = "d12"
		elif level >= 10:
			bardic_die = "d10"
		elif level >= 5:
			bardic_die = "d8"
		else:
			bardic_die = "d6"
		N_Dice = max(1,Modifier(character.abilities.CHA))

		if level >= 1:
			feats.append(Feature("Bardic Inspiration", 1,
								f"""You can supernaturally inspire others through words, music, or dance. This inspiration is represented by your Bardic Inspiration die, which is a {bardic_die}.

Using Bardic Inspiration. As a Bonus Action, you can inspire another creature within 60 feet of yourself who can see or hear you. That creature gains one of your Bardic Inspiration dice. A creature can have only one Bardic Inspiration die at a time.

Once within the next hour when the creature fails a D20 Test, the creature can roll the Bardic Inspiration die and add the number rolled to the d20, potentially turning the failure into a success. A Bardic Inspiration die is expended when it's rolled.

Number of Uses. You can confer a Bardic Inspiration die a number of times equal to your Charisma modifier ({N_Dice}), and you regain all expended uses when you finish a Long Rest."""))
			feats.append(Feature("Spellcasting", 1,
								 "Prepared spells; Charisma‑based casting."))

		# Level 2
		if level >= 2:
			roll_health(self.char)

			feats.append(Feature("Expertise", 2, "Double proficiency in 2 skills."))
			feats.append(Feature("Jack of All Trades", 2,
								 "Add half PB to non‑proficiency checks."))
			feats.append(Feature("Song of Rest", 2,
								 "1d6 extra HP on short rest.") )

		# Level 3 (subclass)
		if level >= 3:
			feats.append(Feature(f"{subclass or 'Bard'} College", 3,
								 "Subclass feature at L3."))
			feats.append(Feature("Expertise II", 3, "Subclass proficiency upgrade (if applicable)."))

		# Level 4
		if level >= 4:
			feats = ApplyRandomFeats(character, n=1)

		# Level 5
		if level >= 5:
			feats.append(Feature("Font of Inspiration", 5,
								 "Recover Bardic Inspiration on short rest."))
			feats.append(Feature("Improved Bardic Die", 5,
								 "Bardic Inspiration becomes d8."))

		# Level 6
		if level >= 6:
			feats.append(Feature(f"{subclass or 'Bard'} College Feature", 6,
								 "Subclass feature at L6."))

		# Level 7
		if level >= 7:
			feats.append(Feature("Countercharm", 7,
								 "Use action, performance gives advantage on saves vs charm/fear."))

		# Level 8
		if level >= 8:
			feats.append(Feature("Ability Score Improvement", 8,
								 "Increase ability scores or take a feat."))

		# Level 9
		if level >= 9:
			feats.append(Feature("Song of Rest Improvement", 9,
								 "Song of Rest becomes 1d8."))

		# Level 10
		if level >= 10:
			feats.append(Feature("Magical Secrets", 10,
								 "Choose 2 spells from any class."))
			feats.append(Feature("Improved Bardic Die", 10,
								 "Bardic Inspiration becomes d10."))

		# Level 11: no core feature

		# Level 12
		if level >= 12:
			feats.append(Feature("Ability Score Improvement", 12,
								 "Increase ability scores or take a feat."))

		# Level 13: no core feature

		# Level 14
		if level >= 14:
			feats.append(Feature(f"{subclass or 'Bard'} College Feature", 14,
								 "Subclass feature at L14."))

		# Level 15
		if level >= 15:
			feats.append(Feature("Improved Bardic Die", 15,
								 "Bardic Inspiration becomes d12."))

		# Level 16
		if level >= 16:
			feats.append(Feature("Ability Score Improvement", 16,
								 "Increase ability scores or take a feat."))

		# Level 17: no core feature

		# Level 18
		if level >= 18:
			feats.append(Feature("Magical Secrets II", 18,
								 "Choose 2 more spells from any class."))

		# Level 19
		if level >= 19:
			feats.append(Feature("Ability Score Improvement", 19,
								 "Increase ability scores or take a feat."))

		# Level 20
		if level >= 20:
			feats.append(Feature("Superior Inspiration", 20,
								 "When you roll initiative with none, regain one Inspiration."))

		return feats
