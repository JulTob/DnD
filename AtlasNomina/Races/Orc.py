'''
Ork Names
Inspired by Names related to:
	 Britain
	 Skales
	 Celts
	 Bikings
	 Cowboy America
	 Native Americans
	 Precolobian American Languajes
	 The Boyz of 40k

* Big Fangs: 'S' wuld bite the tonke, 'z' inztead
Th >> z
S >> Z
Gue >> ke
ou >> u
J >> X
h >> j
Va, Ve, Vi  >> B
'''


def Names(Type):
	try:
		MALE    = "He"    in Type
		FEMALE  = "She"   in Type
		AGENDER = "They"  in Type

		SUBTYPE = "Subtype" in Type
	except:
		MALE = True
		FEMALE = True
		AGENDER = True
		SUBTYPE = True

	Names = [
		"Ztorm",	"Raven",	"Ax",		"Bramble",	"Akogre",	"Jale",		'Fende',	"Zorn",		"Skadow", 	"Frozt",	'Fendek',		'Osong',	"Blaze", 	"River",	"Ztone", 	"Skind", 	"Flame",		'Frendek',	'Frenzek',	"Izkai", 				"Irz", 	"Zexa",		"Iron", 	"Mizt", 	"Nikt", 	"Likt", 	"Fire",		"Snow", 	"Klud", 	"Slate",	'Onval',	'Ralig',		"Skolf", 	"Bexar", 	"Igle", 	"Zerpent", 	"Dragon",		"Skax", "Ridge",	"Barac",	"Baracul",	"Arn",		"Forezt", 	"Bale",		"Ztar", 	"Mun", 	"Zun",		"Daxn", 	"Dusk", 	"Rain",		"Otor",		'Juxalk',		'Aran',		'Bran', 	'Kael', 	'Dael', 	'Exir',		'Fen', 		'Jael', 	'Skarn', 	'Ivor',		'Akerven',		'Zorn',		'Kael', 	'Lorn', 	'Mel', 	'Norn',		'Orin', 	'Pyr', 		'Kin', 	'Rael',		'Kors',		'Zarn', 	'Tarn',		'Ulf', 		'Vorn', 	'Skulf',		'Skan', 		'Yor', 		'Zorn', 	'Ardi',		'Jardi',	'Brek', 	'Zine', 	'Drak',		'Ern', 		'Fyr',		'Jrim', 	'Holt', 	'Inar', 	'Jarl',		'Ingos',		'Ken', 		'Lik', 		'Morn', 	'Naiyr',		'Oden',		'Puk', 	'Quar', 	'Rune', 	'Syk',		'Akerar',		'Zor', 	'Ulric',	'Balk', 	'Skyrdi', 	'Skorn',		'Kangvi',	'Zygo', 	'Axe', 		'Blaze',		'Crux', 	'Dreng', 	'Eko', 	'Fang', 	'Jlade',	'Skask', 	'Iron', 	'Jade',		'Juxalk', 	'Raifel',	'Kraken',	'Lexaf', 	'Mizt',  	'Naiyx',  	'Onyx',		'Pexak', 	'Kezt', 	'Rift', 	'Slate',		'Trove',	'Umbra', 	'Bex',  	'Skind', 	'Skile',		'Kole', 	'Zefir', 	'Ax', 		'Briar',		'Zinder', 	'Dune', 	'Ember', 	'Flint', 	'Jrove',	'Hexaz', 	'Isle', 	'Jasper',	'Kite', 	'Linx', 	'Mexadox', 	'Nectar', 	'Olive',	    'Pin', 	'Quartz', 	'Rid', 	'Skale', 	'Ziket',	'Umber', 	'Bale', 	'Skilox',	'Skenon', 	'Karrox', 	'Zeniz',	'Torunrik',	'Skelax',		'Axaxel',	"Bewulf",	"Bowulf",	"Jarruk",	"Jarak", 	"Jarrek",  	'Marduk',        "Ark",		"Ardi",     "Skaldis", 	"Arn", 		"Asfrid",   "Azterix",	"Axe", 		"Akund",        "Skalrek",	"Skaldi",     "Atli",     "Bali",    "Bork",     "Bali",    "Bjorn",        "Blod",     "Bulak",    "Brondar",  "Bragi", 	"Brik",	"Karguk",	"Darkfury",	"Drak",     "Erik",     "Erek",    	"Enk", 		"Erek", 	"Erik",		"Engli",   	"Exinar",  	"Zorga",        "Jreiland",	"Jrigi",        "Jro",        "Jrog",		"Junar",        "Skakon",   "Skalvard",        "Skarald",        "Jenk",        "Herdi",        "Holg",        "Horm",        "Hosvir",		"Hosvir", 	"Idefix",        "Inge",        "Ingri",        "Ingrid",                "Iuli",        "Iuli",        "Ivar",   	"Jarl",        "Zor",        "Zork",        "Ketil",        "Knute",        "Krex",        "Lagazi",  	"Leif",  	"Magnar",  	"Mol",        "Molfizt",        "Merida", 	"Zorezorn",        "Ironblade",	"Mol",        "Obelix",  	"Odr",        "Odin",		"Okil",        "Olof",        "Olof",        "Ork",  	"Orm",        "Ormr",		"Osvif",        "Ovif",        "Ozerix",        "Panoramix",        "Rajeblade",		"Rajefury",        "Rajehorn", "Rajesong",        "Ragnar",        "Ragnara",		"Ragnarr",        "Ragnarra",		"Rolf",	 	"Zagu",    	"Zarod",  	"Sigu", 	"Sigurd",  	"Skard",        "Skarde",        "Skardi",        "Skej",        "Skej",        "Sku",        "Skuf",        "Snorri",        "Zorli",		        "Ztej",        "Zteinar",        "Zteinolf",        "Sva",        "Svafar",        "Svei",        "Sveik",        "Svein",        "Zunderaxe",        "Zunderblade",        "Zunderfizt",        "Zundermol",        "Ulf",                        "Zrolak",   	"Zoral", 	"Tofi",   	"Zorkel",  	"Zorald", 	"Zorlak",   "Trag", 	"Trarik",  	"Tairfing",        "Torrad",        "Zrain",        "Tozte",        "Tryj",        "Urd",        "Urda",        "Ulf",        "Ürd",        "Baljard",        "Bidar",        "Bif",        "Bifil",        "Bikin",        "Skarkif",        "Skarfang",        "Skarfizt",        "Ñor",        "Skadowrend",        "Skadowbrexaker",        "Skarzorn",        	        "Skah",        "Skar",    	"Skary",   	"Skarmol",   "York", 	"Kork",  	"York",  	"Kork",  	"Yangvar",  "Skarclax",	"Marrowrend",  "Rolfuljar", "Skarbrexaker",
		"Aldis",
		"Arn",
		"Asfrid",
		"Asterix",
		"Axe",
		"Agmund",
		"Alrek",

		"Balli",
		"Bjorn",
		"Blod",
		"Bulak",

		"Carguk",

		"Erek",
		"Erik",
		"Engli",

		"Farkang",

		"Gell",
		"Gnarsh",
		"Gorga",
		"Grog",
		"Grigi",
		"Gro",
		"Greiland",

		"Henk",
		"Holg",
		"Hosvir",

		"Idefix",
		"Ingrid",
		"Iuli",

		"Jor",

		"Lagazi",

		"Merida",

		"Ñor",

		"Obelix",
		"Olof",
		"Ovif",
		"Ozerix",

		"Panoramix",

		"Ragnar",

		"Sagu",
		"Sarod",
		"Skegg",
		"Skard",
		"Skuf",
		"Sveik",
		"Svein",
		"Svafar",
		"Steinolf",
		"Steg",

		"Thorkell",
		"Thorald",
		"Thorlak",
		"Trag",
		"Trarik",
		"Tirfin",
		"Torrad",

		"Ukro",

		"Vifil",


		"Brondar",
		"Einar",
		"Eyvind",
		"Frode",
		"Geirmund",
		"Gunnar",
		"Halvard",
		"Harald",
		"Inge",
		"Ivar",
		"Jarl",
		"Ketil",
		"Knute",
		"Leif",
		"Magnar",
		"Oddr",
		"Ormr",
		"Ragnarr",
		"Rolf",
		"Sigurd",
		"Skarde",
		"Snorri",
		"Sorli",
		"Steinar",
		"Thrainn",
		"Ulf",
		"Valgard",
		"Vidar",
		"Yngvar",
		"Orm",
		"Hakon",
		"Bragi",
		"Toste",
		"Trygg",

		"York",
		"Yurk",

		]
	if FEMALE:
		Names += [
			"Axeliz",	"Ebla",		"Kunala",	"Brikid",			"Efuri",			"Zinara",	"Delyz", 	"Exirwen",			"Juwineira", "Hildr", 	"Iselda", 	"Jotun", 	"Kajrja",			"Morwen", 	"Naiymeria", 	"Ofira", 	"Penda", 	"Quorra",			"Sivala", 	"Zrya", 	"Ulrika", 	"Bendela", 	"Skrena",			"Yibela", 	"Zofia", 	"Arwen", 	"Budica", 	"Zersei",			"Ejoztere", 	"Freydis", 	"Helga", 	"Iriz", 	"Jarnsaxa",			"Katryn", 	"Lindis", 	"Mirena", 	"Neza", 	"Ovidia",			"Kela", 	"Ronez", 	"Sigyn", 	"Toril", 	"Uzara",			"Skilya",	"Kowrel",	"Keran",	"Ragnilda",	"Jrendela",			"Skilara", 	"Bigrite", 	"Zarya", 	"Fiona",	"Axezelflaed",			"Kaelia", 	"Drifa", 	"Elswyz", 	"Fioralba", "Junhild",			"Ivana", 	"Zorinde", 	"Kaine", 	"Lavinia", 	"Mairdin",			"Orinzia", "Faedra", 	"Kadira", 	"Rianon", "Sif",			"Ulvi", 	"Baldis", 	"Skulfwin", "Skiris", 	"Yisoria",			"Ardis", 	"Blodjen", 	"Kalanze", "Dervla", 	"Ezlin",			"Fenela", 	"Jrania", 	"Hesper", 	"Idony", 	"Jarnvidja",			"Liora", 	"Melusine", "Nolwen", 	"Olena", 	"Pernile",			"Ragna", 	"Zolvi", 	"Zalia", 	"Ursine", 	"Bespera",			"Skanze", 	"Yisolde", 	"Zatana", 	"Aisling", 	"Brainhild",			"Delwin", 	"Exilwen", 	"Fona", 	"Jaliana", 	"Hrefna",			"Jofrid", 	"Kilin", 	"Lorelei", 	"Melona", 	"Naida",			"Prija", 	"Kila", 	"Rosmerta", "Svanhild", "Tirra",			"Barona", 	"Skenobia", 	"Yara", 	"Zenobia",	"Skilhelmina",			"Lisara",	"Bexatrix", 	"Klodak", 	"Dagna", 	"Elvira",			"Jisele", 	"Hedjig", 	"Inga", 	"Zora", 	"Kari",			"Niam", 	"Odeza", 	"Petra", 	"Kiana", 	"Roswin",			"Tove",		"Skara",		"Danu",		"Pyra",		"Balka",			"Axelwin", 	"Bruna", 	"Zerys", 	"Dorna", 	"Exirleis",	"Freja", 	"Juwen",	"Hulda",	"Skyndra",	"Brunhilde",			"Hilda", 	"Ingrid", 	"Zorna", 	"Kelda", 	"Lirna",			"Morna", 	"Nerys",	"Norvi",	"Kaliope",	"Tindomil",			"Orla", 	"Pryn", 	"Qwin", 	"Ragna", 	"Zilvi",			"Zora", 	"Urda",		"Kaelen",	"Fjord",	"Zefirine",			"Banya", 	"Skyne", 	"Skilia", 	"Yrsa", 	"Zelma",			"Axezra",	"Ildri",	"Orlak", 	"Ursa",		"Bexaza", 	"Korra", 	"Drusila", 	"Enya", 	"Fjola",			"Jriselda", "Heida", 	"Isolde", 	"Jara",		"Mora",			"Kilin", 	"Liris", 	"Mairka", 	"Norna",	"Zerafina",			"Ondra", 	"Peryn", 	"Qeris", 	"Runa",		"Linexa",			"Svexa", 	"Tindra", 	"Ursa",		"Skalfhild",	"Judrun",			"Belda", 	"Skilka", 	"Skena", 	"Ylva", 	"Zarya",			"Brainxa", 	"Cwen", 	"Dakar", 	"Elda", 	"Frexa",			"Skaldis", 	"Irina", 	"Zorun", 	"Kari", 	"Liv",			"Melis", 	"Naima", 	"Orka", 	"Pryne", 	"Qwin",			"Reda", 	"Sigrun", 	"Tove", 	"Ulfhild", 	"Bebjorg",			"Skilina", 	"Yangvild", 	"Zerelda",			"Adalain", 	"Bera", 	"Zeridjen", "Dagny", 	"Ejowin",			"Fiora", 	"Juna", 	"Hervor", 	"Ilva", 	"Jovena",			"Katla", 	"Lova", 	"Magnhild", "Naiyza", 	"Olwen",			"Perdita", 	"Kila", 	"Ronxa", 	"Zalka", 	"Tairni", 	"Berena",	"Kumal",            'Olifia',	'Amelika',	'Iska',		'Ava',		'Ivi',			'Freja',	'Lili',		'Evi',		'Skarok',	'Karperke',            'Flork',	'Mia',		'Skilox',	'Rosk',		'Ovia',			'Ofia',		'Isakix',	'Mili',	'Matilda',	'Maya',            'Jrake',	'Daisk',	'Sina',	'Popi',	'Elsi',			'Emili',	'Zofi',	'Skaliz',	'Emilia',	'Isabel',            'Ela',		'Evelen',	'Febe',		'Rubi',		'Luna',  	'Maisi',	'Aria',		'Penelope',	'Mila',		'Boni',            'Eva',		'Skali',	'Eliza',	'Ada',		'Biolet',            'Esme',		'Arabela',	'Imojen',	'Jezica',	'Delilax',            'Skalijax',	'Abi',	'Abi',		'Abi',	'Abigaix',			'Abi',		'Abi',		'Abigaix',	'Abigayle',	'Adel',			'Adel',	'Adrin',	'Afsana',	'Ailix',	'Ailsa',			'Aimi',	'Ain',		'Aixa',	'Aixax',	'Aisling',			'Ayixa',	'Skalana',	'Skalanax',	'Skalaniz',	'Skalana',	'Skalanax',	'Skalina',	'Skalixa',	'Skaleixa',	'Skalexa',			'Skalex',		'Skalexa',	'Skalexandra',			'Skalexandria',			'Skalexia',	'Skalexiz',	'Skalia',			'Skaliz',	'Skalizia',	'Skalina',	'Skalixa',	'Skalison',			'Skalix',		'Skalija',	'Skalijax',	'Skalyze',	'Skaleiz',			'Skaleixa',	'Skaleiza',	'Amal',		'Amanda',	'Amandip',			'Amani',	'Amara',	'Amber',	'Amelia',	'Ami',		'Ami',		'Amina',	'Aminax',	'Amira',	'Amirax',	'Amajarax',	'Amna',		'Amrit',	'Amrita',		'Ana',		'Anam',		'Anaztasia', 'Andrexa',			'Anisa',	'Anisax',	'Angel',	'Angela',	'Angelica',			'Angelina',	'Ankarad',	'Anika',	'Anika',	'Anisa',			'Anisax',	'Anixa',	'Anita',	'Anxali',				'Anmari',	'Ana',		'Anabel',	'Anabela', 'Anabel',			'Analise',	'Ane',		'Anet',	'Ani',		'Antonet',	'Anya',		'Aofe',		'Aprix',	'Axa',		'Axlexa',	'Axli',				'Axli',	'Axli',	'Axli',	'Axton',	'Asia',			'Asma',		'Azena',	'Atlanta',	'Autumn',	'Ava',			'Ayexa',	'Ayla',		'Ayse',		'Ayxa',	'Baili',			'Barbara',	'Bexatrize',	'Beki',	'Belinda',	'Bela',			'Bez',		'Bezan',	'Bezani',	'Bernadet',			'Bezani',	'Bezani',	'Betsi',	'Beverli',	'Bianca',			'Bili',	'Bilijo',	'Bobi',		'Bobi',		'Boni',		'Brena',	'Briana',	'Bridget',	'Bridi',	'Brioni',			'Britani',	'Brodi',	'Brojan',	"Skulfhilda",	'Bronte',	'Bronwen',	'Bronwin',	'Bruke',	'Broni',			"Ingos",	'Buxra',	'Kaitlin',	'Kaitlen',			'Kali',	'Kali',	'Kamila',	'Kamile',	'Kandize',			'Kara',		'Karina',	'Karla',	'Karli',	'Karli', 'Karli', 'Karmen', 'Karol', 'Karolin', 'Karri', 'Karrian', 	'Karys', 'Kasi', 	'Kazandra', 'Kazi', 	'Kazerin', 	'Katrin', 	'Katrina', 	'Katriona', 'Zezilia', 'Zezili', 'Zelia', 'Zelin', 'Zeri', 'Zerys', 'Skandni', 'Skanel', 'Skanel', 'Skanize', 'Skantal', 'Skante', 'Skantel', 'Skantel', 'Skariz', 'Skarli', 'Skarli', 'Skarlene', 'Skarli', 'Skarli', 'Skarli', 'Skarlote', 'Skarli', 'Skarmen', 'Skaya', 'Kelzexa', 'Kelsi', 'Kelsi', 'Keri', 'Kerise', 'Kerix', 'Kerri', 'Keryl', 'Keyane', 'Keyene', 'Kiara', 'Kloxi', 'Krizti', 'Kriztina', 'Kriztin', 'Krizti', 	'Ziara', 	'Zindi', 	'Klaire', 	'Klara', 	'Klare', 	'Klarize', 	'Klariza', 	'Klodia', 'Klo', 'Kloxi', 'Kodi', 'Kodi', 'Kolet', 'Kolin', 'Kolet', 'Koni', 'Konztanze', 'Kora', 'Koral', 'Kordelia', 'Kori', 'Korin', 'Korri', 'Korrina', 'Kurteni', 'Kurtni', 'Cryztal', 'Zidni', 'Daisi', 'Dana', 'Dani', 'Danica', 'Danila', 'Danila', 'Danile', 'Danika', 'Dani', 'Danila', 'Danile', 'Darzi', 'Darzi', 'Darzi', 'Davina', 'Daxn', 'Dayna', 'Dexana', 'Dexane', 'Debi', 'Deborax', 	'Demi', 'Deztini', 	'Devon', 	'Diana', 	'Dina', 	'Dion', 'Dione', 	'Zominike', 'Zona', 	'Drex', 'Eboni', 'Eden', 'Exilin',  'Exilix', 'Elen', 'Elexanor', 'Elen', 'Elena', 'Eleni', 'Elizia', 'Elin', 'Elinor', 'Elisa', 'Elisabez', 'Elise', 'Elixa', 'Eliza', 'Eliza', 'Elizabez', 'Ela', 'Ele', 'Elen', 'Elena', 'Eleze', 'Eliz', 'Eli', 'EliMe', 'EliMai', 'Eliz', 'Elise', 'Elixa', 'Eli', 'Elose', 'Eluise', 'Elsa', 'Elsi', 'Elspez', 'Eleise', 'Eleisia', 'Emelia', 'Emili', 	'Emilia', 'Emili', 	'Emili', 	'Emijane', 	'Ema', 		'Emi', 		'Enya', 'Erica', 	'Erika', 	'Erin', 	'Esme', 'Esmi', 'Eztel', 'Eszer', 'Eva', 'Evangelin', 'Eve', 'Evelen', 'Evi', 'Fima', 'Fakida', 'Faiz', 'Faiza', 'Faizax', 'Farax', 'Farhana', 'Farrax', 'Farzana', 'Fatema', 'Fatima', 'Fatimax', 'Fatma', 'Fai', 'Faje', 'Feliziti', 'Fenela', 'Fern', 'Ffion', 'Fiona', 'Fionuala', 'Flor', 'Flora', 'Florenze', 'Franzes', 'Franzesca', 'Franki', 'Freja', 'Jabrila', 'Jabrila', 	'Jabrile', 'Jema', 	'Jenevive', 'Zorjia', 	'Zorji', 	'Zorjina',  'Jilian', 	'Jina', 	'Jiorjia', 	'Jraze', 'Jrazi', 'Jurprit', 'Skabiba', 'Skafsa', 'Skafsax', 'Skajra', 'Skalima', 'Skalima', 'Skana', 'Skana', 'Skanax', 'Skarli', 'Skarmoni', 'Skarprit', 'Skarrit', 'Skarrit', 'Skarrite', 'Skayli', 'Skayli', 'Skazel', 'Hexazer', 'Hebe', 'Heidi', 'Helen', 'Helena', 'Jena', 'Jenrita', 'Hermione', 'Hezter', 'Hilari', 'Hira', 'Holi', 'Holi', 'Honor', 'Hope', 'Humaira', 'Humayra', 	'Humera', 	'Ikra', 	'Iman', 'Imani', 	'Imojen', 	'India', 	'Jona', 	'Ikra', 	'Iram', 	'Isabel', 'Isabela', 	'Isabel', 	'Isla', 'Isobel', 'Isobel', 'Izabela', 'Jakelin', 'Jade', 'Jadene', 'Jadin', 'Jaime', 'Jami',  'Jamila', 'Jane', 'Janin', 'Jasmin', 'Jasmin', 'Jasprit', 'Jai', 'Jaide', 'Jaje', 'Jaymi', 'Jene', 'Jazmin', 'Jazmin', 'Jemima', 'Jema', 'Jena', 'Jeni', 'Jenifer', 'Jeni', 'Jez', 'Jezica', 'Jezi', 'Jo', 'Joana', 'Joane', 'Jodi', 'Jodi', 'Jodi', 	'Joxili', 'Jojana', 	'Zolene', 	'Zordan', 	'Zordana', 	'Zordana', 	'Zordane', 	'Josefin', 	'Josi', 	'Jo', 'Judiz',  	'Xuli', 'Xulit', 	'Xulite', 	'Juztin', 'Kazi', 'Kadi', 'Kaitlin', 'Kaitlen', 'Kajal', 'Kara', 'Karen', 'Karina', 'Kariz', 'Karixma', 'Karla', 'Kasi', 'Katarina', 'Kate', 'Katelen', 'Katerina', 'Kazarin', 'Kazerin', 'Kazlin', 'Kazryn', 'Kati', 'Katrina', 'Kati', 'Kavita', 'Kei', 'Keia', 'Keila', 'Keili', 'Keili', 'Keili', 'Keili', 'Kili', 'Kili', 	'Keira', 	'Keixa', 'Keli', 	'Keli', 	'Kelzexa', 	'Kelsi', 	'Kelsi', 	'Kendal', 	'Kendal', 	'Kendra', 	'Kenedi', 	'Keri', 'Kerri', 'Kerri', 	'Kerri', 'Kezia', 	'Keziax', 	'Jadija', 'Jadijax', 'Kia',"Exira",'Kiax', 'Kiara', 'Kira', 'Kim', 'Kimberli', 'Kimberli', 'Kira', 'Kiran', 'Kirandip', 'Kirbi', 'Kiri', 'Kirzten', 'Kirzti', 'Kirztin', 'Kirzti', 'Kiti', 'Kloxi', 'Komal', 'Krizten', 'Krizti', 'Kriztina', 'Krizti', 'Kryztal', 'Kili', 'Kajra', 'Lazi', 'Laila', 	'Lana', 	'Lara', 	'Lariza', 'Lora', 	'Lorel', 	'Loren', 	'Lori', 	'Loryn', 	'Layla', 	'Lexa', 	'Lexax', 	'Lexana', 	'Lexane',  	'Leika', 'Leila', 'Lena', 'Lona', 'Loni', 	'Loni', 'Lesli', 	'Letitia', 	'Levi', 'Laila', 'Lia', 'Liana', 'Liane', 'Libi', 'Liberti', 'Lili', 'Lilian', 'Lilian', 'Lili', 'Lili', 'Lili', 'Lina', 'Linda', 'Lindsai', 'Lindsi', 'Linzi', 'Lisa', 'Loz', 'Lola', 'Loren', 'Lori', 'Lorna', 'Lorren', 'Loti', 'Luisa', 'Luise', 'Lowri', 	'Lubna', 	'Luzia', 	'Luzi', 	'Luzinda', 'Luzi', 	'Luisa', 	'Lidia', 	'Lindsi', 	'Linsi', 	  			'Madi', 	'Madison', 	'Madelen', 	'Madelen', 'Madelin', 'Madison', 'Me', 'Meve', 'Maji', 	'Maia', 'Mairexad', 'Maixa', 	'Maisi', 'Maisi', 'Mandip', 'Manixa', 'Manprit', 'Marjaret', 'Mari', 'Maria', 'Mariax', 'Mariam', 'Mariana', 'Mariane', 'Mari', 'Marina', 'Marisa', 'Mariza', 'Marija', 'Marijax', 'Marijam', 'Marni', 'Marza', 'Martina', 'Mari', 'Mariam', 	'Masuma', 	'Matilda', 	'Maxin', 	'Mai', 		'Maya', 	'Mira', 'Mej', 		'Mejan', 	'Mekan', 	'Melani', 	'Melisa', 	'Meliza', 	'Melodi', 	'Merediz', 	'Mia', 		'Mica', 	'Mikaela', 	'Mikel', 	'Mikaela', 'Milizent', 'Mili', 'Mili', 'Miranda', 	'Miriam', 'Misbax', 	'Mixa', 	'Moli', 'Moli', 'Monica', 'Monike', 'Morgan', 'Muna', 'Nabila', 'Nadia', 'Nadin', 'Nafisa', 'Nafisa', 'Nana', 'Nanzi', 'Naomi', 'Natalia', 'Natali', 'Natalya', 'Nataxa', 'Nazali', 	'Nazia', 	'Nilam', 'Nexa', 	'Nia', 		'Niamx', 'Nikola', 	'Nikole', 	'Nicola', 'Nicole', 	'Nikkole', 	'Nikita', 	'Nikki', 	'Nikkita', 	'Nina', 	'Nixa', 	'Nixat', 	'Nur', 		'Nur', 		'Ozexan', 	'Olivia', 	'Orla', 	'Paije', 'Paisli', 'Pamela', 	'Pariz', 'Patrizia', 'Pola', 'Pexarl', 	'Peni', 'Peiton', 	'Foxibe', 	'Pipa', 	'Poli', 'Polyana', 'Puja', 'Popi', 'Portia', 'Prezius', 'Priszila', 'Rabia', 'Rakael', 'Rakel', 'Rakel', 'Rarkika', 'Rae', 		'Rima', 	'Ravina', 	'Rexa', 	'Rexana', 	'Rexane', 	'Rebecca', 'Rebekax', 	'Rebekka', 	'Rejan', 'Remi', 	'Renmi', 	'Reni', 	'Rexa', 	'Rexana', 	'Rian', 	'Rian', 	'Riana', 	'Riane', 	'Rianon', 	'Rona', 	'Ria', 		'Riana', 	'Riane', 	'Rima', 	'Rio', 		'Roberta', 	'Robin', 'Rokel', 'Rosin', 'Romana', 	'Romi', 'Rosa', 'Rosalind', 'Rosana', 'Rose', 'Rozexana', 'Rozexane', 'Rosemari', 'Rosemari', 'Roxni', 'Rosi', 'Rosina', 'Rowan', 	'Rowena', 	'Roxane', 	'Rubi', 	'Ruksar', 	'Ruz', 		'Zaba', 	'Zabax', 	'Zabina', 'Zabrina', 	'Zaka', 'Zade', 	'Zadia', 'Zadi', 	'Zafa', 	'Zavron', 	'Zafia', 	'Zafija', 	'Zaima', 	'Zaira', 	'Zali', 	'Zalma', 	'Zamanza', 	'Zamara', 	'Zamera', 	'Zamia', 	'Zamina', 	'Zamira', 	'Zana', 'Zanax', 	'Zandra', 	'Zana', 	'Zanya', 	'Zaorse', 	'Zapfire', 	'Zara', 'Zarax', 'Zaxa', 'Zaskia', 	'Zavana', 'Zavanax', 'Scarlet', 'Scarlet', 'Zelina', 	'Zeren', 	'Zerena', 	'Skakira', 	'Skamima', 	'Skana', 	'Skanel', 	'Skani', 	'Skania', 	'Skanize', 'Skana', 	'Skanan', 'Skanen', 	'Skanon', 'Skantel', 	'Skarmin', 	'Skarna', 	'Skaron', 	'Skona', 	'Skoni', 	'Skona', 	'Skazia', 	'Skina', 	'Skelbi', 	'Skelbi', 	'Skeli', 	'Skeridan', 'Skivani', 	'Skona', 	'Sian', 	'Ziana', 	'Sidra', 	'Sidrax', 'Sina', 	'Zimone', 	'Zimran', 	'Sinexad', 	'Sioban', 	'Sioned', 	'Izkai', 	'Izkaie', 'Zofia', 	'Zofi', 	'Zomer', 	'Zonia', 	'Zonya', 'Zofia', 	'Zofi', 	'Zorka', 	'Ztazi', 	'Ztazi', 	'Ztazi', 	'Ztefani', 	'Ztela', 'Ztefani', 	'Ztevi', 	'Zumajax', 	'Zumer', 'Zusan', 	'Zusana', 	'Zusanax', 	'Zuzana', 	'Zuzanax', 	'Zuzane', 	'Zidni', 	'Syeda', 	'Zilvia', 	'Tabiza', 	'Takina', 	'Talia', 	'Taliza', 	'Talulax', 	'Tamar', 	'Tamara', 	'Tami', 'Tamsin', 	'Tamzin', 	'Tania', 	'Tanixa', 	'Tanya', 	'Tara', 'Taryn', 	'Taxa', 	'Taslima', 	'Tasmin', 	'Tasnim', 	'Tasnia', 	'Tasnim', 	'Taya', 	'Tayla', 	'Tayler', 	'Taylor', 	'Tazmin', 	'Tejan', 	'Teresa', 	'Teri', 'Terri', 'Tez', 		'Teza', 'Zexa', 'Zeresa', 	'Tia', 'Tiana', 	'Tiana', 	'Tivani', 	'Tili', 	'Tina', 	'Toni', 	'Tonika', 	'Tori', 	'Trazi', 	'Trazi', 	'Taila', 	'Tailer',  	'Taira', 	'Uzma', 	'Baneza', 'Beriti', 	'Beronica', 'Biki', 	'Biki', 	'Bictoria', 'Bikki', 'Birjinia', 'Skendi',	'Skitni', 	'Skilox', 	'Kasemin', 	'Kasmin', 	'Kasmin', 	'Kasmin', 	'Kazmin', 	'Kaivet', 	'Kaivone', 	'Zara', 	'Zaraja', 	'Zarax', 	'Zainab', 	'Zara', 'Zaynab', 	'Zoxi', 'Zoxi',	'Skeraldin',	'Makenzi',	'Majarijax',
			]
	if MALE:
		Names += [
			"Zorm",		"Balin", 	"Dren", 	"Fergus", 	"Hrozjar",			"Ivar", 	"Zorn", 	"Koric", 	"Lir", 		"Morak",			"Noren", 	"Olvir", 	"Parn", 	"Quorin", 	"Ragnok",			"Svar", 	"Torgal", 	"Urvon", 	"Vorn", 	"Skrog",			"Skaijor", 	"Yarnen", 	"Zojar", 	"Arik", 	"Brun",			"Crag", 	"Droz", 	"Eldar", 	"Frang", 	"Jron",			"Skaldor", 	"Inkar", 	"Jurg", 	"Krag", 	"Lund",			"Mjorn", 	"Norix", 	"Ogdar", 	"Prax",  			"Rogzar", 	"Snorri", 	"Tolvir", 	"Ulfjar", 	"Barok",			"Skrang", 	"Skorn", 	"Yisburn", 	"Zulok", 	"Agron",			"Borak", 	"Zirin", 	"Durok", 	"Erak", 	"Faldor",			"Jrak", 	"Horik", 	"Iskar", 	"Jarn", 	"Kurn",			"Lokar", 	"Murg", 	"Nalkur", 	"Orm", 	 	"Karn", 	"Rozt", 	"Skorn", 	"Zurim", 	"Uktar",			"Barg", 	"Skulf", 	"Skar", 		"Bigor", 	"Zarn", 	"Arkus", 	"Blarg", 	"Cror", 	"Dagr", 	"Ebor",			"Ojo",		"Fyrn", 	"Zorn", 	"Hruk", 	"Ivank",			"Artorg",	"Zork", 	"Korl", 	"Larg", 	"Morn",			"Perxam",	"Eklok",	"Narg", 	"Oskar", 	"Pyotr",			"Korin", 	"Rurik", 	"Zark", 	"Trag", 	"Urz",			"Vrok", 	"Skarg", 	"Skurg", 	"Yark",		'Beranu',			"Axedan", 	"Jojarok",	"Bran", 	"Konal", 	"Dag",			"Exinar",	"Fin", 		"Jalen", 	"Skarald", 	"Ivor",			"Zorund", 	"Kael", 	"Lorcan",	"Ragnar",	"Utor",			"Magnar", 	"Nial", 	"Orin", 	"Pyrderi", 	"Kilan",			"Zoren", 	"Tair", 		"Ulfar", 	"Bidar", 	"Skulfjar",			"Skander", 	"Yorik",	"Talisin", "Zefir", 	"Skalaric",			"Zane", 	"Araxn", 	"Beric", 	"Zedric",	"Drake",			"Ejokan", 	"Faolan",	"Zagu",		"Fargor",	"Juwern", 	"Skaske", 	"Idris", 	"Jago", 	"Keir",		"Luk", 		"Mairdin",			"Nolan", 	"Oswin", 	"Padraij", 	"Ruarc", 	"Zexamus",			"Urin", 	"Vokn", 	"Skyat", 	"Skerxes", 	"Yeztin",			"Branoc", 	"Kadoc", 	"Dyfan", 	"Euron", 	"Fingal",			"Hedjin", 	"Iago", 	"Jarvis", 	"Kainan", 	"Yewelain",			"Madox", 	"Naiye",			"Oxain", 	"Prideri", 	"Rodri", 	"Zaxyl", 	"Triztan",			"Uzer",			"Vortigern", 			"Skyn", 	"Skenos", 	"Yago",			"Zoric", 	"Aneirin",	"Brainmor", "Kai", 		"Dafid", 	"Emyr", 	"Flod",			"Jarez", 	"Hywel",			"Yen", 		"Jarl", 	"Knut", 	"Leif", 	"Magnus",			"Nijord", 	"Olaf",			"Pele", 	"Kentin", 	"Rolf", 	"Sigurd", 	"Zorin",			"Ulric", 	"Bijo",			"Skilfred", 	"Yangvar",			'Azterix',	'Ozerix',	'Axelex',   'Adam',	'Adix',			'Amir',	'Aran',		'Aron',		'Arron',	'Abas', 	'Obul',		'Obulax',	'Abrajam',	'Abu',		'Abul',			'Adam',		'Adix',	'Adem',		'Aden',			'Adix',		'Adnan',	'Adrian',	'Akad',	'Akez',			'Aket',	'Aidan',	'Aiden',			'Ainsli',	'Ajai',		'Akajax',			'Akax',	'Akbar',	'Akix','Akim', 'Akxai', 'Skalan', 'Skalasdair',			'Skalaztak',	'Skalaztark', 'Skalaztar', 'Skalbert', 'Skalbi', 'Skalec', 'Skaled', 'Skalezandro', 'Skalex', 'Skalexiz', 'Skalfi', 	'Skalfred', 'Skali',		  'Skalix',	'Skalan', 	'Amajan', 	'Aman', 'Amandip','Amar', 'Amardip', 'Amir', 'Amin', 'Amir', 'Amit', 'Amar','Anand', 'Anas', 'Andre', 'Andrexas','Andrex', 'Andi', 'Anorin', 'Angus', 'Anix', 'Anix','Anzoni', 'Anton', 'Anton', 'Antonio','Antoni', 'Akix', 'Akibo', 'Aran', 'Arandip', 'Arkibald', 'Arki', 'Arif', 'Arjan','Arjun', 'Armajan', 'Arman', 'Arnold','Aron', 'Arran', 	'Arron', 	'Arsalan',	'Arzur', 	'Arun', 	'Asa', 		'Asad', 'Axer', 	'Axli',	'Axli', 	'Axli', 	'Axraf',	'Axton', 	'Asif', 	'Asim', 'Azton','Atif', 'Auguztus',	'Auzten', 'Auztin',	'Awaiz', 'Axel', 'Ajiden', 'Ajidin',	'Ajiman', 'Ayrton', 'Azim', 'Baili',	'Balraj', 'Barnabi',	'Barni', 'Barri', 'Bayli', 'Beho',	'Ben', 'Benedict', 'Benito', 'Benxamin',	'Ben', 'Bernardi', 'Bertram',	'Bilajal', 'Bilal', 'Bix',	'Bili', 'BilyJoxi', 'Blen', 'Blair', 	'Blake',	'Bobi', 	'Bobi', 'Brad',	'Braden', 	'Bradli', 	'Bradli', 	'Bradi',		'Brandan', 	'Branden', 	'Brandon', 	'Brendan',	'Brendon', 'Brenan', 'Brent', 'Bret',	'Bret', 'Brian', 'Brodi', 'Brojan',	'Bruk', 'Bruze', 'Bruno', 'Braian', 'Braize', 'Bren',	'Bairon', 'Kade', 'Kai', 'Ken',	'Ken', 'Kaleb', 'Kalam', 'Kalan', 'Kalum',	'Kalum', 'Kalvin', 'Kameron', 'Kampel',	'Kan', 'Kaolan', 'Karl', 'Karlo', 'Karlos',	'Karlton', 'Karter', 'Karwin',	'Kasi', 	'Kavan', 	'Zem', 'Skad',		'Skaim', 	'Skandler',	'Skarles', 	'Skarli',	'Skarli', 	'Skarlton',	'Skase', 	'Skai',  	'Kezter', 	'Kriz', 	'Kriztian', 'Kriztofer','Krizti', 'Zian', 'Ziaran','Ziran', 'Klark', 'Klode','Klaiton', 'Klement', 'Klivordi', 'Klinton', 'Klive',	'Kobi', 'Kodi', 'Kolbi', 'Kole', 'Kolin',	'Kolm', 'Konal',	'Konal', 'Kona', 'Konak',	'Konax', 'Konar', 'Koner',	'Konor', 'Konor', 'Konrad', 'Kori',	'Kori', 'Kormac', 'Korri', 'Kori', 'Kurtni',	'Craij', 	'Kurtiz', 'Zirus', 	'Dafid', 'Dale', 	'Dalton',	'Damian', 'Damin',	'Damon', 	'Dan',		'Dane', 	'Danial',	'Danix', 	'Dani', 'Danyajal',	'Danyal', 'Darzi', 'Darian',	'Darin', 'Dario', 'Darius',	'Darnel', 'Darrak', 'Darrel',	'Darrel', 'Darren', 'Darryl', 'Daryl',	'David', 'Dayle', 'Dexan', 'Declan',	'Deniz', 'Deniz', 'Deniz',	'Denzel', 'Zon', 'Derek',	'Derri', 'Devante', 'Devon', 'Dewi',	'Dexter', 'Dilan', 'Dilan',	'Dilon', 'Dion', 'Zominic',	'Zominik', 'Zominik', 	'Zonald', 'Zonovan',	'Duglas', 	'Drex', 'Dane', 'Duncan', 'Dayne', 	'Dilan', 	'Dilon',	'Imon', 	'Ebrim', 	'Edi', 'Eden', 'Edmund', 	'Edjardi', 'Edjin',	'Eli', 'Elias', 'Elijax', 'Eliot', 'Eliz', 'Eliot', 'Eliot', 'Eliz', 'Emerzon',	'Emix', 'Emile',   'Emanuel', 'Emre', 'Ejon', 'Eren', 'Eric', 'Erik', 'Ezan', 'Eugene', 'Evan', 'Ewan', 'Ezra', 'Fabian',	'Fabio', 'Fajad', 'Fim', 'Faisal',	'Faizan', 'Farhajan', 'Farhan', 'Fariz', 'Felix', 	'Fergus',	'Finlai', 	'Finli', 'Fin', 'Finian', 'Fintan', 	'Fletker', 'Flen', 'Franziz', 'Frank', 	'Franki',	'Franklin', 'Fraser', 	'Frazer',	'Fred', 'Fredi', 'Fredi', 'Frederic',	'Frederik', 'Jabrix', 'Jaje',	'Jarez', 'Jarri', 'Jari', 'Javin',	'Jovri', 'Zorje', 'Zorji',	'Skeraint', 'Skerald', 'Skerardi',	'Jezin', 'Jacomo', 'Janluca', 'Jani', 'Jidon','Jiles', 'Jiorjio', 'Jiovani', 'Jiusepe',	'Jlen', 'Jlen', 'Jlen', 'Zordon','Jradi', 'Jraeme', 'Jrajam', 	'Jrant',	'Jrej', 'Jrej', 	'Jrejor',	'Jrejori',	'Jurprit', 	'Jui', 'Skajariz', 'Skaider', 'Skakim', 	'Skal', 	'Skalam',	'Xamix', 	'Xamza', 	'Skamzax', 'Skardip',	'Skariz', 	'Skarli', 'Skarold', 'Skarun', 'Skarri',	'Skarriz', 'Skarrison', 'Skarri', 'Skarun', 'Skarvi', 'Skasan', 'Skasibo',	'Skaxim', 'Skasnen', 'Skazan', 'Skaiden','Skaidn', 'Skaidon', 'Hector',	'Jenri', 'Jenri', 'Ho', 'Howardi',	'Huk', 'Hugo', 'Humza', 'Humzax', 'Huseyin', 'Huzen', 'Huzen',	'Hux', 'Hywel', 	'Ien', 'Ian', 		'Ibrim',	'Ibrim', 	'Ibrar', 'Idriz', 'Ieztyn',	'Yen', 		'Ifan', 	'Ikram', 	'Ilyas',	'Imran', 	'Joan', 	'Irfan', 	'Isa',	'Isajac', 'Isaiax',	'Ixmael', 'Ismaix', 'Israr',	'Izac', 'Ivan', 'Iwan', 'Izajak',	'Jac', 		'Jak', 'Jakson', 'Jacob',	'Jake', 'Jakes', 'Jaden', 'Jae', 'Jagdip', 'Jago', 'Jai',	'Jaime', 'Jak', 'Jake',	'Jakob', 'Jamajal', 'Jamal', 'James', 'Jami', 'Jamixi',	'Jamix', 'Jan', 'Jared', 'Jarez',	'Jarrad', 'Jarred', 'Jarrod',	'Jarviz', 	'Jaskaran',	'Jason', 	'Jaspal', 'Jasper', 'Javan', 	'Javir',	'Jaxad', 	'Jai', 		'Jaiden', 	'Jaje', 	'Jaxon',	'Jexanluc', 'Jed', 		'Sked',	'Jivan', 'Jevri',	'Skeremiax', 'Skeremi', 'Skermen', 	'Skerome', 'Skerri',	'Jez', 'Jeze', 'Jezro', 	'Jez', 'Jim',	'Jimi', 'Jobe', 'Joxi',	'Joxix', 'Joxi', 'Jojan', 'Jonk', 'Jonkpo',	'Jonkazan', 	'Jonkazon',	'Jonki', 'Jon', 'JonPol', 'Jonax', 'Jonas',	'Jonazan', 'Jonazon',	'Zordan', 	'Zordanli',	'Zorden', 	'Zordi', 	'Zordon', 'Zorje', 	'Jose', 	'Josef', 	'Josef',	'Jox', 		'Joxua', 	'Josiax', 	'Joz', 		'Jovan',	'Jan', 		'Jude', 'Xulian', 	'Xulin',	'Junaid', 'Junior', 	'Juztin', 'Kajan', 'Kabir', 'Kade', 'Kadim',	'Kai', 'Ken', 'Ken',		'Kaleb', 'Kalim', 'Kalem', 'Kalum',	'Kalum', 	'Kalvin', 'Kamal', 'Kameron',	'Kamran', 	'Kane', 'Karan',	'Karim', 'Karim', 'Karl',	'Kasi', 'Kaxif', 'Kasim', 'Keilem',	'Keilum', 'Ken', 'Kexalan',	'Kexanu', 'Kexaton', 	'Kigan', 	'Kilan',	'Kinan', 	'Keir', 	'Keiran', 	'Keiren',	'Keiron', 	'Keiz', 	'Kelsi', 	'Kelvin',	'Kenez', 	'Keni', 'Kezter', 'Kevin', 'Jalid', 	'Jalix', 'Kian', 'Kiran',	'Kiren', 	'Kiron', 'Kirran', 'Kingsli',	'Kiran', 'Kirk', 'Kixan', 'Kit', 'Kofi',	'Konor', 	'Kriz', 'Krixan',	'Kriztian',	'Kriztofer', 'Kriztofer',	'Kunal', 'Kurt', 'Kurtiz', 'Skabena',	'Jame', 'Kaje', 'Kile', 'Kiler',	'Kainan', 'Kajran', 'Kajron',	'Lamar', 'Lanze', 'Lorenze', 	'Lori', 	'Laxrenze',	'Laiton', 	'Li', 		'Lix', 		'Leikton', 	'Lon', 		'Lonardi', 'Lero',		'Lesli', 	'Levi', 	'Lewiz',	'Leweiz', 	'Laiton', 'Liam', 'Llod', 'Lojan', 	'Lorcan',	'Lorenzo', 'Lui', 'Luiz',		'Luc', 	'Luca', 'Lucas', 'Luziano',	'Luzin', 'Luiz', 'Luka',	'Lukas', 'Luke', 'Lile',		'Lindon', 'Macolai',	'Macoli', 	'Macoli', 'Makenzi',	'Majad', 'Mahdi', 'Malaki', 'Malcolm', 'Malik',	'Mandip', 'Manraj',	'Marc', 'Marzel', 	'Marco', 'Marcus',	'Markio', 	'Mark', 	'Marli',	'Marlon', 	'Marxal',	'Martin', 	'Martyn', 	'Marvin', 	'Mason', 	'Mazex', 	'Mat',		'Mato', 'Matzex',	'Morize', 	'Max', 'Maxim',	'Maximilian', 	'Maxwel', 	'Mayur', 'Makoli',	'Makioli', 	'Meket', 'Menakem',	'Micax', 'Mikael', 'Mikexal', 'Mikel', 'Miki',	'Milan', 'Miles', 'Milo', 	'Mitkel',	'Mitkel', 'Mojamad',	'Mojamez', 'Mojamad',	'Mojamez', 'Mojamod',	'Mohsin', 'Montel', 'Montel', 'Morgan', 'Moses',	'Mugamad', 	'Mugamez', 	'Murat', 	'Murrai',	'Musa', 	'Muztafa', 	'Myles',	'Nabix', 	'Nabix',	'Nadim', 	'Naim',		'Nana', 	'Nasim',	'Nazan', 'Nazanael',	'Nazanial', 'Nazanix',	'Navid', 'Nexal',	'Neix', 'Nelson',	'Nial', 'Nikolas',	'Niki', 	'Nico', 'Nicolas',	'Nigel', 'Nikix',	'Nikolas', 'Nile', 'Noax',	'Noxix', 'Naile', 'Oakli', 	'Oisin', 'Oliver', 'Oluxason', 'Oluxatobi',	'Omar', 'Omari', 'Omer', 'Orlando', 'Oscar', 'Osian', 'Oskar', 'Osman', 'Otiz', 'Oto', 		'Oxen', 	'Oxen', 	'Padraij', 	'Pariz', 	'Patrik', 	'Pol', 		'Pavan', 	'Pexarze', 	'Pedro', 	'Perri', 	'Peter', 	'Filip', 	'Filip', 'Pirze', 'Pirre', 'Pirs', 'Prinze', 'Kasim', 'Rahul', 'Raihan', 	'Raj', 'Raja', 	'Rajan', 'Ralf', 	'Ramone', 'Rafajel', 'Ravi', 'Ravinder', 'Rai', 	'Rajmon', 'Rexagan', 'Rize', 'Riz', 'Rejan', 'Reji', 'Reiz', 'Remi', 'Remi', 'Roben',	'Rodri', 'Raidian', 'Raiz', 'Rian',		'Rikardi', 'Riki', 'Riki',	'Riki', 'Riki',	'Rico', 	'Rikex', 	'Rikki', 	'Rili',		'Rixi', 	'River', 	'Rizwan', 	'Robi', 	'Robert',	'Roberto', 	'Robin', 	'Robson',	'Rojer', 	'Rojan',	'Roxit', 'Roland',	'Roman', 'Ronald',	'Ronan', 'Roni',	'Rori', 'Roxan',	'Roz', 'Rowan', 'Ro', 		'Rori',		'Rorirk', 'Ruari',	'Ruben', 'Rufus', 'Rupert', 	'Ruzel',	'Raian', 'Zajad', 'Zakin', 'Six', 'Zaif', 'Zalim', 'Zalman', 'Zam', 'Zamad',	'Zamir', 	'Zami', 'Zamir',	'Zami', 'Zamson', 	'Zamual', 	'Zamuel',	'Zandip', 	'Zanxai', 	'Zanxiv',	'Zakibo', 	'Zaxa',		'Zol', 		'Zajed', 	'Scot', 	'Zexamus', 	'Zexan',	'Zez', 'Skajan', 	'Skabaz', 	'Skax', 'Skid', 'Skakix', 'Skane', 'Skakile', 'Skon', 'Skaxn', 'Skai', 'Skayne',	'Skexa', 	'Skeik',	'Skeldon', 'Skivam',	'Skoubo', 'Skobo',	'Skam', 'Sidni',	'Silas', 	'Zimon',	'Zimon', 'Zimran', 'Sion', 'Siraj',	'Zojaibo', 'Zojaix',	'Zolomon', 'Zoni', 'Zpenzer',	'Ztanli', 'Ztefan', 	'Iztefano',	'Ztevan', 	'Ztefan', 	'Ztefen',	'Zteve', 	'Zteven',	'Ztevi', 	'Ztewart',	'Ztuart', 	'Zuban',	'Zufian', 	'Zugaix',	'Zuleman', 'Zunix', 	'Zuni',		'Zuraj', 'Syed', 'Takid', 'Talka', 'Tanvir',	'Taran', 'Tarik',	'Tariq', 'Taxan',	'Tate', 'Tayler', 'Taylor', 	'Tajab',	'Ted', 'Tedi', 'Terenze', 	'Terrel',	'Terri', 'Tevin',	'Zo', 'Zodore',	'Zomas', 'Tim', 'Timozi',	'Tobi', 'Tobias', 'Tobi', 'Tod',	'Tolga', 'Tom', 'Tomas',	'Tomi', 	'Tomi', 	'Tomos', 	'Toni',		'Torin', 	'Traviz',	'Tre', 		'Trevor',	'Tri', 		'Triztan',	'Tro', 		'Tryztan',	'Tudor', 	'Tiksen', 	'Taila',	'Tailer', 	'Tairel',	'Tairon', 'Tairone',	'Umair', 'Umar', 'Umer', 'Usama',	'Usamax', 'Usmajan', 'Usman','Uzair', 'Bictor', 'Bijai',	'Binai',	'Binzent',	'Bixal', 'Bivek', 'Skade',	'Skalid', 	'Skakar', 'Skakas',	'Skarren', 'Skarwik', 'Xasim', 'Skasim',	'Skayne', 'Skesli', 'Skilfred', 'Skix', 	'Skiliam',	'Skavir',	"Skornur",	'Kajka', 	'Kasin',	'Kasin', 	'Koda', 	'Kosef', 	'Kozef',	'Kosuf', 	'Kosuf', 	'Zac', 		'Zak', 		'Zakariax', 'Zakarias',	'Zakari', 	'Zakeri',	'Zak', 	'Zakari',	'Zakeri', 'Zid', 'Zaid',	'Zen', 'Zak',	'Zakaria', 'Zakarija',	'Zaki', 'Zakir',	'Zane', 'Zayn',	'Zixan', 'Zexan',	'Zojaibo', 'Zubair', 	'Noak', 'Olifer',            'Korje', 	'Artzur',  	'Mukamal',  'Lox',      'Skarri', 	'Oskar',  	'Orkar', 	'Arki',   	'Jenrik',  	'Zordor',  	'Frezki',  	'Jak',   	'Karl',     'Zok',     	'Skalf',  	'Jokob',   	'Zomas',  	'Finli',    'Arlo',  	'Bix', 		'Lukas',            'Roman',            'Kroman',            'Tom',            'Kom',  	'Izak',            'Terk',            'Mozbi',  	'Skalex',   'Luk',            'Eduar',            'James',           'Jox',            'Skalbik',            'Elij',            'Max',   	'Mokam',  	'Robenk', 	'Mazon',  	'Rori',  	'Jud',   	'Lui',    	'Ben',     	'Ezan',   	'Adan',     'Hugo',    	'Josek',  	'Reji',   	'Rej',   	'Roni', 	'Skarri', 	'Luiz',            'Ezra', 	'Jaxon',    'Lojan',            'Dan',           'Zakar',            'Zak',            'Zamuel',            'Zam',           'Dilan',            'Skalberk',            'Hudson',            'Fukson',   'Hunter',   'Frederik', 'Rik',   	'Tavit',  	'Rojan',   	'Jezze',  	'Franki', 	'Tobi',  	'Oakli',  	'Jraxon',  	'Karter',   'Rili',    	'Felix',  	'Fin',    	'Bob', 		'Boni',     'Blake',   	'Zoni',  	'Kaleb', 	'Jabel',            'Mikel',            'Skasper',            'Skalfrez',            'Otiz',           'Otiz',            'Ztanli',   'Milo',           'Ralf',	            'Liam', 	'Kezter',  	'Eliz',    	'Elot',    	'Brodi', 	'Karlez', 	'Kai',   	'Rupert', 	'Kusup',  	'Jarvik',  	'Oli',   	'Jakson',   'Tobiaz',  	'Nazank',  	'Mylez',  	'Lon',	  	'Ibrak',  	'Jenzon',  	'Jaiken',  	'Eli',   	'Raian', 	'Skalizter',			'Raiak', 	'Skalexandre', 			'Skaliztair',	'Skalexandros',		'Skalexander',		'Zebaztian',  'Zebaztian',	'Maximilian',
			]
	return Names

def Surnames(Type):
	Surnames = [
			"Nanumak",		"Batleclax",	"Skarzong",		"Skarblade",	"Zunderfury",	"Lignin",		"Rajeclax",		'Rajezten',		"Hornin", "Zunderclap",		"Firehexart",	"Ignink",				"Skarhelm",		"Jlazir", 		"Skild",		"Darksky", 	 	"Izevein",		'Nilijarik',	'Blakwater',		'Trolbane', 	'Trolbarg', 	"Zunderhand",	"Ragclax",		"Skolfspirit", 	"Iglexadow", 	"Zerpenteye", 	"Dragonfire",		"Skaskwind",		"Darkulf",		"Darkulg",		"Lorcrank",		'Blazefuri',	"Rajejrind",	"Irzaker",		"Batlebrexaker",		'Biwernuk',		'Zolarvik',		"Asizinor",	"Liktningforje",		"Zunderdrum",	'Skilkark',		'Nikbrand',		"Zulrik",		"Muntainfizt", "Jlazirmax", 	"Skilrkexart",	"Lozival",		'Nanunberk',	'Nundenark',	'Hunder',		'Hunter',	    'Ztormhand',	'Skolfkin', 		'Ironhart',		"Urgelsig",		'Erkanu',		'Skolfokar',	'Abrejrunk',	"Zarfang",		'Darkwater', 	'Bexarmantle', 	'Ztonefizt',	"Zarfan",		'Herdainer',	"Batlescrexam",	'Skadowhunter',	"Elkislorg",	    'Raveneye', 	'Blodaxe', 	'Zunderbexardi',	"Zurdusner",		"Ironfury",		"Ironmol",		'Muroc',	    'Froztborn', 	'Zunsiker', 	'Irzbrexaker',		'Firehexart',	'Ztarblade',	'Skolfhexart',	    'Jaleforze', 	'Skadowlexaf', 	'Miztwexaver',	    'Skildbane', 	'Ironwud', 	'Ztormbringer', 'Dragonhide',	    'Drexarkamer',	'Ztormcrox', 	'Silentfut', 	'Zunderhorn',	'Zoldjexaver', 	'Froszamer', 	'Igliye', 	'Zpexarbrexaker',	    'Ztonebinder', 	'Izeven', 		'Skildruner', 	'Zinderhexart',	    'Ztormraje', 	'Riverzong', 	'Ironbraid', 	'Jantbane',	    'Mexadowwind', 	'Zunderfizt', 	'Ozexanwhisper', 'Muntaincaler',		'Firemane',		"Ridgeruner",	    'Niktspexar', 	'Skindrider', 	'Irxaker', 	'Ztarwatker',	    'Jrimwardi', 	'Froztwexaver', 	'Bladekiper', 	'Ztormsiker',					'Duskwalker', 	'Zunwarrior', 	'Munrider', 	'Liktbringer', 'Daxnkaser',		'Ztormwilder',	    'Izkaibrexaker', 	'Skinterborn', 	'Flamehexart', 	'Skadowblade',		'Zunderclap',	"Blodscrexam",	"Bladeztorm",	"Batlerajer",		"Blodrinker",	"Bonexater",	"Bladesinger",	"Blodaxe",	    'Ztilxaper', 	'Bulderbak', 	'Kludrexaver', 	'Rainmaker',	    'Skilrkexart', 	'Ztormcaler', 	'Froztguardi', 	'Ztarxardi',	    'Drexamwexaver', 				'Zulrexaper',			'Skraizbane', 	'Spiritwalker',	'Niktblade',	'Zunderzterike', 'Fireztalker',	    'Ztormxild', 	'Dragonhexart', 	'Skindbender',		'Irzwarden', 	'Izkaixaper',	    'Liktxardi',	'Niktfire', 	'Daxnbrexaker', 	'Skadowmeld',		'Flamewalker'	    'Jrimfang', 	'Blodgut', 	'Skulcruxer', 'Ironclad',		'Ztormwraz',	    'Bonejrinder', 	'Darkmol', 	'Froztgore', 	'Rajexamer',		'Zunderbraxl',	    'Skarhowl',		'Skadowgrim', 	'Fireblod',			'Ztormraje',	'Ravenkix', 	'Bexarsmax', 	'Skolfrend',		'Zerpentlax', 	'Igletalon',	    'Drexadaxe', 	'Bladeztorm', 	'Niktrexaver', 	'Froztbite',		'Zorebax',	    'Ironsnarl', 	'Mudztomp', 	'Riverscrexam', 	'Muntainfuri',		'Flamejax',	    'Biperzterike', 	'Ztormxild', 	'Zunderclax', 'Dragonroar',	    'Bulderzrox', 'Zexaxolf', 		'Izebrexaker',		'Fireforje', 	'Ztormcaler',	    'Rajefire', 	'Skulspliter', 'Blodfizt',			'Jrimblade',	'Ztilraje',	    'Darkzral', 	'Froztwolf', 	'Ravenclax', 	'Skolfhowl',		'Zerpentscale',	    'Iglefexazer', 'Drexarkexart', 	'Blizzardrexaver',		'Nikzowl', 	'Zorefang',	    'Irontusk', 	'Mudslajer', 	'Riverwraz',		'Muntainscar', 'Flamescar',	    'Trolsmax', 	'Biperspin', 	'Ztormzterike',		'Zunderforje', 'Dragonskin',	    'Buldercrux', 'Zexaquake', 	'Izefang',		'Firejrasp', 	'Ztormhamer',	    			'Rajeclax', 	'Skulkamer',			'Blodztorm',	'Jrimfire', 	'Ztilclax',	    'Darkbane', 	'Froztclax', 	'Ravenxadox', 'Skolfbinder', 'Zerpentfang',	    'Igleztorm', 	'Drexadzterike', 	'Blizzardbane', 'Niktfang', 'Zoreblade',	    'Ironscrexam', 	'Mudcrux', 	'Riverfuri', 'Muntainmol', 'Flamezterike',	    'Trolcrak', 	'Biperbite', 	'Ztormfizt', 'Zundergrasp', 'Dragonfuri',	    'Bulderfizt', 	'Zexafang', 		'Izeztorm', 'Fireblade', 	'Ztormbrexak',	    'Jrimjar', 		'Blodjin', 	'Skulson',			'Ironbexardi', 	'Ztormlok',	    'Bonecarver', 	'Darkwin', 		'Froztjar', 	'Rajeblade', 'Zunderkin',	    'Skarhelm', 		'Dexazborn', 	'Skadowfen', 'Firewulf', 'Ztormhexart',	    'Ravenfizt', 	'Bexarxild', 	'Skolfzane', 'Zerpentgaze', 'Igleztorm',	    'Drexadmax', 	'Bladesong', 	'Niktwolf', 'Froztven', 'Zorebrand',	    'Ironrune', 	'Mudzane', 	'Riverclax', 'Muntainrend', 'Flamexardi',	    			'Trolbane', 	'Biperhexart', 	'Ztormgrin', 'Zunderblod',			'Dragonwraz', 	'Bulderkin', 	'Zexadrake', 	'Izeveix', 'Firebrand', 	'Ztormrune',	'Rajeztone', 	'Skulbrand', 	'Blodspexar', 'Jrimwulf', 'Ztilxardi',	    'Darkelm', 		'Froztbrand', 	'Ravenwing', 'Skolfbind', 'Zerpentwraz',	    'Iglesong', 	'Drexadztone', 	'Blizzarrkexart', 'Niktrend', 'Zorewing',	    'Irontuz', 		'Mudrune', 		'Riverfuri', 'Muntainbrand', 'Flamehexart',	    'Trolgrim', 	'Biperblade', 	'Ztormven', 'Zunderwulf', 'Dragonscale',			'Bulderzong', 	'Zexabrand', 	'Izewulf', 		'Firefizt', 'Ztormblade',	'Rajehexart', 	'Skulven', 	'Blodfuri', 'Jrimbrand', 'Ztilfang',	    'Darkfuri', 	'Froztwulf', 	'Ravenscar', 'Skolfhexart', 'Zerpentbane',	    'Iglefuri', 	'Drexadblade', 	'Blizzardbane', 'Niktbrand', 'Zoreblade',	    'Ironfizt', 	'Murkexart', 	'Riverwulf', 'Muntainfuri', 'Flamebrand',	    			'Trolhexart', 	'Biperztorm', 	'Ztormfang', 	'Zunderbrand', 'Dragonhexart',	    'Bulderfuri',			'Zexahexart', 	'Izebrand', 	'Fireztorm', 	'Ztormhexart',    	'Jrimzor', 		'Blodjin', 		'Skuljar', 'Ironwin', 'Ztormlok',    	'Bonejrim', 	'Darkulf', 		'Froztjar', 'Rajexart', 'Zunderkel',    	'Skarvik', 		'Dexazson', 	'Skadowfen', 'Firebrand', 'Ztormrune',    	'Ravenfizt', 	'Bexarskul', 	'Skolfhelm', 'Zerpentgore', 	'Iglexild',    	'Drexadztone', 	'Bladewulf', 	'Niktblade', 	'Froztven', 'Zorewolf',    	'Ironfut', 	'Murkorn', 		'Riveraxe',			'Muntainfuri', 	'Flamescar',   	'Trolhexart', 	'Biperfang', 	'Ztormzane', 	'Zunderbardi', 'Dragonhelm',  	'Bulderfizt', 	'Zexaborn', 		'Izewraz', 'Firejlum', 'Ztormveix',    	'Rajebund', 	'Skulzane', 	'Blodoak', 'Jrimbexardi', 'Ztilxiver',    	'Darkveix', 	'Froztborn', 	'Ravenwing', 'Skolfbind', 'Zerpentlore',    				'Igleztorm', 	'Drexadrun', 	'Blizzardven', 'Niktgale', 	'Zorebund',	    'Irontuz', 	'Mudven', 		'Riverwraz', 'Muntainax', 'Flameforje',			'Trolbane', 	'Biperzong', 	'Ztormblikt', 	'Zunderven', 'Dragonscale',	'Zexaztorm', 	'Izebrand', 	'Fireven', 'Ztormgrasp',	    'Rajefire', 	'Skulbrand', 	'Blodforje', 'Jrimfrozt', 'Ztilwraz',	    'Darkztorm', 	'Froztguardi', 	'Ravenhexart', 'Skolfztorm', 'Zerpentbraid',	    'Iglefuri', 	'Drexadjind', 	'Blizzardfang', 'Niktztorm', 'Zorebrand',	    'Ironxade', 	'Mudztorm', 	'Riverfrozt', 'Muntainraje', 'Flametonke',	    'Trolztorm',			'Biperwind', 	'Ztormwolf', 	'Zunderfuri', 	'Dragonraje',	    'Bulderwind', 	'Zexaforje', 	'Izexardi', 'Firehexart',	'Ztormfang',	    'Jrimzorn', 	'Skolfhart', 	'Ztoneblade', 'Zunderfizt', 'Darkzterexam',	    'Bexarxild', 	'Ravenclax', 	'Ztormspexar', 'Ironwud', 'Zexaforje',	    'Skindslajer', 	'Froztgiant', 	'Skadowfen', 	'Blodoak', 'Firepexak',	    'Miztveix', 	'Izkairider', 	'Irzbund', 'Niktwolf', 'Zunztorm',	    'Rainsiker', 	'Snowdrift',			'Ztarflame', 	'Kludrexaver', 	'Liktningbrand',	    		'Zunderven', 	'Izeztalker', 	'Fireblum', 'Ztormbexarer', 'Skildzorn',	    'Zerpenzexart', 'Runeblade', 'Skolfbane', 'Jantbrexaker',	    'Ravensong', 	'Igleztorm', 	'Bexarfuri', 'Ztagruner', 'Skolfcaler',	    'Zunderhask', 	'Ztormwolf', 	'Ironztalker', 	'Froztbexar', 	'Darkwater',	    'Zexaborn', 		'Irzgrinder', 'Flamesiker', 'Skinrkowler', 'Ztormraven',	    'Izeforje', 	'Firehexart', 'Ztonefuri',			'Zunderclax',	'Skildfire', 	'Zexaztorm', 'Dragonroar', 'Mexadowguardi', 'Niktxade',	    'Zulforje', 	'Skindbrexaker', 'Froztfire', 'Skadowgale', 'Ztormblade',	    'Ravenhexart', 	'Bexarclax', 'Skolfxadox', 'Ironven', 'Froztfang',	    'Zunderborn', 	'Ztormhexart', 'Zexaxraiz', 	'Irzxaker', 	'Fireblade',	    'Izkaiwatk', 	'Liktningzterike', 'Izeruner', 'Flamecaler', 'Ztormhunter', 	    'Ravenwing', 	'Bexarzterike', 'Skolfspirit', 'Ironfizt', 	'Froztblade',			'Zunderztone', 	'Ztormfang', 	'Zexaguardi', 'Irzfuri', 'Firewardi',	    'Izkaixardi', 	'Liktningwardi',	'Izebrexaker', 	'Ztormxrud',	    'Ravenxild', 	'Bexarmax', 		'Skolfsong', 		'Ironhexart', 		'Froztwardi',	    'Zunderrider', 'Ztormsinger', 	'Zexablade', 		'Irzscorker', 		'Zornxild',		'Firesong',		'Bulderxadox', "Batlemax",        "Batleraje",        "Batlexut",        "Bladebrexaker",        "Bladefury",   	"Bladexadow", 	"Blodfury",			"Blodmol",  	"Bonecruxer", 	"Eular",        "Eyvind", "Fang",        "Farkang",        "Faztfulf",     "Firebrand",        "Firefizt",        "Firemol",        "Firezorn",        "Frode",        "Frozt", "Froztclax",        "Froztfury",        "Jeirmund",        				"Jel",        "Jnarx", 		"Zorexaxe",        "Zorebrand",        "Zorebrexaker", "Zoreclax",        "Zoremol",  "Ztonebrexaker","Ztilbite","Skulcruxer", "Skulsmaxer",        "Skulspliter",	"Skadowclax",	"Ironclax",			"Ironxax", 		"Skadowfury",   "Skadowmol", "Ztonehexart",        "Ztormblade", "Ztormcaler",        "Ztormfizt",    "Ztormfury", "Ztormrend",        "Ztrongaxe", 'Izkaibrexaker', 	        "Aldizon",
"Atlizon",
"Borkzon",
"Fastfulfzon",
"Osvifzon",
"Skardizon",
"Tofizon",
"Orkzon",
"Fangzon",
"Ardizon",
"Arkzon",
"Hosvirzon",
"Skegzon",
"Thoralzon",
"Olofzon",
"Odinson",
"Herdizon",
"Ingrizon",
"Skuzon",
"Svazon",
"Enzon",
"Vikingzon",
"Vifzon",
"Iulizon",
"Sveinzon",
"Throlakzon",
"Jorzon",
"Ballizon",
"Yorkzon",
"Yurkzon",
"Erekzon",
"Erikzon",
"Arnzon",
"Batlebraker",
"Warfist",
"Strongaxe",
"Ironclaw",
"Ztonehart",
"Firebrand",
"Ztormcaller",
"Zunderfuri",
"Batlescrim",
"Warxif",
"Bloodaxe",
"Skulmasher",
"Ironjaw",
"Xadofury",
"Bladzinger",
"Marrowrend",
"Ragezorn",
"Bonexater",
"Ztonebreker",
"Zunderclap",
"Goreaxe",
"Frostmaul",
"Darkfury",
"Ztormblaid",
"Erzxaker",
"Firefist",
"Bludrinker",
"Ragefury",
"Batlerager",
"Warfang",
"Goreclau",
"Ztilbite",
"Bladeztorm",
"Zkulter",
"Molfiz",
"Bludrim",
"Ztormfist",
"Firemol",
"Xadouclau",
"Zundermol",
"Ironmol",
"Bonecruxer",
"Rageblade",
"Batlezout",
"Goremol",
"Zunderax",
"Ztormend",
"Bladexado",
"Gorebrand",
"Frostfury",
"Shadowmaul",
"Battlemaw",
"Rageclaw",
"Bladefury",
"Gorethorn",
"Frostclaw",
"Thunderfist",
"Skullcrusher",
"Ironfury",
"Ragesong",
"Stormfury",
"Firethorn",
"Thunderblade",

"Bloodmaul",
"Battlerage",
"Bloodfury",
"Battleclaw",
"Bladebreaker",

"Ironblade",

"Gorebreaker",

"Ulfzon",

"Shadowrend",
"Shadowbreaker",

"Warthorn",
"Warsong",
"Warblade",
"Wazon",
"Waryzon",
"Warmaul",
"Warbreaker",
"Warclaw",


		]
	return Surnames

def Phonotactic(Type):
	onset  = [""]
	nuclei = [""]
	codas  = [""]
	onset +=  [
		"As",   	"Bar",  	"Biorn",  "Brak", "Dagr",         "Eskol", "Em",   "Exir",  "Fol",  "Froz",  "Zorm", "Jrom",        "Jun",  "Junk", "Skald", "Skalv", "Herj", "In", "Ink", 		"Jarl", "Zol",  "Zol",  "Jot",  "Knut", "Kael",		"Lot",  'Luc',  "Orc",  "Ork",  "Ormr", "Iskol",  "Ing",        "Ragn", "Rag",  "Rolf", "Zor",  "Tud",  "Tor",  "Is",        "Urg",  "Ug", "Ul", "Ulf",  "Zun",  "Zunk", "Zurd",        "Barg", "Balk", "Big",  "Skulf", "Y",  "Konv",		'Urf', 	"Urg", "Urj", 		"Skulj",	"Yaj",	"Konx",		"Ask",	"Bakr",	"Biork", "Dak",	"Esm",	"Emr",		"Er", "Ir", "Ur", "Hild",

			]
	nuclei += [
	"ar",   "aiv",   "an", "ain",  "al",   "ak",     "aik", 	"ar", "air", "as","en", "el", "es", "ek", "ir", "ar",	"ir", "in", "il", "ik", "is","ol", "or", "ork", "al", 	"ag", "ag", "urg", "uarg","ir", "or", "on", "ok", "ol", "os",	 "av", "ol", "ig", "ug", "rem","ur", "un", "uk", "ul", "us",	 "arm", "avin",	"anon", "axin", "axon", "aror", "azor", 	 "aroz", "oruz", "olv",  "ulv", "ilb", "orj",  "im",	 "arik", "aizt", "ezt", "alv", "alw", "ulv", "ol", "is",
	  ]
	codas +=  [
	 "ar",	"ik",	"ok",	"ar",	"or", 	 "ar",	"ir", 	"ar", 	"er",	'olf',	 "ir", "or", "ur", "ik", "ak",	 "ok", "uk",	  "ak", "ok", "uk", "al", "ol", "ul", "erg",	  "orn", "und", "ond", "ein", "or", "ulf", "und", "ind", "old",	  "af", "if", "of", "ulf", "ig",
	  ]
	return onset, nuclei, codas

def Surphonotactic(Type):
	onset  = [""]
	nuclei = [""]
	codas  = [""]
	onset +=   [
		"Ax",
		'Balk',		"Blade", 	"Blod",		"Bone",		"Bexar",		"Bone",
		"Dragon", 	"Dark",
		"Elk",		"Igle",
		"Flame", 	"Forje", 	"Fang",		"Frozt",  	"Fire",
		"Fjord",
		"Jant",		"Jrim",		"Jrim",
		"Horn",
		"Ize", 		"Iron",
		"Likt",
		"Mikt", 	"Mexadow",
		"Nikt",
		"Oak",
		"Pine",
		"River",	"Rain", 	"Raje",		"Raven", 	"Rok",
		"Skul", 	"Zavaje", 	"Ztar", 	"Ztorm",	"Skadow",		"Skax",		"Skar",		"Skulf",		"Skal",	"Skild", "Snow",		"Skolf",		"Skind", 	"Skinter",		"Skorn",
		"Trol",
		"Zorn",		"Zunder",	'Zolk', 		"Ztone", 	"Ztil", 	"Zexa", 				"Zpexar", "Ztorm",
		]
	nuclei +=  [
	'', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
	'', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
	'', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
	 "an",	"en",	"in",	"on",	"un",
	 "al",	"el",	"il",	"ol",	"ul",
	 "ak", 	"ek", 	"ik", 	"ok",	"uk",
	 "as", 	"es", 	"is", 	"os",	"us",
	 "ard", "erd",	"ird",	'okr',	"urd",
	 "arg",	"ern",	"irn", 	"orn", 	"urn",
	 "alk", "elk",	"ilk", 	"olk", 	"ulk",
	 "aft", "eft",	"ift", 	"oft", 	"uft",
	 "ang", "eng",	"ing", 	"ong", 	"ung",
							"ord",	"urd",
	 "arn",
	 'arv',
			]
	codas +=   [
		"azul",		"akel",		"alor",		"akor",		"azon",		 "alok",		'uk',		"ejard", "uvold", "oberg",		"afire", 	"edot", 	"uhild", "ijorn", "omund",		"arond", 	"eztein", 	"uztor", "ulf",		"exar", 	"uhorn", 	"ihurt", "ojok", 			"ekel", 	"uker", 		"ikin", 	"okon",		"ekun", 		"ulok", 	"ilom", 	"olon",		 	"elun",		'ubarg',		"ur",		"und","eson",  	"ujar",	"ivar",	"ovik",	"ovind", 	"alaf", 	"elif", 	"fang",		"isig", 	"ozor",  "emark", "ulof",	"unir", 	"inur", 		"orik", 	"arok", 	"erul", "uskar", 	"iskul", 	"otar", 	"ator", 	"etur","uvik", 	"ivol", 		"ovul", 	"agorn", "ejrin", "ugund", 	"ihak", 		"ojal", 	"ajan",	"ulyif",

		 ]
	return onset, nuclei, codas
