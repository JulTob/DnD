def Names(Type):

    Names = [
        'Chloe',	"Alisa",	'Alize',	'Exa',		'Peta',		'Tera',        'Giga',		'Mega',		'Kilo',		'Hecto',	'Deca',        'Uni',		'Unit',		'Deci',		'Centi',	'Mili',        'Micro',	'Nano',		'Pico',		'Exar',		'Petar',        'Terar',	'Gigar',	'Megar',	'Kilor',	'Hector',        'Decar',	'Unir',		'Uniter',	'Decir',	'Centir',        'Milir',	'Micror',	'Nanor',	'Picor',	'Exax',        'Petax',	'Terax',	'Gigax',	'Megax',	'Kilox',        'Hectox',	'Decax',	'Unix',		'Dexi',		'Cenxi',        'Milix',	'Microx',	'Nanox',	'Picox',	'Ki',        'Mi',		'Gi',		'Ti',		'Ei',		'Zi',        'Yi',		'Jack',		"Anodo",	"Alisa",	"Chappie",        "Cathion",	"Catodo",	"Walle",	"Wally",	"Eva",        "Storm",	'Conect',	'Conexion',	'Kusanagi',	'Ghost',		'Shell',	"Shelf",	"Meigar",		"Cathodion",		"Cexron",		"Aloc",		"Deloc",
        ]
    return Names

def Surnames(Type):
    Surnames = [
        "I","II",'III','IV','V','VI','VII','VIXI','XIVI','IX','X', 'XI','XII','C','D',
		"1","2","3","4","5","6","7","8","9","10","11","12",
        'Α','α','β','π','Ω', 'Cixci', 'CIX', 'DIX', ]

    return Surnames

def Phonotactic(Type):
    onset  = ["Rob",'Mo',   'Al','Chap','An',
        'Cat','Ax', 'Max',  'Min',  'Th', 'Meg',
		"Cath"]
    nuclei = ['','','','','','','',
        "o",    'odr',   'i','im',  'esh', 'oc', 'od', ]
    codas  = ['','','','','','','',
        'op','on',   'ta',   'do', 'ion',
                      'mus','us', 'elf' ]
    return onset, nuclei, codas

def Surphonotactic(Type):
    onset  = [""]
    nuclei = [""]
    codas  = [""]
    return onset, nuclei, codas
