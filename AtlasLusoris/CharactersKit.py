"""

CharactersKit

Depends on:
	TOP Kit: Role Tags.

Contains:
	Character: shared skeleton (seed, dices, Roll/Dice, dummies)
	Role / Player / NonPlayer: Core role Tags

Seeds: repeatability between calls.
Dice: the Character's owned RNG (``dices`` bag; ``Roll`` / ``Dice`` draw).

NEVER CHANGE LOCKED CODE

Expected behaviour

For any character, with Role Tags, say charlie:
```
charlie = Character( name= "Charlie" )

Player(Charlie)
Wizard(Charlie)
Farmer(Charlie)

these should return true:
assert Player in Charlie
assert "wizard" in Charlie
assert "They" in Charlie

```



"""

from TagKit import Tag, Pre, Underlay


# ---------------------------------------------------------------------------
# Skeleton
# ---------------------------------------------------------------------------

class Character:
	"""Minimal shared substrate for every
	generated Player or NonPlayer Character.

	Stores dummies that role Tags resolve.
	All rolls go through Roll / Dice.

	"""

	def __init__(
			char,
			seed: int = 0,
			level: int = 1,
			):
		"""Constructs the Character skeleton.

		LOCKED SUBSTRATE
		This ``__init__`` is definitive.
		
		Do not change the parameters or the method body.
		Do NOT change a line of this code.

		Minimal method for optimal TOP compatibility
		"""
		from random import Random

		rng = Random()
		char.seed = int(
				seed if seed != 0 else rng.randint(0, 2**16)
				)
		char.dices = Random(char.seed)
			#-- Random Number Generator initialization.
		char.level = max(1, int(level))
		

	def __contains__(char, key):
		"""Sugar: True if key equals a stored characteristic (any type).

		Strings compare casefold
		Other keys use ``==`` 
		and membership in list/tuple/set values.
		
		Tags still own NAME probes via Role.
		@Underlay before this underlay runs.
		"""
		if isinstance(key, str):
			needle = key.casefold()
			if needle in {"character", "char"}:
				return True
		for name, value in vars(char).items():
			if name.startswith("_") or callable(value):
				continue
			if isinstance(key, str):
				if isinstance(value, str) and value.casefold() == needle:
					return True
				if isinstance(value, (list, tuple, set, frozenset)):
					for item in value:
						if isinstance(item, str) and item.casefold() == needle:
							return True
						if item == key:
							return True
			else:
				if value == key:
					return True
				if isinstance(value, (list, tuple, set, frozenset)) and key in value:
					return True
		if isinstance(key, type) and issubclass(key, Tag):
			return char in key   # Field membership — SPEC
		return False

	# --- Dice Methods ----------------------------------------------

	def Roll(
			char, 
			D: int = 6, 
			N: int = 1, 
			modifier: int = 0) -> int:
		"""	Roll N dice with D sides and add a modifier
			from the Character's Dice stream.
			-- Approved by Julio. Locked Substrate. -- 
			Do not change this code.
			"""
		if N < 1:
			N = 1
		total = 0
		for _ in range(N):
			if D >= 1:
				total += char.dices.randint(1, D)
			else:
				total += char.dices.randint(D, 1)
		return total + modifier

	# Alias used in Decree / Dialog prose
	Dice = Roll

	def __invert__(char):
		"""
		Reseed this Character's Dice from fixed seed.
		Sugar operator.
		Locked Substrate. Do not change this code.
		Usage: `~char` to "remix the Dice bag".
		"""
		char.dices.seed(char.seed)
		return char.seed

	def __le__(char, level: int):
		"""
		Level less than or equal to comparison.
		"""
		return char.level <= level
	
	def __ge__(char, level: int):
		"""
		Level greater than or equal to comparison.
		"""
		return char.level >= level

	def New_Score():
		rolls = [Dice(6) for _ in range(4)]
		return sum(sorted(rolls)[1:])

# ---------------------------------------------------------------------------
# Character Tags
# ---------------------------------------------------------------------------

class Role(Tag):
	"""
	Root tag for character roles.
	Locked Substrate. Do not change this code.
	"""
	NAME = "Role"

	@Pre
	def is_Character(target):
		"""
		Locked Precondition: 
		Only Character targets.
		"""
		return isinstance(target, Character)

	@Underlay
	def __contains__(agent, underlay, key):
		"""
		Membership by Tag NAME (casefold) or Tag-object Field check.
		Locked Substrate. Do not change this code.
		"""
		if isinstance(key, str):
			key = key.casefold()
			for tag in agent.Tags():
				name = getattr(tag, "NAME", "") or tag.__name__
				if name.casefold() == key:
					return True
		return underlay()
		#-- Underlay calls the previous instantiation of contains 
		#-- With the same parameters when empty
		

class Player(Role):
	"""
	Player-character role.

	"""
	NAME = "Player"

class NonPlayer(Role):
	"""
	Non Player Character role.

	"""
	NAME = "Non Player Character"

	@Underlay
	def __contains__(agent, underlay, key):
		"""
		Membership in NPC.
		"""
		if isinstance(key, str):
			key = key.casefold()
			if (key == "npc" 
				or key == "non player"):
					return True
			return False
		return underlay()



# ---------------------------------------------------------------------------
# Focused core suite — one _test_* per behaviour, all independent
# ---------------------------------------------------------------------------

def _test_rng_determinism():
	"""Seed fully determines the Dice stream; ``~char`` reseeds it."""
	a = Character(seed=42)
	b = Character(seed=42)
	seq = [a.Roll(20) for _ in range(5)]
	assert seq == [b.Roll(20) for _ in range(5)]   # same seed -> same stream
	assert all(1 <= x <= 20 for x in seq)
	assert isinstance(a.seed, int)
	assert (~a) == 42                               # reseed returns the seed
	assert [a.Roll(20) for _ in range(5)] == seq    # reseed replays the stream


def _test_roll_shape():
	"""Roll honours D / N / modifier; ``Dice`` is the alias."""
	assert Character.Dice is Character.Roll
	assert Character(seed=1).Roll(D=1, N=3) == 3    # D=1 is deterministic
	assert Character(seed=1).Roll(D=1, N=0) == 1    # N < 1 clamps to 1
	assert Character(seed=1).Roll(D=6, N=1, modifier=100) >= 101


def _test_level():
	"""Level clamps to >= 1 and compares through <= / >=."""
	assert Character(level=0).level == 1
	assert Character(level=3).level == 3
	c = Character(seed=1, level=2)
	assert c <= 2 and c >= 2
	assert c <= 3 and not (c <= 1)
	assert c >= 1 and not (c >= 3)


def _test_contains_core():
	"""Character.__contains__: sentinel, core fields, Tag-key -> Field."""
	z = Character(seed=7, level=1)
	assert "character" in z and "char" in z         # sentinel
	assert 7 in z and 1 in z                        # seed, level reachable
	assert "nonsense" not in z
	assert Player not in z                          # Tag key -> Field (untagged)


def _test_player_role_and_underlay():
	"""Role NAME overlay sits on top of the Character underlay."""
	hero = Character(seed=5, level=2)
	Player(hero)
	# Field membership, both directions
	assert hero in Player and hero in Role
	assert Player in hero and Role in hero
	# NAME probe hits the applied tag; a miss underlays to the Character
	assert "player" in hero                         # Player NAME (overlay)
	assert "character" in hero                       # NAME miss -> underlay -> sentinel
	assert "wizard" not in hero                      # NAME miss -> underlay -> False
	# NAME probe does not walk bases: "role" is not a NAME hit, even though
	# hero *is* in Role's Field (the ``Role in hero`` check above).
	assert "role" not in hero


def _test_is_character_contract():
	"""is_Character Pre rolls the whole tagging back for a non-Character.

	The stub must expose ``__contains__``; otherwise Role's @Underlay
	__contains__ raises TagResolutionError (no visible underlay) before the
	Pre can run.
	"""
	class NotACharacter:
		def __contains__(self, key):
			return False
	try:
		Player(NotACharacter())
	except Exception as err:
		assert type(err).__name__ == "TagPreconditionError", type(err).__name__
	else:
		raise AssertionError("Player must reject a non-Character")


def _test_spaced_name():
	"""A Role NAME with spaces is probed whole and casefold."""
	class Eldritch_Knight(Role):
		NAME = "Eldritch Knight"
	knight = Character(seed=7)
	Eldritch_Knight(knight)
	assert knight in Eldritch_Knight and knight in Role
	assert "eldritch knight" in knight and "Eldritch Knight" in knight
	assert "wizard" not in knight


def _test_nonplayer_short_circuit():
	"""NonPlayer answers its aliases and short-circuits every other string.

	Its @Underlay returns False on a string miss without calling underlay,
	so neither the sentinel nor its own spaced NAME leak through; non-string
	keys still underlay to the Field check.
	"""
	npc = Character(seed=3)
	NonPlayer(npc)
	assert "npc" in npc and "non player" in npc      # explicit aliases
	assert "character" not in npc                     # sentinel blocked
	assert "non player character" not in npc          # own NAME not probed
	assert "grog" not in npc
	assert npc in NonPlayer                            # Field
	assert NonPlayer in npc and Player not in npc      # non-str -> underlay -> Field


def _self_test():
	"""Run the focused core suite — each block is an independent _test_*."""
	_test_rng_determinism()
	_test_roll_shape()
	_test_level()
	_test_contains_core()
	_test_player_role_and_underlay()
	_test_is_character_contract()
	_test_spaced_name()
	_test_nonplayer_short_circuit()
	print("OK — CharactersKit self-test")


if __name__ == "__main__":
	try: 
		# Run as: PYTHONPATH=. python -m AtlasLusoris.CharactersKit
		import AtlasLusoris.CharactersKit as kit
		kit._self_test()
	except:
		_self_test()
