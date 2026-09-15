# QST-0125 — The Paladin's canon pages describe the retired device and four Oaths

- **Type:** docs
- **Priority:** 🟡 normal
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Lorekeeper (Elf Sage) · Readability (Barbarian)
- **Parent:** —
- **Sidequests:** —
- **Related:** PR #7 (the Paladin) · QST-0126 · Dialog 0026 · `AtlasLusoris/AtlasOfGuilds/PaladinKit.py` · `AtlasLusoris/AtlasOfTraining/Map_of_Paladin_Oaths.py`

---

## 🔍 Diagnosis (what & where)

`Documenta/Canon/Mythos/Paladin.md` was written for the first Paladin pass and
was overruled twice in chat. It still says:

- §4 "Four oaths, four wells": there are five. The Oath of Creation shipped on
  2026-09-14 (mechanics from the elemental subclass, lore ours, because an oath
  to a genie is a pact and a pact is the Warlock's seat).
- §9, the device is "the unquoted sentence": five texts refer to the oath and
  none prints it. The shipped device is the opposite. The oath is recited, six
  lines under each Oath paragraph, drawn by `Map_of_Paladin_Oaths.py`, one line
  by species and one by background, roman, one line each.
- §12 quotes the retired class text ("You said something out loud once"). The
  shipped text is the political romantic ("Ask who holds power in this world").

`Documenta/Canon/Mythos/Guilds-Registers-Names-Devices.md` carries the Paladin
row with the same retired register and device, and no poets column for the
five Oaths (Psalms and King James with Cavafy and Hesse; Shakespeare; Twain,
Espronceda, Moore, Gaiman and Cavafy; Lorca, Neruda, Scheherazade; Byron and
Bécquer).

## 🧾 Evidence

`grep -n "unquoted\|Four oaths" Documenta/Canon/Mythos/Paladin.md` finds the
three passages. The shipped `PALADIN_DESCRIPTION` and the docstring of
`Map_of_Paladin_Oaths.py` state the current rulings; the two disagree with the
canon page on fantasy, register, device and Oath count.

## 🎯 Desired outcome

The two pages state what ships: the core fantasy (a principle held; the oath
is its verbalization; will pointed outward, where the Barbarian's rage is
emotion pointed inward), the register (a Knight's tale in storybook aesthetic,
Twain's civic speech, no hedging, no imposed origin, no rule pre-explained),
the device (the oath recited), the five Oaths with their poets, and the reason
the fifth is sworn to Creation and not to a genie.

## 🧭 Notes for the Agora / implementer

No decision. Every ruling is Julio's, given in chat between 2026-09-13 and
2026-09-15 and recorded in the commit messages of PR #7. Record them; do not
reopen them. Keep the alignment-independence paragraph (bindingness rather
than virtue) and the Warlock boundary (sworn and forsworn), which still hold.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council

> Lorekeeper (Elf Sage): A canon page that contradicts the shipped kit is worse than no page, because the next agent will trust the page.
> Readability Consul (Barbarian): Write the page from the kit's docstrings outward. They already say it in plain words.

**Weighting:** reach 1 × severity 2 = **2** · council leaning: `build`
