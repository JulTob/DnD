# QST-0081 — The level shows its number; the orbits flip their coin again

- **Type:** bug / recovery (presentation)
- **Priority:** 🟠 high (beta path, reported by Julio)
- **Status:** Solved
- **Owner:** Claude
- **Route to:** Venustas
- **Parent:** QST-0072
- **Sidequests:** —
- **Related:** QST-0024 · QST-0073 · Decree 0006

---

## 🔍 Diagnosis (what & where)

Two presentation losses from the accident, both reported by Julio in chat
(2026-08-31):

1. **The level control showed no number.** The stylesheet still carried the
   contract for the lost markup: `.character-level-value` with
   `grid-column: 2`, in a grid the controls rule had shrunk to two columns.
   The reforge toolbar rendered only the minus and plus buttons; the current
   level lived exclusively in server state.
2. **The summoning circle stood still.** The CSS held the surviving half of
   the design: spin animations defined on an inner `.orbit-ring`, a
   `perspective`d `.orbit-layer` shell with a 0.85s transform transition, and
   a `.flip-y` coin-flip state annotated "toggled by JS". The loader script
   built neither the ring nor the toggler: planets were appended straight to
   the shell, so nothing spun and nothing flipped. The random X-axis flip
   Julio remembers had no surviving CSS at all.

## 🎯 Desired outcome

Julio's spec, verbatim in substance: the orbits rotate in the summoning
circle, and every second one orbit at random flips 180 degrees on the X or Y
axis, which then changes its direction. The level control shows its number.

---

## ✅ Resolution

- **Decided by:** Julio's report and spec, 2026-08-31
- **What changed:**
  - `shiny_app.py`: a `.character-level-value` cell now sits between the
    buttons, fed by a `char_level_display` text renderer reading the reforge
    state; the controls grid returned to three columns.
  - `Tools_of_Loader.py`: `populatePlanets` builds the `.orbit-ring` child
    the CSS always expected (restoring the spin), and a 1-second ticker
    toggles `flip-x` or `flip-y` on one random orbit while the loader shows.
    The mirrored shell reverses the ring's apparent spin direction: the flip
    IS the direction change, exactly as the surviving CSS comment described.
  - `style.css`: added the missing `.flip-x` and combined `.flip-x.flip-y`
    states.
  - Verified live: level "2" renders for a level-2 URL; class sampling over
    four seconds showed random per-orbit X and Y flips including a flip-back;
    computed style confirms the ring spins (`rotate`, 10s/15s/20s).
- **Practice/preference to remember:** the stylesheet is a witness. When CSS
  names an element or state no markup produces, that is the shape of what
  was lost: rebuild to the contract before inventing a new one.
- **Correction (same day):** the first rebuild put the value in the wrong
  grid: the reforge-era `.character-level-box` IS the three-column grid (the
  controls wrapper is `display: contents`), so the label div auto-placed over
  the minus button. Julio's spec settled the design: the label rides on top
  of the number inside the middle cell, as a small caption. The stray
  three-column edit to the older `.character-level-controls` block was
  reverted. Verified: the pill reads "- / LEVEL over 2 / +" and a press of +
  reforges to level 3 with the sheet chip in sync.

## 🧭 Notes for the Agora / implementer

`app/static/js/loaderMagic.js` is an older, unused p5 loader (undefined
`ctx`, an array passed where a scalar speed is expected). It is debris from
a previous era: retire it deliberately in the orphan sweep (QST-0017), not
silently here.

---

## 🏛️ Council

> Venustas Consul (Bard): A conjuring circle that does not turn is a diagram.
> Turn it, and once a second let one ring show its other face: the eye stays
> because the pattern almost repeats.

**Weighting:** reach 2 × severity 2 = **4** · council leaning: `build`
