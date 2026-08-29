"""
Map of Domains — the mythic spheres an Order may be sworn to.

Each Domain is patterned on one published Dragonmark's three-slot template
(``intuition_die`` · ``signature_magic`` · ``spells_of_the_order``) but wears
a mythic name rather than a trade name, because a trade resists pairing and a
domain turns faces.  Making is not smithing, it is **the Forge**, and behind
it stand Hephaestus, Ptah, Goibniu, and Prometheus.  Finding is not tracking,
which is nobody's god; it is **the Hunt**, and half the pantheons have one.

Adding a Domain is one entry.  Nothing else needs to change.
"""

from __future__ import annotations

from AtlasLusoris.AtlasOfOrders.Grimoire_of_Orders import Domain, Facet
from AtlasMagia.Lodge_of_Spells import (
	Aid,
	Alarm,
	AnimalMessenger,
	ArcaneEye,
	ArcaneLock,
	Augury,
	Barkskin,
	BeastSense,
	Blink,
	Blur,
	CallLightning,
	CalmEmotions,
	Clairvoyance,
	ComprehendLanguages,
	ConjureAnimals,
	ContinualFlame,
	Creation,
	CreateFoodWater,
	CureWounds,
	Darkness,
	DetectMagic,
	DetectThoughts,
	DimensionDoor,
	DisguiseSelf,
	Divination,
	Druidcraft,
	ExpeditiousRetreat,
	Fabricate,
	FindTraps,
	FogCloud,
	Guidance,
	GlyphWarding,
	GreaterRestoration,
	GustofWind,
	Hallow,
	HealingWord,
	Heroism,
	HuntersMark,
	Identify,
	IllusoryScript,
	Invisibility,
	Knock,
	LegendLore,
	LesserRestoration,
	LightningBolt,
	Light,
	LocateCreature,
	LocateObject,
	Longstrider,
	MagicWeapon,
	MassHealingWord,
	Mending,
	Message,
	MinorIllusion,
	Mislead,
	MistyStep,
	Nondetection,
	PassWithoutTrace,
	Passwall,
	PhantomSteed,
	Prestidigitation,
	Revivify,
	RemoveCurse,
	Sanctuary,
	Scrying,
	SeeInvisibility,
	Seeming,
	Sending,
	Silence,
	SleetStorm,
	SpeakwithAnimals,
	SpeakwithDead,
	SpiderClimb,
	StoneShape,
	TeleportationCircle,
	Thaumaturgy,
	ThunderStep,
	TinyHut,
	Tongues,
	UnseenServant,
	WallofForce,
	WardingBond,
	WindWall,
	ZoneOfTruth,
	)


THE_FORGE = Domain(
	name="the Forge",
	mark="Making",
	checks=(
		"Arcana",
		"an Artisan's Tool",
		),
	cantrip=Mending,
	prepared=MagicWeapon,
	spells_of_the_order={
		1: (
			Identify,
			UnseenServant,
			),
		2: (
			ContinualFlame,
			Knock,
			),
		3: (
			GlyphWarding,
			),
		4: (
			Fabricate,
			StoneShape,
			),
		5: (
			Creation,
			),
		},
	facets=(
		Facet(
			name="the Maker",
			creed="nothing that lasts was ever found lying about; it was made, by someone, badly at first",
			goal="finish the work the first hands started and could not complete",
			),
		Facet(
			name="the Unmaker",
			creed="anything built can be taken apart, and someone must know how, in case it must be",
			goal="find the thing that should never have been built, and undo it",
			),
		Facet(
			name="the Fire Thief",
			creed="every craft worth knowing was stolen from something that wanted to keep it",
			goal="take one more secret out of a hand that has held it too long",
			),
		Facet(
			name="the Price",
			creed="the work always takes something back, and the honest maker names it in advance",
			goal="pay off a debt the workshop incurred before you were born",
			),
		),
	perks=(
		"any workshop with the sign above its door will lend you a bench, a fire, and silence",
		"you can put your mark on a thing, and the mark is honored where coin is not",
		"broken gear is not broken for long in your hands, and neither are locks",
		"there is always a commission waiting for someone who can be trusted with the interesting work",
		),
	sacrifices=(
		"the first perfect thing you ever make belongs to them, not to you",
		"you may never teach the finishing step to anyone outside the walls",
		"one day a year your hands are theirs, and you do not ask what for",
		"nothing you make may be signed with your own name",
		),
	descriptors=(
		"Quiet",
		"Unquenched",
		"Iron",
		"First",
		"Patient",
		"Stolen",
		),
	cores=(
		"Forge",
		"Anvil",
		"Ember",
		"Hammer",
		"Crucible",
		"Kiln",
		),
	relics=(
		"a hammer whose head is older than the haft, and older than the house",
		"an unfinished thing nobody will explain",
		"a mould for a key nobody has cut yet",
		),
	)


HOME = Domain(
	name="Home",
	mark="Hospitality",
	checks=(
		"Insight",
		"Persuasion",
		),
	cantrip=Guidance,
	prepared=Sanctuary,
	spells_of_the_order={
		1: (
			Alarm,
			Heroism,
			),
		2: (
			CalmEmotions,
			ZoneOfTruth,
			),
		3: (
			CreateFoodWater,
			TinyHut,
			),
		4: (
			Aid,
			),
		5: (
			Creation,
			),
		},
	facets=(
		Facet(
			name="the Hearth",
			creed="a roof given freely is the oldest law, older than kings and harder to repeal",
			goal="keep one door open in a country that has closed all the others",
			),
		Facet(
			name="the Salt Debt",
			creed="bread taken under a roof is a contract, and contracts are collected",
			goal="collect on a welcome that was accepted and then betrayed",
			),
		Facet(
			name="the Closing Door",
			creed="every house that shelters must also be able to refuse, or the shelter means nothing",
			goal="decide who is not to be let in, and make the decision stick",
			),
		Facet(
			name="the Last Comfort",
			creed="no one should go into the dark cold, hungry, or alone; that is all we promise",
			goal="see that a particular someone eats well, sleeps warm, and is not told why",
			),
		),
	perks=(
		"a bed and a hot meal wait wherever the sign is cut into the lintel, and no one asks your name",
		"you can read a room's loyalties before the second cup is poured",
		"quarrels go quiet when you stand up, because everyone knows whose house rules apply",
		"someone in every town owes the house a favor, and the house is willing to spend it on you",
		),
	sacrifices=(
		"you may not refuse a guest who asks properly, whatever they have done",
		"the house is told everything, including the parts you would rather forget",
		"you keep a place set for someone who is never coming back",
		"you cannot be the one who strikes first under any roof",
		),
	descriptors=(
		"Open",
		"Warm",
		"Last",
		"Quiet",
		"Barred",
		"Long",
		),
	cores=(
		"Hearth",
		"Table",
		"Threshold",
		"Roof",
		"Lintel",
		"Salt",
		),
	relics=(
		"a key to a house that burned down two generations ago",
		"a bowl that is always set out and never eaten from",
		"a guest-book with names in it that predate the building",
		),
	)


THE_HUNT = Domain(
	name="the Hunt",
	mark="Finding",
	checks=(
		"Survival",
		"Investigation",
		),
	cantrip=Druidcraft,
	prepared=HuntersMark,
	spells_of_the_order={
		1: (
			Longstrider,
			),
		2: (
			LocateObject,
			PassWithoutTrace,
			),
		3: (
			Clairvoyance,
			),
		4: (
			LocateCreature,
			Divination,
			),
		5: (
			Scrying,
			),
		},
	facets=(
		Facet(
			name="the Long Pursuit",
			creed="everything that runs leaves a line behind it, and a line can be walked to its end",
			goal="close a pursuit that three generations of the order have failed to finish",
			),
		Facet(
			name="the Debt Collector",
			creed="a thing owed is a thing findable; distance is only a delay",
			goal="bring back one who was let go, and this time bring them back",
			),
		Facet(
			name="What Should Stay Lost",
			creed="some things were hidden by wiser hands than ours, and we guard the hiding",
			goal="reach a buried thing before the people currently digging for it do",
			),
		Facet(
			name="the Provider",
			creed="the hunt is not sport; it is how the hall eats, and the hall must eat",
			goal="feed a place that is starving, whatever is left in the country to hunt",
			),
		),
	perks=(
		"you can pick up a cold trail that professionals abandoned, given a day and something they touched",
		"trackers, wardens, and poachers all read your kind on sight and would rather be owed than owing",
		"you always know roughly where you are, and precisely how you would leave",
		"lost things brought to you have a habit of being found, and finders pay well for that habit",
		),
	sacrifices=(
		"a hunt you accept is a hunt you finish, whoever the quarry turns out to be",
		"you tell the order what you found, even when the finding should die with you",
		"you may not hunt for sport, and they will know",
		"one name on the roster is not to be pursued, and you are not told why",
		),
	descriptors=(
		"Patient",
		"Silent",
		"Long",
		"Cold",
		"Unbroken",
		"Waiting",
		),
	cores=(
		"Trail",
		"Snare",
		"Horn",
		"Quarry",
		"Spoor",
		"Chase",
		),
	relics=(
		"a horn that is only sounded when a pursuit has ended",
		"a knot of hair from something that has never been named",
		"a map with one river drawn where no river is",
		),
	)


MERCY = Domain(
	name="Mercy",
	mark="Healing",
	checks=(
		"Medicine",
		"an Herbalism Kit",
		),
	cantrip=Prestidigitation,
	prepared=CureWounds,
	spells_of_the_order={
		1: (
			HealingWord,
			),
		2: (
			LesserRestoration,
			Aid,
			),
		3: (
			MassHealingWord,
			Revivify,
			RemoveCurse,
			),
		4: (
			Divination,
			),
		5: (
			Creation,
			),
		},
	facets=(
		Facet(
			name="the Open Hand",
			creed="suffering is not a verdict; it is a condition, and conditions are treated",
			goal="reach a place the healers were forbidden to enter",
			),
		Facet(
			name="the Clean Cut",
			creed="what is rotten is cut out early, or it takes the body with it",
			goal="excise something the world has been calling a person",
			),
		Facet(
			name="the Long Vigil",
			creed="most of the work is sitting with someone who will not get better",
			goal="be present at an ending that everyone else intends to miss",
			),
		Facet(
			name="the Plague-Bearer",
			creed="the hand that lifts a sickness understands it well enough to set it down elsewhere",
			goal="settle a debt with a city that let a sickness run",
			),
		),
	perks=(
		"you will be let past a quarantine line, a cordon, or a locked ward on your word alone",
		"the desperate find you, which means you hear what desperate people know",
		"apothecaries and grave-diggers alike extend the professional courtesy of not asking",
		"you can tell, at a glance, which wound in a room is the one that will kill",
		),
	sacrifices=(
		"you treat what is in front of you, including the thing you came to kill",
		"the order is told every remedy you invent, and decides who may have it",
		"you do not charge, ever, which is easy until it is not",
		"you carry the names of everyone you could not save, and recite them",
		),
	descriptors=(
		"Merciful",
		"Unflinching",
		"Sixth",
		"Quiet",
		"Bitter",
		"Faithful",
		),
	cores=(
		"Balm",
		"Vigil",
		"Lancet",
		"Cure",
		"Ward",
		"Mercy",
		),
	relics=(
		"a case of instruments with one empty slot",
		"a ledger of everyone the order has ever refused",
		"a mask that was worn during a plague nobody remembers",
		),
	)


THE_VEIL = Domain(
	name="the Veil",
	mark="Shadow",
	checks=(
		"Stealth",
		"Deception",
		),
	cantrip=MinorIllusion,
	prepared=DisguiseSelf,
	spells_of_the_order={
		1: (
			IllusoryScript,
			),
		2: (
			Darkness,
			Invisibility,
			Silence,
			),
		3: (
			Nondetection,
			Blink,
			),
		4: (
			Seeming,
			),
		5: (
			Mislead,
			),
		},
	facets=(
		Facet(
			name="the Kind Lie",
			creed="most truths arrive too early; our work is to hold them until they can be survived",
			goal="keep one fact buried for exactly as long as it needs to stay buried",
			),
		Facet(
			name="the Watcher",
			creed="what is done in the dark is done honestly, because no one is performing",
			goal="witness something that was arranged to have no witnesses",
			),
		Facet(
			name="the Second Face",
			creed="a person is a costume worn well; change it and you change what is possible",
			goal="become someone specific, for long enough, one time",
			),
		Facet(
			name="the Night Itself",
			creed="the dark was here first, and it is owed a measure of respect and a measure of feeding",
			goal="return something to the dark that was dragged out of it",
			),
		),
	perks=(
		"a room you have left cannot agree on what you looked like",
		"there is a mark chalked low on walls in every city, and it tells you which door is safe tonight",
		"you learn what servants, drivers, and night porters know, which is nearly everything",
		"you can vanish from a conversation without anyone recalling that it ended",
		),
	sacrifices=(
		"you are never publicly one of them, not even to save yourself",
		"a face you wear is retired when they say so, and you do not use it again",
		"you keep another member's secret over your own life",
		"you may not be photographed, painted, or described in writing",
		),
	descriptors=(
		"Silent",
		"Unlit",
		"Second",
		"Kindly",
		"Starless",
		"Veiled",
		),
	cores=(
		"Veil",
		"Mask",
		"Lantern",
		"Curtain",
		"Hour",
		"Shade",
		),
	relics=(
		"a mask with no eyeholes",
		"a lantern that is carried unlit",
		"a mirror the order keeps turned to the wall",
		),
	)


THE_ROAD = Domain(
	name="the Road",
	mark="Passage",
	checks=(
		"Acrobatics",
		"Cartographer's Tools",
		),
	cantrip=Message,
	prepared=ExpeditiousRetreat,
	spells_of_the_order={
		1: (
			Longstrider,
			ComprehendLanguages,
			),
		2: (
			MistyStep,
			SpiderClimb,
			),
		3: (
			PhantomSteed,
			Sending,
			),
		4: (
			DimensionDoor,
			),
		5: (
			Scrying,
			),
		},
	facets=(
		Facet(
			name="the Crossing",
			creed="a border is a decision somebody made, and decisions can be walked around",
			goal="open a route that was closed by treaty, wall, or worse",
			),
		Facet(
			name="the Messenger",
			creed="the word must arrive; what it costs to carry is a separate accounting",
			goal="deliver something that three previous couriers did not survive delivering",
			),
		Facet(
			name="the Return",
			creed="going is easy and common; the art is coming back, and bringing others back",
			goal="retrieve someone from a place people do not return from",
			),
		Facet(
			name="the Threshold Keeper",
			creed="some doors are shut for a reason, and someone has to stand at them",
			goal="close a way that was opened by people who did not read the warnings",
			),
		),
	perks=(
		"there is a house at the edge of most towns that will change your horse and forget your face",
		"you know which crossings are watched this season and which guard can be talked past",
		"couriers, smugglers, and pilgrims treat your word as a passport",
		"you can find a way in or out of almost any place, given an hour to look",
		),
	sacrifices=(
		"a delivery accepted is a delivery completed, and refusal is not offered twice",
		"you never travel the same road twice in the same season",
		"you carry what they give you without opening it",
		"you may not settle anywhere for longer than a season",
		),
	descriptors=(
		"Long",
		"Unmarked",
		"Old",
		"Turning",
		"Sealed",
		"Ninth",
		),
	cores=(
		"Road",
		"Gate",
		"Milestone",
		"Ford",
		"Crossing",
		"Key",
		),
	relics=(
		"a milestone rubbing from a road that no longer exists",
		"a key that fits a gate the order will not name",
		"a horse-brass passed down through eleven couriers",
		),
	)


THE_WORD = Domain(
	name="the Word",
	mark="Scribing",
	checks=(
		"History",
		"Calligrapher's Supplies",
		),
	cantrip=Thaumaturgy,
	prepared=ComprehendLanguages,
	spells_of_the_order={
		1: (
			IllusoryScript,
			Identify,
			),
		2: (
			Silence,
			Augury,
			),
		3: (
			Sending,
			Tongues,
			SpeakwithDead,
			),
		4: (
			ArcaneEye,
			),
		5: (
			LegendLore,
			),
		},
	facets=(
		Facet(
			name="the Record",
			creed="what is not written did not happen, and the powerful know it, which is why they burn things",
			goal="restore a record that somebody spent a fortune erasing",
			),
		Facet(
			name="the True Name",
			creed="to name a thing correctly is to have a hand on it",
			goal="recover a name that was struck from every list",
			),
		Facet(
			name="the Sealed Page",
			creed="some sentences should exist and never be read, so someone must keep them unread",
			goal="ensure a particular text is never spoken aloud again",
			),
		Facet(
			name="the Last Speaker",
			creed="a language dies when the second-to-last speaker does, and we are always the last",
			goal="learn a tongue from someone who is the only one left who has it",
			),
		),
	perks=(
		"archives, registries, and temple libraries open to a hand that writes the old forms correctly",
		"you can tell a forgery from an original, and produce either",
		"scholars extend a courtesy that has nothing to do with liking you",
		"a letter in your hand reaches people who refuse every other letter",
		),
	sacrifices=(
		"a copy of everything you write goes to them, including this",
		"you may not destroy a document, however much it deserves it",
		"you are trusted with a passage you are forbidden to read",
		"you write under their name, never your own",
		),
	descriptors=(
		"Silent",
		"Sealed",
		"Ninth",
		"Burnt",
		"Unspoken",
		"Patient",
		),
	cores=(
		"Quill",
		"Page",
		"Word",
		"Ledger",
		"Seal",
		"Index",
		),
	relics=(
		"a page torn from something the order still owns",
		"an alphabet nobody else can read, taught in one sitting",
		"a sealed envelope to be opened on the day you die",
		),
	)


THE_STORM = Domain(
	name="the Storm",
	mark="Storm",
	checks=(
		"Nature",
		"Athletics",
		),
	cantrip=Light,
	prepared=FogCloud,
	spells_of_the_order={
		1: (
			Alarm,
			),
		2: (
			GustofWind,
			),
		3: (
			CallLightning,
			SleetStorm,
			WindWall,
			ThunderStep,
			),
		4: (
			LightningBolt,
			),
		5: (
			Scrying,
			),
		},
	facets=(
		Facet(
			name="the Breaker",
			creed="what the storm takes was already weak, and pretending otherwise kills people",
			goal="bring something down that has stood too long on rotten footings",
			),
		Facet(
			name="the Weather Eye",
			creed="the sky tells you everything an hour early, if you have paid attention for years",
			goal="warn a coast that has been told and does not believe it",
			),
		Facet(
			name="the Wrath",
			creed="some things deserve to be struck, and the sky is not always available",
			goal="deliver a judgment that no court in the country will issue",
			),
		Facet(
			name="the Calm After",
			creed="anyone can call the storm; the order exists for the morning afterward",
			goal="rebuild a place the order's own weather ruined",
			),
		),
	perks=(
		"sailors, herders, and roofers take your warnings seriously and pay for them",
		"you know an hour ahead of anyone what the sky intends",
		"you can be out in weather that keeps armies indoors",
		"a storm-house on any coast will take you in and ask about the wind, not your business",
		),
	sacrifices=(
		"you go out when it is worst, and you go first",
		"you may not sell a warning to only one side",
		"what the order calls down, you help clean up",
		"you are not permitted to fear it, at least not aloud",
		),
	descriptors=(
		"Rising",
		"Grey",
		"Unbroken",
		"Ninth",
		"Salt",
		"Waiting",
		),
	cores=(
		"Storm",
		"Gale",
		"Thunder",
		"Squall",
		"Tide",
		"Rain",
		),
	relics=(
		"a bell rung only before the worst of it",
		"a length of rope from a ship that came back without its crew",
		"a weather-glass that has been wrong exactly once",
		),
	)


THE_SHIELD = Domain(
	name="the Shield",
	mark="Sentinel",
	checks=(
		"Athletics",
		"Perception",
		),
	cantrip=Light,
	prepared=Heroism,
	spells_of_the_order={
		1: (
			Alarm,
			),
		2: (
			WardingBond,
			Aid,
			),
		3: (
			GlyphWarding,
			),
		4: (
			Divination,
			),
		5: (
			Creation,
			),
		},
	facets=(
		Facet(
			name="the Body Between",
			creed="the work is standing where the blow was going to land, and there is no cleverer version of it",
			goal="keep one person alive through a season in which everyone has agreed they will not be",
			),
		Facet(
			name="the Last Rank",
			creed="a line holds because nobody in it decided separately to run",
			goal="hold a place that has already been written off by everyone who could reinforce it",
			),
		Facet(
			name="the Oathkeeper",
			creed="a guard who can be bought was never a guard, only a delay with a uniform",
			goal="find out which of the order's own has been sold, and to whom",
			),
		Facet(
			name="the Sheathed",
			creed="the best guard is the one whose charge never learns how close it came",
			goal="prevent something quietly enough that nobody ever knows it was prevented",
			),
		),
	perks=(
		"soldiers, watchmen, and bodyguards recognize the stance and treat you as a professional peer",
		"you can read a room for the one person in it who is armed and hoping not to show it",
		"employers pay well and in advance for a guard whose order can be complained to",
		"where the order has stood before, doors are opened and questions are postponed",
		),
	sacrifices=(
		"a charge accepted is a charge kept, including after you learn what they are",
		"you go in front, always, and the order will hear about it if you did not",
		"you may not raise a hand first, whatever the provocation",
		"if you fail, you report it yourself, in person, and you are not shielded",
		),
	descriptors=(
		"Standing",
		"Unbroken",
		"Sworn",
		"Iron",
		"Last",
		"Silent",
		),
	cores=(
		"Shield",
		"Rank",
		"Watch",
		"Bulwark",
		"Guard",
		"Wall",
		),
	relics=(
		"a shield with eleven names scratched inside the boss",
		"a roster of everyone the order failed to protect, read aloud once a year",
		"a helm that is never worn and always carried",
		),
	)


THE_WALL = Domain(
	name="the Wall",
	mark="Warding",
	checks=(
		"Investigation",
		"Thieves' Tools",
		),
	cantrip=Prestidigitation,
	prepared=Alarm,
	spells_of_the_order={
		1: (
			Identify,
			),
		2: (
			ArcaneLock,
			Knock,
			),
		3: (
			GlyphWarding,
			Nondetection,
			),
		4: (
			ArcaneEye,
			),
		5: (
			Scrying,
			),
		},
	facets=(
		Facet(
			name="the Boundary",
			creed="a line drawn and honored is the whole of civilization; everything else is decoration",
			goal="restore a border that somebody has been quietly moving",
			),
		Facet(
			name="the Vault",
			creed="some things are safest when nobody can reach them, including us",
			goal="secure a thing so thoroughly that even the order forgets the way in",
			),
		Facet(
			name="the Locksmith",
			creed="you cannot build a door worth trusting until you have opened every kind there is",
			goal="get into the one place the order has never managed to enter",
			),
		Facet(
			name="What Is Kept Out",
			creed="the wall was not built to keep people in, and the records of why are incomplete",
			goal="learn what the founders were walling out, before the wall fails",
			),
		),
	perks=(
		"bankers, archivists, and jailers take your assessment of a lock as a professional verdict",
		"you can tell whether a room has been entered, and roughly by whom",
		"the order maintains a strongbox in most cities and one of the keys is yours",
		"a seal in your hand is honored by people who have never met you",
		),
	sacrifices=(
		"what you are given to keep, you keep, and you do not read it",
		"every way in that you discover is reported, including the ones you would rather keep",
		"you may not open a thing the order has sealed, whatever is happening on the other side",
		"one door in your life is not yours to open, and you know which",
		),
	descriptors=(
		"Sealed",
		"Ninth",
		"Silent",
		"Unbroken",
		"Old",
		"Patient",
		),
	cores=(
		"Wall",
		"Vault",
		"Seal",
		"Bound",
		"Lock",
		"Gate",
		),
	relics=(
		"a key ring on which one key has no known door",
		"a ledger of every seal the order has ever broken, with reasons",
		"a stone from the original wall, kept in a box",
		),
	)


THE_EYE = Domain(
	name="the Eye",
	mark="Detection",
	checks=(
		"Insight",
		"Perception",
		),
	cantrip=Guidance,
	prepared=DetectMagic,
	spells_of_the_order={
		1: (
			Alarm,
			),
		2: (
			DetectThoughts,
			SeeInvisibility,
			FindTraps,
			),
		3: (
			Clairvoyance,
			Nondetection,
			),
		4: (
			ArcaneEye,
			Divination,
			),
		5: (
			Scrying,
			),
		},
	facets=(
		Facet(
			name="the Open Eye",
			creed="most disasters were visible for weeks and simply not looked at",
			goal="be believed about something you can see coming and cannot prove",
			),
		Facet(
			name="the Sifter",
			creed="the lie is never in what is said; it is in the shape of what is left out",
			goal="expose an omission that a very careful person has maintained for years",
			),
		Facet(
			name="the Cost of Seeing",
			creed="an eye is traded for the sight, in one story or another, and the stories agree",
			goal="learn one thing that cannot be unlearned, knowing the price in advance",
			),
		Facet(
			name="the Unwatched",
			creed="whoever is doing the watching should also be watched, and that is our office",
			goal="audit a power that has never once been audited",
			),
		),
	perks=(
		"you notice the second exit, the wrong accent, and the coin that changed hands",
		"the order keeps files, and will open one for you if your reason is good",
		"magistrates and merchant houses buy a trained eye and do not advertise the purchase",
		"you can tell when you are being lied to, though not always what the truth is",
		),
	sacrifices=(
		"what you see is filed, whether or not it should be",
		"you do not act on what you observe until the order says the word",
		"you are watched in turn, thoroughly, and you agreed to it",
		"you may not warn anyone outside the order, however much they deserve warning",
		),
	descriptors=(
		"Open",
		"Sixth",
		"Sleepless",
		"Grey",
		"Patient",
		"Unblinking",
		),
	cores=(
		"Eye",
		"Watch",
		"Glass",
		"Witness",
		"Lens",
		"Vigil",
		),
	relics=(
		"a lens ground for an eye nobody in the order still has",
		"a file with your own name on it, which you have not been permitted to read",
		"a list of questions the founders never answered",
		),
	)


THE_BEAST = Domain(
	name="the Beast",
	mark="Handling",
	checks=(
		"Animal Handling",
		"Nature",
		),
	cantrip=Druidcraft,
	prepared=SpeakwithAnimals,
	spells_of_the_order={
		1: (
			Longstrider,
			),
		2: (
			AnimalMessenger,
			BeastSense,
			Barkskin,
			),
		3: (
			ConjureAnimals,
			),
		4: (
			LocateCreature,
			),
		5: (
			Scrying,
			),
		},
	facets=(
		Facet(
			name="the Kinship",
			creed="they are not lesser, they are earlier, and they were here when the terms were set",
			goal="honor an agreement made with something that does not speak and has not forgotten",
			),
		Facet(
			name="the Yoke",
			creed="every civilization stands on a partnership with something that could have refused",
			goal="restore a working bond between a people and a creature that has broken down",
			),
		Facet(
			name="the Wild Left In",
			creed="what we tamed we did not tame entirely, and the remainder deserves respect",
			goal="release something the order should never have kept",
			),
		Facet(
			name="the Shepherd",
			creed="the flock does not consent, so the burden of choosing well is entirely ours",
			goal="move a living thing across a country that intends to stop it",
			),
		),
	perks=(
		"beasts settle around you, which country people notice before they notice anything else about you",
		"herders, stablemasters, and beast-handlers trade you news along with the work",
		"you can tell what a place's animals are afraid of, which is usually worth knowing",
		"the order's kennels, stables, and mews will remount you without a written order",
		),
	sacrifices=(
		"a creature the order has claimed is not yours to free, however it looks at you",
		"you eat what you have hunted or raised, and you do the killing yourself",
		"the bond goes both ways, and it can be called upon by the other party",
		"you may not keep a companion the order has not approved",
		),
	descriptors=(
		"Wild",
		"Old",
		"Patient",
		"Unbroken",
		"First",
		"Grey",
		),
	cores=(
		"Beast",
		"Herd",
		"Kinship",
		"Hound",
		"Mane",
		"Flock",
		),
	relics=(
		"a collar with no buckle, sized for nothing that walks",
		"a stable book listing beasts that have not existed for six generations",
		"a whistle that no person present can hear",
		),
	)


DOMAINS = (
	THE_FORGE,
	HOME,
	THE_HUNT,
	MERCY,
	THE_VEIL,
	THE_ROAD,
	THE_WORD,
	THE_STORM,
	THE_SHIELD,
	THE_WALL,
	THE_EYE,
	THE_BEAST,
	)


__all__ = (
	"DOMAINS",
	"HOME",
	"MERCY",
	"THE_BEAST",
	"THE_EYE",
	"THE_FORGE",
	"THE_HUNT",
	"THE_ROAD",
	"THE_SHIELD",
	"THE_STORM",
	"THE_VEIL",
	"THE_WALL",
	"THE_WORD",
	)
