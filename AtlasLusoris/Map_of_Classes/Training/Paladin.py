from ..Grimoire_of_Health  import roll_health, HIT_DIE_TABLE
from ..Codex_of_Progression import Progression

from AtlasLusoris.Grimoire_of_Features import Feature


class Paladin(Progression):
	HIT_DIE = 10

	def features(self, character):
		feats: List[Feature] = []
		level = character.Level  # or .level
		subclass = character.Subclass or "Devotion"

		# Level 1
		if level >= 1:
			feats.append(Feature("Lay on Hands", 1,
								 "Heal pool = 5 × Paladin level (Bonus action)."))
			feats.append(Feature("Spellcasting", 1,
								 "Prepare spells; Charisma-based casting."))

		# Level 2
		if level >= 2:
			roll_health(self.char)
			style_feat = add_new_fighting_style(self.char)
			if style_feat:
				feats.append(style_feat)
			else:
				feats.append(Feature("Fighting Style", 2,
								 "Choose a fighting style (e.g., Defense, Dueling)."))
			feats.append(Feature("Divine Smite", 2,
								 "Expend spell slots for extra radiant damage."))

		# Level 3
		if level >= 3:
			feats.append(Feature("Divine Health", 3,
								 "Immune to disease."))
			feats.append(Feature("Channel Divinity", 3,
								 "2 uses; includes Divine Sense and subclass option."))
			if subclass:
				feats.append(Feature(f"{subclass} Oath Feature", 3,
									 f"Oath of {subclass} feature."))

		# Level 4
		if level >= 4:
			feats = ApplyRandomFeats(character, n=1)

		# Level 5
		if level >= 5:
			feats.append(Feature("Extra Attack", 5,
								 "Attack twice when taking the Attack action."))
			feats.append(Feature("Faithful Steed", 5,
								 "Always have Find Steed prepared; cast once/long rest."))

		# Level 6
		if level >= 6:
			feats.append(Feature("Aura of Protection", 6,
								 "Save throws +CHA within 10 ft; 30 ft @18."))

		# Level 7
		if level >= 7 and subclass:
			feats.append(Feature(f"{subclass} Oath Feature", 7,
								 f"Oath of {subclass} feature."))

		# Level 8
		if level >= 8:
			feats.append(Feature("Ability Score Improvement", 8,
								 "Increase scores or take a feat."))

		# Level 9
		if level >= 9:
			feats.append(Feature("Abjure Foes", 9,
								 "Channel Divinity to frighten enemies."))

		# Level 10
		if level >= 10:
			feats.append(Feature("Aura of Courage", 10,
								 "Immune to frightened; 30 ft @18."))

		# Level 11
		if level >= 11:
			feats.append(Feature("Improved Divine Smite", 11,
								 "Extra 1d8 radiant damage on melee hit."))

		# Level 12
		if level >= 12:
			feats.append(Feature("Ability Score Improvement", 12,
								 "Increase scores or take a feat."))

		# Level 14
		if level >= 14:
			feats.append(Feature("Cleansing Touch", 14,
								 "Use Lay on Hands to end conditions."))

		# Level 15
		if level >= 15 and subclass:
			feats.append(Feature(f"{subclass} Oath Feature", 15,
								 f"Oath of {subclass} feature."))

		# Level 16
		if level >= 16:
			feats.append(Feature("Ability Score Improvement", 16,
								 "Increase scores or take a feat."))

		# Level 18
		if level >= 18:
			feats.append(Feature("Aura Expansion", 18,
								 "Auras increase to 30 ft."))

		# Level 19
		if level >= 19:
			feats.append(Feature("Epic Boon", 19,
								 "Gain an epic boon or feat."))

		# Level 20
		if level >= 20 and subclass:
			feats.append(Feature(f"{subclass} Oath Feature", 20,
								 f"Capstone of Oath of {subclass}."))

		return feats
