# QST-0122 — The backgrounds carry their settled text and Hooks again

- **Type:** repair / lore-fidelity
- **Priority:** 🟠 high
- **Status:** Working
- **Owner:** Claude, with Julio
- **Route to:** Julio
- **Parent:** —
- **Sidequests:** QST-0122.1 · QST-0122.2 · QST-0122.3 · QST-0122.4
- **Related:** `Documenta/Canon/Mythos/Backgrounds-Official.md` · Repairs-Ledger B17 · QST-0081 · QST-0091.4 · QST-0123

---

## 🔍 Diagnosis (what & where)

The sixteen official backgrounds were written and approved with Julio one at a
time (design session of 2026-07-30 to 2026-08-05; the Noble reworked on
2026-08-19, the Scribe on 2026-08-23). The 2026-08-29 wipe lost them. The
recovery (`3b34997`) left one-sentence stubs in `AtlasLusoris/BackgroundKit.py`:
no Hook, and in fifteen of them an old hook title printed where the
background's name belongs.

The same recovery dropped the machinery the settled design used: a Hook granted
as its own titled sheet entry, and a description filled when the sheet is read
(the Scribe's `{guild}`). The thirty-two custom backgrounds lost their separate
Hook the same way; their hook text survives glued to the description as
`roleplay`, with its title as a bold prefix.

On 2026-09-08 an analysis session read the stubs as the design and wrote sixteen
replacement drafts and an "institutional" principle into the Mythos page. Julio
never approved them ("this is not where we settled").

| Sidequest | What it restores |
|---|---|
| QST-0122.1 | The hook architecture: `hook` on a Background, its own sheet entry, slots filled on reading |
| QST-0122.2 | The sixteen officials' settled text, one commit per background |
| QST-0122.3 | The thirty-two custom backgrounds' Hooks as explicit entries, one commit per background |
| QST-0122.4 | The Mythos page and every page that repeated the withdrawn drafts |

## 🧾 Evidence

The settled text survives in
`.recovery-vault/_prewipe-pyc-mirror/AtlasLusoris/BackgroundKit.29bfd8e2057f.pyc`
(source saved 2026-08-26) and in the `BackgroundKit` section of
`.recovery-vault/AUTHORED-TEXT-ARCHIVE.md`; the two agree character for
character. Each background was traced to Julio's last approval in the design
session logs. The pre-wipe `Grimoire_of_Backgrounds` and `Map_of_*` bytecode
carry `hook: Entry | None` for the custom set.

## 🎯 Desired outcome

Every background prints its description under its own name and its Hook as a
separate titled entry, in the words Julio settled. The Mythos page is the
authority; the code adapts to it.

## 🧭 Notes for the Agora / implementer

- Julio, 2026-09-14: restore the settled backgrounds "as the authoritative and
  only form of them"; officials and custom both; one pull request per theme,
  each background its own commit and push, the architecture by itself.
- Julio, 2026-09-14: the Hermit's Hook says GM, as the Noble's does.
- Julio, 2026-09-14: *Somebody's Errand* was never his; the Wayfarer's Hook is
  *The Overlooked*.
- The officials and custom pull requests build on the architecture: merge .1
  first.
- When .2 and .3 are on `main`, close Backgrounds-Official §4 and
  Repairs-Ledger B17.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** before filling what looks like a gap in
  authored text, check `.recovery-vault` and the session logs: the text may
  already exist.

---

## 🏛️ Council

> Lorekeeper (Elf Sage): The words were already the project's, approved one by one. The work is to put them back, not to write them again.
> Repair Consul (Cleric): Two grants, as before the wipe: the life under the background's name, the Hook under its own title.

**Weighting:** reach ⟨3⟩ × severity ⟨2⟩ = **6** · council leaning: `build`
