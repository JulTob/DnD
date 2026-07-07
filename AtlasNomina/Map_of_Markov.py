# Markov baseline – Nothing fancy, just works
import random
from collections import defaultdict, Counter

class MarkovNameGenerator:
	"""
	Minimal tri-gram (order-3) Markov name generator.
	Usage:
		gen  = MarkovNameGenerator(training_names)
		name = gen.generate_name()
	"""

	def __init__(self, names, order: int = 4):
		self.order = order
		self.model = defaultdict(Counter)   # state -> {next_char: count}
		self.starts = []                    # states seen at word-start
		self._train([n.lower() for n in names if isinstance(n, str)])

	# ── training ────────────────────────────────────────────────
	def _train(self, names):
		for nm in names:
			padded = "^" * self.order + nm + "$"
			for i in range(len(padded) - self.order):
				state = padded[i : i + self.order]
				nxt   = padded[i + self.order]
				self.model[state][nxt] += 1
				if i == 0:
					self.starts.append(state)

	# ── helpers ────────────────────────────────────────────────
	def _weighted_pick(self, counter: Counter) -> str:
		chars, weights = zip(*counter.items())
		return random.choices(chars, weights=weights, k=1)[0]

	# ── public API ─────────────────────────────────────────────
	def generate_name(self, min_len=4, max_len=10, attempts=10) -> str:
		"""
		Make a new name.  Falls back to a random training name after
		<attempts> failed tries (too short / too long).
		"""
		for _ in range(attempts):
			state = random.choice(self.starts)
			out   = ""
			while True:
				nxt = self._weighted_pick(self.model[state])
				if nxt == "$":                    # reached end token
					if min_len <= len(out) <= max_len:
						return out.capitalize()
					break                         # length bad → retry
				out   += nxt
				state  = state[1:] + nxt
				if len(out) >= max_len:           # hard cap (safety)
					break
		# fallback
		return random.choice(self.starts).replace("^", "").capitalize()


def save_markov_as_py(gen: MarkovNameGenerator,
					race: str,
					folder: str = "Atlas_of_Markov") -> str:
	"""
	Persist <race>.py with three variables:
		order, chain, starting_states
	"""
	os.makedirs(folder, exist_ok=True)
	path = Path(folder) / f"{race}.py"
	with path.open("w", encoding="utf8") as f:
		f.write(f"# Auto-generated Markov model for {race}\n")
		f.write(f"order = {gen.order}\n")
		f.write(f"chain = {json.dumps({k: dict(c) for k,c in gen.model.items()})}\n")
		f.write(f"starting_states = {json.dumps(gen.starts)}\n")
	return str(path)


"""
Legacy

class MarkovNameGenerator:
	def __init__(self, names, order=random.randint(1, 6)):
		self.names = [name.lower() for name in names if isinstance(name, str)]
		self.order = order
		self.chain = defaultdict(Counter)
		self.starting_states = []
		self.populate_markov_chain()

	def ends_well(self, name):
		return (
			len(name) > 2
			and name[-1] in 'aeioulnrst'
			and not name.endswith(('kk', 'rr', 'zz'))
			)

	def populate_markov_chain(self):
		for name in self.names:
			padded_name = ('^' * self.order) + name + '$'
			for i in range(len(padded_name) - self.order):
				state = padded_name[i:i + self.order]
				next_char = padded_name[i + self.order]
				self.chain[state][next_char] += 1
				if i == 0:
					self.starting_states.append(state)

	def _weighted_random_choice(self, counter):
		choices, weights = zip(*counter.items())
		return random.choices(choices, weights=weights)[0]

	def generate_name(self, min_length=4, max_length=10, max_attempts=20):
		vowels = 'aeiou'
		consonants = 'bcdfghjklmnpqrstvwxyz'

		for attempt in range(max_attempts):
			state = random.choice(self.starting_states)
			name = ''
			consecutive_vowels = consecutive_consonants = 0

			while True:
				next_char = self._weighted_random_choice(self.chain[state])

				if next_char == '$':
					if min_length <= len(name) <= max_length:
						break  # Valid end
					else:
						# Too short, retry from start
						state = random.choice(self.starting_states)
						name = ''
						consecutive_vowels = consecutive_consonants = 0
						continue

				# Avoid triple repeating letters
				if len(name) >= 2 and next_char == name[-1] == name[-2]:
					continue

				# Enforce vowel/consonant balance
				if next_char in vowels:
					consecutive_vowels += 1
					consecutive_consonants = 0
					if consecutive_vowels > 2:
						continue
				elif next_char in consonants:
					consecutive_consonants += 1
					consecutive_vowels = 0
					if consecutive_consonants > 3:
						continue
				else:
					consecutive_vowels = consecutive_consonants = 0

				name += next_char
				state = state[1:] + next_char

				if len(name) >= max_length:
					break  # Forcefully truncate long names

			name = name.capitalize()
			if is_valid_name(name, "Markov"):
				return name

		# After max attempts, fallback to random choice
		fallback = random.choice(self.names).capitalize()
		return fallback
"""
