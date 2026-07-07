

def Names(Type):

	MALE    = "Je"    in Type
	FEMALE  = "She"   in Type
	AGENDER = "They"  in Type

	ISLANDER = "Islander"  in Type

	Names = [
		# Agender-neutral from African, Native, Aboriginal origins
		"Amari",	"Aylen",	"Nuru",		"Neon",		 "Sacari", "Zuri",		"Ayan",		"Bati",		"Cheno", 	"Dayani",	"Elun", "Imani",	"Mica",		"Nodin",	"Citali", 	"Nayeli", 	"Alinta", 	"Jarli",	"Bindi", 	"Ayo",		"Badu", 	"Chica",	"Dacari", 	"Eshex", 	"Fola", 	"Cato",		"Lule",		"Moyo",		"Omari",	"Penda",	"Sade", 	"Taye",		"Tumelo", 	"Nixan",	"Tinase",	"Winta",	"Zola",		"Apon",		"Elu",		"Istas", 	"Caya",		"Onida",	"Xania",	"Tacoda",	"Yoki", 	"Zicala", 	"Okalani",	"Camari",	"Jelani", 	"Tinaxe",	"Lelise", 	"Bekizue",	"Ayilen",	"Tandive",	"Ororo", 	"Ocoro",	"Barka",	"Oban",		"Zikon",	"Juma",		"Tariro",	"Cesi",		"Sanyu",	"Mandoro",	"Ayanda", 	"Bule",		"Esina",	"Zuberi",	"Sisay",	"Nokosana", "Onica", 	"Nayasa",	"Azan",		"Malica",	"Mubali",	"Abeni",	"Zawadi",	"Nadir",	"Zanele", 	"Warimu",	"Maco", 	"Yindi",	"Inala",	"Onar",		"Miro",		"Alira", 	"Lowana", 	"Merri", 	"Cona",		"Nimali",	"Akama",	"Elandra", 	"Cali",		"Calani",	"Naledi",	"Dacaray"	"Ubaris",	"Monro",	"Jarli",	"Tarni",	"Naledi",	"Cani",		"Braca",	"Runaco",	"Moyo",		"Cato",		"Amari",	"Aylen",	"Nuru",		"Neon",		"Sacari",	"Zuri",		"Ayan",		"Bati", 	"Cheno", 	"Dayani",	"Elun",		"Imani",	"Mica",		"Nodin",	"Zuri",		"Tarni", 	"Ameyali",	"Citali", 	"Nayeli",	"Alinta", 	"Jarli",	"Bindi",	"Ayo",		"Badu", 	"Chica",	"Dacari", 	"Eshex",	"Fola", 	"Imani", 	"Cato",		"Lule", 	"Moyo",		"Nuru", 	"Omari",	"Penda", 	"Sade",		"Taye",		"Tumelo",	"Zuri",		"Amari",	"Nixan", 	"Tinase", 	"Winta",	"Zola", 	"Aponi",	"Chenoa", 	"Elu", 		"Istas",	"Caya", 	"Mica",		"Nokomis", 	"Onida",	"Xania", 	"Tacoda",	"Yoki", 	"Zicala",	"Okalani",	"Camari", 	"Nuru", 	"Jelani",	"Runaco",	"Tinaxe",	"Lelise",	"Bekizue",	"Ayilen",	"Tandiwe",	"Ororo",	"Ocoro", 	"Barka", 	"Oban",		"Sacari",	"Anan", 	"Zikon",	"Juma", 	"Tariro", 	"Cesi",		"Sanyu", 	"Mandoro",	"Ayanda", 	"Bule",		"Esina",	"Zuberi",	"Sisay",	"Nokosana",	"Onica",	"Aza",		"Malica",	"Mubali", 	"Abeni", 	"Zawadi",	"Nadid",	"Tinaxe", 	"Zanele",	"Warimu", 	"Tarni", 	"Maco",		"Yindi", 	"Inala", 	"Ona",		"Jarli", 	"Miro", 	"Alira",	"Lowana", 	"Merri", 	"Cona", 	"Nimali",	"Akama", 	"Elandra", 	"Cali", 	"Calani",	"Naledi", 	"Dacaray"

		  ]
	if FEMALE:
		Names += [
			"Salali",	"Odina",	"Aylen",	"Onawa",	"Palesa",	"Yuma",		"Xenoa",	"Sajila",	"Tayana",	"Tiva",		"Winona",	"Yoki",		"Zitala",	"Zikala",	"Nayasa",	"Aira",		"Talia",	"Zalia",	"Lowana",	"Onica", 	"Salia",	"Abeni",	"Camara",	"Chenoa", 	"Caya",	"Inala",	"Aberax",	"Asha", 	"Imala",	"Nayeli",	"Sahila",	"Malica",	"Aponi", 	"Cateri",	"Asila",	"Adila",	"Istas",	"Awentia",	"Zahali",	"Allira", 	"Alora",	"Eluna",	"Dayani",	"Abeni",	"Adama",	"Aixa", "Amale",	"Anaya",	"Axanti",	"Ayana",	"Aziza",	"Behati",	"Chinara",	"Deka",		"Dinea",	"Efua", "Eno", 		"Eshe",		"Furaha",	"Jalima",	"Jasina",	"Ifedayo", 	"Ifeoma",	"Imani",	"Isabis",	"Jendayi",	"Camaria", 	"Cesia",	"Cezian",	"Cian",	"Lelise",	"Lesedi",	"Lindie",	"Macena",	"Malica",	"Mandisa",	"Marjani",	"Mabali",	"Mirem", "Muna",	"Nala",	  "Nandi",	"Nila",		"Nacesi",	"Nozana", "Nena",		"Naya",	"Nayasha",	"Obia",	"Odesa",	"Ogechi",	"Okalani",	 "Olamide",	"Onica",	 "Penda",	 "Runaco",	"Sade", "Sacina",	 "Salama",	"Sana",	"Xani",	 	 "Sifo",	"Sisaya",	"Subira",	 "Tandiwe",	"Tinase",	"Dumel",	"Udaca",	 "Ugochi", "Vuyiswa",		 "Winta",	"Yala", "Yejide",	 	"Zahra", "Zanele",	"Zawa",	"Zola",	"Zubaida",	 "Zuala", "Zuri",	"Ariyana",	 "Aponia",		"Chenoah",	"Elaya", "Istas", "Cachina",	 "Caterina",	"Leotie",	"Mitena",			"Nayeli",		 "Sacari",	 			 	 	
			]
	if MALE:
		Names += [
			"Jengo",	"Amarino",	"Malik", 	"Adenan",	"Bonganix",	"Camaru",	"Taje", 	"Mato",		"Ajanu", 	"Tacoda",	"Denal",	"Jarrax",	"Dajalu", 	"Omeo",		"Tavux", 	"Budi",		"Adebayo", 	"Aden",		"Afolabi",	"Akin",		"Amarix", 	"Ananu",	"Azubike", 	"Bajide",	"Baraca",	"Beziel",	"Bongani", 	"Chibuze",	"Chinedu", 	"Chisulo", 	"Dacari",	"Dumisani", "Ekene", 	"Emeka",	"Eshex", 	"Faraji",	"Femi",		"Folami", 	"Gamban", 	"Gatsa",			"Jabib", 	"Jalif", 	"Jamisi",	"Ikena", 	"Imani", 	"Ishac",	"Jabari",	"Jelani", 	"Jengo",	"Camu", 	"Cato", 	"Cayin",	"Camari", 	"Cofi", 	"Cawame",	"Ciwasi", 	"Lezabo", 	"Lumumba",	"Mandel", 	"Masamba", 	"Masego",	"Muana", 	"Meji", 	"Mosi",		"Muamba", 	"Nuru", 	"Obasi",	"Obina", 	"Olux",		"Omari",			"Onekasi", 	"Osagie", 	"Seku",		"Simaba", 	"Isifo", 	"Tafari",	"Taye", 	"Tenday", 	"Tabani",	"Uba", 		"Uche", 	"Umaru",	"Zuberi", 	"Zuri", 	"Abey",			"Aday", 	"Axanu", 	"Atoxi",	"Bizil", 	"Cochise",	"Dacota",	"Elan", 	"Enaya", 	"Etxemin",	"Jalian", 	"Jazun", 	"Jototo",	"Jacey", 	"Citxi", 	"Cohana",	"Macya", 	"Mato", 	"Nodin",	"Ohanzi", 	"Paco", 	"Cuanah",	"Sani", 	"Tacoda", 	"Tasunka",	"Waya", 	
			]
	# Polynesian
	Names += [
			"Lani",		"Macani", "Nalu", "Joku", "Cay", "Moana", "Canoa", "Caleo",		"Ceona", "Liko",        "Ceahi", "Pono", "Lokahi", "Malie",		"Noelani", "Iolana", "Aolani", "Mahina", "Malia", "Calani",		"Lerua", "Caiea", "Ceahicay", "Maliana", "Cawehi", "Mele",		"Jalia", "Capua", "Ceola", "Cahiau",        "Pua", "Janale",	"Lulani", "Lokelani", "Jäheo", "Ululani", "Cäulani", "Anuhea",		"Jokulani", "Cülei",        "Ceone", "Cailani", "Ailani",		"Alana", "Cainalu", "Nahele", "Macoa", "Liko", 	"Mahinay"
				]
	if FEMALE:
			Names += [	"Aiyana", "Tiva",             "Leilani", "Moana",		"Cailani",	"Nohea", "Cealani", "Lani", "Jalia", "Mele", "Noelani", "Ceona",	"Mahina", "Alana", "Pualani", "Malie", "Anela", "Cawehi",	"Capua", "Miliani", "Iolana", "Calea",        "Mahina", "Joekuelëa",	"Lulani", "Anuhea", "Mahealani", "Malia", "Ceahilani",	"Oliana", "Lokelani", "Aolani",        "Jalïa", "Meleana",	"Nalani", "Lerua", "Ululani", "Cäiulani", "Caimana", "Pua",		"Lilia", "Macana",        "Jaukea", "Jïlani", "Mahie", "Napua",		"Cülei", "Aneka", "Noelica", "Palila", "Ceolewa", "Monikela"
				]
	if MALE:
			Names += [
			"Anacin", "Calian", 			"Ceahi", "Canoa", "Cailoa", "Lono", "Nalu", "Ceola", "Caikoa", "Jano", "Pono", "Macaio",            "Camalani", "Cahekili", "Calani", "Janale", "Capono", "Nainoa", "Canaloa", "Cupono", "Ceone", "Maica",            "Palani", "Ikaica", "Macoa", "Cainalu", "Liko", "Cekoa", "Joku", "Cualii", "Caipo", "Caleo",        "Cahiau", "Jäheo", "Jömalu", "Capena", "Macani", "Jolani", "Lokahi", "Caiea", "Nahele", "Jokulani",        "Celeawe", "Canay", "Pacüi", "Janohano", "Calerua", "Tavay", "Taneoa", "Lautoa", "Matiu", "Taunoa", "Cay",  "Citori", "Maji", 

				]

	# maori
	Names += [
            "Aroha", "Cauri", "Nīkau", "Moana", "Rangi", "Vetue", "Manaia", "Awanui", "Rererua", "Pounamu",
            "Jinemoa", "Tawhiri", "Aio", "Coewhay", "Coetuku", "Raukura", "Venua", "Tay", "Cahurangi", "Atarangi",
            "Rangimaria", "Cahica", "Corora", "Tohora", "Manawa", "Jukarere", "Rangiatea", "Rongomay", "Coetahitanga", "Maioha",
            "Pare", "Marama", "Awhina", "Tuarangi", "Jinekura", "Jineway", "Moerangi", "Raukawa", "Poutama", "Raumati",
            "Ruru", "Tawace", "Coemaru", "Whaitiri", "Jekerangi", "Rangipiki", "Cararaina", "Teina", "Ariki", "Coroua"
							]
	if FEMALE:
			Names += [
            "Aroha",		"Jine",			"Moerangi",		"Cahurangi", "Marama",		 "Rangiatea",	 "Conway",		 "Ciriway",		"Jineva",       "Mereana",		"Ataran",		"Raukura",		"Pare",			"Jinet",		"Jinera",		"Refrua",		"Maduica",		"Cirinoa",		"Angahuia",		"Tiare",		"Mosana",		"Watari",		"Manava",		"Jukarere",		"Cadica",		"Coetuku",		"Jinemoa",		"Rangimaria",	"Jineora",		"Jinetay",		"Awhina",		"Manawaora",	"Macere",		"Vetuemarama",	"Cararaina",	"Miriama",		"Pounam",		"Jinekura",		"Jinek",		"Oraco",		"Rangiatea",	"Ayiso", 		"Cotahita",		"Tuaran",		"Jinewaiora",	"Tawari",		"Maioha",		"Rangi",		"Ararangi"
							]
	if MALE:
			Names += [
            "Tane", "Mawi", "Rangi", "Turi", "Vetue", "Jemi", "Tamati", "Anaru", "Cauri", "Tama",          "Manaaci", "Rawiri", "Tahu", "Cahu", "Jaci", "Rongo", "Ariki", "Teina", "Whiti", "Coroua",            "Taneatua", "Whaitiri", "Maru", "Paora", "Joani", "Nīkau", "Taimoana", "Tanehau", "Tipene",             "Raukawa", "Jekerangi", "Tacitimu", "Venua", "Manaia", "Awanui", "Rongomay", "Moerangi", "Teariki", "Tay",            "Poutama", "Tawace", "Raumati", "Taranui", "Johua", "Jenare", "Ruru", "Cawiti", "Cawea", "Tohora"
				]

	# rapanui
	Names += [
            "Mace", "Rano", "Ika", "Moay", "Ahu", "Janga", "Motu", "Anacena", "Rapa", "Vay",            "Jiva", "Paina", "Coro", "Jaoa", "Mahute", "Tupa", "Tiki", "Jiku", "Cave", "Uka",            "Tane", "Tehana", "Matavay", "Vaihu", "Motunui", "Motuiti", "Rapa Nui", "Ana", "Jopu", "Joa",            "Janga Roa", "Ranoka", "Orongo", "Tangata Manu", "Macea", "Tepito", "Nua", "Riri", "Ohiro", "Mahana",            "Tekao", "Tepito", "Ariki",   "Tupahotu", "Roiho", "Jaoa Ngaro", "Umu", "Mahina", "Jare"
								]
	if FEMALE:
		Names += [
            "Vaenga", "Uka Hina", "Vai Heva", "Tuu Hiva", "Tehani", "Tepiri", "Ariiki", "Macea", "Rapaea", "Anamaru",
            "Tujura", "Vajora", "Jinariru", "Vajata", "Nua", "Janga", "Moerani", "Jarekiri", "Ohiro", "Tupahotu",
            "Ranori", "Ahurei", "Anaiti", "Ananui", "Mahina", "Vaihu", "Matavay", "Oto Uru", "Rapa Riri", "Jine Renga",
            "Cororine", "Mahana", "Jinaaro", "Tepahine", "Janga Roa", "Mau Teao", "Jina Moe", "Joahine", "Vajlani", "Riri Hina",
            "Nuacea", "Tiare", "Rapa", "Anorina", "Ana Renga", "Motu Hina", "Rangiva", "Mauhiva", "Tehaninui", "Moaihine", "Jopa"
			]
			
	if MALE:
			Names += [
            "Jotu Matua", "Mace", "Tuu Ko Iho", "Atamu", "Nuku", "Anacena", "Ika", "Moara", "Tupa", "Tangaroa",
            "Urevaiko", "Tepano", "Rano", "Jeki", "Tiki", "Mahute", "Jaoa", "Juki", "Coro", "Matatoa",
            "Tuki", "Uka", "Tava", "Iriti", "Ranoacea", "Toreka", "Timo", "Tane Roa", "Jaray", "Tepito",
            "Atariki", "Rira", "Motuiti", "Motunui", "Angaro", "Tane Nui", "Ahuaci", "Cave", "Jiku", "Tane Kena",
            "Tanata", "Tupahotu",   "Riro", "Corohea", "Paina", "Caiŋa", "Puhi", "Motue", "Umu"
							]

	# filipino
	Names += [
            "Amihan", "Jabagat", "Liwayway", "Tala", "Bituin", "Alon", "Bayani", "Jiraya", "Luntian", "Liwanag",
            "Sicat", "Araw", "Diwa", "Lualhati", "Ligaya", "Maharlica", "Giting", "Sampaguita", "Mutya", "Janan",
            "Dahon", "Buhawi", "Bagani", "Lacandagat", "Maciling", "Gintong", "Silangan", "Canluran", "Timog", "Jilaga",
            "Uliran", "Bantay", "Bughaw", "Cayumanggi", "Puting", "Dalisay", "Lacambini", "Sicatuna", "Sinag", "Duyog",
            "Bituing", "Talaon", "Jiyas", "Marilag", "Maaliwalas", "Jaraya", "Dalisayan", "Jalimuyac", "Mithi", "Sinta"
											]
	if FEMALE:
			Names += [
            "Amihan", "Mayari", "Diwa", "Liwayway", "Tala", "Bituin", "Mutya", "Diwata", "Ligaya", "Lacambini",
            "Marikit", "Dalisay", "Diwatan", "Jiraya", "Jalimuyac", "Lualhati", "Mahinhin", "Macisigya", "Giliw", "Ganda",
            "Maciling", "Sampaguita", "Bulaclac", "Dalisayan", "Duyog", "Janan", "Sicatuna", "Talaaya", "Bathala", "Lacanmaya",
            "Binibini", "Maaliwalas", "Marilag", "Lacambining", "Mithi", "Sinta", "Jiyas", "Sinagtala", "Diwamara", "Maynila",
            "Mutyara", "Bayang", "Liwanag", "Lacanda", "Silahis", "Luningning", "Mahalia", "Gintara", "Dalisayla", "Mayariluna"			]
			
	if MALE:
			Names += [
            "Bayani", "Lacan", "Datu", "Rajah", "Bautista", "Amado", "Macisig", "Dalisay", "Bituin", "Liwanag",
            "Talas", "Alon", "Dagatan", "Jabagat", "Amihan", "Silangan", "Mayumi", "Giting", "Bantay", "Cidlat",
            "Tamaraw", "Macisigro", "Ligayaon", "Buhawi", "Bagani", "Lacandagat", "Macaniog", "Sicat", "Sarmiento", "Rizal",
            "Malacas", "Macisigtao", "Bulawan", "Jiraya", "Jalimuyac", "Maharlica", "Diwataon", "Mahabagin", "Talaon", "Bituinon",
            "Jaraya", "Liway", "Galang", "Mataas", "Bantugan", "Araw", "Dimasupil", "Canluran", "Luntian", "Maciling"
										]



	return Names

def Surnames(Type):
	
	Surnames = [
 		"Teriva",		"Anacena",		"Vainu",		"Tupamot",		"Ranoabu",		"Morpit",		"Mortep",		"Mortet",		"Mortepit",		"Vaicava",		"Tusito",		"Rapari",		"Panika",		"Pinaka",		"Panaka",		"Pinika",		"Motuti",		"Ariva",		"Motun",		"Corojea",		"Ranojiva",		"Janjeva",		"Ranori",		"Rapatan",		"Vajatua",		"Cainuit",		"Anaitu",		"Jinaroa",		"Ranomace",		"Moriva",		"Tepano",		"Ucana",		"Vailani",		"RiriHine",		"Azure",		"TeHopu", 		"Nuroa",		"MahinaKay",	"TaneMotu",		"Cororoa",		"Jivat",		"Lacandula",	"Sicatuna",		"Macaraig",		"Liwanag",		"Maciling",		"Amihanon",		"Bayanihan",	"Lualhati",		"Bantugan",		"Tagumpay",		"Macisig", 		"Dalisan",		"Silanganon",	"Maynila",		"Magsaysay",	"Bagani",		"Mutang",		"Maharli",		"Lacambini",	"Bituinon",		"Calayan",		"Jirayanon",	"Sampaguita",	"Balanga",		"Canluran",		"Luntian",		"Bathala",		"Liway",		"Dalisay",		"Maharlica",	"Macisigon",	"Banaw",		"Bulan", 		"Bituin",		"Catipunan",	"Mabini",		"Lacanda",		"Marikit",		"Talaon",		"Mayari", 		"Galang",		"Amang",		"Tamaraw", 		"Dagohoy",		"Dalisan",		"Gintong",		"Silahis",		"Lacandat", 	"Mizi",			"Bayani",		"Ligaya",		"Mandela",		"Ocoro", 		"Begay", 		"Yarramundi",	"Dajarapi",		"Wilson", 		"Anguyen",		"Bitanga",	"Galager",		"Cumalo",		"Yelotil",		"Junter",		"Gundabuka",	"Jonson",		"Raven",		"Birrera", 		'Lustar',		"Yaramundi",	"Cealorilani",	"Cainoa", 		"Macanui", 		"Nalucay", 		"Caulalani",	"Jokulea", 		"Lanicay", 		"Caimalie",		"Macailani",	"Nalu",        "Ceahiola",	"Mahinacea",	"Lonoica", 		"Cahaleway", 		"Caulana",		"Nolani",		"Calua",	"Leruaona",		"Capualani", "Caonori",		"Maluhia",		"Cailua",		"Mahelani",		"Jaleacala", "Cahelelani",	 "Cawaiola", "Cealani",	"Cekailoa",		"Lonomacay", "Jaikuway",	 "Ceonipua", "Mahinanoa",	"Caimana",		"Ceahipua", "Capuhale",		"Caleohano", "Calaniway",		"Jaliaca",		"Nahelei", "Lanikuhonua",	"Cahele", "Cawailani",		"Cekumu",		"Melerune", "Cahale",	"Manuja",        "Cualoa",		"Jaumea",		"Ceoloria", "Calerua",	"Macaniva",	"Teriki",		"Whaitiri",		"Rangipoe", "Tawhirimatea",	"Angata",        "Rangihau",	 "Jekerangi", "Venuacura",	"Raukawa", "Whanui",        "Angawaca",		"Tepoe", "Vetuerangitia", "Awanui", "Taimoana",		"Rongomay",		"Jineway", "Tevenua", "Mahuta", "Cawiti",		"Jine",	"Hurangi",		"Terangi", "Coetuku", "Jinemoa", "Toyeya",	"Rangira", "Jikurangi",	"Maniato", "Wharepapa", "Angatay",        "Comaru", "Matora",		"Gahere", "Tujoe", "Tewara", "Jinetitama",        "Angariki",	"Waipapa", "Nahau", "Moerangi",		"Whaitua", "Tawhiti",	"Coetahitanga", "Rangitue", "Rangiatea",		"Warecu", "Rangiora",	"Rererua",	"Angamotu", "Tetay",		"Tuwharetoa",	"Jotumatua",	"Macem",	"Rirokainga",		"JangaRoa",		"Motuni",	"VaiHuna",	"Rongo",	"TangataManu",	"RanoKau",	"Matavay",	 					"Mahute",	"Jarehiva",	"Jangaro",	
		]

	ISLANDER = "Islander"  in Type
	if ISLANDER:
		Surnames += [
			"Wonga", 	"Tongariro", 	"Tiuray"
			]

	return Surnames


def Phonotactic(Type):
	prefix  = [
		#   A-  group
		"Aza",	"Ab", "Ad", "Af", "Ag", "Ak", "Al", "Am", "An", "Ar", "As", "At", 	"Al",	"And",
		#   E-  group
		"Eb", "Ed", "Eg", "Ek", "El", "Em", "En", "Er", "Es", "Et",
		#   I-  group
		"Ib", "Id", "Ig", "Ik", "Il", "Im", "In", "Ir", "Is", "It",
		#   O-  group
		"Ob", "Od", "Og", "Ok", "Ol", "Om", "On", "Or", "Os", "Ot",
		#   U-  group
		"Ub", "Ud", "Ug", "Uk", "Ul", "Um", "Un", "Ur", "Us", "Ut",
			]
	fix = [
		#   A-  group
		"Ab", "Ad", "Af", "Ag", "Ak", "Al", "Am", "An", "Ar", "As", "At",
		#   E-  group
		"Eb", "Ed", "Eg", "Ek", "El", "Em", "En", "Er", "Es", "Et",
		#   I-  group
		"Ib", "Id", "Ig", "Ik", "Il", "Im", "In", "Ir", "Is", "It",
		#   O-  group
		"Ob", "Od", "Og", "Ok", "Ol", "Om", "On", "Or", "Os", "Ot",
		#   U-  group
		"Ub", "Ud", "Ug", "Uk", "Ul", "Um", "Un", "Ur", "Us", "Ut",
		]
	sufix  = [
		"a", "e", "i", "o", "u",
		"ar", "en", "un", "ir", "ok", "as", 'o'
		]
	if "she" in Type:
		sufix += ["a", "ana", "ala"]
	return prefix, fix, sufix

def Surphonotactic(Type):
	prefix = [
		"Am", "An", "Ar", "Al", "Af", "Ak",
		"Em", "En", "Er", "El",
		"Im", "In", "Ir", "Il",
		"Om", "On", "Or", "Ol",
		"Um", "Un", "Ur", "Ul",
		'Bac',	'Sol',
				]
	fix = [
		"Am", "An", "Ar", "Al", "Af", "Ak",
		"Em", "En", "Er", "El",
		"Im", "In", "Ir", "Il",
		"Om", "On", "Or", "Ol",
		"Um", "Un", "Ur", "Ul",
		'alan',
		]
	sufix = [
		"an", "am", "ar", "al",
		"en", "em", "er", "el",
		"in", "im", "ir", "il",
		"on", "om", "or", "ol",
		"un", "um", "ur", "ul",
		'anor'
		]


	ISLANDER = "Islander"  in Type
	if ISLANDER:
		prefix  += [
		"Aul", "Oin", "Eas"
			]
		fix += [
		"Aur", "Ois", "Ela"
			]
		sufix  += [
			]

	return prefix, fix, sufix
