def Names(genus):
	MALE    = "He"    in genus
	FEMALE  = "She"   in genus
	AGENDER = "They"  in genus

	SUBgenus = "Subgenus" in genus

	Names = [
		'Tileon',		'Meryl',		'Ezidas',		'Siargatris',		'Loove',		'Ikat',		'Slacus',		"Tom",		'Uzelax',		"Panthera",		"Feline",		"Felidae",		"Felis",		"Felix",		"Catus",		"Garfield",		"Kitty",		"Salem",		"Boots",		"Simba",		"Nala",		"Tigger",		"Domesticus",		"Catus",		"Miau",		"Kat",		"Katze",		"Gato",		"Gat",		"Mao",		"Kato",		"Katua",		"Chatte",		"Mur",			"Neko",			"Pusi",			"Gata",			"Pisica",		"Maew",		"Kedi",		"Ikati",		"Kiniun",		"Lev",		"Aslan",		"Kedi",		"Singto",		"Lejon",		"Libax",		"Paka",		"Shumba",		"Lav",		"Leona",		"Lev",		"Leu",		"Leo",		"Lew",		"Sera",		"Love",		"Sinha",		"Arslan",		"Sinha",		"Raiona",		"Iljun",		"Singa",		"Sang",		"Aristan",		"Raion",		"Leone",		"Leonessa",		"Oroszlan",		"Sher",			"Liontari",		"Lion",		"Lionne",		"Leono",		"Saja",		"Shizi",		"Tao",		"Sinha",		"Birala",		"Lowin",		"Lowe",		"Leu",		"Acala",		"Felina",		"Neiku",		"Ararga",		"Cazal",		"Jundae",		"Zopar",		"Puma",		"Catopuma",		"Cato",		"Silvestris",		"Leopardus",		"Iniu",		"Uruha",		"Uruah",		"Braccatus",	"Pardalis",		"Tigrinus",		"Lynx",			"Rufus",		"Pantherina",		"Leo","Nubica",		"Persica",		"Pardus",		"Tigris",		"Uncia",		"Igris",		"Persic",		"Atilax",		"Mordax",		"Galerella","Helogale",		"Herpestes","Fuscus",		"Javanicus",		"Urva","Mungos",		"Suricata",		"Crocuta",		"Pantherina",		"Neofelis",		"Smilodon",		"Lynx","Tiger",		"Tigre","Tereon",		"Smilodon",	"Lurus",		"Leopard",		"Jaguar",		"Pardofelis",	"Caracal",		"Serval",		"Kodkod",	"Ocelot",		"Margay","Leopardus","Iberian",		"Bob","Cougar","Cheetah",		"Jubatus",		"Felidae",		"Felinae",		"Atus",		"Bengalensis",		"Chaus","Nigripes",		"Margarita","Bieti",		"Lybica","Silvestris",		"Racal",		"Serval","Margay",		"Ocelot","Oncilla",		"Pampas","Jaguarundi",		"Sunda","Sibala","Sice",		"Chelac",	"Singa",		"Santu",		"Helisa",		"Sisto",		"Catin",		"Miau",			"Mew",			"Niut",		"Nala",		"Simba",		"Mufasa","Scar",		"Sicacu",		"Karaus","Done",		"Sionx","Sinae","Nubi",		"Chal",		"Argala",		"Chatala",		"Sicava",		"Lobax",		"Panthura",		"Silvestris",		"Rocuta",		"Silver",		"Visrio",
		]
	return Names

def Surnames(genus):
	Surnames = [
		'Dentesable',	'Sabertuz',	'Sabertooth',	'Igriz', "Tigric",	"Pride",	"Mane",	"Saber", "Sabertooth",
		]
	return Surnames

def Phonotactic(genus):
	MALE    = "He"    in genus
	FEMALE  = "She"   in genus
	AGENDER = "They"  in genus

	onset  = [
		'Leop',	'Pard',	'Mi',	'Pant',	'Muf',	"Linx",'Pard','Li','Tigr','Lur','Fel','Leop','Oz','Silv','Simb']
	nuclei = [
		'er',	'as',	'on',	'in',	'ard',	'onx','el','ester','igr']
	codas  = [
		'',	"is", 'ez',	'ix',	'al',	'au',	'ex'
		]
	if MALE: codas = [
		'os', 'oxos', 'ixos', 'on', 'oz', 'ox',
		]
	if FEMALE: codas = [
		'as', 'axas', 'ixas', 'ona', 'ax', 'azar', 'iax',
		]
	return onset, nuclei, codas

def Surphonotactic(genus):
	onset, nuclei, codas = Phonotactic(genus)
	codas += [
		'icus', 'aicus', 'eicus', 'iceus',
		]
	return onset, nuclei, codas
