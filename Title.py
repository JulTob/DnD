# NPC creator
import random


def Title():
    descriptor = [
        "The Air",
        "The Alcoholic",
        "The Alpha",
        "The Aberrant",
        "The Aprendice of",
        "The Archfey",
        "The Awakened",
        "The Autumn",
        "The Angry",
        "The Avatar",
        "The Arcane",
        "The Ancient",
        "The Badger",
        "The Battle",
        "The Baron of",
        "The Bat",
        "The Bearded",
        "The Beholder",
        "The Blending",
        "The Black",
        "The Blind",
        "The Blue",
        "The Blood",
        "The Bone",
        "The Bursting",
        "The Brass",
        "The Bronce",
        "The Brown",
        "The Brain",
        "The Butterfly",
        "The Cat",
        "The Climate",
        "The Chain",
        "The Champion",
        "The Chief",
        "The Circus",
        "The City",
        "The Collector",
        "The Conjurer",
        "The Coral",
        "The Clokwork",
        "The Copper",
        "The Cursed",
        "The Crab",
        "The Crimson",
        "The Crown",
        "The Deadly",
        "The Death",
        "The Dawning",
        "The Dark",
        "The Devourer of",
        "The Doctor",
        "The Deep",
        "The Divine",
        "The Diviner",
        "The Dream",
        "The Dust",
        "The Eagle",
        "The Equinox",
        "The Equivalence",
        "The Emphasis",
        "The Emmerald",
        "The Enchanted",
        "The Engine",
        "The Energy",
        "The Errant",
        "The Earth",
        "The Errant",
        "The Fleshwork",
        "The Fire",
        "The First",
        "The Fool",
        "The Forest",
        "The Fullmetal",
        "The Flying",
        "The Flame",
        "The Fury",
        "The Giant",
        "The Gas",
        "The Green",
        "The God",
        "The Golden",
        "The Great",
        "The Gladiator",
        "The Guard",
        "The Guardian",
        "The Hell",
        "The Hill",
        "The High",
        "The Hive",
        "The Hunter",
        "The Hungry",
        "The Impulse",
        "The Inkwork",
        "The Iron",
        "The Ironbark",
        "The Ice",
        "The Icicle",
        "The Ink",
        "The Intellect",
        "The Ignoble",
        "The Illusionist",
        "The Jewelcraft",
        "The Jackal",
        "The Jewel",
        "The Kraken",
        "The Killer",
        "The King's",
        "The King of",
        "The Last",
        "The Lady",
        "The Licht",
        "The Life",
        "The Lightning",
        "The Lizard",
        "The Lord Of the",
        "The Lord Of",
        "The Lonely",
        "The Long",
        "The Love of",
        "The Master",
        "The Mad",
        "The Magic",
        "The Magma",
        "The Marine",
        "The Mental",
        "The Mirror",
        "The Mist",
        "The Minotaur",
        "The Moon",
        "The Mutant",
        "The Mummy",
        "The Night",
        "The Nightmare",
        "The Necromancer",
        "The New",
        "The Noble",
        "The Oceanic",
        "The Orange",
        "The Old",
        "The Owl",
        "The Pack",
        "The Pain",
        "The Paladin",
        "The Plague",
        "The Poisonous",
        "The Powder",
        "The Power",
        "The Punk",
        "The Purifying",
        "The Protector",
        "The Queen's",
        "The Queen of",
        "The Rat",
        "The Rainstorm",
        "The Red",
        "The River",
        "The Rogue",
        "The Ruby",
        "The Rune",
        "The Sad",
        "The Sand",
        "The Science",
        "The Shadow",
        "The Second",
        "The Seventh",
        "The Silver",
        "The Skelleton",
        "The Smiling",
        "The Smoke",
        "The Spring",
        "The Steam",
        "The Storm",
        "The Stone",
        "The Starting",
        "The Stars",
        "The Strong",
        "The Spark",
        "The Spell",
        "The Speaker",
        "The Sphinx",
        "The Solar",
        "The Summer",
        "The Tender",
        "The Third",
        "The Thunder",
        "The Tiger",
        "The True",
        "The Trival",
        "The Tomb",
        "The Valiant",
        "The Vampiric",
        "The Veteran",
        "The Violet",
        "The Voice",
        "The Void",
        "The War",
        "The Warlord",
        "The Warping",
        "The Water",
        "The White",
        "The Wise",
        "The Wind",
        "The Winter",
        "The Wild",
        "The Wolf",
        "The Young",
        "The Zombie",
        "The",
        ""
    ]
    rank = [
        "Abomination",
        "Acolyte",
        "Alchemist",
        "Aprentice",
        "Arrow",
        "Archer",
        "Archfey",
        "Archmage",
        "Armour",
        "Ash",
        "Assassin",
        "Anarchist",
        "Anthropologist",
        "Baboon",
        "Band",
        "Bard",
        "Baron",
        "Basilisk",
        "Benefactor",
        "Berserker",
        "Bear",
        "Beholder",
        "Blade",
        "Bow",
        "Bringer",
        "Breeder",
        "Butterfly",
        "Beetle",
        "Burglar",
        "Bull",
        "Cat",
        "Camel",
        "Captain",
        "Chemist",
        "Champion",
        "Charlatan",
        "Chimera",
        "Collector",
        "Collosus",
        "Commander",
        "Cultist",
        "Dancer",
        "Darkness",
        "Diamond",
        "Dino",
        "Deer",
        "Death",
        "Devil",
        "Doctor",
        "Doom",
        "Dragon",
        "Drake",
        "Druid",
        "Dream",
        "Drone",
        "Devourer",
        "Eagle",
        "Eater",
        "Eclipse",
        "Enforcer",
        "Elite",
        "Elk",
        "Element",
        "Farmer",
        "Fanatic",
        "Fire",
        "Fury",
        "Flutist",
        "Flame",
        "Freedomfighter",
        "Forged",
        "Gargoyle",
        "Genius",
        "Giant",
        "Grandmaster",
        "Ghost",
        "Golem",
        "Goat",
        "Guard",
        "Hand",
        "Hag",
        "Hawk",
        "Heir",
        "Hermit",
        "Hero",
        "Hive",
        "Horror",
        "Hound",
        "Hunter",
        "Hunger",
        "Hyena",
        "Hydra",
        "Inquisitor",
        "Incubus",
        "Intellect",
        "Jackal",
        "Knight",
        "Killer",
        "Knife",
        "King",
        "Kiss",
        "Leader",
        "Lion",
        "Light",
        "Lizard",
        "Lotus",
        "Lord",
        "Lover",
        "Man",
        "Machine",
        "Mage",
        "Magus",
        "Magister",
        "Master",
        "Mastermind",
        "Mastiff",
        "Martyr",
        "Mind",
        "Mist",
        "Monk",
        "Monster",
        "Moon",
        "Mule",
        "Necromancer",
        "Nightmare",
        "Nomad",
        "Of Death",
        "Of Heaven",
        "Of Justice",
        "Of Odin",
        "Of The Abyss",
        "Of the Autumn",
        "Of The Crown",
        "Of The Desert",
        "Of The Dead",
        "Of The East",
        "Of The Forest",
        "Of The Forge",
        "Of The Fiends",
        "Of the Kingdom",
        "Of The Hills",
        "Of the Hells",
        "Of The North",
        "Of The Mountain",
        "Of the Oceans",
        "Of the Old One",
        "Of The Plains",
        "Of the Pack",
        "Of The People",
        "Of The Pharaoh",
        "Of The Sands",
        "Of The Sea",
        "Of The South",
        "Of The Summer",
        "Of The Spring",
        "Of The Storm",
        "Of The West",
        "Of The Winter",
        "Of Thor",
        "Of Zeus",
        "Oni",
        "One",
        "Oracle",
        "Outlaw",
        "Owl",
        "Pathologist",
        "Paw",
        "Pegasus",
        "Pixie",
        "Pirate",
        "Poet",
        "Priest",
        "Prince",
        "Princess",
        "Prophet",
        "Punk",
        "Queen",
        "Ranger",
        "Rat",
        "Raven",
        "Revenant",
        "Reptile",
        "Rider",
        "Rose",
        "Ruby",
        "Rune",
        "Sabertooth",
        "Saurius",
        "Salamander",
        "Scientist",
        "Scarecrow",
        "Scorpion",
        "Shadow",
        "Shark",
        "Shaman",
        "Sorcerer",
        "Snake",
        "Skeleton",
        "Skull",
        "Surgeon",
        "Sucubus",
        "Spirit",
        "Spider",
        "Specter",
        "Spy",
        "Swashbuckler",
        "Swarm",
        "Sword",
        "Tiger",
        "Terror",
        "Trapper",
        "Trapecist",
        "Troll",
        "Thief",
        "Void",
        "Vampire",
        "Vulture",
        "Walker",
        "Warlock",
        "Warrior",
        "Watch",
        "Werewolf",
        "Wizard",
        "Witch",
        "Witchhunter",
        "Writter",
        "Willow",
        "Wolf",
        "Zombie",
        ""
    ]

    title = random.choice(descriptor) + " " + random.choice(rank)
    return title

print(Title())
