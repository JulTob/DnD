# QST-0107 — The nine Dark Gift lines exist and never reach the sheet

- **Type:** docs / voice
- **Priority:** 🟠 high *(the cheapest voice improvement in the project)*
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Lorekeeper · Understanding (Bard)
- **Related:** QST-0062 · QST-0094 · `AtlasLusoris/AtlasOfFeatures/Map_of_Official_Origin_Feats.py`

---

## 🔍 Diagnosis (what & where)

Each of the nine Dark Gifts already carries its inspiration line, written in the
house register, as a Python docstring the sheet never prints:

> *A boon that arrived uninvited and kept a share of you.* (the base)
> *Something in you is already partway across.* (Touch of Death)
> *Something is always looking, and it is not on your side.* (Watchers)
> *Your shadow moves on its own, and occasionally on its own behalf.* (Living Shadow)
> *There is another shape in you, and it does not always wait to be asked.* (Second Skin)
> *Something else lives in you, helps you, and is not on your errand.* (Symbiotic Being)
> *You remember a life that was not this one.* (Echoing Soul)
> *Exposure to something from outside has rearranged you.* (Aberrant Anatomy)

They are already second person, already one sentence, already in the register.
Moving them into the descriptions is a copy, not an authoring task.

It matters most here because a Dark Gift can reach a sheet through a Human's
Versatile with no background to explain it. That sheet needs the line more than
any other feat does.

## 📊 Measurement

Across generated sheets the feat layer carries no inspiration line at all:
General feats 0 of 44, Fighting Styles 0 of 12, Epic Boons 0 of 12.

## 🎯 Desired outcome

1. The nine docstrings become the first line of their descriptions, in the house
   shape: the italic line, a blank line, then the rule.
2. A generated Character carrying a Dark Gift shows the line above the rule.
