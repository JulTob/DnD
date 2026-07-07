import random

def Genus(lusor):
	"""
	Returns a descriptive  Colosseum string for a lusor (NPC or PC).

	- If lusor is already a string, return it.
	- If it has a `. Colosseum` property, use that.
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

def generate_title(lusor):
	"""
	Generates a title from the given lists,
	avoiding double spaces and handling title casing.
	"""
	descriptor = Descriptor(lusor)
	rank = Rank(lusor)
	for _ in range(10):
		if descriptor.lower() not in rank.lower() and rank.lower() not in descriptor.lower():
			break
		rank = Rank(lusor)

	origin = Origin(lusor)
	for _ in range(10):
		if descriptor.lower() not in origin.lower() and rank.lower() not in origin.lower():
			break
		origin = Origin(lusor)

	parts = [descriptor, rank, origin]
	title = " ".join(filter(None, parts))  
	#-- Removes empty strings
	return "The " + custom_title(title)

def Title(lusor):
	random.seed(lusor.seed)
	descriptor = Descriptor(lusor)
	rank = Rank(lusor)
	for _ in range(10):
		if descriptor.lower() not in rank.lower() and rank.lower() not in descriptor.lower():
			break
		rank = Rank(lusor)

	origin = Origin(lusor)
	for _ in range(10):
		if descriptor.lower() not in origin.lower() and rank.lower() not in origin.lower():
			break
		origin = Origin(lusor)

	patterns = [
		f"The {descriptor} {rank}",
		f"The {rank} {origin}",
		f"The {rank}",
		f"The {descriptor} {rank} {origin}"
		]

	weights = [
		20,
		15, 
		4,
		1
		]

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

	genus = Genus(lusor)

	descriptor = []

	# General Descriptors
	try:
		descriptor += [ # Animals
			"Camel",	
			"Baboon",	
			"Butterfly",	
			"Beetle",	
			"Cat",	
			"Cheetah",	
			"Cougar",	
			"Coyote",	
			"Crocodile",	
			"Dolphin",	
			"Dinosaur",	
			"Elephant",	
			"Bison",	
			"Boar",	
			"Badger",	
			"Deer",
			]
		descriptor += [ # A
			"Aquatic",			
			"Adventurous",		
			"Awesome",			
			"Apprentice",		
			"Aquatic",			
			"Ancient",			
			"Accursed",			
			"Abyssal",			
			"Astral",			
			"Ancient",			
			"Accursed",			
			"Amethyst",			
			"Atmospheric",		
			"Astronomical",		
			"Aquatic",			
			"Amulet",			
			"Art", 				
			"Artistic",			
			"Astral",			
			"Alien",			
			"Alpha",			
			"Autumn",			
			"Animal",			
			"Atmospheric",		
			"Archaic",			
			"Antique",			
			"Ancient",			
			"Amulet",			
			"Aurora",			
			"Alchemic",			
			"Amethyst",			
			"Alabaster",		
			"Alien",			
			"Azure",			
			"Amulet",			
			"Arboreal",			
			"Atmospheric",		
			"Airy",				
			"Aerial",			
			"Astute",			
			"Analytical",		
			"Artistic",						
			"Antagonistic",		
			"Aggressive", 		
			"Acrimonious",		
			"Abominable",		
			"Ardent",			
			"Angelic", 			
			"Amulet",					
			"Antagonistic",								
			"Acrimonious",		
			"Abhorrent",		
			"Ardent",			
			"Amorous",			
			"Affection",		
			"Adoring",			
			"Aristocratic",		
			"Astronomical",		
			"Antique",			
			"Antediluvian",		
			"Ancient",			
			"Ancestral",		
			"Ageless",			
			"Astral",			
			"Artifact",			
			"Amulet",			
			"Archaic",			
			"Affectionate",		
			"Aristocratic",		
			"Archaic",			
			"Antique",			
			"Apostolic",		
			"Astral", 			
			"Antediluvian",		
			"Ancient",			
			"Ancestral",		
			"Atemporal",		"Ancient",			
			"Ancestral",		
			"Anachronistic",	
			"Ageless",			
			"Ancient",			
			"Amulet",			
			"Abhorrent",		
			"Abyssal",			
			"Angelic",						
			"Ageless",						
			"Antediluvian",		
			"Archipelago",		
			"Alluring",			
			"Archipelago",		
			"Adorned",			
			"Arctic",			
			"Artistic",			
			"Ascetic",			
			"Ardent",			
			"Arena",			
			"Aristocratic",		
			"Arrogant",			
			"Artifact",			
			"Asgardian",		
			"Astral",			
			"Astute",			
			"Atlantean",		
			"Aurora",			
			"Autumn",			
			"Awakened",			
			"Aztec",			
			"Azure",			
			"Abominable",		
			"Amazonian",		
			"Amethyst",			
			"Amulet",			
			"Ardent",			
			"Ancestral",		
			"Ancient",			
			"Antique",						
			"Apostolic",		
			"Aquatic",			
			"Arachnid",			
			"Arboreal",						
			"Arcanic",			
			"Arch",				
			"Archaic",			
			"Abyssal",			
			"Aerial",			
			"Ageless",			
			"Alabaster",		
			"Alchemical",		
			"Alcoholic",		
			"Alpha",			
			"Amber",			
			"Amber",			
			"Augury",			
			"Amber",			
			"Ancient",			
			"Ancient",			
			"Ancient",			
			"Ancient",			
			"Ancient",			
			"Aberrant",			
			"Ancient",			
			"Amber",			
			"Ancient",			
			"Apex",				
			"Age-old",				
			"Alpha",			
			"Air",				
			"Air",				
			"All-Seeing",		
			"Air",				
			"Armored",			
			"Aura",				
			"Aura",				
			"Alcoholic",		
			"Astral",			
			"Astral",			
			"Archfey",			
			"Awakened",			
			"Autumn",									
			"Antique",			
			"Ageless",			
			"Armored",			
			"Armored",			
			"Armorless",		
			"All Seeing",
			]
		descriptor += [ # B
			"Band",				
			"Bloodmoon",		
			"Blending",			
			"Bat",				
			"Black",			
			"Blind",			
			"Bursting",			
			"Bone",				
			"Bronze",			
			"Book",				
			"Burning",		
			"Blizzard",			
			"Book",			
			"Brass",		
			"Bronze",		
			"Binding",				
			"Boreal",		
			"Bloodmoon",	
			"Blizzard",		
			"Black Hole",	
			"Baroque",		
			"Blade",		
			"Battle",		
			"Blight",		
			"Bone",			
			"Black",		
			"Babylonian",		
			"Badland",			
			"Baleful",			
			"Blade",			
			"Black",			
			"Baronial",			
			"Baroque",			
			"Barracks",			
			"Barren",			
			"Bat",				
			"Battle",		
			"Bark",			
			"Battleground",		
			"Bay",			
			"Beach",						
			"Behemoth",				
			"Benevolent",	
			"Beryl",		
			"Bewitched",	
			"Biblical",				
			"Bitter",			
			"Bramble",			
			"Brass",			
			"Brave",			
			"Breezy",			
			"Bridge",			
			"Brimstone",		
			"Bronze",			
			"Bronze",			
			"Brooch",												
			"Burgundy",		
			"Black",		
			"Bog",				
			"Bone",			
			"Book",					
			"Boreal",		
			"Brain",		
			"Blazing",		
			"Burned",		
			"Burning",		
			"Bursting",		
			"Butterfly",			
			"Bygone",			
			"Byzantine",			
			"Blind",			
			"Blizzard",			
			"Blood",			
			"Blooming",			
			"Blossoming",		
			"Blue",				
			"Battle",			
			"Basalt",			
			"Broken",			
			"Blood",			
			"Battle",		
			"Battle",		
			"Battle",			
			"Battle",		
			"Brave",		
			"Brave",		
			"Bow",			
			"Bold",			
			"Bloodthirst",	
			"Boreal",		
			"Boreal",		
			"Blue",			
			"Blue",			
			"Black",		
			"Black",		
			"Blood",		
			"Blood",		
			"Blood",		
			"Blooming",		
			"Brass",			
			"Bursting",						
			"Brain",		
			"Butterfly",		
			"Burning",		
			"Blade",		
			"Boundless",	
			"Boundless",	
			"Brimstone",	
			"Burning",		
			"Blood",		
			"Beautiful",
			]
		descriptor += [ # C
			"Crowned",			
			"Charmed",			
			"Corrupted",		
			"Cranium",			
			"Celestial",		
			"Colossal",			
			"Crafty",			
			"Codex",			
			"Colossal",			
			"Complex",			
			"Creativity",		
			"Cosmic",			
			"Cosmos", 			
			"Cosmic",			
			"Cometary",		
			"Climatic",			
			"Cloud",			
			"Chimeric",			
			"Compassion",			
			"Celestial",			
			"Cold",			
			"Chivalrous",			
			"Chaotic",			
			"Charcoal",			
			"Charming",			
			"Charter",			
			"Chasm",			
			"Compass",			
			"Compassionate",	
			"Concealed",		
			"Confusion",		
			"Constellation",	
			"Contempt",			
			"Copper",			
			"Coral",			
			"Corpse",			
			"Cosmic",		
			"Cosmos",			
			"Covert",						
			"Crater",			
			"Crescent",			
			"Crest",			
			"Crested",			
			"Crimson",			
			"Crossed",			
			"Crown",						
			"Cruel",			
			"Crypt",			
			"Cryptic",			
			"Crystal",			
			"Crystalline",		
			"Cunning",			
			"Curse",			
			"Cursed",			
			"Cyan",				
			"Cyclic",			
			"Cyclonic",			
			"Cyclopean",
			"Cynical",			
			"Chronal",			
			"Chronic",			
			"Cipher",			
			"Circus",			
			"Citadel",			
			"City",			
			"Clairvoyant",			
			"Clandestine",			
			"Classical",			
			"Comet",			
			"Cleric",			
			"Clerical",			
			"Clever",			
			"Cliff",			
			"Climatic",			
			"Cloaked",			
			"Cloaked",			
			"Clockwork",		
			"Cloud",			
			"Coast",			
			"Cobalt",			
			"Cobweb",			
			"Code",			
			"Cold",				
			"Colonial",			
			"Colossal",			
			"Combat",			
			"Candle",			
			"Canyon",			
			"Cardinal",			
			"Castle",			
			"Cat",			
			"Catacomb",			
			"Cathedral",			
			"Cave",			
			"Cavern",			
			"Celestial",		
			"Cloudreader",		
			"Celtic",			
			"Cerebral",			
			"Cerulean",			
			"Cerulean",			
			"Chain",			
			"Chained",			
			"Chalice",			
			"Champion",			
			"Corrupt",			
			"Chief",		
			"Crowned",			
			"Camouflage",		
			"Cursed",			
			"Charmbreaker",			
			"Chaos",			
			"Cerberus",			
			"Clockwork",			
			"Clockwork",			
			"Charming",			
			"Craft",			
			"Chained",			
			"Chain",			
			"Chaos",			
			"Crystal",			
			"Cosmic",			
			"Cosmic",			
			"Cat",				
			"Chain",			
			"Chief",			
			"Chief",			
			"Chief",			
			"Circus",			
			"City",				
			"Coral",			
			"Copper",		
			"Cursed",							
			"Crimson",			
			"Crown",			
			"Cold",			
			"Colossal",			
			"Cooper",
			]
		descriptor += [ # D
			"Dread",			
			"Dimensional",		
			"Dagger",			
			"Deep Sea",			
			"Dungeon",			
			"Divine",			
			"Dream",						
			"Dusk",			
			"Disgust",			
			"Dauntless",			
			"Dawn",			
			"Deadly",			
			"Death",			
			"Deep",			
			"Delightful",			
			"Delta",			
			"Desert",			
			"Desolated",			
			"Desperate",						
			"Detestable",			
			"Devoted",			
			"Doom",				
			"Dormant",			
			"Draconian",        
			"Draconic",			
			"Dragon",			
			"Dragonfire",			
			"Drained",			
			"Dream",			
			"Dune",			
			"Dungeon",			
			"Dusk",			
			"Dusky",			
			"Dust",			
			"Dynastic",			
			"Day",			
			"Divine",			
			"Devotional",			
			"Daemonic",			
			"Dagger",			
			"Dungeon",			
			"Dark",			
			"Darkness",			
			"Darkstar",			
			"Devout",			
			"Dew",				
			"Diabolical",		
			"Diadem",			
			"Dimension",		
			"Dimensional",		
			"Dire",			
			"Damnation",			
			"Drifting",			
			"District",			"Diavolical",			
			"Doom",			
			"Death",  
			"Dawning",			"Death",			
			"Dominating",			
			"Deadly",						
			"Dragon",			"Deadly",			"Dawning",			
			"Deep",				
			"Divine",			
			"Dream",			"Dust",				
			"Demon",			
			"Deadly",			"Desolate",			 "Deathless",
			]
		descriptor += [ # E
			"Elder",			"Existence",		"Ethereal",			"Eclipse",			"Everlasting",		"Eternal",		"Eldritch",		"Elder",		"Elder",			"Epochal",			"Endless",			"Ether",			"Enemy",			"Empty",			"Everlasting",			"Exalted",						"Existence",			"Exotic",			"Expedition",			"Extraterrestrial",			"Exuberant",			"Everlasting",					"Eclipsed",			"Ecliptic",			"Ecstatic",			"Ectoplasmic",					"Edict",		"Edo",						"Erudite",			"Esoteric",			"Eternal",			"Ethereal",			"Euphoric",			"Evanescent",			"Evangelical",		"Elder",			"Eldritch",			"Electric",			"Elegant",			"Elemental",			"Elixir",						"Elizabethan",			"Eloquent",			"Elusive",			"Elven",			"Elysian",			"Elysium",			"Ember",			"Emblem",		"Emerald",		"Eminent",		"Empathetic",		"Enchanted",		"Enchanting",		"Energetic",		"Energy",			"Engine",			"Enigma",			"Enraged",			"Envious",			"Ephemeral",			"Epochal",			"Equinox",			"Errant",			"Erratic",			"Echo",			"Eagle",			"Earth",			"Ebony",			"Ecclesiastical",	"Eclipse",			"Emissary",			"Elemental",	"Exalted",		"Electric",		"Ever",				"Earth",			"Earth",			"Errant",			"Energy",			"Engine",			"Equinox",			"Enchanted",			"Earthy",			"Enchanted",			"Evasive",			"Eagle",			"Equinox",			"Energy",			"Emerald",			"Enchanted",			"Engine",			"Earth",			"Errant",			"Enchanted",		"Enchanting",		"Endless",		"Earth",		"Eternal",		"Ethereal",
			]
		descriptor += [ # F
			"Forgotten",		
			"Ferocious",		
			"Force",			
			"Forest",			
			"Forgotten",			
			"Flowing",			
			"Fluid",				
			"Frostfire",		
			"Frostbite", 	
			"Fire",				
			"Frost",			
			"Fen",			
			"Fenrir",			
			"Fable",			
			"Fabled",			
			"Fae",			
			"Fairground",			"Faithful",			"Falcon",			"Falcon",			
			"Fallen",			
			"Fanciful",			"Fanged",			"Far",							
			"Fast",				"Fathom",			"Fearful",				
			"Feathered",			"Feral",			"Ferocious",			
			"Fluid",			"Fervent",			"Feudal",						"Fierce",			"Fiery",			"Finned",			"Folk",			
			"Fool",			"Forceful",			"Foreboding",			"Forest",			"Forested",			"Forge",			"Formidable",			
			"Fortress",			"Fountain",			"Frost",			"Frostbound",		"Frostbite",			"Frostfire",			"Frosty",			
			"Frozen",				"Frustrated",			"Fuchsia",			"Fullmetal",		"Fullmoon",			"Furious",			
			"Furred",			"Fury",			"Future",			"Ferocious",			
			"Feral",			"Fire",			"Firebrand",			"Firebreathing",			
			"First",			"Fjord",						"Flame",			
			"Flameheart",		"Flamehearted",		"Flametongue",			"Flaming",			"Fleshwork",		"Floral",				"Flourish",				"Flowing",			"Fluid",			"Flying",			"Fugitive",			"Fire",			"Fleshwork",			"Force",			"Flameborn",			"Flesh",			"Flying",			"Forest",			"Flame","Flame",			"Fullmetal",			"Fleshwork",			"First",			"Forest",			"Forest",			"Fury",					"Freedom",			"Ferocious",			"Fierce",			"Free",				"Freedom",				"Fairy", "Fate",				"Fateful",			"Feathered",		"Fiery",			"Fire",			"Fey",			"Feywild",			"Firbolg",			"Fire",			"Flame",			"Frost",			"False",			"Forge",
			]
		descriptor += [ # G
			"Green",			"Godless",			"Grim",				"Giant",			"Green",			"Gold",				"Gentle",			"Great",			"Glowing",			"Gleaming",			"Gloomy",			"Grieving",			"Grateful",			"Graphite",			"Granite",			"Grail",				"Green",				"Golden",			"Glowing",			"Grail",			"Gavel",			"Gaseous",							"Gases",			"Gaseous",			"Garden",			"Gravitational",		"Galactian",		"Galactic",			"Glacier",			"Gothic",			"Glacial",			"Grail",			"Goblet",			"Glowing",			"Great",			"Grand",			"Golden",			"Gregorian",		"Galactian",		"Galactic",			"Galaxy",			"Gallant",			"Garden",			"Gargantuan",		"Gargoyle",							"Gaseous",			"Gauntlet",			"Gavel",			"Gemmed",			"Gentle",			"Geyser",			"Ghost",			"Ghostly",			"Gleaming",			"Gloom",			"Glorious",			"Glowing",			"Glyph",			"Goblet",			"Gold",				"Golden",			"Goldenhearted",	"Goldenrod",		"Golem",			"Gorge",			"Gorgonian",		"Gothic",			"Graceful",			"Grail",			"Grand",			"Granite",			"Graphite",			"Grassland",		"Grassy",			"Grateful",			"Grave",			"Graveyard",		"Gravitational",	"Great",			"Greathearted",		"Green",			"Gulf",				"Grieving",			"Grim",				"Grimoire",			"Grove",			"Gryphon",			"Grim",				"Glorious",			"Giant",			"Gilded",			"Glacial",			"Glacier",			"Glade",			"Great",			"Green",			"Green",			"Graceful",			"Giant",							"Golden",			"Golden",			"Golden",			"Green",			"Great",			"Gentle",			"Galactic",			"Guarded",			"Grizzly",			"Godless",
			]
		descriptor += [ # H
			"Hollow",		"Hesperidean",		"Heliospheric",		"Historic",			"Heroic",			"Hell",				"Hermetic",				"Heart",		"Harmonious",		"Heartbroken",					"Hourly",			"Heartbroken",		"Hourly",			"Heartbroken",		"Hunting",			"Homeric",			"Horned",			"High",				"Helian",			"Haunting",			"Harpist",			"Harlequin",		"Hidden",			"Hoary", 	"High",			"Holy",				"Hamlet",			"Hammer",			"Han",							"Harbinger",			"Harbor",		"Harlequin",		"Harmony",			"Harpist",			"Harsh",			"Hateful",			"Haunting",			"Heart",			"Heartbroken",		"Heartfelt",		"Heath",			"Heavenly",			"Hedgerow",			"Helian",			"Heliospheric",		"Hell",		"Hellenistic",	"Hellish",		"Hermetic",		"Hermitage",		"Heroic",			"Hex",				"Hidden",			"Hieratic",			"High",					"Hill",			"Historic",			"Hive",				"Hoary",			"Hollow",			"Homeric",			"Honorable",		"Honored",			"Hopeful",			"Horizon",			"Horned",			"Horrific",			"Horus",			"Hostile",			"Hourglass",		"Hourly",			"Hunter",		"Hunting",		"Hydra",			"Hyperion",			"Hypnotic",			"Heretic",			"Howling",			"Hourglass",					"Hunger",			"Hell",				"Hill",				"High",				"Hive",				"Hound",			"Hourglass",		"Harmonic",
			]
		descriptor += [ # I
			"Immortal",			"Icy",				"Inferno",				"Instantaneous",		"Intrepid",				"Inquisitive",			"Intellect",		"Intellectual",			"Inkwork",				"Inkwell",				"Ink",				"Invincible",		"Impenetrable",		"Immortal",			"Icarian",			"Icicle",		"Ice",			"Icy",			"Immemorial",	"Infinite",			"Immortal",		"Indomitable",		"Ink",			"Ice",			"Ion",				"Ionic",			"Ionized",				"Irate",				"Iridescent",			"Iron",										"Island",				"Islet",				"Isolated",				"Ivory",			"Icarian",			"Ice",				"Iceborn",			"Icicle",			"Icon",				"Icy",			"Idol",			"Illusion",		"Illusionist",	"Imagination",		"Imam",			"Immemorial",		"Immortal",			"Impassioned",			"Impenetrable",			"Imperial",			"Imperious",			"Imperishable",			"Impish",				"Impulse",			"Incan",				"Incantation",								"Indigo",						"Inferno",			"Infinite",			"Infinity",			"Inimical",		"Ink",			"Inkwell",		"Inkwork",					"Innovative",		"Inquisitive",		"Inscrutable",			"Insidious",			"Inspired",			"Inspiring",			"Instantaneous",		"Intellect",			"Intellectual",			"Intense",						"Interim",				"Interstellar",			"Intimate",			"Intrepid",					"Intriguing",		"Invincible",		"Iron",				"Iron",			"Ice",			"Icicle",		"Ink",			"Ignoble",			"Infernal",			"Insatiable",
			]
		descriptor += [ # J
			"Journey",		"Jasmine",		"Jaguar",		"Jackal",		"Jackal", 		"Jaguar", 		"Jasmine", 	"Jay", 		"Jester", "Journey", "Judge", "Juggernaut", "Jungle",			"Juniper",		"Jungle",		"Just",		"Just",		"Judgmental",	"Judgmental",	"Judicial", 	"Just",	"Justice",	"Judicial",	"Just",	"Jurassic",	"Jungle",	"Jester",		"Jade",	"Jotunn",	"Judicial",			"Journey",			"Jewel",			"Jungle",			"Jungle",			"Jade",			"Jealous",			"Jewel",			"Jewelcraft",			"Jeweled",			"Jotunn",									"Joyous",		"Jubilant",		"Jungle",		"Just",
			]
		descriptor += [ # K
			"Knowledge",	"Keep",		"Krakenesque",				"Knife",				"Kaleidoscopic",				"Keen",				"Key",				"Kind",												"Kingly",							"Knightly",							"Kerberus",				"Key",
			]
		descriptor += [ # L
			"Loyal",			"Lucky",			"Lost",				"Lonely",			"Liquid",			"Luminous",			"Last",				"Labyrinthine",		"Labyrinth",	"Labyrinth",		"Large",			"Legendary",		"Legal",			"Loving",			"Luminous",			"Lunar",			"Lupine",			"Lordly",			"Laboratory",		"Labyrinth",						"Labyrinthine",		"Lagoon",			"Lake",			"Lantern",			"Last",			"Lauded",			"Lavender",			"Law",				"Liquid",			"Leafy",			"Luminous",			"Learned",			"Leechy",			"Legendary",			"Legislation",		"Lethal",			"Leviathan",		"Leather",			"Libra",			"Library",			"Lich",				"Life",			"Light",			"Lightbringer",		"Lightning",			"Lionmane",			"Lionheart",			"Liquid",			"Literary", 	"Lively",			"Living",			"Lizard",			"Loathsome",		"Lone",				"Lonely",			"Long",	"Looming",			"Lost",			"Loving",			"Loyal",			"Luminous",			"Lush",				"Lustrous",			"Luxurious",		"Lycan",			"Lyre",				"Lyrist",			"Lead",			"Lonely",			"Loyal",			"Lingering", 	"Lore",				"Lost",				"Lost",				"Life",				"Luminous",			"Life",				"Lightning",		"Lizard",			"Lonely",			"Long",				"Leader",			"Lunar",			"Light",			"Labyrinth",		"Labyrinthine",		"Lava",
			]
		descriptor += [ # M
				"Magical",		"Majestic",		"Marsh",		"Mischievous",	"Mirthful",		"Melancholic",	"Mythical",		"Moonlit",		"Moon",			"Mortal",		"Memory",		"Majestic",		"Majestic",		"Mystic",			"Mad",			"Misty",			"Mighty",			"Molten",	"Masterful",	"Monolith",		"Monolithic",			"Monstrous",	"Moon",	"Moonlit",		"Moonshade",	"Moonshadow",	"Moor",			"Moorish",		"Moss",			"Motivated",	"Mountain",		"Mountainous",	"Mournful",		"Muddy",		"Mulberry",		"Museum",				"Mutant",		"Mysterious",	"Mystery",		"Mystic",		"Mystical",		"Mystique",			"Mythic",		"Mythical",	"Mythological",	"Maelstrom",	"Magic",			"Magma",		"Magnetic",		"Mahogany",		"Majestic",		"Maleficent",	"Malevolent",	"Malicious",	"Malign",		"Mammoth",		"Mandrake",		"Maned",		"Mangrove",		"Manticore",	"Manticorian",	"Mantle",		"Marble",			"Marine",	"Maroon",		"Marsh",		"Marshy",			"Martial",	"Martian",		"Marvelous",	"Masked",			"Masterful",	"Mausoleum",	"Mauve",		"Maverick",		"Maze",			"Meadow",		"Mecha",		"Medallion",	"Medieval",		"Meditative",	"Medusian",		"Melancholic",	"Melancholy",	"Meld",			"Melodic",		"Memento",			"Menacing",	"Menagerie",	"Mental",			"Merciless",			"Mercurial",	"Meridian",			"Merlinian",			"Master",		"Marine",		"Mermaid",	"Merry",		"Mesopotamian",	"Messianic",	"Meteor",		"Meteoric",		"Meteoritic",	"Metropolis",	"Midnight",		"Mighty",		"Militant",		"Millennial",	"Mine",			"Ministerial",	"Minotaur",		"Minotaurine",	"Minstrel",		"Miraculous",		"Mirage",		"Mirror",		"Mirthful",		"Mischievous",		"Missionary",	"Mist",			"Mistral",	"Malachite",	"Mighty",		"Moon",			"Moonlit",		"Mysterious",	"Moon",			"Mist",			"Mind",			"Mad",			"Mad",			"Magic",		"Magma",		"Marine",		"Mental",		"Mirror",		"Mist",			"Minotaur",		"Moon",			"Mutant",		"Meteor",		"Mythic",		"Mythic",		"Mighty",	"Monstrous",	"Monstrous",	"Moonlight",	
				]
		descriptor += [ # N
			"Nomad",		"Natural",		"Nautical",		"Notorious",	"Nomadic",		"Nocturnal",	"Noble",		"Nimble",		"Nefarious",	"Noble",		"Nasty",		"Nocturnal",	"Noble",		"Nimble",		"Nefarious",		"Nasty",		"Nebular",		"Notorious",	"Nomadic",	"Nocturnal",	"Nimble",		"Nefarious",	"Noble",	"Nordic",		"Nemean",		"Noble",		"Nordic",		"Nether",		"Neon",		"Nemesis",	"Night",		"Nocturnal",	"Nova",			"Nebulous",						"Nature",		"Night",		"Night",		"Nightmare","Nasty",		"Nautic",		"Nebula",		"Nebular",		"Nebulous",		"Nemean",		"Nemesis",	"Neon",					"Nether",		"Northern",		"Neutron",		"New",			"Nexus",		"Night",		"Nightmare",	"Nimble",		"Nimbus",		"Nirvana",		"Nocturnal",	"Nomadic",		"Nordic",		"Norman",		"Notorious",	"Nova",			"Nun",			"Natural",		"Nature",		"Nocturnal",	"New",			"New",			"Nightmare",	"Night",		"Nocturnal",	"Nebula Born",
			]
		descriptor += [ # O
			"Orchid",		
			"Ozone",		
			"Old",			
			"Old",				
			"Other",			
			"Old",						
			"Oasis",			
			"Oblivion",			
			"Observatory",			"Obsidian",			"Obsolete",			"Occult",			"Ocean",			"Oceanic",			"Ochre",						"Odious",			"Offensive",			"Old",			"Olive",			"Olympian",			"Omen",			"Ominous",			"Omniscient",			"Only",			"Onyx",			"Opal",			"Opalescent",					"Opposed",			"Oppressive",			"Optimistic",			"Opulent",						"Oracular",			"Orange",			"Orb",			"Orbit",			"Orbital",			"Orbiting",			"Orchard",			"Orchid",			"Orphean",			"Otherworldly",	 "Outlandish",			"Outpost",			"Outraged",			"Outrageous",	"Overgrown",	"Overlord",			"Owl",			"Ozone",		"Order",			"Oceanic",			"Orange",			"Old",			"Otherworld",
			]
		descriptor += [ # P
			"Power",			"Phantom",		"Prismatic",		"Prehistoric",	"Petrifying",		"Petrified",		"Perplexing", 		"Pensive",	"Political",		"Polar",			"Primordial",		"Perpetual",		"Perennial",		"Purifying",		"Pure",		"Primeval",			"Plague",			"Pain",				"Palace",	"Pathfinder",		"Patriarch",			"Patriarchal",		"Paw",	"Peaceful",			"Pearl",			"Pearlescent",		"Peat",					"Pendant",			"Pensive",			"Perceptive",		"Peregrine",		"Perennial",		"Perilous",	"Pernicious",		"Perpetual",			"Petal",			"Petrified",			"Phalanx",			"Phantasm",			"Phantasmagorical",				"Phantasmal",		"Phantom",			"Pharaonic",		"Pharaonic",		"Philosophical",	"Phlegmatic",		"Phoenix",			"Phoenixian",		"Phylactery",		"Pietistic",		"Pillar",			"Pine",				"Pinnacle",			"Pioneering",		"Piqued",						"Placid",			"Plague",			"Planar",			"Planetary",			"Plasma",			"Plateau",			"Platinum",		"Pleasant",				"Plucky",			"Plum",				"Poet",				"Poetic",			"Poignant",			"Poisonous",		"Polar",			"Pond",				"Ponderous",		"Pontifical",		"Poppy",			"Porcelain",		"Port",							"Potent",			"Potion",			"Powder",			"Power",			"Poker",			"Powerhouse",			"Prairie",			"Plague",		"Precious",		"Precocious",	"Predatory",	"Preternatural",	"Primal",			"Prime",			"Primeval",			"Primordial",		"Princely",			"Prismatic",		"Prison",			"Private",			"Profound",			"Prohibition",		"Promethean",		"Prophetic",		"Prosperous",		"Protected",		"Proud",		"Psion",		"Pugnacious",		"Pulsar",		"Pulsating",		"Pumpkin",		"Pungent",		"Punk",			"Pure",			"Purifying",	"Purist",		"Purple",			"Puzzled",			"Pyramid",			"Pyro",				"Palm",				"Pandemonium",		"Panicked",			"Papal",			"Paradox",			"Paradoxical",		"Parched",			"Parish",			"Park",				"Parliament",		"Passionate",		"Pack",				"Phantom",			"Primal",			"Pillager",			"Power",			"Powerful",			"Pain",			"Pack",			"Pain",			"Pure",						"Plague",			"Primal",			"Prehistoric",		"Primigenial",		"Primordial",		"Proud",			"Planar",
			]
		descriptor += [ # Q
			"Quest",	"Quicksand",			"Quantum",			"Quartz",			"Quasar",			"Queen",						"Quest",			"Questing",			"Quick",			"Quicksand",			"Quicksilver",			"Quiet",			"Quill",	"Quicksilver",
			]
		descriptor += [ # R
			"Rebellion",	"Rugged",       "Runic",		"Relentless",	"Ritualistic",	"Rogue",		"Risen",		"Restless",		"Requiem",		"Relic",		"Rippling",			"Reality",		"Raging",		"Radiant",		"Rhythm",		"Rising",		"Raging",		"Ragnarok",		"Rain",		"Renegade",		"Rule",		"Runewielder",	"Rainbow",		"Rainforest",	"Rainstorm",		"Rampant",		"Rampart",		"Ranch",		"Rancorous",		"Rising",		"Rose",			"Restless",		"Red",			"Rosethorn",	"Raid",			"Red",			"Red",			"Rule",			 "Rat",	"Rational",		"Ravaged",			"Ravaging",		"Radiant",		"Reality",		"Reckless",		"Reckoner",		"Reckoning",		"Reclusive",		"Red",			"Redoubtable",		"Redwood",		"Reef",	"Refined",		"Regal",		"Regulation",		"Relaxed",		"Relentless",		"Relic",		"Remnant",		"Remote",		"Renaissance",		"Renegade",		"Reptilian",	"Repugnant",	"Resentful",	"Resilient",	"Resolute",		"Resounding",	"Resplendent",		"Revered",		"Reverent",		"Rhapsodic",	"Radiant",		"Rhombus",		"Ribbon",		"Rich",			"Riddle",		"Ridge",		  "Rift",		"Righteous",	"Rime",		"Rippling",		"River",	"Riverine",		"Roaming",		"Robotic",		"Rock",		"Rocky",		"Rod",		"Rogue",		"Roman",		"Rooted",		"Rosaline",		"Rose",			"Rosy",			"Royal",		"Ruby",			"Rugged",		"Ruined",		"Ruins",			"Rule",			"Rune",			"Runecarved",		"Runewielder",	"Runic",		"Rural",		"Rust",			"Rustic",		"Rusty",		"Ruthless",	"Rune",			"Rune",				"Red",				"Rainstorm",	"Red",				"River",				"Rogue",		"Rune",				"Riding",		"Roaring",
			]
		descriptor += [ # S
			"Starship",	"Shadow",			"Silver",			"Star",				"Sparkling",		"Shining",			"Structures",		"Stellar",			"States",			"Supernova",			"Sunset",				"Sunny",			"Sun",				"Starry",			"Star",				"Space",			"Silvertongued",	"Sempiternal",		"Sorrel",			"Swan",				"Stormchaser",		"Stingray",			"Starship",				"Strength",				"Sunblessed",		"Sun",				"Shadow",			"Secret",			"Supreme",			"Strong",			"Supreme",			"Star",				"Sylvan",			"Shadow",				"Sacred",				"Subterranean",		"Solemn",			"Sorrow",				"Mourning",				"Grief",				"Solar",			"Spirit",			"Shade",			"Stalker",			"Stargazer",		"Stellar",			"Sublime",			"Slaying",			"Saga",					"Sagacious",		"Saint",						"Sanctuary",		"Sand",				"Sandy",			"Sanguine",			"Sanskrit",			"Sapphire",			"Satellite",						"Satyric",			"Savanna",			"Savannah",			"Savant",			"Savvy",			"Scaled",			"Scarab",			"Scarlet",			"Scenic",			"Scented",			"Scepter",						"Scholarly",			"School",			"Science",			"Scientific",		"Scintillating",	"Scion",			"Scorching",		"Scroll",			"Sea",				"Seal",					"Seashore",				"Seasonal",			"Secluded",			"Second",			"Secret",			"Secretive",			"Skeletal",			"Mercenary",		"Seductive",		"Seismic",			"Selenian",			"Sempiternal",		"Sensual",				"Sentimental",			"Seraphic",			"Serene",			"Serpentine",		"Seventh",			"Sewer",			"Seychelle",		"Shade",				"Shaded",				"Shadow",			"Shadowy",			"Shallow",			"Shamanic",			"Shark",			"Shattered",		"Shattering",		"Shield",			"Shielded",			"Shimmering",			"Shining",				"Shivering",		"Shore",			"Shrewd",			"Shrine",			"Sickly",			"Sienna",			"Sigil",			"Silent",			"Silver",			"Silvertongued",		"Simian",				"Singing",			"Sinister",			"Siren",			"Sirenian",			"Sirenic",			"Skeleton",			"Sky",				"Skyborn",			"Skyborn",			"Slate",			"Sleeping",			"Slimey",				"Sly",				"Smart",			"Soul",				"Soulbound",		"Soulfire",			"Soulful",			"Space",			"Spark",			"Sparkling",		"Spartan",				"Spectral",				"Spell",			"Spellbound",		"Spined",			"Spiral",			"Spire",			"Spiritual",		"Spiteful",			"Splendid",			"Spring",			"Sprouting",		"Stadium",				"Staff",			"Stalwart",			"Standard",			"Star",				"Star-born",				"Star-crossed",			"Star-crosser",		"Starborn",			"Starcrossed",		"Starcrosser",		"Starfall",			"Starlit",				"Starry",				"Stars",		"Starting",			"Statute",			"Steadfast",		"Stealthy",			"Steam",			"Steamy",			"Steelhearted",		"Stellar",			"Stern",			"Stinger",			"Stoic",			"Stone",			"Storm",			"Stormbringer",		"Stormcaller",		"Stormy",			"Strait",			"Strategist",		"Stratospheric",	"Stream",		"Strong",				"Sea",							"Stunning",		"Stygian",			"Sublime",			"Subterranean",		"Subtle",			"Sulfuric",			"Sullen",			"Summer",			"Sun",				"Sunborn",			"Sunder",			"Sunflare",			"Sunlit",			"Sunny",			"Sunset",			"Sunstone",			"Superb",			"Supernatural",		"Supernova",		"Supreme",			"Suspicious",		"Swamp",			"Swampy",				"Sweet",			"Swift",			"Sympathetic",		"Synthesis",		"Star", 			"Star",				"Silent",			"Stealth",			"Sea",				"Shadow",			"Smoke",			"Shelled",			"Snowy",			"Solar",			"Solstice",			"Sophisticated",	"Sorcery",				"Sorrowful",		"Stone",			"Sky",				"Slinking",			"Scorched",			"Supreme",				"Spell",			"Spark",			"Star",				"Storm",			"Skull",			"Spark",			"Sylvan",			"Sylvan",			"Solstice", 		"Sand",				"Sand",				"Seventh",			"Second",			"Stone",			"Silver",			"Silk",								"Science",				"Shadow",			"Scale",			"Smoke",			"Sneaky",			"Spring",				"Steam",			"Storm",			"Starting",			"Star",				"Strong",			"Spark",			"Spell",			"Solar", 			"Summer",			"Spirit",			"Starry",			"Stellar",			"Sacred",			"Soul",				"Solar",			"Steel",			"Spirit",
				]
		descriptor += [ # T
			"Tireless",			"Treasure",			"Treasure",			"Thorn",			"Twisted",			"Talisman",			"Thorn",			"Timeless",			"Temporal",			"Timebender",		"Time",				"Traditional",		"Timeless",			"Timely",			"True",				"Tenacity",			"Treasure",			"Tomb",				"Time",			"Tomb",				"Tormented",		"Tempest",		"Troll",		"Talisman",	"Tigerstrip",			"Time",				"Timeless",			"Time",				"Titanic",			"Token",			"Tomb",				"Trick",			"Topaz",			"Torch",			"Totem",			"Town",				"Traditional",		"Trail",			"Trance",		"Tranquil",			"Transcend",		"Transcendent",		"Transient",		"Traveling",	"Treacherous",	"Tremendous",		"Tribal",			"Tribe",			"Tribunal",			"Trickster",		"Trojan",			"Tropical",			"True",				"Tudor",			"Tulip",			"Tundra",			"Turbulent",		"Turquoise",		"Turtle",			"Twilight",			"Twisted",			"Typhoon",			"Talon",		"Tangerine",		"Tartarean",		"Taupe",			"Tavern",			"Teal",			"Tectonic",		"Tempest",			"Tempestuous",		"Temple",		"Temporal",		"Tenacious",		"Tender",		"Tentacled",		"Terra",			"Terrifying",		"Thaumaturge",		"Theater",			"Theocratic",		"Thicket",			"Third",			"Thorn",			"Thorny",			"Thousand",			"Threatening",		"Thunder",		"Thundering",		"Thunderous",		"Tidal",			"Tide",				"Timeless",		"Thorn",		"Talisman",		"Threatening",		"Time",		"Time-bender",		"Timebender",		"Timeless",		"Titanic",		"Twilight",			"Terrifying",		"Terrorific",		"True",				"Tower",			"Thunder",			"Thunder",			"Tomb",				"Third",			"Trival",			"Thunder",			"Terrifying",		"Treasure",			"Throne",			"Tide",				"Time",			"Timeless",
			]
		descriptor += [ # U
			"Unholy",		"Unnatural",	"Urban",		"Unyielding",			"Untamed",		"Underdark",		"Underworld",				"Undying",				"Unearthly",				"Unfathomable",				"Unflinching",				"Unforgiving",				"Unhappy",				"Universal",				"Universe",								"Unrevealed",				"Unseen",				"Unstoppable",				"Untamed",				"Unyielding",				"Uplifting",	"Uranian",		"Ursine",		"Utopic",		"Ultimate",			"Ultra",			"Ultra",			"Ultraviolet",			"Unassailable",			"Unbound",			"Unbreakable",			"Uncharted",			"Unconquerable",			"Undaunted",			"Undertow",			"Unholy",				"Underworld",
			]
		descriptor += [ # V
			"Voltaic",		"Venerable",	"Venom",		"Venom",		"Venomous",		"Verdant",		"Vicious",			"Vigilant",			"Vigorous",			"Virtuous",			"Volcano",				"Volcanic",				"Voided",			"Void",				"Vintage",		"Venerable",		"Victorian",		"Valor",			"Valiant",			"Valkyrian",		"Valkyrie",								"Valley",				"Valor",				"Vampiric",		"Vanirian",		"Vault",		"Vapor",		"Vaporous",		"Vase",			"Veiled",			"Victorious",		"Vigilant",			"Viking",				"Village",			"Villainous",		"Vindicator",	"Vindictive",		"Vine",				"Vintage",			"Violent",			"Violet",			"Viridian",				"Virtuoso",				"Virtuous",				"Virulent",				"Visage",			"Visionary",				"Vitriolic",	"Void",			"Vengeful",		"Voidborne",	"Voided",		"Voidless",		"Volatile",			"Volcanic",			"Volcano",				"Voracious",		"Vortex",			"Vulcanian",		"Vulpine",			"Void",				"Void",				"Void",				"Vengeance",				"Vellum",				"Vendetta",				"Venerable",				"Vengeance",				"Vengeful",				"Venomous",		"Valiant",		"Venusian",		"Verdant",		"Vermilion",	"Vernal",		"Vertex",		"Vesper",		"Vesperal",			"Vessel",			"Veteran",			"Vibrant",			"Vicar",			"Vicious",			"Violet",			"Valiant",			"Vampiric",				"Veteran",				"Venom",				"Vicious",				"Volcanic",				"Venom",
			]
		descriptor += [ # W
			"Whitescale",	"Whisper",     "Waterwind",		"Walking",			"Wandering",		"Wealth",			"War",				"Waterborn",		"Water",			"Water",			"Wave",				"Whim",				"Whisper",		"Wholesome",		"Wild",			"Windborn",		"Wind",			"Windborn",		"Winged",		"Winter",		"Wooden",		"Wisdom",		"Witch",			"Wise",				"Winterborn",		"Wolf",			"Wrathful",		"Witty",			"Wandering",		"White",			"War",				"Wormhole",			"Warp",				    "Winter",			"Windy",			"Wind",				"Wailing",			"Wind",				"Wild",				"Wind",			"Wood",				"Wand",			"Wave",			"Wandering",	"War",						"Warp",			"Warping",		"Wary",				"Water",			"Watery",		"Wave",			"Wavy",				"Weapon",			"Weatherlight",		"Web",				"Western",							"Whale",			"Whimsy",			"Whirlwind",		"Whispering",		"Whistle",			"White",			"Wicked",		"Wight",			"Wild",				"Wilderness",	"Wildfire",		"Willow",		"Windy",		"Winged",		"Winter",		"Winterborn",		"Wise",			"Wisp",			     "Witchy",		"Withering",		"Witted",			"Wondrous",			"Woodland",			"Woods",			"Woody",			"Workshop",			"World",			"Wormhole",						"Wrathful",			"Woodland",			"Wind",			"White",			"Water",			"War",			"Warp",			"War",			"Warping",		"Water",		"White",		"Wise",				"Wind",			"Winter",		"Wild",				"Wolf",				"Wind",			"Wild",			"Wicked",
			]
		descriptor += [ # X
			"X-Ray",			"Xenolith",			"Xenon",
			]
		descriptor += [ # Y
									"Yearning",				"Yesteryear",								"Youthful",				"Yellow",
				]
		descriptor += [ # Z
			"Zephyr",	"Zodiacal",		"Zodiac",			"Zombie",			"Zealot",			"Zealous",			"Zen",			"Zenith",			"Zephyr",			"Zephyrian",			"Zestful",			"Zeusian",			"Zodiac",			"Zodiacal",			"Zone",			"Zoo",			"Zypher",			"Zombie",
			]
	except:
		descriptor += ["Dark"]

	# Backgrounds
	if "Barbarian"	in genus:
		descriptor += [
			"Frantic",	"Raging",		"Wild",		"Fierce",		 "Savage",		 "Untamed",		 "Mighty",
			]
	if "Berserker"	in genus:
		descriptor += [
			"Frantic",	"Raging",		"Wild",		"Frenzy",		"Unstoppable",		"Fury",		"Fierce",		 "Savage",		 "Untamed",		 "Mighty",		 "War",		 "Warrior",
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
				"Village",
		]
	if "Crafter" 	in genus:
		descriptor = [
		"Voltaic",		"Mender",		"Master",		"Skillful",		"Artisanal",		"Dexterous",		"Inventive",
		]
	if "Criminal" 	in genus:
		descriptor += [
			"Barber",		"Mercenary",				"Crime",		"Underworld",		 "Sneaking",		 "Sneaky",		 "Ruthless",		 "Shade",		 "Shady",		 "Clever",
			]
	if "Cleric"		in genus:
		descriptor += [
			"Sun",			
			"Sun",			
			"Sun",
			"Sacred",		
			"Sacred",		
			"Hallowed",
			"Dawn",			
			"Dawn",			
			"Radiant",
			"Celestial",	
			"Oracular",		
			"Penitent",
			]
	if "Druid" 		in genus:
		descriptor += [
			"Tusked",			
			"Jungle",			
			"Natural",			
			"Earthy",			
			"Mystical",			
			"Primal",			
			"Guardian",			
			"Green",			
			"Fern",
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
			"Guardan",	"Guarding",	"Protector",	"Alert",		"Discipline",		"Protector",
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
			"Monastery",	"Monastic",	"Artisan",	"Grace",	"Celestial",	"Urn",				"Discipline",				"Spiritual",				"Meditative",				"Ascetic",				"Harmony",
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
				"Ruthless",			"Swashbuckling",				"Seafaring",							"Rebel",			"Infamous",				"Treasure",			"Booty",			"Dock",
				]
	if "Traveler"	in genus:
		descriptor += [
			"Migratory",			"Nomadic",			"Nomad",			"Roaming",			"Traveling",			"Wandering",			"Circus",
			]
	if "Trickster" 	in genus:
		descriptor += [
			"Surviving",			"Quick",			"Lonely",			"Resourceful",			"Scrappy",			"Streetwise",			"Surviving",			"Scrappy",			"Quick",
			]
	if "Priest"		in genus:
		descriptor = [
			"Celestial",	
			"Chapel",
			"Clerical",
			"Devout",
			"Faithful",
			"Holy",
			"Pious",
			"Sacred",
			]
	if "Ranger" 	in genus:
		descriptor += [
			"Troll",		
			"Troll",		
			"Troll",
			"Wild",			
			"Wild",			
			"Thorn",
			"Thorn",		
			"Hollow",		
			"Beast",
			"Green",			
			"Jungle",			
			"Wilderness",			
			"Tracking",			
			"Survivalist",			
			"Rugged",			
			"Master",			
			"Survival",			
			"Rugged",
			]
	if "Rogue" 		in genus:
		descriptor += [
			"Sneaky",  
			"Masterful",		  
			"Cunning",		  
			"Agile",		  "Mysterious",	  
			"Resourceful",		  
			"Shady",		  
			"Shadow",
		  ]
	if "Scholar" 	in genus:
		descriptor += [
			"Learned",	"Learned",	"Learned",			"Intellectual",	"Intellectual",	"Intellectual",			"Studious",	"Studious",	"Studious",			"Erudite",	"Erudite",	"Erudite",			"Inquisitive",	"Inquisitive",	"Inquisitive",
			]
	if "Soldier" 	in genus:
		descriptor += [
			"Veteran",	
			"War",	
			"Battle",	
			"Hardened",		
			"Strategic",	
			"Brave",	
			"Tactical",	
			"Special",	
			"Tactical",	
			"Brave",		
			"Last",	
			"First",	
			"Battle",	
			"Hardened",	
			"Hierarchy",			
			"Strategist",
				]
	if "Shaman" 	in genus:
		descriptor += [
			"Green",			
			"Jungle",			
			"Spiritual",			
			"Mystic",
			"Oracular",		
			"Elemental",			
			"Tribal",			
			"Ancestral",			
			"Shamanic",
			]
	if "Spy" 		in genus:
		descriptor += [
			"Spy",			
			"Undercover",			
			"Covert",			
			"Undercover",			
			"Secret",			
			"Stealthy",			
			"Infiltrating",			
			"Covert",			
			"Undercover",			
			"Secret",			
			"Stealthy",			
			"Infiltrating",
			]
	if "Traveler" 	in genus:
		descriptor += [
			"Jungle",			
			"Wandering",		
			"Adventure",			
			"Nomad",			
			"Curious",			
			"World",
			]
	if "Witch" 		in genus:
		descriptor += [
			"Enchanting",			
			"Hexing",			
			"Mystical",			
			"Occult",			
			"Wise",
			]
	if "Wizard" 	in genus:
		descriptor += [
			"Rune",			
			"Rune",			
			"Rune",
			"Spell",		
			"Spell",		
			"Void",
			"Star",			
			"Star",			
			"Arcane",
			"Knot",			
			"Oracular",		
			"Cryptic",
			]

	# Races
	if "Aberration" in genus:
		descriptor += [
			"Abhorrent",	"Starship",
			]
		if "Githzerai" 			in genus:
			descriptor += [
			"Enlightened","Zen",
			"Mystic",
			"Ascetic","Spiritual",
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
			"Tailed",		"Tusked",			"Wild",
			]
		if "Kong" 			in genus:
			descriptor += [
			"Kong",
			"Silverback",
			"Colossal",
			"Jungle",
			"Mighty",
			"Fierce",
			"Vigilant",
			"Primal",
			"Island",
			"Ancient",
			"Titan",
			"Colossal",
			"Untamed",
			]
		if "Armored Bear" 	in genus:
			descriptor += [
				"Bear",
				"Iron",
				"Armor",
				"Ice",
				"Claw",
				"Northern",
				"Claw",
				"Stalwart",
				"Ursine",
				"Ursa",
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
		descriptor += [ 	"Amber",	"Astral",	"Blessed",	"Celestial",	"Divine",	"Ethereal",	"Fire",	"Flame",		"Golden",	"Green",	"Heavenly",	"Radiant",	"Sacred",		"Shadow",	"Sky",	"Sublime",	"Yellow",	"Luminous", 	"Celestial", 	"Darkness",	"Divine",		"Ethereal", 	"Flame",	"Golden",	"Green",		"Heavenly",	"Radiant", 		"Shadow",	"Sky", 
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
			"Electrostatic",	"Puppeteer",	"Clockwork",	"Living",			"Titanium",		"Iron",			"Steel",	"Palladium",
			]

	if "Dwarf"		in genus:
		descriptor += [
			"Anvil",
			"Forge",
			"Deep",
			"Stone",
			"Rune",
			"Clan",
			"Dwarven",
			"Tunnel",
			]
	if "Dragon"		in genus:
		descriptor += [
		"Tailed",		"Draconic",
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
			"Star",		
			"Moon",		
			"Silver",	
			"Glimmer",
			"Leaf",	
			"Exquisite",	
			"Thorn", 		
			"Elven",	
			"Elven",
			"Elven",
			"Elven",	
			"Elvish",
			]
	if "Fiend" 		in genus:
		descriptor += [
			"Tailed",		"Fiendish",		"Hellish",		"Satanic",
			]
	if "Fae"		in genus:
		descriptor += [
			"Vendilion",
			]
	if "Giant"		in genus:
		descriptor += [
			"Troll",
			"Stone",
			"Peak",
			"Mountain",
			"Boulder",
			"Gigantic",
			]
	if "Gnome"		in genus:
		descriptor +=[
		"Gnomish",
		]
	if "Goblin"		in genus:
		descriptor += [
			"Knot",			"Knot",			"Knot",
			"Cave",			
			"Grease",		
			"Trick",
			"Shadow",		
			"Sly",			
			"Scrap",
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
		"Bituminous",	"Amber",
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
			"Undying",		"Deathless",	"Grave",		"Sepulchral",
			"Necrotic",		"Withered",		"Hollow",		"Cadaverous",
			"Pallid",		"Restless",		"Mournful",		"Shrouded",
			"Grim",			"Eternal",		"Cursed",		"Spectral",
			]
		if "Skeleton" in genus:
			descriptor += [
				"Bone",			"Rattling",		"Fleshless",	"Marrowless",
				]
		elif "Zombie" in genus:
			descriptor += [
				"Rotting",		"Shambling",	"Putrid",		"Decaying",
				]
		elif "Ghost" in genus or "Spectre" in genus or "Spirit" in genus:
			descriptor += [
				"Phantom",		"Wailing",		"Ethereal",		"Haunting",
				]
		elif "Wraith" in genus or "Wight" in genus:
			descriptor += [
				"Shadowed",		"Gravebound",	"Soulchilled",
				]
		elif "Lich" in genus:
			descriptor += [
				"Phylactered",	"Soulcaged",	"Dreadful",		"Arcane",
				]
		elif "Mummy" in genus:
			descriptor += [
				"Bandaged",		"Embalmed",		"Ancient",		"Desiccated",
				]
		elif "Revenant" in genus:
			descriptor += [
				"Vengeful",		"Returned",		"Oathbound",
				]
		elif "Ghoul" in genus:
			descriptor += [
				"Ravenous",		"Carrion",		"Gravehungry",
				]
	if "Vampire" 	in genus:
		descriptor += [
			"Blood",		"Blood",		"Blood",
			"Night",		"Night",		
			"Nocturnal",
			"Crimson",		
			"Pale",			
			"Sanguine",
			"Bloodcursed",	
			"Bloodsoaked",	
			"Vampiric",
			"Dark Sun",		
			"Sun",			"Sun",			
			"Bloodtithe",
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
			"Dawnbringer",			"Daybreak",			"Daylight",			"Ethereal",			"Luminous",			"Morning",			"Radiant",			"Solar",			"Sunlit",			"Sunrise",
			]
	if "Nymph" 		in genus:
		descriptor += [
			"Forest",		"Graceful",			"Nature",			"Nymph",			"Water",
			]
	if "Celestial" 	in genus:
		descriptor += [
			"Divine",			"Holy",			"Celestial",			"Celestian",
			]
	if "Angel" 		in genus:
		descriptor += [
			"Angelic",
			"Divine",
			"Holy",
			"Messenger",
			"Seraphic",
			"Winged",
			]
	if "Atlantian" 	in genus:
		descriptor += [
			"Ancient",
			"Aquatic",
			"Deepsea",
			"Nautic",
			"Ruinbound",
			]
	if "Dragonborn" in genus:
		descriptor += [
			"Tailed",		"Blueblood",			"Dragonborn",
			"Fireblood",			"Greenblood",
			"Iceblood",			"Nightblood",
			]
	if "Noble" 		in genus:
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
	if "Hunter" 	in genus:
		descriptor += [
		"Primal",

		]
	if "Monkey King" in genus:
		descriptor += [
			"Tailed",
			"Cunning",
			"Mammalian",
			"Mighty",
			"Monkey",
			"Tricking",
			"Tricksy",
			"Whimsy",
			"Adventuring",
			]
	if "Birdfolk" 	in genus:
		descriptor += [
			"Flying",
			"Songbird",
			]
	if "Cleric" 	in genus:
		descriptor += [
			"Devout",
			"Golden",
			"Holy",
			"Righteous",
			"Spiritual",
			"Blessed",
			]
	if "Beast" 		in genus:
		descriptor += [
			"Tailed",		"Jungle",		"Sylvan",			"Nature",			"Beast",
			]
	if "Chaotic" 	in genus:
		descriptor += [
			"Anarchic",
			"Erratic",
			"Mad",
			"Unpredictable",
			"Whimsical",
			"Free",
			]
	if "Dragon" 	in genus:
		descriptor += [ 	
			"Tailed",		
			"Clever", 
			"Destroyer",		
			"Draconic",		
			"Eternal",		
			"Evil",		
			"Fierce",		
			"Fierce", 
			"Fire",		
			"Flame",		
			"Furious",		
			"Gentle",		
			"Great",		
			"Grumpy",				
			"Intelligent",		
			"Jealous",		
			"Jungle",	
			"Kind",		
			"Magnificent",		
			"Magnificent",		
			"Majestic",	
			"Maximum",		
			"Mysterious",		
			"Powerful",		
			"Scaled",	
			"Sky",			
			"Strong",		
			"Stubborn",		
			"Voiceless",	
			"Winged",		
			"Legendary",	
			"Wise",		
			"Reptile", 
			"Magnanimous", 
			]
		if "Chromatic" in genus:
			descriptor += [
				"Chromatic",

				]
		if "Metallic" in genus:
			descriptor += [
				"Metallic",
				]
		if "Prismatic" in genus:
			descriptor += [
				"Prismatic",
				]
		if "Red" in genus:
			descriptor += [	
				"Red",			"Fireborn",				"Fireblood",				"Firewing",				"Fireclaw",				"Firetail",				"Firescale",				"Firewing",				"Fireclaw",				"Firetail",				"Firescale",				"Crimson", "Flameborn", "Volcanic", "Furious"
				]
		if "Green" in genus:
			descriptor += [
				"Green", "Emerald", "Acidic", 
				]
		if "Blue" in genus:
			descriptor += [
				"Blue", "Electric", "Desertic"
				]
		if "Black" in genus:
			descriptor += [
				"Black", "Shadow", "Necrotic", "Deathly",   "Haunting",  "Dark",
				]
		if "White" in genus:
			descriptor += [
				"White", "Ice", "Frost", "Cold", "Winter", "Snow", "Frozen", "Frostborn", "Iceborn", "Iceblood", "Icewing", "Iceclaw", "Icetail", "Icecale", "Icewing", "Iceclaw", "Icetail", "Icecale", "Frostborn", "Iceborn", "Iceblood", "Icewing", "Iceclaw", "Icetail", "Icecale",
				]
		if "Gold" in genus:
			descriptor += [	
				"Gold", "Golden", "Sun", "Sunlight", "Sunlit",   "Sunrise", "Sunset", "Sunstone", "Sunflare",  
				]
		if "Silver" in genus:
			descriptor += [
				"Silver", "Silver", "Moon", "Moonlight", 
				]
		if "Bronze" in genus:
			descriptor += [
				"Bronze",
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
	if "Undead" in genus:
		descriptor += [
			"Morgue",		
			"Cursed",	
			"Urn",		
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
			"Arcane",
			"Tarot",
			]
	if "Illithid" in genus:
		descriptor += [
			"Mind", 
			"Psionic", 
			"Telepathic", 
			"Brain", 
			"Thought", 
			"Cerebral",			
			"Deep",			
			"Dimensional",			
			"Dream",			
			"Eldritch",			
			"Illithid",			
			"Inscrutable",			
			"Insidious",			
			"Mindbending",		
			"Otherworldly",			
			"Psionic",			
			"Shadowspeaker",	
			"Soul",		 		
			"Telepathic",			 
			"Thought",			
			"Trascendent",	
			"Voidborn",			
			"Void",			
			"Warp", 
			"Astral",
			]
	if "Shapeshifters" in genus:
		descriptor += [
			"Amorphous", "Changeling", "Formless", "Mimic", "Mutant", "Protean",
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
			"Arcane",
			"Sorcery",
			"Sorcerous",
			"Portal",
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
			"Amber",			"Caustic",			"Contaminated",	"Dark",			"Demon",			"Demonic",			"Diabolical",			"Fiendish",			"Hell",			"Infernal",			"Liar",			"Malevolent",			"Red",			"Sinister",			"Unholy",
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
			"Arcane",	"Arcane",			"Black",			"Blue", 	"Crimson", 	"Enigmatic",	"Golden",			"Green",			"Grey",			"Learned",			"Mystical",			"Rainbow",			"Red",			"Scholar",			"Sorcerous",			"Spellbinder",			"White",			"Yellow",
			]
	if "Ooze" in genus:
		descriptor += [
			"Absorbing",		  "Absorbing",		  "Acidic",		  "Amorphous",		  "Amorphous",		  "Ashen",		  "Crystalline",		  "Cubic",	"Earthen",		  "Fiery",		  "Fluidic",		  "Fungal",		  "Gelatinous",		  "Gelatinous",		  "Glowing",		  "Icy",		  "Mystical",		  "Poisonous",		  "Shapeless",		  "Shapeless",		  "Slime",		  "Slithering",		  "Slithering",		  "Sticky",		  "Thick",		  "Translucent",		  "Viscous",		  "Viscous",		  "Viscous",
			]
	if "High" in genus:
		descriptor += [
			"Elevated",			"High",			"Refined",
			]
	if "Merchant" in genus:
		descriptor += [
			"Bountiful",
			]
	if "Crafter" in genus:
		descriptor += [
			"Voltaic",	"Crafty",	"Urn",
			]
	if "Mountain" in genus:
		descriptor += [
			"Crafty",	"Rugged",		"Snowy",			"Stoic",			"Unyielding",			"Enduring",			"Harsh",			"Mountain",			"Resilient",			"Earthen",			"Stone",			"Deep",			"Rooted",			"Gritty",			"Metalwork",			"Ancestral",			"Tough",			"Boulder",			"Unmovable",			"Iron",			"Strong",			"Mining",			"Gem",			"Ore",			"Frost",	"Ale",		"Echo",			"Gold",			"Silver",			"Mithril",			"Carver",
			]
	if "Sea" in genus:
		descriptor += [
			"Aquatic",			"Piscine",			"Coastal",			"Maritime",			"Oceanic",			"Gilled",
			]
	if "Etherian" in genus:
		descriptor += [
			"Voltaic",	"Ethereal",			"Luminous",			"Heavenly",			"Celestial",			"Stardust",
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
			"Tender",			
			"Hopeful",  
			"Jubilant", 
			]
	if "Evil"		in genus:
		descriptor += [
			"Dark",			
			"Evil",		
			"Malignant",	
			"Cruel",	
			"Foul",
			"Nefarious", 	
			"Angry",	
			"Jealous",	
			"Hostile",
			]
	if "Lawful" 	in genus and "Good" in genus:
		descriptor += [
			"Holy",
			]

	descriptor += [
		"Storm",
		"Sky",
		"Green",		
		"Angelic",		
		"Amethyst",		
		"Amber",		
		"Amber",	
		"Hollow",	
		"Empty",			
		"Arcane",
		"Alchemical",
		"Apothecarian",
		"Arcanic",			
		"Magical",			
		"Wand",
		"Wizard",			
		"Arcane", 
		"Alchemical",			
		"Arcanic", 
		"Magic",			
		"Wand", 
		"Wizardry", 
		"Myrmidon", 
		"Mystic", 
		"Mystical", 
		"Mythical",	
		"Lavender",	
		"Oceanic",	
		"Glacial",	
		"Blind",
		"Mad",	
		"Gallant",
		"Generous",
		"Kind",
		"Unbreakable",
		"Valiant",	
		"Orphean",
		"Abyssal", 
		"Daemonian", 
		"Hellish",		
		"Holy", 		
		"Crystal",		
		"Earth",	
		"Omniscient",	
		"Magenta",	
		"Yellow", 
		"Golden", 
		"Goldenrod",
		"Ochre",					
		"Lime",					
		"Green", 
		"Jade",
		"Olive",					
		"Azure", 
		"Blue", 
		"Cerulean",
		"Indigo",					
		"Lavender",					
		"Ivory",
		"Graphite",					
		"Iridescent",					
		"Gold",
		"Golden",					
		"Graphite",
		"Onyx",					
		"Ivory",				
		"Gemmed",		
		"Jewel",		
		"Jewelcraft",	
		"Eternal",		
		"Glimmer",		
		"Glaive",	
		"Gem",		
		"Ghost",	
		"Gale",		
		"Gaze",	
		"Jeweled",	
		"Northern",		
		"Opal",	
		"Jade",	 
		"Quartz", 		
		"Red", 		
		"Topaz",	
		"Xenolith",
		"Elfstone",		
		"Deep",		
		"Scrappy",		
		"Honor",		
		"Mighty",		
		"Fearless",		
		"Battle",		
		"Ghost",		
		"Cloud",		
		"Dream",	
		"Gloom",		
		"Golden",		
		"Graceful",		
		"Green",		
		"Grove",		
		"Heart",		
		"Hell",		
		"Hidden",		
		"High",			
		"Horn",			
		"Hydra",		
		"Lamp",			
		"Last",		
		"Leaf",		
		"Lore",		
		"Lost",		
		"Lunar",		
		"Magenta",		
		"Master",		
		"Maze",		
		"Mind",		
		"Mischief",		
		"Mystic",		
		"Night",		
		"Plains",		
		"Planar",		
		"Potion",		
		"Pride",		
		"Proud",		
		"Red",		
		"Rune",		
		"Sacred",		
		"Sky",		
		"Spell",		
		"Star",		
		"Silk",		
		"Stone",		
		"Story",		
		"Tunneling",		
		"Vine",		
		"Yellow",		
		"Reptile",		
		"Ruby",			
		"Turtle",	
		"Furious",	
		"Ghostly",	
		"Hesperidean",	
		"Ice",	
		"Illustrious",	
		"Imaginative",	
		"Inscrutable",	
		"Interstellar",	
		"Lagoon",	
		"Leviathan",	
		"Lime",	
		"Liquid",	
		"Lord",	
		"Lunar",	
		"Majestic",	
		"Malign",	
		"Martial",	
		"Merry",	
		"Meteor",	
		"Meteoric",	
		"Mighty",	
		"Mirthful",	
		"Monstrous",	
		"Moonlit",	
		"Mystical",	
		"Occult",	
		"Oracle",	
		"Oracular",	
		"Ordinance",	
		"Pathfinder",	
		"Peerless",		
		"Perennial",	
		"Perfumed",		
		"Perilous",		
		"Petrified",	
		"Phantom",		
		"Pillar",	
		"Piqued",	
		"Planetary",	
		"Plum",	
		"Poetic",	
		"Polar",	
		"Precocious",	
		"Predatory",	
		"Profound",	
		"Promethean",	
		"Protector",	
		"Psychic",
		]
	try:
		descriptor += [
			f"{lusor.archetype}",	
			f"{lusor.archetype}",	
			f"{lusor.archetype}",	
			f"{lusor.archetype}",	
			f"{lusor.archetype}",	
			f"{lusor.archetype}",	
			f"{lusor.archetype}",	
			f"{lusor.archetype}",	
			f"{lusor.archetype}",	
			f"{lusor.archetype}",
			f"{lusor.race}",		
			f"{lusor.race}",		
			f"{lusor.race}",		
			f"{lusor.race}",		
			f"{lusor.race}",		
			f"{lusor.race}",		
			f"{lusor.race}",		
			f"{lusor.race}",		
			f"{lusor.race}",		
			f"{lusor.race}",
			f"{lusor.subrace}",		
			f"{lusor.subrace}",		
			f"{lusor.subrace}",		
			f"{lusor.subrace}",		
			f"{lusor.subrace}",		
			f"{lusor.subrace}",		
			f"{lusor.subrace}",		
			f"{lusor.subrace}",		
			f"{lusor.subrace}",		
			f"{lusor.subrace}",	
			f"{lusor.subrace}",	
			f"{lusor.subrace}",
			]
	except:
		try:
			descriptor += [
				f"{lusor.species}",	
				f"{lusor.species}",	
				f"{lusor.species}",	
				f"{lusor.species}",	
				f"{lusor.species}",	
				f"{lusor.species}",	
				f"{lusor.species}",	
				f"{lusor.species}",	
				f"{lusor.species}",	
				f"{lusor.species}",
				f"{lusor.char_class}",		
				f"{lusor.char_class}",		
				f"{lusor.char_class}",		
				f"{lusor.char_class}",		
				f"{lusor.char_class}",		
				f"{lusor.char_class}",		
				f"{lusor.char_class}",		
				f"{lusor.char_class}",		
				f"{lusor.char_class}",		
				f"{lusor.char_class}",
				f"{lusor.subclass}",		
				f"{lusor.subclass}",		
				f"{lusor.subclass}",		
				f"{lusor.subclass}",		
				f"{lusor.subclass}",		
				f"{lusor.subclass}",		
				f"{lusor.subclass}",		
				f"{lusor.subclass}",		
				f"{lusor.subclass}",		
				f"{lusor.subclass}",	
				f"{lusor.subclass}",	
				f"{lusor.subclass}",
				f"{lusor.background}",		
				f"{lusor.background}",		
				f"{lusor.background}",		
				f"{lusor.background}",		
				f"{lusor.background}",		
				f"{lusor.background}",		
				f"{lusor.background}",		
				f"{lusor.background}",		
				f"{lusor.background}",		
				f"{lusor.background}",	
				f"{lusor.background}",	
				f"{lusor.background}",
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
			"Adventurer",		
			"Arcanist",			
			"Ash",				
			"Alpha",			
			"Abysswalker",		
			"Ambassador",									
			"Angel",			
			"Archfey",			
			"Archmage",			
			"Aristocrat",			
			"Avatar",			
			"Artist",			
			"Artisan",			
			"Armor",			
			"Anarch",			
			"Ascendant",			
			"Acolyte",			
			"Archer",			
			"Arbiter",			
			"Apprentice",			
			"Arsonist",			
			"Assassin",			
			"Arbiter",			
			"Archer",			
			"Assassin",			
			"Abomination",		
			"Anarchist",		
			"Arrow",				
			"Apostle",			
			"Apprentice",			
			"Avatar",			
			"Abomination",			
			"Acolyte",			
			"Alchemist",			
			"Apprentice",			
			"Arrow",			
			"Archer",			
			"Archfey",			
			"Archmage",			
			"Armour",			
			"Ash",			
			"Assassin",			
			"Anarchist",						
			"Abbess",			
			"Abbot",			
			"Abyss",			
			"Abysswalker",		
			"Acolyte",			
			"Admiral",						
			"Adventurer",			
			"Adversary",			
			"Agent",						
			"Alpha",			
			"Ambassador",						
			"Amulet",			
			"Anarchist",			
			"Angel",								
			"Apparition",						
			"Apprentice",			
			"Apprentice",			
			"Apprentice",		
			"Arcanist",			
			"Archbishop",		
			"Archduke",			
			"Archer",			
			"Archivist",			
			"Argonaut",			
			"Armour",			
			"Arrow",			
			"Artificer",			
			"Artisan",			
			"Ascendant",			
			"Ash",			
			"Assassin",			
			"Astral",			
			"Astrologer",			
			"Astronomer",			
			"Atlas",			
			"Augur",			
			"Auralist",			
			"Auramancer",			
			"Avatar",			
			"Avenger",
			]
		# B
		rank += [
			"Bane",			
			"Bane",			
			"Bane",			
			"Bane",		
			"Bane",		
			"Bane",		
			"Bane",		
			"Bane",			
			"Born",			
			"Bringer",		
			"Brutal",		
			"Bard",			
			"Buccaneer",		
			"Bound",			
			"Blaze",			
			"Banner",						
			"Bowmaster",			
			"Behemoth",			
			"Bound",			
			"Bruiser",			
			"Born",			
			"Bull",			
			"Blade",			
			"Behemoth",			
			"Benefactor",			
			"Blade",			
			"Bringer",				
			"Bard",			
			"Baron",		
			"Basilisk",			
			"Benefactor",			
			"Berserker",	
			"Bear",			
			"Beholder",		
			"Blade",		
			"Bow",				
			"Bringer",									
			"Burglar",			
			"Bull",									
			"Bearer",			
			"Band",			
			"Bane",			
			"Banner",	
			"Banner",			
			"Banshee",						
			"Barbarian",					
			"Barrow",		
			"Basilisk",		
			"Battlefury",	
			"Beacon",			
			"Bear",			
			"Bearer",		
			"Beastmaster",	
			"Beastrider",							
			"Bender",			
			"Benefactor",			
			"Berserker",			
			"Bibliomancer",			
			"Breath",			
			"Binder",						
			"Blacksmith",			
			"Blade",			
			"Blade",			
			"Bearer",			
			"Blade",		
			"Singer",			
			"Blaze",		
			"Blaze",		
			"Blessing",		
			"Blight",		
			"Blizzard",		
			"Blood",					
			"Bone",					
			"Bounty Hunter",	
			"Bounty",			
			"Bow",			
			"Brand",			
			"Bravo",			
			"Breaker",			
			"Breath",						
			"Briar",			
			"Brigadier",			
			"Bringer",			
			"Buccaneer",			
			"Bull",			
			"Burglar",			
			"Butcher",				
			"Banshee",		
			"Blessed",
			]
		# C
		rank += [
			"Custodian",		
			"Crow",				
			"Conquistador",		
			"Colonel",			
			"Commander",		
			"Chronist",			
			"Captain",			
			"Caller",			
			"Composer",			
			"Crafter",			
			"Chief",			
			"Conjurer",			
			"Count",			
			"Collector",						
			"Commander",			
			"Catcher",			
			"Curse",			
			"Caller",			
			"Cyclops",			
			"Commander",			
			"Cedar",			
			"Catapulter",			
			"Crafter",			
			"Chief",			
			"Collector",		
			"Collector",		
			"Crystal",			
			"Champion",						
			"Captain",						
			"Champion",			
			"Charlatan",			
			"Chimera",			
			"Collector",			
			"Colossus",			
			"Commander",			
			"Chosen",			
			"Cadet",			
			"Caliph",			
			"Caller",						
			"Cannibal",			
			"Canon",			
			"Cantor",			
			"Captain",			
			"Cardinal",			
			"Cartographer",						
			"Cauldron",			
			"Cavalier",			
			"Centurion",		
			"Champion",			
			"Chancellor",						
			"Chanter",			
			"Chaplain",			
			"Charlatan",			
			"Chaser",									
			"Chief",			
			"Chieftain",			
			"Chimera",			
			"Chosen",						
			"Claw",			
			"Cleric",			
			"Climber",			
			"Cloak",			
			"Codex",			
			"Collector",		
			"Colossus",			
			"Colonel",			
			"Colossus",			
			"Commander",			
			"Commodore",			
			"Conjurer",			
			"Conqueror",			
			"Conquistador",			
			"Consul",			
			"Corsair",			
			"Cossack",						
			"Councillor",			
			"Counselor",			
			"Count",			
			"Courage",									
			"Craft",			
			"Crasher",			
			"Creation",					
			"Crown",			
			"Crow",				
			"Cruor",			
			"Crusader",			
			"Curator",			
			"Curse",			
			"Cursed",			
			"Czar",			
			"Caller",			
			"Commander",
			]
		# D
		rank += [
			"Disciple",			
			"Drake",			
			"Duelist",			"Dreamer",		
			"Detective",		
			"Dreamweaver",		
			"Dancer",							"Devil",			
			"Death",			"Diviner",			
			"Dancer",			
			"Devastator",		"Defender",			
			"Dust",			"Dweller",	
			"Demon",									
			"Dragon",						
			"Diamond",			"Dagger",			
			"Dancer",			
			"Dragon",			"Devourer",			
			"Diviner",			
			"Dancer",			"Darkness",			
			"Diamond",						
			"Death",	"Devil",					
			"Drake",			
			"Druid",	"Dream",			"Devourer",			
			"Defiler",			"Dame",	"Dancer",			"Dancer",	
			"Daredevil",			 "Dawn",	"Deacon",			"Dean",			
			"Death",			"Decay",	"Deceiver",			"Deepseer",						
			"Defender",			"Deity",			"Delegate",			
			"Delver",		"Demigod",			"Demon",		"Demonhunter",			"Demon",			"Demonologist",			"Depth",			"Depths",			"Derringer",			"Descendant",			"Desolation",			"Desperado",			"Despot",			"Detective",			"Devil",			"Devotion",			"Devourer",			"Diamond",			"Dictator",					"Diplomat",			"Disciple",		"Discoverer",							"Dominator",		"Doom",			"Dove",			"Dragon",			"Drake",			"Dread",			"Dream",			"Dryad",			"Demonologist",			"Dancer",			"Devourer",			"Drifter",			"Druid",						"Dryad",			"Duelist",			"Duke",				"Delver",			"Dungeoneer",
			]
		# E
		rank += [
			"Envoy",		"Emissary",				"Enigma",			"Entity",			"Envoy",		"Ethereal",		"Exile",	"Envoy",		"Ethereal",		"Executioner",					"Emperor",			"Evangelist",			"Eye",			"Eyes",			"Enforcer",			"Eyes",			"Executioner",			"Element",			"Eagle",			"Eater",			"Eclipse",			"Enforcer",			"Elite",			"Element",			"Enchanter",	"Executioner",				"Elder",			"Executioner",			"Entity",			"Eagle",			"Earthshaper",			"Eater",			"Echo",			"Echomancer",			"Eclipse",			"Elder",			"Eldest",			"Elector",			"Elegance",			"Element",			"Elementalist",			"Element",						"Elite",			"Envoy",			"Embrace",			"Emissary",			"Enchanter",	"Enchantment",	"Enchantress",						"Enforcer",			"Enigma",			"Envoy",			"Envy",			"Etherbound",			"Ethereal",						"Executioner",			"Exemplar",			"Exile",			"Exorcist",			"Expeditioner",			"Explorer",			"Eye",			"Eyes",
			]
		# F
		rank += [
			"Firestarter",		
			"Falconer",			
			"Fanatic",		
			"Freedomfighter",		
			"Frontier",		
			"Farwalker",		
			"Fallen",		
			"Fel",		
			"Fiend",		
			"Forsaken",		
			"Foreseer",		
			"Forged",		
			"Fern",		
			"Feather",		
			"Frost",		
			"Fire",		
			"Flame",								
			"Farrier",		
			"Fury",		
			"Fisher",		
			"Fire",			
			"Forge",			
			"Fighter",			
			"Fairy",			
			"Feather",			
			"Fire",				
			"Fool",				
			"Fury",				
			"Fist",			
			"Fool",				
			"Fire",						
			"Fanatic",			
			"Fire",			
			"Fury",						
			"Flame",			
			"Fighter",			
			"Forged",			
			"Force",			
			"Fighter",			
			"Frost",			
			"Flamebearer",			
			"Falcon",			
			"Falconer",			
			"Fall",			
			"Fallen",			
			"Fanatic",			
			"Fang",						
			"Farwalker",		
			"Fatesealer",			
			"Faun",				"Fawn",			
			"Fear",			
			"Feather",			
			"Feathered",			"Fel",						
			"Fern",			
			"Fiend",			"Finder",			
			"Fire",			
			"Fisher",			
			"Flame",			
			"Flight",									
			"Forerunner",			
			"Foreseer",			
			"Forge",			
			"Forged",			
			"Forger",			
			"Forsaken",		
			"Fox",			
			"Fragment",			
			"Freedomfighter",			
			"Frontier",			
			"Frost",			
			"Fury",
			]
		# G
		rank += [
			"Geist",			
			"Giant",			
			"Giant",		
			"Ghost",		
			"Gambler",		
			"Governor",		
			"Gazelle",			
			"Gale",			
			"Gargoyle",			
			"Gauntlet",			
			"Gambler",			
			"Genius",			
			"Gladiator",			
			"Goliath",			
			"Governor",			
			"Guide",			
			"Guardian",			
			"Gladiator",			
			"Gargoyle",			
			"Genius",			
			"Giant",			
			"Grandmaster",			
			"Ghost",			
			"Goat",			
			"Guard",			
			"Guide",			
			"Gorgon",			
			"Gale",			
			"Gambit",		
			"Gargoyle",		
			"Gaze",			
			"Gazelle",			
			"Gazer",		
			"Gem",			
			"General",			"Genius",			
			"Geomancer",			
			"Ghast",			
			"Ghost",			
			"Giant",			
			"Gladiator",			
			"Glow",			
			"Goat",			"Gold",			"Governor",			"Grace",			
			"Grandmaster",			"Grave",			"Gravewalker",			
			"Guard",			"Guide",			"Gull",			
			"Gunslinger",	"Genius",		"Giant",
			 ]
		# H
		rank += [
				"Hyena",	
				"Hunter",		"Horror",		"Heart",		"Hero",			
				"Harvester",		"Hydra",		"Hand",			"Hag",			
				"Hawk",			"Heir",			"Hermit",		"Hive",			
				"Hound",			"Hunger",	"Hood",			"Heart",	
				"Hangman",	"Harbinger",	"Harpy",			"Hauler",	"Haunt",		
				"Hawk",			"Head",			"Hole",	"Heart",		"Heir",	
				"Herald",		"Herder",			"Heretic",					
				"Heron",	"Hex",			"Highlander",	"Highness",		
				"Historian",	"Hollow",		"Honor",	"Hoof",			
				"Hope",	
				"Horizon",		"Horn",		"Howl",	"Howler",		
				"Hussar",			"Hydra",	
			]
		# I
		rank += [
			"Inventor",				
			"Infiltrator",	
			"Invoker",		
			"Islander",			
			"Innovator",		
			"Islander",			
			"Invoker",			
			"Invader",			
			"Inquisitor",			
			"Impulse",			
			"Inkwork",			
			"Intellect",			
			"Illusionist",			
			"Inquisitor",			
			"Incubus",			
			"Intellect",			
			"Invoker",			
			"Illusionist",			
			"Immortal",						
			"Infernalist",			
			"Inferno",			
			"Inquisitor",			
			"Intellect",	
			"Intrigue",				
			"Invoker",			
			"Ivy",
			]
		# J
		rank += [
			"Justiciar",	"Judge",	
			"Jackal",	
			"Jackal",			"Jaguar",						
			"Jaguar",			"Janissary",						
			"Juggernaut",			"Jarl",			"Jasmine",			"Jay",			
			"Jinx",			"Journey",			"Judge",			
			"Juggernaut",			"Jumper",			"Jungle",			
			"Juniper",			"Jewel",			"Jackal",			
			"Jackal",
			]
		# K
		rank += [
			"Keeper",	
			"Kraken",	
			"Keeper",			
			"Kestrel",			
			"Khan",			
			"Killer",			
			"Kin",			
			"King",			
			"Kinsman",			
			"Kiss",			
			"Knife",			
			"Knight",			
			"Killer",			
			"Knight",			
			"Kraken",			
			"Killer",			
			"King",			
			"Keeper",			
			"Killer",			
			"King",			
			"Kiss",			
			"Knight",			
			"Knife",	
			"Keeper",
			]
		# L
		rank += [
			"Leader",	"Leviathan",		"Leader",			"Lion",				"Lorekeeper",			"Light",			"Leader",			"Leviathan",			"Leader",			"Lady",			"Lama",			"Lament",	"Lancer",			"Lark",			"Lasso",			"Laurel",			"Leader",			"Leap",			"Lecturer",			"Legacy",			"Legate",			"Legend",			"Legionnaire",			"Librarian",			"Lieutenant",			"Light",			"Lightbringer",		"Lightheart",		"Lily",			"Linguist",			"Lion",			"Lizard",			"Lord",			"Lost",			"Lotus",			"Lover",			"Loyal",			"Loyalty",			"Luminary",			"Lurk",			"Lycan",			"Lyncher",			"Lynx",			"Lord",			"Lotus",			"Leader",			"Lightning",			"Legend",			"Lover",			"Leader",			"Lion",				"Light",			"Lizard",			"Lover",			"Lasher",			"Leviathan",			"Lion",
			]
		# M
		rank += [
			"Mythmaker",    "Menace",	   "Merchant",      "Master",			"Moon",								"Moth",		"Mandril",			"Mistwalker",			"Monarch",			"Mask",			"Master",			"Manipulator",			"Machine",			"Master",			"Mystic",			"Manipulator",			"Mask",			"Master",			"Maestro",			"Mage",			"Magister",			"Magistrate",			"Magus",			"Maiden",			"Major",			"Malefic",		"Mage",				"Mantis",			"Mapper",			"Mare",         "Marigold",		    "Mariner",			"Marshal",			"Martyr",			"Mask",			"Mason",			"Master",			"Mastermind",			"Mastiff",			"Matador",			"Matriarch",			"Mausoleum",			"Mayor",			"Melody",			"Mender",			"Mercenary",			"Merchant",							"Messenger",			"Mestizo",		"Miner",		"Might",			"Mastermind",		"Mindwarden",		"Minotaur",			"Minstrel",			"Mirage",			"Mist",			"Mogul",			"Monarch",			"Mongol",			"Monster",			"Moon",			"Moonmage",			"Morgue",			"Moth",			"Mountainlord",			"Mountaineer",              "Mourner",       			    "Muse",			"Musketeer",			"Mustang",			"Myst",			"Mystagogue",	"Mystic",			"Master",			"Master",			"Master",			"Master",			"Master",			"Marauder",			"Mandate",			"Monster",			"Mind",			"Martyr",			"Mage",			"Machine",			"Mutant",			"Moon",			"Mist",			"Mirror",			"Master",			"Man",			"Machine",			"Mage",			"Magister",			"Master",			"Mastermind",			"Mastiff",			"Martyr",			"Mind",				"Mist",				"Monster",			"Moon",								"Minotaur",			"Mystic",              "Manipulator",
			]
		# N
		rank += [
			"Navigator",	
			"Nomad",			
			"Noble",		
			"Nightshade",		
			"Nexus",			
			"Nemesis",		
			"Nymph",	"Noble",	
			"Noble",					
			"Navigator",					"Necro",			
			"Necrologist",			
			"Nemesis",			
			"Nightingale",			
			"Nightmare",			
			"Nightveil",						
			"Nocturnal",			
			"Nomad",			
			"Noose",			
			"Numerologist",			
			"Nun",			
			"Nightmare",	
			"Nomad",		
			"Nightmare",	
			"Nomad",	
			"Navigator",
			]
		# O
		rank += [
			"Oracle",		"Overseer",		"Oracle",		"Oracle",		"Oracle",		"Outlaw",		"Outlaw",	"One",	"Oni",		"Oracle",	"Otter",	"Outlander",	"Outrider",		"Outlaw",	"Overlord",	"Owl",	"Owlbear",	"Oblivion",			"Occultist",			"One",			"Oni",			"Oracle",			"Orchid",			"Outlander",			"Outlaw",			"Outrider",			"Overlord",			"Overseer",			"Owl",			"Owlbear",			"Overlord",		"Outlaw",		"Oni",			"Overlord",		"Otherworld",	"Owl",		"Oni",	"One",		"Oracle",	"Outlaw",		"Owl",
			]
		# P
		rank += [
			"Paradox",		
			"Peacekeeper",		
			"Pirate",		
			"Prophet",			
			"Painter",			
			"Pyrotechnic",			
			"Prowler",			
			"Prophet",			
			"Prince",			
			"Predator",			
			"Preceptor",		
			"Preacher",			
			"Praetorian",		
			"Pirate",			
			"Pilgrim",			
			"Pastor",			
			"Performer",			
			"Punisher",			
			"Progenitor",			
			"Praetor",			
			"Paladin",			
			"Pale",				
			"Panther",			
			"Pariah",			
			"Parrot",		
			"Pathfinder",		
			"Pathologist",			
			"Patriarch",		
			"Paw",			
			"Peasant",			
			"Pegasus",			
			"Pendulum",			
			"Peregrine",			
			"Pestilence",		
			"Petal",			
			"Phantom",			
			"Pharaoh",			
			"Philosopher",			
			"Phoenix",			
			"Pikeman",			
			"Pilgrim",			
			"Pioneer",			
			"Piper",			
			"Pyromaniac",						
			"Pixie",			
			"Poem",			
			"Poet",			
			"Poltergeist",		
			"Praetor",			
			"Prefect",			
			"Potentate",			
			"Pride",			
			"Prime",			
			"Primrose",			
			"Prince",					
			"Proconsul",			
			"Prodigy",			
			"Paragon",			
			"Progenitor",			
			"Prophet",			
			"Prophetess",			
			"Prospector",			
			"Protege",			
			"Prowler",			
			"Prowlmaster",			
			"Psion",			
			"Puma",			
			"Punk",			
			"Pursuer",		
			"Plague",		
			"Power",			
			"Protector",			
			"Prophet",			
			"Paw",			
			"Power",			
			"Pathologist",		
			"Paw",			
			"Pegasus",			
			"Pixie",			
			"Pirate",			
			"Pyromaniac",			
			"Poet",			
			"Prince",			
			"Prophet",			
			"Punk",				
			"Pyrotechnic",			
			"Predator",
			]
		# Q
		rank += [
			"Queen",		
			"Quail",			
			"Quake",			
			"Queen",
			]
		# R
		rank += [
			"Reaper",		
			"Rider",		
			"Rider",			
			"Reader",		
			"Ruler",			
			"Radiance",			
			"Roar",			
			"Raider",		
			"Raider",			
			"Renegade",		
			"Rainstorm",			
			"Rainmaker",		
			"Rat",			
			"Runer",			
			"Runecarver",			
			"Ruler",		
			"Reverend",			
			"Regent",			
			"Reaper",		
			"Raven",									
			"Raptor",		
			"Rebel",			
			"Ruby",			
			"Rune",			
			"Rune",			
			"Ruby",			
			"Ranger",		
			"Rat",				
			"Raven",			"Reptile",		
			"Rider",			
			"Rose",			
			"Ruby",			"Rune",			
			"Rabbit",			
			"Radiance",		"Raider",			
			"Railroad",			
			"Rain",			"Raj",			
			"Rajput",			"Rancor",		
			"Ranger",			"Raptor",			
			"Rat",			
			"Rattlesnake",			"Raven",			
			"Reader",		"Reed",			
			"Regent",			"Relicarian",	
			"Renegade",			"Representative",	
			"Reptile",		"Requiem",			
			"Researcher",			
			"Riddle",		"Rider",			
			"Risen",			
			"Ritualist",	"Rival",			
			"Riverlord",	
			"Rivermancer",	"Roar",			
			"Robber",			"Rogue",		
			"Ronin",			"Rose",			
			"Ruby",			"Runebound",			
			"Rue",			"Ruler",		
			"Rune",			"Runebearer",		
			"Runekeeper",	"Runemaker",		
			"Runes",			"Runewriter",	
			"Runner",			"Reaper",			
			"Rex",
			]
		# S
		rank += [
			"Scout", 	"Sage", "Saint", 
			"Satyr", "Savant", 
			"Savior", "Scribe",		
			"Seer", "Sentinel",	
			"Serpent", "Shade", 
			"Shadow", "Shaman", 	
			"Sheriff", "Shield", 
			"Sire", "Skyward", 
			"Smith",		"Smuggler", 
			"Sorcerer", 
			"Specter", "Spellbinder",	"Spirit", "Spy", 
			"Squire", "Stag",	
			"Skyward",
			"Skywarden", 			
			"Stingray", 
			"Chaser", "Swallow", 
			"Swan",			"Shadow",			
			"Stalker",			"Scholar",			
			"Spirit",			"Spirit",			
			"Seeker",			"Spirit",			
			"Seeker",			"Sentinel",			
			"Seeker",			"Sheriff",								"Shadow",			"Seer",				
			"Spirit",			"Strategist",		
			"Stone",			"Sandwalker",		
			"Sandkeeper",		"Siren",			
			"Storyteller",		"Spark",			
			"Spirits", 			"Specter",				
			"Sparrow",			"Skywarden",		
			"Stag",				"Spirit",			
			"Strength",			"Sunstrider",		
			"Swordmaster",		"Saber",			
			"Sword",				"Spiritualist",			"Sparkweaver",		"Stoker",			"Seer",				
			"Seer",				"Sword",			
			"Sword",			"Sword",			
			"Swashbuckler",		"Storyteller",		
			"Statue",			"Stargazer",		
			"Spirit",			"Sphinx",				"Spellbinder",		"Speaker",			
			"Shepherd",			"Shapeshifter",		
			"Shaman",			"Serpent",			
			"Sentinel",				"Seer",					"Sectarian",			"Seafarer",			"Sculptor",			"Scorcher",			"Savage",							
			"Specter",			"Servant",			
			"Slayer",			"Saga",				"Saint",			"Salamander",		"Sandkeeper",			"Savant",			"Sparrow",			"Speaker",			"Spear",			"Shadow",			"Specialist",		"Specter",				"Spectre",				"Spellblade",			
			"Spellbreaker",		"Spellshield",		
			"Spellsword",		"Spellweaver",				"Spider",			"Web",				"Spirit",			"Spiritualist",		"Spook",			"Spy",				"Squire",				"Stag",					
			"Stampede",			"Star",				
			"Starblade",		"Starborn",			
			"Stardancer",		"Starforge",		
			"Shadow",				"Starshaper",			"Spy",			"Steward",			"Stingray",			"Stonetunnel",		"Storm",			"Stormcaller",		"Storyteller",		"Strategist",		"Strength",			"Strider",			"Successor",		"Sultan",			"Sun",					"Sunblessed",		"Sunlord",			"Sunscale",			"Sunstrider",					"Swan",				"Swarm",			"Swashbuckler",		"Sword",			"Swordmaster",			"Scale",			"Scar",			"Scholar",					"Scion",			"Scorpion",			"Scout",			"Scribe",			"Secret",					"Seeker",			"Seer",				"Sellsword",		"Senator",				"Sentinel",			"Sepulcher",		"Sergeant",			"Serpent",			"Serpentlord",		"Settler",			"Shade",			"Shadow",			"Shadowcrafter",	"Shadowmancer",			"Shadowseer",		"Shaman",						"Shaper",			"Shark",			"Shepherd",			"Sheriff",			"Shield",			"Shogun",			"Shooter",			"Shroud",			"Siege",			"Silence",			"Silver",			"Silverspeaker",	"Sire",				"Siren",			"Song",				"Skeleton",			"Skull",			"Skymaiden",		"Skyrider",			"Skyweaver",		"Slayer",				"Slinger",			"Smith",			"Smuggler",			"Snake",			"Soldier",			"Song",				"Songblade",		"Soul",				"Soulkeeper",		"Soulless",			"Sovereign",		"Seeker",			"Stalker",			
			"Sentinel",			"Seer",				"Shadow",			"Spirit",			"Shadow",			"Speaker",			"Spirit",			"Skull",			"Shadow",			"Sabertooth",			"Saurius",			"Salamander",				"Scarecrow",		"Scorpion",			"Shadow",			"Shark",			"Shaman",			"Snake",			"Skeleton",			"Skull",						"Spirit",			"Spider",			"Specter",			"Spy",				"Swashbuckler",		"Sword",			"Sword",			"Sword",			"Shaman",			"Summoner",			"Stasis",			"Sharpshooter",			"Sentry",			"Serpent",			"Sun",				"Slayer",			"Spirit",
			]
		# T
		rank += [
		    "Terror",		"Trickster",		"Tempest",			"Thunderbird",		"Tideturner",		"Tidecaller",		"Thunderbearer",		"Thunder",			"Timer",			"Thunderlord",			"Tempest",			"Templar",			"Templar",			"Tyrant",			"Traveler",			"Trailblazer",			"Tiger","Tiger",			"Terror",			"Trapper",			"Titan",			"Thief",			"Tormentor",			"Talon",			"Templar",		"Templar",			"Torturer",			"Trapper",			"Trailblazer",		"Torchbearer",			"Titan",			"Tiger",			"Traveler",			"Trickster",			"Timekeeper",			"Tyrant",			"Tactician",			"Terror",			"Tailor",			"Tale",			"Talon",			"Tamer",			"Technomancer",			"Telepath",			"Tempest",			"Templar",			"Tenacity",			"Terror",		"Taskmaster",	"Thane",			"Thaumaturge",		"Theorist",			"Thief",			"Thunder",			"Thunderbird",			"Tideturner",			"Tiger",			"Timeshifter",			"Titan",			"Tomb",			"Torchbearer",			"Torment",			"Tormented",			"Tormentor",			"Touched",			"Trader",			"Trapezist",			"Trapper",			"Traveler",			"Treasure",			"Treasures",			"Treebinder",			"Tribune",			"Tribute",			"Trick",			"Trickster",			"Troll",			 "Twilight",			"Tyrant",			"Terror",			"Tiger",			"Terror",			"Trapper",			"Trapezist",			"Troll",			"Thief",			"Trapper",			"Thunderer",			"Thrower",			"Titan",
			]
		# U
		rank += [
			"Umbra",
			]
		# V
		rank += [
			"Voyager",		"Vision",     "Verdant",       "Voice",		"Viking",		"Vision",		"Vizier",		"Vanguard",		"Vanguard",		"Voice",		"Voyager",		"Vulture",	"Vagabond",			"Void",			"Voidwalker",			"Vanquisher",	"Voice",		"Voice",			"Vagrant",			"Valkyrie",		"Valor",						"Vanguard",	"Vendetta",		"Vengeance",			"Venom",			"Vicar",		"Viceroy",	"Vigilante",	"Voice",		"Viking",		"Violet",	"Viper",		    "Virtuoso",	"Visionary",	"Vizier",	"Voice",			"Void",			"Voidseer",					"Voidwalker",	"Voyage",		"Voyager",			"Vulture",			"Vortex",		"Vigilante",			"Void",			"Voice",		"Void",						"Vulture",
			]
		# W
		rank += [
			"Warlord",		    
			"Whisperer",	
			"Wishmaker",	
			"Warden",		
			"Wishgranter",	
			"Wing",			
			"Wolf",				
			"Wishmaster",		
			"Wondrous",				
			"Wanderer",			
			"Wanderer",		
			"Witchhunter",		
			"Witchfinder",		
			"Windrider",		
			"Warden",			
			"Writer",			
			"Werewolf",			
			"Watcher",		
			"Watch",		
			"Warrior",		
			"Warlord",			
			"Wanderer",			
			"Wolf",				
			"Weaver",		
			"Walker",			
			"Wingsmith",	
			"Wyvern",		
			"Wolf",			
			"Witcher",		
			"Witch",		
			"Watcher",			
			"Warden",			        
			"Warlord",				    
			"Warrior",			
			"Watchman",		
			"Wild",				
			"Wand",				
			"Weaver",			
			"Weaver",			
			"Wielder",			
			"Wail",				
			"Wailmistress",		
			"Walker",		
			"Wanderer",		
			"War",			
			"Warcaller",				
			"Warchief",			
			"Ward",			
			"Warden",			
			"Wardmaster",	
			"Warforger",	
			"Warhawk",		
			"Warmaster",	
			"Warmonger",		
			"Warrior",				
			"Watch",			
			"Watcher",		
			"Commander",		
			"Wayfarer",			
			"Weaver",			
			"Wendigo",			
			"Werewolf",			
			"Whale",			
			"Whimsy",			
			"Whirlwind",	
			"Whisper",						
			"Wielder",			
			"Wight",		          
			"Wild",			
			"Will",			
			"Willow",			
			"Wind",			
			"Windcaller",	
			"Windrider",	
			"Wing",			
			"Wisdom",		
			"Witch",		
			"Witchdoctor",			
			"Witchhunter",		
			"Wolf",			
			"Wolfkin",			
			"Wrath",			
			"Wrath",			
			"Ward",				
			"Witchhunter",		
			"Wolf",				
			"Writer",			
			"Walker",		
			"Warlock",		
			"Warrior",			
			"Watch",			
			"Werewolf",			
			"Wizard",		
			"Writer",			
			"Willow",			
			"Wolf",						
			"Witch",        
			"Witch",		
			"Witcher",		
			"Wise",			
			"Watcher",
			]
		# Y
		rank += [
				"Yarrow",				
				"Yielder",
				]
		# Z
		rank += [
			"Zealous",	
			"Zealot",			
			"Zenithar",			
			"Zinnia",						
			"Zealot",			
			"Zephyr",
			]
	except:
		rank = ["Lord"]

	if FEMALE:
		rank += [
			"Matriarch",			
			"Mistress",
			]
	if MALE:
		rank += [
			"Gentleman",
			]
	# By Alignment
	if "Good" 	in genus:
		rank += [
			"Savior",		
			"Paragon",
			]
	if "Chaos" 	in genus:
		rank += [
			"Punk",			
			"Rebellion",
			]
	if "Lawful" in genus:
		rank +=[
		"Enforcer",
		]
	if "Evil" 	in genus:
		rank += [
			"Soulless",		
			"Monster",	
			"Nemesis",
			]

	# By Backgrounds
	if "Acolyte" 	in genus:
		rank += [
			"Disciple",		"Acolyte",		"Chaplain",		"Penitent",
			]
	if "Artisan" 	in genus:
		rank += [
			"Craftsman",	"Artificer",	"Mender",		"Maker",
			]
	if "Entertainer" in genus:
		rank += [
			"Performer",	"Dancer",		"Player",
			]
	if "Farmer" 	in genus:
		rank += [
			"Harvester",	"Ploughman",	"Hayward",
			]
	if "Guard" 		in genus:
		rank += [
			"Watchman",		"Warder",		"Gatekeeper",
			]
	if "Guide" 		in genus:
		rank += [
			"Wayfinder",	"Trailblazer",	"Scout",
			]
	if "Hermit" 	in genus:
		rank += [
			"Recluse",		"Anchorite",	"Solitary",
			]
	if "Sailor" 	in genus:
		rank += [
			"Mariner",		"Seafarer",		"Helmsman",
			]
	if "Scribe" 	in genus:
		rank += [
			"Chronicler",	"Scrivener",	"Annotator",
			]
	if "Wayfarer"	in genus:
		rank += [
			"Wanderer",		"Pilgrim",		"Farwalker",
			]
	if "Artist" 	in genus:
		rank += [
			"Reveler",	
			"Visionary",	
			"Artist",	
			"Visionary",	
			"Troubadour",		
			"Shadowcrafter",	
			"Piper",			
			"Illusionist",			
			"Trapezist",			
			"Technomancer",			
			"Alchemist",			
			"Artist",
			"Artist",
			"Artist",			
			"Flutist",			
			"Musician",
			]
		if FEMALE:
			rank += [
			"Enchantress",
			]
	if "Berserker"  in genus:
		rank += [
			"Striker",
			"Wrath",
			"Sword",	
			"Shield",		
			"Chief",		
			"Prowler",		
			"Fanatic",		
			"Warrior",
			]
	if "Barbarian"  in genus:
		rank += [
			"Fury",	
			"Wrath",
			"Reveler",	
			"Striker",	
			"Nomad",	
			"Shieldbearer",		
			"Chief",		
			"Warrior",		
			"Hunter",
			]
	if "Bard"		in genus:
		rank += [
			"Sage",	
			"Enchanter",	
			"Reveler",	
			"Artist",	
			"Visionary",	
			"Troubadour",		
			"Troubadour",		
			"Troubadour",		
			"Silverspeaker",		
			"Mesmer",		
			"Drum",		
			"Musician",		
			"Harlequin",		
			"Flutist",		
			"Archivist",		
			"Trapezist",		
			"Clown",		
			"Mime",		
			"Troubadour",		
			"Illusionist",		
			"Juggler",
			]
		if FEMALE:
			rank += [
			"Enchantress",
			]
	if "Bandit"		in genus:
		rank += [
			"Marauder",	
			"Warlord",	
			"Striker",	
			"Hunter",	
			"Phantom",	
			"Sword",	
			"Marauder",			
			"Pistol",		
			"Bandit",
			"Hunter",			
			"Archer",			
			"Warrior",			
			"Commander",
			]
	if "Charlatan"	in genus:
		rank += [
			"Sage",	
			"Enchanter",	
			"Healer",	
			"Visionary",	
			"Mesmer",	
			"Troubadour",		
			"Sirensong",		
			"Genius",		
			"Mystic",		
			"Fanatic",		
			"Archivist",		
			"Scammer",		
			"Illusionist",		
			"Alchemist",		
			"Arcanologist",
			]
	if "Cleric" 	in genus:
		rank += [
			"Watcher",		"Watcher",		"Watcher", "Watcher",		"Watcher",		
			"Hierophant",
			"Lightbearer",	
			"Exorcist",
			"Zealot",	
			"Sage",	
			"Warcaster",	
			"Witchfinder",	
			"Officiant",	
			"Bishop", 	
			"Cardinal", 	
			"Chaplain", 	
			"Cleric", 	
			"Deacon", 	
			"Devout", 
			"Disciple",	
			"Cultist",			
			"Crusader",		
			"Healer",		
			"Vicar",		
			"Witchhunter",		
			"Soulforger",	
			"Soul",		
			"Inquisitor",		
			"Thaumaturge",			
			"Friar",			
			"Exarch",			
			"Fanatic",			
			"Archbishop",			
			"Acolyte",			
			"Oracle",			
			"Saint",			
			"Oracle",			
			"Priest",			
			"Abbot",			
			"Healer",		
			"Hierophant",	
			"Guide",			
			"Crusader",			
			"Acolyte",			
			"Prelate",			
			"Bishop",			
			"Conjurer",			
			"Minister", 	
			"Mystic",		
			"Hierophant",	
			"Cleric",			
			"Abbot",
			]
		if FEMALE:
			rank += [
				"Abbess",
				]
	if "Commoner" 	in genus:
		rank += [
			"Herbalist",		
			"Hunter",	
			"Miller",	
			"Witchhunter",	
			"Speaker",		
			"Settler",	
			"Chosen",		
			"Elder",		
			"Farmer",		
			"Laborer",		
			"Citizen",		
			"Worker",		
			"Leader",		
			"Farmer",		
			"Brewer",
			]
	if "Crafter" 	in genus:
		rank += [
			"Visionary",	
			"Visionary",	
			"Chronoshifter",	
			"Alchemist", 
			"Alchemist",	
			"Spellbreaker",		
			"Vintner",		
			"Pistol",		
			"Artificer",		
			"Alchemist",		
			"Technomancer",		
			"Craftsman",		 
			"Creator",		 
			"Craftsman",		 
			"Genius",		 
			"Builder",		 
			"Maker",		 
			"Creator",		 
			"Conjurer",		 
			"Engineer",
			"Chemist",
			"Blacksmith",

			]
	if "Criminal" 	in genus:
		rank += [
			"Marauder",	
			"Jailbreaker",	
			"Striker",	
			"Hunter",	
			"Phantom",	
			"Scourger",		
			"Pistol",		
			"Thief",		
			"Assassin",		
			"Dealer",		
			"Swindler",		
			"Boss",		
			"Surgeon",
			]
	if "Cultist" 	in genus:
		rank += [
			"Sage",	
			"Leader",	
			"Reveler",	
			"Hierophant",	
			"Officiant",	
			"Cultist",		
			"Crusader",		
			"Visionary",	
			"Minister",     
			"Mystic",
			"Mesmer",	
			"Witchhunter",	
			"Unholiness",	
			"Exarch",		
			"Enchanter",		
			"Acolyte",		
			"Fanatic",		
			"Archivist",		
			"Archbishop",		
			"Arcanologist",		
			"Acolyte",		
			"Cultist", 
			"Cultist",
			"Cultist",		
			"Conjurer",		
			"Devotee",		
			"Follower",		
			"Fanatic",		
			"Fanatical",		
			"Friar",		
			"Keeper",		
			"Leader",		
			"Minister",		
			"Mystic",		
			"Oracle",		
			"Priest",		
			"Zealot",		
			"Mystic",		
			"Hierophant", 	
			"Friar",		
			"Oracle",	
			"Priest",		
			"Abbot",		
			"Healer",		
			"Guide",		
			"Crusader",		
			"Acolyte",		
			"Prelate",		
			"Bishop",		
			"Conjurer",		
			"Minister",		
			"Mystic",		
			"Hierophant",		
			"Cleric",		
			"Priest",		
			"Priest",		
			"Priest",		
			"Priest",		
			"High Priest",		
			"Archpriest",		
			"Abbot",

			]
		if FEMALE:
			rank += [
			"Abbess",			
			"Priestess",			
			"Priestess",			
			"Priestess",			
			"Priestess",			
			"Priestess",			
			"Priestess",			
			"High Priestess",			
			"Archpriestess",
			]
	if "Druid" 		in genus:
		rank += [
			"Herbalist",	
			"Lavamancer",	
			"Healer",	
			"Alchemist", 
			"Alchemist",	
			"Windcaller",	
			"Elder",		
			"Elementalist",			
			"Dawnbringer",			
			"Druid",			
			"Shaman",			
			"Biomancer",			
			"Stormcaller",			
			"Archdruid",			
			"Warden",			
			"Master",			
			"Mystic",			
			"Botanist",
			]
	if "Explorer" 	in genus:
		rank += [
			"Sailor", 	
			"Zoologist",	
			"Marauder",		
			"Tracker",	
			"Anthropologist",	
			"Hunter",	
			"Visionary",	
			"Tracker",	
			"Chronoshifter",	
			"Sword",	
			"Witchhunter",	
			"Nomad",	
			"Navigator",		
			"Herald",		
			"Mountaineer",		
			"Messenger",		
			"Scout",			
			"Archer",	
			"Leader",	
			"Ranger",			
			"Explorer",			
			"Wanderer",			
			"Adventurer",		
			"Pathfinder",			
			"Scout",	
			"Guide",			
			"Scout",
			]
	if "Expert" 	in genus:
		rank += [
			"Zoologist",	
			"Scientist",		
			"Healer",		
			"Visionary",	
			"Guru",				
			"Chronoshifter",	
			"Alchemist", 		
			"Alchemist",	
			"Professor",	
			"Visionary",		
			"Genius",		
			"Mind",			
			"Minister",			
			"Technomancer",			
			"Astrologer",			
			"Astronomer",			
			"Artificer",		
			"Archivist",		
			"Anthropologist",		
			"Arcanologist",		
			"Alchemist",		
			"Arcanologist",		
			"Apothecary",
			"Apothecary",		
			"Alchemist",	
			"Alchemist",	
			"Alchemist",		
			"Bombardier",		
			"Bomber",		
			"Collector",	
			"Consultant",		
			"Chemist",		
			"Etherscribe",	
			"Grandmaster",		
			"Alchemist",		
			"Genius",		
			"Geneticist",		
			"Engineer",		
			"Master",		
			"Pathologist",					
			"Surgeon",
			]
	if "Fighter"	in genus:
		rank += [
			"Warlord",	
			"Striker",	
			"Hunter",	
			"Blade", 
			"Sword",	
			"Witchhunter",	
			"Vigilante",		
			"Commander",			
			"Warlord",
			"Warrior",			
			"Commander",
			"Warlord",			
			"Samurai",
			"Samurai",			
			"Archer",			
			"Warrior",
			]
	if "Guardian" 	in genus:
		rank += [
			"Protector",	
			"Protector",	
			"Protector",	
			"Protector",	
			"Guardian",			
			"Crusader",			
			"Guardian",		
			"Guardian",		
			"Guardian",		
			"Guardian",		
			"Hunter",		
			"Keeper",		
			"Steward",			
			"Protector",		
			"Protector",	
			"Guardian",		
			"Sword",		
			"Vigilante",	
			"Sandkeeper",	
			"Sentinel",			
			"Sentinel",			
			"Commander",		
			"Overseer",			
			"Steward",		
			"Marshal",			
			"Guardian",			
			"Keeper",		
			"Guardian",		
			"Enforcer",		
			"Enforcer",		
			"Enforcer",		
			"Archer",		
			"Samurai",			
			"Samurai",			
			"Guard",		
			"Guardian",		
			"Keeper",	
			"Sentinel",		
			"Vigilant",		
			"Knight",		
			"Guard",		
			"Guard",		
			"Guard",			
			"Guard",			
			"Sentinel",			
			"Sentinel",		
			"Sentinel",		
			"Sentinel",		
			"Sentinel",		
			"Sentinel",		
			"Keeper", 		
			"Keeper",		
			"Custodian",	
			"Custodian",		
			"Custodian",		
			"Custodian",		
			"Custodian",		
			"Custodian",	
			"Guardian",		
			"Guardian",		
			"Protector",		
			"Guardian",			
			"Guard",			
			"Defender",		
			"Guardian",		
			"Guardian",		
			"Guardian",		
			"Guardian",		
			"Guardian",		
			"Guardian",		
			"Defender",		
			"Protector",		
			"Protector",		
			"Protector",		
			"Protector",	
			"Warden",		
			"Watcher",		
			"Watcher",		
			"Guardian",		
			"Guardian",		
			"Guard",		
			"Defender",		
			"Protector",		
			"Protector",		
			"Protector",		
			"Scarecrow",	
			"Protector",	
			"Protector",	
			"Sentinel",		
			"Keeper",		
			"Shield",			
			"Watcher",			
			"Sharpshooter",		
			"Watchdog",
			]
	if "Hero"		in genus:
		rank += [
			"Crusader",	
			"Troubadour",		
			"Guardian",		
			"Sword",	
			"Vigilante",	
			"Samurai",			
			"Leader",			
			"Warrior",			
			"Champion",			
			"Enforcer",			
			"Archer",			
			"Hero",			
			"Conqueror",			
			"Hero",       
			"Savior",
			"Warrior",
			"Defender",
			"Knight",			
			"Protector",			
			"Samurai",
			"Samurai",
			]
	if "Hunter" 	in genus:
		rank += [
		"Striker",	
		"Tracker",		
		"Cryptozoologist",	
		"Hunter",	
		"Hunter",	
		"Hunter",	
		"Hunter",	
		"Hunter",	
		"Hunter",	
		"Hunter",	
		"Hunter",	
		"Hunter",	
		"Hunter",	
		"Tracker",	
		"Witchhunter",	
		"Viper",		
		"Archer",		
		"Hunter",			
		"Hunter",			
		"Scout",			
		"Hunter",
		"Hunter",
		"Hunter",
		"Hunter",
		"Hunter",
		"Hunter",			
		"Hunter",
		"Hunter",
		"Hunter",
		"Hunter",
		"Hunter",
		"Hunter",			
		"Hound",			
		"Tracker",			
		"Hunter",			
		"Archer",	
		"Zoologist",		
		"Trapper",	
		"Huntmaster",		
		"Stalker",			
		"Ranger",
			]
	if "Healer"		in genus:
		rank += [
			"Herbalist",	
			"Sage",		
			"Cultist",			
			"Healer",	
			"Vicar",	
			"Alchemist", 
			"Alchemist",	
			"Shaman",	
			"Heart",		
			"Mystic",		
			"Blossom",		
			"Alchemist",
			"Healer",
			"Physician",
			"Doctor",
			"Herbalist",
			"Medic",
			"Surgeon",
			]
	if "Knight" 	in genus:
		rank = [
			"Conqueror",	
			"Crusader",	
			"Sword",	
			"Sable",	
			"Samurai",		
			"Enforcer",	
			"Squire",	
			"Squire",	
			"Warrior",	
			"Champion",		
			"Knight",	
			"Knight",	
			"Knight",	
			"Knight",	
			"Knight",
			"Knight",
			"Knight",			
			"Samurai",
			"Samurai",			
			"Champion",			
			"Defender",			
			"Warrior",			
			"Cavalier",			
			"Standard",			
			"Standard",			
			"Standard Bearer",			
			"Standard Bearer",
			]
	if "Mage"		in genus:
		rank += [
			"Herbalist",		
			"Sage",	
			"Warcaster",	
			"Lavamancer",	
			"Enchanter",		
			"Mesmer",	
			"Chronoshifter",	
			"Etherscribe",	
			"Spellweaver",	
			"Alchemist", 
			"Alchemist",	
			"Elder",	
			"Spellbinder",		
			"Telepath",		
			"Mystic",		
			"Archivist",		
			"Mage",		
			"Arcanologist",		
			"Technomancer",		
			"Magus",		
			"Forcemage",		
			"Battlemage",
			]
		if FEMALE:
			rank += [
			"Enchantress",
			]
	if "Monk" 		in genus:
		rank += [
			"Abbot",		
			"Ninja",	
			"Sage",	
			"Monk",				
			"Striker",		
			"Cultist", 		
			"Crusader",	
			"Shaolin",	
			"Shaolin",	
			"Vicar",	
			"Visionary",	
			"Windcaller",	
			"Ninja",	
			"Elder",		
			"Monk",		
			"Warrior",		
			"Exarch",			
			"Friar",			
			"Fanatic",			
			"Archivist",			
			"Acolyte",			
			"Monk",
			"Monk",
			"Monk",		
			"Monk",
			"Monk",
			"Monk",			
			"Monk",			
			"Mystic",			
			"Blossom",			
			"Friar",			
			"Monk",			
			"Master",			
			"Guide",			
			"Sage",			
			"Practitioner", 	
			"Philosopher", 	
			]
		if FEMALE:
			rank += [
			"Abbess",
			]
	if "Merchant" 	in genus:
		rank += [
			"Alchemist", 
			"Alchemist",	
			"Nomad",	
			"Navigator",	
			"Librarian",		
			"Alchemist",			 
			"Merchant",			 
			"Archivist",			 
			"Trader",			 
			"Negotiator",			 
			"Dealer",			 
			"Merchant",
			]
	if "Mentor"		in genus:
		rank += [
			"Sage",
			"Leader",	
			"Maestro",		
			"Archivist",		
			"Commander",
			"Mentor",
			]
	if "Noble" 		in genus:
		rank += [
			"Leader",	
			"Archon",	
			"Governor",		
			"Monarch",		
			"Sovereign",	
			"Monarch",		
			"Duke",		
			"Exarch",			
			"Ruler",			
			"Sovereign",		
			"Monarch",							
			"Major",		
			"Senator",		
			"Archduke",		
			"Archon",		
			"Chieftain",	
			"Chieftain",	
			"Chief",	
			"Chief",	
			"Consul",	
			"Cesar",	
			"Daimyo",	
			"Dictator",			
			"Diplomat",			
			"Earl",			
			"Emperor",			
			"Highness",			
			"Khan",			
			"Leader",	
			"Leader",	
			"Leader",		
			"Monarch",	
			"Monarch",		
			"Marquis",		
			"Primus",		
			"Princeps",		
			"Regent",	
			"Sultan", 			
			"Sultan",	
			"Sovereign",		
			"Sovereign",	
			"Sovereign",	
			"Sovereign",	
			"Sovereign",	
			"Sultan",		
			"Noble",		
			"Noble",		
			"Noble",		
			"Noble",
			]
		if "Fiend" in genus:
			rank += [
				"Archfiend",
				]
		if "Orc" in genus:
			rank += [
				"Khan",	
				"Khan",	
				"Khan",	
				"Khan",	
				"Khan",	
				"Khan",	
				"Khan",	
				"Khan",	
				"Khan",
				]
		if MALE:
			rank += [
				"Baron",	
				"Lord", 
				"Baron",	
				"Baron", 
				"Lord",	
				"Overlord",	
				"Master",	
				"Emperor",	
				"Prince",	
				"King",	
				"King",	
				"Baron",	
				"Baron",	
				"Baron",	
				"Count",	
				"Duke",		
				"Emir",	
				"Emperor",	
				"Emperor",	
				"Lord",	
				"Lord", 
				"Lord",
				"Lord",
				"Lord",				
				"King",
				"King",
				"King",
				"King",
				"King",				
				"Highlord",				
				"Prince",				
				"Viscount",				
				"Warlord",	
				]
		elif FEMALE:
			rank += [
			"Baroness",	"Lady", "Baroness",	"Queen",	"Princess","Princess","Princess",	"Baroness", "Queen",	"Lady",	"Overlady",	"Queen",	"Archduchess",			"Baroness",			"Duchess",			"Empress","Empress",			"Highlady",			"Lady","Lady","Lady",			"Princess",			"Queen","Queen","Queen","Queen","Queen",			"Viscountess",			"Warlady",
			]
		else:
			rank += [
			"Ruler",	"Potentate",	"Liege", "Baronate"
			]
	if "Ninja"		in genus:
		rank += [
			"Striker",	
			"Phantom",	
			"Ninja",	
			"Ninja",	
			"Monk",		
			"Warrior",		
			"Archer",		
			"Ninja", 
			"Hokage",		
			"Shadow",
			]
	if "Priest" 	in genus:
		rank += [
			"Necromancer",	
			"Sage",		
			"Witchfinder",	
			"Hierophant",	
			"Officiant",	
			"Cultist",			
			"Healer",	
			"Vicar",	
			"Pope",		
			"Exarch",		
			"Acolyte",		
			"Fanatic",		
			"Archivist",			
			"Friar",			
			"Bishop",			
			"Deacon",			
			"Chaplain",			
			"Minister",			
			"Mystic",			
			"Hierophant",			
			"Pilgrim",			
			"Abbot",
			]
		if FEMALE:
			rank += [
				"Nun",			"Abbess",			"Archduchess",			"Priestess",				"Priestess",				"Priestess",
				]
	if "Paladin"	in genus:
		rank += [
			"Crusader",	
			"Healer",	
			"Exarch",			
			"Sword",	
			"Witchhunter",	
			"Noble",		
			"Exarch",		
			"Warrior",		
			"Acolyte",		
			"Champion",		
			"Knight",		
			"Enforcer",			
			"Paladin",			
			"Warlord",			
			"Samurai",
			"Samurai",
			]
		if "Evil" in genus:
			rank += [
			"Warlord",
			]
	if "Pirate" 	in genus:
		rank += [
				"Sailor", 
				"Marauder",	
				"Striker",	
				"Hunter",	
				"Sword",		
				"Navigator",		
				"Commander",			
				"Pirate",		
				"Captain",	
				"Buccaneer",			 
				"Pistol",		
				"Raider",	
				"Corsair",		
				"Corsair",			 
				"Marauder",	
				"Sea Dog",
				"Pirate",
			]
	if "Rogue"		in genus:
		rank += [
			"Herbalist",	
			"Marauder",	
			"Striker",	
			"Phantom",	
			"Tracker",	
			"Ninja",		
			"Agent",		
			"Operative",		
			"Archer",		
			"Rogue",		
			"Poisoner",		
			"Thief",		
			"Illusionist",		
			"Investigator",
			"Rogue",
			]
	if "Ranger" 	in genus:
		rank += [
			"Pathfinder",	"Pathfinder",	"Pathfinder",
			"Stalker",		"Stalker",		
			"Hunter",		"Hunter",		
			"Hunter",		"Hunter",		
			"Herbalist",	
			"Zoologist",	
			"Ranger",	
			"Marauder",	
			"Tracker",	
			"Slayer",	
			"Vampire Slayer",	
			"Monster Slayer",	
			"Striker",	
			"Cryptozoologist",	
			"Rider",	
			"Hunter",	
			"Hunter",	
			"Hunter",	
			"Ranger",	
			"Ranger",	
			"Tracker",		
			"Nomad",			
			"Ranger",			
			"Archer",			
			"Sharpshooter",			
			"Scout",			
			"Tracker",			
			"Expert",			
			"Outlander",			
			"Warden",			
			"Investigator",
			]
	if "Scholar"	in genus:
		rank += [
			"Herbalist",	
			"Sage",	
			"Zoologist",	
			"Visionary",	
			"Scientist",	
			"Visionary",	
			"Troubadour",		
			"Professor",	
			"Scholar",		
			"Acolyte",		
			"Auralist",		
			"Archivist", 
			"Archivist",		
			"Arcanologist",		
			"Anthropologist",		
			"Alchemist",		
			"Mystic",		
			"Technomancer",		
			"Professor",		
			"Magus",		
			"Illusionist",		
			"Researcher",		
			"Arcanologist",		
			"Alchemist",		
			"Professor",		
			"Arcanist",		
			"Historian",		
			"Philosopher",		
			"Sage",		
			"Hierophant",
			]
	if "Shaman"		in genus:
		rank += [
			"Herbalist",	
			"Necromancer",	
			"Sage",		
			"Visionary",	
			"Healer",	
			"Doctor",	
			"Spellweaver",	
			"Shaman",		
			"Mystic",		
			"Druid",    
			"Oracle",		
			"Leader",
			"Healer",		
			"Guide",
			"Sage",		
			"Keeper",		
			"Shaman",		
			"Shaman",		
			"Hierophant",		
			"Blossom",
			]
	if "Soldier" 	in genus:
		rank += [
		"Conqueror",	
		"Warlord",	
		"Striker",	
		"Crusader",	
		"Hunter",	
		"Sword",	
		"Sergeant",		
		"Commander",		
		"Warrior",		
		"Archer",		
		"Enforcer",			
		"Captain",			
		"General",			
		"Leader",			
		"Warlord",			
		"Commander",			
		"Gladiator",			
		"Warrior",			
		"Samurai",
		"Samurai",		
		"Standard Bearer",
			]
	if "Sorcerer" 	in genus:
		rank += [
			"Lavamancer",	
			"Enchanter",		
			"Sorcerer",	
			"Visionary",	
			"Mesmer",	
			"Chronoshifter",	
			"Weaver",	
			"Sorcerer",	
			"Windcaller",	
			"Sorcerer",			
			"Sage",			
			"Mystic",			
			"Elementalist",			
			"Sorcerer",			
			"Magus",			
			"Illusionist",
			]
		if FEMALE:
			rank += [
				"Enchantress",			"Enchantress",			"Enchantress",			"Enchantress",
				]
	if "Spy" 		in genus:
		rank += [
			"Striker",	
			"Hunter",	
			"Tracker",	
			"Witchhunter",	
			"Ninja",		
			"Agent",		
			"Operative",		
			"Spy",
			"Operative",
			]
	if "Trickster"	in genus:
		rank += [
			"Enchanter",	
			"Reveler",	
			"Scientist",	
			"Mesmer",	
			"Troubadour",			
			"Chronoshifter",	
			"Shadowspinner",		
			"Arcanologist",		
			"Minstrel",		
			"Mist",		
			"Juggler",
			]
	if "Traveler" 	in genus:
		rank += [
				"Sailor", 	
				"Zoologist",	
				"Marauder",	
				"Tracker",		
				"Drifter",		
				"Cryptozoologist",	
				"Crusader",	
				"Scientist",	
				"Hunter",		
				"Visionary",	
				"Tracker",	
				"Troubadour",	
				"Walker",	
				"Wayfarer",		
				"Witchhunter",	
				"Nomad",		
				"Navigator",	
				"Seeker",				
				"Messenger",	
				"Anthropologist",			
				"Trapezist",		
				'Traveler',			
				"Traveler",
				]
	if "Warrior"	in genus:
		rank += [
			"Conqueror",	
			"Warlord",	
			"Striker",	
			"Sword",	
			"Sergeant",	
			"Sellsword",	
			"Slinger",		
			"General",		
			"Commander",		
			"Warrior",		
			"Pikemen",		
			"Champion",		
			"Warrior",		
			"General",		
			"Archer",		
			"Samurai",
			"Samurai",
			]
	if "Warlock"	in genus:
		rank += [
			"Necromancer",		
			"Warcaster",	
			"Occultist",	
			"Visionary",	
			"Cultist",			
			"Mesmer",	
			"Weaver",	
			"Alchemist", 
			"Alchemist",		
			"Spellsword",	
			"Spectre",		
			"Infernalist",		
			"Occultist",		
			"Fanatic",		
			"Archivist",		
			"Taromancer",		
			"Reader",		
			"Arcanologist",		
			"Arcanologist",			
			"Sage",			
			"Alchemist",			
			"Mystic",			
			"Hex",		
			"Magus",
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
			"Teller",		"Teller",		"Teller",	"Teller",		"Teller",		
			"Magister",
			"Loremaster",	
			"Necromancer",		
			"Sage",	
			"Warcaster",		
			"Lavamancer",		
			"Enchanter",		
			"Visionary",			
			"Mesmer",				
			"Auramancer",			
			"Archivist",			
			"Arcanologist",			
			"Alchemist",			
			"Astromancer",			
			"Aetheromancer",		
			"Arcanomancer",			
			"Cryptomancer",			
			"Cardiomancer",			
			"Cardmancer",			
			"Cosmomancer",			
			"Chronoshifter",		
			"Eclipsomancer",		
			"Etherscribe",			
			"Weaver",			
			"Alchemist", 		
			"Alchemist",		
			"Writer",			
			"Seer",					
			"Elementalist",			
			"Magician",				
			"Wizard",				
			"Wizard",				
			"Magus",			
			"Chronomancer",			
			"Draconomancer",		
			"Mystic",				
			"Crystalmancer",		
			"Shadowmancer",			
			"Stellomancer",			
			"Heliomancer",			
			"Selenomancer",			
			"Aquamancer",			
			"Necromancer",			
			"Pyromancer",			
			"Aeromancer",		
			"Geomancer",		
			"Gaiamancer",		
			"Uranomancer",		
			"Electromancer",		
			"Psychomancer",			
			"Lithomancer",			
			"Sage",					
			"Thermomancer",			
			"Technomancer",			
			"Lunamancer",			
			"Venomancer",			
			"Cryomancer",			
			"Oniromancer",			
			"Morpheomancer",		
			"Venusmancer",			
			"Logomancer",			
			"Numeromancer",			
			"Osteomancer",			
			"Spectromancer",		
			"Noctimancer",		
			"Celestimancer",	
			"Galaxiomancer",	
			"Abyssomancer",		
			"Infernomancer",	
			"Tempestomancer",		
			"Gravitomancer",		
			"Harmonimancer",		
			"Illusiomancer",		
			"Juramancer",			
			"Kosmomancer",			
			"Lumimancer",			
			"Lumomancer",			
			"Luximancer",			
			"Luxomancer",			
			"Nihilomancer",			
			"Omnimancer",			
			"Sanguimancer",			
			"Ghoulmancer",			
			"Vampiromancer",			
			"Magus",			
			"Titanomancer",		
			"Oracle",			
			"Illusionist",
			]
	if "Witch"		in genus:
		rank += [
				"Herbalist",	
				"Necromancer",	
				"Sage",	
				"Elementalist",
				"Brewmaster",	
				"Healer",		
				"Mesmer",		
				"Stormcaller",	
				"Raincaller",	
				"Firecaller",	
				"Weaver",	
				"Alchemist",	
				"Windcaller",	
				"Shaman",	
				"Witch",
				]
		if FEMALE: rank += [
			"Harridan",
			]

	# By races (And then subraces)
	if "Aven" 		in genus:
		rank += [
				"Thunderbird",			
				"Firebird",			
				"Windbird",			
				"Seabird",			
				"Stormbird",			
				"Sandbird",			
				"Sunbird",			
				"Moonbird",			
				"Thunderlord",			
				"Aven",			
				"Celestial",			
				"Aven",		
				"Peacock",			
				"Skywing",			
				"Wing",			
				"Wing",			
				"Wing",
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
			"Crab",	
			"Aberration",	
			"Deathclaw",
			]
		if "Beholder"	in genus:
			rank +[
				"Oculus",	"Beholder",				"Eye",				"Watcher",
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
				"Devourer"
				]
		if "Parasyte" in genus:
			rank += [
				"Leech",	"Parasyte",				 "Dominator",				 "Invader",				 "Master",
				 ]
		if "Symbioid" in genus:
			rank += [
				"Communion",				"Union",
				"Symbiote",				"Symbioid",
				]
		if "Alien Spawn" in genus:
			rank += [
			"Star",			"Invader",
			"Parasite",
			"Entity",
			"Horror",
			]
		if "Chaos Warper" in genus:
			rank += [
				  "Giant",				  "Sovereign",
				  "Colossus",
				  "Dominator",				  "Titan",
				  ]
		if "Dominators" in genus:
			rank += [
			"Slaver",		 "Master",
			 "Lord",			 "Dominator",
			 "Subjugator",			 "Enforcer",
			 ]
		if "Living Spell" in genus:
				rank += [
					"Spell",					"Entity",
					"Aberration",
					"Devourer",					"Curse",
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
				"Monkey",				"Master",				"Baboon",
				]
		if "Armored Bear" 	in genus:
			rank += [
					"Bruin",					"Guardian",					"Ursus",
					"Bear"
					]
		if "Kong" 			in genus:
			rank += [
				"Kong",				"Baboon",
				"Colossus",
				"Titan",				"Ape",
				"Silverback",				"Orangutan",
				]
		if "Giant Eagle" 	in genus:
			rank += [
			  "Eagle",			  "Giant",
			  ]
		if "Tiger" 			in genus:
			rank += [
				"Sabertooth",				"Tiger",
				"Sovereign",				"Stalker",				"Predator",				"Striker"
				]
		if "Vulture" 		in genus:
			rank += [
			"Wing",			"Spirit",
			"Vulture",
			"Sky",			"Scavenger",
			"Vision",			"Predator"
			]
		if "Deer" 			in genus:
			rank += [
			"Stag",			"Deer",
			]
		if "Owl"			in genus:
			rank += [
			"Owl",			 "Seer",
			]
		if "Kaiju" 			in genus:
			rank += [
			"Kaiju",			"Behemoth",
			"Dinosaur",			"Gigantosaurus",			"Dinosaur",
			]
		if "Sun Scarab" 	in genus:
			rank += [
				"Scarab",				"Pharaoh",
				"Beetle",				"Sun"
				]
	if "Catfolk"	in genus:
		rank = [
			"Striker",	
			"Mane",			
			"Sabertooth",			
			"Leopard",			
			"Lion",
			]
	if "Celestial" 	in genus:
		rank += [
			"Angel",
			"Emissary",			
			"Kami",			
			"Guardian",			
			"Guide",
			"Herald",			
			"Light",			
			"Messenger",			
			"Oracle",			
			"Celestial",			
			"Celestian",			
			"Minister",			
			"Muse",
			]
		if "Archangel"	in genus:
			rank += [
				"Archangel",			
				"Archangel",			
				"Archangel",			
				"Archangel",			
				"Archangel",
			]
	if "Construct"	in genus:
		rank += [
				"Puppet",	
				"Crab",	
				"Droid",		
				"Scarecrow",		
				"Robot",		
				"Slave",		
				"Drone",		
				"Automaton",		
				"Engine",		
				"Clockdroid",		
				"Statue",		
				"Drone",		
				"Golem",		
				"Golem",		
				"Golem",		
				"Golem",		
				"Sentry",
				]
	if "Dwarf"		in genus:
		rank += [
			"Conquistador",	
			"Beard",
			]
	if "Dragon"		in genus:
		rank += [
			"Wyrm",	
			"Hatchling",
			]
		if "Noble" in genus:
			rank += [
			"Dragonlord",			
			"Elder",
			]
	if "Elemental"	in genus:
		rank += [
			"Elemental",			
			"Elemental",			"Genie",
			]
		if "Genasi" in genus:
			rank +=[
			"Genasi",
			]
	if "Fiend"		in genus:
		rank += [
			"Demon",	
			"Incubus",			
			"Infernal",	
			"Fiend",	
			"Hellknight",		
			"Sucubus",		
			"Sucubus",		
			"Baboon",		
			"Firefiend",
			]
	if "Fey"		in genus:
		rank += [
			"Sprite",	
			"Sprite", 
			"Duende", 
			"Duende", 
			"Duende",
			]
	if "Giant"		in genus:
		rank += [
			"Titan",	
			"Giant",		
			"Colossus",			
			"Titan",
			]
		if "Goliath"		in genus:
			rank += [
					"Golem",
					]
	if "Goblin"		in genus:
		rank += [
			"Duende",	
			"Duende",	
			"Duende",	
			"Goblin",		
			"Baboon",		
			"Gnawer",		
			"Raider",		
			"Akki",
			]
		if "Redcap" in genus:
			rank += [
				"Raider", 
				"Goatraider",			
				"Redcap",
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
			"Viashino",	"Dinosaur", "Saurius",							"Lizard",
			]
		if "Turtle"	in genus:
			rank += [
			"Turtle",	"Turtle",			"Shield",
			]
	if "Monstrosity" 	in genus:
		rank += [
			"Crab",
			]
		if "Shapeshifter" in genus:
			rank += [
				"Sasquatch",			"Mimic",			"Double",			"Monster", "Monster", "Monster",
				]
	if "Ooze" 		in genus:
		rank += [
		"Blob", "Blob",
			]
	if "Plant" 		in genus:
		rank += [
			"Oak",	"Maple",	"Flora",
			]
	if "Undead"		in genus:
		rank += [
		"Zombie",			"Zombie",		"Awakener",	
		"Skeleton",	"Requiem", "Ghost",	"Apparition",	"Wraith",			"Wraith",	"Phantom",	"Wraith",	"Mourner",		"Ghost","Ghost","Ghast","Ghost",		"Revenant","Revenant","Revenant",			"Cadaver", "Cadaver",			"Hellhound",			
		"Skeleton",			"Visit",			"Visitor",			"Soul",			"Phantom",			"Ghoul",			"Ghoulcaller",			"Carnophage",			"Cannibal",			"Hemophage",	"Mummy",	"Mummy",		"Mummy",	"Mummy",
			]
	if "Vampire" 	in genus:
		rank += [
		"Vampire",  "Reveler",	"Socialite",	"Bloodlord", "Revenant",			"Vampire",			"Vampyr",			"Vampyre",			"Strigoi",
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
		  "Thief",	"Assassin",	"Scout",	"Spy",	"Trickster",
		  ]
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
			"Herbalist",	"Nomad",			"Explorer",			"Wanderer",		"Traveler",
			]
	if "Trickster" in genus:
		rank += [
			"Scamp",			"Survivor",
			]
	if "Warrior" in genus:
		rank += [
			"Wrath",	"Fighter",		  "Warlord",		  "Warrior",		 "Champion",		 "Duelist",		 "Gladiator",
			]
	if "Warlock" in genus:
		rank += [
			"Arcanologist",		"Wizard",			"Advisor",			"Caster",			"Conjurer",			"Maker",			"Occultist",			"Oracle",			"Priest",			"Scholar",			"Warlock","Warlock","Warlock",			"Hierophant",		"Sorcerer",
			]
	if "Witch" in genus:
		rank += [
			"Sage",	"Caster",			"Crone",			"Herbalist",			"Sorceress",			"Witch","Witch",
			]
	if "Aberration" in genus:
		rank += [
			"Abomination",			"Abyss",			"Born",			"Breaker",			"Controller",			"Devourer",			"Distorter",			"Dominator",			"Dreamer",			"Eater",			"Enforcer",			"Gazer",			"Harbinger",			"Horror",			"Manipulator",	"Netherbrain",			"Nethermind",			"Oblivion",			"Overseer",			"Ravager",			"Speaker",			"Stealer",			"Void",			"Voidshaper",			"Warden",			"Warp",			"Warper",			"Whisperer",
			]
	if "Priest" in genus:
		rank += [
			"Sage",	
			"Acolyte",			
			"Cleric",			
			"High Priest",			
			"Keeper",			
			"Preacher",			
			"Priest",			
			"Priestess",			
			"Cardinal",			
			"Hierophant",
			]
	if "Plant" in genus:
		rank += [
			"Tree",		  
			"Plant",
			"Plant",	
			"Blossom",
			]
	if "Dragon" in genus:
		rank += [
			"Wrath",	
			"Breath",	
			"Calm",		  
			"Champion",		  
			"Dominator",		  
			"Drake",		  
			"Fang",		  
			"Fang",		  
			"Fire",		  
			"Firebreather",		  
			"Firebreather",		  
			"Fury",		  
			"Fury",		  
			"Hunter",		  
			"Keeper",		  
			"Lord",		  
			"Mind",		  
			"Moon",		  
			"One",		  
			"One",		  
			"Rex",		  
			"Ruler",		  
			"Scale",		  
			"Seeker",		  
			"Shadow",		  
			"Sovereign",		  
			"Sovereign",		  
			"Star",		  
			"Sun",		  
			"Terror",	
			"Wing",
			]
	if "Illithid" in genus:
		rank += [
			"Astral",		
			"Brainkeeper",		
			"Brainmaster",		
			"Cerebral",		
			"Cerebromancer",		
			"Commander",		
			"Conjurer",		
			"Controller",		
			"Cortex",		
			"Deep",		
			"Dominator",		
			"Dominator",		
			"Eater",		
			"Elder",		
			"Emissary",		
			"Encephalarch",		
			"Flayer",		
			"Flayer",		
			"Gloom",		
			"Illithid",		
			"Lurker",		
			"Master",		
			"Master",		
			"Mind",		
			"Mind",		
			"Mind",		
			"Mind",		
			"Mind",		
			"Mind",		
			"Mind",		
			"Mind",		
			"Mindking",		
			"Mindlord",		
			"Mindqueen",		
			"Mindspeaker",		
			"Neurocaptain",		
			"Oracle",		
			"Orb",		
			"Prophet",		
			"Psychic",		
			"Psychic",		
			"Psychic",		
			"Seer",		
			"Sovereign",		
			"Sovereign",		
			"Strider",		
			"Synapse",		
			"Tentacle",		
			"Thought",		
			"Thought",		
			"Tyrant",		
			"Void",		
			"Warpweaver",
			]
	if "Beholder" in genus:
		rank += [
			"Beholder",		
			"Eye",	
			"Gaze",		
			"Lord",		
			"Lord",		
			"Master",		
			"Oracle",		
			"Orb",		
			"Overseer",		
			"Pasha",		
			"Ruler",		
			"Sovereign",		
			"Sovereign",		
			"Sphere",		
			"Tyrant",		
			"Tyrant",		
			"Watcher",
			]
	if "Shapeshifters" in genus:
		rank += [
			"Formless",		  
			"Shapechanger",		  
			"Shifter",
			]
	if "Old One" in genus:
		rank += [
			"Elder Entity",	 
			"Cosmic Sage", 
			"Star Spawn", 
			"Void Seer", 
			"Ancient Horror",
			]
	if "Mindlinker" in genus:
		rank += [
			"Conductor",			
			"Connector",			
			"Linker",
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
				"Cat",				
				"Grace",				
				"Hunter",				
				"Lord",				
				"Master",				
				"Sabertooth",				
				"Sage",				
				"Seer",				
				"Paw",				
				"Fang",				
				"Mane",
				]
	if "Undead" in genus:
		rank += [
				"Necron",				
				"Reaper",				
				"Lich",
				"Lich",
				]
	if  "Mage"  in genus:
		rank += [
			"Mage",			
			"Archmage",			
			"Mage",			
			"Hierophant",
			]
	if "Bard" 	in genus:
		rank += [
			"Bard",		
			"Jester",			
			"Flutist",			
			"Fiddler",			
			"Poet",			
			"Bard",
			]
	if "Berserker" in genus:
		rank += [
			"Berserker",    
			]
	if "Druid" 	in genus:
		rank += [
			"Druid",
			]
	if "Sorcerer" in genus:
		rank += [
			"Sorcerer",	
			"Sorcerer",	
			"Sorcerer",
			"Sorcerer",
			]
	if "Archfey" in genus:
		rank += [
			"Archfey",
				]
	if "Merfolk" in genus:
		rank += [
			"Merfolk", 
			"Siren", 
			"Triton",
			]

	try:
		rank += [
			f"{lusor.archetype}",	
			f"{lusor.archetype}",	
			f"{lusor.archetype}",	
			f"{lusor.archetype}",	
			f"{lusor.archetype}",	
			f"{lusor.archetype}",	
			f"{lusor.archetype}",	
			f"{lusor.archetype}",	
			f"{lusor.archetype}",	
			f"{lusor.archetype}",
			f"{lusor.race}",		
			f"{lusor.race}",		
			f"{lusor.race}",		
			f"{lusor.race}",		
			f"{lusor.race}",		
			f"{lusor.race}",		
			f"{lusor.race}",		
			f"{lusor.race}",		
			f"{lusor.race}",		
			f"{lusor.race}",
			f"{lusor.subrace}",		
			f"{lusor.subrace}",		
			f"{lusor.subrace}",		
			f"{lusor.subrace}",		
			f"{lusor.subrace}",		
			f"{lusor.subrace}",		
			f"{lusor.subrace}",		
			f"{lusor.subrace}",		
			f"{lusor.subrace}",		
			f"{lusor.subrace}",	
			f"{lusor.subrace}",	
			f"{lusor.subrace}",
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

def Place(lusor):
	genus = Genus(lusor)
	place = []
	place += [
        "Realm",		
		"Kingdom", 
		"Empire", 
		"Sanctuary", "Tomb", 		"Dungeon",		
		"Woods", 
		"Forest", 
		"Lands", "Caves",		"Halls",		
		"Temple", 		
		"Temples",	"Ruins",		"Wilds",		
		"Abyss",		
		"Desert",		"Lake",			"Sea", 
		"Ocean",        
		"Labyrinth",		
		"Labyrinths", 	"Road", "Paths",		
		"Circle", 
		"Skies",		
		"Court",		
		"Throne", "Watch",		
		"Fortress", 
		"Marshes", "Camp",		
		"Garden",	"Gardens",		
		"Peaks", "Groves", 
		"Groove",		"Wastes"
	]	
	return random.choice(place)

def Origin(lusor):
	'''
	If you can say: The Dark Lord of X
	X goes here
	'''

	genus = Genus(lusor)
	descriptor = Descriptor(lusor)
	rank = Rank(lusor)
	for _ in range(10):
		if descriptor.lower() not in rank.lower() and rank.lower() not in descriptor.lower():
			break
		rank = Rank(lusor)

	place = Place(lusor)
	for _ in range(10):
		if place.lower() not in descriptor.lower() and descriptor.lower() not in place.lower() and \
		   place.lower() not in rank.lower() and rank.lower() not in place.lower():
			break
		place = Place(lusor)

	origin = []

	
	# of
	# from
	# {rank}
	# {descriptor}
	origin += [
		f"of the {place} Ring", 
		f"of the {descriptor} Realm", 
		f"of the {descriptor} Kingdom", 
		f"of the {descriptor} Empire", 
		f"of the {descriptor} Sanctuary", 
		f"of the {descriptor} Dungeon", 
		f"of the {descriptor} Woods", 
		f"of the {descriptor} Forest", 
		f"of the {descriptor} Tomb", 
		f"of the {descriptor} Lands", 
		f"of the {descriptor} Caves", 
		f"of the {descriptor} Halls", 
		f"of the {descriptor} Temple", 
		f"of the {descriptor} Temples", 
		f"of the {descriptor} Ruins", 
		f"of the {descriptor} Wilds", 
		f"of the {descriptor} Abyss", 
		f"of the {descriptor} Desert", 
		f"of the {descriptor} Lake", 
		f"of the {descriptor} Sea", 
		f"of the {descriptor} Ocean", 

		f"of the {descriptor} Labyrinth", 
		f"of the {descriptor} Labyrinths", 
		f"of the {descriptor} Road", 
		f"of the {descriptor} Paths", 
		f"of the {descriptor} Circle", 
		f"of the {descriptor} Skies", 
		f"of the {descriptor} Court", 

		f"of the {descriptor} Throne", 
		f"of the {descriptor} Watch", 
		f"of the {descriptor} Fortress", 
		f"of the {descriptor} Marshes", 
		f"of the {descriptor} Camp", 
		f"of the {descriptor} Garden",        
		f"of the {descriptor} Gardens", 
		f"of the {descriptor} Peaks", 
		f"of the {descriptor} Forest", 
		f"of the {descriptor} Forests", 
		f"of the {descriptor} Lands", 
		f"of the {descriptor} Caves", 
		f"of the {descriptor} Halls", 
		f"of the {descriptor} Temples", 
		f"of the {descriptor} Groves", 
		f"of the {descriptor} Grove", 
		f"of the {descriptor} Wastes",
		f"of the {descriptor} Aura",
		f"of the {descriptor} Dragon",
		f"of the {descriptor} Dungeon",
		f"of the {descriptor} Fire",
		f"of the {descriptor} Kingdom",
		f"of the {descriptor} Realm",
		f"of the {descriptor} Sanctuary",
		f"of the {descriptor} Shadows",
		"of the Pegasus",
		"with no master",
		"with no masters",
		"of Progress",
        "of the Fallen",
        "of the Shrine",
        "of the Godless Shrine",
        f"of the {descriptor} Shrine",
        "of Zenithar",
        "of Kazandu",
        f"of the {descriptor} Tomb",
        "of Time",
        "of the Fires",
        "of the Fires",
        "of Hell",
        "of the Fateweb",
        "of the Golden Sun",
        f"of the {descriptor} Sun",
        f"of the First Sun",
        f"of the Dark Sun",
        f"of the Red Sun",
        f"of the White Sun",
        f"of the Black Sun",
        f"of the Antisun",

        "of The Amulet",
        "of The Sword",
        "of The Talisman",
        "of The Goblet",
        "of the Galaxy",

        "of Baba Yaga",
        "of the Kraken",
        "of the Hydra",
        "of the Waterfall",
        f"of the {descriptor} Waterfall",
        f"of the {descriptor} Sagas",
        f"of the {descriptor} Eternals",
        "of the Eternal Sagas",
        "of the Eternals",
        "Of Athena",
        "of Delphos",
        "of the Underworld Gate",
        "of the Underworld",
        "Odyssey",
        "Of Death",
        "of El Dorado",
        "of Eldorado",
        "Of Fate",
        "Of Heaven",
        "Of Justice",
        "Of Odin",
        "Of The Abyss",
        "Of the Autumn",
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
        "Of the Kingdom",
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
        "of the Jewels","of the Ruby",
        "of Gold",
        "of Silver",
        "of Iron",
        "of Steel",
        f"of the {descriptor} Woods",
        f"of the {descriptor} Woods",
        f"of the {descriptor} Woods",
        f"of the {descriptor} Woods",
        f"of the {descriptor} Woods",
        f"of the {descriptor} Woods",
        f"of the {descriptor} Woods",
        f"of the {descriptor} Woods",
        f"of the {descriptor} Woods",
        f"of the {descriptor} Woods",
        f"of the {descriptor} Woods",
        f"of the {descriptor} Woods",
        f"of the {descriptor} Woods",
        f"of the {descriptor} Woods",
        f"of the {descriptor} Woods",
        f"of the {descriptor} Woods",
        f"of the {descriptor} Woods",
        f"of the {descriptor} Woods",
        f"of the {descriptor} Realms",
        f"of the {descriptor} Realms",
        f"of the {descriptor} Realms",
        f"of the {descriptor} Realms",
        f"of the {descriptor} Realms",
        f"of the {descriptor} Realms",
        f"of the {descriptor} Realms",
        f"of the {descriptor} Realms",
        f"of the {descriptor} Realms",
        f"of the {descriptor} Realms",
        f"of the {descriptor} Realms",
        f"of the {descriptor} Realms",
        f"of the {descriptor} Realms",
        f"of the {descriptor} Realms",
        f"of the {descriptor} Realms",
        f"of the {descriptor} Realms",
        f"of the {descriptor} Realms",
        f"of the {descriptor} Realms",
        f"of the {descriptor} Realms",
        f"of the {descriptor} Realms",
        f"of the {descriptor} Realms",
        f"of the {descriptor} Realms",
        f"of the {descriptor} Realms",
        f"of the {descriptor} Realms",
        "of Hamlet",
        "of the Swamp",
        "of the Island",
        "of the Forest",
        "of the Plain",
        "of the Mountain",
        "of the Swamps",
        "of the Islands",
        "of the Forests",
        "of the Plains",
        "of the Mountains",
        "of the Cosmos",
        "of Dread",
	f"of the {rank}'s Curse",
	f"of the {descriptor} Curse",
	f"of the Curse",
	"of the Crypt",
	f"of the {descriptor} Crypt",
	f"of the {descriptor} City",
	"of the Golden City",
	"of the Ouroboros",
	f"of the {descriptor} Master",

	f"of the {descriptor} Wars",
	f"of the {descriptor} War",
	f"of the {rank} Wars",
	f"of the {rank} War",

	"of the Wars",
	"of the War",
	"of the Damned",
	"of the Moon",
	"from the Moon",
	"of the Jungle",
	"from the Jungle",
	f"of the {descriptor} Shadows",
	"of Orisha",
	"of Osiris",
	"of Jade",
	"of Justice",
	"of Beauty",
	"of Ambition",
	"of the Parliament",
	"of Appetite",
	"of Change",
	"of Endeavor",
	"of Adventure",
	f"from the {descriptor} Island",
	f"of the {descriptor} Island",
	"from the Island",
	"of the Island",
	"of the Hive",
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
	"of Werewolves",
	"of the Valkyrie",
	"of the Universe",
	"of Trolls",
	"of the Sorcerer",
	"of the Totem",
	"of the Shepherd",
	"of the Shaman",
	"of Shamans",
	f"of the {descriptor} Shaman",
	"of the Serpent",
	f"of the {descriptor} Serpent",
	"of Serpents",
		"of the Scholar",
		"of Scholars",
		f"of the {descriptor} Scholar",
		f"of the {descriptor} River",
		"of the River",
		"of the Queen",
		f"of the {descriptor} Queen",
		"of the Prince",
		f"of the {descriptor} Prince",
		"of the Pirate",
		"of Pirates",
		f"of the {descriptor} Pirates",
		"of the Minotaur",
		"of the Oracle",
		"of Odin",
		f"of the {descriptor} Meadow",
		"of the Meadow",
		f"of the {descriptor} Mage",
		"of the Mage",
		"of Mages",
		"of the Master",
		f"of the {descriptor} Master",
		f"of the {descriptor} Lich",
		"of the Lich",
		f"of the {descriptor} Lion",
		"of the Lion",
		"from the Labyrinth",
		f"of the {descriptor} Labyrinth",
		"of the Labyrinth",
		f"of the {descriptor} Kraken",
		"of the Kraken",
		f"of the {rank} Knight",
		f"of the {descriptor} Knight",
		"of the Knight",
		f"of the {descriptor} Kingdom",
		f"of the {rank} Kingdom",
		"of the Kingdom",
		"of the King",
		f"of the {descriptor} King",
		f"of the {rank} King",
		"of the Inn",
		f"of the {rank} Inn",
		f"of the {descriptor} Inn",
		"of the Highlord",
		f"of the {descriptor} Highlord",
		"of the Harbor",
		f"of {rank} Harbor",
		f"of {descriptor} Harbor",
		"of the Glade",
		f"of the {rank} Glade",
		f"of the {descriptor} Glade",
		"of the Gulf",
		f"of the {rank} Gulf",
		f"of the {descriptor} Gulf",
		"of the Guild",
		f"of the {rank} Guild",
		f"of the {descriptor} Guild",
		"of the Guardian",
		f"of the {rank} Guardian",
		f"of the {descriptor} Guardian",
		f"of the {descriptor} Geyser",
		"of the Geyser",
		f"of the {descriptor} Field",
		"of the Field",
		"of the Eagle",
		"of the Elixir",
		f"of the {descriptor} Elixir",
		"of Death",
		f"of the {descriptor} Death",
		"of the Crown",
		"of the Condor",
		"of the Boar",
		f"of {descriptor} Battle",
		f"of {rank} Battle",
		"of Battle",
		f"of the {descriptor} Battle",
		f"of the {rank} Battle",
		"of the Battle",
		"of the Baobab",
		"of the Baron",
		"of the Amulet",
		"of the Amazon",
		"of the Arena",
		"of War",
		"of the Wizard",
		"of the Wolf",
		f"of the {descriptor} Wolf",
		f"of the {descriptor} Wizard",
		"of the Skies",
		"from Beyond the Veil",
		"from Beyond The Wall",
		"of Stonehenge",
		"of the Cemetery",
		"of the Temple",
		"of Malady",
		"of the Paladin",
		"of the Pyramid",
		f"of the {descriptor} Pyramid",
		"of the Labyrinth",
		f"of the {descriptor} Labyrinth",
		f"of the {descriptor} Laboratory",
		"of the Laboratory",
		"of the Wilderness",
		f"of the {descriptor} Hunter",
		"of the Hunter",
		"of the Kraken",
		f"of the {rank} Organization",
		f"of the {descriptor} Organization",
		f"of the {rank} Organization",
		f"of the {descriptor} Organization",
		f"of the {rank} Organization",
		f"of the {descriptor} Organization",
		f"of the {rank} Organization",
		f"of the {descriptor} Organization",
		"of the Organization",
		f"of the {rank} Guild",
		f"of the {rank} Guild",
		f"of the {rank} Guild",
		f"of the {rank} Guild",
		f"of the {rank} Guild",
		f"of the {rank} Guild",
		f"of the {rank} Guild",
		f"of the {descriptor} Guild",
		"of the Guild",
		"of the Werewolves",
		"of the Galaxy",
		"of the Sphinx",
		"of Infinity",
		"of the Grassland",
		f"of the {descriptor} Grassland",
		"of Mystery",
		"of Mischief",
		"of Secrecy",
		"of the Kingdom",
		f"of the {descriptor} Kingdom",
		f"of the {descriptor} Baron",
		"of the Baron",
		"of Condor",
		"of the Hive",
		f"of the {descriptor} Wolf",
		"of the Wolf",
		"of The Goblet",
		"of The Talisman",
		"of The Sword",
		"of The Amulet",
		f"of The {descriptor} Goblet",
		f"of The {descriptor} Talisman",
		f"of The {descriptor} Sword",
		f"of The {descriptor} Amulet",
		f"of the {descriptor} Waterfall",
		"of the Waterfall",
		"of the Order",
		f"of the {descriptor} Order",
		"of the Owl",
		"of the Garden",
		"of the Ghost",
		f"of the {descriptor} Ghost",
		f"of {descriptor} Ghosts",
		f"of Ghosts",
		f"of the {descriptor}  Garden",
		"Of Athena",
		"of Delphos",
		"of the Vampire",
		"of the Underworld Gate",
		"of the Underworld",
		"of the Odyssey",
		"of Death",
		"of El Dorado",
		"of Eldorado",
		"of Fate",
		"Of Heaven",										"Of Justice",
		"Of Odin",
		"Of The Abyss",
		"Of the Autumn",

												"Of Justice",
		"Of Odin",
		"Of The Abyss",
		"Of the Autumn",

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
		f"of the {descriptor} Tactics",
		f"of the {descriptor} City",
		"of the Golden City",
		"of the Treasure",	"of the Kraken",
		"of the Sunlord",
		"of Sundiata",
		
		"of the Sword",
		"of Baba Yaga",
		f"of the {descriptor} Kraken",
		"of the Hydra",
		"of the Aegean",
		"of the Amazon",
		"of the Amazonians",
		"of the Archipelago",
		f"of the {descriptor} Archipelago",
		"of the Asgardians",
		"of the Atlanteans",
		"of the Aztecs",	"of the Badlands",
		"of the Babylonians",	"of the Bay",
		f"of the {descriptor} Bay",
		"of the Beach",
		f"of the {descriptor} Beach",
		"of the Glade",
		f"of the {descriptor} Glade",
		"of the Gorgonians",
		"of the Grassland",
		f"of the {descriptor} Grassland",
		"of the Gulf",
		f"of the {descriptor} Gulf",
		"of the Garden",
		f"of the {descriptor} Garden",
		"of the Geyser",
		f"of the {descriptor} Geyser",
		"of the Harbor",
		f"of the {descriptor} Harbor",
		f"of {descriptor} Harbor",
		"of the Hill",
		f"of the {descriptor} Hill",
		"of the Island",
		f"of the {descriptor} Island",
		f"of {descriptor} Island",
		"of the Marsh",
		f"of the {descriptor} Marsh",
		f"of {descriptor} Marsh",
		"of the Meadow",
		f"of the {descriptor} Meadow",
		f"of {descriptor} Meadows",
		"of the Mine",
		f"of the {descriptor} Mine",
		f"of {descriptor}mine",
		"of Moss",
		"of the Mountain",
		f"of the {descriptor} Mountain",
		f"of {descriptor} Mountain",
		"of the Museum",
		f"of the {descriptor} Museum",
		"of the Oasis",
		f"of the {descriptor} Oasis",
		f"of {descriptor} Oasis",
		"of the Ocean",
		f"of {descriptor} Ocean",
		f"of the {descriptor} Ocean",
		"of the Outpost",
		f"of the {descriptor} Outpost",
		f"of {descriptor} Outpost",
		"of the Outlands",
		f"of the {descriptor} Outlands",
		f"of {descriptor} Outlands",
		"of the Glade",
		f"of the {descriptor} Glade",
		f"of {descriptor} Glade",
		"of the Grassland",
		f"of the {descriptor} Grassland",
		"of the Graveyard",
		f"of the {descriptor} Graveyard",
		"of the Grove",
		f"of the {descriptor} Grove",
		f"of the {descriptor} Abyss",
		"of The Seventh Hell",
		"of Hell",
		"of the Hells",
		f"of the {descriptor} Hells",
		"of Horus",
		"of the Jewels",
		"of the Ruby",
		"of Gold",
		"of Silver",
		"of Iron",
		"of Steel",
		"of the Underworld",
		f"of the {descriptor} Sanctum",
		f"of the {descriptor} Palace",
		f"of the {rank} Palace",
		"of Osiris",
		"of Helios",
		"of Helio",
		"of Helion",
		"of Heliod",
		"of Blood",
		f"of the {rank} Shrine",
		"of Akros",
		"for the Hunt",
		"of Kiranta",
		f"for the {descriptor} Hunt",
		"of Lunden",
		"of Ages",
		"of the Ages",
		"of Londinium",
		"of the Great Hunt",
		"of Azurius",
		"of Power",
		"of Darkwood",
		"of the Blood Rites",
		f"of the {descriptor} Rites",
		f"of the {rank}'s Island",
		f"of the {descriptor} Island",
		f"of the {descriptor} Hunt",
		"of the Moon Fortress",
		f"of the {descriptor} Fortress",
		f"of the {descriptor} Throne",
		f"of the Throne",
		"of Queen Boudica",
		"of Liliana",
		"of Athens",
		"of Paradise",
		"of Vesuvius",
		"of Vesuvia",
		"of the Glade",
		"of Carcosa",
		"of Azorius",
		"of Nylea",
		"of Rakdos",
		"of the Monolith",
		"of the Smoke",
		"of The Capital",
		"of the Triumvirate",
		f"of the {descriptor} Triumvirate",
		f"of The {descriptor} Smoke",
		f"of The {descriptor} Capital",
		"of the Overgrown Forest",
		"of the Overgrown Land",
		f"of the {descriptor} Monolith",
		"of the Wild Hunt",
		f"of the {descriptor} Hunt",
		f"of the {rank}'s Hunt",
		"of the Ancient Tomb",
		f"of the Broken Land",
		f"of the Sea Gate",
		"of the Deep",
		f"of the {rank}'s Revenge",
		f"of the {rank}'s Menace",
		f"of the Raging Storm",
		f"of the {descriptor} Storm",
		f"of the {descriptor} Fountain",
		f"of the {descriptor} Gate",
		f"of the {descriptor} Land",
		f"of the {descriptor} Tomb",
		f"of the {descriptor} Forest",
		f"of the {rank}'s Palace",
		f"of the {rank}'s Glade",
		f"of the {rank}'s Gate",
		f"of the {rank}'s Land",
		f"of the {rank}'s Forest",
		f"of the {rank}'s Tomb",
		"of the Blossoming Sands",
		f"of the {rank}",
		f"of the {rank}",
		f"of the {rank}",
		f"of the {rank}",
		f"of the {rank}'s Road'",
		f"of the {rank}'s Road'",
		f"of the {rank}'s Road'",
		f"of the {rank}'s Road'",
		"of the Pilgrim's Road",
		"of Myth",
		"Of The Marsh",
		"of the Talisman",
		"of Memory",
		"of the Tiger",
		"of Extinction",
		f"of the {descriptor} Sandbar",
		f"of the {descriptor} Sun's Zenith",
		f"of {descriptor} Memory",
		"of the Watcher",
		"of the Consulate",
		"of the False God",
		f"of the {descriptor} God",
		"of Spirits",
		"of the Moon",
		"Of Mirrodin",
		"of the Depths",
		"of Might",
		"of the Provinces",
		"of the Stars",
		f"of the {descriptor} Star",
		f"of {descriptor} Might",
		"of the Elemental",
		f"of the {descriptor} Elemental",
		"Of Denial",
		"of the Sun",
		"of the Black Sun",
		f"of the {descriptor} Sun",
		"of the Spirit",
		"of the Spirits",
		f"of the {descriptor} Spirit",
		f"of the {descriptor} Spirits",
		"of the Damned",
		"of the Sands of Time",
		f"of the {descriptor} Fire",
		f"of {descriptor} Fire",
		f"of the Temple",
		f"of the {descriptor} Temple",
		f"of the {descriptor} Temple",
		"of Death",
		f"of the {rank}'s' Temple",
		f"of Fire",
		"of the Flames",
		f"of the {descriptor} Flames",
		f"of the {descriptor} Descent",
		f"of the {descriptor} Destiny",
		f"of the {descriptor} Fire",
		f"of the {descriptor} Heritage",
		f"of the {descriptor} Hoard",
		f"of the {descriptor} Horn",
		f"of the {descriptor} Lineage",
		f"of the {descriptor} Maze",
		f"of the {descriptor} Ocean",
		f"of the {descriptor} Sea",
		f"of the {descriptor} Shore",
		"Of Death",
		"of the Enigma",
		"of the Eclipse",
		"Of Blood",
		"of the Blood Court",
		"of the Throne",
		"of the Tomb",
		"of the Underworld",
		"of the Cavern",
		f"of {descriptor} Duty",
		f"of the {descriptor} Tribe",
		f"of the {descriptor} Wings",
		f"of the {descriptor} Tomb",
		f"of the {descriptor} Throne",
		f"of the {descriptor} Legion",
		f"of the {descriptor} Realm",
		f"of the {descriptor} Court",
		f"of the {descriptor} Blood",
		f"of the {descriptor} Castle",
		f"of the {descriptor} Jungle",
		"of Darkness",
		"of the Covenant",
		f"of the {descriptor} Covenant",
		f"of the {descriptor} Depths",
		"of the Depths",
		"of the Unknown",
		f"of the {descriptor} Unknown",
		"of the Dragon",
		f"of the {descriptor} Prophecy",
		"of the Blood Moon",
		f"of the {descriptor} Moon",
		f"of the {descriptor} Prophecy",
		"of the Plains",
		"of the Hunt",
		"of the Stars",
		f"of the {descriptor} Dream",
		"of the Spirits",
		f"of the {descriptor} Spirit",
		f"of the {descriptor} Mountain",
		f"of the {descriptor} Lair",
		"Of Heaven",
		"Of Justice",
		f"of the {descriptor} Death",
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
		f"of the {descriptor} Maelstrom",
		f"of the {descriptor} Whirl",
		f"of the {descriptor} Realm",
		f"of the {descriptor} Vision",
		f"of the {descriptor} Depth",
		f"of the {descriptor} Sands",
		f"of the {descriptor} Storm",
		f"of the {descriptor} Frontier",
		f"of the {descriptor} Battle",
		f"of the {descriptor} Roar",
		f"of the {descriptor} Forest",
		f"of the {descriptor} Meadow",
		f"of the {descriptor} Glades",
		f"of the {descriptor} Forest",
		f"of the {descriptor} Realm",
		f"of the {descriptor} Legend",
		f"of the {descriptor} Wild",
		f"of the {descriptor} Tundra",
		f"of the {descriptor} Pack",
		f"of the {descriptor} Roar",
		f"of the {descriptor} Grove",
		f"of the {descriptor} Sea",
		f"of the {descriptor} Depths",
		"of the Void",
		"of the Stars",
		 f"of the {descriptor} World",
		 f"of the {descriptor} Ruin",
		 f"of the {descriptor} Jungle",
		 f"of the {descriptor} Land",
		"of the Endless Hunt",
		f"of the {descriptor} Hunt",
		]

	# Backgrounds 		{descriptor}
	if "Berserker"	in genus:
		origin += [
		 f"of the {descriptor} Fury",
		 f"of the {descriptor} Tribe",
		 f"of the {descriptor} Lands",
		 f"of the {descriptor} Mountain",
		 f"of the {descriptor} Clan",
		 f"of the {descriptor} Raid",
		 "of the Colosseum",
		]
	if "Bard"		in genus:
		origin += [
			"of the Festival",
			]
	if "Barbarian"	in genus:
		origin += [
		 f"of the {descriptor} Tribe",
		 "Of the Colosseum",
		]
	if "Cleric" 	in genus:
		origin += [
		"of Rebirth",
			"from Heaven",
			f"from the {descriptor} Heaven",
			f"of the {descriptor} Gods",
			"of the Gods",
			"of the Holy Order",
			"of the Order",
			"of the Mission",
			"of the Journey",
			"of the Path",
			"of the Light",
			f"of the {descriptor} Order",
			f"of the {descriptor} Order",
			f"of the {descriptor} Mission",
			f"of the {descriptor} Journey",
			f"of the {descriptor} Pilgrimage",
			f"of the {descriptor} Crusade",
			f"of the {descriptor} Path",
			f"of the {descriptor} Light",
			f"of the {descriptor} Quest",
			]
	if "Criminal" 	in genus:
		origin += [
		f"of the {descriptor} Penitentiary",
		"of the Penitentiary",
		"of the Underworld",
		"of the Network",
		f"of the {descriptor} Escape",
		f"of the {descriptor} Ambitions",
		f"of the {descriptor} Deal",
		f"of the {descriptor} Scheme",
		"Of the Colosseum",
		]
	if "Cultist" 	in genus:
		origin += [
		"of the Abhorrent",
			"from Heaven",
			f"from the {descriptor} Heaven",
			f"of the {descriptor} Gods",
			f"of the Gods",
			"of the Sect",
			"of Rites",
			"of the Order",
			"of the Ritual",
			"of the Yellow King",
			"of the King in Yellow",
			f"of the {descriptor} King",
			]
	if "Expert" 	in genus:
		origin += [
			f"of {descriptor} Field",
			f"of {descriptor} Trade",
			f"of {descriptor} Study",
			f"of {descriptor} Research",
			f"of {descriptor} Skill"]
	if "Explorer" 	in genus:
		origin += [
			"of the Uncharted Lands",
			f"of the Jungle",
			f"of the {descriptor} Jungle",
			f"of the {descriptor} Expedition",
			f"of the {descriptor} Journey",
			f"of the {descriptor} Quest",
			f"of the {descriptor} Frontiers",
			]
	if "Crafter" 	in genus:
		origin += [
			f"of the {descriptor} Hand",
			f"of the {descriptor} Market",
			f"of the {descriptor} Design",
			f"of the {descriptor} Creation",
			f"of the {descriptor} Mind"]
	if "Druid" 		in genus:
		origin += [
		"of the Wild",
		"of the Jungle",
		"of the Woods",
		"of the Grove",
		f"of the {descriptor} Circle",
		f"of the {descriptor} Circle",
		f"of the {descriptor} Circle",
		f"of the {descriptor} Circle",
		f"of the {descriptor} Circle",
		f"of the {descriptor} Circle",
		f"of the {descriptor} Circle",
		f"of the {descriptor} Circle",
		f"of the {descriptor} Circle",
		f"of the {descriptor} Circle",
		f"of the {descriptor} Woods",
		f"of the {descriptor} Woods",
		f"of the {descriptor} Woods",
		f"of the {descriptor} Jungle",
		f"of the {descriptor} Jungle",
		f"of the {descriptor} Jungle",
		f"of the {descriptor} Jungle",
		]
	if "Guard" 		in genus:
		origin += [
			f"of the {descriptor} Guards",
			f"of the {rank} Guards",
			f"of the {descriptor} Watch",
			f"of the {descriptor} Fortress",
			f"of the {descriptor} Wall",
			f"of the {descriptor} Gate",
			f"of the {descriptor} Patrol",
			f"of the {descriptor} Tower",
			f"of the {descriptor} Keep",
			]
	if "Healer" 	in genus:
		origin += [
			"from Heaven",
			f"from the {descriptor} Heaven",
			f"of the {descriptor} Gods",
			f"of the {descriptor} Touch",
			f"of the {descriptor} Remedy",
			f"of the {descriptor} Hand",
			f"of the {descriptor} Treatment",
			f"of the {descriptor} Care",
				   ]
	if "Hero" 		in genus:
		origin += [
			"from Heaven",
			f"from the {descriptor} Heaven",
			f"of the {descriptor} Gods",
			f"of the {descriptor} Deed",
			f"of the {descriptor} Battle",
			f"of the {descriptor} Venture",
			f"of the {descriptor} Quest",
			f"of the {descriptor} Cause",
			"of the Colosseum",
			f"Of the {descriptor} Colosseum",
			]
	if "Hunter" 	in genus:
		origin += [
			f"of the {descriptor} Jungle",
			f"of the {descriptor} Hunt",
			f"of the {descriptor} Stealth",
			f"of the {descriptor} Wilderness",
			f"of the {descriptor} Range",
			f"of the {descriptor} Snares",
			 "of the Wild Hunt",
			f"of the {descriptor} Hunt",
			]
	if "Knight" 	in genus:
		origin += [
			f"of the {descriptor} Gods",
			f"of the {descriptor} Order",
			f"of the {descriptor} Quest",
			f"of the {descriptor} Deed",
			f"of the {descriptor} Battle",
			f"of the {descriptor} Venture",
			]
	if "Mage" 		in genus:
		origin += [
			"of Mysteries",
			"of Mystical Arts",
			"of the Scrolls",
			"of Potions",
			f"of the {descriptor} Academy",
			f"of the {descriptor} Tower",
			f"of the {descriptor} Scroll",
			f"of the {descriptor} Mystery",
			]
	if "Monk" 		in genus:
		origin += [
			"from Heaven",
			f"from the {descriptor} Heaven",
			f"of the {descriptor} Gods",
		  f"of the {descriptor} Path",
		  f"of {descriptor} Enlightenment",
		  f"of {descriptor} Tranquility",
		  f"of the {descriptor} Way",
		  f"of {descriptor} Balance",
		  f"of {descriptor} Order",
		  ]
	if "Merchant" 	in genus:
		origin += [
			f"of the {descriptor} Empire",
			f"of the {descriptor} Market",
			f"of the {descriptor} Venture",
			f"of the {descriptor} Organization",
			f"of the {descriptor} Company",
			f"of the {descriptor} Company",
			f"of the {descriptor} Company",
			f"of the {descriptor} Company",
			f"of the {descriptor} Corporation",
			f"of the {descriptor} Corporation",
			f"of the {descriptor} Corporation",
			f"of the {descriptor} Corporation",
			f"of the {descriptor} Corporation",
			]
	if "Pirate" 	in genus:
		origin += [
			"of Blackbeard",
			f"of the {descriptor}beard",
			f"of the {descriptor} Sea",
			f"of the {descriptor} Crew",
			f"of the {descriptor} Voyage",
			f"of the {descriptor} Journey",
			f"of the {descriptor} Fleet",
			f"of the {descriptor} Ship",
			f"of the {descriptor} Treasure",
			]
	if "Ranger" 	in genus:
		origin += [
			f"of the {descriptor} Jungle",
			f"of the {descriptor} Paths",
			f"of the {descriptor} Hunts",
			f"of the {descriptor} Camps",
			f"of the {descriptor} Mountains",
			f"of the {descriptor} Secrets",
			]
	if "Scholar" 	in genus:
		origin += [
			f"of the {descriptor} Academy",
			f"of the {descriptor} Society",
			f"of the {descriptor} Library",
			f"of the {descriptor} Lecture",
			f"of the {descriptor} Scroll",
			]
	if "Soldier" 	in genus:
		origin += [
			f"of the {descriptor} Regiments",
			f"of the {descriptor} Regiment",
			f"of the {descriptor} Regiment",
			f"of the {descriptor} Fronts",
			f"of the {descriptor} Fronts",
			f"of the {descriptor} Commands",
			f"of the {descriptor} Units",
			f"of the {descriptor} Operations",
			f"of {descriptor} Operations",
			"of the Colosseum",
			f"of the {descriptor} Colosseum",
			]
	if "Wizard"		in genus:
		origin += [
		"of Merlin",
		]
	if "Sorcerer" 	in genus:
		origin += [
		f"of {descriptor} Ancestry",
		f"of {descriptor} Descent",
		f"of {descriptor} Genealogy",
		f"of {descriptor} Origin",
		f"of {descriptor} Birth",
		f"of {descriptor} Blood",
		f"of {descriptor} Heritage",
		f"of {descriptor} Origin",
		f"of {descriptor} Birth",
		]
		# Races			{descriptor}

	# Species
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
				f"of the {descriptor} Tale",
				"of the Hidden Dojo",
				"of the Martial Paths",
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
		origin += [
			"of Carcosa",
			"of the Deep",
			f"of the {descriptor} Deep",
			"of the Dark Void",
			f"of the {descriptor} Void",
			
			]
		if "Githzerai" 			in genus:
			origin += [
			"of the Inner Peace",
			 "of the Mystic Paths",
			 "of the Ascetic Way",
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
				f"of the {descriptor} Bodies",
				f"of the {descriptor} Hive",
				f"of the {descriptor} Web",
				f"of the {descriptor} Realm",
				f"of the {descriptor} Infection"]
		if "Symbioid" 			in genus:
			origin += [
				f"of the {descriptor} Union",
				f"of the {descriptor} Hive",
				f"of the {descriptor} Web",
				f"of the {descriptor} Organism"]
		if "Alien Spawn" in genus:
			origin += [
			f"of the {descriptor} World",
			f"of the {descriptor} Realm",
			f"of the {descriptor} Cosmos",
			f"of the {descriptor} Dominions",
			f"of the {descriptor} Terror"]
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
			"of the Pack",
			"of the Stampede",
			f"of the {descriptor} Stampede",
			"of the Jungle",
			f"of the {descriptor} Jungle",
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
				f"of the {descriptor} Isle",
				f"of the {descriptor} Jungle",
				f"of the {descriptor} Grove",
				f"of the {descriptor} Peak",
				f"of the {descriptor} Wild"]
		if "Monkey King" 	in genus:
			origin += [
				f"of the {descriptor} Mischief",
				f"of the {descriptor} Path",
				f"of the {descriptor} Mountain",
				f"of the {descriptor} Realm",
				f"of the {descriptor} Adventure"]
		if "Armored Bear" 	in genus:
			origin += [
				f"of the {descriptor} Realm",
				f"of the {descriptor} Fortress",
				f"of the {descriptor} Clan",
				f"of the {descriptor} Woods",
				f"of the {descriptor} Defenders"]
		if "Tiger" 			in genus:
			origin += [
				"of the Snow",
				f"of the {descriptor} Mountain",
				f"of the {descriptor} Forests",
				f"of the {descriptor} Valleys",
				"of the Frost",
				"of the Hunt",
				f"of the {descriptor} Hunt",
				]
		if "Vulture" 		in genus:
			origin += [
				"of Death",
				f"of the {descriptor} Sky",
				f"of the {descriptor} Omen",
				f"of the {descriptor} Desert"
				]
		if "Deer" 			in genus:
			origin += [
			f"of the {descriptor} Woods",
			f"of the {descriptor} Glade",
			f"of the {descriptor} Trail",
			f"of the {descriptor} Path",
			f"of the {descriptor} Kingdom",
			f"of the {descriptor} Lake",
			]
		if "Owl" 			in genus:
			origin += [
			f"of the {descriptor} Knowledge",
			f"of the {descriptor} Sky",
			f"of the {descriptor} Hunt",
			f"of the {descriptor} Vision",
			f"of the {descriptor} Woods",
			]
	if "Kitsune"	in genus:
		origin += [
			"of Nine Tails",			"of Nine Tails",			"of the Trickster",
			]
	if "Catfolk"	in genus:
		origin += [
		"of the Pride",
		f"of the {descriptor} Pride",
		]
	if "Elf"		in genus:
		origin += [
		"of Llanowar",
		"of the Elves",
		]
	if "Fiend"		in genus:
		origin += [
		"of Heaven",
		"of Avernus",
		f"of the {descriptor} Heaven",
		"of Hades",
		"of the Underworld Gates",
		"of the Pit",
		]

	origin += [
		f"of the {descriptor} War",
		f"of the {rank} War",
		"of the Sun Stone",
		f"of the {descriptor} Stone",
		"of Souls",
		"of Bane",
		"of Tiamat",
		f"of The {descriptor} Town",
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
		f"of the {descriptor} Realm",
		f"of the {descriptor} Church",
		f"of the {descriptor} Dawn",
		f"of the {descriptor} Grove",
		f"of the {descriptor} Desert",
		f"of the {descriptor} Dragon",
		f"of the {descriptor} Elders",
		f"of the {descriptor} Faith",
		f"of the {descriptor} Forest",
		f"of the {descriptor} Kingdom",
		f"of the {descriptor} Mountain",
		f"of the {descriptor} Night",
		f"of the {descriptor} Phoenix",
		f"of the {descriptor} Plains",
		f"of the {descriptor} River",
		f"of the {descriptor} Sea",
		f"of the {descriptor} Star",
		f"of the {descriptor} Swamp",
		f"of the {descriptor} War",
		"of Vampires",
		f"of the {descriptor} Arts",
		f"of the {descriptor} Flame",
		f"of the {descriptor} Order",
		f"of the {descriptor} Eternal",
		f"of the {descriptor} Fire",
		f"of the {descriptor} Firestorm",
		f"of the {descriptor} Gate",
		f"of the {descriptor} Labyrinth",
		f"of the {descriptor} Mountain",
		f"of the {descriptor} Realm",
		f"of the {descriptor} Saga",
		f"of the {descriptor} Waterfall",
		f"of the {descriptor} Woods",
		f"of the {descriptor} Thieves",
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
		f"of the {descriptor} Land",
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
		f"of the {descriptor} Tomb",
		"of the Sun",
		"of the Golden Hoard",
		f"of the {descriptor} Hoard",
		]

	if "Rogue" in genus:
		origin += [
			"of the Shadows",
			f"of the {descriptor} Shadow",
			f"of the {descriptor} Plot",
			f"of the {descriptor} Escape",
			f"of the {descriptor} Underworld",
			f"of the {descriptor} Heist"]
	if "Shaman" in genus:
		origin += [
			f"of the {descriptor} Gods",
			f"of the {descriptor} Jungle",
			f"of the {descriptor} Rites",
			f"of the {descriptor} Visions",
			f"of the {descriptor} Forces",
			f"of the {descriptor} Traditions",
			f"of the {descriptor} Spirits",
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
			f"of the {descriptor} Jungle",
			f"of the {descriptor} Path",
			f"of the {descriptor} Expedition",
			f"of the {descriptor} Tribe",
			f"of the {descriptor} Voyage",
			f"of the {descriptor} Discovery"]
	if "Trickster" in genus:
		origin += [
			"of the Street",
			f"of the {descriptor} Corner",
			f"of the {descriptor} Alleys",
			]
	if "Warrior" in genus:
		origin += [
		f"of the Colosseum",
		f"of the {descriptor} Colosseum",
			f"of the {descriptor} Arena",
			f"of the {descriptor} Campaign",
			f"of the {descriptor} Conquest",
			f"of the {descriptor} Combat",
			f"of the {descriptor} Duels",
			f"of the {descriptor} War",
			]
	if "Warlock" in genus:
		origin += [
			f"of the {descriptor} Gods",
			"of the Deal",
			"of the King in Yellow",
			"of The Master",
			"of the Sold Soul",
			f"of the {descriptor} God",
			f"of the {descriptor} King",
			f"of the {descriptor} Lore",
			f"of The {descriptor} Master",
			f"of the {descriptor} Powers",
			f"of the {descriptor} Rites",
			f"of the {descriptor} Secrets",
			]
	if "Witch" in genus:
		origin += [
			"of La Llorona",
			"of the Enchanting Spell",
			f"of the {descriptor} Arts",
			f"of the {descriptor} Curse",
			f"of the {descriptor} Curses",
			f"of the {descriptor} Jungle",
			f"of the {descriptor} Ritual",
			f"of the {descriptor} Spell",
			f"of the {descriptor} Tradition",
			]
	if "Priest" in genus:
		origin += [
			"from Heaven",
			f"from the {descriptor} Heaven",
			f"of the {descriptor} Gods",
			"of the Orders",
			f"of the {descriptor} Congregation",
			f"of the {descriptor} Ministry",
			f"of the {descriptor} Order",
			f"of the {descriptor} Rite",
			f"of the {descriptor} Sanctuary",
			]
	if "Aberration" in genus:
		origin += [
			"of the Jungle",

			f"of the {descriptor} Jungle",

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
		origin += [	"of the Thousand Eyes",
					
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
			f"of the {descriptor} Palace",
			f"of the {descriptor} Court",
			f"of the {descriptor} Estate",
			f"of the {descriptor} Mansions",
			f"of the {descriptor} Council",
			f"of the {descriptor} Assembly",
			]
	if "Goblin" in genus:
		origin += [
    "of the Clan Zanzigzags", "of the Clan Fuddleheads", "of the Caravan of Nowherelse", "of the Pirate Paraders",  f"of the {descriptor} Klan", "of the Rusty Dagga Klan",		f"of the {descriptor} Dagga Klan", "of the Broke Toof Klan",		f"of the {descriptor} Toof Klan", "of the Sneeky Shaddaz Klan",	f"of the {descriptor} Shaddaz Klan", "of the Raginfaya Klan",		f"of the {descriptor} Fiya Klan", "of the Laffinskullz Klan", f"of the {descriptor} Skull Klan", f"of the {descriptor} Moon Klan", "of the Mystik Mushrumz Klan", "of the Spareem Klan", "of the Gligrove Klan", "of the Frosternz Klan", "of the Vybroilet Klan", "of the Whimzikren Klan", "of the Moonlinyun Klan", "of the Dazzliancaz Klan", "of the Enchantenvoyz Klan", "of the Silvant Klan", "of the Gleamguard Klan", "of the Raydirunnaz Klan", "of the Mystinger Klan", "of the Faefollowaz Klan", "of the Shaddasneek Klan", "of the Lunalurka Klan", "of the Sinistez Klan", "of the Vortekandalz Klan", "of the Zanizip Klan", "of the Puzzleress Klan", "of the Trickytinka Klan", "of the Unbrites Klan", "of the Snareroot Clan", "of the Gravetooth Gigglers", "of the Marblesharp Klan", "of the Shaddafriend Klan", "of the Tanglestride Clan", "of the Wackiskaz Klan", "of the Riddleskull Clan", "of the Gigglang Klan", "of the Twistailz Klan", "of the Crookknee Clan", "of the Zanzigzagz Klan", "of the Quirkilz Klan", f"of the {descriptor} Pirates", f"of the {descriptor} Horde", f"of the {descriptor} Nomadz", f"of the {descriptor} Swampz Klan", f"of the {descriptor} Leafz Klan", f"of the {descriptor} Shade Klan", "of the Sinistart Klan", "of the Ravvinlot Klan", "of the Riddleburr Clan", "of the Springsprong Klan", "of the Sneekyshadda Klan", "of the Lonesok Klan", "of the Sparkypark Klan", "of the Spisnow Conez Klan", "of the Skwiril Klan", "of the Stalkawalkaz Klan", "of the Threshold Shades", "of the Suntare Lot", "of the Swifity Klan", "of the Silvarviz Klan", "of the Silvandaz Klan", "of the Talktrees Lot", "of the Whizirlaz Klan", "of the Wilboarz Lot", "of the Witbitz Klan", "of the Woozlez Klan", "of the Wandrerz Klan", "of the Wrongwayz Klan", "of the Zany Zip-Zip Klan", f"of the {descriptor} Dagga", f"of the {descriptor} Fiya", f"of the {descriptor} Moon", f"of the {descriptor} Serpent", f"of the {descriptor} Shadda", f"of the {descriptor} Skull", f"of the {descriptor} Toof", f"of the {descriptor} Tree", f"of the {descriptor} Wolf", "of the Redhats Klan","of the Traphunters Clan", f"of the {descriptor} Clan","of the Rustydagger Clan", f"of the {descriptor} Dagger Clan","of the Brokentooth Clan", f"of the {descriptor} Tooth Clan","of the Sneaky Shadows Clan",	f"of the {descriptor} Shadow Clan", "of the Ragingfire Clan", f"of the {descriptor} Fire Clan", "of the Cunninfox Clan", "of the Wildboar Clan", "of the Quickfoot Clan", "of the Slyraven Clan", "of the Mudwater Clan", "of the Gleamgem Clan", "of the Fierce Wolf Clan", f"of the {descriptor} Wolf Clan", "of the Bounrabbit Clan", "of the Laughskull Clan", f"of the {descriptor} Skull Clan", "of the Dancileaf Clan", "of the Twilickster Clan", "of the Lunantern Clan", f"of the {descriptor} Moon Clan", "of the Mystimushroom Clan", "of the Whisperwillow Clan", "of the Starstalker Clan", "of the Enchantember Clan", "of the Dancedrop Clan", "of the Shimmershade Clan", "of the Gleaminglade Clan", "of the Blinkblossom Clan", "of the Sparkleam Clan", "of the Glimmerove Clan", "of the Sylvadow Clan", "of the Charmerry Clan", "of the Moonmarauder Clan", "of the Deweamer Clan", "of the Frostern Clan", f"of the {descriptor} Tree Clan", "of the Etherelm Clan", "of the Vibriolet Clan", "of the Whimsicren Clan", "of the Moonlinion Clan", "of the Dazzlancer Clan","of the Enchantenvoy Clan", "of the Sylvant Clan", "of the Gleamguardian Clan","of the Radiant Runner Clan", "of the Mystic Messenger Clan", "of the Whimward Clan", "of the Fey Messenger Clan", "of the Nocturnal Nuisance Clan", "of the Mystic Mirage Clan", "of the Twilight Trickster Clan", "of the Dusk Dweller Clan", "of the Midnight Marauder Clan", "of the Veiled Vagabond Clan", "of the Lunar Lurker Clan", "of the Nightshade Clan", "of the Crimson Clan", "of the Vortex Vandals", "of the Moxier Clan", "of the Unbrights Clan", "of the Laterunner Clan", "of the Shadowtrippers Clan", "of the Moonlit Misrule Clan", "of the Jarstuckers Clan", "of the Dancing Tree Clan", "of the Rockmunch Clan", "of the Sunstarer Clan", "of the Tallyrot Clan", "of the Moonbark Clan", "of the Marblesharp Clan",  "of the Redsnow Clan", "of the Shadowfriend Clan", "of the Broken Compass Nomads", "of the Tail Twisters Clan", f"of the {descriptor} Pirates", f"of the {descriptor} Horde", f"of the {descriptor} Nomads", f"of the {descriptor} Travelers", f"of the {descriptor} Swamp", f"of the {descriptor} Leaf", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", f"of the {descriptor} Clan", "of the Boggle Clan", "of Brilliantbolt Clan", "of the Broken Compass Nomads", "of Brokentooth Clan", "of the Trickster Clan", "of the Dull Blade Clan", "of the Dusk Dwellers", "of the Enchanember Clan",  "of the Pumpkin Smasher Clan", "Of the Dreamwalker Clan", "of the Enchanted Elm Clan", "of the Treethrower Clan", "of the Tripfeet Clan", "of the Holefeller Clan","of the Feywild Fellows", "of the Fierce Wolf Klan", "of the Forgotten Name Clan", "of the Fuzzy Clan", "of the Gleamgem Clan", "of the Gleamglade Clan", "of the Gringuardian Clan", "of the Gloomgrin", "Of the Bulcander Clan", "of the Lost Clan", "of the Hidden Clan", "of the Laughing Skull Clan", "of the Lost Clan", "of the Lost Marble Clan", "of the Lunar Lurker Clan", "of the Lustrous Clan", "of the Marblesharp Klan", "of the Tatiana Messengers Clan", "of the Oberon Messengers Clan", "of the Midnight Marauder Klan", "of the Moonbark Klan", f"of the {descriptor} Mystic Clan", f"of the {descriptor} Mushroom Clan", "of the Nightshade Clan", f"of the Nocturnal {rank}", f"of the {descriptor} Brawler", "of the Keenscent Clan", "of the Unbright Clan", "of the Obsidian Clan", "of the Quickfoot Clan", "of the Radiant Runner Clan", "of the Redhats", "of the Redsnow Klan", "of the Rock Eater Clan", "of the Rusty Clan", "of the Shadow Clans", f"of the {descriptor} Shade", f"of the {descriptor} Raven", "of the Spring Court", "of the Sunstarer Clan", "of the Titan's Servant Clan", "of the Sylvan Shadows", "of the Traphunter Clan", "of the Veiled Vagabonds", "of the Vortex Vandals", "of the Whispering Willow Clan", "of the Wild Boar Clan", "of the Wrong Nomads", f"of the {descriptor} Clan", f"of the {descriptor} Dagger Clan", f"of the {descriptor} Fire Clan", f"of the {descriptor} Moon Clan", f"of the {descriptor} Serpent Clan", f"of the {rank} Shadow Clan", f"of the {descriptor} Shadow Clan", f"of the {descriptor} Skull Klan", f"of the {descriptor} Tooth Clan", f"of the {descriptor} Tree Clan", f"of the {descriptor} Wolf Clan", "of the Redhat Clan","of the Trapsnack Hunters Clan", "of the Bright Shadow Clan", "of the Harmless Marauders", "of the Foxfire Clan","of the Tealeaf Tricksters", "of the Dewdrop Dancer Clan", "of the Peacebrawlers", "of the Startrail Stalkers", "of the Briarhop Clan", "of the Hollowstep Marchers", "of the Wallwalkers", "of the Sock Seekers", "of the Witchlight Wastrels", "of the Beerspearer Clan", "of the Dagger Swagger Clan", "of the Moon Goons", "of the Shade Parade", "of the Fireflyers", "of the Veilvanish", "of the Midmuckers", "of the Gloomgrin Gang", 
	"of the Mystic Messengers", "of the Mud Nomads", "of the Leaf Loafers",	"of the Swamp Marchers", f"of the {descriptor} Horde", f"of the {rank} Horde", "of the Pirate Parade", f"of the {rank} Parade",	f"of the {descriptor} Firedancers", f"of the {descriptor} Wolfriders", f"of the {descriptor} Pirates", f"of the {descriptor} Horde", f"of the {descriptor} Nomads", f"of the {descriptor} Travelers", f"of the {descriptor} Leaflurkers", "of the Bramblebunch Clan", "of the Clan Rubaruse", "of the Clan Sarisandal", "of the Clan Rumrazor", "of the Klan Makrobaz", "of the Clan Bargabeh", "of the Klan Willowhisper", "of the Star Stalker Clan", "of the Shadeshimmer Clan", "of the Gladegleamer Clan", "of the Clan Baglimmer", "of the Clan Zilsylvan", "of the Klan Anarkarmers", "of the Clan Derakrifters", "of the Clan Barqaruners", "of the Lamalacky Klan", "of the Veiled Vagabonds", "of the Gloomgrin Gang", "of the Toolate Caravan", "of the Briar Mask Tricksters", "of the Wrong Dune Caravan", "of the Clan Jarstuckjam", "of the Clan Headbonkers",  "of the Pathless Caravan", "of the Slipshadow Caravan", "of the Wallwalkers Clan", "of the Sunstare Society", "of the Clan Treetalkers", "of the Clan Moonbarkers", f"of the {descriptor} Nomads", f"of the {descriptor} Clan", "of the Dullblade Nomads", "of the Kabila Mudmind Mystics", f"of the {descriptor} Caravan", "of the Broken Compass Caravan", f"of the {descriptor} Troupe", "of the Turvy Troupe", "of the Fluzzy Clan", "of the Clan Wacky Whiskers", "of the Clan Tailtwisters", "of the Zigzagers", "of the Clan Quirkyquills", "of the Fuddleheads", "of the Green Horde", "of the Caravan of Nowherelse", "of the Dustway Nomads", "of the Leaflurker Travelers", "of the Swamp Stompers", "of the Parade Pirates", f"of the {descriptor} Wolf Whistlers", f"of the {descriptor} Skull Clan", f"of the {descriptor} Moon {rank} Clan", f"of the {descriptor} Fire Dancers Clan", "of the Redjatz Klan", "of the Trapunters Klan", f"of the {descriptor} Firedancers Clan", "of the Clan Rubahruse", "of the Clan Dandanxekan", "of the Kabila Zillers", "of the Clan Gurazgallop", "of the Forgoten Name Clan",
 ]
	if "Undead" in genus:
		origin += [
		"of the Ossuary",
		"from the Ossuary",
		f"of the {descriptor} Ossuary",
		"of the Mummy",
		f"of the {descriptor} Mummy",
		"of the Zombies",
		]

	# Alignment
	if "Evil" in genus:
		origin += [
		"of Cruelty",

		]

	origin += [
		"of Cyclops",
		"of the Cyclops",
		"of Agonas",
		"of the Moon",
		"of the Moonlit Glades",
		"of the Mystical Moons",
		"of the Mythic Battles",
		"of the Natural Springs",
		"of the Night",
		"of the Obscured Mysteries",
		"of the Otherworldly Visions",
		"of the Powerful Empires",
		"of the Raven Queen",
		"of the Woodlands",
		"of Air",
		"of Dragons",
		f"of the {descriptor} Dragon",
		"of Earth",
		f"of the {descriptor} Earth",
		f"of the {descriptor} Heaven",
		"of Hell",
		f"of the {descriptor} Hell",
		f"of the {rank} Hell",
		"of Life",
		"of Light",
		f"of the {descriptor} Light",
		"of Nature",
		"of the Primal Essence",
		f"of the {descriptor} Essence",
		"of the Abbey",
		f"of the {descriptor} Abbey",
		"of the Abyss",
		"of the Abyssal Depths",
		"of the Academy",
		f"of the {descriptor} Academy",
		"of Ageless Wisdom",
		f"of {descriptor}  Wisdom",
		f"of the Ages",
		"of the Ancient Tribe",
		f"of the {descriptor} Tribe",
		f"of the Beast Realm",
		f"of the {rank} Realm",
		"of the Blackened Sky",
		f"of the {descriptor} Sky",
		"of the Blessed Waters",
		"of the Divine",
		"of Divine Will",
		"of Zeus' Will",
		"of Odin's Will",
		"of Thor's Will",
		"of Gods' Will",
		"of God's Will",
		"of King's Will",
		f"of {rank}'s Will",
		f"of the Dread Fortress",
		f"of the {descriptor} Fortress",
		"of the Elements",
		"of the Endless Night",
		f"of the {descriptor} Night",
		"of the Santa Campaña",
		"of the Eternal Chains",
		f"of the {descriptor} Chains",
		"of the Eternal Clock",
		"of the Eternal Watch",
		f"of the {descriptor} Watch",
		"of the Eternal Flame",
		f"of the {descriptor} Flame",
		"of the Ethereal Realm",
		f"of the {descriptor} Realm",
		"of the Fiery Lake",
		f"of the {descriptor} Lake",
		"of the Forbidden Arts",
		f"of the {descriptor} Arts",
		"of the Forbidden Knowledge",
		f"of the {descriptor} Knowledge",
		"of the Forbidden Throne",
		f"of the {descriptor} Throne",
		"of the Forces",
		f"of the {descriptor} Forces",
		"of the Fungal Forests",
		"of the Gale",
		"of the Glaciers",
		"of the Glade",
		"of Hellfire",
		f"of the {descriptor} Void",
		"of the Infernal Realm",
		f"of the {descriptor} Realm",
		"of the Inferno",
		f"of the {descriptor} Inferno",
		"of Lava",
		"of the Light",
		f"of the {descriptor} Light",
		"of Light",
		"of the Lost Library",
		f"of the {descriptor} Library",
		"of the Mythic Tale",
		f"of the {descriptor} Tale",
		"of Nature's Heart",
		"of Nature",
		"of the Netherworld",
		"of the Ninth Circle",
		"of Past and Future",
		"of the Primal Forest",
		f"of the {descriptor} Forest",
		"of the Realm",
		"of the Reptilian Marshes",
		"of the Road",
		f"of the {descriptor} Road",
		"of the Rocks",
		f"of the {descriptor} Rock",
		"of the Ruined Empire",
		"of the Old Empire",
		"of the Empire",
		"of the Gone Empire",
		"of the Rising Empire",
		f"of the {descriptor} Empire",
		"of the Searing Flame",
		"of the Shadowflame",
		"of the Shadows",
		f"of the {descriptor} Shadows",
		"of The Shapeless",
		"of the Slime Pits",
		"of the Spheres",
		"of the Sphere",
		f"of the {descriptor} Sphere",
		"of the Tempest",
		"of The Tempest",
		f"of The {descriptor} Tempest",
		f"of the Timeless Realm",
		f"of the {descriptor} Realm",
		"of The Tormented",
		"of the Unseen Terror",
		"of the Unseen",
		"of the Untamed Wilds",
		"of the Wailing Abyss",
		"of the Wild",
		"of the Woods",
		"of Water",
		f"of the {descriptor} Realm",
		f"of the {descriptor} Gods",
		f"of the {descriptor} Forest",
		"of the Enchanted Woods",
		"of the Eternal King",
	]
	result = random.choice(origin)
	for _ in range(10):
		words = [w.lower() for w in result.split() if w.lower() not in ('the', 'of', 'and', 'a', 'in', 'to', 'is', 'on')]
		if len(words) == len(set(words)):
			break
		result = random.choice(origin)
	return result
