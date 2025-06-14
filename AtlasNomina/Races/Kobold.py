def Names(genus):
	MALE    = "He"    in genus
	FEMALE  = "She"   in genus
	AGENDER = "They"  in genus

	SUBgenus = "Subgenus" in genus

	Names = [
"Regakil",		"Cocoriter",	"Chipi",		"Chape",		"Aki",         	"Assik",        "Bik",            "Biki",            "Bakaki",            "Deekin",            "Durnn",            "Eek",            "Kurtulmak",           "Kib",            "Meepo",            "Hox",            "Grit",            "Naknak",            "Fizban",            "Gnarl",            "Grizzle",            "Kratch",            "Pog",            "Ratch",            "Scamp",            "Snarl",            "Skizziks",		"Snick", 		"Sniv",   		"Squee", 		"Sqwik",  		"Slythe",            "Torch",            "Tucker",            "Urdo",            "Whiskar",            "Yipper",            "Zax",            "Zik",		"Xiaoyu",		"Law",		"Lee",		"Lei",		"Rakitoo",		"Rakito",		"Rakita",		"Rakitu",		"Feng",		"Fang",		"Reizik",		"Akbuzz",		"Aki",		"Assik",		"Adeleadle",		"Law",		"Brinix",		"Britnik",		"Bjork",		"Beikle",		"Bowisk",		"Biyonzik",		"Bidink",		"Bux",		"Blairk",		"Bismirk",		"Beezovink",		"Bark",		"Bizzik",		"Bang",		"Breezle",		"Bik",		"Biki",		"Bakaki",		"Churx",		"Cascrock",		"Castrock",		"Curchilk",		"Curierk",		"Clopatrikle",		"Crackle",		"Coromanic",		"Dilank",		"Dok",		"Drakek",		"Darwink",		"Davizzik",		"Dazzle",		"Deekin",		"Durnn",		"Eminemik",		"Elviz",		"Einstix",		"Ediksonk",		"Einsteek",		"Eek",		"Fitzik",		"Friki",		"Fizz",		"Freuk",		"Flemink",		"Fizzle",		"Fizz",		"Fizban",		"Galink",		"Gagalink",		"Gatesk",		"Galilk",		"Gakil",		"Gandalk",		"Gobble",		"Grizzle",		"Glint",		"Gizzik",		"Grit",		"Gnarlak",		"Grizzle",		"Hox",		"Houdinix",		"Hawkink",			  "Hix",			  "Iminink",		"Joplink",		"Jiggerk",		"Josk",			"Jinxle",		"Kobink",		"Kratch",		"Kandi",			  "Kinidi",			  "Kint",		"Krazzle",		"Kurtulmak",			  "Kib",		'Krull',			  "Linconk",		"Leorikca",		"Moikos",			  "Marlix",			  "Midonak",		"Mandalak",		"Macronk",			  "Merkilk",		"Mandik",			  "Mozark",			  "Mizznix",		"Meepo",		"Nixonk",			  "Nikt",			"Newtonk",		"Narf",			"Nibs",			"Naknak",		"Obimi",		"Obimik",		"Pink",		"Princik",			  "Pitink",		"Putink",			  "Picazzok",		"Prattle",		"Poggle",			  "Pog",			  "Rikanix",		"Regank",		"Rusvel",			  "Rattle",		"Ratch",			  "Sinitrix",		"Shikirak",		"Snook",			  "Stilink",			  "Shakeskik",		"Squibble",		"Squeak",			  "Skreech",		"Snarkle",		"Skakrix",		"Scamp",		"Snarl",		"Skizziks",		"Snick",		"Sniv",			  "Squee",		"Sqwik",		"Slythe",			  "Tupack",			  "Trumk",		"Trudok",		"Tacherk",			  "Tolkink",		"Teslak",			  "Trazzik",		"Torch",		"Tucker",			  "Urd",			  "Vizzlebop",		"Vang",		"Warp",			  "Whisker",		"Whisk",			  "Whiskar",			  "Xizz",		"Yipper",		"Zik",			"Zax",			"Zape",			"Zipi",			"Zibzob",		"Zippik",
		]

	return Names

def Surnames(genus):
	Surnames = [""]
	Surnames = Names(genus)
	return Surnames

def Phonotactic(genus):
	onset =  [
"Ak", 	"As", 	"Ax", 	"Bek", 	"Bik", 	"Bok", 	'ak', 'bak', 'drak', 'snik', 'zak', 'krak', 'grik', 'trik', 'skak', 'blak'						"Bak", "Braz", "Chag", "Cax", "Cuk", "Clak", "Cox", "Crix",						"Drag", "Diy","Dil", "Dach", "Dak", "Dan",						"Dank", "Dek", "Duk", "El", "Em", "Elk", "Ekik", "Eik",						"El", 'El', 'Al', 'Fel', 'Gal', 'Lex'						"Em", "Ekl", "Ekil", "El", "Em", "Elx", "Eix", "Exik", "Ed",	"Eiks", "Eek", 	"Fik", 	"Filk", "Fis", 	"Fix", 	"Fr",	"Fl", "Fr",						"Fiz", "Gak", "Gag", "Gax", "Gak", "Gax", "Garag", "Gay", "Gal",						"Gach", "Gak", "Gan", "Gank", "Gr", "Gakuk", "Galam", "Galk",						"Gakik", "Goik", "Giak", "Glik", "Grik", "Hoz", "Hog", "Hax",						"Jok", "Jag", "Joy", "Jal", "Joach", "Jak", "Jon", "Jink",						"Ken", "Kek", "Keuk", "Kel", "Kem", "Kelk", "Kekik", "Keik", "Kelim",	"Kum", "Kikl", "Kr", 	"Lik", 	"Lil", 	"Lim", 	"Likik", "Lix", "Liks",						"Lit", "Lim", "Makl", "Mok", "Mez", "Mik", "Nik", "Nix", "Nilk",						"Nim", "Niks", "Nirl", "Nirk", "Nil", "Niz", "Nak", "Nik", "Nelk",						"Ob", "Obis", "Obz", "Obs", "Obiz", "Obak", "Pik", "Pr", "Punk",						"Pr", "Puzz", "Pur", "Prir", "P", "Puk", "Pix", "Pr", "Pok",						"Pink", "Rek", "Ronz", "Riz",						"Rin", "Rix",	"Rim", 	"Ror", 	"Ret", 	"Rouk", "Rok", 	"Rak",	"St",						"Sik", "Sn", "Shik", "Stik", "Siz", "Snik", "Shik",						"Stik", "Six",						"Sn", "Sh", "Shik", "Sik", "Sc", "Sn", "Sq", "Sl", "Sn",						"Sk",            "Tuc", "Tr", "Th", "Trek", "Thul", "Triz",						"Tux", "Tric", "Thor", "That", "Treps", "Truk", "Thil", "Trox", "Thac",						"Tur", "Trif", "Thot", "Trag", "Treg", "Thub", "Triy", "Trok",	"Tos",	"Tox", 	"Tec", 	"Tor", 	"Tud", 	"Tir", 	"Ur", "Vic", "Wh", "Xir",						"Yif", "Zat", "Zit",
				]
	nuclei = [
'ka', 	'ke', 	'ki', 	'ko', 	'ku', 	'nak', 	'nek',	'nuk',	"ag", 	"az", "al", "ak", "an", "ar", "agik",  "eek",	"ek", "ik", "in", "ic", "ib", "it",						"iz", "iv", "ir", "ikoz", "ix", "iw",						"ixax", "inax", "ikax",						"inet", "ikej", "irax", "ixac", "ikuk", "ixet", "ikiz",						"ikox", "ikac", "ikek", "ikeb", "ikut", "ikip", "inuf", "ikos", "iroc",						"ikax", "iker", "ikut", "ikin", "ixez",  "ikus", "ixus", "ikix", "ikor",	"ikak", "ikel", "ikuz", "ikis", "in", 	"ikox", "irar", "ikark", "iket",						"ik", "ik", "ix","ik", "ix", "ik", "ik", "ik", "ik",						"ik", "ik", "ik", "in", "ik", "ir", "ik", "ik", "ik",						"ik", "ix", "ik", "iz",						"ik", "ik",  "in", "ik", "ir",						"ix",  "ik","emp", 'le',						"og", "ok", "ok", "ok", "ok", "ok", "ok", "ox", "ok",'at',
		]
	codas =  [
'ken',	'kin', 	'tor', 	'rix', 	'nak', 	'zik', 	'rak', 	'nik', 	'lak', 'dor', 'gik',	"arl",  "ark",	"az", 	"ang",	"arl",	"amp",	"arl",	"a",	"ack",  "ae", "ai", "ank",  "ash", "au", "aki", "ble",						"ban","bik","bop", "bik", "cor", "dolf", "deek", "durn",						"erna","eak","ee", "eek","e",  "ea", "ee", "fiz", "hox",						"ish","izle","ik", "izz","ik", "izz", "iv", "i",  "ie",						"io", "ix","keak","kle","kak", "ki", 	"kiz",	'k',	"le",	"mak", 	"nar",	"nak",	"o", 	"oi", 	"oo", 	"ou", 	"oe",	'os',	"pog",	"po",	"rick",	"ax",	"rit",						"sik", "teek", "tch",           "ul","uzz",						"u", "ua", "ue","ik","ya",						"zok","ik","zob","zle",
		]


	return onset, nuclei, codas

def Surphonotactic(genus):
	onset  = [""]
	nuclei = [""]
	codas  = [""]
	onset, nuclei, codas = Phonotactic(genus)
	return onset, nuclei, codas
