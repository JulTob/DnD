# NPC class
# for D&D 5e

import random
import backgrounds 
import races
import dnd
import ability_scores 


def Dice(D=6,N=1):
    return dnd.Dice(D=D,N=N)

def Dizero(D=6,N=1):
    return dnd.Dizero(D=D,N=N)

def Alignment( alignment = ""):
    return dnd.Alignment(alignment)

def Modifier(score):
    return dnd.Modifier(score)

def PB(level):
    return dnd.PB(level)


class SavingThrows:
    def __init__(self, AS, PB):
        self.STR = Modifier(AS.STR)
        self.DEX = Modifier(AS.DEX)
        self.CON = Modifier(AS.CON)
        self.INT = Modifier(AS.INT)
        self.WIS = Modifier(AS.WIS)
        self.CHA = Modifier(AS.CHA)
        self.proficiency = None
        self.set_ST(PB)
        

    def set_ST(self,PB):
        # Dictionary to determine if saving throw is proficient
        self.proficiency = {
            'STR': False,
            'DEX': False,
            'CON': False,
            'INT': False,
            'WIS': False,
            'CHA': False}
        # Randomly assign proficiency to at least two saving throws
        while list(self.proficiency.values()).count(True) < 2:
            ability = random.choice(list(self.proficiency.keys()))
            self.proficiency[ability] = True
        if self.proficiency['STR']: self.STR += Dice(PB)
        if self.proficiency['DEX']: self.DEX += Dice(PB) 
        if self.proficiency['CON']: self.CON += Dice(PB) 
        if self.proficiency['INT']: self.INT += Dice(PB) 
        if self.proficiency['WIS']: self.WIS += Dice(PB) 
        if self.proficiency['CHA']: self.CHA += Dice(PB) 

    @property
    def string(self):
        string =("\nSaving Throws: \t" +
          f"STR: {self.STR:+}  \t" +
          f"DEX: {self.DEX:+}  \t" +
          f"CON: {self.CON:+}  \t" +
          f"INT: {self.INT:+}  \t" +
          f"WIS: {self.WIS:+}  \t" +
          f"CHA: {self.CHA:+}  \t")

        return string

class Skills:
    def __init__(self, AS, PB):
        self.PB = PB
        #STR
        self.Athletics = Modifier(AS.STR)+ self.proficient()
        #DEX
        self.Acrobatics = Modifier(AS.DEX)+ self.proficient()        
        self.Sleight_of_Hand = Modifier(AS.DEX)+ self.proficient()        
        self.Stealth = Modifier(AS.DEX)+ self.proficient()
        #CON
        #INT
        self.Arcana = Modifier(AS.INT)+ self.proficient()        
        self.History = Modifier(AS.INT)+ self.proficient()
        self.Investigation = Modifier(AS.INT)+ self.proficient()
        self.Nature = Modifier(AS.INT)+ self.proficient()
        self.Religion = Modifier(AS.INT)+ self.proficient()
        #WIS
        self.Animal_Handling = Modifier(AS.WIS)+ self.proficient()
        self.Insight = Modifier(AS.WIS)+ self.proficient()
        self.Medicine = Modifier(AS.WIS)+ self.proficient()
        self.Perception = Modifier(AS.WIS)+ self.proficient()
        self.Survival = Modifier(AS.WIS)+ self.proficient()
        #CHA
        self.Deception = Modifier(AS.CHA)+ self.proficient()        
        self.Intimidation = Modifier(AS.CHA)+ self.proficient()
        self.Performance = Modifier(AS.CHA)+ self.proficient()
        self.Persuasion = Modifier(AS.CHA) + self.proficient()

    def proficient(self):
        if Dice()==1: return Dice(self.PB)
        elif Dice(10)==1: return Dice(D=self.PB,N=2)
        elif Dice(20)==1: return Dice(D=self.PB,N=3)
        else: return 0

    @property
    def string(self):
        # Dictionary to hold skill names associated with their respective abilities
        skills = {
            'Athletics': self.Athletics,
            'Acrobatics': self.Acrobatics,
            'Sleight of Hand': self.Sleight_of_Hand,
            'Stealth': self.Stealth,
            'Arcana': self.Arcana,
            'History': self.History,
            'Investigation': self.Investigation,
            'Nature': self.Nature,
            'Religion': self.Religion,
            'Animal Handling': self.Animal_Handling,
            'Insight': self.Insight,
            'Medicine': self.Medicine,
            'Perception': self.Perception,
            'Survival': self.Survival,
            'Deception': self.Deception,
            'Intimidation': self.Intimidation,
            'Performance': self.Performance,
            'Persuasion': self.Persuasion
        }
        
        # Begin the skills string
        skills_str = "Skills:"

        # Iterate over the skills dictionary and add proficient skills based on a dice roll
        for skill, score in skills.items():
            sign = '+' if score >= 0 else ''
            skills_str += f"\n\t{skill}:\t{sign}{score}"

        # Set the attribute for skills
        return skills_str.strip()

    def Passive(self,skill):
        return 10+skill



"""
Main class
"""
class NPC:
    def __init__(self, race, background, lvl=1):
        self.race = race
        self.subrace =self.set_subrace()
        self.background = background
        self.title = self.SetTitle()
        self.gender = random.choice(["he", "she", "they"])
        self.level = lvl
        self.name = self.Naming()
        self.alignment = self.SetAlignment()
        
        self.AS = ability_scores.AbilityScores(10, 10, 10, 10, 10, 10) # Default
        self.AS.RandomAbilityScores()
        self.AC = 10 # Default
        self.ideal = None
        self.ST = SavingThrows(self.AS, self.proficiency_bonus)
        self.skills = Skills(self.AS,self.proficiency_bonus)                # Initialization
        self.passive_perception = self.skills.Passive(self.skills.Perception)
        self.languages = self.Languages()

        self.simple_attacks = self.SimpleAttack()   # Initialize simple attacks
        self.special_attack = self.SpecialAttack()  # Initialize special attack

        self.spellcasting_ability = ""
        self.spell_save_dc = None
        self.spell_attack_bonus = None
        self.set_spellcasting_info()

        self.spells = self.Magic()

        self.AC = self.setAC()

        self.abilities = self.setAbilities()
        self.movement = self.Movement()

        self.HP = self.SetHitPoints(lvl)
        self.ideal = self.setIdeal()
        self.plothook = self.setHook()
        self.trait = self.setTrait()
        
    @property
    def armor_class(self):
        return self.AC
    
    @property
    def saving_throws(self):
        return self.ST

    @property
    def pb(self):
        return self.PB()

    @property
    def proficiency_bonus(self):
        return self.PB()

    @property
    def ability_scores(self):
        return self.AS
    
    def setTrait(self):
        import personality
        trait = personality.Trait(self)
        #print(f"SetTrait: {trait}")
        return trait

    def setHook(self):
        import personality
        return personality.PlotHook(self)
    
    def setIdeal(self):
        import personality
        return personality.Ideal(self)
    
    def setAbilities(self):
        import abilities
        return abilities.Abilities(self)

        
    def SetTitle(npc):
        import names as name
        return name.Title(npc)
        
    def Movement(npc):
        import move
        return move.Movement(npc)

    def setAC(self):
        PB = self.proficiency_bonus
        AC = 10 + Dice(Modifier(self.AS.DEX)) + Dice(PB)
        if self.background == "Berserker":
            AC += Dice(Modifier(self.AS.CON))
        if self.background == "Monk":
            AC += Dice(Modifier(self.AS.WIS))
        if self.background == "Guard":
            AC += Dice(Modifier(self.AS.STR))       
        if self.background == "Hero":
            AC += Dice(Modifier(self.AS.STR))
        if self.background == "Hunter":
            AC += Dice(Modifier(self.AS.DEX))       
        if self.background == "Knight":
            AC += Dice(Modifier(self.AS.STR))       
            AC += Dice(Modifier(self.AS.CON))     
        if self.background == "Mage":
            AC += Dice(Modifier(self.AS.INT))      
        if self.background == "Noble":
            AC += Dice(Modifier(self.AS.DEX))       
        if self.background == "Pirate":
            AC += Dice(Modifier(self.AS.DEX))       
        if self.background == "Soldier":
            AC += Dice(Modifier(self.AS.STR))
        if self.background == "Spy":
            AC += Dice(Modifier(self.AS.DEX))
        if self.background == "Warrior":
            AC += Dice(Modifier(self.AS.STR))
        if self.background == "Warlock":
            AC += Dice(Modifier(self.AS.CHA))
        if self.background == "Witch":
            AC += Dice(self.AS.WIS)
        if self.race == "Human":
            AC += Dice(2)
        if self.race == "Beast":
            AC += Dice(3)
        if self.race == "Beastfolk":
            AC += Dice(3)
        if self.race == "Construct":
            AC += Dice(4)
        if self.race == "Dragon":
            AC += Dice(5)
        if self.race == "Dwarf":
            AC += Dice(3)
        if self.race == "Elf":
            AC += Dice(2)
        if self.race == "Giant":
            AC += Dice(3)
        if self.race == "Goblin":
            AC -= Dice(3)
        if self.race == "Kobold":
            AC -= Dice(3)
        if self.race == "Lizardfolk":
            AC += Dice(5)
        if self.race == "Orc":
            AC += Dice(3)
        if self.race == "Undead":
            AC -= Dice(3)

        if AC <10: return 10
        if AC >18 + PB: return 18 + PB
        else: return AC
        


    def set_subrace(self):
        return races.Monster(self.race)
        
    
    def Naming(self):
        import npc_namer as namer
        return namer.Racial_Names(self)
        
    def Magic(self):
        import magic
        return magic.Magic(self)

    def set_spellcasting_info(self):
        self.set_spellcasting_ability()
        self.set_spell_save_dc()
        self.set_spell_attack_bonus()

    def set_spell_attack_bonus(self):
        ability_mod = getattr(self.ability_scores, f"{self.spellcasting_ability.lower()}_mod")
        self.spell_attack_bonus = ability_mod + self.proficiency_bonus


    def set_spell_save_dc(self):
        ability_mod = getattr(self.ability_scores, f"{self.spellcasting_ability.lower()}_mod")
        self.spell_save_dc = 8 + ability_mod + self.proficiency_bonus

    def set_spellcasting_ability(self):
        # Find the highest modifier among INT, WIS, and CHA
        int_mod = self.ability_scores.int_mod
        wis_mod = self.ability_scores.wis_mod
        cha_mod = self.ability_scores.cha_mod

        # Create a dictionary to associate the ability score with its modifier
        ability_mod_dict = {'INT': int_mod, 'WIS': wis_mod, 'CHA': cha_mod}

        # Find the ability with the highest modifier
        self.spellcasting_ability = max(ability_mod_dict, key=ability_mod_dict.get)


        
    def SpecialAttack(self):
        import attacks
        special = ""
        special += attacks.SpecialAttack(self)
        special += "\n"
        return special
    
    def SimpleAttack(self):
        import attacks
        simple = ""
        simple += attacks.Attack(self)
        simple += "\n"
        for n in range(Dice(1+self.proficiency_bonus//3)):
            simple += attacks.Attack(self)
            simple += "\n"
        return simple
        
    def Languages(self):
        import languages
        return languages.Language(self)
        
        
    def SetAbilityScores(self, STR, DEX, CON, INT, WIS, CHA):
        self.AS = ability_scores.AbilityScores(STR, DEX, CON, INT, WIS, CHA)
        self.AbilityScoresPlus()
        self.ST = SavingThrows(self.AS, self.proficiency_bonus)
                

    def SetSubrace(self,race):
        self.subrace = bg.Monster(race)

    def SetName(self):
        import npc_namer as naming
        self.name = naming.Racial_Names(self)


    def PB(self):
        """Calculate the proficiency bonus based on level."""
        if self.level < 5: return 2
        else:
            return 2 + (self.level - 1) // 4
        

    def SetAlignment(self):
        self.alignment = Alignment()
        return self.alignment

    def SetArmorClass():
        self.AC = self.generate_armor_class()

    def generate_armor_class(self):
        crature_type = self.race + ' ' + self.type + ' ' + self.subrace
        AC = 10 + self.ability_scores.mod.dex + Dice(self.proficiency_bonus)
        if "Monk" in creature_type:
            AC += Dice(self.ability_scores.dex_mod)
        if "Berserker" in creature_type:
            AC += Dice(self.ability_scores.con_mod)
        if "Kobold" in creature_type:
            AC += Dice(2) # Natural Armor
        if "Dragon" in creature_type:
            AC += Dice(2) # Natural Armor
            
        if AC > 18 + self.proficiency_bonus:
            AC  = 18 + self.proficiency_bonus
        return AC

    def SetHitPoints(self, level):
        # Determine the size of the hit dice (between 2 and 12)
        hit_dice_sides = Dice(3,4)
            # Each Dice(3) call rolls a 3-sided die  
            # range: 4-12 , expected value: 8        
        dice_hp = Dice(
            D = hit_dice_sides,
            N = level)
        con_hp =  level * self.ability_scores.con_mod
        if con_hp<0:
            con_hp=0
        total_hp = dice_hp + con_hp
        self.HP = total_hp
        return total_hp

    def SetIdeal(self):
         import personality
         self.ideal = personality.Ideal(self)

    @property
    def to_hit_bonus(self):
        # Assuming to hit is based on the higher of STR or DEX modifier
        highest_ability_mod = Modifier(max(self.ability_scores.STR,
                                      self.ability_scores.DEX))
        return highest_ability_mod + self.proficiency_bonus
    
    @property
    def attack_bonus(self):
        return self.to_hit_bonus



