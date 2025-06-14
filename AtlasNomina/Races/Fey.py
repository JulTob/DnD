'''
Names for Fairies
Inspirations
	- Fairies
	- Nymph (Meaning)
		- Nayade (Meaning)
		- Sprite
'''
from Minion import Initialized, Alert, Inform, Warning, News, Ends, Fail, Catched, FailureError
from AtlasLudus.Map_of_Useful_Functions import select1

def Name(Character):
	return select1(Names(Character))

def Surname(Character):
	return select1(Surnames(Character))

def Names(Character):
	FEMALE = "Female" in Character
	MALE = "Male" in Character

	Names = []

	Names += [
		'Crow',			'Tsubasu',			'Orionis',			"Oxariox",		"Ofrat",		"Duskheart",		"Glowheart",		"Senka",		"Shixian",		"Senna",		"Fay",		"Pari",		"Tien",		"Keijo",		"Afrinus",		"Alberich",		"Alunsina",		"Aman",		"Amihan",		"Animas",		"Anitun",		"Anjana",		"Anjana",		"Apolaki",		"Ariel",		"Arintero",		"Aswang",		"Arkam",		"Ayalga",		"Balangaw",		"Baranugon",	"Barragán",			"Basajaun",			"Basilisco",		"Basilisco",		"Bathala",		"Bell",		"Bel",		"Bluebell",		"Brujorga",		"Bulan",		"Bungisngis",		"Burlón",		"Busgosu",		"Busgosu",		"Cegua",		"Cid",		"Caspian",		"Cojuelo",		"Compana",		"Coruxa",		"Covadonga",		"Cuelebre",		"Cuevanre",		"Culebre",		"Culebre",		"Cuelebre",		"Dalikamata",		"Dama",		"Diañu",		"Diwata",		"Dorado",			"Duende",			"Duenderde",		"Duwende",		"Ellette",		"Encantaria",		"Etain",		"Fada",		"Fatua",		"Fatue",		"Fatuo",		"Fay",		"Faye",		"Ferret",		"Florian",		"Galipote",		"Glaurung",		"Goodfellow",		"Guajona",		"Gwydion",		"Hadarina",		"Hanan",		"Irati",		"Idiyanale",		"Ikapati",		"Iduri",		"Idulre",		"Kapre",		"Kabunian",		"Lamiak",		"Lavandera",		"Lazarillo",		"Lavandera",		"Llorona",		"Liadlaw",		"Lidagat",		"Lakapati",		"Leazarmire",		"Lin",		"Lorelei",		'Lulu',		"Moura",		"Mari",		"Mora",		"Moron",		"Mananangal",		"Manaul",		"Magwayen",		"Maganda",		"Malakas",		"Mapulon",		"Mab",		"Morgana",		"Melusine",		"Maria",		"Makiling",		"Mayari",		"Nuberu",		"Nuberu",		"Niamh",		"Nyx",				"Tartalo",			"Tikbalang",		"Titania",			"Tinkerbell",		"Tinker",		"Tam",		"Ojancano",		"Oberon",		"Pataricu",		"Patasola",		"Pira",		"Panday",		"Puck",		"Pari",		"Reinoba",		"Ramweldu",		"Rumpelstinski",		"Robin",		"Rhiannon",		"Rusalka",		"Serenagua",		"Sarimanok",		"Silfo",		"Serena",		"Sorgiña",	"Silbon",		"Saco",		"Sidapa",		"Sinaya",		"Silvanus",			"Seelian",			"Sylph",			"Trasgu",			"Tarasca",			"Trasgu",		"Tala",		"Unseelian",		"Ventolín",		"Xana",		"Xana",		"Zana",		"Zahori",		"Zurragamurdi",		'Siofra',
		]

	NYMPH = "Nymph" in Character
	if  NYMPH:
		Names += [
		"Rhapsodia",
		"Rapsodia",
		'Orinia',
		'Naida',
		'Nayade',
		'Naiad',
		'Naida',
		'Nereida',
		'Nerissa',
		'Nymphe',
		'Nymphodoros',
		'Aallotar',
		'Houria',
		'Lamina',
		'Náyade',
		'Nerina',
		'Perihan',
		'Sylph',
		'Uriye',
		'Silfe',
		'Silfide',
		'Silfia',
		'Nereida',
		'Nerissa',
		'Ælfhild',
		'Aibhse',
		'Oillill',
		'Parizad',
		'Síobhra',
		'Umbriel',
		'Yojeong',
		 ]

	if MALE:
		Names += [
		"Merlin",
		"Saruman", "Sayuman", "Suliman",	"Seijuro",		"Senichi",		"Senhichi",		"Sennin",		"Shermatali",
		"Yosei",
		'Orion',		'Oniros',		'Oniro',		'Orino',		'Orinus',		'Onirus',
		]

	if FEMALE:
		Names += [
		"Viribunda",
		'Oriona',
		'Orina',

		"Zura",
		"Ofrata",
		"Zana",
		"Yojeong",
		"Parivash",
		"Villo",
		"Villő",
		"Vilina",
		"Vila",
		"Uriye",
		"Soni",
		"Síobhra",
		"Siobhra",
		"Sheelin",
		"Shaperai",
		"Senki",
		"Sânziana",
		"Sanziana",
		"Quvenzhané",
		"Perihan",
		"Parizad",
		"Parisima",
		"Paribanou",
		"Pariruh",
		"Pariqush",
		"Parinoz",
		"Parinaz",
		"Parijahon",
		"Parigul",
		"Parichehra",
		"Oypari",
		"Lume",
		"Storm",
		"Bellatrix",
		"Nozpari",
		"Norika",
		"Mohipari",
		"Misen",
		"Mayblossom",
		"Mahpari",
		"Mahpare",
		"Mahpara",
		"Gulperi",
		"Lilofee",
		"Lendabair",
		"Lefaye",
		"Khanperi",
		"Jononpari",
		"Hurpari",
		"Hada",
		"Gülperi",
		"Tunde",
		"Gulpari",
		"Golpari",
		"Feya",
		"Aoibhann",
		"Badiaperi",
		"Ferun",
		"Fee",
		"Ehuang",
		"Erina",
		"Älva",
		"Alva",
		"Tunder",
		"Masal",
		"Parisa",
		"Saga",
		"Satu",
		"Sithmaith",
		"Ada",
		]

	return Names

def Surnames(Character):
	Surnames = [
		f"The {Character.subrace}",
		f"The {Character.race}",
		f"Le {Character.subrace}",
		f"El {Character.race}",
		]

	return Surnames

def Phonotactic(Character):
	onset  = [
		"Aur", 		"Alder", 	"Aeg", 		"Aquil",
		"Bram", 	"Briar", 	"Cron", 	"Cael",
		"Circe", 	"Cedar", 	"Divin", 	"Delph",
		"Druid", 	"Druik", 	"Dell", 	"Dusk",
		"Elm",		"Faun", 	"Fol", 		"Flor",
		"Fay",
		"Fawn", 	"Fern",
		"Gorg",
		"Glen",
		"Yur",
		"Hec",  	"Ign", 		"Luc", 		"Lun",
		"Lark", 	"Nostr", 	"Nym", 		"Nim",
		"Medus", 	"Myst",		"Necr", 	"Ocul",
		"Ocu", 		"Orac", 	"Fant", 	"Piz",
		"Pan",		"Ruid", 	"Riv", 		"Riv",
		"Sorc", 	"Sibyl", 	"Ser", 		"Sol",
		"Stell", 	"Sylv",		"Zaum", 	"Trism",
		"Thorn", 	"Taur",		"Vatic", 	"Verd",
		"Vent", 	"Vit", 		"Vern",		"Temp",
		"Wood",     "Row",		"Silv",		"Viv",
		]
	nuclei = [
		"astr", "at", "abr", "ab",
		"aed", "aif", "auf", "agel", "agir",
		"aul", "ath", "aewh",
		"ik",
		"eh", "el", "er", "esapr",
		"eos", "eash", "eo",
		"eah", "eil", "esupr",
		"isper", "iv",
		"iz", "isetr", "istor", "istar", "ister",
		"io", "ia", "io", "ia",
		"ilu",
		"ow", "ok", "ors", "olum", "osopr", "ospur", "oin", "oul",
		"uz", "ux", "uc", "uvir", "utam", "unim",]
	codas  = [
		"a", "andis","amor", "anthe", "anthe",
		"algia","alis", "aris","asia",
		"amis", "andra", "ook", "ark","ance",
		"eia","elix", "entia","era",
		"ella", "enna", "ecia",  "ella", "essa","oot",
		"ern", "ade","ove",
		"art", "orn",        "ithra","ipha",
		"idus","ignis","ina",  "iana",
		"itus", "imna",        "us",
		"eaf",        "oria","osia", "onia",
		"onia", "olus","ora", "orix","ompha",
		"eed",       "ing",
		"ong", "ade", "eam",        "orn",      "urna","une","us",
		"ale", "o",
		"ood","isp",        "ixis",         ]
	NYMPH = "Nymph" in Character
	if  NYMPH:
		Character = 'she'
		codas = [
		'ia', 'idia', 'ilia', 'isia', 'inia', 'isilia', 'ania',
		'acia', 'alia',
		]

	return onset, nuclei, codas

def Surphonotactic(Character):
	onset  = ["Ob", "Tit", "Exc", "Camp"]
	nuclei = ["er", "an", "elenc", "an"]
	codas  = ["on", "ia", "ina", "illa"]
	return onset, nuclei, codas
