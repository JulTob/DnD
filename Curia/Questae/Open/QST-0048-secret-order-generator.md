# QST-0048 — The Secret Order generator

- **Type:** design / tagkit
- **Priority:** 🟠 high
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Architecture Consul (Druid), Contracts Consul (Warlock), Lorekeeper, Simplicity Consul (Monk)
- **Parent:** —
- **Sidequests:** QST-0048.1 (spell theme Tags), QST-0048.2 (Atlas of Vocabulary)
- **Related:** QST-0016.2 (every Character rolls their own dice), QST-0020 (Features with TOP), QST-0047 (Skills and Tools as Tags)

---

## 🔍 Diagnosis (what & where)

`AtlasLusoris/AtlasOfBackgrounds/Map_of_Eberron_Backgrounds.py` holds 17 records, of which **12 are `House <Name> Heir`** — one per dragonmarked house — plus `Aberrant Heir` and `House Agent`. Each heir background differs from its siblings only by which Mark feat it carries.

Two problems:

1. **Setting-locked.** Twelve proper-noun houses are exactly the copyrighted material this project de-couples from.
2. **Twelve records for one idea.** They are the same background wearing different mark names, and hand-writing twelve variants produces a set whose entries are, by construction, near-duplicates.

The de-coupling work so far (34 backgrounds across PHB + Forgotten Realms) replaced each record with a bespoke identity. Applying that here would produce twelve competent, similar entries — the least interesting possible outcome for a project whose name is GenLegend.

## 🧾 Evidence

The Marks are a **strict three-slot template**, verified against the published feat (Mark of Making):

| Slot | Mark of Making | Varies by mark |
|---|---|---|
| Intuition die | *Artisan's Intuition* — +1d4 on Arcana or Artisan's Tools checks | which checks |
| Signature magic | *Spellsmith* — Mending cantrip; Magic Weapon always prepared, free 1/Long Rest; INT/WIS/CHA | cantrip + spell |
| Spells of the Mark | Identify, Tenser's Floating Disk / Continual Flame, Spiritual Weapon / … / Creation | the 1st–5th list |

13 Dragonmark origin feats, plus 14 "Greater Mark" general feats (level 4+, each requiring a mark) — the same two-tier shape already implemented here as `Field Lieutenant` → `Field Marshal`.

2024 also **removed the bioessentialism at source**: any species may take any mark. The bloodline is already vestigial in the rules; only the house names still carry it.

Supporting machinery already exists in the codebase:

- **Themed spell pools** — `AtlasMagia/Map_of_Magic.py` keys spell lists by theme (`"Celestial"`, `"Undead"`, `"Traveler"`, `"Plant"`…).
- **Name fragments** — `AtlasEpica/Map_of_Titles.py` holds `of the <thing>` patterns.
- **Tags minted per instance** — `AtlasLusoris/Map_of_Weapon_Masteries.py` mints `Mastery_Of_<Weapon>` via `type(...)`.

## 🎯 Desired outcome

One background whose **Secret Order is generated per Character**, replacing the twelve heir records while preserving every mark's mechanics.

An Order collapses from independent axes:

```
Tradition     Arcane | Divine | Primal   → places, practices, customs; fallback spell pool
Domains       one or more, unordered      → mechanics (the three slots), philosophy, tension
  each with a facet                       → which face this Order turns
Devotion      god | demon | dragon | ancestor | trade | principle | the dead
Organization  Brotherhood | Temple | Academy | Lodge | Circle | Company | Order
Perk          what it gives
Sacrifice     what it takes
Goal          what it wants (drives the Hook)
Name          <organization> of the <descriptor> <core>
```

The Tradition axis is deliberately **independent of Domain**: an Order of Death may be Arcane, Divine, or Primal for entirely different reasons. It also guarantees a non-empty spell pool when a domain's own list is thin, which is the safe-coding reason to keep it.

Solved looks like: rolling a Character produces an Order with a name, a philosophy, a feat assembled from the three-slot template, and a Hook — and rolling again produces a different one that is equally evocative.

## 🧭 Principles (decided — do not re-litigate)

1. **Evocative first.** Drama and colour are priority one. A generic, colourless Order is a failure even if the machinery is elegant; scrap and rebuild rather than ship dull output. *"Theme is a direction, and we make it an outlier along that axis."*
2. **No bioessentialism.** Membership is never inherited. Orders initiate, teach, license, and mark; they do not breed. Any species, any class.
3. **Themes are complementary, not exclusive.** `Life and Death` is a philosophy, not a contradiction; Greek gods held plague and healing at once. **Do not build exclusion lists.**
4. **Guided randomness, not filtered randomness.** A Healing order whose goal is assassination (surgeons excising society's cancer) is a *feature*. Each collapsed choice constrains how later choices *relate*, never which are permitted.
5. **Domains are tagged, not ranked.** An Order simply *has* domains — there is no primary and no secondary. Some followers come to Hera for vengeance on a cruel husband, others for the safety of the house; neither is her "first" function. Tagging rather than ordering also leaves the gate open for a third or fourth domain later without reworking the model.
5a. **Domains are mythic and archetypal, never job descriptions.** "Hospitality" is a trade; **Home** is a domain, and every pantheon has one. Look to real mythology when naming: Making becomes **the Forge** (Hephaestus, Goibniu, Ptah, Prometheus) and covers craft and building, not literal smithing; Finding becomes **the Hunt**, which pantheons are full of, where "Tracking" is nobody's god. Aim for the Jungian register: the archetype under the trade.
5b. **A domain turns several faces.** Hera held *xenia* and vengeance at once and nobody calls her incoherent, so each domain carries **facets**. The generator picks a facet, letting one domain produce an order of sanctuary-keepers and an order that offers a last comfortable night before the knife. It is also how two orders share a domain and remain enemies.
5c. **Never explain the pairing.** State it and stop. The reader invents the reason faster and better than the generator could, and the invention is theirs.
5d. **The object of devotion is open-ended.** An Order may follow a god, a demon, a dragon, an ancestor, a trade, a principle, or a dead sorcerer. What it must have is *cultists* — devotion and obligation — not a deity.
5e. **The organization word is chosen, and then it propagates.** The name pattern is `<organization> of the <descriptor> <core>`: **Brotherhood** of the Wild Dragon, **Temple** of the Mad God, **Academy** of the First Sorcerer. Whatever word is drawn must then govern the prose — *"the brotherhood is your home"*, *"the temple taught you everything"*, *"the academy made you a wizard"*. The collapse propagates instead of stopping at the title, which is what makes it feel authored rather than assembled.
6. **One Order per Character, never shared.** Two characters unknowingly belonging to different secret orders is comedy and drama; co-membership flattens agency (one becomes an authority, or both play safe). *"They are watching"* is a better threat unseen.
7. **Every roll is the Character's.** All picks go through `char.Pick` (QST-0016.2). Same seed, same Order.
8. **Wave-function collapse in the prose, too.** Connective sentences are drawn from pools, so the same meaning arrives in different words. No fixed scaffolding sentence may ever repeat verbatim across characters.
9. **The dice may still produce the classics.** The twelve canonical marks stop being backgrounds but remain reachable as Theme outcomes, mechanically intact.
10. **Themes are data.** Adding *Death*, *Debt*, *Memory*, or *Sleep* later is one entry, not a refactor.

## 🧭 Notes for the Agora / implementer

- **Feat generation:** fill the three verified slots from the Theme (which checks take the d4; which cantrip + prepared spell; which 1st–5th list). Do not invent new mechanical shapes. The Greater Mark tier maps onto the existing general-feat gate (`requires_feat_any`, added for Field Marshal).
- **Do not name the body a Guild** (that is the class Tag), a **School** (schools of magic), or a **College** (bard). `Order` is chosen.
- Vertical slice first: **two domains end to end** — **the Forge** (from Making) and **Home** (from Hospitality) — with real feat assembly, generated name, and assembled Hook. Read the output before adding more. **the Hunt** (from Finding) is the obvious third.
- Slot names, fixed: **`intuition_die`**, **`signature_magic`**, **`spells_of_the_order`**. They generalize the published slot names (Artisan's Intuition / Spellsmith / Spells of the Mark) and read clearly at the call site.
- Weave practices and places **into** the description and hook rather than emitting them as fields. Leak the world instead of documenting it: *"any temple to a Dark God may take you to a back room with a warm bed and a hot meal"* teaches that dark gods have public temples without ever saying so. Subtle and evocative, never an encyclopedia entry.
- Count changes: 12 background records collapse to 1. Update the `BackgroundKit` self-test total.
- The Hook keeps the house shape used throughout the set: **what it is · what it gives · what it takes**.

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

> *(awaiting the Agora)*

**Weighting:** reach ⟨3⟩ × severity ⟨2⟩ = **6** · council leaning: `build`
*(Reach 3: backgrounds, feats, spells, and vocabulary. Severity 2: design — the current records work, they are merely setting-locked and duplicative.)*
