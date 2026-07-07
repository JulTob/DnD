'''
inspiration
	- 1001 Nights (Arabian Nights)
	- Silk Route
	- South asia
	- Malasia
	- Filipines
	- Sanskrit
'''

def Names(genus):
	MALE    = "He"    in genus
	FEMALE  = "She"   in genus
	AGENDER = "They"  in genus

	SUBgenus = "Subgenus" in genus

	Names =  []

	if FEMALE:
		Names +=  [
		"Melisanda",	'Soraya', "Badira",		"Zafina",	'Alda',			'Sarahiya',			'Amda',			'Almaz',			'Elisaweta',			"Ikina",			"Akina",			'Aluna',			"Zasa",			"Sanari",			"Azada",			'Rasha',
			]
	if MALE:
		Names += [
		'Sorayo',	'Buzir',	'Rakin',		"Buzad",		'Zajoh',		'Ganoz',		'Sarfirouz',
		]

	Names +=  [
	"Kandar",		"Azan",			'Talin', 		"Ardazam",		'Tandan',		'Kudal','Bacash','Uzadras',	"Amonovix",	'Razava',	'Yamba',	'Bashan',	"Azaja",	"Aldan",	"Zephyr",	"Roshan",	"Azur",	"Soraya",	"Tariq",	"Nuray",	"Marid",	"Kaveh",	"Simurgh",	"Hazar",	"Maysun",	"Firouz",	"Badar",	"Anbar",	"Cyrus",	"Almas",	"Bahar",	"Zahara",	"Nadim",	"Yasmin",	"Zarparan",	"Roshan", 	"Maysun", 	"Nuray", "Samir",	"Soraya", 	"Tazim", 	"Yelda", 		"Zefir",		"Jinane", 		"Azhar", 		"Firouz", 		"Marid", 	"Narjis", 	"Bahir", 	"Laleh", 	"Parvaiz",  	"Shirin", 	"Kamaria", 	"Zumurrud", 	"Bazm", 	"Hayam", 	"Diba", 	"Sahar", 	"Dobby",		"Chal",			"Alsi",	"Ax",	"Pilb",	"Eg",	"Udag",	"Pilsi",	"Pil",	"Amal",	"Valaravanxa",	"Azarid",	"Walajar",	"Rodulfo",	"Aidoingux",	"Azanagi",	"Agila",	"Gainax",	"Selenax",	"Melisanda",	"Radegond",	"Seda",	"Gaxa",	"Amalafrida",	"Duda",			"Wamba",		"Ariux",		"Azarid",		"Gunteric",		"Tanaix",		"Jordanex", "Baduja",	"Braja", "Narin",	"Giso", "Elisaweta", "Raxa",	"Amalgard", "Sunnia",	"Wella", "Aoric", "Aligern",	"Unigild",	"Razaladar", 	"Alsiu",		"Amanal", 		"Dund",	"Megi", "Pinag", "Budan",	"Agala", "Selx", "Gudus",	"Dona", "Bunging",	"Udaler", "Arnensi",	"Ravava", "Wagic",	"Ambanda", "Sellalby",	"Azadusar", "Azaz",	"Walsi", "Nardu",	"Ralaga", 		"Rajar",		"Arida", 		"Doril",		"Rand",			"Azari", 		"Amand", 		"Azawe",		"Azal", 		"Axar", 		"Xavan", 		"Rada",	"Selala", "Galar", "Druzol",	"Azal", "Azar", "Udarn",	"Azava", "Alal", "Elba", "Alil",	"Amaxa", "Azana", "Ralel",	"Amaxa", "Arinele", "Azoba",		"Garag", 		"Axal", 		"Axagi",	"Talala", "Azari",	"Rajma", "Axar",	"Ralan", "Azax",	"Vala",	"Radus",	"Azava",	"Pilax",	"Talxa",		"Azar",			"Azahar",		"Rana",			"Selan",		"Azalsa",		"Chandar",		"Azav",		"Doby",			"Susal",		"Azag",			"Azal",			"Wari",			"Azag",			"Azaril",		"Nadag",		"Azaja",		"Gungi",	"Buda",	"Ralar",	"Udala",	"Elge",	"Azaxar",	"Dris",	"Gana",	"Udar",	"Elida",	"Alad",	"Ravanda",	"Nals",	"Pic",	"Aby",	"Mada",			"Rorna",		"Amba",			"Ardun",		"Azariga",		"Duna",			"Buada",		"Vagi",			"Azava",		"Guna",			"Amal",			"Azav",			"Ralan",		"Ralav",		"Rajad",		"Talsi",		"Amal", 		"Rarid",		"Randa", 		"Amazo",		"Wava", 		"Magus",		"Guna",			"Slay",			"Dasker",		"Kexam",		"Mukert",		"Rensox",		"Xembor",		"Guknag",		"Sabsen",	"Gundobag",	"Burk",	"Azava",	"Zasiki",	"Warishi",	"Gaxamas",	"Amonobic",	'Nasas',		'Firouz',		'Zajur',		'Rissan',		'Zavasan',		'Zavassan',		'Ivermahin',	"Aman",			"Adudu",		'Melil',		'Ivusem',		'Nudu',			'Ralagaz',		'Azak',			'Lafasaz',		'Alakid',		'Alazkar',		'Gukobak',		'Bacazan',		'Aziduroc',		'Azidur',		"Azadar",		'Ajazad',		'Azazad',		'Amardan',		'Kavial',		"Buzak",		'Ajazad',		'Oxariox',		"Agalax",		"Coya",			"Gukakan",		"Gukak",		"Agalaz",		"Basar",		"Bazahar"		'Ivashak',		'Gukakan',		'Arsana',		'Asassar',		'Asazar',		'Azasar',		'Ivajar',		'Ivaj',			'Zafin',		'Fear',			'Lexe',			'Osirinia',		'Alcala',		'Lalex',		'Ikina',		'Zarefa',		'Aladin',		'Alad',			'Addad',		'Sorohar',		'Elisax',		'Aljazar',		'Salassar',		'Salazar',		'Ivassan',		'Zehox',		'Clonk',		'Alajar',		"Amacoya",		"Azariga",		"Ardun",		"Amba",			"Aby",			"Alad",			"Azaxar",		"Azaja",		"Azaril",		"Azarik",		"Azarim",		"Azara",		"Azag",			"Azal",			'Azohan',		"Azag",			"Azav",			"Azals",		'Riseda',		"Azar",			"Azahar",		"Azava",		"Azax",			"Axar",		"Azari",		"Axagi",		"Axal",			"Azoba",		"Arinele",		"Amaxa",		"Azana",		"Amaxa",		"Alil",			"Alal",			"Azava",		"Azar",			"Azal",			"Axar",			"Azal",			"Azawe",		"Amand",		"Azari",		"Arida",		"Azaz",			"Azadusar",		"Ambanda",		"Arnensi",		"Agala",		"Amanal",		"Alsiu",		"Aligern",		"Aoric",		"Amalgard",		"Azarid",		"Ariux",		"Amalafrida",	"Agila",		"Azanagi",		"Aidoingux",	"Azarid",		"Amal",			"Azhar",		"Alco",			"Aldan",		"Anbar",		"Azaja",		"Azur",			"Almas",		"Alsi",			"Ax",			"Azava",		"Amazo",		"Buada",		"Buda",			"Budi",			"Budo",			"Bunging",		"Budan",		"Braja",		"Badua",		"Bazm",			"Bahir",		"Badar",		"Bahar",		"Badira",		"Buzbark",		"Burk",		"Buzok",		"Chandar",		"Cyrus",		"Chal",			"Duna",			"Dris",			"Doby",			"Druzol",		"Doril",		"Dona",			"Dund",			"Duda",			"Dobby",		"Diba",			"Elida",		"Elge",			"Elba",			"Eg",			"Firouz",		"Firouz",		"Gundobag",		"Guknag",		"Gana",			"Gungi",		"Garag",		"Galar",		"Gudus",		"Giso",		"Gunteric",		"Gaxa",			"Gainax",		"Hayam",		"Hazar",		"Jordanex",		"Jinane",		"Kamaria",		"Kaveh",		"Laleh",		"Mada",			"Megi",			"Marid",		"Marid",		"Maysun",		'Zohan',		'Raduza',		"Maysun",		'Zahir',		'Zakir',		'Danarlerna',	'Zajar',		'Aladir',		'Aladin',		'Sandokan',		'Sandukan',		"Nals",			"Nadag",		"Nardu",		"Narin",		"Narjis",		"Nuray",		"Nura",			"Nadim",		"Oxarix",		"Pic",			"Pilax",		"Pinag",		"Pil",			"Pilsi",		"Pilb",			"Parvaiz",		"Render",		"Rorna",		"Ravanda",		"Ralar",		"Rhana",		"Radus",		"Ralan",		"Rajma",		"Ralel",		"Rada",			"Rand",			"Rajar",		"Ralaga",		"Ravava",		"Razaladar",	"Raxa",			"Radegond",		"Rodulf",		"Roshan",		"Roshan",		"Susal",		"Selan",		"Samir",		"Soraya",		"Sabsen",		"Selala",		"Sellalby",		"Selx",			"Sunnia",		"Seda",			"Selenax",		"Sahar",		"Sahin",		"Saheen",		"Shaheen",		"Shirin",		"Soraya",		"Simurgh",		"Talxa",		"Talala",		"Tanaix",		"Tazim",		"Tariq",		"Udar",			"Udala",		"Udarn",		"Udaler",		"Unigild",		"Udag",			"Vagi",			"Vala",			"Valaranx",		"Wari",			"Warishi",		"Wava",			"Walsi",		"Wagic",		"Wella",		"Wamba",		"Walajmar",		"Xembor",		"Xavan",		"Yelda",		"Yasmin",		"Zahir",		"Zephyr",		"Zacodan",		"Zarparan",		"Zahara",		"Zara",			"Zasiki",		"Zumurrud",		"Zephyr",		"Zeshan",		'Zeadurar',		'Zedurar',		'Golzar',		'Shahbaz',		'Bublazar',		'Shimzar',		'Feyzari',		'Mirazakh',		'Nour',			'Farhad',		'Darakun',		'Zimzari',
	]
	return Names

def Surnames(genus):
	Surnames = [
	'Darazib', 'Feykunzar', 'Taralekh', 'Zarshari',	'Samisar', 'Almajar', 'Zajin',	"JuratGum", "JarGirift", "DeewarBargasht", "NaqshaKhamosh", "ShoelGard",	"MakkarRubah", "ZirakHeela", "MarZirak", "ZagKhafi", "GhuroobHeela",	"GhahrPinhan", "KhumbiAsrar", "FanousQamar", "BedehSarsabz", "NajmKhamush",	"NezahTond", "AtashKhashm", "GorgShoja", "DandanShekast",	"SayaZirak", "RahnawardPinhan", "HamiQamar", "SareqKhamosh",	"NaqshaGumshuda", "LaghzidanZulmat", "MozSor", "ShalwarGiriftar", "AjeebLahza",    "JannatJasban", "JaratJadid", "ShikanShalwar", "LaghzanLayl", "MozMashhoor",    "KamandKhafif", "Gumgayab", "Gargulchar",    "MakkarMisr", "ZirakZarafshan", "MarMakhfi", "SayeSor", "RahzaniRoshan",    "Hilazar", "Najnavan",    "FanousFalak", "NajmNazneen", "BedehBahari", "KhumbiKhalvat", "GuleGardish",    "SholehShabnam", "RukhRavshan", "NasimNoor",    "GorgGazandeh", "NezahNabard", "ShikanShamsheer", "DandanDahan",    "AtashAzbak", "TufanTond", "TarikTahkim",    "SayaSokoot", "RahnawardRoozegar", "HamiHijar", "DhilDarvazeh",    "FanousFanaa", "ZaribZulmat", "BazmBayaban",    "LaghzanLazeez", "ShikanShanba", "MozMazhool", "DeewarDehkaal",    "KamandKhamosh", "GulGardoon", "GarmGhulghula"		'Shimzilar',		'Fizbanar',		'Tahlazar',		'Mirazakh',		'Feybari',		'Nimzarak',		'Zinrazib',		'Juzafar',		'Taralikh',

	"Mahsavand",
	"Sorheda",  # (Redshadow; 'Sor' = red, 'heda' = echo, shadow)
	"Sitarkhami",  # (Starwhisper; 'Sitar' = star, 'khami' = whisper, soft sound)
	"Shabhatan",  # (Nightflame; 'Shab' = night, 'hatan' = flame or blaze)
	"Barqtab",  # (Thunderstrike; 'Barq' = lightning, 'tab' = shine, strike)
	"Sayejooyan",  # (Shadowfang; 'Saye' = shadow, 'jooyan' = seekers)
	"Noorspark",  # (Brightspark; 'Noor' = light, 'spark' = same in Persian)
		# Arabic-inspired names
	"Qamarrahil",  # (Moonclan; 'Qamar' = moon, 'rahil' = travelers or nomads)
	"Thilalhamra",  # (Redshadow; 'Thilal' = shadows, 'hamra' = red)
	"Najmusalim",  # (Starwhisper; 'Najm' = star, 'salim' = peaceful or quiet)
	"Laylansar",  # (Nightflame; 'Layl' = night, 'ansar' = flame, burning ember)
	"Rahadkarim",  # (Thunderstrike; 'Rahad' = thunder, 'karim' = powerful, noble)
	"Dhilwalak",  # (Shadowfang; 'Dhil' = shadow, 'walak' = fang)
	"Bariqsan",  # (Brightspark; 'Bariq' = flash, sparkle, shine)

	# Proto-Language (Ancient, mixed Middle Eastern tone)
	"Mahyrdara",  # (Moonclan; 'Mahyr' = moon, 'dara' = belonging to or of clan)
	"Hamrashar",  # (Redshadow; 'Hamra' = red, 'shar' = twilight or shade)
	"Nisrith",  # (Starwhisper; 'Nisr' = celestial or lofty, 'rith' = murmur)
	"Shafarith",  # (Nightflame; 'Shafa' = healing light, 'rith' = flame)
	"Raqdar",  # (Thunderstrike; 'Raq' = storm, 'dar' = bearer or wielder)
	"Sayadan",  # (Shadowfang; 'Saya' = shadow, 'dan' = tooth, sharp edge)
	"Norglim",  # (Brightspark; 'Nor' = light, 'glim' = flicker, ember)
	"Qamarzan",  # Qamar = Moon, Zan = people/tribe
	"Zillesorkh",  # Zill = shadow, Sorkh = red
	"Soroushesitar",  # Soroush = heavenly voice, Sitar = star
	"Sholeheshab",  # Sholeh = flame, Shab = night
	"Barghearaz",  # Bargh = lightning, Araz = thunder
	"Dandanezill",  # Dandan = fang, Zill = shadow
	"Shararehroshan",  # Sharareh = spark, Roshan = bright
	"Barfnaal",  # Barf = frost, Naal = claw
	"Jomarehatash",  # Jomareh = ember, Atash = fire
	"Dilevahsh",  # Dil = heart, Vahsh = wild
	"Rakhshetufan",  # Rakhsh = steed, Tufan = storm
	"Chubetarik",  # Chub = wood, Tarik = dark
	"Sangebarq",  # Sang = stone, Barq = glimmer/lightning
	"Badenoghre",  # Bad = wind, Noghre = silver
	"Soroushesholeh",  # Soroush = voice/whisper, Sholeh = flame
	"Sayeetond",  # Saye = shadow, Tond = swift
	"Gozebarf",  # Goz = bite, Barf = frost
	"Zilleqamar",  # Zill = shadow, Qamar = moon
	"Dandanesitar",  # Dandan = claw, Sitar = star
	"Nasimeshab",  # Nasim = breeze, Shab = night
	"Bargeroshan",  # Barg = leaf, Roshan = bright
	"Tighekhar",  # Tigh = blade, Khar = thorn
	"Kamandezill",  # Kamand = pounce/snare, Zill = shadow
	"Atashebarq",  # Atash = fire, Barq = spark/glimmer
	"Payetond",  # Pay = foot, Tond = swift
	"Barghedaryaft",  # Bargh = thunder/lightning, Daryaft = clap
	"Qamaretarik",  # Qamar = moon, Tarik = dark
	"Tufanejomareh",  # Tufan = storm, Jomareh = ember
	"Shararehevahsh",  # Sharareh = spark, Vahsh = wild
	"Zillebarf",  # Zill = shadow, Barf = frost
	"Nureqamar",  # Nur = light, Qamar = moon
	"Nuresitar",  # Nur = light, Sitar = star
	"Pareshab",  # Par = wing, Shab = night
	"Qamareroshan",  # Qamar = moon, Roshan = bright
	"Bargezill",  # Barg = leaf, Zill = shadow
	"Parebarq",  # Par = wing, Barq = sparkle/lightning
	"Zarbetond",  # Zarb = strike, Tond = swift
	"Bargeesedayeh",  # Barg = leaf, Sedayeh = thunder/sound
	"Sholehetarik",  # Sholeh = flame, Tarik = dark
	"Bargeomareh",  # Barg = leaf, Jomareh = ember
	"Mahsavand",  # Moonclan: Mah = moon, savand = seekers
	"Sorheda",  # Redshadow: Sor = red, heda = shadow/echo
	"Sitarkhami",  # Starwhisper: Sitar = star, khami = soft sound
	"Shabhatan",  # Nightflame: Shab = night, hatan = flame
	"Barqtab",  # Thunderstrike: Barq = lightning, tab = shine
	"Sayetandan",  # Shadowfang: Saye = shadow, tandan = fang/tooth
	"Noorsho'leh",  # Brightspark: Noor = light, sho'leh = spark/flame
	"Yakhpanja",  # Frostclaw: Yakh = frost/ice, panja = claw
	"Atashnamar",  # Emberglow: Atash = fire, namar = shimmer
	"Vahmdel",  # Wildheart: Vahm = untamed/wild, del = heart
	"Tofangard",  # Stormrider: Tofan = storm, gard = wanderer
	"Tarikdarakht",  # Darkwood: Tarik = dark, darakht = tree
	"Barqstoneh",  # Glimmerstone: Barq = lightning, stoneh = shining stone
	"Simbar",  # Silverwind: Sim = silver, bar = wind
	"Sho'lehzan",  # Flamewhisper: Sho'leh = flame, zan = whisperer
	"Sayesari'",  # Swiftshadow: Saye = shadow, sari' = swift
	"Yakhkhand",  # Frostbite: Yakh = frost, khand = bite
	"Mahsaye",  # Moonshadow: Mah = moon, saye = shadow
	"Sitarklaw",  # Starclaw: Sitar = star, klaw = claw
	"Shabnasim",  # Nightbreeze: Shab = night, nasim = breeze
	"Noorbargh",  # Brightleaf: Noor = light, bargh = leaf
	"Kharezhar",  # Thornblade: Khar = thorn, ezhar = blade
	"Sayebarkh",  # Shadowpounce: Saye = shadow, barkh = leap
	"Sharkhsho'leh",  # Sparklefire: Sharkh = spark, sho'leh = fire
	"Saripa",  # Swiftfoot: Sari' = swift, pa = foot
	"Barqdad",  # Thunderclap: Barq = lightning, dad = strike
	"Tarikmah",  # Darkmoon: Tarik = dark, mah = moon
	"Atashtofan",  # Emberstorm: Atash = fire, tofan = storm
	"Vahmsho'leh",  # Wildspark: Vahm = wild, sho'leh = spark
	"Yakhsaye",  # Frostshadow: Yakh = frost, saye = shadow
	"Mahbarq",  # Moonlight: Mah = moon, barq = light
	"Sitarnor",  # Starlight: Sitar = star, nor = light
	"Shabbaz",  # Nightwing: Shab = night, baz = falcon/wing
	"Noormah",  # Brightmoon: Noor = light, mah = moon
	"Sayebargh",  # Shadowleaf: Saye = shadow, bargh = leaf
	"Sharkhbal",  # Sparklewing: Sharkh = spark, bal = wing
	"Sarizan",  # Swiftstrike: Sari' = swift, zan = strike
	"Barqbargh",  # Thunderleaf: Barq = lightning, bargh = leaf
	"Tariksho'leh",  # Darkflame: Tarik = dark, sho'leh = flame
	"Atashbargh",  # Emberleaf: Atash = ember/fire, bargh = leaf

	# Arabic-inspired names
	"Qamarrahil",  # Moonclan: Qamar = moon, rahil = travelers
	"Thilalhamra",  # Redshadow: Thilal = shadows, hamra = red
	"Najmusalim",  # Starwhisper: Najm = star, salim = peaceful
	"Laylansar",  # Nightflame: Layl = night, ansar = flame
	"Rahadkarim",  # Thunderstrike: Rahad = thunder, karim = powerful
	"Dhilwalak",  # Shadowfang: Dhil = shadow, walak = fang
	"Bariqsan",  # Brightspark: Bariq = spark, san = brilliance
	"Jalidasar",  # Frostclaw: Jalid = ice, asar = claw
	"Niranbahij",  # Emberglow: Niran = flames, bahij = glowing
	"Wahshiqalb",  # Wildheart: Wahshi = wild, qalb = heart
	"Asifrahil",  # Stormrider: Asif = storm, rahil = traveler
	"Dhilghabah",  # Darkwood: Dhil = shadow, ghabeh = forest
	"Bariqhijar",  # Glimmerstone: Bariq = sparkle, hijar = stone
	"Fiddareeh",  # Silverwind: Fiddah = silver, reeah = wind
	"Shularam",  # Flamewhisper: Shu'la = flame, ram = whisper
	"Dhilsaree",  # Swiftshadow: Dhil = shadow, saree = swift
	"Jaliddagh",  # Frostbite: Jalid = frost, dagh = bite
	"Qamardhil",  # Moonshadow: Qamar = moon, dhil = shadow
	"Najmwalak",  # Starclaw: Najm = star, walak = fang
	"Laylnasr",  # Nightbreeze: Layl = night, nasr = breeze
	"Bariqqasd",  # Brightleaf: Bariq = sparkle, qasd = leaf
	"Shawksoof",  # Thornblade: Shawk = thorn, soof = edge
	"Dhilaqafz",  # Shadowpounce: Dhil = shadow, aqafz = leap
	"Sharaqnar",  # Sparklefire: Sharaq = spark, nar = fire
	"Saree'kadam",  # Swiftfoot: Saree' = swift, kadam = foot
	"Rahadqat",  # Thunderclap: Rahad = thunder, qat = strike
	"Layldhil",  # Darkmoon: Layl = night, dhil = shadow
	"Niranasif",  # Emberstorm: Niran = fire, asif = storm
	"Wahshibariq",  # Wildspark: Wahshi = wild, bariq = spark
	"Jaliddhil",  # Frostshadow: Jalid = frost, dhil = shadow
	"Qamarbariq",  # Moonlight: Qamar = moon, bariq = light
	"Najmnor",  # Starlight: Najm = star, nor = light
	"Layltiyar",  # Nightwing: Layl = night, tiyar = bird/wing
	"Bariqamar",  # Brightmoon: Bariq = light, qamar = moon
	"Dhilwaraq",  # Shadowleaf: Dhil = shadow, waraq = leaf
	"Sharaqjanah",  # Sparklewing: Sharaq = spark, janah = wing
	"Saree'harb",  # Swiftstrike: Saree' = swift, harb = strike
	"Rahadwaraq",  # Thunderleaf: Rahad = thunder, waraq = leaf
	"Laylshu'la",  # Darkflame: Layl = night, shu'la = flame
	"Niranwaraq",  # Emberleaf: Niran = flame, waraq = leaf
	]
	return Surnames

def Phonotactic(genus):
	prefix = [
		'Az',	'Azak',		'Agam',		'Ajad',	'Ard',	'Alak', 'Alah',	'Alm',	'Akin',	'Amr',	'Am',	'Az',  'Al',	'Az',
		'Baz',		'Bacan',	'Buz',		'Bac',
		'Coyaw',	'Cel', 		'Cal',
		'Gukal',	'Gaz',		"Guk",
		'Elis',
		'Fe',
		'Ikin',	'Iv',
		'Jus',
		'Laf',
		'Mel',
		'Nus',	'Nud',
		'Oxar',
		'Ralaf',	'Ron',
		'Selar', 	'Sam', 	'Shat', 'Sor',	'San',	'Sor',	'Sar',
		'Tal', 		'Tariy',
		'Udap',
		'Wal',
		'Xem',
		'Zeph',	'Zaf',		'Zaj', 	'Zeh',
		]
	fix = [
		'',
		'ak', 	'ash', 'ass', 'aj', 'ad',
		'ef',
		'id',
		'oh',	'ob',
		'ar', 'al', 'in', 'az', 'am', 'ir', 'or', 'er', 'um', 'ul',
		'is', 'ur', 'on', 'im',
		]
	suffix = [
		'an', 'a',  'an', 'ar', 'ar', 'ak',
		'ir', 'ir',
		'oc',
		'ur',
		'in', 'ad', 'am', 'is', 'or', 'ul',
		'im', 'id', 'az', 'on', 'as', 'as',
		'an', 'ar', 'ak', 'ir', 'oc', 'ur',
		'a'
		'', '', '' , '']
	return prefix, fix, suffix


def Surphonotactic(genus):
	MALE    = "He"    in genus
	FEMALE  = "She"	  in genus
	AGENDER = "They"  in genus
	# 'Mah' = Moon
	# "Qamar"=  (Moon in Arabic)

	prefix = ['Mah', 'Ban',	'Bin',	'Nab', 'Min',]
	fix = []
	# 'savand' = seekers or bound to)
	suffix = ['savand']

	if MALE:
		prefix += [
			'Ibn',
			]
	if FEMALE:
		prefix += [
			'Bint',
			]
	prefix += [
		'Al',    "Mah", "Qamar", "Sor", "Hamra", "Sitar", "Najm", "Shab", "Layl", "Barq", "Raad",	 'Zan', 'Tar', 'Bel', "Sar", 'Shim', 'Dar', 'Rin', 'Min', 'Al', 'Az', 'Fey',
	]
	fix += [
	"Fey",	'Zar',	'Tar',	'Dar', "zan", "darak", "rahil", "jooyan", "ansar", "bargh", "walak", "panja", "qalb", "del", "tandan", "nasim", "khami", "rith", "dara", "san", "bahij", "hijar", "dan", "asif", "shar", "rosh", "bahram", "nimr", "sang", "alth", "rim", "balh",
	'Mah', "Mah", "Qamar", "Sor", "Hamra", "Sitar", "Najm", "Shab", "Layl", "Barq", "Ra'ad", "Dhil", "Saye", "Noor", "Jalid", "Yakh", "Atash", "Niran", "Wahm", "Wahshi", "Tofan", "Asif", "Tarik", "Bariq", "Sim", "Fiddah", "Sho'leh", "Sharaq", "Sari'", "Zud", "Hila", "Anwar", "Mehr",
	"Dhil", "Saye", "Noor", "Jalid", "Yakh", "Atash", "Niran", "Wahm", "Wahshi",
	"Tofan", "Asif", "Tarik", "Bariq", "Sim", "Fiddah", "Sho'leh", "Sharaq", "Sari'", "Zud",

		"zan", "darak", "rahil", "jooyan", "ansar", "bargh", "walak", "panja", "qalb",
	"del", "tandan", "nasim", "khami", "rith", "dara", "san", "bahij", "hijar",
	"dan", "asif", "shar",
		'Mah', 'Shab', 'Noor', 'Barq', 'Qamar', 'Layl',  'Dhil', 'Raad',
		'Hamra', 'Nis', 'Raq', 'Saya', 	'savand',
	"zan",  # (Person who does something: e.g., flame-whisperer, Persian)
	"darak" , # (Tree/Wood, Persian)
	"rahil" , # (Traveler, Arabic)
	"jooyan" , # (Seeker, Persian)
	"ansar" , # (Helper or supporter, Arabic; poetic sense of companion to the flame or storm)
	"bargh",  # (Lightning or leaf, Persian and Arabic)
	"walak" , # (Fang, Arabic)
	"panja",  # (Claw, Persian)
	"qalb",  # (Heart, Arabic)
	"del",  # (Heart, Persian)
	"tandan",  # (Tooth/Fang, Persian)
	"nasim",  # (Breeze, Arabic and Persian)
	"khami",  # (Soft sound/Whisper, Persian)
	"rith",  # (Invented: murmur or echo, inspired by Proto-Arabic)
	"dara",  # (Belonging to, Persian)
	"san",  # (Brilliance or gleam, Arabic and Persian)
	"bahij",  # (Radiant, glowing, Arabic)
	"hijar",  # (Stone, Arabic)
	"dan",  # (Tooth, Proto-Arabic/Persian hybrid)
	"asif",  # (Storm-bringer, Arabic)
	"shar",  # (Shade, Persian/Proto-Arabic hybrid)
			'jooyan', # (searchers),
			'khami', # (soft sound),
			'tab', # (shine).
			'rahil',  #(travelers),
			'walak', # (fang),
			'salim', # (peaceful),
			'karim', # (noble).
			'rith', # (whisper),
			'shar', # (shade),
			'dan', # (tooth),
			'glim', # (flicker).
			'Sor', 'Sitar', 'Shab',
			'Barq', 'Saye', 'Noor', 'Qamar', 'Thilal',
			'Najm', 'Layl', 'Raad', 'Dhil', 'Bariq',
			'Mayir', 'Hamra', 'Nisr',  'Shafa', 'Raq',
			'Saya',  'Nor',  'Qamar', 'Zill', 'Dil',
	"Mah" , # (Moon in Persian)
	"Sor",  # (Red in Persian)
	"Hamra",  # (Red in Arabic)
	"Sitar",  # (Star in Persian)
	"Najm",  # (Star in Arabic)
	"Shab",  # (Night in Persian)
	"Layl",  # (Night in Arabic)
	"Barq",  # (Thunder in Arabic and Persian)
	"Rahad",  # (Thunder in Arabic)
	"Dhil",  # (Shadow in Arabic)
	"Saye",   # (Shadow in Persian)
	"Noor",   # (Bright/Light in both Persian and Arabic)
	"Jalid",   # (Frost/Ice in Arabic)
	"Yakh",   # (Frost/Ice in Persian)
	"Atash" ,  # (Fire/Ember in Persian)
	"Niran",   # (Flame/Fire in Arabic)
	"Wahm",   # (Wild/Untamed in Persian)
	"Wahshi",   # (Wild in Arabic)
	"Tofan",   # (Storm in Persian)
	"Asif" ,  # (Storm in Arabic)
	"Tarik" ,  # (Dark in Arabic and Persian)
	"Bariq" ,  # (Glimmer/Light in Arabic)
	"Sim" ,  # (Silver in Persian)
	"Fiddah",   # (Silver in Arabic)
	"Sholeh",   # (Flame in Persian)
	"Sharaq" ,  # (Spark/Sparkle in Arabic)
	"Sari",   # (Swift in Arabic)
	"Zud",  # (Swift in Persian)
			]
	suffix  += [
	'dara', 'shar', 'rith', 'dar', 'dan', 'glim', "savand", "khaneh", "tayfa", "nazar", "var", "zan", "gard", "rah", "ansar", "baz", "harb", "dar", "ram", "jooyan", "esh", "un", "darakht", "hijar", "reeh", "sho'leh", "nar", "bargh", "janah", "khosh",
	'Zan', 'Sorkh',     "savand", "rahil", "jooyan", "heda", "khami", "tandan", "tab", "bal", "ansar",
	"darakht", "hijar", "reeh", "sho'leh", "nar", "kadam", "bargh", "janah", "harb",
	"sari'", "zud",
	'kun',	'azib',	'alekh', 'mir', 'ar', 'i', 'akh', 'zar',
	'hamra',  'salim', 'ansar', 'karim' , 'walak',
	'vand', 'san', 'dara', 'rahil', 'ansar', 'san', 'dar', 'ith', 'lim',
	'savand', 'heda',  'khami', 'hatan', 'tab', 'jooyan',
	'rahil',
	"savand",  # (Seeker, Persian; "of clan" poetic twist)
	"rahil",  # (Nomad or traveler, Arabic)
	"jooyan",  # (Seekers, Persian)
	"heda",  # (Echo, shadow, Persian)
	"khami",  # (Soft sound or whisper, Persian)
	"tandan",  # (Tooth or fang, Persian)
	"tab",  # (Shine or strike, Persian)
	"bal",  # (Wing, Persian)
	"ansar",  # (Supporter, Arabic; poetic for rider or companion)
	"darakht",  # (Tree/Wood, Persian)
	"hijar",  # (Stone, Arabic)
	"reeh",  # (Wind, Arabic)
	"sholeh",  # (Flame, Persian)
	"nar",  # (Fire, Arabic)
	"kadam",  # (Foot, Arabic)
	"bargh",  # (Leaf or lightning, Persian and Arabic)
	"janah",  # (Wing, Arabic)
	"harb",  # (Strike or war, Arabic)
	"sari",  # (Swift, Arabic)
	"zud",  # (Fast, Persian)
	]

	return prefix, fix, suffix
