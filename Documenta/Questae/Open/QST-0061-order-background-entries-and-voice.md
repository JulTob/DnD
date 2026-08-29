# QST-0061 — The Order background: too many entries, and the voice is off

- **Type:** design / docs
- **Priority:** 🟡 normal
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Understanding (Bard), Readability (Barbarian), Simplicity (Monk), Lorekeeper
- **Parent:** QST-0048 (The Secret Order generator)
- **Sidequests:** —
- **Related:** QST-0048.2 (Atlas of Vocabulary), QST-0055 (voice sweep), QST-0060 (sheet presentation)

---

## 🔍 Diagnosis (what & where)

Julio, reading a generated Order background: *"it lacks something still… It doesn't make sense to
have three entries for it. And they all sound off."*

Two separate problems sit on top of each other.

### 1. One Order occupies five Feature Entries

A Character with the Order Cultist background carries **five** entries that are all about the same
Order, three of which are pure narration of it:

| # | source | name | what it does |
|---|---|---|---|
| 1 | `Background` | Order Cultist | explains the *generator*, not the character |
| 2 | `Background Hook` | Sworn | restates 1 in three clauses |
| 3 | `Secret Order` | *(the Order's name)* | one very long narrative paragraph |
| 4 | `Order Hook` | *(the same name)* | three sentences on worth / price / purpose |
| 5 | `Origin Feat` | Sign of the *(Order)* | the mechanics — the only one with rules |

Entries 3 and 4 **share a title verbatim**, so the sheet prints the Order's name twice as two
headings. Entries 1 and 2 duplicate each other's content, and neither says anything specific to
this character.

Sites: `AtlasLusoris/OrderKit.py:969` (`source="Secret Order"`) and `:975` (`source="Order Hook"`);
`AtlasLusoris/BackgroundKit.py:971` (the Background text) and `:975` (the Hook).

### 2. The prose gives away its own machinery

Four distinct defects, each reproducible:

**(a) It breaks the fourth wall.** The Background entry describes the generator rather than the
world: *"…are collapsed the moment you are rolled: no two initiates have ever answered to the same
house. Read your Order below."* (`BackgroundKit.py:971`). "Rolled" and "read below" are addressed
to the player looking at a sheet, not to a person in the setting. The Hook does the same: *"Your
Order was decided when you were"* (`BackgroundKit.py:975`).

**(b) A template shows through.** The Order Hook is visibly a three-slot fill:
*"Ask what the {house} is worth… Ask the price… Ask the purpose…"*
(`AtlasLusoris/AtlasOfOrders/Map_of_Myth.py:933`). Every Order in the game produces the same three
questions in the same order, so the shape is legible after reading two characters.

**(c) Clause-length fillers fuse the sentences.** The templates are written as though their slots
take *noun*-length fillers; several slots return whole clauses. The rendered result loses its
grammar. From `Map_of_Myth.py:892`:

> template: `"Everyone in town knew you for {trade_name}. {contact_agent} knew it too, and brought you to {place} without explaining the {house} until you were already inside."`

> rendered: *"Everyone in town knew you for soft speech. A carter who stopped at your door with no
> load and a sealed hour, knew it too, and brought you to a spring that is kept clean by people
> nobody sees doing it without explaining the brotherhood until you were already inside."*

Two faults follow from the same cause: a stray comma before "knew it too" (the template assumed a
short subject), and a fused run-on where `{place}` ends in "…doing it" and the next clause begins
"without explaining…".

**(d) Person drift.** The Secret Order paragraph is second person throughout and then switches to
the Order's collective voice mid-sentence: *"No one should go into the dark cold, hungry, or alone;
that is all **we** promise."*

**(e) Em-dash in generated content.** The paragraph opens *"Someone has to keep the hall worth
returning to — and someone has to bring back what feeds it."* (`Map_of_Myth.py:732`), against the
standing preference for parentheses, colons or separate sentences.

---

## 🧾 Evidence

Reproduce with seed 62 at level 5 (background rolls as Order Cultist):

```python
from AtlasLusoris.Grimoire_of_Characters import Character, New_Player
c = Character(seed=62, level=5)
New_Player(c, level=5)
for f in c.features:
	if str(getattr(f, "source", "")) in (
			"Secret Order", "Order Hook", "Origin Feat",
			"Background", "Background Hook",
			):
		print(f"[{f.source}] {f.name}\n    {f.description}\n")
```

Order drawn: **Brotherhood of the Warm Trail**. Full output is quoted in the Diagnosis above.

Note that the **Origin Feat is not part of the complaint** — `Sign of the Warm Trail` reads
cleanly, states its rules plainly, and is the one entry that earns its place.

---

## 🎯 Desired outcome

An Order reads as *one thing* on the sheet, in a voice that does not reveal that it was assembled.
A reader who generates two Order characters should not be able to recover the template from them.

Specifically, "solved" means: no entry describes the generator; no two entries share a title; the
rendered sentences are grammatical whatever length their fillers happen to be; the voice does not
change person mid-paragraph; and the mechanical entry stays as clear as it already is.

---

## 🧭 Notes for the Agora / implementer

- **This is a diagnosis, not a plan.** How many entries an Order *should* have, and which of the
  five survive, is a design decision — open a Dialog rather than merging them on instinct.
- **Do not touch the Origin Feat.** It is the part that works.
- The prose belongs to Julio. An implementer may fix *grammar* (the comma, the fused clause) and
  remove fourth-wall phrasing, but new narrative text is written by Julio, not generated to fill
  the gap. See the standing rule in `Canon/`.
- Defect (c) is structural rather than editorial: it will recur for any new template unless slots
  declare what shape of filler they accept. Worth considering alongside QST-0048.2 (Atlas of
  Vocabulary), which owns the fillers.
- Defects (a), (d) and (e) are single-line edits and could be split into a sidequest if the entry
  count needs a Dialog first.

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

*(not yet convened)*

**Weighting:** reach ⟨2⟩ × severity ⟨2⟩ = **4** · council leaning: `needs a Dialog`
*(Reach: the Order background plus the shared Myth templates. Severity: presentation and voice, no
rules are wrong.)*
