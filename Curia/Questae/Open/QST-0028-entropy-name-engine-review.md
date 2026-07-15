# QST-0028 — Review and optimize the entropy name engine

- **Type:** refactor
- **Priority:** 🟡 normal
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Contracts (Warlock/Cleric), Simplicity (Monk)
- **Parent:** —
- **Sidequests:** —
- **Related:** AtlasNomina/Map_of_Word_Entropy.py · AtlasNomina/Map_of_Names.py

---

## 🔍 Diagnosis (what & where)
`entropify()` (`AtlasNomina/Map_of_Word_Entropy.py`) hung character generation indefinitely on seed 6: its `while True:` convergence loop had no iteration cap, and on a degenerate input (an empty-string name, produced by `NewWord`'s `"Mutate"` strategy chaining `increase_entropy` → `reduce_entropy` → `to_mean_entropy` in `Map_of_Names.py`) both `current_entropy` and `average_entropy` read as `0`, so the loop's own exit condition could never be satisfied. Patched directly (early-return on empty input + a 20-iteration cap) as an emergency stop — that patch is a backstop, not a design review.

The wider entropy-mutation system (`mutate_entropy`, `replace_symbol`, the three-mutation `"Mutate"` strategy in `NewWord`) has no contract on what a "valid" intermediate name looks like — nothing stops a name from shrinking to a handful of characters, or zero, mid-chain. The bounded retry (`MAX_ATTEMPTS**2` in `mutate_entropy`) caps *attempts*, not *degeneracy* of the input those attempts operate on.

## 🧾 Evidence
Traced live via Minion `@spy` wrapping (no source edits) — the hang's last call was `mutate_entropy(('', to_mean_entropy_fn, ['']), {})`, called from `NewWord` (`Map_of_Names.py:73`), itself called from `Character.New_name` during `summon_character(seed=6)`. Reproduced deterministically before the patch; fixed after (0.11s). Full sweep of 80 seeds afterward: 17.8s total, no seed over 2.6s.

## 🎯 Desired outcome
The entropy engine can't produce or propagate a degenerate (empty / near-empty) intermediate name at any step, by contract — not by a cap that happens to catch this one case. Ideally: a precondition on `mutate_entropy`/`entropify` that a name below some minimum length short-circuits immediately, and a look at whether `replace_symbol`'s substring-replacement can shrink a name unboundedly across chained calls in the first place.

## 🧭 Notes for the Agora / implementer
- Not urgent — the immediate hang is patched (see `Map_of_Word_Entropy.py::entropify`).
- Worth asking whether the whole entropy-mutation approach earns its complexity relative to `Syllabic`/`Markov`/`Choose` (the other `NewWord` strategies) — anti-bloat lens, not just a bug hunt.
- Self-tests: this module has none (`if __name__ == "__main__":`) — add one exercising degenerate/short-name input per Code-Style Canon.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council
*(not yet convened)*
