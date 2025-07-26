from ..Grimoire_of_Health  import roll_health, HIT_DIE_TABLE
from ..Codex_of_Progression import Progression

class Multiclass(Progression):
	def __init__(self, class1: Progression, level1: int, class2: Progression, level2: int):
		self.class1 = class1
		self.level1 = level1
		self.class2 = class2
		self.level2 = level2
