# QST-0060 — Sheet presentation: cantrip scaling, stacked items, kits

- **Type:** docs
- **Priority:** 🟡 normal
- **Status:** Open
- **Related:** QST-0055 · `AtlasInventarium/GearKit.py`

---

## 🔍 Diagnosis

Small presentation faults, each cheap, all visible on every sheet.

**Cantrip scaling is appended as extra prose.** A levelled cantrip should update
its damage **silently and in bold** inside its own description, not carry a
trailing sentence explaining that it scaled.

**Equipment stacks that should be entries.** Two Potions of Greater Healing
print as `x2`; they should be two entries, because they are consumed
individually and a player ticks them off one at a time.

**Equipment entries that should be one item.** Book, Ink and Ink Pen are three
lines for one object in practice. They want a single **Writing Kit**.

**Warlock ability preference order.** Currently primary Charisma, secondary
Constitution. Dexterity belongs **after** Constitution as a defensive third,
without being a priority in its own right. Blocked on QST-0049.

## 🎯 Desired outcome

Cantrips read as one paragraph with current numbers. Consumables list per unit.
Composite kits list as the kit. Warlock stat order runs casting ability,
Constitution, Dexterity.

## 🧭 Notes

The casting ability is drawn **lazily**, after `set_stats` has rolled, so a
Covenantor can still land on a mediocre Wisdom. Drawing it during `Apply_Guild`
would let the array build around it. That belongs with QST-0049 rather than
here.
