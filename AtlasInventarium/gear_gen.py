import random




import random

class RandomItemGenerator:
    def __init__(self):
        self.type = random.choice(["Weapon", "Armor", "Potion", "Ring", "Wand", "Scroll", "Amulet", "Miscellaneous"])
        self.rarity = random.choice(["Common", "Uncommon", "Rare", "Very Rare", "Legendary", "Artifact"])
        self.feature = self.generate_feature() if self.rarity != "Common" else "No special feature"

    def generate_feature(self):
        features = {
            "Weapon": ["Flaming", "Frost", "Sharpness", "Life-Stealing", "Returning"],
            "Armor": ["Invisibility", "Invulnerability", "Resistance", "Etherealness", "Regeneration"],
            "Potion": ["Healing", "Giant Strength", "Invisibility", "Flying", "Heroism"],
            "Ring": ["Water Walking", "X-Ray Vision", "Invisibility", "Telekinesis", "Spell Storing"],
            "Wand": ["Fireballs", "Lightning Bolts", "Magic Missiles", "Web", "Paralysis"],
            "Scroll": ["Fireball", "Cure Wounds", "Teleport", "Raise Dead", "Time Stop"],
            "Amulet": ["Protection", "Health", "Proof against Detection", "Life Preservation", "Spell Reflection"],
            "Miscellaneous": ["Bag of Holding", "Flying Carpet", "Goggles of Night", "Helm of Comprehending Languages", "Deck of Many Things"]
        }
        return random.choice(features[self.type])

    def __str__(self):
        return f"Item Type: {self.type}\nRarity: {self.rarity}\nSpecial Feature: {self.feature}"

# Example usage:
random_item = RandomItemGenerator()
print(random_item)





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




gear = [
"Boots",
"Staff",
"Pendulum",
"Plate",
    ]

of = [
"Riot",
"Contamination",
"Storm",
"Strength",
"Cedar",
"the Magus",
"The Brawler",
    ]



def ItemName():

    name = f"{random.choice(gear)} of {random.choice(of)}"
    return name
