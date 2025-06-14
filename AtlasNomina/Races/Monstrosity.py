'''
Monstrosities are monsters in the strictest sense—
frightening creatures that are not ordinary, not truly
natural, and almost never benign. Some are the
results of magical experimentation gone awry (such
as owlbears), and others are the product of terrible
curses (including minotaurs and yuan-ti). They defy
categorization, and in some sense serve as a catch-all
category for creatures that don’t fit into any other genus.
'''

'''
Names for Monsters
Inspirations
	- Monster (Meaning)
	# Cipactli (m,f)
	# Atargatis (f)  Belvina (f)  Ceto (f)  Cipactonal (m)  Draca (m)  Kaibutsu (m)  Kumamon (m)  Operetta (f)
'''

def Names(genus):
	MALE    = "He"    in genus
	FEMALE  = "She"   in genus
	AGENDER = "They"  in genus

	SUBgenus = "Subgenus" in genus

	Names = [
"Alatrox",			"Azatrox",			"Aatrox", 			"Gazeus",			"Aneve",			"Galak",	"Bulektri",	"Thyrm",	"Kragma",	"Slytherr",	"Vorlash",	"Grindle",	"Morgax",	"Draknos",	"Venomar",	"Thrashtalon",	"Skreech",	"Vorgash",	"Charron",	"Gloomclaw",	"Ravix",	"Snarlgrim",	"Blightfang",	"Kryx",	"Zephyros",	"Stormrend",	"Nemnir",	"Gastrix",	"Varthrax",	"Sunderbeak",	"Cyclonix",	"Razorfang",	"Shriekshell",	"Dreadmaw",	"Gorgath",	"Fenroar",	"Quillspike",		"Marlgoth",			"Ironscale",		"Ebonclaw",			"Thornback",		"Wrathmore",		"Skyterror",	"Grizzlemaul",	"Slitherfang",	"Bramblethorn",	"Nightscream",	"Cragjaw",	"Echo",	"Frostgaze",	"Infernox",	"Mudgraw",	"Obsidion",	"Ripple",	"Squall",	"Tempest",	"Whisper",	"Zephyr"	"Grendel", 	"Kaiju",	"Mothra", 	"Balrog", 	"Chimera",	"Basilisk",  	"Gorgon", 	"Behemoth",  "Medusa",	"Leviathan", 	"Rodan",  	"Cerberus",  	"King",	"Ghidorah",  		"Hydra", 			"Argus",  			"Panoptes",			"Minotaur",  		"Orthrus",   		"Hati",   			"Nemean",   		"Typhon",   	"Echidna",   	"Scylla",   	"Charybdis",   	"Manticore",  	"Griffin",  	"Sphinx",  	"Cthulhu",  	"Dagon",  	"Yogsothoth", 	"Nyarlathotep",  	"Shubniggurath",  	"Fenrir",   	"Jormungandr",  	"Tiamat",  	"Gojira",  	"Zuul",  	"Vincent",  	"Orlok",  	"Audrey",   	"Asmodeus",   	"Pazuzu",  	"Ghoul",  			"Bunyip",   		"Koatl",  			"Anansi",   		"Wendigo",   		"Jersey",   		"Kracken",			"Tarrasque",		"Chimera",			"Basilisk",			"Kraken",			"Hydra",	"Manticore",	"Gorgon",	"Roc",	"Behemoth",	"Leviathan",	"Minotaur",	"Cerberus",	"Griffin",	"Wyvern",	"Sphinx",	"Bunyip",	"Cockatrice",	"Naga",	"Harpy",	"Centaur",	"Lamia",	"Scylla",	"Orthros",	"Typhon",	"Echidna",	"Balor",	"Jersey",	"Mothman",			"Wendigo",			"Yeti",				"Sasquatch",		"Chupacabra",		"Grendel",			"Fenrir",			"Jormungandr",		"Skoll",			"Hati",				"Umberhulk",		"Doppelganger",		"Rustmonster",		"Owlbear",			"Ankheg",			"Aboleth",			"Bulette",			"Behir",	"Cloaker",	"Displacerbeast",	"Gibberingmouther",	"Jabberwock",  ,	"Zarvox",		"Carnentus",		"Rodator",		"Amrik",		"Urabrask",			"Aboleth",			"Ankeg",			"Anansi",			"Audrey",			"Argus",			"Athotep",			"Bulette",			"Behir",			"Balor",			"Bunyip",			"Behemoth",			"Basilisk",			"Bunyip",			"Behemoth",			"Basilisk",			"Balrog",			"Bramblethorn",		"Bulektri",		"Blightfang",		"Centaur",		"Chupacabra",		"Cockatrice",		"Cloaker",		"Cerberus",		"Chimera",		"Cthulhu",			"Charybdis",		"Cerberus",			"Kimera",			"Cragjaw",			"Ziclonix",			"Charron",			"Doppelganger",		"Displacer",		"Dagon",			"Dreadmaw",			"Draknos",			"Ekidna",			"Echidna",			"Echo",				"Ebonclaw",			"Fenrir",			"Fenrir",			"Frostgaze",		"Fenroar",			"Grendel",			"Gibbering",	"Mouther",		"Griffin",		"Gorgon",		"Ghoul",		"Gojira",			"Griffin",			"Gorgan",			"Godzilla",			"Grendel",			"Grizzlemaul",		"Gorgath",			"Gastrix",			"Grindle",			"Gloomclaw",		"Harpy",			"Hati",				"Hydra",			"Hati",				"Hydra",			"Infernox",			"Ironscale",		"Jersey",			"Jormungander",		"Jabberwock",		"Jersey",			"Jormungandor",		"Kraken",			"Kracken",			"Kinghidorah",		"Kaiju",			"Kragma",			"Killorak",			"Krix",		"Lamia",			"Leviatan",			"Leviathan",		"Mothman",			"Minot",			"Manticore",		"Manticore",		"Minotaur",		"Mothra",			"Mudgraw",			"Morgax",			"Marlgoth",			"Naga",				"Nyarlathotep",		"Nemean",			"Nemnir",			"Nightscream",		"Orthros",			"Owlbear",		"Orlok",			"Orthrus",			"Obsidion",			"Oxas",				"Pazuzu",			"Quetzalcoatl",		"Quillspike",		"Rustmonster",		"Roc",				"Rodan",			"Ripple",			"Razorfang",		"Ravix",			"Scylla",			"Sasquatch",		"Skoll",			"Sphinx",			"Shubniggurath",	"Sphinx",			"Scylla",			"Skoll",			"Squall",			"Slitherfang",		"Skyterror",		"Shriekshell",		"Sunderbeak",		"Slytherr",			"Skreech",			"Snarlgrim",		"Stormrend",		"Typhon",			"Tarrasque",		"Tiamat",			"Typhon",			"Tempest",			"Thornback",		"Zirm",			"Thrashtalon",		"Umberhulk",		"Vorlash",			"Vincent",			"Varthrax",			"Venomar",			"Vorgash",			"Wendigo",			"Wyvern",			"Wendigo",			"Whisper",			"Wrathmore",		"Yeti",				"Yogsothoth",		"Zarvox",			"Zuul",				"Zephyr",			"Zephyros",
			]
	return Names

def Surnames(genus):
	Surnames = Names(genus)
	return Surnames

def Phonotactic(genus):
	onset = nuclei = codas  = [""]
	onset += [
		'Prim',	"Disp",	"Ker",	"Tu",	"An",	'Zar',	'Zark',	"Cam",	'Carn',	'Har',	'Rod',	'Gol',	'Skoll', 	'Roc', 'Gurt',
		]
	nuclei += [
		'atr',	'at',	"laz",	"brer",	"rov",	"ke",	'ev',	'el',	'iv',	'ent', 	'zal',	'set',	'mak',	'nuz',	'gal'
		]
	codas += [
		"ox",	"us",	"ak",	'ox',	"er",	'ox',	'or',	'e', 	'sa',	'se', 	'si', 	'so', 	'su', 	'sha', 	'she', 'shi', 'sho', 'shu'
		]

	return onset, nuclei, codas

def Surphonotactic(genus):
	onset, nuclei, codas  = Phonotactic(genus)
	return onset, nuclei, codas
