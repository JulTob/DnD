# NPC creator
import random
import json
 
from npc_namer import Title, Racial_Names


from backgrounds import Background

from races import Race, Monster


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

def Dizero(D=6):
    """Rolls a dice with D sides. If D is 0, simulates a coin flip."""
    if D < 0: roll = random.randint(D, 0) 
    else: roll = random.randint(0, D)
    return roll

def AbilityScore():
    d1 = Dice()
    d2 = Dice()
    d3 = Dice()
    d4 = Dice()
    return d1+d2+d3+d4 - min(d1, d2, d3, d4) 

def Modifier(AS):
    return (AS - 10) // 2

def Proficiency(AS):
    return Dice(Modifier(AS)*2)

def PB(Lvl):
    if Lvl < 5:
        return 2
    else:
        return 2 + (Lvl - 1) // 4

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
        "Toni Morrison",
        "Monty Pythons",
        "Ernest Hemingway",
        "Homer",
        "Dante Alighieri"
        
        ]
    return random.choice(styles)




































    
def Attack(Type,npc):
    PB = npc.proficiency_bonus
    STR = npc.ability_scores.str_mod
    DEX = npc.ability_scores.dex_mod
    
    sign_str = '+' if STR >= 0 else ''
    sign_dex = '+' if DEX >= 0 else ''
    

    SimpleMeleeWeapons = [
        f"Rock, {Dice(PB-1)}d6 {sign_str}{STR} Bludgeoning, 25/50 thrown",
        f"Fists, {Dice(PB-1)}d4 {sign_str}{STR} Bludgeoning",
        f"Brass Knuckles, {Dice(PB-1)}d4 {sign_str}{STR} Bludgeoning",
        f"Bite, {Dice(PB-1)}d4 {sign_str}{STR} Piercing",
        f"Bite, {Dice(PB-1)}d6 {sign_str}{STR} Piercing",
        f"Claws, {Dice(PB-1)}d4 {sign_str}{STR} Slashing",
        f"Claws, {Dice(PB-1)}d6 {sign_str}{STR} Slashing",
        f"Club, {Dice(PB-1)}d4 {sign_str}{STR} Bludgeoning",
        f"Dagger, {Dice(PB-1)}d4 {sign_str}{STR}Piercing, 20/60 thrown",
        f"Dagger, {Dice(PB-1)}d4 {sign_dex}{DEX} Piercing, 20/60 thrown",
        f"GreatClub, {Dice(PB-1)}d8 {sign_str}{STR} Bludgeoning",
        f"Handaxe, {Dice(PB-1)}d6 {sign_str}{STR} Slashing, 20/60 thrown",
        f"Javelin, {Dice(PB-1)}d6 {sign_str}{STR} Piercing, 30/120 thrown",
        f"Light Hammer, {Dice(PB-1)}d4 {sign_str}{STR} Bludgeoning, 20/60 thrown",
        f"Mace, {Dice(PB-1)}d6 {sign_str}{STR} Bludgeoning",
        f"Quarterstaff, {Dice(PB-1)}d6 {sign_str}{STR} Bludgeoning",
        f"Quarterstaff, {Dice(PB-1)}d8 {sign_str}{STR} Bludgeoning",
        f"Sickle, {Dice(PB-1)}d4 {sign_str}{STR} Slashing",
        f"Slam, {Dice(PB-1)}d8 {sign_str}{STR} Bludgeoning",
        f"Spear, {Dice(PB-1)}d6 {sign_str}{STR} Piercing, 20/60 thrown",
        f"Spear, {Dice(PB)+1}d8 {sign_str}{STR} Piercing, 20/60 thrown",
        f"Nunchaku, {Dice(PB-1)}d6 {sign_str}{STR} Bludgeoning"
        ]
    
    SimpleRangedWeapons = [
        f"Rock, {Dice(PB-1)}d6 {sign_str}{STR} Bludgeoning, 25/50 thrown",
        f"Light Crossbow, {Dice(PB-1)}d8 {sign_dex}{DEX} Piercing, 80/320 range",
        f"Dart, {Dice(PB-1)}d4 {sign_dex}{DEX} Piercing, 20/60 range",
        f"Dart, {Dice(PB-1)}d4 {sign_str}{STR} Piercing, 20/60 range",
        f"Shortbow, {Dice(PB-1)}d6 {sign_dex}{DEX} Piercing, 80/320 range",
        f"Sling, {Dice(PB-1)}d4 {sign_dex}{DEX} Bludgeoning, 30/120 range",
        f"Light Crossbow, {Dice(PB-1)}d8 {sign_dex}{DEX} Piercing, 80/320 range, loading, two handed"
        ]
    
    MartialMeleeWeapons = [
        f"Battleaxe, {Dice(PB-1)}d8 {sign_str}{STR} Slashing",
        f"Battleaxe, {Dice(PB-1)}d10 {sign_str}{STR} Slashing",
        f"Flail, {Dice(PB-1)}d8 {sign_str}{STR} Bludgeoning",
        f"Glaive, {Dice(PB-1)}d10 {sign_str}{STR} Bludgeoning, reach",
        f"Greataxe, {Dice(PB-1)}d12 {sign_str}{STR} Slashing, reach",
        f"Greatsword, {Dice(PB)+1}d6 {sign_str}{STR} Slashing",
        f"Halberd, {Dice(PB-1)}d10 {sign_str}{STR} Slashing, reach",
        f"Lance, {Dice(PB-1)}d12 {sign_str}{STR} Piercing, reach",
        f"Longsword, {Dice(PB-1)}d8 {sign_str}{STR} Slashing",
        f"Longsword, {Dice(PB-1)}d10 {sign_str}{STR} Slashing",
        f"Maul, {Dice(PB)+1}d6 {sign_str}{STR} Bludgeoning",
        f"Morningstar, {Dice(PB-1)}d8 {sign_str}{STR} Piercing",
        f"Pike, {Dice(PB-1)}d10 {sign_str}{STR} Piercing, reach",
        f"Rapier, {Dice(PB-1)}d8 {sign_str}{STR} Piercing, Finesse",
        f"Rapier, {Dice(PB-1)}d8 {sign_dex}{DEX} Piercing, Finesse",
        f"Scimitar, {Dice(PB-1)}d6 {sign_str}{STR} Slashing, Finesse, light",
        f"Scimitar, {Dice(PB-1)}d6 {sign_dex}{DEX} Slashing, Finesse, light",
        f"Shortsword, {Dice(PB-1)}d6 {sign_str}{STR} Slashing, Finesse, light",
        f"Shortsword, {Dice(PB-1)}d6 {sign_dex}{DEX} Slashing, Finesse, light",
        f"Trident, {Dice(PB-1)}d6 {sign_str}{STR} Piercing, 20/60 thrown",
        f"Trident, {Dice(PB-1)}d8 {sign_str}{STR} Piercing, 20/60 thrown",
        f"War pick, {Dice(PB-1)}d8 {sign_str}{STR} Bludgeoning",
        f"Warhammer, {Dice(PB-1)}d8 {sign_str}{STR} Bludgeoning",
        f"Warhammer, {Dice(PB-1)}d10 {sign_str}{STR} Bludgeoning",
        f"Whip, {Dice(PB-1)}d4 {sign_str}{STR} Slashing, Finesse, reach"
        f"Whip, {Dice(PB-1)}d4 {sign_dex}{DEX} Slashing, Finesse, reach"
        ]
    
    MartialRangedWeapons = [
        f"Blowgun, 1 Piercing, 25/100 range, Ammunition, Loading",
        f"Hand Crossbow, {Dice(PB-1)}d6 {sign_dex}{DEX} Piercing, 30/120 range, Ammunition, Light, Loading",
        f"Heavy Crossbow, {Dice(PB-1)}d10 {sign_dex}{DEX} Piercing, 100/400 range, Ammunition, Heavy, Loading, Two-Handed",
        f"Longbow, {Dice(PB-1)}d8 {sign_dex}{DEX} Piercing, 150/600 range, Ammunition, Heavy, Two-Handed",
        f"Net, Special, 5/15 range, Thrown",
        f"Throwing Axe, {Dice(PB-1)}d6 {sign_str}{STR} Slashing, 20/60 range, Thrown",
        f"Flintlock Pistol, {Dice(PB-1)}d8 {sign_dex}{DEX} Piercing, 30/90 range, Loading, Jamming: On an attack roll of 1, the gun jams and requires an action to clear before it can be fired again.",
        f"Musket, {Dice(PB-1)+1}d10 {sign_dex}{DEX} Piercing, 60/180 range, Loading, Jamming: On an attack roll of 1, the gun jams and requires an action to clear before it can be fired again.",
        f"Blunderbuss, {Dice(PB)+2}d10 {sign_dex}{DEX} Fire, 10/30 range, Loading, Exploding: On an attack roll of 1, the gun explodes and requires a short rest fixing it before it can be fired again. You don't gain the benefits of that short rest."
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





def SpecialAttack(npc):
    Lvl = npc.level
    Mod = PB(npc.level) + random.choice([npc.ability_scores.str_mod,npc.ability_scores.dex_mod,npc.ability_scores.con_mod,
                                    npc.ability_scores.int_mod, npc.ability_scores.wis_mod, npc.ability_scores.cha_mod])
    STR=npc.ability_scores.str_mod
    DEX=npc.ability_scores.dex_mod
    dmg = Damage()
    con = Condition(dmg)
    r = ""

    # Basic attack description    
    r += Attack(Dice(4), npc) + " +"

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




        
def Language(npc):
    race = npc.race
    background = npc.background
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
            "Dwarvish": 15,
            "Elvish": 10,
            "Giant": 16,
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
   
        if Dice(2): add_language(languages, "Telepathy. (60 feet).", 8) 
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
            "Celestial": 25,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 2,
            "Primordial": 22,
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
            "Celestial": 19,
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
            "Dwarvish": 9,
            "Elvish": 21,
            "Giant": 9,
            "Gnomish": 21,
            "Goblin": 11,
            "Halfling": 21,
            "Orc": 7,
            "Abyssal": 4,
            "Celestial": 21,
            "Draconic": 5,
            "Deep Speech": 1,
            "Infernal": 5,
            "Primordial": 11,
            "Sylvan": 9,
            "Undercommon": 1
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    
    if race == "Ooze":
        add_language(languages, "Telepathy. ", 1)

    if race == "Orc":
        langs = {
            "Dwarvish": 12,
            "Elvish": 12,
            "Giant": 4,
            "Gnomish": 22,
            "Goblin": 2,
            "Halfling": 22,
            "Orc": 1,
            "Abyssal": 8,
            "Celestial": 8,
            "Draconic": 8,
            "Deep Speech": 22,
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






def get_max_spell_level(character_level, difficulty = 1):
    if difficulty < 1: difficulty = 1
    if difficulty > 8: difficulty = 8
    level = (character_level - difficulty) // (2 * difficulty)
    if level < 0: return 0
    if level > 9: return 9
    return level






        

def add_spell(spell_list, spell_name, spell_level, slots, max_spell_level, spell_definition=""):
    if slots < 1: slots = 1
    # Check if the spell level is within the allowable range
    if spell_level <= 0 or max_spell_level <= 0:
        if spell_name not in spell_list:    spell_list += f"\n- {spell_name}"
        if spell_definition:                spell_list += f": {spell_definition}"
        return spell_list, slots
        
    elif spell_level <= max_spell_level:
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
            if spell_name not in spell_list:
                spell_list += f"\n- {spell_name}"
                if spell_definition:
                    spell_list += f": {spell_definition}"
                slots += 1
    return spell_list, slots






def Magic(npc):

    Lvl = npc.level
    race = npc.race
    background = npc.background

    cantrip = "Cantrips (at will): "
    first   = "1st Level Spells: "
    second  = "2nd Level Spells: "
    third   = "3rd Level Spells: "
    fourth  = "4th Level Spells: "
    fifth   = "5th Level Spells: "
    sixth   = "6th Level Spells: "
    seventh = "7th Level Spells: "
    eighth  = "8th Level Spells: "
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

    recharge = ""
    
    difficulty = 10
    max_spell_level = 1

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

# BACKGROUNDS:

    # Bandit
    if background == "Bandit":
        difficulty = 2 + Dice(6) 
        max_spell_level = get_max_spell_level(Lvl,difficulty)
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
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        cantrips_list += [            "Dancing Lights",            "Vicious Mockery",            "Mage Hand",            "Minor Illusion",            "Prestidigitation", "Light",            "Message",            "Mending",            "Friends"        ]
        one_day_each_list += [            "Charm Person", "Disguise Self", "Feather Fall"]
        two_day_each_list += [            "Invisibility", "Suggestion", "Enhance Ability"]
        three_day_each_list += [            "Hypnotic Pattern",            "Major Image",            "Counterspell"]

        first_list += [            "Disguise Self",            "Healing Word",            "Identify",            "Faerie Fire",            "Charm Person",            "Silent Image",            "Sleep",            "Tasha’s Hideous Laughter",    "Unseen Servant",            "Speak With Animals"]
        
        second_list += [
            "Invisibility",
            "Knock",
            "Detect Thoughts",
            "Enhance Ability",
            "Lesser Restoration",
            "Zone of Truth",
            "Calm Emotions",
            "Heat Metal",
            "Suggestion",
            "Phantasmal Force"
        ]
        
        # 3rd Level Spells
        third_list += [
            "Dispel Magic",
            "Leomund’s Tiny Hut",
            "Hypnotic Pattern",
            "Major Image",
            "Sending",
            "Tongues",
            "Fear",
            "Charm Monster",
            "Stinking Cloud",
            "Speak with Dead"
        ]

        # 4th Level Spells
        fourth_list += [
            "Dimension Door",
            "Polymorph",
            "Greater Invisibility",
            "Freedom of Movement",
            "Hallucinatory Terrain",
            "Locate Creature",
            "Compulsion",
            "Confusion",
            "Geas",
            "Stone Shape"
        ]

        # 5th Level Spells
        fifth_list += [
            "Mass Cure Wounds",
            "Raise Dead",
            "Greater Restoration",
            "Teleportation Circle",
            "Mislead",
            "Modify Memory",
            "Animate Objects",
            "Awaken",
            "Scrying",
            "Dominate Person"
        ]
        
        # 6th Level Spells
        sixth_list += [
            "True Seeing",
            "Otto’s Irresistible Dance",
            "Programmed Illusion",
            "Mass Suggestion",
            "Heroes’ Feast",
            "Find The Path",
            "Eyebite",
            "Countercharm"
        ]

        # 7th Level Spells
        seventh_list += [
            "Teleport",
            "Resurrection",
            "Regenerate",
            "Mirage Arcane",
            "Etherealness",
            "Symphony Of The Masked",
            "Forcecage",
            "Dream Of The Blue Veil"
        ]

        # 8th Level Spells
        eighth_list += [
            "Power Word Stun",
            "Mind Blank",
            "Maze",
            "Glibness",
            "Dominate Monster",
            "Antimagic Field",
            "Foresight",
            "Feeblemind"
        ]

        # 9th Level Spells
        ninth_list += [
            "Power Word Kill",
            "True Polymorph",
            "Time Stop",
            "Psychic Scream",
            "Prismatic Wall",
            "Mass Polymorph",
            "Foresight",
            "Meteor Swarm"
        ]




    # Berserker
    if background == "Berserker":

        difficulty = 2+ Dice(10)  # 1/7 Caster
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
        cantrips_list += [
            "Blade Ward",
            "Thaumaturgy",
            "True Strike",
            "Guidance"
        ]

        one_day_each_list += [
            "Longstrider",
            "False Life",
            "Shield"]
        two_day_each_list += ["Enhance Ability", "Blur", "Protection from Energy"]
        three_day_each_list += ["Haste", "Fear", "Heroism"]

        # 1st Level Spells
        first_list += [
            "Bane",
            "Compelled Duel",
            "Wrathful Smite",
            "Searing Smite"
        ]

        # 2nd Level Spells
        second_list += [
            "Branding Smite",
            "Magic Weapon",
            "Find Steed"
        ]

        second, slots2 = add_spell(second, "Enhance Ability", 2, slots2, max_spell_level, "Bull's Strength")

        third_list += [            "Crusader's Mantle",
            "Elemental Weapon",            "Fear",
            "Spirit Guardians"        ]

        # 4th Level Spells
        fourth_list += [            "Stoneskin",
            "Freedom Of Movement",            "Compulsion",
            "Grasping Vine"        ]

        # 5th Level Spells
        fifth_list += [
            "Destructive Wave",            "Flame Strike",
            "Geas",            "Commune With Nature"
        ]
        
        # 6th Level Spells
        sixth_list += [            "Heroes' Feast",
            "Find the Path",
            "Wind Walk"        ]

        # 7th Level Spells
        seventh_list += [            "Regenerate",
            "Fire Storm",            "Resurrection"
        ]

        # 8th Level Spells
        eighth_list += [            "Earthquake",
            "Control Weather",            "Animal Shapes"]

        # 9th Level Spells
        ninth_list += ["Storm of Vengeance","True Resurrection","Shapechange"]


    # Charlatan
    if background == "Charlatan":

        difficulty = Dice(8)  # 1/4 Caster
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
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
        max_spell_level = get_max_spell_level(Lvl, difficulty)

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
        ninth, slots9 = add_spell(ninth, "Wish" , 9, slots9, max_spell_level, "One per Lifetime")

    # Cultist

    if background == "Cultist":

        difficulty = Dice(3) 
        max_spell_level = get_max_spell_level(Lvl,difficulty)

        cantrips_list += [            "Chill Touch",            "Eldritch Blast",            "Guidance",            "Infestation",            "Light",            "Sacred Flame",           "Thaumaturgy",            "Toll The Dead",            "Vicious Mockery"            ]
        one_day_each_list += [            "Command",            "Inflict Wounds",            "Protection from Good and Evil"]
        two_day_each_list += [            "Suggestion",
            "Silence",            "Hold Person"]
        three_day_each_list += [            "Detect Thoughts", "Darkness", "Disguise Self"]
        first_list += [            "Bane",
            "Cause Fear",            "Command",
            "Hex",            "Inflict Wounds",
            "Protection From Good And Evil",            "Shield Of Faith",
            "Unseen Servant"            ]
        second_list += [            "Blindness/Deafness",
            "Darkness",            "Enthrall",
            "Hold Person",            "Mind Spike",
            "Ray Of Enfeeblement",            "Silence",
            "Spiritual Weapon"]
        third_list += [    "Animate Dead",
            "Bestow Curse",            "Fear",
            "Hypnotic Pattern",            "Speak With Dead",
            "Vampiric Touch",            "Tongues",
            "Spirit Guardians"            ]
        fourth_list += [            "Blight",
            "Death Ward",            "Hallucinatory Terrain",
            "Locate Creature",            "Phantasmal Killer",
            "Shadow Of Moil",            "Sickening Radiance",
            "Summon Greater Demon"            ]
        fifth_list += [            "Contagion",
            "Danse Macabre",            "Geas",
            "Hold Monster",            "Insect Plague",
            "Mass Cure Wounds",            "Scrying",
            "Wrath Of Nature"            ]
        sixth_list += [            "Circle Of Death",
            "Create Undead",            "Eyebite",
            "Harm",            "Heroes' Feast",
            "Mass Suggestion",            "True Seeing",
            "Word Of Recall"            ]
        seventh_list += [
            "Finger Of Death",            "Plane Shift",
            "Regenerate",            "Resurrection",
            "Symbol",            "Teleport",
            "Etherealness",
            "Fire Storm"
            ]
        eighth_list += [
            "Antimagic Field",          "Dominate Monster",
            "Feeblemind",            "Holy Aura",
            "Incendiary Cloud",
            "Maze",            "Power Word Stun",
            "Sunburst"                      ]
        ninth_list += [
            "Astral Projection",
            "Gate",            "Implosion",
            "Mass Heal",            "Power Word Kill",
            "Psychic Scream",            "True Resurrection",
            "Weird"            ]

    # Criminal
    if background == "Criminal":
        difficulty = 1 + Dice(6)  
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        cantrips_list += [            "Mage Hand",
            "Minor Illusion",            "Prestidigitation",
            "Message"        ]
        one_day_each_list += ["Disguise Self", "Silent Image", "Expeditious Retreat"]
        two_day_each_list += ["Invisibility", "Pass without Trace", "Knock"]
        three_day_each_list += ["Mage Hand", "Message", "Prestidigitation"]
        first_list += [            "Disguise Self",
            "Charm Person",
            "Silent Image",
            "Sleep",            "Expeditious Retreat"        ]
        second_list += [            "Invisibility",
            "Suggestion",            "Alter Self",
            "Darkness",            "Pass Without Trace"
        ]
        
        third_list += [            "Nondetection",
            "Dispel Magic",
            "Hypnotic Pattern",
            "Major Image",
            "Leomund’s Tiny Hut"
        ]
        fourth_list += [            "Greater Invisibility",
            "Dimension Door",
            "Arcane Eye",
            "Freedom of Movement",
            "Locate Creature"
        ]
        fifth_list += [            "Mislead",
            "Modify Memory",
            "Teleportation Circle",
            "Passwall",            "Seeming"
        ]
        sixth_list += [
            "True Seeing",
            "Programmed Illusion",
            "Find the Path"
        ]
        seventh_list += [            "Mirage Arcane",
            "Project Image",
            "Teleport"        ]
        eighth_list += [
            "Demiplane",            "Mind Blank",
            "Antimagic Field"        ]
        ninth_list += [            "Imprisonment",
            "Time Stop",            "Power Word Kill"
        ]

    # Druid
    if background == "Druid":

        difficulty = Dice(3)  # Full caster
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        cantrips_list = [            "Druidcraft",
            "Guidance",            "Mending",
            "Produce Flame",
            "Shillelagh",            "Resistance"
        ]

        one_day_each_list += [            "Cure Wounds",
            "Entangle",            "Speak with Animals"]
        two_day_each_list += [            "Barkskin",
            "Moonbeam",            "Pass without Trace"]
        three_day_each_list += [            "Guidance",
            "Thorn Whip",            "Druidcraft"]
        first_list += [            "Cure Wounds",
            "Entangle",            "Faerie Fire",
            "Goodberry",
            "Healing Word",
            "Thunderwave",
            "Create or Destroy Water",
            "Speak With Animals",
            "Longstrider"        ]
        second_list += [            "Barkskin",
            "Flame Blade",            "Flaming Sphere",
            "Lesser Restoration",
            "Moonbeam",            "Pass Without Trace",
            "Spike Growth",
            "Animal Messenger"        ]
        third_list += [            "Call Lightning",
            "Cure Wounds",
            "Dispel Magic",            "Protection From Energy",
            "Water Breathing",            "Water Walk",
            "Wind Wall"        ]
        fourth_list += [            "Control Water",
            "Freedom Of Movement",            "Ice Storm",
            "Stoneskin",            "Wall of Fire",
            "Giant Insect"        ]
        fifth_list += [            "Awaken",
            "Commune With Nature",            "Cure Wounds",
            "Geas",            "Mass Cure Wounds",
            "Reincarnate",            "Tree Stride"
        ]
        sixth_list = [            "Heal",
            "Heroes' Feast",            "Move Earth",
            "Sunbeam",            "Transport Via Plants",
            "Wall Of Thorns",            "Wind Walk"
        ]
        seventh_list = [            "Fire Storm",
            "Mirage Arcane",            "Plane Shift",
            "Regenerate",            "Reverse Gravity",
            "Teleport"        ]
        eighth_list = [            "Animal Shapes",
            "Control Weather",            "Earthquake",
            "Sunburst",            "Tsunami",
            "Antipathy/Sympathy"        ]
        ninth_list = [            "Shapechange",
            "Storm of Vengeance",            "True Resurrection",
            "Foresight",            "Mass Heal"
        ]

    # Expert
    if background == "Expert":

        difficulty = Dice(6)  
        max_spell_level = get_max_spell_level(Lvl, difficulty)
        cantrips_list += ["Guidance",  "Mending",            "Message",            "Prestidigitation",            "Thaumaturgy"]
        one_day_each_list += ["Identify", "Disguise Self", "Detect Thoughts"]
        two_day_each_list += ["Enhance Ability", "Invisibility", "Knock"]
        three_day_each_list += ["Mage Hand", "Message", "Prestidigitation"]
        first_list += ["Comprehend Languages",            "Cure Wounds",            "Detect Magic",          "Disguise Self",            "Identify"]
        second_list += ["Enhance Ability",            "Find Traps",            "Lesser Restoration",            "Locate Animals Or Plants",            "Locate Object"]
        third_list += ["Create Food And Water",            "Dispel Magic",            "Protection From Energy",            "Remove Curse",            "Tongues"]
        fourth_list += ["Freedom Of Movement",            "Greater Restoration",            "Locate Creature",            "Stone Shape",            "Fabricate"]
        fifth_list += ["Contact Other Plane",            "Legend Lore",            "Mass Cure Wounds",            "Planar Binding",            "Teleportation Circle"]
        sixth_list += ["Find The Path",            "Guards And Wards",            "Heal",            "Heroes' Feast",            "True Seeing"]
        seventh_list += ["Regenerate",            "Resurrection",            "Sequester",            "Symbol",            "Teleport"]
        eighth_list += ["Antimagic Field",            "Control Weather",            "Earthquake",            "Mind Blank",            "Power Word Stun"]
        ninth_list += [ "Foresight",            "Mass Heal",            "Power Word Heal",            "True Resurrection",            "Wish"]

    # Explorer
    if background == "Explorer":

        difficulty = Dice(8)  # One Third Caster
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        cantrips_list += [            "Druidcraft",            "Guidance",            "Mage Hand",            "Mending",            "Thaumaturgy"]
        one_day_each_list += ["Find the Path", "Pass without Trace", "Water Walk"]
        two_day_each_list += ["Goodberry", "Protection from Energy", "Speak with Animals"]
        three_day_each_list += ["Longstrider", "Guidance", "Light"]
        first_list += [            "Cure Wounds",            "Detect Magic",            "Goodberry",            "Jump",            "Longstrider"]
        second_list += [            "Find Traps",            "Flame Blade",            "Locate Animals Or Plants",            "Pass Without Trace",            "Rope Trick"]
        third_list += ["Create Food And Water","Daylight","Feign Death","Protection From Energy","Water Breathing"]
        fourth_list += [            "Control Water",            "Fabricate",            "Freedom Of Movement",            "Locate Creature",            "Stone Shape"        ]
        fifth_list += [            "Commune With Nature", "Legend Lore",            "Passwall","Teleportation Circle",            "Tree Stride"]
        sixth_list += ["Find The Path","Move Earth",            "Transport Via Plants", "Wind Walk",            "True Seeing"]
        seventh_list += ["Mirage Arcane",            "Plane Shift",            "Regenerate",            "Reverse Gravity",            "Teleport"        ]
        eighth_list += [            "Antimagic Field",            "Control Weather",            "Earthquake",            "Telepathy",            "Tsunami"        ]
        ninth_list += [            "Foresight",           "Gate",            "Imprisonment",            "Meteor Swarm",            "Time Stop"        ]

    # Gladiator
    if background == "Gladiator":

        difficulty = Dice(8)  # One Fourth Caster
        max_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
        cantrips_list += [            "Blade Ward", "Friends",            "Prestidigitation",            "True Strike",            "Thaumaturgy"        ]
        one_day_each_list += [            "Heroism","Compelled Duel",            "Shield"]
        two_day_each_list += ["Enhance Ability", "Thunderous Smite", "Blur"]
        three_day_each_list += ["Mage Hand", "True Strike", "Prestidigitation"]
        first_list += [            "Bless","Command",            "Heroism",            "Shield",            "Thunderwave"        ]
        second_list += [            "Branding Smite","Enhance Ability",            "Enlarge/Reduce",            "Magic Weapon",            "Spiritual Weapon"        ]
        third_list += [            "Crusader's Mantle","Fear",            "Haste",            "Protection From Energy",            "Slow"        ]
        fourth_list += ["Compulsion",            "Freedom Of Movement",            "Stone Shape",            "Stoneskin",            "Wall Of Fire"        ]
        fifth_list += ["Flame Strike",            "Greater Restoration",            "Hold Monster",            "Legend Lore",            "Skill Empowerment"        ]
        sixth_list += ["Blade Barrier",            "Find The Path",            "Heal",            "Heroes' Feast",            "Tenser's Transformation"        ]
        seventh_list += ["Crown Of Stars",            "Forcecage",            "Mordenkainen's Sword",            "Regenerate",            "Resurrection"]
        eighth_list += ["Antimagic Field",            "Dominate Monster",            "Earthquake",            "Holy Aura",            "Incendiary Cloud"        ]
        ninth_list += ["Blade Of Disaster","Foresight","Mass Heal","Power Word Kill","Time Stop"]

    # Guard
    if background == "Guard":
        difficulty = Dice(12)  
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
        cantrips_list = [
            "Blade Ward",
            "Control Flames",
            "Friends",
            "Light",
            "True Strike"
        ]
        for c in cantrips_list:
            cantrip, _ = add_spell(cantrip, c, 0, 0, max_spell_level)

        one_day_each_list += [
            "Shield",
            "Alarm",
            "Protection from Evil and Good"]
        two_day_each_list = ["Hold Person", "Calm Emotions", "Zone of Truth"]
        for s in two_day_each_list:
            two, _ = add_spell(two, s, max_spell_level-2, 0, max_spell_level, spell_definition="2/Day each")
        three_day_each_list = ["Message", "Prestidigitation", "Light"]
        for s in three_day_each_list:
            three, _ = add_spell(three, s, max_spell_level-1, 0, max_spell_level, spell_definition="3/Day each")

        # 1st Level Spells
        first_list = [
            "Alarm", "Compelled Duel", "Protection from Evil and Good", "Shield", "Wrathful Smite"
        ]
        for s in first_list:
            first, slots1 = add_spell(first, s, 1, slots1, max_spell_level)  

        # 2nd Level Spells
        second_list = [
            "Aid", "Find Traps", "Hold Person", "Magic Weapon", "Zone of Truth"
        ]
        for s in second_list:
            second, slots2 = add_spell(second, s, 2, slots2, max_spell_level)
        
        # 3rd Level Spells
        third_list += [
            "Counterspell", "Crusader's Mantle", "Protection from Energy", "Slow", "Spirit Guardians"
        ]

        # 4th Level Spells
        fourth_list = [
            "Aura of Life", "Banishment", "Mordenkainen's Private Sanctum", "Stoneskin", "Watery Sphere"
        ]
        for s in fourth_list:
            fourth, slots4 = add_spell(fourth, s, 4, slots4, max_spell_level)

        # 5th Level Spells
        fifth_list = [
            "Circle of Power", "Geas", "Hold Monster", "Wall of Force", "Teleportation Circle"
        ]
        for s in fifth_list:
            fifth, slots5 = add_spell(fifth, s, 5, slots5, max_spell_level)
        
        # 6th Level Spells
        sixth_list = [
            "Find the Path", "Forbiddance", "Harm", "Heroes' Feast", "True Seeing"
        ]
        for s in sixth_list:
            sixth, slots6 = add_spell(sixth, s, 6, slots6, max_spell_level)

        # 7th Level Spells
        seventh_list = [
            "Etherealness", "Forcecage", "Mordenkainen's Sword", "Resurrection", "Symbol"
        ]
        for s in seventh_list:
            seventh, slots7 = add_spell(seventh, s, 7, slots7, max_spell_level)

        # 8th Level Spells
        eighth_list = [
            "Antimagic Field", "Control Weather", "Earthquake", "Holy Aura", "Telepathy"
        ]
        for s in eighth_list:
            eighth, slots8 = add_spell(eighth, s, 8, slots8, max_spell_level)

        # 9th Level Spells
        ninth_list = [
            "Foresight", "Imprisonment", "Mass Heal", "Power Word Kill", "True Resurrection"
        ]
        for s in ninth_list:
            ninth, slots9 = add_spell(ninth, s, 9, slots9, max_spell_level)



    # Healer
    if background == "Healer":

        difficulty = Dice(4)  
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
        cantrips_list += [
            "Guidance",
            "Resistance",
            "Spare the Dying",
            "Thaumaturgy",
            "Virtue"]
        first_list += ["Cure Wounds", "Detect Poison and Disease", "Healing Word", "Purify Food and Drink", "Sanctuary"]
        second_list += ["Aid", "Calm Emotions", "Lesser Restoration", "Prayer of Healing", "Protection from Poison"]
        third_list += ["Create Food and Water", "Mass Healing Word", "Protection from Energy", "Remove Curse", "Remove Disease"]
        fourth_list += ["Death Ward", "Freedom of Movement", "Guardian of Faith", "Greater Restoration", "Stone Shape"]
        fifth_list += ["Greater Restoration", "Hallow", "Mass Cure Wounds", "Raise Dead", "Scrying"]
        sixth_list += [
            "Heal",
            "Heroes' Feast",
            "Planar Ally",
            "True Seeing",
            "Word of Recall"
        ]
        seventh_list += [
            "Etherealness",            "Regenerate",
            "Resurrection",            "Symbol",
            "Teleport"        ]
        eighth_list += [
            "Antimagic Field",
            "Control Weather",
            "Earthquake",
            "Holy Aura",
            "Telepathy"
        ]

        ninth_list += [
            "Foresight",
            "Mass Heal",
            "Power Word Heal",
            "True Resurrection",
            "Wish"
        ]





    # Hermit
    if background == "Hermit":

        difficulty = Dice(4)  # Full Caster
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
        cantrips_list = [
            "Druidcraft",
            "Guidance",
            "Mending",
            "Resistance",
            "Thaumaturgy"
        ]
        for c in cantrips_list:
            cantrip, _ = add_spell(cantrip, c, 0, 0, max_spell_level)
        one_day_each_list += [
            "Cure Wounds",
            "Lesser Restoration",
            "Shield of Faith"]
        two_day_each_list += [
            "Prayer of Healing",
            "Remove Poison",
            "Protection from Poison"]
        three_day_each_list += [
            "Purify Food and Drink",
            "Detect Poison and Disease",
            "Resistance"]
        first_list += [
            "Cure Wounds",
            "Detect Poison and Disease",
            "Goodberry",
            "Purify Food and Drink",
            "Speak with Animals"
        ]
        second_list += [
            "Animal Messenger",
            "Find Traps",
            "Lesser Restoration",
            "Protection from Poison",
            "Silence"
        ]
        third_list += [
            "Create Food and Water",
            "Meld into Stone",
            "Protection from Energy",
            "Remove Curse",
            "Water Walk"
        ]
        fourth_list += [
            "Divination",
            "Freedom of Movement",
            "Locate Creature",
            "Stone Shape",
            "Wild Shape"
        ]
        fifth_list += [
            "Commune",
            "Geas",
            "Greater Restoration",
            "Legend Lore",
            "Scrying"
        ]
        sixth_list += [
            "Find the Path",
            "Heal",
            "Heroes' Feast",
            "True Seeing",
            "Wind Walk"
        ]
        seventh_list += [
            "Etherealness", "Regenerate", "Resurrection", "Symbol", "Teleport"
        ]
        eighth_list += [
            "Antimagic Field",
            "Control Weather",
            "Earthquake", "Holy Aura", "Telepathy"
        ]
        ninth_list += [
            "Foresight", "Gate", "Mass Heal", "True Resurrection", "Wish"
        ]

    # Hero
    if background == "Hero":

        difficulty = Dice(10)  
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        cantrips_list += [
            "Guidance",
            "Light",
            "Resistance",
            "Spare the Dying",
            "Thaumaturgy"
        ]

        one_day_each_list += [
            "Bless", "Cure Wounds", "Shield of Faith"]
        two_day_each_list += ["Aid", "Lesser Restoration", "Protection from Energy"]
        three_day_each_list += ["Beacon of Hope", "Crusader's Mantle", "Remove Curse"]
        first_list += [
            "Bless", "Command", "Cure Wounds", "Heroism", "Shield of Faith"
        ]
        second_list += [
            "Aid", "Branding Smite", "Find Steed", "Lesser Restoration", "Protection from Poison"
        ]
        third_list += [
            "Beacon of Hope", "Crusader's Mantle", "Daylight", "Remove Curse", "Revivify"
        ]
        fourth_list += [            "Aura of Purity", "Aura of Life", "Death Ward", "Freedom of Movement", "Stoneskin"]
        fifth_list += [
            "Circle of Power", "Greater Restoration", "Mass Cure Wounds", "Raise Dead", "Flame Strike"
        ]
        sixth_list += [
            "Find the Path",
            "Heal",
            "Heroes' Feast",
            "True Seeing",
            "Word of Recall"
        ]
        seventh_list += [
            "Regenerate", "Resurrection", "Symbol", "Teleport", "Conjure Celestial"
        ]

        eighth_list += [
            "Antimagic Field",
            "Holy Aura", "Control Weather", "Earthquake", "Sunburst"
        ]

        ninth_list += [
            "Foresight",
            "Gate", "Mass Heal", "True Resurrection", "Storm of Vengeance"
        ]

    # Hunter
    if background == "Hunter":

        difficulty = Dice(6)  
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
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
        ninth_list += [
            "Foresight",
            "Shapechange",
            "Storm of Vengeance",
            "True Resurrection",
            "Tsunami"
        ]

    # Knight
    if background == "Knight":

        difficulty = Dice(8)  
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
        cantrips_list += [            "Blade Ward", "Light", "Prestidigitation", "Resistance", "Spare the Dying", "Thaumaturgy"]
        one_day_each_list += ["Command", "Compelled Duel", "Shield of Faith"]
        two_day_each_list += ["Aid", "Branding Smite", "Protection from Poison"]
        three_day_each_list += ["Crusader’s Mantle", "Magic Weapon", "Warding Bond"]
        first_list += [
            "Bless", "Compelled Duel", "Cure Wounds", "Heroism", "Shield of Faith"
        ]
        second_list += [
            "Aid", "Find Steed", "Lesser Restoration", "Magic Weapon", "Warding Bond"
        ]
        third_list += [
            "Crusader's Mantle", "Dispel Magic", "Protection from Energy", "Remove Curse", "Revivify"
        ]
        fourth_list += [
            "Aura of Life",
            "Aura of Purity", "Banishment", "Death Ward", "Stoneskin"
        ]
        fifth_list += [
            "Circle of Power",
            "Destructive Wave",
            "Dispel Evil and Good",
            "Geas",
            "Raise Dead"
        ]
        sixth_list += [
            "Find the Path",
            "Heal", "Heroes' Feast", "True Seeing", "Wind Walk"
        ]

        seventh_list += [
            "Resurrection",
            "Symbol",
            "Teleport"
        ]

        # 8th Level Spells
        eighth_list = [
            "Antimagic Field",
            "Earthquake",
            "Holy Aura"
        ]
        for s in eighth_list:
            eighth, slots8 = add_spell(eighth, s, 8, slots8, max_spell_level)

        # 9th Level Spells
        ninth_list = [
            "Mass Heal", "True Resurrection"
        ]
        for s in ninth_list:
            ninth, slots9 = add_spell(ninth, s, 9, slots9, max_spell_level)


    # Mage
    if background == "Mage":

        difficulty = 1  # Full Caster
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
        cantrips_list = [
            "Acid Splash", "Fire Bolt", "Mage Hand", "Prestidigitation", "Ray of Frost",
            "Minor Illusion", "Detect Magic"
        ]
        for c in cantrips_list:
            cantrip, _ = add_spell(cantrip, c, 0, 0, max_spell_level)
        one_day_each_list += ["Shield", "Magic Missile", "Identify"]
        two_day_each_list = ["Misty Step", "Detect Thoughts", "Scorching Ray"]
        for s in two_day_each_list:
            two, _ = add_spell(two, s, max_spell_level-2, 0, max_spell_level, spell_definition="2/Day each")
        three_day_each_list = ["Counterspell", "Dispel Magic", "Fireball"]
        for s in three_day_each_list:
            three, _ = add_spell(three, s, max_spell_level-1, 0, max_spell_level, spell_definition="3/Day each")

        # 1st Level Spells
        first_list = [
            "Detect Magic",
            "Mage Armor",
            "Magic Missile",
            "Shield",
            "Thunderwave",
             "Identify"
        ]
        for s in first_list:
            first, slots1 = add_spell(first, s, 1, slots1, max_spell_level)  

        # 2nd Level Spells
        second_list += [
            "Arcane Lock",
            "Invisibility", "Levitate", "Mirror Image", "Scorching Ray",
            "Misty Step", "Detect Thoughts", "Scorching Ray", "Arcane Lock", "Invisibility"
        ]
        
        # 3rd Level Spells
        third_list = [
            "Counterspell", "Dispel Magic", "Fireball", "Fly", "Haste"
        ]
        for s in third_list:
            third, slots3 = add_spell(third, s, 3, slots3, max_spell_level)

        # 4th Level Spells
        fourth_list = [
            "Dimension Door", "Greater Invisibility", "Ice Storm", "Polymorph", "Stone Shape"
        ]
        for s in fourth_list:
            fourth, slots4 = add_spell(fourth, s, 4, slots4, max_spell_level)

        # 5th Level Spells
        fifth_list = [
            "Animate Objects", "Cone of Cold", "Teleportation Circle", "Wall of Force", "Telekinesis"
        ]
        for s in fifth_list:
            fifth, slots5 = add_spell(fifth, s, 5, slots5, max_spell_level)
        
        # 6th Level Spells
        sixth_list = [
            "Chain Lightning", "Contingency", "Disintegrate", "Globe of Invulnerability", "True Seeing"
        ]
        for s in sixth_list:
            sixth, slots6 = add_spell(sixth, s, 6, slots6, max_spell_level)

        # 7th Level Spells
        seventh_list = [
            "Delayed Blast Fireball", "Teleport", "Plane Shift", "Prismatic Spray", "Simulacrum"
        ]
        for s in seventh_list:
            seventh, slots7 = add_spell(seventh, s, 7, slots7, max_spell_level)

        # 8th Level Spells
        eighth_list = [
            "Antimagic Field", "Clone", "Demiplane", "Power Word Stun", "Telepathy"
        ]
        for s in eighth_list:
            eighth, slots8 = add_spell(eighth, s, 8, slots8, max_spell_level)

        # 9th Level Spells
        ninth_list = [
            "Gate", "Meteor Swarm", "Power Word Kill", "Time Stop", "Wish"
        ]
        for s in ninth_list:
            ninth, slots9 = add_spell(ninth, s, 9, slots9, max_spell_level)


    # Monk
    if background == "Monk":
        difficulty = Dice(8)  # One-Half Caster
        max_spell_level = get_max_spell_level(Lvl, difficulty)

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
    if background == "Noble":
        difficulty = Dice(12)  
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        cantrips_list = [
            "Prestidigitation",
            "Mage Hand", "Friends", "Message"]
        for c in cantrips_list:
            cantrip, _ = add_spell(cantrip, c, 0, 0, max_spell_level)
        one_day_each_list = ["Charm Person", "Identify"]
        for s in one_day_each_list:
            one, _ = add_spell(one, s, max_spell_level-3, 0, max_spell_level, spell_definition="1/Day")
        two_day_each_list = ["Detect Thoughts", "Suggestion"]
        for s in two_day_each_list:
            two, _ = add_spell(two, s, max_spell_level-2, 0, max_spell_level, spell_definition="2/Day")
        three_day_each_list = ["Tongues", "Sending"]
        for s in three_day_each_list:
            three, _ = add_spell(three, s, max_spell_level-1, 0, max_spell_level, spell_definition="3/Day")
        # 1st Level Spells
        first_list = ["Charm Person", "Disguise Self", "Identify", "Feather Fall", "Alarm"]
        for s in first_list:
            first, slots1 = add_spell(first, s, 1, slots1, max_spell_level)

        # 2nd Level Spells
        second_list = ["Detect Thoughts", "Suggestion", "Locate Object", "See Invisibility", "Nystul's Magic Aura"]
        for s in second_list:
            second, slots2 = add_spell(second, s, 2, slots2, max_spell_level)

        # 3rd Level Spells
        third_list = ["Tongues", "Sending", "Leomund's Tiny Hut", "Clairvoyance", "Counterspell"]
        for s in third_list:
            third, slots3 = add_spell(third, s, 3, slots3, max_spell_level)

        # 4th Level Spells
        fourth_list = [
            "Leomund's Secret Chest", "Mordenkainen's Private Sanctum", "Arcane Eye", "Greater Invisibility", "Charm Monster"]
        for s in fourth_list:
            fourth, slots4 = add_spell(fourth, s, 4, slots4, max_spell_level)

        # 5th Level Spells
        fifth_list += [            "Geas","Legend Lore", "Modify Memory", "Scrying", "Teleportation Circle"]
        sixth_list += [
            "Mass Suggestion",
            "True Seeing",
            "Guards and Wards",
            "Contingency",
            "Find the Path"]
        seventh_list += [
            "Teleport",
            "Mordenkainen's Magnificent Mansion",
            "Symbol",
            "Mirage Arcane",
            "Regenerate"]

        # 8th Level Spells
        eighth_list = [
            "Mind Blank",
            "Antipathy/Sympathy",
            "Demiplane",
            "Maze",
            "Dominate Monster"]
        for s in eighth_list:
            eighth, slots8 = add_spell(eighth, s, 8, slots8, max_spell_level)

        # 9th Level Spells
        ninth_list = [
            "Foresight",
            "Imprisonment",
            "Power Word Kill",
            "True Polymorph",
            "Wish"]
        for s in ninth_list:
            ninth, slots9 = add_spell(ninth, s, 9, slots9, max_spell_level)

    # Priest
    if background == "Priest":
        difficulty = Dice(6)  # Half-Caster
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
        cantrips_list = [
            "Guidance",
            "Light",
            "Mending",
            "Sacred Flame",
            "Thaumaturgy",
            "Resistance" ]
        for c in cantrips_list:
            cantrip, _ = add_spell(cantrip, c, 0, 0, max_spell_level)
        
        one_day_each_list += ["Cure Wounds", "Sanctuary"]
        
        # 2/Day each
        two_day_each_list = ["Lesser Restoration", "Prayer of Healing"]
        for s in two_day_each_list:
            two, _ = add_spell(two, s, max_spell_level-2, 0, max_spell_level, spell_definition="2/Day each")
        
        # 3/Day each
        three_day_each_list = ["Dispel Magic", "Remove Curse"]
        for s in three_day_each_list:
            three, _ = add_spell(three, s, max_spell_level-1, 0, max_spell_level, spell_definition="3/Day each")
        
        # 1st Level Spells
        first_list = [
            "Cure Wounds", "Bless", "Healing Word", "Protection from Evil and Good",
            "Detect Poison and Disease", "Sanctuary", "Guiding Bolt", "Command", "Detect Magic"
            ]
        for s in first_list:
            first, slots1 = add_spell(first, s, 1, slots1, max_spell_level)

        # 2nd Level Spells
        second_list = [
            "Lesser Restoration",
            "Spiritual Weapon",
            "Prayer of Healing",
            "Aid",
            "Find Traps",
            "Augury",
            "Hold Person" ]
        for s in second_list:
            second, slots2 = add_spell(second, s, 2, slots2, max_spell_level)

        third_list += ["Dispel Magic", "Remove Curse", "Mass Healing Word","Spirit Guardians", "Protection from Energy", "Tongues"]

        fourth_list = ["Death Ward", "Guardian of Faith", "Divination", "Banishment", "Freedom of Movement"]
        for s in fourth_list:
            fourth, slots4 = add_spell(fourth, s, 4, slots4, max_spell_level)

        # 5th Level Spells
        fifth_list = ["Greater Restoration", "Mass Cure Wounds", "Scrying", "Flame Strike", "Geas"]
        for s in fifth_list:
            fifth, slots5 = add_spell(fifth, s, 5, slots5, max_spell_level)

        # 6th Level Spells
        sixth_list += [            "Heal", "Planar Ally", "Harm", "True Seeing", "Create Undead"]

        # 7th Level Spells
        seventh_list = ["Resurrection", "Regenerate", "Symbol", "Conjure Celestial", "Etherealness"]
        for s in seventh_list:
            seventh, slots7 = add_spell(seventh, s, 7, slots7, max_spell_level)

        # 8th Level Spells
        eighth_list = ["Holy Aura", "Antimagic Field", "Earthquake", "Control Weather", "Dominate Monster"]
        for s in eighth_list:
            eighth, slots8 = add_spell(eighth, s, 8, slots8, max_spell_level)

        # 9th Level Spells
        ninth_list = [
            "Mass Heal", "True Resurrection", "Gate", "Astral Projection", "Power Word Heal"]
        for s in ninth_list:
            ninth, slots9 = add_spell(ninth, s, 9, slots9, max_spell_level)


    # Pirate
    if background == "Pirate":
        difficulty = Dice(4)+Dice(4)
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
        cantrips_list = ["Mage Hand", "Message", "Prestidigitation", "Druidcraft"]
        for c in cantrips_list:
            cantrip, _ = add_spell(cantrip, c, 0, 0, max_spell_level)

        one_day_each_list += ["Fog Cloud", "Grease"]

        # 2/Day each
        two_day_each_list = ["Misty Step", "Suggestion"]
        for s in two_day_each_list:
            two, _ = add_spell(two, s, max_spell_level-2, 0, max_spell_level, spell_definition="2/Day each")

        # 3/Day each
        three_day_each_list = ["Gaseous Form", "Water Walk"]
        for s in three_day_each_list:
            three, _ = add_spell(three, s, max_spell_level-1, 0, max_spell_level, spell_definition="3/Day each")

        # 1st Level Spells
        first_list = ["Expeditious Retreat", "Disguise Self", "Create or Destroy Water", "Fog Cloud", "Grease"]
        for s in first_list:
            first, slots1 = add_spell(first, s, 1, slots1, max_spell_level)

        # 2nd Level Spells
        second_list = ["Misty Step", "Suggestion", "Alter Self", "Gust of Wind", "Locate Object"]
        for s in second_list:
            second, slots2 = add_spell(second, s, 2, slots2, max_spell_level)

        # 3rd Level Spells
        third_list += ["Gaseous Form",
                      "Water Walk",
                      "Tidal Wave",
                      "Major Image",
                      "Water Breathing"]

        # 4th Level Spells
        fourth_list += ["Control Water",
                       "Watery Sphere",
                       "Dimension Door",
                       "Storm Sphere",
                       "Greater Invisibility"]

        # 5th Level Spells
        fifth_list += ["Control Winds",
                      "Mislead",
                      "Maelstrom",
                      "Teleportation Circle",
                      "Rary's Telepathic Bond"]

        # 6th Level Spells
        sixth_list = ["Investiture of Wind",
                      "Chain Lightning",
                      "True Seeing",
                      "Wind Walk",
                      "Find the Path"]
        for s in sixth_list:
            sixth, slots6 = add_spell(sixth, s, 6, slots6, max_spell_level)

        # 7th Level Spells
        seventh_list = ["Teleport", "Regenerate", "Control Weather", "Reverse Gravity", "Whirlwind"]
        for s in seventh_list:
            seventh, slots7 = add_spell(seventh, s, 7, slots7, max_spell_level)

        # 8th Level Spells
        eighth_list = ["Control Weather", "Telepathy", "Incendiary Cloud", "Tsunami", "Dominate Monster"]
        for s in eighth_list:
            eighth, slots8 = add_spell(eighth, s, 8, slots8, max_spell_level)

        # 9th Level Spells
        ninth_list = ["Meteor Swarm", "Storm of Vengeance", "Time Stop", "Mass Polymorph", "Foresight"]
        for s in ninth_list:
            ninth, slots9 = add_spell(ninth, s, 9, slots9, max_spell_level)

    # Ranger
    if background == "Ranger":
        difficulty = Dice(4)  
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
        cantrips_list = ["Druidcraft", "Guidance", "Resistance", "Thorn Whip"]

        one_day_each_list += ["Longstrider", "Speak with Animals"]

        # 2/Day each
        two_day_each_list = ["Pass without Trace", "Spike Growth"]
        for s in two_day_each_list:
            two, _ = add_spell(two, s, max_spell_level-2, 0, max_spell_level, spell_definition="2/Day each")

        # 3/Day each
        three_day_each_list = ["Water Walk", "Water Breathing"]
        for s in three_day_each_list:
            three, _ = add_spell(three, s, max_spell_level-1, 0, max_spell_level, spell_definition="3/Day each")

        # 1st Level Spells
        first_list = [
            "Cure Wounds",
            "Goodberry", "Hunter's Mark", "Fog Cloud", "Alarm"]
        for s in first_list:
            first, slots1 = add_spell(first, s, 1, slots1, max_spell_level)

        # 2nd Level Spells
        second_list = ["Pass without Trace", "Spike Growth", "Lesser Restoration", "Silence", "Locate Animals or Plants"]
        for s in second_list:
            second, slots2 = add_spell(second, s, 2, slots2, max_spell_level)

        # 3rd Level Spells
        third_list += ["Water Walk", "Water Breathing", "Protection from Energy", "Speak with Plants", "Conjure Animals"]
        fourth_list += ["Freedom of Movement", "Stoneskin", "Locate Creature", "Grasping Vine", "Conjure Woodland Beings"]
        fifth_list += ["Commune with Nature", "Swift Quiver", "Tree Stride", "Greater Restoration", "Conjure Volley"]
        sixth_list += ["Heal", "Sunburst", "Heroes' Feast", "Find the Path", "Transport via Plants"]
        seventh_list += ["Mirage Arcane", "Regenerate", "Fire Storm", "Reverse Gravity", "Plane Shift"]
        eighth_list += ["Tsunami", "Earthquake", "Sunburst", "Control Weather", "Animal Shapes"]
        ninth_list += ["Storm of Vengeance","Shapechange",                      "Foresight",                      "True Resurrection",                      "Mass Heal"]

    # Scholar
    if background == "Scholar":
        difficulty = Dice(3)
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
        cantrips_list = ["Prestidigitation",
                         "Mage Hand",
                         "Mending",
                         "Message"]
        for c in cantrips_list:
            cantrip, _ = add_spell(cantrip, c, 0, 0, max_spell_level)

        one_day_each_list += ["Identify", "Comprehend Languages"]

        # 2/Day each
        two_day_each_list = ["Detect Thoughts", "Locate Object"]
        for s in two_day_each_list:
            two, _ = add_spell(two, s, max_spell_level-2, 0, max_spell_level, spell_definition="2/Day each")

        # 3/Day each
        three_day_each_list = ["Tongues", "Clairvoyance"]
        for s in three_day_each_list:
            three, _ = add_spell(three, s, max_spell_level-1, 0, max_spell_level, spell_definition="3/Day each")

        # 1st Level Spells
        first_list = ["Identify", "Comprehend Languages", "Find Familiar", "Detect Magic", "Alarm"]
        for s in first_list:
            first, slots1 = add_spell(first, s, 1, slots1, max_spell_level)

        # 2nd Level Spells
        second_list = ["Detect Thoughts", "Locate Object", "Arcane Lock", "Gentle Repose", "Nystul's Magic Aura"]
        for s in second_list:
            second, slots2 = add_spell(second, s, 2, slots2, max_spell_level)

        # 3rd Level Spells
        third_list = ["Tongues", "Clairvoyance", "Leomund's Tiny Hut", "Rary's Telepathic Bond", "Sending"]
        for s in third_list:
            third, slots3 = add_spell(third, s, 3, slots3, max_spell_level)

        # 4th Level Spells
        fourth_list = ["Leomund's Secret Chest", "Arcane Eye", "Stone Shape", "Fabricate", "Mordenkainen's Private Sanctum"]
        for s in fourth_list:
            fourth, slots4 = add_spell(fourth, s, 4, slots4, max_spell_level)

        # 5th Level Spells
        fifth_list = [
            "Legend Lore", "Contact Other Plane", "Scrying", "Teleportation Circle", "Rary's Telepathic Bond"]
        for s in fifth_list:
            fifth, slots5 = add_spell(fifth, s, 5, slots5, max_spell_level)

        # 6th Level Spells
        sixth_list = [
            "True Seeing",
            "Find the Path", "Analyze Dweomer", "Guards and Wards", "Create Undead"]
        for s in sixth_list:
            sixth, slots6 = add_spell(sixth, s, 6, slots6, max_spell_level)

        # 7th Level Spells
        seventh_list = ["Teleport", "Symbol", "Sequester", "Rary's Telepathic Bond", "Mordenkainen's Sword"]
        for s in seventh_list:
            seventh, slots7 = add_spell(seventh, s, 7, slots7, max_spell_level)

        # 8th Level Spells
        eighth_list = [
            "Mind Blank", "Antipathy/Sympathy", "Telepathy", "Clone", "Demiplane"]
        for s in eighth_list:
            eighth, slots8 = add_spell(eighth, s, 8, slots8, max_spell_level)

        # 9th Level Spells
        ninth_list = [
            "Foresight",
            "Astral Projection", "Time Stop", "Gate", "Wish"]
        for s in ninth_list:
            ninth, slots9 = add_spell(ninth, s, 9, slots9, max_spell_level)


    # Shaman
    if background == "Shaman":
        difficulty = Dice(3)  # Full Caster
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
        cantrips_list = ["Guidance", "Druidcraft", "Spare the Dying", "Resistance", "Produce Flame",
                         "Thorn Whip"]
        for c in cantrips_list:
            cantrip, _ = add_spell(cantrip, c, 0, 0, max_spell_level)

        one_day_each_list += ["Cure Wounds", "Detect Poison and Disease"]

        # 2/Day each
        two_day_each_list = ["Lesser Restoration", "Pass Without Trace"]
        for s in two_day_each_list:
            two, _ = add_spell(two, s, max_spell_level-2, 0, max_spell_level, spell_definition="2/Day")

        # 3/Day each
        three_day_each_list = ["Dispel Magic", "Speak with Dead"]
        for s in three_day_each_list:
            three, _ = add_spell(three, s, max_spell_level-1, 0, max_spell_level, spell_definition="3/Day")

        # 1st Level Spells
        first_list = ["Cure Wounds", "Detect Poison and Disease",
                      "Entangle", "Create or Destroy Water", "Fog Cloud",
                      "Bane", "Shield Of Faith"]
        for s in first_list:
            first, slots1 = add_spell(first, s, 1, slots1, max_spell_level)

        # 2nd Level Spells
        second_list = [
            "Lesser Restoration", "Pass Without Trace", "Flame Blade",
                       "Animal Messenger", "Heat Metal", "Spike Growth"]
        for s in second_list:
            second, slots2 = add_spell(second, s, 2, slots2, max_spell_level)

        # 3rd Level Spells
        third_list = ["Dispel Magic", "Speak with Dead",
                      "Call Lightning", "Water Walk", "Meld into Stone",
                      "Conjure Animals", "Plant Growth"]
        for s in third_list:
            third, slots3 = add_spell(third, s, 3, slots3, max_spell_level)

        # 4th Level Spells
        fourth_list = ["Divination", "Freedom of Movement", "Stone Shape", "Locate Creature", "Control Water"]
        for s in fourth_list:
            fourth, slots4 = add_spell(fourth, s, 4, slots4, max_spell_level)

        # 5th Level Spells
        fifth_list = ["Commune",
                      "Greater Restoration",
                      "Awaken",
                      "Mass Cure Wounds",
                      "Reincarnate"]
        for s in fifth_list:
            fifth, slots5 = add_spell(fifth, s, 5, slots5, max_spell_level)

        # 6th Level Spells
        sixth_list = ["Heal", "Find the Path", "Heroes' Feast", "Move Earth", "Create Undead"]
        for s in sixth_list:
            sixth, slots6 = add_spell(sixth, s, 6, slots6, max_spell_level)

        # 7th Level Spells
        seventh_list = ["Regenerate", "Etherealness", "Fire Storm", "Resurrection", "Symbol"]
        for s in seventh_list:
            seventh, slots7 = add_spell(seventh, s, 7, slots7, max_spell_level)

        eighth_list += ["Earthquake", "Control Weather", "Sunburst", "Antipathy/Sympathy", "Animal Shapes"]
        ninth_list += ["True Resurrection", "Storm of Vengeance", "Shapechange", "Foresight", "Astral Projection"]
            
    # Soldier
    if background == "Soldier":
        difficulty = Dice(8)  # One-Fourth Caster
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
        cantrips_list += ["Blade Ward", "True Strike", "Resistance", "Guidance"]

        one_day_each_list += ["Shield", "Heroism"]

        # 2/Day each
        two_day_each_list += ["Magic Weapon",
                             "Aid"]

        # 3/Day each
        three_day_each_list += ["Protection from Energy", "Haste"]

        # 1st Level Spells
        first_list = ["Shield", "Heroism", "Cure Wounds", "Expeditious Retreat", "Protection from Evil and Good"]
        for s in first_list:
            first, slots1 = add_spell(first, s, 1, slots1, max_spell_level)

        # 2nd Level Spells
        second_list = ["Magic Weapon", "Aid", "Enhance Ability", "Blur", "Protection from Poison"]
        for s in second_list:
            second, slots2 = add_spell(second, s, 2, slots2, max_spell_level)

        third_list += ["Protection from Energy", "Haste", "Dispel Magic", "Revivify", "Crusader's Mantle"]

        # 4th Level Spells
        fourth_list = ["Death Ward", "Freedom of Movement", "Stoneskin", "Aura of Life", "Aura of Purity"]
        for s in fourth_list:
            fourth, slots4 = add_spell(fourth, s, 4, slots4, max_spell_level)

        # 5th Level Spells
        fifth_list = ["Greater Restoration", "Raise Dead", "Destructive Wave", "Flame Strike", "Planar Binding"]
        for s in fifth_list:
            fifth, slots5 = add_spell(fifth, s, 5, slots5, max_spell_level)

        # 6th Level Spells
        sixth_list = ["Heal", "Heroes' Feast", "Find the Path", "Contingency", "Create Undead"]
        for s in sixth_list:
            sixth, slots6 = add_spell(sixth, s, 6, slots6, max_spell_level)

        # 7th Level Spells
        seventh_list = [
            "Resurrection",
            "Regenerate",
            "Symbol",
            "Teleport",
            "Conjure Celestial"]
        for s in seventh_list:
            seventh, slots7 = add_spell(seventh, s, 7, slots7, max_spell_level)

        # 8th Level Spells
        eighth_list = [
            "Holy Aura",
            "Antimagic Field",
            "Glibness", "Earthquake", "Dominate Monster"]
        for s in eighth_list:
            eighth, slots8 = add_spell(eighth, s, 8, slots8, max_spell_level)

        # 9th Level Spells
        ninth_list = ["Mass Heal", "True Resurrection", "Power Word Kill", "Astral Projection", "Gate"]
        for s in ninth_list:
            ninth, slots9 = add_spell(ninth, s, 9, slots9, max_spell_level)





    # Spy
    if background == "Spy":
        difficulty = Dice(12)  # Quarter-Caster
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
        cantrips_list = [
            "Mage Hand", "Message", "Minor Illusion", "Prestidigitation"]
        for c in cantrips_list:
            cantrip, _ = add_spell(cantrip, c, 0, 0, max_spell_level)

        one_day_each_list += ["Disguise Self", "Charm Person"]

        # 2/Day each
        two_day_each_list = ["Invisibility", "Suggestion"]
        for s in two_day_each_list:
            two, _ = add_spell(two, s, max_spell_level-2, 0, max_spell_level, spell_definition="2/Day")

        # 3/Day each
        three_day_each_list = [
            "Clairvoyance", "Sending"]
        for s in three_day_each_list:
            three, _ = add_spell(three, s, max_spell_level-1, 0, max_spell_level, spell_definition="3/Day")

        # 1st Level Spells
        first_list = ["Disguise Self", "Charm Person", "Detect Magic", "Feather Fall", "Silent Image"]
        for s in first_list:
            first, slots1 = add_spell(first, s, 1, slots1, max_spell_level)

        # 2nd Level Spells
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
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
        cantrips_list = ["Druidcraft", "Guidance", "Mage Hand", "Message"]
        for c in cantrips_list:
            cantrip, _ = add_spell(cantrip, c, 0, 0, max_spell_level)

        one_day_each_list += ["Longstrider", "Goodberry"]

        # 2/Day each
        two_day_each_list = ["Pass without Trace", "Lesser Restoration"]
        for s in two_day_each_list:
            two, _ = add_spell(two, s, max_spell_level-2, 0, max_spell_level, spell_definition="2/Day")

        three_day_each_list += ["Create Food and Water", "Protection from Energy"]

        # 1st Level Spells
        first_list = ["Longstrider", "Goodberry", "Cure Wounds", "Alarm", "Detect Poison and Disease"]
        for s in first_list:
            first, slots1 = add_spell(first, s, 1, slots1, max_spell_level)

        # 2nd Level Spells
        second_list = [
            "Pass without Trace", "Lesser Restoration", "Find Traps", "Locate Animals or Plants", "Aid"]
        for s in second_list:
            second, slots2 = add_spell(second, s, 2, slots2, max_spell_level)

        third_list += [
            "Create Food and Water", "Protection from Energy", "Speak with Plants", "Water Walk", "Beacon of Hope"]

        # 4th Level Spells
        fourth_list = ["Freedom of Movement", "Locate Creature", "Stone Shape", "Control Water", "Death Ward"]
        for s in fourth_list:
            fourth, slots4 = add_spell(fourth, s, 4, slots4, max_spell_level)

        # 5th Level Spells
        fifth_list = ["Commune with Nature", "Greater Restoration", "Teleportation Circle", "Scrying", "Mass Cure Wounds"]
        for s in fifth_list:
            fifth, slots5 = add_spell(fifth, s, 5, slots5, max_spell_level)

        # 6th Level Spells
        sixth_list = ["Find the Path", "Wind Walk", "Heal", "Heroes' Feast", "Move Earth"]
        for s in sixth_list:
            sixth, slots6 = add_spell(sixth, s, 6, slots6, max_spell_level)

        # 7th Level Spells
        seventh_list += ["Regenerate",
                        "Teleport",
                        "Mirage Arcane",
                        "Resurrection",
                        "Transport via Plants"]

        # 8th Level Spells
        eighth_list = [
            "Control Weather",
            "Earthquake", "Antipathy/Sympathy", "Telepathy", "Holy Aura"]
        for s in eighth_list:
            eighth, slots8 = add_spell(eighth, s, 8, slots8, max_spell_level)

        # 9th Level Spells
        ninth_list = [
            "Storm of Vengeance", "Gate", "Foresight", "True Resurrection", "Mass Heal"]
        for s in ninth_list:
            ninth, slots9 = add_spell(ninth, s, 9, slots9, max_spell_level)

    # Urchin
    if background == "Urchin":
        difficulty = Dice(10)  
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
        cantrips_list = [
            "Mage Hand", "Prestidigitation", "Minor Illusion", "Message"]
        for c in cantrips_list:
            cantrip, _ = add_spell(cantrip, c, 0, 0, max_spell_level)

        one_day_each_list += ["Disguise Self", "Unseen Servant"]

        # 2/Day each
        two_day_each_list = ["Invisibility", "Pass without Trace"]
        for s in two_day_each_list:
            two, _ = add_spell(two, s, max_spell_level-2, 0, max_spell_level, spell_definition="2/Day")

        # 3/Day each
        three_day_each_list = ["Nondetection", "Blink"]
        for s in three_day_each_list:
            three, _ = add_spell(three, s, max_spell_level-1, 0, max_spell_level, spell_definition="3/Day")

        # 1st Level Spells
        first_list = [
            "Disguise Self", "Silent Image", "Charm Person", "Sleep", "Expeditious Retreat"]
        for s in first_list:
            first, slots1 = add_spell(first, s, 1, slots1, max_spell_level)

        # 2nd Level Spells
        second_list = ["Invisibility", "Pass without Trace", "Silence", "Alter Self", "Calm Emotions"]
        for s in second_list:
            second, slots2 = add_spell(second, s, 2, slots2, max_spell_level)

        # 3rd Level Spells
        third_list = ["Nondetection", "Blink", "Haste", "Clairvoyance", "Leomund's Tiny Hut"]
        for s in third_list:
            third, slots3 = add_spell(third, s, 3, slots3, max_spell_level)

        # 4th Level Spells
        fourth_list = ["Greater Invisibility", "Freedom of Movement", "Arcane Eye", "Dimension Door", "Confusion"]
        for s in fourth_list:
            fourth, slots4 = add_spell(fourth, s, 4, slots4, max_spell_level)

        # 5th Level Spells
        fifth_list = ["Mislead", "Teleportation Circle", "Modify Memory", "Legend Lore", "Dream"]
        for s in fifth_list:
            fifth, slots5 = add_spell(fifth, s, 5, slots5, max_spell_level)

        # 6th Level Spells
        sixth_list = ["True Seeing", "Find the Path", "Programmed Illusion", "Chain Lightning", "Mass Suggestion"]
        for s in sixth_list:
            sixth, slots6 = add_spell(sixth, s, 6, slots6, max_spell_level)

        # 7th Level Spells
        seventh_list = ["Mirage Arcane", "Project Image", "Teleport", "Regenerate", "Sequester"]
        for s in seventh_list:
            seventh, slots7 = add_spell(seventh, s, 7, slots7, max_spell_level)

        # 8th Level Spells
        eighth_list = ["Mind Blank", "Antipathy/Sympathy", "Maze", "Dominate Monster", "Power Word Stun"]
        for s in eighth_list:
            eighth, slots8 = add_spell(eighth, s, 8, slots8, max_spell_level)

        # 9th Level Spells
        ninth_list = ["Foresight", "Power Word Kill", "Time Stop", "Imprisonment", "True Polymorph"]
        for s in ninth_list:
            ninth, slots9 = add_spell(ninth, s, 9, slots9, max_spell_level)

    # Warrior
    if background == "Warrior":
        difficulty = Dice(8)  
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
        cantrips_list += ["Blade Ward", "True Strike", "Light", "Resistance"]

        one_day_each_list += ["Shield", "Heroism"]

        # 2/Day each
        two_day_each_list = ["Magic Weapon", "Aid"]
        for s in two_day_each_list:
            two, _ = add_spell(two, s, max_spell_level-2, 0, max_spell_level, spell_definition="2/Day")

        three_day_each_list += ["Protection from Energy", "Haste"]

        # 1st Level Spells
        first_list = ["Shield", "Heroism", "Magic Missile", "Cure Wounds", "Thunderwave"]
        for s in first_list:
            first, slots1 = add_spell(first, s, 1, slots1, max_spell_level)

        # 2nd Level Spells
        second_list = ["Magic Weapon", "Aid", "Blur", "Enlarge/Reduce", "Spiritual Weapon"]
        for s in second_list:
            second, slots2 = add_spell(second, s, 2, slots2, max_spell_level)

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
        max_spell_level = get_max_spell_level(Lvl, difficulty)
        cantrips_list += [
            "Eldritch Blast", "Mage Hand", "Minor Illusion", "Prestidigitation",
                         "Thaumaturgy", "Poison Spray"]
        one_day_each_list += ["Armor of Agathys", "Hellish Rebuke"]
        two_day_each_list += ["Summon Lesser Demons", "Summon Greater Demon"]
        three_day_each_list += ["Infernal Calling", "Contact Other Plane"]
        first_list += ["Armor of Agathys", "Hellish Rebuke", "Hex", "Charm Person",
                      "Comprehend Languages", "Sanctuary", "Detect Magic", "Bane",
                      "Shield", "Magic Missile"]
        second_list += [            "Summon Lesser Demons",
            "Darkness",            "Silence",
            "Mirror Image",            "Misty Step",
            "Suggestion",            "Flaming Sphere",
            "Hold Person",            "Blur"]
        third_list += ["Summon Greater Demon", "Counterspell", "Fly","Hypnotic Pattern", "Magic Circle", "Dispel Magic",                      "Clairvoyance", "Fireball"]
        fourth_list += ["Infernal Calling",  "Banishment",                       "Dimension Door",                       "Hallucinatory Terrain",                       "Shadow of Moil",                       "Freedom Of Movement",                       "Divination"]
        fifth_list += ["Contact Other Plane", "Dream", "Enervation", "Hold Monster", "Scrying"]
        sixth_list += ["Arcane Gate", "Circle of Death", "Conjure Fey", "Eyebite", "Flesh to Stone"]
        seventh_list += ["Crown of Stars", "Etherealness", "Finger of Death", "Forcecage", "Plane Shift"]
        eighth_list += ["Demiplane", "Dominate Monster", "Feeblemind", "Glibness", "Power Word Stun"]
        ninth_list += ["Astral Projection", "Foresight", "Imprisonment", "Power Word Kill", "True Polymorph"]

    # Witch
    if background == "Witch":
        difficulty = Dice(3)  
        max_spell_level = get_max_spell_level(Lvl, difficulty)
        
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
    if race == "Aberration" or "Beholder":
        difficulty += Dice(4) - Dice(6)
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        if race == "Beholder":
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



        # Cantrips
        cantrips_list += ["Eldritch Blast",
                         "Mage Hand",
                         "Minor Illusion",
                         "Thaumaturgy",
                         "Message"]
        
        one_day_each_list += ["Detect Thoughts",
                             "Dissonant Whispers"]
        
        two_day_each_list += ["Hold Person",
                             "Levitate",
                             "Crown of Madness",
                             "Hold Person"]

        three_day_each_list += [ "Telekinesis",
                                "Mind Spike",
                                "Fear",
                                "Hypnotic Pattern"]

        first_list += ["Detect Magic",
                      "Dissonant Whispers",
                      "Mage Armor",
                      "Shield",
                      "Tasha's Hideous Laughter",
                      "Charm Person",
                      "Illusory Script"]

        second_list += ["Hold Person",
                       "Mirror Image",
                       "Misty Step",
                       "Detect Thoughts",
                       "Blur",
                       "Crown of Madness",
                       "Phantasmal Force"]

        third_list += [            "Counterspell",            "Dispel Magic",            "Hypnotic Pattern",            "Telekinesis",            "Tongues",            "Fear",            "Major Image",            "Sending",            "Clairvoyance"]
        fourth_list += [            "Banishment",           "Dimension Door",            "Arcane Eye",            "Confusion",            "Greater Invisibility",            "Phantasmal Killer"]

        fifth_list += [            "Contact Other Plane",            "Scrying",            "Teleportation Circle",
            "Dream",            "Modify Memory",             "Dominate Person",            "Telekinesis",            "Mislead" ]

        sixth_list += [
            "True Seeing",
            "Arcane Gate",
            "Mass Suggestion",
            "Plane Shift",
            "Disintegrate",
            "Mental Prison",
            "Eyebite",
            "Programmed Illusion"
                      ]
        seventh_list += ["Teleport",
                        "Etherealness",
                        "Project Image",
                        "Symbol",
                        "Forcecage",
                        "Mirage Arcane",
                        "Etherealness",
                        "Simulacrum"]
        
        eighth_list += ["Feeblemind",
                       "Mind Blank",
                       "Antipathy/Sympathy",
                       "Demiplane",
                       "Maze",
                       "Telepathy",
                       "Antimagic Field",
                       "Power Word Stun"]

        ninth_list += ["Astral Projection",
                      "Foresight",
                      "Gate",
                      "Imprisonment",
                      "Psychic Scream",
                      "Power Word Kill",
                      "Time Stop",
                      "Gate",
                      "True Polymorph"]


        
    # Aven
    if race == "Aven":
        difficulty += Dice(6) - Dice(3)
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        recharge, _ = add_spell(recharge, "Summon Air Elemental", 3, 0, max_spell_level,
                               "Five Aven within 30 feet of each other can magically summon an air elemental. Each of the five must use its action and movement on three consecutive turns to perform an aerial dance and must maintain concentration while doing so (as if concentrating on a spell). When all five have finished their third turn of the dance, the elemental appears in an unoccupied space within 60 feet of them. It is friendly toward them and obeys their spoken commands. It remains for 1 hour, until it or all its summoners die, or until any of its summoners dismisses it as a bonus action. A summoner can't perform the dance again until it finishes a short rest. When the elemental returns to the Elemental Plane of Air, any Aven within 5 feet of it can return with it.")

        cantrips_list += ["Guidance", "Gust", "Mage Hand", "Message"]
        one_day_each_list += [
            "Feather Fall", "Jump"]
        two_day_each_list += ["Levitate", "Fly"]
        three_day_each_list += ["Wind Wall", "Gaseous Form"]
        first_list += [
            "Feather Fall", "Jump", "Expeditious Retreat", "Longstrider", "Fog Cloud"]
        second_list += [ "Levitate",
                        "Fly",
                        "Gust of Wind",
                        "Skywrite",
                        "Spider Climb"]
        third_list += ["Wind Wall", "Gaseous Form", "Daylight", "Protection from Energy", "Feign Death"]
        fourth_list += [
            "Freedom of Movement", "Control Winds", "Greater Invisibility", "Stone Shape", "Conjure Minor Elementals"]
        fifth_list += [            "Control Winds",            "Telekinesis",            "Commune with Nature",            "Conjure Elemental",            "Passwall"            ]

        sixth_list += ["Wind Walk", "True Seeing", "Chain Lightning", "Move Earth", "Sunbeam"]
        seventh_list += ["Teleport", "Control Weather", "Reverse Gravity", "Whirlwind", "Regenerate"]
        eighth_list += ["Control Weather",
                       "Telepathy",
                       "Antipathy/Sympathy",
                       "Earthquake",
                       "Tsunami"]
        ninth_list += ["Meteor Swarm",
                      "Time Stop",
                      "Gate",
                      "Shapechange",
                      "Mass Polymorph"]

    # BEASTS AND BEASTFOLK
    if race == "Beast":
        difficulty += Dice(8) - Dice(12)
        max_spell_level = get_max_spell_level(Lvl, difficulty)
        
        recharge, _ = add_spell(recharge, "Cold Breath", 0, 0, max_spell_level,
                               f"(Recharge 5–6). \n\t The beast exhales a blast of freezing wind in a 15-foot cone. Each creature in that area must make a DC {10+PB(Lvl)} Dexterity saving throw, taking 18 (4d8) cold damage on a failed save, or half as much damage on a successful one.")

        cantrips_list += ["Druidcraft", "Guidance", "Mending", "Resistance"]
        one_day_each_list += ["Animal Friendship", "Speak with Animals"]
        two_day_each_list += ["Barkskin", "Beast Sense"]
        three_day_each_list += ["Conjure Animals",
                                "Water Walk"]
        first_list += [            "Cure Wounds",            "Entangle",           "Goodberry",            "Longstrider",             "Speak with Animals"]
        second_list += [           "Animal Messenger",            "Barkskin",            "Darkvision",            "Locate Animals or Plants",            "Pass without Trace"]
        third_list += [            "Beacon of Hope",            "Conjure Animals",            "Daylight",            "Protection from Energy",            "Water Walk"]
        fourth_list += [            "Conjure Minor Elementals",            "Dominate Beast",            "Freedom of Movement",            "Grasping Vine",            "Stoneskin"]
        fifth_list += [            "Awaken",            "Commune with Nature",            "Conjure Elemental",            "Greater Restoration",            "Reincarnate"]
        sixth_list += [            "Find the Path",            "Heal",            "Heroes' Feast",            "Move Earth",            "Transport via Plants"]
        seventh_list += ["Mirage Arcane", "Plane Shift", "Regenerate", "Reverse Gravity", "Whirlwind"]
        eighth_list += ["Animal Shapes", "Antipathy/Sympathy", "Control Weather", "Earthquake", "Tsunami"]
        ninth_list += ["Foresight", "Shapechange", "Storm of Vengeance", "True Resurrection", "Mass Heal"]

        if Dice(12)==1:
            recharge += "\n-Web (Recharge 6)"


    if race == "Beastfolk":
        difficulty += Dice(3) - Dice(6)
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
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
        difficulty += Dice(5) - Dice(10)
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
        cantrips_list = [
            "Guidance",
            "Light", "Mending", "Sacred Flame", "Thaumaturgy", "Druidcraft"]
        for c in cantrips_list:
            cantrip, _ = add_spell(cantrip, c, 0, 0, max_spell_level)

        one_day_each_list += ["Cure Wounds",
                             "Bless",
                             "Detect Evil and Good",
                             "Teleport",
                             "Entangle",
                             "Calm Emotions",
                             "Scrying",
                             "Greater Restoration",
                             "Dream"]
        two_day_each_list += ["Lesser Restoration",
                             "Aid",
                             "Zone of Truth"]
        three_day_each_list += ["Remove Curse",
                               "Dispel Magic",
                               "Revivify",
                               "Healing Touch",
                               "Shield",
                               "Sanctuary",
                               "Protection From Poison",
                               "Lesser Restoration",
                               "Create Food And Water",
                               "Cure Wounds",
                               "Bless",
                               "Detect Magic",
                               "Detect Thoughts"]
        first_list += ["Detect Magic", "Healing Word", "Protection from Evil and Good", "Purify Food and Drink", "Shield of Faith"]
        second_list += ["Enhance Ability", "Find Traps", "Hold Person", "Prayer of Healing", "Warding Bond"]
        third_list += ["Daylight", "Protection from Energy", "Remove Curse", "Speak with Dead", "Spirit Guardians"]
        fourth_list += ["Death Ward",
                       "Freedom of Movement",
                       "Guardian of Faith",
                       "Locate Creature",
                       "Stoneskin"]
        fifth_list += ["Flame Strike",
                       "Geas",
                       "Greater Restoration", "Hallow", "Raise Dead"]
        sixth_list += ["Blade Barrier", "Find the Path", "Heal", "Heroes' Feast", "Planar Ally"]
        seventh_list += ["Etherealness", "Regenerate", "Resurrection", "Symbol", "Teleport"]
        eighth_list += ["Antimagic Field", "Control Weather", "Holy Aura", "Sunburst", "Telepathy"]
        ninth_list += ["Astral Projection", "Gate", "Mass Heal", "Power Word Heal", "True Resurrection"]

    # CONSTRUCTS.
    if race == "Construct":
        difficulty += Dice(8) - Dice(4)
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        recharge, _ = add_spell(recharge, "Paralysis Gas", 4, 0, max_spell_level,
                               f"(Recharge 5–6). \n\t The construct exhales a 30-foot cone of gas. Each creature in that area must succeed on a DC {10+PB(Lvl)} Constitution saving throw or be paralyzed for 1 minute. A creature can repeat the saving throw at the start of each of its turns, ending the effect on itself on a success.")
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
        eighth_list += ["Antimagic Field",
                        "Control Weather",
                        "Demiplane", "Mind Blank", "Telepathy"]
        ninth_list += ["Gate", "Imprisonment", "Mass Heal", "Meteor Swarm", "True Resurrection"]

    # DRAGONS.

    #Breath weapons
    if race == "Dragon" and Dice(3) == 1:
        d = 20
        if Dice(d) == 1 and not ("Fire Breath" in recharge):
            recharge += f"\n  - Fire Breath \n\t(Recharge 5-6) The dragon exhales fire in a 20-foot line that is 5 feet wide. Each creature in that line must make a DC {10+PB(Lvl)} Dexterity saving throw, taking 14 (4d6) fire damage on a failed save, or half as much damage on a successful one."
        elif Dice(d) == 1 and not ("Fire Breath" in recharge):       recharge += f"\n  - Fire Breath \n\t(Recharge 5-6) The dragon exhales fire in a 15-foot cone. Each creature in that area must make a DC {10+PB(Lvl)} Dexterity saving throw, taking 22 (4d10) fire damage on a failed save, or half as much damage on a successful one."
        elif Dice(d) == 1 and not ("Fire Breath" in recharge):       recharge += f"\n  - Fire Breath \n\t(Recharge 5-6) The dragon exhales fire in a 15-foot cone. Each creature in that area must make a DC {10+PB(Lvl)} Dexterity saving throw, taking 24 (7d6) fire damage on a failed save, or half as much damage on a successful one."
        if Dice(d) == 2 and not ("Sleep Breath" in recharge):        recharge += f"\n  - Sleep Breath \n\t(Recharge 5-6) The dragon exhales sleep gas in a 15-foot cone. Each creature in that area must succeed on a DC {10+PB(Lvl)} Constitution saving throw or fall unconscious for 1 minute. This effect ends for a creature if the creature takes damage or someone uses an action to wake it."
        if Dice(d) == 3 and not ("Acid Breath" in recharge):         recharge += f"\n  - Acid Breath \n\t(Recharge 5-6) The dragon exhales acid in a 20-foot line that is 5 feet wide. Each creature in that line must make a DC {10+PB(Lvl)} Dexterity saving throw, taking 18 (4d8) acid damage on a failed save, or half as much damage on a successful one"
        if Dice(d) == 4 and not ("Slowing Breath" in recharge):      recharge += f"\n  - Slowing Breath \n\t(Recharge 5-6) The dragon exhales gas in a 15-foot cone. Each creature in that area must succeed on a DC {10+PB(Lvl)} Constitution saving throw. On a failed save, the creature can't use reactions, its speed is halved, and it can't make more than one attack on its turn. In addition, the creature can use either an action or a bonus action on its turn, but not both. These effects last for 1 minute. The creature can repeat the saving throw at the start of each of its turns, ending the effect on itself with a successful save."
        if Dice(d) == 5 and not ("Euphoria Breath" in recharge):     recharge += f"\n  - Euphoria Breath \n\t(Recharge 5-6) The dragon exhales a puff of euphoria gas at one creature within 5 feet of it. The target must succeed on a DC {10+PB(Lvl)} Wisdom saving throw, or for 1 minute, the target can't take reactions and must roll a d6 at the start of each of its turns to determine its behavior during the turn: \n\t\t 1–4. The target takes no action or bonus action and uses all of its movement to move in a random direction. \n\t\t 5–6. The target doesn't move, and the only thing it can do on its turn is make a DC {10+PB(Lvl)} Wisdom saving throw, ending the effect on itself on a success."
        if Dice(d) == 6 and not ("Repulsion Breath" in recharge):    recharge += f"\n  - Repulsion Breath \n\t(Recharge 5-6) The dragon exhales repulsion energy in a 30-foot cone. Each creature in that area must succeed on a DC {10+PB(Lvl)} Strength saving throw. On a failed save, the creature is pushed 30 feet away from the dragon."
        if Dice(d) == 7 and not ("Poison Breath" in recharge):       recharge += f"\n  - Poison Breath \n\t(Recharge 5-6) The dragon exhales poisonous gas in a 15-foot cone. Each creature in that area must make a DC {10+PB(Lvl)} Constitution saving throw, taking 21 (6d6) poison damage on a failed save, or half as much damage on a successful one."
        if Dice(d) == 8 and not ("Lightning Breath" in recharge):    recharge += f"\n  - Lightning Breath \n\t(Recharge 5-6) The dragon exhales lightning in a 40-foot line that is 5 feet wide. Each creature in that line must make a DC {10+PB(Lvl)} Dexterity saving throw, taking 16 (3d10) lightning damage on a failed save, or half as much damage on a successful one."
        elif Dice(d) == 8 and not ("Lightning Breath" in recharge):  recharge += f"\n  - Lightning Breath \n\t(Recharge 5-6) The dragon exhales lightning in a 30-foot line that is 5 feet wide. Each creature in that line must make a DC {10+PB(Lvl)} Dexterity saving throw, taking 22 (4d10) lightning damage on a failed save, or half as much damage on a successful one."
        if Dice(d) == 9 and not ("Cold Breath" in recharge):         recharge += f"\n  - Cold Breath \n\t(Recharge 5-6) The dragon exhales an icy blast in a 15-foot cone. Each creature in that area must make a DC {10+PB(Lvl)} Constitution saving throw, taking 18 (4d8) cold damage on a failed save, or half as much damage on a successful one."
        elif Dice(d) == 10 and not ("Cold Breath" in recharge):      recharge += f"\n  - Cold Breath \n\t(Recharge 5-6) The dragon exhales an icy blast in a 15-foot cone. Each creature in that area must make a DC {10+PB(Lvl)} Constitution saving throw, taking 22 (5d8) cold damage on a failed save, or half as much damage on a successful one."
        if Dice(d) == 11 and not ("Paralyzing Breath" in recharge):  recharge += f"\n  - Paralyzing Breath \n\t(Recharge 5-6) The dragon exhales paralyzing gas in a 15-foot cone. Each creature in that area must succeed on a {10+PB(Lvl)} Constitution saving throw or be paralyzed for 1 minute. A creature can repeat the saving throw at the start of each of its turns, ending the effect on itself on a success."
        if Dice(d) == 12 and not ("WeakeningBreath" in recharge):    recharge += f"\n  - Weakening Breath \n\t(Recharge 5-6) The dragon exhales gas in a 15-foot cone. Each creature in that area must succeed on a DC {10+PB(Lvl)} Strength saving throw or have disadvantage on Strength-based attack rolls, Strength checks, and Strength saving throws for 1 minute. A creature can repeat the saving throw at the start of each of its turns, ending the effect on itself on a success."

    if race == "Dragon" and Dice(12) == 1 and not ("Change Shape" in recharge):  recharge += "\n- Change Shape \n\t The dragon magically polymorphs into a humanoid or beast that has a challenge rating no higher than its own, or back into its true form. It reverts to its true form if it dies. Any equipment it is wearing or carrying is absorbed or borne by the new form (the dragon's choice).In a new form, the dragon retains its alignment, hit points, Hit Dice, ability to speak, proficiencies, Legendary Resistance, lair actions, and Intelligence, Wisdom, and Charisma scores, as well as this action. Its statistics and capabilities are otherwise replaced by those of the new form, except any class features or legendary actions of that form."

    if race == "Dragon":
        
        difficulty += Dice(6) - Dice(10)
        max_spell_level = get_max_spell_level(Lvl, difficulty)
        cantrips_list += ["Control Flames", "Gust", "Mage Hand", "Minor Illusion", "Dancing Lights", "Color Spray" ]
        one_day_each_list += ["Charm Person", "Fear", "Shield"]
        two_day_each_list += ["Flame Strike", "Fly", "Invisibility"]
        three_day_each_list += ["Fireball", "Protection from Energy", "Wind Walk"]
        first_list += ["Charm Person", "Detect Magic", "Mage Armor", "Magic Missile", "Shield", "Suggestion", "Polymorph", "Mirror Image", "Major Image"]

        # 2nd Level Spells
        second_list = [
            "Darkness", "Flaming Sphere", "Hold Person", "Invisibility", "Mirror Image"]
        for s in second_list:
            second, slots2 = add_spell(second, s, 2, slots2, max_spell_level)

        third_list += ["Fear", "Fireball", "Fly", "Haste", "Protection from Energy"]

        # 4th Level Spells
        fourth_list += ["Charm Monster", "Control Flames", "Greater Invisibility", "Wall of Fire", "Stone Shape"]

        # 5th Level Spells
        fifth_list = ["Dominate Person", "Flame Strike", "Geas", "Hold Monster", "Teleportation Circle"]
        for s in fifth_list:
            fifth, slots5 = add_spell(fifth, s, 5, slots5, max_spell_level)

        # 6th Level Spells
        sixth_list = ["Chain Lightning",
                      "Disintegrate",
                      "Move Earth",
                      "True Seeing",
                      "Sunburst"]
        for s in sixth_list:
            sixth, slots6 = add_spell(sixth, s, 6, slots6, max_spell_level)

        # 7th Level Spells
        seventh_list = [
            "Fire Storm",
            "Plane Shift", "Reverse Gravity", "Teleport", "Prismatic Spray"]
        for s in seventh_list:
            seventh, slots7 = add_spell(seventh, s, 7, slots7, max_spell_level)

        # 8th Level Spells
        eighth_list = [
            "Control Weather", "Earthquake", "Incendiary Cloud", "Telepathy", "Sunburst"]
        for s in eighth_list:
            eighth, slots8 = add_spell(eighth, s, 8, slots8, max_spell_level)

        # 9th Level Spells
        ninth_list = ["Gate",
                      "Imprisonment",
                      "Meteor Swarm",
                      "Power Word Kill",
                      "Time Stop"]
        for s in ninth_list:
            ninth, slots9 = add_spell(ninth, s, 9, slots9, max_spell_level)

    # DWARF.

    if race == "Dwarf":
        difficulty += Dice(6) - Dice(4)
        max_spell_level = get_max_spell_level(Lvl, difficulty)

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
        difficulty += Dice(6) - Dice(10)
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
        cantrips_list += ["Control Flames", "Gust", "Mold Earth", "Shape Water", "Dancing lights"]

        recharge, _ = add_spell(recharge, "Whirlwind", 0, 0, max_spell_level,
                                f" (Recharge 4–6)."+
                                f"\t Each creature in the {race}'s space must make a Strength saving throw. " +
                                f"On a failure, a target takes 15 (3d8 + 2) bludgeoning damage and is flung up 20 feet away from the {race} in a random direction and knocked prone. " +
                                f"If a thrown target strikes an object, such as a wall or floor, the target takes 3 (1d6) bludgeoning damage for every 10 feet it was thrown. "  +
                                f"If the target is thrown at another creature, that creature must succeed on a Dexterity Saving Throw or take the same damage and be knocked prone. " +
                                f"/n/t If the saving throw is successful, the target takes half the bludgeoning damage and isn't flung away or knocked prone. ")

        recharge, _ = add_spell(recharge, "Cinder breath", 0, 0, max_spell_level,
                                f"\t (Recharge 6). The Elemental exhales a 15-foot cone of smoldering ash. Each creature in that area must succeed on a DC [10+%Cha] Dexterity saving throw or be blinded until the end of the Elemental's next turn.")

        recharge, _ = add_spell(recharge, "Blinding breath", 0, 0, max_spell_level,
                               f"\t (Recharge 6). The Elemental exhales a 15-foot cone of blinding dust. Each creature in that area must succeed on a Dexterity saving throw or be blinded for one minute.")

        recharge, _ = add_spell(recharge, "Steam breath", 0, 0, max_spell_level,
                                f"\t (Recharge 6). The Elemental exhales a 15-foot cone of scalding steam. Each creature in that area must succeed on a Dexterity saving throw, taking 4 (1d8) fire damage on a failed save, or half as much damage on a successful one.")

        recharge, _ = add_spell(recharge, "Frost Breath", 0, 0, max_spell_level,
                                f"\t (Recharge 6). The Elemental exhales a 15-foot cone of cold air. Each creature in that area must succeed on a Dexterity saving throw, taking 5 (2d4) cold damage on a failed save, or half as much damage on a successful one.")

        recharge, _ = add_spell(recharge, "Fire Breath", 0, 0, max_spell_level,
                               "\t (Recharge 6). The Elemental exhales a 15-foot cone of cold air. Each creature in that area must succeed on a Dexterity saving throw, taking 7 (2d6) fire damage on a failed save, or half as much damage on a successful one.")

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

        recharge, _ = add_spell(recharge, "Summon Mephits", max_spell_level-3, 0, max_spell_level,
                                  "(recharge 6):\t The Elemental has a 25 percent chance of summoning 1d4 mephits. A summoned mephit appears in an unoccupied space within 60 feet of its summoner, acts as an ally of its summoner, and can't summon other mephits. It remains for 1 minute, until it or its summoner dies, or until its summoner dismisses it as an action.")
        one, _ = add_spell(one, "Innate Spellcasting", max_spell_level-3, 0, max_spell_level,
                           "The Elemental can innately cast fog cloud, requiring no material components")

        one, _ = add_spell(one, "Innate Spellcasting", max_spell_level-3, 0, max_spell_level,
                 "\tThe Elemental can innately cast heat metal, requiring no material components.")

        one, _ = add_spell(one, "Blur", max_spell_level-3,0, max_spell_level,)
        one, _ = add_spell(one, "Sleep", max_spell_level-3, 0, max_spell_level,)

    # ELF.
    if race == "Elf":
        difficulty += Dice(6) - Dice(4)
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        cantrips_list += ["Dancing Lights", "Druidcraft", "Mage Hand", "Minor Illusion"]
        one_day_each_list += ["Charm Person", "Disguise Self", "Sleep", "Darkness", "Faerie Fire", "Levitate"]
        two_day_each_list += [
            "Detect Thoughts",
            "Invisibility",
            "Mirror Image"]
        three_day_each_list += [
            "Counterspell",
            "Feather Fall",
            "Protection from Energy"]
        first_list += ["Charm Person", "Detect Magic", "Fog Cloud", "Goodberry", "Healing Word"]
        second_list += ["Barkskin", "Darkvision", "Enhance Ability", "Pass without Trace", "Silence"]
        third_list += ["Dispel Magic", "Protection from Energy", "Remove Curse", "Speak with Dead", "Water Breathing"]
        fourth_list += ["Dimension Door", "Freedom of Movement", "Greater Invisibility", "Hallucinatory Terrain", "Locate Creature"]
        fifth_list += ["Awaken", "Commune with Nature", "Mislead", "Modify Memory", "Teleportation Circle"]
        sixth_list += ["Find the Path", "Heal", "Heroes' Feast", "Transport via Plants", "True Seeing"]
        seventh_list += ["Etherealness", "Mirage Arcane", "Plane Shift", "Regenerate", "Teleport"]
        eighth_list += ["Antipathy/Sympathy", "Earthquake", "Incendiary Cloud", "Mind Blank", "Power Word Stun"]
        ninth_list += ["Foresight", "Mass Heal", "Power Word Heal", "Shapechange", "Time Stop"]

    # FAE.
    if race == "Fey" and Dice(8) == 1 and not ("Ethereal Jaunt" in recharge):    recharge += "\n- Ethereal Jaunt (Recharge 6):\n\t As a bonus action, the fey can magically shift from the Material Plane to the Ethereal Plane, or vice versa."
    if race == "Fey" and Dice(10) == 1 and not ("Teleport" in recharge):         recharge += "\n- Teleport (Recharge 4–6). \n\t The Fey magically teleports, along with any equipment it is wearing or carrying, up to 40 feet to an unoccupied space it can see. Before or after teleporting, the Fey can make one bite attack."
    if race == "Fey" and Dice(10) == 1 and not ("Heart Sight" in recharge):      recharge += "\n- Heart Sight. (Recharge 6)\n\t The Fey touches a creature and magically knows the creature's current emotional state. If the target fails a DC [10+%Cha] Charisma saving throw, the Fey also knows the creature's alignment. Celestials, fiends, and undead automatically fail the saving throw."
    if race == "Fey" and Dice(10) == 1 and not ("Invisibility" in recharge):     recharge += "\n- Invisibility. (Recharge 6)\n\t The Fey  magically turns invisible until it attacks or casts a spell, or until its concentration ends (as if concentrating on a spell). Any equipment the Fey wears or carries is invisible with it."
    if race == "Fey" and Dice(8) == 1 and not ("Change Shape" in recharge):      recharge += "\n- Change Shape. (Recharge 6)\n\t The fey magically polymorphs into a Small or Medium humanoid, or back into their true form. Their statistics are the same in each form. Any equipment they are wearing or carrying isn't transformed. They reverts to their true form if they dies."
    if race == "Fey" and Dice() == 1 and not ("Etherealness" in recharge):       recharge += "\n- Etherealness. (Recharge 6)\n\t The fey magically enters the Ethereal Plane from the Material Plane, or vice versa. To do so, the fey must have a heartstone in her possession."



    if race == "Fey" and Dice(8) == 1 and not ("Charming Melody" in one):       one += "\n- Charming Melody [DC 10+%Cha Wisdom saving throw]\n\t The creature is charmed by the Fey for 1 minute. If the Fey or any of its companions harms the creature, the effect on it ends immediately."
    if race == "Fey" and Dice(8) == 1 and not ("Frightening Strain" in one):    one += "\n- Frightening Strain [DC 10+%Cha Wisdom saving throw] \n\t The creature is charmed by the Fey for 1 minute. If the Fey or any of its companions harms the creature, the effect on it ends immediately."
    if race == "Fey" and Dice(8) == 1 and not ("Gentle Lullaby" in one):        one += "\n- Gentle Lullaby [DC 10+%Cha Wisdom saving throw] \n\t The creature falls asleep and is unconscious for 1 minute. The effect ends if the creature takes damage or if someone takes an action to shake the creature awake."
    if race == "Fey" and Dice(8) == 1 and not ("Nightmare Haunting" in one):    one += "\n- Nightmare Haunting \n\t While on the Ethereal Plane, the fey magically touches a sleeping humanoid on the Material Plane. A protection from evil and good spell cast on the target prevents this contact, as does a magic circle. As long as the contact persists, the target has dreadful visions. If these visions last for at least 1 hour, the target gains no benefit from its rest, and its hit point maximum is reduced by 5 (1d10). If this effect reduces the target's hit point maximum to 0, the target dies, and if the target was evil, its soul is trapped in the fey's soul bag. The reduction to the target's hit point maximum lasts until removed by the greater restoration spell or similar magic."

        
    if race == "Fey":
        difficulty += Dice(6) - Dice(12)
        max_spell_level = get_max_spell_level(Lvl, difficulty)

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

    if race == "Fiend":
        difficulty += Dice(6) - Dice(8)
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        if Dice()==1 and not ("Charm" in cantrip):
            if Dice(2)==1:  cantrip += "\n- Charm \n\t One humanoid the fiend can see within 30 feet of it must succeed on a DC [10+%CHA] Wisdom saving throw or be magically charmed for 1 day. The charmed target obeys the fiend's verbal or telepathic commands. If the target suffers any harm or receives a suicidal command, it can repeat the saving throw, ending the effect on a success. If the target successfully saves against the effect, or if the effect on it ends, the target is immune to this fiend's Charm for the next 24 hours. \n\t The fiend can have only one target charmed at a time. If it charms another, the effect on the previous target ends. "
            else:           cantrip += "\n- Fiendish Charm. \n\t One humanoid the fiend can see within 30 feet of it must succeed on a DC [11+%CHA] Wisdom saving throw or be magically charmed for 1 day. The charmed target obeys the fiend's spoken commands. If the target suffers any harm from the fiend or another creature or receives a suicidal command from the fiend, the target can repeat the saving throw, ending the effect on itself on a success. If a target's saving throw is successful, or if the effect ends for it, the creature is immune to the fiend's Fiendish Charm for the next 24 hours."
            if Dice()==1 and not ("Draining Kiss" in cantrip):      cantrip += "\n- Draining Kiss \t The fiend kisses a creature charmed by it or a willing creature. The target must make a DC 15 Constitution saving throw against this magic, taking 32 (5d10 + 5) psychic damage on a failed save, or half as much damage on a successful one. The target's hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0. "
            if Dice()==1 and not ("Telepathic Bond" in cantrip):    cantrip += "\n- Telepathic Bond. \t The fiend ignores the range restriction on its telepathy when communicating with a creature it has charmed. The two don't even need to be on the same plane of existence."

        if Dice() == 1 and not ("Etherealness" in cantrip):         cantrip += "\n- Etherealness.\t The fiend magically enters the Ethereal Plane from the Material Plane, or vice versa."
        if Dice() == 1 and not ("Fire Breath" in cantrip):          cantrip += "\n- Fire Breath (Recharge 5-6).\t The fiend exhales fire in a 15-foot cone. Each creature in that area must make a DC [10+%CON] Dexterity saving throw, taking 21 (6d6) fire damage on a failed save, or half as much damage on a successful one."
        if Dice() == 1 and not ("Fire Ray" in cantrip):             cantrip += "\n- Fire Ray \t Ranged Spell Attack. Range 120ft. One target. Hit: 10(3d6) fire damage."

    # Once a day
    if race == "Fiend":
        if Dice() == 1 and not ("Scare" in one):            one += "\n- Scare \n\t One creature of the Fiend's choice within 20 feet of it must succeed on a DC 10 Wisdom saving throw or be frightened for 1 minute. The target can repeat the saving throw at the begguining of each of its turns, with disadvantage if the Fiend is within line of sight, ending the effect on itself on a success."
        if Dice() == 1 and not ("Fetid Cloud" in one):      one += "\n- Fetid Cloud.\n\t A 10-foot radius of disgusting sulfuric gas extends out from the Fiend. The gas spreads around corners, and its area is lightly obscured. It lasts for 1 minute or until a strong wind disperses it. Any creature that starts its turn in that area must succeed on a DC 11 Constitution saving throw or be poisoned until the start of its next turn. While poisoned in this way, the target can take either an action or a bonus action on its turn, not both, and can't take reactions."
        if Dice() == 1 and not ("Summon Yugoloth" in one):  one += "\n- Summon Yugoloth. \n\t The fiend attempts a magical summoning. \n\t A fiend has a 30 percent chance of summoning one mezzoloth. \n\t A summoned yugoloth appears in an unoccupied space within 60 feet of its summoner, does as it pleases, and can't summon other yugoloths. The summoned yugoloth remains for 1 minute, until it or its summoner dies, or until its summoner takes a bonus action to dismiss it."
            
        
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

        difficulty += Dice(12) - Dice(12)
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
        cantrips_list += [
            "Gust",
            "Mold Earth",
            "Thunderclap",
            "Magic Stone"]

        one_day_each_list += [
            "Enlarge/Reduce", "Earth Tremor", "Thunderwave"]

        # 2/Day each
        two_day_each_list = ["Gust of Wind", "Spike Growth", "Warding Wind"]
        for s in two_day_each_list:
            two, _ = add_spell(two, s, max_spell_level-2, 0, max_spell_level, spell_definition="2/Day each")

        # 3/Day each
        three_day_each_list = ["Erupting Earth", "Meld into Stone", "Wind Wall"]
        for s in three_day_each_list:
            three, _ = add_spell(three, s, max_spell_level-3, 0, max_spell_level, spell_definition="3/Day each")

        # 1st Level Spells
        first_list = [
            "Earth Tremor", "Entangle", "Longstrider", "Shield of Faith", "Thunderwave"]
        for s in first_list:
            first, slots1 = add_spell(first, s, 1, slots1, max_spell_level)

        # 2nd Level Spells
        second_list = ["Enlarge/Reduce", "Gust of Wind", "Spike Growth", "Stone Fist", "Warding Wind"]
        for s in second_list:
            second, slots2 = add_spell(second, s, 2, slots2, max_spell_level)

        # 3rd Level Spells
        third_list = ["Erupting Earth", "Meld into Stone", "Sleet Storm", "Stoneskin", "Wind Wall"]
        for s in third_list:
            third, slots3 = add_spell(third, s, 3, slots3, max_spell_level)

        # 4th Level Spells
        fourth_list = ["Control Water", "Stone Shape", "Storm Sphere", "Wall of Fire", "Watery Sphere"]
        for s in fourth_list:
            fourth, slots4 = add_spell(fourth, s, 4, slots4, max_spell_level)

        # 5th Level Spells
        fifth_list = ["Control Winds", "Transmute Rock", "Wall of Stone", "Cloudkill", "Insect Plague"]
        for s in fifth_list:
            fifth, slots5 = add_spell(fifth, s, 5, slots5, max_spell_level)

        sixth_list += ["Bones of the Earth", "Move Earth", "Sunburst", "Wind Walk", "Investiture of Stone"]
        seventh_list += ["Whirlwind", "Reverse Gravity", "Fire Storm", "Regenerate", "Sequester"]
        eighth_list += ["Control Weather",
                       "Earthquake",
                       "Incendiary Cloud",
                       "Abi-Dalzim’s Horrid Wilting",
                       "Telepathy"]

        # 9th Level Spells
        ninth_list = [
            "Meteor Swarm", "Storm of Vengeance", "Tsunami", "Weird", "Imprisonment"]
        for s in ninth_list:
            ninth, slots9 = add_spell(ninth, s, 9, slots9, max_spell_level)

    # GNOME.
    if race == "Gnome":
        
        difficulty += Dice(6) - Dice(4)
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
        cantrips_list = [
            "Prestidigitation",
            "Minor Illusion",
            "Mage Hand", "Dancing Lights"]
        for c in cantrips_list:
            cantrip, _ = add_spell(cantrip, c, 0, 0, max_spell_level)

        one_day_each_list = ["Disguise Self",
                             "Expeditious Retreat",
                             "Silent Image",
                             "Nondetection"]

        # 2/Day each
        two_day_each_list = ["Blur", "Invisibility", "Nystul’s Magic Aura", "Blindness/Deafness"]
        for s in two_day_each_list:
            two, _ = add_spell(two, s, max_spell_level-2, 0, max_spell_level, spell_definition="2/Day each")

        # 3/Day each
        three_day_each_list = ["Blink", "Major Image", "Phantom Steed"]
        for s in three_day_each_list:
            three, _ = add_spell(three, s, max_spell_level-3, 0, max_spell_level, spell_definition="3/Day each")

        # 1st Level Spells
        first_list = ["Illusory Script", "Color Spray", "Charm Person", "Tasha’s Hideous Laughter", "Detect Magic"]
        for s in first_list:
            first, slots1 = add_spell(first, s, 1, slots1, max_spell_level)

        # 2nd Level Spells
        second_list = ["Invisibility", "Mirror Image", "Suggestion", "Arcane Lock", "Pyrotechnics"]
        for s in second_list:
            second, slots2 = add_spell(second, s, 2, slots2, max_spell_level)

        # 3rd Level Spells
        third_list = ["Major Image", "Dispel Magic", "Nondetection", "Hypnotic Pattern", "Leomund’s Tiny Hut"]
        for s in third_list:
            third, slots3 = add_spell(third, s, 3, slots3, max_spell_level)

        # 4th Level Spells
        fourth_list = ["Dimension Door", "Greater Invisibility", "Polymorph", "Stone Shape", "Confusion"]
        for s in fourth_list:
            fourth, slots4 = add_spell(fourth, s, 4, slots4, max_spell_level)

        # 5th Level Spells
        fifth_list = ["Animate Objects", "Mislead", "Seeming", "Teleportation Circle", "Rary’s Telepathic Bond"]
        for s in fifth_list:
            fifth, slots5 = add_spell(fifth, s, 5, slots5, max_spell_level)

        # 6th Level Spells
        sixth_list = ["Programmed Illusion", "True Seeing", "Mass Suggestion", "Eyebite", "Magic Jar"]
        for s in sixth_list:
            sixth, slots6 = add_spell(sixth, s, 6, slots6, max_spell_level)

        # 7th Level Spells
        seventh_list = ["Mirage Arcane", "Simulacrum", "Project Image", "Teleport", "Sequester"]
        for s in seventh_list:
            seventh, slots7 = add_spell(seventh, s, 7, slots7, max_spell_level)

        # 8th Level Spells
        eighth_list += ["Incendiary Cloud", "Dominate Monster", "Maze", "Mind Blank", "Power Word Stun"]
    

        # 9th Level Spells
        ninth_list = ["Time Stop", "True Polymorph", "Weird", "Power Word Heal", "Power Word Kill"]
        for s in ninth_list:
            ninth, slots9 = add_spell(ninth, s, 9, slots9, max_spell_level)

    # GOBLIN.
    if race == "Goblin" and Dice() == 1 and not ("Leadership" in cantrip):           cantrip += " \n- Leadership (Recharges after a Short or Long Rest). \n\t For 1 minute, the goblin can utter a special command or warning whenever a nonhostile creature that it can see within 30 feet of it makes an attack roll or a saving throw. The creature can add a d4 to its roll provided it can hear and understand the goblin. A creature can benefit from only one Leadership die at a time. This effect ends if the goblin is incapacitated."
    if race == "Goblin":
        
        difficulty += Dice(10) - Dice(10)
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
        cantrips_list = ["Minor Illusion", "Prestidigitation", "Mage Hand", "Vicious Mockery"]
        for c in cantrips_list:
            cantrip, _ = add_spell(cantrip, c, 0, 0, max_spell_level)

        one_day_each_list += ["Disguise Self", "Tasha's Hideous Laughter", "Bane"]

        # 2/Day each
        two_day_each_list = ["Darkness", "Misty Step", "Silent Image"]
        for s in two_day_each_list:
            two, _ = add_spell(two, s, max_spell_level-2, 0, max_spell_level, spell_definition="2/Day each")

        # 3/Day each
        three_day_each_list = ["Fear", "Hypnotic Pattern", "Major Image"]
        for s in three_day_each_list:
            three, _ = add_spell(three, s, max_spell_level-3, 0, max_spell_level, spell_definition="3/Day each")

        # 1st Level Spells
        first_list = ["Charm Person", "Sleep", "Dissonant Whispers", "Hideous Laughter", "Faerie Fire"]
        for s in first_list:
            first, slots1 = add_spell(first, s, 1, slots1, max_spell_level)

        # 2nd Level Spells
        second_list = ["Invisibility", "Silence", "Suggestion", "Mirror Image", "Phantasmal Force"]
        for s in second_list:
            second, slots2 = add_spell(second, s, 2, slots2, max_spell_level)

        # 3rd Level Spells
        third_list = ["Fear", "Major Image", "Bestow Curse", "Enemies Abound", "Blink"]
        for s in third_list:
            third, slots3 = add_spell(third, s, 3, slots3, max_spell_level)

        # 4th Level Spells
        fourth_list = [
            "Confusion", "Greater Invisibility", "Polymorph", "Shadow of Moil", "Dimension Door"]
        for s in fourth_list:
            fourth, slots4 = add_spell(fourth, s, 4, slots4, max_spell_level)

        # 5th Level Spells
        fifth_list = [
            "Mislead", "Animate Objects", "Dominate Person", "Geas", "Seeming"]
        for s in fifth_list:
            fifth, slots5 = add_spell(fifth, s, 5, slots5, max_spell_level)

        # 6th Level Spells
        sixth_list = ["Mass Suggestion", "Programmed Illusion", "True Seeing", "Eyebite", "Circle of Death"]
        for s in sixth_list:
            sixth, slots6 = add_spell(sixth, s, 6, slots6, max_spell_level)

        # 7th Level Spells
        seventh_list = ["Mirage Arcane", "Project Image", "Prismatic Spray", "Simulacrum", "Etherealness"]
        for s in seventh_list:
            seventh, slots7 = add_spell(seventh, s, 7, slots7, max_spell_level)

        # 8th Level Spells
        eighth_list = ["Dominate Monster", "Power Word Stun", "Antipathy/Sympathy", "Demiplane", "Feeblemind"]
        for s in eighth_list:
            eighth, slots8 = add_spell(eighth, s, 8, slots8, max_spell_level)

        # 9th Level Spells
        ninth_list = ["Power Word Kill", "Weird", "True Polymorph", "Foresight", "Meteor Swarm"]
        for s in ninth_list:
            ninth, slots9 = add_spell(ninth, s, 9, slots9, max_spell_level)
            
    if race == "Goblin":

        # Cantrips
        cantrips_list = ["Minor Illusion", "Mage Hand", "Message", "Poison Spray"]
        for c in cantrips_list:
            cantrip, _ = add_spell(cantrip, c, 0, 0, max_spell_level)

        one_day_each_list += ["Disguise Self", "Expeditious Retreat", "Jump"]

        # 2/Day each
        two_day_each_list = ["Grease", "Fog Cloud", "Hideous Laughter"]
        for s in two_day_each_list:
            two, _ = add_spell(two, s, max_spell_level-2, 0, max_spell_level, spell_definition="2/Day each")

        # 3/Day each
        three_day_each_list = [
            "Blur", "Silence", "Darkness"]
        for s in three_day_each_list:
            three, _ = add_spell(three, s, max_spell_level-3, 0, max_spell_level, spell_definition="3/Day each")

        # 1st Level Spells
        first_list = ["Sleep", "Dissonant Whispers", "Snare", "Entangle", "Charm Person"]
        for s in first_list:
            first, slots1 = add_spell(first, s, 1, slots1, max_spell_level)

        # 2nd Level Spells
        second_list = ["Invisibility", "Pass without Trace", "Suggestion", "Mirror Image", "Web"]
        for s in second_list:
            second, slots2 = add_spell(second, s, 2, slots2, max_spell_level)

        # 3rd Level Spells
        third_list += [
            "Gaseous Form", "Fear", "Stinking Cloud", "Hypnotic Pattern", "Bestow Curse"]

        # 4th Level Spells
        fourth_list = ["Confusion", "Greater Invisibility", "Polymorph", "Dimension Door", "Hallucinatory Terrain"]
        for s in fourth_list:
            fourth, slots4 = add_spell(fourth, s, 4, slots4, max_spell_level)

        # 5th Level Spells
        fifth_list += ["Mislead", "Animate Objects", "Dominate Person", "Geas", "Cloudkill"]

        # 6th Level Spells
        sixth_list = ["Programmed Illusion", "Eyebite", "Mass Suggestion", "Circle of Death", "True Seeing"]
        for s in sixth_list:
            sixth, slots6 = add_spell(sixth, s, 6, slots6, max_spell_level)

        # 7th Level Spells
        seventh_list = ["Mirage Arcane", "Prismatic Spray", "Project Image", "Etherealness", "Teleport"]
        for s in seventh_list:
            seventh, slots7 = add_spell(seventh, s, 7, slots7, max_spell_level)

        # 8th Level Spells
        eighth_list = ["Dominate Monster",
                       "Power Word Stun",
                       "Incendiary Cloud",
                       "Demiplane",
                       "Maze"]
        for s in eighth_list:
            eighth, slots8 = add_spell(eighth, s, 8, slots8, max_spell_level)

        # 9th Level Spells
        ninth_list = ["Power Word Kill", "Weird", "Time Stop", "Foresight", "Meteor Swarm"]
        for s in ninth_list:
            ninth, slots9 = add_spell(ninth, s, 9, slots9, max_spell_level)

    # HALFLING. 
    if race == "Halfling":
        difficulty += Dice(4) - Dice(4)
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
        cantrips_list = ["Minor Illusion", "Prestidigitation", "Mage Hand", "Guidance"]
        for c in cantrips_list:
            cantrip, _ = add_spell(cantrip, c, 0, 0, max_spell_level)

        one_day_each_list += ["Cure Wounds", "Bless", "Jump"]

        # 2/Day each
        two_day_each_list = [
            "Invisibility", "Calm Emotions", "Protection from Poison"]
        for s in two_day_each_list:
            two, _ = add_spell(two, s, max_spell_level-2, 0, max_spell_level, spell_definition="2/Day each")

        # 3/Day each
        three_day_each_list += [
            "Heroism",
            "Haste", "Protection from Energy"]

        # 1st Level Spells
        first_list = ["Cure Wounds", "Disguise Self", "Feather Fall", "Hideous Laughter", "Charm Person"]
        for s in first_list:
            first, slots1 = add_spell(first, s, 1, slots1, max_spell_level)

        # 2nd Level Spells
        second_list = ["Alter Self", "Invisibility", "Knock", "Mirror Image", "Pass without Trace"]
        for s in second_list:
            second, slots2 = add_spell(second, s, 2, slots2, max_spell_level)

        # 3rd Level Spells
        third_list += ["Blink", "Fly", "Haste", "Protection from Energy", "Water Walk"]

        # 4th Level Spells
        fourth_list = ["Greater Invisibility", "Polymorph", "Dimension Door", "Freedom of Movement", "Stone Shape"]
        for s in fourth_list:
            fourth, slots4 = add_spell(fourth, s, 4, slots4, max_spell_level)

        # 5th Level Spells
        fifth_list = ["Mislead", "Modify Memory", "Passwall", "Teleportation Circle", "Greater Restoration"]
        for s in fifth_list:
            fifth, slots5 = add_spell(fifth, s, 5, slots5, max_spell_level)

        # 6th Level Spells
        sixth_list = ["Find the Path", "Guards and Wards", "Move Earth", "True Seeing", "Word of Recall"]
        for s in sixth_list:
            sixth, slots6 = add_spell(sixth, s, 6, slots6, max_spell_level)

        # 7th Level Spells
        seventh_list = ["Etherealness", "Plane Shift", "Regenerate", "Teleport", "Resurrection"]
        for s in seventh_list:
            seventh, slots7 = add_spell(seventh, s, 7, slots7, max_spell_level)

        # 8th Level Spells
        eighth_list = ["Antimagic Field", "Control Weather", "Earthquake", "Holy Aura", "Telepathy"]
        for s in eighth_list:
            eighth, slots8 = add_spell(eighth, s, 8, slots8, max_spell_level)

        ninth_list += ["Foresight", "Imprisonment", "Meteor Swarm", "Time Stop", "True Resurrection"]


    # HUMAN. 
    if race == "Human":
        difficulty += Dice(6) - Dice(6)
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        # Cantrips
        cantrips_list = [
            "Prestidigitation",
            "Thaumaturgy",
            "Light",
            "Mending"]
        for c in cantrips_list:
            cantrip, _ = add_spell(cantrip, c, 0, 0, max_spell_level)

        one_day_each_list += ["Longstrider", "Charm Person", "Goodberry"]

        # 2/Day each
        two_day_each_list = ["Enhance Ability", "Aid", "Calm Emotions"]
        for s in two_day_each_list:
            two, _ = add_spell(two, s, max_spell_level-2, 0, max_spell_level, spell_definition="2/Day each")

        # 3/Day each
        three_day_each_list = ["Create Food and Water", "Sending", "Dispel Magic"]
        for s in three_day_each_list:
            three, _ = add_spell(three, s, max_spell_level-3, 0, max_spell_level, spell_definition="3/Day each")

        first_list += ["Alarm",
                      "Comprehend Languages",
                      "Cure Wounds",
                      "Detect Magic",
                      "Shield"]

        # 2nd Level Spells
        second_list = ["Detect Thoughts", "Locate Object", "Magic Weapon", "See Invisibility", "Zone of Truth"]
        for s in second_list:
            second, slots2 = add_spell(second, s, 2, slots2, max_spell_level)

        # 3rd Level Spells
        third_list = ["Clairvoyance", "Counterspell", "Dispel Magic", "Speak with Dead", "Water Walk"]
        for s in third_list:
            third, slots3 = add_spell(third, s, 3, slots3, max_spell_level)

        # 4th Level Spells
        fourth_list = ["Arcane Eye", "Dimension Door", "Greater Invisibility", "Locate Creature", "Stoneskin"]
        for s in fourth_list:
            fourth, slots4 = add_spell(fourth, s, 4, slots4, max_spell_level)

        # 5th Level Spells
        fifth_list += ["Animate Objects", "Contact Other Plane", "Legend Lore", "Mass Cure Wounds", "Teleportation Circle"]
        sixth_list += ["Contingency", "Find the Path", "Guards and Wards", "Mass Suggestion", "True Seeing"]
        seventh_list += ["Etherealness", "Mirage Arcane", "Plane Shift", "Regenerate", "Teleport"]
        eighth_list += ["Antimagic Field", "Control Weather", "Demiplane", "Dominate Monster", "Telepathy"]
        ninth_list += [ "Foresight", "Gate", "Imprisonment", "Mass Heal", "Time Stop"]



    # KOBOLDS.
    if race == "Kobold":
        difficulty += Dice(12) - Dice(12)
        max_spell_level = get_max_spell_level(Lvl, difficulty)

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
        difficulty += Dice(6) - Dice(6)
        max_spell_level = get_max_spell_level(Lvl, difficulty)

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
        difficulty += Dice(6) - Dice(12)
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        if Dice(8) == 1 and not ("Acid Spray" in recharge):
            recharge += f"\n- Acid Spray (Recharge 6): \n\t The {race} spits acid in a line that is 30 feet long and 5 feet wide, provided that it has no creature grappled." +\
                        f"Each creature in that line must make a Dexterity saving throw, "+\
                        "taking {3*npc.proficiency_bonus} ({npc.proficiency_bonus}d6) acid damage on a failed save, or half as much damage on a successful one."
        if Dice(10) == 1 and not ("Confusing Gaze" in recharge):
            recharge += f"\n- Confusing Gaze (Recharge 6): \n\t When a creature starts its turn within 30 feet of the monstrosity and is able to see the {race}'s eyes, "+\
                        f"the {race} can magically force it to make a Charisma saving throw, unless the {race} is incapacitated. "+ \
                        f"\n\t On a failed saving throw, the creature can't take reactions until the start of its next turn and rolls a d8 to determine what it does during"+\
                        f"that turn. On a 1 to 4, the creature does nothing. On a 5 or 6, the creature takes no action but uses all its movement to move in a random direction."+\
                        f"On a 7 or 8, the creature makes one melee attack against a random creature, or it does nothing if no creature is within reach. "+\
                        "\n\t Unless surprised, a creature can avert its eyes to avoid the saving throw at the start of its turn. If the creature does so, "+\
                        f"it can't see the {race} until the start of its next turn, when it can avert its eyes again. If the creature looks at the {race} in the meantime, "+\
                        "it must immediately make the save." 
        if Dice() == 1 and not ("Chilling Gaze" in recharge):
            recharge += f"\n - Chilling Gaze (Recharge 6): \n\t The monstrosity targets one creature it can see within 30 feet of it. If the target can see the monstrosity, the target must succeed on a DC [10+%CON] Constitution saving throw against this magic or take 10 (3d6) cold damage and then be paralyzed for 1 minute, unless it is immune to cold damage. The target can repeat the saving throw at the start of each of its turns, ending the effect on itself on a success. If the target's saving throw is successful, or if the effect ends on it, the target is immune to the Chilling Gaze of all monstrosities for 1 hour."
        if Dice() == 1 and not ("Disguise Self" in recharge):
            recharge += "\n - Disguise self (humanoid form) Aura (Recharge 6): \n\t A 15-foot radius of magical darkness extends out from the Monstrosity, moves with it, and spreads around corners. The darkness lasts as long as the Monstrosity maintains concentration, up to 10 minutes (as if concentrating on a spell). Darkvision can't penetrate this darkness, and no natural light can illuminate it. If any of the darkness overlaps with an area of light created by a spell of 2nd level or lower, the spell creating the light is dispelled."
        if Dice(8) == 1 and not ("Fire Breath" in recharge):
            recharge += "\n -  Fire Breath (Recharge 5–6). \n\t The monstrosity exhales fire in a 15-foot cone. Each creature in that area must make a DC[11+%CON] Dexterity saving throw, taking 31 (7d8) fire damage on a failed save, or half as much damage on a successful one."
                
        if Dice(8) == 1 and not ("Luring Song" in recharge):
            recharge += "\n - Luring Song: \n\t The {race} sings a magical melody. Every humanoid and giant within 300 feet of the monstrosity that can hear the song must succeed on a DC [10+%Cha] Wisdom saving throw or be charmed until the song ends. The monstrosity must take a bonus action on its subsequent turns to continue singing. It can stop singing at any time. The song ends if the monstrosity is incapacitated. While charmed by the monstrosity, a target is incapacitated and ignores the songs of other monstrosities. If the charmed target is more than 5 feet away from the monstrosity, the target must move on its turn toward the monstrosity by the most direct route. It doesn't avoid opportunity attacks, but before moving into damaging terrain, such as lava or a pit, and whenever it takes damage from a source other than the monstrosity, a target can repeat the saving throw. A creature can also repeat the saving throw at the begguining of each of its turns. If a creature's saving throw is successful, the effect ends on it. A target that successfully saves is immune to this monstrosity's song for the next 24 hours."

        if Dice(10) == 1 and not ("Petrifying Breath" in cantrip):    cantrip += "\n - Petrifying Breath (Recharge 5-6): \n\t The monstrosity exhales petrifying gas in a 30-foot cone. Each creature in that area must succeed on a Constitution saving throw (against the creature's Spellsave DC). On a failed save, a target begins to turn to stone and is restrained. The restrained target must repeat the saving throw at the start of its next turn. On a success, the effect ends on the target. On a failure, the target is petrified until freed by the greater restoration spell or other magic."
        if Dice(10) == 1 and not ("Petrifying Gaze" in cantrip):      cantrip += "\n - Petrifying Gaze: \n\t If a creature starts its turn within 30 feet of the monstrosity and the two of them can see each other, the monstrosity can force the creature to make a DC [10+%CON] Constitution saving throw if the monstrosity isn't incapacitated. On a failed save, the creature magically begins to turn to stone and is restrained. It must repeat the saving throw at the start of its next turn. On a success, the effect ends. On a third failure, the creature is petrified until freed by the greater restoration spell or other magic. \n\t A creature that isn't surprised can avert its eyes to avoid the saving throw at the start of its turn. If it does so, it can't see the monstrosity until the start of its next turn, when it can avert its eyes again. If it looks at the monstrosity in the meantime, it must immediately make the save. \n\t If the monstrosity sees its reflection within 30 feet of it in bright light, it mistakes itself for a rival and targets itself with its gaze."
        if Dice(8) == 1 and not ("Read Thoughts" in cantrip):        cantrip += "\n - Read Thoughts: \n\t The monstrosity magically reads the surface thoughts of one creature within 60 feet of it. The effect can penetrate barriers, but 3 feet of wood or dirt, 2 feet of stone, 2 inches of metal, or a thin sheet of lead blocks it. While the target is in range, the monstrosity can continue reading its thoughts, as long as the monstrosity's concentration isn't broken (as if concentrating on a spell). While reading the target's mind, the monstrosity has advantage on Wisdom (Insight) and Charisma (Deception, Intimidation, and Persuasion) checks against the target."


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
    if race == "Ooze":

        difficulty += Dice(3) - Dice(6)
        max_spell_level = get_max_spell_level(Lvl, difficulty)

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
        difficulty += Dice(4) - Dice(4)
        max_spell_level = get_max_spell_level(Lvl, difficulty)

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
        recharge, _ = add_spell(recharge, "Hallucination Spores", max_spell_level, 0, max_spell_level,
                             spell_definition="Recharge(6):" +
                                "\t-Hallucination Spores \n\t The plant ejects spores at one creature it can see within 5 feet of it. The target must succeed on a DC 10+%CON Constitution saving throw or be poisoned for 1 minute. The poisoned target is incapacitated while it hallucinates. The target can repeat the saving throw at the start of each of its turns, ending the effect on itself on a success.")
        recharge, _ = add_spell(recharge, "Rapport Spores", max_spell_level, 0, max_spell_level,
                             spell_definition="Recharge(6):" +
                                "\t-Rapport Spores \n\t A 20-foot radius of spores extends from the plant. These spores can go around corners and affect only creatures with an Intelligence of 2 or higher that aren't undead, constructs, or elementals. Affected creatures can communicate telepathically with one another while they are within 30 feet of each other. The effect lasts for 1 hour.")
        recharge, _ = add_spell(recharge, "Caustic Spores", max_spell_level, 0, max_spell_level,
                             spell_definition="Recharge(6):" +
                                "\t-Caustic Spores \n\t The Plant releases spores in a 30-foot cone. Each creature inside the cone must succeed on a DC [10+%Con] Dexterity saving throw or take 3 (1d6) acid damage at the start of each of the plant's turns. A creature can repeat the saving throw at the start of its turn, ending the effect on itself on a success.")
        recharge, _ = add_spell(recharge, "Infestation Spores", max_spell_level, 0, max_spell_level,
                             spell_definition="Recharge(6):" +
                                "\t- Infestation Spores \n\t The plant releases spores that burst out in a cloud that fills a 10-foot-radius sphere centered on it, and the cloud lingers for 1 minute. Any flesh-and-blood creature in the cloud when it appears, or that enters it later, must make a DC [10+%CON] Constitution saving throw. On a successful save, the creature can't be infected by these spores for 24 hours. On a failed save, the creature is infected with a disease called the spores of Zuggtmoy and also gains a random form of indefinite madness (determined by rolling on the Madness of Zuggtmoy table) that lasts until the creature is cured of the disease or dies. While infected in this way, the creature can't be reinfected, and it must repeat the saving throw at the end of every 24 hours, ending the infection on a success. On a failure, the infected creature's body is slowly taken over by fungal growth, and after three such failed saves, the creature dies and is reanimated as a spore servant if it's a humanoid or a Large or smaller beast. \n d100 \t	Flaw (lasts until cured) \n 01-20 \t I see visions in the world around me that others do not. \n 21-40 \t I periodically slip into a catatonic state, staring off into the distance for long stretches at a time. \n 41-60 \t I see an altered version of reality, with my mind convincing itself that things are true even in the face of overwhelming evidence to the contrary. \n 61-80 \t My mind is slipping away, and my intelligence seems to wax and wane. \n  81-00 \t I am constantly scratching at unseen fungal infections.")
        recharge, _ = add_spell(recharge, "Euphoria Spores", max_spell_level, 0, max_spell_level,
                             spell_definition="Recharge(6):" +
                                 "\t-Euphoria Spores \n\t The plant releases a cloud of spores in a 20-foot-radius sphere centered on itself. " +
                                 "Other creatures in that area must each succeed on a Constitution saving throw or become poisoned for 1 minute. " +
                                 "A creature can repeat the saving throw at the start of each of its turns, ending the effect early on itself on a success. " +
                                 "When the effect ends on it, the creature gains one level of exhaustion.")
        recharge, _ = add_spell(recharge, "Pacifying Spores", max_spell_level, 0, max_spell_level,
                             spell_definition="Recharge(6):" +
                             "\t- Pacifying Spores \n\t The Plant ejects spores at one creature it can see within 5 feet of it. "+
                             "The target must succeed on a Constitution saving throw or be stunned for 1 minute. "+
                             "The target can repeat the saving throw at the start of each of its turns, ending the effect on itself on a success.")
        recharge, _ = add_spell(recharge, "Animating Spores", max_spell_level, 0, max_spell_level,
                             spell_definition="Recharge(6):" +
                                 "\t- Animating Spores \n\t The Plant targets one corpse of a humanoid or a Large or smaller beast within 5 feet of it and releases spores at the corpse. "+
                                 "Next turn, the corpse rises as a spore servant. The corpse stays animated for 1d4 + 1 weeks or until destroyed, and it can't be animated again in this way.")


    if race == "Plant":
        difficulty += Dice(4) - Dice(6)
        max_spell_level = get_max_spell_level(Lvl, difficulty)

        cantrips_list += ["Druidcraft",
                         "Shillelagh",
                         "Poison Spray",
                         "Thorn Whip"]
        one_day_each_list += ["Entangle", "Goodberry", "Speak with Plants"]
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
        difficulty += Dice(6) - Dice(8)
        max_spell_level = get_max_spell_level(Lvl, difficulty)

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
        if Dice(8) == 1 and not ("Create Specter" in recharge):             recharge += "\n - Create Specter (Recharge 6)\n\t The undead targets a humanoid within 10 feet of it that has been dead for no longer than 1 minute and died violently. The target's spirit rises as a specter in the space of its corpse or in the nearest unoccupied space. The specter is under the undead's control. The undead can have no more than seven specters under its control at one time." 
        if Dice(8) == 1 and not ("Corrupting Touch" in recharge):           recharge += "\n - Corrupting Touch (Recharge 6)\n\t Melee Spell Attack: reach 5 ft., one target. Hit: 10 (3d6) necrotic damage."
        if Dice(8) == 1 and not ("Dreadful Glare" in recharge):             recharge += "\n - Dreadful Glare.(Recharge 6) \n\t The undead targets one creature it can see within 60 feet of it. If the target can see the undead, it must succeed on a DC [10+%CHA] Wisdom saving throw against this magic or become frightened until the end of the undead's next turn. If the target fails the saving throw by 5 or more, it is also paralyzed for the same duration. A target that succeeds on the saving throw is immune to the Dreadful Glare of all undead for the next 24 hours."
        if Dice(8) == 1 and not ("Forceful Slam" in recharge):              recharge += "\n - Forceful Slam (Recharge 6)\n\t Magic melee attack. Hit: 10 (3d6) force damage. "
        if Dice(8) == 1 and not ("Fire Ray" in recharge):                   recharge += "\n - Fire Ray (Recharge 6)\n\t Magic attack. Range 30 ft. Hit: 10 (3d6) fire damage. "
        if Dice(8) == 1 and not ("Horrifying Visage" in recharge):          recharge += "\n - Horrifying Visage (Recharge 6)\n\t Each non-undead creature within 60 feet of the Undead that can see them must succeed on a DC [10+%CHA] Wisdom saving throw or be frightened for 1 minute. A frightened target can repeat the saving throw at the start of each of its turns, with disadvantage if the Undead is within line of sight, ending the effect on itself on a success. If a target's saving throw is successful or the effect ends for it, the target is immune to the Undead's Horrifying Visage for the next 24 hours. "
        if Dice(8) == 1 and not ("Life Drain" in recharge):                 recharge += "\n - Life Drain (Recharge 6)\n\t On an hit, the target's Hit Points Maximum is reduced by the damage dealt. The target dies if this reduces its Hit Points Maximum to 0. Otherwise, the reduction lasts until the target finishes a short or long rest. "
        elif Dice(8) == 1 and not ("Life Drain" in recharge):               recharge += "\n - Life Drain (Recharge 6)\n\t On an hit, the target makes a Constitution saving throw. On a fail, the target takes 4d6 necrotic damage. The target's Hit Points Maximum is reduced by the necrotic damage dealt. The target dies if this reduces its Hit Points Maximum to 0. Otherwise, the reduction lasts until the target finishes a long rest. "
        if Dice(8) == 1 and not ("Rotting Fist" in recharge):               recharge += "\n - Rotting Fist. (Recharge 6)\n\t Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) bludgeoning damage plus 10 (3d6) necrotic damage. If the target is a creature, it must succeed on a DC [10+%CHA] Constitution saving throw or be cursed with undead rot. The cursed target can't regain hit points, and its hit point maximum decreases by 10 (3d6) for every 24 hours that elapse. If the curse reduces the target's hit point maximum to 0, the target dies, and its body turns to dust. The curse lasts until removed by the remove curse spell or other magic."
        if Dice(8) == 1 and not ("Strength Drain" in recharge):             recharge += "\n - Strength Drain (Recharge 6)\n\t On an attack hit the target's Strength score is reduced by 1d4. The target dies if this reduces its Strength to 0. Otherwise, the reduction lasts until the target finishes a short or long rest. \n\t If a non-evil humanoid dies from this attack, a new shadow rises from the corpse 1d4 hours later."
        if Dice(8) == 1 and not ("Telekinetic Thrust" in recharge):         recharge += "\n - Telekinetic Thrust.(Recharge 6) \n\t The undead targets a creature or unattended object within 30 feet of it. A creature must be Medium or smaller to be affected by this magic, and an object can weigh up to 150 pounds. \n\t If the target is a creature, the undead makes a Charisma check contested by the target's Strength check. If the undead wins the contest, the undead hurls the target up to 30 feet in any direction, including upward. If the target then comes into contact with a hard surface or heavy object, the target takes 1d6 damage per 10 feet moved. \n\t If the target is an object that isn't being worn or carried, the undead hurls it up to 30 feet in any direction. The undead can use the object as a ranged weapon, attacking one creature along the object's path (+4 to hit) and dealing 5 (2d4) bludgeoning damage on a hit."
        if Dice(8) == 1 and not ("Wail" in recharge):                       recharge += "\n - Wail. (Rechrge 6)\n\t The undead releases a mournful wail, provided that they aren't in sunlight. This wail has no effect on constructs and undead. All other creatures within 30 feet of them that can hear them must make a DC [10+%CHA] Constitution saving throw. On a failure, a creature drops to 0 hit points. On a success, a creature takes 10 (3d6) psychic damage."
    if race == "Undead":

        difficulty += Dice(6) - Dice(12)
        max_spell_level = get_max_spell_level(Lvl, difficulty)

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
        ninth_list += ["Astral Projection",                      "Gate",                      "Power Word Kill",                      "True Resurrection",                      "Wish"]
                
    #def add_spell(spell_list, spell_name, spell_level, slots, max_spell_level, spell_definition=""):

    # Ensure there are no duplicates in the lists
    cantrips_list = list(set(cantrips_list))
    first_list = list(set(first_list))
    second_list = list(set(second_list))
    third_list = list(set(third_list))
    fourth_list = list(set(fourth_list))
    fifth_list = list(set(fifth_list))
    sixth_list = list(set(sixth_list))
    seventh_list = list(set(seventh_list))
    eighth_list = list(set(eighth_list))
    ninth_list = list(set(ninth_list))
    three_day_each_list = list(set(three_day_each_list))
    two_day_each_list = list(set(two_day_each_list)) 
    one_day_each_list = list(set(one_day_each_list))


    numc = min(5, len(cantrips_list))
    num1 = min(10, len(first_list))
    num2 = min(9, len(second_list))
    num3 = min(8, len(third_list))
    num4 = min(7, len(fourth_list))
    num5 = min(6, len(fifth_list))
    num6 = min(5, len(sixth_list))
    num7 = min(4, len(seventh_list))
    num8 = min(3, len(eighth_list))
    num9 = min(2, len(ninth_list))
    num1d = min(5, len(one_day_each_list))
    num2d = min(5, len(two_day_each_list))
    num3d = min(5, len(three_day_each_list))
    
    cantrips_list = random.sample(cantrips_list, numc)
    first_list = random.sample(first_list, num1)
    second_list = random.sample(second_list, num2)
    third_list = random.sample(third_list, num3)
    fourth_list = random.sample(fourth_list, num4)
    fifth_list = random.sample(fifth_list, num5)
    sixth_list = random.sample(sixth_list, num6)
    seventh_list = random.sample(seventh_list, num7)
    eighth_list = random.sample(eighth_list, num8)
    ninth_list = random.sample(ninth_list, num9)
    one_day_each_list = random.sample(one_day_each_list, num1d)
    two_day_each_list = random.sample(two_day_each_list, num2d)
    three_day_each_list = random.sample(three_day_each_list, num3d)
    for c in cantrips_list:
        cantrip, _ = add_spell(cantrip, c, 0, 0, max_spell_level)
    for s in first_list:
        first, slots1 = add_spell(first, s, 1, slots1, max_spell_level)
    for s in second_list:
        second, slots2 = add_spell(second, s, 2, slots2, max_spell_level)
    for s in third_list:
        third, slots3 = add_spell(third, s, 3, slots3, max_spell_level)
    for s in fourth_list:
        fourth, slots4 = add_spell(fourth, s, 4, slots4, max_spell_level)
    for s in fifth_list:
        fifth, slots5 = add_spell(fifth, s, 5, slots5, max_spell_level)
    for s in sixth_list:
        sixth, slots6 = add_spell(sixth, s, 6, slots6, max_spell_level)
    for s in seventh_list:
        seventh, slots7 = add_spell(seventh, s, 7, slots7, max_spell_level)
    for s in eighth_list:
        eighth, slots8 = add_spell(eighth, s, 8, slots8, max_spell_level)
    for s in ninth_list:
        ninth, slots9 = add_spell(ninth, s, 9, slots9, max_spell_level)
    for s in three_day_each_list:
        three, _ = add_spell(three, s, max_spell_level-3, 0, max_spell_level, spell_definition="3/Day")
    for s in two_day_each_list:
        two, _ = add_spell(two, s, max_spell_level-2, 0, max_spell_level, spell_definition="2/Day")
    for s in one_day_each_list:
        one, _ = add_spell(one, s, max_spell_level-1, 0, max_spell_level, spell_definition="1/Day")
        

    r = "\n"
    if not (cantrip == "Cantrips (at will): "):         r += cantrip + "\n"
    if not (first == "1st Level Spells: "):             r += "[{}]".format(min(10,Dice(slots1))) + first  + "\n"
    if Lvl>=3:
        if not (second == "2nd Level Spells: "):        r += "[{}]".format(min(10,Dice(slots2)))  + second + "\n"
    if Lvl>=5:
        if not (third == "3rd Level Spells: "):         r += "[{}]".format(min(10,Dice(slots3)))+ third  + "\n"
    if Lvl>=7:
        if not (fourth == "4th Level Spells: "):        r += "[{}]".format( min(10,Dice(slots4))) + fourth + "\n"
    if Lvl>=9:
        if not (fifth == "5th Level Spells: "):         r += "[{}]".format(min(9,Dice(slots5))) + fifth  + "\n"
    if Lvl>=11:
        if not (sixth == "6th Level Spells: "):         r += "[{}]".format(min(8,Dice(slots6))) + sixth  + "\n"
    if Lvl>=15:
        if not (seventh == "7th Level Spells: "):       r += "[{}]".format(min(7,Dice(slots7))) + seventh + "\n"
    if Lvl>=18:
        if not (eighth == "8th Level Spells: "):         r += "[{}]".format(min(6,Dice(slots8))) + eighth  + "\n"
    if Lvl>=20:
        if not (ninth == "9th Level Spells: "):         r += "[{}]".format(min(5,Dice(slots9))) + ninth  + "\n"
    if not (one == "1/Day each: "):        r += "\n" + one
    if not (two == "2/Day each: "):        r += "\n" + two
    if not (three == "3/Day each: "):      r += "\n" + three
    if recharge: r += "\n" + "Recharge:" + recharge
    return r


























def Senses(npc):
    race = npc.race
    background = npc.background
    # Senses
    sense = ""
    normal = 0
    darkvision = 0
    blindsight = 0
    tremorsense = 0
    telepathy = 0
    truesight = 0

    extras = ""

    # Enhanced Senses
    enhanced_smell =    f"\n- Enhanced Smell: The {race} can detect specific odors or substances within 60 feet."
    enhanced_hearing =  f"\n- Enhanced Hearing: The {race} can hear frequencies outside the normal range and detect sounds from up to {Dice(12) * 100} feet away."
    enhanced_taste =    f"\n- Enhanced Taste: The {race} can taste and identify specific ingredients or substances, and has advantage on saving throws against ingested poisons."
    enhanced_touch =    f"\n- Enhanced Touch: The {race} can feel vibrations through surfaces and detect changes in air pressure."
    keen_smell =        f"\n- Keen Smell. \n\t The {race} has advantage on Wisdom (Perception) checks that rely on smell."
    keen_hearing =      f"\n- Keen Hearing. \n\t The {race} has advantage on Wisdom (Perception) checks that rely on hearing."


    # Specialized Senses
    echolocation = f"\n- Echolocation: The {race} can perceive its surroundings within 60 feet as if it had blindsight, but only if it isn't deafened."
    electroreception = f"\n- Electroreception: The {race} can detect electric fields within 30 feet, useful for tracking creatures and navigating underwater."
    heat_vision = f"\n- Heat Vision: The {race} can see infrared radiation, allowing it to see heat signatures within 60 feet."
    magnetoreception = f"\n- Magnetoreception: The {race} can sense magnetic fields, and therefor presence of metals, aiding in navigation."

    # Psychic Senses
    aura_sense = f"\n- Aura Sense: The {race} can see the auras of living beings within 30 feet, possibly determining their emotional state or alignment."
    empathy = f"\n- Empathy: The {race} can sense the emotions of others within 30 feet."
    precognition = f"\n- Precognition: The {race} has brief, unreliable glimpses of possible future events."
    psychometry = f"\n- Psychometry: The {race} can read the history of an object it touches."

    # Sensory Communication
    pheromones = f"\n- Pheromones: The {race} can communicate with others of its kind through the release of chemical signals."
    color_change = f"\n- Color Change: The {race} can change the color of its skin to communicate or as a response to its environment."

    # Sensory Deprivation & Resistance
    sensory_dampening = f"\n- Sensory Dampening: The {race} can voluntarily dampen its own senses to resist sensory overload or certain types of attacks. Until the end of turn, all their Perception (Wisdom) checks are made at disadvantage"
    blind_fighting = f"\n- Blind Fighting: The {race} doesn’t need to see a creature to target it with an attack, provided the creature isn't hidden from the {race}."

    # Hide and Mimic
    mimicry = (f"\n- Mimicry \n\t The {race} can mimic simple sounds it has heard, such as a person whispering, a baby crying, or an animal chittering. " 
                "A creature that hears the sounds can tell they are imitations with a successful DC {8+npc.proficiency_bonus} Wisdom (Insight) check.")
    chameleon_skin = "\n - Chameleon Skin \n\t The {race} has advantage on Dexterity (Stealth) checks made to hide."

    # Enviromental adaptations
    water_breathing= f"\n- Water Breathing. The {race} can breathe underwater"
    underwater_camouflage = f"\n- Underwater Camouflage. \n\t The {race} has advantage on Dexterity (Stealth) checks made while underwater."
    hold_breath = f"\n- Hold Breath. \n\t The {race} can hold its breath for {5*Dice(3)*Dice(4)} minutes"

    # Sensibilities
    sunlight_sensitivity = f"\n - Sunlight Sensitivity:\t While in sunlight, the {race} has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."

    # Illumination
    illumination = f"\n- Illumination:\t The {race} sheds bright light in a {Dice(3)*10}-foot radius and dim light for an additional {Dice(3)*10} ft."



                
    if race in [ "Human", "Aberration", "Aven", "Beast", "Beastfolk", "Celestial", "Construct", "Dragon","Dwarf","Elf","Elemental","Fey","Fiend",
        "Giant","Gnome","Goblin","Halfling","Kobold","Lizardfolk","Monstrosity","Ooze","Orc","Plant","Snakefolk","Undead"]:
        normal = 60
        
    if race == "Aberration":
        normal      -= Dice(2) * Dice(6) * 30
        blindsight  += Dice(0) * Dice(4) * 30
        telepathy   += Dice(0) * Dice(4) * 30
        tremorsense += Dice(0) * Dice(3) * 10
        truesight   += Dice(0) * Dice(3) * 10
        extras      += f"\n- Sense Magic: \t The {race} senses magic within 120 feet of it at will. This trait otherwise works like the Detect Magic spell but isn't itself magical."

        if Dice()==1: extras += enhanced_smell
        if Dice()==1: extras += enhanced_hearing
        if Dice()==1: extras += enhanced_taste
        if Dice()==1: extras += enhanced_touch
        if Dice()==1: extras += echolocation
        if Dice()==1: extras += electroreception
        if Dice()==1: extras += heat_vision
        if Dice()==1: extras += magnetoreception
        if Dice()==1: extras += aura_sense
        if Dice()==1: extras += empathy
        if Dice()==1: extras += precognition
        if Dice()==1: extras += psychometry
        if Dice()==1: extras += pheromones
        if Dice()==1: extras += color_change
        if Dice()==1: extras += sensory_dampening
        if Dice()==1: extras += blind_fighting
        if Dice()==1: extras += keen_smell
        if Dice()==1: extras += water_breathing
        if Dice()==1: extras += underwater_camouflage
        if Dice()==1: extras += hold_breath
        if Dice()==1: extras += keen_hearing
        if Dice()==1: extras += chameleon_skin
        if Dice()==1: extras += sunlight_sensitivity
    if race == "Aven":
        normal      += Dice(2) * Dice(6) * 30
        darkvision  += Dice(0) * Dice(6) * 30
        blindsight  += Dice(0) * Dice(3) * 10
        tremorsense -= Dice(0) * Dice(0) * 10
        telepathy   += Dice(0) * Dice(6) * 10
        truesight   += Dice(0) * Dice(0) * 10

        extras += f"\n- Keen Sight: \t Advantage on Wisdom (Perception) checks that rely on sight."
        if Dice()==1: extras += enhanced_hearing
        if Dice()==1: extras += magnetoreception
        if Dice(12)==1: extras += aura_sense
        if Dice()==1: extras += sensory_dampening
        if Dice(12)==1: extras += blind_fighting
        if Dice==1: extras += mimicry
        if Dice()==1: extras += hold_breath

    if race == "Beast":
        normal      += Dice(2) * Dice(8) * 30
        darkvision  += Dice(0) * Dice(5) * 30
        blindsight  += Dice(0) * Dice(3) * Dice(4) * 10
        tremorsense += Dice(0) * Dice(6) * 10
        telepathy   += Dice(0) * Dice(3) * 10
        truesight   += Dice(0) * Dice(6) * 10

        extras += f"\n- Keen Senses: Advantage on Wisdom (Perception) checks that rely on one of their senses"
        if Dice()==1: extras += enhanced_smell
        if Dice()==1: extras += enhanced_hearing
        if Dice()==1: extras += enhanced_taste
        if Dice()==1: extras += echolocation
        if Dice()==1: extras += electroreception
        if Dice()==1: extras += heat_vision
        if Dice()==1: extras += magnetoreception
        if Dice()==1: extras += empathy
        if Dice()==1: extras += pheromones
        if Dice()==1: extras += color_change
        if Dice(12)==1: extras += blind_fighting
        if Dice()==1: extras += keen_smell
        if Dice()==1: extras += mimicry
        if Dice()==1: extras += water_breathing
        if Dice()==1: extras += underwater_camouflage
        if Dice()==1: extras += hold_breath
        if Dice()==1: extras += keen_hearing
        if Dice()==1: extras += chameleon_skin
        if Dice()==1: extras += sunlight_sensitivity
        if Dice()==1: extras += illumination
        
    if race == "Beastfolk":
        normal      += Dice(2) * Dice(8) * 30
        darkvision  += Dice(0) * Dice(5) * 30
        blindsight  += Dice(0) * Dice(3) * Dice(4) * 10
        tremorsense += Dice(0) * Dice(6) * 5
        telepathy   += Dice(0) * Dice(6) * 10
        truesight   += Dice(0) * Dice(3) * 10

        extras += f"\n- Keen Senses: Advantage on Wisdom (Perception) checks that rely on one of their senses"
        extras += "\n- Speak with Animal:\t The Beastfolk can communicate simple concepts to his affinity animal when it speaks in Beast language."


        if Dice()==1: extras += enhanced_smell
        if Dice()==1: extras += enhanced_hearing
        if Dice()==1: extras += enhanced_taste
        if Dice()==1: extras += echolocation
        if Dice()==1: extras += electroreception
        if Dice()==1: extras += heat_vision
        if Dice()==1: extras += magnetoreception
        if Dice()==1: extras += precognition
        if Dice()==1: extras += pheromones
        if Dice()==1: extras += color_change
        if Dice()==1: extras += blind_fighting
        if Dice()==1: extras += water_breathing
        if Dice()==1: extras += underwater_camouflage
        if Dice()==1: extras += hold_breath
        if Dice()==1: extras += chameleon_skin
        if Dice()==1: extras += sunlight_sensitivity
        if Dice()==1: extras += illumination
        
    if race == "Celestial":
        normal      += Dice(2) * Dice(10) * 20
        darkvision  += Dice(6) * Dice(6) * 10
        blindsight  += Dice(0) * Dice(6) * 10
        tremorsense += Dice(0) * Dice(0) * 5
        telepathy   += Dice(0) * Dice(10) * 20
        truesight   += Dice(3) * Dice(6) * 10

        extras += f"\n- Radiant Sight: Can see divine auras and celestial beings within a {normal} range."
        if Dice()==1: extras += aura_sense
        if Dice()==1: extras += empathy
        if Dice()==1: extras += precognition
        if Dice(12)==1: extras += psychometry
        if Dice()==1: extras += blind_fighting
        if Dice()==1: extras += keen_hearing
        if Dice()==1: extras += illumination


    if race == "Construct":
        normal      += Dice(6) * Dice(6) * 20 - Dice(12)*10
        darkvision  += Dice(0) * Dice(6) * Dice(6) * 10
        blindsight  += Dice(0) * Dice(4) * Dice(4) * 10
        tremorsense += Dice(0) * Dice(3) * 5
        telepathy   += Dice(0) * Dice(0) * 20
        truesight   += Dice(0) * Dice(4) * Dice(4) * 10

        extras += f""
        if Dice()==1: extras += enhanced_hearing
        if Dice()==1: extras += enhanced_touch
        if Dice()==1: extras += electroreception
        if Dice()==1: extras += heat_vision
        if Dice()==1: extras += magnetoreception
        if Dice()==1: extras += precognition
        if Dice(12)==1: extras += psychometry
        if Dice()==1: extras += color_change
        if Dice()==1: extras += sensory_dampening
        if Dice()==1: extras += blind_fighting
        if Dice()==1: extras += mimicry
        if Dice()==1: extras += illumination

    if race == "Dragon":
        normal      += Dice(2) * Dice(12) * 20
        darkvision  += Dice(0) * Dice(12) * 20
        blindsight  += Dice(0) * Dice(12) * 10
        tremorsense += Dice(0) * Dice(3) * 5
        telepathy   += Dice(0) * Dice(6) * 20
        truesight   += Dice(0) * Dice(6) * 10

        extras += f""

        if Dice()==1: extras += enhanced_smell
        if Dice()==1: extras += enhanced_hearing
        if Dice()==1: extras += enhanced_taste
        if Dice()==1: extras += enhanced_touch
        if Dice()==1: extras += heat_vision
        if Dice(12)==1: extras += magnetoreception
        if Dice(12)==1: extras += aura_sense
        if Dice(12)==1: extras += empathy
        if Dice(12)==1: extras += precognition
        if Dice()==1: extras += psychometry
        if Dice()==1: extras += pheromones
        if Dice()==1: extras += color_change
        if Dice()==1: extras += blind_fighting
        if Dice()==1: extras += keen_smell
        if Dice(12)==1: extras += water_breathing
        if Dice()==1: extras += underwater_camouflage
        if Dice()==1: extras += hold_breath
        if Dice()==1: extras += keen_hearing
        if Dice()==1: extras += chameleon_skin

    if race == "Dwarf":
        normal      += Dice(2) * Dice(4) * 20
        darkvision  += Dice(2) * Dice(6) * 20
        blindsight  += Dice(0) * Dice(1) * 10
        tremorsense += Dice(0) * Dice(1) * 5
        telepathy   += Dice(0) * Dice(3) * 10
        truesight   += Dice(0) * Dice(0) * 10

        extras += f""
        if Dice()==1: extras += psychometry
        if Dice()==1: extras += sunlight_sensitivity
        
    if race == "Elf":
        normal      += Dice(2) * Dice(12) * 20
        darkvision  += Dice(0) * Dice(6) * 20
        blindsight  += Dice(0) * Dice(0) * 10
        tremorsense += 0 * 5
        telepathy   += Dice(0) * Dice(3) * 10
        truesight   += Dice(0) * Dice(0) * 10

        extras += f"\n- Keen Senses: Advantage on Wisdom (Perception) checks that rely on sight and hearing."
        if Dice()==1: extras += enhanced_hearing
        if Dice()==1: extras += blind_fighting
        if Dice()==1: extras += sunlight_sensitivity

    if race == "Elemental":
        normal      += Dice(2) * Dice(6) * 20
        darkvision  += Dice(0) * Dice(6) * Dice(3) * 10
        blindsight  += Dice(0) * Dice(3) * 10
        tremorsense += Dice(0) * Dice(4) * Dice(4) * 5
        telepathy   += Dice(0) * Dice(0) * 10
        truesight   += Dice(0) * Dice(2) * 10

        extras += f""
        if Dice()==1: extras += electroreception
        if Dice()==1: extras += heat_vision
        if Dice()==1: extras += magnetoreception
        if Dice()==1: extras += water_breathing
        if Dice()==1: extras += underwater_camouflage
        if Dice()==1: extras += chameleon_skin
        if Dice()==1: extras += illumination



    if race == "Fey":
        normal      += Dice(2) * Dice(6) * 20
        darkvision  += Dice(2) * Dice(6) * 20
        blindsight  += Dice(0) * Dice(3) * 10
        tremorsense += 0 * Dice(0) * 5
        telepathy   += Dice(2) * Dice(6) * 10
        truesight   += Dice(0) * Dice(6) * 10

        extras += f"\n- Fey Sight: Can see through magical darkness and illusions up to {normal} feet."
        
        if Dice()==1: extras += aura_sense
        if Dice()==1: extras += empathy
        if Dice()==1: extras += precognition
        if Dice()==1: extras += psychometry
        if Dice()==1: extras += pheromones
        if Dice()==1: extras += blind_fighting
        if Dice()==1: extras += mimicry
        if Dice()==1: extras += chameleon_skin
        
    if race == "Fiend":
        normal      += Dice(4) * Dice(6) * 20
        darkvision  += Dice(2) * Dice(6) * 20
        blindsight  += Dice(0) * Dice(10) * 10
        tremorsense += Dice(0) * Dice(2) * 5
        telepathy   += Dice(0) * Dice(12) * 10
        truesight   += Dice(2) * Dice(6) * 10

        extras += f""

        if Dice(12)==1: extras += enhanced_smell
        if Dice()==1: extras += enhanced_taste
        if Dice(12)==1: extras += heat_vision
        if Dice()==1: extras += aura_sense
        if Dice()==1: extras += precognition
        if Dice()==1: extras += psychometry
        if Dice()==1: extras += sensory_dampening
        if Dice()==1: extras += blind_fighting
        if Dice()==1: extras += keen_smell
        if Dice()==1: extras += mimicry
        if Dice()==1: extras += hold_breath
        if Dice()==1: extras += sunlight_sensitivity

    if race == "Giant":
        normal      += Dice(3) * Dice(6) * 20
        darkvision  += Dice(0) * Dice(0) * 20
        blindsight  += Dice(0) * Dice(0) * 10
        tremorsense += Dice(0) * Dice(0) * 5
        telepathy   += Dice(0) * Dice(0) * 10
        truesight   += Dice(0) * Dice(0) * 10

        extras += f""
        if Dice()==1: extras += psychometry
        if Dice()==1: extras += keen_smell
        if Dice()==1: extras += sunlight_sensitivity
        
    if race == "Gnome":
        normal      += Dice(10) * Dice(10) * 20
        darkvision  += Dice(2) * Dice(6) * 20
        blindsight  += Dice(0) * Dice(5) * 10
        tremorsense += Dice(0) * Dice(0) * 5
        telepathy   += Dice(0) * Dice(3) * 10
        truesight   += Dice(0) * Dice(0) * 10

        extras += f""
        if Dice()==1: extras += empathy
        if Dice()==1: extras += precognition
        if Dice()==1: extras += psychometry
        if Dice()==1: extras += mimicry
        
    if race == "Goblin":
        normal      += Dice(10) * Dice(10) * 20
        darkvision  += Dice(2) * Dice(6) * 20
        blindsight  += Dice(0) * Dice(0) * 10
        tremorsense += Dice(0) * Dice(0) * 5
        telepathy   += Dice(0) * Dice(0) * 10
        truesight   += Dice(0) * Dice(0) * 10

        extras += f""
        if Dice()==1: extras += enhanced_smell
        if Dice()==1: extras += enhanced_hearing
        if Dice()==1: extras += keen_smell

    if race == "Halfling":
        normal      += Dice(10) * Dice(10) * 20
        darkvision  += Dice(0) * Dice(0) * 20
        blindsight  += Dice(0) * Dice(0) * 10
        tremorsense += Dice(0) * Dice(0) * 5
        telepathy   += Dice(0) * Dice(0) * 10
        truesight   += Dice(0) * Dice(0) * 10

        extras += f""
        if Dice()==1: extras += precognition

    if race == "Kobold":
        normal      += Dice(0) * Dice(0) * 20
        darkvision  += Dice(2) * Dice(6) * 20
        blindsight  += Dice(0) * Dice(0) * 10
        tremorsense += Dice(0) * Dice(0) * 5
        telepathy   += Dice(0) * Dice(0) * 10
        truesight   += Dice(0) * Dice(0) * 10

        extras += f""

        if Dice()==1: extras += enhanced_smell
        if Dice()==1: extras += enhanced_taste
        if Dice()==1: extras += keen_smell
        if Dice()==1: extras += hold_breath
        if Dice()==1: extras += sunlight_sensitivity

    if race == "Lizardfolk":
        normal      += Dice(10) * Dice(10) * 20
        darkvision  += Dice(4) * Dice(3) * 10
        blindsight  += Dice(0) * Dice(0) * 10
        tremorsense += Dice(0) * Dice(0) * 5
        telepathy   += Dice(0) * Dice(0) * 10
        truesight   += Dice(0) * Dice(0) * 10

        extras += f""
        if Dice(2)==1: extras += enhanced_smell
        if Dice()==1: extras += enhanced_taste
        if Dice()==1: extras += enhanced_touch
        if Dice()==1: extras += heat_vision
        if Dice()==1: extras += pheromones
        if Dice()==1: extras += color_change
        if Dice()==1: extras += sensory_dampening
        if Dice()==1: extras += blind_fighting
        if Dice()==1: extras += keen_smell
        if Dice()==1: extras += underwater_camouflage
        if Dice()==1: extras += hold_breath
        if Dice()==1: extras += chameleon_skin
        if Dice(8)==1: extras += sunlight_sensitivity

    if race == "Monstrosity":
        normal      += Dice(-1) * Dice(100) * 20
        darkvision  += Dice(0) * Dice(12) * 20
        blindsight  += Dice(0) * Dice(12) * 10
        tremorsense += Dice(0) * Dice(12) * 5
        telepathy   += Dice(0) * Dice(12) * 10
        truesight   += Dice(0) * Dice(3) * Dice(2) * 10

        extras += f""
        if Dice(12)==1: extras += enhanced_smell 
        if Dice(12)==1: extras += enhanced_hearing
        if Dice(12)==1: extras += enhanced_taste
        if Dice(12)==1: extras += enhanced_touch
        if Dice(12)==1: extras += echolocation
        if Dice(12)==1: extras += electroreception
        if Dice(12)==1: extras += heat_vision
        if Dice(12)==1: extras += magnetoreception
        if Dice(12)==1: extras += pheromones
        if Dice(12)==1: extras += color_change
        if Dice(12)==1: extras += sensory_dampening
        if Dice(12)==1: extras += blind_fighting
        if Dice(12)==1: extras += keen_smell
        if Dice(12)==1: extras += mimicry
        if Dice(12)==1: extras += water_breathing
        if Dice(12)==1: extras += underwater_camouflage
        if Dice(12)==1: extras += hold_breath
        if Dice(12)==1: extras += chameleon_skin
        if Dice(12)==1: extras += sunlight_sensitivity
        if Dice(12)==1: extras += illumination

    if race == "Ooze":
        normal      += Dice(-1) * Dice(0) * 60
        darkvision  += Dice(-1) * Dice(0) * 20
        blindsight  += Dice(0) * Dice(3) * 10
        tremorsense += Dice(0) * Dice(6) * 5
        telepathy   += Dice(0) * Dice(12) * 10
        truesight   += Dice(-1) * Dice(0) * 10

        extras += f""
        if Dice()==1: extras += electroreception
        if Dice()==1: extras += magnetoreception
        if Dice()==1: extras += pheromones
        if Dice()==1: extras += color_change
        if Dice(2)==1: extras += blind_fighting
        if Dice()==1: extras += water_breathing
        if Dice()==1: extras += underwater_camouflage

    if race == "Orc":
        normal      += Dice(10) * Dice(10) * 20
        darkvision  += Dice(2) * Dice(6) * 20
        blindsight  += Dice(0) * Dice(0) * 10
        tremorsense += Dice(0) * Dice(0) * 5
        telepathy   += Dice(0) * Dice(0) * 10
        truesight   += Dice(0) * Dice(0) * 10

        extras += f""
        if Dice()==1: extras += enhanced_touch

    if race == "Plant":
        normal      += Dice(-10) * Dice(10) * 20
        darkvision  += Dice(-1) * Dice(0) * 20
        blindsight  += Dice(4) * Dice(3) * 10
        tremorsense += Dice(2) * Dice(3) * 5
        telepathy   += Dice(0) * Dice(6) * 10
        truesight   += Dice(0) * Dice(3) * 10

        extras += f""
        if Dice()==1: extras += enhanced_touch
        if Dice()==1: extras += aura_sense
        if Dice()==1: extras += empathy
        if Dice()==1: extras += pheromones
        if Dice()==1: extras += color_change
        if Dice()==1: extras += blind_fighting
        if Dice()==1: extras += water_breathing
        if Dice()==1: extras += underwater_camouflage
        if Dice()==1: extras += chameleon_skin
        if Dice(20)==1: extras += sunlight_sensitivity
        if Dice(20)==1: extras += illumination

    if race == "Snakefolk":
        normal      += Dice(10) * Dice(10) * 20
        darkvision  += Dice(2) * Dice(6) * 20
        blindsight  += Dice(2) * Dice(4) * 10
        tremorsense += Dice(0) * Dice(3) * 5
        telepathy   += Dice(0) * Dice(2) * 10
        truesight   += Dice(0) * Dice(0) * 10

        extras += f""
        if Dice()==1: extras += enhanced_smell
        if Dice()==1: extras += enhanced_taste
        if Dice()==1: extras += enhanced_touch
        if Dice()==1: extras += electroreception
        if Dice()==1: extras += heat_vision
        if Dice()==1: extras += magnetoreception
        if Dice()==1: extras += pheromones
        if Dice()==1: extras += color_change
        if Dice()==1: extras += blind_fighting
        if Dice()==1: extras += keen_smell
        if Dice()==1: extras += underwater_camouflage
        if Dice()==1: extras += hold_breath
        if Dice()==1: extras += chameleon_skin
        

    if race == "Undead":
        normal      += Dice(10) * Dice(10) * 20
        darkvision  += Dice(0) * Dice(12) * 20
        blindsight  += Dice(0) * Dice(12) * 10
        tremorsense += Dice(0) * Dice(5) * 5
        telepathy   += Dice(0) * Dice(12) * 10
        truesight   += Dice(0) * Dice(12) * 10
        extras += f""
        
        if Dice()==1: extras += enhanced_taste
        if Dice()==1: extras += aura_sense
        if Dice()==1: extras += precognition
        if Dice()==1: extras += sensory_dampening
        if Dice()==1: extras += blind_fighting
        if Dice()==1: extras += sunlight_sensitivity
        if Dice(100)==1: extras += illumination

    if race == "":
        normal      += Dice(10) * Dice(10) * 20
        darkvision  += Dice(0) * Dice(0) * 20
        blindsight  += Dice(0) * Dice(0) * 10
        tremorsense += Dice(0) * Dice(0) * 5
        telepathy   += Dice(0) * Dice(0) * 10
        truesight   += Dice(0) * Dice(0) * 10

        extras += f""
        
        
    # Additional sense-related abilities
    if telepathy>0:
        if Dice() == 1:
            extras += f"\n- Advanced Telepathy: \n\t The {race} can perceive the content of any telepathic communication used within {telepathy//2} feet of it, and it can't be surprised by creatures with any form of telepathy."
        if Dice() == 1:
            extras += f"\n- Telepathic Shroud. \n\t The {race} is immune to any effect that would sense its emotions or read its thoughts, as well as all divination spells."
        if Dice() == 1:
            extras += f"\n- Limited Telepathy. \n\t The {race} can magically transmit simple messages and images to any creature within {telepathy} feet of it that can understand a language. This form of telepathy doesn't allow the receiving creature to telepathically respond."
        if Dice() == 1:
            extras += f"\n- Detect Sentience: \n\t The {race} can sense the presence and location of any creature within {2*telepathy} feet of it that has an Intelligence of 3 or higher, regardless of interposing barriers, unless the creature is protected by a mind blank spell."

    if normal<=0: sense += f"Blind\t"
    if darkvision>0: sense += f"Darkvision: {darkvision}ft. \t"
    if blindsight>0: sense += f"Blindsight: {blindsight}ft. \t"
    if tremorsense>0: sense += f"Tremorsense: {tremorsense}ft. \t"
    if truesight>0: sense += f"Truesight: {truesight}ft. \t"
    sense += extras

    return sense



































def Movement(npc):

    race = npc.race
    background = npc.background

    # movement
    movement = "Speed: "
    normal = 0
    fly = 0
    swim = 0
    burrow = 0
    climb = 0

    extras = ""

    spider_climb = f"\n -Spider Climb: \t The {race} can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."
    flyby = f"\n- Flyby \n\t The {race} is an agile flier, quick to fly out of enemies' reach. The {race} doesn't provoke an opportunity attack when it flies out of an enemy's reach."
    earth_glide = f"\n- Earth Glide:\t The {race} can burrow through nonmagical, unworked earth and stone. While doing so, the {race} doesn't disturb the material it moves through."

    if race in [ "Human", "Aberration", "Aven", "Beast", "Beastfolk", "Celestial", "Construct", "Dragon","Dwarf","Elf","Elemental","Fey","Fiend", "Giant","Gnome","Goblin","Halfling","Kobold","Lizardfolk","Monstrosity","Ooze","Orc","Plant","Snakefolk","Undead"]:
        normal = 30
        
    base_speeds = {
        "Human": {      "Walk": 30},
        "Dwarf": {      "Walk": 25,                                                                                                 "Climb": Dizero(2) * 5},
        "Elf": {        "Walk": 30},
        "Halfling": {   "Walk": 25},
        "Aberration": { "Walk": Dizero(6) * 10, "Fly": Dizero(6) * 10,                                                              "Climb": Dizero(3) * 10},
        "Aven": {       "Walk": 30,             "Fly": Dizero(6) * 10},
        "Beast": {      "Walk": Dice(12)*10,    "Fly": Dizero(6) * 10,          "Swim": Dizero(4) * 10, "Burrow": Dizero(4) * 5,    "Climb": Dizero(3) * 10},  
        "Beastfolk": {  "Walk": Dice(8)*10,     "Fly": Dizero(3) * 10,          "Swim": Dizero(3) * 10, "Burrow": Dizero(2) * 5,    "Climb": Dizero(3) * 10},  
        "Celestial": {  "Walk": Dice(6) * 10,   "Fly": Dice(4) * Dice(2) * 10},  
        "Construct": {  "Walk": Dice(6) * 10,   "Fly": Dizero(2) * 10,          "Swim": Dizero(2) * 10, "Burrow": Dizero(2) * 5},
        "Dragon": {     "Walk": Dice(12) * 10,  "Fly": Dice(12) * 10,           "Swim": Dice(12) * 10,  "Burrow": Dizero(5) * 5,    "Climb": Dizero() * 5},  
        "Dwarf": {      "Walk": 25},
        "Elf": {        "Walk": 30,                                             "Swim": Dizero(3) * Dizero(3) * 5},
        "Elemental": {  "Walk": Dizero(6) * 10, "Fly": Dizero(6) * 10,          "Swim": Dizero(6) * 10, "Burrow": Dizero(6) * 5}, 
        "Fey": {        "Walk": Dice(6) * 10,   "Fly": Dizero(6) * 5},
        "Fiend": {      "Walk": Dice(6) * 10,   "Fly": Dizero(8) * 10,                                                              "Climb": Dizero(3) * 10},  
        "Giant": {      "Walk": Dice(6) * 20},
        "Gnome": {      "Walk": 25},
        "Goblin": {     "Walk": 30},
        "Halfling": {   "Walk": 25},
        "Kobold": {     "Walk": 30},
        "Lizardfolk": { "Walk": Dice(3) * Dice(3) * 10,                         "Swim": Dice(6) * 10,                               "Climb": Dizero(3) * 10},
        "Monstrosity": {"Walk": Dice(6) * 10,   "Fly": Dizero(6) * 5,           "Swim": Dice(6) * 10,                               "Climb": Dizero(3) * 10},
        "Ooze": {       "Walk": Dice(6) * 10,                                                                                       "Climb": Dice(6) * 10},  
        "Orc": {        "Walk": 30},
        "Plant":  {     "Walk": Dice(3) * 10,                                   "Swim": Dice(3) * 10,   "Burrow": Dice(3) * 5,      "Climb":  Dice(3) * 10},  
        "Snakefolk": {  "Walk": 30,                                             "Swim": Dizero(6) * 10,                             "Climb":  Dizero(3) * 5},  
        "Undead": {     "Walk": Dizero(12) * 5, "Fly": Dizero(6) * 5,           "Swim": Dizero(3) * 5,  "Burrow": Dizero(2) * 5},  
    }


    # Set default speeds to 0
    normal = base_speeds.get(race, {}).get("Walk", 0)
    fly = base_speeds.get(race, {}).get("Fly", 0)
    swim = base_speeds.get(race, {}).get("Swim", 0)
    burrow = base_speeds.get(race, {}).get("Burrow", 0)
    climb = base_speeds.get(race, {}).get("Climb", 0)
    

    if normal>=0:   movement += f"Walk: {normal}ft. \t"
    if fly>0:       movement += f"Fly: {fly}ft. \t"
    if swim>0:      movement += f"Swim: {swim}ft. \t"
    if burrow>0:    movement += f"Burrow: {burrow}ft. \t"
    if climb>0:     movement += f"Climb: {climb}ft. \t"

    # Additional Movement-related abilities
    if race in [ "Aberration", "Beast", "Beastfolk", "Construct", "Dragon","Fey","Fiend", "Lizardfolk","Monstrosity","Ooze","Plant","Snakefolk","Undead"]:
        if Dice()==1: extras += spider_climb

    if race in [ "Beast", "Beastfolk", "Dragon","Fey"]:
        if fly>0 and Dice() == 1: extras += flyby

    if race in [ "Aberration", "Beast", "Beastfolk","Gnome","Lizardfolk","Monstrosity"]:
        if Dice() == 1: extras += f"\n- Standing Leap. \n\t The {race}'s long jump is up to half his speed in feet and its high jump is up to third his speed, with or without a running start."

    if race in [ "Aberration", "Beast", "Beastfolk","Monstrosity","Fiend", "Lizardfolk","Ooze","Snakefolk","Undead"]:
        if Dice()==1:
            extras += f"\n- Spider Climb \n\t The {race} can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."
            if Dice() == 1:
                extras += f"\n- Web Sense \n\t While in contact with a web, the {race} knows the exact location of any other creature in contact with the same web."
            if Dice() == 1:
                extras += f"\n- Web Walker \n\t The {race} ignores movement restrictions caused by webbing."

    if race in [ "Beast", "Beastfolk", "Dragon","Fey"]:
        if Dice()==1: extras += f"\n- Hold Breath:\t The {race} can hold its breath for {Dice(3) * Dice(4) * 5} minutes."

    if race in [ "Aberration", "Beast", "Beastfolk", "Construct", "Dragon","Fiend", "Lizardfolk","Monstrosity","Plant","Snakefolk","Undead"]:
        if burrow > 0 and Dice()==1: extras += "\n - Tunneler: \t The {race} can burrow through solid rock at half its burrowing speed and leaves a 5 foot-wide, 8-foot-high tunnel in its wake."

    if race in ["Elemental"]:
        if burrow > 0 and Dice()==1: earth_glide


    movement += extras

    return movement

































def Resistances(npc):

    race = npc.race
    background = npc.background

    damage_types = [
        "acid", "bludgeoning", "cold", "fire", "force", 
        "lightning", "necrotic", "piercing", "poison", 
        "psychic", "radiant", "slashing", "thunder",
        "bludgeoning, piercing, and slashing from nonmagical attacks"

    ]
    race_damage_tendencies = {
        "Dragon": {
            "acid": {
                "Immune": 3, "Resistant": 6, "None": 3, "Vulnerable": 2},
            "bludgeoning": {
                "Immune": 1, "Resistant": 3, "None": 5, "Vulnerable": 1},
            "cold": {
                "Immune": 2, "Resistant": 5, "None": 2, "Vulnerable": 1},
            "fire": {
                "Immune": 2, "Resistant": 5, "None": 2, "Vulnerable": 1},
            "force": {
                "Immune": 1, "Resistant": 2, "None": 7, "Vulnerable": 0},
            "lightning": {
                "Immune": 2, "Resistant": 5, "None": 2, "Vulnerable": 1},
            "necrotic": {
                "Immune": 1, "Resistant": 3, "None": 4, "Vulnerable": 1},
            "piercing": {
                "Immune": 0, "Resistant": 2, "None": 7, "Vulnerable": 1},
            "poison": {
                "Immune": 2, "Resistant": 4, "None": 3, "Vulnerable": 1},
            "psychic": {
                "Immune": 1, "Resistant": 3, "None": 5, "Vulnerable": 1},
            "radiant": {
                "Immune": 1, "Resistant": 3, "None": 5, "Vulnerable": 1},
            "slashing": {
                "Immune": 0, "Resistant": 2, "None": 7, "Vulnerable": 1},
            "thunder": {
                "Immune": 1, "Resistant": 4, "None": 4, "Vulnerable": 1},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 0, "Resistant": 1, "None": 8, "Vulnerable": 1},
            },

        "Human": {
                "acid":{
                    "Immune": 0, "Resistant": 2, "None": 10, "Vulnerable": 2},
                "bludgeoning": {
                    "Immune": 1, "Resistant": 3, "None": 10, "Vulnerable": 2},
                "cold": {
                    "Immune": 1, "Resistant": 2, "None": 10, "Vulnerable": 2},
                "fire": {
                    "Immune": 1, "Resistant": 2, "None": 10, "Vulnerable": 2},
                "force": {
                    "Immune": 0, "Resistant": 2, "None": 10, "Vulnerable": 2},
                "lightning": {
                    "Immune": 1, "Resistant": 2, "None": 10, "Vulnerable": 2},
                "necrotic": {
                    "Immune": 1, "Resistant": 2, "None": 12, "Vulnerable": 3},
                "piercing": {
                    "Immune": 1, "Resistant": 3, "None": 12, "Vulnerable": 2},
                "poison": {
                    "Immune": 1, "Resistant": 3, "None": 12, "Vulnerable": 2},
                "psychic": {
                    "Immune": 1, "Resistant": 1, "None": 12, "Vulnerable": 2},
                "radiant": {
                    "Immune": 1, "Resistant": 1, "None": 12, "Vulnerable": 2},
                "slashing": {
                    "Immune": 1, "Resistant": 3, "None": 12, "Vulnerable": 2},
                "thunder": {
                    "Immune": 1, "Resistant": 3, "None": 12, "Vulnerable": 2},
                "bludgeoning, piercing, and slashing from nonmagical attacks": {
                    "Immune": 1, "Resistant": 2, "None": 12, "Vulnerable": 2},
                },
        "Aberration": {
                "acid": {"Immune": 2, "Resistant": 5, "None": 3, "Vulnerable": 0},
                "bludgeoning": {"Immune": 1, "Resistant": 4, "None": 4, "Vulnerable": 1},
                "cold": {"Immune": 2, "Resistant": 4, "None": 3, "Vulnerable": 1},
                "fire": {"Immune": 2, "Resistant": 3, "None": 4, "Vulnerable": 1},
                "force": {"Immune": 2, "Resistant": 5, "None": 3, "Vulnerable": 10},
                "lightning": {"Immune": 1, "Resistant": 4, "None": 4, "Vulnerable": 1},
                "necrotic": {"Immune": 5, "Resistant": 3, "None": 2, "Vulnerable": 0},
                "piercing": {"Immune": 1, "Resistant": 4, "None": 4, "Vulnerable": 1},
                "poison": {"Immune": 5, "Resistant": 3, "None": 2, "Vulnerable": 0},
                "psychic": {"Immune": 3, "Resistant": 5, "None": 2, "Vulnerable": 0},
                "radiant": {"Immune": 1, "Resistant": 2, "None": 4, "Vulnerable": 3},
                "slashing": {"Immune": 1, "Resistant": 4, "None": 4, "Vulnerable": 1},
                "thunder": {"Immune": 1, "Resistant": 4, "None": 4, "Vulnerable": 1},
                "bludgeoning, piercing, and slashing from nonmagical attacks": {
                    "Immune": 2, "Resistant": 6, "None": 2, "Vulnerable": 0},
                },
        "Aven": {
                "acid": {"Immune": 0, "Resistant": 2, "None": 7, "Vulnerable": 1},
                "bludgeoning": {"Immune": 0, "Resistant": 4, "None": 4, "Vulnerable": 2},
                "cold": {"Immune": 0, "Resistant": 2, "None": 5, "Vulnerable": 3},
                "fire": {"Immune": 0, "Resistant": 2, "None": 5, "Vulnerable": 3},
                "force": {"Immune": 0, "Resistant": 2, "None": 7, "Vulnerable": 1},
                "lightning": {"Immune": 0, "Resistant": 3, "None": 6, "Vulnerable": 1},
                "necrotic": {"Immune": 0, "Resistant": 2, "None": 6, "Vulnerable": 2},
                "piercing": {"Immune": 0, "Resistant": 3, "None": 4, "Vulnerable": 3},
                "poison": {"Immune": 0, "Resistant": 2, "None": 6, "Vulnerable": 2},
                "psychic": {"Immune": 0, "Resistant": 2, "None": 7, "Vulnerable": 1},
                "radiant": {"Immune": 0, "Resistant": 2, "None": 7, "Vulnerable": 1},
                "slashing": {"Immune": 0, "Resistant": 3, "None": 4, "Vulnerable": 3},
                "thunder": {"Immune": 0, "Resistant": 3, "None": 6, "Vulnerable": 1},
                "bludgeoning, piercing, and slashing from nonmagical attacks": {"Immune": 0, "Resistant": 2, "None": 8, "Vulnerable": 0},
                },
        "Beast": {
                "acid": {"Immune": 1, "Resistant": 3, "None": 6, "Vulnerable": 2},
                "bludgeoning": {"Immune": 2, "Resistant": 4, "None": 3, "Vulnerable": 3},
                "cold": {"Immune": 2, "Resistant": 4, "None": 4, "Vulnerable": 2},
                "fire": {"Immune": 1, "Resistant": 3, "None": 5, "Vulnerable": 3},
                "force": {"Immune": 1, "Resistant": 1, "None": 8, "Vulnerable": 2},
                "lightning": {"Immune": 2, "Resistant": 3, "None": 5, "Vulnerable": 2},
                "necrotic": {"Immune": 1, "Resistant": 2, "None": 6, "Vulnerable": 3},
                "piercing": {"Immune": 2, "Resistant": 4, "None": 3, "Vulnerable": 3},
                "poison": {"Immune": 3, "Resistant": 4, "None": 2, "Vulnerable": 3},
                "psychic": {"Immune": 1, "Resistant": 2, "None": 7, "Vulnerable": 2},
                "radiant": {"Immune": 1, "Resistant": 2, "None": 6, "Vulnerable": 3},
                "slashing": {"Immune": 2, "Resistant": 4, "None": 3, "Vulnerable": 3},
                "thunder": {"Immune": 2, "Resistant": 3, "None": 5, "Vulnerable": 2},
                "bludgeoning, piercing, and slashing from nonmagical attacks": {
                    "Immune": 4, "Resistant": 3, "None": 2, "Vulnerable": 3},
                },
        "Beastfolk": {
                "acid": {"Immune": 1, "Resistant": 4, "None": 6, "Vulnerable": 1},
                "bludgeoning": {"Immune": 2, "Resistant": 5, "None": 4, "Vulnerable": 1},
                "cold": {"Immune": 3, "Resistant": 5, "None": 3, "Vulnerable": 1},
                "fire": {"Immune": 2, "Resistant": 4, "None": 4, "Vulnerable": 2},
                "force": {"Immune": 1, "Resistant": 2, "None": 8, "Vulnerable": 1},
                "lightning": {"Immune": 2, "Resistant": 3, "None": 6, "Vulnerable": 1},
                "necrotic": {"Immune": 1, "Resistant": 2, "None": 7, "Vulnerable": 2},
                "piercing": {"Immune": 2, "Resistant": 5, "None": 4, "Vulnerable": 1},
                "poison": {"Immune": 4, "Resistant": 5, "None": 2, "Vulnerable": 1},
                "psychic": {"Immune": 1, "Resistant": 3, "None": 7, "Vulnerable": 1},
                "radiant": {"Immune": 1, "Resistant": 3, "None": 6, "Vulnerable": 2},
                "slashing": {"Immune": 2, "Resistant": 5, "None": 4, "Vulnerable": 1},
                "thunder": {"Immune": 3, "Resistant": 5, "None": 3, "Vulnerable": 1},
                "bludgeoning, piercing, and slashing from nonmagical attacks": {
                    "Immune": 4, "Resistant": 4, "None": 5, "Vulnerable": 1},
                "bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered": {
                    "Immune": 8, "Resistant": 4, "None": 4, "Vulnerable": 0},
                },

        "Celestial": {
                "acid": {
                    "Immune": 5, "Resistant": 7, "None": 3, "Vulnerable": 1},
                "bludgeoning": {
                    "Immune": 3, "Resistant": 8, "None": 4, "Vulnerable": 1},
                "cold": {
                    "Immune": 6, "Resistant": 7, "None": 3, "Vulnerable": 1},
                "fire": {
                    "Immune": 6, "Resistant": 6, "None": 3, "Vulnerable": 1},
                "force": {
                    "Immune": 6, "Resistant": 8, "None": 4, "Vulnerable": 1},
                "lightning": {
                    "Immune": 5, "Resistant": 8, "None": 4, "Vulnerable": 1},
                "necrotic": {
                    "Immune": 9, "Resistant": 5, "None": 3, "Vulnerable": 1},
                "piercing": {
                    "Immune": 3, "Resistant": 8, "None": 4, "Vulnerable": 1},
                "poison": {
                    "Immune": 9, "Resistant": 4, "None": 3, "Vulnerable": 1},
                "psychic": {
                    "Immune": 6, "Resistant": 6, "None": 3, "Vulnerable": 1},
                "radiant": {
                    "Immune": 11, "Resistant": 3, "None": 1, "Vulnerable": 1},
                "slashing": {
                    "Immune": 3, "Resistant": 8, "None": 4, "Vulnerable": 1},
                "thunder": {
                    "Immune": 5, "Resistant": 7, "None": 3, "Vulnerable": 1},
                "bludgeoning, piercing, and slashing from nonmagical attacks": {
                    "Immune": 6, "Resistant": 6, "None": 3, "Vulnerable": 1},
                "bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered": {
                    "Immune": 9, "Resistant": 5, "None": 5, "Vulnerable": 1},
                },
        "Construct": {
                "acid": {"Immune": 2, "Resistant": 5, "None": 4, "Vulnerable": 1},
                "bludgeoning": {"Immune": 0, "Resistant": 2, "None": 5, "Vulnerable": 5},
                "cold": {"Immune": 4, "Resistant": 4, "None": 4, "Vulnerable": 0},
                "fire": {"Immune": 1, "Resistant": 3, "None": 3, "Vulnerable": 5},
                "force": {"Immune": 0, "Resistant": 0, "None": 10, "Vulnerable": 2},
                "lightning": {"Immune": 5, "Resistant": 5, "None": 2, "Vulnerable": 0},
                "necrotic": {"Immune": 10, "Resistant": 0, "None": 2, "Vulnerable": 0},
                "piercing": {"Immune": 0, "Resistant": 2, "None": 5, "Vulnerable": 5},
                "poison": {"Immune": 10, "Resistant": 0, "None": 2, "Vulnerable": 0},
                "psychic": {"Immune": 10, "Resistant": 0, "None": 2, "Vulnerable": 0},
                "radiant": {"Immune": 0, "Resistant": 0, "None": 8, "Vulnerable": 4},
                "slashing": {"Immune": 0, "Resistant": 2, "None": 5, "Vulnerable": 5},
                "thunder": {"Immune": 2, "Resistant": 4, "None": 6, "Vulnerable": 0},
                "bludgeoning, piercing, and slashing from nonmagical attacks": {
                    "Immune": 3, "Resistant": 7, "None": 2, "Vulnerable": 0},
                },
        "Dwarf": {
            "acid": {"Immune": 0, "Resistant": 3, "None": 7, "Vulnerable": 0},
            "bludgeoning": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 0},
            "cold": {"Immune": 0, "Resistant": 3, "None": 7, "Vulnerable": 0},
            "fire": {"Immune": 0, "Resistant": 3, "None": 7, "Vulnerable": 0},
            "force": {"Immune": 0, "Resistant": 2, "None": 8, "Vulnerable": 0},
            "lightning": {"Immune": 0, "Resistant": 3, "None": 7, "Vulnerable": 0},
            "necrotic": {"Immune": 0, "Resistant": 1, "None": 8, "Vulnerable": 1},
            "piercing": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 0},
            "poison": {
                "Immune": 3, "Resistant": 7, "None": 0, "Vulnerable": 0},
            "psychic": {"Immune": 0, "Resistant": 2, "None": 8, "Vulnerable": 0},
            "radiant": {"Immune": 0, "Resistant": 2, "None": 8, "Vulnerable": 0},
            "slashing": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 0},
            "thunder": {"Immune": 0, "Resistant": 3, "None": 7, "Vulnerable": 0},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 0},
            },
        "Elf": {
            "acid": {"Immune": 1, "Resistant": 4, "None": 4, "Vulnerable": 1},
            "bludgeoning": {"Immune": 0, "Resistant": 3, "None": 6, "Vulnerable": 1},
            "cold": {"Immune": 1, "Resistant": 5, "None": 4, "Vulnerable": 0},
            "fire": {"Immune": 1, "Resistant": 5, "None": 4, "Vulnerable": 0},
            "force": {"Immune": 0, "Resistant": 4, "None": 6, "Vulnerable": 0},
            "lightning": {"Immune": 1, "Resistant": 4, "None": 4, "Vulnerable": 1},
            "necrotic": {"Immune": 1, "Resistant": 2, "None": 5, "Vulnerable": 2},
            "piercing": {"Immune": 0, "Resistant": 3, "None": 6, "Vulnerable": 1},
            "poison": {"Immune": 3, "Resistant": 5, "None": 2, "Vulnerable": 0},
            "psychic": {"Immune": 0, "Resistant": 3, "None": 7, "Vulnerable": 0},
            "radiant": {"Immune": 1, "Resistant": 3, "None": 5, "Vulnerable": 1},
            "slashing": {"Immune": 0, "Resistant": 3, "None": 6, "Vulnerable": 1},
            "thunder": {"Immune": 0, "Resistant": 3, "None": 6, "Vulnerable": 1},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 0, "Resistant": 2, "None": 8, "Vulnerable": 0},
            },
        "Elemental": {
            "acid": {
                "Immune": 5, "Resistant": 6, "None": 5, "Vulnerable": 5},
            "bludgeoning": {
                "Immune": 6, "Resistant": 6, "None": 6, "Vulnerable": 6},
            "cold": {
                "Immune": 6, "Resistant": 6, "None": 8, "Vulnerable": 7},
            "fire":{
                "Immune": 6, "Resistant": 6, "None": 6, "Vulnerable": 6},
            "force": {
                "Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 15},
            "lightning": {
                "Immune": 5, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "necrotic": {
                "Immune": 5, "Resistant": 5, "None": 10, "Vulnerable": 5},
            "piercing": {
                "Immune": 5, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "poison": {
                "Immune": 10, "Resistant": 5, "None": 0, "Vulnerable": 0},
            "psychic": {
                "Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 5},
            "radiant": {
                "Immune": 5, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "slashing": {
                "Immune": 5, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "thunder": {
                "Immune": 6, "Resistant": 6, "None": 7, "Vulnerable": 6},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 6, "Resistant": 7, "None": 10, "Vulnerable": 0},
            },
        "Fey": {
            "acid": {"Immune": 2, "Resistant": 8, "None": 5, "Vulnerable": 0},
            "bludgeoning": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "cold": {"Immune": 2, "Resistant": 8, "None": 5, "Vulnerable": 0},
            "fire": {"Immune": 2, "Resistant": 8, "None": 5, "Vulnerable": 0},
            "force": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "lightning": {"Immune": 2, "Resistant": 8, "None": 5, "Vulnerable": 0},
            "necrotic": {"Immune": 0, "Resistant": 2, "None": 2, "Vulnerable": 10},
            "piercing": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "poison": {"Immune": 10, "Resistant": 0, "None": 0, "Vulnerable": 0},
            "psychic": {"Immune": 2, "Resistant": 8, "None": 5, "Vulnerable": 0},
            "radiant": {"Immune": 0, "Resistant": 2, "None": 2, "Vulnerable": 10},
            "slashing": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "thunder": {"Immune": 2, "Resistant": 8, "None": 5, "Vulnerable": 0},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 0, "Resistant": 10, "None": 0, "Vulnerable": 0},
            },
        "Fiend": {
            "acid": {
                "Immune": 5, "Resistant": 10, "None": 0, "Vulnerable": 0},
            "bludgeoning": {
                "Immune": 0, "Resistant": 0, "None": 5, "Vulnerable": 0},
            "cold": {
                "Immune": 5, "Resistant": 10, "None": 0, "Vulnerable": 0},
            "fire": {
                "Immune": 10, "Resistant": 2, "None": 0, "Vulnerable": 0},
            "force": {
                "Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 0},
            "lightning": {
                "Immune": 5, "Resistant": 10, "None": 0, "Vulnerable": 0},
            "necrotic": {
                "Immune": 5, "Resistant": 0, "None": 5, "Vulnerable": 0},
            "piercing": {
                "Immune": 0, "Resistant": 0, "None": 5, "Vulnerable": 0},
            "poison": {
                "Immune": 15, "Resistant": 0, "None": 0, "Vulnerable": 0},
            "psychic": {
                "Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 0},
            "radiant": {
                "Immune": 0, "Resistant": 0, "None": 1, "Vulnerable": 20},
            "slashing": {
                "Immune": 0, "Resistant": 0, "None": 5, "Vulnerable": 0},
            "thunder": {
                "Immune": 5, "Resistant": 10, "None": 0, "Vulnerable": 0},
            "bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered": {
                "Immune": 8, "Resistant": 4, "None": 4, "Vulnerable": 0},
            },
        "Giant": {
            "acid": {
                "Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 5},
            "bludgeoning": {
                "Immune": 0, "Resistant": 10, "None": 5, "Vulnerable": 0},
            "cold": {
                "Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "fire": {
                "Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "force": {
                "Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "lightning": {
                "Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "necrotic": {"Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "piercing": {"Immune": 0, "Resistant": 10, "None": 5, "Vulnerable": 0},
            "poison": {"Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "psychic": {"Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "radiant": {"Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "slashing": {"Immune": 0, "Resistant": 10, "None": 5, "Vulnerable": 0},
            "thunder": {"Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 0, "Resistant": 10, "None": 5, "Vulnerable": 0},
            },
        "Gnome": {
            "acid": {"Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "bludgeoning": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "cold": {"Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "fire": {"Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "force": {"Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "lightning": {"Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "necrotic": {"Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "piercing": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "poison": {"Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "psychic": {"Immune": 0, "Resistant": 6, "None": 10, "Vulnerable": 0},
            "radiant": {"Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "slashing": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "thunder": {
                "Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            },
        "Goblin": {
            "acid": {
                "Immune": 0, "Resistant": 4, "None": 10, "Vulnerable": 5},
            "bludgeoning": {
                "Immune": 1, "Resistant": 4, "None": 18, "Vulnerable": 10},
            "cold": {
                "Immune": 2, "Resistant": 8, "None": 16, "Vulnerable": 4},
            "fire": {
                "Immune": 0, "Resistant": 4, "None": 8, "Vulnerable": 6},
            "force": {
                "Immune": 0, "Resistant": 1, "None": 10, "Vulnerable": 8},
            "lightning": {
                "Immune": 1, "Resistant": 7, "None": 12, "Vulnerable": 4},
            "necrotic": {
                "Immune": 1, "Resistant": 4, "None": 16, "Vulnerable": 8},
            "piercing": {
                "Immune": 1, "Resistant": 4, "None": 16, "Vulnerable": 8},
            "poison": {
                "Immune": 4, "Resistant": 8, "None": 6, "Vulnerable": 1},
            "psychic": {
                "Immune": 2, "Resistant": 4, "None": 16, "Vulnerable": 10},
            "radiant": {
                "Immune": 1, "Resistant": 2, "None": 20, "Vulnerable": 10},
            "slashing": {
                "Immune": 1, "Resistant": 4, "None": 12, "Vulnerable": 12},
            "thunder": {
                "Immune": 1, "Resistant": 10, "None": 16, "Vulnerable": 4},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 1, "Resistant": 1, "None": 20, "Vulnerable": 0},
            },
        "Halfling": {
            "acid": {"Immune": 1, "Resistant": 4, "None": 10, "Vulnerable": 0},
            "bludgeoning": {"Immune": 1, "Resistant": 6, "None": 8, "Vulnerable": 0},
            "cold": {"Immune": 1, "Resistant": 5, "None": 9, "Vulnerable": 0},
            "fire": {"Immune": 1, "Resistant": 5, "None": 9, "Vulnerable": 0},
            "force": {"Immune": 0, "Resistant": 2, "None": 13, "Vulnerable": 0},
            "lightning": {"Immune": 1, "Resistant": 5, "None": 9, "Vulnerable": 0},
            "necrotic": {"Immune": 0, "Resistant": 3, "None": 12, "Vulnerable": 0},
            "piercing": {"Immune": 1, "Resistant": 7, "None": 7, "Vulnerable": 0},
            "poison": {"Immune": 3, "Resistant": 10, "None": 2, "Vulnerable": 0},
            "psychic": {"Immune": 1, "Resistant": 5, "None": 9, "Vulnerable": 0},
            "radiant": {"Immune": 0, "Resistant": 3, "None": 12, "Vulnerable": 0},
            "slashing": {"Immune": 1, "Resistant": 7, "None": 7, "Vulnerable": 0},
            "thunder": {"Immune": 1, "Resistant": 5, "None": 9, "Vulnerable": 0},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            },
        "Kobold": {
            "acid": {"Immune": 1, "Resistant": 2, "None": 8, "Vulnerable": 4},
            "bludgeoning": {"Immune": 0, "Resistant": 1, "None": 6, "Vulnerable": 8},
            "cold": {"Immune": 1, "Resistant": 2, "None": 7, "Vulnerable": 5},
            "fire": {"Immune": 1, "Resistant": 2, "None": 7, "Vulnerable": 5},
            "force": {"Immune": 0, "Resistant": 1, "None": 10, "Vulnerable": 4},
            "lightning": {"Immune": 1, "Resistant": 2, "None": 8, "Vulnerable": 4},
            "necrotic": {"Immune": 0, "Resistant": 2, "None": 8, "Vulnerable": 5},
            "piercing": {"Immune": 0, "Resistant": 1, "None": 7, "Vulnerable": 7},
            "poison": {"Immune": 2, "Resistant": 3, "None": 7, "Vulnerable": 3},
            "psychic": {"Immune": 0, "Resistant": 1, "None": 9, "Vulnerable": 5},
            "radiant": {"Immune": 0, "Resistant": 1, "None": 9, "Vulnerable": 5},
            "slashing": {"Immune": 0, "Resistant": 1, "None": 7, "Vulnerable": 7},
            "thunder": {"Immune": 1, "Resistant": 2, "None": 7, "Vulnerable": 5},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 0, "Resistant": 2, "None": 5, "Vulnerable": 8},
            },
        "Lizardfolk": {
            "acid": {
                "Immune": 3, "Resistant": 6, "None": 9, "Vulnerable": 1},
            "bludgeoning": {
                "Immune": 2, "Resistant": 7, "None": 9, "Vulnerable": 1},
            "cold": {
                "Immune": 3, "Resistant": 6, "None": 10, "Vulnerable": 1},
            "fire": {
                "Immune": 2, "Resistant": 5, "None": 10, "Vulnerable": 3},
            "force": {
                "Immune": 0, "Resistant": 4, "None": 11, "Vulnerable": 4},
            "lightning": {
                "Immune": 2, "Resistant": 6, "None": 8, "Vulnerable": 3},
            "necrotic": {
                "Immune": 1, "Resistant": 4, "None": 10, "Vulnerable": 5},
            "piercing": {
                "Immune": 2, "Resistant": 10, "None": 7, "Vulnerable": 2},
            "poison": {
                "Immune": 6, "Resistant": 6, "None": 6, "Vulnerable": 1},
            "psychic": {
                "Immune": 2, "Resistant": 3, "None": 10, "Vulnerable": 6},
            "radiant": {
                "Immune": 1, "Resistant": 3, "None": 10, "Vulnerable": 6},
            "slashing": {
                "Immune": 2, "Resistant": 8, "None": 8, "Vulnerable": 3},
            "thunder": {
                "Immune": 2, "Resistant": 5, "None": 10, "Vulnerable": 3},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 4, "Resistant": 7, "None": 10, "Vulnerable": 1},
            },

        "Monstrosity": {
            "acid": {
                "Immune": 6, "Resistant": 6, "None": 6, "Vulnerable": 1},
            "bludgeoning": {
                "Immune": 3, "Resistant": 6, "None": 6, "Vulnerable": 4},
            "cold": {
                "Immune": 6, "Resistant": 6, "None": 6, "Vulnerable": 1},
            "fire": {
                "Immune": 6, "Resistant": 6, "None": 6, "Vulnerable": 1},
            "force": {
                "Immune": 3, "Resistant": 3, "None": 6, "Vulnerable": 6},
            "lightning": {
                "Immune": 6, "Resistant": 6, "None": 6, "Vulnerable": 1},
            "necrotic": {
                "Immune": 4, "Resistant": 4, "None": 6, "Vulnerable": 5},
            "piercing": {
                "Immune": 3, "Resistant": 6, "None": 6, "Vulnerable": 4},
            "poison": {
                "Immune": 6, "Resistant": 6, "None": 6, "Vulnerable": 1},
            "psychic": {
                "Immune": 4, "Resistant": 4, "None": 6, "Vulnerable": 5},
            "radiant": {
                "Immune": 3, "Resistant": 4, "None": 6, "Vulnerable": 6},
            "slashing": {
                "Immune": 3, "Resistant": 6, "None": 6, "Vulnerable": 4},
            "thunder": {
                "Immune": 6, "Resistant": 6, "None": 6, "Vulnerable": 1},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 6, "Resistant": 6, "None": 6, "Vulnerable": 1},
            },
        "Ooze": {
            "acid": {
                "Immune": 11, "Resistant": 1, "None": 6, "Vulnerable": 1},
            "bludgeoning": {
                "Immune": 11, "Resistant": 6, "None": 1, "Vulnerable": 1},
            "cold": {
                "Immune": 1, "Resistant": 6, "None": 6, "Vulnerable": 6},
            "fire": {
                "Immune": 1, "Resistant": 6, "None": 6, "Vulnerable": 6},
            "force": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "lightning": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "necrotic": {"Immune": 5, "Resistant": 5, "None": 5, "Vulnerable": 0},
            "piercing": {"Immune": 10, "Resistant": 5, "None": 0, "Vulnerable": 0},
            "poison": {"Immune": 10, "Resistant": 0, "None": 5, "Vulnerable": 0},
            "psychic": {"Immune": 10, "Resistant": 0, "None": 5, "Vulnerable": 0},
            "radiant": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "slashing": {"Immune": 10, "Resistant": 5, "None": 0, "Vulnerable": 0},
            "thunder": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 10, "Resistant": 0, "None": 0, "Vulnerable": 0},
            },
        "Orc": {
            "acid": {"Immune": 0, "Resistant": 3, "None": 7, "Vulnerable": 0},
            "bludgeoning": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 0},
            "cold": {
                "Immune": 0, "Resistant": 3, "None": 7, "Vulnerable": 0},
            "fire": {"Immune": 0, "Resistant": 3, "None": 7, "Vulnerable": 0},
            "force": {"Immune": 0, "Resistant": 2, "None": 8, "Vulnerable": 0},
            "lightning": {"Immune": 0, "Resistant": 3, "None": 7, "Vulnerable": 0},
            "necrotic": {"Immune": 0, "Resistant": 2, "None": 8, "Vulnerable": 0},
            "piercing": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 0},
            "poison": {"Immune": 1, "Resistant": 4, "None": 5, "Vulnerable": 0},
            "psychic": {"Immune": 0, "Resistant": 2, "None": 8, "Vulnerable": 0},
            "radiant": {"Immune": 0, "Resistant": 2, "None": 8, "Vulnerable": 0},
            "slashing": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 0},
            "thunder": {"Immune": 0, "Resistant": 3, "None": 7, "Vulnerable": 0},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 0},
            },
        
        "Plant": {
            "acid": {"Immune": 1, "Resistant": 5, "None": 4, "Vulnerable": 5},
            "bludgeoning": {
                "Immune": 0, "Resistant": 3, "None": 6, "Vulnerable": 7},
            "cold": {
                "Immune": 0, "Resistant": 3, "None": 6, "Vulnerable": 7},
            "fire": {
                "Immune": 1, "Resistant": 2, "None": 4, "Vulnerable": 16},
            "force": {"Immune": 0, "Resistant": 1, "None": 9, "Vulnerable": 5},
            "lightning": {"Immune": 1, "Resistant": 1, "None": 9, "Vulnerable": 5},
            "necrotic": {"Immune": 0, "Resistant": 1, "None": 4, "Vulnerable": 10},
            "piercing": {
                "Immune": 0, "Resistant": 6, "None": 5, "Vulnerable": 5},
            "poison": {"Immune": 11, "Resistant": 5, "None": 0, "Vulnerable": 0},
            "psychic": {"Immune": 5, "Resistant": 5, "None": 5, "Vulnerable": 0},
            "radiant": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "slashing": {"Immune": 0, "Resistant": 7, "None": 3, "Vulnerable": 5},
            "thunder": {"Immune": 0, "Resistant": 2, "None": 8, "Vulnerable": 5},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 0, "Resistant": 10, "None": 0, "Vulnerable": 0},
            },
        

        "Snakefolk": {
            "acid": {"Immune": 2, "Resistant": 5, "None": 7, "Vulnerable": 1},
            "bludgeoning": {"Immune": 1, "Resistant": 3, "None": 8, "Vulnerable": 3},
            "cold": {"Immune": 1, "Resistant": 3, "None": 7, "Vulnerable": 4},
            "fire": {"Immune": 2, "Resistant": 5, "None": 6, "Vulnerable": 2},
            "force": {"Immune": 1, "Resistant": 2, "None": 10, "Vulnerable": 2},
            "lightning": {"Immune": 1, "Resistant": 4, "None": 8, "Vulnerable": 2},
            "necrotic": {"Immune": 1, "Resistant": 3, "None": 8, "Vulnerable": 3},
            "piercing": {"Immune": 1, "Resistant": 8, "None": 6, "Vulnerable": 0},
            "poison": {"Immune": 10, "Resistant": 5, "None": 0, "Vulnerable": 0},
            "psychic": {"Immune": 1, "Resistant": 4, "None": 8, "Vulnerable": 2},
            "radiant": {"Immune": 0, "Resistant": 3, "None": 9, "Vulnerable": 3},
            "slashing": {"Immune": 1, "Resistant": 6, "None": 6, "Vulnerable": 2},
            "thunder": {"Immune": 1, "Resistant": 3, "None": 9, "Vulnerable": 2},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 1, "Resistant": 7, "None": 5, "Vulnerable": 2},
            },
        "Undead": {
            "acid": {
                "Immune": 2, "Resistant": 5, "None": 5, "Vulnerable": 3},
            "bludgeoning": {
                "Immune": 2, "Resistant": 6, "None": 6, "Vulnerable": 5},
            "cold": {
                "Immune": 5, "Resistant": 5, "None": 3, "Vulnerable": 2},
            "fire": {
                "Immune": 2, "Resistant": 5, "None": 6, "Vulnerable": 5},
            "force": {
                "Immune": 0, "Resistant": 3, "None": 9, "Vulnerable": 2},
            "lightning": {
                "Immune": 2, "Resistant": 4, "None": 7, "Vulnerable": 2},
            "necrotic": {
                "Immune": 10, "Resistant": 5, "None": 0, "Vulnerable": 0},
            "piercing": {
                "Immune": 2, "Resistant": 6, "None": 5, "Vulnerable": 2},
            "poison": {
                "Immune": 10, "Resistant": 5, "None": 0, "Vulnerable": 0},
            "psychic": {
                "Immune": 2, "Resistant": 3, "None": 5, "Vulnerable": 5},
            "radiant": {
                "Immune": 1, "Resistant": 2, "None": 3, "Vulnerable": 12},
            "slashing": {
                "Immune": 2, "Resistant": 6, "None": 5, "Vulnerable": 2},
            "thunder": {
                "Immune": 2, "Resistant": 5, "None": 6, "Vulnerable": 2},
            "bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered": {
                "Immune": 8, "Resistant": 4, "None": 4, "Vulnerable": 0},
            },


        }
            
    # Fetch the damage tendencies for the selected race, or use an empty dictionary if the race is not defined
    damage_tendencies = race_damage_tendencies.get(race, {})

    # Randomly determine resistances, immunities, and vulnerabilities based on the damage tendencies
    resistances = []
    immunities = []
    vulnerabilities = []
    for damage_type, tendencies in damage_tendencies.items():
        category = random.choices(list(tendencies.keys()), list(tendencies.values()))[0]
        if category == "Resistant":
            resistances.append(damage_type)
        elif category == "Immune":
            immunities.append(damage_type)
        elif category == "Vulnerable":
            vulnerabilities.append(damage_type)

            
    # Convert lists to strings
    resistances_str = "; ".join(resistances) if resistances else "None"
    immunities_str = "; ".join(immunities) if immunities else "None"
    vulnerabilities_str = "; ".join(vulnerabilities) if vulnerabilities else "None"

    # Compile the final string
    result = f" \nImmunities: {immunities_str}. \nResistances: {resistances_str}. \nVulnerabilities: {vulnerabilities_str}."
    return result



































def ConditionImmunities(npc):
    race=npc.race
    background=npc.background
    
    # Condition Immunities
    condition_immunities = []

    conditions = [
        "Blinded", "Charmed", "Deafened", "Frightened", "Grappled",
        "Incapacitated", "Paralyzed", "Petrified", "Poisoned", "Prone",
        "Restrained", "Stunned", "Unconscious"
    ]

    race_condition_immunities = {
"Human": {      "Blinded": 10,  "Charmed": 5,   "Deafened": 10,     "Frightened": 10/2,     "Grappled": 100,    "Incapacitated": 100,   "Paralyzed": 10/1,  "Petrified": 100,   "Poisoned": 10/3,   "Prone": 100,   "Restrained": 100,  "Stunned": 10,      "Unconscious": 100,},   
"Aberration": { "Blinded": 2,   "Charmed": 1,   "Deafened": 2,      "Frightened": 10/10,    "Grappled": 10/3,   "Incapacitated": 10/2,  "Paralyzed": 10/2,  "Petrified": 10/1,  "Poisoned": 10/4,   "Prone": 10/2,  "Restrained": 10/3, "Stunned": 10/3,    "Unconscious": 100,},
"Aven": {       "Blinded": 5,   "Charmed": 3,   "Deafened": 5,      "Frightened": 10/3,     "Grappled": 10,     "Incapacitated": 10,    "Paralyzed": 5,     "Petrified": 10,    "Poisoned": 5,      "Prone": 100,   "Restrained": 10,   "Stunned": 5,       "Unconscious": 100,},
"Beast": {      "Blinded": 3,   "Charmed": 10,  "Deafened": 3,      "Frightened": 10,       "Grappled": 2,      "Incapacitated": 10/1,  "Paralyzed": 10/2,  "Petrified": 10/2,  "Poisoned": 10/4,   "Prone": 10/3,  "Restrained": 10/4, "Stunned": 10/2,    "Unconscious": 100,},
"Beastfolk": {  "Blinded": 3,   "Charmed": 5,   "Deafened": 3,      "Frightened": 10/2,     "Grappled": 10/3,   "Incapacitated": 10/2,  "Paralyzed": 10/2,  "Petrified": 10/1,  "Poisoned": 10/3,   "Prone": 10/2,  "Restrained": 10/3, "Stunned": 10/2,    "Unconscious": 100,},
"Celestial": {  "Blinded": 5,   "Charmed": 1,   "Deafened": 5,      "Frightened": 1,        "Grappled": 10/3,   "Incapacitated": 10/3,  "Paralyzed": 3,     "Petrified": 10/2,  "Poisoned": 2,      "Prone": 5,     "Restrained": 3,    "Stunned": 5,       "Unconscious": 100,},
"Construct": {  "Blinded": 5,   "Charmed": 100, "Deafened": 100,    "Frightened":100,       "Grappled": 10/3,   "Incapacitated": 100,   "Paralyzed": 5,     "Petrified": 100,   "Poisoned": 100,    "Prone": 10/3,  "Restrained": 10/3, "Stunned": 100,     "Unconscious": 100,},
"Dragon": {     "Blinded": 3,   "Charmed": 2,   "Deafened": 2,      "Frightened": 10/7,     "Grappled": 10/5,   "Incapacitated": 10/2,  "Paralyzed": 10/2,  "Petrified": 10/2,  "Poisoned": 10/6,   "Prone": 10/3,  "Restrained": 10/4, "Stunned": 10/3,    "Unconscious": 100,},
"Dwarf": {      "Blinded": 5,   "Charmed": 3,   "Deafened": 5,      "Frightened": 10/2,     "Grappled": 10/3,   "Incapacitated": 10/2,  "Paralyzed": 10/2,  "Petrified": 10/2,  "Poisoned": 10/8,   "Prone": 10/2,  "Restrained": 10/3, "Stunned": 10/2,    "Unconscious": 100,},
"Elf":{         "Blinded": 3,   "Charmed": 2,   "Deafened": 3,      "Frightened": 10/3,     "Grappled": 10/3,   "Incapacitated": 10/3,  "Paralyzed": 10/3,  "Petrified": 5,     "Poisoned": 5/2,    "Prone": 10/3,  "Restrained": 10/3, "Stunned": 3/10,    "Unconscious": 100,},
"Elemental": {  "Blinded": 5,   "Charmed": 50,  "Deafened": 50,     "Frightened": 5,        "Grappled": 3,      "Incapacitated": 10,    "Paralyzed": 9,     "Petrified": 3,     "Poisoned": 3,      "Prone": 3,     "Restrained": 3,    "Stunned": 10,      "Unconscious": 9,},
"Fey":{         "Blinded": 5,   "Charmed": 2,   "Deafened": 5,      "Frightened": 10/5,     "Grappled": 10/3,   "Incapacitated": 10/4,  "Paralyzed": 10/3,  "Petrified": 10/1,  "Poisoned": 10/4,   "Prone": 10/2,  "Restrained": 10/3, "Stunned": 10/3,    "Unconscious": 100,},
"Fiend": {      "Blinded": 3,   "Charmed": 2,   "Deafened": 3,      "Frightened": 10/7,     "Grappled": 10/4,   "Incapacitated": 10/2,  "Paralyzed": 10/3,  "Petrified": 10/1,  "Poisoned": 10/6,   "Prone": 10/3,  "Restrained": 10/4, "Stunned": 10/3,    "Unconscious": 5,},
"Giant": {      "Blinded": 3,   "Charmed": 5,   "Deafened": 3,      "Frightened": 10/3,     "Grappled": 10/7,   "Incapacitated": 5,     "Paralyzed": 5,     "Petrified": 5,     "Poisoned": 3,      "Prone": 2,     "Restrained": 2,    "Stunned": 3,       "Unconscious": 100,},
"Gnome": {      "Blinded": 4,   "Charmed": 3,   "Deafened": 4,      "Frightened": 4,        "Grappled": 6,      "Incapacitated": 4,     "Paralyzed": 6,     "Petrified": 6,     "Poisoned": 4,      "Prone": 6,     "Restrained": 6,    "Stunned": 4,       "Unconscious": 100,},
"Goblin": {     "Blinded": 6,   "Charmed": 5,   "Deafened": 6,      "Frightened": 3,        "Grappled": 12,     "Incapacitated": 6,     "Paralyzed": 12,    "Petrified": 15,    "Poisoned": 6,      "Prone": 12,    "Restrained": 10,   "Stunned": 6,       "Unconscious": 101,},
"Halfling": {   "Blinded": 5,   "Charmed": 3,   "Deafened": 5,      "Frightened": 2,        "Grappled": 10,     "Incapacitated": 5,     "Paralyzed": 5,     "Petrified": 10,    "Poisoned": 3,      "Prone": 5,     "Restrained": 10,   "Stunned": 5,       "Unconscious": 100,},
"Kobold": {     "Blinded": 5,   "Charmed": 5,   "Deafened": 5,      "Frightened": 3,        "Grappled": 10,     "Incapacitated": 5,     "Paralyzed": 10,    "Petrified": 10,    "Poisoned": 5,      "Prone": 5,     "Restrained": 10,   "Stunned": 5,       "Unconscious": 100,},
"Lizardfolk": { "Blinded": 5,   "Charmed": 5,   "Deafened": 5,      "Frightened": 2,        "Grappled": 4,      "Incapacitated": 5,     "Paralyzed": 5,     "Petrified": 7,     "Poisoned": 2,      "Prone": 5,     "Restrained": 3,    "Stunned": 4,       "Unconscious": 100,},
"Monstrosity": {"Blinded": 3,   "Charmed": 5,   "Deafened": 3,      "Frightened": 5,        "Grappled": 2,      "Incapacitated": 3,     "Paralyzed": 3,     "Petrified": 3,     "Poisoned": 2,      "Prone": 2,     "Restrained": 2,    "Stunned": 3,       "Unconscious": 100,},
"Ooze": {       "Blinded": 1,   "Charmed": 1,   "Deafened": 100,    "Frightened": 1,        "Grappled": 100,    "Incapacitated": 2,     "Paralyzed": 2,     "Petrified": 2,     "Poisoned": 100,    "Prone": 100,   "Restrained": 100,  "Stunned": 2,       "Unconscious": 100,},
"Orc": {        "Blinded": 10,  "Charmed": 5,   "Deafened": 10,     "Frightened": 1.5,      "Grappled": 2,      "Incapacitated": 10,    "Paralyzed": 5,     "Petrified": 10,    "Poisoned": 3,      "Prone": 2,     "Restrained": 3,    "Stunned": 5,       "Unconscious": 100,},
"Plant": {      "Blinded": 100, "Charmed": 100, "Deafened": 100,    "Frightened": 100,      "Grappled": 1,      "Incapacitated": 2,     "Paralyzed": 10,    "Petrified": 5,     "Poisoned": 10,     "Prone": 100,   "Restrained": 1,    "Stunned": 10,      "Unconscious": 100,},
"Snakefolk": {  "Blinded": 5,   "Charmed": 2,   "Deafened": 5,      "Frightened": 3,        "Grappled": 3,      "Incapacitated": 5,     "Paralyzed": 10,    "Petrified": 10,    "Poisoned": 1.5,    "Prone": 5,     "Restrained": 5,    "Stunned": 10,      "Unconscious": 100,},
"Undead": {     "Blinded": 1,   "Charmed": 1,   "Deafened": 1,      "Frightened": 1,        "Grappled": 2,      "Incapacitated": 10,    "Paralyzed": 1,     "Petrified": 1,     "Poisoned": 1,      "Prone": 2,     "Restrained": 2,    "Stunned": 1,       "Unconscious": 5,}

    }



    if race in ["Elemental", "Undead"] and Dice() == 1:
        exhaustion = "Exhaustion, "
    else: exhaustion = ""

    # Fetch the condition immunities for the selected race, or use an empty dictionary if the race is not defined
    condition_immunity_weights = race_condition_immunities.get(race, {})

    # Randomly determine condition immunities based on the weights
    for condition, weight in condition_immunity_weights.items():
        if random.choices([True, False], [1/weight, 1 - (1/weight)])[0]:
            condition_immunities.append(condition)

    # Format the output
    if condition_immunities:
        return "Condition Immunities: " + exhaustion + ", ".join(condition_immunities)
    else:
        return "No condition immunities"




































def Extra_Defenses(npc):
    race= npc.race
    background= npc.background
    lvl = npc.level
    # Definitions of extra defenses
    acidic_blood = "\n- Acidic Blood: \n\t Any creature that hits the {} with a melee attack while within 5 feet of it takes 2d6 acid damage."
    alien_mind = "\n- Alien Mind: \n\t The {} has advantage on saving throws against being charmed or dominated."
    aberrant_ground = "\n- Aberrant Ground. \n\t  The ground in a 10-foot radius around the {} is doughlike difficult terrain. Each creature that starts its turn in that area must succeed on a DC 10 Strength saving throw or have its speed reduced to 0 until the start of its next turn.  "
    arcane_awareness = "\n- Arcane Awareness: \n\t The {} has advantage on Intelligence (Arcana) checks to recognize or recall information about spells or magical effects."
    berserker_resistance = "\n- Berserker Resistance: \n\t The {} has resistance to bludgeoning, piercing, and slashing damage."
    diabolic_resilience = "\n- Diabolic Resilience: \n\t The {} has resistance to bludgeoning, piercing, and slashing damage from non-magical attacks not made with silvered weapons."
    etherealness = "\n- Etherealness: \n\t The {} can shift partially into the Ethereal Plane, granting it resistance to non-magical attacks and the ability to move through solid objects until the end of their next turn."
    fey_ancestry = f"\n - Fey Ancestry \n\t The {race} has advantage on saving throws against being charmed, and magic can't put the {race} to sleep."
    hellish_rebuke = "\n- Hellish Rebuke: \n\t Once per turn, when the {} takes damage from a melee attack, it can cause flames to engulf its attacker, dealing fire 1d6 damage in return."
    infernal_wisdom = "\n- Infernal Wisdom: \n\t The {} has advantage on saving throws against being charmed or frightened."
    lore_preservation = "\n- Lore Preservation: \n\t Once per day, the {} can reroll a failed Intelligence check, taking the new roll."
    magic_resistance = "\n- Magic Resistance: \n\t The {} has advantage on saving throws against spells and other magical effects."
    mental_fortitude = "\n- Mental Fortitude: \n\t The {} has advantage on saving throws against being charmed or frightened."
    meticulous = "\n- Meticulous: \n\t The {} has advantage on Investigation checks when analyzing texts or searching for information."
    otherwordly_perception = "\n- Otherworldly Perception: \n\t The {} can sense the presence of invisible or hidden creatures within 60 feet of it."
    parry = "\n- Parry: \n\t The {} can add 2 to its AC against one melee attack that would hit it."
    psychic_feedback = "\n- Psychic Feedback: \n\t Any creature that attempts to read the {}'s thoughts or communicate telepathically with it takes 2d8 psychic damage."
    regeneration = "\n- Regeneration: \n\t The {} regains 10 hit points at the start of its turn if it has at least 1 hit point."
    relentless = f"\n - Relentless \n\t (Recharges after a Short or Long Rest). \n\t If the {race} takes {lvl} damage or less that would reduce it to 0 hit points, it is reduced to 1 hit point instead."
    telepathic_shield = "\n- Telepathic Shield: \n\t The {} has advantage on intelligence, wisdom, and charisma saving throws against spells and other magical effects that target its mind."
    spell_reflection = "\n- Spell Reflection. \n\t  If the {} makes a successful saving throw against a spell, or a spell attack misses it, the {} can choose another creature (including the spellcaster) it can see within 30 feet of it. The spell targets the chosen creature instead of the {}. If the spell forced a saving throw, the chosen creature makes its own save. If the spell was an attack, the attack roll is rerolled against the chosen creature"
    snow_camouflage = "\n- Snow Camouflage. \t The {} has advantage on Dexterity (Stealth) checks made to hide in snowy terrain."
    sure_footed = f"\n- Sure-Footed:\t The {race} has advantage on Strength and Dexterity saving throws made against effects that would knock it prone."
    shielded_mind = f"\n- Shielded Mind \t The {race} is immune to any effect that would sense its emotions, read its thoughts, or detect its location."
    nimble_scape = f"\n- Nimble Scape:\t The {race} can take the Disengage or Hide action as a bonus action on each of its turns."
    freeze = f"\n- Freeze: If the {race} takes cold damage, it partially freezes; All its speed is reduced by 20 feet until the end of its next turn."



    
    # Dictionary to store possible extra defenses for each race
    extra_defenses_race = {
        "Aberration": [shielded_mind, relentless,spell_reflection, aberrant_ground, magic_resistance, regeneration, telepathic_shield, otherwordly_perception, etherealness, acidic_blood, psychic_feedback, alien_mind],
        "Beast":[sure_footed],
        "Beastfolk": [fey_ancestry,sure_footed],
        "Celestial": [shielded_mind],
        "Construct": [magic_resistance],
        "Dragon":[magic_resistance],
        "Elf": [fey_ancestry],
        "Elemental":[freeze],
        "Fey": [nimble_scape],
        "Fiend": [ relentless,magic_resistance, regeneration, otherwordly_perception, etherealness, infernal_wisdom],
        "Goblin": [nimble_scape],
        "Lizardfolk":[freeze,relentless,regeneration],
        "Orc": [relentless],
        "Snakefolk":[],
    }

    # Dictionary to store possible extra defenses for each background
    extra_defenses_background = {
        "Noble": [parry],
        "Berserker": [relentless,berserker_resistance],
        "Scholar":[spell_reflection, arcane_awareness, mental_fortitude, lore_preservation, meticulous, shielded_mind],

        }

    # Fetch the extra defenses for the selected race and background
    possible_extra_defenses_race = extra_defenses_race.get(race, [])
    possible_extra_defenses_background = extra_defenses_background.get(background, [])

    # Combine race and background defenses
    possible_extra_defenses = possible_extra_defenses_race + possible_extra_defenses_background

    # Determine the number of defenses to select, this number can be changed as needed
    number_of_defenses_to_select = PB(lvl)  # for example

    # Randomly determine which extra defenses the character has
    if possible_extra_defenses and len(possible_extra_defenses) >= number_of_defenses_to_select:
        selected_defenses = random.sample(possible_extra_defenses, number_of_defenses_to_select)
        formatted_defenses = [defense.format(race) for defense in selected_defenses]
    else:
        formatted_defenses = [""]

    # Join the list of formatted defenses into a single string separated by newlines or any other separator
    formatted_defenses_string = '\n'.join(formatted_defenses)

    return formatted_defenses_string

def Extra_Weaknesses(npc):
    race= npc.race
    background= npc.background
    lvl = npc.level
    # Definitions of extra weaknesses
    freeze = f"\n- Freeze: If the {race} takes cold damage, it partially freezes; All its speed is reduced by 20 feet until the end of its next turn."



    
    # Dictionary to store possible extra weaknesses for each race
    extra_weaknesses_race = {
        "Aberration": [],
        "Beast":[],
        "Beastfolk": [],
        "Celestial": [],
        "Construct": [],
        "Dragon":[],
        "Elf": [],
        "Elemental":[freeze],
        "Fey": [],
        "Fiend": [freeze],
        "Goblin": [],
        "Lizardfolk":[freeze],
        "Orc": [],
        "Snakefolk":[freeze],
    }

    # Dictionary to store possible extra weaknesses for each background
    extra_weaknesses_background = {
        "Noble": [],
        "Berserker": [],
        "Scholar":[],

        }

    # Fetch the extra weaknesses for the selected race and background
    possible_extra_weaknesses_race = extra_weaknesses_race.get(race, [])
    possible_extra_weaknesses_background = extra_weaknesses_background.get(background, [])

    # Combine race and background weaknesses
    possible_extra_weaknesses = possible_extra_weaknesses_race + possible_extra_weaknesses_background

    # Determine the number of weaknesses to select, this number can be changed as needed
    number_of_weaknesses_to_select = PB(lvl)  # for example

    # Randomly determine which extra weaknesses the character has
    if possible_extra_weaknesses and len(possible_extra_weaknesses) >= number_of_weaknesses_to_select:
        selected_weaknesses = random.sample(possible_extra_weaknesses, number_of_weaknesses_to_select)
        formatted_weaknesses = [weaknesses.format(race) for weaknesses in selected_weaknesses]
    else:
        formatted_weaknesses = [""]

    # Join the list of formatted weaknesses into a single string separated by newlines or any other separator
    formatted_weaknesses_string = '\n'.join(formatted_weaknesses)

    return formatted_weaknesses_string






































def Martial_Skills(npc):
    race = npc.race
    background = npc.background
    lvl = npc.level
    
    # Definitions of extra martial skills
    blinding_spittle = f"\n- Blinding Spittle (Recharge 5–6). \n\t The {race} spits a chemical glob at a point it can see within 15 feet of it. The glob explodes in a blinding flash of light on impact. Each creature within 5 feet of the flash must succeed on a DC {10+PB(lvl)} Dexterity saving throw or be blinded until the end of the {race}'s next turn."
    body_thief = f"\n- Body Thief." + \
        f"\n\t The {race} initiates an Intelligence contest with an incapacitated humanoid within 5 feet of it that isn't protected by protection from evil and good." + \
        f"If it wins the contest, the {race}'s magically takes control of the target's body. " +\
        f"The {race} retains its Intelligence, Wisdom, and Charisma scores, as well as its understanding of any language, its senses, and its traits." +\
        f"It otherwise adopts the target's statistics. It knows everything the creature knew, including spells and languages." +\
        f"\n\t If the host body dies, the {race} must leave it. A protection from evil and good spell cast on the body drives the {race} out. " +\
        f"The {race} is also forced out if the target regains control by means of a wish. " +\
        f"By spending 5 feet of its movement, the {race} can voluntarily leave the body within 5 feet of it."
    devour_intellect = ( f"\n- Devour Intellect: \t The {race} targets one creature it can see within 10 feet of it that has a brain. "
                         f"The target must succeed on a DC {10+PB(lvl)} Intelligence saving throw against this magic or take 11 (2d10) psychic damage. "
                         "Also on a failure, roll 3d6: If the total equals or exceeds the target's Intelligence score, that score is reduced to 0. "
                         "The target is stunned until it regains at least one point of Intelligence.")

    amphibious = f"\n- Amphibious. \n\t The {race} can breathe air and water."
    invisible_passage = f"\n- Invisible Passage \n\t  The {race} magically turns invisible until they attack or cast a spell, or until their concentration ends (as if concentrating on a spell)." +\
                        "While invisible, they leave no physical evidence of their passage, so they can be tracked only by magic. Any equipment they wear or carry is invisible with them."
    gibbering = f"\n- Gibbering. \n\t The {race} babbles incoherently while it can see any creature and isn't incapacitated. " +\
                f"Each creature that starts its turn within 20 feet of the Aberration and can hear the gibbering must succeed on a DC {10+PB(lvl)} Wisdom saving throw. " +\
                "On a failure, the creature can't take reactions until the start of its next turn and rolls a d8 to determine what it does during its turn. " +\
                "On a 1 to 4, the creature does nothing. " +\
                "On a 5 or 6, the creature takes no action or bonus action and uses all its movement to move in a randomly determined direction. " +\
                "On a 7 or 8, the creature makes a melee attack against a randomly determined creature within its reach or does nothing if it can't make such an attack."
    tentacles= "\n- Tentacles. \n\t Reach 10 ft., one creature. Hit: 7 (1d10 + 2) piercing damage, and the target must succeed on a " +\
               f"DC {10+PB(lvl)} Constitution saving throw or be poisoned for 1 minute. The poisoned target is paralyzed, and it can repeat the saving throw at the" +\
               f" start of each of its turns, ending the effect on a success. \n\t The target is also grappled (escape DC {10+PB(lvl)}). If the target is Medium or " +\
               f"smaller, it is also restrained until this grapple ends. While grappling the target, the {race} has advantage on attack rolls against it and can 't "+\
               f"use this attack against other targets. When the {race} moves, any Medium or smaller target it is grappling moves with it."
    multiattack = random.choice([
        f"\n-Multiattack: The {race} makes two simple attacks.",
        f"\n-Multiattack: The {race} makes two simple melee attacks.",
        f"\n-Multiattack: The {race} makes three simple attacks.",
        f"\n-Multiattack (Two-Weapon Combat Style): The {race} makes two attacks with its main hand weapon and one with its offhand weapon.",
        f"\n-Multiattack (Rapid Shot): The {race} makes three ranged attacks, each with a -2 penalty to the attack roll.",
        f"\n-Multiattack (Sweeping Attack): The {race} makes a single attack against all enemies within reach."
        ])
    skewer = f"\n- Skewer:\t Once per turn, when the {race} makes a Melee attack and hits, the target takes an extra 10 (3d6) damage, and the {race} gains temporary hit points equal to the extra damage dealt."
    stench = f"\n- Stench:\t Any creature other than a {race} that starts its turn within 5 feet of the {race} must succeed on a DC {8+npc.proficiency_bonus + npc.ability_scores.con_mod} Constitution saving throw or be poisoned until the start of the creature's next turn. On a successful saving throw, the creature is immune to the stench of all Lizardfolk for 1 hour."
    blood_frenzy = f"\n- Blood Frenzy:\t The {race} has advantage on melee attack rolls against any creature that doesn't have all its hit points."
    reckless = f"\n-Reckless:\t At the start of its turn, the {background} can gain advantage on all melee weapon attack rolls during that turn, but attack rolls against it have advantage until the start of its next turn."
    martial_advantage = f"\n- Martial Advantage \n\t Once per turn, the {race} can deal an extra {npc.proficiency_bonus*3} ({npc.proficiency_bonus}d6) damage to a creature it hits with a weapon attack if that creature is within 5 feet of an ally of the {race} that isn't incapacitated."



    # Dictionary to store possible extra martial skills for each race
    extra_skills_race = {
        "Aberration": [reckless, blinding_spittle, body_thief, amphibious, gibbering, tentacles, multiattack, devour_intellect, stench],
        "Beast":[reckless, blood_frenzy, amphibious, multiattack,skewer, stench],
        "Beastfolk":[reckless, blood_frenzy, amphibious, multiattack],
        "Fey": [amphibious, invisible_passage, gibbering, multiattack],
        "Fiend":[skewer, stench, multiattack, blood_frenzy, reckless],
        "Lizardfolk": [skewer, stench, blood_frenzy, reckless],
        "Monstrosity":[blood_frenzy, reckless],
        "Plant": [body_thief, amphibious, tentacles, multiattack, devour_intellect, skewer],
        "Undead": [body_thief, invisible_passage, multiattack, devour_intellect,skewer, stench, blood_frenzy, reckless],
    }

    # Dictionary to store possible extra skills for each background
    extra_skills_background = {
        "Commoner": [reckless],
        "Berserker": [multiattack, blood_frenzy, reckless],
        "Noble": [multiattack],
        
    }

    # Fetch the extra skills for the selected race and background
    possible_extra_skills_race = extra_skills_race.get(race, [])
    possible_extra_skills_background = extra_skills_background.get(background, [])

    # Combine race and background defenses
    possible_extra_skills = list(set(possible_extra_skills_race + possible_extra_skills_background))

    # Determine the number of skills to select, this number can be changed as needed
    number_of_skills_to_select = Dice(npc.proficiency_bonus+1)  # for example, you can change this to what makes sense in your context

    # Randomly determine which extra skills the character has
    if possible_extra_skills and len(possible_extra_skills) >= number_of_skills_to_select:
        selected_skills = random.sample(possible_extra_skills, number_of_skills_to_select)
        formatted_skills = [skill.format(race=race, background=background) for skill in selected_skills]
    else:
        formatted_skills = []

    # Join the list of formatted skills into a single string separated by newlines or any other separator
    formatted_skills_string = '\n'.join(formatted_skills)

    return formatted_skills_string






































def Abilities(npc):
    """
    Generate abilities for a character based on its race and background.
    
    :param race: The character.
    :param background: The background of the character.
    :return: A string describing the character's abilities.
    """
    # Initialize variables
    race = npc.race
    background = npc.background
    lvl = npc.level
    
    Type = race

    r = ""

    r += Senses(npc) + "\n\n"
    r += Movement(npc) + "\n\n"
    r += Resistances(npc) + "\n"
    r += ConditionImmunities(npc) + "\n\n"
    r += Extra_Defenses(npc) + "\n\n"
    r += Martial_Skills(npc) + "\n\n"



    ## Skills
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

    if (Type == "Beast" or Type == "Beastfolk") and Dice(12) == 1:      r += "\n- Rampage. \n\t When the Beast reduces a creature to 0 hit points with a melee attack on its turn, the beast can take a bonus action to move up to half its speed and make a bite attack."
    if (Type == "Beast" or Type == "Beastfolk") and Dice(12) == 1:      r += "\n- Slippery. \n\t The beast has advantage on ability checks and saving throws made to escape a grapple."
    if (Type == "Beast" or Type == "Beastfolk") and Dice() == 1:        r += "\n- Sunlight Sensitivity.  \n\t While in sunlight, the beastfolk has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."

    if Type == "Beastfolk" and Dice() == 1:     r += "\n - Damage Immunities \n\t Bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered."
    if Type == "Beastfolk" and Dice() == 1:     r += "\n - Beast Telepathy \n\t The Beastfolk can magically command any animal it shares an affinity to within 120 feet of it, using a limited telepathy."
    if Type == "Beastfolk" and Dice() == 1:     r += "\n - Shapechanger \n\t The Beastfolk can use its action to polymorph into a specific Medium humanoid or a Beast-humanoid hybrid, or into its beast form. Other than its size, its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies."
    if Type == "Beastfolk" and Dice() == 1:     r += "\n - Pack Tactics \n\t The Beastfolk has advantage on an attack roll against a creature if at least one of the Beastfolk's allies is within 5 feet of the creature and the ally isn't incapacitated."
    if Type == "Beastfolk" and Dice() == 1:     r += "\n - Rampage.\n\t When the beastfolk reduces a creature to 0 hit points with a melee attack on its turn, the beastfolk can take a bonus action to move up to half its speed and make a bite attack."
    if Type == "Beastfolk" and Dice(8) == 1:    r += "\n - Wounded Fury \n\t While it has 10 hit points or fewer, the beastfolk has advantage on attack rolls. In addition, it deals an extra 7 (2d6) damage to any target it hits with a melee attack."
    if Type == "Beastfolk" and Dice() == 1:     r += "\n - Multiattack \n\t The Beastfolk can make two different simple attacks."
    if Type == "Beastfolk" and Dice(8) == 1:    r += "\n - Otherworldly Perception \n\t The Beastfolk can sense the presence of any creature within 30 feet of it that is invisible or on the Ethereal Plane. It can pinpoint such a creature that is moving."
    if Type == "Beastfolk" and Dice(8) == 1:    r += "\n - Reckless \n\t At the start of its turn, the berserker can gain advantage on all melee weapon attack rolls during that turn, but attack rolls against it have advantage until the start of its next turn."



    # CELESTIALS

    ## Strengths and Weaknesses
    if Type == "Celestial" and Dice() == 1:     r += "\n- Damage Resistances: \t Radiant."
    if Type == "Celestial" and Dice() == 1:     r += "\n- Damage Immunities: \t Psychic."
    if Type == "Celestial" and Dice() == 1:     r += "\n- Damage Immunities: \t Bludgeoning, Piercing, and slashing from nonmagical attacks."

    if Type == "Celestial" and Dice() == 1:     r += "\n- Magic Resistance: \t The Celestial's has advantage on saving throws against magical effects."
    if Type == "Celestial" and Dice() == 1:     r += "\n- Magic Weapons: \t The Celestial's attacks are magical."

    ## Actions
    if Type == "Celestial" and Dice() == 1:     r += "\n- Change Shape. \n\t The Celestial magically polymorphs into a humanoid or beast that has a challenge rating equal to or less than 4, or back into its true form. It reverts to its true form if it dies. Any equipment it is wearing or carrying is absorbed or borne by the new form (the celestial's choice). \n\t In a new form, the celestial retains its game statistics and ability to speak, but its AC, movement modes, Strength, Dexterity, and other actions are replaced by those of the new form, and it gains any statistics and capabilities (except class features, legendary actions, and lair actions) that the new form has but that it lacks. The Celestial can still use its special attacks."

    ## Combat skills
    if Type == "Celestial" and Dice() == 1:     r += "\n- Multiattack: \t The Celestial's can attack once with a Special Attack and once with a Simple Attack."


    # CRIMINALS
    if Type == "Criminal" and Dice() == 1:  r += "\n- Pack Tactics \n\t The Criminal has advantage on an attack roll against a creature if at least one of the Criminal's allies is within 5 feet of the creature and the ally isn't incapacitated."

    # CONSTRUCTS

    # Senses

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

    if Type == "Fey" and Dice() == 1:   r += "\n-Night Hag Items. \n\t A night hag carries two very rare magic items that she must craft for herself. If either object is lost, the night hag will go to great lengths to retrieve it, as creating a new tool takes time and effort. \n\t - Heartstone: This lustrous black gem allows a night hag to become ethereal while it is in her possession. The touch of a heartstone also cures any disease. Crafting a heartstone takes 30 days. \n\t -Soul Bag: When an evil humanoid dies as a result of a night hag's Nightmare Haunting, the hag catches the soul in this black sack made of stitched flesh. A soul bag can hold only one evil soul at a time, and only the night hag who crafted the bag can catch a soul with it. Crafting a soul bag takes 7 days and a humanoid sacrifice (whose flesh is used to make the bag)."

    # ELFS

    if Type == "Elf":
        if Dice(4) <= 3:
            r = r + "\n- Darkvision \n\t 60ft"
        else:
            r = r + "\n- Darkvision \n\t 120ft"
            r = r + "\n- Sunlight Sensitivity. \n\t While in sunlight, the Elf has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."


    # ELEMENTALS
    ## Movement


    if Type == "Elemental" and Dice() == 1: r += " Air Form. \n\t The elemental can enter a hostile creature's space and stop there. It can move through a space as narrow as 1 inch wide without squeezing."

    if Type == "Elemental" and Dice() == 1: r += " Water Form. \n\t The elemental can enter a hostile creature's space and stop there. It can move through a space as narrow as 1 inch wide without squeezing."

    ## Senses

    ## Strengths and Weaknesses



    ## Combat Skills
    if Type == "Elemental" and Dice() == 1:     r += "\n - Multiattack \n\t The elemental makes two simple attacks."
    elif Type == "Elemental" and Dice() == 1:   r += "\n - Multiattack \n\t The elemental makes three simple attacks."

    if Type == "Elemental" and Dice() == 1:
        r += "\n -Charge \n\t If the elemental moves at least 20 feet straight toward a target and then hits it with a simple attack on the same turn, the target takes an extra 7 (2d6) bludgeoning damage. If the target is a creature, it must succeed on a DC 16 Strength saving throw or be knocked prone."
        
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

    if Type == "Goblin" and Dice() == 1:    r += "\n- Brute \n\t A melee weapon deals one extra die of its damage when the Goblin hits with it (included in the attack)."
    if Type == "Goblin" and Dice() == 1:    r += "\n- Surprise Attack \n\t If the Goblin surprises a creature and hits it with an attack during the first round of combat, the target takes an extra 7 (2d6) damage from the attack."
    if Type == "Goblin" and Dice(8) == 1:   r += "\n- Redirect Attack (Reaction) \n\t When a creature the goblin can see targets it with an attack, the goblin chooses another goblin within 5 feet of it. The two goblins swap places, and the chosen goblin becomes the target instead."
    if Type == "Goblin" and Dice() == 1:    r += "\n- Multiattack \n\t The goblin makes two Simple Attacks attacks. The second attack has disadvantage."
    elif Type == "Goblin" and Dice() == 1:  r += "\n- Multiattack \n\t The goblin makes two Simple Attacks attacks."
    if Type == "Goblin" and Dice() == 1:    r += "\n- Heart of Hruggek \n\t The goblin has advantage on saving throws against being charmed, frightened, paralyzed, poisoned, stunned, or put to sleep."

    if Type == "Knight" and Dice() == 1:    r += "\n- Brave \n\t The knight has advantage on saving throws against being frightened."
    if Type == "Knight" and Dice() == 1:    r += "\n- Parry \n\t The knight adds 2 to its AC against one melee attack that would hit it. To do so, the knight must see the attacker and be wielding a melee weapon."

    # LIZARDFOLK


    
    # Strengths and weaknesses 
    if Type == "Lizardfolk":
        if Dice() == 1: r += "\n- Condition Immunities \t Frightened"

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
        
        if Dice() == 1:     r += "\n- Devil's Sight. \n\t Magical darkness doesn't impede the Fiend's darkvision."

    if Type == "Fiend" and Dice(12) == 1:   r += "\n- Keen Hearing and Smell. \n\t The fiend has advantage on Wisdom (Perception) checks that rely on hearing or smell."


    if Type == "Fiend" and Dice(10) == 1:
        r += "\n- Incorporeal Movement. \n\t The demon can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object."

    if Type == "Fiend" and Dice(10) == 1:
        r += "\n- Teleport. \n\t The fiend magically teleports, along with any equipment it is wearing or carrying, up to 60 feet to an unoccupied space it can see."


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
            

        if Dice() == 1:
            r += "\n- Keen Smell.\n\t The monstrosity has advantage on Wisdom (Perception) checks that rely on smell.\n"

    # Movement
        

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
    elif Type == "Undead" and Dice() == 1:      r += "\n- Damage Resistances: Piercing. "

    if Type == "Undead" and Dice() == 1:        r += "\n- Damage Resistances: Cold. "
    elif Type == "Undead" and Dice() == 1:      r += "\n- Damage Immunities: Cold "

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


def Legendary(race = Race(), background = Background(), lvl = 10):
    actions = []
    
    attack = f"\n- Attack \n\t The {race} can do one simple attack to any creature"
    move = f"\n- Move \n\t The {race} can move half their movement"
    shimmering_shield = f"\n- Shimmering Shield (Costs 2 Actions). The {race} creates a shimmering, magical field around itself or another creature it can see within 60 feet of it. The target gains a +2 bonus to AC until the end of the {race}'s next turn."
    heal_self = f"\n- Heal Self (Costs 3 Actions). \n\t The {race} magically regains {2*4+PB(lvl)} (2d8 + {PB(lvl)}) hit points."
    wing_attack = f"\n- Wing Attack (Costs 2 Actions): The {race} beats its wings. Each creature within 10 feet of the {race} must succeed on a DC {10+PB(lvl)}DEX saving throw or take {Dice(6, 2) + PB(lvl)} bludgeoning damage and be knocked prone."
    command_ally = f"\n- Command Ally: The {background} issues a command to one of its allies, allowing the ally to immediately take an extra action on the {background}'s turn."

    if race == "Celestial": actions += [attack, shimmering_shield, heal_self]

    if background == "Noble": actions += command_ally

    actions += [attack, move]

    num_actions = min(PB(lvl) // 2, len(actions))  # Simple example: 1 action per 5 levels

    selected_actions = random.sample(actions, num_actions) if actions else ["No legendary actions available."]
    return "\n".join(selected_actions)


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
        "I hope to bring prestige to a library.",
        "I hope to bring prestige to a museum.",
        "I hope to bring prestige to a university.",
        "I won't sell an art object that has historical significance.",
        "I won't sell an art object that is one of a kind.",
        "I won't sell a treasure that has historical significance.",
        "I won't sell a treasure that is one of a kind.",
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
        "My mistake got someone hurt. I'll never make that mistake again.",
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
        "Virtuous", "Principled", "Honorable", "Unprincipled", "Dishonorable",
        
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
        "I'm a hopeless romantic, always searching for that 'special someone'.",
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
        "I feel indebted to a witch for giving me a home and a purpose.",
        "I feel indebted to a fae for giving me a home and a purpose.",
        "I'm drawn to the Feywild and long to return there, if only for a short while.",
        "The Witchlight Carnival (Halloween) feels like home to me.",
        "I can't bring myself to harm a Fey creature, because I consider myself one.",
        "I can't bring myself to harm a Fey creature, I fear the repercussions.",
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


def Ideal(npc):

    background = npc.background
    alignment= npc.alignment
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
        "Nation. My city is all that matter.",
        "Nation. My nation, is all that matter.",
        "Nation. My people are all that matter.",
        "Aspiration. I'm going to prove that I'm worthy of a better life.",
        "Comfort. I want to ensure that me and mine enjoy the best things in life.",
        "Discovery. I want to learn all I can, both for my organization and for my own curiosity.",
        "Self-Knowledge. If you know yourself, there's nothing left to know.",
        "Live and Let Live. Meddling in the affairs of others only causes trouble.",
        "Power. Solitude and contemplation are paths toward mystical power.",
        "Power. Solitude and contemplation are paths toward magical power.",
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

def AbilityScoresGeneration(npc):

    rc = npc.race
    
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
            if Dice(4) == 1: INT += Dice(6)     # For engineering skills of tinkering.
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


class NPC:
    class AbilityScores:
        def __init__(self, STR, DEX, CON, INT, WIS, CHA):
            self.STR = STR
            self.DEX = DEX
            self.CON = CON
            self.INT = INT
            self.WIS = WIS
            self.CHA = CHA

        def mod(self, score):
            """Calculate the modifier for a given ability score."""
            return (score - 10) // 2
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
        
    def __init__(self, title, race, background, lvl=1):
        self.title = title
        self.race = race
        self.subrace = Monster(race)
        self.background = background
        self.gender = random.choice(["♀", "♂", "⚥", "⚬", "?", ""])
        self.name = Racial_Names(self)
        self.level = lvl
        self.proficiency_bonus = PB(lvl)
        self.alignment = self.Alignment()        
        self.ability_scores = self.generate_ability_scores()
        self.AC = self.generate_armor_class()
        self.HP = Dice( Dice()+ Dice(), self.level) + lvl*self.ability_scores.con_mod
        self.ideal = Ideal(self)
        self.saving_throws = ""         # Initialization
        self.generate_saving_throws()
        self.skills = ""                # Initialization
        self.generate_skills()  
        self.passive_perception = self.calculate_passive_perception()  # Initialize and set passive perception
        self.languages = Language(self)
        self.simple_attacks = self.generate_simple_attacks()  # Initialize simple attacks
        self.special_attack = self.generate_special_attack()  # Initialize special attack
        self.spellcasting_ability = ""
        self.spell_save_dc = None
        self.spell_attack_bonus = None
        self.generate_spellcasting_ability()  # Call the method to set the ability
        self.generate_spellcasting_info()
        self.spells = Magic(self)
        self.abilities = Abilities(self)
        
    def Alignment(self):
        Alignments = [
            "Lawful Good",          "Neutral Good",        "Chaotic Good",
            "Lawful Neutral",       "True Neutral",        "Chaotic Neutral",
            "Lawful Evil",          "Neutral Evil",        "Chaotic Evil",
            "Unaligned",            ""
            ]
        return random.choice(Alignments)

    def generate_ability_scores(self, method="Randomiced"):
        # Replace this with your actual ability score generation code.
        # Example ability score generation:
        if method == "Standard" or method == "Standard Array":
            scores = [15, 14, 13, 12, 10, 8]
            random.shuffle(scores)
            return NPC.AbilityScores(STR=scores[0], DEX=scores[1], CON=scores[2], INT=scores[3], WIS=scores[4], CHA=scores[5])
        if method == "" or method=="Randomiced":
            STR,DEX,CON,INT,WIS,CHA = AbilityScoresGeneration(self)
            return NPC.AbilityScores(STR=STR, DEX=DEX, CON=CON, INT=INT, WIS=WIS, CHA=CHA)
        else:
            return NPC.AbilityScores(STR=10, DEX=10, CON=10, INT=10, WIS=10, CHA=10)
        
    def generate_armor_class(self):
        AC = 10 + self.ability_scores.dex_mod+ Dice(self.proficiency_bonus)
        if Dice(10) == 1 or self.background == "Monk":       AC += self.ability_scores.dex_mod
        if Dice(10) == 1 or self.background == "Berserker":  AC += self.ability_scores.con_mod
        if AC > 18 + self.proficiency_bonus: AC  = 18 + self.proficiency_bonus
        return AC

    def generate_saving_throws(self):
        # Initialize a dictionary to keep track of saving throw bonuses
        saving_throws = {
            'STR': self.ability_scores.str_mod,
            'DEX': self.ability_scores.dex_mod,
            'CON': self.ability_scores.con_mod,
            'INT': self.ability_scores.int_mod,
            'WIS': self.ability_scores.wis_mod,
            'CHA': self.ability_scores.cha_mod,
        }
        
        # Initialize the string that will display the saving throws
        saving_throws_str = "Saving Throws: "
        
        # Ensure at least two saving throws are proficient
        while sum(1 for bonus in saving_throws.values() if bonus >= self.proficiency_bonus) < 2:
            for ability in saving_throws:
                if Dice(4) == 1:
                    saving_throws[ability] += self.proficiency_bonus
        
        # Format the saving throw string
        for ability, bonus in saving_throws.items():
            sign = '+' if bonus >= 0 else ''
            saving_throws_str += f"{ability}:{sign}{bonus}\t"
        
        # Set the attribute for saving throws
        self.saving_throws = saving_throws_str.strip()
    
    def generate_skills(self):
        # Dictionary to hold skill names associated with their respective abilities
        skills = {
            'Athletics': 'STR',
            'Acrobatics': 'DEX', 'Sleight of Hand': 'DEX', 'Stealth': 'DEX',
            'Arcana': 'INT', 'History': 'INT', 'Investigation': 'INT', 'Nature': 'INT', 'Religion': 'INT',
            'Animal Handling': 'WIS', 'Insight': 'WIS', 'Medicine': 'WIS', 'Perception': 'WIS', 'Survival': 'WIS',
            'Deception': 'CHA', 'Intimidation': 'CHA', 'Performance': 'CHA', 'Persuasion': 'CHA'
        }
        
        # Begin the skills string
        skills_str = "Skills:"

        # Iterate over the skills dictionary and add proficient skills based on a dice roll
        for skill, ability in skills.items():
            if Dice(8) <= getattr(self.ability_scores, ability.lower() + '_mod'):
                bonus = getattr(self.ability_scores, ability.lower() + '_mod') + self.proficiency_bonus
                sign = '+' if bonus >= 0 else ''
                skills_str += f"\n{skill}:{sign}{bonus}"

        # Set the attribute for skills
        self.skills = skills_str.strip()

    def calculate_passive_perception(self):
        # Base value of 10 plus the Perception skill bonus
        perception_mod = getattr(self.ability_scores, 'wis_mod')
        passive_perception = 10 + perception_mod
        
        # Check if the NPC is proficient in the Perception skill
        if 'Perception' in self.skills:
            passive_perception += self.proficiency_bonus

        return passive_perception

    def to_hit_bonus(self):
        # Assuming to hit is based on the higher of STR or DEX modifier
        highest_ability_mod = Modifier(max(self.ability_scores.STR,
                                      self.ability_scores.DEX))
        return highest_ability_mod + self.proficiency_bonus

    def generate_simple_attacks(self):
        attacks = "\n- SIMPLE ATTACKS:\n"
        num_weapons = Dice(3)
        for i in range(num_weapons):
            attacks += Attack(Dice(4), self)
            attacks += "\n"
        return attacks

    def generate_special_attack(self):
        # Assuming SpecialAttack is a function that returns a string description of the attack
        # and takes level, a modifier, STR, and DEX as arguments
        uses_per_combat = Dice(self.proficiency_bonus)
        chosen_ability_score = random.choice([
            self.ability_scores.STR, self.ability_scores.DEX, self.ability_scores.CON,
            self.ability_scores.INT, self.ability_scores.WIS, self.ability_scores.CHA
        ])
        modifier = Modifier(chosen_ability_score)
        return f"\n- SPECIAL ATTACK: {uses_per_combat} Uses per Combat\n" + \
               SpecialAttack(self)
    
    def generate_spellcasting_ability(self):
        # Find the highest modifier among INT, WIS, and CHA
        int_mod = self.ability_scores.int_mod
        wis_mod = self.ability_scores.wis_mod
        cha_mod = self.ability_scores.cha_mod

        # Create a dictionary to associate the ability score with its modifier
        ability_mod_dict = {'INT': int_mod, 'WIS': wis_mod, 'CHA': cha_mod}

        # Find the ability with the highest modifier
        self.spellcasting_ability = max(ability_mod_dict, key=ability_mod_dict.get)
        
    def calculate_spell_save_dc(self):
        ability_mod = getattr(self.ability_scores, f"{self.spellcasting_ability.lower()}_mod")
        self.spell_save_dc = 8 + ability_mod + self.proficiency_bonus

    def calculate_spell_attack_bonus(self):
        ability_mod = getattr(self.ability_scores, f"{self.spellcasting_ability.lower()}_mod")
        self.spell_attack_bonus = ability_mod + self.proficiency_bonus

    def generate_spellcasting_info(self):
        self.generate_spellcasting_ability()
        self.calculate_spell_save_dc()
        self.calculate_spell_attack_bonus()


        
def NPC_gen():
    """NPC creator"""

    npc = NPC(
        title = Title(),
        race = Race(),
        background = Background(),
        lvl = Dice(30)
        )

    bg = npc.background
    Lvl = npc.level
    
    rc = npc.race
    mn = npc.subrace
    


    STR, DEX, CON, INT, WIS, CHA = npc.ability_scores.STR, npc.ability_scores.DEX, npc.ability_scores.CON, npc.ability_scores.INT, npc.ability_scores.WIS, npc.ability_scores.CHA


    print(f"{npc.name}, {npc.title}")


    AC = npc.AC
    HP = npc.HP


    r = ""
    r += "- {} - ".format(npc.alignment) + npc.gender
    r += "\n"
    r += npc.background
    r += "\n"
    r += f"{npc.race}: {npc.subrace}"
    r += "\n"
    r += "\n"



    r += f"Lvl: {npc.level}⚜︎\t    HP: {npc.HP}♡\t    AC: {npc.AC}⛨️"
    r += ("\n\t" +
          f"STR: {npc.ability_scores.STR}  \t |  {Modifier(npc.ability_scores.STR)} \n\t" +
          f"DEX: {npc.ability_scores.DEX}  \t |  {Modifier(npc.ability_scores.DEX)} \n\t" +
          f"CON: {npc.ability_scores.CON}  \t |  {Modifier(npc.ability_scores.CON)} \n\t" +
          f"INT: {npc.ability_scores.INT}  \t |  {Modifier(npc.ability_scores.INT)} \n\t" +
          f"WIS: {npc.ability_scores.WIS}  \t |  {Modifier(npc.ability_scores.WIS)} \n\t" +
          f"CHA: {npc.ability_scores.CHA}  \t |  {Modifier(npc.ability_scores.CHA)} \n\t")
    r += "\n"

    r += (npc.saving_throws) + "\n\n"
    r += (npc.skills) + "\n"



    r += "\n"
    r += "Passive Perception: {}".format( npc.passive_perception)
    r += "\n"
    r += "Proficiency Bonus: +{}".format( npc.proficiency_bonus)
    r += "\n"

    r += "\n"
    r += "Languages: \n\t{}".format(npc.languages)
    r += "\n"
    r += "\n"
    
    r += "⫷   COMBAT ACTIONS:   ⫸"
    r += "\n"
    r += "\tTo hit: +{}".format( npc.to_hit_bonus())
    
    r += "\n" + npc.simple_attacks + "\n"
        
    r += f"\n {npc.special_attack}" 
    r += "\n\n"



    r += "༼ SPELLCASTING:\t{} ༽".format(npc.spellcasting_ability)
    r += "\n"
    r += "\t Spellsave DC {}".format(npc.spell_save_dc)
    r += "\n"
    r += "\t To hit: +{}".format(npc.spell_attack_bonus)
    r += "\n"
    r += npc.spells
        
        

    r += "\n"
    r += "\n⚔︎    SKILLS & ACCTIONS:   ⚔︎"
    r += "\n"
    r += npc.abilities
    r += "\n"

    if Dice(Lvl) >= 15:
        r += "\n✯    LEGENDARY ACTIONS:    ✯"
        r += "\n"
        r += f"The {npc.background} {rc} can take {Dice(PB(Lvl))} legendary actions, choosing from the options below. " +\
             f"\n\t Only one legendary action can be used at a time, and only at the end of another creature's turn. "+\
             f"\n\t The {npc.background} {rc} regains spent legendary actions at the start of its turn."
        r += "\n"
        r += Legendary(rc,bg,Lvl)
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
        r += f"The {npc.background} {rc} has an effect on its domains that may include any of the following magical effects:"
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
    s += npc.ideal
    s += "\n"
    s += " - Story Hook -"
    s += "\n"
    ph = PlotHook()
    s += ph


    try: 
        question = "Craft the presentation for a D&D NPC: "
        question += "\n Their real name is " + npc.name
        question += "\n They are known as " + npc.title
        question += "\n They are a " + npc.subrace + ", a kind of " + npc.race
        question += "\n Their alignment: " + npc.alignment
        question += "\n They are known for being a " + npc.background
        question += "\n They are" + tr1 + " They also are " + tr2
        question += "\n They follow the ideal of " + npc.ideal
        question += "\n Also, there's a problem related to the following Plot Hook: " + ph 
        question += "\n Suggest a creative problem that leads to a conflict with the group. This conflict must be specific and well defined, having a certain specific goal, but solvable in many different creative ways. The group of players should be able to adopt a possition of antagonists or allies. Expand details as necessary. One of the possible solutions must be martial, and one must be social."
        question += "\n Write it in the style of " + Style()
        question += "\n Write it in first person, as if he was introducing himself, and use three paragraphs of about 100 words each, expanding where appropiate. The first paragraph must contain information of their name and background. The second paragraph must express their ideals and goals. The third paragraph must explain why the player's characters may help or confront the NPC."  
        answer = ask_chatgpt(question)
        print(answer)
        print(s)
    except Exception as e:
        print(s)
        print(f"Encountered an error: {e}")

    
NPC_gen()
