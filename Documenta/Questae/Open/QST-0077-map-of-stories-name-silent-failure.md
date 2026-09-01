# QST-0077 — `Map_of_Stories.Name()` silently failed on every character

- **Type:** bug / recovery
- **Priority:** 🟢 low (cosmetic — never crashed generation)
- **Status:** Solved
- **Owner:** Claude (Sonnet 5, main checkout)
- **Route to:** —
- **Parent:** QST-0072 (post-accident recovery)
- **Sidequests:** —
- **Related:** QST-0076 (proposes sweeping the rest of `.recovery-vault` for the same shape) · `AtlasEpica/Map_of_Stories.py`

---

## 🔍 Diagnosis (what & where)

`AtlasEpica/Map_of_Stories.py` is a bytecode-bootstrap file (loads compiled
`.pyc` from `.recovery-vault/epica/`, per QST-0072's recovery law). Its
`Name(hero)` function tried `hero._name` — a private attribute the
**pre-accident** Character carried — inside a bare `try/except Exception as
e: print(e)`, falling back to `FullName(hero)` on failure. The current
(post-TagKit-refactor) Character never has `._name`, so the try branch
failed on **every single call**, printing the exception to stdout as noise
on every character generated, before correctly falling through anyway.

## 🧾 Evidence

Confirmed by exact bytecode disassembly, not inference — `dis.dis` against
the live imported `Map_of_Stories.Name` showed the precise try/except shape
and its two branches:

```
def Name(hero):
    try:
        return hero._name
    except Exception as e:
        print(e)
        return FullName(hero)
```

`FullName(hero)` (same file) reads the current, real `hero.name` — correct,
unaffected. Reproduced live: 100% of characters across a 19-seed sweep
printed `"...Spellcasting has no Tag view '_name'"` before this fix; 0/19
after.

## 🎯 Desired outcome — met

`Name()` returns the same value it always fell through to, without the
detour through a dead attribute or the printed noise.

## 🧭 Notes for the Agora / implementer

The fix is minimal by design and does **not** touch the rest of this file
(several thousand lines, still bytecode-bootstrapped) — no certainty was
established beyond this one function. `Name`/`FullName`/`Title` were the
only three functions checked; the other ~130 files in `.recovery-vault` are
unswept — see QST-0076.

A wrinkle worth recording as practice: functions loaded from the vaulted
`.pyc` close over the **compiled body module's own globals**
(`AtlasEpica._bc_Map_of_Stories`), not the thin wrapper file's. Patching only
`Map_of_Stories.Name` in the wrapper is a no-op for anything the bytecode
calls internally (`Story`/`Script` still reached the old broken `Name`) —
the fix has to also land in `body.__dict__["Name"]`. Expect this for any
other fix inside a bytecode-bootstrap file.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** Julio, in chat, 2026-08-30 — "you can restore the file
  then, if you are certain" (after the fix and its disassembly evidence were
  reported, not applied silently)
- **What changed:** `AtlasEpica/Map_of_Stories.py` — `Name(hero)` now calls
  `FullName(hero)` directly, patched into both the wrapper module and the
  compiled body's `__dict__`. See the doc-comment on the fix itself.
- **Practice/preference to remember:** report a fix and its evidence before
  committing, even when certain — Julio confirms, the Questa records the
  confirmation. See QST-0076 for the reusable method (grep the bytecode
  shape → disassemble → confirm the fallback is always taken → patch both
  namespaces) before touching any other vaulted file.

---

## 🏛️ Council
*(not convened — narrow, disassembly-verified, single-function fix; Julio confirmed directly in chat)*
