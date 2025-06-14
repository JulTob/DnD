'''
Names for Dragons
Inspirations
	- Dragons (RL)

'''
def Names(Type):
	MALE    = "He"    in Type
	FEMALE  = "She"   in Type
	AGENDER = "They"  in Type

	SUBTYPE = "Subtype" in Type

	Names = [
			"Locked",			"Xinlong",			"Bons",				"Pikachu",			"Pikax",			"Dragonite",		"Drudigon",	"Fraxure",	"Haxorus",	"Axew",	"Dratini",	"Dragonair",	"Bagon",	"Selgon",	"Axew",	"Charmander", "Charmaleon", "Charizard",	"Pikachu",	"Picaxu",	"Pikaxu",	'Oshu',			'Kante',			'Serkad',			'Totomit',			'Entarak',			"Meganlon",			"Megenlon",			'Oxariox',			'Xiaolong',			'Xianlong',			'Wenlong',			'Uriuu',			'Tayland',			'Tatsuzo',			'Tatsuyuki',		'Tatsuto',			'Tatsumichi',			'Tatsuru',			'Tatsumi',			'Tatsuma',			'Tatsuki',			'Tatsuhisa',			'Tatsuhiko',			'Tatsuakira',			'Tatsuemon',			'Tatsue',			'Tatsuako',			'Tatsuaki',			'Tatsu',			'Takeru',			'Takayoshi',			'Solontu',			'Shulong',			'Shulgan',			'Sholontu',			'Shiriu',			'Riuuichi',			'Riuugo',			'Riuto',			'Riutsuki',			'Riutaro',			'Riusei',			'Riumi',			'Riuko',			'Riuko',			'Riujin',			'Riujiro',			'Riuhito',			'Ryohei',			'Ryouji',			'Ryoma',			'Riuhei',			'Riuhiko',			'Riuha',			'Rhaenyra',			'Qionglong',			'Pendragon',		'Monagrong'			'Miruku',			'Mireu',			'Menglong',			'Mir',				'Meguro',			'Mederu',			'Lucerys',			'Loung',			'Longyue',			'Longying',			'Longyao',			'Longmei',			'Longyan',			'Longhua',			'Longfei',			'Longcui',			'Longbei',			'Linlong',			'Lingormr',			'Leliana',			'Lindorm',			'Lilong',			'Kisara',			'Khuzaimah',		'Kayda',			'Jiyong',			'Jinyong',			'Jaxom',			'Huilong',			'Hiccup',			'Honalee',			'Helaena',			'Tatsugo',			'Hakuriu',			'Hailong',			'Eltanin',			'Dreki',			'Drakul',		'Dragon',			'Nugamba',			'Dracaena',			'Draca',			'Corypheus',			'Corlys',			'Cipactonal',			'Chinglai',			'Alicent',			'Riuuichirou',		'Aemond',			'Boremund',			'Chinglai',			'Seiriu',			'Sarkan',			'Zilong',			'Longxue',			'Riuya',			'Zhenlong',			'Riuusuke',			'Zaj',			'Yunlong',			'Longxing',			'Yuelong',			'Yichen',			'Yongju',			'Yongjin',			'Riuma',			'Riuki',			'Yongbok',			'Yinglong',			'Brugmo',			'Longxiao',			'Yasutatsu',		'Yilong',			'Yanlong',			'Xingchen',			'Zhulong',			'Tatsuya',			'Tatsuo',			'Seokjin',			'Riunosuke',			'Huanglong',			'Longwang',			'Chen',			'Qinglong',			'Riu',			'Riuji',			'Long',			'Ejder',			'Drake',			"Draco",			"Dracul",			"Dracu",			"Astrit",			"Dromoka",			'Dunve',			'Adjet',			'Nafabal',			"Jade",				"Agumon",			"Akra",				"Among",			"Amari",			"Akra",			"Arava",			"Arjan",			"Ancalagon",			"Adrex",			"Arjan",			"Azax",			"Avilar",			"Amoritatu",			"Ange",			"Anlong",			"Bri",			"Bathesh",			"Bons",			"Buraki",			"Batan",			"Bomon",			"Baxilia",			"Bowser",			"Biri",				"Burana",			"Bangol",			"Balerion",			"Balasar",			"Balasar",			"Bangak",			"Banlon",			"Baishe",			"Braveheart",			"Boyan",			"Cegu",			"Cthulhu",			"Celintess",			"Cong",			"Corlias",			"Chonglong",			"Darron",			"Dithura",			"Draco",			"Diarrin",			"Drong",			"Dirk",				"Dudra",			"Dalong",			"Dulcy",			"Draco",			"Dirgun",			"Durang",			"Dranges",			"Drogon",			"Donar",			"Duan",			"Daemon",			"Dedalon",			"Daldrat",			"Dikynth",			"Dangon",			"Dulong",			"Drago",			"Dracul",			"Drake",			"Dungan",			"Danshi",			"Drodon",			"Dangon",			"Danglon",			"Dishe",			"Duanlong",			"Dalong",			"Duanlong",			"Dunlon",			"Dunlin",			"Errol",			"Eldrax",			"Endriago",			"Faongu",			"Fenga",			"Falorun",			"Fanlil",			"Fangl",			"Fanlong",			"Fadirax",			"Faranth",			"Firnen",			"Falong",			"Felong",			"Fadron",			"Fin",			"Fang",			"Foom",			"Festus",			"Fafnir",			"Feng",				"Fatu",				"Frode",			"Fury",				"Falkor",			"Falond",			"Fenglon",			"Feilian",			"Goro",			"Gargax",			"Gong",			"Ghidorah",			"Goulong",			"Glaurung",			"Goulong",			"Gouteng",			"Guteng",			"Haku",			"Heskan",			"Houshen",			"Huarran",			"Heilong",			"Heilon",			"Hung",				"Heronga",			"Hungrig",			"Heilong",			"Hesh",				"Heshuan",			"Henia",			"Honshu",			"Hudran",			"Haolian",			"Haixin",			"Hanlong",			"Haiya",			"Hongteng",			"Heiteng",			"Heilian",			"Huanlong",			"Heilong",			"Houlong",			"Huashen",			"Heixin",			"Huanxiong",			"Icefyre",			"Ildrex",			"Igneel",			"Iglo",				"Juma",				"Jaxi",				"Jinglong",			"Julong",			"Julivert",			"Jinlong",			"Jakelong",			"Kava",			"Katla",			"Komodo",			"Krivo",			"Kaladan",			"Kerkad",			"Kriv",			"Kazul",			"Kurasi",			"Kiritatu",			"Kozuki",			"Kadana",			"Kava",			"Kaido",			"Kongotu",			"Longur",			"Lao",				"Lanitua",			"Lulong",			"Laolong",			"Langlong",			"Laoshe",			"Laotze",			"Laolong",			"Manlong",			"Meraxes",			"Maheng",			"Marvur", "Meraxes",			"Mehen",			"Maxiong",			"Megatron",			"Merleng",			"Mushu",			"Megren",			"Maleficent",			"Mushu",			"Malong",			"Mulong",			"Moon",		"Nala",			"Norbert",			"Nuarozi",			"Nala",				"Neceron",			"Niaolong",			"Nailong",			"Orress",			"Oresi",			"Oilux",			"Porunga",			"Patrin",			"Pixrin",			"Panyan",			"Pushe",			"Qilong",			"Rensen",			"Rengax",			"Rente",			"Raiana",			"Rezena",			"Ridley",			"Relong",			"Saphira",			"Savara",			"Sora",				"Surina",			"Shugeng",			"Sitece",			"Sisu",				"Shenron",			"Saphira",			"Shanteng",			"Shanten",			"Simotatu",			"Shengan",			"Shenglon",			"Smaug",			"Sora",			"Shubei",			"Shilong",			"Senlong",			"Tureol",			"Torin",			"Tido",			"Tuange",			"Torin",			"Totomitatu",			"Tonloong",			"Toothless",		"Tiamat",			"Tuang",			"Thorn",			"Tatian",			"Tuling",			"Tulong",			"Tianshe",			"Valorean",			"Viserion",			"Vhagar",			"Vermitrax",			"Vesa",			"Whedon",			"Wadjet",			"Wufu",			"Wuxiong",			"Xuelian",			"Xailan",			"Xulong",			"Xorrad",			"Xaten",			"Xur",			"Xingteng",			"Xuanshe",			"Yuang",			"Yurran",			"Yanglong",			"Yangling",			"Yurilo",			"Yuteng",			"Yulong",			"Yinshe",			"Yunlong",			"Yuanshen",			"Yunshen",			'Zudo',			'Zuko',			'Ozai',			"Zizui",			"Zog",			"Zudonis",			"Zhiya",			"Darrow",
			]

	if FEMALE:
		Names += [
			'Talia',
			]
	return Names

def Surnames(Type):
	Surnames = ["Long", "Tze", 'Jingralong', "Zahilong",		'Jinlong',]
	return Surnames

def Phonotactic(Type):
	prefix  =  [
		'Jar','Brak','Kriv','Dun','Drac',		'Zurk','Esp', 'Drom', 'Drak', 'Riuc',		'Riuy', 'Tats', 'Dran', 'Drant', 'Kant'
		]
	fix = [
		'et','irk',  'ar',]
	suffix  =  [
		'onheart', 'ulux',		 'oka'
		]
	return prefix, fix, suffix

def Surphonotactic(Type):
	prefix = ["F", "Put", "H", "Tat", "Zand", "Miz", "Tats", "T"]
	fix = ["", "", "", "", "", "", "", "", "", "", "", "", "",
		"ak", "ait", "ouj"	]
	suffix  = [
		"utsu", "ong", "uo", "i", "ai", "a", "u",
		'atze', "etze",	"itze",	"otze", 'otze',  'ilin',  'odao',  'utao', "utze",
		'ilon', 'inlong', 'ulong','along','elong','ilong', 'olong',
		'atsue', 'ue',
		]
	return prefix, fix, suffix
