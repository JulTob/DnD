# AtlasLusoris/Grimoire_of_Spellcasters.py

import random
from AtlasMagia.Lodge_of_Spells import *


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



class Spellcaster:
	def __init__(caster, character, known=None):
		if known is None:      known = []
		caster.character     = character
		caster.level         = character.level
		caster.casting_stat = caster.get_casting_stat()
		caster.spell_slots     =  caster.get_spell_slots()
		caster.spells_available = caster.available_spells()
		caster.spells_known = known
		caster.prepare_spells()

	def get_casting_stat(caster):
		return "INT"  # default, override in subclasses

	def get_spell_slots(caster):
		slots_table = {}
		return slots_table

	def available_spells(caster):
		"""Return all spells this character can *learn* at their current level."""
		table = SPELL_LISTS.get(caster.character.char_class, {})
		# Collapse all spell levels the character has unlocked
		unlocked = [lvl for lvl in table if lvl <= caster.level]
		spells = [s for lvl in unlocked for s in table[lvl]]
		return spells

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

	def __str__(caster):
		spells_names = "".join(f"<li>〖{spell.level}〗{spell.name}</li>" for spell in caster.spells_known)
		slots_html = ", ".join(f"Level {lvl}: {num}" for lvl, num in caster.spell_slots.items())
		spells_html = "".join(f"""<div class="npc-textbox">{spell}</div>""" for spell in caster.spells_known)

		return f"""
			<h1 style="font-family: 'Iglesia'; font-size:    3.1em; ">{caster.character.char_class} Spellcasting</h1>
			<p><b>Spell Slots:</b> {slots_html}</p>
			<ul style="list-style-type: '🪄'; text-align: left; font-family: 'Iglesia'">{spells_names}</ul>
			</div>
			<div class="npc-textbox" style="margin-bottom: 1em;">
				<b>Spell Save DC:</b> {caster.spell_save_dc()}<br>
				<b>Spell Attack Bonus:</b> +{caster.spell_attack_bonus()}
				</div>
			{spells_html}
		"""

	def html(caster):
		if not caster.spells_known:
			return "<i>No spells known</i>"
		list_items = "".join(f"<li>{s.name}</li>" for s in caster.spells_known)
		return f"""<div class="npc-textbox"><b>Spellcasting</b><ul>{list_items}</ul></div>"""

class Wizard(Spellcaster):
	def __init__(caster, character, known=None):
		if known is None:      known = []
		caster.class_name     = "Wizard"
		caster.character     = character
		caster.level         = character.level
		caster.spell_slots     =  caster.get_spell_slots()
		caster.spells_available = caster.available_spells()
		caster.spells_known = known
		caster.casting_stat = caster.get_casting_stat()
		caster.prepare_spells()

	def get_casting_stat(caster):
		return "INT"

	def get_stats(caster, key):
		table = {
			1:  {"cantrips": 3, "spells": 4,     "slots": (2,0,0,0,0,0,0,0,0)},
			2:  {"cantrips": 3, "spells": 5,      "slots": (3,0,0,0,0,0,0,0,0)},
			3:  {"cantrips": 3, "spells": 6,      "slots": (4,2,0,0,0,0,0,0,0)},
			4:  {"cantrips": 4, "spells": 7,      "slots": (4,3,0,0,0,0,0,0,0)},
			5:  {"cantrips": 4, "spells": 9,      "slots": (4,3,2,0,0,0,0,0,0)},
			6:  {"cantrips": 4, "spells": 10,      "slots": (4,3,3,0,0,0,0,0,0)},
			7:  {"cantrips": 4, "spells": 11,      "slots": (4,3,3,1,0,0,0,0,0)},
			8:  {"cantrips": 4, "spells": 12,      "slots": (4,3,3,2,0,0,0,0,0)},
			9:  {"cantrips": 4, "spells": 14,      "slots": (4,3,3,3,1,0,0,0,0)},
			10: {"cantrips": 5, "spells": 15,      "slots": (4,3,3,3,2,0,0,0,0)},
			11: {"cantrips": 5, "spells": 16,      "slots": (4,3,3,3,2,1,0,0,0)},
			12: {"cantrips": 5, "spells": 16,      "slots": (4,3,3,3,2,1,0,0,0)},
			13: {"cantrips": 5, "spells": 17,      "slots": (4,3,3,3,2,1,1,0,0)},
			14: {"cantrips": 5, "spells": 18,      "slots": (4,3,3,3,2,1,1,0,0)},
			15: {"cantrips": 5, "spells": 19,      "slots": (4,3,3,3,2,1,1,1,0)},
			16: {"cantrips": 5, "spells": 21,      "slots": (4,3,3,3,2,1,1,1,0)},
			17: {"cantrips": 5, "spells": 22,      "slots": (4,3,3,3,2,1,1,1,1)},
			18: {"cantrips": 5, "spells": 23,      "slots": (4,3,3,3,3,1,1,1,1)},
			19: {"cantrips": 5, "spells": 24,      "slots": (4,3,3,3,3,2,1,1,1)},
			20: {"cantrips": 5, "spells": 25,      "slots": (4,3,3,3,3,2,2,1,1)},
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

	def prepare_spells(caster):
		num_spells = caster.level*2 + 4
		available = caster.available_spells()
		caster.spells_known = random.sample(available, min(len(available), num_spells))

	def modifier(caster):
		return (getattr(caster.character.AS, caster.casting_stat) - 10) // 2

	def html(caster):
		return str(caster)

	def __str__(caster):
		n = caster.get_stats("spells")
		cantrips = [s for s in caster.spells_known if s.level == 0]
		other_spells = [s for s in caster.spells_known if s.level > 0]

		random.shuffle(other_spells)
		prepared = other_spells[:n]
		unprepared = other_spells[n:]
		all_spells = sorted(prepared + unprepared, key=lambda s: (s.level, s.name))
		spells = ""
		for spell in cantrips:
			spells += f"<li>【{spell.level}】{spell.name}</li>"
		for spell in all_spells:
			if spell in prepared or spell.level==0:
				spells += f"<li>【{spell.level}】{spell.name}</li>"
			else:
				spells += f"<li>〖{spell.level}〗{spell.name}</li>"
		slots_html = "<br>".join(
			f"<b>Level {lvl}</b>: <i>{num}</i>"
			for lvl, num in caster.spell_slots.items()
			if num  # This skips levels with 0 slots
			)
		spells_html = "".join(
			f"""<div class="npc-textbox">{spell}</div>"""
			for spell in cantrips
			)
		spells_html += "".join(
			f"""<div class="npc-textbox">{spell}</div>"""
			for spell in all_spells
			)
		return f"""
			<div class="npc-textbox" style="grid-column: span 3;">
				<h1 style="font-family: 'Iglesia'; font-size:    3.1em; ">
					Wizard Spellcasting</h1>
				<p> As a student of arcane magic, you have learned to cast spells. </p>
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
			<ul style="list-style-type: '🪄'; text-align: left; font-family: 'Iglesia' ">
				{spells}</ul>
			<h2>Arcane Focus</h2>
			You can use an Arcane Focus (such as a wand or scepter),  as a Spellcasting Focus for your Wizard spells.
			</div>
			{spells_html}
			"""

class Druid(Spellcaster):
	def __init__(caster, character, known=None):
		if known is None:      known = []
		caster.class_name     = "Druid"
		caster.character     = character
		caster.level         = character.level
		caster.spell_slots     =  caster.get_spell_slots()
		caster.spells_available = caster.available_spells()
		caster.spells_known = known
		caster.casting_stat = caster.get_casting_stat()
		caster.prepare_spells()

	def get_casting_stat(caster):
		return "WIS"

	def get_stats(caster, key):
		table = {
			1:  {"cantrips": 2, "spells": 4,	"slots": (2,0,0,0,0,0,0,0,0)},
			2:  {"cantrips": 2, "spells": 5, 	"slots": (3,0,0,0,0,0,0,0,0)},
			3:  {"cantrips": 2, "spells": 6,	"slots": (4,2,0,0,0,0,0,0,0)},
			4:  {"cantrips": 3, "spells": 7, 	"slots": (4,3,0,0,0,0,0,0,0)},
			5:  {"cantrips": 3, "spells": 9, 	"slots": (4,3,2,0,0,0,0,0,0)},
			6:  {"cantrips": 3, "spells": 10, 	"slots": (4,3,3,0,0,0,0,0,0)},
			7:  {"cantrips": 3, "spells": 11, 	"slots": (4,3,3,1,0,0,0,0,0)},
			8:  {"cantrips": 3, "spells": 12, 	"slots": (4,3,3,2,0,0,0,0,0)},
			9:  {"cantrips": 3, "spells": 14, 	"slots": (4,3,3,3,1,0,0,0,0)},
			10: {"cantrips": 4, "spells": 15, 	"slots": (4,3,3,3,2,0,0,0,0)},
			11: {"cantrips": 4, "spells": 16, 	"slots": (4,3,3,3,2,1,0,0,0)},
			12: {"cantrips": 4, "spells": 16, 	"slots": (4,3,3,3,2,1,0,0,0)},
			13: {"cantrips": 4, "spells": 17, 	"slots": (4,3,3,3,2,1,1,0,0)},
			14: {"cantrips": 4, "spells": 17, 	"slots": (4,3,3,3,2,1,1,0,0)},
			15: {"cantrips": 4, "spells": 18, 	"slots": (4,3,3,3,2,1,1,1,0)},
			16: {"cantrips": 4, "spells": 18, 	"slots": (4,3,3,3,2,1,1,1,0)},
			17: {"cantrips": 4, "spells": 19, 	"slots": (4,3,3,3,2,1,1,1,1)},
			18: {"cantrips": 4, "spells": 20, 	"slots": (4,3,3,3,3,1,1,1,1)},
			19: {"cantrips": 4, "spells": 21, 	"slots": (4,3,3,3,3,2,1,1,1)},
			20: {"cantrips": 4, "spells": 22, 	"slots": (4,3,3,3,3,2,2,1,1)},
			}
		lvl = caster.level
		if lvl > 20: lvl = 20
		value = table.get(lvl, {"cantrips": 0, "spells": 0, "slots": (0,0,0,0)})
		if key == "cantrips":
			result = value["cantrips"]
			if character.Primal_Order and character.Primal_Order == "Magician":
				result += 1
			return result
		if key == "spells":
			return value["spells"]
		if key == "slots":
			return {i + 1: val for i, val in enumerate(value["slots"])}

	def get_spell_slots(caster):
		return caster.get_stats("slots")

	def prepare_spells(caster):
		num_spells = caster.level*2 + 4
		available = caster.available_spells()
		caster.spells_known = random.sample(available, min(len(available), num_spells))

	def modifier(caster):
		return (getattr(caster.character.AS, caster.casting_stat) - 10) // 2

	def html(caster):
		return str(caster)

	def __str__(caster):
		n = caster.get_stats("spells")
		cantrips = [s for s in caster.spells_known if s.level == 0]
		other_spells = [s for s in caster.spells_known if s.level > 0]

		random.shuffle(other_spells)
		prepared = other_spells[:n]
		unprepared = other_spells[n:]
		all_spells = sorted(prepared + unprepared, key=lambda s: (s.level, s.name))
		spells = ""
		for spell in cantrips:
			spells += f"<li>【{spell.level}】{spell.name}</li>"
		for spell in all_spells:
			if spell in prepared or spell.level==0:
				spells += f"<li>【{spell.level}】{spell.name}</li>"
			else:
				spells += f"<li>〖{spell.level}〗{spell.name}</li>"
		slots_html = "<br>".join(
			f"<b>Level {lvl}</b>: <i>{num}</i>"
			for lvl, num in caster.spell_slots.items()
			if num  # This skips levels with 0 slots
			)
		spells_html = "".join(
			f"""<div class="npc-textbox">{spell}</div>"""
			for spell in cantrips
			)
		spells_html += "".join(
			f"""<div class="npc-textbox">{spell}</div>"""
			for spell in all_spells
			)
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
			<ul style="list-style-type: '🪄'; text-align: left; font-family: 'Iglesia' ">
				{spells}</ul>
			<h2>Arcane Focus</h2>
			You can use an Arcane Focus (such as a wand or scepter),  as a Spellcasting Focus for your Druid spells.
			</div>
			{spells_html}
			"""

class Ranger(Spellcaster):
	def __init__(self, character, known: list[Spell] | None = None):
		super().__init__(character, known or [])

	def get_casting_stat(caster):
		return "WIS"

	def get_known_cap(self) -> int:
		wis_mod = self.modifier()
		return max(1, (self.level // 2) + wis_mod)

	# map the slot tuple for this level into {level: slots}
	def get_spell_slots(self):
		row = Ranger.HALF_CASTER_SLOTS[self.level]
		return {i + 1: n for i, n in enumerate(row) if n}

	# same helper used by base class
	def modifier(self) -> int:
		return (getattr(self.character.AS, self.get_casting_stat()) - 10) // 2

	def get_stats(caster, key):
		"""Spellcasting stats: spell slots and number of prepared spells."""
		table = {
			1:  {"prepared": 2,  "slots": (2,0,0,0,0)},
			2:  {"prepared": 3,  "slots": (2,0,0,0,0)},
			3:  {"prepared": 4,  "slots": (3,0,0,0,0)},
			4:  {"prepared": 5,  "slots": (3,0,0,0,0)},
			5:  {"prepared": 6,  "slots": (4,2,0,0,0)},
			6:  {"prepared": 6,  "slots": (4,2,0,0,0)},
			7:  {"prepared": 7,  "slots": (4,3,0,0,0)},
			8:  {"prepared": 7,  "slots": (4,3,0,0,0)},
			9:  {"prepared": 9,  "slots": (4,3,2,0,0)},
			10: {"prepared": 9,  "slots": (4,3,2,0,0)},
			11: {"prepared": 10, "slots": (4,3,3,0,0)},
			12: {"prepared": 10, "slots": (4,3,3,0,0)},
			13: {"prepared": 11, "slots": (4,3,3,1,0)},
			14: {"prepared": 11, "slots": (4,3,3,1,0)},
			15: {"prepared": 12, "slots": (4,3,3,2,0)},
			16: {"prepared": 12, "slots": (4,3,3,2,0)},
			17: {"prepared": 14, "slots": (4,3,3,3,1)},
			18: {"prepared": 14, "slots": (4,3,3,3,1)},
			19: {"prepared": 15, "slots": (4,3,3,3,2)},
			20: {"prepared": 15, "slots": (4,3,3,3,2)},
		}
		lvl = min(caster.level, 20)
		entry = table.get(lvl, {"prepared": 0, "slots": (0,0,0,0,0)})
		if key == "prepared":
			return entry["prepared"]
		if key == "slots":
			return {i + 1: val for i, val in enumerate(entry["slots"])}

	def get_spell_slots(caster):
		return caster.get_stats("slots")

	def prepare_spells(caster):
		n = caster.get_stats("prepared")
		available = [s for s in caster.available_spells() if s.level > 0]
		random.shuffle(available)
		caster.spells_known = available[:n]

	def modifier(caster):
		return (getattr(caster.character.AS, caster.casting_stat) - 10) // 2

	def html(caster):
		return str(caster)

	def __str__(caster):
		n = caster.get_stats("prepared")

		prepared = caster.spells_known[:n]
		unprepared = caster.spells_known[n:]
		all_spells = sorted(prepared + unprepared, key=lambda s: (s.level, s.name))
		spells = "".join(
			f"<li>【{s.level}】{s.name}</li>" if s in prepared else f"<li>〖{s.level}〗{s.name}</li>"
			for s in all_spells
		)
		slots_html = "<br>".join(
			f"<b>Level {lvl}</b>: <i>{num}</i>"
			for lvl, num in caster.spell_slots.items()
			if num
		)
		spells_descriptions = "".join(f'<div class="npc-textbox">{spell}</div>' for spell in all_spells)

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
			<ul style="list-style-type: '🍀'; font-family: 'Iglesia'; text-align: left;">
				{spells}
			</ul>
		</div>
		{spells_descriptions}
		"""

class Sorcerer(Spellcaster):
	def __init__(caster, character):
		super().__init__(character)
		caster.metamagic_points = caster.level  # Basic rule, extend as needed

	def get_casting_stat(caster):
		return "CHA"

	def get_spell_slots(caster):
		slots_table = {
			1: {1: 2}, 2: {1: 3}, 3: {1: 4, 2: 2},
			4: {1: 4, 2: 3}, # Extend as needed
		}
		return slots_table.get(caster.level, {})

	def prepare_spells(caster):
		num_spells = caster.level + 1
		available = caster.available_spells()
		caster.spells_known = random.sample(available, min(len(available), num_spells))

	def __str__(caster):
		base_str = super().__str__()
		return base_str + f"<p><strong>Metamagic Points:</strong> {caster.metamagic_points}</p>"


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
		return str(caster)

	def __str__(caster):
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
		"""Return all spells this character can *learn* at their current level."""
		table = (SPELL_LISTS.get(caster.character.subclass)
				or SPELL_LISTS.get("Wizard", {}))
		# Collapse all spell levels the character has unlocked
		unlocked = [lvl for lvl in table if lvl <= caster.level]
		spells = [s for lvl in unlocked for s in table[lvl]]
		for lvl in unlocked:
			spells.extend(table[lvl])
		return spells

	def prepare_spells(caster):
		cantrip_pool = [s for s in caster.spells_available if int(s.level) == 0]
		leveled_pool = [s for s in caster.spells_available if int(s.level) > 0]

		caster.spells_known = random.sample(cantrip_pool, min(len(cantrip_pool), caster.get_stats("cantrips")))

		slots = caster.get_stats("slots")
		weights = {lvl: slots.get(lvl, 0) for lvl in range(1, 10)}
		leveled_pool = list({s.name: s for s in leveled_pool}.values())
		leveled_weighted = [(s, weights.get(int(s.level), 0)) for s in leveled_pool if weights.get(int(s.level), 0) > 0]

		spells, spell_weights = zip(*leveled_weighted) if leveled_weighted else ([], [])

		chosen = random.choices(spells, weights=spell_weights, k=min(len(spells), caster.get_stats("spells")))
		unique_chosen = []
		seen = set()
		for s in chosen:
			if s.name not in seen:
				unique_chosen.append(s)
				seen.add(s.name)
		caster.spells_known += unique_chosen[:caster.get_stats("spells")]


	def modifier(caster):
		return (getattr(caster.character.AS, caster.casting_stat) - 10) // 2

	def html(caster):
		return str(caster)

	def __str__(caster):
		ordered_spells = sorted(caster.spells_known, key=lambda s: int(s.level))
		spells_names = "".join(f"<li>〖{spell.level}〗{spell.name}</li>" for spell in ordered_spells)
		spells_html = "".join(f"""<div class="npc-textbox">{spell}</div>""" for spell in ordered_spells)
		slots_html = "<br>".join(f"<b>Level {lvl}</b>: <i>{num}</i> " for lvl, num in caster.spell_slots.items())
		return f"""
			<div class="npc-textbox" style="grid-column: span 1;">
			<h1 style="font-family: 'Iglesia'; font-size:    3.1em; ">{caster.character.subclass} Spellcasting</h1>
			<p> Eldritch Knights combine the martial mastery common to all Fighters with a careful study of magic. Their spells both complement and extend their combat skills.<br> You have learned to cast spells. </p>
			<h2>Spell Slots:</h2> {slots_html} <br>  You regain all expended slots when you finish a Long Rest.</p>
			<ul style="list-style-type: '♟️'; text-align: left; font-family: 'Iglesia' ">{spells_names}</ul>
			<h2>Arcane Focus</h2>
			You can use an Arcane Focus (such as a wand or scepter),  as a Spellcasting Focus for your Wizard spells.
			</div>
			<div class="npc-textbox" style="margin-bottom: 1em;">
				<b>Spell Save DC:</b> {caster.spell_save_dc()}<br>
				<b>Spell Attack Bonus:</b> +{caster.spell_attack_bonus()}
				</div>
			{spells_html}
			"""

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
		"""Return all spells this Arcane Trickster can learn/cast at their current level."""
		# Prefer the tailored Arcane Trickster list
		source = (
			SPELL_LISTS.get("Arcane Trickster")
			or
			SPELL_LISTS.get("Wizard")
			)
		if not source:
			return []
		# Unlock spells up to allowed level
		lvl = getattr(trickster.character, "level", getattr(trickster.character, "Level", 1))
		# Find max spell slot level available
		max_slot = max(i+1 for i, n in enumerate(trickster.get_stats("slots").values()) if n > 0)
		unlocked_levels = [k for k in source if k <= max_slot]
		# Collate spells
		spells = [spell for lvl in unlocked_levels for spell in source[lvl]]
		return spells

	def prepare_spells(trickster):
		"""
		Select cantrips and prepared spells for Arcane Trickster.
		Mage Hand is always known and cannot be replaced.
		"""
		# Cantrips - always include Mage Hand if present
		available_cantrips = [s for s in trickster.spells_available if int(s.level) == 0]
		mage_hand = next((c for c in available_cantrips if c.name == "Mage Hand"), None)
		other_cantrips = [c for c in available_cantrips if c.name != "Mage Hand"]

		n_cantrips = trickster.get_stats("cantrips")
		trickster.spells_known = [mage_hand] if mage_hand else []
		needed = n_cantrips - len(trickster.spells_known)

		if needed > 0:
			suggested = [MindSliver, MinorIllusion]
			chosen = []
			for rec in suggested:
				found = next((c for c in other_cantrips if c.name == rec), None)
				if found and found not in chosen:
					chosen.append(found)
			remaining = [c for c in other_cantrips if c not in chosen]
			random.shuffle(remaining)
			chosen += remaining
			trickster.spells_known += chosen[:needed]
		# Now select leveled spells (prepared)
		n_prepared = trickster.get_stats("prepared")
		leveled_pool = [s for s in trickster.spells_available if int(s.level) > 0]

		# Optionally: Recommended spells for level 3
		recommended = ["Charm Person", "Disguise Self", "Fog Cloud"]
		chosen_prepared = []
		for rec in recommended:
			found = next((s for s in leveled_pool if s.name == rec), None)
			if found and found not in chosen_prepared:
				chosen_prepared.append(found)
		# Fill remaining randomly
		remaining = [s for s in leveled_pool if s not in chosen_prepared]
		random.shuffle(remaining)
		chosen_prepared += remaining[:max(0, n_prepared - len(chosen_prepared))]
		trickster.spells_known += chosen_prepared[:n_prepared]


	def modifier(trickster):
		int_val = getattr(trickster.character.AS, "INT", 10)
		return (int_val - 10) // 2

	def html(trickster):
		return str(trickster)

	def __str__(trickster):
		ordered_spells = sorted(trickster.spells_known, key=lambda s: int(s.level))
		spells_names = "".join(f"<li>〖{spell.level}〗{spell.name}</li>" for spell in ordered_spells)
		spells_html = "".join(f"""<div class="npc-textbox">{spell}</div>""" for spell in ordered_spells)
		slots = trickster.get_stats("slots")
		slots_html = "<br>".join(f"<b>Level {lvl}</b>: <i>{num}</i> " for lvl, num in slots.items() if num > 0)
		return f"""
			<div class="npc-textbox" style="grid-column: span 3;">
				<h1 style="font-family: 'Iglesia'; font-size:    3.1em;">Arcane Trickster Spellcasting</h1>
				<p> As an Arcane Trickster, you've learned to weave subtle magic with your rogue's cunning. Your spells come from the Wizard list, cast using Intelligence. <br> You always know <b>Mage Hand</b>, and can select other cantrips and spells from the Wizard list. </p>
				</div>
			<div class="npc-textbox" style="grid-column: span 1;">
				<h2>Spell Slots:</h2> {slots_html} <br>  You regain all expended slots when you finish a Long Rest.
				<ul style="list-style-type: '🎩'; text-align: left; font-family: 'Iglesia';">{spells_names}</ul>
				<h2>Arcane Focus</h2>
				You can use an Arcane Focus (such as a wand or scepter), as a Spellcasting Focus for your Wizard spells.
				</div>
			<div class="npc-textbox" style="margin-bottom: 1em;">
				<h2>Spell Save DC:</h2> {trickster.spell_save_dc()}<br>
				</div>
			<div class="npc-textbox" style="margin-bottom: 1em;">
				<h2 style="font-size:    1.35em;">Spell Attack Bonus:</h2> +{trickster.spell_attack_bonus()}
				</div>
			{spells_html}
			"""


# Warlock spellcasting progression for 2024 PHB
WARLOCK_SPELLCASTING_TABLE = {
		1:  {"cantrips": 2, "prepared": 3,  "slots": (1,),   "slot_level": 1},
		2:  {"cantrips": 2, "prepared": 3,  "slots": (2,),   "slot_level": 1},
		3:  {"cantrips": 2, "prepared": 4,  "slots": (2,),   "slot_level": 2},
		4:  {"cantrips": 3, "prepared": 5,  "slots": (2,),   "slot_level": 2},
		5:  {"cantrips": 3, "prepared": 6,  "slots": (2,),   "slot_level": 3},
		6:  {"cantrips": 3, "prepared": 7,  "slots": (2,),   "slot_level": 3},
		7:  {"cantrips": 3, "prepared": 8,  "slots": (2,),   "slot_level": 4},
		8:  {"cantrips": 3, "prepared": 9,  "slots": (2,),   "slot_level": 4},
		9:  {"cantrips": 3, "prepared": 10, "slots": (2,),   "slot_level": 5},
		10: {"cantrips": 4, "prepared": 10, "slots": (2,),   "slot_level": 5},
		11: {"cantrips": 4, "prepared": 11, "slots": (3,),   "slot_level": 5},
		12: {"cantrips": 4, "prepared": 11, "slots": (3,),   "slot_level": 5},
		13: {"cantrips": 4, "prepared": 12, "slots": (3,),   "slot_level": 5},
		14: {"cantrips": 4, "prepared": 12, "slots": (3,),   "slot_level": 5},
		15: {"cantrips": 4, "prepared": 13, "slots": (3,),   "slot_level": 5},
		16: {"cantrips": 4, "prepared": 13, "slots": (3,),   "slot_level": 5},
		17: {"cantrips": 4, "prepared": 14, "slots": (4,),   "slot_level": 5},
		18: {"cantrips": 4, "prepared": 14, "slots": (4,),   "slot_level": 5},
		19: {"cantrips": 4, "prepared": 15, "slots": (4,),   "slot_level": 5},
		20: {"cantrips": 4, "prepared": 15, "slots": (4,),   "slot_level": 5},
		}

class Warlock(Spellcaster):
	def __init__(caster, character,known=None):
		if known is None:     known = []
		caster.class_name     = "Warlock"
		caster.character     = character
		caster.level         = character.level
		caster.spell_slots     = caster.get_spell_slots()
		caster.spells_available = caster.available_spells()
		caster.spells_known = known
		caster.casting_stat = caster.get_casting_stat()
		caster.prepare_spells()
		# Optionally track invocations, pact, arcanum

	def get_casting_stat(caster):
		return "CHA"

	def get_stats(caster, key):
		lvl = min(caster.level, 20)
		value = WARLOCK_SPELLCASTING_TABLE.get(lvl, WARLOCK_SPELLCASTING_TABLE[20])
		if key == "cantrips":
			return value["cantrips"]
		if key == "prepared":
			return value["prepared"]
		if key == "slots":
			# Unlike wizards, Warlocks only ever have one slot level at a time
			return {value["slot_level"]: value["slots"][0]}
		if key == "slot_level":
			return value["slot_level"]

	def get_spell_slots(caster):
		return caster.get_stats("slots")

	def available_spells(caster):
		"""Returns all spells this character can *prepare* at their current level."""
		table = SPELL_LISTS.get(caster.character.char_class, {})
		max_slot = caster.get_stats("slot_level")
		# Only show spells up to max_slot (warlock can never prepare 6+)
		unlocked = [lvl for lvl in table if lvl <= max_slot]
		spells = [s for lvl in unlocked for s in table[lvl]]
		return spells

	def prepare_spells(caster):
		# 1) Pact‐spells
		n = caster.get_stats("prepared")
		# Warlocks can change prepared spells on level-up/long rest
		available = caster.available_spells()
		# Random for demo; in-app, let user select!
		chosen = random.sample(available, min(n, len(available)))

		# 2) Cantrips
		cantrip_pool = [s for s in available if int(s.level) == 0]
		cantrips = random.sample(cantrip_pool, min(len(cantrip_pool), caster.get_stats("cantrips")))

		caster.spells_known = cantrips + [s for s in chosen if int(s.level) > 0]
		if caster.character.subclass == "Celestial":
			if caster.level >= 3: caster.spells_known += [Aid, CureWounds,    GuidingBolt, LesserRestoration, Light, SacredFlame]
			if caster.level >= 5: caster.spells_known += [Daylight, Revivify]
			if caster.level >= 7: caster.spells_known += [GuardianFaith, WallofFire]
			if caster.level >= 9: caster.spells_known += [GreaterRestoration, SummonCelestial]
		if caster.character.subclass == "Fiend":
			if caster.level >= 3: caster.spells_known += [BurningHands,    Command,    ScorchingRay,    Suggestion]
			if caster.level >= 5: caster.spells_known += [Fireball, StinkingCloud]
			if caster.level >= 7: caster.spells_known += [FireShield, WallofFire]
			if caster.level >= 9: caster.spells_known += [Geas,    InsectPlague]
		if caster.character.subclass == "Great Old One":
			if caster.level >= 3: caster.spells_known += [DetectThoughts,    DissonantWhispers,    PhantasmalForce,    HideousLaughter]
			if caster.level >= 5: caster.spells_known += [Clairvoyance, HungerHadar]
			if caster.level >= 7: caster.spells_known += [Confusion,    SummonAberration]
			if caster.level >= 10: caster.spells_known += [Hex]
			if caster.level >= 9: caster.spells_known += [ModifyMemory,    Telekinesis]
		if caster.character.subclass == "Genie":
			if caster.level >= 1: caster.spells_known += [DetectEvilandGood]
			if caster.level >= 3: caster.spells_known += [PhantasmalForce]
			if caster.level >= 5: caster.spells_known += [CreateFoodWater]
			if caster.level >= 7: caster.spells_known += [PhantasmalKiller]
			if caster.level >= 9: caster.spells_known += [Creation]
			if caster.level >= 17: caster.spells_known += [Wish]
			random.seed(caster.character.seed)
			patron = random.choice([
				"Dao", "Djinni", "Efreeti", "Marid"
				])
			if patron == "Dao":
				if caster.level >= 1: caster.spells_known += [sanctuary]
				if caster.level >= 3: caster.spells_known += [SpikeGrowth]
				if caster.level >= 5: caster.spells_known += [MeldIntoStone]
				if caster.level >= 7: caster.spells_known += [StoneShape]
				if caster.level >= 9: caster.spells_known += [WallStone]
			if patron == "Djinni":
				if caster.level >= 1: caster.spells_known += [Thunderwave]
				if caster.level >= 3: caster.spells_known += [GustOfWind]
				if caster.level >= 5: caster.spells_known += [WindWall]
				if caster.level >= 7: caster.spells_known += [GreaterInvisibility]
				if caster.level >= 9: caster.spells_known += [Seeming]
			if patron == "Efreeti":
				if caster.level >= 1: caster.spells_known += [BurningHands]
				if caster.level >= 3: caster.spells_known += [ScorchingRay]
				if caster.level >= 5: caster.spells_known += [Fireball]
				if caster.level >= 7: caster.spells_known += [FireShield]
				if caster.level >= 9: caster.spells_known += [FlameStrike]
			if patron == "Marid":
				if caster.level >= 1: caster.spells_known += [FogCloud]
				if caster.level >= 3: caster.spells_known += [Blur]
				if caster.level >= 5: caster.spells_known += [SleetStorm]
				if caster.level >= 7: caster.spells_known += [ControlWater]
				if caster.level >= 9: caster.spells_known += [ConeofCold]
		if caster.character.subclass == "Archfey":
			if caster.level >= 3: caster.spells_known += [CalmEmotions, FaerieFire, MistyStep, PhantasmalForce, Sleep]
			if caster.level >= 5: caster.spells_known += [Blink, PlantGrowth]
			if caster.level >= 7: caster.spells_known += [DominateBeast, GreaterInvisibility]
			if caster.level >= 9: caster.spells_known += [DominatePerson,    Seeming]
		if caster.level >= 9: caster.spells_known += [ContactOtherPlane]


		# 3) Mystic Arcanum — one per slot-level at these thresholds:
		caster.mystic_arcanum = []
		arcanum_requirements = {6: 11, 7: 13, 8: 15, 9: 17}
		warlock_table = SPELL_LISTS.get(caster.character.char_class, {})
		for lvl, req_level in arcanum_requirements.items():
			if caster.level >= req_level:
				pool = warlock_table.get(lvl, [])
				if pool:
					caster.mystic_arcanum.append(random.choice(pool))

	def modifier(caster):
		# CHA-based, so use character abilities
		return (getattr(caster.character.AS, caster.casting_stat) - 10) // 2

	def html(caster):
		# simply delegate to __str__, which you’ve already written
		return str(caster)

	def __str__(caster):
		cantrips = [s for s in caster.spells_known if int(s.level) == 0]
		leveled = [s for s in caster.spells_known if int(s.level) > 0]
		n_prep = caster.get_stats("prepared")
		arcanums   = getattr(caster, "mystic_arcanum", [])

		spell_list = "".join(f"<li>【{s.level}】{s.name}</li>" for s in cantrips + leveled)
		spells_html = "".join(f"""<div class="npc-textbox">{s}</div>""" for s in cantrips + leveled)

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
			lis = "".join(f"<li>【{s.level}】{s.name}</li>" for s in arcanums)
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
			<ul style="list-style-type: '🔮'; text-align: left; font-family: 'Iglesia'">
				{spell_list}
			</ul>
			<h3 style="font-family: 'Iglesia'; font-size: 2.1em;">Cantrips</h3>
			You always know {caster.get_stats("cantrips")} cantrips from the warlock list.<br>
		</div>

		{arcanum}
		{spells_html}
		"""

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
