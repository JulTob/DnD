# QST-0049 — Ability weights, and the +2/+1 split that a multiplier cannot protect

- **Type:** design / refactor
- **Priority:** 🟠 high
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Architecture Consul (Druid), Rules Consul
- **Parent:** —
- **Sidequests:** —
- **Related:** QST-0016.2 (reproducible RNG)

---

## 🔍 Diagnosis (what & where)

`AtlasLusoris/GuildKit.py` now carries `ability_weights(char, pool, amount)` and
`pick_ability(...)`: one dictionary that every "choose a score" site can draw
from. Julio's scale:

```
+50  the Guild's spellcasting ability
+10  any ability a class feature names
+1   each Background, Species, or Feat that mentions it   (these stack)
x1.25  landing the score on an even number
```

Parity **multiplies** rather than adds, decided after measurement: added at
`+10` it *created* interest rather than amplifying it, and a Fighter with
`STR 14 / WIS 9 / CHA 9` raised CHA as often as STR, because a dump stat scored
the same as the class primary purely for being odd.

The remaining problem is that a gentle multiplier cannot protect the **+2/+1
split**, and that decision is not a preference.

## 🧾 Evidence

Measured on `STR 13 / DEX 15 / CON 12 / INT 14 / WIS 10 / CHA 8`, asking how
often the **+2** lands on an odd score (which throws a whole ability point
away, since `13+2` and `13+1` both read `+2`):

```
x1.00   50% wasted        x1.25   46% wasted        x2.00   34% wasted
x1.10   48% wasted        x1.50   41% wasted
```

Even at `x2.00` the generator wastes a point a third of the time. The previous
implementation sorted on parity as a **hard primary key** and wasted 0%.

## 🎯 Desired outcome

Split the two decisions, because they are not the same kind of choice:

* **Which stats to raise** — weighted random through `pick_ability`, parity as
  the `x1.25` nudge. Variety here produces genuinely different characters, and
  a Fighter who takes DEX over STR is a legitimate build.
* **Which of the chosen stats takes the +2 rather than the +1** — deterministic
  parity. Once the pool is settled the `+2` goes on the even score and the `+1`
  on the odd one, every time. There is no upside to trade against and no
  variety argument for a strictly worse character.

## 🔧 Work

1. Wire the three "choose a score" sites onto `pick_ability`:
   - `BackgroundKit._pick_boost_ability`
   - `FeatKit._raise_one_of`
   - `Map_of_Official_Origin_Feats._pick_mental_casting_ability`
2. In `_grant_ability_boosts`, keep the parity filter deterministic for the
   allocation step, so `pick_ability` chooses *which* abilities and the split
   decides *how much*.
3. Confirm reproducibility survives (same seed, identical sheet).
4. Re-measure the waste rate; it should return to 0% on the `+2`.

## ⚠️ Notes

`ability_weights` and `pick_ability` exist and pass GuildKit's self-test, but
**no call site uses them yet** — the three sites still run on the older ordered
tuple from `ability_preference`, which works. Nothing is half-migrated.

`ability_preference` (ordered tuple) is retained: it is the readable authoring
surface, and Guilds and Specializations already declare it. Weights are derived
from position at read time, so the thirteen guild declarations never had to be
rewritten.
