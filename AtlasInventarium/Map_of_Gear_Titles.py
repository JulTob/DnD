"""
Map_of_Gear_Titles — evocative names for gear, from the item AND its hero.

Julio's idea (2026-08-01): a defensive longsword in a Dragonborn's hand should
be a *Blade of Scales*; a cleric's mace, a *Mace of Redemption*. So a title is
read off two axes at once —

	the ITEM's craft Tags   ("of Defense" → a warding theme), and
	the HERO's genus Tags   (Dragonborn → a draconic theme),

— and where a pairing has a name of its own, that name wins. Neither axis
alone would produce "Scales".

The mechanical vocabulary is NOT replaced. ``of Defense`` still means +1 AC,
the Craft Tag is still on the item (``item in Of_Defense``), and the blurb
still prints "+1 AC" in plain sight. Only the display title becomes prose.

Shape follows ``AtlasEpica/Map_of_Titles`` (vocabulary chosen by Tags) but
takes an explicit stream rather than seeding the global RNG, per
``Canon/Modus-Operandi``.
"""

from __future__ import annotations

import random


# ---------------------------------------------------------------------------
# What to call the thing itself — read off the item, not the hero
# ---------------------------------------------------------------------------

_NOUNS: dict[str, tuple[str, ...]] = {
		"Club": ("Club", "Bat", "Baton", "Truncheon"),
		"Dagger": ("Dagger", "Knife", "Blade", "Dirk", "Poniard"),
		"Greatclub": ("Greatclub", "War Club", "Bludgeon"),
		"Handaxe": ("Handaxe", "Hatchet", "Belt Axe"),
		"Javelin": ("Javelin", "Throwing Spear", "Light Spear"),
		"Light Hammer": ("Light Hammer", "Mallet", "Tack Hammer", "Hand Mallet"),
		"Mace": ("Mace", "Meteor", "Flanged Mace", "Sceptre"),
		"Quarterstaff": ("Quarterstaff", "Staff", "Cane"),
		"Sickle": ("Sickle", "Billhook", "Reaping Hook"),
		"Spear": ("Spear", "Boar Spear", "Partisan"),
		"Dart": ("Dart", "Needle", "Bodkin", "Fléchette"),
		"Light Crossbow": ("Light Crossbow", "Crossbow", "Latchbow", "Prod"),
		"Shortbow": ("Shortbow", "Bow", "Hunting Bow", "Recurve"),
		"Sling": ("Sling", "Staff Sling", "Stone-Cord"),
		"Battleaxe": ("Battleaxe", "War Axe", "Broadaxe"),
		"Flail": ("Flail", "Chain", "Threshing Flail", "Chain-Head"),
		"Glaive": ("Glaive", "Fauchard", "Polearm"),
		"Greataxe": ("Greataxe", "Executioner's Axe", "Great Cleaver"),
		"Greatsword": ("Greatsword", "Great Edge", "Two-Hander"),
		"Halberd": ("Halberd", "Poleaxe", "Bill", "Guisarme"),
		"Lance": ("Lance", "Jousting Lance", "Couched Lance"),
		"Longsword": ("Longsword", "Blade", "Arming Sword", "Bastard Sword"),
		"Maul": ("Maul", "Sledge", "Great Hammer", "War Maul"),
		"Morningstar": ("Morningstar", "Spiked Mace", "Holy Water Sprinkler"),
		"Pike": ("Pike", "Long Pike", "Phalanx Spear"),
		"Rapier": ("Rapier", "Stinger", "Estoc", "Épée", "Smallsword"),
		"Scimitar": ("Scimitar", "Sabre", "Falchion"),
		"Shortsword": ("Shortsword", "Sidearm", "Shortblade"),
		"Trident": ("Trident", "Fish Spear", "Fork"),
		"War Pick": ("War Pick", "Horseman's Pick", "Crow's Beak", "Beak"),
		"Warhammer": ("Warhammer", "Hammer", "War Mallet"),
		"Whip": ("Whip", "Lash", "Bullwhip", "Cat"),
		"Blowgun": ("Blowgun", "Blowpipe", "Reed"),
		"Hand Crossbow": ("Hand Crossbow", "Sleeve Crossbow", "Pocket Bow"),
		"Heavy Crossbow": ("Heavy Crossbow", "Siege Bow", "Windlass"),
		"Longbow": ("Longbow", "Warbow", "Yew Bow"),
		"Musket": ("Musket", "Matchlock", "Firelock"),
		"Pistol": ("Pistol", "Flintlock", "Handcannon", "Snaphance"),
		"Padded": ("Padded", "Quilted Coat", "Padded Coat"),
		"Leather": ("Leather", "Jerkin", "Leather Coat"),
		"Studded Leather": ("Studded Leather", "Studded Jerkin", "Riveted Coat"),
		"Hide": ("Hide", "Pelts", "Furs", "Skins"),
		"Chain Shirt": ("Chain Shirt", "Mail Shirt"),
		"Scale Mail": ("Scale Mail", "Scale Coat"),
		"Breastplate": ("Breastplate", "Cuirass", "Plackart"),
		"Half Plate": ("Half Plate", "Demi-Plate", "Three-Quarter Harness"),
		"Ring Mail": ("Ring Mail", "Ringed Coat", "Coat of Rings"),
		"Chain Mail": ("Chain Mail", "Mail Coat"),
		"Splint": ("Splint", "Banded Mail", "Splinted Harness"),
		"Plate": ("Plate", "Full Harness", "Panoply"),
		"Shield": ("Shield", "Aegis", "Buckler", "Heater"),
		}


# ---------------------------------------------------------------------------
# Culture — a third, lighter axis: what a hero's PEOPLE call the thing
# ---------------------------------------------------------------------------

# Julio's setting inspirations (2026-08-03). These are orientative, not
# mandatory: they WEIGHT the pool rather than replacing it, so a Dragonborn
# still sometimes carries a plain Longsword, just more often a Katana.
_CULTURES: tuple[tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]], ...] = (
		(("Dragonborn", "Dragon"), ("japan", "aztec"), ("eragon_dragons", "wyrm_myth")),
		(("Kobold",), ("japan", "china", "korea"), ("wyrm_myth",)),
		(("Fey", "Fae"), ("china",), ("fairytale_fae",)),
		(("Goblin",), ("persia", "levante"), ("fairytale_fae", "grimdark")),
		(("Elemental", "Genasi", "Djinn", "Efreet", "Marid", "Dao"), ("india", "oceania"), ("arabian_nights",)),
		(("Human",), ("africa", "egypt", "maghreb", "carthage"), ("arthuriana",)),
		(("Elf",), ("norse", "rus", "mongol", "celt"), ("tolkien_elves", "fairytale_fae")),
		(("Dwarf",), ("iberia", "andalus"), ("folklore_dwarf", "tolkien_dwarves")),
		(("Gnome",), ("italy", "germany", "switzerland"), ("folklore_dwarf", "clockpunk")),
		(("Aasimar", "Celestial"), ("rome",), ("arthuriana",)),
		(("Giant", "Goliath"), ("greece",), ("wyrm_myth",)),
		(("Monk",), ("ninja",), ("anime",)),
		(("Barbarian",), (), ("sword_and_sorcery",)),
		(("Warlock", "Fiend", "Tiefling"), (), ("grimdark",)),
		(("Artificer",), (), ("clockpunk",)),
		(("Paladin",), (), ("arthuriana",)),
		)

# A theme and an item, met at their crossing: what a rustic spear or a
# corsair cutlass is actually called. Themes come from the wearer's story.
_THEMED_NOUNS: dict[tuple[str, str], tuple[str, ...]] = {
		("rustic", "Spear"): ("Pitchfork", "Hayfork", "Farmer's Spear"),
		("rustic", "Sickle"): ("Harvest Blade", "Reaping Hook"),
		("rustic", "Club"): ("Fence Post", "Threshing Stick"),
		("rustic", "Quarterstaff"): ("Shepherd's Crook", "Walking Staff"),
		("rustic", "Sling"): ("Shepherd's Cord", "Stone-Cord"),
		("rustic", "Handaxe"): ("Woodaxe", "Splitting Axe"),
		("rustic", "Dagger"): ("Skinning Knife", "Paring Knife"),
		("rustic", "Maul"): ("Fence Maul", "Post-Driver"),
		("sylvan", "Longbow"): ("Yew Bow", "Greenbow", "Hunter's Longbow"),
		("sylvan", "Shortbow"): ("Green Curve", "Whisperbow"),
		("sylvan", "Quarterstaff"): ("Heartwood Staff", "Grove-Staff"),
		("sylvan", "Dagger"): ("Thorn Knife", "Grafting Knife"),
		("shadow", "Dagger"): ("Misericorde", "Sleeve Knife", "Quiet Answer"),
		("shadow", "Hand Crossbow"): ("Sleeve Crossbow", "Alley Snap"),
		("shadow", "Whip"): ("Garrote-Lash", "Silent Cord"),
		("shadow", "Shortsword"): ("Cutpurse's Blade", "Alley Sidearm"),
		("holy", "Mace"): ("Censer", "Reliquary Mace", "Priest's Mace"),
		("holy", "Warhammer"): ("Judgement Hammer", "Dawn Hammer"),
		("holy", "Morningstar"): ("Dawnstar", "Vigil-Head"),
		("holy", "Dagger"): ("Sacrificial Knife", "Altar Blade"),
		("grave", "Sickle"): ("Reaper's Hook", "Last Harvest"),
		("grave", "Dagger"): ("Grave Knife", "Cold Kiss"),
		("grave", "Scimitar"): ("Barrow Sabre", "Shroud-Cutter"),
		("deep", "Warhammer"): ("Smith's Hammer", "Forge-Hammer", "Anvil-Song"),
		("deep", "Battleaxe"): ("Miner's Axe", "Seam-Splitter"),
		("deep", "Maul"): ("Stonebreaker", "Deep Sledge"),
		("deep", "Light Hammer"): ("Bench Hammer", "Chasing Hammer"),
		("deep", "War Pick"): ("Miner's Pick", "Seam-Pick"),
		("draconic", "Greatsword"): ("Wyrmtooth", "Drake-Edge"),
		("draconic", "Longsword"): ("Drake-Fang", "Scaled Blade"),
		("draconic", "Halberd"): ("Wyrm-Hook", "Drake Poleaxe"),
		("infernal", "Whip"): ("Scourge", "Hell-Cord"),
		("infernal", "Flail"): ("Hell-Chain", "Debt-Collector"),
		("infernal", "Dagger"): ("Pact Knife", "Contract Blade"),
		("savage", "Greataxe"): ("Skullsplitter", "Red Feller"),
		("savage", "Maul"): ("Bonebreaker", "Skull-Sledge"),
		("savage", "Greatclub"): ("Root-Club", "Giant's Limb"),
		("savage", "Spear"): ("Boar Spear", "Hunting Spear"),
		("arcane", "Quarterstaff"): ("Focus-Rod", "Rune-Staff", "Scholar's Staff"),
		("arcane", "Dagger"): ("Letter Opener", "Athame", "Sigil-Knife"),
		("arcane", "Light Hammer"): ("Sigil Mallet", "Binding Mallet"),
		}

# Influence, not a wall: each people hears its neighbours, at a weight.
# The network is what the viking test at the bottom protects.
_INFLUENCES: dict[str, tuple[tuple[str, int], ...]] = {
		"japan": (("china", 2), ("korea", 2)),
		"korea": (("china", 2), ("japan", 2)),
		"china": (("korea", 1), ("japan", 1), ("india", 2), ("mongol", 1)),
		"aztec": (),
		"india": (("china", 2), ("persia", 2), ("oceania", 1)),
		"oceania": (("india", 1),),
		"persia": (("india", 2), ("levante", 2), ("greece", 1), ("mongol", 1)),
		"levante": (("persia", 2), ("egypt", 2), ("greece", 1), ("rome", 1)),
		"egypt": (("levante", 2), ("greece", 1), ("rome", 1), ("africa", 1)),
		"africa": (("egypt", 1), ("maghreb", 1), ("carthage", 1), ("rome", 1)),
		"maghreb": (("andalus", 2), ("africa", 1), ("carthage", 1), ("levante", 1)),
		"carthage": (("iberia", 2), ("africa", 1), ("rome", 1), ("greece", 1)),
		"andalus": (("maghreb", 2), ("iberia", 2), ("levante", 1), ("persia", 1)),
		"iberia": (("andalus", 2), ("carthage", 1), ("celt", 1), ("rome", 1)),
		"celt": (("iberia", 1), ("norse", 1), ("rome", 1)),
		"norse": (("rus", 2), ("celt", 1), ("iberia", 1), ("maghreb", 1)),
		"rus": (("norse", 2), ("mongol", 2), ("greece", 1)),
		"mongol": (("rus", 2), ("china", 2), ("persia", 1)),
		"italy": (("rome", 3), ("germany", 1), ("switzerland", 1), ("greece", 1)),
		"germany": (("italy", 1), ("switzerland", 2), ("rome", 1)),
		"switzerland": (("germany", 2), ("italy", 2)),
		"rome": (("greece", 3), ("egypt", 1), ("carthage", 1)),
		"greece": (("rome", 2), ("persia", 1), ("egypt", 1)),
		"ninja": (("japan", 2),),
		"tolkien_elves": (("norse", 2), ("celt", 2), ("fairytale_fae", 1)),
		"tolkien_dwarves": (("norse", 2), ("folklore_dwarf", 2)),
		"folklore_dwarf": (("germany", 2), ("switzerland", 1), ("norse", 1)),
		"fairytale_fae": (("celt", 2), ("germany", 1)),
		"eragon_dragons": (("wyrm_myth", 2), ("tolkien_elves", 1)),
		"wyrm_myth": (("norse", 1), ("greece", 1), ("china", 1)),
		"arabian_nights": (("persia", 2), ("levante", 2), ("india", 1)),
		"arthuriana": (("celt", 2), ("rome", 1), ("italy", 1)),
		"sword_and_sorcery": (("mongol", 1), ("levante", 1), ("grimdark", 1)),
		"grimdark": (("germany", 1), ("sword_and_sorcery", 1)),
		"clockpunk": (("italy", 2), ("germany", 2), ("switzerland", 2)),
		"anime": (("ninja", 2), ("japan", 2)),
		}

_CULTURAL_NOUNS: dict[str, dict[str, tuple[str, ...]]] = {
		"japan": {
				"Longsword": ("Katana",),
				"Greatsword": ("Nodachi", "Odachi Greatsword"),
				"Shortsword": ("Wakizashi",),
				"Dagger": ("Tanto", "Kunai"),
				"Glaive": ("Naginata",),
				"Sickle": ("Kama Sickle",),
				"Spear": ("Yari Spear",),
				"Club": ("Nunchaku", "Tetsubo Club"),
				"Quarterstaff": ("Bo Staff", "Jo Staff"),
				"Dart": ("Shuriken",),
				"Blowgun": ("Fukiya Blowpipe",),
				"Longbow": ("Yumi Bow", "Daikyu Bow"),
				"Flail": ("Kusari-Fundo Chain",),
				},
		"aztec": {
				"Longsword": ("Macuahuitl Sword",),
				"Greatsword": ("Macuahuitl Greatsword",),
				"Glaive": ("Tepoztopilli Polearm",),
				"Spear": ("Tepoztopilli Spear",),
				"Javelin": ("Atlatl Dart",),
				"Dart": ("Tlacochtli Dart",),
				"Club": ("Cuauhololli Club",),
				"Mace": ("Cuauhololli Mace",),
				"Battleaxe": ("Itztopilli Axe",),
				"Sling": ("Tematlatl Sling",),
				"Shield": ("Chimalli Shield",),
				"Dagger": ("Tecpatl Knife",),
				},
		"china": {
				"Longsword": ("Jian Sword", "Changdao Sword"),
				"Greatsword": ("Zhanmadao Greatsword",),
				"Scimitar": ("Dao Sabre",),
				"Glaive": ("Guandao Glaive",),
				"Spear": ("Qiang Spear",),
				"Dagger": ("Bishou Dagger",),
				"Quarterstaff": ("Gun Staff",),
				"Whip": ("Jiujiebian Chain-Whip",),
				"Halberd": ("Ji Halberd",),
				},
		"korea": {
				"Longsword": ("Hwando Sabre", "Geom Sword"),
				"Greatsword": ("Ssangsudo Greatsword",),
				"Shortsword": ("Hwando Sabre",),
				"Glaive": ("Woldo Glaive",),
				"Spear": ("Changgeom Spear",),
				"Longbow": ("Gakgung Bow",),
				"Shortbow": ("Gakgung Bow",),
				"Flail": ("Pyeongon Flail",),
				"Dagger": ("Jangdo Knife",),
				},
		"india": {
				"Longsword": ("Khanda Sword",),
				"Scimitar": ("Talwar", "Firangi Sabre"),
				"Dagger": ("Katar Punch-Dagger", "Bichuwa Dagger"),
				"Whip": ("Urumi Whip-Blade",),
				"Trident": ("Trishula Trident",),
				"Mace": ("Gada Mace",),
				"Dart": ("Chakram Ring",),
				"Battleaxe": ("Tabar Axe",),
				"Shortbow": ("Kaman Bow",),
				"Shield": ("Dhal Buckler",),
				"Spear": ("Vel Spear",),
				},
		"oceania": {
				"Club": ("Patu Club", "Leiomano Club"),
				"Greatclub": ("Taiaha Staff-Club",),
				"Quarterstaff": ("Taiaha Staff",),
				"Spear": ("Tao Spear", "Bone Spear"),
				"Javelin": ("Huata Javelin",),
				"Shortsword": ("Leiomano Blade",),
				"Dagger": ("Shark-Tooth Knife",),
				"Trident": ("Fish Spear",),
				"Sling": ("Coral Sling",),
				},
		"persia": {
				"Shortsword": ("Akinakes Blade",),
				"Dagger": ("Akinakes Dagger", "Khanjar Dagger"),
				"Scimitar": ("Shamshir",),
				"Battleaxe": ("Sagaris Axe",),
				"Mace": ("Gorz Mace",),
				"Javelin": ("Zhupin Javelin",),
				"Shortbow": ("Kaman Bow",),
				"Longbow": ("Kaman Bow",),
				"Spear": ("Palta Spear",),
				"Shield": ("Spara Shield",),
				},
		"levante": {
				"Shortsword": ("Sica Blade", "Khopesh Sabre"),
				"Dagger": ("Jambiya Dagger",),
				"Scimitar": ("Kilij Sabre", "Shamshir"),
				"Sling": ("Kela Sling", "Shepherd's Honda"),
				"Mace": ("Pear Mace",),
				"Club": ("Was Sceptre",),
				"Spear": ("Romfea Spear",),
				},
		"egypt": {
				"Shortsword": ("Khopesh Sabre",),
				"Scimitar": ("Khopesh Sabre",),
				"Flail": ("Nekhakha Flail",),
				"Quarterstaff": ("Heka Crook", "Was Sceptre"),
				"Club": ("Was Sceptre",),
				"Mace": ("Pear Mace",),
				"Battleaxe": ("Epsilon Axe",),
				"Shortbow": ("Pedjet Bow",),
				"Longbow": ("Pedjet Bow",),
				"Spear": ("Djeba Spear",),
				},
		"africa": {
				"Longsword": ("Kaskara Sword", "Takouba Sword"),
				"Shortsword": ("Ida Sword",),
				"Scimitar": ("Shotel Sabre",),
				"Dagger": ("Billao Dagger",),
				"Javelin": ("Assegai", "Iklwa Spear"),
				"Spear": ("Iklwa Spear", "Assegai"),
				"Club": ("Knobkerrie",),
				"Battleaxe": ("Epa Axe",),
				"Shield": ("Ishlangu Shield", "Nguni Shield"),
				},
		"maghreb": {
				"Scimitar": ("Nimcha Sabre", "Flissa Sabre"),
				"Longsword": ("Takouba Sword", "Jineta Sword"),
				"Dagger": ("Koummya Dagger",),
				"Shield": ("Lamt Shield",),
				"Javelin": ("Zagaya Javelin",),
				},
		"carthage": {
				"Shortsword": ("Falcata",),
				"Scimitar": ("Falcata",),
				"Javelin": ("Soliferrum Javelin", "Numidian Javelin"),
				"Sling": ("Balearic Sling",),
				"Shield": ("Caetra Shield",),
				},
		"norse": {
				"Greataxe": ("Dane Axe", "Breidox Axe"),
				"Battleaxe": ("Bearded Axe", "Skeggox Axe"),
				"Dagger": ("Seax",),
				"Shortsword": ("Langseax Sword",),
				"Longsword": ("Ulfberht Blade",),
				"Spear": ("Ash Spear", "Gierr Spear"),
				"Glaive": ("Atgeir Polearm",),
				"Halberd": ("Atgeir Polearm",),
				"Chain Mail": ("Brynja", "Hringserkr Mail"),
				"Chain Shirt": ("Brynja",),
				"Shield": ("Round Shield", "Skjoldr Shield"),
				},
		"rus": {
				"Scimitar": ("Shashka Sabre",),
				"Battleaxe": ("Berdiche Axe",),
				"Greataxe": ("Berdiche Axe",),
				"Mace": ("Pernach Mace",),
				"Longsword": ("Kontar Blade",),
				"Shield": ("Kite Shield",),
				},
		"mongol": {
				"Shortbow": ("Horsebow", "Composite Bow"),
				"Longbow": ("Composite Bow",),
				"Scimitar": ("Saber of the Steppe",),
				"Lance": ("Kontos",),
				"Spear": ("Steppe Lance",),
				},
		"celt": {
				"Greatsword": ("Claymore",),
				"Dagger": ("Sgian Dubh",),
				"Shield": ("Targe",),
				"Spear": ("Gae Spear",),
				"Longsword": ("Spatha Celtica",),
				},
		"iberia": {
				"Rapier": ("Espada Ropera", "Bilbo Rapier"),
				"Longsword": ("Toledo Blade",),
				"Greatsword": ("Montante",),
				"Dagger": ("Vizcaina Dagger",),
				"Shield": ("Rodela Shield",),
				"Halberd": ("Alabarda Halberd",),
				"Musket": ("Arcabuz",),
				"Pistol": ("Pedrenal Pistol",),
				"Breastplate": ("Coselete Cuirass", "Peto Breastplate"),
				"Plate": ("Armadura Plate",),
				"Sling": ("Honda Sling",),
				},
		"andalus": {
				"Scimitar": ("Jineta Sabre", "Nimcha Sabre"),
				"Longsword": ("Jineta Sword",),
				"Dagger": ("Koummya Dagger",),
				"Shield": ("Adarga Shield",),
				"Shortbow": ("Ballesta Bow",),
				},
		"italy": {
				"Dagger": ("Cinquedea", "Stiletto"),
				"Greatsword": ("Spadone",),
				"Rapier": ("Schiavona",),
				"Longsword": ("Spada",),
				"Shield": ("Rotella Shield", "Pavise"),
				},
		"germany": {
				"Dagger": ("Rondel Dagger",),
				"Greatsword": ("Zweihander", "Bidenhander"),
				"Shortsword": ("Katzbalger",),
				"Rapier": ("Panzerstecher",),
				"Longsword": ("Langes Messer",),
				"Halberd": ("Hellebarde",),
				"Morningstar": ("Morgenstern",),
				"Plate": ("Gothic Plate", "Maximilian Plate"),
				"Musket": ("Hakenbuchse",),
				},
		"switzerland": {
				"Halberd": ("Schweizer Halbarte", "Sempacher Halbarte"),
				"Pike": ("Langspiess Pike", "Schweizer Pike"),
				"Warhammer": ("Luzerner Hammer",),
				"Maul": ("Luzerner Hammer",),
				"Dagger": ("Baselard", "Schweizerdegen"),
				"Shortsword": ("Baselard",),
				"Scimitar": ("Schweizersabel",),
				"Glaive": ("Vouge Polearm",),
				"Spear": ("Ahlspiess Spike",),
				"Musket": ("Handrohr",),
				},
		"rome": {
				"Shortsword": ("Gladius",),
				"Dagger": ("Pugio Dagger",),
				"Longsword": ("Spatha",),
				"Javelin": ("Pilum", "Plumbata Dart"),
				"Trident": ("Fuscina Trident",),
				"Shield": ("Scutum Shield",),
				"Scale Mail": ("Lorica Squamata",),
				"Chain Mail": ("Lorica Hamata",),
				"Splint": ("Lorica Segmentata",),
				"Sling": ("Funda Sling",),
				},
		"greece": {
				"Shortsword": ("Xiphos", "Kopis"),
				"Spear": ("Dory Spear", "Xyston Lance"),
				"Pike": ("Sarissa",),
				"Shield": ("Aspis Shield", "Hoplon Shield"),
				"Scimitar": ("Makhaira Sabre", "Kopis"),
				"Club": ("Rhopalon Club",),
				"Sling": ("Sphendone Sling",),
				"Padded": ("Linothorax",),
				"Leather": ("Linothorax",),
				},
		"ninja": {
				"Dart": ("Shuriken",),
				"Sickle": ("Kama Sickle", "Kusarigama"),
				"Club": ("Nunchaku",),
				"Quarterstaff": ("Bo Staff", "Jo Staff"),
				"Dagger": ("Tanto", "Kunai"),
				"Shortsword": ("Ninjato",),
				"Flail": ("Kusarigama", "Kusari-Fundo Chain"),
				"Blowgun": ("Fukiya Blowpipe",),
				},
		}

# How much heavier a hero's own words are than the generic pool. Several
# copies means they usually win without ever being the only option — which
# How loudly each layer speaks. Culture and trade WEIGHT the pool rather than
# short-circuiting it, so a Dragonborn usually gets a Katana and sometimes a
# plain Longsword — which is what "orientative, not mandatory" has to mean
# mechanically.
#
# A people's own voice is a BUDGET, shared among the markers they hold, not a
# weight paid per marker. Otherwise a Human (Africa + Egypt + Maghreb +
# Carthage) would shout four times louder than an Aasimar (Rome) purely for
# having a richer heritage, and the trade layer would vanish underneath.
# 12 divides cleanly by every marker count we use (1, 2, 3, 4).
_CULTURAL_BUDGET = 12
# What one point of influence data (1…3) is worth, read against the old
# per-society weight of 3: a neighbour at 3 speaks as loudly as the people
# themselves, at 1 it is an accent.
_INFLUENCE_SCALE = 3
_GENERIC_WEIGHT = 4
_TRADE_WEIGHT = 16


_GENERIC_CACHE: dict[str, tuple[str, ...]] | None = None


def _culture_owned() -> frozenset[str]:
	"""Every name some people or legend claims for itself."""
	claimed: set[str] = set()
	for vocabulary in _vocabulary().values():
		for names in vocabulary.values():
			claimed.update(
					names
					)
	return frozenset(
			claimed
			)


def _generic_nouns(
		name: str,
		) -> tuple[str, ...]:
	"""
	The culture-neutral pool for an item.

	Strongly marked words are removed here and supplied by the culture layer
	instead — otherwise a Dwarf's spear came out a Yari and a Fey's shortsword
	a Wakizashi, which dilutes exactly the flavour the culture axis adds.
	The item's own proper name always survives.
	"""
	global _GENERIC_CACHE
	if _GENERIC_CACHE is None:
		claimed = _culture_owned()
		_GENERIC_CACHE = {
				item: tuple(
						noun
						for noun in pool
						if noun == item
						or noun not in claimed
						)
				for item, pool in _NOUNS.items()
				}
	return _GENERIC_CACHE.get(
			name,
			(),
			)


# ---------------------------------------------------------------------------
# The two axes, reduced to themes
# ---------------------------------------------------------------------------

# Craft name -> what it FEELS like (not what it grants; that stays mechanical).
_CRAFT_THEME: dict[str, str] = {
		"of Defense": "warding",
		"of Warding": "warding",
		"of the Aegis": "warding",
		"of the Paragon": "warding",
		"of Precision": "keen",
		"of Wounding": "cruel",
		"of Ruin": "cruel",
		"of the Bear": "enduring",
		"of Swiftness": "swift",
		"of Vigilance": "watchful",
		}

# Genus words -> what the HERO feels like.
_HERO_THEMES: tuple[tuple[tuple[str, ...], str], ...] = (
		(
				(
						"Dragonborn",
						"Dragon",
						"Drake",
						),
				"draconic",
				),
		(
				(
						"Cleric",
						"Paladin",
						"Acolyte",
						"Priest",
						"Celestial",
						"Aasimar",
						"Moonwell",
						),
				"holy",
				),
		(
				(
						"Elf",
						"Druid",
						"Ranger",
						"Wildkeeper",
						"Fey",
						),
				"sylvan",
				),
		(
				(
						"Undead",
						"Vampire",
						"Tomb",
						"Grave",
						"Haunted",
						),
				"grave",
				),
		(
				(
						"Fiend",
						"Tiefling",
						"Warlock",
						"Cultist",
						),
				"infernal",
				),
		(
				(
						"Orc",
						"Barbarian",
						"Berserker",
						"Goliath",
						"Giant",
						),
				"savage",
				),
		(
				(
						"Wizard",
						"Sorcerer",
						"Sage",
						"Scholar",
						"Mage",
						),
				"arcane",
				),
		(
				(
						"Dwarf",
						"Mason",
						"Smith",
						),
				"deep",
				),
		(
				(
						"Rogue",
						"Criminal",
						"Charlatan",
						"Spy",
						"Shadowmasters",
						),
				"shadow",
				),
		(
				(
						"Farmer",
						"Herder",
						"Fisher",
						"Guide",
						"Wayfarer",
						"Survivalist",
						"Vagabond",
						),
				"rustic",
				),
		)


# The stories half of the double mapping: not where a people lived, but
# which shelf of the library their gear walked out of.
_LEGEND_NOUNS: dict[str, dict[str, tuple[str, ...]]] = {
		"tolkien_elves": {
				"Longsword": ("Elven Blade", "Elf-Sword", "Star-Glass Blade"),
				"Shortsword": ("Elven Knife", "Grey-Leaf Blade"),
				"Dagger": ("Elf-Knife", "Leaf Knife"),
				"Longbow": ("Galadhrim Bow", "Wood-Elf Bow"),
				"Shortbow": ("Elven Curve",),
				"Spear": ("Silverthorn Spear",),
				"Chain Shirt": ("Mithril Shirt",),
				},
		"tolkien_dwarves": {
				"Battleaxe": ("Rune-Axe", "Delving Axe"),
				"Greataxe": ("Mattock of the Deeps",),
				"Warhammer": ("Rune-Hammer", "Deep-Delver's Hammer"),
				"Maul": ("Mountain-Breaker",),
				"War Pick": ("Delving Pick",),
				"Chain Mail": ("Mithril Mail",),
				"Chain Shirt": ("Mithril Shirt",),
				"Shield": ("Iron-Bound Shield",),
				},
		"folklore_dwarf": {
				"Light Hammer": ("Tapping Hammer", "Knocker's Hammer"),
				"War Pick": ("Kobold's Pick", "Seam-Tapper"),
				"Warhammer": ("Nisse Hammer",),
				"Handaxe": ("Wood-Sprite's Axe",),
				"Dagger": ("Whittling Knife",),
				},
		"fairytale_fae": {
				"Dagger": ("Thorn Knife", "Cold Iron Knife", "Briar Fang"),
				"Rapier": ("Needle", "Thistle-Point"),
				"Shortsword": ("Bramble Blade",),
				"Quarterstaff": ("Hazel Wand", "Rowan Staff"),
				"Whip": ("Bramble Lash",),
				"Sickle": ("Moon-Sickle",),
				"Sling": ("Acorn Sling",),
				},
		"eragon_dragons": {
				"Longsword": ("Rider's Blade", "Oath-Sworn Blade"),
				"Greatsword": ("Wyrmrider's Greatblade",),
				"Glaive": ("Wing-Cutter Glaive",),
				"Lance": ("Skylance",),
				"Scale Mail": ("Rider's Scale",),
				},
		"wyrm_myth": {
				"Longsword": ("Dragonslayer", "Wyrmbane"),
				"Greatsword": ("Hoard-Cleaver", "Serpent's Bane"),
				"Spear": ("Wyrm-Spear", "Serpent Lance"),
				"Lance": ("Dragon Lance",),
				"Shield": ("Scale-Faced Shield",),
				},
		"arabian_nights": {
				"Scimitar": ("Djinn's Scimitar", "Moonlit Sabre"),
				"Dagger": ("Wish-Knife", "Lamp-Keeper's Dagger"),
				"Quarterstaff": ("Wind-Staff",),
				"Whip": ("Sandstorm Lash",),
				"Sling": ("Roc-Feather Sling",),
				"Trident": ("Marid's Trident",),
				},
		"arthuriana": {
				"Longsword": ("Kingsword", "Sword in the Stone", "Oathblade"),
				"Greatsword": ("Grail-Knight's Greatsword",),
				"Lance": ("Tourney Lance", "Questing Lance"),
				"Mace": ("Chapel Mace",),
				"Shield": ("Blazoned Shield", "Heater of Arms"),
				"Plate": ("White Harness",),
				"Half Plate": ("Questing Harness",),
				},
		"sword_and_sorcery": {
				"Greataxe": ("Reaver's Axe", "Barbarian's Great Axe"),
				"Greatsword": ("Atlantean Greatsword",),
				"Battleaxe": ("Reaver's Axe",),
				"Longsword": ("Broadsword of the Wastes",),
				"Hide": ("Beast-Pelts",),
				"Shield": ("Hide-Bound Shield",),
				},
		"grimdark": {
				"Greatsword": ("Warglaive", "Executioner's Slab"),
				"Flail": ("Penitent's Flail",),
				"Morningstar": ("Heretic's Star",),
				"Dagger": ("Oath-Breaker's Knife",),
				"Whip": ("Chastening Lash",),
				"Halberd": ("Witch-Hunter's Poleaxe",),
				},
		"clockpunk": {
				"Hand Crossbow": ("Ratchet Crossbow", "Clockwork Hand-Bow"),
				"Light Crossbow": ("Geared Crossbow",),
				"Heavy Crossbow": ("Windlass Engine",),
				"Pistol": ("Wheel-Lock Pistol",),
				"Musket": ("Wheel-Lock Musket",),
				"Light Hammer": ("Gearwright's Hammer",),
				"Dart": ("Spring-Loaded Bolt",),
				},
		"anime": {
				"Longsword": ("Nameless Blade", "Sword of the Wandering Style"),
				"Greatsword": ("Impossible Greatblade",),
				"Quarterstaff": ("Sealing Staff",),
				"Dagger": ("Paired Kunai",),
				"Dart": ("Throwing Star",),
				"Sickle": ("Twin Kama",),
				"Shortsword": ("Reverse-Blade Sword",),
				},
		}


def _vocabulary() -> dict[str, dict[str, tuple[str, ...]]]:
	"""Both halves of the naming map, read as one. Peoples and legends."""
	merged = {}
	for source in (
			_CULTURAL_NOUNS,
			_LEGEND_NOUNS,
			):
		for culture, entries in source.items():
			into = merged.setdefault(
					culture,
					{},
					)
			for item_name, nouns in entries.items():
				into[item_name] = into.get(
						item_name,
						(),
						) + nouns
	return merged

# Where the two axes MEET, the pairing has its own name. This is the whole
# point: "Scales" is not a defensive word or a draconic word, it is what a
# draconic defensive thing is called.
_PAIRED: dict[tuple[str, str], tuple[str, ...]] = {
		("warding", "draconic"): ("Scales", "the Wyrm's Hide"),
		("warding", "holy"): ("Redemption", "the Vigil", "Sanctuary"),
		("warding", "sylvan"): ("Bark", "the Deep Grove"),
		("warding", "grave"): ("the Cairn", "Still Earth"),
		("warding", "infernal"): ("the Bargain", "Cold Iron"),
		("warding", "savage"): ("the Standing Stone", "Unbroken"),
		("warding", "arcane"): ("the Sigil", "the Seventh Ward"),
		("warding", "deep"): ("the Anvil", "Mountain's Patience"),
		("warding", "shadow"): ("the Unseen Step", "Quiet Refusal"),
		("cruel", "draconic"): ("Embers", "the Devouring"),
		("cruel", "holy"): ("Judgement", "the Reckoning"),
		("cruel", "sylvan"): ("Bramble", "the Long Winter"),
		("cruel", "grave"): ("the Barrow", "Cold Appetite"),
		("cruel", "infernal"): ("the Pact-Debt", "Sinner's Due"),
		("cruel", "savage"): ("the Red Hour", "Ruin"),
		("cruel", "arcane"): ("Unmaking", "the Last Word"),
		("cruel", "deep"): ("the Deep Seam", "Hammerfall"),
		("cruel", "shadow"): ("the Quiet Debt", "Last Regret"),
		("keen", "draconic"): ("the Hunting Eye", "Talon"),
		("keen", "holy"): ("Clear Sight", "the Revealed"),
		("keen", "sylvan"): ("the Long Sight", "Hawkfeather"),
		("keen", "grave"): ("the Sure Hour", "Certain Ending"),
		("keen", "infernal"): ("the Named Hour", "Whispered Aim"),
		("keen", "savage"): ("the True Cast", "First Blood"),
		("keen", "arcane"): ("the Traced Line", "Calculated Ruin"),
		("keen", "deep"): ("the Measured Blow", "True Temper"),
		("keen", "shadow"): ("the Found Gap", "One Breath"),
		("enduring", "draconic"): ("the Long Hoard", "Ages"),
		("enduring", "holy"): ("the Long Vigil", "Steadfast Faith"),
		("enduring", "sylvan"): ("Old Root", "the Standing Oak"),
		("enduring", "grave"): ("the Patient Dust", "What Remains"),
		("enduring", "savage"): ("the Unyielding", "Stubborn Bone"),
		("enduring", "deep"): ("Bedrock", "the Deep Hold"),
		("swift", "sylvan"): ("the Running Deer", "Windstep"),
		("swift", "shadow"): ("the Quick Exit", "Fleet Shadow"),
		("swift", "draconic"): ("Wingbeat", "the Stooping Wyrm"),
		("watchful", "holy"): ("the Watchful Dawn", "First Warning"),
		("watchful", "shadow"): ("the Open Eye", "No Surprises"),
		("watchful", "grave"): ("the Sleepless", "Restless Watch"),
		("warding", "rustic"): ("Thatch and Iron", "the Homestead"),
		("cruel", "rustic"): ("the Lean Year", "Harvest's End"),
		("keen", "rustic"): ("the Straight Furrow", "True Sowing"),
		("enduring", "rustic"): ("the Long Season", "Weathered"),
		("swift", "rustic"): ("the Market Road", "Quick Errand"),
		("watchful", "rustic"): ("the Night Watch", "Fox in the Coop"),
		}

# When only one axis speaks.
_CRAFT_ONLY: dict[str, tuple[str, ...]] = {
		"warding": ("Warding", "the Bulwark", "Refusal"),
		"cruel": ("Ruin", "the Wound", "Sorrows"),
		"keen": ("the Keen Edge", "True Aim"),
		"enduring": ("Endurance", "the Long Road"),
		"swift": ("Swiftness", "the Quick Path"),
		"watchful": ("Vigilance", "the Open Eye"),
		}

_HERO_ONLY: dict[str, tuple[str, ...]] = {
		"draconic": ("Scales", "the Wyrm"),
		"holy": ("the Dawn", "Redemption"),
		"sylvan": ("the Green", "Old Wood"),
		"grave": ("the Grave", "Ash"),
		"infernal": ("the Bargain", "Embers"),
		"savage": ("the Red Hour", "the Wild"),
		"arcane": ("the Sigil", "Secrets"),
		"deep": ("the Deep", "the Anvil"),
		"shadow": ("the Unseen", "Whispers"),
		"rustic": ("the Furrow", "Plain Work", "the Homestead"),
		}


def _genus_of(
		target,
		) -> str:
	genus = getattr(
			target,
			"genus",
			None,
			)
	return str(
			target
			if genus is None
			else genus
			)


def _catalogue_names() -> frozenset[str]:
	"""Every real item name, so a title never borrows one from a rival."""
	global _CATALOGUE
	if _CATALOGUE is None:
		names: set[str] = set()
		try:
			from AtlasInventarium.Ledger_of_Armors import ARMORS_BY_NAME
			from AtlasInventarium.Ledger_of_Weapons import WEAPONS_BY_NAME
			names |= set(
					WEAPONS_BY_NAME
					)
			names |= set(
					ARMORS_BY_NAME
					)
		except Exception:
			pass
		_CATALOGUE = frozenset(
				names
				)
	return _CATALOGUE


_CATALOGUE: frozenset[str] | None = None


def noun_for(
		item,
		rng: random.Random,
		target=None,
		) -> str | None:
	"""
	What to call this kind of thing — Blade, Stinger, Pitchfork.

	Looked up by EXACT name, so a Sling is never called a Bow and a Maul is
	never called a Mace. When the hero's trade renames the thing outright
	(a farmer's spear is a pitchfork) that wins, because it says more.

	A noun that is the real name of a DIFFERENT item is rejected: a Maul
	titled "Mace of the Red Hour" reads as a Mace, and a reader cannot tell
	the flourish from the stat block. Only the item's own name may repeat.
	"""
	name = getattr(
			item,
			"name",
			"",
			) or ""
	taken = _catalogue_names() - {
			name,
			}

	def honest(
			nouns,
			):
		return [
				noun
				for noun in nouns
				if noun not in taken
				]

	# Everything WEIGHTS the same pool; nothing short-circuits it. An early
	# return here meant a Dragonborn's draconic trade-name masked their
	# culture entirely, so the one species that should reach for a Katana
	# never did. Julio: the inspirations are orientative, not mandatory.
	pool = honest(
			_generic_nouns(
					name
					)
			) * _GENERIC_WEIGHT

	if target is not None:
		theme = hero_theme(
				target
				)
		if theme:
			pool = pool + honest(
					_THEMED_NOUNS.get(
							(
									theme,
									name,
									),
							(),
							)
					) * _TRADE_WEIGHT

		# Already weighted by influences_of() — do not multiply again.
		pool = pool + honest(
				cultural_nouns(
						item,
						target,
						)
				)

	if pool:
		return rng.choice(
				pool
				)
	return None


def craft_theme(
		item,
		) -> str | None:
	"""The feel of whatever has been forged onto this item."""
	try:
		from AtlasInventarium.Grimoire_of_Crafts import crafts_on
		for craft in crafts_on(
				item
				):
			theme = _CRAFT_THEME.get(
					craft.NAME
					)
			if theme:
				return theme
	except Exception:
		pass
	return None


def hero_theme(
		target,
		) -> str | None:
	"""The feel of the hero who carries it."""
	genus = _genus_of(
			target
			).lower()
	for words, theme in _HERO_THEMES:
		if any(
				word.lower() in genus
				for word in words
				):
			return theme
	return None


def cultures_of(
		target,
		) -> tuple[str, ...]:
	"""
	Every culture this hero draws vocabulary from — usually one, sometimes two.

	Species is the main axis, and a species may hold SEVERAL markers rather
	than one blended label: a Dragonborn is Japan *and* Aztec, a Human is
	Africa, Egypt, the Maghreb and Carthage. Monks add a ninja register on top
	of whatever their species already gives, so a Dragonborn Monk can reach for
	both a Katana and a Kusarigama.
	"""
	genus = _genus_of(
			target
			).lower()
	held: list[str] = []
	for words, societies, legends in _CULTURES:
		if not any(
				word.lower() in genus
				for word in words
				):
			continue
		for marker in societies + legends:
			if marker not in held:
				held.append(
						marker
						)
	return tuple(
			held
			)


def _markers_of(
		target,
		index: int,
		) -> tuple[str, ...]:
	genus = _genus_of(
			target
			).lower()
	held: list[str] = []
	for row in _CULTURES:
		if not any(
				word.lower() in genus
				for word in row[0]
				):
			continue
		for marker in row[index]:
			if marker not in held:
				held.append(
						marker
						)
	return tuple(
			held
			)


def societies_of(
		target,
		) -> tuple[str, ...]:
	"""Just the real peoples — the history half of the double mapping."""
	return _markers_of(
			target,
			1,
			)


def legends_of(
		target,
		) -> tuple[str, ...]:
	"""Just the stories — the genre half of the double mapping."""
	return _markers_of(
			target,
			2,
			)


def influences_of(
		target,
		) -> dict[str, int]:
	"""
	Every culture within this hero's reach, and how strongly.

	Their own culture(s) at full weight, then whoever those peoples traded
	with, conquered, or lived beside, at a fraction. This is what makes the
	setting a NETWORK rather than a set of sealed boxes: a Dwarf mostly names
	things in Iberian, but sometimes reaches for the Andalusi or Punic word,
	because those peoples were never actually separate.
	"""
	reach: dict[str, int] = {}
	held = cultures_of(
			target
			)
	if not held:
		return reach

	# The budget is SHARED, so holding four markers means drawing on four
	# traditions — not speaking four times as loudly as everyone else.
	share = _CULTURAL_BUDGET // len(
			held
			)

	for culture in held:
		reach[culture] = reach.get(
				culture,
				0,
				) + share
		for neighbour, weight in _INFLUENCES.get(
				culture,
				(),
				):
			reach[neighbour] = reach.get(
					neighbour,
					0,
					) + max(
					1,
					share * weight // _INFLUENCE_SCALE,
					)

	return reach


def cultural_nouns(
		item,
		target,
		) -> tuple[str, ...]:
	"""
	Names this hero's culture and its influences would use for this item.

	Returns a WEIGHTED list — a name repeats once per point of reach — so a
	single ``rng.choice`` over it lands on the hero's own vocabulary most of
	the time and on a neighbour's occasionally.
	"""
	name = getattr(
			item,
			"name",
			"",
			) or ""
	weighted: list[str] = []
	vocabulary = _vocabulary()

	for culture, weight in influences_of(
			target
			).items():
		for noun in vocabulary.get(
				culture,
				{},
				).get(
				name,
				(),
				):
			weighted.extend(
					[
							noun,
							] * weight
					)

	return tuple(
			weighted
			)


def epithet_pool(
		item,
		target,
		) -> tuple[str, ...]:
	"""Every "of X" this item and hero could justify, best source first."""
	craft = craft_theme(
			item
			)
	hero = hero_theme(
			target
			)

	if craft and hero:
		paired = _PAIRED.get(
				(
						craft,
						hero,
						)
				)
		if paired:
			return paired

	if craft:
		return _CRAFT_ONLY[craft]
	if hero:
		return _HERO_ONLY[hero]
	return ()


def epithet(
		item,
		target,
		rng: random.Random,
		) -> str | None:
	"""The "of X" — the pairing first, then whichever axis still speaks."""
	pool = epithet_pool(
			item,
			target,
			)
	if not pool:
		return None
	return rng.choice(
			pool
			)


def _echoes(
		noun: str,
		phrase: str,
		) -> bool:
	"""
	True when the epithet just says the noun again.

	"Wyrmtooth of the Wyrm" and "Deep Sledge of the Deep" are the failure
	this prevents — the flourish should add a second idea, not repeat the
	first one back.
	"""
	flat = noun.lower().replace(
			"-",
			"",
			).replace(
			" ",
			"",
			)
	for word in phrase.lower().replace(
			"-",
			" ",
			).split():
		if len(
				word
				) < 4 or word == "the":
			continue
		if word in flat or flat in word:
			return True
		# Stem compare too, or "Scaled Blade of Scales" survives on a plural.
		stem = word[:5]
		if len(
				stem
				) >= 5 and stem in flat:
			return True
	return False


def gear_title(
		item,
		target,
		rng: random.Random | None = None,
		) -> str | None:
	"""
	Compose "<Noun> of <Epithet>", or None when neither axis has anything.

	Returning None is meaningful: a plain Club carried by a plain farmhand
	should stay a Club, not become the Cudgel of Nothing In Particular.
	"""
	if rng is None:
		seed = getattr(
				target,
				"seed",
				None,
				)
		if seed is None:
			seed = _genus_of(
					target
					)
		rng = random.Random(
				f"{seed}:{getattr(item, 'name', '')}:gear_title"
				)

	pool = epithet_pool(
			item,
			target,
			)
	if not pool:
		return None

	# Noun first, so the epithet can avoid simply repeating it.
	noun = noun_for(
			item,
			rng,
			target,
			) or getattr(
			item,
			"name",
			None,
			)
	if not noun:
		return None

	fresh = [
			candidate
			for candidate in pool
			if not _echoes(
					noun,
					candidate,
					)
			]
	chosen = rng.choice(
			fresh or list(
					pool
					)
			)

	return f"{noun} of {chosen}"


__all__ = (
		"craft_theme",
		"cultural_nouns",
		"cultures_of",
		"epithet",
		"gear_title",
		"hero_theme",
		"influences_of",
		"legends_of",
		"noun_for",
		"societies_of",
		)


def _self_test():
	from AtlasInventarium.Grimoire_of_Crafts import (
			Of_Defense,
			Of_Ruin,
			forge,
			)
	from AtlasInventarium.ItemKit import instantiate
	from AtlasInventarium.Ledger_of_Armors import Shield
	from AtlasInventarium.Ledger_of_Weapons import Longsword, Mace

	class Hero:
		def __init__(
				self,
				genus,
				level=20,
				seed=3,
				):
			self.genus = genus
			self.level = level
			self.seed = seed

	dragonborn = Hero(
			"Dragonborn , Fighter , Soldier , Champion , He , True Neutral"
			)
	cleric = Hero(
			"Human , Cleric , Acolyte , Light , She , True Good"
			)

	# --- Julio's two examples, from the HERO axis alone -------------------
	# Note: warding crafts are armour-only (Grimoire_of_Crafts applies_to),
	# so an uncrafted blade in a Dragonborn's hand still earns its name from
	# who carries it.
	assert hero_theme(
			dragonborn
			) == "draconic"
	blade = instantiate(
			Longsword
			)
	title = gear_title(
			blade,
			dragonborn,
			random.Random(
					0
					),
			)
	assert title is not None and title.split(
			" of "
			)[1] in (
			"Scales",
			"the Wyrm",
			), title
	# The noun draws on all three layers at once — generic, the draconic
	# trade names, and every culture within reach — so a Dragonborn's Longsword
	# may be a Longsword, a Drake-Fang, a Katana or a Macuahuitl Sword.
	legal = set(
			_generic_nouns(
					"Longsword"
					)
			) | set(
			_THEMED_NOUNS[
					(
							"draconic",
							"Longsword",
							)
					]
			) | set(
			cultural_nouns(
					blade,
					dragonborn,
					)
			)
	assert title.split(
			" of "
			)[0] in legal, (
			f"{title} — noun outside the weighted pool {sorted(legal)}"
			)

	mace = instantiate(
			Mace
			)
	holy = gear_title(
			mace,
			cleric,
			random.Random(
					1
					),
			)
	assert holy is not None and holy.split(
			" of "
			)[1] in (
			"the Dawn",
			"Redemption",
			), holy
	# A cleric's mace is a censer — the trade renames the thing.
	assert holy.split(
			" of "
			)[0] in _THEMED_NOUNS[
			(
					"holy",
					"Mace",
					)
			], holy

	# --- both axes: the PAIRING wins, and says something neither could ----
	from AtlasInventarium.Ledger_of_Armors import Splint

	mail = instantiate(
			Splint
			)
	forge(
			mail,
			Of_Defense,
			hero=dragonborn,
			)
	assert craft_theme(
			mail
			) == "warding"
	paired = gear_title(
			mail,
			dragonborn,
			random.Random(
					5
					),
			)
	assert paired.split(
			" of "
			)[1] in (
			"Scales",
			"the Wyrm's Hide",
			), paired

	# --- the mechanical vocabulary survives --------------------------------
	assert mail in Of_Defense, "the Craft Tag must remain queryable"
	assert mail.grants.get(
			"AC",
			) == 1, "of Defense must still mean +1 AC"
	# The bonus is FOLDED into the armour line (Splint 17 + 1 = 18) rather
	# than tacked on as "+1 AC" — the reader should not do the sum.
	assert "AC 18" in mail.blurb(), mail.blurb()

	# --- a weapon's own craft steers it too --------------------------------
	from AtlasInventarium.Ledger_of_Weapons import Greatsword

	cruel = instantiate(
			Greatsword
			)
	forge(
			cruel,
			Of_Ruin,
			hero=dragonborn,
			)
	assert craft_theme(
			cruel
			) == "cruel"
	cruel_title = gear_title(
			cruel,
			dragonborn,
			random.Random(
					6
					),
			)
	assert cruel_title.split(
			" of "
			)[1] in (
			"Embers",
			"the Devouring",
			), cruel_title

	# --- neither axis: stay a Club ----------------------------------------
	# Genuinely themeless — a Farmer would now read as "rustic".
	nobody = Hero(
			"Human , Commoner , Merchant , He , True Neutral"
			)
	assert hero_theme(
			nobody
			) is None
	plain = instantiate(
			Longsword
			)
	assert gear_title(
			plain,
			nobody,
			random.Random(
					3
					),
			) is None, "an unremarkable thing keeps its plain name"

	# --- shields and armour get their own nouns ---------------------------
	shield = instantiate(
			Shield
			)
	forge(
			shield,
			Of_Defense,
			hero=dragonborn,
			)
	shield_title = gear_title(
			shield,
			dragonborn,
			random.Random(
					4
					),
			)
	# Shields have their own nouns, generic or cultural — never a weapon's.
	shield_legal = set(
			_generic_nouns(
					"Shield"
					)
			) | set(
			cultural_nouns(
					shield,
					dragonborn,
					)
			)
	assert shield_title.split(
			" of "
			)[0] in shield_legal, (
			f"{shield_title} — outside {sorted(shield_legal)}"
			)

	# --- EVERY catalogue item can be named, and never borrows a rival's ----
	# Regressions this guards: a Maul titled "Mace of the Red Hour" (reads as
	# a different weapon), and Whip / Musket / Pistol falling through the old
	# substring groups with no name at all.
	from AtlasInventarium.Ledger_of_Armors import ARMORS
	from AtlasInventarium.Ledger_of_Weapons import WEAPONS

	catalogue = _catalogue_names()
	everything = list(
			WEAPONS
			) + list(
			ARMORS
			) + [
			Shield,
			]

	for record in everything:
		assert record.name in _NOUNS, (
				f"{record.name} has no entry in _NOUNS — it would go unnamed"
				)
		copy = instantiate(
				record
				)
		named = False
		for attempt in range(
				8,
				):
			noun = noun_for(
					copy,
					random.Random(
							attempt
							),
					)
			if noun is None:
				continue
			named = True
			assert noun == copy.name or noun not in catalogue, (
					f"{copy.name} would be titled with another item's name: {noun}"
					)
		assert named, f"{copy.name} never produced a noun"

	# themed overrides must be honest too, and must key on a real item
	for (theme, item_name), nouns in _THEMED_NOUNS.items():
		assert item_name in _NOUNS, (
				f"themed noun keys unknown item {item_name!r}"
				)
		for noun in nouns:
			assert noun == item_name or noun not in catalogue, (
					f"themed noun {noun!r} borrows another item's name"
					)

	# --- the epithet must not simply repeat the noun -----------------------
	# Regression: "Wyrmtooth of the Wyrm", "Deep Sledge of the Deep",
	# "Scaled Blade of Scales" (the last survived a whole-word check, hence
	# the stem compare).
	assert _echoes(
			"Wyrmtooth",
			"the Wyrm",
			)
	assert _echoes(
			"Scaled Blade",
			"Scales",
			)
	assert not _echoes(
			"Censer",
			"the Dawn",
			)

	for genus, protos in (
			(
					"Dragonborn , Fighter , Soldier , Champion , He , Neutral",
					(
							Longsword,
							),
					),
			(
					"Dwarf , Fighter , Smith , Champion , She , Legal",
					(
							Mace,
							),
					),
			):
		who = Hero(
				genus
				)
		for proto in protos:
			whole = gear_title(
					instantiate(
							proto
							),
					who,
					)
			if whole and " of " in whole:
				head, tail = whole.split(
						" of ",
						1,
						)
				assert not _echoes(
						head,
						tail,
						), f"title echoes itself: {whole}"

	# --- a hero's trade renames the thing ---------------------------------
	from AtlasInventarium.Ledger_of_Weapons import Spear

	farmer = Hero(
			"Human , Fighter , Farmer , Champion , He , True Neutral"
			)
	assert hero_theme(
			farmer
			) == "rustic"
	pitchfork = instantiate(
			Spear
			)
	trade_names = set(
			_THEMED_NOUNS[
					(
							"rustic",
							"Spear",
							)
					]
			)
	rolls = [
			noun_for(
					pitchfork,
					random.Random(
							i
							),
					farmer,
					)
			for i in range(
					60,
					)
			]
	# Trade no longer short-circuits — a Human farmer may also reach for an
	# Assegai (their culture) or a plain Spear. What must hold is that the
	# trade name still DOMINATES, which is what the weighting is for.
	share = sum(
			1
			for roll in rolls
			if roll in trade_names
			) / len(
			rolls
			)
	assert share > 0.4, (
			f"rustic Spear names only {share:.0%} of rolls: "
			f"{sorted(set(rolls))}"
			)

	# --- culture weights the pool without owning it ------------------------
	from AtlasInventarium.Ledger_of_Weapons import Longbow, Shortsword

	dragon_kin = Hero(
			"Dragonborn , Fighter , Soldier , Champion , He , Neutral"
			)
	# Two markers held at once, neither blended into an invented middle:
	# Shinto/Daoist Japan AND the Mexica.
	assert set(
			societies_of(
					dragon_kin
					)
			) == {
			"japan",
			"aztec",
			}
	assert "eragon_dragons" in legends_of(
			dragon_kin
			)
	bow_rolls = {
			noun_for(
					instantiate(
							Longbow
							),
					random.Random(
							i
							),
					dragon_kin,
					)
			for i in range(
					40,
					)
			}
	assert "Yumi Bow" in bow_rolls, bow_rolls
	assert bow_rolls - {
			"Yumi Bow",
			"Daikyu Bow",
			"Gakgung Bow",
			}, "culture must weight the pool, not replace it"

	# Kobolds are draconic AND their own thing — both registers reach them.
	kobold = Hero(
			"Kobold , Fighter , Soldier , Champion , She , Neutral"
			)
	assert set(
			societies_of(
					kobold
					)
			) == {
			"japan",
			"china",
			"korea",
			}
	kobold_swords = {
			noun_for(
					instantiate(
							Longsword
							),
					random.Random(
							i
							),
					kobold,
					)
			for i in range(
					40,
					)
			}
	assert "Katana" in kobold_swords, kobold_swords
	assert "Hwando Sabre" in kobold_swords, kobold_swords
	# …and the influence network reaches further than their own three markers:
	# Indian vocabulary arrives through China.
	assert kobold_swords & {
			"Khanda Sword",
			"Talwar",
			}, kobold_swords

	# Gnomes hold Italy, Germany AND Switzerland — three markers, not a blend.
	from AtlasInventarium.Ledger_of_Armors import Chain_Mail
	from AtlasInventarium.Ledger_of_Weapons import Halberd

	gnome = Hero(
			"Gnome , Fighter , Soldier , Champion , He , Neutral"
			)
	assert set(
			societies_of(
					gnome
					)
			) == {
			"italy",
			"germany",
			"switzerland",
			}
	poleaxes = {
			noun_for(
					instantiate(
							Halberd
							),
					random.Random(
							i
							),
					gnome,
					)
			for i in range(
					48,
					)
			}
	# The German and Swiss words for the halberd — the weapon Switzerland is
	# most known for — should both be reachable.
	assert "Hellebarde" in poleaxes, poleaxes
	assert poleaxes & {
			"Schweizer Halbarte",
			"Sempacher Halbarte",
			}, poleaxes

	# Old Norse is the ELVES' register — but influence, not a wall. The Alps
	# look north, so a Gnome may occasionally reach a Norse word too; what
	# must hold is that an Elf reaches it far more often. Under a network
	# model "never" would be the wrong invariant.
	viking = Hero(
			"Elf , Fighter , Soldier , Champion , They , Neutral"
			)
	assert set(
			societies_of(
					viking
					)
			) == {
			"norse",
			"rus",
			"mongol",
			"celt",
			}
	assert "tolkien_elves" in legends_of(
			viking
			)

	def norse_share(
			who,
			):
		rolls = [
				noun_for(
						instantiate(
								Chain_Mail
								),
						random.Random(
								i
								),
						who,
						)
				for i in range(
						80,
						)
				]
		return sum(
				1
				for roll in rolls
				if roll in (
						"Brynja",
						"Hringserkr Mail",
						)
				) / len(
				rolls
				)

	elf_share = norse_share(
			viking
			)
	gnome_share = norse_share(
			gnome
			)
	assert elf_share > 0.4, f"Elves should mostly speak Norse: {elf_share:.0%}"
	assert gnome_share < elf_share / 2, (
			f"Norse should be a Gnome's accent, not their voice: "
			f"elf {elf_share:.0%} vs gnome {gnome_share:.0%}"
			)

	# A Monk reads ninja on top of whatever species already gives — and anime
	# just as strongly, which is the legend half of the same row.
	monk = Hero(
			"Human , Monk , Guard , Open Hand , He , Neutral"
			)
	assert "ninja" in societies_of(
			monk
			)
	assert "anime" in legends_of(
			monk
			)

	# --- legends name things too, beside the peoples -----------------------
	# Julio (2026-08-05): "'fairytale_elf' or 'folklore_dwarf' … even
	# 'Tolkien_Elfs' and 'Eragon_Dragons', even 'anime' for monks."
	# The two families feed one pool: an Elf may reach for a Norse word, a
	# Tolkien one, or the plain English one, and it is a single roll.
	elf_blades = {
			noun_for(
					instantiate(
							Longsword
							),
					random.Random(
							i
							),
					viking,
					)
			for i in range(
					80,
					)
			}
	assert elf_blades & {
			"Elven Blade",
			"Elf-Sword",
			"Star-Glass Blade",
			}, elf_blades
	assert "Ulfberht Blade" in elf_blades, elf_blades
	assert "Longsword" in elf_blades, "legend must weight the pool, not own it"

	# Every legend marker a species can hold must have vocabulary, or it is
	# a dead entry that silently does nothing.
	for row in _CULTURES:
		for legend in row[2]:
			assert legend in _LEGEND_NOUNS, (
					f"{legend} is claimed by {row[0]} but names nothing"
					)
		for society in row[1]:
			assert society in _CULTURAL_NOUNS, (
					f"{society} is claimed by {row[0]} but names nothing"
					)

	# Every marker referenced by the influence network must exist as well —
	# a typo there is otherwise invisible.
	known = set(
			_CULTURAL_NOUNS
			) | set(
			_LEGEND_NOUNS
			)
	for culture, neighbours in _INFLUENCES.items():
		assert culture in known, f"_INFLUENCES keys unknown marker {culture!r}"
		for neighbour, _weight in neighbours:
			assert neighbour in known, (
					f"{culture} points at unknown marker {neighbour!r}"
					)

	# --- one culture's words must not leak into another --------------------
	# Regression: a Dwarf's spear came out a Yari and a Fey's shortsword a
	# Wakizashi, because culture-marked names sat in the generic pool.
	smith = Hero(
			"Dwarf , Fighter , Smith , Champion , She , Neutral"
			)
	for proto, foreign in (
			(
					Spear,
					"Yari",
					),
			(
					Shortsword,
					"Wakizashi",
					),
			):
		rolls = {
				noun_for(
						instantiate(
								proto
								),
						random.Random(
								i
								),
						smith,
						)
				for i in range(
						40,
						)
				}
		assert foreign not in rolls, (
				f"Dwarf reached for {foreign}: {rolls}"
				)

	# --- deterministic per hero + item ------------------------------------
	again = instantiate(
			Splint
			)
	forge(
			again,
			Of_Defense,
			hero=dragonborn,
			)
	assert gear_title(
			again,
			dragonborn,
			) == gear_title(
			again,
			dragonborn,
			), "same hero and item must always name it the same"

	print(
			f"OK — Map_of_Gear_Titles self-test ("
			f"{len(_CULTURAL_NOUNS)} peoples + {len(_LEGEND_NOUNS)} legends; "
			f"({len(_PAIRED)} pairings; item axis x hero axis, "
			"craft meaning preserved)"
			)


if __name__ == "__main__":
	_self_test()
