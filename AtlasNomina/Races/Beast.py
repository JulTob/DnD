def Names(Type):
	MALE    = "He"    in Type
	FEMALE  = "She"   in Type
	AGENDER = "They"  in Type

	SUBTYPE = "Subtype" in Type
	BEAR = "Bear" in Type

	Names = [
		"Solikus",	'Icewind',	'Star', 	'Heyla',				'Aestor',				'Naxios',				'Neymor',				'Loiki',				'Wader',				'Juliuski',				"Sionwe",				"Secalus",                "Tod",                "Toby",                "Cerbero",                "Griffin",                "Storm",                "Zephyr",                "Azure",                               "Cobalt",                "Shade",        "Ghost", 	"Bagira",  	"Frost",                "Blizzard",                "Yuki",                "Abyss",                "Erebus",                "Nyx",                "Molten",                "Pyro",                "Vulcan",                "Gale",                "Cyclone",                "Aeolus",               "Crystal",                "Glint",                "Lucid",                "Depth",                "Tentaculus",                "Charybdis", 	"Fang",                "Lupus", 	"Grim",  	"Aether", 	"Celeste",                "Pegasus",                "Terra",                "Gaia",                "Atlas",                "Blaze",                "Inferno",                "Salamander",                "Cloud",                "Stratus",                "Serpens",                "Ether",                "Sky",                "Falcon",                "Crimson",                "Smaug",                "Drace",                "Void",                "Obsidian", 	"Nocturne",	"Ikuslus",	"Ikulus",
		]
	if MALE:
		Names += [
		"King",
		]

	if FEMALE:
		Names += [
		"Saphira",	"Queen",
		]
	if BEAR:
		Names += [
			"Kuma",		'Panda',			"Kuma",			"Akuma",				"Iorek",				"Bjorn",			"Ursus",
			]
	if  "Lion" in Type or "Leon" in Type:
		Names += [
		'Quasali',		"Storm",		"Atalon",
		]

	if  "Monkey" in Type:
		Names +=  [
				  "Sunwukong",
				  "Hanzi",
				  "Bali",
				  "Songoku",
				  "Son",
				  "Sun",
				  "Wukon",
				  "Goku",
				  "Gotan",
				  ]

	if  "Kong" in Type:
		Names   +=  [
				"Donkey",
				"King",
				"Titus"
				]

	if  "Eagle" in Type:
		Names   +=  [
				"Thorondor",
				"Gwaihir",
				"Aquila"
				]

	if  "Lion" in Type:
		Names +=  [
			"Aslan",	"Simba",	"Leo",	"Simba",
			]

	if  "Tiger" in Type:
		Names +=  [
			  "Byakko",
			  "Rajah",
			  "Frost",
			  ]

	if  "Vulture" in Type:
		Names +=  [
			  "Carrion",
			  "Voltura",
			  "Nekhbet",
			  ]

	if  "Kitsune" in Type:
		Names +=  [
			  "Kurama",
			  "Yako",
			  "Renard",
			  "Vulpik",
			  "Vulpin",
			  ]
		if FEMALE:
			Names += [
			  "Vulpika",
			  "Vulpina",
				]
	if  "Deer" in Type:
		Names +=  [
		  "Hart",
		  "Cernunnos",
		  "Elen",
		  ]

	if  "Owl" in Type:
		Names +=  [
		  "Blodeuwedd",
		  "Strix",
		  "Noctua",
		  ]
	if  "Stag" in Type:
		Names +=  [
		  "Altair",
		  "Orion",
		  "Sephiroth",
		  "Sirius",
		  "Odin",
		  "Thor",
		   ]

	if  "Wolf" in Type:
		Names +=  ["Fenris",
				   "Skoll",
				   "Hati"]
	if  "Forest" in Type:
		Names +=  [
					"Silvanus",
					"Pan",
					"Cernunnos",
								  ]

	if  "Whale" in Type:
		Names +=  [
					"Cetus",
					"Orion",
					"Nebula",
							  ]
	if  "Dinosaur" in Type: Names +=  ["Gojira", "Rex", "Indominus"]
	if  "Dog" in Type: Names +=  ["Cerberus", "Orthrus", "Hades"]
	if  "Sun Scarab" in Type: Names +=  ["Khepri", "Ra", "Surya"]
	if  "Jackal" in Type: Names +=  ["Anubis", "Luna", "Chandra"]
	if  "Spider" in Type: Names +=  ["Arachne", "Lloth", "Tsuchigumo"]
	if  "Serpent" in Type: Names +=  ["Jormungandr", "Leviathan", "Nidhogg"]
	if  "Elephant" in Type: Names +=  ["Ganesha", "Indra", "Manfred"]

	return Names

def Surnames(Type):
	Surnames = [""]
	return Surnames

def Phonotactic(Type):
	prefx  = [""]
	fix = [""]
	sufx  = [""]

	prefx += [
		"Av","Afr",
		"But", "Blam", "Brew",
		"Chir", "Can", "Crit", "Cel",
		"Droy", "Dev",
		"El",
		"Frup", "Fil", "Fur",
		"Graes", "Gil", "Gal",
		"Julk",
		"Kraid", "Kum",
		"Lo",
		"Mox",
		"Ninf",
		"Pumb", "Praon", "Pol",
		"Quej",
		"Run",
		"Sip", "Sat", "Soh", "Set", "Sek", "Sep", "Sec", "Sol",
		"Trauf", "Tij",
		"Voz",
		"Wrol",
		"Xen",
		"Zun",
		]
	if  "Kitsune" in Type:
		prefx = ["Fux",	"Volp",	"Tilk",	"Rav",	"Nar",	"Vurp",	"Lom",	"Alop",	"Lis",	"Resut",	"Rapos",	"Lis",	"Rob",	"Rev",	"Un",	"Pok",	"Rev",	"Y",	"Tulk",	"Nar",	"Kits",	"Sionn",	"Ref",	"Rok",	"Lomr",	"Shu",	"Ren",	"Alop",	"Alep",	"Fuch",	"Rapos",	"Rus",	"Ren",	"Vos",	"Lisk",	"Vulp", "Fox", "Zor",	"Laps",	"Vilt",	"Vorp", "Vos", "Lap", "Golp", "Omus", "Kibw", "Fus", "Lis", "Mos", "Lom", "Rub", "Zael","Dhak", "Hul", "Volp",	]

	fix += ['ar','e','il','o','a',
				  "an", "et", "ik", "os", "ur",
				  "al", "em", "ad", "ig", "ab",
				  "oz", "av", "ux",
				  "each", "ejet", "ehis", "epoh", "eguh",
				  "inag", "icek", "ipof", "ihur",
				  "otah", "oset", "osik", "osup", "onot",
				  "unad", "umep", "ucit", "ulot",
				  "id","er","in","odis","eph"]
	sufx += ["us","a","ant", "ia", ""]

	return prefx, fix, sufx

def Surphonotactic(Type):
	prefx  = [""]
	fix = [""]
	sufx  = [""]
	return prefx, fix, sufx
