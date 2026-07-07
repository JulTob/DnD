# QST-0022 — Lodge symbol rationale review (species · class · element)

- **Type:** design / question
- **Priority:** 🟡 normal
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Design-Team, Lorekeeper Consul, Readability Consul (Barbarian), Julio
- **Parent:** QST-0021
- **Sidequests:** —
- **Related:** QST-0021.1 · `AtlasVenustas/Lodge_of_Symbols.py` · `SpellsEffects/` · QST-0003 (Flask retirement)

---

## 🔍 Diagnosis (what & where)
`Lodge_of_Symbols` now holds default pools plus species/class maps, but the **mapping rationale is implicit** — chosen quickly during QST-0021.1 scaffolding. Aesthetic is what the user sees; each glyph should correspond to a **conscious** element (species, class, alignment, mood) with documented reasoning.

Early concept work in `SpellsEffects/*.p5js` (Dwarf, Paladin, Warlock, warlok2) prototyped class-themed **sol** (center) vs **planet** (orbit) invocations — richer than the current Lodge, but never reviewed or canonized.

## 🧾 Evidence
- `SpellsEffects/Dwarf.p5js` — center: `⛏` `⚒` (craft/earth); orbit: full Futhark + `⬨` + `⛰`
- `SpellsEffects/Paladin.p5js` — center: `♥` `⚜` `♡`; orbit pool: stars/flowers; accent `☥`
- `SpellsEffects/Warlock.p5js` — center: `⛦` `◯` `⛥`; uses `🜏` (alchemical — emoji risk on mobile)
- `SpellsEffects/warlok2.p5js` — `unholy()` pool: `⛤⛥⛦⛧۞☣༄࿓☥`; center `𐦝` `◯` `⛥`
- `Lodge_of_Symbols.py` — maps exist but no `Map_of_Symbol_Rationale` or Agora Decree
- Julio (QST-0021.1 Council): avoid phone-emoji rendering; prefer unicode; map alphabets to species, symbols to classes

## 🎯 Desired outcome
A reviewed, **documented symbol taxonomy** that Julio ratifies:

1. **Rationale table** — for each species/class (and eventually background/alignment): which symbols, why, sol vs planet role
2. **SpellsEffects harvest** — adopt useful glyphs; reject emoji-risk or redundant ones
3. **`Lodge_of_Symbols` updated** to match the ratified table (or split into `Map_of_Symbol_Rationale.py` + thin Lodge)
4. **Loader behavior** — when URL/selection carries species+class, loader uses the merged pool (Kit_of_Loader already accepts kwargs)
5. Optional: open **Agora Dialog** if counselors disagree on mappings (e.g. Dwarf = runes only vs runes + tools)

*This questa diagnoses and prepares the review — it does not pre-solve every mapping.*

## 🧭 Notes for the Agora / implementer

### Review agenda (suggested)
| Lens | Question |
|------|----------|
| Species | Which alphabet/script per species? (Runic→Dwarf, Tibetan→Dragonborn, …) |
| Class | Which symbol family per class? (Math→Wizard, botanical→Druid, …) |
| Sol vs planet | Center = identity; orbit = invocations — confirm or revise |
| Mobile safety | Re-audit `_is_safe_symbol()` against SpellsEffects picks |
| Duplication | Merge with `base.html` Flask pools before QST-0003 deletes them |

### Candidates from SpellsEffects (for discussion, not adoption yet)
| Symbol | Source | Proposed element | Risk |
|--------|--------|------------------|------|
| `⛏` `⚒` | Dwarf sol | craft, earth | `⚒︎` has variation selector |
| `⛰` | Dwarf orbit | mountains | safe |
| `⬨` | all sketches | orbit geometry anchor | safe |
| `⚜` `♥` `♡` | Paladin sol | devotion, crown | hearts may emoji on some OS |
| `⛤⛥⛦⛧` | warlok2 unholy | warlock/pact | already in Lodge |
| `◯` | Warlock sol | circle/pact | safe |
| `𐦝` | Warlock sol | obscure script | verify font coverage |
| `🜏` | Warlock orbit | alchemy | **reject** — U+1F70F emoji block |

### Deliverables
- [ ] Review notes in `Agora/Dialogs/` (new Dialog) or inline in this questa's Resolution
- [ ] Julio signs off mappings
- [ ] Lodge updated + self-test still passes
- [ ] `SpellsEffects/` marked orphan or archived in QST-0017 after harvest

### Do NOT
- Block QST-0021.3–6 on this review (defaults work; review refines)
- Add emoji or unreviewed alchemical supplementary symbols without Julio's OK

## ✅ Resolution
*(pending — filled when Solved)*

---

## 🏛️ Council
> Design-Team: SpellsEffects is a mood board — mine it for intent, not code. The sol/planet split is the real find.
> Lorekeeper Consul: Species and class mappings need a table Julio can read like a bestiary index, not a Python dict only.
> Readability Consul (Barbarian): Document the *why* next to each symbol — future agents will otherwise re-litigate every glyph.
> Julio: Aesthetic is user-facing; conscious decisions required.

**Weighting:** reach 2 × severity 2 = **4** · council leaning: `needs a Dialog`
