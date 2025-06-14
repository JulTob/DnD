DWARVEN_RUNES = [
    "ᚠ", "ᚢ", "ᚦ", "ᚨ", "ᚱ", "ᚷ", "ᚹ", "ᛋ", "ᛏ", "ᛒ", "ᛗ", "ᛚ",
    "ᛝ", "ᛟ", "ᛞ", "ᛖ", "ᚺ", "ᛉ", "ᛇ", "ᚾ", "ᚻ", "ᛃ", "ᛣ", "ᛜ",
    "ᚣ", "ᚤ", "ᚥ", "ᚦ", "ᚧ", "ᚨ","ᚡ", "ᚩ", "ᚪ", "ᚫ",
    "ᚬ","ᚭ","ᚮ","ᚯ","ᚰ","ᚱ","ᚲ","ᚳ","ᚴ","ᚵ",
    "ᚶ","ᚷ","ᚸ","ᚹ","ᚺ","ᚻ","ᚼ","ᚽ","ᚾ","ᚿ","ᛀ",
    "ᛁ", "ᛂ","ᛃ","ᛄ","ᛅ","ᛆ","ᛇ","ᛈ","ᛉ","ᛊ","ᛋ",
    "ᛌ","ᛍ","ᛎ","ᛏ","ᛐ","ᛑ","ᛒ","ᛓ","ᛔ","ᛕ","ᛖ",
    "ᛗ","ᛘ","ᛙ","ᛚ","ᛛ","ᛜ","ᛝ","ᛞ","ᛟ","ᛠ","ᛡ",
    "ᛢ","ᛣ","ᛤ","ᛥ","ᛦ","ᛧ","ᛨ","ᛩ","ᛪ","᛫","᛬","᛭",
    "ᛮ","ᛯ","ᛰ",
]
DWARVEN_DECORATORS = [
    # Technical and Forge-like
    "🜊","🜋","🜌","☩",
    "⛦", "⛥", "⛤",
    "♦","♢",
    "⏀","⏁","⏂","⏃","⏄","⏅",
    "⸏",
    "⧫", "⨀", "◇", "◆",
    "⚒", "⚙", "⛏", "☷", "☲",
    "⸔", "⸕",
    "☷","☶","☰","☱","☲","☳","☴","☵","⚌","⚍","⚎","⚏","⚊","⚋",
    "𐘥","𐣿",
]
COMBINE = [
        "⃠", "⃟","⃞", "⃝","⃤","⃣","⃘","⃭","⃬",
]


import random

def generate_dwarven_word(length=5):
    word = ""
    for _ in range(length):
        base = random.choice(DWARVEN_RUNES)
        base2 = random.choice(DWARVEN_RUNES)
        base3 = random.choice(DWARVEN_RUNES)
        deco = random.choice(DWARVEN_DECORATORS)

        word += base + base2 + base3 + deco
    return word

# Generate and print 5 dwarven words
for i in range(5):
    print(generate_dwarven_word())
