import random
from collections import defaultdict

def Genus(lusor):
	"""
	Returns a descriptive genus string for a lusor (NPC or PC).

	- If lusor is already a string, return it.
	- If it has a `.genus` property, use that.
	- Else, build it manually from attributes.
	"""
	# Case 1: already a string
	if isinstance(lusor, str):
		return lusor

	# Case 2: has a genus property
	if hasattr(lusor, "genus"):
		try:
			return lusor.genus
		except Exception as e:
			pass  # fallback to manual if it fails

	# Case 3: build manually (best-effort fallback)
	archetype = getattr(lusor, "archetype", None) or getattr(lusor, "char_class", "")
	attributes = [
		str(getattr(lusor, "race", "") or ""),
		str(getattr(lusor, "subrace", "") or ""),
		str(archetype),
		str(getattr(lusor, "gender", "") or ""),
		str(getattr(lusor, "alignment", "") or ""),
	]
	return " , ".join(filter(None, attributes))

def custom_title(s):
	"""
	Converts a string to title case while handling apostrophes correctly.
	"""
	return " ".join([word[0].upper() + word[1:] if word else "" for word in s.split()])

def generate_title(descriptor, rank, origin):
	"""
	Generates a title from the given lists,
	avoiding double spaces and handling title casing.
	"""
	random.seed(lusor.seed)

	parts = [Descriptor(lusor),random.choice(rank), random.choice(origin)]
	title = " ".join(filter(None, parts))  # Removes empty strings
	return "The " + custom_title(title)

def Title(lusor):

	descriptor = Descriptor(lusor)
	rank = Rank(lusor)
	origin = Origin(lusor)

	# Define your patterns
	patterns = [
		f"The {descriptor} {rank}",
		f"The {rank} {origin}",
		f"The {rank}",
		f"The {descriptor} {rank} {origin}",
	]

	# Define weights for each pattern
	weights = [20, 15, 4, 1]  # Adjust weights to match your desired frequency

	# Select a title based on the weights
	title = random.choices(patterns, weights=weights, k=1)[0]
	return title.title()

def Descriptor(lusor):
	'''
	General Rule:
	If you can say
	 - The X Lord -
	 And sounds cool
	 X goes here
	'''
	random.seed(lusor.seed)
	genus =  lusor

	descriptor = []

	# General Descriptors
	try:
			# A
		descriptor += [
			"Aquatic",			"Ancient",			"Accursed",			"Abyssal",			"Astral",			"Ancient",			"Accursed",			"Amethyst",			"Atmospheric",		"Astronomical",		"Aquatic",			"Amulet",			"Art", 				"Artistic",			"Astral",			"Alien",			"Alpha",			"Autumn",			"Animal",			"Atmospheric",		"Archaic",			"Antique",			"Ancient",			"Arcane",			"Amulet",			"Aurora",			"Alchemic",			"Amethyst",			"Alabaster",		"Alien",			"Azure",			"Amulet",			"Arboreal",			"Atmospheric",		"Airy",				"Aerial",			"Astute",			"Analytical",		"Artistic",			"Arcane",			"Antagonistic",		"Aggressive", 		"Acrimonious",		"Abominable",		"Ardent",			"Angelic", 			"Amulet",			"Apathetic",		"Antagonistic",		"Annoyed",			"Angry",			"Acrimonious",		"Abhorrent",		"Ardent",			"Amorous",			"Affection",		"Adoring",			"Aristocratic",		"Astronomical",		"Antique",			"Antediluvian",		"Ancient",			"Ancestral",		"Ageless",			"Astral",			"Artifact",			"Amulet",			"Archaic",			"Affectionate",		"Aristocratic",		"Archaic",			"Antique",			"Apostolic",		"Astral", 			"Antediluvian",		"Ancient",			"Ancestral",		"Atemporal",		"Ancient",			"Ancestral",		"Anachronistic",	"Ageless",			"Ancient",			"Amulet",			"Abhorrent",		"Abyssal",			"Angelic",			"Angry",			"Ageless",			"Arcane",			"Antediluvian",		"Archipelago",		"Alluring",			"Archipelago",		"Adorned",			"Arctic",			"Artistic",			"Ascetic",			"Ardent",			"Arena",			"Aristocratic",		"Arrogant",			"Artifact",			"Asgardian",		"Astral",			"Astute",			"Atlantean",		"Aurora",			"Autumn",			"Awakened",			"Aztec",			"Azure",			"Abominable",		"Amazonian",		"Amethyst",			"Amulet",			"Ardent",			"Ancestral",		"Ancient",			"Antique",			"Arcane",			"Apostolic",		"Aquatic",			"Arachnid",			"Arboreal",			"Arcane",			"Arcanic",			"Arch",				"Archaic",			"Abyssal",			"Aerial",			"Ageless",			"Alabaster",		"Alchemical",		"Alcoholic",		"Alpha",			"Amber",			"Amber",			"Augury",			"Amber",			"Ancient",			"Ancient",			"Ancient",			"Ancient",			"Ancient",			"Aberrant",			"Ancient",			"Amber",			"Ancient",			"Apex",				"Age-old",				"Alpha",			"Air",				"Air",				"All-Seeing",		"Air",				"Armored",			"Aura",				"Aura",				"Alcoholic",		"Astral",			"Astral",			"Archfey",			"Awakened",			"Autumn",			"Angry",			"Arcane",			"Antique",			"Ageless",			"Armored",			"Armored",			"Armorless",		"All Seeing",
				]
			# B
		descriptor += [
			"Blizzard",			"Book",			"Brass",		"Bronze",		"Binding",		"Beauty",		"Boreal",		"Bloodmoon",	"Blizzard",		"Black Hole",	"Baroque",		"Blade",		"Battle",		"Blight",		"Bone",			"Black",		"Babylonian",			"Badland",			"Baleful",			"Blade",			"Black",			"Baronial",			"Baroque",			"Barracks",			"Barren",			"Bat",			"Battle",					"Battleground",		"Bay",			"Beach",		"Beachy",		"Bearded",		"Behemoth",		"Beige",		"Benevolent",	"Beryl",		"Bewitched",	"Biblical",		"Bipedal",		"Bitter",			"Bramble",			"Brass",			"Brave",			"Breezy",			"Bridge",			"Brimstone",			"Bronce",			"Bronze",			"Brooch",			"Brook",			"Brown",			"Brush",			"Burgundy",			"Black",			"Bog",			"Bone",			"Book",			"Booming",		"Boreal",		"Brain",		"Blazing",		"Burned",		"Burning",		"Bursting",		"Butterfly",			"Bygone",			"Byzantine",			"Blind",			"Blizzard",			"Blood",			"Bloodmoon",			"Blooming",			"Blossoming",			"Blue",					"Battle",		"Basalt",		"Broken",		"Blood",		"Battle",		"Battle",			"Battle",		"Battle",		"Brave",		"Brave",		"Bow",			"Bold",			"Bloodthirst",	"Boreal",		"Boreal",		"Blue",			"Blue",			"Black",		"Black",		"Blood",		"Blood",		"Blood",		"Blooming",		"Brass",		"Band",		"Bursting",		"Blending",		"Bat",		"Black",				"Blind",				"Bursting",				"Bone",				"Bronce",			"Brown",			"Brain",		"Book",			"Butterfly",	"Burning",		"Blade",		"Boundless",	"Boundless",	"Brimstone",	"Burning",		"Blood",		"Beautiful",
				]
			# C
		descriptor += [
			"Cranium",			"Celestial",		"Colossal",			"Crafty",			"Codex",			"Colossal",			"Complex",			"Creativity",		"Cosmic",			"Cosmos", 			"Cosmic",			"Cometary",		"Climatic",			"Cloud",			"Chimeric",			"Compassion",			"Celestial",			"Cold",			"Chivalrous",			"Chaotic",			"Charcoal",			"Charming",			"Charter",			"Chasm",			"Compass",			"Compassionate",	"Concealed",		"Confusion",		"Constellation",	"Contempt",			"Copper",			"Coral",			"Corpse",			"Cosmic",		"Cosmos",			"Coverted",			"Crab",			"Crater",			"Crescent",			"Crest",			"Crested",			"Crimson",			"Crossed",			"Crown",						"Cruel",			"Crypt",			"Cryptic",			"Crystal",			"Crystalline",		"Cunning",			"Curse",			"Cursed",			"Cyan",				"Cyclic",			"Cyclonic",			"Cyclopean",		"Cyclops",		"Cynical",			"Chronal",			"Chronic",			"Cipher",			"Circus",			"Citadel",			"City",			"Clairvoyant",			"Clandestine",			"Classical",			"Comet",			"Cleric",			"Clerical",			"Clever",			"Cliff",			"Climatic",			"Cloaked",			"Cloaked",			"Clockwork",		"Cloud",			"Coast",			"Cobalt",			"Cobweb",			"Code",			"Cold",				"Colonial",			"Colossal",			"Combat",			"Candle",			"Canyon",			"Cardinal",			"Castle",			"Cat",			"Catacomb",			"Cathedral",			"Cave",			"Cavern",			"Celestial",			"Celtic",			"Cerebral",			"Cerulean",			"Cerulian",			"Chain",			"Chained",			"Chalice",			"Champion",			"Corrupt",			"Chief",		"Crowned",			"Camouflage",		"Cursed",			"Charmbreaker",			"Chaos",			"Cerberus",			"Clockwork",			"Clokwork",			"Charming",			"Craft",			"Chained",			"Chain",			"Chaos",			"Crystal",			"Cosmic",			"Cosmic",			"Cat",				"Chain",			"Chief",			"Chief",			"Chief",			"Circus",			"City",				"Coral",			"Copper",		"Cursed",			"Crab",				"Crimson",			"Crown",			"Cold",			"Colossal",			"Cooper",
			]
			# D
		descriptor += [
			"Dread",			"Darkin",			"Dimensional",		"Dagger",			"Deep Sea",			"Dungeon",			"Divine",			"Dream",			"Disciple",			"Dusk",			"Disgust",			"Dauntless",			"Dawn",			"Deadly",			"Death",			"Deep",			"Deity",			"Delightful",			"Delta",			"Desert",			"Desolated",			"Desperate",			"Detached",			"Detestable",			"Devoted",			"Doom",				"Dormant",			"Draconian",		"Draconic",			"Dragon",			"Dragonfire",			"Drained",			"Dream",			"Dune",			"Dungeon",			"Dusk",			"Dusky",			"Dust",			"Dynastic",			"Day",			"Divine",			"Dock",			"Devotional",			"Daemonic",			"Dagger",			"Dungeon",			"Dark",			"Darkness",			"Darkstar",			"Devout",			"Dew",				"Diabolical",		"Diadem",			"Dimension",		"Dimensional",		"Dire",			"Damnation",			"Drifting",			"District",			"Diavolical",			"Doom",			"Death","Death",			"Darkness",			"Dark",			"Dark",			"Dark",			"Dark"			"Dawning",			"Death",			"Dominating",			"Deadly",						"Dragon",			"Deadly",			"Dawning",			"Deep",				"Divine",			"Dream",			"Dust",				"Demon",			"Deadly",			"Desolate",			 "Deathless",
			]
			# E
		descriptor += [
			"Elder",			"Existence",		"Ethereal",			"Eclipse",			"Everlasting",		"Eternal",		"Eldritch",		"Elder",		"Elder",			"Epochal",			"Endless",			"Ether",			"Enemy",			"Empty",			"Everlasting",			"Exalted",			"Exhausted",			"Existence",			"Exotic",			"Expedition",			"Extraterrestrial",			"Exuberant",			"Everlasting",			"Egotistic",		"Eclipsed",			"Ecliptic",			"Ecstatic",			"Ectoplasmic",		"Edgy",			"Edict",		"Edo",			"Educated",			"Erudite",			"Esoteric",			"Eternal",			"Ethereal",			"Euphoric",			"Evanescent",			"Evangelical",		"Elder",			"Eldritch",			"Electric",			"Elegant",			"Elemental",			"Elixir",						"Elizabethan",			"Eloquent",			"Elusive",			"Elven",			"Elysian",			"Elysium",			"Ember",			"Emblem",		"Emerald",		"Eminent",		"Empathetic",		"Enchanted",		"Enchanting",		"Energetic",		"Energy",			"Engine",			"Enigma",			"Enraged",			"Envious",			"Ephemeral",			"Epochal",			"Equinox",			"Errant",			"Erratic",			"Echo",			"Eagle",			"Earth",			"Ebony",			"Ecclesiastical",	"Eclipse",			"Emissary",			"Elemental",	"Exalted",		"Electric",		"Ever",				"Earth",			"Earth",			"Errant",			"Energy",			"Engine",			"Equinox",			"Enchanted",			"Earthy",			"Enchanted",			"Evasive",			"Eagle",			"Equinox",			"Energy",			"Emmerald",			"Enchanted",			"Engine",			"Earth",			"Errant",			"Enchanted",		"Enchanteing",		"Endless",		"Earth",		"Eternal",		"Ethereal",
			]
			# F
		descriptor += [
			"Ferocious",		"Force",			"Forest",			"Forgotten",			"Flowing",			"Fluid",				"Frostfire",		"Frostbite",		"Flight",			"Fire",				"Frost",			"Fen",			"Fenrir",			"Fable",			"Fabled",			"Fae",			"Fairground",			"Faithful",			"Falcon",			"Falcon",			"Fallen",			"Fanciful",			"Fanged",			"Far",			"Farm",				"Fast",				"Fathom",			"Fearful",				"Feathered",			"Feral",			"Ferocious",			"Fluid",			"Fervent",			"Feudal",						"Fierce",			"Fiery",			"Finned",			"Folk",			"Fond",			"Fool",			"Forceful",			"Foreboding",			"Forest",			"Forested",			"Forge",			"Formidable",			"Fortress",			"Fountain",			"Frost",			"Frostbound",		"Frostbite",			"Frostfire",			"Frosty",			"Frozen",				"Frustrated",			"Fuchsia",			"Fullmetal",		"Fullmoon",			"Furious",			"Furred",			"Fury",			"Futuristic",			"Ferocious",			"Feral",			"Fire",			"Firebrand",			"Firebreathing",			"First",			"Fjord",			"Flag",			"Flame",			"Flameheart",		"Flamehearted",		"Flametongue",			"Flaming",			"Fleshwork",		"Floral",				"Flourish",				"Flowing",			"Fluid",			"Flying",			"Fugitive",			"Fire",			"Fleshwork",			"Force",			"Flameborn",			"Flesh",			"Flying",			"Forest",			"Flame","Flame",			"Fullmetal",			"Fleshwork",			"First",			"Forest",			"Forest",			"Fury",					"Freedom",			"Ferocious",			"Fierce",			"Free",				"Freedom",				"Fairy",				"Fallen",			"Fate",				"Fateful",			"Feathered",		"Fiery",			"Fire",			"Fey",			"Feywild",			"Firbolg",			"Fire",			"Flame",			"Frost",			"False",			"Forge",
			]
			# G
		descriptor += [
			"Grim",				"Giant",			"Green",			"Gold",				"Gentle",			"Great",			"Glowing",			"Gleaming",			"Gloomy",			"Grieving",			"Grateful",			"Graphite",			"Granite",			"Grail"				"Green"				"Golden",			"Glowing",			"Grail",			"Gavel",			"Gaseous",			"Gas",				"Gases",			"Gaseous",			"Garden",			"Gravitational"		"Galactian",		"Galactic",			"Glacier",			"Gothic"			"Glacial",			"Grail",			"Goblet",			"Glowing",			"Great",			"Grand",			"Golden",			"Gregorian",		"Galactian",		"Galactic",			"Galaxy",			"Gallant",			"Garden",			"Gargantuan",		"Gargoyle",			"Gas",				"Gaseous",			"Gauntlet",			"Gavel",			"Gemmed",			"Gentle",			"Geyser",			"Ghost",			"Ghostly",			"Gleaming",			"Gloom",			"Glorious",			"Glowing",			"Glyph",			"Goblet",			"Gold",				"Golden",			"Goldenhearted",	"Goldenrod",		"Golem",			"Gorge",			"Gorgonian",		"Gothic",			"Graceful",			"Grail",			"Grand",			"Granite",			"Graphite",			"Grassland",		"Grassy",			"Grateful",			"Grave",			"Graveyard",		"Gravitational",	"Great",			"Greathearted",		"Green",			"Gulf",				"Grieving",			"Grim",				"Grimoire",			"Grove",			"Gryphon",			"Grim",				"Glorious",			"Giant",			"Gilded",			"Glacial",			"Glacier",			"Glade",			"Great",			"Green",			"Green",			"Green",			"Graceful",			"Giant",			"Gas",				"Golden",			"Golden",			"Golden",			"Green",			"Great",			"Gentle",			"Galactic",			"Guarded",			"Grizzly",			"Godless",
			]
			# H
		descriptor += [
			"Hollow",		"Hesperidean",		"Heliospheric",		"Historic",			"Heroic",			"Hell",				"Hermetic",				"Heart",		"Harmonious",		"Heartbroken",		"Happy",			"Hourly",			"Heartbroken",		"Hourly",			"Heartbroken",		"Hunting",			"Homeric",			"Horned",			"High",				"Helian",			"Haunting",			"Harpist",			"Harlequin",		"Hidden",			"Hoary", 	"High",			"Holy",				"Hamlet",			"Hammer",			"Han",				"Happy",			"Harbinger",			"Harbor",		"Harlequin",		"Harmony",			"Harpist",			"Harsh",			"Hateful",			"Haunting",			"Heart",			"Heartbroken",		"Heartfelt",		"Heath",			"Heavenly",			"Hedgerow",			"Helian",			"Heliospheric",		"Hell",		"Hellenistic",	"Hellish",		"Hermetic",		"Hermitage",		"Heroic",			"Hex",				"Hidden",			"Hieratic",			"High",					"Hill",			"Historic",			"Hive",				"Hoary",			"Hollow",			"Homeric",			"Honorable",		"Honored",			"Hopeful",			"Horizon",			"Horned",			"Horrified",		"Horus",			"Hostile",			"Hourglass",		"Hourly",	"Hungry",		"Hunter",		"Hunting",		"Hydra",			"Hyperion",			"Hypnotic",			"Heretic",			"Howling",			"Hourglass",			"Hungry",		"Hunger",			"Hell",				"Hill",				"High",				"Hive",				"Hound",			"Hourglass",		"Harmonic",
			]
			# I
		descriptor += [
			"Immortal",			"Icy",				"Inferno",				"Instantaneous",		"Intrepid",				"Inquisitive",			"Intellect",		"Intellectual",			"Inkwork",				"Inkwell",				"Ink",				"Invincible",		"Impenetrable",		"Immortal",			"Icarian",			"Icicle",		"Ice",			"Icy",			"Immemorial",	"Infinite",			"Immortal",		"Indomitable",		"Ink",			"Ice",			"Ion",				"Ionic",			"Ionized",				"Irate",				"Iridescent",			"Iron",					"Irritable",			"Irritated",		"Island",				"Islet",				"Isolated",				"Ivory",			"Icarian",			"Ice",				"Iceborn",			"Icicle",			"Icon",				"Icy",			"Idol",			"Illusion",		"Illusionist",	"Imagination",		"Imam",			"Immemorial",		"Immortal",			"Impassioned",			"Impenetrable",			"Imperial",			"Imperious",			"Imperishable",			"Impish",				"Impulse",			"Incan",				"Incantation",			"Indifferent",			"Indignant",		"Indigo",			"Infernal",			"Inferno",			"Infinite",			"Infinity",			"Inimical",		"Ink",			"Inkwell",		"Inkwork",					"Innovative",		"Inquisitive",		"Inscrutable",			"Insidious",			"Inspired",			"Inspiring",			"Instantaneous",		"Intellect",			"Intellectual",			"Intense",			"Interested",			"Interim",				"Interstellar",			"Intimate",			"Intrepid",			"Intrigued",		"Intriguing",		"Invincible",		"Iron",				"Iron",			"Ice",			"Icicle",		"Ink",			"Ignoble",			"Infernal",			"Insatiable",
			]
			# J
		descriptor += [
			"Jasmine",		"Jaguar",		"Jackal",		"Jackal", 		"Jaguar", 		"Jasmine", 	"Jay", 		"Jester", "Journey", "Judge", "Juggernaut", "Jungle",
			"Juniper",		"Jungle",		"Just",		"Just",		"Judgmental",	"Judgmental",	"Judicial", 	"Just",	"Justice",	"Judicial",	"Just",	"Jurassic",	"Jungle",	"Jester",	"Joyful",	"Jade",	"Jotunn",	"Judicial",			"Journey",			"Jewel",			"Jungle",			"Jungle",			"Jade",			"Jealous",			"Jewel",			"Jewelcraft",			"Jeweled",			"Jotunn",			"Jovial",			"Joyful",			"Joyous",		"Jubilant",		"Jungle",		"Just",
			]
			# K
		descriptor += [
			"Knowledge",	"Keep",		"Krakenesque",				"Knife",				"Kaleidoscopic",				"Keen",				"Key",				"Kind",												"Kingly",							"Knightly",							"Kerberus",				"Key",
			]
			# L
		descriptor += [
			"Lost",				"Lonely",			"Liquid",			"Luminous",			"Last",				"Labyrinthine",		"Labyrinth",			"Labyrinth",		"Large",			"Legendary",		"Legal",			"Loving"			"Luminous",			"Lunar",		"Lupine",			"Lordly",			"Laboratory",			"Labyrinth",						"Labyrinthine",			"Lagoon",			"Lake",			"Lantern",			"Last",			"Lauded",			"Lavender",			"Law",				"Liquid",			"Leafy",			"Luminous",			"Learned",			"Leechy",			"Legendary",			"Legislation",		"Lethal",			"Leviathan",		"Leather",			"Libra",			"Library",			"Lich",			"Life",			"Light",			"Lightbringer",			"Lightning",			"Lion Heart",			"Lionheart",			"Liquid",			"Literary",			"Lively",			"Living",			"Lizard",			"Loathsome",		"Lone",				"Lonely",			"Long",				"Longstanding",			"Loom",				"Looming",			"Lost",			"Loving",			"Loyal",			"Luminous",			"Lush",				"Lustrous",		"Luxuriant",			"Luxurious",			"Lycan",			"Lyre",			"Lyrist",			"Lead",			"Lonely",			"Loyal",			"Lingering",			"Lore",				"Lost",				"Lost",				"Life",			"Luminous",			"Life",				"Lightning",		"Lizard",				"Lonely",			"Long",				"Leader",			"Lunar",			"Light",			"Labyrinth",		"Labyrinthine",		"Lava",
			]
			# M
		descriptor += [
			"Moonlight",	"Mischievous",	"Mirthful",		"Melancholic",	"Momentary",	"Mythical",		"Moonlit",		"Moon",			"Mortal",		"Memory",		"Majestic",		"Majestic",		"Mystic",			"Mad",			"Misty",			"Mighty",			"Molten",			"Momentary",			"Monastery",			"Monastic",			"Masterful",			"Monolith",		"Monolithic",			"Monstrous",			"Moon",			"Moonlit",			"Moonshade",	"Moonshadow",	"Moor",			"Moorish",		"Moss",			"Motivated",	"Mountain",		"Mountainous",	"Mournful",		"Muddy",		"Mulberry",		"Museum",		"Mustard",			"Mutant",			"Mysterious",			"Mystery",			"Mystic",			"Mystical",			"Mystique",			"Mythic",			"Mythical",			"Mythological",			"Maelstrom",						"Magic",			"Magma",			"Magnetic",		"Mahogany",		"Majestic",		"Maleficent",	"Malevolent",	"Malicious",	"Malign",		"Mammoth",		"Mandrake",		"Maned",		"Mangrove",		"Manticore",	"Manticorian",		"Mantle",			"Marble",			"Marine",			"Maroon",			"Marsh",			"Marshy",			"Martial",			"Martian",			"Marvelous",			"Masked",			"Masterful",			"Mausoleum",			"Mauve",			"Maverick",		"Maze",			"Meadow",		"Mecha",		"Medallion",	"Medieval",		"Meditative",	"Medusian",		"Melancholic",	"Melancholy",	"Meld",			"Melodic",		"Memento",			"Menacing",			"Menagerie",			"Mental",			"Merciless",			"Mercurial",			"Meridian",			"Merlinian",			"Master",			"Marine",		"Mermaid",		"Merry",		"Mesopotamian",	"Messianic",	"Meteor",		"Meteoric",		"Meteoritic",	"Metropolis",	"Midnight",		"Mighty",		"Militant",		"Millennial",	"Mine",			"Ministerial",	"Minotaur",		"Minotaurine",	"Minstrel",		"Miraculous",		"Mirage",		"Mirror",		"Mirthful",		"Mischievous",		"Missionary",		"Mist",		"Mistral",				"Malachite",				"Mighty",				"Moon",			"Moonlit",		"Mysterious",	"Mystical",		"Moon",			"Mist",			"Mind",			"Mad",			"Mad",			"Magic",		"Magma",		"Marine",		"Mental",		"Mirror",		"Mist",			"Minotaur",		"Moon",			"Mutant",		"Meteor",		"Mythic",			"Mythic",				"Mighty",				"Monstrous",	"Monstrous",	"Mystical",
				]
			# N
		descriptor += [
			"Nomad",			"Natural",		"Nautical",		"Notorious",	"Nomadic",		"Nocturnal",	"Noble",		"Nimble",		"Nefarious",	"Noble",		"Nasty",		"Nocturnal",	"Noble",		"Nimble",		"Nefarious",		"Nasty",		"Nebular",		"Notorious",	"Nomadic",	"Nocturnal",	"Nimble",	"Nefarious",	"Noble",	"Nordic",	"Nemean",		"Noble",		"Nordic",		"Nether",	"Neon",		"Nemesis",	"Night",		"Nocturnal", 		"Nova",			"Nebulous",		"Nervous",		"Nervous",		"Nature",		"Night",		"Night",		"Nightmare",	"Napoleonic",	"Nasty",		"Nautic",		"Nebula",		"Nebular",		"Nebulous",		"Nemean",		"Nemesis",	"Neon",		"Nervous",	"Nether",	"Northern",		"Neutron",	"New",		"Nexus",	"Night",		"Nightmare",	"Nimble",		"Nimbus",	"Nirvana",		"Nocturnal",	"Nomadic",		"Nordic",		"Norman",			"Notorious",	"Nova",			"Nun",			"Natural",		"Nature",		"Nocturnal",	"New",			"New",			"Nightmare",	"Night",		"Nocturnal",	"Nebula-born",
			]
			# O
		descriptor += [
			"Orchid",		"Ozone",		"Old",			"Old",				"Other",			"Old",						"Oasis",			"Oblivion",			"Observatory",			"Obsidian",			"Obsolete",			"Occult",			"Ocean",			"Oceanic",			"Ochre",						"Odious",			"Offensive",			"Old",			"Olive",			"Olympian",			"Omen",			"Ominous",			"Omniscient",			"Only",			"Onyx",			"Opal",			"Opalescent",					"Opposed",			"Oppressive",			"Optimistic",			"Opulent",						"Oracular",			"Orange",			"Orb",			"Orbit",			"Orbital",			"Orbiting",			"Orchard",			"Orchid",			"Orphean",			"Otherworldly",	 "Outlandish",			"Outpost",			"Outraged",			"Outrageous",	"Overgrown"		"Overgrown",	"Overlord",			"Owl",						"Ozone",		"Order",			"Oceanic",			"Orange",			"Old",			"Otherworld",
			]
			# P
		descriptor += [
			"Phantom",			"Prismatic",		"Prehistoric",		"Petrifying",		"Petrified",		"Perplexing", 		"Pensive",			"Power",			"Political",		"Polar",			"Primordial",		"Perpetual",		"Perennial",		"Purifying",		"Pure",				"Primeval",			"Plague",			"Pain",			"Palace",			"Pastoral",			"Pathfinder",			"Patriarch",			"Patriarchal",			"Pawed",			"Peaceful",			"Peach",			"Pearl",			"Pearlescent",		"Peat",				"Pebble",			"Peerless",			"Peeved",			"Pegasus",			"Pendant",			"Pensive",			"Perceptive",		"Peregrine",		"Perennial",		"Perilous",			"Pernicious",		"Perpetual",			"Perplexed",			"Petal",			"Petrified",			"Phalanx",			"Phantasm",			"Phantasmagorical",			"Phantasmal",		"Phantom",			"Pharaonic",		"Pharaonic",		"Philosophical",	"Phlegmatic",		"Phoenix",			"Phoenixian",		"Phylactery",		"Pietistic",		"Pillar",			"Pine",				"Pinnacle",			"Pioneering",		"Piqued",						"Placid",			"Plague",			"Planar",			"Planetary",			"Plasma",			"Plateau",			"Platinum",			"Pleasant",			"Pleased",			"Plucky",			"Plum",				"Poet",				"Poetic",			"Poignant",			"Poisonous",		"Polar",			"Pond",				"Ponderous",		"Pontifical",		"Poppy",			"Porcelain",		"Port",				"Portal",			"Potent",			"Potion",			"Powder",			"Power",			"Poker",			"Powerhouse",			"Prairie",			"Plague",		"Precious",		"Precocious",		"Predatory",		"Preternatural",	"Primal",			"Prime",			"Primeval",			"Primordial",		"Princely",			"Prismatic",		"Prison",			"Private",			"Profound",			"Prohibition",		"Promethean",		"Prophetic",		"Prosperous",		"Protected",		"Proud",		"Psion",		"Pugnacious",		"Pulsar",		"Pulsating",		"Pumpkin",		"Pungent",		"Punk",		"Pure",		"Purifying",		"Purist",			"Purple",			"Puzzled",			"Pyramid",			"Pyro",				"Palm",				"Pandemonium",		"Panicked",			"Papal",			"Paradox",			"Paradoxical",		"Parched",			"Parish",			"Park",				"Parliament",		"Passionate",		"Pack",				"Phantom",			"Primal",			"Pillager",			"Power",			"Powerful",			"Pain",			"Pack",				"Pain",			"Pure",				"Portal",			"Plague",			"Primal",			"Prehistoric",		"Primigenial",		"Primordial",		"Proud",			"Planar",
			]
			# Q
		descriptor += [
			"Quest",	"Quicksand",			"Quantum",			"Quartz",			"Quasar",			"Queen",						"Quest",			"Questing",			"Quick",			"Quicksand",			"Quicksilver",			"Quiet",			"Quill",	"Quicksilver",
			]
			# R
		descriptor += [
			"Relentless",	"Ritualistic",	"Rogue",		"Risen",		"Restless",		"Requiem",		"Relic",		"Rippling",			"Reality",		"Raging",		"Radiant",		"Rhythm",		"Rising",		"Raging",		"Ragnarok",		"Rain",		"Renegade",		"Rule",		"Runewielder",	"Rainbow",		"Rainforest",		"Rainstorm",		"Rampant",		"Rampart",		"Ranch",		"Rancorous",		"Rising",		"Rose",			"Restless",		"Red",		"Rosethorn",	"Raid",			"Red",			"Red",			"Rule",			"Rat",			"Rational",		"Ravaged",			"Ravaging",			"Radiant",		"Reality",		"Reckless",		"Reckoner",		"Reckoning",		"Reclusive",		"Red",		"Redoubtable",		"Redwood",		"Reef",		"Refined",		"Regal",		"Regulation",		"Relaxed",		"Relentless",		"Relic",		"Remnant",		"Remote",		"Renaissance",		"Renegade",		"Reptilian",	"Repugnant",	"Resentful",	"Resilient",	"Resolute",		"Resounding",	"Resplendent",		"Revered",		"Reverent",			"Rhapsodic",	"Radiant",		"Rhombus",		"Ribbon",		"Rich",			"Riddle",		"Ridge",		"Rift",		"Righteous",		"Rime",		"Rippling",		"River",				"Riverine",		"Roaming",		"Robotic",		"Rock",		"Rocky",		"Rod",		"Rogue",		"Roman",		"Rooted",		"Rosaline",		"Rose",			"Rosy",			"Royal",		"Ruby",			"Rugged",		"Ruined",		"Ruins",			"Rule",			"Rune",			"Runecarved",		"Runewielder",	"Runic",		"Rural",		"Rust",			"Rustic",		"Rusty",		"Ruthless",				"Rune",				"Rune",				"Red",				"Rainstorm",				"Red",				"River",				"Rogue",				"Rune",				"Riding",		"Roaring",
			]
			# S
		descriptor += [
			"Shadow",			"Silver",			"Star",				"Sparkling",		"Shining",			"Structures",		"Stellar",			"States",			"Supernova",			"Sunset",				"Sunny",			"Sun",				"Starry",			"Star",				"Space",			"Silvertongued",	"Sempiternal",		"Sorrel",			"Swan",				"Stormchaser",		"Stingray",			"Starship",				"Strength",				"Sunblessed",		"Sun",				"Shadow",			"Secret",			"Supreme",			"Strong",			"Supreme",			"Star",				"Sylvan",			"Shadow",				"Sacred",				"Subterranean",		"Solemn",			"Sad",				"Solar",			"Spirit",			"Shade",			"Stalker",			"Stargazer",		"Stellar",			"Sublime",			"Slaying",			"Saga",					"Sagacious",		"Saint",			"Smiling",			"Sanctuary",		"Sand",				"Sandy",			"Sanguine",			"Sanskrit",			"Sapphire",			"Satellite",			"Satisfied",			"Satyric",			"Savanna",			"Savannah",			"Savant",			"Savvy",			"Scaled",			"Scarab",			"Scarlet",			"Scenic",			"Scented",			"Scepter",						"Scholarly",			"School",			"Science",			"Scientific",		"Scintillating",	"Scion",			"Scorching",		"Scroll"			"Sea"				"Seal"					"Seashore"				"Seasonal"			"Secluded"			"Second"			"Secret"			"Secretive"			"Skeletal",			"Mercenary",		"Seductive",		"Seismic",			"Selenian",			"Sempiternal",		"Sensual",				"Sentimental",			"Seraphic",			"Serene",			"Serpentine",		"Seventh",			"Sewer",			"Seychelle",		"Shade",				"Shaded",				"Shadow",			"Shadowy",			"Shallow",			"Shamanic",			"Shark",			"Shattered",		"Shattering",		"Shield",			"Shielded",			"Shimmering",			"Shining",				"Shivering",		"Shore",			"Shrewd",			"Shrine",			"Sickly",			"Sienna",			"Sigil",			"Silent",			"Silver",			"Silvertongued",		"Simian",				"Singing",			"Sinister",			"Siren",			"Sirenian",			"Sirenic",			"Skeleton",			"Sky",				"Skyborn",			"Skyborn",			"Slate",			"Sleeping",			"Slimey",				"Sly",				"Smart",			"Soul",				"Soulbound",		"Soulfire",			"Soulful",			"Space",			"Spark",			"Sparkling",		"Spartan",				"Spectral",				"Spell",			"Spellbound",		"Spined",			"Spiral",			"Spire",			"Spiritual",		"Spiteful",			"Splendid",			"Spring",			"Sprouting",		"Stadium",				"Staff",			"Stalwart",			"Standard",			"Star",				"Star-born",				"Star-crossed",			"Star-crosser",		"Starborn",			"Starcrossed",		"Starcrosser",		"Starfall",			"Starlit",				"Starry",				"Stars",		"Starting",			"Statute",			"Steadfast",		"Stealthy",			"Steam",			"Steamy",			"Steelhearted",		"Stellar",			"Stern",			"Stinger",			"Stoic",			"Stone",			"Storm",			"Stormbringer",		"Stormcaller",		"Stormy",			"Strait",			"Strategist",		"Stratospheric",	"Stream",		"Strong",				"Sea",							"Stunning",		"Stygian",			"Sublime",			"Subterranean",		"Subtle",			"Sulfuric",			"Sullen",			"Summer",			"Sun",				"Sunborn",			"Sunder",			"Sunflare",			"Sunlit",			"Sunny",			"Sunset",			"Sunstone",			"Superb",			"Supernatural",		"Supernova",		"Supreme",			"Suspicious",		"Swamp",			"Swampy",				"Sweet",			"Swift",			"Sympathetic",		"Synthesis",		"Star", 			"Star",				"Silent",			"Stealth",			"Sea",				"Shadow",			"Smoke",			"Shelled",			"Snowy",			"Solar",			"Solstice",			"Sophisticated",	"Sorcery",				"Sorrowful",		"Stone",			"Sky",				"Slinking",			"Scorched",			"Supreme",				"Spell",			"Spark",			"Star",				"Storm",			"Skull",			"Spark",			"Sylvan",			"Sylvan",			"Solstice", 		"Sand",				"Sand",				"Seventh",			"Second",			"Stone",			"Silver",			"Silk",				"Sad",				"Science",				"Shadow",			"Skelleton",		"Scale",			"Smoke",			"Sneaky",			"Spring",				"Steam",			"Storm",			"Starting",			"Star",				"Strong",			"Spark",			"Spell",			"Sphinx", 			"Solar", 			"Summer",			"Spirit",			"Starry",			"Stellar",			"Sacred",			"Soul",				"Solar",			"Steel",			"Spirit",
				]
			# T
		descriptor += [
			"Thorn",	"Timeless",			"Temporal",			"Timebender",		"Time",				"Traditional",		"Timeless",			"Timely",			"Talisman",		"True",				"Tenacity",			"Treasure",			"Tomb",				"Time",			"Tomb",				"Tormented",		"Tempest",		"Troll",		"Tailed",		"Talisman",	"Tigerstrip",			"Time",			"Timeless",			"Timely",			"Titanic",			"Token",			"Tomb",		"Trick",		"Topaz",			"Torch",			"Totem",			"Town",				"Traditional",		"Trail",			"Trance",		"Tranquil",			"Transcend",		"Transcendent",		"Transient",		"Traveling",	"Treacherous",	"Tremendous",		"Tribal",			"Tribe",			"Tribunal",			"Trickster",			"Trojan",						"Tropical",			"True",			"Tudor",			"Tulip",			"Tundra",			"Turbulent",		"Turquoise",		"Turtle",			"Twilight",			"Twisted",			"Typhoon",			"Talon",		"Tangerine",		"Tartarean",		"Taupe",			"Tavern",			"Teal",			"Tectonic",		"Tempest",			"Tempestuous",		"Temple",		"Temporal",		"Tenacious",		"Tender",		"Tentacled",		"Terra",		"Terrified",		"Terrifying",		"Thaumaturge",		"Theater",			"Theocratic",		"Thicket",			"Third",			"Thorn",			"Thorny",			"Thousand",			"Threatening",		"Thunder",		"Thundering",		"Thunderous",		"Tidal",			"Tide",				"Timeless",		"Thorn",		"Talisman",		"Threatening",		"Time",		"Time-bender",		"Timebender",		"Timeless",		"Titanic",		"Twilight",		"Terrifying",		"Terrorific",		"True",				"Tower",			"Thunder",			"Thunder",			"Tomb",				"Third",			"Trival",			"Thunder",			"Terrifying",		"Treasure",			"Throne",			"Tide",				"Time",			"Timeless",
			]
			# U
		descriptor += [
			"Unnatural",	"Urban",		"Unyielding",	"Undead",		"Untamed",		"Underdark",		"Underworld",				"Undying",				"Unearthly",				"Unfathomable",				"Unflinching",				"Unforgiving",				"Unhappy",				"Universal",				"Universe",								"Unrevealed",				"Unseen",				"Unstoppable",				"Untamed",				"Unyielding",				"Uplifting",	"Uranian",		"Ursine",		"Utopic",		"Ultimate",			"Ultra",			"Ultra",			"Ultraviolet",			"Unassailable",			"Unbound",			"Unbreakable",			"Uncharted",			"Unconquerable",			"Undaunted",			"Undertow",			"Unholy",				"Underworld",
			]
			# V
		descriptor += [
			"Venerable",	"Venom",		"Venom",		"Venomous",		"Verdant",		"Vicious",			"Vigilant",			"Vigorous",			"Virtuous",			"Volcano",				"Volcanic",				"Voided",			"Void",				"Vintage",		"Venerable",		"Victorian",		"Valor",			"Valiant",			"Valkyrian",		"Valkyrie",								"Valley",				"Valor",				"Vampiric",				"Vanirian",		"Vault",		"Vapor",		"Vaporous",		"Vase",			"Veiled",			"Victorious",		"Vigilant",			"Viking",				"Village",			"Villainous",		"Vindicator",	"Vindictive",		"Vine",				"Vintage",			"Violent",			"Violet",			"Viridian",				"Virtuoso",				"Virtuous",				"Virulent",				"Visage",			"Visionary",				"Vitriolic",				"Void",			"Vengeful",		"Voidborne",	"Voided",		"Voidless",		"Volatile",			"Volcanic",			"Volcano",				"Voracious",		"Vortex",			"Vulcanian",		"Vulpine",			"Void",				"Void",				"Void",				"Vengeance",				"Vellum",				"Vendetta",				"Venerable",				"Vengeance",				"Vengeful",				"Venomous",		"Valiant",		"Venusian",				"Verdant",		"Vermilion",	"Vernal",		"Vertex",		"Vesper",		"Vesperal",			"Vessel",			"Veteran",			"Vibrant",			"Vicar",			"Vicious",			"Violet",			"Valiant",			"Vampiric",				"Veteran",				"Venom",				"Vicious",				"Volcanic",				"Venom",
			]
			# W
		descriptor += [
			"Walking",			"Wandering",		"Wealth",			"War",				"Waterborn",		"Water",			"Water",			"Wave",				"Whim",				"Whisper",		"Wholesome",		"Wild",			"Windborn",		"Wind",			"Windborn",		"Winged",		"Winter",		"Wooden",		"Wisdom",		"Witch",			"Wise",				"Winterborn",		"Wolf",			"Wrathful",		"Witty",			"Wandering",		"White",			"War",				"Wormhole",			"Warp",				"Winter",			"Windy",			"Wind",				"Wailing",			"Wind",				"Wild",				"Wind",			"Wood",				"Wand",			"Wave",			"Wandering",	"War",			"Warm",			"Warp",			"Warping",		"Wary",				"Water",			"Watery",		"Wave",			"Wavy",				"Weapon",			"Weatherlight",		"Web",				"Western",			"Wet",				"Whale",			"Whimsy",			"Whirlwind",		"Whispering",		"Whistle",			"White",			"Wicked",		"Wight",			"Wild",				"Wilderness",	"Wildfire",		"Willow",		"Windy",		"Winged",		"Winter",		"Winterborn",		"Wise",			"Wisp",			"Witchy",			"Withering",		"Witted",			"Wondrous",			"Woodland",		"Woods",			"Woody",			"Workshop",			"World",			"Wormhole",			"Worried",			"Wrathful",			"Woodland",			"Wind",			"White",			"Water",			"War",			"Warp",			"War",			"Warping",		"Water",		"White",		"Wise",				"Wind",			"Winter",		"Wild",				"Wolf",				"Wind",				"Wild",			"Wicked",
			]
			# X
		descriptor += [
			"X-Ray",			"Xenolith",			"Xenon",
			]
			# Y
		descriptor += [
				"Young",	"Young",				"Yearning",				"Yesteryear",				"Young",				"Youthful",				"Yellow",
				]
			# Z
		descriptor += [
			"Zephyr",	"Zodiacal",		"Zodiac",			"Zombie",			"Zealot",			"Zealous",			"Zen",			"Zenith",			"Zephyr",			"Zephyrian",			"Zestful",			"Zeusian",			"Zodiac",			"Zodiacal",			"Zone",			"Zoo",			"Zypher",			"Zombie",
			]
	except:
		descriptor += ["Dark"]

	# Backgrounds
	if "Barbarian"	in genus:
		descriptor += [
			"Raging",		"Wild",		"Fierce",		 "Savage",		 "Untamed",		 "Mighty",
			]
	if "Berserker"	in genus:
		descriptor += [
			"Raging",		"Wild",		"Frenzy",		"Unstoppable",		"Fury",		"Fierce",		 "Savage",		 "Untamed",		 "Mighty",		 "War",		 "Warrior",
			]
	if "Cultist" 	in genus:
		descriptor += [
			"Celestial",	"Cult",		"Fanatical",	"Friar",			"Mystical",		"Secret",			"Zealous",		"Obscure",
			]
	if "Charlatan"	in genus:
		descriptor += [
		"Deception",		"Charm",		"Charmming",		"Sly",		"Smooth",		"Stylish",		"Wealthy",		"Word",
		]
	if "Commoner" 	in genus:
		descriptor += [
		"Honest",		"Modest",
		"Simple",		"Village",
		]
	if "Crafter" 	in genus:
		descriptor = [
		"Mender",		"Master",
		"Skillful",		"Artisanal",
		"Dexterous",		"Inventive",
		]
	if "Criminal" 	in genus:
		descriptor += [
			"Barber",		"Mercenary",				"Crime",		"Underworld",		 "Sneaking",		 "Sneaky",		 "Ruthless",		 "Shade",		 "Shady",		 "Clever",
			]
	if "Cleric"		in genus:
		descriptor += [
			"Celestial",
			]
	if "Druid" 		in genus:
		descriptor += [
			"Tusked",			"Jungle",			"Natural",			"Earthy",			"Mystical",			"Primal",			"Guardian",			"Green",
			]
	if "Expert" 	in genus:
		descriptor += [
			"Historic",		"Knowledge",		"Skill",
			]
	if "Explorer" 	in genus:
		descriptor += [
			"Adventure",			"Brave",			"Daring",			"Jungle",			"Migratory",			"Nomadic",			"Nomad",			"Roaming",			"Traveling",			"Wandering",
			 ]
	if "Fighter" 	in genus:
		descriptor += [
		"Mercenary",		"Battle","Battle","Battleground","War",
		]
	if "Guardian" 	in genus:
		descriptor += [
			"Protector",	"Alert",		"Discipline",		"Protector",
			 ]
	if "Healer" 	in genus:
		descriptor += [
		"Celestial",	"Compassion","Heal","Wise","Care",
		]
	if "Hero" 		in genus:
		descriptor += [
			"Celestial",	"Valiant", "Brave", "Heroic", "Gallant",
			]
	if "Hunter" 	in genus:
		descriptor += [
			"Jungle",   "Green","Stealth", "Rugged",			 "Trapper", "Wild", "Gloom",
			]
	if "Knight" 	in genus:
		descriptor += [
			"Chivalrous",			"Gallant",			"Golden",			"Honorable",			"Bold",			"Cavalier",
			]
	if "Monk" 		in genus:
		descriptor += [
				"Celestial",	"Urn",				"Discipline",				"Spiritual",				"Meditative",				"Ascetic",				"Harmony",
				]
	if "Merchant" 	in genus:
		descriptor += [
			"Shrewd",			"Wealthy",			"Trading",			"Skilled",			"Resourceful",			"Prosperous",
			]
	if "Noble"		in genus:
		descriptor += [
			"Kingly",
			]
	if "Pirate" 	in genus:
		descriptor += [
				"Ruthless",			"Swashbuckling",				"Seafaring",							"Rebel",			"Infamous",				"Treasure",			"Booty",
				]
	if "Traveler"	in genus:
		descriptor += [
			"Migratory",			"Nomadic",			"Nomad",			"Roaming",			"Traveling",			"Wandering",			"Circus","Circus","Circus","Circus","Circus","Circus",			"Circus","Circus","Circus","Circus","Circus",
			]
	if "Trickster" 	in genus:
		descriptor += [
			"Surviving",			"Quick",			"Lonely",			"Resourceful",			"Scrappy",			"Streetwise",			"Surviving",			"Scrappy",			"Quick",
			]
	if "Priest"		in genus:
		descriptor = [
			"Celestial",	"Chapel",
			]
	if "Ranger" 	in genus:
		descriptor += [
			"Green",			"Jungle",			"Wilderness",			"Tracking",			"Survivalist",			"Rugged",			"Master",			"Survival",			"Rugged",
			]
	if "Rogue" 		in genus:
		descriptor += [
		  "Sneaky",  "Masterful",		  "Cunning",		  "Agile",		  "Mysterious",	  "Resourceful",		  "Shady",		  "Shadow",
		  ]
	if "Scholar" 	in genus:
		descriptor += [
			"Learned",	"Learned",	"Learned",			"Intellectual",	"Intellectual",	"Intellectual",			"Studious",	"Studious",	"Studious",			"Erudite",	"Erudite",	"Erudite",			"Inquisitive",	"Inquisitive",	"Inquisitive",
			]
	if "Soldier" 	in genus:
		descriptor += [
			"Veteran",	"War",	"Battle",	"Hardened",		"Strategic",	"Brave",	"Tactical",	"Special",	"Tactical",	"Brave",		"Last",	"First",	"Battle",	"Hardened",	"Hierarchy",			"Strategist",
				]
	if "Shaman" 	in genus:
		descriptor += [
			"Green",			"Jungle",			"Spiritual",			"Mystic",			"Elemental",			"Tribal",			"Ancestral",			"Shamanic",
			]
	if "Spy" 		in genus:
		descriptor += [
			"Spy",			"Undercover",			"Covert",			"Undercover",			"Secret",			"Stealthy",			"Infiltrating",			"Covert",			"Undercover",			"Secret",			"Stealthy",			"Infiltrating",
			 ]
	if "Traveler" 	in genus:
		descriptor += [
			"Jungle",			"Wandering",		"Adventure",			"Nomad",			"Curious",			"World",
			]
	if "Witch" 		in genus:
		descriptor += [
			"Dark",		"Enchanting",			"Hexing",			"Mystical",			"Occult",			"Wise",
			]

	# Races
	if "Aberration" in genus:
		descriptor += [
			"Starship",
			]
		if "Githzerai" 			in genus:
			descriptor += [
			"Enlightened","Zen",
			 "Mystic",
			 "Ascet","Spiritual",
			 "Harmonious","Harmony",
			 ]
		if "Githyanki" 			in genus:
			descriptor += [
				"Marauding",
				"Conquering",
				"War",
				"Ruthless",
				"Dominant",
				]
		if "Destiny Devouers" 	in genus:
			descriptor += [
				"Oracle",
				"Time",
				"Body",
				"Destiny",
				"Fate",
				"Chrono",
				"Fate",
				"Traveling",
				"Temporal",
				"Altered",
				"Shattered",
				"Future",
				"Swapping",
				]
		if "Parasyte" 			in genus:
			descriptor += [
			"Parasitic","Infestation",
			 "Mind","Control",
			 "Body","Snatcher",
			 "Host","Taker","Infested",
			 "Infesting","Neural"]
		if "Alien Spawn" 		in genus:
			descriptor += [
			"Celestial",
			"Galactic",
			"Extraterrestrial",
			"Distant",
			"Alien",
			"Outer",
			"Unearthly",
			"Starborne",
			]
		if "Chaos Warper" 		in genus:
			descriptor += [
			"Star",
			"Galactic",
			"Cosmic",
			"Nebula",
			"Golden",
				"Cosmic",
				"Starborn",
				"Astral",
				"Nebulous",
				"Galactic",
				"Nebula",
				"Star",
				"Galaxy",
				]
		if "Symbioid" in genus:
			descriptor += [
				"Symbioitic",
				"Communing",
				]
	if "Aven" 		in genus:
		descriptor += [
			"Celestial",	"Sky",		"Feathered",	"Aerial",
			]
		if "Owlin" in genus:
			descriptor += [
						"Nocturnal",
						"Wise",
						"Silent",
						"Moon",
						"Feathered",
						"Stargazer",
						"Night",
						"Star",
						]
		if "Raptoran" in genus:
			descriptor += [
			 "Mountain",
			 "Falcon",
			 "Windsoarer",
			 "Cliffdweller",
			 "Wingwarrior",
			 "Highflyer",
			 "Cliff",
			"Sky",
			"Peak",
			"Windrider",
			"Aerie"]
		if "Aarakocra" in genus:
			descriptor += [
				"Soaring",
				 "Spiritual",
				 "Windrider",
				 "Feather",
				 "Skydancer"]
		if "Kenku" in genus:
			descriptor += [
			"Mimicking",
			 "Crafty",
			 "Raven",
			 "Streetwise",
			 "Scheming"]
		if "Birdfolk" in genus:
			descriptor += [
			"Flock",
			"Nest",
			"Wing",
			"Feathered",
			]
		if "Avens" in genus:
			descriptor += [
			"Avian",
			"Golden",
			"Red","Sky",
			"Feathered",
			"Yellow","Wing",
			"Skybound",
			"Winged","Flight",
			"Wind","Feathered",
			"Aerial","Aerie",
			"Soaring",
			]
		if "Tengu" in genus:
			descriptor += [
			"Mystical","Ancient",
			 "Folkloric",
			 "Martial",
			 "Wise",
			 "Trickster",
			"Mystic","Raven",
			"Kenshi","Master",
			"Lore",
			"Shadow",
			]
	if "Beast" 		in genus:
		descriptor += [
			"Tusked",			"Wild",
			]
		if "Kong" 			in genus:
			descriptor += [
			"Kong",
			"Silverback",
			"Colossal",
			"Jungle",
			"Mighty",
			"Fierce",			"Vigilant",
			"Primal",			"Island",
			"Ancient",
			"Titan",			"Colossal",
			"Untamed",
			]
		if "Armored Bear" 	in genus:
			descriptor += [
				"Bear","Iron",				"Armor","Ice",
				"Claw","Northern",				"Claw","Stalwart",				"Ursine", "Ursa",
				]
		if "Giant Eagle" 	in genus:
			descriptor += [
				"Celestial",	  "Majestic",				  "Sky",				  "Soaring",				  "Keen",				  "Eagle",				  "Sky",				  "Wing",				  "Aerial",				  "Feather",
				  ]
		if "Tiger" 			in genus:
			descriptor += [
				"White",				"Feline",
				"Silent",
				"Fierce",				"Snow",
				"Mystic",				"Alabaster",
				"Stealth",
				"Silent",				"Snow",
				"Frost",				"Amber",
				]
		if "Vulture Spirit" in genus:
			descriptor += [
			"Celestial",		"Carrion",
			 "Death",
			 "Spirit",
			 "Sight",
			 "Scavenger"]
		if "Deer Spirit" 	in genus:
			descriptor += [
				"Amber",
				"Forest",
				"Gentle",
				 "Graceful",
				 "Spirit",
				 "Gentle",
				 "Nature",
				 "Woodland",
				 "Whispering",
				 "Gentle",
				]
		if "Owl"			in genus:
			descriptor += [
			"Ancient",
			"Night",
			"Silent",
			"Mystic",
			"Wise",
			]
		if "Lion"			in genus:
			descriptor += [
				"Feline",
				]
	if "Celestial" 	in genus:
		descriptor += [
			"Amber",			"Astral",
			"Blessed",
			"Celestial",	"Celestial",
			"Dark",			"Darkness",
			"Divine",
			"Ethereal",
			"Fire",			"Flame",
			"Golden",
			"Green",			"Heavenly",

			"Radiant",
			"Sacred",			"Shadow",
			"Sky",			"Sublime",
			"Yellow",
			"Luminous",
			]
		if "Planetar" in genus:
			descriptor += [
				"Mighty",				"Divine",
				"Radiant",				"Just"]
		if "Angelic Bloodline" in genus:
			descriptor += [				"Born",
				"Touched",
								]
	if "Construct"	in genus:
		descriptor += [
			"Clockwork",	"Living",			"Titanium",		"Iron",			"Steel",	"Palladium",
			]
	if "Dwarf"		in genus:
		descriptor += [
			"Bearded",
			"Clan",
			"Dwarven",
			"Bearded",
			"Tunnel",
			]
	if "Dragon"		in genus:
		descriptor += [
		"Draconic",
		"Dragon","Dragon","Dragon","Dragon",
		]
		if "Wyrm" 		in genus:
			descriptor += [
			"Serpentine",
			  ]

		if "Silver" in genus:
			descriptor += [
			"Silver",
			"Quicksilver",
			"Metal",
			"Metallic",
			   ]
	if "Elf"		in genus:
		descriptor += [
		"Elven","Elven","Elven","Elven",
		"Elvish",
		]
	if "Fiend" 		in genus:
	  descriptor += [
		"Fiendish",
		"Hellish",
		"Satanic",
		]
	if "Fae"		in genus:
		descriptor += [
			"Vendilion",
			]
	if "Giant"		in genus:
		descriptor += [
			"Gigantic",
			]
	if "Gnome"		in genus:
		descriptor +=[
		"Gnomish",
		]
	if "Human"		in genus:
		descriptor += [
		"Mortal",
		]
	if "Halfling"	in genus:
		descriptor += [
		"Plucky",
		]
	if "Orc"		in genus:
		descriptor += [
		"Tusked",
		"Green",
		"Green Skin",
		]
	if "Ooze"		in genus:
		descriptor += [
		"Amber",
		]
	if "Plant"		in genus:
		descriptor += [
			"Spore",
			"Treefolk",
			"Green",
			]
		if "Dryad" 		in genus:
			descriptor += [
			"Dryad",
				]
	if "Undead" 	in genus:
		descriptor += [
			"Mausoleum",	"Spooky",			"Urn",			"Mummy","Mummy","Mummy","Mummy",			"Necrotic",			"Skeletal",			"Zombified",			"Undead",			"Rusalka",			"Dreamborn",			"Ghoulish",			"Ghostly",
			]
	if "Vampire" in genus:
		descriptor += [
			"Sanguine",			"Sanguine",				"Bloodtithe",				"Vampiric",
			]
	if "Sun Scarab" in genus:
		descriptor += [
			"Amber",
			"Ancient",
			"Astral",
			"Eternal",
			"Gold",
			"Golden",
			"Radiant",
			"Resilient",
			"Sacred",
			"Solar",
			"Yellow",
			]
	if "Eosian" 	in genus:
		descriptor += [
			"Dawnbringer",
			"Daybreak",
			"Daylight",
			"Ethereal",
			"Luminous",			"Morning",
			"Radiant",
			"Solar",
			"Sunlit",
			"Sunrise",
			]
	if "Nymph" 		in genus:
		descriptor += [
			"Forest",		"Graceful",			"Nature",			"Nymph",			"Water",
			]
	if "Celestial" in genus:
		descriptor += [
			"Divine",
			"Holy",
			"Celestial",
			"Celestian",
			]
	if "Angel" in genus:
		descriptor += [
			"Angelic",
			"Divine",
			"Holy",
			"Messenger",
			"Seraphic",
			"Winged",
			]
	if "Atlantian" in genus:
		descriptor += [
			"Ancient",
			"Aquatic",
			"Deepsea",
			"Nautic",
			"Ruinbound",
			]
	if "Dragonborn" in genus:
		descriptor += [
			"Blueblood",
			"Dragonborn",
			"Fireblood",
			"Greenblood",
			"Iceblood",
			"Nightblood",
			]
	if "Noble" in genus:
		descriptor += [
			"Graceful",
			"Influential",
			"Mayor",
			"Noble",
			"Refined",
			"Ruler",
			"Sovereign",
			"Aristocratic",
			"Bountiful",
			]
	if "Hunter" in genus:
	  descriptor += [
		"Primal",

		]
	if "Monkey King" in genus:
	  descriptor += [
		"Cunning",
		"Mammalian",
		"Mighty",
		"Monkey",
		"Tricking",
		"Tricksy",
		"Whimsy",
		"Adventuring",
		]
	if "Birdfolk" in genus:
	  descriptor += [
		"Flying",
		"Songbird",
		]
	if "Cleric" in genus:
	  descriptor += [
		"Devout",
		"Golden",
		"Holy",
		"Righteous",
		"Spiritual",
		"Blessed",
		]
	if "Beast" in genus:
		descriptor += [
			"Jungle",		"Sylvan",			"Nature",			"Beast",
			]
	if "Chaotic" in genus:
	  descriptor += [
		"Anarchic",
		"Erratic",
		"Mad",
		"Unpredictable",
		"Whimsical",
		"Free",
		]
	if "Dragon" in genus:
	  descriptor += [
		"Clever",		"Dark",		"Destroyer",
		"Draconic",
		"Eternal",		"Evil",		"Fierce",
		"Fierce",		"Fire",		"Fire",		"Flame",		"Furious",
		"Gentle",		"Great",		"Grumpy",		"Hungry",		"Intelligent",
		"Jealous",		"Jungle",
		"Kind",		"Magnificent",
		"Magnificent",
		"Majestic",
		"Maximum",
		"Mysterious",
		"Powerful",
		"Scaled",
		"Sky",
		"Sky",
		"Strong",
		"Stubborn",
		"Voiceless",
		"Warm",
		"Winged",
		"Wise",
		"Reptile",
		]
	if "Illithid" in genus:
	  descriptor += [
		"Mindbender",
		"Psionic",
		"Telepathic",
		"Thoughtstealer",
		"Brainfeeder",
		]
	if "Aberration" in genus:
	  descriptor += [
		"Alien",
		"Aberrant",
		"Astral",
		"Eldritch",
		"Eldritch",
		"Existential",
		"Formless",
		"Forsaken",
		"Green",
		"Horror",		"Identity",		"Jungle",		"Lost",		"Mind",		"Nether",
		"Soulless",		"Underworld",		"Unworldly",		"Yellow",
		]
	if "Beholder" in genus:
		descriptor += [
			"All Seeing",		"Beholder",		"Omniscient",		"Paranoid",		"Tyrannical",		"Unblinking",		"Visionary",
			]
	if "Old One" in genus:
		descriptor += [
			"Ancient",
			"All Knowing",
			"Eldritch",
			"Mysterious",
			"Old",
			"Timeless",
				]
	if "Mindlinker" in genus:
	  descriptor += [
		"Benevolent",
		"Knowledge",
		"Linker",
		"Mind",
		"Seeker",
		"Thought",
		"Weaver",
		"Wise",
		]
	if "Dominators" in genus:
	  descriptor += [
		"Commanding",
		"Hierarchical",
		"Ruthless",
		"Subjugating",
		"Tyrant",
		"Master",
		]
	if "Priest" in genus:
	  descriptor += [
		"Clerical",
		"Devout",
		"Faithful",
		"Holy",
		"Pious",

		"Sacred",
		]
	if "Undead" in genus:
		descriptor += [
		"Morgue",
		"Cursed",	"Urn",
		"Deathly",
		"Dreadhorde",
		"Eternal",
		"Ethereal",
		"Ghostly",
		"Ghoul",
		"Haunting",
		"Spectral",
		"Undead",
		"Zombie",
		"Ancient",
		]
	if "Warlock" in genus:
	  descriptor += [
		  "Eldritch",
		  "Fallen",
		  "Mage",
		  "Mysterious",
		  "New",
		  "Otherworldly",
		  "Pact",
		  "Arcane",
		  ]
	if "Illithid" in genus:
		descriptor += [
			"Brainfeaster",
			"Cerebral",
			"Deep",
			"Dimensional",
			"Dreamweaver",
			"Eldritch",
			"Illithid",
			"Inscrutable",
			"Insidious",
			"Mindbending",
			"Mindflayer",
			"Mindreaper",
			"Otherworldly",
			"Psionic",
			"Shadowspeaker",
			"Soulflayer",
			"Starcaller",
			"Telepathic",
			"Tentacled",
			"Thoughtstealer",
			"Trascendent",
			"Unarcaned",
			"Voidborn",
			"Voidgazer",
			"Warp",
			"Warpwalker",
			"Astral",
			]
	if "Shapeshifters" in genus:
		descriptor += [
			"Amorphous",
			"Changeling",
			"Formless",
			"Mimic",
			"Mutant",
			"Protean",
			]
	if "Living Spell" in genus:
		descriptor += [
			"Arcane",
			"Enchanted",
			"Enchantment",
			"Ethereal",
			"Golden",
			"Green",
			"Magenta",
			"Magic",
			"Magical",
			"Spellbound",

			"Wizardly",
			"Amber",
			]
	if "Dog" in genus:
		descriptor += [
			"Fierce",			"Hellhound",			"Loyal",			"Mammal",		"Three Head",
			]
	if "Warrior" in genus:
		descriptor += [
			"Battle",			"Fearless",		"Honorable",			"Mighty",			"Ready",			"Skilled",
			]
	if "Alien Spawn" in genus:
		descriptor += [
			"Alien",			"Extraterrestrial",		"Otherworldly",			"Starborne",			"Unearthly",
			]
	if "Monstrosity" in genus:
		descriptor += [
			"Beastly",			"Fearsome",			"Monstrous",			"Mythical",			"Terrifying",			"Yellow",
			]
		if "Sphynx" in genus:
			descriptor += [
				"Thoughtful",
				]
	if "Mage" in genus:
		descriptor +=[
			"Sorcerer",			"Sorcerous",
			]
	if "Elf" in genus:
		descriptor +=[
			"Elfstone",			"Fae",
			]
	if "Fey" in genus:
		descriptor +=[
			"Fey",	"Fae",
			]
	if "Ghost" in genus:
		descriptor += [
			"Ethereal",			"Mournful",			"Pain",			"Sorrow",			"Unresolved",			"Urn",			"Unholy",
			]
	if "Catfolk" in genus:
		descriptor += [
			"Agile",		"Amber",		"Cat",		"Claw",		"Feline",		"Mammalian",		"Mystical",		"Prowler",		"Shadow",		"Stealthy",		"Whiskered",		"Whiskers",
			]
	if "Centaur" in genus:
		descriptor += [
			"Centaur",			"Equs",			"Forest",			"Horse",			"Herd",			"Hooved",					"Wildheart",
			]
	if "Fiend" in genus:
		descriptor += [
			"Amber",			"Caustic",			"Contaminated",			"Dark",			"Demon",			"Demonic",			"Diabolical",			"Fiendish",			"Hell",			"Infernal",			"Liar",			"Malevolent",			"Red",			"Sinister",			"Unholy",
			]
	if "Owl" in genus:
		descriptor += [
			"All Seeing",			  "Mystic",			  "Mystical",			  "Night",			  "Nocturnal",			  "Omniscient",			  "Silent",			  "Silentwing",			  "Wisdom",			  "Wise",
			]
	if "Kitsune" in genus:
		descriptor += [
			"Nine Tales",		"Amber",			"Masked",			"Astral",			"Blue",			"Blue",			"Cunning",			"Enchanted",			"Enchanter",			"Enchanting",			"Fox",		"Foxfire",			"Foxy",			"Golden",			"Illusion",			"Illusory",		"Mystic",			"Mystical",			"Nine Tailed",			"Nine Tailed",			"Red",			"Tailed",			"Tale",			"Trickster",			"Trickster",		"Yellow",

			]
	if "Lion" in genus or "Leon" in genus:
		descriptor += [
				"Amber",				"Brave",				"Exalted",				"Gold",				"Golden",				"Golden",				"Lion",				"Majestic",				"Mammalian",				"Pride",				"Pride",				"Regal",				"Roaring",				"Sun",				"Sunlit",				"Yellow",
				]
	if "Mage" in genus:
		descriptor += [
			"Arcane",			"Black",			"Blue",			"Crimson",			"Dark",			"Enigmatic",			"Golden",			"Green",			"Grey",			"Learned",			"Mystical",			"Rainbow",			"Red",			"Scholar"			"Sorcerous",			"Spellbinder",			"White",			"Yellow",
			]
	if "Ooze" in genus:
		descriptor += [
			"Absorbing",		  "Absorbing",		  "Acidic",		  "Amorphous",		  "Amorphous",		  "Ashen",		  "Crystalline",		  "Cubic",		  "Dark",		  "Earthen",		  "Fiery",		  "Fluidic",		  "Fungal",		  "Gelatinous",		  "Gelatinous",		  "Glowing",		  "Icy",		  "Mystical",		  "Poisonous",		  "Shapeless",		  "Shapeless",		  "Slime",		  "Slithering",		  "Slithering"		  "Sticky"		  "Thick"		  "Translucent"		  "Viscous",		  "Viscous",		  "Viscous",
			]
	if "High" in genus:
		descriptor += [
			"Elevated",			"High",			"Refined",
			]
	if  "Merchant" in genus:
		descriptor += [
			"Bountiful",
			]
	if  "Crafter" in genus:
		descriptor += [
			"Crafty",	"Urn",
			]
	if  "Mountain" in genus:
		descriptor += [
			"Crafty",	"Rugged",		"Snowy",			"Stoic",			"Unyielding",			"Enduring",			"Harsh",			"Mountain",			"Resilient",			"Earthen",			"Stone",			"Deep",			"Rooted",			"Gritty",			"Metalwork",			"Ancestral",			"Tough",			"Boulder",			"Unmovable",			"Iron",			"Strong",			"Mining",			"Gem",			"Ore",			"Frost",	"Ale",		"Echo",			"Gold",			"Silver",			"Mithril",			"Carver",
			]
	if "Sea" in genus:
		descriptor += [
			"Aquatic",			"Piscine",			"Coastal",			"Maritime",			"Oceanic",			"Gilled",
			]
	if "Etherian" in genus:
		descriptor += [
			"Ethereal",			"Luminous",			"Heavenly",			"Celestial",			"Stardust",
			]
	if "Snakefolk"	in genus:
		descriptor += [
			"Ophidian",
			]
	# By Alignment
	if "Good" in genus:
		descriptor +=[
			"Celestial",	"Helping",			"Benevolent",
			]
	if "Lawful" in genus:
		descriptor += [
		"Hierarchy",		"Disciplined",
		]
	if "Chaotic" in genus:
		descriptor += [
			"Untamed",			"Chaos",			"Chaos",		"Anarchy",			"Mad",			"Free",			"Chaotic",			"Unpredictable",			"Mad",			"Erratic",			"Anarchic",			"Anarchist",
			]
	if "Good" 		in genus:
		descriptor += [
			"Tender",			"Hopeful", "Joyful", "Jubilant", "Jovial",
			]
	if "Evil"		in genus:
		descriptor += [
			"Dark",			"Evil",					"Malignant",					"Pillager",			"Cruel",	"Nefarious", "Aggressive","Angry","Annoyed","Apathetic","Irate", "Jealous", "Hostile",
			]
	if "Lawful" 	in genus and "Good" in genus:
		descriptor += [
			"Holy",
			]

	descriptor += [
		"Green",		"Angelic",		"Amethyst",		"Amber",		"Amber",	"Hollow",	"Empty",			"Arcane","Alchemical","Apothecarian","Arcanic",			"Magical",			"Wand","Wizard",			"Arcane", "Alchemical",			"Arcanic", "Magic",			"Wand", "Wizardry", "Myrmidonic", "Mystic", "Mystical", "Mythical"	"Lavender",	"Oceanic",	"Glacial",	"Blind","Mad",	"Gallant","Generous","Kind","Unbreakable","Valiant",	"Orphean","Abyssal", "Daemonian", "Infernal", 	"Hellish",		"Holy", 		"Crystal",		"Earth",	"Omniscient",	"Magenta",	"Yellow", "Golden", "Goldenrod","Ochre",					"Lime",					"Green", "Jade","Olive",					"Azure", "Blue", "Cerulian","Indigo",					"Lavender",					"Beige","Ivory","Graphite",					"Iridescent",					"Gold","Golden",					"Graphite","Onyx",					"Ivory",				"Gemmed",		"Jewel",		"Jewelcraft",	"Eternal",		"Glimmer",		"Glaive",	"Gem",		"Ghost",	"Gale",		"Gaze",	"Jeweled",	"Northern",		"Opal",	"Jade",	 "Quartz", 		"Red", 		"Topaz",	"Xenolith","Elfstone",		"Deep",		"Scrappy",		"Honor",		"Mighty",		"Fearless",		"Battle",		"Ghost",		"Cloud",		"Dream",	"Gloom",		"Golden",		"Graceful",		"Green",		"Grove",		"Heart",		"Hell",		"Hidden",		"High",			"Horn",			"Hydra",		"Lamp",			"Last",		"Leaf",		"Lore",		"Lost",		"Lunar",		"Magenta",		"Master",		"Maze",		"Mind",		"Mischief",		"Mystic",		"Night",		"Plains",		"Planar",		"Potion",		"Pride",		"Proud",		"Red",		"Rune",		"Sacred",		"Sky",		"Spell",		"Star",		"Silk",		"Stone",		"Story",		"Tunneling",		"Vine",		"Yellow",		"Reptile",		"Ruby",			"Turtle",	"Furious",	"Ghostly",	"Hesperidean",	"Ice",	"Illustrious",	"Imaginative",	"Inscrutable",	"Interstellar",	"Lagoon",	"Leviathan",	"Lime",	"Liquid",	"Lord",	"Lunar",	"Majestic",	"Malign",	"Martial",	"Merry",	"Meteor",	"Meteoric",	"Mighty",	"Mirthful",	"Monstrous",	"Moonlit",	"Mystical",	"Occult",	"Oracle",	"Oracular",	"Ordinance",	"Pathfinder",	"Peerless",		"Perennial",	"Perfumed",		"Perilous",		"Petrified",	"Phantom",		"Pillar",	"Piqued",	"Planetary",	"Plum",	"Poetic",	"Polar",	"Precocious",	"Predatory",	"Profound",	"Promethean",	"Protector",	"Psychic",
		]
	try:
		descriptor += [
			f"{lusor.archetype}",	f"{lusor.archetype}",	f"{lusor.archetype}",	f"{lusor.archetype}",	f"{lusor.archetype}",	f"{lusor.archetype}",	f"{lusor.archetype}",	f"{lusor.archetype}",	f"{lusor.archetype}",	f"{lusor.archetype}",
			f"{lusor.race}",		f"{lusor.race}",		f"{lusor.race}",		f"{lusor.race}",		f"{lusor.race}",		f"{lusor.race}",		f"{lusor.race}",		f"{lusor.race}",		f"{lusor.race}",		f"{lusor.race}",
			f"{lusor.subrace}",		f"{lusor.subrace}",		f"{lusor.subrace}",		f"{lusor.subrace}",		f"{lusor.subrace}",		f"{lusor.subrace}",		f"{lusor.subrace}",		f"{lusor.subrace}",		f"{lusor.subrace}",		f"{lusor.subrace}",	f"{lusor.subrace}",	f"{lusor.subrace}",
			]
	except:
		try:
			descriptor += [
				f"{lusor.species}",	f"{lusor.species}",	f"{lusor.species}",	f"{lusor.species}",	f"{lusor.species}",	f"{lusor.species}",	f"{lusor.species}",	f"{lusor.species}",	f"{lusor.species}",	f"{lusor.species}",
				f"{lusor.char_class}",		f"{lusor.char_class}",		f"{lusor.char_class}",		f"{lusor.char_class}",		f"{lusor.char_class}",		f"{lusor.char_class}",		f"{lusor.char_class}",		f"{lusor.char_class}",		f"{lusor.char_class}",		f"{lusor.char_class}",
				f"{lusor.subclass}",		f"{lusor.subclass}",		f"{lusor.subclass}",		f"{lusor.subclass}",		f"{lusor.subclass}",		f"{lusor.subclass}",		f"{lusor.subclass}",		f"{lusor.subclass}",		f"{lusor.subclass}",		f"{lusor.subclass}",	f"{lusor.subclass}",	f"{lusor.subclass}",
				f"{lusor.background}",		f"{lusor.background}",		f"{lusor.background}",		f"{lusor.background}",		f"{lusor.background}",		f"{lusor.background}",		f"{lusor.background}",		f"{lusor.background}",		f"{lusor.background}",		f"{lusor.background}",	f"{lusor.background}",	f"{lusor.background}",
				]
		except:
			pass

	return random.choice(descriptor)

def Rank(lusor):
	'''
	General rule: If you can say
	- The Dark X -
	and sounds cool!!!
	X goes here
	'''
	genus = Genus(lusor)
	MALE    = "He"    in genus
	FEMALE  = "She"   in genus
	AGENDER = "They"  in genus

	rank = []

	# Ordered by First letter
	try:
		# A
		rank += [
			"Arcanist",			"Ash",				"Alpha",			"Abysswalker",		"Ambassador",			"Ambition",			"Appetite",			"Angel",			"Archfey",			"Archmage",			"Aristocrat",			"Avatar",			"Artist",			"Artisan",			"Armor",			"Anarch",			"Ascendant",			"Acolyte",			"Archer",			"Arbiter",			"Apprentice",			"Arsonist",			"Assassin",			"Arbiter",			"Archer",			"Assassin",			"Abomination",		"Anarquist",		"Arrow",				"Apostle",			"Apprentice",			"Avatar",			"Abomination",			"Acolyte",			"Alchemist",			"Aprentice",			"Arrow",			"Archer",			"Archfey",			"Archmage",			"Armour",			"Ash",			"Assassin",			"Anarchist",			"Anthropologist",			"Abbess",			"Abbot",			"Abyss",			"Abysswalker",		"Acolyte",			"Admiral",			"Adventure",			"Adventurer",			"Adversary",			"Agent",						"Alpha",			"Ambassador",			"Ambition",			"Amulet",			"Anarchist",			"Angel",			"Anthropologist",			"Antler",			"Apparition",			"Appetite",			"Apprentice",			"Apprentice",			"Aprentice",		"Arcanist",			"Archbishop",		"Archduke",			"Archer",			"Archivist",			"Argonaut",			"Armour",			"Arrow",			"Artificer",			"Artisan",			"Ascendant",			"Ash",			"Assassin",			"Astral",			"Astrologer",			"Astronomer",			"Atlas",			"Augur",			"Auralist",			"Auramancer",			"Avatar",			"Avenger",
			]
		# B
		rank += [
		"Born",			"Bringer",		"Brutal",		"Bard",			"Buccaneer",		"Bound",			"Blaze",			"Banner",			"Bird",			"Bowmaster",			"Behemoth",			"Bound",			"Bruiser",			"Born",			"Bull",			"Blade",			"Behemoth",			"Benefactor",			"Blade",			"Bringer",			"Baboon",			"Bard",			"Baron",			"Basilisk",			"Benefactor",			"Berserker",	"Bear",			"Beholder",		"Blade",		"Bow",				"Bringer",			"Butterfly",			"Beetle",			"Burglar",			"Bull",			"Baboon",			"Badger",			"Bearer",			"Band",			"Bane",			"Banner","Banner",			"Banshee",						"Barbarian",			"Baron",			"Baroness",			"Barrow",			"Basilisk",			"Battlefury",			"Beacon",			"Bear",			"Bearer",		"Beastmaster",	"Beastrider",	"Beauty",			"Beetle",			"Bender",			"Benefactor",			"Berserker",			"Bibliomancer",			"Breath",			"Binder",			"Bison",			"Blacksmith",			"Blade",			"Blade",			"Bearer",			"Blade",		"Singer",			"Blaze",			"Blaze",			"Blessing",			"Blight",			"Blizzard",			"Blood",		"Boar",			"Bone",			"Boot",			"Botanist",		"Bounty Hunter",	"Bounty",			"Bow",			"Brand",			"Bravo",			"Breaker",			"Breath",			"Brewer",			"Briar",			"Brigadier",			"Bringer",			"Buccaneer",			"Bull",			"Burglar",			"Butcher",			"Butterfly",			"Banshee",			"Blessed",
			]
		# C
		rank += [
			"Custodian",		"Crow",				"Conquistador",		"Colonel",			"Commander",		"Chronist",			"Captain",			"Caller",			"Composer",			"Crafter",			"Chief",			"Conjurer",			"Count",			"Collector",			"Crusader",			"Commander",			"Catcher",			"Curse",			"Caller",			"Cyclop",			"Commander",			"Cedar",			"Catapulter",			"Crafter",			"Chief",			"Collector",		"Collector",		"Crystal",			"Champion",			"Cat",			"Captain",			"Chemist",			"Champion",			"Charlatan",			"Chimera",			"Collector",			"Collosus",			"Commander",			"Chosen",			"Cadet",			"Caliph",			"Caller",			"Camel",			"Cannibal",			"Canon",			"Cantor",			"Captain",			"Cardinal",			"Cartographer",		"Cat",				"Cauldron",			"Cavalier",			"Centurion",		"Champion",			"Chancellor",			"Change",			"Chanter",			"Chaplain",			"Charlatan",			"Chaser",			"Cheetah",			"Chemist",			"Chief",			"Chieftain",			"Chimera",			"Chosen",						"Claw",			"Cleric",			"Climber",			"Cloak",			"Codex",			"Collector",		"Collosus",			"Colonel",			"Colossus",			"Commander",			"Commodore",			"Conjurer",			"Conqueror",			"Conquistador",			"Consul",			"Corsair",			"Cossack",			"Cougar",			"Councillor",			"Counselor",			"Count",			"Courage",			"Covered",			"Coyote",			"Craft",			"Crasher",			"Creation",			"Crocodile",		"Crown",			"Crow",				"Cruor",			"Crusader",			"Crypt",			"Cultist",			"Curator",			"Curse",			"Cursed",			"Czar",			"Caller",			"Commander",
			]
		# D
		rank += [
			"Drake",			"Duelist",			"Dreamer",		"Detective",		"Dreamweaver",		"Dancer",		"Doctor",					"Devil",			"Death",			"Diviner",			"Dancer",			"Devastator",			"Defender",			"Dust",			"Dweller",			"Demon",			"Doctor",			"Doctor",			"Dragon",			"Doctor",			"Diamond",			"Dagger",			"Dancer",			"Dragon",			"Devourer",			"Diviner",			"Dancer",		"Darkness",			"Diamond",			"Deer",			"Death",			"Devil",		"Doctor",			"Drake",			"Druid",			"Dream",			"Devourer",			"Defiler",			"Daisy",			"Dame",			"Dance",			"Dancer",			"Daredevil",			"Darkness",			"Dawn",			"Deacon",			"Dean",			"Death",			"Decay",			"Deceiver",			"Deepseer",			"Deer",			"Defender",		"Deity",			"Delegate",			"Delver",		"Demigod",			"Demon",		"Demonhunter",			"Demon",			"Demonologist",			"Depth",			"Depths",			"Derringer",			"Descendant",			"Desolation",			"Desperado",			"Despot",			"Detective",			"Devil",			"Devotion",			"Devourer",			"Diamond",			"Dictator",			"Dinosaur",		"Diplomat",		"Disciple",		"Discoverer",		"Doctor",			"Dolphin",		"Dominator",		"Doom",			"Dove",			"Dragon",			"Drake",			"Dread",			"Dream",			"Dryad",			"Demonologist",			"Dancer",			"Devourer",			"Drifter",			"Druid",			"Drum",			"Dryad",			"Duelist",						"Duke",			"Delver",			"Dungeoneer",
			]
		# E
		rank += [
			"Emissary",				"Enigma",			"Entity",			"Envoy",		"Ethereal",		"Exile",	"Envoy",		"Ethereal",		"Executioner",		"Endeavor",			"Emperor",			"Evangelist",			"Eye",			"Eyes",			"Enforcer",			"Eyes",			"Executioner",			"Element",			"Eagle",			"Eater",			"Eclipse",			"Enforcer",			"Elite",			"Element",			"Enchanter",			"Executioner",			"Engineer",			"Elder",			"Executioner",			"Entity",			"Eagle",			"Earthshaper",			"Eater",			"Echo",			"Echomancer",			"Eclipse",			"Elder",			"Eldest",			"Elector",			"Elegance",			"Element",			"Elementalist",			"Element",			"Elephant",			"Elite",			"Envoy",			"Embrace",			"Emissary",			"Enchanter",			"Enchantment",		"Enchantress",			"Endeavor",			"Enforcer",			"Enigma",			"Envoy",			"Envy",			"Etherbound",			"Ethereal",						"Executioner",			"Exemplar",			"Exile",			"Exorcist",			"Expeditioner",			"Explorer",			"Eye",			"Eyes",
			]
		# F
		rank += [
			"Firestarter",		"Figure",			"Falconer",			"Fanatic",		"Freedomfighter",		"Frontier",		"Farwalker"		"Fallen",		"Fel",		"Fiend",		"Forsaken",		"Foreseer",		"Forged"		"Fern",		"Feather",		"Frost",		"Fire",		"Flame"		"Fellow",		"Fin",		"Flutist",		"Farrier",		"Fury"		"Fisher",		"Fire",			"Forge",			"Fighter",			"Fairy",			"Feather",			"Fire",				"Fool",				"Fury",				"Fist",			"Fool",				"Fire",			"Farmer",			"Fanatic",			"Fire",			"Fury",			"Flutist",			"Flame",			"Fighter",			"Forged",			"Force",			"Fighter",			"Frost",			"Flamebearer",			"Falcon",			"Falconer",			"Fall",			"Fallen",			"Fanatic",			"Fang",			"Farmer",			"Farwalker",		"Fatesealer",			"Faun",				"Fawn",			"Fear",			"Feather",			"Feathered",			"Fel",			"Fellow",			"Fern",			"Fiend",			"Finder",			"Fire",			"Fisher",			"Flame",			"Flight",			"Flutist",			"Foil",			"Forerunner",			"Foreseer",			"Forge",			"Forged",			"Forger",			"Forsaken",		"Fox",			"Fragment",			"Freedomfighter",			"Frontier",			"Frost",			"Fury",
			]
		# G
		rank += [
			"Geist",			"Giant",			"Giant",		"Ghost",		"Gambler",		"Governor",		"Gazelle",			"Gale",			"Gargoyle",			"Gauntlet",			"Gambler",			"Genius",			"Gladiator",			"Goliath",			"Governor",			"Guide",			"Guardian",			"Gladiator",			"Gargoyle",			"Genius",			"Giant",			"Grandmaster",			"Ghost",			"Goat",			"Guard",			"Guide",			"Gorgon",			"Gale",			"Gambit",		"Gargoyle",		"Gaze",			"Gazelle",			"Gazer",		"Gem",			"General",			"Genius",			"Geomancer",			"Ghast",			"Ghost",			"Giant",			"Gladiator",			"Glow",			"Goat",			"Gold",			"Governor",			"Grace",			"Grandmaster",			"Grave",			"Gravewalker",			"Guard",			"Guardian",			"Guide",			"Gull",			"Gunslinger",	"Genius",		"Giant",
			 ]
		# H
		rank += [
			"Hunter",	"Horror",		"Hunter",			"Hunter",			"Hunter",			"Heart",			"Hero",			"Hunter",			"Hero",			"Hunter",			"Hunter",			"Hunter",			"Harvester",			"Horror",			"Herbalist",			"Horror",			"Horror",			"Hydra",			"Hand",			"Hand",			"Hag",			"Hawk",			"Heir",			"Hermit",			"Hero",			"Hive",			"Horror",	"Hound",		"Hunter",		"Hunger",			"Hyena",			"Hydra",			"Hood",			"Heart",			"Hag",			"Hand",			"Hangman",			"Harbinger",			"Harpy",			"Hauler",			"Haunt",			"Hawk",			"Head",			"Hole",						"Heart",			"Heir",			"Herald",			"Herbalist",			"Herder",			"Heretic",			"Hermit",	"Hero",		"Heron",	"Hex",			"Highlander",	"Highness",			"Historian",			"Hive",			"Hollow",			"Honor",			"Hoof",			"Hope",			"Horizon",			"Horn",			"Horror",			"Horse",			"Hound",			"Howl",			"Howler",			"Hunger",			"Hunter",			"Horror",			"Hussar",			"Hydra",			"Hyena",
			]
		# I
		rank += [
			"Inventor",				"Infiltrator",	"Invoker",		"Islander",			"Innovator",		"Islander",			"Invoker",			"Invader",			"Inquisitor",			"Impulse",			"Inkwork",			"Intellect",			"Illusionist",			"Inquisitor",			"Incubus",			"Intellect",			"Invoker",			"Illusionist",			"Immortal",			"Incubus",			"Infernal",			"Infernalist",			"Inferno",			"Inquisitor",			"Intellect",	"Intrigue",		"Investigator",		"Invoker",			"Ivy",
			]
		# J
		rank += [
			"Justiciar",	"Judge",	"Jackal",	"Jackal",			"Jaguar",						"Jaguar",			"Janissary",			"Juggler",			"Juggernaut",			"Jarl",			"Jasmine",			"Jay",			"Jinx",			"Journey",			"Judge",			"Juggernaut",			"Jumper",			"Jungle",			"Juniper",			"Jewel",			"Jackal",			"Jackal",
			]
		# K
		rank += [
			"Keeper",	"Kraken",	"Keeper",			"Kestrel",			"Khan",			"Killer",			"Kin",			"King",			"Kinsman",			"Kiss",			"Knife",			"Knight",			"Killer",			"Knight",			"Kraken",			"Killer",			"King",			"Keeper",			"Killer",			"King",			"Kiss",			"Knight",			"Knife",	"Keeper",
			]
		# L
		rank += [
			"Leader",	"Leviathan",		"Leader",			"Lion",				"Lorekeeper",			"Light",			"Leader",			"Leviathan",			"Leader",			"Lady",			"Lama",			"Lament",	"Lancer",			"Lark",			"Lasso",			"Laurel",			"Leader",			"Leap",			"Lecturer",			"Legacy",			"Legate",			"Legend",			"Legionnaire",			"Librarian",			"Lieutenant",			"Light",			"Lightbringer",		"Lightheart",		"Lily",			"Linguist",			"Lion",			"Lizard",			"Lord",			"Lost",			"Lotus",			"Lover",			"Loyal",			"Loyalty",			"Luminary",			"Lurk",			"Lycan",			"Lyncher",			"Lynx",			"Lord",			"Lotus",			"Leader",			"Lightning",			"Legend",			"Lover",			"Leader",			"Lion",				"Light",			"Lizard",			"Lover",			"Lasher",			"Leviathan",			"Lion",
			]
		# M
		rank += [
			"Menace",		"Merchant",			"Master",			"Moon",				"Mule",				"Moth",		"Mandril",			"Mistwalker",			"Monarch",			"Mask",			"Master",			"Manipulator",			"Machine",			"Master",			"Mystic",			"Manipulator",			"Mask",			"Master",			"Maestro",			"Mage",			"Magister",			"Magistrate",			"Magus",			"Maiden",			"Major",			"Malefic",		"Mage",				"Mantis",			"Mapper",			"Mare",				"Marigold",		"Mariner",			"Marshal",			"Martyr",			"Mask",			"Mason",			"Master",			"Mastermind",			"Mastiff",			"Matador",			"Matriarch",			"Mausoleum",			"Mayor",			"Melody",			"Mender",			"Mercenary",			"Merchant",							"Messenger",			"Mestizo",		"Miner",		"Might",			"Mastermind",		"Mindwarden",		"Minotaur",			"Minstrel",			"Mirage",			"Mist",			"Mogul",			"Monarch",			"Mongol",			"Monster",			"Moon",			"Moonmage",			"Morgue",			"Moth",			"Mountainlord",			"Mountaineer",			"Mourner",			"Mule",			"Muse",			"Musketeer",			"Mustang",			"Myst",			"Mystagogue",	"Mystic",			"Master",			"Master",			"Master",			"Master",			"Master",			"Marauder",			"Mandate",			"Monster",			"Mind",			"Martyr",			"Mage",			"Machine",			"Mutant",			"Moon",			"Mist",			"Mirror",			"Master",			"Man",			"Machine",			"Mage",			"Magister",			"Master",			"Mastermind",			"Mastiff",			"Martyr",			"Mind",				"Mist",				"Monster",			"Moon",				"Mule",				"Minotaur",			"Mystic",			"Manipulator",
			]
		# N
		rank += [
			"Nomad",			"Noble",		"Nightshade",		"Nexus",			"Nemesis",		"Nymph",	"Noble",	"Noble",					"Navigator",			"Necromancer",			"Necro",			"Necrologist",			"Necromancer",			"Nemesis",			"Nightingale",			"Nightmare",			"Nightveil",			"Ninja",			"Nocturnal",			"Nomad",			"Noose",			"Numerologist",			"Nun",			"Necromancer",		"Nightmare",	"Nomad",			"Necromancer",		"Nightmare",	"Nomad",	"Navigator",
			]
		# O
		rank += [
			"Oracle",		"Overseer",		"Oracle",		"Oracle",		"Oracle",		"Outlaw",		"Outlaw",	"One",	"Oni",		"Oracle",	"Otter",	"Outlander",	"Outrider",		"Outlaw",	"Overlord",	"Owl",	"Owlbear",	"Oblivion",			"Occultist",			"One",			"Oni",			"Oracle",			"Orchid",			"Outlander",			"Outlaw",			"Outrider",			"Overlord",			"Overseer",			"Owl",			"Owlbear",			"Overlord",		"Outlaw",		"Oni",			"Overlord",		"Otherworld",	"Owl",		"Oni",	"One",		"Oracle",	"Outlaw",		"Owl",
			]
		# P
		rank += [
			"Paradox",		"Peacekeeper",		"Pirate",		"Prophet",			"Painter",			"Pyrotechnic",			"Prowler",			"Prophet",			"Prince",			"Predator",			"Preceptor",		"Preacher",			"Praetorian",		"Pirate",			"Pilgrim",			"Pastor",			"Performer",			"Punisher",			"Progenitor",			"Praetor",			"Paladin",			"Pale",				"Panther",			"Pariah",			"Parrot",		"Pathfinder",		"Pathologist",			"Patriarch",		"Paw",			"Peasant",			"Pegasus",			"Pendulum",			"Peregrine",			"Pestilence",		"Petal",			"Phantom",			"Pharaoh",			"Philosopher",			"Phoenix",			"Pikeman",			"Pilgrim",			"Pilot",			"Pioneer",			"Piper",			"Piromaniac",			"Pistol",			"Pixie",			"Poem",			"Poet",			"Poltergeist",		"Praetor",			"Prefect",			"President",			"Pride",			"Prime",			"Primrose",			"Prince",					"Proconsul",			"Prodigy",			"Professional",			"Progenitor",			"Prophet",			"Prophetess",			"Prospector",			"Protege",			"Prowler",			"Prowlmaster",			"Psion",			"Puma",			"Punk",			"Pursuer",		"Plague",		"Power",			"Protector",			"Prophet",			"Paw",			"Power",			"Pathologist",		"Paw",			"Pegasus",			"Pixie",			"Pirate",			"Piromaniac",			"Poet",			"Prince",			"Prophet",			"Punk",				"Pyrotechnic",			"Predator",
			]
		# Q
		rank += [
			"Queen",		"Quail",			"Quake",			"Queen",
			]
		# R
		rank += [
			"Rider",		"Rider",			"Reader",			"Ruler",			"Radiance",			"Roar",			"Raider",		"Raider",			"Renegade",			"Rainstorm",			"Rainmaker",			"Rat",			"Runer",			"Runecarver",			"Ruler",			"Reverend",			"Regent",			"Reaper",			"Raven",									"Raptor",			"Rebel",			"Ruby",			"Rune",			"Rune",			"Ruby",			"Ranger",			"Rat",				"Raven",			"Reptile",			"Rider",			"Rose",			"Ruby",			"Rune",			"Rabbit",			"Radiance",			"Raider",			"Railroad",			"Rain",			"Raj",			"Rajput",			"Rancor",			"Ranger",			"Raptor",			"Rat",			"Rattlesnake",			"Raven",			"Reader",			"Rebellion",			"Reclaimer",			"Reed",			"Regent",			"Relicarian",		"Renegade",			"Representative",	"Reptile",			"Requiem",			"Researcher",			"Riddle",			"Rider",			"Risen",			"Ritualist",			"Rival",			"Riverlord",	"Rivermancer",			"Roar",			"Robber",			"Rogue",			"Ronin",			"Rose",			"Rowan",			"Ruby",			"Robot",			"Rue",			"Ruler",			"Rune",			"Runebearer",		"Runekeeper",		"Runemaker",		"Runes",			"Runewritter",			"Runner",			"Reaper",			"Rex",
			]
		# S
		rank += [
			"Shadow",			"Stalker",			"Scholar",			"Spirit",			"Spirit",			"Seeker",			"Spirit",			"Seeker",			"Sentinel",			"Seeker",			"Sheriff",				"Shaolin",				"Shadow",			"Seer",				"Spirit",			"Strategist",		"Stone",			"Sandwalker",		"Sandkeeper",		"Siren",			"Storyteller",		"Spark",			"Spirits", 			"Specter",				"Sparrow",			"Skywarden",		"Stag",				"Spirit",			"Strength",			"Sunstrider",		"Swordmaster",		"Saber",			"Sword",				"Spiritualist",			"Sparkweaver",		"Stoker",			"Seer",				"Seer",				"Sword",			"Sword",			"Sword",			"Swashbuckler",		"Storyteller",		"Statue",			"Stargazer",		"Spirit",			"Sphinx",				"Spellbinder",		"Speaker",			"Shepherd",			"Shapeshifter",		"Shaman",			"Serpent",			"Sentinel",				"Seer",					"Sectarian",			"Seafarer",			"Sculptor",			"Scorcher",			"Savage",			"Sage",				"Specter",			"Servant",			"Slayer",			"Saga",				"Sage",				"Sailor",			"Saint",			"Salamander",		"Sandkeeper",			"Savant",			"Sparrow",			"Speaker",			"Spear",			"Shadow",			"Specialist",		"Specter",				"Spectre",				"Spellblade",			"Spellbreaker",		"Spellshield",		"Spellsword",		"Spellweaver",		"Spelunker",		"Spider",			"Web",				"Spirit",			"Spiritualist",		"Spook",			"Spy",				"Squire",				"Stag",					"Stagecoach",			"Stampede",			"Star",				"Starblade",		"Starborn",			"Stardancer",		"Starforge",		"Shadow",				"Starshaper",			"Spy",			"Steward",			"Stingray",			"Stonetunnel",		"Storm",			"Stormcaller",		"Storyteller",		"Strategist",		"Strength",			"Strider",			"Successor",		"Sultan",			"Sun",					"Sunblessed",		"Sunlord",			"Sunscale",			"Sunstrider",		"Surgeon",			"Swan",				"Swarm",			"Swashbuckler",		"Sword",			"Swordmaster",			"Scale",			"Scar",			"Scholar",			"Scientist",		"Scion",			"Scorpion",			"Scout",			"Scribe",			"Secret",			"Secretary",		"Seeker",			"Seer",				"Sellsword",		"Senator",				"Sentinel",			"Sepulcher",		"Sergeant",			"Serpent",			"Serpentlord",		"Settler",			"Shade",			"Shadow",			"Shadowcrafter",	"Shadowmancer",			"Shadowseer",		"Shaman",			"Shaolin",			"Shaper",			"Shark",			"Shepherd",			"Sheriff",			"Shield",			"Shogun",			"Shooter",			"Shroud",			"Siege",			"Silence",			"Silver",			"Silverspeaker",	"Sire",				"Siren",			"Song",				"Skeleton",			"Skull",			"Skymaiden",		"Skyrider",			"Skyweaver",		"Slayer",				"Slinger",			"Smith",			"Smuggler",			"Snake",			"Soldier",			"Song",				"Songblade",		"Soul",				"Soulkeeper",		"Soulless",			"Sovereign",		"Seeker",			"Stalker",			"Sage",				"Sentinel",			"Seer",				"Shadow",			"Spirit",			"Shadow",			"Speaker",			"Spirit",			"Skull",			"Shadow",			"Sabertooth",			"Saurius",			"Salamander",		"Scientist",		"Scarecrow",		"Scorpion",			"Shadow",			"Shark",			"Shaman",			"Snake",			"Skeleton",			"Skull",			"Surgeon",			"Spirit",			"Spider",			"Specter",			"Spy",				"Swashbuckler",		"Sword",			"Sword",			"Sword",			"Shaman",			"Summoner",			"Stasis",			"Sharpshooter",			"Sentry",			"Serpent",			"Sun",				"Slayer",			"Spirit",
			]
		# T
		rank += [
			"Terror",		"Trickster",		"Tempest",			"Thunderbird",		"Tideturner",		"Tidecaller",		"Thunderbearer",		"Thunder",			"Timer",			"Thunderlord",			"Tempest",			"Templar",			"Templar",			"Tyrant",			"Traveler",			"Trailblazer",			"Tiger","Tiger",			"Terror",			"Trapper",			"Titan",			"Thief",			"Tormentor",			"Talon",			"Templar",		"Templar",			"Torturer",			"Trapper",			"Trailblazer",		"Torchbearer",			"Titan",			"Tiger",			"Traveler",			"Trickster",			"Timekeeper",			"Tyrant",			"Tactician",			"Terror",			"Tailor",			"Tale",			"Talon",			"Tamer",			"Technomancer",			"Telepath",			"Tempest",			"Templar",			"Tenacity",			"Terror",		"Taskmaster",	"Thane",			"Thaumaturge",		"Theorist",			"Thief",			"Thunder",			"Thunderbird",			"Tideturner",			"Tiger",			"Time Jumper",			"Titan",			"Tomb",			"Torchbearer",			"Torment",			"Tormented",			"Tormentor",			"Touched",			"Trader",			"Trapecist",			"Trapper",			"Traveler",			"Treasure",			"Treasures",			"Treebinder",		"Tribune",			"Tribute",			"Trick",			"Trickster",			"Troll",			 "Twilight",			"Tyrant",			"Terror",			"Tiger",			"Terror",			"Trapper",			"Trapecist",			"Troll",			"Thief",			"Trapper",			"Thunderer",			"Thrower",			"Titan",
			]
		# U
		rank += [
			"Umbra",
			]
		# V
		rank += [
			"Voice",		"Viking",	"Vision",		"Vizier",		"Vanguard",		"Vanguard",		"Voice",		"Voyager",		"Vulture",	"Vagabond",			"Void",			"Voidwalker",			"Vanquisher",			"Voice",			"Voice",			"Vagrant",			"Valkyrie",			"Valor",			"Vampire",			"Vanguard",			"Vendetta",			"Vengeance",			"Venom",			"Vicar",			"Viceroy",			"Vigilante",			"Viking",		"Violet",	"Viper",		"Virtuoso",		"Vision",		"Visionary",	"Vizier",	"Voice",			"Void",			"Voidseer",					"Voidwalker",			"Voyage",			"Voyager",			"Vulture",			"Vortex",			"Vigilante",			"Void",			"Voice",			"Void",			"Vampire",			"Vulture",
			]
		# W
		rank += [
			"Warlord",		"Whisperer",	"Wishmaker",	"Warden",		"Wishgranter",	"Wing",			"Wolf",				"Wishmaster",		"Wondrous",				"Wanderer",			"Wanderer",		"Witchhunter",		"Witchfinder",		"Windrider",		"Warden",			"Writter",			"Werewolf",			"Watcher",		"Watch",		"Warrior",		"Warlord",			"Wanderer",			"Wolf",				"Weaver",		"Walker",			"Wingsmith",			"Wyvern",		"Wolf",			"Witcher",		"Witch",		"Watcher",			"Warden",			"Warlord",				"Warrior",			"Watchman",		"Wild",				"Wand",				"Weaver",			"Weaver",			"Wielder",			"Wail",				"Wailmistress",		"Walker",		"Wanderer",		"War",			"Warcaller",		"Warcaster",		"Warchief",			"Ward",			"Warden",			"Wardmaster",			"Warforger",	"Warhawk",		"Warlord",		"Warmaster",	"Warmonger",		"Warrior",				"Watch",			"Watcher",		"Commander",		"Wayfarer",			"Weaver",			"Wendigo",			"Werewolf",			"Whale",			"Whimsy",			"Whirlwind",	"Whisper",		"Whisperer",		"Whitescale",		"Wielder",			"Wight",		"Wild",			"Will",			"Willow",			"Wind",			"Windcaller",		"Windrider",	"Wing",			"Wisdom",		"Witch",		"Witchdoctor",			"Witchhunter",		"Wolf",			"Wolfkin",			"Wrath",			"Wrath",			"Ward",				"Witchhunter",		"Wolf",				"Writter",			"Walker",		"Warlock",		"Warrior",			"Watch",			"Werewolf",			"Wizard",		"Writter",			"Willow",			"Wolf",						"Witch",        "Witch",		"Witcher",		"Wise",			"Watcher",
			]
		# Y
		rank += [
				"Yarrow",				"Yielder",
				]
		# Z
		rank += [
			"Zealous",	"Zealot",			"Zenithar",			"Zinnia",			"Zombie",			"Zombie",			"Zealot",			"Zephyr",
			]
	except:
		rank = ["Lord"]

	if FEMALE:
		rank += [
			"Matriarch",			"Mistress",
			]
	if MALE:
		rank += [
			"Gentleman",
			]
	# By Alignment
	if "Good" 	in genus:
		rank += [
			"Savior",		"Paragon",
			]
	if "Chaos" 	in genus:
		rank += [
			"Punk",			"Rebellion",
			]
	if "Lawful" in genus:
		rank +=[
		"Enforcer",
		]
	if "Evil" 	in genus:
		rank += [
			"Soulless",		"Monster",	"Nemesis",
			]
	# By Backgrounds
	if "Artist" 	in genus:
		rank += [
			"Artist",	"Visionary",	"Troubadour",		"Shadowcrafter",	"Piper",			"Illusionist",			"Trapecist",			"Technomancer",			"Alchemist",			"Artist","Artist","Artist",			"Flutist",			"Musician",
			]
		if FEMALE:
			rank += [
			"Enchantress",
			]
	if "Berserker"  in genus:
		rank += [
			"Sword",	"Shield",		"Chief",		"Prowler",		"Fanatic",		"Warrior",
			]
	if "Barbarian"  in genus:
		rank += [
			"Nomad",	"Shieldbearer",		"Chief",		"Warrior",		"Hunter",
			]
	if "Bard"		in genus:
		rank += [
			"Artist",	"Visionary",	"Troubadour",		"Troubadour",		"Troubadour",		"Silverspeaker",		"Mesmer",		"Drum",		"Musician",		"Harlequin",		"Flutist",		"Archivist",		"Trapecist",		"Clown",		"Mime",		"Troubadour",		"Illusionist",
			]
		if FEMALE:
			rank += [
			"Enchantress",
			]
	if "Bandit"		in genus:
		rank += [
			"Hunter",	"Phantom",	"Sword",	"Marauder",			"Bandit","Hunter",			"Archer",			"Warrior",			"Commander",
			]
	if "Charlatan"	in genus:
		rank += [
			"Healer",	"Visionary",	"Mesmer",	"Troubadour",		"Sirensong",		"Genius",		"Mystic",		"Fanatic",		"Archivist",		"Scammer",		"Illusionist",		"Alchemist",		"Arcanologist",
			]
	if "Cleric" 	in genus:
		rank += [
			"Healer",		"Vicar",		"Witchhunter",		"Soulforger",	"Soul",		"Inquisitor",		"Thaumaturge",			"Friar",			"Exarch",			"Fanatic",			"Archbishop",			"Acolyte",			"Oracle",			"Saint",			"Oracle",			"Priest",			"Abbot",			"Healer",			"Guide",			"Crusader",			"Acolyte",			"Prelate",			"Bishop",			"Conjurer",			"Minister",			"Mystic",		"Hierophant",	"Cleric",			"Abbot",
			]
		if FEMALE:
			rank += [
			"Abbess",
			]
	if "Commoner" 	in genus:
		rank += [
			"Hunter",	"Miller",	"Witchhunter",	"Speaker",		"Settler",	"Chosen",		"Elder",		"Farmer",		"Laborer",		"Citizen",		"Worker",		"Leader",		"Farmer",
			]
	if "Crafter" 	in genus:
		rank += [
			"Visionary",	"Chronoshifter",	"Alchemist", "Alchemist",	"Spellbreaker",		"Vintner",		"Artificer",		"Alchemist",		"Technomancer",		"Craftsman",		 "Creator",		 "Craftsman",		 "Genius",		 "Builder",		 "Maker",		 "Creator",		 "Conjurer",		 "Engineer",		 "Chemist",
			]
	if "Criminal" 	in genus:
		rank += [
			"Hunter",	"Phantom",	"Scourger",		"Thief",		"Assassin",		"Dealer",		"Swindler",		"Boss",
			]
	if "Cultist" 	in genus:
		rank += [
			"Visionary",	"Mesmer",	"Witchhunter",	"Unholyness",	"Exarch",		"Enchanter",		"Acolyte",		"Fanatic",		"Archivist",		"Archbishop",		"Arcanologist",		"Acolyte",		"Cultist", "Cultist","Cultist",		"Conjurer",		"Devotee",		"Follower",		"Fanatic",		"Fanatical",		"Friar",		"Keeper",		"Leader",		"Minister",		"Mystic",		"Oracle",		"Priest",		"Zealot",		"Mystic",		"Hierophant",		"Friar",		"Oracle",	"Priest",		"Abbot",		"Healer",		"Guide",		"Crusader",		"Acolyte",		"Prelate",		"Bishop",		"Conjurer",		"Minister",		"Mystic",		"Hierophant",		"Cleric",		"Priest",		"Priest",		"Priestess",		"Priestess'",		"Priest",		"Priest",		"High Priest",		"Archpriest",		"Abbot",
			]
		if FEMALE:
			rank += [
			"Abbess",			"Priestess",			"Priestess",			"Priestess",			"Priestess'",			"Priestess",			"Priestess",			"High Priestess",			"Archpriestess",
			]
	if "Druid" 		in genus:
		rank += [
			"Healer",	"Alchemist", "Alchemist",	"Windcaller",	"Elder",		"Elementalist",		"Sage",		"Dawnbringer",			"Druid",			"Shaman",			"Biomancer",			"Stormcaller",			"Archdruid",			"Warden",			"Master",			"Mystic",
			]
	if "Explorer" 	in genus:
		rank += [
			"Hunter",	"Visionary",	"Tracker",	"Chronoshifter",	"Sword",	"Witchhunter",	"Nomad",	"Navigator",	"Herald",		"Mountaineer",		"Messenger",			"Scout",			"Archer",			"Anthropologist",			"Leader",			"Ranger",			"Explorer",			"Wanderer",			"Adventurer",			"Pathfinder",			"Scout",			"Guide",			"Scout",
			]
	if "Expert" 	in genus:
		rank += [
			"Healer",		"Visionary",	"Guru",				"Chronoshifter",	"Alchemist", 		"Alchemist",	"Professor",	"Visionary",		"Genius",		"Mind",			"Minister",			"Technomancer",			"Astrologer",			"Astronomer",			"Artificer",		"Archivist",		"Anthropologist",		"Arcanologist",		"Alchemist",		"Arcanologist",		"Apothecary","Apothecary",		"Alchemist","Alchemist","Alchemist",		"Bombardier",		"Bomber",		"Collector",	"Consultant",		"Chemist",		"Etherscribe",	"Grandmaster",		"Alchemist",		"Genius",		"Geneticist",		"Engineer",		"Master",		"Pathologist",		"Scientist",			"Surgeon",
			]
	if "Fighter"	in genus:
		rank += [
			"Hunter",	"Blade", "Sword",	"Witchhunter",	"Vigilante",		"Commander",			"Warlord","Warrior",			"Commander","Warlord",			"Samurai","Samurai",			"Archer",			"Warrior",
			]
	if "Guardian" 	in genus:
		rank += [
			"Guardian",		"Guardian",		"Guardian",		"Guardian",		"Hunter",		"Keeper",		"Steward",			"Protector",		"Protector",	"Guardian",		"Sword",		"Vigilante",	"Sandkeeper",	"Sentinel",			"Sentinel",			"Commander",		"Overseer",			"Steward",		"Marshal",			"Guardian",			"Keeper",		"Guardian",		"Enforcer",		"Enforcer",		"Enforcer",		"Archer",		"Samurai",		"Samurai",		"Guard",		"Guardian",		"Keeper",	"Sentinel",		"Vigilant",		"Knight",		"Guard",		"Guard",		"Guard",			"Guard",			"Sentinel",			"Sentinel",		"Sentinel",		"Sentinel",		"Sentinel",		"Sentinel",		"Keeper", 		"Keeper",		"Custodian",	"Custodian",		"Custodian",		"Custodian",		"Custodian",		"Custodian",	"Guardian",		"Guardian",			"Guardian",			"Guard",		"Defender",		"Guardian",		"Guardian",		"Guardian",		"Guardian",		"Guardian",		"Guardian",		"Defender"		"Protector",		"Protector",		"Protector",		"Protector",	"Warden",		"Watcher",		"Watcher",		"Guardian",		"Guardian",		"Guard",		"Defender",		"Protector",		"Protector",		"Protector",		"Scarecrow",		"Sentinel",		"Keeper",		"Shield",			"Watcher",			"Sharpshooter",		"Watchdog",
			]
	if "Hero"		in genus:
		rank += [
			"Troubadour",		"Guardian",		"Sword",	"Vigilante",	"Samurai",			"Leader",			"Warrior",			"Champion",			"Enforcer",			"Archer",			"Hero",			"Conqueror",			"Hero",       "Saviour","Warrior","Defender","Knight",			"Protector",			"Samurai","Samurai",
			]
	if "Hunter" 	in genus:
		rank += [
			"Hunter",	"Hunter",	"Hunter",	"Hunter",	"Hunter",	"Hunter",	"Hunter",	"Hunter",	"Hunter",	"Hunter",	"Tracker",	"Witchhunter",	"Viper",		"Archer",		"Hunter",			"Hunter",			"Scout",			"Hunter","Hunter","Hunter","Hunter","Hunter","Hunter",			"Hunter","Hunter","Hunter","Hunter","Hunter","Hunter",			"Hound",			"Tracker",			"Hunter",			"Archer",			"Trapper",			"Stalker",			"Ranger",
			]
	if "Healer"		in genus:
		rank += [
		"Healer",	"Vicar",	"Alchemist", "Alchemist",	"Shaman",	"Heart",		"Mystic",		"Blossom",		"Alchemist","Healer","Physician","Herbalist","Medic",
		]
	if "Knight" 	in genus:
		rank = [
		"Sword",	"Sable",	"Samurai",		"Enforcer",	"Squire",	"Squire",	"Warrior",	"Champion",		"Knight",	"Knight",	"Knight",	"Knight",	"Knight","Knight","Knight",			"Samurai","Samurai",			"Champion",			"Defender",			"Warrior",			"Cavalier",			"Standard",			"Standard",			"Standard Bearer",			"Standard Bearer",
		]
	if "Mage"		in genus:
		rank += [
			"Mesmer",	"Chronoshifter",	"Etherscribe",	"Spellwover",	"Alchemist", "Alchemist",	"Elder",	"Spellbinder",		"Telepath",		"Mystic",		"Archivist",		"Mage",		"Arcanologist",		"Technomancer",		"Magus",		"Forcemage",		"Battlemage",
			]
		if FEMALE:
			rank += [
			"Enchantress",
			]
	if "Monk" 		in genus:
		rank += [
			"Vicar",	"Visionary",	"Windcaller",	"Ninja",	"Elder",		"Monk",		"Warrior",		"Exarch",			"Friar",			"Fanatic",			"Archivist",			"Acolyte",			"Monk","Monk","Monk","Monk","Monk","Monk",			"Monk",			"Mystic",			"Blossom",			"Friar",			"Monk",			"Master",			"Guide",			"Sage",			"Practitioner",			"Philosopher",			"Abbot",
			]
		if FEMALE:
			rank += [
			"Abbess",
			]
	if "Merchant" 	in genus:
		rank += [
			"Alchemist", "Alchemist",	"Nomad",	"Navigator",	"Librarian",		"Alchemist",			 "Merchant",			 "Archivist",			 "Trader",			 "Negotiator",			 "Dealer",			 "Merchant",
			]
	if "Mentor"		in genus:
		rank += [
			"Maestro",		"Archivist",		"Commander",
			]
	if "Noble" 		in genus:
		rank += [
			"Sovereign",	"Monarch",		"Duke",		"Exarch",			"Ruler",			"Sovereign",		"Monarch",							"Major",		"Senator",		"Archduke",		"Archon",		"Chieftain",	"Chieftain",	"Chief",	"Chief",	"Consul",	"Cesar",	"Daimyo",	"Dictator",			"Diplomat",			"Earl",			"Emperor",			"Highness",			"Khan",			"Leader","Leader","Leader",			"Monarch","Monarch",			"Marquis",		"Primus",		"Princeps",		"Regent",	"Sultan", 			"Sultan",	"Sovereign",		"Sovereign",	"Sovereign",	"Sovereign",	"Sovereign",	"Sultan",		"Noble",		"Noble",		"Noble",		"Noble",
			]
		if "Fiend" in genus:
			rank += [
				"Archfiend",
				]
		if "Orc" in genus:
			rank += [
			"Khan",	"Khan",	"Khan",	"Khan",	"Khan",	"Khan",	"Khan",	"Khan",	"Khan",
			]
		if MALE:
			rank += [
			"Baron", "Lord",	"Overlord",	"Master",	"Emperor",	"Prince",	"King",	"King",	"Baron",	"Baron",	"Baron",	"Count",	"Duke",		"Emir",	"Emperor",	"Emperor",	"Lord",	"Lord", "Lord","Lord","Lord",				"King","King","King","King","King",				"Highlord",				"Prince",				"Viscount",				"Warlord",
			]
		if FEMALE:
			rank += [
			"Queen",	"Princess","Princess","Princess",	"Baroness", "Queen",	"Lady",	"Overlady",	"Queen",	"Archduchess",			"Baroness",			"Duchess",			"Empress","Empress",			"Highlady",			"Lady","Lady","Lady",			"Princess",			"Queen","Queen","Queen","Queen","Queen",			"Viscountess",			"Warlady",
			]
	if "Ninja"		in genus:
		rank += [
			"Phantom",	"Ninja",	"Ninja",	"Monk",		"Warrior",		"Archer",		"Ninja", "Hokage",		"Shadow",
			]
	if "Priest" 	in genus:
		rank += [
			"Healer",	"Vicar",	"Pope",		"Exarch",		"Acolyte",		"Fanatic",		"Archivist",			"Friar",			"Bishop",			"Deacon",			"Chaplain",			"Minister",			"Mystic",			"Hierophant",			"Pilgrim",			"Abbot",
			]
		if FEMALE:
			rank += [
				"Nun",			"Abbess",			"Archduchess",			"Priestess",				"Priestess",				"Priestess",
				]
	if "Paladin"	in genus:
		rank += [
			"Healer",	"Exarch",			"Sword",	"Witchhunter",	"Noble",		"Exarch",		"Warrior",		"Acolyte",		"Champion",		"Knight",		"Enforcer",			"Paladin",			"Warlord",			"Samurai","Samurai",
			]
	if "Pirate" 	in genus:
		rank += [
			"Hunter",	"Sword",	"Navigator",		"Commander",			"Pirate",			 "Captain",			 "Buccaneer",			 "Raider",			 "Corsair","Corsair",			 "Marauder",	"Sea Dog"
			]
	if "Rogue"		in genus:
		rank += [
			"Phantom",	"Tracker",	"Ninja",		"Agent",		"Archer",		"Rogue",		"Poisoner",		"Thief",		"Illusionist",
			]
	if "Ranger" 	in genus:
		rank += [
			"Hunter",	"Hunter",	"Hunter",	"Ranger",	"Ranger",	"Tracker",		"Nomad",			"Ranger",			"Archer",			"Sharpshooter",			"Scout",			"Tracker",			"Expert",			"Outlander",			"Warden",
			]
	if "Scholar"	in genus:
		rank += [
			"Visionary",	"Troubadour",		"Professor",	"Scholar",		"Acolyte",		"Auralist",		"Archivist", "Archivist",		"Arcanologist",		"Anthropologist",		"Alchemist",		"Mystic",		"Technomancer",		"Professor",		"Magus",		"Illusionist",		"Researcher",		"Arcanologist",		"Alchemist",		"Professor",		"Arcanist",		"Historian",		"Philosopher",		"Sage",		"Hierophant",
			]
	if "Shaman"		in genus:
		rank += [
			"Healer",	"Spellwover",	"Shaman",		"Mystic",		"Druid",    "Oracle",		"Leader","Healer",		"Guide","Sage",		"Keeper",		"Shaman",		"Shaman",		"Hierophant",		"Blossom",
			]
	if "Soldier" 	in genus:
		rank += [
			"Hunter",	"Sword",	"Sergeant",		"Commander",		"Warrior",		"Archer",		"Enforcer",			"Captain",			"General",			"Leader",			"Warlord",			"Commander",			"Gladiator",			"Warrior",			"Samurai","Samurai",
			]
	if "Sorcerer" 	in genus:
		rank += [
			"Visionary",	"Mesmer",	"Chronoshifter",	"Spellwover",	"Sorcerer",	"Windcaller",	"Sorcerer",			"Sage",			"Mystic",			"Sorcerer",			"Magus",			"Illusionist",
			]
		if FEMALE:
			rank += [
				"Enchantress",			"Enchantress",			"Enchantress",			"Enchantress",
				]
	if "Spy" 		in genus:
		rank += [
			"Hunter",	"Tracker",	"Witchhunter",	"Ninja",			"Agent",			"Operative",			"Spy",
			]
	if "Trickster"	in genus:
		rank += [
		"Mesmer",	"Troubadour",			"Chronoshifter",	"Shadowspinner",		"Arcanologist",		"Minstrel",		"Mist",
			]
	if "Traveler" 	in genus:
		rank += [
			"Hunter",	"Visionary",	"Tracker",	"Troubadour",			"Walker",	"Wayfarer",	"Witchhunter",	"Nomad",	"Navigator",	"Seeker",			"Messenger",			"Hunter",			"Anthropologist",			"Trapecist",			'Traveler',			"Traveler",
			]
	if "Warrior"	in genus:
		rank += [
			"Sword",	"Sergeant",	"Sellsword",	"Slinger",		"General",		"Commander",		"Warrior",		"Pikemen",		"Champion",		"Warrior",		"General",		"Archer",		"Samurai","Samurai",
			]
	if "Warlock"	in genus:
		rank += [
			"Mesmer",	"Spellwover",	"Alchemist", "Alchemist",		"Spellsword",	"Spectre",		"Infernalist",		"Ocultist",		"Fanatic",		"Archivist",		"Taromancer",		"Tarot reader",		"Arcanologist",		"Arcanologist",			"Sage",			"Alchemist",			"Mystic",			"Hex",		"Magus",
			]
		if FEMALE:
			rank += [
				"Enchantress",
				]
	if "Wizard"    	in genus:
		if FEMALE:
			rank += [
				"Enchantress",
				]
		rank += [
			"Visionary",			"Mesmer",				"Auramancer",			"Archivist",			"Arcanologist",			"Alchemist",			"Astromancer",			"Aetheromancer",		"Arcanomancer",			"Cryptomancer",			"Cardiomancer",			"Cardmancer",			"Cosmomancer",			"Chronoshifter",		"Eclipsomancer",		"Etherscribe",			"Spellwover",			"Alchemist", 			"Alchemist",			"Writter",				"Seer",					"Elementalist",			"Magician",				"Wizard",				"Wizard",				"Magus",			"Chronomancer",			"Draconomancer",		"Mystic",				"Crystalmancer",		"Shadowmancer",			"Stellomancer",			"Heliomancer",			"Selenomancer",			"Aquamancer",			"Necromancer",			"Pyromancer",			"Aeromancer",			"Geomancer",			"Gaiamancer",			"Uranomancer",			"Electromancer",		"Psychomancer",			"Lithomancer",			"Sage",					"Thermomancer",			"Technomancer",			"Lunamancer",			"Venomancer",			"Cryomancer",			"Oniromancer",			"Morpheomancer",		"Venusmancer",			"Logomancer",			"Numeromancer",			"Osteomancer",			"Spectromancer",		"Noctimancer",			"Celestimancer",			"Galaxiomancer",			"Abyssomancer",			"Infernomancer",		"Tempestomancer",		"Gravitomancer",		"Harmonimancer",		"Illusiomancer",		"Juramancer",			"Kosmomancer",			"Lumimancer",			"Lumomancer",			"Luximancer",			"Luxomancer",			"Nihilomancer",			"Omnimancer",			"Sanguimancer",			"Ghoulmancer",			"Vampiromancer",			"Magus",			"Titanomancer",			"Oracle",			"Illusionist",
			]
	if "Witch"		in genus:
		rank += [
			"Healer",	"Mesmer",	"Stormcaller",	"Raincaller",	"Firecaller",	"Spellwover",	"Alchemist",	"Windcaller",		"Shaman",	"Witch",
			]

	# By races (And then subraces)
	if "Aven" 		in genus:
		rank += [
			"Thunderbird",			"Firebird",			"Windbird",			"Seabird",			"Stormbird",			"Sandbird",			"Sunbird",			"Moonbird",			"Thunderlord",			"Aven",			"Celestial",			"Aven",		"Peacock",			"Skywing",			"Wing",			"Wing",			"Wing",
			]
		if "Owlin" in genus:
			rank += [
				"Seer",				"Sage",
				"Watcher",
				"Keeper",
				"Whisperer",
				]
		if "Tengu" in genus:
			rank += [
			"Raven",
			"Master",
			"Keeper",
			"Trickster",
			]
		if "Raptoran" in genus:
			rank += [
			 "Raptoran",
			 ]
		if "Aarakocra" in genus:
			rank += [
				"Wind",
				"Aarakocra"
				]
		if "Birdfolk" in genus:
			rank += [
			"Bird",

			"Keeper",
			"Songweaver",
			"Scout",
			"Elder"]
	if "Aberration"	in genus:
		rank += [
			"Aberration",	"Deathclaw",
			]
		if "Beholder"	in genus:
			rank +[
				"Beholder",				"Eye",				"Watcher",
				]
		if "Githzerai" in genus:
			rank += [
				 "Guide",
				 "Mindhunter"
				 ]
		if "Githyanki" in genus:
			rank += [
				"Githyanki",
				]
		if "Destiny Devouers" in genus:
			rank += [
				"Traveler","Hierophant",
				"Ravager",
				"Thief",
				"Alterer",
				"Eater",
				"Predator",
				"Bender",
				"Usurper",
				"Devourer"]
		if "Parasyte" in genus:
			rank += [
				"Leech","Parasyte",
				 "Dominator",
				 "Invader",
				 "Master",]
		if "Symbioid" in genus:
			rank += [
				"Communion",
				"Union",
				"Symbiote",
				"Symbioid",
				]
		if "Alien Spawn" in genus:
			rank += [
			"Star",
			"Invader",
			"Parasite",
			"Entity",
			"Horror",
			]
		if "Chaos Warper" in genus:
			rank += [
				  "Giant",
				  "Sovereign",
				  "Colossus",
				  "Dominator",
				  "Titan",
				  ]
		if "Dominators" in genus:
			rank += [
			"Slaver",
			 "Master",
			 "Lord",
			 "Dominator",
			 "Subjugator",
			 "Enforcer"]
		if "Living Spell" in genus:
				rank += [
					"Spell",
					"Entity",
					"Aberration",
					"Devourer",
					"Curse",
					]
	if "Beast" 		in genus:
		if "Beastfolk"	in genus:
			rank += [
				"Satyr",
				]
		rank +=[
		 "Howler",
		"Apex",
			]
		if "Kitsune"	in genus:
			rank += [
				"Fox",	"Fox",	"Fox",	"Fox",	"Fox",
				]
		if "Monkey" 	in genus:
				rank += [
				"Monkey",
				"Master",
				"Baboon",
				]
		if "Armored Bear" 	in genus:
			rank += [
					"Bruin",
					"Guardian",
					"Ursus",
					"Bear"]
		if "Kong" 			in genus:
			rank += [
				"Kong",
				"Baboon",
				"Colossus",
				"Titan",
				"Ape",
				"Silverback",
				"Orangutan",
				]
		if "Giant Eagle" 	in genus:
			rank += [
			  "Eagle",
			  "Giant",
			  ]
		if "Tiger" 			in genus:
			rank += [
				"Sabertooth",
				"Tiger",
				"Sovereign",
				"Stalker",
				"Predator",
				"Striker"
				]
		if "Vulture" 		in genus:
			rank += [
			"Wing",
			"Spirit",
			"Vulture",
			"Sky",
			"Scavenger",
			"Vision",
			"Predator"]
		if "Deer" 			in genus:
			rank += [
			"Stag",
			"Deer",
			]
		if "Owl"			in genus:
			rank += [
			"Owl",
			 "Seer",
			]
		if "Kaiju" 			in genus:
			rank += [
			"Kaiju",
			"Behemoth",
			"Dinosaur",
			"Gigantosaurus",
			"Dinosaur",
			]
		if "Sun Scarab" 	in genus:
			rank += [
				"Scarab",
				"Pharaoh",
				"Beetle",
				"Sun"
				]
	if "Catfolk"	in genus:
		rank = [
			"Mane",
			"Sabertooth",
			"Leopard",
			"Lion",
			]
	if "Celestial" 	in genus:
		rank += [
			"Angel",	"Emissary",			"Kami",			"Guardian",			"Guide",			"Herald",			"Light",			"Messenger",			"Oracle",			"Celestial",			"Celestian",			"Minister",			"Muse",
			]
		if "Archangel"	in genus:
			rank += [
			"Archangel",			"Archangel",			"Archangel",			"Archangel",			"Archangel",
			]
	if "Construct"	in genus:
		rank += [
		"Droid",		"Scarecrow",		"Robot",		"Slave",		"Drone",		"Automaton",		"Engine",		"Clockdroid",		"Statue",		"Drone",		"Golem",		"Golem",		"Golem",		"Golem",		"Sentry",
				]
	if "Dwarf"		in genus:
		rank += [
			"Beard",
			]
	if "Dragon"		in genus:
		rank += [
			"Wyrm",	"Hatchling",
			]
		if "Noble" in genus:
			rank += [
			"Dragonlord",
			"Elder",
			]
	if "Elemental"	in genus:
		rank += [
			"Elemental",
			"Elemental",
			"Genie",
			]
		if "Genasi" in genus:
			rank +=[
			"Genasi",
			]
	if "Fiend"		in genus:
		rank += [
		"Fiend",	"Hellknight",		"Sucubus",		"Sucubus",		"Baboon",		"Firefiend",
		]
	if "Fey"		in genus:
		rank += [
		"Sprite",	"Sprite", "Duende", "Duende", "Duende",
		]
	if "Giant"		in genus:
		rank += [
			"Titan",	"Giant",		"Colossus",			"Titan",
			]
		if "Goliath"		in genus:
			rank += [
					"Golem",
					]
	if "Goblin"		in genus:
		rank += [
		"Duende",	"Duende",	"Duende",	"Goblin",		"Baboon",		"Gnawer",		"Raider",		"Akki",
		]
		if "Redcap" in genus:
			rank += [
			"Raider", "Goatraider",			"Redcap",
			]
	if "Human"		in genus:
		rank += [
				"Golem",
				]
		if MALE:
			rank += [
				"Man", "Man", "Wer",
				]
		if FEMALE:
			rank += [
				"Woman", "Woman", "Wif",
				]
	if "Kobold"		in genus:
		rank += [
		"Kobold",
		]
	if "Lizardfolk" in genus:
		rank += [
			"Dinosaur", "Saurius",							"Lizard",
			]
		if "Turtle"	in genus:
			rank += [
			"Turtle",	"Turtle",			"Shield",
			]
	if "Monstrosity" 	in genus:
		if "Shapeshifter" in genus:
			rank += [
				"Sasquatch",			"Mimic",			"Double",			"Monster", "Monster", "Monster",
				]
	if "Ooze" in genus:
		rank += [
		"Blob", "Blob",
			]
	if "Plant" 		in genus:
		rank += [
			"Oak",	"Maple",	"Flora",
			]
	if "Undead"		in genus:
		rank += [
			"Ghost",	"Apparition",	"Wraith",			"Wraith",	"Phantom",	"Wraith",	"Mourner",		"Ghost","Ghost","Ghast","Ghost",		"Revenant","Revenant","Revenant",			"Cadaver", "Cadaver",			"Hellhound",			"Skelleton",			"Visit",			"Visitor",			"Soul",			"Phantom",			"Ghoul",			"Ghoulcaller",			"Carnophage",			"Cannibal",			"Hemophage",			"Mummy","Mummy","Mummy","Mummy",
			]
	if "Vampire" 	in genus:
		rank += [
		"Bloodlord",
		"Vampire",
		"Vampyr",
		"Vampyre",
		"Strigoi",
		]
	if "Snakefolk"  in genus:
		rank += [
			"Snake", "Naga",
			]
		if "Gorgonian" in genus:
			rank += [
				"Gorgon",
				"Gorgona",
				]
	# By subrace
	if ("Deer" 	in genus) or ("Stag"	in	genus):
		rank += [
		"Antler",
		]
	if "Soldier" 	in genus:
		rank += [
			"Commander","Sergeant","Warrior","General","Soldier",]
	if "Rogue" 		in genus:
		rank += [
		  "Thief","Assassin","Scout","Spy","Trickster",]
	if "Rakshasa" 	in genus:
		rank += [
			"Sabertooth",   "Fiend",    "Deceiver", "Trickster",    "Rakshasa",
			"Demon",        ]
	if "Kenku" 	in genus:
		rank += [
		"Crow",
		"Mimic",
		"Shadow",
		"Raven",
		"Spy",
		]
	if "Wyrm" in genus:
		rank += [
			"Serpent",
			"Wyrm",
			"Worm",
			]
	if "Mage" in genus:
		rank += [
			"Arcanologist",		  "Alchemist",		  "Arcanist",		  "Magician",		  "Oracle",		  "Scholar",		  "Sorcerer",		  "Spellbinder",		  "Wizard", "Wizard",		  "Hierophant",		  "Sorcerer",
			]
	if "Traveler" in genus:
		rank += [
			"Nomad",			"Explorer",			"Wanderer",		"Traveler",
			]
	if "Trickster" in genus:
		rank += [
			"Scamp",			"Survivor",
			]
	if "Warrior" in genus:
		rank += [
			"Fighter",		  "Warlord",		  "Warrior",		 "Champion",		 "Duelist",		 "Gladiator",
			]
	if "Warlock" in genus:
		rank += [
			"Arcanologist",		"Wizard",			"Advisor",			"Caster",			"Conjurer",			"Maker",			"Occultist",			"Oracle",			"Priest",			"Scholar",			"Warlock","Warlock","Warlock",			"Hierophant",		"Sorcerer",
			]
	if "Witch" in genus:
		rank += [
			"Caster",			"Crone",			"Herbalist",			"Sorceress",			"Witch","Witch",
			]
	if "Aberration" in genus:
		rank += [
			"Abomination",			"Abyss",			"Born",			"Breaker",			"Controller",			"Devourer",			"Distorter",			"Dominator",			"Dreamer",			"Eater",			"Enforcer",			"Gazer",			"Harbinger",			"Horror",			"Manipulator",	"Netherbrain",			"Nethermind",			"Oblivion",			"Overseer",			"Ravager",			"Speaker",			"Stealer",			"Void",			"Voidshaper",			"Warden",			"Warp",			"Warper",			"Whisperer",
			]
	if "Priest" in genus:
		rank += [
			"Acolyte",			"Cleric",			"High Priest",			"Keeper",			"Preacher",			"Priest",			"Priestess",			"Cardinal",			"Hierophant",
			]
	if "Plant" in genus:
		rank += [
		  "Tree",		  "Plant","Plant",	"Blossom",
		  ]
	if "Dragon" in genus:
		rank += [
			"Breath",	"Calm",		  "Champion",		  "Dominator",		  "Drake",		  "Fang",		  "Fang",		  "Fire",		  "Firebreather",		  "Firebreather",		  "Fury",		  "Fury",		  "Hunter",		  "Keeper",		  "Lord",		  "Mind",		  "Moon",		  "One",		  "One",		  "Rex",		  "Ruler",		  "Scale",		  "Seeker",		  "Shadow",		  "Sovereign",		  "Sovereign",		  "Star",		  "Sun",		  "Terror",	"Wing",
				 ]
	if "Illithid" in genus:
		rank += [
			"Astral",		"Brain",		"Brain",		"Brainkeeper",		"Brainmaster",		"Cerebral",		"Cerebromancer",		"Commander",		"Conjurer",		"Controller",		"Cortex",		"Deep",		"Dominator",		"Dominator",		"Eater",		"Elder",		"Emissary",		"Encephalarch",		"Flayer",		"Flayer",		"Gloom",		"Illithid",		"Lurker",		"Master",		"Master",		"Mind",		"Mind",		"Mind",		"Mind",		"Mind",		"Mind",		"Mind",		"Mind",		"Mindking",		"Mindlord",		"Mindqueen",		"Mindspeaker",		"Neurocaptain",		"Oracle",		"Orb",		"Prophet",		"Psychic",		"Psychic",		"Psychic",		"Seer",		"Sovereign",		"Sovereign",		"Strider",		"Synapse",		"Tentacle",		"Thought",		"Thought",		"Tyrant",		"Void",		"Warpweaver",
			]
	if "Beholder" in genus:
		rank += [
		"Beholder",		"Eye",	"Gaze",		"Lord",		"Lord",		"Master",		"Oracle",		"Orb",		"Overseer",		"Pasha",		"Ruler",		"Sovereign",		"Sovereign",		"Sphere",		"Tyrant",		"Tyrant",		"Watcher",
		]
	if "Shapeshifters" in genus:
		rank += [
			"Formless",		  "Shapechanger",		  "Shifter",
			]
	if "Old One" in genus:
		rank += [
			"Elder Entity",	 "Cosmic Sage", "Star Spawn", "Void Seer", "Ancient Horror",
			]
	if "Mindlinker" in genus:
		rank += [
			"Conductor",			"Connector",			"Linker",
			]
	if "Snake" in genus:
		rank += [
			"Cobra",
			]
	if "Hunter" in genus:
		rank += [
			"Hunter",
			]
	if "Catfolk" in genus:
		rank += [
				"Cat",				"Grace",				"Hunter",				"Lord",				"Master",				"Sabertooth",				"Sage",				"Seer",				"Paw",				"Fang",				"Mane",
				]
	if "Undead" in genus:
		rank += [
				"Necron",				"Reaper",				"Lich","Lich",
				]
	if  "Mage"  in genus:
		rank += [
			"Mage"			"Archmage",			"Mage",			"Hierophant",
			]
	if "Bard" 	in genus:
		rank += [
			"Bard",		"Jester",			"Flutist",			"Fiddler",			"Poet",			"Bard",
			]
	if "Berserker" in genus:
		rank += [
			"Berserker",    ]
	if "Druid" 	in genus:
		rank += [
			"Druid",
			]
	if "Sorcerer" in genus:
		rank += [
			"Sorcerer",	"Sorcerer",	"Sorcerer","Sorcerer",
			]
	if "Archfey" in genus:
		rank += [
			"Archfey",
				]
	if "Merfolk" in genus:
		rank += [
			"Merfolk", "Siren", "Triton",
			]

	try:
		rank += [
			f"{lusor.archetype}",	f"{lusor.archetype}",	f"{lusor.archetype}",	f"{lusor.archetype}",	f"{lusor.archetype}",	f"{lusor.archetype}",	f"{lusor.archetype}",	f"{lusor.archetype}",	f"{lusor.archetype}",	f"{lusor.archetype}",
			f"{lusor.race}",		f"{lusor.race}",		f"{lusor.race}",		f"{lusor.race}",		f"{lusor.race}",		f"{lusor.race}",		f"{lusor.race}",		f"{lusor.race}",		f"{lusor.race}",		f"{lusor.race}",
			f"{lusor.subrace}",		f"{lusor.subrace}",		f"{lusor.subrace}",		f"{lusor.subrace}",		f"{lusor.subrace}",		f"{lusor.subrace}",		f"{lusor.subrace}",		f"{lusor.subrace}",		f"{lusor.subrace}",		f"{lusor.subrace}",	f"{lusor.subrace}",	f"{lusor.subrace}",
			]
	except:
		try:
			rank += [
				f"{lusor.species}",	f"{lusor.species}",	f"{lusor.species}",	f"{lusor.species}",	f"{lusor.species}",	f"{lusor.species}",	f"{lusor.species}",	f"{lusor.species}",	f"{lusor.species}",	f"{lusor.species}",
				f"{lusor.char_class}",		f"{lusor.char_class}",		f"{lusor.char_class}",		f"{lusor.char_class}",		f"{lusor.char_class}",		f"{lusor.char_class}",		f"{lusor.char_class}",		f"{lusor.char_class}",		f"{lusor.char_class}",		f"{lusor.char_class}",
				f"{lusor.subclass}",		f"{lusor.subclass}",		f"{lusor.subclass}",		f"{lusor.subclass}",		f"{lusor.subclass}",		f"{lusor.subclass}",		f"{lusor.subclass}",		f"{lusor.subclass}",		f"{lusor.subclass}",		f"{lusor.subclass}",	f"{lusor.subclass}",	f"{lusor.subclass}",
				f"{lusor.background}",		f"{lusor.background}",		f"{lusor.background}",		f"{lusor.background}",		f"{lusor.background}",		f"{lusor.background}",		f"{lusor.background}",		f"{lusor.background}",		f"{lusor.background}",		f"{lusor.background}",	f"{lusor.background}",	f"{lusor.background}",
				]
		except:
			pass


	return random.choice(rank)

def Origin(lusor):
	'''
	If you can say: The Dark Lord of X
	X goes here
	'''
	genus = Genus(lusor)
	origin = []
	# of
	# from
	# {Rank(lusor)}
	# {Descriptor(lusor)}
	origin += [
	"of the Ouroboros",
	f"of the {Descriptor(lusor)} Master",

	f"of the {Descriptor(lusor)} Wars",
	f"of the {Descriptor(lusor)} War",
	f"of the {Rank(lusor)} Wars",
	f"of the {Rank(lusor)} War",

	"of the Wars",
	"of the War",
	"of the Damned",
	"of the Moon",
	"from the Moon",
	"of the Jungle",
	"from the Jungle",
	f"of the {Descriptor(lusor)} Shadows",
	"of Orisha",
	"of Osiris",
	"of Jade",
	"of Justice",
	f"from the {Descriptor(lusor)} Island",
	f"of the {Descriptor(lusor)} Island",
	"from the Island",
	"of the Island",
	"of the Hive"
	"of the Hill",
	"from the Hill",
	"of the Heath",
	"of the Harbor",
	"of the Hamlet",
	"of the Geyser",
	"of the Garden",
	"of the Gulf",
	"of Merlin",
	"of the Griffon",
	"of Cthulhu",
	"of the Jackal",
	"of the Banshee",
	"of Pirates",
	"of Odin",
	"from the Hill",
	"of the Nymph",
	"from Nature",
	"of the Wizard",
	"of Nature",
	"of Light",
	"of Nature",
	"from Nature",
	"of Adventures",
	"of Nature",
	"of the Circle",
	"of Zombies",
	"of Warriors",
	"of Warlords",
	"of Vecna",
	"of Werevolves",
	"of the Valkyrie",
	"of the Universe",
	"of Trolls",
	"of the Sorcerer",
	"of the Totem",
	"of the Shepherd",
	"of the Shaman",
	"of Shamans",
	f"of the {Descriptor(lusor)} Shaman",
	"of the Serpent",
	f"of the {Descriptor(lusor)} Serpent",
	"of Serpents",
		"of the Scholar",
		"of Scholars",
		f"of the {Descriptor(lusor)} Scholar",
		f"of the {Descriptor(lusor)} River",
		"of the River",
		"of the Queen",
		f"of the {Descriptor(lusor)} Queen",
		"of the Prince",
		f"of the {Descriptor(lusor)} Prince",
		"of the Pirate",
		"of Pirates",
		f"of the {Descriptor(lusor)} Pirates",
		"of the Minotaur",
		"of the Oracle",
		"of Odin",
		f"of the {Descriptor(lusor)} Meadow",
		"of the Meadow",
		f"of the {Descriptor(lusor)} Mage",
		"of the Mage",
		"of Mages",
		"of the Master",
		f"of the {Descriptor(lusor)} Master",
		f"of the {Descriptor(lusor)} Lich",
		"of the Lich",
		f"of the {Descriptor(lusor)} Lion",
		"of the Lion",
		"from the Labyrinth",
		f"of the {Descriptor(lusor)} Labyrinth",
		"of the Labyrinth",
		f"of the {Descriptor(lusor)} Kraken",
		"of the Kraken",
		f"of the {Rank(lusor)} Knight",
		f"of the {Descriptor(lusor)} Knight",
		"of the Knight",
		f"of the {Descriptor(lusor)} Kingdom",
		f"of the {Rank(lusor)} Kingdom",
		"of the Kingdom",
		"of the King",
		f"of the {Descriptor(lusor)} King",
		f"of the {Rank(lusor)} King",
		"of the Inn",
		f"of the {Rank(lusor)} Inn",
		f"of the {Descriptor(lusor)} Inn",
		"of the Highlord",
		f"of the {Descriptor(lusor)} Highlord",
		"of the Harbor",
		f"of {Rank(lusor)} Harbor",
		f"of {Descriptor(lusor)} Harbor",
		"of the Glade",
		f"of the {Rank(lusor)} Glade",
		f"of the {Descriptor(lusor)} Glade",
		"of the Gulf",
		f"of the {Rank(lusor)} Gulf",
		f"of the {Descriptor(lusor)} Gulf",
		"of the Guild",
		f"of the {Rank(lusor)} Guild",
		f"of the {Descriptor(lusor)} Guild",
		"of the Guardian",
		f"of the {Rank(lusor)} Guardian",
		f"of the {Descriptor(lusor)} Guardian",
		f"of the {Descriptor(lusor)} Geyser",
		"of the Geyser",
		f"of the {Descriptor(lusor)} Field",
		"of the Field",
		"of the Eagle",
		"of the Elixir",
		f"of the {Descriptor(lusor)} Elixir",
		"of Death",
		f"of the {Descriptor(lusor)} Death",
		"of the Crown",
		"of the Condor",
		"of the Boar",
		f"of {Descriptor(lusor)} Battle",
		f"of {Rank(lusor)} Battle",
		"of Battle",
		f"of the {Descriptor(lusor)} Battle",
		f"of the {Rank(lusor)} Battle",
		"of the Battle",
		"of the Baobab",
		"of the Baron",
		"of the Amulet",
		"of the Amazon",
		"of the Arena",
		"of War",
		"of the Wizard",
		"of the Wolf",
		f"of the {Descriptor(lusor)} Wolf",
		f"of the {Descriptor(lusor)} Wizard",
		"of the Skies",
		"from Beyond the Veil",
		"from Beyond The Wall",
		"of Stonehenge",
		"of the Cemetery",
		"of the Temple",
		"of Malady",
		"of the Paladin",
		"of the Pyramid",
		f"of the {Descriptor(lusor)} Pyramid",
		"of the Labyrinth",
		f"of the {Descriptor(lusor)} Labyrinth",
		f"of the {Descriptor(lusor)} Laboratory",
		"of the Laboratory",
		"of the Wilderness",
		f"of the {Descriptor(lusor)} Hunter",
		"of the Hunter",
		"of the Kraken",
		f"of the {Rank(lusor)} Organization",
		f"of the {Descriptor(lusor)} Organization",
		f"of the {Rank(lusor)} Organization",
		f"of the {Descriptor(lusor)} Organization",
		f"of the {Rank(lusor)} Organization",
		f"of the {Descriptor(lusor)} Organization",
		f"of the {Rank(lusor)} Organization",
		f"of the {Descriptor(lusor)} Organization",
		"of the Organization",
		f"of the {Rank(lusor)} Guild",
		f"of the {Rank(lusor)} Guild",
		f"of the {Rank(lusor)} Guild",
		f"of the {Rank(lusor)} Guild",
		f"of the {Rank(lusor)} Guild",
		f"of the {Rank(lusor)} Guild",
		f"of the {Rank(lusor)} Guild",
		f"of the {Descriptor(lusor)} Guild",
		"of the Guild",
		"of the Werevolves",
		"of the Galaxy",
		"of the Sphinx",
		"of Infinity",
		"of the Grassland",
		f"of the {Descriptor(lusor)} Grassland",
		"of Mistery",
		"of Mischief",
		"of Secrecy",
		"of the Kingdom",
		f"of the {Descriptor(lusor)} Kingdom",
		f"of the {Descriptor(lusor)} Baron",
		"of the Baron",
		"of Condor",
		"of the Hive",
		f"of the {Descriptor(lusor)} Wolf",
		"of the Wolf",
		"of The Goblet",
		"of The Talisman",
		"of The Sword",
		"of The Amulet",
		f"of The {Descriptor(lusor)} Goblet",
		f"of The {Descriptor(lusor)} Talisman",
		f"of The {Descriptor(lusor)} Sword",
		f"of The {Descriptor(lusor)} Amulet",
		f"of the {Descriptor(lusor)} Waterfall",
		"of the Waterfall",
		"of the Order",
		f"of the {Descriptor(lusor)} Order",
		"of the Owl",
		"of the Garden",
		"of the Ghost",
		f"of the {Descriptor(lusor)} Ghost",
		f"of {Descriptor(lusor)} Ghosts",
		f"of Ghosts",
		f"of the {Descriptor(lusor)}  Garden",
		"Of Athena",
		"of Delphos",
		"of the Vampire",
		"of the Underworld Gate",
		"of the Underworld",
		"of the Odyssey",
		"of Death",
		"of El Dorado",
		"of Eldorado"
		"Of Fate",
		"Of Heaven",										"Of Justice",
		"Of Odin",
		"Of The Abyss",
		"Of the Autumn",
		"Of the Coliseum",
		"from Heaven",										"Of Justice",
		"Of Odin",
		"Of The Abyss",
		"Of the Autumn",
		"Of the Coliseum",
		"Of The Crown",
		"Of The Dead",
		"Of The Desert",
		"Of the Divine",
		"Of The East",
		"Of The Fiends",
		"Of The Forest",
		"Of The Forge",
		"Of The Hells",
		"Of The Hills",
		"Of the Hidden",
		"of the Kingdom",
		"Of the Last Fire",
		"Of The Mountain",
		"Of The North",
		"Of the Oceans",
		"Of the Old One",
		"Of The Oracle",
		"Of the Pack",
		"Of The People",
		"Of The Pharaoh",
		"Of The Plains",
		"Of The Sands",
		"Of The Sea",
		"Of The South",
		"Of The Spring",
		"Of The Storm",
		"Of The Summer",
		"Of The West",
		"Of The Winter",
		"Of Thor",
		"Of Youth",
		"Of Zeus",
		"of the Faith",
		"of the Forty Thieves",
		"of the Morningstar",
		"of the Thousand Tears",
		"of the Jungle",
		"of the City",
		"of the Land",
		"of the North",
		"of the South",
		"of the East",
		"of the West",
		"of the Forest",
		"of the Plains",
		"of the Sea",
		"of the Sky",
		"of Fire",
		f"of the {Descriptor(lusor)} Tactics",
		f"of the {Descriptor(lusor)} City",
		"of the Golden City",
		"of the Treasure",	"of the Kraken",
		"of the Sunlord",
		"of Sundiata",
		"of Sundiatan",
		"of the Sword",
		"of Baba Yaga",
		f"of the {Descriptor(lusor)} Kraken",
		"of the Hydra",
		"of the Aegean",
		"of the Amazon",
		"of the Amazonians",
		"of the Archipelago",
		f"of the {Descriptor(lusor)} Archipelago",
		"of the Asgardians",
		"of the Atlanteans",
		"of the Aztecs",	"of the Badlands",
		"of the Babylonians",	"of the Bay",
		f"of the {Descriptor(lusor)} Bay",
		"of the Beach",
		f"of the {Descriptor(lusor)} Beach",
		"of the Glade",
		f"of the {Descriptor(lusor)} Glade",
		"of the Gorgonians",
		"of the Grassland",
		f"of the {Descriptor(lusor)} Grassland",
		"of the Gulf",
		f"of the {Descriptor(lusor)} Gulf",
		"of the Garden",
		f"of the {Descriptor(lusor)} Garden",
		"of the Geyser",
		f"of the {Descriptor(lusor)} Geyser",
		"of the Harbor",
		f"of the {Descriptor(lusor)} Harbor",
		f"of {Descriptor(lusor)} Harbor",
		"of the Hill",
		f"of the {Descriptor(lusor)} Hill",
		"of the Island",
		f"of the {Descriptor(lusor)} Island",
		f"of {Descriptor(lusor)} Island",
		"of the Marsh",
		f"of the {Descriptor(lusor)} Marsh",
		f"of {Descriptor(lusor)} Marsh",
		"of the Meadow",
		f"of the {Descriptor(lusor)} Meadow",
		f"of {Descriptor(lusor)} Meadows",
		"of the Mine",
		f"of the {Descriptor(lusor)} Mine",
		f"of {Descriptor(lusor)} Mine",
		f"of {Descriptor(lusor)}mine",
		"of Moss",
		"of the Mountain",
		f"of the {Descriptor(lusor)} Mountain",
		f"of {Descriptor(lusor)} Mountain",
		"of the Museum",
		f"of the {Descriptor(lusor)} Museum",
		"of the Oasis",
		f"of the {Descriptor(lusor)} Oasis",
		f"of {Descriptor(lusor)} Oasis",
		"of the Ocean",
		f"of {Descriptor(lusor)} Ocean",
		f"of the {Descriptor(lusor)} Ocean",
		"of the Outpost",
		f"of the {Descriptor(lusor)} Outpost",
		f"of {Descriptor(lusor)} Outpost",
		"of the Outlands",
		f"of the {Descriptor(lusor)} Outlands",
		f"of {Descriptor(lusor)} Outlands",
		"of the Glade",
		f"of the {Descriptor(lusor)} Glade",
		f"of {Descriptor(lusor)} Glade",
		"of the Grassland",
		f"of the {Descriptor(lusor)} Grassland",
		"of the Graveyard",
		f"of the {Descriptor(lusor)} Graveyard",
		"of the Grove",
		f"of the {Descriptor(lusor)} Grove",
		"of the Dark Abyss",
		"of The Seventh Hell",
		"of Hell",
		"of the Hells",
		f"of the {Descriptor(lusor)} Hells",
		"of Horus",
		"of the Jewels",
		"of the Ruby",
		"of Gold",
		"of Silver",
		"of Iron",
		"of Steel",
		"of the Underworld",
		f"of the {Descriptor(lusor)} Sanctum",
		f"of the {Descriptor(lusor)} Palace",
		f"of the {Rank(lusor)} Palace",
		"of Osiris",
		"of Helios",
		"of Helio",
		"of Helion",
		"of Heliod",
		"of Blood",
		f"of the {Rank(lusor)} Shrine",
		"of Akros",
		"for the Hunt",
		"of Kiranta",
		f"for the {Descriptor(lusor)} Hunt",
		"of Lunden",
		"of Ages",
		"of the Ages",
		"of Londinium",
		"of the Great Hunt",
		"of Azurius",
		"of Power",
		"of Darkwood",
		"of the Blood Rites",
		f"of the {Descriptor(lusor)} Rites",
		f"of the {Rank(lusor)}'s Island",
		f"of the {Descriptor(lusor)} Island",
		f"of the {Descriptor(lusor)} Hunt",
		"of the Moon Fortress",
		f"of the {Descriptor(lusor)} Fortress",
		f"of the {Descriptor(lusor)} Throne",
		f"of the Throne",
		"of Queen Boudica",
		"of Liliana",
		"of Athens",
		"of Paradise",
		"of Vesuva",
		"of the Glade",
		"of Carcosa",
		"of Azorius",
		"of Nylea",
		"of Rakdos",
		"of the Monolith",
		"of the Smoke",
		"of The Capital",
		"of the Triumvirate",
		f"of the {Descriptor(lusor)} Triumvirate",
		f"of The {Descriptor(lusor)} Smoke",
		f"of The {Descriptor(lusor)} Capital",
		"of the Overgrown Forest",
		"of the Overgrown Land",
		f"of the {Descriptor(lusor)} Monolith",
		"of the Wild Hunt",
		f"of the {Descriptor(lusor)} Hunt",
		f"of the {Rank(lusor)}'s Hunt",
		"of the Ancient Tomb",
		f"of the Broken Land",
		f"of the Sea Gate",
		"of the Deep",
		f"of the {Rank(lusor)}'s Revenge",
		f"of the {Rank(lusor)}'s Menace",
		f"of the Raging Storm",
		f"of the {Descriptor(lusor)} Storm",
		f"of the {Descriptor(lusor)} Fountain",
		f"of the {Descriptor(lusor)} Gate",
		f"of the {Descriptor(lusor)} Land",
		f"of the {Descriptor(lusor)} Tomb",
		f"of the {Descriptor(lusor)} Forest",
		f"of the {Rank(lusor)}'s Palace",
		f"of the {Rank(lusor)}'s Glade",
		f"of the {Rank(lusor)}'s Gate",
		f"of the {Rank(lusor)}'s Land",
		f"of the {Rank(lusor)}'s Forest",
		f"of the {Rank(lusor)}'s Tomb",
		"of the Blossoming Sands",
		f"of the {Rank(lusor)}",
		f"of the {Rank(lusor)}",
		f"of the {Rank(lusor)}",
		f"of the {Rank(lusor)}",
		f"of the {Rank(lusor)}'s Road'",
		f"of the {Rank(lusor)}'s Road'",
		f"of the {Rank(lusor)}'s Road'",
		f"of the {Rank(lusor)}'s Road'",
		"of the Pilgrim's Road",
		"of Myth",
		"Of The Marsh",
		"of the Talsiman",
		"of Memory",
		"of the Tiger",
		"of Extinction",
		f"of the {Descriptor(lusor)} Sandbar",
		f"of the {Descriptor(lusor)} Sun's Zenith",
		f"of {Descriptor(lusor)} Memory",
		"of the Watcher",
		"of the Consulate",
		"of the False God",
		f"of the {Descriptor(lusor)} God",
		"of Spirits",
		"of the Moon",
		"Of Mirrodin",
		"of the Depths",
		"of Might",
		"of the Provinces",
		"of the Stars",
		f"of the {Descriptor(lusor)} Star",
		f"of {Descriptor(lusor)} Might",
		"of the Elemental",
		f"of the {Descriptor(lusor)} Elemental",
		"Of Denial",
		"of the Sun",
		"of the Black Sun",
		f"of the {Descriptor(lusor)} Sun",
		"of the Spirit",
		"of the Spirits",
		f"of the {Descriptor(lusor)} Spirit",
		f"of the {Descriptor(lusor)} Spirits",
		"of the Damned",
		"of the Sands of Time",
		f"of the {Descriptor(lusor)} Fire",
		f"of {Descriptor(lusor)} Fire",
		f"of the Temple",
		f"of the {Descriptor(lusor)} Temple",
		f"of the {Descriptor(lusor)} Temple",
		"of Death",
		f"of the {Rank(lusor)}'s' Temple",
		f"of Fire",
		"of the Flames",
		f"of the {Descriptor(lusor)} Flames",
		f"of the {Descriptor(lusor)} Descent",
		f"of the {Descriptor(lusor)} Destiny",
		f"of the {Descriptor(lusor)} Fire",
		f"of the {Descriptor(lusor)} Heritage",
		f"of the {Descriptor(lusor)} Hoard",
		f"of the {Descriptor(lusor)} Horn",
		f"of the {Descriptor(lusor)} Lineage",
		f"of the {Descriptor(lusor)} Maze",
		f"of the {Descriptor(lusor)} Ocean",
		f"of the {Descriptor(lusor)} Sea",
		f"of the {Descriptor(lusor)} Shore",
		"Of Death",
		"of the Enigma",
		"of the Eclipse",
		"Of Blood",
		"of the Blood Court",
		"of the Throne",
		"of the Tomb",
		"of the Underworld",
		"of the Cavern",
		f"of {Descriptor(lusor)} Duty",
		f"of the {Descriptor(lusor)} Tribe",
		f"of the {Descriptor(lusor)} Wings",
		f"of the {Descriptor(lusor)} Tomb",
		f"of the {Descriptor(lusor)} Throne",
		f"of the {Descriptor(lusor)} Legion",
		f"of the {Descriptor(lusor)} Realm",
		f"of the {Descriptor(lusor)} Court",
		f"of the {Descriptor(lusor)} Blood",
		f"of the {Descriptor(lusor)} Castle",
		f"of the {Descriptor(lusor)} Jungle",
		"Of Darkness",
		"of the Covenant",
		f"of the {Descriptor(lusor)} Covenant",
		f"of the {Descriptor(lusor)} Depths",
		"of the Depths",
		"of the Unknown",
		f"of the {Descriptor(lusor)} Unknown",
		"of the Dragon",
		"of the Dark Prophecy",
		"of the Blood Moon",
		f"of the {Descriptor(lusor)} Moon",
		f"of the {Descriptor(lusor)} Prophecy",
		"of the Plains",
		"of the Hunt",
		"of the Stars",
		f"of the {Descriptor(lusor)} Dream",
		"of the Spirits",
		f"of the {Descriptor(lusor)} Spirit",
		f"of the {Descriptor(lusor)} Mountain",
		f"of the {Descriptor(lusor)} Lair",
		"Of Heaven",
		"Of Justice",
		f"of the {Descriptor(lusor)} Death",
		"Of Odin",
		"Of Power",
		"Of The Abyss",
		"Of the Autumn",
		"Of The Crown",
		"Of The Desert",
		"Of The Dead",
		"Of The East",
		"Of The Forest",
		"Of The Forge",
		"Of The Fiends",
		"Of the Kingdom",
		"Of The Hills",
		"Of the Hells",
		"Of The North",
		"Of The Mountain",
		"Of the Oceans",
		"Of the Old One",
		"Of The Plains",
		"Of the Pack",
		"Of The People",
		"Of The Pharaoh",
		"Of The Sands",
		"Of The Sea",
		"Of The South",
		"Of The Summer",
		"Of The Spring",
		"Of The Storm",
		"Of The West",
		"Of The Winter",
		"Of Thor",
		"Of Zeus",
		"Of Justice",
		"Of The East",
		"Of The West",
		"Of The North",
		"Of The South",
		"Of The Forest",
		"Of The Hills",
		"Of The Mountain",
		"Of The Sands",
		"Of The Sea",
		"of the Wild",
		"of the Otherworld",
		"of Pain",
		f"of the {Descriptor(lusor)} Maelstrom",
		f"of the {Descriptor(lusor)} Whirl",
		f"of the {Descriptor(lusor)} Realm",
		f"of the {Descriptor(lusor)} Vision",
		f"of the {Descriptor(lusor)} Depth",
		f"of the {Descriptor(lusor)} Sands",
		f"of the {Descriptor(lusor)} Storm",
		f"of the {Descriptor(lusor)} Frontier",
		f"of the {Descriptor(lusor)} Battle",
		f"of the {Descriptor(lusor)} Roar",
		f"of the {Descriptor(lusor)} Forest",
		f"of the {Descriptor(lusor)} Meadow",
		f"of the {Descriptor(lusor)} Glades",
		f"of the {Descriptor(lusor)} Forest",
		f"of the {Descriptor(lusor)} Realm",
		f"of the {Descriptor(lusor)} Legend",
		f"of the {Descriptor(lusor)} Wild",
		f"of the {Descriptor(lusor)} Tundra",
		f"of the {Descriptor(lusor)} Pack",
		f"of the {Descriptor(lusor)} Roar",
		f"of the {Descriptor(lusor)} Grove",
		f"of the {Descriptor(lusor)} Sea",
		f"of the {Descriptor(lusor)} Depths",
		"of the Void",
		"of the Stars",
		 f"of the {Descriptor(lusor)} World",
		 f"of the {Descriptor(lusor)} Ruin",
		 f"of the {Descriptor(lusor)} Jungle",
		 f"of the {Descriptor(lusor)} Land",
		"of the Endless Hunt",
		f"of the {Descriptor(lusor)} Hunt",
		]

	# Backgrounds 		{Descriptor(lusor)}
	if "Berserker"	in genus:
		origin += [
		 f"of the {Descriptor(lusor)} Fury",
		 f"of the {Descriptor(lusor)} Tribe",
		 f"of the {Descriptor(lusor)} Lands",
		 f"of the {Descriptor(lusor)} Mountain",
		 f"of the {Descriptor(lusor)} Clan",
		 f"of the {Descriptor(lusor)} Raid",
		]
	if "Bard"		in genus:
		origin += [
			"of the Festival",
			]
	if "Barbarian"	in genus:
		origin += [
		 f"of the {Descriptor(lusor)} Tribe",
		]
	if "Cleric" 	in genus:
		origin += [
			f"of the {Descriptor(lusor)} Gods",
			"of the Gods",
			"of the Holy Order",
			"of the Order",
			"of the Mission",
			"of the Journey",
			"of the Path",
			"of the Light",
			f"of the {Descriptor(lusor)} Order",
			f"of the {Descriptor(lusor)} Order",
			f"of the {Descriptor(lusor)} Mission",
			f"of the {Descriptor(lusor)} Journey",
			f"of the {Descriptor(lusor)} Pilgrimage",
			f"of the {Descriptor(lusor)} Crusade",
			f"of the {Descriptor(lusor)} Path",
			f"of the {Descriptor(lusor)} Light",
			f"of the {Descriptor(lusor)} Quest",
			]
	if "Criminal" 	in genus:
		origin += [
		f"of the {Descriptor(lusor)} Penitentiary",
		"of the Penitentiary",
		"of the Underworld",
		"of the Network",
		f"of the {Descriptor(lusor)} Escape",
		f"of the {Descriptor(lusor)} Ambitions",
		f"of the {Descriptor(lusor)} Deal",
		f"of the {Descriptor(lusor)} Scheme"]
	if "Cultist" 	in genus:
		origin = [
			f"of the {Descriptor(lusor)} Gods",
			f"of the Gods",
			"of the Sect",
			"of Rites",
			"of the Order",
			"of the Ritual",
			"of the Yellow King",
			"of the King in Yellow",
			f"of the {Descriptor(lusor)} King",
			]
	if "Expert" 	in genus:
		origin += [
			f"of {Descriptor(lusor)} Field",
			f"of {Descriptor(lusor)} Trade",
			f"of {Descriptor(lusor)} Study",
			f"of {Descriptor(lusor)} Research",
			f"of {Descriptor(lusor)} Skill"]
	if "Explorer" 	in genus:
		origin = [
			"of the Uncharted Lands",
			f"of the Jungle",
			f"of the {Descriptor(lusor)} Jungle",
			f"of the {Descriptor(lusor)} Expedition",
			f"of the {Descriptor(lusor)} Journey",
			f"of the {Descriptor(lusor)} Quest",
			f"of the {Descriptor(lusor)} Frontiers",
			]
	if "Crafter" 	in genus:
		origin = [
			f"of the {Descriptor(lusor)} Hand",
			f"of the {Descriptor(lusor)} Market",
			f"of the {Descriptor(lusor)} Design",
			f"of the {Descriptor(lusor)} Creation",
			f"of the {Descriptor(lusor)} Mind"]
	if "Druid" 		in genus:
		origin += [
		"of the Wild",
		"of the Jungle",
		"of the Woods",
		"of the Grove"
		f"of the {Descriptor(lusor)} Circle",
		f"of the {Descriptor(lusor)} Circle",
		f"of the {Descriptor(lusor)} Circle",
		f"of the {Descriptor(lusor)} Circle",
		f"of the {Descriptor(lusor)} Circle",
		f"of the {Descriptor(lusor)} Circle",
		f"of the {Descriptor(lusor)} Circle",
		f"of the {Descriptor(lusor)} Circle",
		f"of the {Descriptor(lusor)} Circle",
		f"of the {Descriptor(lusor)} Circle",
		f"of the {Descriptor(lusor)} Woods",
		f"of the {Descriptor(lusor)} Woods",
		f"of the {Descriptor(lusor)} Woods",
		f"of the {Descriptor(lusor)} Jungle",
		f"of the {Descriptor(lusor)} Jungle",
		f"of the {Descriptor(lusor)} Jungle",
		f"of the {Descriptor(lusor)} Jungle",
		]
	if "Guard" 		in genus:
		origin = [
			f"of the {Descriptor(lusor)} Guards",
			f"of the {Rank(lusor)} Guards",
			f"of the {Descriptor(lusor)} Watch",
			f"of the {Descriptor(lusor)} Fortress",
			f"of the {Descriptor(lusor)} Wall",
			f"of the {Descriptor(lusor)} Gate",
			f"of the {Descriptor(lusor)} Patrol",
			f"of the {Descriptor(lusor)} Tower",
			f"of the {Descriptor(lusor)} Keep",
			]
	if "Healer" 	in genus:
		origin += [
			f"of the {Descriptor(lusor)} Gods",
			f"of the {Descriptor(lusor)} Touch",
			f"of the {Descriptor(lusor)} Remedy",
			f"of the {Descriptor(lusor)} Hand",
			f"of the {Descriptor(lusor)} Treatment",
			f"of the {Descriptor(lusor)} Care",
				   ]
	if "Hero" 		in genus:
		origin = [
			f"of the {Descriptor(lusor)} Gods",
			f"of the {Descriptor(lusor)} Deed",
			f"of the {Descriptor(lusor)} Battle",
			f"of the {Descriptor(lusor)} Venture",
			f"of the {Descriptor(lusor)} Quest",
			f"of the {Descriptor(lusor)} Cause"]
	if "Hunter" 	in genus:
		origin = [
			f"of the {Descriptor(lusor)} Jungle",
			f"of the {Descriptor(lusor)} Hunt",
			f"of the {Descriptor(lusor)} Stealth",
			f"of the {Descriptor(lusor)} Wilderness",
			f"of the {Descriptor(lusor)} Range",
			f"of the {Descriptor(lusor)} Snares",
			 "of the Wild Hunt",
			f"of the {Descriptor(lusor)} Hunt",
			]
	if "Knight" 	in genus:
		origin = [
			f"of the {Descriptor(lusor)} Gods",
			f"of the {Descriptor(lusor)} Order",
			f"of the {Descriptor(lusor)} Quest",
			f"of the {Descriptor(lusor)} Deed",
			f"of the {Descriptor(lusor)} Battle",
			f"of the {Descriptor(lusor)} Venture",
			]
	if "Mage" 		in genus:
		origin = [
			"of Mysteries",
			"of Mystical Arts",
			"of the Scrolls",
			"of Potions",
			f"of the {Descriptor(lusor)} Academy",
			f"of the {Descriptor(lusor)} Tower",
			f"of the {Descriptor(lusor)} Scroll",
			f"of the {Descriptor(lusor)} Mystery",
			]
	if "Monk" 		in genus:
		origin += [
			f"of the {Descriptor(lusor)} Gods",
		  f"of the {Descriptor(lusor)} Path",
		  f"of {Descriptor(lusor)} Enlightenment",
		  f"of {Descriptor(lusor)} Tranquility",
		  f"of the {Descriptor(lusor)} Way",
		  f"of {Descriptor(lusor)} Balance",
		  f"of {Descriptor(lusor)} Order",
		  ]
	if "Merchant" 	in genus:
		origin = [
			f"of the {Descriptor(lusor)} Empire",
			f"of the {Descriptor(lusor)} Market",
			f"of the {Descriptor(lusor)} Venture",
			f"of the {Descriptor(lusor)} Organization",
			f"of the {Descriptor(lusor)} Company",
			f"of the {Descriptor(lusor)} Company",
			f"of the {Descriptor(lusor)} Company",
			f"of the {Descriptor(lusor)} Company",
			f"of the {Descriptor(lusor)} Corporation",
			f"of the {Descriptor(lusor)} Corporation",
			f"of the {Descriptor(lusor)} Corporation",
			f"of the {Descriptor(lusor)} Corporation",
			f"of the {Descriptor(lusor)} Corporation",
			]
	if "Pirate" 	in genus:
		origin += [
			"of Blackbeard",
			f"of the {Descriptor(lusor)}beard",
			f"of the {Descriptor(lusor)} Sea",
			f"of the {Descriptor(lusor)} Crew",
			f"of the {Descriptor(lusor)} Voyage",
			f"of the {Descriptor(lusor)} Journey",
			f"of the {Descriptor(lusor)} Fleet",
			f"of the {Descriptor(lusor)} Ship",
			f"of the {Descriptor(lusor)} Treasure",
			]
	if "Ranger" 	in genus:
		origin += [
			f"of the {Descriptor(lusor)} Jungle",
			f"of the {Descriptor(lusor)} Paths",
			f"of the {Descriptor(lusor)} Hunts",
			f"of the {Descriptor(lusor)} Camps",
			f"of the {Descriptor(lusor)} Mountains",
			f"of the {Descriptor(lusor)} Secrets",
			]
	if "Scholar" 	in genus:
		origin += [
		 f"of the {Descriptor(lusor)} Academy",
		 f"of the {Descriptor(lusor)} Society",
		 f"of the {Descriptor(lusor)} Library",
		 f"of the {Descriptor(lusor)} Lecture",
		 f"of the {Descriptor(lusor)} Scroll",
		 ]
	if "Soldier" 	in genus:
		origin += [
			f"of the {Descriptor(lusor)} Regiments",
			f"of the {Descriptor(lusor)} Regiment",
			f"of the {Descriptor(lusor)} Regiment",
			f"of the {Descriptor(lusor)} Fronts",
			f"of the {Descriptor(lusor)} Fronts",
			f"of the {Descriptor(lusor)} Commands",
			f"of the {Descriptor(lusor)} Units",
			f"of the {Descriptor(lusor)} Operations",
			f"of {Descriptor(lusor)} Operations",
			]
	if "Wizard"		in genus:
		origin += [
		"of Merlin",
		]
	# Races			{Descriptor(lusor)}
	if "Avens" 		in genus:
		origin += [
		"of the High Skies",
		 "of the Soaring Winds",
		 "of the Cloud Realm",
		 "of the Endless Horizon",
		 "of the Winged Tribes",
		 ]
		if "Owlin" 		in genus:
				origin += [
					"of the Moonlight",
					"of the Forests",
					"of Silence",
					"of the Skies",
					"of the Twilight",
					"of Wisdom"]
		if "Tengu" 		in genus:
			origin += [
				f"of the {Descriptor(lusor)} Tale",
				 "of the Hidden Dojo",
				 "of the Martial Paths",
				 "of the Folklore Mysteries",
				 "of the Clever Beaks"]
		if "Raptoran" 	in genus:
			origin += [
				"of the Mountain Aeries",
				 "of the Windcut Cliffs",
				 "of the High Ridges",
				 "of the Soaring Currents",
				 "of the Lofty Nests"]
		if "Aarakocra" 	in genus:
			origin += [
			"of the Mountain Peak",
			"of the Spiraling Thermal",
			 "of the Sacred Wind",
			 "of the Cloud Monastery",
			 "of the Heavenly Dances"]
		if "Kenku" 		in genus:
			origin += [
			"of the Echoing Voice",
			 "of the Shadowed Alley",
			 "of the Urban Jungle",
			 "of the Crafty Beak",
			 "of the Stolen Secret"]
		if "Birdfolk" 	in genus:
			origin += [
			"of the Verdant Forest",
			 "of the Melodious Song",
			 "of the Nested Height",
			 "of the Diverse Plume",
			 "of the Winged Assembly"]
	if "Aberration" in genus:
		if "Githzerai" 			in genus:
			origin += [
			"of the Inner Peace",
			 "of the Mystic Paths",
			 "of the Ascet Way",
			 "of the Spiritual Harmony",
			 "of the Enlightened Realm"]
		if "Githyanki" 			in genus:
			origin += [
			"of the Astral Raids",
			 "of the Conquered Realm",
			 "of the Endless War",
			 "of the Ruthless Campaign",
			 "of the Dominant Force"]
		if "Destiny Devouers" 	in genus:
			origin += [
				"of Time",
				"of Destiny",
				"of the Vortex",
				]
		if "Parasyte" 			in genus:
			origin += [
				f"of the {Descriptor(lusor)} Bodies",
				f"of the {Descriptor(lusor)} Hive",
				f"of the {Descriptor(lusor)} Web",
				f"of the {Descriptor(lusor)} Realm",
				f"of the {Descriptor(lusor)} Infection"]
		if "Symbioid" 			in genus:
			origin += [
				f"of the {Descriptor(lusor)} Union",
				f"of the {Descriptor(lusor)} Hive",
				f"of the {Descriptor(lusor)} Web",
				f"of the {Descriptor(lusor)} Organism"]
		if "Alien Spawn" in genus:
			origin += [
			f"of the {Descriptor(lusor)} World",
			f"of the {Descriptor(lusor)} Realm",
			f"of the {Descriptor(lusor)} Cosmos",
			f"of the {Descriptor(lusor)} Dominions",
			f"of the {Descriptor(lusor)} Terror"]
		if "Chaos Warper" in genus:
			origin += [
			 "of the Star Field",
			 "of the Galactic Core",
			 "of the Astral Plane",
			 "of the Cosmic Void",
			 "of the Nebula"]
		if "Living Spell" in genus:
				origin += [
				"of the Spell Storms",
				 "of the Arcane Nexus",
				 "of the Magical Anomalies",
				 "of the Enchanted Vortex",
				 "of the Wizard's Binding"]
		if "Dominators" in genus:
			origin += [
			"of the Iron Will",
			 "of the Dominant Chain",
			 "of the Enslaved Realm",
			 "of the Ruthless Order",
			 "of the Commanding Heights"]
	if "Beast" 		in genus:
		origin += [
			"of the Stampede",
			f"of the {Descriptor(lusor)} Stampede",
			"of the Jungle",
			f"of the {Descriptor(lusor)} Jungle",
			]
		if "Giant Eagle" 	in genus:
			origin += [
			"of the Soaring Height",
			 "of the Mountain",
			 "of the Sky",
			 "of the Wind",
			 "of the Cloud Kingdom",
			 "of the Clouds",
			 ]
		if "Kong" 			in genus:
			origin += [
			f"of the {Descriptor(lusor)} Isle",
			f"of the {Descriptor(lusor)} Jungle",
			f"of the {Descriptor(lusor)} Grove",
			f"of the {Descriptor(lusor)} Peak",
			f"of the {Descriptor(lusor)} Wild"]
		if "Monkey King" 	in genus:
			origin += [
				f"of the {Descriptor(lusor)} Mischief",
				f"of the {Descriptor(lusor)} Path",
				f"of the {Descriptor(lusor)} Mountain",
				f"of the {Descriptor(lusor)} Realm",
				f"of the {Descriptor(lusor)} Adventure"]
		if "Armored Bear" 	in genus:
			origin += [
				f"of the {Descriptor(lusor)} Realm",
				f"of the {Descriptor(lusor)} Fortress",
				f"of the {Descriptor(lusor)} Clan",
				f"of the {Descriptor(lusor)} Woods",
				f"of the {Descriptor(lusor)} Defenders"]
		if "Tiger" 			in genus:
			origin += [
				"of the Snow",
				f"of the {Descriptor(lusor)} Mountain",
				f"of the {Descriptor(lusor)} Forests",
				f"of the {Descriptor(lusor)} Valleys",
				"of the Frost",
				"of the Hunt",
				f"of the {Descriptor(lusor)} Hunt",
				]
		if "Vulture" 		in genus:
			origin += [
			"of Death",
			 f"of the {Descriptor(lusor)} Sky",
			 f"of the {Descriptor(lusor)} Ommen",
			 f"of the {Descriptor(lusor)} Desert"
			 ]
		if "Deer" 			in genus:
			origin += [
			f"of the {Descriptor(lusor)} Woods",
			f"of the {Descriptor(lusor)} Glade",
			f"of the {Descriptor(lusor)} Trail",
			f"of the {Descriptor(lusor)} Path",
			f"of the {Descriptor(lusor)} Kingdom",
			f"of the {Descriptor(lusor)} Lake",
			]
		if "Owl" 			in genus:
			origin += [
			f"of the {Descriptor(lusor)} Knowledge",
			f"of the {Descriptor(lusor)} Sky",
			f"of the {Descriptor(lusor)} Hunt",
			f"of the {Descriptor(lusor)} Vision",
			f"of the {Descriptor(lusor)} Woods",
			]
	if "Kitsune"	in genus:
		origin += [
			"of Nine Tails",			"of Nine Tails",			"of the Trickster",
			]
	if "Catfolk"	in genus:
		origin += [
		"of the Pride",
		f"of the {Descriptor(lusor)} Pride"
		f"of the {Descriptor(lusor)} Pride",
		]
	if "Elf"		in genus:
		origin += [
		"of Llanowar",
		]
	if "Fiend"		in genus:
		origin += [
		"of Hades",
		"of the Underworld Gates",
		"of the Pit",
		]

	origin += [
		f"of the {Descriptor(lusor)} War",
		f"of the {Rank(lusor)} War",
		"of the Sun Stone",
		f"of the {Descriptor(lusor)} Stone",
		"of Souls",
		"of Bane",
		"of Tiamat",
		f"of The {Descriptor(lusor)} Town",
		"of the Forbidden Cave",
		"of the Frontier",
		"of the Gods",
		"of Fate",
		"of Freya",
		"of Icarus",
		"of Midgard",
		"of Prometheus",
		"of the Caribbean",
		"of the State",
		"of Monsters",
		f"of the {Descriptor(lusor)} Realm",
		f"of the {Descriptor(lusor)} Church",
		f"of the {Descriptor(lusor)} Dawn",
		f"of the {Descriptor(lusor)} Grove",
		f"of the {Descriptor(lusor)} Desert",
		f"of the {Descriptor(lusor)} Dragon",
		f"of the {Descriptor(lusor)} Elders",
		f"of the {Descriptor(lusor)} Faith",
		f"of the {Descriptor(lusor)} Forest",
		f"of the {Descriptor(lusor)} Kingdom",
		f"of the {Descriptor(lusor)} Mountain",
		f"of the {Descriptor(lusor)} Night",
		f"of the {Descriptor(lusor)} Phoenix",
		f"of the {Descriptor(lusor)} Plains",
		f"of the {Descriptor(lusor)} River",
		f"of the {Descriptor(lusor)} Sea",
		f"of the {Descriptor(lusor)} Star",
		f"of the {Descriptor(lusor)} Swamp",
		f"of the {Descriptor(lusor)} War",
		"of Vampires",
		f"of the {Descriptor(lusor)} Arts",
		f"of the {Descriptor(lusor)} Flame",
		f"of the {Descriptor(lusor)} Order",
		f"of the {Descriptor(lusor)} Eternal",
		f"of the {Descriptor(lusor)} Fire",
		f"of the {Descriptor(lusor)} Firestorm",
		f"of the {Descriptor(lusor)} Gate",
		f"of the {Descriptor(lusor)} Labyrinth",
		f"of the {Descriptor(lusor)} Mountain",
		f"of the {Descriptor(lusor)} Realm",
		f"of the {Descriptor(lusor)} Saga",
		f"of the {Descriptor(lusor)} Waterfall",
		f"of the {Descriptor(lusor)} Woods",
		f"of the {Descriptor(lusor)} Thieves",
		"of the Quest",
		"for Hire",
		"for Hire",
		"for Hire",
		"for Hire",
		"for Hire",
		"for Hire",
		"of Akroma",
		"Of Athena",
		"of Baba Yaga",
		"Of Death",
		"of Delphos",
		"of El Dorado",
		"of Eldorado",
		"of Elysium",
		"Of Fate",
		"of Fire",
		"of Gold",
		"Of Heaven",
		"of Hell",
		"of Hispaniola",
		"of Iron",
		"Of Justice",
		"of La Noche Triste",
		"of Niflheim",
		"Of Odin",
		"of Port Royal",
		"of Silver",
		"of Steel",
		"Of The Abyss",
		"of The Seventh Hell",
		"of The Amulet",
		"Of the Autumn",
		"of the Bamboo Grove",
		"of the City",
		"Of the Coliseum",
		"Of The Crown",
		"Of The Dead",
		"Of The Desert",
		"Of the Divine",
		"Of The East",
		"of the East",
		"of the Endless Sands",
		"of the Eternal Saga",
		"of the Eternal",
		"of the Faith",
		"Of The Fiend",
		"Of The Forest",
		"of the Forest",
		"Of The Forge",
		"of the Forty Thieves",
		"of the Galaxy",
		"of The Goblet",
		"of the Gods",
		"of the Golden City",
		"of The Griffon",
		"Of The Hells",
		"Of the Hidden",
		"Of The Hill",
		"of the Hydra",
		"of the Jewel",
		"of the Jungle",
		"Of the Kingdom",
		"of the Kraken",
		"of the Labyrinth",
		"of the Land",
		f"of the {Descriptor(lusor)} Land",
		"Of the Last Fire",
		"of the Moon Wood",
		"of the Morningstar",
		"of the Mountain",
		"Of The Mountain",
		"Of The North",
		"of the North",
		"Of the Oceans",
		"of the Odyssey",
		"Of the Old One",
		"Of The Oracle",
		"Of the Pack",
		"Of The People",
		"Of The Pharaoh",
		"Of The Plain",
		"of the Plains",
		"of the Ruby",
		"Of The Sands",
		"Of The Sea",
		"of the Sea",
		"of the Sky",
		"Of The South",
		"of the South",
		"Of The Spring",
		"Of The Storm",
		"Of The Summer",
		"of the Swamp",
		"of The Sword",
		"of The Talisman",
		"of the Thousand Tears",
		"of the Underworld Gate",
		"of the Underworld",
		"of the Waterfall",
		"Of The West",
		"of the West",
		"Of The Winter",
		"Of Thor",
		"of Uruk",
		"of Vasilisa",
		"of Whispers",
		"Of Youth",
		"Of Zeus",
		"of the Temple",
		"of the Dunes",
		f"of the {Descriptor(lusor)} Tomb",
		"of the Sun",
		"of the Golden Hoard",
		f"of the {Descriptor(lusor)} Hoard",
		]

	if "Rogue" in genus:
		origin += [
		  "of the Shadows",
		  f"of the {Descriptor(lusor)} Shadow",
		  f"of the {Descriptor(lusor)} Plot",
		  f"of the {Descriptor(lusor)} Escape",
		  f"of the {Descriptor(lusor)} Underworld",
		  f"of the {Descriptor(lusor)} Heist"]
	if "Shaman" in genus:
		origin += [
			f"of the {Descriptor(lusor)} Gods",
			f"of the {Descriptor(lusor)} Jungle",
			f"of the {Descriptor(lusor)} Rites",
			f"of the {Descriptor(lusor)} Visions",
			f"of the {Descriptor(lusor)} Forces",
			f"of the {Descriptor(lusor)} Traditions",
			f"of the {Descriptor(lusor)} Spirits",
			f"of the Ancestral Spirits",]
	if "Spy" in genus:
		origin += [
			 "of the Mission",
			 "of the Undercover Operation",
			 "of the Network",
			 "of Reconnaissance",
			 ]
	if "Fiend" in genus:
		origin += [
			"of Avernus",
			]
	if "Traveler" in genus:
		origin += [
			f"of the {Descriptor(lusor)} Jungle",
			f"of the {Descriptor(lusor)} Path",
			f"of the {Descriptor(lusor)} Expedition",
			f"of the {Descriptor(lusor)} Tribe",
			f"of the {Descriptor(lusor)} Voyage",
			f"of the {Descriptor(lusor)} Discovery"]
	if "Trickster" in genus:
		origin += [
			"of the Street",
			f"of the {Descriptor(lusor)} Corner",
			f"of the {Descriptor(lusor)} Alleys",
			]
	if "Warrior" in genus:
		origin += [
			f"of the {Descriptor(lusor)} Arena",
			f"of the {Descriptor(lusor)} Campaign",
			f"of the {Descriptor(lusor)} Conquest",
			f"of the {Descriptor(lusor)} Combat",
			f"of the {Descriptor(lusor)} Duels",
			f"of the {Descriptor(lusor)} War",
			]
	if "Warlock" in genus:
		origin += [
			f"of the {Descriptor(lusor)} Gods",
			"of the Deal",
			"of the King in Yellow",
			"of The Master",
			"of the Sold Soul",
			f"of the  God",
			f"of the {Descriptor(lusor)} King",
			f"of the {Descriptor(lusor)} Lore",
			f"of The {Descriptor(lusor)} Master",
			f"of the {Descriptor(lusor)} Powers",
			f"of the {Descriptor(lusor)} Rites",
			f"of the {Descriptor(lusor)} Secrets",
			]
	if "Witch" in genus:
		origin += [
			"of La Llorona",
			"of the Enchanting Spell",
			f"of the {Descriptor(lusor)} Arts",
			f"of the {Descriptor(lusor)} Curse",
			f"of the {Descriptor(lusor)} Curses",
			f"of the {Descriptor(lusor)} Jungle",
			f"of the {Descriptor(lusor)} Ritual",
			f"of the {Descriptor(lusor)} Spell",
			f"of the {Descriptor(lusor)} Tradition",
			]
	if "Priest" in genus:
		origin += [
		f"of the {Descriptor(lusor)} Gods",
		  "of the Orders",
		  f"of the {Descriptor(lusor)} Congregation",
		  f"of the {Descriptor(lusor)} Ministry",
		  f"of the {Descriptor(lusor)} Order",
		  f"of the {Descriptor(lusor)} Rite",
		  f"of the {Descriptor(lusor)} Sanctuary",
		  ]
	if "Aberration" in genus:
		origin += [
			"of the Jungle",

			f"of the {Descriptor(lusor)} Jungle",

			]
	if "Shapeshifters" in genus:
		origin += [
			"of the Shifting Forms",
			"of the Many Faces",
			"of the Illusory Guises",
			"of the Changing Aspects",
			"of the Protean Nature",
			]
	if "Illithid" in genus:
		origin += [
			"of the Deep Mind",
			"of the Psychic Network",
			"of the Mind Harvest",
			"of the Brain Conclave",
			"of the Mental Dominion",
			]
	if "Beholder" in genus:
		origin += ["of the Thousand Eyes",

					   "of the Dark Void",

					   "of the Unseen Terrors",

					   "of the Realm",

					   "of the Arcane"]
	if "Old One" in genus:
			origin += [
			  "of the Ageless Eon",

			  "of the Cosmic Depth",

			  "of the Eldritch Secret",

			  "of the Starry Void",

			  "of the Ancient Mystery"]
	if "Mindlinker" in genus:
	  origin += ["of the Collective Consciousness",
		 "of the Wisdom Network",
		 "of the Harmonious Minds",
		 "of the Thought Weave",
		 "of the Knowledge Nexus"]
	if "Noble" 	in genus:
		origin += [
			f"of the {Descriptor(lusor)} Palace",
			f"of the {Descriptor(lusor)} Court",
			f"of the {Descriptor(lusor)} Estate",
			f"of the {Descriptor(lusor)} Mansions",
			f"of the {Descriptor(lusor)} Council",
			f"of the {Descriptor(lusor)} Assembly",
			]
	if "Goblin" in genus:
		origin += [
			f"of the {Descriptor(lusor)} Pirates",
			f"of the {Descriptor(lusor)} Horde",
			f"of the {Descriptor(lusor)} Nomads",
			f"of the {Descriptor(lusor)} Travelers",
			f"of the {Descriptor(lusor)} Swamp",
			f"of the {Descriptor(lusor)} Leaf",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			f"of the {Descriptor(lusor)} Clan",f"of the {Descriptor(lusor)} Clan",
			"of the Abyssal Agents",
			"of the Astute Axle",
			"of the Ate Map",
			"of the Backwards Bunch",
			"of the Blinking Bearer",
			"of the Blinking Blossom",
			"of the Boggles",
			"of the Bouncing Rabbit",
			"of the Brainy Bolt",
			"of the Bright Bannerman",
			"of Brilliantbolt",
			"of the Broken Compass",
			"of Brokentooth",
			"of the Can’t Pants",
			"of the Can’t Tie Shoes",
			"of the Cantcount",
			"of the Cats Talk",
			"of the Charming Cherry",
			"of the Clever",
			"of the Clever Trickster",
			"of the Crafty Coil",
			"of the Crimson Creepers",
			"of the Cunning Fox",
			"of the Dancing Dewdrop",
			"of the Dancing Leaf",
			"of the Dancing Tree",
			"of the Dark Abyss",
			"of the Dark",
			"of the Dazzling",
			"of the Dazzling Dancer",
			"of the Dewy Dreamer",
			"of the Dizzy",
			"of the Drools",
			"of the Dull Blade",
			"of the Dusk Dweller",
			"of the Enchanted Ember",
			"of the Enchanted",
			"of the Ethereal Elm",
			"of the Ethereal Errand",
			"of the Feet Trips",
			"of the Fell Hole",
			"of the Feywild Follower",
			"of the Fierce Wolf",
			"of the Forgotten Names",
			"of the Frosty Fern",
			"of the Fuddle",
			"of the Fuzzy",
			"of the Gadget Gleam",
			"of the Giggly",
			"of the Gizmo Glisten",
			"of the Gleaming Gem",
			"of the Gleaming Glade",
			"of the Guardian",
			"of the Glimmering Grove",
			"of the Gloomgrin",
			"of the Lost",
			"of the Hells",
			"of the Hidden",
			"of the Hithead",
			"of the Illuminatea",
			"of the Inventator",
			"of the Jaws",
			"of the Kooky",
			"of the Laughing Skull",
			"of the Loopy Legs",
			"of the Lost",
			"of the Lost Marbles",
			"of the Lunar Lantern",
			"of the Lunar Lurkers",
			"of the Lustrous",
			"of the Marblesharp",
			"of the Messenger",
			"of the Midnight Marauder",
			"of the Moonbarks",
			"of the Marauder",
			"of the Minion",
			"of the Mechanisers",
			"of the Muddy Mind",
			"of the Muddy Water",
			"of the Mystic",
			"of the Mushroom",
			"of the Nightshade",
			"of the Nocturnal",
			"of the Brawler",
			"of the Noodle",
			"of the Nosefinders",
			"of the Unbright",
			"of the Obsidian",
			"of the Oops",
			"of the Ownlaughs",
			"of the Phantom Pilferers",
			"of the Puzzle",
			"of the Quickfoot",
			"of the Quills",
			"of the Quirk Quiver",
			"of the Radiant Runner",
			"of the Raging",
			"of the Redhats",
			"of the Redsnow",
			"of the Rock Eaters",
			"of the Laters",
			"of the Rusty",
			"of the Scamp",
			"of the Shadow",
			"of the Shadowfriend",
			"of the Sharp Spear",
			f"of the {Descriptor(lusor)} Shade",
			"of the Squire",
			"of the Sinister",
			f"of the {Descriptor(lusor)}",
			f"of the {Descriptor(lusor)}",
			f"of the {Descriptor(lusor)}",
			f"of the {Descriptor(lusor)}",
			f"of the {Descriptor(lusor)}",
			f"of the {Descriptor(lusor)}",
			"of the Banana",
			"of the Raven",
			"of the Smarty",
			"of the Spring",
			"of the Sneaky Shadow",
			"of the Snouts",
			"of the Sock",
			"of the Spark",
			f"of the {Descriptor(lusor)}",
			f"of the {Descriptor(lusor)}",
			"of the Spicysnow",
			"of the Squirrel",
			"of the Stalker",
			f"of the {Descriptor(lusor)}",
			"of the Stuck",
			"of the Sunstare",
			"of the Swift",
			"of the Sylvan Servant",
			"of the Sylvan Shadow",
			"of the Talks Trees",
			"of the Tinker Twist",
			"of the Topsy Turvy",
			"of the Traphunters",
			"of the Tricky Tinkers",
			"of the Twilight Trickster",
			"of the Twilight Tricksters",
			"of the Twinkling Tender",
			"of the Twisted",
			"of the Umbral Ushers",
			"of the Veiled Vagabonds",
			"of the Vibrant Violet",
			"of the Vivid Valet",
			"of the Vortex Vandals",
			"of the Wacky",
			"of the Walked into Wall",
			"of the Where’s Hat",
			"of the Whimsy Ward",
			"of the Whispering Willow",
			"of the Whiz Whirl",
			"of the Wild Boar",
			"of the Witty",
			"of the Woozy",
			"of the Wraith Wanderers",
			"of the Wrong",
			"of the Yellowsnow",
			"of the Zany Zip",
			"of the Zigzag",
			f"of the {Descriptor(lusor)}",
			f"of the {Descriptor(lusor)} Dagger",
			f"of the {Descriptor(lusor)} Fire",
			f"of the {Descriptor(lusor)} Moon",
			f"of the {Descriptor(lusor)} Serpent",
			f"of the {Descriptor(lusor)} Shadow",
			f"of the {Descriptor(lusor)} Shadow",
			f"of the {Descriptor(lusor)} Skull",
			f"of the {Descriptor(lusor)} Tooth",
			f"of the {Descriptor(lusor)} Tree",
			f"of the {Descriptor(lusor)} Wolf",


			]
	if "Undead" in genus:
		origin += [
		"of the Ossuary",
		"from the Ossuary",
		f"of the {Descriptor(lusor)} Ossuary",
		"of the Mummy",
		f"of the {Descriptor(lusor)} Mummy",

		]

	origin += [
			"of Air",
			"of Dragons",
			f"of the {Descriptor(lusor)} Dragon",
			"of Earth",
			f"of the {Descriptor(lusor)} Earth",
			f"of the {Descriptor(lusor)} Heaven",
			"of Hell",
			f"of the {Descriptor(lusor)} Hell",
			f"of the {Rank(lusor)} Hell",
			"of Life",
			"of Light",
			f"of the {Descriptor(lusor)} Light",
			"of Nature",
			"of the Primal Essence",
			f"of the {Descriptor(lusor)} Essence",
			"of the Abbey",
			f"of the {Descriptor(lusor)} Abbey",
			"of the Abyss",
			"of the Abyssal Depths",
			"of the Academy",
			f"of the {Descriptor(lusor)} Academy",
			"of Ageless Wisdom",
			f"of {Descriptor(lusor)}  Wisdom",
			f"of the Ages",
			"of the Ancient Tribe",
			f"of the {Descriptor(lusor)} Tribe",
			f"of the Beast Realm",
			f"of the {Rank(lusor)} Realm",
			"of the Blackened Sky",
			f"of the {Descriptor(lusor)} Sky",
			"of the Blessed Waters",
			"of the Divine",
			"of Divine Will",
			"of Zeus' Will",
			"of Odin's Will",
			"of Thor's Will",
			"of Gods' Will",
			"of God's Will",
			"of King's Will",
			f"of {Rank(lusor)}'s Will",
			f"of the Dread Fortress",
			f"of the {Descriptor(lusor)} Fortress",
			"of the Elements",
			"of the Endless Night",
			f"of the {Descriptor(lusor)} Night",
			"of the Santa Campaña",
			"of the Eternal Chains",
			f"of the {Descriptor(lusor)} Chains",
			"of the Eternal Clock",
			"of the Eternal Watch",
			f"of the {Descriptor(lusor)} Watch",
			"of the Eternal Flame",
			f"of the {Descriptor(lusor)} Flame",
			"of the Ethereal Realm",
			f"of the {Descriptor(lusor)} Realm",
			"of the Fiery Lake",
			f"of the {Descriptor(lusor)} Lake",
			"of the Forbidden Arts",
			f"of the {Descriptor(lusor)} Arts",
			"of the Forbidden Knowledge",
			f"of the {Descriptor(lusor)} Knowledge",
			"of the Forbidden Throne",
			f"of the {Descriptor(lusor)} Throne",
			"of the Forces",
			f"of the {Descriptor(lusor)} Forces",
			"of the Fungal Forests",
			"of the Gale",
			"of the Glaciers",
			"of the Glade",
			"of Hellfire",
			f"of the {Descriptor(lusor)} Void",
			"of the Infernal Realm",
			f"of the {Descriptor(lusor)} Realm",
			"of the Inferno",
			f"of the {Descriptor(lusor)} Inferno",
			"of Lava",
			"of the Light",
			f"of the {Descriptor(lusor)} Light",
			"of Light",
			"of the Lost Library",
			f"of the {Descriptor(lusor)} Library",
			"of the Mythic Tale",
			f"of the {Descriptor(lusor)} Tale",
			"of Nature's Heart",
			"of the Netherworld",
			"of the Ninth Circle",
			"of Past and Future",
			"of the Primal Forest",
			f"of the {Descriptor(lusor)} Forest",
			"of the Realm",
			"of the Reptilian Marshes",
			"of the Road",
			f"of the {Descriptor(lusor)} Road",
			"of the Rocks",
			f"of the {Descriptor(lusor)} Rock",
			"of the Ruined Empire",
			"of the Old Empire",
			"of the Empire",
			"of the Gone Empire",
			"of the Rising Empire",
			f"of the {Descriptor(lusor)} Empire",
			"of the Searing Flame",
			"of the Shadowflame",
			"of the Shadows",
			f"of the {Descriptor(lusor)} Shadows",
			"of The Shapeless",
			"of the Slime Pits",
			"of the Spheres",
			"of the Sphere",
			f"of the {Descriptor(lusor)} Sphere",
			"of the Tempest",
			"of The Tempest",
			f"of The {Descriptor(lusor)} Tempest",
			f"of the Timeless Realm",
			f"of the {Descriptor(lusor)} Realm",
			"of The Tormented",
			"of the Unseen Terror",
			"of the Unseen",
			"of the Untamed Wilds",
			"of the Wailing Abyss",
			"of the Wild",
			"of the Woods",
			"of Water",
			"of the Dark Realm",
			f"of the {Descriptor(lusor)} Gods",
			f"of the {Descriptor(lusor)} Forest",
			"of the Enchanted Woods",
			"of the Eternal King",
			"of the Arcane",
			]
	result = random.choice(origin)
	return result

# To refactor:
def Title2(lusor):
	#	{Descriptor(lusor)}
	'''
of the Moon Paths
of the Moonlit Glades
of the Mystical Moons
of the Mythic Battles
of the Natural Springs
of the Night
of the Obscured Mysteries
of the Otherworldly Visions
of the Powerful Empires
of the Raven Queen

of the Unyielding Grasp
of the Warrior's Curse
of the Woodland Paths
Enchanter
Envoy
Protector
Ferret
Ghoul
Guardian
Hunter
Majestic Hunter
Marsh Leader
Mummy
Power
Ranger
Sailor Adventurer
Scout
Sea-Bound Marauder
Sentinel
Specter
Stardrake
Stout Fiend
Winter Marauder

fof the  Aura
fof the  Dragon
fof the  Dungeon
fof the  Fire
fof the  Kingdom
fof the  Realm
fof the  Sanctuary
fof the  Shadows
fof the {Descriptor(lusor)} Swarm
fof the {Descriptor(lusor)} Tomb
of the Ancient Tomb
of the Blazing Inferno
of the Blazing Spirit
of the Clever Creations
of the Curious Expeditions
of the Deathly Shadows
of the Ghostly Echoes
of the Haunted Halls
of the Scorching Heat
of the Small Wonders
of the Spectral Realm
of the Whimsical Gardens
Yellow
Artisan
Buzzing
Chitinous
Explorer
Guardian
Inventor
Marauder
Sage
Tinker
Acidic
Adventurous
Ambaric
Amber

Arcane
Arid
Awesome
Banished
Beast
Being
Blaze
Blazing
Blob
Bone
Botanical
Bull
Bullhead
Canine
Charismatic
Chronal
Cityzen
Claimant
Claimer
Clay
Collecting
Collector
Colossus
Conqueror
Construct
Constructed
Coral
Corrupted
Creator
Cunning
Darkened
Deadly
Deceptive
Deep
Deity
Descendant
Desert
Despairing
Destiny
Dragon
Dragonborn
Dune
Dutiful
Dweller
Dynamic
Earth Sage
Eclipse
Eclipsed
Ectoplasm
Elder
Electrifying
Elemental
Elementalborn
Ember
Enchanting
Energetic
Energy
Enforcer
Enigmatic
Eon
Firelord
Flame-Breather
fof the {Descriptor(lusor)}  Waves
fof the {Descriptor(lusor)} Ancestors
fof the {Descriptor(lusor)} Blood
fof the {Descriptor(lusor)} Bloodline
fof the {Descriptor(lusor)} Court
Force
Forgotten
Form Changer
Fury
Gargoyle
Ghostly
Golden
Golden Sun's
Goo
Greedy
Harvester
Heir
Hell's Seeker
Hive
Hoarder
Honorable
Horn
Horned
Illusionist
Illusive

Infernal
Inferno
Influential
King
Leader

Literate

Lovelorn
Lunar
Magenta
Massive
Maze
Menace
Monstrous
Mountain
Mythic
Obsessive
Ocean
of Destiny
of Energy
of Fate
of Fireborne Essence
of Greed
of Ice
of Innovation
of Moonlit Paths
of Secrets
of Souls
of the Ancient Earth
of the Ancient Faiths
of the Ancient Ruins
of the Ancient Tombs
of the Astral Realm
of the Blood Curse
of the Burning Heart
of the Charismatic Enchantment
of the Claimed Essences
of the Colossal Depths
of the Colossal Strength
of the Constructed Might
of the Crimson Moon
of the Cunning Illusion
of the Deep Oceans
of the Depths
of the Earthen Cores
of the Elemental Form
of the Enigma
of the Ethereal Planes
of the Fateweb
of the Feathered Wings
of the Fires
of the Forgotten Realm
of the Greedy Vaults
of the Guarded Treasures
of the Hoard
of the Icy Peaks
of the Illusionist Arts
of the Immortal Nights
of the Last Kingdom
of the Lost
of the Lost Souls
of the Lost Temples
of the Lunar Lakes
of the Malevolent Schemes
of the Manipulative Ploys
of the Mighty Peaks
of the Monument
of the Moonlit Woods
of the Mournful Whisper
of the Mythic Memories
of the Nocturnal Groves
of the Nocturnal Hunts
of the Obsessive Collections
of the Otherworld
of the Pained Existence
of the Peaks
of the Power Unleashed
of the Red Court
of the Revered Seas
of the Riddles
of the Rifts

of the Secrets
of the Shores
of the Silent Walk

of the Sorrowful Memories

of the Starry Skies
of the Stony Bastions
of the Storms
of the Streams
of the Thousand Guises
of the Throne
of the Unresolved Matter
of the Unyielding Earth
of the Vanished Worship
of the Veil
of the Void
of the Vortex
of the Waves
of the Wild Lands
of the Woodland Groves
of the {Descriptor(lusor)} Ancients
of the {Descriptor(lusor)} Labyrinths
of the {Descriptor(lusor)} Paths
of the {Descriptor(lusor)} Riddles
of Time
of Visions
of Wisdom
Offspring


of the  Scale Lairs
of the  Scaled Forges
Ox
Pale
Pathfinder
Phantom
Playful
Poison
Poisonous
Predator
Preserved
Primal
Progeny
Promethean
Promethus
Rainbow
 Scout
Scale Artisan
Scale Scout
Red
Regal
Revered
Riddle
Riddler
Rider
Rocky
Ruler
Runner
Sabertooth
Sand
Savage
Scale
Scion
Sea
Secure
Seductive
Seer
Shadowed
Shaper
Shift
Siren
Sludge
Solar
Sorrowful
Soul
Soulbound
Sovereign
Speaker
Speaking
Sphynx
Starry
Stellar
Stone
Sunlit
Swamp
Temporal
Tempting
Tentacled
Titan
Tomb
Translucent
Tricky
Twilight
Tyrant

Underdark
Unearthly

Unweavering

Venerable
Verdant
Versatile
Warden

Weaver
White


Wild Archer
Wise
Wraith
Acid
Adolescent
Adorable
Aged
Ageless
Agile Scout
Alluring
 Tracker
Arctic
Atemporal
Bloodsucker
Blue
Bunny
Child
Cold
Coolest
Count
Crop
Domestic
Drake
Druid
Elvenlady
Elvenlord
Feral Hunter
Fiend
fof the {Descriptor(lusor)} Depths
fof the {Descriptor(lusor)} Havens
fof the {Descriptor(lusor)} Nest
fof the {Descriptor(lusor)} Wonders

Frost
Glacial
Graceful
Hearth
Hearthbound
Hellbound
High Elf
Home
House
Housebound
Ice
Icebreath
Icy
Killer
Little
Lord
Lover
Merciless
Monarch
of Deserts
of Fire
of Forests
of the Fields
of the Forest
of the Frozen Wastes
of the Poisoned Woods
of the Thundering Skies
Old
Protective
Pursuer
Radiant Enchanter

Scales
Seducer
Seeker
Snow
Stalker
Strigoi
Tempter
Tiny
Tracker
Trickster
Vampire
Watcher
Wisdom
Witty
Wyrm
Elusive
Spirit-Walker
Transforming
Abbess
Academic
Academician
Aerial
Agile
Air
Analyst
Animated
Anointed
Aqua
Artificial
Artisan's
Artistic
Astute
Automated
Baleful
Bandit
Bender
Black
Blessed


Bloodsucking
Brave
Breeze
Brigand
Bronce
Brown
Brutal
Brutish
Captivating
Chronomaster

Chuthonic

City
Cleric
Clever
Colorful
Commander
Crafted
Creative
Cruel
Curious
Daring
Darkflame
Deacon
Deceiver
Demonic
descriptor +=  Chooser
descriptor +=  Lightning
descriptor += Abominable
descriptor += Aerial
descriptor += Airy
descriptor += Amorphous
descriptor += Amphibious
descriptor += Angry
descriptor += Animated
descriptor += Aquatic
descriptor += Armored

descriptor += Arrogant

descriptor += Artistic

descriptor += Ashen
descriptor += Astral
descriptor += Bark-Skinned
descriptor += Battle-Born
descriptor += Bear
descriptor += Beautiful
descriptor += Biblical
Blood-Sucking
descriptor += Brutal
descriptor += Brutish
descriptor += Burning
descriptor += Burrowing
descriptor += Cannibalistic
descriptor += Cavernous
descriptor += Chameleon
descriptor += Chaotic
descriptor += City
descriptor += Clever
descriptor += Clockwork
descriptor += Connective
descriptor += Corrupted
descriptor += Creeping
descriptor += Crystalline
descriptor += Cubic
descriptor += Cunning
descriptor += Cursed
descriptor += Dark
descriptor += Deathly
descriptor += Deepsea
descriptor += Desert
descriptor += Disciplinarian
descriptor += Discipline
descriptor += Divine
descriptor += Dune
descriptor += Elderly

descriptor += Elegant
descriptor += Elevated
descriptor += Enchanted
descriptor += Enchanting
descriptor += Enlightened
descriptor += Ethereal
descriptor += Exalted
descriptor += Feathered
descriptor += Frail
descriptor += Frost
descriptor += Frosty

descriptor += Fundamental

descriptor += Fungal

descriptor += Gargantuan

descriptor += Gelatinous
descriptor += Gentle
descriptor += Gentle Breeze
descriptor += Geometric
descriptor += Glowing
descriptor += Graceful
descriptor += Greedy


descriptor += Guardian
descriptor += Handsome
descriptor += Harmonious

descriptor += Haughty

Horned

descriptor += Hybrid

descriptor += Icy

descriptor += Infernal
descriptor += Isolated
Judgmental
descriptor += Judicial
descriptor += Just

descriptor += Large

descriptor += Lawful

descriptor += Lesser
descriptor += Lion-Scorpion
descriptor += Lycanthropic
descriptor += Majestic
descriptor += Maritime
descriptor += Mason
descriptor += Mature
descriptor += Mechanical
descriptor += Merry
descriptor += Minor
descriptor += Mischievous
descriptor += Misleading
descriptor += Modest
descriptor += Monstrous
descriptor += Mountainous
descriptor += Mournful
descriptor += Multi-headed
descriptor += Mysterious
descriptor += Mystical
descriptor += Mythical
descriptor += Native
descriptor += Nightmarish
descriptor += Nocturnal
descriptor += One-Eyed
descriptor += Pale
descriptor += Penitent
Petal
descriptor += Petrifying
descriptor += Powerful
descriptor += Predatory
descriptor += Primordial
descriptor += Prismatic
descriptor += Protective
descriptor += Pure
descriptor += Radiant
descriptor += Regal
descriptor += Regenerating
descriptor += Repentant
descriptor += Retaliatory
descriptor += Reveler
descriptor += Revenge-Seeking
descriptor += Rocky
descriptor += Rugged
descriptor += Saboteur
descriptor += Sacred
descriptor += Sapient
descriptor += Savage
descriptor += Scaled
descriptor += Screeching
descriptor += Sea-Bound
descriptor += Seeker

descriptor += Shadowed
descriptor += Shadowy
descriptor += Shape-Changing

descriptor += Shape-shifting

descriptor += Shell-Backed

descriptor += Skeletal

descriptor += Skyborne

descriptor += Slim

descriptor += Slimy

descriptor += Smithing

descriptor += Snow

descriptor += Stout

descriptor += Sturdy


descriptor += Subterranean
descriptor += Terrifying

descriptor += Thick
descriptor += Three-Headed
descriptor += Thunderous
descriptor += Tidal

descriptor += Tiny

descriptor += Titanic
descriptor += Traveling
descriptor += Tricky
descriptor += Twisted

descriptor += Two-Headed

Undying

descriptor += Venerable

descriptor += Vengeful

descriptor += Venomous

descriptor += Vibrant
descriptor += Vigilant
descriptor += Vigorous

descriptor += Wailing
descriptor += Wandering
descriptor += Warbred
descriptor += Weaver
descriptor += Weeping
descriptor += Werebeast
descriptor += Winged
descriptor += Wise
descriptor += Witch
descriptor += Youthful
Design
Diabolical
Dreadful

Earth
Eccentric
Elegant
Emissary
Enlightened
Epochal
Erudite
Expressive

Fearsome

Feral

Fey

Fierce
Firefiend
fof the {Descriptor(lusor)} Ballads
fof the {Descriptor(lusor)} Deal
fof the {Descriptor(lusor)} Dragon

fof the {Descriptor(lusor)} Enclaves

fof the {Descriptor(lusor)} Horde

fof the {Descriptor(lusor)} Lands

fof the {Descriptor(lusor)} Melody
fof the {Descriptor(lusor)} Pact
fof the {Descriptor(lusor)} Paths
fof the {Descriptor(lusor)} Peaks
fof the {Descriptor(lusor)} Performances
fof the {Descriptor(lusor)} Plan
fof the {Descriptor(lusor)} Roads
fof the {Descriptor(lusor)} Scheme
fof the {Descriptor(lusor)} Sky
fof the {Descriptor(lusor)} Tales
fof the {Descriptor(lusor)} Tribe
fof the {Descriptor(lusor)} Verses
fof the {random.choice(rank)}


Hellraiser
Hidden
Historian
Hydro


Lawless

Learned

Lyricist
Magma

Maleficent

Marine

Mechanical
Mechanized
Melodic

Mercilless

Monk

Musician

Naturalist
Necromancer
Oceanic
Ominous
origin += of Foreign Lands
origin += of the Abyssal Depths
origin += of the Abyssal Layers

of the Accursed Curse
origin += of the Acidic Pits
origin += of the Ageless Times
of the Alchemist's Lab

origin += of the Amphibious Marshes
origin += of the Ancient Epochs
origin += of the Ancient Halls
origin += of the Ancient Libraries
origin += of the Ancient Lore
origin += of the Ancient Myths
origin += of the Ancient Tombs
origin += of the Ancient Wishes
origin += of the Angelic Wings
origin += of the Angry Haunts
origin += of the Artistic Mischief
origin += of the Bark Forests
origin += of the Beautiful Faces

origin += of the Bewitching Charm
origin += of the Blazing Choirs
origin += of the Blazing Trails
origin += of the Blood-Soaked Fields
origin += of the Bloodied Stones
origin += of the Blossoming Fields
origin += of the Blossoming Gardens
origin += of the Bone Crypts
origin += of the Brutal Wars
origin += of the Burrowing Depths
origin += of the Cavernous Labyrinths
origin += of the Celestial Armies
origin += of the Celestial Courts
origin += of the Celestial Harmony
origin += of the Celestial Realm
origin += of the City Forges

origin += of the City Lights
origin += of the City Slums
origin += of the Clear Lakes
origin += of the Coastal Shores
origin += of the Colorful Forests
origin += of the Colossal Cliffs
origin += of the Coral Reefs
origin += of the Corrupted Depths
origin += of the Creeping Jungles
origin += of the Crossroad Journeys
origin += of the Cryptid Legends

origin += of the Crystal Caverns
origin += of the Crystal Mines
origin += of the Cubic Chambers
origin += of the Cunning Ambushes
origin += of the Cursed Battlefields

origin += of the Cursed Eternity

origin += of the Dancing Steel

origin += of the Dark Caverns

origin += of the Dark Corners

origin += of the Dark Depths

origin += of the Dark Forests
origin += of the Dark Swamps

origin += of the Dark Woods
origin += of the Deceptive Forms
origin += of the Deep Earth

origin += of the Deep Forests
origin += of the Deep Ocean
origin += of the Deep Seas
origin += of the Dense Jungles

origin += of the Departed Souls

origin += of the Desert Expanse

origin += of the Desert Wastes

origin += of the Dominating Reign

origin += of the Dragon Clans

origin += of the Dune Seas
origin += of the Eastern Mountains
origin += of the Echoing Mines

origin += of the Elderly Wisdom

origin += of the Elemental Origins

origin += of the Enchanted Chambers
origin += of the Enchanted Forests
origin += of the Enchanted Hearts

origin += of the Enchanted Woods

of the Energetic Nexus

			origin += of the Enlightened Forest

			origin += of the Eternal Flames
			origin += of the Ethereal Hunt
			origin += of the Ethereal Skies
			origin += of the Exotic Illusions

			origin += of the Fairy Rings
			origin += of the Fallen Heavens
			origin += of the Feathered Jungles
			origin += of the Feywild Realm
			origin += of the Fiery Forges
			origin += of the First Light
			origin += of the Fit Battalions
			origin += of the Flowing Rivers
			origin += of the Forbidden Spells
			origin += of the Four Elements
			origin += of the Frail Bodies
			origin += of the Frosty Peaks
			origin += of the Frozen Terrors
			origin += of the Frozen Tundras
			origin += of the Frozen Wastes

			origin += of the Fungal Depths
			origin += of the Fungal Forests
			origin += of the Gearworks
			origin += of the Gentle Winds

			origin += of the Geometric Spheres
			origin += of the Glowing Caves
			origin += of the Graceful Estates
			origin += of the Gray Wastelands
			origin += of the Great Hives
			origin += of the Greedy Depths
			origin += of the Half-Bloods
			origin += of the Handsome Visages
			origin += of the Harmonious Ponds
			origin += of the Haughty Tombs
			origin += of the Haunted Houses
			origin += of the Hearth and Home
			origin += of the Hidden Gold
			origin += of the Hidden Realm

			origin += of the High Clouds
			origin += of the High Courts
			origin += of the Higher Planes
			origin += of the Highest Order
			origin += of the Holy Choirs
			origin += of the Honorable Deeds
			origin += of the Hybrid Clans
			origin += of the Hybrid Forms
			origin += of the Icy Depths
of the Icy Wastes
			origin += of the Inexorable Justice
			origin += of the Infernal Courts
			origin += of the Infernal Forges
			origin += of the Infernal Gates
			origin += of the Infernal Legions

			origin += of the Infernal Order
			origin += of the Infernal Wastelands
			origin += of the Ingenious Contraptions
			origin += of the Inventive Labs
			origin += of the Isolated Isles
			origin += of the Large Clans
			origin += of the Lava Flows
			origin += of the Lawful Heavens
			origin += of the Lesser Realm
			origin += of the Lone Isles
			origin += of the Lost Love
			origin += of the Lost Loves
			origin += of the Lost Souls
			origin += of the Lost Treasures
			origin += of the Lush Groves
			origin += of the Mason's Hall

			origin += of the Militant Camps
			origin += of the Misleading Trails

of the Mixed Clans
			origin += of the Modest Communities
			origin += of the Moonlit Curse
			origin += of the Moonlit Forests
			origin += of the Mountain Caves
			origin += of the Mountain Clans
			origin += of the Mountain Nests
			origin += of the Mountain Peaks
			origin += of the Mournful Crypts
			origin += of the Muddy Banks

			origin += of the Multiverse
			origin += of the Mysterious East
			origin += of the Mystic Skies
			origin += of the Native Soil
			origin += of the New Frontiers
			origin += of the Night's Embrace
			origin += of the Nightmare Realm
			origin += of the Nightmarish Visions
			origin += of the Nine Hells
			origin += of the Nocturnal Forests
			origin += of the Nocturnal Mischief
			origin += of the Oceanic Voyages
			origin += of the Old Forest
			origin += of the Open Plains

			origin += of the Pale Shadows
			origin += of the Penitent Shadows
			origin += of the Petrifying Gaze
			origin += of the Playful Mischief

			origin += of the Poisoned Marshes

			origin += of the Powerful Armies

			origin += of the Rainbow Veil

			origin += of the Ritual Circles
			origin += of the Roaming Tribes

			origin += of the Rocky Highlands

			origin += of the Rocky Peaks

			origin += of the Rugged Cliffs

			origin += of the Rugged Lands

			origin += of the Rustic Festivals
of the Sacred Duties
			origin += of the Sacred Grounds

			origin += of the Sacred Groves

			origin += of the Sacred Vaults

			origin += of the Sapient Colonies

			origin += of the Savage Lands

			origin += of the Savage Wastes

			origin += of the Scorching Deserts
			origin += of the Scorching Sands
			origin += of the Seductive Powers
			origin += of the Shadowed Alleys
			origin += of the Shadowed Depths
			origin += of the Shadowed Paths
			origin += of the Shadowfell
			origin += of the Shadowy Depths
			origin += of the Shadowy Veil
			origin += of the Shapeless Forms
			origin += of the Shell-Covered Shores
			origin += of the Shielded Realm
			origin += of the Shifting Forms
			origin += of the Sinful Mysteries
			origin += of the Sky Castles
			origin += of the Sky Dominions
			origin += of the Slain Heroes

			origin += of the Slim Figures
			origin += of the Slippery Slopes
			origin += of the Smithing Halls
			origin += of the Snow Fields

			origin += of the Soaring Heights

			origin += of the Solar Flames

			origin += of the Sorrowful Places

			origin += of the Spiked Tails
			origin += of the Spiky Deserts

			origin += of the Starry Expanse
			origin += of the Starry Heavens
			origin += of the Sticky Floors

			origin += of the Stoic Mountains

			origin += of the Stone Gaze

			origin += of the Stony Mountains

			origin += of the Suffering Shadows

			origin += of the Sunken Cities

			origin += of the Sunlit Glades

			origin += of the Swamp Lands

			origin += of the Swamp Waters

			origin += of the Sylvan Groves

			origin += of the Tangled Wires
			origin += of the Thundering Skies
			origin += of the Tidal Forces
			origin += of the Toxic Wastes
			origin += of the Traveling Caravans
			origin += of the Twilight Forests
			origin += of the Twisted Jungle
			origin += of the Two Minds
			origin += of the Unbreakable Bonds
			origin += of the Underdark Realm
			origin += of the Unformed Swamps
			origin += of the Unrestful Graves
			origin += of the Untamed Lands
			origin += of the Venerable Groves
			origin += of the Vengeful Shadows
			origin += of the Vibrant Canopies
			origin += of the Vigorous Fields

			origin += of the Volcanic Vents
			origin += of the Wailing Moors
			origin += of the Wailing Winds
			origin += of the Wandering Tribes
			origin += of the War Forges
			origin += of the War Torn Lands
			origin += of the Warbred Legions
			origin += of the Wastelands
			origin += of the Wealthy Vaults
			origin += of the Webbed Dominions
			origin += of the Weeping Moors
			origin += of the Weeping Rivers
			origin += of the Whispering Forests
			origin += of the Whispering Woods

			origin += of the Wild Jungles
			origin += of the Wild Lands
			origin += of the Woodland Glades
			origin += of the Woodland Glens
			origin += of the Youthful Spirit
			Outlaw
			Overlord
			Pebble
Performer
Poetic
Primitive
Prince
Pyro
Raider
rank +=
rank +=  Diplomat
rank += Abominable Snowbeast
rank += Accursed Soul
rank += Acidic Sludge
rank += Adventurous Pioneer
rank += Airy Dancer
rank += Amorphous Mass
rank += Amphibious Scout
rank += Ancient Nephilim
rank += Ancient Treant
rank += Angel
rank += Angry Spirit
rank += Aquatic Predator
rank += Archdevil

rank += Archon Judge
rank += Ascended Master
rank += Ashen Blob

Bark Guardian

rank += Battle Maiden

rank += Bear Guardian

rank += Beautiful Bard

rank += Bloom
rank += Botanical Curator
rank += Brass Diplomat
rank += Brawny Ettin
rank += Breeze Keeper
rank += Bronze
rank += Brutal Warlord
rank += Bugbear Stalker
rank += Burrowing Terror
rank += Cannibalistic Fiend
rank += Cap
rank += Cavern Chief
rank += Celestial
rank += Celestial Commander
rank += Celestial Kirin

rank += Celestial Serpent

rank += Celestial Wanderer

rank += Chameleon Scout

rank += City Chief

rank += City Craftsman

rank += Cloud Monarch

rank += Colossal Leviathan

rank += Corrupted Forge Lord
rank += Creeping Vine
rank += Crossroad Explorer

rank += Cryptid Predator

rank += Crystalline Mass

rank += Crystalline Miner

Cubic Mass

rank += Cunning Fiend
rank += Cunning Goldsmith
rank += Cursed Wanderer
rank += Dark Enchanter
rank += Dark Sludge
rank += Dark Trickster

rank += Deepsea Sovereign
rank += Demon Lord
rank += Desert Raider
rank += Desert Survivor
rank += Despairing Wraith
rank += Deva
rank += Draco Guardian
rank += Dragon Apprentice
rank += Dragonkin
rank += Drake Hunter
rank += Dutiful Specter
rank += Earthen Slime
rank += Elderly Sage
rank += Elf
rank += Enchanting Dryad
rank += Enchantress
rank += Enforcer of Agreements

rank += Enlightened Tree
rank += Ethereal Spirit
rank += Farmer
rank += Feathered
rank += Feathered Scout
rank += Ferocious Alpha
rank += Fiery Blob
rank += Fiery Smith
rank += Foreign Traveler
rank += Forest Wanderer
rank += Frail Hermit
rank += Frost Monarch
rank += Frosty Ranger
rank += Fundamental Force
rank += Fungal Growth
rank += Fungal King

rank += Galactic Sovereign
rank += Gear Artisan
rank += Gel
rank += Gelatinous Blob
rank += Gem Guardian
rank += Genie Lord
rank += Geometric Keeper
rank += Ghostly Light
rank += Giant
rank += Glacial Master
rank += Goliath Champion
rank += Graceful Diplomat
rank += Greedy Keeper
rank += Guardian
rank += Guardian Defender
rank += Guardian Shade
rank += Guardian Spirit

rank += Handsome Courtier
rank += Harpy Queen
rank += Haughty Wight
rank += Hearth Guardian
rank += High Lord
rank += Hobgoblin Captain
rank += Hybrid Terror
rank += Icy Blob
rank += Icy Tracker
rank += Impish Spy
rank += Infernal Commander
rank += Infernal Forgemaster
rank += Infernal Judge
rank += Infernal Overlord
rank += Infernal Pack Leader
rank += Infernal Punisher
rank += Infernal Rider

rank += Infernal Scion
rank += Infernal Warlord
rank += Inventive Engineer
rank += Isolated Chief
rank += Jackal Lord
Knight
rank += Knowledgeable Skull
rank += Large Leader

rank += Lava Creator
rank += Lesser Deity
rank += Lichen
rank += Local Merchant
rank += Lovelorn Ghost
rank += Lycan Alpha
rank += Mage
rank += Majestic Flyer
rank += Maritime Captain

rank += Master Mason
rank += Master of Disguise
rank += Master Saboteur
rank += Master Tinker
rank += Merry Piper
rank += Mighty Behemoth
rank += Mind
rank += Mine Knocker
rank += Mischievous Rascal
rank += Mountain Artisan
rank += Mountain King
rank += Mountain Warlord
rank += Moving Chair
rank += Muse of the Arts
rank += Mushroom
rank += Mysterious Stranger

rank += Mystic
rank += Mystic Shifter

rank += Mystic Tempter
rank += Mythical Giant
rank += Nightmarish Entity
rank += Nocturnal Lord
rank += Nodal Guardian
rank += Nomad
rank += Nymph
rank += Ocean Sovereign
rank += Ocean Terror
rank += Ogre Warlord
rank += Oni Warlord
rank += Overlord
rank += Pack Alpha
rank += Pale Stalker
rank += Pan Piper

rank += Patron Deity
rank += Penitent Specter
rank += Petal Guardian
rank += Petrifying Serpent
rank += Pixie Trickster
rank += Planar Wanderer
rank += Playful Spirit
rank += Poisonous Mass
rank += Powerful Soldier
rank += Primal Force
rank += Prismatic Sovereign
rank += Rat King
rank += Redcap Slayer
rank += Repentant Spirit
rank += Retaliatory Force
rank += Revenge-Seeking Spirit
rank += River Nyk

rank += Roaming Artisan
rank += Rocky Guardian
rank += Rocky Titan
rank += Rugged Outlander
rank += Sacred Totem
rank += Savage Manticore
rank += Scholar
rank += Scorpion King
rank += Scout
rank += Screeching Fiend
rank += Sea Giant King
rank += Seducer
rank += Sentinel
rank += Seraph
rank += Seraphim Guardian
rank += Serpent
rank += Shadow Steed

rank += Shadow Trow
rank += Shadowed Miner
rank += Shadowy Terror
rank += Shadowy Wraith
rank += Shark Lord
rank += Shell-Backed Protector
rank += Sin Examiner
rank += Sinister Enchanter
rank += Sky Eye
rank += Slim Scholar
rank += Slimy Menace
rank += Smithing Master
rank += Snow Chief
rank += Solar Guardian
rank += Soul Collector
rank += Soul Harvester
rank += Sovereign

rank += Spiky
rank += Spirit of Revenge
rank += Sticky Trap
rank += Stone Curse Bringer
rank += Storm Dragon




Mass
Oak
of Cattle
of Cities

of Skies
of the Ancient Woods
of the Ethereals
of Towns
Painter
Poet
Sculptor
Trap

Tree
Willow


Fearless Raider

for color in Colors:
Goblin
if lusor.gender == he:
Mighty Berserker
of the Abodes
of the Hearth
of the Hearths

of the Home
of the Housebound Mysteries
origin += of the Crafted Realm
origin += of the Dark Wilderness
origin += of the Deep
origin += of the Deep Woods
origin += of the Eternal Flame
origin += of the Forgotten Crypts
origin += of the Fundamental Forces
origin += of the Hidden Workshops
origin += of the Mountain Halls
origin += of the Orde
origin += of the Rural Lands
origin += of the Shadowy Nooks
origin += of the Solar Flares
origin += of the Titans
origin =
origin = of the Hidden Hideouts
rank += Dawnlord
rank += Djinn

rank += Elder
rank += Elementalist
rank += Giant Chieftain
rank += Gnome
rank += Goblin Chief
rank += Hunter
rank += Lord
rank += Monstrous Overlord
rank += Sunlord
rank += Titan
rank += Tribe Leader
rank += Wandering Leader
rank += Warden

rank =
rank = Bandit Leader
Savage Fighter
Skeletal
Untamed Conqueror
#	{Descriptor(lusor)}


Honest
Toxic

Abbott

Abominable

Abominable Presence

Abyss Watcher

Abyssal Guardian
Abyssal Monster
Abyssal
Abyssal Ruler
Acid Spitter
Acidic Pool
Acolyte
Adaptive
Adhesive
Adhesive Mass
Adventurous Creator

Adventurous Scout

Adventurous Wanderer

Aerial Scout
Afterlife Guardian
Aged Mentor
Aggressive
Aggressive Pudding
Agile Hunter
Agile Predator
Ailing
Ailing Mystic
Air Cutter
Airborne

Airy
Airy Spirit
Albino
Albino Hunter

Alchemical
Alchemical Being

Alive
Alive Willow
Alley Master
Allure
Alluring Fiend
Alluring Performer
Alluring Traveler
Amulet Warden

Analytical
Analytical Inquirer
Ancestral
Ancient Drake
Ancient Hoarder
Ancient Intellect
Ancient Mariner
Ancient Tree
Angelical
Animated Carpet
Anubis Kin
Apostolic
Aquatic Trickster
Arachnid Sage
Arbiter
Arcane Sovereign

 Archivist
 Archon


 Arctic Force
 Armored Guardian
 Armored Watcher
 Artisan of Rock
 Ascendant
 Astral Force
 Astral Keeper

 Astronomer
 Atoning
 Atoning Spirit
 Attractive
 Auroral
 Auroral Guardian
 Auroral Spirit
 Baron
 Battle Construct
 Beast Chieftain
 Beast Master
 Beast Shifter
 Beastly

 Beastly Sovereign
 Beauty
 Behemoth Keeper

 Benevolent

 Benevolent Wraith
 Biblical Titan
 Binding Fiend
 Blaze Master
 Blazing Colossus
 Blazing Puddle
 Blood
 Blood-Sucking Fiend
 Bloodthirsty Fiend

 Bloodthirsty Predator
 Bloody
 Blossoming
 Blossoming Inventor
 Blossoming Wanderer
 Bog
 Bold
 Bold Leader
 Bone Gnawer

 Bone Warden
 Bookish

 Bound
 Bound Sentinel
 Bound Spirit
 Boundary Sentinel
 Boundary-Crosser
 Boundless
 Brash
 Brash Firebrand
 Brass-Scaled
 Brawny
 Bright
 Bright Archer
 Bronze-Scaled
 Brute
 Brutish Ambusher
 Brutish Behemoth
 Brutish Fiend
 Bug Sage
 Bulk
 Bulk Trader
 Burning
 Burning Gel
 Calculating
 Camouflaged
 Canine Seer
 Canyon
 Capped
 Captain
 Carved
 Carved Elder
 Carver
 Carver of Runes
 Caustic

 Caustic Mass
 Celestial Horse
 Celestial Judge

 Celestial Lawkeeper
 Celestial Offspring
 Celestial Wanderer
 Champion
 Chaos Bringer

 Chaotic
 Chaotic Marauder
 Chaplain
 Charismatic Outcast

 Charmcaster
 Charmcaster Fiend
 Charmer
 Charming Artist
 Charming Minstrel
 Charmweaver
 Cherub
 Chieftain
 Chill
 Chill Sentinel
 Chilling
 Chilling Lord
 Chilling Slime

 Chosen
 Chromatic
 Chromatic Guardian
 Civic
 Civic Leader
 Civilized
 Civilized Commander
 Clan Leader
 Clay Mass
 Clever Guardian
 Clever Outlaw
 Clever Rogue
 Cliffside
 Clingy
 Clingy Blob
 Clockwork

 Cloud Dancer
 Cloud Roamer
 Coastal
 Cold-Resistant
 Cold-Resistant Hunter
 Coldblood
 Colony Master
 Colorful Hunter
 Colossal Beast
  Sea Beast

 Colossus Master
 Colossus Ruler

 Commanding

 Commanding

 Conflicted

 Conflicted Behemoth

 Conjurer

 Connective Spirit
 Conquering Fiend

 Conqueror Hero

 Consuming

 Consuming Horror
 Contract Maker
 Contrite

 Contrite Phantom

 Coordinator

 Copper

 Core

 Core Essence
 Core Shaper
 Core Spirit
 Corroting
 Corrupted Vine
 Cosmic
 Cosmic Drake
 Cosmic Voyager
 Cover
 Crafted Assistant
 Craftsman
 Crafty Artisan
 Crafty Inventor
 Crafty Thief
 Crafty Underminer
 Cranial
 Cranial Sage

 Crimson
 Croaking
 Crossroad
 Crowned
 Cryptic
 Cryptid
 Crystalline Gel
 Cultured
 Cultured Diplomat
 Cultured Scholar
 Cunning Goblin
 Cunning Hag


 Cunning Strategist

 Curate
 Curator

 Cursed

 Cursed Monstrosity
 Cursed Wanderer
 Dark Enchantress

 Dark Gatherer
 Dark Ocean Lord
 Dark Phantom
 Dark Shinigami
 Dark Trickster
 Dark Wanderer
 Dark-Touched

 Darkwater
 Darkwater Guardian
 Dawn Herald
 Daykeeper

 Daylight Keeper
 Daystar
 Daystar Keeper
 Deadly Basilisk
 Deadly Hunter
 Death Dealer
 Deathly
 Deathly Harbinger
 Deathly Herald
 Decaying
 Decaying Mass
 Deceiver of the Woods

 Deceptive Beauty
 Deceptive Mimic
 Deceptive Phantom
 Deceptive Wyrm
 Decimator
 Deep Hunter
 Deep Miner
 Deep Sea Terror

 Deepblue
 Deepsea
 Deepsea Guardian

 Demon Ogre
 Demonic Chieftain
 Demonic Pack Leader
 Demonic Trickster
 Dense
 Dense Mass
 Desert Dweller
 Desert Guardian
 Desert Prowler
 Desert-Born
 Desert-Born Wanderer
 Detective
 Detective of Deceit
 Determined
 Determined Pursuer
 Devil
 Devious
 Devious Saboteur
 Devout
 Dimensional
 Dimensional Guardian
 Discipline Keeper
 Distant
 Distant Wanderer
 Divine

 Divine Agent
 Divine Aspect
 Divine Being
 Divine Champion
 Divine Emissary
 Divine Giant

 Divine Herald
 Divine Ruler
 Divine Watcher
 Divineborn
 Djinn

 Domestic Keeper
 Dominant
 Dominant Hunter

 Doombringer

 Draconic

 Draconic Scion
 Dread
 Dreaded

 Dreaded Leviathan

 Dual-Nature

 Dual-Nature Chief

 Dual-Natured

 Dual-Natured Colossus

 Duke
 Dull
 Dull Mass

 Duplicitous

 Duplicitous Phantom

 Dutiful Shade

 Eager
 Eager Flyer
 Eagle-Lion
 Eagle-Lion Ruler
 Earthbound
 Earthen Guardian
 Earthy Innovator
 Echoing
 Echoing Fighter
 Echoing Spirit
 Eerie
 Eerie Imposter
 Eight-Legged
 Eldritch
 Eldritch Horror
 Electric Monarch
 Electric Serpent
 Elegant Fiend
 Elemental Founder
 Elemental Root
 Elemental Sage
 Elevated One
 Elite
 Elusive Beast

 Elusive Guide
 Elusive Phantom
 Elusive Wanderer
 Emberheart
 Eminent
 Eminent Ruler
 Empty Helm
 Enchanted Being
 Enchanted Fiend
 Enchanted Guardian
 Enchanted Saber
 Enchanted Wardrobe
 Enchanting Sorceress
 Enduring
 Enduring Wanderer
 Energetic Apprentice
 Energetic Performer
 Energetic Weaver
 Engulfing
 Engulfing Cube
 Enigmatic Master
 Enigmatic Performer
 Ent
 Entangling
 Entangling Guardian
 Entrancing
 Entrancing Demon
 Envy
 Erosive
 Erosive Ooze
 Essence
 Essence Keeper
 Eternal Aspect
 Eternal Hunger
 Eternal Paramour

 Eternal Seeker
 Eternal Spirit
 Eternal Wanderer
 Ethereal Deceiver
 Ethereal Drake
 Ethereal Guardian
 Ethereal Horror
 Ethereal Lord
 Ethereal Messenger

 Ethereal Mourner
 Ethereal Phantom
 Ethereal
 Ethereal Reaper
 Ethereal Reaver
 Ethereal Sentinel
 Ethereal Spirit

 Ethnographer

 Exalted

 Exalted Spirit

 Exiled

 Exotic

 Exotic Enchanter

 Exotic Merchant

 Explorative

 Explorative Pioneer

 Explorer Captain
 f Claw
 f Crest Shaman

 f Crested
 f Eyed
 Faithful
 Familiar
 Familiar Face

 fArcane
 fArcane  Sage

 Fascinating
 Fascinating Outsider
 Fate Spinner

 Fear-Inducer

 Fear-Inducing

 Fearful

 Fearful Apparition

 Fearsome Beast
 Fearsome Cavalier
 Fearsome Commander

 Fearsome Fomorian
 Fearsome Harpy
 Fearsome Hunter
 Fearsome Predator


 fEnigmatic
 fEnigmatic  Trickster
 Feral Beast
 Feral Leader
 Feral Lord
 Feral Overseer
 Ferocious
 Ferocious Brute
 Festive
 Festive Companion
 Fetching

 Fetching Trader
 Field
 Fiendish Diplomat
 Fierce Flyer
 Fierce Hunter
 Fierce Marauder
 Fierce Monarch
 Fierce Raider
 Fierce Watchdog
 Fiery Artisan

 Fiery Earth Ruler
 Fiery Horseman
 Fiery Titan
 Fighter
 Fire Talker
 Fire-Touched
 Firemind
 Flame Master
 Flame of God

 Flame Warden
 Flighty
 Flighty Wanderer
 Floral
 Floral Artisan
 Flower
 Fluidic
 Fluidic Ooze
 fLustrous
 fLustrous  Sage
 Flying
 Flying Blade
 fMetallic

 fMetallic  Guardian
 fMystical
 fMystical  Enchanter
 fof the  Claw Clans
 fof the  Crest Packs
 fof the  Eye Covens
 fof the Lustrous  Libraries
 fof the Metallic  Bastions
 fof the Shining  Workshops
 Force Wielder
 Forest Dweller
 Forest Nymph
 Forest Reveler

 Forest Sovereign
 Forest Warden
 Forged
 Forged Fighter
 Forger
 Forlorn
 Forlorn Ghost
 Formless
 Formless Devourer
 Forsaken
 Fossilized
 Fossilized Guardian

 Fragrant
 Fragrant
 Free Spirit
 Fresh
 Fresh Talent
 Frosty
 Frosty Behemoth
 Frosty Guardian
 Frozen
 Frozen Ooze
 Frozen Sovereign
 fShining

 fShining  Smith
 Fungal

 Fungi
 Furnish
 Furry
 Furry
 Galactic
 Garden Keeper
 Gardener
 Gargantua Ruler
 Gargantuan
 Gaunt
 Gaunt Predator
 Gear-Driven
 Gem
 Gem Blob
 Gemstone
 Gentle
 Gentle Breeze
 Gentle Gust Guardian
 Gentle
 Ghastly Wraith
 Ghost
 Ghostly Screamer
 Ghostly Wanderer

 Giant
 Giant Tree
 Glacial Mass
 Gleaming
 Gleaming Carver
 Gloomy
 Gloomy Forger
 Gloomy Specter
 Goblin's
 Gold-Loving
 Gold-Loving Mischief

 Graceful Dancer
 Gravetaker
 Grecian
 Grecian Titan
 Greed
 Green Artisan
 Green Wanderer
 Green-Thumb
 Green-Thumb Tinker
 Gremlin Engineer
 Grim Collector

 Grounded
 Grounded Ruler
 Grovekeeper
 Growing

 Growing Drake

 Gruff

 Gruff Miner
 Guardian
 Guardian God

 Guardian of Bones

 Guardian of Graves

 Guardian of Order
 Guardian of the Gates

 Guardian of the Home

 Guardian of Wealth

 Half-Goat
 Half-Goat Wanderer
 Half-Infernal
 Half-Scaled
 Half-Wyrm
 Harbinger
 Hardy
 Hardy Sailor
 Hat
 Hatchling
 Haunting
 Hazardous

 Hazardous Goo
  of Forests
 Healing
 Heartbroken
 Heartbroken Specter
 Heartbroken Wraith
 Heaven-Touched
 Heavenly
 Heavenly Arbiter
 Heavenly Force
 Heavenly Guardian
 Heavenly
 Heavenly Scion
 Hefty
 Hefty Brawler
 Hellbound Locator
 Hellbound Rider

 Hellish Arbiter

 Hellish Disciplinarian

 Hellish General

 Helm Watcher

 Hermit

 Hero Escort

 Heroic
 Hidden Dweller
 High
 Highest
 Highland
 Highland Brewer
 Highland Leader
 Holy

 Holy
 Homegrown
 Homegrown Hero
 Honorable Defender
 Honorable
 Honorable Wraith
 Hoofed Sage
 Horizon Walker
 Horned Dancer
 Horned Nomad
 Horned Trickster
 Horrifying
 Horrifying Spirit

 Howling
 Howling Apparition
 Howling Phantom
 Humble
 Humble Divinity
 Humble Godling
 Hungering
 Hungering Undead

 Hungry
 Hybrid
 Hybrid Guardian
 Hyena

 Hyena Demon
 Hyena Warlord
 Hypnotic
 Hypnotic Seducer
 Icy Horror
 Icy Jotunn
 Icy Leviathan

 Icy Predator
 Icy
 Icy Raider
 Icy Scout
 Icy Slush
 Igneous
 Igneous Guardian
 Illuminated
 Illuminated Emissary
 Immortal Count
 Immovable
 Immovable Lord
 Imperious

 Imperious Undead
 Implacable

 Implacable Phantom
 Imposing
 Industrious
 Industrious Worker
 Inexorable
 Inexorable Punisher
 Infernal Count
 Infernal Investigator
 Infernal Judge
 Infernal
 Infernal Tracker
 Infernoborn

 Ingenious

 Ingenious Mechanic
 Inky
 Inky Blob
 Innovative Artisan
 Innovator Sage
 Inquisitive
 Inscribed

 Insightful
 Instructor
 Intangible
 Intangible Horror
 Interlinked
 Interlinked Emissary



 Inventive Mischief-Maker

 Justice Bearer
 Justiciar of Flames
 Knight

 Knowledgeable

 Lady
 Lamenting
 Lamenting Spirit

 Land Shark
 Lava Sludge
 Lawbringer
 Lawful
 Leaf
 Leafy
 Leafy Scout
 Lean
 Lean Runner

 Leaping
 Learned Scholar
 Legendary
 Legendary Behemoth
 Lesser
 Lethal

 Lethal Lizard
 Librarian

 Light
 Light Sprite

 Lightbringer
 Lightning Tyrant
 Lightning Wielder
 Lightning-Wielder
 Lightweaver
 Linguist
 Lion-Scorpion Predator
 Little Guardian
 Lively
 Lively Performer
 Living Decor
 Local

 Lofty
 Lofty Sovereign
 Logician
 Lorekeeper
 Lotus

 Lovely
 Lovely Poet
 Luminescent

 Luminous
 Luminous Explorer
 Luminous Guardian

 Luminous Phantom

 Luminous Wyrm
 Lurking
 Lurking Brute
 Lust
 Lustrous
 Lustrous Drake
 Machine
 Maiden
 Majestic
 Majestic Coiler
 Majestic Flyer
 Majestic Titan
 Malefic
 Malefic Smith
 Malevolent Crone
 Malevolent Growth
 Malevolent Schemer
 Malevolent Trickster
 Man-Eating
 Man-Eating Brute
 Manipulator
 Marine Sovereign
 Maritime
 Maritime Raider
 Marsh
 Mastermind
 Matron
 Mausoleum
 Mausoleum Warden
 Mechanical Fiend
 Mechanical

 Mechanical Marvel
 Mechanical Regulator
 Menacing
 Menacing Beast
 Menacing Brute

 Menacing Hunter
 Menacing Leader
 Menacing Phantom
 Menacing Terror
 Merchant
 Merciless Brigand
 Merry
 Merry Wanderer
 Messenger
 Messenger of Light
 Metal-Bound
 Metallic
 Metallic Forger
 Metaphysicist

 Metropolitan
 Metropolitan Artist
 Mighty Ancestor
 Mighty Behemoth
 Mighty Champion
 Mighty Enforcer
 Mighty Hunter
 Mighty Overlord
 Migratory Chieftain
 Militant
 Militant Leader
 Mimic
 Mindless
 Mindless Horror
 Mine-Dwelling
 Miner
 Miniature
 Miniature Helper
 Minor Divinity
 Miracle-working
 Mire

 Mire Chieftain
 Mischevious
 Mischevious Agent
 Mischief-Maker
 Mischief-Making Fiend
 Mischievous
 Mischievous Fairy
 Mischievous Fiend
 Mischievous Ghost
 Mischievous Goblin
 Mischievous Imp
 Mischievous Trickster

 Misleading Glow
 Missionary
 Mistress
 Mixed
 Mixed Blood
 Modron Monitor
 Molten
 Molten Ooze
 Molten Shaper
 Monochrome
 Monochrome Sludge

 Monstrous Behemoth
 Monstrous Fiend
 Monstrous Predator
 Monstrous Shark
 Monumental
 Monumental
 Moon Howler
 Moon Stalker
 Moon-Caller
 Moon-Howler
 Moss
 Mountain Dweller

 Mountainous
 Mournful
 Mournful Phantom
 Mournful Shade
 Mournful Wraith
 Muck
 Muddy Blob
 Multi-Headed Beast

 Mummified
 Murderous
 Murderous Goblin
 Muscular
 Muscular Laborer
 Musical
 Musical Satyr
 Muspelheim
 Muspelheim Ruler
 Musty
 Musty Mold
 Mycelial
 Mysterious Enchanter

 Mysterious Impersonator
 Mysterious Miner
 Mysterious Water Spirit
 Mysterious Wayfarer
 Mystic Coil
 Mystic Drake
 Mystic Effigy
 Mystic Ruler
 Mystic Sage

 Mystic Shaper
 Mystic Steed
 Mystic Walker
 Mystic Wyrm
 Mystical Blob
 Mystical Guardian
 Mystical Sovereign
 Mythic Giant
 Mythical
 Mythical Fiend
 Mythical Horror

 Mythical Medusa
 Native Artisan
 Nature Guardian
 Nature Tinker
 Nature's
 Nature's Bard
 Nature's Child
 Nature's Essence
 Nature's Herald
 Nature's Sentinel
 Nature-Bound
 Nature-Loving

 Nature-Spirit

 Naturebound

 Nautic
 Navigator

 Necrotic

 Nest

 Night Prowler

 Nightmare Lord

 Nightwalker

 Nimble
 Nimble Navigator

 Nocturnal Goblin
 Nocturnal Terror
 Nodal
 Noisy
 Noisy Phantom

 Nomad

 Nomadic Tinker

 Norse
 Norse Colossus
 Norse Titan
 Nun

 Nymph
 Oblivion Sire
 Observation Sentinel
 Obsidian
 Obsidian Mass
 Ocean Sage
 Oceanian
 Oceanic Force
 Oceanic Ruler
 of Distant Shores

 of Exotic Cultures
 of the Abominable Lands
 of the Absorbing Mires
 of the Abyssal Trenches
 of the Abyssal Waters
 of the Acidic Mists
 of the Acidic Springs
 of the Acidic Waters
 of the Adaptive Underbrush
 of the Adhesive Walls

 of the Adolescent Roost

 of the Adventurous Expeditions

 of the Adventurous Paths

 of the Adventurous Roads
 of the Adventurous Trails
 of the Aerial Dominions
 of the Aged Histories
 of the Aggressive Attacks
 of the Agile Branches
 of the Agile Hunts
 of the Ailing Souls
 of the Airborne Assault
 of the Airy Flights
 of the Airy Heights
 of the Albino Enclaves

 of the Alchemical Mysteries
 of the Alluring Abyss
 of the Alluring Brooks
 of the Alluring Jungles

 of the Alluring Night

 of the Alluring Stages

 of the Amorphous Depths
 of the Amorphous Expanse
 of the Amulet's Bond
 of the Analytical Pursuits

 of the Ancestral Spirits

 of the Ancient Canopy

 of the Ancient Deserts

 of the Ancient Forests
 of the Ancient Groves
 of the Ancient Lycanthropy
 of the Ancient Mysteries
 of the Ancient Oceans
 of the Ancient Rites
 of the Ancient Scrolls
 of the Ancient Skies

 of the Ancient Technologies
 of the Ancient Vaults
 of the Ancient Waters
 of the Animated Abodes
 of the Aquatic Havens
 of the Aquatic Realm
 of the Arcane Mysteries
 of the Arcane Secrets
 of the Arctic Expanse
 of the Arctic Realm
 of the Arid Wastelands
 of the Armored Claws

 of the Armored Guardians
 of the Artificial Life
 of the Artisan Guilds
 of the Artisan's Workshop
 of the Ashen Bogs
 of the Ashen Mires
 of the Astral Planes
 of the Astral Studies
 of the Atoning Souls
 of the Attractive Galleries
 of the Auroral Lights
 of the Automated Legions
 of the Banished Realm

 of the Battlefields
 of the Bear Clans
 of the Beastly Dominions
 of the Beastly Hunts
 of the Beastly Realm
 of the Behemoth's Roar
 of the Benevolent Guidance
 of the Benevolent Watch
 of the Bewitching Spells

 of the Biblical Lands
 of the Binding Oaths
 of the Blazing Fields
 of the Blazing Mountains
 of the Blood Coven
 of the Blood-Sucking Myths
 of the Bog Territories
 of the Bold Ventures

 of the Botanical Wonders
 of the Bound Duties
 of the Bound Duty
 of the Boundary Edges
 of the Boundless Realm
 of the Brass Sands
 of the Brawny Mountains
 of the Breezes
 of the Bright Skies
 of the Bronze Cliffs
 of the Brutish Clans
 of the Brutish Territories
 of the Bulk Markets

 of the Burning Lakes
 of the Buzzing Swarms
 of the Calculating Minds
 of the Camouflaged Terrains
 of the Canine Packs
 of the Cannibalistic Legends
 of the Canyon Depths
 of the Carved Forests
 of the Carved Mountains
 of the Caustic Swamps
 of the Caverns
 of the Celestial Alignments
 of the Celestial Choir
 of the Celestial Courts

 of the Celestial Gallop
 of the Celestial Lights
 of the Celestial Might
 of the Celestial Observations

 of the Celestial Orbs

 of the Celestial Order

 of the Chameleon Jungles
 of the Chaotic Maelstrom
 of the Chaotic Wilderness
 of the Charismatic Deceit
 of the Charmcaster's Domain
 of the Charming Courts
 of the Charming Spells
 of the Charming Streams
 of the Charming Tales
 of the Chill Tundras
 of the Chilling Fields
 of the Chilling Realm

 of the Chitinous Carapaces

 of the Chosen Path

 of the Chromatic Radiance

 of the Chronal Sands

 of the Civic Hubs
 of the Civilized Districts
 of the Clans

 of the Clay Fields

 of the Clever Minds

 of the Clever Ruses

 of the Cliffside Forges

 of the Clingy Depths
 of the Clockwork Mechanisms
 of the Cloud Kingdoms

 of the Cloud Realm

 of the Coastal Jungles

 of the Cold-Blooded Tribes

 of the Cold-Resistant Tribes

 of the Colossal Lands

 of the Colossal Might

 of the Commanding Shadows
 of the Conflicted Lands
 of the Connective Networks

 of the Conquered Lands

 of the Conquered Realm

 of the Constructs

 of the Consuming Darkness

 of the Contrite Echoes

 of the Copper Caverns
 of the Core Elements

 of the Core Reality

 of the Corrosive Lairs

 of the Corrupted Courts

 of the Corrupted Wings

 of the Corrupted Woods
 of the Cosmic Expanse
 of the Cosmic Frontiers
 of the Crafted Companions
 of the Crafty Gadgets
 of the Crafty Guilds
 of the Crafty Hideouts
 of the Crafty Lairs
 of the Crafty Workshops
 of the Cranial Archives
 of the Crimson Battles
 of the Croaking Jungles
 of the Cryptic Codes
 of the Cryptic Stones

 of the Crystal Lakes
 of the Crystalline Caverns
 of the Cubic Dungeons
 of the Cultured Academies
 of the Cultured Districts
 of the Cunning Plans
 of the Cunning Spells
 of the Cunning Traps
 of the Cunning Tricks
 of the Cunning Undergrowth
 of the Damned Armies
 of the Dancing Streams
 of the Dapper Societies
 of the Dark Caverns

 of the Dark Caves
 of the Dark Collections
 of the Dark Crevices

 of the Dark Fears
 of the Dark Pursuit
 of the Dark Rites
 of the Dark Seas
 of the Dark Swamps
 of the Dark Waters
 of the Darkened Paths
 of the Darkened Skies
 of the Dawn's Promise
 of the Daylight
 of the Deadly Hunts

 of the Deadly Shadows
 of the Deadly Terrains
 of the Deathly Missions
 of the Deathly Visions
 of the Decaying Woods
 of the Deception
 of the Deceptive Charm
 of the Deceptive Faces
 of the Deceptive Groves
 of the Deceptive Guises
 of the Deceptive Trails
 of the Deep Waters
 of the Demon Legends

 of the Demonic Clans
 of the Demonic Forges

 of the Demonic Mischief

 of the Demonic Packs

 of the Desert Winds

 of the Desert's Heart

 of the Desert-Born Oasis

 of the Despairing Abyss
 of the Determined Hunts
 of the Devious Plots

 of the Diabolical Pacts

 of the Dimensional Crossroads

 of the Distant Shores

 of the Divine Armies
 of the Divine Ascent
 of the Divine Crusade

 of the Divine Essence

 of the Divine Fragments

 of the Divine Harmony

 of the Divine Lineage

 of the Divine Mission
 of the Divine Mystery
 of the Divine Order
 of the Divine Oversight
 of the Divine Purity
 of the Domestic Bliss
 of the Dominant Realm
 of the Draconic Blood
 of the Draconic Lineage
 of the Dragon Realm
 of the Dreaded Tides
 of the Dual-Nature Realm
 of the Dual-Natured Realm
 of the Dull Caverns

 of the Dune Seas
 of the Duplicitous Shadows
 of the Dutiful Protection
 of the Dutiful Watch

 of the Eager Flames
 of the Earthen Core
 of the Earthen Marshes
 of the Earthen Pits
 of the Earthen Realm
 of the Earthy Depths
 of the Earthy Dwellings
 of the Echoing Caves
 of the Eclipsed Moons
 of the Eerie Doubles
 of the Eldritch Shadows
 of the Eldritch Truth
 of the Electric Peaks
 of the Electric Realm
 of the Elegant Balls
 of the Elegant Courts
 of the Elemental Essence
 of the Elemental Harmony
 of the Elemental Realm
 of the Elemental Roots
 of the Elevated Realm
 of the Elite Forces
 of the Elusive Natures
 of the Elusive Nights
 of the Elusive Paths

 of the Elusive Shadows
 of the Ember Fields
 of the Embers
 of the Eminent Thrones
 of the Enchanted Edge
 of the Enchanted Forests
 of the Enchanted Shadows
 of the Enchanting Eyes
 of the Endless Ocean
 of the Enduring Sands
 of the Energetic Shows
 of the Energetic Ventures
 of the Enforced Rule
 of the Engulfing Depths

 of the Enigmatic Performances
 of the Enigmatic Powers
 of the Entangling Canopies
 of the Entrancing Realm
 of the Erosive Gullies
 of the Eternal Cycle
 of the Eternal Elevation
 of the Eternal Flames
 of the Eternal Longing
 of the Eternal Moments
 of the Eternal Night
 of the Eternal Search
 of the Eternal Suffering
 of the Eternal Vigil
 of the Eternal Watch
 of the Ethereal Abyss
 of the Ethereal Bonds
 of the Ethereal Chains
 of the Ethereal Flames
 of the Ethereal Forms
 of the Ethereal Graves
 of the Ethereal Guard
 of the Ethereal Heights
 of the Ethereal Laments
 of the Ethereal Plane

 of the Ethereal Radiance
 of the Ethereal Shadows
 of the Ethereal Spheres
 of the Ethereal Veil
 of the Ethereal Veils
 of the Ethereal Winds
 of the Exalted Heavens
 of the Exalted Realm
 of the Explorative Paths
 of the Faithful
 of the Familiar Streets
 of the Fascinating Unknown
 of the Fateful Strands

 of the Fearful Nights
 of the Fearsome Battalions
 of the Fearsome Clans
 of the Fearsome Claws
 of the Fearsome Depths
 of the Fearsome Journeys
 of the Fearsome Night
 of the Fearsome Skies
 of the Fearsome Territories
 of the Fearsome Tides
 of the Feral Dominions
 of the Feral Jungles
 of the Feral Packs
 of the Feral Wilderness

 of the Feral Wilds
 of the Ferocious Assaults
 of the Ferocious Raids
 of the Festive Gatherings
 of the Fetching Markets
 of the Fierce Battles
 of the Fierce Clans
 of the Fierce Cliffs
 of the Fierce Currents
 of the Fierce Legions
 of the Fierce Raids
 of the Fierce Ranges

 of the Fierce Realm
 of the Fierce Wars
 of the Fiery Conversations
 of the Fiery Depths
 of the Fiery Earth
 of the Fiery Forges
 of the Fiery Gallop
 of the Fiery Pits
 of the Fiery Realm
 of the Fiery Rivers
 of the Fire's Heart
 of the Fire-Breathers
 of the Fire-Touched Lineage

 of the Flame Realm
 of the Flame-Enveloped Lairs
 of the Flighty Mirth
 of the Floral Gardens
 of the Floral Paradises
 of the Fluidic Pools
 of the Fluidic Streams
 of the Flying Arsenal
 of the Forest Dominions
 of the Forest Sanctuaries
 of the Forged Legions
 of the Forgotten Armory
 of the Forlorn Hearts
 of the Formless Pits

 of the Fossilized Valleys
 of the Fragrant Trails
 of the Free Forests
 of the Free Lands
 of the Fresh Ideas
 of the Frost
 of the Frost Lands
 of the Frostbound Lairs
 of the Frosty Peaks
 of the Frosty Realm

 of the Fundamental Forces
 of the Galactic Cores
 of the Gardener's Delights
 of the Gaunt Shadows
 of the Gelatinous Depths

 of the Gelatinous Mounds
 of the Gem Forests
 of the Gemstone Mountains
 of the Gentle Wilds
 of the Ghastly Woods
 of the Ghostly Marshes
 of the Ghostly Realm
 of the Giant Woods

 of the Glacial Caverns
 of the Glacial Peaks
 of the Glacial Pools
 of the Gleaming Halls
 of the Gloomy Shadows

 of the Gloomy Tunnels
 of the Gold-Loving Lore

 of the Graceful Bends
 of the Graceful Meadows
 of the Graceful Movements
 of the Graceful Skies
 of the Grecian Wars
 of the Green Sanctuaries
 of the Green Vines

 of the Green Woods
 of the Grim Harvest
 of the Grounded Lands
 of the Growing Prowess

 of the Gruff Mountains
 of the Guarded Tombs
 of the Guardian Banks
 of the Guardian Mummies
 of the Guardian Realm

 of the Guardian Scrolls
 of the Guardian Skies
 of the Guardian Spirits
 of the Guardian Tombs
 of the Guardian's Keep

 of the Half-Blood Realm

 of the Half-Breed Tribes
 of the Half-Goat Tribes
 of the Hallowed Shrine

 of the Hardy Seas


 of the Harvest Guardians
 of the Hazardous Quagmires
 of the Healing Streams

 of the Heartbroken Souls


 of the Heartbroken Tales
 of the Heavenly Bodies


 of the Heavenly Host
 of the Heavenly Peace
 of the Heavenly Realm
 of the Heavenly Scales

 of the Heavenly Spheres

 of the Heavenly Winds

 of the Hefty Challenges

 of the Hell's Tracks

 of the Hellbound Paths
 of the Hellish Battlegrounds

 of the Hellish Discipline
 of the Hellish Law
 of the Heroic Souls
 of the Hidden Chambers
 of the Hidden Lore
 of the Hidden Spirits
 of the Highest Heavens
 of the Highland Caverns
 of the Highland Realm
 of the Historical Chronicles
 of the Holy Fires

 of the Holy Quest
 of the Homegrown Community
 of the Honest Dealings
 of the Honorable Safeguards
 of the Honorable Temples
 of the Hooved Tribes
 of the Horned Dunes
 of the Hourglass Realm
 of the Howling Hollows
 of the Howling Winds
 of the Humble Domains
 of the Humble Faith
 of the Hungering Shadows
 of the Hyena Packs
 of the Hypnotic Gazes

 of the Icy Caverns
 of the Icy Glaciers
 of the Icy Mountains
 of the Icy Nightmares
 of the Icy Realm
 of the Icy Rivers
 of the Igneous Formations
 of the Illuminated Heavens
 of the Illusive Stalk
 of the Immortal Realm
 of the Immovable Fortresses
 of the Imperious Ruins
 of the Impish Games
 of the Implacable Fury

 of the Imposing Peaks
 of the Industrious Clans
 of the Industrious Workshops
 of the Infernal Ancestry
 of the Infernal Battles
 of the Infernal Courts
 of the Infernal Depths
 of the Infernal Quests
 of the Infernal Roads
 of the Infernal Trail
 of the Infernal Truths
 of the Inky Pools
 of the Innovative Designs
 of the Innovator's Mind

 of the Inscribed Wisdom
 of the Insect Colonies
 of the Intangible Fear
 of the Interlinked Realm
 of the Intricate Craft
 of the Inventive Disruptions
 of the Inventive Solutions
 of the Jiggly Horrors
 of the Judgmental Fury
 of the Judicial Inquiries
 of the Judicious Spheres

 of the Just Cause
 of the Just Order
 of the Just Vengeance
 of the Knowledgeable Tomes
 of the Lamenting Moors
 of the Land Seas
 of the Lands
 of the Laughing Packs
 of the Lawless Lands
 of the Leaf-Crowned Canopies
 of the Leafy Canopies

 of the Lean Paths
 of the Leaping Rivers
 of the Learned Repositories
 of the Learned Society
 of the Learned Undergrowth
 of the Legendary Tales
 of the Light Beams

 of the Lightbringer's Domain
 of the Lightning Skies
 of the Lightning Storms
 of the Lion-Scorpion's Lair
 of the Lively Markets
 of the Lively Quarters

 of the Living Groves
 of the Living Rooms
 of the Local Taverns
 of the Lofty Realm
 of the Lost Grace
 of the Lovely Gardens
 of the Luminescent Swamps
 of the Luminous Caverns
 of the Luminous Expanse
 of the Luminous Horizons
 of the Luminous Nights
 of the Luminous Realm
 of the Lurking Shadows

 of the Lush Canopies
 of the Lustrous Depths
 of the Lycan Packs
 of the Magma
 of the Majestic Canopies
 of the Majestic Mountains
 of the Majestic Rule
 of the Majestic Skies
 of the Majestic Storms
 of the Malefic Caverns
 of the Malefic Spells
 of the Malevolent Curses

 of the Malevolent Deeds
 of the Malevolent Depths
 of the Malevolent Plans
 of the Malevolent Thickets
 of the Malevolent Woods
 of the Man-Eating Forests
 of the Manipulative Arts
 of the Marine Depths
 of the Maritime Adventures
 of the Maritime Cliffs
 of the Maritime Depths
 of the Marsh Realm
 of the Mausoleum's Secrets

 of the Mechanical Havoc
 of the Mechanical Planes
 of the Mechanical Wings
 of the Mechanical Wonders
 of the Mechanical Workshops
 of the Mechanized Worlds
 of the Melodic Streams
 of the Menacing Bogs
 of the Menacing Hunts
 of the Menacing Shadows
 of the Menacing Tales
 of the Menacing Terrains

 of the Merciless Chase
 of the Merry Woods
 of the Metal-Bound Guilds
 of the Metallic Creations
 of the Metropolitan Melting Pots
 of the Mighty Battles
 of the Mighty Clans
 of the Mighty Deeds
 of the Mighty Heritage
 of the Mighty Realm
 of the Mighty Skies
 of the Mighty Wastes
 of the Mighty Woods
 of the Migratory Routes

 of the Mimicked Faces
 of the Mindless Hordes
 of the Miniature World
 of the Minor Miracles
 of the Minor Wonders
 of the Mire Depths
 of the Mischevious Plots
 of the Mischievous Antics
 of the Mischievous Deeds
 of the Mischievous Raids
 of the Mischievous Shadows
 of the Mischievous Spirits
 of the Molten Depths

 of the Molten Lakes
 of the Monochrome Pools
 of the Monstrous Dominions
 of the Monstrous Lands
 of the Monstrous Realm
 of the Monstrous Waves
 of the Monumental Fortresses
 of the Morning Rays
 of the Morning Skies
 of the Mountain Lairs
 of the Mountain Peaks
 of the Mountain Trails
 of the Mountain's Heart
 of the Mountainous Wilderness
 of the Mountains
 of the Mournful Echoes
 of the Mournful Echos
 of the Moving Households
 of the Multi-Headed Nightmares
 of the Murderous Rampages
 of the Muscular Guilds
 of the Musical Glens
 of the Musical Groves
 of the Muspelheim Flames
 of the Musty Dungeons

 of the Mycelial Networks
 of the Mysterious Guises
 of the Mysterious Realm
 of the Mysterious Streams
 of the Mysterious Travels
 of the Mysterious Tunnels
 of the Mystic Arts
 of the Mystic Dunes
 of the Mystic Glades
 of the Mystic Illusions
 of the Mystic Paths
 of the Mystic Realm
 of the Mystic Rites

 of the Mystic Sands
 of the Mystic Visions
 of the Mystic Winds
 of the Mystical Charms
 of the Mystical Forces
 of the Mystical Glades
 of the Mystical Scales
 of the Mystical Tides
 of the Mystical Undergrowth
 of the Mystical Vapors
 of the Mythical Curses
 of the Mythical Lands
 of the Mythical Legends
 of the Mythical Menace
 of the Natural Order
 of the Nature Spirits' Realm
 of the Nature's Core
 of the Nature's Embrace
 of the Nature's Wonders
 of the Nature-Crafted Items
 of the Necrotic Realm
 of the New Day
 of the New Sky
 of the Night's Seduction
 of the Nocturnal Haunts


 of the Nocturnal Shadows
 of the Nodal Points
 of the Noisy Mansions

 of the Nomadic Journeys

 of the Nomadic Tribes

 of the Norse Legends

 of the Norse Wilds

 of the Obsidian Caves

 of the Ocean Depths

 of the Oceanic Expanse
 of the Oceanic Hunts

 of the Oceanic Realm

 of the Oceanic Ruins
 of the Ogre Realm
 of the Ominous Nights

 of the Open-Air Quarries

 of the Orderly

 of the Orderly Barracks

 of the Orderly Heavens

 of the Origin Point

 of the Origin Realm
 of the Other Realm
 of the Pactkeeper's Realm
 of the Pallid Complexions

 of the Paralyzing Breath

 of the Petal Meadows
 of the Petrifying Presence
 of the Phantom Grudges
 of the Philosophers
 of the Pilgrimage
 of the Planar Gateways

 of the Playful Dances
 of the Poisoned Fangs
 of the Poisonous Marshes

 of the Poisonous Mists

 of the Powerful Dominions

 of the Powerful Rivers

 of the Powerful Roars
 of the Prankter's Games

 of the Predatory Hunts

 of the Predatory Lands
 of the Predatory Schools

 of the Prehistoric Lands

 of the Preserved Crypts

 of the Primal Essence
 of the Primal Forces
 of the Primal Jungles

 of the Primal Snows

 of the Primeval Essence

 of the Primitive Lands

 of the Primordial Sands

 of the Prismatic Scales
 of the Prophetic Vision

 of the Protected Treasures

 of the Protective Arms

 of the Protective Mantle

 of the Protector's Might

 of the Proud Dynasties
 of the Psionic Spheres

 of the Punishing Flames

 of the Pure Hearts

 of the Pure Skies

 of the Pyres

 of the Quick Movements
 of the Radiant Host

 of the Radiant Lakes
 of the Radiant Order
 of the Radiant Skies

 of the Radiant Spheres

 of the Radiant Valleys

 of the Raging Storms

 of the Raging Waves
 of the Rare Jewels
 of the Rare Sightings
 of the Ravaged Lands

 of the Ravenous Appetites

 of the Ravenous Deserts

 of the Redeeming Mist
 of the Redemptive Acts
 of the Refined Art

 of the Refined Circles

 of the Refined

 of the Regal Realm

 of the Regenerating Woods
 of the Relentless Chases
 of the Relentless Pursuit

 of the Repentant Pains

 of the Reptilian Depths
 of the Resilient Folk

 of the Resilient Sands

 of the Resilient Spirits

 of the Resourceful Creations

 of the Resourceful Packs

 of the Respected Forest
 of the Resurrected Revenge
 of the Retaliatory Strikes

 of the Retributive Haunts

 of the Righteous Judgments

 of the Rising Sun
 of the Rivers

 of the Roadbarter Paths

 of the Roaming Lands
 of the Roaming Packs

 of the Roaming Vapors

 of the Robust Battles

 of the Rocky Caverns
 of the Rocky Enclaves
 of the Rooted Paths

 of the Rugged Highlands

 of the Rugged Landscapes

 of the Rugged Mountains

 of the Rugged Peaks

 of the Rugged Terrain

 of the Rugged Territories
 of the Rugged Wastelands

 of the Running Rivers

 of the Rustic Marshes

 of the Ruthless Command

 of the Ruthless Enforcement
 of the Ruthless Hunts
 of the Ruthless Raids

 of the Sabotaged Machines

 of the Sacred Light
 of the Sacred Oath
 of the Sacred Scrolls

 of the Sages

 of the Sailor's Seas

 of the Sand Dunes

 of the Sand-Worn Trails
 of the Sapient Circles
 of the Savage Fury
 of the Savage Jungles
 of the Savage Packs
 of the Savage Plains
 of the Savage Realm
 of the Scaled Fortresses
 of the Scaled Tribes
 of the Scaly Jungles
 of the Scheming Depths
 of the Scholar Tower

 of the Scholarly Archives
 of the Scholarly Halls
 of the Scouting Skies
 of the Screeching Cliffs
 of the Screeching Winds
 of the Sculptor's
 of the Sea Monsters' Lair
 of the Sea Mysteries
 of the Sea's Embrace
 of the Sea-Bound Realm
 of the Sea-Bound Shores
 of the Seafaring Journeys
 of the Seas

 of the Secure Banks
 of the Seductive Shadows
 of the Seeking Souls
 of the Sentient Brigade

 of the Sentient Woods

 of the Seraphic Host

 of the Seraphic Light

 of the Serene Heavens
 of the Serene Waters
 of the Serpentine Coils
 of the Serpentine Grace
 of the Serpentine Heavens
 of the Serpentine Lairs
 of the Sewer Depths
 of the Shaded Depths
 of the Shadowed Paths
 of the Shadowy Abyss
 of the Shadowy Corners
 of the Shadowy Realm

 of the Shape-Shifting Mystery
 of the Shapeless Expanse
 of the Shark Waters
 of the Shifting Forms

 of the Shimmering Depths

 of the Shining Pits

 of the Silent Shadows

 of the Silent Tombs

 of the Silent Watch

 of the Silken Threads
 of the Silver Realm
 of the Simple Life

 of the Sinister Dominions
 of the Sinister Fields
 of the Sinister Glades
 of the Sinister Paths

 of the Siren's Call
 of the Skeletal Chambers
 of the Skillful Creations
 of the Sky Dominions

 of the Sky Realm

 of the Skybound Dominance

 of the Skybound Dominions

 of the Sleep-Inducing Winds
 of the Slight Touches
 of the Slimy Trails

 of the Slippery Banks

 of the Slowing Mists

 of the Sly Escapades
 of the Sly Escapes
 of the Snow

 of the Snowbound Lands

 of the Snowbound Peaks

 of the Sociable Tribes

 of the Soft Gusts
 of the Solar Brilliance
 of the Solar Realm

 of the Solitary Mountains
 of the Sophisticated Guilds
 of the Sophisticated Salons
 of the Sophisticated Societies
 of the Sorrowful Shadows
 of the Soulbound Realm
 of the Sovereign Peaks
 of the Spaceborne Nebulae
 of the Spark of Innovation
 of the Sparkling Mines
 of the Speaking Woods
 of the Spectral Abyss

 of the Spectral Wrath
 of the Spectrum Light
 of the Spiritual Realm
 of the Spore-Crowned Kingdom
 of the Spore-Filled Caves
 of the Sporty Competitions
 of the Square Passages
 of the Stalwart Guards
 of the Stardust Clouds
 of the Starry Heavens
 of the Statuesque Realm
 of the Steady Streams
 of the Stealthy Bogs

 of the Stealthy Raids
 of the Steampunk Realm
 of the Steel Clans

 of the Stellar Depths

 of the Stellar Realm

 of the Stern Judgments

 of the Stern Rule
 of the Sticky Floors
 of the Stoic Lands
 of the Stoic Woods
 of the Stoneheart Mountains
 of the Stones
 of the Stony Realm
 of the Stony Valleys
 of the Stormcaller Realm
 of the Stormy Seas
 of the Stout Clans
 of the Stout Legions
 of the Strategic Battalions
 of the Streetwise Gangs
 of the Striking Figures
 of the Strongblood Lines
 of the Strongholds
 of the Sturdy Branches
 of the Sturdy Cliffs
 of the Sturdy Fortresses

 of the Sturdy Mines
 of the Subterranean Depths
 of the Subterranean Tribes
 of the Sun's Core
 of the Sun-Scorched Sands
 of the Sunfire Realm
 of the Sunken Cities
 of the Surveillance Network
 of the Swampy Enclaves
 of the Swaying Meadows
 of the Swift Rivers
 of the Swift Strikes
 of the Swift Winds
 of the Sylvan Glades

 of the Sylvan Groves
 of the Symbolic Grounds
 of the Systematic Order
 of the Tempestuous Clouds

 of the Tempting Darkness

 of the Tempting Whispers

 of the Tenebrous Depths

 of the Tentacled Horrors

 of the Terran Realm
 of the Terrifying Abyss
 of the Terrifying Depths
 of the Terrifying Dreams
 of the Terrifying Hunts
 of the Terrifying Legends
 of the Terrifying Myths
 of the Terrifying Peaks
 of the Terrifying Realm
 of the Terrifying Roars

 of the Terrifying Strength
 of the Thick Goo
 of the Thick Swamps
 of the {} Groves
 of the Three-Headed Vigil
 of the Tidal Waves
 of the Tides
 of the Time Streams

 of the Tinkering Chaos
 of the Tiny {rank}
 of the Titanic Depths
 of the Titanic Jungles
 of the Tormented Lands

 of the Tormented Realm
 of the Totemic Woods
 of the Tough Streets
 of the Towering Groves
 of the Towering Mountains
 of the Toxic Thickets
 of the Trader Routes
 of the Traditional Keeps
 of the Transcendent Light
 of the Translucent Depths
 of the Translucent Forms
 of the Translucent Veils

 of the Transparent Traps
 of the Trapping Pits
 of the Traveler's Destinations
 of the Traveling Bands
 of the Traveling Caravans
 of the Treacherous Roads
 of the Tribes
 of the Trickster's Lair
 of the Trickster's Theater
 of the Trickster's Web
 of the Tricky Mischief
 of the Tropical Jungles
 of the Tundra Expanse

 of the Tunnel Depths
 of the Twisted Mines
 of the Twisted Paths
 of the Twisting Thickets
 of the Tyrannical Rule
 of the Unassuming Faith
 of the Underground Realm
 of the Undying Dominance
 of the Undying Vigil
 of the Undying Will
 of the Unforgiving Night
 of the Unique Realm
 of the Unnatural Gardens

 of the Unpredictable Madness
 of the Unrelenting Searches
 of the Unseen Watchers
 of the Unspeakable Realm
 of the Untamed Realm
 of the Untamed Territories
 of the Unyielding Edicts
 of the Unyielding Law
 of the Urban Jungles
 of the Urban Streets
 of the Urban Underbelly
 of the Valhalla Halls
 of the Venerable Ancestors
 of the Vengeful Night

 of the Vengeful Nights
 of the Vengeful Spirits
 of the Venomous Barrens
 of the Venomous Bogs
 of the Verdant Glades
 of the Verdant Jungles
 of the Versatile Kin
 of the Vibrant Communities
 of the Vibrant Connections
 of the Vibrant Gardens
 of the Vibrant Scales
 of the Vicious Storms
 of the Vigilant Spirits
 of the Vigilant Thicket

 of the Vigilant Watches
 of the Vigorous Hunts
 of the Virtuous Paths
 of the Viscous Swamps
 of the Visionary Peaks
 of the Volcanic Lands
 of the Volcanic Mountains
 of the Volcanoes
 of the Wandering Bazaars
 of the Wandering Dunes
 of the Wandering Spirits
 of the Wandering Tales
 of the War-Torn Realm
 of the Warm Embrace

 of the Warrior Spirits
 of the Watchful Eyes
 of the Waterborne Gardens
 of the Watery Banks
 of the Watery Depths
 of the Weak Spirits
 of the Wealthy Treasuries
 of the Wee Folk
 of the Whimsical Breezes
 of the Whirlwinds
 of the Whispering Leaves
 of the Wholesome Villages
 of the Wild Festivities
 of the Wild Frontiers

 of the Wild Hunt
 of the Wild Trails
 of the Windborn Realm
 of the Windy Cliffs

 of the Winged Dominance

 of the Winged Patrols

 of the Winged Shadows

 of the Winged Territories

 of the Winter Territories
 of the Winterborn Forests
 of the Wise Dominions
 of the Wise Groves
 of the Wise Skulls
 of the Wise Traditions
 of the Wishful Dominions
 of the Witching Hours
 of the Witty Escapades
 of the Wolf Shadows
 of the Wrathful Haunts
 of the Wrathful Shadows
 of the Wyrm Garden
 of the Young Realm

 of the Zephyr Valleys
 of the Zephyrs
 of Unfamiliar Territories
 Ogre
 Ominous Apparition
 Open-Air
 Order Keeper
 Orderly
 Orderly Chieftain
 Origin
 Origin Keeper
 Origin Master
 Otherworldly Emissary
 Pact Guardian

 Pactkeeper
 Paladin
 Pallid
 Pallid Alchemist

 Paralyzing

 Parson

 Patron

 Paw

 Perceptive

 Phantom of Vengeance
 Phantom Stalker
 Philosopher
 Philosophic
 Pious
 Pit Fiend

 Pitmaster
 Playful Imp
 Playful Prankter
 Poisonous Jelly
 Power Sovereign
 Powerful Crocfolk
 Powerful Emissary
 Powerful Titan
 Prankter
 Preacher
 Predatory

 Predatory Beast
 Predatory Menace
 Prehistoric
 Pride


 Primal Giant
 Primal Hunter
 Primal Sage
 Primeval
 Primeval Guardian
 Primitive Chieftain
 Primordial Spirit
 Professor
 Profound
 Prophet
 Prophetic
 Protective Spirit
 Proud
 Proud Scion
 Psionic
 Psionic Wyrm
 Puddle
 Pure
 Queen
 Quick
 Quick Slime
 Radiance

 Radiant
 Radiant Angel
 Radiant Emissary
 Radiant
 Radiant Serpent
 Radiant Sovereign
 Raging
 Raging Demon
 Rainbow Serpent
 Rainbow-Scaled
 Rare

 Rare Sovereign
 Rare Vision
 Ravager
 Ravenous

 Ravenous Beast
 Ravenous Fiend
 Reality Weaver
 Recon Unit
 Redeemed
 Redeeming

 Redeeming Wraith
 Redemptive
 Redemptive Ghost
 Refined
 Refined Artist
 Regal Lady
 Regenerating Behemoth
 Relentless Entity
 Relentless Pursuer
 Reptilian Horror
 Researcher

 Resilient Cactus
 Resourceful Creator
 Respected
 Respected Elder
 Resurrected
 Resurrected Avenger
 Retributive
 Retributive Ghost

 Reverent
 Riding

 Righteous
 Righteous Punisher
 Ritual Guardian
 River-Dwelling
 Roadbarter Adventurer
 Roaming
 Roaming Hunter
 Roaming Mystic

 Robust
 Rocky Marauder
 Rocky Sage
 Rooted
 Rooted Wanderer

 Rugged
 Rugged Fiend
 Rugged Fighter
 Rugged Inventor

 Rugged Overlord
 Rugged
 Rugged Titan
 Rustic Puddle

 Rustic Reveler

 Ruthless Commander

 Ruthless Enforcer

 Ruthless Executor

 Ruthless Predator

 Sacred
 Sacred Wraith

 Sailor
 Sanctified
 Sand Marauder
 Sand Shaman
 Sandspeaker
 Sapient
 Sapient Shroom
 Savage Destroyer
 Savage Druid
 Savage Fiend
 Savage Giant
 Savage Predator
 Savant
 Scaled Guardian
 Scaled

 Scarecrow
 Scary
 Scavenger
 Scavenger Lord
 Scheming
 Scheming Ruler
 Scholarly
 Scholarly
 Scouting
 Screeching
 Scribe
 Scripted Guardian
 Sculptor of Stone
 Sea Captain
 Sea Guardian
 Sea Monster
 Sea Predator
 Sea Technologist

 Sea-Bound

 Seafarer

 Seafaring

 Seafaring Navigator

 Secure Banker
 Seductive Fiend

 Seductress


 Seductress of the Night
 Seeking

 Seeking Spirit

 Sentient Armor

 Sentient Oak

 Seraph Guardian

 Seraphic

 Seraphic Kin

 Serene

 Serene Guide

 Serpent

 Serpent Guardian
 Serpentine

 Serpentine Horror

 Serpentine Monster

 Sewer Sovereign

 Shade

 Shade Hunter

 Shadow Ruler

  Ooze
 Shaman
 Shape Sovereign

 Shape-Changing Enigma
 Shape-Shifter

 Shapeless
 Shapeless Horror

 Shapeshifter
 Sharp
 Shimmering
 Shimmering Artisan

 Shining
 Silk Weaver

 Silken
 Simple
 Sin Keeper
 Sinister Hunter

 Sire
 Siren
 Six-Winged
 Skilled Artisan
 Skilled Thief

 Skillful
 Skillful Mechanic
 Sky Coiler
 Sky Lord
 Sky Runner
 Sky Screamer
 Sky Serpent
 Sky Sovereign

 Skyborne Ruler
 Skybound
 Slain Chooser
 Sleek

 Sleek Guardian
 Sleep Master
 Sleep-Inducer
 Slick
 Slick Predator

 Slight
 Slight Artist
 Slime

 Slippery
 Slippery Fiend
 Sloth
 Slowing
 Slowing Wyrm
 Sly Imp
 Sly Messenger

 Smith
 Sneak Master

 Snowbound
 Snowbound Giant
 Snowbound Guardian
 Snowman


 Sociable Drake
 Soft Gust
 Solar Emissary
 Solar Guardian
 Solitary
 Sombre
 Sombre Ooze
 Songster
 Sophisticated
 Sophisticated Artisan
 Sophisticated Diplomat
 Sorrowful Ghost
 Soul Reaper

 Soulbound Keeper

 Sovereign Wyrm

 Spaceborne

 Spaceborne Entity

 Spark Commander

 Sparkling

 Sparkling Slime

 Sparkmaster

 Spectral

 Spectral Avenger

 Spectral Judge

 Spectral Terror
 Spectrum
 Spectrum Drake
 Spiked

 Spiked Terror
 Spinner of Lies
 Spirit Shifter
 Spiritual

 Spiritual Sentinel
 Spore
 Spore-Crowned
 Spore-Crowned Ruler
 Spore-Producing

 Spore-Producing Blob
 Sporty
 Sporty Adventurer
 Square
 Square Behemoth

 Stalwart
 Stalwart
 Stardust Weaver
 Starlight
 Starlight Emissary
 Starry Guardian
 Statue Warden
 Statuesque
 Steady
 Steady Guardian

 Stealthy Predator

 Stealthy Tracker

 Steampunk
 Steampunk Sentinel
 Steel
 Steelbound
 Stellar Guardian

 Stern
 Stern Enforcer
 Stern Overseer
 Stinger
 Stinger Master
 Stoic
 Stoic Colossus

 Stoic Defender
 Stoic Oak
 Stoneheart
 Stoneheart Guardian
 Stony
 Stony Chieftain
 Storm Dragon
 Stormborn
 Stormcaller

 Stormwing
 Storytelling
 Strategic
 Strategic Warlord
 Straw
 Streetwise
 Streetwise Leader
 Striking
 Striking Leader


 Strong Colossus
 Strongblood
 Strongblood Fighter

 Sturdy

 Sturdy Craftsman

 Sturdy Explorer
 Sturdy Guardian

 Sturdy Miner

 Subterranean

 Subterranean Chief

 Subterranean Guardian
 Suffering
 Suffering Phantom

 Sun

 Sun-Scorched
 Sun-Scorched Chief
 Sunfire
 Sunfire Master
 Surveillance
 Surveillance Machine
 Survivor
 Swamp-Dweller
 Swamp-Dwelling Shaman
 Swarm Leader
 Swaying
 Swift
 Swift Rapier
 Swift Runner
 Sylvan
 Sylvan Creator
 Symbolic
 Symbolic
 Systematic
 Systematic Overseer
 Talon Mistress
 Taloned
 Technologic
 Tempestuous
 Tempestuous Ruler
 Temptress
 Tenebrous
 Tentacled Behemoth
 Terramancer
 Terran
 Terran
 Terrifying Abomination
 Terrifying Beast
 Terrifying Chimera
 Terrifying Colossus
 Terrifying Giant
 Terrifying Gorgon
 Terrifying Kraken
 Terrifying Predator
 Terrifying Specter
 Terrifying Warlord
 Terror
 Terror King
 Thunder Drake
 Thunderous
 Tidal Master
 Tinkering
 Tinkering Rogue
 Tiny Sentinel
 Tiny Trickster
 Titanic
 Titanic Guardian
 Tome Sentinel
 Tormented
 Tormented Being
 Tormented Soul
 Tormentor
 Totemic
 Totemic Guardian
 Tough
 Tough Mercenary
 Towering
 Toxic Overlord
 Toxic Sludge
 Trader
 Trader Explorer
 Traditional
 Traditional Elder
 Transcendent
 Transcendent Sage
 Translucent Goo
 Translucent Mass
 Transparent
 Transparent Predator
 Trapping
 Trapping Goo
 Traveler of Paths
 Traveler of Realm
 Traveling
 Traveling Bard
 Traveling Warlord
 Trickster Apparition
 Trickster Artist
 Tricky Deceiver
 Tricky Guardian
 Tropical
 Tropical Guardian
 Tundra
 Tundra Wanderer
 Tunnel
 Tunnel Raider
 Twisted
 Twisted Aristocrat
 Twisted Miner
 Twisting
 Twisting Creeper
 Two-Headed Giant
 Tyrannical
 Tyrannical Leader
 Unbreakable
 Underlord
 Underworld Scout
 Undying
 Undying Commander
 Undying Sentinel
 Unfamiliar
 Unfamiliar Visitor
 Unforgiving
 Unforgiving Shade
 Unique
 Unique Individual
 Unmanned
  Entity
 Unpredictable
 Unrelenting
 Unrelenting Finder
 Unspeakable
 Unspeakable Fiend
 Unstructured
 Untamed Giant
 Untamed Leader
 Unyielding Judge
  Warlord
  Guardian
  Keeper
  Leader
  Overlord
  Specter
 Wraith
'''
