# QST-0059 — Verify spell texts against the 2024 rules

- **Type:** rule-update
- **Priority:** 🟠 high
- **Status:** Open
- **Related:** `AtlasMagia/Lodge_of_Spells.py` · QST-0057

---

## 🔍 Diagnosis

Two spell descriptions are wrong on inspection, which implies the ledger has not
been audited as a whole.

- **Frostbite** — the printed description does not match the rules.
- **Hunger of Hadar** — likewise.
- **Touch of Death** — HTML tags are visible in the rendered entry (see
  QST-0056).

The Warlock work touched roughly forty spells by name across patron lists,
invocations and arcana, all of which are now assumed correct.

## 🎯 Desired outcome

Every spell the generator can place on a sheet carries its 2024 text, with no
markup leaking and no 2014 wording.

## 🧭 Notes

Sweep rather than spot-fix. Cross-check against a machine-readable source; the
markdown export in `Documenta/Sources` is an index only and has no rules bodies,
so it cannot be used for this.

Cantrip scaling is a related presentation bug, tracked in QST-0060.
