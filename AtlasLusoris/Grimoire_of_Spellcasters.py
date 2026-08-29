# AtlasLusoris/Grimoire_of_Spellcasters.py

import random
from AtlasMagia.Lodge_of_Spells import *
from AtlasLusoris.Compass_of_Learned_Spells import (
	CLASS_SALT,
	catalog_spells,
	caster_rng,
	finish_learning,
	grant_spell,
	html_spell_catalog,
	html_spell_index,
	max_slot_from,
	pick_new,
	progressive_learn,
	spell_key,
	spell_level,
	spell_mark,
	stats_at_level,
	unique_spells,
	)


from AtlasLusoris.Map_of_Casting_Tables import (
	LIST_FALLBACK,
	casting_row,
	slots_as_map,
	)


SPELL_LISTS = {
	"test":  {
			0: [ ],
			1: [ ],
			2: [ ],
			3: [ ],
			4: [ ],
			5: [ ],
			6: [ ],
			7: [ ],
			8: [ ],
			9: [ ],
			},
	"Monk":  {
			0: [ ],
			1: [ ],
			2: [ ],
			3: [ ],
			4: [ ],
			5: [ ],
			6: [ ],
			7: [ ],
			8: [ ],
			9: [ ],
			},
	"Warlock":  {
			0: [
				BladeWard,    BoomingBlade, ChillTouch, CreateBonfire,
				EldritchBlast,    Friends, Frostbite,    GreenFlameBlade,
				Infestation,    LightningLure,    MageHand,    MagicStone,
				MindSliver,    MinorIllusion,    PoisonSpray,    Prestidigitation,
				SwordBurst, Thunderclap,    TolltheDead,    TrueStrike,
				],
			1: [
				ArmorofAgathys,    ArmsOfHadar,    Bane,    CauseFear, CharmPerson,
				ComprehendLanguages,    DetectMagic,    DistortValue,
				ExpeditiousRetreat,    HellishRebuke,    Hex,    IllusoryScript,
				ProtectionfromEvilandGood,    SpeakwithAnimals,    HideousLaughter,
				UnseenServant,    WitchBolt,
				],
			2: [
				BorrowedKnowledge,    CloudofDaggers,    CrownofMadness, Darkness,
				Earthbind,    Enthrall, HoldPerson,    Invisibility,    MindSpike,
				MirrorImage,    RayofEnfeeblement,    ShadowBlade,    SpiderClimb,
				SprayOfCards,    Suggestion,    WarpSense, MistyStep,
				],
			3: [
				Antagonize,    Counterspell,    DispelMagic,    EnemiesAbound,
				Fear,    Fly,    GaseousForm,    HungerHadar,    HypnoticPattern,
				InciteGreed,    IntellectFortress,    MagicCircle,    MajorImage,
				RemoveCurse,    SpiritShroud,    SummonFey,    SummonLesserDemons,
				SummonShadowspawn,    SummonUndead,    ThunderStep,    Tongues,
				VampiricTouch,
				],
			4: [
				Banishment,    Blight,    CharmMonster,    DimensionDoor,
				ElementalBane,    GateSeal,    HallucinatoryTerrain,
				RaulothimPsychicLance,    ShadowofMoil,    SickeningRadiance,
				SpiritOfDeath,    SummonAberration,    SummonGreaterDemon,
				],
			5: [
				ContactOtherPlane,    DanseMacabre,    Dream,    Enervation,    FarStep,
				HoldMonster,    InfernalCalling,    JallarziStormofRadiance,
				Mislead,    NegativeEnergyFlood,    PlanarBinding,    Scrying,
				SynapticStatic,    TeleportationCircle,    WallLight,
				],
			6: [
				ArcaneGate,    CircleofDeath,    CreateUndead,    Eyebite,
				InvestitureFlame,    InvestitureIce,    InvestitureStone,
				InvestitureWind,    MentalPrison,    Scatter,    SoulCage,
				SummonFiend,    TashasBubblingCauldron,    TashaOtherworldlyGuise,
				TrueSeeing,
				],
			7: [
				CrownofStars,    DreamOfTheBlueVeil,    Etherealness,
				FingerofDeath,    Forcecage,    PlaneShift,    PowerWordPain
				],
			8: [
				Befuddlement,    Demiplane,    DominateMonster,    Glibness,
				MaddeningDarkness,    PowerWordStun,
				],
			9: [
				AstralProjection,    BladeofDisaster,    Foresight, Gate,
				Imprisonment,    PowerWordKill,    PsychicScream,    TruePolymorph,
				Weird
				],
			},
	"Wizard": {
			0: [
				AcidSplash,       BladeWard,
				ChillTouch,       DancingLights,
				Elementalism,     FireBolt,
				Friends,          Light,
				MageHand,         Mending,
				Message,          MindSliver,
				MinorIllusion,    PoisonSpray,
				Prestidigitation, RayofFrost,
				ShockingGrasp,    Thunderclap,
				TolltheDead,      TrueStrike,
				BoomingBlade,        ControlFlames,
				],
			1: [Thunderwave,    BurningHands,     IllusoryScript,
				MagicMissile, Alarm, CharmPerson, ChromaticOrb,
				ColorSpray,    ComprehendLanguages,    DetectMagic,
				DisguiseSelf,    ExpeditiousRetreat,    FalseLife,
				FeatherFall,    FindFamiliar,    FogCloud,    Grease,    IceKnife,
				Identify,    Jump,    Longstrider,    MageArmor,
				ProtectionfromEvilandGood,    RayofSickness,    Shield,
				SilentImage,    Sleep,    HideousLaughter, FloatingDisk,
				UnseenServant,    WitchBolt,
				],
			2: [Blur, MistyStep, AlterSelf,    ArcaneLock,    Augury,
				BlindnessDeafness,    Blur,    CloudofDaggers,    ContinualFlame,
				CrownofMadness,    Darkness,    Darkvision,    DetectThoughts,
				DragonsBreath,    EnhanceAbility,    EnlargeReduce,    FlamingSphere,
				GentleRepose,    GustOfWind,    HoldPerson,    Invisibility,    Knock,
				Levitate,    LocateObject,    MagicMouth,    MagicWeapon,
				AcidArrow,    MindSpike,    MirrorImage,    MistyStep,    MagicAura,
				PhantasmalForce,    RayOfEnfeeblement,    RopeTrick,
				ScorchingRay,    SeeInvisibility,    Shatter,    SpiderClimb,
				Suggestion,    Web,
				AlterSelf, ArcaneLock, ArcaneVigor, Augury, BlindnessDeafness, Blur,
				CloudofDaggers, ContinualFlame, CrownofMadness, Darkness, Darkvision,
				DetectThoughts, DragonsBreath, EnhanceAbility, EnlargeReduce,
				FlamingSphere, GentleRepose, GustOfWind, HoldPerson, Invisibility,
				Knock, Levitate, LocateObject, MagicMouth, MagicWeapon, AcidArrow,
				MindSpike, MirrorImage, MistyStep, MagicAura, PhantasmalForce,
				RayOfEnfeeblement, RopeTrick, ScorchingRay, SeeInvisibility, Shatter,
				SpiderClimb, Suggestion, Web,

				],
			3: [AnimateDead,    BestowCurse,
				Blink,            Clairvoyance,
				Counterspell,    DispelMagic,    Fear,
				FeignDeath,        Fireball,
				Fly,            GaseousForm,    GlyphWarding,
				Haste,            HypnoticPattern,
				TinyHut,        LightningBolt,
				MagicCircle,    MajorImage,
				Nondetection,    PhantomSteed,    ProtectionfromEnergy,
				RemoveCurse,    Sending,        SleetStorm,
				Slow,            SpeakwithDead,
				StinkingCloud,    SummonFey,
				SummonUndead,    Tongues,
				VampiricTouch,    WaterBreathing,
				],
			4: [ArcaneEye,    Banishment,    Blight,    CharmMonster,    Confusion,
				ConjureMinorElementals,    ControlWater,    DimensionDoor,
				Divination,    EvardsBlackTentacles,
				ArcaneEye, Banishment, Blight, CharmMonster, Confusion,
				ConjureMinorElementals, ControlWater, DimensionDoor, Divination,
				EvardsBlackTentacles, Fabricate, FireShield, GreaterInvisibility,
				HallucinatoryTerrain, IceStorm, SecretChest, LocateCreature,
				PrivateSanctum, OtilukeResilientSphere, PhantasmalKiller, Polymorph,
				StoneShape, Stoneskin, SummonAberration, SummonConstruct,
				SummonElemental, VitriolicSphere, WallofFire,
				],
			5: [
				AnimateObjects, BigbysHand, CircleofPower, Cloudkill, ConeCold,
				ConjureElemental, ContactOtherPlane, Creation, DominatePerson, Dream,
				Geas, HoldMonster, JallarziStormofRadiance, LegendLore, Mislead,
				ModifyMemory, Passwall, PlanarBinding, RarysTelepathicBond, Scrying,
				Seeming, SteelWindStrike, SummonDraconicSpirit, SynapticStatic,
				Telekinesis, TeleportationCircle, WallForce, WallStone,
				YolandeRegalPresence,
				],
			6: [
				ArcaneGate, ChainLightning, CircleofDeath, Contingency, CreateUndead,
				Disintegrate, DrawmijInstantSummons, Eyebite, FleshtoStone,
				GlobeInvulnerability, GuardsandWards, MagicJar, MassSuggestion,
				MoveEarth, OtilukeFreezingSphere, IrresistibleDance, ProgrammedIllusion,
				SummonFiend, Sunbeam, TashasBubblingCauldron, TrueSeeing, WallIce,
				],
			7: [
				DelayedBlastFireball, Etherealness, FingerDeath, Forcecage,
				MirageArcane, MagnificentMansion, MordenkainenSword, PlaneShift,
				PrismaticSpray, ProjectImage, ReverseGravity, Sequester, Simulacrum,
				Symbol, Teleport,
				 ],
			8: [
				AntimagicField, AntipathySympathy, Befuddlement, Clone, ControlWeather,
				Demiplane, DominateMonster, IncendiaryCloud, Maze, MindBlank,
				PowerWordStun, Sunburst, Telepathy,
				],
			9: [
				AstralProjection, Foresight, Gate, Imprisonment, MeteorSwarm,
				PowerWordKill, PrismaticWall, Shapechange, TimeStop, TruePolymorph,
				Weird, Wish,
				],
			},
	"Sorcerer":  {
			0: [ ],
			1: [ ],
			2: [ ],
			3: [ ],
			4: [ ],
			5: [ ],
			6: [ ],
			7: [ ],
			8: [ ],
			9: [ ],
			},
	"Druid":  {
			0: [PrimalSavagery, Thunderclap, ThornWhip, StarryWisp, SparetheDying,
				Shillelagh, Resistance, ProduceFlame, PoisonSpray,	Message,
				Mending,	Guidance,	Elementalism,	Druidcraft],
			1: [ AnimalFriendship,	CharmPerson,	CreateorDestroyWater,
				CureWounds,	DetectMagic,	DetectPoisonandDisease,
				Entangle,	FaerieFire,	FogCloud, Goodberry,	HealingWord,
				IceKnife,	Jump,	Longstrider,	ProtectionfromEvilandGood,
				PurifyFoodandDrink, SpeakwithAnimals,	Thunderwave,
				],
			2: [
				Aid, AnimalMessenger,	Augury,	Barkskin,	BeastSense,
				ContinualFlame,	Darkvision,	EnhanceAbility,	EnlargeReduce,
				FindTraps,	FlameBlade,	FlamingSphere,	GustOfWind,	HeatMetal,
				HoldPerson,	LesserRestoration,	LocateAnimalsPlants,
				LocateObject,	Moonbeam,	PassWithoutTrace,
				ProtectionFromPoison,	SpikeGrowth,	SummonBeast,
				],
			3: [
				AuraofVitality, CallLightning,	ConjureAnimals,	Daylight,
				DispelMagic,	ElementalWeapon,	FeignDeath,	MeldIntoStone,
				PlantGrowth,	ProtectionfromEnergy,	Revivify,	SleetStorm,
				SpeakWithPlants,	SummonFey,	WaterBreathing,	WaterWalk,
				WindWall,
				],
			4: [
				Blight,	CharmMonster,	Confusion,	ConjureMinorElementals,
				ConjureWoodlandBeings,	ControlWater,	Divination,
				DominateBeast,	FireShield,	FountofMoonlight, FreedomofMovement,
				GiantInsect,	GraspingVine,	HallucinatoryTerrain,
				IceStorm,	LocateCreature,	Polymorph,	StoneShape,	Stoneskin,
				SummonElemental,	WallofFire,
				],
			5: [
				AntilifeShell,	Awaken,	CommuneWithNature,	ConeofCold,
				ConjureElemental,	Contagion,	Geas,	GreaterRestoration,
				InsectPlague,	MassCureWounds,	PlanarBinding,	Reincarnate,
				Scrying,	TreeStride,	WallStone,
				],
			6: [
				ConjureFey,	FindthePath,	FleshtoStone,	Heal,	HeroesFeast,
				MoveEarth,	Sunbeam,	TransportviaPlants,	WallThorns,	WindWalk
				],
			7: [
				FireStorm,	MirageArcane,	PlaneShift,	Regenerate,
				ReverseGravity,	Symbol
				],
			8: [
				AnimalShapes,	AntipathySympathy,	Befuddlement,
				ControlWeather,	Earthquake,	IncendiaryCloud,	Sunburst,
				Tsunami
				],
			9: [
				Foresight,	Shapechange,	StormofVengeance,	TrueResurrection
				],
			},
	"Ranger":  {
			0: [PrimalSavagery, Thunderclap, ThornWhip, StarryWisp, SparetheDying,
				Shillelagh, Resistance, ProduceFlame, PoisonSpray,	Message,
				Mending,	Guidance,	Elementalism,	Druidcraft ],
			1: [Alarm, CureWounds, DetectMagic, Entangle, FogCloud,
				Goodberry, HuntersMark, HailofThorns, Longstrider, SpeakwithAnimals],
			2: [Aid, BeastSense, CordonofArrows, Darkvision, EnhanceAbility,
				FindTraps, GustOfWind, HealingSpirit, LesserRestoration,
				LocateObject, PassWithoutTrace, SpikeGrowth],
			3: [ConjureAnimals, ConjureBarrage, Daylight, LightningArrow,
				MeldIntoStone, Nondetection, PlantGrowth, ProtectionfromEnergy,
				SpeakPlants, WaterBreathing, WaterWalk],
			4: [ConjureWoodlandBeings, DominateBeast, FreedomofMovement,
				GraspingVine, LocateCreature, Stoneskin],
			5: [CommuneWithNature, ConjureVolley, SwiftQuiver, TreeStride,
				WrathNature],

			6: [ ],
			7: [ ],
			8: [ ],
			9: [ ],
			},
	"Eldritch Knight": {
			0: [    AcidSplash,           BladeWard,
					ChillTouch,           DancingLights,
					Elementalism,         FireBolt,
					Friends,              Light,
					MageHand,             Mending,
					Message,              MindSliver,
					MinorIllusion,        PoisonSpray,
					Prestidigitation,     RayofFrost,
					ShockingGrasp,        Thunderclap,
					TolltheDead,          TrueStrike,
					BoomingBlade,        ControlFlames
					 ],
			1: [     Shield,         MagicMissile,     AbsorbElements,
					BurningHands,     Alarm,             CharmPerson,
					ChromaticOrb,     ColorSpray,      DetectMagic,
					ExpeditiousRetreat,        FalseLife,
					],
			2: [     MistyStep,                 MirrorImage,
					HoldPerson,             Shatter,
					Blur,                    Web,
					MistyStep,                MagicWeapon,
					Invisibility,
					Darkness,                CrownofMadness,
					CloudofDaggers,            BlindnessDeafness,
					],
			3: [     Counterspell,             Fireball,
					DispelMagic,             Fly,
					Slow,                    SleetStorm,
					PhantomSteed,            Haste,
					Blink,
					],
			4: [     GreaterInvisibility,     IceStorm,
					DimensionDoor,             Stoneskin,
					Confusion,
					],
			5: [ ],
			6: [ ],
			7: [ ],
			8: [ ],
			9: [ ],
			},
	"Arcane Trickster": {
		0: [    AcidSplash,           BladeWard,
				BoomingBlade,
				ChillTouch,        ControlFlames,
				DancingLights,
				Elementalism,         FireBolt,
				Friends,              GreenFlameBlade,
				Light,
				MageHand,             Mending,
				Message,              MindSliver,
				MinorIllusion,        PoisonSpray,
				Prestidigitation,     RayofFrost,
				ShockingGrasp,        Thunderclap,
				TolltheDead,          TrueStrike,

				],
		1: [
					Alarm,             AbsorbElements,
					BurningHands,
					ChromaticOrb,     ColorSpray,      CharmPerson, Catapult,
						CauseFear,    ComprehendLanguages,
					DetectMagic,    DisguiseSelf,
					ExpeditiousRetreat,
					FogCloud,    FalseLife, FeatherFall,    FindFamiliar,
					Grease,
					IceKnife,    Identify,    IllusoryScript,
					Jump,
					Longstrider,
					MagicMissile, MageArmor,
					ProtectionfromEvilandGood,
					Shield, SilentImage,    SilveryBarbs,    Sleep,    Snare,
					HideousLaughter,
					Thunderwave,
					UnseenServant,
					],
		2: [     AlterSelf,    ArcaneLock,    ArcaneVigor, Augury,
					BlindnessDeafness,    Blur,    BorrowedKnowledge,
					CloudofDaggers,        CrownofMadness,
					Darkness,    DetectThoughts,
					Earthbind,    EnhanceAbility,    EnlargeReduce,
					GustOfWind,
					HoldPerson,
					Invisibility,
					KineticJaunt, Knock,
					Levitate,    LocateObject,
					MagicMouth,    MagicWeapon, MindSpike,
						MistyStep,     MirrorImage, MagicAura,
					PhantasmalForce,    Pyrotechnics,
					RayOfEnfeeblement, RopeTrick,
					ScorchingRay,     Shatter,    SeeInvisibility,    ShadowBlade,
						Shatter,    SpiderClimb,    SprayOfCards,
						Suggestion,
					MindWhip,
					VortexWarp,
					Web,    WardingWind,    WarpSense,    WitherBloom,

					],
			3: [     AnimateDead,    Antagonize,
					BestowCurse,    Blink,
					Counterspell,     Catnap,    Clairvoyance,    Counterspell,
					DispelMagic,
					EnemiesAbound,
					Fear,    Fireball,     Fly,    FeignDeath,    FlameArrows,
					GaseousForm,    GlyphWarding,
					Haste,    HypnoticPattern,
					IntellectFortress,
					LifeTransference,    LightningBolt,
					MagicCircle,    MelfsMinuteMeteors,
					Nondetection,
					PhantomSteed,    ProtectionfromEnergy,
					RemoveCurse,
					Sending,    Slow,    SleetStorm,    SpeakwithDead,
					SpiritShroud,    StinkingCloud,    SummonFey,
						SummonLesserDemons,    SummonShadowspawn,    SummonUndead,
					TinyHut,    ThunderStep,    TidalWave,    TinyServant,
						Tongues,    VampiricTouch,    WallSand,    WallWater,
						WaterBreathing,
					],
			4: [     ArcaneEye,
					Banishment,    Blight,
					CharmMonster,    Confusion,    ConjureMinorElementals,
						ControlWater,
					DimensionDoor, Divination,
					Fabricate,
					GreaterInvisibility,
					HallucinatoryTerrain,
					LocateCreature,
					FaithfulHound,
					OtilukeResilientSphere,
					PhantasmalKiller,
					Polymorph,
					SpiritOfDeath,    StoneShape,    Stoneskin, StormSphere,
						SummonAberration,    SummonConstruct,    SummonElemental,
						SummonGreaterDemon,    WallofFire,
					],
			5: [ ],
			6: [ ],
			7: [ ],
			8: [ ],
			9: [ ],
			}

	}



def class_spell_table(name):
	"""Class list, or a fallback list when this class's table is still empty."""
	table = SPELL_LISTS.get(name) or {}
	if any(table.values()):
		return table
	fallback = LIST_FALLBACK.get(name)
	if fallback:
		return SPELL_LISTS.get(fallback) or {}
	return table


class Spellcaster:
	def __init__(caster, character, known=None):
		if known is None:      known = []
		caster.character     = character
		caster.level         = character.level
		caster.casting_stat = caster.get_casting_stat()
		caster.granted_spells = []
		caster.always_prepared = set()
		caster.prepared_spells = []
		caster.catalog_known = True
		caster.spell_slots     =  caster.get_spell_slots()
		caster.spells_available = caster.available_spells()
		caster.spells_known = known
		caster.prepare_spells()

	def get_casting_stat(caster):
		return "INT"  # default, override in subclasses

	def get_spell_slots(caster):
		slots_table = {}
		return slots_table

	def list_name(caster):
		subclass = getattr(caster.character, "subclass", None)
		if subclass in SPELL_LISTS:
			return subclass
		return getattr(caster, "class_name", None) or caster.character.char_class

	def available_spells(caster):
		"""Spells this character can learn, capped by slot level — not character level."""
		table = class_spell_table(caster.list_name()) or class_spell_table(caster.character.char_class)
		max_slot = max_slot_from(caster.spell_slots)
		unlocked = [lvl for lvl in table if lvl == 0 or lvl <= max_slot]
		return unique_spells([spell for lvl in unlocked for spell in table[lvl]])

	def prepare_spells(caster):
		pass

	def spell_save_dc(caster):
		# Use whatever you call your prof bonus and ability mod
		prof = getattr(caster.character, "proficiency_bonus", 2)  # or caster.character.get_prof_bonus()
		stat_mod = caster.modifier()
		return 8 + prof + stat_mod

	def spell_attack_bonus(caster):
		prof = getattr(caster.character, "proficiency_bonus", 2)
		stat_mod = caster.modifier()
		return prof + stat_mod

	def modifier(caster):
		return (getattr(caster.character.AS, caster.casting_stat) - 10) // 2

	def html_slots(caster):
		slots = caster.spell_slots or {}
		return "<br>".join(
			f"<b>Level {lvl}</b>: <i>{num}</i>"
			for lvl, num in slots.items()
			if num
			)

	def html_rules(caster):
		index = html_spell_index(caster)
		slots_html = caster.html_slots()
		return f"""
			<div class="npc-textbox" style="grid-column: span 3;">
				<h1 style="font-family: 'Iglesia'; font-size: 3.1em;">{caster.character.char_class} Spellcasting</h1>
				</div>
			<div class="npc-textbox">
				<h2>Spell Slots:</h2>
				{slots_html}
				<p>You regain all expended slots when you finish a Long Rest.</p>
				</div>
			<div class="npc-textbox">
				<b>Spell Save DC:</b> {caster.spell_save_dc()}<br>
				<b>Spell Attack Bonus:</b> +{caster.spell_attack_bonus()}
				</div>
			<div class="npc-textbox">
				{index}
				</div>
			"""

	def html_catalog(caster):
		return html_spell_catalog(caster)

	def __str__(caster):
		return caster.html_rules()

	def html(caster):
		return caster.html_rules()

class Wizard(Spellcaster):
	def __init__(caster, character, known=None):
		if known is None:      known = []
		caster.class_name     = "Wizard"
		caster.character     = character
		caster.level         = character.level
		caster.granted_spells = []
		caster.always_prepared = set()
		caster.prepared_spells = []
		caster.catalog_known = True
		caster.spell_slots     =  caster.get_spell_slots()
		caster.spells_available = caster.available_spells()
		caster.spells_known = known
		caster.casting_stat = caster.get_casting_stat()
		caster.prepare_spells()

	def get_casting_stat(caster):
		return "INT"

	def get_stats(caster, key):
		row = casting_row("Wizard", caster.level)
		if key == "cantrips":
			return row.get("cantrips", 0)
		if key == "spells":
			return row.get("prepared", 0)
		if key == "slots":
			return slots_as_map(row.get("slots"))

	def get_spell_slots(caster):
		return caster.get_stats("slots")

	def prepare_spells(caster):
		table = class_spell_table("Wizard")
		cantrips, book = progressive_learn(
			caster.character,
			table,
			caster.level,
			cantrips_at=lambda lvl: stats_at_level(caster, lvl, "cantrips"),
			known_at=lambda lvl: 2 * lvl + 4,
			slots_at=lambda lvl: stats_at_level(caster, lvl, "slots"),
			salt=CLASS_SALT["Wizard"],
			)
		finish_learning(caster, cantrips, book, prepared_count=caster.get_stats("spells"))

	def modifier(caster):
		return (getattr(caster.character.AS, caster.casting_stat) - 10) // 2

	def html(caster):
		return caster.html_rules()

	def html_rules(caster):
		n = caster.get_stats("spells")
		index = html_spell_index(caster)
		slots_html = caster.html_slots()
		return f"""
			<div class="npc-textbox" style="grid-column: span 3;">
				<h1 style="font-family: 'Iglesia'; font-size:    3.1em; ">
					The Book of Names</h1>
				<p>Wonder happens on the road. The book is how you carry it.
				You hunt names, write them, and speak them when the world
				will answer. Intelligence is the voice you use.</p>
				</div>
			<div class="npc-textbox" style="grid-column: span 1;">
				<h2>Spell Slots:</h2>
				{slots_html} <br>
				You regain all expended slots when you finish a Long Rest.
				</p>
				<br><br>
				</div>
			<div class="npc-textbox" style="font-family: 'Iglesia'">
				<h2 style="font-family: 'Iglesia'">
					Spell Save DC:</h2> {caster.spell_save_dc()}<br>
				<h2 style="font-family: 'Iglesia'">
					Spell Attack Bonus:</h2> +{caster.spell_attack_bonus()}
				</div>
			<div class="npc-textbox" style="grid-column: span 1;">
			<h3 style="font-family: 'Iglesia'; font-size:    3.1em; "> Spellbook </h3>
			When you finish a Long Rest, you may prepare {n} spells from the
			book — the ones you can speak at any moment.
			{index}
			<h2>Arcane Focus</h2>
			You can use an Arcane Focus as a Spellcasting Focus for your
			Wizard spells.
			</div>
			"""

	def __str__(caster):
		return caster.html_rules()

class Druid(Spellcaster):
	def __init__(caster, character, known=None):
		if known is None:      known = []
		caster.class_name     = "Druid"
		caster.character     = character
		caster.level         = character.level
		caster.granted_spells = []
		caster.always_prepared = set()
		caster.prepared_spells = []
		caster.catalog_known = True
		caster.spell_slots     =  caster.get_spell_slots()
		caster.spells_available = caster.available_spells()
		caster.spells_known = known
		caster.casting_stat = caster.get_casting_stat()
		caster.prepare_spells()

	def get_casting_stat(caster):
		return "WIS"

	def get_stats(caster, key):
		row = casting_row("Druid", caster.level)
		if key == "cantrips":
			result = row.get("cantrips", 0)
			if getattr(caster.character, "Primal_Order", None) == "Magician":
				result += 1
			return result
		if key == "spells":
			return row.get("prepared", 0)
		if key == "slots":
			return slots_as_map(row.get("slots"))

	def get_spell_slots(caster):
		return caster.get_stats("slots")

	def prepare_spells(caster):
		table = class_spell_table("Druid")
		cantrips, book = progressive_learn(
			caster.character,
			table,
			caster.level,
			cantrips_at=lambda lvl: stats_at_level(caster, lvl, "cantrips"),
			known_at=lambda lvl: stats_at_level(caster, lvl, "spells"),
			slots_at=lambda lvl: stats_at_level(caster, lvl, "slots"),
			salt=CLASS_SALT["Druid"],
			)
		finish_learning(caster, cantrips, book)

	def modifier(caster):
		return (getattr(caster.character.AS, caster.casting_stat) - 10) // 2

	def html(caster):
		return caster.html_rules()

	def html_rules(caster):
		n = caster.get_stats("spells")
		index = html_spell_index(caster)
		slots_html = caster.html_slots()
		return f"""
			<div class="npc-textbox" style="grid-column: span 3;">
				<h1 style="font-family: 'Iglesia'; font-size:    3.1em; ">
					Druid Spellcasting</h1>
				<p> As a student of natural magic, you have learned to cast spells. </p>
				</div>
			<div class="npc-textbox" style="grid-column: span 1;">
				<h2>Spell Slots:</h2>
				{slots_html} <br>
				You regain all expended slots when you finish a Long Rest.</p>
				<br><br>
				</div>
			<div class="npc-textbox" style="font-family: 'Iglesia'">
				<h2 style="font-family: 'Iglesia'">
					Spell Save DC:</h2> {caster.spell_save_dc()}<br>
				<h2 style="font-family: 'Iglesia'">
					Spell Attack Bonus:</h2> +{caster.spell_attack_bonus()}
				</div>
			<div class="npc-textbox" style="grid-column: span 1;">
			<h3 style="font-family: 'Iglesia'; font-size:    3.1em; "> SpellBook </h3>
			You may prepare {n} spells whenever you finish a Long Rest, that you can use at any moment, from your book of spells:
			{index}
			<h2>Arcane Focus</h2>
			You can use an Arcane Focus (such as a wand or scepter),  as a Spellcasting Focus for your Druid spells.
			</div>
			"""

	def __str__(caster):
		return caster.html_rules()

class Ranger(Spellcaster):
	def __init__(self, character, known: list[Spell] | None = None):
		super().__init__(character, known or [])

	def get_casting_stat(caster):
		return "WIS"

	def get_known_cap(self) -> int:
		wis_mod = self.modifier()
		return max(1, (self.level // 2) + wis_mod)

	def modifier(self) -> int:
		return (getattr(self.character.AS, self.get_casting_stat()) - 10) // 2

	def get_stats(caster, key):
		row = casting_row("Ranger", caster.level)
		if key == "prepared":
			return row.get("prepared", 0)
		if key == "slots":
			return slots_as_map(row.get("slots"))

	def get_spell_slots(caster):
		return caster.get_stats("slots")

	def prepare_spells(caster):
		table = class_spell_table("Ranger")
		cantrips, known = progressive_learn(
			caster.character,
			table,
			caster.level,
			cantrips_at=lambda lvl: 0,
			known_at=lambda lvl: stats_at_level(caster, lvl, "prepared"),
			slots_at=lambda lvl: stats_at_level(caster, lvl, "slots"),
			salt=CLASS_SALT["Ranger"],
			)
		finish_learning(caster, cantrips, known)

	def modifier(caster):
		return (getattr(caster.character.AS, caster.casting_stat) - 10) // 2

	def html(caster):
		return caster.html_rules()

	def html_rules(caster):
		n = caster.get_stats("prepared")
		index = html_spell_index(caster, bullet="🍀")
		slots_html = caster.html_slots()
		return f"""
		<div class="npc-textbox" style="grid-column: span 3;">
			<h1 style="font-family: 'Iglesia'; font-size: 3.1em;">Ranger Spellcasting</h1>
			<p>You prepare {n} spells each day, using your Wisdom as your spellcasting ability.</p>
		</div>
		<div class="npc-textbox">
			<h2>Spell Slots:</h2>
			{slots_html}
			<p>You regain all slots when you finish a long rest.</p>
		</div>
		<div class="npc-textbox">
			<h2>Spell Save DC:</h2> {caster.spell_save_dc()}<br>
			<h2>Spell Attack Bonus:</h2> +{caster.spell_attack_bonus()}
		</div>
		<div class="npc-textbox" style="grid-column: span 1;">
			<h3 style="font-family: 'Iglesia'; font-size: 3.1em;">Spell List</h3>
			{index}
		</div>
		"""

	def __str__(caster):
		return caster.html_rules()

class Sorcerer(Spellcaster):
	def __init__(caster, character):
		super().__init__(character)
		lvl = getattr(character, "level", 1)
		caster.metamagic_points = 0 if lvl < 2 else lvl

	def get_casting_stat(caster):
		return "CHA"

	def get_stats(caster, key):
		row = casting_row("Sorcerer", caster.level)
		if key == "cantrips":
			return row.get("cantrips", 0)
		if key in ("spells", "prepared"):
			return row.get("prepared", 0)
		if key == "slots":
			return slots_as_map(row.get("slots"))

	def get_spell_slots(caster):
		return caster.get_stats("slots")

	def prepare_spells(caster):
		table = class_spell_table("Sorcerer")
		cantrips, known = progressive_learn(
			caster.character,
			table,
			caster.level,
			cantrips_at=lambda lvl: stats_at_level(caster, lvl, "cantrips"),
			known_at=lambda lvl: stats_at_level(caster, lvl, "spells"),
			slots_at=lambda lvl: stats_at_level(caster, lvl, "slots"),
			salt=CLASS_SALT["Sorcerer"],
			)
		finish_learning(caster, cantrips, known)

	def html_rules(caster):
		n = caster.get_stats("prepared")
		index = html_spell_index(caster)
		slots_html = caster.html_slots()
		points = getattr(caster, "metamagic_points", 0)
		points_line = ""
		if points:
			points_line = f"<p><strong>Sorcery Points:</strong> {points}</p>"
		return f"""
			<div class="npc-textbox" style="grid-column: span 3;">
				<h1 style="font-family: 'Iglesia'; font-size: 3.1em;">Sorcerer Spellcasting</h1>
				<p>You prepare {n} Sorcerer spells. Charisma is your spellcasting ability.</p>
				{points_line}
				</div>
			<div class="npc-textbox">
				<h2>Spell Slots:</h2>
				{slots_html}
				<p>You regain all expended slots when you finish a Long Rest.</p>
				</div>
			<div class="npc-textbox">
				<b>Spell Save DC:</b> {caster.spell_save_dc()}<br>
				<b>Spell Attack Bonus:</b> +{caster.spell_attack_bonus()}
				</div>
			<div class="npc-textbox">
				{index}
				</div>
			"""

	def __str__(caster):
		return caster.html_rules()


MONK_TECHNIQUE_LEVELS = [
	(2, [FlurryofBlows, PatientDefense, StepOfTheWind]),    # Level 2: Focus starts
	(3, [DeflectAttacks]),                                 # Level 3: Improved Deflection
	(5, [StunningStrike]),                                 # Level 5: Stunning Strike
	# Subclass techniques: You can append dynamically based on subclass.
	]


class Monk(Spellcaster):
	def __init__(caster, character):
		caster.character = character
		caster.level = character.Level
		caster.casting_stat = caster.get_casting_stat()
		caster.focus_points = caster.get_focus_points()
		caster.granted_spells = []
		caster.always_prepared = set()
		caster.prepared_spells = []
		caster.catalog_known = False
		caster.spell_slots = {}

	def get_casting_stat(caster):
		return "WIS"

	def get_focus_points(caster):
		if caster.level >= 2: return caster.level
		else: return 0

	@property
	def spells_known(self):
		"""Return all Focus Techniques available to this Monk."""
		techniques = []
		for lvl, feats in MONK_TECHNIQUE_LEVELS:
			if self.level >= lvl:
				techniques.extend(feats)
		# Deduplicate by name
		unique = {ft.name: ft for ft in techniques}
		return list(unique.values())

	def focus_save_dc(self):
		# Usual: 8 + prof + WIS modifier
		prof = getattr(self.character, "proficiency_bonus", 2)
		wis_mod = self.WIS_modifier()
		return 8 + prof + wis_mod

	def WIS_modifier(self):
		# WIS modifier
		return (getattr(self.character.AS, "WIS", 10) - 10) // 2

	def html(caster):
		return caster.html_rules()

	def html_rules(caster):
		features = caster.spells_known
		symb = random.choice(["☯","☯︎","࿊","࿋","࿌","࿅", "☮",
			"☥", "☣", "𓂀", "𖥂", "𖨢", "⧊", "⧋","⚳", "⚴", "⚸",
			"♆", "♅", "♄", "♃", "☿", "♁", "𖤓", "ᙏ", "ᙎ", "𒀭",
			"𒐊", "𒐉", "𒐋", "𒐏", "𒐖","𒐕", "𒐗", "𒐘", "𐫱", "🀄︎", "🜹",
			"᛭", "⧾", "⚚", "⚕", "✯", "⚝", "⛤", "⛥","⛦", "❄","𖣓",
			"֎", "֍", "𖣐", "۝", "۩", "🃟", "🜾", "🝋", "𝚿", "𝛀", "Ʊ", "𓇳",
			"𓉱", "𓉷", "𓉶", "𓉴", "𖧞", "𖥋", "𖥘", "𖧑", "𓍢", "𓍣", "꥟", "꧁꧂",
			"⏾", "❂", "🀀", "🏵️", "ॐ", "⚕︎", "𐁊", "☸︎", "⚔︎", "𖡨", "🜍", "🜎",
			"㊍", "㊐", "㊥", "㊉", "㊏", "☷", "☶", "☰", "☱", "☲", "☳", "☴",
			"☵",

						])
		features_list = "".join(
			f"""<div class="npc-textbox" style="grid-column: span 1;">
					<h2 style="font-family: 'Cinzel Decorative'; font-size: 1.5em;">
						{ft.name}</h2>
					{symb}
					{ft.action_type} <br>
					Cost: {ft.cost} Focus Point<br>
					<i>{ft.description}</i>
					</div>"""
			for ft in features
			)
		return f"""
		<div class="npc-textbox" style="grid-column: span 3;">
			<h1 style="font-family: 'Cinzel Decorative'; font-size:    2.5em; ">
				Monk's Focus
				</h1>
				<p>Your martial training grants you extraordinary inner
				strength known as Focus.
				</p>
				</div>
		<div class="npc-textbox" style="grid-column: span 1;">
			<h2 style="font-family: 'Cinzel Decorative'; font-size: 1.5em;">
				Focus Points: <b>{caster.focus_points}</b>
				</h2>
				You regain all expended Focus Points upon finishing a Short or Long Rest.
				</div>
		<div class="npc-textbox" style="font-size: 1.521em;">
			<h3 style="font-family: 'Cinzel Decorative'">
				Focus Save DC:</h3>
				{caster.focus_save_dc()}<br>
			<h3 style="font-family: 'Cinzel Decorative'">
				Focus Ability Modifier:</h3>
				+{caster.WIS_modifier()}
			</div>

		<div class="npc-textbox" style="grid-column: span 1;">
			<h2 style="font-family: 'Cinzel Decorative'; font-size: 1.3em;">
				Focus Techniques:</h2>
			You can channel Focus to perform special techniques.
			</div>

				{features_list}


		"""

	def __str__(caster):
		return caster.html_rules()


def get_monk_focus_features(level, subclass=None):
	features = []
	for lvl, feats in MONK_TECHNIQUE_LEVELS:
		if level >= lvl:
			features.extend(feats)
	# Add subclass focus techniques here if needed (by subclass and level)
	return features


class EldritchKnight(Spellcaster):
	def get_casting_stat(caster):
		return "INT"

	def get_stats(caster, key):
		table = {
			1:  {"cantrips": 0, "spells": 0,  "slots": (0,0,0,0)},
			2:  {"cantrips": 0, "spells": 0,  "slots": (0,0,0,0)},
			3:  {"cantrips": 2, "spells": 3,  "slots": (2,0,0,0)},
			4:  {"cantrips": 2, "spells": 4,  "slots": (3,0,0,0)},
			5:  {"cantrips": 2, "spells": 4,  "slots": (3,0,0,0)},
			6:  {"cantrips": 2, "spells": 4,  "slots": (3,0,0,0)},
			7:  {"cantrips": 2, "spells": 5,  "slots": (4,2,0,0)},
			8:  {"cantrips": 2, "spells": 6,  "slots": (4,2,0,0)},
			9:  {"cantrips": 2, "spells": 6,  "slots": (4,2,0,0)},
			10: {"cantrips": 3, "spells": 7,  "slots": (4,3,0,0)},
			11: {"cantrips": 3, "spells": 8,  "slots": (4,3,0,0)},
			12: {"cantrips": 3, "spells": 8,  "slots": (4,3,0,0)},
			13: {"cantrips": 3, "spells": 9,  "slots": (4,3,2,0)},
			14: {"cantrips": 3, "spells":10,  "slots": (4,3,2,0)},
			15: {"cantrips": 3, "spells":10,  "slots": (4,3,2,0)},
			16: {"cantrips": 3, "spells":11,  "slots": (4,3,3,0)},
			17: {"cantrips": 3, "spells":11,  "slots": (4,3,3,0)},
			18: {"cantrips": 3, "spells":11,  "slots": (4,3,3,0)},
			19: {"cantrips": 3, "spells":12,  "slots": (4,3,3,1)},
			20: {"cantrips": 3, "spells":13,  "slots": (4,3,3,1)}
			}
		lvl = caster.level
		if lvl > 20: lvl = 20
		value = table.get(lvl, {"cantrips": 0, "spells": 0, "slots": (0,0,0,0)})
		if key == "cantrips":
			return value["cantrips"]
		if key == "spells":
			return value["spells"]
		if key == "slots":
			return {i + 1: val for i, val in enumerate(value["slots"])}

	def get_spell_slots(caster):
		return caster.get_stats("slots")

	def available_spells(caster):
		"""Spells this Eldritch Knight can learn, capped by slot level."""
		table = (SPELL_LISTS.get(caster.character.subclass)
				or SPELL_LISTS.get("Eldritch Knight")
				or SPELL_LISTS.get("Wizard", {}))
		max_slot = max_slot_from(caster.spell_slots)
		unlocked = [lvl for lvl in table if lvl == 0 or lvl <= max_slot]
		return unique_spells([spell for lvl in unlocked for spell in table[lvl]])

	def prepare_spells(caster):
		table = (SPELL_LISTS.get(caster.character.subclass)
				or SPELL_LISTS.get("Eldritch Knight")
				or SPELL_LISTS.get("Wizard", {}))
		cantrips, known = progressive_learn(
			caster.character,
			table,
			caster.level,
			cantrips_at=lambda lvl: stats_at_level(caster, lvl, "cantrips"),
			known_at=lambda lvl: stats_at_level(caster, lvl, "spells"),
			slots_at=lambda lvl: stats_at_level(caster, lvl, "slots"),
			salt=CLASS_SALT["Eldritch Knight"],
			)
		finish_learning(caster, cantrips, known)


	def modifier(caster):
		return (getattr(caster.character.AS, caster.casting_stat) - 10) // 2

	def html(caster):
		return caster.html_rules()

	def html_rules(caster):
		index = html_spell_index(caster, bullet="♟️")
		slots_html = caster.html_slots()
		return f"""
			<div class="npc-textbox" style="grid-column: span 1;">
			<h1 style="font-family: 'Iglesia'; font-size:    3.1em; ">{caster.character.subclass} Spellcasting</h1>
			<p> Eldritch Knights combine the martial mastery common to all Fighters with a careful study of magic. Their spells both complement and extend their combat skills.<br> You have learned to cast spells. </p>
			<h2>Spell Slots:</h2> {slots_html} <br>  You regain all expended slots when you finish a Long Rest.</p>
			{index}
			<h2>Arcane Focus</h2>
			You can use an Arcane Focus (such as a wand or scepter),  as a Spellcasting Focus for your Wizard spells.
			</div>
			<div class="npc-textbox" style="margin-bottom: 1em;">
				<b>Spell Save DC:</b> {caster.spell_save_dc()}<br>
				<b>Spell Attack Bonus:</b> +{caster.spell_attack_bonus()}
				</div>
			"""

	def __str__(caster):
		return caster.html_rules()

class ArcaneTrickster(Spellcaster):
	"""
	Arcane Trickster spellcasting rules, 2024 PHB.
	Handles cantrips, spell slots, prepared spells, and focus.
	"""
	ARCANE_TRICKSTER_TABLE = {
		1:  {"cantrips": 0, "prepared": 0,  "slots": (0,0,0,0)},
		2:  {"cantrips": 0, "prepared": 0,  "slots": (0,0,0,0)},
		3:  {"cantrips": 3, "prepared": 3,  "slots": (2,0,0,0)},
		4:  {"cantrips": 3, "prepared": 4,  "slots": (3,0,0,0)},
		5:  {"cantrips": 3, "prepared": 4,  "slots": (3,0,0,0)},
		6:  {"cantrips": 3, "prepared": 4,  "slots": (3,0,0,0)},
		7:  {"cantrips": 3, "prepared": 5,  "slots": (4,2,0,0)},
		8:  {"cantrips": 3, "prepared": 6,  "slots": (4,2,0,0)},
		9:  {"cantrips": 3, "prepared": 6,  "slots": (4,2,0,0)},
		10: {"cantrips": 4, "prepared": 7,  "slots": (4,3,0,0)},
		11: {"cantrips": 4, "prepared": 8,  "slots": (4,3,0,0)},
		12: {"cantrips": 4, "prepared": 8,  "slots": (4,3,0,0)},
		13: {"cantrips": 4, "prepared": 9,  "slots": (4,3,2,0)},
		14: {"cantrips": 4, "prepared":10,  "slots": (4,3,2,0)},
		15: {"cantrips": 4, "prepared":10,  "slots": (4,3,2,0)},
		16: {"cantrips": 4, "prepared":11,  "slots": (4,3,3,0)},
		17: {"cantrips": 4, "prepared":11,  "slots": (4,3,3,0)},
		18: {"cantrips": 4, "prepared":11,  "slots": (4,3,3,0)},
		19: {"cantrips": 4, "prepared":12,  "slots": (4,3,3,1)},
		20: {"cantrips": 4, "prepared":13,  "slots": (4,3,3,1)},
		}

	def get_casting_stat(trickster):
		return "INT"

	def get_stats(trickster, key):
		lvl = getattr(trickster.character, "level", getattr(trickster.character, "Level", 1))
		table = ArcaneTrickster.ARCANE_TRICKSTER_TABLE
		if lvl > 20: lvl = 20
		data = table.get(lvl, {"cantrips": 0, "prepared": 0, "slots": (0,0,0,0)})
		if key == "cantrips":
			return data["cantrips"]
		if key == "prepared":
			return data["prepared"]
		if key == "slots":
			return {i+1: v for i, v in enumerate(data["slots"])}

	def get_spell_slots(trickster):
		return trickster.get_stats("slots")

	def available_spells(trickster):
		"""Spells this Arcane Trickster can learn, capped by slot level."""
		source = (
			SPELL_LISTS.get("Arcane Trickster")
			or SPELL_LISTS.get("Wizard")
			or {}
			)
		max_slot = max_slot_from(trickster.get_stats("slots"))
		unlocked = [key for key in source if key == 0 or key <= max_slot]
		return unique_spells([spell for lvl in unlocked for spell in source[lvl]])

	def prepare_spells(trickster):
		"""
		Select cantrips and prepared spells for Arcane Trickster.
		Mage Hand is always known and cannot be replaced.
		"""
		source = (
			SPELL_LISTS.get("Arcane Trickster")
			or SPELL_LISTS.get("Wizard")
			or {}
			)
		always = [MageHand] if getattr(trickster.character, "level", 1) >= 3 else []
		cantrips, known = progressive_learn(
			trickster.character,
			source,
			trickster.character.level,
			cantrips_at=lambda lvl: stats_at_level(trickster, lvl, "cantrips"),
			known_at=lambda lvl: stats_at_level(trickster, lvl, "prepared"),
			slots_at=lambda lvl: stats_at_level(trickster, lvl, "slots"),
			salt=CLASS_SALT["Arcane Trickster"],
			always=always,
			)
		finish_learning(trickster, cantrips, known)
		if getattr(trickster.character, "level", 1) >= 3:
			grant_spell(trickster.character, MageHand)


	def modifier(trickster):
		int_val = getattr(trickster.character.AS, "INT", 10)
		return (int_val - 10) // 2

	def html(trickster):
		return trickster.html_rules()

	def html_rules(trickster):
		index = html_spell_index(trickster, bullet="🎩")
		slots = trickster.get_stats("slots")
		slots_html = "<br>".join(f"<b>Level {lvl}</b>: <i>{num}</i> " for lvl, num in slots.items() if num > 0)
		return f"""
			<div class="npc-textbox" style="grid-column: span 3;">
				<h1 style="font-family: 'Iglesia'; font-size:    3.1em;">Arcane Trickster Spellcasting</h1>
				<p> As an Arcane Trickster, you've learned to weave subtle magic with your rogue's cunning. Your spells come from the Wizard list, cast using Intelligence. <br> You always know <b>Mage Hand</b>, and can select other cantrips and spells from the Wizard list. </p>
				</div>
			<div class="npc-textbox" style="grid-column: span 1;">
				<h2>Spell Slots:</h2> {slots_html} <br>  You regain all expended slots when you finish a Long Rest.
				{index}
				<h2>Arcane Focus</h2>
				You can use an Arcane Focus (such as a wand or scepter), as a Spellcasting Focus for your Wizard spells.
				</div>
			<div class="npc-textbox" style="margin-bottom: 1em;">
				<h2>Spell Save DC:</h2> {trickster.spell_save_dc()}<br>
				</div>
			<div class="npc-textbox" style="margin-bottom: 1em;">
				<h2 style="font-size:    1.35em;">Spell Attack Bonus:</h2> +{trickster.spell_attack_bonus()}
				</div>
			"""

	def __str__(trickster):
		return trickster.html_rules()


def genie_kind(character):
	kind = getattr(character, "genie_kind", None)
	if kind:
		return kind
	rng = caster_rng(character, 0x6E1)
	kind = rng.choice(["Dao", "Djinni", "Efreeti", "Marid"])
	character.genie_kind = kind
	return kind


def warlock_patron_spells(caster):
	"""Always-prepared patron spells. Grows with level; never reshuffles."""
	subclass = caster.character.subclass
	level = caster.level
	spells = []
	if subclass == "Celestial":
		if level >= 3: spells += [Aid, CureWounds, GuidingBolt, LesserRestoration, Light, SacredFlame]
		if level >= 5: spells += [Daylight, Revivify]
		if level >= 7: spells += [GuardianFaith, WallofFire]
		if level >= 9: spells += [GreaterRestoration, SummonCelestial]
	elif subclass == "Fiend":
		if level >= 3: spells += [BurningHands, Command, ScorchingRay, Suggestion]
		if level >= 5: spells += [Fireball, StinkingCloud]
		if level >= 7: spells += [FireShield, WallofFire]
		if level >= 9: spells += [Geas, InsectPlague]
	elif subclass == "Great Old One":
		if level >= 3: spells += [DetectThoughts, DissonantWhispers, PhantasmalForce, HideousLaughter]
		if level >= 5: spells += [Clairvoyance, HungerHadar]
		if level >= 7: spells += [Confusion, SummonAberration]
		if level >= 9: spells += [ModifyMemory, Telekinesis]
		if level >= 10: spells += [Hex]
	elif subclass == "Genie":
		if level >= 1: spells += [DetectEvilandGood]
		if level >= 3: spells += [PhantasmalForce]
		if level >= 5: spells += [CreateFoodWater]
		if level >= 7: spells += [PhantasmalKiller]
		if level >= 9: spells += [Creation]
		if level >= 17: spells += [Wish]
		patron = genie_kind(caster.character)
		if patron == "Dao":
			if level >= 1: spells += [Sanctuary]
			if level >= 3: spells += [SpikeGrowth]
			if level >= 5: spells += [MeldIntoStone]
			if level >= 7: spells += [StoneShape]
			if level >= 9: spells += [WallStone]
		elif patron == "Djinni":
			if level >= 1: spells += [Thunderwave]
			if level >= 3: spells += [GustOfWind]
			if level >= 5: spells += [WindWall]
			if level >= 7: spells += [GreaterInvisibility]
			if level >= 9: spells += [Seeming]
		elif patron == "Efreeti":
			if level >= 1: spells += [BurningHands]
			if level >= 3: spells += [ScorchingRay]
			if level >= 5: spells += [Fireball]
			if level >= 7: spells += [FireShield]
			if level >= 9: spells += [FlameStrike]
		elif patron == "Marid":
			if level >= 1: spells += [FogCloud]
			if level >= 3: spells += [Blur]
			if level >= 5: spells += [SleetStorm]
			if level >= 7: spells += [ControlWater]
			if level >= 9: spells += [ConeofCold]
	elif subclass == "Archfey":
		if level >= 3: spells += [CalmEmotions, FaerieFire, MistyStep, PhantasmalForce, Sleep]
		if level >= 5: spells += [Blink, PlantGrowth]
		if level >= 7: spells += [DominateBeast, GreaterInvisibility]
		if level >= 9: spells += [DominatePerson, Seeming]
	if level >= 9:
		spells += [ContactOtherPlane]
	return unique_spells(spells)


class Warlock(Spellcaster):
	def __init__(caster, character,known=None):
		if known is None:     known = []
		caster.class_name     = "Warlock"
		caster.character     = character
		caster.level         = character.level
		caster.granted_spells = []
		caster.always_prepared = set()
		caster.prepared_spells = []
		caster.catalog_known = True
		caster.mystic_arcanum = []
		caster.spell_slots     = caster.get_spell_slots()
		caster.spells_available = caster.available_spells()
		caster.spells_known = known
		caster.casting_stat = caster.get_casting_stat()
		caster.prepare_spells()
		# Optionally track invocations, pact, arcanum

	def get_casting_stat(caster):
		return "CHA"

	def get_stats(caster, key):
		row = casting_row("Warlock", caster.level)
		if key == "cantrips":
			return row.get("cantrips", 0)
		if key == "prepared":
			return row.get("prepared", 0)
		if key == "slots":
			return {row["slot_level"]: row["slots"]}
		if key == "slot_level":
			return row["slot_level"]

	def get_spell_slots(caster):
		return caster.get_stats("slots")

	def available_spells(caster):
		"""Returns all spells this character can *prepare* at their current level."""
		table = class_spell_table(caster.character.char_class)
		max_slot = caster.get_stats("slot_level")
		# Only show spells up to max_slot (warlock can never prepare 6+)
		unlocked = [lvl for lvl in table if lvl <= max_slot]
		spells = [s for lvl in unlocked for s in table[lvl]]
		return spells

	def prepare_spells(caster):
		table = class_spell_table("Warlock")
		cantrips, known = progressive_learn(
			caster.character,
			table,
			caster.level,
			cantrips_at=lambda lvl: stats_at_level(caster, lvl, "cantrips"),
			known_at=lambda lvl: stats_at_level(caster, lvl, "prepared"),
			slots_at=lambda lvl: stats_at_level(caster, lvl, "slots"),
			salt=CLASS_SALT["Warlock"],
			)
		finish_learning(caster, cantrips, known)
		for spell in warlock_patron_spells(caster):
			grant_spell(caster.character, spell)
		# Mystic Arcanum — one per slot-level, stable as the warlock levels
		caster.mystic_arcanum = []
		arcanum_requirements = {6: 11, 7: 13, 8: 15, 9: 17}
		rng = caster_rng(caster.character, 0xA0C ^ CLASS_SALT["Warlock"])
		already = {spell_key(spell) for spell in catalog_spells(caster)}
		for spell_lvl, req_level in arcanum_requirements.items():
			if caster.level >= req_level:
				pool = table.get(spell_lvl, [])
				added = pick_new(pool, 1, rng, already)
				for spell in added:
					caster.mystic_arcanum.append(spell)
					grant_spell(caster.character, spell)
					already.add(spell_key(spell))

	def modifier(caster):
		# CHA-based, so use character abilities
		return (getattr(caster.character.AS, caster.casting_stat) - 10) // 2

	def html(caster):
		return caster.html_rules()

	def html_rules(caster):
		n_prep = caster.get_stats("prepared")
		arcanums   = getattr(caster, "mystic_arcanum", [])
		index = html_spell_index(caster, bullet="🔮")

		slots = caster.get_stats("slots")
		slot_level = caster.get_stats("slot_level")
		symb = "⚀"
		if slot_level == 2: symb = "⚁"
		if slot_level == 3: symb = "⚂"
		if slot_level == 4: symb = "⚃"
		if slot_level == 5: symb = "⛥"
		slot_str = f"""
			<h3>{slots[slot_level]} × Level {slot_level} Spell Slot(s)</h3>
			<br><h2 style="font-family: 'Iglesia'; font-size: 2.1em;">"""
		for j in range(slots[slot_level]):
			slot_str += f" {symb} "
		slot_str += "</h2>"

		if arcanums:
			lis = "".join(f"<li>{spell_mark(s)}</li>" for s in arcanums)
			arcanum = f"""
				<div class="npc-textbox" style="grid-column: span 1;">
					<h2 style="font-family: 'Iglesia'; font-size: 2.1em;">Mystic Arcanum</h2>
					<p>You know these special once‐per‐rest spells:</p>
					<ul style="list-style-type: '🪬'; text-align: left; font-family: 'Iglesia'">
						{lis}
						</ul>
					<p><i>Each arcanum can be cast once per <i>Long Rest</i> without spending a slot.</i></p>
					</div>
				<div class="npc-textbox" style="grid-column: span 1;">
					<h1 style="font-family: 'Iglesia';"">Spellcasting Focus.</h1>
					You can use an Arcane Focus (a wand, a cristal ball, or
					scepter are exmples or Foci) as a <i>Spellcasting Focus</i>
					for your Warlock spells.
					</div>
					"""
		else:
			arcanum = ""

		return f"""
		<div class="npc-textbox" style="grid-column: span 3;">
			<h1 style="font-family: 'Iglesia'; font-size: 3.1em;">Warlock Pact Magic</h1>
			<p>As a warlock, your pact grants you spellcasting drawn from a supernatural patron. Pact Magic uses <b>Charisma</b> and works differently from other spellcasters.</p>
		</div>
		<div class="npc-textbox" style="grid-column: span 1;">
			<h2 style="font-family: 'Iglesia'; font-size: 2.1em;">Pact Magic Slots:</h2>
			{slot_str}
			<br><b>All slots are cast at highest slot level.<br>
			You regain all slots on a Short or Long Rest.</b>
		</div>
		<div class="npc-textbox" style="grid-column: span 1;">
			<h3 style="font-family: 'Iglesia'; font-size: 2.1em;">Prepared Spells</h3>
			You prepare {n_prep} warlock spells at the end of each long rest. Each must be of a level you can cast.<br>
			{index}
			<h3 style="font-family: 'Iglesia'; font-size: 2.1em;">Cantrips</h3>
			You always know {caster.get_stats("cantrips")} cantrips from the warlock list.<br>
		</div>

		{arcanum}
		"""

	def __str__(caster):
		return caster.html_rules()

# Factory to get the appropriate class
def spellcaster(character):
	if "Wizard" in character:
		return Wizard(character)
	if "Sorcerer" in character:
		return Sorcerer(character)
	if "Monk" in character:
		return Monk(character)
	if "Warlock" in character:
		return Warlock(character)
	if "Eldritch Knight" in character:
		return EldritchKnight(character)
	if "Arcane Trickster" in character:
		return ArcaneTrickster(character)
	if "Ranger" in character:
		return Ranger(character)
	if "Druid" in character:
		return Druid(character)
	# Add further subclasses or specific cases as needed
	return None
