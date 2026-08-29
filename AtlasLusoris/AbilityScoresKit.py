"""
Ability Scores — the six numbers, and the combat-style bonuses that ride them.

``char.AS`` holds one of these. It is a plain value object, not a Tag: the
Character owns it by reference, and TagKit is not involved.

Preferences do not live here. How much a Character wants each score raised is
answered by ``GuildKit.ability_weights``, whose Tags declare the one canonical
preference model.

MAR and MAG are bonuses applied to whichever relevant score is already
highest, so they are properties of the scores themselves.
"""


class AbilityScores:
	"""The six scores, plus the martial and magical style bonuses.

	* ``_raw_scores`` stores ``str``, ``dex``, ``con``, ``int``, ``wis``, ``cha``.
	* ``mar`` applies dynamically to the highest of Strength and Dexterity.
	* ``mag`` applies dynamically to the highest of Intelligence, Wisdom, and
	  Charisma.
	"""
	NAME = "AbilityScores"

	def __init__(
			self,
			target=None,
			STR=10,
			DEX=10,
			CON=10,
			INT=10,
			WIS=10,
			CHA=10,
			*,
			character=None,
			):
		self.character = target or character
		self._raw_scores = {
			"str": int(
				STR
				),
			"dex": int(
				DEX
				),
			"con": int(
				CON
				),
			"int": int(
				INT
				),
			"wis": int(
				WIS
				),
			"cha": int(
				CHA
				),
			}
		self.mar = 0
		self.mag = 0

	# -----------------------------------------------------------------------
	# Rolling
	# -----------------------------------------------------------------------

	def RandomAbilityScores(self):
		"""Roll all six scores from the Character's own dice."""
		from AtlasActorLudi.Grimoire_of_AbilityScores import RandomAbilityScore

		if self.character is None:
			raise ValueError(
				"Random Ability Scores require their Character owner."
				)

		for key in (
				"str",
				"dex",
				"con",
				"int",
				"wis",
				"cha",
				):
			self._raw_scores[
				key
				] = int(
					RandomAbilityScore(
						self.character
						)
					)

	def StandardArray(self):
		"""Assign the standard array, shuffled on the Character's dice."""
		if self.character is None:
			raise ValueError(
				"Standard Array assignment requires its Character owner."
				)

		scores = [
			15,
			14,
			13,
			12,
			10,
			8,
			]
		self.character.dices.shuffle(
			scores
			)

		for key, value in zip(
				(
					"str",
					"dex",
					"con",
					"int",
					"wis",
					"cha",
					),
				scores,
				):
			self._raw_scores[
				key
				] = int(
					value
					)

	# -----------------------------------------------------------------------
	# Dynamic Ability Properties
	# -----------------------------------------------------------------------

	@property
	def STR(self) -> int:
		raw_str = self._raw_scores[
			"str"
			]
		raw_dex = self._raw_scores[
			"dex"
			]

		return (
			raw_str + self.mar
			if raw_str >= raw_dex
			else raw_str
			)

	@STR.setter
	def STR(
			self,
			value: int,
			):
		self._raw_scores[
			"str"
			] = int(
				value
				)

	@property
	def DEX(self) -> int:
		raw_str = self._raw_scores[
			"str"
			]
		raw_dex = self._raw_scores[
			"dex"
			]

		return (
			raw_dex + self.mar
			if raw_dex > raw_str
			else raw_dex
			)

	@DEX.setter
	def DEX(
			self,
			value: int,
			):
		self._raw_scores[
			"dex"
			] = int(
				value
				)

	@property
	def CON(self) -> int:
		return self._raw_scores[
			"con"
			]

	@CON.setter
	def CON(
			self,
			value: int,
			):
		self._raw_scores[
			"con"
			] = int(
				value
				)

	@property
	def INT(self) -> int:
		raw_int = self._raw_scores[
			"int"
			]
		raw_wis = self._raw_scores[
			"wis"
			]
		raw_cha = self._raw_scores[
			"cha"
			]
		is_highest = (
			raw_int >= raw_wis
			and raw_int >= raw_cha
			)

		return (
			raw_int + self.mag
			if is_highest
			else raw_int
			)

	@INT.setter
	def INT(
			self,
			value: int,
			):
		self._raw_scores[
			"int"
			] = int(
				value
				)

	@property
	def WIS(self) -> int:
		raw_int = self._raw_scores[
			"int"
			]
		raw_wis = self._raw_scores[
			"wis"
			]
		raw_cha = self._raw_scores[
			"cha"
			]
		is_highest = (
			raw_wis > raw_int
			and raw_wis >= raw_cha
			)

		return (
			raw_wis + self.mag
			if is_highest
			else raw_wis
			)

	@WIS.setter
	def WIS(
			self,
			value: int,
			):
		self._raw_scores[
			"wis"
			] = int(
				value
				)

	@property
	def CHA(self) -> int:
		raw_int = self._raw_scores[
			"int"
			]
		raw_wis = self._raw_scores[
			"wis"
			]
		raw_cha = self._raw_scores[
			"cha"
			]
		is_highest = (
			raw_cha > raw_int
			and raw_cha > raw_wis
			)

		return (
			raw_cha + self.mag
			if is_highest
			else raw_cha
			)

	@CHA.setter
	def CHA(
			self,
			value: int,
			):
		self._raw_scores[
			"cha"
			] = int(
				value
				)

	# -----------------------------------------------------------------------
	# Public helpers
	# -----------------------------------------------------------------------

	def adjust_mar(
			self,
			delta: int = 1,
			):
		"""Increase or decrease the Martial combat style bonus."""
		self.mar += int(
			delta
			)

		return self.mar

	def adjust_mag(
			self,
			delta: int = 1,
			):
		"""Increase or decrease the Magical combat style bonus."""
		self.mag += int(
			delta
			)

		return self.mag

	def set_score(
			self,
			score_name: str,
			value: int,
			):
		"""Set one raw ability score, clamped to 1–30."""
		name = score_name.lower()[
			:3
			]

		if name not in self._raw_scores:
			raise ValueError(
				f"Invalid ability score name: {score_name}"
				)

		self._raw_scores[
			name
			] = max(
				1,
				min(
					30,
					int(
						value
						),
					),
				)

		return self._raw_scores[
			name
			]

	def adjust_score(
			self,
			score_name: str,
			delta: int,
			):
		"""Adjust one raw ability score by a signed delta."""
		name = score_name.lower()[
			:3
			]

		if name not in self._raw_scores:
			raise ValueError(
				f"Invalid ability score name: {score_name}"
				)

		current = self._raw_scores[
			name
			]
		new = max(
			1,
			min(
				30,
				current + int(
					delta
					),
				),
			)
		self._raw_scores[
			name
			] = new

		return new

	# -----------------------------------------------------------------------
	# Modifiers
	# -----------------------------------------------------------------------

	def mod(
			self,
			score: int,
			) -> int:
		"""Calculate the ability modifier for one score."""
		from AtlasActorLudi.Map_of_Scores import Modifier

		return Modifier(
			score
			)

	@property
	def str_mod(self) -> int:
		return self.mod(
			self.STR
			)

	@property
	def dex_mod(self) -> int:
		return self.mod(
			self.DEX
			)

	@property
	def con_mod(self) -> int:
		return self.mod(
			self.CON
			)

	@property
	def int_mod(self) -> int:
		return self.mod(
			self.INT
			)

	@property
	def wis_mod(self) -> int:
		return self.mod(
			self.WIS
			)

	@property
	def cha_mod(self) -> int:
		return self.mod(
			self.CHA
			)

	@property
	def modifiers(self) -> dict[str, int]:
		"""Return modifiers for each ability score."""
		return {
			"Strength": self.str_mod,
			"Dexterity": self.dex_mod,
			"Constitution": self.con_mod,
			"Intelligence": self.int_mod,
			"Wisdom": self.wis_mod,
			"Charisma": self.cha_mod,
			}


def ensure_ability_scores(
		agent,
		**scores,
		):
	"""Give an Agent an AbilityScores record if it lacks one."""
	existing = getattr(
		agent,
		"AS",
		None,
		)

	if isinstance(
			existing,
			AbilityScores,
			):
		return existing

	record = AbilityScores(
		character=agent,
		**scores,
		)
	agent.AS = record

	return record
