# QST-0043 — Suggest to TagKit: Guide the Label / string-probe contract

- **Type:** tagkit-upstream
- **Priority:** 🔴 urgent *(tagkit-upstream)*
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Wizard, Warlock, Lorekeeper, Druid → TagKit upstream
- **Parent:** —
- **Sidequests:** —
- **Related:** TagKit-Doctrine · CONFORMANCE.md · `Tag.Label` / `Tagged.__contains__` · CharactersKit Role membership sugar · SpellsKit string probes

---

## 🔍 Diagnosis (what & where)
TagKit’s Python implementation exposes human-readable Tag labels and string membership probes that the TOP Guide / SPEC do **not** name as paradigm obligations:

1. **`Tag.NAME` / `Tag.DESCRIPTION`** — `ClassVar` metadata on the Tag class.
2. **`Tag.Label()`** — returns `NAME or __name__`.
3. **String probe** — `"Evocation" in agent` / `"Eldritch Knight" in agent` via `Tagged.__contains__`, comparing `tag.Label().casefold()` against the probe.

Downstream (this project) wants display names with spaces (`NAME = "Eldritch Knight"`) and explicit, pin-stable membership sugar. Today that behavior is **Kit surface, not Guide law**. CONFORMANCE lists `agent in Tag` (Tag object), Fields, Overlay, contracts — it does **not** list string-by-Label probes. A conformant TagKit could drop or change the string probe and remain “TOP Verified.”

## 🧾 Evidence
- Pinned TagKit: `Tag.Label()` → `NAME or __name__`; `Tagged.__contains__` string branch uses `Label().casefold()`.
- Upstream `spec/SPECIFICATION.md` / `CONFORMANCE.md`: no obligation for `Label`, `NAME`, or string probes (search of SPEC for Label/string-probe obligations: absent).
- Local Doctrine: TagKit is settled upstream; gaps become **"Suggest to TagKit"** quests, never a local fork.
- Project choice (2026-07-21): do **not** load-bear on Kit string sugar alone — own an explicit name→Tag map and resolve to SPEC membership (`agent in Tag`). Still want the Guide/Kit gap closed so future pins don’t surprise consumers.

## 🎯 Desired outcome
Upstream decides and documents one of:

1. **Promote** — SPEC/CONFORMANCE (and Guide prose) state that string probes against `Label()` (and/or `NAME`) are part of the membership contract, with clear semantics (casefold, spaces, Base closure or not); **or**
2. **Demote** — Guide/Kit docs mark `NAME`/`Label`/string `in` as **Python TagKit convenience only**, not TOP-conformant surface; consumers must treat them as non-portable.

Either way, the gap between Guide and implementation is explicit. This project bumps the pin only after the chosen rule lands.

## 🧭 Notes for the Agora / implementer
- **Proposal only** — open on TagKit’s repo (issue / SPEC PR). Do not patch the pinned package in DnD.
- Workaround already designed locally: Role (or Character root Tag) contributes `__contains__` that resolves strings via an owned `NAMES` map, then uses SPEC `agent in Tag`; optional transitional `genus` fallback until genus retires.
- Python `is` remains identity and must not be overloaded for membership.
- When filing upstream, attach: desired Guide wording, CONFORMANCE bullet (if promote), and a minimal failing/passing example (`NAME = "Eldritch Knight"`; `"Eldritch Knight" in agent`).

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** — *(upstream issue/PR URL + pin bump when accepted)*
- **Moved to Solved:** —

---

## ⚗️ Reward (separate dialog — do not fill during implementation)

- **Reward file:** `Rewards/REW-####-short-title.md` *(pending distillation dialog)*
- **Distilled:** —

---

## 🏛️ Council
> Wizard Consul: Kit ships Label-probes; Guide is silent — consumers cannot tell contract from sugar. Upstream must name the law.
> Warlock Consul: Our mitigation (owned NAMES + Tag-object `in`) is correct until SPEC speaks. Do not fork TagKit.
> Lorekeeper Consul: File as Suggest to TagKit; close this questa when upstream accepts promote *or* demote and we bump/document the pin.
> Druid Consul: SpellsKit already advertises `"evocation" in fireball` — same gap. One upstream decision covers both Atlases.

**Weighting:** reach 2 × severity 2 = **4** · council leaning: `build` *(file upstream; local workaround proceeds)*
