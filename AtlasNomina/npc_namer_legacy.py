#     "Poignant", "Proud", "Puzzled", "Quiet"]
# Performers and Artists "Actor", "Artist", "Bard", "Composer", "Dancer", "Harpist", "Jester", "Juggler", "Lyrist", "Minstrel", "Musician", "Painter", "Performer", "Poet", "Sculptor", "Singer", "Storyteller", "Troubadour"]
# Luminous and Radiant "Luminous", "Radiant", "Shining", "Sparkling", "Glowing"]
# Liquid and Fluid "Liquid", "Fluid", "Flowing", "Rippling", "Wet"]
# Time-related,  "Instantaneous", "Interim", "Momentary", "Temporal", "Timeless"]
# Emotional States,  "Lonely", "Melancholic", "Mirthful", "Mischievous",  "Pensive", "Perplexed", "Petrified", "Phlegmatic", "Piqued", "Pleased", "Plucky", "Poignant", "Proud", "Puzzled", "Quiet"]
# Performers and Artists, "Actor", "Artist", "Bard", "Composer", "Dancer", "Harpist", "Jester", "Juggler", "Lyrist", "Minstrel", "Musician", "Painter", "Performer", "Poet", "Sculptor", "Singer", "Storyteller", "Troubadour", "Blizzard", "Bloodmoon", "Boreal", "Dawnbringer",
# Mystical and Occult, "Cipher", "Clairvoyant", "Cloak", "Cobweb", "Cthulhu", "Deity", "Dimension", "Dissonance", "Dragonfire"]
# Celestial and , "Celestia", "Chrono", "Constellation", "Cosmos", "Crimson", "Darkstar"]
# Marine and Aquatic, "King's", "Coral", "Oceanic"]
# Crystals and Minerals, "Crystal",  "Quartz", "Topaz", "Xenolith"]
# Weather and  Phenomena,   "Dusk", "Eclipse", "Horizon", "Hyperion", "Iceborn"]
# Mystical and Occult, "Cipher", "Clairvoyant", "Cloak", "Cobweb", "Cthulhu", "Deity", "Dimension", "Dissonance", "Dragonfire", "Dreamweaver", "Elemental", "Elfstone", "Ember", "Ethereal", "Fable", "Fae", "Falcon", "Fenrir", "Feral", "Firebrand", "Flametongue", "Fulcrum", "Galaxy", "Gargoyle", "Gauntlet", "Ghoul", "Glitch", "Glyph", "Golem", "Grimoire", "Gryphon", "Guardianship", "Harbinger", "Hex", "Horizon", "Hydra", "Hyperion", "Iceborn", "Illusion", "Immortal", "Impulse", "Incantation", "Inferno", "Invoker", "Ion", "Iridescent", "Jester", "Juggernaut", "Kaleidoscope", "Kraken", "Leviathan", "Libra", "Lightbringer"]
# Celestial and , "Celestia", "Chrono", "Constellation", "Cosmos", "Crimson", "Darkstar", "Dimension", "Eclipse", "Galaxy", "Horizon", "Hyperion", "Star", "Stellar", "Zodiac"]
# Marine and , "Coral", "Oceanic"

def Title(npc):
    #return f"The {random.choice(descriptor)} {random.choice(rank)} {random.choice(of_the)}"

    # Adding to existing lists
    of_the_hell = []
    location_descriptor = [  "Islet", "Jungle", "Lake", "Lagoon"]
    loving_descriptor = ["Hopeful", "Jovial", "Joyful", "Jubilant"]
    hate_descriptor = ["Hostile", "Horrified", "Hungry", "Jealous", "Irate", "Irritated", "Jittery"]
    feelings_descriptor = ["Indifferent", "Inspired", "Interested", "Intrigued"]
    hell_descriptor = ["Infernal"]
    guardian_rank = ["Hunter", "Hunter's"]
    elder_descriptor = ["Homeric", "Jacobean"]
    space_descriptor = ["Ionized"]
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
    feelings_descriptor = ["Loyal", "Melancholic", "Merry", "Mindful", "Motivated", "Mournful",
                            "Optimistic", "Outraged", "Panicked", "Passionate", "Pensive", "Perceptive", "Pleased",
                            "Poetic", "Proud", "Quiet"]
    space_descriptor = ["Lunar", "Magnetic", "Magnetospheric",
                         "Meteor", "Meteoric", "Meteoritic", "Moon", "Moonlit",
                         "Nautical",
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
    elder_descriptor = ["Historic", "Homeric", "Jacobean", "Mesopotamian", "Millennial", "Myrmidonic",  "Odin's",
                         "Olympian", "Orphean", "Romanesque"]
    loving_descriptor = ["Hopeful", "Loving", "Merry", "Optimistic", "Passionate", "Proud"]
    hate_descriptor = ["Hostile", "Horrified", "Hungry", "Irate", "Irritated", "Jealous", "Jittery",
                        "Outraged", "Panicked", "Ruthless"]
    secret_descriptor = ["Hermetic", "Inscrutable", "Insidious", "Intriguing", "Intrigued", "Mysterious"]
    guardian_rank = ["Guardian", "Paladin", "Protector", "Ranger"]
    noble_rank = ["Emperor", "Governor", "King", "King's", "King of", "Kingly", "Kingdom's", "Lord", "Lordly",
                   "Lord Of the", "Lord Of", "Master", "Monarch",  "Overlord", "Queen", "Queen of", "Queen's",
                   "Regal", "Ruler", "Sovereign"]
    legal_judicial_objects = ["Gavel"]
    art_creativity_descriptor = ["Harlequin", "Harpist", "Haunting", "Poetic"]
    intellectual_thoughtful_descriptor = ["Intellect", "Inquisitive", "Intrepid", "Mindful", "Perceptive"]
    gaseous_descriptor = ["Gas", "Gaseous"]
    flora_natural_beauty = ["Garden", "Leafy", "Lush", "Mangrove", "Moss", "Muddy", "Orchid", "Palm",
                             "Pearl", "Petal", "Plum", "Pumpkin", "Purple", "Redwood", "Ribbon", "Rose",
                             "Rosy", "Ruby", "Sapphire", "Tulip"]
    wilderness_descriptor = ["Jungle", "Mangrove", "Marsh", "Marshy", "Meadow", "Moor", "Morass", "Mountain", "Mountainous", "Muddy", "Palm", "Prairie", "Savannah", "Tundra", "Wilderness"]
    mythical_legendary_descriptor = ["Legendary", "Lich", "Lion-hearted", "Lupine", "Majestic", "Manticorian", "Mighty", "Minotaur", "Minotaurine", "Miraculous", "Monstrous", "Mythical",   "Odin's", "Olympian", "Orphean", "Pegasus", "Phantom", "Phoenix", "Phoenixian", "Pirate's", "Promethean", "Protector"]
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
    elder_descriptor = [   "Elder", "Historic", "Legendary", "Mythic", "Old", "Timeless", "Venerable", "Vintage"]
    loving_descriptor = [   "Charming", "Delightful", "Dreamy", "Enchanting", "Loving", "Romantic", "Sensual", "Sentimental", "Sultry"]
    hate_descriptor = ["Baleful", "Belligerent", "Bitter", "Brutal", "Cruel", "Ferocious", "Fierce", "Fiery", "Furious", "Grim", "Harsh", "Hostile", "Malevolent", "Malign", "Menacing", "Merciless", "Ruthless", "Savage", "Sinister", "Stern", "Stormy", "Tartarean", "Terrifying", "Threatening", "Treacherous", "Turbulent", "Violent", "Villainous", "Vindictive", "Wicked", "Wrathful"]
    secret_descriptor = [ "Cryptic", "Enigmatic", "Esoteric", "Hidden", "Inscrutable", "Mysterious", "Mystical", "Occult", "Secret", "Shadowy", "Subtle", "Surreptitious", "Unseen", "Veiled"]
    guardian_rank = ["Defender", "Guardian", "Keeper", "Protector", "Sentinel", "Vigilant", "Watchman", "Warden"]
    noble_rank = [ "Baronial", "Dignified", "Eminent", "Exalted", "Grand", "Honorable", "Imperial", "Kingly", "Lordly", "Majestic",  "Regal", "Royal", "Sovereign"]
    legal_judicial_objects = ["Charter", "Code", "Decree", "Edict", "Law", "Legislation", "Mandate", "Ordinance", "Precept", "Regulation", "Rule", "Statute"]
    art_creativity_descriptor = [ "Creative", "Cultural", "Elegant", "Expressive",
                                  "Imaginative", "Innovative", "Inspiring", "Intellectual", "Literary", "Poetic",]

    color_descriptor = ["Gilded", "Golden-hearted", "Jade-eyed", "Opalescent", "Platinum"]
    nature_descriptor = ["Frost-bound", "Lone", "Moonlit", "Mystical", "Oceanic", "Polar", "Solar", "Star-born", "Star-crossed", "Stellar", "Tempest", "Thunderous", "Twilight"]
    feelings_descriptor = ["Fervent", "Fiery-eyed", "Flame-hearted", "Furious", "Harmonious", "Icy-hearted", "Imperious", "Impish", "Intense", "Jovial", "Mirthful", "Passionate", "Sanguine", "Sinister", "Sly", "Soulbound", "Sovereign", "Spellbinder", "Sphinx-like", "Spiritual", "Stealthy", "Sublime", "Supreme", "Swashbuckler", "Swift", "Swordmaster", "Timeless", "Unassailable", "Unbound", "Unconquerable", "Undaunted", "Unearthly", "Unfathomable", "Unflinching"]
    space_descriptor = ["Interstellar", "Quasar", "Stargazer", "Stellar", "Time-bender", "Titanic"]
    arcane_descriptor = ["Enchanting", "Mystical", "Oracle", "Orbiting", "Otherworldly", "Outlandish", "Pathfinder", "Phantasmal", "Profound", "Prophetic", "Prowler", "Purist", "Pyrotechnic", "Rune-carved", "Runewielder", "Sage", "Savage", "Scintillating", "Scorcher", "Seafarer", "Seer", "Sempiternal", "Shaman", "Shapeshifter", "Silent", "Sinister", "Sky-born", "Sly", "Solar", "Sorcerer", "Sovereign", "Spectral", "Spellbinder", "Sphinx-like", "Spiritual", "Star-born", "Star-crossed", "Stargazer", "Stealthy", "Stellar", "Stormbringer", "Strategist", "Sublime", "Sun-born", "Superb", "Supreme", "Swashbuckler", "Swift", "Swordmaster", "Tempest", "Thaumaturge", "Thunderous", "Time-bender", "Timeless", "Titanic", "Torchbearer", "Trailblazer", "Transcendent", "Tribal", "Trickster", "Twilight", "Tyrant", "Ubiquitous", "Unassailable", "Unbound", "Unconquerable", "Undaunted", "Unearthly", "Unfathomable", "Unflinching"]
    hell_descriptor += ["Ferocious", "Fiery", "Fierce", "Flaming", "Forceful", "Foreboding", "Furious", "Gargantuan", "Ghostly", "Grim", "Inferno", "Maleficent", "Martial", "Meteoric", "Mighty", "Monolithic", "Monstrous", "Mysterious",      "Ominous", "Outrageous", "Pandemonium", "Paradoxical", "Passionate", "Perilous", "Phantasmal", "Pillar", "Pioneering", "Pirate", "Polar", "Powerhouse", "Praetorian", "Precocious", "Predatory", "Preternatural", "Primal", "Prime", "Prismatic", "Profound", "Prophetic", "Prowler", "Pulsating", "Purist", "Pyrotechnic", "Quasar", "Questing", "Quick-witted", "Quiet", "Radiant", "Raging", "Rainmaker", "Rampant", "Ranger", "Ravaging", "Rebel", "Reckoning", "Redoubtable", "Refined", "Regal", "Relentless", "Renegade", "Resolute", "Resounding", "Revered", "Rhapsodic", "Rogue", "Rune-carved", "Runewielder", "Sage", "Sanguine", "Savage", "Scintillating", "Scorcher", "Seafarer", "Seer", "Sempiternal", "Shadow", "Shaman", "Shapeshifter", "Silent",  "Sinister", "Sky-born", "Sly", "Solar", "Sorcerer", "Soulbound", "Sovereign", "Spectral", "Spellbinder", "Sphinx-like", "Spiritual", "Star-born", "Star-crossed", "Stargazer", "Stealthy", "Stellar", "Stormbringer", "Strategist", "Sublime", "Sun-born", "Superb", "Supreme", "Swashbuckler", "Swift", "Swordmaster", "Tempest", "Thaumaturge", "Thunderous", "Time-bender", "Timeless", "Titanic", "Torchbearer", "Trailblazer", "Transcendent", "Tribal", "Trickster", "Twilight", "Tyrant", "Ubiquitous", "Unassailable", "Unbound", "Unconquerable", "Undaunted", "Unearthly", "Unfathomable", "Unflinching"]
    object_descriptor += [  "Banner", "Chalice", "Crest", "Crown", "Emblem", "Ensign", "Flag", "Goblet", "Grail", "Icon", "Idol", "Jewel", "Key", "Lantern", "Medallion", "Orb", "Pendant", "Relic", "Rod", "Scepter", "Seal", "Sigil", "Standard", "Statue", "Stone", "Sword", "Talisman", "Token", "Totem", "Vase"]
    cosmic_stellar_descriptor += [ "Celestial", "Cosmic", "Ethereal", "Galactic", "Interstellar", "Lunar", "Martian", "Mercurial", "Meteor",  "Orbital", "Planetary", "Solar", "Space", "Starry", "Sublime", "Supernatural", "Universal"]
    faith_church_heaven_religious += ["Angel", "Apostle", "Archangel", "Bishop", "Cardinal", "Chaplain", "Cleric", "Deacon", "Devout", "Disciple", "Divine", "Evangelist", "Faithful", "Friar", "Holy", "Imam", "Minister", "Missionary", "Monk", "Nun", "Pastor", "Patriarch", "Pilgrim", "Preacher", "Priest", "Prophet", "Rabbi", "Reverend", "Saint", "Savior", "Seer", "Shaman", "Shepherd", "Spiritual", "Theologian", "Vicar", "Zealot"]
    elder_descriptor += [      "Baronial", "Bygone", "Classical", "Elder", "Eternal", "Everlasting", "Historic", "Hoary", "Immortal", "Imperishable", "Infinite", "Long-standing", "Old", "Perennial", "Perpetual", "Primeval", "Primordial", "Time-honored", "Timeless", "Traditional", "Venerable", "Veteran", "Vintage"]
    loving_descriptor += [    "Caring", "Cherishing", "Compassionate", "Devoted", "Enamored", "Fond", "Gentle", "Heartfelt", "Loving", "Passionate", "Romantic", "Sentimental", "Sweet", "Tender", "Warm", "Yearning"]
    hate_descriptor += [      "Belligerent", "Bitter", "Contemptuous", "Cruel", "Cynical", "Detestable", "Disdainful", "Disgusted", "Enraged", "Fierce", "Furious", "Hateful", "Hostile", "Indignant", "Inimical", "Irate", "Irritable", "Jealous", "Loathsome", "Malevolent", "Malicious",  "Odious", "Offensive", "Opposed", "Outraged", "Peeved", "Pernicious", "Piqued", "Rancorous", "Resentful", "Spiteful", "Sullen", "Vengeful", "Vindictive", "Virulent"]
    color_descriptor += ["Gilded", "Golden-hearted", "Jade-eyed", "Opalescent", "Platinum"]
    nature_descriptor += ["Flourishing", "Frost-bound", "Meadowborn", "Moonlit",  "Oceanic", "Polar", "Solar", "Sun-born"]
    feelings_descriptor += ["Fervent", "Fiery-eyed", "Flame-hearted", "Furious", "Gallant", "Glorious", "Graceful", "Greathearted", "Harmonious", "Heartfelt", "Heroic", "Hypnotic", "Illustrious", "Imaginative", "Impassioned", "Intense", "Jovial", "Joyous", "Judicious", "Keen", "Lauded", "Majestic", "Maleficent", "Martial", "Masterful", "Maverick", "Melodic", "Meteoric", "Mighty", "Miraculous", "Mirthful", "Monolithic", "Mysterious", "Mystical", "Mythical",     "Nomadic", "Notorious", "Ominous", "Ornate", "Otherworldly", "Outlandish", "Outrageous", "Passionate", "Pathfinder", "Peerless", "Perilous", "Phantasmal", "Pillar", "Pioneering", "Predatory", "Preternatural", "Prime", "Primal", "Prismatic", "Profound", "Prophetic", "Prowler", "Purist", "Quick-witted", "Radiant", "Raging", "Rebel", "Redoubtable", "Refined", "Regal", "Relentless", "Renegade", "Resilient", "Resolute", "Resounding", "Revered", "Rogue", "Rune-carved", "Runewielder", "Sage", "Sanguine", "Savage", "Scintillating", "Seafarer", "Seer", "Sempiternal", "Shaman", "Silent", "Sinister", "Sky-born", "Sly", "Sorcerer", "Sovereign", "Spectral", "Spellbinder", "Spiritual", "Star-born", "Star-crossed", "Stargazer", "Stealthy", "Stellar", "Stormbringer", "Strategist", "Sublime", "Superb", "Supreme", "Swashbuckler", "Swift", "Swordmaster", "Tempest", "Thaumaturge", "Thunderous", "Time-bender", "Timeless", "Titanic", "Torchbearer", "Trailblazer", "Transcendent", "Trickster", "Twilight", "Tyrant", "Ubiquitous", "Unassailable", "Unbound", "Unconquerable", "Undaunted", "Unearthly", "Unfathomable", "Unflinching", "Uplifting", "Valiant", "Venerable", "Vigilant", "Visionary", "Voracious", "Warrior", "Wise", "Wraith", "Wondrous"]
    space_descriptor += ["Far-reaching", "Interstellar", "Quasar"]
    metal_descriptor += ["Ironwill", "Platinum", "Steel-hearted"]
    arcane_descriptor += ["Sorcerer's", "Spectral", "Spellbound", "Spirit", "Shamanic", "Shadowy", "Spellbound"]
    hell_descriptor += ["Inferno", "Sinister", "Tartarean", "Fiery-eyed"]
    object_descriptor += [ "Blade", "Chalice", "Crown", "Orb", "Pendant", "Relic", "Scepter", "Shield", "Staff", "Talisman", "Totem", "Vessel", "Wand", "Weapon"]
    cosmic_stellar_descriptor += ["Celestial", "Cosmic", "Galactic", "Interstellar", "Lunar", "Planetary", "Solar", "Stellar", "Supernova", "Universal"]
    faith_church_heaven_religious += [  "Biblical", "Cherubic", "Clerical", "Devotional", "Divine", "Ecclesiastical", "Elysian", "Evangelical", "Heavenly", "Hierophant", "Hieratic", "Holy", "Messianic", "Ministerial", "Monastic", "Monk", "Mystic", "Nun", "Papal", "Parish", "Pastoral", "Patriarchal", "Pietistic", "Pontifical", "Preacher", "Priest", "Priestess", "Prophet", "Rabbinical", "Reverend", "Sacred", "Sage", "Saint", "Savior", "Sectarian", "Seraphic", "Shaman", "Shepherd", "Spiritual", "Theocratic", "Theological", "Vicar", "Virtuous"]
    loving_descriptor += [  "Charming", "Compassionate", "Devoted", "Enamored", "Fond", "Gentle", "Heartfelt", "Intimate", "Kind", "Loving", "Passionate", "Romantic", "Sentimental", "Sweet", "Tender", "Warm", "Yearning"]
    hate_descriptor += [   "Belligerent", "Bitter", "Brutal", "Cruel", "Detestable", "Envious", "Fierce", "Fiery", "Furious", "Hateful", "Hostile", "Indignant", "Inimical", "Irate", "Irritable", "Jealous", "Loathsome", "Malicious", "Malignant", "Menacing",  "Odious", "Offensive", "Oppressive", "Outrageous", "Pernicious", "Pugnacious", "Rancorous", "Repugnant", "Resentful", "Ruthless", "Savage", "Spiteful", "Vengeful", "Vicious", "Vindictive", "Violent", "Virulent", "Vitriolic", "Wicked"]
    secret_descriptor += [ "Concealed", "Covert", "Cryptic", "Clandestine", "Discreet", "Elusive", "Enigmatic", "Esoteric", "Hidden", "Inscrutable", "Mysterious", "Mystic", "Occult", "Private", "Secretive", "Stealthy", "Subtle", "Surreptitious", "Undisclosed", "Unrevealed", "Veiled"]
    guardian_rank += ["Custodian", "Defender", "Guardian", "Keeper", "Protector", "Sentinel", "Vigilant", "Warden", "Watchman"]
    noble_rank += ["Aristocrat", "Baron", "Count", "Duke", "Earl", "Emperor", "King", "Knight", "Lady", "Lord", "Monarch",  "Prince", "Princess", "Queen", "Regent", "Royal", "Sovereign"]
    legal_judicial_objects += ["Charter", "Code", "Decree", "Edict", "Law", "Legislation", "Mandate", "Ordinance", "Precept", "Regulation", "Rule", "Statute"]
    art_creativity_descriptor += [ "Creative", "Cultural", "Elegant", "Expressive", "Imaginative", "Innovative", "Inspiring", "Intellectual", "Literary", "Poetic", "Refined", "Sophisticated", "Stylish"]
    intellectual_thoughtful_descriptor += [  "Brainy", "Cerebral", "Clever", "Educated", "Erudite", "Genius", "Intellectual", "Learned", "Logical", "Philosophical", "Rational", "Reasoned", "Sagacious", "Savvy", "Scholarly", "Shrewd", "Smart", "Sophisticated", "Thoughtful", "Wise"]
    gaseous_descriptor += [   "Breezy", "Ethereal", "Gaseous", "Misty", "Vaporous", "Windy"]
    color_descriptor += ["Gilded", "Golden-hearted", "Jade-eyed", "Opalescent", "Platinum"]
    nature_descriptor += ["Frost-bound", "Meadowborn", "Moonlit",  "Oceanic", "Polar", "Rainmaker", "Sky-born", "Star-born", "Sun-born", "Tempest"]
    feelings_descriptor += ["Fervent", "Fiery-eyed", "Flame-hearted", "Furious", "Gallant", "Glorious", "Greathearted", "Harmonious", "Heavenly", "Hero", "Jovial", "Judicious", "Keen", "Lauded", "Leviathan", "Lionhearted", "Majestic", "Maleficent", "Martial", "Masterful", "Maverick", "Meteoric", "Mighty", "Miraculous", "Mirthful", "Misty", "Monstrous", "Mysterious",       "Ominous", "Outlandish", "Outrageous", "Passionate", "Pathfinder", "Peacekeeper", "Peerless", "Peregrine", "Perilous", "Pillar", "Pioneering", "Pirate", "Powerhouse", "Praetorian", "Precocious", "Predatory", "Preternatural", "Primal", "Prime", "Profound", "Prophetic", "Prowler", "Pulsating", "Purist", "Pyrotechnic", "Questing", "Quick-witted", "Radiant", "Raging", "Rampant", "Ranger", "Ravaging", "Rebel", "Reckoning", "Redoubtable", "Refined", "Regal", "Relentless", "Renegade", "Resolute", "Resounding", "Revered", "Rogue", "Runewielder", "Sage", "Sanguine", "Savage", "Scintillating", "Scorcher", "Seafarer", "Seer", "Sempiternal", "Shadow", "Shaman", "Shapeshifter", "Sinister", "Sky-born", "Sly", "Solar", "Sorcerer", "Soulbound", "Sovereign", "Spectral", "Spellbinder", "Sphinx-like", "Spiritual", "Star-crossed", "Stargazer", "Stealthy", "Stellar", "Stormbringer", "Strategist", "Sublime", "Superb", "Supreme", "Swashbuckler", "Swift", "Swordmaster", "Thaumaturge", "Thunderous", "Time-bender", "Timeless", "Titanic", "Torchbearer", "Trailblazer", "Transcendent", "Tribal", "Trickster", "Twilight", "Tyrant", "Ubiquitous", "Unassailable", "Unbound", "Unconquerable", "Undaunted", "Unearthly", "Unfathomable", "Unflinching"]
    space_descriptor += ["Interstellar",   "Quasar", "Solar", "Stargazer", "Star-crossed", "Stellar"]
    metal_descriptor += ["Platinum"]
    arcane_descriptor += ["Oracle", "Orbiting", "Sorcerer", "Spectral", "Spellbinder", "Sphinx-like", "Spiritual", "Thaumaturge", "Time-bender", "Witch"]
    hell_descriptor += ["Ferocious", "Fiery-eyed", "Flame-hearted", "Flaming", "Inferno", "Maleficent", "Sinister"]
    object_descriptor += [ "Goblet", "Grail", "Orb", "Pillar", "Scepter", "Statue", "Stone", "Sword", "Thorn", "Torch"]
    cosmic_stellar_descriptor += ["Celestial", "Galactic", "Interstellar", "Lunar",   "Quasar", "Solar", "Star-crossed", "Stargazer", "Stellar", "Sublime", "Supernatural", "Supreme", "Temporal", "Timeless", "Titanic", "Transcendent", "Twilight", "Ubiquitous", "Ultimate", "Uncharted", "Unearthly", "Unfathomable", "Unforgiving", "Universal", "Unseen"]
    color_descriptor += [ "Verdant"]
    nature_descriptor += ["Verdant", "Winterborn"]
    feelings_descriptor += ["Valorous", "Venerable", "Vengeful", "Vigilant", "Vindictive", "Visionary", "Volatile", "Wicked", "Wild", "Wise", "Wrathful", "Yearning", "Zealot", "Zestful"]
    space_descriptor += [  "Interstellar", "Stellar", "Zodiac"]
    metal_descriptor += [  "Xenolith"]
    arcane_descriptor += [ "Archmage",  "Bewitched", "Warlock", "Witch", "Wizard", "Wraithlike"]
    hell_descriptor += ["Fiery", "Infernal", "Sulfuric", "Vengeful", "Wicked", "Wrathful"]
    object_descriptor += [  "Grimoire", "Orb", "Pillar", "Scepter", "Statue", "Stone", "Sword", "Talisman", "Thorn", "Torch", "Wand"]
    cosmic_stellar_descriptor += ["Celestial", "Galactic", "Interstellar", "Lunar",   "Quasar", "Solar", "Star-crossed", "Stargazer", "Stellar", "Sublime", "Supernatural", "Supreme", "Temporal", "Timeless", "Titanic", "Transcendent", "Twilight", "Ubiquitous", "Ultimate", "Uncharted", "Unearthly", "Unfathomable", "Unforgiving", "Universal", "Unseen", "Untamed"]
    faith_church_heaven_religious += ["Celestial", "Cherubic", "Divine", "Elysian", "Ethereal", "Heavenly", "Holy", "Mythical", "Sacred", "Seraphic", "Spectral", "Spiritual", "Sublime", "Supernatural", "Supreme", "Temple", "Unseen", "Valkyrie's", "Venerable", "Zenith"]
    elder_descriptor += [   "Elder", "Historic", "Legendary", "Mythic", "Old", "Timeless", "Venerable", "Vintage"]
    loving_descriptor += [ "Alluring", "Ardent", "Charming", "Delightful", "Dreamy", "Enchanting", "Loving", "Romantic", "Sensual", "Sentimental", "Sultry"]
    hate_descriptor += ["Baleful", "Belligerent", "Bitter", "Brutal", "Cruel", "Ferocious", "Fierce", "Fiery", "Furious", "Grim", "Harsh", "Hostile", "Malevolent", "Malign", "Menacing", "Merciless", "Ruthless", "Savage", "Sinister", "Stern", "Stormy", "Tartarean", "Terrifying", "Threatening", "Treacherous", "Turbulent", "Violent", "Villainous", "Vindictive", "Wicked", "Wrathful"]
    secret_descriptor += ["Arcane", "Cryptic", "Enigmatic", "Esoteric", "Hidden", "Inscrutable", "Mysterious", "Mystical", "Occult", "Secret", "Shadowy", "Subtle", "Surreptitious", "Unseen", "Veiled"]
    guardian_rank += ["Defender", "Guardian", "Keeper", "Protector", "Sentinel", "Vigilant", "Watchman", "Warden"]
    noble_rank += ["Aristocratic", "Baronial", "Dignified", "Eminent", "Exalted", "Grand", "Honorable", "Imperial", "Kingly", "Lordly", "Majestic",  "Regal", "Royal", "Sovereign"]
    legal_judicial_objects += ["Charter", "Code", "Decree", "Edict", "Law", "Legislation", "Mandate", "Ordinance", "Precept", "Regulation", "Rule", "Statute"]
    art_creativity_descriptor += ["Artistic", "Creative", "Cultural", "Elegant", "Expressive", "Imaginative", "Innovative", "Inspiring", "Intellectual", "Literary", "Poetic", "Refined", "Sophisticated", "Stylish"]
    intellectual_thoughtful_descriptor += ["Analytical", "Astute", "Brainy", "Cerebral", "Clever", "Educated", "Erudite", "Genius", "Intellectual", "Learned", "Philosophical", "Sage", "Scholarly", "Scientific", "Thoughtful", "Wise"]
    gaseous_descriptor += ["Zephyrian"]
    flora_natural_beauty += ["Flourishing", "Lush", "Luxuriant", "Verdant", "Zenith"]
    wilderness_descriptor += ["Feral", "Forested", "Jungle", "Marshy", "Meadow", "Moorish", "Mountainous", "Savannah", "Tropical", "Tundra", "Wilderness", "Woodland"]
    mythical_legendary_descriptor += ["Arcane", "Chimerical", "Dragon", "Ethereal", "Fabled", "Fairy", "Folkloric", "Legendary", "Mythic", "Mythological",   "Olympian", "Otherworldly", "Phantasmagorical", "Spectral", "Supernatural", "Unearthly"]
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
    ghost_spirit_descriptor += ["Ethereal", "Fable", "Fae", "Ghoul", "Grimoire", "Gryphon", "Harbinger", "Hex", "Hydra", "Illusion", "Incantation", "Inferno"]
    giant_large_entity_descriptor += ["Gargoyle", "Ghoul", "Golem", "Gryphon", "Juggernaut", "Kraken", "Leviathan"]


    descriptor += [
    "Lorekeeper", "Lunar", "Lycan",  "Maelstrom", "Magma", "Mandrake", "Manticore", "Marauder", "Matrix",    "Mecha", "Meld", "Merlin", "Mimic", "Mirage", "Mistwalker", "Monolith", "Moonshade",
    "Mystique", "Nebula",  "Nether",   "Nimbus",     "Nirvana", "Nova", "Oblivion", "Omen", "Onyx", "Oracle", "Orbit", "Ouroboros",
    "Pandemonium", "Paradox", "Phantasm", "Phoenix", "Pirate", "Plasma", "Portal",     "Potion", "Prowler", "Psion", "Quantum", "Quasar", "Quest", "Quicksilver",
    "Radiance", "Ragnarok", "Reaper", "Reckoner", "Redwood", "Revenant", "Rift", "Rime", "Rune", "Saga", "Sage", "Sanguine", "Savant", "Scarab", "Scion", "Serpent", "Shadow",
    "Shaman", "Siren", "Solstice", "Sorcery", "Soulfire", "Specter", "Sphinx", "Spire",     "Spirit", "Starfall", "Stormcaller", "Sunder", "Sunflare", "Supernova", "Synthesis",
    "Terra", "Thorn", "Thunder", "Timekeeper", "Titan", "Totem", "Trance", "Transcend", "Tribunal", "Twilight", "Undertow", "Universe", "Utopia","Valkyrie","Vapor","Vendetta",
    "Aegean", "Amazon's", "Amazonian", "Archipelago", "Asgardian", "Atlantean", "Aztec",     "Bay", "Beach", "Beachy", "Garden", "Gas", "Gaseous", "Gulf",
    "Gorge", "Gorgonian", "Grassland", "Graveyard", "Green", "Grove", "Guild's", "Hamlet",    "Harbor", "Heart", "Heath", "Hedgerow", "Helian", "Heliospheric", "Hill", "Hive", "Hollow",
    "Homeric", "Horned", "Hourly", "Hourglass", "Hunting", "Ice", "Icicle", "Icy",    "Ink", "Inkwell", "Inkwork", "Inn's", "Island", "Islet", "Isolated", "Jungle",
    "Keep", "Key", "Lab", "Laboratory", "Labyrinth", "Labyrinth's", "Labyrinthine", "Lagoon",     "Lake", "Lantern", "Last", "Leafy", "Legendary", "Lethal", "Library", "Lich", "Life",
    "Lightning", "Lion-hearted", "Liquid", "Lively", "Living", "Lizard", "Lonely", "Long",     "Loom", "Looming", "Lordly", "Lord Of the", "Lord Of", "Lost", "Love Of", "Loyal",
    "Luminous", "Lunar", "Lupine", "Lush", "Lustrous", "Luxurious", "Lyre", "Magic", "Magma",    "Magnetic", "Magnetospheric", "Mahogany", "Majestic", "Malignant", "Malevolent", "Mammoth",
    "Mangrove", "Mantle", "Manticorian", "Marble", "Marine", "Marketplace", "Marsh", "Marshy",     "Marvelous", "Master", "Matinal", "Mausoleum", "Maze", "Meadow", "Medallion", "Meditative",
    "Medusian", "Melancholic", "Menagerie", "Menacing", "Mental", "Mercurial", "Merry",    "Mesopotamian", "Meteor", "Meteoric", "Meteoritic", "Metropolis", "Midnight", "Mighty",
    "Militant", "Millennial", "Mindful", "Mine", "Minotaur", "Minotaurine", "Miraculous",    "Mirror", "Mirthful", "Mischievous", "Mist", "Mistral", "Misty", "Molten", "Monastic",
    "Monastery", "Monolithic", "Monstrous", "Momentary",  "Moor", "Morass",    "Moss", "Motivated", "Mountain", "Mountainous", "Mournful", "Muddy", "Mulberry", "Mummy",
    "Museum", "Mustard", "Mutant", "Myrmidonic", "Mysterious", "Mystic", "Mystical", "Mythical",    "Nautical", "Nebulous", "Nemean", "Nemesis", "Neon", "Nether", "Night", "Noble", "Nocturnal",
    "Nomadic", "Nordic", "Notorious", "Nova", "Oasis", "Observatory", "Obsidian", "Obsolete",    "Ocean", "Oceanic", "Odin's", "Olympian", "Optimistic", "Opulent", "Oracular", "Orb",
    "Orbital", "Orchard", "Orchid", "Ornate", "Orphean", "Outlandish", "Outpost", "Outraged",    "Overgrown", "Owl's", "Palace", "Palm", "Palatial", "Parched", "Parliament", "Pastoral",
    "Peaceful", "Pearlescent", "Peat", "Pebble", "Pegasus", "Penitentiary", "Perfumed",     "Perilous", "Perpetual", "Petrified", "Phantom", "Phoenix", "Pine", "Pinnacle", "Pirate's",
    "Placid", "Planetary", "Plant", "Plateau", "Platinum", "Pleasant", "Plum", "Polar",    "Ponderous", "Poppy", "Porcelain", "Portal", "Port", "Potent", "Prairie", "Precious",
    "Predator", "Primeval", "Primordial", "Prince's", "Princely", "Princess", "Prismatic",    "Prison", "Private", "Profound", "Prosperous", "Protected", "Proud", "Pumpkin", "Pungent",
    "Pure", "Purple", "Pyramid", "Quartz", "Queen's", "Quicksand", "Quiet", "Quill",    "Radiant", "Raging", "Rainbow", "Rainforest", "Rampart", "Ranger's", "Ravaged", "Raven",
    "Rebel", "Reclusive", "Red", "Regal", "Relic", "Remnant", "Remote", "Renegade", "Resplendent",    "Restless", "Revered", "Rhombus", "Rich", "Riddle", "Rift", "Righteous", "River", "Roaming",
    "Robotic", "Rock", "Rocky", "Rogue", "Rose", "Royal", "Ruby", "Rugged", "Ruined", "Runic",    "Rural", "Rustic", "Rusty", "Sacred", "Sad", "Sage", "Sapphire", "Savage", "Scarlet",
    "Scenic", "Scented", "Scholar's", "School", "Scorching", "Secluded", "Secret", "Seductive",    "Selenian", "Semi-Precious", "Serpent's", "Serpentine", "Settler's", "Shadowy", "Shady",
    "Shallow", "Shaman's", "Shattered", "Shepherd's", "Shielded", "Shimmering", "Shining",    "Shivering", "Shrine", "Sickly","Vengeance","Vertex","Vesper","Vex","Vindicator", "Virtuoso","Visage","Void","Vortex","Warden","Warlock","Warp","Watcher", "Whirlwind","Wildfire","Willow","Wisp","Witcher","Wizardry","Wraith","Wyvern", "Xenon",        "Ubiquitous"        "Ultramarine",        "Unemotional","Unhappy",        "Universal",
    "Unstoppable",        "Unyielding",        "Uranian",        "Urn",           "Ursine",       "Mantle",        "Radiant",
    "Vessel",                       "Epochal",        "Twilight",        "Primeval",        "Compass",        "Millennial",        "Meridian",        "Hammer",
        "Eternal",        "Fleeting",             "Black Hole",           "Meteoritic",            "Edwardian",            "Samurai",            "Cosmic",           "Nebulous",
        "Norman",           "Orbital",           "Han",           "Orbital",           "Gregorian",           "Renaissance",        "Spartan",           "Prohibition",
        "Crusader",         "Hellenistic",           "Sanskrit",            "Dynastic",           "Flapper",           "Napoleonic",           "Pharaonic",
        "Interstellar",            "Elizabethan",          "Feudal",           "Age",           "Cyclic",          "Timeless",         "Neutron",                "Punctual",                "Quill",                        "Bygone",        "Banner",        "Blade",        "Brooch",        "Buccaneer",
        "Byzantine",        "Bat",        "Bipedal",        "Black",        "Blending",        "Blood",        "Brass",        "Brave",        "Bursting",
        "Butterfly",        "Byzantine",                "Chiropteran",        "Crested",        "Curse",        "Cursed",        "Celestial",
        "Celtic",         "Cat",        "Celestial",        "Collector",        "Conjurer",        "Coral",        "Cosmic",        "Crimson",        "Desert",
        "Daemonian",        "Dawn",        "Draconic",        "Dimensional",        "Eldritch",        "Eclipse",        "Eagle",        "Eagle's",        "Edo",
        "Eternal",        "Extraterrestrial",          "Fountain",        "Fanged",        "Feathered",        "Feline",        "Finned",        "Fire-breathing",
        "Fuchsia",        "Feather",           "Fiery",        "Hermitage",        "Horned",                "Incan",         "Icy",        "Indigo",        "Infinite",        "Lion-hearted",        "Lion's",        "Leechy",        "Luminous",
        "Lunar",                "Medieval",         "Mammalian",        "Maned",        "Masked",        "Melancholy",        "Mermaid-tailed",
        "Mist",        "Misty",        "Minotaur's",        "Momentary",        "Moonlit",        "Mountain",        "Mysterious",
        "Nebulous",        "Necromancer",        "New",        "Nightmare",        "Noble",        "Nemean",        "Nomadic",
        "Old",        "Ophidian",        "Orange",        "Orb",        "Owl",        "Ottoman",        "Oceanic",        "Olympian",
        "Pain",        "Paladin",        "Passionate",        "Pawed",        "Pegasus-winged",        "Piscine",
        "Pirate's",        "Plague",        "Poisonous",        "Powder",        "Power",        "Punk",        "Purifying",
        "Pyramid's",        "Phalanx",        "Quasar",                "Radiant",        "Rainstorm",
        "Raptor",        "Raven",        "Red",        "River",        "River's"        "Rogue",        "Ruby",        "Rune",
        "Runer",         "Renaissance",        "River",        "Radiant",        "Rainforest",        "Ranch",        "Raspberry",        "Rat",
        "Ravine",        "Ravishing",        "Reckless",        "Reef",        "Relaxed",        "Relentless",        "Relic",           "Reptilian",
        "Resentful",        "Resilient",        "Restless",        "Reverent",        "Ridge",        "River",        "Riverine",
        "Rocky",        "Romantic",        "Rooted",        "Rose",        "Ruby",        "Ruins",        "Rust",        "Ruthless",
        "Romanesque",        "Sand",        "Scaled",        "Science",        "Second",        "Serpentine",        "Serpent's",
        "Seventh",        "Shadow",        "Shaman's",        "Shark-toothed",        "Shell-backed",        "Silver",        "Simian",
        "Skeleton",        "Smiling",        "Smoke",        "Snail-shelled",        "Solar",        "Sorcerous",        "Spark",        "Speaker",
        "Spell",        "Sphinx",        "Spined",        "Spring",        "Stars",        "Starting",        "Steam",        "Stone",
        "Storm",        "Strong",        "Summer",        "Sun Stone's",        "Sunstone",        "Silent",        "Sirenic",        "Solar",
        "Stellar",        "Stoic",        "Swift",        "Sword",        "Sphinx's ",        "Scarlet",        "Stinger",
        "Sacred",        "Sad",        "Salmon",        "Sanctuary",        "Sandy",        "Sapphire",        "Satisfied",        "Satyric",
        "Savage",        "Savanna",        "Savannah",        "Scarlet",        "School",        "Scrub",        "Sea",        "Seashore",
        "Secular",        "Seismic",        "Serene",        "Sewer",        "Seychelle",        "Shaded",        "Shadowy",        "Shore",
        "Shrine",        "Sienna",        "Sigil",        "Silent",        "Silver",        "Sirenian",        "Slate",        "Slimey",
        "Solar",        "Sorrowful",        "Sparkling",        "Spectral",        "Sprouting",        "Square",        "Stadium",        "Stalwart",
        "Starlit",        "Steadfast",        "Steamy",        "Stellar",        "Steppe",        "Stern",        "Stoic",        "Stone",
        "Strait",        "Stratospheric",        "Stream",        "Stressed",        "Studio",        "Stygian",        "Subterranean",
        "Sunlit",        "Supernova",        "Suspicious",        "Swamp",        "Swampy",        "Sword",        "Sylvan",        "Sympathetic",
        "Swift",        "Scepter",                 "Staff",        "Shield",        "Spire",        "Scroll",
        "Satellite",        "Seasonal",        "Stellar",                   "Temporal",         "Tailed",        "Tamer of",        "Tentacled",
        "Third",        "Thunder",        "Tiger",        "Tigerstrip",        "Titan",        "Tomb",        "Trival",        "True",
        "Turquoise",        "Tartarean",        "Thundering",        "Timeless",       "Titanic",        "Trojan",
        "Totem's",        "Troll's",        "Tailed",        "Talon",
        "Tangerine",        "Tapestry",        "Taupe",        "Tavern",
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
        "Zealous",
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
        "Blue",        "Boar's",
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
        "Falcon",        "Fallen",
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

    if npc.race == "Aberration":
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
            ]

        # rank for Illithid names
        rank += noble_rank + military_rank + guardian_rank + guardian_rank
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
            "Voidshaper", "Controller", "Breaker",
            "Distorter", "Existence Ravager", "Enforcer", "Void"
            ]

        of_the += of_the_space

        #return f"The {random.choice(descriptor)} {random.choice(rank)}"

        if "Illithid" in npc.subrace:
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
                "Mindlord", "Brainmaster", "Psychic Sovereign", "Elder Brain", "Void Seer",
                "Arcanist", "Lurker", "Thought Tyrant", "Cerebromancer", "Mindking",
                "Mindqueen", "Encephalarch", "Neurocaptain", "Astral Dominator", "Psychic Emissary",
                "Synapse Commander", "Tentacle", "Brainkeeper", "Mindspeaker", "Warpweaver",
                "Strider", "Cortex Conjurer", "Gloom Prophet", "Orb Master", "Deep Controller",
                "Illithid", "Mind Flayer"
                ]
        elif npc.subrace == "Illithid":
            descriptor += ["Mindbender", "Psionic", "Brainfeeder", "Thoughtstealer", "Telepathic"]
            rank += ["Mind Flayer", "Cerebral Dominator", "Brain Sovereign", "Thought Eater", "Psychic Master"]
            of_the += [
                "of the Deep Mind",
                "of the Psychic Network",
                "of the Mind Harvest",
                "of the Brain Conclave",
                "of the Mental Dominion"]


        if "Beholder" in npc.subrace:
            descriptor += [
                "Beholder",
                "All-Seeing",
                "Omniscient",
                "Paranoid",
                "Tyrannical",
                "Visionary",
                "Unblinking",]

            rank += ["Eye",
                    "Eye Tyrant",
                    "Overseer",
                    "Sphere Sovereign",
                    "Orb Lord",
                    "Watcher"]
            rank += ["Eye Tyrant", "Orb Master", "Watcher Lord", "Gaze Sovereign", "Sphere Ruler"]

            of_the += ["of the Thousand Eyes",
                       "of the All-Seeing Gaze",
                       "of the Unblinking Watch",
                       "of the Visionary Realms",
                       "of the Dark Voids",
                       "of the Unseen Terrors",
                       "of the Visionary Realms",
                       "of the Arcane Orbs"]


        if npc.subrace == "Shapeshifters":
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


        elif npc.subrace == "Old One":
            descriptor += ["Ancient", "Eldritch", "Timeless", "Mysterious", "All-Knowing"]
            rank += ["Elder Entity", "Cosmic Sage", "Star Spawn", "Void Seer", "Ancient Horror"]
            of_the += ["of the Ageless Eons", "of the Cosmic Depths", "of the Eldritch Secrets", "of the Starry Voids", "of the Ancient Mysteries"]

        elif npc.subrace == "Mindlinker":
            descriptor += ["Knowledge-Seeker", "Benevolent", "Wise", "Thought-Linker", "Mind Weaver"]
            rank += ["Thought Sage", "Mental Harmonizer", "Brain Conductor", "Psychic Connector", "Mind Ambassador"]
            of_the += ["of the Collective Consciousness", "of the Wisdom Network", "of the Harmonious Minds", "of the Thought Weave", "of the Knowledge Nexus"]

        elif npc.subrace == "Dominators":
            descriptor += ["Commanding", "Hierarchical", "Ruthless", "Subjugating", "Tyrant"]
            rank += ["Slave Master", "Hierarchy Lord", "Domination Sovereign", "Subjugator", "Rule Enforcer"]
            of_the += ["of the Iron Will", "of the Dominant Chain", "of the Enslaved Realms", "of the Ruthless Order", "of the Commanding Heights"]

        elif npc.subrace == "Living Spell":
            descriptor += ["Arcane-Wrought", "Spellbound", "Magical", "Enchanted", "Wizardly"]
            rank += ["Spell Entity", "Arcane Aberration", "Magic Devourer", "Enchantment Lord", "Wizard's Curse"]
            of_the += ["of the Spell Storms", "of the Arcane Nexus", "of the Magical Anomalies", "of the Enchanted Vortex", "of the Wizard's Binding"]

        elif npc.subrace == "Chaotic":
            descriptor += ["Unpredictable", "Erratic", "Mad", "Whimsical", "Anarchic"]
            rank += ["Chaos Bringer", "Anarchy Lord", "Mad Sovereign", "Whimsy Master", "Randomizer"]
            of_the += ["of the Chaotic Maelstrom", "of the Unpredictable Whirl", "of the Mad Realms", "of the Erratic Visions", "of the Anarchic Depths"]

        elif npc.subrace == "Star Titan":
            descriptor += ["Cosmic", "Starborn", "Astral", "Nebulous", "Galactic"]
            rank += ["Cosmic Giant", "Nebula Lord", "Star Sovereign", "Astral Colossus", "Galaxy Dominator"]
            of_the += ["of the Star Fields", "of the Galactic Cores", "of the Astral Planes", "of the Cosmic Voids", "of the Nebula Realms"]

        elif npc.subrace == "Alien Spawn":
            descriptor += ["Otherworldly", "Unearthly", "Extraterrestrial", "Alien", "Starborne"]
            rank += ["Star Fiend", "Celestial Invader", "Galactic Parasite", "Extraterrestrial Entity", "Alien Horror"]
            of_the += ["of the Distant Worlds", "of the Alien Realms", "of the Outer Cosmos", "of the Unearthly Dominions", "of the Starborne Terror"]

        elif npc.subrace == "Parasyte":
            descriptor += ["Parasitic", "Mind-Control", "Body-Snatcher", "Host-Taker", "Infesting"]
            rank += ["Mind Leech", "Body Dominator", "Neural Invader", "Host Master", "Infestation Lord"]
            of_the += ["of the Host Bodies", "of the Mind Hive", "of the Control Webs", "of the Infested Realms", "of the Parasitic Dominance"]

        elif npc.subrace == "Destiny Devouers":
            descriptor += ["Time-Traveling", "Body-Swapping", "Fate-Altering", "Chrono-Eater", "Destiny-Bender"]
            rank += ["Time Ravager", "Destiny Thief", "Chrono Predator", "Fate Usurper", "Temporal Devourer"]
            of_the += ["of the Time Streams", "of the Altered Destinies", "of the Chrono Vortex", "of the Shattered Timelines", "of the Future Eaters"]

        elif npc.subrace == "Githyanki":
            descriptor += ["Marauding", "Conquering", "Warlike", "Ruthless", "Dominant"]
            rank += ["Raid Leader", "Conqueror", "Warlord", "Supreme Commander", "Battle Master"]
            of_the += ["of the Astral Raids", "of the Conquered Realms", "of the Endless Wars", "of the Ruthless Campaigns", "of the Dominant Force"]

        elif npc.subrace == "Githzerai":
            descriptor += ["Enlightened", "Mystic", "Ascetic", "Disciplined", "Harmonious"]
            rank += ["Monk Master", "Zen Lord", "Mystic Sage", "Spiritual Guide", "Harmony Keeper"]
            of_the += ["of the Inner Peace", "of the Mystic Paths", "of the Ascetic Ways", "of the Spiritual Harmony", "of the Enlightened Realms"]

    if npc.race == "Avens":
        descriptor += [
            "Avian",
            "Feathered", "Skybound", "Winged", "Aerial", "Soaring"]
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

        if npc.subrace == "Owlin":
            descriptor += ["Nocturnal", "Wise", "Silentwing", "Moonfeathered", "Stargazer"]
            rank += ["Night Seer", "Moon Sage", "Silent Watcher", "Wisdom Keeper", "Star Whisperer"]
            of_the += ["of the Moonlit Groves", "of the Silent Forests", "of the Starry Skies", "of the Twilight Realms", "of the Owl’s Wisdom"]

    if npc.race == "Beast":
        if npc.subrace == "Armored Bear":
            descriptor += ["Mighty", "Ironclad", "Noble", "Warrior", "Stalwart"]
            rank += ["Bear King", "Armor Lord", "Battle Bruin", "Iron Guardian", "Noble Ursine"]
            of_the += ["of the Northern Realms", "of the Icy Fortresses", "of the Warrior Clans", "of the Iron Woods", "of the Stalwart Defenders"]

        if npc.subrace == "Monkey King":
            descriptor += ["Cunning", "Whimsical", "Mighty", "Trickster", "Adventurous"]
            rank += ["Monkey Monarch", "Wily Sovereign", "King", "Trickster Lord", "Journey Master"]
            of_the += ["of the Infinite Mischief", "of the Winding Paths", "of the Mystic Mountains", "of the Cloud Realms", "of the Endless Adventure"]

        if npc.subrace == "Guardian Kong":
            descriptor += ["Colossal", "Protector", "Mighty", "Fierce", "Vigilant"]
            rank += ["Kong Guardian", " Protector", "Island Lord", "Colossus Keeper", "Titan Defender"]
            of_the += ["of the Primal Isles", "of the Ancient Jungles", "of the Titan Groves", "of the Colossal Peaks", "of the Untamed Wilds"]

        if npc.subrace == "Giant Eagle":
            descriptor += ["Majestic", "Skybound", "Soaring", "Keen-Eyed", "Noble"]
            rank += ["Eagle Lord", "Sky Master", "Wing Sovereign", "Aerial Guardian", "Feathered Monarch"]
            of_the += ["of the Soaring Heights", "of the Mountain Eyries", "of the Sky Realms", "of the Wind Currents", "of the Cloud Kingdoms"]

        if npc.subrace == "Golden Lion":
            descriptor += ["Regal", "Majestic", "Golden-Maned", "Noble", "Brave"]
            rank += ["Lion King", "Golden Sovereign", "Pride Lord", "Sun Mane", "Regal Predator"]
            of_the += ["of the Sunlit Savannahs", "of the Golden Prairies", "of the Regal Realms", "of the Brave Prides", "of the Noble Roars"]

        if npc.subrace == "White Tiger":
            descriptor += ["Graceful", "Fierce", "Mystical", "Alabaster", "Stealthy"]
            rank += ["Tiger Guardian", "White Sovereign", "Silent Stalker", "Snow Predator", "Mystic Striker"]
            of_the += ["of the Snowy Peaks", "of the Silent Forests", "of the Mystic Valleys", "of the Frost Lands", "of the Stealthy Hunt"]

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

        if npc.subrace == "Celestial Stag":
            descriptor += ["Astral", "Majestic", "Otherworldly", "Luminous", "Graceful"]
            rank += ["Star Antler", "Cosmic Deer", "Astral Hart", "Luminous Sovereign", "Otherworldly Guide"]
            of_the += ["of the Starry Forests", "of the Celestial Meadows", "of the Cosmic Glades", "of the Astral Trails", "of the Luminous Realms"]

        if npc.subrace == "Fenrir Wolf":
            descriptor += ["Ferocious", "Mythic", "Boundless", "Mighty", "Primal"]
            rank += ["Wolf Titan", "Mythic Predator", "Primal Howler", "Fenrir's Kin", "Raging Lycan"]
            of_the += ["of the Ancient Legends", "of the Primal Wilds", "of the Boundless Tundra", "of the Mythic Packs", "of the Mighty Roars"]

        if npc.subrace == "Forest-God Boar":
            descriptor += ["Untamed", "Guardian", "Brave", "Sovereign", "Wild"]
            rank += ["Boar King", "Forest Protector", "Tusked Guardian", "Wild Sovereign", "Braveheart"]
            of_the += ["of the Untamed Groves", "of the Wild Thickets", "of the Ancient Forests", "of the Brave Trails", "of the Guardian Oaks"]

        if npc.subrace == "Cosmic Whale":
            descriptor += ["Stellar", "Majestic", "Cosmic", "Gentle Giant", "Starbound"]
            rank += ["Galaxy Leviathan", "Star Whale", "Cosmic Navigator", "Astral Behemoth", "Void Swimmer"]
            of_the += ["of the Starry Seas", "of the Galactic Depths", "of the Cosmic Voids", "of the Astral Currents", "of the Stellar Gales"]

        if npc.subrace == "Kaiju Dinosaur":
            descriptor += ["Colossal", "Terrifying", "Prehistoric", "Monstrous", "Primal"]
            rank += ["Titan Rex", "Kaiju Behemoth", "Primal Terror", " Overlord", "Dino Monarch"]
            of_the += ["of the Lost Worlds", "of the Ancient Ruins", "of the Primal Jungles", "of the Monstrous Lands", "of the Colossal Footprints"]

        if npc.subrace == "Kerberus Dog":
            descriptor += ["Three-Headed", "Guardian", "Infernal", "Fierce", "Loyal"]
            rank += ["Hound of Hades", "Infernal Watchdog", "Cerberus Keeper", "Three-Faced Guardian", "Hellhound Sovereign"]
            of_the += ["of the Underworld Gates", "of the Infernal Depths", "of the Guarded Realms", "of the Threefold Paths", "of the Fierce Loyalty"]

        if npc.subrace == "Sun Scarab":
            descriptor += ["Solar", "Ancient", "Resilient", "Radiant", "Sacred"]
            rank += ["Scarab Pharaoh", "Solar Beetle", "Eternal Guardian", "Radiant Crawler", "Sun Worshipper"]
            of_the += ["of the Sunlit Sands", "of the Ancient Temples", "of the Resilient Dunes", "of the Radiant Tombs", "of the Sacred Sunrays"]

        if npc.subrace == "Moon Jackal":
            descriptor += ["Nocturnal", "Mystical", "Lunar", "Sleek", "Wily"]
            rank += ["Moon Guardian", "Lunar Predator", "Night Prowler", "Mystic Howler", " Sage"]
            of_the += ["of the Moonlit Plains", "of the Lunar Mysteries", "of the Night Hunts", "of the Starry Eyed", "of the Wily Spirits"]

        if npc.subrace == "Spider Queen":
            descriptor += ["Weaver", "Silken", "Deadly", "Arachnid", "Matriarch"]
            rank += ["Web Mistress", "Silk Sovereign", "Venom Lord", "Arachnid Matron", "Spinner of Fates"]
            of_the += ["of the Webbed Realms", "of the Silken Threads", "of the Deadly Traps", "of the Arachnid Dominions", "of the Hidden Lairs"]

        if npc.subrace == "World Serpent's Spawn":
            descriptor += ["Ancient", "Mythic", "Cosmic", "Endless", "Primordial"]
            rank += ["Serpent Progeny", "Cosmic Coiler", "Mythic Python", "Galactic Viper", "Eternal Slitherer"]
            of_the += ["of the World's Roots", "of the Cosmic Scales", "of the Mythic Depths", "of the Endless Coils", "of the Primordial Seas"]

        if npc.subrace == "Elder Elephant":
            descriptor += ["Sage", "Majestic", "Ancient", "Wise", "Gentle Giant"]
            rank += ["Elder Matriarch", "Tusker Sage", "Memory Keeper", "Gentle Titan", "Ancient One"]
            of_the += ["of the Ageless Herds", "of the Sacred Plains", "of the Ancient Wisdom", "of the Gentle Lands", "of the Majestic Paths"]

    if npc.race == "Beastfolk":
        descriptor += ["Feral", "Wild", "Naturebound", "Primal", "Beastly"]
        rank += ["Tribe Leader", "Nature Guardian", "Primal Warrior", "Wild Seeker", "Beast Master"]
        of_the += ["of the Untamed Wilds", "of the Primal Forests", "of the Ancient Tribes", "of the Nature's Heart", "of the Beast Realms"]

        if npc.subrace == "Arachnidfolk":
            descriptor += ["Weaver", "Silken", "Eight-Legged", "Trickster", "Fate Spinner"]
            rank += ["Web Master", "Silk Weaver", "Venom Lord", "Spinner of Lies", "Arachnid Sage"]
            of_the += ["of the Webbed Dominions", "of the Silken Threads", "of the Poisoned Fangs", "of the Trickster's Web", "of the Fateful Strands"]

        if npc.subrace == "Catfolk":
            descriptor += ["Agile", "Whiskered", "Feline", "Stealthy", "Mystical"]
            rank += ["Prowler Lord", "Feline Seer", "Claw Master", "Whisker Sage", "Shadow Hunter"]
            of_the += ["of the Silent Paws", "of the Moonlit Paths", "of the Agile Hunters", "of the Mystic Whiskers", "of the Feline Grace"]

        if npc.subrace == "Centaur":
            descriptor += ["Hooved", "Wildheart", "Nature's Rider", "Forest Runner", "Half-Horse"]
            rank += ["Herd Leader", "Forest Guardian", "Wild Archer", "Hoofed Sage", "Pathfinder"]
            of_the += ["of the Open Plains", "of the Ancient Forests", "of the Running Rivers", "of the Wild Trails", "of the Hooved Tribes"]

        if npc.subrace == "Gnoll":
            descriptor += ["Savage", "Hyena", "Hungry", "Ravenous", "Fierce", "Chaotic"]
            rank += ["Pack Alpha", "Hyena Warlord", "Ravager", "Bone Gnawer", "Chaos Bringer"]
            of_the += ["of the Wastelands", "of the Laughing Packs", "of the Ravaged Lands", "of the Fierce Clans", "of the Chaotic Wilderness"]

        if npc.subrace == "Insectfolk":
            descriptor += ["Hive-Minded", "Chitinous", "Six-Legged", "Buzzing", "Versatile"]
            rank += ["Hive King", "Colony Master", "Swarm Leader", "Bug Sage", "Nest Protector"]
            of_the += ["of the Great Hives", "of the Buzzing Swarms", "of the Chitinous Carapaces", "of the Insect Colonies", "of the Versatile Kin"]

        if npc.subrace == "Jackalmen":
            descriptor += ["Canine", "Desert-Born", "Cunning", "Ancestral", "Afterlife Guardian"]
            rank += ["Lord", "Desert Prowler", "Canine Seer", "Anubis Kin", "Sandspeaker"]
            of_the += ["of the Ancient Tombs", "of the Desert Winds", "of the Canine Packs", "of the Ancestral Spirits", "of the Sand Dunes"]

        if npc.subrace == "Lycan":
            descriptor += ["Werebeast", "Moon-Caller", "Shapeshifter", "Feral", "Cursed"]
            rank += ["Lycan Alpha", "Moon Howler", "Beast Shifter", "Feral Lord", "Cursed Wanderer"]
            of_the += ["of the Moonlit Curse", "of the Shifting Forms", "of the Feral Packs", "of the Ancient Lycanthropy", "of the Wild Hunt"]

        if npc.subrace == "Leonid":
            descriptor += ["Maned", "Regal", "Sun-Kissed", "Proud", "Roaring"]
            rank += ["Lion King", "Pride Lord", "Mane Guardian", "Sun Sovereign", "Roaring Leader"]
            of_the += ["of the Golden Savannas", "of the Pride Lands", "of the Sunlit Realms", "of the Roaring Clans", "of the Majestic Roars"]

        if npc.subrace == "Merfolk":
            descriptor += ["Aquatic", "Siren", "Ocean", "Mystical", "Deep Sea"]
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
            rank += ["Form Changer", "Mystic Walker", "Spirit Shifter", "Shape Sovereign", "Phantom Stalker"]
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

    if npc.subrace == "Kitsune":
        descriptor += ["Foxy", "Enchanting", "Nine-Tailed", "Trickster", "Mystical"]
        rank += ["Fox Spirit", "Mystic Vixen", "Enchanter", "Illusion Weaver", "Tale Spinner"]
        of_the += ["of the Enchanted Woods", "of the Illusory Realms", "of the Mystic Tails", "of the Trickster's Den", "of the Foxfire Glades"]


    if npc.subrace == "Kitsune":
        descriptor += ["Cunning", "Enchanting", "Mystical", "Trickster", "Nine-Tailed"]
        rank += ["Fox Spirit", "Enchanter", "Mystic Trickster", "Illusion Weaver", "Tale Spinner"]
        of_the += ["of the Enchanted Woods", "of the Illusory Realms", "of the Mystic Tails", "of the Trickster's Den", "of the Foxfire Glades"]

    if npc.race == "Celestial":
        descriptor += ["Radiant", "Divine", "Heavenly", "Ethereal", "Sublime"]
        rank += ["Sky Herald", "Divine Messenger", "Celestial Guardian", "Ethereal Guide", "Heavenly Emissary"]
        of_the += ["of the Celestial Spheres", "of the Divine Realms", "of the Heavenly Host", "of the Ethereal Light", "of the Sublime Vistas"]

        if npc.subrace == "Angelic Bloodline":
            descriptor += ["Blessed", "Celestial", "Radiantborn", "Sacred", "Divine-Touched"]
            rank += ["Radiant Scion", "Blessed Heir", "Sacred Offspring", "Celestial Descendant", "Divine Progeny"]
            of_the += ["of the Blessed Lineage", "of the Radiant Ancestors", "of the Sacred Blood", "of the Divine Heritage", "of the Ethereal Descent"]

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

        if npc.subrace == "Couatl":
            descriptor += ["Feathered", "Guardian", "Serpentine", "Mystic", "Vibrant"]
            rank += ["Feathered Protector", "Serpent Guardian", "Mystic Coil", "Vibrant Spirit", "Sky Serpent"]
            of_the += ["of the Feathered Wings", "of the Mystic Visions", "of the Serpentine Grace", "of the Vibrant Scales", "of the Guardian Skies"]

        if npc.subrace == "Forgotten God":
            descriptor += ["Lost", "Ancient", "Forgotten", "Fallen", "Mythic"]
            rank += ["Forgotten Deity", "Lost Divinity", "Ancient Spirit", "Mythic Echo", "Once-Mighty Being"]
            of_the += ["of the Lost Temples", "of the Forgotten Realms", "of the Ancient Faiths", "of the Mythic Memories", "of the Vanished Worship"]

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
            descriptor += ["Mighty", "Warrior", "Divine", "Radiant", ]
            rank += ["Celestial Warrior", "Divine Champion", "Radiant Protector", "Just Arbiter", "Mighty Enforcer"]
            of_the += ["of the Celestial Armies", "of the Divine Crusade", "of the Radiant Order", "of the Just Cause", "of the Mighty Skies"]

        if npc.subrace == "Seraph":
            descriptor += ["Burning", "Highest", "Holy", "Radiant", "Six-Winged"]
            rank += ["Seraphim Guardian", "Flame of God", "Radiant Angel", "Holy Protector", "Divine Watcher"]
            of_the += ["of the Blazing Choirs", "of the Highest Heavens", "of the Holy Fires", "of the Radiant Spheres", "of the Divine Purity"]

        if npc.subrace == "Throne":
            descriptor += [ "Imposing", "Celestial", "Majestic", "Orderly"]
            rank += ["Throne Arbiter", "Celestial Judge", "Divine Ruler", "Order Keeper", " Bearer"]
            of_the += ["of the Celestial Courts", "of the Divine Order", "of the Judicious Spheres", "of the Majestic Rule", "of the Orderly Heavens"]

        if npc.subrace == "Unicorn":
            descriptor += ["Pure", "Mystical", "Enchanted", "Healing", "Gentle"]
            rank += ["Unicorn Guardian", "Mystic Steed", "Enchanted Being", "Healer of Forests", "Gentle Protector"]
            of_the += ["of the Enchanted Woods", "of the Healing Streams", "of the Mystic Glades", "of the Pure Hearts", "of the Gentle Wilds"]

        if npc.subrace == "Celestial Serpent":
            descriptor += ["Dragonlike", "Stellar", "Majestic", "Cosmic", "Heavenly"]
            rank += ["Stardrake", "Celestial Dragon", "Sky Serpent", "Majestic Coiler", "Heavenly Guardian"]
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
            descriptor += [ "Lawful", "Heavenly", "Noble", "Guardian"]
            rank += ["Archon Judge", "Celestial Lawkeeper", "Heavenly Protector", "Noble Arbiter", "Guardian of Order"]
            of_the += ["of the Lawful Heavens", "of the Celestial Courts", "of the Just Order", "of the Noble Realms", "of the Heavenly Scales"]

        if npc.subrace == "Solar":
            descriptor += ["Exalted", "Powerful", "Heavenly", "Radiant", "Divine"]
            rank += ["Celestial Commander", "Divine Warrior", "Exalted Protector", "Radiant Emissary", "Heavenly Arbiter"]
            of_the += ["of the Highest Order", "of the Divine Armies", "of the Radiant Host", "of the Exalted Heavens", "of the Celestial Might"]

    if npc.race == "Construct":
        descriptor += ["Artificial", "Crafted", "Mechanized", "Sentient", "Constructed"]
        rank += ["Animated Being", "Mechanical Guardian", "Crafted Sentinel", "Sentient Machine", "Artificial Entity"]
        of_the += ["of the Crafted Realms", "of the Mechanized Worlds", "of the Artisan's Design", "of the Sentient Constructs", "of the Automated Legions"]

        if npc.subrace == "Animated Armor":
            descriptor += ["Guardian", "Steelbound", "Empty Helm", "Armored", "Vigilant"]
            rank += ["Steel Sentinel", "Guardian Armor", "Helm Watcher", "Knight Protector", "Armored Guardian"]
            of_the += ["of the Ancient Halls", "of the Silent Watch", "of the Armored Guardians", "of the Forgotten Armory", "of the Eternal Vigil"]

        if npc.subrace == "Drone":
            descriptor += ["Aerial", "Scouting", "Unmanned", "Surveillance", "Mechanical"]
            rank += ["Sky Eye", "Recon Unit", "Aerial Scout", "Observation Sentinel", "Surveillance Machine"]
            of_the += ["of the Soaring Heights", "of the Scouting Skies", "of the Unseen Watchers", "of the Mechanical Wings", "of the Surveillance Network"]

        if npc.subrace == "Golem":
            descriptor += ["Stony", "Earthen", "Mighty", "Constructed", "Elemental"]
            rank += ["Stone Keeper", "Earthen Warrior", "Clay Sentinel", "Golem Guardian", "Elemental Construct"]
            of_the += ["of the Ancient Earth", "of the Stony Bastions", "of the Earthen Cores", "of the Constructed Might", "of the Elemental Form"]

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
            descriptor += ["Literate", "Scholarly", "Guardian", "Inscribed", "Wise"]
            rank += ["Book Keeper", "Scholarly Protector", "Tome Sentinel", "Scripted Guardian", "Wise Custodian"]
            of_the += ["of the Ancient Libraries", "of the Scholarly Archives", "of the Inscribed Wisdom", "of the Guardian Scrolls", "of the Learned Repositories"]

        if npc.subrace == "Effigy":
            descriptor += ["Ritualistic", "Statuesque", "Symbolic", "Mystical", "Ethereal"]
            rank += ["Angel", "Ritual Guardian", "Statue Warden", "Symbolic Protector", "Mystic Effigy", "Ethereal Sentinel"]
            of_the += ["of the Ritual Circles", "of the Statuesque Realms", "of the Symbolic Grounds", "of the Mystic Rites", "of the Ethereal Forms"]

    if npc.race == "Dragon":
        descriptor += ["Majestic", "Ancient", "Scales", "Winged", "Fire-Breathing"]
        rank += ["Dragon Sovereign", "Winged Ruler", "Flame Keeper", "Sky Dominator", "Eternal Drake"]
        of_the += ["of the Ancient Roosts", "of the Sky Realms", "of the Fire Peaks", "of the Winged Dominions", "of the Scaled Kin"]

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
        if "Green" in npc.subrace:
            descriptor += ["Poisonous", "Verdant", "Deceptive", "Forest Dweller", "Toxic"]
            rank += ["Poison Master", "Verdant Guardian", "Deceptive Wyrm", "Forest Sovereign", "Toxic Overlord"]
            of_the += ["of the Poisoned Woods", "of the Verdant Jungles", "of the Deceptive Groves", "of the Toxic Thickets", "of the Forest Dominions"]
        if "Red" in npc.subrace:
            descriptor += ["Fiery", "Infernal", "Terrifying", "Mountain King", "Flame-Breather"]
            rank += ["Fire Lord", "Infernal Tyrant", "Red Sovereign", "Mountain Ruler", "Blaze Master"]
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
        if "Gold" in npc.subrace:
            descriptor += ["Regal", "Fire-Wielder", "Weakening", "Gold-Scaled", "Venerable"]
            rank += ["Gold Sovereign", "Regal Protector", "Fire Master", "Weakening Drake", "Venerable Wyrm"]
            of_the += ["of the Golden Hoards", "of the Fire Peaks", "of the Regal Thrones", "of the Weakening Flames", "of the Venerable Realms"]
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
        if "Ethereal" in npc.subrace:
            descriptor += ["Ethereal", "Ghostly", "Astral", "Translucent", "Otherworldly"]
            rank += ["Astral Drake", "Ghostly Guardian", "Ethereal Sovereign", "Translucent Wyrm", "Otherworldly Serpent"]
            of_the += ["of the Ethereal Planes", "of the Astral Realms", "of the Ghostly Veils", "of the Translucent Worlds", "of the Otherworldly Spheres"]
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
        descriptor += ["Primal", "Elemental", "Natural", "Force", "Ethereal"]
        rank += ["Elemental Guardian", "Primal Force", "Natural Spirit", "Ethereal Warden", "Force of Nature"]
        of_the += ["of the Primal Elements", "of the Ethereal Realms", "of the Natural World", "of the Elemental Forces", "of the Primal Essence"]

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
            descriptor += ["Dawnbringer", "Luminous", "Sunrise", "Solar", "Daylight"]
            rank += ["Sunrise Sovereign", "Luminous Guardian", "Dawn Herald", "Solar Emissary", "Daylight Keeper"]
            of_the += ["of the First Light", "of the Rising Sun", "of the Morning Rays", "of the Solar Brilliance", "of the Luminous Horizons"]

        # Genasi
        if "Genasi" in npc.subrace:
            descriptor += ["Elementalborn", "Primal", "Versatile", "Mystical", "Nature's Child"]
            rank += ["Primal Force", "Elemental Sage", "Nature's Herald", "Mystic Shaper", "Versatile Guardian"]
            of_the += ["of the Four Elements", "of the Mystical Forces", "of the Primal Essence", "of the Nature's Wonders", "of the Elemental Realms"]

        # Genie
        if "Genie" in npc.subrace:
            descriptor += ["Primordial", "Mystical", "Powerful", "Enigmatic", "Wishmaker"]
            rank += ["Genie Lord", "Primordial Spirit", "Mystical Sovereign", "Enigmatic Master", "Wish Granter"]
            of_the += ["of the Ancient Wishes", "of the Mystic Realms", "of the Primordial Sands", "of the Enigmatic Powers", "of the Wishful Dominions"]

        # Gaians
        if "Gaians" in npc.subrace:
            descriptor += ["Earthen", "Stoneheart", "Terran", "Nature's Essence", "Grounded"]
            rank += ["Earth Sage", "Stoneheart Guardian", "Terran Protector", "Nature's Essence", "Grounded Ruler"]
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
        if "Promethean" in npc.subrace:
            descriptor += ["Innovative", "Fiery", "Energetic", "Dynamic", "Electrifying"]
            rank += ["Fire Innovator", "Dynamic Creator", "Energetic Shaper", "Electrifying Spirit", "Promethean Guardian"]
            of_the += ["of the Innovative Fires", "of the Dynamic Energies", "of the Electrifying Storms", "of the Fiery Inventions", "of the Energetic Realms"]

        # Salamandrian
        if "Salamandrian" in npc.subrace:
            descriptor += ["Flameborn", "Blazing", "Inferno", "Ember", "Fire-Souled"]
            rank += ["Inferno Guardian", "Blazing Spirit", "Flame Master", "Ember Warden", "Fire-Souled Protector"]
            of_the += ["of the Blazing Fires", "of the Inferno Realms", "of the Ember Lands", "of the Flame Heart", "of the Fireborne Essence"]

        # Titan
        if "Titan" in npc.subrace:
            descriptor += ["Colossal", "Powerful", "Elemental Giant", "Mighty", "Unyielding"]
            rank += ["Colossus", "Elemental Behemoth", "Mighty Titan", "Powerful Sovereign", "Unyielding Force"]
            of_the += ["of the Colossal Strength", "of the Elemental Might", "of the Mighty Peaks", "of the Power Unleashed", "of the Unyielding Earth"]

        # Uranians
        if "Uranians" in npc.subrace:
            descriptor += ["Stellar", "Celestial", "Skybound", "Astral", "Starlight"]
            rank += ["Celestial Wanderer", "Stellar Guardian", "Sky Sovereign", "Astral Keeper", "Starlight Emissary"]
            of_the += ["of the Starry Heavens", "of the Celestial Orbs", "of the Astral Realms", "of the Skybound Dominions", "of the Stellar Depths"]

        # Magmaforged
        if "Magmaforged" in npc.subrace:
            descriptor += ["Lava", "Volcanic", "Igneous", "Molten", "Fiery Earth"]
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
        if "Chronian" in npc.subrace:
            descriptor += ["Timeless", "Chronal", "Temporal", "Eon", "Hourglass"]
            rank += ["Time Keeper", "Chronal Warden", "Temporal Guardian", "Eon Master", "Hourglass Sentinel"]
            of_the += ["of the Time Streams", "of the Chronal Rifts", "of the Temporal Vortex", "of the Eon Depths", "of the Hourglass Sands"]

        # Tundran
        if "Tundran" in npc.subrace:
            descriptor += ["Icy", "Frozen", "Glacial", "Arctic", "Snowbound"]
            rank += ["Glacial Master", "Frozen Sovereign", "Icy Protector", "Arctic Force", "Snowbound Guardian"]
            of_the += ["of the Frozen Wastes", "of the Glacial Peaks", "of the Icy Realms", "of the Arctic Expanse", "of the Snowbound Lands"]

    # Fiend Race and Subraces
    if "Fiend" in npc.race:
        # General Fiend descriptor, rank, and Of_the Phrases
        descriptor += ["Infernal", "Diabolical", "Sinister", "Malevolent", "Demonic"]
        rank += ["Hell Lord", "Demon Prince", "Fiendish Sovereign", "Infernal Commander", "Dark Deceiver"]
        of_the += ["of the Infernal Realms", "of the Abyssal Depths", "of the Sinister Schemes", "of the Malevolent Plans", "of the Demonic Hordes"]

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

        if "Cubus" in npc.subrace:
            descriptor += ["Seductive", "Charming", "Enchanting", "Tempting", "Deceptive"]
            rank += ["Seducer", "Charming Fiend", "Enchanting Spirit", "Temptress", "Deceptive Charmer"]
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
        if "Rakshasa" in npc.subrace:
            descriptor += ["Deceptive", "Cunning", "Malevolent", "Illusionist", "Manipulative"]
            rank += ["Deceptive Master", "Cunning Fiend", "Malevolent Deceiver", "Illusionist Trickster", "Manipulative Demon"]
            of_the += ["of the Deceptive Guises", "of the Cunning Illusions", "of the Malevolent Schemes", "of the Illusionist Arts", "of the Manipulative Ploys"]

        # Fallen Angel
        if "Fallen Angel" in npc.subrace:
            descriptor += ["Fallen", "Darkened", "Lost", "Banished", "Corrupted"]
            rank += ["Fallen Seraph", "Darkened Messenger", "Lost Cherub", "Banished Guardian", "Corrupted Emissary"]
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
        if "Infernal Finder" in npc.subrace:
            descriptor += ["Seeker", "Infernal", "Unrelenting", "Determined", "Tracker"]
            rank += ["Hell's Seeker", "Infernal Tracker", "Unrelenting Finder", "Determined Pursuer", "Hellbound Locator"]
            of_the += ["of the Lost Treasures", "of the Infernal Quests", "of the Unrelenting Searches", "of the Determined Hunts", "of the Hell's Tracks"]

        # Sin Investigator
        if "Sin Investigator" in npc.subrace:
            descriptor += ["Infernal", "Insightful", "Detective", "Analytical"]
            rank += ["Sin Examiner", "Infernal Investigator", " Sleuth", "Detective of Deceit", "Analytical Inquirer"]
            of_the += ["of the Sinful Mysteries", "of the Infernal Truths", "of the Judicial Inquiries", "of the Deceptive Trails", "of the Analytical Pursuits"]

        # Infernal Warlord
        if "Infernal Warlord" in npc.subrace:
            descriptor += ["Warlike", "Commanding", "Infernal", "Tyrannical", "Conqueror"]
            rank += ["Infernal Commander", "Hellish General", "Warlord of the Damned", "Tyrannical Leader", "Conquering Fiend"]
            of_the += ["of the Infernal Legions", "of the Hellish Battlegrounds", "of the Conquered Realms", "of the Tyrannical Rule", "of the Damned Armies"]

        # Infernal Justiciar
        if "Infernal Justiciar" in npc.subrace:
            descriptor += [ "Righteous", "Infernal", "Lawbringer", "Stern"]
            rank += ["Infernal Judge", "Hellish Arbiter", " of Flames", "Righteous Punisher", "Stern Enforcer"]
            of_the += ["of the Infernal Courts", "of the Righteous Judgments", "of the Hellish Law", "of the Stern Rule", "of the Punishing Flames"]

        # Vengeance Spirit
        if "Vengeance Spirit" in npc.subrace:
            descriptor += ["Vengeful", "Spectral", "Retributive", "Unforgiving", "Phantom"]
            rank += ["Spirit of Revenge", "Spectral Avenger", "Retributive Ghost", "Unforgiving Shade", "Phantom of Vengeance"]
            of_the += ["of the Vengeful Shadows", "of the Spectral Wrath", "of the Retributive Haunts", "of the Unforgiving Night", "of the Phantom Grudges"]

        # Retributioner
        if "Retributioner" in npc.subrace:
            descriptor += ["Retaliatory",  "Unyielding",  "Inexorable"]
            rank += ["Retaliatory Force", "Unyielding Judge", " Avenger", "Inexorable Punisher", "Executioner"]
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


    if npc.race == "Fiend":
        # descriptor for Fiend names
        descriptor += [
            "Infernal", "Diabolical", "Hellish", "Sinister", "Maleficent",
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
    if "Fey" in npc.race:
        # General Fey descriptor, rank, and Of_the Phrases
        descriptor += ["Enchanted", "Mystical", "Otherworldly", "Charming", "Ethereal"]
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
            descriptor += ["Bloodthirsty", "Malevolent", "Sinister", "Ruthless", "Ferocious"]
            rank += ["Blood Cap", "Malevolent Gnome", "Sinister Fiend", "Ruthless Killer", "Ferocious Goblin"]
            of_the += ["of the Bloodied Stones", "of the Malevolent Woods", "of the Sinister Paths", "of the Ruthless Hunts", "of the Ferocious Raids"]

        # Banshee
        if "Banshee" in npc.subrace:
            descriptor += ["Wailing", "Ethereal", "Deathly", "Mournful", "Ghostly"]
            rank += ["Wailing Spirit", "Ethereal Mourner", "Deathly Herald", "Mournful Phantom", "Ghostly Screamer"]
            of_the += ["of the Wailing Moors", "of the Ethereal Laments", "of the Deathly Visions", "of the Mournful Echoes", "of the Ghostly Realms"]

        # Leprechaun
        if "Leprechaun" in npc.subrace:
            descriptor += ["Tricky", "Gold-Loving", "Mischievous", "Wee", "Cunning"]
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
            descriptor += ["Destiny", "Mystic", "Fateful", "Enigmatic", "Influential"]
            rank += ["Destiny Weaver", "Mystic Fate", "Fateful Guide", "Enigmatic Oracle", "Influential Seer"]
            of_the += ["of the Mystic Destinies", "of the Fateful Encounters", "of the Enigmatic Futures", "of the Influential Visions", "of the Destiny's Path"]

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
        if "Jotunn (Frost Giant)" in npc.subrace:
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
            descriptor += [ "Demonlike", "Terrifying", "Ogre", "Menacing"]
            rank += ["Oni Warlord", "Demonlike Ogre", "Terrifying Giant", "Fiend", "Menacing Brute"]
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
    if "Gnome" in npc.race:
        # General Gnome descriptor, rank, and Of_the Phrases
        descriptor += ["Inventive", "Curious", "Small", "Whimsical", "Clever"]
        rank += ["Master Tinker", "Inventor", "Whimsical Sage", "Curious Explorer", "Clever Artisan"]
        of_the += ["of the Hidden Workshops", "of the Whimsical Gardens", "of the Curious Expeditions", "of the Clever Creations", "of the Small Wonders"]

        # Mountain
        if "Mountain" in npc.subrace:
            descriptor += ["Sturdy", "Mountainous", "Rocky", "Adventurous", "Rugged"]
            rank += ["Mountain Artisan", "Sturdy Explorer", "Rocky Sage", "Adventurous Creator", "Rugged Inventor"]
            of_the += ["of the Mountain Peaks", "of the Sturdy Cliffs", "of the Rocky Caverns", "of the Adventurous Trails", "of the Rugged Landscapes"]

        # Forest
        if "Forest" in npc.subrace:
            descriptor += ["Woodland", "Nature-Loving", "Green", "Sylvan", "Earthy"]
            rank += ["Forest Wanderer", "Nature Tinker", "Green Artisan", "Sylvan Creator", "Earthy Innovator"]
            of_the += ["of the Woodland Glens", "of the Nature-Crafted Items", "of the Green Canopies", "of the Sylvan Groves", "of the Earthy Dwellings"]

        # Garden
        if "Garden" in npc.subrace:
            descriptor += ["Botanical", "Floral", "Green-Thumb", "Gardener", "Blossoming"]
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
            descriptor += ["Nomadic", "Roaming", "Adventurous", "Wandering", "Explorative"]
            rank += ["Roaming Artisan", "Nomadic Tinker", "Adventurous Creator", "Wandering Inventor", "Explorative Pioneer"]
            of_the += ["of the Roaming Tribes", "of the Nomadic Journeys", "of the Adventurous Expeditions", "of the Wandering Spirits", "of the Explorative Paths"]

    # Goblin Kind Race and Subraces
    if "Goblin" in npc.race:
        # General Goblin descriptor, rank, and Of_the Phrases
        descriptor += ["Sneaky", "Green-Skinned", "Goblin's", "Crafty", "Cunning",]
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
            descriptor += ["Bloodthirsty", "Murderous", "Menacing", "Crimson-Capped", "Fierce"]
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
    if "Monstrosity" in npc.race:
        # General Monstrosity descriptor, rank, and Of_the Phrases
        descriptor += ["Terrifying", "Monstrous", "Fearsome", "Beastly", "Mythical"]
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
            descriptor += ["Illusive", "Feline", "Deadly", "Shift", "Evasive"]
            rank += ["Illusive Predator", "Deadly Phantom", "Feline Menace", "Shift Beast", "Evasive Hunter"]
            of_the += ["of the Ethereal Hunt", "of the Deadly Shadows", "of the Illusive Stalk", "of the Feline Deception", "of the Evasive Tactics"]

        # Doppelganger
        if "Doppelganger" in npc.subrace:
            descriptor += ["Shape-shifting", "Deceptive", "Mimic", "Duplicitous", "Eerie"]
            rank += ["Master of Disguise", "Deceptive Mimic", "Shape-Shifter", "Duplicitous Phantom", "Eerie Imposter"]
            of_the += ["of the Deceptive Forms", "of the Mimicked Faces", "of the Shape-Shifting Mystery", "of the Duplicitous Shadows", "of the Eerie Doubles"]

        # Gorgon
        if "Gorgon" in npc.subrace:
            descriptor += ["Stone-Gazing", "Serpentine", "Terrifying", "Mythical", "Cursed"]
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
        if "Sphynx" in npc.subrace:
            descriptor += ["Enigmatic", "Riddle-Speaker", "Mystical", "Wise", "Guardian"]
            rank += ["Enigmatic Oracle", "Riddle-Speaking Guardian", "Mystical Sphynx", "Wise Protector", "Guardian of Secrets"]
            of_the += ["of the Enigmatic Riddles", "of the Mystical Realms", "of the Wise Guardianship", "of the Secret Keepers", "of the Riddle-Speaking Monuments"]

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
            descriptor += ["Tentacled", "Sea Monster", "Deep Sea", "Colossal", "Terrifying"]
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
        descriptor += ["Amorphous", "Viscous", "Slithering", "Absorbing", "Gelatinous"]
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
            descriptor += ["Gelatinous", "Translucent", "Wobbly",¡]
            rank += ["Gelatinous Blob", "Translucent Mass", "Wobbly Menace", " Beast"]
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
        if "Ochre" in npc.subrace:
            descriptor += ["Earthen", "Muddy", "Rustic", "Clay-Like"]
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
        if "Corrosive" in npc.subrace:
            descriptor += ["Acidic", "Caustic", "Erosive", "Burning"]
            rank += ["Acidic Sludge", "Caustic Mass", "Erosive Ooze", "Burning Gel"]
            of_the += ["of the Acidic Pits", "of the Caustic Swamps", "of the Erosive Gullies", "of the Burning Lakes"]

        # Frost
        if "Frost" in npc.subrace:
            descriptor += ["Icy", "Frozen", "Chilling", "Glacial"]
            rank += ["Icy Blob", "Frozen Ooze", "Chilling Slime", "Glacial Mass"]
            of_the += ["of the Frozen Tundras", "of the Icy Caverns", "of the Chilling Fields", "of the Glacial Pools"]

        # Eldritch
        if "Eldritch" in npc.subrace:
            descriptor += ["Mystical", "Arcane", "Otherworldly", "Unearthly"]
            rank += ["Mystical Sludge", "Arcane Ooze", "Otherworldly Blob", "Unearthly Goo"]
            of_the += ["of the Arcane Realms", "of the Mystical Voids", "of the Otherworldly Depths", "of the Unearthly Planes"]

        # Luminous
        if "Luminous" in npc.subrace:
            descriptor += ["Glowing", "Radiant", "Luminescent", "Shining"]
            rank += ["Glowing Gel", "Radiant Ooze", "Luminescent Blob", "Shining Slime"]
            of_the += ["of the Glowing Caves", "of the Radiant Lakes", "of the Luminescent Swamps", "of the Shining Pits"]

        # Toxic
        if "Toxic" in npc.subrace:
            descriptor += ["Poisonous", "Venomous", "Toxic", "Hazardous"]
            rank += ["Poisonous Mass", "Venomous Blob", "Toxic Sludge", "Hazardous Goo"]
            of_the += ["of the Toxic Wastes", "of the Venomous Bogs", "of the Poisonous Marshes", "of the Hazardous Quagmires"]

    # Orc Race and Subraces
    if "Orc" in npc.race:
        # General Orc descriptor, rank, and Of_the Phrases
        descriptor += ["Warrior", "Brutish", "Fierce", "Strong", "Savage"]
        rank += ["War Chief", "Brutish Overlord", "Fierce Marauder", "Strong Leader", "Savage Fighter"]
        of_the += ["of the Orc Clans", "of the Brutish Tribes", "of the Fierce Legions", "of the Strongholds", "of the Savage Lands"]

        # Mountain
        if "Mountain" in npc.subrace:
            descriptor += ["Mountainous", "Stony", "Rugged", "Highland"]
            rank += ["Mountain Warlord", "Stony Chieftain", "Rugged Fighter", "Highland Leader"]
            of_the += ["of the Mountain Peaks", "of the Stony Valleys", "of the Rugged Terrain", "of the Highland Realms"]

        # Desert
        if "Desert" in npc.subrace:
            descriptor += ["Desert", "Sun-Scorched", "Nomadic", "Sand"]
            rank += ["Desert Raider", "Sun-Scorched Chief", "Nomadic Warrior", "Sand Marauder"]
            of_the += ["of the Desert Wastes", "of the Sun-Scorched Sands", "of the Nomadic Tribes", "of the Sand Dunes"]

        # Swamp
        if "Swamp" in npc.subrace:
            descriptor += ["Swamp", "Mire", "Bog", "Marsh"]
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
        if "Half-Orc" in npc.subrace:
            descriptor += ["Half-Breed", "Mixed", "Strongblood", "Dual-Nature"]
            rank += ["Half-Breed Leader", "Mixed Blood Warrior", "Strongblood Fighter", "Dual-Nature Chief"]
            of_the += ["of the Mixed Clans", "of the Half-Breed Tribes", "of the Strongblood Lines", "of the Dual-Nature Realms"]

        # Orog (Underdark)
        if "Orog (Underdark)" in npc.subrace:
            descriptor += ["Underdark", "Tunnel", "Subterranean", "Dark"]
            rank += ["Underdark Commander", "Tunnel Raider", "Subterranean Chief", "Dark Warrior"]
            of_the += ["of the Underdark Realms", "of the Tunnel Depths", "of the Subterranean Tribes", "of the Dark Caverns"]

        # Cave
        if "Cave" in npc.subrace:
            descriptor += ["Cavernous", "Rocky", "Echoing", "Shade"]
            rank += ["Cavern Chief", "Rocky Marauder", "Echoing Fighter", "Shade Hunter"]
            of_the += ["of the Cavernous Labyrinths", "of the Rocky Enclaves", "of the Echoing Caves", "of the Shaded Depths"]

        # Forest
        if "Forest" in npc.subrace:
            descriptor += ["Woodland", "Leafy", "Verdant", "Sylvan"]
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
        descriptor += ["Verdant", "Leafy", "Woody", "Floral", "Nature-Bound"]
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
            rank += ["Sapient Mushroom", "Learned Fungi", "Mycelial Scholar", "Thoughtful Spore"]
            of_the += ["of the Sapient Colonies", "of the Learned Undergrowth", "of the Mycelial Networks", "of the Thoughtful Groves"]

    # Undead Race and Subraces
    if "Undead" in npc.race:
        # General Undead descriptor, rank, and Of_the Phrases
        descriptor += ["Ethereal", "Ghostly", "Spectral", "Deathly", "Haunting"]
        rank += ["Eternal Warden", "Ghostly Guardian", "Spectral Marauder", "Deathly Overseer", "Haunting Spirit"]
        of_the += ["of the Forgotten Crypts", "of the Haunted Halls", "of the Deathly Shadows", "of the Spectral Realms", "of the Ghostly Echoes"]

        # Death Knight
        if "Death Knight" in npc.subrace:
            descriptor += ["Armored", "Cursed", "Warrior", "Terrifying"]
            rank += ["Cursed Knight", "Armored Fiend", "Terrifying Warlord", "Undead Champion"]
            of_the += ["of the Cursed Battlefields", "of the Armored Tombs", "of the Terrifying Wars", "of the Warrior's Curse"]

        # Honor Phantom
        if "Honor Phantom" in npc.subrace:
            descriptor += ["Dutiful", "Honorable", "Ethereal", "Bound"]
            rank += ["Dutiful Specter", "Honorable Wraith", "Ethereal Sentinel", "Bound Spirit"]
            of_the += ["of the Honorable Deeds", "of the Dutiful Watch", "of the Ethereal Bonds", "of the Bound Duty"]

        # Regret Ghost
        if "Regret Ghost" in npc.subrace:
            descriptor += ["Mournful", "Unresolved", "Sorrowful", "Pained"]
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
        if "Mischief Poltergeist" in npc.subrace:
            descriptor += ["Playful", "Mischievous", "Noisy", "Trickster"]
            rank += ["Playful Spirit", "Mischievous Ghost", "Noisy Phantom", "Trickster Apparition"]
            of_the += ["of the Haunted Houses", "of the Mischievous Antics", "of the Noisy Mansions", "of the Trickster's Lair"]

        # Vengeful Revenant
        if "Vengeful Revenant" in npc.subrace:
            descriptor += ["Revenge-Seeking", "Wrathful", "Resurrected", "Implacable"]
            rank += ["Revenge-Seeking Spirit", "Wrathful Wraith", "Resurrected Avenger", "Implacable Phantom"]
            of_the += ["of the Unrestful Graves", "of the Wrathful Shadows", "of the Resurrected Revenge", "of the Implacable Fury"]

        # Skeleton Protector
        if "Skeleton Protector" in npc.subrace:
            descriptor += ["Skeletal", "Undying", "Bone", "Guardian"]
            rank += ["Skeletal Guardian", "Undying Sentinel", "Bone Warden", "Guardian of Bones"]
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
            descriptor += ["Despairing", "Sorrowful", "Gloomy", "Mournful"]
            rank += ["Despairing Wraith", "Sorrowful Ghost", "Gloomy Specter", "Mournful Shade"]
            of_the += ["of the Sorrowful Places", "of the Despairing Abyss", "of the Gloomy Shadows", "of the Mournful Echoes"]

        # Vampire
        if "Vampire" in npc.subrace:
            descriptor += ["Bloodthirsty", "Nocturnal", "Charismatic", "Immortal"]
            rank += ["Bloodthirsty Count", "Nocturnal Predator", "Charismatic Fiend", "Immortal Sovereign"]
            of_the += ["of the Blood-Cursed Castles", "of the Nocturnal Hunts", "of the Charismatic Enchantment", "of the Immortal Nights"]

        # Prideful Wight
        if "Prideful Wight" in npc.subrace:
            descriptor += ["Arrogant", "Powerful", "Dominating", "Unyielding"]
            rank += ["Arrogant Wight", "Powerful Undead", "Dominating Specter", "Unyielding Ghoul"]
            of_the += ["of the Dominating Reign", "of the Arrogant Thrones", "of the Powerful Empires", "of the Unyielding Grasp"]

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
            descriptor += ["Lovelorn", "Heartbroken", "Eternal", "Seeking"]
            rank += ["Lovelorn Ghost", "Heartbroken Specter", "Eternal Seeker", "Seeking Spirit"]
            of_the += ["of the Lost Love", "of the Heartbroken Tales", "of the Eternal Search", "of the Seeking Souls"]

        # Weeping Howler
        if "Weeping Howler" in npc.subrace:
            descriptor += ["Weeping", "Howling", "Mournful", "Ominous"]
            rank += ["Weeping Spirit", "Howling Phantom", "Mournful Wraith", "Ominous Apparition"]
            of_the += ["of the Weeping Moors", "of the Howling Winds", "of the Mournful Echos", "of the Ominous Nights"]

        # Tomb's Hoarder
        if "Tomb's Hoarder" in npc.subrace:
            descriptor += ["Greedy", "Obsessive", "Guardian", "Ancient"]
            rank += ["Greedy Guardian", "Obsessive Wraith", "Tomb Keeper", "Ancient Hoarder"]
            of_the += ["of the Greedy Vaults", "of the Obsessive Collections", "of the Ancient Tombs", "of the Guarded Treasures"]

        # Penance Wraith
        if "Penance Wraith" in npc.subrace:
            descriptor += ["Repentant", "Suffering", "Tormented", "Redemptive"]
            rank += ["Repentant Spirit", "Suffering Phantom", "Tormented Soul", "Redemptive Ghost"]
            of_the += ["of the Suffering Shadows", "of the Repentant Pains", "of the Tormented Realms", "of the Redemptive Acts"]

        # Protector Spirit
        if "Protector Spirit" in npc.subrace:
            descriptor += ["Guardian", "Vigilant", "Sacred", "Dutiful"]
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

    if "Vampire" in npc.subrace:
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
            "Warlock", "Witch", "Enchanter", "Seer", "Harbinger",
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
        descriptor += ["Resourceful", "Diverse", "Adaptive", "Innovative", "Resilient"]
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
            descriptor += ["Forest", "Nature-Bound", "Woodland", "Green"]
            rank += ["Forest Guardian", "Nature-Bound Druid", "Woodland Ranger", "Green Enchanter"]
            of_the += ["of the Sylvan Groves", "of the Forest Shadows", "of the Woodland Paths", "of the Green Canopies"]

        # Wood Elf
        if "Wood" in npc.subrace:
            descriptor += ["Woodland", "Earthy", "Rustic", "Natural"]
            rank += ["Woodland Scout", "Earthy Hunter", "Rustic Protector", "Natural Herbalist"]
            of_the += ["of the Woodland Glades", "of the Earthy Forests", "of the Rustic Thickets", "of the Natural Springs"]

        # Dark Elf
        if "Dark" in npc.subrace:
            descriptor += ["Shadowy", "Underworld", "Mysterious", "Stealthy"]
            rank += ["Shadowy Assassin", "Underworld Warlock", "Mysterious Sorcerer", "Stealthy Infiltrator"]
            of_the += ["of the Shadowy Depths", "of the Underworld Caverns", "of the Mysterious Night", "of the Stealthy Ambushes"]

        # Night Elf
        if "Night" in npc.subrace:
            descriptor += ["Nocturnal", "Mystical", "Shadow-Woven", "Moonlit"]
            rank += ["Nocturnal Warrior", "Mystical Enchanter", "Shadow-Woven Ranger", "Moonlit Scout"]
            of_the += ["of the Nocturnal Forests", "of the Mystical Moons", "of the Shadow-Woven Paths", "of the Moonlit Glades"]

        # Feywild Elf
        if "Feywild" in npc.subrace:
            descriptor += ["Fey-Touched", "Enchanted", "Otherworldly", "Fairylike"]
            rank += ["Fey-Touched Ranger", "Enchanted Mystic", "Otherworldly Envoy", "Fairylike Wanderer"]
            of_the += ["of the Feywild Realms", "of the Enchanted Woods", "of the Otherworldly Visions", "of the Fairylike Dreams"]

        # Shadow Elf
        if "Shadow" in npc.subrace:
            descriptor += ["Dark", "Stealthy", "Evasive", "Obscured"]
            rank += ["Dark Stalker", "Stealthy Assassin", "Evasive Scout", "Obscured Ranger"]
            of_the += ["of the Shadowed Alleys", "of the Dark Realms", "of the Evasive Tactics", "of the Obscured Mysteries"]

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
        if "Sun" in npc.subrace:
            descriptor += ["Sunlit", "Radiant", "Bright", "Solar"]
            rank += ["Sunlit Warrior", "Radiant Enchanter", "Bright Archer", "Solar Guardian"]
            of_the += ["of the Sunlit Glades", "of the Radiant Valleys", "of the Bright Skies", "of the Solar Realms"]

        # Eclipse Elf
        if "Eclipse" in npc.subrace:
            descriptor += ["Twilight", "Eclipsed", "Shadowed", "Celestial"]
            rank += ["Twilight Seer", "Eclipsed Mystic", "Shadowed Ranger", "Celestial Enchanter"]
            of_the += ["of the Twilight Forests", "of the Eclipsed Moons", "of the Shadowed Paths", "of the Celestial Alignments"]

        # Moon Elf
        if "Moon" in npc.subrace:
            descriptor += ["Lunar", "Moonlit", "Nocturnal", "Starry"]
            rank += ["Lunar Mystic", "Moonlit Ranger", "Nocturnal Scout", "Starry Seer"]
            of_the += ["of the Lunar Lakes", "of the Moonlit Woods", "of the Nocturnal Groves", "of the Starry Skies"]

        # Wild Elf
        if "Wild" in npc.subrace:
            descriptor += ["Untamed", "Feral", "Savage", "Free"]
            rank += ["Untamed Warrior", "Feral Hunter", "Savage Druid", "Free Spirit"]
            of_the += ["of the Untamed Lands", "of the Feral Jungles", "of the Savage Plains", "of the Free Forests"]

        # Urban Elf
        if "Urban" in npc.subrace:
            descriptor += ["City-Born", "Metropolitan", "Sophisticated", "Civic"]
            rank += ["City-Born Scholar", "Metropolitan Artist", "Sophisticated Diplomat", "Civic Leader"]
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
            descriptor += ["Adventurous", "Explorer", "Conqueror", "Bold"]
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
    if "Lizardfolk" in npc.race:
        # General Lizardfolk descriptor, rank, and Of_the Phrases
        descriptor += ["Scaly", "Cold-Blooded", "Reptilian", "Stealthy", "Primitive"]
        rank += ["Scaly Hunter", "Reptilian Shaman", "Cold-Blooded Warrior", "Stealthy Tracker", "Primitive Chieftain"]
        of_the += ["of the Reptilian Marshes", "of the Scaly Jungles", "of the Cold-Blooded Tribes", "of the Stealthy Bogs", "of the Primitive Lands"]

        # Swamp Crocfolk
        if "Swamp Crocfolk" in npc.subrace:
            descriptor += ["Aquatic", "Toothy", "Menacing", "Powerful"]
            rank += ["Aquatic Predator", "Toothy Guardian", "Menacing Leader", "Powerful Crocfolk"]
            of_the += ["of the Swamp Waters", "of the Toothy Caverns", "of the Menacing Bogs", "of the Powerful Rivers"]

        #  Guanafolk
        if " Guanafolk" in npc.subrace:
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

    if "Kobold" in npc.race:
        descriptor = ["Cunning", "Small", "Agile", "Crafty", "Sneaky"]
        rank = ["Scout", "Trapmaker", "Sorcerer", "Warrior", "Shaman"]
        of_the = ["of the Dragon's Brood", "of the Cunning Warrens", "of the Agile Tribes", "of the Crafty Enclaves", "of the Sneaky Paths"]

        Colors = [ "Black","Blue","Green", "Red","White","Bronze","Silver",
                  "Gold","Brass","Copper","Shadow","Gem","Prismatic"]
        for color in Colors:
            if color in npc.subrace:
                descriptor += [f"{color} Scaled", f"{color} Clawed", f"{color} Eyed", f"{color} Crested"]
                rank += [f"{color} Scale Scout", f"{color} Claw Warrior", f"{color} Eye Sorcerer", f"{color} Crest Shaman"]
                of_the += [f"of the {color} Scale Lairs", f"of the {color} Claw Clans", f"of the {color} Eye Covens", f"of the {color} Crest Packs"]
                descriptor += [f"{color} Scaled", f"Metallic {color}", f"Shining {color}", f"Lustrous {color}"]
                rank += [f"{color} Scale Artisan", f"Metallic {color} Guardian", f"Shining {color} Smith", f"Lustrous {color} Sage"]
                of_the += [f"of the {color} Scaled Forges", f"of the Metallic {color} Bastions", f"of the Shining {color} Workshops", f"of the Lustrous {color} Libraries"]
                descriptor += [f"{color} Aura", f"Mystical {color}", f"Enigmatic {color}", f"Arcane {color}"]
                rank += [f"{color} Aura Scout", f"Mystical {color} Enchanter", f"Enigmatic {color} Trickster", f"Arcane {color} Sage"]
                of_the += [f"of the {color} Aura Shadows", f"of the Mystical {color} Realms", f"of the Enigmatic {color} Enclaves", f"of the Arcane {color} Sanctuaries"]

    if npc.background == "Bandit":
        descriptor = ["Ruthless", "Cunning", "Sly", "Daring", "Fierce"]
        rank = ["Bandit Leader", "Skilled Thief", "Merciless Brigand", "Clever Outlaw", "Fierce Raider"]
        of_the = ["of the Hidden Hideouts", "of the Silent Shadows", "of the Lawless Lands", "of the Treacherous Roads", "of the Wild Frontiers"]



    if npc.background == "Scholar":
        # 'Of the' phrases for Scholar names
        of_the += [
            "of the Academy", "of the Ancient Scrolls", "of the Hidden Lore", "of the Arcane Secrets",
            "of the Lost Library", "of the Philosophers", "of the Astral Studies", "of the Eldritch Truth",
            "of the Forbidden Knowledge", "of the Alchemical Mysteries", "of the Historical Chronicles",
            "of the Mythic Tales", "of the Cryptic Codes", "of the Learned Society", "of the Mystic Arts",
            "of the Elemental Theory", "of the Celestial Observations", "of the Ethereal Plane", "of the Sages"
        ]

        # descriptor for Scholar names
        descriptor += [
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
            "Analyst", "Polyglot", "Savant", "Curator", "Mastermind"
        ]
        #return f"The {random.choice(descriptor)} {random.choice(rank)} {random.choice(of_the)}"


    if npc.race == "Elemental":
        descriptor += [
            "Air",
            "Fire",
            "Watter",
            "Rock",
            "Earth",
            "Storm",
            "Aerial",
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
    elif npc.subrace == "Cronusian":
        descriptor += ["Ageless", "Timebound", "Epochal", "Hourglass", "Eternal"]
        rank += ["Chronomaster", "Timekeeper", "Oracle", "Elder", "Historian"]
        of_the += ["of the Ages", "of the Timeless Realms", "of the Eternal Clock", "of the Past and Future", "of the Ageless Wisdom"]

    # Eosian
    elif npc.subrace == "Eosian":
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
        descriptor = ["Creative", "Expressive", "Imaginative", "Artistic", "Innovative"]
        rank = ["Master Painter", "Skilled Sculptor", "Renowned Musician", "Gifted Poet", "Eccentric Performer"]
        of_the = ["of the Colorful Canvases", "of the Sculpted Masterpieces", "of the Melodic Harmonies", "of the Poetic Verses", "of the Theatrical Arts"]

    if npc.background == "Bandit":
        descriptor = ["Ruthless", "Cunning", "Sly", "Daring", "Fierce"]
        rank = ["Bandit Leader", "Skilled Thief", "Merciless Brigand", "Clever Outlaw", "Fierce Raider"]
        of_the = ["of the Hidden Hideouts", "of the Silent Shadows", "of the Lawless Lands", "of the Treacherous Roads", "of the Wild Frontiers"]

    if npc.background == "Bard":
        descriptor = ["Charismatic", "Talented", "Storytelling", "Melodic", "Witty"]
        rank = ["Master Storyteller", "Enchanting Musician", "Clever Lyricist", "Charismatic Performer", "Witty Troubadour"]
        of_the = ["of the Enchanting Ballads", "of the Ancient Tales", "of the Melodic Chords", "of the Witty Verses", "of the Captivating Performances"]

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
        descriptor = ["Devout", "Holy", "Spiritual", "Righteous", "Blessed"]
        rank = ["Holy Priest", "Devout Healer", "Spiritual Guide", "Righteous Crusader", "Blessed Acolyte"]
        of_the = ["of the Holy Order", "of the Devout Mission", "of the Spiritual Journey", "of the Righteous Path", "of the Blessed Light"]

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
        descriptor = ["Fanatical", "Mystical", "Secretive", "Zealous", "Obscure"]
        rank = ["Cult Leader", "Fanatical Acolyte", "Mystical Devotee", "Zealous Follower", "Obscure Priest"]
        of_the = ["of the Fanatical Sect", "of the Mystical Rites", "of the Secretive Orders", "of the Zealous Beliefs", "of the Obscure Rituals"]

    # Background: Druid
    if npc.background == "Druid":
        descriptor = ["Nature-Bound", "Earthy", "Mystical", "Primal", "Guardian"]
        rank = ["Circle Archdruid", "Earthy Protector", "Mystical Shaman", "Primal Warden", "Guardian of the Wild"]
        of_the = ["of the Nature's Circle", "of the Earthy Realms", "of the Mystical Woods", "of the Primal Forces", "of the Guardian Groves"]

    # Background: Expert
    if npc.background == "Expert":
        descriptor = ["Knowledgeable", "Skilled", "Professional", "Adept", "Specialized"]
        rank = ["Expert Consultant", "Knowledgeable Practitioner", "Skilled Professional", "Adept Analyst", "Specialized Technician"]
        of_the = ["of the Knowledgeable Fields", "of the Skilled Trades", "of the Professional Studies", "of the Adept Research", "of the Specialized Skills"]

    # Background: Explorer
    if npc.background == "Explorer":
        descriptor = ["Adventurous", "Curious", "Intrepid", "Daring", "Pioneering"]
        rank = ["Legendary Explorer", "Curious Wanderer", "Intrepid Adventurer", "Daring Pathfinder", "Pioneering Scout"]
        of_the = ["of the Uncharted Lands", "of the Curious Expeditions", "of the Intrepid Journeys", "of the Daring Quests", "of the Pioneering Frontiers"]

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
        descriptor = ["Stealthy", "Rugged", "Sharpshooter", "Trapper", "Wild"]
        rank = ["Stealthy Tracker", "Rugged Huntsman", "Sharpshooter Archer", "Skilled Trapper", "Wild Stalker"]
        of_the = ["of the Stealthy Pursuit", "of the Rugged Wilderness", "of the Sharpshooter's Range", "of the Skilled Snares", "of the Wild Hunt"]

    # Background: Knight
    if npc.background == "Knight":
        descriptor = ["Chivalrous", "Gallant", "Honorable", "Bold", "Noble"]
        rank = ["Knight", "Champion", "Defender", "Warrior", "Cavalier"]
        of_the = ["of the Noble Order", "of the Chivalrous Quests", "of the Gallant Deeds", "of the Honorable Battles", "of the Bold Ventures"]

    # Background: Mage
    if npc.background == "Mage":
        descriptor = ["Arcane", "Mystical", "Learned", "Enigmatic", "Sorcerous"]
        rank = ["Arcane Wizard", "Mystical Sorcerer", "Learned Magician", "Enigmatic Alchemist", "Sorcerous Scholar"]
        of_the = ["of the Arcane Mysteries", "of the Mystical Arts", "of the Learned Scrolls", "of the Enigmatic Potions", "of the Sorcerous Academies"]

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
    if npc.background == "Noble":
        descriptor = ["Aristocratic", "Refined", "Graceful", "Influential", "Dignified"]
        rank = ["Noble Lord", "Aristocratic Lady", "Refined Diplomat", "Influential Baron", "Dignified Count"]
        of_the = ["of the Aristocratic Courts", "of the Refined Estates", "of the Graceful Mansions", "of the Influential Councils", "of the Dignified Assemblies"]

    # Background: Priest
    if npc.background == "Priest":
        descriptor = ["Devout", "Pious", "Clerical", "Faithful", "Sacred"]
        rank = ["High Priest", "Devout Cleric", "Pious Acolyte", "Faithful Preacher", "Sacred Keeper"]
        of_the = ["of the Holy Sanctuaries", "of the Devout Congregations", "of the Pious Orders", "of the Faithful Ministries", "of the Sacred Rites"]

    # Background: Pirate
    if npc.background == "Pirate":
        descriptor = ["Ruthless", "Swashbuckling", "Seafaring", "Adventurous", "Rebellious"]
        rank = ["Infamous Captain", "Swashbuckling Buccaneer", "Seafaring Raider", "Adventurous Corsair", "Rebellious Marauder"]
        of_the = ["of the Infamous Seas", "of the Swashbuckling Crews", "of the Seafaring Voyages", "of the Adventurous Journeys", "of the Rebellious Fleets"]

    # Background: Ranger
    if npc.background == "Ranger":
        descriptor = ["Wilderness", "Tracking", "Survivalist", "Rugged", "Nature's"]
        rank = ["Wilderness Scout", "Master Tracker", "Survivalist Expert", "Rugged Outlander", "Nature's Warden"]
        of_the = ["of the Wilderness Paths", "of the Tracking Hunts", "of the Survivalist Camps", "of the Rugged Mountains", "of the Nature's Secrets"]

    # Background: Scholar
    if npc.background == "Scholar":
        descriptor = ["Learned", "Intellectual", "Inquisitive", "Studious", "Erudite"]
        rank = ["Learned Professor", "Intellectual Researcher", "Inquisitive Historian", "Studious Philosopher", "Erudite Sage"]
        of_the = ["of the Learned Academies", "of the Intellectual Societies", "of the Inquisitive Libraries", "of the Studious Lectures", "of the Erudite Scrolls"]

    # Background: Soldier
    if npc.background == "Soldier":
        descriptor = ["Disciplined", "Battle-Hardened", "Strategic", "Brave", "Tactical"]
        rank = ["Veteran Commander", "Disciplined Sergeant", "Battle-Hardened Warrior", "Strategic General", "Brave Soldier"]
        of_the = ["of the Disciplined Regiments", "of the Battle-Hardened Fronts", "of the Strategic Commands", "of the Brave Units", "of the Tactical Operations"]

    # Background: Rogue
    if npc.background == "Rogue":
        descriptor = ["Sneaky", "Cunning", "Agile", "Mysterious", "Resourceful"]
        rank = ["Master Thief", "Cunning Assassin", "Agile Scout", "Mysterious Spy", "Resourceful Trickster"]
        of_the = ["of the Sneaky Shadows", "of the Cunning Plots", "of the Agile Escapes", "of the Mysterious Underworld", "of the Resourceful Heists"]

    # Background: Shaman
    if npc.background == "Shaman":
        descriptor = ["Spiritual", "Mystic", "Elemental", "Tribal", "Ancestral"]
        rank = ["Leader", "Healer", "Elemental Guide", "Tribal Sage", "Ancestral Keeper"]
        of_the = ["of the Spiritual Rites", "of the Mystic Visions", "of the Elemental Forces", "of the Tribal Traditions", "of the Ancestral Spirits"]

    # Background: Spy
    if npc.background == "Spy":
        descriptor = ["Covert", "Undercover", "Secretive", "Stealthy", "Infiltrating"]
        rank = ["Covert Agent", "Undercover Operative", "Secretive Informant", "Stealthy Scout", "Infiltrating Spy"]
        of_the = ["of the Covert Missions", "of the Undercover Operations", "of the Secretive Networks", "of the Stealthy Reconnaissance", "of the Infiltrating Tactics"]

    # Background: Traveler
    if npc.background == "Traveler":
        descriptor = ["Wandering", "Adventurous", "Nomadic", "Curious", "Worldly"]
        rank = ["Wandering Nomad", "Adventurous Explorer", "Nomadic Wanderer", "Curious Journeyer", "Worldly Traveler"]
        of_the = ["of the Wandering Paths", "of the Adventurous Expeditions", "of the Nomadic Tribes", "of the Curious Voyages", "of the Worldly Discoveries"]

    # Background: Prankster
    if npc.background == "Prankster":
        descriptor = ["Streetwise", "Scrappy", "Surviving", "Quick", "Resourceful"]
        rank = ["Streetwise Scamp", "Scrappy Survivor", "Surviving Orphan", "Quick Pickpocket", "Resourceful Rogue"]
        of_the = ["of the Street Corners", "of the Scrappy Alleys", "of the Surviving Struggles", "of the Quick Escapes", "of the Resourceful Scrounges"]

    # Background: Warrior
    if npc.background == "Warrior":
        descriptor = ["Battle-Ready", "Fearless", "Mighty", "Skilled", "Honorable"]
        rank = ["Battle-Ready Fighter", "Fearless Warrior", "Mighty Gladiator", "Skilled Duelist", "Honorable Champion"]
        of_the = ["of the Battle Arenas", "of the Fearless Campaigns", "of the Mighty Conquests", "of the Skilled Combats", "of the Honorable Duels"]

    # Background: Warlock
    if npc.background == "Warlock":
        descriptor = ["Eldritch", "Mysterious", "Pact-Bound", "Arcane", "Otherworldly"]
        rank = ["Eldritch Caster", "Mysterious Occultist", "Pact-Bound Conjurer", "Arcane Scholar", "Otherworldly Advisor"]
        of_the = ["of the Eldritch Secrets", "of the Mysterious Rites", "of the Pact-Bound Servitude", "of the Arcane Lore", "of the Otherworldly Powers"]

    # Background: Witch
    if npc.background == "Witch":
        descriptor = ["Enchanting", "Occult", "Mystical", "Hexing", "Wise"]
        rank = ["Enchanting Sorceress", "Occult Witch", "Mystical Herbalist", "Hexing Caster", "Wise Crone"]
        of_the = ["of the Enchanting Spells", "of the Occult Rituals", "of the Mystical Arts", "of the Hexing Curses", "of the Wise Traditions"]































    rank += [





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
        "Avenger",
        "Apprentice",

# B

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
"Curse Breaker",
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
"Flame",
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
"Ascendant",
"Astral Voyager",
"Lost",

    # B
    "Baboon",
 "Banshee", "Bard", "Baron", "Barrow", "Basilisk",
    "Battlemage", "Beacon", "Bear", "Beastmaster", "Beetle", "Beholder", "Benefactor",
    "Berserker", "Bishop", "Bison", "Blacksmith", "Blade", "Blaze", "Blighted", "Blizzard",
    "Blossom", "Boar", "Bone", "Bounty Hunter", "Bow", "Bravo", "Breeder", "Brewer", "Briar",
    "Brigadier", "Bringer", "Buccaneer", "Bull", "Burglar", "Butcher", "Butterfly", "Buzzard",

    # C
     "Cairn", "Camel", "Cannibal", "Captain", "Cartographer", "Cedar", "Centurion",
     "Charlatan", "Cheetah", "Chemist", "Chieftain", "Chimera", "Claw", "Cleric",
    "Climber", "Cobbler", "Cobra", "Collector", "Colossus", "Commander", "Commodore", "Conjurer",
    "Conqueror", "Corsair", "Cougar", "Counselor", "Courage", "Crow", "Crusader", "Crypt",
    "Cultist", "Curator", "Curse Breaker", "Cursed Wanderer", "Cyclops",

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
    "Feather", "Fel", "Fellow", "Fern", "Ferret", "Fiend", "Fin", "Fire", "Flame", "Flutist",
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
     "Kaiju", "Keeper", "Kestrel", "Killer", "King", "Kinsman", "Kiss", "Knife",
    "Knight", "Lark", "Laurel", "Leader", "Legate", "Legend", "Legionnaire", "Leopard", "Lich",
    "Light", "Lily", "Lion", "Lizard", "Lord", "Lost", "Lotus", "Lover", "Lynx",

    # M
    "Machine", "Mage", "Magister", "Magus", "Man", "Mantis", "Marauder", "Mare", "Marigold",
    "Mariner", "Marquis", "Marshal", "Martyr", "Mask",
"Mason", "Master", "Mastermind", "Mastiff",
    "Matriarch", "Mausoleum", "Memento", "Mender", "Mercenary", "Merlin", "Mesmer", "Messenger",
    "Miller", "Mimic", "Mind", "Minister", "Minstrel", "Mist", "Monk", "Monster Hunter", "Monster",
    "Moon", "Morgue", "Mortal", "Moth", "Mountaineer", "Mourner", "Mule", "Mystic", "Mystic",

    # N - O
    "Navigator", "Necro", "Necromancer", "Nether", "Nightingale", "Nightmare", "Ninja", "Noble",
    "Nomad", "Oracle", "Orchid", "Ossuary", "Otter", "Outlander", "Outlaw", "Outrider", "Overlord",
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
    "Valkyrie", "Vampire", "Vanguard", "Vicar", "Virtuoso", "Visionary", "Voyager", "Warlock",
     "Watcher", "Werewolf", "Witch", "Witchhunter", "Wizard",

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
        "Curse Breaker",
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
        "Exorcist",
        "Expedition",
        "Explorer",
        "for Hire",
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

                "Jackal's",


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
        "Baron",
        "Barbarian",
        "Bard",
        "Baron",
        "Baron",
        "Baroness",
        "Cleric",
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

        "Wing",
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
        "Gaucho",
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


        "Intrigue",



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




        "Orcish Warchief",
        "'s Chosen",
        "'s Rise",

        "Kin",
















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
        "Queen",
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
        " Seeker",


        "Rider",

        "Ritualist",

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
        "Sabertooth",
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

        "Secret",
        "Secretary",
        "Seeker",

        "Sentinel",
        "Strength",
        "Sergeant",
        "Scale",
        "Serpentlord",
        "Serpent",

        "Shadowmancer",
        "Shadowseer",
        "Shaman",

        "Radiance",



        "Shogun",
        "Siege",
		"Master",
        "Mountain",

        "Silver",

        "Pride",

        "Six-Shooter",

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
        "Sorcerer",
		"Bishop",

        "Soulkeeper",
        "Sovereign",
        "Sparkweaver",

        "Spell",
		"Commander",
        "Spellblade",

        "Spellshield",
        "Spellweaver",
        "Spellwoven",
        "Spelunker",
        "Riddle",
        "Spiderweb",
        "Spiritguide",


        "Whisperer",
        "blade",
        "born",
        "dancer",
        "forge",
        "shadow",
        "shaper",


        "of Stonehenge",


        "Stormbinder",
        "Stormbringer",
        "Storyteller",


        "Thane",

        "Theorist",
        "Warhawk",


        "Heir",

        "Tiamat's Scion",


        "Tiefling",
		"Hellstrider",
        "Tale",
        "Torchbearer",


        "Star",



        "Echo",



        "of the Treasure Fleet",
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
        "Turtle",
		"Islander",
        "Treasure",
        "Twilight",
        "Skymaiden",
        "Valkyrie",
        "Chosen",
        "Valor",
        "Valorblade",
        "Lord",
        "Vanguard",
        "Serpent",
        "Venerable",
        "Vicar",
        "Voyager",
        "Viscount",
        "Vizier",
        "Viceroy",
        "of Hispaniola",
        "Rival",
        "Voidseer",
        "Voidtouched",
        "Vagabond",
        "Valkyrie",
        "Vampire",
        "Vicar",
        "Viking",
        "Vintner",
        "Violet",
        "Viscount",
        "Vampire",
        "Vagrant",
        "Voyage",
        "Valkyrie",
        "Pilgrim",
        "Trader",
        "Serpentlord",


        "Cruor",
        "Hex",
        "Inferno",
        "Jinx",
        "Lurk",
        "Malefic",
        "Nefarious",
        "Oblivion",
        "of the Endless Sands",
        "of the Gods",
        "Pestilence",
        "Quake",
        "Rancor",
        "Torment",
        "Umbra",
        "Vendetta",
        "Wraith",
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



        "Exemplar",
        "Guardian",
        "Ghoul",
        "High Priest",
        "Harbinger",
        "Illusionist",
        "Infernal",

        "Lama",
        "Lecturer",
        "Legate",
        "Lieutenant",
        "Matriarch",
        "Marshal",
        "Matriarch",
        "Mogul",
        "Nomad",
        "Numerologist",
        "Nun",
        "Naga",
        "Necro",
        "Necromancer",
        "Nether",
        "Nightingale",
        "Nightmare",

        "Noble",
        "Nocturnal",

        "Nightshade",
        "Nightshade",
        "Nightveil",
        "Necrologist",
        "Netherbound",
		"Navigator",
        "Paragon",
        "Patriarch",
        "Pharaoh",

        "Pasha",
        "Prelate",
        "Priestess",
        "Prodigy",
        "Patriarch",
        "Progenitor",
        "Pioneer",

        "Raj",

        "Renegade",

        "Samurai",
        "Scholar",



        "Tutor",
        "Tribe Leader",

        "Vanguard",
        "Vicar",
        "Virtuoso",
        "Voyager",

        "Warlord",
        "Whisper",
        "Wanderer",

        "Windrider",
        "Winglord",
        "Wisdom",
        "Witchdoctor",
        "Wolfkin",
        "Wail",
        "Walker",
        "Warlock",
        "Warrior",


        "Wizard",
        "Witch",


        "Willow",



        "Wandering Healer",


        " Poet",

        "Whale",
        "Whirlwind",
        "Whisper",
        "Wight",
        "Wild",
        "Willow",


        "Wolf"
        "Wraith",
        "Windcaller",

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
        "Zenithar",
        "Zealot",
        "Zinnia",
        "Zombie",
        "Zoologist",

    ]






        elif Dice(10) < 5:
            Name = SyllabicName(
                syllables = SyllabicExtraction(Names),
                min_syllables=2,
                max_syllables=3)



    if npc.race == "Snakefolk":
        snakefolk = [

            ]
        Names += snakefolk




    if Dice(9)<9:
        namer = MarkovNameGenerator(Names)
        Name = namer.generate_name()

        FullName =  Name

    else:
        FullName =  random.choice(Names)

    return FullName



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
