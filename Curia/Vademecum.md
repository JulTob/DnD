# 📖 Vademecum

> *Vademecum — "go with me." The handbook the adventurer keeps in a pocket and never travels without.*

Welcome to the project, traveller. Whether you are a human programmer or an AI assistant taking up a seat at the desk, **read this scroll first.** It is short on purpose. The detail lives in the `Canon/`.

---

## 🎒 What this project is

A set of tools for Dungeon Masters — a generator of characters and NPCs, and, in time, a companion for building worlds. It is a **personal project** with a strong aesthetic: the code is meant to be not only correct but *beautiful*. The naming is adventurous, the architecture is arcane-by-design, and the whole thing should feel like a work of craft.

The engine underneath is **TagKit** — a home-grown library implementing **Tag-Oriented Programming (TOP)**, a paradigm built specifically for this project. We use it, and we improve it. See `Canon/TagKit-Doctrine.md`.

---

## 🧑‍⚖️ Who is in charge

**Julio.** Always. The Curia exists to help him decide well, not to decide for him. Agents and programmers propose, deliberate, and prepare choices — Julio chooses. If you are ever unsure whether you may do something, the answer is: **mint a Questa and ask.** See `Canon/Single-Source-of-Truth.md`.

---

## 🗣️ How we talk

- **In the code:** magic and the arcane. Grimoires *invoke* entities, Kits *provide* utility, Atlases are *libraries*, Maps are *algorithms & lookups*, Compasses give *direction* (types).
- **In the Agora:** the tone of a conclave. Consuls address one another with reason and courtesy. Each line is signed by its speaker (`Readability Consul (Barbarian): …`).
- **In tickets:** plain and precise. Flavor is welcome in titles; the body must be clear enough that anyone can act on it.

Adventurous tone is not decoration — it is how this project stays *Julio's*. Adopt it. Have fun with it. But never let flavor obscure meaning: a maintainer must always understand what the code and the documents actually mean.

---

## 🧾 The two things you will do most

**1. Work a Questa (a ticket).**
Nothing meaningful happens without one. Find work in `Questae/Open/`, claim it by moving it to `Questae/Working/`, and when done move it to `Questae/Solved/`. Tickets are how we distribute tasks and remember why we did things.

**2. Bring questions to the Agora.**
Any decision that affects rules, architecture, naming, or design goes to the Agora. You add it to `Agora/Questions.md`; the Consuls deliberate; **Vox** reports to Julio; Julio issues a **Decree**. See `Agora/Agora-Protocol.md`.

---

## ⚔️ The etiquette (short version)

- **Dialog first, always.** One topic at a time, shown before landed, decided by Julio. This is Canon: read `Canon/Modus-Operandi.md` before touching anything.
- **Propose, don't push.** Especially external rules (new D&D content) and IP-adjacent design — those *always* open a discussion first.
- **Ask for confirmation** before non-trivial code changes and before any decision. Confirmation is a feature, not a delay.
- **Keep it light.** Avoid overengineering. Repeat proven patterns — especially TagKit patterns — instead of inventing new machinery.
- **If TagKit is insufficient** for a clean solution, that is not a workaround situation. Mint a Questa tagged `tagkit` with the **highest urgency**; TagKit is the heart, and the heart gets treated first.
- **Leave memory.** Solved questae and Decrees are the project's long-term memory of practice and preference. Write them so a future stranger understands.

---

## 🧩 Naming quick-reference (folders you'll see)

| You'll see | It means |
|------------|----------|
| `Curia/` | this coordination hall |
| `Agora/` | the council where we decide |
| `Consuls` | the expert voices in the Agora |
| `Vox` | the Speaker who reports the council to Julio |
| `Agentia/` | the working agents |
| `Questae/` | the quest log (tickets); each ticket is a `Questa` (`QST-####`) |
| `Atlas*` | a code library / package |
| `Map_of_*` | data tables & lookups (algorithms) |
| `Grimoire_of_*` | core classes / "books" that invoke entities |
| `Compass_of_*` | canonical types & categories |
| `Minion.py` | the fail-system decorators (@watcher, @warden…) |

Now read the `Canon/`. Then pick up a Questa. Safe travels.
