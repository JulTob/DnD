"""
Great Grimoire of NonPlayer rites
Awakens a Character skeleton as NonPlayer (CharactersKit).
follows D&D 5e Rules
"""

from AtlasActorLudi.Map_of_Scores import Modifier
from AtlasActorLudi.Map_of_Scores import PB
from AtlasActorLudi.Grimoire_of_AbilityScores import AbilityScores
from AtlasActorLudi.Grimoire_of_AbilityScores import apply_creature_ability_modifiers
from AtlasActorLudi.Grimoire_of_SavingThrows import SavingThrows
from AtlasActorLudi.Grimoire_of_Skills import Char_Skills
from AtlasActorLudi.AtlasAlusoris.Map_of_Races import Creature_Type_For_Race
from AtlasActorLudi.AtlasAlusoris.Map_of_Races import race_weights
from AtlasActorLudi.AtlasAlusoris.Map_of_Archetypes import Classify_Archetype
from AtlasActorLudi.AtlasAlusoris.Map_of_Archetypes import Identity_Axis
from TagKit import Imprint
from AtlasActorLudi.CharactersKit import Character
from AtlasActorLudi.CharactersKit import NonPlayer as Character_NonPlayer
from AtlasActorLudi.GendersKit import Gender_Reveal
from AtlasActorLudi.AtlasAlusoris.RaceKit import Apply_Race
from AtlasActorLudi.AtlasAlusoris.Map_of_NonPlayer_Features import Apply_NonPlayer_Features
from AtlasLusoris.BackgroundKit import Apply_Background
from AtlasLusoris.BackgroundKit import Apply_Background_Training
from AtlasLusoris.BackgroundKit import NONPLAYER_BACKGROUNDS
from AtlasLusoris.GuildKit import Apply_Guild
from AtlasLusoris.GuildKit import GUILDS


class NonPlayer(
		Character_NonPlayer,
		):
	"""Alusoris rites layered over the canonical NonPlayer role Tag."""

	DESCRIPTION = "Non-player rites: Race, Guild, Background, and light sheet."

	@Imprint
	def Awaken(
			npc,
			race=None,
			archetype=None,
			guild=None,
			background=None,
			profile=None,
			lvl=1,
			light=False,
			**_,
			):
		"""Stash summon kwargs — full rites run after membership binds Actions."""
		npc._seed = npc.seed
		npc.level = max(
				int(
						lvl
						),
				1,
				)
		npc._nonplayer_light = bool(
				light
				)
		npc._nonplayer_race = race
		npc._nonplayer_archetype = archetype
		npc._nonplayer_guild = guild
		npc._nonplayer_background = background
		npc._nonplayer_profile = profile

	def Finish_Awakening(
			npc,
			):
		"""Resolve NonPlayer dummies once Tag Actions are bound on the agent."""
		~npc
		race = getattr(
				npc,
				"_nonplayer_race",
				None,
				)
		guild = getattr(
				npc,
				"_nonplayer_guild",
				None,
				)
		background = getattr(
				npc,
				"_nonplayer_background",
				None,
				)
		profile_alias = getattr(
				npc,
				"_nonplayer_profile",
				None,
				)
		legacy_archetype = getattr(
				npc,
				"_nonplayer_archetype",
				None,
				)
		light = getattr(
				npc,
				"_nonplayer_light",
				False,
				)
		if profile_alias:
			if background and background != profile_alias:
				raise ValueError(
						"NonPlayer Background and legacy Profile disagree: "
						f"{background!r}"
						" != "
						f"{profile_alias!r}"
						"."
						)
			background = profile_alias
		if legacy_archetype:
			legacy_identity = Classify_Archetype(
					legacy_archetype
					)
			if legacy_identity.axis == Identity_Axis.GUILD:
				guild = guild or legacy_identity.name
			else:
				background = background or legacy_identity.name
		npc.race = race if race else npc.Pick(
				tuple(
						race_weights
						),
				weights=tuple(
						race_weights.values()
						),
				)
		Apply_Race(
				npc,
				race=npc.race,
				creature_type=Creature_Type_For_Race(
						npc.race
						),
				)
		npc.subrace = npc.SetSubrace()
		selected_guild = guild or npc.Pick(
				tuple(
						GUILDS
						)
				)
		selected_background = background or npc.Pick(
				tuple(
						NONPLAYER_BACKGROUNDS
						)
				)
		Apply_Guild(
				npc,
				selected_guild,
				)
		npc.gender = npc.SetGender()
		Gender_Reveal(
				npc,
				npc.gender,
				)
		if not light:
			npc.AS = AbilityScores(
					10,
					10,
					10,
					10,
					10,
					10,
					character=npc,
					)
			npc.AS.RandomAbilityScores()
		Apply_Background(
				npc,
				selected_background,
				)
		from AtlasActorLudi.AlignmentKit import New_Alignment
		New_Alignment(
				npc
				)
		npc.proficiency_bonus = npc.ProficiencyBonus()
		npc.genus = npc.BuildGenus()
		npc.Type = npc.genus
		npc.SetIdentitySummary()
		npc.name = npc.Naming()
		npc.title = npc.SetTitle()
		if not light:
			npc.size = npc.SetSize()
			npc.height = npc.size
			npc.ability_scores = npc.AS
			npc.pb = npc.proficiency_bonus
			npc.PB = npc.proficiency_bonus
			npc.AC = npc.SetAC()
			npc.armor_class = npc.AC
			npc.HP = npc.SetHitPoints(
					npc.level
					)
			npc.speed = 30
			npc.movement = npc.SetMovement()
			npc.ST = SavingThrows(
					npc,
					npc.AS,
					npc.proficiency_bonus,
					)
			npc.saving_throws = npc.ST
			npc.skills = Char_Skills(
					npc,
					npc.AS,
					npc.proficiency_bonus,
					)
			Apply_Background_Training(
					npc
					)
			npc.passive_perception = npc.ResolvePassivePerception()
			npc.to_hit_bonus = npc.CalculateToHitBonus()
			npc.spellcasting_ability = npc.SelectSpellcastingAbility()
			npc.spellcasting_ability_mod = npc.CalculateSpellcastingAbilityModifier()
			npc.spell_attack_bonus = (
					npc.spellcasting_ability_mod
					+ npc.proficiency_bonus
					)
			npc.spell_save_dc = 8 + npc.spell_attack_bonus
			npc.dc = npc.spell_save_dc
			npc.ready = True
		Apply_NonPlayer_Features(
				npc
				)
		return npc

	def SetIdentitySummary(
			npc,
			):
		"""Materialize the identity fields consumed by legacy Maps."""
		values = (
				npc.race,
				npc.subrace,
				npc.char_class,
				npc.background,
				npc.gender,
				npc.alignment,
				)
		npc._identity_summary = " , ".join(
				str(
						value
						)
				for value in values
				if value not in (
						None,
						"",
						)
				)
		return npc._identity_summary

	def ResolvePassivePerception(
			npc,
			):
		"""Resolve passive Perception from the finalized Skills Record."""
		return npc.skills.passive(
				"Perception"
				)

	def ResolveLanguages(
			npc,
			) -> list:
		"""Generate the language projection for this NonPlayer."""
		from AtlasLudus.Map_of_Languages import Language
		return Language(
				npc
				)

	def ResolveIdeal(
			npc,
			):
		"""Generate one deterministic ideal inside its projection Dice Bag."""
		from AtlasActorLudi.Map_of_Personality import Ideal
		return Ideal(
				npc
				)

	def ResolvePlotHook(
			npc,
			) -> str:
		"""Generate one deterministic plot hook inside its Dice Bag."""
		from AtlasActorLudi.Map_of_Personality import PlotHook
		return PlotHook(
				npc
				)

	def ResolveTrait(
			npc,
			) -> str:
		"""Generate one deterministic personality trait inside its Dice Bag."""
		from AtlasActorLudi.Map_of_Personality import Trait
		return Trait(
				npc
				)

	def set_name(
			npc,
			):
		npc.name = npc.Naming()

	def set_title(
			npc,
			):
		npc.title = npc.SetTitle()

	def set_stats(
			npc,
			):
		npc.size = npc.SetSize()
		npc.AC = npc.SetAC()
		npc.HP = npc.SetHitPoints(
				npc.level
				)
		npc.speed = 30
		npc.movement = npc.SetMovement()
		npc.ST = SavingThrows(
				npc,
				npc.AS,
				npc.proficiency_bonus,
				)
		npc.skills = Char_Skills(
				npc,
				npc.AS,
				npc.proficiency_bonus,
				)
		Apply_Background_Training(
				npc
				)
		npc.simple_attacks = npc.SimpleAttack()
		npc.special_attack = npc.SpecialAttack()

	def set_personality(
			npc,
			):
		npc.spells = npc.Magic()
		npc.personality_ready.set()

	def SetAbilities(
			npc,
			):
		"""Determine the abilities of the NPC. """
		from AtlasPugna.Map_of_Abilities import Abilities
		npc.abilities = Abilities(
				npc
				)
		return npc.abilities

	def to_dict(
			npc,
			):
		return {
				"race": npc.race,
				"guild": npc.char_class,
				"background": npc.background,
				"lvl": npc.level,
				"seed": npc.seed,
				"feature_ids": [
						feature.key
						for feature in getattr(
								npc,
								"npc_features",
								(),
								)
						],
				}

	@classmethod
	def from_dict(
			cls,
			data,
			):
		background = data.get(
				"profile"
				) or data.get(
				"background"
				)
		return NPC(
				race=data.get(
						"race"
						),
				guild=data.get(
						"guild"
						),
				background=background,
				lvl=data.get(
						"lvl"
						),
				seed=data.get(
						"seed"
						),
				)

	def SetGender(
			npc,
			) -> str:
		"""Set the gender of the NPC. """
		from AtlasActorLudi.Map_of_Gender import NewGender
		from AtlasActorLudi.Map_of_Gender import ElementalGender
		try:
			npc.gender = NewGender(
					npc
					)
			VALKYRE = "Valkyrie" in npc.subrace
			NYMPH = "Nymph" in npc.subrace
			if VALKYRE or NYMPH:
				npc.gender = "She"
			if "Elemental" in npc.race:
				npc.gender = ElementalGender(
						npc,
						npc.subrace,
						)
				return npc.gender
		except Exception:
			npc.gender = "They"
		return npc.gender

	def SetSize(
			npc,
			) -> str:
		"""Set the size of the NPC. """
		from AtlasActorLudi.Map_of_Size import Size
		npc.size = Size(
				npc,
				getattr(
						npc,
						"_identity_summary",
						npc.race,
						),
				)
		return npc.size

	def SetTitle(
			npc,
			) -> str:
		"""Generate a title (a name they are known for) for the NPC. """
		from AtlasEpica.Map_of_Titles import Title
		try:
			return Title(
					npc
					)
		except Exception:
			return (
					f"The {npc.race} {npc.char_class} {npc.background}"
					)

	def SetSubrace(
			npc,
			) -> str:
		"""Determine the subrace of the NPC. """
		from AtlasActorLudi.AtlasAlusoris.Map_of_Races import Subrace
		npc.subrace = Subrace(
				npc,
				npc.race,
				)
		return npc.subrace

	def Naming(
			npc,
			) -> str:
		"""Generate a name for the NPC. """
		try:
			from AtlasNomina.Map_of_Names import NewName
			return NewName(
					npc
					)
		except Exception:
			return npc.Pick(
					[
							"Zax",
							"Jon",
							"Nix",
							"Max",
							"Tod",
							"Raz",
							"Mox",
							]
					)

	def SetAC(
			npc,
			) -> int:
		"""
		Calculate the NPC's armor class
		based on various factors.

		Postconditions:
		<<      Returns an integer representing the NPC's armor class.
		"""
		from AtlasActorLudi.AtlasAlusoris.Map_of_Archetypes import AC_Identity_modifier
		from AtlasActorLudi.AtlasAlusoris.Map_of_Races import AC_race_modifier
		Dice = npc.Roll
		Dizero = npc.Roll_Zero
		PB = npc.proficiency_bonus
		AC = 10 + Dice(
				Modifier(
						npc.AS.DEX
						)
				) + Dice(
				PB
				)
		abilities = {
				"STR": Modifier(
						npc.AS.STR
						),
				"DEX": Modifier(
						npc.AS.DEX
						),
				"CON": Modifier(
						npc.AS.CON
						),
				"INT": Modifier(
						npc.AS.INT
						),
				"WIS": Modifier(
						npc.AS.WIS
						),
				"CHA": Modifier(
						npc.AS.CHA
						),
				}
		for identity in (
				npc.char_class,
				npc.background,
				):
			AC += Dizero(
					AC_Identity_modifier(
							identity,
							**abilities
							)
					)
		AC += Dizero(
				AC_race_modifier(
						race=npc.race,
						subrace=npc.subrace,
						)
				)
		if AC < 10 + PB:
			AC = 10 + PB
		if AC > 20 + PB:
			AC = 20 + PB
		return AC

	def SetHitPoints(
			npc,
			level: int,
			) -> int:
		"""
		Determine and Set the hit points of the NPC.

		Preconditions:
		>>              <level> must be an [integer] greater than or equal to 1.

		Postconditions:
		<<              Returns the calculated hit points as an [integer].
		"""
		Dice = npc.Roll
		hit_dice_sides = Dice(
				3,
				4,
				)
		dice_hp = hit_dice_sides + Dice(
				D=hit_dice_sides,
				N=level - 1,
				)
		con_hp = level * npc.ability_scores.con_mod
		if con_hp < 0:
			con_hp = 0
		total_hp = dice_hp + con_hp
		npc.HP = total_hp
		return total_hp

	def SetMovement(
			npc,
			) -> str:
		"""Determine the NPC's movement capabilities. """
		from AtlasPugna.Map_of_Movement import Movement
		npc.movement = Movement(
				npc
				)
		return Movement(
				npc
				)

	def SimpleAttack(
			npc,
			) -> str:
		"""Generate simple attack options for the NPC. """
		from AtlasPugna.Map_of_Attacks import Attack
		Dice = npc.Roll
		count = max(
				Dice(
						1,
						PB(
								npc.proficiency_bonus
								),
						),
				1,
				) or 1
		simple_list = []
		for _ in range(
				count
				):
			new_attack = Attack(
					npc
					)
			if new_attack not in simple_list:
				simple_list.append(
						new_attack
						)
		simple = "\n".join(
				simple_list
				)
		return simple

	def SpecialAttack(
			npc,
			) -> str:
		from AtlasPugna.Map_of_Attacks import SpecialAttack
		special = ""
		special += SpecialAttack(
				npc
				)
		special += "\n"
		return special

	def SetName(
			npc,
			) -> str:
		return npc.Naming(
				npc
				)

	def ProficiencyBonus(
			npc,
			) -> int:
		from AtlasActorLudi.Map_of_Scores import PB
		return PB(
				npc.level
				)

	def ResolveSenses(
			npc,
			):
		"""Generate the senses projection for this NonPlayer."""
		from AtlasPugna.Map_of_Senses import Senses
		return Senses(
				npc
				)

	def ResolveResistances(
			npc,
			):
		"""Generate resistances, immunities, and protections."""
		from AtlasPugna.Map_of_Resistances import Map_of_Resistances
		resistances = Map_of_Resistances
		result = (
				f"{resistances.Resistances(npc)} \n"
				f"{resistances.ConditionImmunities(npc)}\n "
				)
		result += (
				f"\n<h4>Protections:</h4> {resistances.Protections(npc)} \n "
				)
		return result

	def BuildGenus(
			npc,
			):
		"""
		Build the compatibility identity summary used by legacy Maps.

		Returns:
		        A comma-separated string of the current identity Records.
		"""
		attributes = [
				npc.race,
				npc.subrace,
				npc.char_class,
				npc.background,
				npc.gender,
				npc.alignment,
				]
		delimiter = " , "
		result = delimiter.join(
				str(
						attribute
						)
				for attribute in attributes
				if attribute not in (
						None,
						"",
						)
				)
		return result

	def SetArmorClass(
			npc,
			):
		npc.AC = npc.SetAC()
		return npc.AC

	def CalculateToHitBonus(
			npc,
			) -> int:
		"""Calculate the NPC's to-hit bonus. """
		highest_ability_mod = Modifier(
				max(
						npc.ability_scores.STR,
						npc.ability_scores.DEX,
						)
				)
		if npc.char_class == "Druid":
			highest_ability_mod = max(
					highest_ability_mod,
					Modifier(
							npc.ability_scores.WIS
							),
					)
		if npc.background == "Shaman":
			highest_ability_mod = max(
					highest_ability_mod,
					Modifier(
							npc.ability_scores.WIS
							),
					)
		if npc.char_class == "Warlock":
			highest_ability_mod = max(
					highest_ability_mod,
					Modifier(
							npc.ability_scores.CHA
							),
					)
		if npc.char_class == "Wizard":
			highest_ability_mod = max(
					highest_ability_mod,
					Modifier(
							npc.ability_scores.INT
							),
					)
		return highest_ability_mod + npc.proficiency_bonus

	def SelectSpellcastingAbility(
			npc,
			) -> str:
		"""Select the strongest mental ability for legacy spell generation."""
		int_mod = npc.ability_scores.int_mod
		wis_mod = npc.ability_scores.wis_mod
		cha_mod = npc.ability_scores.cha_mod
		ability_mod_dict = {
				"INT": int_mod,
				"WIS": wis_mod,
				"CHA": cha_mod,
				}
		return max(
				ability_mod_dict,
				key=ability_mod_dict.get,
				)

	def CalculateSpellcastingAbilityModifier(
			npc,
			) -> int:
		"""Return the modifier for the selected spellcasting ability."""
		int_mod = npc.ability_scores.int_mod
		wis_mod = npc.ability_scores.wis_mod
		cha_mod = npc.ability_scores.cha_mod
		return max(
				int_mod,
				wis_mod,
				cha_mod,
				)

	def Magic(
			npc,
			):
		from AtlasMagia.Map_of_Magic import Map_of_Magic
		magic = Map_of_Magic
		return magic.Magic(
				npc
				)

	def SetAbilityScores(
			npc,
			STR,
			DEX,
			CON,
			INT,
			WIS,
			CHA,
			):
		npc.AS = AbilityScores(
				STR,
				DEX,
				CON,
				INT,
				WIS,
				CHA,
				character=npc,
				)
		apply_creature_ability_modifiers(
				npc
				)
		npc.ST = SavingThrows(
				npc,
				npc.AS,
				npc.proficiency_bonus,
				)

	def SetMyStory(
			npc,
			):
		try:
			from AtlasEpica.Map_of_Stories import Story
			return Story(
					npc
					)
		except Exception:
			return ""

	def Check(
			npc,
			race=None,
			archetype=None,
			guild=None,
			background=None,
			profile=None,
			gender=None,
			alignment=None,
			subrace=None,
			):
		"""
		Check if specific attributes match given values.
		Args:
		        race (str, optional): Race tag to check.
		        archetype (str, optional): Former mixed identity-axis value.
		        guild (str, optional): Guild / class Tag to check.
		        background (str, optional): True Background Tag to check.
		        profile (str, optional): Deprecated alias for Background.
		        gender (str, optional): Gender tag to check.
		        alignment (str, optional): Alignment tag to check.
		        subrace (str, optional): Subrace tag to check.
		Returns:
		        bool: True if all provided parameters match NPC's attributes exactly.
		"""
		if archetype is not None:
			try:
				legacy_identity = Classify_Archetype(
						archetype
						)
			except ValueError:
				return False
			actual_by_axis = {
					Identity_Axis.GUILD: npc.char_class,
					Identity_Axis.BACKGROUND: npc.background,
					}
			if archetype.strip().casefold() != actual_by_axis[
					legacy_identity.axis
					].strip().casefold():
				return False
		checks = [
				(
						race,
						npc.race,
						),
				(
						guild,
						npc.char_class,
						),
				(
						background,
						npc.background,
						),
				(
						profile,
						npc.background,
						),
				(
						gender,
						npc.gender,
						),
				(
						alignment,
						npc.alignment,
						),
				(
						subrace,
						npc.subrace,
						),
				]
		for provided, actual in checks:
			if provided is None:
				continue
			if provided.strip().lower() != actual.strip().lower():
				return False
		return True

	def LightNPC_Hyperlink(
			npc,
			):
		from AtlasActorLudi.AtlasAlusoris.Map_of_NonPlayer_Paths import nonplayer_hash
		url = "/" + nonplayer_hash(
				race=npc.race,
				guild=npc.char_class,
				background=npc.background,
				level=npc.level,
				seed=npc._seed,
				)
		return (
				f'<a href="{url}">{npc.name}, {npc.title}</a>'
				)


def awaken_nonplayer(
		npc,
		race=None,
		archetype=None,
		guild=None,
		background=None,
		profile=None,
		lvl=1,
		light=False,
		**_,
		):
	"""Apply NonPlayer to an existing Character skeleton (module-level helper)."""
	NonPlayer(
			npc,
			race=race,
			archetype=archetype,
			guild=guild,
			background=background,
			profile=profile,
			lvl=lvl,
			light=light,
			)
	npc.Finish_Awakening()
	return npc


def NPC(
		race=None,
		archetype=None,
		guild=None,
		background=None,
		profile=None,
		lvl=1,
		light=False,
		seed=-1,
		target=None,
		**kwargs,
		):
	"""
	Interim constructor for call sites that still say NPC(...).
	Public Summon design lives in AtlasActorLudi — do not grow this.
	"""
	level = kwargs.pop(
			"level",
			lvl,
			)
	npc = target or Character(
			seed=seed,
			level=level,
			)
	if not isinstance(
			npc,
			Character,
			):
		raise TypeError(
				"NPC target must be a Character."
				)
	return awaken_nonplayer(
			npc,
			race=race,
			archetype=archetype,
			guild=guild,
			background=background,
			profile=profile,
			lvl=level,
			light=light,
			**kwargs,
			)
