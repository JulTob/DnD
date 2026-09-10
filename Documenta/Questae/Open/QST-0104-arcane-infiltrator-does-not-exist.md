# QST-0104 — Arcane Infiltrator is named by a background and does not exist

- **Type:** bug
- **Priority:** 🟠 high
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Technical Team · Design-Team
- **Related:** `AtlasLusoris/AtlasOfBackgrounds/Map_of_Arcana_Unleashed_Backgrounds.py`

---

## 🔍 Diagnosis (what & where)

The **Agent of the Ninth Quill** background declares `origin_feat='Arcane
Infiltrator'`. No such feat is implemented: not in the setting catalogue, not in
the base twelve, nowhere in the repository.

The background file concedes it in its own comment.

The background is also the roster's only stub in another respect: it has no
`roleplay` field at all, so it carries neither a hook nor a feat.

## 🎯 Desired outcome

1. Arcane Infiltrator is written, or the background points at an existing feat.
2. The background gains a hook, or is retired. Its own analysis suggests the
   thesis *the dangerous books are not kept by people who want them read*, and a
   hook where the Quill lends you what you stole and takes it back.
3. A generated Agent of the Ninth Quill shows an Origin feat on the sheet.
