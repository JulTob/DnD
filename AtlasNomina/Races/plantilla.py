import random

def Names(genus):
	"""
	Generate a single name for an (N)PC by
		randomly selecting from a list
		based on the elements provided in genuss [set].
	Preconditions:
	- 	<genus> should be a set that can
		contain <race>, <gender>, <subraceZ>.

	Postconditions:
	- 	Returns a string representing the
		selected name for the NPC.
	"""
	# Step 1: Check if the <gender> is valid
	# Step 2: Determine gender-related flags
	MALE    = "He"    in genus
	FEMALE  = "She"   in genus
	AGENDER = "They"  in genus

	SUBTYPE = "Subtype" in genus

	# Step 3: Initialize the list of names
	Names = [
		"Axel",			"Baldur",		"Balrog",
		"Banner",		"Barnes",		"Barney",
		"Basilisk",		"Bast",			"Bayek",
		"Bragi",		"Brook",		"Bruce",
		"Bucky",		"Bulma",		"Burney",
		"Byakuya",		"Byron",		"Castiel",
		"Cerberus",		"Cersei",		"Chief",
		"Chimera",		"Chopper",		"Circe",
		"Clark",		"Cloud",		"Cortana",
		"Coulson",		"Cronos",		"Cyclone",
		"Daenerys",		"Danerys",		"Dante",
		"Dexter",		"Diana",		"Dio",
		"Django",		"Donnar",		"Dorian",
		"Draco",		"Drake",		"Draven",
		"Drizzt",		"Echo",			"Electron",
		"Elektra",		"Ellaria", 		"Ellie",
		"Ender",		"Eragon",		"Exul",
		"Ezio",			"Ezio",			"Fitz",
		"Forajido",		"Franky",		"Freya",
		"Furiosa",		"Furiosa",		"Fury",
		"Fury",			"Gaara",		"Gambit",
		"Gandalf",		"Ged",			"Geralt",
		"Geralt",		"Gohan",		"Goku",
		"Goku",			"Gorgon",		"Grendel",
		"Halcyon",		"Hector",		"Hela",
		"Hera",			"Hermes",		"Hill",
		"Hinata",		"Hope",			"Horus",
		"Horus",		"Icarus",		"Icean",
		"Idunn",		"Inara",		"Irey",
		"Isis",			"Ixchel",		"Jabberwock",
		"Jean",			"Jesse",		"Jill",
		"Jim",			"Joel",			"Jon",
		"Jotaro",		"Jubilee",		"Jules",
		"Kai",			"Kaiju",		"Kain",
		"Kakashi",		"Kali",			"Katniss",
		"Kenpachi",		"Kent",			"Khal",
		"Kirilla",		"Korben",		"Krait",
		"Kratos",		"Kratos",		"Kuothe",
		"Kvothe",		"Lang",			"Lara",
		"Lee",			"Legolas",		"Legolas",
		"Leviathan",	"Light",		"Lirael",
		"Locke",		"Logan",		"Logan",
		"Loki",			"Loki",			"Loki",
		"Luffy",		"Luke",			"Lysandra",
		"Magneto",		"Malcom",		"Maleficent",
		"Malivar",		"Mara",			"Master",
		"Matrim",		"Maverick",		"Maximus",
		"Maximus",		"Medusa",		"Meteor",
		"Midas",		"Morena",		"Morgan",
		"Morgana",		"Morpheus",		"Morpheus",
		"Mothra",		"Mystic",		"Mystique",
		"Mystique",		"Nami",			"Narcissus",
		"Narkia",		"Naruto",		"Natasha",
		"Naxius",		"Nebula",		"Nemo",
		"Neo",			"Nick",			"Nightwing",
		"Nova",			"Nyx",			"Oak",
		"Oberyn",		"Orihime",		"Orion",
		"Orion",		"Osiris",		"Osiris",
		"Paragon",		"Parker",		"Pascal",
		"Pepper",		"Perrin",		"Perseus",
		"Perseus",		"Peter",		"Phil",
		"Phoenix",		"Phoenix",		"Phoenix",
		"Piccolo",		"Pietro",		"Portentia",
		"Potts",		"Prince",		"Quantum",
		"Quasar",		"Quetzalcoatl",	"Ra",
		"Ragnar",		"Ragnarok",		"Ramses",
		"Rand",			"Raven",		"Raven",
		"Raziel",		"Rei",			"Renji",
		"Rhea",			"Riku",			"Rincewind",
		"Rinoa",		"Robin",		"Rodan",
		"Rogers",		"Rogue",		"Rogue",
		"Romanoff",		"Rosie",		"Rowan",
		"Rukia",		"Sabriel",		"Sabrina",
		"Sabrina",		"Sakura",		"Sam",
		"Samus",		"Samwell",		"Sanji",
		"Sasuke",		"Scott",		"Seraph",
		"Shadowcat",	"Shepard",		"Sherlock",
		"Shinji",		"Shuri",		"Skywalker",
		"Snake",		"Snow",			"Solaris",
		"Solaris",		"Sora",			"Spike",
		"Squall",		"Starfire",		"Stark",
		"Steve",		"Stormborn",	"Strider",
		"Strider",		"Striker",		"Susano",
		"Sylar",		"Thalia",		"Thanos",
		"Theseus",		"Thor",			"Thor",
		"Thorin",		"Thorin",		"Tidus",
		"Tireus",		"Titan",		"Tlaloc",
		"Toushiro",		"Trinity",		"Trinity",
		"Trunks",		"Tyr",			"Tyrion",
		"Uryu",			"Usag",			"Usat",
		"Usopp",		"Vaelin",		"Valentine",
		"Valkyrie",		"Vash",			"Vega",
		"Vegeta",		"Viari",		"Vibe",
		"Vic",			"Vision",		"Vortex",
		"Watson",		"Wayne",		"Wolver",
		"Wong",			"Wraith",		"Zidane",
		"Zoro",			"Zorro",		'Keene',
		'Kovik',		'Rael',			"Anakin",
		"Anarkia",		"Artemis",		"Atreyu",
"Arthurius",
"Ada",
"Aberrant",
"Amelia",
"Anarkia",
"Anakin",
"Ares",
"Alucard",
"Altair",
"Arya",
"Athena",
"Azrael",
"Altair",
"Aelin",
"Aurora",
"Aragorn",
"Artemis",
"Aeneas",
"Achilles",
"Akiles",
"Aslan",
"Arya",
"Athena",
"Apollo",
"Artemis",
"Atreyu",

"Baldur",
"Bast",
"Blade",
"Byron",
"Brienne",
"Basilisk",
"Behemoth",

"Bellatrix",
"Blaze",

"Cloud",
"Cortana",
"Cyclone",

"Drizzt",

"Eragon",

"Frodo",

"Gandalf",

"Halcyon",

"Magneto",
"Mystique",
"Mystic",

"Nebula",

"Quasar",
"Quantum",

"Ragnarok",
"Ripley",

"Solaris",
"Striker",
"Starfire",

"Valkyrie",
"Vibe",

# Inspired by Comics
"Nightwing", "Raven",
"Shadowcat", "Electron", "Phoenix",
"Rogue", "Stormborn", "Wraith", "Gambit",
"Vortex", "Iceman", "Jubilee",  "Meteor",

# Inspired by Films
"Skywalker", "Fury", "Strider", "Neo", "Trinity", "Morpheus",
"Vader",  "Legolas",  "Thorin",
"Inara",
"Malcom",
"Lee",
"Korben", "Maximus", "Leonidas", "Katniss", "Spartacus", "Ellaria",
"Furiosa",  "Django",  "Snake", "Jules", "Vic",

# Inspired by Books
"Vaelin", "Kvothe", "Fitz", "Chivalry", "Rincewind", "Matrim", "Perrin",
"Rand", "Ged",  "Yennefer", "Geralt", "Darrow", "Ender",
"Locke", "Jean",  "Falconer", "Sabriel", "Lirael", "Rhapsody",
"Hector",  "Daenerys", "Jon", "Snow",  "Bran", "Samwell",

# Inspired by Mythology
"Odysseus", "Hermes",  "Perseus", "Theseus",
"Hercules", "Orion", "Freya", "Loki", "Thor", "Anubis", "Osiris",
"Isis", "Ra", "Horus", "Quetzalcoatl", "Tlaloc", "Ixchel", "Amaterasu", "Susanoo",
"Tsukuyomi",  "Tyr", "Bragi", "Idunn",

# Inspired by Video Games
"Squall", "Zidane", "Tidus", "Link", "Zelda", "Shepard", "Geralt",
"Yuna", "Rinoa", "Kain", "Raziel", "Dante", "Kratos", "Lara", "Samus", "Master", "Chief",
"Ezio", "Bayek", "Aloy", "Sora", "Roxas", "Axel", "Sephiroth",
"Riku", "Nathan", "Drake", "Ellie", "Joel", "Jill", "Valentine", "Leon", "Ada", "Wong",

# Inspired by Anime and Manga
"Spike", "Vash", "Alucard", "Asuka", "Rei", "Shinji", "Luffy", "Zoro", "Nami",
"Usopp", "Sanji", "Chopper", "Robin", "Franky", "Brook", "Jotaro", "Dio",
"Goku", "Vegeta", "Gohan", "Piccolo", "Trunks", "Bulma", "Light", "Naruto",
"Sasuke", "Sakura", "Kakashi", "Itachi", "Gaara", "Hinata", "Ichigo", "Rukia",
"Orihime", "Uryu", "Kenpachi", "Toushiro", "Byakuya", "Renji",

# Inspired by Pop Culture
"Sherlock", "Watson", "Dexter", "Heisenberg", "Jesse", "Tony", "Stark", "Bruce","Wayne",
"Peter", "Parker", "Clark", "Kent", "Diana", "Prince", "Steve", "Rogers", "Logan", "Bruce", "Banner",
"Natasha", "Romanoff", "Wanda", "Pietro", "Scott", "Lang", "Hope", "Shuri", "Thanos", "Loki",
"Thor", "Hela", "Odin", "Frigga", "Vision",
"Sam", "Bucky", "Barnes", "Nick", "Fury", "Maria", "Hill", "Phil", "Coulson", "Pepper", "Potts"



"Caspian",
"Cersei",
"Chimera",
"Cleopatra",
"Cerberus",
"Castiel",
"Crowley",
"Cronos",
"Circe",

"Dorian",
"Draven",
"Dante",
"Daenerys",
"Draco",
"Daemon",
"Desmond",

"Elektra",
"Echo",
"Ezio",

"Furiosa",
"Forajido",

"Goku",
"Gorgon",
"Grendel",

"Horus",
"Hera",

"Jareth",

"Khal",
"Kratos",

"Loki",
"Leia",
"Luke",
"Legolas",
"Logan",

"Maleficent",
"Morpheus",
"Maximus",
"Mystique",

"Nemo",
"Neo",
"Narkia",

"Odin",
"Orion",
"Oberyn",

"Pascal",
"Paragon",
"Phoenix",
"Perseus",

"Icarus",

"Jabberwock",

"Kaiju",
"Kali",
"Kai",

"Leviathan",
"Lucifer",
"Leonardo",
"Lysandra",

"Mothra",
"Mara",
"Midas",
"Medusa",
"Maverick",

"Nyx",
"Naxius",
"Nova",
"Narcissus",

"Osiris",


"Rodan",
"Rhea",
"Ramses",
"Rowan",
"Ripley",
"Ragnar",
"Rogue",
"Raven",

"Solaris",
"Sylar",
"Strider",
"Spartacus",
"Storm",
"Sabrina",
"Seraph",

"Tyrion",
"Trinity",
"Thorin",
"Thalia",
"Titan",

"Vega",

"Wolverine",

"Xena",

"Zeus",
"Zorro",
		]
	if MALE:
		Names += [
		"Bruce",		"Jareth", 		"Leon",
		"Leonardo",		"Leonidas",
		]
	if FEMALE:
		Names += [
		"Anna",		"Aurora",		"Auspicia",
		"Leia",
		]
	if AGENDER:
		Names += [
			"Link",
			]

	return Names

def Surnames(genus):
	"""
	Generate a single surname for an NPC by randomly selecting from a list.

	Preconditions:
	 - None.

	Postconditions:
	- Returns a string representing the selected surname for the NPC.
	"""

	# Step 1: Initialize the list of surnames
	Surnames = [
		"Heisenberg",	"Falconer",	"Neo",		"Ripley",	"Vader",
		"Smith", 		"Jones", 	"Stark", 	"Wayne",
		"Banner", 	"Kent", 	"Skywalker",
		"Bladebreaker",
		"Bonecrusher",
		"Beastmaster",
		"Bloodfist",
		"Blackthorn",
		"Bluesky",

		"Dreamchaser",
		"Duskwatcher",
		"Darkstone",

		"Maximoff",

		"Wilson",

		"Ironclad",
		"Tusker",
		"Stormhowler",
		"Mudwalker",
		"Thunderlord",
		"Stormbringer",
		"Ravenclaw",
		"Moonshadow",
		"Ironfist",
		"Fireheart",
		"Silvervein",
		"Dawnbreaker",
		"Nightshade",
		"Starfall",
		"Darkwood",
		"Lightbringer",
		"Earthshaker",
		"Skybreaker",
		"Seastalker",
		"Mountaincaller",
		"Thunderspear",
		"Sunshield",
		"Flameforge",
		"Whitewind",
		"Blackspear",
		"Goldenaxe",
		"Steelstrike",
		"Silentblade",
		"Dragonbane",
		"Wolfsbane",
		"Lionsmane",
		"Eagleseye",
		"Stoneheart",
		"Shadowdancer",
		"Battlemaster",
		"Swiftfoot",
		"Thunderclaw",
		"Snowfury",
		"Oceansong",

		"Flameseeker",
		"Frostweaver",
		"Firewhisper",
		"Frostfire",

		"Greycloud",
		"Goldeneye",

		"Highwind",
		"Ironshard",

		"Lightstep",

		"Moondancer",

		"Nightwhisper",

		"Riverblade",
		"Redraven",

		"Stormforge",
		"Stardust",
		"Sunfire",
		"Shadowhawk",
		"Stormwatcher",
		"Sandshifter",
		"Starweaver",
		"Stormrider",

		"Thunderforge",
		"Trueblade",
		"Twilight", "Bearer",

		"Windrunner",
		"Warbrute",
		"Whitewave",
		"Whitewolf",
		"Windweaver",


		]

	return Surnames

def Phonotactic(gender):
	"""
	Generate a phonotactic name string for an NPC by randomly selecting components.

	Preconditions:
	- <gender> must exist, but no specific attributes are required.

	Postconditions:
	- Returns a string combining randomly selected onset, nucleus, and coda.
	"""

	# Determine gender-related flags
	MALE    = "He"    in gender
	FEMALE  = "She"   in gender
	AGENDER = "They"  in gender

	# Define phonotactic components
	onset = ["Br", "Th", "Kr", "Gl", "Tr"]
	nuclei = ["a", "e", "i", "o", "u", "ae", "io"]
	if MALE:
		codas = ["n", "th", "k", "s", "r"]
	elif FEMALE:
		codas = ["na", "tha", "ka", "sa", "ra"]
	else:
		codas = ["ny", "thy", "ky", "sy", "ry"]

	return onset, nuclei, codas

def Surphonotactic(genus):
	"""
	Generate a phonotactic string for surnames by randomly selecting components.

	Preconditions:
	- None.

	Postconditions:
	- Returns a string combining randomly selected onset, nucleus, and coda.
	"""
	# Step 1: Define syllable components for surnames
	onset = ["Gr", "Bl", "Dr", "Vr", "Pl"]
	nuclei = ["ia", "io", "ae", "ou", "ei"]
	codas = ["x", "th", "n", "s", "m"]


	return onset, nuclei, codas
