# QST-0023 — Silent name fusions: implicit string concatenation across the Races

- **Type:** bug
- **Priority:** 🟡 normal
- **Status:** Open  *(renumbered 2026-07-07: first minted as 0021, which belongs to AtlasVenustas)*
- **Owner:** unclaimed
- **Route to:** Safety Consul (Paladin), Readability Consul (Barbarian), Lorekeeper
- **Parent:** —
- **Sidequests:** —
- **Related:** QST-0007 (diagnostic sweep) · the Races repair of 2026-07-07 (commit 35031e6)

---

## 🔍 Diagnosis (what & where)
Adjacent string literals with a missing comma fuse silently in Python:
`"Zephyr" "Grendel"` becomes the single name `"ZephyrGrendel"`. A tokenizer
sweep during the 2026-07-07 Races repair found **~60 such fusions** across
`AtlasNomina/Races/` — beyond the four files repaired that day. Worst
offenders: `Plant.py` (a dozen in one list), `Dwarf.py` (~10, including
phonotactic fragments like `'Arg' 'Aur'`), `Aven.py`, `Dragon.py`,
`Gnome.py`, `Halfling.py`, `Kobold.py`, `HumanLegacy.py`, `plantilla.py`.
Docstring-adjacent matches (Monstrosity/Plant/Undead line ~9-12) are
consecutive module docstrings — harmless, not part of this quest.

## 🧾 Evidence
Reproduce the sweep from the repo root:

```python
import tokenize, pathlib
for f in sorted(pathlib.Path('AtlasNomina/Races').glob('*.py')):
    toks = list(tokenize.tokenize(open(f, 'rb').readline))
    prev = None
    for t in toks:
        if t.type == tokenize.STRING and prev and prev.type == tokenize.STRING:
            print(f"{f}:{t.start[0]}", prev.string[:20], "+", t.string[:20])
        if t.type not in (tokenize.NL, tokenize.NEWLINE, tokenize.COMMENT,
                          tokenize.INDENT, tokenize.DEDENT):
            prev = t
```

Output on 2026-07-07: 65 hits (list preserved in the session log).

## 🎯 Desired outcome
Every name list yields the names its author typed: one comma restored per
fusion, no data lost, no dedup or reordering (duplicates may be deliberate
weighting). The sweep above returns only docstring pairs afterward.

## 🧭 Notes for the Agora / implementer
- Mechanical fix, but review each: a few fusions might be intentional
  (e.g. phonotactic fragments) — when in doubt, ask Julio.
- Do NOT reformat the files wholesale while fixing commas; one concern
  per commit.
- Consider adding the tokenizer sweep as a self-test or a recurring
  check under QST-0017 (orphan/health sweeps), so fusions cannot
  regrow unseen.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council
> Safety Consul (Paladin): A missing comma that silently changes data is the same disease as the silent import shim — the program runs, the output lies. The tokenizer makes the invisible visible; keep it.
> Readability Consul (Barbarian): Fix commas only. The temptation to reflow those giant lines belongs to another quest, with its own diff.

**Weighting:** reach 2 × severity 2 = **4** · council leaning: `build`
