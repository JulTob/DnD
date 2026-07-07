from ..Grimoire_of_Health  import roll_health, HIT_DIE_TABLE
from ..Codex_of_Progression import Progression

from AtlasLusoris.Grimoire_of_Features import (
	Feature,
	BuildAvailableInvocations,
	ApplyRandomFeats,
	ApplyEpicBoon
	)

class Cleric(Progression):
	HIT_DIE = 8

	def features(self, character):
		feats = []
		level = character.Level  # or .level
		subclass = character.Subclass or "Light"

		if level >= 1:
			feats.append(Feature("Spellcasting", "Cast divine spells"))
			feats.append(Feature("Divine Domain", f"{subclass or 'Generic'} domain"))
		if level >= 2:
			roll_health(self.char)
		if level >= 4:
			feats = ApplyRandomFeats(character, n=1)
		return feats
