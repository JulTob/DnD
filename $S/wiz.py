import sys, re, textwrap
sys.path.insert(0, "/Users/tbs/Desktop/DnD")
from AtlasActorLudi.Map_of_Character_Generation import summon_player
c = summon_player(seed=13, level=20, guild="Wizard")
WANT = ("Spellbook","Ritual Adept","Arcane Recovery","Scholar","Memorize Spell","Spell Mastery","Signature Spells")
feats = {f.name: f for f in c.features}
out = []
for n in WANT:
    f = feats.get(n)
    if not f: out.append(f"[{n}]  MISSING"); continue
    out.append(f"[{n}]")
    for part in str(f.description).replace("<br>", "\n").split("\n"):
        t = re.sub(r"<[^>]+>", "", part).strip()
        out.append(textwrap.fill(t, 72, initial_indent="   ", subsequent_indent="   "))
txt = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", str(c.get_spellcaster())))
out.append("\n[magic section, opening]")
out.append(textwrap.fill(txt[:330], 72, initial_indent="   ", subsequent_indent="   "))
open(sys.argv[1], "w").write("\n".join(out))
