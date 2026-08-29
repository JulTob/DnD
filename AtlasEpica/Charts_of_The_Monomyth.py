'''
Charts of The Monomyth — shared wave-function collapse for Epica prose.

Campbell's monomyth (The Hero with a Thousand Faces) as metaphor — here it is
the *DM Character* of a thousand faces: a Myth dict collapses by membership on a
host (DM Character / lusor / key-string). Villain, Quest Master, guardian, or
other roles are equally valid; the actuators do not assume evil. Stories,
Scenes, and Titles-adjacent Lodges reuse these actuators.

	If(host, conds)           # gate by membership / ANY / ALL / NOT / !Tag
	Choice(seq)               # collapse one option
	resolve(myth, host, key)  # literal collapse of (conds, value) into myth[key]
	render(template, myth, host)  # fill {tokens}

Tracked under QST-0037.16 — not the WorldBuild grid WFC kit.
'''

from __future__ import annotations

import random
import re

TOKEN = re.compile(r"{([a-zA-Z_][a-zA-Z0-9_]*)}")


def fail(tag: str, why: str):
	msg = f"[MythError] <{tag}>: {why}"
	print(msg)
	raise ValueError(msg)


def If(host, conds):
	"""
	Membership gate. Host may be a Tagged agent (`x in host`), a string of
	keys, or any object with __contains__.
	"""
	if conds == "" or conds is None:
		return True
	if isinstance(conds, str):
		if conds.startswith("!"):
			return conds[1:] not in host
		return conds in host
	if isinstance(conds, (tuple, list)):
		if not conds:
			return True
		first = conds[0]
		if first == "NOT" and len(conds) >= 2:
			rest = conds[1]
			if isinstance(rest, (tuple, list)):
				return all((tok not in host) for tok in rest)
			return str(rest) not in host
		if first == "ANY" and len(conds) >= 2:
			return any((tok in host) for tok in conds[1:])
		if first == "ALL" and len(conds) >= 2:
			return all((tok in host) for tok in conds[1:])
		for token in conds:
			if isinstance(token, str) and token.startswith("!"):
				if token[1:] in host:
					return False
			else:
				if token not in host:
					return False
		return True
	return False


def Choice(seq, rng: random.Random | None = None):
	if not seq:
		raise ValueError("Choice() called with an empty sequence.")
	picker = rng.choice if rng is not None else random.choice
	return picker(list(seq))


def Weighted_Choice(pairs, rng: random.Random | None = None):
	"""pairs: iterable of (value, weight)."""
	pairs = list(pairs)
	if not pairs:
		raise ValueError("Weighted_Choice() called with an empty sequence.")
	values = [v for v, _ in pairs]
	weights = [w for _, w in pairs]
	picker = rng.choices if rng is not None else random.choices
	return picker(values, weights=weights, k=1)[0]


def resolve(myth, host, key, rng: random.Random | None = None):
	"""
	Resolve a token from top-level Myth.
	- string: return as-is
	- list/tuple of (conds, value): pick among eligible, STORE back (literal collapse)
	"""
	if key not in myth:
		print(f"[MythWarn] <{key}>: missing token key in Myth")
		return ""

	val = myth[key]

	if isinstance(val, str):
		return val

	if isinstance(val, (list, tuple)):
		first = val[0] if val else None
		if isinstance(first, (list, tuple)):
			eligible = [v for conds, v in val if If(host, conds)]
			if not eligible:
				eligible = [v for conds, v in val if conds in ("", None)]
			if not eligible:
				print(f"[MythWarn] <{key}>: no eligible values for current host")
				return ""
			chosen = Choice(eligible, rng=rng)
			myth[key] = chosen
			return chosen if isinstance(chosen, str) else str(chosen)

	return str(val)


def render(template, myth, host, rng: random.Random | None = None):
	"""Replace {tokens} from Myth; a few passes for nested tokens."""
	if isinstance(template, (list, tuple)):
		if not template:
			fail("render", "empty template list")
		template = Choice(template, rng=rng)

	if not isinstance(template, str):
		template = str(template)

	text = template
	for _ in range(5):
		changed = False

		def repl(m):
			nonlocal changed
			k = m.group(1)
			val = resolve(myth, host, k, rng=rng)
			if val != "":
				changed = True
			return str(val) if val != "" else ""

		new_text = TOKEN.sub(repl, text)
		if not changed or new_text == text:
			text = new_text
			break
		text = new_text

	# Never leak a raw {placeholder}: strip any token that never resolved,
	# then tidy the whitespace/punctuation left where it was removed.
	if TOKEN.search(text):
		text = TOKEN.sub("", text)
		text = re.sub(r"[ \t]{2,}", " ", text)
		text = re.sub(r"[ \t]+([.,;:!?])", r"\1", text)
	return text


def eligible_values(spec, host):
	"""
	From a list of (conds, value) or (conds, value, weight), return eligible
	(value, weight) pairs. Weight defaults to 1.
	"""
	hits = []
	for row in spec:
		if len(row) == 2:
			conds, value = row
			weight = 1
		else:
			conds, value, weight = row[0], row[1], row[2]
		if If(host, conds):
			hits.append((value, weight))
	if not hits:
		hits = [(v, w if len(row) > 2 else 1) for row in spec for v, w in [
			(row[1], row[2] if len(row) > 2 else 1)
		] if row[0] in ("", None)]
	return hits


if __name__ == "__main__":
	host = "Elf Druid Forest"
	assert If(host, "Druid")
	assert If(host, ("ANY", "Wizard", "Druid"))
	assert not If(host, "Vampire")
	assert If(host, "!Vampire")

	myth = {
		"place": [
			(("ANY", "Druid", "Ranger"), "a mossy circle"),
			(("Criminal",), "a dockside den"),
			("", "a forgotten room"),
		],
		"line": "They wait in {place}.",
	}
	rng = random.Random(1)
	text = render("{line}", myth, host, rng=rng)
	assert "mossy circle" in text
	assert myth["place"] == "a mossy circle"  # collapsed

	print("AtlasEpica.Charts_of_The_Monomyth self-test OK")
	print(text)
