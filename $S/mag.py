import sys, re
sys.path.insert(0, "/Users/tbs/Desktop/DnD")
from AtlasActorLudi.Map_of_Character_Generation import summon_player
c = summon_player(seed=13, level=6, guild="Wizard")
txt = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", str(c.get_spellcaster())))
open(sys.argv[1], "w").write(txt[:700])
