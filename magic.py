import dnd
import npc_class as NPC
import random

### Notes ###
# Calculate the probability of learning the spell
# Two Points Slope
# (SpellLvl,Chance)
# (0,p0) & (max+1,0)
# ch = y1 + (x-x1) * (y2-y1):(x2-x1)
# ch = p0 + (Lvl) * (-p0):(max+1) = p0 + (1 - Lvl):(max+1)
#p0 = 1 - (0.95/max_spell_level)
#probability = p0 * ( 1 - spell_level / (1 + max_spell_level))
# Randomly select if the spell is not already in the list
#if random.random() < probability:


def PB(lvl):
    # Proficiency Bonus
    return dnd.PB(lvl)
    
def Dice(D=6,N=1):
    return dnd.Dice(D,N)

def safe_sample(source_list, sample_size):
    """Safely sample from a list, ensuring we don't exceed its length."""
    if not source_list or sample_size <= 0:
        return []  # Return an empty list if the source list is empty or sample size is invalid
    return random.sample(source_list, min(len(source_list), sample_size))    

def get_max_spell_level(character_level, difficulty = 1):
    if difficulty < 1: difficulty = 1
    if difficulty > 10: difficulty = 10
    level = (character_level - difficulty) // (2 * difficulty)
    if level < 0: return 0
    if level > 9: return 9
    return level


def add_spell(spell_list, spell_name, spell_definition=""):
    if spell_name not in spell_list:
        spell_list += f"\n- {spell_name}"
        if spell_definition:
            spell_list += f": {spell_definition}"            
    return spell_list


class Spellbook:
    def __init__(self,npc):
        
        self.character_level = npc.level
        self.cantrip = ""
        self.spells = {level: "" for level in range(1, 10)}

        self.cantrip_set = set()
                
        self.difficulty = 10
        
        self.slots = {level: 0 for level in range(1, 10)}

        # Natural Spellcasting. Doesn't need spell slots.
        self.one     = ""
        self.two     = ""
        self.three   = ""
        self.one_day_each_list = []
        self.two_day_each_list = []
        self.three_day_each_list = []
        self.num1d = 3
        self.num2d = 3
        self.num3d = 3

        self.recharge = []
        self.recharge_list = []
        
        self.accessible = {level: [] for level in range(1, 10)}
        self.selected = {level: [] for level in range(1, 10)}

    def slots_at(self, spell_level):
        character_level = self.character_level
        difficulty = self.difficulty
        pb = PB(character_level)

        # Calculate the maximum spell level
        max_level = get_max_spell_level(character_level, difficulty)

        # If max_level is 0, then no slots should be available
        if max_level == 0:
            return None

        # For levels beyond the maximum level, there should be no slots
        if spell_level > max_level:
            return None
        
        # For the maximum level, there should be exactly 1 slot
        if spell_level == max_level:
            return 1

        # Calculate slots for levels below the maximum
        # The function should start at pb / difficulty at level 0 and approach 1 at max_level
        max_slots_at_zero = 5
        slope = (1-max_slots_at_zero) / (max_level-0.5)  # Calculate the slope of the line
        slots = max_slots_at_zero + slope * spell_level

        # Round and adjust the number of slots
        slots = max(1, round(slots+0.5))  # Ensure at least 1 slot and round to nearest whole number

        return slots if slots >= 1 else None  # Return None if slots fall below 1
    

    def select_spells(self,spellcaster = False):
        selected_spells_set = set()  # Keep track of all selected spells
        self.UpdateSlots()
        power_level = self.max_spell_level
        
        if spellcaster:
            for level in range(1, 10):

                num_slots = self.slots[level] if self.slots[level] is not None else 0
                num_spells =  min( num_slots, max(self.number_spell(level), 0) ) # Ensure non-negative

                # Update accessible spells for each level
                accessible_spells = set(self.accessible[level]) - selected_spells_set  # Remove already selected spells
                accessible_spells = list(accessible_spells)

                if accessible_spells and num_spells > 0:  # Check for non-empty list and positive num_spells
                    num_to_select = min(num_spells, len(accessible_spells))
                    selected_spells = random.sample(accessible_spells, num_to_select)
                    self.selected[level] = selected_spells
                    selected_spells_set.update(selected_spells)  # Add new selections to the set of selected spells
                else:
                    self.selected[level] = []  # Handle empty or non-applicable cases

        else:

            # Update for one, two, three times per day lists            
            for spell_list, num in [(self.one_day_each_list, self.num1d), 
                                    (self.two_day_each_list, self.num2d), 
                                    (self.three_day_each_list, self.num3d)]:
                available_spells = list(set(spell_list) - selected_spells_set)
                # Remove already selected spells
                num = min(num, len(available_spells))
                # Ensure we don't exceed the number of available spells
                if num > 0:
                    selected_spells = random.sample(available_spells, num)
                    spell_list[:] = selected_spells
                    # Update the list in place
                    selected_spells_set.update(selected_spells)
                    # Add to the set of selected spells
                else:
                    spell_list[:] = []  # Clear the list if no spells are to be selected


    def number_spell(self,spell_level):
        if spell_level == 0:
            return min(5, max(0, self.max_spell_level))
        d = self.difficulty
        l = spell_level
        pb = PB(self.character_level)
        num = (2*pb-d-l)//d
        return num

    
    def number_daily_spells(self, times_day):
        num   = 6-times_day
        return num

    def add_random_spells(self):
        for level, spells in self.accessible.items():
            num_spells = self.number_spell(level)
            if spells:
                selected_spells = random.sample(spells, min(num_spells, len(spells)))
                for spell in selected_spells:
                    self.add_spell(level, spell)
    @property
    def first(self):
        return self.spells[1]

    @property
    def second(self):
        return self.spells[2]

    @property
    def third(self):
        return self.spells[3]

    @property
    def fourth(self):
        return self.spells[4]

    @property
    def fifth(self):
        return self.spells[5]

    @property
    def sixth(self):
        return self.spells[6]

    @property
    def seventh(self):
        return self.spells[7]

    @property
    def eighth(self):
        return self.spells[8]

    @property
    def ninth(self):
        return self.spells[9]

    @property
    def max_spell_level(self):
        difficulty = self.difficulty
        character_level = self.character_level
        if difficulty < 1: difficulty = 1
        if difficulty > 10: difficulty = 10
        self.difficulty = difficulty
        level = (character_level - difficulty) // (2 * difficulty)
        if level < 0: return 0
        if level > 9: return 9
        return level


    def UpdateDifficulty(self,D):
        if D < 1: D = 1
        if D > 10: D = 10
        self.difficulty = D
        self.UpdateSlots()

    def slots_calculator(self, spell_level):
        import math
        max_spell_level = self.max_spell_level
        k = -math.log(1 / max_spell_level) / max_spell_level
        slots = max_spell_level * math.exp(-k * spell_level)
        slots = math.ceil(slots)
        return max(1, int(slots))

    def UpdateSlots(self):
        max_spell_level = self.max_spell_level
        for level in range(1, 10):
            # Example slot allocation: Decrease slots as the level approaches max_spell_level
            self.slots[level] = self.slots_at(level) if level <= max_spell_level else 1
            


    def add_spell(self, spell_level, spell_name, spell_definition=""):
        # Using a set to track added spells
        if spell_level == 0:
            if spell_name not in self.cantrip_set:
                self.cantrip += f"\n\t- {spell_name}"
                if spell_definition:
                    self.cantrip += f": {spell_definition}"
                self.cantrip_set.add(spell_name)
        elif 1 <= spell_level <= 9:
            spell_list = self.spells.get(spell_level, "")
            if spell_name not in spell_list:
                spell_list += f"\n\t- {spell_name}"
                if spell_definition:
                    spell_list += f": {spell_definition}"
                self.spells[spell_level] = spell_list

                
    def add_natural(self, spell, definition="", times_day = 1):
        result = f"\n\t{spell}: {times_day} per day. {definition}"
        if times_day == 1:
            self.one += result
        elif times_day == 2:
            self.two += result
        elif times_day == 3:
            self.three += result


    def add_rechargeable(self, spell, definition="", recharge_at=6):
        if spell:  # Ensure the spell name is not empty
            #roll = f"{recharge_at}-6" if recharge_at < 6 else "6"
            recharge_entry = f"\n\t{spell}\n" # + \t- Recharges at {roll} in a d6. {definition}"
            self.recharge.append(recharge_entry)        

    def SpellbookString(self,npc):
        result = "\n"
        if is_ritual(npc):
            result += f"{npc.title} is a ritual spellcaster. \n"
        if self.cantrip:
            result += "Cantrips (at will): " + self.cantrip + "\n"
        if is_spellcaster(npc):    
            for level in range(1, 10):
                slots = self.slots[level]
                if slots is not None:  # Check if slots is not None
                    if self.spells[level]:
                        ordinal = "th" if 4 <= level <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(level % 10, "th")
                        result += f"\n[{slots}]{level}{ordinal} Level Spells:" + self.spells[level]
                        result += "\n"
        else:
            # Include natural spells
            
            if self.one.strip():
                result += "\nNatural Spells (1/day): " + self.one + "\n"
            if self.two.strip():
                result += "\nNatural Spells (2/day): " + self.two + "\n"
            if self.three.strip():
                result += "\nNatural Spells (3/day): " + self.three + "\n"

            # Include rechargeable spells
            if self.recharge:
                result += "\nRechargeable Spells:"
                for spell_entry in self.recharge:
                    if spell_entry.strip():  # Ensure the entry is not empty
                        result += spell_entry

        return result.strip()

def is_ritual(npc):
    if npc.background == "Priest": return True
    if npc.background == "Cleric": return True
    if npc.background == "Cultist": return True
    if npc.background == "Druid": return True
    if npc.background == "Mage": return True
    if npc.background == "Shaman": return True
    if npc.background == "Warlock": return True
    if npc.background == "Witch": return True
    return False

def is_spellcaster(npc):
    if npc.background == "Priest": return True
    if npc.background == "Cleric": return True
    if npc.background == "Cultist": return True
    if npc.background == "Druid": return True
    if npc.background == "Mage": return True
    if npc.background == "Shaman": return True
    if npc.background == "Warlock": return True
    if npc.background == "Witch": return True
    return False

def Magic(npc):

    Lvl = npc.level
    race = npc.race
    background = npc.background

    spellbook = Spellbook(npc)


    cantrips_list=[]
    one_day_each_list=[]
    two_day_each_list=[]
    three_day_each_list=[]
    first_list=[]
    second_list=[]
    third_list=[]
    fourth_list=[]
    fifth_list=[]
    sixth_list = []
    seventh_list = []
    eighth_list = []
    ninth_list = []
    recharge = []

    difficulty = 2
# BACKGROUNDS:

    # Bandit
    if background == "Bandit":
        difficulty = 2 + Dice(6) 
        cantrips_list += ["Mage Hand","Minor Illusion","Prestidigitation","Message","Thaumaturgy"            ]
        one_day_each_list += ["Disguise Self", "Expeditious Retreat", "Silent Image"]
        two_day_each_list = ["Darkness", "Invisibility", "Pass Without Trace"]
        three_day_each_list += ["Misty Step", "Blur", "Feather Fall"]
        first_list += [            "Charm Person",            "Disguise Self",            "Expeditious Retreat",            "Fog Cloud",            "Sleep"]
        second_list += [            "Darkness",            "Pass Without Trace",            "Silence",            "Invisibility",            "Alter Self"]
        third_list += [            "Hypnotic Pattern",            "Leomund’s Tiny Hut",            "Nondetection",            "Dispel Magic",            "Blink"]
        fourth_list += [            "Dimension Door","Greater Invisibility",            "Arcane Eye",            "Locate Creature",            "Confusion"]
        fifth_list += [            "Mislead",            "Modify Memory",            "Passwall",            "Seeming",            "Teleportation Circle"]        
        sixth_list += [            "True Seeing",            "Contingency",            "Mass Suggestion"]
        seventh_list += [            "Teleport",            "Mirage Arcane",            "Project Image"]
        eighth_list += [            "Antimagic Field",            "Mind Blank",            "Demiplane"]
        ninth_list += [ "Time Stop", "Foresight","Imprisonment"]

    # Bard
    if background == "Bard":

        difficulty = 1  # Full Caster
        cantrips_list += [            "Dancing Lights",            "Vicious Mockery",            "Mage Hand",            "Minor Illusion",            "Prestidigitation", "Light",            "Message",            "Mending",            "Friends"        ]
        one_day_each_list += [            "Charm Person", "Disguise Self", "Feather Fall"]
        two_day_each_list += [            "Invisibility", "Suggestion", "Enhance Ability"]
        three_day_each_list += [            "Hypnotic Pattern",            "Major Image",            "Counterspell"]
        first_list += [            "Disguise Self",            "Healing Word",            "Identify",            "Faerie Fire",            "Charm Person",            "Silent Image",            "Sleep",            "Tasha’s Hideous Laughter",    "Unseen Servant",            "Speak With Animals"]
        second_list += [      "Invisibility",            "Knock",            "Detect Thoughts",            "Enhance Ability",            "Lesser Restoration",            "Zone of Truth",            "Calm Emotions",            "Heat Metal",            "Suggestion",            "Phantasmal Force"        ]
        third_list += [            "Dispel Magic",            "Leomund’s Tiny Hut",            "Hypnotic Pattern",            "Major Image",            "Sending",            "Tongues",            "Fear",            "Charm Monster",            "Stinking Cloud",            "Speak with Dead"        ]
        fourth_list += [            "Dimension Door",            "Polymorph",            "Greater Invisibility",            "Freedom of Movement",            "Hallucinatory Terrain",            "Locate Creature",            "Compulsion",            "Confusion",            "Geas",            "Stone Shape"        ]
        fifth_list += [            "Mass Cure Wounds",            "Raise Dead",            "Greater Restoration",            "Teleportation Circle",            "Mislead",            "Modify Memory",            "Animate Objects",            "Awaken",            "Scrying",            "Dominate Person"        ]
        sixth_list += [            "True Seeing",            "Otto’s Irresistible Dance",            "Programmed Illusion",            "Mass Suggestion",            "Heroes’ Feast",            "Find The Path",            "Eyebite",            "Countercharm"        ]
        seventh_list += [            "Teleport",            "Resurrection",            "Regenerate",            "Mirage Arcane",            "Etherealness",            "Symphony Of The Masked",            "Forcecage",            "Dream Of The Blue Veil"        ]
        eighth_list += [            "Power Word Stun",            "Mind Blank",            "Maze",            "Glibness",            "Dominate Monster",            "Antimagic Field",            "Foresight",            "Feeblemind"        ]
        ninth_list += [            "Power Word Kill",           "True Polymorph",            "Time Stop",            "Psychic Scream",            "Prismatic Wall",            "Mass Polymorph",            "Foresight",            "Meteor Swarm"        ]




    # Berserker
    if background == "Berserker":

        difficulty = Dice(5)+ Dice(5)  
        cantrips_list += [  "Blade Ward",            "Thaumaturgy",            "True Strike",   "Guidance"]
        one_day_each_list += [            "Longstrider",            "False Life",            "Shield"]
        two_day_each_list += ["Enhance Ability", "Blur", "Protection from Energy"]
        three_day_each_list += ["Haste", "Fear", "Heroism"]
        first_list += [  "Bane",            "Compelled Duel",            "Wrathful Smite",   "Searing Smite"        ]
        second_list += [            "Branding Smite",            "Magic Weapon",            "Find Steed"        ]
        third_list += [            "Crusader's Mantle",    "Elemental Weapon",            "Fear",           "Spirit Guardians"        ]
        fourth_list += [            "Stoneskin","Freedom Of Movement",            "Compulsion",        "Grasping Vine"        ]
        fifth_list += [            "Destructive Wave",            "Flame Strike",   "Geas",            "Commune With Nature"        ]
        sixth_list += [            "Heroes' Feast",            "Find the Path",            "Wind Walk"        ]
        seventh_list += [            "Regenerate",    "Fire Storm",            "Resurrection"        ]
        eighth_list += [            "Earthquake",            "Control Weather",            "Animal Shapes"]
        ninth_list += ["Storm of Vengeance","True Resurrection","Shapechange"]

    # Charlatan
    if background == "Charlatan":
        difficulty = Dice(8) 
        cantrips_list += ["Minor Illusion", "Prestidigitation","Mage Hand",            "Friends"        ]
        one_day_each_list += ["Disguise Self","Charm Person",            "Illusory Script"]
        two_day_each_list += ["Minor Illusion","Message", "Silent Image"]
        three_day_each_list += ["Suggestion","Mirror Image",            "Invisibility"]
        first_list += ["Disguise Self",            "Charm Person",            "Illusory Script",            "Sleep"        ]
        second_list += ["Invisibility",            "Suggestion",            "Alter Self",            "Mirror Image"        ]
        third_list += ["Hypnotic Pattern",            "Major Image",            "Nondetection",            "Gaseous Form"        ]
        fourth_list += ["Greater Invisibility",            "Confusion",            "Dimension Door",            "Polymorph"        ]
        fifth_list += ["Mislead",            "Seeming",            "Modify Memory",            "Dominate Person"        ]
        sixth_list += [      "Programmed Illusion",            "True Seeing",            "Mass Suggestion"        ]
        seventh_list += [   "Mirage Arcane",            "Project Image",            "Simulacrum"        ]
        eighth_list += ["Mind Blank",            "Dominate Monster",            "Power Word Stun"        ]
        ninth_list += [ "Time Stop",            "True Polymorph",            "Foresight"        ]
            
    # Commoner
    if background == "Commoner":

        difficulty = Dice(4) + Dice(4) + Dice(4)  
        # Cantrips
        cantrips_list += ["Mending",            "Prestidigitation",            "Message",            "Guidance"        ]
        one_day_each_list += ["Prestidigitation", "Mending", "Light"]
        two_day_each_list += ["Guidance", "Resistance", "Mage Hand"]
        three_day_each_list += ["Cure Wounds", "Shield", "Feather Fall"]
        first_list += [            "Cure Wounds",            "Purify Food And Drink",            "Alarm",            "Goodberry"]
        second_list += [            "Lesser Restoration",           "Animal Messenger",            "Find Steed",            "Locate Animals Or Plants"]
        third_list += [            "Create Food And Water",            "Sending",            "Tiny Hut",            "Speak With Plants"]
        fourth_list += [            "Control Water",            "Stone Shape",            "Locate Creature",            "Fabricate"]
        fifth_list += [            "Awaken",            "Commune With Nature",            "Greater Restoration",            "Teleportation Circle"]
        sixth_list += [            "Heroes' Feast",            "Move Earth",            "Heal"]
        seventh_list += [            "Regenerate",            "Resurrection",            "Miracle"          ]
        eighth_list += [            "Control Weather",            "Earthquake",            "Holy Aura"  ]
        ninth_list += [            "True Resurrection","Storm of Vengeance",]
        '''
        spellbook.add_spell(ninth_list, "Wish" , 9, "One per Lifetime")
        '''

    # Cultist
    if background == "Cultist":
        difficulty = Dice(3) 
        cantrips_list += [            "Chill Touch",            "Eldritch Blast",            "Guidance",            "Infestation",            "Light",            "Sacred Flame",           "Thaumaturgy",            "Toll The Dead",            "Vicious Mockery"            ]
        one_day_each_list += [            "Command",            "Inflict Wounds",            "Protection from Good and Evil"]
        two_day_each_list += [            "Suggestion",            "Silence",            "Hold Person"]
        three_day_each_list += [            "Detect Thoughts", "Darkness", "Disguise Self"]
        first_list += [            "Bane",            "Cause Fear",            "Command",            "Hex",            "Inflict Wounds",            "Protection From Good And Evil",            "Shield Of Faith",            "Unseen Servant"            ]
        second_list += [            "Blindness/Deafness",            "Darkness",            "Enthrall",            "Hold Person",            "Mind Spike",            "Ray Of Enfeeblement",            "Silence",            "Spiritual Weapon"]
        third_list += [    "Animate Dead",            "Bestow Curse",            "Fear",            "Hypnotic Pattern",            "Speak With Dead",           "Vampiric Touch",            "Tongues",            "Spirit Guardians"            ]
        fourth_list += [            "Blight",            "Death Ward",            "Hallucinatory Terrain",            "Locate Creature",            "Phantasmal Killer",            "Shadow Of Moil",            "Sickening Radiance",            "Summon Greater Demon"            ]
        fifth_list += [            "Contagion",           "Danse Macabre",            "Geas",            "Hold Monster",            "Insect Plague",            "Mass Cure Wounds",            "Scrying",            "Wrath Of Nature"            ]
        sixth_list += [            "Circle Of Death",            "Create Undead",            "Eyebite",           "Harm",            "Heroes' Feast",    "Mass Suggestion",            "True Seeing",            "Word Of Recall"            ]
        seventh_list += [            "Finger Of Death",            "Plane Shift",            "Regenerate",            "Resurrection",           "Symbol",            "Teleport","Etherealness","Fire Storm"            ]
        eighth_list += [           "Antimagic Field",          "Dominate Monster","Feeblemind",            "Holy Aura",            "Incendiary Cloud",            "Maze",            "Power Word Stun",            "Sunburst"                      ]
        ninth_list += [           "Astral Projection","Gate",            "Implosion",            "Mass Heal",            "Power Word Kill",            "Psychic Scream",            "True Resurrection",            "Weird"            ]

    # Criminal
    if background == "Criminal":
        difficulty = 1 + Dice(6)  
        cantrips_list += [            "Mage Hand",            "Minor Illusion",            "Prestidigitation",            "Message"        ]
        one_day_each_list += ["Disguise Self", "Silent Image", "Expeditious Retreat"]
        two_day_each_list += ["Invisibility", "Pass without Trace", "Knock"]
        three_day_each_list += ["Mage Hand", "Message", "Prestidigitation"]
        first_list += [            "Disguise Self",            "Charm Person",            "Silent Image",            "Sleep",            "Expeditious Retreat"        ]
        second_list += [            "Invisibility",   "Suggestion",            "Alter Self",            "Darkness",            "Pass Without Trace"]
        third_list += ["Nondetection",            "Dispel Magic",            "Hypnotic Pattern",            "Major Image",            "Leomund’s Tiny Hut"        ]
        fourth_list += ["Greater Invisibility",            "Dimension Door",            "Arcane Eye",            "Freedom of Movement",            "Locate Creature"]
        fifth_list += [ "Mislead",            "Modify Memory",            "Teleportation Circle",            "Passwall","Seeming"        ]
        sixth_list += [            "True Seeing",            "Programmed Illusion",            "Find the Path"        ]
        seventh_list += ["Mirage Arcane",            "Project Image",           "Teleport"        ]
        eighth_list += [ "Demiplane",            "Mind Blank",            "Antimagic Field"        ]
        ninth_list += [            "Imprisonment",            "Time Stop",            "Power Word Kill"        ]

    # Druid
    if background == "Druid":

        difficulty = 1  # Full caster
        cantrips_list += [            "Druidcraft",            "Guidance",            "Mending",           "Produce Flame",            "Shillelagh",            "Resistance"        ]
        one_day_each_list += [            "Cure Wounds",            "Entangle",            "Speak with Animals"]
        two_day_each_list += [            "Barkskin",            "Moonbeam",            "Pass without Trace"]
        three_day_each_list += [            "Guidance",            "Thorn Whip",            "Druidcraft"]
        first_list += [            "Cure Wounds",            "Entangle",            "Faerie Fire",           "Goodberry",            "Healing Word",          "Thunderwave",            "Create or Destroy Water",            "Speak With Animals",            "Longstrider"        ]
        second_list += [            "Barkskin",            "Flame Blade",            "Flaming Sphere",            "Lesser Restoration",            "Moonbeam",            "Pass Without Trace",            "Spike Growth",            "Animal Messenger"        ]
        third_list += ["Call Lightning",            "Cure Wounds",            "Dispel Magic",            "Protection From Energy",            "Water Breathing",            "Water Walk",            "Wind Wall"        ]
        fourth_list += ["Hallucinatory Terrain","Control Water","Freedom Of Movement","Ice Storm","Stoneskin","Wall of Fire","Giant Insect"]
        fifth_list += [            "Awaken",            "Commune With Nature",            "Cure Wounds",            "Geas",            "Mass Cure Wounds",            "Reincarnate",            "Tree Stride"        ]
        sixth_list += [            "Heal",            "Heroes' Feast",            "Move Earth",            "Sunbeam",            "Transport Via Plants",            "Wall Of Thorns",            "Wind Walk"        ]
        seventh_list += [            "Fire Storm",            "Mirage Arcane",            "Plane Shift",            "Regenerate",            "Reverse Gravity",            "Teleport"        ]
        eighth_list += [            "Animal Shapes",            "Control Weather",            "Earthquake",            "Sunburst",            "Tsunami",            "Antipathy/Sympathy"        ]
        ninth_list += [            "Shapechange",            "Storm of Vengeance",            "True Resurrection","Foresight","Mass Heal"        ]

    # Expert
    if background == "Expert":
        difficulty = Dice(6)  
        cantrips_list += ["Guidance",  "Mending","Message",            "Prestidigitation",            "Thaumaturgy"]
        one_day_each_list += ["Identify", "Disguise Self", "Detect Thoughts"]
        two_day_each_list += ["Enhance Ability", "Invisibility", "Knock"]
        three_day_each_list += ["Mage Hand", "Message", "Prestidigitation"]
        first_list += ["Comprehend Languages",          "Cure Wounds",            "Detect Magic",          "Disguise Self",            "Identify"]
        second_list += ["Enhance Ability",         "Find Traps",            "Lesser Restoration",            "Locate Animals Or Plants",            "Locate Object"]
        third_list += ["Create Food And Water",            "Dispel Magic",            "Protection From Energy",            "Remove Curse",            "Tongues"]
        fourth_list += ["Freedom Of Movement",            "Greater Restoration",            "Locate Creature",            "Stone Shape",            "Fabricate"]
        fifth_list += ["Contact Other Plane",            "Legend Lore",            "Mass Cure Wounds",            "Planar Binding",            "Teleportation Circle"]
        sixth_list += ["Find The Path",         "Guards And Wards",            "Heal",            "Heroes' Feast",            "True Seeing"]
        seventh_list += ["Regenerate",            "Resurrection",            "Sequester",            "Symbol",            "Teleport"]
        eighth_list += ["Antimagic Field",            "Control Weather",            "Earthquake",            "Mind Blank",            "Power Word Stun"]
        ninth_list += [ "Foresight",         "Mass Heal",            "Power Word Heal",            "True Resurrection",            "Wish"]

    # Explorer
    if background == "Explorer":
        difficulty = Dice(8)  
        cantrips_list += [  "Druidcraft","Guidance","Mage Hand","Mending","Thaumaturgy"]
        one_day_each_list += ["Find the Path", "Pass without Trace", "Water Walk"]
        two_day_each_list += ["Goodberry", "Protection from Energy", "Speak with Animals"]
        three_day_each_list += ["Longstrider", "Guidance", "Light"]
        first_list += [ "Cure Wounds","Detect Magic","Goodberry","Jump","Longstrider"]
        second_list += ["Find Traps","Flame Blade", "Locate Animals Or Plants", "Pass Without Trace","Rope Trick"]
        third_list += ["Create Food And Water","Daylight","Feign Death","Protection From Energy","Water Breathing"]
        fourth_list += ["Control Water","Fabricate","Freedom Of Movement","Locate Creature","Stone Shape"]
        fifth_list += [ "Commune With Nature", "Legend Lore","Passwall","Teleportation Circle","Tree Stride"]
        sixth_list += ["Find The Path","Move Earth","Transport Via Plants", "Wind Walk",            "True Seeing"]
        seventh_list += ["Mirage Arcane","Plane Shift","Regenerate",            "Reverse Gravity",            "Teleport"        ]
        eighth_list += ["Antimagic Field","Control Weather","Earthquake",            "Telepathy",            "Tsunami"        ]
        ninth_list += ["Foresight","Gate","Imprisonment","Meteor Swarm",            "Time Stop"        ]

    # Gladiator
    if background == "Gladiator":
        difficulty = Dice(8)  
        cantrips_list += ["Blade Ward", "Friends",            "Prestidigitation",            "True Strike",            "Thaumaturgy"        ]
        one_day_each_list += ["Heroism","Compelled Duel",            "Shield"]
        two_day_each_list += ["Enhance Ability", "Thunderous Smite", "Blur"]
        three_day_each_list += ["Mage Hand", "True Strike", "Prestidigitation"]
        first_list += ["Bless","Command",            "Heroism",            "Shield",            "Thunderwave"        ]
        second_list += ["Branding Smite","Enhance Ability",            "Enlarge/Reduce",            "Magic Weapon",            "Spiritual Weapon"        ]
        third_list += ["Crusader's Mantle","Fear",            "Haste",            "Protection From Energy",            "Slow"        ]
        fourth_list += ["Compulsion","Freedom Of Movement",            "Stone Shape",            "Stoneskin",            "Wall Of Fire"        ]
        fifth_list += ["Flame Strike","Greater Restoration",            "Hold Monster",            "Legend Lore",            "Skill Empowerment"        ]
        sixth_list += ["Blade Barrier","Find The Path",            "Heal",            "Heroes' Feast",            "Tenser's Transformation"        ]
        seventh_list += ["Crown Of Stars","Forcecage",            "Mordenkainen's Sword",            "Regenerate",            "Resurrection"]
        eighth_list += ["Antimagic Field","Dominate Monster",            "Earthquake",            "Holy Aura",            "Incendiary Cloud"        ]
        ninth_list += ["Blade Of Disaster","Foresight","Mass Heal","Power Word Kill","Time Stop"]

    # Guard
    if background == "Guard":
        difficulty = Dice(12)  
        cantrips_list += [            "Blade Ward", "Control Flames","Friends","Light",            "True Strike"]
        one_day_each_list += [            "Shield", "Alarm",            "Protection from Evil and Good"]
        two_day_each_list += ["Hold Person", "Calm Emotions", "Zone of Truth"]
        three_day_each_list += ["Message", "Prestidigitation", "Light"]
        first_list += ["Alarm", "Compelled Duel", "Protection from Evil and Good", "Shield", "Wrathful Smite"        ]
        second_list += ["Aid", "Find Traps", "Hold Person", "Magic Weapon", "Zone of Truth"        ]
        third_list += ["Counterspell", "Crusader's Mantle", "Protection from Energy", "Slow", "Spirit Guardians"        ]
        fourth_list += ["Aura of Life", "Banishment", "Mordenkainen's Private Sanctum", "Stoneskin", "Watery Sphere"        ]
        fifth_list += ["Circle of Power", "Geas", "Hold Monster", "Wall of Force", "Teleportation Circle"        ]
        sixth_list += ["Find the Path", "Forbiddance", "Harm", "Heroes' Feast", "True Seeing"        ]
        seventh_list += ["Etherealness", "Forcecage", "Mordenkainen's Sword", "Resurrection", "Symbol"        ]
        eighth_list += ["Antimagic Field", "Control Weather", "Earthquake", "Holy Aura", "Telepathy"        ]
        ninth_list += ["Foresight", "Imprisonment", "Mass Heal", "Power Word Kill", "True Resurrection"        ]

    # Healer
    if background == "Healer":
        difficulty = Dice(4)  
        cantrips_list += ["Guidance",           "Resistance",            "Spare the Dying",            "Thaumaturgy",            "Virtue"]
        first_list += ["Cure Wounds", "Detect Poison and Disease", "Healing Word", "Purify Food and Drink", "Sanctuary"]
        second_list += ["Aid", "Calm Emotions", "Lesser Restoration", "Prayer of Healing", "Protection from Poison"]
        third_list += ["Create Food and Water", "Mass Healing Word", "Protection from Energy", "Remove Curse", "Remove Disease"]
        fourth_list += ["Death Ward", "Freedom of Movement", "Guardian of Faith", "Greater Restoration", "Stone Shape"]
        fifth_list += ["Greater Restoration", "Hallow", "Mass Cure Wounds", "Raise Dead", "Scrying"]
        sixth_list += [            "Heal",            "Heroes' Feast",            "Planar Ally",            "True Seeing",            "Word of Recall"        ]
        seventh_list += [            "Etherealness",            "Regenerate",            "Resurrection",            "Symbol",            "Teleport"        ]
        eighth_list += [            "Antimagic Field",            "Control Weather",            "Earthquake",            "Holy Aura",            "Telepathy"        ]
        ninth_list += [            "Foresight",            "Mass Heal",            "Power Word Heal",            "True Resurrection",            "Wish"        ]

    # Hermit
    if background == "Hermit":
        difficulty = Dice(4)  
        cantrips_list += [            "Druidcraft",           "Guidance",            "Mending",            "Resistance",            "Thaumaturgy"        ]
        one_day_each_list += [            "Cure Wounds",          "Lesser Restoration",            "Shield of Faith"]
        two_day_each_list += [            "Prayer of Healing",            "Remove Poison",            "Protection from Poison"]
        three_day_each_list += [            "Purify Food and Drink",            "Detect Poison and Disease",            "Resistance"]
        first_list += [            "Cure Wounds",            "Detect Poison and Disease",            "Goodberry",            "Purify Food and Drink",            "Speak with Animals"        ]
        second_list += [            "Animal Messenger",            "Find Traps",            "Lesser Restoration",            "Protection from Poison",            "Silence"        ]
        third_list += [            "Create Food and Water",            "Meld into Stone",            "Protection from Energy",            "Remove Curse",            "Water Walk"        ]
        fourth_list += [            "Divination",            "Freedom of Movement",            "Locate Creature",            "Stone Shape",            "Wild Shape"        ]
        fifth_list += [            "Commune",            "Geas",            "Greater Restoration",            "Legend Lore",            "Scrying"     ]
        sixth_list += [            "Find the Path",            "Heal",            "Heroes' Feast",            "True Seeing",            "Wind Walk"        ]
        seventh_list += [            "Etherealness", "Regenerate", "Resurrection", "Symbol", "Teleport"        ]
        eighth_list += [            "Antimagic Field",            "Control Weather",            "Earthquake",            "Holy Aura",            "Telepathy"        ]
        ninth_list += [            "Foresight",            "Gate",            "Mass Heal",            "True Resurrection",           "Wish"        ]

    # Hero
    if background == "Hero":
        difficulty = Dice(10)  
        cantrips_list += [            "Guidance",   "Light",            "Resistance",            "Spare the Dying",            "Thaumaturgy"]
        one_day_each_list += [            "Bless", "Cure Wounds", "Shield of Faith"]
        two_day_each_list += ["Aid", "Lesser Restoration", "Protection from Energy"]
        three_day_each_list += ["Beacon of Hope", "Crusader's Mantle", "Remove Curse"]
        first_list += [            "Bless", "Command", "Cure Wounds", "Heroism", "Shield of Faith"]
        second_list += [            "Aid", "Branding Smite", "Find Steed", "Lesser Restoration", "Protection from Poison"]
        third_list += [            "Beacon of Hope", "Crusader's Mantle", "Daylight", "Remove Curse", "Revivify"]
        fourth_list += [            "Aura of Purity", "Aura of Life", "Death Ward", "Freedom of Movement", "Stoneskin"]
        fifth_list += [            "Circle of Power", "Greater Restoration", "Mass Cure Wounds", "Raise Dead", "Flame Strike"]
        sixth_list += [            "Find the Path",            "Heal",            "Heroes' Feast",            "True Seeing",            "Word of Recall"]
        seventh_list += [            "Regenerate", "Resurrection", "Symbol", "Teleport", "Conjure Celestial"]
        eighth_list += [            "Antimagic Field",            "Holy Aura", "Control Weather", "Earthquake", "Sunburst"]
        ninth_list += [           "Foresight",            "Gate", "Mass Heal", "True Resurrection", "Storm of Vengeance"        ]

    # Hunter
    if background == "Hunter":

        difficulty = Dice(6)  
        cantrips_list += ["Druidcraft", "Guidance", "Resistance", "Thorn Whip", "Produce Flame"]            
        one_day_each_list += ["Detect Poison and Disease", "Entangle", "Snare"]
        two_day_each_list += ["Calm Animals", "Darkvision", "Pass without Trace"]
        three_day_each_list += ["Beast Sense", "Locate Animals or Plants", "Speak with Animals"]
        first_list += ["Alarm", "Entangle", "Fog Cloud", "Goodberry", "Hunter's Mark"]
        second_list += ["Barkskin", "Beast Sense", "Darkvision", "Find Traps", "Pass Without Trace"]
        third_list += ["Conjure Animals","Daylight", "Nondetection", "Speak with Plants", "Water Walk"]
        fourth_list += ["Freedom of Movement", "Locate Creature", "Stoneskin", "Control Water", "Divination"]
        fifth_list += ["Commune with Nature", "Conjure Elemental", "Scrying", "Tree Stride", "Awaken"]
        sixth_list += ["Find the Path", "Move Earth", "Sunbeam", "Transport via Plants", "Wind Walk"]
        seventh_list += ["Fire Storm", "Mirage Arcane", "Plane Shift", "Regenerate", "Reverse Gravity"]
        eighth_list += ["Animal Shapes", "Antimagic Field", "Control Weather", "Earthquake", "Sunburst"]
        ninth_list += [            "Foresight",            "Shapechange",            "Storm of Vengeance",            "True Resurrection",            "Tsunami"        ]

    # Knight
    if background == "Knight":
        difficulty = Dice(8)  
        cantrips_list += [            "Blade Ward", "Light", "Prestidigitation", "Resistance", "Spare the Dying", "Thaumaturgy"]
        one_day_each_list += ["Command", "Compelled Duel", "Shield of Faith"]
        two_day_each_list += ["Aid", "Branding Smite", "Protection from Poison"]
        three_day_each_list += ["Crusader’s Mantle", "Magic Weapon", "Warding Bond"]
        first_list += [            "Bless", "Compelled Duel", "Cure Wounds", "Heroism", "Shield of Faith"]
        second_list += [            "Aid", "Find Steed", "Lesser Restoration", "Magic Weapon", "Warding Bond"]
        third_list += [            "Crusader's Mantle", "Dispel Magic", "Protection from Energy", "Remove Curse", "Revivify"]
        fourth_list += [            "Aura of Life",            "Aura of Purity", "Banishment", "Death Ward", "Stoneskin"]
        fifth_list += [            "Circle of Power",            "Destructive Wave",            "Dispel Evil and Good",            "Geas",            "Raise Dead"]
        sixth_list += [            "Find the Path",            "Heal", "Heroes' Feast", "True Seeing", "Wind Walk"]
        seventh_list += [            "Resurrection",            "Symbol",            "Teleport"        ]
        eighth_list += [            "Antimagic Field",            "Earthquake",            "Holy Aura"        ]
        ninth_list += ["Mass Heal", "True Resurrection"]

    # Mage
    if background == "Mage":
        difficulty = 1  # Full Caster
        cantrips_list += [            "Acid Splash", "Fire Bolt", "Mage Hand", "Prestidigitation", "Ray of Frost", "Minor Illusion", "Detect Magic"]
        one_day_each_list += ["Shield", "Magic Missile", "Identify"]
        two_day_each_list += ["Misty Step", "Detect Thoughts", "Scorching Ray"]
        three_day_each_list += ["Counterspell", "Dispel Magic", "Fireball"]
        first_list += [            "Detect Magic",            "Mage Armor",            "Magic Missile",            "Shield",            "Thunderwave",             "Identify"]
        second_list += [            "Arcane Lock",            "Invisibility", "Levitate", "Mirror Image", "Scorching Ray",        "Misty Step", "Detect Thoughts", "Scorching Ray", "Arcane Lock", "Invisibility"]
        third_list += ["Counterspell", "Dispel Magic", "Fireball", "Fly", "Haste"]
        fourth_list += ["Dimension Door", "Greater Invisibility", "Ice Storm", "Polymorph", "Stone Shape"]
        fifth_list += ["Animate Objects", "Cone of Cold", "Teleportation Circle", "Wall of Force", "Telekinesis"]
        sixth_list += ["Chain Lightning", "Contingency", "Disintegrate", "Globe of Invulnerability", "True Seeing"]
        seventh_list += ["Delayed Blast Fireball", "Teleport", "Plane Shift", "Prismatic Spray", "Simulacrum"]
        eighth_list += ["Antimagic Field", "Clone", "Demiplane", "Power Word Stun", "Telepathy"]
        ninth_list += ["Gate", "Meteor Swarm", "Power Word Kill", "Time Stop", "Wish"]

    # Monk
    if background == "Monk":
        difficulty = Dice(8)  # One-Half Caster
        cantrips_list += ["Control Flames", "Gust", "Mold Earth", "Shape Water", "True Strike","Mage Hand","Guidance", "Resistance", "Spare the Dying", "Thaumaturgy"]
        one_day_each_list += ["Shield", "Expeditious Retreat", "Longstrider","Blur", "Jump"]
        two_day_each_list += ["Pass Without Trace", "Enhance Ability","Darkvision"]
        three_day_each_list += ["Haste", "Protection from Energy", "Water Walk", "Feather Fall", "Jump","See Invisibility", "Shield", "Misty Step", "Nondetection"        ]
        first_list += [            "Expeditious Retreat",            "Feather Fall",            "Jump", "Longstrider", "Shield",            "Unseen Servant"        ]
        second_list += [            "Blur", "Darkvision", "Enhance Ability", "Gust of Wind", "Pass Without Trace",            "Spider Climb",  "Darkvision"]
        third_list += [            "Haste",            "Protection from Energy",            "Slow",            "Water Walk",            "Wind Walk"            ]
        fourth_list += [            "Freedom of Movement",            "Stoneskin",            "Giant Insect",            "Control Water",            "Control Winds",            "Death Ward",            "Dimension Door"        ]
        fifth_list += [            "Far Step",           "Transmute Rock",            "Control Winds",            "Steel Wind Strike",            "Greater Restoration",            "Telekinesis",            "Hold Monster",            "Wall of Force"        ]
        sixth_list += [            "Heal", "Wind Walk", "Word of Recall", "Tenser's Transformation", "Primordial Ward"]
        seventh_list += ["Etherealness", "Plane Shift", "Regenerate", "Teleport", "Resurrection"]
        eighth_list += ["Antimagic Field", "Holy Aura", "Mind Blank", "Earthquake", "Incendiary Cloud"]
        ninth_list += ["Foresight", "Imprisonment", "Mass Heal", "Power Word Heal", "True Resurrection"]

    # Noble
    if "Noble" in background:
        difficulty = Dice(12)  
        cantrips_list += [            "Prestidigitation",            "Mage Hand", "Friends", "Message"]
        one_day_each_list += ["Charm Person", "Identify"]
        two_day_each_list += ["Detect Thoughts", "Suggestion"]
        three_day_each_list += ["Tongues", "Sending"]
        first_list += ["Charm Person", "Disguise Self", "Identify", "Feather Fall", "Alarm"]
        second_list += ["Detect Thoughts", "Suggestion", "Locate Object", "See Invisibility", "Nystul's Magic Aura"]
        third_list += ["Tongues", "Sending", "Leomund's Tiny Hut", "Clairvoyance", "Counterspell"]
        fourth_list += ["Leomund's Secret Chest", "Mordenkainen's Private Sanctum", "Arcane Eye", "Greater Invisibility", "Charm Monster"]
        fifth_list += ["Geas","Legend Lore", "Modify Memory", "Scrying", "Teleportation Circle"]
        sixth_list += [            "Mass Suggestion",            "True Seeing",           "Guards and Wards",      "Contingency",            "Find the Path"]
        seventh_list += [            "Teleport",            "Mordenkainen's Magnificent Mansion",            "Symbol",            "Mirage Arcane",            "Regenerate"]
        eighth_list += [            "Mind Blank",            "Antipathy/Sympathy",            "Demiplane",            "Maze",            "Dominate Monster"]
        ninth_list += [           "Foresight",            "Imprisonment",            "Power Word Kill",            "True Polymorph",            "Wish"]

    # Priest
    if background == "Priest":
        difficulty = Dice(3)
        cantrips_list += ["Guidance",            "Light",            "Mending",            "Sacred Flame",           "Thaumaturgy",            "Resistance" ]        
        one_day_each_list += ["Cure Wounds", "Sanctuary"]
        if npc.level > 20: one_day_each_list += ["Divine Intervention"]
        two_day_each_list += ["Lesser Restoration", "Prayer of Healing"]
        three_day_each_list += ["Dispel Magic", "Remove Curse"]
        first_list += ["Cure Wounds", "Bless", "Healing Word", "Protection from Evil and Good","Detect Poison and Disease", "Sanctuary",
                       "Guiding Bolt", "Command", "Detect Magic"]
        second_list += ["Lesser Restoration",            "Spiritual Weapon",            "Prayer of Healing",            "Aid",
                        "Find Traps",            "Augury",            "Hold Person" ]
        third_list += ["Dispel Magic", "Remove Curse", "Mass Healing Word","Spirit Guardians", "Protection from Energy", "Tongues"]
        fourth_list += ["Death Ward", "Guardian of Faith", "Divination", "Banishment", "Freedom of Movement"]
        fifth_list += ["Greater Restoration", "Mass Cure Wounds", "Scrying", "Flame Strike", "Geas"]
        sixth_list += [ "Heal", "Planar Ally", "Harm", "True Seeing", "Create Undead"]
        seventh_list += ["Resurrection", "Regenerate", "Symbol", "Conjure Celestial", "Etherealness"]
        eighth_list += ["Holy Aura", "Antimagic Field", "Earthquake", "Control Weather", "Dominate Monster"]
        ninth_list += ["Mass Heal", "True Resurrection", "Gate", "Astral Projection", "Power Word Heal"]

    # Pirate
    if background == "Pirate":
        difficulty = Dice(4)+Dice(4)
        cantrips_list += ["Mage Hand", "Message", "Prestidigitation", "Druidcraft"]
        one_day_each_list += ["Fog Cloud", "Grease"]
        two_day_each_list += ["Misty Step", "Suggestion"]
        three_day_each_list += ["Gaseous Form", "Water Walk"]
        first_list += ["Expeditious Retreat", "Disguise Self", "Create or Destroy Water", "Fog Cloud", "Grease"]
        second_list += ["Misty Step", "Suggestion", "Alter Self", "Gust of Wind", "Locate Object"]
        third_list += ["Gaseous Form",                      "Water Walk",                      "Tidal Wave",                      "Major Image",                      "Water Breathing"]
        fourth_list += ["Control Water",                       "Watery Sphere",                       "Dimension Door",                       "Storm Sphere",                       "Greater Invisibility"]
        fifth_list += ["Control Winds",                      "Mislead",                      "Maelstrom",                      "Teleportation Circle",                      "Rary's Telepathic Bond"]
        sixth_list += ["Investiture of Wind",                      "Chain Lightning",                      "True Seeing",                     "Wind Walk",                      "Find the Path"]
        seventh_list += ["Teleport", "Regenerate", "Control Weather", "Reverse Gravity", "Whirlwind"]
        eighth_list += ["Control Weather", "Telepathy", "Incendiary Cloud", "Tsunami", "Dominate Monster"]
        ninth_list += ["Meteor Swarm", "Storm of Vengeance", "Time Stop", "Mass Polymorph", "Foresight"]

    # Ranger
    if background == "Ranger":
        difficulty = Dice(4)  
        cantrips_list += ["Druidcraft", "Guidance", "Resistance", "Thorn Whip"]
        one_day_each_list += ["Longstrider", "Speak with Animals"]
        two_day_each_list += ["Pass without Trace", "Spike Growth"]
        three_day_each_list += ["Water Walk", "Water Breathing"]
        first_list += [            "Cure Wounds",            "Goodberry", "Hunter's Mark", "Fog Cloud", "Alarm"]
        second_list += ["Pass without Trace", "Spike Growth", "Lesser Restoration", "Silence", "Locate Animals or Plants"]
        third_list += ["Water Walk", "Water Breathing", "Protection from Energy", "Speak with Plants", "Conjure Animals"]
        fourth_list += ["Freedom of Movement", "Stoneskin", "Locate Creature", "Grasping Vine", "Conjure Woodland Beings"]
        fifth_list += ["Commune with Nature", "Swift Quiver", "Tree Stride", "Greater Restoration", "Conjure Volley"]
        sixth_list += ["Heal", "Sunburst", "Heroes' Feast", "Find the Path", "Transport via Plants"]
        seventh_list += ["Mirage Arcane", "Regenerate", "Fire Storm", "Reverse Gravity", "Plane Shift"]
        eighth_list += ["Tsunami", "Earthquake", "Sunburst", "Control Weather", "Animal Shapes"]
        ninth_list += ["Storm of Vengeance","Shapechange",                      "Foresight", "True Resurrection",                      "Mass Heal"]

    # Rogue
    if background == "Rogue":
        difficulty = Dice(8)
        cantrips_list += ["Mage Hand", "Minor Illusion", "Prestidigitation", "Message"]
        one_day_each_list += ["Disguise Self", "Silent Image", "Expeditious Retreat"]
        two_day_each_list += ["Invisibility", "Misty Step", "Pass Without Trace"]
        three_day_each_list += ["Blink", "Nondetection", "Leomund's Tiny Hut"]
        first_list += ["Charm Person", "Sleep", "Tasha's Hideous Laughter", "Fog Cloud", "Feather Fall"]
        second_list += ["Darkness", "Suggestion", "Mirror Image", "Alter Self", "Silence"]
        third_list += ["Haste", "Major Image", "Dispel Magic", "Hypnotic Pattern", "Counterspell"]
        fourth_list += ["Dimension Door", "Greater Invisibility", "Arcane Eye", "Freedom of Movement", "Confusion"]
        fifth_list += ["Mislead", "Teleportation Circle", "Modify Memory", "Dominate Person", "Passwall"]
        sixth_list += ["True Seeing", "Mass Suggestion", "Programmed Illusion", "Chain Lightning", "Find the Path"]
        seventh_list += ["Mirage Arcane", "Teleport", "Etherealness", "Regenerate", "Project Image"]
        eighth_list += ["Mind Blank", "Dominate Monster", "Power Word Stun", "Antimagic Field", "Maze"]
        ninth_list += ["Time Stop", "Foresight", "Imprisonment", "True Polymorph", "Astral Projection"]

    # Scholar
    if background == "Scholar":
        difficulty = Dice(3)
        cantrips_list += ["Prestidigitation",                         "Mage Hand",                         "Mending",                         "Message"]
        one_day_each_list += ["Identify", "Comprehend Languages"]
        two_day_each_list += ["Detect Thoughts", "Locate Object"]
        three_day_each_list += ["Tongues", "Clairvoyance"]
        first_list += ["Identify", "Comprehend Languages", "Find Familiar", "Detect Magic", "Alarm"]
        second_list += ["Detect Thoughts", "Locate Object", "Arcane Lock", "Gentle Repose", "Nystul's Magic Aura"]
        third_list += ["Tongues", "Clairvoyance", "Leomund's Tiny Hut", "Rary's Telepathic Bond", "Sending"]
        fourth_list += ["Leomund's Secret Chest", "Arcane Eye", "Stone Shape", "Fabricate", "Mordenkainen's Private Sanctum"]
        fifth_list += [            "Legend Lore", "Contact Other Plane", "Scrying", "Teleportation Circle", "Rary's Telepathic Bond"]
        sixth_list += [            "True Seeing",            "Find the Path", "Analyze Dweomer", "Guards and Wards", "Create Undead"]
        seventh_list += ["Teleport", "Symbol", "Sequester", "Rary's Telepathic Bond", "Mordenkainen's Sword"]
        eighth_list += [            "Mind Blank", "Antipathy/Sympathy", "Telepathy", "Clone", "Demiplane"]
        ninth_list += [            "Foresight",            "Astral Projection", "Time Stop", "Gate", "Wish"]

    # Shaman
    if background == "Shaman":
        difficulty = Dice(3)  # Full Caster
        cantrips_list += ["Guidance", "Druidcraft", "Spare the Dying", "Resistance", "Produce Flame",                         "Thorn Whip"]
        one_day_each_list += ["Cure Wounds", "Detect Poison and Disease"]
        two_day_each_list += ["Lesser Restoration", "Pass Without Trace"]
        three_day_each_list += ["Dispel Magic", "Speak with Dead"]
        first_list += ["Cure Wounds", "Detect Poison and Disease",                      "Entangle", "Create or Destroy Water", "Fog Cloud",                      "Bane", "Shield Of Faith"]
        second_list += [
            "Lesser Restoration",
            "Pass Without Trace",
            "Flame Blade",
            "Animal Messenger",
            "Heat Metal",
            "Spike Growth",
            ]
        third_list += ["Dispel Magic", "Speak with Dead",                      "Call Lightning", "Water Walk", "Meld into Stone",                      "Conjure Animals", "Plant Growth"]
        fourth_list += ["Divination", "Freedom of Movement", "Stone Shape", "Locate Creature", "Control Water"]
        fifth_list += ["Commune",
                       "Greater Restoration",
                       "Awaken",
                       "Mass Cure Wounds",
                       "Reincarnate"]
        sixth_list += ["Heal", "Find the Path", "Heroes' Feast", "Move Earth", "Create Undead"]
        seventh_list += ["Regenerate", "Etherealness", "Fire Storm", "Resurrection", "Symbol"]
        eighth_list += ["Earthquake", "Control Weather", "Sunburst", "Antipathy/Sympathy", "Animal Shapes"]
        ninth_list += ["True Resurrection", "Storm of Vengeance", "Shapechange", "Foresight", "Astral Projection"]
            
    # Soldier
    if background == "Soldier":
        difficulty = Dice(8) 
        cantrips_list += ["Blade Ward", "True Strike", "Resistance", "Guidance"]
        one_day_each_list += ["Shield", "Heroism"]
        two_day_each_list += ["Magic Weapon",  "Aid"]
        three_day_each_list += ["Protection from Energy", "Haste"]
        first_list += ["Shield", "Heroism", "Cure Wounds", "Expeditious Retreat", "Protection from Evil and Good"]
        second_list += ["Magic Weapon", "Aid", "Enhance Ability", "Blur", "Protection from Poison"]
        third_list += ["Protection from Energy", "Haste", "Dispel Magic", "Revivify", "Crusader's Mantle"]
        fourth_list += ["Death Ward", "Freedom of Movement", "Stoneskin", "Aura of Life", "Aura of Purity"]
        fifth_list += ["Greater Restoration", "Raise Dead", "Destructive Wave", "Flame Strike", "Planar Binding"]
        sixth_list += ["Heal", "Heroes' Feast", "Find the Path", "Contingency", "Create Undead"]
        seventh_list += [            "Resurrection",            "Regenerate",            "Symbol",            "Teleport",            "Conjure Celestial"]
        eighth_list += [            "Holy Aura",            "Antimagic Field",            "Glibness", "Earthquake", "Dominate Monster"]
        ninth_list += ["Mass Heal", "True Resurrection", "Power Word Kill", "Astral Projection", "Gate"]

    # Spy
    if background == "Spy":
        difficulty = Dice(12)  # Quarter-Caster
        cantrips_list += ["Mage Hand", "Message", "Minor Illusion", "Prestidigitation"]
        one_day_each_list += ["Disguise Self", "Charm Person"]
        two_day_each_list += ["Invisibility", "Suggestion"]
        three_day_each_list += ["Clairvoyance", "Sending"]
        first_list += ["Disguise Self", "Charm Person", "Detect Magic", "Feather Fall", "Silent Image"]
        second_list += ["Invisibility", "Suggestion", "Detect Thoughts", "Locate Object", "Alter Self"]
        third_list += ["Clairvoyance", "Sending", "Nondetection", "Dispel Magic", "Tongues"]
        fourth_list += ["Arcane Eye", "Greater Invisibility", "Locate Creature", "Charm Monster", "Divination"]
        fifth_list += ["Scrying", "Modify Memory", "Teleportation Circle", "Legend Lore", "Geas"]
        sixth_list += ["True Seeing", "Find the Path", "Programmed Illusion", "Mass Suggestion", "Contingency"]
        seventh_list += ["Mirage Arcane", "Teleport", "Sequester", "Regenerate", "Symbol"]
        eighth_list += ["Mind Blank", "Dominate Monster", "Telepathy", "Power Word Stun", "Antipathy/Sympathy"]
        ninth_list += ["Foresight", "True Polymorph", "Power Word Kill", "Imprisonment", "Time Stop"]

    # Traveler
    if background == "Traveler":
        difficulty = Dice(8)  # Quarter-Caster
        cantrips_list += ["Druidcraft", "Guidance", "Mage Hand", "Message"]
        one_day_each_list += ["Longstrider", "Goodberry"]
        two_day_each_list += ["Pass without Trace", "Lesser Restoration"]
        three_day_each_list += ["Create Food and Water", "Protection from Energy"]
        first_list += ["Longstrider", "Goodberry", "Cure Wounds", "Alarm", "Detect Poison and Disease"]
        second_list += ["Pass without Trace", "Lesser Restoration", "Find Traps", "Locate Animals or Plants", "Aid"]
        third_list += ["Create Food and Water", "Protection from Energy", "Speak with Plants", "Water Walk", "Beacon of Hope"]
        fourth_list += ["Freedom of Movement", "Locate Creature", "Stone Shape", "Control Water", "Death Ward"]
        fifth_list += ["Commune with Nature", "Greater Restoration", "Teleportation Circle", "Scrying", "Mass Cure Wounds"]
        sixth_list += ["Find the Path", "Wind Walk", "Heal", "Heroes' Feast", "Move Earth"]
        seventh_list += ["Regenerate","Teleport",                        "Mirage Arcane",                        "Resurrection",                "Transport via Plants"]
        eighth_list += ["Control Weather","Earthquake", "Antipathy/Sympathy", "Telepathy", "Holy Aura"]
        ninth_list += ["Storm of Vengeance", "Gate", "Foresight", "True Resurrection", "Mass Heal"]

    # Urchin
    if background == "Urchin":
        difficulty = Dice(10)  
        cantrips_list = ["Mage Hand", "Prestidigitation", "Minor Illusion", "Message"]
        one_day_each_list += ["Disguise Self", "Unseen Servant"]
        two_day_each_list += ["Invisibility", "Pass without Trace"]
        three_day_each_list += ["Nondetection", "Blink"]
        first_list += ["Disguise Self", "Silent Image", "Charm Person", "Sleep", "Expeditious Retreat"]
        second_list += ["Invisibility", "Pass without Trace", "Silence", "Alter Self", "Calm Emotions"]
        third_list += ["Nondetection", "Blink", "Haste", "Clairvoyance", "Leomund's Tiny Hut"]
        fourth_list += ["Greater Invisibility", "Freedom of Movement", "Arcane Eye", "Dimension Door", "Confusion"]
        fifth_list += ["Mislead", "Teleportation Circle", "Modify Memory", "Legend Lore", "Dream"]
        sixth_list += ["True Seeing", "Find the Path", "Programmed Illusion", "Chain Lightning", "Mass Suggestion"]
        seventh_list += ["Mirage Arcane", "Project Image", "Teleport", "Regenerate", "Sequester"]
        eighth_list += ["Mind Blank", "Antipathy/Sympathy", "Maze", "Dominate Monster", "Power Word Stun"]
        ninth_list += ["Foresight", "Power Word Kill", "Time Stop", "Imprisonment", "True Polymorph"]

    # Warrior
    if background == "Warrior":
        difficulty = Dice(8)  
        cantrips_list += ["Blade Ward", "True Strike", "Light", "Resistance"]
        one_day_each_list += ["Shield", "Heroism"]
        two_day_each_list += ["Magic Weapon", "Aid"]
        three_day_each_list += ["Protection from Energy", "Haste"]
        first_list += ["Shield", "Heroism", "Magic Missile", "Cure Wounds", "Thunderwave"]
        second_list += ["Magic Weapon", "Aid", "Blur", "Enlarge/Reduce", "Spiritual Weapon"]
        third_list += ["Protection from Energy", "Haste", "Crusader's Mantle", "Dispel Magic", "Wind Wall"]
        fourth_list += [            "Freedom of Movement", "Stoneskin", "Greater Invisibility", "Death Ward", "Banishment"]
        fifth_list += ["Circle of Power", "Destructive Wave", "Flame Strike", "Geas", "Raise Dead"]
        sixth_list += ["Heal", "Heroes' Feast", "True Seeing", "Find the Path", "Move Earth"]
        seventh_list += ["Resurrection", "Teleport", "Forcecage", "Regenerate", "Symbol"]
        eighth_list += ["Antipathy/Sympathy", "Earthquake", "Holy Aura", "Dominate Monster", "Power Word Stun"]
        ninth_list += ["Mass Heal", "Power Word Heal", "True Resurrection", "Time Stop", "Foresight"]

    # Warlock
    if background == "Warlock":
        difficulty = Dice(2)  
        cantrips_list += [            "Eldritch Blast", "Mage Hand", "Minor Illusion", "Prestidigitation",                         "Thaumaturgy", "Poison Spray"]
        one_day_each_list += ["Armor of Agathys", "Hellish Rebuke"]
        two_day_each_list += ["Summon Lesser Demons", "Summon Greater Demon"]
        three_day_each_list += ["Infernal Calling", "Contact Other Plane"]
        first_list += ["Armor of Agathys", "Hellish Rebuke", "Hex", "Charm Person",                      "Comprehend Languages", "Sanctuary", "Detect Magic", "Bane",                      "Shield", "Magic Missile"]
        second_list += [            "Summon Lesser Demons",           "Darkness",            "Silence",            "Mirror Image",            "Misty Step",            "Suggestion",            "Flaming Sphere",            "Hold Person",            "Blur"]
        third_list += ["Summon Greater Demon", "Counterspell", "Fly","Hypnotic Pattern", "Magic Circle", "Dispel Magic",                      "Clairvoyance", "Fireball"]
        fourth_list += ["Infernal Calling",  "Banishment",                       "Dimension Door",                       "Hallucinatory Terrain",                       "Shadow of Moil",                       "Freedom Of Movement",                       "Divination"]
        fifth_list += ["Contact Other Plane", "Dream", "Enervation", "Hold Monster", "Scrying"]
        sixth_list += ["Arcane Gate", "Circle of Death", "Conjure Fey", "Eyebite", "Flesh to Stone"]
        seventh_list += ["Crown of Stars", "Etherealness", "Finger of Death", "Forcecage", "Plane Shift"]
        eighth_list += ["Demiplane", "Dominate Monster", "Feeblemind", "Glibness", "Power Word Stun"]
        ninth_list += ["Astral Projection", "Foresight", "Imprisonment", "Power Word Kill", "True Polymorph"]

    # Witch
    if background == "Witch":
        difficulty = 1          
        cantrips_list += ["Eldritch Blast", "Mage Hand", "Minor Illusion", "Thaumaturgy"]
        one_day_each_list += ["Hex", "Cure Wounds"]
        two_day_each_list += ["Bane", "Ray of Enfeeblement"]
        three_day_each_list += ["Bestow Curse", "Speak with Dead"]
        first_list += ["Bane", "Cure Wounds", "Identify", "Sleep", "Charm Person", "Ray Of Sickness" ]
        second_list += ["Ray of Enfeeblement", "Detect Thoughts",                        "Hold Person", "Suggestion", "Locate Object"]
        third_list += ["Bestow Curse", "Speak with Dead", "Tongues", "Dispel Magic", "Remove Curse",                      "Counterspell", "Lightning Bolt"]
        fourth_list += [            "Divination", "Locate Creature", "Banishment", "Hallucinatory Terrain","Greater Invisibility", "Phantasmall Killer", "Polymorph"]
        fifth_list += [            "Geas", "Legend Lore", "Scrying", "Contact Other Plane", "Dream"]
        sixth_list += [            "Find the Path", "True Seeing", "Eyebite", "Mass Suggestion", "Flesh to Stone"]
        seventh_list += [            "Divine Word", "Etherealness", "Finger of Death", "Plane Shift", "Regenerate"]
        eighth_list += [            "Demiplane",            "Dominate Monster",            "Feeblemind",            "Glibness",            "Power Word Stun"]
        ninth_list += [            "Astral Projection",            "Foresight", "Imprisonment",            "Power Word Kill",            "True Polymorph"]

## RACES

    # Aberration
    
    if race == "Aberration":
        '''
        if npc.subrace == "Beholder":
            cantrip, _ = add_spell(cantrip, "Rotting Gaze", 3, 0, max_spell_level,
                                   f"The aberration targets one creature it can see within 30 feet of it. The target must succeed on a DC {10+PB(Lvl)} Constitution saving throw against this magic or take 10 (3d6) necrotic damage.")
            cantrip, _ = add_spell(cantrip, "Weird Insight", 4, 0, max_spell_level,
                                   f"The aberration targets one creature it can see within 30 feet of it. The target must contest its Charisma (Deception) check against the aberration's Wisdom (Insight) check. If the aberration wins, it magically learns one fact or secret about the target. The target automatically wins if it is immune to being charmed.")
            cantrip, _ = add_spell(cantrip, "Confusion Ray", 3, 0, max_spell_level,
                                   f"The target must succeed on a DC {10+PB(Lvl)} Wisdom saving throw, or it can't take reactions until the end of its next turn. On its turn, the target can't move, and it uses its action to make a melee or ranged attack against a randomly determined creature within range. If the target can't attack, it does nothing on its turn.")
            cantrip, _ = add_spell(cantrip, "Paralyzing Ray", 4, 0, max_spell_level,
                                   f"The target must succeed on a DC {10+PB(Lvl)} Constitution saving throw or be paralyzed for 1 minute. The target can repeat the saving throw at the start of each of its turns, ending the effect on itself on a success.")
            cantrip, _ = add_spell(cantrip, "Fear Ray", 2, 0, max_spell_level,
                                   f"The target must succeed on a DC {10+PB(Lvl)} Wisdom saving throw or be frightened for 1 minute. The target can repeat the saving throw at the end of each of its turns, with disadvantage if the monstrosity is visible to the target, ending the effect on itself on a success.")
            cantrip, _ = add_spell(cantrip, "Wounding Ray", 2, 0, max_spell_level,
                                   f"The target must make a DC {10+PB(Lvl)} Constitution saving throw, taking 16 (3d10) necrotic damage on a failed save, or half as much damage on a successful one.")
            one, _ = add_spell(one, "Stench Spray", 3, 0, max_spell_level,
                               f"1/Day. The target must make a DC {10+PB(Lvl)} Constitution saving throw, taking 16 (3d10) necrotic damage on a failed save, or half as much damage on a successful one.")
        '''


        # Cantrips
        cantrips_list += ["Eldritch Blast",
                          "Mage Hand",
                          "Minor Illusion",
                          "Thaumaturgy",
                          "Message",
                          ]        
        one_day_each_list += ["Detect Thoughts",
                              "Dissonant Whispers",]        
        two_day_each_list += ["Hold Person",
                              "Levitate",
                              "Crown of Madness",
                             ]
        three_day_each_list += [ "Telekinesis",
                                 "Mind Spike",
                                 "Fear",
                                 "Hypnotic Pattern",
                                 ]
        first_list += ["Detect Magic",
                       "Dissonant Whispers",
                       "Mage Armor",
                       "Shield",
                       "Tasha's Hideous Laughter",
                       "Charm Person",
                       "Illusory Script",
                       ]
        second_list += ["Hold Person",
                        "Mirror Image",
                        "Misty Step",
                        "Detect Thoughts",
                        "Blur",
                        "Crown of Madness",
                        "Phantasmal Force",
                        ]
        third_list += [
            "Counterspell",
            "Dispel Magic",
            "Hypnotic Pattern",
            "Telekinesis",
            "Tongues",
            "Fear",
            "Major Image",
            "Sending",
            "Clairvoyance",
            ]
        fourth_list += [
            "Banishment",
            "Dimension Door",
            "Arcane Eye",
            "Confusion",
            "Greater Invisibility",
            "Phantasmal Killer",
            ]
        fifth_list += [
            "Contact Other Plane",
            "Scrying",
            "Teleportation Circle",
            "Dream",
            "Modify Memory",
            "Dominate Person",
            "Telekinesis",
            "Mislead",
            ]
        sixth_list += [            "True Seeing",            "Arcane Gate",            "Mass Suggestion",   "Plane Shift",
            "Disintegrate",            "Mental Prison",            "Eyebite",            "Programmed Illusion"              ]
        seventh_list += ["Teleport",                        "Etherealness",                        "Project Image",                        "Symbol",                       "Forcecage",
                        "Mirage Arcane",                        "Etherealness",                        "Simulacrum"]        
        eighth_list += ["Feeblemind",                       "Mind Blank",                       "Antipathy/Sympathy",               "Demiplane",                       "Maze",                       "Telepathy",                       "Antimagic Field",                       "Power Word Stun"]
        ninth_list += ["Astral Projection",                    "Foresight",                      "Gate",                      "Imprisonment",                     "Psychic Scream",                      "Power Word Kill",                      "Time Stop",                      "Gate",                      "True Polymorph"]

        
    # Aven
    if race == "Aven":
        '''
        recharge = add_spell(recharge, "Summon Air Elemental", 3, 0,
                               "Five Aven within 30 feet of each other can magically summon an air elemental. Each of the five must use its action and movement on three consecutive turns to perform an aerial dance and must maintain concentration while doing so (as if concentrating on a spell). When all five have finished their third turn of the dance, the elemental appears in an unoccupied space within 60 feet of them. It is friendly toward them and obeys their spoken commands. It remains for 1 hour, until it or all its summoners die, or until any of its summoners dismisses it as a bonus action. A summoner can't perform the dance again until it finishes a short rest. When the elemental returns to the Elemental Plane of Air, any Aven within 5 feet of it can return with it.")
        '''

        cantrips_list += ["Guidance", "Gust", "Mage Hand", "Message"]
        one_day_each_list += [            "Feather Fall", "Jump"]
        two_day_each_list += ["Levitate", "Fly"]
        three_day_each_list += ["Wind Wall", "Gaseous Form"]
        first_list += [            "Feather Fall", "Jump", "Expeditious Retreat", "Longstrider", "Fog Cloud"]
        second_list += [ "Levitate",                    "Fly",     "Gust of Wind",
                    "Skywrite",            "Spider Climb"]
        third_list += ["Wind Wall", "Gaseous Form", "Daylight", "Protection from Energy", "Feign Death"]
        fourth_list += [            "Freedom of Movement", "Control Winds", "Greater Invisibility", "Stone Shape", "Conjure Minor Elementals"]
        fifth_list += [   "Control Winds",            "Telekinesis",            "Commune with Nature",            "Conjure Elemental",            "Passwall"            ]
        sixth_list += ["Wind Walk", "True Seeing", "Chain Lightning", "Move Earth", "Sunbeam"]
        seventh_list += ["Teleport", "Control Weather", "Reverse Gravity", "Whirlwind", "Regenerate"]
        eighth_list += ["Control Weather",                       "Telepathy",
                       "Antipathy/Sympathy",                       "Earthquake",                       "Tsunami"]
        ninth_list += ["Meteor Swarm",                      "Time Stop",
                      "Gate",                      "Shapechange",
                      "Mass Polymorph"]
        
    # BEASTS AND BEASTFOLK
    if race == "Beast":
        '''
        recharge, _ = add_spell(recharge, "Cold Breath", 0,
                               f"(Recharge 5–6). \n\t The beast exhales a blast of freezing wind in a 15-foot cone. Each creature in that area must make a DC {10+PB(Lvl)} Dexterity saving throw, taking 18 (4d8) cold damage on a failed save, or half as much damage on a successful one.")
        '''
        cantrips_list += ["Druidcraft", "Guidance", "Mending", "Resistance"]
        one_day_each_list += ["Animal Friendship", "Speak with Animals"]
        two_day_each_list += ["Barkskin", "Beast Sense"]
        three_day_each_list += ["Conjure Animals","Water Walk"]
        first_list += [            "Cure Wounds",            "Entangle",           "Goodberry",            "Longstrider",             "Speak with Animals"]
        second_list += [           "Animal Messenger",            "Barkskin",            "Darkvision",            "Locate Animals or Plants",            "Pass without Trace"]
        third_list += [            "Beacon of Hope",            "Conjure Animals",            "Daylight",            "Protection from Energy",            "Water Walk"]
        fourth_list += [            "Conjure Minor Elementals",            "Dominate Beast",            "Freedom of Movement",            "Grasping Vine",            "Stoneskin"]
        fifth_list += [            "Awaken",      "Commune with Nature",            "Conjure Elemental",            "Greater Restoration",            "Reincarnate"]
        sixth_list += [            "Find the Path",            "Heal",            "Heroes' Feast",            "Move Earth",            "Transport via Plants"]
        seventh_list += ["Mirage Arcane", "Plane Shift", "Regenerate", "Reverse Gravity", "Whirlwind"]
        eighth_list += ["Animal Shapes", "Antipathy/Sympathy", "Control Weather", "Earthquake", "Tsunami"]
        ninth_list += ["Foresight", "Shapechange", "Storm of Vengeance", "True Resurrection", "Mass Heal"]

        if Dice(12)==1:
            recharge += "\n-Web (Recharge 6)"


    if race == "Beastfolk":
        cantrips_list += ["Druidcraft", "Guidance", "Resistance", "Shillelagh","Poison Spray", "Dancing Lights", "Feather Fall", "Thaumaturgy","Mage Hand", "Sacred Flame", "Sleep Gaze"]
        one_day_each_list += ["Animal Friendship", "Speak with Animals", "Longstrider", "Invisibility","Darkness", "Mirror Image", "Heat Metal", "Enlarge/Reduce", "Cure Wounds"]
        two_day_each_list += ["Barkskin", "Enhance Ability", "Find Traps", "Magic Weapon", "Blur"]
        three_day_each_list += ["Beast Sense", "Conjure Animals", "Dispel Magic"]
        first_list += [         "Cure Wounds", "Detect Magic", "Entangle", "Goodberry", "Healing Word", "Faerie Fire"]
        second_list += ["Animal Messenger", "Flame Blade", "Moonbeam", "Pass without Trace", "Spike Growth"]
        third_list += [            "Call Lightning", "Create Food and Water", "Cure Wounds (3rd level)", "Protection from Energy", "Water Walk"]
        fourth_list += ["Conjure Minor Elementals", "Control Water", "Freedom of Movement", "Locate Creature", "Stoneskin"]
        fifth_list += ["Awaken",                      "Commune with Nature","Conjure Elemental",                      "Greater Restoration",                      "Mass Cure Wounds"]
        sixth_list += ["Find the Path", "Heal", "Heroes' Feast", "Move Earth", "Transport via Plants"]
        seventh_list += ["Mirage Arcane", "Plane Shift", "Regenerate", "Reverse Gravity", "Whirlwind"]
        eighth_list += ["Animal Shapes", "Antipathy/Sympathy", "Control Weather", "Earthquake", "Tsunami"]
        ninth_list += ["Foresight", "Shapechange", "Storm of Vengeance", "True Resurrection", "Mass Heal"]
    
    # CELESTIALS.
    if race == "Celestial":
        cantrips_list += [            "Guidance",            "Light", "Mending", "Sacred Flame", "Thaumaturgy", "Druidcraft"]
        one_day_each_list += ["Cure Wounds",                             "Bless",
                             "Detect Evil and Good",                             "Teleport",
                             "Entangle",                             "Calm Emotions",
                             "Scrying",                             "Greater Restoration",                             "Dream"]
        two_day_each_list += ["Lesser Restoration",                             "Aid",                             "Zone of Truth"]
        three_day_each_list += ["Remove Curse",                               "Dispel Magic",
                               "Revivify",                               "Healing Touch",
                               "Shield",                               "Sanctuary",
                               "Protection From Poison",                               "Lesser Restoration",
                               "Create Food And Water",                               "Cure Wounds",
                               "Bless",                               "Detect Magic",                               "Detect Thoughts"]
        first_list += ["Detect Magic", "Healing Word", "Protection from Evil and Good", "Purify Food and Drink", "Shield of Faith"]
        second_list += ["Enhance Ability", "Find Traps", "Hold Person", "Prayer of Healing", "Warding Bond"]
        third_list += ["Daylight", "Protection from Energy", "Remove Curse", "Speak with Dead", "Spirit Guardians"]
        fourth_list += ["Death Ward",                       "Freedom of Movement",
                       "Guardian of Faith",                       "Locate Creature",
                       "Stoneskin"]
        fifth_list += ["Flame Strike",               "Geas",
                       "Greater Restoration", "Hallow", "Raise Dead"]
        sixth_list += ["Blade Barrier", "Find the Path", "Heal", "Heroes' Feast", "Planar Ally"]
        seventh_list += ["Etherealness", "Regenerate", "Resurrection", "Symbol", "Teleport"]
        eighth_list += ["Antimagic Field", "Control Weather", "Holy Aura", "Sunburst", "Telepathy"]
        ninth_list += ["Astral Projection", "Gate", "Mass Heal", "Power Word Heal", "True Resurrection"]

    # CONSTRUCTS.
    if race == "Construct":
        '''
        recharge, _ = add_spell(recharge, "Paralysis Gas", 4, 0, max_spell_level,
                               f"(Recharge 5–6). \n\t The construct exhales a 30-foot cone of gas. Each creature in that area must succeed on a DC {10+PB(Lvl)} Constitution saving throw or be paralyzed for 1 minute. A creature can repeat the saving throw at the start of each of its turns, ending the effect on itself on a success.")
        '''

        cantrips_list += ["Guidance", "Mage Hand", "Mending", "Prestidigitation", "Light"]
        one_day_each_list += ["Alarm", "Cure Wounds", "Grease"]
        two_day_each_list += ["Darkvision", "Enhance Ability", "Heat Metal"]
        three_day_each_list += ["Counterspell", "Dispel Magic", "Protection from Energy"]
        first_list += ["Alarm", "Cure Wounds", "Identify", "Shield", "Unseen Servant"]
        second_list += ["Darkvision", "Enhance Ability", "Heat Metal", "Levitate", "Magic Weapon"]
        third_list += ["Counterspell", "Dispel Magic", "Protection from Energy", "Tiny Servant", "Water Walk"]
        fourth_list += ["Death Ward", "Fabricate", "Stone Shape", "Stone Skin", "Control Water"]
        fifth_list += ["Animate Objects", "Creation", "Greater Restoration", "Teleportation Circle", "Wall of Stone"]
        sixth_list += ["Find the Path", "Move Earth", "True Seeing", "Wall of Ice", "Programmed Illusion"]
        seventh_list += ["Forcecage", "Mordenkainen's Magnificent Mansion", "Teleport", "Regenerate", "Resurrection"]
        eighth_list += ["Antimagic Field",                        "Control Weather",                        "Demiplane", "Mind Blank", "Telepathy"]
        ninth_list += ["Gate", "Imprisonment", "Mass Heal", "Meteor Swarm", "True Resurrection"]

    # DRAGONS.

    #Breath weapons
    if race == "Dragon" and Dice(3) == 1:
        d = 20
        if Dice(d) == 1 and not ("Fire Breath" in recharge):
            recharge += [f"\n  - Fire Breath \n\t(Recharge 5-6) The dragon exhales fire in a 20-foot line that is 5 feet wide. Each creature in that line must make a DC {10+PB(Lvl)} Dexterity saving throw, taking 14 (4d6) fire damage on a failed save, or half as much damage on a successful one."]
        elif Dice(d) == 1 and not ("Fire Breath" in recharge):
            recharge += [f"\n  - Fire Breath \n\t(Recharge 5-6) The dragon exhales fire in a 15-foot cone. Each creature in that area must make a DC {10+PB(Lvl)} Dexterity saving throw, taking 22 (4d10) fire damage on a failed save, or half as much damage on a successful one."]
        elif Dice(d) == 1 and not ("Fire Breath" in recharge):       recharge += [f"\n  - Fire Breath \n\t(Recharge 5-6) The dragon exhales fire in a 15-foot cone. Each creature in that area must make a DC {10+PB(Lvl)} Dexterity saving throw, taking 24 (7d6) fire damage on a failed save, or half as much damage on a successful one."]
        if Dice(d) == 2 and not ("Sleep Breath" in recharge):        recharge += [f"\n  - Sleep Breath \n\t(Recharge 5-6) The dragon exhales sleep gas in a 15-foot cone. Each creature in that area must succeed on a DC {10+PB(Lvl)} Constitution saving throw or fall unconscious for 1 minute. This effect ends for a creature if the creature takes damage or someone uses an action to wake it."]
        if Dice(d) == 3 and not ("Acid Breath" in recharge):         recharge += [f"\n  - Acid Breath \n\t(Recharge 5-6) The dragon exhales acid in a 20-foot line that is 5 feet wide. Each creature in that line must make a DC {10+PB(Lvl)} Dexterity saving throw, taking 18 (4d8) acid damage on a failed save, or half as much damage on a successful one"]
        if Dice(d) == 4 and not ("Slowing Breath" in recharge):      recharge += [f"\n  - Slowing Breath \n\t(Recharge 5-6) The dragon exhales gas in a 15-foot cone. Each creature in that area must succeed on a DC {10+PB(Lvl)} Constitution saving throw. On a failed save, the creature can't use reactions, its speed is halved, and it can't make more than one attack on its turn. In addition, the creature can use either an action or a bonus action on its turn, but not both. These effects last for 1 minute. The creature can repeat the saving throw at the start of each of its turns, ending the effect on itself with a successful save."]
        if Dice(d) == 5 and not ("Euphoria Breath" in recharge):     recharge += [f"\n  - Euphoria Breath \n\t(Recharge 5-6) The dragon exhales a puff of euphoria gas at one creature within 5 feet of it. The target must succeed on a DC {10+PB(Lvl)} Wisdom saving throw, or for 1 minute, the target can't take reactions and must roll a d6 at the start of each of its turns to determine its behavior during the turn: \n\t\t 1–4. The target takes no action or bonus action and uses all of its movement to move in a random direction. \n\t\t 5–6. The target doesn't move, and the only thing it can do on its turn is make a DC {10+PB(Lvl)} Wisdom saving throw, ending the effect on itself on a success."]
        if Dice(d) == 6 and not ("Repulsion Breath" in recharge):    recharge += [f"\n  - Repulsion Breath \n\t(Recharge 5-6) The dragon exhales repulsion energy in a 30-foot cone. Each creature in that area must succeed on a DC {10+PB(Lvl)} Strength saving throw. On a failed save, the creature is pushed 30 feet away from the dragon."]
        if Dice(d) == 7 and not ("Poison Breath" in recharge):       recharge += [f"\n  - Poison Breath \n\t(Recharge 5-6) The dragon exhales poisonous gas in a 15-foot cone. Each creature in that area must make a DC {10+PB(Lvl)} Constitution saving throw, taking 21 (6d6) poison damage on a failed save, or half as much damage on a successful one."]
        if Dice(d) == 8 and not ("Lightning Breath" in recharge):    recharge += [f"\n  - Lightning Breath \n\t(Recharge 5-6) The dragon exhales lightning in a 40-foot line that is 5 feet wide. Each creature in that line must make a DC {10+PB(Lvl)} Dexterity saving throw, taking 16 (3d10) lightning damage on a failed save, or half as much damage on a successful one."]
        elif Dice(d) == 8 and not ("Lightning Breath" in recharge):  recharge += [f"\n  - Lightning Breath \n\t(Recharge 5-6) The dragon exhales lightning in a 30-foot line that is 5 feet wide. Each creature in that line must make a DC {10+PB(Lvl)} Dexterity saving throw, taking 22 (4d10) lightning damage on a failed save, or half as much damage on a successful one."]
        if Dice(d) == 9 and not ("Cold Breath" in recharge):         recharge += [f"\n  - Cold Breath \n\t(Recharge 5-6) The dragon exhales an icy blast in a 15-foot cone. Each creature in that area must make a DC {10+PB(Lvl)} Constitution saving throw, taking 18 (4d8) cold damage on a failed save, or half as much damage on a successful one."]
        elif Dice(d) == 10 and not ("Cold Breath" in recharge):      recharge += [f"\n  - Cold Breath \n\t(Recharge 5-6) The dragon exhales an icy blast in a 15-foot cone. Each creature in that area must make a DC {10+PB(Lvl)} Constitution saving throw, taking 22 (5d8) cold damage on a failed save, or half as much damage on a successful one."]
        if Dice(d) == 11 and not ("Paralyzing Breath" in recharge):  recharge += [f"\n  - Paralyzing Breath \n\t(Recharge 5-6) The dragon exhales paralyzing gas in a 15-foot cone. Each creature in that area must succeed on a {10+PB(Lvl)} Constitution saving throw or be paralyzed for 1 minute. A creature can repeat the saving throw at the start of each of its turns, ending the effect on itself on a success."]
        if Dice(d) == 12 and not ("WeakeningBreath" in recharge):    recharge += [f"\n  - Weakening Breath \n\t(Recharge 5-6) The dragon exhales gas in a 15-foot cone. Each creature in that area must succeed on a DC {10+PB(Lvl)} Strength saving throw or have disadvantage on Strength-based attack rolls, Strength checks, and Strength saving throws for 1 minute. A creature can repeat the saving throw at the start of each of its turns, ending the effect on itself on a success."]

    if race == "Dragon" and Dice(12) == 1 and not ("Change Shape" in recharge):  recharge += ["\n- Change Shape \n\t The dragon magically polymorphs into a humanoid or beast that has a challenge rating no higher than its own, or back into its true form. It reverts to its true form if it dies. Any equipment it is wearing or carrying is absorbed or borne by the new form (the dragon's choice).In a new form, the dragon retains its alignment, hit points, Hit Dice, ability to speak, proficiencies, Legendary Resistance, lair actions, and Intelligence, Wisdom, and Charisma scores, as well as this action. Its statistics and capabilities are otherwise replaced by those of the new form, except any class features or legendary actions of that form."]

    if race == "Dragon":
        cantrips_list += ["Control Flames", "Gust", "Mage Hand", "Minor Illusion", "Dancing Lights", "Color Spray" ]
        one_day_each_list += ["Charm Person", "Fear", "Shield"]
        two_day_each_list += ["Flame Strike", "Fly", "Invisibility"]
        three_day_each_list += ["Fireball", "Protection from Energy", "Wind Walk"]
        first_list += ["Charm Person", "Detect Magic", "Mage Armor", "Magic Missile", "Shield", "Suggestion", "Polymorph", "Mirror Image", "Major Image"]
        second_list += ["Darkness", "Flaming Sphere", "Hold Person", "Invisibility", "Mirror Image"]
        third_list += ["Fear", "Fireball", "Fly", "Haste", "Protection from Energy"]
        fourth_list += ["Charm Monster", "Control Flames", "Greater Invisibility", "Wall of Fire", "Stone Shape"]
        fifth_list += ["Dominate Person", "Flame Strike", "Geas", "Hold Monster", "Teleportation Circle"]
        sixth_list += ["Chain Lightning",                      "Disintegrate",
                      "Move Earth",                      "True Seeing",
                      "Sunburst"]
        seventh_list += [            "Fire Storm",
            "Plane Shift", "Reverse Gravity", "Teleport", "Prismatic Spray"]
        eighth_list += [            "Control Weather", "Earthquake", "Incendiary Cloud", "Telepathy", "Sunburst"]
        ninth_list += ["Gate",
                      "Imprisonment",
                      "Meteor Swarm",
                      "Power Word Kill",                      "Time Stop"]

    # DWARF.

    if race == "Dwarf":
        cantrips_list += ["Blade Ward",
                         "Mending",
                         "Resistance",
                         "Stone Fist"]
        one_day_each_list += ["Shield of Faith",
                             "Compelled Duel",
                             "Searing Smite",
                             "Invisibility"]
        two_day_each_list += ["Enlarge/Reduce",
                             "Magic Weapon",
                             "Shatter"]
        three_day_each_list += ["Meld into Stone", "Protection from Energy", "Stone Shape"]
        first_list += ["Bless", "Command", "Cure Wounds", "Shield of Faith", "Thunderous Smite"]
        second_list += ["Aid", "Find Traps", "Magic Weapon", "Spike Growth", "Stone Fist"]
        third_list += ["Crusader's Mantle", "Elemental Weapon", "Meld into Stone", "Protection from Energy", "Remove Curse"]
        fourth_list += ["Fabricate", "Guardian of Nature", "Stone Shape", "Stoneskin", "Wall of Fire"]
        fifth_list += ["Destructive Wave", "Geas", "Greater Restoration", "Passwall", "Wall of Stone"]
        sixth_list += ["Find the Path", "Heal", "Heroes' Feast", "Move Earth", "True Seeing"]
        seventh_list += ["Etherealness", "Regenerate", "Resurrection", "Symbol", "Teleport"]
        eighth_list += ["Antimagic Field", "Earthquake", "Holy Aura", "Telepathy", "Incendiary Cloud"]
        ninth_list += ["Foresight", "Imprisonment", "Mass Heal", "Power Word Heal", "True Resurrection"]

        
    # ELEMENTAL.
    if race == "Elemental":
        cantrips_list += ["Control Flames", "Gust", "Mold Earth", "Shape Water", "Dancing lights"]
        """
        recharge, _ = add_spell(recharge, "Whirlwind", 0, 
                                f" (Recharge 4–6)."+
                                f"\t Each creature in the {race}'s space must make a Strength saving throw. " +
                                f"On a failure, a target takes 15 (3d8 + 2) bludgeoning damage and is flung up 20 feet away from the {race} in a random direction and knocked prone. " +
                                f"If a thrown target strikes an object, such as a wall or floor, the target takes 3 (1d6) bludgeoning damage for every 10 feet it was thrown. "  +
                                f"If the target is thrown at another creature, that creature must succeed on a Dexterity Saving Throw or take the same damage and be knocked prone. " +
                                f"/n/t If the saving throw is successful, the target takes half the bludgeoning damage and isn't flung away or knocked prone. ")

        recharge, _ = add_spell(recharge, "Cinder breath", 0,
                                f"\t (Recharge 6). The Elemental exhales a 15-foot cone of smoldering ash. Each creature in that area must succeed on a DC [10+%Cha] Dexterity saving throw or be blinded until the end of the Elemental's next turn.")

        recharge, _ = add_spell(recharge, "Blinding breath", 0, 
                               f"\t (Recharge 6). The Elemental exhales a 15-foot cone of blinding dust. Each creature in that area must succeed on a Dexterity saving throw or be blinded for one minute.")

        recharge, _ = add_spell(recharge, "Steam breath", 0, 0,
                                f"\t (Recharge 6). The Elemental exhales a 15-foot cone of scalding steam. Each creature in that area must succeed on a Dexterity saving throw, taking 4 (1d8) fire damage on a failed save, or half as much damage on a successful one.")

        recharge, _ = add_spell(recharge, "Frost Breath", 0, 0,
                                f"\t (Recharge 6). The Elemental exhales a 15-foot cone of cold air. Each creature in that area must succeed on a Dexterity saving throw, taking 5 (2d4) cold damage on a failed save, or half as much damage on a successful one.")

        recharge, _ = add_spell(recharge, "Fire Breath", 0, 0,
                               "\t (Recharge 6). The Elemental exhales a 15-foot cone of cold air. Each creature in that area must succeed on a Dexterity saving throw, taking 7 (2d6) fire damage on a failed save, or half as much damage on a successful one.")
        """
        one_day_each_list += ["Burning Hands", "Earth Tremor", "Ice Knife"]
        two_day_each_list += ["Dust Devil", "Flame Blade", "Misty Step"]
        three_day_each_list += ["Elemental Weapon", "Gaseous Form", "Wind Wall"]
        first_list += ["Absorb Elements", "Earth Tremor", "Fog Cloud", "Ice Knife", "Thunderwave"]
        second_list += ["Dust Devil", "Flame Blade", "Gust of Wind", "Melf's Acid Arrow", "Snilloc's Snowball Swarm"]
        third_list += ["Erupting Earth", "Flame Arrows", "Melf's Minute Meteors", "Tidal Wave", "Wind Wall"]
        fourth_list += ["Control Water", "Elemental Bane", "Storm Sphere", "Watery Sphere", "Fire Shield"]
        fifth_list += ["Control Winds", "Flame Strike", "Immolation", "Maelstrom", "Transmute Rock"]
        sixth_list += ["Chain Lightning", "Investiture of Flame", "Investiture of Ice", "Investiture of Stone", "Investiture of Wind"]
        seventh_list += ["Fire Storm", "Prismatic Spray", "Whirlwind", "Plane Shift", "Teleport"]
        eighth_list += ["Earthquake",            "Incendiary Cloud", "Sunburst", "Tsunami", "Control Weather"]
        ninth_list += [            "Meteor Swarm", "Storm of Vengeance", "Tsunami", "Gate", "Prismatic Wall"]
        '''
        recharge, _ = add_spell(recharge, "Summon Mephits", max_spell_level-3, 0, max_spell_level,
                                  "(recharge 6):\t The Elemental has a 25 percent chance of summoning 1d4 mephits. A summoned mephit appears in an unoccupied space within 60 feet of its summoner, acts as an ally of its summoner, and can't summon other mephits. It remains for 1 minute, until it or its summoner dies, or until its summoner dismisses it as an action.")
        one, _ = add_spell(one, "Innate Spellcasting", max_spell_level-3, 0, max_spell_level,
                           "The Elemental can innately cast fog cloud, requiring no material components")

        one, _ = add_spell(one, "Innate Spellcasting", max_spell_level-3, 0, max_spell_level,
                 "\tThe Elemental can innately cast heat metal, requiring no material components.")

        one, _ = add_spell(one, "Blur", max_spell_level-3,0, max_spell_level,)
        one, _ = add_spell(one, "Sleep", max_spell_level-3, 0, max_spell_level,)
        '''
    # ELF.
    if "Elf" in npc.race:
        cantrips_list += ["Dancing Lights", "Druidcraft", "Mage Hand", "Minor Illusion"]
        one_day_each_list += ["Charm Person", "Disguise Self", "Sleep", "Darkness", "Faerie Fire", "Levitate"]
        two_day_each_list += [            "Detect Thoughts",            "Invisibility",            "Mirror Image"]
        three_day_each_list += [            "Counterspell",            "Feather Fall",            "Protection from Energy"]
        first_list += ["Charm Person", "Detect Magic", "Fog Cloud", "Goodberry", "Healing Word"]
        second_list += ["Barkskin", "Darkvision", "Enhance Ability", "Pass without Trace", "Silence"]
        third_list += ["Dispel Magic", "Protection from Energy", "Remove Curse", "Speak with Dead", "Water Breathing"]
        fourth_list += ["Dimension Door", "Freedom of Movement", "Greater Invisibility", "Hallucinatory Terrain", "Locate Creature"]
        fifth_list += ["Awaken", "Commune with Nature", "Mislead", "Modify Memory", "Teleportation Circle"]
        sixth_list += ["Find the Path", "Heal", "Heroes' Feast", "Transport via Plants", "True Seeing"]
        seventh_list += ["Etherealness", "Mirage Arcane", "Plane Shift", "Regenerate", "Teleport"]
        eighth_list += ["Antipathy/Sympathy", "Earthquake", "Incendiary Cloud", "Mind Blank", "Power Word Stun"]
        ninth_list += ["Foresight", "Mass Heal", "Power Word Heal", "Shapechange", "Time Stop"]

        if "Urban" in npc.subrace:
            cantrips_list += ["Mage Hand", "Prestidigitation", "Minor Illusion", "Message"]
            one_day_each_list += ["Charm Person", "Disguise Self", "Silent Image", "Sleep"]
            two_day_each_list += ["Invisibility", "Misty Step", "Nondetection"]
            three_day_each_list += ["Major Image", "Leomund's Tiny Hut", "Counterspell"]
            first_list += ["Detect Magic", "Feather Fall", "Sleep", "Tasha's Hideous Laughter", "Unseen Servant"]
            second_list += ["Arcane Lock", "Darkness", "Knock", "Silence", "Spider Climb"]
            third_list += ["Clairvoyance", "Nondetection", "Tongues", "Dispel Magic", "Hypnotic Pattern"]
            fourth_list += ["Dimension Door", "Greater Invisibility", "Arcane Eye", "Leomund's Secret Chest", "Freedom of Movement"]
            fifth_list += ["Mislead", "Passwall", "Teleportation Circle", "Modify Memory", "Seeming"]
            sixth_list += ["Programmed Illusion", "True Seeing", "Mass Suggestion", "Find the Path", "Guards and Wards"]
            seventh_list += ["Mirage Arcane", "Project Image", "Etherealness", "Teleport", "Sequester"]
            eighth_list += ["Antimagic Field", "Mind Blank", "Demiplane", "Maze", "Dominate Monster"]
            ninth_list += ["Foresight", "Time Stop", "Astral Projection", "Imprisonment", "True Polymorph"]

    # FAE.
    
    if race == "Fey" and Dice(8) == 1 and not ("Ethereal Jaunt" in recharge):
        recharge += ["\n- Ethereal Jaunt (Recharge 6):\n\t As a bonus action, the fey can magically shift from the Material Plane to the Ethereal Plane, or vice versa."]
    if race == "Fey" and Dice(10) == 1 and not ("Teleport" in recharge):
        recharge += ["\n- Teleport (Recharge 4–6). \n\t The Fey magically teleports, along with any equipment it is wearing or carrying, up to 40 feet to an unoccupied space it can see. Before or after teleporting, the Fey can make one bite attack."]
    if race == "Fey" and Dice(10) == 1 and not ("Heart Sight" in recharge):
        recharge += ["\n- Heart Sight. (Recharge 6)\n\t The Fey touches a creature and magically knows the creature's current emotional state. If the target fails a DC [10+%Cha] Charisma saving throw, the Fey also knows the creature's alignment. Celestials, fiends, and undead automatically fail the saving throw."]
    if race == "Fey" and Dice(10) == 1 and not ("Invisibility" in recharge):
        recharge += ["\n- Invisibility. (Recharge 6)\n\t The Fey  magically turns invisible until it attacks or casts a spell, or until its concentration ends (as if concentrating on a spell). Any equipment the Fey wears or carries is invisible with it."]
    if race == "Fey" and Dice(8) == 1 and not ("Change Shape" in recharge):
        recharge += ["\n- Change Shape. (Recharge 6)\n\t The fey magically polymorphs into a Small or Medium humanoid, or back into their true form. Their statistics are the same in each form. Any equipment they are wearing or carrying isn't transformed. They reverts to their true form if they dies."]
    if race == "Fey" and Dice() == 1 and not ("Etherealness" in recharge):
        recharge += ["\n- Etherealness. (Recharge 6)\n\t The fey magically enters the Ethereal Plane from the Material Plane, or vice versa. To do so, the fey must have a heartstone in her possession."]



    if race == "Fey" and Dice(8) == 1 and not ("Charming Melody" in one_day_each_list):       one_day_each_list += "\n- Charming Melody [DC 10+%Cha Wisdom saving throw]\n\t The creature is charmed by the Fey for 1 minute. If the Fey or any of its companions harms the creature, the effect on it ends immediately."
    if race == "Fey" and Dice(8) == 1 and not ("Frightening Strain" in one_day_each_list):    one_day_each_list += "\n- Frightening Strain [DC 10+%Cha Wisdom saving throw] \n\t The creature is charmed by the Fey for 1 minute. If the Fey or any of its companions harms the creature, the effect on it ends immediately."
    if race == "Fey" and Dice(8) == 1 and not ("Gentle Lullaby" in one_day_each_list):        one_day_each_list += "\n- Gentle Lullaby [DC 10+%Cha Wisdom saving throw] \n\t The creature falls asleep and is unconscious for 1 minute. The effect ends if the creature takes damage or if someone takes an action to shake the creature awake."
    if race == "Fey" and Dice(8) == 1 and not ("Nightmare Haunting" in one_day_each_list):    one_day_each_list += "\n- Nightmare Haunting \n\t While on the Ethereal Plane, the fey magically touches a sleeping humanoid on the Material Plane. A protection from evil and good spell cast on the target prevents this contact, as does a magic circle. As long as the contact persists, the target has dreadful visions. If these visions last for at least 1 hour, the target gains no benefit from its rest, and its hit point maximum is reduced by 5 (1d10). If this effect reduces the target's hit point maximum to 0, the target dies, and if the target was evil, its soul is trapped in the fey's soul bag. The reduction to the target's hit point maximum lasts until removed by the greater restoration spell or similar magic."

        
    if race == "Fey":
        cantrips_list += ["Dancing Lights",
                         "Druidcraft",
                         "Minor Illusion",
                         "Prestidigitation",
                         "Shillelagh",
                         "Vicious Mockery"]

        one_day_each_list += ["Charm Person",
                             "Entangle",
                             "Sleep",
                             "Polymorph",
                             "Sleep",
                             "Phantasmal Force",
                             "Entangle",
                             "Dispel Magic",
                             "Detect Thoughts",
                             "Detect Evil and Good",
                             "Confusion",
                             "Pass Without Trace"]

        two_day_each_list += ["Invisibility",
                             "Mirror Image",
                             "Suggestion",
                             "Sleep",
                             "Ray Of Enfeeblement",
                             "Plane Shift"]

        three_day_each_list += ["Blink", "Confusion", "Dispel Magic", "Goodberry", "Entangle", "Barkskin", "Detect Magic"]
        first_list += ["Charm Person", "Detect Magic", "Entangle", "Faerie Fire", "Healing Word"]
        second_list += ["Calm Emotions", "Enthrall", "Hold Person", "Misty Step", "Moonbeam"]
        third_list += ["Dispel Magic", "Plant Growth", "Protection from Energy", "Sleet Storm", "Speak with Plants"]
        fourth_list += ["Confusion", "Dimension Door", "Greater Invisibility", "Hallucinatory Terrain", "Polymorph"]
        fifth_list += ["Awaken", "Dominate Person", "Dream", "Geas", "Mislead"]
        sixth_list += ["Eyebite", "Find the Path", "Mass Suggestion", "Transport via Plants", "True Seeing"]
        seventh_list += ["Etherealness", "Mirage Arcane", "Plane Shift", "Regenerate", "Teleport"]
        eighth_list += ["Antipathy/Sympathy", "Dominate Monster", "Feeblemind", "Incendiary Cloud", "Power Word Stun"]
        ninth_list += ["Foresight", "Mass Heal", "Power Word Heal", "Shapechange", "Time Stop"]


    # FIENDS.
    # Cantrips and at-will magic
    '''
    if race == "Fiend":
        if Dice()==1 and not ("Charm" in cantrip):
            if Dice(2)==1:  cantrip += "\n- Charm \n\t One humanoid the fiend can see within 30 feet of it must succeed on a DC [10+%CHA] Wisdom saving throw or be magically charmed for 1 day. The charmed target obeys the fiend's verbal or telepathic commands. If the target suffers any harm or receives a suicidal command, it can repeat the saving throw, ending the effect on a success. If the target successfully saves against the effect, or if the effect on it ends, the target is immune to this fiend's Charm for the next 24 hours. \n\t The fiend can have only one target charmed at a time. If it charms another, the effect on the previous target ends. "
            else:           cantrip += "\n- Fiendish Charm. \n\t One humanoid the fiend can see within 30 feet of it must succeed on a DC [11+%CHA] Wisdom saving throw or be magically charmed for 1 day. The charmed target obeys the fiend's spoken commands. If the target suffers any harm from the fiend or another creature or receives a suicidal command from the fiend, the target can repeat the saving throw, ending the effect on itself on a success. If a target's saving throw is successful, or if the effect ends for it, the creature is immune to the fiend's Fiendish Charm for the next 24 hours."
            if Dice()==1 and not ("Draining Kiss" in cantrip):      cantrip += "\n- Draining Kiss \t The fiend kisses a creature charmed by it or a willing creature. The target must make a DC 15 Constitution saving throw against this magic, taking 32 (5d10 + 5) psychic damage on a failed save, or half as much damage on a successful one. The target's hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0. "
            if Dice()==1 and not ("Telepathic Bond" in cantrip):    cantrip += "\n- Telepathic Bond. \t The fiend ignores the range restriction on its telepathy when communicating with a creature it has charmed. The two don't even need to be on the same plane of existence."

        if Dice() == 1 and not ("Etherealness" in cantrip):         cantrip += "\n- Etherealness.\t The fiend magically enters the Ethereal Plane from the Material Plane, or vice versa."
        if Dice() == 1 and not ("Fire Breath" in cantrip):          cantrip += "\n- Fire Breath (Recharge 5-6).\t The fiend exhales fire in a 15-foot cone. Each creature in that area must make a DC [10+%CON] Dexterity saving throw, taking 21 (6d6) fire damage on a failed save, or half as much damage on a successful one."
        if Dice() == 1 and not ("Fire Ray" in cantrip):             cantrip += "\n- Fire Ray \t Ranged Spell Attack. Range 120ft. One target. Hit: 10(3d6) fire damage."
    '''
    # Once a day
    '''
    if race == "Fiend":
        if Dice() == 1 and not ("Scare" in one):            one += "\n- Scare \n\t One creature of the Fiend's choice within 20 feet of it must succeed on a DC 10 Wisdom saving throw or be frightened for 1 minute. The target can repeat the saving throw at the begguining of each of its turns, with disadvantage if the Fiend is within line of sight, ending the effect on itself on a success."
        if Dice() == 1 and not ("Fetid Cloud" in one):      one += "\n- Fetid Cloud.\n\t A 10-foot radius of disgusting sulfuric gas extends out from the Fiend. The gas spreads around corners, and its area is lightly obscured. It lasts for 1 minute or until a strong wind disperses it. Any creature that starts its turn in that area must succeed on a DC 11 Constitution saving throw or be poisoned until the start of its next turn. While poisoned in this way, the target can take either an action or a bonus action on its turn, not both, and can't take reactions."
        if Dice() == 1 and not ("Summon Yugoloth" in one):  one += "\n- Summon Yugoloth. \n\t The fiend attempts a magical summoning. \n\t A fiend has a 30 percent chance of summoning one mezzoloth. \n\t A summoned yugoloth appears in an unoccupied space within 60 feet of its summoner, does as it pleases, and can't summon other yugoloths. The summoned yugoloth remains for 1 minute, until it or its summoner dies, or until its summoner takes a bonus action to dismiss it."
    '''       
        
    if race == "Fiend":

        cantrips_list += ["Eldritch Blast","Fire Bolt","Minor Illusion","Thaumaturgy"]
        one_day_each_list += ["Hellish Rebuke", "Inflict Wounds", "Dispel Magic", "Disguise Self", "Cloudkill", "Plane Shift", "Phantasmal Force" ]
        two_day_each_list += ["Darkness", "Scorching Ray", "Suggestion", "Alter Self", "Invisibility"]
        three_day_each_list += ["Fireball", "Vampiric Touch", "Fear", "Detect Magic", "Command", "Entangle"]
        first_list += ["Burning Hands", "Charm Person", "Command", "Hellish Rebuke", "Inflict Wounds"]
        second_list += ["Blindness/Deafness", "Darkness", "Hold Person", "Ray of Enfeeblement", "Scorching Ray"]
        third_list += ["Animate Dead", "Bestow Curse", "Fear", "Fireball", "Vampiric Touch"]
        fourth_list += ["Blight", "Dimension Door", "Fire Shield", "Wall of Fire", "Phantasmal Killer"]
        fifth_list += ["Flame Strike", "Infernal Calling", "Dominate Person", "Hold Monster", "Geas"]
        sixth_list += ["Chain Lightning", "Circle of Death", "Create Undead", "Eyebite", "True Seeing"]
        seventh_list += ["Finger of Death", "Fire Storm", "Plane Shift", "Power Word Pain", "Symbol"]
        eighth_list += ["Demiplane", "Dominate Monster", "Incendiary Cloud", "Power Word Stun", "Sunburst"]
        ninth_list += ["Gate", "Imprisonment", "Meteor Swarm", "Power Word Kill", "True Polymorph"]

    # GIANT.
    if race == "Giant":
        # Cantrips
        cantrips_list += [
            "Gust",
            "Mold Earth",
            "Thunderclap",
            "Magic Stone"]
        one_day_each_list += ["Enlarge/Reduce", "Earth Tremor", "Thunderwave"]
        two_day_each_list += ["Gust of Wind", "Spike Growth", "Warding Wind"]
        three_day_each_list += ["Erupting Earth", "Meld into Stone", "Wind Wall"]
        first_list += ["Earth Tremor", "Entangle", "Longstrider", "Shield of Faith", "Thunderwave"]
        second_list += ["Enlarge/Reduce", "Gust of Wind", "Spike Growth", "Stone Fist", "Warding Wind"]
        third_list += ["Erupting Earth", "Meld into Stone", "Sleet Storm", "Stoneskin", "Wind Wall"]
        fourth_list += ["Control Water", "Stone Shape", "Storm Sphere", "Wall of Fire", "Watery Sphere"]
        fifth_list += ["Control Winds", "Transmute Rock", "Wall of Stone", "Cloudkill", "Insect Plague"]
        sixth_list += ["Bones of the Earth", "Move Earth", "Sunburst", "Wind Walk", "Investiture of Stone"]
        seventh_list += ["Whirlwind", "Reverse Gravity", "Fire Storm", "Regenerate", "Sequester"]
        eighth_list += ["Control Weather",
                       "Earthquake",
                       "Incendiary Cloud",
                       "Abi-Dalzim’s Horrid Wilting",
                       "Telepathy"]
        ninth_list += ["Meteor Swarm", "Storm of Vengeance", "Tsunami", "Weird", "Imprisonment"]

    # GNOME.
    if race == "Gnome":
        # Cantrips
        cantrips_list += [
            "Prestidigitation",
            "Minor Illusion",
            "Mage Hand", "Dancing Lights"]
        one_day_each_list += ["Disguise Self",
                             "Expeditious Retreat",
                             "Silent Image",
                             "Nondetection"]
        two_day_each_list += ["Blur", "Invisibility", "Nystul’s Magic Aura", "Blindness/Deafness"]
        three_day_each_list += ["Blink", "Major Image", "Phantom Steed"]
        first_list += ["Illusory Script", "Color Spray", "Charm Person", "Tasha’s Hideous Laughter", "Detect Magic"]
        second_list += ["Invisibility", "Mirror Image", "Suggestion", "Arcane Lock", "Pyrotechnics"]
        third_list += ["Major Image", "Dispel Magic", "Nondetection", "Hypnotic Pattern", "Leomund’s Tiny Hut"]
        fourth_list += ["Dimension Door", "Greater Invisibility", "Polymorph", "Stone Shape", "Confusion"]
        fifth_list += ["Animate Objects", "Mislead", "Seeming", "Teleportation Circle", "Rary’s Telepathic Bond"]
        sixth_list += ["Programmed Illusion", "True Seeing", "Mass Suggestion", "Eyebite", "Magic Jar"]
        seventh_list += ["Mirage Arcane", "Simulacrum", "Project Image", "Teleport", "Sequester"]
        eighth_list += ["Incendiary Cloud", "Dominate Monster", "Maze", "Mind Blank", "Power Word Stun"]
        ninth_list += ["Time Stop", "True Polymorph", "Weird", "Power Word Heal", "Power Word Kill"]

    # GOBLIN.
    if "Goblin" in race:
        cantrips_list += ["Minor Illusion", "Prestidigitation", "Mage Hand", "Vicious Mockery"]
        one_day_each_list += ["Disguise Self", "Tasha's Hideous Laughter", "Bane"]
        two_day_each_list += ["Darkness", "Misty Step", "Silent Image"]
        three_day_each_list += ["Fear", "Hypnotic Pattern", "Major Image"]
        first_list += ["Charm Person", "Sleep", "Dissonant Whispers", "Hideous Laughter", "Faerie Fire"]
        second_list += ["Invisibility", "Silence", "Suggestion", "Mirror Image", "Phantasmal Force"]
        third_list += ["Fear", "Major Image", "Bestow Curse", "Enemies Abound", "Blink"]
        fourth_list += ["Confusion", "Greater Invisibility", "Polymorph", "Shadow of Moil", "Dimension Door"]
        fifth_list += ["Mislead", "Animate Objects", "Dominate Person", "Geas", "Seeming"]
        sixth_list += ["Mass Suggestion", "Programmed Illusion", "True Seeing", "Eyebite", "Circle of Death"]
        seventh_list += ["Mirage Arcane", "Project Image", "Prismatic Spray", "Simulacrum", "Etherealness"]
        eighth_list += ["Dominate Monster", "Power Word Stun", "Antipathy/Sympathy", "Demiplane", "Feeblemind"]
        ninth_list += ["Power Word Kill", "Weird", "True Polymorph", "Foresight", "Meteor Swarm"]
        cantrips_list += ["Minor Illusion", "Mage Hand", "Message", "Poison Spray"]
        one_day_each_list += ["Disguise Self", "Expeditious Retreat", "Jump"]
        two_day_each_list += ["Grease", "Fog Cloud", "Hideous Laughter"]
        three_day_each_list += ["Blur", "Silence", "Darkness"]
        first_list += ["Sleep", "Dissonant Whispers", "Snare", "Entangle", "Charm Person"]
        second_list += ["Invisibility", "Pass without Trace", "Suggestion", "Mirror Image", "Web"]
        third_list += ["Gaseous Form", "Fear", "Stinking Cloud", "Hypnotic Pattern", "Bestow Curse"]
        fourth_list = ["Confusion", "Greater Invisibility", "Polymorph", "Dimension Door", "Hallucinatory Terrain"]
        fifth_list += ["Mislead", "Animate Objects", "Dominate Person", "Geas", "Cloudkill"]
        sixth_list += ["Programmed Illusion", "Eyebite", "Mass Suggestion", "Circle of Death", "True Seeing"]
        seventh_list += ["Mirage Arcane", "Prismatic Spray", "Project Image", "Etherealness", "Teleport"]
        eighth_list += ["Dominate Monster","Power Word Stun","Incendiary Cloud","Demiplane","Maze"]
        ninth_list += ["Power Word Kill", "Weird", "Time Stop", "Foresight", "Meteor Swarm"]

        if Dice() == 1 and not ("Leadership" in recharge):
            recharge += [" \n- Leadership (Recharges after a Short or Long Rest). \n\t For 1 minute, the goblin can utter a special command or warning whenever a nonhostile creature that it can see within 30 feet of it makes an attack roll or a saving throw. The creature can add a d4 to its roll provided it can hear and understand the goblin. A creature can benefit from only one Leadership die at a time. This effect ends if the goblin is incapacitated."]

    # HALFLING. 
    if "Halfling" in race:
        cantrips_list += ["Minor Illusion", "Prestidigitation", "Mage Hand", "Guidance"]
        one_day_each_list += ["Cure Wounds", "Bless", "Jump"]
        two_day_each_list += ["Invisibility", "Calm Emotions", "Protection from Poison"]
        three_day_each_list += ["Heroism","Haste", "Protection from Energy"]
        first_list += ["Cure Wounds", "Disguise Self", "Feather Fall", "Hideous Laughter", "Charm Person"]
        second_list += ["Alter Self", "Invisibility", "Knock", "Mirror Image", "Pass without Trace"]
        third_list += ["Blink", "Fly", "Haste", "Protection from Energy", "Water Walk"]
        fourth_list += ["Greater Invisibility", "Polymorph", "Dimension Door", "Freedom of Movement", "Stone Shape"]
        fifth_list += ["Mislead", "Modify Memory", "Passwall", "Teleportation Circle", "Greater Restoration"]
        sixth_list += ["Find the Path", "Guards and Wards", "Move Earth", "True Seeing", "Word of Recall"]
        seventh_list += ["Etherealness", "Plane Shift", "Regenerate", "Teleport", "Resurrection"]
        eighth_list += ["Antimagic Field", "Control Weather", "Earthquake", "Holy Aura", "Telepathy"]
        ninth_list += ["Foresight", "Imprisonment", "Meteor Swarm", "Time Stop", "True Resurrection"]


    # HUMAN. 
    if "Human" in race:
        cantrips_list += ["Prestidigitation","Thaumaturgy","Light","Mending"]
        one_day_each_list += ["Longstrider", "Charm Person", "Goodberry"]
        two_day_each_list += ["Enhance Ability", "Aid", "Calm Emotions"]
        three_day_each_list += ["Create Food and Water", "Sending", "Dispel Magic"]
        first_list += ["Alarm","Comprehend Languages","Cure Wounds","Detect Magic","Shield"]
        second_list += ["Detect Thoughts", "Locate Object", "Magic Weapon", "See Invisibility", "Zone of Truth"]
        third_list += ["Clairvoyance", "Counterspell", "Dispel Magic", "Speak with Dead", "Water Walk"]
        fourth_list += ["Arcane Eye", "Dimension Door", "Greater Invisibility", "Locate Creature", "Stoneskin"]
        fifth_list += ["Animate Objects", "Contact Other Plane", "Legend Lore", "Mass Cure Wounds", "Teleportation Circle"]
        sixth_list += ["Contingency", "Find the Path", "Guards and Wards", "Mass Suggestion", "True Seeing"]
        seventh_list += ["Etherealness", "Mirage Arcane", "Plane Shift", "Regenerate", "Teleport"]
        eighth_list += ["Antimagic Field", "Control Weather", "Demiplane", "Dominate Monster", "Telepathy"]
        ninth_list += [ "Foresight", "Gate", "Imprisonment", "Mass Heal", "Time Stop"]



    # KOBOLDS.
    if "Kobold" in race:
        cantrips_list += ["Dancing Lights", "Minor Illusion", "Prestidigitation", "Message"]
        one_day_each_list += ["Color Spray", "Grease", "Hideous Laughter"]
        two_day_each_list += ["Enlarge/Reduce", "Glitterdust", "Pyrotechnics"]
        three_day_each_list += ["Hypnotic Pattern", "Stinking Cloud", "Major Image"]
        first_list += ["Alarm", "Expeditious Retreat", "Feather Fall", "Snare", "Tasha’s Hideous Laughter"]
        second_list += ["Find Traps", "Misty Step", "Nystul’s Magic Aura", "Silence", "Web"]
        third_list += ["Blink", "Glyph of Warding", "Hypnotic Pattern", "Leomund’s Tiny Hut", "Sleet Storm"]
        fourth_list += ["Dimension Door", "Greater Invisibility", "Polymorph", "Stone Shape", "Watery Sphere"]
        fifth_list += ["Animate Objects", "Creation", "Mislead", "Seeming", "Teleportation Circle"]
        sixth_list += ["Arcane Gate", "Find the Path", "Programmed Illusion", "True Seeing", "Wall of Ice"]
        seventh_list += ["Etherealness", "Mirage Arcane", "Mordenkainen’s Magnificent Mansion", "Prismatic Spray", "Teleport"]
        eighth_list += ["Antipathy/Sympathy", "Demiplane", "Dominate Monster", "Feeblemind", "Illusory Dragon"]
        ninth_list += ["Imprisonment", "Invulnerability", "Mass Polymorph", "Power Word Kill", "Time Stop"]

    # LIZARDFOLK.
    if race == "Lizardfolk":
        cantrips_list += ["Guidance", "Mending", "Poison Spray", "Thorn Whip"]
        one_day_each_list += ["Cure Wounds", "Entangle", "Fog Cloud"]
        two_day_each_list += ["Barkskin", "Lesser Restoration", "Protection from Poison"]
        three_day_each_list += ["Conjure Animals", "Plant Growth", "Water Walk"]
        first_list += ["Create or Destroy Water", "Cure Wounds", "Entangle", "Fog Cloud", "Speak with Animals"]
        second_list += ["Animal Messenger", "Barkskin", "Find Traps", "Pass without Trace", "Spike Growth"]
        third_list += ["Call Lightning", "Conjure Animals", "Meld into Stone", "Plant Growth", "Water Walk"]
        fourth_list += ["Conjure Woodland Beings", "Control Water", "Freedom of Movement", "Giant Insect", "Stoneskin"]
        fifth_list += ["Awaken", "Commune with Nature", "Conjure Elemental", "Mass Cure Wounds", "Reincarnate"]
        sixth_list += ["Bones of the Earth", "Heal", "Heroes’ Feast", "Move Earth", "Sunbeam"]
        seventh_list += ["Mirage Arcane", "Regenerate", "Resurrection", "Reverse Gravity", "Whirlwind"]
        eighth_list += [ "Antipathy/Sympathy", "Control Weather", "Earthquake", "Tsunami", "Sunburst"]
        ninth_list += ["Foresight","Shapechange","Storm of Vengeance","True Resurrection","Mass Heal"]

    #MONSTROSITIES.
    if race == "Monstrosity":
        if Dice(8) == 1 and not ("Acid Spray" in recharge):
            recharge += [f"\n- Acid Spray (Recharge 6): \n\t The {race} spits acid in a line that is 30 feet long and 5 feet wide, provided that it has no creature grappled."] +\
                        [f"Each creature in that line must make a Dexterity saving throw, "+\
                        "taking {3*npc.proficiency_bonus} ({npc.proficiency_bonus}d6) acid damage on a failed save, or half as much damage on a successful one."]
        if Dice(10) == 1 and not ("Confusing Gaze" in recharge):
            recharge += [f"\n- Confusing Gaze (Recharge 6): \n\t When a creature starts its turn within 30 feet of the monstrosity and is able to see the {race}'s eyes, "+\
                        f"the {race} can magically force it to make a Charisma saving throw, unless the {race} is incapacitated. "+ \
                        f"\n\t On a failed saving throw, the creature can't take reactions until the start of its next turn and rolls a d8 to determine what it does during"+\
                        f"that turn. On a 1 to 4, the creature does nothing. On a 5 or 6, the creature takes no action but uses all its movement to move in a random direction."+\
                        f"On a 7 or 8, the creature makes one melee attack against a random creature, or it does nothing if no creature is within reach. "+\
                        "\n\t Unless surprised, a creature can avert its eyes to avoid the saving throw at the start of its turn. If the creature does so, "+\
                        f"it can't see the {race} until the start of its next turn, when it can avert its eyes again. If the creature looks at the {race} in the meantime, "+\
                        "it must immediately make the save." ]
        if Dice() == 1 and not ("Chilling Gaze" in recharge):
            recharge += [f"\n - Chilling Gaze (Recharge 6): \n\t The monstrosity targets one creature it can see within 30 feet of it. If the target can see the monstrosity, the target must succeed on a DC [10+%CON] Constitution saving throw against this magic or take 10 (3d6) cold damage and then be paralyzed for 1 minute, unless it is immune to cold damage. The target can repeat the saving throw at the start of each of its turns, ending the effect on itself on a success. If the target's saving throw is successful, or if the effect ends on it, the target is immune to the Chilling Gaze of all monstrosities for 1 hour."]
        if Dice() == 1 and not ("Disguise Self" in recharge):
            recharge += ["\n - Disguise self (humanoid form) Aura (Recharge 6): \n\t A 15-foot radius of magical darkness extends out from the Monstrosity, moves with it, and spreads around corners. The darkness lasts as long as the Monstrosity maintains concentration, up to 10 minutes (as if concentrating on a spell). Darkvision can't penetrate this darkness, and no natural light can illuminate it. If any of the darkness overlaps with an area of light created by a spell of 2nd level or lower, the spell creating the light is dispelled."]
        if Dice(8) == 1 and not ("Fire Breath" in recharge):
            recharge += ["\n -  Fire Breath (Recharge 5–6). \n\t The monstrosity exhales fire in a 15-foot cone. Each creature in that area must make a DC[11+%CON] Dexterity saving throw, taking 31 (7d8) fire damage on a failed save, or half as much damage on a successful one."]
                
        if Dice(8) == 1 and not ("Luring Song" in recharge):
            recharge += ["\n - Luring Song: \n\t The {race} sings a magical melody. Every humanoid and giant within 300 feet of the monstrosity that can hear the song must succeed on a DC [10+%Cha] Wisdom saving throw or be charmed until the song ends. The monstrosity must take a bonus action on its subsequent turns to continue singing. It can stop singing at any time. The song ends if the monstrosity is incapacitated. While charmed by the monstrosity, a target is incapacitated and ignores the songs of other monstrosities. If the charmed target is more than 5 feet away from the monstrosity, the target must move on its turn toward the monstrosity by the most direct route. It doesn't avoid opportunity attacks, but before moving into damaging terrain, such as lava or a pit, and whenever it takes damage from a source other than the monstrosity, a target can repeat the saving throw. A creature can also repeat the saving throw at the begguining of each of its turns. If a creature's saving throw is successful, the effect ends on it. A target that successfully saves is immune to this monstrosity's song for the next 24 hours."]

        if Dice(10) == 1 and not ("Petrifying Breath" in cantrip):
            cantrip += ["\n - Petrifying Breath (Recharge 5-6): \n\t The monstrosity exhales petrifying gas in a 30-foot cone. Each creature in that area must succeed on a Constitution saving throw (against the creature's Spellsave DC). On a failed save, a target begins to turn to stone and is restrained. The restrained target must repeat the saving throw at the start of its next turn. On a success, the effect ends on the target. On a failure, the target is petrified until freed by the greater restoration spell or other magic."]
        if Dice(10) == 1 and not ("Petrifying Gaze" in cantrip):
            cantrip += ["\n - Petrifying Gaze: \n\t If a creature starts its turn within 30 feet of the monstrosity and the two of them can see each other, the monstrosity can force the creature to make a DC [10+%CON] Constitution saving throw if the monstrosity isn't incapacitated. On a failed save, the creature magically begins to turn to stone and is restrained. It must repeat the saving throw at the start of its next turn. On a success, the effect ends. On a third failure, the creature is petrified until freed by the greater restoration spell or other magic. \n\t A creature that isn't surprised can avert its eyes to avoid the saving throw at the start of its turn. If it does so, it can't see the monstrosity until the start of its next turn, when it can avert its eyes again. If it looks at the monstrosity in the meantime, it must immediately make the save. \n\t If the monstrosity sees its reflection within 30 feet of it in bright light, it mistakes itself for a rival and targets itself with its gaze."]
        if Dice(8) == 1 and not ("Read Thoughts" in cantrip):
            cantrip += ["\n - Read Thoughts: \n\t The monstrosity magically reads the surface thoughts of one creature within 60 feet of it. The effect can penetrate barriers, but 3 feet of wood or dirt, 2 feet of stone, 2 inches of metal, or a thin sheet of lead blocks it. While the target is in range, the monstrosity can continue reading its thoughts, as long as the monstrosity's concentration isn't broken (as if concentrating on a spell). While reading the target's mind, the monstrosity has advantage on Wisdom (Insight) and Charisma (Deception, Intimidation, and Persuasion) checks against the target."]


    if race == "Monstrosity":
        if Dice(10) == 1 and not ("Paralyzing Ray" in cantrip):   cantrip += "\n - Paralyzing Ray \n\t The targeted creature must succeed on a DC [11+%CON] Constitution saving throw or be paralyzed for 1 minute. The target can repeat the saving throw at the start of each of its turns, ending the effect on itself on a success."
        if Dice(10) == 1 and not ("Fear Ray" in cantrip):         cantrip += "\n - Fear Ray \n\t The targeted creature must succeed on a DC [11+%CON] Wisdom saving throw or be frightened for 1 minute. The target can repeat the saving throw at the start of each of its turns, ending the effect on itself on a success."
        if Dice(10) == 1 and not ("Enervation Ray" in cantrip):   cantrip += "\n - Enervation Ray \n\t The targeted creature must make a DC [11+%CON] Constitution saving throw, taking 36 (8d8) necrotic damage on a failed save, or half as much damage on a successful one."
        if Dice(10) == 1 and not ("Disintegration Ray" in cantrip):   cantrip += "\n - Disintegration Ray. \n\t If the target is a creature, it must succeed on a DC [11+%CON] Dexterity saving throw or take 45 (10d8) force damage. If this damage reduces the creature to 0 hit points, its body becomes a pile of fine gray dust. \n\t If the target is a Large or smaller nonmagical object or creation of magical force, it is disintegrated without a saving throw. If the target is a Huge or larger nonmagical object or creation of magical force, this ray disintegrates a 10-foot cube of it."

    if race == "Monstrosity":

        cantrips_list += ["Acid Splash", "Infestation", "Poison Spray", "Thaumaturgy"]
        one_day_each_list += ["Disguise Self", "Fear", "Silent Image"]
        two_day_each_list += ["Alter Self", "Blur", "Mirror Image"]
        three_day_each_list += ["Major Image", "Protection from Energy", "Tongues"]
        first_list += ["Charm Person", "Detect Magic", "Disguise Self", "Illusory Script", "Silent Image"]
        second_list += ["Blur", "Darkness", "Invisibility", "Magic Mouth", "Mirror Image"]
        third_list += ["Fear", "Major Image", "Nondetection", "Protection from Energy", "Speak with Dead"]
        fourth_list += ["Confusion", "Dimension Door", "Greater Invisibility", "Hallucinatory Terrain", "Polymorph"]
        fifth_list += ["Dominate Person", "Dream", "Geas", "Mislead", "Modify Memory"]
        sixth_list += ["Eyebite", "Mass Suggestion", "Programmed Illusion", "True Seeing", "Contingency"]
        seventh_list += ["Mirage Arcane", "Project Image", "Regenerate", "Resurrection", "Sequester"]
        eighth_list += ["Dominate Monster", "Feeblemind", "Power Word Stun", "Telepathy", "Trap the Soul"]
        ninth_list += ["Imprisonment", "Power Word Kill", "Psychic Scream", "True Polymorph", "Weird"]

    '''
    ## Once a day
    if race == "Monstrosity" and Dice() == 1 and not ("Darkness Aura" in one):      one += "\n - Darkness Aura: \n\t A 15-foot radius of magical darkness extends out from the Monstrosity, moves with it, and spreads around corners. The darkness lasts as long as the Monstrosity maintains concentration, up to 10 minutes (as if concentrating on a spell). Darkvision can't penetrate this darkness, and no natural light can illuminate it. If any of the darkness overlaps with an area of light created by a spell of 2nd level or lower, the spell creating the light is dispelled."
    if race == "Monstrosity" and Dice() == 1 and not ("Geas" in one):               one += "\n - Geas."
    ## Three a day
    if race == "Monstrosity" and Dice() == 1 and not ("Charm Person" in three): three += "\n - Charm Person."
    if race == "Monstrosity" and Dice() == 1 and not ("Mirror Image" in three): three += "\n - Mirror Image."
    if race == "Monstrosity" and Dice() == 1 and not ("Scrying" in three):      three += "\n - Scrying."
    if race == "Monstrosity" and Dice() == 1 and not ("Suggestion" in three):   three += "\n - Suggestion."
    '''

    # OOZE
    '''
    if race == "Ooze" and Dice() == 1 and not ("Psychic Crush" in cantrip):     cantrip += " \n- Psychic Crush (Recharge 5–6). \n\t The ooze targets one creature that it can sense within 60 feet of it. The target must make a DC [10+%INT] Intelligence saving throw, taking 10 (3d6) psychic damage on a failed save, or half as much damage on a successful one."
    '''


    if race == "Ooze":
        cantrips_list += ["Acid Splash","Shape Water","Mold Earth","Gust"]
        one_day_each_list += ["Grease", "Entangle", "Tasha’s Hideous Laughter"]
        two_day_each_list += ["Web", "Melf's Acid Arrow", "Slippery Surface"]
        three_day_each_list += ["Stinking Cloud", "Slow", "Sleet Storm"]
        first_list += ["Absorb Elements", "Create or Destroy Water", "Ray of Sickness", "Mage Armor", "Grease"]
        second_list += ["Acid Arrow", "Web", "Levitate", "Gust of Wind", "Misty Step"]
        third_list += ["Stinking Cloud", "Water Walk", "Water Breathing", "Protection from Energy", "Gaseous Form"]
        fourth_list += ["Vitriolic Sphere", "Watery Sphere", "Stone Shape", "Control Water", "Ooze Form"]
        fifth_list += [ "Acidic Rain", "Control Winds", "Transmute Rock", "Maelstrom", "Creation"]
        sixth_list += ["Acid Fog", "Move Earth", "Create Undead", "Tenser's Transformation", "Wall of Ice"]
        seventh_list += ["Reverse Gravity", "Regenerate", "Whirlwind", "Plane Shift", "Prismatic Spray"]
        eighth_list += ["Incendiary Cloud", "Control Weather", "Earthquake", "Telepathy", "Abi-Dalzim's Horrid Wilting"]
        ninth_list += ["Shapechange", "Storm of Vengeance", "Time Stop", "Imprisonment", "Meteor Swarm"]


    # ORCS
    if race == "Orc":
        cantrips_list += ["Blade Ward", "True Strike", "Thaumaturgy", "Shillelagh"]
        one_day_each_list += ["Longstrider", "Fog Cloud", "Jump"]
        two_day_each_list += ["Enlarge/Reduce", "Darkvision", "Barkskin"]
        three_day_each_list += ["Crusader's Mantle", "Haste", "Conjure Barrage"]
        first_list += ["Guiding Bolt", "Thunderous Smite", "Cure Wounds", "Shield of Faith", "Hunter's Mark"]
        second_list += ["Hold Person", "Spiritual Weapon", "Aid", "Branding Smite", "Prayer of Healing"]
        third_list += ["Crusader's Mantle", "Dispel Magic", "Magic Weapon", "Revivify", "Call to Arms"]
        fourth_list += ["Stoneskin", "Freedom of Movement", "Divine Power", "Banishment", "Aura of Purity"]
        fifth_list += ["Destructive Wave", "Flame Strike", "Greater Restoration", "Circle of Power", "Raise Dead"]
        sixth_list += ["Heal", "Heroes' Feast", "Planar Ally", "Word of Recall", "Find the Path"]
        seventh_list += ["Regenerate", "Resurrection", "Symbol", "Conjure Celestial", "Fire Storm"]
        eighth_list += ["Earthquake", "Holy Aura", "Antipathy/Sympathy", "Control Weather", "Giant Form"]
        ninth_list += ["Gate","Mass Heal","True Resurrection","Power Word Kill","Storm of Vengeance"]
            
    # PLANTS
    # Spores
    if race == "Plant":
        recharge = add_spell(recharge, "Hallucination Spores",
                             spell_definition="Recharge(6):" +
                                "\t-Hallucination Spores \n\t The plant ejects spores at one creature it can see within 5 feet of it. The target must succeed on a DC 10+%CON Constitution saving throw or be poisoned for 1 minute. The poisoned target is incapacitated while it hallucinates. The target can repeat the saving throw at the start of each of its turns, ending the effect on itself on a success.")
        recharge = add_spell(recharge, "Rapport Spores",
                             spell_definition="Recharge(6):" +
                                "\t-Rapport Spores \n\t A 20-foot radius of spores extends from the plant. These spores can go around corners and affect only creatures with an Intelligence of 2 or higher that aren't undead, constructs, or elementals. Affected creatures can communicate telepathically with one another while they are within 30 feet of each other. The effect lasts for 1 hour.")
        recharge = add_spell(recharge, "Caustic Spores",
                             spell_definition="Recharge(6):" +
                                "\t-Caustic Spores \n\t The Plant releases spores in a 30-foot cone. Each creature inside the cone must succeed on a DC [10+%Con] Dexterity saving throw or take 3 (1d6) acid damage at the start of each of the plant's turns. A creature can repeat the saving throw at the start of its turn, ending the effect on itself on a success.")
        recharge = add_spell(recharge, "Infestation Spores",
                             spell_definition="Recharge(6):" +
                                "\t- Infestation Spores \n\t The plant releases spores that burst out in a cloud that fills a 10-foot-radius sphere centered on it, and the cloud lingers for 1 minute. Any flesh-and-blood creature in the cloud when it appears, or that enters it later, must make a DC [10+%CON] Constitution saving throw. On a successful save, the creature can't be infected by these spores for 24 hours. On a failed save, the creature is infected with a disease called the spores of Zuggtmoy and also gains a random form of indefinite madness (determined by rolling on the Madness of Zuggtmoy table) that lasts until the creature is cured of the disease or dies. While infected in this way, the creature can't be reinfected, and it must repeat the saving throw at the end of every 24 hours, ending the infection on a success. On a failure, the infected creature's body is slowly taken over by fungal growth, and after three such failed saves, the creature dies and is reanimated as a spore servant if it's a humanoid or a Large or smaller beast. \n d100 \t	Flaw (lasts until cured) \n 01-20 \t I see visions in the world around me that others do not. \n 21-40 \t I periodically slip into a catatonic state, staring off into the distance for long stretches at a time. \n 41-60 \t I see an altered version of reality, with my mind convincing itself that things are true even in the face of overwhelming evidence to the contrary. \n 61-80 \t My mind is slipping away, and my intelligence seems to wax and wane. \n  81-00 \t I am constantly scratching at unseen fungal infections.")
        recharge = add_spell(recharge, "Euphoria Spores",
                             spell_definition="Recharge(6):" +
                                 "\t-Euphoria Spores \n\t The plant releases a cloud of spores in a 20-foot-radius sphere centered on itself. " +
                                 "Other creatures in that area must each succeed on a Constitution saving throw or become poisoned for 1 minute. " +
                                 "A creature can repeat the saving throw at the start of each of its turns, ending the effect early on itself on a success. " +
                                 "When the effect ends on it, the creature gains one level of exhaustion.")
        recharge = add_spell(recharge, "Pacifying Spores",
                             spell_definition="Recharge(6):" +
                             "\t- Pacifying Spores \n\t The Plant ejects spores at one creature it can see within 5 feet of it. "+
                             "The target must succeed on a Constitution saving throw or be stunned for 1 minute. "+
                             "The target can repeat the saving throw at the start of each of its turns, ending the effect on itself on a success.")
        recharge = add_spell(recharge, "Animating Spores",
                             spell_definition="Recharge(6):" +
                                 "\t- Animating Spores \n\t The Plant targets one corpse of a humanoid or a Large or smaller beast within 5 feet of it and releases spores at the corpse. "+
                                 "Next turn, the corpse rises as a spore servant. The corpse stays animated for 1d4 + 1 weeks or until destroyed, and it can't be animated again in this way.")


    if race == "Plant":

        cantrips_list += ["Druidcraft",
                         "Shillelagh",
                         "Poison Spray",
                         "Thorn Whip"]
        one_day_each_list += ["Entangle",
                              "Goodberry",
                              "Speak with Plants"
                              ]
        two_day_each_list += ["Barkskin", "Spike Growth", "Plant Growth"]
        three_day_each_list += ["Conjure Woodland Beings", "Grasping Vine", "Freedom of Movement (self only)"]
        first_list += ["Cure Wounds", "Detect Poison and Disease", "Entangle", "Purify Food and Drink", "Fog Cloud"]
        second_list += ["Barkskin", "Goodberry", "Lesser Restoration", "Spike Growth", "Moonbeam"]
        third_list += ["Create Food and Water", "Dispel Magic", "Plant Growth", "Protection from Energy", "Speak with Plants"]
        fourth_list += ["Blight", "Control Water", "Freedom of Movement", "Giant Insect", "Stone Shape (earthy plants only)"]
        fifth_list += [
            "Awaken",
            "Commune with Nature",
            "Conjure Elemental",
            "Geas",
            "Reincarnate"]
        sixth_list += ["Heal", "Heroes' Feast", "Move Earth", "Sunbeam", "Transport via Plants"]
        seventh_list += ["Plane Shift",
                        "Regenerate",
                        "Reverse Gravity",
                        "Whirlwind",
                        "Mirage Arcane"]
        eighth_list += ["Antipathy/Sympathy", "Control Weather", "Earthquake", "Sunburst", "Tsunami"]
        ninth_list += ["Storm of Vengeance", "True Resurrection", "Shapechange (into plant creatures only)", "Foresight", "Mass Heal"]

    #Snakefolk
    if race == "Snakefolk":
        cantrips_list += ["Guidance", "Mending", "Poison Spray", "Thorn Whip", "Animal Friendship"]
        one_day_each_list += ["Cure Wounds", "Entangle", "Fog Cloud"]
        two_day_each_list += ["Barkskin", "Lesser Restoration", "Protection from Poison"]
        three_day_each_list += ["Conjure Animals", "Plant Growth", "Water Walk", "Poison Spray", "Suggestion"]
        first_list += ["Create or Destroy Water", "Cure Wounds", "Entangle", "Fog Cloud", "Speak with Animals"]
        second_list += ["Animal Messenger", "Barkskin", "Find Traps", "Pass without Trace", "Spike Growth"]
        third_list += ["Call Lightning", "Conjure Animals", "Meld into Stone", "Plant Growth", "Water Walk"]
        fourth_list += ["Conjure Woodland Beings", "Control Water", "Freedom of Movement", "Giant Insect", "Stoneskin"]
        fifth_list += ["Awaken", "Commune with Nature", "Conjure Elemental", "Mass Cure Wounds", "Reincarnate"]
        sixth_list += ["Bones of the Earth", "Heal", "Heroes’ Feast", "Move Earth", "Sunbeam"]
        seventh_list += ["Mirage Arcane", "Regenerate", "Resurrection", "Reverse Gravity", "Whirlwind"]
        eighth_list += ["Antipathy/Sympathy", "Control Weather", "Earthquake", "Tsunami", "Sunburst"]
        ninth_list += ["Foresight","Shapechange","Storm of Vengeance","True Resurrection","Mass Heal"]

    # UNDEAD
    if race == "Undead":
        if Dice(8) == 1 and not ("Create Specter" in recharge):             recharge += ["\n - Create Specter (Recharge 6)\n\t The undead targets a humanoid within 10 feet of it that has been dead for no longer than 1 minute and died violently. The target's spirit rises as a specter in the space of its corpse or in the nearest unoccupied space. The specter is under the undead's control. The undead can have no more than seven specters under its control at one time." ]
        if Dice(8) == 1 and not ("Corrupting Touch" in recharge):           recharge += ["\n - Corrupting Touch (Recharge 6)\n\t Melee Spell Attack: reach 5 ft., one target. Hit: 10 (3d6) necrotic damage."]
        if Dice(8) == 1 and not ("Dreadful Glare" in recharge):             recharge += ["\n - Dreadful Glare.(Recharge 6) \n\t The undead targets one creature it can see within 60 feet of it. If the target can see the undead, it must succeed on a DC [10+%CHA] Wisdom saving throw against this magic or become frightened until the end of the undead's next turn. If the target fails the saving throw by 5 or more, it is also paralyzed for the same duration. A target that succeeds on the saving throw is immune to the Dreadful Glare of all undead for the next 24 hours."]
        if Dice(8) == 1 and not ("Forceful Slam" in recharge):              recharge += ["\n - Forceful Slam (Recharge 6)\n\t Magic melee attack. Hit: 10 (3d6) force damage. "]
        if Dice(8) == 1 and not ("Fire Ray" in recharge):                   recharge += ["\n - Fire Ray (Recharge 6)\n\t Magic attack. Range 30 ft. Hit: 10 (3d6) fire damage. "]
        if Dice(8) == 1 and not ("Horrifying Visage" in recharge):          recharge += ["\n - Horrifying Visage (Recharge 6)\n\t Each non-undead creature within 60 feet of the Undead that can see them must succeed on a DC [10+%CHA] Wisdom saving throw or be frightened for 1 minute. A frightened target can repeat the saving throw at the start of each of its turns, with disadvantage if the Undead is within line of sight, ending the effect on itself on a success. If a target's saving throw is successful or the effect ends for it, the target is immune to the Undead's Horrifying Visage for the next 24 hours. "]
        if Dice(8) == 1 and not ("Life Drain" in recharge):                 recharge += ["\n - Life Drain (Recharge 6)\n\t On an hit, the target's Hit Points Maximum is reduced by the damage dealt. The target dies if this reduces its Hit Points Maximum to 0. Otherwise, the reduction lasts until the target finishes a short or long rest. "]
        elif Dice(8) == 1 and not ("Life Drain" in recharge):               recharge += ["\n - Life Drain (Recharge 6)\n\t On an hit, the target makes a Constitution saving throw. On a fail, the target takes 4d6 necrotic damage. The target's Hit Points Maximum is reduced by the necrotic damage dealt. The target dies if this reduces its Hit Points Maximum to 0. Otherwise, the reduction lasts until the target finishes a long rest. "]
        if Dice(8) == 1 and not ("Rotting Fist" in recharge):               recharge += ["\n - Rotting Fist. (Recharge 6)\n\t Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) bludgeoning damage plus 10 (3d6) necrotic damage. If the target is a creature, it must succeed on a DC [10+%CHA] Constitution saving throw or be cursed with undead rot. The cursed target can't regain hit points, and its hit point maximum decreases by 10 (3d6) for every 24 hours that elapse. If the curse reduces the target's hit point maximum to 0, the target dies, and its body turns to dust. The curse lasts until removed by the remove curse spell or other magic."]
        if Dice(8) == 1 and not ("Strength Drain" in recharge):             recharge += ["\n - Strength Drain (Recharge 6)\n\t On an attack hit the target's Strength score is reduced by 1d4. The target dies if this reduces its Strength to 0. Otherwise, the reduction lasts until the target finishes a short or long rest. \n\t If a non-evil humanoid dies from this attack, a new shadow rises from the corpse 1d4 hours later."]
        if Dice(8) == 1 and not ("Telekinetic Thrust" in recharge):         recharge += ["\n - Telekinetic Thrust.(Recharge 6) \n\t The undead targets a creature or unattended object within 30 feet of it. A creature must be Medium or smaller to be affected by this magic, and an object can weigh up to 150 pounds. \n\t If the target is a creature, the undead makes a Charisma check contested by the target's Strength check. If the undead wins the contest, the undead hurls the target up to 30 feet in any direction, including upward. If the target then comes into contact with a hard surface or heavy object, the target takes 1d6 damage per 10 feet moved. \n\t If the target is an object that isn't being worn or carried, the undead hurls it up to 30 feet in any direction. The undead can use the object as a ranged weapon, attacking one creature along the object's path (+4 to hit) and dealing 5 (2d4) bludgeoning damage on a hit."]
        if Dice(8) == 1 and not ("Wail" in recharge):                       recharge += ["\n - Wail. (Rechrge 6)\n\t The undead releases a mournful wail, provided that they aren't in sunlight. This wail has no effect on constructs and undead. All other creatures within 30 feet of them that can hear them must make a DC [10+%CHA] Constitution saving throw. On a failure, a creature drops to 0 hit points. On a success, a creature takes 10 (3d6) psychic damage."]
    if race == "Undead":
        cantrips_list += ["Chill Touch","Mage Hand","Spare the Dying","Thaumaturgy"]
        one_day_each_list += ["False Life", "Disguise Self", "Speak with Dead"]
        two_day_each_list += ["Ray of Enfeeblement", "Blindness/Deafness", "Gentle Repose"]
        three_day_each_list += ["Animate Dead", "Bestow Curse", "Vampiric Touch"]
        first_list += ["Inflict Wounds", "Ray of Sickness", "Shield", "Bane", "Cause Fear"]
        second_list += ["Blindness/Deafness", "Gentle Repose", "Ray of Enfeeblement", "Darkness", "Silence"]
        third_list += ["Animate Dead", "Bestow Curse", "Feign Death", "Speak with Dead", "Vampiric Touch"]
        fourth_list += ["Blight", "Death Ward", "Shadow of Moil", "Greater Invisibility", "Locate Creature"]
        fifth_list += ["Antilife Shell", "Contagion", "Danse Macabre", "Greater Restoration", "Raise Dead"]
        sixth_list += ["Create Undead", "Eyebite", "Harm", "Magic Jar", "True Seeing"]
        seventh_list += ["Etherealness", "Finger of Death", "Regenerate", "Resurrection", "Symbol"]
        eighth_list += ["Clone", "Create Undead (upgraded)", "Horrid Wilting", "Power Word Stun", "Telepathy"]
        ninth_list += ["Astral Projection", "Power Word Kill", "True Resurrection", "Wish", "Astral Projection (self only)"]
     

    if race == "Vampire" or race == "Undead":
        cantrips_list += ["Friends", "Mage Hand", "Minor Illusion", "Thaumaturgy"]
        one_day_each_list += ["Charm Person", "Disguise Self", "Misty Step"]
        two_day_each_list += ["Detect Thoughts", "Invisibility", "Hold Person"]
        three_day_each_list += ["Gaseous Form", "Hypnotic Pattern", "Suggestion"]
        first_list += ["Charm Person", "Disguise Self", "Mage Armor", "Shield", "Sleep"]
        second_list += ["Hold Person", "Invisibility", "Mirror Image", "Misty Step", "Suggestion"]
        third_list += ["Gaseous Form", "Hypnotic Pattern", "Vampiric Touch", "Feign Death", "Nondetection"]
        fourth_list += ["Charm Monster", "Dimension Door", "Greater Invisibility", "Shadow of Moil", "Blight"]
        fifth_list += [ "Dominate Person","Geas","Hold Monster", "Mislead", "Teleportation Circle"]
        sixth_list += [ "Create Undead", "Eyebite", "Mass Suggestion", "True Seeing", "Contingency"]
        seventh_list += ["Etherealness", "Finger of Death", "Plane Shift", "Teleport", "Resurrection"]
        eighth_list += ["Charm Monster (Mass)", "Dominate Monster", "Power Word Stun", "True Polymorph", "Glibness"]
        ninth_list += ["Astral Projection","Gate","Power Word Kill","True Resurrection","Wish"]

      
    spellbook.UpdateDifficulty(difficulty)

    # Ensure there are no duplicates in the lists

    spellbook.accessible[0] = list(set(cantrips_list))

    spellbook.accessible[1] = list(set(first_list))
    spellbook.accessible[2] = list(set(second_list))
    spellbook.accessible[3] = list(set(third_list))
    spellbook.accessible[4] = list(set(fourth_list))
    spellbook.accessible[5] = list(set(fifth_list))
    spellbook.accessible[6] = list(set(sixth_list))
    spellbook.accessible[7] = list(set(seventh_list))
    spellbook.accessible[8] = list(set(eighth_list))
    spellbook.accessible[9] = list(set(ninth_list))

    power_level = spellbook.max_spell_level
    
    spellbook.one_day_each_list = list(set(spellbook.accessible[power_level]))
    spellbook.two_day_each_list = list(set(spellbook.accessible[1 + power_level//2 ] ))
    spellbook.three_day_each_list = list(set(spellbook.accessible[1 + Dice(power_level)//3 ] ))


    spellbook.select_spells(is_spellcaster(npc))
    selected_spells_set = set()
    # Keep track of selected spells

    sample_size = min(len(cantrips_list), ( 2* npc.pb-difficulty)//difficulty, 5)
    for spell in safe_sample(cantrips_list, sample_size):
        spellbook.add_spell(0,spell)

    # Adding regular spells to the spellbook
    for level, spells in spellbook.selected.items():
        for spell in spells:
            spellbook.add_spell(level, spell)

    # Adding natural and rechargeable spells
    sample_size = min(len(one_day_each_list),1+ power_level//difficulty,6)
    for spell in safe_sample(one_day_each_list,sample_size):
        if spell not in selected_spells_set:
            spellbook.add_natural(spell, times_day=1)
            selected_spells_set.add(spell)

    sample_size = min(len(two_day_each_list), 2+ power_level//difficulty,6)
    for spell in safe_sample(two_day_each_list,sample_size):
        if spell not in selected_spells_set:
            spellbook.add_natural(spell, times_day=2)
            selected_spells_set.add(spell)

        
    sample_size = min(len(three_day_each_list),3+ power_level//difficulty,6)
    for spell in safe_sample(three_day_each_list,sample_size):
        if spell not in selected_spells_set:
            spellbook.add_natural(spell, times_day=3)
            selected_spells_set.add(spell)

    sample_size = min(len(recharge), Dice(npc.pb),6)
    for spell in safe_sample(recharge, sample_size):
        if spell:
        # Check if the spell name is valid and not empty
            spellbook.add_rechargeable(spell)
        
    return spellbook.SpellbookString(npc)








