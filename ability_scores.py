""" Ability Scores """

import dnd
import npc_class

def Modifier(score):
    return dnd.Modifier(score)

def RandomAbilityScore():
    return dnd.NewAbilityScore()


class AbilityScores:
    def __init__(self, STR, DEX, CON, INT, WIS, CHA):
        self.STR = STR
        self.DEX = DEX
        self.CON = CON
        self.INT = INT
        self.WIS = WIS
        self.CHA = CHA
        
    def RandomAbilityScores(self):
        self.STR = RandomAbilityScore()
        self.DEX = RandomAbilityScore()
        self.CON = RandomAbilityScore()
        self.INT = RandomAbilityScore()
        self.WIS = RandomAbilityScore()
        self.CHA = RandomAbilityScore()

    def mod(self, score):
        """Calculate the modifier for a given ability score."""
        return Modifier(score)
    
    @property
    def str_mod(self):
        return self.mod(self.STR)
    
    @property
    def dex_mod(self):
        return self.mod(self.DEX)

    @property
    def con_mod(self):
        return self.mod(self.CON)

    @property
    def int_mod(self):
        return self.mod(self.INT)

    @property
    def wis_mod(self):
        return self.mod(self.WIS)

    @property
    def cha_mod(self):
        return self.mod(self.CHA)

    def StandardArray(self):
        scores = [15, 14, 13, 12, 10, 8]
        random.shuffle(scores)
        self.STR=scores[0]
        self.DEX=scores[1]
        self.CON=scores[2]
        self.INT=scores[3]
        self.WIS=scores[4]
        self.CHA=scores[5]

def AbilityScoresPlus(npc):

    rc = npc.race
        
    ### Ability Scores Generation
    STR = self.AS.STR
    DEX = self.AS.DEX
    CON = self.AS.CON
    INT = self.AS.INT
    WIS = self.AS.WIS
    CHA = self.AS.CHA

      


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

        if "Highlander" in npc.subrace:
            STR += Dice(6)
        elif "Nomad" in npc.subrace:
            CON += Dice(6)
        elif "Islander" in npc.subrace:
            DEX += Dice(6)
        elif "Forester" in npc.subrace:
            WIS += Dice(6)
        elif "Plainsfolk" in npc.subrace:
            CON += Dice(3)
            STR += Dice(3)
        elif "Urbanite" in npc.subrace:
            CHA += Dice(6)
            
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

        if celestial_type == "Angelic Guardians" or "Angel" in npc.subrace:
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
            if Dice(4) == 1: INT += Dice(6)     # For engineering skills of tinkering.
        elif gnome_type == "Illusionist":
            CHA += Dice(3)                      # Charisma often governs spellcasting, especially illusions.
            if Dice(4) == 1: WIS += Dice(2)     # For a deeper understanding of magic
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
            CHA += Dice(4)                      # Enhanced charisma for their regal presence.                if Dice(4) == 1: INT += Dice(3)     # Intelligence for ruling and understanding fey politics.
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
            STR += Dice(4)                      # Strength from continuous mining.                if Dice(4) == 1: CON += Dice(3)     # Endurance from working in harsh conditions.
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
            CON += Dice(4)                      # To produce and resist their own venom.                if Dice(4) == 1: CHA += Dice(3)     # Intimidation due to the fear of their venom.
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

    if "Scholar" in npc.background:
        # Bonus to intelligence and wisdom due to their pursuit of knowledge.
        INT += Dice(6)
        WIS += Dice(3)

    if "Traveler" in npc.background:
        # Bonus to intelligence and wisdom due to their pursuit of knowledge.
        CON += Dice(6)
        
    self.AS.STR = STR
    self.AS.DEX = DEX
    self.AS.CON = CON
    self.AS.INT = INT
    self.AS.WIS = WIS
    self.AS.CHA = CHA
    
