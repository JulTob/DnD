import random

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
        "Rogue",
        "Scholar",
        "Soldier",
        "Shaman",
        "Spy",
        "Traveler",
        "Urchin",
        "Warrior",
        "Warlock",
        "Witch"
        ]
    return random.choice(Backgrounds)
