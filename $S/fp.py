import sys, hashlib
sys.path.insert(0, "/Users/tbs/Desktop/DnD")
from AtlasActorLudi.Map_of_Character_Generation import summon_player
ks = summon_player(seed=13, level=12, guild="Wizard").get_spellcaster().spells_known
key = "|".join(sorted(str(s.name) for s in ks))
open(sys.argv[1], "w").write("%s  levels=%s\n" % (
    hashlib.md5(key.encode()).hexdigest()[:12], sorted(s.level for s in ks)))
