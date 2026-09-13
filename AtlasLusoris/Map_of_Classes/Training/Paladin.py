"""Legacy Paladin Progression — the grants that are still Progression's.

Core and Oath lessons live in ``Map_of_Paladin_Training`` (2024 PHB), which
carries all four Oaths at every level. This module must not re-emit 2014
class feature blurbs.

``filter_legacy_features`` drops a legacy Feature whose *name* matches a TOP
Training, so most of the old body was already invisible. Five features were
not, because 2024 renamed or deleted what they described, and they reached
the sheet beside the features that replaced them:

	Abjure Enemy        folded into core Abjure Foes at level 9; the old text
	                    also printed the literal placeholder "CHA"
	Turn the Unholy     deleted; Devotion's Channel Divinity is Sacred Weapon
	Purity of Spirit    replaced by Smite of Protection at level 15
	Ancients / Glory    the branch knew only Devotion and Vengeance, so the
	  Oath Feature      other two Oaths printed "Oath of {subclass} feature."

The 2014 body knew two Oaths of four and could not be repaired into knowing
the rest; the 2024 Map already does. So the blurbs are gone and this file
keeps only what it was doing that nothing else does.

**Three grants stay, because they are mutations rather than prose.** Removing
them costs a Paladin most of their Hit Points and their Fighting Style, which
is how they were found: the trim was measured against the untrimmed file
rather than assumed. The Cleric's legacy module is the shape this follows,
but not on these three, because a Cleric has no Fighting Style and its own
missing ``roll_health`` is a separate question.
"""

from __future__ import annotations

from ..Grimoire_of_Health import roll_health
from ..Codex_of_Progression import Progression
from AtlasLusoris.Grimoire_of_Features import (
	ApplyEpicBoon,
	ApplyRandomFeats,
	Feature,
	add_new_fighting_style,
	)


FIGHTING_STYLE_LEVEL = 2
HEALTH_ROLL_LEVEL = 2

ASI_LEVELS = (
	4,
	8,
	12,
	16,
	)

EPIC_BOON_LEVEL = 19


class Paladin(Progression):

	HIT_DIE = 10

	def features(
			self,
			character=None,
			):
		if character is None:
			character = self.char
		else:
			self.char = character

		level = character.Level

		self._roll_health_once(
			character,
			level,
			)

		granted = []
		granted.extend(
			self._fighting_style(
				character,
				level,
				)
			)
		granted.extend(
			self._ability_score_improvements(
				character,
				level,
				)
			)
		granted.extend(
			self._epic_boon(
				character,
				level,
				)
			)

		return granted

	# Levels beyond the first roll their Hit Die into base health. Nothing
	# else does this for a Paladin, so it stays here until health moves to
	# the 2024 Map wholesale.
	def _roll_health_once(
			self,
			character,
			level: int,
			) -> None:
		if level < HEALTH_ROLL_LEVEL:
			return

		roll_health(
			character,
			)

	# 2024: one Fighting Style at level 2, drawn rather than offered.
	# TrainingKit keeps the "Fighting Style" Training off the sheet precisely
	# so the drawn style names itself here instead.
	def _fighting_style(
			self,
			character,
			level: int,
			):
		if level < FIGHTING_STYLE_LEVEL:
			return []

		style = add_new_fighting_style(
			character,
			)
		if style is None:
			# Only reachable if the Paladin already owns every style, which
			# cannot happen at level 2. Granting nothing beats printing a
			# defect notice on a player's sheet.
			return []

		return [
			style,
			]

	# 2024: Ability Score Improvement (a feat) at 4 / 8 / 12 / 16.
	def _ability_score_improvements(
			self,
			character,
			level: int,
			):
		earned = []
		for threshold in ASI_LEVELS:
			if level < threshold:
				continue
			earned.extend(
				self._feat_or_placeholder(
					character,
					)
				)

		return earned

	# 2024: Epic Boon at 19, not another ASI.
	def _epic_boon(
			self,
			character,
			level: int,
			):
		if level < EPIC_BOON_LEVEL:
			return []

		try:
			return list(
				ApplyEpicBoon(
					character,
					n=1,
					) or ()
				)
		except Exception:
			return [
				Feature(
					"Epic Boon",
					"You gain an Epic Boon feat or another feat of your "
					"choice for which you qualify.",
					"Class: Paladin",
					),
				]

	def _feat_or_placeholder(
			self,
			character,
			):
		"""One drawn feat, or the named grant if the draw cannot be made."""
		try:
			return list(
				ApplyRandomFeats(
					character,
					n=1,
					) or ()
				)
		except Exception:
			return [
				Feature(
					"Ability Score Improvement",
					"You gain the Ability Score Improvement feat or another "
					"feat of your choice for which you qualify.",
					"Class: Paladin",
					),
				]
