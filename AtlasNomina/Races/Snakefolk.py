
def Names(genus):
	MALE    = "He"    in genus
	FEMALE  = "She"   in genus
	AGENDER = "They"  in genus

	SUBgenus = "Subgenus" in genus

	Names = [
		'Avenaxi',
		"Medusa",
		'Yesses',
		'Dragunov',
		'Drakun',
		'Dragun',
		'Ganriu',
		"Gunen",
		"Essesraku",
		"Anuri",
		"Ansuri",
		"Anruix",
		"Sesrak",
		"Esraku",
		"Venaxi",
		"Raka",
		"Vena",
		"Salazax",
		"Rayezar",
		]

	if MALE:
		Names += [
		"Drogun",
		"Draku",

		]

	if FEMALE:
		Names += [
			"Xasha",
			"Medusa",
			"Melyassa",
			"Rennesse",
			"Xasha",
			"Gorgona",
			"Nuri",
			"Nonure",
			]

	return Names

def Surnames(genus):
	Surnames = [""]
	return Surnames

def Phonotactic(genus):
	onset   = ['Zal','Saj','Ray','Med','Ren',
		'Xas', 'Yez','Sal', 'Av',]
	nuclei  = [ 'ak', 'am', 'amr', 'an', 'as',
		'ez',   'ush','ex', 'es',  'az', 'en',]
	codas   = ['','a',  'az','ar','ax',
		'an','as','esh','ah','aj','', 'ax',  ]
	return onset, nuclei, codas

def Surphonotactic(genus):
	onset  = [""]
	nuclei = [""]
	codas  = [""]
	return onset, nuclei, codas
