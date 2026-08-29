# QST-0068 — Nine feats choose a casting ability before the scores exist

- **Type:** bug
- **Priority:** 🔴 urgent
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Technical Team
- **Related:** QST-0058 · `Documenta/Canon/Feature-Text.md` (an Entry is a projection)

---

## 🔍 Diagnosis (what & where)

`_pick_mental_casting_ability` (`Map_of_Official_Origin_Feats.py` ~line 532) is
documented as *"Choose Intelligence, Wisdom, or Charisma — prefer the
Character's strongest."* It never does.

	scores = getattr(char, "AS", None) or getattr(char, "abilities", None)
	if scores is None:
		return char.Pick(list(labels))

At the moment an Origin Feat awakens, **both `AS` and `abilities` are `None`**.
The preference branch is unreachable, and every call falls through to
`char.Pick(list(labels))` — an unweighted draw, taken from the **shared stream**
with no Dice Bag.

So the ability is neither the strongest nor stable, and the docstring describes
behaviour the function has never had.

**Nine feats call it**: lines 420, 740, 1043, 1339, 1389, 1676, 1718, 1816 and
the definition site.

## 🧾 Evidence

Reported from the app by Julio: a Goliath Wildkeeper Barbarian whose Wisdom is
higher than its Intelligence, with Wildwarden printing Intelligence.

	localhost:8000/#/20/Goliath/Wildkeeper/Barbarian/World_Tree/He/2504349135602673103

Reproduced across levels, so this is not an ASI-ordering artefact:

	lvl  INT  WIS  CHA  should be     printed
	1    11   13   11   Wisdom        Intelligence
	4    12   13   11   Wisdom        Intelligence
	12   12   14   11   Wisdom        Intelligence
	20   12   14   12   Wisdom        Intelligence

Instrumenting the call at awaken time:

	AS=None abilities=None

## 🎯 Desired outcome

The printed casting ability is the Character's strongest of Intelligence,
Wisdom and Charisma, decided against the **final** scores, stable across
renders, and off the shared stream.

## 🧭 Notes for the Agora / implementer

- **This is a pure read, not a decision.** `max()` over three scores involves no
  dice, so computing it when the sheet is *read* satisfies the purity invariant
  in `Feature-Text.md`: an Entry may read anything and must decide nothing.
  Late-binding is therefore the correct fix, not a workaround.
- All nine sites share one shape: `ability = _pick_mental_casting_ability(char)`
  at awaken, interpolated into a description string, handed to `grant`. The
  smallest correct change is to emit a slot in the text and resolve it in a
  callable description, since `grant` already accepts callables and `Feature`
  carries the subject.
- **Check whether the ability is also needed mechanically**, not only in prose.
  If the magic section or a spell record needs to know the casting ability for
  these spells, a read-time-only fix leaves that half unset, and the value must
  be recorded as well as printed.
- Do not "fix" this by keeping the draw and giving it a Dice Bag. A bagged draw
  would be stable but still ignores the scores, which is the actual complaint.
- Same family as the Barbarian save DC that printed two points low: a value
  resolved earlier than the state it depends on. Worth a sweep for other
  `getattr(char, "AS", None)` reads that happen during awaken.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Moved to Solved:** —

---

## ⚗️ Reward (separate dialog — do not fill during implementation)

- **Reward file:** *(pending distillation dialog)*
- **Distilled:** *(pending)*

---

## 🏛️ Council
*(unheard — routed, not yet convened)*

**Weighting:** reach ⟨2⟩ × severity ⟨3⟩ = **6** · council leaning: `build`
*(Reach 2: nine feats across several backgrounds. Severity 3: the sheet states
a casting ability that is wrong, and the draw is on the shared stream, which
the RNG refactor exists to eliminate.)*
