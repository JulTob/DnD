# NPC creator
import random
import json





def ask_chatgpt(question):
    try: 
        import openai

        # Open AI Key
        keyFile = open("key.txt", "r")
        key = keyFile.read()
        openai.api_key = key
        keyFile.close()

        # Use the Completion API to ask the question
        response = openai.Completion.create(
            model = "gpt-3.5-turbo-instruct", #"text-davinci-002", ## You can specify other models as well: "text-davinci-002", "curie", "ada
            prompt=question,
            max_tokens=500,  # Limit the response length, adjust as needed
            temperature=1
        )
        return response.choices[0].text.strip()
    except:
        return ""

def Style():
    styles = [
        "Edgard Allan Poe",
        "Oscar Wilde",
        "J.R.R. Tolkien",
        "George R. R. Martin",
        "Terry Pratchett",
        "Neil Gaiman",
        "Patrick Rothfuss",
        "Ursula K. Le Guin",
        "Stephen King",
        "H. P. Lovecraft",
        "Isaac Asimov",
        "Bram Stoker",
        "Erin Morgenstern",
        "Madeline Miller",
        "Phillip Pullman",
        "F. Scott Fitzgerald",
        "Mark Twain",
        "George Orwell",
        "Fyodor Dostoevsky",
        "Mary Shelley",
        "Lord Byron",
        "William Shakespeare",
        "Fran Kafka",
        "C.S. Lewis",
        "Jorge Luis Borges",
        "Hermann Hesse",
        "Richard Bach",
        "Haruki Murakami",
        "Maya Angelou",
        "Gabriel García Márquez", 
        "Jane Austen",
        "Chinua Achebe",
        "Virginia Woolf",
        "Salman Rushdie",
        "Toni Morrison"
        ]
    return random.choice(styles)


def Title():
    descriptor = [
        "Aberrant",           
        "Ageless",
        "Air",
        "Amazon's",
        "Anachronistic",
        "Ancient",
        "Angry",
        "Arcane",
        "Aegean",
        "Antediluvian",
        "Asgardian",
        "Amazonian",
        "Arachnid",
        "Astral",
        "Atemporal",
        "Autumn",
        "Aprendice of",
        "Archaic",
        "Alcoholic",
        "Alpha",
        "Ancestral",
        "Ancient",
        "Angelic",
        "Atlantean",
        "Avatar",
        "Abyssal",
        "Amulet",
        "Anvil",
        "Arch",
        "Awakened",        
        "Antlered",
        "Apothecary",
        "Aquatic",
        "Archfey",
        "Avian",
        "Azure",

        
        "Babylonian",
        "Baobab's",
        "Blind",
        "Badger",
        "Battle",
        "Battle 's",
        "Brown",
        "Bearded",
        "Beholder",
        "Bone",
        "Book",
        "Bronce",
        "Baron of",
        "Blue",
        "Brain",
        "Circus",
        "Clockwork",
        "Content",
        "Copper",
        "Celestial",
        "Chimeric",
        "City",
        "Climate",
        "Cursed",
        "Celtic",
        "Chain",
        "Cheerful",
        "Chief",
        "Cobalt",
        "Crown",
        "Candle",
        "Champion of",
        "Crab",
        "Cryptic",
        "Divine",
        "Draconian",
        "Dusk",
        "Dwarven",
        "Enchanted",
        "Eldritch",
        "Elven",
        "Epicurean",
        "Fierce",
        "Goldenrod",
        "Midnight",
        "Protector",
        "Scarlet",
        "Stinger-tailed",
        "Tusked",
        "Abbey",
        "Abyssal",
        "Academy",
        "Aerial",
        "Affectionate",
        "Aggressive",
        "Alienated",
        "Amber",
        "Angry",
        "Annoyed",
        "Anxious",
        "Apathetic",
        "Apprehensive",
        "Aquatic",
        "Archipelago",
        "Ardent",
        "Arena",
        "Arrogant",
        "Atmospheric",
        "Auburn",
        "Austere",
        "Aztec",
        "Azure",
        "Badland",
        "Baroque",
        "Barracks",
        "Barren",
        "Battleground",
        "Bay",
        "Beach",
        "Beachy",
        "Beige",
        "Benevolent",
        "Beryl",
        "Bitter",
        "Blazing",
        "Blooming",
        "Blossoming",
        "Boar-tusked",
        "Boastful",
        "Bog",
        "Boggy",
        "Bountiful",
        "Bramble",
        "Brave",
        "Bridge",
        "Bronze",
        "Brook",
        "Brush",
        "Budding",
        "Burgundy",
        "Burned-out"
        "Cannon",
        "Castle",
        "Calm",
        "Camp",
        "Canary",
        "Canopy",
        "Canyon",
        "Capricious",
        "Catacomb",
        "Cathedral",
        "Cautious",
        "Cave",
        "Cavern",
        "Cavernous",
        "Celestial",
        "Cemetery",
        "Cerulean",
        "Chalice",
        "Champagne",
        "Chaotic",
        "Chapel",
        "Charcoal",
        "Chasm",
        "Chest",
        "Chocolate",
        "Chronal",
        "Circus",
        "Citadel",
        "City",
        "Cliff",
        "Clockwork",
        "Coast",
        "Cobalt",
        "Cold",
        "Colonial",
        "Cometary",
        "Compassionate",
        "Confident",
        "Confused",
        "Copper",
        "Coppice",
        "Coral",
        "Cosmic",
        "Crater",
        "Crescent",
        "Crimson",
        "Crown",
        "Cryptic",
        "Crystalline",
        "Cunning",
        "Curious",
        "Cyan",
        "Cyclonic",
        "Cyclopean",
        "Dagger",
        "Dark Matter",
        "Dark",
        "Dashing",
        "Dated",
        "Dauntless",
        "Dawn",
        "Dawning",
        "Dawnlike",
        "Death",
        "Deep",
        "Delta",
        "Depressed",
        "Desert",
        "Desperate",
        "Despondent",
        "Detached",
        "Devourer of",
        "Dewy",
        "Diadem",
        "Disappointed",
        "Discouraged",
        "Distrustful",
        "Diurnal",
        "Divine",
        "Diviner",
        "Dock",
        "Doctor",
        "Dormant",
        "Drained",
        "Dragon's",
        "Dream",
        "Driftwood",
        "Dune",
        "Dungeon",
        "Duskish",
        "Dusky",
        "Dust",
        "Dynamic",
        "Eager",
        "Eagle",
        "Earth",
        "Earthen",
        "Ebony",
        "Echinate",
        "Eclipsed",
        "Eclipsing",
        "Ecliptic",
        "Ecstatic",
        "Edgy",
        "Egotistic",
        "Elated",
        "Electric",
        "Eloquent",
        "Elusive",
        "Emerald",
        "Emmerald",
        "Empathetic",
        "Emphasis",
        "Encampment",
        "Enchanted",
        "Energy",
        "Engine",
        "Enthusiastic",
        "Envious",
        "Ephemeral",
        "Equinox",
        "Equivalence",
        "Errant",
        "Erratic",
        "Ethereal",
        "Evanescent",
        "Excited",
        "Exhausted",
        
        "Factory",
        "Faerie",
        "Fairground",
        "Faithful",
        "Fallen",
        "Farm",
        "Fearful",
        "Fen",
        "Fenririan",
        "Ferocious",
        "Field",
        "Fierce",
        "Fiery",
        "Fire",
        "First",
        "Fjord",
        "Flame",
        "Flaming",
        "Fleshwork",
        "Floral",
        "Flying",
        "Fool",
        "Forest",
        "Forge",
        "Formidable",
        "Fortress",
        "Frosty",
        "Frozen",
        "Frustrated",
        "Fuchsia",
        "Fullmetal",
        "Fullmoon",
        "Furious",
        "Furred",
        "Fury",
        "Futuristic",
        
        "Galactic",
        "Gallant"
        "Deadly",
        "Garden",
        "Gas",
        "Gaseous",
        "Generous",
        "Gentle",
        "Geyser",
        "Giant",
        "Glacial",
        "Glacier",
        "Glade",
        "Gladiator",
        "Gloomy",
        "Glowing",
        "God",
        "Golden",
        "Gorge",
        "Gorgonian",
        "Graceful",
        "Grail",
        "Guardian",
        "Graphite",
        "Guardian of",
        "Grassland",
        "Grassy",
        "Grateful",
        "Graveyard",
        "Gravitational",
        "Great",
        "Green",
        "Grieving",
        "Griffon-winged",
        "Griffonian",
        "Grove",
        "Guard",
        "Guardian",
        "Guardian's",
        "Guildhall",
        "Gulf",
        "Hamlet",
        "Happy",
        "Harbor",
        "Harlequin",
        "Harmonious",
        "Harpylike",
        "Heart",
        "Heartbroken",
        "Heath",
        "Hedgerow",
        "Helian",
        "Heliospheric",
        "Hell",
        "Hermetic",
        "Heroic",
        "Hesperidean",
        "High",
        "Hill",
        "Historic",
        "Hive",
        "Homeric",
        "Hopeful",
        "Horned",
        "Horrified",
        "Hostile",
        "Hourglass",
        "Hourly",
        "Hungry",
        "Hunter",
        "Hunter's",
        "Hydra's",
        "Icarian",
        "Ice",
        "Icicle",
        "Icy",
        "Ignoble",
        "Illusionist",
        "Immortal",
        "Immutable",
        "Impulse",
        "Indifferent",
        "Indigo",
        "Infernal",
        "Ink",
        "Inkwell",
        "Inkwork",
        "Inn's",
        "Inscrutable",
        "Insectoid",
        "Insidious",
        "Inspired",
        "Instantaneous",
        "Intellect",
        "Interested",
        "Interim",
        "Intrepid",
        "Intrigued",
        "Ionized",
        "Irate",
        "Iron",
        "Ironbark",
        "Irritated",
        "Island",
        "Islet",
        "Isolated",
        "Ivory",
        "Jackal",
        "Jacobean",
        "Jade",
        "Jealous",
        "Jewel",
        "Jewelcraft",
        "Jittery",
        "Jotunn",
        "Joyful",
        "Jungle",
        "Keep",
        "Key",
        "Killer",
        "Kind",
        "King of",
        "King's",
        "Kraken's",
        "Krakenesque",
        "Lab",
        "Laboratory"
        "Labyrinth",
        "Labyrinthine",
        "Lady",
        "Lagoon",
        "Lake",
        "Lantern",
        "Last",
        "Lavender",
        "Leafy",
        "Lethal",
        "Library",
        "Lich",
        "Life",
        "Lightning",
        "Lime",
        "Liquid",
        "Lizard",
        "Lonely",
        "Long",
        "Loom",
        "Lord Of the",
        "Lord Of",
        "Love of",
        "Loving",
        "Loyal",
        "Luminous",
        "Lunar",
        "Lupine",
        "Lush",
        "Lyre",
        
        "Mad",
        "Magenta",
        "Magic",
        "Magma",
        "Magnetic",
        "Magnetospheric",
        "Mahogany",
        "Majestic",
        "Malevolent",
        "Mangrove",
        "Manticorian",
        "Marine",
        "Marketplace",
        "Maroon",
        "Marsh",
        "Marshy",
        "Master",
        "Matinal",
        "Mausoleum",
        "Mauve",
        "Maze",
        "Meadow",
        "Medusian",
        "Melancholic",
        "Menagerie",
        "Mental",
        "Mercurial",
        "Mesopotamian",
        "Meteoric",
        "Meteoritic",
        "Metropolis",
        "Mine",
        "Minotaur",
        "Minotaurine",
        "Mirror",
        "Mirthful",
        "Mist",
        "Mistral",
        "Mjolnirian",
        "Mollusk",
        "Molten",
        "Momentary",
        "Monastery",
        "Moon",
        "Moor",
        "Morass",
        "Moss",
        "Motivated",
        "Mountain", 
        "Mountainous",
        "Mournful",
        "Muddy",
        "Mulberry",
        "Mummy",
        "Museum",
        "Mustard",
        "Mutant",
        "Myrmidonic",
        "Mysterious",
        "Mystical",
        "Mythical", 
        "Nebulous",
        "Nemean",
        "Nervous",
        "Nether",
        "Night",
        "Noble",
        "Nocturnal",
        "Nomadic",
        "Nordic",
        "Oasis",
        "Observatory",
        "Obsidian",
        "Obsolete",
        "Ocean",
        "Oceanic",
        "Ochre",
        "Olive",
        "Olympian",
        "Omniscient",
        "Onyx",
        "Optimistic",
        "Opulent",
        "Oracular",
        "Orb",
        "Orchard",
        "Orchid",
        "Orphean",
        "Outpost",
        "Outraged",
        "Overwhelmed",
        "Owl-eyed",
        "Ozone",
        "Pack",
        "Palace",
        "Pandoran",
        "Panicked",
        "Park",
        "Passionate",
        "Peaceful",
        "Peach",
        "Pearl",
        "Pebble",
        "Pegasusian",
        "Pendulum",
        "Pensive",
        "Perceptive",
        "Perennial",
        "Periwinkle",
        "Petal",
        "Pewter",
        "Phantasmal",
        "Phoenixian",
        "Phylactery",
        "Pine",
        "Pistachio",
        "Plain",
        "Plasma",
        "Plateau",
        "Pleased",
        "Plum",
        "Plumed",
        "Pond",
        "Port",
        "Poseidonian",
        "Prairie",
        "Prison",
        "Pristine",
        "Profane",
        "Promethean",
        "Prophetic",
        "Proud",
        "Pulsar",
        "Pharaoh's",
        "Pyroclastic",
        "Quagmire",
        "Quarry",
        "Queen's",
        "Quotidian",
        "Radiant",
        "Rainforest",
        "Ranch",
        "Raspberry",
        "Rat",
        "Ravine",
        "Ravishing",
        "Reckless",
        "Reef",
        "Relaxed",
        "Relentless",
        "Reptilian",
        "Resentful",
        "Resilient",
        "Restless",
        "Reverent",
        "Ridge",
        "River",
        "Riverine",
        "Rocky",
        "Romantic",
        "Rooted",
        "Rose",
        "Ruby",
        "Ruins",
        "Rust",
        "Ruthless",
        
        "Sacred",
        "Sad",
        "Salmon",
        "Sanctuary",
        "Sandy",
        "Sapphire",
        "Satisfied",
        "Satyric",
        "Savage",
        "Savanna",
        "Savannah",
        "Scarlet",
        "School",
        "Scrub",
        "Sea",
        "Seal",
        "Seashore",
        "Secular",
        "Seismic",
        "Sepia",
        "Serene",
        "Settlement",
        "Sewer",
        "Seychelle",
        "Shaded",
        "Shadowy",
        "Shore",
        "Shrine",
        "Sienna",
        "Sigil",
        "Silent",
        "Silver",
        "Sirenian",
        "Slate",
        "Slime-covered",
        "Solar",
        "Sorrowful",
        "Spacetime",
        "Sparkling",
        "Spectral",
        "Sprouting",
        "Square",
        "Stadium",
        "Stalwart",
        "Starlit",
        "Steadfast",
        "Steamy",
        "Stellar",
        "Steppe",
        "Stern",
        "Stoic",
        "Stone",
        "Strait",
        "Stratospheric",
        "Stream",
        "Stressed",
        "Studio",
        "Stygian",
        "Subterranean",
        "Sunlit",
        "Supernova",
        "Suspicious",
        "Swamp",
        "Swampy",
        "Sword",
        "Sylvan",
        "Sympathetic",
        "Tangerine",
        "Tapestry",
        "Taupe",
        "Tavern",
        "Tawny",
        "Teal",
        "Tectonic",
        "Tempestuous",
        "Temple",
        "Tenacious",
        "Tender",
        "Tense",
        "Terrified",
        "Theater",
        "Thicket",
        "Thorny",
        "Thundering",
        "Tidal",
        "Tidepool",
        "Timely",
        "Tomb",
        "Topaz",
        "Totem",
        "Tower",
        "Town",
        "Transient",
        "Tudor",
        "Tundra",
        "Tunnel",
        "Turquoise",
        "Twilight",
        "Twisted",
        "Typhoon",
        "Ubiquitous"
        "Swift",
        "Ultramarine",
        "Unemotional",
        "Unhappy",
        "Universal",
        "Unstoppable",
        "Unyielding",
        "Uranian",
        "Ursine",
        "Valiant",
        "Valkyrian",
        "Valley",
        "Vampiric",
        "Vanirian",
        "Vapor",
        "Vellum",
        "Venusian",
        "Verdant",
        "Vermilion",
        "Vernal",
        "Vexing",
        "Vibrant",
        "Vigilant",
        "Village",
        "Vine",
        "Volcanic",
        "Volcano",
        "Voracious",
        "Vulcanian",
        "Ancient",
        "Wily",
        "Windy",
        "Winged",
        "Witchy",
        "Withering"
        "Fiery",
        "Woodland",
        "Woods",
        "Woody",
        "Workshop",
        "Worried",
        "War",
        "Wormhole", 
        "Yesteryear",  
        "Young",
        "Talon-clawed", 
        "Gavel",  
        "X-ray",  
        "Elixir",  
        "Scepter",   
        "Medallion",   
        "Feather",   
        "Goblet",    
        "Urn",   
        "Relic",   
        "Wand",   
        "Parchment",   
        "Telescopic",  
        "Mantle",
        "Radiant",   
        "Spire",
        "Scroll",
        "Satellite",
        "Seasonal",
        "Vessel",
        "Sempiternal",
        "Epochal",
        "Twilight",
        "Primeval",
        "Compass",
        "Millennial",
        "Meridian",
        "Hammer",
        "Eternal",
        "Fleeting",     
        "Black Hole",   
        "Meteoritic",    
        "Edwardian",    
        "Samurai",    
        "Cosmic",   
        "Nebulous",   
        "Norman",   
        "Orbital",   
        "UFO",   
        "Han",   
        "Suborbital",   
        "Gregorian",   
        "Renaissance",  
        "Spartan",   
        "Prohibition",    
        "Crusader",   
        "Hellenistic",   
        "Sanskrit",    
        "Dynastic",   
        "Flapper",   
        "Napoleonic",   
        "Pharaonic",   
        "Victorian",  
        "Void",      
        "Interstellar",    
        "Elizabethan",  
        "Feudal",   
        "Jazz Age",   
        "Cyclic",  
        "Timeless",   
        "Zenith",   
        "Neutron",   
        "Punctual",   
        "Quill",   
        "Romanesque",   
        "Stellar",   
        "Extraterrestrial",  
        "Infinite",   
        "Bat",
        "Bipedal",
        "Black",
        "Blending",
        "Blood",
        "Brass",
        "Brave",
        "Bursting",
        "Butterfly",
        "Byzantine",
        "Cat",
        "Celestial",
        "Collector",
        "Conjurer",
        "Coral",
        "Cosmic",
        "Crimson",
        "Daemonian",
        "Dawn",
        "Draconic",
        "Eagle",
        "Edo",
        "Eternal",
        "Fanged",
        "Feathered",
        "Feline",
        "Finned",
        "Fire-breathing",
        "Fuchsia",
        "Galactic",
        "Gemmed",
        "Gilled",
        "Glacial",
        "Goat-footed",
        "Hoofed",
        "Horned",
        "Icy",
        "Indigo",
        "Leech-mouthed",
        "Luminous",
        "Lunar",
        "Mammalian",
        "Maned",
        "Mask",
        "Melancholy",
        "Mermaid-tailed",
        "Mist",
        "Misty",
        "Momentary",
        "Mountain",
        "Mysterious",
        "Nemean",
        "Nomadic",
        "Oceanic",
        "Olympian",
        "Renaissance",
        "River",
        "Silent",
        "Sirenic",
        "Solar",
        "Stellar",
        "Stoic",
        "Swift",
        "Sword",
        "Tartarean",
        "Thundering",
        "Timeless",
        "Titanic",
        "Trojan",
        "Ultraviolet",
        "Valkyrian",
        "Vampiric",
        "Voidborne",
        "Byzantine", 
        "Medieval", 
        "Staff", 
        "Rune", 
        "Celtic", 
        "Shield", 
        "Mughal", 
        "Vesperal", 
        "Vintage", 
        "Ottoman", 
        "Quasar", 
        "Incan", 
        "Temporal", 
        "Hermitage", 
        "Bygone",
        "Banner",
        "Blade",
        "Brooch",
        "Chiropteran",
        "Crested",
        "Desert",
        "Lion-hearted",
        "Nebulous",
        "Necromancer",
        "New",
        "Nightmare",
        "Noble",
        "Old",
        "Ophidian",
        "Orange",
        "Orb",
        "Owl",
        "Pain",
        "Paladin",
        "Passionate",
        "Pawed",
        "Pegasus-winged",
        "Piscine",
        "Plague",
        "Poisonous",
        "Powder",
        "Power",
        "Punk",
        "Purifying",
        "Queen of",
        "Radiant",
        "Rainstorm",
        "Raptor-clawed",
        "Raven-haired",
        "Red",
        "River",
        "Rogue",
        "Ruby",
        "Rune",
        "Sand",
        "Scaled",
        "Science",
        "Second",
        "Serpentine",
        "Seventh",
        "Shadow",
        "Shark-toothed",
        "Shell-backed",
        "Silver",
        "Simian",
        "Skeleton",
        "Smiling",
        "Smoke",
        "Snail-shelled",
        "Solar",
        "Spark",
        "Speaker",
        "Spell",
        "Sphinx",
        "Spined",
        "Spring",
        "Squirrel-tailed",
        "Stars",
        "Starting",
        "Steam",
        "Stone",
        "Storm",
        "Strong",
        "Summer",
        
        "Tailed",
        "Tamer of",
        "Tentacled",
        "Third",
        "Thunder",
        "Tiger",
        "Tiger-striped",
        "Titan",
        "Tomb",
        "Trival",
        "True",
        "Turquoise",
        
        "Undying",
        "Underworld",
        
        "Vampiric",
        "Venomous",
        "Veteran",
        "Victorian",
        "Victorious",
        "Viking",   
        "Violet",
        "Voice",
        "Void",
        "Vulpine",
        "Vengeful",
        "Valkyrie's",
        
        "Winged",
        "Wandering",
        "Warm",
        "Wary",
        "Waterfall",
        "Watery",
        "Wavy",
        "Web",
        "Werewolfish",
        "Wheel",
        "Whispering",
        "Whistle"
        "Warlord",
        "Warping",
        "Water",
        "Whale",
        "White",
        "Wild",
        "Wind",
        "Windy",
        "Winter",
        "Wise",
        "Wolf",
        "Wolf-pawed"
        "Wrathful",
        "Wight",
        
        "Zodiacal",   
        "Zealous",
        "Zen",
        "Zephyr",
        "Zeusian"
        "Joyful",
        "Zombie",
        "Zoo", 
        ""
    ]




    
    rank = [
    
        "Abbot",
        "Abbess",
        "Abyss",
        "Admiral",
        "Archbishop",
        "Abomination",
        "Abyssal",
        "Acolyte",
        "Admiral",
        "Advent",
        "Adventurer",
        "Aero",
        "Afterlife",
        "Agent",
        "Alchemical Brewer",
        "Alchemist",
        "Alpha",
        "Ambassador",
        "Anarchist",
        "Angel",
        "Anthropologist",
        "Antler",
        "Apostle",
        "Apparition",
        "Apparition",
        "Aprentice",
        "Arcane Detective",
        "Archer",
        "Archer",
        "Archfey",
        "Archmage",
        "Argonaut",
        "Armour",
        "Arrow",
        "Artisan",
        "Ash",
        "Assassin",
        "Assassin",
        "Astral Navigator",
        "Atlas",
        "Augur",
        "Avatar",
        
        "Baboon",
        "Badger",
        "Baker",
        "Band",
        "Banshee",
        "Bard",
        "Baron",
        "Barrow",
        "Basilisk",
        "Battlemage",
        "Beacon",
        "Bear",
        "Bear",
        "Beastmaster",
        "Beetle",
        "Beetle",
        "Beholder",
        "Benefactor",
        "Berserker",
        "Bishop",
        "Bison",
        "Blacksmith",
        "Blade",
        "Blaze",
        "Blighted",
        "Blizzard",
        "Blossom",
        "Boar",
        "Bone",
        "Bounty Hunter",
        "Bow",
        "Bravo",
        "Breeder",
        "Brewer",
        "Briar",
        "Brigadier",
        "Bringer",
        "Buccaneer",
        "Bull",
        "Burglar",
        "Butcher",
        "Butterfly",
        "Buzzard",

        "Cat",
        "Cadaver",
        "Cairn",
        "Camel",
        "Cannibal",
        "Captain",
        "Captain",
        "Cartographer",
        "Cedar",
        "Celestial Mapper",
        "Centurion",
        "Champion",
        "Charlatan",
        "Cheetah",
        "Chemist",
        "Chieftain",
        "Chimera",
        "Claw",
        "Cleric",
        "Climber",
        "Cobbler",
        "Cobra",
        "Collector",
        "Collosus",
        "Commander",
        "Commodore",
        "Conjurer",
        "Conqueror",
        "Corsair",
        "Corsair",
        "Cougar",
        "of the Coliseum",
        "Counselor",
        "Courage",
        "Crow",
        "Crusader",
        "Crusader",
        "Crypt",
        "Cultist",
        "Curator",
        "Curse Breaker",
        "Curse Collector",
        "Cursed Wanderer",
        "Cursed",
        "Cursed",
        "Cyclops",
        
        "Daisy",
        "Dame",
        "Dancer",
        "Daredevil",
        "Darkness",
        "Death",
        "Death",
        "Deathless",
        "Decay",
        "Deer",
        "Defender",
        "Deity",
        "Demigod",
        "Demon",
        "Demonhunter",
        "Desolate",
        "Despot",
        "Devil",
        "Devourer",
        "Diamond",
        "Dimensional Traveler",
        "Dino",
        "Diplomat",
        "Disciple",
        "Discoverer",
        "Djinn",
        "Doctor",
        "Dolphin",
        "Dominator",
        "Doom",
        "Dove",
        "Dragon",
        "Dragon",
        "Drake",
        "Dread",
        "Dream",
        "Drifter",
        "Drone",
        "Druid",
        "Duchess",
        "Duke",
        "Dungeon Delver",
        
        "Eagle",
        "Eagle",
        "Eater",
        "Eclipse Chaser",
        "Eclipse",
        "Ectoplasm",
        "Elder",
        "Eldritch Scholar",
        "Element",
        "Elemental Whisperer",
        "Elite",
        "Elk",
        "Emperor",
        "Empress",
        "Enchantress",
        "Endeavor",
        "Enforcer",
        "Envoy",
        "Ethereal Fisher",
        "Ethereal",
        "Exarch",
        "Executioner",
        "Exile",
        "Exorcist",
        "Expedition",
        "Explorer",

        "Falcon",
        "Falconer",
        "Fallen",
        "Fanatic",
        "Farmer",
        "Farrier",
        "Farwalker",
        "Fawn",
        "Feather",
        "Fel",
        "Fellow",
        "Fern",
        "Ferret",
        "Fiend",
        "Fin",
        "Fire",
        "Flame",
        "Flutist",
        "Foreseer",
        "Forged",
        "Forsaken",
        "Fox",
        "Freedomfighter",
        "Frog",
        "Frontier",
        "Frost",
        "Fury",
        
        "Gale",
        "Gambler of Fate",
        "Gargoyle",
        "Gazelle",
        "General",
        "Genius",
        "Ghast",
        "Ghost Hunter",
        "Ghost",
        "Ghost",
        "Giant",
        "Gladiator",
        "Globetrotter",
        "Goat",
        "Golem",
        "Grandmaster",
        "Grave Robber",
        "Grave",
        "Gravewalker",
        "Guard",
        "Guardian",
        "Great Guardian",
        "Guide",
        "Gull",
        "Guru",
        
        "Hag",
        "Hand",
        "Harbinger",
        "Harpy",
        "Haunt",
        "Hawk",
        "Hawk",
        "Heather",
        "Heir",
        "Herbalist",
        "Heretic",
        "Hermit",
        "Hero",
        "Heron",
        "Highlord",
        "Highness",
        "Hive",
        "Hollow",
        "Holly",
        "Horizon",
        "Horror",
        "Horse",
        "Hound",
        "Hummingbird",
        "Hunger",
        "Hunter",
        "Hunter",
        "Hydra",
        "Hyena",
        
        "Incubus",
        "Infernal",
        "Inquisitor",
        "Intellect",
        "Ivy",
        
        "Jackal",
        "Jackal's",
        "Jaguar",
        "Jasmine",
        "Jay",
        "Jester",
        "Journey",
        "Judge",
        "Juggernaut",
        "Jungle",
        "Juniper",
        
        "Kaiju",
        "Keeper",
        "Kestrel",
        "Killer",
        "King",
        "Kinsman",
        "Kiss",
        "Knife",
        "Knight",
        
        "Lark",
        "Lark",
        "Laurel",
        "Leader",
        "Legate",
        "Legend",
        "Legionnaire",
        "Leopard",
        "Lich",
        "Lich's",
        "Light",
        "Lily",
        "Lion",
        "Lizard",
        "Lord",
        "Lost",
        "Lotus",
        "Lover",
        "Lynx",
        
        "Machine",
        "Mage",
        "Mage for Hire",
        "Magister",
        "Magus",
        "Man",
        "Mantis",
        "Marauder",
        "Marauder",
        "Mare",
        "Marigold",
        "Mariner",
        "Mariner",
        "Marquis",
        "Marshal",
        "Martyr",
        "Mason",
        "Master",
        "Mastermind",
        "Mastiff",
        "Matriarch",
        "Mausoleum",
        "Memento",
        "Mender",
        "Mercenary",
        "Mercenary",
        "Merlin",
        "Mesmer",
        "Messenger",
        "Miller",
        "Mimic",
        "Mind",
        "Minister",
        "Minstrel",
        "Mist",
        "Monk",
        "Monster Hunter",
        "Monster",
        "Moon",
        "Moonlit Merchant",
        "Morgue",
        "Mortal",
        "Mortal",
        "Moth",
        "Mountaineer",
        "Mourner",
        "Mule",
        "Mystic",
        "Mystic Investigator",
        "Mystic Artisan",
        "Beast Rider",
        
        "Naga",
        "Navigator",
        "Necro",
        "Necromancer",
        "Nether",
        "Nightingale",
        "Nightmare",
        "Ninja",
        "Noble",
        "Nocturnal",
        "Nomad",
        
        "Odyssey",
        "Of Death",
        "Of Heaven",
        "Of Justice",
        "Of Odin",
        "Of The Abyss",
        "Of the Autumn",
        "Of The Crown",
        "Of The Dead",
        "Of The Desert",
        "Of The East",
        "Of The Fiends",
        "Of The Forest",
        "Of The Forge",
        "Of The Hells",
        "Of The Hills",
        "Of the Hidden",
        "Of the Kingdom",
        "Of The Mountain",
        "Of The North",
        "Of the Oceans",
        "Of the Old One",
        "Of The Oracle",
        "Of the Pack",
        "Of The People",
        "Of The Pharaoh",
        "Of The Plains",
        "Of The Sands",
        "Of The Sea",
        "Of The South",
        "Of The Spring",
        "Of The Storm",
        "Of The Summer",
        "Of The West",
        "Of The Winter",
        "Of Thor",
        "Of Zeus",
        "One",
        "Oni",
        "Oracle",
        "Orchid",
        "Ossuary",
        "Otter",
        "Outlander",
        "Outlaw",
        "Outrider",
        "Overlord",
        "Owl",
        "Owlbear",
        
        "Paladin",
        "Pale",
        "Panther",
        "Pariah",
        "Parrot",
        "Pathologist",
        "Paw",
        "Pegasus",
        "Pixie",
        "Pirate",
        "Piromaniac",
        "Poet",
        "Priest",
        "Prince",
        "Patriarch",
        "Paw",
        "Peasant",
        "Pilgrim",
        "Pegasus",
        "Peregrine",
        "Petal",
        "Phantom",
        "Phoenix",
        "Pioneer",
        "Pirate",
        "Planar Wanderer",
        "Poltergeist",
        "Poppy",
        "Potter",
        "Primrose",
        "Protege",
        "Prowler",
        "Puma",
        "Princess",
        "Prophet",
        "Punk",
        
        "Quail",
        "Queen",
        "Quest",
        
        "Rabbit",
        "Raider",
        "Ranger",
        "Rat",
        "Raven",
        "Revenant",
        "Reptile",
        "Rider",
        "Rose",
        "Ruby",
        "Rune",
        "Raptor",
        "Raven",
        "Reaper",
        "Reclaimer",
        "Reed",
        "Relic Seeker",
        "Requiem",
        "Restless",
        "Rider",
        "Risen",
        "Ritualist",
        "Rogue",
        "Rogue",
        "Rose",
        "Rowan",
        "Rue",
        "Runesmith",
        
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
        "Stagecoach",
        "Surgeon",
        "Sucubus",
        "Spirit",
        "Spider",
        "Specter",
        "Spy",
        "Swashbuckler",
        "Swarm",
        "Sword",
        "Sage",
        "Sage",
        "Sailor",
        "Saint",
        "Satyr",
        "Savant",
        "Savior",
        "Scout",
        "Scribe",
        "Sea Captain",
        "Seeker",
        "Seer",
        "Sentinel",
        "Sepulcher",
        "Serpent",
        "Serpent",
        "Shade",
        "Shadow",
        "Shark",
        "Shepherd",
        "Sheriff",
        "Shield",
        "Sire",
        "Skeletal",
        "Skyward",
        "Smith",
        "Smuggler",
        "Sorcerer",
        "Sorcerous Duelist",
        "Sorrel",
        "Soul",
        "Soulless",
        "Sparrow",
        "Specter",
        "Spectre",
        "Spellbinder",
        "Spirit",
        "Spook",
        "Spy",
        "Squire",
        "Squire",
        "Settler"
        "Stag",
        "Starship Pilot",
        "Stingray",
        "Storm Chaser",
        "Swallow",
        "Swan",
        "Skywarden",
        
        "Tailor",
        "Talon",
        "Tanner",
        "Tempest",
        "Templar",
        "Thistle",
        "Tiger",
        "Tiger",
        "Terror",
        "Trapper",
        "Trapecist",
        "Troll",
        "Thief",
        "Time Jumper",
        "Titan",
        "Tomb Raider",
        "Tomb",
        "Tormented",
        "Tormentor",
        "Trailblazer",
        "Traveler",
        "Treasure Hunter",
        "Treasure",
        "Turtle",
        "Tyrant",
        
        "Guide",
        "Unholy",
        
        "Vagabond",
        "Valkyrie",
        "Vampire",
        "Vanguard",
        "Vanguard",
        "Vicar",
        "Vigilante",
        "Vigilante",
        "Viking",
        "Vintner",
        "Violet",
        "Viper",
        "Viscount",
        "Void",
        "Voidwalker",
        "Vampire",
        "Vulture",
        "Vagrant",
        "Voyager",
        
        "Wail",
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
        "Wraith",
        "Wanderer",
        "Wandering Healer",
        "Warden",
        "Warlord",
        "Warrior Poet",
        "Wayfarer",
        "Whale",
        "Whirlwind",
        "Whisper",
        "Wight",
        "Wild",
        "Willow",
        "Windrider"
        "Witchfinder",
        "Wolf"
        "Wraith",
        
        
        "Abbess",
        "Abbot",
        "Abysswalker",
        "Acolyte",
        "Celestian",
        "Of Athena",
        "Alchemist",
        "Algonquin's Light",
        "Alpha",
        "Heart",
        "Ambassador",
        "High Ambassador",
        "Ambition",
        "Appetite",
        "Anthropologist",
        "Arcanologist",
        "Archbishop",
        "Archduchess",
        "Archduke",
        "Archer",
        "Archivist",
        "Archmage",
        "Argonaut's Heir",
        "Artificer",
        "Ascendant",
        "Ashanti's Gold",
        "Astral Voyager",
        "Astrologer",
        "Astronomer",
        "Auralist",
        "Auramancer",
        "Avalon's Lost Knight",
        "Avatar",
        "Aztec Avenger",
        "Sentinel",
        "Baba Yaga's Apprentice",
        "Bandana Masked",
        "Banneret",
        "Banshee Wailmistress",
        "Banshee's Wail Seeker",
        "Flight",
        
        "Baron",
        "Barbarian",
        "Bard",
        "Baron",
        "Baron",
        "Baroness",
        "Battle Cleric",
        "Battle Herald",
        "Shaman",
        "Battlefury",
        "Battlemage",
        "Battleseer",
        "Bayou Spirit",
        "Bearer",
        "Beastmaster",
        "Beauty",
        "Berserker",
        "Berserker",
        "Bibliomancer",
        "Biloko's Envy",
        "Bishop",
        "Bison Rider",
        "Blackbeard's Bane"
        "Bladebearer",
        "Bladesinger",
        "Blessing",
        "Boot Hill's Ghost",
        "Botanist",
        "Bow",
        "Breath",
        "Brigadier",
        "Buccaneer of the Burning Seas",
        "Buffalo Soldier",
        "Buffalo Whisperer",
        "Bushman's Dance",
        "Cacao Bringer",  
        "Cacao Mystic",
        "Calico's Cursebreaker",
        "Caliph",
        "Cantor",
        "Captain",
        "Cardinal",
        "Cattle Baron",
        "Cauldronbearer of Cerridwen",
        "Cavalier",
        "Celestial Priest",
        "Celestialist",
        "Celestian",
        "Celestwarden",
        "Centaur Alpha",
        "Centurion",
        "Centurion",
        "Chameleon's Change",
        "Champion",
        "Chancellor",
        "Chancellor",
        "Chaneque's Chosen",
        "Changeling Mimic",
        "Chaplain",
        "Charm",
        "Cheetah's Chase",
        "Chief",
        "Chief",
        "Chieftain",
        "Chronomancer",
        "Chronoshifter",
        "Cibola's Seeker",
        "Claim Jumper",
        "Cleric",
        "Cloudcaller",
        "Codex Keeper",
        "Coil",
        "Combat Priest",
        "Commander",
        "Commander",
        "Condor's Wing",
        "Congo Serpent's Scale",
        "Conquistador",
        "Consul",
        "Consul",
        "Cossack",
        "Councillor",
        "Count",
        "Count",
        "Countess",
        "Covered Wagon's Trail",
        "Coyote's Howl",
        "Coyote's Kin",
        "Craft",
        "Creation",
        "Crocodile's Jaws",
        "Crown",
        "Crusader",
        "Crusader",
        "Cryptozoologist",
        "Cunning",
        "Curator",
        "Czar",

        "Dance",
        "Dangun's Heir",
        "Dawnbringer of Amaterasu",
        "Dawnbringer",
        "Dawncaller"
        "Deacon",
        "Deceiver",
        "Deepseer",
        "Delegate",
        "Demonmask",
        "Demonologist",
        "Depths",
        "Derringer Dame",
        "Descendant",
        "Desert Mirage",
        "Desperado",
        "Despot",
        "Devotion",
        "Dictator",
        "Divine Artisan",
        "Divine Emissary",
        "Divine Herald",
        "Divine Sage",
        "Djinn Sultan",
        "Djinn Whisperer",
        "Djinn's Whimsy",
        "Domovoi's Guardian",
        "Doomsayer",
        "Dragon Knight",
        "Dragonborn Flamecrest",
        "Dragoon",
        "Dragoon",
        "Dreambinder",
        "Dreamcatcher",
        "Dreamer",
        "Dreamforge",
        "Dreamweaver of Zhuang",
        "Dreamweaver",
        "Dreamweaver",
        "Drow Nightshade",
        "Druid of the Enchanted Grove",
        "Druid",
        "Dryad Treebinder",
        "Duchess",
        "Duel's Dawn",
        "Duelist",
        "Duende's Mischiefmate",
        "Duke",
        "Duke",
        "Dungeon Delver",
        "Duskwielder",
        "Dusty Boots",
        "Dwarven Thane",
        "Eagle's Eye",
        "Earl",
        "Earthkeeper",
        "Earthshaper",
        "Echomancer",
        "Eclipse Chaser",
        "Efreet Flamekeeper",
        "El Cid's Successor",
        "Elder",
        "Elder",
        "Elder",
        "Elder",
        "Eldritch Scholar",
        "Elector",
        "Elementalist",
        "Elementward",
        "Elephant's Memory",
        "Elixir",
        "Elvenlady",
        "Elvenlord",
        "Emir",
        "Emissary",
        "Emissary",
        "Emperor",
        "Emperor",
        "Empress",
        "Enchantment Specialist",
        "Encomienda Enchanter",
        "Enigma",
        "Epicseeker of Uruk",
        "Etherbound",
        "Etherscribe",
        "Ethnographer",
        "Exile",
        "of the Bamboo Grove",
        
        "Faith",
        "Fatesealer",
        "Faun Grovekeeper",
        "Feytouched",
        "Feywild Wanderer",
        "Firbolg Earthshaper",
        "Firebrand",
        "Spiral",
        "Flame",
        "Flamecrest",
        "Flamekeeper",
        "Flamekeeper",
        "Flight",
        "Flute",
        "Folklore Weaver of Vasilisa",
        "Fountain of Youth's Guardian",
        "Freya's Heartshield",
        "Friar",
        "Frontier's Flame",
        "Frostbinder of Niflheim",
        "Frostheart of Yuki-onna",
        "Frostweaver",
        "Fulani's Journey",
        "Fury",
        
        "Galeweaver",
        "Gaucho",
        "Gaze",
        "Gemseeker",
        "Genasi Elementward",
        "General",
        "Geomancer",
        "Geomancer",
        "Ghost of La Noche Triste",
        "Ghost Town's Echo",
        "Ghostseer",
        "Giant Cloudcaller",
        "Githyanki Starblade",
        "Githzerai Mindwarden",
        "Gladiator",
        "Gladiator",
        "Glaivemaster",
        "Glimmerblade",
        "Gloomshade",
        "Glow",
        "Gnomish Mastermind",
        "Goblin King",
        "Godsbane Priest",
        "Godspeaker",
        "Gold Nugget's Glint",
        "Gold Rush Seeker",
        "Governor",
        "Governor",
        "Grace",
        "Graceful",
        "Griot's Song",
        "Grovekeeper",
        "Guarani's Dream",
        "of the Faith",
        "of the Forty Thieves",
        "of the Morningstar",
        "of the Thousand Tears",
        "Guardian",
        "Guardian",
        "Gunslinger's Grit",
        "Haetae's Stoneguard",
        "Halfling Leafdancer",
        "Hangman's Noose",
        "Harbinger of Fate"
        "Harpist of Elysium",
        "Harpy Matriarch",
        "Harvestshade of Jacheongbi",
        "Head of State",
        "Heir",
        "Hellstrider",
        "Hellstrider",
        "Herbalist",
        "Hierophant",
        "High Councillor",
        "High Judge",
        "High Priest",
        "High Priestess",
        "Highlander",
        "Historian",
        "Holy Avenger",
        "Holy Enchanter",
        "Homestead's Hope",
        "Honor",
        "Hornbreaker",
        "Horus's Gaze",
        "Hussar",
        "Hydra Slayer",
        "Icarus Skyfall",
        "Illusionist",
        "Immortal Pursuer",
        "Inca's Echo",
        "Inca's Last Defender",
        "Infernalist",
        "Inquisitor",
        "Intrigue",
        "Ironmaw Bulgasari",
        "Ishtar's Chosen",
        "Jaguar Prowler",
        "Janissary",
        "Jarl",
        "Jester",
        "Jormungandr's Foil",
        "Journey",
        "Kenku Storyteller",
        "Khan",
        "King",
        "'s Quest",
        "Knight",
        "Knight",
        "Tunnelchief",
        "Song",
        "Bane",
        
        "Lady",
        "Lamia's Enchanter",
        "Lampbearer of the Forbidden Cave",
        "Lancer",
        "Lasso's Master",
        "Leafdancer",
        "Leap",
        "Legate",
        "Legionnaire",
        "Legionnaire",
        "Lieutenant",
        "Lightbringer",
        "Lightbringer",
        "Lightheart",
        "Linguist",
        "Lion's Roar",
        "Lizardfolk Sunscale",
        "Llama Rider",
        "Logician",
        "Loki's Gambit",
        "Lone Star's Luminary",
        "Lord",
        "Lorekeeper",
        "Lorekeeper",
        "Lorekeeper",
        "Lover of La Llorona",
        "Loyal",
        "Loyalty",
        "Lugh's Spearwielder",
        "Lunarblade",
        "Lycan Alpha",
        "Lynch Mob's Fear",
        
        "Maasai's Spear",
        "Maestro",
        "Mage-Priest",
        "Magistrate",
        "Maize Guardian",
        "Mami Wata's Embrace",
        "Mamluk",
        "Mandingo's Sword",
        "Manitou's Chosen",
        "Mapuche's Might",
        "Marauder of the Caribbean",
        "Marauder",
        "Marchioness",
        "Marduk's Hand",
        "Marshal",
        "Marshal's Might",
        "Martyr",
        "Maskbearer",
        "Matador",
        "Matriarch",
        "Matriarch",
        "Might",
        "Moonmage",
        "Mayor",
        "Maze Runner",  
        "Mazulu's Grace",
        "Medusa's Adversary",
        "Melody",
        "Mender",
        "Mercenary Leader",
        "Mercenary",
        "Merfolk Tidecaller",
        "Mestizo Mage",
        "Metaphysician",
        "Mimic",
        "Mindwarden",
        "Minister",
        "Minotaur Bull",
        "Minotaur's Labyrinth Keeper",
        "Mirage",
        "Mischiefmaster Tanuki",
        "Monarch",
        "Mongol",
        "Monk",
        "Moon Seer",
        "Moon's Maiden",
        "Mooncaller",
        "Moonlady",
        "Moonshadow Samurai",
        "Moonshine's Muse",
        "Morozko's Chillblade",
        "Mountainbreak",
        "Mummy Sandkeeper",
        "Musketeer",
        "Mustang Tamer",
        "Mystagogue",
        "Mystic Archer",
        "Mystic Mestizo",
        "Mystic Seer",
        "Mystic",
        "Mystic",
        "Mystic",
        "Mystshroud",
        "Mystweaver",
        
        "Naga Siren",
        "Nazca Enigma",  
        "Necrologist",
        "Nefertiti's Elegance",
        "Nemesis",
        "Nemesis' Vengeance",
        "Netherbound",
        "Night's Last Storyteller",
        "Nightshade",
        "Nightshade",
        "Nightveil",
        "Nine-Tail Illusionist",
        "Ninja",
        "Ninki Nanka's Kin",
        "Noble Sachem",
        "Nomad",
        "Numerologist",
        "Nun",
        
        "Sky's Wrath",
        
        "Echo",
        
        "Occultist",
        "Odin's Whisperer",
        "Oni",
        "Mountainbreak",
        "Forge",
        "Legacy",
        "Depth",
        "Demonmask",
        "Warcaller",
        "Oracle of Delphic Echoes",
        "Oracle",
        "Oracle",
        "Oracle",
        "Orcish Warchief",
        "Orisha's Chosen",
        "Osiris's Rise",
        "Outlaw",
        "Outlaw's Kin",
        "Overseer",
        "of the Divine",
        
        
        "Fragment",
        
        "Paladin",
        "Pioneer",
        "Pathfinder",
        "Patriarch",
        "Pedagogue",
        "Stormcaller",
        "Visionary",
        "Phalanx Leader",
        "Pharaoh",
        "Legacy",
        "Philosopher",
        "Pikeman",
        "Piper",
        "Pirate",
        "Pirate's Ghost",
        "of Port Royal",
        "Pistolero",
        "Plains Wanderer",
        "Planar Researcher",
        "Poem",
        "Poker Face",
        "Poncho's Pride",
        "Pony Express's Wind",
        "Pope",
        "Posse Leader",
        "Potato Sage",  
        "Potion Master",
        "Praetor",
        "Praetor",
        "Prairie's Shadow",
        "Prefect",
        "Prefect",
        "Prelate",
        "President",
        "Pride",
        "Prime Minister",
        "Prime",
        "Prince",
        "Princess",
        "Proconsul",
        "Progeny",
        "Prometheus' Torchbearer",
        "Prophet",
        "Prophetess",
        "Prospector's Dream",
        "Prowlmaster",
        "Psion",
        "Puma's Shadow",
        "Pyramid's Secret",
        
        "Queen",
        "Quetzal Feathered",
        
        "Radiance",
        "Radiantstar",
        "Railroad Pioneer",
        "Rain Dancer",
        "Rain Queen's Blessing",
        "Rajput",
        "Rakshasa Deceiver",
        "Ranger",
        "Rattlesnake's Fang",
        "Raven's Tale",
        "Realmstrider",
        "Regent",
        "Regent",
        "Relic Hunter",
        "Renegade's Run",
        "Representative",
        "Resolve",
        "Resolve",
        "Rhythm",
        "Riddlemaster",
        "River's Gem" 
        "Riverlord",
        "Rivermancer",
        "Lost Settler",
        "Roar",
        "Rodeo Star",
        "Rombo's Horn",
        "Ronin",
        "Ruler",
        "Rune Knight",
        "Runebearer",
        "Runebearer of Midgard",
        "Runechanter",
        "Runekeeper",
        
        "Lament",
        
        "Bane",
        
        "Sacred Keeper",
        "Sacred Speaker",
        "Scar",
        "Spirit",
        "Saga",
        "Sage",
        "Saint",
        
        
        "Sentinel",
        "Samurai",
        "Sandkeeper",
        "Seeker",
        "Slinger",
        "Sasquatch",
        "Piper",
        "Scholar",
        "Secret",
        "Secretary",
        "of the Underworld Gate",
        "Seeker",
        "Seer",
        "Sellsword",
        "Spellsword",
        "Senator",
        "Sentinel",
        "Strength",
        "Sergeant",
        "Scale",
        "Serpentlord",
        "Serpent",
        "Shadow",
        "Shadowcrafter",
        "Shadowmancer",
        "Shadowseer",
        "Shaman",
        "Shaolin",
        "Radiance",
        "Sheriff",
        "Shield",
        "Shieldbearer",
        "Shogun",
        "Siege Master",
        "Mountains Seeker",  
        "Silver",
        "Silverspeaker",
        "Pride",
        "Sirensong",
        "Six-Shooter Sage",
        "of the Eternal Sagas",
        "Skymaiden",
        "Skyrider of the Buraq",
        "Skyrider",
        "Skysovereign",
        "Skywarden",
        "Skyweaver",
        "Song",
        "Songblade",
        "Songstress",
        "Sorcerer",
        "Sorcerer-Bishop",
        "Soulforger",
        "Soulkeeper",
        "Sovereign",
        "Sparkweaver",
        "Speaker",
        "Spell Commander",
        "Spellblade",
        "Spellbreaker",
        "Spellshield",
        "Spellweaver",
        "Spellwoven",
        "Spelunker",
        "Sphinx's Riddle",
        "Spider's Web",  
        "Spiritguide",
        "Spiritualist",
        "Sprite Sparkweaver",
        "Guardian",
        "Stampede's Roar",
        "Star Quilter",
        "Star Whisperer",
        "Starblade",
        "Starborn",
        "Stardancer",
        "Starforge",
        "Starshadow",
        "Starshaper",
        "Steward",
        "Steward",
        "Stonehenge Arcanist",
        "Stonetunnel",
        "Stormbinder",
        "Stormbringer",
        "Storyteller",
        "Strategist",
        "Strength",
        "Sultan",
        "Sultan",
        "Sun Caller",
        "Sun Stone's Keeper",  
        "Sunblessed",
        "Sundiata's Valor",
        "Sunlord",
        "Sunscale",
        "Sunstrider",
        "Supreme Leader",
        "Sworddancer of Covadonga",
        "Swordmaster",
        "Sylph Windcaller",
        "Tabaxi Prowlmaster",
        "Tactics",
        "Talespinner",
        "Technomancer",
        "Telepath",
        "Tempest",
        "Templar",
        "Templar",
        "Tenacity",
        "Thane",
        "Thaumaturge",
        "Theorist",
        "Three-Legged Warhawk",
        "Thunder",
        "Thunderbearer",
        "Thunderbird's Heir",
        "Thunderlord",
        "Tiamat's Scion",
        "Tidecaller",
        "Tideturner",
        "Tiefling Hellstrider",
        "Tikal's Timebender",
        "Timbuktu's Tale",
        "Tin Star's Shine",
        "Tobacco Seer",
        "Tobacco Spirit",
        "Tobacco Spit",
        "Totem's Echo",
        "Totem's Voice",
        "Treasure Fleet's Scourge",
        "Treasure",
        "Treebinder",
        "Tribal",
        "Trick",
        "Trickster",
        "Tribune",
        "Triton Wavecommander",
        "Troll Chieftain",
        "Troll Hunter",
        "Troubadour",
        "Champion",
        "Drifter",
        "Tunnelchief",
        "Turtle Islander",  
        "Treasure",
        "Twilight Herald",
        
        "Elder",
        
        "Voyage",        
        "Valkyrie Skymaiden",
        "Valkyrie",
        "Chosen",
        "Valor",
        "Valorblade of Mulan",
        "Vampire Lord",
        "Vanguard",
        "Veles' Serpent Kin",
        "Venerable One",
        "Vicar",
        "Viking",
        "Vinland Voyager",
        "Viscount",
        "Vision",
        "Vizier",
        "Vodun Viceroy of Hispaniola",
        "Vodyanoy's Rival",
        "Voidseer",
        "Voidtouched",
        "Volva's Visionary",
        "Vizier",
        
        "of the Endless Sands",
        
        "Heart",
        "Wanderer",
        "War Druid",
        "War Witch",
        "Warcaller",
        "Warcaster",
        "Warchief",
        "Warden",
        "Wisdom",
        "Warden",
        "Warder of the Gods",
        "Wardmaster",
        "Warforger",
        "Warhawk",
        "Warlord",
        "Warlord",
        "Warmaster",
        "Warmonger",
        "Wavecommander",
        "Wendigo's Kin",
        "Westward Pilgrim",
        "Whiskey Trader",
        "Whisper",
        "Whisperer",
        "Whitescale Enchanter",
        "Whisper",
        "Wild West Wanderer",
        "Windcaller",
        "Windrider",
        "Winglord of the Tengu",
        "Wisdom",
        "Witchdoctor",
        "Wolfkin",
        "Rebellion",
        "Drum",
        "Serpentlord",
        "Zoologist",
        "Dawnbringer",
        "Zulu",
        "Colonel",
        "Commander",
        "Cruor",
        "Hex",
        "Inferno",
        "Jinx",
        "Krait",
        "Lurk",
        "Malefic",
        "Nefarious",
        "Oblivion",
        "Pestilence",
        "Quake",
        "Rancor",
        "Sable",
        "Torment",
        "Umbra",
        "Vex",
        "Wraith",
        "Xeno",
        "Yielder",
        "Brahmin",
        "Bane",
        "Brigadier",
        "Bishop",
        "Blight",
        "Cadet",
        "Canon","Cardinal",
        "Captain", "Centurion",
        "Chieftain","Cleric",
        "Daimyo","Deacon",
        "Dean","Dread",
        "Eldorado Seeker",
        "Enigma",
        "Ensign",
        "Fang",
        "Friar",
        "Fellow",
        "General",
        "Ghoul",
        "Gilded Voyager",
        "Guardian of the Golden City",
        "Guardian",
        "Sentinel",
        "Vanguard",
        "Seeker",
        "Harbinger",
        "Progenitor",
        "Elder",
        "Pioneer",
        "Forerunner",
        "Exemplar",
        "Paragon",
        
        "Conquistador",
        
        "High Priest",
        
        "Illusionist",
        "Immortal",
        "Infernal",
        "Invoker",
        
        "Lama",
        "Lecturer",
        "Legate",
        "Librarian",
        "Lieutenant",

        "Matriarch",
        "Maestro",
        "Major",
        "Marshal",
        "Matriarch",
        "Mogul",
        "Monk",
        
        "Nun",
        "Ninja",

        "of El Dorado",
        "of Eldorado"
        
        "Patriarch",
        "Pharaoh",
        "Professor",
        "Pasha",
        "Prelate",
        "Priestess",
        "Prodigy",
        "Patriarch",
        
        "Raj",
        "Reader",
        "Renegade",
        
        "Samurai",
        "Scholar",
        "Sergeant",
        "Shaman",
        
        "Tutor",
        "Tribe Leader",
        
        "Vicar",
        "Virtuoso",
        
        "Warlord",
        
        "Yarrow",

        "Zenithar",
        "Zealot"
        "Zinnia"
        "Zombie"
        "Zombie",
        ""
    ]

    title = "The " + random.choice(descriptor) + " " + random.choice(rank)
    return title

def Alignment():
    Alignments = [
        "Lawful Good",          "Neutral Good",        "Chaotic Good",
        "Lawful Neutral",       "True Neutral",        "Chaotic Neutral",
        "Lawful Evil",          "Neutral Evil",        "Chaotic Evil",
        "Unaligned",            ""
        ]
    return random.choice(Alignments)






def Background():
    Backgrounds = [
        "Artist",
        "Bandit",
        "Bard",
        "Barbarian",
        "Berserker",
        "Charlatan",
        "Cleric",
        "Crafter",
        "Criminal",
        "Commoner",
        "Cultist",
        "Druid",
        "Expert",
        "Explorer",
        "Guard",
        "Healer",
        "Hero",
        "Hunter",
        "Knight",
        "Mage",
        "Monk",
        "Merchant",
        "Noble",
        "Priest",
        "Pirate",
        "Ranger",
        "Scholar",
        "Soldier",
        "Rogue",
        "Scholar",
        "Shaman",
        "Soldier",
        "Spy",
        "Traveler",
        "Urchin",
        "Warrior",
        "Warlock",
        "Witch",
        ""
        ]
    return random.choice(Backgrounds)






def Race():
    race_weights = {
        "Human": 10,
        "Aberration": 1,
        "Aven": 1,
        "Beast": 5,
        "Beastfolk": 3,
        "Celestial": 1,
        "Construct": 2,
        "Dragon": 3,
        "Dwarf": 5,
        "Elf": 5,
        "Elemental": 3,
        "Fey": 2,
        "Fiend": 1,
        "Giant": 2,
        "Gnome": 3,
        "Goblin": 5,
        "Halfling": 6,
        "Kobold": 5,
        "Lizardfolk": 2,
        "Monstrosity": 4,
        "Ooze": 1,
        "Orc": 6,
        "Plant": 3,
        "Snakefolk": 2,
        "Undead": 7,
        "": 0
    }
    
    return random.choices(list(race_weights.keys()), weights=race_weights.values(), k=1)[0]











# Racial Names
def Racial_Names(Type):
    Names = [
        "Caspian",
        "Nemo",
        "Ada",
        "Pascal",
        "Byron",
        "Arthurius",
        "Neo",
        "AbErrant",
        "Dorian", 
        "Narkia",
        "Anarkia",
        "Anakin",
        "Draven",
        "Furiosa",
        "Goku",
        "Jareth",
        "Maleficent", 
        "Kratos",
        "Xena",
        "Zorro",
        "Forajido",
        "Paragon",
        "Amelia", 
        "Morpheus",
        "Trinity",
        "Ripley",
        "Leia",
        "Luke",
        "Maximus",
        "Arya",
        "Odin", 
        "Ragnar",
        "Loki",
        "Athena",
        "Dante",
        "Orion",
        "Alucard",
        "Thorin",
        "Legolas", 
        "Strider",
        "Spartacus",
        "Elektra",
        "Storm",
        "Logan",
        "Wolverine",
        "Rogue", 
        "Phoenix",
        "Mystique",
        "Cersei",
        "Daenerys",
        "Khal",
        "Brienne",
        "Oberyn", 
        "Raven",
        "Sabrina",
        "Seraph",
        "Azrael",
        "Lucifer",
        "Castiel",
        "Crowley", 
        "Maverick",
        "Icarus",
        "Circe",
        "Nyx",
        "Osiris",
        "Horus",
        "Perseus",
        "Cronos", 
        "Medusa",
        "Tyrion",
        "Lysandra",
        "Aelin",
        "Rowan",
        "Daemon",
        "Altair",
        "Ezio", 
        "Desmond",
        "Leonardo",
        "Ramses",
        "Cleopatra",
        "Ares",
        "Hera",
        "Zeus", 
        "Midas",
        "Echo",
        "Narcissus",
        "Sylar",
        "Kai",
        "Rhea",
        "Mara",
        "Kali", 
        "Draco",
        "Bellatrix",
        "Vega",
        "Nyx",
        "Thalia",
        "Titan",
        "Nova",
        "Solaris"
        ]
    
    Surnames = [
        "Warbrute",
        "Bladebreaker",
        "Ironclad",
        "Tusker",
        "Bonecrusher",
        "Stormhowler",
        "Mudwalker",
        "Beastmaster",
        "Bloodfist",
        "Thunderlord",
        "Stormbringer",
        "Ravenclaw",
        "Moonshadow",
        "Ironfist",
        "Fireheart",
        "Silvervein",
        "Dawnbreaker",
        "Nightshade",
        "Starfall",
        "Windrunner",
        "Darkwood",
        "Lightbringer",
        "Earthshaker",
        "Skybreaker",
        "Seastalker",
        "Mountaincaller",
        "Thunderspear",
        "Sunshield",
        "Flameforge",
        "Whitewind",
        "Blackspear",
        "Goldenaxe",
        "Steelstrike",
        "Silentblade",
        "Dragonbane",
        "Wolfsbane",
        "Lionsmane",
        "Eagleseye",
        "Stoneheart",
        "Shadowdancer",
        "Battlemaster",
        "Swiftfoot",
        "Thunderclaw",
        "Snowfury",
        "Oceansong",
        "Riverblade",
        "Frostweaver",
        "Sandshifter",
        "Firewhisper",
        "Windweaver",
        "Dreamchaser",
        "Starweaver",
        "Stormrider",
        "Duskwatcher",
        "Whitewolf",
        "Redraven",
        "Frostfire",
        "Nightwhisper",
        "Trueblade",
        "Bluesky",
        "Goldeneye",
        "Ironshard",
        "Sunfire",
        "Shadowhawk",
        "Blackthorn",
        "Highwind",
        "Stormwatcher",
        "Twilightbearer",
        "Darkstone",
        "Lightstep",
        "Moondancer",
        "Stardust",
        "Thunderforge",
        "Stormforge",
        "Whitewave",
        "Greycloud",
        "Silverleaf",
        "Flameseeker"
    ]


    Humans = [
        "Arthur",
        "Ambrose",
        "Albus",
        "Albertus",
        "Aragorn",
        "Anselm",
        "Augustine",
        "Anastasia",
        "Beowulf","Belos",
        "Cid", "Cicero","Caesar",
        "Cleopatra",
        "Denis",
        "Emelot", "Jean", "Frank",  "Isildur",
        "Theoden", "Lancelot", 
        "Thomas", "Nicole", "Herbin",
        "Elisabeth", "Katarina", "Beau",
        "Reginald", "Ernest", "Aubert", 
        "Neil",  "Menard", "Euphemia",
        "Lucy", "Oda", "Lazarus", "Blanche",
        "Regina", 
        "Jasper",
        "Anastasia", "Mathilda", "Brian",
        "George", "Colbert", "Hubert", "James", 
        "William", "Nathaniel",
        "Edric", "Edward", "Christopher", "Martin", "Emma",
        "Avis", 
        "Wilmot",
        "Audrey",
        "Cecilia",
        "Joy",
        "Joan",
        "Tobias",
        "Mark",
        "Solomon",
        "Eve",
        "Alice", 
        "Berthold",
        "Hypatia",
        "Pythagoras",
        "Hercules",
        "Pascal",
        "Marie",
        "Curie",
        "Bruce", 
        "Merlin",
        "Galahad",
        "Tristan",
        "Isolde",
        "Robin",
        "Marian",
        "Sigurd",
        "Brunhild", 
        "Ragnar",
        "Roland",
        "Roderick",
        "Elaine",
        "Morgana",
        "Uther",
        "Iseult",
        "Geraint", 
        "Percival",
        "Gawain",
        "Bedivere",
        "Cedric",
        "Leif",
        "Erik",
        "Harald",
        "Olaf",
        "Charlemagne", 
        "Frederick",
        "Louis",
        "Eleanor",
        "Isabella",
        "Ferdinand",
        "Alfred", 
        "Edward",
        "Matilda",
        "Henry",
        "Richard",
        "Philip",
        "Joan",
        "Eloise",
        "Abelard", 
        "Daedalus",
        "Theseus",
        "Odysseus",
        "Penelope",
        "Helen",
        "Paris",
        "Hector",
        "Orpheus", 
        "Eurydice",
        "Siegfried",
        "Gudrun",
        "Vercingetorix",
        "Julius",
        "Marcus",
        "Lucius",
        "Octavia",
        "Titus",
        "Claudius", 
        "Nero",
        "Spartacus",
        "Ovid",
        "Virgil",
        "Horace",
        "Gregory", 
        "Jerome",
        "Rollo",
        "Ivan",
        "Peter",
        "Catherine",
        "Nicholas", 
        "Rasputin",
        "Vladimir",
        "Maria",
        "Olga",

        
        "Augustus", 
        "Alexei",
        "Attila",

        "Boudicca",

        "Isabella",

        "Jeremias",
        
        "Luz",
        "Louis",

        "Percy",
        "Percival",
        
        "Tatiana",
  
        "Vigo",
        
        ""]
    
    Human_Surnames = [
        "Aragon", 

        "Borgia",

        "Capulet",
        "Camelot",
        "Castilla",
        "Capetian",
        
        "DuLac",
        "DeLion",
        "d'Anjou",
        "d'Arc",
        "d'Aquitaine",
        
        "Gondor",

        "Hohenstaufen",

        "Montague",
        "Medici",

        "Normandy",

        "Plantagenet",
        "Pendragon",
        
        "Rohan",
        "Romanov",

        "Stuart",

        "Tudor",
        
        "Valois",
        "Visigoth",
        "Valdemar",
        
        "Wessex",

        "Bourbon",
        "York",
        "Lancaster",
        "Windsor",
        "Sforza",
        "Navarre",
        "Hapsburg",
        "Plantin",
        "Rurikid",
        "Palaiologos",
        "Comnenus",
        "Dragomir", 
        "Valerius",
        "Aurelius",
        "Tiberius",
        "Antonius",
        "Flavius",
        "Merovingian",
        "Carolingian", 
        "Athens",
        "Sparta",
        "Macedon",
        "Scipio",
        "Brutus",
        "Gallico",
        "Varangian",
        "Kiev",
        "Byzantine",
        "Ostrogoth",
        "Visconti",
        "Guelph", 
        "Hohenzollern",
        "Teutonic",
        "Gaul",
        "Pict",
        "Ravenclaw",
        "Eagleshield", 
        "Wolfheart",
        "DeLeon",
        "Dragonbane",
        "Fitzroy",
        "Hawklight",
        "Northwind",
        "Sterlingshire", 
        "Brightstar",
        "Courtenay",
        "Isles",
        "Sunshield",
        "Dawnbringer",
        "Elmsworth", 
        "Lockewood",
        "Riversend",
        "Troy",
        "Thracian",
        "Thebes",
        "Alighieri",
        "Pazzi", 
        "Novgorod",
        "Moorheart",
        "Grimaldi",
        "Toledo",
        "Dumnonia",
        "Rhodes",
        "Salamis", 
        "Beauharnais",
        "Marathon",
        "Delphini",
        "Bardic",
        "Gothicus",
        "Eboracum",
        "Caledonia", 
        "Gothland",
        "Magnusson",
        "Vandale",
        "Thule",
        "Corinth",
        "Argos",
        "Lusitan", 
        "Valkyrja",
        "Saxony",
        "Bavaria",
        "Corinthia",
        "Moldavia",
        "Merovian",
        "Uralic",
        "Commoner",
        "Nomad",
        "Wanderer",
        "Peasant",
        "Squire",
        "Mortal",
        "Kinsman",
        "Vagrant",
        "Pilgrim",
        "Settler",
        "Amblecrown",
        "Buckman",
        "Evenwood",
        "Greycastle",
        "Tallstag",
        "Bersk",
        "Chernin",
        "Dotsk",
        "Kulenov",
        "Marsk",
        "Nemetsk",
        "Shemov",
        "Starag",
        "Brightwood",
        "Helder",
        "Hornraven",
        "Lackman",
        "Stormwind",
        "Windriver",
        "Ankhalab",
        "Anskuld",
        "Fezim",
        "Hahpet",
        "Nathandem",
        "Sepret",
        "Uuthrakt",
        "Chergoba",
        "Dyernina",
        "Iltazyara",
        "Murnyethara",
        "Stayanoga",
        "Ulmokina",
        "Chien",
        "Huang",
        "Kao",
        "Kung",
        "Lao",
        "Ling",
        "Mei",
        "Pin",
        "Shin",
        "Sum",
        "Tan",
        "Agosto",
        "Astorio",
        "Calabra",
        "Domine",
        "Falone",
        "Marivaldi",
        "Pisacar",
        "Ramondo",
        "Picasso",
        "Blackbeast",
        "Blackbeard",
        "Blackbear",
        "Violetdawn",
        "Rosedawn",
        "Wanderlust",
        "Dostoyevsky",
        "Dundragon",
        "Pendragon",
        "Clawthorne"
        ]
    if Type == "Human":
        Names = Humans
        Surnames = Human_Surnames
        FullNames =  random.choice(Names) + ' ' + random.choice(Surnames) 
        return FullNames

    Elves =[
        "Aegnor",
        "Ael",
        "Aelar",
        "Aeol",
        "Aerandir",
        "Aeris",
        "Aero",
        "Adalara",
        "Adalin",
        "Adran",
        "Adrie",
        "Ag",
        "Alador",
        "Alagos",
        "Alathaea",
        "Aldovale",
        "Alima",
        "Alorio",
        "Althaea",
        "Althos",
        "Amastacia",
        "Amelia",
        "Amity",
        "Anali",
        "Anakin", 
        "Andraste",
        "Ang",
        "Angorn",
        "Angrod",
        "Annon",
        "Anastriana",
        "Antinua",
        "Anthon",
        "Ara",
        "Aramil",
        "Aranel",
        "Aranis",
        "Araphor",
        "Arathorn",
        "Aratlion",
        "Arondir",
        "Arthern",
        "Arannis",
        "Arn",
        "Aro",
        "Arphor",
        "Arros",
        "Arthalion",
        "Arthriol",
        "Asur", 
        "Astrid",
        "Athos",
        "Atro",
        "Aubren",
        "Aust",
        "Austio",
        "Autumnfall",
        "Ava",
        "Avafi",
        "Azaki",
        "Austio",
        "Austarion",
        "Autumn",
        "Aelthion",
        "Adalara",
        "Adal",
        "Ada",
        "Adran",
        "Adrie", 
        "Aera",
        "Aevis",
        "Aldovale",
        "Alagos",
        "Alador",
        "Alimo",
        "Alima",
        "Alyssum",
        "Amastacia",
        "Amberpath", 
        "Amelia",
        "Amity",
        "Anali",
        "Andraste",
        "Ang",
        "Angorn",
        "Anastriana",
        "Anarkia",
        "Anakin",
        "Antinua", 
        "Ara",
        "Aralph",
        "Aramil",
        "Arandin",
        "Araran",
        "Aranis",
        "Arathor",
        "Ari",
        "Arizima",
        "Arondir", 
        "Arn",
        "Aro",
        "Arthurius",
        "Arthur",
        "Arzein",
        "Arne",
        "Aro",
        "Aslyssum",
        "Astrid",
        "Atala", 
        "Aubert",
        "Aust",
        "Austio",
        "Autumn",
        "Autumnheart",
        "Awaldiel",
        "Avis",
        "Azaki",
        
        "Baldric",
        "Banderliss",
        "Bark",
        "Barathor",
        "Basha",
        "Bella",
        "Belladonna",
        "Beren",
        "Bertin",
        "Birel",
        "Birel",
        "Bleonal",
        "Blim",
        "Blorin",
        "Bodil",
        "Bor",
        "Borivik",
        "Boromir",
        "Bral",
        "Brannon",
        "Brath",
        "Brithiel",
        "Brodin",
        "Broe",
        "Brom",
        "Bryn",
        "Brueral",
        "Byrius",

        "Cael",
        "Caelin",
        "Caelum",
        "Caladwen",
        "Caran",
        "Carric",
        "Caspian",
        "Celtana",
        "Certhel",
        "Celeborn",
        "Celebrian",
        "Celebriel",
        "Celebrimbor",
        "Certhel",
        "Chel",
        "Chelri",
        "Cirdan",
        "Clagna",
        "Claira",
        "Cothiel",
        "Curufin",
        "Curulire",
        "Cuthalion",
        
        "Daeron",
        "Dalanzal",
        "Danel",
        "Dartagnan",
        "Dawnpath",
        "Del",
        "Delian",
        "Deloth", 
        "Denethor",
        "Denir",
        "Dilon",
        "Dinendal",
        "Dineloth",
        "Donael",
        "Donathan",
        "Dor",
        "Dorin",
        "Dorn",
        "Douglas",
        "Draven",
        "Driel",
        "Drusilia",
        "Durin",
        "Durgwen",
        
        "Earendil",
        "Eariol",
        "Earwen",
        "Eda",
        "Edalin",
        "Edan",
        "Edrial",
        "Edriol",
        "Eero",
        "Egorn", 
        "Eilinora",
        "Eilri",
        "Eiro",
        "Elandrial",
        "Elanor",
        "Ela",
        "Elenia",
        "Eleonor",
        "Elendil",
        "Elendithas",
        "Elennanor",
        "Elenwe", 
        "Elestirne",
        "Elessar",
        "Elhalyn",
        "Elion",
        "Elmo",
        "Elphir",
        "Elriol",
        "Elrond",
        "Elros",
        "Elrohir",
        "Elu",
        "Elwen",
        "Elwing",
        "Elion",
        "Eli",
        "Elian",
        "Elior",
        "Elinor",
        "Elwe",
        "Elyan",
        "Elerian",
        "Elthorin",
        "Elerossë",
        "Elphir",
        "Elvandar",
        "Eol", 
        "Eolande",
        "Eoliel",
        "Eoloriel",
        "Eorl",
        "Ephelion",
        "Erevan",
        "Eriol",
        "Erin",
        "Ermo",
        "Ero",
        "Erol",
        "Eru",
        "Erwen",
        "Eryn",
        "Ethalion",
        "Ethir",
        
        "Faelir",
        "Fae",
        "Faen",
        "Fael",
        "Faelon",
        "Faenor",
        "Fara",
        "Farin",
        "Faral",
        "Felosial",
        "Fen",
        "Fera",
        "Ferumbras",
        "Feantur",
        "Feanor",
        
        "Bai",
        "Baldric", 
        "Banderliss",
        "Barathor",
        "Bark",
        "Basha",
        "Beaux",
        "Beiro",
        "Belos",
        "Bella",
        "Belladona",
        "Berevan", 
        "Berrian",
        "Betha",
        "Bertin",
        "Birel",
        "Birel",
        "Blath",
        "Blein",
        "Blanchet",
        "Bleonal",
        "Blim", 
        "Bodil",
        "Bor",
        "Borivik",
        "Bram",
        "Bran",
        "Bri",
        "Brion",
        "Brim",
        "Broe",
        "Brueral", 
        "Bryn",
        "Bryn",
        "Byron",
        "Byrius",
        "Cael",
        "Caelin",
        "Cael",
        "Caelin",
        "Caladwen",
        "Carric", 
        "Caspian",
        "Catarina",
        "Cecilia",
        "Celeborn",
        "Celebrimbor",
        "Celebros",
        "Celtana", "Certhel", "Cezar", "Chaelana", 
        "Chathi", "Chen", "Chi", "Christopher", "Clagnemart",
        "Claira", "Clark", "Colart", "Conan", "Constance", 
        "Cuarion", "Curie", "Curu", "Daneloth", "Dartagnan", "Dartañan",
        "Dartagnan", "Dartañan", "David", "Dawnpath", 
        "Dawnwalker", "Del", "Dilan", "Dineloth",
        "Donael", "Douglas", "Dont", "Dorn", "Dorian", "Doliel", 
        "Dorn", "Dramo", "Draven", "Drusilia", "Dumein",
        "Durgwen", "Earendil", "Eberk", "Eda", "Edric", 
        "Ela", "Elandrial", "Elama", "Elari", "Elbereth",
        "Elenia", "Elendil", "Elendil", "Elenia", "Ele", 
        "Elendil", "Elerinna", "Elevas", "Eli", "Elia",
        "Eli", "Elidyr", "Elien", "Elin", "Elle", 
        "Elladan", "Elma", "Elphaba", "Elpetor",
        "Elrieth", "Elrohir", "Elros", "Eluin",
        "Elwing", "Elzevir", 
        "Elye", "Elyl", "Elys", "Ema", "Emma",
        "Emmy", "Ender", "Endor", "Enialis", "Enna", 
        "Eol", "Erafe", "Eran", "Erdan",
        "Erestor", "Erevan", "Erwin", "Espar", "Esmeralda", "Esvele", 
        "Eufemia", "Euler", "Eurin", "Evadne", "Evandel", "Evanescense", "Eve",
        "Evidam", "Eyla", "Faelir", 
        "Faen", "Faera", "Fae", "Faethis",
        "Faila", "Fai", "Falchion",
        "Fandel", "Fan", "Fanal", 
        "Faelir", "Faen", "Faera", "Faethis", "Fai", "Faila", "Falchion", "Fandel", "Fan", "Fanal",
        "Fandel", "Fandral", "Fara", "Faral", "Faelorn", "Faralin",
        "Farol", "Feanor", "Felicity", "Felosial",
        "Fen", "Fera", "Feralia", "Featherspark", "Felan", "Feravel",
        "Feremar", "Feyla", "Feylin", "Filius",
        "Fingolfin", "Firael", "Foli",
        "Forestmoon", "Forestflower", "Forestheart", "Forojol", "Fral", "Frelia", "Freya",
        "Froemar", "Galadriel", "Galdor", "Galindan", "Gara", "Gawain",
        "Gael", "Gara", "Gerngwen", "Glorfindel",
        "Goldleaf", "Gus", "Goku", "Galdric", "Galin", "Galor", "Galthor", "Glyn", "Haedir", "Hadarai",
        "Halana", "Heian", "Holara", "Horatio", "Horneth", "Huroz",
        "Iannien", "Iellan", "Ienor", "Ilanis",
        "Ilebellis", "Ilima", "Immeral", "Innil",
        "Irion", "Ira", "Irui", "Iorhel", "Isolde", "Ivellios",
        "Iusus", "Iylar", "Jareth", "Jar",
        "Jarsali", "Jay", "Jelenet", "Jorel", "Kai", "Kalel",
        "Kan", "Kari", "Karnwyl", "Karn", "Kay", "Keiro", "Keyleth",
        "Kern", "Kratos", "Kylar",
        "Laucian", "Lael", "Laer", "Larin", "Lauriel", "Laurin",
        "Leshanna", "Lia", "Liliandil", "Liadon",
        "Lilis", "Lirn", "Lithor", "Lora", "Loria", "Loria", "Loriel", "Lorin", "Lue", "Lura",
        "Luthien", "Lyfaen", "Lyrial", "Mai", "Maindaer", "Malkis",
        "Mara", "Maleficent", "Maralen", "Maur",
        "Melehtion", "Melwen", "Mella", "Meriele", "Merric", "Mialee",
        "Mial", "Mindartis", "Mial", "Mistwatcher",
        "Morhel", "Morwen", "Mya", "Mykar", "Myla", "Myr", "Nae",
        "Naeris", "Naivara", "Nail",
        "Naila", "Nailo", "Narkia", "Narn", "Neo", "Neuse", "Newa", "Noarnad", "Nora", "Norul",
        "Oceania", "Oceanwalker", "Odalia",
        "Ofandrus", "Oi", "Olimion", "Ol", "Oren", "Ostoroth", "Oromis",
        "Paelia", "Pascal", "Pegnith", "Peren", "Peri", "Peria",
        "Pharana", "Quildohtare", "Quelenna", "Quinar",
        "Rain", "Raine", "Raingaze", "Rael", "Raelim", "Raer",
        "Raen", "Ravenflow", "Ravenwatcher", "Ridaro",
        "Relix", "Ren", "Reseo", "Riardon",
        "Rithel", "Rocenel", "Roden", "Roen", "Rolan", "Rolen",
        "Rua", "Rumathran", "Ryann", "Ryer", "Rym", "Sael", "Sai",
        "Sann", "Sariel", "Saynal",
        "Shava", "Soderac", "Sovelis", "Starwatcher", "Starwhisper",
        "Sudelrin", "Sumi", "Sumnes", "Syllin", "Sylvaranz",
        "Sylv", "Tauriel", "Thia",
        "Thranduil", "Tindecet", "Tris",
        "Trian", "Valance", "Vadan", "Valna",
        "Vanimial", "Vall",
        "Van",
        "Vanes", "Vax", "Vaxeldan",
        "Vex", "Vexhalia", "Viasta", "Wasanzi",
        "Wil", "Wenion", "Xanapia", "Xyrkraken", "Xylia", "Yael",
        "Yaeldrin", "Yesstina",
        "Zamior", "Zarivol",
        "Zay", "Zelaerys",
        "Zelir",
        "Zeren",
        "Zia",
        "Zorro"
        ]

    ElvenSurnames = [
        "Moonshadow",
        "Nightbreeze",
        "Sunweaver",
        "Moonglow", 
        "Leafdancer",
        "Stardancer",
        "Silverleaf",
        "Nightsong",
        "Riverwind",
        "Goldenwood", 
        "Dawntreader",
        "Starshine",
        "Lighthaven",
        "Silverbrook",
        "Windrunner",
        "Moonbeam", 
        "Skydancer",
        "Glimmerwing",
        "Sunglow",
        "Thornheart",
        "Lightbearer", "Twilightveil", 
        "Morningstar", "Dreamweaver",
        "Whisperwind",
        "Duskweaver", "Raindancer",
        "Sunshadow", 
        "Starfall", "Mistwood",
        "Dreamshade",
        "Frostvale", "Leafshade",
        "Goldenbough",
        "Silverpine",
        "Mistwalker", "Dawnshadow",
        "Dreamsong",
        "Nightshade", "Starleaf",
        "Moonrise", "Sunblade", 
        "Mistbreeze", "Eveningstar",
        "Sundancer",
        "Whisperleaf", "Dreamcatcher",
        "Leafwhisper", 
        "Starweaver", "Sunshard", "Silentbrook",
        "Glimmermoon", "Nightriver", "Silverwind", 
        "Lightshade", "Moondancer", "Frostleaf",
        "Starbloom", "Rainwhisper", "Glimmerstone", 
        "Silverfrost", "Goldensong", "Sunspark",
        "Nightglow",
        "Starflight", "Rainshadow", 
        "Goldenleaf", "Whisperbreeze", "Moonlace",
        "Dewshine",
        "Twilightbloom", "Moonstone", 
        "Sunsinger", "Shadowsong", "Ebonwood",
        "Goldenrain", "Skywhisper", "Starfire", 
        "Sunstone", "Moonbrook", "Nightsinger",
        "Goldenstar", "Shimmerwood", "Sapphireglow", 
        "Emeraldshade",
        "Crystalbrook", "Silverstream",
        "Starbright",
        "Moonsinger", "Twilightleaf",
        "Sunburst",
        "Dreamlight", "Whispershade",
        "Glimmerleaf",
        "Silentmoon", "Shadowvale", 
        "Dawnlight",
        "Glimmershade", "Goldendew",
        "Nightstar",
        "Twilightmist",
        "Eldar",
        "Moonchild",
        "Sunweaver",
        "Starcaller",
        "Leafdancer",
        "Nightrunner",
        "Twilightseeker",
        "Woodlander",
        "Astralborn",
        "Silverkin",
        "Starwhisper",
        "Silversong"
        ]

    if Type == "Elf":
        Names = Elves
        Surnames = ElvenSurnames
        FullNames =  random.choice(Names) + ' ' + random.choice(Surnames) 

        return FullNames

    Giant = [
        "Rotder", "Flunfum", "Bunce", "Calamundis",
        "Droroc", "Gerdur", "Grad", "Bridget", "Ananias",
        "Atlas", "Bunari", "Casade", "Atlumun", "Coeus",
        "Crius", "Hyperion", "Iapetus", "Cronus", "Thea",
        "Rhea", "Themis", "Memosyne", "Foebe", "Tethis", "Tezis",
        "Tethys", "Bunasas", "Calan", "Brasan", "Tialam", "Bundero", "Atlar", "Caramu", "Cadet", "Flasari", "Geroro", "Bundun", "Andurd", "Draro", "Tisar", "Coni", "Bunfunfu", "Atlaria", "Bundunde", "Candu", "Teri", "Casaris", "Candun", "Andun", "Caris", "Bunasa", "Tialas", "Brisar", "Bumo", "Bunde", "Ragnarok", "Arzur", "Arturus", "Bedivere", "Bedwyr", "Bohort", "Bors", "Cai", "Caradoc", "Caradog", "Culch", "Elaine", "Enid", "Enide", "Gaheriet", "Gaheris", "Galaad", "Galahad", "Gareth", "Garez", "Gauvain", "Goven", "Gawain", "Geraint", "Gualguainus", "Guendolen", "Guendolena", "Guenevere", "Guinivere", "Guiomar", "GynezGyneth", "Hector", "Hoel", "Igerna", "Igraine", "Iseult", "Iseut", "Isolda", "Isolde", "Kay", "Lancelot", "Loncelote", "Lancelote", "Laudine", "Linet", "Lionel", "Lionesse", "Lionors", "Lohengrin", "Loherangrin", "Lot", "Luned", "Lunete", "Lynet", "Lynette", "Lyones", "Lyonesse", "Lyonors", "Medraut", "Medrod", "Mordred", "MerlinMyrdin", "Merlinus", "Merdinus", "Modred", "Mordred", "Morgaine", "Morgen", "Nimue", "Vivien", "Niniane", "Olwen", "Owain", "Parsifal", "Parzival", "Percival", "Pellam", "Pelleas", "Pellehand", "Pellehan", "Pelles", "Beli", "Pellinore", "Percival", "Peredur", "Tristan", "Drust", "Drustan", "Urien", "Uther", "Uthyr", "Walganus", "Yseut", "Iseult", "Ysolt", "Iseult", "Yvain", "Owain", "Ywain", "Lynn", "Lunete", "Eluned", "Lohengrin", "Lorraine", "Lot", "Gaius", "Iseult", "Gawain", "Garez", "Enid", "Helen", "Caratacos", "Caradog", "Bors", "Bedivere", "Tigsar", "Morgan", "Arthur", "Oceanus"
        ]
    if Type == "Giant":
        Names = Giant
        Surnames = Giant
        FullNames =  random.choice(Names) + ' ' + random.choice(Surnames)  + "son"
        return FullNames

    Orcs =[
        "Aldis",
        "Arn",
        "Asfrid",
        "Asterix",
        "Axe",
        "Balli",
        "Bjorn",
        "Blod",
        "Bulak",
        "Carguk",
        "Erek",
        "Erik",
        "Engli",
        "Farkang",
        "Gell",
        "Gnarsh",
        "Gorga",
        "Grog",
        "Grigi",
        "Gro",
        "Greiland",
        "Henk",
        "Holg",
        "Hosvir",
        "Idefix",
        "Ingrid",
        "Iuli",
        "Jor",
        "Lagazi", 
        "Merida",
        "Obelix",
        "Olof",
        "Ovif",
        "Ozerix",
        "Panoramix",
        "Ragnar",
        "Sagu",
        "Sarod", 
        "Skegg",
        "Skard",
        "Skuf",
        "Sveik",
        "Svein",
        "Svafar",
        "Steinolf",
        "Steg",
        "Thorkell", 
        "Thorald",
        "Thorlak",
        "Trag",
        "Trarik",
        "Tyrfing",
        "Torrad",
        "Vifil",
        "York",
        "Yurk",
        "Ñor",
        "Agmund",
        "Alrek",
        "Bjarte",
        "Brondar",
        "Dagfinn",
        "Einar",
        "Eyvind",
        "Frode",
        "Geirmund",
        "Gunnar",
        "Halvard",
        "Harald",
        "Inge",
        "Ivar",
        "Jarl",
        "Ketil",
        "Knute",
        "Leif",
        "Magnar",
        "Oddr",
        "Ormr",
        "Ragnarr",
        "Rolf",
        "Sigurd",
        "Skarde",
        "Snorri",
        "Sorli",
        "Steinar", 
        "Thrainn",
        "Ulf",
        "Valgard",
        "Vidar",
        "Yngvar",
        "Orm",
        "Hakon",
        "Bragi",
        "Toste",
        "Trygg"
        
        ]
    OrcSurnames = [
        "Vikingsson", 
        "Odinson", "Ulfsson", "Atlisson",
        "Fastfulfsson", "Osvifsson", "Warysson",
        "Skardisson", "Tofisson", "Borksson",
        "Orksson", "Fangsson", "Ardisson", "Arksson",
        "Wasson", "Hosvirsson", "Skegsson",
        "Thoralsson",
        "Olofsson", "Aldisson",
        "Herdisson",
        "Ingrisson", "Skusson", "Svasson",
        "Ensson", "Vifsson",
        "Iulisson", "Sveinsson",
        "Throlaksson", "Jorsson",
        "Ballisson",
        "Yorksson",
        "Yurksson",
        "Ereksson", "Eriksson",
        "Arnsson",
        "Battlebreaker", "Warfist",
        "Strongaxe", "Ironclaw",
        "Stoneheart", "Firebrand", 
        "Stormcaller", "Thunderfury",
        "Battlescream", "Warchief",
        "Bloodaxe", "Skullsmasher", 
        "Ironjaw", "Shadowfury",
        "Bladesinger", "Marrowrend",
        "Ragehorn", "Boneshatter", 
        "Stonebreaker", "Thunderclap",
        "Warblade", "Goreaxe",
        "Frostmaul", "Darkfury", 
        "Stormblade", "Earthshaker",
        "Firefist",
        "Blooddrinker", "Ragefury",
        "Warsong", 
        "Battlerager",
        "Goreclaw", "Steelbite",
        "Bladestorm", "Skullsplitter",
        "Maulfist", 
        "Bloodscream", "Stormfist",
        "Firemaul", "Shadowclaw",
        "Thundermaul",
        "Warfang", 
        "Ironmaul",
        "Bonecrusher",
        "Rageblade",
        "Battleshout",
        "Goremaul",
        "Thunderaxe", 
        "Stormrend",
        "Bladeshadow", "Gorebrand",
        "Warthorn",
        "Frostfury", "Shadowmaul", 
        "Battlemaw", "Warclaw",
        "Rageclaw",
        "Bladefury", "Gorethorn",
        "Warbreaker", 
        "Frostclaw", "Thunderfist",
        "Skullcrusher",
        "Shadowbreaker", "Ironfury",
        "Bloodfury", 
        "Ragesong",
        "Battleclaw", "Warmaul",
        "Bladebreaker",
        "Stormfury", "Firethorn", 
        "Shadowrend", "Thunderblade",
        "Gorebreaker",
        "Ironblade", "Bloodmaul",
        "Battlerage"
        ]
    if Type == "Orc":
        Names = Orcs
        Surnames = OrcSurnames
        FullNames =  random.choice(Names) + ' ' + random.choice(Surnames) 
        return FullNames
    Dwarves = [
        "Graviel", "Juan",
        "Fernan", "Enrique",
        "Mariana",
        "Aularia", "Inés",
        "Blanca",
        "Ignacio",
        "Gonzalo", "Rafael",
        "Igon",
        "Marian", "Aurelio",
        "Alfredo",
        "Ramon", "Ramona",
        "Eulario", "Paca", "Francisca",
        "Paco", "Francisco", "Antonio",
        "Leonor", "Juanes",
        "Juliana", "Ramono", "Angela",
        "Arturo", "Leandro", "Cornelio",
        "Feliz", "Jose", "Josejuan",
        "Joseramon", "Josealberto",
        "Josenrique", "Joseantonio",
        "Lucia", "Diego", "Armando",
        "Samuel", "Enrique", "Antonio",
        "Miguel", "Bernardo", "Alberto",
        "Adelaida", "Adelita",
        "Adora", "Adrian", "Agustin",
        "Agustina",
        "Ainara",
        "Ainoa",
        "Aitana", "Aitor",
        "Alba", "Alejandra", "Alejandro",
        "Alejo", "Alex", "Alfonso", "Alfredo",
        "Almudena", "Alonso",
        "Alvaro", "Amadeo",
        "Amancio", "Amaya", "Ambrosio", "Amparo",
        "Belen", "Anacleto", "Isabel", "Maria",
        "Sofia", "Angustias", "Anibal", "Anselmo",
        "Antonio", "Apolonio",
        "Araceli", "Armando",
        "Aroa", "Arsenio", "Arturo", "Ascensión",
        "Asunción", "Atanasio",
        "Atilio", "Aureliano",
        "Aurelio", "Avelina",
        "Azucena", "Baldomero",
        "Bárbara", "Bartolomé",
        "Basilio", "Beatriz",
        "Begoña", "Benita",
        "Bermudo", "Bernarda",
        "Borja", "Brigida",
        "Calisto", "Camila",
        "Candelaria", "Candida",
        "Carlos", "Carlota",
        "Carmela", "Carmelo",
        "Casilda", "Casimiro",
        "Catalina", "Cecili",
        "Celeste", "Celestino",
        "Celino", "Chema",
        "Clara", "Clarisa",
        "Claudia", "Claudio",
        "Clemente", "Cleto",
        "Constantino", "Consuela",
        "Corina", "Cornelio",
        "Cosmo", "Cristian",
        "Cristina", "Cristobal",
        "Curro", "Custodia",
        "Custodio", "Dagoberto",
        "Damian", "Daniel",
        "Daniela", "Danilo",
        "Dariel", "Darío",
        "Debora", "Demetrio",
        "Desideria", "Desiderio",
        "Diego", "Domingo",
        "Domitilda", "Eberardo",
        "Edelmira", "Edmundo",
        "Eduardo", "Eladio",
        "Eleuterio", "Eligio", "Elisa",
        "Eliseo", "Elodia", "Emigdia",
        "Emiliano", "Emilio",
        "Encarnación", "Enriqueta",
        "Erasmo",
        "Esmeralda",
        "Esperanza",
        "Opalo", "Esteban",
        "Estefanía", "Eulogia",
        "Eulogio", "Eustaquio",
        "Eva", "Evangelina",
        "Evaristo", "Ezequiel",
        "Fabián", "Fabiola",
        "Facundo", "Fátima",
        "Faustina", "Federico",
        "Felipe", "Fernanda",
        "Fernando", "Filomena",
        "Fina", "Flavia",
        "Flavio", "Flora", "Floro",
        "Fulgencio",
        "Fabio",
        "Gabriel",
        "Geraldo", "Gilberta",
        "Godofredo", "Gonzalo", "Gregoria",
        "Gregorio", "Grimaldo",
        "Guadalupe", "Guillermo",
        "Haroldo", "Hector", "Herminia",
        "Hernando", "Hortensia",
        "Humberto", "Iban",
        "Ignacia", "Ignacio", "Inés", "Iñigo",
        "Inmaculada", "Inocencio",
        "Isidora", "Isidoro",
        "Jacinta", "Jacinto", "Jeremías",
        "Jerónimo", "Jesusa", "Jimeno", "Jimena",
        "Jorge", "Jose", "Joseangel", "Joseantonio",
        "Josefa", "Joseluis",
        "Josemanuel", "Josemari",
        "Josemaria", "Juan",
        "Juana", "Juancho",
        "Juancarlos", "Juanfran",
        "Juanita", "Juanjosé",
        "Juanma", "Juanpablo",
        "Justina",
        "Justino", "Justo",
        "Kiko", "Laura", "Lázaro",
        "Leandro", "Lope", "Lucas",
        "Lucrecio",
        "Lucrecia", "Luisa",
        "Manolo", "Manola",
        "Manuel", "Marcelo",
        "Marcela", "Marcos",
        "Margarita", "Maribel",
        "Mario", "Marta",
        "Martín", "Mateo",
        "Mauro", "Melania",
        "Mercedes",
        "Ignacio",
        "Natalio",
        "Nicodemo",
        "Nieves",
        "Norberto",
        "Octavia",
        "Octavio",
        "Olegario",
        
        "Pascual",
        "Pascuala",
        "Patricia",
        "Patricio",
        "Patrocinia",
        "Patrocinio",
        "Paulino",
        "Pedro",
        "Pelayo",
        "Placido",
        "Placida",
        "Prospero",
        
        "Raimundo",
        "Ramón",
        "Raúl",
        "Remedios",
        "Ricardo",
        "Roberta",
        "Robertina",
        "Roberto",
        "Rocío",
        "Rodrigo",
        "Rogelio",
        "Rolando",
        "Rosendo",
        "Rufina",
        "Rufino",
        "Roberto",
        "Roberta",
        
        "Sabrino",
        "Saturnino",
        "Sebastiana",
        "Segismundo",
        "Severiano",
        "Severo",
        "Silvestre",
        "Simón",
        "Susana",

        "Tácito",
        "Tadeo",
        "Telesforo",
        "Teodomiro",
        "Teodora",
        "Teodosio",
        "Trinidad",
        "Tristán",
        "Tulio",

        "Ulises",
        "Urbana",
        "Urbano",

        "Valente",
        "Valeria",
        "Vanesa",
        "Varinia",
        "Verónica",
        "Vicenta",
        "Victoriano",
        "Virgilio",
        "Virtudes",

        "Yago",
        
        "Diego",
        
        "Lorencio",
        
        "Nuño",
        
        "Sans",
        "Sancho",
        "Sancha",
        "Suero",
        
        "Velasco",
        
        "Ximeno",
        
        "Jimeno",
        
        "Brostan",
        "Amón",
        "Igoberto",
        "Rigoberto",
        "Astualso",
        "Alosa",
        "Isiarino",
        "Rordrigo",
        "Daya",
        "Justosa",
        "Fiosio",
        "Eloseva",
        "Daniano",
        "Costo",
        "Anodino",
        "Sonio",
        "Béforo", "Teoberon",
        "Jalisto", "Rostino",
        "Romartín", "Rorto",
        "Prospero", "Rosto",
        "Seldo",
        "Selda", "Aunara",
        "Artosta", "Juriano",
        "Juro", "Joseros",
        "Rosero", "Rosera",
        "Jura",
        "Jácaro", "Rosario",
        "Fingido", "Anancio",
        "Anancia",
        "Pansiano", "Fertilio",
        "Constantina", "Jarana",
        "Morana", "Nora",
        "Olivia", "Olivio",
        "Noro", "Jarano",
        "Valido",
        "Valida", "Abela",
        "Adalina", "Adora",
        "Adriana", "Ana",
        "Antonia", "Basilia",
        "Beatriz", "Bonita",
        "Camila", "Candela",
        "Carmen", "Catalina",
        "Dolores", "Dominga",
        "Dorotea", "Elena",
        "Elicia", "Esmeralda",
        "Felipina", "Francisca",
        "Gabriela", "Imelda",
        "Ines", "Isabel",
        "Juana",
        "Leocadia", "Leonor",
        "Leta", "Lucinda",
        "Marisol",
        "Maria",
        "Maricela",
        "Matilde",
        "Melania",
        "Monica",
        "Nieves",
        "Nilda",
        "Petrona",
        "Rafaela",
        "Ramira",
        "Rosario",
        
        "Sofia",
        "Consuelo",
        "Teresa",
        "Tomasa",
        "Valentia",
        "Veronica",
        "Ines",
        "Isabel",
        "Alejandro",
        "Alfonso",
        "Alonso",
        "Anton",
        "Arcos",
        "Arnoto",
        "Arturo",
        "Bartolomeo",
        "Benito",
        "Bernardo",
        "Blasco",
        "Carlos",
        "Damian",
        "Diego",
        "Domingo",
        "Enrique",
        "Escobar",
        "Aitor",
        "Fernando",
        "Francisco",
        "Gabriel",
        "Garcia",
        "Gaspar",
        "Gilberto",
        "Gonzalo",
        "Gostantin",
        "Jaime",
        "Joan",
        "Juanito",
        "Jorge",
        "Jose",
        "Juan",
        "Martino",
        "Mateo",
        "Miguel",
        "Nicolas",
        "Pascual",
        "Pedro",
        "Ramiro",
        "Ramon",
        "Rodrigo",
        "Sebastian",
        "Salvador",
        "Simon",
        "Tomas",
        "Tristan",
        "Valeriano",
        "Iñigo",
        "Justoso",
        "Vandina",
        "Favio",
        "Rodrigo",
        "Antonia",
        "Iñigo",
        "Juana",
        "Ramonet",
        "Apolonia",
        "Aida",
        "Adolfo",
        "Alvar",
        "Baldomar",
        "Beltran",
        "Carmelo",
        "Dorando",
        "Elvio",
        "Fernan",
        "Gerardo",
        "Heraldo",
        "Isandro",
        "Jovito",
        "Ladislao",
        "Maximo",
        "Nando",
        "Orlando",
        "Paco",
        "Quinto",
        "Ricardo",
        "Santiago",
        "Teodoro",
        "Ubaldo",
        "Vidal",
        "Wilfredo",
        "Ximen", "Yago",
        "Zaragoza", "Esteban",
        "Ignacio",
        "Julio",
        "Mauricio",
        "Nestor", 
        "Oscar", "Pablo",
        "Quirino", "Reynaldo",
        "Sergio", "Teo",
        "Ulises", "Vicente",
        "Xavier", "Ysmael",
        "Zeferino", "Felipe",
        "Gerardo", "Horacio",
        "Isidro", "Jacobo",
        "Lorenzo",
        "Maceo",
        "Norberto",
        "Octavio",
        "Ponce", "Quique",
        "Raul", "Silverio", 
        "Toribio", "Ugo",
        "Victorino", "Waldo",
        "Xerxes", "Yesid",
        "Zacarias", "Adan", 
        "Bartolome", "Celestino",
        "Demetrio",
        "Ernesto",
        "Fidel",
        "Guillermo",
        "Hilario", 
        "Indalecio", "Joaquin",
        "Luis",
        "Manolo",
        "Narciso",
        "Osvaldo",
        "Pedro",
        "Ramon",
        "Sancho",
        "Timoteo",
        "Urbano",
        "Valentino",
        "Wilmer",
        "Xico",
        "Ysidro",
        "Zenon"
        ]
    
    DwarvenSurnames = [
        "Stonewrought",
        "Forgekeeper",
        "Gemseeker",
        "Deepdelver",
        "Mountainborn",
        "Anvilbender",
        "Goldbeard",
        "Runebearer",
        "Earthshaker",
        "Fireforge", 
        "Oropeza",
        "Montoya",
        "Castillo",
        "Valencia",
        "De la Vega",
        "Cortez",
        "Navarro",
        "Esparza",
        "Aguirre",
        "Del Toro",
        "Cervantes",
        "Mendoza",
        "Lopez de Oro",
        "Zambrano",
        "Arroyo",
        "Bernal",
        "Herrera",
        "De la Cruz",
        "Serrano",
        "Villanueva",
        "Galindo",
        "Salazar",
        "Bautista",
        "Vega",
        "Cardenas",
        "Valdez",
        "Coronado",
        "De Leon",
        "Hidalgo",
        "Trejo",
        "Bolivar",
        "De la Fuente",
        "Moreno",
        "Pizarro",
        "Velazquez",
        "Estrella",
        "Salcedo",
        "Machado",
        "De Santiago",
        "Del Rio",
        "Luna", "Solis",
        "Miranda",
        "Rojas",
        "Ortega",
        "Ponce de Leon",
        "Marquez",
        "Fuentes", 
        "Dorado",
        "Belmonte",
        "Guevara", "Cordero",
        "Rico",
        "De la Mora",
        "Trujillo",
        "Andino",
        "Sierra",
        "De las Casas",
        "Valiente",
        "Santos",
        "Mojica",
        "Reyes de Oro",
        "Briseno",
        "De la Torre",
        "Montes",
        "Barrios",
        "Orellana",
        "Valero",
        "Escobar",
        "Nunez del Prado", 
        "Cazares",
        "Zaragoza",
        "Alcantar",
        "Del Monte",
        "De la Rosa",
        "Toledo",
        "Paredes", 
        "Rendon",
        "Giron",
        "Vargas",
        "De Alba",
        "Cazador",
        "De la Garza",
        "Salvador",
        "Rios",
        "Oronegro",
        "Hierrofino",
        "Piedrapreciosa",
        "Minadeplata",
        "Piedrajoya",
        "Oroazul",  
        "Plataclara",
        "Rubirote",
        "Joyadelmar",
        "Montediamante",
        "Ororico",
        "Cavernaoro",  
        "Platafuerte",
        "Gemaestrella",
        "Hierroprofundo",
        "Metalbrillante",  
        "Oradelfuego",  
        "Fraguamaestra", 
        "Mazodehierro",  
        "Escudopiedra", 
        "Corazóndorada",   
        "Martillazo", 
        "Picoagudo",  
        "Lingotedeoro",  
        "Cristalclaro",  
        "Montañaminera",   
        "Escudojoya",  
        "Ardorfuego",   
        "Aceroantiguo",  
        "Cascoduro",   
        "Piedrafuerte",  
        "Esmeraldaeterna",  
        "Piedradeluz",  
        "Oroescondido",   
        "Luzdemina",  
        "Relucienteplata",   
        "Hierrosagrado",  
        "Agujerojoya",  
        "Piedradevalor",   
        "Riolatente",  
        "Corazóndeacero",  
        "Oradelsol",  
        "Minadellago",  
        "Grialdeplata",   
        "Escoriabrillante",  
        "Monteplata",  
        "Astilladehierro",   
        "Fuentedeoro",  
        "Cascodediamante",  
        "Reflejometálico",   
        "Torredelmina",   
        "Guardiánmetal",   
        "Aurorubí",  
        "Luzdeesmeralda",  
        "Piedrapura",  
        "Mantojade",   
        "Brazodehierro",  
        "Cristaldelmonte",   
        "Eslabónantiguo",  
        "Cuentadeoro",   
        "Piedraluna",   
        "Hojadeplata"  
        "Rocaeterna",  
        "Platacasta",   
        "Cristalazul",  
        "Orofrío",  
        "Escudorubi",  
        "Hierroestelar",  
        "Joyasolida",  
        "Martillodeluz",   
        "Cavernadiamante",   
        "Aceroazur",  
        "Ororiel",  
        "Cristalmontaraz",  
        "Labradodeplata",
        "Mazodeplata",  
        "Picoresplandor",  
        "Piedraestrella",  
        "Orígenmetal",   
        "Riachuelooro",  
        "Gemaalma",   
        "Acerodelsur",   
        "Piedrarosada",   
        "Pozodeplata",  
        "Vínculodehierro",   
        "Ororosado",   
        "Escudoesmeralda",  
        "Minacorazón",  
        "Labiosderubi", 
        "Espejoplata",  
        "Relojdeoro",  
        "Lagrimajoya",  
        "Piedramar",   
        "Esteladiamante",   
        "Cristalreal",  
        "Monteescudo",   
        "Orablanco",  
        "Luzdeambar",   
        "Guardiándeplata",  
        "Espiraldehierro",  
        "Tesoroabierto",   
        "Cumbredelplata",   
        "Sueñodeoro",  
        "Piedrasagaz",  
        "Cadenadeacero",   
        "Aguamarinaclara",  
        "Aullidometálico",   
        "Torrejoya",  
        "Pilardeoro",   
        "Lanzadeplata",   
        "Piedrasusurro",  
        "Rocíometálico",  
        "Lagodeesmeralda",
        "Valledejoyas",  
        "Manantialdeacero",  
        "Oronevado",  
        "Espadacristal",  
        "Cordilleraacero",
        "Almadeplata",  
        "Fuentedejoyas",
        "Escudodorado",  
        "Hojametal",  
        "Riscoplata",  
        "Cavernaclaridad",  
        "Orígenpiedra",  
        "Gotaesmeralda"  
        ]
    if Type == "Dwarf": 
        Names = Dwarves
        Surnames = DwarvenSurnames
        FullNames =  random.choice(Names) + ' ' + random.choice(Names) + ' ' + random.choice(Surnames)
        return FullNames

    Elementals = [
        # Water Elementals
        "Aqualis",
        "Vatnavi",
        "Suyasha",
        "Neptaline",
        "Llyncor",
        "Aqua",
        "Atlantic",
        "Pacific",
        "Indian",
        "Arctic",
        "Antartic",
        "Argonaut",
        "Lotus",
        "Kailani",
        "Neptune",
        "Neptuno",
        "India",
        "Maren",
        "Mar",
        "Oceano",
        "Lake",
        "Kai",
        "Bay",
        "Lake",
        "Bahia",
        "River",
        "Nile",
        "Kai", "Caspian",
        "Cora", "Maya", "Amalia", "Maia", "Mira",
        "Talia", "Amaya", "Tallulah", "Ren", "Rene",
        "Well", "Marin", "Severn", "Marina", "Tiber",
        "Tiberius", "Jennifer", "Jen", "Rain", "Wade",
        "Ocen", "Oceanus", "Beck", "Malik", "Malek",
        "Irv", "Clyde", "Indus", "Indo", "Nimue", "Nim",
        "Avalon", "Merlin", "Nixie", "Doris", "Kent",
        "Kendall", "Rio", "Cove", "Bahia", "Innes",
        "Moses", "Fuji", "Anahita", "Ginevra", "Gin",
        "Ginebra", "Jordan", "Rayan", "Kelvin", "Nori",
        "Arno", "Saga", "Lago", "Struan", "Stream", "Varsha",
        "Shannon", "Ondine", "Onda",
        "Misty", "Monroe", "Arnav",
        "Ama", "Lynn",
        "Moishe", "Yara",
        "Yareli", "Oceane", "Thalassa",
        "Bay", "Bey", "Neptune",
        "Neptuna", "Sea", "Kairi",
        "Ria", "Indra",
        "Kano", "Aarna", "Niara",
        "Niagara", "Nebula",
        "Delta", "Aalto",
        "Po", "Araluen", "Jora",
        "Naim", "Narelle", "Nahla", "Nerida",
        "Nereida", "Neri", "Cherith",
        "Adair", "Lir", "Reva", "Sereia",
        "Aqua", "Eyre", "Mar", "Moana",
        "Triton", "Euna", "Undine", "Nebula",
        "Meara", "Loch", "Naida", "Oceana",
        "Gali", "Tal", "Loire", "Rilla",
        "Varuna", "Maayan", "Oceanus",
        "Kalani", "Aquarius", "Acuario", "Danu",
        "Danubio", "Tarka", "Nen", "Gal",
        "Rivo", "Duna", "Zarya", "Laguna",
        "Seine", "Sena", "Alun", "Kallan",
        "Cascada", "Danube", "Onda", "Wave",
        "Baia", "Nile", "Nilo", "Maree",
        "Marea", "Adria", "Adriana", "Alda",
        "Alma", "Amaya", "Anahita",
        "Asita", "Cherith", "Darya",
        "Dayla", "Hali",
        "Kendra", "Loire",
        "Marella",
        "Michal", "Mira",
        "Nahla", "Namra", "Reva",
        "Ria", "Salila",
        "Sarita", "Talia",
        "Zarna", "Zarya",
        "Adair", "Afron", "Alon",
        "Andreus", "Arnon",
        "Bahari", "Gafar",
        "Haf", "Jafar", "Kallan",
        "Kaveri", "Malik",
        "Ninad", "Odine",
        "Pavati", "Pulin",
        "Sagara", "Siva",
        "Wade", "Adva", "Ara",
        "Arna",
        "Baia", "Bay", "Cascade",
        "Cascada",
        "Coral", "Eira", "Euri",
        "Isa", "Ice", "Snow",
        "Isla", "Jamaica",
        "Jordan", "Jubal",
        "Kai", "Kenga", "Kline",
        "Lago", "Laguna",
        "Laco", "Lake", "Laik",
        "Maris", "Morgan",
        "Morgana", "Nira",
        "Rayan", "Shandy",
        "Shannon", "Shore",
        "Adair", "Amaya",
        "Cary", "Kisima",
        "Laguna", "Narelle", "Nile",
        "Nilo", "Nimue", "Serena", "Sereno",
        "Yara", "Alon", "Kano", "Wade", "Naia", "Tide",
        "Adriatic", "Ariel", "Athena",
        "Atena", "Azena",
        "Eldoris", "Marin",
        "Kona", "Argo",
        "Arcadia",
        "Blue", "Lima",
        "Andaya",
        "Niar", "Mora",
        "Amal",
        "Kaya", "Dorian",
        # Fire Elementals
        "Pyraan",
        "Agnivir", "Tulikor",
        "Igniferro", "Lavasol",
        "Fuocco", "Phoenix", "Ember",
        "Cyrus", "Rhys",
        "Apollo", "Kenna", "Blaze",
        "Flame", "Arsenic",
        "Kenna", "Ravi",
        "Aster", "Ignatius",
        "Ignacio", "Ignatio",
        "Hera", "Uri",
        "Edris", "Satish",
        "Calcifer", "Sol",
        "Solina", "Solin", "Salamander",
        "Ardea", "Ravee",
        "Vulcan", "Eldir",
        "Hito", "Agni", "Waru",
        "Alev", "Haco", "Adar",
        "Agni", "Aiden",
        "Adish", "Afi",
        "Ardere", "Ash",
        "Ashbel", "Atesh", "Blaze",
        "Bodaway", "Brand",
        "Brando",
        "Branton", "Brent",
        "Conleth", "Cimbeline",
        "Cyrus", "Cirio", "Egan", "Finlo",
        "Fintan", "Flint",
        "Haco", "Hagan", "Hakan",
        "Helios", "Elio", "Inigo", "Iñigo",
        "Ishaan", "Keahi",
        "Keegan", "Kenneth",
        "Kiran",
        "Maccoy", "Nuri",
        "Prometheus",
        "Prometeo", "Promezeus",
        "Prometeus", "Ra",
        "Rhys",
        "Tyson", "Uri",
        "Vulcan", "Aalish",
        "Aidan", "Adar",
        "Aithne", "Aizne",
        "Alinta",
        "Anala", "Azar",
        "Barbara", "Calida",
        "Candace", "Cinder",
        "Ceniza", "Cinderella",
        "Cinderel", "Edan",
        "Ember", "Ambar",
        "Amber", "Ena",
        "Enya", "Anya", "Fiamma",
        "Flama",
        "Idris",
        "Kalama",
        "Kenna",
        "Pele", "Fenix",
        "Shula", "Souzan", "Tana",
        "Burn", "Abenanka",
        "Aguya", "Aithne",
        "Alinta", "Bedelia",
        "Brid", "Calida",
        "Calina", "Enya",
        "Eña", "Enia", "Ember",
        "Fiamma", "Nina",
        "Shula", "Tana",
        "Tanwen", "Admani",
        "Agni", "Aiden",
        "Anala", "Aodh",
        "Brandr", "Branton",
        "Blaze", "Brand",
        "Cinaed", "Conleth",
        "Conlez", "Egan",
        "Edan", "Edana",
        "Flint", "Fintan",
        "Hagan", "Haco",
        "Vela", "Ignacio",
        "Inigo", "Iñigo",
        "Ignatius",
        "Kenez", "McCoy",
        "Mishal", "Mogotsi",
        "Nuri",
        "Nuria", "Plamen",
        "Pirro", "Pyrrhus",
        "Pirrus", "Tanguy",
        "Tito", "Titus",
        "Uri", "Vatroslav",
        "Azar", "Hayden",
        "Keahi",
        "Liekki", "Fenix",
        "Rhys", "Igno",
        "Kenez",
        "Blaise", "Blaze",
        "Aalish", "Aatish",
        "Aatix", "Atix",
        "Aarush", "Aarux",
        "Arux",
        "Abenanka", "Adara",
        "Adeen", "Adish",
        "Admani", "Amani",
        "Adurnarseh", "Aed",
        "Afi", "Agneya", "Agnes", "Agni", "Agnimitra",
        "Agnivo", "Aguya", "Ahdan", "Aidan",
        "Aiden", "Aine", "Aithne", "Aizne", "Akiho",
        "Aldebrand", "Alev", "Alinta", "Amarkeeri",
        "Anala", "Angarika", "Apoy", "Ardere",
        "Arder", "Ardor", "Atsila", "Azar",
        "Azula", "Azarnoosh", "Basia", "Bedelia",
        "Brantley", "Brigid", "Brit", "Cemre",
        "Chantico", "Conlez", "Conleth", "Conley",
        "Fajra", "Faira", "Fiamma", "Flama",
        "Fiama", "Felio", "Felia", "Felios", "Hurik",
        "Idris", "Ignacia", "Ishat", "Kamar",
        "Kazuya", "Keahi", "Keegan", "Kenna", "Kindle",
        "Kai", "Lieki", "Mahuika", "Mashal",
        "Torch", "Antorcha", "Torcha", "Mogotsi", "Nina",
        "Nootau", "Nutau",
        "Oya", "Plamen",
        "Pyro", "Piro", "Piros", "Pirus", "Ris", "Piris",
        "Shohreh", "Sore", "Shula", "Souzan",
        "Tanguy", "Ugne", "Igne", "Ignea", "Azar",
        "Calida", "Calido", "Fuji", "Neri",
        "Aiden", "Adal", "Cora", "Areli", "Brina",
        "Arian", "Igna", "Kalal", "Pikah",
        "Alen", "Brind", "Cosha", "Ari", "Keri",
        "Cider", "Cavo", "Fenix", "Adarin",
        "Bris", "Azam", "Calan", "Arur",
        # Earth Elementals
        "Terraque", "Muldor", "Rocalia",
        "Kivinari", "Prithvani",
        "Terra", "Onix", "Opal", "Aluminum",
        "Gallium", "Indium", "Tin", "Thallium",
        "Lead", "Bismuth", "Nihonium", "Igneus",
        "Igneous", "Igneo", "Ignea", "Sedimentar",
        "Sedimentario", "Sedimentaria", "Metamor",
        "Metam", "Dacite", "Basalt", "Granite",
        "Pegmatite", "Basalt", "Obsidian", "Stone",
        "Chalk", "Sand", "Iron", "Slate", "Skist",
        "Garnet", "Marble",
        "Jade", "Ore", "Adakite",
        "Andesite", "Alkali", "Basalt", "Basanite",
        "Magnesium", "Lava", "Volcan", "Potassium",
        "Silica", "Rock", "Carbon", "Carbonite",
        "Ender", "Dacite", "Dolerite", "Corsite",
        "Dunite", "Olivine", "Essexite", "Granite",
        "Grane", "Dune", "Pluton",
        "Kimberlite", "Diamond", "Latite",
        "Obsidian", "Pumice", "Scoria", "Sovite",
        "Dolomite", "Chalk", "Coal", "Quartz", "Cuarzo",
        "Salt", "Marble", "Granite", "Lapislazuli", "Lapis",
        "Lazuli", "Adamite", "Adelite", "Arenite", "Almandite",
        "Alumn", "Alunite", "Amarantite", "Anandite", "Antimony",
        "Azurite", "Adamantine", "Agate", "Alabaster", "Bismite",
        "Bismut", "Bronce", "Cadmium", "Cerite", "Carvonite", "Crystal",
        "Copper", "Cobre", "Cementite", "Emerald", "Diamond", "Mine", "Fluorite",
        "Garnet", "Gold", "Hematite", "Magnetite", "Manganite", "Mesolite", "Mimetite",
        "Mica", "Magnesia", "Neptinite", "Pyrite", "Pirite", "Quartz", "Ruby", "Titanite",
        "Turquesa", "Turkis", "Turquoise", "Tremor", "Uralite", "Zeolite", "Zinc", "Zircon",
        "Lithium", "Sodium", "Potassium", "Rubidium", "Cesium", "Francium", "Berillium", "Magnesium",
        "Calcium", "Strontium", "Barium", "Radium", "Aluminium", "Gallium", "Indium", "Tin", "Thallium",
        "Lead", "Bismuto", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel",
        "Copper", "Zinc", "Zirconium", "Rodium", "Palladium", "Silver", "Cadmium", "Tunsten", "Osmium",
        "Platinum", "Gold", "Mercury", "Plata", "Oro", "Copernicium", "Uranium", "Plutonium", "Curium",
        "Californium", "Einstenium", "Fermium", "Nobelium", "Lithium", "Berilium", "Sodium", "Magnesium",
        "Potasium", "Calcium", "Titanium", "Vanadium", "Chrome", "Chromium", "Manganese", "Iron",
        "Cobalt", "Nickel", "Copper", "Zinc", "Gallium", "Rubidium", "Strontium", "Zirconium", "Niobium",
        "Rodium", "Silver", "Cadmium", "Indium", "Tin", "Cesium", "Cerium", "Promethium", "Iridium",
        "Platinum", "Mercury", "Mercurium", "Lead", "Bismutium", "Polonium", "Uranium", "Alabaster",
        "Argento", "Berilio", "Clay", "Coal", "Cobalt", "Dustin", "Elessar", "Emerald", "Ferro", "Granite", "Mercury", "Mica", "Oriol", "Oro", "Peter", "Pedro", "Saphir", "Silver", "Steel", "Stone", "Zircon", "Bronze", "Iron", "Ferro", "Electrum", "Sterling", "Argentium", "Titanium", "Cole", "Arena", "Arenita", "Flint", "Duna", "Amatist", "Gravel", "Gaia", "Boulder", "Bould", "Atlas", "Avalanche", "Midas", "Flint", "Basalt", "Jade", "Mita", "Coba",
        # Air Elementals
        "Aerlyn", "Vaataan", "Tuulikas", "Ilmara", "Caelistis",
        "Aero", "Aelio", "Aeolian", "Gale", "Zefir", "Zefyr", "Zephyr", "Zefirus",
        "Wuzer", "Wuther", "Haboob", "Abroholos",
        "Auster", "Austru", "Barat", "Barber",
        "Bayamo", "Bora", "Borasco", "Boreas", "Boreal",
        "Aurora", "Brisa", "Briza", "Brisot", "Brubu", "Cave",
        "Kaver", "Chubasco", "Cierzo", "Contrastes", "Cordonazo",
        "Cyclone", "Etesian", "Euros", "Hurricane", "Huracan", "Wind",
        "Viento", "Leste", "Levanter", "Levante", "Levantera", "Levanto",
        "Leveche", "Mistral", "Norte", "Noreaster", "Norestero", "Norwester",
        "Noroestero",
        "Nortero", "Ostria", "Pali", "Santana", "Shamal", "Sharki",
        "Siroco", "Sumatra", "Tramontana", "Tifon", "Zefiros", "Zefiro", "Zefir",
        "Bora", "Etesian", "Levant", "Levante", "Leveche", "Harmatan", "Karaburan",
        "Buran", "Orosi", "Sarma", "Shamal", "Alisio", "Alize", "Bayamo", "Brisote",
        "Caju", "Nordeste", "Minuano", "Zonda", "Pampero", "Sudestada", "Cordonazo",
        "Coromuel", "Norte", "Autan", "Bise", "Brise", "Brisa", "Burle", "Cers",
        "Cierzo", "Etesian", "Euroclydon", "Fohn", "Gregale", "Helm", "Leveche",
        "Lodos", "Maestro", "Marin", "Mistral", "Nordes", "Ostro", "Poliente",
        "Solano", "Tramontane", "Vendavel", "Kona", "Abel", "Aeolus", "AkashAmun",
        "Anan", "Cloud", "Anil", "Nube", "Anore", "Arkansas", "Avel", "Barak",
        "Baran", "Brontes", "Caelus", "Corentin", "EnlilErjon", "Esen", "Guntur",
        "Keanu", "Matuu", "Mellan", "Moe", "Myrsky", "Naseem", "Neifion", "Neil",
        "Neve", "Nigel", "Notus", "Payne", "Perun", "Firun", "Samir", "Sepher",
        "Shu", "Sky", "Stromur", "Sturm", "Thor", "Thunder", "Storm", "Torm", "Tufani",
        "Van", "Zenith", "Zephyr", "Zeus", "Aella", "Aethra", "Ahana", "Alize", "Amihan",
        "Anemos", "Anila", "Araceli", "Audra", "Aura", "Auretta", "Awen", "Azure", "Bonaria",
        "Ciela", "Cielo", "Dangira", "Dima", "Ekaitza", "Era", "Glaw", "Haizea", "Haneul",
        "Inanna", "Iris", "Kafeira", "Cafeira", "Minnesota", "Misty", "Mist", "Nephele", "Ninlil", "Nuit", "Pilvi", "Puleng", "Rain", "Rakia", "Samira", "Sema", "Skye", "Stormy", "Tempest", "Tondra", "Varsha", "Vetra", "Zerua", "Zilan", "Mistral", "Gibli", "Zonda", "Etesian", "Shamal", "Aither", "Akash", "AlizehAmphorn", "Amun", "Anan", "AnilAnore", "Anvindr", "Ayaz", "Bayu", "Boreas", "Caelus", "Corentin", "Enlil", "Erjon", "Ermir", "Esen", "Eyvinder", "FujinGokcan", "Govad", "Guzrie", "Hayate", "Ilmari", "Keyne", "Naseem", "Neven", "Notus", "Ouranos", "Payne", "Rabi", "Samir", "Sepher", "Soma", "Sota", "Tifon", "Vayu", "Zeferino", "Zenit", "Zefir", "Zeru", "Zeus", "Aella", "Aethra", "Ahana", "Alizee", "Alizeh", "Alya", "Amaterasu", "Amihan", "Anila", "Aria", "Aureole", "Auretta", "Azure", "Bonaria", "Breeze", "Brisa", "Ciela", "CoroEra", "Esen", "Eteri", "Haizea", "Haneul", "Ilma", "Kailani", "Kalani", "Lulani", "Makani", "Meltem", "Miku", "Mystral", "Nasima", "Ninlil", "Nuit", "Rakia", "Samira", "Sciron", "Scirocco", "Sefarina", "Sema", "Skye", "Tadita", "Wind", "Zephyrine", "Zerua", "Damini", "Oya", "Nebula", "Misty", "Mist", "Wind", "Brenna", "Sail", "Vela", "Katrina", "Amakir", "Abub", "Zeam", "Vesha", "Nura", "Wura", "Enarise", "Amana", "Aeana", "Akades", "Miste", "Zecori", "Sirocco", "Siroco", "Aura", "Zepherien", "Sior", "Annora", "Ael",

        # Additional Elemental References
        "Lignan", "Metallor", "Astrelitz", "Fulgarnis",
        "Glacialyne", 
        "Rayostrike",
        "Jääspirit", "Ombrosyl",
        "Element"
    ]
    if Type == "Elemental": 
        Names = Elementals
        Surnames = Elementals
        FullNames =  random.choice(Names) + ' ' + random.choice(Surnames)
        return FullNames

    Avens = [
        "Murder", "Corvid", "Corvus", "Cuervo",
        "Raven", "Murderfoe", "Corvo", "Crow",
        "Kraai", "Taruja", "Sorre", "Krahe",
        "Alghurab", "Agrrav", "Qarga", "KaKasi",
        "Kaka", "Varona", "Kyaeekaann", "Vrana",
        "Kaek", "Kage", "Corb", "Uwak",
        "Khwangwala", "Wuya", "Kaputa", "Kamagwi",
        "Corbu", "Kok", "Krage", "Kaalhu",
        "Cuervo", "Korbo", "Vares", "Belea", "Akpavia",
        "Varis", "Corbeau", "Feannag",
        "Fran", "Corvo", "Kheree", "Choak", "Kavala",
        "Kaokao", "Cawla", "Caw", "Goaika",
        "Gagak", "Kakka", "Vrana", "Kraischen",
        "Nnamungoona", "Libata", "Varna", "Fung",
        "Zax", "Blak", "Bod", "Black", "Karga", "Igikona",
        "Qarga", "Manuk", "Gagak",
        "Karasu", "Corvo", "Kraka", "Preachan", "Crow",
        "Raven", "Rook", "Corax", "Burung",
        "Gagak", "Uwak", "Uko", "Varju", "Tsov", "Kaua",
        "Koo", "Hankaka", "Kagado", "Yryvu",
        "Koraki", "Qvavi", "Kaga", "Krake", "Qurruu",
        "Kam", "Wrona", "Corvo", "Cuervo",
        "Cioara", "Vorona", "Matuu", "Legokobu", "Vrana",
        "Lekgwaba", "Gunguwo", "Tuke",
        "Kunguru", "Gala", "Gagak", "Uwak", "Xika",
        "Kakam", "Kapra", "Zoq", "Kaki",
        "Vukuvuku", "Karga", "Garga", "Kwaakwaadabi",
        "Vorona", "Qarga", "Conqua",
        "Unomyayi", "Krou", "Kuroo", "Igwababa", "Kror",
        "Kak", "Kakab",
        "Kargw", "Kri",
        "Karok", "Corak", "Kavue", "Kakur", "Karaga",
        "Kakor", "Kaerv", "Kagaka", "Comunko",
        "Corv", "Krueng", "Karak", "Kalaa", "Cabur",
        "Kara", "Kak", "Karvis", "Korvun",
        "Corvi", "Kukurv", "Haden", "Kanak", "Lera",
        "Krai", "Kabak", "Unkur", "Kagan",
        "Kakur", "Krara", "Koror", "Kakara", "Kar",
        "Kaa", "Corr", "Kavon", "Kanaka",
        "Kakut", "Kakak", "Kax", "Koke", "Kaeru",
        "Karva", "Covar", "Karu", "Kakar",
        "Kana", "Kav", "Draven",
        "Kenku",
        "Chirrik", "Flit", "Glide", "Mimic", "Echo",
        "Shimmer", "Talon", "Plume", 
        "Soar", "Shade", "Dusk", "Dawn", "Twilight",
        "Nightcall", "Wingbeat", 
        "Rustle",
        "Murmur", "Feather", "Perch",
        "Roost", "Glitter", "Beaksharp", 
        "Swoop", "Windrider", "Cloudwing", "Skydance",
        "Mooncaw", "Sunfeather", 
        "Starshine", "Hoopoe", "Chatter", "Squawk",
        "Preen", "Beacon", "Ruffle", 
        "Silhouette", "Frostwing", "Skyshriek",
        "Windwhisper", "Nighthawk", "Skygleam", 
        "Stormwatch", "Raincry", "Snowplume",
        "Thundercaw", "Windfeather", "Songthief", 
        "Eclipsing", "Shadowplay", "Sunshadow",
        "Pinnacle", "Crest", "Echoflap", 
        "Nestling", "Skyward", "Sable", "Flock",
        "Whistle", "Hush", "Lustrous", 
        "Mottle", "Pepper", "Tint", "Hue",
        "Canvas", "Sketch", "Inkfeather", 
        "Jewel", "Gemwing", "Prism", "Spectra",
        "Ripple", "Glisten", "Gleam", 
        "Harmony", "Rhythm", "Melody", "Crescendo",
        "Lilt", "Aria", "Sonnet", 
        "Verse", "Chorus", "Note", "Chime", "Bell",
        "Tune", "Clef", "Lyric", 
        "Resonate", "Hum", "Whirl", "Echoing",
        "Tempest", "Zephyr",
        "Soarer", "Glider", "Diver", "Migrant",
        "Nester", "Chirper", "Hover", "Plumage",
        "Beak", "Wing",
        "Feather", "Claw", "Talon", "Beacon",
        "Singer", "Caller", "Flight", "Skyward",
        "Preen",
        "Bill",
        # Raptor-inspired:
        "Falcara", "Hawkwind", "Aquila",
        "Kestralis", "Ospryion", "Harrix", "Buzzaros",
        "Vultar", "Condrex", "Merlynx",

        # Songbirds-inspired:
        "Finchwind", "Larkspire", "Warblyn",
        "Thrushtar", "Sparrox", "Oriox", "Tanagral",
        "Chickador", "Wrenshade", "Nightinglare",

        # Waterfowl-inspired:
        "Duckshade", "Gooslyn", "Swanpeak",
        "Pintar", "Mallarion", "Tealis", "Pelicarn",
        "Heronshade", "Egryx", "Loonspire",

        # Ocean Birds-inspired:
        "Gullwind", "Terrix", "Albatrosar",
        "Puffinox", "Cormorantyx", "Petralis",
        "Skuarion", "Shearshade",

        # Tropical Birds-inspired:
        "Parroshade", "Macawind", "Toucanar",
        "Hoopion", "Sunbyrd", "Hornbillar",
        "Quetzyx", "Cotingar",

        # Game Birds-inspired:
        "Quailfire",
        "Pheasanar",
        "Grousewind",
        "Turkshade",
        "Guineaflare",
        "Peacox",
        "Ptarmyx",

        # Miscellaneous-inspired:
        "Owlspire", "Dovewind", "Pigeonyx",
        "Magpyre", "Jayshade",
        "Lyrebyrd", "Kiwix",
        "Pengshade", "Emurion", "Ostrix",
        "Cassowar", "Flamyn", "Cranar",
        "Storkwind", "Kingfisar",
        "Hummshade", "Woodpyre",
        "Ibix",
        "Tropicar"
        ]
   
    if Type == "Aven": 
        Names = Avens
        FullNames =  random.choice(Names) + ' ' + random.choice(Surnames)
        return FullNames

    Halflings = [
        "Grinhand", "Adaldrida", "Lifwalker",
        "Regina", "Jasmine", "Sam", "Pipim", "Crim",
        "Pint", "Chocolaty", "Love", "Afiry", "Cuki",
        "Chunk", "Dairy", "Peanut", "Buter",
        "Cake", "Milk", "Cone", "Canoli",
        "Caramel", "Canela", "Chis", "Chery", "Chip",
        "Browny", "Chuby", "Tofy", "Cofy",
        "Dublin", "Bake", "Joint", "Widy", "Milky",
        "Minty", "Cuky", "Pistacho", "Pumpin",
        "Almond", "Fresy", "Berry", "Cake", "Vanilla",
        "Sutra", "Tiramisu", "Whisky", "Bacon",
        "Banana", "Beer", "Bluemoon", "Bubble", "Gum",
        "Coffee", "Apple", "Cream", "Candy", "Cotton",
        "Dulce", "Garlic", "Grape", "Punch",
        "Ponche", "Uva", "Grape", "Tea", "Lucuma", "Mango", "Maple", "Chip", "Napolito",
        "Napolita", "Pistacho",
        "Mora", "Rum", "Ron", "Ginebra", "Gin", "Martin", "Martini",
        "Martina", "Licor", "Melon", "Almond", "Almendra", "Manela", "Manzana", "Apple",
        "Apricot", "Balsamic", "Basil", "Berry", "Pepper", "Bourbon", "Bread", "Sugar",
        "Palomita", "Palomito", "Cacao", "Corn", "Caramel", "Carrot", "Cardamom", "Cheddar",
        "Chili", "Chocolate", "Canela", "Cinnamon", "Coconut", "Nut", "Coffee", "Cranberry",
        "Apricot", "Durian", "Espresso",
        "Ferrero", "Fig", "Garlic", "Ginger", "Guinness",
        "Hazelnut", "Honey", "Jam", "Bean",
        "Jelly", "Kaffir", "Lime", "Kiwi", "Fruit",
        "Lemon", "Macadamia", "Mango", "Maple", "Mocha", "Nutella", "Nocciola", "Nuts",
        "Olive", "Pear", "Peppermint", "Pickle", "Pineaple", "Pistachio", "Plum", "Praline",
        "Vino", "Pumpkin", "Raisin", "Rose",
        "Rum", "Tangerine", "Violet", "Walnut", "Oreo",
        "Avocado", "Amaretto", "Almendra",
        "Aguacate", "Amarula", "Aqua", "Burbon", "Cognac",
        "Chai", "Creme", "Coconut", "Pie", "Tarta", "Choc", "Custard", "Dorian",
        "Elderflower", "Evermint", "Fresa", "Fraise", "Fejoa", "Fragola", "Fruitella",
        "Granada", "Granadilla", "Macedonia", "Grosella", "Guava", "Hazelnut", "Honeycomb",
        "Habanero", "Puro", "Cigarro", "Hunny", "Honey", "Miel", "Crema", "Limon", "Cafe",
        "Kinder", "Kitkat", "Leche", "Piruleta", "Nougat", "Neapolitana", "Neopolitan",
        "Nectarina", "Nuggets", "Orange",
        "Naranja", "Onion", "Cebolla", "Oresos", "Orchid",
        "Orangina", "Cacahuete", "Mani", "Peach", "Pomme", "Pera", "Rubarb", "Raisin",
        "Toblerone", "Truffle", "Walnuss",
        "Waffle", "Yogurt", "Yema", "Yuzu", "Carlota",
        "Carrot", "Zanahoria", "Zitron",
        "Picho", "Beler", "Sune", "Numea", "Orelle", "Trafa",
        "Marb", "Sanue", "Nenara", "Nanut",
        "Egumugoni", "Maximus", "Maximo", "Meridio",
        "Bilbo", "Samwise", "Trim", "Milo",
        "Perry", "Pipin", "Caramel", "Gamwick", "Mint",
        "Herleva", "Fairfut", "Berta", "Underfut", "Pamfila", "Punkin",
        "Bramblefoot", "Tansy", "Loras", "Faela", "Primrose", 
        "Celandine", "Bramber", "Eldo",
        "Lalia", "Thistle", 
        "Honeybun", "Ciderpress",
        "Butterscotch", "Tiramis", "Muffinette", 
        "Truffelino", "Raisinet",
        "Orangetwist", "Gelatino", "Sorbetta", 
        "Pesto", "Cinnamelle",
        "Pistachio", "Creampuff", "Nutmeggy", 
        "Frappucin", "Caramelita", "Marshmellowy", "Puddington", "Lemonella", 
        "Gingerspice", "Briochee",
        "Cappuccina",
        "Cherrybelle", "Brownieboots", 
        "Jollybean", "Gigglepot",
        "Merrychuckle",
        "Twinkletoes", "Gleeheart", 
        "Sunshine", "Chuckleberry", "Lightheart",
        "Giddyup", "Delighta", 
        "Gingersnap", "Berry",
        "Mocha", "Taffy", "Nectarina", 
        "Hopskip", "Crumblecake",
        "Lemonlark",
        "Peppermint",
        "Cocoa"
        ]

    HalflingSurnames = [
        "Meadowrover",
        "Hearthkeeper",
        "Merrymaker",
        "Piebaker",
        "Ciderbrewer",
        "Riverfriend",
        "Hillhugger",
        "Woolspinner",
        "Greenpatcher",
        "Fieldwhistler",
        "Goldleaf",
        "Greenhill",
        "Sweetmeadow",
        "Downyhill",
        "Brushwood", 
        "Tumbletoe",
        "Honeyhill",
        "Tealeaf",
        "Burrowbrook",
        "Greenbush", 
        "Brightbrow",
        "Morningdew",
        "Toehop",
        "Nightshade",
        "Honeybrew", 
        "Longmeadow",
        "Clearbrook",
        "Puddlejump",
        "Cloudskip",
        "Smilemore",
        "Raisinfield",
        "Vignoble",     
        "Champignon",   
        "Oliveroot",     
        "Boulanger",    
        "Cidergrove",    
        "Fromagebrook",  
        "Grainmiller",   
        "Lavenderlea",   
        "Beecheese",     
        "Pommierwood",   
        "Barleyville",   
        "Garlicglen",   
        "Trufflemoor",  
        "Berrybush",    
        "Rougemeadow",   
        "Honeycombhill", 
        "Patisserie",   
        "Herbheart",     
        "Légumebrook",  
        "Figflower",     
        "Cheesewick",    
        "Vinewynd",      
        "Moulinmeadow",  
        "Sunflowerfield", 
        "Tarragontrail", 
        "Mustardmont",   
        "Walnutwood",    
        "Thymetown",     
        "Rosemaryridge"  
        "Laughmore",
        "Gourmet",
        "Daydream",
        "Pomme",
        "Avocat",
        "Banane",
        "Mure",
        "Cerise",
        "Chataigne",
        "Clementine",
        "Coco",
        "Datte",
        "Figue",
        "Goyave",
        "Raisin",
        "Pamplemousse",
        "Kiwi",
        "Lime",
        "Mandarine",
        "Mangue",
        "Melon",
        "Olive",
        "Orange",
        "Papaye",
        "Peche",
        "Poire",
        "Anananas",
        "Prune",
        "Pomelo",
        "Framboise",
        "Fraise",
        "Melon",
        "Groseille",
        "Boire",
        "Jouer",
        "Jus",
        "Tomate",
        "Raisin",
        "Limonade",
        "Lait",
        "Fromage",
        "Glace",
        "Champagne",
        "Vin",
        "Bonbon",
        "Oeuf",
        "Pain",
        "Fromage",
        "Fruit",
        "Salade",
        "Mere",
        "Fleurdepomme",
        "Noisette",
        "Noix",
        "Citron"
        ]
    if Type == "Halfling": 
        Names = Halflings
        Surnames = HalflingSurnames
        FullNames =  random.choice(Names) + ' ' + random.choice(Names) + ' ' + random.choice(Surnames)
        return FullNames
    
    Gnomes = [
        "Lando", "Fideli",
        "Jacopo",
        "Acerbi", "Orsini",
        "Domenico", "Montefeltro",
        "Zane", "Garzoni",
        "Orsa", "Rosso", "Masina",
        "Anzola", "Bonzi",
        "Chola",
        "Novella",
        "Babilonio", "Calvis",
        "Contarini",
        "Antonia",
        "Barbolani", "Amideo",
        "Federigo", "Malipiero", "Barbeta",
        "Fabiano", "Calis",
        "Vasari", "Vittoria",
        "Caliara", "Flora",
        "Catalina",
        "Corner",
        "Mudazo", "Loredana",
        "Grana", "Fiorensi",
        "Joanna", "Bascio",
        "Nezetta", "Cecilia",
        "Canasi",
        "Basariona",
        "Maneli", "Candet",
        "Wedekind", "Romuald",
        "Guido", "Reinhold", "Hartwig", "Sunnhild", "Linde",
        "Gerlinde", "Huguette", "Engel", "Ralf", "Norbert",
        "Alberich", "Waldemar", "Markolf",
        "Guerino", "Hugo", "Hugh", "Donella",
        "Cristofano", "Bernardo", "Martinella",
        "Caldarini", "Ludovico",     "Lorenzino",
        "Fiorino",
        "Bellando",
        "Cerzino", "Ortanio", "Dellini", "Vezzoli", 
        "Zanetti", "Graziano", "Orlando",
        "Ruffino",
        "Masetti",
        "Ambrogio", "Bonzino", 
        "Chiaro", "Novelli",
        "Baldassare", "Calvio",
        "D'Este", "Antonello",
        "Bartolini", 
        "Amedeo",
        "Federica", "Malatesta", "Barbato",
        "Fabbretti", "Calisto", "Venturi", 
        "Vigorito", "Calandra", "Fiorenza",
        "Catania",
        "Cortese",
        "Murano", "Lorez", 
        "Granito", "Fiesoli",
        "Jovanni", "Basso",
        "Nerezza", "Celestina",
        "Canelli", 
        "Bassani",
        "Marzio",
        "Candida", "Westaro",
        "Romano",
        "Giulio", "Rinaldo",
        "Hartino", 
        "Serafina",
        "Lindoro",
        "Gherardini",
        "Humberto",
        "Engelo",
        "Rafaelo",
        "Norbino", 
        "Albertino",
        "Waldo",
        "Marcato",
        "Guerriero",
        "Ugo", "Humberto",
        "Donatello", 
        "Cristiano",
        "Bernardino",
        "Martelli",
        "Calabrese",
        "Ludivico",
        "Silvestro"
        ]
    GnomesSurnames = [
        "Gearspinner",
        "Mindtwister",
        "Aetherwisp",
        "Tinkerfoot",
        "Starwhisperer",
        "Clockfixer",
        "Mysticmechanic",
        "Illusionweaver",
        "Sparkjumper",
        "Gadgetgrabber",
        "Bellatink",
        "Fiorentwig",
        "Venetgear",
        "Tuscantool",
        "Luminotti",
        "Artispring",
        "Waldentinker",
        "Folkforge",
        "Bergbolt",
        "Holzcraft",
        "Steinleaf",
        "Wundergear",
        "Florenbolt",
        "Bergvene",
        "Luminwald",
        "Pietravalle",
        "Luccinetti",
        "Bellamonte",
        "Verdini",
        "Montefiore",
        "Ferrato",
        "D'Argento",
        "Zaffiro",
        "Granatello", "Pietradura",
        "Olivetti", "Rovellino",
        "Bianchetti", "Morosini",
        "Dorato", "Marmorini",
        "Fabbretti", "Stellato",
        "Orlandini", "Grazzini",
        "Lapidello", "Smeraldini",
        "Rubinelli", "Diamante",
        "Vespucci", "Palladino",
        "Ghirlanda", "Lunetti",
        "Solari", "Venturino",
        "Piccolino", "Peruzzini",
        "Baldovini",
        "Veneziano",
        "Fiorentini", "Milanesi",
        "Romanelli", "Napolitano",
        "Torresi", "Siciliano",
        "Pescatore",
        "Montanari",
        "Riviero",
        "Valentini", "Fontana",
        "Molinari",
        "Bosco", "Castello",
        "Palazzo",
        "Villa", "Mura",
        "Piazza",
        "Borgo", "Costa",
        "Grotta", "Rocca",
        "Ponte",
        "Giardino",
        "Parco",
        "Fontanella",
        "Mondello",
        "Vigneto",
        "Orchardino",
        "Frutteto",
        "Bacino",
        "Lago",
        "Ruscello"
        ]
    
    if Type == "Gnome": 
        Names = Gnomes
        Surnames = GnomesSurnames
        FullNames =  random.choice(Names) + ' ' + random.choice(Names) + ' ' + random.choice(Names) + ' ' + random.choice(Surnames) + ' ' + random.choice(Surnames) + ' ' + random.choice(Surnames)
        return FullNames

    Tieflings = [
        "Hope",
        "Valor",
        "Mystery",
        "Quiet",
        "Song",
        "Charm",
        "Glimmer",
        "Glory",
        "Noble",
        "Lumin",
        "Whisper",
        "Dancer",
        "Mirth",
        "Revel",
        "Wry",
        "Prayer",
        "Pursuit",
        "Promise",
        "Sorrow",
        "Chance",
        "Eager",
        "Endure",
        "Hallow",
        "Luster",
        "Mend",
        "Riddle",
        "Shade", "Wander",
        "Penance", "Dream",
        "Serenity", "Bliss",
        "Fury",
        "Glee",
        "Insight",
        "Seeker",
        "Solemn",
        "Fate",
        "Grace",
        "Truth",
        "Honor",
        "Vigor", "Rapture",
        "Zeal", "Oath",
        "Radiant", "Sacred", "Bravery",
        "Cunning", "Defiance",
        "Elude", "Freedom",
        "Justice",
        "Mercy",
        "Temperance",
        "Trust",
        "Victory", "Vow",
        "Watch", "Will",
        "Silent", "Solace", "Subtle",
        "Thrift", "Vivid",
        "Abyss", "Serene",
        "Blaze",
        "Glimmer",
        "Torment",
        "Comfort",
        "Wrath",
        "Calm",
        "Venom",
        "Elixir",
        "Malice",
        "Grace",
        "Ravage",
        "Mend",
        "Deceit",
        "Truth",
        "Vile",
        "Pure",
        "Treachery",
        "Loyal",
        "Gloom",
        "Radiance",
        "Dread",
        "Hope",
        "Spite",
        "Favor",
        "Chaos",
        "Order",
        "Ruin",
        "Preserve",
        "Fury",
        "Peace",
        "Woe",
        "Bliss",
        "Taint",
        "Wholesome",
        "Cruel",
        "Kind",
        "Envy",
        "Cherish",
        "Despair",
        "Optimism",
        "Scream",
        "Whisper",
        "Bane",
        "Blessing",
        "Strife",
        "Unity",
        "Haunt",
        "Guard",
        "Sin",
        "Merit",
        "Curse",
        "Gift",
        "Hate",
        "Love",
        "Thorn",
        "Bloom",
        "Shadow",
        "Light",
        "Scorch",
        "Soothe",
        "Rage",
        "Temperance",
        "Grieve",
        "Joy",
        "Decay",
        "Nourish",
        "Lust",
        "Devotion",
        "Pride",
        "Humble",
        "Greed",
        "Generosity",
        "Lies",
        "Honesty"
        "Zephyron",
        "Draconar",
        "Typhos", "Venox",
        "Grisham",
        "Blazefur",
        "Sulfuron",
        "Vornak",
        "Ildrex",
        "Mortigon",
        "Firesyl",
        "Lilivra", "Mornara",
        "Shadeveil",
        "Nefari",
        "Blazelle", "Sorcaria",
        "Vexiana", "Glimshade",
        "Vorrela",
        "Raventhorn",
        "Skullrend", "Shadowclaw",
        "Doomspire", "Felrend",
        "Horrorspire",
        "Nighthowl",
        "Vileshade",
        "Hexmorn",
        "Darkgleam",
        "Hellkin",
        "Nightshade",
        "Doombringer",
        "Ashcaller",
        "Soulbinder",
        "Fireheart",
        "Demonblood",
        "Sinwhisperer",
        "Darkmender",
        "Brimstonetouched",
        "Kurzam", "Rhul", "Zorlarg",
        "Steamsable", "Onyxmaw",
        "Kral",
        "Moltenhorn",
        "Crimsonhorn",
        "Gloomhorn", "Madhorn",
        "Killsin", "Purific", "Nye", "Assurance",
        "Watson", "Faith", "Harris", "Ashes",
        "Shepard", "Tenacious",
        "Coleman", "Desire",
        "Llwyd", "Vanity", "Temple",
        "Submit", "French", "Fear",
        "Reynolds", "Wheelwright",
        "Called", "Burroughs",
        "Confidence", "Udal", "Remember",
        "Bond", "Recuerdo", "Miedo",
        "Obedience", "Young", "Faint",
        "Gilby", "Abuse", "Cawdrey",
        "Constant", "Calamy",
        "Calamidad", "Vanity",
        "Twisse", "Discretion",
        "Boston", "Buried", "Sampson",
        "Hate-ill", "Burton",
        "Forsaken",
        "Williams",
        "Virtue", "Shepard",
        "Amynus",
        "Smen",
        "Apronadius", "Abdamelek", "Xonsu",
        "Aziza", "Ramla",
        "Neema", "Cleopatra",
        "Jendayi", "At", "Sahura", "Hor",
        "Zesiro", "Nub", "Bubastis", "Tauret",
        "Sarapous",
        "Ma",
        "Sapt", "Ritho", "Nenet", "Sanura",
        "Sethenes", "Sept", "Uetu", "Kashto",
        "Clémence", "Firefur", "Gloomtail",
        "Nuuch", "Zenglac", "Ablo", "Gadreel",
        "Uzza",
        "Musique",
        "Haine", "Gloire", "Pyra", "Désespoir",
        "Doute", "Chagrin", "Terreur",
        "Ambition", "Vice", "Ouverture", "Amour",
        "Témérité", "Credo", "Charogne",
        "Chagrin",
        "Hasard",
        "Astaro", "Kali", "Brave", "Crash", "Delver",
        "Helm", "Hungry", "Violence",
        "Providence", "Surprise", "Conqueror",
        "Defender", "Invader", "Juvileo", "Nephelin",
        "Nefelin", "Serafina", "Luz", "Carolin",
        "Dilan", "Kurt", "Freddie", "Pride", "Bulur",
        "Abyx", "Apolion", "Abezetibou", "Abigor",
        "Abraxas", "Abraxis", "Solomon", "Aexma",
        "Acaos",
        "Adramalek", "Agares", "Ariman", "Agraz",
        "Ainin", "Alloces",
        "Alp", "Amduscias",
        "Amenadiel",
        "Amon", "Amorth", "Gabriele", "Andra",
        "Indra", "Andras", "Andrealfus",
        "Mastemoth", "Andromalius", "Angra",
        "Antaura", "Antichrist", "Armadiel", "Aseliel",
        "Asmodeus", "Aeshma", "Ashmedai",
        "Asmodius", "Sydonay", "Astaroth",
        "Azael", "Azazel",
        "Baal", "Bael",
        "Balam", "Baphomet",
        "Bafomet",
        "Barbiel", "Barbuel", "Barmiel",
        "Baruchas",
        "Bathin",
        "Barbatos",
        "Beelxebub",
        "Belzebub",
        "Satan",
        "Ornias",
        "Nicodemus",
        "Behemoth",
        "Lucifer",
        "Madilon",
        "Solymo",
        "Saroy",
        "Zeu",
        "Ameclo",
        "Sagrael",
        "Praredun",
        "Venite",
        "Amen",
        "Leviatan",
        "Beherit",
        "Belet",
        "Bilet",
        "Belfegor",
        "Belial",
        "Beliar",
        "Bernael",
        "Bidiel",
        "Beriz",
        "Balberiz",
        "Beal",
        "Bofi",
        "Bolfri", "Elberiz", "Bidiel",
        "Bifrons",
        "Botis", "Otis", "Buer", "Buriel",
        "Busyasta",
        "Cabariel", "Calder", "Camuel",
        "Caim",
        "Camion", "Carnesiel", "Caspiel",
        "Cassian",
        "Kerberos", "Cerberus", "Cesmak",
        "Coronzon",
        "Cimeries", "Constantine", "Crowley",
        "Daeva", "Deva", "Dev", "Daimon",
        "Agato",
        "Agatodaimon", "Kako", "Kakodaimon",
        "Dalkiel", "Dantanian", "Decarabia",
        "Carabia",
        "Demoriel", "Faustus", "Eligor", "Emoniel",
        "Erinyes", "Fury", "Furia", "Eurynomus",
        "Forneus", "Fortea", "Flauros", "Hauras",
        "Haurus", "Foras", "Furcas", "Furfur", "Gadreel",
        "Gadriel", "Garadriel", "Gediel", "Gemori",
        "Gamaliel", "Gamigin", "Solomon", "Gusion",
        "Hades", "Hagenti", "Harlequin", "Halahel",
        "Halpas", "Hecataea", "Hel", "Hemah", "Hutriel",
        "Iblis", "Icosiel", "Incubus", "Imp", "Ipos",
        "Isacaron", "Leviatan", "Cabala", "Sephirot",
        "Sefirot", "Kezer", "Kokmah", "Binah", "Kesed",
        "Geburah", "Tifarez", "Netzak", "Hod",
        "Yesod", "Malkut", "Kababiel", "Kesilim",
        "Kunda", "Kabiel", "Kokab", "Labartu", "Lahmu",
        "Lamastu", "Legion", "Lerajie", "Oary",
        "Leviatan", "Liliz", "Lucifer", "Luzer", "Lutin",
        "Macariel", "Malgaras", "Malphas", "Malpas",
        "Marbas", "Maseriel", "Mazaquin", "Mazzikin",
        "Mazikin", "Mazakin", "Menadiel", "Mefistofeles",
        "Moloch", "Morax", "Murmur", "Naberius",
        "Nephilim", "Nefilim", "Nemesis", "Nisroc",
        "Onoskelis", "Orias",
        "Ornias", "Orobas", "Ose",
        "Padiel", "Pamersiel", "Paimon", "Pairikas",
        "Pazuzu", "Santeria", "Purson", "Curson",
        "Rabisu", "Raum", "Ravana", "Raysiel",
        "Rimmon", "Ronove", "Roneve", "Sabbat", "Sabnak",
        "Salem", "Saleos", "Salt", "Samael", "Sammael",
        "Sariel", "Sarakiel",
        "Suriel",
        "Uriel",
        "Zerakiel",
        "Satanael",
        "Scepter",
        "Skepter",
        "Shamsiel",
        "Shax",
        "Chax", "Scox",
        "Shedim", "Sinistrari",
        "Lodovico", "Sitri",
        "Solas", "Soleviel",
        "Soraz", "Orleans",
        "Surin", "Symiel",
        "Taru", "TaseTeofilus",
        "Udug", "Ukobach",
        "Usiel", "Uziel",
        "Uzza",
        "Uriel", "Valac",
        "Valefor", "Vapula",
        "Vassago", "Veltis",
        "Vepar", "Separ",
        "Vine",
        "Warren",
        "Zaffis",
        "Zarika",
        "Zepar",
        "Zohk",
        "Zoroastra",
        "Zohak",
        "Disaster",
        "Strong",
        "Forte",
        "Glory",
        "Hawk",
        "Falcon",
        "Sinner",
        "Dawn",
        "Crepusculo",
        "Flama",
        "Flame",
        "Sunrise",
        "Alba",
        "Star",
        "Estrella",
        "Estela",
        "Legend",
        "Blood",
        "Aeon",
        "Veil",
        "Victor",
        "Victoria",
        "Honor",
        "Noble",
        "Ley",
        "Law",
        "Melody",
        "Purity",
        "Rune",
        "Ron",
        "Gin",
        "Sinfinder",
        "Sinner",
        "Song",
        "Cult",
        "Culto",
        "Prayer",
        "Pray",
        "Gunner",
        "Katana",
        "Jester",
        "King",
        "Dante",
        "Danza",
        "Apocalypse",
        "Astaroz",
        "Astaroth",
        "Khemed",
        "Ahset",
        "Amunet",
        "Aneksi",
        "Atet", "Baketamon",
        "Bunefer",
        "Hentie",
        "Herit",
        "Heteferes",
        "Ipuet",
        "Itet",
        "Joba", "Kasmut", "Kemanub", "Khemut",
        "Maia", "Menhet", "Merit", "Nebet",
        "Neferu", "Nit", "Nofret", "Nubemiunu",
        "Peseshet",
        "Rai", "Sadeh", "Sadek", "Sitamun", "Sitre",
        "Takhat", "Tarset", "Werenro", "Ahmose",
        "Amasis", "Amenemhet", "Anen", "Banefre",
        "Bek", "Henenu", "Huya", "Ibebi", "Idu",
        "Ineni", "Ipuki", "Irsu", "Kawad", "Kawab",
        "Kenamon", "Kewap", "Khafra", "Khuesebek",
        "Masaharta", "Meketre", "Merenre", "Metjen",
        "Nebamun", "Nehi", "Nekure", "Nessumontu",
        "Pawah", "Ramose", "Rudjek", "Sabaf", "Sebni",
        "Senusret", "Shabaka", "Somintu",
        "Thaneni", "Theti", "Aktas", "Anakis",
        "Armara", "Astaro", "Astaroz", "Azza", "Belez",
        "Bune", "Criella", "Damaia", "Ishte", "Jezebez",
        "Kali", "Kallista", "Kasdeya", "Lilith",
        "Makaria", "Markosian", "Nemeian", "Nija",
        "Oriana", "Osah", "Felaia", "Pura", "Pyra",
        "Rieta", "Sekhmet", "Semyaza", "Shava", "Zendaya",
        "Shax", "Vapula", "Vepar", "Verin",
        "Akmen", "Amon", "Astar", "Balam",
        "Bazin", "Cain", "Caim",
        "Cimer", "Damakos", "Euron",
        "Kairon", "Nicor", "Oriax", "Paymon", "Atraxas",
        "Samal", "Zamuz", "Valafar", "Zezan",
        "Ambition", "Art", "Carrion", "Chant",
        "Canto",
        "Creed",
        "Death",
        "Despair",
        "Doom",
        "Doubt",
        "Dread",
        "Ecstasy",
        "Ennui",
        "Entropy",
        "Excellence",
        "Fear",
        "Miedo",
        "Glory",
        "Gloria",
        "Gluttony",
        "Grief",
        "Hate",
        "Hope",
        "Horror",
        "Ideal",
        "Ignominy",
        "Risa",
        "Love",
        "Amor",
        "Lust",
        "Mayhem",
        "Mockery",
        "Murder",
        "Muse",
        "Musa",
        "Music",
        "Mystery",
        "Nowhere",
        "Open",
        "Pain",
        "Passion",
        "Poetry",
        "Quest",
        "Random",
        "Reverence",
        "Revulsion",
        "Sorrow",
        "Temerity",
        "Torment",
        "Tragedy",
        "Vice",
        "Virtue",
        "Weary",
        "Ariatari",
        "Grace",
        "Caos",
        "Piety",
        "Azizi",
        "Wit",
        "Dawala",
        "Crimson",
        "Umayma",
        "Nushim",
        "Abrasax",
        "Liberty",
        "Luz",
        "Luzimer"
        ]
    if Type == "Fiend":
        Names = Tieflings
        
        return random.choice(Names)

    return random.choice(Names)


    Goblins = [
        "Dobby", "Chal", "Alsi", "Ax", "Pilb", "Eg", "Udag", "Pilsi", "Pil", "Amal",
        "Valaravanx", "Azarid", "Walajmar", "Roduulf", "Aidoingux", "Azanagi", "Agila",
        "Gainax", "Selenax", "Melisanda", "Radegond", "Seda", "Gaxa", "Amalafrida", "Duda",
        "Wamba", "Ariux", "Azarid", "Gunteric", "Tanaix", "Jordanex", "Badua", "Braja", "Narin",
        "Giso", "Elisaweta", "Raxa", "Amalgard", "Sunnia", "Wella", "Aoric", "Aligern", "Unigild",
        "Razaladar", "Alsiu", "Amanal", "Dund", "Megi", "Pinag", "Budan", "Agala", "Selx", "Gudus",
        "Dona", "Bunging", "Udaler", "Arnensi", "Ravava", "Wagic", "Ambanda", "Sellalby",
        "Azadusar", "Azaz", "Walsi", "Nardu", "Ralaga", "Rajar", "Arida", "Doril", "Rand",
        "Azari", "Amand", "Azawe", "Azal", "Axar", "Xavan", "Rada", "Selala", "Galar", "Druzol",
        "Azal", "Azar", "Udarn", "Azava", "Alal", "Elba", "Alil", "Amaxa", "Azana", "Ralel",
        "Amaxa", "Arinele", "Azoba", "Garag", "Axal", "Axagi", "Talala", "Azari", "Rajma", "Axar",
        "Ralan", "Azax", "Vala", "Radus", "Azava", "Pilax", "Talxa", "Azar", "Azahar", "Rhana",
        "Azaja", "Aldan", "Selan", "Azals", "Chandar", "Azav", "Doby", "Susal", "Azag", "Azan",
        "Azal", "Wari", "Azag", "Azaril", "Nadag", "Azaja", "Gungi", "Buda", "Ralar", "Udala",
        "Elge", "Azaxar", "Dris", "Gana", "Udar", "Elida", "Azan", "Alad", "Ravanda", "Nals",
        "Pic", "Aby", "Mada", "Rorna", "Amba", "Ardun", "Azariga", "Duna", "Buada", "Vagi",
        "Azava", "Guna", "Amal", "Azav", "Ralan", "Ralav", "Rajad", "Talsi", "Amal", "Rarid",
        "Randa", "Amazo", "Wava", "Magus", "Guna", "Slay", "Dasker", "Kexam", "Mukert", "Rensox",
        "Xembor", "Guknag", "Sabsen", "Gundobag", "Burk", "Azava", "Zasiki", "Warishi"
               ]
    Clans = [
        "Redhats",
        "Traphunters",
        "Rusty Dagger Clan",
        "Broken Tooth Clan",
        "Sneaky Shadow Clan",
        "Raging Fire Clan",
        "Cunning Fox Clan",
        "Wild Boar Clan",
        "Quickfoot Clan",
        "Sharp Spear Clan",
        "Sly Raven Clan",
        "Hidden Cave Clan",
        "Noisy Brawler Clan",
        "Muddy Water Clan",
        "Swift River Clan",
        "Gleaming Gem Clan",
        "Fierce Wolf Clan",
        "Clever Trickster Clan",
        "Wily Serpent Clan",
        "Bouncing Rabbit Clan",
        "Laughing Skull Clan",
        "Dancing Leaf Clan",
        "Twilight Trickster Clan",
        "Lunar Lantern Clan",
        "Mystic Mushroom Clan",
        "Whispering Willow Clan",
        "Starlight Stalker Clan",
        "Enchanted Ember Clan",
        "Dancing Dewdrop Clan",
        "Shimmering Shade Clan",
        "Gleaming Glade Clan",
        "Blinking Blossom Clan",
        "Sparkling Stream Clan",
        "Glimmering Grove Clan",
        "Sylvan Shadow Clan",
        "Charming Cherry Clan",
        "Moonlit Marauder Clan",
        "Dewy Dreamer Clan",
        "Frosty Fern Clan",
        "Ethereal Elm Clan",
        "Vibrant Violet Clan",
        "Whimsical Wren Clan",
        "Moonlit Minion Clan",
        "Dazzling Dancer Clan",
        "Enchanted Envoy Clan",
        "Sylvan Servant Clan",
        "Gleaming Guardian Clan",
        "Starlit Steward Clan",
        "Radiant Runner Clan",
        "Shimmering Squire Clan",
        "Lustrous Lackey Clan",
        "Blinking Bearer Clan",
        "Twinkling Tender Clan",
        "Illuminated Intendant Clan",
        "Vivid Valet Clan",
        "Ethereal Errand Clan",
        "Bright Bannerman Clan",
        "Sparkling Seneschal Clan",
        "Luminous Liaison Clan",
        "Mystic Messenger Clan",
        "Whimsical Ward Clan",
        "Feywild Follower Clan",
        "Shadow Sneak Clan",
        "Eclipse Enigma Clan",
        "Nocturnal Nuisance Clan",
        "Mystic Mirage Clan",
        "Gloom Grin Clan",
        "Twilight Trickster Clan",
        "Obsidian Outlaw Clan",
        "Dusk Dweller Clan",
        "Midnight Marauder Clan",
        "Veiled Vagabond Clan",
        "Lunar Lurker Clan",
        "Abyssal Agent Clan",
        "Umbral Usher Clan",
        "Phantom Pilferer Clan",
        "Sable Scamp Clan",
        "Nightshade Nihilist Clan",
        "Wraithlike Wanderer Clan",
        "Crimson Creeper Clan",
        "Sinister Sprite Clan",
        "Vortex Vandal Clan",
        "Tinker Twist Clan",
        "Gadget Gleam Clan",
        "Clever Contraption Clan",
        "Whiz Whirl Clan",
        "Sly Spark Clan",
        "Dazzle Device Clan",
        "Quirk Quiver Clan",
        "Brainy Bolt Clan",
        "Witty Widget Clan",
        "Zany Zip Clan",
        "Puzzle Prowess Clan",
        "Tricky Tinker Clan",
        "Smart Sprocket Clan",
        "Crafty Coil Clan",
        "Inventive Imp Clan",
        "Gizmo Glisten Clan",
        "Snazzy Spring Clan",
        "Brilliant Bolt Clan",
        "Astute Axle Clan",
        "Moxie Mechanism Clan",
        "Not Bright Clan",
        "Lost Map Clan",
        "Running Late Clan",
        "Can’t Pants Clan",
        "Tripped in Dark Clan",
        "Wrong Turn Clan",
        "Oops Clan",
        "Lost Sock Clan",
        "Stuck Jar Clan",
        "Hit Head Clan",
        "Forgot Name Clan",
        "Can’t Tie Shoes Clan",
        "Where’s Hat Clan",
        "Ate Map Clan",
        "Slipped Banana Clan",
        "Walked into Wall Clan",
        "Sitting Puddle Clan",
        "Lost Marbles Clan",
        "Fell Hole Clan",
        "Dancing Tree Clan",
        "Rock Eaters Clan",
        "Sun Stares Clan",
        "Feet Trips Clan",
        "Talks Trees Clan",
        "Head Lost Clan",
        "Cantcount Clan",
        "Moonbarks Clan",
        "Cats Talk Clan",
        "Drools Clan",
        "Marblesharp Clan",
        "Squirrel Dancers Clan",
        "Nosefinders Clan",
        "Spicysnow Clan",
        "Ownlaughs Clan",
        "Shadowfriend Clan",
        "Dull Blade Clan",
        "Muddy Mind Clan",
        "Broken Compass Clan",
        "Topsy Turvy Clan",
        "Backwards Bunch Clan",
        "Loopy Legs Clan",
        "Fuzzy Logic Clan",
        "Silly Snouts Clan",
        "Boggled Brains Clan",
        "Dizzy Dudes Clan",
        "Wacky Whiskers Clan",
        "Noodle Noggins Clan",
        "Giggly Gang Clan",
        "Jumbled Jaws Clan",
        "Twisted Tails Clan",
        "Kooky Knees Clan",
        "Woozy Whelps Clan",
        "Zany Zigzags Clan",
        "Quirky Quills Clan",
        "Fuddle Heads Clan"

        ]
    if Type == "Goblin":
        Names = Goblins 
        
        return random.choice(Names) + "of the " + random.choice(Clans)

    return random.choice(Names)

    if Type == "Undead":
        Names += Goblins + Tieflings + Gnomes + Halflings + Avens + Elementals + Dwarves + Orcs + Giants + Elves + Humans
        
        return random.choice(Names)

    return random.choice(Names)





def Aberrations():
    Names = {
        "Beholder": 8,        # Known for their paranoia and individualism.
        "Shapeshifters": 3,   # Unique appearance as Mimics and shapeshifters with horrible true forms.
        "Illithid": 9,        # A highly intelligent race known for their psionic powers.
        "Aboleth": 7,         # Ancient beings with vast knowledge and a desire to dominate other species. 
        "Flumph": 4,          # They are benevolent and seek knowledge.
        "Neogi": 5,           # Slave traders with a unique hierarchy.
        "Nothic": 6,          # Former wizards transformed into monstrous forms.
        "Slaad": 6,           # Representing pure chaos, they're unpredictable.
        "Star Spawn": 5,      # Cosmic horror element.
        "Tsochar": 4,         # Parasitic entities that can control other beings.
        "Yithian": 4,         # Time-traveling and body-swapping aliens.
        "Githyanki": 7,       # Raiders and conquerors.
        "Githzerai": 7,       # More enlightened.
        }

    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]



def Avens():
    Names = {
        "Birdfolk": 6,    # Generic birdfolk, versatile in nature.
        "Kenku": 8,       # Unique mimicry ability and urban setting.
        "Aarakocra": 7,   # High-flying and more spiritual.
        "Tengu": 5,       # Martial arts and folklore connections.
        "Raptoran": 4,    # Mountain dwellers with a unique flight lifecycle.
        "Strig": 4,       # Owl-like Nocturnal and wise.
        "": 1             # Empty choice for variety.
    }
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]


def Beasts():
    Names = {
        "Armored Bear": 8,  # From Philip Pullman's His Dark Materials series.
        "Monkey King": 9,
        "Guardian Kong": 7,
        "Giant Eagle": 8,      # Inspired by Tolkien.
        "Golden Lion": 7, 
        "White Tiguer": 6,
        "Vulture Spirit": 5,
        "Kitsune Fox": 10,
        "Deer Spirit": 6,  # Associated with gentleness and intuition in various cultures.
        "Giant Owl of Wisdom": 8,  # A universal symbol of knowledge.
        "Celestial Stag": 7,  # Stags are often seen as messengers or connected to the otherworld in various mythologies.
        "Fenrir Wolf": 7,
        "Forest-God Boar": 5,  # A guardian of the forests, revered for its bravery.
        "Cosmic Whale": 6, 
        "Kaiju Dinosaur": 6, 
        "Kerberus Dog": 7,
        "Sun Scarab": 9,
        "Moon Jackal": 6,
        "Godess Spider Queen": 7,
        "World Serpent's Spawn": 7,
        "Elder Elephant": 8 ,
        "":1}
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]


def Beastfolks():
    Names = {
        "Arachnidfolk": 6,     # Spiders are often associated with trickery and weaving fate.
        "Centaur": 9,          # Classic mythological creature, representing the wild side of humanity.
        "Gnoll": 6,            # Often seen as savage and chaotic, inspired by hyenas.
        "Insectfolk": 5,       # Unique and diverse, representing both hive minds and individuality.
        "Jackalmen": 6,        # Often seen in Egyptian mythologies, associated with the afterlife.
        "Kitsune": 8,          # Japanese fox spirits, both mischievous and wise.
        "Lycan": 7,            # General term for were-creatures, known for their cursed transformations.
        "Merfolk": 9,          # Classic creatures of the sea, representing both beauty and danger.
        "Minotaur": 8,         # The embodiment of the labyrinth's mystery and challenge.
        "Ratfolk": 7,          # Clever, opportunistic, and often seen in urban settings.
        "Scorpionfolk": 5,     # Dangerous and venomous, often used as guardians in myths.
        "Sharkfolk": 7,        # Predators of the sea, representing both fear and respect.
        "Werebear": 6,         # A more noble version of lycanthropes, often associated with strength and protection.
        "Werewolf": 9,         # One of the most recognized lycanthropes, representing the untamed side of humanity.
        "Harpies": 7,          # Half-bird, half-woman, often seen as omens.
        "Satyr": 8,            # Revelers and musicians, representing the carefree side of nature.
        "": 1
        }
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

def Celestials():
    Names = {
        "Angelic Bloodline": 17,  # Mortals with celestial ancentry 
        "Half-Angel": 12,         # Mortals with a celestial parent
        "Angel": 9,               # Classic representatives of good, messengers of deities.
        "Ascended": 8,            # Mortals who have risen to a divine or semi-divine status.
        "Couatl": 7,              # Feathered serpents, often seen as guardians or protectors.
        "Forgotten God": 6,       # Once powerful, now forgotten. Represents the ebb and flow of faith.
        "Lesser God": 8,          # Deities of minor aspects or domains.
        "Minor God": 8,           # Similar to Lesser God, deities with limited influence.
        "Pegasus": 7,             # The majestic winged horse, symbol of purity and grace.
        "Planetar": 9,            # High-ranking angels, often seen as warriors of good.
        "Seraph": 9,              # Burning ones, highest order of angels.
        "Throne": 8,              # Angels associated with celestial justice and maintaining the cosmic order.
        "Unicorn": 7,             # Pure and gentle creatures, often associated with forests and healing.
        "Celestial Dragon": 8,    # Dragons that reside in the heavens, symbols of power and majesty.
        "Valkyrie": 7,            # Choosers of the slain, guiding heroes to the afterlife.
        "Solar": 9,               # Extremely powerful celestial beings, champions of deities.
        "Ki-rin": 7,              # Eastern counterpart to unicorns, symbols of wisdom.
        "Deva": 8,                # Divine beings in Hindu mythology, often in conflict with Asuras.
        "Archon": 8,              # Beings of pure law and good, often in opposition to demons and devils.
        "": 1}

    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]


def Constructs():
    Names = {
        "Animated Armor": 8,         # Empty suits of armor brought to life, often as guardians.
        "Drone": 7,                  # Modern or futuristic unmanned devices, often for reconnaissance.
        "Golem": 9,                  # Beings made from inanimate material, like clay or stone. Classic magic constructs.
        "Homunculus": 7,             # Miniature, artificially created humanoids.
        "Flying Sword": 7,           # Enchanted weapons that move on their own.
        "Living Rug": 6,             # Animated carpets or rugs, often serving as traps.
        "Scarecrow": 7,              # Animated scarecrows, often created to protect crops but can be sinister.
        "Clockwork Construct": 8,   # Intricate mechanical beings, often steampunk-inspired.
        "Warforged": 9,              # Sentient constructs made for war, often searching for purpose after conflict.
        "Modron": 8,                 # Geometrically inspired beings from a plane of utter order.
        "Shield Guardian": 8,       # Created to protect its creator, often bound by an amulet.
        "Tome Guardian": 7,         # Animated books or beings made of paper, protecting knowledge.
        "Effigy": 8                  # Ritualistic statues or figures, animated for various purposes.
    }
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

def Dragons():
    DragonTypes = {
        "Dragonborn": 20,         # Dragon-like humanoids.
        "Wyrmling": 8,            # Baby dragons.
        "Young Dragon": 7,        # Adolescent dragons, coming into their power.
        "Adult Dragon": 6,        # Fully grown, mature dragons.
        "Elder Dragon": 5,        # Ancient and powerful.
        "Ancient Dragon": 4,      # Near mythical in their power and age.
        "Titan Dragon": 3,        # Immense size, power, and beyond-ancient origin.
        "Dragon Aspect": 1        # Manifestation of a dragon god or powerful entity.
    }

    DragonColors = {
        "Black": 8,               # Chromatic, acid breath.
        "Blue": 8,                # Chromatic, electric breath.
        "Green": 8,               # Chromatic, poison breath.
        "Red": 8,                 # Chromatic, fire breath.
        "White": 8,               # Chromatic, cold breath.
        "Bronze": 7,              # Metallic, good-aligned, lightning breath.
        "Silver": 7,              # Metallic, cold/paralyzing breath.
        "Gold": 7,                # Metallic, fire/weakening breath.
        "Brass": 7,               # Metallic, fire/sleep breath.
        "Copper": 7,              # Metallic, acid/slowing breath.
        "Shadow": 6,              # Tainted by Shadowfell, necrotic breath.
        "Gem": 6,                 # Rare, associated with gemstones and psionics.
        "Ethereal": 5,            # From the Ethereal Plane.
        "Planar": 5,              # Associated with specific planes.
        "Prismatic": 3            # Rare and extremely powerful, known for multi-colored, rainbow-like powers.
    }

    # Pick one from each category
    chosen_type = random.choices(list(DragonTypes.keys()), weights=DragonTypes.values(), k=1)[0]
    chosen_color = random.choices(list(DragonColors.keys()), weights=DragonColors.values(), k=1)[0]

    return f"{chosen_color} {chosen_type}"


def Elementals():
    Names = {
    "Atlantian": 8,      # Connection to water or ancient technology.
    "Cronusian": 4,      # Representing time and age.
    "Eosian": 7,         # Tied to the rising sun.
    "Genasi": 19,        # Representing air, earth, fire, and water.
    "Genie": 9,          # Powerful magical entities.
    "Gaians": 8,         # Essence of the earth.
    "Hyperian": 6,       # Radiant, solar-powered.
    "Oceanians": 8,      # Depths, tides, storms.
    "Primordial": 5,     # Fundamental forces of reality.
    "Promethean": 7,     # Fire or spirit of innovation.
    "Salamander": 9,     # Associated with fire.
    "Titan": 6,          # Raw elemental power.
    "Uranians": 7,       # Sky, stars, celestial magic.
    "Magmaforged": 8,    # Fusion of earth and fire.
    "Zephyrians": 8,     # Gentle airs.
    "Abyssal": 7,        # Dark ocean depths.
    "Theian": 7,         # Ether and the heavenly shine.
    "Criusian": 7,       # Elemental related to constellations and stars.
    "Coean": 5,          # Intellect, heavenly revolutions and gravity.
    "Tundran": 7         # Harsh icy landscapes.
    }
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]


def Fiends():
    Names = {
        "Tiefling": 20,
        "Devil": 10,
        "Demon": 10,
        "Imp": 8,
        "Incubus/Succubus": 7,  
        "Dwarvendevil": 3,
        "Elvendevil": 3,
        "Gnolldevil": 3,
        "Orkishdevil": 3,
        "Goblindevil": 3,
        "Dwarvendemon": 2,
        "Elvendemon": 2,
        "Demongnoll": 2,
        "Orkishdemon": 2,
        "Goblindemon": 2,
        "Nightmare": 5,
        "Rakshasa": 3,
        "Fallen Angel": 6,
        "Hellbound Hunter": 7,
        "Leviathan": 4,
        "Behemoth": 4,
        "Shinigami":2,
        "Hell's Rider": 7,
        "Soul Collector": 6,
        "Infernal Detective": 5,
        "Dread Enforcer": 5,
        "Sin Investigator": 4,
        "Infernal Warlord": 4,
        "Infernal Justiciar": 6,
        "Vengeance Spirit": 5,
        "Retributioner": 5,
        "Pact Enforcer": 6,
        "Soulclaimer": 6,
        "Infernal Marshal": 5
        }
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]


def Feys():
    Names = {
        "Dryad": 10,    # Tree spirits
        "Hag": 8,       # Witches often associated with dark magic
        "Nymph": 9,     # Spirits of nature: water, forest, etc.
        "Pixie": 8,     # Tiny, mischievous spirits
        "Satyr": 9,     # Half-man, half-goat
        "Sprite": 7,    # Airy spirits similar to pixies but usually less mischievous
        "High Fae": 6,  # Powerful fey lords and ladies
        "Redcap": 5,    # Malicious goblin-like creatures
        "Banshee": 5,   # Spirits heralding death
        "Leprechaun": 7,  # Mischievous little fey associated with pots of gold
        "Changeling": 5,  # Fey child left in place of a stolen human child
        "Nexus Fey": 6,       # Fey connected to a connection point
        "Duende": 5,          # Fey of the arts, beauty, and nature. Tricksters.
        "Home Lares": 4,      # Guardians of homes and families
        "Will-o'-the-wisp": 6,  # Ghostly lights that lure travelers away from paths
        "Fata": 5              # Fae that intervine in someone's fate
    }
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

def Giants():
    Names = {
        "Cyclops": 8,                # Greek one-eyed giants
        "Ogre": 10,                  # Brutish man-eaters
        "Troll": 9,                  # Norse mountain dwellers
        "Jotunn (Frost Giant)": 7,   # Norse primal giants
        "Fire Giant": 7,             # Inhabitants of Muspelheim
        "Gigantes": 6,               # Giants from Greek mythology
        "Nephilim": 5,               # Biblical giants
        "Oni": 7,                    # Japanese ogre-like giants
        "Ettin (Two headed)": 6,     # English two-headed giants
        "Fomorians (Sea Giants)": 5, # Irish sea giants
        "Goliath": 5,                # Biblical Philistine giant
        "Cloud Giant": 7,            # Noble sky dwellers
        "Stone Giant": 7,            # Earthy, rocky giants
        "Storm Giant": 6             # Majestic tempest giants
    }
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

def Gnomes():
    Names = {
        "Mountain": 8,
        "Forest": 8,
        "Garden": 1,
        "Tinker": 4,
        "Crossroad": 3,
        "Trickster": 3,
        "Wandering": 3
    }
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]


def Goblins():
    Names = {
        "Goblin": 15,                       # Mischievous green-skinned creatures
        "Hobgoblin": 8,                     # Disciplined, militant goblinoids
        "Bugbear": 7,                       # Stealthy brutes of the goblinoid family
        "Gremlin (Tecnogoblin)": 6,         # Saboteurs of machinery
        "Redcap": 5,                        # Bloodthirsty goblin-like fey
        "Nyk (Watergoblin)": 6,             # Slavic water-dwelling goblins
        "Trow (Dark goblin)": 5,            # Orcadian mischief-makers
        "Knocker (Underdark goblin)": 6,    # Cornish mine-dwelling creatures
        "Domovoi (House Goblin)": 5         # Slavic house spirits
    }
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]


def Monstrosities():
    Names = {
        "Basilisk": 7,        
        "Chimera": 8,         
        "Displacer Beast": 9,
        "Doppelganger": 8,    
        "Gorgon": 7,          
        "Griffon": 9,         
        "Harpy": 8,           
        "Horror": 6,          
        "Kerberus": 8,        
        "Lamia": 7,           
        "Manticore": 9,       
        "Yeti": 7,            
        "Worg": 8,
        "Wendigo": 3,
        "Kraken": 5,
        "Chupacabra":3,
        "Land Shark":3,
        "":1
    }
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]


def Oozes():
    Types = {
        "Blob": 8,      # Standard, amorphous entity.
        "Slime": 6,     # Slightly more fluidic, might move faster
        "Jelly": 7,     # More gelatinous and transparent
        "Pudding": 5,   # Thicker, more aggressive.
        "Goo": 4,       # Sticky and adhesive, might trap prey.
        "Mold": 3,      # Fungus-like, possibly releasing spores or gases.
        "Cube": 9       # Perfectly square, often large enough to engulf adventurers.
    }
    
    Properties = {
        "Gray": 7,
        "Ochre": 5,
        "Black": 6,
        "Magma": 4,
        "Crystal": 4,
        "Corrosive": 7,
        "Frost": 5,
        "Eldritch": 3,
        "Luminous": 6,
        "Toxic": 6
    }
    
    chosen_type = random.choices(list(Types.keys()), weights=Types.values(), k=1)[0]
    chosen_property = random.choices(list(Properties.keys()), weights=Properties.values(), k=1)[0]
    
    return f"{chosen_property} {chosen_type}"


def Orcs():
    Names = {
        "Mountain Orc": 5,
        "Desert Orc": 5,
        "Swamp Orc": 6,
        "Snow Orc": 4,
        "Uruk": 6,
        "Half-Orc": 7,
        "Orog (Underdark Orc)": 5,
        "Cave Orc": 6,
        "Forest Orc": 6,
        "Nomadic Orc": 7,
        "Island Orc": 6,
        "Urbanite Orc": 9,
        "Feral Orc": 7
        
    }
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

       
def Plants():
    Names = {
        "Willow Guardian": 7,
        "Treant": 9,
        "Awakened Tree": 9,
        "Forefather Oak": 7,
        "Myconid Sovereign": 8,
        "Ent": 9,
        "Treefolk": 7,
        "Floral Walkers": 7,
        "Living Totem": 7,
        "Walker Vine": 9,
        "Singing Lotus": 7,
        "Lichen Gravetaker": 7,
        "Cactoid Nomad": 6,
        "Vegetation Abomination":3,
        "Dryad":7
        
    }
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]


def Undeads():
    Names = {
            "Death Knight": 5,           # Elite undead warriors, remnants of former knights or warlords.
            "Honor Phantom": 7,          # Ethereal spirits bound by duty or a promise made in life.
            "Regret Ghost": 8,           # Souls trapped due to unfinished business or profound regrets.
            "Lich": 4,                   # Undying mages who sought eternal life through dark rituals.
            "Pride Mummy": 6,            # Preserved dead, animated to guard ancient tombs and relics.
            "Mischief Poltergeist": 7,   # Playful spirits, causing disturbances to attract attention.
            "Vengeful Revenant": 5,      # Resurrected by sheer force of will to enact revenge.
            "Skeleton Protector": 9,     # Animated skeletal guardians, defending locations or treasures.
            "Thinker Skull": 7,          # Knowledgeable remnants, often used by dark mages for counsel.
            "Fear Shadow": 7,            # Undead born from intense fear, lurking in darkness.
            "Despair Specter": 8,        # Souls that suffered tremendous despair, wishing the same for the living.
            "Vampire": 5,                # Bloodsucking undead, intelligent and driven by hunger and desire.
            "Prideful Wight": 6,         # Powerful undead often found leading other lesser undead.
            "Cursed Eternal": 7,         # Mindless undead, driven by a hunger for the living.
            "Wraith": 6,                 # Souls consumed by anger, seeking to draw others into death.
            "Lone Lover": 6,             # Animated by profound love or loss, searching for their beloved.
            "Weeping Howler": 5,         # Spirits that mourn and wail, often announcing death.
            "Tomb's Hoarder": 5,         # Guardians of burial sites, obsessed with their treasures.
            "Penance Wraith": 5,         # Souls seeking atonement for sins committed in life.
            "Protector Spirit": 7        # Benevolent spirits still guarding a place, object, or person.
        }
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

def Humans():
    Types = {
        "Local": 30,       
        "Foreigner": 20,    
        "Exotic": 10,       
        "Well dressed":10,
        "Humble":10,
        "Healty": 20,
        "Strong": 5,
        "Big": 6,
        "Thin": 4,
        "Athletic": 5,
        "Sickly": 5,
        "Pretty": 5,
        "Rough": 5,
        "Elegant": 5,
        "Old":5,
        "Young":5,
        "Attractive":5
        }
    
    chosen_type = random.choices(list(Types.keys()), weights=Types.values(), k=1)[0]
    
    return f"{chosen_type} "


def Elves():
    Types = {
        "High": 15,       
        "Sylvan": 15,    
        "Wood": 15,    
        "Dark": 15,
        "Night": 8,
        "Feywild": 5,       
        "Shadow": 5,       
        "Sea": 10,       
        "Nomadic": 10,       
        "Snow":5,
        "Sun": 3,
        "Eclipse":1,
        "Moon": 3,
        "Wild": 3,
        "Urban": 10,
        "Sands": 7
        }
    
    chosen_type = random.choices(list(Types.keys()), weights=Types.values(), k=1)[0]
    
    return f"{chosen_type} "

def Dwarfs():
    Types = {
        "Mountain": 20,
        "Conquistador": 10,        
        "Seawolf": 10,        
        "Tinkerer": 10,        
        "Roadbarter": 10,        
        "Urbanite": 12,        
        "Stonemason": 7,        
        "Dark":5,
        "Crystal Cavern": 3,
        "Canyon Dweller":5,
        "Bank Templar":5,
        "Forgeclan": 5
        }
    
    chosen_type = random.choices(list(Types.keys()), weights=Types.values(), k=1)[0]
    
    return f"{chosen_type} "

def Lizardfolks():
    Types = {
        "Swamp Crocfolk": 8,
        "Jungle Guanafolk": 7,
        "Desertic Horned": 5,
        "Dune Dino":4,
        "White Albino": 1,
        "Feathered Dinofolk":5,
        "Colored Chamalfolk":3,
        "Titan Rex": 3,
        "Tundra Saurius": 3
        }
    
    chosen_type = random.choices(list(Types.keys()), weights=Types.values(), k=1)[0]
    
    return f"{chosen_type} "

def Monster(Type):
    type_function_map = {
        "Aberration": Aberrations,
        "Aven": Avens,
        "Beast": Beasts,
        "Beastfolk": Beastfolks,
        "Celestial": Celestials,
        "Construct": Constructs,
        "Dragon": Dragons,
        "Elemental": Elementals,
        "Elf": Elves,
        "Fey": Feys,
        "Fiend": Fiends,
        "Giant": Giants,
        "Goblin": Goblins,
        "Human": Humans,
        "Lizardfolk":Lizardfolks,
        "Monstrosity": Monstrosities,
        "Orc": Orcs,
        "Ooze": Oozes,
        "Plant": Plants,
        "Undead": Undeads
    }

    if Type in type_function_map:
        return type_function_map[Type]()
    else:
        return f"Is an unknown type of {Type}!"


def Dice(D=6):
    """Rolls a dice with D sides. If D is 0, simulates a coin flip."""
    if D < 1: roll = random.randint(D, 1) 
    else: roll = random.randint(1, D)
    return roll

def Dice(D=6,N=1):
    roll = 0
    for m in range(N):
        if D >= 1: roll += random.randint(1, D)
        else: roll += random.randint(D, 1)
    return roll


def AbilityScore():
    d1 = Dice()
    d2 = Dice()
    d3 = Dice()
    d4 = Dice()
    return d1+d2+d3+d4 - min(d1, d2, d3, d4) 


#def Modifier(AS):
#    if AS >= 10:    return int((AS-10)/2)
#    else:           return int((AS-11)/2)

def Modifier(AS):
    return (AS - 10) // 2

def Proficiency(AS):
    return Dice(Modifier(AS)*2)

def PB(Lvl):
    if Lvl < 5:
        return 2
    else:
        return 2 + (Lvl - 1) // 4
    
def Attack(Type,PB = 2, STR =10,  DEX = 10 ):
    STR = Modifier(STR)
    DEX = Modifier(DEX)

    SimpleMeleeWeapons = [
        f"Rock, {Dice(PB-1)}d6 + {STR} Bludgeoning, 25/50 thrown",
        f"Fists, {Dice(PB-1)}d4 + {STR} Bludgeoning",
        f"Brass Knuckles, {Dice(PB-1)}d4 + {STR} Bludgeoning",
        f"Bite, {Dice(PB-1)}d4 + {STR} Piercing",
        f"Bite, {Dice(PB-1)}d6 + {STR} Piercing",
        f"Claws, {Dice(PB-1)}d4 + {STR} Slashing",
        f"Claws, {Dice(PB-1)}d6 + {STR} Slashing",
        f"Club, {Dice(PB-1)}d4 + {STR} Bludgeoning",
        f"Dagger, {Dice(PB-1)}d4 + {STR} Piercing, 20/60 thrown",
        f"Dagger, {Dice(PB-1)}d4 + {DEX} Piercing, 20/60 thrown",
        f"GreatClub, {Dice(PB-1)}d8 + {STR} Bludgeoning",
        f"Handaxe, {Dice(PB-1)}d6 + {STR} Slashing, 20/60 thrown",
        f"Javelin, {Dice(PB-1)}d6 + {STR} Piercing, 30/120 thrown",
        f"Light Hammer, {Dice(PB-1)}d4 + {STR} Bludgeoning, 20/60 thrown",
        f"Mace, {Dice(PB-1)}d6 + {STR} Bludgeoning",
        f"Quarterstaff, {Dice(PB-1)}d6 + {STR} Bludgeoning",
        f"Quarterstaff, {Dice(PB-1)}d8 + {STR} Bludgeoning",
        f"Sickle, {Dice(PB-1)}d4 + {STR} Slashing",
        f"Slam, {Dice(PB-1)}d8 + {STR} Bludgeoning",
        f"Spear, {Dice(PB-1)}d6 + {STR} Piercing, 20/60 thrown",
        f"Spear, {Dice(PB)+1}d8 + {STR} Piercing, 20/60 thrown",
        f"Nunchaku, {Dice(PB-1)}d6 + {STR} Bludgeoning"
        ]
    
    SimpleRangedWeapons = [
        f"Rock, {Dice(PB-1)}d6 + {STR} Bludgeoning, 25/50 thrown",
        f"Light Crossbow, {Dice(PB-1)}d8 + {DEX} Piercing, 80/320 range",
        f"Dart, {Dice(PB-1)}d4 + {DEX} Piercing, 20/60 range",
        f"Dart, {Dice(PB-1)}d4 + {STR} Piercing, 20/60 range",
        f"Shortbow, {Dice(PB-1)}d6 + {DEX} Piercing, 80/320 range",
        f"Sling, {Dice(PB-1)}d4 + {DEX} Bludgeoning, 30/120 range",
        f"Light Crossbow, {Dice(PB-1)}d8 + {DEX} Piercing, 80/320 range, loading, two handed"
        ]
    
    MartialMeleeWeapons = [
        f"Battleaxe, {Dice(PB-1)}d8 + {STR} Slashing",
        f"Battleaxe, {Dice(PB-1)}d10 + {STR} Slashing",
        f"Flail, {Dice(PB-1)}d8 + {STR} Bludgeoning",
        f"Glaive, {Dice(PB-1)}d10 + {STR} Bludgeoning, reach",
        f"Greataxe, {Dice(PB-1)}d12 + {STR} Slashing, reach",
        f"Greatsword, {Dice(PB)+1}d6 + {STR} Slashing",
        f"Halberd, {Dice(PB-1)}d10 + {STR} Slashing, reach",
        f"Lance, {Dice(PB-1)}d12 + {STR} Piercing, reach",
        f"Longsword, {Dice(PB-1)}d8 + {STR} Slashing",
        f"Longsword, {Dice(PB-1)}d10 + {STR} Slashing",
        f"Maul, {Dice(PB)+1}d6 + {STR} Bludgeoning",
        f"Morningstar, {Dice(PB-1)}d8 + {STR} Piercing",
        f"Pike, {Dice(PB-1)}d10 + {STR} Piercing, reach",
        f"Rapier, {Dice(PB-1)}d8 + {STR} Piercing, Finesse",
        f"Rapier, {Dice(PB-1)}d8 + {DEX} Piercing, Finesse",
        f"Scimitar, {Dice(PB-1)}d6 + {STR} Slashing, Finesse, light",
        f"Scimitar, {Dice(PB-1)}d6 + {DEX} Slashing, Finesse, light",
        f"Shortsword, {Dice(PB-1)}d6 + {STR} Slashing, Finesse, light",
        f"Shortsword, {Dice(PB-1)}d6 + {DEX} Slashing, Finesse, light",
        f"Trident, {Dice(PB-1)}d6 + {STR} Piercing, 20/60 thrown",
        f"Trident, {Dice(PB-1)}d8 + {STR} Piercing, 20/60 thrown",
        f"War pick, {Dice(PB-1)}d8 + {STR} Bludgeoning",
        f"Warhammer, {Dice(PB-1)}d8 + {STR} Bludgeoning",
        f"Warhammer, {Dice(PB-1)}d10 + {STR} Bludgeoning",
        f"Whip, {Dice(PB-1)}d4 + {STR} Slashing, Finesse, reach"
        f"Whip, {Dice(PB-1)}d4 + {DEX} Slashing, Finesse, reach"
        ]
    
    MartialRangedWeapons = [
        f"Blowgun, 1 piercing, 25/100 range, Ammunition, Loading",
        f"Hand Crossbow, {Dice(PB-1)}d6 + {DEX} piercing, 30/120 range, Ammunition, Light, Loading",
        f"Heavy Crossbow, {Dice(PB-1)}d10 + {DEX} piercing, 100/400 range, Ammunition, Heavy, Loading, Two-Handed",
        f"Longbow, {Dice(PB-1)}d8 + {DEX} piercing, 150/600 range, Ammunition, Heavy, Two-Handed",
        f"Net, Special, 5/15 range, Thrown",
        f"Throwing Axe, {Dice(PB-1)}d6 + {STR} slashing, 20/60 range, Thrown",
        f"Flintlock Pistol, {Dice(PB-1)}d8 + {DEX} piercing, 30/90 range, Loading, Jamming: On an attack roll of 1, the gun jams and requires an action to clear before it can be fired again.",
        f"Musket, {Dice(PB)+1}d10 + {DEX} piercing, 60/180 range, Loading, Jamming: On an attack roll of 1, the gun jams and requires an action to clear before it can be fired again.",
        f"Blunderbuss, {Dice(PB)+2}d10 + {DEX} fire, 10/30 range, Loading, Exploding: On an attack roll of 1, the gun explodes and requires a short rest fixing it before it can be fired again. You don't gain the benefits of that short rest."
        ]

    if Type == "Melee" or Type == 1:
        return random.choice(SimpleMeleeWeapons)
    elif Type == "Ranged" or Type == 2:
        return random.choice(SimpleRangedWeapons)
    elif Type == "Martial" or Type == "MartialMelee" or Type == 3:
        return random.choice(MartialMeleeWeapons)
    elif Type == "RangedMartial" or Type == 4:
        return random.choice(MartialRangedWeapons)
    else:
        return random.choice(Attack(random.choice(["Melee","Ranged","Martial","RangedMartial"]),STR,DEX))


def Damage():
    DamageTypes = [
        "Slashing",
        "Piercing",
        "Bludgeoning",
        "Poison",
        "Acid",
        "Fire",
        "Cold",
        "Radiant",
        "Necrotic",
        "Lightning",
        "Force",
        "Psychic",
        "Thunder",
        ""
    ]
    return random.choice(DamageTypes)


def Condition(dmg):
    ConditionsTypes = [
        "Blinded",
        "Charmed",
        "Deafened",
        "Exhaustion",
        "Frightened",
        "Grappled",
        "Incapacitated",
        "Invisible",
        "Paralyzed",
        "Petrified",
        "Poisoned",
        "Prone",
        "Restrained",
        "Stunned",
        "Unconscious",
        ""
    ]
    if dmg == "Slashing":       return random.choice(["Exhaustion", "Incapacitated", "Poisoned", "Prone"])
    elif dmg == "Piercing":     return random.choice(["Blinded", "Exhaustion", "Incapacitated", "Poisoned", "Grappled"])
    elif dmg == "Bludgeoning":  return random.choice(["Blinded", "Deafened", "Exhaustion", "Incapacitated", "Prone", "Stunned", "Uncoscious", "Grappled", "Restrained"])
    elif dmg == "Poison":       return random.choice(["Blinded", "Charmed", "Exhaustion", "Frightened", "Incapacitated", "Paralyzed", "Petrified", "Poisoned", "Restrained", "Unconscious"])
    elif dmg == "Acid":         return random.choice(["Blinded", "Exhaustion", "Incapacitated", "Paralyzed", "Petrified", "Poisoned", "Restrained", "Unconscious"])
    elif dmg == "Fire":         return random.choice(["Blinded", "Charmed", "Incapacitated", "Paralyzed", "Stunned", "Unconscious"])
    elif dmg == "Cold":         return random.choice(["Exhaustion", "Incapacitated", "Paralyzed", "Petrified", "Restrained", "Grappled"])
    elif dmg == "Radiant":      return random.choice(["Blinded", "Charmed", "Deafened", "Frightened", "Incapacitated", "Paralyzed", "Prone", "Stunned", "Unconscious"])
    elif dmg == "Necrotic":     return random.choice(["Exhaustion", "Frightened", "Incapacitated", "Paralyzed", "Poisoned", "Prone", "Restrained", "Stunned", "Unconscious"])
    elif dmg == "Lightning":    return random.choice(["Blinded", "Charmed", "Deafened", "Exhaustion", "Frightened", "Grappled", "Incapacitated", "Paralyzed", "Petrified", "Prone", "Restrained", "Stunned", "Unconscious"])
    elif dmg == "Force":        return random.choice(["Blinded", "Deafened", "Exhaustion", "Incapacitated", "Prone", "Stunned", "Unconscious", "Grappled"])
    elif dmg == "Psychic":      return random.choice(["Blinded", "Charmed", "Deafened", "Exhaustion", "Frightened", "Incapacitated", "Paralyzed", "Petrified", "Poisoned", "Prone", "Restrained", "Stunned", "Unconscious"])
    elif dmg == "Thunder":      return random.choice(["Blinded", "Deafened", "Exhaustion", "Incapacitated", "Paralyzed", "Prone", "Stunned"])
    else:                       return random.choice(ConditionsTypes)


def SavingThrow(dmg):
    if dmg == "Slashing":       st = random.choice(["STR", "DEX"])
    elif dmg == "Piercing":     st = random.choice(["STR", "DEX", "CON"])
    elif dmg == "Bludgeoning":  st = random.choice(["STR", "DEX", "CON"])
    elif dmg == "Poison":       st = "CON"
    elif dmg == "Acid":         st = random.choice(["STR", "DEX", "CON"])
    elif dmg == "Fire":         st = random.choice(["STR", "DEX", "CON", "CHA"])
    elif dmg == "Cold":         st = random.choice(["STR", "DEX", "CON"])
    elif dmg == "Radiant":      st = random.choice(["DEX", "CON", "WIS", "CHA"])
    elif dmg == "Necrotic":     st = random.choice(["STR", "CON", "WIS", "CHA"])
    elif dmg == "Lightning":    st = random.choice(["DEX", "CON", "WIS", "INT"])
    elif dmg == "Force":        st = random.choice(["STR", "CON", "CHA"])
    elif dmg == "Psychic":      st = random.choice(["INT", "WIS", "CHA"])
    elif dmg == "Thunder":      st = random.choice(["STR", "DEX", "CON"])
    else:                       st = "DEX"
    return st


def Recovery(con):
    if con == "Unconscious":    st = random.choice(["CON", "INT", "WIS", "CHA"])
    elif con == "Stunned":      st = random.choice(["CON", "INT", "WIS", "CHA"])
    elif con == "Restrained":   st = random.choice(["STR", "DEX", "CON"])
    elif con == "Poisoned":     st = random.choice(["CON", "WIS"])
    elif con == "Prone":        st = random.choice(["STR", "DEX", "CON"])
    elif con == "Petrified":    st = random.choice(["STR", "CON", "INT", "WIS", "CHA"])
    elif con == "Paralyzed":    st = random.choice(["STR", "CON", "WIS", "CHA"])
    elif con == "Invisible":    st = random.choice(["CON", "INT", "WIS", "CHA"])
    elif con == "Incapacitated":st = random.choice(["STR", "CON", "WIS", "CHA"])
    elif con == "Grappled":     st = random.choice(["STR", "DEX"])
    elif con == "Blinded":      st = random.choice(["CON", "INT", "WIS", "CHA"])
    elif con == "Frightened":   st = random.choice(["CON", "INT", "WIS", "CHA"])
    elif con == "Exhaustion":   st = random.choice(["STR", "CON", "CHA"])
    elif con == "Deafened":     st = random.choice(["STR", "CON", "WIS"])
    elif con == "Charmed":      st = random.choice(["CHA", "WIS"])
    else:                       st = "CON"
    return st


def SpecialAttack(Lvl, Mod, STR=0, DEX=0):
    dmg = Damage()
    con = Condition(dmg)
    r = ""

    # Basic attack description    
    r += Attack(Dice(4), STR = STR, DEX = DEX) + " +"

    # Damage calculation
    damage_die = random.choice(["d4", "d6", "d8", "d10", "d12"])
    r += "{}".format(Dice(PB(Lvl)//2) + Dice(2))
    r += damage_die + " "
    r += dmg
    r += " dmg"

    # Saving throw description    
    r += " on a failed Saving Throw at DC "
    r += str((10 + Mod)) + " "
    r += SavingThrow(dmg) + "."

    # Potential condition application 
    if Dice(10)+Dice(10) <= Dice(Lvl):
        r += " The target is then affected by the " + con + " condition. "
        r += " The Condition may be countered with a succesful " + \
            str((10 + Mod)) + " " + Recovery(con) + \
            " Saving Throw at the beggining of the target's turn."
    return r


def add_language(languages, language, chance=6):
    """Try to add a language based on a dice roll and chance."""
    if Dice(chance) == 1 and language not in languages:
        languages.append(language)


        
def Language(race=Race(), background=Background()):
    if race == "":
        race = Race()
    if background == "":
        background = Background()

    languages = [""]

    if race == "base":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            
    if race == "Human":
        langs = {
            "Dwarvish": 6,
            "Elvish": 6,
            "Giant": 6,
            "Gnomish": 6,
            "Goblin": 6,
            "Halfling": 6,
            "Orc": 6,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Aberration":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 10,
            "Gnomish": 20,
            "Goblin": 10,
            "Halfling": 20,
            "Orc": 10,
            "Abyssal": 8,
            "Celestial": 20,
            "Draconic": 10,
            "Deep Speech": 1,
            "Infernal": 10,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 6,
            "Telepathy (60 ft.) ": 6
            }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)      

    if race == "Aven":
        langs = {
            "Dwarvish": 10,
            "Elvish": 10,
            "Giant": 15,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 15,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 10,
            "Draconic": 10,
            "Deep Speech": 100,
            "Infernal": 100,
            "Primordial": 4,
            "Sylvan": 6,
            "Undercommon": 100
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Beast":
        langs = {
            "Beastly Speech":1,
            "Dwarvish": 20,
            "Elvish": 10,
            "Giant": 20,
            "Gnomish": 10,
            "Goblin": 10,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 10,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 10,
            "Sylvan": 2,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Beastfolk":
        langs = {
            "Beastly Speech":1,
            "Dwarvish": 20,
            "Elvish": 8,
            "Giant": 15,
            "Gnomish": 6,
            "Goblin": 6,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 10,
            "Celestial": 10,
            "Draconic": 10,
            "Deep Speech": 20,
            "Infernal": 10,
            "Primordial": 10,
            "Sylvan": 4,
            "Undercommon": 10
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            

    if race == "Celestial":
        langs = {
            "Dwarvish": 10,
            "Elvish": 8,
            "Giant": 10,
            "Gnomish": 10,
            "Goblin": 10,
            "Halfling": 10,
            "Orc": 10,
            "Abyssal": 8,
            "Celestial": 1,
            "Draconic": 10,
            "Deep Speech": 20,
            "Infernal": 8,
            "Primordial": 20,
            "Sylvan": 6,
            "Undercommon": 20,
            "All languages":8,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
   
        if Dice(2): add_language(l, "Telepathy. (60 feet).", 8) 
        else: add_language(languages, "Telepathy. (120 feet).", 10) 

    if race == "Construct":
        add_language(languages, "Understands the languages of its creator.", 1) 
        add_language(languages, "All languages.", 5) 

    if race == "Dragon":
        langs = {
            "Dwarvish": 8,
            "Elvish": 8,
            "Giant": 8,
            "Gnomish": 8,
            "Goblin": 8,
            "Halfling": 8,
            "Orc": 8,
            "Abyssal": 8,
            "Celestial": 8,
            "Draconic": 1,
            "Deep Speech": 10,
            "Infernal": 8,
            "Primordial": 10,
            "Sylvan": 4,
            "Undercommon": 10
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Dwarf":
        langs = {
            "Dwarvish": 1,
            "Elvish": 5,
            "Giant": 5,
            "Gnomish": 16,
            "Goblin": 16,
            "Halfling": 8,
            "Orc": 20,
            "Abyssal": 18,
            "Celestial": 16,
            "Draconic": 12,
            "Deep Speech": 3,
            "Infernal": 12,
            "Primordial": 12,
            "Sylvan": 20,
            "Undercommon": 4
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Elf":
        langs = {
            "Dwarvish": 6,
            "Elvish": 1,
            "Giant": 12,
            "Gnomish": 6,
            "Goblin": 18,
            "Halfling": 12,
            "Orc": 20,
            "Abyssal": 8,
            "Celestial": 8,
            "Draconic": 8,
            "Deep Speech": 16,
            "Infernal": 8,
            "Primordial": 6,
            "Sylvan": 4,
            "Undercommon": 6
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            
    if race == "Elemental":
        langs = {
            "Dwarvish": 8,
            "Elvish": 8,
            "Giant": 8,
            "Gnomish": 8,
            "Goblin": 18,
            "Halfling": 18,
            "Orc": 12,
            "Abyssal": 12,
            "Celestial": 12,
            "Draconic": 12,
            "Deep Speech": 20,
            "Infernal": 12,
            "Primordial": 1,
            "Sylvan": 4,
            "Undercommon": 10,
            "Ignan": 4,
            "Terran":4,
            "Aquan":4,
            "Auran":4
            
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if race == "Fey":
        langs = {
            "Dwarvish": 14,
            "Elvish": 3,
            "Giant": 10,
            "Gnomish": 8,
            "Goblin": 4,
            "Halfling": 16,
            "Orc": 16,
            "Abyssal": 16,
            "Celestial": 16,
            "Draconic": 8,
            "Deep Speech": 20,
            "Infernal": 16,
            "Primordial": 8,
            "Sylvan": 1,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Fiend":
        langs = {
            "Dwarvish": 4,
            "Elvish": 4,
            "Giant": 8,
            "Gnomish": 4,
            "Goblin": 2,
            "Halfling": 12,
            "Orc": 4,
            "Abyssal": 2,
            "Celestial": 20,
            "Draconic": 18,
            "Deep Speech": 20,
            "Infernal": 2,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 8,
            "Telepathy (60 ft.)": 10,
            "Telepathy (120 ft.)": 12            
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Giant":
        langs = {
            "Dwarvish": 4,
            "Elvish": 20,
            "Giant": 1,
            "Gnomish": 8,
            "Goblin": 8,
            "Halfling": 20,
            "Orc": 8,
            "Abyssal": 12,
            "Celestial": 12,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 12,
            "Primordial": 16,
            "Sylvan": 8,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Gnome":
        langs = {
            "Dwarvish": 3,
            "Elvish": 3,
            "Giant": 3,
            "Gnomish": 1,
            "Goblin": 6,
            "Halfling": 6,
            "Orc": 10,
            "Abyssal": 12,
            "Celestial": 12,
            "Draconic": 12,
            "Deep Speech": 12,
            "Infernal": 12,
            "Primordial": 12,
            "Sylvan": 4,
            "Undercommon": 12
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Goblin":
        langs = {
            "Dwarvish": 18,
            "Elvish": 16,
            "Giant": 10,
            "Gnomish": 18,
            "Goblin": 1,
            "Halfling": 18,
            "Orc": 4,
            "Abyssal": 10,
            "Celestial": 18,
            "Draconic": 6,
            "Deep Speech": 10,
            "Infernal": 10,
            "Primordial": 20,
            "Sylvan": 2,
            "Undercommon": 2
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Halfling":
        langs = {
            "Dwarvish": 4,
            "Elvish": 4,
            "Giant": 20,
            "Gnomish": 4,
            "Goblin": 20,
            "Halfling": 1,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 4,
            "Draconic": 6,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 18,
            "Sylvan": 18,
            "Undercommon": 20
            }
        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if race == "Kobold":
        langs = {
            "Dwarvish": 6,
            "Elvish": 18,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 8,
            "Halfling": 20,
            "Orc": 12,
            "Abyssal": 8,
            "Celestial": 10,
            "Draconic": 1,
            "Deep Speech": 8,
            "Infernal": 8,
            "Primordial": 20,
            "Sylvan": 16,
            "Undercommon": 6
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            
        
    if race == "Lizardfolk":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 10,
            "Gnomish": 20,
            "Goblin": 10,
            "Halfling": 20,
            "Orc": 4,
            "Abyssal": 4,
            "Celestial": 20,
            "Draconic": 1,
            "Deep Speech": 4,
            "Infernal": 4,
            "Primordial": 4,
            "Sylvan": 4,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Monstrosity":
        langs = {
            "Dwarvish": 8,
            "Elvish": 20,
            "Giant": 8,
            "Gnomish": 20,
            "Goblin": 10,
            "Halfling": 20,
            "Orc": 6,
            "Abyssal": 4,
            "Celestial": 20,
            "Draconic": 4,
            "Deep Speech": 1,
            "Infernal": 4,
            "Primordial": 10,
            "Sylvan": 8,
            "Undercommon": 1
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    
    if race == "Ooze":
        add_language(l, "Telepathy. ", 1)

    if race == "Orc":
        langs = {
            "Dwarvish": 10,
            "Elvish": 10,
            "Giant": 4,
            "Gnomish": 20,
            "Goblin": 2,
            "Halfling": 20,
            "Orc": 1,
            "Abyssal": 8,
            "Celestial": 8,
            "Draconic": 8,
            "Deep Speech": 20,
            "Infernal": 8,
            "Primordial": 8,
            "Sylvan": 8,
            "Undercommon": 8
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Plant":
        langs = {
            "Dwarvish": 20,
            "Elvish": 5,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 10,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 2,
            "Sylvan": 1,
            "Undercommon": 8,
            "Telepathy":4
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Snakefolk":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 2,
            "Celestial": 20,
            "Draconic": 1,
            "Deep Speech": 2,
            "Infernal": 10,
            "Primordial": 4,
            "Sylvan": 8,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
        
    if race == "Undead":
        langs = {
            "Dwarvish": 6,
            "Elvish": 6,
            "Giant": 6,
            "Gnomish": 6,
            "Goblin": 6,
            "Halfling": 6,
            "Orc": 6,
            "Abyssal": 2,
            "Celestial": 2,
            "Draconic": 6,
            "Deep Speech": 2,
            "Infernal": 2,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 4
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    # BACKGROUNDS
    if background == "base":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if background == "Druid":
        langs = {
            "Druidic":1,
            "Dwarvish": 20,
            "Elvish": 4,
            "Giant": 20,
            "Gnomish": 10,
            "Goblin": 10,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 16,
            "Draconic": 4,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 4,
            "Sylvan": 4,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    
    if background == "Bandit":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            

    if background == "Bard":
        langs = {
            "Dwarvish": 6,
            "Elvish": 6,
            "Giant": 20,
            "Gnomish": 6,
            "Goblin": 6,
            "Halfling": 6,
            "Orc": 6,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 6,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Berserker":
        langs = {
            "Dwarvish": 6,
            "Elvish": 20,
            "Giant": 6,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 6,
            "Abyssal": 12,
            "Celestial": 20,
            "Draconic": 16,
            "Deep Speech": 16,
            "Infernal": 12,
            "Primordial": 16,
            "Sylvan": 20,
            "Undercommon": 6
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            


    if background == "Charlatan":
        langs = {
            "Dwarvish": 6,
            "Elvish": 6,
            "Giant": 20,
            "Gnomish": 6,
            "Goblin": 6,
            "Halfling": 6,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Cultist":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 8,
            "Celestial": 8,
            "Draconic": 8,
            "Deep Speech": 8,
            "Infernal": 8,
            "Primordial": 8,
            "Sylvan": 20,
            "Undercommon": 8
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)



    if background == "Criminal":
        langs = {
            "Thieve's Cant":1,
            "Dwarvish": 12,
            "Elvish": 12,
            "Giant": 20,
            "Gnomish": 12,
            "Goblin": 12,
            "Halfling": 12,
            "Orc": 12,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 4
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Expert":
        langs = {
            "Dwarvish": 6,
            "Elvish": 6,
            "Giant": 6,
            "Gnomish": 6,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 6,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if background == "Explorer":
        langs = {
            "Dwarvish": 4,
            "Elvish": 4,
            "Giant": 4,
            "Gnomish": 4,
            "Goblin": 4,
            "Halfling": 4,
            "Orc": 4,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 4,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "base":
        langs = {
            "Dwarvish": 6,
            "Elvish": 6,
            "Giant": 20,
            "Gnomish": 6,
            "Goblin": 6,
            "Halfling": 6,
            "Orc": 6,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Healer":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 10,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 4,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 4,
            "Sylvan": 4,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Hero":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 6,
            "Draconic": 6,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 6,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Hunter":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 6,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 6,
            "Sylvan": 1,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Knight":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 6,
            "Draconic": 6,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 6,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Mage":
        langs = {
            "Dwarvish": 6,
            "Elvish": 6,
            "Giant": 6,
            "Gnomish": 6,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 6,
            "Celestial": 6,
            "Draconic": 6,
            "Deep Speech": 6,
            "Infernal": 6,
            "Primordial": 6,
            "Sylvan": 6,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Monk":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 6,
            "Draconic": 6,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 6,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)




    if background == "Noble":
        langs = {
            "Dwarvish": 6,
            "Elvish": 6,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 12,
            "Draconic": 12,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)



    if background == "Priest":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 6,
            "Celestial": 6,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 6,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)



    if background == "Pirate":
        langs = {
            "Thieve's Cant":1,
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 12,
            "Infernal": 20,
            "Primordial": 12,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Ranger":
        langs = {
            "Dwarvish": 20,
            "Elvish": 4,
            "Giant": 4,
            "Gnomish": 20,
            "Goblin": 4,
            "Halfling": 20,
            "Orc": 4,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 6,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 6,
            "Sylvan": 6,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Scholar":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 6,
            "Celestial": 6,
            "Draconic": 6,
            "Deep Speech": 6,
            "Infernal": 6,
            "Primordial": 6,
            "Sylvan": 6,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Shaman":
        langs = {
            "Druidic":1,
            "Dwarvish": 20,
            "Elvish": 6,
            "Giant": 6,
            "Gnomish": 20,
            "Goblin": 6,
            "Halfling": 20,
            "Orc": 6,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 8,
            "Sylvan": 1,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "base":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)



    if background == "Spy":
        langs = {
            "Thieve's Cant":1,
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            

    if background == "Traveler":
        langs = {
            "Dwarvish": 6,
            "Elvish": 6,
            "Giant": 6,
            "Gnomish": 6,
            "Goblin": 6,
            "Halfling": 6,
            "Orc": 6,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 12,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Urchin":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            

    if background == "Warrior":
        langs = {
            "Dwarvish": 6,
            "Elvish": 6,
            "Giant": 6,
            "Gnomish": 6,
            "Goblin": 6,
            "Halfling": 6,
            "Orc": 6,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            



    if background == "Warlock":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 6,
            "Celestial": 6,
            "Draconic": 6,
            "Deep Speech": 6,
            "Infernal": 6,
            "Primordial": 6,
            "Sylvan": 6,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            


    if background == "Witch":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 12,
            "Gnomish": 20,
            "Goblin": 6,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 6,
            "Celestial": 6,
            "Draconic": 6,
            "Deep Speech": 6,
            "Infernal": 6,
            "Primordial": 6,
            "Sylvan": 12,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            
    return "Common" + ", ".join(languages)



def Magic(Lvl, race=Race(), background=Background()):



    cantrip = "Cantrips (at will): "
    first   = "1st Level Spells: "
    second  = "2nd Level Spells: "
    third   = "3rd Level Spells: "
    fourth  = "4th Level Spells: "
    fifth   = "5th Level Spells: "
    sixth   = "6th Level Spells: "
    seventh = "7th Level Spells: "
    eigth   = "8th Level Spells: "
    ninth   = "9th Level Spells: "


    slots1 = 0
    slots2 = 0
    slots3 = 0
    slots4 = 0
    slots5 = 0
    slots6 = 0
    slots7 = 0
    slots8 = 0
    slots9 = 0

    one     = "1/Day each: "
    two     = "2/Day each: "
    three   = "3/Day each: "


# BACKGROUNDS:
    # Bandit
    # Bard
    # Berserker
    # Charlatan
    # Commoner
    # Cultist

    if background == "Cultist":

        if Dice(0) < Dice(Lvl) and not ("Light" in cantrip):            cantrip += "\n- Light."
        if Dice(0) < Dice(Lvl) and not ("Sacred Flame" in cantrip):     cantrip += "\n- Sacred Flame"
        if Dice(0) < Dice(Lvl) and not ("Thaumaturgy" in cantrip):      cantrip += "\n- Thaumaturgy"


    if background == "Cultist":
        if Dice(2) < Dice(Lvl) and not ("Command" in first):
            first += "\n- Command"
            slots1 += Dice()
        if Dice(2) < Dice(Lvl) and not ("Inflict Wounds" in first):
            first += "\n- Inflict Wounds"
            slots1 += Dice()
        if Dice(2) < Dice(Lvl) and not ("Shield Of Faith" in first):
            first += "\n- Shield Of Faith"
            slots1 += Dice()
                

    if background == "Cultist":
        if Dice(5) < Dice(Lvl) and not ("Hold Person" in second):
            second += "\n- Hold Person"
            slots2 += Dice(5)
        if Dice(5) < Dice(Lvl) and not ("Spiritual Weapon" in second):
            second += "\n- Spiritual Weapon"
            slots2 += Dice(5)

    # Criminal
    # Druid


    if background == "Druid" and not ("Druidcraft" in cantrip):                     cantrip += "\n- Druidcraft."

    if background == "Druid" and Dice(0) < Dice(Lvl) and not ("Produce Flame" in cantrip):  cantrip += "\n- Produce Flame."
    if background == "Druid" and Dice(0) < Dice(Lvl) and not ("Shillelagh" in cantrip):     cantrip += "\n- Shillelagh."
    if background == "Druid" and Dice(2) < Dice(Lvl) and not ("Entangle" in first):
        first += "\n- Entangle"
        slots1 += Dice()
    if background == "Druid" and Dice(2) < Dice(Lvl) and not ("Longstrider" in first):
        first += "\n- Longstrider"
        slots1 += Dice()
    if background == "Druid" and Dice(2) < Dice(Lvl) and not ("Thunderwave" in first):
        first += "\n- Thunderwave"
        slots1 += Dice()
    if background == "Druid" and Dice(5) < Dice(Lvl) and not ("Animal Messenger" in second):
        second += "\n- Animal Messenger"
        slots2 += Dice(5)
    if background == "Druid" and Dice(5) < Dice(Lvl) and not ("Barkskin" in second):
        second += "\n- Barkskin"
        slots2 += Dice(5)
    if background == "Druid" and Dice(5) < Dice(Lvl) and not ("Speak With Animals" in first):
        first += "\n- Speak With Animals"
        slots1 += Dice()

    # Expert
    # Explorer
    # Gladiator
    # Guard
    # Healer

    if background == "Healer" and Dice(0) < Dice(Lvl) and not ("Guidance" in cantrip):            cantrip += "\n- Guidance"
    if background == "Healer" and Dice(0) < Dice(Lvl) and not ("Sacred Flame" in cantrip):        cantrip += "\n- Sacred Flame"
    if background == "Healer" and Dice(2) < Dice(Lvl) and not ("Cure Wounds" in first):
        first += "\n- Cure Wounds"
        slots1 += Dice()


    # Hermit
    # Hero
    # Hunter
    # Knight

    if background == "Knight" and Dice(6) < Dice(Lvl) and not ("Guidance" in cantrip):            cantrip += "\n- Guidance"
    if background == "Knight" and Dice(6) < Dice(Lvl) and not ("Leadership" in cantrip):          cantrip += "\n- Leadership (Recharges after a Short or Long Rest). \n\t For 1 minute, the knight can utter a special command or warning whenever a nonhostile creature that it can see within 30 feet of it makes an attack roll or a saving throw. The creature can add a d4 to its roll provided it can hear and understand the knight. A creature can benefit from only one Leadership die at a time. This effect ends if the knight is incapacitated."


    # Mage

    if background == "Mage" and Dice(0) < Dice(Lvl) and not ("Firebolt" in cantrip):       cantrip += "\n - Firebolt"
    if background == "Mage" and Dice(0) < Dice(Lvl) and not ("Light" in cantrip):          cantrip += "\n - Light"
    if background == "Mage" and Dice(3) < Dice(Lvl) and not ("Sleep" in first):
        first += "\n - Sleep"
        slots1 += Dice(6)

    # Monk

    if background == "Monk" and Dice(0) < Dice(Lvl) and not ("Mage Hand" in cantrip):          cantrip += "\n- Mage Hand"
    if background == "Monk" and Dice(10) < Dice(Lvl) and not ("Feather Fall" in three):         three += "\n- Feather Fall"
    if background == "Monk" and Dice(10) < Dice(Lvl) and not ("Jump" in three):                 three += "\n- Jump"
    if background == "Monk" and Dice(10) < Dice(Lvl) and not ("See Invisibility" in three):     three += "\n- See Invisibility"
    if background == "Monk" and Dice(10) < Dice(Lvl) and not ("Shield" in three):               three += "\n- Shield"
    if background == "Monk" and Dice(20) < Dice(Lvl) and not ("Misty Step" in three):           three += "\n- Misty Step"
    if background == "Monk" and Dice(20) < Dice(Lvl) and not ("Nondetection" in three):         three += "\n- Nondetection, self Only."

    # Noble
    # Priest

    if background == "Priest" and Dice(0) < Dice(Lvl) and not ("Light" in cantrip):            cantrip += "\n- Light. "
    if background == "Priest" and Dice(0) < Dice(Lvl) and not ("Sacred Flame" in cantrip):     cantrip += "\n- Sacred Flame. "
    if background == "Priest" and Dice(0) < Dice(Lvl) and not ("Thaumaturgy" in cantrip):      cantrip += "\n- Thaumaturgy"
    if background == "Priest" and Dice(2) < Dice(Lvl) and not ("Guidance" in cantrip):          cantrip += "\n- Guidance"
    if background == "Priest" and Dice(2) < Dice(Lvl) and not ("Resistance" in cantrip):        cantrip += "\n- Resistance"


    if background == "Priest" and Dice(6) < Dice(Lvl) and not ("Bless" in first):
        first += "\n- Bless"
        slots1 += Dice()
    if background == "Priest" and Dice(6) < Dice(Lvl) and not ("Cure Wounds" in first):
        first += "\n- Cure Wounds"
        slots1 += Dice()
    if background == "Priest" and Dice(6) < Dice(Lvl) and not ("Sanctuary" in first):
        first += "\n- Sanctuary"
        slots1 += Dice()
    if background == "Priest" and Dice(6) < Dice(Lvl) and not ("Cure Wounds" in first):
        first += "\n- Cure Wounds"
        slots1 += Dice()
    if background == "Priest" and Dice(6) < Dice(Lvl) and not ("Guiding Bolt" in first):
        first += "\n- Guiding Bolt"
        slots1 += Dice()
    if background == "Priest" and Dice(6) < Dice(Lvl) and not ("Sanctuary" in first):
        first += "\n- Sanctuary"
        slots1 += Dice()
    if background == "Priest" and Dice(6) < Dice(Lvl) and not ("Command" in first):
        first += "\n- Command"
        slots1 += Dice()
    if background == "Priest" and Dice(6) < Dice(Lvl) and not ("Guiding Bolt" in first):
        first += "\n- Guiding Bolt"
        slots1 += Dice()
    if background == "Priest" and Dice(6) < Dice(Lvl) and not ("Cure Wounds" in first):
        first += "\n- Cure Wounds"
        slots1 += Dice()
    if background == "Priest" and Dice(6) < Dice(Lvl) and not ("Detect Magic" in first):
        first += "\n- Detect Magic"
        slots1 += Dice()

            

    if background == "Priest" and Dice() == 1 and not ("Lesser Restoration" in second):
        second += "\n- Lesser Restoration"
        slots2 += Dice(5)
    if background == "Priest" and Dice() == 1 and not ("Augury" in second):
        second += "\n- Augury"
        slots2 += Dice(5)
    if background == "Priest" and Dice() == 1 and not ("Spiritual Weapon" in second):
        second += "\n- Spiritual Weapon"
        slots2 += Dice(5)
    if background == "Priest" and Dice() == 1 and not ("Lesser Restoration" in second):
        second += "\n- Lesser Restoration"
        slots2 += Dice(5)
    if background == "Priest" and Dice() == 1 and not ("Hold Person" in second):
        second += "\n- Hold Person"
        slots2 += Dice(5)


    if background == "Priest" and Dice() == 1 and not ("Dispel Magic" in third):
        third += "\n- Dispel Magic"
        slots3 += Dice(4)
    if background == "Priest" and Dice() == 1 and not ("Spirit Guardians" in third):
        third += "\n- Spirit Guardians"
        slots3 += Dice(4)
    if background == "Priest" and Dice() == 1 and not ("Mass Healing Word" in third):
        third += "\n- Mass Healing Word"
        slots3 += Dice(4)
    if background == "Priest" and Dice() == 1 and not ("Tongues" in third):
        third += "\n- Tongues"
        slots3 += Dice(4)

    # Pirate
    # Ranger
    
    # Scholar
    # Shaman

    if background == "Shaman" and Dice() == 1 and not ("Druidcraft" in cantrip):        cantrip += "\n- Druidcraft"
    if background == "Shaman" and Dice() == 1 and not ("Produce Flame" in cantrip):     cantrip += "\n-  Produce Flame"
    if background == "Shaman" and Dice() == 1 and not ("Thorn Whip" in cantrip):        cantrip += "\n-  Thorn Whip"
    if background == "Shaman" and Dice() == 1 and not ("Entangle" in first):
        first += "\n- Entangle"
        slots1 += Dice()
    if background == "Shaman" and Dice() == 1 and not ("Fog Cloud" in first):
        first += "\n- Fog Cloud"
        slots1 += Dice()
    if background == "Shaman" and Dice() == 1 and not ("Bane" in first):
        first += "\n- Bane"
        slots1 += Dice()
    if background == "Shaman" and Dice() == 1 and not ("Shield Of Faith" in first):
        first += "\n- Shield Of Faith"
        slots1 += Dice()
    if background == "Shaman" and Dice(2) == 1 and not ("Heat Metal" in second):
        second += "\n- Heat Metal"
        slots2 += Dice(5)
    if background == "Shaman" and Dice(2) == 1 and not ("Spike Growth" in second):
        second += "\n- Spike Growth"
        slots2 += Dice(5)
    if background == "Shaman" and Dice() == 1 and not ("Conjure Animals" in third):
        third += "\n- Conjure Animals"
        slots3 += Dice(4)
    if background == "Shaman" and Dice() == 1 and not ("Plant Growth" in third):
        third += "\n- Plant Growth"
        slots3 += Dice(4)
    # Soldier
    # Spy
    # Traveler
    # Urchin
    # Warrior
    
    # Warlock
    if background == "Warlock" and Dice() == 1 and not ("Poison Spray" in cantrip):
        cantrip += "\n- Poison Spray"
            
    if background == "Warlock" and Dice() == 1 and not ("Thaumaturgy" in cantrip):
        cantrip += "\n- Thaumaturgy"

    if background == "Warlock" and Dice() == 1 and not ("Magic Missile" in first):
        first += "\n- Magic Missile"
        slots1 += Dice()

    if background == "Warlock" and Dice() == 1 and not ("Shield" in first):
        first += "\n- Shield"
        slots1 += Dice()

    if background == "Warlock" and Dice() == 1 and not ("Bane" in first):
        first += "\n- Bane"
        slots1 += Dice()

    if background == "Warlock" and Dice() == 1 and not ("Detect Magic" in first):
        first += "\n- Detect Magic"
        slots1 += Dice()
            
    if background == "Warlock" and Dice() == 1 and not ("Sanctuary" in first):
        first += "\n- Sanctuary"
        slots1 += Dice()


    if background == "Warlock" and Dice() == 1 and not ("Blur" in second):
        second += "\n- Blur"
        slots2 += Dice(5)

    if background == "Warlock" and Dice() == 1 and not ("Hold Person" in second):
        second += "\n- Hold Person"
        slots2 += Dice(5)

    if background == "Warlock" and Dice() == 1 and not ("Flaming Sphere" in second):
        second += "\n- Flaming Sphere"
        slots2 += Dice(5)

    if background == "Warlock" and Dice() == 1 and not ("Silence" in second):
        second += "\n- Silence"
        slots2 += Dice(5)
            
    if background == "Warlock" and Dice() == 1 and not ("Fireball" in third):
        third += "\n- Fireball"
        slots3 += Dice(4)

    if background == "Warlock" and Dice() == 1 and not ("Clairvoyance" in third):
        third += "\n- Clairvoyance"
        slots3 += Dice(4)

    if background == "Warlock" and Dice() == 1 and not ("Dispel Magic" in third):
        third += "\n- Dispel Magic"
        slots3 += Dice(4)

    if background == "Warlock" and Dice() == 1 and not ("Divination" in third):
        fourth += "\n- Divination"
        slots4 += Dice(3)

    if background == "Warlock" and Dice() == 1 and not ("Freedom Of Movement" in third):
        fourth += "\n- Freedom Of Movement"
        slots4 += Dice(3)

        # Witch
    if background == "Witch" and Dice() == 1 and not ("Identify" in first):
        first += "\n- Identify"
        slots1 += Dice()
    if background == "Witch" and Dice() == 1 and not ("Ray Of Sickness" in first):
        first += "\n- Ray Of Sickness"
        slots1 += Dice()
    if background == "Witch" and Dice(7) == 1 and not ("Hold Person" in second):
        second += "\n- Hold Person"
        slots2 += Dice(5)
    if background == "Witch" and Dice(7) == 1 and not ("Locate Object" in second):
        second += "\n- Locate Object"
        slots2 += Dice(5)
    if background == "Witch" and Dice(8) == 1 and not ("Bestow Curse" in third):
        third += "\n- Bestow Curse"
        slots3 += Dice(4)
    if background == "Witch" and Dice(8) == 1 and not ("Counterspell" in third):
        third += "\n- Counterspell"
        slots3 += Dice(4)
    if background == "Witch" and Dice(8) == 1 and not ("Lightning Bolt" in third):
        third += "\n- Lightning Bolt"
        slots3 += Dice(4)
    if background == "Witch" and Dice(9) == 1 and not ("Phantasmall Killer" in fourth):
        fourth += "\n- Phantasmall Killer"
        slots4 += Dice(3)
    if background == "Witch" and Dice(9) == 1 and not ("Polymorph" in fourth):
        fourth += "\n- Polymorph"
        slots4 += Dice(3)
    if background == "Witch" and Dice(10) == 1 and not ("Contact Other Plane" in fifth):
        fifth += "\n- Contact Other Plane"
        slots5 += Dice(2)
    if background == "Witch" and Dice(10) == 1 and not ("Scrying" in fifth):
        fifth += "\n- Scrying"
        slots5 += Dice(2)
    if background == "Witch" and Dice(11) == 1 and not ("Eyebite" in sixth):
        sixth += "\n- Eyebite"
        slots6 += 1

## RACES

        # ABERRATION.
    if race == "Aberration" and Dice() == 1 and not ("Create Food and Water" in cantrip):   cantrip += "\n- Create Food and Water. \n\t The monstrosity magically creates enough food and water to sustain itself for 24 hours."
    if race == "Aberration" and Dice() == 1 and not ("Rotting Gaze" in cantrip):            cantrip += "\n- Rotting Gaze. \n\t The aberration targets one creature it can see within 30 feet of it. The target must succeed on a DC 10+%CON Constitution saving throw against this magic or take 10 (3d6) necrotic damage."
    if race == "Aberration" and Dice(7) == 1 and not ("Weird Insight" in cantrip):          cantrip += "\n- Weird Insight. \n\t The aberration targets one creature it can see within 30 feet of it. The target must contest its Charisma (Deception) check against the aberration's Wisdom (Insight) check. If the aberration wins, it magically learns one fact or secret about the target. The target automatically wins if it is immune to being charmed."
    if race == "Aberration" and Dice() == 1 and not ("Confusion Ray" in cantrip):           cantrip += "\n- Confusion Ray. \n\t The target must succeed on a DC 13 Wisdom saving throw, or it can't take reactions until the end of its next turn. On its turn, the target can't move, and it uses its action to make a melee or ranged attack against a randomly determined creature within range. If the target can't attack, it does nothing on its turn."
    if race == "Aberration" and Dice(7) == 1 and not ("Paralyzing Ray" in cantrip):         cantrip += "\n- Paralyzing Ray. \n\t The target must succeed on a DC 13 Constitution saving throw or be paralyzed for 1 minute. The target can repeat the saving throw at the start of each of its turns, ending the effect on itself on a success."
    if race == "Aberration" and Dice() == 1 and not ("Fear Ray" in cantrip):                cantrip += "\n- Fear Ray. \n\t The target must succeed on a DC 13 Wisdom saving throw or be frightened for 1 minute. The target can repeat the saving throw at the end of each of its turns, with disadvantage if the monstrosity is visible to the target, ending the effect on itself on a success."
    if race == "Aberration" and Dice() == 1 and not ("Wounding Ray" in cantrip):            cantrip += "\n- Wounding Ray. \n\t The target must make a DC 13 Constitution saving throw, taking 16 (3d10) necrotic damage on a failed save, or half as much damage on a successful one."
    if race == "Aberration" and Dice(7) == 1 and not ("Stench Spray" in one):       one += "\n- Stench Spray (1/Day). \n\t Each creature in a 15-foot cone originating from the Aberration must succeed on a DC 10 Dexterity saving throw or be coated in a foul-smelling liquid. A coated creature exudes a horrible stench for 1d4 hours. The coated creature is poisoned as long as the stench lasts, and other creatures are poisoned while with in 5 feet of the coated creature. A creature can remove the stench on itself by using a short rest to bathe in water, alcohol, or vinegar."

        # AVEN
    if race == "Aven" and Dice(8) == 1 and not ("Summon Air Elemental" in cantrip):     cantrip += "\n- Summon Air Elemental. \n\t Five Aven within 30 feet of each other can magically summon an air elemental. Each of the five must use its action and movement on three consecutive turns to perform an aerial dance and must maintain concentration while doing so (as if concentrating on a spell). When all five have finished their third turn of the dance, the elemental appears in an unoccupied space within 60 feet of them. It is friendly toward them and obeys their spoken commands. It remains for 1 hour, until it or all its summoners die, or until any of its summoners dismisses it as a bonus action. A summoner can't perform the dance again until it finishes a short rest. When the elemental returns to the Elemental Plane of Air, any Aven within 5 feet of it can return with it."

    # BEASTS AND BEASTFOLK
    if race == "Beast" and Dice() == 1 and not ("Cold Breath" in cantrip):      cantrip += "\n- Cold Breath. \t (Recharge 5–6). \n\t The beast exhales a blast of freezing wind in a 15-foot cone. Each creature in that area must make a DC [10+%CON] Dexterity saving throw, taking 18 (4d8) cold damage on a failed save, or half as much damage on a successful one."

    if race == "Beastfolk" and Dice(10) == 1 and not ("Sleep Gaze" in cantrip):     cantrip += "\n- Sleep Gaze. \n\t The Beastfolk gazes at one creature it can see within 30 feet of it. The target must make a DC [10+%Wis] Wisdom saving throw. On a failed save, the target succumbs to a magical slumber, falling unconscious for 10 minutes or until someone uses an action to shake the target awake. A creature that successfully saves against the effect is immune to this Beastfolk's gaze for the next 24 hours. Undead and creatures immune to being charmed aren't affected by it."
    if race == "Beastfolk" and Dice(10) == 1 and not ("Sacred Flame" in cantrip):   cantrip += "\n- Sacred Flame."
    if race == "Beastfolk" and Dice() == 1 and not ("Mage Hand" in cantrip):        cantrip += "\n- Mage Hand (invisible)."
    if race == "Beastfolk" and Dice() == 1 and not ("Thaumaturgy" in cantrip):      cantrip += "\n- Thaumaturgy."
    if race == "Beastfolk" and Dice() == 1 and not ("Feather Fall" in cantrip):     cantrip += "\n- Feather Fall."
    if race == "Beastfolk" and Dice() == 1 and not ("Dancing Lights" in cantrip):   cantrip += "\n- Dancing Lights."
    if race == "Beastfolk" and Dice() == 1 and not ("Poison Spray" in cantrip):     cantrip += "\n- Poison Spray."

    if race == "Beastfolk" and Dice() == 1 and not ("Invisibility" in one):     one += "\n- Invisibility (self only)."
    if race == "Beastfolk" and Dice() == 1 and not ("Cure Wounds" in one):      one += "\n- Cure Wounds."
    if race == "Beastfolk" and Dice() == 1 and not ("Enlarge/Reduce" in one):   one += "\n- Enlarge/Reduce."
    if race == "Beastfolk" and Dice() == 1 and not ("Heat Metal" in one):       one += "\n- Heat Metal."
    if race == "Beastfolk" and Dice() == 1 and not ("Mirror Image" in one):     one += "\n- Mirror Image."
    if race == "Beastfolk" and Dice() == 1 and not ("Darkness" in one):         one += "\n- Darkness."
    if race == "Beastfolk" and Dice() == 1 and not ("Faerie Fire" in one):      one += "\n- Faerie Fire."

    if race == "Beastfolk" and Dice() == 1 and not ("Blur" in two):             two += "\n- Blur."
    if race == "Beastfolk" and Dice() == 1 and not ("Magic Weapon" in two):     two += "\n- Magic Weapon."


    
    # CELESTIALS.
    ## Cantrips and At Will magic
    if race == "Celestial" and Dice() == 1 and not ("Light" in cantrip):                cantrip += "\n- Light"
    if race == "Celestial" and Dice() == 1 and not ("Sacred Flame" in cantrip):         cantrip += "\n- Sacred Flame"
    if race == "Celestial" and Dice() == 1 and not ("Thaumaturgy" in cantrip):          cantrip += "\n- Thaumaturgy"
    if race == "Celestial" and Dice() == 1 and not ("Detect Evil And Good" in cantrip): cantrip += "\n- Detect Evil And Good"
    if race == "Celestial" and Dice() == 1 and not ("Detect Magic" in cantrip):         cantrip += "\n- Detect Magic."
    if race == "Celestial" and Dice() == 1 and not ("Detect Thoughts" in cantrip):      cantrip += "\n- Detect Thoughts."
    if race == "Celestial" and Dice() == 1 and not ("Druidcraft" in cantrip):           cantrip += "\n- Druidcraft."
    if race == "Celestial" and Dice() == 1 and not ("Pass Without Trace" in cantrip):   cantrip += "\n- Pass Without Trace."
        

        ## Three times a Day
    if race == "Celestial" and Dice() == 1 and not ("Bless" in three):                  three += "\n- Bless"
    if race == "Celestial" and Dice() == 1 and not ("Cure Wounds" in three):            three += "\n- Cure Wounds"
    if race == "Celestial" and Dice() == 1 and not ("Create Food And Water" in three):  three += "\n- Create Food And Water"
    if race == "Celestial" and Dice() == 1 and not ("Lesser Restoration" in three):     three += "\n- Lesser Restoration"
    if race == "Celestial" and Dice() == 1 and not ("Protection From Poison" in three): three += "\n- Protection From Poison"
    if race == "Celestial" and Dice() == 1 and not ("Sanctuary" in three):              three += "\n- Sanctuary"
    if race == "Celestial" and Dice() == 1 and not ("Shield" in three):                 three += "\n- Shield"
    if race == "Celestial" and Dice() == 1 and not ("Healing Touch" in three):          three += "\n- Healing Touch \n\t The celestial touches another creature. The target magically regains 10 (2d8 + %CON) hit points. In addition, the touch removes all diseases and neutralizes all poisons afflicting the target."

        ## One time a Day
    if race == "Celestial" and Dice() == 1 and not ("Dream" in one):                    one += "\n- Dream"
    if race == "Celestial" and Dice() == 1 and not ("Greater Restoration" in one):      one += "\n- Greater Restoration"
    if race == "Celestial" and Dice() == 1 and not ("Scrying" in one):                  one += "\n- Scrying"
    if race == "Celestial" and Dice() == 1 and not ("Calm Emotions" in one):            one += "\n- Calm Emotions"
    if race == "Celestial" and Dice() == 1 and not ("Dispel Evil And Good" in one):     one += "\n- Dispel Evil And Good"
    if race == "Celestial" and Dice() == 1 and not ("Entangle" in one):                 one += "\n- Entangle"
    if race == "Celestial" and Dice() == 1 and not ("Teleport" in one):                 one += "\n- Teleport \n\t The celestial magically teleports itself and up to three willing creatures it can see within 5 feet of it, along with any equipment they are wearing or carrying, to a location the celestial is familiar with, up to 1 mile away."

    # CONSTRUCTS.
    if race == "Construct" and Dice(2) == 1 and not ("Light" in cantrip):           cantrip += "\n- Light"
    if race == "Construct" and Dice(2) == 1 and not ("Paralysis Gas" in cantrip):   cantrip += "\n- Paralysis Gas (Recharge 5–6). \n\t The construct exhales a 30-foot cone of gas. Each creature in that area must succeed on a DC 10+%CON Constitution saving throw or be paralyzed for 1 minute. A creature can repeat the saving throw at the start of each of its turns, ending the effect on itself on a success."

    # DRAGONS.

    #Breath weapons
    if race == "Dragon" and Dice(3) == 1:
        d = 20
        if Dice(d) == 1 and not (" Fire Breath" in cantrip):        cantrip += "\n  - Fire Breath \n\t(Recharge 5-6) The dragon exhales fire in a 20-foot line that is 5 feet wide. Each creature in that line must make a DC [10+%Con] Dexterity saving throw, taking 14 (4d6) fire damage on a failed save, or half as much damage on a successful one."
        elif Dice(d) == 1 and not ("Fire Breath" in cantrip):       cantrip += "\n  - Fire Breath \n\t(Recharge 5-6) The dragon exhales fire in a 15-foot cone. Each creature in that area must make a DC [10+%Con] Dexterity saving throw, taking 22 (4d10) fire damage on a failed save, or half as much damage on a successful one."
        elif Dice(d) == 1 and not ("Fire Breath" in cantrip):       cantrip += "\n  - Fire Breath \n\t(Recharge 5-6) The dragon exhales fire in a 15-foot cone. Each creature in that area must make a DC [10+%Con] Dexterity saving throw, taking 24 (7d6) fire damage on a failed save, or half as much damage on a successful one."
        if Dice(d) == 2 and not ("Sleep Breath" in cantrip):        cantrip += "\n  - Sleep Breath \n\t(Recharge 5-6) The dragon exhales sleep gas in a 15-foot cone. Each creature in that area must succeed on a DC [10+%Con] Constitution saving throw or fall unconscious for 1 minute. This effect ends for a creature if the creature takes damage or someone uses an action to wake it."
        if Dice(d) == 3 and not ("Acid Breath" in cantrip):         cantrip += "\n  - Acid Breath \n\t(Recharge 5-6) The dragon exhales acid in a 20-foot line that is 5 feet wide. Each creature in that line must make a DC [10+%Con] Dexterity saving throw, taking 18 (4d8) acid damage on a failed save, or half as much damage on a successful one"
        if Dice(d) == 4 and not ("Slowing Breath" in cantrip):      cantrip += "\n  - Slowing Breath \n\t(Recharge 5-6) The dragon exhales gas in a 15-foot cone. Each creature in that area must succeed on a DC [10+%Con] Constitution saving throw. On a failed save, the creature can't use reactions, its speed is halved, and it can't make more than one attack on its turn. In addition, the creature can use either an action or a bonus action on its turn, but not both. These effects last for 1 minute. The creature can repeat the saving throw at the start of each of its turns, ending the effect on itself with a successful save."
        if Dice(d) == 5 and not ("Euphoria Breath" in cantrip):     cantrip += "\n  - Euphoria Breath \n\t(Recharge 5-6) The dragon exhales a puff of euphoria gas at one creature within 5 feet of it. The target must succeed on a DC [10+%Con] Wisdom saving throw, or for 1 minute, the target can't take reactions and must roll a d6 at the start of each of its turns to determine its behavior during the turn: \n\t\t 1–4. The target takes no action or bonus action and uses all of its movement to move in a random direction. \n\t\t 5–6. The target doesn't move, and the only thing it can do on its turn is make a DC [10+%Con] Wisdom saving throw, ending the effect on itself on a success."
        if Dice(d) == 6 and not ("Repulsion Breath" in cantrip):    cantrip += "\n  - Repulsion Breath \n\t(Recharge 5-6) The dragon exhales repulsion energy in a 30-foot cone. Each creature in that area must succeed on a DC [10+%Con] Strength saving throw. On a failed save, the creature is pushed 30 feet away from the dragon."
        if Dice(d) == 7 and not ("Poison Breath" in cantrip):       cantrip += "\n  - Poison Breath \n\t(Recharge 5-6) The dragon exhales poisonous gas in a 15-foot cone. Each creature in that area must make a DC [10+%Con] Constitution saving throw, taking 21 (6d6) poison damage on a failed save, or half as much damage on a successful one."
        if Dice(d) == 8 and not ("Lightning Breath" in cantrip):    cantrip += "\n  - Lightning Breath \n\t(Recharge 5-6) The dragon exhales lightning in a 40-foot line that is 5 feet wide. Each creature in that line must make a DC [10+%Con] Dexterity saving throw, taking 16 (3d10) lightning damage on a failed save, or half as much damage on a successful one."
        elif Dice(d) == 8 and not ("Lightning Breath" in cantrip):  cantrip += "\n  - Lightning Breath \n\t(Recharge 5-6) The dragon exhales lightning in a 30-foot line that is 5 feet wide. Each creature in that line must make a DC [10+%Con] Dexterity saving throw, taking 22 (4d10) lightning damage on a failed save, or half as much damage on a successful one."
        if Dice(d) == 9 and not ("Cold Breath" in cantrip):         cantrip += "\n  - Cold Breath \n\t(Recharge 5-6) The dragon exhales an icy blast in a 15-foot cone. Each creature in that area must make a DC [10+CON%] Constitution saving throw, taking 18 (4d8) cold damage on a failed save, or half as much damage on a successful one."
        elif Dice(d) == 10 and not ("Cold Breath" in cantrip):      cantrip += "\n  - Cold Breath \n\t(Recharge 5-6) The dragon exhales an icy blast in a 15-foot cone. Each creature in that area must make a DC [10+CON%] Constitution saving throw, taking 22 (5d8) cold damage on a failed save, or half as much damage on a successful one."
        if Dice(d) == 11 and not ("Paralyzing Breath" in cantrip):  cantrip += "\n  - Paralyzing Breath \n\t(Recharge 5-6) The dragon exhales paralyzing gas in a 15-foot cone. Each creature in that area must succeed on a [10+CON%] Constitution saving throw or be paralyzed for 1 minute. A creature can repeat the saving throw at the start of each of its turns, ending the effect on itself on a success."
        if Dice(d) == 12 and not ("WeakeningBreath" in cantrip):    cantrip += "\n  - Weakening Breath \n\t(Recharge 5-6) The dragon exhales gas in a 15-foot cone. Each creature in that area must succeed on a DC [10+CON%] Strength saving throw or have disadvantage on Strength-based attack rolls, Strength checks, and Strength saving throws for 1 minute. A creature can repeat the saving throw at the start of each of its turns, ending the effect on itself on a success."

    if race == "Dragon" and Dice(12) == 1 and not ("Change Shape" in cantrip):  cantrip += "\n- Change Shape \n\t The dragon magically polymorphs into a humanoid or beast that has a challenge rating no higher than its own, or back into its true form. It reverts to its true form if it dies. Any equipment it is wearing or carrying is absorbed or borne by the new form (the dragon's choice).In a new form, the dragon retains its alignment, hit points, Hit Dice, ability to speak, proficiencies, Legendary Resistance, lair actions, and Intelligence, Wisdom, and Charisma scores, as well as this action. Its statistics and capabilities are otherwise replaced by those of the new form, except any class features or legendary actions of that form."
    if race == "Dragon" and Dice() == 1 and not ("Color Spray" in cantrip):     cantrip += "\n- Color Spray"
    if race == "Dragon" and Dice() == 1 and not ("Dancing lights" in cantrip):  cantrip += "\n- Dancing lights"
    if race == "Dragon" and Dice() == 1 and not ("Mage Hand" in cantrip):       cantrip += "\n- Mage Hand"
    if race == "Dragon" and Dice() == 1 and not ("Minor Illusion" in one):      one += "\n- Minor Illusion"
    if race == "Dragon" and Dice(8) == 1 and not ("Major Image" in one):        one += "\n- Major Image"
    if race == "Dragon" and Dice(8) == 1 and not ("Mirror Image" in one):       one += "\n- Mirror Image"
    if race == "Dragon" and Dice(8) == 1 and not ("Polymorph" in one):          one += "\n- Polymorph"
    if race == "Dragon" and Dice(8) == 1 and not ("Suggestion" in one):         one += "\n- Suggestion"

    # DWARF.
    if race == "Dwarf" and Dice(7) == 1 and not ("Enlarge" in cantrip):            cantrip += "\n- Enlarge (Recharges after a Short or Long Rest). \n\t For 1 minute, the Dwarf magically increases in size, along with anything it is wearing or carrying. While enlarged, the Dwarf is Large, doubles its damage dice on Strength-based weapon attacks (included in the attacks), and makes Strength checks and Strength saving throws with advantage. If the Dwarf lacks the room to become Large, it attains the maximum size possible in the space available."
    if race == "Dwarf" and Dice(7) == 1 and not ("Invisibility" in cantrip):       cantrip += "\n- Invisibility (Recharges after a Short or Long Rest). \n\t The dwarf magically turns invisible until it attacks, casts a spell, or until its concentration is broken, up to 1 hour (as if concentrating on a spell). Any equipment the Dwarf wears or carries is invisible with it."


        
    # ELEMENTAL.
    if race == "Elemental" and Dice() == 1 and not ("Whirlwind" in cantrip):
        cantrip += "\n- Whirlwind (Recharge 4–6). \n\t Each creature in the elemental's space must make a DC [11+%STR] Strength saving throw. On a failure, a target takes 15 (3d8 + 2) bludgeoning damage and is flung up 20 feet away from the elemental in a random direction and knocked prone. If a thrown target strikes an object, such as a wall or floor, the target takes 3 (1d6) bludgeoning damage for every 10 feet it was thrown. If the target is thrown at another creature, that creature must succeed on a DC 13 Dexterity saving throw or take the same damage and be knocked prone. /n/t If the saving throw is successful, the target takes half the bludgeoning damage and isn't flung away or knocked prone."
    if race == "Elemental" and Dice() == 1 and not ("Dancing lights" in cantrip):
        cantrip += "\n- Dancing lights"
    if race == "Elemental" and Dice(8) == 1 and not ("Cinder breath" in cantrip):
        cantrip += "\n- Cinder breath \n\t (Recharge 6). The Elemental exhales a 15-foot cone of smoldering ash. Each creature in that area must succeed on a DC [10+%Cha] Dexterity saving throw or be blinded until the end of the Elemental's next turn."
    if race == "Elemental" and Dice(8) == 1 and not ("Blinding breath" in cantrip):
        cantrip += "\n- Blinding breath \n\t (Recharge 6). The Elemental exhales a 15-foot cone of blinding dust. Each creature in that area must succeed on a DC [10+%Cha] Dexterity saving throw or be blinded for one minute."
    if race == "Elemental" and Dice(8) == 1 and not ("Steam breath" in cantrip):
        cantrip += "\n- Steam breath \n\t (Recharge 6). The Elemental exhales a 15-foot cone of scalding steam. Each creature in that area must succeed on a DC [10+%Cha] Dexterity saving throw, taking 4 (1d8) fire damage on a failed save, or half as much damage on a successful one."
    if race == "Elemental" and Dice(8) == 1 and not ("Frost Breath" in cantrip):
        cantrip += "\n- Frost Breath \n\t (Recharge 6). The Elemental exhales a 15-foot cone of cold air. Each creature in that area must succeed on a DC [10+%Con] Dexterity saving throw, taking 5 (2d4) cold damage on a failed save, or half as much damage on a successful one."
    if race == "Elemental" and Dice(8) == 1 and not ("Fire Breath" in cantrip):
        cantrip += "\n- Fire Breath \n\t (Recharge 6). The Elemental exhales a 15-foot cone of cold air. Each creature in that area must succeed on a DC [10+%Con] Dexterity saving throw, taking 7 (2d6) fire damage on a failed save, or half as much damage on a successful one."
    if race == "Elemental":
        if Dice(8) == 1 and not ("Summon Mephits" in one):
            one += "\n- Summon Mephits (1/Day) \n\t The Elemental has a 25 percent chance of summoning 1d4 mephits. A summoned mephit appears in an unoccupied space within 60 feet of its summoner, acts as an ally of its summoner, and can't summon other mephits. It remains for 1 minute, until it or its summoner dies, or until its summoner dismisses it as an action."
        if Dice() == 1 and not ("Innate Spellcasting" in one):
            one += "\n-  Innate Spellcasting (1/Day) \n\t The Elemental can innately cast fog cloud, requiring no material components."
        if Dice() == 1 and not ("Innate Spellcasting" in one):
            one += "\n-  Innate Spellcasting (1/Day) \n\t The Elemental can innately cast heat metal, requiring no material components."
        if Dice() == 1 and not ("Blur" in one):
            one += "\n- Blur"
        if Dice() == 1 and not ("Sleep" in one):
            one += "\n- Sleep"

    # ELF.
    if race == "Elf" and Dice() == 1 and not ("Dancing lights" in cantrip): cantrip += "\n- Dancing lights"
    if race == "Elf" and Dice() == 1 and not ("Darkness" in one):               one += "\n- Darkness"
    if race == "Elf" and Dice() == 1 and not ("Faerie fire" in one):            one += "\n- Faerie fire"
    if race == "Elf" and Dice(8) == 1 and not ("Levitate" in one):              one += "\n- Levitate (Self Only)"

    # FAE.
    if race == "Fey" and Dice(8) == 1 and not ("Ethereal Jaunt" in cantrip):    cantrip += "\n- Ethereal Jaunt \n\t As a bonus action, the fey can magically shift from the Material Plane to the Ethereal Plane, or vice versa."
    if race == "Fey" and Dice(10) == 1 and not ("Teleport" in cantrip):         cantrip += "\n- Teleport (Recharge 4–6). \n\t The Fey magically teleports, along with any equipment it is wearing or carrying, up to 40 feet to an unoccupied space it can see. Before or after teleporting, the Fey can make one bite attack."
    if race == "Fey" and Dice(10) == 1 and not ("Heart Sight" in cantrip):      cantrip += "\n- Heart Sight. \n\t The Fey touches a creature and magically knows the creature's current emotional state. If the target fails a DC [10+%Cha] Charisma saving throw, the Fey also knows the creature's alignment. Celestials, fiends, and undead automatically fail the saving throw."
    if race == "Fey" and Dice(10) == 1 and not ("Invisibility" in cantrip):     cantrip += "\n- Invisibility. \n\t The Fey  magically turns invisible until it attacks or casts a spell, or until its concentration ends (as if concentrating on a spell). Any equipment the Fey wears or carries is invisible with it."
    if race == "Fey" and Dice() == 1 and not ("Druidcraft" in cantrip):         cantrip += "\n- Druidcraft"
    if race == "Fey" and Dice() == 1 and not ("Dancing Lights" in cantrip):     cantrip += "\n- Dancing Lights"
    if race == "Fey" and Dice() == 1 and not ("Detect Magic" in cantrip):       cantrip += "\n- Detect Magic"
    if race == "Fey" and Dice(8) == 1 and not ("Minor Illusion" in cantrip):    cantrip += "\n- Minor Illusion"
    if race == "Fey" and Dice() == 1 and not ("Magic Missile" in cantrip):      cantrip += "\n- Minor Illusion"
    if race == "Fey" and Dice() == 1 and not ("Vicious Mockery" in cantrip):    cantrip += "\n- Vicious Mockery"
    if race == "Fey" and Dice(8) == 1 and not ("Change Shape" in cantrip):      cantrip += "\n- Change Shape. \n\t The fey magically polymorphs into a Small or Medium humanoid, or back into their true form. Their statistics are the same in each form. Any equipment they are wearing or carrying isn't transformed. They reverts to their true form if they dies."
    if race == "Fey" and Dice() == 1 and not ("Etherealness" in cantrip):       cantrip += "\n- Etherealness. \n\t The fey magically enters the Ethereal Plane from the Material Plane, or vice versa. To do so, the fey must have a heartstone in her possession."



    if race == "Fey" and Dice() == 1 and not ("Barkskin" in one):               one += "\n- Barkskin"
    if race == "Fey" and Dice() == 1 and not ("Pass Without Trace" in one):     one += "\n- Pass Without Trace"
    if race == "Fey" and Dice() == 1 and not ("Shillelagh" in one):             one += "\n- Shillelagh"
    if race == "Fey" and Dice() == 1 and not ("Confusion" in one):              one += "\n- Confusion"
    if race == "Fey" and Dice() == 1 and not ("Dancing lights" in one):         one += "\n- Dancing lights"
    if race == "Fey" and Dice() == 1 and not ("Detect Evil and Good" in one):   one += "\n- Detect Evil and Good"
    if race == "Fey" and Dice() == 1 and not ("Detect Thoughts" in one):        one += "\n- Detect Thoughts"
    if race == "Fey" and Dice() == 1 and not ("Dispel Magic" in one):           one += "\n- Dispel Magic"
    if race == "Fey" and Dice() == 1 and not ("Entangle" in one):               one += "\n- Entangle"
    if race == "Fey" and Dice() == 1 and not ("Fly" in one):                    one += "\n- Fly: 30 ft"
    if race == "Fey" and Dice() == 1 and not ("Phantasmal Force" in one):       one += "\n- Phantasmal Force"
    if race == "Fey" and Dice() == 1 and not ("Polymorph" in one):              one += "\n- Polymorph"
    if race == "Fey" and Dice(8) == 1 and not ("Sleep" in one):                 one += "\n- Sleep"
    if race == "Fey" and Dice(8) == 1 and not ("Charming Melody" in one):       one += "\n- Charming Melody [DC 10+%Cha Wisdom saving throw]\n\t The creature is charmed by the Fey for 1 minute. If the Fey or any of its companions harms the creature, the effect on it ends immediately."
    if race == "Fey" and Dice(8) == 1 and not ("Frightening Strain" in one):    one += "\n- Frightening Strain [DC 10+%Cha Wisdom saving throw] \n\t The creature is charmed by the Fey for 1 minute. If the Fey or any of its companions harms the creature, the effect on it ends immediately."
    if race == "Fey" and Dice(8) == 1 and not ("Gentle Lullaby" in one):        one += "\n- Gentle Lullaby [DC 10+%Cha Wisdom saving throw] \n\t The creature falls asleep and is unconscious for 1 minute. The effect ends if the creature takes damage or if someone takes an action to shake the creature awake."
    if race == "Fey" and Dice(8) == 1 and not ("Nightmare Haunting" in one):    one += "\n- Nightmare Haunting \n\t While on the Ethereal Plane, the fey magically touches a sleeping humanoid on the Material Plane. A protection from evil and good spell cast on the target prevents this contact, as does a magic circle. As long as the contact persists, the target has dreadful visions. If these visions last for at least 1 hour, the target gains no benefit from its rest, and its hit point maximum is reduced by 5 (1d10). If this effect reduces the target's hit point maximum to 0, the target dies, and if the target was evil, its soul is trapped in the fey's soul bag. The reduction to the target's hit point maximum lasts until removed by the greater restoration spell or similar magic."


    if race == "Fey" and Dice() == 1 and not ("Plane Shift" in two):            two += "\n- Plane Shift (self only)"
    if race == "Fey" and Dice() == 1 and not ("Ray Of Enfeeblement" in two):    two += "\n- Ray Of Enfeeblement"
    if race == "Fey" and Dice() == 1 and not ("Sleep" in two):                  two += "\n- Sleep"
        
    if race == "Fey" and Dice() == 1 and not ("Entangle" in three):           three += "\n- Entangle"
    if race == "Fey" and Dice() == 1 and not ("Goodberry" in three):          three += "\n- Goodberry"



    # FIENDS.
    # Cantrips and at-will magic

    if race == "Fiend":
        if Dice()==1 and not ("Charm" in cantrip):
            if Dice(2)==1:  cantrip += "\n- Charm \n\t One humanoid the fiend can see within 30 feet of it must succeed on a DC [10+%CHA] Wisdom saving throw or be magically charmed for 1 day. The charmed target obeys the fiend's verbal or telepathic commands. If the target suffers any harm or receives a suicidal command, it can repeat the saving throw, ending the effect on a success. If the target successfully saves against the effect, or if the effect on it ends, the target is immune to this fiend's Charm for the next 24 hours. \n\t The fiend can have only one target charmed at a time. If it charms another, the effect on the previous target ends. "
            else:           cantrip += "\n- Fiendish Charm. \n\t One humanoid the fiend can see within 30 feet of it must succeed on a DC [11+%CHA] Wisdom saving throw or be magically charmed for 1 day. The charmed target obeys the fiend's spoken commands. If the target suffers any harm from the fiend or another creature or receives a suicidal command from the fiend, the target can repeat the saving throw, ending the effect on itself on a success. If a target's saving throw is successful, or if the effect ends for it, the creature is immune to the fiend's Fiendish Charm for the next 24 hours."
            if Dice()==1 and not ("Draining Kiss" in cantrip):      cantrip += "\n- Draining Kiss \n\t The fiend kisses a creature charmed by it or a willing creature. The target must make a DC 15 Constitution saving throw against this magic, taking 32 (5d10 + 5) psychic damage on a failed save, or half as much damage on a successful one. The target's hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0. "
            if Dice()==1 and not ("Telepathic Bond" in cantrip):    cantrip += "\n- Telepathic Bond. \n\t The fiend ignores the range restriction on its telepathy when communicating with a creature it has charmed. The two don't even need to be on the same plane of existence."

        if Dice() == 1 and not ("Ethereal Stride" in cantrip):      cantrip += "\n- Ethereal Stride.\n\t The fiend and up to three willing creatures within 5 feet of it magically enter the Ethereal Plane from the Material Plane, or vice versa."
        if Dice() == 1 and not ("Etherealness" in cantrip):         cantrip += "\n- Etherealness.\n\t The fiend magically enters the Ethereal Plane from the Material Plane, or vice versa."
        if Dice() == 1 and not ("Fire Breath" in cantrip):          cantrip += "\n- Fire Breath (Recharge 5-6).\n\t The fiend exhales fire in a 15-foot cone. Each creature in that area must make a DC [10+%CON] Dexterity saving throw, taking 21 (6d6) fire damage on a failed save, or half as much damage on a successful one."
        if Dice() == 1 and not ("Fire Ray" in cantrip):             cantrip += "\n- Fire Ray \n\t Ranged Spell Attack. Range 120ft. One target. Hit: 10(3d6) fire damage."

    # Once a day
    if race == "Fiend":
        if Dice() == 1 and not ("Scare" in one):            one += "\n- Scare \n\t One creature of the Fiend's choice within 20 feet of it must succeed on a DC 10 Wisdom saving throw or be frightened for 1 minute. The target can repeat the saving throw at the begguining of each of its turns, with disadvantage if the Fiend is within line of sight, ending the effect on itself on a success."
        if Dice() == 1 and not ("Fetid Cloud" in one):      one += "\n- Fetid Cloud.\n\t A 10-foot radius of disgusting sulfuric gas extends out from the Fiend. The gas spreads around corners, and its area is lightly obscured. It lasts for 1 minute or until a strong wind disperses it. Any creature that starts its turn in that area must succeed on a DC 11 Constitution saving throw or be poisoned until the start of its next turn. While poisoned in this way, the target can take either an action or a bonus action on its turn, not both, and can't take reactions."
        if Dice() == 1 and not ("Entangle" in one):         one += "\n- Entangle."
        if Dice() == 1 and not ("Phantasmal Force" in one): one += "\n- Phantasmal Force."
        if Dice() == 1 and not ("Plane Shift" in one):      one += "\n- Plane Shift."
        if Dice() == 1 and not ("Cloudkill" in one):        one += "\n- Cloudkill."
        if Dice() == 1 and not ("Summon Yugoloth" in one):  one += "\n- Summon Yugoloth. \n\t The fiend attempts a magical summoning. \n\t A fiend has a 30 percent chance of summoning one mezzoloth. \n\t A summoned yugoloth appears in an unoccupied space within 60 feet of its summoner, does as it pleases, and can't summon other yugoloths. The summoned yugoloth remains for 1 minute, until it or its summoner dies, or until its summoner takes a bonus action to dismiss it."
            
            

    # Twice a day
    if race == "Fiend":
        if Dice() == 1 and not ("Disguise Self" in two):    two += "\n- Disguise Self."
        if Dice() == 1 and not ("Invisibility" in two):     two += "\n- Invisibility (self only)."
        if Dice() == 1 and not ("Darkness" in two):         two += "\n- Darkness."
        if Dice() == 1 and not ("Dispel Magic" in two):     two += "\n- Dispel Magic."

    # Three times a day
    if race == "Fiend":
        if Dice() == 1 and not ("Alter Self" in three):     three += "\n- Alter Self"
        if Dice() == 1 and not ("Command" in three):        three += "\n- Command"
        if Dice() == 1 and not ("Detect Magic" in three):   three += "\n- Detect Magic"

    # GIANT.

    # GNOME.
    if race == "Gnome" and Dice() == 1 and not ("Nondetection" in cantrip):          cantrip += "\n- Nondetection (self only)"
    if race == "Gnome" and Dice() == 1 and not ("Blindness/Deafness" in one):        one += " \n- Blindness/Deafness"
    if race == "Gnome" and Dice() == 1 and not ("Blur" in one):                      one += " \n- Blur"
    if race == "Gnome" and Dice() == 1 and not ("Disguise Self" in one):             one += " \n- Disguise Self"

    # GOBLIN.
    if race == "Goblin" and Dice() == 1 and not ("Leadership" in cantrip):           cantrip += " \n- Leadership (Recharges after a Short or Long Rest). \n\t For 1 minute, the goblin can utter a special command or warning whenever a nonhostile creature that it can see within 30 feet of it makes an attack roll or a saving throw. The creature can add a d4 to its roll provided it can hear and understand the goblin. A creature can benefit from only one Leadership die at a time. This effect ends if the goblin is incapacitated."

    # HALFLING. 

    # HUMAN. 

    # KOBOLDS.

    # LIZARDFOLK.
        

    #MONSTROSITIES.
    ## At will:
    if race == "Monstrosity":
        if Dice(8) == 1 and not ("Acid Spray" in cantrip):
            cantrip += "\n - Acid Spray (Recharge 6): \n\t The Monstrosity spits acid in a line that is 30 feet long and 5 feet wide, provided that it has no creature grappled. Each creature in that line must make a DC [10+%Str] Dexterity saving throw, taking 10 (3d6) acid damage on a failed save, or half as much damage on a successful one."
        if Dice(10) == 1 and not ("Confusing Gaze" in cantrip):
            cantrip += "\n - Confusing Gaze: \n\t When a creature starts its turn within 30 feet of the monstrosity and is able to see the monstrosity's eyes, the monstrosity can magically force it to make a DC [11+%CON] Charisma saving throw, unless the monstrosity is incapacitated. \n\t On a failed saving throw, the creature can't take reactions until the start of its next turn and rolls a d8 to determine what it does during that turn. On a 1 to 4, the creature does nothing. On a 5 or 6, the creature takes no action but uses all its movement to move in a random direction. On a 7 or 8, the creature makes one melee attack against a random creature, or it does nothing if no creature is within reach. \n\t Unless surprised, a creature can avert its eyes to avoid the saving throw at the start of its turn. If the creature does so, it can't see the monstrosity until the start of its next turn, when it can avert its eyes again. If the creature looks at the monstrosity in the meantime, it must immediately make the save." 
        if Dice() == 1 and not ("Chilling Gaze" in cantrip):
            cantrip += "\n - Chilling Gaze: \n\t The monstrosity targets one creature it can see within 30 feet of it. If the target can see the monstrosity, the target must succeed on a DC [10+%CON] Constitution saving throw against this magic or take 10 (3d6) cold damage and then be paralyzed for 1 minute, unless it is immune to cold damage. The target can repeat the saving throw at the start of each of its turns, ending the effect on itself on a success. If the target's saving throw is successful, or if the effect ends on it, the target is immune to the Chilling Gaze of all monstrosities for 1 hour."
        if Dice() == 1 and not ("Disguise Self" in cantrip):
            cantrip += "\n - Disguise self (humanoid form) Aura: \n\t A 15-foot radius of magical darkness extends out from the Monstrosity, moves with it, and spreads around corners. The darkness lasts as long as the Monstrosity maintains concentration, up to 10 minutes (as if concentrating on a spell). Darkvision can't penetrate this darkness, and no natural light can illuminate it. If any of the darkness overlaps with an area of light created by a spell of 2nd level or lower, the spell creating the light is dispelled."
        if Dice(8) == 1 and not ("Fire Breath" in cantrip):
            cantrip += "\n -  Fire Breath (Recharge 5–6). \n\t The monstrosity exhales fire in a 15-foot cone. Each creature in that area must make a DC[11+%CON] Dexterity saving throw, taking 31 (7d8) fire damage on a failed save, or half as much damage on a successful one."
                
        if Dice(8) == 1 and not ("Luring Song" in cantrip):
            cantrip += "\n - Luring Song: \n\t The monstrosity sings a magical melody. Every humanoid and giant within 300 feet of the monstrosity that can hear the song must succeed on a DC [10+%Cha] Wisdom saving throw or be charmed until the song ends. The monstrosity must take a bonus action on its subsequent turns to continue singing. It can stop singing at any time. The song ends if the monstrosity is incapacitated. While charmed by the monstrosity, a target is incapacitated and ignores the songs of other monstrosities. If the charmed target is more than 5 feet away from the monstrosity, the target must move on its turn toward the monstrosity by the most direct route. It doesn't avoid opportunity attacks, but before moving into damaging terrain, such as lava or a pit, and whenever it takes damage from a source other than the monstrosity, a target can repeat the saving throw. A creature can also repeat the saving throw at the begguining of each of its turns. If a creature's saving throw is successful, the effect ends on it. A target that successfully saves is immune to this monstrosity's song for the next 24 hours."

        if Dice(8) == 1 and not ("Major Image" in cantrip):          cantrip += "\n - Major Image."
        if Dice(10) == 1 and not ("Petrifying Breath" in cantrip):    cantrip += "\n - Petrifying Breath (Recharge 5-6): \n\t The monstrosity exhales petrifying gas in a 30-foot cone. Each creature in that area must succeed on a Constitution saving throw (against the creature's Spellsave DC). On a failed save, a target begins to turn to stone and is restrained. The restrained target must repeat the saving throw at the start of its next turn. On a success, the effect ends on the target. On a failure, the target is petrified until freed by the greater restoration spell or other magic."
        if Dice(10) == 1 and not ("Petrifying Gaze" in cantrip):      cantrip += "\n - Petrifying Gaze: \n\t If a creature starts its turn within 30 feet of the monstrosity and the two of them can see each other, the monstrosity can force the creature to make a DC [10+%CON] Constitution saving throw if the monstrosity isn't incapacitated. On a failed save, the creature magically begins to turn to stone and is restrained. It must repeat the saving throw at the start of its next turn. On a success, the effect ends. On a third failure, the creature is petrified until freed by the greater restoration spell or other magic. \n\t A creature that isn't surprised can avert its eyes to avoid the saving throw at the start of its turn. If it does so, it can't see the monstrosity until the start of its next turn, when it can avert its eyes again. If it looks at the monstrosity in the meantime, it must immediately make the save. \n\t If the monstrosity sees its reflection within 30 feet of it in bright light, it mistakes itself for a rival and targets itself with its gaze."
        if Dice(8) == 1 and not ("Read Thoughts" in cantrip):        cantrip += "\n - Read Thoughts: \n\t The monstrosity magically reads the surface thoughts of one creature within 60 feet of it. The effect can penetrate barriers, but 3 feet of wood or dirt, 2 feet of stone, 2 inches of metal, or a thin sheet of lead blocks it. While the target is in range, the monstrosity can continue reading its thoughts, as long as the monstrosity's concentration isn't broken (as if concentrating on a spell). While reading the target's mind, the monstrosity has advantage on Wisdom (Insight) and Charisma (Deception, Intimidation, and Persuasion) checks against the target."


    if race == "Monstrosity":
        if Dice(10) == 1 and not ("Paralyzing Ray" in cantrip):   cantrip += "\n - Paralyzing Ray \n\t The targeted creature must succeed on a DC [11+%CON] Constitution saving throw or be paralyzed for 1 minute. The target can repeat the saving throw at the start of each of its turns, ending the effect on itself on a success."
        if Dice(10) == 1 and not ("Fear Ray" in cantrip):         cantrip += "\n - Fear Ray \n\t The targeted creature must succeed on a DC [11+%CON] Wisdom saving throw or be frightened for 1 minute. The target can repeat the saving throw at the start of each of its turns, ending the effect on itself on a success."
        if Dice(10) == 1 and not ("Enervation Ray" in cantrip):   cantrip += "\n - Enervation Ray \n\t The targeted creature must make a DC [11+%CON] Constitution saving throw, taking 36 (8d8) necrotic damage on a failed save, or half as much damage on a successful one."
        if Dice(10) == 1 and not ("Disintegration Ray" in cantrip):   cantrip += "\n - Disintegration Ray. \n\t If the target is a creature, it must succeed on a DC [11+%CON] Dexterity saving throw or take 45 (10d8) force damage. If this damage reduces the creature to 0 hit points, its body becomes a pile of fine gray dust. \n\t If the target is a Large or smaller nonmagical object or creation of magical force, it is disintegrated without a saving throw. If the target is a Huge or larger nonmagical object or creation of magical force, this ray disintegrates a 10-foot cube of it."

    ## Once a day
    if race == "Monstrosity" and Dice() == 1 and not ("Darkness Aura" in one):      one += "\n - Darkness Aura: \n\t A 15-foot radius of magical darkness extends out from the Monstrosity, moves with it, and spreads around corners. The darkness lasts as long as the Monstrosity maintains concentration, up to 10 minutes (as if concentrating on a spell). Darkvision can't penetrate this darkness, and no natural light can illuminate it. If any of the darkness overlaps with an area of light created by a spell of 2nd level or lower, the spell creating the light is dispelled."
    if race == "Monstrosity" and Dice() == 1 and not ("Geas" in one):               one += "\n - Geas."
    ## Three a day
    if race == "Monstrosity" and Dice() == 1 and not ("Charm Person" in three): three += "\n - Charm Person."
    if race == "Monstrosity" and Dice() == 1 and not ("Mirror Image" in three): three += "\n - Mirror Image."
    if race == "Monstrosity" and Dice() == 1 and not ("Scrying" in three):      three += "\n - Scrying."
    if race == "Monstrosity" and Dice() == 1 and not ("Suggestion" in three):   three += "\n - Suggestion."

    # OOZE
    if race == "Ooze" and Dice() == 1 and not ("Psychic Crush" in cantrip):     cantrip += " \n- Psychic Crush (Recharge 5–6). \n\t The ooze targets one creature that it can sense within 60 feet of it. The target must make a DC [10+%INT] Intelligence saving throw, taking 10 (3d6) psychic damage on a failed save, or half as much damage on a successful one."

    # ORCS
        
    # PLANTS
    # Spores
    if race == "Plant" and Dice(8) == 1 and not ("Hallucination Spores" in cantrip):         cantrip += "\n - Hallucination Spores \n\t The plant ejects spores at one creature it can see within 5 feet of it. The target must succeed on a DC 10+%CON Constitution saving throw or be poisoned for 1 minute. The poisoned target is incapacitated while it hallucinates. The target can repeat the saving throw at the start of each of its turns, ending the effect on itself on a success."
    if race == "Plant" and Dice(8) == 1 and not ("Rapport Spores" in cantrip):               cantrip += "\n - Rapport Spores \n\t A 20-foot radius of spores extends from the plant. These spores can go around corners and affect only creatures with an Intelligence of 2 or higher that aren't undead, constructs, or elementals. Affected creatures can communicate telepathically with one another while they are within 30 feet of each other. The effect lasts for 1 hour."
    if race == "Plant" and Dice(8) == 1 and not ("Caustic Spores" in one):           one += "\n - Caustic Spores \n\t The Plant releases spores in a 30-foot cone. Each creature inside the cone must succeed on a DC [10+%Con] Dexterity saving throw or take 3 (1d6) acid damage at the start of each of the plant's turns. A creature can repeat the saving throw at the start of its turn, ending the effect on itself on a success."
    if race == "Plant" and Dice(8) == 1 and not ("Infestation Spores" in one):       one += "\n - Infestation Spores \n\t The plant releases spores that burst out in a cloud that fills a 10-foot-radius sphere centered on it, and the cloud lingers for 1 minute. Any flesh-and-blood creature in the cloud when it appears, or that enters it later, must make a DC [10+%CON] Constitution saving throw. On a successful save, the creature can't be infected by these spores for 24 hours. On a failed save, the creature is infected with a disease called the spores of Zuggtmoy and also gains a random form of indefinite madness (determined by rolling on the Madness of Zuggtmoy table) that lasts until the creature is cured of the disease or dies. While infected in this way, the creature can't be reinfected, and it must repeat the saving throw at the end of every 24 hours, ending the infection on a success. On a failure, the infected creature's body is slowly taken over by fungal growth, and after three such failed saves, the creature dies and is reanimated as a spore servant if it's a humanoid or a Large or smaller beast. \n d100 \t	Flaw (lasts until cured) \n 01-20 \t I see visions in the world around me that others do not. \n 21-40 \t I periodically slip into a catatonic state, staring off into the distance for long stretches at a time. \n 41-60 \t I see an altered version of reality, with my mind convincing itself that things are true even in the face of overwhelming evidence to the contrary. \n 61-80 \t My mind is slipping away, and my intelligence seems to wax and wane. \n  81-00 \t I am constantly scratching at unseen fungal infections."
    if race == "Plant" and Dice(8) == 1 and not ("Euphoria Spores" in one):          one += "\n - Euphoria Spores \n\t The plant releases a cloud of spores in a 20-foot-radius sphere centered on itself. Other creatures in that area must each succeed on a DC [10+%Con] Constitution saving throw or become poisoned for 1 minute. A creature can repeat the saving throw at the start of each of its turns, ending the effect early on itself on a success. When the effect ends on it, the creature gains one level of exhaustion."
    if race == "Plant" and Dice(8) == 1 and not ("Pacifying Spores" in three):            three += "\n - Pacifying Spores \n\t The Plant ejects spores at one creature it can see within 5 feet of it. The target must succeed on a DC [10+%CON] Constitution saving throw or be stunned for 1 minute. The target can repeat the saving throw at the start of each of its turns, ending the effect on itself on a success."
    if race == "Plant" and Dice(8) == 1 and not ("Animating Spores" in three):            three += "\n - Animating Spores \n\t The Plant targets one corpse of a humanoid or a Large or smaller beast within 5 feet of it and releases spores at the corpse. In 24 hours, the corpse rises as a spore servant. The corpse stays animated for 1d4 + 1 weeks or until destroyed, and it can't be animated again in this way."

    if race == "Snakefolk" and Dice() == 1 and not ("Animal Friendship" in cantrip):            cantrip += "\n- Animal Friendship (snakes only)"
    if race == "Snakefolk" and Dice() == 1 and not ("Poison Spray" in three):           three += "\n- Poison Spray"
    if race == "Snakefolk" and Dice() == 1 and not ("Suggestion" in three):             three += "\n- Suggestion"

    # UNDEAD
    if race == "Undead":
        if Dice(8) == 1 and not ("Create Specter" in cantrip):             cantrip += "\n - Create Specter \n\t The undead targets a humanoid within 10 feet of it that has been dead for no longer than 1 minute and died violently. The target's spirit rises as a specter in the space of its corpse or in the nearest unoccupied space. The specter is under the undead's control. The undead can have no more than seven specters under its control at one time." 
        if Dice(8) == 1 and not ("Corrupting Touch" in cantrip):           cantrip += "\n - Corrupting Touch \n\t Melee Spell Attack: reach 5 ft., one target. Hit: 10 (3d6) necrotic damage."
        if Dice(8) == 1 and not ("Dreadful Glare" in cantrip):             cantrip += "\n - Dreadful Glare. \n\t The undead targets one creature it can see within 60 feet of it. If the target can see the undead, it must succeed on a DC [10+%CHA] Wisdom saving throw against this magic or become frightened until the end of the undead's next turn. If the target fails the saving throw by 5 or more, it is also paralyzed for the same duration. A target that succeeds on the saving throw is immune to the Dreadful Glare of all undead for the next 24 hours."
        if Dice(8) == 1 and not ("Forceful Slam" in cantrip):              cantrip += "\n - Forceful Slam \n\t Magic melee attack. Hit: 10 (3d6) force damage. "
        if Dice(8) == 1 and not ("Fire Ray" in cantrip):                   cantrip += "\n - Fire Ray \n\t Magic attack. Range 30 ft. Hit: 10 (3d6) fire damage. "
        if Dice(8) == 1 and not ("Horrifying Visage" in cantrip):          cantrip += "\n - Horrifying Visage \n\t Each non-undead creature within 60 feet of the Undead that can see them must succeed on a DC [10+%CHA] Wisdom saving throw or be frightened for 1 minute. A frightened target can repeat the saving throw at the start of each of its turns, with disadvantage if the Undead is within line of sight, ending the effect on itself on a success. If a target's saving throw is successful or the effect ends for it, the target is immune to the Undead's Horrifying Visage for the next 24 hours. "
        if Dice(8) == 1 and not ("Life Drain" in cantrip):                 cantrip += "\n - Life Drain \n\t On an hit, the target's Hit Points Maximum is reduced by the damage dealt. The target dies if this reduces its Hit Points Maximum to 0. Otherwise, the reduction lasts until the target finishes a short or long rest. "
        elif Dice(8) == 1 and not ("Life Drain" in cantrip):               cantrip += "\n - Life Drain \n\t On an hit, the target makes a Constitution saving throw. On a fail, the target takes 4d6 necrotic damage. The target's Hit Points Maximum is reduced by the necrotic damage dealt. The target dies if this reduces its Hit Points Maximum to 0. Otherwise, the reduction lasts until the target finishes a long rest. "
        if Dice(8) == 1 and not ("Mage Hand" in cantrip):                  cantrip += "\n - Mage Hand "
        if Dice(8) == 1 and not ("Rotting Fist" in cantrip):               cantrip += "\n - Rotting Fist. \n\t Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) bludgeoning damage plus 10 (3d6) necrotic damage. If the target is a creature, it must succeed on a DC [10+%CHA] Constitution saving throw or be cursed with undead rot. The cursed target can't regain hit points, and its hit point maximum decreases by 10 (3d6) for every 24 hours that elapse. If the curse reduces the target's hit point maximum to 0, the target dies, and its body turns to dust. The curse lasts until removed by the remove curse spell or other magic."
        if Dice(8) == 1 and not ("Strength Drain" in cantrip):             cantrip += "\n - Strength Drain \n\t On an attack hit the target's Strength score is reduced by 1d4. The target dies if this reduces its Strength to 0. Otherwise, the reduction lasts until the target finishes a short or long rest. \n\t If a non-evil humanoid dies from this attack, a new shadow rises from the corpse 1d4 hours later."
        if Dice(8) == 1 and not ("Telekinetic Thrust" in cantrip):         cantrip += "\n - Telekinetic Thrust. \n\t The undead targets a creature or unattended object within 30 feet of it. A creature must be Medium or smaller to be affected by this magic, and an object can weigh up to 150 pounds. \n\t If the target is a creature, the undead makes a Charisma check contested by the target's Strength check. If the undead wins the contest, the undead hurls the target up to 30 feet in any direction, including upward. If the target then comes into contact with a hard surface or heavy object, the target takes 1d6 damage per 10 feet moved. \n\t If the target is an object that isn't being worn or carried, the undead hurls it up to 30 feet in any direction. The undead can use the object as a ranged weapon, attacking one creature along the object's path (+4 to hit) and dealing 5 (2d4) bludgeoning damage on a hit."

    if race == "Undead":
        if Dice(8) == 1 and not ("Wail" in one):   one += "\n - Wail. \n\t The undead releases a mournful wail, provided that they aren't in sunlight. This wail has no effect on constructs and undead. All other creatures within 30 feet of them that can hear them must make a DC [10+%CHA] Constitution saving throw. On a failure, a creature drops to 0 hit points. On a success, a creature takes 10 (3d6) psychic damage."
        

            

    r = "\n"
    if not (cantrip == "Cantrips (at will): "):         r += cantrip + "\n"
    if not (first == "1st Level Spells: "):             r += "[{}]".format(Dice(slots1)) + first  + "\n"
    if not (second == "2nd Level Spells: "):            r += "[{}]".format(Dice(slots2)) + second + "\n"
    if Lvl>=5:
        if not (third == "3rd Level Spells: "):         r += "[{}]".format(Dice(slots3)) + third  + "\n"
        if not (fourth == "4th Level Spells: "):        r += "[{}]".format(Dice(slots4)) + fourth + "\n"
    if Lvl>=10:
        if not (fifth == "5th Level Spells: "):         r += "[{}]".format(Dice(slots5)) + fifth  + "\n"
        if not (sixth == "6th Level Spells: "):         r += "[{}]".format(Dice(slots6)) + sixth  + "\n"
    if Lvl>=15:
        if not (seventh == "7th Level Spells: "):       r += "[{}]".format(Dice(slots7)) + seventh + "\n"
    if Lvl>=17:
        if not (eigth == "8th Level Spells: "):         r += "[{}]".format(Dice(slots8)) + eigth  + "\n"
    if Lvl>=20:
        if not (ninth == "9th Level Spells: "):         r += "[{}]".format(Dice(slots9)) + ninth  + "\n"
    if not (one == "1/Day each: "):        r += "\n" + one
    if not (two == "2/Day each: "):        r += "\n" + two
    if not (three == "3/Day each: "):      r += "\n" + three
    return r






def Abilities(Type=""):
    if Type == "":
        if Dice(0) == 1:    Type= Race()
        else:               Type= Background()

    r = ""

    # ABERRATIONS

    ## Senses
    if Type == "Aberration":
        if Dice() == 1:            r = r + "\n- Blindsight: \n\t 60ft"
        elif Dice() == 1:          r = r + "\n- Darkvision: \n\t 120ft"
        else:                      r = r + "\n- Darkvision: \n\t 60ft"
        
    if Type == "Aberration":
        if Dice() == 1:
            r = r + "\n- Telepathy: \n\t 60ft"
            if Dice() == 1:    r = r + "\n- Advanced Telepathy: \n\t The Aberration can perceive the content of any telepathic communication used within 60 feet of it, and it can't be surprised by creatures with any form of telepathy."
            if Dice() == 1:    r = r + "\n- Telepathic Shroud. \n\t The Aberration is immune to any effect that would sense its emotions or read its thoughts, as well as all divination spells."
            if Dice() == 1:    r = r + "\n- Limited Telepathy. \n\t The Aberration can magically transmit simple messages and images to any creature within 120 feet of it that can understand a language. This form of telepathy doesn't allow the receiving creature to telepathically respond."

    if Type == "Aberration" and Dice() == 1:        r += "\n- Sense Magic. \n\t The Aberration senses magic within 120 feet of it at will. This trait otherwise works like the Detect Magic spell but isn't itself magical."

    ## Movement
    if Type == "Aberration":
        if Dice() == 1:            r = r + "\n- Swim: \n\t 30ft"
        elif Dice() == 1:          r = r + "\n- Swim: \n\t 50ft"

    ## Resistances and Weaknesses
    if Type == "Aberration" and Dice() == 1:        r += "\n- Damage Resistances:  \t acid"
    if Type == "Aberration" and Dice() == 1:        r += "\n- Damage Resistances:  \t bludgeoning, piercing, and slashing from nonmagical attacks"
    if Type == "Aberration" and Dice() == 1:        r += "\n- Damage Resistances:  \t cold"
    if Type == "Aberration" and Dice() == 1:        r += "\n- Damage Resistances:  \t fire"
    if Type == "Aberration" and Dice() == 1:        r += "\n- Damage Resistances:  \t lightning"

    if Type == "Aberration" and Dice() == 1:        r += "\n- Damage Immunities:  \t poison"

    if Type == "Aberration" and Dice() == 1:        r = r + "\n- Damage Vulnerabilities: \n\t psychic"

    if Type == "Aberration" and Dice() == 1:        r += "\n- Damage Resistances:  \t thunder"

    if Type == "Aberration" and Dice() == 1:        r += "\n- Condition Immunities:  \n\t Prone"
    if Type == "Aberration" and Dice() == 1:        r += "\n- Condition Immunities:  \n\t Blinded"
    if Type == "Aberration" and Dice() == 1:        r += "\n- Condition Immunities:  \n\t Poisoned"

    if Type == "Aberration" and Dice() == 1:        r = r + "\n- Magic Resistance: \n\t The Aberration has advantage on saving throws against spells and other magical effects."
    if Type == "Aberration" and Dice() == 1:        r = r + "\n- Regeneration: \n\t The Aberration regains 10 hit points at the start of its turn if it has at least 1 hit point."


    ## Combat Actions
    if Type == "Aberration" and Dice() == 1:        r += "\n- Blinding Spittle (Recharge 5–6). \n\t The Aberration spits a chemical glob at a point it can see within 15 feet of it. The glob explodes in a blinding flash of light on impact. Each creature within 5 feet of the flash must succeed on a DC 13 Dexterity saving throw or be blinded until the end of the aberration's next turn."
    if Type == "Aberration" and Dice(7) == 1:       r += "\n- Aberrant Ground. \n\t  The ground in a 10-foot radius around the Aberration is doughlike difficult terrain. Each creature that starts its turn in that area must succeed on a DC 10 Strength saving throw or have its speed reduced to 0 until the start of its next turn.  "
    if Type == "Aberration" and Dice() == 1:        r += "\n- Spell Reflection. \n\t  If the Aberration makes a successful saving throw against a spell, or a spell attack misses it, the aberration can choose another creature (including the spellcaster) it can see within 30 feet of it. The spell targets the chosen creature instead of the aberration. If the spell forced a saving throw, the chosen creature makes its own save. If the spell was an attack, the attack roll is rerolled against the chosen creature"
    if Type == "Aberration" and Dice() == 1:        r += "\n- Body Thief. \n\t The intellect devourer initiates an Intelligence contest with an incapacitated humanoid within 5 feet of it that isn't protected by protection from evil and good. If it wins the contest, the intellect devourer magically consumes the target's brain, teleports into the target's skull, and takes control of the target's body. While inside a creature, the intellect devourer has total cover against attacks and other effects originating outside its host. The intellect devourer retains its Intelligence, Wisdom, and Charisma scores, as well as its understanding of Deep Speech, its telepathy, and its traits. It otherwise adopts the target's statistics. It knows everything the creature knew, including spells and languages. \n\t If the host body dies, the intellect devourer must leave it. A protection from evil and good spell cast on the body drives the intellect devourer out. The intellect devourer is also forced out if the target regains its devoured brain by means of a wish. By spending 5 feet of its movement, the intellect devourer can voluntarily leave the body, teleporting to the nearest unoccupied space within 5 feet of it. The body then dies, unless its brain is restored within 1 round."
    if Type == "Aberration" and Dice() == 1:        r += "\n- Aberrant Ground: \n\t The ground in a 10-foot radius around the Aberration is doughlike difficult terrain. Each creature that starts its turn in that area must succeed on a DC 10 Strength saving throw or have its speed reduced to 0 until the start of its next turn."
    if Type == "Aberration" and Dice() == 1:        r += "\n- Gibbering. \n\t The Aberration babbles incoherently while it can see any creature and isn't incapacitated. Each creature that starts its turn within 20 feet of the Aberration and can hear the gibbering must succeed on a DC 10 Wisdom saving throw. On a failure, the creature can't take reactions until the start of its next turn and rolls a d8 to determine what it does during its turn. On a 1 to 4, the creature does nothing. On a 5 or 6, the creature takes no action or bonus action and uses all its movement to move in a randomly determined direction. On a 7 or 8, the creature makes a melee attack against a randomly determined creature within its reach or does nothing if it can't make such an attack."
    if Type == "Aberration" and Dice() == 1:        r += "\n- Tentacles. \n\t Reach 10 ft., one creature. Hit: 7 (1d10 + 2) piercing damage, and the target must succeed on a DC [10+%CON] Constitution saving throw or be poisoned for 1 minute. The poisoned target is paralyzed, and it can repeat the saving throw at the start of each of its turns, ending the effect on a success. \n\t The target is also grappled (escape DC [10+%STR]). If the target is Medium or smaller, it is also restrained until this grapple ends. While grappling the target, the aberration has advantage on attack rolls against it and can 't use this attack against other targets. When the aberration moves, any Medium or smaller target it is grappling moves with it."
    if Type == "Aberration" and Dice() == 1:        r += "\n- Amphibious. \n\t The Aberration can breathe air and water."
    if Type == "Aberration":
        if Dice() == 1:         r += "\n- Multiattack. \n\t The Aberration makes two simple attacks."
        elif Dice() == 1:       r += "\n- Multiattack. \n\t The Aberration makes three simple attacks."

    if Type == "Aberration":
        if Dice() == 1:
            r = r + "\n- Detect Sentience: \n\t It can sense the presence and location of any creature within 300 feet of it that has an Intelligence of 3 or higher, regardless of interposing barriers, unless the creature is protected by a mind blank spell."
            if Dice() == 1:        r = r + "\n- Devour Intellect: \n\t It targets one creature it can see within 10 feet of it that has a brain. The target must succeed on a DC [10+%DEX] Intelligence saving throw against this magic or take 11 (2d10) psychic damage. Also on a failure, roll 3d6: If the total equals or exceeds the target's Intelligence score, that score is reduced to 0. The target is stunned until it regains at least one point of Intelligence."

    

    # AVENS
    if Type == "Aven":        r = r + "\n- Fly \n\t 50ft"
    if Type == "Aven" and Dice() == 1:        r += "\n- Ambusher"
    if Type == "Aven" and Dice() == 1:        r += "\n- Mimicry \n\t The Ravenfolk can mimic simple sounds it has heard, such as a person whispering, a baby crying, or an animal chittering. A creature that hears the sounds can tell they are imitations with a successful DC 10 Wisdom (Insight) check."

    # BEASTS and BEASTFOLK

    if Type == "Beastfolk": r += "\n - Speak with Animal \n\t The Beastfolk can communicate simple concepts to his affinity animal when it speaks in Beast language."


    ## Senses
    
    if (Type == "Beast" or Type == "Beastfolk"):
        if Dice(2) == 1:
            r = r + "\n- Darkvision."
            if Dice() == 1:   r += "\n\t 120 ft."
            elif Dice(3) == 1:   r += "\n\t 60 ft."
            else:               r += "\n\t 30 ft."
        elif Dice() == 1:
            r += "\n- Blindsight."
            if Dice(12) == 1:   r += "\n\t 120 ft."
            elif Dice() == 1:   r += "\n\t 60 ft."
            else:               r += "\n\t 30 ft."
            if Dice(4) == 1:
                r = r + "\n- Echolocation. \n\t The Beast can't use its blindsight while deafened."
                r = r + "\n- Keen Hearing. \n\t The beast has advantage on Wisdom (Perception) checks that rely on hearing."

    if Type == "Beast" or Type == "Beastfolk":
        if Dice() == 1:     r += "\n- Keen Senses\n\t The beast has advantage on Wisdom (Perception) checks that rely on sight, hearing, or smell."
        else:
            if Dice() == 1: r += "\n- Keen Smell. \n\t The Beast has advantage on Wisdom (Perception) checks that rely on smell."
            if Dice() == 1: r += "\n- Keen Sight. \n\tThe beast has advantage on Wisdom (Perception) checks that rely on sight."
            if Dice() == 1: r += "\n- Keen Hearing. \n\tThe beast has advantage on Wisdom (Perception) checks that rely on hearing."

    ## Movement
    if (Type == "Beast" or Type == "Beastfolk"):
        if Dice() == 1:         r += "\n- Speed. \t 20 ft."
        elif Dice() == 1:       r += "\n- Speed. \t 30 ft."
        elif Dice() == 1:       r += "\n- Speed. \t 40 ft."
        elif Dice() == 1:       r += "\n- Speed. \t 50 ft."

    if (Type == "Beast" or Type == "Beastfolk"):
        if Dice() == 1:        r = r + "\n- Climb. \t 30 ft."
        
    if (Type == "Beast" or Type == "Beastfolk"):        
        if Dice() == 1:        r = r + "\n- Burrow. \t 10 ft."

    if (Type == "Beast" or Type == "Beastfolk") and Dice(8) == 1:
        if Dice(2) == 1:
            r += "\n- Fly. \n\t 60 ft."
            if Dice(3) == 1:        r = r + "\n- Flyby. \n\t The beast doesn't provoke opportunity attacks when it flies out of an enemy's reach."
        elif Dice(2) == 1:
            r += "\n- Fly. \n\t 80 ft."
            if Dice() == 1:         r = r + "\n- Flyby. \n\t The beast doesn't provoke opportunity attacks when it flies out of an enemy's reach."

    if (Type == "Beast" or Type == "Beastfolk") and Dice(8) == 1:
        if Dice(2) == 1:    r += "\n- Water Breathing. The beast can breathe underwater"
        if Dice() == 1:     r += "\n- Swim. \t 60 ft."
        elif Dice() == 1:   r += "\n- Swim. \t 50 ft."
        elif Dice() == 1:   r += "\n- Swim. \t 40 ft."
        elif Dice() == 1:   r += "\n- Swim. \t 30 ft."
        else:               r += "\n- Swim. \t 20 ft."
        
        if Dice(4) == 1:    r += "\n- Underwater Camouflage. \n\t The beast has advantage on Dexterity (Stealth) checks made while underwater."

        if Dice() == 1:     r += "\n- Hold Breath. \n\t The beast can hold its breath for 15 minutes"
        elif Dice() == 1:   r += "\n- Hold Breath. \n\t The beast can hold its breath for 30 minutes"

        if Dice() == 1:
            r = r + "\n- Amphibious"
            if Dice() == 1:
                r = r + "\n- Standing Leap. \n\t The Beast's long jump is up to half his speed in feet and its high jump is up to third his speed, with or without a running start."

    if (Type == "Beast" or Type == "Beastfolk") and Dice(8) == 1:
        r += "\n- Spider Climb \n\t The beast can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."
        if Dice(2) == 1:    r += "\n- Web Sense \n\t While in contact with a web, the beast knows the exact location of any other creature in contact with the same web."
        if Dice(2) == 1:    r += "\n- Web Walker \n\t The beast ignores movement restrictions caused by webbing."
        if Dice(2) == 1:    r += "Web (Recharge 5–6). \n\t Ranged Weapon Attack: +4 to hit, range 30/60 ft., one Large or smaller creature. Hit: The creature is restrained by webbing. As an action, the restrained creature can make a DC 11 Strength check, escaping from the webbing on a success. The effect ends if the webbing is destroyed. The webbing has AC 10, 5 hit points, is vulnerable to fire damage and immune to bludgeoning, poison and psychic damage."


    ## Weaknesses and strengths
    if (Type == "Beast" or Type == "Beastfolk") and Dice(8) == 1:
        r += "\n- Damage Immunities. \t cold."
        if Dice(4) == 1:   r += "\n- Snow Camouflage. \t The beast has advantage on Dexterity (Stealth) checks made to hide in snowy terrain."

    if (Type == "Beast" or Type == "Beastfolk") and Dice(8) == 1:        r += "\n - Relentless \n\t (Recharges after a Short or Long Rest). \n\t If the beast takes 7 damage or less that would reduce it to 0 hit points, it is reduced to 1 hit point instead."

    if (Type == "Beast" or Type == "Beastfolk") and Dice() == 1:         r += "\n - Damage Immunities \n\t bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered."

    if (Type == "Beastfolk") and Dice(12) == 1:
        r += "\n - Sunlight Sensitivity. \n\t While in sunlight, the drider has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."

    if (Type == "Beastfolk") and Dice(12) == 1:
        r += "\n - Fey Ancestry \n\t The beastfolk has advantage on saving throws against being charmed, and magic can't put the beastfolk to sleep."


    ## Skills
    if (Type == "Beast" or Type == "Beastfolk") and Dice(8) == 1:         r = r + "\n- Illumination.\n\tThe beast sheds bright light in a 10-foot radius and dim light for an additional 10 ft."
    if (Type == "Beast" or Type == "Beastfolk") and Dice(8) == 1:         r = r + "\n- Sure-Footed \n\t The beast has advantage on Strength and Dexterity saving throws made against effects that would knock it prone."
    if (Type == "Beast" or Type == "Beastfolk") and Dice(8) == 1:         r = r + "\n- Hold Breath. \n\t The beast can hold its breath for 30 minutes."
    if (Type == "Beast" or Type == "Beastfolk") and Dice(10) == 1:        r = r + "\n- Mimicry \n\t The Beast can mimic simple sounds it has heard, such as a person whispering, a baby crying, or an animal chittering. A creature that hears the sounds can tell they are imitations with a successful DC 10 Wisdom (Insight) check."
    if (Type == "Beast" or Type == "Beastfolk") and Dice(10) == 1:        r = r + "\n- Beast of Burden \n\t The Beast is considered to be a Large animal for the purpose of determining its carrying capacity."
    if (Type == "Beast" or Type == "Beastfolk") and Dice(8) == 1:         r = r + "\n- Swamp Camouflage \n\t The Beast has advantage on Dexterity (Stealth) checks made to hide in swampy terrain."
    if (Type == "Beast" or Type == "Beastfolk") and Dice(8) == 1:         r = r + "\n- Labyrinthine Recall \n\t The Beast can perfectly recall any path it has traveled."


    ## Combat Skills
    if (Type == "Beast" or Type == "Beastfolk") and Dice(8) == 1:
        r += "\n-  Pack Tactics. \n\t The Beast has advantage on an attack roll against a creature if at least one of the beast's allies is within 5 feet of the creature and the ally isn't incapacitated."

    if (Type == "Beast" or Type == "Beastfolk"):
        if Dice() == 1:        r += "\n-  Multiattack. \n\t The Beast makes two simple attacks."
        elif Dice() == 1:      r += "\n-  Multiattack. \n\t The Beast makes three simple attacks."
        elif Dice() == 1:      r += "\n-  Multiattack. \n\t The Beast makes three simple attacks. It can replace two of those for a special attack."
        elif Dice(8) == 1:     r += "\n-  Multiattack. \n\t The Beast makes one special attack and a simple attacks."

    if (Type == "Beast" or Type == "Beastfolk") and Dice(9) == 1:
        r += "\n - Grappler. \n\t On an attack, the target is grappled,  [DC 10+%STR]"
        if Dice(2) == 1:    r += "\n - Constrict. \n\t Until the grapple ends, the creature is restrained. The creature can't constrict another creature."

    if (Type == "Beast" or Type == "Beastfolk"):
        if Dice(9) == 1:        r += "\n - Charge \n\t If the Beast moves at least 20 feet straight toward a target and then hits it with an attack on the same turn, the target takes an extra [2d6+%STR] bludgeoning damage. If the target is a creature, it must succeed on a DC=[10+%STR] Strength saving throw or be knocked prone."
        elif Dice(9) == 1:      r += "\n - Charge \n\t If the Beast moves at least 15 feet straight toward a target and then hits it with an attack on the same turn, the target takes an extra [2d6+%STR] slashing damage. If the target is a creature, it must succeed on a DC=[10+%STR] Strength saving throw or be knocked prone."
        elif Dice(9) == 1:      r += "\n - Charge \n\t If the Beast moves at least 10 feet straight toward a target and then hits it with an attack on the same turn, the target takes an extra [2d8+%STR] piercing damage. If the target is a creature, it must succeed on a DC=[10+%STR] Strength saving throw or be pushed up to 10 feet away and knocked prone."
        elif Dice(9) == 1:      r += "\n - Trampling Charge \n\t If the Beast moves at least 20 feet straight toward a creature and then hits it with an attack on the same turn, that target must succeed on a DC [10+%STR] Strength saving throw or be knocked prone. If the target is prone, the beast can make one simple attack against it as a bonus action."

    if (Type == "Beast" or Type == "Beastfolk"):
        if Dice(9) == 1:        r += "\n- Blood Frenzy \n\t The beast has advantage on melee attack rolls against any creature that doesn't have all its hit points."

    if (Type == "Beast" or Type == "Beastfolk"):
        if Dice(10) == 1:     r = r + "\n- Pounce \n\t If the beast moves at least 20 feet straight toward a creature and then hits it with an attack on the same turn, that target must succeed on a DC [10+%STR] Strength saving throw or be knocked prone. If the target is prone, the Beast can make one attack against it as a bonus action."
        elif Dice(10) == 1:   r = r + "\n- Pounce \n\t If the beast moves at least 15 feet straight toward a creature and then hits it with an attack on the same turn, that target must succeed on a DC [10+%STR] Strength saving throw or be knocked prone. If the target is prone, the Beast can make one attack against it as a bonus action."


    if (Type == "Beast" or Type == "Beastfolk"):
        if Dice(4) == 1:
            r = r + "\n- Bite. \n\t  Melee Weapon Attack: reach 5 ft., one  target. Hit: 4 (1d6 + %STR) piercing damage, and the target is grappled (escape DC 10 + %STR). Until this grapple ends, the target is restrained, and the beast can't bite another target."
            if Dice() == 1: r = r + "\n- Swallow. \n\t  The beast makes one bite attack against a target creature smaller than themselves it is grappling. If the attack hits, the target is swallowed, and the grapple ends. The swallowed target is blinded and restrained, it has total cover against attacks and other effects outside the beast, and it takes 6 (2d4+%CON) acid damage at the start of each of the beast's turns. The beast can have only one target swallowed at a time. If the beast dies, a swallowed creature is no longer restrained by it and can escape from the corpse using 5 feet of movement, exiting prone."
        elif Dice() == 1:   r = r + "\n- Bite. \n\t  Melee Weapon Attack: reach 5 ft., one target. Hit: 8 (2d6 + %STR) piercing damage, and the target is grappled (escape DC 10 + %STR). Until this grapple ends, the target is restrained, and the beast can't bite another target."
        elif Dice() == 1:        r = r + "\n- Bite. \n\t  Melee Weapon Attack: reach 5 ft., one target. Hit: 10 (3d6 + %STR) piercing damage, and the target is grappled (escape DC 10 + %STR). Until this grapple ends, the target is restrained, and the beast can't bite another target."
        elif Dice() == 1:        r = r + "\n- Bite. \n\t  Melee Weapon Attack: reach 5 ft., one target. Hit: 15 (4d6 + %STR) piercing damage, and the target is grappled (escape DC 10 + %STR)."
        elif Dice() == 1:        r = r + "\n- Bite. \n\t  Melee Weapon Attack: reach 5 ft., one target. Hit: 20 (5d6 + %STR) piercing damage, and the target is grappled (escape DC 10 + %STR)."
        elif Dice() == 1:        r = r + "\n- Bite. \n\t  Melee Weapon Attack: reach 5 ft., one target. Hit: 7 (1d10 + %STR) piercing damage, and the target is grappled (escape DC 10 + %STR) and the target must make a DC [10+%CON] Constitution saving throw, taking 18 (4d8) poison damage on a failed save, or half as much damage on a successful one. If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour, even after regaining hit points, and is paralyzed while poisoned in this way."
        elif Dice(8) == 1:       r = r + "\n- Bite. \n\t  Melee Weapon Attack: reach 5 ft., one target. Hit: 23 (3d10 + %STR) piercing damage."
        elif Dice(4) == 1:
            r += "\n- Bite. \n\t  Melee Weapon Attack: reach 5 ft., one target. Hit: 5 (1d8 + %STR) piercing damage, and the target is grappled (escape DC 10 + %STR) and the target must make a DC [10+%CON] Constitution saving throw, taking 18 (4d8) poison damage on a failed save, or half as much damage on a successful one. If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour, even after regaining hit points, and is paralyzed while poisoned in this way."
            r += "\n- Lycan Curse \n\t When a Bite attack hits, the target must succeed on a DC[10+%CON] Constitution saving throw or be cursed with the lycanthropy curse of the affinity beast."

    if (Type == "Beast" or Type == "Beastfolk") and Dice(12) == 1:      r += "\n- Hold Breath. \n\t  The beast can hold its breath for 15 minutes.\n- Swimming \n\t  speed of 30 feet."
    elif (Type == "Beast" or Type == "Beastfolk") and Dice(12) == 1:    r += "\n- Hold Breath. \n\t  The beast can hold its breath for 1 hour."
    if (Type == "Beast" or Type == "Beastfolk") and Dice(12) == 1:      r += "\n- Rampage. \n\t When the Beast reduces a creature to 0 hit points with a melee attack on its turn, the beast can take a bonus action to move up to half its speed and make a bite attack."
    if (Type == "Beast" or Type == "Beastfolk") and Dice(12) == 1:      r += "\n- Slippery. \n\t The beast has advantage on ability checks and saving throws made to escape a grapple."
    if (Type == "Beast" or Type == "Beastfolk") and Dice() == 1:        r += "\n- Sunlight Sensitivity.  \n\t While in sunlight, the beastfolk has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."

    if Type == "Beastfolk" and Dice() == 1:     r += "\n - Damage Immunities \n\t Bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered."
    if Type == "Beastfolk" and Dice() == 1:     r += "\n - Beast Telepathy \n\t The Beastfolk can magically command any animal it shares an affinity to within 120 feet of it, using a limited telepathy."
    if Type == "Beastfolk" and Dice() == 1:     r += "\n - Shapechanger \n\t The Beastfolk can use its action to polymorph into a specific Medium humanoid or a Beast-humanoid hybrid, or into its beast form. Other than its size, its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies."
    if Type == "Beastfolk" and Dice() == 1:     r += "\n - Pack Tactics \n\t The Beastfolk has advantage on an attack roll against a creature if at least one of the Beastfolk's allies is within 5 feet of the creature and the ally isn't incapacitated."
    if Type == "Beastfolk" and Dice() == 1:     r += "\n - Rampage.\n\t When the beastfolk reduces a creature to 0 hit points with a melee attack on its turn, the beastfolk can take a bonus action to move up to half its speed and make a bite attack."
    if Type == "Beastfolk" and Dice() == 1:     r += "\n - Chameleon Skin \n\t The beastfolk has advantage on Dexterity (Stealth) checks made to hide."
    if Type == "Beastfolk" and Dice(8) == 1:    r += "\n - Wounded Fury \n\t While it has 10 hit points or fewer, the beastfolk has advantage on attack rolls. In addition, it deals an extra 7 (2d6) damage to any target it hits with a melee attack."
    if Type == "Beastfolk" and Dice() == 1:     r += "\n - Multiattack \n\t The Beastfolk can make two different simple attacks."
    if Type == "Beastfolk" and Dice(8) == 1:    r += "\n - Otherworldly Perception \n\t The Beastfolk can sense the presence of any creature within 30 feet of it that is invisible or on the Ethereal Plane. It can pinpoint such a creature that is moving."
    if Type == "Beastfolk" and Dice(8) == 1:    r += "\n - Reckless \n\t At the start of its turn, the berserker can gain advantage on all melee weapon attack rolls during that turn, but attack rolls against it have advantage until the start of its next turn."


    # BERSERKER
    if Type == "Berserker" and Dice(2) == 1:    r += "\n- Multiattack \n\t The berserker makes two simple melee attacks."
    if Type == "Berserker" and Dice(2) == 1:    r += "\n- Reckless \n\t At the start of its turn, the berserker can gain advantage on all melee weapon attack rolls during that turn, but attack rolls against it have advantage until the start of its next turn."

    # CELESTIALS

    ## Senses
    if Type == "Celestial" and Dice() == 1:     r += "\n- Truesight \t 120ft."

    ## Movement
    if Type == "Celestial" and Dice() == 1:     r += "\n- Fly \t 90ft."
    elif Type == "Celestial" and Dice() == 1:   r += "\n- Fly \t 60ft."
    elif Type == "Celestial" and Dice() == 1:   r += "\n- Fly \t 30ft."

    ## Strengths and Weaknesses
    if Type == "Celestial" and Dice() == 1:     r += "\n- Damage Resistances: \t Radiant."
    if Type == "Celestial" and Dice() == 1:     r += "\n- Damage Immunities: \t Psychic."
    if Type == "Celestial" and Dice() == 1:     r += "\n- Damage Immunities: \t Bludgeoning, Piercing, and slashing from nonmagical attacks."

    if Type == "Celestial" and Dice() == 1:     r += "\n- Magic Resistance: \t The Celestial's has advantage on saving throws against magical effects."
    if Type == "Celestial" and Dice() == 1:     r += "\n- Magic Weapons: \t The Celestial's attacks are magical."
    if Type == "Celestial" and Dice() == 1:     r += "\n- Shielded Mind \t The Celestial is immune to any effect that would sense its emotions, read its thoughts, or detect its location."

    ## Actions
    if Type == "Celestial" and Dice() == 1:     r += "\n- Change Shape. \n\t The Celestial magically polymorphs into a humanoid or beast that has a challenge rating equal to or less than 4, or back into its true form. It reverts to its true form if it dies. Any equipment it is wearing or carrying is absorbed or borne by the new form (the celestial's choice). \n\t In a new form, the celestial retains its game statistics and ability to speak, but its AC, movement modes, Strength, Dexterity, and other actions are replaced by those of the new form, and it gains any statistics and capabilities (except class features, legendary actions, and lair actions) that the new form has but that it lacks. The Celestial can still use its special attacks."

    ## Combat skills
    if Type == "Celestial" and Dice() == 1:     r += "\n- Multiattack: \t The Celestial's can attack once with a Special Attack and once with a Simple Attack."


    # CRIMINALS
    if Type == "Criminal" and Dice() == 1:  r += "\n- Pack Tactics \n\t The Criminal has advantage on an attack roll against a creature if at least one of the Criminal's allies is within 5 feet of the creature and the ally isn't incapacitated."

    # CONSTRUCTS

    # Senses
    if Type == "Construct":
        if Dice() == 1:     r += "\n- Dark Vision:\n\t 60 ft"
        elif Dice() == 1:   r += "\n- Blindsight:\n\t 60 ft (blind beyond this radius)"
        elif Dice() == 1:   r += "\n- Blindsight:\n\t 60 ft"
        elif Dice() == 1:   r += "\n- Truesight:\n\t 60 ft"
        elif Dice() == 1:   r += "\n- Truesight:\n\t 120 ft"

    # Strengths and Weaknesses
    if Type == "Construct":
        if Dice() == 1:     r += "\n- Damage Resistances: Bludgeoning, piercing, and slashing from nonmagical attacks that aren't adamantine."
        if Dice() == 1:     r += "\n- Damage Immunities: Force"
        if Dice() == 1:     r += "\n- Damage Immunities: Necrotic"
        r += "\n- Damage Immunities: Poison"
        if Dice() == 1:     r += "\n- Damage Immunities: Psychic"
        if Dice() == 1:     r += "\n- Condition Immunities: Blinded"
        r += "\n- Condition Immunities: Charmed"
        if Dice() == 1:     r += "\n- Condition Immunities: Feafened"
        if Dice() == 1:     r += "\n- Condition Immunities: Exhaustion"
        if Dice() == 1:     r += "\n- Condition Immunities: Frightened"
        if Dice() == 1:     r += "\n- Condition Immunities: Paralyzed"
        if Dice() == 1:     r += "\n- Condition Immunities: Petrified"
        r += "\n- Condition Immunities: Poisoned"
        if Dice() == 1:     r += "\n- Condition Immunities: Stunned"

    # Skills
    if Type == "Construct":   
        if Dice() == 1:     r += "\n- Antimagic Susceptibility:\n\t The Construct is incapacitated while in the area of an antimagic field. If targeted by dispel magic, the Construct must succeed on a Constitution saving throw against the caster's spell save DC or fall unconscious for 1 minute."
        if Dice() == 1:     r += "\n- Axiomatic Mind. \n\t The Construct can't be compelled to act in a manner contrary to its nature or its instructions."
        if Dice() == 1:     r += "\n- Disintegration. \n\t If the Construct dies, its body disintegrates into dust, leaving behind its weapons and anything else it was carrying."
        if Dice() == 1:     r += "\n- Damage Transfer:\n\t While it is grappling a creature, the construct takes only half the damage dealt to it, and the creature grappled by the rug takes the other half."
        if Dice() == 1:     r += "\n- False Apperance \n\t While the Construct remains motionless in rest, it is indistinguishable from a mundane object"
        if Dice() == 1:     r += "\n- Magic Resistance \n\t The Construct has advantage on saving throws against spells and other magical effects."
        if Dice() == 1:     r += "\n- Smother. \n\t Melee Weapon Attack: +5 to hit, reach 5 ft., one Medium or smaller creature. Hit: The creature is grappled (escape DC 13). Until this grapple ends, the target is restrained, blinded, and at risk of suffocating, and the construct can't smother another target. In addition, at the start of each of the target's turns, the target takes 10 (2d6 + 3) bludgeoning damage."
        if Dice() == 1:     r += "\n- Spell Immunity. \n\t The construct is immune to three spells chosen by its creator. Typical immunities include fireball, heat metal, and lightning bolt."
        if Dice() == 1:     r += "\n- Telepathic Bond:\n\t While the Construct is on the same plane of existence as its master, it can magically convey what it senses to its master, and the two can communicate telepathically."
        if Dice() == 1:     r += "\n- Terrifying Glare:\n\t The Construct is incapacitated while in the area of an antimagic field. If targeted by dispel magic, the Construct must succeed on a Constitution saving throw against the caster's spell save DC or fall unconscious for 1 minute."
        if Dice() == 1:     r += "\n- Aversion of Fire:\n\t If the golem takes fire damage, it has disadvantage on attack rolls and ability checks until the end of its next turn."
        if Dice() == 1:     r += "\n- Berserk:\n\t Whenever the golem starts its turn with 40 hit points or fewer, roll a d6. On a 6, the golem goes berserk. On each of its turns while berserk, the golem attacks the nearest creature it can see. If no creature is near enough to move to and attack, the golem attacks an object, with preference for an object smaller than itself. Once the golem goes berserk, it continues to do so until it is destroyed or regains all its hit points. \n\t The golem's creator, if within 60 feet of the berserk golem, can try to calm it by speaking firmly and persuasively. The golem must be able to hear its creator, who must take an action to make a DC 15 Charisma (Persuasion) check. If the check succeeds, the golem ceases being berserk. If it takes damage while still at 40 hit points or fewer, the golem might go berserk again."
        if Dice() == 1:     r += "\n- Immutable Form:\n\t The golem is immune to any spell or effect that would alter its form."
        if Dice() == 1:     r += "\n- Lightning Absorption:\n\t Whenever the golem is subjected to lightning damage, it takes no damage and instead regains a number of hit points equal to the lightning damage dealt."
        if Dice() == 1:     r += "\n- Magic Weapons:\n\t The golem's weapon attacks are magical."


        



    #Dragons
    ## Movement
    if Type == "Dragon" and Dice(4) == 1:
        r = r + "\n- Fly: 60 ft"
        if Dice() == 1:     r += "\n- Flyby \n\t The dragon is an agile flier, quick to fly out of enemies' reach. The dragon doesn't provoke an opportunity attack when it flies out of an enemy's reach."

    if Type == "Dragon" and Dice() == 1:
        r = r + "\n- Burrow: 15 ft"
        if Dice() == 1: r = r + "\n- Tremorsense: 60 ft"

    if Type == "Dragon" and Dice() == 1:    r = r + "\n- Climb: 30 ft"

    if Type == "Dragon" and Dice(3) == 1:
        r += "\n- Swim: 30ft."
        if Type == "Dragon" and Dice(4) == 1:   r = r + "\n - Amphibious \n\t The dragon can breathe air and water."

    ## Senses
    if Type == "Dragon":
        if Dice(2) == 1:    r = r + "\n- Darkvision: 60 ft"
        if Dice(2) == 1:    r = r + "\n- Blindsight: 10 ft"
        elif Dice() == 1:   r = r + "\n- Blindsight: 60 ft"
        elif Dice() == 1:   r = r + "\n- Truesight: 10 ft"
        elif Dice() == 1:   r = r + "\n- Truesight: 60 ft"

    if Type == "Dragon" and Dice() == 1:    r += "\n- Keen Senses \n\t The Dragon has advantage on Wisdom (Perception) checks that rely on sight, hearing, or smell."
    if Type == "Dragon" and Dice() == 1:    r += "\n- Limited Telepathy \n\t The Dragon can magically communicate simple ideas, emotions, and images telepathically with any creature within 100 feet of it that can understand a language. It can also communicate with any Dragon"

    ## Strengths and Weaknesses
    if Type == "Dragon" and Dice() == 1:    r += "\n- Magic Resistance \n\t The Dragon has advantage on saving throws against spells and other magical effects."

    if Type == "Dragon" and Dice() == 1:    r += "\n- Damage Immunities: Fire"
    if Type == "Dragon" and Dice() == 1:    r += "\n- Damage Immunities: Lightning"
    if Type == "Dragon" and Dice() == 1:    r += "\n- Damage Immunities: Poison"
    if Type == "Dragon" and Dice() == 1:    r += "\n- Damage Immunities: Acid"

    if Type == "Dragon" and Dice() == 1:    r += "\n- Condition Immunities: Poisoned"

    ## Skills
    if Type == "Dragon" and Dice() == 1:    r += "\n- Superior Invisibility \n\t  The Dragon magically turns invisible until its concentration ends (as if concentrating on a spell). Any equipment the Dragon wears or carries is invisible with it."
    if Type == "Dragon" and Dice() == 1:    r += "\n- Mimicry \n\t The dragon can mimic any sounds it has heard, including voices. A creature that hears the sounds can tell they are imitations with a successful DC [10+%CHA] Wisdom (Insight) check."
    if Type == "Dragon" and Dice(12) == 1:  r += "\n- Rejuvenation \n\t You might decide that dragons in your campaign, being an essential part of the Material Plane, are nearly impossible to destroy. A dragon's life essence might be preserved in the egg from which it first emerged, in its hoard, or in a cavernous hall at the center of the world, just as a lich's essence is hidden in a phylactery. \n\t If it has an essence-preserving object, a destroyed dragon gains a new body in 1d10 days, regaining all its hit points and becoming active again. The new body appears within 5 feet of the object."


    if Type == "Fey" and Dice() == 1:   r += "\n- Magic Resistance \n\t The Fey has advantage on saving throws against spells and other magical effects."
    if Type == "Fey" and Dice() == 1:   r += "\n- Superior Invisibility \n\t  The Fey magically turns invisible until its concentration ends (as if concentrating on a spell). Any equipment the Fey wears or carries is invisible with it."
    if Type == "Fey" and Dice() == 1:   r += "\n- Amphibious \n\t  The Fey can breath air and water."
    if Type == "Fey" and Dice() == 1:   r += "\n- Mimicry \n\t The Fey can mimic animal sounds and humanoid voices. A creature that hears the sounds can tell they are imitations with a successful DC [10+%CHA] Wisdom (Insight) check."
    if Type == "Fey" and Dice() == 1:
        r += "\n- Horrific Appearance \n\t  Any humanoid that starts its turn within 30 feet of the Fey and can see the Fey's true form must make a DC 11 Wisdom saving throw. On a failed save, the creature is frightened for 1 minute. A creature can repeat the saving throw at the start of each of its turns, with disadvantage if the Fey is within line of sight, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the Fey's Horrific Appearance for the next 24 hours. \n\t Unless the target is surprised or the revelation of the Fey's true form is sudden, the target can avert its eyes and avoid making the initial saving throw. Until the start of its next turn, a creature that averts its eyes has disadvantage on attack rolls against the Fey."
        if Dice() == 1: r += "\n- Death Glare. \n\t The fey targets one frightened creature she can see within 30 feet of themselves. If the target can see the fey, it must succeed on a DC 11 Wisdom saving throw against this magic or drop to 0 hit points."
    if Type == "Fey" and Dice() == 1:   r += "\n- Illusory Appearance \n\t  The fey covers herself and anything they are wearing or carrying with a magical illusion that makes her look like other creature of their general size and humanoid shape. The effect ends if the fey takes a bonus action to end it or if they dies. \n\t The changes wrought by this effect fail to hold up to physical inspection. For example, a hag could appear to have no claws, but someone touching her hand might feel the claws. Otherwise, a creature must take an action to visually inspect the illusion and succeed on a DC [10+2·%CHA] Intelligence (Investigation) check to discern that the fey is disguised."
    if Type == "Fey" and Dice() == 1:   r += "\n- Invisible Passage \n\t  The Fey magically turns invisible until they attack or cast a spell, or until their concentration ends (as if concentrating on a spell). While invisible, they leave no physical evidence of their passage, so they can be tracked only by magic. Any equipment they wear or carry is invisible with them."

    if Type == "Fey" and Dice() == 1:   r += "Night Hag Items. \n\t A night hag carries two very rare magic items that she must craft for herself. If either object is lost, the night hag will go to great lengths to retrieve it, as creating a new tool takes time and effort. \n\t - Heartstone: This lustrous black gem allows a night hag to become ethereal while it is in her possession. The touch of a heartstone also cures any disease. Crafting a heartstone takes 30 days. \n\t -Soul Bag: When an evil humanoid dies as a result of a night hag's Nightmare Haunting, the hag catches the soul in this black sack made of stitched flesh. A soul bag can hold only one evil soul at a time, and only the night hag who crafted the bag can catch a soul with it. Crafting a soul bag takes 7 days and a humanoid sacrifice (whose flesh is used to make the bag)."

    # ELFS
    if Type == "Elf":   r += "\n - Fey Ancestry.\n\t The Elf has advantage on saving throws against being charmed, and magic can't put the Elf to sleep."

    if Type == "Elf":
        if Dice(4) <= 3:
            r = r + "\n- Darkvision \n\t 60ft"
        else:
            r = r + "\n- Darkvision \n\t 120ft"
            r = r + "\n- Sunlight Sensitivity. \n\t While in sunlight, the Elf has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."


    # ELEMENTALS
    ## Movement

    if Type == "Elemental" and Dice() == 1: r += "\n - Fly : 30ft."

    if Type == "Elemental" and Dice() == 1: r += "\n - Burrow : 30ft."

    if Type == "Elemental" and Dice() == 1:     r += "\n - Swim : 30ft."
    elif Type == "Elemental" and Dice() == 1:   r += "\n - Swim : 60ft."

    if Type == "Elemental" and Dice() == 1: r += " Air Form. \n\t The elemental can enter a hostile creature's space and stop there. It can move through a space as narrow as 1 inch wide without squeezing."

    if Type == "Elemental" and Dice() == 1: r += " Water Form. \n\t The elemental can enter a hostile creature's space and stop there. It can move through a space as narrow as 1 inch wide without squeezing."

    ## Senses
    if Type == "Elemental" and Dice() == 1:     r += "\n - Darkvision : 60ft."

    if Type == "Elemental" and Dice() == 1:     r += "\n - Blindsight : 30ft."

    if Type == "Elemental" and Dice() == 1:     r += "\n - Tremorsense : 60ft."

    ## Strengths and Weaknesses

    if Type == "Elemental" and Dice() == 1: r += "\n - Damage Resistances: Acid"

    if Type == "Elemental" and Dice() == 1:
        r += "\n - Damage Resistances: bludgeoning, piercing, and slashing from nonmagical attacks"
    elif Type == "Elemental" and Dice() == 1:
        r += "\n - Damage Resistances: bludgeoning, piercing, and slashing from nonmagical attacks that aren't adamantine."

    if Type == "Elemental" and Dice() == 1:     r += "\n - Damage Resistances: fire"
    elif Type == "Elemental" and Dice() == 1:   r += "\n - Damage Immunities: fire"
    elif Type == "Elemental" and Dice() == 1:   r += "\n - Damage Vulnerabilities: fire"

    if Type == "Elemental" and Dice() == 1:     r += "\n - Damage Resistances: lightning"

    if Type == "Elemental" and Dice(4) == 1:    r += "\n - Damage Immunities: poison"
    
    if Type == "Elemental" and Dice() == 1:     r += "\n - Damage Resistances: thunder"
    elif Type == "Elemental" and Dice() == 1:   r += "\n - Damage Vulnerabilities: thunder"

    if Type == "Elemental" and Dice() == 1: r += "\n - Damage Vulnerabilities: cold"
    
    if Type == "Elemental" and Dice() == 1: r += "\n - Condition Immunities: Exhaustion"
    if Type == "Elemental" and Dice() == 1: r += "\n - Condition Immunities: Grappled"
    if Type == "Elemental" and Dice() == 1: r += "\n - Condition Immunities: Paralyzed"
    if Type == "Elemental" and Dice() == 1: r += "\n - Condition Immunities: Petrified"
    if Type == "Elemental" and Dice() == 1: r += "\n - Condition Immunities: Poisoned"
    if Type == "Elemental" and Dice() == 1: r += "\n - Condition Immunities: Prone"
    if Type == "Elemental" and Dice() == 1: r += "\n - Condition Immunities: Restrained"
    if Type == "Elemental" and Dice() == 1: r += "\n - Condition Immunities: Unconscious"

    if Type == "Elemental" and Dice() == 1: r += "\n - Freeze: If the elemental takes cold damage, it partially freezes; its speed is reduced by 20 feet until the end of its next turn."

    ## Combat Skills
    if Type == "Elemental" and Dice() == 1:     r += "\n - Multiattack \n\t The elemental makes two simple attacks."
    elif Type == "Elemental" and Dice() == 1:   r += "\n - Multiattack \n\t The elemental makes three simple attacks."

    if Type == "Elemental" and Dice() == 1:
        r += "\n -Charge \n\t If the elemental moves at least 20 feet straight toward a target and then hits it with a simple attack on the same turn, the target takes an extra 7 (2d6) bludgeoning damage. If the target is a creature, it must succeed on a DC 16 Strength saving throw or be knocked prone."
        
    if Type == "Elemental" and Dice() == 1:     r += "\n - Earth Glide \n\t The elemental can burrow through nonmagical, unworked earth and stone. While doing so, the elemental doesn't disturb the material it moves through."
    if Type == "Elemental" and Dice() == 1:     r += "\n - False Appereance. \n\t While motionless, the elemental is indistinguishable from a natural feature, such as ponds, rocks, statues, campfires, etc"
    if Type == "Elemental" and Dice() == 1:     r += "\n - Fire Form \n\t The elemental can move through a space as narrow as 1 inch wide without squeezing. A creature that touches the elemental or hits it with a melee attack while within 5 feet of it takes 5 (1d10) fire damage. In addition, the elemental can enter a hostile creature's space and stop there. The first time it enters a creature's space on a turn, that creature takes 5 (1d10) fire damage and catches fire; until someone takes an action to douse the fire, the creature takes 5 (1d10) fire damage at the start of each of its turns."
    elif Type == "Elemental" and Dice() == 1:   r += "\n - Fire Form \n\t The elemental can move through a space as narrow as 1 inch wide without squeezing. A creature that touches the elemental or hits it with a melee attack while within 5 feet of it takes 10 (2d10) fire damage. In addition, the elemental can enter a hostile creature's space and stop there. The first time it enters a creature's space on a turn, that creature takes 5 (1d10) fire damage and catches fire; until someone takes an action to douse the fire, the creature takes 5 (1d10) fire damage at the start of each of its turns."
    if Type == "Elemental" and Dice() == 1:     r += "\n - Fire Touch \n\t Melee Weapon Attack \t Hit: 10 (2d6 + %CON) fire damage. If the target is a creature or a flammable object, it ignites. Until a creature takes an action to douse the fire, the target takes 5 (1d10) fire damage at the start of each of its turns."
    if Type == "Elemental" and Dice() == 1:     r += "\n - Heated Body \n\t A creature that touches the Elemental or hits it with a melee attack while within 5 feet of it takes 3 (1d6) fire damage"
    elif Type == "Elemental" and Dice() == 1:   r += "\n - Heated Body \n\t Any metal melee weapon the elemental wields deals an extra 3 (1d6) fire damage on a hit (included in the attack)."
    if Type == "Elemental" and Dice() == 1:     r += "\n - Heated Weapons \n\t A creature that touches the Elemental or hits it with a melee attack while within 5 feet of it takes 7 (2d6) fire damage"
    if Type == "Elemental" and Dice(8) == 1:    r += "\n - Illumination.\n\t The beast sheds bright light in a 10-foot radius and dim light for an additional 10 ft."
    elif Type == "Elemental" and Dice() == 1:   r += "\n - Illumination \n\t The elemental sheds bright light in a 30-foot radius and dim light in an additional 30 feet."
    elif Type == "Elemental" and Dice() == 1:   r += "\n - Ignited Illumination. \n\t As a bonus action, the Elemental can set itself ablaze or extinguish its flames. While ablaze, the Elemental sheds bright light in a 10-foot radius and dim light for an additional 10 feet."
    if Type == "Elemental" and Dice() == 1:     r += "\n - Invisible in Water \n\t The Elemental is invisible while fully immersed in water."
    if Type == "Elemental" and Dice() == 1:     r += "\n - Siege Monster \n\t The elemental deals double damage to objects and structures."
    if Type == "Elemental" and Dice() == 1:     r += "\n - Stone Camouflage. \n\t The elemental has advantage on Dexterity (Stealth) checks made to hide in rocky terrain."
    if Type == "Elemental" and Dice() == 1:     r += "\n - Treasure Sense. \n\t The elemental can pinpoint, by scent, the location of precious metals and stones, such as coins and gems, within 60 feet of it."
    if Type == "Elemental" and Dice() == 1:     r += "\n - Water Susceptibility \n\t For every 5 feet the elemental moves in water, or for every gallon of water splashed on it, it takes 1 cold damage."
    if Type == "Elemental" and Dice() == 1:     r += "\n - Water Bound \n\t The Elemental dies if it leaves the water body to which it is bound or if that water is destroyed."
    if Type == "Elemental" and Dice() == 1:     r += "\n - Whelm (Recharge 4–6). \n\t Each creature in the elemental's space must make a DC 15 Strength saving throw. On a failure, a target takes 13 (2d8 + 4) bludgeoning damage. If it is Large or smaller, it is also grappled (escape DC 14). Until this grapple ends, the target is restrained and unable to breathe unless it can breathe water. If the saving throw is successful, the target is pushed out of the elemental's space. \n\t The elemental can grapple one Large creature or up to two Medium or smaller creatures at one time. At the start of each of the elemental's turns, each target grappled by it takes 13 (2d8 + 4) bludgeoning damage. A creature within 5 feet of the elemental can pull a creature or object out of it by taking an action to make a DC 14 Strength check and succeeding."



    
    if Type == "Elemental":
        if Dice() == 1:
            r = r + "\n - Death Burst: \n\t When the Elemental dies, it leaves behind a burst of elemental essence that fills a 5-foot-radius sphere centered on its space. \n\t"
            rdm = Dice(4)
            if rdm == 1:    r += "The sphere is heavily obscured. Wind disperses the cloud, which otherwise lasts for 1 minute."
            if rdm == 2:    r += "Each creature in range must succeed on a DC [10+%Cha] Constitution Saving Throw or be blinded for 1 minute."
            if rdm == 3:    r += "Each creature in range must succeed on a DC [10+%Cha] Constitution Saving Throw or take 4 (1d8) slashing damage on a failed save, or half as much on a successful one."
            if rdm == 4:    r += "Each creature in range must succeed on a DC [10+%Con] Constitution Saving Throw or take 7 (2d6) fire damage on a failed save, or half as much on a successful one. Flammable objects that aren't being worn or carried in that area are ignited."



    # FEY
    if Type == "Fey" and Dice(8) == 1:  r += "\n- Invisibility \n\t The Fey magically turns invisible until it attacks, or until its concentration ends (as if concentrating on a spell). Any equipment the Fey wears or carries is invisible with it."
    if Type == "Fey" and Dice(8) == 1:  r += "\n- Speak with Beasts and Plants \n\t The Fey can communicate with beasts and plants as if they shared a language."
    if Type == "Fey" and Dice(8) == 1:  r += "\n- Tree Stride \n\t Once on her turn, the Fey can use 10 feet of her movement to step magically into one living tree within her reach and emerge from a second living tree within 60 feet of the first tree, appearing in an unoccupied space within 5 feet of the second tree. Both trees must be large or bigger."
    if Type == "Fey" and Dice(8) == 1:  r += "\n- Fey Charm \n\t The Fey targets one humanoid or beast that she can see within 30 feet of her. If the target can see the Fey, it must succeed on a DC [10+Cha] Wisdom saving throw or be magically charmed. The charmed creature regards the Fey as a trusted friend to be heeded and protected. Although the target isn't under the Fey's control, it takes the Fey's requests or actions in the most favorable way it can. Each time the Fey or its allies do anything harmful to the target, it can repeat the saving throw, ending the effect on itself on a success. Otherwise, the effect lasts 24 hours or until the Fey dies, is on a different plane of existence from the target, or ends the effect as a bonus action. If a target's saving throw is successful, the target is immune to the Fey's Fey Charm for the next 24 hours. The Fey can have no more than one humanoid and up to three beasts charmed at a time."

    # GIANTS
    
    ## Senses
    if Type == "Giant" and Dice(2) == 1: r += "\n Darkvision: 60ft"
        
    if Type == "Giant" and Dice() == 1: r += "\n Keen Smell \n\t The giant has advantage on Wisdom (Perception) checks that rely on smell."

    if Type == "Giant" and Dice() == 1: r += "\n Poor Depth Perception. \n\t  The giant has disadvantage on any attack roll against a target more than 30 feet away."
    
    
    ## Movement
    if Type == "Giant" and Dice() == 1:     r += "\n Speed: 40ft"

    ## Skills
    if Type == "Giant" and Dice() == 1:     r += "\n Two Heads \n\t The giant has advantage on Wisdom (Perception) checks and on saving throws against being blinded, charmed, deafened, frightened, stunned, and knocked unconscious."

    if Type == "Giant" and Dice() == 1:     r += "\n Regeneration \n\t The giant regains 10 hit points at the start of its turn. If the giant takes acid or fire damage, this trait doesn't function at the start of the giant's next turn. The giant dies only if it starts its turn with 0 hit points and doesn't regenerate."
    elif Type == "Giant" and Dice() == 1:   r += "\n Regeneration \n\t The giant regains 10 hit points at the start of its turn. If the giant takes " + Damage() + " damage, this trait doesn't function at the start of the giant's next turn. The giant dies only if it starts its turn with 0 hit points and doesn't regenerate."

    ## Combat
    if Type == "Giant" and Dice() == 1:     r += "\n Multiattack \n\t The giant makes two simple attacks."
    
    if Type == "Giant" and Dice() == 1:     r += "\n Greatclub \n\t reach 10 ft., one target. Hit: 18 (3d8 + %STR) bludgeoning damage."

    if Type == "Giant":
        if Dice() == 1:     r += "\n Rock \n\t range 30/120 ft., one target. Hit: 28 (4d10 + %STR) bludgeoning damage."
        elif Dice() == 1:   r += "\n Rock \n\t range 60/240 ft., one target. Hit: 21 (3d10 + %STR) bludgeoning damage."
    if Type == "Giant" and Dice() == 1:     r += "\n Squash \n\t Some giants like to hurl themselves bodily at smaller foes and crush them beneath their bulk. Melee Weapon Attack: Reach 5 ft., one Medium or Smaller creature. Hit: 26 (6d6 + %STR) bludgeoning damage, the giant lands prone in the target's space, and the target is grappled (escape DC 10+%STR). Until this grapple ends, the target is prone. The grapple ends early if the giant stands up."


    # GNOME
    if Type == "Gnome": r += "\n - Gnome Cunning \n\t The gnome has advantage on Intelligence, Wisdom, and Charisma saving throws against magic."
    if Type == "Gnome": r += "\n - Stone Camouflage \n\t The gnome has advantage on Dexterity (Stealth) checks made to hide in rocky terrain."

    if Type == "Goblin" and Dice() == 1:    r += "\n- Nimble Scape \n\t The goblin can take the Disengage or Hide action as a bonus action on each of its turns."
    if Type == "Goblin" and Dice() == 1:    r += "\n- Martial Advantage \n\t Once per turn, the Goblin can deal an extra 7 (2d6) damage to a creature it hits with a weapon attack if that creature is within 5 feet of an ally of the goblin that isn't incapacitated."
    elif Type == "Goblin" and Dice(10) == 1:r += "\n- Martial Advantage \n\t Once per turn, the Goblin can deal an extra 10 (3d6) damage to a creature it hits with a weapon attack if that creature is within 5 feet of an ally of the goblin that isn't incapacitated."
    if Type == "Goblin" and Dice() == 1:    r += "\n- Brute \n\t A melee weapon deals one extra die of its damage when the Goblin hits with it (included in the attack)."
    if Type == "Goblin" and Dice() == 1:    r += "\n- Surprise Attack \n\t If the Goblin surprises a creature and hits it with an attack during the first round of combat, the target takes an extra 7 (2d6) damage from the attack."
    if Type == "Goblin" and Dice(8) == 1:   r += "\n- Redirect Attack (Reaction) \n\t When a creature the goblin can see targets it with an attack, the goblin chooses another goblin within 5 feet of it. The two goblins swap places, and the chosen goblin becomes the target instead."
    if Type == "Goblin" and Dice() == 1:    r += "\n- Multiattack \n\t The goblin makes two Simple Attacks attacks. The second attack has disadvantage."
    elif Type == "Goblin" and Dice() == 1:  r += "\n- Multiattack \n\t The goblin makes two Simple Attacks attacks."
    if Type == "Goblin" and Dice() == 1:    r += "\n- Heart of Hruggek \n\t The goblin has advantage on saving throws against being charmed, frightened, paralyzed, poisoned, stunned, or put to sleep."

    if Type == "Knight" and Dice() == 1:    r += "\n- Brave \n\t The knight has advantage on saving throws against being frightened."
    if Type == "Knight" and Dice() == 1:    r += "\n- Parry \n\t The knight adds 2 to its AC against one melee attack that would hit it. To do so, the knight must see the attacker and be wielding a melee weapon."

    # LIZARDFOLK
    # Movement
    if Type == "Lizardfolk":    r += "\n - Hold Breath \n\t The lizardfolk can hold its breath for 15 minutes."
    if Type == "Lizardfolk" and Dice(2) == 1:   r += "\n - Spider Climb. \n\t The lizard can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."
    if Type == "Lizardfolk" and Dice(2) == 1:   r += "\n - Swim. \t 30 ft."

    # Senses
    if Type == "Lizardfolk" and Dice(2) == 1:   r += "\n - Darkvision. \t 60 ft."

    # Combat Skills
    if Type == "Lizardfolk" and Dice(2) == 1:   r += "\n - Chameleon Skin \n\t The lizard has advantage on Dexterity (Stealth) checks made to hide."    
    if Type == "Lizardfolk" and Dice() == 1:    r += "\n - Skewer.  \n\t Once per turn, when the lizardfolk makes a Melee attack and hits, the target takes an extra 10 (3d6) damage, and the lizardfolk gains temporary hit points equal to the extra damage dealt."
    if Type == "Lizardfolk" and Dice() == 1:    r += "\n - Stench.  \n\t Any creature other than a Lizardfolk that starts its turn within 5 feet of the Lizardfolk must succeed on a DC [10+%CON] Constitution saving throw or be poisoned until the start of the creature's next turn. On a successful saving throw, the creature is immune to the stench of all Lizardfolk for 1 hour."
    if Type == "Lizardfolk" and Dice() == 1:    r += "\n - Sunlight Sensitivity.  \n\t While in sunlight, the lizardfolk has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."

    
    # Strengths and weaknesses 
    if Type == "Lizardfolk":
        if Dice() == 1: r += "\n - Condition Immunities \t Frightened"

    if Type == "Ooze":
        if Dice(7) == 1:
            r = r + "\n- Amorphous \n\t The ooze can move through a space as narrow as 1 inch wide without squeezing."
        elif Dice() == 1:
            r += "\n- Ooze Cube \n\t The cube takes up its entire space. Other creatures can enter the space, but a creature that does so is subjected to the cube's Engulf and has disadvantage on the saving throw. Creatures inside the cube can be seen but have total cover. A creature within 5 feet of the cube can take an action to pull a creature or object out of the cube. Doing so requires a successful DC 12 Strength check, and the creature making the attempt takes 10 (3d6) acid damage. The cube can hold only one Large creature or up to four Medium or smaller creatures inside it at a time."
            r += "\n- Engulf. \n\t The cube moves up to its speed. While doing so, it can enter Large or smaller creatures' spaces. Whenever the cube enters a creature's space, the creature must make a DC 12 Dexterity saving throw. On a successful save, the creature can choose to be pushed 5 feet back or to the side of the cube. A creature that chooses not to be pushed suffers the consequences of a failed saving throw. On a failed save, the cube enters the creature's space, and the creature takes 10 (3d6) acid damage and is engulfed. The engulfed creature can't breathe, is restrained, and takes 21 (6d6) acid damage at the start of each of the cube's turns. When the cube moves, the engulfed creature moves with it. An engulfed creature can try to escape by taking an action to make a DC 12 Strength check. On a success, the creature escapes and enters a space of its choice within 5 feet of the cube."

    if Type == "Ooze" and Dice() == 1:
        r = r + "\n- Corrode Material: Any nonmagical weapon made of the material that hits the ooze corrodes. After dealing damage, the weapon takes a permanent and cumulative −1 penalty to damage rolls. If its penalty drops to −5, the weapon is destroyed. Nonmagical ammunition made of the material that hits the ooze is destroyed after dealing damage. The ooze can eat through 2-inch-thick, nonmagical material in 1 round. On a hit from the Ooze, if the target is wearing nonmagical armor of the material, its armor is partly corroded and takes a permanent and cumulative −1 penalty to the AC it offers. The armor is destroyed if the penalty reduces its AC to 10."
        if Dice() == 1: r = r + "\n\t Wood"
        if Dice() == 1: r = r + "\n\t Metal"
        if Dice() == 1: r = r + "\n\t Meat & Leather"
        if Dice() == 1: r = r + "\n\t Iron"
        if Dice() == 1: r = r + "\n\t Gold"
        if Dice() == 1: r = r + "\n\t Silver"

    if Type == "Ooze" and Dice() == 1:
        r += "\n- Split: Under the effect of certain damage types, the ooze may split in two, making a new ooze. The new Ooze has half(rounded down) hit points of the original ooze, and their size is Small. The original ooze must be 10hp or higher. "
        if Dice(2) == 1:    r += "\n\t - Slashing"
        if Dice() == 1:     r = r + "\n\t - (Yellow): Lightning"
        if Dice() == 1:     r = r + "\n\t - (Red): Fire"
        if Dice() == 1:     r = r + "\n\t - (Black): Necrotic"
        if Dice() == 1:     r = r + "\n\t - (Green): Poison"

    if Type == "Ooze" and Dice() == 1:  r = r + "\n- False Appearance \n\t While the ooze remains motionless, it is indistinguishable from an oily pool, wet rock, or a normal enviromental object"
    if Type == "Ooze" and Dice() == 1:  r = r + "\n- Transparent \n\t The Ooze has advantage on stealth checks against creatures without tremorsense or blindsight."
    if Type == "Ooze" and Dice() == 1:  r = r + "\n- Spider Climb \n\t The ooze can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."

    if Type == "Ooze" and Dice() == 1:  r = r + "\n- Damage Resistance: Acid"
    if Type == "Ooze" and Dice() == 1:  r = r + "\n- Damage Resistance: Cold"
    if Type == "Ooze" and Dice() == 1:  r = r + "\n- Damage Resistance: Fire"
    if Type == "Ooze" and Dice() == 1:  r = r + "\n- Condition Immunities: Blinded"
    if Type == "Ooze" and Dice() == 1:  r = r + "\n- Condition Immunities: Charmed"
    if Type == "Ooze" and Dice() == 1:  r = r + "\n- Condition Immunities: Deafened"
    if Type == "Ooze" and Dice() == 1:  r = r + "\n- Condition Immunities: Exhaustion"
    if Type == "Ooze" and Dice() == 1:  r = r + "\n- Condition Immunities: Frightened"
    if Type == "Ooze" and Dice() == 1:  r = r + "\n- Condition Immunities: Prone"

    if Type == "Ooze" and Dice() == 1:  r = r + "\n- Speed: 20 ft"
    if Type == "Ooze" and Dice() == 1:  r = r + "\n- Climb: 20 ft"

    # ORCS
    # Senses
    if Type == "Orc":   r += "\n- Darkvision \t 60ft."

    # Combat Skills
    if Type == "Orc":
        r += "\n- Aggressive \n\t As a bonus action, the orc can move up to its speed toward a hostile creature that it can see."
        r += "\n- Orkish Fury \n\t The Orc deals an extra 4(1d8) damage when it hits with a simple weapon attack."
    if Type == "Orc" and Dice():   r += "\n- Battle Cry (1/Day). \n\t Each creature of the orc's choice that is within 30 feet of it, can hear it, and not already affected by Battle Cry gain advantage on attack rolls until the start of the war chief's next turn. The war chief can then make one attack as a bonus action."


    if Type == "Explorer" and Dice() == 1:  r += "\n- Keen Senses\n\t The Explorer has advantage on Wisdom (Perception) checks that rely on senses."

    # PLANTS

    ## Weaknesses and Strengths
    
    if Type == "Plant" and Dice() == 1:     r += "\n- Damage Resistance: Bludgeoning"
    if Type == "Plant" and Dice() == 1:     r += "\n- Damage Resistance: Cold"

    if Type == "Plant": r += "\n- Damage Vulnerabilities: Fire"
    
    if Type == "Plant" and Dice(9) == 1:    r += "\n- Damage Immunities: Lightning"
    if Type == "Plant" and Dice() == 1:     r += "\n- Damage Immunities: Poison"
    if Type == "Plant" and Dice() == 1:     r += "\n- Damage Resistance: Piercing"
    
    if Type == "Plant" and Dice() == 1: r = r + "\n- Condition Immunities: Blinded"
    if Type == "Plant" and Dice() == 1: r = r + "\n- Condition Immunities: Charmed"
    if Type == "Plant" and Dice() == 1: r = r + "\n- Condition Immunities: Deafened"
    if Type == "Plant" and Dice(9) == 1: r = r + "\n- Condition Immunities: Exhaustion"
    if Type == "Plant" and Dice() == 1: r = r + "\n- Condition Immunities: Frightened"
    if Type == "Plant" and Dice() == 1: r = r + "\n- Condition Immunities: Poisoned"
    if Type == "Plant" and Dice() == 1: r = r + "\n- Condition Immunities: Prone"
    if Type == "Plant" and Dice() == 1: r = r + "\n- Condition Immunities: Paralyzed"

    ## Combat Skill
    if Type == "Plant" and Dice() == 1:        r += "\n- Entangling Plants. \n\t Grasping roots and vines sprout in a 15-foot radius centered on the blight, withering away after 1 minute. For the duration, that area is difficult terrain."
    if Type == "Plant" and Dice() == 1:        r += "\n- Engulf \n\t The plant engulfs a Medium or smaller creature grappled by it. The engulfed target is blinded, restrained, and unable to breathe, and it must succeed on a DC [10+%STR] Constitution saving throw at the start of each of the plant's turns or take 8 (2d8 + %STR) bludgeoning damage. If the plant moves, the engulfed target moves with it. The plant can have only one creature engulfed at a time."
    if Type == "Plant" and Dice(3) == 1:       r += "\n- False Appereance: \n\t While the plant remains motionless, it is indistinguishable from a normal plant."
    if Type == "Plant" and Dice(9) == 1:       r += "\n- Lightning Absorption: \n\t Whenever the plant is subjected to lightning damage, it takes no damage and regains a number of hit points equal to the lightning damage dealt."


    if Type == "Plant" and Dice() == 1:         r += "\n- Multiattack: \n\t The plant makes two simple attacks."
    elif Type == "Plant" and Dice() == 1:       r += "\n- Multiattack: \n\t The plant makes two simple attacks. If both hit a Medium or smaller creature, the target is grappled (escape DC[10+%STR])"


    # SNAKEFOLK
    if Type == "Snakefolk":                     r += "\n- Darkvision: 60 ft"
    if Type == "Snakefolk":                     r += "\n- Damage Immunities \t Poison"
    if Type == "Snakefolk":                     r += "\n- Condition Immunities \t Poisoned"
    if Type == "Snakefolk" and Dice(3) == 1:    r += "\n- Magic Resistance \n\t The Snakefolk has advantage on saving throws against spells and other magical effects."
    if Type == "Snakefolk" and Dice() == 1:     r += "\n- Shapechanger \n\t The Snakefolk can use its action to polymorph into a Medium snake, or back into its true form. Its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It doesn't change form if it dies."
    if Type == "Snakefolk" and Dice() == 1:     r += "\n- Multiattack \n\t The Snakefolk makes two ranged attacks or two melee attacks."
    if Type == "Snakefolk" and Dice() == 1:     r += "\n- Constrict \n\t Melee Weapon Attack, reach 5 ft., one target. Hit: 10 (2d6 + 3) bludgeoning damage, and the target is grappled (escape DC [10+%STR]). Until this grapple ends, the target is restrained, and the Snakefolk can't constrict another target."

    if Type == "Spy":   r += "\n- Superior Invisibility"

    if Type == "Bandit" and Dice(2) == 1:   r = r + "\n- Pack Tactics \n\t The Bandit has advantages on attack on targets within 5ft of an ally of the bandit."
    if Type == "Bandit" and Dice(2) == 1:   r = r + "\n- Multiattack \n\t The Bandit makes three simple melee attacks. Or the Bandit makes two ranged or special attacks."
    if Type == "Bandit" and Dice(2) == 1:   r = r + "\n- Parry (Reaction) \n\t The Bandit adds 2 to its AC against one melee attack that would hit it. To do so, the bandit must see the attacker and be wielding a melee weapon."

    if Type == "Dwarf":     r = r + "\n- Damage Resistance: Poison"

    if Type == "Dwarf":
        if Dice() == 1:     r = r + "\n- Darkvision: 60ft"
        else:               r = r + "\n- Darkvision: 120ft"

    if Type == "Dwarf" and Dice() == 1:
        r = r + "\n- Duergar Resilience. \n\t The Dwarf has advantage on saving throws against poison, spells, and illusions, as well as to resist being charmed or paralyzed."
        r = r + "\n- Sunlight Sensitivity \n\t While in sunlight, the Dwarf has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."

    if Type == "Cultist" and Dice(2) == 1:  r = r + "\n Dark Devotion.\n\t The cultist has advantage on saving throws against being charmed or frightened."
    if Type == "Cultist" and Dice(2) == 1:  r = r + "\n Multiattack.\n\t The cultist makes two simple melee attacks."

    # FIENDS

    # Senses
    if Type == "Fiend":
        if Dice(2) == 1:    r += "\n- Darkvision: \t 60 ft."
        elif Dice(2) == 1:  r += "\n- Darkvision: \t 120 ft."
        
        if Dice() == 1:     r += "\n- Blindsight: \t 10 ft."
        elif Dice() == 1:   r += "\n- Blindsight: \t 30 ft."
        elif Dice() == 1:   r += "\n- Blindsight: \t 60 ft."
        
        if Dice() == 1:     r += "\n- Devil's Sight. \n\t Magical darkness doesn't impede the Fiend's darkvision."

    if Type == "Fiend" and Dice(12) == 1:   r += "\n- Keen Hearing and Smell. \n\t The fiend has advantage on Wisdom (Perception) checks that rely on hearing or smell."

    # Movement
    if Type == "Fiend":
        if Dice() == 1:     r += "\n- Speed: 20 ft."
        elif Dice() == 1:   r += "\n- Speed: 30 ft."
        elif Dice() == 1:   r += "\n- Speed: 40 ft."

    if Type == "Fiend":
        if Dice() == 1:     r += "\n- Fly: 20 ft."
        elif Dice() == 1:   r += "\n- Fly: 30 ft."
        elif Dice() == 1:   r += "\n- Fly: 40 ft."
        elif Dice() == 1:   r += "\n- Fly: 60 ft."

    if Type == "Fiend":
        if Dice() == 1:     r += "\n- Climb: 40 ft."

    if Type == "Fiend" and Dice(10) == 1:
        r += "\n- Incorporeal Movement. \n\t The demon can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object."

    if Type == "Fiend" and Dice(10) == 1:
        r += "\n- Teleport. \n\t The fiend magically teleports, along with any equipment it is wearing or carrying, up to 60 feet to an unoccupied space it can see."

    if Type == "Fiend" and Dice(10) == 1:
        r += "\n- Spider Climb. \n\t The fiend can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."


    # Strengths and Weaknesses
    if Type == "Fiend":
        if Dice() == 1:     r += "\n- Damage Vulnerabilities: Radiant"
    
        if Dice() == 1:     r += "\n- Damage Resistances: acid"
        elif Dice() == 1:     r += "\n- Damage Immunities: acid"

        if Dice() == 1:     r += "\n- Damage Resistances: bludgeoning, piercing, and slashing from nonmagical attacks not made with silvered weapons."
        elif Dice() == 1:   r += "\n- Damage Resistances: bludgeoning, piercing, and slashing from nonmagical attacks."

        if Dice() == 1:     r += "\n- Damage Resistances: cold"
        elif Dice() == 1:   r += "\n- Damage Immunities: cold"
    
        if Dice() == 1:     r += "\n- Damage Resistances: fire"
        elif Dice() == 1:   r += "\n- Damage Immunities: fire"

        if Dice() == 1:     r += "\n- Damage Resistances: necrotic"

        if Dice() == 1:     r += "\n- Damage Resistances: lightning"
        elif Dice() == 1:   r += "\n- Damage Immunities: lightning"

        if Dice() == 1:     r += "\n- Damage Resistances: poison"
        elif Dice() == 1:   r += "\n- Damage Immunities: poison"

        if Dice() == 1:     r += "\n- Damage Resistances: thunder"

    if Type == "Fiend":
        if Dice() == 1:    r += "\n- Condition Immunities: charmed"
        if Dice() == 1:    r += "\n- Condition Immunities: exhaustion"
        if Dice() == 1:    r += "\n- Condition Immunities: frightened"
        if Dice() == 1:    r += "\n- Condition Immunities: grappled"
        if Dice() == 1:    r += "\n- Condition Immunities: paralyzed"
        if Dice() == 1:    r += "\n- Condition Immunities: petrified"
        if Dice() == 1:    r += "\n- Condition Immunities: poisoned"
        if Dice() == 1:    r += "\n- Condition Immunities: prone"
        if Dice(10) == 1:  r += "\n- Condition Immunities: restrained"

    if Type == "Fiend" and Dice() == 1: r = r + "\n- Magic Resistance \n\t The fiend has advantage on saving throws against spells and other magical effects."

    if Type == "Fiend" and Dice() == 1: r = r + "\n- Light Sensitivity \n\t While in bright light, the demon has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."

    # Skills
    if Type == "Fiend":
        if Dice() == 1:     r = r + "\n- Shapechanger \n\t The fiend can use its action to polymorph into a beast form that resembles a rat (speed 20 ft.), a raven (20 ft., fly 60 ft.), or a spider (20 ft., climb 20 ft.), or back into its true form. Its statistics are the same in each form, except for the speed changes noted. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies."
        elif Dice() == 1:   r = r + "\n- Shapechanger \n\t The fiend can use its action to polymorph into a beast form that resembles a bat (speed 10 feet fly 40 ft.), a centipede (40 ft., climb 40 ft.), or a toad (40 ft., swim 40 ft.), or back into its true form. Its statistics are the same in each form, except for the speed changes noted. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies."
    if Type == "Fiend" and Dice() == 1:    r += "\n- Invisibility. \n\t The fiend magically turns invisible until it attacks, or until its concentration ends (as if concentrating on a spell). Any equipment the fiend wears or carries is invisible with it."
    if Type == "Fiend" and Dice() == 1:    r += "\n- Shadow Stealth. \n\t While in dim light or darkness, the demon can take the Hide action as a bonus action."
    if Type == "Fiend" and Dice() == 1:    r += "\n- Etherealness. \n\t The fiend magically enters the Ethereal Plane from the Material Plane, or vice versa."


    # Combat
    if Type == "Fiend" and Dice() == 1:         r += "\n- Hellish Rejuvenation. \n\t A Fiend that dies in the Nine Hells comes back to life with all its hit points in " + str(Dice(10)) + " days unless it is killed by a good-aligned creature with a bless spell cast on that creature or its remains are sprinkled with holy water."
    if Type == "Fiend" and Dice() == 1:         r += "\n- Multiattack. \n\t The fiend makes two simple melee attacks."
    if Type == "Fiend" and Dice(12) == 1:       r += "\n- Rampage. \n\t When the Beast reduces a creature to 0 hit points with a melee attack on its turn, the beast can take a bonus action to move up to half its speed and make a bite attack."
    if Type == "Fiend" and Dice() == 1:         r += "\n- Steadfast. \n\t The fiend can't be frightened while it can see an allied creature within 30 feet of it."
    if Type == "Fiend" and Dice(12) == 1:       r += "\n- Reckless. \n\t At the start of its turn, the fiend can gain advantage on all melee weapon attack rolls it makes during that turn, but attack rolls against it have advantage until the start of its next turn."
    if Type == "Fiend" and Dice(12) == 1:       r += "\n- Running Leap. \n\t The fiend's long jump is up to 40 feet and its high jump is up to 20 feet when it has a running start"
    if Type == "Fiend" and Dice(12) == 1:       r += "\n- Fiendish Blessing. \n\t Add the Charisma modifier bonus to the Fiend's AC"
    if Type == "Fiend" and Dice(12) == 1:       r += "\n- Horned One's Call. \n\t When the fiend targets only one creature within all their turn's attacks, it can choose one ally it can see within 30 feet. That ally can use its reaction to make one melee attack against a target of its choice."
    if Type == "Fiend" and Dice(12) == 1:       r += "\n- Spawn of the Grave. \n\t At the end of each of the fiend's turns, each undead of its choice that it can see within 30 feet gains 10 temporary hit points, provided the fiend isn't incapacitated. \n\t In addition, this fiend can use its Innate Spellcasting ability to cast animate dead three times per day."
    if Type == "Fiend" and Dice(12) == 1:       r += "\n- Magic Weapons. \n\t The fiend's weapon attacks are magical."
    if Type == "Fiend" and Dice(12) == 1:       r += "\n- Fiendish Noise. \n\t The fiend produces a horrid sound to which demons are immune. Any other creature that starts its turn with in 30 feet of the fiend must succeed on a DC[11+%CON] Constitution saving throw or fall unconscious for 10 minutes. A creature that can't hear the drone automatically succeeds on the save. The effect on the creature ends if it takes damage or if another creature takes an action to splash it with holy water. If a creature's saving throw is successful or the effect ends for it, it is immune to the noise for the next 24 hours."
    
    if Type == "Fiend" and Dice(12) == 1:       r += "\n- Life Consumtion. \n\t A simple attack deals an extra damage 24 (7d6) necrotic damage, and the target's hit point maximum is reduced by an amount equal to the necrotic damage taken. If this effect reduces a creature's hit point maximum to 0, the creature dies. This reduction to a creature's hit point maximum lasts until the creature finishes a long rest or until it is affected by a spell like greater restoration."



    # MONK
    if Type == "Monk" and Dice(2) == 1:        r = r + "\n- Multiattack. \n\t The monk makes two attacks."


    # MONSTROSITIES
    # Senses
    if Type == "Monstrosity":
        if Dice() == 1:
            r += "\n - Darkvision: 60 ft.\n"
        
        if Dice() == 1:
            r += "\n - Blindsight: 30 ft.\n"
        elif Dice() == 1:
            r += "\n - Blindsight: 60 ft.\n"
            if Dice() == 1:
                r += "\n - Echolocation: The monster can't use its blindsight while deafened.\n"
                r += "\n - Keen Hearing: The monster has advantage on Wisdom (Perception) checks that rely on hearing.\n"

        if Dice() == 1: r += "\n - Tremorsense: 60 ft.\n"
            
    if Type == "Monstrosity":
        if Dice() == 1:
            r += "\n- Keen Sight.\n\t The monstrosity has advantage on Wisdom (Perception) checks that rely on sight.\n"

        if Dice() == 1:
            r += "\n- Keen Smell.\n\t The monstrosity has advantage on Wisdom (Perception) checks that rely on smell.\n"

    # Movement
    if Type == "Monstrosity":
        if Dice() == 1:            r += "\n - Speed: 50 ft"
        elif Dice() == 1:          r += "\n - Speed: 40 ft"
        elif Dice() == 1:          r += "\n - Speed: 30 ft"
        else:                      r += "\n - Speed: 20 ft"
        
    if Type == "Monstrosity" and Dice()==1:
        if Dice() == 1:         r += "\n - Burrow: \t 40 ft"
        elif Dice() == 1:       r += "\n - Burrow: \t 20 ft"
        else:                   r += "\n - Burrow: \t 10 ft"
        if Dice() == 1:         r += "\n - Tunneler: \t The monstrosity can burrow through solid rock at half its burrowing speed and leaves a 5 foot-wide, 8-foot-high tunnel in its wake."

    if Type == "Monstrosity":
        if Dice() == 1:         r += "\n- Speed: 0 ft. \n- Fly: 20 ft(Hover)"
        elif Dice() == 1:       r += "\n- Fly: 30 ft"
        elif Dice() == 1:       r += "\n- Fly: 40 ft"
        elif Dice() == 1:
            r += "\n - Fly: 60 ft"
            if Dice(3) == 1:       r += "\n- Dive Attack: \n\t If the monster is flying and dives at least 30 feet straight toward a target and then hits it with a melee weapon attack, the attack deals an extra 9 (2d8) damage to the target."
            if Dice(3) == 1:       r += "\n- Flyby: \n\t If the monster doesn't provoke an opportunity attack when it flies out of an enemy's reach."

    if Type == "Monstrosity" and Dice() == 1:   r += "\n- Spider Climb.\n\t The Monstrosity can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check.\n"

    # Strengths and weaknesses
    if Type == "Monstrosity":
        if Dice() == 1:   r += "\n- Damage Immunities: \t cold"
        if Dice() == 1:   r += "\n- Damage Immunities: \t fire"
        
    if Type == "Monstrosity" and Dice() == 1:   r += "\n- Fear of Fire. \n\t If the Monstrosity takes fire damage, it has disadvantage on attack rolls and ability checks until the end of its next turn."

    # Fight skills
    if Type == "Monstrosity" and Dice() == 1:        r += "\n- Avoidance.\n\t If the Monstrosity is subjected to an effect that allows it to make a saving throw to take only half damage, it instead takes no damage if it succeeds on the saving throw, and only half damage if it fails.\n"
    if Type == "Monstrosity" and Dice() == 1:        r += "\n- Ambusher.\n\t In the first round of a combat, the Monstrosity has advantage on attack rolls against any creature it surprised.\n"
    if Type == "Monstrosity" and Dice() == 1:        r += "\n- Displacement.\n\t The Monstrosity projects a magical illusion that makes it appear to be standing near its actual location, causing attack rolls against it to have disadvantage. If it is hit by an attack, this trait is disrupted until the end of its next turn. This trait is also disrupted while the displacer beast is incapacitated or has a speed of 0.\n"
    if Type == "Monstrosity" and Dice(8) == 1:       r += "\n- Deadly Leap.\n\t  If the monstrosity jumps at least 15 feet as part of its movement, it can then use this action to land on its feet in a space that contains one or more other creatures. Each of those creatures must succeed on a DC [11+%STR] Strength or Dexterity saving throw (target's choice) or be knocked prone and take 14 (3d6 + %STR) bludgeoning damage plus 14 (3d6 + %STR) slashing damage. On a successful save, the creature takes only half the damage, isn't knocked prone, and is pushed 5 feet out of the monster's space into an unoccupied space of the creature's choice. If no unoccupied space is within range, the creature instead falls prone in the monster's space."
    if Type == "Monstrosity" and Dice() == 1:        r += "\n- False Appearance \n\t While the Monstrosity remains motionless, it is indistinguishable from a natural element, ordinary object, or innofensive creature."
    if Type == "Monstrosity" and Dice() == 1:        r += "\n- Grappler. \n\t On a simple melee attack, the target is grappled,  [DC 10+%STR]"
    if Type == "Monstrosity" and Dice() == 1:        r += "\n- Heated Body. \n\t A creature that touches the monstrosity or hits it with a melee attack while within 5 feet of it takes 7 (2d6) fire damage."
    if Type == "Monstrosity" and Dice() == 1:        r += "\n- Intoxicating Touch. \n\t On a simple melee attack, The target is magically cursed for 1 hour. Until the curse ends, the target has disadvantage on Wisdom saving throws and all ability checks."
    if Type == "Monstrosity":
        if Dice() == 1:
            r += "\n- Multiattack. \n\t The monstrosity makes two Simple attacks."
        elif Dice() == 1:
            r += "\n- Multiattack. \n\t The monstrosity makes three Simple attacks."
    if Type == "Monstrosity":
        if Dice() == 1:        r += "\n- Shapechanger \n\t The monstrosity can use its action to polymorph into an object or back into its true, amorphous form. Its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies."
        elif Dice() == 1:      r += "\n- Shapechanger \n\t The monstrosity can use its action to polymorph into a Small or Medium humanoid it has seen, or back into its true form. Its statistics, other than its size, are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies."
    if Type == "Monstrosity" and Dice() == 1:        r += "\n- Surprise Attack \n\t  If the monstrosity surprises a creature and hits it with an attack during the first round of combat, the target takes an extra 10 (3d6) damage from the attack."
    if Type == "Monstrosity" and Dice() == 1:        r += "\n- Stone Camouflage.\n\t The monstrosity has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.\n"
    if Type == "Monstrosity" and Dice() == 1:        r += "\n- Snow Camouflage. \n\t The Monstrosity has advantage on Dexterity (Stealth) checks made to hide in snowy terrain."
    if Type == "Monstrosity" and Dice() == 1:        r += "\n- Two-Headed. \n\t The monstrosity has advantage on Wisdom (Perception) checks and on saving throws against being blinded, charmed, deafened, frightened, stunned, or knocked unconscious."

    # Special Attacks.
    
    if Type == "Monstrosity" and Dice() == 1:
        r += "\n- Multiattack. \n\t The monstrosity makes three simple attacks."

    if Type == "Monstrosity" and Dice(9) == 1: r += "\n- Bite. \n\t Reach 5ft. Hit: 30 (4d12 + %STR) piercing damage. "
    elif Type == "Monstrosity" and Dice() == 1: r += "\n- Bite. \n\t Reach 5ft. Hit: 9 (dd8 + %STR) slashing damage. "

    if Type == "Monstrosity" and Dice() == 1:
        r += "\n- Tendril. \n\t Melee Weapon Attack: Reach 50 ft., one creature. Hit: The target is grappled (escape DC [11+%STR]). Until the grapple ends, the target is restrained and has disadvantage on Strength checks and Strength saving throws, and the monstrosity can't use the same tendril on another target."
        if Dice() == 1: r += "\n- Grasping Tendrils. \n\t The monstrosity can have up to [1d6] tendrils at a time. Each tendril can be attacked (AC 20; 10 hit points; immunity to poison and psychic damage). Destroying a tendril deals no damage to the monstrosity, which can extrude a replacement tendril on its next turn. A tendril can also be broken if a creature takes an action and succeeds on a DC 15 Strength check against it."
        if Dice() == 1: r += "\n-  Reel. \n\t The roper pulls each creature grappled by it up to 25 feet straight toward it."


    # RANGER. 
    if Type == "Ranger":        r += "\n- " + Attack("RangedMartial")
    if Type == "Ranger":        r += "\n - Multiattack. \n\t The Ranger can do two ranged attacks."

    if Type == "Priest" and Dice(2) == 1:        r += "\n- Divine Eminence. \n\t As a bonus action, the priest can expend a spell slot to cause its melee weapon attacks to magically deal an extra 10 (3d6) radiant damage to a target on a hit. This benefit lasts until the end of the turn. If the priest expends a spell slot of 2nd level or higher, the extra damage increases by 1d6 for each level above 1st."

    if Type == "Shaman" and Dice(2) == 1:        r += "\n- Change Shape: \n\t The Shaman magically polymorphs into a Beast, remaining in that form for up to 1 hour. It can revert to its true form as a bonus action. Its statistics, other than its size, are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies."

    if Type == "Soldier":        r += "\n- " + Attack("Martial")
    if Type == "Soldier":        r += "\n - Multiattack \n\t The Soldier can do two martial attacks and one simple attack."

    if Type == "Spy" and Dice(2) == 1:        r = r + "\n- Cunning Action \n\t On each of its turns, the spy can use a bonus action to take the Dash, Disengage, or Hide action."
    if Type == "Spy" and Dice(2) == 1:        r = r + "\n- Sneak Attack (1/Turn). \n\t The spy deals an extra 7 (2d6) damage when it hits a target with a weapon attack and has advantage on the attack roll, or when the target is within 5 feet of an ally of the spy that isn't incapacitated and the spy doesn't have disadvantage on the attack roll."
    if Type == "Spy" and Dice(2) == 1:        r = r + "\n- Multiattack. \n\t The spy makes two simple melee attacks."

    if Type == "Kobold":        r += "\n- Darkvision \t 60ft."
    if Type == "Kobold":        r += "\n- Pack Tactics \n\t The kobold has advantage on an attack roll against a creature if at least one of the kobold's allies is within 5 feet of the creature and the ally isn't incapacitated."
    if Type == "Kobold":        r += "\n- Sunlight Sensitivity \n\t While in sunlight, the kobold has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."
    if Type == "Kobold" and Dice() == 1:        r += "\n Fly \t 30ft."

    # UNDEADS

    # Movement
    if Type == "Undead" and Dice() == 1:    r = r + "\n- Speed: 0 \n- Fly: 40 ft (hover)"
    if Type == "Undead" and Dice() == 1:    r = r + "\n- Spider Climb. \n\t The undead can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."

    # Senses
    if Type == "Undead":
        if Dice(2) == 1:        r = r + "\n- Darkvision: 60ft"
        elif Dice(2) == 1:      r = r + "\n- Darkvision: 120ft"

    # Weaknesses and Strengths

    if Type == "Undead" and Dice() == 1:        r += "\n- Damage Resistances: Acid."
    
    if Type == "Undead" and Dice() == 1:        r += "\n- Damage Resistances: Bludgeoning, piercing, and slashing from nonmagical attacks. "
    elif Type == "Undead" and Dice() == 1:      r += "\n- Damage Vulnerabilities: Bludgeoning."
    elif Type == "Undead" and Dice() == 1:      r += "\n- Damage Resistances: Piercing. "

    if Type == "Undead" and Dice() == 1:        r += "\n- Damage Resistances: Cold. "
    elif Type == "Undead" and Dice() == 1:      r += "\n- Damage Immunities: Cold "

    if Type == "Undead" and Dice() == 1:        r += "\n- Damage Vulnerabilities: Fire"
    elif Type == "Undead" and Dice() == 1:      r += "\n- Damage Resistances: Fire."
    elif Type == "Undead" and Dice() == 1:      r += "\n- Damage Immunities: Fire "

    if Type == "Undead" and Dice() == 1:        r += "\n- Damage Resistances: Lightning. "

    if Type == "Undead" and Dice() == 1:        r += "\n- Damage Resistances: Necrotic."
    elif Type == "Undead" and Dice(2) == 1:     r += "\n- Damage Immunities: Necrotic "

    if Type == "Undead" and Dice(2) == 1:       r += "\n- Damage Resistances: Psychic "
    if Type == "Undead" and Dice(2) == 1:       r += "\n- Damage Immunities: Psychic "
    
    if Type == "Undead" and Dice() == 1:        r += "\n- Damage Resistances: Poison "
    elif Type == "Undead" and Dice() == 1:      r += "\n- Damage Immunities: Poison "
    
    if Type == "Undead" and Dice(3) == 1:       r += "\n- Damage Vulnerabilities: Radiant"

    if Type == "Undead" and Dice() == 1:        r += "\n- Damage Resistances: Thunder. "


    if Type == "Undead" and Dice() == 1:    r += "\n- Condition Immunities: Charmed"
    if Type == "Undead" and Dice() == 1:    r += "\n- Condition Immunities: Exhaustion"
    if Type == "Undead" and Dice() == 1:    r += "\n- Condition Immunities: Grappled"
    if Type == "Undead" and Dice() == 1:    r += "\n- Condition Immunities: Frightened"
    if Type == "Undead" and Dice() == 1:    r += "\n- Condition Immunities: Paralyzed"
    if Type == "Undead" and Dice() == 1:    r += "\n- Condition Immunities: Petrified"
    if Type == "Undead" and Dice() == 1:    r += "\n- Condition Immunities: Poisoned"
    if Type == "Undead" and Dice() == 1:    r += "\n- Condition Immunities: Prone"
    if Type == "Undead" and Dice() == 1:    r += "\n- Condition Immunities: Restrained"
    if Type == "Undead" and Dice() == 1:    r += "\n- Condition Immunities: Stunned"
    if Type == "Undead" and Dice() == 1:    r += "\n- Condition Immunities: Unconscious"

    if Type == "Undead" and Dice() == 1:    r += "\n- Magic Resistance \n\t The undead has advantage on saving throws against spells and other magical effects."
    if Type == "Undead":
        if Dice() == 1:     r += "\n- Regeneration\n\t The undead regains 10 hit points at the start of its turn. If the undead takes fire or radiant damage, this trait doesn't function at the start of the undead's next turn. The undead's body is destroyed only if it starts its turn with 0 hit points and doesn't regenerate."
        elif Dice() == 1:   r += "\n- Regeneration\n\t The undead regains 10 hit points at the start of its turn if it has at least 1 hit point and isn't in sunlight or running water. If the undead takes radiant damage or damage from holy water, this trait doesn't function at the start of the undead's next turn."
    if Type == "Undead" and Dice() == 1:    r += "\n- Rejuvenation\n\t When the undead's body is destroyed, its soul lingers. After 24 hours, the soul inhabits and animates another humanoid corpse on the same plane of existence and regains all its hit points. While the soul is bodiless, a wish spell can be used to force the soul to go to the afterlife and not return."
    if Type == "Undead":
        if Dice() == 1:     r += "\n- Turn Defiance \n\t The undead and any undeads within 30 feet of it have advantage on saving throws against effects that turn undead."
        elif Dice() == 1:   r += "\n- Turn Immunity \n\t The Undead is immune to effects that turn undead."

    if Type == "Undead":
        if Dice() == 1:
            r += "\nVampire Weaknesses \n\t The undead has the following flaws:"
            r += "\n- Forbiddance \n\t The vampire can't enter a residence without an invitation from one of the occupants."
            r += "\n- Harmed by Running Water \n\t The vampire takes 20 acid damage when it ends its turn in running water."
            r += "\n- Stake to the Heart. \n\tThe vampire is destroyed if a piercing weapon made of wood is driven into its heart while it is incapacitated in its resting place."
            r += "\n- Sunlight Hypersensitivity. \n\t The vampire takes 20 radiant damage when it starts its turn in sunlight. While in sunlight, it has disadvantage on attack rolls and ability checks."
        else:
            if Dice() == 1:
                r += "\n- Forbiddance \n\t The undead can't enter a residence without an invitation from one of the occupants."
            if Dice() == 1:
                r += "\n- Harmed by Running Water \n\t The undead takes 20 acid damage when it ends its turn in running water."
            if Dice() == 1:
                r += "\n- Stake to the Heart. \n\tThe undead is destroyed if a piercing weapon made of wood is driven into its heart while it is incapacitated in its resting place."
            if Dice() == 1:
                r += "\n- Sunlight Hypersensitivity. \n\t The undead takes 20 radiant damage when it starts its turn in sunlight. While in sunlight, it has disadvantage on attack rolls and ability checks."

    if Type == "Undead" and Dice() == 1:    r += "\n - Sunlight Weakness \n\t While in sunlight, the undead has disadvantage on attack rolls, ability checks, and saving throws."
    if Type == "Undead" and Dice() == 1:    r += "\n - Sunlight Sensitivity  \n\t While in sunlight, the undead has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."
    if Type == "Undead" and Dice() == 1:    r += "\n - Undead Fortitude. \n\t If damage reduces the Undead to 0 hit points, it must make a Constitution saving throw with a DC of 5 + the damage taken, unless the damage is radiant or from a critical hit. On a success, the Undead drops to 1 hit point instead."

    

    # Skills
    if Type == "Undead" and Dice(7) == 1:   r += "\n - Amorphous \n\t The Undead can move through a space as narrow as 1 inch wide without squeezing."
    if Type == "Undead" and Dice() == 1:    r += "\n - Consume Life. \n\t As a bonus action, the undead can target one creature it can see within 5 feet of it that has 0 hit points and is still alive. The target must succeed on a DC 10 Constitution saving throw against this magic or die. If the target dies, the undead regains 10 (3d6) hit points."
    if Type == "Undead" and Dice() == 1:    r += "\n - Detect Life. \n\t The undead can magically sense the presence of living creatures up to 5 miles away that aren't undead or constructs. She knows the general direction they're in but not their exact locations."
    if Type == "Undead" and Dice() == 1:    r += "\n - Ephemeral \n\t The Undead  can't wear or carry anything."
    if Type == "Undead" and Dice() == 1:    r += "\n - Ethereal Sight \n\t The undead can see 60 feet into the Ethereal Plane when it is on the Material Plane, and vice versa."
    if Type == "Undead" and Dice() == 1:    r += "\n - Etherealness \n\t The undead enters the Ethereal Plane from the Material Plane, or vice versa. It is visible on the Material Plane while it is in the Border Ethereal, and vice versa, yet it can't affect or be affected by anything on the other plane."
    if Type == "Undead" and Dice() == 1:    r += "\n - Incorporeal Movement \n\t The Undead  can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object."
    if Type == "Undead" and Dice() == 1:    r += "\n - Invisibility \n\t The Undead magically turns invisible until it attacks, or until its concentration ends (as if concentrating on a spell). Any equipment the undead wears or carries is invisible with it."
    elif Type == "Undead" and Dice() == 1:  r += "\n - Invisibility \n\t The Undead is invisible."
    if Type == "Undead" and Dice() == 1:    r += "\n - Illumination \n\t The undead sheds either dim light in a 15-foot radius, or bright light in a 15-foot radius and dim light for an additional 15 feet. It can switch between the options as an action."
    if Type == "Undead" and Dice() == 1:    r += "\n - Rejuvenation \n\t If the undead is destroyed, it regains all its hit points in 1 hour unless holy water is sprinkled on its remains or a dispel magic or remove curse spell is cast on them."
    if Type == "Undead" and Dice() == 1:    r += "\n - Shadow Stealth \n\t While in dim light or darkness, the Undead can take the Hide action as a bonus action. Its stealth bonus is also improved to +6."
    if Type == "Undead" and Dice() == 1:    r += "\n - Telekinetic Thrust"
    if Type == "Undead" and Dice() == 1:    r += "\n - Variable Illumination. \n\t The undead sheds bright light in a 5 to 20-foot radius and dim light for an additional number of ft. equal to the chosen radius. The will-o'-wisp can alter the radius as a bonus action."
    if Type == "Undead" and Dice() == 1:    r += "\n - Vengeful Tracker. \n\t The undead knows the distance to and direction of any creature against which it seeks revenge, even if the creature and the undead are on different planes of existence. If the creature being tracked by the undead dies, the undead knows. \n\t If the undead hits the creaure has sworn vengance against, the creature recives an extra 4d6 bludgeoning damage."


    # Combat Skills
    if Type == "Undead" and Dice(7) == 1:   r += "\n - Blood Frenzy \n\t The undead has advantage on melee attack rolls against any creature that doesn't have all its hit points."
    if Type == "Undead" and Dice() == 1:    r += "\n - Charge. \n\t If the undead moves at least 10 feet straight toward a target and then hits it with a simple melee attack on the same turn, the target takes an extra 9 (2d8) piercing damage. If the target is a creature, it must succeed on a DC 14 Strength saving throw or be pushed up to 10 feet away and knocked prone."
    if Type == "Undead" and Dice() == 1:    r += "\n - Horrifying Visage. \n\t Each non-undead creature within 60 feet of the undead that can see it must succeed on a DC [10+%CHA] Wisdom saving throw or be frightened for 1 minute. If the save fails by 5 or more, the target also ages 1d4 × 10 years. A frightened target can repeat the saving throw at the end of each of its turns, ending the frightened condition on itself on a success. If a target's saving throw is successful or the effect ends for it, the target is immune to this undead's Horrifying Visage for the next 24 hours. The aging effect can be reversed with a greater restoration spell, but only within 24 hours of it occurring."
    if Type == "Undead" and Dice() == 1:    r += "\n - Possession (Recharge 6).  \n\t One humanoid that the undead can see within 5 feet of it must succeed on a DC 13 Charisma saving throw or be possessed by the undead; the undead then disappears, and the target is incapacitated and loses control of its body. The undead now controls the body but doesn't deprive the target of awareness. The undead can't be targeted by any attack, spell, or other effect, except ones that turn undead, and it retains its alignment, Intelligence, Wisdom, Charisma, and immunity to being charmed and frightened. It otherwise uses the possessed target's statistics, but doesn't gain access to the target's knowledge, class features, or proficiencies. \n\t The possession lasts until the body drops to 0 hit points, the undead ends it as a bonus action, or the undead is turned or forced out by an effect like the dispel evil and good spell. When the possession ends, the undead reappears in an unoccupied space within 5 feet of the body. The target is immune to this undead's Possession for 24 hours after succeeding on the saving throw or after the possession ends."
    if Type == "Undead" and Dice() == 1:    r += "\n - Stench.  \n\t Any creature that starts its turn within 5 feet of the undead must succeed on a DC 10 Constitution saving throw or be poisoned until the start of its next turn. On a successful saving throw, the creature is immune to the undead's Stench for 24 hours."
    if Type == "Undead":
        if Dice() == 1:    r += "\n - Multiattack. \n\t The undead makes two simple attacks."
        if Dice() == 1:    r += "\n - Multiattack. \n\t The undead makes one simple attack and one special attack"
        if Dice() == 1:    r += "\n - Multiattack. \n\t Melee Weapon Attack: Reach 5 ft., one willing creature, or a creature that is grappled by the undead, incapacitated, or restrained. Hit: 4 (1d6 + %CON) piercing damage plus 7 (2d6) necrotic damage. The target's hit point maximum is reduced by an amount equal to the necrotic damage taken, and the undead regains hit points equal to that amount. The reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0."

    if Type == "Undead" and Dice() == 1:    r += "\n - Life Drain \n\t Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 5 (1d6 + 2) necrotic damage. The target must succeed on a DC 13 Constitution saving throw or its hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0. \n\t A humanoid slain by this attack rises 24 hours later as a zombie under the wight's control, unless the humanoid is restored to life or its body is destroyed. The wight can have no more than twelve zombies under its control at one time."
    if Type == "Undead" and Dice() == 1:
        r += "\n - Bite \n\t Melee Weapon Attack: Reach 5 ft., one creature. Hit: 5 (1d6 + 2) necrotic damage. The target must succeed on a DC 13 Constitution saving throw or its hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0. \n\t A humanoid slain by this attack rises 24 hours later as a zombie under the wight's control, unless the humanoid is restored to life or its body is destroyed. The wight can have no more than twelve zombies under its control at one time."
        r += "\n - Grappling Attack \n\t When the undead makes a simple attack, it can grapple the creature instead of dealing damage (escape DC 10+%STR)." 
    elif Type == "Undead" and Dice() == 1:
        r += "\n - Bite \n\t Melee Weapon Attack: Reach 5 ft., one willing creature, or a creature that is grappled by the undead, incapacitated, or restrained. Hit: 6 (1d6 + %CON) piercing damage plus 7 (2d6) necrotic damage. The target's hit point maximum is reduced by an amount equal to the necrotic damage taken, and the undead regains hit points equal to that amount. The reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0."
        
    

    # NOBLE
    if Type == "Noble" and Dice() == 1:        r += "\n- Parry \n\t The noble adds 2 to its AC against one melee attack that would hit it. To do so, the noble must see the attacker and be wielding a melee weapon."

    if Type == "Plant" and Dice() == 1:        r = r + "\n- Distress Spores. \n\t When the plant takes damage, all other plants within 240 feet of it can sense its pain."
    if Type == "Plant" and Dice() == 1:        r = r + "\n- Sun Sickness. \n\t While in sunlight, the plant has disadvantage on ability checks, attack rolls, and saving throws. The plant dies if it spends more than 1 hour in direct sunlight."
    if Type == "Plant" and Dice() == 1:        r = r + "\n- Condition Immunities\n\t Blinded"
    if Type == "Plant" and Dice() == 1:        r = r + "\n- Condition Immunities\n\t Deafened"
    if Type == "Plant" and Dice() == 1:        r = r + "\n- Condition Immunities\n\t Frightened"
    if Type == "Plant":
        if Dice() == 1:         r = r + "\n- Blindsight\t 30 ft"
        elif Dice() == 1:       r = r + "\n- Blindsight\t 60 ft (Blind Beyond this radius)."
    if Type == "Plant" and Dice() == 1:        r = r + "\n- Darkvision\t 120 ft"
    if Type == "Plant" and Dice() == 1:        r = r + "\n- Death Burst\n\t The Plant explodes when it drops to 0 hit points. Each creature within 20 feet of it must succeed on a DC 15 Constitution saving throw or take 10 (3d6) poison damage and become infected with a disease on a failed save. Creatures immune to the poisoned condition are immune to this disease. Spores invade an infected creature's system, killing the creature in a number of hours equal to 1d12 + the creature's Constitution score, unless the disease is removed. In half that time, the creature becomes poisoned for the rest of the duration. After the creature dies, it sprouts 2d4 Tiny gas spores that grow to full size in 7 days."
    if Type == "Plant" and Dice() == 1:        r = r + "\n- Multiattack\n\t The Plant can do one special attack and a simple attack each turn."

    # WARRIOR
    if Type == "Warrior":
        if Dice() == 1:       r += "\n- Parry \n\t The warrior adds 2 to its AC against one melee attack that would hit it. To do so, the warrior must see the attacker and be wielding a melee weapon."
        elif Dice() == 1:     r += "\n- Parry \n\t The warrior adds 3 to its AC against one melee attack that would hit it. To do so, the warrior must see the attacker and be wielding a melee weapon."
    if Type == "Warrior" and Dice(2) == 1:      r += "\n- Pack Tactics \n\t The warrior has advantage on an attack roll against a creature if at least one of the warrior's allies is within 5 feet of the creature and the ally isn't incapacitated."
    if Type == "Warrior":
        if Dice() == 1:         r += "\n- Multiattack \n\t The Warrior can attack twice with their simple melee attack on his turn."
        elif Dice() == 1:       r += "\n- Multiattack \n\t The Warrior makes three melee attacks or two ranged attacks."
        elif Dice() == 1:       r += "\n- Multiattack \n\t The Warrior makes two special melee attacks and one simple melee attack."
    if Type == "Warrior" and Dice() == 1:       r += "\n- Brave \n\t The warrior has advantage on saving throws against being frightened."
    if Type == "Warrior" and Dice() == 1:       r += "\n- Brute \n\t A melee weapon deals one extra die of its damage when the warrior hits with it (included in the attack)."

    if Type == "Warrior" and Dice() == 1:       r += "Shield Bash. \n\t Melee Weapon Attack: Reach 5 ft., one creature. Hit: 9 (2d4 + %STR) bludgeoning damage. If the target is a Medium or smaller creature, it must succeed on a DC [11+%STR] Strength saving throw or be knocked prone."


    # RETURN the skills' string
    return r


def Legendary(Type=""):
    if Type == "":
        if Dice(0) == 1:    Type= Race()
        else:               Type= Background()

    if Type == "Human":
        if Dice()==1:        return "\n- Attack \n\t It can do one simple attack to any creature"
        if Dice()==1:        return "\n- Move: \n\t It can move half their movement"

    if Type == "Celestial":
        if Dice()==1:        return "\n- Attack \n\t It can do one simple attack to any creature"
        if Dice()==1:        return "\n- Shimmering Shield (Costs 2 Actions). The Celestial creates a shimmering, magical field around itself or another creature it can see within 60 feet of it. The target gains a +2 bonus to AC until the end of the celestial's next turn."
        if Dice()==1:        return "\n- Heal Self (Costs 3 Actions). \n\t The celestial magically regains 8 (2d8 + %CON) hit points."
       
    return Legendary()


def Lair(Type=""):
    if Type == "":
        if Dice(0) == 1:    Type= Race()
        else:               Type= Background()

    r = ""

    if Type == "Dragon" and Dice() == 1:        r += "\n- Chaotic Aura \n\t The dragon creates misdirecting currents of air and magic around itself. Until initiative count 20 on the next round, whenever a ranged attack roll misses the dragon, reroll the attack against a random creature within 30 feet of the dragon that doesn't have total cover against the attack."
    if Type == "Dragon" and Dice() == 1:        r += "\n- Grasping Plants \n\t The dragon causes roots and vines to temporarily grow around it; until initiative count 20 on the next round, the ground within 20 feet of the dragon is difficult terrain."

    if Type == "Fey" and Dice() == 1:        r += "\n- Chaotic Aura \n\t The Fey creates misdirecting currents of air and magic around itself. Until initiative count 20 on the next round, whenever a ranged attack roll misses the Fey, reroll the attack against a random creature within 30 feet of the fey that doesn't have total cover against the attack."
    if Type == "Fey" and Dice() == 1:        r += "\n- Grasping Plants \n\t The fey causes roots and vines to temporarily grow around it; until initiative count 20 on the next round, the ground within 20 feet of the fey is difficult terrain."
    if Type == "Fey" and Dice() == 1:        r += "\n- Fey Walk \n\t Until initiative count 20 on the next round, the fey can pass through solid walls, doors, ceilings, and floors as if the surfaces weren't there."
    if Type == "Fey" and Dice() == 1:        r += "\n- The fey targets any number of doors and windows that they can see, causing each one to either open or close as they wish. Closed doors can be magically locked (requiring a successful DC 20 Strength check to force open) until they choose to make them unlocked, or until they use this lair action again to open them."
    if Type == "Fey" and Dice() == 1:        r += "\n- The fey fills up to four 10-foot cubes of water with ink. The inky areas are heavily obscured for 1 minute, although a steady, strong underwater current disperses the ink on initiative count 10. The fey ignores the obscuring effect of the ink."
    if Type == "Fey" and Dice() == 1:        r += "\n- The fey chooses one humanoid within the lair and instantly creates a simulacrum of that creature (as if created with the simulacrum spell). This hideous simulacrum is formed out of seaweed, slime, half-eaten fish, and other garbage, but still generally resembles the creature it is imitating. This simulacrum obeys the fey's commands and is destroyed on initiative count 20 on the next round."
    if Type == "Fey" and Dice() == 1:        r += "\n- The fey creates an illusory duplicate of themselves, which appears in its own space. As long as they can see their duplicate, the fey can move it a distance equal to their walking speed as well as make the illusion speak on their turn (no action required). The illusion has the same statistics as the fey but can't take actions or reactions. It can interact with its environment and even pick up and hold real objects. The illusion seems real in every way but disappears if it takes any amount of damage. Otherwise, it lasts until the fey dismisses it (no action required) or can no longer see it. If the fey uses this lair action to create a new duplicate, the previous one vanishes, dropping any real objects in its possession."

    if Type == "Fiend" and Dice() == 1:     r += "\n- One creature the fiend can see within 120 feet of them must succeed on a Charisma saving throw or be banished to a prison demiplane. To escape, the creature must use its action to make a Charisma check contested by the fiend's. If the creature wins, it escapes the demiplane. Otherwise, the effect ends on initiative count 20 on the next round. When the effect ends, the creature reappears in the space it left or in the nearest unoccupied space if that one is occupied."
    if Type == "Fiend" and Dice() == 1:     r += "\n- The fiend targets up to three creatures that they can see within 60 feet of them. Each target must succeed on a Constitution saving throw or be flung up to 30 feet through the air. A creature that strikes a solid object or is released in midair takes 1d6 bludgeoning damage for every 10 feet moved or fallen."


    if Type == "Plant" and Dice() == 1:        r += "\n- Grasping Plants \n\t The plant causes roots and vines to temporarily grow around it; until initiative count 20 on the next round, the ground within 20 feet of the plant is difficult terrain."

    if r == "": return  Lair()
    return r


def Region(Type = ""):
    if Type == "":
        if Dice(0) == 1:    Type= Race()
        else:               Type= Background()

    r = ""
    

    if Type == "Beastfolk":
        if Dice() == 1:        r += "\n- Beasts that have an Intelligence score of 2 or lower are charmed by the beastfolk and directed to be aggressive toward intruders in the area."

    if Type == "Celestial":
        if Dice() == 1:        r += "\n- Open flames of a non magical nature are extinguished within the celestial's domain. Torches and campfires refuse to burn, but closed lanterns are unaffected."
        if Dice() == 1:        r += "\n- Creatures native to the celestial's domain have an easier time hiding; they have advantage on all Dexterity (Stealth) checks made to hide."
        if Dice() == 1:        r += "\n- When a good-aligned creature casts a spell or uses a magical effect that causes another good-aligned creature to regain hit points, the target regains the maximum number of hit points possible for the spell or effect."
        if Dice() == 1:        r += "\n- Curses affecting any good-aligned creature are suppressed."
        

    
    if Type == "Fey":
        if Dice() == 1:        r += "\n- Compulsory Offering \n\t The first time a creature comes within 1 mile of the faerie dragon's lair, the creature must succeed on a DC 15 Wisdom saving throw or feel an overwhelming compulsion to leave an offering worth at least 5 gp stashed in an out-of-the-way place. The dragon immediately senses the location of this gift. A creature can be affected only once by this compulsion."
        if Dice() == 1:        r += "\n- Malleable Time \n\t Time is fluid within 1 mile of the fey's lair, flowing somewhere between half and twice its normal speed."
        if Dice() == 1:        r += "\n- Birds, rodents, snakes, spiders, or toads (or some other creatures appropriate to the fey) are found in great profusion."
        if Dice() == 1:        r += "\n- Beasts that have an Intelligence score of 2 or lower are charmed by the fey and directed to be aggressive toward intruders in the area."
        if Dice() == 1:        r += "\n- Strange carved figurines, twig fetishes, or rag dolls magically appear in trees."
        if Dice(8) == 1:       r += "\n- Most surfaces are covered by a thin film of slime, which is slick and sticks to anything that touches it."
        if Dice(8) == 1:       r += "\n- Currents and tides are exceptionally strong and treacherous. Any ability check made to safely navigate or control a vessel moving through these waters has disadvantage."
        if Dice(8) == 1:       r += "\n- Shores are littered with dead, rotting fish. The fey can sense when one of the fish is handled and cause it to speak with their voice."

    if Type == "Fiend":
        if Dice() == 1:        r += "\n- Birds, rodents, snakes, spiders, or toads (or some other creatures appropriate to the fiend) are found in great profusion."
        if Dice() == 1:        r += "\n- Shadows seem abnormally gaunt and sometimes move on their own as though alive."
        if Dice() == 1:        r += "\n- Creatures are transported to a harmless but eerie demiplane filled with shadowy forms, waxy corpses, and cackling. The creatures are trapped there for a minute or two, and then returned to the place where they vanished from."
        if Dice() == 1:        r += "\n- Intelligent creatures see hallucinations of dead friends, family members, and even themselves littering the fiendish realm. Any attempt to interact with a hallucinatory image causes it to disappear."


    if r == "": return  Region()
    return r


def PlotHook():
    Hooks = [
        "I received a message from a God, but it was unclear. I must find a long forgotten shrine to talk to him again.", 
        "I must find a rare alchemist element to make a medicine needed for my kind.",
        "I was chosen to defeat the enemy of my kind.",
        "I must contact a spirit that belongs to this place.",
        "I lost somebody. There may be a way to have them back in this place.",
        "There is something trapped in this place. I seek to liberate them.",
        "There is something trapped in this place. I seek to keep it that way.",
        "I'm trapped. Could you please help me?",
        "I'm infiltrating a corrupt organization to take it down from the inside.",
        "I'm looking for a child that was taken from my kind.",
        "I am a gladiator entertainer. I need to give a good spectacle to provide for my kind.",
        "I shall prove myself in the Arena.",
        "I shall gain fame and fortune in the Arena.",
        "One from my kind was killed. I seek revenge.",
        "One from my kind was harmed. I seek compensation.",
        "I was slaved for a long time. I seek revenge.",      
        "I was slaved for a long time. I seek to liberate others in chains.",      
        "A partner was taken in battle. I will liberate them or die trying.",
        "One from my kind has been taken by slavers. I will liberate them or die trying.",
        "I am connected to the spirits of my kind. They carry a purpose for me that I shall carry on my shoulders.",
        "I lost all hope in my civilization. I shall make something new.",
        "I lost my purpose long ago. I'm looking for something new to care for.",
        "My kind carries an ancient curse. I shall cleanse our souls.",
        "My kind is alienated in these lands. We just try to survive, but anger folows wherever we go. ",
        "I run away from the opression of my kind",
        "I fight against the opression of my kind",
        "My kind is under repression. I aim to liberate them.",
        "I was unjustly imprisoned by a rival, I will get my revenge and then more. ",
        "I've been away of home to fight a war. I now want to go back to my loved ones.",
        "I was promised for a convenience marriage. I decided to run away.",
        "I'm the legacy of a tyrant. I am correcting their sins.",
        "My family was victim to a great injustice. I seek restitution to my name.",
        "My family is guilty of a great crime. I'm trying to ammend this injustice.",
        "I was excommunicated. I'm redeeming myself in the eyes of my gods. ",
        "I'm condemned to hell. I want redemption.",
        "I'm already condemned to the hells. I might as well earn it.",
        "These are my hunting territories. You are now my prey.",
        "I am the tyrant of these lands",
        "I must visit all the oceans of the world and behold the ships that sail there.",
        "I was tricked by a smuggler who stole something precious from me. I will find that thief.",
        "After one last job, I will retire from the business.",
        "I owe a debt that cannot be repaid in gold.",
        "I intend to become the leader of the kind that I belong to.",
        "My most valuable possession was stolen from me, and I burn with the desire to recover it.",
        "My vessel was stolen from me, and I burn with the desire to recover it.",
        "My familiar was stolen from me, and I burn with the desire to recover it.",
        "My sword was stolen from me, and I burn with the desire to recover it.",
        "My loved one was kidnapped from me, and I burn with the desire to recover them.",
        "An item with personal value was stolen from me, and I burn with the desire to recover it.",
        "Someone I love was killed by a rival kind, and I will have revenge.",
        "I love someone from another kind, but the relationship is forbidden.",
        "I was exiled for a crime I didn't commit.",
        "I keep my thoughts and discoveries in a journal. My journal is my legacy. I just lost it!",
        "A monster that slaughtered dozens of innocent people spared my life, and I don’t know why. I am certain it follows me since.",
        "I protect those who cannot protect themselves.",
        "I have a family, but I have no idea where they are. One day, I hope to see them again.",
        "Recruited into a lord's army, I rose to leadership and was commended for my heroism. Now I fight for them.",
        "A celestial, fey, or similar creature gave me a blessing or revealed my secret origin.",
        "I'm breaking into a tyrant's castle to steal weapons to arm the people.",
        "I lead a militia to fight off an invading army.",
        "I steal from merchants to help the poor.",
        "I'm the last hope against a terrible monster.",
        "I want to save people of a comming disaster.",
        "I stand up to a tyrant's agents.",
        "I must repay my village's debt.",
        "My destiny awaits me at the bottom of a particular pond in the Feywild.",
        "The gods saved me during a terrible storm, and I will honor their gift.",
        "I will hunt the many famous beasts of this land.",
        "I will fish the many famous waters of this land.",
        "Someone else's greed destroyed my livelihood, and I will be compensated.",
        "I lost something important in the deep sea, and I intend to find it.",
        "I have a tail like that of a dog or another animal, as a punishment from a Fey for an accidental insult.",
        "I have a weakness for the exotic beauty of the people of these lands.",
        "I do everything for those who were taken from me.",
        "I am exceptional. I do this because no one else can, and no one can stop me.",
        "I stand in opposition, lest the wicked go unopposed.",
        "I've seen too many in need. I must not fail them as everyone else has.",
        "What I do, I do for the world. The people don't realize how much they need me.",
        "I do everything for my kind. My first thought is keeping them safe.",
        "I once satirized a noble who still wants my head. It was a mistake that I will likely repeat.",
        "I would do anything for the other members of my old troupe.",
        "I will do anything to prove myself superior to my hated rival.",
        "I want to be famous, whatever it takes.",
        "Someone stole an object precious to me, and someday I'll get it back.",
        "Someone I loved died because of I mistake I made. That will never happen again.",
        "I'm guilty of a terrible crime. I hope I can redeem myself for it.",
        "I will become the greatest thief that ever lived.",
        "Something important was taken from me, and I aim to steal it back.",
        "My ill-gotten gains go to support my kind.",
        "I'm trying to pay off an old debt I owe to a generous benefactor.",
        "I swindled and ruined a person who didn't deserve it. I seek to atone for my misdeeds but might never be able to forgive myself.",
        "A powerful person killed someone I love. Some day soon, I'll have my revenge.",
        "I come from a noble family, and one day I'll reclaim my lands and title from those who stole them from me.",
        "Somewhere out there, I have a child who doesn't know me. I'm making the world better for him or her.",
        "I owe everything to my mentor – a horrible person who's probably rotting in jail somewhere.",
        "I fleeced the wrong person and must work to ensure that this individual never crosses paths with me or those I care about.",
        "I hope to bring prestige to a library, a museum, or a university.",
        "I won't sell an art object or other treasure that has historical significance or is one of a kind.",
        "I have a friendly rival. Only one of us can be the best, and I aim to prove it's me.",
        "I want to find my mentor, who disappeared on an expedition some time ago.",
        "Ever since I was a child, I've heard stories about a lost city. I aim to find it, learn its secrets, and earn my place in the history books.",
        "I'm under a curse.",
        "I'm the Protector of this Land",
        "I'm guarding something of great importance.",
        "I'm protecting someone of great importance.",
        "I'm looking for a special thing",
        "I I just want to have fun",
        "I'm looking for someone",
        "I want to get rich",
        "I'm selling something",
        "I'm buying something",
        "I want to ammend a mistake.",
        "I want to recuperate my honor",
        "I'm protecting my kind",
        "I want to prove myself",
        "I'm curious",
        "I'm protecting my interests",
        "I am lost",
        "I am a freedomfighter.",
        "I want to topple a tyrant.",
        "I fight to preserve order",
        "I am in pilgrimage",
        "I lost my home, and I'm looking for a new life.",
        "A higher power commanded a very important mission.",
        "I'm just following orders.",
        "I am injured. ",
        "I'm in a forbidden or impossible relationship. ",
        "I have a legacy to mantain",
        "I have a great rival",
        "I pursue a goal that breaks tradition or law",
        "I am in debt.",
        "I lead an uprising.",
        "Feels loyalty to two opposing causes.",
        "Feels loyalty to two opposing kinds.",
        "Has a crisis of faith.",
        "Is looking for revenge",
        "Is trying to solve a failure.",
        "Is trying to solve a tragedy.",
        "Is standing up for those who are not equipped to stand up for themselves.",
        "They keep a great secret.",
        "They need to unveil a great secret.",
        "I am bored.",
        "I am hungry.",
        "I am trapped.",
        "I want to create something.",
        "I am running from justice.",
        "I am running from justice for a crime I didn't commit.",
        "I have to make a very difficult choice",
        "I serve an unethical and corrupt organization.",
        "I would die to recover an ancient relic of my faith that was lost long ago.",
        "I will someday get revenge on the corrupt temple hierarchy who branded me a heretic.",
        "I owe my life to the priest who took me in when my parents died.",
        "Everything I do is for the common people.",
        "I will do anything to protect the holy site where I serve.",
        "I seek to preserve a sacred text that my enemies consider heretical and seek to destroy.",
        "My mentor gave me a journal filled with lore and wisdom. Losing it would devastate me.",
        "Having lived among the people of a primeval tribe or clan, I long to return and see how they are faring.",
        "Years ago, tragedy struck the members of an isolated society I befriended, and I will honor them.",
        "I want to learn more about a particular humanoid culture that fascinates me.",
        "I seek to avenge a clan that was wiped out.",
        "I seek to avenge a tribe that was wiped out.",
        "I seek to avenge a kingdom that was wiped out.",
        "I seek to avenge an empire that was wiped out.",
        "I seek to avenge my kind, that was wiped out.",
        "I have a trinket that I believe is the key to finding a long-lost society.",
        "I will overcome a rival and prove myself their better.",
        "My mistake got someone hurt. Ill never make that mistake again.",
        "I will be the best for the honor and glory of my home.",
        "A proud noble once gave me a horrible beating, and I will take my revenge on any bully I encounter.",
        "The tyrant who rules my land will stop at nothing to see me killed.",
        "My kind has a history of practicing the dark arts. I dabbled once and felt something horrible clutch at my soul, whereupon I fled in terror.",
        "An apparition that has haunted my family for generations now haunts me. I don’t know what it wants, and it won’t leave me alone.",
        "An oni took my sibling one cold, dark night, and I was unable to stop it.",
        "I was cursed with lycanthropy. I am now haunted by the innocents I slaughtered.",
        "My torment drove away the person I love. I strive to win back the love I’ve lost.",
        "I have a child to protect. I must make the world a safer place for them.",
        "I am searching for spiritual enlightenment.",
        "I am the caretaker of an ancient ruin.",
        "I am the caretaker of an ancient relic.",
        "I have great insight into a great evil that only I can destroy.",
        "Should my discovery come to light, it could bring ruin to the world.",
        "I entered seclusion to hide from the ones who might still be hunting me. I must someday confront them.",
        "I am a pilgrim in search of a person, place, or relic of spiritual significance.",
        "A fiend possessed you as a child. You were locked away but escaped. The fiend is still inside you, but now you try to keep it locked away.",
        "I owe a debt I can never repay to the person who took pity on me.",
        "I escaped my life of poverty by robbing an important person, and I'm wanted for it.",
        "Grand Designs. You are working on plans and schematics for a new, very fast ship. You must examine as many different kinds of vessels as possible to help ensure the success of your design.",
        "I must find a kind of wood rumored to possess magical qualities.",
        "I will craft a boat capable of sailing through the most dangerous of storms.",
        "A kraken destroyed my ship; its teeth shall adorn my hearth.",
        "A dragon destroyed my town; its teeth shall adorn my armour.",
        "A monster destroyed my town; its teeth shall adorn my armour.",
        "A monster destroyed my home; I will find it, and destroy it.",
        "I work to preserve a library, university, scriptorium, or monastery.",
        "I have an ancient text that holds terrible secrets that must not fall into the wrong hands.",
        "I was cheated out of my fair share of the profits, and I want to get my due.",
        "I've been searching my whole life for the answer to a certain question.",
        "Ruthless pirates murdered my captain and crewmates, plundered our ship, and left me to die. Vengeance will be mine.",
        "I must ran twenty-five miles without stopping to warn my clan of an approaching horde.",
        "I will bring terrible wrath down on the evildoers who destroyed my homeland.",
        "I am the last of my kind, and it is up to me to ensure their names enter legend.",
        "I suffer awful visions of a coming disaster and will do anything to prevent it.",
        "It is my duty to raise children to mantain my kind.",
        "I face danger and evil to offset an unredeemable act in my past.",
        "I'm searching for a friend captured by an elusive enemy.",
        "My commander betrayed my unit, and I will have revenge.",
        ""]
    return random.choice(Hooks)


def Trait(background=""):
    Traits = [
        # Moral Compass
        "Virtuous", "Principled", "Honorable", "Unprincipled", "Dishonorable", "Depraved",
        
        # Personal Goals
        "Power-Seeker", "Knowledge-Seeker", "Peace-Seeker", "Chaos-Seeker", "Revenge-Seeker", "Justice-Seeker",
        
        # Relationship with Society
        "Conformist", "Rebel", "Outsider", "Leader", "Follower", "Anarchist",
        
        # Primal Instincts
        "Survivalist", "Protector", "Predator", "Opportunist", "Guardian", "Destroyer",
        
        # Complex Alignments
        "Benevolent Dictator", "Reluctant Hero", "Martyr", "Machiavellian", "Nihilist", "Altruist",
        
        # Belief Systems
        "Theist", "Atheist", "Agnostic", "Spiritualist", "Skeptic", "Zealot",
        
        # Existential Alignments
        "Existentialist", "Absurdist", "Fatalist", "Optimist", "Pessimist", "Realist"
  
        "I am optimistic, seeing events in the most positive light.",   
        "If you do me an injury, I will crush you, ruin your name, and salt your fields.",
        "My favor, once lost, is lost forever.",
        "Despite my noble birth, I do not place myself above other folk. We all have the same blood.",
        "I don't like to get my hands dirty, and I won't be caught dead in unsuitable accommodations.",
        "I take great pains to always look my best and follow the latest fashions.",
        "No one could doubt by looking at my regal bearing that I am a cut above the unwashed masses.",
        "The common folk love me for my kindness and generosity.",
        "My eloquent flattery makes everyone I talk to feel like the most wonderful and important person in the world.",
        "I sometimes stay up all night listening to the ghosts of my fallen enemies.",
        "I become irrational when innocent people are hurt.",
        "I hold grudges and have difficulty forgiving others.",
        "My intensity can drive others away.",
        "I find civilian life difficult and struggle to say the right thing in social situations.",
        "I grow combative and unpredictable when I drink.",
        "Fear leads to tyranny, and both must be eradicated.",
        "I must set an example of hope for those who have given up.",
        "I. Will. Finish. The. Job.",
        "When the sea is within my sight, my mood is jovial and optimistic.",
        "I become cantankerous and quiet in the rain.",
        "I am always working on some project or other.",
        "I am dependable.",
        "I enjoy being out in nature; poor weather never sours my mood.",
        "I prefer to solve problems without violence, but I finish fights decisively.",
        "I laugh loudly and see the humor in stressful situations.",
        "I speak rarely but mean every word I say.",
        "By my words and actions, I often bring shame to my family.",
        "In fact, the world does revolve around me.",
        "I have an insatiable desire for carnal pleasures.",
        "I too often hear veiled insults and threats in every word addressed to me, and I'm quick to anger.",
        "I hide a truly scandalous secret that could ruin my family forever.",
        "I secretly believe that everyone is beneath me.",
        "The common folk must see me as a hero of the people.",
        "My loyalty to my sovereign is unwavering.",
        "I am in love with the heir of a family that my family despises.",
        "Nothing is more important than the other members of my family.",
        "My house's alliance with another noble family must be sustained at all costs.",
        "I will face any challenge to win the approval of my family.",
        "If you do me an injury, I will crush you, ruin your name, and salt your fields.",
        "My favor, once lost, is lost forever.",
        "Despite my noble birth, I do not place myself above other folk. We all have the same blood.",
        "I don't like to get my hands dirty, and I won't be caught dead in unsuitable accommodations.",
        "I take great pains to always look my best and follow the latest fashions.",
        "No one could doubt by looking at my regal bearing that I am a cut above the unwashed masses.",
        "The common folk love me for my kindness and generosity.",
        "My eloquent flattery makes everyone I talk to feel like the most wonderful and important person in the world.",
        "Don't expect me to save those who can't save themselves. It is nature's way that the strong thrive and the weak perish.",
        "Violence is my answer to almost any challenge.",
        "I am slow to trust members of other races, tribes, and societies.",
        "I remember every insult I've received and nurse a silent resentment toward anyone who's ever wronged me.",
        "There's no room for caution in a life lived to the fullest.",
        "I am too enamored of ale, wine, and other intoxicants.",
        "I was, in fact, raised by wolves.",
        "I feel far more comfortable around animals than people.",
        "I'm always picking things up, absently fiddling with them, and sometimes accidentally breaking them.",
        "I place no stock in wealthy or well-mannered folk. Money and manners won't save you from a hungry owlbear.",
        "I have a lesson for every situation, drawn from observing nature.",
        "I once ran twenty-five miles without stopping to warn my clan of an approaching orc horde. I'd do it again if I had to.",
        "I watch over my friends as if they were a litter of newborn pups.",
        "I'm driven by a wanderlust that led me away from home.",
        "I can't keep a secret to save my life, or anyone else's."
        "I speak without really thinking through my words, invariably insulting others."
        "I overlook obvious solutions in favor of complicated ones.",
        "Unlocking an ancient mystery is worth the price of a civilization.",
        "Most people scream and run when they see a demon. I stop and take notes on its anatomy.",
        "I am easily distracted by the promise of information.",
        "I sold my soul for knowledge. I hope to do great deeds and win it back.",
        "My life's work is a series of tomes related to a specific field of lore.",
        "I'm convinced that people are always trying to steal my secrets.",
        "I am horribly, horribly awkward in social situations.",
        "I… speak… slowly… when talking… to idiots,… which… almost… everyone… is… compared… to me.",
        "I'm willing to listen to every side of an argument before I make my own judgment.",
        "There's nothing I like more than a good mystery.",
        "I'm used to helping out those who aren't as smart as I am, and I patiently explain anything and everything to others.",
        "I've read every book in the world's greatest libraries – or I like to boast that I have.",
        "I use polysyllabic words that convey the impression of great erudition.",
        "My pride will probably lead to my destruction.",
        "I can't help but pocket loose coins and other trinkets I come across.",
        "Once I start drinking, it's hard for me to stop.",
        "Once someone questions my courage, I never back down no matter how dangerous the situation.",
        "I'll say anything to avoid having to do extra work.",
        "I follow orders, even if I think they're wrong.",
        "In a small town, I have a paramour whose eyes nearly stole me from my purpose.",
        "I'll always remember my first ship.",
        "The ship is most important – crewmates and captains come and go.",
        "I'm loyal to my captain first, everything else second.",
        "I don't know when to throw something away. You never know when it might be useful again.",
        "I repair broken things to redeem what's broken in myself.",
        "Much of the treasure I claim will be used to enrich my community.",
        "I don't mind getting my hands dirty.",
        "I have an endless supply of cautionary tales related to the sea.",
        "A pipe, an ale, and the smell of the sea: paradise.",
        "I'm not afraid of hard work—in fact, I prefer it.",
        "I love sketching and designing objects.",
        "I love sketching and designing objects, especially traps.",
        "I love sketching and designing objects, especially boats.",
        "I love sketching and designing objects, especially weapons.",
        "I love sketching and designing objects, especially constructs.",
        "I love sketching and designing objects, especially magic items.",
        "I thrive under pressure.",
        "I'm extremely fond of puzzles.",
        "I love talking and being heard more than I like to listen.",
        "Mysteries of the Deep. You experienced an encounter with a possibly divine being while sailing alone. Work with your DM to determine the secret about the deep waters of the sea that this entity revealed to you.",
        "Low Places. You have contacts in the smuggling outfits along the coast; you occasionally repair the criminals' ships in exchange for coin and favors.",
        "Master of Armaments. You specialized in designing and mounting defenses for the navy. You easily recognize and determine the quality of such items.",
        "Favored. Gave a great advice to a merchant, which saved it from ruin. You have a standing invitation to visit the merchant's distant mansion.",
        "Solid and Sound. You patched up a war galley and prevented it from sinking. The local navy regards you as a friend.",
        "Though I act charming, I feel nothing for others and don't know what friendship is.",
        "Few people know the real me.",
        "I struggle to trust the words of others.",
        "I believe everyone has a price and am cynical toward those who present themselves as virtuous.",
        "I tend to assess my relationships in terms of profit and loss.",
        "Lying is reflexive, and I sometimes engage in it without realizing.",
        "I give most of my profits to a charitable cause, and I don't like to brag about it.",
        "I become wistful when I see the sun rise over the ocean.",
        "I enjoy doing things others believe to be impossible.",
        "I love gold but won't cheat a friend.",
        "Nothing rattles me; I have a lie for every occasion.",
        "I never stop smiling.",
        "I think of everything in terms of monetary value.",
        "I'd rather eat my armor than admit when I'm wrong.",
        "I obey the law, even if the law causes misery.",
        "My hatred of my enemies is blind and unreasoning.",
        "I made a terrible mistake in battle that cost many lives – and I would do anything to keep that mistake secret.",
        "I have little respect for anyone who is not a proven warrior.",
        "The monstrous enemy we faced in battle still leaves me quivering with fear.",
        "I fight for those who cannot fight for themselves.",
        "Those who fight beside me are those worth dying for.",
        "I'll never forget the crushing defeat my kind suffered or the enemies who dealt it.",
        "My honor is my life.",
        "Someone saved my life on the battlefield. To this day, I will never leave a friend behind.",
        "I would still lay down my life for the people I served with.",
        "I face problems head-on. A simple, direct solution is the best path to success.",
        "I have a crude sense of humor.",
        "I enjoy being strong and like breaking things.",
        "I can stare down a hell hound without flinching.",
        "I'm full of inspiring and cautionary tales from my military experience relevant to almost every combat situation.",
        "I've lost too many friends, and I'm slow to make new ones.",
        "I'm haunted by memories of war. I can't get the images of violence out of my mind.",
        "I'm always polite and respectful.",
        "People who can't take care of themselves get what they deserve.",
        "It's not stealing if I need it more than someone else.",
        "I'd rather kill someone in their sleep than fight fair.",
        "I will never fully trust anyone other than myself.",
        "Gold seems like a lot of money to me, and I'll do just about anything for more of it.",
        "If I'm outnumbered, I will run away from a fight.",
        "No one else should have to endure the hardships I've been through.",
        "I owe my survival to another urchin who taught me to live on the streets.",
        "I sponsor an orphanage to keep others from enduring what I was forced to endure.",
        "My town or city is my home, and I'll fight to defend it.",
        "My secret could get me expelled from my kind.",
        "My kind and blood line make me the best!",
        "I'm obsessed with conspiracy theories and worried about secret societies and hidden demons.",
        "I'm fixated on following official protocols.",
        "I'm determined to impress the leaders of my faction, and to become a leader myself.",
        "My organization must evolve, and I'll lead the evolution.",
        "I don't care about the organization as a whole, but I would do anything for my old mentor.",
        "I never forget an insult against me.",
        "I'm always looking to improve efficiency.",
        "I like keeping secrets and won't share them with anyone.",
        "I'd risk too much to uncover a lost bit of knowledge.",
        "I let my need to win arguments overshadow friendships and harmony.",
        "I am dogmatic in my thoughts and philosophy.",
        "I harbor dark, bloodthirsty thoughts that my isolation and meditation failed to quell.",
        "Now that I've returned to the world, I enjoy its delights a little too much.",
        "I entered seclusion because I loved someone I could not have.",
        "I'm still seeking the enlightenment I pursued in my seclusion, and it still eludes me.",
        "I am working on a grand philosophical theory and love sharing my ideas.",
        "I often get lost in my own thoughts and contemplation, becoming oblivious to my surroundings.",
        "I connect everything that happens to me to a grand, cosmic plan.",
        "I'm oblivious to etiquette and social expectations.",
        "I feel tremendous empathy for all who suffer.",
        "The leader of my community had something wise to say on every topic, and I am eager to share that wisdom.",
        "I am utterly serene, even in the face of disaster.",
        "I've been isolated for so long that I rarely speak, preferring gestures and the occasional grunt.",
        "I needed to commune with nature, far from civilization.",
        "I needed a quiet place to work on my art, literature, music, or manifesto.",
        "I retreated from society after a life-altering event.",
        "I talk to spirits that no one else can see.",
        "I am a purveyor of doom and gloom who lives in a world without hope.",
        "I have an addiction.",
        "I feel no compassion for the dead. They’re the lucky ones.",
        "I assume the worst in people.",
        "I have certain rituals that I must follow every day. I can never break them.",
        "There’s evil in me, I can feel it. It must never be set free.",
        "A terrible guilt consumes me. I hope that I can find redemption through my actions.",
        "I would sacrifice my life and my soul to protect the innocent.",
        "I put no trust in divine beings.",
        "I refuse to become a victim, and I will not allow others to be victimized.",
        "I expect danger around every corner.",
        "I don’t talk about the thing that torments me. I’d rather not burden others with my curse.",
        "I live for the thrill of the hunt.",
        "I spend money freely and live life to the fullest, knowing that tomorrow I might die.",
        "I like to read and memorize poetry. It keeps me calm and brings me fleeting moments of happiness.",
        "I don't run from evil. Evil runs from me.",
        "You did terrible things to avenge the murder of someone you loved. You became a monster, and it haunts your waking dreams.",
        "You opened an eldritch tome and saw things unfit for a sane mind. You burned the book, but its words and images are burned into your psyche.",
        "A hag kidnapped and raised you. You escaped, but the hag still has a magical hold over you and fills your mind with evil thoughts.",
        "I was born under a dark star. I can feel it watching me, coldly and distantly. Sometimes it beckons me in the dead of night.",
        "I'm well known for my work, and I want to make sure everyone appreciates it. I'm always taken aback when people haven't heard of me.",
        "I don't part with my money easily and will haggle tirelessly to get the best deal possible."
        "I like to talk at length about my profession.",
        "I'm rude to people who lack my commitment to hard work and fair play.",
        "I'm full of witty aphorisms and have a proverb for every occasion.",
        "I always want to know how things work and what makes people tick.",
        "I'm a snob who looks down on those who can't appreciate fine art.",
        "I believe that anything worth doing is worth doing right. I can't help it – I'm a perfectionist.",
        "I change my mood or my mind as quickly as I change key in a song.",
        "I'll settle for nothing less than perfection.",
        "I get bitter if I'm not the center of attention.",
        "I love a good insult, even one directed at me.",
        "Nobody stays angry at me or around me for long, since I can defuse any amount of tension.",
        "I'm a hopeless romantic, always searching for that 'special someone'."
        "Whenever I come to a new place, I collect local rumors and spread gossip.",
        "I know a story relevant to almost every situation.",
        "I have trouble trusting in my allies.",
        "Secretly, I believe that things would be better if I were a tyrant lording over the land.",
        "I have a weakness for the vices of the city, especially hard drink.",
        "The people who knew me when I was young know my shameful secret, so I can never go home again.",
        "I'm convinced of the significance of my destiny, and blind to my shortcomings and the risk of failure.",
        "I wish my childhood sweetheart had come with me to pursue my destiny.",
        "My tools are symbols of my past life, and I carry them so that I will never forget my roots.",
        "I worked the land, I love the land, and I will protect the land.",
        "I get bored easily. When am I going to get on with my destiny?",
        "I misuse long words in an attempt to sound smarter.",
        "Thinking is for other people. I prefer action.",
        "I'm confident in my own abilities and do what I can to instill confidence in others.",
        "I have a strong sense of fair play and always try to find the most equitable solution to arguments.",
        "When I set my mind to something, I follow through no matter what gets in my way.",
        "If someone is in trouble, I'm always ready to lend help.",
        "I judge people by their actions, not their words.",
        "I am obsessed with catching an elusive beast, often to the detriment of other pursuits.",
        "I work hard, but I play harder.",
        "I am inclined to tell long-winded stories at inopportune times.",
        "I have lived a hard life and find it difficult to empathize with others.",
        "I become depressed and anxious if I'm away from the sea too long.",
        "I am judgmental, especially of those I deem homebodies or otherwise lazy.",
        "Luck favors me, and I take risks others might not.",
        "I dislike bargaining; state your price and mean it.",
        "I work hard; nature offers no handouts.",
        "I laugh heartily, feel deeply, and fear nothing.",
        "Rich folk don't know the satisfaction of hard work.",
        "I need long stretches of quiet to clear my head.",
        "My friends are my crew; we sink or float together.",
        "I am unmoved by the wrath of nature.",
        "I'm always changing my mind-well, almost always.",
        "I have many vices and tend to indulge them.",
        "I never give away anything for free and always expect something in return.",
        "I'm forgetful. Sometimes I can't remember even the simplest things.",
        "I'm a kleptomaniac who covets shiny, sparkling treasure.",
        "I'm always operating under a tight timeline, and I'm obsessed with keeping everything on schedule.",
        "I think the whole multiverse is out to get me.",
        "I easily lose track of time. My poor sense of time means I'm always late.",
        "I feel indebted to a witch or fae for giving me a home and a purpose.",
        "I'm drawn to the Feywild and long to return there, if only for a short while.",
        "The Witchlight Carnival (Halloween) feels like home to me.",
        "I can't bring myself to harm a Fey creature, either because I consider myself one or because I fear the repercussions.",
        "A trusted friend is the most important thing in the multiverse to me.",
        "I do what I can to protect the natural world.",
        "I find magic in all its forms to be compelling. The more magical a place, the more I am drawn to it.",
        "I would never break my word.",
        "Rule of Three. Everything in the multiverse happens in threes. I see the 'rule of three' everywhere.",
        "I can't bring myself to trust most adults.",
        "I live by my own set of weird and wonderful rules.",
        "When I have a new idea, I get wildly excited about it until I come up with another, better idea.",
        "I have never lost my childlike sense of wonder.",
        "Wherever I go, I try to bring a little of the warmth and tranquility of home with me.",
        "Good music makes me weep like a baby.",
        "Like a nomad, I can't settle down in one place for very long.",
        "I'm haunted by fey laughter that only I can hear, though I know it's just my mind playing tricks on me.",
        "Flowers wilt in my presence.",
        "Flowers bloom in my presence.",
        "My skin sparkles in sunlight.",
        "My skin sparkles in moonlight.",
        "I have a sweet scent, like that of nectar or honey",
        "My eyes swirl with iridescent colors.",
        "I consider the adherents of other gods to be deluded innocents at best, or ignorant fools at worst.",
        "I don't take kindly to some of the actions and motivations of the people of this land, because these folk are different from me.",
        "I have a weakness for the new intoxicants and other pleasures of this land.",
        "I pretend not to understand the local language in order to avoid interactions I would rather not have.",
        "I am secretly (or not so secretly) convinced of the superiority of my own culture over that of this foreign land.",
        "Though I had no choice, I lament having to leave my loved ones behind. I hope to see them again one day.",
        "I'm fascinated by the beauty and wonder of this new land.",
        "My freedom is my most precious possession. I'll never let anyone take it from me again.",
        "I hold no greater cause than my service to my people.",
        "The gods of my people are a comfort to me so far from home.",
        "So long as I have this token from my homeland, I can face any adversity in this strange land.",
        "I begin or end my day with small traditional rituals that are unfamiliar to those around me.",
        "I honor my deities through practices that are foreign to this land.",
        "I express affection or contempt in ways that are unfamiliar to others.",
        "I have a strong code of honor or sense of propriety that others don't comprehend.",
        "I have my own ideas about what is and is not food, and I find the eating habits of those around me fascinating, confusing, or revolting.",
        "I have different assumptions from those around me concerning personal space, blithely invading others' space in innocence, or reacting to ignorant invasion of my own.",
        "I see morality entirely in black and white.",
        "I think far ahead, a detachedness often mistaken for daydreaming.",
        "I overexert myself, sometimes needing to recuperate for a day or more.",
        "I have no sense of humor. Laughing is uncomfortable and embarrassing.",
        "I never make eye contact.",
        "I always make eye contact and hold it unflinchingly.",
        "I an callous about death. It comes to us all eventually.",
        "I am ever learning how to be among others—when to stay quiet, when to laugh.",
        "I cultivate a single obscure hobby or study and eagerly discuss it at length.",
        "I think far ahead, a detachedness often mistaken for daydreaming.",
        "I sleep just as much as I need to and on an unusual schedule.",
        "I treasure a memento of a person or instance that set me upon my path.",
        "I strive to have no personality—it's easier to forget what's hardly there.",
        "I'm earnest and uncommonly direct.",
        "Despite my best efforts, I am unreliable to my friends.",
        "I have trouble keeping my true feelings hidden. My sharp tongue lands me in trouble.",
        "A scandal prevents me from ever going home again. That kind of trouble seems to follow me around.",
        "I'm a sucker for a pretty face.",
        "I'll do anything to win fame and renown.",
        "I idolize a hero of the old tales and measure my deeds against that person's.",
        "I change my mood or my mind as quickly as I change key in a song.",
        "I'll settle for nothing less than perfection.",
        "I get bitter if I'm not the center of attention.",
        "I love a good insult, even one directed at me.",
        "Nobody stays angry at me or around me for long, since I can defuse any amount of tension.",
        "I'm a hopeless romantic, always searching for that 'special someone.'",
        "Whenever I come to a new place, I collect local rumors and spread gossip.",
        "I know a story relevant to almost every situation.",
        "An innocent person is in prison for a crime that I committed. I'm okay with that.",
        "I turn tail and run when things look bad.",
        "I have a 'tell' that reveals when I'm lying.",
        "If there's a plan, I'll forget it. If I don't forget it, I'll ignore it.",
        "When faced with a choice between money and my friends, I usually choose the money.",
        "When I see something valuable, I can't think about anything but how to steal it.",
        "I blow up at the slightest insult.",
        "The best way to get me to do something is to tell me I can't do it.",
        "I don't pay attention to the risks in a situation. Never tell me the odds.",
        "I am incredibly slow to trust. Those who seem the fairest often have the most to hide.",
        "I would rather make a new friend than a new enemy.",
        "The first thing I do in a new place is note the locations of everything valuable – or where such things could be hidden.",
        "I am always calm, no matter what the situation. I never raise my voice or let my emotions control me.",
        "I always have a plan for what to do when things go wrong.",
        "I hate to admit it and will hate myself for it, but I'll run and preserve my own hide if the going gets tough.",
        "I can't resist swindling people who are more powerful than me.",
        "I'm too greedy for my own good. I can't resist taking a risk if there's money involved.",
        "I'm convinced that no one could ever fool me the way I fool others.",
        "I'm always in debt. I spend my ill-gotten gains on decadent luxuries faster than I bring them in.",
        "I can't resist a pretty face.",
        "I pocket anything I see that might have some value.",
        "I keep multiple holy symbols on me and invoke whatever deity might come in useful at any given moment.",
        "Sarcasm and insults are my weapons of choice.",
        "I lie about almost everything, even when there's no good reason to.",
        "I'm a born gambler who can't resist taking a risk for a potential payoff.",
        "Flattery is my preferred trick for getting what I want.",
        "I have a joke for every occasion, especially occasions where humor is inappropriate.",
        "I fall in and out of love easily, and am always pursuing someone.",
        "I convince people that worthless junk is worth their hard-earned money.",
        "I run sleight-of-hand cons on street corners.",
        "I put on new identities like clothes.",
        "I insinuate myself into people's lives to secure their fortunes.",
        "I shave coins or forge documents.",
        "I cheat at games of chance.",
        "I must be the captain of any group I join.",
        "Any defeat or failure on my part is because my opponents cheated.",
        "I have lingering pain of old injuries.",
        "I ignore anyone who doesn't compete and anyone who loses to me.",
        "I'll do absolutely anything to win.",
        "I indulge in a habit that threatens my reputation or health.",
        "I strive to live up to a specific hero's example.",
        "The person who trained me is the most important person in my world.",
        "My teammates are my family.",
        "I get irritated if people praise someone else and not me.",
        "Anything worth doing is worth doing best.",
        "I love to trade banter and gibes.",
        "When I see others struggling, I offer to help.",
        "Obstacles exist to be overcome.",
        "I have a daily exercise routine I refuse to break.",
        "I don't like to sit idle.",
        "I feel most at peace during physical exertion, whether exercise or battle.",
        "I can't sleep except in total darkness.",
        "When given the choice of going left or right, I always go left.",
        "I have no time for friends or family. I spend every waking moment thinking about and preparing for my next expedition.",
        "When I'm not exploring dungeons or ruins, I get jittery and impatient.",
        "I can't leave a room without searching it for secret doors.",
        "I have a secret fear of some common wild animal – and in my work, I see them everywhere.",
        "You might think I'm a scholar, but I love a good brawl. These fists were made for punching.",
        "I might fail, but I will never give up.",
        "I have no qualms about stealing from the dead.",
        "I love a good puzzle or mystery.",
        "I'm a pack rat who never throws anything away.",
        "I wear a tribal mask and never take it off.",
        "I complain about everything.",
        "I've picked up some unpleasant habits living among races such as goblins, lizardfolk, or orcs.",
        "I believe that I'm intellectually superior to people from other cultures and have much to teach them.",
        "Boats make me seasick.",
        "I talk to myself, and I don't make friends easily.",
        "When I arrive at a new settlement for the first time, I must learn all its customs.",
        "I would risk life and limb to discover a new culture or unravel the secrets of a dead one.",
        "By living among violent people, I have become desensitized to violence.",
        "I would rather observe than meddle.",
        "I prefer the company of those who aren't like me, including people of other races.",
        "I'm a stickler when it comes to observing proper etiquette and local customs.",
        "I judge others harshly, and myself even more severely.",
        "I put too much trust in those who wield power within my temple's hierarchy.",
        "My piety sometimes leads me to blindly trust those that profess faith in my god.",
        "I am inflexible in my thinking.",
        "I am suspicious of strangers and expect the worst of them.",
        "Once I pick a goal, I become obsessed with it to the detriment of everything else in my life.",
        "Adaptable: Shows flexibility and versatility regardless of the situation. Thinks quickly.",
        "Since no one else is stepping up, I will.",
        "Adventurous. Willing to try new experiences and take risks.",
        "Affectionate: Shows open fondness for others",
        "Compassionate. Will prevent damage to others. ",
        "In Alert. Aware of and watchful for possible change or danger.",
        "I plan ahead. Always having an exit strategy",
        "I am highly observant",
        "I am ambitious.",
        "I am confident and prideful",
        "I am analytical, logical, rational.",
        "I am highly curious.",
        "I fear making a mistake.",
        "I am bold and intrepid.",
        "I desire to prove myself",
        "I am driven by a strong sense of righteousness: The belief in a higher power or purpose",
        "I am calmed, and inclined toward tranquility and serenity",
        "I have a higher purpose.",
        "I have a boring personality.",
        "I enjoy simple pleasures",
        "I am cautious, given to prudent forethought before acting.",
        "They are wise.",
        "They are charming",
        "They are confident, fully assured of themself",
        "I am cooperative.",
        "They are courageous.",
        "They are courteous, friendly, and have good maners.",
        "They are curious. Marked by the desire to investigate and learn",
        "They have the ability to make quick, efficient decisions; lacking hesitation.",
        "They are diplomatic: Skilled at handling people while respecting their needs",
        "They are disciplined: Exhibiting willpower and self-control.",
        "They are strongly dedicated to a goal or belief",
        "They are Carefree and relaxed.",
        "They are enthusiastic: Frequently feeling or exhibiting much excitement.",
        "They are generous, altruistic, philanthropic.",
        "They are harsh, brusque, and violent.",
        "They are honorable, having noble principles and displaying integrity.",
        "They are passionate, capable of or expressing deep feeling.",
        "They are patient. Exhibiting self-control and composure under trial or strain.",
        "They are patriotic. Having love for or loyalty to their country.",
        "They are persistent: Stubbornly continuing on despite opposition, difficulty, or danger.",
        "They are playful, immature, and cheerful.",
        "They are protective.",
        "Traps don't make me nervous. Idiots who trigger traps make me nervous.",
        "I'm happier in a dusty old tomb than I am in the centers of civilization.",
        "Fame is more important to me than money.",
        "I pursue wealth to secure someone's love.",
        "I'll do anything to get my hands on something rare or priceless.",
        "I'm quick to assume that someone is trying to cheat me.",
        "I'm never satisfied with what I have – I always want more.",
        "I would kill to acquire a noble title.",
        "My kind are my family. I would do anything for them.",
        "I hide scraps of food and trinkets away in my pockets.",
        "I ask a lot of questions.",
        "I like to squeeze into small places where no one else can get to me.",
        "I sleep with my back to a wall or tree, with everything I own wrapped in a bundle in my arms.",
        "I eat like a pig and have bad manners.",
        "I think anyone who's nice to me is hiding evil intent.",
        "I don't like to bathe.",
        "I bluntly say what other people are hinting at or hiding.",
        "I am no common criminal; I am a mastermind.",
        "My friends know they can rely on me, no matter what.",
        "I work hard so that I can play hard when the work is done.",
        "I enjoy sailing into new ports and making new friends over a flagon of ale.",
        "I stretch the truth for the sake of a good story.",
        "To me, a tavern brawl is a nice way to get to know a new city.",
        "I never pass up a friendly wager.",
        "My language is as foul as a stable.",
        "I like a job well done, especially if I can convince someone else to do it.",
        "It is my duty to protect my students.",
        "An injury to the unspoiled wilderness of my home is an injury to me.",
        "My kind (family, clan, or tribe) is the most important thing in my life, even when they are far from me.",
        ""
    ]

    if background == "Expert":
        return random.choice(Traits + [
            "I'm horribly jealous of anyone who can outshine my handiwork. Everywhere I go, I'm surrounded by rivals.",
            "No one must ever learn that I once stole money from guild coffers.",
            "One day I will return to my guild and prove that I am the greatest artisan of them all.",
            "The workshop where I learned my trade is the most important place in the world to me.",
            "I created a great work for someone, and then found them unworthy to receive it. I'm still looking for someone worthy.",
            "I owe my guild a great debt for forging me into the person I am today.",
            "I will get revenge on the evil forces that destroyed my place of business and ruined my livelihood.",
            "I get frustrated to the point of distraction by shoddy craftsmanship.",
            "Though I am an excellent crafter, my work tends to look as though it belongs on a ship.",
            "I am so obsessed with sketching my ideas for elaborate inventions that I sometimes forget little thing like eating and sleeping.",
            "I'm judgmental of those who are not skilled with tools of some kind.",
            "I sometimes take things that don't belong to me, especially if they are very well made."
        ])

    if background == "Priest" or background == "Cultist":
        return random.choice(Traits + [
            "I was partaking of communal living in accordance with the dictates of a religious order.",
            "They idolize a particular hero of my faith, and constantly refer to that person's deeds and example.",
            "I can find common ground between the fiercest enemies, empathizing with them and always working toward peace.",
            "I see omens in every event and action. The gods try to speak to us, we just need to listen.",
            "Nothing can shake my optimistic attitude.",
            "I quote (or misquote) sacred texts and proverbs in almost every situation.",
            "I am tolerant  of other faiths and respect the worship of other gods.",
            "I am intolerant of other faiths and condemn the worship of other gods.",
            "I've enjoyed fine food, drink, and high society among my temple's elite. Rough living grates on me.",
            "I've spent so long in the temple that I have little practical experience dealing with people in the outside world.",
            "Nothing is more important than the other members of my hermitage, order, or association.",
            ""])
    if background == "Bard":
        return random.choice(Traits + [
            "My instrument is my most treasured possession, and it reminds me of someone I love."
        ])

    return random.choice(Traits)


def Ideal(background, alignment):

    if background == "Noble":
        if ("Good" in alignment) and Dice() == 1:
            return random.choice([
                "Noble Obligation. It is my duty to protect and care for the people beneath me.",
                "Respect. Respect is due to me because of my position, but all people regardless of station deserve to be treated with dignity."
            ])

    if background == "Priest":
        if "Lawful" in alignment and Dice() == 1:
            return random.choice([
                "Tradition. The ancient traditions of worship and sacrifice must be preserved and upheld.",
                "Faith. I trust that my deity will guide my actions. I have faith that if I work hard, things will go well."
            ])
        if "Good" in alignment and Dice() == 1:
            return random.choice(
                ["Charity. I always try to help those in need, no matter what the personal cost."
                 ])
        if "Chaotic" in alignment and Dice() == 1:
            return random.choice([
                "Change. We must help bring about the changes the gods are constantly working in the world."
            ])

    if background == "Charlatan":
        if "Chaotic" in alignment and Dice() == 1:
            return random.choice([
                "Independence. I am a free spirit – no one tells me what to do.",
                "Creativity. I never run the same con twice."
            ])
        if "Lawful" in alignment and Dice() == 1:
            return random.choice([
                "Fairness. I never target people who can't afford to lose a few coins."
            ])
        if "Good" in alignment and Dice() == 1:
            return random.choice([
                "Fairness. I never target people who can't afford to lose a few coins.",
                "Charity. I distribute the money I acquire to the people who really need it.",
                "Friendship. Material goods come and go. Bonds of friendship last forever."
            ])

    if background == "Commoner":
        if "Good" in alignment and Dice() == 1:
            return random.choice([
                "Camaraderie. Good people make even the longest voyage bearable."
            ])
        if "Lawful" in alignment and Dice() == 1:
            return random.choice([
                "Luck. Our luck depends on respecting its rules—now throw this salt over your shoulder."
            ])
        if "Chaotic" in alignment and Dice() == 1:
            return random.choice([
                "Daring. The richest bounty goes to those who risk everything."
            ])
        if "Neutral" in alignment and Dice() == 1:
            return random.choice([
                "Balance. Do not fish the same spot twice in a row; suppress your greed, and nature will reward you."
            ])

    if background == "Criminal" or background == "Bandit":
        if "Lawful" in alignment and Dice() == 1:
            return random.choice([
                "Honor. I don't steal from others in the trade.",
            ])
        if "Chaotic" in alignment and Dice() == 1:
            return random.choice([
                "Freedom. Chains are meant to be broken, as are those who would forge them.",
            ])
        if "Good" in alignment and Dice() == 1:
            return random.choice([
                "Charity. I steal from the wealthy so that I can help people in need.",
                "Redemption. There's a spark of good in everyone",
            ])
        if "Evil" in alignment and Dice() == 1:
            return random.choice([
                "Greed. I will do whatever it takes to become wealthy.",
                "Plunder. Take all that you can and leave nothing for the scavengers.",
            ])
        if "Neutral" in alignment and Dice() == 1:
            return random.choice([
                "People. I'm loyal to my friends, not to any ideals, and everyone else can take a trip down the Styx for all I care."
            ])


    if background == "Pirate":
        if "Good" in alignment and Dice() == 1:
            return random.choice([
                "Crew. If everyone on deck pitches in, we'll never sink.",
                "Respect. The thing that keeps a ship together is mutual respect between captain and crew."
            ])
        if "Lawful" in alignment and Dice() == 1:
            return random.choice([
                "Careful Lines. A ship must be balanced according to the laws of the universe.",
                "Fairness. We all do the work, so we all share in the rewards."
            ])
        if "Chaotic" in alignment and Dice() == 1:
            return random.choice([
                "Freedom. The sea is freedom-the freedom to go anywhere and do anything."
            ])
        if "Evil" in alignment and Dice() == 1:
            return random.choice([
                "Mastery. I'm a predator, and the other ships on the sea are my prey."
            ])
        if "Neutral" in alignment and Dice() == 1:
            return random.choice([
                "People. I'm committed to my crewmates, not to ideals. "
            ])
        if Dice() == 1:
            return random.choice([
                "Aspiration. Someday I'll own my own ship and chart my own destiny."
            ])

    if background == "Scholar":
        if "Lawful" in alignment and Dice() == 1:
            return random.choice(
                ["Distance. One must not interfere with the affairs of another culture – even one in need of aid.",
                 "Power. Common people crave strong leadership, and I do my utmost to provide it.",
                 "Dignity. The dead and their belongings deserve to be treated with respect."
                 ])
        if "Good" in alignment and Dice() == 1:
            return random.choice([
                "Protection. I must do everything possible to save a society facing extinction.",
                "Preservation. That artifact belongs in a museum."
            ])
        if "Evil" in alignment and Dice() == 1:
            return random.choice([
                "Indifferent. Life is cruel. What's the point in saving people if they're going to die anyway?"
            ])
        if "Chaotic" in alignment and Dice() == 1:
            return random.choice([
                "Death Wish. Nothing is more exhilarating than a narrow escape from the jaws of death."
            ])

    if background == "Bard":
        if "Good" in alignment and Dice() == 1:
            return random.choice([
                "Beauty. When I perform, I make the world better than it was."
            ])
        if "Lawful" in alignment and Dice() == 1:
            return random.choice([
                "Tradition. The stories, legends, and songs of the past must never be forgotten, for they teach us who we are."
            ])
        if "Chaotic" in alignment and Dice() == 1:
            return random.choice([
                "Creativity. The world is in need of new ideas and bold action.",
                "Invention. Make what you need out of whatever is at hand. "
            ])
        if "Evil" in alignment and Dice() == 1:
            return random.choice([
                "Greed. I'm only in it for the money and fame.",
                "Perfection. To measure a being and find it lacking is the greatest disappointment",
            ])
        if "Neutral" in alignment and Dice() == 1:
            return random.choice([
                "People. I like seeing the smiles on people's faces when I perform. That's all that matters."
            ])
        if Dice() == 1:
            return random.choice([
                "Honesty. Art should reflect the soul; it should come from within and reveal who we really are."
            ])

    if background == "Traveler":
        if "Good" in alignment and Dice() == 1:
            return random.choice([
                "Open. I have much to learn from the kindly folk I meet along my way."
            ])
        if "Lawful" in alignment and Dice() == 1:
            return random.choice([
                "Reserved. As someone new to these strange lands, I am cautious and respectful in my dealings."
            ])
        if "Chaotic" in alignment and Dice() == 1:
            return random.choice([
                "Wanderlust. I prefer to take the less traveled path",
                "Adventure. I'm far from home, and everything is strange and wonderful!"
            ])
        if "Evil" in alignment and Dice() == 1:
            return random.choice([
                " Cunning. Though I may not know their ways, neither do they know mine, which can be to my advantage."
            ])
        if "Neutral" in alignment and Dice() == 1:
            return random.choice([
                "Inquisitive. Everything is new, but I have a thirst to learn."
            ])

    if background == "Criminal":
        if "Lawful" in alignment and Dice() == 1:
            return random.choice([
                "Smuggler's Code I uphold the unwritten rules of the smugglers, who do not cheat one another or directly harm innocents."
            ])
        if "Good" in alignment and Dice() == 1:
            return random.choice([
                "Peace and Prosperity I smuggle only to achieve a greater goal that benefits my community."
            ])
        
    if background == "Warrior":
        if "Chaotic" in alignment and Dice() == 1:
            return random.choice([
                "Competition. I strive to test myself in all things."
            ])
        if "Evil" in alignment and Dice() == 1:
            return random.choice([
                "Triumph. The best part of winning is seeing my rivals brought low."
            ])
        if "Good" in alignment and Dice() == 1:
            return random.choice([
                "Camaraderie. The strongest bonds are forged through struggle."
            ])
        if "Neutral" in alignment and Dice() == 1:
            return random.choice([
                "People. I strive to inspire my spectators."
            ])
        if "Lawful" in alignment and Dice() == 1:
            return random.choice([
                "Tradition. Every game has rules, and the playing field must be level."
            ])

    if "Good" in alignment and Dice() == 1:
        return random.choice([
            "Teamwork. Success depends on cooperation and communication.",
            "Greater Good. Our lot is to lay down our lives in defense of others.",
            "Common Good. My organization serves a vital function, and its prosperity will help everyone.",
            "Greater Good. My gifts are meant to be shared with all, not used for my own benefit.",
            "Greater Good. I kill monsters to make the world a safer place, and to exorcise my own demons.",
            "Selflessness. I try to help those in need, no matter what the personal cost.",
            "Generosity. My talents were given to me so that I could use them to benefit the world.",
            "Empathy. No creature should be made to suffer.",
            "Respect. People deserve to be treated with dignity and respect.",
            "Friendship. I never leave a friend behind. ",
            "Respect. All people, rich or poor, deserve respect.",
            "Beauty. What is beautiful points us beyond itself toward what is true.",
            "Greater Good. It is each person's responsibility to make the most happiness for the whole tribe.",
        ])
    if "Chaotic" in alignment and Dice() == 1:
        return random.choice([
            "Embracing. Life is messy. Throwing yourself into the worst of it is necessary to get the job done.",
            "Independence. I must prove that I can handle myself without the coddling of my family.",
            "Change. Life is like the seasons, in constant change, and we must change with it.",
            "No Limits. Nothing should fetter the infinite possibility inherent in all existence.",
            "Independence. When people follow orders blindly, they embrace a kind of tyranny",
            "Innovation. Abandon old traditions and find better ways to do things.",
            "Free Thinking. Inquiry and curiosity are the pillars of progress.",
            "Freedom. I have a dark calling that puts me above the law.",
            "Freedom. Everyone should be free to pursue his or her own livelihood.",
            "Freedom. Tyrants must not be allowed to oppress the people.",
            "Changeability. Change is good, which is why I live by an ever-changing set of rules.",
            "Change. The low are lifted up, and the high and mighty are brought down. Change is the nature of things."
        ])
    if "Lawful" in alignment and Dice() == 1:
        return random.choice([
            "Code. The code provides a solution for every problem, and following it is imperative.",
            "Responsibility. It is my duty to respect the authority of those above me, just as those below me must respect mine.",
            "Honor. If I dishonor myself, I dishonor my whole kind.",
            "Logic. Emotions must not cloud our logical thinking.",
            "Responsibility. I do what I must and obey just authority.",
            "Tradition. I uphold traditions of my kind and bring honor to my family.",
            "Logic. Emotions must not cloud our sense of what is right and true, or our logical thinking.",
            "Logic. I like to know my enemy’s capabilities and weaknesses before rushing into battle.",
            "Community. It is the duty of all civilized people to strengthen the bonds of community and the security of civilization.",
            "Fairness. No one should get preferential treatment before the law, and no one is above the law.",
            "Honor. A deal is a deal, and I would never break one.",
            "Community. We have to take care of each other, because no one else is going to do it."
        ])
    if "Evil" in alignment and Dice() == 1:
        return random.choice([
            "Might. The strong train so that they might rule those who are weak.",
            "Power. If I can attain more power, no one will tell me what to do.",
            "Power. Knowledge is the path to power and domination.",
            "All for a Coin. I'll do nearly anything if it means I turn a profit.",
            "Might. In life as in war, the stronger force wins.",
            "Power. I want to ensure the prosperity of my kind and wield its power myself.",
            "Destruction. I’m a monster that destroys other monsters, and anything else that gets in my way.",
            "Greed. I'm only in it for the money.",
            "Might. If I become strong, I can take what I want – what I deserve.",
            "Obsession. I won't let go of a grudge",
            "Greed. I will do whatever it takes to get what I want, regardless of the harm it might cause.",
            "Confusion. Deception is a weapon. Strike from where your foes won't expect.",
            "Retribution. The rich need to be shown what life and death are like in the gutters.",
            "Might. The strongest are meant to rule.",
            "Greed. The gods make people constantly, but only made a certain quantity of gold.",
            "Power. The gods show me their favour by allowing my success and power. If they favoured others, they wouldn't be in suffering. It's theis own fault for not gaining their favour."
        ])
    if "Neutral" in alignment and Dice() == 1:
        return random.choice([
            "People. I help the people who help me-that's what keeps us alive.",
            "People. I'm committed to the people I care about, not to ideals.",
            "Danger. With every great discovery comes grave danger. The two walk hand in hand.",
            "Sincerity. There's no good in pretending to be something I'm not.",
            "Live and Let Live. Ideals aren't worth killing over or going to war for.",
            "Nature. The natural world is more important than all the constructs of civilization."
        ])
    return random.choice([
        "Perseverance. No injury or obstacle can turn me from my goal.",
        "Bravery. To act when others quake in fear- this is the essence of the warrior.",
        "Family. Blood runs thicker than water.",
        "Glory. I must earn glory in battle, for myself and my clan.",
        "Self-Improvement. The goal of a life of study is the betterment of oneself.",
        "Knowledge. The path to power and self-improvement is through knowledge.",
        "Hope. The horizon at sea holds the greatest promise.",
        "Reflection. Muddied water always clears in time.",
        "Daring. I am most happy when risking everything.",
        "People. For all my many lies, I place a high value on friendship.",
        "Wealth. Heaps of coins in a secure vault is all I dream of.",
        "Nation. My city, nation, or people are all that matter.",
        "Aspiration. I'm going to prove that I'm worthy of a better life.",
        "Comfort. I want to ensure that me and mine enjoy the best things in life.",
        "Discovery. I want to learn all I can, both for my organization and for my own curiosity.",
        "Self-Knowledge. If you know yourself, there's nothing left to know.",
        "Live and Let Live. Meddling in the affairs of others only causes trouble.",
        "Power. Solitude and contemplation are paths toward mystical or magical power.",
        "Determination. I’ll stop the spirits that haunt me or die trying.",
        "Aspiration. I work hard to be the best there is at my craft.",
        "Suspicious. I must be careful, for I have no way of telling friend from foe here.",
        "Destiny. Nothing and no one can steer me away from my higher calling.",
        "Anonymity. It's my deeds that should be remembered, not their instrument.",
        "Incorruptibility. Be a symbol, and leave your flawed being behind.",
        "Infamy. My name will be a malediction, a curse that fulfills my will.",
        "Security. Doing what must be done can't bring the innocent to harm.",
        "Justice. Place in society shouldn't determine one's access to what is right. ",
        "Discovery. I want to be the first person to discover a lost culture.",
        "Knowledge. By understanding other races and cultures, we learn to understand ourselves.",
        "Immortality. All my exploring is part of a plan to find the secret of everlasting life.",
        "Aspiration. I seek to prove myself worthy of my deity's favor by matching my actions against their teachings.",
        "Greed. I won't risk my life for nothing. I expect some kind of payment.",
        "Growth. Lessons hide in victory and defeat",
        "Aspiration. I'm determined to make something of myself.",
        "Hard Work. No sea can beat me if I fight hard.",
        ""
    ])

def AbilityScoresGeneration(rc = ""):
    ### Ability Scores Generation
    STR = AbilityScore()
    DEX = AbilityScore()
    CON = AbilityScore()
    INT = AbilityScore()
    WIS = AbilityScore()
    CHA = AbilityScore()

  


    ### Race-based Ability Score Adjustments

    if rc == "Human":
        # All humans have a baseline adaptability, hence the small boost to every ability score.
        STR += 1
        DEX += 1
        CON += 1
        INT += 1
        WIS += 1
        CHA += 1

        human_type = random.choice(["Highlander", "Nomad", "Islander", "Scholar", "Forester", "Plainsfolk", "Urbanite"])

        if human_type == "Highlander":
            # Bonus to strength and constitution due to the challenging environment.
            STR += Dice(2)
            CON += Dice(2)
        elif human_type == "Nomad":
            # Bonus to constitution for their endurance and wisdom for their survival skills.
            CON += Dice(3)
            WIS += Dice(2)
        elif human_type == "Islander":
            # Bonus to dexterity for their agility and charisma for their storytelling traditions.
            DEX += Dice(3)
            CHA += Dice(2)
        elif human_type == "Scholar":
            # Bonus to intelligence and wisdom due to their pursuit of knowledge.
            INT += Dice(3)
            WIS += Dice(2)
        elif human_type == "Forester":
            # Bonus to dexterity for their agility in the woods and wisdom for their understanding of nature.
            DEX += Dice(2)
            WIS += Dice(3)
        elif human_type == "Plainsfolk":
            # Bonus to constitution and strength for their grounded nature.
            CON += Dice(2)
            STR += Dice(2)
        elif human_type == "Urbanite":
            # Bonus to charisma and intelligence for their social adeptness and cunning.
            CHA += Dice(3)
            INT += Dice(2)
    if rc == "Aberration":
        CON += Dice(6)  # Aberrations often have hardy constitutions due to their alien nature.
        
        aberration_type = random.choice(["Eldritch Horror", "Deep Dweller", "Reality Warper", "Psionic Entity"])

        if aberration_type == "Eldritch Horror":
            # Bonus to charisma due to their terrifying presence and wisdom for their ancient knowledge.
            CHA += Dice(3)
            WIS += Dice(2)
        elif aberration_type == "Deep Dweller":
            # Bonus to strength for their adaptability to high pressures and dexterity for navigating the dark depths.
            STR += Dice(2)
            DEX += Dice(3)
        elif aberration_type == "Reality Warper":
            # Bonus to intelligence for their manipulation of realities and wisdom for perceiving alternate dimensions.
            INT += Dice(3)
            WIS += Dice(2)
        elif aberration_type == "Psionic Entity":
            # Bonus to intelligence for their psychic capabilities and charisma for their mental influence.
            INT += Dice(6)
            CHA += Dice(3)

    if rc == "Aven":
        DEX += Dice(6)  # Avens, being bird-like, generally have good agility and coordination.
        
        aven_type = random.choice(["Raptor", "Songbird", "Waterfowl", "Flightless Bird"])

        if aven_type == "Raptor":
            # Bonus to wisdom for their keen senses and dexterity for their agile flight.
            WIS += Dice(2)
            DEX += Dice(2)
        elif aven_type == "Songbird":
            # Bonus to charisma for their pleasant vocalizations and dexterity for nimbleness.
            CHA += Dice(3)
            DEX += Dice(1)
        elif aven_type == "Waterfowl":
            # Bonus to constitution for being hardy and adaptability in water environments.
            CON += Dice(4)
        elif aven_type == "Flightless Bird":
            # Bonus to strength due to their strong legs and possibly larger size.
            STR += Dice(3)

    if rc == "Beast":
        CON += Dice(6)
        beast_type = random.choice(["Predator", "Grazer", "Small Mammal", "Aquatic Animal", "Avian", "Reptilian"])

        if beast_type == "Predator":
            STR += Dice(4)
            DEX += Dice(2)
            WIS += Dice(2)  # Representing their keen hunting senses
        elif beast_type == "Grazer":
            CON += Dice(4)  # Many grazers are sturdy animals
            WIS += Dice(2)  # For their awareness of the surroundings
        elif beast_type == "Small Mammal":
            DEX += Dice(4)  # Agile and quick
            INT += Dice(2)  # Some small mammals exhibit surprising cleverness
        elif beast_type == "Aquatic Animal":
            DEX += Dice(3)  # Good swimmers
            CON += Dice(3)  # Adapted to aquatic life
        elif beast_type == "Avian":
            DEX += Dice(4)  # For their flying capabilities
            WIS += Dice(2)  # Keen senses, especially sight
        elif beast_type == "Reptilian":
            STR += Dice(2)
            CON += Dice(4)  # Many reptiles have tough hides or scales

        
    if rc == "Beastfolk":
        beastfolk_type = random.choice(["Equine Folk", "Bovine Folk", "Canine Folk", "Feline Folk", "Caprine Folk", "Ursine Folk"])

        if beastfolk_type == "Equine Folk":
            STR += Dice(3)
            DEX += Dice(3)  # Representing their speed and agility
            WIS += Dice(2)  # Keen senses
        elif beastfolk_type == "Bovine Folk":
            STR += Dice(4)  
            CON += Dice(4)  # Sturdy constitution
        elif beastfolk_type == "Canine Folk":
            DEX += Dice(3)  # Agile
            WIS += Dice(4)  # Keen senses and awareness
        elif beastfolk_type == "Feline Folk":
            DEX += Dice(4)  # Graceful and fast
            CHA += Dice(2)  # Perhaps representing a regal or charismatic nature
        elif beastfolk_type == "Caprine Folk":
            DEX += Dice(3)  # Agile, especially in mountainous terrain
            CHA += Dice(3)  # Playful or whimsical nature
        elif beastfolk_type == "Ursine Folk":
            STR += Dice(5)  # Bear-like strength
            CON += Dice(3)  # Tough constitution

    if rc == "Celestial":
        WIS += Dice(3)
        CHA += Dice(3)
        celestial_type = random.choice(["Angelic Guardians", "Astral Avatars", "Seraphim", "Cherubim", "Spiritual Messengers"])

        if celestial_type == "Angelic Guardians":
            STR += Dice(3)
            WIS += Dice(4)  # For their divine insight
            CHA += Dice(3)  # Radiant presence
        elif celestial_type == "Astral Avatars":
            INT += Dice(4)  # Cosmic knowledge
            WIS += Dice(3)
            CHA += Dice(3)  # Mysterious aura
        elif celestial_type == "Seraphim":
            STR += Dice(3)
            CON += Dice(3)  # Fiery endurance
            WIS += Dice(5)  # Closest to divine presence
        elif celestial_type == "Cherubim":
            STR += Dice(4)  
            INT += Dice(3)
            WIS += Dice(3)
        elif celestial_type == "Spiritual Messengers":
            DEX += Dice(4)  # Speed in delivering messages
            CHA += Dice(4)  # Charisma for delivering divine edicts

    if rc == "Construct":
        STR += Dice(3)
        CON += Dice(3)
        construct_type = random.choice(["Stone Golem", "Iron Golem", "Wooden Puppet", "Clockwork Automaton", "Magical Sentinel", "Homunculus"])

        if construct_type == "Stone Golem":
            STR += Dice(5)
            CON += Dice(5)  # Durability
        elif construct_type == "Iron Golem":
            STR += Dice(6)  # Peak strength
            CON += Dice(4)
        elif construct_type == "Wooden Puppet":
            DEX += Dice(5)  # Agility
            CHA += Dice(3)  # Often carved in humanoid forms, potentially charming
        elif construct_type == "Clockwork Automaton":
            DEX += Dice(4)
            INT += Dice(4)  # Precision
        elif construct_type == "Magical Sentinel":
            INT += Dice(5)  # Magical prowess
            WIS += Dice(3)
            CHA += Dice(3)  # Enigmatic presence
        elif construct_type == "Homunculus":
            INT += Dice(3)
            CHA += Dice(4)  # Unnatural allure


    if rc == "Dragon":
        STR += Dice(8)  # For their raw physical power.
        DEX += Dice(3)  # While they're big, many dragons are also agile, especially in flight.
        CON += Dice(6)  # They're resilient creatures.
        INT += Dice(3)  # Many dragons are depicted as highly intelligent.
        WIS += Dice(3)  # Their long lifespans grant them vast wisdom.
        CHA += Dice(8)  # Their mere presence is often enough to command respect or instill fear.

        age_category = random.choice(["Wyrmling", "Young", "Adult", "Ancient"])
        dragon_type = random.choice(["Red", "Blue", "Green", "White", "Black", "Gold", "Silver", "Bronze", "Brass", "Copper"])

        # Age-based adjustments
        if age_category == "Wyrmling":
            STR += Dice(3)
            CON += Dice(3)
            INT += Dice(2)
        elif age_category == "Young":
            STR += Dice(4)
            CON += Dice(4)
            INT += Dice(3)
        elif age_category == "Adult":
            STR += Dice(6)
            CON += Dice(6)
            INT += Dice(5)
        elif age_category == "Ancient":
            STR += Dice(8)
            CON += Dice(8)
            INT += Dice(7)

        # Type-based adjustments
        if dragon_type == "Red":
            CHA += Dice(4)  # Fiery presence
            CON += Dice(2)  # Resilience to fire
        elif dragon_type == "Blue":
            INT += Dice(3)  # Cunning
            DEX += Dice(2)  # Quick reflexes for lightning attacks
        elif dragon_type == "Green":
            WIS += Dice(3)  # Manipulation
            CON += Dice(2)  # Resistance to poison
        elif dragon_type == "White":
            STR += Dice(3)  # Raw power
            CON += Dice(3)  # Resilience to cold
        elif dragon_type == "Black":
            DEX += Dice(3)  # Stealth
            CON += Dice(2)  # Acid resistance
        elif dragon_type == "Gold":
            CHA += Dice(4)  # Nobility and charisma
            WIS += Dice(2)  # Healing prowess
        elif dragon_type == "Silver":
            WIS += Dice(4)  # Divination and insight
            CON += Dice(2)  # Cold resilience
        elif dragon_type == "Bronze":
            WIS += Dice(3)  # Coastal guardians
            STR += Dice(2)  # Strength from lightning
        elif dragon_type == "Brass":
            CHA += Dice(3)  # Gregarious nature
            DEX += Dice(2)  # Desert agility
        elif dragon_type == "Copper":
            CHA += Dice(3)  # Trickster's charm
            DEX += Dice(2)  # Acrobatics

            
        
    if rc == "Dwarf":
        STR += Dice(3)  # For their natural strength.
        CON += Dice(4)  # Known for their hardiness.
        WIS += Dice(3)  # For their accumulated knowledge and wisdom.
        if Dice(4) == 1: DEX += Dice(2)  # Some dwarves might be surprisingly agile.
        if Dice(6) == 1: INT += Dice(3)  # Some could be especially knowledgeable or clever.
        if Dice(6) == 1: CHA += Dice(2)  # A few dwarves might have a notably commanding or charismatic presence.
    if rc == "Elf":
        DEX += Dice(6)  # Elves are commonly known for their agility and grace.
        INT += Dice(3)  # Their long lifespans allow them to accumulate knowledge.
        WIS += Dice(3)  # Representing their inherent connection to the world and ancient wisdom.
    
        if Dice(4) == 1: STR += Dice(2)  # Some elves could be stronger, especially if they're warrior-types.
        if Dice(5) == 1: CON += Dice(2)  # Rarely, an elf might have more physical hardiness.
        if Dice(3) == 1: CHA += Dice(3)  # Many elves possess a natural charisma and allure.
    
    if rc == "Elemental":
        CON += Dice(4)  # Base hardiness for all elementals.
        WIS += Dice(3)  # Base elemental wisdom.
        elemental_type = random.choice(["Earth", "Air", "Fire", "Water"])  # Or however you choose the elemental type.
        if elemental_type == "Earth":
            STR += Dice(6)                      # Earth elementals are strong and sturdy.
            if Dice(4) == 1: INT += Dice(3)     # Occasionally, a deep ancient wisdom.
        elif elemental_type == "Air":
            DEX += Dice(6)                      # Air elementals are swift and elusive.
            if Dice(4) == 1: CHA += Dice(3)     # Some air elementals can be captivatingly graceful.
        elif elemental_type == "Fire":
            CHA += Dice(5)                      # Fire elementals are often seen as charismatic and passionate.
            if Dice(4) == 1: DEX += Dice(4)     # The unpredictable movement of flames.
        elif elemental_type == "Water":
            WIS += Dice(4)                      # Water elementals often have a deeper connection to the flows of life.
            if Dice(4) == 1: DEX += Dice(3)     # The ability to move fluidly and adapt to surroundings.
        
    if rc == "Fiend":
        CHA += Dice(3)
        CON += Dice(2)
        INT += Dice(3)

        fiend_type = random.choice(["Brute", "Deceiver", "Spellcaster", "Horror"])

        if fiend_type == "Brute":
            STR += Dice(6)
            if Dice(4) == 1: DEX += Dice(2)     # Occasionally, a brute fiend can be swift.
        elif fiend_type == "Deceiver":
            CHA += Dice(4)
            if Dice(4) == 1: WIS += Dice(3)     # For their insight into reading others.
        elif fiend_type == "Spellcaster":
            INT += Dice(4)                      # Boost to their arcane knowledge.
            if Dice(4) == 1: WIS += Dice(3)     # For a deeper understanding of magic.
        elif fiend_type == "Horror":
            WIS += Dice(4)                      # Represents their ability to insight terror.
            if Dice(4) == 1: CHA += Dice(3)     # Some horrors have a terrifying presence.

    if rc == "Giant":
        STR += Dice(6)  # All giants possess enormous strength.
        CON += Dice(3)  # And have a tough constitution.

        giant_type = random.choice(["Hill", "Stone", "Frost", "Fire", "Storm", "Cloud", "Forest"])

        if giant_type == "Hill":
            # Additional boosts to strength and constitution.
            STR += Dice(2)
            CON += Dice(2)
        elif giant_type == "Stone":
            # Improved constitution, and wisdom reflecting their contemplative nature.
            CON += Dice(3)
            WIS += Dice(3)
        elif giant_type == "Frost":
            # Bonus to intelligence for their cunning, and dexterity for their hunting skills.
            DEX += Dice(3)
            INT += Dice(3)
        elif giant_type == "Fire":
            # Bonus to charisma due to their commanding presence.
            CHA += Dice(4)
        elif giant_type == "Storm":
            # Bonus to wisdom and charisma for their godlike nature.
            WIS += Dice(4)
            CHA += Dice(4)
        elif giant_type == "Cloud":
            # Bonus to dexterity and charisma for their majestic nature.
            DEX += Dice(3)
            CHA += Dice(3)
        elif giant_type == "Forest":
            # Bonus to wisdom for their affinity with nature and constitution for their resilience.
            WIS += Dice(3)
            CON += Dice(3)
            
    if rc == "Gnome":
        DEX += Dice(2)
        INT += Dice(2)
        CHA += Dice(2)

        gnome_type = random.choice(["Tinkerer", "Illusionist", "Nature Lover", "Lore Keeper"])

        if gnome_type == "Tinkerer":
            DEX += Dice(3)                      # Enhanced nimbleness for intricate work.
            if Dice(4) == 1: Int += Dice(6)     # For engineering skills of tinkering.
        elif gnome_type == "Illusionist":
            CHA += Dice(3)                      # Charisma often governs spellcasting, especially illusions.
            if Dice(4) == 1: WIS += Dice(2)     # For a deeper understanding of magic.
        elif gnome_type == "Nature Lover":
            WIS += Dice(3)                      # Represents their connection with nature.
            if Dice(4) == 1: CON += Dice(2)     # For resilience in the wild.
        elif gnome_type == "Lore Keeper":
            INT += Dice(4)                      # Boosted intelligence for their vast knowledge.
            if Dice(4) == 1: CHA += Dice(2)     # As they often share tales and stories.
    if rc == "Goblin":
        DEX += Dice(3)                      # For their nimbleness.
        INT += Dice(3)                      # For their cunning and potential for strategy or invention.
        CHA += Dice(2)                      # For their often charismatic or manipulative nature.
        goblin_type = random.choice(["Skirmisher", "Tinkerer", "Shaman", "Warlord", "Schemer"])

        if goblin_type == "Skirmisher":
            DEX += Dice(4)                      # Boosted agility for hit-and-run tactics.
            if Dice(4) == 1: STR += Dice(2)     # Some physical prowess for combat.
        elif goblin_type == "Tinkerer":
            INT += Dice(3)                      # Enhanced intelligence for crafting.
            if Dice(4) == 1: DEX += Dice(3)     # Nimbleness for setting up traps.
        elif goblin_type == "Shaman":
            WIS += Dice(3)                      # Wisdom for their connection to magic.
            if Dice(4) == 1: CHA += Dice(3)     # As charisma might govern some of their spells.
        elif goblin_type == "Warlord":
            STR += Dice(4)                      # Physical strength and command.
            if Dice(4) == 1: CON += Dice(3)     # Robustness for enduring battles.
        elif goblin_type == "Schemer":
            INT += Dice(4)                      # Boosted intelligence for devising strategies.
            if Dice(4) == 1: CHA += Dice(3)     # Manipulative skills and charm.

    if rc == "Fey":
        CHA += Dice(6)
        DEX += Dice(3)

        fey_type = random.choice(["Trickster", "Noble", "Beastly", "Mystic", "Warrior", "Hag"])

        if fey_type == "Trickster":
            DEX += Dice(4)                      # Boosted agility for evasiveness.
            if Dice(4) == 1: WIS += Dice(3)     # Insight into their pranks.
        elif fey_type == "Noble":
            CHA += Dice(4)                      # Enhanced charisma for their regal presence.
            if Dice(4) == 1: INT += Dice(3)     # Intelligence for ruling and understanding fey politics.
        elif fey_type == "Beastly":
            CON += Dice(3)                      # Connection to the physical world.
            if Dice(4) == 1: WIS += Dice(3)     # Understanding of nature and its creatures.
        elif fey_type == "Mystic":
            INT += Dice(4)                      # Boosted intelligence for their magic.
            if Dice(4) == 1: WIS += Dice(3)     # Wisdom for their connection to the mystical.
        elif fey_type == "Warrior":
            STR += Dice(4)                      # Physical prowess for combat.
            if Dice(4) == 1: CON += Dice(3)     # Robustness for enduring battles.
        elif fey_type == "Hag":
            INT += Dice(4)                      # Cunning intelligence.
            if Dice(4) == 1: CHA += Dice(3)     # Malevolent charm or fear-inducing presence.
            if Dice(4) == 1: WIS += Dice(3)     # Dark knowledge or foresight.

    if rc == "Halfling":
        DEX += Dice(2)
        CHA += Dice(2)
        
        halfling_type = random.choice(["Nomad", "Townsperson", "Stealthy", "Jovial", "Farmer"])

        if halfling_type == "Nomad":
            DEX += Dice(4)                      # Nimbleness from constant movement.
            if Dice(4) == 1: WIS += Dice(3)     # Wisdom from seeing different parts of the world.
        elif halfling_type == "Townsperson":
            CHA += Dice(4)                      # Social skills from interacting with others in a community setting.
            if Dice(4) == 1: INT += Dice(3)     # General knowledge from a settled life.
        elif halfling_type == "Stealthy":
            DEX += Dice(6)                      # Exceptional agility and sneaking skills.
            if Dice(4) == 1: WIS += Dice(3)     # Insight from being observant.
        elif halfling_type == "Jovial":
            CHA += Dice(6)                      # An irresistible charm and charisma.
            if Dice(4) == 1: WIS += Dice(3)     # Wisdom from stories and tales.
        elif halfling_type == "Farmer":
            CON += Dice(4)                      # Physical robustness from working the land.
            if Dice(4) == 1: WIS += Dice(3)     # Rustic wisdom.

    if rc == "Kobold":
        DEX += Dice(2)
        INT += Dice(2)

        kobold_type = random.choice(["Tinkerer", "Miner", "Dragon Worshiper", "Trapper", "Scout"])

        if kobold_type == "Tinkerer":
            INT += Dice(4)                      # Enhanced intelligence from creating devices.
            if Dice(4) == 1: DEX += Dice(3)     # Manual dexterity from handling tools.
        elif kobold_type == "Miner":
            STR += Dice(4)                      # Strength from continuous mining.
            if Dice(4) == 1: CON += Dice(3)     # Endurance from working in harsh conditions.
        elif kobold_type == "Dragon Worshiper":
            CHA += Dice(4)                      # Charisma from spiritual practices and rituals.
            if Dice(4) == 1: WIS += Dice(3)     # Wisdom from understanding dragon lore.
        elif kobold_type == "Trapper":
            DEX += Dice(6)                      # Expertise in setting up and avoiding traps.
            if Dice(4) == 1: INT += Dice(3)     # Intelligence from strategizing trap locations.
        elif kobold_type == "Scout":
            DEX += Dice(6)                      # Agility from scouting territories.
            if Dice(4) == 1: WIS += Dice(3)     # Wisdom from observing and understanding the terrain.

    if rc == "Lizardfolk":
        STR += Dice(2)
        CON += Dice(2)
        CHA += Dice(2)  # Representing their tribal leadership and strong community ties.

        lizardfolk_type = random.choice(["Hunter", "Shaman", "Warrior", "Nature Adept", "Swamp Scout"])

        if lizardfolk_type == "Hunter":
            DEX += Dice(4)                      # Agility and precision from hunting.
            if Dice(4) == 1: WIS += Dice(3)     # Tracking and understanding prey.
        elif lizardfolk_type == "Shaman":
            WIS += Dice(6)                      # Connection to spirits and nature.
            if Dice(4) == 1: CHA += Dice(3)     # Leadership in spiritual ceremonies.
        elif lizardfolk_type == "Warrior":
            STR += Dice(6)                      # Enhanced strength from combat training.
            if Dice(4) == 1: CON += Dice(3)     # Endurance from battle.
        elif lizardfolk_type == "Nature Adept":
            INT += Dice(4)                      # Knowledge of herbs, plants, and natural remedies.
            if Dice(4) == 1: WIS += Dice(3)     # Sensing changes in the environment.
        elif lizardfolk_type == "Swamp Scout":
            DEX += Dice(6)                      # Stealth and quickness from moving silently in swampy terrain.
            if Dice(4) == 1: INT += Dice(3)     # Understanding of swamp ecology and strategy.

    if rc == "Monstrosity":
        STR += Dice(3)
        CON += Dice(3)

        monstrosity_type = random.choice(["Chimeric Beast", "Behemoth", "Nightmare Creature", "Stalker", "Aquatic Horror"])

        if monstrosity_type == "Chimeric Beast":
            DEX += Dice(4)                      # Agility from combined animal traits.
            if Dice(4) == 1: INT += Dice(3)     # Cunning of combined animal instincts.
        elif monstrosity_type == "Behemoth":
            STR += Dice(6)                      # Immense strength.
            if Dice(4) == 1: CON += Dice(4)     # Incredible endurance.
        elif monstrosity_type == "Nightmare Creature":
            CHA += Dice(6)                      # Presence that instills fear.
            if Dice(4) == 1: WIS += Dice(3)     # Keen senses to detect prey.
        elif monstrosity_type == "Stalker":
            DEX += Dice(6)                      # Stealth and precision in hunting.
            if Dice(4) == 1: WIS += Dice(4)     # Tracking and ambushing skills.
        elif monstrosity_type == "Aquatic Horror":
            CON += Dice(6)                      # Surviving in deep or treacherous waters.
            if Dice(4) == 1: STR += Dice(3)     # Overpowering aquatic prey.

    if rc == "Ooze":
        CON += Dice(6)  # Base increase for being amorphous and hard to damage.

        ooze_type = random.choice(["Acidic Ooze", "Engulfing Ooze", "Eldritch Ooze", "Regenerative Ooze", "Camouflaging Ooze"])

        if ooze_type == "Acidic Ooze":
            CON += Dice(4)                      # Resilient due to corrosive nature.
            if Dice(4) == 1: STR += Dice(3)     # Corrosive attacks can be considered stronger.
        elif ooze_type == "Engulfing Ooze":
            STR += Dice(6)                      # Adept at pulling in prey.
            if Dice(4) == 1: DEX += Dice(3)     # Speed and agility to engulf rapidly.
        elif ooze_type == "Eldritch Ooze":
            INT += Dice(4)                      # Mystical understanding or unnatural cognition.
            if Dice(4) == 1: WIS += Dice(4)     # Otherworldly perception.
            if Dice(4) == 1: CHA += Dice(4)     # Strange allure or presence.
        elif ooze_type == "Regenerative Ooze":
            CON += Dice(6)                      # Rapid regeneration boosts resilience.
        elif ooze_type == "Camouflaging Ooze":
            DEX += Dice(4)                      # Ability to quickly adapt to surroundings.
            if Dice(4) == 1: WIS += Dice(3)     # Enhanced senses to detect prey while hidden.

    if rc == "Orc":
        STR += Dice(2)  # Base increase due to the general physical prowess of orcs.
        CON += Dice(2)  # Due to their rugged and tough nature.

        orc_type = random.choice(["Warrior Orc", "Shamanic Orc", "Scout Orc", "Berserker Orc", "Chieftain Orc"])

        if orc_type == "Warrior Orc":
            STR += Dice(4)                      # Extra physical training and combat experience.
            if Dice(4) == 1: CON += Dice(3)     # More resilience from battle scars.
        elif orc_type == "Shamanic Orc":
            WIS += Dice(4)                      # Spiritual understanding and magic channeling.
            if Dice(4) == 1: CHA += Dice(3)     # Spiritual presence and leadership.
        elif orc_type == "Scout Orc":
            DEX += Dice(4)                      # Agility and nimbleness for reconnaissance.
            if Dice(4) == 1: WIS += Dice(3)     # Sharpened senses.
        elif orc_type == "Berserker Orc":
            STR += Dice(6)                      # Raw power from the rage.
            if Dice(4) == 1: CON += Dice(4)     # Ability to endure pain.
        elif orc_type == "Chieftain Orc":
            CHA += Dice(4)                      # Leadership and command.
            if Dice(4) == 1: WIS += Dice(3)     # Tactical insight.
            if Dice(4) == 1: STR += Dice(3)     # Respect gained through strength.

    if rc == "Plant":
        CON += Dice(2)  # Base increase due to the hardiness of plants.

        plant_type = random.choice(["Treant", "Carnivorous Plant", "Healer Herb", "Vine Controller", "Blighted Plant"])

        if plant_type == "Treant":
            STR += Dice(6)                      # Their massive size provides them with great strength.
            WIS += Dice(3)                      # Connection to nature and the forests.
            if Dice(4) == 1: CON += Dice(3)     # Their bark can be exceptionally tough.
        elif plant_type == "Carnivorous Plant":
            DEX += Dice(4)                      # Quick reflexes to capture prey.
            if Dice(4) == 1: STR += Dice(3)     # Strength to hold and consume prey.
        elif plant_type == "Healer Herb":
            WIS += Dice(4)                      # Knowledge of the natural world and its healing properties.
            if Dice(4) == 1: CHA += Dice(3)     # Pleasant and inviting presence.
        elif plant_type == "Vine Controller":
            DEX += Dice(3)                      # Control over nimble vines.
            INT += Dice(3)                      # Strategy in using vines for various tasks.
        elif plant_type == "Blighted Plant":
            CON += Dice(4)                      # Resistance due to its corrupted nature.
            if Dice(4) == 1: CHA += Dice(3)     # Intimidating or eerie presence.


    if rc == "Snakefolk":
        DEX += Dice(2)  # Base increase because of their nimble, snake-like nature.

        snake_type = random.choice(["Constrictor", "Venomous", "Mystic", "Ambusher", "Scaled Protector"])

        if snake_type == "Constrictor":
            STR += Dice(4)                      # Power to constrict and bind.
            CON += Dice(3)                      # To endure while binding their foes.
            if Dice(4) == 1: DEX += Dice(3)     # To quickly wrap around foes.
        elif snake_type == "Venomous":
            CON += Dice(4)                      # To produce and resist their own venom.
            if Dice(4) == 1: CHA += Dice(3)     # Intimidation due to the fear of their venom.
        elif snake_type == "Mystic":
            INT += Dice(4)                      # Proficiency with magic and ancient lore.
            WIS += Dice(4)                      # Connection to mystical energies.
            if Dice(4) == 1: CHA += Dice(3)     # Presence as a leader or a figure of worship.
        elif snake_type == "Ambusher":
            DEX += Dice(4)                      # Mastery of stealth and quick strikes.
            if Dice(4) == 1: STR += Dice(3)     # For quick and powerful strikes.
        elif snake_type == "Scaled Protector":
            CON += Dice(4)                      # Due to their durable scales.
            STR += Dice(3)                      # Strength to hold the line.
            if Dice(4) == 1: WIS += Dice(2)     # Tactical understanding of battles.

    if rc == "Undead":
        # Basic stats increase due to the unnatural nature of undead.
        CON += Dice(2)  # Undying nature.
        CHA += Dice(2)  # Eerie presence.

        undead_type = random.choice(["Skeleton", "Ghost", "Zombie", "Vampire", "Mummy", "Lich", "Ghoul"])

        if undead_type == "Skeleton":
            STR += Dice(3)
            DEX += Dice(3)
        elif undead_type == "Ghost":
            DEX += Dice(4)  # Ethereal nature.
            CHA += Dice(4)  # Haunting presence.
        elif undead_type == "Zombie":
            STR += Dice(3)
            CON += Dice(5)  # Hard to put down.
        elif undead_type == "Vampire":
            DEX += Dice(4)  # Supernatural agility.
            CHA += Dice(5)  # Mesmerizing presence.
            INT += Dice(3)  # Often they are quite intelligent.
        elif undead_type == "Mummy":
            STR += Dice(3)
            CON += Dice(4)  # Preserved nature.
            WIS += Dice(3)  # Ancient knowledge.
        elif undead_type == "Lich":
            INT += Dice(6)  # Mastery over dark arts.
            WIS += Dice(6)  # Arcane knowledge.
            CHA += Dice(4)  # Fearsome presence.
        elif undead_type == "Ghoul":
            STR += Dice(3)
            DEX += Dice(3)
            if Dice(4) == 1: INT += Dice(3)  # Some are quite cunning.
    return [STR,DEX,CON,INT,WIS,CHA]

def NPC():
    """NPC creator"""

    ### Title 
    Ttl = Title()

    ### Background
    bg = Background()

    ### Level
    Lvl = Dice(30)

    #Lvl = 1

    
    rc = Race()
    mn = Monster(rc)
    al = Alignment()

    Name = Racial_Names(rc)

    STR,DEX,CON,INT,WIS,CHA = AbilityScoresGeneration(rc)


    print(f"{Name}, {Ttl}")

    AC = 10 + Modifier(DEX) + Dice( PB(Lvl))
    if Dice(10) == 1 or bg == "Monk":       AC += Modifier(WIS)
    if Dice(10) == 1 or bg == "Berserker":  AC += Modifier(CON)
    if AC>18 + PB(Lvl): AC  = 18 + PB(Lvl)

    HP = Dice( Dice()+ Dice(), Lvl) + Lvl*Modifier(CON)


    r = ""
    r += "- {} - ".format(al) + random.choice(["♀", "♂", "⚥", "⚬", "?", ""])
    r += "\n"
    r += bg
    r += "\n"
    r += f"{rc}: {mn}"
    r += "\n"
    r += "\n"



    r += f"Lvl: {Lvl}⚜︎\t    HP: {HP}♡\t    AC: {AC}⛨️"
    r += ("\n\t" +
          f"STR: {STR}  \t |  {Modifier(STR)} \n\t" +
          f"DEX: {DEX}  \t |  {Modifier(DEX)} \n\t" +
          f"CON: {CON}  \t |  {Modifier(CON)} \n\t" +
          f"INT: {INT}  \t |  {Modifier(INT)} \n\t" +
          f"WIS: {WIS}  \t |  {Modifier(WIS)} \n\t" +
          f"CHA: {CHA}  \t |  {Modifier(CHA)} \n\t")
    r += "\n"

    # Initialize a variable to keep track of the number of proficient saving throws
    proficient_saving_throws = 0

    # While loop to ensure at least one saving throw is proficient
    while proficient_saving_throws < 2:
        # Reset the saving throws
        saving_throws_str = "Saving Throws:" + "\t"
        proficient_saving_throws = 0

        if Dice(4) == 1:
            saving_throws_str += f"Str:+ {Modifier(STR) + PB(Lvl)}" + "\t"
            proficient_saving_throws += 1
            
        if Dice(4) == 1:
            saving_throws_str += f"Dex:+ {Modifier(DEX) + PB(Lvl)}" + "\t"
            proficient_saving_throws += 1
            
        if Dice(4) == 1:
            saving_throws_str += f"Con:+ {Modifier(CON) + PB(Lvl)}" + "\t"
            proficient_saving_throws += 1
            
        if Dice(4) == 1:
            saving_throws_str += f"Int:+ {Modifier(INT) + PB(Lvl)}" + "\t"
            proficient_saving_throws += 1
            
        if Dice(4) == 1:
            saving_throws_str += f"Wis:+ {Modifier(WIS) + PB(Lvl)}" + "\t"
            proficient_saving_throws += 1
            
        if Dice(4) == 1:
            saving_throws_str += f"Cha:+ {Modifier(CHA) + PB(Lvl)}" + "\t"
            proficient_saving_throws += 1

    # Add the saving throws to the r string
    r += saving_throws_str + "\n"


    r += "Skills:"
    if Dice(8) <= Modifier(STR): r += f"\tAthletics:+{Proficiency(STR) + PB(Lvl)}"
    if Dice(8) <= Modifier(DEX): r += f"\tAcrobatics:+{Proficiency(DEX) + PB(Lvl)}"
    if Dice(8) <= Modifier(DEX): r += f"\tSleight of Hand:+{Proficiency(DEX) + PB(Lvl)}"
    if Dice(8) <= Modifier(DEX): r += f"\tStealth:+{Proficiency(DEX) + PB(Lvl)}"
    if Dice(8) <= Modifier(INT): r += f"\tArcana:+{Proficiency(INT) + PB(Lvl)}"
    if Dice(8) <= Modifier(INT): r += f"\tHistory:+{Proficiency(INT) + PB(Lvl)}"
    if Dice(8) <= Modifier(INT): r += f"\tInvestigation:+{Proficiency(INT) + PB(Lvl)}"
    if Dice(8) <= Modifier(INT): r += f"\tNature:+{Proficiency(INT) + PB(Lvl)}"
    if Dice(8) <= Modifier(INT): r += f"\tReligion:+{Proficiency(INT) + PB(Lvl)}"
    if Dice(8) <= Modifier(WIS): r += f"\tAnimal Handling:+{Proficiency(WIS) + PB(Lvl)}"
    if Dice(8) <= Modifier(WIS): r += f"\tInsight:+{Proficiency(WIS) + PB(Lvl)}"
    if Dice(8) <= Modifier(WIS): r += f"\tMedicine:+{Proficiency(WIS) + PB(Lvl)}"
    if Dice(8) <= Modifier(WIS): r += f"\tPerception:+{Proficiency(WIS) + PB(Lvl)}"
    if Dice(8) <= Modifier(WIS): r += f"\tSurvival:+{Proficiency(WIS) + PB(Lvl)}"
    if Dice(8) <= Modifier(CHA): r += f"\tDeception:+{Proficiency(CHA) + PB(Lvl)}"
    if Dice(8) <= Modifier(CHA): r += f"\tIntimidation:+{Proficiency(CHA) + PB(Lvl)}"
    if Dice(8) <= Modifier(CHA): r += f"\tPerformance:+{Proficiency(CHA) + PB(Lvl)}"
    if Dice(8) <= Modifier(CHA): r += f"\tPersuasion:+{Proficiency(CHA) + PB(Lvl)}"
    r += "\n"

    r += "\n"
    r += "Passive Perception: {}".format( 10 + Modifier(WIS) + PB(Lvl))
    r += "\n"
    r += "Proficiency Bonus: +{}".format( PB(Lvl))
    r += "\n"

    r += "\n"
    r += "Languages: \n\t{}".format(Language(rc, bg))
    r += "\n"
    
    r += "⫷   COMBAT ACTIONS:   ⫸"
    r += "\n"
    r += "\tTo hit: +{}".format( Modifier(max(STR, DEX)) + PB(Lvl))
    
    r += "\n- SIMPLE ATTACKS:"
    r += "\n"
    num_weapons = Dice(3)
    for i in range (num_weapons):
        r += Attack(Dice(4), STR = STR, DEX = DEX, PB = PB(Lvl))
        r += "\n"
    
    r += "\n- SPECIAL ATTACK: {} Uses per Combat".format(Dice(PB(Lvl)))
    r += "\n"
    r += SpecialAttack(Lvl, Modifier(random.choice([STR, DEX, CON, INT, WIS, CHA])), STR, DEX)
    r += "\n\n"
    
    r += "༼ SPELLCASTING:\t{} ༽".format(random.choice(["INT", "WIS", "CHA"]))
    r += "\n"
    r += "\t Spellsave DC {}".format(8 + Modifier(max(INT, WIS, CHA))+ PB(Lvl) )
    r += "\n"
    r += "\t To hit: +{}".format( Modifier(max(INT, WIS, CHA) + PB(Lvl)))
    r += "\n"
    r += Magic(Lvl, rc, bg)

    r += "\n"
    r += "\n⚔︎    SKILLS & ACCTIONS:   ⚔︎"
    r += "\n"
    r += Abilities(bg)
    r += "\n"
    r += Abilities(rc)
    r += "\n"

    if Dice(Lvl) >= 15:
        r += "\n✯    LEGENDARY ACTIONS:    ✯"
        r += "\n"
        r += f"The {bg} {rc} can take {Dice(PB(Lvl))} legendary actions, choosing from the options below. \n\t Only one legendary action can be used at a time, and only at the end of another creature's turn. \n\t The {bg} {rc} regains spent legendary actions at the start of its turn."
        r += "\n"
        r += Legendary(bg)
        r += "\n"
        r += Legendary(rc)
        r += "\n"

    if Dice(Lvl) >= 20:
        r += "\n⛫   LAIR ACTIONS:   ⛫"
        r += "\n"
        r += "Unless otherwise noted, any lair action that demands a saving throw uses the spellsave DC above."
        r += "\n On initiative count 20 (losing initiative ties), the creature can take a lair action to cause one of the following effects, but can't use the same effect two rounds in a row:"
        r += "\n"
        r += Lair(bg)
        r += "\n"
        r += Lair(rc)

    if Dice(Lvl) >= 10:
        r += "\n♕   REGIONAL EFFECTS:   ♛"
        r += "\n"
        r += f"The {bg} {rc} has an effect on its domains that may include any of the following magical effects:"
        r += "\n"
        r += Region(bg)
        r += "\n"
        r += Region(rc)
        r += "\n"
        r += f"If the {bg} {rc} dies, these effects dissipate during the next {Dice(6,2)} days."



    print(r)


    
    print("\n꧁  Their Story ꧂\n\n")
    s = ""
    s += "\n"
    s += " - Traits -"
    s += "\n"
    tr1 = Trait()
    tr2 = Trait(bg)
    tr = tr1 + "\n" + tr2 + "\n"
    s += tr
    s += " - Ideal -"
    s += "\n"
    idl = Ideal(bg, al)
    s += idl
    s += "\n"
    s += " - Story Hook -"
    s += "\n"
    ph = PlotHook()
    s += ph


    try: 
        question = "Craft the presentation for a D&D NPC: "
        question += "\n Their real name is " + Name
        question += "\n They are known as " + Ttl
        question += "\n They are a " + mn + ", a kind of " + rc
        question += "\n Their alignment: " + al
        question += "\n They are known for being a " + bg
        question += "\n They are" + tr1 + " They also are " + tr2
        question += "\n They follow the ideal of " + idl
        question += "\n Also, there's a problem whith which they need urgent help, related to the following Plot Hook: " + ph 
        question += "\n Based on their race and background, what would be a plausible story for them? And a problem that leads to a D&D adventure?"
        question += "\n Write it in the style of " + Style()
        question += "\n Write it in first person, as if he was introducing himself, and use three paragraphs of about 100 words each, expanding where appropiate. The first paragraph must contain information of their name and background. The second paragraph must express their ideals and goals. The third paragraph must explain why the player's characters may help or confront the NPC."  
        answer = ask_chatgpt(question)
        print(answer)
        print(s)
    except Exception as e:
        print(s)
        print(f"Encountered an error: {e}")

    
NPC()
