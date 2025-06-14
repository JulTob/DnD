
genus = ""

def combine(*maps):
    def combine_two(map1, map2):
        combined = {}
        # Combine all keys from both dictionaries
        all_keys = set(map1) | set(map2)
        for key in all_keys:
            combined[key] = map1.get(key, []) + map2.get(key, [])
        return combined

    if len(maps) == 0:
        return {}
    if len(maps) == 1:
        return maps[0]

    combined = maps[0]
    for map in maps[1:]:
        combined = combine_two(combined, map)

    return combined


Dwarven_mapping = { # Spanishish
    'a': ['e', 'o', 'a'],
    'b': ['v', 'b'],
    'c': ['s', 'ch', 'k', 'c', 'th', 'k'],
    'd': ['d', 't'],
    'e': ['i', 'ei', 'e'],
    'f': ['f', 'v'],
    'g': ['g', 'j'],
    'h': ['h', 'j', '', 'f'],
    'i': ['ie', 'e', 'i'],
    'j': ['g', 'x', 'j', 'h'],
    'k': ['k'],
    'l': ['l','ll','y','l','l'],
    'm': ['m','n'],
    'n': ['nn', 'n', 'm', 'ñ'],
    'o': ['u', 'ou', 'uo', 'o'],
    'p': ['p', 'b', 't'],
    'q': ['q', ''],
    'r': ['r', 'rr', 'r', ''],
    's': ['z','s', 'c', ],
    'u': ['ue', 'u'],
    'v': ['b', 'v'],
    'w': ['gu', 'hu', 'u', 'v', 'w'],
    'x': ['s', 'j', 'x', 'ch', 'sh'],
    'y': ['y', 'll', '', 'lli', 'yi'],
    'z': ['c', 's', 'th', 'z']
}
Celestial_mapping = { # Greekish
    'a': ['e', 'o', 'a'],
    'b': ['v', 'b'],
    'c': ['s', 'k', 'ch', 'th'],
    'd': ['th', 'd'],
    'e': ['i', 'e'],
    'f': ['f', 'ph'],
    'g': ['g', 'gh', 'y'],
    'h': ['h', 'e', ''],
    'i': ['i', 'e', 'y'],
    'j': ['i', 'y'],
    'k': ['k', 'q'],
    'l': ['l'],
    'm': ['m'],
    'n': ['n'],
    'o': ['o', 'u'],
    'p': ['p', 'b', 'ph'],
    'q': ['k'],
    'r': ['r'],
    's': ['s', 'c', 'z'],
    't': ['t', 'th'],
    'u': ['u', 'o', 'y'],
    'v': ['v', 'b', 'f'],
    'w': ['o', 'v', 'u'],
    'x': ['x', 'ch', 'ks'],
    'y': ['i', 'y', 'e'],
    'z': ['z', 's', 'dz']
}
Sylvan_mapping = { # Germanish and Vikingish
    'a': ['a', 'e', 'o', 'ao', 'au', 'ae'],
    'b': ['b', 'p', 'v'],
    'c': ['k', 's', 'ch'],
    'd': ['d', 't', 'th', 'th', 'f'],
    'e': ['e', 'i', 'ae', 'ei', 'ey'],
    'f': ['f', 'v'],
    'g': ['g', 'k', 'gh', 'j'],
    'h': ['h', '', 'hv'],
    'i': ['i', 'e', 'y', 'i'],
    'j': ['j', 'i', 'y'],
    'k': ['k', 'ch', 'c'],
    'l': ['l'],
    'm': ['m'],
    'n': ['n', 'nn'],
    'o': ['o', 'ou', 'oi', 'oo'],
    'p': ['p', 'b', 'f'],
    'q': ['k', 'kv', 'qu'],
    'r': ['r', 'rr'],
    's': ['s', 'ss', 'sh'],
    't': ['t', 'd', 'th', 'tt'],
    'u': ['u', 'o', 'ui', 'uu'],
    'v': ['v', 'f', 'w'],
    'w': ['w', 'v', 'u'],
    'x': ['ks', 'x', 'ch'],
    'y': ['y', 'i', 'iu', 'ý'],
    'z': ['z', 's', 'ts', 't']
}
Giant_mapping = { # Old English + French
    'a': ['a', 'e', 'o', 'æ', 'aa', 'ai'],
    'b': ['b', 'p', 'v'],
    'c': ['k', 's', 'ch', 'c'],
    'd': ['d', 't', 'ð', 'th'],
    'e': ['e', 'e', 'ei', 'ie', 'æ', 'ea'],
    'f': ['f', 'v', 'ph'],
    'g': ['g', 'j', 'gh', 'gu'],
    'h': ['h', '', 'ch'],
    'i': ['i', 'e', 'y', 'ie'],
    'j': ['j', 'g', 'i'],
    'k': ['k', 'c', 'qu'],
    'l': ['l'],
    'm': ['m'],
    'n': ['n', 'gn'],
    'o': ['o', 'ou', 'oe', 'o', 'u'],
    'p': ['p', 'b'],
    'q': ['qu', 'k'],
    'r': ['r'],
    's': ['s', 'ss', 'c', 't'],
    't': ['t', 'th', 'd'],
    'u': ['u', 'ou', 'o', 'eu'],
    'v': ['v', 'f'],
    'w': ['w', 'v', 'u'],
    'x': ['x', 'ks', 's', 'z'],
    'y': ['y', 'i', 'e'],
    'z': ['z', 's', 't', 'dz']
}
Gnomish_mapping = { # Swiss, German, Italian
    'a': ['a', 'ai', 'aa', 'e', 'o'],
    'b': ['b', 'p', 'v'],
    'c': ['k', 'ch', 's', 'c'],
    'd': ['d', 't', 'th'],
    'e': ['e', 'ia', 'ee', 'ei', 'i'],
    'f': ['f', 'v'],
    'g': ['g', 'k', 'j', 'gh'],
    'h': ['h', 'ch', ''],
    'i': ['i', 'ie', 'e', 'ii'],
    'j': ['j', 'i', 'y'],
    'k': ['k', 'ch', 'c'],
    'l': ['l'],
    'm': ['m'],
    'n': ['n'],
    'o': ['o', 'io', 'oo', 'ou'],
    'p': ['p', 'b'],
    'q': ['k', 'qu'],
    'r': ['r', 'rr'],
    's': ['s', 'ss', 'z'],
    't': ['t', 'th', 'd'],
    'u': ['u', 'iu', 'uu', 'o'],
    'v': ['v', 'f', 'w'],
    'w': ['w', 'v', 'u'],
    'x': ['x', 'ks', 's'],
    'y': ['y', 'i', 'iu'],
    'z': ['z', 's', 'tz', 'ts']
}
Gobling_mapping = { # Egiptian, Ancient coptic and arab
    'a': ['a', 'e', 'i', 'o', 'u'],
    'b': ['b', 'v', 'p'],
    'c': ['sh','z'],
    'd': ['d', 't', 'z', 'f'],
    'e': ['e', 'a', 'i'],
    'f': ['f', 'ph'],
    'g': ['g', 'k', 'gh', 'q'],
    'h': ['h', 'hj', 'kh'],
    'i': ['i', 'e', 'a', 'y'],
    'j': ['j', 'g', 'dj','z'],
    'k': ['k', 'q', 'g'],
    'l': ['l'],
    'm': ['m','n'],
    'n': ['n','m'],
    'o': ['o', 'u', 'w','ho'],
    'p': ['p', 'b', 'f'],
    'q': ['q', 'k', 'g'],
    'r': ['r','z'],
    's': ['s', 'z', 'sh'],
    't': ['t', 'z', 'th', 'd'],
    'u': ['u', 'o', 'w','hu'],
    'v': ['v', 'f', 'b'],
    'w': ['w', 'u', 'o'],
    'x': ['kh', 'j', 'q', 'ch'],
    'y': ['y', 'i', 'e'],
    'z': ['z', 'th', 's', 'sh','ch',]
}
Hellish_mapping = {
 # Latin and Old Hebrew, because the book od David names many demons
    'a': ['a', 'e', 'o', 'ah', 'eh'],
    'b': ['b', 'v', 'bh', 'p'],
    'c': ['k', 's', 'ch', 'q'],
    'd': ['d', 'dh', 't'],
    'e': ['e', 'a', 'i', 'eh'],
    'f': ['f', 'ph'],
    'g': ['g', 'gh', 'k'],
    'h': ['h', '', 'ch'],
    'i': ['i', 'e', 'y'],
    'j': ['j', 'y', 'i'],
    'k': ['k', 'q', 'c'],
    'l': ['l'],
    'm': ['m'],
    'n': ['n'],
    'o': ['o', 'u', 'oh'],
    'p': ['p', 'ph', 'f'],
    'q': ['q', 'k', 'c'],
    'r': ['r'],
    's': ['s', 'sh', 'ss'],
    't': ['t', 'th'],
    'u': ['u', 'o', 'v'],
    'v': ['v', 'u', 'b'],
    'w': ['w', 'v', 'u'],
    'x': ['ks', 'x', 's'],
    'y': ['y', 'i', 'j'],
    'z': ['z', 's', 'tz', 'dh']
    }
Draconic_mapping = { # Persian and ancient indian
    'a': ['e', 'i', 'o', 'u'],
    'b': ['v', 'bah', 'p'],
    'c': ['caj', 'seh', 's', 'k'],
    'd': ['drac', 'duh', 't'],
    'e': ['ere', 'ahi', 'i'],
    'f': ['fas', 'peh', 'p'],
    'g': ['j', 'gah', 'k'],
    'h': ['hul', 'kah', ''],
    'i': ['iri', 'e', 'ui'],
    'j': ['jan', 'y', 'g'],
    'k': ['kon', 'q', 'koh'],
    'l': ['lac'],
    'm': ['mer'],
    'n': ['nes', 'non'],
    'o': ['oki', 'urku', 'azru'],
    'p': ['par', 'poh', 'f'],
    'q': ['c', 'k'],
    'r': ['rac', 'reh'],
    's': ['suz', 'soh', 'saz'],
    't': ['tox', 'toh'],
    'u': ['uri', 'onza'],
    'v': ['vil', 'war', 'bor'],
    'w': ['wil', 'vil', 'u'],
    'x': ['kas', 'xis', 's'],
    'y': ['xay', 'i'],
    'z': ['zik', 's', 'dz']
}
Primordial_mapping = { # American languages
    'a': ['a', 'e', 'i', 'o', 'u'],
    'b': ['b', 'p'],
    'c': ['k', 's', 'ch'],
    'd': ['d', 't', 'th'],
    'e': ['e', 'i', 'ae', 'ee'],
    'f': ['f', 'ph'],
    'g': ['g', 'k', 'gh'],
    'h': ['h', 'kh', ''],
    'i': ['i', 'e', 'y'],
    'j': ['j', 'y', 'dj'],
    'k': ['k', 'q', 'kh'],
    'l': ['l', 'll'],
    'm': ['m'],
    'n': ['n', 'nn'],
    'o': ['o', 'u', 'oo'],
    'p': ['p', 'b', 'ph'],
    'q': ['q', 'k'],
    'r': ['r', 'rr'],
    's': ['s', 'sh', 'ss'],
    't': ['t', 'th', 'tt'],
    'u': ['u', 'o', 'uu'],
    'v': ['v', 'w', 'f'],
    'w': ['w', 'v', 'u'],
    'x': ['x', 'ks', 'sh'],
    'y': ['y', 'i'],
    'z': ['z', 's', 'dz']
}
Undercommon_mapping = { # Mayan
    'a': ['a', 'aa', 'e', 'ai', 'ao'],
    'b': ['b', 'p', ''],
    'c': ['k', 's', 'ch', 'qu'],
    'd': ['t', 'd', 'th'],
    'e': ['e', 'ei', 'ee', 'i'],
    'f': ['f', 'ph'],
    'g': ['g', 'k', 'gh'],
    'h': ['h', 'j', ''],
    'i': ['i', 'ii', 'ie', 'e'],
    'j': ['h', 'j', 'x'],
    'k': ['k', 'q', 'c'],
    'l': ['l', 'll'],
    'm': ['m'],
    'n': ['n', 'nn'],
    'o': ['o', 'oo', 'u', 'oe'],
    'p': ['p', 'b', 'f'],
    'q': ['k', 'q'],
    'r': ['r', 'rr'],
    's': ['s', 'sh', 'z'],
    't': ['t', 'th', 'd'],
    'u': ['u', 'uu', 'o'],
    'v': ['v', 'b', 'f'],
    'w': ['w', 'u', 'v'],
    'x': ['x', 'sh', 's'],
    'y': ['y', 'i', 'j'],
    'z': ['z', 's', 'tz']
}
Deep_Mapping = {
    # BS
    'a': ['ar', 'ah', 'ao', 'ae', 'arre'],
    'b': ['br', 'bh', 'b', 'bur'],
    'c': ['cr', 'ch', 'cq', 'cur', 'z'],
    'd': ['dr', 'dh', 'd', 'dur'],
    'e': ['er', 'eh', 'ei', 'ey', 'eur'],
    'f': ['fr', 'fh', 'f', 'frur'],
    'g': ['gr', 'gh', 'g', 'gur'],
    'h': ['hr', 'h', '', 'hur'],
    'i': ['ir', 'ih', 'ie', 'iy', 'irju'],
    'j': ['jr', 'jh', 'j', 'jur'],
    'k': ['kr', 'kh', 'kq', 'kur'],
    'l': ['lr', 'lh', 'l', 'yur','r'],
    'm': ['mr', 'mh', 'm', 'mur'],
    'n': ['nr', 'nh', 'n', 'nur'],
    'o': ['or', 'oh', 'ou', 'oe','orru'],
    'p': ['pr', 'ph', 'p', 'prur', 'pur', 'fur'],
    'q': ['k', 'kh', 'kur'],
    'r': ['rr', 'rh', 'r','rur'],
    's': ['sr', 'sh', 'sz', 'sur'],
    't': ['tr', 'th', 't', 'tur', 'z', 'zur'],
    'u': ['ur', 'uh', 'uo', 'ue','au', 'ue','iu','uru','ou'],
    'v': ['vr', 'vh', 'v', 'vir'],
    'w': ['wr', 'wh', 'w', 'war'],
    'x': ['xr', 'xh', 'xs', 'xur','x'],
    'y': ['yr', 'yh', 'y', 'yir'],
    'z': ['zr', 'zh', 'z']
    }

Ork_Mapping = {
    # BS
    'a': ['arga', 'aha', 'aza', ],
    'b': ['bur', 'bah', 'bru'],
    'c': ['kur', 'k', 'kak', 'kuz', 'z', 'zuk'],
    'd': ['t',  ],
    'e': ['erze', 'ehe', 'ehi', 'eke', 'a', 'u'],
    'f': ['fruf', 'fah', 'j', 'frur', 'furk'],
    'g': ['w', 'k', '', ''],
    'h': ['har', 'hur', '', 'hurk'],
    'i': ['o', 'ohu', 'uho', 'uhi', 'uri'],
    'j': ['h', 'huk', 'hak', 'h'],
    'k': ['kur', 'huk', 'kur', 'kuz'],
    'l': ['', 'yur',],
    'm': ['n', '', 'mur', 'muruk'],
    'n': ['nur', 'hun', 'nuk', 'nuruk'],
    'o': ['or', 'oh', 'orku', 'orke','oru'],
    'p': ['pur', 'puk', 'puz', 'prur', 'pur', 'fur'],
    'q': ['k', 'kuh', 'huk'],
    'r': ['rr', 'ruh', 'hur','rur','rk'],
    's': ['z', 'zuh', 'huz', 'zuz'],
    't': ['tuk', 'kut', 'z', 'zut'],
    'u': ['uru', 'uhu', 'urko', 'urke','arku', 'urke','irku','urku','orku'],
    'v': ['fur', 'f', 'z', 'zuf'],
    'w': ['wah', 'wuh', 'woh', 'war', 'wor', 'wur'],
    'x': ['zur', 'zuh', 'zus', 'zuk','z'],
    'y': ['yor', 'yuh', 'y', 'yur'],
    'z': ['zur', 'zuh', 'huz', 'zzuz']
    }

Common_mapping = { # Diverse Changes Mostly english and european languages
    'a': ['a', 'e', 'i', 'o', 'u', 'are', 'ati', 'ayu', 'epa',
		'esi', 'ido', 'ofa', 'uge'],
    'b': ['buh', 'p', 'v', 'bij', 'pol'],
    'c': ['caz', 'k', 's', 'cex', 'tus', 'kis', ],
    'd': ['dod', 't', 'daf', 'teg'],
    'e': ['ehu', 'a', 'i', 'o', 'u', 'eja', 'eke', 'eli', 'ize', 'uxe'],
    'f': ['fuc', 'piv', 'v'],
    'g': ['geb', 'k', 'j', 'gob', 'can'],
    'h': ['hun', '', 'cem', 'guw', 'wir'],
    'i': ['imo', 'e', 'a', 'o', 'u', 'ite', 'eyi', 'api', 'osi', 'udi'],
    'j': ['jaw', 'y', 'jif', 'doj', 'zah'],
    'k': ['ker', 'c', 'keh'],
    'l': ['lut', 'r', 'lul', 'liz'],
    'm': ['miy', 'n', 'mon', 'mab'],
    'n': ['nop', 'm', 'nan', 'neg'],
    'o': ['oha', 'a', 'e', 'i', 'u', 'oja', 'oke', 'olu', 'ozo'],
    'p': ['pax', 'b', 'pec', 'f'],
    'q': ['c', 'k', 'cuv'],
    'r': ['rib', 'lon', 'ram', 'rer'],
    's': ['sut', 'z', 'c', 'siy', 'top'],
    't': ['tas', 'd', 'ted', 'tut'],
    'u': ['udi', 'o', 'a', 'e', 'i', 'ofu', 'uge', 'uhi'],
    'v': ['vij', 'b', 'f', 'w'],
    'w': ['wok', 'v', 'u', 'wal'],
    'x': ['xuz', 'kis', 's', 'z', 'sod', 'caf'],
    'y': ['yeg', 'i', 'j', 'e', 'ipe'],
    'z': ['zus', 's', 'tis', 'doz', 'zaf']
	}

def initialize(Genus):
    global genus  # Declare genus as global to modify the global variable
    genus = Genus

def sound_mapping():
    global genus

    if "Aberration" in genus: return Deep_Mapping
    if "Aven"   	in genus: return combine(Primordial_mapping,Celestial_mapping)
    if "Beast"  	in genus: return Sylvan_mapping
    if "Beastfolk"  in genus: return Celestial_mapping
    if "Catfolk"    in genus: return combine(Sylvan_mapping, Common_mapping,Undercommon_mapping)
    if "Celestial"  in genus: return Celestial_mapping
    if "Construct"  in genus: return combine(Gnomish_mapping, Common_mapping, Dwarven_mapping, Giant_mapping)
    if "Dragon" 	in genus: return Draconic_mapping
    if "Dwarf" 		in genus: return Dwarven_mapping
    if "Elemental"	in genus: return Primordial_mapping
    if "Elf"		in genus: return combine(Sylvan_mapping,Common_mapping)
    if "Fey"		in genus: return Sylvan_mapping
    if "Fiend"			in genus: return Hellish_mapping
    if "Giant" 			in genus: return Giant_mapping
    if "Gnome" 			in genus: return Gnomish_mapping
    if "Goblin" 		in genus: return Gobling_mapping
    if "Kobold" 		in genus: return combine(Draconic_mapping, Undercommon_mapping)
    if "Lizardfolk" 	in genus: return combine(Draconic_mapping,Sylvan_mapping)
    if "Monstrosity"    in genus: return Undercommon_mapping
    if "Ooze"   		in genus: return Undercommon_mapping
    if "Orc"    		in genus: return Ork_Mapping
    if "Plant"  		in genus: return Primordial_mapping
    if "Snakefolk"  in genus: return combine(Hellish_mapping, Draconic_mapping)
    if "Undead"  	in genus: return combine(Hellish_mapping, Celestial_mapping)

    return Common_mapping
