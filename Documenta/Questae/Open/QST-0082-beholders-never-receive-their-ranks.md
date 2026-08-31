# QST-0082 — Beholders never receive their ranks

- **Type:** bug (pre-existing, preserved faithfully)
- **Priority:** 🟢 low (NonPlayer path, dark for the beta)
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Workshop
- **Parent:** QST-0072
- **Related:** Decree 0006 · QST-0075

---

## 🔍 Diagnosis (what & where)

`AtlasEpica/Map_of_Titles.py`, inside `Rank`: the Beholder branch reads

	if "Beholder" in genus:
		rank + ["Oculus", "Beholder", "Eye", "Watcher"]

A plain `+` whose result is discarded: the list never joins `rank`, so a
Beholder draws from the generic pool. Every sibling branch uses `+=`.

This is not a reconstruction slip. The vault bytecode compiles the same
discarded expression (`BINARY_OP +` followed by `POP_TOP`), so the bug is
authentic pre-wipe work, and the recovery reproduces it exactly per the
recovery law: restore first, improve in its own commit.

## 🎯 Desired outcome

One keystroke (`+` becomes `+=`) in the improvement phase, with a glance at
the surrounding branches for any sibling of the same slip.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council

> Workshop Consul (Artificer): The eye tyrant, of all creatures, denied its
> titles by a missing equals sign. The bytecode remembers even our lapses;
> that is exactly why we restore before we repair.

**Weighting:** reach 1 × severity 1 = **1** · council leaning: `build`
