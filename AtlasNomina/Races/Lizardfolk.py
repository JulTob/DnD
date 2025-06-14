def Names(Type):
	MALE    = "He"    in Type
	FEMALE  = "She"   in Type
	AGENDER = "They"  in Type

	TURTLEFOLK = "Turtlefolk" in Type

	Names = [
		"Gojira",	"Gozilla",
	"Kermit",	"Lizzy",
	"Argonian",
	"Kroxigor",
	"Zrog",	"Sobek",
	"Kala",	"Slippy",
	"Frogger",
	"Jabba",	"Godzilla",
	"Gorn",	"Reptar",
	"Rango",
	"Charizard",
	"Lickitung",
	"Salazle",	"Bowser",
	"Koopa",	"Rath",
	"Rex",	"Tiranus",
	"Teradon",
	"Tricer",
	"Ceratops",
	"Ricerato",
	"Triceratops",
	"Megalodon",
	"Raptor",	"Velox",
	"Veloxi",	"Loxitor",
	"Saurus",	"Saurius",
	"Lilfoot",
	"Piecitos",	"Turok",
	"Crocomire",
	"Leatherhead",
	"Killcroak",	"Thornback",
	"Yenpa",
		'Targor',
		'Sizerer',
		'Iratet',
		'Kuiza',
		'Etrikun',
		"Etriza",
		'Kowalek',
		"Argonian",
		'Akashecmus',
		'Eptar',
		'Jin',
		'Heihachi',
		'Howarang',
		'Crokek',
		'Eihar',
		'Eizar',

		"Bowser",
		'Xiyit',
		'Kunimitsu',
		"Crocomire",
		"Charizard",
		"Frogger",
		"Gex",
		"Gorn",
		'Lars',
			"Gamcal",
			"Getrin",
			"Gojira",
			"Godzilla",
			"Gozilla",
			"Gojira",
			"Goxila",
			"Jabba",
			"Killcroak",
			"Koopa",
			"Kaa",
			"Kroxigor",
			"Kermit",
			"Kowalouba",
			"Leatherhead",
			"Lickitung",
			"Lizzy",
			"Nowak"
			"Rath",
			"Rango",
			"Reptar",
			"Salazzle",
			"Slippy",
			"Sobek",
			"Thornback",
			"Turok",
			"Throgg",
			'Toek',
			"Turoc",
			"Yenpa",
			]
	if  FEMALE:
		Names += [
			"Asuka",
			'Akita',
			]
	if  TURTLEFOLK:
		Names += [
			"Donatello",
			"Leonardo",
			"Michelangelo",
			"Raphael",
			# Teenage Mutant Ninja Renaissance Artists!
			"Botticelli",
			"Caravaggio",
			"Giotto",
			"Titian",
			"Verrocchio",
			"Masaccio",
			"Bellini",
			"Tintoretto",
			"Uccello",
			"Bronzino",
			"Vasari",
			"Greco",
			"Ghiberti",
			"Perugino",
			"Vincent",       # Vincent van Gogh, Post-Impressionist painter
			"Vangogh",
			"Rembrandt",     # Rembrandt van Rijn, Dutch Golden Age painter
			"Picasso",       # Pablo Picasso, Spanish painter and sculptor, known for Cubism
			"Dali",          # Salvador Dalí, Spanish Surrealist artist
			"Monet",         # Claude Monet, founder of French Impressionist painting
			"Klimt",         # Gustav Klimt, Austrian Symbolist painter
			"Cezanne",       # Paul Cézanne, French artist and Post-Impressionist painter
			"Gauguin",       # Paul Gauguin, French Post-Impressionist artist
			"Matisse",       # Henri Matisse, French artist, known for his use of color and draughtsmanship
			"Hokusai",       # Katsushika Hokusai, Japanese ukiyo-e artist
			"Warhol",        # Andy Warhol, leading figure in the visual art movement known as pop art
			"Frida",         # Frida Kahlo, Mexican painter known for her many portraits and self-portraits
			"Keeffe",        # Georgia O'Keeffe, American artist known for her paintings of enlarged flowers
			"Pollock",       # Jackson Pollock, American painter and a major figure in the abstract expressionist movement
			"Basquiat",      # Jean-Michel Basquiat, American artist known for his raw gestural style of painting
			"Kandinsky",     # Wassily Kandinsky, Russian painter and art theorist
			"Rothko",        # Mark Rothko, American abstract painter known for his color field paintings
			"Goya",          # Francisco Goya, Spanish romantic painter and printmaker
			"Davinci",       # Leonardo da Vinci, Italian polymath of the Renaissance
					"Basquiat",
					"Beksinski",
					"Bellini",
					"Botticelli",
					"Bronzino",
					"Caravaggio",
					"Cezanne",
					"Dali",
					"Davinci",
					"Frida",
					"Gauguin",
					"Ghiberti",
					"Giotto",
					"Goya",
					"Greco",
					"Hokusai",
					"Kandinsky",
					"Keeffe",
					"Klimt",
					"Masaccio",
					"Matisse",
					"Monet",
					"Perugino",
					"Picasso",
					"Pollock",
					"Rembrandt",
					"Rothko",
					"Tintoretto",
					"Titian",
					"Uccello",
					"Vangogh",
					"Vasari",
					"Verrocchio",
					"Vincent",
					"Warhol",
										]

	return Names

def Surnames(Type):
	Surnames = [""]
	return Surnames

def Phonotactic(Type):
	TURTLEFOLK = "Turtlefolk" in Type

	prefx=[
		"S",    "Kir",  "Zer",  "Tas",  "Xiy",
		"Ger",  "Vir",  "Sik",  "Sil",  "Der",
		"Has",  "Kas",  "Zes",  "Cah",  "Geh",
		"Kil",  "Tal",  "Vel",  "Zil",  "Raz",
		"Sez",  "Tih",  "Xoz",  "Yuz",	'Rept',
		"Bal",  "Ber",  "Diz",	'Ept',
		"For",  "Gul",  "Gaz",  "G",    "Kero",
		"Tihr", "S",    "Gar",
		"K",    "Sil",  "Jab",  "Gor",  "Rep",
		"Ran",  "Coh",  "Jaz",
		"Lick", "Sal",  "Bow",  "K",    "Rath",
		"Gex",  "Tur",  "Cer",  "L",
		"Kill", "Torn", "Yen",  "Liz",  "Kerm",
		"Arg",
		"Fur",  "Godz", "Rang", "Tur",
		"Kowal",        "Nowak",        "Win",
		"Woj",  "Kam",
		"Lew",  "Dab",  "Sob",  "Kacz", "Zaj",
		"Baran",
		"Krol", "Maj",  "Jaw",  "Mal",  "Sta",
		"Pol",  "Sep",  "Zar",  "Kub",
				 ]
	fix = [
		'and',  "en",   'in',   'or',   "urt",
		'ar',   "epep", 'in',   'og',   "ul",
		"as",   "ekak", 'ip',   "or",   "ucuc",
		"ases", "eb",   "iz",   "oxox", "unon",
		"amum", "elil", "ikik", 'ocom', "ugag",
		"anan", "eror", "itat", "olal", "uziz",
		"atit", "esus", "ixex", "orur", "umem",
		"anon", "ek",   "izoz", "otet", "ucr",
		"ab",   "er",   "irur", "onin", "uk",
		"ango", "ert",  "ill",  "og",   "ung",
		"aro",  "ez",   "iras", "orok", "urt",
		"ack",  "ew",   "illa", "oga",  "uzar",
		"anp",  "ep",   "izo",  "or",   "uith",
		"ar",   "eok",  "ix",   "opop", "uir",
		"aow",  "eko",  "ith",  "og",   "uski",
		"ak",   "ecziy","ib",   "on",   "uska",
		"aczak","eik",  "ile",  "ong",  "uyk",
		"asz",  "eisz", "ieth",	'','','','','',
		]
	sufx = [
		"at",   "ek",   "it",   "ot",   "uk",
		"at",   "et",   "ih",   "oh",   "ut",
		"ad",   "eg",   "ik",   "op",   "uh",
		"ap",   "ep",   "ip",   "ot",   "ut",
		"ak",   "es",   "is",   "os",   "us",
		"a",    "ek",   "it",   "oy",   "ukik",
		"a",    "ey",   "ian",  "or",   "uski",
		"a",    "er",   "igor", "og",   "urok",
		"a",    "ex",   "in",   "owski","uzle",
		"ak",   "ek",   "ik",   "otar", "utun",
		"ago",  "ead",  "ire",  "oak",  "ucak",
		"ar",   "ewic", "icek", "okic", "uzak",
		"ack",  "er",   "i",    "ozak", "uko",
		"a",    "enki", "inki", "oski",	'ar',
		"cka",  "eski", "iki",  "oskik",
		"a",
		"aki",
		]

	if TURTLEFOLK:
			prefx+=["Don", "Leo", "Mich", "Raph", "Bott", "Cara", "Giot", "Tit",
					 "Verr", "Masa", "Bell", "Tinto", "Ucc", "Bron", "Vas", "Grec",
					 "Ghib", "Peru", "Vinc", "Van", "Rem",
					 "Pic", "Dal", "Mon", "Klim", "Cez", "Gaug", "Mat", "Hoku",
					 "War", "Frid", "Kee", "Poll", "Basi", "Kand", "Roth",
					  "Goy", "Davi",
					   ]
			fix+=["a", "e", "i", "o", "u", "ello", "ardo", "angelo", "ael",
					  "icci", "aggio", "otto", "ian", "occhio", "accio", "ini",
					  "etto", "ello", "ino", "eco", "erti", "ino", "ent",
					  "ang", "brandt", "asso", "ali", "net", "mt", "sse", "sai",
					  "hol", "rida", "effe", "llock", "quiat", "insky", "thko",
					  "ya", "vinci"
						]
			sufx+=["tello", "nardo", "gelo", "phael", "celli", "vaggio", "otto",
					 "tian", "cchio", "saccio", "ini", "tto", "cello", "sari", "eco",
					 "hiberti", "gino", "cent", "gogh","ent",
					 "brandt", "sso", "li", "net", "mt", "sse", "sai", "hol", "rida",
					 "effe", "llock", "quiat", "insky", "thko", "ya", "vinci"
						]

	return prefx, fix, sufx

def Surphonotactic(Type):
	prefx  = [""]
	fix = [""]
	sufx  = [""]
	return prefx, fix, sufx
