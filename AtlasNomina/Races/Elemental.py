
from AtlasLudus.Map_of_Useful_Functions import select1, flip_coin

Water_Elementals = [
		"Arno",			"Marin",		"Anahita",		"Aqualis",		"Avalon",		"Avalon",		"Aqualis",		"Suyasha",		"Neptaline",		"Llyncor",		"Aqua",		"Atlantic",		"Pacific",		"Indian",		"Arctic",		"Antartic",		"Argonaut",		"Lotus",		"Kailani",		"Neptune",		"Neptuno",		"India",		"Maren",		"Mar",		"Oceano",		"Lake",		"Kai",		"Bay",		"Lake",		"Bahia",		"River",		"Nile",		"Kai",			"Caspian",		"Cora",			"Maya",			"Amalia",		"Maia",		"Mira",		"Talia",		"Amaya",		"Tallulah",		"Ren",		"Rene",		"Well",		"Marin",		"Severn",		"Marina",		"Tiber",		"Tiberius",		"Jennifer",		"Jen",		"Rain",		"Wade",		"Ocen",		"Oceanus",		"Beck",		"Malik",		"Malek",		"Irv",		"Clyde",		"Indus",		"Indo",		"Nimue",		"Nim",		"Merlin",		"Nixie",		"Doris",		"Kent",			"Kendall",		"Rio",		"Cove",		"Bahia",		"Innes",		"Moses",		"Fuji",		"Anahita",		"Ginevra",		"Gin",		"Ginebra",		"Jordan",		"Rayan",		"Kelvin",		"Nori",		"Arno",		"Saga",		"Lago",		"Struan",		"Stream",		"Varsha",		"Shannon",		"Ondine",	'Aki',		"Onda",		"Misty",		"Monroe",		"Arnav",		"Ama",		"Lynn",		"Moishe", "Yara",			"Yareli", 		"Oceane",		"Thalassa",		"Bay", "Bey", "Neptune",		"Neptuna", "Sea", "Kairi",		"Ria", "Indra",		"Kano", "Aarna", "Niara",		"Niagara", "Nebula",		"Delta", "Aalto",		"Po", "Araluen", "Jora",		"Naim", "Narelle",		"Nahla", 	"Nerida",		"Nereida", "Neri",		"Cherith",		"Adair",		"Lir",		"Reva",		"Sereia",		"Aqua", "Eyre",		"Mar", "Moana",		"Triton", "Euna",		"Undine", "Nebula",		"Meara", 		"Loch",			"Naida", 		"Oceana",		"Gali", "Tal",		"Loire", "Rilla",		"Varuna",		"Maayan",		"Oceanus",		"Kalani",		"Aquarius",		"Acuario",		"Danu",		"Danubio",		"Tarka",		"Nen",		"Gal",		"Rivo",		"Duna",		"Zarya",		"Laguna",		"Seine",		"Sena",		"Alun", "Kallan",		"Cascada", "Danube",		"Onda", "Wave",		"Baia", "Nile",		"Nilo", "Maree",		"Marea",		"Adria",		"Adriana",		"Alda",			"Alma",		"Amaya",		"Anahita",		"Asita",		"Cherith",		"Darya",		"Dayla",		"Hali",		"Kendra",		"Loire",		"Marella",		"Michal", "Mira",		"Nahla", "Namra", "Reva",		"Ria", "Salila",		"Sarita", "Talia",		"Zarna",		"Zarya",		"Adair",		"Afron",		"Alon",		"Andreus",		"Arnon",		"Bahari",		"Gafar",		"Haf",		"Jafar",		"Kallan",		"Kaveri",		"Malik",		"Ninad",		"Odine",		"Pavati",		"Pulin",		"Sagara",		"Siva",		"Wade",		"Adva",		"Ara",		"Arna",		"Baia",		"Bay",		"Cascade",		"Cascada",		"Coral",		"Eira",		"Euri",		"Isa",		"Ice",		"Snow",		"Isla",		"Jamaica",		"Jordan",		"Jubal",		"Kai",		"Kenga",		"Kline",		"Lago",		"Laguna",		"Laco",		"Lake",		"Laik",			"Maris", 		"Morgan",		"Morgana", 		"Nira",		"Rayan", "Shandy",		"Shannon", "Shore",		"Adair", "Amaya",		"Cary", "Kisima",		"Laguna",		"Narelle", "Nile",		"Nilo",		"Nimue",		"Serena",		"Sereno",		"Yara",		"Alon",		"Kano",		"Wade",		"Naia",		"Tide",		"Adriatic",		"Ariel",		"Athena",		"Atena",		"Azena",		"Eldoris",		"Marin",		"Kona",		"Argo",		"Arcadia",		"Blue",			"Lima",			"Andaya",		"Niar",			"Mora",		"Amal",		"Kaya",		"Dorian",		"Vatnavi",		"Aqua",		"Atlantic",		"Arctic",		"Antartic",		"Argonaut",		"Amalia",		"Amaya",		"Adair",		"Amaya",		"Amal",		"Adair",		"Adriatic",		"Ariel",		"Athena",		"Atena",		"Azena",		"Argo",		"Arcadia",		"Andaya",		"Alon",		"Bahia",		"Beck",		"Bay",		"Bahia",		"Cove",			"Clyde",		"Caspian",		"Cora",			"Doris",		"Fuji",		"Ginebra",		"Gin",		"Ginevra",		"Innes",		"Indo",		"Indus",		"Irv",		"Indian",		"India",		"Jordan",		"Jennifer",		"Jen",		"Kelvin",		"Kendall",		"Kent",		"Kailani",		"Kai",		"Lago",		"Lotus",		"Llyncor",		"Lake",		"Lago",		"Laguna",		"Moses",		"Merlin",		"Malek",		"Malik",		"Marina",		"Maren",		"Mar",			"Marin",		"Marina",		"Marino",		"Maya",		"Maia",		"Mira",		"Nori",		"Nixie",		"Nim",		"Nimue",		"Neptuno",		"Neptune",		"Neptaline",		"Nile",		"Onda",		"Ondine",		"Oceanus",		"Ocen",		"Oceano",		"Pacific",		"Rayan",		"Rio",		"Rain","Ren",		"Rene",		"River",		"Shannon",		"Stream",		"Struan",		"Saga",		"Tiberius",		"Tiber",		"Talia",		"Tallulah",		"Suyasha",		"Severn",		"Varsha",		"Wade",		"Aalto",		"Aarna",		"Acuario",		"Ama",		"Aqua",		"Aquarius",		"Araluen",		"Arnav",		"Bay",		"Bey",		"Cherith",		"Danu",		"Danubio",		"Delta",		"Duna",		"Euna",		"Eyre",		"Gal",		"Gali",		"Indra",		"Jora",		"Kairi",		"Kalani",		"Kano",		"Lir",		"Loch",		"Loire",		"Lynn",			"Maayan",		"Mar",			"Meara",		"Misty",		"Moana",		"Moishe",		"Monroe",		"Nahla",		"Naida",		"Naim",		"Narelle",		"Nebula",		"Nebula",		"Nen",		"Neptuna",		"Neptune",		"Nereida",		"Neri",		"Nerida",		"Niagara",		"Niara",		"Oceana",		"Oceane",		"Oceanus",		"Po",		"Reva",		"Ria",		"Rilla",		"Rivo",		"Sea",		"Sereia",		"Tal",			"Tarka",		"Thalassa",		"Triton",		"Undine",		"Varuna",		"Yara",		"Yareli",		"Zarya",		"Laguna",		"Seine",		"Sena",		"Alun",		"Kallan",		"Cascada",		"Danube",		"Onda",		"Wave",		"Baia",		"Nile",		"Nilo",		"Maree",		"Marea",		"Adria",		"Adriana",		"Alda",		"Alma",		"Amaya",		"Anahita",		"Asita",		"Cherith",		"Darya",		"Dayla",		"Hali",			"Kendra",		"Loire",		"Marella",		"Michal",		"Mira",			"Nahla",		"Namra",		"Reva",		"Ria",		"Salila",		"Sarita",		"Talia",		"Zarna",		"Zarya",		"Adair",		"Afron",		"Alon",		"Andreus",		"Arnon",		"Bahari",		"Gafar",		"Haf",		"Jafar",		"Kallan",		"Kaveri",		"Malik",		"Ninad",		"Odine",		"Pavati",		"Pulin",		"Sagara",		"Siva",			"Wade",			"Adva",			"Ara",			"Arna",		"Baia",			"Dorian",		"Kaya",		"Vatnavi",		"Well",		"Bay",		"Blue",		"Cary",		"Cascada",		"Cascade",		"Coral",		"Eira",		"Eldoris",		"Euri",		"Ice",		"Isa",		"Isla",		"Jamaica",		"Jordan",		"Jubal",		"Kai",		"Kano",		"Kenga",		"Kisima",		"Kline",		"Kona",		"Laco",		"Lago",			"Laguna",		"Laguna",		"Laik",			"Lake",			"Lima",			"Marin",		"Maris",		"Mora",			"Morgan",		"Morgana",		"Naia",		"Narelle",		"Niar",		"Nile",		"Nilo",		"Nimue",		"Nira",		"Rayan",		"Serena",		"Sereno",		"Shandy",		"Shannon",		"Shore",		"Snow",		"Tide",		"Wade",		"Yara",
		]

Fire_Elementals = [
	"Agnam",		"Adarix",		"Arin",			"Alren",		"Adrian",		"Areli",		"Adal",			"Aiden",		"Ardien",		"Azar",			"Alunus",		"Arur",			"Aalish",		"Aatish",		"Aatix",		"Atix",		"Aarush",		"Aarux",		"Arux",		"Abenanka",		"Adara",		"Adeen",		"Adish",		"Admani",		"Adurnarseh",		"Aed",		"Afi",		"Agnes",		"Agneya",		"Agni",		"Agnimitra",		"Agnivo",		"Aguya",		"Ahdan",		"Aidan",		"Aiden",		"Aine",			"Aithne",		"Aizne",		"Akihus",		"Aldebrand",	"Alev",			"Alinta",		"Amani",		"Amarkeeri",	"Anala",		"Angarika",		"Antorcha",		"Apoy",		"Arder",		"Ardere",		"Ardor",		"Atsila",		"Azar",		"Azarnoosh",		"Azula",	"Azar",			"Agni",			"Aiden",		"Anala",		"Aodhox",	"Admani",		"Aalish",		"Adar",			"Aidan",		"Aithne",		"Aizne",		"Alinta",		"Ambar",		"Amber",		"Anala",		"Anya",			"Azav",			"Agni",			"Ardea",		"Aster",		"Arsenic",		"Apollo",		"Agnivir",		"Abenanka",		"Aguya",		"Aithne",		"Alinta",	"Alev",			"Atesh",		"Ashbel",		"Ash",			"Ardere",		"Afi",			"Adish",		"Aidenax",		"Agnix",			"Arur",			"Agnivir",		"Azam",			"Adarin",		"Ari",			"Alen",			"Ambar",		"Arian", 		"Arsenic",		"Aster",		"Areli",		"Arsiden", 		"Adal",			"Ardena",		"Adish",		"Afi",			"Ardere",		"Ash",			"Ashbel",		"Atesh",	"Anya",		"Apollo",	"Amber", 	"Azar",		"Abenanka",	"Azar",			"Aalish",		"Aatish",		"Admani",		"Aalish",		"Aidan", 		"Adar",			"Aithne",		"Aizne",		"Alinta",		"Anala", 		"Azar",			"Azatix",		"Atix",			"Aarush",		"Aarux",		"Arux",			"Abenanka",		"Adara",		"Adeen",		"Adis",			"Admani",		"Agni",			"Aiden",		"Anala",		"Aodh",			"Amani",	"Adurnarseh",	"Aed",	"Afi",		"Agneya",	"Agnes",	"Agni",		"Agnimitra",	"Agnivo",		"Aguya",		"Ahdan",		"Aidan",		"Aiden",		"Aine",			"Aidne",		"Aiznek",		"Akiho",		"Aldebrand",	"Alev",			"Alinta",		"Amarkeri",		"Anala", 		"Angarika",		"Apoy", 		"Ardere",		"Arder", 		"Ardor",		"Atsila", 		"Azah",			"Azula", 		"Azarnux",		"Aguya",		"Aithne",		"Alinta",		"Agni",			"Alev",			"Adar",		"Agni",			"Aiden",		"Antorcha",		"Aigne",	"Adar", 		"Bris",			"Brind",		"Blaise",	"Blaze",		"Bris",			"Brina",		"Brandor",		"Brind",		"Branton",		"Blaze",		"Brand",		"Blazian",		"Brina",		"Blaze",		"Blaise",		"Blaze",		"Bodaway",		"Brent",		"Barbara",		"Bedelia",		"Brid",			"Burn",	"Brand",		"Basia",		"Brit",			"Brigid",		"Brantley",		"Bedelia",		"Blaze",		"Brid",			"Bedelia",		"Basia", 		"Brando",	"Bedelia",		"Brantley", 	"Brigid",		"Brit", 		"Brandr",		"Blaze",		"Blaze",		"Bodaway",		"Brandel",		"Brando",		"Branton",		"Brent",		"Barbara",		"Brand",		"Burn",			"Burn",			"Branton",		"Brenton",		"Calidox",		"Calidax",		"Calan",		"Calcifer",		"Calida",		"Conlex",		"Conley",		"Conlez",		"Calan",		"Cemre",		"Chantico",		"Chantico",		"Cemre",		"Calida",		"Calidad",		"Calina",		"Candace",		"Cenicienta",	"Cavo",			"Cider",		"Ceniza",		"Cinder",		"Cosha",		"Cinderel",		"Cinderella",	"Conlez",		"Cavo",			"Cider",		"Conleth", 		"Cora",			"Conley",		"Cyrus",		"Cosha",		"Cinaed",		"Cyrus",		"Cirio",		"Conlez",		"Cinaed",		"Conlet",		"Conlez",		"Calida",		"Ceniza",		"Candace", 		"Calcifer",		"Cimbeline",	"Cirio",		"Conleth",		"Cairus",		"Cyrus",		"Conlez",		"Conletix",		"Cimbeline",	"Caliza", 		"Calido",		"Cindar",		"Cenicienta",	"Calina",		"Cora",			"Cinderella",	"Cinderel",		"Eldir",		"Emberan",		"Egan",			"Enya",			"Eña",			"Ember",		"Edris",		"Egan",			"Exan",			"Ezan",			"Edana",		"Edan",			"Enya",			"Edana",		"Edris",		"Egan",			"Eldir",		"Elio",			"Ember",		"Eliok",		"Fenix",		"Finlo",		"Fintan",		"Edan",			"Ember",		"Emberic",		"Ena",			"Enia",			"Enya",			"Enix",			"Eña",			"Hito",			"Haco",			"Enya",			"Edan",			"Ember", 		"Ena",			"Enia",			"Flint",		"Fuji",	"Feniax",		"Fujix",		"Fenix",		"Flint",		"Fintan",		"Flama",		"Fiamal",		"Fiama",		"Felios",		"Feliox",		"Feliax",		"Fajra",		"Faira",		"Fiamma",		"Flama",		"Fuocco",		"Fajra", 		"Faira",		"Felia", 		"Fiamma", 		"Fenix",		"Fiama", 		"Flama",		"Felio",		"Flame",		"Fintan",		"Fenix",		"Flame",		"Finlo",		"Flint",		"Fuocco",		"Fedrix",		"Fiamada",		"Fiama",		"Flama",		"Flintan",		"Felios",		"Fiamma",		"Flint",		"Hayden",		"Hera",			"Hayden",		"Haco",			"Hagnan",		"Hagan",		"Haco",			"Hakan",		"Helios",		"Hagan",		"Hurik",		"Haco",			"Idrix",		"Idris", 		"Ignacia",		"Ishat", 		"Idris",		"Iagne",		"Ignacio",		"Igno",			"Ignatius",		"Iñigno", 		"Iñigo",		"Inigo",		"Iñigo",		"Haco",			"Hafla",		"Hagan",		"Hurik",		"Hakan",		"Helios",		"Hera",			"Hito",	 		"Igne",			"Igno",			"Ishat",		"Ignacia",		"Ixan",			"Idris",		"Ignacio",		"Ignatio",		"Igna",			"Ignatius",		"Ignatius",		"Iñigo",		"Ignigo",		"Ignacio",		"Igniferro",	"Inigo",		"Ishan",		"Iñigo", 		"Kalama",		"Igniferro",	"Inigo",		"Igna",			"Ignacio",		"Iñigo",		"Igno",			"Igne", 		"Ignea", 		"Ignea",		"Igne",			"Ignatio",		"Igniatius",	"Kindle",		"Kemna",		"Keegan",		"Keahi",		"Kazuya",		"Kenna",		"Kiran",		"Kai",			"Kalal",		"Kenez",		"Keegan", 		"Kalal",		"Kenna",		"Kalama",		"Kenez",		"Kenna",		"Kindle",		"Keahi",		"Kai",			"Keahis",		"Keegan",		"Kenez",		"Kenneth",		"Keri",			"Kenna",		"Keahi",		"Keegan",		"Kaenna",		"Kayena",		"Kenneth",		"Kiran",		"Kenna",		"Kema",			"Kamar",		"Kazuya", 		"Keri",			"Kari",			"Kamar",		"Kenez",		"Lieki",		"Lavasol",		"Lieki",		"McCoy",		"Mahika",		"Mahuika", 		"Nero",			"Neron",		"Nutau", 		"Mishal",		"Mogotsi",		"Nuri",	 		"Keahi",		"Kahi",			"Liekki",		"Lavasol",		"Lieki",		"Mashal",		"Mogotsi",		"Mishal",		"McCoy",		"Maccoy",		"Maccoy",		"Mogot",		"Mashal",		"Mogotsi",		"Nuria",		"Nootau",		"Nuri",			"Naina",		"Nutau",		"Nina",			"Neri",			"Neron",		"Nuri",			"Nero",			"Nuri",			"Nina",			"Nootau",		"Nuria",		"Neri",			"Nina",			"Oyax",			"Oya", 			"Pele",			"Phoenix",		"Prometeo",		"Prometeus",	"Prometheus",	"Promezeus",	"Pironix",		"Phoenix",		"Prometeus",	"Pairan",		"Pikah",		"Piro", 		"Piris",		"Pairux",		"Piros",		"Piro",			"Pirox",		"Plamen",		"Pirus",		"Pairus",		"Pikah",		"Pirro",		"Plamex",		"Plamen",		"Piros",		"Prometheus",	"Prometeo",		"Promezeus",	"Pele",			"Piris",		"Pirus",		"Pyro", 		"Pirrus", 		"Ra",			"Rave",			"Ravi",			"Rik",			"Rix",			"Ravi", 		"Ris",			"Rayis",		"Rix",			"Plamen",		"Pirro",		"Pirhus",		"Ris",			"Rishe",		"Raix",			"Ra",			"Ravee",		"Satish",		"Sol",			"Saula",		"Solin",		"Souzan",		"Shula", 		"Souzan",		"Shohreh", 		"Soren",		"Sore",			"Torch",		"Tanwen",		"Tulikor",		"Tana",			"Tanya",		"Tulikor",		"Tyson",		"Tana",			"Tangay",		"Tanguy",		"Tito",			"Salamander",	"Satix",		"Shula",		"Shula",		"Souzan",		"Shula",		"Sore",			"Shohreh",		"Sol",			"Solin",		"Solina",		"Souzan",		"Shula",		"Salamander",	"Tanguy",		"Titus",		"Tayson",		"Solina",		"Torch", 		"Titus",		"Torxa",		"Tito",			"Tanguy",		"Torcha", 		"Tana",			"Tanwen",		"Uri", 			"Uric",			"Ugne",			"Uriz",			"Urik",	 		"Uri",			"Urian",		"Ugne",			"Vela",			"Velak",		"Vulcian",		"Vulcanik",		"Vatroslav",	"Vulcan",		"Vatroslav",	"Vulcanic",		"Waruk", 		"Waru",

		]

Earth_Elementals = [
		"Titanium",		"Aluminium", 	"Petra",		"Crystal",		"Aluminum",		"Basalt",		"Basalt",		"Bismuth",		"Alkali",		"Andesite",		"Basalt",		"Basanite",		"Carbon",		"Carbonite",		"Chalk",		"Corsite",		"Dacite",		"Dacite",		"Diamond",		"Dolerite",		"Duna",		"Dune",		"Dunite",		"Ender",		"Essexite",		"Gallium",		"Garnet",		"Grane",		"Granite",		"Granite",		"Geo",		"Ignea",		"Igneo",		"Igneous",		"Igneus",		"Indium",		"Iron",		"Jade",		"Kimberlite",		"Kivinari",		"Latite",		"Lava",		"Lead",		"Magnesium",		"Marble",		"Metam",		"Metamor",		"Muldor",		"Nihonium",		"Obsidian",		"Olivine",		"Onix",		"Opal",		"Ore",		"Adakite",		"Pegmatite",		"Plata",		"Plomo",		"Pluton",		"Potassium",		"Prithvani",		"Rocalia",		"Rock",			"Ruby",			"Sand",			"Sedimentar",	"Sedimentaria",		"Sedimentario",		"Silica",		"Skist",		"Slate",		"Stone",		"Terra",		"Terraque",		"Thallium",		"Tin",		"Titanite",		"Volcan",		"Obsidian",		"Pumice",		"Scoria",		"Sovite",		"Dolomite",		"Chalk",		"Coal",		"Quartz",		"Cuarzo",		"Salt",		"Marble",		"Granite",		"Lapislazuli",		"Lapis",		"Lazuli",		"Adamite",		"Adelite",		"Arenite",		"Almandite",		"Alumn",		"Alunite",		"Amarantite",		"Anandite",		"Antimony",		"Azurite",		"Adamantine",		"Agate",		"Alabaster",		"Bismite",		"Bismut",		"Bronce",		"Cadmium",		"Cerite",		"Carvonite",		"Crystal",		"Copper",		"Cobre",		"Cementite",		"Emerald",		"Diamond",		"Mine",		"Fluorite",		"Garnet",		"Gold",			"Hematite",		"Magnetite",	"Manganite",	"Mesolite",		"Mimetite",		"Mica",		"Magnesia",		"Neptinite",		"Pyrite",		"Pirite",		"Quartz",		"Ruby",		"Turquesa",		"Turkis",		"Turquoise",		"Tremor",		"Uralite",		"Zeolite",		"Zinc",		"Zircon",		"Lithium",		"Sodium",		"Potassium",		"Rubidium",		"Cesium",		"Francium",		"Berillium",		"Magnesium",		"Calcium",		"Strontium",	"Barium",		"Radium",		"Gallium",		"Indium",		"Tin",		"Thallium",		"Alabaster",		"Argento",		"Berilio",		"Berilium",		"Bismutium",		"Bismuto",		"Cadmium",		"Cadmium",		"Calcium",		"Californium",		"Cerium",		"Cesium",		"Chrome",		"Chromium",		"Chromium",		"Clay",		"Coal",		"Cobalt",		"Cobalt",		"Cobalt",		"Copernicium",		"Copper",		"Copper",		"Curium",		"Dustin",		"Einstenium",	"Elessar",		"Fermium",		"Gallium",		"Gold",		"Indium",		"Iridium",		"Iron",		"Iron",		"Lead",		"Lithium",		"Magnesium",		"Manganese",		"Manganese",		"Mercurium",		"Mercury",		"Mercury",		"Nickel",		"Nickel",		"Niobium",		"Nobelium",		"Oro",		"Osmium",		"Palladium",		"Plata",		"Platinum",		"Platinum",		"Plutonium",		"Polonium",		"Potasium",		"Promethium",	"Rodium",		"Rodium",		"Rubidium",		"Silver",		"Silver",		"Sodium",		"Strontium",		"Tin",				"Titanium",		"Tunsten",		"Uranium",		"Uranium",		"Vanadium",		"Vanadium",		"Zinc",		"Zinc",		"Zirconium",		"Zirconiox",		"Emerald",		"Ferro",		"Granite",		"Mercury",		"Mica",		"Oriol",		"Oro",		"Peter",		"Pedro",		"Saphir",		"Silver",		"Steel",		"Stone",		"Zircon",		"Bronze",		"Iron",		"Ferro",		"Electrum",		"Sterling",		"Argentium",		"Titanium",		"Cole",		"Arena",		"Arenita",		"Flint",		"Duna",		"Amatist",		"Gravel",		"Gaia",		"Boulder",		"Bould",		"Atlas",		"Avalanche",		"Midas",		"Flint",		"Basalt",	 "Jade",	 "Mita",	 "Coba",	 "Lead", "Terraque", "Muldor", "Rocalia", 		"Kivinari", 	"Prithvani", 	"Terra", 		"Onix", 		"Opal", "Aluminum", "Gallium", "Indium", "Tin", "Thallium", "Lead", "Bismuth", "Nihonium", "Igneus", "Igneous", "Igneo", "Ignea", "Sedimentar", "Sedimentario", "Sedimentaria", "Metamor", "Metam", "Dacite", "Basalt", "Granite", "Pegmatite", "Basalt", "Obsidian", "Stone", "Chalk", "Sand", "Iron", "Slate", "Skist", "Garnet", "Marble", "Jade", "Ore", "Adakite", "Andesite", "Alkali", "Basalt", "Basanite", "Magnesium", 	"Lava", 		"Volcan", 		"Potassium", 	"Silica", 		"Rock", 		"Carbon", "Carbonite", "Ender", "Dacite", "Dolerite", "Corsite", "Dunite", "Olivine", "Essexite", "Granite", "Grane", "Dune", "Duna", "Pluton", "Kimberlite", "Diamond", "Latite", "Obsidian", "Pumice", "Scoria", "Sovite", "Dolomite", "Chalk", "Coal", "Quartz", "Cuarzo", "Salt", "Marble", "Granite", "Lapislazuli", "Lapis", "Lazuli", "Adamite", "Adelite", "Arenite", "Almandite", "Alumn", "Alunite", 		"Amarantite", 	"Anandite", 	"Antimony", 	"Azurite", 		"Adamantine", 	"Agate", 		"Alabaster", 	"Bismite", "Bismut", "Bronce", "Cadmium", "Cerite", "Carvonite", "Crystal", "Copper", "Cobre", "Cementite", "Emerald", "Diamond", "Mine", "Fluorite", "Garnet", "Gold", "Hematite", "Magnetite", "Manganite", "Mesolite", "Mimetite", "Mica", "Magnesia", "Neptinite", "Pyrite", "Pirite", "Quartz", "Ruby", "Titanite", "Turquesa", "Turkis", "Turquoise", "Tremor", "Uralite", 		"Zeolite", 		"Zinc", 		"Zircon", 		"Lithium", 		"Sodium", 		"Potassium", 	"Rubidium", 	"Cesium", 		"Francium", 	"Berillium", 	"Magnesium", 	"Calcium", "Strontium", "Barium", "Radium", "Aluminium", "Gallium", "Indium", "Tin", "Thallium", "Lead", "Bismuto", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Zirconimum", "Rodium", "Palladium", "Silver", "Cadmium", "Tunsten", "Osmium", "Platinum", 	"Gold", 		"Mercury", 		"Plata", 		"Oro", 			"Copernicium", 	"Uranium", 		"Plutonium", 	"Curium", 		"Californium", 	"Einstenium", 	"Fermium", 		"Nobelium", 	"Lithium", 		"Berilium", 	"Sodium", 		"Magnesium", 	"Potasium", "Calcium", "Titanium", "Vanadium", "Chrome", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Gallium", "Rubidium", "Strontium", "Zirconiam", "Niobium", "Rodium", "Silver", "Cadmium", "Indium", 		"Tin", 			"Cesium", 		"Cerium", 		"Promethium", 	"Iridium", 		"Platinum", 	"Mercury", 		"Mercurium", 	"Lead", 		"Bismutium", 	"Polonium", 	"Uranium", 		"Alabaster", 	"Argento", 		"Berilio", "Clay", 		"Coal", 	"Cobalt", 		"Dustin", 		"Elessar", 		"Emerald", 		"Ferro", 		"Granite", 		"Mercury", 		"Mica", "Oriol", "Oro", "Peter", "Pedro", "Saphir", "Silver", "Steel", "Stone", "Zircon", "Bronze",	"Iron", 		"Ferro",		"Electrum",		"Sterling",		"Argentium",	"Titanium",		"Cole",			"Arena",		"Arenita",		"Flint",		"Duna",			"Amatist",		"Gravel",		"Gaia",			"Boulder", 		"Bould",	"Atlas",		"Avalanche", 	"Midas",		"Flint", 		"Basalt",		"Jade", 		"Mita",	"Coba",
]

Air_Elementals = [
		"Avel", 		"Aerlyn", 		"Vaataan", "Tuulikas", "Ilmara", "Caelistis", "Aero", "Aelio", "Aeolian", "Gale", "Zefir", "Zefyr", "Zephyr", "Zefirus", "Wuzer", "Wuther", "Haboob", "Abroholos", "Auster", "Austru", "Barat", "Berber", "Bayamo", "Bora", "Borasco", "Boreas", "Boreal", "Aurora", "Brisa", "Briza", "Brisot", "Brubu", "Cave", "Kaver", "Chubasco", "Cierzo", "Contrastes", "Cordonazo", "Cyclone", "Etesian", "Euros", "Hurricane", "Huracan", "Wind", "Viento", "Leste", "Levanter", "Levante", 		"Levantera", 	"Levanto", "Leveche", "Mistral", "Norte", "Noreaster", "Norestero", "Norwester", "Noroestero", "Nortero", "Ostria", "Pali", "Santana", "Shamal", "Sharki", "Siroco", "Sumatra", "Tramontana", "Tifon", "Zefiros", "Zefiro", "Zefir", "Bora", "Etesian", "Levant", "Levante", "Leveche", "Harmatan", "Karaburan", "Buran", "Orosi", "Sarma", "Shamal", "Alisio", "Alize", "Bayamo", "Brisote", "Caju", "Nordeste", "Minuano", "Zonda", "Pampero", "Sudestada", "Cordonazo", "Coromuel", 	"Norte", 		"Autan", "Bise", "Brise", "Brisa", "Burle", "Cers", "Cierzo", "Etesian", "Euroclydon", "Fohn", "Gregale", "Helm", "Leveche", "Lodos", "Maestro", "Marin", "Mistral", "Nordes", "Ostro", "Poliente", "Solano", "Tramontane", "Vendavel", "Kona", "Abel", "Aeolus", "Akash", "Amun", "Anan", "Cloud", "Anil", "Nube", "Anore", "Arkansas", "Avel", "Barak", "Baran", "Brontes", "Caelus", "Corentin", "EnlilErjon", "Esen", "Guntur", "Keanu", "Matuu", "Mellan", "Moe", "Myrsky", 		"Naseem", 		"Neifion", 		"Neil", "Neve", "Nigel", "Notus", "Payne", "Perun", "Firun", "Samir", "Sepher", "Shu", "Sky", "Stromur", "Sturm", "Thor", "Thunder", "Storm", "Torm", "Tufani", "Van", "Zenith", "Zephyr", "Zeus", "Aella", "Aethra", "Ahana", "Alize", "Amihan", "Anemos", "Anila", "Araceli", "Audra", "Aura", "Auretta", "Awen", "Azure", "Bonaria", "Ciela", "Cielo", "Dangira", "Dima", "Ekaitza", "Era", "Glaw", "Haizea", "Haneul", "Inanna", "Iris", "Kafeira", "Cafeira", 		"Minnesota", 	"Misty", "Mist", 		"Nephele", 		"Ninlil", "Nuit", "Pilvi", "Puleng", "Rain", "Rakia", "Samira", "Sema", "Skye", "Stormy", "Tempest", "Tondra", "Varsha", "Vetra", "Zerua", "Zilan", "Mistral", "Gibli", "Zonda", "Etesian", "Shamal", "Aither", "Akash", "AlizehAmphorn", "Amun", "Anan", "AnilAnore", "Anvindr", "Ayaz", "Bayu", "Boreas", "Caelus", "Corentin", "Enlil", "Erjon", "Ermir", "Esen", "Eyvinder", "FujinGokcan", "Govad", "Guzrie", "Hayate", "Ilmari", 		"Keyne", 		"Naseem", 		"Neven", "Notus", "Ouranos", 		"Payne", 		"Rabi", 		"Samir", "Sepher", "Soma", "Sota", "Tifon", "Vayu", "Zeferino", "Zenit", "Zefir", "Zeru", "Zeus", "Aella", "Aethra", "Ahana", "Alizee", "Alizeh", "Alya", "Amaterasu", "Amihan", "Anila", "Aria", "Aureole", "Auretta", "Azure", "Bonaria", "Breeze", "Brisa", "Ciela", "CoroEra", "Esen", "Eteri", "Haizea", "Haneul", "Ilma", "Kailani", "Kalani", "Lulani", "Makani", "Meltem", "Miku", 		"Mystral", 		"Nasima", 		"Ninlil", 		"Nuit", 		"Rakia", "Samira", "Sciron", 		"Scirocco", 	"Sefarina", 	"Sema", 		"Skye", 		"Tadita", "Wind", "Zephyrine", "Zerua", "Damini", "Oya", "Nebula", "Misty", "Mist", "Wind", "Brenna", "Sail", "Vela", "Katrina", "Amakir", "Abub", "Zeam", "Vesha", "Nura", "Wura", "Enarise", "Amana", "Aeana", "Akades", "Miste", "Zecori", "Sirocco", "Siroco", "Aura", "Zepherien", "Sior", "Annora", "Ael", 		"Arkansas", 	"Anore", 		"Anil", 		"Anan", 		"Amun", 		"Akash", 		"Aeolus", 		"Abel", 		"Autan", 		"Alize", 		"Alisio", 		"Aurora", 		"Abroholos", 		"Auster", 		"Austru", 		"Aerlyn", 		"Aero", 		"Aelio",		"Aeolian", 		"Brontes",		"Baran", 		"Barak",		"Burle",		"Brisa",		"Brise",		"Bise",		"Brisote",		"Bayamo",		"Buran",		"Bora",		"Barat",		"Berber",		"Bayamo",		"Bora",			"Borasco",		"Boreas",		"Boreal",		"Brisa",		"Briza",		"Brisot",		"Brubu",		"Corentin",		"Caelus",		"Cloud",		"Cierzo",		"Cers",		"Coromuel",		"Cordonazo",		"Caju",		"Cierzo",		"Contrastes",		"Cordonazo",		"Cyclone",		"Chubasco",		"Cave",		"Caelistis",		"Esen",	 "Erjon",		"Enlil",		"Euroclydon",		"Etesian",		"Etesian",		"Etesian",		"Euros",		"Eolien",		"Firun",		"Fohn",		"Guntur",		"Gale",			"Gale",			"Gregale", 		"Helm",		"Harmatan",		"Hurricane",	"Huracan",		"Haboob",		"Ilmara",		"Keanu",		"Kona",		"Kaver",		"Karaburan", 		"Lodos",		"Leveche",		"Leveche",		"Levante",		"Levant",		"Leste",		"Levanter",		"Levante",		"Levantera",		"Levanto",		"Leveche",		"Myrsky",		"Moe",			"Mellan",		"Matuu",		"Mistral",		"Marin",		"Maestro",		"Minuano",		"Mistral",		"Notus",		"Nigel",		"Neve",			"Neil", 		"Neifion",		"Naseem", 		"Nube", 		"Nordes",		"Norte", 		"Nordeste",		"Norte", 		"Noreaster",		"Norestero", 		"Norwester",		"Noroestero",		"Nortero",		"Ostro",		"Orosi", 		"Ostria",		"Perun",		"Payne",		"Poliente", 	"Pampero",		"Pali",			"Sturm",		"Stromur", 		"Sky",		"Shu",		"Sepher",		"Samir", 		"Solano", 		"Sudestada", 	"Shamal", 		"Sarma", 		"Santana", 		"Shamal", 		"Sharki", 		"Siroco", 		"Sumatra", 		"Thunder", 		"Thor", 		"Tramontane", 		"Tuulikas", 		"Tramontana", 		"Tifon",  		"Vendavel", 		"Viento", 		"Vaataan", 		"Wind", 		"Wuzer", 		"Wuther", 		"Zonda", 		"Zefiros", 		"Zefiro", 		"Zefir", 		"Zefir",		"Zefyr", 		"Zephyr", 		"Zefirus",  	"Storm", 		"Torm", 		"Tufani", 		"Van", 		"Zenith", 		"Zephyr", 		"Zeus", 		"Aella", 		"Aethra", 		"Ahana", 		"Aither", 		"Akash", 		"Alize", 		"Alizeh", 		"Amihan", 		"Amphorn", 		"Amun", 		"Anan", 		"Anemos", 		"Anil", 		"Anila", 		"Anore", 		"Anvindr", 		"Araceli", 		"Audra", 		"Aura", 		"Auretta", 		"Awen", 		"Ayaz", 		"Azure", 		"Bayu", 		"Bonaria", 		"Boreas",		"Caelus", 		"Cafeira", 		"Ciela", 		"Cielo", 		"Corentin", 		"Dangira", 		"Dima", 		"Ekaitza", 		"Enlil",		"Era", 		"Erjon",		"Ermir", 		"Esen", 		"Etesian", 		"Eyvinder",		"Fujin", 		"Aella", 		"Aethra",		"Ahana", 		"Alizee", 		"Alizeh",		"Alya",		"Amaterasu",	"Amihan",		"Anila", 		"Aria",		"Aureole",		"Auretta",		"Azure",		"Bonaria", 		"Gibli",		"Glaw", 		"Gokcan",		"Govad",		"Guzrie",		"Haizea", 		"Haneul",		"Hayate", 		"Ilmari", 		"Inanna",		"Iris",		"Kafeira", 		"Keyne",		"Minnesota", 		"Mist",		"Mistral",		"Misty",		"Naseem", 		"Nephele",		"Neven", 		"Ninlil", 		"Notus",		"Nuit", 		"Ouranos", 		"Payne",		"Pilvi", 		"Puleng",		"Rabi",			"Rain",			"Rakia",		"Samir",		"Samira",		"Sema",			"Sepher",		"Shamal",		"Skye", 		"Soma",		"Sota",		"Stormy",		"Tempest", 		"Tifon",		"Tondra",		"Varsha",		"Vayu", 		"Vetra", 		"Zeferino", 		"Zefir",		"Zenit", 		"Zeru", 		"Zerua", 		"Zeus",			"Zilan", 		"Zonda",		"Breeze",		"Brisa",		"Ciela",		"Coro",		"Era",		"Esen",		"Eteri",		"Haizea",		"Haneul",		"Ilma",			"Kailani", 		"Kalani",		"Lulani",		"Makani",		"Meltem",		"Miku",		"Mystral",		"Nasima",		"Ninlil",		"Nuit",		"Rakia",		"Samira",		"Sciron",		"Scirocco",		"Sefarina",		"Sema",		"Skye",		"Tadita", 		"Wind",		"Zephyrine",	"Zerua",		"Damini", 		"Oya",		"Nebula", 		"Misty",		"Mist", 		"Wind", 		"Brenna", 		"Sail",			"Vela", 		"Katrina",		"Amakir", 		"Abub", 		"Zeam", 		"Vesha",		"Nura",		"Wura",		"Enarise",		"Amana",		"Aeana",		"Akades",		"Miste",		"Zecori",		"Sirocco",		"Siroco",		"Aura",		"Zepherien",		"Sior",		"Annora",		"Ael",
		]

Elementals = [
		"Zeruano",		"Exula",		"Estix",	"Stix",		"Lignan",		"Metallor",		"Astrelitz",		"Fulgarnis",		"Glacialyne",		"Rayostrike",		"Jaespirit",		"Ombrosyl",		"Element",		"Lignan",		"Metallor",		"Astrelitz",		"Fulgarnis",		"Glacialyne",		"Rayostrike",		"Ombrosyl",		"Element"		"Aetheria", "Agni", "Agnostos", "Alkeides", "Amphitrite",	"Ananta", "Anemoi", "Aquaena", "Aranya", "Asura",	"Atlantea", "Aura", 		"Azura", 		"Brontes", 		"Calida",	"Celestia", "Chandra", 		"Chasca", 		"Cyclopean", "Darya",	"Dionysus", "Drakon", "Electra", "Eos", "Ephyra",	"Eurus", "Fulgora", "Gaia", "Ganges", "Halia",	"Helios", "Hespera", "Hydros", "Ignatius", "Indra",	"Ixel", "Jadeite", "Kalki", "Khepri", "Kratos",	"Lavaea", "Levana", "Lykos", "Maia", "Marina",	"Mazu", "Medea", "Merapi", "Mnemosyne", "Nereus",	"Nyx", "Oceanus", "Ondine", "Ophion", "Orithyia",	"Osiris", "Pallas", 		"Perseis", 		"Phobos", 		"Poseidia",		"Pyrrhus", 	"Quetzal", 	"Raijin", 		"Rhea", 		"Sagara",		"Samael", "Selene", "Sesha", "Sirocco", "Skiron",	"Styx", "Sula", "Surya", "Tefnut", "Thalassa",	"Thalmos", "Theia", "Tlaloc", "Tridentis", "Typhon",	"Urania", "Varuna", "Vulcan", "Xipil", "Yamuna",	"Zephyra", "Zephyros", "Zinerva", "Zircon", "Zosimos",	    "Aetheria", "Agni", "Agnostos", "Alkeides", "Amphitrite",    "Ananta", "Anemoi", "Aquaena", 		"Aranya", 		"Asura",    	"Atlantea",	 	"Aura", 		"Azura", 		"Brontes", 	"Calida",  	"Celestia", 	"Chandra", 		"Chasca", 		"Cyclopean", 	"Darya",    "Dionysus", "Drakon", "Electra", "Eos", "Ephyra",    "Eurus", "Fulgora", "Gaia", "Ganges", "Halia",    "Helios", "Hespera", "Hydros", "Ignatius", "Indra",    "Ix Chel", "Jadeite", "Kalki", "Khepri", "Kratos",    "Lavaea", "Levana", "Lykos", "Maia", "Marina",	    "Mazu", "Medea", "Merapi", "Mnemosyne", 	"Nereus",	    "Nyx", 			"Oceanus", 		"Ondine", 		"Ophion", 		"Orithyia",	    "Osiris", 		"Pallas", 	"Perseis", 	"Phobos", 		"Poseidia",	    "Pirus", 		"Quetzal", 		"Raijin", 		"Rhea", "Sagara",	    "Samael", "Selene", "Sesha", "Sirocco", "Skiron",	    "Styx", "Sula", "Surya", "Tefnut", "Thalassa",	    "Thalmos", "Theia", "Tlaloc", "Tridentis", "Typhon",	    "Urania", "Varuna", "Vulcan", "Xipil", "Yamuna",	    "Zephyra", "Zephyros", 	"Zinerva", 		"Zircon", 		"Zosimos",	    "Aetheria", 	"Aegon", 		"Agni", 		"Alkeides", 	"Amara",	    "Amphitrite", 	"Ananta", 	"Anemoi", 	"Aquaena", 		"Aranya",	    "Areion", 		"Asura", 		"Astraea", 		"Aura", 		"Aurelian",	    "Azura", 	"Boreas", "Brontes", "Calida", "Calypso",	    "Celestia", "Chandra", "Chasca", "Chronos", "Clymene",	    "Cyclopean", "Darya", "Demeter", "Dionysus", "Drakon",	    "Electra"	, "Eos", 			"Ephyra", 		"Eros", 		"Eurus",	    "Eurybia", 		"Fulgora", 		"Gaia",				"Galene", 		"Ganges",	    "Halia", 		"Helios",		"Hespera",		"Hesperos", 	"Hydros",	"Ignatius", "Indra", 	"Iris",			"Ixachel", 		"Jadeite",	    "Kalki", 		"Khepri", "Kratos",		"Lavaea",	 	"Levana",	    "Lykos", 	"Maia", "Marina",		"Mazu", "Medea",	    "Merapi", "Mnemosyne",		"Nereus", "Nephele", "Nysa",	    "Nyx", 			"Oceanus",		"Ondine", 		"Ophion", 		"Orithyia",	    "Osiris", 		"Pallas",		"Perseis", 			"Phobos",		"Phorcys",	    "Poseidia", 	"Proteus",		"Pyrrhus", 		"Raijin", 		"Rhea",	    "Sagara", 		"Samael", 	"Selene", 	"Sesha", 	"Sirocco",	    "Skiron", 		"Styx", 		"Surya", 		"Tefnut", "Thalassa",	    "Thalmos", "Theia", 		"Tlaloc", 		"Tridentis", 	"Typhon",	    "Urania",	"Varuna", "Vulcan", "Xipil", 		"Yamuna",	    "Zephyra", 		"Zephyros", 	"Zinerva", 		"Zircon", 		"Zosimos",		"Ufana",		"Asaita",			"Merrocurjix",			"Cospian",		"Nainian",		"Kureus",
	]


def Name(genus):
	if flip_coin():
		return select1(Names(genus))
	O, N, C = Phonotactic(genus)
	o = select1(O)
	n = select1(N)
	c = select1(C)
	return f"{o}{n}{c}"

def Surname(genus):
	if flip_coin():
		ancestor = Name(genus)
		return f"{ancestor}us"
	P, F, S = Surphonotactic(genus)
	p = select1(P)
	f = select1(F)
	s = select1(S)
	return f"{p}{f}{s}us"

def Names(genus):
	ATLANTIAN = "Atlantian" in genus
	ZEPHYRIAN = "Zephyrian" in genus
	CRONUSIAN = "Cronusian" in genus

	# ``Names = Elementals`` bound the module global itself, so every ``Names +=``
	# below grew it in place and it never shrank: +1,121 entries per call,
	# without bound. Worse than the memory, it broke the seed. Pick draws from
	# whatever this list holds, so the pool depended on how many Elementals had
	# been asked for earlier in the session, and one seed named one character
	# two different things depending on what came before it. A copy is what was
	# meant: this function reads the vocabulary, it does not edit it.
	Names = list( Elementals )


	if ATLANTIAN:
		Names += [
			"Kida",			"Milo",			"Helga",			"Gaetan",			"Audri",			"Vini",			"Nedak",			"Kashekim",			"Jeb",			"Presten",			"Joxua",
			]
		Names += Earth_Elementals + Water_Elementals
		return Names

	if ZEPHYRIAN:
		Names += [
			"Anon",
			]
		Names += Air_Elementals
		Names += Water_Elementals
		return Names

	if CRONUSIAN:
		Names += Air_Elementals + Fire_Elementals + Earth_Elementals
		return Names

	if  "Eosian" in genus:
		Names += Air_Elementals

	if  "Genasi" in genus:
		pass

	if  "Genie" in genus:
		pass

	if  "Gaians" in genus:
		Names += Earth_Elementals
		return Names

	if  "Hyperian" in genus:
		Names += Air_Elementals + Fire_Elementals
		return Names

	if  "Oceanians" in genus:
		Names += Water_Elementals
		return Names

	if  "Primordial" in genus:
		Names += Water_Elementals + Air_Elementals + Fire_Elementals + Earth_Elementals
		return Names

	if "Promethean" in genus:
		Names += Fire_Elementals + Earth_Elementals
		return Names

	if "Promethean" in genus:
		Names += Fire_Elementals
		return Names

	if  "Salamandrian" in genus:
		Names += Air_Elementals + Fire_Elementals
		return Names

	if  "Titan" in genus:
		Names += Water_Elementals + Air_Elementals + Fire_Elementals + Earth_Elementals
		return Names

	if  "Uranians" in genus:
		Names += Air_Elementals + Earth_Elementals
		return Names

	if  "Magmaforged" in genus:
		Names += Fire_Elementals + Earth_Elementals
		return Names

	if  "Zephyrian" in genus:
		Names += Air_Elementals
		return Names

	if  "Tartarian" in genus:
		Names += Water_Elementals + Earth_Elementals
		return Names

	if  "Etherian" in genus:
		Names +=  Air_Elementals + Fire_Elementals
		return Names

	if  "Galaxian" in genus:
		Names +=  Air_Elementals + Fire_Elementals + Earth_Elementals
		return Names

	if  "Chronian" in genus:
		Names += Water_Elementals + Air_Elementals + Fire_Elementals + Earth_Elementals
		return Names

	if  "Tundran" in genus:
		Names += Water_Elementals + Air_Elementals + Earth_Elementals
		return Names

	Names += Air_Elementals
	Names += Water_Elementals
	Names += Earth_Elementals
	Names += Fire_Elementals

	return Names


def Phonotactic(genus):
	prefx = ["Piro", "Aqua", "Aero", "Geo", "Ferro", "Ether", "Elem"]
	fix = ["i", "a", "o", "e", "u"]
	sufx = ["us", "ix", "or", "an", "el", "ent"]

	if True:
		if "Promethean" in genus:
			prefx += ["Flam", "Igni", "Volt",'Amp','El']
			fix += ["e", "a", "o", 'eri', 'ectr']
			sufx += ["ex", "us", "ar", 'um', 'on']

		if  "Salamandrian" in genus:
			prefx += ["Blaz", "Inf", "Flar"]
			fix += ["i", "o", "u",'er','e','e']
			sufx += ["us", "an", "el",'no']

		if  "Titan" in genus:
			prefx += ["Gig", "Might", "Col"]
			fix += ["a", "e", "o",'os','ant']
			sufx += ["us", "an", "or"]

		if  "Uranians" in genus:
			prefx += ["Celest", "Astra", "Sky"]
			fix += ["i", "u", "o"]
			sufx += ["al", "um", "ion"]

		if  "Magmaforged" in genus:
			prefx += ["Lav", "Magm", "Pyr"]
			fix += ['a','o',"i", "u", "o"]
			sufx += ["us", "an", "on"]

		if  "Zephyrian" in genus:
			prefx += ["Breez", "Gale", "Wind"]
			fix += ["e", "a", "o"]
			sufx += ["or", "us", "an"]

		if  "Tartarian" in genus:
			prefx += ["Abyss", "Deep", "Naut"]
			fix += ["i", "o", "u"]
			sufx += ["us", "an", "ic"]

		if  "Etherian" in genus:
			prefx += ["Ether", "Spir", "Astral"]
			fix += ["a", "e", "i"]
			sufx += ["us", "el", "an"]

		if  "Galaxian" in genus:
			prefx += ["Star", "Cosm", "Galax"]
			fix += ["i", "o", "a"]
			sufx += ["us", "an", "or"]

		if  "Chronian" in genus:
			prefx += ["Etern", "Aeon", "Temp"]
			fix += ["a", "o", "e"]
			sufx += ["us", "or", "um"]

		if  "Tundran" in genus:
			prefx += ["Frost", "Glac", "Snow"]
			fix += ["i", "o", "u"]
			sufx += ["ar", "us", "en"]

	if "Promethean" in genus:
			prefx += ["Flam", "Igni", "Volt",'Amp','El']
			fix += ["e", "a", "o", 'eri', 'ectr']
			sufx += ["ex", "us", "ar", 'um', 'on']

	if  "Primordial" in genus:
			prefx += ["Prim", "Or", "El"]
			fix += ["a", "e", "i",'igi','em']
			sufx += ["us", "on", "ar",'nal',]

	if  "Oceanian" in genus:
			prefx += ["Mare", "Tide", "Wave"]
			fix += ["a", "o", "e"]
			sufx += ["an", "or", "ium"]

	if  "Hyperian" in genus:
			prefx += ["Sol", "Radi", "Lum"]
			fix += ["a", "o", "u", 'in']
			sufx += ["us", "ar", "en"]

	if  "Gaian" in genus:
			prefx += ["Terr", "Geo", "Arbor"]
			fix += ["a", "e", "i"]
			sufx += ["an", "us", "ra"]

	if  "Genie" in genus:
			prefx += ["Myst", "Magi", "Spir"]
			fix += ["i", "o", "a"]
			sufx += ["que", "rix", "an"]

	if  "Genasi" in genus:
			prefx += ["Elem", "Natur", "Vita"]
			fix += ["a", "e", "i", "o"]
			sufx += ["ra", "an", "el", "us"]

	if  "Cronusian" in genus:
			prefx += ["Chron", "Temp", "Aev"]
			fix += ["o", "u", "e"]
			sufx += ["os", "um", "or"]

	if  "Eosian" in genus:
			prefx += ["Sol", "Dawn", "Lum"]
			fix += ["e", "a", "i"]
			sufx += ["ra", "os", "en"]

	if  "Atlantian" in genus:
			prefx += ["Atl","Kid","Aqua", "Mar", "Ocea", "Thal"]
			fix += ["a", "e", "in", "o", "u","ant"]
			sufx += ["ix", "rus", "tus", "lan", "sea","ian"]

	return prefx, fix, sufx

def Surnames(genus):
	"""
	The lexicon of Elemental family names.

	An ingredient returns *data*: a list, built from the genus alone. Surname()
	is the other thing, a generator, and it needs a Character to roll with. This
	used to call it with the genus in the Character's place, so it raised
	TypeError on every Elemental ever generated and each of them silently wore
	a template surname off plantilla.

	The patronymic is what Surname() reaches for first, so it is what the
	lexicon offers here: an ancestor's name with the Latin ending on it. The
	other half of Surname(), building from syllables, is what Surphonotactic is
	already for, and NewWord will do that on its own.
	"""
	return [
		f"{ancestor}us"
		for ancestor in Names( genus )
		]

def Surphonotactic(genus):
	prefx = ["Atl", "Eos", "Cron", "Gen" , 'Gaian',
	 	'Hyp', 'Ocean', 'Prim', 'Prom', 'Tundr',
		'Chron', 'Gal', 'Eth', 'Tart', 'Zeph',
		'Magm', 'Ur', 'Tit', 'Salam', 'Prom']
	fix = ["ant", "",  'us', 'as', '', 'er',
	 	'ord', 'eth', 'ax', 'er', 'ar', 'ir',
		'aforg', 'an', '', 'andr']
	sufx = ["ian", 'i', 'ie', 'ial', 'ean', 'an',
		'an', 'ian']

	try:
		if "Promethean" in genus:
			prefx += ["Flam", "Igni", "Volt",'Amp','El']
			fix += []
			sufx += []

		if  "Salamandrian" in genus:
			prefx += ["Blaz", "Inf", "Flar"]
			fix += []
			sufx += []

		if  "Titan" in genus:
			prefx += ["Gig", "Might", "Col"]
			fix += []
			sufx += []

		if  "Uranians" in genus:
			prefx += ["Celest", "Astra", "Sky"]
			fix += []
			sufx += []

		if  "Magmaforged" in genus:
			prefx += ["Lav", "Magm", "Pyr"]
			fix += []
			sufx += []

		if  "Zephyrian" in genus:
			prefx += ["Breez", "Gale", "Wind"]
			fix += []
			sufx += []

		if  "Tartarian" in genus:
			prefx += ["Abyss", "Deep", "Naut"]
			fix += []
			sufx += [ ]

		if  "Etherian" in genus:
			prefx += ["Ether", "Spir", "Astral"]
			fix += ["a", "e", "i"]
			sufx += ["us", "el", "an"]

		if  "Galaxian" in genus:
			prefx += ["Star", "Cosm", "Galax"]
			fix += [ ]
			sufx += [ ]

		if  "Chronian" in genus:
			prefx += ["Etern", "Aeon", "Temp"]
			fix += [ ]
			sufx += [ ]

		if  "Tundran" in genus:
			prefx += ["Frost", "Glac", "Snow"]
			fix += [ ]
			sufx += [ ]

		if "Promethean" in genus:
				prefx += ["Flam", "Igni", "Volt",'Amp','El']
				fix += [ ]
				sufx += [ ]

		if  "Primordial" in genus:
				prefx += ["Prim", "Or", "El"]
				fix += [ ]
				sufx += [ ]

		if  "Oceanian" in genus:
				prefx += ["Mare", "Tide", "Wave"]
				fix += [ ]
				sufx += [ ]

		if  "Hyperian" in genus:
				prefx += ["Sol", "Radi", "Lum"]
				fix += [ ]
				sufx += [ ]

		if  "Gaian" in genus:
				prefx += ["Terr", "Geo", "Arbor"]
				fix += [ ]
				sufx += [ ]

		if  "Genie" in genus:
				prefx += ["Myst", "Magi", "Spir"]
				fix += [ ]
				sufx += [ ]

		if  "Genasi" in genus:
				prefx += ["Elem", "Natur", "Vita"]
				fix += [ ]
				sufx += [ ]

		if  "Cronusian" in genus:
				prefx += ["Chron", "Temp", "Aev"]
				fix += [ ]
				sufx += [ ]

		if  "Eosian" in genus:
				prefx += ["Sol", "Dawn", "Lum"]
				fix += [ ]
				sufx += [ ]

		if  "Atlantian" in genus:
				prefx += ["Atl","Kid","Aqua", "Mar", "Ocea", "Thal"]
				fix += []
				sufx += [  ]
	except:
		pass
	return prefx, fix, sufx
