'''
Names for Fairies
Inspirations
	- Mermaid (Meaning)
	#   Nāra (f)  Nerina (f)  Sirena (f)  Syrén (f)  Tsugkinúa (f)  Undinė (f)  Uriye (f)  Vandenė (f)
'''
from Minion import Initialized, Alert, Inform, Warning, News, Ends, Fail, Catched, FailureError



def Names(genus):
	Initialized("Beastfolk Names")
	MALE    = "He"    in genus
	FEMALE  = "She"   in genus
	AGENDER = "They"  in genus
	PAN = ("Satyr" in genus) or ("Minotaur" in genus) or ("Centaur" in genus)
	ARACNID = ("Arachnid" in genus) or ("Scorpion" in genus)
	ELEPHANT = ("Elephantian" in genus)
	GNOLL = ("Gnoll" in genus)
	INSECT = ("Insectfolk" in genus)
	JACKAL = ("Jackalmen" in genus)
	FOX = ("Kitsune" in genus)

	Names = [
		'Aurrijae',
		"Yoshi",
		"Mitsu",
		"Yoshimitsu",
		"Ichigo",
		"Itachi",
		"Akuma",
		'King',
		"Aurig",
		"Auriga",
		"Aurigia",
		"Lorjan",
		"Xelisi",
		"Gamcal",
		"Kunimitsu",
		'Jentukin',
	"Amaruq",
	"Bleddyn",
	"Boris",
	"Caleb",
	"Catellus",
	"Fox",
	"Gela",
	"Gurgen",
	"Ivaylo",
	"Loup",
	"Lowell",
	"Lycus",
	"Mahihkan",
	"Shaw",
	"Sítheach",
	"Tod",
	"Todd",
	"Ulf",
	"Valko",
	"Varg",
	"Vuk",
	"Vukašin",
	"Wolf",
	"Zeev",
	"Zorro",
	"Anwolf",
	"Æðelwulf",
	"Agilulf",
	"Arnulf",
	"Aþalawulfaz",
	"Athaulf",
	"Badulf",
	"Banquo",
	"Bardulf",
	"Baugulf",
	"Beowulf",
	"Botwulf",
	"Cailean",
	"Coileán",
	"Conall",
	"Conán",
	"Conan",
	"Conchobar",
	"Connla",
	"Conrí",
	"Cúán",
	"Cúchulainn",
	"Cúchulainn",
	"Cunobelinos",
	"Eadwulf",
	"Eardwulf",
	"Faolán",
	"Fastúlfr",
	"Gerulf",
	"Hrōþiwulfaz",
	"Hroðulf",
	"Hróðulfr",
	"Ingolf",
	"Ingólfr",
	"Inola",
	"Kentigern",
	"Landulf",
	"Lovel",
	"Lovell",
	"Ludolf",
	"Lycurgus",
	"Maelgwn",
	"Radulf",
	"Raginolf",
	"Randolf",
	"Raðulfr",
	"Rēdawulfaz",
	"Rudolf",
	"Stithulf",
	"Tahmuras",
	"Velvel",
	"Wolfdietrich",
	"Wolfgang",
	"Wolfhard",
	"Wolfram",
	"Wulfflæd",
	"Wulfgifu",
	"Wulfila",
	"Wulfnoð",
	"Wulfric",
	"Wulfrun",
	"Wulfsige",
	"Wulfstan",
	"Wulfwynn"
	]

	if FEMALE:
		Names += [
			'Katarina',
			'Kazumi',
			]

	if MALE:
		Names += [
			'Naruto',
			'Kazumi',
			'Samir',
			"Obalor",
			]

	if PAN:
		Names += [
		'Chiron',
		'Ferethos',
		'Zaumastrasia',
		'Kaelion',
		'Heronax',
		'Pheras',
		'Alkipos',
		'Mithreon',
		'Galaxion',
		'Tiberios',
		'Nikostos',
		'Aridias',
				'Erigo',
				'Savikas',
				"Rhapsody",
				"Agosto",
				"Antoniopoulos",
				"Aras",
				"Augustus",
				"Callipe",
				"Canadi",
				"Channadi",
				"Erxidor",
				"Faeral",
				"Famtoros",
				"Famtos",
				"Fannus",
				"Fauna",
				"Faunnus",
				"Fauno",
				"Faustou",
				"Feoros",
				"Fladora",
				"Gotae",
				"Hector",
				"Herald",
				"Kratos",
				"Lamtus",
				"Minos",
				"Minos",
				"Nicolaos",
				"Pamtus",
				"Pan",
				"Pantao",
				"Toros",
				'Heracles',
				'Omero',
				]

	if ARACNID:
		Names += [
			'Aranea',
			'Arachna',
			'Silkena',
			'Tkalara',
			'Webrix',
			'Venemir',
			'Ophrida',
			'Spindra',
			'Xerith',
			'Lilacra',
			'Zenthis',
			'Weavrith',
			'Kinasuj',
			"Ahhotep",
			"Ahmose",
			"Akhethetep",
			"Amenemhat",
			"Amenemope",
			"Amenhotep",
			"Amenirdis",
			"Amenmose",
			"Ameny",
			"Ankhesenpepi",
			"Dijehuty",
			"Harsiese",
			"Henuttawy",
			"Hetepheres",
			"Hori",
			"Huy",
			"Iset",
			"Isetemekheb",
			"Isetnofret",
			"Karomama",
			"Khaemwaset",
			"Khamerernebty",
			"Khenemetneferhedjet",
			"Khentkaus",
			"Kheti",
			"Khnumhotep",
			"Maatkare",
			"Menkheperre",
			"Mentuherkhepeshef",
			"Mentuhotep",
			"Meresankh",
			"Meritamen",
			"Meritites",
			"Mery",
			"Meryre",
			"Minmose",
			"Neferkare",
			"Neferneferuaten",
			"Nefertari",
			"Neferu",
			"Nimlot",
			"Panehesy",
			"Pedubastis",
			"Psusennes",
			"Ptahhotep",
			"Ptahmose",
			"Qar",
			"Ramesses",
			"Ramose",
			"Sekhemrekhutawy",
			"Senusret",
			"Setepenre",
			"Shoshenq",
			"Siamun",
			"Smendes" ,
			"Sobekemsaf",
			"Sobekhotep",
			"Tentamun",
			"Thutmose",
			"Tiye",
			"Usermontu",
			]

	if "Merfolk" in genus:
		Names += [
		"Halimar",
		"Ariel",
		"Coral",
		"Aquata",
		"Merliah",
		"Morvoren",
		"Elana",
		]

	if ELEPHANT:
		Names += [
		'Ganeshar',
		'Mammuthas',
		'Tandaro',
		'Ivorya',
		'Jumbari',
		'Pachyros',
		'Alvantos',
		'Tenabrax',
		'Gurushal',
		'Varnath',
		]

	if GNOLL:
		Names += [
			'Graknir',
			'Yenogu',
			'Zarrek',
			'Vrakta',
			'Zrazik',
			'Korrag',
			'Nilka',
			'Rozas',
			'Zufrik',
			'Zarkla',
			]

	if INSECT:
		Names += [
		'Chitik',
		'Xivara',
		'Kriyilix',
		'Zirnoz',
		'Vespara',
		'Antirok',
		'Scayiken',
		'Mandabrix',
		'Larvius',
		'Buzzik',
			]

	if JACKAL:
		Names += [
		"Anubek", "Setanos", "Kheptra",
		"Ahmenis", "Sobakra", "Tijarith",
		"Kenra", "Makteth", "Zarukhan", "Isiroth",
		]

	if FOX:
		Names += [
			"Ahri",	"Amateru", "Inari", "Mitsuko",	"Yukari", "Hikaru", "Renji",			"Kiyora", "Aokitsune", "Sorano",		"Karasu",
			]
	return Names

def Surnames(genus):
	Initialized("Beastfolk Surnames")
	Surnames = Names(genus)
	return Surnames

def Phonotactic(genus):
	Initialized("Phonotactic")
	PAN = ("Satyr" in genus) or ("Minotaur" in genus) or ("Centaur" in genus)
	ARACNID = ("Arachnid" in genus) or ("Scorpion" in genus)
	ELEPHANT = ("Elephantian" in genus)
	GNOLL = ("Gnoll" in genus)
	INSECT = ("Insectfolk" in genus)
	JACKAL = ("Jackalmen" in genus)
	FOX = ("Kitsune" in genus)

	onset  = [
		'Lorj','Xen','Fur','Kor','Xent','Jaur','Gam', 'Afr'
		]
	nuclei = ['ic','','er','ios','uk','is','alc','in']
	codas  = ['an','ax','ios','ix','in','ot','as']

	if  PAN:
		onset += [
			'Taur','Krar','Call','Fam','Top','Tu','Pan','Min','Tau', 'Chix', 'Kael', 'Her', 'Nik', 'Alk', 'Gal', 'Tib', 'Fer']
		nuclei += [
			'','aur','il','ot','op','ops', 'er', 'or', 'ap', 'it', 'eth', 'olp', 'ut']
		codas += [
			'os','os','e','e','os','us',	'on', 'ios', 'as', 'os', 'oron', 'opos', 'ion']
	if ARACNID:
		onset += ['Ar', 'Tk', 'Sp', 'We', 'Xer', 'Zent', 'Lil', 'Ven', 'Arach']
		nuclei += ['an', 'er', 'ir', 'om', 'ux', 'ay',
			]
		codas += ['a', 'a', 'ath', 'ix', 'ir', 'id', 'eth']
	if ELEPHANT:
		onset += ['Gan', 'Mam', 'Tan', 'Iv', 'Jum', 'Alv', 'Gur', 'Var']
		nuclei += ['al', 'on', 'ut', 'ebr', 'ar']
		codas += ['ar', 'os', 'ax', 'al', 'os', 'eth']
	if GNOLL:
		onset +=  ['Gar', 'Zaj', 'Sun', 'Var', 'Kor', 'Fur', 'Nay', 'Zar']
		nuclei +=  ['an', 'iz', 'ur', 'oz', 'ar', 'agr']
		codas +=  ['ir', 'a', 'ek', 'ik', 'ag', 'aka']
	if INSECT:
		onset += ['Kir', 'Xiv', 'Kriy', 'Zir', 'Ves', 'Ant', 'Zik']
		nuclei += ['it', 'ar', 'on', 'iy', 'ap', 'or', 'iv', ]
		codas += ['ik', 'ix', 'oz', 'ar', 'ix', 'ius']
	if JACKAL:
		onset += ['An', 'Set', 'Khep', 'Ahm', 'Sob', 'Taj', 'Ken', 'Mak']
		nuclei += ['ub', 'ab', 'en', 'itr', 'okr', 'akh']
		codas += ['ek', 'os', 'a', 'at', 'it', 'an', 'is']
	if FOX:
		onset += ['Am', 'In', 'Mit', 'Yuk', 'Hik', 'Ren', 'Kiyo']
		nuclei += [
			'ar', 'ak', 'an',
			'er', 'ek', 'en',
			'ir', 'ik', 'in',
			'or', 'ok', 'on',
			'ur', 'uk', 'un',
			]
		codas += ['u', 'o', 'i', 'oko', 'a']
	return onset, nuclei, codas

def Surphonotactic(genus):
	Initialized("Surphonotactic")
	onset, nuclei, codas  = Phonotactic(genus)
	codas = [
		"us", 'azus',
		]
	return onset, nuclei, codas
