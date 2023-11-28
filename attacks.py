import npc_class
import random
import dnd

def Dice(D=6,N=1):
    return dnd.Dice(D=D,N=N)

def PB(level):
    return dnd.PB(level)

def Attack(npc):
    PB = npc.proficiency_bonus
    STR = npc.ability_scores.str_mod
    DEX = npc.ability_scores.dex_mod
    
    sign_str = '+' if STR >= 0 else ''
    sign_dex = '+' if DEX >= 0 else ''

    creature_type = npc.background + ' ' + npc.race + ' ' + npc.subrace
    
    SimpleMeleeWeapons = [
        f"Rock, {Dice(PB-1)}d6 {sign_str}{STR} Bludgeoning, 25/50 thrown",
        f"Fists, {Dice(PB-1)}d4 {sign_str}{STR} Bludgeoning",
        f"Brass Knuckles, {Dice(PB-1)}d4 {sign_str}{STR} Bludgeoning",
        f"Bite, {Dice(PB-1)}d4 {sign_str}{STR} Piercing",
        f"Bite, {Dice(PB-1)}d6 {sign_str}{STR} Piercing",
        f"Claws, {Dice(PB-1)}d4 {sign_str}{STR} Slashing",
        f"Claws, {Dice(PB-1)}d6 {sign_str}{STR} Slashing",
        f"Club, {Dice(PB-1)}d4 {sign_str}{STR} Bludgeoning",
        f"Dagger, {Dice(PB-1)}d4 {sign_str}{STR} Piercing, 20/60 thrown",
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

    
    if "Beast" in creature_type or "Dragon" in creature_type or "Kobold" in creature_type:
        SimpleMeleeWeapons += [
            f"\n- Bite, {Dice(PB-1)}d6 {sign_str}{STR} Piercing, and the target is grappled (escape DC {8+npc.ability_scores.str_mod+PB}). Until this grapple ends, the target is restrained, and the {npc.race} can't bite another target.",
            f"\n- Bite, {Dice(PB-1)}d10 {sign_str}{STR} Piercing.",
            ]
        
    SimpleRangedWeapons = [
        f"Rock, {Dice(PB-1)}d6 {sign_str}{STR} Bludgeoning, 25/50 thrown",
        f"Light Crossbow, {Dice(PB-1)}d8 {sign_dex}{DEX} Piercing, 80/320 range",
        f"Dart, {Dice(PB-1)}d4 {sign_dex}{DEX} Piercing, 20/60 range",
        f"Dart, {Dice(PB-1)}d4 {sign_str}{STR} Piercing, 20/60 range",
        f"Shortbow, {Dice(PB-1)}d6 {sign_dex}{DEX} Piercing, 80/320 range",
        f"Sling, {Dice(Dice(PB-1))}d4 {sign_dex}{DEX} Bludgeoning, 30/120 range",
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
    
    selection = SimpleMeleeWeapons + SimpleRangedWeapons

    if "Bandit" in creature_type:
        selection += MartialMeleeWeapons + MartialRangedWeapons

    if "Barbarian" in creature_type:
        selection += MartialMeleeWeapons + MartialRangedWeapons

    if "Berserker" in creature_type:
        selection += MartialMeleeWeapons + MartialRangedWeapons

    if "Cleric" in creature_type:
        selection += MartialMeleeWeapons

    if "Criminal" in creature_type:
        selection += MartialMeleeWeapons + MartialRangedWeapons

    if "Guard" in creature_type:
        selection += MartialMeleeWeapons + MartialRangedWeapons

    if "Hero" in creature_type:
        selection += MartialMeleeWeapons + MartialRangedWeapons

    if "Hunter" in creature_type:
        selection += MartialRangedWeapons

    if "Knight" in creature_type:
        selection += MartialMeleeWeapons

    if "Monk" in creature_type:
        selection += MartialMeleeWeapons + MartialRangedWeapons

    if "Noble" in creature_type:
        selection += MartialMeleeWeapons + MartialRangedWeapons

    if "Pirate" in creature_type:
        selection += MartialMeleeWeapons + MartialRangedWeapons

    if "Ranger" in creature_type:
        selection += MartialRangedWeapons

    if "Soldier" in creature_type:
        selection += MartialMeleeWeapons + MartialRangedWeapons

    if "Rogue" in creature_type:
        selection += MartialMeleeWeapons + MartialRangedWeapons

    if "Spy" in creature_type:
        selection += MartialMeleeWeapons + MartialRangedWeapons

    if "Warrior" in creature_type:
        selection += MartialMeleeWeapons + MartialRangedWeapons


    return random.choice(selection)




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
    r = f"Special Attack: {Dice(npc.PB())} use(s) per combat. \n\t"

    # Basic attack description    
    r += Attack(npc) + " +"

    # Damage calculation
    damage_die = random.choice(["d4", "d6", "d8", "d10"])
    r += "{}".format(Dice(1 + PB(Lvl)//4))
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

