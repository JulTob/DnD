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
 	#  (f)  Belvina (f)  Ceto (f)  Cipactonal (m)  Draca (m)  Kaibutsu (m)  Kumamon (m)  Operetta (f)
'''

def Names(genus):
	MALE    = "He"    in genus
	FEMALE  = "She"   in genus
	AGENDER = "They"  in genus

	SUBgenus = "Subgenus" in genus

	Names = [
"Kimera",			"Belvinax",			"Atargatis",		"Cipactli",			"Whisper",			"Zuksul",			"Alatrox",			"Azatrox",			"Aatrox", 			"Gazeus",			"Aneve",			"Galak",	"Bulektri",	"Thyrm",	"Kragma",	"Slytherr",	"Vorlash",	"Grindle",	"Morgax",	"Draknos",	"Venomar",	"Thrashtalon",	"Skreech",	"Vorgash",	"Charron",	"Gloomclaw",	"Ravix",	"Snarlgrim",	"Blightfang",	"Kryx",	"Zephyros",	"Stormrend",	"Nemnir",	"Gatrix",			"Varitrax",			"Sunderbeak",	"Ciclonix",			"Razorfang",		"Sriekel",		"Dreadmaw",	"Gorgath",			"Fenroar",	"Quilpik",			"Margoth",			"Ironscale",		"Ebonclaw",			"Thornback",		"Wrathmore",		"Skyterror",	"Grizzlemaul",	"Slitherfang",	"Bramblethorn",	"Nightscream",	"Cragjaw",	"Echo",	"Frostgaze",	"Infernox",	"Mudgraw",	"Obsidion",	"Ripple",	"Squall",	"Tempest",	"Whisper",	"Zephyr"	"Grendel", 	"Kaiju",			"Motra", 			"Balrog", 			"Chimera",	"Basilisk",  		"Gorgon", 			"Behemot",  		"Medusa",			"Leviatan", 	"Rodan",  			"Cerberus",  	"King",	"Gidorax",  		"Hydra", 			"Argus",  			"Panoptes",			"Minotaur",  		"Orthrus",   		"Hati",   			"Nemean",   		"Typhon",   	"Echidna",   	"Scylla",   	"Charybdis",   	"Manticore",  	"Griffin",  	"Sphinx",  	"Cthulhu",  	"Dagon",  			"Yogsozot", 	"Nyarlathotep",  	"Shubniggurath",  	"Fenrir",   		"Jormungandar",  	"Timatak", 			"Gojira",  			"Zuxul",  			"Vincent",  		"Orlok",  	"Odrex",   			"Pazuzu",  	"Gorjul",  			"Bunyip",   		"Koatl",  			"Anansi",   		"Wendigo",   		"Jersey",   		"Kracken",			"Tarrasque",		"Chimera",			"Basilisk",			"Kraken",			"Hydra",	"Manticore",	"Gorgon",	"Roc",				"Behemot",			"Leviathan",	"Minotaur",			"Cerberus",			"Griffin",	"Royvern",			"Esfinxor",			"Bunyip",			"Cockatrice",		"Naga",				"Harpay",			"Centaur",			"Lamia",			"Scarla",			"Orrosan",			"Tifon",	"Ekidan",			"Balor",	"Jersey",	"Mothan",			"Wendigo",			"Yeti",				"Sasquatch",		"Chupacabra",		"Grendel",			"Fenrir",			"Jormungandr",		"Skoll",			"Hati",				"Umberhulk",		"Doppelganger",		"Rustmonster",		"Owlbear",			"Ankheg",			"Aboleth",			"Bulette",			"Behir",			"Cloaker",			"Displacerbeast",	"Giberinmer",	"Jabberwock",  ,	"Zarvox",			"Carnentus",		"Rodator",		"Amrik",		"Urabrask",			"Aboleth",			"Ankeg",			"Anansi",			"Audrey",			"Argus",			"Athotep",			"Bulette",			"Behir",			"Balor",			"Bunyip",			"Behemoth",			"Basilisk",			"Bunyip",			"Behemoth",			"Basilisk",			"Balrog",			"Bramblethorn",		"Bulektri",			"Bligang",		"Centaur",			"Chupacabra",		"Cockatrice",		"Cloaker",		"Cerberus",		"Chimera",		"Cuthulhu",			"Charybdis",		"Cerberus",			"Kimera",			"Cragjaw",			"Ziclonix",			"Charron",			"Doppelganger",		"Displacer",		"Dagon",			"Dreadmaw",			"Draknos",			"Ekidna",			"Echidna",			"Echo",				"Ebonclaw",			"Fenrir",			"Fenrir",			"Frostaze",			"Fenroar",			"Grendel",			"Gibbering",		"Mouther",		"Griffin",		"Gorgon",		"Ghoul",		"Gojikra",			"Griffin",			"Gorgan",			"Godzilla",			"Grendel",			"Grizzlemaul",		"Gorgath",			"Gastrix",			"Grindle",			"Gloomclaw",		"Harpy",			"Hati",				"Hydra",			"Hati",				"Hydra",			"Infernox",			"Ironscale",		"Jersey",			"Jormungander",		"Jabberwock",		"Jersek",			"Jormungandor",		"Kraken",			"Kracken",			"Kinghidorah",		"Kainju",			"Kragma",			"Killorak",			"Krix",				"Lamia",			"Leviatan",			"Leviathan",		"Mothman",			"Minot",			"Manticore",		"Manticore",		"Minotaur",			"Mozra",			"Mudgraw",			"Morgax",			"Marlgoth",			"Naga",				"Nyarlathotep",		"Nemean",			"Nemnir",			"Nixream",			"Ortaros",			"Owlbear",		"Orlok",			"Orthrus",			"Obsidion",			"Oxas",				"Pazuzu",			"Quillspike",		"Rustmonster",		"Roc",				"Rodan",			"Ripple",			"Razorfang",		"Ravix",			"Scylla",			"Sasquatch",		"Skoll",			"Sfinx",			"Shubniggurath",	"Sphinx",			"Scalla",			"Skoll",			"Squall",			"Slitherfang",		"Skyterror",		"Shriekshell",		"Sunderbeak",		"Slytherr",			"Sakrec",			"Snarlgrim",		"Stormrend",		"Typhon",			"Tarrasque",		"Tiamat",			"Typhon",			"Tempest",			"Thornback",		"Zirm",				"Trashalon",		"Umberhulk",		"Vorlash",			"Vincent",			"Varthrax",			"Venomar",			"Vorgash",			"Wendigo",			"Rivern",			"Wendigo",			"Wrathmore",		"Yeti",				"Yogsothoth",		"Zarvox",			"Zefair",			"Zefirod",
			]
	return Names

def Surnames(genus):
	Surnames = Names(genus)
	return Surnames

def Phonotactic(genus):
	onset = nuclei = codas  = [""]
	onset += [
		"Esf",	'Prim',	"Disp",	"Ker",	"Tu",	"An",	'Zar',	'Zark',	"Cam",	'Carn',	'Har',	'Rod',	'Gol',	'Skoll', 	'Roc', 'Gurt',
		]
	nuclei += [
		"inx",	"ing",	'atr',	'at',	"laz",	"brer",	"rov",	"ke",	'ev',	'el',	'iv',	'ent', 	'zal',	'set',	'mak',	'nuz',	'gal'
		]
	codas += [
		"e",	"ox",	"us",	"ak",	'ox',	"er",	'ox',	'or',	'e', 	'sa',	'se', 	'si', 	'so', 	'su', 	'sha', 	'she', 'shi', 'sho', 'shu'
		]

	return onset, nuclei, codas

def Surphonotactic(genus):
	onset, nuclei, codas  = Phonotactic(genus)
	return onset, nuclei, codas
