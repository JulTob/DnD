# QST-0099 — `Strong_Arm` is defined twice and the degraded copy is the live one

- **Type:** bug
- **Priority:** 🟠 high
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Technical Team · Readability (Barbarian)
- **Related:** `Canon/Feature-Text.md` (breaks are written, never inferred) · `AtlasLusoris/AtlasOfFeatures/Map_of_Official_Origin_Feats.py`

---

## 🔍 Diagnosis (what & where)

`class Strong_Arm(Origin_Feat)` is declared twice in the same file, at line 864
and again at line 2021. The second wins.

The two are not identical. The dead copy carries `<br>` before its second
sub-benefit; **the surviving copy does not.** So the live Strong Arm prints its
two benefits run together: *"...against the target. On My Mark. If you have..."*

Every other feat in the file keeps its break, so this is the one entry that
violates the formatting law, and it does so because the wrong copy survived.

## 🧾 Evidence

- Verified at runtime: the catalogue entry resolves to the line-2021 class.
- The earlier note in the Mythos folder recorded the duplication but not that
  the surviving copy is the degraded one.

## 🎯 Desired outcome

1. One `Strong_Arm`, keeping the `<br>`.
2. A sweep for other duplicate declarations in the same file.
3. The rendered feat shows its two sub-benefits on separate lines.
