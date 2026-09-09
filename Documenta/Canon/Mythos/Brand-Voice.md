# 🏷 Brand Voice: the words around the sheet

> 🚧 **Draft.** Analysis and proposals, not yet authoritative. Under review.

*Wiki entry for the design team. Decree 0006 ranks the beta's priorities:
aesthetics, brand, the service. The sheet's voice has forty pages; the frame
around it (home page, buttons, empty states, errors, the share link, the type
and the palette) has none. Compiled 2026-09-08 from `app/pages`,
`app/publish_scope.py`, `app/character_url.py` and `app/static/style.css`.*

> **In one sentence.** Inside the sheet the app speaks in second person with
> one register per voice; at the sheet's edge it says "Generate a legendary
> Character for your next adventure," which is every fantasy product's sentence
> and none of this one's.

---

## 1. Every word the frame says

| Where | Text |
|---|---|
| Home heading | Welcome to Gen Legend |
| Home lede | Generate a legendary Character for your next adventure. |
| Tablet title | Character Generator |
| Buttons | Generate · Random (seven times, one per selector) · Level Up · Level Down · Share |
| Selectors | Species · Specialization · Background · Gender · Level {n} |
| Empty state | Generate a character from Home. |
| Error | Character generation failed |
| Share status | (element exists; copy not found in the page) |
| The link | `/species/class/specialization/background/level/gender/seed`, with `random`, `none` and `_` as "let the dice" |
| Parked (Decree 0004) | NPC Generator · Generate a Non Player Character · Generate 5 NPCs · Dungeon Master Companion · "Set a DM Character — Area and Lair lock from their Tags. They may be a villain, a Quest Master, a contested…" |

The frame is functional, clear and anonymous. Nothing in it could not be on
any other generator's home page.

✅ **The one exception is the URL.** A character is a readable path with the
seed at the end, and the same path is the same person forever. That is the
product's promise (the replay contract) made visible, and it is already the
best brand statement the app has. It should be said in words once, where the
link is copied.

⚠️ **One sentence of lore lives in the presentation layer.** "Humans have
complex lives, and they adapt quickly." is written in `character_sheet.py`
(the Versatile renderer), the only species prose anywhere in `app/`. The Human
page proposed a line for Versatile; whichever line wins, it belongs with the
Human entry, not in the view.

---

## 2. The voice the frame should borrow

The sheet already has a voice and the frame should be its outer edge, not a
different product. Three rules carry over:

1. **Second person, present tense.** The sheet says *you*; the frame says
   "Generate a legendary Character," which is about a product.
2. **Nothing explained.** The frame should not say what a Character is or what
   the app does; the button does that.
3. **The seed is the promise.** Say it once, plainly.

Per the Design-Team charter ("propose 2–3 variations, not one"):

| Slot | Today | A | B | C |
|---|---|---|---|---|
| Home lede | Generate a legendary Character for your next adventure. | *You did not choose this one. Read it anyway.* | *Somebody is about to exist. Press the button.* | *A stranger, a sheet, and a seed you can hand to anyone.* |
| Empty state | Generate a character from Home. | *Nobody here yet.* | *No one on the table. Go to Home and draw.* | *The page is waiting for a person.* |
| Error | Character generation failed | *Nothing came of that seed. Draw again.* | *The dice would not settle. Once more.* | *That one did not come through. Try another seed.* |
| Share status | (none) | *Copied. Same link, same person.* | *Copied. Whoever opens this meets the same one.* | *Link copied. The seed is in it.* |
| Random (selector) | Random | *Let the dice* | *Any* | keep *Random*: the label must stay a lookup |

The button labels (Generate, Level Up, Share) are lookups and should stay
plain, the way chips do on the sheet. The voice belongs in the sentences.

---

## 3. Type

Nineteen font families are requested from the hosted service: eight IM Fell
variants, Cinzel and Cinzel Decorative, Spectral SC, Eagle Lake, four scripts
(Italianno, Tangerine, Beau Rivage, Fleur De Leah), UnifrakturMaguntia (the
Warlock's title face), Manufacturing Consent (the default spell-section title
face), plus two local names in the stacks (Kings and Pirates, Nordic Chance).

| Variable | Face | Reads as |
|---|---|---|
| `--font-text`, `--font-entry`, `--font-record`, `--font-name`, `--font-impact` | IM Fell (DW Pica, Double Pica, Great Primer, English; roman and small caps) | ✅ One family for the book: a seventeenth-century Fell type on parchment is exactly right, and five roles from one family is coherence, not clutter. |
| `--font-header` | Cinzel | ✅ Roman inscriptional capitals: the Goliaths' Rome, on every heading. |
| `--font-fancy`, `--font-fantasy` | Kings and Pirates, Eagle Lake, Cinzel Decorative | ⚠️ Three display faces for the ornamental slot. |
| `--font-script` | Italianno, with Beau Rivage, Fleur De Leah, Tangerine and Dancing Script in fallbacks | ⚠️ Four scripts requested where one is used. |
| spell titles | Manufacturing Consent; UnifrakturMaguntia for the Warlock | ❓ A face named *Manufacturing Consent* as the default voice of magic is a joke only the developer hears. The Warlock's gothic is a voice (Spells page). |

**Brand is one voice.** Three families carry the whole identity today (Fell,
Cinzel, one script); the other sixteen requests are weight without identity,
and every request is load time on a page that is meant to look like craft.
The house preference for plain Unicode over hosted fonts applies with force
here: undecided, and the Spells page's gothic-title question is the same
question.

---

## 4. Colour and metaphor

Gold (`#ffd700`, `#d4af37`, `#cda410`), red (`#cd1017`, `#aa0a12`), parchment
(`#fff9f0`). Heraldic gold and gules on vellum, and the CSS calls the page a
**tablet** (`tablet-title`, `tablet-nav`, "the NPC tablet face"). ✅ One
metaphor, consistently named in the code and never in the copy. Say it once
on the page or let it stay a secret; either is a brand decision, and today it
is neither.

---

## 5. Decisions log

**Standing**: the URL shape; the Fell and Cinzel pairing; the tablet metaphor;
plain labels for buttons.

**Open (this page proposes)**: the five sentences of frame copy (§2, three
variations each); the font stack pruned to three families and one accent; the
Versatile sentence moved out of the view; the share status sentence.

**Undecided:** hosted fonts versus plain Unicode; whether the tablet is
named.

---

## 6. Pointers

- **Lenses §10**: atmosphere as the wordless layer.
- **Spells-and-Invocations §5**: the Warlock's title face.
- **Human page**: the Versatile line.
- **Sheet-Alignment-Languages §1**: chips are lookups; prose is the entry. The
  same rule sorts the frame's words.
- Decree 0006; Decree 0004 (`PLAYER_ONLY_PUBLISH` decides which sentences show).
