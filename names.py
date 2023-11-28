import random
import npc_class as NPC
import dnd

def Dice(D=6,N=1):
    return dnd.Dice(D,N)

def is_valid_name(name):
    if len(name) < 3 or len(name) > 12:
        return False
    # Every substring of four letters should have at least one vocal
    vowels = "aeiou"
    for i in range(len(name) - 3):
        chunk = name[i:i+3].lower()
        if not any(vowel in chunk for vowel in vowels):
            return False

    return True

def NewName(Names,onset=[""],nuclei=[""],codas=[""]):     
        namer = MarkovNameGenerator(Names)
        Name = namer.generate_name()
            
        if is_valid_name(Name):
            return Name
        
        # If not valid, try generating a name using SyllabicGenerator
        Name = SyllabicGenerator(
                onset = onset,
                nuclei=nuclei,
                codas=codas
                ).name

        if is_valid_name(Name):
            return Name

        Name = SyllabicName(
                syllables = SyllabicExtraction(Names),
                min_syllables=1,
                max_syllables=size)

        if is_valid_name(Name):
            return Name

        Name =  random.choice(Names)
        return Name
    
class SyllabicGenerator:
    def __init__(self, onset, nuclei, codas, count = 1):
        self.onset = onset
        self.nuclei = nuclei
        self.codas = codas
        self.name = self.generate_name()
        return self.name

    def generate_syllable(self):
        return random.choice(self.onset) + random.choice(self.nuclei) + random.choice(self.codas)

    def generate_name(self, max_attempts=100):
        for _ in range(max_attempts):
            name = self.generate_syllable()
            if is_valid_name(name):
                return name.capitalize()
        return "Lorem Ipsum"


''' Legacy
def SyllabicGenerator(onset,nuclei,codas, count):
    name = ''
    # Randomly decide how many syllables the name will have
    name += random.choice(onset)
    # Generate each syllable
    for _ in range(count-2):
        nucleus = random.choice(nuclei) if random.random() > 0.3 else ''
        name += nucleus
    name += random.choice(codas)
    # Format name with first letter uppercase and rest lowercase
    return name.capitalize()
'''

def SyllabicExtraction(names):
    syllables = set()
    for name in names:
        length = len(name)
        for i in range(1, length):
            syllables.add(name[:i].lower())
            syllables.add(name[i:].lower())
    return list(syllables)

def SyllabicName(syllables, min_syllables=2, max_syllables=8):
    name = ''.join(random.choice(syllables) for _ in range(random.randint(min_syllables, max_syllables)))
    return name.capitalize()


from collections import defaultdict

class MarkovNameGenerator:
    def __init__(self, names, order=2):
        self.order = order
        self.markov_chain = defaultdict(list)
        self.populate_markov_chain(names)

    def populate_markov_chain(self, names):
        for name in names:
            padded_name = name.lower() + ' '  # Add a padding character to signify the end of a name
            for i in range(len(padded_name) - self.order):
                state = padded_name[i:i + self.order]
                next_state = padded_name[i + self.order]
                self.markov_chain[state].append(next_state)

    def generate_name(self, min_length=5, max_length=10):
        name = ''
        state = random.choice(list(self.markov_chain.keys()))
        while len(name) < max_length:
            name += state[0]
            next_states = self.markov_chain.get(state, [' '])
            if ' ' in next_states and len(name) >= min_length:
                break
            state = state[1:] + random.choice(next_states)
        return name.title().strip()



descriptor =[]
rank = []
of_the = []

#Color
color_descriptor = [
                    "Amber","Golden", "Goldenrod","Ochre",
                    "Lime",
                    "Jade","Olive",
                    "Azure", "Blue", "Cerulian","Indigo",
                    "Lavender",
                    "Beige","Ivory","Graphite",
                    "Iridescent",]



descriptor += color_descriptor


# Material
material_descriptor =   ["Gold","Golden",]
material_descriptor +=  ["Graphite","Onyx"]
material_descriptor +=  ["Ivory",]
material_descriptor +=  ["Gemmed","Jewel","Jewelcraft","Jeweled","Opal","Jade","Crystal","Amethyst", "Quartz", "Topaz","Xenolith","Elfstone"]
descriptor += material_descriptor

of_the_material = ["of the Jewels","of the Ruby",]
of_the_material+= ["of Gold","of Silver","of Iron","of Steel",]
of_the += of_the_material


# Plants
plant_descriptor = ["Lavender"]
descriptor += plant_descriptor


# Faith
faith_descriptor = ["Holy", "Celestial""Angelic",]
faith_descriptor+= ["Omniscient"]
faith_descriptor+= ["Horus's"]
descriptor += faith_descriptor

faith_rank  = ["Oracle","Saint",]
faith_rank += ["God", "Deity"]
rank += faith_rank



# Hellish
hell_descriptor = ["Orphean","Abyssal", "Daemonian", "Infernal", "Hellish"]
descriptor += hell_descriptor

of_the_hell = ["of the Dark Abyss","of The Seventh Hell","of Hell","of the Hells",]
of_the += of_the_hell





# Power
power_descriptor = ["Grand"]
descriptor +=  power_descriptor

# Feelings
feelings_descriptor =[ "Affectionate", "Loving"]
feelings_descriptor+= ["Hopeful", "Joyful", "Jubilant", "Jovial",]
feelings_descriptor+= ["Aggressive","Angry","Annoyed","Apathetic","Irate", "Jealous", "Hostile"]
feelings_descriptor+= ["Anxious", "Horrified", "Nervous", "Terrified"]
descriptor += feelings_descriptor

# Martials
martial_descriptor = ["Guardian's","Guardian of",]
martial_descriptor+= ["Battle","Battle's","Battleground","War","Warlord's","Warrior's",]
descriptor += martial_descriptor

martial_rank = ["Guard","Guardian","Keeper","Sentinel","Vigilant","Knightly",]
martial_rank += ["Commander","Warlord",]
martial_rank += ["Gladiator","Warrior","War",]
rank += martial_rank


#Flaw & Virtue
flaw_descriptor = ["Alcoholic","Blind","Mad",]
virtue_descriptor = ["Gallant","Generous","Kind","Unbreakable","Valiant",]
descriptor +=  flaw_descriptor + virtue_descriptor


# Locations, lands, empires, countries
location_descriptor = [
        "Aegean","Amazon's","Amazonian","Archipelago's","Asgardian","Atlantean","Aztec",
        "Badland","Babylonian","Bay","Beach","Beachy","Glacial", "Glade's", "Gorgonian",
        "Grassland's", "Gulf's", "Garden's", "Geyser's", "Harbor's", "Hill's",  
        "Island", "Islet", "Marsh", "Marshy", "Meadow", "Mine", "Moor", "Morass", "Moss", "Mountain",
        "Mountainous", "Muddy", "Museum", "Oasis", "Ocean", "Oceanic", "Orchard", "Outpost", "Outlandish", "Overgrown"
        "Glade", "Gorge", "Grassland", "Graveyard", "Grove"]

descriptor += location_descriptor


empty = ["Hollow","Empty"]
descriptor += empty

# Magic, wizzardry, and Arcane
arcane_descriptor = [
        "Arcane","Alchemical","Apothecary","Arcanic",
        "Mage","Mage's",
        "Wand","Wizard's",
        "Arcane", "Alchemical", "Apothecary", "Arcanic", "Mage", "Mage's", "Magic",
        "Wand", "Wizard's", "Myrmidonic", "Mystic", "Mystical", "Mythical"
        ]

descriptor += arcane_descriptor
# Creatures 
creature_descriptor = [
    "Kraken's", "Krakenesque"]
descriptor += creature_descriptor

creature_rank = ["Kraken", "Leviathan", ]
rank += creature_rank

of_the_creature = [
        "of Baba Yaga",
        "of the Kraken",
        "of the Hydra",
        ]
of_the += of_the_creature

# Nature, animals
air_descriptor = ["Atmospheric", "Tempest", "Wind", "Windy"]
seasonal_descriptor = ["Autumn", "Climatic", "Winter"]
cold_descriptor = ["Glacial", "Polar", "Icy", "Ice", "Icicle", "Frostbite", "Frostfire","Glacier",]

wolf_descriptor = ["Alpha", "Wolf's"]
insect_descriptor = ["Hive",]
fish_descriptor = ["Gilled"]
bird_descriptor = ["Condor's"]

nature_descriptor = ["Grassy"]

animal_descriptor = insect_descriptor + fish_descriptor + wolf_descriptor + bird_descriptor

descriptor += animal_descriptor

of_the_nature = ["of the Waterfall"]

# Objects
object_descriptor = [
"Amulet", "Dagger", "Sword", "Talisman", "Goblet", "Grail"]
of_the_object = ["of The Amulet", "of The Sword", "of The Talisman", "of The Goblet"]

# Old, Ancient, Epochal, Timely
elder_descriptor = [
"Ageless", "Anachronistic", "Ancestral", "Ancient", "Atemporal", "Elder", "Old", "Sempiternal"
"Age-old", "Ancestral", "Ancient", "Antediluvian", "Antique", "Archaic", "Elder", "Eldritch",
"Eternal", "Everlasting", "Historic", "Hoary", "Immemorial", "Long-lived", "Old", "Perennial",
"Perpetual", "Primordial", "Time-honored", "Timeless", "Traditional", "Venerable", "Vintage"]

epochal_descriptor = ["Baroque", "Gothic"]


# Political, noble, and power figures
noble_rank = [
"Baron", "Baron of", "Governor", "Lord", "Monarch", "Overlord", "Sovereign",
"Emperor", "Master", "Ruler", "King", "King's", "King of", "Kingly", "Kingdom's",
"Queen", "Queen of", "Queen's"]


# Secrecy, Mischief and Mistery
secret_descriptor =["Hidden"]
mischief_descriptor = [ "Gambler","Mischievous", "Silver-tongued",]

# Space and Scifi
space_descriptor = [
"Alien", "Astral", "Black Hole", "Cometary", "Cosmic", "Cosmos", "Dimensional",
"Eclipse", "Ethereal", "Existence", "Galactic", "Galactian", "Infinity", "Moon", "Moonlit", "Ozone",
"Reality", "Star", "Starry", "Sun", "Sunny", "Sunset", "Supernova", "Time", "Timebender",
"Void", "Voided", "Warp", "Wormhole", "Zodiac", "Zodiacal"
]
of_the_space = ["of the Galaxy"]

cosmic_descriptor = ["Gravitational"]

# Horror
horror_descriptor = ["Werevolve's"]

# Guilds and Organizations
guild_organizational_descriptor = ["Guild's"]
# Flora and Natural Beauty
flora_natural_beauty = ["Garden"]
# Gases and Gaseous States
gaseous_descriptor = ["Gas", "Gaseous"]
# Legal and Judicial Objects
legal_judicial_objects = ["Gavel"]
# Artistic and Cultural
artistic_cultural_descriptor = ["Harlequin", "Harpist", "Haunting"]
# Cosmic and Stellar Phenomena
cosmic_stellar_descriptor = ["Helian"]
# Geographical Elevations
geographical_elevations = ["High"]
# Mythical and Legendary
mythical_legendary_descriptor = ["Horned", "Homeric", "Icarian", "Immortal", "Impenetrable", "Invincible", "Jotunn", "Kraken's", "Krakenesque"]
# Hunting and Wilderness
hunting_wilderness_descriptor = ["Hunting", "Hunter's"]
# Ghosts and Spirits
ghost_spirit_descriptor = ["Ghost"]
# Giants and Large Entities
giant_large_entity_descriptor = ["Giant"]
# Art and Creativity
art_creativity_descriptor = ["Ink", "Inkwell", "Inkwork"]
# Intellectual and Thoughtful
intellectual_thoughtful_descriptor = ["Intellect", "Inquisitive", "Intrepid"]
# Labs and Research Facilities
lab_research_facilities = ["Lab", "Laboratory"]
# Labyrinths and Complex Structures
labyrinth_complex_structures = ["Labyrinth", "Labyrinth's", "Labyrinthine"]
# Objects of Significance
significant_objects = ["Amulet", "Grail", "Keep", "Last"]
# Luminous and Radiant
luminous_radiant_descriptor = ["Luminous", "Radiant", "Shining", "Sparkling", "Glowing"]
# Liquid and Fluid
liquid_fluid_descriptor = ["Liquid", "Fluid", "Flowing", "Rippling", "Wet"]
# Time-related
time_related_descriptor = ["Hourly", "Instantaneous", "Interim", "Momentary", "Temporal", "Timeless"]
# Emotional States
emotional_states_descriptor = ["Heartbroken", "Lonely", "Melancholic", "Mirthful", "Mischievous", "Nervous", "Pensive", "Perplexed", "Petrified", "Phlegmatic", "Piqued", "Pleased", "Plucky", "Poignant", "Proud", "Puzzled", "Quiet"]
# Performers and Artists
performers_artists_descriptor = ["Actor", "Artist", "Bard", "Composer", "Dancer", "Harpist", "Jester", "Juggler", "Lyrist", "Minstrel", "Musician", "Painter", "Performer", "Poet", "Sculptor", "Singer", "Storyteller", "Troubadour"]
# Luminous and Radiant
luminous_radiant_descriptor = ["Luminous", "Radiant", "Shining", "Sparkling", "Glowing"]
# Liquid and Fluid
liquid_fluid_descriptor = ["Liquid", "Fluid", "Flowing", "Rippling", "Wet"]
# Time-related
time_related_descriptor = ["Hourly", "Instantaneous", "Interim", "Momentary", "Temporal", "Timeless"]
# Emotional States
emotional_states_descriptor = ["Heartbroken", "Lonely", "Melancholic", "Mirthful", "Mischievous", "Nervous", "Pensive", "Perplexed", "Petrified", "Phlegmatic", "Piqued", "Pleased", "Plucky", "Poignant", "Proud", "Puzzled", "Quiet"]
# Performers and Artists
performers_artists_descriptor = ["Actor", "Artist", "Bard", "Composer", "Dancer", "Harpist", "Jester", "Juggler", "Lyrist", "Minstrel", "Musician", "Painter", "Performer", "Poet", "Sculptor", "Singer", "Storyteller", "Troubadour"]
weather_atmospheric_descriptor = ["Blizzard", "Bloodmoon", "Boreal", "Dawnbringer"]
# Mystical and Occult
mystical_occult_descriptor = ["Cipher", "Clairvoyant", "Cloak", "Cobweb", "Cthulhu", "Deity", "Dimension", "Dissonance", "Dragonfire"]
# Celestial and Astronomical
celestial_astronomical_descriptor = ["Celestia", "Chrono", "Constellation", "Cosmos", "Crimson", "Darkstar"]
# Marine and Aquatic
marine_aquatic_descriptor = ["Coral", "Oceanic"]
# Crystals and Minerals
crystals_minerals_descriptor = ["Crystal", "Amethyst", "Quartz", "Topaz", "Xenolith"]
# Weather and Atmospheric Phenomena
weather_atmospheric_descriptor = ["Blizzard", "Bloodmoon", "Boreal", "Dusk", "Eclipse", "Horizon", "Hyperion", "Iceborn"]
# Mystical and Occult
mystical_occult_descriptor = ["Cipher", "Clairvoyant", "Cloak", "Cobweb", "Cthulhu", "Deity", "Dimension", "Dissonance", "Dragonfire", "Dreamweaver", "Elemental", "Elfstone", "Ember", "Ethereal", "Fable", "Fae", "Falcon", "Fenrir", "Feral", "Firebrand", "Flametongue", "Fulcrum", "Galaxy", "Gargoyle", "Gauntlet", "Ghoul", "Glitch", "Glyph", "Golem", "Grimoire", "Gryphon", "Guardianship", "Harbinger", "Hex", "Horizon", "Hydra", "Hyperion", "Iceborn", "Illusion", "Immortal", "Impulse", "Incantation", "Inferno", "Invoker", "Ion", "Iridescent", "Jester", "Juggernaut", "Kaleidoscope", "Kraken", "Leviathan", "Libra", "Lightbringer"]
# Celestial and Astronomical
celestial_astronomical_descriptor = ["Celestia", "Chrono", "Constellation", "Cosmos", "Crimson", "Darkstar", "Dimension", "Eclipse", "Galaxy", "Horizon", "Hyperion", "Star", "Stellar", "Zodiac"]
# Marine and Aquatic
marine_aquatic_descriptor = ["Coral", "Oceanic"]




def Title(npc):
    creature_type = npc.race + ' ' + npc.subrace + ' ' + npc.background

    #return f"The {random.choice(descriptor)} {random.choice(rank)} {random.choice(of_the)}"

    descriptor = []
    rank = []
    of_the = []


    # Adding to existing lists
    color_descriptor = ["Golden", "Goldenrod", "Green"]
    jewel_descriptor = ["Grail"]
    metal_descriptor = ["Granite", "Graphite"]
    loving_descriptor = ["Grateful"]
    hate_descriptor = ["Gloomy", "Grieving"]
    feelings_descriptor = ["Gleaming", "Glowing", "Great"]
    of_the_monster = ["of the Griffon"]
    location_descriptor = ["Gulf", "Garden", "Geyser", "Hamlet", "Harbor", "Heath", "Hedgerow", "Hill", "Hive"]
    loving_descriptor = ["Happy"]
    hate_descriptor = ["Heartbroken"]
    feelings_descriptor = ["Gentle", "Harmonious", "Heart"]
    secret_descriptor = ["Hermetic"]
    hell_descriptor = ["Hell"]
    guardian_rank = ["Heroic"]
    elder_descriptor = ["Historic"]
    space_descriptor = ["Heliospheric"]
    of_the_hell = ["Hesperidean"]
    location_descriptor = ["Hollow", "Island", "Islet", "Jungle", "Lake", "Lagoon"]
    loving_descriptor = ["Hopeful", "Jovial", "Joyful", "Jubilant"]
    hate_descriptor = ["Hostile", "Horrified", "Hungry", "Jealous", "Irate", "Irritated", "Jittery"]
    feelings_descriptor = ["Indifferent", "Inspired", "Interested", "Intrigued"]
    hell_descriptor = ["Infernal"]
    guardian_rank = ["Hunter", "Hunter's"]
    elder_descriptor = ["Homeric", "Jacobean"]
    space_descriptor = ["Ionized"]
    of_the_jewel = ["Jade"]
    metal_descriptor = ["Iron"]
    object_descriptor = ["Hourglass", "Key", "Lantern"]
    noble_rank = ["Imperial", "Knightly", "Lady"]
    secret_descriptor = ["Inscrutable", "Insidious"]
    arcane_descriptor = ["Illusionist"]
    hell_descriptor = ["Infernal"]
    cosmic_stellar_descriptor = ["Interim"]
    faith_church_heaven_religious = ["Holy"]
    color_descriptor = ["Ivory", "Iridescent", "Lavender"]
    # Adding to existing lists
    location_descriptor = ["Loom", "Marketplace", "Mausoleum", "Maze", "Meadow",
                            "Metropolis", "Mine", "Moor", "Morass", "Mountain", "Mountainous",
                            "Museum", "Oasis", "Observatory", "Ocean", "Oceanic", "Orchard", "Outpost",
                            "Palace", "Palm", "Park", "Pond", "Port", "Prairie", "Prison", "Pyramid", "River"]
    nature_descriptor = ["Leafy", "Lush", "Mangrove", "Moss", "Muddy", "Pebble", "Petal", "Plum", "Pumpkin", "Purple"]
    feelings_descriptor = ["Loyal", "Melancholic", "Merry", "Mindful", "Motivated", "Mournful", "Nervous",
                            "Optimistic", "Outraged", "Panicked", "Passionate", "Pensive", "Perceptive", "Pleased",
                            "Poetic", "Proud", "Quiet"]
    space_descriptor = ["Lunar", "Magnetic", "Magnetospheric",
                         "Meteor", "Meteoric", "Meteoritic", "Moon", "Moonlit", "Nebulous",
                         "Nautical", "Nemesis", "Neon", "Nether", "Night", "Nocturnal", "Nova",
                         "Orbital", "Pulsar"]
    metal_descriptor = ["Mahogany", "Magma", "Marble", "Mustard", "Myrmidonic", "Obsidian",
                         "Orb", "Platinum", "Pyro", "Quartz", "Quicksilver"]
    arcane_descriptor = ["Magic", "Mystic", "Mystical", "Mythical", "Oracle", "Oracular", "Orphean",
                          "Pegasus", "Phantasmal", "Phantom", "Pharaoh's", "Phoenix", "Phoenixian", "Phylactery",
                          "Pirate's", "Plasma", "Promethean", "Prophetic", "Protector", "Pyramid"]
    hell_descriptor = ["Malignant", "Malevolent"]
    of_the_monster = ["Lich", "Minotaur", "Minotaurine", "Manticorian"]
    object_descriptor = ["Lyre", "Medallion", "Mirror", "Phylactery"]
    cosmic_stellar_descriptor = ["Luminous", "Magnetic", "Magnetospheric", "Meteor", "Meteoric", "Meteoritic",
                                  "Mighty", "Miraculous", "Mistral"]
    color_descriptor = ["Maroon", "Mauve", "Mulberry", "Mustard", "Olive", "Peach", "Pearl", "Plum", "Purple",
                         "Radiant", "Rainbow", "Rosaline", "Rosy", "Ruby", "Sapphire"]
    faith_church_heaven_religious = ["Holy", "Oracle", "Omniscient", "Oracular", "Promethean", "Prophetic", "Protector",
                                      "Sage", "Sacred"]
    elder_descriptor = ["Historic", "Homeric", "Jacobean", "Mesopotamian", "Millennial", "Myrmidonic", "Nordic", "Odin's",
                         "Olympian", "Orphean", "Romanesque"]
    loving_descriptor = ["Hopeful", "Loving", "Merry", "Optimistic", "Passionate", "Proud"]
    hate_descriptor = ["Hostile", "Horrified", "Hungry", "Irate", "Irritated", "Jealous", "Jittery",
                        "Outraged", "Panicked", "Ruthless"]
    secret_descriptor = ["Hermetic", "Inscrutable", "Insidious", "Intriguing", "Intrigued", "Mysterious"]
    guardian_rank = ["Guardian", "Paladin", "Protector", "Ranger"]
    noble_rank = ["Emperor", "Governor", "King", "King's", "King of", "Kingly", "Kingdom's", "Lord", "Lordly",
                   "Lord Of the", "Lord Of", "Master", "Monarch", "Noble", "Overlord", "Queen", "Queen of", "Queen's",
                   "Regal", "Ruler", "Sovereign"]
    legal_judicial_objects = ["Gavel"]
    art_creativity_descriptor = ["Harlequin", "Harpist", "Haunting", "Poetic"]
    intellectual_thoughtful_descriptor = ["Intellect", "Inquisitive", "Intrepid", "Mindful", "Perceptive"]
    gaseous_descriptor = ["Gas", "Gaseous"]
    flora_natural_beauty = ["Garden", "Leafy", "Lush", "Mangrove", "Moss", "Muddy", "Orchid", "Palm",
                             "Pearl", "Petal", "Plum", "Pumpkin", "Purple", "Redwood", "Ribbon", "Rose",
                             "Rosy", "Ruby", "Sapphire", "Tulip"]
    wilderness_descriptor = ["Jungle", "Mangrove", "Marsh", "Marshy", "Meadow", "Moor", "Morass", "Mountain", "Mountainous", "Muddy", "Palm", "Prairie", "Savannah", "Tundra", "Wilderness"]
    mythical_legendary_descriptor = ["Legendary", "Lich", "Lion-hearted", "Lupine", "Majestic", "Manticorian", "Mighty", "Minotaur", "Minotaurine", "Miraculous", "Monstrous", "Mythical", "Nemean", "Nordic", "Odin's", "Olympian", "Orphean", "Pegasus", "Phantom", "Phoenix", "Phoenixian", "Pirate's", "Promethean", "Protector"]
    hunting_wilderness_descriptor = ["Hunter", "Hunter's", "Hunting", "Ranger"]
    ghost_spirit_descriptor = ["Ghost", "Phantasmal", "Phantom", "Spirit", "Wraith"]
    giant_large_entity_descriptor = ["Giant", "Goliath", "Mammoth", "Titan"]

    color_descriptor = ["Scarlet", "Silver", "Tangerine", "Topaz", "Turquoise", "Violet", "Viridian", "White"]
    nature_descriptor = ["Scenic", "Secluded", "Snowy", "Sultry", "Summer", "Swamp", "Sylvan", "Tropical", "Tundra", "Verdant", "Vibrant", "Wild"]
    feelings_descriptor = ["Serene", "Sleepy", "Sly", "Soulful", "Splendid", "Stunning", "Sublime", "Tranquil", "Uplifting", "Vibrant", "Whimsical", "Wondrous", "Youthful"]
    space_descriptor = ["Stellar", "Universal", "Galactic", "Celestial", "Cosmic"]
    metal_descriptor = ["Sulfuric", "Silver"]
    arcane_descriptor = ["Sorcerer's", "Spectral", "Spellbound", "Spirit", "Shamanic", "Shadowy", "Spellbound"]
    hell_descriptor = ["Sinister", "Tartarean", "Sulfuric", "Ardent"]
    object_descriptor = ["Spire", "Statue", "Stone", "Sword", "Thorn"]
    cosmic_stellar_descriptor = ["Sky", "Star", "Stellar", "Sublime", "Supernatural", "Supreme",
                                  "Temporal", "Timeless", "Titan", "Transcendent", "Twilight", "Ubiquitous", "Ultimate", "Uncharted", "Unearthly", "Unfathomable", "Unforgiving", "Universal", "Unseen", "Untamed"]
    faith_church_heaven_religious = ["Celestial", "Cherubic", "Divine", "Elysian", "Ethereal", "Heavenly", "Holy", "Mythical", "Sacred", "Seraphic", "Spectral", "Spiritual", "Sublime", "Supernatural", "Supreme", "Temple", "Unseen", "Valkyrie's", "Venerable"]
    elder_descriptor = ["Ancient", "Antique", "Archaic", "Elder", "Historic", "Legendary", "Mythic", "Old", "Timeless", "Venerable", "Vintage"]
    loving_descriptor = ["Affectionate", "Alluring", "Ardent", "Charming", "Delightful", "Dreamy", "Enchanting", "Loving", "Romantic", "Sensual", "Sentimental", "Sultry"]
    hate_descriptor = ["Baleful", "Belligerent", "Bitter", "Brutal", "Cruel", "Ferocious", "Fierce", "Fiery", "Furious", "Grim", "Harsh", "Hostile", "Malevolent", "Malign", "Menacing", "Merciless", "Ruthless", "Savage", "Sinister", "Stern", "Stormy", "Tartarean", "Terrifying", "Threatening", "Treacherous", "Turbulent", "Violent", "Villainous", "Vindictive", "Wicked", "Wrathful"]
    secret_descriptor = ["Arcane", "Cryptic", "Enigmatic", "Esoteric", "Hidden", "Inscrutable", "Mysterious", "Mystical", "Occult", "Secret", "Shadowy", "Subtle", "Surreptitious", "Unseen", "Veiled"]
    guardian_rank = ["Defender", "Guardian", "Keeper", "Protector", "Sentinel", "Vigilant", "Watchman", "Warden"]
    noble_rank = ["Aristocratic", "Baronial", "Dignified", "Eminent", "Exalted", "Grand", "Honorable", "Imperial", "Kingly", "Lordly", "Majestic", "Noble", "Regal", "Royal", "Sovereign"]
    legal_judicial_objects = ["Charter", "Code", "Decree", "Edict", "Law", "Legislation", "Mandate", "Ordinance", "Precept", "Regulation", "Rule", "Statute"]
    art_creativity_descriptor = ["Artistic", "Creative", "Cultural", "Elegant", "Expressive",
                                  "Imaginative", "Innovative", "Inspiring", "Intellectual", "Literary", "Poetic",]

    color_descriptor = ["Gilded", "Golden-hearted", "Jade-eyed", "Opalescent", "Platinum"]
    nature_descriptor = ["Frost-bound", "Lone", "Moonlit", "Mystical", "Nebula-born", "Oceanic", "Polar", "Solar", "Star-born", "Star-crossed", "Stellar", "Tempest", "Thunderous", "Twilight"]
    feelings_descriptor = ["Fervent", "Fiery-eyed", "Flame-hearted", "Furious", "Harmonious", "Icy-hearted", "Imperious", "Impish", "Intense", "Jovial", "Mirthful", "Passionate", "Sanguine", "Sinister", "Sly", "Soulbound", "Sovereign", "Spellbinder", "Sphinx-like", "Spiritual", "Stealthy", "Sublime", "Supreme", "Swashbuckler", "Swift", "Swordmaster", "Timeless", "Unassailable", "Unbound", "Unconquerable", "Undaunted", "Unearthly", "Unfathomable", "Unflinching"]
    space_descriptor = ["Interstellar", "Quasar", "Stargazer", "Stellar", "Time-bender", "Titanic"]
    arcane_descriptor = ["Enchanting", "Mystical", "Oracle", "Orbiting", "Otherworldly", "Outlandish", "Pathfinder", "Phantasmal", "Profound", "Prophetic", "Prowler", "Purist", "Pyrotechnic", "Rune-carved", "Runewielder", "Sage", "Savage", "Scintillating", "Scorcher", "Seafarer", "Seer", "Sempiternal", "Shaman", "Shapeshifter", "Silent", "Sinister", "Sky-born", "Sly", "Solar", "Sorcerer", "Sovereign", "Spectral", "Spellbinder", "Sphinx-like", "Spiritual", "Star-born", "Star-crossed", "Stargazer", "Stealthy", "Stellar", "Stormbringer", "Strategist", "Sublime", "Sun-born", "Superb", "Supreme", "Swashbuckler", "Swift", "Swordmaster", "Tempest", "Thaumaturge", "Thunderous", "Time-bender", "Timeless", "Titanic", "Torchbearer", "Trailblazer", "Transcendent", "Tribal", "Trickster", "Twilight", "Tyrant", "Ubiquitous", "Unassailable", "Unbound", "Unconquerable", "Undaunted", "Unearthly", "Unfathomable", "Unflinching"]
    hell_descriptor += ["Ferocious", "Fiery", "Fierce", "Flaming", "Forceful", "Foreboding", "Furious", "Gargantuan", "Ghostly", "Grim", "Inferno", "Maleficent", "Martial", "Meteoric", "Mighty", "Monolithic", "Monstrous", "Mysterious", "Nefarious", "Nimble", "Nocturnal", "Nomadic", "Notorious", "Ominous", "Outrageous", "Pandemonium", "Paradoxical", "Passionate", "Perilous", "Phantasmal", "Pillar", "Pioneering", "Pirate", "Polar", "Powerhouse", "Praetorian", "Precocious", "Predatory", "Preternatural",
                         "Prime", "Prismatic", "Profound", "Prophetic", "Prowler", "Pulsating", "Purist", "Pyrotechnic", "Quasar", "Questing", "Quick-witted", "Quiet", "Radiant", "Raging", "Rainmaker", "Rampant", "Ranger", "Ravaging", "Rebel", "Reckoning", "Redoubtable", "Refined", "Regal", "Relentless", "Renegade", "Resolute", "Resounding", "Revered", "Rhapsodic", "Rogue", "Rune-carved", "Runewielder", "Sage", "Sanguine", "Savage", "Scintillating", "Scorcher", "Seafarer", "Seer", "Sempiternal", "Shadow", "Shaman", "Shapeshifter", "Silent",  "Sinister", "Sky-born", "Sly", "Solar", "Sorcerer", "Soulbound", "Sovereign", "Spectral", "Spellbinder", "Sphinx-like", "Spiritual", "Star-born", "Star-crossed", "Stargazer", "Stealthy", "Stellar", "Stormbringer", "Strategist", "Sublime", "Sun-born", "Superb", "Supreme", "Swashbuckler", "Swift", "Swordmaster", "Tempest", "Thaumaturge", "Thunderous", "Time-bender", "Timeless", "Titanic", "Torchbearer", "Trailblazer", "Transcendent", "Tribal", "Trickster", "Twilight", "Tyrant", "Ubiquitous", "Unassailable", "Unbound", "Unconquerable", "Undaunted", "Unearthly", "Unfathomable", "Unflinching"]
    object_descriptor += ["Amulet", "Artifact", "Banner", "Chalice", "Crest", "Crown", "Emblem", "Ensign", "Flag", "Goblet", "Grail", "Icon", "Idol", "Jewel", "Key", "Lantern", "Medallion", "Orb", "Pendant", "Relic", "Rod", "Scepter", "Seal", "Sigil", "Standard", "Statue", "Stone", "Sword", "Talisman", "Token", "Totem", "Vase"]
    cosmic_stellar_descriptor += ["Astral", "Celestial", "Cosmic", "Ethereal", "Galactic", "Interstellar", "Lunar", "Martian", "Mercurial", "Meteor", "Nebular", "Orbital", "Planetary", "Solar", "Space", "Starry", "Sublime", "Supernatural", "Universal"]
    faith_church_heaven_religious += ["Angel", "Apostle", "Archangel", "Bishop", "Cardinal", "Chaplain", "Cleric", "Deacon", "Devout", "Disciple", "Divine", "Evangelist", "Faithful", "Friar", "Holy", "Imam", "Minister", "Missionary", "Monk", "Nun", "Pastor", "Patriarch", "Pilgrim", "Preacher", "Priest", "Prophet", "Rabbi", "Reverend", "Saint", "Savior", "Seer", "Shaman", "Shepherd", "Spiritual", "Theologian", "Vicar", "Zealot"]
    elder_descriptor += ["Ageless", "Ancestral", "Ancient", "Antediluvian", "Antique", "Aristocratic", "Baronial", "Bygone", "Classical", "Elder", "Eternal", "Everlasting", "Historic", "Hoary", "Immortal", "Imperishable", "Infinite", "Long-standing", "Old", "Perennial", "Perpetual", "Primeval", "Primordial", "Time-honored", "Timeless", "Traditional", "Venerable", "Veteran", "Vintage"]
    loving_descriptor += ["Adoring", "Affectionate", "Amorous", "Ardent", "Caring", "Cherishing", "Compassionate", "Devoted", "Enamored", "Fond", "Gentle", "Heartfelt", "Loving", "Passionate", "Romantic", "Sentimental", "Sweet", "Tender", "Warm", "Yearning"]
    hate_descriptor += ["Abhorrent", "Acrimonious", "Angry", "Annoyed", "Antagonistic", "Apathetic", "Belligerent", "Bitter", "Contemptuous", "Cruel", "Cynical", "Detestable", "Disdainful", "Disgusted", "Enraged", "Fierce", "Furious", "Hateful", "Hostile", "Indignant", "Inimical", "Irate", "Irritable", "Jealous", "Loathsome", "Malevolent", "Malicious", "Nasty", "Odious", "Offensive", "Opposed", "Outraged", "Peeved", "Pernicious", "Piqued", "Rancorous", "Resentful", "Spiteful", "Sullen", "Vengeful", "Vindictive", "Virulent"]
    color_descriptor += ["Gilded", "Golden-hearted", "Jade-eyed", "Opalescent", "Platinum"]
    nature_descriptor += ["Flourishing", "Frost-bound", "Meadowborn", "Moonlit", "Nebula-born", "Oceanic", "Polar", "Solar", "Sun-born"]
    feelings_descriptor += ["Fervent", "Fiery-eyed", "Flame-hearted", "Furious", "Gallant", "Glorious", "Graceful", "Greathearted", "Harmonious", "Heartfelt", "Heroic", "Hypnotic", "Illustrious", "Imaginative", "Impassioned", "Intense", "Jovial", "Joyous", "Judicious", "Keen", "Lauded", "Majestic", "Maleficent", "Martial", "Masterful", "Maverick", "Melodic", "Meteoric", "Mighty", "Miraculous", "Mirthful", "Monolithic", "Mysterious", "Mystical", "Mythical", "Nefarious", "Nimble", "Noble", "Nocturnal", "Nomadic", "Notorious", "Ominous", "Ornate", "Otherworldly", "Outlandish", "Outrageous", "Passionate", "Pathfinder", "Peerless", "Perilous", "Phantasmal", "Pillar", "Pioneering", "Predatory", "Preternatural", "Prime",
                            "Prismatic", "Profound", "Prophetic", "Prowler", "Purist", "Quick-witted", "Radiant", "Raging", "Rebel", "Redoubtable", "Refined", "Regal", "Relentless", "Renegade", "Resilient", "Resolute", "Resounding", "Revered", "Rogue", "Rune-carved", "Runewielder", "Sage", "Sanguine", "Savage", "Scintillating", "Seafarer", "Seer", "Sempiternal", "Shaman", "Silent", "Sinister", "Sky-born", "Sly", "Sorcerer", "Sovereign", "Spectral", "Spellbinder", "Spiritual", "Star-born", "Star-crossed", "Stargazer", "Stealthy", "Stellar", "Stormbringer", "Strategist", "Sublime", "Superb", "Supreme", "Swashbuckler", "Swift", "Swordmaster", "Tempest", "Thaumaturge", "Thunderous", "Time-bender", "Timeless", "Titanic", "Torchbearer", "Trailblazer", "Transcendent", "Trickster", "Twilight", "Tyrant", "Ubiquitous", "Unassailable", "Unbound", "Unconquerable", "Undaunted", "Unearthly", "Unfathomable", "Unflinching", "Uplifting", "Valiant", "Venerable", "Vigilant", "Visionary", "Voracious", "Warrior", "Wise", "Wraith", "Wondrous"]
    space_descriptor += ["Far-reaching", "Interstellar", "Quasar"]
    metal_descriptor += ["Ironwill", "Platinum", "Steel-hearted"]
    arcane_descriptor += ["Sorcerer's", "Spectral", "Spellbound", "Spirit", "Shamanic", "Shadowy", "Spellbound"]
    hell_descriptor += ["Inferno", "Sinister", "Tartarean", "Fiery-eyed"]
    object_descriptor += ["Amulet", "Blade", "Chalice", "Crown", "Orb", "Pendant", "Relic", "Scepter", "Shield", "Staff", "Talisman", "Totem", "Vessel", "Wand", "Weapon"]
    cosmic_stellar_descriptor += ["Astral", "Celestial", "Cosmic", "Galactic", "Interstellar", "Lunar", "Planetary", "Solar", "Stellar", "Supernova", "Universal"]
    faith_church_heaven_religious += ["Angelic", "Apostolic", "Ascetic", "Biblical", "Cherubic", "Clerical", "Devotional", "Divine", "Ecclesiastical", "Elysian", "Evangelical", "Heavenly", "Hierophant", "Hieratic", "Holy", "Messianic", "Ministerial", "Monastic", "Monk", "Mystic", "Nun", "Papal", "Parish", "Pastoral", "Patriarchal", "Pietistic", "Pontifical", "Preacher", "Priest", "Priestess", "Prophet", "Rabbinical", "Reverend", "Sacred", "Sage", "Saint", "Savior", "Sectarian", "Seraphic", "Shaman", "Shepherd", "Spiritual", "Theocratic", "Theological", "Vicar", "Virtuous"]
    loving_descriptor += ["Affectionate", "Amorous", "Ardent", "Charming", "Compassionate", "Devoted", "Enamored", "Fond", "Gentle", "Heartfelt", "Intimate", "Kind", "Loving", "Passionate", "Romantic", "Sentimental", "Sweet", "Tender", "Warm", "Yearning"]
    hate_descriptor += ["Abominable", "Acrimonious", "Aggressive", "Antagonistic", "Belligerent", "Bitter", "Brutal", "Cruel", "Detestable", "Envious", "Fierce", "Fiery", "Furious", "Hateful", "Hostile", "Indignant", "Inimical", "Irate", "Irritable", "Jealous", "Loathsome", "Malicious", "Malignant", "Menacing", "Nasty", "Odious", "Offensive", "Oppressive", "Outrageous", "Pernicious", "Pugnacious", "Rancorous", "Repugnant", "Resentful", "Ruthless", "Savage", "Spiteful", "Vengeful", "Vicious", "Vindictive", "Violent", "Virulent", "Vitriolic", "Wicked"]
    secret_descriptor += ["Arcane", "Concealed", "Covert", "Cryptic", "Clandestine", "Discreet", "Elusive", "Enigmatic", "Esoteric", "Hidden", "Inscrutable", "Mysterious", "Mystic", "Occult", "Private", "Secretive", "Stealthy", "Subtle", "Surreptitious", "Undisclosed", "Unrevealed", "Veiled"]
    guardian_rank += ["Custodian", "Defender", "Guardian", "Keeper", "Protector", "Sentinel", "Vigilant", "Warden", "Watchman"]
    noble_rank += ["Aristocrat", "Baron", "Count", "Duke", "Earl", "Emperor", "King", "Knight", "Lady", "Lord", "Monarch", "Noble", "Prince", "Princess", "Queen", "Regent", "Royal", "Sovereign"]
    legal_judicial_objects += ["Charter", "Code", "Decree", "Edict", "Law", "Legislation", "Mandate", "Ordinance", "Precept", "Regulation", "Rule", "Statute"]
    art_creativity_descriptor += ["Artistic", "Creative", "Cultural", "Elegant", "Expressive", "Imaginative", "Innovative", "Inspiring", "Intellectual", "Literary", "Poetic", "Refined", "Sophisticated", "Stylish"]
    intellectual_thoughtful_descriptor += ["Analytical", "Astute", "Brainy", "Cerebral", "Clever", "Educated", "Erudite", "Genius", "Intellectual", "Learned", "Logical", "Philosophical", "Rational", "Reasoned", "Sagacious", "Savvy", "Scholarly", "Shrewd", "Smart", "Sophisticated", "Thoughtful", "Wise"]
    gaseous_descriptor += ["Aerial", "Airy", "Atmospheric", "Breezy", "Ethereal", "Gaseous", "Misty", "Vaporous", "Windy"]
    flora_natural_beauty += ["Arboreal"]
    color_descriptor += ["Gilded", "Golden-hearted", "Jade-eyed", "Opalescent", "Platinum"]
    nature_descriptor += ["Frost-bound", "Meadowborn", "Moonlit", "Nebula-born", "Oceanic", "Polar", "Rainmaker", "Sky-born", "Star-born", "Sun-born", "Tempest"]
    feelings_descriptor += ["Fervent", "Fiery-eyed", "Flame-hearted", "Furious", "Gallant", "Glorious", "Greathearted", "Harmonious", "Heavenly", "Hero", "Jovial", "Judicious", "Keen", "Lauded", "Leviathan", "Lionhearted", "Majestic", "Maleficent", "Martial", "Masterful", "Maverick", "Meteoric", "Mighty", "Miraculous", "Mirthful", "Misty", "Monstrous", "Mysterious", "Nefarious", "Nimble", "Noble", "Nocturnal", "Nomadic", "Notorious", "Ominous", "Outlandish", "Outrageous", "Passionate", "Pathfinder", "Peacekeeper", "Peerless", "Peregrine", "Perilous", "Pillar", "Pioneering", "Pirate", "Powerhouse", "Praetorian", "Precocious", "Predatory", "Preternatural", "Prime", "Profound", "Prophetic", "Prowler", "Pulsating", "Purist", "Pyrotechnic", "Questing", "Quick-witted", "Radiant", "Raging", "Rampant", "Ranger", "Ravaging", "Rebel", "Reckoning", "Redoubtable", "Refined", "Regal", "Relentless", "Renegade", "Resolute", "Resounding", "Revered", "Rogue", "Runewielder", "Sage", "Sanguine", "Savage", "Scintillating", "Scorcher", "Seafarer", "Seer", "Sempiternal", "Shadow", "Shaman", "Shapeshifter", "Sinister", "Sky-born", "Sly", "Solar", "Sorcerer", "Soulbound", "Sovereign", "Spectral", "Spellbinder", "Sphinx-like", "Spiritual", "Star-crossed", "Stargazer", "Stealthy", "Stellar", "Stormbringer", "Strategist", "Sublime", "Superb", "Supreme", "Swashbuckler", "Swift", "Swordmaster", "Thaumaturge", "Thunderous", "Time-bender", "Timeless", "Titanic", "Torchbearer", "Trailblazer", "Transcendent", "Tribal", "Trickster", "Twilight", "Tyrant", "Ubiquitous", "Unassailable", "Unbound", "Unconquerable", "Undaunted", "Unearthly", "Unfathomable", "Unflinching"]
    space_descriptor += ["Interstellar", "Nebula-born", "Quasar", "Solar", "Stargazer", "Star-crossed", "Stellar"]
    metal_descriptor += ["Platinum"]
    arcane_descriptor += ["Oracle", "Orbiting", "Sorcerer", "Spectral", "Spellbinder", "Sphinx-like", "Spiritual", "Thaumaturge", "Time-bender", "Witch"]
    hell_descriptor += ["Ferocious", "Fiery-eyed", "Flame-hearted", "Flaming", "Inferno", "Maleficent", "Sinister"]
    object_descriptor += ["Amulet", "Goblet", "Grail", "Orb", "Pillar", "Scepter", "Statue", "Stone", "Sword", "Thorn", "Torch"]
    cosmic_stellar_descriptor += ["Celestial", "Galactic", "Interstellar", "Lunar", "Nebula-born", "Quasar", "Solar", "Star-crossed", "Stargazer", "Stellar", "Sublime", "Supernatural", "Supreme", "Temporal", "Timeless", "Titanic", "Transcendent", "Twilight", "Ubiquitous", "Ultimate", "Uncharted", "Unearthly", "Unfathomable", "Unforgiving", "Universal", "Unseen"]
    color_descriptor += ["Azure", "Verdant"]
    nature_descriptor += ["Verdant", "Winterborn"]
    feelings_descriptor += ["Valorous", "Venerable", "Vengeful", "Vigilant", "Vindictive", "Visionary", "Volatile", "Wicked", "Wild", "Wise", "Wrathful", "Yearning", "Zealot", "Zestful"]
    space_descriptor += ["Alien", "All-Seeing", "Interstellar", "Stellar", "Zodiac"]
    metal_descriptor += ["Alabaster", "Amethyst", "Xenolith"]
    arcane_descriptor += ["Alchemist", "Archmage", "Aurora", "Bewitched", "Witch", "Wizard", "Wraithlike"]
    hell_descriptor += ["Fiery", "Infernal", "Sulfuric", "Vengeful", "Wicked", "Wrathful"]
    object_descriptor += ["Amulet", "Arcane", "Grimoire", "Orb", "Pillar", "Scepter", "Statue", "Stone", "Sword", "Talisman", "Thorn", "Torch", "Wand"]
    cosmic_stellar_descriptor += ["Celestial", "Galactic", "Interstellar", "Lunar", "Nebula-born", "Quasar", "Solar", "Star-crossed", "Stargazer", "Stellar", "Sublime", "Supernatural", "Supreme", "Temporal", "Timeless", "Titanic", "Transcendent", "Twilight", "Ubiquitous", "Ultimate", "Uncharted", "Unearthly", "Unfathomable", "Unforgiving", "Universal", "Unseen", "Untamed"]
    faith_church_heaven_religious += ["Celestial", "Cherubic", "Divine", "Elysian", "Ethereal", "Heavenly", "Holy", "Mythical", "Sacred", "Seraphic", "Spectral", "Spiritual", "Sublime", "Supernatural", "Supreme", "Temple", "Unseen", "Valkyrie's", "Venerable", "Zenith"]
    elder_descriptor += ["Ancient", "Antique", "Archaic", "Elder", "Historic", "Legendary", "Mythic", "Old", "Timeless", "Venerable", "Vintage"]
    loving_descriptor += ["Affectionate", "Alluring", "Ardent", "Charming", "Delightful", "Dreamy", "Enchanting", "Loving", "Romantic", "Sensual", "Sentimental", "Sultry"]
    hate_descriptor += ["Baleful", "Belligerent", "Bitter", "Brutal", "Cruel", "Ferocious", "Fierce", "Fiery", "Furious", "Grim", "Harsh", "Hostile", "Malevolent", "Malign", "Menacing", "Merciless", "Ruthless", "Savage", "Sinister", "Stern", "Stormy", "Tartarean", "Terrifying", "Threatening", "Treacherous", "Turbulent", "Violent", "Villainous", "Vindictive", "Wicked", "Wrathful"]
    secret_descriptor += ["Arcane", "Cryptic", "Enigmatic", "Esoteric", "Hidden", "Inscrutable", "Mysterious", "Mystical", "Occult", "Secret", "Shadowy", "Subtle", "Surreptitious", "Unseen", "Veiled"]
    guardian_rank += ["Defender", "Guardian", "Keeper", "Protector", "Sentinel", "Vigilant", "Watchman", "Warden"]
    noble_rank += ["Aristocratic", "Baronial", "Dignified", "Eminent", "Exalted", "Grand", "Honorable", "Imperial", "Kingly", "Lordly", "Majestic", "Noble", "Regal", "Royal", "Sovereign"]
    legal_judicial_objects += ["Charter", "Code", "Decree", "Edict", "Law", "Legislation", "Mandate", "Ordinance", "Precept", "Regulation", "Rule", "Statute"]
    art_creativity_descriptor += ["Artistic", "Creative", "Cultural", "Elegant", "Expressive", "Imaginative", "Innovative", "Inspiring", "Intellectual", "Literary", "Poetic", "Refined", "Sophisticated", "Stylish"]
    intellectual_thoughtful_descriptor += ["Analytical", "Astute", "Brainy", "Cerebral", "Clever", "Educated", "Erudite", "Genius", "Intellectual", "Learned", "Philosophical", "Sage", "Scholarly", "Scientific", "Thoughtful", "Wise"]
    gaseous_descriptor += ["Zephyrian"]
    flora_natural_beauty += ["Flourishing", "Lush", "Luxuriant", "Verdant", "Zenith"]
    wilderness_descriptor += ["Feral", "Forested", "Jungle", "Marshy", "Meadow", "Moorish", "Mountainous", "Savannah", "Tropical", "Tundra", "Wilderness", "Woodland"]
    mythical_legendary_descriptor += ["Arcane", "Chimerical", "Dragon", "Ethereal", "Fabled", "Fairy", "Folkloric", "Legendary", "Mythic", "Mythological", "Nautical", "Nymph", "Olympian", "Otherworldly", "Phantasmagorical", "Spectral", "Supernatural", "Unearthly"]
    hunting_wilderness_descriptor += ["Falcon-eyed", "Hunter", "Huntsman", "Ranger", "Stalker", "Tracker", "Trapper"]
    ghost_spirit_descriptor += ["Ectoplasmic", "Ghostly", "Phantasmal", "Spectral", "Spirit", "Wraith"]
    giant_large_entity_descriptor += ["Behemoth", "Colossal", "Gargantuan", "Giant", "Juggernaut", "Leviathan", "Mammoth", "Titan", "Tremendous"]
    color_descriptor += ["Bloodmoon", "Boreal", "Celestia", "Crimson"]
    nature_descriptor += ["Blizzard", "Boreal", "Coral"]
    feelings_descriptor += ["Chaotic", "Dire"]
    space_descriptor += ["Celestia", "Chrono", "Constellation", "Cosmos", "Darkstar"]
    arcane_descriptor += ["Cipher", "Clairvoyant", "Cloak", "Cobweb", "Crystal", "Cthulhu", "Deity", "Dimension", "Dragonfire", "Dawnbringer"]
    object_descriptor += ["Cloak", "Cobweb", "Crypt", "Crystal"]
    cosmic_stellar_descriptor += ["Celestia", "Chrono", "Constellation", "Cosmos", "Crimson", "Darkstar", "Dimension"]
    faith_church_heaven_religious += ["Celestia", "Deity"]
    hell_descriptor += ["Crimson", "Dire", "Dissonance"]
    secret_descriptor += ["Cipher", "Cloak", "Crypt"]
    gaseous_descriptor += ["Cosmos"]
    flora_natural_beauty += ["Coral"]
    wilderness_descriptor += ["Boreal"]
    mythical_legendary_descriptor += ["Celestia", "Cthulhu", "Darkstar", "Deity", "Dragonfire"]
    hunting_wilderness_descriptor += ["Dragonfire"]
    ghost_spirit_descriptor += ["Cloak", "Crypt", "Cthulhu"]
    giant_large_entity_descriptor += ["Cthulhu"]
    color_descriptor += ["Dusk", "Eclipse", "Ethereal", "Iridescent"]
    nature_descriptor += ["Dusk", "Eclipse", "Elysium", "Fathom", "Fenrir", "Feral"]
    feelings_descriptor += ["Ethereal", "Feral", "Immortal"]
    space_descriptor += ["Eclipse", "Galaxy", "Horizon", "Hyperion"]
    arcane_descriptor += ["Dreamweaver", "Elemental", "Elfstone", "Ember", "Fable", "Fae", "Falcon", "Fenrir", "Firebrand", "Flametongue", "Fulcrum", "Gauntlet", "Ghoul", "Glitch", "Glyph", "Golem", "Grimoire", "Gryphon", "Guardianship", "Harbinger", "Hex", "Hydra", "Iceborn", "Illusion", "Impulse", "Incantation", "Inferno", "Invoker", "Ion", "Jester", "Juggernaut", "Kaleidoscope", "Kraken", "Leviathan", "Libra", "Lightbringer"]
    object_descriptor += ["Elfstone", "Ember", "Falcon", "Gauntlet", "Ghoul", "Glitch", "Glyph", "Golem", "Grimoire", "Gryphon", "Hex", "Horizon", "Hydra", "Iceborn", "Illusion", "Incantation", "Inferno", "Invoker", "Ion", "Jester", "Juggernaut", "Kaleidoscope", "Kraken", "Leviathan", "Libra", "Lightbringer"]
    cosmic_stellar_descriptor += ["Eclipse", "Galaxy", "Horizon", "Hyperion"]
    faith_church_heaven_religious += ["Elysium", "Immortal"]
    hell_descriptor += ["Fenrir", "Feral", "Firebrand", "Ghoul", "Hydra", "Inferno"]
    secret_descriptor += ["Dreamweaver", "Elemental", "Elfstone", "Fable", "Fae", "Fenrir", "Ghoul", "Glitch", "Glyph", "Golem", "Grimoire", "Gryphon", "Harbinger", "Hex", "Hydra", "Illusion", "Incantation", "Inferno", "Invoker"]
    gaseous_descriptor += ["Ion"]
    flora_natural_beauty += ["Elysium"]
    wilderness_descriptor += ["Fathom", "Fenrir", "Feral"]
    mythical_legendary_descriptor += ["Elemental", "Elfstone", "Fae", "Fenrir", "Firebrand", "Flametongue", "Fulcrum", "Gargoyle", "Ghoul", "Golem", "Grimoire", "Gryphon", "Harbinger", "Hex", "Hydra", "Hyperion", "Iceborn", "Immortal", "Impulse", "Incantation", "Inferno", "Invoker", "Ion", "Jester", "Juggernaut", "Kaleidoscope", "Kraken", "Leviathan", "Lightbringer"]
    hunting_wilderness_descriptor += ["Falcon", "Fenrir", "Feral", "Firebrand", "Flametongue", "Gargoyle", "Ghoul", "Golem", "Gryphon", "Hydra", "Juggernaut", "Kraken", "Leviathan"]
    ghost_spirit_descriptor += ["Fable", "Fae", "Ghoul", "Grimoire", "Gryphon", "Harbinger", "Hex", "Hydra", "Illusion", "Incantation", "Inferno"]
    giant_large_entity_descriptor += [ "Ghoul", "Golem", "Gryphon", "Juggernaut", "Kraken", "Leviathan"]


    descriptor += [
    # Generic Descriptors
        "Enigmatic",
        "Thousand",
        "Hundred",
        "Only",
        "Second",
        "First",
        "Seventh",
        "Last",

        "Curse"
        
        "Lorekeeper",
        "Lunar",
        "Lycan",
        

        "Maelstrom",
        "Magma", "Mandrake", "Manticore", "Marauder", "Matrix",    "Mecha", "Meld",
        "Merlin", "Mimic", "Mirage", "Mistwalker", "Monolith", "Moonshade", 
        "Mystique", "Nebula", "Nemesis", "Nether", "Nexus", "Nightshade", "Nimbus",
        "Nirvana", "Nova", "Oblivion", "Omen", "Onyx", "Oracle", "Orbit", "Ouroboros", 
        "Pandemonium", "Paradox", "Phantasm", "Phoenix", "Pirate", "Plasma", "Portal",
        "Potion", "Prowler", "Psion", "Quantum", "Quasar", "Quest", "Quicksilver", 
        "Radiance", "Ragnarok", "Reaper", "Reckoner", "Redwood", "Revenant", "Rift", "Rime",
        "Rune", "Saga", "Sage", "Sanguine", "Savant", "Scarab", "Scion", "Serpent", "Shadow", 
        "Shaman", "Siren", "Solstice", "Sorcery", "Soulfire", "Specter", "Sphinx", "Spire",
        "Spirit", "Starfall", "Stormcaller", "Sunder", "Sunflare", "Supernova", "Synthesis", 
        "Terra", "Thorn", "Thunder", "Timekeeper", "Titan", "Totem", "Trance", "Transcend",
        "Tribunal", "Twilight", "Undertow", "Universe", "Utopia","Valkyrie","Vapor","Vendetta",
        "Aegean", "Amazon's", "Amazonian", "Archipelago", "Asgardian", "Atlantean", "Aztec",
        "Bay", "Beach", "Beachy",
        "Garden", "Gas", "Gaseous", "Gulf",
        "Gorge", "Gorgonian", "Grassland",
        "Graveyard", "Green", "Grove",
        "Guild's", "Hamlet",
        "Harbor", "Heart", "Heath",
        "Hedgerow", "Helian",
        "Heliospheric",
        "Hill", "Hive", "Hollow",
        "Homeric", "Horned", "Hourly",
        "Hourglass", "Hunting", "Ice",
        "Icicle", "Icy",    "Ink",
        "Inkwell", "Inkwork", "Inn's",
        "Island", "Islet", "Isolated", "Jungle",
        "Keep", "Key", "Lab", "Laboratory",
        "Labyrinth", "Labyrinth's",
        "Labyrinthine", "Lagoon",
        "Lake", "Lantern", "Last", "Leafy",
        "Legendary",
        "Lethal",
        "Library",
        "Lich",
        "Life",
        "Lightning",
        "Lion-hearted",
        "Liquid",
        "Lively",
        "Living",
        "Lizard",
        "Lonely",
        "Long",
        "Loom",
        "Looming",
        "Lordly",
        "Lord Of the",
        "Lord Of",
        "Lost",
        "Love Of",
        "Loyal",
        "Luminous",
        "Lunar",
        "Lupine",
        "Lush",
        "Lustrous",
        "Luxurious",
        "Lyre", "Magic", "Magma",
        "Magnetic", "Magnetospheric", "Mahogany", "Majestic", "Malignant", "Malevolent", "Mammoth",
        "Mangrove", "Mantle", "Manticorian", "Marble", "Marine", "Marketplace", "Marsh", "Marshy",
        "Marvelous", "Master", "Matinal", "Mausoleum", "Maze", "Meadow", "Medallion", "Meditative",
        "Medusian", "Melancholic", "Menagerie", "Menacing", "Mental", "Mercurial", "Merry",
        "Mesopotamian", "Meteor", "Meteoric", "Meteoritic", "Metropolis", "Midnight", "Mighty",
        "Militant", "Millennial", "Mindful", "Mine", "Minotaur", "Minotaurine", "Miraculous",
        "Mirror", "Mirthful", "Mischievous", "Mist", "Mistral", "Misty", "Molten", "Monastic",
        "Monastery", "Monolithic", "Monstrous", "Momentary",  "Moor", "Morass",    "Moss",
        "Motivated", "Mountain", "Mountainous", "Mournful", "Muddy", "Mulberry", "Mummy",
        "Museum", "Mustard", "Mutant", "Myrmidonic", "Mysterious", "Mystic", "Mystical",
        "Mythical",    "Nautical", "Nebulous", "Nemean", "Nemesis", "Neon", "Nether", "Night",
        "Noble", "Nocturnal",
        "Nomadic", "Nordic", "Notorious", "Nova", "Oasis", "Observatory", "Obsidian", "Obsolete",
        "Ocean", "Oceanic", "Odin's", "Olympian", "Optimistic", "Opulent", "Oracular", "Orb", 
        "Orbital", "Orchard", "Orchid", "Ornate", "Orphean", "Outlandish", "Outpost", "Outraged",
        "Overgrown", "Owl's", "Palace", "Palm", "Palatial", "Parched", "Parliament", "Pastoral",
        "Peaceful", "Pearlescent", "Peat", "Pebble", "Pegasus", "Penitentiary", "Perfumed",
        "Perilous", "Perpetual", "Petrified", "Phantom", "Phoenix", "Pine", "Pinnacle", "Pirate's",
        "Placid", "Planetary", "Plant", "Plateau", "Platinum", "Pleasant", "Plum", "Polar",
        "Ponderous", "Poppy", "Porcelain", "Portal", "Port", "Potent", "Prairie", "Precious",
        "Predator", "Primeval", "Primordial", "Prince's", "Princely", "Princess", "Prismatic",
        "Prison", "Private", "Profound", "Prosperous", "Protected", "Proud", "Pumpkin", "Pungent",
        "Pure", "Purple", "Pyramid", "Quartz", "Queen's", "Quicksand", "Quiet", "Quill",
        "Radiant", "Raging", "Rainbow", "Rainforest", "Rampart", "Ranger's", "Ravaged", "Raven",
        "Rebel", "Reclusive", "Red", "Regal", "Relic", "Remnant", "Remote", "Renegade", "Resplendent",
        "Restless", "Revered", "Rhombus", "Rich", "Riddle", "Rift", "Righteous", "River", "Roaming",
        "Robotic", "Rock", "Rocky", "Rogue", "Rose", "Royal", "Ruby", "Rugged", "Ruined", "Runic",
        "Rural", "Rustic", "Rusty", "Sacred", "Sad", "Sage", "Sapphire", "Savage", "Scarlet",
        "Scenic", "Scented", "Scholar's", "School", "Scorching", "Secluded", "Secret", "Seductive",
        "Selenian", "Semi-Precious", "Serpent's", "Serpentine", "Settler's", "Shadowy", "Shady",
        "Shallow", "Shaman's", "Shattered", "Shepherd's", "Shielded", "Shimmering", "Shining",
        "Shivering", "Shrine", "Sickly","Vengeance","Vertex","Vesper","Vex","Vindicator",
        "Virtuoso","Visage","Void","Vortex","Warden",

        "Warp","Watcher", "Whirlwind","Wildfire","Willow","Wisp","Witcher","Wizardry","Wraith",
        "Wyvern", "Xenon",        "Ubiquitous"        "Ultramarine",        "Unemotional","Unhappy",        "Universal",
        "Unstoppable",        "Unyielding",        "Uranian",        "Urn",           "Ursine",
        "Mantle",        "Radiant",
        "Vessel",                       "Epochal",        "Twilight",        "Primeval",
        "Compass",        "Millennial",        "Meridian",        "Hammer",
        "Eternal",        "Fleeting",             "Black Hole",           "Meteoritic",
        "Edwardian",            "Samurai",            "Cosmic",           "Nebulous",   
        "Norman",           "Orbital",           "Han",           "Orbital",
        "Gregorian",           "Renaissance",        "Spartan",           "Prohibition",    
        "Crusader",         "Hellenistic",           "Sanskrit",            "Dynastic",
        "Flapper",           "Napoleonic",           "Pharaonic",   
        "Interstellar",            "Elizabethan",          "Feudal",           "Age",
        "Cyclic",          "Timeless",         "Neutron",                "Punctual",
        "Quill",                        "Bygone",        "Banner",        "Blade",
        "Brooch",        "Buccaneer",
        "Byzantine",        "Bat",        "Bipedal",        "Black",        "Blending",
        "Blood",        "Brass",        "Brave",        "Bursting",
        "Butterfly",        "Byzantine",                "Chiropteran",        "Crested",
        "Curse",        "Cursed",        "Celestial",
        "Celtic",         "Cat",        "Celestial",        "Collector",        "Conjurer",
        "Coral",        "Cosmic",        "Crimson",        "Desert",
        "Daemonian",        "Dawn",        "Draconic",        "Dimensional",        "Eldritch",
        "Eclipse",        "Eagle",        "Eagle's",        "Edo",
        "Eternal",        "Extraterrestrial",          "Fountain",        "Fanged",
        "Feathered",        "Feline",        "Finned",        "Fire-breathing",
        "Fuchsia",        "Feather",           "Fiery",        "Hermitage",        "Horned",
        "Incan",         "Icy",        "Indigo",        "Infinite",        "Lion-hearted",
        "Lion's",        "Leechy",        "Luminous",
        "Lunar",                "Medieval",         "Mammalian",        "Maned",
        "Masked",        "Melancholy",        "Mermaid-tailed",
        "Mist",        "Misty",        "Minotaur's",        "Momentary",        "Moonlit",
        "Mountain",        "Mysterious",        
        "Nebulous",        "Necromancer",        "New",        "Nightmare",        "Noble",
        "Nemean",        "Nomadic",        
        "Old",        "Ophidian",        "Orange",        "Orb",        "Owl",
        "Ottoman",        "Oceanic",        "Olympian",
        "Pain",        "Paladin",        "Passionate",        "Pawed",
        "Pegasus-winged",        "Piscine",
        "Pirate's",        "Plague",        "Poisonous",        "Powder",
        "Power",        "Punk",        "Purifying",
        "Pyramid's",        "Phalanx",        "Quasar",                "Radiant",
        "Rainstorm",
        "Raptor",        "Raven",        "Red",        "River",        "River's"
        "Rogue",        "Ruby",        "Rune",
        "Runer",         "Renaissance",        "River",        "Radiant",
        "Rainforest",        "Ranch",        "Raspberry",        "Rat",
        "Ravine",        "Ravishing",        "Reckless",        "Reef",
        "Relaxed",        "Relentless",        "Relic",           "Reptilian",
        "Resentful",        "Resilient",        "Restless",        "Reverent",
        "Ridge",        "River",        "Riverine",
        "Rocky",        "Romantic",        "Rooted",        "Rose",        "Ruby",
        "Ruins",        "Rust",        "Ruthless",
        "Romanesque",        "Sand",        "Scaled",        "Science",
        "Second",        "Serpentine",        "Serpent's",
        "Seventh",        "Shadow",        "Shaman's",        "Shark-toothed",
        "Shell-backed",        "Silver",        "Simian",
        "Skeleton",        "Smiling",        "Smoke",        "Snail-shelled",
        "Solar",        "Sorcerous",        "Spark",        "Speaker",
        "Spell",        "Sphinx",        "Spined",        "Spring",
        "Stars",        "Starting",        "Steam",        "Stone",
        "Storm",        "Strong",        "Summer",        "Sun Stone's",
        "Sunstone",        "Silent",        "Sirenic",        "Solar",
        "Stellar",        "Stoic",        "Swift",        "Sword",
        "Sphinx's ",        "Scarlet",        "Stinger",     
        "Sacred",        "Sad",        "Salmon",        "Sanctuary",
        "Sandy",        "Sapphire",        "Satisfied",        "Satyric",
        "Savage",        "Savanna",        "Savannah",        "Scarlet",
        "School",        "Scrub",        "Sea",        "Seashore",
        "Secular",        "Seismic",        "Serene",        "Sewer",
        "Seychelle",        "Shaded",        "Shadowy",        "Shore",
        "Shrine",        "Sienna",        "Sigil",        "Silent",
        "Silver",        "Sirenian",        "Slate",        "Slimey",
        "Solar",        "Sorrowful",        "Sparkling",        "Spectral",
        "Sprouting",        "Square",        "Stadium",        "Stalwart",
        "Starlit",        "Steadfast",        "Steamy",        "Stellar",
        "Steppe",        "Stern",        "Stoic",        "Stone",
        "Strait",        "Stratospheric",        "Stream",        "Stressed",
        "Studio",        "Stygian",        "Subterranean",
        "Sunlit",        "Supernova",        "Suspicious",        "Swamp",
        "Swampy",        "Sword",        "Sylvan",        "Sympathetic",
        "Swift",        "Scepter",                 "Staff",        "Shield",
        "Spire",        "Scroll",
        "Satellite",        "Seasonal",        "Stellar",
        "Temporal",         "Tailed",        "Tamer of",        "Tentacled",
        "Third",        "Thunder",        "Tiger",        "Tigerstrip",
        "Titan",        "Tomb",        "Trival",        "True",
        "Turquoise",        "Tartarean",        "Thundering",
        "Timeless",       "Titanic",        "Trojan",
        "Totem's",        "Troll's",        "Tailed",
        "Talon",
        "Tangerine",
        "Tapestry",
        "Taupe",
        "Tavern",
        "Tawny",        "Teal",        "Tectonic",        "Tempestuous",
        "Temple",        "Tenacious",        "Tender",        "Terrified",
        "Theater",        "Thicket",        "Thorny",        "Thundering",
        "Tidal",        "Tide",        "Timely",        "Tomb",
        "Topaz",        "Totem",        "Tower",        "Town",
        "Transient",        "Tusked",        "Tudor",        "Tundra",
        "Tunnel",        "Turquoise",        "Twilight",        "Twisted",
        "Typhoon",        "Traveling",        "Undying",
        "Underworld",        "Ultraviolet",        "Valiant",
        "Valley",        "Vanirian",
        "Vapor",        "Vampiric",
        "Vampire's",        "Valkyrian",
        "Valkyrie's",        "Vengeful",
        "Venomous",        "Veteran",
        "Victorian",        "Victorious",
        "Viking",           "Violet",
        "Voice",        "Void",
        "Voidborne",        "Vulpine",
        "Vellum",        "Venusian",
        "Verdant",        "Vermilion",
        "Vernal",        "Vexing",
        "Vibrant",        "Vigilant",
        "Village",        "Vine",
        "Volcanic",        "Volcano",
        "Voracious",        "Vulcanian",
        "Vecna's",        "Vesperal", 
        "Vintage",         "Victorian",  
        "Voidless",              "Windy",
        "Winged",        "Witchy",
        "Withering"        "Woodland",
        "Woods",        "Woody",
        "Workshop",        "Worried",
        "Winged",        "Wandering",
        "Warm",        "Wary",
        "Watery",        "Wavy",
        "Web",        "Wheelbraker",
        "Whispering",        "Whistle"
        "Warping",        "Water",
        "Whale",        "White",
        "Wild",        "Wise",
        "Wolf",        "Wolf's"
        "Wrathful",        "Wight",
        "Western",         "X-ray",  
        "Yesteryear",          "Young",
        "Zen",        "Zeusian"
        "Joyful","Zealous",        
"Zenith","Zephyr",
"Zombie","Zombie's",
"Zone","Zoo", 
"Zypher",        "Antediluvian",
        "Anvil",        "Antlered",
        "Apprehensive",        "Aprendice",
        "Aquatic",        "Archaic",
        "Arctic",        "Ardent",
        "Arena",        "Arch",
        "Archfey",        "Ardent",
        "Arena's",        "Arrogant",
        "Arachnid",        "Austere",
        "Avatar",        "Awakened",
        "Badger",        "Baobab's",
        "Barracks",        "Barren",
        "Bearded",        "Behemoth",
        "Benevolent",        "Beryl",
        "Bitter",        "Blazing",
        "Blooming",        "Blossoming",
        "Blue",
        "Boar's",
        "Boastful",        "Bog",
        "Boggy",        "Bone",
        "Book",        "Booming",
        "Bountiful",        "Boastful",
        "Bramble",        "Brain",
        "Brave",        "Brimstone",
        "Bronce",        "Bronze",
        "Brook",        "Brown",
        "Bridge",        "Brush",
        "Buccaneer",        "Budding",
        "Burgundy",        "Burned",
        "Bygone"
    ]

    rank += [
        "Apparition",    "Aprentice",
        "Archer",        "Archfey",
        "Archmage",        "Argonaut",
        "Armour",        "Arrow",
        "Artisan",        "Ash",
        "Assassin",        "Abyss",
        "Abyssal",        "Abbot",
        "Abbess",        "Acolyte",
        "Admiral",        "Adventure",
        "Adventurer",        "Afterlifer",
        "Aero",        "Agent",
        "Alchemist",        "Alpha",
        "Ambassador",        "Anarchist",
        "Angel",        "Anthropologist",
        "Antler",        "Apostle",
        "Apparition",        "Apprentice",
        "Archer",        "Archfey",
        "Archbishop",        "Archmage",
        "Argonaut",        "Armour",
        "Arrow",        "Artisan",
        "Ash",        "Assassin",
        "Atlas",        "Augur",
        "Avatar",
        ]
    descriptor += [


        # C
        "Calm",        "Camp",
        "Canary",        "Candle",
        "Canopy",        "Canyon",
        "Capricious",        "Castle",
        "Catacomb",        "Cathedral",
        "Cautious",        "Cave",
        "Cavern",        "Cavernous",
        "Celestial",        "Cemetery",
        "Cerulean",        "Celtic",
        "Chained",        "Chalice",
        "Champagne",        "Champion of",
        "Chaotic",        "Chapel",
        "Charcoal",        "Chasm",
        "Chest",        "Cherished",
        "Chimeric",        "Chivalrous",
        "Chocolate",        "Chronal",
        "Chain",        "Cheerful",
        "Chief",        "Circus",
        "Citadel",        "City",
        "Cliff",        "Clockwork",
        "Coast",        "Cobalt",
        "Cold",        "Colonial",
        "Colossal",        "Compassionate",
        "Confident",        "Confused",
        "Copper",        "Coppice",
        "Coral",        "Cobalt",
        "Crab",        "Crater",
        "Crescent",        "Crimson",
        "Crown",        "Cryptic",
        "Crystalline",        "Crown's",
        "Cunning",        "Curious",
        "Cursed",        "Cyan",
        "Cyclonic",        "Cyclopean",
        "Cyclops",        "Dark",
        "Darkness",        "Dashing",
        "Dated",        "Dauntless",
        "Dawn",        "Dawning", 
        "Deadly",        "Death",
        "Deep",        "Delta",
        "Depressed",        "Desert",
        "Desolate",        "Despondent",
        "Desperate",        "Detached",
        "Detective",        "Dewy",
        "Diabolical",        "Diadem",
        "Dimensional",        "Disappointed",
        "Discouraged",        "Distrustful",
        "Diurnal",        "Divine",
        "Diviner",        "Doctor",
        "Dormant",        "Dock",
        "Draconian",        "Dragon's",
        "Drained",        "Dream",
        "Driftwood",        "Dune",
        "Dungeon",        "Dusk",
        "Dusky",        "Dust",
        "Dynamic",                "Eager",
        "Eagle",        "Earth",
        "Earthen",        "Ebony",
        "Eclipsed",        "Eclipsing",
        "Ecliptic",        "Ecstatic",
        "Edgy",        "Egotistic",
        "Electric",        "Elegant",
        "Eloquent",        "Elusive",
        "Eldritch",        "Elven",
        "Elixir",        "Emerald",
        "Empathetic",        "Enchanted",
        "Energetic",        "Energy",
        "Engine",        "Enigmatic",
        "Enthusiastic",        "Envious",
        "Ephemeral",        "Errant",
        "Erratic",        "Equinox",
        "Ethereal",
        "Euphoric",        "Evanescent",
        "Excited",        "Exotic",
        "Extravagant",
        "Exuberant",        "Exhausted",
    
        "Fabled",
      "Faerie",
       "Fairground",
        "Faithful",
        "Falcon",
        "Fallen",
        "Fanciful",
        "Fanged",        "Farm",
        "Fearful",        "Feathered",
        "Fen",        "Fenririan",
        "Ferocious",
        "Fervent",        "Field's",
        "Fierce",        "Fiery",
        "Fire",        "First",
        "Fjord",        "Flame",
        "Flaming",        "Floral",
        "Flying",        "Fleshwork",
        "Fool",        "Forest",
        "Forge",        "Formidable",
        "Fortress",        "Fountain",
        "Frosty",        "Frozen",
        "Frustrated",        "Fuchsia",
        "Fullmetal",
        "Fullmoon",        "Furious",
        "Furred",        "Fury",
        "Futuristic", ]





















     
    if "Aberration" in creature_type:
        # descriptor for Aberration Names names
        descriptor += space_descriptor
        descriptor += [
            "Alienated",
            "Aberrant",
            "Eldritch",
            "Horror",
            "Soulless",
            "Underworld",
            "Unworldly",
            "Formless",
            "Mind",
            "Identity",
            "Forsaken",
            "Lost",
            "Eldritch",
            "Nether",
            "Astral",
            "Yellow",
            "Green",
            ]
        
        # rank for Illithid names
        rank += noble_rank + guardian_rank + guardian_rank
        rank += [
            "Abomination",
            "Manipulator",
            "Whisperer",
            "Speaker",
            "Devourer",
            "Dreamer",
            "Gazer",
            "Nethermind",
            "Born",
            "Warper",
            "Horror",
            "Warp",
            "Eater",
            "Lost",
            "Stealer",
            "Dominator",
            "Netherbrain",
            "Oblivion",
            "Harbinger",
            "Overseer",
            "Abyssmal",
            "Warden",
            "Voidshaper",
            "Controller", "Breaker",
            "Distorter",
            "Existence Ravager", "Enforcer", "Void"
            ]

        of_the += of_the_space

        #return f"The {random.choice(descriptor)} {random.choice(rank)}"

        if "Illithid" in creature_type:
            # descriptor for Illithid names
            descriptor += [
                "Mindflayer",
                "Mindbending", "Brainfeaster", "Thoughtstealer", "Eldritch", "Voidgazer",
                "Psionic", "Deepdweller",  "Insidious", "Arcane",
                "Otherworldly", "Tentacled", "Soulflayer", "Dimensional", "Mystic",
                "Cerebral", "Astral", "Telepathic", "Shadowspeaker", "Dreamweaver",
                "Mindreaper", "Voidborn", "Inscrutable", "Starcaller", "Warpwalker",
                ]

            # rank for Illithid names
            rank += [
                "Oracle",
                "Mindlord", "Brainmaster", "Psychic Sovereign", "Elder Brain", "Void Seer",
                "Arcanist", "Lurker", "Thought Tyrant", "Cerebromancer", "Mindking",
                "Mindqueen", "Encephalarch", "Neurocaptain", "Astral Dominator", "Psychic Emissary",
                "Synapse Commander", "Tentacle", "Brainkeeper", "Mindspeaker", "Warpweaver",
                "Strider", "Cortex Conjurer", "Gloom Prophet", "Orb Master", "Deep Controller",
                "Illithid", "Mind Flayer"
                ]
            descriptor += ["Mindbender", "Psionic", "Brainfeeder", "Thoughtstealer", "Telepathic"]
            rank += ["Mind Flayer", "Cerebral Dominator", "Brain Sovereign", "Thought Eater", "Psychic Master"]
            of_the += [
                "of the Deep Mind",
                "of the Psychic Network",
                "of the Mind Harvest",
                "of the Brain Conclave",
                "of the Mental Dominion"]


        if "Beholder" in creature_type:
            descriptor += [
                "Beholder",
                "All-Seeing",
                "Omniscient",
                "Paranoid",
                "Tyrannical",
                "Visionary",
                "Unblinking",]
            
            rank += ["Oracle",
                    "Eye",
                    "Tyrant",
                    "Overseer",
                    "Sphere",
                    "Sovereign",
                    "Orb",
                    "Lord",
                    "Watcher",
                     "Gaze"]
            rank += [
                "Tyrant",
                "Master",
                "Lord",
                "Sovereign",
                "Ruler"]

            of_the += ["of the Thousand Eyes",
                       "of the Dark Void",
                       "of the Unseen Terrors",
                       "of the Realms",
                       "of the Arcane"]


        if "Shapeshifters" in creature_type:
            descriptor += [
                "Formless",
                "Mutable",
                "Changeling",
                "Amorphous",
                "Protean",
                ]
            rank += [
                "Mimic Sovereign",
                "Shapechanger",
                "Form Warden",
                "Shift Master",
                "Mutable Lord"]
            of_the += ["of the Shifting Forms", "of the Many Faces", "of the Illusory Guises", "of the Changing Aspects", "of the Protean Nature"]


        elif "Old One" in creature_type:
            descriptor += ["Ancient", "Eldritch", "Timeless", "Mysterious", "All-Knowing"]
            rank += ["Elder Entity", "Cosmic Sage", "Star Spawn", "Void Seer", "Ancient Horror"]
            of_the += ["of the Ageless Eons", "of the Cosmic Depths", "of the Eldritch Secrets", "of the Starry Voids", "of the Ancient Mysteries"]

        elif "Mindlinker" in creature_type:
            descriptor += ["Knowledge-Seeker", "Benevolent", "Wise", "Thought-Linker", "Mind Weaver"]
            rank += ["Thought Sage", "Mental Harmonizer", "Brain Conductor", "Psychic Connector", "Mind Ambassador"]
            of_the += ["of the Collective Consciousness", "of the Wisdom Network", "of the Harmonious Minds", "of the Thought Weave", "of the Knowledge Nexus"]

        elif "Dominators" in creature_type:
            descriptor += ["Commanding", "Hierarchical", "Ruthless", "Subjugating", "Tyrant"]
            rank += ["Slave Master", "Hierarchy Lord", "Domination Sovereign", "Subjugator", "Rule Enforcer"]
            of_the += ["of the Iron Will", "of the Dominant Chain", "of the Enslaved Realms", "of the Ruthless Order", "of the Commanding Heights"]

        elif "Living Spell" in creature_type:
            descriptor += [
                "Amber",
                "Magenta",
                "Ethereal",
                "Arcane",
                "Spellbound",
                "Magical",
                "Enchanted",
                "Wizardly",
                "Green",
                ]
            rank += ["Spell Entity", "Arcane Aberration", "Magic Devourer", "Enchantment Lord", "Wizard's Curse"]
            of_the += ["of the Spell Storms", "of the Arcane Nexus", "of the Magical Anomalies", "of the Enchanted Vortex", "of the Wizard's Binding"]

        elif "Chaotic" in creature_type:
            descriptor += ["Unpredictable", "Erratic", "Mad", "Whimsical", "Anarchic"]
            rank += ["Chaos Bringer", "Anarchy Lord", "Mad Sovereign", "Whimsy Master", "Randomizer"]
            of_the += ["of the Chaotic Maelstrom", "of the Unpredictable Whirl", "of the Mad Realms", "of the Erratic Visions", "of the Anarchic Depths"]

        elif "Star Titan" in creature_type:
            descriptor += ["Cosmic", "Starborn", "Astral", "Nebulous", "Galactic"]
            rank += ["Cosmic Giant", "Nebula Lord", "Star Sovereign", "Astral Colossus", "Galaxy Dominator"]
            of_the += ["of the Star Fields", "of the Galactic Cores", "of the Astral Planes", "of the Cosmic Voids", "of the Nebula Realms"]

        elif "Alien Spawn" in creature_type:
            descriptor += ["Otherworldly", "Unearthly", "Extraterrestrial", "Alien", "Starborne"]
            rank += ["Star Fiend", "Celestial Invader", "Galactic Parasite", "Extraterrestrial Entity", "Alien Horror"]
            of_the += ["of the Distant Worlds", "of the Alien Realms", "of the Outer Cosmos", "of the Unearthly Dominions", "of the Starborne Terror"]

        elif "Parasyte" in creature_type:
            descriptor += ["Parasitic", "Mind-Control", "Body-Snatcher", "Host-Taker", "Infesting"]
            rank += ["Mind Leech", "Body Dominator", "Neural Invader", "Host Master", "Infestation Lord"]
            of_the += ["of the Host Bodies", "of the Mind Hive", "of the Control Webs", "of the Infested Realms", "of the Parasitic Dominance"]

        elif "Destiny Devouers" in creature_type:
            descriptor += [
                "Oracle",
                "Time",
                "Body",
                "Destiny",
                "Fate",
                "Chrono",
                "Fate",
                "Traveling",
                "Temporal",
                "Altered",
                "Shattered",
                "Future"
                ]
            rank += [
                "Traveler"
                "Ravager",
                "Swapping",
                "Thief",
                "Alterer",
                "Eater",
                "Predator",
                "Bender",
                "Usurper",
                "Devourer"]
            of_the += [
                "of Time",
                "of Destinies",
                "of the Vortex",
                ]

        elif npc.subrace == "Githyanki":
            descriptor += [
                "Marauding",
                "Conquering",
                "Warlike",
                "Ruthless", "Dominant"]
            rank += ["Raid Leader", "Conqueror", "Warlord", "Supreme Commander", "Battle Master"]
            of_the += ["of the Astral Raids", "of the Conquered Realms", "of the Endless Wars", "of the Ruthless Campaigns", "of the Dominant Force"]

        elif npc.subrace == "Githzerai":
            descriptor += ["Enlightened", "Mystic", "Ascetic", "Disciplined", "Harmonious"]
            rank += ["Monk Master", "Zen Lord", "Mystic Sage", "Spiritual Guide", "Harmony Keeper"]
            of_the += ["of the Inner Peace", "of the Mystic Paths", "of the Ascetic Ways", "of the Spiritual Harmony", "of the Enlightened Realms"]

    if npc.race == "Avens":
        descriptor += [
            "Avian",
            "Red", 
            "Feathered",
            "Yellow",
            "Skybound", "Winged", "Aerial", "Soaring"]
        rank += ["Sky Watcher", "Wing Leader", "Feathered Sage", "Flight Master", "Aerie Guardian"]
        of_the += ["of the High Skies", "of the Soaring Winds", "of the Cloud Realms", "of the Endless Horizon", "of the Winged Tribes"]

        if npc.subrace == "Birdfolk":
            descriptor += ["Plumaged", "Chirping", "Nesting", "Songbird", "Versatile"]
            rank += ["Flock Leader", "Nest Keeper", "Songweaver", "Wing Scout", "Feathered Elder"]
            of_the += ["of the Verdant Forests", "of the Melodious Songs", "of the Nested Heights", "of the Diverse Plumes", "of the Winged Assembly"]

        if npc.subrace == "Kenku":
            descriptor += ["Mimicking", "Crafty", "Ravenlike", "Streetwise", "Scheming"]
            rank += ["Mimic Master", "Urban Trickster", "Shadow Lurker", "Raven Sage", "Guild Spy"]
            of_the += ["of the Echoing Voices", "of the Shadowed Alleys", "of the Urban Jungle", "of the Crafty Beaks", "of the Stolen Secrets"]

        if npc.subrace == "Aarakocra":
            descriptor += ["Soaring", "Spiritual", "Windrider", "Featherpriest", "Skydancer"]
            rank += ["Wind Sage", "Sky Monk", "Feathered Seer", "Aerial Shaman", "Celestial Messenger"]
            of_the += ["of the Mountain Peaks", "of the Spiraling Thermals", "of the Sacred Winds", "of the Cloud Monasteries", "of the Heavenly Dances"]

        if npc.subrace == "Raptoran":
            descriptor += ["Mountainborn", "Windsoarer", "Cliffdweller", "Wingwarrior", "Highflyer"]
            rank += ["Cliff Guardian", "Sky Hunter", "Peak Scout", "Windrider Captain", "Aerie Protector"]
            of_the += ["of the Mountain Aeries", "of the Windcut Cliffs", "of the High Ridges", "of the Soaring Currents", "of the Lofty Nests"]

        if npc.subrace == "Tengu":
            descriptor += ["Mystical", "Folkloric", "Martial", "Wise", "Trickster"]
            rank += ["Blade Wing", "Mystic Raven", "Kenshi Master", "Lore Keeper", "Shadow Trickster"]
            of_the += ["of the Ancient Tales", "of the Hidden Dojo", "of the Martial Paths", "of the Folklore Mysteries", "of the Clever Beaks"]

        if "Owlin" in creature_type:
            descriptor += [
                "Nocturnal",
                "Wise",
                "Silent",
                "Moon",
                "Feathered",
                "Stargazer",
                "Night",
                "Star",
                ]
            rank += [
                "Wing",
                "Seer",
                "Sage",
                "Watcher",
                "Keeper",
                "Whisperer"]
            of_the += [
                "of the Moonlight",
                "of the Forests",
                "of Silence",
                "of the Skies",
                "of the Twilight",
                "of Wisdom"]

    if "Beast" in npc.race:
        descriptor += [
            "Red",
            "Magenta",
            "Yellow",
            ]
        rank += [
            "Shadow",
            ]
        if npc.subrace == "Armored Bear":
            descriptor += [
                "Mighty",
                "Ironclad", "Noble", "Warrior", "Stalwart"]
            rank += ["Bear King", "Armor Lord", "Battle Bruin", "Iron Guardian", "Noble Ursine"]
            of_the += ["of the Northern Realms", "of the Icy Fortresses", "of the Warrior Clans", "of the Iron Woods", "of the Stalwart Defenders"]

        if npc.subrace == "Monkey King":
            descriptor += ["Cunning", "Whimsical", "Mighty", "Trickster", "Adventurous"]
            rank += ["Monkey Monarch", "Wily Sovereign", "Jester King", "Trickster Lord", "Journey Master"]
            of_the += ["of the Infinite Mischief", "of the Winding Paths", "of the Mystic Mountains", "of the Cloud Realms", "of the Endless Adventure"]

        if npc.subrace == "Guardian Kong":
            descriptor += ["Colossal", "Protector", "Mighty", "Fierce", "Vigilant"]
            rank += ["Kong Guardian", "Jungle Protector", "Island Lord", "Colossus Keeper", "Titan Defender"]
            of_the += ["of the Primal Isles", "of the Ancient Jungles", "of the Titan Groves", "of the Colossal Peaks", "of the Untamed Wilds"]

        if npc.subrace == "Giant Eagle":
            descriptor += ["Majestic", "Skybound", "Soaring", "Keen-Eyed", "Noble"]
            rank += ["Eagle Lord", "Sky Master", "Wing Sovereign", "Aerial Guardian", "Feathered Monarch"]
            of_the += ["of the Soaring Heights", "of the Mountain Eyries", "of the Sky Realms", "of the Wind Currents", "of the Cloud Kingdoms"]


        if "Tiger" in creature_type:
            descriptor += [
                "White",
                "Graceful",
                "Silent",
                "Fierce",
                "Snow",
                "Mystical",
                "Alabaster",
                "Stealthy",
                "Silent",
                "Snowy",
                "Fros",
                ]
            rank += [
                "Sabertooth",
                "Tiger",
                "Sovereign",
                "Stalker",
                "Predator",
                "Striker"
                ]
            of_the += [
                "of the Snow",
                f"of the {random.choice(descriptor)} Mountain",
                f"of the {random.choice(descriptor)} Forests",
                f"of the {random.choice(descriptor)} Valleys",
                "of the Frost",
                "of the Hunt"]

        if npc.subrace == "Vulture Spirit":
            descriptor += ["Carrion", "Deathbound", "Spiritual", "Sightful", "Scavenger"]
            rank += ["Death Wing", "Carrion Lord", "Spirit Vulture", "Sky Scavenger", "Visionary Predator"]
            of_the += ["of the Death Realms", "of the Spirit Skies", "of the Carrion Fields", "of the Sightful Heights", "of the Scavenger Lands"]


        if npc.subrace == "Deer Spirit":
            descriptor += ["Gentle", "Graceful", "Spiritual", "Intuitive", "Forestbound"]
            rank += ["Forest Stag", "Gentle Guardian", "Spirit Deer", "Nature's Seer", "Woodland Sovereign"]
            of_the += ["of the Whispering Woods", "of the Gentle Glades", "of the Spiritual Trails", "of the Intuitive Paths", "of the Forest Kingdom"]

        if npc.subrace == "Giant Owl of Wisdom":
            descriptor += ["Wise", "Nocturnal", "Silentwing", "Omniscient", "Mystical"]
            rank += ["Owl Sage", "Night Seer", "Wisdom Keeper", "Silent Hunter", "Mystic Watcher"]
            of_the += ["of the Ancient Knowledge", "of the Night Skies", "of the Silent Hunt", "of the Mystic Visions", "of the Wise Woods"]

        if "Celestial Stag" in creature_type:
            descriptor += [
                "Astral",
                "Majestic",
                "Otherworldly",
                "Luminous",
                "Graceful",
                "Star",
                "Cosmic",
                ]
            rank += [
                "Antler",
                "Deer",
                "Hart",
                "Sovereign",
                "Guide"]
            of_the += [
                "of the Starry Forests",
                f"of the {random.choice(descriptor)} Meadows",
                f"of the {random.choice(descriptor)} Glades",
                f"of the {random.choice(descriptor)} Forest",
                f"of the {random.choice(descriptor)} Realms"]

        if npc.subrace == "Fenrir Wolf":
            descriptor += ["Ferocious", "Mythic", "Boundless", "Mighty",
                           ]
            rank += ["Wolf Titan", "Mythic Predator", "Howler", "Fenrir's Kin", "Raging Lycan"]
            of_the += ["of the Ancient Legends", "of the Primal Wilds", "of the Boundless Tundra", "of the Mythic Packs", "of the Mighty Roars"]

        if "Forest God" in creature_type:
            descriptor += ["Untamed", "Guardian", "Brave", "Sovereign", "Wild"]
            rank += [
                "Ferret",
                "Boar King", "Forest Protector", "Tusked Guardian", "Wild Sovereign", "Braveheart"]
            of_the += ["of the Untamed Groves", "of the Wild Thickets", "of the Ancient Forests", "of the Brave Trails", "of the Guardian Oaks"]

        if "Cosmic Whale" in creature_type:
            descriptor += [
                "Astral",
                "Stellar",
                "Majestic",
                "Cosmic",
                "Gentle",
                "Giant",
                "Starbound",
                "Star's",
                "Galaxy's",
                "Void",
                "Galactic",
                "Boreal",
                "Ferret",
                ]
            rank += [
                "Leviathan",
                "Rorcual",
                "Whale",
                "Orca",
                "Torcual"
                "Navigator",
                "Behemoth",
                "Swimmer",
                "Cetacean"]
            of_the += [
                f"of the {random.choice(descriptor)} Seas",
                f"of the {random.choice(descriptor)} Depths",
                "of the Void",
                "of the Stars",
                ]

        if npc.subrace == "Kaiju Dinosaur":
            descriptor += [
                "Green",
                "Colossal", "Terrifying", "Prehistoric", "Monstrous"]
            rank += ["Titan",
                     "Rex", "Kaiju Behemoth", "Terror", "Jurassic Overlord", "Dino Monarch"]
            of_the += ["of the Lost Worlds", "of the Ancient Ruins", "of the Primal Jungles", "of the Monstrous Lands", "of the Colossal Footprints"]

        if npc.subrace == "Kerberus Dog":
            descriptor += ["Three-Headed", "Guardian", "Infernal", "Fierce", "Loyal"]
            rank += ["Hound of Hades", "Infernal Watchdog", "Cerberus Keeper", "Three-Faced Guardian", "Hellhound Sovereign"]
            of_the += ["of the Underworld Gates", "of the Infernal Depths", "of the Guarded Realms", "of the Threefold Paths", "of the Fierce Loyalty"]

        if "Sun Scarab" in creature_type:
            descriptor += [
                "Amber",
                "Astral",
                "Solar",
                "Ancient",
                "Resilient",
                "Radiant",
                "Sacred",
                "Eternal",
                "Gold",
                "Golden",
                "Yellow",
                ]
            rank += [
                "Scarab",
                "Pharaoh",
                "Beetle",
                "Guardian",
                "Crawler",
                "Sun"
                ]
            of_the += [
                "of the Sands",
                "of the Temple",
                "of the Dunes",
                "of the Tombs",
                "of the Sun"]

        if "Moon Jackal" in creature_type:
            descriptor += [
                "Astral",
                "Nocturnal",
                "Mystical",
                "Lunar",
                "Sleek",
                "Wily",
                "Moon",
                "Night",
                "Moonlit",
                ]
            rank += ["Guardian",
                     "Predator",
                     "Prowler",
                     "Howler",
                     "Jackal",
                     ]
            of_the += [
                "of the Plains",
                "of the Hunt",
                "of the Stars",
                "of the Spirits"]

        if npc.subrace == "Spider Queen":
            descriptor += ["Weaver", "Silken", "Deadly", "Arachnid", "Matriarch"]
            rank += ["Web Mistress", "Silk Sovereign", "Venom Lord", "Arachnid Matron", "Spinner of Fates"]
            of_the += ["of the Webbed Realms", "of the Silken Threads", "of the Deadly Traps", "of the Arachnid Dominions", "of the Hidden Lairs"]

        if "World Serpent's Spawn" in creature_type:
            descriptor += [
                "Green",
                "Ancient", "Mythic", "Cosmic", "Endless", "Primordial"]
            rank += ["Serpent Progeny", "Cosmic Coiler", "Mythic Python", "Galactic Viper", "Eternal Slitherer"]
            of_the += ["of the World's Roots", "of the Cosmic Scales", "of the Mythic Depths", "of the Endless Coils", "of the Primordial Seas"]

        if npc.subrace == "Elder Elephant":
            descriptor += ["Sage", "Majestic", "Ancient", "Wise", "Gentle Giant"]
            rank += ["Elder Matriarch", "Tusker Sage", "Memory Keeper", "Gentle Titan", "Ancient One"]
            of_the += ["of the Ageless Herds", "of the Sacred Plains", "of the Ancient Wisdom", "of the Gentle Lands", "of the Majestic Paths"]

    if "Lion" in creature_type or "Leon" in creature_type:
        descriptor += [
                "Amber",
                "Yellow",
                "Regal",
                "Majestic",
                "Golden",
                "Noble",
                "Brave",
                "Lion",
                "Pride",
                "Sun",
                "Sunlit",
                "Gold",
                "Roaring",
                ]
        rank += [
                "Mane",
                "Sabertooth",
                "King",
                "Sovereign",
                "Lord",
                "Predator"]
        of_the += [
                "of the Savannahs",
                "of the Prairies",
                f"of the {random.choice(descriptor)} Realms",
                "of the Brave",
                "of the Pride",
                ]
        descriptor += [
                "Amber",
                "Maned",
                "Regal",
                "Sun",
                "Proud",
                "Roaring",
                "Lion",
                "Pride's",
                "Sun",
                "Sun's",
                "Majestic"]
        rank += [
                "King",
                "Lord",
                "Guardian",
                "Sovereign",
                "Leader"]
        of_the += [f"of the {random.choice(descriptor)} Savannas",
                   "of the Pride Lands",
                   "of the Sun",
                   "of the Roaring Clans",
                   f"of the {random.choice(descriptor)} Clans",
                   f"of the {random.choice(descriptor)} Roars"
                   ]
    if npc.race == "Beastfolk":
        descriptor += ["Feral", "Wild", "Naturebound", "Primal", "Beastly"]
        rank += ["Tribe Leader", "Nature Guardian", "Primal Warrior", "Wild Seeker", "Beast Master"]
        of_the += ["of the Untamed Wilds", "of the Primal Forests", "of the Ancient Tribes", "of the Nature's Heart", "of the Beast Realms"]

        if npc.subrace == "Arachnidfolk":
            descriptor += ["Weaver", "Silken", "Eight-Legged", "Trickster", "Fate Spinner"]
            rank += ["Web Master", "Silk Weaver", "Venom Lord", "Spinner of Lies", "Arachnid Sage"]
            of_the += ["of the Webbed Dominions", "of the Silken Threads", "of the Poisoned Fangs", "of the Trickster's Web", "of the Fateful Strands"]

        if npc.subrace == "Catfolk":
            descriptor += [
                "Prowler",
                "Agile",
                "Whiskered",
                "Whiskers",
                "Feline",
                "Stealthy",
                "Mystical",
                "Claw",
                "Shadow",
                ]
            rank += [
                "Sabertooth",
                "Lord",
                "Seer",
                "Master",
                "Sage",
                "Hunter",
                "Grace",
                ]
            of_the += [
                "of the Silent Walk",
                "of Moonlit Paths",
                ]

        if npc.subrace == "Centaur":
            descriptor += ["Hooved", "Wildheart", "Nature's Rider", "Forest Runner", "Half-Horse"]
            rank += ["Herd Leader", "Forest Guardian", "Wild Archer", "Hoofed Sage", "Pathfinder"]
            of_the += ["of the Open Plains", "of the Ancient Forests", "of the Running Rivers", "of the Wild Trails", "of the Hooved Tribes"]

        if npc.subrace == "Gnoll":
            descriptor += ["Savage", "Hyena", "Hungry", "Ravenous", "Fierce", "Chaotic"]
            rank += ["Pack Alpha", "Hyena Warlord", "Ravager", "Bone Gnawer", "Chaos Bringer"]
            of_the += ["of the Wastelands", "of the Laughing Packs", "of the Ravaged Lands", "of the Fierce Clans", "of the Chaotic Wilderness"]

        if "Insectfolk" in creature_type:
            descriptor += [
                "Green",
                "Hive-Minded", "Chitinous", "Six-Legged", "Buzzing", "Versatile"]
            rank += ["Hive King", "Colony Master", "Swarm Leader", "Bug Sage", "Nest Protector"]
            of_the += ["of the Great Hives", "of the Buzzing Swarms", "of the Chitinous Carapaces", "of the Insect Colonies", "of the Versatile Kin"]

        if npc.subrace == "Jackalmen":
            descriptor += ["Canine", "Desert-Born", "Cunning", "Ancestral", "Afterlife Guardian"]
            rank += ["Jackal Lord", "Desert Prowler", "Canine Seer", "Anubis Kin", "Sandspeaker"]
            of_the += ["of the Ancient Tombs", "of the Desert Winds", "of the Canine Packs", "of the Ancestral Spirits", "of the Sand Dunes"]

        if npc.subrace == "Lycan":
            descriptor += ["Werebeast", "Moon-Caller", "Shapeshifter", "Feral", "Cursed"]
            rank += ["Lycan Alpha", "Moon Howler", "Beast Shifter", "Feral Lord", "Cursed Wanderer"]
            of_the += ["of the Moonlit Curse", "of the Shifting Forms", "of the Feral Packs", "of the Ancient Lycanthropy", "of the Wild Hunt"]



        if npc.subrace == "Merfolk":
            descriptor += [
                "Green",
                "Aquatic", "Siren", "Ocean", "Mystical", "Deep Sea"]
            rank += ["Ocean Sovereign", "Songster", "Coral Keeper", "Tide Master", "Deep Dweller"]
            of_the += ["of the Coral Reefs", "of the Siren's Call", "of the Ocean Depths", "of the Mystical Tides", "of the Sea's Embrace"]

        if npc.subrace == "Minotaur":
            descriptor += ["Labyrinthine", "Horned", "Mighty", "Maze Guardian", "Bullheaded"]
            rank += ["Maze Master", "Horned Lord", "Labyrinth Keeper", "Bull Warrior", "Pathfinder"]
            of_the += ["of the Twisting Mazes", "of the Horned Tribes", "of the Stone Labyrinths", "of the Hidden Paths", "of the Ancient Riddles"]

        if npc.subrace == "Ratfolk":
            descriptor += ["Clever", "Scavenger", "Nimble", "Resourceful", "Urban"]
            rank += ["Rat King", "Scavenger Lord", "Sewer Sovereign", "Alley Master", "Nimble Navigator"]
            of_the += ["of the Shadowed Alleys", "of the Sewer Depths", "of the Urban Jungles", "of the Resourceful Packs", "of the Clever Minds"]

        if npc.subrace == "Scorpionfolk":
            descriptor += ["Venomous", "Desert-Born", "Stinger", "Armored", "Mystic"]
            rank += ["Scorpion King", "Venom Lord", "Desert Guardian", "Stinger Master", "Sand Shaman"]
            of_the += ["of the Scorching Sands", "of the Venomous Barrens", "of the Desert's Heart", "of the Armored Claws", "of the Mystic Dunes"]

        if npc.subrace == "Sharkfolk":
            descriptor += ["Predatory", "Deepsea", "Toothed", "Fierce", "Oceanic"]
            rank += ["Shark Lord", "Deep Hunter", "Toothed Terror", "Sea Predator", "Wave Stalker"]
            of_the += ["of the Abyssal Depths", "of the Shark Waters", "of the Oceanic Hunts", "of the Fierce Currents", "of the Predatory Schools"]

        if npc.subrace == "Skinwalker":
            descriptor += ["Shapeshifting", "Mystical", "Spirit-Walker", "Transforming", "Elusive"]
            rank += [
                "Ferret","Form Changer", "Mystic Walker", "Spirit Shifter", "Shape Sovereign", "Phantom Stalker"]
            of_the += ["of the Shifting Forms", "of the Hidden Spirits", "of the Ancient Mysteries", "of the Elusive Natures", "of the Mystic Paths"]

        if npc.subrace == "Werebear":
            descriptor += ["Bear", "Noble", "Protector", "Furry", "Strong", "Paw"]
            rank += ["Bear Guardian", "Furry Protector", "Clan Leader", "Noble Brute", "Forest Warden"]
            of_the += ["of the Deep Forests", "of the Bear Clans", "of the Mountain Trails", "of the Protector's Might", "of the Noble Roars"]

        if npc.subrace == "Werewolf":
            descriptor += ["Lycanthropic", "Moon-Howler", "Feral", "Beastly", "Nocturnal"]
            rank += ["Wolf Alpha", "Moon Stalker", "Feral Leader", "Beast Chieftain", "Night Prowler"]
            of_the += ["of the Moonlit Forests", "of the Lycan Packs", "of the Feral Wilds", "of the Beastly Hunts", "of the Nocturnal Shadows"]

        if npc.subrace == "Harpy":
            descriptor += ["Winged", "Screeching", "Taloned", "Skybound", "Siren"]
            rank += ["Harpy Queen", "Sky Screamer", "Talon Mistress", "Wind Rider", "Siren of the Skies"]
            of_the += ["of the Mountain Peaks", "of the Sky Realms", "of the Windy Cliffs", "of the Screeching Winds", "of the Aerial Dominions"]

        if npc.subrace == "Satyr":
            descriptor += ["Reveler", "Horned", "Musical", "Merry", "Forest Dweller"]
            rank += ["Pan Piper", "Forest Reveler", "Horned Dancer", "Merry Wanderer", "Nature's Bard"]
            of_the += ["of the Lush Groves", "of the Merry Woods", "of the Dancing Streams", "of the Wild Festivities", "of the Musical Glens"]

    if "Kitsune" in creature_type:
        descriptor += [
            "Astral",
            "Red",
            "Fox",
            "Foxy",
            "Enchanting",
            "Nine-Tailed",
            "Trickster",
            "Mystical",
            "Mystic",
            "Illusion",
            "Tale",
            "Enchanted",
            "Enchanter",
            "Illusory",
            "Trickster's",
            "Foxfire",
            "Cunning",
            "Trickster",
            "Nine-Tailed",
            "Tailed",
            "Blue",
            "Yellow",
            ]

        rank += [
            "Oracle",
            "Spirit",
            "Vixen",
            "Enchanter",
            "Weaver",
            "Spinner",
            "Tails",
            "Spirit",
            "Trickster",
            ]

        of_the += [
            "of the Woods",
            "of the Realms",
            "of the Glades",
            "of the Nine Tails",
            "of the Glades",
            "of the Night"]

    if "Celestial" in creature_type:
        descriptor += [
            "Amber",
            "Astral",
            "Ethereal",
            "Radiant",
            "Divine",
            "Heavenly",
            "Ethereal",
            "Sublime",
            "Sky",
            "Celestial",
            "Blessed",
            "Light's",
            "Sacred",
            "Yellow",
            "Green",
            ]
        rank += [
            "Oracle",
            "Herald",
            "Messenger",
            "Guardian",
            "Guide",
            "Emissary",
            "Light"]
        of_the += [
            "of the Spheres",
            "of the Divine",
            "of Heaven",
            "of the Light",
            "of Light"]

        if "Angelic Bloodline" in creature_type:
            descriptor += [
                "Born",
                "Touched",
                ]
            rank += [
                "Oracle",
                "Scion",
                "Heir",
                "Offspring",
                "Descendant",
                "Progeny"]
            of_the += [
                f"of the {random.choice(descriptor)} Lineage",
                f"of the {random.choice(descriptor)} Ancestors",
                f"of the {random.choice(descriptor)} Blood",
                f"of the {random.choice(descriptor)} Bloodline",
                f"of the {random.choice(descriptor)} Heritage",
                f"of the {random.choice(descriptor)} Descent"]

        if npc.subrace == "Half-Angel":
            descriptor += ["Winged", "Heaven-Touched", "Seraphic", "Divineborn", "Auroral"]
            rank += ["Winged Emissary", "Seraphic Kin", "Celestial Offspring", "Heavenly Scion", "Auroral Spirit"]
            of_the += ["of the Angelic Wings", "of the Heavenly Realms", "of the Divine Essence", "of the Ethereal Radiance", "of the Seraphic Light"]

        if npc.subrace == "Angel":
            descriptor += ["Holy", "Winged", "Seraphic", "Divine", "Messenger"]
            rank += ["Angel Protector", "Divine Herald", "Seraph Guardian", "Messenger of Light", "Winged Savior"]
            of_the += ["of the Holy Choirs", "of the Divine Mission", "of the Seraphic Host", "of the Celestial Order", "of the Ethereal Realms"]

        if npc.subrace == "Ascended":
            descriptor += ["Elevated", "Transcendent", "Divine", "Exalted", "Ascendant"]
            rank += ["Ascended Master", "Divine Being", "Elevated One", "Transcendent Sage", "Exalted Spirit"]
            of_the += ["of the Higher Planes", "of the Transcendent Light", "of the Exalted Realm", "of the Divine Ascent", "of the Eternal Elevation"]

        if "Couatl" in creature_type:
            descriptor += [
                "Green",
                "Rainbow",
                "Colored",
                "Beautiful",
                "Feathered", "Guardian", "Serpentine", "Mystic", "Vibrant"]
            rank += ["Feathered Protector", "Serpent Guardian", "Mystic Coil", "Vibrant Spirit", "Sky Serpent"]
            of_the += ["of the Feathered Wings", "of the Mystic Visions", "of the Serpentine Grace", "of the Vibrant Scales", "of the Guardian Skies"]

        if "Forgotten God" in creature_type:
            descriptor += [
                "Lost",
                "Ancient",
                "Forgotten",
                "Fallen",
                "Mythic"]
            rank += [
                "Deity",
                "Divinity",
                "Spirit",
                "Echo",
                "Being"]
            of_the += [
                "of the Lost Temples",
                "of the Forgotten Realms",
                "of the Ancient Faiths",
                "of the Mythic Memories",
                "of the Vanished Worship"]

        if npc.subrace == "Lesser God":
            descriptor += ["Minor", "Lesser", "Divine", "Eternal", "Humble"]
            rank += ["Lesser Deity", "Minor Divinity", "Eternal Spirit", "Humble Godling", "Divine Aspect"]
            of_the += ["of the Lesser Realms", "of the Minor Miracles", "of the Eternal Cycle", "of the Humble Faith", "of the Divine Fragments"]

        if npc.subrace == "Minor God":
            descriptor += ["Lesser", "Divine", "Eternal", "Humble", "Patron"]
            rank += ["Patron Deity", "Eternal Aspect", "Divine Emissary", "Humble Divinity", "Guardian God"]
            of_the += ["of the Sacred Duties", "of the Divine Oversight", "of the Eternal Watch", "of the Humble Domains", "of the Minor Wonders"]

        if npc.subrace == "Pegasus":
            descriptor += ["Winged", "Majestic", "Pure", "Graceful", "Skybound"]
            rank += ["Winged Steed", "Celestial Horse", "Sky Runner", "Majestic Flyer", "Cloud Dancer"]
            of_the += ["of the High Clouds", "of the Heavenly Winds", "of the Pure Skies", "of the Starry Heavens", "of the Celestial Gallop"]

        if npc.subrace == "Planetar":
            descriptor += ["Mighty", "Warrior", "Divine", "Radiant", "Just"]
            rank += ["Celestial Warrior", "Divine Champion", "Radiant Protector", "Just Arbiter", "Mighty Enforcer"]
            of_the += ["of the Celestial Armies", "of the Divine Crusade", "of the Radiant Order", "of the Just Cause", "of the Mighty Skies"]

        if npc.subrace == "Seraph":
            descriptor += ["Burning", "Highest", "Holy", "Radiant", "Six-Winged"]
            rank += ["Seraphim Guardian", "Flame of God", "Radiant Angel", "Holy Protector", "Divine Watcher"]
            of_the += ["of the Blazing Choirs", "of the Highest Heavens", "of the Holy Fires", "of the Radiant Spheres", "of the Divine Purity"]

        if npc.subrace == "Throne":
            descriptor += ["Judicial", "Imposing", "Celestial", "Majestic", "Orderly"]
            rank += ["Throne Arbiter", "Celestial Judge", "Divine Ruler", "Order Keeper", "Justice Bearer"]
            of_the += ["of the Celestial Courts", "of the Divine Order", "of the Judicious Spheres", "of the Majestic Rule", "of the Orderly Heavens"]

        if npc.subrace == "Unicorn":
            descriptor += ["Pure", "Mystical", "Enchanted", "Healing", "Gentle"]
            rank += ["Unicorn Guardian", "Mystic Steed", "Enchanted Being", "Healer of Forests", "Gentle Protector"]
            of_the += ["of the Enchanted Woods", "of the Healing Streams", "of the Mystic Glades", "of the Pure Hearts", "of the Gentle Wilds"]

        if "Celestial Serpent" in creature_type:
            descriptor += [
                "Green",
                "Celestial",
                "Stellar", "Majestic", "Cosmic", "Heavenly"]
            rank += ["Serpent",
                     "Stardrake", "Dragon", "Sky Serpent", "Majestic Coiler", "Heavenly Guardian"]
            of_the += ["of the Starry Heavens", "of the Cosmic Expanse", "of the Majestic Skies", "of the Stellar Realms", "of the Heavenly Bodies"]

        if npc.subrace == "Valkyrie":
            descriptor += ["Warrior", "Chooser", "Heroic", "Mighty", "Winged"]
            rank += ["Battle Maiden", "Slain Chooser", "Hero Escort", "Winged Warrior", "Valiant Guardian"]
            of_the += ["of the Slain Heroes", "of the Valhalla Halls", "of the Heroic Souls", "of the Mighty Deeds", "of the Warrior Spirits"]

        if npc.subrace == "Solar":
            descriptor += ["Exalted", "Powerful", "Heavenly", "Radiant", "Divine"]
            rank += ["Celestial Commander", "Divine Warrior", "Exalted Protector", "Radiant Emissary", "Heavenly Arbiter"]
            of_the += ["of the Highest Order", "of the Divine Armies", "of the Radiant Host", "of the Exalted Heavens", "of the Celestial Might"]

        if npc.subrace == "Ki-rin":
            descriptor += ["Wise", "Benevolent", "Mystical", "Auroral", "Celestial"]
            rank += ["Celestial Kirin", "Mystic Sage", "Divine Emissary", "Auroral Guardian", "Wisdom Bringer"]
            of_the += ["of the Celestial Harmony", "of the Mystic Winds", "of the Auroral Lights", "of the Heavenly Peace", "of the Benevolent Guidance"]

        if npc.subrace == "Deva":
            descriptor += ["Divine", "Ethereal", "Serene", "Virtuous", "Celestial"]
            rank += ["Deva Protector", "Divine Agent", "Ethereal Messenger", "Serene Guide", "Virtuous Emissary"]
            of_the += ["of the Celestial Realms", "of the Divine Order", "of the Ethereal Spheres", "of the Serene Heavens", "of the Virtuous Paths"]

        if npc.subrace == "Archon":
            descriptor += ["Just", "Lawful", "Heavenly", "Noble", "Guardian"]
            rank += ["Archon Judge", "Celestial Lawkeeper", "Heavenly Protector", "Noble Arbiter", "Guardian of Order"]
            of_the += ["of the Lawful Heavens", "of the Celestial Courts", "of the Just Order", "of the Noble Realms", "of the Heavenly Scales"]

        if npc.subrace == "Solar":
            descriptor += ["Exalted", "Powerful", "Heavenly", "Radiant", "Divine"]
            rank += ["Celestial Commander", "Divine Warrior", "Exalted Protector", "Radiant Emissary", "Heavenly Arbiter"]
            of_the += ["of the Highest Order", "of the Divine Armies", "of the Radiant Host", "of the Exalted Heavens", "of the Celestial Might"]

    if "Construct" in creature_type:
        descriptor += [
            "Amber",
            "Automated",
            "Artificial",
            "Artisan's",
            "Animated",
            "Crafted",
            "Design",
            "Mechanical",
            "Mechanized",
            "Sentient",
            "Constructed",
            "Crafted",
            "Sentient",
            "Yellow",
            "Golden",
            "Silver",
            "Bronce",
            "Iron",
            "Green",
            ]
        rank += [
            "Gargoyle",
            "Being", "Guardian", "Sentinel", "Machine", "Entity"]
        of_the += ["of the Crafted Realms", "of the Mechanized Worlds", "of the Constructs", "of the Automated Legions"]

        if npc.subrace == "Animated Armor":
            descriptor += ["Guardian", "Steelbound", "Empty Helm", "Armored", "Vigilant"]
            rank += ["Steel Sentinel", "Guardian Armor", "Helm Watcher", "Knight Protector", "Armored Guardian"]
            of_the += ["of the Ancient Halls", "of the Silent Watch", "of the Armored Guardians", "of the Forgotten Armory", "of the Eternal Vigil"]

        if npc.subrace == "Drone":
            descriptor += ["Aerial", "Scouting", "Unmanned", "Surveillance", "Mechanical"]
            rank += ["Sky Eye", "Recon Unit", "Aerial Scout", "Observation Sentinel", "Surveillance Machine"]
            of_the += ["of the Soaring Heights", "of the Scouting Skies", "of the Unseen Watchers", "of the Mechanical Wings", "of the Surveillance Network"]

        if "Golem" in creature_type:
            descriptor += [
                "Stone",
                "Earthen",
                "Mighty",
                "Constructed",
                "Elemental",
                "Silver",
                "Golden",
                "Clay",
                "Bone",
                "Flesh",
                "Ancient",
                ]
            rank += [
                "Gargoyle",
                "Golem",
                "Keeper",
                "Warrior",
                "Sentinel",
                "Guardian",
                "Construct"]
            of_the += [
                "of the Last Kingdom",
                "of the Ancient Ruins",
                "of the Ancient Earth",
                "of the Stony Bastions",
                "of the Earthen Cores",
                "of the Constructed Might",
                "of the Elemental Form"]

        if npc.subrace == "Homunculus":
            descriptor += ["Tiny", "Artificial", "Crafted", "Miniature", "Alchemical"]
            rank += ["Wrath", "Greed", "Lust", "Sloth", "Pride", "Envy", "Little Guardian", "Crafted Assistant", "Alchemical Being", "Tiny Sentinel", "Miniature Helper"]
            of_the += ["of the Alchemist's Lab", "of the Crafted Companions", "of the Miniature World", "of the Tiny Protectors", "of the Artificial Life"]

        if npc.subrace == "Flying Sword":
            descriptor += ["Enchanted", "Flying", "Sharp", "Airborne", "Swift"]
            rank += ["Sword Dancer", "Air Cutter", "Flying Blade", "Swift Rapier", "Enchanted Saber"]
            of_the += ["of the Dancing Steel", "of the Airborne Assault", "of the Swift Strikes", "of the Enchanted Edge", "of the Flying Arsenal"]

        if npc.subrace == "Living Furniture":
            descriptor += ["Animated", "Furnish", "Lively", "Enchanted", "Wooden"]
            rank += ["Moving Chair", "Walking Table", "Animated Carpet", "Enchanted Wardrobe", "Living Decor"]
            of_the += ["of the Enchanted Chambers", "of the Living Rooms", "of the Moving Households", "of the Animated Abodes", "of the Lively Quarters"]

        if npc.subrace == "Scarecrow":
            descriptor += ["Straw-Filled", "Guardian", "Sinister", "Field-Watcher", "Scary"]
            rank += ["Field Sentinel", "Snowman", "Straw Guardian", "Crop Protector", "Sinister Scarecrow", "Watcher of the Fields"]
            of_the += ["of the Corn Rows", "of the Scarecrow Guards", "of the Sinister Fields", "of the Watchful Eyes", "of the Harvest Guardians"]

        if npc.subrace == "Clockwork Construct":
            descriptor += ["Clockwork", "Mechanical", "Intricate", "Steampunk", "Gear-Driven"]
            rank += ["Gear Artisan", "Clockwork Warrior", "Mechanical Marvel", "Intricate Automaton", "Steampunk Sentinel"]
            of_the += ["of the Gearworks", "of the Clockwork Mechanisms", "of the Mechanical Wonders", "of the Intricate Craft", "of the Steampunk Realms"]

        if npc.subrace == "Warforged":
            descriptor += ["Battle-Born", "Warrior", "Forged", "Sturdy", "Sentient"]
            rank += ["War Machine", "Forged Fighter", "Battle Construct", "Steel Warrior", "Sentient Armor"]
            of_the += ["of the War Forges", "of the Battlefields", "of the Forged Legions", "of the Steel Clans", "of the Sentient Brigade"]

        if npc.subrace == "Modron":
            descriptor += ["Geometric", "Orderly", "Mechanical", "Systematic", "Logical"]
            rank += ["Geometric Keeper", "Modron Monitor", "Mechanical Regulator", "Systematic Overseer", "Logical Coordinator"]
            of_the += ["of the Geometric Spheres", "of the Orderly Matrix", "of the Mechanical Planes", "of the Systematic Order", "of the Logical Constructs"]

        if npc.subrace == "Shield Guardian":
            descriptor += ["Protective", "Stalwart", "Bound", "Vigilant", "Armored"]
            rank += ["Guardian Defender", "Amulet Warden", "Stalwart Protector", "Bound Sentinel", "Armored Watcher"]
            of_the += ["of the Shielded Realms", "of the Amulet's Bond", "of the Stalwart Guards", "of the Bound Duties", "of the Protective Arms"]

        if npc.subrace == "Tome Guardian":
            descriptor += [
                "Literate", "Scholarly", "Guardian", "Inscribed", "Wise"]
            rank += [
                "Gargoyle","Book Keeper", "Scholarly Protector", "Tome Sentinel", "Scripted Guardian", "Wise Custodian"]
            of_the += ["of the Ancient Libraries", "of the Scholarly Archives", "of the Inscribed Wisdom", "of the Guardian Scrolls", "of the Learned Repositories"]

        if "Effigy" in creature_type:
            descriptor += [
                "Ritualistic", "Statuesque", "Symbolic", "Mystical", "Ethereal"]
            rank += [
                "Gargoyle",
                "Angel", "Ritual Guardian", "Statue Warden", "Symbolic Protector", "Mystic Effigy", "Ethereal Sentinel"]
            of_the += ["of the Ritual Circles", "of the Statuesque Realms", "of the Symbolic Grounds", "of the Mystic Rites", "of the Ethereal Forms"]

    if "Dragon" in creature_type:
        descriptor += [
            "Draconic",
            "Majestic",
            "Ancient",
            "Scales",
            "Winged",
            "Breathing",
            "Flame",
            "Eternal",
            "Sky",
            "Fire"]
        rank += ["Sovereign",
                 "Ruler",
                 "Keeper",
                 "Dominator",
                 "Drake",
                "Fang",
                "Sovereign",
                "Wing",
                "Scale"]
        of_the += [
            "of the {random.choice(rank)}",
            f"of the {random.choice(descriptor)} Realms",
            f"of the {random.choice(descriptor)} Sky",
            f"of the {random.choice(descriptor)} Peaks",
            ]

        if "Dragonborn" in npc.subrace:
            descriptor += ["Draconic", "Scaled", "Proud", "Noble", "Fire-Blooded"]
            rank += ["Dragonborn Chieftain", "Scaled Guardian", "Draconic Warrior", "Proud Scion", "Noble Drake"]
            of_the += ["of the Dragon Clans", "of the Scaled Tribes", "of the Draconic Lineage", "of the Noble Wings", "of the Fire-Breathers"]

        if "Wyrmling" in npc.subrace:
            descriptor += ["Newborn", "Tiny", "Playful", "Curious", "Hatchling"]
            rank += ["Little Wyrm", "Dragon Child", "Hatchling Scout", "Tiny Flame", "Playful Drake"]
            of_the += ["of the Dragon Nursery", "of the Hatchling's Nest", "of the Wyrm Gardens", "of the Newborn Skies", "of the Curious Ones"]

        if "Young Dragon" in npc.subrace:
            descriptor += ["Adolescent", "Growing", "Eager", "Brash", "Youngling"]
            rank += ["Dragon Apprentice", "Young Wyrm", "Eager Flyer", "Brash Firebrand", "Growing Drake"]
            of_the += ["of the Soaring Heights", "of the Growing Prowess", "of the Young Realms", "of the Eager Flames", "of the Adolescent Roost"]

        if "Dragon" in npc.subrace:
            descriptor += ["Mature", "Powerful", "Winged", "Ancient", "Sovereign"]
            rank += ["Dragon Lord", "Winged Monarch", "Flame Master", "Ancient Drake", "Sovereign Wyrm"]
            of_the += ["of the Eternal Flames", "of the Winged Dominance", "of the Ancient Skies", "of the Sovereign Peaks", "of the Dragon Realms"]

        if "Drake" in npc.subrace:
            descriptor += ["Lesser", "Fierce", "Agile", "Sleek", "Vigorous"]
            rank += ["Drake Hunter", "Fierce Flyer", "Agile Predator", "Sleek Guardian", "Vigorous Wyrm"]
            of_the += ["of the Wild Jungles", "of the Mountain Lairs", "of the Swift Winds", "of the Fierce Cliffs", "of the Vigorous Hunts"]

        if "Draco" in npc.subrace:
            descriptor += ["Scaled", "Winged", "Stoic", "Noble", "Resilient"]
            rank += ["Draco Guardian", "Scaled Protector", "Winged Warrior", "Stoic Defender", "Noble Dragon"]
            of_the += ["of the Stoic Mountains", "of the Scaled Fortresses", "of the Winged Patrols", "of the Noble Realms", "of the Resilient Spirits"]

        if "Sky Serpent" in npc.subrace:
            descriptor += ["Ethereal", "Skybound", "Mystical", "Serpentine", "Cloud Roamer"]
            rank += ["Celestial Serpent", "Ethereal Drake", "Mystic Wyrm", "Sky Coiler", "Cloud Dancer"]
            of_the += ["of the Mystic Skies", "of the Cloud Realms", "of the Ethereal Winds", "of the Serpentine Heavens", "of the Roaming Vapors"]

        if "Half Dragon" in npc.subrace:
            descriptor += ["Hybrid", "Half-Scaled", "Draconic", "Fire-Touched", "Mystical"]
            rank += ["Dragonkin", "Hybrid Guardian", "Half-Wyrm", "Draconic Scion", "Mystic Drake"]
            of_the += ["of the Hybrid Clans", "of the Draconic Blood", "of the Fire-Touched Lineage", "of the Mystical Scales", "of the Half-Blood Realms"]

        if "Dragon Turtle" in npc.subrace:
            descriptor += ["Ancient", "Sea-Bound", "Colossal", "Revered", "Armored"]
            rank += ["Ocean Guardian", "Colossal Leviathan", "Revered Elder", "Armored Behemoth", "Sea Dragon"]
            of_the += ["of the Deep Oceans", "of the Colossal Depths", "of the Revered Seas", "of the Armored Shores", "of the Ancient Waves"]
        if "Black" in npc.subrace:
            descriptor += ["Acidic", "Dark-Scaled", "Malevolent", "Swamp Dweller", "Corrosive"]
            rank += ["Acid Lord", "Swamp Sovereign", "Dark Drake", "Corrosive Wyrm", "Malevolent Serpent"]
            of_the += ["of the Poisoned Marshes", "of the Dark Swamps", "of the Acidic Mists", "of the Corrosive Lairs", "of the Malevolent Depths"]
        if "Blue" in npc.subrace:
            descriptor += ["Electric", "Stormcaller", "Skybound", "Lightning-Wielder", "Thunderous"]
            rank += ["Storm Dragon", "Lightning Tyrant", "Sky Sovereign", "Thunder Drake", "Electric Serpent"]
            of_the += ["of the Thundering Skies", "of the Lightning Storms", "of the Electric Peaks", "of the Stormcaller Realms", "of the Skybound Dominance"]
        if "Green" in creature_type:
            descriptor += [
                "Green",
                "Poisonous", "Verdant", "Deceptive", "Forest",  "Toxic"]
            rank += [
                "Dweller",
                "Poison Master", "Verdant Guardian", "Deceptive Wyrm", "Forest Sovereign", "Toxic Overlord"]
            of_the += ["of the Poisoned Woods", "of the Verdant Jungles", "of the Deceptive Groves", "of the Toxic Thickets", "of the Forest Dominions"]
        if "Red" in creature_type:
            descriptor += [
                "Red",
                "Magenta",
                "Fiery",
                "Infernal",
                "Terrifying",
                "Mountain",
                "Flame-Breather",
                "Fire",
                "Blazing",
                "Blaze",
                ]
            rank += [
                "Firelord",
                "Tyrant",
                "Sovereign",
                "King",
                "Ruler",
                "Master",
                ]
            of_the += ["of the Burning Mountains", "of the Infernal Depths", "of the Fiery Realms", "of the Terrifying Peaks", "of the Flame-Enveloped Lairs"]
        if "White" in npc.subrace:
            descriptor += ["Frosty", "Icy", "Arctic", "Cold-Breather", "Glacial"]
            rank += ["Ice Monarch", "Frost Sovereign", "Arctic Tyrant", "Glacial Ruler", "Cold Drake"]
            of_the += ["of the Frozen Wastes", "of the Icy Peaks", "of the Arctic Realms", "of the Glacial Caverns", "of the Frostbound Lairs"]
        if "Bronze" in npc.subrace:
            descriptor += ["Noble", "Lightning", "Sea-Bound", "Bronze-Scaled", "Stormwing"]
            rank += ["Bronze Protector", "Storm Dragon", "Sea Guardian", "Lightning Wielder", "Noble Drake"]
            of_the += ["of the Coastal Shores", "of the Stormy Seas", "of the Bronze Cliffs", "of the Lightning Skies", "of the Noble Waves"]
        if "Silver" in npc.subrace:
            descriptor += ["Graceful", "Icy", "Paralyzing", "Silver-Scaled", "Wise"]
            rank += ["Silver Sage", "Frost Guardian", "Graceful Sovereign", "Paralyzing Drake", "Wise Serpent"]
            of_the += ["of the Icy Peaks", "of the Silver Realms", "of the Graceful Skies", "of the Paralyzing Breath", "of the Wise Dominions"]
        if "Gold" in creature_type:
            descriptor += [
                "Amber",
                "Regal",
                "Golden",
                "Unweavering",
                "Gold",
                "Venerable",
                "Fire"]
            rank += [
                "Scale",
                "Sovereign",
                "Protector",
                "Master",
                "Flame"
                ]
            of_the += [
                "of the Golden Hoards",
                "of the Hoard",
                f"of the {random.choice(descriptor)} Hoards",
                "of the Peaks",
                "of the Throne",
                "of the Flames",
                f"of the {random.choice(descriptor)} Realms"]
        if "Brass" in npc.subrace:
            descriptor += ["Sociable", "Fiery", "Sleep-Inducer", "Brass-Scaled", "Desert Dweller"]
            rank += ["Brass Diplomat", "Desert Guardian", "Fire Talker", "Sleep Master", "Sociable Drake"]
            of_the += ["of the Scorching Deserts", "of the Brass Sands", "of the Fiery Conversations", "of the Sleep-Inducing Winds", "of the Sociable Tribes"]
        if "Copper" in npc.subrace:
            descriptor += ["Witty", "Acidic", "Slowing", "Copper-Scaled", "Clever"]
            rank += ["Copper Trickster", "Acid Spitter", "Witty Drake", "Clever Guardian", "Slowing Wyrm"]
            of_the += ["of the Rocky Highlands", "of the Copper Caverns", "of the Acidic Springs", "of the Clever Minds", "of the Slowing Mists"]
        if "Shadow" in npc.subrace:
            descriptor += ["Shadowy", "Tenebrous", "Necrotic", "Ethereal", "Sinister"]
            rank += ["Shadow Sovereign", "Tenebrous Tyrant", "Necrotic Drake", "Ethereal Serpent", "Sinister Wyrm"]
            of_the += ["of the Shadowfell", "of the Tenebrous Depths", "of the Necrotic Realms", "of the Ethereal Shadows", "of the Sinister Dominions"]
        if "Gem" in npc.subrace:
            descriptor += ["Radiant", "Gemstone", "Psionic", "Lustrous", "Rare"]
            rank += ["Gem Guardian", "Radiant Serpent", "Psionic Wyrm", "Lustrous Drake", "Rare Sovereign"]
            of_the += ["of the Crystal Caverns", "of the Gemstone Mountains", "of the Psionic Spheres", "of the Lustrous Depths", "of the Rare Jewels"]
        if "Ethereal" in creature_type:
            descriptor += [
                "Astral",
                "Ethereal",
                "Ghostly",
                "Translucent",
                "Otherworldly"
                ]
            rank += [
                "",
                ]
            of_the += [
                "of the Ethereal Planes",
                "of the Astral Realms",
                "of the Veil",
                "of the Otherworld",
                ]
        if "Planar" in npc.subrace:
            descriptor += ["Planar", "Dimensional", "Traveler", "Cosmic", "Boundary-Crosser"]
            rank += ["Planar Wanderer", "Dimensional Guardian", "Cosmic Drake", "Traveler of Realms", "Boundary Sentinel"]
            of_the += ["of the Multiverse", "of the Planar Gateways", "of the Cosmic Expanse", "of the Dimensional Crossroads", "of the Boundary Edges"]
        if "Prismatic" in npc.subrace:
            descriptor += ["Prismatic", "Rainbow-Scaled", "Spectrum", "Luminous", "Chromatic"]
            rank += ["Prismatic Sovereign", "Rainbow Serpent", "Spectrum Drake", "Luminous Wyrm", "Chromatic Guardian"]
            of_the += ["of the Rainbow Veil", "of the Prismatic Scales", "of the Spectrum Light", "of the Luminous Realms", "of the Chromatic Radiance"]

    # Elemental Race and Subraces
    if "Elemental" in npc.race:
        # General Elemental descriptor, rank, and Of_the Phrases
        descriptor += [
            "Primal",
            "Elemental",
            "Natural",
            "Valance",
            "Ethereal"]
        rank += [
            "Guardian",
            "Force",
            "Spirit",
            "Warden",
            ]
        of_the += [
            "of Nature",
            "of the Elements",
            "of the Ethereal Realms",
            "of the Natural World",
            "of the Forces",
            "of Primal Essence"]

        # Atlantian
        if "Atlantian" in npc.subrace:
            descriptor += ["Aquatic", "Ancient", "Deepsea", "Nautical", "Technologic"]
            rank += ["Ocean Sovereign", "Deepsea Guardian", "Ancient Mariner", "Wave Master", "Sea Technologist"]
            of_the += ["of the Sunken Cities", "of the Deep Oceans", "of the Ancient Technologies", "of the Maritime Depths", "of the Oceanic Ruins"]

        # Cronusian
        if "Cronusian" in npc.subrace:
            descriptor += ["Timeless", "Aged", "Eternal", "Hourglass", "Chronal"]
            rank += ["Time Keeper", "Ageless Sage", "Eternal Watcher", "Hourglass Guardian", "Chronal Master"]
            of_the += ["of the Ageless Times", "of the Eternal Moments", "of the Time Streams", "of the Chronal Sands", "of the Hourglass Realms"]

        # Eosian
        if "Eosian" in npc.subrace:
            descriptor += [
                "Ethereal",
                "Dawnbringer", "Luminous", "Sunrise", "Solar", "Daylight"]
            rank += ["Sunrise Sovereign", "Luminous Guardian", "Dawn Herald", "Solar Emissary", "Daylight Keeper"]
            of_the += ["of the First Light", "of the Rising Sun", "of the Morning Rays", "of the Solar Brilliance", "of the Luminous Horizons"]

        # Genasi
        if "Genasi" in npc.subrace:
            descriptor += [
                "Elementalborn",
                "Primal",
                "Versatile", "Mystical", "Nature's Child"]
            rank += ["Primal Force", "Elemental Sage", "Nature's Herald", "Mystic Shaper", "Versatile Guardian"]
            of_the += ["of the Four Elements", "of the Mystical Forces", "of the Primal Essence", "of the Nature's Wonders", "of the Elemental Realms"]

        # Genie
        if "Genie" in npc.subrace:
            descriptor += ["Primordial", "Mystical", "Powerful", "Enigmatic", "Wishmaker"]
            rank += ["Genie Lord", "Primordial Spirit", "Mystical Sovereign", "Enigmatic Master", "Wish Granter"]
            of_the += ["of the Ancient Wishes", "of the Mystic Realms", "of the Primordial Sands", "of the Enigmatic Powers", "of the Wishful Dominions"]

        # Gaians
        if "Gaians" in creature_type:
            descriptor += [
                "Green",
                "Earthen", "Stoneheart", "Terran", "Nature's Essence", "Grounded"]
            rank += [
                "Gargoyle",
                "Earth Sage", "Stoneheart Guardian", "Terran Protector", "Nature's Essence", "Grounded Ruler"]
            of_the += ["of the Deep Earth", "of the Stoneheart Mountains", "of the Terran Realms", "of the Nature's Core", "of the Grounded Lands"]

        # Hyperian
        if "Hyperian" in npc.subrace:
            descriptor += ["Solar", "Radiant", "Sunfire", "Illuminated", "Lightbringer"]
            rank += ["Solar Guardian", "Radiant Sovereign", "Sunfire Master", "Illuminated Emissary", "Lightbringer"]
            of_the += ["of the Solar Flames", "of the Radiant Skies", "of the Sunfire Realms", "of the Illuminated Heavens", "of the Lightbringer's Domain"]

        # Oceanians
        if "Oceanians" in npc.subrace:
            descriptor += ["Tidal", "Marine", "Abyssal", "Stormcaller", "Oceanic"]
            rank += ["Tide Master", "Marine Sovereign", "Abyssal Guardian", "Stormcaller", "Oceanic Ruler"]
            of_the += ["of the Tidal Forces", "of the Marine Depths", "of the Abyssal Waters", "of the Stormy Seas", "of the Oceanic Expanse"]

        # Primordial
        if "Primordial" in npc.subrace:
            descriptor += ["Fundamental", "Origin", "Elemental", "Primeval", "Core"]
            rank += ["Fundamental Force", "Origin Keeper", "Elemental Sage", "Primeval Guardian", "Core Spirit"]
            of_the += ["of the Elemental Origins", "of the Fundamental Forces", "of the Primeval Essence", "of the Core Elements", "of the Origin Realms"]

        # Promethean
        if "Promethean" in creature_type:
            descriptor += [
                "Promethean"
                "Amber",
                "Ambaric",
                "Red",
                "Innovative",
                "Fiery",
                "Energetic",
                "Dynamic",
                "Electrifying",
                "Electric"
                "Energy",
                "Fire"]
            rank += [
                "Innovator",
                "Creator",
                "Shaper",
                "Spirit",
                "Promethus"]
            of_the += [
                "of the Fires",
                "of the Fire",
                f"of the {random.choice(descriptor)} Fire",
                "of Energy",
                "of the Storms",
                "of Innovation",
                ]

        # Salamandrian
        if "Salamandrian" in npc.subrace:
            descriptor += [
                "Amber",
                "Flameborn",
                "Blazing",
                "Inferno",
                "Ember",
                "Flame",
                "Fire"]
            rank += [
                "Guardian",
                "Spirit",
                "Master",
                "Soul",
                "Warden",
                "Blaze",
                ]
            of_the += [
                "of the Burning Heart",
                "of Fireborne Essence"]

        # Titan
        if "Titan" in creature_type:
            descriptor += [
                "Colossal",
                "Powerful",
                "Elemental",
                "Mighty",
                "Unyielding",
                "Red",
                ]
            rank += [
                "Colossus",
                "Behemoth",
                "Titan",
                "Sovereign",
                "Force"]
            of_the += [
                "of the Colossal Strength",
                "of the Elemental Might",
                "of the Mighty Peaks",
                "of the Power Unleashed",
                "of the Unyielding Earth"]

        # Uranians
        if "Uranians" in npc.subrace:
            descriptor += [
                "Ethereal",
                "Stellar", "Celestial", "Skybound", "Astral", "Starlight"]
            rank += ["Celestial Wanderer", "Stellar Guardian", "Sky Sovereign", "Astral Keeper", "Starlight Emissary"]
            of_the += ["of the Starry Heavens", "of the Celestial Orbs", "of the Astral Realms", "of the Skybound Dominions", "of the Stellar Depths"]

        # Magmaforged
        if "Magmaforged" in npc.subrace:
            descriptor += [
                "Red",
                "Lava", "Volcanic", "Igneous", "Molten", "Fiery Earth"]
            rank += ["Lava Creator", "Volcanic Force", "Igneous Guardian", "Molten Shaper", "Fiery Earth Ruler"]
            of_the += ["of the Lava Flows", "of the Volcanic Mountains", "of the Igneous Formations", "of the Molten Depths", "of the Fiery Earth"]

        # Zephyrian
        if "Zephyrian" in npc.subrace:
            descriptor += ["Gentle Breeze", "Airy", "Zephyr", "Windborn", "Soft Gust"]
            rank += ["Breeze Keeper", "Airy Spirit", "Zephyr Warden", "Windborn Leader", "Gentle Gust Guardian"]
            of_the += ["of the Gentle Winds", "of the Airy Heights", "of the Zephyr Valleys", "of the Windborn Realms", "of the Soft Gusts"]

        # Tartarian
        if "Tartarian" in npc.subrace:
            descriptor += ["Deepsea", "Darkwater", "Abyssal", "Oceanic", "Tidal"]
            rank += ["Deepsea Sovereign", "Darkwater Guardian", "Abyssal Protector", "Oceanic Force", "Tidal Master"]
            of_the += ["of the Deep Ocean", "of the Dark Waters", "of the Abyssal Trenches", "of the Oceanic Realms", "of the Tidal Waves"]

        # Etherian
        if "Etherian" in npc.subrace:
            descriptor += ["Ethereal", "Luminous", "Heavenly", "Celestial", "Stardust"]
            rank += ["Ethereal Spirit", "Luminous Guardian", "Heavenly Force", "Celestial Wanderer", "Stardust Weaver"]
            of_the += ["of the Ethereal Skies", "of the Luminous Expanse", "of the Heavenly Spheres", "of the Celestial Lights", "of the Stardust Clouds"]

        # Galaxian
        if "Galaxian" in npc.subrace:
            descriptor += ["Starry", "Galactic", "Cosmic", "Astral", "Spaceborne"]
            rank += ["Galactic Sovereign", "Cosmic Voyager", "Starry Guardian", "Astral Force", "Spaceborne Entity"]
            of_the += ["of the Starry Expanse", "of the Galactic Cores", "of the Cosmic Frontiers", "of the Astral Planes", "of the Spaceborne Nebulae"]

        # Chronian
        if "Chronian" in creature_type:
            descriptor += [
                "Timeless",
                "Chronal",
                "Temporal",
                "Eon",
                "Hourglass",
                "Time"]
            rank += [
                "Oracle",
                "Keeper",
                "Warden",
                "Guardian",
                "Master",
                "Sentinel"]
            of_the += [
                "of the Streams",
                "of the Rifts",
                "of the Vortex",
                "of the Depths",
                "of the Sands of Time",
                "of Time",
                ]

        # Tundran
        if "Tundran" in npc.subrace:
            descriptor += ["Icy", "Frozen", "Glacial", "Arctic", "Snowbound"]
            rank += ["Glacial Master", "Frozen Sovereign", "Icy Protector", "Arctic Force", "Snowbound Guardian"]
            of_the += ["of the Frozen Wastes", "of the Glacial Peaks", "of the Icy Realms", "of the Arctic Expanse", "of the Snowbound Lands"]

    # Fiend Race and Subraces
    if "Fiend" in creature_type:
        # General Fiend descriptor, rank, and Of_the Phrases
        descriptor += [
            "Red",
            "Infernal",
            "Hell",
            "Diabolical",
            "Sinister",
            "Malevolent",
            "Demonic",
            "Demon",
            "Fiendish",
            "Dark",
            ]
        rank += [
            "Sabertooth",
            "Lord",
            "Prince",
            "Sovereign",
            "Commander",
            "Deceiver"]
        of_the += [
            f"of the {random.choice(descriptor)} Realms",
            "of the Abyssal Depths",
            f"of the {random.choice(descriptor)} Schemes",
            f"of the {random.choice(descriptor)} Plans",
            f"of the {random.choice(descriptor)} Hordes",
            f"of the {random.choice(descriptor)} Deal",
            f"of the {random.choice(descriptor)} Pact",
            ]

        # Specific Subclass Conditions
        if "Tiefling" in npc.subrace:
            descriptor += ["Horned", "Mischievous", "Half-Infernal", "Charismatic", "Dark-Touched"]
            rank += ["Infernal Scion", "Horned Trickster", "Dark Wanderer", "Fiendish Diplomat", "Charismatic Outcast"]
            of_the += ["of the Half-Bloods", "of the Mischievous Spirits", "of the Infernal Ancestry", "of the Darkened Paths", "of the Charismatic Deceit"]

        if "Devil" in npc.subrace:
            descriptor += ["Lawful", "Malefic", "Tempter", "Scheming", "Calculating"]
            rank += ["Archdevil", "Pit Fiend", "Infernal Judge", "Contract Maker", "Scheming Ruler"]
            of_the += ["of the Nine Hells", "of the Infernal Courts", "of the Diabolical Pacts", "of the Scheming Depths", "of the Calculating Minds"]

        if "Demon" in npc.subrace:
            descriptor += ["Chaotic", "Raging", "Savage", "Feral", "Unpredictable"]
            rank += ["Demon Lord", "Abyssal Ruler", "Chaos Bringer", "Savage Destroyer", "Feral Beast"]
            of_the += ["of the Abyssal Layers", "of the Chaotic Maelstrom", "of the Savage Fury", "of the Feral Wilderness", "of the Unpredictable Madness"]

        if "Imp" in npc.subrace:
            descriptor += ["Tiny", "Tricky", "Sly", "Mischevious", "Winged"]
            rank += ["Impish Spy", "Tiny Trickster", "Sly Messenger", "Winged Infiltrator", "Mischevious Agent"]
            of_the += ["of the Hidden Realms", "of the Sly Escapades", "of the Impish Games", "of the Winged Shadows", "of the Mischevious Plots"]

        if "cubus" in creature_type:
            descriptor += [
                "Magenta",
                "Seductive",
                "Charming",
                "Enchanting",
                "Tempting",
                "Deceptive"]
            rank += ["Seducer", "Fiend", "Spirit", "Temptress", "Charmer"]
            of_the += ["of the Seductive Powers", "of the Charming Spells", "of the Enchanting Eyes", "of the Tempting Whispers", "of the Deceptive Guises"]
        # Incubus
        if "Incubus" in npc.subrace:
            descriptor += ["Seductive", "Charming", "Tempting", "Manipulative", "Alluring"]
            rank += ["Master Tempter", "Dark Seducer", "Charming Fiend", "Deceptive Lover", "Enthralling Demon"]
            of_the += ["of the Bewitching Charm", "of the Seductive Shadows", "of the Tempting Darkness", "of the Manipulative Arts", "of the Alluring Night"]

        # Succubus
        if "Succubus" in npc.subrace:
            descriptor += ["Enchanting", "Alluring", "Seductress", "Deceptive", "Charmweaver"]
            rank += ["Enchantress", "Alluring Fiend", "Seductress of the Night", "Charmweaver", "Deceptive Beauty"]
            of_the += ["of the Enchanted Hearts", "of the Alluring Abyss", "of the Night's Seduction", "of the Deceptive Charm", "of the Bewitching Spells"]

        # Concubus
        if "Concubus" in npc.subrace:
            descriptor += ["Mystical", "Entrancing", "Exotic", "Charmcaster", "Hypnotic"]
            rank += ["Mystic Tempter", "Entrancing Demon", "Exotic Enchanter", "Charmcaster Fiend", "Hypnotic Seducer"]
            of_the += ["of the Exotic Illusions", "of the Entrancing Realms", "of the Mystical Charms", "of the Hypnotic Gazes", "of the Charmcaster's Domain"]

        # Dwarvendevil
        if "Dwarvendevil" in npc.subrace:
            descriptor += ["Stout", "Infernal", "Crafty", "Fiery", "Rugged"]
            rank += ["Infernal Forgemaster", "Fiery Warrior", "Stout Fiend", "Crafty Underminer", "Rugged Overlord"]
            of_the += ["of the Infernal Forges", "of the Fiery Depths", "of the Rugged Mountains", "of the Crafty Lairs", "of the Stout Legions"]

        # Elvendevil
        if "Elvendevil" in npc.subrace:
            descriptor += ["Elegant", "Malevolent", "Deceiver", "Sinister", "Twisted"]
            rank += ["Sinister Enchanter", "Elegant Fiend", "Malevolent Trickster", "Twisted Aristocrat", "Deceiver of the Woods"]
            of_the += ["of the Enchanted Forests", "of the Elegant Courts", "of the Malevolent Schemes", "of the Twisted Paths", "of the Sinister Glades"]

        # Gnolldevil
        if "Gnolldevil" in npc.subrace:
            descriptor += ["Savage", "Infernal", "Hyena-Like", "Ruthless", "Feral"]
            rank += ["Infernal Pack Leader", "Savage Fiend", "Hyena Demon", "Ruthless Predator", "Feral Overseer"]
            of_the += ["of the Infernal Wastelands", "of the Savage Realms", "of the Hyena Packs", "of the Ruthless Hunts", "of the Feral Dominions"]

        # Orkishdevil
        if "Orkishdevil" in npc.subrace:
            descriptor += ["Brutish", "Warlike", "Fierce", "Infernal", "Raging"]
            rank += ["Infernal Warlord", "Brutish Fiend", "Fierce Marauder", "Warlike Overlord", "Raging Demon"]
            of_the += ["of the War Torn Lands", "of the Infernal Battles", "of the Brutish Clans", "of the Fierce Wars", "of the Raging Storms"]

        # Goblindevil
        if "Goblindevil" in npc.subrace:
            descriptor += ["Tricky", "Mischievous", "Malevolent", "Cunning", "Dark"]
            rank += ["Dark Trickster", "Mischievous Fiend", "Cunning Goblin", "Malevolent Schemer", "Tricky Deceiver"]
            of_the += ["of the Dark Caverns", "of the Mischievous Shadows", "of the Cunning Plans", "of the Malevolent Deeds", "of the Tricky Mischief"]

        # Dwarvendemon
        if "Dwarvendemon" in npc.subrace:
            descriptor += ["Corrupted", "Demonic", "Rugged", "Malefic", "Twisted"]
            rank += ["Corrupted Forge Lord", "Demonic Warrior", "Rugged Fiend", "Malefic Smith", "Twisted Miner"]
            of_the += ["of the Corrupted Depths", "of the Demonic Forges", "of the Rugged Mountains", "of the Malefic Caverns", "of the Twisted Mines"]

        # Elvendemon
        if "Elvendemon" in npc.subrace:
            descriptor += ["Enchanted", "Dark", "Sinister", "Malefic", "Corrupted"]
            rank += ["Dark Enchanter", "Sinister Hunter", "Malefic Sorcerer", "Corrupted Noble", "Enchanted Fiend"]
            of_the += ["of the Dark Woods", "of the Sinister Glades", "of the Malefic Spells", "of the Corrupted Courts", "of the Enchanted Shadows"]

        # Demongnoll
        if "Demongnoll" in npc.subrace:
            descriptor += ["Savage", "Demonic", "Ravenous", "Chaotic", "Fierce"]
            rank += ["Savage Overlord", "Demonic Pack Leader", "Ravenous Fiend", "Chaotic Marauder", "Fierce Hunter"]
            of_the += ["of the Savage Wastes", "of the Demonic Packs", "of the Ravenous Deserts", "of the Chaotic Wilderness", "of the Fierce Battles"]

        # Orkishdemon
        if "Orkishdemon" in npc.subrace:
            descriptor += ["Brutal", "Demonic", "War-Torn", "Ruthless", "Ferocious"]
            rank += ["Brutal Warlord", "Demonic Chieftain", "War-Torn Fiend", "Ruthless Commander", "Ferocious Brute"]
            of_the += ["of the Brutal Wars", "of the Demonic Clans", "of the War-Torn Realms", "of the Ruthless Raids", "of the Ferocious Assaults"]

        # Goblindemon
        if "Goblindemon" in npc.subrace:
            descriptor += ["Cunning", "Demonic", "Sly", "Mischievous", "Devious"]
            rank += ["Cunning Fiend", "Demonic Trickster", "Sly Imp", "Mischievous Goblin", "Devious Saboteur"]
            of_the += ["of the Cunning Ambushes", "of the Demonic Mischief", "of the Sly Escapes", "of the Mischievous Raids", "of the Devious Plots"]

        # Nightmare
        if "Nightmare" in npc.subrace:
            descriptor += ["Terrifying", "Ethereal", "Shadowy", "Fear-Inducing", "Dark"]
            rank += ["Shadow Steed", "Terrifying Specter", "Ethereal Horror", "Fear-Inducer", "Dark Phantom"]
            of_the += ["of the Nightmare Realms", "of the Ethereal Shadows", "of the Terrifying Dreams", "of the Dark Fears", "of the Shadowy Abyss"]

        # Rakshasa
        if "Rakshasa" in creature_type:
            descriptor += [
                "Sabertooth",
                "Deceptive",
                "Cunning",
                "Malevolent",
                "Illusionist",
                "Manipulative"
                ]
            rank += [
                "Sabertooth",
                "Master",
                "Fiend",
                "Deceiver",
                "Trickster",
                "Demon"]
            of_the += [
                "of the Thousand Guises",
                "of the Cunning Illusions",
                "of the Malevolent Schemes",
                "of the Illusionist Arts",
                "of the Manipulative Ploys"]

        # Fallen Angel
        if "Fallen Angel" in npc.subrace:
            descriptor += [
                "Ethereal",
                "Fallen",
                "Darkened",
                "Lost",
                "Banished",
                "Corrupted"]
            rank += ["Seraph", "Messenger", "Cherub", "Guardian", "Emissary"]
            of_the += ["of the Fallen Heavens", "of the Darkened Skies", "of the Lost Grace", "of the Banished Realms", "of the Corrupted Wings"]

        # Hellbound Hunter
        if "Hellbound Hunter" in npc.subrace:
            descriptor += ["Relentless", "Infernal", "Tracker", "Merciless", "Dark"]
            rank += ["Infernal Tracker", "Relentless Pursuer", "Dark Stalker", "Merciless Hunter", "Hellbound Seeker"]
            of_the += ["of the Endless Hunt", "of the Infernal Trails", "of the Dark Pursuits", "of the Merciless Chases", "of the Hellbound Paths"]

        # Leviathan
        if "Leviathan" in npc.subrace:
            descriptor += ["Monstrous", "Oceanic", "Colossal", "Abyssal", "Dreaded"]
            rank += ["Ocean Terror", "Colossal Sea Beast", "Abyssal Monster", "Dreaded Leviathan", "Monstrous Predator"]
            of_the += ["of the Deep Seas", "of the Colossal Depths", "of the Abyssal Waters", "of the Dreaded Tides", "of the Monstrous Waves"]

        # Behemoth
        if "Behemoth" in npc.subrace:
            descriptor += ["Massive", "Powerful", "Terrifying", "Untamed", "Monstrous"]
            rank += ["Mighty Behemoth", "Terrifying Colossus", "Untamed Giant", "Powerful Titan", "Monstrous Behemoth"]
            of_the += ["of the Wild Lands", "of the Terrifying Strength", "of the Untamed Realms", "of the Powerful Roars", "of the Monstrous Dominions"]

        # Shinigami
        if "Shinigami" in npc.subrace:
            descriptor += ["Deathly", "Spectral", "Soul Reaper", "Ethereal", "Dark"]
            rank += ["Soul Collector", "Deathly Harbinger", "Ethereal Reaper", "Spectral Judge", "Dark Shinigami"]
            of_the += ["of the Departed Souls", "of the Ethereal Veil", "of the Deathly Missions", "of the Spectral Realms", "of the Dark Rites"]

        # Hell's Rider
        if "Hell's Rider" in npc.subrace:
            descriptor += ["Infernal", "Relentless", "Fiery", "Riding", "Fearsome"]
            rank += ["Infernal Rider", "Fiery Horseman", "Relentless Pursuer", "Fearsome Cavalier", "Hellbound Rider"]
            of_the += ["of the Blazing Trails", "of the Infernal Roads", "of the Relentless Chases", "of the Fiery Gallop", "of the Fearsome Journeys"]

        # Soul Collector
        if "Soul Collector" in npc.subrace:
            descriptor += ["Grim", "Ethereal", "Soulbound", "Dark", "Collector"]
            rank += ["Soul Harvester", "Grim Collector", "Ethereal Reaver", "Dark Gatherer", "Soulbound Keeper"]
            of_the += ["of the Lost Souls", "of the Ethereal Chains", "of the Soulbound Realms", "of the Dark Collections", "of the Grim Harvest"]

        # Infernal Finder
        if "Infernal Finder" in creature_type:
            descriptor += ["Seeker", "Infernal", "Unrelenting", "Determined", "Tracker"]
            rank += [
                "Gargoyle",
                "Hell's Seeker", "Infernal Tracker", "Unrelenting Finder", "Determined Pursuer", "Hellbound Locator"]
            of_the += ["of the Lost Treasures", "of the Infernal Quests", "of the Unrelenting Searches", "of the Determined Hunts", "of the Hell's Tracks"]

        # Sin Investigator
        if "Sin Investigator" in npc.subrace:
            descriptor += ["Judicial", "Infernal", "Insightful", "Detective", "Analytical"]
            rank += ["Sin Examiner", "Infernal Investigator", "Judicial Sleuth", "Detective of Deceit", "Analytical Inquirer"]
            of_the += ["of the Sinful Mysteries", "of the Infernal Truths", "of the Judicial Inquiries", "of the Deceptive Trails", "of the Analytical Pursuits"]

        # Infernal Warlord
        if "Infernal Warlord" in npc.subrace:
            descriptor += ["Warlike", "Commanding", "Infernal", "Tyrannical", "Conqueror"]
            rank += ["Infernal Commander", "Hellish General", "Warlord of the Damned", "Tyrannical Leader", "Conquering Fiend"]
            of_the += ["of the Infernal Legions", "of the Hellish Battlegrounds", "of the Conquered Realms", "of the Tyrannical Rule", "of the Damned Armies"]

        # Infernal Justiciar
        if "Infernal Justiciar" in npc.subrace:
            descriptor += ["Judgmental", "Righteous", "Infernal", "Lawbringer", "Stern"]
            rank += ["Infernal Judge", "Hellish Arbiter", "Justiciar of Flames", "Righteous Punisher", "Stern Enforcer"]
            of_the += ["of the Infernal Courts", "of the Righteous Judgments", "of the Hellish Law", "of the Stern Rule", "of the Punishing Flames"]

        # Vengeance Spirit
        if "Vengeance Spirit" in npc.subrace:
            descriptor += ["Vengeful", "Spectral", "Retributive", "Unforgiving", "Phantom"]
            rank += ["Spirit of Revenge", "Spectral Avenger", "Retributive Ghost", "Unforgiving Shade", "Phantom of Vengeance"]
            of_the += ["of the Vengeful Shadows", "of the Spectral Wrath", "of the Retributive Haunts", "of the Unforgiving Night", "of the Phantom Grudges"]

        # Retributioner
        if "Retributioner" in npc.subrace:
            descriptor += ["Retaliatory", "Judgmental", "Unyielding", "Just", "Inexorable"]
            rank += ["Retaliatory Force", "Unyielding Judge", "Just Avenger", "Inexorable Punisher", "Judgmental Executioner"]
            of_the += ["of the Inexorable Justice", "of the Retaliatory Strikes", "of the Unyielding Law", "of the Just Vengeance", "of the Judgmental Fury"]

        # Pact Enforcer
        if "Pact Enforcer" in npc.subrace:
            descriptor += ["Binding", "Unbreakable", "Pactkeeper", "Stern", "Ruthless"]
            rank += ["Enforcer of Agreements", "Pact Guardian", "Binding Fiend", "Stern Overseer", "Ruthless Executor"]
            of_the += ["of the Unbreakable Bonds", "of the Binding Oaths", "of the Pactkeeper's Realm", "of the Stern Judgments", "of the Ruthless Enforcement"]

        # Soulclaimer
        if "Soulclaimer" in npc.subrace:
            descriptor += [
                "Soulbound",
                "Harvester",
                "Soul",
                "Ethereal",
                "Claimant",
                "Collecting",
                "Soulbound"]
            rank += [
                "Harvester",
                "Claimer",
                "Collector",
                "Enforcer"]
            of_the += [
                "of Spirits",
                "of Souls",
                "of the Lost",
                "of the Lost Souls",
                "of the Damned",
                "of the Contract",
                "of the Claimed Essences",
                "of Duty"]

        # Infernal Enforcer
        if "Infernal Enforcer" in npc.subrace:
            descriptor += ["Disciplinarian", "Infernal", "Ruthless", "Enforcer", "Unyielding"]
            rank += ["Infernal Punisher", "Hellish Disciplinarian", "Ruthless Enforcer", "Unyielding Taskmaster", "Discipline Keeper"]
            of_the += ["of the Infernal Order", "of the Hellish Discipline", "of the Ruthless Command", "of the Unyielding Edicts", "of the Enforced Rule"]

                            
    if "Fiend" in creature_type:
        # descriptor for Fiend names
        descriptor += [
            "Infernal",
            "Red",
            "Diabolical",
            "Magenta",
            "Hellish", "Sinister", "Maleficent",
            "Dreadful", "Fiery", "Baleful", "Malevolent", "Nefarious",
            "Sulfurous", "Darkflame", "Abyssal", "Brutal", "Tormenting",
            "Fearsome", "Terrifying", "Cruel", "Wicked", "Vicious",
            "Ghastly", "Demonic", "Satanic", "Chthonic", "Malignant"
        ]

        # rank for Fiend names
        rank += [
            "Overlord", "Demon", "Devil", "Archfiend", "Pitmaster",
            "Hellknight", "Underlord", "Dread Duke", "Infernal Count", "Chaos Bringer",
            "Soul Collector", "Abyss Watcher", "Flame Warden", "Shadow Ruler", "Terror King",
            "Scream Queen", "Nightmare Lord", "Ravager", "Decimator", "Tormentor",
            "Hellraiser", "Doombringer", "Death Dealer", "Sin Keeper", "Oblivion Sire"
        ]
        # 'Of the' phrases for Fiend names
        of_the += [
            "of the Abyss",
            "of the Ninth Circle",
            "of the Burning Pits",
            "of the Endless Night",
            "of the Infernal Realms",
            "of the Searing Flames",
            "of the Unseen Terror",
            "of the Dread Fortress",
            "of the Lost Souls",
            "of the Eternal Chains",
            "of the Dark Prophecy",
            "of the Forbidden Arts",
            "of the Shadowflame",
            "of the Blood Moon",
            "of the Brimstone Path",
            "of the Netherworld",
            "of the Tormented",
            "of the Howling Void",
            "of the Wailing Abyss",
            "of the Hellfire",
            "of the Ruined Empire",
            "of the Desolate Wastes",
            "of the Blackened Skies",
            "of the Depths Unknown",
            "of the Forbidden Throne"
            ]
        #return f"The {random.choice(descriptor)} {random.choice(rank)} {random.choice(of_the)}"

    # Fey Race and Subraces
    if "Fey" in creature_type:
        # General Fey descriptor, rank, and Of_the Phrases
        descriptor += [
            "Green",
            "Enchanted", "Mystical", "Otherworldly", "Charming", "Ethereal"]
        rank += ["Fey Sovereign", "Mystic Wanderer", "Enchanted Guardian", "Otherworldly Emissary", "Ethereal Spirit"]
        of_the += ["of the Enchanted Woods", "of the Mystic Glades", "of the Ethereal Realms", "of the Otherworldly Visions", "of the Charming Streams"]

        # Hag
        if "Hag" in npc.subrace:
            descriptor += ["Witchlike", "Dark", "Cunning", "Malevolent", "Enchanting"]
            rank += ["Witch Queen", "Dark Enchantress", "Cunning Hag", "Malevolent Crone", "Enchanting Sorceress"]
            of_the += ["of the Dark Swamps", "of the Enchanted Forests", "of the Malevolent Curses", "of the Witching Hours", "of the Cunning Spells"]

        # Nymph
        if "Nymph" in npc.subrace:
            descriptor += ["Nature", "Graceful", "Alluring", "Forest", "Water"]
            rank += ["Forest Guardian", "Water Nymph", "Nature's Maiden", "Alluring Spirit", "Graceful Protector"]
            of_the += ["of the Whispering Woods", "of the Crystal Lakes", "of the Nature's Embrace", "of the Alluring Brooks", "of the Graceful Meadows"]

        # Pixie
        if "Pixie" in npc.subrace:
            descriptor += ["Tiny", "Mischievous", "Whimsical", "Playful", "Flighty"]
            rank += ["Pixie Trickster", "Whimsical Sprite", "Mischievous Fairy", "Playful Imp", "Flighty Wanderer"]
            of_the += ["of the Fairy Rings", "of the Whimsical Breezes", "of the Mischievous Antics", "of the Playful Dances", "of the Flighty Mirth"]

        # Satyr
        if "Satyr" in npc.subrace:
            descriptor += ["Merry", "Half-Goat", "Musical", "Rustic", "Festive"]
            rank += ["Merry Piper", "Rustic Reveler", "Musical Satyr", "Half-Goat Wanderer", "Festive Companion"]
            of_the += ["of the Rustic Festivals", "of the Merry Woods", "of the Musical Groves", "of the Festive Gatherings", "of the Half-Goat Tribes"]

        # Sprite
        if "Sprite" in npc.subrace:
            descriptor += ["Airy", "Ethereal", "Gentle", "Whispering", "Light"]
            rank += ["Airy Dancer", "Ethereal Guardian", "Gentle Breeze", "Whispering Spirit", "Light Sprite"]
            of_the += ["of the Gentle Winds", "of the Ethereal Veils", "of the Whispering Leaves", "of the Light Beams", "of the Airy Flights"]

        # High Fae
        if "High Fae" in npc.subrace:
            descriptor += ["Noble", "Regal", "Powerful", "High", "Eminent"]
            rank += ["High Lord", "Regal Lady", "Noble Sovereign", "Powerful Emissary", "Eminent Ruler"]
            of_the += ["of the High Courts", "of the Regal Realms", "of the Noble Castles", "of the Powerful Dominions", "of the Eminent Thrones"]

        # Redcap
        if "Redcap" in npc.subrace:
            descriptor += ["Ferocious", "Ruthless", "Blood", "Bloodthirsty", "Malevolent", "Sinister", "Ruthless", "Ferocious"]
            rank += ["Cap", "Hat", "Killer", "Goblin"]
            of_the += ["of the Bloodied Stones", "of the Malevolent Woods", "of the Sinister Paths", "of the Ruthless Hunts", "of the Ferocious Raids"]

        # Banshee
        if "Banshee" in npc.subrace:
            descriptor += ["Wailing", "Ethereal", "Deathly", "Mournful", "Ghostly"]
            rank += ["Wailing Spirit", "Ethereal Mourner", "Deathly Herald", "Mournful Phantom", "Ghostly Screamer"]
            of_the += ["of the Wailing Moors", "of the Ethereal Laments", "of the Deathly Visions", "of the Mournful Echoes", "of the Ghostly Realms"]

        # Leprechaun
        if "Leprechaun" in npc.subrace:
            descriptor += [
                "Green",
                "Tricky", "Gold-Loving", "Mischievous", "Wee", "Cunning"]
            rank += ["Cunning Goldsmith", "Wee Trickster", "Mischievous Imp", "Gold-Loving Mischief", "Tricky Guardian"]
            of_the += ["of the Hidden Gold", "of the Wee Folk", "of the Mischievous Deeds", "of the Cunning Traps", "of the Gold-Loving Lore"]

        # Changeling
        if "Changeling" in npc.subrace:
            descriptor += ["Shape-Changing", "Mysterious", "Deceptive", "Elusive", "Mystic"]
            rank += ["Mystic Shifter", "Deceptive Phantom", "Elusive Wanderer", "Mysterious Impersonator", "Shape-Changing Enigma"]
            of_the += ["of the Shapeless Forms", "of the Mysterious Guises", "of the Deceptive Faces", "of the Elusive Shadows", "of the Mystic Illusions"]

        # Nexus Fey
        if "Nexus Fey" in npc.subrace:
            descriptor += ["Connective", "Energetic", "Nodal", "Vibrant", "Interlinked"]
            rank += ["Nodal Guardian", "Energetic Weaver", "Connective Spirit", "Vibrant Linker", "Interlinked Emissary"]
            of_the += ["of the Energetic Nexus", "of the Vibrant Connections", "of the Nodal Points", "of the Interlinked Realms", "of the Connective Networks"]

        # Duende
        if "Duende" in npc.subrace:
            descriptor += ["Artistic", "Enigmatic", "Trickster", "Charming", "Creative"]
            rank += ["Muse of the Arts", "Enigmatic Performer", "Trickster Artist", "Charming Minstrel", "Creative Spirit"]
            of_the += ["of the Artistic Mischief", "of the Enigmatic Performances", "of the Trickster's Theater", "of the Charming Tales", "of the Creative Inspiration"]

        # Home Lares
        if "Home Lares" in npc.subrace:
            descriptor += ["Guardian", "Hearthbound", "Protective", "Domestic", "Warm"]
            rank += ["Hearth Guardian", "Protective Spirit", "Domestic Keeper", "Warm Protector", "Guardian of the Home"]
            of_the += ["of the Hearth and Home", "of the Protective Mantle", "of the Domestic Bliss", "of the Warm Embrace", "of the Guardian Spirits"]

        # Will-o'-the-wisp
        if "Will-o'-the-wisp" in npc.subrace:
            descriptor += ["Misleading", "Ghostly", "Ethereal", "Luminous", "Elusive"]
            rank += ["Ghostly Light", "Ethereal Deceiver", "Misleading Glow", "Luminous Phantom", "Elusive Guide"]
            of_the += ["of the Misleading Trails", "of the Ghostly Marshes", "of the Ethereal Flames", "of the Luminous Nights", "of the Elusive Paths"]

        # Fata
        if "Fata" in npc.subrace:
            descriptor += [
                "Destiny",
                "Mystic",
                "Fateful",
                "Enigmatic",
                "Influential"]
            rank += [
                "Oracle",
                "Weaver",
                "Fate",
                "Guide",
                "Seer"]
            of_the += [
                f"of the {random.choice(descriptor)} Destinies",
                "of Fate",
                "of Destiny",
                "of Visions",
                "of the Fateweb"
                ]

    # Giant Race and Subraces
    if "Giant" in npc.race:
        # General Giant descriptor, rank, and Of_the Phrases
        descriptor += ["Colossal", "Mighty", "Gargantuan", "Titanic", "Monumental"]
        rank += ["Giant Chieftain", "Colossus Ruler", "Titanic Guardian", "Mighty Overlord", "Monumental Protector"]
        of_the += ["of the Mountain Peaks", "of the Mighty Realms", "of the Colossal Lands", "of the Titanic Depths", "of the Monumental Fortresses"]

        # Cyclops
        if "Cyclops" in npc.subrace:
            descriptor += ["One-Eyed", "Ancient", "Solitary", "Mythical", "Visionary"]
            rank += ["Solitary Watcher", "One-Eyed Titan", "Ancient Cyclops", "Mythical Giant", "Visionary Colossus"]
            of_the += ["of the Lone Isles", "of the Ancient Ruins", "of the Solitary Mountains", "of the Mythical Legends", "of the Visionary Peaks"]

        # Ogre
        if "Ogre" in npc.subrace:
            descriptor += ["Brutish", "Fearsome", "Man-Eating", "Savage", "Monstrous"]
            rank += ["Ogre Warlord", "Brutish Behemoth", "Savage Giant", "Fearsome Predator", "Man-Eating Brute"]
            of_the += ["of the Savage Lands", "of the Fearsome Clans", "of the Man-Eating Forests", "of the Brutish Territories", "of the Monstrous Realms"]

        # Troll
        if "Troll" in npc.subrace:
            descriptor += ["Regenerating", "Mountain", "Norse", "Rugged", "Fierce"]
            rank += ["Mountain King", "Norse Colossus", "Regenerating Behemoth", "Rugged Titan", "Fierce Monarch"]
            of_the += ["of the Mountain Caves", "of the Norse Wilds", "of the Regenerating Woods", "of the Rugged Highlands", "of the Fierce Ranges"]

        # Jotunn (Frost Giant)
        if "Jotunn" in npc.subrace:
            descriptor += ["Frost", "Icy", "Norse", "Primal", "Chilling"]
            rank += ["Frost Monarch", "Icy Jotunn", "Norse Titan", "Primal Giant", "Chilling Lord"]
            of_the += ["of the Frozen Wastes", "of the Icy Mountains", "of the Norse Legends", "of the Primal Snows", "of the Chilling Realms"]

        # Fire Giant
        if "Fire Giant" in npc.subrace:
            descriptor += ["Infernal", "Fiery", "Muspelheim", "Blazing", "Volcanic"]
            rank += ["Infernal Overlord", "Fiery Titan", "Muspelheim Ruler", "Blazing Colossus", "Volcanic Giant"]
            of_the += ["of the Infernal Forges", "of the Fiery Pits", "of the Muspelheim Flames", "of the Blazing Mountains", "of the Volcanic Lands"]

        # Gigantes
        if "Gigantes" in npc.subrace:
            descriptor += ["Mythical", "Grecian", "Mighty", "Warlike", "Vengeful"]
            rank += ["Mythical Giant", "Grecian Titan", "Warlike Colossus", "Mighty Behemoth", "Vengeful Overlord"]
            of_the += ["of the Ancient Myths", "of the Grecian Wars", "of the Mighty Battles", "of the Warlike Realms", "of the Vengeful Spirits"]

        # Nephilim
        if "Nephilim" in npc.subrace:
            descriptor += ["Biblical", "Ancient", "Mighty", "Legendary", "Divine"]
            rank += ["Ancient Nephilim", "Divine Giant", "Legendary Behemoth", "Mighty Ancestor", "Biblical Titan"]
            of_the += ["of the Ancient Epochs", "of the Divine Lineage", "of the Legendary Tales", "of the Mighty Heritage", "of the Biblical Lands"]

        # Oni
        if "Oni" in npc.subrace:
            descriptor += ["Japanese", "Demonlike", "Terrifying", "Ogre", "Menacing"]
            rank += ["Oni Warlord", "Demonlike Ogre", "Terrifying Giant", "Japanese Fiend", "Menacing Brute"]
            of_the += ["of the Eastern Mountains", "of the Demonlike Legends", "of the Terrifying Myths", "of the Ogre Realms", "of the Menacing Tales"]

        # Ettin (Two headed)
        if "Ettin (Two headed)" in npc.subrace:
            descriptor += ["Two-Headed", "Brawny", "Conflicted", "Dual-Natured", "Rugged"]
            rank += ["Brawny Ettin", "Two-Headed Giant", "Dual-Natured Colossus", "Conflicted Behemoth", "Rugged Titan"]
            of_the += ["of the Two Minds", "of the Brawny Mountains", "of the Conflicted Lands", "of the Dual-Natured Realms", "of the Rugged Territories"]

        # Fomorians (Sea Giants)
        if "Fomorians (Sea Giants)" in npc.subrace:
            descriptor += ["Sea-Bound", "Fearsome", "Ancient", "Icy", "Dark"]
            rank += ["Sea Giant King", "Fearsome Fomorian", "Ancient Mariner", "Icy Leviathan", "Dark Ocean Lord"]
            of_the += ["of the Icy Depths", "of the Sea-Bound Realms", "of the Fearsome Tides", "of the Ancient Oceans", "of the Dark Seas"]

        # Goliath
        if "Goliath" in npc.subrace:
            descriptor += ["Gargantuan", "Strong", "Imposing", "Warrior", "Mythic"]
            rank += ["Goliath Champion", "Strong Colossus", "Imposing Warrior", "Gargantuan Fighter", "Mythic Giant"]
            of_the += ["of the Mountain Clans", "of the Strongholds", "of the Imposing Peaks", "of the Warrior Tribes", "of the Mythic Battles"]

        # Cloud Giant
        if "Cloud Giant" in npc.subrace:
            descriptor += ["Noble", "Skyborne", "Lofty", "Ethereal", "Majestic"]
            rank += ["Cloud Monarch", "Skyborne Ruler", "Lofty Sovereign", "Ethereal Lord", "Majestic Titan"]
            of_the += ["of the Sky Castles", "of the Cloud Kingdoms", "of the Lofty Realms", "of the Ethereal Heights", "of the Majestic Skies"]

        # Stone Giant
        if "Stone Giant" in npc.subrace:
            descriptor += ["Rocky", "Stoic", "Earthen", "Immovable", "Rugged"]
            rank += ["Rocky Titan", "Stoic Colossus", "Earthen Guardian", "Immovable Lord", "Rugged Protector"]
            of_the += ["of the Stony Mountains", "of the Earthen Realms", "of the Immovable Fortresses", "of the Stoic Lands", "of the Rugged Peaks"]

        # Storm Giant
        if "Storm Giant" in npc.subrace:
            descriptor += ["Thunderous", "Tempestuous", "Sky Lord", "Majestic", "Electric"]
            rank += ["Thunderous Sovereign", "Tempestuous Ruler", "Sky Lord", "Majestic Titan", "Electric Monarch"]
            of_the += ["of the Thundering Skies", "of the Tempestuous Clouds", "of the Electric Realms", "of the Majestic Storms", "of the Sky Dominions"]

    # Gnome Race and Subraces
    if "Gnome" in creature_type:
        # General Gnome descriptor, rank, and Of_the Phrases
        descriptor += [
            "Master",
            "Gnomish", 
            "Inventive",
            "Curious", "Small", "Whimsical", "Clever"]
        rank += ["Tinker",
                 "Inventor",
                 "Sage",
                 "Explorer",
                 "Artisan"]
        of_the += ["of the Hidden Workshops",
                   "of the Whimsical Gardens",
                   "of the Curious Expeditions",
                   "of the Clever Creations",
                   "of the Small Wonders"]

        # Mountain
        if "Mountain" in npc.subrace:
            descriptor += ["Sturdy", "Mountainous", "Rocky", "Adventurous", "Rugged"]
            rank += ["Mountain Artisan", "Sturdy Explorer", "Rocky Sage", "Adventurous Creator", "Rugged Inventor"]
            of_the += ["of the Mountain Peaks", "of the Sturdy Cliffs", "of the Rocky Caverns", "of the Adventurous Trails", "of the Rugged Landscapes"]

        # Forest
        if "Forest" in creature_type:
            descriptor += [
                "Green",
                "Woodland", "Nature-Loving", "Green", "Sylvan", "Earthy"]
            rank += ["Forest Wanderer", "Nature Tinker", "Green Artisan", "Sylvan Creator", "Earthy Innovator"]
            of_the += ["of the Woodland Glens", "of the Nature-Crafted Items", "of the Green Canopies", "of the Sylvan Groves", "of the Earthy Dwellings"]

        # Garden
        if "Garden" in creature_type:
            descriptor += [
                "Green",
                "Botanical", "Floral", "Green-Thumb", "Gardener", "Blossoming"]
            rank += ["Botanical Curator", "Floral Artisan", "Garden Keeper", "Green-Thumb Tinker", "Blossoming Inventor"]
            of_the += ["of the Blossoming Gardens", "of the Botanical Wonders", "of the Floral Paradises", "of the Green Sanctuaries", "of the Gardener's Delights"]

        # Tinker
        if "Tinker" in npc.subrace:
            descriptor += ["Mechanical", "Ingenious", "Crafty", "Inventive", "Resourceful"]
            rank += ["Master Tinker", "Ingenious Mechanic", "Crafty Inventor", "Inventive Genius", "Resourceful Creator"]
            of_the += ["of the Ingenious Contraptions", "of the Mechanical Wonders", "of the Crafty Gadgets", "of the Inventive Solutions", "of the Resourceful Creations"]

        # Crossroad
        if "Crossroad" in npc.subrace:
            descriptor += ["Traveler", "Wandering", "Mysterious", "Crossroad", "Adventurous"]
            rank += ["Crossroad Explorer", "Wandering Nomad", "Mysterious Wayfarer", "Adventurous Wanderer", "Traveler of Paths"]
            of_the += ["of the Crossroad Journeys", "of the Wandering Tales", "of the Mysterious Travels", "of the Adventurous Roads", "of the Traveler's Destinations"]

        # Trickster
        if "Trickster" in npc.subrace:
            descriptor += ["Mischievous", "Playful", "Cunning", "Prankter", "Witty"]
            rank += ["Mischievous Rascal", "Playful Prankter", "Cunning Jester", "Witty Trickster", "Clever Rogue"]
            of_the += ["of the Playful Mischief", "of the Cunning Tricks", "of the Prankter's Games", "of the Witty Escapades", "of the Clever Ruses"]

        # Wandering
        if "Wandering" in npc.subrace:
            descriptor += [
                "Nomadic", "Roaming", "Adventurous", "Wandering", "Explorative"]
            rank += ["Roaming Artisan", "Nomadic Tinker", "Adventurous Creator", "Wandering Inventor", "Explorative Pioneer"]
            of_the += ["of the Roaming Tribes", "of the Nomadic Journeys", "of the Adventurous Expeditions", "of the Wandering Spirits", "of the Explorative Paths"]

    # Goblin Kind Race and Subraces
    if "Goblin" in creature_type:
        # General Goblin descriptor, rank, and Of_the Phrases
        descriptor += [
            "Green",
            "Sneaky", "Green Skin", "Goblin's", "Crafty", "Cunning",]
        rank += ["Goblin Chief", "Sneak Master", "Crafty Thief", "Cunning Strategist", "Mischievous Trickster"]
        of_the += ["of the Shadowy Nooks", "of the Green Woods", "of the Crafty Hideouts", "of the Cunning Plans", "of the Mischievous Antics"]

        # Hobgoblin
        if "Hobgoblin" in npc.subrace:
            descriptor += ["Disciplined", "Militant", "Red-Skinned", "Strategic", "Orderly"]
            rank += ["Hobgoblin Captain", "Militant Leader", "Disciplined Commander", "Strategic Warlord", "Orderly Chieftain"]
            of_the += ["of the Militant Camps", "of the Disciplined Legions", "of the Strategic Battalions", "of the Orderly Barracks", "of the Red-Skinned Warriors"]

        # Bugbear
        if "Bugbear" in npc.subrace:
            descriptor += ["Stealthy", "Brutish", "Lurking", "Fearsome", "Predatory"]
            rank += ["Bugbear Stalker", "Brutish Ambusher", "Stealthy Predator", "Lurking Brute", "Fearsome Hunter"]
            of_the += ["of the Shadowed Paths", "of the Brutish Clans", "of the Stealthy Raids", "of the Lurking Shadows", "of the Predatory Hunts"]

        # Gremlin (Tecnogoblin)
        if "Gremlin (Tecnogoblin)" in npc.subrace:
            descriptor += ["Saboteur", "Mechanical", "Inventive", "Mischief-Maker", "Tinkering"]
            rank += ["Master Saboteur", "Mechanical Fiend", "Inventive Mischief-Maker", "Tinkering Rogue", "Gremlin Engineer"]
            of_the += ["of the Tangled Wires", "of the Mechanical Havoc", "of the Inventive Disruptions", "of the Tinkering Chaos", "of the Sabotaged Machines"]

        # Redcap
        if "Redcap" in npc.subrace:
            descriptor += [
                "Red",
                "Bloodthirsty", "Murderous", "Menacing", "Crimson-Capped", "Fierce"]
            rank += ["Redcap Slayer", "Bloodthirsty Fiend", "Murderous Goblin", "Menacing Terror", "Crimson Warrior"]
            of_the += ["of the Blood-Soaked Fields", "of the Murderous Rampages", "of the Menacing Shadows", "of the Crimson Battles", "of the Fierce Raids"]

        # Nyk (Watergoblin)
        if "Nyk" in npc.subrace:
            descriptor += ["Aquatic", "Slippery", "River-Dwelling", "Mysterious", "Watery"]
            rank += ["River Nyk", "Aquatic Trickster", "Slippery Fiend", "Mysterious Water Spirit", "Watery Phantom"]
            of_the += ["of the Flowing Rivers", "of the Aquatic Realms", "of the Slippery Banks", "of the Mysterious Streams", "of the Watery Depths"]

        # Trow (Dark goblin)
        if "Trow" in npc.subrace:
            descriptor += ["Shadowy", "Mischief-Maker", "Dark", "Elusive", "Nocturnal"]
            rank += ["Shadow Trow", "Dark Trickster", "Mischief-Making Fiend", "Elusive Phantom", "Nocturnal Goblin"]
            of_the += ["of the Nocturnal Mischief", "of the Shadowy Corners", "of the Dark Caves", "of the Elusive Nights", "of the Nocturnal Haunts"]

        # Knocker (Underdark goblin)
        if "Knocker" in npc.subrace:
            descriptor += ["Subterranean", "Mine-Dwelling", "Echoing", "Mysterious", "Hidden"]
            rank += ["Mine Knocker", "Subterranean Guardian", "Echoing Spirit", "Mysterious Miner", "Hidden Dweller"]
            of_the += ["of the Echoing Mines", "of the Subterranean Depths", "of the Mysterious Tunnels", "of the Hidden Chambers", "of the Underground Realms"]

        # Domovoi (House Goblin)
        if "Domovoi (House Goblin)" in npc.subrace:
            descriptor += ["Hearthbound", "Guardian", "Domestic", "Protective", "Housebound"]
            rank += ["Hearth Domovoi", "Guardian of the Home", "Domestic Spirit", "Protective Phantom", "Housebound Goblin"]
            of_the += ["of the Hearth and Home", "of the Guardian Hearths", "of the Domestic Realms", "of the Protective Abodes", "of the Housebound Mysteries"]
    # Monstrosity Race and Subraces
    if "Monstrosity" in creature_type:
        # General Monstrosity descriptor, rank, and Of_the Phrases
        descriptor += [
            "Yellow",
            "Terrifying", "Monstrous", "Fearsome", "Beastly", "Mythical"]
        rank += ["Monstrous Overlord", "Terrifying Beast", "Fearsome Predator", "Beastly Sovereign", "Mythical Fiend"]
        of_the += ["of the Dark Wilderness", "of the Fearsome Depths", "of the Mythical Lands", "of the Beastly Dominions", "of the Terrifying Realms"]

        # Basilisk
        if "Basilisk" in npc.subrace:
            descriptor += ["Petrifying", "Lethal", "Reptilian", "Deadly", "Serpentine"]
            rank += ["Petrifying Serpent", "Lethal Lizard", "Reptilian Horror", "Deadly Basilisk", "Serpentine Monster"]
            of_the += ["of the Stone Gaze", "of the Reptilian Depths", "of the Deadly Terrains", "of the Serpentine Lairs", "of the Petrifying Presence"]

        # Chimera
        if "Chimera" in npc.subrace:
            descriptor += ["Multi-headed", "Hybrid", "Terrifying", "Monstrous", "Mythical"]
            rank += ["Hybrid Terror", "Multi-Headed Beast", "Terrifying Chimera", "Monstrous Fiend", "Mythical Horror"]
            of_the += ["of the Hybrid Forms", "of the Terrifying Roars", "of the Monstrous Realms", "of the Multi-Headed Nightmares", "of the Mythical Menace"]

        # Displacer Beast
        if "Displacer Beast" in npc.subrace:
            descriptor += [
                "Ethereal",
                "Illusive",
                "Feline",
                "Deadly",
                "Shift",
                "Evasive"]
            rank += [
                "Predator",
                "Phantom",
                "Menace",
                "Beast",
                "Hunter"]
            of_the += ["of the Ethereal Hunt", "of the Deadly Shadows", "of the Illusive Stalk", "of the Feline Deception", "of the Evasive Tactics"]

        # Doppelganger
        if "Doppelganger" in npc.subrace:
            descriptor += ["Shape-shifting", "Deceptive", "Mimic", "Duplicitous", "Eerie"]
            rank += ["Master of Disguise", "Deceptive Mimic", "Shape-Shifter", "Duplicitous Phantom", "Eerie Imposter"]
            of_the += ["of the Deceptive Forms", "of the Mimicked Faces", "of the Shape-Shifting Mystery", "of the Duplicitous Shadows", "of the Eerie Doubles"]

        # Gorgon
        if "Gorgon" in creature_type:
            descriptor += [
                "Green",
                "Stone-Gazing", "Serpentine", "Terrifying", "Mythical", "Cursed"]
            rank += ["Stone Curse Bringer", "Serpentine Horror", "Terrifying Gorgon", "Mythical Medusa", "Cursed Monstrosity"]
            of_the += ["of the Petrifying Gaze", "of the Serpentine Coils", "of the Terrifying Legends", "of the Mythical Curses", "of the Stony Realms"]

        # Griffon
        if "Griffon" in npc.subrace:
            descriptor += ["Majestic", "Winged", "Noble", "Beastly", "Eagle-Lion"]
            rank += ["Majestic Flyer", "Noble Guardian", "Winged Protector", "Beastly Sovereign", "Eagle-Lion Ruler"]
            of_the += ["of the Sky Dominions", "of the Noble Heights", "of the Winged Territories", "of the Majestic Mountains", "of the Beastly Realms"]

        # Harpy
        if "Harpy" in npc.subrace:
            descriptor += ["Screeching", "Winged", "Fearsome", "Predatory", "Vicious"]
            rank += ["Screeching Fiend", "Winged Terror", "Fearsome Harpy", "Predatory Menace", "Vicious Hunter"]
            of_the += ["of the Mountain Nests", "of the Screeching Cliffs", "of the Fearsome Skies", "of the Predatory Hunts", "of the Vicious Storms"]

        # Horror
        if "Horror" in npc.subrace:
            descriptor += ["Nightmarish", "Terrifying", "Eldritch", "Unspeakable", "Abominable"]
            rank += ["Nightmarish Entity", "Terrifying Abomination", "Eldritch Horror", "Unspeakable Fiend", "Abominable Presence"]
            of_the += ["of the Nightmarish Visions", "of the Terrifying Depths", "of the Eldritch Shadows", "of the Unspeakable Realms", "of the Abominable Lands"]

        # Kerberus
        if "Kerberus" in npc.subrace:
            descriptor += ["Three-Headed", "Guardian", "Infernal", "Fierce", "Menacing"]
            rank += ["Three-Headed Guardian", "Infernal Protector", "Fierce Watchdog", "Menacing Beast", "Guardian of the Gates"]
            of_the += ["of the Infernal Gates", "of the Three-Headed Vigil", "of the Fierce Realm", "of the Menacing Terrains", "of the Guardian's Keep"]

        # Sphynx
        if "Sphynx" in creature_type:
            descriptor += [
                "Astral",
                "Enigmatic",
                "Mystical",
                "Wise",
                "Riddler",
                "Speaking",
                "Mystical",
                ]
            rank += [
                "Riddle",
                "Speaker",
                "Guardian",
                "Enigma",
                "Oracle",
                "Sphynx",
                "Protector",
                "Keepers",
                ]
            of_the += [
                "of the Enigma",
                "of the Riddles",
                f"of the {random.choice(descriptor)} Realms",
                "of Wisdom",
                "of the Secrets",
                "of the Monument",
                "of Secrets"]

        # Manticore
        if "Manticore" in npc.subrace:
            descriptor += ["Lion-Scorpion", "Deadly", "Spiked", "Fearsome", "Savage"]
            rank += ["Savage Manticore", "Deadly Hunter", "Spiked Terror", "Fearsome Beast", "Lion-Scorpion Predator"]
            of_the += ["of the Spiked Tails", "of the Savage Jungles", "of the Deadly Hunts", "of the Fearsome Claws", "of the Lion-Scorpion's Lair"]

        # Yeti
        if "Yeti" in npc.subrace:
            descriptor += ["Abominable", "Snowbound", "Icy", "Frosty", "Mountain"]
            rank += ["Abominable Snowbeast", "Snowbound Giant", "Icy Predator", "Frosty Behemoth", "Mountain Dweller"]
            of_the += ["of the Frozen Wastes", "of the Snowbound Peaks", "of the Icy Caverns", "of the Frosty Realms", "of the Mountainous Wilderness"]

        # Worg
        if "Worg" in npc.subrace:
            descriptor += ["Ferocious", "Wolf-Like", "Savage", "Menacing", "Predatory"]
            rank += ["Ferocious Alpha", "Wolf-Like Leader", "Savage Predator", "Menacing Hunter", "Predatory Beast"]
            of_the += ["of the Dark Forests", "of the Savage Packs", "of the Menacing Hunts", "of the Wolf-Like Shadows", "of the Predatory Lands"]

        # Wendigo
        if "Wendigo" in npc.subrace:
            descriptor += ["Cannibalistic", "Horrifying", "Gaunt", "Icy", "Ghastly"]
            rank += ["Cannibalistic Fiend", "Horrifying Spirit", "Gaunt Predator", "Icy Horror", "Ghastly Wraith"]
            of_the += ["of the Frozen Terrors", "of the Cannibalistic Legends", "of the Ghastly Woods", "of the Icy Nightmares", "of the Gaunt Shadows"]

        # Kraken
        if "Kraken" in npc.subrace:
            descriptor += [
                "Green",
                "Tentacled", "Sea Monster", "Deep Sea", "Colossal", "Terrifying"]
            rank += ["Colossal Leviathan", "Deep Sea Terror", "Tentacled Behemoth", "Sea Monster", "Terrifying Kraken"]
            of_the += ["of the Deep Ocean", "of the Colossal Depths", "of the Tentacled Horrors", "of the Sea Monsters' Lair", "of the Terrifying Abyss"]

        # Chupacabra
        if "Chupacabra" in npc.subrace:
            descriptor += ["Blood-Sucking", "Cryptid", "Elusive", "Nocturnal", "Fearsome"]
            rank += ["Cryptid Predator", "Blood-Sucking Fiend", "Elusive Beast", "Nocturnal Terror", "Fearsome Hunter"]
            of_the += ["of the Cryptid Legends", "of the Blood-Sucking Myths", "of the Elusive Shadows", "of the Nocturnal Hunts", "of the Fearsome Night"]

        # Land Shark
        if "Land Shark" in npc.subrace:
            descriptor += ["Burrowing", "Terrifying", "Predatory", "Monstrous", "Ravenous"]
            rank += ["Burrowing Terror", "Terrifying Predator", "Monstrous Shark", "Ravenous Beast", "Land Shark"]
            of_the += ["of the Burrowing Depths", "of the Terrifying Hunts", "of the Monstrous Lands", "of the Ravenous Appetites", "of the Land Seas"]

    if "Ooze" in npc.race:
        # General Ooze descriptor, rank, and Of_the Phrases
        descriptor += [
            "Amorphous", "Viscous", "Slithering", "Absorbing", "Gelatinous"]
        rank += ["Amorphous Mass", "Viscous Entity", "Slithering Blob", "Absorbing Horror", "Gelatinous Devourer"]
        of_the += ["of the Slime Pits", "of the Gelatinous Depths", "of the Viscous Swamps", "of the Amorphous Expanse", "of the Absorbing Mires"]
        descriptor += [
            "Amorphous", "Viscous", "Slithering", "Absorbing", "Gelatinous",
            "Shapeless", "Fluidic", "Translucent", "Thick", "Sticky",
            "Fungal", "Cubic", "Ashen", "Earthen", "Dark",
            "Fiery", "Crystalline", "Acidic", "Icy", "Mystical",
            "Glowing", "Poisonous"
        ]

        # Expanded rank
        rank += [
            "Amorphous Mass", "Viscous Entity", "Slithering Blob", "Absorbing Horror", "Gelatinous Devourer",
            "Shapeless Horror", "Fluidic Menace", "Translucent Predator", "Thick Sludge", "Sticky Trap",
            "Fungal Growth", "Cubic Engulfer", "Ashen Slime", "Earthen Muck", "Dark Puddle",
            "Fiery Magma Ooze", "Crystalline Gel", "Acidic Pool", "Icy Slush", "Mystical Blob",
            "Glowing Goo", "Poisonous Jelly"
        ]

        # Expanded Of_the Phrases
        of_the += [
            "of the Slime Pits", "of the Gelatinous Depths", "of the Viscous Swamps", "of the Amorphous Expanse", "of the Absorbing Mires",
            "of the Shapeless Form", "of the Fluidic Streams", "of the Translucent Veils", "of the Thick Goo", "of the Sticky Floors",
            "of the Fungal Forests", "of the Cubic Dungeons", "of the Ashen Bogs", "of the Earthen Marshes", "of the Dark Crevices",
            "of the Fiery Lakes", "of the Crystalline Caverns", "of the Acidic Waters", "of the Icy Glaciers", "of the Mystical Vapors",
            "of the Glowing Radiance", "of the Poisonous Mists"
        ]


        # Blob
        if "Blob" in npc.subrace:
            descriptor += ["Amorphous", "Shapeless", "Formless", "Unstructured"]
            rank += ["Amorphous Mass", "Shapeless Horror", "Formless Devourer", "Unstructured Blob"]
            of_the += ["of the Unformed Swamps", "of the Shapeless Expanse", "of the Amorphous Depths", "of the Formless Pits"]

        # Slime
        if "Slime" in npc.subrace:
            descriptor += ["Slimy", "Slick", "Fluidic", "Quick"]
            rank += ["Slimy Menace", "Slick Predator", "Fluidic Ooze", "Quick Slime"]
            of_the += ["of the Slippery Slopes", "of the Fluidic Pools", "of the Slimy Trails", "of the Quick Movements"]

        # Jelly
        if "Jelly" in npc.subrace:
            descriptor += ["Gelatinous", "Translucent", "Wobbly", "Jiggly"]
            rank += ["Gelatinous Blob", "Translucent Mass", "Wobbly Menace", "Jiggly Beast"]
            of_the += ["of the Clear Lakes", "of the Gelatinous Mounds", "of the Translucent Forms", "of the Jiggly Horrors"]

        # Pudding
        if "Pudding" in npc.subrace:
            descriptor += ["Thick", "Dense", "Aggressive", "Consuming"]
            rank += ["Thick Sludge", "Dense Mass", "Aggressive Pudding", "Consuming Horror"]
            of_the += ["of the Dense Jungles", "of the Thick Swamps", "of the Aggressive Attacks", "of the Consuming Darkness"]

        # Goo
        if "Goo" in npc.subrace:
            descriptor += ["Sticky", "Adhesive", "Clingy", "Trapping"]
            rank += ["Sticky Trap", "Adhesive Mass", "Clingy Blob", "Trapping Goo"]
            of_the += ["of the Sticky Floors", "of the Adhesive Walls", "of the Clingy Depths", "of the Trapping Pits"]

        # Mold
        if "Mold" in npc.subrace:
            descriptor += ["Fungal", "Spore-Producing", "Decaying", "Musty"]
            rank += ["Fungal Growth", "Spore-Producing Blob", "Decaying Mass", "Musty Mold"]
            of_the += ["of the Fungal Forests", "of the Spore-Filled Caves", "of the Decaying Woods", "of the Musty Dungeons"]

        # Cube
        if "Cube" in npc.subrace:
            descriptor += ["Cubic", "Square", "Transparent", "Engulfing"]
            rank += ["Cubic Mass", "Square Behemoth", "Transparent Predator", "Engulfing Cube"]
            of_the += ["of the Cubic Chambers", "of the Square Passages", "of the Transparent Traps", "of the Engulfing Depths"]

        # Gray
        if "Gray" in npc.subrace:
            descriptor += ["Ashen", "Dull", "Sombre", "Monochrome"]
            rank += ["Ashen Blob", "Dull Mass", "Sombre Ooze", "Monochrome Sludge"]
            of_the += ["of the Gray Wastelands", "of the Ashen Mires", "of the Dull Caverns", "of the Monochrome Pools"]

        # Ochre
        if "Ochre" in creature_type:
            descriptor += [
                "Yellow",
                "Earthen", "Muddy", "Rustic", "Clay-Like"]
            rank += ["Earthen Slime", "Muddy Blob", "Rustic Puddle", "Clay-Like Mass"]
            of_the += ["of the Muddy Banks", "of the Earthen Pits", "of the Rustic Marshes", "of the Clay Fields"]

        # Black
        if "Black" in npc.subrace:
            descriptor += ["Dark", "Obsidian", "Shadowy", "Inky"]
            rank += ["Dark Sludge", "Obsidian Mass", "Shadowy Ooze", "Inky Blob"]
            of_the += ["of the Dark Depths", "of the Obsidian Caves", "of the Shadowy Corners", "of the Inky Pools"]

        # Magma
        if "Magma" in npc.subrace:
            descriptor += ["Fiery", "Molten", "Lava-Like", "Blazing"]
            rank += ["Fiery Blob", "Molten Ooze", "Lava-Like Sludge", "Blazing Puddle"]
            of_the += ["of the Volcanic Vents", "of the Fiery Rivers", "of the Molten Lakes", "of the Blazing Fields"]

        # Crystal
        if "Crystal" in npc.subrace:
            descriptor += ["Crystalline", "Sparkling", "Gem-Like", "Translucent"]
            rank += ["Crystalline Mass", "Sparkling Slime", "Gem-Like Blob", "Translucent Goo"]
            of_the += ["of the Crystal Caverns", "of the Sparkling Mines", "of the Gem Forests", "of the Translucent Depths"]

        # Corrosive
        if "Corrosive" in creature_type:
            descriptor += [
                "Green",
                "Acidic", "Caustic", "Erosive", "Burning"]
            rank += ["Acidic Sludge", "Caustic Mass", "Erosive Ooze", "Burning Gel"]
            of_the += ["of the Acidic Pits", "of the Caustic Swamps", "of the Erosive Gullies", "of the Burning Lakes"]

        # Frost
        if "Frost" in npc.subrace:
            descriptor += ["Icy", "Frozen", "Chilling", "Glacial"]
            rank += ["Icy Blob", "Frozen Ooze", "Chilling Slime", "Glacial Mass"]
            of_the += ["of the Frozen Tundras", "of the Icy Caverns", "of the Chilling Fields", "of the Glacial Pools"]

        # Eldritch
        if "Eldritch" in creature_type:
            descriptor += [
                "Astral",
                "Mystical",
                "Arcane",
                "Otherworldly",
                "Unearthly"]
            rank += [
                "Sludge",
                "Ooze",
                "Blob",
                "Goo"]
            of_the += [
                f"of the {random.choice(descriptor)} Realms",
                "of the Void",
                "of the Otherworld",
                ]

        # Luminous
        if "Luminous" in npc.subrace:
            descriptor += ["Glowing", "Radiant", "Luminescent", "Shining"]
            rank += ["Glowing Gel", "Radiant Ooze", "Luminescent Blob", "Shining Slime"]
            of_the += ["of the Glowing Caves", "of the Radiant Lakes", "of the Luminescent Swamps", "of the Shining Pits"]

        # Toxic
        if "Toxic" in npc.subrace:
            descriptor += [
                "Green",
                "Poisonous", "Venomous", "Toxic", "Hazardous"]
            rank += ["Poisonous Mass", "Venomous Blob", "Toxic Sludge", "Hazardous Goo"]
            of_the += ["of the Toxic Wastes", "of the Venomous Bogs", "of the Poisonous Marshes", "of the Hazardous Quagmires"]

    # Orc Race and Subraces
    if "Orc" in npc.race:
        # General Orc descriptor, rank, and Of_the Phrases
        descriptor += [
            "Red",
            "Yellow",
            "Green",
            "Black",
            "Brown",
            "Warrior", "Brutish", "Fierce", "Strong", "Savage", "Free"]
        rank += ["War Chief", "Brutish Overlord", "Fierce Marauder", "Strong Leader", "Savage Fighter"]
        of_the += ["of the Orde", "of the Clans", "of the Tribes", "of the Fierce Legions", "of the Strongholds", "of the Free Lands"]

        # Mountain
        if "Mountain" in npc.subrace:
            descriptor += ["Mountainous", "Stony", "Rugged", "Highland"]
            rank += ["Mountain Warlord", "Stony Chieftain", "Rugged Fighter", "Highland Leader"]
            of_the += ["of the Mountain Peaks", "of the Stony Valleys", "of the Rugged Terrain", "of the Highland Realms"]

        # Desert
        if "Desert" in npc.subrace:
            descriptor += [
                "Yellow",
                "Desert", "Sun-Scorched", "Nomadic", "Sand"]
            rank += ["Desert Raider", "Sun-Scorched Chief", "Nomadic Warrior", "Sand Marauder"]
            of_the += ["of the Desert Wastes", "of the Sun-Scorched Sands", "of the Nomadic Tribes", "of the Sand Dunes"]

        # Swamp
        if "Swamp" in creature_type:
            descriptor += [
                "Green",
                "Swamp", "Mire", "Bog", "Marsh"]
            rank += ["Swamp Hunter", "Mire Chieftain", "Bog Warrior", "Marsh Leader"]
            of_the += ["of the Swamp Lands", "of the Mire Depths", "of the Bog Territories", "of the Marsh Realms"]

        # Snow
        if "Snow" in npc.subrace:
            descriptor += ["Snow", "Icy", "Frost", "Winter"]
            rank += ["Snow Chief", "Icy Raider", "Frost Warrior", "Winter Marauder"]
            of_the += ["of the Snow Fields", "of the Icy Mountains", "of the Frost Lands", "of the Winter Territories"]

        # Uruk
        if "Uruk" in npc.subrace:
            descriptor += ["Warbred", "Mighty", "Elite", "Fearsome"]
            rank += ["Warbred Leader", "Mighty Champion", "Elite Warrior", "Fearsome Commander"]
            of_the += ["of the Warbred Legions", "of the Mighty Clans", "of the Elite Forces", "of the Fearsome Battalions"]

        # Half-Orc
        if "Half-Orc" in creature_type:
            descriptor += [
                "Green",
                "Half-Breed", "Mixed", "Strongblood", "Dual-Nature"]
            rank += [
                "Mestizo",
                "Half-Breed Leader", "Mixed Blood Warrior", "Strongblood Fighter", "Dual-Nature Chief"]
            of_the += ["of the Mixed Clans", "of the Half-Breed Tribes", "of the Strongblood Lines", "of the Dual-Nature Realms"]

        # Orog (Underdark)
        if "Orog (Underdark)" in npc.subrace:
            descriptor += [
                "White",
                "Pale",
                "Underdark", "Tunnel", "Subterranean", "Dark"]
            rank += ["Underdark Commander", "Tunnel Raider", "Subterranean Chief", "Dark Warrior"]
            of_the += ["of the Underdark Realms", "of the Tunnel Depths", "of the Subterranean Tribes", "of the Dark Caverns"]

        # Cave
        if "Cave" in npc.subrace:
            descriptor += ["Cavernous", "Rocky", "Echoing", "Shade"]
            rank += ["Cavern Chief", "Rocky Marauder", "Echoing Fighter", "Shade Hunter"]
            of_the += ["of the Cavernous Labyrinths", "of the Rocky Enclaves", "of the Echoing Caves", "of the Shaded Depths"]

        # Forest
        if "Forest" in npc.subrace:
            descriptor += [
                "Green",
                "Woodland", "Leafy", "Verdant", "Sylvan"]
            rank += ["Woodland Chieftain", "Leafy Scout", "Verdant Warrior", "Sylvan Hunter"]
            of_the += ["of the Woodland Groves", "of the Leafy Canopies", "of the Verdant Jungles", "of the Sylvan Glades"]

        # Nomadic
        if "Nomadic" in npc.subrace:
            descriptor += ["Wandering", "Traveling", "Roaming", "Migratory"]
            rank += ["Wandering Leader", "Traveling Warlord", "Roaming Hunter", "Migratory Chieftain"]
            of_the += ["of the Wandering Tribes", "of the Traveling Bands", "of the Roaming Packs", "of the Migratory Routes"]

        # Island
        if "Island" in npc.subrace:
            descriptor += ["Isolated", "Maritime", "Coastal", "Sea-Bound"]
            rank += ["Isolated Chief", "Maritime Raider", "Coastal Warrior", "Sea-Bound Marauder"]
            of_the += ["of the Isolated Isles", "of the Maritime Cliffs", "of the Coastal Jungles", "of the Sea-Bound Shores"]

        # Urbanite
        if "Urbanite" in npc.subrace:
            descriptor += ["City", "Urban", "Streetwise", "Civilized"]
            rank += ["City Chief", "Urban Warlord", "Streetwise Leader", "Civilized Commander"]
            of_the += ["of the City Slums", "of the Urban Jungles", "of the Streetwise Gangs", "of the Civilized Districts"]

        # Feral
        if "Feral" in npc.subrace:
            descriptor += ["Wild", "Untamed", "Savage", "Primal"]
            rank += ["Wild Chief", "Untamed Leader", "Savage Warrior", "Primal Hunter"]
            of_the += ["of the Wild Lands", "of the Untamed Territories", "of the Savage Packs", "of the Primal Jungles"]

    # Plant Race and Subraces
    if "Plant" in npc.race:
        # General Plant descriptor, rank, and Of_the Phrases
        descriptor += [
            "Red",
            "Green",
            "Verdant", "Leafy", "Woody", "Floral", "Nature-Bound"]
        rank += ["Verdant Guardian", "Leafy Protector", "Woody Sentinel", "Floral Emissary", "Nature-Bound Elder"]
        of_the += ["of the Deep Woods", "of the Lush Canopies", "of the Floral Gardens", "of the Ancient Groves", "of the Verdant Glades"]

        # Willow Guardian
        if "Willow Guardian" in npc.subrace:
            descriptor += ["Weeping", "Graceful", "Watery", "Swaying"]
            rank += ["Weeping Protector", "Graceful Willow", "Watery Sentinel", "Swaying Guardian"]
            of_the += ["of the Weeping Rivers", "of the Graceful Bends", "of the Watery Banks", "of the Swaying Meadows"]

        # Treant
        if "Treant" in npc.subrace:
            descriptor += ["Ancient", "Giant", "Wise", "Sturdy"]
            rank += ["Ancient Treant", "Giant Tree", "Wise Oak", "Sturdy Guardian"]
            of_the += ["of the Old Forest", "of the Giant Woods", "of the Wise Groves", "of the Sturdy Branches"]

        # Awakened Tree
        if "Awakened Tree" in npc.subrace:
            descriptor += ["Enlightened", "Sentient", "Alive", "Vigilant"]
            rank += ["Enlightened Tree", "Sentient Oak", "Alive Willow", "Vigilant Maple"]
            of_the += ["of the Enlightened Forest", "of the Sentient Woods", "of the Living Groves", "of the Vigilant Thicket"]

        # Forefather Oak
        if "Forefather Oak" in npc.subrace:
            descriptor += ["Venerable", "Mighty", "Respected", "Ancient"]
            rank += ["Venerable Oak", "Mighty Ancestor", "Respected Elder", "Ancient Tree"]
            of_the += ["of the Venerable Groves", "of the Mighty Woods", "of the Respected Forest", "of the Ancient Canopy"]

        # Myconid Sovereign
        if "Myconid Sovereign" in npc.subrace:
            descriptor += ["Fungal", "Mystical", "Spore-Crowned", "Sapient"]
            rank += ["Fungal King", "Mystical Sovereign", "Spore-Crowned Ruler", "Sapient Shroom"]
            of_the += ["of the Fungal Depths", "of the Mystical Undergrowth", "of the Spore-Crowned Kingdom", "of the Sapient Circles"]

        # Ent
        if "Ent" in npc.subrace:
            descriptor += ["Gentle", "Towering", "Speaking", "Leaf-Crowned"]
            rank += ["Gentle Giant", "Towering Ent", "Speaking Tree", "Leaf-Crowned Elder"]
            of_the += ["of the Whispering Forests", "of the Towering Groves", "of the Speaking Woods", "of the Leaf-Crowned Canopies"]

        # Treefolk
        if "Treefolk" in npc.subrace:
            descriptor += ["Bark-Skinned", "Stoic", "Nature's Child", "Rooted"]
            rank += ["Bark Guardian", "Stoic Oak", "Nature's Sentinel", "Rooted Wanderer"]
            of_the += ["of the Bark Forests", "of the Stoic Woods", "of the Nature's Embrace", "of the Rooted Paths"]

        # Floral Walkers
        if "Floral Walkers" in npc.subrace:
            descriptor += ["Petal", "Blossoming", "Vibrant", "Fragrant"]
            rank += ["Petal Guardian", "Blossoming Wanderer", "Vibrant Bloom", "Fragrant Protector"]
            of_the += ["of the Blossoming Fields", "of the Petal Meadows", "of the Vibrant Gardens", "of the Fragrant Trails"]

        # Living Totem
        if "Living Totem" in npc.subrace:
            descriptor += ["Sacred", "Totemic", "Carved", "Spiritual"]
            rank += ["Sacred Totem", "Totemic Guardian", "Carved Elder", "Spiritual Sentinel"]
            of_the += ["of the Sacred Groves", "of the Totemic Woods", "of the Carved Forests", "of the Spiritual Realms"]

        # Walker Vine
        if "Walker Vine" in npc.subrace:
            descriptor += ["Creeping", "Entangling", "Green", "Twisting"]
            rank += ["Creeping Vine", "Entangling Guardian", "Green Wanderer", "Twisting Creeper"]
            of_the += ["of the Creeping Jungles", "of the Entangling Canopies", "of the Green Vines", "of the Twisting Thickets"]

        # Singing Lotus
        if "Singing Lotus" in npc.subrace:
            descriptor += ["Harmonious", "Serene", "Melodic", "Waterborne"]
            rank += ["Bloom", "Lotus", "Flower", "Beauty"]
            of_the += ["of the Harmonious Ponds", "of the Serene Waters", "of the Melodic Streams", "of the Waterborne Gardens"]

        # Lichen Gravetaker
        if "Lichen Gravetaker" in npc.subrace:
            descriptor += ["Mournful", "Ethereal", "Silent", "Cryptic", "Fungal"]
            rank += ["Lichen", "Moss", "Guardian", "Cover", "Gravetaker"]
            of_the += ["of the Mournful Crypts", "of the Ethereal Graves", "of the Silent Tombs", "of the Cryptic Stones"]

        # Cactoid Nomad
        if "Cactoid Nomad" in npc.subrace:
            descriptor += ["Spiky", "Desert-Born", "Resilient", "Wandering"]
            rank += ["Spiky Protector", "Desert-Born Wanderer", "Resilient Cactus", "Wandering Thorn"]
            of_the += ["of the Spiky Deserts", "of the Resilient Sands", "of the Desert-Born Oasis", "of the Wandering Dunes"]

        # Vegetation Abomination
        if "Vegetation Abomination" in npc.subrace:
            descriptor += ["Twisted", "Malevolent", "Corrupted", "Unnatural"]
            rank += ["Twisted Horror", "Malevolent Growth", "Corrupted Vine", "Unnatural Entity"]
            of_the += ["of the Twisted Jungle", "of the Malevolent Thickets", "of the Corrupted Woods", "of the Unnatural Gardens"]

        # Dryad
        if "Dryad" in npc.subrace:
            descriptor += ["Enchanting", "Forest", "Mystical", "Nature-Spirit"]
            rank += ["Enchanting Dryad", "Forest Nymph", "Mystical Guardian", "Nature-Spirit"]
            of_the += ["of the Enchanted Woods", "of the Mystical Glades", "of the Forest Sanctuaries", "of the Nature Spirits' Realm"]

        # Fungical Intellectual
        if "Fungical Intellectual" in npc.subrace:
            descriptor += ["Sapient", "Learned", "Mycelial", "Thoughtful"]
            rank += ["Mushroom", "Fungi", "Scholar", "Spore"]
            of_the += ["of the Sapient Colonies", "of the Learned Undergrowth", "of the Mycelial Networks", "of the Thoughtful Groves"]

    # Undead Race and Subraces
    if "Undead" in npc.race:
        # General Undead descriptor, rank, and Of_the Phrases
        descriptor += ["Ethereal",
                       "Ghostly",
                       "Spectral",
                       "Deathly",
                       "Haunting",
                       "Eternal",
                       "Undead",
                       "Cursed"]
        rank += ["Warden",
                 "Guardian",
                 "Marauder",
                 "Overseer",
                 "Spirit"]
        of_the += ["of the Forgotten Crypts",
                   "of the Haunted Halls",
                   "of the Deathly Shadows",
                   "of the Spectral Realms",
                   "of the Ghostly Echoes"]

        # Death Knight
        if "Death Knight" in npc.subrace:
            descriptor += ["Armored", "Cursed", "Warrior", "Terrifying"]
            rank += ["Knight", "Terrifying Warlord", "Champion"]
            of_the += ["of the Cursed Battlefields",
                       "of the Armored Tombs",
                       "of the Terrifying Wars",
                       "of the Warrior's Curse"]

        # Honor Phantom
        if "Honor Phantom" in npc.subrace:
            descriptor += [
                "Ethereal",
                "Dutiful", "Honorable", "Ethereal", "Bound"]
            rank += ["Dutiful Specter", "Honorable Wraith", "Ethereal Sentinel", "Bound Spirit"]
            of_the += ["of the Honorable Deeds", "of the Dutiful Watch", "of the Ethereal Bonds", "of the Bound Duty"]

        # Regret Ghost
        if "Regret Ghost" in npc.subrace:
            descriptor += [
                "Ethereal",
                "Mournful",
                "Green",
                "Unresolved", "Sorrowful", "Pained"]
            rank += ["Mournful Apparition", "Unresolved Specter", "Sorrowful Ghost", "Pained Wraith"]
            of_the += ["of the Unresolved Matters", "of the Mournful Whispers", "of the Sorrowful Memories", "of the Pained Existence"]

        # Lich
        if "Lich" in npc.subrace:
            descriptor += ["Undying", "Arcane", "Malevolent", "Power-Hungry"]
            rank += ["Undying Mage", "Arcane Lich", "Malevolent Sorcerer", "Power-Hungry Necromancer"]
            of_the += ["of the Forbidden Spells", "of the Undying Will", "of the Arcane Secrets", "of the Malevolent Plans"]

        # Pride Mummy
        if "Pride Mummy" in npc.subrace:
            descriptor += ["Ancient", "Preserved", "Guardian", "Proud"]
            rank += ["Ancient Guardian", "Preserved Warrior", "Proud Protector", "Mummified Sentinel"]
            of_the += ["of the Ancient Tombs", "of the Preserved Crypts", "of the Proud Dynasties", "of the Guardian Mummies"]

        # Mischief Poltergeist
        if "Mischief Poltergeist" in creature_type:
            descriptor += [
                "Yellow",
                "Playful", "Mischievous", "Noisy", "Trickster"]
            rank += ["Playful Spirit", "Mischievous Ghost", "Noisy Phantom", "Trickster Apparition"]
            of_the += ["of the Haunted Houses", "of the Mischievous Antics", "of the Noisy Mansions", "of the Trickster's Lair"]

        # Vengeful Revenant
        if "Vengeful Revenant" in npc.subrace:
            descriptor += ["Revenge-Seeking", "Wrathful", "Resurrected", "Implacable"]
            rank += ["Revenge-Seeking Spirit", "Wrathful Wraith", "Resurrected Avenger", "Implacable Phantom"]
            of_the += ["of the Unrestful Graves", "of the Wrathful Shadows", "of the Resurrected Revenge", "of the Implacable Fury"]

        # Skeleton Protector
        if "Skeleton Protector" in creature_type:
            descriptor += ["Skeletal", "Undying", "Bone", "Guardian"]
            rank += [
                "Gargoyle",
                "Guardian", "Undying Sentinel", "Bone Warden", "Guardian of Bones"]
            of_the += ["of the Bone Crypts", "of the Skeletal Chambers", "of the Undying Vigil", "of the Guardian Tombs"]

        # Thinker Skull
        if "Thinker Skull" in npc.subrace:
            descriptor += ["Knowledgeable", "Cranial", "Ancient", "Wise"]
            rank += ["Knowledgeable Skull", "Cranial Sage", "Ancient Intellect", "Wise Cranium"]
            of_the += ["of the Ancient Lore", "of the Cranial Archives", "of the Wise Skulls", "of the Knowledgeable Tomes"]

        # Fear Shadow
        if "Fear Shadow" in npc.subrace:
            descriptor += ["Shadowy", "Fearful", "Dark", "Intangible"]
            rank += ["Shadowy Terror", "Fearful Apparition", "Dark Phantom", "Intangible Horror"]
            of_the += ["of the Dark Corners", "of the Fearful Nights", "of the Shadowy Realms", "of the Intangible Fear"]

        # Despair Specter
        if "Despair Specter" in npc.subrace:
            descriptor += [
                "Ethereal",
                "Despairing",
                "Green",
                "Sorrowful", "Gloomy", "Mournful"]
            rank += ["Despairing Wraith", "Sorrowful Ghost", "Gloomy Specter", "Mournful Shade"]
            of_the += ["of the Sorrowful Places", "of the Despairing Abyss", "of the Gloomy Shadows", "of the Mournful Echoes"]

        # Vampire
        if "Vampire" in npc.subrace:
            descriptor += [
                "Red",
                "Bloodthirsty", "Nocturnal", "Charismatic", "Immortal"]
            rank += ["Count", "Predator", "Fiend", "Sovereign"]
            of_the += [
                "of the Blood-Cursed Castles",
                "of the Nocturnal Hunts",
                "of the Charismatic Enchantment",
                "of the Immortal Nights",
                "of the Red Court",
                "of the Black Sun"]

        # Prideful Wight
        if "Prideful Wight" in npc.subrace:
            descriptor += ["Arrogant",
                           "Powerful",
                           "Dominating",
                           "Unyielding"]
            rank += ["Wight",
                     "Power",
                     "Specter",
                     "Ghoul"]
            of_the += ["of the Dominating Reign",
                       "of the Arrogant Thrones",
                       "of the Powerful Empires",
                       "of the Unyielding Grasp",
                       "of the Forgotten Pride",
                       "of the Eternal King"]

        # Cursed Eternal
        if "Cursed Eternal" in npc.subrace:
            descriptor += ["Cursed", "Eternal", "Mindless", "Hungering"]
            rank += ["Cursed Wanderer", "Eternal Hunger", "Mindless Horror", "Hungering Undead"]
            of_the += ["of the Cursed Eternity", "of the Eternal Night", "of the Mindless Hordes", "of the Hungering Shadows"]

        # Wraith
        if "Wraith" in npc.subrace:
            descriptor += ["Angry", "Vengeful", "Spectral", "Menacing"]
            rank += ["Angry Spirit", "Vengeful Wraith", "Spectral Terror", "Menacing Phantom"]
            of_the += ["of the Angry Haunts", "of the Vengeful Nights", "of the Spectral Abyss", "of the Menacing Shadows"]

        # Lone Lover
        if "Lone Lover" in npc.subrace:
            descriptor += [
                "Red",
                "Lovelorn", "Heartbroken", "Eternal", "Seeking"]
            rank += ["Lovelorn Ghost", "Heartbroken Specter", "Eternal Seeker", "Seeking Spirit"]
            of_the += ["of the Lost Love", "of the Heartbroken Tales", "of the Eternal Search", "of the Seeking Souls"]

        # Weeping Howler
        if "Weeping Howler" in npc.subrace:
            descriptor += ["Weeping", "Howling", "Mournful", "Ominous"]
            rank += ["Weeping Spirit", "Howling Phantom", "Mournful Wraith", "Ominous Apparition"]
            of_the += ["of the Weeping Moors", "of the Howling Winds", "of the Mournful Echos", "of the Ominous Nights"]

        # Tomb's Hoarder
        if "Tomb's Hoarder" in creature_type:
            descriptor += [
                "Greedy",
                "Obsessive",
                "Ancient",
                "Tomb"]
            rank += [
                "Gargoyle",
                "Guardian",
                "Wraith",
                "Keeper",
                "Hoarder"]
            of_the += [
                "of Greed",
                "of the Greedy Vaults",
                "of the Obsessive Collections",
                "of the Ancient Tombs",
                "of the Guarded Treasures"]

        # Penance Wraith
        if "Penance Wraith" in npc.subrace:
            descriptor += ["Repentant", "Suffering", "Tormented", "Redemptive"]
            rank += ["Repentant Spirit", "Suffering Phantom", "Tormented Soul", "Redemptive Ghost"]
            of_the += ["of the Suffering Shadows", "of the Repentant Pains", "of the Tormented Realms", "of the Redemptive Acts"]

        # Protector Spirit
        if "Protector Spirit" in npc.subrace:
            descriptor += [
                "Ethereal",
                "Guardian", "Vigilant", "Sacred", "Dutiful"]
            rank += ["Guardian Spirit", "Vigilant Phantom", "Sacred Wraith", "Dutiful Shade"]
            of_the += ["of the Sacred Grounds", "of the Guardian Realms", "of the Vigilant Watches", "of the Dutiful Protection"]
        # Vampire
        if "Vampire" in npc.subrace:
            descriptor += ["Nocturnal", "Bloodthirsty", "Seductive", "Immortal"]
            rank += ["Nocturnal Lord", "Bloodthirsty Predator", "Seductive Fiend", "Immortal Count"]
            of_the += ["of the Night's Embrace", "of the Blood Coven", "of the Seductive Shadows", "of the Immortal Realm"]

        # Prideful Wight
        if "Prideful Wight" in npc.subrace:
            descriptor += ["Haughty", "Imperious", "Undying", "Commanding"]
            rank += ["Haughty Wight", "Imperious Undead", "Undying Commander", "Commanding Revenant"]
            of_the += ["of the Haughty Tombs", "of the Imperious Ruins", "of the Undying Dominance", "of the Commanding Shadows"]

        # Cursed Eternal
        if "Cursed Eternal" in npc.subrace:
            descriptor += ["Accursed", "Eternal", "Tormented", "Relentless"]
            rank += ["Accursed Soul", "Eternal Wanderer", "Tormented Being", "Relentless Entity"]
            of_the += ["of the Accursed Curse", "of the Eternal Suffering", "of the Tormented Lands", "of the Relentless Pursuit"]

        # Wraith
        if "Wraith" in npc.subrace:
            descriptor += ["Shadowy", "Vengeful", "Ethereal", "Wrathful"]
            rank += ["Shadowy Wraith", "Vengeful Specter", "Ethereal Phantom", "Wrathful Spirit"]
            of_the += ["of the Shadowy Veil", "of the Vengeful Night", "of the Ethereal Abyss", "of the Wrathful Haunts"]

        # Lone Lover
        if "Lone Lover" in npc.subrace:
            descriptor += ["Romantic", "Forlorn", "Eternal", "Heartbroken"]
            rank += ["Romantic Spirit", "Forlorn Ghost", "Eternal Paramour", "Heartbroken Wraith"]
            of_the += ["of the Lost Loves", "of the Forlorn Hearts", "of the Eternal Longing", "of the Heartbroken Souls"]

        # Weeping Howler
        if "Weeping Howler" in npc.subrace:
            descriptor += ["Wailing", "Lamenting", "Howling", "Sorrowful"]
            rank += ["Wailing Phantom", "Lamenting Spirit", "Howling Apparition", "Sorrowful Ghost"]
            of_the += ["of the Wailing Winds", "of the Lamenting Moors", "of the Howling Hollows", "of the Sorrowful Shadows"]

        # Tomb's Hoarder
        if "Tomb's Hoarder" in npc.subrace:
            descriptor += ["Greedy", "Guardian", "Mausoleum", "Ancient"]
            rank += ["Greedy Keeper", "Guardian of Graves", "Mausoleum Warden", "Ancient Hoarder"]
            of_the += ["of the Greedy Depths", "of the Guarded Tombs", "of the Ancient Vaults", "of the Mausoleum's Secrets"]

        # Penance Wraith
        if "Penance Wraith" in npc.subrace:
            descriptor += ["Penitent", "Atoning", "Redeeming", "Contrite"]
            rank += ["Penitent Specter", "Atoning Spirit", "Redeeming Wraith", "Contrite Phantom"]
            of_the += ["of the Penitent Shadows", "of the Atoning Souls", "of the Redeeming Mist", "of the Contrite Echoes"]

        # Protector Spirit
        if "Protector Spirit" in npc.subrace:
            descriptor += ["Guardian", "Benevolent", "Ethereal", "Vigilant"]
            rank += ["Guardian Shade", "Benevolent Wraith", "Ethereal Protector", "Vigilant Ghost"]
            of_the += ["of the Sacred Grounds", "of the Benevolent Watch", "of the Ethereal Guard", "of the Vigilant Spirits"]

    if "Vampire" in creature_type:
        # descriptor for vampire names
        descriptor += [
            "Bloodsucking", "Bloodthirsty", "Bloody", "Nocturnal", "Ancient", "Mysterious", "Shadowy", 
            "Elegant", "Crimson", "Dread", "Eternal", "Forsaken", 
            "Ghastly", "Haunting", "Immortal", "Malevolent", "Nefarious", 
            "Ominous", "Pale", "Ravenous", "Sinister", "Unholy", 
            "Vengeful", "Whispering", "Exiled", "Enigmatic", "Spectral", 
            "Wraithlike"
        ]

        # rank for vampire names
        rank += [
            "Vampire", "Queen","Count", "Baron", "Lord", "Lady", 
            "Master", "Mistress", "Duke", "Duchess", "Overlord", 
            "Sovereign", "Nightwalker", "Shade", "Phantom", "Revenant", 
            "Necromancer", "Sire", "Matron", "Chieftain", "Guardian", 
            "Warlord",
            "Enchanter", "Seer", "Harbinger", 
            "Emissary",
           
        ]
        of_the += [
            "of the Blood",
            "of the Blood Court",

            ]
        #return f"The {random.choice(descriptor)} {random.choice(rank)} {random.choice(of_the)}"


    # Human Race and Subraces
    if "Human" in npc.race:
        # General Human descriptor, rank, and Of_the Phrases
        descriptor += [
            "Red",
            "Resourceful", "Diverse", "Adaptive", "Innovative", "Resilient"]
        rank += ["Village Elder", "City Dweller", "Wandering Nomad", "Learned Scholar", "Skilled Artisan"]
        of_the += ["of the Rural Lands", "of the Urban Streets", "of the Distant Shores", "of the Scholarly Halls", "of the Artisan Guilds"]

        # Local
        if "Local" in npc.subrace:
            descriptor += ["Native", "Familiar", "Homegrown", "Local"]
            rank += ["Local Merchant", "Native Artisan", "Familiar Face", "Homegrown Hero"]
            of_the += ["of the Native Soil", "of the Familiar Streets", "of the Local Taverns", "of the Homegrown Community"]

        # Foreigner
        if "Foreigner" in npc.subrace:
            descriptor += ["Foreign", "Exotic", "Distant", "Unfamiliar"]
            rank += ["Foreign Traveler", "Exotic Merchant", "Distant Wanderer", "Unfamiliar Visitor"]
            of_the += ["of Foreign Lands", "of Exotic Cultures", "of Distant Shores", "of Unfamiliar Territories"]

        # Exotic
        if "Exotic" in npc.subrace:
            descriptor += ["Mysterious", "Alluring", "Unique", "Fascinating"]
            rank += ["Mysterious Stranger", "Alluring Traveler", "Unique Individual", "Fascinating Outsider"]
            of_the += ["of the Mysterious East", "of the Alluring Jungles", "of the Unique Realms", "of the Fascinating Unknown"]

        # Well Dressed
        if "Well dressed" in npc.subrace:
            descriptor += ["Stylish", "Elegant", "Refined", "Dapper"]
            rank += ["Stylish Noble", "Elegant Diplomat", "Refined Scholar", "Dapper Gentleman"]
            of_the += ["of the High Courts", "of the Elegant Balls", "of the Refined Circles", "of the Dapper Societies"]

        # Humble
        if "Humble" in npc.subrace:
            descriptor += ["Modest", "Simple", "Unassuming", "Honest"]
            rank += ["Modest Farmer", "Simple Craftsman", "Unassuming Monk", "Honest Trader"]
            of_the += ["of the Modest Communities", "of the Simple Life", "of the Unassuming Faith", "of the Honest Dealings"]

        # Healthy
        if "Healthy" in npc.subrace:
            descriptor += ["Vigorous", "Robust", "Wholesome", "Lively"]
            rank += ["Vigorous Worker", "Robust Warrior", "Wholesome Healer", "Lively Performer"]
            of_the += ["of the Vigorous Fields", "of the Robust Battles", "of the Wholesome Villages", "of the Lively Markets"]

        # Strong
        if "Strong" in npc.subrace:
            descriptor += ["Powerful", "Muscular", "Sturdy", "Tough"]
            rank += ["Powerful Soldier", "Muscular Laborer", "Sturdy Craftsman", "Tough Mercenary"]
            of_the += ["of the Powerful Armies", "of the Muscular Guilds", "of the Sturdy Fortresses", "of the Tough Streets"]

        # Big
        if "Big" in npc.subrace:
            descriptor += ["Large", "Towering", "Hefty", "Bulk"]
            rank += ["Large Leader", "Towering Giant", "Hefty Brawler", "Bulk Trader"]
            of_the += ["of the Large Clans", "of the Towering Mountains", "of the Hefty Challenges", "of the Bulk Markets"]

        # Thin
        if "Thin" in npc.subrace:
            descriptor += ["Slim", "Lean", "Slight", "Graceful"]
            rank += ["Slim Scholar", "Lean Runner", "Slight Artist", "Graceful Dancer"]
            of_the += ["of the Slim Figures", "of the Lean Paths", "of the Slight Touches", "of the Graceful Movements"]

        # Athletic
        if "Athletic" in npc.subrace:
            descriptor += ["Fit", "Agile", "Energetic", "Sporty"]
            rank += ["Fit Warrior", "Agile Scout", "Energetic Performer", "Sporty Adventurer"]
            of_the += ["of the Fit Battalions", "of the Agile Hunts", "of the Energetic Shows", "of the Sporty Competitions"]

        # Sickly
        if "Sickly" in npc.subrace:
            descriptor += ["Frail", "Pallid", "Weak", "Ailing"]
            rank += ["Frail Hermit", "Pallid Alchemist", "Weak Scholar", "Ailing Mystic"]
            of_the += ["of the Frail Bodies", "of the Pallid Complexions", "of the Weak Spirits", "of the Ailing Souls"]

        # Pretty
        if "Pretty" in npc.subrace:
            descriptor += ["Beautiful", "Charming", "Attractive", "Lovely"]
            rank += ["Beautiful Bard", "Charming Artist", "Attractive Noble", "Lovely Poet"]
            of_the += ["of the Beautiful Faces", "of the Charming Courts", "of the Attractive Galleries", "of the Lovely Gardens"]

        # Rough
        if "Rough" in npc.subrace:
            descriptor += ["Rugged", "Tough", "Hardy", "Gruff"]
            rank += ["Rugged Outlander", "Tough Mercenary", "Hardy Sailor", "Gruff Miner"]
            of_the += ["of the Rugged Lands", "of the Tough Streets", "of the Hardy Seas", "of the Gruff Mountains"]

        # Elegant
        if "Elegant" in npc.subrace:
            descriptor += ["Graceful", "Sophisticated", "Refined", "Cultured"]
            rank += ["Graceful Diplomat", "Sophisticated Noble", "Refined Artist", "Cultured Scholar"]
            of_the += ["of the Graceful Estates", "of the Sophisticated Salons", "of the Refined Studios", "of the Cultured Academies"]

        # Old
        if "Old" in npc.subrace:
            descriptor += ["Elderly", "Wise", "Aged", "Venerable"]
            rank += ["Elderly Sage", "Wise Elder", "Aged Mentor", "Venerable Leader"]
            of_the += ["of the Elderly Wisdom", "of the Wise Traditions", "of the Aged Histories", "of the Venerable Ancestors"]

        # Young
        if "Young" in npc.subrace:
            descriptor += ["Youthful", "Energetic", "Fresh", "Vibrant"]
            rank += ["Youthful Adventurer", "Energetic Apprentice", "Fresh Talent", "Vibrant Artist"]
            of_the += ["of the Youthful Spirit", "of the Energetic Ventures", "of the Fresh Ideas", "of the Vibrant Communities"]

        # Attractive
        if "Attractive" in npc.subrace:
            descriptor += ["Handsome", "Fetching", "Alluring", "Striking"]
            rank += ["Handsome Courtier", "Fetching Trader", "Alluring Performer", "Striking Leader"]
            of_the += ["of the Handsome Visages", "of the Fetching Markets", "of the Alluring Stages", "of the Striking Figures"]

            
    # Elf Race and Subraces
    if "Elf" in npc.race:
        # General Elf descriptor, rank, and Of_the Phrases
        descriptor += ["Ethereal", "Graceful", "Ancient", "Mystical", "Agile"]
        rank += ["Elven Elder", "Mystic Archer", "Graceful Diplomat", "Ancient Sage", "Agile Scout"]
        of_the += ["of the Ancient Woods", "of the Ethereal Realms", "of the Mystic Rivers", "of the Graceful Valleys", "of the Agile Winds"]

        # High Elf
        if "High" in npc.subrace:
            descriptor += ["Noble", "Refined", "Elevated", "Scholarly"]
            rank += ["Noble High Elf", "Refined Magician", "Elevated Scholar", "High Mage"]
            of_the += ["of the Noble Courts", "of the Refined Arts", "of the Elevated Realms", "of the Scholarly Towers"]

        # Sylvan Elf
        if "Sylvan" in npc.subrace:
            descriptor += ["Green",
                           "Forest",
                           "Nature",
                           "Woodland",
                           "Green"]
            rank += ["Guardian",
                     "Enchanter"]
            of_the += ["of the Sylvan Groves",
                       "of the Forest Shadows",
                       "of the Woodland Paths",
                       "of the Green Canopies"]

        # Wood Elf
        if "Wood" in npc.subrace:
            descriptor += ["Green",
                           "Woodland",
                           "Earthy",
                           "Rustic",
                           "Natural",
                           "Wood"]
            rank += ["Scout",
                     "Hunter",
                     "Protector",
                     "Herbalist"]
            of_the += ["of the Woodland Glades",
                       "of the Earthy Forests",
                       "of the Rustic Thickets",
                       "of the Natural Springs"]

        # Dark Elf
        if "Dark" in npc.subrace:
            descriptor += ["Shadowy",
                           "Dark",
                           "Underworld",
                           "Mysterious",
                           "Stealthy"]
            rank += ["Elf"
                     ]
            of_the += ["of the Shadowy Depths",
                       "of the Underworld Caverns",
                       "of the Night",
                       "of the Raven Queen"]

        # Night Elf
        if "Night" in npc.subrace:
            descriptor += ["Astral",
                           "Nocturnal",
                           "Mystical",
                           "Shadow",
                           "Moonlit"]
            rank += ["Warrior",
                     "Enchanter",
                     "Ranger",
                     "Scout"]
            of_the += ["of the Nocturnal Forests",
                       "of the Mystical Moons",
                       "of the Moon Paths",
                       "of the Moonlit Glades",
                       "of the Moon",
                       "of the Stars"]

        # Feywild Elf
        if "Feywild" in npc.subrace:
            descriptor += ["Green",
                           "Fey-Touched",
                           "Enchanted",
                           "Otherworldly",
                           "Fairy"]
            rank += ["Mystic",
                     "Envoy",
                     "Wanderer"]
            of_the += ["of the Feywild Realms",
                       "of the Enchanted Woods",
                       "of the Otherworldly Visions",
                       "of the Fairylike Dreams"]

        # Shadow Elf
        if "Shadow" in npc.subrace:
            descriptor += ["Dark",
                           "Stealthy",
                           "Evasive",
                           "Obscured"]
            rank += ["Stalker",
                     "Assassin",
                     "Scout",
                     "Ranger"]
            of_the += ["of the Shadowed Alleys",
                       "of the Dark Realms",
                       "of the Evasive Tactics",
                       "of the Obscured Mysteries"]

        # Sea Elf
        if "Sea" in npc.subrace:
            descriptor += ["Aquatic", "Maritime", "Oceanic", "Coastal"]
            rank += ["Aquatic Hunter", "Maritime Explorer", "Oceanic Guardian", "Coastal Druid"]
            of_the += ["of the Aquatic Depths", "of the Maritime Shores", "of the Oceanic Wonders", "of the Coastal Havens"]

        # Nomadic Elf
        if "Nomadic" in npc.subrace:
            descriptor += ["Wandering", "Traveling", "Adventurous", "Roaming"]
            rank += ["Wandering Nomad", "Traveling Bard", "Adventurous Scout", "Roaming Mystic"]
            of_the += ["of the Wandering Tribes", "of the Traveling Caravans", "of the Adventurous Paths", "of the Roaming Lands"]

        # Snow Elf
        if "Snow" in npc.subrace:
            descriptor += ["Frosty", "Winterborn", "Chill", "Icy"]
            rank += ["Frosty Ranger", "Winterborn Mage", "Chill Sentinel", "Icy Scout"]
            of_the += ["of the Frosty Peaks", "of the Winterborn Forests", "of the Chill Tundras", "of the Icy Rivers"]

        # Sun Elf
        if "Sun" in creature_type:
            descriptor += [
                "Ethereal",
                "Yellow",
                "Sunlit", "Radiant", "Bright", "Solar"]
            rank += ["Sunlit Warrior", "Radiant Enchanter", "Bright Archer", "Solar Guardian"]
            of_the += ["of the Sunlit Glades", "of the Radiant Valleys", "of the Bright Skies", "of the Solar Realms"]

        # Eclipse Elf
        if "Eclipse" in creature_type:
            descriptor += [
                "Astral",
                "Ethereal",
                "Twilight",
                "Eclipsed",
                "Shadowed",
                "Celestial"]
            rank += [
                "",
                ]
            of_the += ["of the Twilight Forests", "of the Eclipsed Moons", "of the Shadowed Paths", "of the Celestial Alignments"]

        # Moon Elf
        if "Moon" in creature_type:
            descriptor += [
                "Astral",
                "Lunar",
                "Moonlit",
                "Nocturnal",
                "Starry",
                ]
            rank += [
                "Mystic",
                "Ranger",
                "Scout",
                "Seer",
                ]
            of_the += [
                "of the Lunar Lakes",
                "of the Moonlit Woods",
                "of the Nocturnal Groves",
                "of the Starry Skies"]

        # Wild Elf
        if "Wild" in creature_type:
            descriptor += ["Green",
                           "Untamed", "Feral", "Savage", "Free"]
            rank += ["Untamed Warrior", "Feral Hunter", "Savage Druid", "Free Spirit"]
            of_the += ["of the Untamed Lands", "of the Feral Jungles", "of the Savage Plains", "of the Free Forests"]

        # Urban Elf
        if "Urban" in npc.subrace:
            descriptor += [
                "Cityzen", "Metropolitan", "Sophisticated", "Civic"]
            rank += ["Scholar", "Metropolitan Artist", "Sophisticated Diplomat", "Civic Leader"]
            of_the += ["of the City Lights", "of the Metropolitan Melting Pots", "of the Sophisticated Societies", "of the Civic Hubs"]

        # Sands Elf
        if "Sands" in npc.subrace:
            descriptor += ["Desert", "Sand-Worn", "Dune", "Arid"]
            rank += ["Desert Nomad", "Sand-Worn Scout", "Dune Wanderer", "Arid Survivor"]
            of_the += ["of the Desert Expanse", "of the Sand-Worn Trails", "of the Dune Seas", "of the Arid Wastelands"]
    # Dwarf Race and Subraces
    if "Dwarf" in npc.race:
        # General Dwarf descriptor, rank, and Of_the Phrases
        descriptor += [
            "Red",
            "Clan",
            "Dwarven",
            "Master",
            "Stout", "Bearded", "Resilient", "Earthy", "Crafty"]
        rank += ["Elder", "Smith", "Deep Miner", "Crafty Artisan"]
        of_the += ["of the Mountain Halls", "of the Earthy Depths", "of the Stout Clans", "of the Crafty Guilds", "of the Resilient Folk"]

        # Mountain Dwarf
        if "Mountain" in npc.subrace:
            descriptor += ["Rocky", "Highland", "Sturdy", "Traditional"]
            rank += ["Rocky Guardian", "Highland Brewer", "Sturdy Miner", "Traditional Elder"]
            of_the += ["of the Rocky Peaks", "of the Highland Caverns", "of the Sturdy Mines", "of the Traditional Keeps"]

        # Conquistador Dwarf
        if "Conquistador" in npc.subrace:
            descriptor += [
                "Golden Sun's",
                "Adventurous", "Explorer", "Conqueror", "Bold"]
            rank += ["Adventurous Pioneer", "Explorer Captain", "Conqueror Hero", "Bold Leader"]
            of_the += ["of the New Frontiers", "of the Adventurous Expeditions", "of the Conquered Lands", "of the Bold Ventures"]

        # Seawolf Dwarf
        if "Seawolf" in npc.subrace:
            descriptor += ["Maritime", "Seafaring", "Oceanic", "Sailor"]
            rank += ["Maritime Captain", "Seafaring Navigator", "Oceanic Warrior", "Sailor Adventurer"]
            of_the += ["of the Oceanic Voyages", "of the Seafaring Journeys", "of the Maritime Adventures", "of the Sailor's Seas"]

        # Tinkerer Dwarf
        if "Tinkerer" in npc.subrace:
            descriptor += ["Inventive", "Mechanical", "Innovative", "Skillful"]
            rank += ["Inventive Engineer", "Mechanical Genius", "Innovative Artisan", "Skillful Mechanic"]
            of_the += ["of the Inventive Labs", "of the Mechanical Workshops", "of the Innovative Designs", "of the Skillful Creations"]

        # Roadbarter Dwarf
        if "Roadbarter" in npc.subrace:
            descriptor += ["Traveling", "Trader", "Wandering", "Merchant"]
            rank += ["Traveling Salesman", "Trader Explorer", "Wandering Merchant", "Roadbarter Adventurer"]
            of_the += ["of the Traveling Caravans", "of the Trader Routes", "of the Wandering Bazaars", "of the Roadbarter Paths"]

        # Urbanite Dwarf
        if "Urbanite" in npc.subrace:
            descriptor += ["City", "Sophisticated", "Urban", "Cultured"]
            rank += ["City Craftsman", "Sophisticated Artisan", "Urban Miner", "Cultured Diplomat"]
            of_the += ["of the City Forges", "of the Sophisticated Guilds", "of the Urban Underbelly", "of the Cultured Districts"]

        # Stonemason Dwarf
        if "Stonemason" in npc.subrace:
            descriptor += ["Mason", "Carver", "Sculptor", "Artisan"]
            rank += ["Master Mason", "Carver of Runes", "Sculptor of Stone", "Artisan of Rock"]
            of_the += ["of the Mason's Hall", "of the Carved Mountains", "of the Sculptor's Studio", "of the Artisan's Workshop"]

        # Dark Dwarf
        if "Dark" in npc.subrace:
            descriptor += ["Shadowed", "Gloomy", "Underworld", "Mysterious"]
            rank += ["Shadowed Miner", "Gloomy Forger", "Underworld Scout", "Mysterious Enchanter"]
            of_the += ["of the Shadowed Depths", "of the Gloomy Tunnels", "of the Underworld Caverns", "of the Mysterious Realms"]

        # Crystal Cavern Dwarf
        if "Crystal Cavern" in npc.subrace:
            descriptor += ["Crystalline", "Shimmering", "Luminous", "Gleaming"]
            rank += ["Crystalline Miner", "Shimmering Artisan", "Luminous Explorer", "Gleaming Carver"]
            of_the += ["of the Crystal Mines", "of the Shimmering Depths", "of the Luminous Caverns", "of the Gleaming Halls"]

        # Canyon Dweller Dwarf
        if "Canyon Dweller" in npc.subrace:
            descriptor += ["Rugged", "Cliffside", "Canyon", "Open-Air"]
            rank += ["Rugged Scout", "Cliffside Forger", "Canyon Explorer", "Open-Air Miner"]
            of_the += ["of the Rugged Cliffs", "of the Cliffside Forges", "of the Canyon Depths", "of the Open-Air Quarries"]

        # Bank Templar Dwarf
        if "Bank Templar" in npc.subrace:
            descriptor += ["Wealthy", "Secure", "Guardian", "Honorable"]
            rank += ["Wealthy Guardian", "Secure Banker", "Honorable Protector", "Vault Keeper"]
            of_the += ["of the Wealthy Vaults", "of the Secure Banks", "of the Honorable Safeguards", "of the Protected Treasures"]

        # Forgeclan Dwarf
        if "Forgeclan" in npc.subrace:
            descriptor += ["Smithing", "Fiery", "Industrious", "Metallic"]
            rank += ["Smithing Master", "Fiery Artisan", "Industrious Worker", "Metallic Forger"]
            of_the += ["of the Smithing Halls", "of the Fiery Forges", "of the Industrious Workshops", "of the Metallic Creations"]
        # Bank Templar
        if "Bank Templar" in npc.subrace:
            descriptor += ["Vigilant", "Guardian", "Honorable", "Wealthy"]
            rank += ["Vigilant Keeper", "Guardian of Wealth", "Honorable Defender", "Wealthy Protector"]
            of_the += ["of the Sacred Vaults", "of the Guardian Banks", "of the Honorable Temples", "of the Wealthy Treasuries"]

        # Forgeclan
        if "Forgeclan" in npc.subrace:
            descriptor += ["Fiery", "Crafty", "Industrious", "Metal-Bound"]
            rank += ["Fiery Smith", "Crafty Artisan", "Industrious Worker", "Metal-Bound Warrior"]
            of_the += ["of the Fiery Forges", "of the Crafty Workshops", "of the Industrious Clans", "of the Metal-Bound Guilds"]

    # Lizardfolk Race and Subraces
    if "Lizardfolk" in creature_type:
        # General Lizardfolk descriptor, rank, and Of_the Phrases
        descriptor += [
            "Red",
            "Scaly",
            "Yellow",
            "Green",
            
            "Cold-Blooded", "Reptilian", "Stealthy", "Primitive"]
        rank += ["Scaly Hunter", "Reptilian Shaman", "Cold-Blooded Warrior", "Stealthy Tracker", "Primitive Chieftain"]
        of_the += ["of the Reptilian Marshes", "of the Scaly Jungles", "of the Cold-Blooded Tribes", "of the Stealthy Bogs", "of the Primitive Lands"]

        # Swamp Crocfolk
        if "Swamp Crocfolk" in npc.subrace:
            descriptor += ["Aquatic", "Toothy", "Menacing", "Powerful"]
            rank += ["Aquatic Predator", "Toothy Guardian", "Menacing Leader", "Powerful Crocfolk"]
            of_the += ["of the Swamp Waters", "of the Toothy Caverns", "of the Menacing Bogs", "of the Powerful Rivers"]

        # Jungle Guanafolk
        if "Jungle Guanafolk" in npc.subrace:
            descriptor += ["Vibrant", "Agile", "Tropical", "Cunning"]
            rank += ["Vibrant Scout", "Agile Hunter", "Tropical Guardian", "Cunning Warrior"]
            of_the += ["of the Vibrant Canopies", "of the Agile Branches", "of the Tropical Jungles", "of the Cunning Undergrowth"]

        # Desertic Horned
        if "Desertic Horned" in npc.subrace:
            descriptor += ["Desert", "Horned", "Enduring", "Rugged"]
            rank += ["Desert Survivor", "Horned Nomad", "Enduring Wanderer", "Rugged Fighter"]
            of_the += ["of the Desert Expanse", "of the Horned Dunes", "of the Enduring Sands", "of the Rugged Wastelands"]

        # Dune Dino
        if "Dune Dino" in npc.subrace:
            descriptor += ["Dune", "Ancient", "Fossilized", "Mighty"]
            rank += ["Dune Warrior", "Ancient Tracker", "Fossilized Guardian", "Mighty Hunter"]
            of_the += ["of the Dune Seas", "of the Ancient Deserts", "of the Fossilized Valleys", "of the Mighty Wastes"]

        # White Albino
        if "White Albino" in npc.subrace:
            descriptor += ["Pale", "Albino", "Ghostly", "Rare"]
            rank += ["Pale Stalker", "Albino Hunter", "Ghostly Wanderer", "Rare Vision"]
            of_the += ["of the Pale Shadows", "of the Albino Enclaves", "of the Ghostly Realms", "of the Rare Sightings"]

        # Feathered Dinofolk
        if "Feathered Dinofolk" in npc.subrace:
            descriptor += ["Feathered", "Prehistoric", "Majestic", "Swift"]
            rank += ["Feathered Scout", "Prehistoric Warrior", "Majestic Hunter", "Swift Runner"]
            of_the += ["of the Feathered Jungles", "of the Prehistoric Lands", "of the Majestic Canopies", "of the Swift Rivers"]

        # Colored Chamalfolk
        if "Colored Chamalfolk" in npc.subrace:
            descriptor += ["Chameleon", "Colorful", "Adaptive", "Camouflaged"]
            rank += ["Chameleon Scout", "Colorful Hunter", "Adaptive Warrior", "Camouflaged Guardian"]
            of_the += ["of the Colorful Forests", "of the Chameleon Jungles", "of the Adaptive Underbrush", "of the Camouflaged Terrains"]

        # Titan Rex
        if "Titan Rex" in npc.subrace:
            descriptor += ["Titanic", "Fearsome", "Dominant", "Colossal"]
            rank += ["Titanic Leader", "Fearsome Predator", "Dominant Hunter", "Colossal Beast"]
            of_the += ["of the Colossal Cliffs", "of the Titanic Jungles", "of the Fearsome Territories", "of the Dominant Realms"]

        # Tundra Saurius
        if "Tundra Saurius" in npc.subrace:
            descriptor += ["Icy", "Frosty", "Cold-Resistant", "Tundra"]
            rank += ["Icy Tracker", "Frosty Guardian", "Cold-Resistant Hunter", "Tundra Wanderer"]
            of_the += ["of the Icy Wastes", "of the Frosty Peaks", "of the Cold-Resistant Tribes", "of the Tundra Expanse"]

        # Turtlefolk
        if "Turtlefolk" in npc.subrace:
            descriptor += ["Shell-Backed", "Steady", "Aquatic", "Guardian"]
            rank += ["Shell-Backed Protector", "Steady Guardian", "Aquatic Warrior", "Guardian of the Depths"]
            of_the += ["of the Shell-Covered Shores", "of the Steady Streams", "of the Aquatic Havens", "of the Deep Waters"]

        # Frogfolk
        if "Frogfolk" in npc.subrace:
            descriptor += ["Amphibious", "Leaping", "Croaking", "Swamp-Dweller"]
            rank += ["Amphibious Scout", "Leaping Warrior", "Croaking Mystic", "Swamp-Dwelling Shaman"]
            of_the += ["of the Amphibious Marshes", "of the Leaping Rivers", "of the Croaking Jungles", "of the Swampy Enclaves"]

    if "Kobold" in creature_type:
        descriptor = [
            "Cunning",
            "Small",
            "Agile",
            "Crafty",
            "Sneaky",
            ]
        rank = [
            "Kobold",
            ]
        of_the = [
            "of the Dragon",
            f"of the {random.choice(descriptor)} Dragon",
            "of the Cunning Warrens",
            f"of the {random.choice(descriptor)} Tribe",
            f"of the {random.choice(descriptor)} Enclaves",
            f"of the {random.choice(descriptor)} Paths"
            ]

        Colors = [ "Black","Blue",
                   "Green", "Red","White","Bronze","Silver",
                  "Gold","Brass","Copper","Shadow","Gem","Prismatic", "Amber",
                   "Yellow",]
        descriptor += Colors
        for color in Colors:
            if color in creature_type:
                descriptor += [f"{color} Scaled", f"{color} Clawed", f"{color} Eyed", f"{color} Crested"]
                rank += [f"{color} Scale Scout", f"{color} Claw Warrior", f"{color} Eye Sorcerer", f"{color} Crest Shaman"]
                of_the += [f"of the {color} Scale Lairs", f"of the {color} Claw Clans", f"of the {color} Eye Covens", f"of the {color} Crest Packs"]
                descriptor += [f"{color} Scaled", f"Metallic {color}", f"Shining {color}", f"Lustrous {color}"]
                rank += [f"{color} Scale Artisan", f"Metallic {color} Guardian", f"Shining {color} Smith", f"Lustrous {color} Sage"]
                of_the += [f"of the {color} Scaled Forges", f"of the Metallic {color} Bastions", f"of the Shining {color} Workshops", f"of the Lustrous {color} Libraries"]
                descriptor += [f"{color} Aura", f"Mystical {color}", f"Enigmatic {color}", f"Arcane {color}"]
                rank += [f"{color} Aura Scout", f"Mystical {color} Enchanter", f"Enigmatic {color} Trickster", f"Arcane {color} Sage"]
                of_the += [
                    f"of the {color} Aura",
                    f"of the {color} Shadows",
                    f"of the {color} Kingdom",
                    f"of the {color} Realms",
                    f"of the {color} Enclaves",
                    f"of the {color} Fire",
                    f"of the {color} Dragon",
                    f"of the {color} Death",
                    f"of the {color} Master",
                    f"of the Arcane {color} Sanctuaries"]


    # Backgrounds
    if "Bandit" in creature_type:
        descriptor = [
            "Ruthless",
            "Cunning",
            "Sly",
            "Daring",
            "Fierce",
            "Brave",
            "Skilled",
            "Mercilless",
            "Hidden",
            "Silent",
            "Lawless",
            "Treacherous",
            ]
        rank = [
            "Bandit",
            "Leader",
            "Thief",
            "Brigand",
            "Outlaw",
            "Raider",
            ]
        of_the = [
            "of the Hideouts",
            "of the Shadows",
            f"of the {random.choice(descriptor)} Lands",
            f"of the {random.choice(descriptor)} Roads",
            "of the Road",
            "of the Wild"]


            
    if "Scholar" in creature_type:


        # descriptor for Scholar names
        descriptor += [
            "Astral",
            "Learned", "Wise", "Erudite", "Sage", "Insightful", 
            "Astute", "Knowledgeable", "Savant", "Scholarly", "Philosophic",
            "Studious", "Enlightened", "Inquisitive", "Cultured", "Illuminated",
            "Intellectual", "Analytical", "Thoughtful", "Perceptive", "Inventive",
            "Academic", "Bookish", "Curious", "Intuitive", "Profound"
        ]

        # rank for Scholar names
        rank += [
            "Scholar", "Philosopher", "Librarian", "Archivist", "Professor",
            "Academician", "Historian", "Alchemist", "Astronomer", "Scribe",
            "Theorist", "Logician", "Ethnographer", "Linguist", "Lorekeeper",
            "Naturalist", "Metaphysicist", "Researcher", "Mystic", "Instructor",
            "Analyst", "Savant", "Curator", "Mastermind"
        ]
        
        # 'Of the' phrases for Scholar names
        of_the += [
            "of the Academy", "of the Ancient Scrolls", "of the Hidden Lore", "of the Arcane Secrets",
            "of the Lost Library", "of the Philosophers", "of the Astral Studies", "of the Eldritch Truth",
            "of the Forbidden Knowledge", "of the Alchemical Mysteries", "of the Historical Chronicles",
            "of the Mythic Tales", "of the Cryptic Codes", "of the Learned Society", "of the Mystic Arts",
            "of the Elemental Theory", "of the Celestial Observations", "of the Ethereal Plane", "of the Sages"
        ]
        
        
    if npc.race == "Elemental":
        descriptor += [
            "Red",
            "Air",
            "Fire",
            "Watter",
            "Rock",
            "Earth",
            "Storm",
            "Aerial",
            "Yellow",
            "Green",
            "Inferno", "Tidal", "Terra", "Frost", "Magma",
            "Gale", "Flame", "Aqua", "Stone", "Blizzard",
            "Lava", "Zephyr", "Pyro", "Hydro", "Geo",
            "Glacial", "Volcanic", "Breeze", "Ember", "Marine",
            "Pebble", "Whirlwind", "Scorch", "Oceanic", "Mountain"
            ]
        rank += [
            "Bender",
            "Elemental", "Guardian", "Warden", "Spirit", "Master",
            "Protector", "Overseer", "Champion", "Sentinel", "Shaper",
            "Keeper", "Lord", "Sovereign", "Ruler", "Conjurer",
            "Elder", "Invoker", "Creator", "Sage", "Harbinger",
            "Watcher", "Archon", "Mystic", "Enforcer", "Manipulator"
            ]
        of_the += [
            "of Air",
            "of Fire",
            "of Watter",
            "of Earth",
            "of the Tempest",
            "of the Inferno", "of the Tides", "of the Mountains", "of the Frost", "of the Magma",
            "of the Gale", "of the Flames", "of the Depths", "of the Stones", "of the Snow",
            "of the Lava", "of the Zephyrs", "of the Pyres", "of the Rivers", "of the Lands",
            "of the Glaciers", "of the Volcanoes", "of the Breezes", "of the Embers", "of the Seas",
            "of the Rocks", "of the Whirlwinds", "of the Scorching Heat", "of the Oceanic Expanse", "of the Mountain Peaks"
            ]
    # Atlantian
    if npc.subrace == "Atlantian":
        descriptor += ["Aquatic", "Ancient", "Deepsea", "Nautical", "Ruinbound"]
        rank += ["Guardian", "Explorer", "Sage", "Keeper", "Navigator"]
        of_the += ["of the Deep", "of the Sunken Cities", "of the Oceanic Ruins", "of the Ancient Waters", "of the Sea Mysteries"]

    # Cronusian
    if "Cronusian" in creature_type:
        descriptor += [
            "Ageless",
            "Timebound",
            "Epochal",
            "Hourglass",
            "Eternal"]
        rank += [
            "Chronomaster",
            "Timekeeper",
            "Oracle",
            "Elder",
            "Historian"]
        of_the += [
            "of the Ages",
            "of the Timeless Realms",
            "of the Eternal Clock",
            "of the Past and Future",
            "of the Ageless Wisdom"]

    # Eosian
    if npc.subrace == "Eosian":
        descriptor += ["Dawnbringer", "Radiant", "Morning", "Daybreak", "Sunlit"]
        rank += ["Dawnlord", "Sun Priest", "Lightbringer", "Horizon Walker", "Daykeeper"]
        of_the += ["of the First Light", "of the Rising Sun", "of the New Day", "of the Morning Skies", "of the Dawn's Promise"]

    # Genasi
    elif npc.subrace == "Genasi":
        descriptor += ["Elemental", "Natural", "Primal", "Essence", "Core"]
        rank += ["Elementalist", "Nature Guardian", "Force Wielder", "Primal Sage", "Essence Keeper"]
        of_the += ["of the Four Elements", "of the Primal Forces", "of the Elemental Essence", "of the Natural Order", "of the Elemental Harmony"]

    # Genie
    elif npc.subrace == "Genie":
        descriptor += ["Mystical", "Wondrous", "Ancient", "Boundless", "Enigmatic"]
        rank += ["Genie Lord", "Wishmaster", "Arcane Sovereign", "Eternal Spirit", "Mystic Ruler"]
        of_the += ["of the Ancient Wishes", "of the Mystic Sands", "of the Boundless Realms", "of the Eternal Flames", "of the Arcane Mysteries"]

    # Gaians
    elif npc.subrace == "Gaians":
        descriptor += ["Earth ", "Earthbound", "Stoneheart", "Terran", "Grovekeeper", "Nature's"]
        rank += ["Lord", "Sage", "Terramancer", "Guardian", "Voice"]
        of_the += ["of the Deep Earth", "of the Ancient Groves", "of the Mountain's Heart", "of the Earthen Core", "of the Nature's Embrace"]

    # Hyperian
    elif npc.subrace == "Hyperian":
        descriptor += ["Solar", "Luminous", "Sunfire", "Daystar", "Radiance", "Radiant", "Solar"]
        rank += ["Sunlord", "Lightweaver", "Master", "Sage", "Daystar Keeper"]
        of_the += ["of the Solar Flares", "of the Luminous Expanse", "of the Radiant Spheres", "of the Sun's Core", "of the Daylight"]

    # Oceanians
    elif npc.subrace == "Oceanians":
        descriptor += ["Tidal", "Stormborn", "Deepblue", "Wave Rider", "Seafarer"]
        rank += ["Tide Master", "Storm Lord", "Ocean Sage", "Wave Whisperer", "Sea Captain"]
        of_the += ["of the Tidal Forces", "of the Stormy Seas", "of the Ocean Depths", "of the Raging Waves", "of the Endless Ocean"]

    # Primordial
    elif npc.subrace == "Primordial":
        descriptor += ["Fundamental", "Origin", "Primeval", "Core Essence", "Elemental Root"]
        rank += ["Primeval Lord", "Origin Master", "Core Shaper", "Elemental Founder", "Reality Weaver"]
        of_the += ["of the Fundamental Forces", "of the Origin Point", "of the Elemental Roots", "of the Primeval Essence", "of the Core Reality"]

    # Promethean
    if npc.subrace == "Promethean":
        descriptor += ["Flamebearer", "Innovator", "Firemind", "Sparkmaster", "Blaze","Spirit",
                        "Electric","Spark","Fire", "Flame" ]
        rank += ["Lord", "Keeper", "Innovator Sage", "Spark Commander", "Blaze Master"]
        of_the += ["of the Eternal Flame", "of the Spark of Innovation", "of the Blazing Spirit", "of the Fire's Heart", "of the Innovator's Mind"]

    if npc.subrace == "Salamandrian":
        descriptor += ["Flamebearer", "Firemind", "Blaze","Spirit", "Fire",
                        "Electric","Spark","Fire", "Flame", "Fiery", "Emberheart","Ember"
                        "Flamekin", "Infernoborn", "Scorch" , "Flame"]
        rank += ["Lord", "Keeper", "Innovator Sage", "Spark Commander", "Blaze Master",
                    "Master", "Warden", "Sage", "Captain"]
        of_the += ["of the Eternal Flame", "of the Spark of Innovation",
                   "of the Blazing Spirit", "of the Fire's Heart",
                   "of the Blazing Inferno", "of the Ember Fields", "of the Flame Realms",
                   "of the Scorching Heat", "of the Fiery Depths"]

    if npc.subrace == "Titan":
        descriptor += ["Colossal", "Mighty", "Behemoth", "Gargantuan", "Power"]
        rank += ["Titan Lord", "Colossus Master", "Behemoth Keeper", "Gargantua Ruler", "Power Sovereign"]
        of_the += ["of the Titans", "of the Colossal Might", "of the Behemoth's Roar", "of the Other Realm"]


    if npc.background == "Cleric":
        of_the += [
            "of the Abbey", "of the Sacred Light", "of the Divine Order", "of the Holy Quest",
            "of the Eternal Flame", "of the Celestial Choir", "of the Hallowed Shrine", "of the Sacred Scrolls",
            "of the Divine Will", "of the Chosen Path", "of the Pilgrimage", "of the Faithful",
            "of the Covenant", "of the Ancient Rites", "of the Divine Mystery", "of the Prophetic Vision",
            "of the Blessed Waters", "of the Heavenly Host", "of the Sacred Oath", "of the Divine Harmony"
        ]
        descriptor += [
            "Blessed", "Holy", "Devout", "Pious", "Virtuous", 
            "Anointed", "Sanctified", "Righteous", "Divine", "Spiritual",
            "Celestial", "Sacred", "Zealous", "Faithful", "Chosen",
            "Enlightened", "Redeemed", "Prophetic", "Miracle-working", "Apostolic",
            "Ethereal", "Seraphic", "Angelical", "Mystic", "Reverent"
            ]
        rank += [
            "Cleric", "Priest", "High Priest", "Archpriest", "Bishop", 
            "Monk", "Nun", "Paladin", "Prophet", "Acolyte", 
            "Deacon", "Cardinal", "Chaplain", "Curate", "Missionary",
            "Abbess", "Abbott", "Hermit", "Friar", "Mystic",
            "Theurgist", "Vicar", "Parson", "Elder", "Preacher"
            ]


        #return f"The {random.choice(descriptor)} {random.choice(rank)} {random.choice(of_the)}"

    if npc.background == "Artist":
        descriptor = [
            "Red",
            "Creative", "Expressive", "Imaginative", "Artistic", "Innovative"]
        rank = ["Master Painter", "Skilled Sculptor", "Renowned Musician", "Gifted Poet", "Eccentric Performer"]
        of_the = ["of the Colorful Canvases", "of the Sculpted Masterpieces", "of the Melodic Harmonies", "of the Poetic Verses", "of the Theatrical Arts"]

    if npc.background == "Bandit":
        descriptor = [
            "Ruthless", "Cunning", "Sly", "Daring", "Fierce"]
        rank = ["Bandit Leader", "Skilled Thief", "Merciless Brigand", "Clever Outlaw", "Fierce Raider"]
        of_the = ["of the Hidden Hideouts", "of the Silent Shadows", "of the Lawless Lands", "of the Treacherous Roads", "of the Wild Frontiers"]

    if "Bard" in creature_type:
        descriptor = [
            "Ancient",
            "Enchanting",
            "Charismatic",
            "Clever",
            "Talented", "Storytelling", "Melodic", "Witty"]
        rank = [
            "Master",
            "Storyteller",
            "Musician",
            "Lyricist",
            "Performer",
            "Troubadour",
            ]
        of_the = [
            f"of the {random.choice(descriptor)} Ballads",
            f"of the {random.choice(descriptor)} Tales", "of the Melodic Chords", "of the Witty Verses", "of the Captivating Performances"]

    if npc.background == "Barbarian":
        # descriptor for the Barbarian background
        descriptor = ["Fierce", "Savage", "Untamed", "Mighty", "Warlike"]
        
        # rank for the Barbarian background
        rank = ["Warrior Chief", "Savage Fighter", "Mighty Berserker", "Untamed Conqueror", "Fearless Raider"]
        
        # 'Of the' phrases for the Barbarian background
        of_the = [
            "of the Wild Tribes", "of the Savage Lands", "of the Untamed Mountains", "of the Mighty Clans", "of the Fearless Raids"]

    # Background: Berserker
    if npc.background == "Berserker":
        descriptor = ["Raging", "Wild", "Frenzied", "Unstoppable", "Ferocious"]
        rank = ["Raging Warrior", "Wild Berserker", "Frenzied Fighter", "Unstoppable Force", "Ferocious Mauler"]
        of_the = ["of the Raging Storms", "of the Wild Frontiers", "of the Frenzied Battles", "of the Unstoppable Fury", "of the Ferocious Roar"]

    # Background: Charlatan
    if npc.background == "Charlatan":
        descriptor = ["Deceptive", "Charming", "Sly", "Cunning", "Smooth-Talking"]
        rank = ["Master Con Artist", "Charming Trickster", "Sly Fox", "Cunning Deceiver", "Smooth Scammer"]
        of_the = ["of the Deceptive Guises", "of the Charming Facades", "of the Sly Maneuvers", "of the Cunning Plots", "of the Smooth Words"]

    # Background: Cleric
    if npc.background == "Cleric":
        descriptor = [
            "Devout",
            "Holy",
            "Spiritual",
            "Righteous",
            "Blessed"]
        rank = [
            "Oracle",
            "Priest",
            "Healer",
            "Guide",
            "Crusader",
            "Acolyte"]
        of_the = [
            "of the Holy Order",
            "of the Order",
            "of the Mission",
            "of the Journey",
            "of the Path",
            "of the Light"]

    # Background: Crafter
    if npc.background == "Crafter":
        descriptor = ["Skillful", "Artisanal", "Creative", "Dexterous", "Inventive"]
        rank = ["Master Craftsman", "Artisanal Genius", "Creative Builder", "Dexterous Maker", "Inventive Creator"]
        of_the = ["of the Skillful Hands", "of the Artisanal Workshops", "of the Creative Designs", "of the Dexterous Creations", "of the Inventive Minds"]

    # Background: Criminal
    if npc.background == "Criminal":
        descriptor = ["Underworld", "Sneaky", "Ruthless", "Shady", "Clever"]
        rank = ["Crime Lord", "Sneaky Thief", "Ruthless Assassin", "Shady Dealer", "Clever Swindler"]
        of_the = ["of the Underworld Networks", "of the Sneaky Escapes", "of the Ruthless Ambitions", "of the Shady Deals", "of the Clever Schemes"]

    # Background: Commoner
    if npc.background == "Commoner":
        descriptor = ["Simple", "Honest", "Hardworking", "Modest", "Steadfast"]
        rank = ["Village Elder", "Honest Farmer", "Hardworking Laborer", "Modest Craftsman", "Steadfast Citizen"]
        of_the = ["of the Simple Life", "of the Honest Work", "of the Hardworking Hands", "of the Modest Homes", "of the Steadfast Communities"]

    # Background: Cultist
    if npc.background == "Cultist":
        descriptor = [
            "Cult",
            "Fanatical",
            "Mystical",
            "Secretive",
            "Zealous",
            "Obscure"]
        rank = [
            "Oracle",
            "Leader",
            "Acolyte",
            "Devotee",
            "Follower",
            "Priest"]
        of_the = [
            "of the Sect",
            "of Rites",
            "of the Order",
            "of the Rituals",
            "of the Yellow King",
            "of the King in Yellow",
            f"of the {random.choice(descriptor)} King",
            ]

    # Background: Druid
    if npc.background == "Druid":
        descriptor = [
            "Natural",
            "Earthy",
            "Mystical",
            "Primal",
            "Guardian",
            "Circle's",
            "Nature's",
            "Green",
            ]
        rank = [
            "Druid",
            "Archdruid",
            "Protector",
            "Shaman",
            "Warden",
            "Guardian"]
        of_the = [
            "of the Wild",
            f"of the {random.choice(descriptor)} Circle",
            f"of the {random.choice(descriptor)} Circle",
            f"of the {random.choice(descriptor)} Circle",
            f"of the {random.choice(descriptor)} Circle",
            f"of the {random.choice(descriptor)} Circle",
            f"of the {random.choice(descriptor)} Circle",
            f"of the {random.choice(descriptor)} Circle",
            f"of the {random.choice(descriptor)} Circle",
            f"of the {random.choice(descriptor)} Circle",
            f"of the {random.choice(descriptor)} Woods",
            f"of the {random.choice(descriptor)} Woods",
            f"of the {random.choice(descriptor)} Woods",
            "of the Woods",
            "of the Groves"]

    # Background: Expert
    if npc.background == "Expert":
        descriptor = ["Knowledgeable", "Skilled", "Professional", "Adept", "Specialized"]
        rank = ["Expert Consultant", "Knowledgeable Practitioner", "Skilled Professional", "Adept Analyst", "Specialized Technician"]
        of_the = ["of the Knowledgeable Fields", "of the Skilled Trades", "of the Professional Studies", "of the Adept Research", "of the Specialized Skills"]

    # Background: Explorer
    if "Explorer" in creature_type:
        descriptor = [
            "Adventurous",
            "Curious",
            "Intrepid",
            "Daring",
            "Pioneering",
            "Legendary",
            ]
        rank = [
            "Explorer",
            "Wanderer",
            "Adventurer",
            "Pathfinder",
            "Scout",
            ]
        of_the = [
            "of the Uncharted Lands",
            f"of the {random.choice(descriptor)} Expedition",
            f"of the {random.choice(descriptor)} Journey",
            f"of the {random.choice(descriptor)} Quests",
            f"of the {random.choice(descriptor)}  Frontiers",
            ]

    # Background: Guard
    if npc.background == "Guard":
        descriptor = ["Vigilant", "Stalwart", "Protective", "Disciplined", "Alert"]
        rank = ["Seasoned Guard", "Stalwart Defender", "Protective Watchman", "Disciplined Sentinel", "Alert Keeper"]
        of_the = ["of the Guarded Fortresses", "of the Stalwart Walls", "of the Protective Gates", "of the Disciplined Patrols", "of the Alert Towers"]

    # Background: Healer
    if npc.background == "Healer":
        descriptor = ["Master","Compassionate", "Healing", "Wise", "Caring", "Skillful"]
        rank = ["Healer", "Physician", "Herbalist", "Medic", "Practitioner"]
        of_the = ["of the Healing Touch", "of the Wise Remedies", "of the Caring Hands", "of the Skillful Treatments", "of the Compassionate Care"]

    # Background: Hero
    if npc.background == "Hero":
        descriptor = ["Valiant", "Brave", "Heroic", "Gallant", "Noble"]
        rank = ["Valiant Saviour", "Brave Warrior", "Heroic Defender", "Gallant Knight", "Noble Protector"]
        of_the = ["of the Valiant Deeds", "of the Brave Battles", "of the Heroic Ventures", "of the Gallant Quests", "of the Noble Causes"]

    # Background: Hunter
    if npc.background == "Hunter":
        descriptor = [
            "Green",
            "Stealthy", "Rugged", "Sharpshooter", "Trapper", "Wild"]
        rank = ["Stealthy Tracker", "Rugged Huntsman", "Sharpshooter Archer", "Skilled Trapper", "Wild Stalker"]
        of_the = ["of the Stealthy Pursuit", "of the Rugged Wilderness", "of the Sharpshooter's Range", "of the Skilled Snares", "of the Wild Hunt"]

    # Background: Knight
    if npc.background == "Knight":
        descriptor = ["Chivalrous", "Gallant", "Honorable", "Bold", "Noble"]
        rank = ["Knight", "Champion", "Defender", "Warrior", "Cavalier"]
        of_the = ["of the Noble Order", "of the Chivalrous Quests", "of the Gallant Deeds", "of the Honorable Battles", "of the Bold Ventures"]

    # Background: Mage
    if "Mage" in creature_type:
        descriptor = [
            "Arcane",
            "Mystical",
            "Learned",
            "Enigmatic",
            "Sorcerous",
            "Yellow",
            "Blue",
            "Red",
            "Crimson",
            "Rainbow",
            "White",
            "Grey",
            "Green",
            "Black",
            "Dark",
            
            ]
        rank = [
            "Oracle",
            "Wizard",
            "Sorcerer",
            "Magician",
            "Alchemist",
            "Scholar"]
        of_the = [
            "of Mysteries",
            "of Mystical Arts",
            "of the Scrolls",
            "of the Potions",
            "of the Academy"]

    # Background: Monk
    if npc.background == "Monk":
        descriptor = ["Disciplined", "Spiritual", "Meditative", "Ascetic", "Harmonious"]
        rank = ["Disciplined Master", "Spiritual Guide", "Meditative Sage", "Ascetic Practitioner", "Harmonious Philosopher"]
        of_the = ["of the Disciplined Path", "of the Spiritual Enlightenment", "of the Meditative Tranquility", "of the Ascetic Way", "of the Harmonious Balance"]

    # Background: Merchant
    if npc.background == "Merchant":
        descriptor = ["Shrewd", "Wealthy", "Trading", "Negotiating", "Resourceful"]
        rank = ["Wealthy Trader", "Shrewd Businessperson", "Skilled Negotiator", "Resourceful Dealer", "Prosperous Merchant"]
        of_the = ["of the Trading Empires", "of the Wealthy Markets", "of the Negotiating Tables", "of the Resourceful Ventures", "of the Prosperous Exchanges"]
        
    # Background: Noble
    if "Noble" in creature_type:
        descriptor += [
            "Aristocratic",
            "Noble",
            "Refined",
            "Graceful",
            "Influential",
            "Dignified"]
        if npc.gender == "he":
            rank += ["Lord"]
        if npc.gender == "he":
            rank += ["Lady"]
        rank += [
            "Marquis",
            "Diplomat",
            "Baron",
            "Count",
            ]
        of_the += [
            f"of the {random.choice(descriptor)} Court",
            f"of the {random.choice(descriptor)} Estate",
            "of the Mansions",
            f"of the {random.choice(descriptor)} Council",
            f"of the {random.choice(descriptor)} Assembly"]

    # Background: Priest
    if npc.background == "Priest":
        descriptor += ["Devout", "Pious", "Clerical", "Faithful", "Sacred"]
        rank += ["High Priest", "Devout Cleric", "Pious Acolyte", "Faithful Preacher", "Sacred Keeper"]
        of_the += ["of the Holy Sanctuaries", "of the Devout Congregations", "of the Pious Orders", "of the Faithful Ministries", "of the Sacred Rites"]

    # Background: Pirate
    if npc.background == "Pirate":
        descriptor += ["Ruthless", "Swashbuckling", "Seafaring", "Adventurous", "Rebellious"]
        rank += ["Infamous Captain", "Swashbuckling Buccaneer", "Seafaring Raider", "Adventurous Corsair", "Rebellious Marauder"]
        of_the += ["of the Infamous Seas", "of the Swashbuckling Crews", "of the Seafaring Voyages", "of the Adventurous Journeys", "of the Rebellious Fleets"]

    # Background: Ranger
    if "Ranger" in creature_type:
        descriptor += [
            "Green",
            "Wilderness", "Tracking", "Survivalist", "Rugged", "Nature's"]
        rank += ["Wilderness Scout", "Master Tracker", "Survivalist Expert", "Rugged Outlander", "Nature's Warden"]
        of_the += ["of the Wilderness Paths", "of the Tracking Hunts", "of the Survivalist Camps", "of the Rugged Mountains", "of the Nature's Secrets"]

    # Background: Scholar
    if npc.background == "Scholar":
        descriptor += ["Learned", "Intellectual", "Inquisitive", "Studious", "Erudite"]
        rank += ["Learned Professor", "Intellectual Researcher", "Inquisitive Historian", "Studious Philosopher", "Erudite Sage"]
        of_the += ["of the Learned Academies", "of the Intellectual Societies", "of the Inquisitive Libraries", "of the Studious Lectures", "of the Erudite Scrolls"]

    # Background: Soldier
    if "Soldier" in creature_type:
        descriptor += [
            "Disciplined",
            "Veteran",
            "Battle",
            "Hardened",
            "Strategic",
            "Brave",
            "Tactical"]
        rank += [
            "Commander",
            "Sergeant",
            "Warrior",
            "General",
            "Soldier"]
        of_the += [
            "of the Disciplined Regiments",
            "of the Last Regiment",
            "of the First Regiment",
            "of the Battle-Hardened Fronts",
            "of the Northern Fronts",
            "of the Strategic Commands",
            "of the Brave Units",
            "of the Tactical Operations",
            "of Special Operations",
            ]

    # Background: Rogue
    if npc.background == "Rogue":
        descriptor += ["Sneaky", "Cunning", "Agile", "Mysterious", "Resourceful"]
        rank += ["Master Thief", "Cunning Assassin", "Agile Scout", "Mysterious Spy", "Resourceful Trickster"]
        of_the += ["of the Sneaky Shadows", "of the Cunning Plots", "of the Agile Escapes", "of the Mysterious Underworld", "of the Resourceful Heists"]

    # Background: Shaman
    if "Shaman" in creature_type:
        descriptor += [
            "Green",
            "Spiritual",
            "Mystic",
            "Elemental",
            "Tribal",
            "Ancestral"]
        rank += [
            "Oracle",
            "Leader",
            "Healer",
            "Guide",
            "Sage",
            "Keeper"]
        of_the += [
            f"of the {random.choice(descriptor)} Rites",
            f"of the {random.choice(descriptor)} Visions",
            f"of the {random.choice(descriptor)} Forces",
            f"of the {random.choice(descriptor)} Traditions",
            f"of the Ancestral Spirits"]

    # Background: Spy
    if npc.background == "Spy":
        descriptor += ["Covert", "Undercover", "Secretive", "Stealthy", "Infiltrating"]
        rank += ["Covert Agent", "Undercover Operative", "Secretive Informant", "Stealthy Scout", "Infiltrating Spy"]
        of_the += ["of the Covert Missions", "of the Undercover Operations", "of the Secretive Networks", "of the Stealthy Reconnaissance", "of the Infiltrating Tactics"]

    # Background: Traveler
    if npc.background == "Traveler":
        descriptor += ["Wandering", "Adventurous", "Nomadic", "Curious", "Worldly"]
        rank += ["Wandering Nomad", "Adventurous Explorer", "Nomadic Wanderer", "Curious Journeyer", "Worldly Traveler"]
        of_the += ["of the Wandering Paths", "of the Adventurous Expeditions", "of the Nomadic Tribes", "of the Curious Voyages", "of the Worldly Discoveries"]

    # Background: Urchin
    if npc.background == "Urchin":
        descriptor += ["Streetwise", "Scrappy", "Surviving", "Quick", "Resourceful"]
        rank += ["Streetwise Scamp", "Scrappy Survivor", "Surviving Orphan", "Quick Pickpocket", "Resourceful Rogue"]
        of_the += ["of the Street Corners", "of the Scrappy Alleys", "of the Surviving Struggles", "of the Quick Escapes", "of the Resourceful Scrounges"]

    # Background: Warrior
    if npc.background == "Warrior":
        descriptor = ["Battle-Ready", "Fearless", "Mighty", "Skilled", "Honorable"]
        rank = ["Battle-Ready Fighter", "Fearless Warrior", "Mighty Gladiator", "Skilled Duelist", "Honorable Champion"]
        of_the = ["of the Battle Arenas", "of the Fearless Campaigns", "of the Mighty Conquests", "of the Skilled Combats", "of the Honorable Duels"]

    # Background: Warlock
    if npc.background == "Warlock":
        descriptor += ["Eldritch",
                      "Mysterious",
                      "Pact",
                      "Arcane",
                      "Otherworldly",
                       "Fallen",
                       "New",
                       ]
        rank += ["Oracle",
                "Warlock",
                "Caster",
                "Occultist",
                "Maker",
                "Conjurer",
                "Scholar",
                "Advisor"]
        of_the += [
                  f"of the {random.choice(descriptor)} Secrets",
                  f"of the {random.choice(descriptor)} Rites",
                  "of Servitude",
                  f"of the {random.choice(descriptor)} Lore",
                  f"of the {random.choice(descriptor)} Powers",
                  "of the Sold Soul",
                  "of the Deal",
                   f"of the {random.choice(descriptor)} King",
                   "of the King in Yellow",
                   f"of the {random.choice(descriptor)} God",
                   ]

    # Background: Witch
    if npc.background == "Witch":
        descriptor += ["Enchanting", "Occult", "Mystical", "Hexing", "Wise"]
        rank += ["Enchanting Sorceress", "Occult Witch", "Mystical Herbalist", "Hexing Caster", "Wise Crone"]
        of_the += ["of the Enchanting Spells", "of the Occult Rituals", "of the Mystical Arts", "of the Hexing Curses", "of the Wise Traditions"]




















    descriptor += [
    "Primal",
    "Lost",
        ]

























    
    rank += [
        "Howl"
        "Artisan",
        "Abbess",
        "Abbot",
        "Abysswalker",
        "Acolyte",        
        "Alchemist",
        "Light",
        "Alpha",
        "Ambassador",
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
        "Heir",
        "Artificer",
        "Ascendant",
        "Gold",
        "Voyager",
        "Astrologer",
        "Astronomer",
        "Auralist",
        "Auramancer",
        "Avalon's Lost Knight",
        "Avatar",
        "Avenger",
        "Apprentice",

# B
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
"Beastmaster",
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
"Bow",

"Bravo",
"Breeder",
"Brewer",
"Briar",
"Brigadier",
"Bringer",
"Breaker",        

"Buccaneer",
"Bull",
"Burglar",
"Butcher",
"Butterfly",
"Buzzard",

# C
"Cadaver",
"Cairn",
"Camel",
"Cannibal",
"Captain",
"Cartographer",
"Cedar",
"Centurion",
"Champion",
"Charlatan",
"Cheetah",
"Chemist",
"Chieftain",
"Chimera",
"Cleric",
"Claw",
"Climber",
"Cobbler",
"Cobra",
"Collector",
"Colossus",
"Commander",
"Commodore",
"Conjurer",
"Conqueror",
"Corsair",
"Cougar",
"Counselor",
"Courage",
"Crow",
"Crusader",
"Crypt",
"Cultist",
"Curator",
"Curse",
"Cyclops",


"Daisy",
"Dame",
"Dancer",
"Daredevil",
"Darkness",

"Death",
"Deathless",
"Decay",
"Deer",
"Defender",
"Deity",
"Demigod",
"Demon",
"Demonhunter",
"Detective",
"Devil",
"Devourer",
"Diamond",
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
"Eater",
"Eclipse",
"Ectoplasm",
"Elder",
"Element",
"Elite",
"Elixir",
"Elk",

"Emperor",
"Empress",

"Enchantress",
"Endeavor",
"Enforcer",
"Envoy",

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
"Gargoyle",
"Gazelle",

"General",
"Genius",

"Ghast",
"Ghost Hunter",
"Ghost",

"Giant",

"Gladiator",

"Goat",
"Golem",

"Grandmaster",
"Grave Robber",
"Grave",
"Gravewalker",

"Guard",
"Guardian",
"Guide",
"Gull",
"Guru",

"Hag",
"Hand",
"Harbinger",
"Harpy",
"Haunt",
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

"Assassin",
"Atlas",
"Augur",
"Avatar",
"Acolyte",
"Alchemist",
"Alpha",
"Ambassador",
"Ambition",
"Anthropologist",
"Arcanologist",
"Archbishop",
"Archduchess",
"Archduke",
"Archer",
"Archivist",
"Archmage",
"Argonaut",
        
"Heir",
        
"Artificer",
"Ascendant",
"Astral Voyager",
"Astrologer",
"Astronomer",
"Auralist",
"Auramancer",



    # B
    "Baboon", "Badger", "Baker", "Band", "Banshee", "Bard", "Baron", "Barrow", "Basilisk",
    "Battlemage", "Beacon", "Bear", "Beastmaster", "Beetle", "Beholder", "Benefactor", 
    "Berserker", "Bishop", "Bison", "Blacksmith", "Blade", "Blaze", "Blighted", "Blizzard",
    "Blossom", "Boar", "Bone", "Bounty Hunter", "Bow", "Bravo", "Breeder", "Brewer", "Briar",
    "Brigadier", "Bringer", "Buccaneer", "Bull", "Burglar", "Butcher", "Butterfly", "Buzzard",

    # C
    "Cadaver", "Cairn", "Camel", "Cannibal", "Captain", "Cartographer", "Cedar", "Centurion",
    "Champion", "Charlatan", "Cheetah", "Chemist", "Chieftain", "Chimera", "Claw", "Cleric",
    "Climber", "Cobbler", "Cobra", "Collector", "Colossus", "Commander", "Commodore", "Conjurer",
    "Conqueror", "Corsair", "Cougar", "Counselor", "Courage", "Crow", "Crusader", "Crypt",
    "Cultist", "Curator", "Breaker", "Cursed Wanderer", "Cyclops",

    # D - E
    "Daisy", "Dame", "Dancer", "Daredevil", "Darkness", "Death", "Deathless", "Decay",
    "Deer", "Defender", "Deity", "Demigod", "Demon", "Demonhunter", "Detective", "Desolate",
    "Despot", "Devil", "Devourer", "Diamond", "Dino", "Diplomat", "Disciple", "Discoverer",
    "Djinn", "Doctor", "Dolphin", "Dominator", "Doom", "Dove", "Dragon", "Drake", "Dread",
    "Dream", "Drifter", "Drone", "Druid", "Duchess", "Duke", "Dungeon Delver", "Eagle", "Eater",
    "Eclipse", "Ectoplasm", "Elder", "Element", "Elite", "Elixir", "Elk", "Emperor", "Empress",
    "Enchantress", "Endeavor", "Enforcer", "Envoy", "Ethereal", "Exarch", "Executioner", "Exile",
    "Exorcist", "Expedition", "Explorer",

    # F - G
    "Falcon", "Falconer", "Fallen", "Fanatic", "Farmer", "Farrier", "Farwalker", "Fawn",
    "Feather", "Fel", "Fellow", "Fern",

        "Fiend", "Fin", "Fire", "Flame", "Flutist",
    "Foreseer", "Forged", "Forsaken", "Fox", "Freedomfighter", "Frog", "Frontier", "Frost",
    "Fury", "Gale", "Gargoyle", "Gazelle", "General", "Genius", "Ghast", "Ghost Hunter", "Ghost",
    "Giant", "Gladiator", "Goat", "Golem", "Grandmaster", "Grave Robber", "Grave", "Gravewalker",
    "Guard", "Guardian", "Guide", "Gull", "Guru",

    # H - I
        "Hag", "Hand", "Harbinger", "Harpy", "Haunt", "Hawk", "Heather", "Heir", "Herbalist",
    "Heretic", "Hermit", "Hero", "Heron", "Highlord", "Highness", "Hive", "Hollow", "Holly",
    "Horizon", "Horror", "Horse", "Hound", "Hoof", "Hunger", "Hunter", "Hydra", "Hyena", "Incubus",
    "Infernal", "Inquisitor", "Intellect", "Ivy",

    # J - L
    "Jackal", "Jaguar", "Jasmine", "Jay", "Jester", "Journey", "Judge", "Juggernaut", "Jungle",
    "Juniper", "Kaiju", "Keeper", "Kestrel", "Killer", "King", "Kinsman", "Kiss", "Knife",
    "Knight", "Lark", "Laurel", "Leader", "Legate", "Legend", "Legionnaire", "Leopard", "Lich",
    "Light", "Lily", "Lion", "Lizard", "Lord", "Lost", "Lotus", "Lover", "Lynx",
"Knight",

    # M
    "Machine", "Mage", "Magister", "Magus", "Man", "Mantis", "Marauder", "Mare", "Marigold",
    "Mariner",  "Marshal", "Martyr", "Mask",
"Mason", "Master", "Mastermind", "Mastiff",
    "Matriarch", "Mausoleum", "Memento", "Mender", "Mercenary", "Merlin", "Mesmer", "Messenger",
    "Miller", "Mimic", "Mind", "Minister", "Minstrel", "Mist", "Monk", "Monster Hunter", "Monster",
    "Moon", "Morgue", "Mortal", "Moth", "Mountaineer", "Mourner", "Mule", "Mystic", "Mystic",

    # N - O
    "Navigator", "Necro", "Necromancer", "Nether", "Nightingale", "Nightmare", "Ninja", "Noble",
    "Nomad", "Orchid", "Ossuary", "Otter", "Outlander", "Outlaw", "Outrider", "Overlord",
    "Owl", "Owlbear",

    # P - R
    "Paladin", "Patriarch", "Peasant", "Pegasus", "Peregrine", "Petal", "Phantom", "Phoenix",
    "Pilgrim", "Pirate", "Plains Wanderer", "Planar Researcher", "Poem", "Poker Face", "Potter",
    "Primrose", "Protege", "Prowler", "Puma",

"Queen", "Quest",

"Radiance", "Raj", "Ranger",
    "Rattlesnake", "Raven", "Reaper", "Reclaimer", "Reed", "Relic Seeker", "Requiem", "Restless",
    "Rider", "Risen", "Ritualist", "Rogue", "Rose", "Rowan", "Rue", "Runesmith",

    # S
    "Sage", "Sailor", "Saint", "Satyr", "Savant", "Savior", "Scout", "Scribe", "Seer", "Sentinel",
    "Serpent", "Shade", "Shadow", "Shaman", "Sheriff", "Shield", "Sire", "Skyward", "Smith",
    "Smuggler", "Sorcerer", "Specter", "Spellbinder", "Spirit", "Spy", "Squire", "Stag",
    "Starship Pilot", "Stingray", "Storm Chaser", "Swallow", "Swan",

    # T - U
    "Tailor", "Talon", "Tamer", "Templar", "Thistle", "Tiger", "Tormented", "Tormentor",
    "Trailblazer", "Traveler", "Treasure Hunter", "Troll", "Tyrant", "Unholy",

    # V - Z
    "Valkyrie", "Vampire", "Vanguard", "Vicar", "Virtuoso", "Visionary", "Voyager",

    "Warrior", "Watcher", "Werewolf", "Witch", "Witchhunter", "Wizard",

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
        "Brewer",

        "Cat",
        "Cadaver",
        "Cairn",
        "Camel",
        "Cannibal",
        "Captain",
        "Captain",
        "Cartographer",
        "Mapper",
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
        "Cougar",
        "Counselor",
        "Courage",
        "Crow",
        "Crusader",
        "Crypt",
        "Cultist",
        "Curator",
        "Curse",
        "Breaker",
        "Collector",
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
        "Detective",
        "Desolate",
        "Despot",
        "Devil",
        "Devourer",
        "Diamond",
        "Traveler",
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
        "Chaser",
        "Eclipse",
        "Ectoplasm",
        "Elder",
        "Scholar",
        "Element",
        "Whisperer",
        "Elite",
        "Elixir",
        "Elk",
        "Emperor",
        "Empress",
        "Enchantress",
        "Endeavor",
        "Enforcer",
        "Envoy",
        "Fisher",
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
        "for Hire",

        
        "Gale",
        "Gargoyle",
        "Gazelle",
        "General",
        "Genius",
        "Ghast",
        "Ghost Hunter",
        "Ghost",
        "Ghost's",
        "Giant",
        "Gladiator",
        "Goat",
        "Golem",
        "Grandmaster",
        "Grave Robber",
        "Grave",
        "Gravewalker",
        "Guard",
        "Guardian",
        "Great",
        "Guardian",
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
        "Hoof",
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
        "Merchant",
        "Morgue",
        "Mortal",
        "Mortal",
        "Moth",
        "Mountaineer",
        "Mourner",
        "Mule",
        "Mystic",
        "Investigator",
        
        
        
        

        

        
        


        "Celestian",
        
        "Guide",
        
        "Heart",
        "High Ambassador",

        "Sentinel",
        "Masked",
        "Wailmistress",
        "Banshee's",
        "Flight",
        
        "Baron",
        "Barbarian",
        "Bard",
        "Baron",
        "Baron",
        "Baroness",
        "Battle Cleric",
        "Battle Herald",
        "Beastrider",
        "Banneret",
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
        "of the Burning Seas",
        "Buffalo Soldier",
        "Buffalo Whisperer",
        "Bushman's Dance",
        "Bringer",
        
        "Mystic",
        
        "Cursebreaker",
        "Caliph",
        "Cantor",
        "Captain",
        "Cardinal",
        "Baron",
        "Cauldron",
        "Cavalier",
        "Celestial Priest",
        "Celestialist",
        "Celestian",
        "Celestwarden",
        "Alpha",
        "Centurion",
        "Centurion",
        "Change",
        "Champion",
        "Chancellor",
        "Chancellor",
        "Chosen",
        "Mimic",
        "Chaplain",
        "Charm",
        "Chase",
        "Chief",
        "Chief",
        "Chieftain",
        "Chronomancer",
        "Chronoshifter",
        "Seeker",
        "Jumper",
        "Cleric",
        "Cloudcaller",
        "Keeper",
        "Coil",
        "Codex ",
        "Combat Priest",
        "Commander",
        "Commander",
        "Wing",
        "Conquistador",
        "Consul",
        "Consul",
        "Cossack",
        "Councillor",
        "Count",
        "Count",
        "Countess",
        "Covered",
        "Coyote's",
        "Coyote's",
        "Craft",
        "Creation",
        "Crocodile's",
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
        "Artisan",
        "Emissary",
        "Herald",
        "Sage",
        "Djinn Sultan",
        "Djinn Whisperer",
        "Djinn's Whimsy",
        "Domovoi's Guardian",
        "Doomsayer",
        "Dragon Knight",
        "Dragonson",
        "Dragoon",
        "Dragoon",
        "Dreambinder",
        "Dreamcatcher",
        "Dreamer",
        "Dreamforge",
        "Dreamweaver",
        "Dreamweaver",
        "Dreamweaver",
        "Nightshade",
        "of the Swamp",
        "Druid",
        "Dryad",
        "Duchess",
        "Dawn",
        "Duelist",
        "Duende",
        "Duke",
        "Duke",
        "Dungeon Delver",
        "Duskwielder",
        "Dusty Boots",
        
        "Eye",
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
        "Eldest",
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
        "of Vasilisa",
        "'s Guardian",
        "Freya's Heartshield",
        "Friar",
        "Frontier's Flame",
        "Frostbinder of Niflheim",
        "Frostheart of Yuki-onna",
        "Frostweaver",
        "Last Journey",
        "Fury",
        
        "Galeweaver",
        "Gaze",
        "Gemseeker",
        "Genasi Elementward",
        "General",
        "Geomancer",
        "Geomancer",
        "of La Noche Triste",
        "Ghost Town's",
        "Ghostseer",
        "Cloudcaller",
        "Starblade",
        "Mindwarden",
        "Gladiator",
        "Gladiator",
        "Glaivemaster",
        "Glimmerblade",
        "Gloomshade",
        "Glow",
        "Mastermind",
        "King",
        "Godsbane Priest",
        "Godspeaker",
        "Seeker",
        "Governor",
        "Grace",
        "Graceful",
        "Griot's Song",
        "Grovekeeper",
        "Guarani's Dream",
        "Guardian",
        "Guardian",
        "Gunslinger",
        
        "Stoneguard",
        "Scale",
        "Shaman",

        "Leafdancer",
        "Hangman's Noose",
        "Harbinger of Fate"
        "of Elysium",
        "Matriarch",
        "Harvestshade",
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
        "Gaze",
        "Hussar",
        "Hydra Slayer",
        "Icarus Skyfall",
        "Illusionist",
        "Immortal",
        "Pursuer",
        "Echo",
        "Last Defender",
        "Infernalist",
        "Inquisitor",
        "Intrigue",
        "Chosen",
        "Jaguar",
        "Prowler",
        "Janissary",
        "Jarl",
        "Jester",
        "Foil",
        "Journeys",
        "Storyteller",
        "Khan",
        "King",
        "'s Quest",
        "Knight",
        "Knight",
        "Tunnelchief",
        "Song",
        
        "Lady",
        "Enchanter",
        "Lampbearer",
        "of the Forbidden Cave",
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
        "Roar",
        "Sunscale",
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
        "Minotaur",
        "Bull",
        "Labyrinth Keeper",
        "Mirage",
        "Mischiefmaster",
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
        "Mountain",
        "Mummy",
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
        
        "Sandkeeper",
        "Siren",
        "Storyteller",
        
        "Illusionist",
        
        
        "Echo",
        "Enigma",  
        "Elegance",
        
        "Occultist",
        "Oni",


        "Forge",

        "Legacy",

        "Depth",
        "Demonmask",



        "Echoes",

        "Fragment",
        
        "Oracle",
        "Oracle",
        "Oracle",
        "Orcish",
        "Warchief's",
        "Orisha's",
        "Chosen",
        "Osiris's",
        "Rise",
        "Outlaw",
        "Outlaw's",
        "Kin",
        "Overseer",
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
        "Pendulum",
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
        "Paladin",
        "Pioneer",
        "Pathfinder",
        "Patriarch",
        "Pedagogue",
        "Pharaoh",
        
        "Stormcaller",
        
        "Visionary",
        "Vengeance",
        
        "Leader",
        "Legacy",
        "Philosopher",
        "Pikeman",
        "Piper",
        "Pirate",
        "Ghost",
        "of Port Royal",
        "Pistolero",
        "Plains Wanderer",
        "Planar Researcher",
        "Poem",
        "Poker Face",
        "Pride",
        "Wind",
        "Pope",
        "Leader",
        "Potato",  
        "Potion Master",
        "Praetor",
        "Praetor",
        "Shadow",
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
        "Progenitor",
        "of Prometheus",
        "Prophet",
        "Prophetess",
        "Prospector's Dream",
        "Prowlmaster",
        "Psion",
        
        "Queen",
        "Feathered",
        "Quail",
        "Queen",
        "Quest",
        
        "Radiance",
        "Radiantstar",
        "Railroad Pioneer",
        "Rain Dancer",
        "Rain Queen's Blessing",
        "Rajput",
        "Rakshasa Deceiver",
        "Ranger",
        "Rattlesnake's",
        "Fang",
        "Raven's",
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
        "Gem",
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
        "Runemaker",
        "Runewritter",
        "of Midgard",
        "Runechanter",
        "Runekeeper",
        "Rabbit",
        "Raider",
        "Ranger",
        "Rat",
        "Raven",
        "Raven",
        "Revenant",
        "Reptile",
        "Rider",
        "Rose",
        "Ruby",
        "Rune",
        "Raptor",
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


        "Keeper",
        
        "Lament",
        
        "Bane",
        "Bane",
        "Bane",
        "Bane",
        "Bane",
        "Bane",
        "Bane",
        "Bane",
        
        
        "Sacred Keeper",
        "Sacred Speaker",
        "Speaker",
        "Scar",
        "Spirit",
        "Saga",
        "Sage",
        "Saint",
        "Tooth",
        "Saurius",
        "Salamander",
        "Scientist",
        "Scarecrow",
        "Scorpion",
        "Shadow",
        "Shark",
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
        "Duelist",
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
        "Six-Shooter",
        "Sage",
        "of the Eternal Sagas",
        "of the Eternals",
        "Skymaiden",
        "Skyrider",
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
        "Riddle",
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
        "Keeper",  
        "Sunblessed",
        "Sundiata's Valor",
        "Sunlord",
        "Sunscale",
        "Sunstrider",
        "Supreme Leader",
        "Sworddancer",
        "Swordmaster",
        "Shadow",
        "Secret",
        
        "Prowlmaster",

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
        "Tale",
        "Torchbearer",
        "Thunderbird",
        
        "Star",
        "Seer",
        "Spirit",
        
        "Echo",
        

        
        "Treasure Fleet's Scourge",
        "Treasure",
        "Treebinder",
        "Tribal",
        "Trick",
        "Trickster",
        "Tribune",
        "Wavecommander",
        "Chieftain",
        "Hunter",
        "Troubadour",
        "Champion",
        "Drifter",
        "Tunnelchief",
        "Turtle Islander",  
        "Treasure",
        "Twilight",
        "Herald",

        "Unholy",
        
        "Elder",
        
        "Skymaiden",
        "Valkyrie",
        "Chosen",
        "Valor",
        "Valorblade",
        "Lord",
        "Vanguard",
        "Serpent",
        "Venerable One",
        "Vicar",
        "Viking",
        "Voyager",
        "Viscount",
        "Vision",
        "Vizier",
        "Viceroy",
        "of Hispaniola",
        "Rival",
        "Voidseer",
        "Voidtouched",
        "Visionary",
        "Vizier",
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
        "Voyage",        
        "Valkyrie",
        "Voice",
        
        
        "Heart",
        
        
        "Pilgrim",
        
        "Trader",
        
        "Enchanter",
        
        "Dawnbringer",
        "Drum",

        "Rebellion",
        
        "Serpentlord",
                
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
        "of the Endless Sands",
        "of the Gods",
        
        "Pestilence",
        
        "Quake",
        
        "Rancor",
        
        "Sable",
        
        "Torment",
        
        "Umbra",
        
        "Vendetta",
        
        "Wraith",
        
        
        "Brahmin",
        "Bane",
        "Brigadier",
        "Bishop",
        "Blight",
        
        "Cadet",
        "Canon",
        "Cardinal",
        "Captain",
        "Centurion",
        "Chieftain",
        "Cleric",
        
        "Daimyo",
        "Deacon",
        "Dean",
        "Dread",
        
        "Seeker",
        
        "Enigma",
        "Ensign",
        
        "Fang",
        "Friar",
        "Fellow",
        
        
        "of the Golden City",
        
        "Sentinel",
        "Seeker",
        
        "Conquistador",

        "Exemplar",
        "Elder",

        "Forerunner",

        "Guardian",
        "General",
        "Ghoul",
        
        "High Priest",
        "Harbinger",
        
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
        "Noble",
        "Nomad",
        "Numerologist",
        "Nun",
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
        "Nightshade",
        "Nightshade",
        "Nightveil",
        "Necrologist",
        "Netherbound",
        "Nemesis",
        "Navigator",

        
        "Paragon",
        "Patriarch",
        "Pharaoh",
        "Professor",
        "Pasha",
        "Prelate",
        "Priestess",
        "Prodigy",
        "Patriarch",
        "Progenitor",
        "Pioneer",
        
        "Raj",
        "Reader",
        "Renegade",
        
        "Samurai",
        "Scholar",
        "Sergeant",
        "Shaman",
        
        "Tutor",
        "Tribe Leader",
        
        "Vanguard",
        "Vicar",
        "Virtuoso",
        "Voyager",
        
        "Warlord",
        "Whisper",
        "Wanderer",
        "Windcaller",
        "Windrider",
        "Winglord",
        "Wisdom",
        "Witchdoctor",
        "Wolfkin",
        "Wail",
        "Walker",

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
        "Windcaller",
        "Wanderer",
        "War Druid",
        "Warwitch",
        "Warcaller",
        "Warcaster",
        "Warchief",
        "Warden",
        "Wisdom",
        "Warden",
        "Wardmaster",
        "Warforger",
        "Warhawk",
        "Warlord",
        "Warlord",
        "Warmaster",
        "Warmonger",
        "Wavecommander",
        "Wendigo",
        "Whiskey",
        "Whisper",
        "Whisperer",
        "Whitescale",
        "Warcaller",
        "Whisperer",
        "Wrath",
        
        "Yarrow",
        "Yielder",

        "Zenithar",
        "Zealot",
        "Zinnia",
        "Zombie",
        "Zoologist",
        "Zulu",
        
        ""
    ]

    of_the += [
        "Of Athena",
        "of Delphos",
        "of the Underworld Gate",
        "of the Underworld",
        "Odyssey",
        "Of Death",
        "of El Dorado",
        "of Eldorado"
        "Of Fate",
        "Of Heaven",
        "Of Justice",
        "Of Odin",
        "Of The Abyss",
        "Of the Autumn",
        "Of the Coliseum",
        "Of The Crown",
        "Of The Dead",
        "Of The Desert",
        "Of the Divine",
        "Of The East",
        "Of The Fiends",
        "Of The Forest",
        "Of The Forge",
        "Of The Hells",
        "Of The Hills",
        "Of the Hidden",
        "Of the Kingdom",
        "Of the Last Fire",        
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
        "Of Youth",
        "Of Zeus",
        "of the Faith",
        "of the Forty Thieves",
        "of the Morningstar",
        "of the Thousand Tears",
        "of the Jungle",
        "of the City",
        "of the Land",
        "of the North",
        "of the South",
        "of the East",
        "of the West",
        "of the Forest",
        "of the Plains",
        "of the Sea",
        "of the Sky",
        "of Fire",
        f"of the {random.choice(descriptor)} Woods",
        f"of the {random.choice(descriptor)} Woods",
        f"of the {random.choice(descriptor)} Woods",
        f"of the {random.choice(descriptor)} Woods",
        f"of the {random.choice(descriptor)} Woods",
        f"of the {random.choice(descriptor)} Woods",
        f"of the {random.choice(descriptor)} Woods",
        f"of the {random.choice(descriptor)} Woods",
        f"of the {random.choice(descriptor)} Woods",
        f"of the {random.choice(descriptor)} Woods",
        f"of the {random.choice(descriptor)} Woods",
        f"of the {random.choice(descriptor)} Woods",
        f"of the {random.choice(descriptor)} Woods",
        f"of the {random.choice(descriptor)} Woods",
        f"of the {random.choice(descriptor)} Woods",
        f"of the {random.choice(descriptor)} Woods",
        f"of the {random.choice(descriptor)} Woods",
        f"of the {random.choice(descriptor)} Woods",
        f"of the {random.choice(descriptor)} Realms",
        f"of the {random.choice(descriptor)} Realms",
        f"of the {random.choice(descriptor)} Realms",
        f"of the {random.choice(descriptor)} Realms",
        f"of the {random.choice(descriptor)} Realms",
        f"of the {random.choice(descriptor)} Realms",
        f"of the {random.choice(descriptor)} Realms",
        f"of the {random.choice(descriptor)} Realms",
        f"of the {random.choice(descriptor)} Realms",
        f"of the {random.choice(descriptor)} Realms",
        f"of the {random.choice(descriptor)} Realms",
        f"of the {random.choice(descriptor)} Realms",
        f"of the {random.choice(descriptor)} Realms",
        f"of the {random.choice(descriptor)} Realms",
        f"of the {random.choice(descriptor)} Realms",
        f"of the {random.choice(descriptor)} Realms",
        f"of the {random.choice(descriptor)} Realms",
        f"of the {random.choice(descriptor)} Realms",
        f"of the {random.choice(descriptor)} Realms",
        f"of the {random.choice(descriptor)} Realms",
        f"of the {random.choice(descriptor)} Realms",
        f"of the {random.choice(descriptor)} Realms",
        f"of the {random.choice(descriptor)} Realms",
        f"of the {random.choice(descriptor)} Realms",
        "","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",
        ]

    descriptor += [
        "Red",
        ]


    title = f"The {random.choice(descriptor)} {random.choice(rank)} {random.choice(of_the)}"
    return title






























        



# Racial Names
def Racial_Names(npc):
    creature_type = npc.race + ' ' + npc.subrace + ' ' + npc.background
    Type = npc.race    
    Names = [
        "Arthurius",
        "Ada",
        "Aberrant",
        "Amelia", 
        "Anarkia",
        "Anakin",
        "Ares",
        "Alucard",
        "Altair",
        "Arya",
        "Athena",
        "Azrael",
        "Altair",
        "Aelin",
        "Aurora",
        "Aragorn",
        "Artemis",
        "Aeneas",
        "Achilles",
        "Akiles",
        "Aslan",
        "Arya",
        "Athena",
        "Apollo",
        "Artemis",
        "Atreyu",

        "Baldur",
        "Bast",
        "Blade",
        "Byron",
        "Brienne",
        "Basilisk",
        "Behemoth",
        "Balrog",
        "Bellatrix",
        "Blaze",
        
        "Cloud",
        "Cortana",
        "Cyclone",

        "Drizzt",
        
        "Eragon",

        "Frodo",
        
        "Gandalf",

        "Halcyon",

        "Magneto",
        "Mystique",
        "Mystic",

        "Nebula",
        "Nightwing",

        "Quasar",
        "Quantum",

        "Ragnarok",
        "Raven",     
        "Ripley",

        "Shadowcat",
        "Skywalker",
        "Solaris",
        "Striker",
        "Starfire",

        "Valkyrie",
        "Vibe",
        
        "Electron",
        "Phoenix",    
        "Rogue",
        "Stormborn",
        "Wraith",
        "Gambit",  
        "Vortex",
        "Iceman",
        "Jubilee",
        "Meteor",   

        "Fury",
        "Strider",
        "Neo",
        "Trinity",
        "Morpheus",  
        "Vader",
        "Legolas",
        "Thorin",
        "Inara",
        "Malcom",
        "Lee",
        "Korben",
        "Maximus",
        "Leonidas",
        "Katniss",
        "Spartacus",
        "Ellaria", 
        "Furiosa",
        "Django",
        "Snake",
        "Jules",
        "Vic",

    # Inspired by Books
     "Vaelin", "Kvothe", "Fitz", "Chivalry", "Rincewind", "Matrim", "Perrin",
    "Rand", "Ged",  "Yennefer", "Geralt", "Darrow", "Ender",  
    "Locke", "Jean",  "Falconer", "Sabriel", "Lirael", "Rhapsody",
     "Hector",  "Daenerys", "Jon", "Snow",  "Bran", "Samwell",

    # Inspired by Mythology
    "Odysseus", "Hermes",  "Perseus", "Theseus",
     "Hercules", "Orion", "Freya", "Loki", "Thor", "Anubis", "Osiris",
    "Isis", "Ra", "Horus", "Quetzalcoatl", "Tlaloc", "Ixchel", "Amaterasu", "Susanoo",
    "Tsukuyomi",  "Tyr", "Bragi", "Idunn",

    # Inspired by Video Games
    "Squall", "Zidane", "Tidus", "Link", "Zelda", "Shepard", "Geralt",
    "Yuna", "Rinoa", "Kain", "Raziel", "Dante", "Kratos", "Lara", "Samus", "Master", "Chief",
      "Ezio", "Bayek", "Aloy", "Sora", "Roxas", "Axel", "Sephiroth",
    "Riku", "Nathan", "Drake", "Ellie", "Joel", "Jill", "Valentine", "Leon", "Ada", "Wong",

    # Inspired by Anime and Manga
    "Spike", "Vash", "Alucard", "Asuka", "Rei", "Shinji", "Luffy", "Zoro", "Nami",
    "Usopp", "Sanji", "Chopper", "Robin", "Franky", "Brook", "Jotaro", "Dio",
    "Goku", "Vegeta", "Gohan", "Piccolo", "Trunks", "Bulma", "Light", "Naruto",
    "Sasuke", "Sakura", "Kakashi", "Itachi", "Gaara", "Hinata", "Ichigo", "Rukia",
    "Orihime", "Uryu", "Kenpachi", "Toushiro", "Byakuya", "Renji",

    # Inspired by Pop Culture
    "Sherlock", "Watson", "Dexter", "Heisenberg", "Jesse", "Tony", "Stark", "Bruce","Wayne",
    "Peter", "Parker", "Clark", "Kent", "Diana", "Prince", "Steve", "Rogers", "Logan", "Bruce", "Banner",
    "Natasha", "Romanoff", "Wanda", "Pietro", "Scott", "Lang", "Hope", "Shuri", "Thanos", "Loki",
    "Thor", "Hela", "Odin", "Frigga", "Vision",
    "Sam", "Bucky", "Barnes", "Nick", "Fury",  "Hill", "Phil", "Coulson", "Pepper", "Potts"


        
        "Caspian",
        "Cersei",
        "Chimera",
        "Cleopatra",
        "Cerberus",
        "Castiel",
        "Crowley", 
        "Cronos", 
        "Circe",
        
        "Dorian", 
        "Draven",
        "Dante",
        "Daenerys",
        "Draco",
        "Daemon",
        "Desmond",

        "Elektra",
        "Echo",
        "Ezio",

        "Furiosa",
        "Forajido",

        "Goku",
        "Gorgon",
        "Grendel",

        "Horus",
        "Hera",

        "Jareth",

        "Khal",
        "Kratos",

        "Loki",
        "Leia",
        "Luke",
        "Legolas", 
        "Logan",

        "Maleficent", 
        "Morpheus",
        "Maximus",
        "Mystique",

        "Nemo",
        "Neo",
        "Narkia",

        "Odin", 
        "Orion",
        "Oberyn", 
        
        "Pascal",
        "Paragon",
        "Phoenix",        
        "Perseus",

        "Icarus",

        "Jabberwock",

        "Kaiju",
        "Kali", 
        "Kai",
        
        "Leviathan",
        "Lucifer",
        "Leonardo",
        "Lysandra",

        "Mothra",
        "Mara",
        "Midas",
        "Medusa",
        "Maverick",

        "Nyx",
        "Naxius",
        "Nova",        
        "Narcissus",

        "Osiris",


        "Rodan",
        "Rhea",
        "Ramses",
        "Rowan",
        "Ripley",
        "Ragnar",
        "Rogue", 
        "Raven",

        "Solaris",
        "Sylar",
        "Strider",
        "Spartacus",
        "Storm",
        "Sabrina",
        "Seraph",
        
        "Tyrion",
        "Trinity",
        "Thorin",
        "Thalia",
        "Titan",

        "Vega",

        "Wolverine",

        "Xena",

        "Zeus",
        "Zorro",
        ]
    
    Surnames = [
        "Bladebreaker",
        "Bonecrusher",
        "Beastmaster",
        "Bloodfist",
        "Blackthorn",
        "Bluesky",
        
        "Dreamchaser",
        "Duskwatcher",
        "Darkstone",

        "Maximoff",     

        "Wilson",

        "Ironclad",
        "Tusker",
        "Stormhowler",
        "Mudwalker",
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
        
        
        "Flameseeker",
        "Frostweaver",
        "Firewhisper",
        "Frostfire",

        "Greycloud",
        "Goldeneye",

        "Highwind",

        "Ironshard",
        
        "Lightstep",

        "Moondancer",

        "Nightwhisper",
        
        "Riverblade",
        "Redraven",

        "Stormforge",
        "Stardust",
        "Sunfire",
        "Shadowhawk",
        "Stormwatcher",
        "Sandshifter",
        "Starweaver",
        "Stormrider",

        "Thunderforge",
        "Trueblade",
        "Twilightbearer",

        "Windrunner",
        "Warbrute",
        "Whitewave",
        "Whitewolf",
        "Windweaver",

    ]


    Humans = [
        "Arthur",
        "Ambrose",
        "Albus",
        "Albertus",
        "Aragorn",
        "Anselm",
        "Augustine",
        "Aubert", 
        "Anastasia",
        "Augustus", 
        "Alexei",
        "Attila",
        "Audrey",
        "Anastasia",
        "Avis", 
        
        "Beowulf",
        "Belos",
        "Boudicca",
        "Beau",
        "Blanche",
        "Brian",
        
        "Cid",
        "Cicero",
        "Caesar",
        "Cleopatra",
        "Catherine",
        "Claudius", 
        "Colbert",
        "Christopher",
        
        "Denis",
        
        "Emelot",
        "Ernest",
        "Elisabeth",
        "Euphemia",
        "Edric",
        "Edward",
        "Emma",

        "Frank",

        "George",

        "Hubert",

        "Isildur",
        
        "Jean",

        "Katarina",
        
        "Lancelot",
        "Lucy",

        "Menard",
        "Mathilda",
        "Martin",
        
        "Nicole",
        "Neil",
        "Nathaniel",
        
        "Oda",
        
        "Herbin",

        "Jasper",
        "James", 
        
        "Red",
        "Reginald",
        "Regina",
        
        "William",
        "Wilmot",
        
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
        "Nero",
        "Ovid",

        


        
        "Gregory",
        
        "Horace",

        "Isabella",
        "Ivan",

        "Jeremias",
        "Jerome",
        
        "Luz",
        "Louis",
        "Lazarus",

        "Maria",

        "Nicholas", 
        
        "Olga",

        "Percy",
        "Percival",
        "Peter",

        "Rollo",
        "Rasputin",
        
        "Spartacus",

        "Tatiana",
        "Thomas",
        "Theoden",
  
        "Vigo",
        "Vladimir",
        "Virgil",
        
        ""]
    
    Human_Surnames = [
        "Aragon", 
        "Agosto",
        "Astorio",
        "Aurelius",
        "Antonius",
        "Athens",

        "Borgia",
        "Bourbon",
        "Black",
        "Blackbeast",
        "Blackbeard",
        "Blackbear",

        "Capulet",
        "Camelot",
        "Castilla",
        "Capetian",
        "Calabra",
        "Carolingian", 
        "Clawthorne",
        "Comnenus",
        
        "DuLac",
        "DeLion",
        "d'Anjou",
        "d'Arc",
        "d'Aquitaine",
        "Dragomir", 

        "Flavius",
        
        "Gondor",

        "Hohenstaufen",
        "Hapsburg",

        "Lancaster",

        "Macedon",
        "Montague",
        "Medici",
        "Merovingian",

        "Normandy",
        "Navarre",

        "Plantagenet",
        "Pendragon",
        "Plantin",
        "Palaiologos",
        
        "Rohan",
        "Romanov",
        "Rurikid",

        "Stuart",
        "Sforza",
        "Sparta",

        "Tudor",
        "Tiberius",
        
        "Valerius",
        
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

        
        "Chergoba",

        "Dostoyevsky",
        "Dundragon",
        "Domine",

        "Falone",

        "Ling",

        "Marivaldi",
        "Mei",

        "Pendragon",
        "Pisacar",
        "Picasso",
        "Pin",
        
        "Rosedawn",
        "Ramondo",

        "Shin",
        "Sum",

        "Tan",

        "Violetdawn",
        "Valois",
        "Visigoth",
        "Valdemar",

        "Wessex",
        "Windsor",
        "Wanderlust",
        
        "York",

        ""]
    if Type == "Human":
        Names += Humans
        Surnames += Human_Surnames
        Name = NewName(
            Names = Names,
            onset = [
                    'Mar', 'Tar', 'Jen', 'Cal', 'Ser', 
                    'Bran', 'Ari', 'Viv', 'Lor', 'Rav',
                    'Edd', 'Rob', 'Bran', 'Rick', 'Jon', 
                    'Sans', 'Ary', 'Cers', 'Tyr', 'Jaime', 
                    'Dav', 'Bri', 'Marga', 'Theon', 'Sam'
                    ],
            nuclei = [ '','','','','','','',
                    'a', 'e', 'i', 'o', 'u', 
                    'ae', 'ie', 'io', 'ou', 'ia', 
                    'ara', 'ena', 'ili', 'ora', 'una',
                    'ard', 'ert', 'on', 'an', 'or', 
                    'en', 'a', 'ei', 'ie', 'yn', 
                    'elle', 'ary', 'ery', 'ora', 'enna'
                    ],
            codas = ['','','','','','','',
                    'nor', 'las', 'wen', 
                    'thor', 'fin', 'mir', 'dan', 'ion', 
                    'bert', 'vian', 'mond', 'gan', 'dor',
                    'ton', 'ster', 'well', 'wyn', 'mont', 
                    'ford', 'snow', 'hill', 'pool', 'water', 
                    'fing', 'rick', 'mond', 'son', 'lan',
                    ]
            ) 
        Surame = NewName(
            Names = Surnames,
            onset = [
                    'Ash', 'Black', 'Green', 'Fair', 'Storm', 
                    'Wolf', 'Red', 'Iron', 'Swift', 'Bright', 
                    'High', 'Dark', 'Gold', 'White', 'Frost',
                    'Stark', 'Lann', 'Barr', 'Targ', 'Grey', 
                    'Bol', 'Tar', 'Mart', 'Ty', 'Frey', 
                    'Arr', 'Bael', 'Cleg', 'Har', 'Um'
                    ],
                nuclei = ['','','','','','','',
                    'wood', 'field', 'stone', 'water', 'wind', 
                    'fire', 'hill', 'dale', 'ford', 'brook', 
                    'shaw', 'ridge', 'bourne', 'thorn', 'lee',
                    'ath', 'eon', 'eon', 'ary', 'joy', 
                    'ton', 'th', 'ell', 'ly', 'dor', 
                    'law', 'ish', 'ane', 'law', 'ber'
                    ],
                codas = ['','','','','','','',
                    'ton', 'son', 'worth', 'ford', 'hart', 
                    'lock', 'well', 'bridge', 'by', 'shaw', 
                    'land', 'man', 'ley', 'end', 'more',
                    'well', 'ster', 'ford', 'hall', 'moor', 
                    'wick', 'wood', 'wind', 'stream', 'vale', 
                    'gate', 'keep', 'tower', 'glen', 'ridge'
                    ])
        return Name + ' ' + Surname
                

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
        "Astralborn",
        "Azel",
        
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
        "Celtana",
        "Certhel",
        "Cezar",
        "Chaelana", 
        "Chathi",
        "Chen",
        "Chi",
        "Christopher",
        "Clagnemart",
        "Claira",
        "Clark",
        "Colart",
        "Conan",
        "Constance", 
        "Cuarion",
        "Curie",
        "Curu",
        
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
        
        

        
        
        "Daneloth",
        "Dartagnan",
        "Dartañan",
        "Dartagnan",
        "Dartañan",
        "David",
        "Dawnpath", 
        "Dawnwalker",
        "Del",
        "Dilan",
        "Dineloth",
        "Donael",
        "Douglas",
        "Dont",
        "Dorn",
        "Dorian",
        "Doliel", 
        "Dorn",
        "Dramo",
        "Draven",
        "Drusilia",
        "Dumein",
        "Durgwen",

        "Earendil",
        "Eberk",
        "Eda",
        "Edric", 
        "Ela",
        "Elandrial",
        "Elama",
        "Elari",
        "Elbereth",
        "Elenia",
        "Elendil",
        "Elendil",
        "Elenia",
        "Ele", 
        "Elendil",
        "Elerinna",
        "Elevas",
        "Eli",
        "Elia",
        "Eli",
        "Elidyr",
        "Elien",
        "Elin",
        "Elle", 
        "Elladan",
        "Elma",
        "Elphaba",
        "Elpetor",
        "Elrieth",
        "Elrohir",
        "Elros",
        "Eluin",
        "Elwing",
        "Elzevir", 
        "Elye",
        "Elyl",
        "Elys",
        "Ema",
        "Emma",
        "Emmy",
        "Ender",
        "Endor",
        "Enialis",
        "Enna", 
        "Eol",
        "Erafe",
        "Eran",
        "Erdan",
        "Erestor",
        "Erevan",
        "Erwin",
        "Espar",
        "Esmeralda",
        "Esvele", 
        "Eufemia",
        "Euler",
        "Eurin",
        "Evadne",
        "Evandel",
        "Evanescense",
        "Eve",
        "Evidam",
        "Eyla",

        "Faelir", 
        "Faen",
        "Faera",
        "Fae",
        "Faethis",
        "Faila",
        "Fai", 
        "Falchion",
        "Fandel",
        "Fan",
        "Fanal", 
        "Faelir",
        "Faen",
        "Faera",
        "Faethis",
        "Fai",
        "Faila",
        "Falchion",
        "Fandel",
        "Fan",
        "Fanal",
        "Fandel",
        "Fandral",
        "Fara",
        "Faral",
        "Faelorn",
        "Faralin",
        "Farol",
        "Feanor",
        "Felicity",
        "Felosial",
        "Fen",
        "Fera",
        "Feralia",
        "Featherspark",
        "Felan",
        "Feravel",
        "Feremar",
        "Feyla",
        "Feylin",
        "Filius",
        "Fingolfin",
        "Firael",
        "Foli",
        "Forestmoon",
        "Forestflower",
        "Forestheart",
        "Forojol",
        "Fral",
        "Frelia",
        "Freya",
        "Froemar",
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

        "Galadriel",
        "Galdor",
        "Galindan",
        "Gara",
        "Gawain",
        "Gael",
        "Gara",
        "Gerngwen",
        "Glorfindel",
        "Goldleaf",
        "Gus",
        "Goku",
        "Gokun",
        "Gokune",
        "Galdric",
        "Galin",
        "Galor",
        "Galthor",
        "Glyn",
        
        "Haedir",
        "Hadarai",
        "Halana",
        "Heian",
        "Holara",
        "Horatio",
        "Horneth",
        "Huroz",
        
        "Iannien",
        "Iellan",
        "Ienor",
        "Ilanis",
        "Ilebellis",
        "Ilima",
        "Immeral",
        "Innil",
        "Irion",
        "Ira",
        "Irui",
        "Iorhel",
        "Isolde",
        "Ivellios",
        "Iusus",
        "Iylar",

        "Jareth",
        "Jar",
        "Jarsali",
        "Jay",
        "Jelenet",
        "Jorel",

        "Kai",
        "Kalel",
        "Kan",
        "Kari",
        "Karnwyl",
        "Karn",
        "Kay",
        "Keiro",
        "Keyleth",
        "Kern",
        "Kratos",
        "Kylar",
        
        "Laucian",
        "Lael",
        "Laer",
        "Larin",
        "Lauriel",
        "Laurin",
        "Leshanna",
        "Lia",
        "Liliandil",
        "Liadon",
        "Lilis",
        "Lirn",
        "Lithor",
        "Lora",
        "Loria",
        "Loria",
        "Loriel",
        "Lorin",
        "Lue",
        "Lura",
        "Luthien",
        "Lyfaen",
        "Lyrial",
        
        "Mai",
        "Maindaer",
        "Malkis",
        "Mara",
        "Maleficent",
        "Maralen",
        "Maur",
        "Melehtion",
        "Melwen",
        "Mella",
        "Meriele",
        "Merric",
        "Mialee",
        "Mial",
        "Mindartis",
        "Mial",
        "Mistwatcher",
        "Morhel",
        "Morwen",
        "Mya",
        "Mykar",
        "Myla",
        "Myr",

        "Nae",
        "Naeris",
        "Naivara",
        "Nail",
        "Naila",
        "Nailo",
        "Narkia",
        "Narn",
        "Neo",
        "Neuse",
        "Newa",
        "Noarnad",
        "Nora",
        "Norul",
        
        "Oceania",
        "Oceanwalker",
        "Oceansong",
        "Odalia",
        "Ofandrus",
        "Oi",
        "Olimion",
        "Ol",
        "Oren",
        "Ostoroth",
        "Oromis",
        
        "Paelia",
        "Pascal",
        "Pegnith",
        "Peren",
        "Peri",
        "Peria",
        "Pharana",

        "Quildohtare",
        "Quelenna",
        "Quinar",
        
        "Rain",
        "Raine",
        "Raingaze",
        "Rael",
        "Raelim",
        "Raer",
        "Raen",
        "Ravenflow",
        "Ravenwatcher",
        "Ravenwatch",
        "Ridaro",
        "Relix",
        "Ren",
        "Reseo",
        "Riardon",
        "Rithel",
        "Rocenel",
        "Roden",
        "Roen",
        "Rolan",
        "Rolen",
        "Rua",
        "Rumathran",
        "Ryann",
        "Ryer",
        "Rym",
        
        "Sael",
        "Sai",
        "Sann",
        "Sariel",
        "Saynal",
        "Shava",
        "Soderac",
        "Sovelis",
        "Starwatcher",
        "Starwhisper",
        "Sudelrin",
        "Sumi",
        "Sumnes",
        "Syllin",
        "Sylvaranz",
        "Sylv",
        
        "Tauriel",
        "Thia",
        "Thranduil",
        "Tindecet",
        "Tris",
        "Trian",
        
        "Valance",
        "Vadan",
        "Valna",
        "Vanimial",
        "Vall",
        "Van",
        "Vanes",
        "Vax",
        "Vaxeldan",
        "Vex",
        "Vexhalia",
        "Viasta",
        
        "Wasanzi",
        "Wil",
        "Wenion",
        
        "Xanapia",
        "Xyrkraken",
        "Xylia",
        
        "Yael",
        "Yaeldrin",
        "Yesstina",

        "Zalta",
        "Zamior",
        "Zarivol",
        "Zay",
        "Zelaerys",
        "Zelir",
        "Zeren",
        "Zia",
        "Zorro"
        ]

    ElvenSurnames = [
        "Dawntreader",
        "Duskweaver",
        "Dreamweaver",

        "Goldenwood", 
        "Glimmerwing",

        "Leafdancer",
        "Lighthaven",
        "Lightbearer",

        "Moonshadow",
        "Moonglow", 
        "Moonbeam", 
        "Morningstar",

        "Nightbreeze",
        "Nightsong",
        
        "Riverwind",
        "Raindancer",

        "Silverleaf",
        "Sunweaver",
        "Stardancer",
        "Silverleaf",
        "Starshine",
        "Silverbrook",
        "Skydancer",
        "Sunglow",
        "Sunshadow", 
        "Starfall",
        
        "Thornheart",
        "Twilightveil", 

        
        "Mistwood",
        "Dreamshade",
        "Frostvale",
        "Leafshade",
        "Goldenbough",
        "Silverpine",
        "Mistwalker",
        "Dawnshadow",
        "Dreamsong",
        "Nightshade",
        "Starleaf",
        "Moonrise",
        "Sunblade", 
        "Mistbreeze",
        "Eveningstar",
        "Sundancer",
        "Whisperleaf",
        "Dreamcatcher",
        "Leafwhisper", 
        "Starweaver",
        "Sunshard",
        "Silentbrook",
        "Glimmermoon",
        "Nightriver",
        "Silverwind", 
        "Lightshade",
        "Moondancer",
        "Frostleaf",
        "Starbloom",
        "Rainwhisper",
        "Glimmerstone", 
        "Nightglow",
        "Starflight",
        "Rainshadow", 
        

        "Crystalbrook",

        "Dreamlight",
        "Dawnlight",
        "Dewshine",

        "Eldar",
        "Emeraldshade",
        "Ebonwood",

        "Glimmerleaf",
        "Glimmershade",
        "Goldendew",
        "Goldenstar",
        "Goldenrain",
        "Goldensong",
        "Goldenleaf",

        "Leafdancer",
        
        "Moonchild",
        "Moonsinger",
        "Moonbrook",
        "Moonstone", 
        "Moonlace",

        "Nightrunner",
        "Nightstar",
        "Nightsinger",

        "Twilightleaf",
        "Twilightbloom",

        "Silverkin",
        "Starwhisper",
        "Silversong",
        "Sunweaver",
        "Starcaller",
        "Sunburst",
        "Silverstream",
        "Starbright",
        "Silentmoon",
        "Shimmerwood",
        "Sapphireglow", 
        "Shadowvale", 
        "Sunstone",
        "Starfire", 
        "Sunsinger",
        "Shadowsong",
        "Skywhisper",
        "Silverfrost",
        "Sunspark",

        "Twilightseeker",
        "Twilightmist",

        "Woodlander",
        "Whispershade",
        "Whisperbreeze",
        "Windrunner",
        "Whisperwind",

        ]

    if Type == "Elf":
        Names = Elves
        Surnames = ElvenSurnames
        

        
        Name = NewName(Names,
                onset = ['El', 'Al', 'Fel', 'Gal', 'Le'],
                nuclei = ['a','dri'],
                codas = ['el','rond']
                )

        Surname = NewNames(Surnames,
                onset = ['Wood', 'Whisper', 'Sun', 'Silver', 'Ocean'],
                nuclei = [''],
                codas = ['shade', 'song',
                         'wind','weaver','reader','wing','dancer','bearer','rain','glow','shine'],
                )
            

        FullName = Name + ' ' + Surname
        return FullName
    
    
    Giant = [
        "Aureliu",
        "Agrippa",
        "Ananias",
        "Atlas",
        "Atlumun",
        "Atlaria",
        
        "Bunce",
        "Bridget",
        
        "Calamundis",
        "Colossu",
        
        "Droroc",
        
        "Gerdur",
        "Grad",
        
        "Bunari",
        "Casade",
        "Coeus",
        "Criu",
        "Hyperion",
        "Iapetu",
        "Cronu",
        "Thea",
        "Rhea",
        "Themis",
        "Memosyne",
        "Foebe",
        "Tethis",
        "Tezis",
        "Tethys",
        "Bunasas",
        "Calan",
        "Brasan",
        "Tialam",
        "Bundero",
        "Atlar",
        "Caramu",
        "Cadet",
        "Flasari",
        "Geroro",
        "Bundun",
        "Andurd",
        "Draro",
        "Tisar",
        "Coni",
        "Bunfunfu",
        "Bundunde",
        "Candu", "Teri",
        "Casaris",
        "Candun", "Andun",
        "Caris", "Bunasa", "Tialas",
        "Brisar", "Bumo", "Bunde",
        "Ragnarok", "Arzur", "Arturus",
        "Bedivere", "Bedwyr", "Bohort",
        "Bors", "Cai", "Caradoc",
        "Caradog", "Culch", "Elaine",
        "Enid", "Enide", "Gaheriet",
        "Gaheris", "Galaad", "Galahad",
        "Gareth", "Garez", "Gauvain",
        "Goven", "Gawain",
        "Geraint",
        "Gualguainu",
        "Guendolen",
        "Guendolena",
        "Guenevere", "Guinivere",
        "Guiomar", "GynezGyneth",
        "Hector", "Hoel", "Igerna",
        "Igraine", "Iseult", "Iseut",
        "Isolda", "Isolde", "Kay",
        "Lancelot", "Loncelote",
        "Lancelote", "Laudine", "Linet",
        "Lionel", "Lionesse", "Lionors",
        "Lohengrin",
        "Loherangrin", "Lot", "Luned",
        "Lunete", "Lynet", "Lynette",
        "Lyones", "Lyonesse",
        "Lyonors", "Medraut", "Medrod",
        "Mordred", "MerlinMyrdin",
        "Merlinus", "Merdinus",
        "Modred", "Mordred", "Morgaine",
        "Morgen", "Nimue", "Vivien",
        "Niniane", "Olwen",
        "Owain", "Parsifal", "Parzival",
        "Percival", "Pellam", "Pelleas",
        "Pellejand",
        "Pellejan",
        "Pelles", "Beli", "Pellinore",
        "Percival", "Peredur", "Tristan",
        "Drust", "Drustan", "Urien",
        "Uther", "Uthyr", "Walganus",
        "Yiseut", "Iseult", "Yisolt",
        "Iseult", "Yivain", "Owain", "Yiwain",
        "Lynn",
        "Lunete",
        "Eluned",
        "Lojengrin", "Lorraine", "Lot",
        "Gaius", "Iseult", "Gawain", "Garez",
        "Enid", "Helen", "Caratacos",
        "Caradog", "Bors", "Bedivere",
        "Tigsar", "Morgan", "Arthur",
        "Oceanus",
        "Artorius", "Avalonia",
        "Branwen", "Caledor",
        "Dagonet",
        "Ectoriu", 
        "Elainea",
        "Fionor",
        "Galaz",
        "Guerrier", "Hengist", "Igrainia", 
        "Jernon", "Kaledvoulc", "Llynis",
        "Mabonagrain", "Niviene", "Orkney", 
        "Pelinora",
        "Questar", "Rhience",
        "Segwarides",
        "Tintagil", "Urian", 
        "Vortigern",
        "Yigerne",
        "Zephyros",
        "Ambershade", 
        "Blaiddyd",
        "Caliburnu",
        "Duirward",
        "Elthain",
        "Galajault",
        "Hiberna", 
        "Isoude",
        "Julanar",
        "Kelpius",
        "Lucanor",
        "Meliodas",
        "Nimuena", 
        "Olyndicus",
        "Pellamor",
        "Querent",
        "Rowenar",
        "Siluria",
        "Tristanus", 
        "Ulfius",
        "Vivienus",
        "Yisbaden",
        "Argante",
        "Brocéliande",
        "Corbenic", 
        "Dinadan",
        "Evrain",
        "Guiber",
        "Hoelus",
        "Ider",
        "Joyous",
        "Kerwyn", 
        "Lynettea",
        "Moire",
        "Niniane",
        "Oberon",
        "Pendragon",
        "Questine", 
        "Roncesvalles",
        "Seraphiel",
        "Tegid",
        "Utherius",
        "Vortimer", 
        "Ywaineth",
        "Zephyrius",
        "Ambrosius",
        "Bronwen",
        "Caerleon",
        "Dindrane", 
        "Elyan",
        "Galeran",
        "Harlequin",
        "Isolier",
        "Jaufré",
        "Kynereth",
        "Lyones", 
        "Morgause",
        
        
        "Ossian",
        
        "Palamedes",
        
        "Quex",
        
        
        "Sadb",
        
        "Taulurd",
        
        "Uriens",
        
                
        "Yisbail",
        
        "Cassius",
        "Drusus",
        "Flavia",
        "Gaius",
        "Hadrian",
        "Julia",
        "Lucretia",
        "Maximu",
        "Octavia",
        "Priscus",
        "Romulus",
        "Sabina",
        "Tacitu",
        "Valeriu",
        "Vitu",
        "Brutu",
        "Cornelia",
        "Decimu",
        "Faustina",
        "Gracchu",
        "Horatia",
        "Livia",
        "Marcellu",
        "Nerva",
        "Pontius",
        "Quintus",
        "Regulus",
        "Sergius",
        "Tiberius",
        "Varinia",
        "Antonia",
        "Claudius",
        "Diana",
        "Felix",
        "Germanicus",
        "Helena",
        "Juno",
        "Lucius",
        "Minerva",
        "Octavian",
        "Portia",
        "Remus",
        "Scipio",
        "Titus",
        "Vespasian",
        "Balbus",
        "Cicero",
        "Draco",
        "Fabius",
        "Galba",
        "Hercules",
        "Julius",
        "Lucretius",
        "Martialis",
        "Nero",
        "Paulinus",
        "Rufus",
        "Seneca",
        "Merlina",
        "Gaiadoc",
        "Lancelian",
        "Guinerva",
        "Aureliot",
        "Vivianu",
        "Galahadrian",
        "Octarthur",
        "Elynia",
        "Cassilote",
        "Drustus",
        "Helenaire",
        "Guainu",
        "Titania",
        "Brutigern",
        "Flaviad",
        "Luciuslyn",
        "Marcian",
        "Nimoria",
        "Guenu",
        "Viviane",
        "Tristianu",
        "Agravainu",
        "Maximor",
        "Bellereu",
        "Morgausea",
        "Lancelotu",
        "Priscival",
        "Romelein",
        "Sabinael",
        "Taciturn",
        "Valkyriu",
        "Bedwiru",
        "Caratacu",
        "Dianadoc",
        "Faustelot",
        "Gwenyivaru",
        "Herculot",
        "Lunetea",
        "Octaviane",
        "Pontifex",
        "Quintavere",
        "Regulad",
        "Senegalad",
        "Tituriu",
        "Vespaval",
        "Caiulu",
        "Drusin",
        "Felixor",
        "Germanica",
        "Horatine",
        "Luneliu",
        "Minervadoc",
        "Balbusu",   # from 'balbus', meaning stammering or inarticulate
        "Clunclu",   # a twist on 'cluncus', a nonsense word mimicking 'clumsy'
        "Nugaxiu",   # from 'nugax', meaning trivial or petty
        "Lirpalo",   # from 'lirpa', a playful twist on a nonexistent Latin word
        "Brutulu",   # a play on 'brutus', meaning heavy, dull, or stupid
        "Pedicu",    # sounds like a Latin word but is actually nonsensical, implying something foot-related
        "Flatulu",   # humorous twist on 'flatus', meaning blowing or a gust
        "Stultor",   # from 'stultus', meaning foolish
        "Asinino",   # from 'asininus', pertaining to a donkey, or foolish
        "Confusio",  # from 'confusio', meaning confusion
        "Caudex",    # literally a block of wood, used to mean blockhead
        "Caputus",   # play on 'caput', head, implying a 'big head'
        "Mogonus",   # a made-up word that sounds like a Latin name but is just silly
        "Semicapru", # 'half-goat', nonsensical and humorous
        "Ineptor",   # from 'ineptus', meaning inappropriate or silly
        "Somniculo", # a playful take on 'somniculus', little sleeper
        "Naso",      # meaning nose, implying someone with a big nose
        "Bovido",    # from 'bovidus', ox-like, implying slow-witted
        "Tardigradu",   # slow stepper, a play on the term 'tardigrade'
        "Bumbulu",      
        "Blunderu",     
        "Lorariu",      
        "Nonplusiu",    
        "Gurguliu", 
        "Snoru",        
        "Cacofonix",    # from 'cacophony', implying a loud, dissonant noise
        "Vacu",         # meaning empty, or vacuous
        "Glutu",        # a twist on 'glutus', giving the impression of gluttony
        
        "Aurelien",
        "Antonialot",
        "Aeliana",
        "Augustu",
        "Aquila",
        "Artorius",
        
        "Bacchu",
        
        "Camilla",
        "Cato",
        "Claudiad",
        
        "Domitian",
        "Dido",
        "Domicia",

        
        "Fauna",
        "Florian",
        "Florianel",
        "Flunfum",
        
        "Gratian",
        "Gordian",
        "Galainu",
        
        "Hadriana",
        "Honori",
        "Honoriu",
        "Helenor",

        "Igrainiu",
        
        "Jovian",
        "Jadriana",
        "Jonoriu",
        "Julianor",
        "Jelenor",
        "Juniu",
        
        "Lin",
        "Linu",
        "Laris",
        "Lariu",
        "Lucion",
        "Ludicro",      
        "Ludicru",      
        
        "Mercuriu",
        "Mars",
        "Marcelot",
        
        "Numa",
        "Nentres",
        
        "Ovid",
        "Octaviad",
        "Oblivio",  
        
        "Proserpina",
        "Plini",
        "Pliniu",
        "Percivu",
        "Porcia",
        
        "Quirinus",
        
        "Rea",
        "Rotder",
        "Rience",
        "Remulu",
        
        "Saturn",
        "Sever",
        "Scipiogern",
        
        "Tull",
        "Trajan",
        "Titan",
        "Tibergain",

        "Vergil",
        "Vitell",        
        "Vespasia",
        "Vestia",
        "Vulcan",
        "Varliniu",
        "Vesta",
        "Vortigan",

        "Zilchais",

        ]
    if Type == "Giant":
        Names = Giant
        Surnames = Giant

        onset = [    "Au", "Ag", "An", "At", "Al", "Ar", "As", "Ac", "Am",     "Br", "Bu", "Ba", "Be", "Bo", "Bl", "Bi", "By", "Be", "Bi",     "Ca", "Co", "Cr", "Cu", "Ce", "Ci", "Cl", "Ca", "Ch", "Cu",     "Do", "Dr", "Da", "Di", "De", "Du", "Da", "Do", "Di",     "El", "En", "Ed", "Eg", "Er", "Es", "Et", "Eu", "Ev", "Ei",     "Fa", "Fl", "Fe", "Fo", "Fu", "Fa", "Fi", "Fo",     "Ga", "Go", "Gu", "Ge", "Ga", "Gr", "Gi", "Ga",     "He", "Ho", "Ha", "Hu", "Hy", "He", "Ho", "Ha",     "In", "Ig", "Is", "Id", "Io", "Iv", "Il", "Im",     "Ju", "Jo", "Ja", "Je", "Jo", "Ju", "Ji", "Jo",     "Ka", "Ke", "Ki", "Ko", "Ku", "Ka", "Kn", "Kr",     "Li", "Lo", "La", "Le", "Lu", "Ly", "La", "Li",     "Ma", "Mi", "Me", "Mo", "Mu", "Ma", "Me", "Mi",     "No", "Ne", "Ni", "No", "Nu", "Ne", "Na", "Ni",     "Oc", "Or", "Os", "Ov", "Ol", "Od", "Oc", "Op",     "Pe", "Po", "Pa", "Pi", "Pu", "Pe", "Pr", "Po",     "Qu", "Qu", "Qu", "Qu", "Qu", "Qu", "Qu", "Qu",     "Re", "Ro", "Ra", "Ri", "Ru", "Re", "Ro", "Ra",     "Sa", "Se", "Si", "So", "Su", "Sa", "Sc", "St",     "Ti", "Tr", "Ta", "To", "Tu", "Ti", "Th", "Te",     "Va", "Ve", "Vi", "Vo", "Vu", "Va", "Vi", "Ve",     "Zi", "Zo", "Zu", "Ze", "Za", "Zo", "Zi", "Ze"]
        nuclei = [    "a", "e", "i", "o", "u", "ae", "ai", "ea", "ie", "ou",     "ia", "ara", "ena", "ili", "ora", "una", "ion", "ian", "ein",     "ian", "io", "ua", "eo", "ia", "ie", "ai", "eo", "iu", "ui"]
        codas = [    "u", "ix", "as", "is", "or", "un", "ia", "u", "al",     "ar", "um", "an", "in", "el", "on", "en", "er", "ar",     "ad", "or", "ia", "ic", "os", "id", "ot", "ul", "ud",     "or", "an", "ur", "en", "on", "al", "ir", "ia", "es",     "ar", "et", "ia", "or", "or", "ia", "us", "in", "al",     "or", "er", "en", "is", "an", "u", "ic", "u", "in",     "u", "an", "er", "u", "ad", "os", "es", "an", "or"]
        
        Name = NewName(Names,onset,nuclei,codas)
        Surname = NewName(Surnames,onset,nuclei,codas)
        
        FullName =  Name + ' ' + Surname + "son"

        return FullName


    Orcs =[
        "Aldis",
        "Arn",
        "Asfrid",
        "Asterix",
        "Axe",
        "Agmund",
        "Alrek",
        
        "Balli",
        "Bjorn",
        "Blod",
        "Bulak",
        "Brondar",
        "Bragi",
        
        "Carguk",
        
        "Erek",
        "Erik",
        "Engli",
        "Einar",
        "Eyvind",
        
        "Farkang",
        "Frode",
        
        "Gell",
        "Gnarsh",
        "Gorga",
        "Grog",
        "Grigi",
        "Gro",
        "Greiland",
        "Geirmund",
        "Gunnar",
        
        "Halvard",
        "Harald",
        "Henk",
        "Holg",
        "Hosvir",
        "Hakon",
        
        "Idefix",
        "Ingrid",
        "Iuli",
        "Inge",
        "Ivar",
        
        "Jor",
        "Jarl",

        "Ketil",
        "Knute",
        
        "Lagazi",
        "Leif",
        
        "Merida",
        "Magnar",
        
        "Ñor",
        
        "Obelix",
        "Olof",
        "Ovif",
        "Ozerix",
        "Oddr",
        "Ormr",
        "Orm",
        
        "Panoramix",
        
        "Ragnar",
        "Ragnarr",
        "Ragnarra",
        "Ragnara",
        "Rolf",
        
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
        "Sigurd",
        "Skarde",
        "Snorri",
        "Sorli",
        "Steinar", 
        
        "Thorkell", 
        "Thorald",
        "Thorlak",
        "Trag",
        "Trarik",
        "Tyrfing",
        "Torrad",
        "Thrainn",
        "Toste",
        "Trygg",

        "Urd",
        "Urda",
        "Ulf",
        
        "Vifil",
        "Valgard",
        "Vidar",
        
        "York",
        "Yurk",
        "Yngvar",
        
        ]
    OrcSurnames = [
        # Inpirations: Vikings
        "Aldisson",
        "Atlisson",
        "Borksson",
        "Fastfulfsson",
        "Osvifsson",
        "Skardisson",
        "Tofisson",
        "Orksson",
        "Fangsson",
        "Ardisson",
        "Arksson",
        "Hosvirsson",
        "Skegsson",
        "Thoralsson",
        "Olofsson",
        "Odinson",
        "Herdisson",
        "Ingrisson",
        "Skusson",
        "Svasson",
        "Ensson",
        "Vikingsson", 
        "Vifsson",
        "Iulisson",
        "Sveinsson",
        "Throlaksson",
        "Jorsson",
        "Ballisson",
        "Yorksson",
        "Yurksson",
        "Ereksson",
        "Eriksson",
        "Arnsson",
        "Battlebreaker",
        "Warfist",
        "Strongaxe",
        "Ironclaw",
        "Stoneheart",
        "Firebrand", 
        "Stormcaller",
        "Thunderfury",
        "Battlescream",
        "Warchief",
        "Bloodaxe",
        "Skullsmasher", 
        "Ironjaw",
        "Shadowfury",
        "Bladesinger",
        "Marrowrend",
        "Ragehorn",
        "Boneshatter", 
        "Stonebreaker",
        "Thunderclap",
        "Goreaxe",
        "Frostmaul",
        "Darkfury", 
        "Stormblade",
        "Earthshaker",
        "Firefist",
        "Blooddrinker",
        "Ragefury",
        "Battlerager",
        "Warfang", 
        "Goreclaw",
        "Steelbite",
        "Bladestorm",
        "Skullsplitter",
        "Maulfist", 
        "Bloodscream",
        "Stormfist",
        "Firemaul",
        "Shadowclaw",
        "Thundermaul",
        "Ironmaul",
        "Bonecrusher",
        "Rageblade",
        "Battleshout",
        "Goremaul",
        "Thunderaxe", 
        "Stormrend",
        "Bladeshadow",
        "Gorebrand",
        "Frostfury",
        "Shadowmaul", 
        "Battlemaw",
        "Rageclaw",
        "Bladefury",
        "Gorethorn",
        "Frostclaw",
        "Thunderfist",
        "Skullcrusher",
        "Ironfury",
        "Ragesong",
        "Stormfury",
        "Firethorn", 
        "Thunderblade",
        
        "Bloodmaul",
        "Battlerage",
        "Bloodfury", 
        "Battleclaw",
        "Bladebreaker",

        "Gorebreaker",
        
        "Ironblade",

        "Maulsson",
        
        "Ulfsson",

        "Shadowrend",
        "Shadowbreaker",
        
        "Warthorn",
        "Warsong", 
        "Warblade",
        "Wasson",
        "Warsson",
        "Warysson",
        "Warmaul",
        "Warbreaker", 
        "Warclaw",

        f"{random.choice(Orcs)}sson",
        f"{random.choice(Orcs)}sson",
        f"{random.choice(Orcs)}sson",
        f"{random.choice(Orcs)}sson",
        f"{random.choice(Orcs)}sson",
        f"{random.choice(Orcs)}sson",
        f"{random.choice(Orcs)}sson",
        f"{random.choice(Orcs)}sson",
        f"{random.choice(Orcs)}sson",
        f"{random.choice(Orcs)}sson",
        f"{random.choice(Orcs)}sson",
        f"{random.choice(Orcs)}sson",
        f"{random.choice(Orcs)}sson",
        f"{random.choice(Orcs)}sson",
        ]
    if Type == "Orc":
        Names = Orcs
        Surnames = OrcSurnames

        Name = NewName(Names,
                onset = [
                    "Orc",
                    "Ork",
                    "Grom", "Thun", "Varg", "Skol", "Bjorn", "Ragn", "Ulfr", "Hald", "Gunn", "Fjol", "Knut", "Brak", "Froth", "Halv", "Jot", "Mjol", "Njor", "Skag", "Thrud", "Valk", "Yngv", "Asgr", "Bar", "Dagr", "Eir", "Gorm", "Herj", "Ing", "Jarl", "Kael", "Loth", "Njal", "Ormr", "Rolf", "Snor", "Tor", "Ulf", "Vig", "Wulf", "Ymir"],
                nuclei = ["ar", "ur", "ir", "or", "an", "en", "in", "on", "un", "al", "el", "il", "ol", "ul", "ak", "ek", "ik", "ok", "uk", "as", "es", "is", "os", "us", "ra", "ro", "ri", "ru", "re"],
                codas = ["var", "vik", "lok", "gar", "gor", "mar", "mir", "nar", "ner", "nir", "nor", "nur", "rik", "rak", "rok", "ruk", "thak", "thok", "thuk", "val", "vol", "vul", "berg", "dott", "hild", "jorn", "mund", "rond", "stein", "stor", "ulf", "und", "vind", "vold", "laf", "lif", "lof", "lyf", "sig"]
                )

        Surname = NewNames(Surnames,
                onset = ["Blood", "Iron", "Wolf", "Rage", "Storm", "Frost", "Bear", "Fire", "Dark", "Grim", "Skull", "Bone", "Night", "War", "Shadow", "Thorn", "Eagle", "Raven", "Rock", "Spear", "Thunder", "Wind", "Blade", "Fang", "Forge", "Steel", "Troll", "Dragon", "Flame", "Might", "Fjord", "Horn", "Ice", "Stone", "Giant", "River", "Sea", "Snow", "Ash", "Elk", "Hawk", "Light", "Meadow", "Oak", "Pine", "Rain", "Savage", "Star", "Whale", "Wild"],
                nuclei = ["an", "en", "in", "on", "un", "al", "el", "il", "ol", "ul", "ak", "ek", "ik", "ok", "uk", "as", "es", "is", "os", "us", "ard", "erd", "ird", "ord", "urd", "arn", "ern", "irn", "orn", "urn", "all", "ell", "ill", "oll", "ull", "aft", "eft", "ift", "oft", "uft", "ang", "eng", "ing", "ong", "ung"],
                codas = ["sson","son", "gar", "var", "vik", "lok", "gard", "vold", "berg", "dott", "hild", "jorn", "mund", "rond", "stein", "stor", "ulf", "und", "vind", "laf", "lif", "lof", "lyf", "sig", "thor", "thul", "mark", "nir", "nur", "rik", "rok", "rul", "skar", "skul", "tar", "tor", "tur", "vik", "vol", "vul", "gorn", "grin", "gund", "hak", "hal", "han", "har", "horn", "hurt", "jok", "kel", "kell", "ker", "kin", "kon", "kor", "kun", "lok", "lom", "lon", "lor", "lun",
                         "sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson",
                         "sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson",
                         "sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson","sson",
                         ],
                )
            

        FullName = Name + ' ' + Surname

        return FullName
    Dwarves = []
    if npc.gender == "he":
        Dwarves_he = [
            "Alfredo",
            "Alfredus",
            "Antonio",
            "Antonius",
            "Antoniano",
            "Antonianus",
            "Aulario",
            "Aularius",
            "Aurelio",
            "Aurelius",
            "Blanco",
            "Blancus",
            "Enrique",
            "Enricus",
            "Enrico",
            "Fernando",
            "Fernandus",
            "Gonzalo",
            "Gonzalus",
            "Gravielo",
            "Gravielus",
            "Graviel",
            "Ineso",
            "Ignacio",
            "Ignacius",
            "Igon",
            "Igón",
            "Igonus",
            "Juanus",
            "Juan",
            "Juano",
            "Mario",
            "Marius",
            "Mariano",
            "Marianus",
            "Rafael",
            "Rafaelo",
            "Rafaelus",
            "Roberto",
            "Robertus",
            ]
        Dwarves += Dwarves_he

    if npc.gender == "she":
        Dwarves_she = [
            "Alfreda",
            "Antonia",
            "Antoniana",
            "Aularia",
            "Aurelia",
            "Blanca",
            "Enrica",
            "Fernanda",
            "Gonzala",
            "Graviela",
            "Juana",
            "Juani",
            "Maria",
            "Mari",
            "Marian",
            "Mariana",
            "Inés",
            "Ignacia",
            "Igona",
            "Rafaela",
            "Roberta",
            ]
        Dwarves += Dwarves_she
        
    if npc.gender == "they":
        Dwarves_they = [
            "Alfrede",
            "Alfredés",
            "Antonie",
            "Antoniés",
            "Antoniane",
            "Antonianés",
            "Aularie",
            "Aulariés",
            "Aureli",
            "Aurelie",
            "Aureliés",
            "Blanque",
            "Blanqués",
            "Enrique",
            "Enriqués",
            "Fer",
            "Fernan",
            "Fernande",
            "Fernandés",
            "Graviel",
            "Graviele",
            "Gravielés",
            "Gonzale",
            "Gonzalés",
            "Gonzál",
            "Ignacie",
            "Ignaciés",
            "Igone",
            "Igoné",
            "Igones",
            "Igonés",
            "Juane",
            "Juané",
            "Juanés",
            "Marie",
            "Marié",
            "Mariés",
            "Mariane",
            "Mariané",
            "Inese",
            "Ignacié",
            "Rafaele",
            "Rafaelé",
            "Roberte",
            "Roberté",
            ]
        Dwarves += Dwarves_they

    Dwarves += [
        
        
        
        "Ramon",
        "Ramona",
        "Eulario",
        "Paca",
        "Francisca",
        "Paco",
        "Francisco",
        "Antonio",
        "Leonor",
        "Juanes",
        "Juliana",
        "Ramono",
        "Angela",
        "Arturo",
        "Leandro",
        "Cornelio",
        "Feliz",
        "Jose",
        "Josejuan",
        "Joseramon",
        "Josealberto",
        "Josenrique",
        "Joseantonio",
        "Lucia",
        "Diego",
        "Armando",
        "Samuel",
        "Enrique",
        "Antonio",
        "Miguel",
        "Bernardo",
        "Alberto",
        "Adelaida",
        "Adelita",
        "Adora",
        "Adrian",
        "Agustin",
        "Agustina",
        "Ainara",
        "Ainoa",
        "Aitana",
        "Aitor",
        "Alba",
        "Alejandra",
        "Alejandro",
        "Alejo",
        "Alex",
        "Alfonso",
        "Alfredo",
        "Almudena",
        "Alonso",
        "Alvaro",
        "Amadeo",
        "Amancio",
        "Amaya",
        "Ambrosio",
        "Amparo",
        "Belen",
        "Anacleto",
        "Isabel",
        "Maria",
        "Sofia",
        "Angustias",
        "Anibal",
        "Anselmo",
        "Antonio",
        "Apolonio",
        "Araceli",
        "Armando",
        "Aroa",
        "Arsenio",
        "Arturo",
        "Ascensión",
        "Asunción",
        "Atanasio",
        "Atilio",
        "Aureliano",
        "Aurelio",
        "Avelina",
        "Azucena",
        "Baldomero",
        "Bárbara",
        "Bartolomé",
        "Basilio",
        "Beatriz",
        "Begoña",
        "Benita",
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
        "Custodio",
        "Dagoberto",
        "Damian", "Daniel",
        "Daniela", "Danilo",
        "Dariel", "Darío",
        "Debora",
        "Demetrio",
        "Desideria",
        "Desiderio",
        "Diego",
        "Domingo",
        "Domitilda",
        "Eberardo",
        "Edelmira",
        "Edmundo",
        "Eduardo",
        "Eladio",
        "Eleuterio",
        "Eligio",
        "Elisa",
        "Eliseo",
        "Elodia",
        "Emigdia",
        "Emiliano", "Emilio",
        "Encarnación",
        "Enriqueta",
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
        "Fina",
        "Flavia",
        "Flavio",
        "Flora",
        "Floro",
        "Fulgencio",
        "Fabio",
        "Gabriel",
        "Geraldo",
        "Gilberta",
        "Godofredo",
        "Gonzalo",
        "Gregoria",
        "Gregorio",
        "Grimaldo",
        "Guadalupe",
        "Guillermo",
        "Haroldo",
        "Hector",
        "Herminia",
        "Hernando",
        "Hortensia",
        "Humberto",
        "Iban",
        "Ignacia",
        "Ignacio",
        "Inés",
        "Iñigo",
        "Inmaculada",
        "Inocencio",
        "Isidora",
        "Isidoro",
        "Jacinta",
        "Jacinto",
        "Jeremías",
        "Jerónimo",
        "Jesusa",
        "Jimeno",
        "Jimena",
        "Jorge",
        "Jose",
        "Joseangel",
        "Joseantonio",
        "Josefa",
        "Joseluis",
        "Josemanuel",
        "Josemari",
        "Josemaria",
        "Juan",
        "Juana",
        "Juancho",
        "Juancarlos",
        "Juanfran",
        "Juanita",
        "Juanjosé",
        "Juanma",
        "Juanpablo",
        "Justina",
        "Justino",
        "Justo",
        "Kiko",
        "Laura",
        "Lázaro",
        "Leandro",
        "Lope",
        "Lucas",
        "Lucrecio",
        "Lucrecia",
        "Luisa",
        "Manolo",
        "Manola",
        "Manuel",
        "Marcelo",
        "Marcela",
        "Marcos",
        "Margarita",
        "Maribel",
        "Mario",
        "Marta",
        "Martín",
        "Mateo",
        "Mauro",
        "Melania",
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
        "Béforo",
        "Teoberon",
        "Jalisto",
        "Rostino",
        "Romartín",
        "Rorto",
        "Prospero",
        "Rosto",
        "Seldo",
        "Selda",
        "Aunara",
        "Artosta",
        "Juriano",
        "Juro",
        "Joseros",
        "Rosero",
        "Rosera",
        "Jura",
        "Jácaro",
        "Jimeno",
        "Rosario",
        "Fingido",
        "Anancio",
        "Anancia",
        "Pansiano",
        "Fertilio",
        "Constantina",
        "Jarana",
        "Morana",
        "Nora",
        "Olivia",
        "Olivio",
        "Noro",
        "Jarano",
        "Valido",
        "Valida",
        "Abela",
        "Adalina",
        "Adora",
        "Adriana",
        "Ana",
        "Antonia",
        "Basilia",
        "Beatriz",
        "Bonita",
        "Camila",
        "Candela",
        "Carmen",
        "Catalina",
        "Dolores",
        "Dominga",
        "Dorotea",
        "Elena",
        "Elicia",
        "Esmeralda",
        "Felipina",
        "Francisca",
        "Gabriela",
        "Imelda",
        "Ines",
        "Isabel",
        "Juana",
        "Leocadia",
        "Leonor",
        "Leta",
        "Lucinda",
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
        "Sofia",
        "Teodoro",
        "Ubaldo",
        "Vidal",
        "Wilfredo",
        "Ximen",
        "Yago",
        "Zaragoza",
        "Esteban",
        "Ignacio",
        "Julio",
        "Mauricio",
        "Nestor", 
        "Oscar",
        "Pablo",
        "Quirino",
        "Reynaldo",
        "Sergio",
        "Teo",
        "Ulises",
        "Vicente",
        "Xavier",
        "Ysmael",
        "Felipe",
        "Gerardo",
        "Horacio",
        "Isidro",
        "Jacobo",
        "Lorenzo",
        "Maceo",
        "Norberto",
        "Octavio",
        "Ponce",
        "Quique",
        "Raul",
        "Silverio", 
        "Toribio",
        "Ugo",
        "Victorino",
        "Waldo",

        "Adan",
        
        "Bartolome",

        "Celestino",
        
        "Demetrio",
        
        "Ernesto",
        
        "Fidel",
        
        "Guillermo",
        
        "Hilario",
        
        "Indalecio",
        
        "Joaquin",
        
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
        "Ximeno",
        "Xerxes",
        
        "Ysidro",
        "Yesid",
        
        "Zenon",
        "Zeferino",
        "Zacarias",

        ""]
    
    DwarvenSurnames = [
        "Aguaclara",  
        "Aguamarina",  
        "Aguirre",

        "Andino",
        "Anvilado",

        "Aullidometálico",   
        "Arguna",
        "Arguña",
        "Arroyo",
        
        "Astillaferro",   
        

        "Barboro",
        "Barbaroja",
        "Barbanegra",
        "Barbablanca",
        "Barbaplata",
        "Barbaferra",
        "Barbacobre",
        "Barbanieve",
        "Barbaflama",
        "Barbalarga",
        "Barbana",
        "Barbarecia",

        "Bellomonte",
        "Belmonte",

        "Buscagemas",
        "Buscarocas",
        "Buscaoros",
        "Buscaplata",

        "Castillo",
        
        "De la Fuente",
        "De la Forja",
        "De la Monta",
        "De la Vega",
        "Delareina",
        "Delmonte",
        "Delrey",
        
        "Forjanegra",
        "Forjablanca",
        "Forjaroja",
        "Forjareal",
        "Forjadoro",
        "Forjaura",
        "Forjador",
        "Forjarocas",
        "Forjalmas",
        "Forjalta",
        "Forjabaja",
        "Forjagemas",
        "Forjaplata",
        "Forjaferro",
        "Forjamares",
        "Forjaestaño",
        "Forjargenta",
        "Forjasangre",
        "Forjafilos",
        "Forjachizos",
        "Forjaruna",
        "Forjayunques",
        "Forjafuegos",
        "Forjaflama",
        "Forjaespina",

        "Fuegoforja", 

        "Guardamonte",
        "Guardapico",
        "Guardagema",
        "Guardaoro",
        "Guardargenta",
        "Guardahierros",
        "Guardaferro",
        "Guardaferrea",
        "Guardaluna",
        "Guardasol",

        "Leñaforja",
        
        "Montealtivo",
        "Montoya",
        "Montanza",

        "Oropeza",
        "Oropieza",

        "Profundador",
        "Portarrunas",

        "Rocantinero",

        "Temblaterra",

        "Valencia",
        "Viejomonte",

        
        
        
        
        "Cortez",
        "Navarro",
        "Esparza",
        "Del Toro",
        "Cervantes",
        "Mendoza",
        "Lopez de Oro",
        "Lopez",
        "Topacio",

        "Zambrano",
        "Bernal",
        "Herrera",
        "De la Cruz",
        "De las Nieves",
        "Piconevado",
        "De la Beta",
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
        "Moreno",
        "Pizarro",
        "Velazquez",
        "Estrella",
        "Salcedo",
        "Machado",
        "De Santiago",
        "Del Rio",
        "Argenta",
        "Argentez",

        "Luna",
        "Solis",
        "Miranda",
        "Rojas",
        "Ortega",
        "Ponce de Leon",
        "Marquez",
        "Fuentes", 
        "Dorado",
        "Belmonte",
        "Guevara",
        "Cordero",
        "Rico",
        "De la Mora",
        "Trujillo",
        "Sierra",
        "De las Casas",
        "Valiente",
        "Santos",
        "Mojica",
        "Reyes de Oro",
        "Briseno",
        "De la Torre",
        "Montes",
        "Montellano",
        "Monteagudo",
        "Montenueva",
        "Montenuevo",
        "Monteviejo",
        "Bellomonte",
        "Noblemonte",
        "Monterroble",
        "Roblemonte",
        "Montepicado",
        "Montanza",
        "Montarazo",
        
        
        "Soloro",
        
        "Orosol",
        
        "Uranio",
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
        "Toledano",
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
        "Piedraociosa",
        "Minaplata",
        "Piedrajoya",
        "Oroazul",  
        "Oroclaro",  
        "Plataclara",
        "Rubirote",
        "Joyamar",
        "Montediamante",
        "Monteamante",
        "Montemante",
        "Ororico",
        "Cavernoro",  
        "Platafuerte",
        "Gemestrella",
        "Hierroprofundo",
        "Hierrofundo",
        "Metalbrillante",  
        "Metalante",  
        "Oradelfuego",  
        "Orafuego",  
        "Fraguamaestra", 
        "Fraguaestra", 
        "Mazodehierro",  
        "Mazohierro",  
        "Mazoferro",  
        "Escudopiedra", 
        "Escupiedra", 
        "Corazondorada",   
        "Corazondoro",   
        "Martillazo", 
        "Picoagudo",  
        "Picogudo",  
        "Lingotedeoro",  
        "Lingoteoro",  
        "Lingoro",  
        "Cristalclaro",  
        "Crisclaro",  
        "Montañaminera",   
        "Montinera",   
        "Escudojoya",  
        "Escujoya",  
        "Ardorfuego",   
        "Aceroantiguo",  
        "Cascoduro",   
        "Piedrafuerte",  
        "Esmeraldaeterna",  
        "Esmeralterna",  
        "Piedradeluz",  
        "Piedraluz",  
        "Oroescondido",   
        "Orondido",   
        "Luzdemina",  
        "Luzmina",  
        "Relucienteplata",   
        "Hierrosagrado",  
        "Agujerojoya",  
        "Agujoya",  
        "Piedradevalor",   
        "Riolatente",  
        "Corazóndeacero",  
        "Oradelsol",  
        "Minadellago",  
        "Minalago",  
        "Grialdeplata",   
        "Escoriabrillante",  
        "Escoriante",  
        "Monteplata",  
        "Fuentedeoro",  
        "Fuenteoro",  
        "Cascodediamante",  
        "Cascodiamante",  
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
        "Cristazul",  
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
        "Oroblanco",
        "Oronegro",
        "Ororojo",
        
        "Guardiándeplata",  
        "Espiraldehierro",  
        "Tesoroabierto",   
        "Cumbredelplata",   
        "Cumbreplata",   
        "Piedrasagaz",  
        "Cadenadeacero",   
        "Cadenaferro",   
        "Pilardeoro",   
        "Lanzadeplata",   
        "Piedrasusurro",  
        "Rocíometálico",  
        "Lagodeesmeralda",
        "Valledejoyas",  
        "Manantialdeacero",  
        "Espadacristal",  
        "Cordilleraacero",
        "Almadeplata",  
        "Fuentedejoyas",
        "Escudodorado",  
        "Hojametal",  
        "Riscoplata",  
        "Cavernaclaridad",  
        "Orígenpiedra",  
        "Gotaesmeralda",
        
        "Lingotazo",
        "Luzdeambar",   
        "Luzambar",   

        "Oronevado",  
        
        "Reflejometálico",
        
        "Sueñodeoro",  
        "Sueñoaureo",
        
        "Torredelmina",   
        "Torrealmina",   
        "Torremina",   
        "Torrejoya",  
        "Torreaurea",  
        ""]
    if Type == "Dwarf": 
        Names = Dwarves
        Surnames = DwarvenSurnames

        if Dice(10)<5:
            on_name = ['Gio','Lo',"Gi", "Lu", "Mar", "An", "Fe", "Cal", "Bi", "Ros", "Ser", "Val", "Al", "Ber", "Fried", "Ger", "Hans", "Karl", "Lud", "Rein", "Wal", "Hel"]
            nu_names = ['van','ren', "a", "e", "i", "o", "u"]
            co_names = ['ni', 'zo', "no", "lo", "ni", "ri", "ti", "si", "na", "ra", "ta", "la", "rich", "helm", "bert", "hard", "mar", "mut", "olf", "wig", "win", "wald"]

            on_sname = ['Roble', 'Oro']
            nu_snames = ['', "a", "e", "i", "o", "u", 'de']
            co_snames = ['']
            Name = SyllabicGenerator(
                onset = on_name,
                nuclei = nu_names,
                codas = co_names,
                count = 1
                )            
            Surname = SyllabicGenerator(
                onset = on_sname,
                nuclei = nu_snames,
                codas = co_snames,
                count = 1
                )

            
        elif Dice(10) < 5:
            Name = SyllabicName(
                syllables = SyllabicExtraction(Names),
                min_syllables=1,
                max_syllables=8)
            Surname = SyllabicName(
                syllables = SyllabicExtraction(Surnames),
                min_syllables=1,
                max_syllables=8)
            
        elif Dice(10)<5: 
            namer = MarkovNameGenerator(Names)
            Name = namer.generate_name()
            surnamer = MarkovNameGenerator(Surnames)
            Surname = surnamer.generate_name()
            
            FullName =  Name +  ' ' + Surname 
            
        else:
            FullName =  random.choice(Names) + ' ' + random.choice(Surnames) 

        return FullName






    Water_Elementals = [
        "Aqualis",
        "Avalon",
        "Aqua",
        "Atlantic",
        "Arctic",
        "Antartic",
        "Argonaut",
        "Amalia",
        "Amaya",

        "Bay",
        "Bahia",

        "Caspian",
        "Cora",

        "India",

        "Kai",

        "Lake",
        "Lago",
        "Laguna",
        
        "Maren",
        "Mar",
        "Marin",
        "Marina",
        "Marino",
        "Maya",
        "Maia",
        "Mira",

        "Nile",
        
        "Oceano",
        
        "Ren",
        "Rene",
        "River",
        
        "Talia",
        "Tallulah",
        
        "Well",
        
        "Suyasha",
        "Severn",
        "Neptaline",
        "Marina",
        "Llyncor",
        "Tiber",
        "Pacific",
        "Tiberius",
        "Indian",
        "Lotus",
        "Kailani",
        "Jennifer",
        "Jen",
        "Neptune",
        "Neptuno",
        "Rain",
        "Wade",
        "Ocen",
        "Oceanus",
        "Beck",
        "Malik",
        "Malek",
        "Irv",
        "Clyde",
        "Indus",
        "Indo",
        "Nimue",
        "Nim",
        "Merlin",
        "Nixie",
        "Doris",
        "Kent",
        "Kendall",
        "Rio",
        "Cove",
        "Bahia",
        "Innes",
        "Moses",
        "Fuji",
        "Anahita",
        "Ginevra",
        "Gin",
        "Ginebra",
        "Jordan",
        "Rayan",
        "Kelvin",
        "Nori",
        "Arno",
        "Saga",
        "Lago",
        "Struan",
        "Stream",
        "Varsha",
        "Shannon",
        "Ondine",
        "Onda",
        "Misty",
        "Monroe",
        "Arnav",
        "Ama",
        "Lynn",
        "Moishe",
        "Yara",
        "Yareli",
        "Oceane",
        "Thalassa",
        "Bay",
        "Bey",
        "Neptune",
        "Neptuna",
        "Sea",
        "Kairi",
        "Ria",
        "Indra",
        "Kano",
        "Aarna",
        "Niara",
        "Niagara",
        "Nebula",
        "Delta", "Aalto",
        "Po", "Araluen", "Jora",
        "Naim", "Narelle",
        "Nahla", "Nerida",
        "Nereida", "Neri",
        "Cherith",
        "Adair",
        "Lir",
        "Reva",
        "Sereia",
        "Aqua", "Eyre",
        "Mar", "Moana",
        "Triton", "Euna",
        "Undine", "Nebula",
        "Meara", "Loch",
        "Naida", "Oceana",
        "Gali", "Tal",
        "Loire",
        "Rilla",
        "Varuna",
        "Maayan",
        "Oceanus",
        "Kalani",
        "Aquarius",
        "Acuario",
        "Danu",
        "Danubio",
        "Tarka",
        "Nen",
        "Gal",
        "Rivo",
        "Duna",
        "Zarya",
        "Laguna",
        "Seine",
        "Sena",
        "Alun", "Kallan",
        "Cascada", "Danube",
        "Onda", "Wave",
        "Baia", "Nile",
        "Nilo", "Maree",
        "Marea",
        "Adria",
        "Adriana",
        "Alda",
        "Alma",
        "Amaya",
        "Anahita",
        "Asita",
        "Cherith",
        "Darya",
        "Dayla",
        "Hali",
        "Kendra",
        "Loire",
        "Marella",
        "Michal", "Mira",
        "Nahla", "Namra", "Reva",
        "Ria", "Salila",
        "Sarita", "Talia",
        "Zarna",
        "Zarya",
        "Adair",
        "Afron",
        "Alon",
        "Andreus",
        "Arnon",
        "Bahari",
        "Gafar",
        "Haf",
        "Jafar",
        "Kallan",
        "Kaveri",
        "Malik",
        "Ninad",
        "Odine",
        "Pavati",
        "Pulin",
        "Sagara",
        "Siva",
        "Wade",
        "Adva",
        "Ara",
        "Arna",
        "Baia",
        "Bay",
        "Cascade",
        "Cascada",
        "Coral",
        "Eira",
        "Euri",
        "Isa",
        "Ice",
        "Snow",
        "Isla",
        "Jamaica",
        "Jordan",
        "Jubal",
        "Kai",
        "Kenga",
        "Kline",
        "Lago",
        "Laguna",
        "Laco",
        "Lake",
        "Laik",
        "Maris", "Morgan",
        "Morgana", "Nira",
        "Rayan", "Shandy",
        "Shannon", "Shore",
        "Adair", "Amaya",
        "Cary", "Kisima",
        "Laguna",
        "Narelle",
        "Nile",
        "Nilo",
        "Nimue",
        "Serena",
        "Sereno",
        "Yara",
        "Alon",
        "Kano",
        "Wade",
        "Naia",
        "Tide",
        "Adriatic",
        "Ariel",
        "Athena",
        "Atena",
        "Azena",
        "Eldoris",
        "Marin",
        "Kona",
        "Argo",
        "Arcadia",
        "Blue",
        "Lima",
        "Andaya",
        "Niar",
        "Mora",
        "Amal",
        "Kaya",
        "Dorian",
        "Vatnavi",
        ]
    
    Fire_Elementals = [
        "Neron",
        "Nero",
        "Pyraan",
        "Agnivir",
        "Tulikor",
        "Igniferro",
        "Lavasol",
        "Fuocco",
        "Phoenix",
        "Ember",
        "Cyrus",
        "Rhys",
        "Apollo",
        "Kenna",
        "Blaze",
        "Flame",
        "Arsenic",
        "Kenna",
        "Ravi",
        "Aster",
        "Ignatius",
        "Ignacio",
        "Ignatio",
        "Hera",
        "Uri",
        "Edris",
        "Satish",
        "Calcifer",
        "Sol",
        "Solina",
        "Solin",
        "Salamander",
        "Ardea",
        "Ravee",
        "Vulcan",
        "Eldir",
        "Hito",
        "Agni",
        "Waru",
        "Alev",
        "Haco",
        "Adar",
        "Agni",
        "Aiden",
        "Adish",
        "Afi",
        "Ardere",
        "Ash",
        "Ashbel",
        "Atesh",
        "Blaze",
        "Bodaway",
        "Brand",
        "Brando",
        "Branton",
        "Brent",
        "Conleth",
        "Cimbeline",
        "Cyrus",
        "Cirio",
        "Egan",
        "Finlo",
        "Fintan",
        "Flint",
        "Haco",
        "Hagan",
        "Hakan",
        "Helios",
        "Elio",
        "Inigo",
        "Iñigo",
        "Ishaan",
        "Keahi",
        "Keegan",
        "Kenneth",
        "Kiran",
        "Maccoy", "Nuri",
        "Prometheus",
        "Prometeo",
        "Promezeus",
        "Prometeus",
        "Ra",
        "Rhys",
        "Tyson",
        "Uri",
        "Vulcan",
        "Aalish",
        "Aidan",
        "Adar",
        "Aithne",
        "Aizne",
        "Alinta",
        "Anala",
        "Azar",
        "Barbara",
        "Calida",
        "Candace",
        "Cinder",
        "Ceniza",
        "Cenicienta",
        "Cinderella",
        "Cinderel",
        "Edan",
        "Ember",
        "Ambar",
        "Amber",
        "Ena",
        "Enya",
        "Anya",
        "Fiamma",
        "Flama",
        "Idris",
        "Kalama",
        "Kenna",
        "Pele",
        "Fenix",
        "Shula",
        "Souzan",
        "Tana",
        "Burn",
        "Abenanka",
        "Aguya",
        "Aithne",
        "Alinta",
        "Bedelia",
        "Brid",
        "Calida",
        "Calina",
        "Enya",
        "Eña",
        "Enia",
        "Ember",
        "Fiamma",
        "Nina",
        "Shula",
        "Tana",
        "Tanwen",
        "Admani",
        "Agni",
        "Aiden",
        "Anala",
        "Aodh",
        "Brandr",
        "Branton",
        "Blaze",
        "Brand",
        "Cinaed",
        "Conleth",
        "Conlez",
        "Egan",
        "Edan",
        "Edana",
        "Flint",
        "Fintan",
        "Hagan",
        "Haco",
        "Vela",
        "Ignacio",
        "Inigo",
        "Iñigo",
        "Ignatius",
        "Kenez",
        "McCoy",
        "Mishal",
        "Mogotsi",
        "Nuri",
        "Nuria",
        "Plamen",
        "Pirro",
        "Pyrrhus",
        "Pirrus",
        "Tanguy",
        "Tito",
        "Titus",
        "Uri",
        "Vatroslav",
        "Azar",
        "Hayden",
        "Keahi",
        "Liekki",
        "Fenix",
        "Rhys",
        "Igno",
        "Kenez",
        "Blaise",
        "Blaze",
        "Aalish",
        "Aatish",
        "Aatix",
        "Atix",
        "Aarush",
        "Aarux",
        "Arux",
        "Abenanka",
        "Adara",
        "Adeen",
        "Adish",
        "Admani",
        "Amani",
        "Adurnarseh",
        "Aed",
        "Afi",
        "Agneya",
        "Agnes",
        "Agni",
        "Agnimitra",
        "Agnivo",
        "Aguya",
        "Ahdan",
        "Aidan",
        "Aiden",
        "Aine",
        "Aithne",
        "Aizne",
        "Akiho",
        "Aldebrand",
        "Alev",
        "Alinta",
        "Amarkeeri",
        "Anala", "Angarika",
        "Apoy", "Ardere",
        "Arder", "Ardor",
        "Atsila", "Azar",
        "Azula", "Azarnoosh",
        "Basia", "Bedelia",
        "Brantley", "Brigid",
        "Brit", "Cemre",
        "Chantico", "Conlez",
        "Conleth", "Conley",
        "Fajra", "Faira",
        "Fiamma", "Flama",
        "Fiama", "Felio",
        "Felia", "Felios",
        "Hurik",
        "Idris", "Ignacia",
        "Ishat", "Kamar",
        "Kazuya", "Keahi",
        "Keegan", "Kenna",
        "Kindle",
        "Kai", "Lieki",
        "Mahuika", "Mashal",
        "Torch", "Antorcha",
        "Torcha", "Mogotsi",
        "Nina",
        "Nootau",
        "Nutau",
        "Oya", "Plamen",
        "Pyro", "Piro", "Piros",
        "Pirus", "Ris", "Piris",
        "Shohreh", "Sore",
        "Shula", "Souzan",
        "Tanguy",
        "Ugne",
        "Igne", "Ignea", "Azar",
        "Calida", "Calido", "Fuji", "Neri",
        "Aiden", "Adal", "Cora", "Areli", "Brina",
        "Arian", "Igna",
        "Kalal", "Pikah",
        "Alen", "Brind", "Cosha", "Ari", "Keri",
        "Cider", "Cavo", "Fenix", "Adarin",
        "Bris", "Azam", "Calan", "Arur",
        ]

    Earth_Elementals = [
        "Terraque",
        "Muldor", "Rocalia",
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
        "Andesite", "Alkali",
        "Basalt", "Basanite",
        "Magnesium", "Lava",
        "Volcan", "Potassium",
        "Silica", "Rock",
        "Carbon", "Carbonite",
        "Ender", "Dacite",
        "Dolerite", "Corsite",
        "Dunite", "Olivine",
        "Essexite",
        "Granite",
        "Grane",
        "Dune",
        "Duna",
        "Pluton",
        "Kimberlite",
        "Diamond",
        "Latite",
        "Obsidian",
        "Pumice",
        "Scoria",
        "Sovite",
        "Dolomite",
        "Chalk",
        "Coal",
        "Quartz",
        "Cuarzo",
        "Salt",
        "Marble",
        "Granite",
        "Lapislazuli",
        "Lapis",
        "Lazuli",
        "Adamite",
        "Adelite",
        "Arenite",
        "Almandite",
        "Alumn",
        "Alunite",
        "Amarantite",
        "Anandite",
        "Antimony",
        "Azurite",
        "Adamantine",
        "Agate",
        "Alabaster",
        "Bismite",
        "Bismut",
        "Bronce",
        "Cadmium",
        "Cerite",
        "Carvonite",
        "Crystal",
        "Copper",
        "Cobre",
        "Cementite",
        "Emerald",
        "Diamond",
        "Mine",
        "Fluorite",
        "Garnet",
        "Gold",
        "Hematite",
        "Magnetite",
        "Manganite",
        "Mesolite",
        "Mimetite",
        "Mica",
        "Magnesia",
        "Neptinite",
        "Pyrite",
        "Pirite",
        "Quartz",
        "Ruby",
        "Titanite",
        "Turquesa",
        "Turkis",
        "Turquoise",
        "Tremor",
        "Uralite",
        "Zeolite",
        "Zinc",
        "Zircon",
        "Lithium",
        "Sodium",
        "Potassium",
        "Rubidium",
        "Cesium",
        "Francium",
        "Berillium",
        "Magnesium",
        "Calcium",
        "Strontium",
        "Barium",
        "Radium",
        "Aluminium",
        "Gallium",
        "Indium",
        "Tin",
        "Thallium",
        "Lead",
        "Bismuto",
        "Titanium",
        "Vanadium",
        "Chromium",
        "Manganese",
        "Iron",
        "Cobalt",
        "Nickel",
        "Copper",
        "Zinc",
        "Zirconium",
        "Rodium",
        "Palladium",
        "Silver",
        "Cadmium",
        "Tunsten",
        "Osmium",
        "Platinum",
        "Gold",
        "Mercury",
        "Plata",
        "Oro",
        "Copernicium",
        "Uranium",
        "Plutonium",
        "Curium",
        "Californium",
        "Einstenium",
        "Fermium",
        "Nobelium",
        "Lithium",
        "Berilium",
        "Sodium",
        "Magnesium",
        "Potasium",
        "Calcium",
        "Titanium",
        "Vanadium",
        "Chrome",
        "Chromium",
        "Manganese",
        "Iron",
        "Cobalt",
        "Nickel",
        "Copper",
        "Zinc",
        "Gallium", "Rubidium",
        "Strontium", "Zirconium", "Niobium",
        "Rodium", "Silver", "Cadmium", "Indium",
        "Tin", "Cesium", "Cerium",
        "Promethium", "Iridium",
        "Platinum", "Mercury", "Mercurium",
        "Lead", "Bismutium",
        "Polonium", "Uranium",
        "Alabaster",
        "Argento", "Berilio",
        "Clay", "Coal",
        "Cobalt",
        "Dustin", "Elessar",
        "Emerald",
        "Ferro", "Granite",
        "Mercury", "Mica",
        "Oriol", "Oro",
        "Peter", "Pedro",
        "Saphir", "Silver",
        "Steel",
        "Stone", "Zircon",
        "Bronze",
        "Iron", "Ferro",
        "Electrum",
        "Sterling",
        "Argentium",
        "Titanium",
        "Cole",
        "Arena",
        "Arenita",
        "Flint",
        "Duna",
        "Amatist",
        "Gravel",
        "Gaia",
        "Boulder",
        "Bould",
        "Atlas",
        "Avalanche",
        "Midas",
        "Flint",
        "Basalt",
        "Jade",
        "Mita",
        "Coba",
        ]
    
    Air_Elementals = [
        "Aerlyn",
        "Vaataan",
        "Tuulikas",
        "Ilmara", "Caelistis",
        "Aero", "Aelio",
        "Aeolian", "Gale", "Zefir",
        "Zefyr", "Zephyr", "Zefirus",
        "Wuzer", "Wuther",
        "Haboob", "Abroholos",
        "Auster", "Austru", "Barat",
        "Berber",
        "Bayamo", "Bora",
        "Borasco", "Boreas", "Boreal",
        "Aurora", "Brisa", "Briza",
        "Brisot", "Brubu", "Cave",
        "Kaver", "Chubasco",
        "Cierzo", "Contrastes",
        "Cordonazo",
        "Cyclone", "Etesian",
        "Euros", "Hurricane",
        "Huracan", "Wind",
        "Viento", "Leste",
        "Levanter", "Levante",
        "Levantera", "Levanto",
        "Leveche", "Mistral",
        "Norte", "Noreaster",
        "Norestero", "Norwester",
        "Noroestero",
        "Nortero", "Ostria",
        "Pali", "Santana",
        "Shamal", "Sharki",
        "Siroco", "Sumatra", "Tramontana",
        "Tifon", "Zefiros", "Zefiro", "Zefir",
        "Bora", "Etesian", "Levant", "Levante",
        "Leveche", "Harmatan", "Karaburan",
        "Buran", "Orosi", "Sarma",
        "Shamal", "Alisio", "Alize",
        "Bayamo", "Brisote",
        "Caju", "Nordeste", "Minuano",
        "Zonda", "Pampero", "Sudestada",
        "Cordonazo",
        "Coromuel", "Norte", "Autan",
        "Bise", "Brise", "Brisa", "Burle",
        "Cers",
        "Cierzo", "Etesian", "Euroclydon",
        "Fohn", "Gregale", "Helm", "Leveche",
        "Lodos", "Maestro", "Marin",
        "Mistral", "Nordes", "Ostro",
        "Poliente",
        "Solano", "Tramontane", "Vendavel",
        "Kona", "Abel", "Aeolus",
        "Akash",
        "Amun",
        "Anan", "Cloud", "Anil", "Nube",
        "Anore", "Arkansas",
        "Avel", "Barak",
        "Baran", "Brontes", "Caelus", "Corentin",
        "EnlilErjon", "Esen", "Guntur",
        "Keanu", "Matuu", "Mellan", "Moe", "Myrsky",
        "Naseem", "Neifion", "Neil",
        "Neve", "Nigel", "Notus",
        "Payne", "Perun",
        "Firun", "Samir", "Sepher",
        "Shu", "Sky", "Stromur",
        "Sturm", "Thor",
        "Thunder", "Storm", "Torm", "Tufani",
        "Van", "Zenith", "Zephyr",
        "Zeus", "Aella",
        "Aethra", "Ahana", "Alize", "Amihan",
        "Anemos", "Anila", "Araceli", "Audra",
        "Aura", "Auretta", "Awen", "Azure", "Bonaria",
        "Ciela", "Cielo", "Dangira", "Dima",
        "Ekaitza", "Era", "Glaw", "Haizea", "Haneul",
        "Inanna", "Iris", "Kafeira", "Cafeira",
        "Minnesota", "Misty", "Mist",
        "Nephele", "Ninlil", "Nuit", "Pilvi",
        "Puleng", "Rain", "Rakia", "Samira", "Sema",
        "Skye", "Stormy", "Tempest", "Tondra",
        "Varsha", "Vetra", "Zerua", "Zilan", "Mistral",
        "Gibli", "Zonda", "Etesian", "Shamal",
        "Aither", "Akash", "Alizeh",
        "Amphorn", "Amun", "Anan",
        "AnilAnore", "Anvindr",
        "Ayaz", "Bayu",
        "Boreas", "Caelus",
        "Corentin",
        "Enlil", "Erjon",
        "Ermir", "Esen",
        "Eyvinder", "FujinGokcan",
        "Govad", "Guzrie",
        "Hayate", "Ilmari",
        "Keyne",
        "Naseem", "Neven",
        "Notus", "Ouranos", "Payne",
        "Rabi", "Samir", "Sepher", "Soma", "Sota",
        "Tifon", "Vayu", "Zeferino", "Zenit", "Zefir",
        "Zeru", "Zeus", "Aella", "Aethra", "Ahana",
        "Alizee",
        "Alizeh",
        "Alya",
        "Amaterasu",
        "Amihan",
        "Anila",
        "Aria",
        "Aureole",
        "Auretta",
        "Azure",
        "Bonaria",
        "Breeze",
        "Brisa",
        "Ciela",
        "CoroEra",
        "Esen",
        "Eteri",
        "Haizea",
        "Haneul",
        "Ilma",
        "Kailani",
        "Kalani",
        "Lulani",
        "Makani",
        "Meltem",
        "Miku",
        "Mystral",
        "Nasima",
        "Ninlil",
        "Nuit",
        "Rakia",
        "Samira",
        "Sciron",
        "Scirocco",
        "Sefarina",
        "Sema",
        "Skye",
        "Tadita",
        "Wind",
        "Zephyrine",
        "Zerua",
        "Damini",
        "Oya",
        "Nebula",
        "Misty",
        "Mist",
        "Wind",
        "Brenna",
        "Sail",
        "Vela",
        "Katrina",
        "Amakir",
        "Abub",
        "Zeam",
        "Vesha",
        "Nura",
        "Wura",
        "Enarise",
        "Amana",
        "Aeana",
        "Akades",
        "Miste",
        "Zecori",
        "Sirocco",
        "Siroco",
        "Aura",
        "Zepherien",
        "Sior",
        "Annora",
        "Ael",
        ]

    Elementals = [
        "Lignan",
        "Metallor",
        "Astrelitz",
        "Fulgarnis",
        "Glacialyne", 
        "Rayostrike",
        "Jääspirit",
        "Ombrosyl",
        "Element"
    ]
    
    if Type == "Elemental": 
        Names = Elementals + Water_Elementals + Air_Elementals + Fire_Elementals + Earth_Elementals
        Surnames = Names
        
        if True:
            # Onset Syllables
            on_name = ["Pyro", "Aqua", "Aero", "Geo", "Ferro", "Ether", "Elem"]
            on_sname = ["Flam", "Hydro", "Zeph", "Terr", "Metal", "Spir"]

            # Nuclei Syllables
            nu_names = ["i", "a", "o", "e", "u"]
            nu_snames = ["ar", "el", "in", "on", "um"]

            # Codas Syllables
            co_names = ["us", "ix", "or", "an", "el", "ent"]
            co_snames = ["ius", "ax", "or", "an", "el"]

            subrace_syllables = {
                "Atlantian": {
                    "onset": ["Aqua", "Mar", "Ocea", "Thal"],
                    "nuclei": ["a", "e", "i", "o", "u"],
                    "codas": ["nix", "rus", "tus", "lan", "sea"],
                },
                "Cronusian": {
                    "onset": ["Chron", "Temp", "Aev"],
                    "nuclei": ["o", "u", "e"],
                    "codas": ["os", "um", "or"],
                },
                "Eosian": {
                    "onset": ["Sol", "Dawn", "Lum"],
                    "nuclei": ["e", "a", "i"],
                    "codas": ["ra", "os", "en"],
                },
                "Genasi": {
                    "onset": ["Elem", "Natur", "Vita"],
                    "nuclei": ["a", "e", "i", "o"],
                    "codas": ["ra", "an", "el", "us"],
                },
                "Genie": {
                    "onset": ["Myst", "Magi", "Spir"],
                    "nuclei": ["i", "o", "a"],
                    "codas": ["que", "rix", "an"],
                },
                "Gaians": {
                    "onset": ["Terr", "Geo", "Arbor"],
                    "nuclei": ["a", "e", "i"],
                    "codas": ["an", "us", "ra"],
                },
                "Hyperian": {
                    "onset": ["Sol", "Radi", "Lum"],
                    "nuclei": ["a", "o", "u"],
                    "codas": ["us", "ar", "en"],
                },
                "Oceanians": {
                    "onset": ["Mare", "Tide", "Wave"],
                    "nuclei": ["a", "o", "e"],
                    "codas": ["an", "or", "ium"],
                },
                "Primordial": {
                    "onset": ["Prim", "Origi", "Elem"],
                    "nuclei": ["a", "e", "i"],
                    "codas": ["us", "on", "ar"],
                },
                "Promethean": {
                    "onset": ["Flam", "Igni", "Volt"],
                    "nuclei": ["e", "a", "o"],
                    "codas": ["ex", "us", "ar"],
                },
                "Salamandrian": {
                    "onset": ["Blaze", "Inferno", "Flare"],
                    "nuclei": ["i", "o", "u"],
                    "codas": ["us", "an", "el"],
                },
                "Titan": {
                    "onset": ["Gigant", "Might", "Colos"],
                    "nuclei": ["a", "e", "o"],
                    "codas": ["us", "an", "or"],
                },
                "Uranians": {
                    "onset": ["Celest", "Astra", "Sky"],
                    "nuclei": ["i", "u", "o"],
                    "codas": ["al", "um", "ion"],
                },
                "Magmaforged": {
                    "onset": ["Lava", "Magma", "Pyro"],
                    "nuclei": ["a", "e", "i"],
                    "codas": ["us", "an", "on"],
                },
                "Zephyrian": {
                    "onset": ["Breez", "Gale", "Wind"],
                    "nuclei": ["e", "a", "o"],
                    "codas": ["or", "us", "an"],
                },
                "Tartarian": {
                    "onset": ["Abyss", "Deep", "Naut"],
                    "nuclei": ["i", "o", "u"],
                    "codas": ["us", "an", "ic"],
                },
                "Etherian": {
                    "onset": ["Ether", "Spir", "Astral"],
                    "nuclei": ["a", "e", "i"],
                    "codas": ["us", "el", "an"],
                },
                "Galaxian": {
                    "onset": ["Star", "Cosm", "Galax"],
                    "nuclei": ["i", "o", "a"],
                    "codas": ["us", "an", "or"],
                },
                "Chronian": {
                    "onset": ["Etern", "Aeon", "Temp"],
                    "nuclei": ["a", "o", "e"],
                    "codas": ["us", "or", "um"],
                },
                "Tundran": {
                    "onset": ["Frost", "Glac", "Snow"],
                    "nuclei": ["i", "o", "u"],
                    "codas": ["ar", "us", "en"],
                },
            }


            
            # Extend base lists with subrace-specific syllables
            if npc.subrace in subrace_syllables:
                sr_syllables = subrace_syllables[subrace]
                on_name.extend(sr_syllables["onset"])
                nu_names.extend(sr_syllables["nuclei"])
                co_names.extend(sr_syllables["codas"])
                on_sname.extend(sr_syllables["onset"])
                nu_snames.extend(sr_syllables["nuclei"])
                co_snames.extend(sr_syllables["codas"])

        Name = NewName(Names,nu_names,co_names) 
        Surname = NewName(Names,on_sname,nu_snames,co_snames)      
                
        FullName =  Name +  ' ' + Surname 

        return FullName



























    
    Avens = [
        "Murder",
        "Corvid",
        "Corvus",
        "Cuervo",
        "Raven",
        "Murderfoe",
        "Corvo",
        "Crow",
        "Kraai",
        "Taruja",
        "Sorre",
        "Krahe",
        "Alghurab",
        "Agrrav",
        "Qarga",
        "KaKasi",
        "Kaka",
        "Varona",
        "Kyaeekaann",
        "Vrana",
        "Kaek",
        "Kage",
        "Corb",
        "Uwak",
        "Khwangwala",
        "Wuya",
        "Kaputa",
        "Kamagwi",
        "Corbu",
        "Kok",
        "Krage",
        "Kaalhu",
        "Cuervo",
        "Korbo",
        "Vares",
        "Belea",
        "Akpavia",
        "Varis",
        "Corbeau",
        "Feannag",
        "Fran",
        "Flit",
        "Glide",
        "Mimic", "Echo",
        "Shimmer", "Talon", "Plume", 
        "Soar", "Shade",
        "Dusk", "Dawn",
        "Twilight",
        "Nightcall",
        "Wingbeat", 
        "Rustle",
        "Murmur", "Feather",
        "Perch",
        "Roost", "Glitter", "Beaksharp", 
        "Swoop", "Windrider",
        "Cloudwing", "Skydance",
        "Mooncaw",
        "Sunfeather", 
        "Starshine", "Hoopoe",
        "Chatter", "Squawk",
        "Preen", "Beacon", "Ruffle", 
        "Silhouette",
        "Frostwing",
        "Skyshriek",
        "Windwhisper",
        "Nighthawk", "Skygleam", 
        "Stormwatch",
        "Raincry", "Snowplume",
        "Thundercaw", "Windfeather", "Songthief", 
        "Eclipsing", "Shadowplay", "Sunshadow",
        "Pinnacle", "Crest",
        "Echoflap", 
        "Nestling", "Skyward", "Sable", "Flock",
        "Whistle",
        "Hush",
        "Lustrous", 
        "Mottle",
        "Pepper",
        "Tint",
        "Hue",
        "Canvas",
        "Sketch",
        "Inkfeather", 
        "Jewel", "Gemwing",
        "Prism", "Spectra",
        "Ripple", "Glisten",
        "Gleam", 
        "Harmony", "Rhythm",
        "Melody", "Crescendo",
        "Lilt", "Aria",
        "Sonnet", 
        "Verse", "Chorus",
        "Note", "Chime", "Bell",
        "Tune", "Clef",
        "Lyric", 
        "Resonate", "Hum",
        "Whirl", "Echoing",
        "Tempest", "Zephyr",
        "Soarer", "Glider",
        "Diver", "Migrant",
        "Nester", "Chirper",
        "Hover", "Plumage",
        "Beak", "Wing",
        "Feather",
        "Claw",
        "Talon", "Beacon",
        "Singer", "Caller",
        "Flight", "Skyward",
        "Preen",
        "Bill",
        # Raptor-inspired:
        "Falcara", "Hawkwind", "Aquila",
        "Kestralis", "Ospryion",
        "Harrix", "Buzzaros",
        "Vultar", "Condrex", "Merlynx",

        # Songbirds-inspired:
        "Finchwind", "Larkspire", "Warblyn",
        "Thrushtar", "Sparrox", "Oriox", "Tanagral",
        "Chickador", "Wrenshade", "Nightinglare",

        # Waterfowl-inspired:
        "Duckshade", "Gooslyn",
        "Swanpeak",
        "Pintar", "Mallarion",
        "Tealis", "Pelicarn",
        "Heronshade", "Egryx",
        "Loonspire",

        # Ocean Birds-inspired:
        "Gullwind",
        "Terrix",
        "Albatrosar",
        "Puffinox",
        "Cormorantyx",
        "Petralis",
        "Skuarion",
        "Shearshade",

        # Tropical Birds-inspired:
        "Parroshade",
        "Macawind",
        "Toucanar",
        "Hoopion",
        "Sunbyrd",
        "Hornbillar",
        "Quetzyx",
        "Cotingar",

        # Game Birds-inspired:
        "Quailfire",
        "Pheasanar",
        "Grousewind",
        "Turkshade",
        "Guineaflare",
        "Peacox",
        "Ptarmyx",

        # Miscellaneous-inspired:
        "Owlspire",
        "Dovewind",
        "Pigeonyx",
        "Magpyre",
        "Jayshade",
        "Lyrebyrd",
        "Kiwix",
        "Pengshade",
        "Emurion",
        "Ostrix",
        "Cassowar",
        "Flamyn",
        "Cranar",
        "Storkwind",
        "Kingfisar",
        "Hummshade",
        "Woodpyre",
        "Ibix",
        "Tropicar"
        ]

    if "Kenku" in creature_type:
        Kenku = [
        "Corvo",
        "Kheree", "Choak",
        "Kavala",
        "Kaokao", "Cawla",
        "Caw", "Goaika",
        "Gagak",
        "Kakka",
        "Vrana", "Kraischen",
        "Nnamungoona", "Libata",
        "Varna", "Fung",
        "Zax", "Blak", "Bod",
        "Black", "Karga",
        "Igikona",
        "Qarga", "Manuk",
        "Gagak",
        "Karasu", "Corvo",
        "Kraka", "Preachan",
        "Crow",
        "Raven",
        "Rook",
        "Corax", "Burung",
        "Gagak",
        "Uwak", "Uko",
        "Varju",
        "Tsov",
        "Kaua",
        "Koo", "Hankaka",
        "Kagado", "Yryvu",
        "Koraki", "Qvavi",
        "Kaga", "Krake",
        "Qurruu",
        "Kam", "Wrona",
        "Corvo", "Cuervo",
        "Cioara", "Vorona",
        "Matuu", "Legokobu",
        "Vrana",
        "Lekgwaba", "Gunguwo",
        "Tuke",
        "Kunguru", "Gala",
        "Gagak", "Uwak", "Xika",
        "Kakam", "Kapra", "Zoq", "Kaki",
        "Vukuvuku", "Karga",
        "Garga", "Kwaakwaadabi",
        "Vorona", "Qarga", "Conqua",
        "Unomyayi", "Krou",
        "Kuroo", "Igwababa", "Kror",
        "Kak", "Kakab",
        "Kargw", "Kri",
        "Karok", "Corak",
        "Kavue", "Kakur",
        "Karaga",
        "Kakor", "Kaerv",
        "Kagaka",
        "Comunko",
        "Corv", "Krueng",
        "Karak",
        "Kalaa",
        "Cabur",
        "Kara", "Kak",
        "Karvis", "Korvun",
        "Corvi", "Kukurv",
        "Haden", "Kanak", "Lera",
        "Krai", "Kabak",
        "Unkur", "Kagan",
        "Kakur", "Krara",
        "Koror", "Kakara",
        "Kar",
        "Kaa", "Corr",
        "Kavon", "Kanaka",
        "Kakut", "Kakak",
        "Kax",
        "Koke",
        "Kaeru",
        "Karva",
        "Covar",
        "Karu",
        "Kakar",
        "Kana",
        "Kav",
        "Draven",
        "Kenku",
        "Chirrik", ]
        Names += Kenku
        
    if "Aven" in creature_type: 
        Names += Avens
        Name = NewName(Names)
        FullName =  Name
        return FullName

    Halflings = [
        "Grinhand",
        "Adaldrida",
        "Lifwalker",
        "Regina",
        "Jasmine",
        "Sam",
        "Pipim",
        "Crim",
        "Pint",
        "Chocolaty",
        "Love", "Afiry", "Cuki",
        "Chunk", "Dairy",
        "Peanut", "Buter",
        "Cake", "Milk",
        "Cone", "Canoli",
        "Caramel", "Canela",
        "Chis", "Chery", "Chip",
        "Browny", "Chuby",
        "Tofy", "Cofy",
        "Dublin", "Bake",
        "Joint", "Widy", "Milky",
        "Minty", "Cuky",
        "Pistacho", "Pumpin",
        "Almond", "Fresy", "Berry", "Cake", "Vanilla",
        "Sutra", "Tiramisu", "Whisky", "Bacon",
        "Banana", "Beer",
        "Bluemoon", "Bubble", "Gum",
        "Coffee", "Apple", "Cream",
        "Candy", "Cotton",
        "Dulce", "Garlic", "Grape", "Punch",
        "Ponche", "Uva", "Grape", "Tea",
        "Lucuma", "Mango", "Maple",
        "Chip", "Napolito",
        "Napolita", "Pistacho",
        "Mora", "Rum", "Ron", "Ginebra",
        "Gin", "Martin", "Martini",
        "Martina", "Licor", "Melon",
        "Almond", "Almendra", "Manela",
        "Manzana", "Apple",
        "Apricot", "Balsamic", "Basil",
        "Berry", "Pepper", "Bourbon",
        "Bread", "Sugar",
        "Palomita", "Palomito", "Cacao",
        "Corn", "Caramel", "Carrot",
        "Cardamom", "Cheddar",
        "Chili", "Chocolate", "Canela",
        "Cinnamon", "Coconut", "Nut",
        "Coffee", "Cranberry",
        "Apricot", "Durian", "Espresso",
        "Ferrero", "Fig", "Garlic",
        "Ginger", "Guinness",
        "Hazelnut", "Honey", "Jam", "Bean",
        "Jelly", "Kaffir",
        "Lime", "Kiwi", "Fruit",
        "Lemon", "Macadamia", "Mango", "Maple",
        "Mocha", "Nutella", "Nocciola", "Nuts",
        "Olive", "Pear", "Peppermint",
        "Pickle", "Pineaple", "Pistachio",
        "Plum", "Praline",
        "Vino", "Pumpkin",
        "Raisin", "Rose",
        "Rum",
        "Tangerine",
        "Violet",
        "Walnut",
        "Oreo",
        "Avocado",
        "Amaretto",
        "Almendra",
        "Aguacate",
        "Amarula",
        "Aqua",
        "Burbon",
        "Cognac",
        "Chai",
        "Creme",
        "Coconut",
        "Pie",
        "Tarta",
        "Choc",
        "Custard",
        "Dorian",
        "Elderflower",
        "Evermint",
        "Fresa",
        "Fraise",
        "Fejoa",
        "Fragola",
        "Fruitella",
        "Granada",
        "Granadilla",
        "Macedonia",
        "Grosella",
        "Guava",
        "Hazelnut",
        "Honeycomb",
        "Habanero",
        "Puro",
        "Cigarro",
        "Hunny",
        "Honey",
        "Miel",
        "Crema",
        "Limon",
        "Cafe",
        "Kinder",
        "Kitkat",
        "Leche",
        "Piruleta",
        "Nougat",
        "Neapolitana",
        "Neopolitan",
        "Nectarina",
        "Nuggets",
        "Orange",
        "Naranja",
        "Onion",
        "Cebolla",
        "Oresos",
        "Orchid",
        "Orangina",
        "Cacahuete",
        "Mani",
        "Peach",
        "Pomme",
        "Pera",
        "Rubarb",
        "Raisin",
        "Toblerone",
        "Truffle",
        "Walnuss",
        "Waffle",
        "Yogurt",
        "Yema",
        "Yuzu",
        "Carlota",
        "Carrot",
        "Zanahoria",
        "Zitron",
        "Picho",
        "Beler",
        "Sune",
        "Numea",
        "Orelle",
        "Trafa",
        "Marb",
        "Sanue",
        "Nenara",
        "Nanut",
        "Egumugoni",
        "Maximus",
        "Maximo",
        "Meridio",
        "Bilbo",
        "Samwise",
        "Trim",
        "Milo",
        "Perry",
        "Pipin",
        "Caramel",
        "Gamwick",
        "Mint",
        "Herleva",
        "Fairfut",
        "Berta",
        "Underfut",
        "Pamfila",
        "Punkin",
        "Bramblefoot",
        "Tansy",
        "Loras",
        "Faela",
        "Primrose", 
        "Celandine",
        "Bramber", "Eldo",
        "Lalia", "Thistle", 
        "Honeybun",
        "Ciderpress",
        "Butterscotch",
        "Tiramis",
        "Muffinette", 
        "Truffelino",
        "Raisinet",
        "Orangetwist",
        "Gelatino",
        "Sorbetta", 
        "Pesto",
        "Cinnamelle",
        "Pistachio",
        "Creampuff",
        "Nutmeggy", 
        "Frappucin",
        "Caramelita",
        "Marshmellowy",
        "Puddington",
        "Lemonella", 
        "Gingerspice",
        "Briochee",
        "Cappuccina",
        "Cherrybelle",
        "Brownieboots", 
        "Jollybean",
        "Gigglepot",
        "Merrychuckle",
        "Twinkletoes",
        "Gleeheart", 
        "Sunshine",
        "Chuckleberry",
        "Lightheart",
        "Giddyup",
        "Delighta", 
        "Gingersnap",
        "Berry",
        "Mocha",
        "Taffy",
        "Nectarina", 
        "Hopskip",
        "Crumblecake",
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
        if Dice(10)<10: 
            namer = MarkovNameGenerator(Names)
            Name = namer.generate_name()
            Name2 = namer.generate_name()
            surnamer = MarkovNameGenerator(Surnames)
            Surname = surnamer.generate_name()
            #Surname2 = surnamer.generate_name()

            
            FullName =  Name + ' ' +  Name2 + ' ' + Surname #+ ' ' + Surname2 
            #FullNames =  random.choice(Names) + ' ' + random.choice(Surnames) 
            
        else:
            FullName =  random.choice(Names) + ' ' + random.choice(Names) + ' ' + random.choice(Surnames) #+ ' ' + random.choice(Surnames)

        return FullName
    
    Gnomes = [
        "Acerbi",
        "Amadea",
        "Amadeo",
        "Amidea",
        "Amideo",
        "Antonia",
        "Antonio",
        "Anzola",
        "Anzolo",
        "Alberich",
        "Albericha",
        "Albertino",
        "Albertina",
        "Ambrogia",
        "Ambrogio",
        "Amedeo",
        "Amedea",
        "Antonello",
        "Antonella",
        "Babilonia",
        "Babilonio",
        "Baldassare",
        "Barbato",
        "Barbatta",
        "Barbeta",
        "Barbolani",
        "Barbolania",
        "Barbolanio",
        "Bartolini", 
        "Basariona",
        "Bascio",
        "Bassani",
        "Basso",
        "Bellando",
        "Bernardino",
        "Bernardo",
        "Bonzi",
        "Bonzino", 
        "Calabrese",
        "Calandra",
        "Caldarini",
        "Caliara",
        "Calis",
        "Calisto",
        "Calvio",
        "Calvis",
        "Canasi",
        "Candet",
        "Candida",
        "Canelli", 
        "Catalina",
        "Catania",
        "Cecilia",
        "Celestina",
        "Cerzino",
        "Chiaro",
        "Chola",
        "Contarini",
        "Corner",
        "Cortese",
        "Cristiano",
        "Cristofano",
        "Deste",
        "Dellini",
        "Domenica",
        "Domenico",
        "Donatello", 
        "Donella",
        "Engel",
        "Engelo",
        "Engela",
        "Fabbretti",
        "Fabiano",
        "Federica",
        "Federigo",
        "Fideli",
        "Fiesoli",
        "Fiorensi",
        "Fiorenza",
        "Fiorino",
        "Flora",
        "Garzoni",
        "Gerlinde",
        "Gherardini",
        "Giulio",
        "Grana",
        "Granito",
        "Graziano",
        "Guerino",
        "Guerriero",
        "Guido",
        "Hartino", 
        "Hartwig",
        "Hugh",
        "Hugo",
        "Huguette",
        "Humberto",
        "Humberto",
        "Jacopo",
        "Joanna",
        "Jovanni",
        "Lando",
        "Linde",
        "Lindoro",
        "Loredana",
        "Lorenzino",
        "Lorez", 
        "Ludivico",
        "Ludovico",
        "Malatesta",
        "Malipiero",
        "Maneli",
        "Marcato",
        "Markolf",
        "Martelli",
        "Martinella",
        "Marzio",
        "Masetti",
        "Masina",
        "Montefeltro",
        "Mudazo",
        "Murano",
        "Nerezza",
        "Nezetta",
        "Norbert",
        "Norbino", 
        "Novella",
        "Novelli",
        "Orlando",
        "Orsa",
        "Orsini",
        "Ortanio",
        "Rafaelo",
        "Ralf",
        "Reinhold",
        "Rinaldo",
        "Romano",
        "Romuald",
        "Rosso",
        "Ruffino",
        "Serafina",
        "Silvestro"
        "Sunnhild",
        "Ugo",
        "Vasari",
        "Venturi", 
        "Vezzoli", 
        "Vigorito",
        "Vittoria",
        "Waldemar",
        "Waldo",
        "Wedekind",
        "Westaro",
        "Zane",
        "Zanetti",

        ]
    GnomesSurnames = [

        "Artispring",
        "Bacino",
        "Baldovini",
        "Bellamonte",
        "Bellatink",
        "Bergbolt",
        "Bergvene",
        "Bianchetti",
        "Borgo",
        "Bosco",
        "Castello",
        "Clockfixer",
        "Costa",
        "D'Argento",
        "Diamante",
        "Diamantinno",
        "Dorato",
        "Fabbretti",
        "Ferrato",
        "Fiorentini",
        "Fiorentwig",
        "Florenbolt",
        "Folkforge",
        "Fontana",
        "Fontanella",
        "Frutteto",
        "Gadgetgrabber",
        "Gearspinner",
        "Ghirlanda",
        "Giardino",
        "Granatello",
        "Grazzini",
        "Grotta",
        "Holzcraft",
        "Illusionweaver",
        "Lago",
        "Lapidello",
        "Luccinetti",
        "Luminotti",
        "Luminwald",
        "Lunetti",
        "Marmorini",
        "Milanesi",
        "Mindtwister",
        "Molinari",
        "Mondello",
        "Montanari",
        "Montefiore",
        "Morosini",
        "Mura",
        "Misticatto",
        "Napolitano",
        "Olivetti",
        "Orchardino",
        "Orlandini",
        "Palazzo",
        "Palladino",
        "Parco",
        "Peruzzini",
        "Pescatore",
        "Piazza",
        "Piccolino",
        "Pietradura",
        "Pietravalle",
        "Ponte",
        "Riviero",
        "Rocca",
        "Romanelli",
        "Rovellino",
        "Rubinelli",
        "Ruscello"
        "Siciliano",
        "Smeraldini",
        "Solari",
        "Sparkjumper",
        "Starwhisperer",
        "Steinleaf",
        "Stellato",
        "Sussurro",
        "Tinkerfoot",
        "Torresi",
        "Tuscantool",
        "Valentini",
        "Venetgear",
        "Veneziano",
        "Venturino",
        "Verdini",
        "Vespucci",
        "Vigneto",
        "Villa",
        "Waldentinker",
        "Wundergear",
        "Zaffiro",
        ]
    
    if Type == "Gnome": 
        Names = Gnomes
        Surnames = GnomesSurnames

        if Dice(10)<5:
            on_name = ['Gio','Lo',"Gi", "Lu", "Mar", "An", "Fe", "Cal", "Bi", "Ros", "Ser", "Val", "Al", "Ber", "Fried", "Ger", "Hans", "Karl", "Lud", "Rein", "Wal", "Hel"]
            nu_names = ['van','ren', "a", "e", "i", "o", "u"]
            co_names = ['ni', 'zo', "no", "lo", "ni", "ri", "ti", "si", "na", "ra", "ta", "la", "rich", "helm", "bert", "hard", "mar", "mut", "olf", "wig", "win", "wald"]

            on_sname = ['Gio',
                        "Bel", "Fer", "Mar", "Ros", "Cap", "Gal", "Ric", "Cas", "Bor", "Ven",
                        "Schm", "Wein", "Stein", "Baum", "Fisch", "Hoff", "Klein", "Lang", "Schwarz", "Wolff"]
            nu_snames = ['', "a", "e", "i", "o", "u"]
            co_snames = ['',
                         "ini", "elli", "etti", "oni", "aldo", "ato", "azzo", "ucci", "uzzi", "ente",
                         "mann", "berg", "wald", "stein", "hardt", "lein", "bauer", "schmidt", "meier", "brück"]
            Name = SyllabicGenerator(
                onset = on_name,
                nuclei = nu_names,
                codas = co_names,
                count = Dice()-1
                )
            Name2 = SyllabicGenerator(
                onset = on_name,
                nuclei = nu_names,
                codas = co_names,
                count = Dice()-1
                )
            
            Surname = SyllabicGenerator(
                onset = on_sname,
                nuclei = nu_snames,
                codas = co_snames,
                count = Dice()-1
                )
            Surname2 = SyllabicGenerator(
                onset = on_sname,
                nuclei = nu_snames,
                codas = co_snames,
                count = Dice()-1
                )
            Surname3 = SyllabicGenerator(
                onset = on_sname,
                nuclei = nu_snames,
                codas = co_snames,
                count = Dice()-1
                )
            
            Surname4 = SyllabicGenerator(
                onset = on_sname,
                nuclei = nu_snames,
                codas = co_snames,
                count = Dice()-1
                )

            
        elif Dice(10) < 5:
            Name = SyllabicName(
                syllables = SyllabicExtraction(Names),
                min_syllables=1,
                max_syllables=8)
            Name2 = SyllabicName(
                syllables = SyllabicExtraction(Names),
                min_syllables=1,
                max_syllables=8)
            Surname = SyllabicName(
                syllables = SyllabicExtraction(Surnames),
                min_syllables=1,
                max_syllables=8)
            Surname2 = SyllabicName(
                syllables = SyllabicExtraction(Surnames),
                min_syllables=1,
                max_syllables=8)
            Surname3 = SyllabicName(
                syllables = SyllabicExtraction(Surnames),
                min_syllables=1,
                max_syllables=8)
            Surname4 = SyllabicName(
                syllables = SyllabicExtraction(Surnames),
                min_syllables=1,
                max_syllables=8)
            
        elif Dice(10)<5: 
            namer = MarkovNameGenerator(Names)
            Name = namer.generate_name()
            Name2 = namer.generate_name()
            surnamer = MarkovNameGenerator(Surnames)
            Surname = surnamer.generate_name()
            Surname2 = surnamer.generate_name()
            Surname3 = surnamer.generate_name()
            Surname4 = surnamer.generate_name()

            
            FullName =  Name + ' ' +  Name2 + ' ' + Surname + ' ' + Surname2 + ' ' + Surname3 + ' ' + Surname4 
            
        else:
            FullName =  random.choice(Names) + ' ' + random.choice(Names) + ' ' + random.choice(Surnames) + ' ' + random.choice(Surnames) + ' ' + random.choice(Surnames) + ' ' + random.choice(Surnames)

        return FullName
        

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
        "Shade",
        "Wander",
        "Penance",
        "Dream",
        "Serenity",
        "Bliss",
        "Fury",
        "Glee",
        "Insight",
        "Seeker",
        "Solemn",
        "Fate",
        "Grace",
        "Truth",
        "Honor",
        "Vigor",
        "Rapture",
        "Zeal",
        "Oath",
        "Radiant",
        "Sacred",
        "Bravery",
        "Cunning",
        "Defiance",
        "Elude",
        "Freedom",
        "Justice",
        "Mercy",
        "Temperance",
        "Trust",
        "Victory",
        "Vow",
        "Watch",
        "Will",
        "Silent",
        "Solace",
        "Subtle",
        "Thrift",
        "Vivid",
        "Abyss",
        "Serene",
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
        "Typhos",
        "Venox",
        "Grisham",
        "Blazefur",
        "Sulfuron",
        "Vornak",
        "Ildrex",
        "Mortigon",
        "Firesyl",
        "Lilivra",
        "Mornara",
        "Shadeveil",
        "Nefari",
        "Blazelle",
        "Sorcaria",
        "Vexiana",
        "Glimshade",
        "Vorrela",
        "Raventhorn",
        "Skullrend",
        "Shadowclaw",
        "Doomspire",
        "Felrend",
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
        "Kurzam",
        "Rhul",
        "Zorlarg",
        "Steamsable",
        "Onyxmaw",
        "Kral",
        "Moltenhorn",
        "Crimsonhorn",
        "Gloomhorn",
        "Madhorn",
        "Killsin",
        "Purific",
        "Nye",
        "Assurance",
        "Watson",
        "Faith",
        "Harris",
        "Ashes",
        "Shepard",
        "Tenacious",
        "Coleman",
        "Desire",
        "Llwyd",
        "Vanity",
        "Temple",
        "Submit",
        "French",
        "Fear",
        "Reynolds",
        "Wheelwright",
        "Called",
        "Burroughs",
        "Confidence",
        "Udal",
        "Remember",
        "Bond",
        "Recuerdo",
        "Miedo",
        "Obedience",
        "Young",
        "Faint",
        "Gilby",
        "Abuse",
        "Cawdrey",
        "Constant",
        "Calamy",
        "Calamidad",
        "Vanity",
        "Twisse",
        "Discretion",
        "Boston",
        "Buried",
        "Sampson",
        "Hateill",
        "Burton",
        "Forsaken",
        "Williams",
        "Virtue",
        "Shepard",
        "Amynus",
        "Smen",
        "Apronadius",
        "Abdamelek",
        "Xonsu",
        "Aziza",
        "Ramla",
        "Neema",
        "Cleopatra",
        "Jendayi",
        "At",
        "Sahura",
        "Hor",
        "Zesiro",
        "Nub",
        "Bubastis",
        "Tauret",
        "Sarapous",
        "Ma",
        "Sapt",
        "Ritho",
        "Nenet",
        "Sanura",
        "Sethenes",
        "Sept",
        "Uetu",
        "Kashto",
        "Clémence",
        "Firefur",
        "Gloomtail",
        "Nuuch",
        "Zenglac",
        "Ablo",
        "Gadreel",
        "Uzza",
        "Musique",
        "Haine",
        "Gloire",
        "Pyra",
        "Désespoir",
        "Doute",
        "Chagrin",
        "Terreur",
        "Ambition",
        "Vice",
        "Ouverture",
        "Amour",
        "Témérité",
        "Credo",
        "Charogne",
        "Chagrin",
        "Hasard",
        "Astaro", "Kali",
        "Brave",
        "Crash",
        "Delver",
        "Helm",
        "Hungry",
        "Violence",
        "Providence",
        "Surprise", "Conqueror",
        "Defender", "Invader",
        "Juvileo", "Nephelin",
        "Nefelin", "Serafina",
        "Luz", "Carolin",
        "Dilan", "Kurt",
        "Freddie", "Pride", "Bulur",
        "Abyx", "Apolion",
        "Abezetibou", "Abigor",
        "Abraxas", "Abraxis",
        "Solomon", "Aexma",
        "Acaos",
        "Adramalek",
        "Agares",
        "Ariman",
        "Agraz",
        "Ainin",
        "Alloces",
        "Alp",
        "Amduscias",
        "Amenadiel",
        "Amon",
        "Amorth",
        "Gabriele",
        "Andra",
        "Indra",
        "Andras",
        "Andrealfus",
        "Mastemoth",
        "Andromalius",
        "Angra",
        "Antaura",
        "Antichrist",
        "Antichristian",
        "Armadiel",
        "Aseliel",
        "Asmodeus",
        "Aeshma",
        "Ashmedai",
        "Asmodius",
        "Sydonay",
        "Astaroth",
        "Azael",
        "Azazel",
        "Baal",
        "Bael",
        "Balam",
        "Baphomet",
        "Bafomet",
        "Barbiel",
        "Barbuel",
        "Barmiel",
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
        "Bolfri",
        "Elberiz",
        "Bidiel",
        "Bifrons",
        "Botis",
        "Otis",
        "Buer",
        "Buriel",
        "Busyasta",
        "Cabariel",
        "Calder",
        "Camuel",
        "Caim",
        "Camion",
        "Carnesiel",
        "Caspiel",
        "Cassian",
        "Kerberos",
        "Cerberus",
        "Cesmak",
        "Coronzon",
        "Cimeries",
        "Constantine",
        "Crowley",
        "Daeva",
        "Deva",
        "Dev",
        "Daimon",
        "Agato",
        "Agatodaimon",
        "Kako",
        "Kakodaimon",
        "Dalkiel",
        "Dantanian",
        "Decarabia",
        "Carabia",
        "Demoriel",
        "Faustus",
        "Eligor",
        "Emoniel",
        "Erinyes",
        "Fury",
        "Furia",
        "Eurynomus",
        "Forneus",
        "Fortea",
        "Flauros",
        "Hauras",
        "Haurus",
        "Foras",
        "Furcas",
        "Furfur",
        "Gadreel",
        "Gadriel", "Garadriel",
        "Gediel", "Gemori",
        "Gamaliel", "Gamigin",
        "Solomon", "Gusion",
        "Hades",
        "Hagenti",
        "Harlequin",
        "Halahel",
        "Halpas",
        "Hecataea",
        "Hel",
        "Hemah",
        "Hutriel",
        "Iblis",
        "Icosiel",
        "Incubus",
        "Imp",
        "Ipos",
        "Isacaron",
        "Leviatan",
        "Cabala",
        "Sephirot",
        "Sefirot",
        "Kezer",
        "Kokmah",
        "Binah",
        "Kesed",
        "Geburah",
        "Tifarez",
        "Netzak",
        "Hod",
        "Yesod",
        "Malkut",
        "Kababiel",
        "Kesilim",
        "Kunda",
        "Kabiel",
        "Kokab",
        "Labartu",
        "Lahmu",
        "Lamastu",
        "Legion",
        "Lerajie",
        "Oary",
        "Leviatan",
        "Liliz",
        "Lucifer",
        "Luzer",
        "Lutin",
        "Macariel",
        "Malgaras",
        "Malphas",
        "Malpas",
        "Marbas",
        "Maseriel",
        "Mazaquin",
        "Mazzikin",
        "Mazikin",
        "Mazakin",
        "Menadiel",
        "Mefistofeles",
        "Moloch",
        "Morax",
        "Murmur",
        "Naberius",
        "Nephilim",
        "Nefilim",
        "Nemesis",
        "Nisroc",
        "Onoskelis",
        "Orias",
        "Ornias",
        "Orobas",
        "Ose",
        "Padiel",
        "Pamersiel",
        "Paimon",
        "Pairikas",
        "Pazuzu",
        "Santeria",
        "Purson",
        "Curson",
        "Rabisu",
        "Raum",
        "Ravana",
        "Raysiel",
        "Rimmon",
        "Ronove",
        "Roneve",
        "Sabbat",
        "Sabnak",
        "Salem",
        "Saleos",
        "Salt",
        "Samael",
        "Sammael",
        "Sariel",
        "Sarakiel",
        "Suriel",
        "Uriel",
        "Zerakiel",
        "Satanael",
        "Scepter",
        "Skepter",
        "Shamsiel",
        "Shax",
        "Chax",
        "Scox",
        "Shedim",
        "Sinistrari",
        "Lodovico",
        "Sitri",
        "Orleans",
        "Surin",
        "Symiel",
        "Taru",
        "Tase",
        "Teofilus",
        "Udug",
        "Ukobach",
        "Usiel",
        "Uziel",
        "Uzza",
        "Uriel",
        "Valac",
        "Valefor",
        "Vapula",
        "Vassago",
        "Veltis",
        "Vepar",
        "Separ",
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
        "Joba",
        "Kasmut",
        "Kemanub",
        "Khemut",
        "Maia",
        "Menhet",
        "Merit",
        "Nebet",
        "Neferu",
        "Nit",
        "Nofret",
        "Nubemiunu",
        "Peseshet",
        "Rai",
        "Sadeh",
        "Sadek",
        "Sitamun",
        "Sitre",
        "Takhat",
        "Tarset",
        "Werenro",
        "Ahmose",
        "Amasis",
        "Amenemhet",
        "Anen",
        "Banefre",
        "Bek",
        "Henenu",
        "Huya",
        "Ibebi",
        "Idu",
        "Ineni",
        "Ipuki",
        "Irsu",
        "Kawad",
        "Kawab",
        "Kenamon", "Kewap", "Khafra", "Khuesebek",
        "Masaharta", "Meketre", "Merenre", "Metjen",
        "Nebamun", "Nehi",
        "Nekure", "Nessumontu",
        "Pawah", "Ramose", "Rudjek", "Sabaf", "Sebni",
        "Senusret", "Shabaka", "Somintu",
        "Thaneni", "Theti", "Aktas", "Anakis",
        "Armara", "Astaro",
        "Astaroz", "Azza", "Belez",
        "Bune", "Criella",
        "Damaia", "Ishte",
        "Jezebez",
        "Kali", "Kallista",
        "Kasdeya", "Lilith",
        "Makaria", "Markosian", "Nemeian", "Nija",
        "Oriana", "Osah", "Felaia", "Pura", "Pyra",
        "Rieta", "Sekhmet", "Semyaza",
        "Shava", "Zendaya",
        "Shax", "Vapula", "Vepar", "Verin",
        "Akmen", "Amon",
        "Astar", "Balam",
        "Bazin", "Cain",
        "Caim",
        "Cimer",
        "Damakos",
        "Euron",
        "Kairon",
        "Nicor",
        "Oriax",
        "Paymon",
        "Atraxas",
        "Samal",
        "Zamuz",
        "Valafar",
        "Zezan",
        "Ambition",
        "Art",
        "Carrion",
        "Chant",
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
                
        "Abrasax",
        "Ariatari",
        "Azizi",
        "Amor",

        "Crimson",
        "Caos",

        "Dawala",

        "Grace",
        
        "Liberty",
        "Luz",
        "Luzimer",
        "Lust",
        "Love",
        
        "Mayhem",
        "Mockery",
        "Murder",
        "Muse",
        "Musa",
        "Music",
        "Mystery",

        "Nushim",
        "Nowhere",

        "Open",

        "Piety",
        "Pain",
        "Passion",
        "Poetry",
        
        "Quest",
        
        "Random",
        "Reverence",
        "Revulsion",
        "Risa",
        
        "Sorrow",
        "Solas",
        "Soleviel",
        "Soraz",
        
        "Temerity",
        "Torment",
        "Tragedy",

        "Umayma",
        
        "Vice",
        "Virtue",
        
        "Weary",
        "Wit",

        ]
    if Type == "Fiend":
        Names += Tieflings
        if Dice(10)<5: 
            namer = MarkovNameGenerator(Names)
            Name = namer.generate_name()
            
            FullName =  Name 
            
        else:
            FullName =  random.choice(Names)
            
        return FullName        



    Goblins = [
        "Alco",
        "Aldan",
        "Anbar",
        "Azaja",
        "Azur",

        "Badar",

        "Roshan",
        
        "Soraya",

        "Zahir",
        "Zephyr",
        
        "Tariq",
        "Nuray",
        "Marid",
        "Kaveh",
        "Simurgh",
        "Hazar",
        "Maysun",
        "Firouz",
        "Cyrus",
        "Almas",
        "Bahar",
        "Zahara",
        "Nadim",
        "Yasmin",
        "Zarparan", # ("Golden feather" in Persian),
        "Badira", # - ("Full moon", connoting beauty and awe),
        "Roshan", # - ("Bright" or "light", symbolizing illumination and wisdom),
        "Maysun", # - ("Beautiful" or "attractive"),
        "Nuray", # - ("Bright moon"),
        "Samir", 
        "Soraya", # - ("Pleiades", a star cluster, symbolizing wonder),
        "Tazim", # - ("Respect" or "admiration", carrying a sense of awe),
        "Yelda", # - ("Long, dark night", mysterious and evocative),
        "Zephyr", # - (A soft, gentle breeze, whimsical and playful),
        "Jinane", # - ("Gardens", connoting a sense of beauty and nature),
        "Azhar", # - ("Flowers", signifying beauty and nature),
        "Firouz", # - ("Turquoise", representing beauty and value),
        "Marid", # - (A term for a rebellious jinn, fitting for a mischievous goblin),
        "Narjis", # - ("Narcissus flower", beautiful and enchanting),
        "Bahir", # - ("Dazzling" or "brilliant"),
        "Laleh", # - ("Tulip", representing beauty and grace),
        "Parvaiz", # - (Derived from Persian, meaning "fortunate" or "lucky"),
        "Shirin", # - ("Sweet" or "pleasant"),
        "Kamaria", # - ("Moon-like", symbolizing beauty and radiance),
        "Zumurrud", # - ("Emerald", precious and beautiful),
        "Bazm", # - ("Party" or "feast", evoking fun and celebration),
        "Hayam", # - ("Infatuated" or "enamored", whimsical),
        "Diba", # - ("Brocade", signifying luxury and beauty),
        "Sahar", # - ("Dawn", new beginnings, hope),
        "Dobby",
        "Chal",
        "Alsi",
        "Ax",
        "Pilb",
        "Eg",
        "Udag",
        "Pilsi",
        "Pil",
        "Amal",
        "Valaravanx",
        "Azarid",
        "Walajmar",
        "Roduulf",
        "Aidoingux",
        "Azanagi",
        "Agila",
        "Gainax",
        "Selenax",
        "Melisanda",
        "Radegond",
        "Seda",
        "Gaxa",
        "Amalafrida",
        "Duda",
        "Wamba",
        "Ariux",
        "Azarid",
        "Gunteric",
        "Tanaix",
        "Jordanex",
        "Badua",
        "Braja",
        "Narin",
        "Giso",
        "Elisaweta",
        "Raxa",
        "Amalgard",
        "Sunnia",
        "Wella",
        "Aoric",
        "Aligern",
        "Unigild",
        "Razaladar",
        "Alsiu",
        "Amanal",
        "Dund",
        "Megi",
        "Pinag",
        "Budan",
        "Agala",
        "Selx",
        "Gudus",
        "Dona",
        "Bunging",
        "Udaler",
        "Arnensi",
        "Ravava",
        "Wagic",
        "Ambanda",
        "Sellalby",
        "Azadusar",
        "Azaz",
        "Walsi",
        "Nardu",
        "Ralaga",
        "Rajar",
        "Arida",
        "Doril",
        "Rand",
        "Azari",
        "Amand",
        "Azawe",
        "Azal", "Axar", "Xavan", "Rada",
        "Selala", "Galar", "Druzol",
        "Azal", "Azar", "Udarn",
        "Azava", "Alal", "Elba", "Alil",
        "Amaxa", "Azana", "Ralel",
        "Amaxa", "Arinele", "Azoba",
        "Garag", "Axal", "Axagi",
        "Talala", "Azari",
        "Rajma", "Axar",
        "Ralan", "Azax",
        "Vala",
        "Radus",
        "Azava",
        "Pilax",
        "Talxa",
        "Azar",
        "Azahar",
        "Rhana",
        "Selan",
        "Azals",
        "Chandar",
        "Azav",
        "Doby",
        "Susal",
        "Azag",
        "Azan",
        "Azal",
        "Wari",
        "Azag",
        "Azaril",
        "Nadag",
        "Azaja",
        "Gungi",
        "Buda",
        "Ralar",
        "Udala",
        "Elge",
        "Azaxar",
        "Dris",
        "Gana",
        "Udar",
        "Elida",
        "Azan",
        "Alad",
        "Ravanda",
        "Nals",
        "Pic",
        "Aby",
        "Mada",
        "Rorna",
        "Amba",
        "Ardun",
        "Azariga",
        "Duna",
        "Buada",
        "Vagi",
        "Azava",
        "Guna",
        "Amal",
        "Azav",
        "Ralan",
        "Ralav",
        "Rajad",
        "Talsi",
        "Amal",
        "Rarid",
        "Randa",
        "Amazo",
        "Wava",
        "Magus",
        "Guna",
        "Slay",
        "Dasker",
        "Kexam",
        "Mukert",
        "Rensox",
        "Xembor",
        "Guknag",
        "Sabsen",
        "Gundobag",
        "Burk",
        "Azava",
        "Zasiki",
        "Warishi"
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
        "Redsnow Clan",
        "Yellowsnow Clan",
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
        Names += Goblins            

        if Dice(10)<5:
            FullName = SyllabicGenerator(
                onset = ['So','Ro','Aza', 'Al', 'Za', 'Ze', 'Az', 'Ba', 'Am'],
                nuclei = ['', 'ra', 'ja', 'ha', 'co'],
                codas = ['shan','ja', 'dan', 'hir','','fir','ur', 'dar', 'bar'],
                count = Dice(2)
                )
            
        elif Dice(10) < 5:
            Name = SyllabicName(
                syllables = SyllabicExtraction(Names),
                min_syllables=2,
                max_syllables=3)
                
            FullName =  Name 

        elif Dice(10) < 5:
            namer = MarkovNameGenerator(Names)
            Name = namer.generate_name()
                
            FullName =  Name 
                
        else:
            FullName =  random.choice(Names)

        return FullName + " of the " + random.choice(Clans)



    if "Beast" in npc.race:
        Beasts = []
        
        Names += Beasts

    if "Beastfolk" in npc.race:
        Beasts = []
        
        Names += Beasts

        
    
    if "Plant" in npc.race:
        Plants = [
            "Artemisia",
            "Aidenia",

            "Dalia",
            
            "Naussia",
            "Nubia",
            "Numia",
            "Nustia",

            "Rennia",
            "Talria",
            
            "Jussia",
            "Ejamia",
            "Elyria",
            "Venusia",
            "Rihannia",
            "Calliopia",
            "Tallia",
            "Talia",
            "Artemia",
            "Ardenia",
            "Nusia",
            "Nalia",
            "Vemia",
            "Alia",
            "Nusia",
            "Nalia",
            "Venasia",
            "Artenia",
            "Elisia",
            "Venia",
            "Sinia",
            "Rosia",
            "Celestia",
            "Titania",
            "Amelia",
            ]
        
        Names += Plants
        

    if "Undead" in npc.race:
        Undeads = [
            "Amunet",
            "Bastet",
            "Khufu",
            "Nefertari",
            "Seti",
            "Anubis",
            "Tah",
            "Neith",
            "Senusret",
            "Meritamun",
            "Tutankhamun",
            "Hatshepsut",
            "Amenhotep",
            "Sobekhotep",
            "Mutnofret",
            "Irynefer",
            "Merneith",
            "Userkaf",
            "Mutemwia",
            "Horemheb",
            "Tauret",
            "Montuhotep",
            "Meresankh",
            "Pepi",
            "Tuthmosis",
            "Ankhesenamun",
            "Amenemhat",
            "Renpet",
            "Nakht",
            "Nubia",
            "Sobekneferu",
            "Khaemweset",
            "Tuya",
            "Meryt",
            "Seshat",
            'Cepos',
            'Aia',
            'Zosar',
            'Achencheres',
            'Rah',
            'Ahmesseker',
            'Djoser',
            'Uthman',
            'Baahir',
            'Hager',
            'Pilis',
            'Naguib',
            'Bast',
            'Abianes',
            'Nkosi',
            'Aaheru',
            'Donkor',
            'Zahur',
            'Akl',
            'Amenhotep',
            'Ahmose',
            'Aaani',
            'Mosiah',
            'Uratum',
            'Darwish',
            'Acetaminophen', 'Adderall', 'Amitriptyline', 'Amlodipine', 'Amoxicillin', 'Ativan', 'Atorvastatin', 'Azithromycin', 'Benzonatate', 'Brilinta', 'Bunavail', 'Buprenorphine', 'Cephalexin', 'Ciprofloxacin', 'Citalopram', 'Clindamycin', 'Clonazepam', 'Cyclobenzaprine', 'Cymbalta', 'Doxycycline', 'Dupixent', 'Entresto', 'Entyvio', 'Farxiga', 'Fentanyl Patch', 'Gabapentin', 'Gilenya', 'Humira', 'Hydrochlorothiazide', 'Hydroxychloroquine', 'Ibuprofen', 'Imbruvica', 'Invokana', 'Januvia', 'Jardiance', 'Kevzara', 'Leqvio', 'Lexapro', 'Lisinopril', 'Lofexidine', 'Loratadine', 'Lyrica', 'Melatonin', 'Meloxicam', 'Metformin', 'Methadone', 'Methotrexate', 'Metoprolol', 'Mounjaro', 'Naloxone', 'Naltrexone', 'Naproxen', 'Narcan', 'Nurtec', 'Omeprazole', 'Onpattro', 'Otezla', 'Ozempic', 'Pantoprazole', 'Plan B', 'Prednisone', 'Probuphine', 'Rybelsus', 'secukinumab', 'Sublocade', 'Tramadol', 'Trazodone', 'Viagra', 'Wegovy', 'Wellbutrin', 'Xanax', 'Zubsolv'
            'Aciclovir', 'Zovirax', 'Acrivastine', 'Adalimumab', 'Alendronic', 'Allopurinol', 'Alogliptin', 'Amitriptyline', 'Amlodipine', 'Amoxicillin', 'Anastrozole', 'Apixaban', 'Aripiprazole', 'Aspirin', 'Atenolol', 'Atorvastatin', 'Azathioprine', 'Azithromycin', 'Baclofen', 'Beclometasone', 'Bendroflumethiazide', 'Benzoyl', 'Peroxide', 'Benzydamine', 'Betahistine', 'Betamethasone', 'Bimatoprost', 'Bisacodyl', 'Bisoprolol', 'Brinzolamide', 'Budesonide', 'Bumetanide', 'Buprenorphine', 'Buscopan', 'Hyoscine ', 'Butylbromide', 'Calcipotriol', 'Candesartan', 'Carbamazepine', 'Carbimazole', 'Carbocisteine', 'Carmellose', 'Carvedilol', 'Cefalexin', 'Cetirizine', 'Champix', 'Varenicline', 'Chloramphenicol', 'Chlorhexidine', 'Chlorphenamine', 'Piriton', 'Cinnarizine', 'Ciprofloxacin', 'Citalopram', 'Clarithromycin', 'Clobetasol', 'Clobetasone', 'Clonazepam', 'Clonidine', 'Clopidogrel', 'Clotrimazole', 'Canesten', 'Coamoxiclav', 'Cobeneldopa', 'Cocareldopa', 'Cocodamol', 'Cocodaprin', 'Codydramol', 'Coaltar', 'Codeine', 'Colchicine', 'Colecalciferol', 'Medroxyprogesterone', 'Cyanocobalamin', 'Cyclizine', 'Dabigatran', 'Dapagliflozin', 'Dexamethasone', 'Diazepam', 'Diclofenac', 'Digoxin', 'Dihydrocodeine', 'Diltiazem', 'Diphenhydramine', 'Dipyridamole', 'Docusate', 'Domperidone', 'Donepezil', 'Dosulepin', 'Doxazosin', 'Doxycycline', 'Duloxetine', 'Edoxaban', 'Empagliflozin', 'Enalapril', 'Eplerenone', 'Erythromycin', 'Escitalopram', 'Esomeprazole', 'Ezetimibe', 'Felodipine', 'Fentanyl', 'Ferrousfum', 'Ferroussulf', 'Fexofenadine', 'Finasteride', 'Flucloxacillin', 'Fluconazole', 'Prozac', 'Fluticasone', 'Folic', 'Furosemide', 'Fusidic', 'Fybogel', 'Ispaghula ', 'Husk', 'Gabapentin', 'Gaviscon ', 'Alginic', 'Gliclazide', 'Glimepiride', 'Glyceryl', 'Trinitrate', 'Haloperidol', 'Heparinoid', 'Hydrocortisone', 'Hydroxocobalamin', 'Hydroxychloroquine', 'Hyoscine', 'Hydrobromide', 'Ibuprofen ', 'Codeine', 'Ibuprofen', 'Nurofen', 'Ibuprofen', 'Indapamide', 'Insulin', 'Irbesartan', 'Isosorbide ', 'Mononitrate', 'Isosorbide', 'Dinitrate', 'Roaccutane', 'Isotretinoin ', 'Isotrex', 'Ketoconazole', 'Labetalol', 'Lactulose', 'Lamotrigine', 'Lansoprazole', 'Latanoprost', 'Lercanidipine', 'Letrozole', 'Levetiracetam', 'Levothyroxine', 'Lidocaine', 'Linagliptin', 'Lisinopril', 'Lithium', 'Loperamide', 'Loratadine ', 'Clarityn', 'Lorazepam', 'Losartan', 'Lymecycline', 'Macrogol', 'Mebendazole', 'Mebeverine', 'Medroxyprogesterone', 'Melatonin', 'Memantine', 'Mesalazine', 'Metformin', 'Methadone', 'Methotrexate', 'Methylphenidate', 'Metoclopramide', 'Metoprolol', 'Metronidazole', 'Mirabegron', 'Mirtazapine', 'Molnupiravir ', 'Lagevrio', 'Mometasone', 'Montelukast', 'Morphine', 'Naproxen', 'Nefopam', 'Nicorandil', 'Nifedipine', 'Nitrofurantoin', 'Nortriptyline', 'Nystatin', 'Olanzapine', 'Olmesartan', 'Omeprazole', 'Oxybutynin', 'Oxycodone', 'Pantoprazole', 'Paracetamol', 'Calpol', 'Paroxetine', 'Paxlovid', 'Peppermintoil', 'Peptobismol ', 'Bismuth ', 'Subsalicylate', 'Perindopril', 'Phenoxymethylpenicillin', 'Phenytoin', 'Pioglitazone', 'Pravastatin', 'Prophylaxis', 'Prednisolone', 'Pregabalin', 'Prochlorperazine', 'Progesterone', 'Utrogestan', 'Promethazine ', 'Phenergan', 'Propranolol', 'Pseudoephedrine ', 'Sudafed', 'Quetiapine', 'Rabeprazole', 'Ramipril', 'Ranitidine', 'Remdesivir ', 'Veklury', 'Risedronate', 'Risperidone', 'Rivaroxaban', 'Ropinirole', 'Rosuvastatin', 'Salbutamol', 'Saxagliptin', 'Senna', 'Sertraline', 'Sildenafil', 'Simeticone', 'Simvastatin', 'Sitagliptin', 'Cromoglicate', 'Valproate', 'Solifenacin', 'Sotalol', 'Sotrovimab ', 'Xevudy', 'Spironolactone', 'Sulfasalazine', 'Sumatriptan', 'Tadalafil', 'Tamsulosin', 'Temazepam', 'Terbinafine', 'Thiamine', 'Tibolone', 'Ticagrelor', 'Timolol eye', 'Tiotropium', 'Tolterodine', 'Topiramate', 'Tramadol', 'Tranexamic', 'Trastuzumab ', 'Herceptin', 'Trazodone', 'Trimethoprim', 'Utrogestan', 'progesterone', 'Valproicacid', 'Valsartan', 'Varenicline', 'Champix ', 'Varenicline', 'Venlafaxine', 'Verapamil', 'Warfarin', 'Zolpidem', 'Zopiclone',
            ]

        Names += Undeads

        if "Vampire" in npc.subrace:
            Vampires = [
                'Dracula',
                'Vonrichter',
                'Sivert',
                'Narten',
                'Faredun',
                'Armun',
                'Farkhan',
                'Blanche',
                'Hunston',
                'Elizabeth',
                'Anesthesia',
                'Eslavor',
                'Ansiare',
                'Lestrat',
                'Estesia',
                'Nosferatu',
                'Barnabas',
                'Count',
                'Lestat',
                'Louis',
                'Claudia',
                'Blade',
                'Lux',
                'Xado',
                'Selene',
                'Eli',
                'Stefan',
                'Salvatore',
                'Morbius',
                'Katherine',
                'Marceline',
                'Akasha',
                'Alexander',
                'Baltazar',
                'Caius',
                'Caelan', 'Cain', 'Casanova', 'Claudia',
                'Cleopatra',
                'Demian',
                'Darius', 'Dorian', 'Alucard', 'Tepes', 'Vladracul',
                'Vlad', 'Tepes', 'Eudoxia', 'Gabrielle', 'Laurent',
                'Lilith', 'Magnus', 'Maladict', 'Neferata', 'Neferet', 
                'Nicodemus', 'Pandora', 'Sauron', 'Socrates', 'Xander',
                'Zafrina', 'Alexander', 'Lucard', 'Tesla', 'Caleb',
                'Daedalus', 'Eramus', 'Incongitus', 'Judas', 'Iscariot',
                'Kraven', 'Marcus', 'Seras', 'Victoria', 'Siddhartha',
                'Vladimir', 'Valentine', 'Hellsing', 'Dumas', 'Kain',
                'Lazarus', 'Orpheus', 'Drarian', 'Lesaricus', 'Orinus',
                'Kasandre', 'Lorian', 'Sidarta', 'Selena', 'Elektra',
                'Edipo', 'Alazane', 'Lefair', 'Samael', 'Benedict',
                'Barnard', 'Solomon', 'Rose', 'Hanibal', 'Beatrice',
                'Alice', 'Bastavar', 'Melkor', 'Gaspar', 'Baltasar',
                'Aerik', 'Siamak', 'Astaroz', 'Roxana', 'Helena', 'Agripa',
                'Cornelius', 'Magnus', 'Belladona', 'Jerico', 'Albion',
                'Bane', 'Claw', 'Lance', 'Valentine', 'Valentina', 'Krauss',
                'Casandra', 'Pompadour', 'Moriarty', 'Delacroix', 'Kurt',
                'Lucrecia', 'Romulus', 'Solomon', 'Salizar', 'Salazar',
                'Andromeda', 'Xavier', 'Xosefus', 'Isabella', 'Mortensen',
                'Vondrak', 'Jezebell', 'Barlow', 'Crowley', 'Josephine',
                'Kristopher', 'Luther', 'Vincent', 'Ambrose', 'Cornelius',
                'Diego', 'Devon', 'Lucius', 'Luna', 'Samuel', 'Sirius',
                'Zane', 'Demetrius', 'Orlando', 'Fausto', 'Ofelia',
                'Ulises', 'Nemo', 'Dante', 'Leonor', 'Rouge', 'Remus',
                'Victor', 'Virgil', 'Virginia', 'Samaras', 'Sorin',
                'Markov', 'Felisa', 'Fang', 'Valentin', 'Crovax',
                'Kazarov', 'Florian', 'Voldaren', 'Henrika', 'Odric',
                'Olivia', 'Estrefan', 'Elenda', 'Vona', 'Vito',
                'Maurer', 'Kinzu', 'Vraan', 'Anhelo', 'Cormela', 'Evelyn',
                'Xander', 'Zoltan', 'Baron', 'Sergin', 'Sangre', 'Sanguineo',
                'Drana', 'Licia', 'Monoxa', 'Nocturno', 'Astarion', 'Sorin',
                'Markov', 'Damon', 'Darius', 'Nemus', 'Karius', 'Andara',
                'Alana', 'Sasamus', 'Vicesar', 'Sariam', 'Nemion', 'Kabel',
                'Kaibel', 'Draven', 'Maleficent', 'Morticia', 'Akenaton',
                'Keops', 'Imhotep', 'Neferkare', 'Nefertiti', 'Akhenaton',
                'Ramses', 'Rameses', 'Seti', 'Cleopatra', 'Imhotep',
                'Amelia', 'Vetala', 'Desmon', 'Rufus', 'Desmodus',

                'Carmilla',

                ]
            Names += Vampires
            onset = ["Mor", "Vor", "Gra", "Shri", "Nec",
                     "Phan", "Skel", "Ghul", "Vam", "Spect",
                     "Wail", "Lich", "Crypt", "Dread", "Bane",
                     "Haunt", "Ruin", "Whisp", "Val", "Luc", "Oct", "Max",
                     "Cass", "Aur", "Mar", "Silv", "Const", "Vit", "Claud",
                     "Flor", "Grat", "Hor", "Jul", "Leon", "Narc", "Prisc",
                     "Quint", "Reg", "Ser", "Tac", "Virg", "Xen", "Zeph",
                     "Bel", "Ren", "Est", "Lor", "Gael", "Raf", "Em", "Car",
                     "Fab", "Gio", "Leon", "Maur", "Nicol", "Patr", "Raim",
                     "Ric", "Serg", "Theo", "Vinc", "Yves"]
            nuclei = ["a", "e", "i", "o", "u", "ae", "ai", "ea", "ie", "ou",
                      "io", "ou", "ia", "eu", "ae", "oe", "au", "ei", "ui",
                      "ya", "yo", "ye", "oa", "eo", "iu",
                      "","","","","","","","","","","","","","","","",""]
            codas = ["mire", "gast", "raith", "reth", "loom", "moth",
                     "nacht", "geist", "bone", "fang", "shade", "tear",
                     "gor", "grim", "thorn", "shade", "gloom", "crypt",
                     "ius", "an", "or", "um", "as", "es", "is", "os",
                     "us", "ent", "ix", "ax", "on", "ar", "ium", "ina",
                     "ora", "ena", "to", "do", "no", "lo", "ro", "so",
                     "ta", "da", "na", "la", "ra", "sa", "nte", "nce",
                     "lle", "tte", "che", "gno", "mio", "tio"]
                           
       


            subrace_syllables = {
                "Death Knight": {
                    "onset": ["Krieg", "War", "Ruin", "Doom"],
                    "nuclei": ["au", "o", "ui"],
                    "codas": ["garde", "blade", "helm"]
                    },
                "Vampire": {
                    "onset": ["Sang","Vamp", "Noct", "Blood", "Night", "Drac", "Carm"],
                    "nuclei": ["i", "ae", "u", "ul"],
                    "codas": ["fang", "sire", "thirst", "la",]
                    },
                "Lich": {
                    "onset": ["Lich", "Arcan", "Necro", "Immort"],
                    "nuclei": ["e", "a", "o", "no","xa","ki"],
                    "codas": ["mancer", "lich", "lore"]
                    },
                "Wraith": {
                    "onset": ["Wraith", "Spect", "Shade", "Ghast"],
                    "nuclei": ["a", "e", "i"],
                    "codas": ["wail", "fury", "shade"]
                    },
                }

            # Selecting the specific syllables for the subrace
            subrace_onset, subrace_nuclei, subrace_codas = subrace_syllables[subrace].values()
            onset.extend(subrace_onset)
            nuclei.extend(subrace_nuclei)
            codas.extend(subrace_codas)
            
            # Fallback to common syllables if specific ones aren't provided

            Name = NewName(Names,
                           onset=onset,
                           nuclei=nuclei,
                           codas = codas
                           ) 
            return Name        

    if Type == "Lizardfolk":
        Lizardfolk = [
            "Gojira",
            "Gozilla",
            "Kermit",
            "Lizzy",
            "Argonian",
            "Kroxigor",
            "Throgg",
            "Sobek",
            "Kaa",
            "Slippy",
            "Frogger",
            "Jabba",
            "Godzilla",
            "Gorn",
            "Reptar",
            "Rango",
            "Charizard",
            "Lickitung",
            "Salazzle",
            "Bowser",
            "Koopa",
            "Rath",
            "Gex",
            "Turok",
            "Crocomire",
            "Leatherhead",
            "Killcroak",
            "Thornback",
            "Yenpa",
            ]
        Names += Lizardfolk

    if "Turtle" in npc.subrace:
        Turtlefolk = [
            "Donatello",
            "Leonardo",
            "Michelangelo",
            "Raphael",
            # Teenage Mutant Ninja Renaissance Artists!
            "Botticelli",
            "Caravaggio",
            "Giotto",
            "Titian",
            "Verrocchio",
            "Masaccio",
            "Bellini",
            "Tintoretto",
            "Uccello",
            "Bronzino",
            "Vasari",
            "Greco",
            "Ghiberti",
            "Perugino",
            "Vincent",       # Vincent van Gogh, Post-Impressionist painter
            "Vangogh",       
            "Rembrandt",     # Rembrandt van Rijn, Dutch Golden Age painter
            "Picasso",       # Pablo Picasso, Spanish painter and sculptor, known for Cubism
            "Dali",          # Salvador Dalí, Spanish Surrealist artist
            "Monet",         # Claude Monet, founder of French Impressionist painting
            "Klimt",         # Gustav Klimt, Austrian Symbolist painter
            "Cezanne",       # Paul Cézanne, French artist and Post-Impressionist painter
            "Gauguin",       # Paul Gauguin, French Post-Impressionist artist
            "Matisse",       # Henri Matisse, French artist, known for his use of color and draughtsmanship
            "Hokusai",       # Katsushika Hokusai, Japanese ukiyo-e artist
            "Warhol",        # Andy Warhol, leading figure in the visual art movement known as pop art
            "Frida",         # Frida Kahlo, Mexican painter known for her many portraits and self-portraits
            "Keeffe",        # Georgia O'Keeffe, American artist known for her paintings of enlarged flowers
            "Pollock",       # Jackson Pollock, American painter and a major figure in the abstract expressionist movement
            "Basquiat",      # Jean-Michel Basquiat, American artist known for his raw gestural style of painting
            "Kandinsky",     # Wassily Kandinsky, Russian painter and art theorist
            "Rothko",        # Mark Rothko, American abstract painter known for his color field paintings
            "Goya",          # Francisco Goya, Spanish romantic painter and printmaker
            "Davinci",       # Leonardo da Vinci, Italian polymath of the Renaissance
            "Beksinski",
            ]
        Names += Turtlefolk
        
        Name = NewName(Names,
                    onset=["Don", "Leo", "Mich", "Raph", "Bott", "Cara", "Giot", "Tit", "Verr", "Masa", "Bell", "Tinto", "Ucc", "Bron", "Vas", "Grec", "Ghib", "Peru", "Vinc", "Van", "Rem",
                           "Pic", "Dal", "Mon", "Klim", "Cez", "Gaug", "Mat", "Hoku", "War", "Frid", "Kee", "Poll", "Basi", "Kand", "Roth", "Goy", "Davi",
                           ],
                    nuclei=["a", "e", "i", "o", "u", "ello", "ardo", "angelo", "ael", "icci", "aggio", "otto", "ian", "occhio", "accio", "ini", "etto", "ello", "ino", "eco", "erti", "ino", "ent",
                            "ang", "brandt", "asso", "ali", "net", "mt", "sse", "sai", "hol", "rida", "effe", "llock", "quiat", "insky", "thko", "ya", "vinci"
                            ],
                    codas=["tello", "nardo", "gelo", "phael", "celli", "vaggio", "otto", "tian", "cchio", "saccio", "ini", "tto", "cello", "sari", "eco", "hiberti", "gino", "cent", "gogh",
                           "brandt", "sso", "li", "net", "mt", "sse", "sai", "hol", "rida", "effe", "llock", "quiat", "insky", "thko", "ya", "vinci"
                           ]) 
        return Name


    Name = NewName(Names,
                onset=["Ss", "Kr", "Zr", "Ts", "Xy", "Gr", "Vr", "Sk", "Sl", "Dr", "Hs", "Ks", "Zs", "Ch", "Gh", "Kl", "Tl", "Vl", "Zl", "Rz", "Sz", "Th", "Xz", "Yz", "Bl", "Br", "Dz",
                       "Fr", "Gl", "Gz", "Go", "Kro", "Thro", "So", "Ka", "Slip", "Jab", "Gor", "Rep", "Ran", "Char", "Lick", "Sala", "Bow", "Koo", "Rath", "Gex", "Tur", "Croco", "Lea",
                       "Kill", "Thorn", "Yen", "Liz", "Kerm", "Argo", "Frog", "Godz", "Rango", "Turo",
                       "Kowal", "Nowak", "Wiśn", "Wójc", "Kamiń", "Lewand", "Dąb", "Sobie", "Kacz", "Zaj", "Baran", "Król", "Maj", "Jawor", "Malin", "Sta", "Pol", "Szczep", "Czar", "Kubi",
                       ],
                nuclei=["a", "e", "i", "o", "u", "aa", "ee", "ii", "oo", "uu", "ae", "ai", "ao", "au", "ea", "ei", "eo", "eu", "ia", "ie", "io", "iu", "oa", "oe", "oi", "ou",
                        "ua", "ue", "ui", "uo", "a", "o", "i", "e", "u", "ira", "illa", "oro", "oga", "ango", "aro", "izo", "ix", "ung", "or", "urt", "ack", "oop", "yth",
                        "yth", "rog", "er", "on", "zar", "ong", "ile", "urt", "zar", "ith", "ert",
                        "i", "e", "a", "o", "ow", "ak", "ew", "ie", "ko", "czy", "ski", "ska", "czak", "ek", "ik", "yk", "uk", "asz", "ysz", "isz"
                        ],
                codas=["sk", "ss", "zz", "rk", "rt", "lk", "lt", "nt", "pt", "kt", "xt", "ch", "sh", "th", "nd", "ng", "nk", "mp", "kt", "lp", "rp", "sp", "st", "tch", "xk", "zk",
                       "rs", "ls", "ts", "ns", "ra", "gor", "mit", "zy", "nian", "igor", "ogg", "bek", "aa", "py", "ger", "ba", "zilla", "rn", "tar", "go", "zard", "tung", "zzle",
                       "ser", "pa", "th", "ex", "rok", "mire", "head", "croak", "back", "npa",
                       "ski", "cka", "dzki", "ak", "ek", "ik", "owski", "ewicz", "inski", "kiewicz", "czyk", "czak", "szek", "zak", "ko", "owski", "ewski", "owski", "yński", "akowski",
                       
                       ]) 
    return Name
    
    if Type == "Kobold":
        Kobold_Names = [
            "Aki",
            "Assik",
            "Bik",
            "Biki",
            "Bakaki",
            "Coromanic",
            "Deekin",
            "Durnn",
            "Eek",
            "Kurtulmak",
            "Kib",
            "Meepo",
            "Hox",
            "Grit",
            "Naknak",
            "Fizban",
            "Gnarl",
            "Grizzle",
            "Kratch",
            "Pog",
            "Ratch",
            "Scamp",
            "Snarl",
            "Skizziks",
            "Snick",
            "Sniv",
            "Squee",
            "Sqwik",
            "Slythe",
            "Torch",
            "Tucker",
            "Urdo",
            "Whiskar",
            "Yipper",
            "Zax",
            "Zik",    
            "Snarklefang",
            "Gizzik",
            "Rattlewhisk",
            "Zippik",
            "Glint",
            "Nibsnarf",
            "Skreech",
            "Mizznix",
            "Breezle",
            "Whiskerfizz",
            "Krazzle",
            "Fizzlebang",
            "Grizzle",
            "Trazzik",
            "Poggle",
            "Bizzik",
            "Cracklefizz",
            "Squeak",
            "Dazzlefix",
            "Gobblewarp",
            "Jinxle",
            "Vizzlebop",
            "Prattlebark",
            "Squibble",
            "Zibzob",
            "Einsteek",
            "Cleopatrickle",
            "Davizzik",
            "Shakesqueak",
            "Mozfizzle",
            "Beethovinik",
            "Gandalfang",
            "Picazzok",
            "Hawkingsnarl",
            "Curiecrackle",
            "Newtonnibble",
            "Galileoglint",
            "Edisonspark",
            "Teslaflash",
            "Darwizzle",
            "Flemingfuzz",
            "Freudfiddle",
            "Tolkienwhisk",
            "Rowlingrumble",
            "Gatesglimmer",
            "Jobsjingle",
            "Houdinibop",
            "Einsteinix",
            "Nightingfizz",
            "Mandibuzz",
            "Lincolnik",
            "Churchillchomp",
            "Rooseveltrix",
            "Thatchertwist",
            "Kennedikwik",
            "Gandhiglint",
            "Merkelfizzle",
            "Obamablink",
            "Putinspark",
            "Macronmunch",
            "Trudeautrickle",
            "Reaganrattle",
            "Nixonnibble",
            "Disraelidazzle",
            "Bismarckbop",
            "Castrocrackle",
            "Mandelaflash",
            "TheresaTwinkle",
            "Blairblaze",
            "Bushbushel",
            "Maymerriment",
            "Trumptwirl",
            "Bidenbreeze",
            "Churchspark",
            "Stalinstealth",
            "Elvizzle",
            "Madonnak",
            "Beyonzbuzz",
            "Beyonzik",
            "Rihannarix",
            "Gagaglint",
            "Drakedrizzle",
            "Eminemunch",
            "Snoopdoggspark",
            "Shakirashine",
            "Jaggerjingle",
            "Bowiwhisk",
            "Princeprickle",
            "Tupacshimmer",
            "Beyzle",
            "Fitzfizzle",
            "Marleymane",
            "Dylansnarl",
            "Joplinsqueak",
            "Sinatrasnap",
            "Bjorkbubble",
            "Kobainkink",
            "Adeleadle",
            "Britneysplinter",
            "Pinkpuff",
            "Brunobrizzle"
            ]
        Names = Kobold_Names

        Name = NewName(Names,onset,nuclei,codas) 
        return Name







    if Type == "Monstrosity":

        Monstrosity_Names = [
            "Bulektri",
            "Thyrm",
            "Kragma",
            "Slytherr",
            "Vorlash",
            "Grindle",
            "Morgax",
            "Draknos",
            "Venomar",
            "Thrashtalon",
            "Skreech",
            "Vorgash",
            "Charron",
            "Gloomclaw",
            "Ravix",
            "Snarlgrim",
            "Blightfang",
            "Kryx",
            "Zephyros",
            "Stormrend",
            "Nemnir",
            "Gastrix",
            "Varthrax",
            "Sunderbeak",
            "Cyclonix",
            "Razorfang",
            "Shriekshell",
            "Dreadmaw",
            "Gorgath",
            "Fenroar",
            "Quillspike",
            "Marlgoth",
            "Ironscale",
            "Ebonclaw",
            "Thornback",
            "Wrathmore",
            "Skyterror",
            "Grizzlemaul",
            "Slitherfang",
            "Bramblethorn",
            "Nightscream",
            "Cragjaw",
            "Echo",
            "Frostgaze",
            "Infernox",
            "Mudgraw",
            "Obsidion",
            "Ripple",
            "Squall",
            "Tempest",
            "Whisper",
            "Zephyr"
            "Grendel",  # From "Beowulf"
            "Kaiju",
            "Mothra",  # From the Godzilla franchise
            "Balrog",  # From "The Lord of the Rings"
            "Chimera",  # From Greek mythology
            "Basilisk",  # From European folklore and "Harry Potter"
            "Gorgon",  # From Greek mythology
            "Behemoth",  # From the Bible
            "Leviathan",  # From the Bible
            "Rodan",  # From the Godzilla franchise
            "Cerberus",  # From Greek mythology
            "King Ghidorah",  # From the Godzilla franchise
            "Hydra",  # From Greek mythology
            "Argus",  # From Greek mythology, referring to Argus Panoptes
            "Minotaur",  # From Greek mythology
            "Orthrus",  # A two-headed dog from Greek mythology
            "Skoll",  # A wolf from Norse mythology
            "Hati",  # Another wolf from Norse mythology
            "Nemean",  # Referring to the Nemean lion from Greek mythology
            "Typhon",  # From Greek mythology
            "Echidna",  # Mother of monsters in Greek mythology
            "Scylla",  # From Greek mythology
            "Charybdis",  # From Greek mythology
            "Manticore",  # A mythical beast from Persian lore
            "Griffin",  # A creature with the body of a lion and the head and wings of an eagle
            "Sphinx",  # From Greek mythology
            "Cthulhu",  # From H.P. Lovecraft's stories
            "Dagon",  # From H.P. Lovecraft's stories and biblical mythology
            "Yog-Sothoth",  # From H.P. Lovecraft's stories
            "Nyarlathotep",  # From H.P. Lovecraft's stories
            "Shub-Niggurath",  # From H.P. Lovecraft's stories
            "Fenrir",  # A monstrous wolf from Norse mythology
            "Jormungandr",  # The Midgard Serpent from Norse mythology
            "Tiamat",  # A dragon goddess from Mesopotamian mythology
            "Gojira",  # The original Japanese name for Godzilla
            "Zuul",  # From the film "Ghostbusters"
            "Vincent",  # A nod to Vincent Price, often associated with horror
            "Orlok",  # Count Orlok from "Nosferatu"
            "Audrey II",  # From "Little Shop of Horrors"
            "Asmodeus",  # A demon king from the Apocrypha and later occult lore
            "Pazuzu",  # From Assyrian and Babylonian mythology, known from "The Exorcist"
            "Ghoul",  # A monster or evil spirit from Arabic mythology
            "Bunyip",  # A creature from Aboriginal Australian mythology
            "Quetzalcoatl",  # A feathered serpent deity from Mesoamerican culture
            "Anansi",  # A trickster god in the form of a spider from African folklore
            "Wendigo",  # A mythological creature or evil spirit from the folklore of the First Nations Algonquin tribes
            "Jersey",  # Referring to the Jersey Devil of American folklore
            "Kracken",  
            "Tarrasque",
            "Chimera",
            "Basilisk",
            "Kraken",
            "Hydra",
            "Manticore",
            "Gorgon",
            "Roc",
            "Behemoth",
            "Leviathan",
            "Minotaur",
            "Cerberus",
            "Griffin",
            "Wyvern",
            "Sphinx",
            "Bunyip",
            "Cockatrice",
            "Naga",
            "Harpy",
            "Centaur",
            "Lamia",
            "Scylla",
            "Orthros",
            "Typhon",
            "Echidna",
            "Balor",
            "Jersey",
            "Mothman",
            "Wendigo",
            "Yeti",
            "Sasquatch",
            "Chupacabra",
            "Grendel",
            "Fenrir",
            "Jormungandr",
            "Skoll",
            "Hati",
            "Umberhulk",
            "Doppelganger",
            "Rustmonster",
            "Owlbear",
                        
            "Ankheg",
            "Aboleth",
            
            "Bulette",
            "Behir",

            "Cloaker",

            "Displacerbeast",

            "Gibberingmouther",
                        
            "Jabberwock",  # From "Through the Looking-Glass" by Lewis Carroll

            "Zarvox",

        ]

        Names += Monstrosity_Names

        Name = NewName(Names,onset,nuclei,codas) 
        return Name






    if npc.race == "Celestial":
        Celestials = [
            "Auriel",
            "Azarael",
            "Anael",       # In some Christian traditions, Anael is one of the seven archangels
            "Azrael",      # Often identified with the Angel of Death in Islam and some Jewish traditions
            "Alpheratz",
            "Altair",
            "Antares",
            "Arcturus",
            "Aether",   # Greek personification of the upper air, breathed by the gods
            "Astral",

            "Betelgeuse",

            "Cassiel",
            "Canopus",
            
            "Deneb",
            
            "Ethal",
            "Ethael",
            "Electra",
            "Electron",
            
            "Gabriel",
            
            "Haniel",
            
            "Israfil",
            
            "Jophiel",
            
            "Lumiel",
            
            "Metatron",
            "Maia",
            "Merope",
            
            "Raguel",
            "Raphael",
            
            "Sariel",
            "Seraphiel",
            
            "Uriel",
            
            "Zadkiel",
            "Zaphkiel",
            "Zerachiel",

            "Polaris",
            "Procyon",
            "Rigel",
            "Sirius",
            "Spica",
            "Vega",
            "Tienmu",  # Chinese god of lightning
            "Indra",    # Hindu god of thunder and king of the gods
            "Nyx",      # Greek goddess of the night
            "Eos",      # Greek goddess of the dawn
            "Hemera",   # Greek goddess of the day
            "Selene",   # Greek goddess of the moon
            "Elion",    # A name that evokes "light"
            "Caelum",   # Latin for "heaven" or "sky"
            "Celestine",
            "Etheria",
            "Galaxia",
            "Luminara",
            "Nova",
            "Orion",
            "Solara",
            "Stellaris",
            "Zenith",
            "Aeon",
            "Anahita",  # Persian goddess of fertility, water, and wisdom
            "Asteria",  # Greek titaness, name means "of the stars"
            "Astrophel",  # A name coined by the poet Sir Philip Sidney, meaning "star lover"
            "Caelestis",  # Latin term for "heavenly" or "celestial"
            "Deva",  # Sanskrit for "heavenly, divine", refers to celestial beings in Hinduism
            "Elara",  # One of Zeus' lovers in Greek mythology, and a moon of Jupiter
            "Elyon",  # A Hebrew name meaning "Most High" or "Exalted"
            "Hyperion",  # A titan in Greek mythology, associated with heavenly light
            "Izar",  # Basque name meaning "star"
            "Juno",  # Roman goddess, equivalent to the Greek Hera
            "Kalypso",  # Greek name meaning "to cover", "to conceal", "to hide", or "to deceive"
            "Levana",  # Hebrew name meaning "white", "moon", or "to rise"
            "Meissa",  # A star in the constellation Orion
            "Naharai",  # Hebrew name meaning "light" or "shiny"
            "Oriel",  # A name derived from "Aura", means light or gold
            "Pavati",  # Hindi for "clear water", also a goddess of the river
            "Quirinus",  # An early Roman god of the Roman state
            "Raziel",  # Angel in Jewish mysticism, keeper of secrets
            "Sorin",  # A name of Romanian origin, possibly derived from "Soare" meaning "sun"
            "Talitha",  # A star in the constellation Ursa Major
            "Thalassa",  # Greek sea goddess, represents the Mediterranean Sea
            "Vela",  # A constellation in the southern sky, means "sails (of a ship)"
            "Zephyr",  # The Greek god of the west wind
            "Selene",      # Greek goddess of the moon
            "Helios",      # Greek god of the sun
            "Atlas",       # A titan tasked to hold up the sky in Greek mythology
            "Aurora",      # Roman goddess of the dawn
            "Orion",       # A great hunter and a constellation in Greek mythology
            "Gaia",        # Greek personification of Earth
            "Artemis",     # Greek goddess of the hunt and moon
            "Apollo",      # Greek god of the sun, music, and prophecy
            "Hestia",      # Greek goddess of the hearth and home
            "Rhea",        # A titaness in Greek mythology, mother of the Olympian gods
            "Chronos",     # Personification of time in pre-Socratic philosophy and later literature
            "Urania",      # Greek muse of astronomy and astrology
            "Electra",     # One of the Pleiades in Greek mythology
            "Maia",        # Eldest of the Pleiades and mother of Hermes in Greek mythology
            "Perseus",     # Greek hero who slew Medusa
            "Callisto",    # A nymph, and a lover of Zeus in Greek mythology
            "Dione",       # A prophetic titaness in Greek mythology
            "Eos",         # Greek goddess of the dawn
            "Aether",      # The personification of the "upper sky", space, and heaven, in Greek mythology
            "Ananke",      # The personification of inevitability, compulsion, and necessity in Greek mythology
            "Chaos",       # The void state preceding the creation of the universe or cosmos in Greek mythology
            "Erebus",      # Personification of darkness and shadow in Greek mythology
            "Nyx",         # Greek goddess of the night
            "Tartarus",    # The deep abyss in Greek mythology, used as a dungeon of torment
            "Thalassa",    # Primeval spirit of the sea in Greek mythology
            "Pontus",      # Pre-Olympian sea god in Greek mythology
            "Ouranos",     # The personification of the sky and one of the Greek primordial deities
            "Hemera",      # The personification of day in Greek mythology
            "Nemesis",     # Greek goddess of retribution
            "Tyche",       # Greek goddess of fortune and prosperity of a city
            "Metatron",    # An archangel in Judaism and some branches of Christianity
            "Raziel",      # The keeper of secrets and the angel of mysteries in Jewish mysticism
            "Jophiel",     # An archangel of wisdom, understanding, and judgment in some traditions
            "Israfil",     # An archangel who will blow the trumpet to announce the Day of Judgment in Islam
            "Mithra",      # A divinity in Zoroastrianism and later Roman mythology, associated with the sun
            "Tien",        # The term for heaven or sky in Chinese religions and philosophy
            "Amaterasu",   # The sun goddess in Shinto religion of Japan
            "Tenshi",      # Japanese for "angel" or "celestial being"
            "Indra",       # A deity in Hinduism, king of the highest heaven called Saudharmakalpa
            "Gandharvas",  # Male nature spirits and celestial musicians in Hinduism
            "Apsaras",     # Female spirits of the clouds and waters in Hindu and Buddhist culture
            "Barong",      # A lion-like creature and character in the mythology of Bali, Indonesia
            "Kinnara",     # Celestial musicians in Hinduism, Buddhism, and Jainism
            "Tianlong",    # Celestial dragons in Chinese mythology
            "Devas",       # Godlike beings in Hinduism and Buddhism
            "Sraosha",     # An angel in Zoroastrianism who leads the soul to the afterlife
            "Valkyries",   # Female figures in Norse mythology who choose those who may die or live in battle
            "Heimdallr",   # A Norse god who possesses the resounding horn Gjallarhorn
            "Gabriel",     # An archangel in Judaism, Christianity, and Islam
            "Michael",     # An archangel in Jewish, Christian, and Islamic teachings
            "Uriel",       # An archangel in some Jewish and Christian traditions
            "Cherubim",    # A type of angelic being in the Abrahamic religions
            "Seraphim",    # The highest order of angels in Christian angelology
            "Itherael",    # A name created from the Hebrew elements for "abundance" and "God"
            "Raphael",     # An archangel responsible for healing in the traditions of most Abrahamic religions
            "Cassiel",     # An angel in post-biblical Judeo-Christian religion, particularly in the Kabbalah
            "Morpheus",  

            ]
        Names.extend(Celestials)
        Name = NewName(Names) 
        return Name


    if npc.race == "Ooze":
        oozes = [
            "Blob",
            "Flubber",
            "Gloop",
            "Squish",
            "Slurp",
            "Gelatin",
            "Dripple",
            "Slick",
            "Goober",
            "Slimey",
            "Glurt",
            "Slosh",
            "Mucus",
            "Globule",
            "Quiver",
            "Slicker",
            "Oobleck",
            "Sludge",
            "Smear",
            "Drool",
            "Jelly",
            "Puddle",
            "Gunge",
            "Splodge",
            "Muddle",
            ]
        Names += oozes
        if Dice(10)<10: 
            namer = MarkovNameGenerator(Names)
            Name = namer.generate_name()
                
            FullName =  Name 
                
        else:
            FullName =  random.choice(Names)

        return FullName


    if "Fey" in creature_type:
        fae =[
            "Titania", "Oberon", "Puck", "Robin", "Goodfellow",
            "Tinkerbell",
            "Tinker", "Bell",
            "Mab", "Ariel", "Morgana", "Niamh", "Tam", "Lin", "Rhiannon",
            "Melusine", "Gwydion", "Etain", "Bluebell", "Florian", "Lorelei",
            "Rusalka", "Alberich", "Ellette", "Fay", "Faye", "Silvanus",
            "Glaurung", "Nyx", "Pari", "Seelian", "Unseelian", "Sylph",
            "Diwata", "Maria", "Makiling", "Tala", "Mayari", "Amihan", 
            "Hanan", "Apolaki", "Anitun", "Ikapati", "Lakapati", 
            "Mapulon", "Malakas", "Maganda", "Bathala", "Kabunian", 
            "Idiyanale", "Balangaw", "Bulan", "Lidagat", "Liadlaw",
            "Baranugon", "Aman", "Sinaya", "Magwayen", "Manaul", "Aswang",
            "Tikbalang", "Kapre", "Duwende", "Sarimanok", "Manananggal",
            "Panday", "Pira", "Dalikamata", "Sidapa", "Alunsina", "Bungisngis",
            "Llorona", "Cid", "Duende", "Dorado", "Covadonga",
            "Anjana", "Trasgu", "Xana", "Lavandera", "Basilisco",
            "Nuberu", "Cuelebre", "Saco", "Busgosu", "Tarasca",
            "Culebre", "Dama", "Arintero", "Compana", "Moron",
            "Animas", "Zurragamurdi", "Silbon", "Zahori",
            "Cojuelo", "Lazarillo",     "Trasgu", "Xana", "Nuberu", "Cuélebre", "Basilisco",
            "Anjana", "Ojáncano", "Mora", "Lavandera", "Barragán",
            "Mari", "Sorgiña", "Irati", "Lamiak", "Basajaun",
            "Tartalo", "Guajona", "Culebre", "Ventolín", "Busgosu",
            "Diañu", "Burlón", "Zana", "Cegua", "Encantaria",
            "Fada", "Serena", "Galipote", "Patasola",
            "Duenderde", "Hadarina", "Ayalga", "Coruxa", "Serenagua",
            "Brujorga", "Reinoba", "Silfo", "Moura", "Pataricu", "Fatuo", "Fatua",
            "Fatue",
            ]

        Names += Fae
        Name = NewName(Names,
             onset=["Fawn", "Pan", "Sylv", "Thorn", "Elm", "Bram", "Nim", "Vern", "Glen", "Fern", "Riv", "Lark", "Row", "Taur", "Wood", "Dell", "Alder", "Briar", "Cedar", "Dusk",
                    "Aur", "Flor", "Lun", "Stell", "Vit", "Fol", "Silv", "Nym", "Cael", "Luc", "Sol", "Vent", "Ign", "Viv", "Ser", "Verd", "Faun", "Aquil", "Riv", "Temp",
                    "Cron", "Hecat", "Pyth", "Sibyl", "Druid", "Ruid",
                    "Druik","Orac", "Myst", "Nostr", "Divin", "Aeg", "Circe", "Delph", "Gorg", "Medus", "Necr", "Phant", "Sorc", "Thaum", "Trism", "Vatic",
                    "Ocul", "Ocu"
                    ],
            nuclei=[
                "a", "e", "i", "o", "u", "ae", "ea", "ie", "io", "ou", "ia", "eo", "ai", "au", "oo",
                "a", "e", "i", "o", "u", "ae", "ea", "ie", "io", "ou", "ia", "ui", "eo", "ai", "au",
                "a", "e", "i", "o", "u", "ae", "ea", "io", "oi", "ou", "ua", "ei", "eu", "ia", "ui",
                "lu",
                    ],
            codas=[
                "horn", "leaf", "wood", "song", "shade", "brook", "vale", "whisp", "stream", "grove", "thorn", "wind", "foot", "dance", "fern", "glade", "hart", "bark", "reed", "spring",
                "alis", "aris", "ella", "enna", "iana", "itus", "orix", "us", "era", "ora", "ina", "anthe", "entia", "idus", "olus", "andis", "urna", "elix", "amor", "ignis",
                "astra", "onia", "asia", "amis", "andra", "onia", "ipha", "ecia", "algia", "ella", "essa", "imna", "osia", "une", "yxis", "ompha", "anthe", "eia", "ithra", "oria",
                "lus",
                    ]) 


    if npc.race == "Dragon":
        dragons = [
            "Jakelong",
            "Braveheart"
            ]
        Names += dragons

        if Dice(10)<5:
            Name = SyllabicGenerator(
                onset = ['Ja','Brave'],
                nuclei = ['ke','heart'],
                codas = ['','long'],
                count = Dice(8)
                )
            
        elif Dice(10) < 5:
            Name = SyllabicName(
                syllables = SyllabicExtraction(Names),
                min_syllables=1,
                max_syllables=8)
                

        elif Dice(10) < 5:
            namer = MarkovNameGenerator(Names)
            Name = namer.generate_name()
                
            Name =  Name 
                
        else:
            Name =  random.choice(Names)

                                
        FullName =  Name 
        return FullName


    if npc.race == "Snakefolk":
        snakefolk = [
            "Medusa",
            "Rennesse",
            ]
        Names += snakefolk



    
    if Dice(10)<5: 
        namer = MarkovNameGenerator(Names)
        Name = namer.generate_name()
            
        FullName =  Name 
            
    else:
        FullName =  random.choice(Names)

    return FullName 


    if "Aberration" in creature_type:
        Aberrations = [
            "Uthigol",
            ]
        if Type == "Aberration":
            Names += Aberrations        
            
            if Dice(10)<4: 
                namer = MarkovNameGenerator(Names)
                Name = namer.generate_name()

                
            elif Dice(10)<4:
                Name = SyllabicGenerator(
                    onset = [
                        "Xyr", "Thar", "Ghoul", "Zor", "Krak",
                        "Nyx", "Vor", "Mord", "Quel", "Rax",
                        "Syl", "Drak", "Obl", "Vex", "Cth"
                        ],
                    nuclei = [ '','','','','','','',
                        "ae", "i", "o", "u", "a",
                        "ei", "ai", "oo", "ua", "ie",
                        "oy", "au", "eo", "io", "ya"
                        ],
                    codas = ['','','','','','','',
                        "ron", "lax", "thun", "mox", "gron",
                        "nash", "zoth", "quil", "tar", "gon",
                        "kesh", "rith", "lon", "mur", "zar"
                        ],
                    count = Dice(5)
                    )

            elif Dice(10) < 4:
                Name = SyllabicName(
                    syllables = SyllabicExtraction(Names),
                    min_syllables=1,
                    max_syllables=8)
            else:
                Name =  random.choice(Names)

                


        FullName = NewName(Names) 
        return FullName

