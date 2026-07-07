'''
Inspirations
- Food
- Delights of Life
- Hobbits

Names in English
Surnames in French
'''

def Names(Type):
	MALE    = "He"    in Type
	FEMALE  = "She"   in Type
	AGENDER = "They"  in Type

	SUBTYPE = "Subtype" in Type
	Names = []

	Names += [  # English: Joyful things, specially food
	  "Grinhand",		"Adaldrida",	"Lifwalker",	"Regina",	"Jasmine",	    "Sam",	"Pipim",	"Crim",	"Pint",	"Chocolaty",	"Love", "Afiry", "Cuki",	"Chunk", "Dairy",	"Peanut", "Buter",	"Cake", "Milk",	"Cone", "Canoli",	"Caramel", "Canela",	"Chis", "Chery", "Chip",	"Browny", "Chuby",	"Tofy", "Cofy",	"Dublin", "Bake",	"Joint", "Widy", "Milky",	"Minty", "Cuky",	"Pistacho", "Pumpin",	"Almond", "Fresy", "beri", "Cake", 		"Vanilla",		"Sutra", 		"Tiramisu", 	"Whisky", 		"Bacon",		"Banana", 		"Beer",	            "Bluemoon", "Bubble", "Gum",	"Coffee", "Apple", "Cream",	"Candy", "Cotton",	"Dulce", "Garlic", "Grape", "Punch",	"Ponche", "Uva", "Grape", "Tea",	"Lucuma", "Mango", "Maple",	"Chip", "Napolito",	"Napolita", "Pistacho",	"Mora", "Rum", "Ron", "Ginebra",	"Gin", "Martin", "Martini",	"Martina", "Licor", "Melon",	"Almond", "Almendra", "Manela",	"Manzana", "Apple",	"Apricot", "Balsamic", 	"Basil",		"Bluberi", 		"Pepper", 		"Bourbon",		"Bread", 		"Sugar",		"Palomita", "Palomito", "Cacao",	"Corn",     "Caramel",      "Carrot",	"Cardamom", "Cheddar",	"Chili", "Chocolate", "Canela",	"Cinnamon", "Coconut", "Nut",	"Coffee", "Cranberi",	"Apricot", "Durian", "Espresso",	"Ferrero", "Fig", "Garlic",	"Ginger", "Guinness",	"Hazelnut", "Honey", "Jam", "Bean",	"Jelly", "Kaffir",	"Lime", "Kiwi", "Fruit",	"Lemon", "Macadamia", "Mango", "Maple",		"Mocha", 		"Nutella", 		"Nocciola", 	"Nuts",			"Olive", 		"Pear", 		"Peppermint",	"Pickle", 		"Pineaple", 	"Pistachio",	"Plum", "Praline",	"Vino", "Pumpkin",	    "Raisin", "Rose",	            "Rum",	        "Tangerine",	"Violet",	"Walnut",	"Oreo",	"Avocado",	"Amaretto",	"Almendra",	"Aguacate",	"Amarula",	"Aqua",	"Burbon",	"Cognac",	"Chai",	"Creme",	"Coconut",	"Pie",	"Tarta",	"Choc",	"Custard",	"Dorian",	"Elderflower",	"Evermint",	"Fresa",	"Fraise",		"Fejoa",		"Fragola",		"Fruitella",	"Granada",		"Macedonia",	"Grosella",		"Guava",		"Hazelnut",		"Honeycomb",	"Habanero",	"Puro",	"Cigarro",	"Hunny",	"Honey",	"Miel",	"Crema",	"Limon",	"Cafe",	"Kinder",	"Kitkat",	    "Leche",	    "Piruleta",	        "Nougat",	"Neapolitana",	"Neopolitan",	"Nectarina",	"Nuggets",	"Orange",	"Naranja",	"Onion",	"Cebolla",	"Oresos",	"Orchid",	"Orangina",	"Cacahuete",	"Mani",	"Peach",		"Pomme",		"Rubarb",		"Raisin",		"Toblerone",	"Truffle",		"Walnuss",		"Waffle",	"Yogurt",		"Yema",			"Yuzu",			"Carlota", 		"Carrot",		"Zanahoria",	"Zitron",	"Picho",	"Beler",	"Sune",	"Numea",	"Orelle",	"Trafa",	"Marb",	"Sanue",	"Nenara",	"Nanut",	"Egumugoni",	"Maximus",	"Maximo",	"Meridio",	"Bilbo",	    "Samwise",	    "Trim",	    "Milo",	            "Perry",	"Pipin",	"Caramel",	    "Gamwick",	"Mint",	"Herleva",		"Fairfut",		"Berta", 		"Underfut",		"Punkin", 	 	"Tansy",		"Loras", 		"Faela",	"Primrose",		"Celandine", 	"Bramber", 		"Eldo",			"Lalia", 		"Thistle",		"Honeybun", "Ciderpress",	"Butterscotch", "Tiramis", 	"Muffinette",	"Truffelino",		"Raisinet",		"Orangetwist", 	"Gelatino",	"Sorbetta",	"Pesto",	"Cinnamelle",		"Pistachio", 	"Creampuff",	"Nutmeggy",		"Frappucin",		"Caramelita",	"Lemonella",	"Gingerpice",	    "Briochee", "Cherrybelle",	"Brownie",		"Jollybean",	"Gigglepot", 	"Merrychuckle",	"Twinkletoes",	"Gleeheart",	"Sunshine", 	"Chuckleberi",	"Lightheart",	"Giddyup",	"Delighta",	"Gingersnap",	"beri",	"Mocha",	"Taffy",	"Nectarina",	"Hopskip",	"Crumblecake",	"Lemonlark",	"Peppermint",	"Cocoa",	"Ribolum",	"Ribol",	'Bilbedon',	'Aprici',	'Cider',	'Hone',	'Cermel',	'Verlic',	'Varlic',		'Lavender',		'Tumeric',		'Iven',			"Banan",		"Bacon",		"Burbon",		"beri",		"Basil",		"Bread",	"Oriniac",		    "Orin",         "Pan",	        "Bourbon",		"Bean",			"Boots",		"Kaffir",		"Brownie",	"Violet",	"Widy",		"Miel",	"Tofy",		"Kiwi",	"Yem",	"Zitron",	"Yogurt",	"Coco",	"Balsamic",	"Whisky",	"Bramber",	"Carrot",	"Butterscotch",	"beri",	"Vini",		"Apricot",		"Apple",		"Apricot",		"Apple",		"Avocat",		"Almond",		"Almond",		"Afiry",		"Zanahor",		"Uve",			"Waffle",		"Almend",		"Aguacate",		"Amaret", 		"Amarul",		"Bilbi",		"Beler", 		"Macedon",		"Mochi",		"Yuzu",		"Brioche",		"Brioch",		"Briox",
		]
	if FEMALE:
		Names += [
	"Averna",		"Jasmine",		"Vodkaia",		"Tequila",		"Whiskyelle",	"Rumina",	"Ginetta",	"Brandyssa",	"Amaretina",	"Sambuca",	"Kahlúaia",	"Camparina",	"Chartreusea",	"Cointrea",	"Baileysa",	"Drambella",	"Frangelica",	"Pernodia",	"Galliana",	"Benedicta",	"Licorquina",	"Grandmarnie",	"Jenevia",	"Aquavia",	"Cognassa",	"Mezcala",	"Cachaca",	"Orujina",	"Lambanoga",	"Vermuta",	"Piscina",	"Ryeia",	"Macadama",	"TripleSeca",	"Avernina",	"Nonina",	"Chartreusea",	"Marascina",	"Sloea",		"IrishMista",	"Goldschlagi",	"Licorforta",	"Hennessina",	"Patrona",	"Smirna",	"Absoluta",	"JoseCuerva",	"CaptainMorga",	"CrownRoyala",	"Titoia",	"Makersa",	"Thaita",		"Neapolita",	"Sorbetta",		"Oliva",			"Limea",		"Macadamia",	"Basilina",		"Avocada",		"Espressa",		"Fruitella", 	"Caramilia",	"Tiramisa",		"Custarda",		"Hazelina",		"Caramela",		"Dulcina",		"Tartufa",		"Fragolina",	"Limona",		"Cioccolata",	"Stracciatella",	"Nocciola",		"Pistacia",		"Granadilla",	"Lemonella", 	"Melonella",	"Nocciolina",	"Cremina",		"Gelatina",		"Mandorlette",	"Fragollita",	"Limonette",	"Baciolina",	"Stracciabella",	"Mangala",		"Pescarose",	"Arancia",		"Fruttibosca",	"Mirtilla",		"Vegana",		"Senzazucca",	"Variegata",	"Croccantina",	"Cafféta",		"Cassata",		"Rose",			"Cioccolata",	"Lampetta",		"Ananassa",		"Fondenta",		"Cremolina",		"Malaga",		"Cremina",		"Tartufa",		"Liquirisia",	"Caramela",		"Coccona",	"Mandorla",		"Melonia", 		"Gianduina",	"Amarena",		"Zabajona",		"Nocciola",	"Fiordilina",	"Bacia",			"Cioccolata", 	"Fragolina",	"Limonella",	"Pistacia",		"Stracciella",	"Cremina",		"Arany",		"Palomita",		"Nutella", 		"Nocciola",		"Vanilla",		"Manela",		"Canela",		"Pera",			'Rosemary',		"Tarta",		"Granadilla",		"Granada",		"Trafa",		"Pistacha",		"Truffelina", 	"Banana", 		'Pipicia', 		"Cappuccina", 	'Vinnala', 		'Azieta',		'Murielin', 	"Orina",		'Muriel', 		"Beer",				"Birra",			"Cerveza",		"Violeta",		"Yema",			"Zitrona",		"Yogurta", 		"Mocha",		"Vina",			"Aguacata",		'Nara',			'Nari',			"Almendra",		"Almendra",		"Adaldrida", 	"Berta",		"Avocada",		"Almonda",		"Zanoria",			"Uva",			"Amaretta",		"Amarula",		"Aqua",			"Bilba",		"Macedonia",	"Carrota",		"Balsamica", 	"Yuza",
		]
	if MALE:
		Names += [
	"Patron",		"Patrono",		"Smirn",		"Absoluto",		"Jose",				"Cuervo",	"CaptainMor",	"CrownRoy",	"Vodkan",		"Tequil",		"Whiskar",		"Rumo",	"Ginar",	"Brandor",	"Amaret",	"Sambuc",	"Kahlur",	"Campar",	"Chartreus",	"Cointre",	"Baileas",	"Drambui",	"Frangel",	"Pernod",	"Gallian",	"Benedictor",	"Licorquin",	"Grandmar",	"Jenev",	"Aquav",	"Cognac",	"Mezcal",	"Cachac",	"Oruj",	"Lambanog",	"Vermut",	"Pisco",	"Ryeon",		"Macadam",		"TripleSeco",	"Averna",		"Nonin",		"Chartreux",		"Marascin",	"Sloeon",	"IrishMist",	"GreenChar",	"Goldschlag",	"Licorfort",	"Neapolitano",	"Sorbetto",		"Olivero",		"Peachino",		"Limeno",		"Grapafruto",	"Macadamio",	"Basilico",		"Avocado",		"Mango",		"Espresso",		"Cruncho",		"Coconutino",	"Caramelino",	"Salcarmelo",	"Tiramiso",		"Custadius",	"Hazelnuto",	"Caramelo",		"Tartufo",		"Fiorlatto",	"Fragolo",		"Limone",		"Cioccolato",	"Stracciatello",	"Nocciolo",		"Pistachio",	"Mandorin",		"Melonor",		"Amarendil",	"Limoro",		"Cioccol",	"Stracciat",	"Noccior",		"Melonito",		"Noccio",		"Creminor",		"Gelatino",		"Mandorlino",	"Zabai",		"Fragollin",	"Limorick",		"Baciolino",	"Stracciabrim",	"Fiorlemon",	"Tiramino",		"Mangoro",		"Pesco",		"Coccofield",	"Arancio",		"Fruttibosco",	"Mirtillio",	"Vegano",		"Senzo",		"Zuccher",		"Variegato",		"Croccantio",	"Fiordiflor",	"Caffél",		"Cassatino",	"Lamporin",		"Fondentin",	"Cremino",	"Tartufo",		"Liquirizio",	"Caramello",	"Coccon",		"Mandorlin",	"Melonel",		"Amareno",		"Zabajon",		"Nocciar",		"Fiorin",		"Bacio",		"Cioccolotto",	"Fragolin",		"Limono",		"Pistachin",	"Stracciat",	"Amandine",		"Kornigo", 		"Kincake", 		"Napolito",		"Pistacho", 	"Palomito",		"Mantecado",	"Pistachio",		'Cermelo',		"Pistacho",		"Truffelino", 	"Pamfilo",		"Adilian",		"Violeto",		"Yuzo",		"Orinico", 		"Orino", 		"Yemo",			"Zitrono",		"Yogurto",		"Vino",			"Carroto",		"Macedonio", 	"Leroy",		"Frodo",		"Avocado",		"Almondo",		"Zanahorio", 	"Uvo",			"Almendro",		"Aguacato",		"Amaretto",		"Amarulo",		"Aguo",			"Bilbo", 		"Mocho",		"Balsamico",
		]

	Names += [
	"Absant",		"Absol",		"Macadam",		"Vermut",		"Mezcal",		"Amaret",		"Saltine",		"Greente",		"Maple",		"Halva",		"Rootbeer",		"Earlegrey", 	"Seasal",		"Dulce",		"Pistacci",		"Fragol",		"Cioccolat",	"Latte",	"Straccia",		"Aranci",		"Croccan",		"Caramel",		"Cioccolat",	"Ananas",		"Cherryade", 	"Lamington", 	"Banbury", 			"Galusc",			'Volarete',		"Kuchen",		"Kransekake", 	"Puddin",		"Chiskake",		"Honey",		"Marshmellow",	"Fig", 			"Walnut", 		"Cookies",		"Dulce",		"Deleche",		"Hazelnut",		"Nougat",		'Anex',			"Chip",			"Bubble",		"beri",			"Bake",			"Browny",		"Buter",		"Cacahuete", 	"Creampuff", 	"Chuckleberi", 	"Caramel", 		"Caramelita", 	"Ciderpress",		"Cigarro",			"Carlota",		"Cebolla", 		"Celandine", 	"Cinnamelle",	"Crema",		"Cafe",			"Cappuccina",	"Cherrybelle", 	"Crumblecake", 	"Coffee",		"Cranberi",		"Choc",			"Custard",		"Chili",		"Chocolate", 	"Cinnamon",		"Coconut",		"Cacao",		"Corn",			"Caramel",		"Carrot",		"Cardamom",		"Cheddar",		"Cognac",		"Chai",			"Creme", 		"Coconut", 		"Coffee", 		"Cream",			"Candy",			"Cotton",		"Cake",			"Cuky",			"Cofy",			"Chuby",		"Caramel",		"Canela",		"Chis", 		"Chery",		"Chip", 		"Canoli", 		"Cone",			"Cake",			"Chunk",		"Cuki",		"Chocolaty", 	"Choclaty",		"Crima",		"Delighta",		"Durian",		"Dorian",		"Dulce",		"Dublin",		"Dairy",		"Eldo", 		"Egumugoni", 	"Espresso", 	"Elderflower",		"Evermint",			"Fairfut",			"Frappucin", 	"Faela", 		"Ferrero",		"Fig",			"Fruit",		"Fresa",		"Fraise",		"Fejoa",		"Fragola",		"Fresy", 		"Gelatino",		"Gingeralle", 	"Gamwick",		"Giddyup",		"Gingersnap", 	"Gigglepot", 	"Grosella",		"Guava",		"Garlic",		"Ginger",		"Guinness",		"Ginebra",		"Grape",		"Gin",			"Garlic",		"Grape",			"Gum",				"Grinhand",			"Herleva",			"Honeybun",			"Hunny",		"Honey", 		"Hazelnut",		"Honeycomb", 	"Habanero",		"Hopskip",		"Hazelnut",		"Joint", 		"Jam",			"Kinder",		"Kitkat",		"Leche",		"Orider",		"Bilbedon",		"Loras",		"Lalia",		"Lemonlark", 	"Lemon", 		"Limon", 		"Lime",			"Lucuma", 		"Licor",			"Love",				"Lifwalker",		"Merrychuckle",		"Mani",		"Meridio",			"Milo",			"Marb",			"Muffinette", 	"Mint",			"Macadamia",	"Mango",		"Maple",		"Mocha",		"Mora",			"Mango",		"Maple",		"Melon",		"Manzana",		"Martin",		"Martini",		"Martina",		"Minty",		"Milky",		"Milk",			"Maxim",		"Marigold", 	"Numea", 		"Nutmeggy",		"Nectarina",		"Nenara",			"Nanut",			"Naranja",			"Nougat",			"Neapolitana",		"Neopolitan",		"Nectarina", 	"Nuggets", 		"Nuts", 		"Nut",			"Napolita",		"Orangetwist",	"Orelle",		"Oresos",		"Orchid",		"Orangina",		"Onion",		"Orange",		"Olive",		"Oreo",			"Punkin",		"Piruleta",		"Picho",		"Primrose",		"Puddington", 	"Peach", 		"Pomme", 		"Pera",			"Peppermint",		"Pesto",			"Pistachio",		"Perry",			"Pipin",			"Pamfila",		"Pie",		"Puro",				"Pepper",		"Ponche", 		"Punch", 		"Pumpin",		"Peanut",		"Pipim",		"Pint",			"Pear",			"Peppermint", 	"Pickle",		"Pineaple",		"Pistachio", 	"Plum",			"Praline",		"Pumpkin",		"Raisinet",		"Rubarb", 		"Raisin", 		"Raisin", 		"Rose",			"Rum",				"Rumcoke",				"Ron",				"Regina",		"Samwise",			"Sorbetta",			"Sunshine",			"Sune",		"Sanue",			"Sugar",			"Sutra", 		"Sam", 			"Trim",			"Tansy",		"Thistle",		"Twinkletoes", 	"Toblerone", 	"Truffle",		"Tiramis",		"Tangerine",	"Taffy",		"Tea",			"Tequila",		"Tiramisu",		"Underfut",		"Vanilla", 		"Walnuss", 		"Walnut",
		]
	return Names

def Surnames(Type):
	Surnames = [ # French: Joyful things
	"Charteu",			"Cognac",			"Malaga",		"Mieldefleurs",		"Haricot",		"Cervelle",			"Rosé",			"Sourcils",			"Pecan",			"Catalan",		"Xixona"			"Jijona",			"Puddington",		"Frow",				"Bolson",			'Poinare',			"Bilbona",			"Meadowrover",	"Heartkeep",	"Merrymaker",	"Piebaker",	"Ciderbrewer",	"Riverfriend",	"Hillhugger",	"Woolspinner",	"Greenpatcher",	"Fieldwhistler",	"Goldleaf",	"Greenhill",		"Fumherbe",			"Citrouille",	"Honeyhill",	"Tealeaf",	"Basilic",		"Origan",	"Toehop", 			"Honeybrew",		"Longmeadow",		"Clearbrook",		"Puddlejump",		"Cloudskip",		"Smilemore",		"Raisinfield",		"Vignoble",		"Champignon",	"Oliveroot",	"Boulanger",	"Cidergrove",	"Fromagebrook",	"Grainmiller",	"Lavenderlea",	"Beecheese",	"Pommierwood",	"Barleyville",	"Garlicglen",	"Trufflemoor",	"beribush",	"Rougemeadow",		"Rayondemiel",		"Patisserie",	"Herbe",			"Légume",		"Figflower",	"Cheesewick",		"Vinewynd",	"Moulinmeadow",		"Sunflowerfield",	"Tarragontrail",	"Mustardmont",		"Walnutwood",		"Thymetown",		"Rosemaryridge",	"Laughmore",		"Gourmet",		"Daydream",	"Pomme",	"Avocat",	"Banane",	"Mure",	"Cerise",	"Chataigne",	"Clementine",	"Coco",	"Datte",	"Figue",	"Goyave",	"Raisin",	"Pamplemousse",	"Kiwi",	"Lime",				"Mandarine",		"Mangue",			"Melon",	"Olive",			"Orange",			"Papaye",			"Peche",		"Poire",			"Anananas",	"Prune",	"Pomelo",			"Framboise",		"Fraise",			"Melon",			"Groseille",		"Boire",			"Jouer",			"Jus",				"Tomate",			"Raisin",			"Limonade",			"Lait",				"Fromage",		"Glace",		"Champagne",	"Vin",	"Bonbon",			"Oeuf",				"Pain",				"Fromage",			"Fruit",	"Salade",	"Mere",	"Fleurdepomme",		"Noisette",			"Noix",				"Citron"			'Vococ',			'Anocat',		'Pechear',			'Terragon',	'Tarragon',	'Ebruf',	'Curcuma',			'Muror',			'Mure',				"Bramblefoot",		'Bleuet',			"Myrtille",			"Anananas",			"Avocat",			"Banane",			"Barleyville",		"Beecheese",		"beribush",			"Boire", 			"Bonbon",			"Boulanger",	"Brightbrow",	"Cerise",			"Cherise",		"Ciderer",			"Champagne",		"Champignon", 	"Chataigne",		"Cheesewick",		"Cidergrove",		"Citron",			"Clearbrook",		"Clementine",		"Cloudskip",		"Coco",				"Datte",			"Daydream",			"Downyhill",		"Fieldwhistler",	"Figflower",		"Figue",			"Fleurdepomme",		"Fraise",			"Framboise",		"Vachefromage",		"Bleufromage",		"Fromage",			"Fruit",			"Garlicglen",		"Glace",			"Goldleaf",			"Gourmet",			"Goyave",		"Grainmiller",		"Greenbush",		"Greenhill",		"Greenpatcher",		"Groseille",		"Hearthkeeper",		"Herbheart",		"Hillhugger",		"Honeybrew",		"Honeycombhill",	"Honeyhill",		"Jouer",			"Jus",				"Kiwi",				"Lait", 			"Lime",				"Limonade",			"Longmeadow",		"Légume",			"Mandarine",		"Mangue",			"Melon",			"Melon",		"Mere",		"Merrymaker",		"Meadowrover",		"Morningdew",		"Moulinmeadow",		"Mure",				"Mustardmont",		"Nightshade",		"Noisette",			"Noix",		  		"Oeuf",				"Olive",				"Oliveroot",		"Orange",			"Pain", 		"Papaye",			"Patisserie",		"Peche",		  	"Pâtissier",		"Pâtissière",		"Poire",			"Pomelo",			"Pomme",			"Pommierwood",		"Prune",		"Puddlejump",	"Raisin",			"Raisin",		  "Raisinfield",		"Riverfriend",		"Rosemaryridge",	"Rougemeadow",		"Salade",		"Smilemore",		"Sunflowerfield",	"Sweetmeadow",		"Tarragontrail",		"Tealeaf",	  		"Thymetown", 	"Tomate", 		"Truffe",			"Vin",		  		"Noyer",
		]
	return Surnames

def Phonotactic(Type):
	MALE    = "He"    in Type
	FEMALE  = "She"   in Type
	AGENDER = "They"  in Type

	prefix = [
	    'Ad', "Alm", 'Am',
		'Bilb',	"Bel", "Bramb",	"Bals",	"Balsam",
		"Coc", "Carr",
		'El',
		"Frow",	'Frod',	"Fres", 'Frag',
		"Mac", 'Merr', 'Miel', "Moch",
		'Pip',
		'Vin', 'Viol'
		'Yem',
		"Zitr",
		]
	fix = ['',
		"amic", 'aret', "arul",
		"edon", 'endr', 'et',
		'ic', 'in',
		'on', 'ol', "ot",
		]
	suffix =  ["","","",
		'e','elbi',
		'i',
		'on','om',
		]
	if FEMALE:
		suffix = ['a','ia','','a']
	if MALE:
		suffix = ['o','io','','o']

	return prefix, fix, suffix

def Surphonotactic(Type):

	prefix  = ["The", "Coco", "Noix", "Choco", 'Cane',
				'Cafe', 'Coco', 'Viande', "Fraise", "Grape"
				"Raisin", "Creme", "Tea", "Sweet", ]
	fix = [""]
	suffix  = [
		"Feulle", 'lait', 'lolo', 'yourt',		"eufs", 'jaunes', 'sale', 'miel',		'cocotte', 'cheri', "baie", 'sel',		'salte', 'gin', "Beurre", "ecremer",		"leaf", "soucre",
		]
	return prefix, fix, suffix
