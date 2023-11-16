import dnd
import npc_class as NPC
import random

def Dice(D=6,N=1):
    return dnd.Dice(D=D,N=N)


def Abilities(npc):
    """
    Generate abilities for a character based on its race and background.
    
    :param race: The character.
    :param background: The background of the character.
    :return: A string describing the character's abilities.
    """
    import senses
    import move
    import resistances
    import martial
    
    # Initialize variables
    race = npc.race
    background = npc.background
    lvl = npc.level
    
    Type = race

    r = ""

    r += senses.Senses(npc) + "\n\n"
    r += move.Movement(npc) + "\n\n"
    r += resistances.Resistances(npc) + "\n"
    r += resistances.ConditionImmunities(npc) + "\n\n"
    r += resistances.Extra_Defenses(npc) + "\n\n"
    r += martial.Skills(npc) + "\n\n"



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
    if Type == "Celestial" and Dice() == 1:     r += "\n- Multiattack: \t The {npc.race}'s can attack once with a Special Attack and once with a Simple Attack."


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
