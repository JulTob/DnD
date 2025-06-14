def Names(Type):
	MALE    = "He"    in Type
	FEMALE  = "She"   in Type
	AGENDER = "They"  in Type

	SUBTYPE = "Subtype" in Type
	GITH = "Gith" in Type
	SHAPER = "Shapeshifters" in Type


	Names = [
	'Nemesis',
		'Darinxan',
		'Balea',
		'Xioleg'
		'Hexir',
		"Olinaon",
		"Iripirocon",
		"Aberrant",
		"Alke",
		'Voxiraex',
		"Relhitur",
		"Mienalline",
		"Sulfikon",
		'Darkirox',
		'Oblivrion',
		'Inalin',
				"Echen",
				"Exen",
				"Raxozot",
				"Uthigol",
				'Amrou',
				'Uroy',
				'Chuka',
				"Storm",
				"Narlazotep",
				"Dagon",
				"Gith",
				"Mindwarp",
				"Shoggoth",
				"Xilix",
				"Zothommog",
				"Tsochar",
				"Beholster",
				"Nehthalggu",
				"Yogsothoth",
				"Abol",
				"Vorvadoss",
				"Carcosa",
				"Sathogua",
				"Wondertainment",
				"Scarleting",
				"Voidwalker",
				"Whisperwraith",
				"Eclipserpent",
				"Miragestalker",
				"Oblivion",
				"Seeker",
				"Inspir",
				"Entiti",
				"Drawn",
				"Embody",
				"Nothingness",
				"Phantom",
				"Limn",
				"Inspiry",
				"Creature",
				"Existon",
				"Edge",
				"Reality",
				"Aetherborn",
				"Creaturade",
				"Connecto",
				"Theether",
				"Dreamweaver",
				"Entithat",
				"Manipulrem",
				"Nexus",
				"Shade",
				"Originan",
				"Espirby",
				"Creatat",
				"Dwellinor",
				"Guardimen",
				"Sional",
				"Crossads",
				"Chronight",
				"Orig",
				"Inalin",
				"Espire",
				"Dyenti",
				"Tieswi",
				"Control",
				"Over",
				"Zime",
				"Fathomless",
				"Inspir",
				"Edby",
				"Deepsea",
				"Secapus",
				"Andex",
				"Lovecraft",
				"Ianhor",
				"Ror",
				"Terrorade",
				"Origen",
				"Inalin",
				"Sepired",
				"Bicreat",
				"Ures",
				"Zat",
				"Embod",
				"Yazfear",
				"Voideart",
				"Inspir",
				"Edyent",
				"Iteswit",
				"Avoidor",
				"Absence",
				"Atheir",
				"Core",
				"Eldritorn",
				"Insireby",
				"Theover",
				"Alteme",
				"Ofosmic",
				"Horror",
				"Nether",
				"Scribe",
				"Creat",
				"Urestha",
				"Trecord",
				"Forbidden",
				"Konuled",
				"Abyssecho",
				"Resonate",
				"Fromze",
				"Abyss",
				"Warpeaver",
				"Inby",
				"Entithat",
				"Cananip",
				"Ulepace",
				"Silenterald",
				"Pireden",
				"Tithat",
				"Precede",
				"Catastrophe",
				"Withomak",
				"Kingas",
				"Zound",
				"Cognitohazard",
				"Sicipes",
				"Tataf",
				"Feknow",
				"Ledgan",
				"Undertank",
				"Memetic",
				"Phantom",
				"Propagater",
				"Trinfor",
				"Mation",
				"Anomaly",
				"Nexus",
				"Centers",
				"Sactivit",
				"Ralit",
				"Relit",
				"Fracture",
				"Breakor",
				"Altereal",
				]

	if GITH:
		Names += [
			'Lorkan',
			"Vlaakith",
			"Laezel",
			'Xirauzar',
			]
	if  SHAPER:
		Names += [
		'Sakashima',
		"Tsukuyomi",
		]

	return Names

def Surnames(Type):
	Surnames = [""]
	return Surnames

def Phonotactic(Type):
	GITH = "Gith" in Type

	onset  = [  "Xirk", 'Chuk', "Zar",  "Gul",  "Zor",
		"Kar",  "Nix",  "Voxr", 'Hel',  "Hidr", "Helx",
		"Mord", "Quex", "Ral",  "Sil",  "Dark", "Ol",
		"Veth", "Viz",  "Cur",  'Lith', "Berx", 'Bor',
		'Uy',   "Yabl", 'Carb', 'Nitr', 'Ox',   'Fluor',
		'Ne',   'Sod',  'Magn', 'Alum', 'Sil',  'Fosf',
		'Sulf', 'Chol', 'Arg',  'Aurg',
				]
	nuclei = [
		'al',   'ezi',  "ith",  "om",   "uz",   'y',
		"aeth", "ein",  'ir',   "ogen", "ugr",  '',
		"ai",   'ez',   "iek",  "oot",  "uag",  '',
		"az",   "eo",   'i',    "or",   "uhl",  '',
		"aqui", 'es',   "io",   'orus', "umn",  '',
		"a",    'esi',  'in',   'og',   "uzt",  '',
		"aux",          'ini',  'or',
		"auz",          'ic',   'orin',
		"auj",          'ic',
		"auk",          'ig',
		"Auch",         'inx',
						'ili',
						'i',
				]
	codas  = [
		"ax",   'e',    "icon", "ox",   "un",   "l",
		"as",   'ew',   "iz",   "on",   'um',
		"ar",   "es",           "on",   "ur",
		"ar",   'eh',           "ot",   'um',
		"a",    "en",           "on",   'us',
				]

	if  GITH:
			onset += ['Lar','Gi','Xi']
			nuclei += ['eth','','az','uz',]
			codas += ['','','ar',]

	return onset, nuclei, codas

def Surphonotactic(Type):
	onset  = [""]
	nuclei = [""]
	codas  = [""]
	return onset, nuclei, codas
