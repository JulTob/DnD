'''
Undead are once-living creatures brought to a
horrifying state of undeath through the practice of
necromantic magic or some unholy curse. Undead
include walking corpses, such as vampires and zombies,
as well as bodiless spirits, such as ghosts and specters.
'''

'''
Names for Undead
Inspirations
	- Undeads
		- Phantom (Meaning)



'''

def Names(Type):
	MALE    = "He"    in Type
	FEMALE  = "She"   in Type
	AGENDER = "They"  in Type

	Names = [
			'Voxresil',				'Cutnulo',				'Biket',			'Nithas',			'Poemu',			'Makani',			'Chepi',			'Aave',			'Alginic',			'Aciclovir',			'Abianes',			'Acrivastine',			'Adalimumab',			'Alendronic',			'Allopurinol',			'Alogliptin',			'Amitriptyline',			'Amlodipine',			'Amoxicillin',			'Anastrozole',			'Apixaban',			'Aripiprazole',			'Aspirex',				'Aspiriz',				'Atenolol',			'Atorvastatin',			'Azathioprine',			'Azithromycin',			"Amunet",			"Anubis",			'Acetaminophen',			'Adderallix',			'Amitriptylin',			'Amlodipin',			'Amox',			'Aicillin',			'Ativan',			'Atorvas',			'Atatin',			'Azithromycin',			"Amenhotep",			"Ankhesenamun",			"Amenemhat",			'Ayia',					'Achencheres',			'Ahmesseker',			"Akalef",			'Aaheru',			'Akl',			'Amenhotep',			'Ahmose',			'Ani',			'Bismuth',			'Bromide',			'Butyl',			'Buskopan',			'Buprenorphinex',			'Bumetanid',			'Budesonid',			'Brinzolamid',			'Bisoprolox',			'Bisacodyl',			'Bimatoprost',			'Betamethason',			'Betahistix',			'Benzydamix',			'Benzyl',				'Bendroflumethiazid',	'Beclometasone',			'Baclofen',			'Buprenorphine',			'Bunavail',			'Brilinta',			'Benzonatate',			'Bast',			'Baahir',			"Bastet",			'Cersark',			'Cesar',			'Cromoglicate',			'Calpol',			'Clarityn',			'Codeine',			'Cyclizine',			'Cyanocobalamin',			'Colecalciferol',		'Colchicine',			'Codeine',				'Coaltar',				'Codydramol',			'Cocodaprin',			'Cocodamol',			'Cocareldopa',			'Cobeneldopa',			'Coamoxiclav',			'Canesten',			'Cain',			'Clotrimazole',			'Clopidogrel',			'Clonidine',			'Clonazepam',			'Clobetasone',			'Clobetasol',			'Clarithromycin',			'Citalopram',			'Ciprofloxacin',		'Cinnarizine',			'Chlorphenamine',		'Chlorhexidine',		'Chloramphenicol',			'Champix',			'Cetirizine',			'Cefalexin',			'Carvedilol',			'Carmellose',			'Carbocisteine',			'Carbimazole',			'Carbamazepine',			'Candesartan',			'Calcipotriol',			'Coco',			'Cephalexin',			'Ciprofloxacin',			'Citalopram',			'Clindamycin',			'Clonazepam',			'Cyclobenzaprine',		'Cymbalta',				'Cepos',				'Champix',			'Dinitrate',			'Dabigatran',			'Dapagliflozin',			'Dexamethasone',			'Diazepam',			'Diclofenac',			'Digoxin',			'Taydros',			'Xodeimel',			'Diltiazem',			'Diphenhydramine',			'Dipyridamole',			'Docusate',			'Domperidone',			'Donepezil',			'Dosulepin',			'Doxazosin',			'Doxycycline',			'Duloxetine',			'Doxycycline',			'Dupixent',			'Darwish',			'Darawin',			'Donkor',			'Djoser',			'Edoxaban',			'Empagliflozin',			'Enalapril',			'Eplerenone',			'Erythromycin',			'Escitalopram',			'Esomeprazole',			'Ezetimibe',			'Entresto',			'Entyvio',			'Fluticasone',			'Folic',				'Furosemide',			'Fusidic',				'Fybogel',				'Felodipine',			'Fentanyl',			'Ferrousfum',			'Ferroussulf',			'Fexofenadine',			'Finasteride',			'Flucloxacillin',			'Fluconazole',			'Fentanyl',			'Farxiga',			'Glyceryl',			'Glimepiride',			'Gliclazide',			'Gaviscon',			'Gabapentin',			'Gilenya',			'Gabapentix',			'Herceptix',			'Hyzrocorkoson',		'Hilroxocobalamix',		'Hycroxybloronixe',		'Hyoscixe',				'Hedrorbumide',			'Heparinoid',			'Haxokeridol',			'Husk',			'Hyoscinex',			'Humira',			'Hyrodlorot',			"Hiazide",			"Hyrodxix",			"Cholroquine",			'Hager',			"Horemheb",			"Hatshepsut",			'Isotrex',			'Isotretinoix',			'Isosorbide',			'Isosorbike',			'Irbesartax',			'Insulin',				'Indapamide',			'Ibucroxex',			'Ibutrofex',			'Iburoferk',			'Ispaghula',			'Imbruvica',			'Invokana',			'Inusrofex',			"Irynefer",			'Iscariot',			'Iscariotes',			'Iscaris',			'Jardiance',			'Januvia',			'Ketoconazole',			'Kevzara',			"Khaemweset",			"Khufu",			'Lagevrio',				'Lymecycline',			'Losartan',				'Lorazepam',			'Labetalol',			'Lactulose',			'Lamotrigine',			'Lansoprazole',			'Latanoprost',			'Lercanidipine',			'Letrozole',			'Levetiracetam',			'Levothyroxine',			'Lidocaine',			'Linagliptin',			'Lisinopril',			'Lithium',			'Loperamide',			'Loratadine',			'Leqvio',			'Lexapro',				'Lisinopril',			'Lofexidine',			'Loratadine',			'Lyrica',				'Mometasone',			'Montelukast',			'Morphine',			'Mebendazole',			'Mebeverine',			'Medroxyprogesterone',			'Melatonin',			'Memantine',			'Mesalazine',			'Metformin',			'Methadone',			'Methotrexate',			'Methylphenidate',			'Metoclopramide',			'Metoprolol',			'Metronidazole',		'Mirabegron',			'Mirtazapine',			'Molnupiravir',			'Macrogol',			'Mononitrate',			'Medroxyprogesterone',			'Melatonin',			'Meloxicam',			'Metformin',			'Methadone',			'Methotrexate',			'Metoprolol',			'Mounjaro',			'Mosiah',			"Meryt",			"Meritamun",			"Mutnofret",			"Merneith",			"Mutemwia",			"Montuhotep",			"Meresankh",			'Naproxen',				'Nefopam',				'Nicorandil',			'Nifedipine',			'Nitrofurantoin',			'Nortriptyline',			'Nystatin',			'Nurofen',			'Naloxone',			'Naltrexone',			'Naproxen',			'Narcan',			'Nurtec',			'Nkosi',			'Naguib',			"Neith",			"Nefertari",			"Nakht",			"Nubia",			'Olanzapine',			'Olmesartan',			'Omeprazole',			'Oxybutynin',			'Oxycodone',			'Omeprazole',			'Onpattro',			'Otezla',			'Ozempic',			'Pseudoephedrine',			'Propranolol',			'Phenergan',			'Promethazine ',			'Phenytoin',			'Pioglitazone',			'Pravastatin',			'Prophylaxis',			'Prednis',		  'Solone',		  'Pregabalin',			'Prochlor',		  'Perazine',				'Progesterone',			'Phenox',		  		'Aymethyl',		  		'Penxillin',			'Perindopril',			'Peptobismol',			'Peppermintoil',			'Paxlovid',			'Paroxetine',			'Pantoprazole',			'Paracetamol',			'Prozac',			'Piriton',			'Pantoprazole',			'Prednisone',			'Probuphine',			'Pilis',			"Pepi",			'Progesterone',			'Quetiapine',			'Risedronate',			'Risperidone',			'Rivaroxaban',			'Ropinirole',			'Rosuvastatin',			'Remdesivir',			'Ranitidine',			'Ramipril',			'Rabeprazole',			'Roaccutane',			'Rybelsus',			'Rah',			"Renpet",			'Sumatriptan',			'Sulfasalazine',			'Spironolactone',			'Solifenacin',			'Sotalol',			'Sotrovimab',			'Salbutamol',			'Saxagliptin',			'Senna',				'Sertraline',			'Sildenafil',			'Simeticoxe',			'Simvastatix',			'Sitagliptix',			'Sudafed',			'Subsalicylate',			'Secukinumab',			'Sublocade',			"Seshat",			"Sobekneferu",			"Seti",			"Senusret",			"Sobekhotep",			'Tadalafil',			'Tamsulosin',			'Temazepam',			'Terbinafixe',			'Thiamine',			'Tibolone',			'Ticagrelor',			'Timololeye',			'Tiotropium',			'Tolterodin',			'Topiramate',			'Tramadol',				'Tranexamic',			'Trastuzumab',			'Trazodone',			'Trimethoprim',			'Trinitrate',			'Tramadol',			'Trazodone',			"Tuya",			"Tah",			"Tutankhamun",			"Tauret",			"Tuthmosis",			'Urza',			'Utrogestan',			'Utrogestan',			'Uratum',				'Uthman',				'Uzuzar',			"Userkaf",				'Valproicacid',			'Valsartan',			'Varenicline',			'Varenixline',			'Venlafaxine',			'Verapamil',			'Vokian',			'Valproate',			'Veklury',			'Varenicline',			'Vigrax',			'Viagrax',			'Warfarin',			'Wegovy',			'Wellbutrin',			'Xevudy',			'Xanax',			'Zopiclon',			'Zolpidex',				'Zovirax',				'Zubsolv',			'Zosar', 				'Norbidol',
			]

	if MALE:
		Names += [
			'Iraclio',		'Bryan',			'Vaitautas',			'Vaidvilas',			'Vaidmantas',			'Vaidminas',			'Vaidaras',			'Vaidaugas',			'Vaidilas',			'Vaidgintas',			'Tonraq',			'Drogo',			'Seijuro',			'Enlil',			'Alvaidas',			'Arvaidas',			'Bunki',			'Dovaidas',			'Duchomys',			'Duchoslaw',			'Gedvaidas',			'Jovaidas',			'Kaitou',			'Minvaidas',	'Norvaidas',			'Phantom',
			]

	if FEMALE:
		Names += [
			'Guinevere',			'Vaida',			'Marzana',			'Morrigu',			'Larentia',			'Kishimojin',			'Bryan',			'Drogo',			'Enlil',			'Ninlil',			'Eimi',
			]

	return Names

def Surnames(Type):
	Names = [""]

	VAMPIRE = "Vampire" in Type
	if VAMPIRE:
		Names += [

			]
	return Names

def Phonotactic(Type):
	onset  = ['Mort','Trax', 'Bik',]
	nuclei = ['im','ig', 'ez',]
	codas  = ['er','lok','or']

	if  "Death Knight" in Type:
			onset += ["Krieg", "War", "Ruin", "Doom"]
			nuclei += ["aug", "obl", "uih"]
			codas += ["arde", "ade", "elm"]
	if  "Lich" in Type:
			onset += ["Lich", "Arcan", "Necro", "Immort"]
			nuclei += ["e", "a", "o", "no","xa","ki"]
			codas += ["mancer", "lich", "lore"]

	if  "Wraith" in Type:
			onset += ["Wraz", "Sect", "Xad", "Gast"]
			nuclei += ["aw", "ef", "ish"]
			codas += ["ail", "ury", "ade"]

	return onset, nuclei, codas

def Surphonotactic(Type):
	onset  = ["Tum", 'Tumb', 'Necr']
	nuclei = ["ul", 'of']
	codas  = ["ar", 'age', 'us']

	return onset, nuclei, codas
