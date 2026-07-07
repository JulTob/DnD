# 🧭 Conventions — Naming & Lore

> **Canon.** Read, do not edit. The naming is not decoration; it is how the project stays legible *and* stays Julio's. Names are adventurous, but purpose is always clear to a maintainer.

This Canon consolidates the naming law. Tool-specific naming reviewers are downstream of this file and must stay in sync with it; this file wins on any conflict.

---

## 📚 Libraries (packages) = **Atlases**

Top-level packages are **Atlases**. The name is flavorful; the domain is clear.

| Atlas | Domain |
|-------|--------|
| `AtlasLusoris` | players / PCs |
| `AtlasAlusoris` | non-players / NPCs |
| `AtlasLudus` | the game itself (dice, damage) |
| `AtlasPugna` | combat |
| `AtlasMagia` | magic |
| `AtlasInventarium` | items & equipment |
| `AtlasNomina` | names & linguistics |
| `AtlasScriptum` | writing / documents (PDF, export) |
| `AtlasActorLudi` | actor stats (scores, modifiers) |
| `AtlasWorldBuild` | world & map building |
| `AtlasIntelligentiaArtificialis` | AI (portraits, prompts) |

New domains earn a new Atlas name that fits the theme. **No generic or non-thematic package names.**

> ⚠️ **Known inconsistency to resolve via the Agora:** `AtlasLusoris` (players) and `AtlasAlusoris` (NPCs) differ by a single letter and are easy to confuse and mistype. This is logged as a Questa. Until a Decree rules on it, **do not silently rename** — both are load-bearing in imports.

---

## 📜 Files (modules) = Maps, Grimoires, Compasses, Lodges, Ledgers

| Prefix | Use for | Examples |
|--------|---------|----------|
| **`Map_of_X`** | lookups, data tables, mappings — "where to find things", key→value data, algorithms | `Map_of_Races`, `Map_of_Dice`, `Map_of_Backgrounds` |
| **`Grimoire_of_X`** | substantial definitions, classes, "books" that invoke entities | `Grimoire_of_Characters`, `Grimoire_of_NPC` |
| **`Compass_of_X`** | canonical types, enums, categories — "direction" | `Compass_of_Conditions`, `Compass_of_Damages`, `Compass_of_Armors` |
| **`Lodge_of_X`** | curated, closed sets | `Lodge_of_Spells`, `Lodge_of_Basic_Weapons` |
| **`Ledger_of_X`** | lists, records, enumerations | `Ledger_of_Weapons`, `Ledger_of_Legendary_Actions` |

Other established patterns (`Kit_of_`, `Scroll_of_`, `Shop_of_`, `Helm_of_`, …) stay consistent: adventurous theme, clear purpose. **Flag any new file that does not follow one of these prefixes** or invents an ad-hoc pattern.

**No mislabelling:** a data table is not a `Grimoire_`; a class-heavy module is not a `Map_`.

---

## 🧞 Runtime helpers = **Minions**

`Minion.py` provides fail-system decorators. They **never change a function's return value**; they only feed the log system.

| Decorator | Use when |
|-----------|----------|
| `@minion` | entry points / main flows: log success/failure, re-raise on failure |
| `@warden` | retry-friendly: on failure log, retry once with default args |
| `@watcher` | I/O & handlers: log result; on failure log enriched `file:line`, re-raise |
| `@spy` | trace the call tree (chain of command) |
| `@guardian` | critical/flaky: retry same args until success or 100 attempts |

---

## 🏛️ Coordination = the Curia lexicon

| Term | Meaning |
|------|---------|
| **Curia** | the coordination hall (this folder) |
| **Canon** | Julio's law — read-only for agents |
| **Agora** | the council where decisions are deliberated |
| **Consul** | an expert voice in the Agora |
| **Vox** | the Speaker who reports the Agora to Julio |
| **Decree** | a ratified decision |
| **Agentia** | the working agents |
| **Questa** | a quest — one unit of work / a ticket (`QST-####`) |

---

## ✍️ In-world vs. code

- **User-facing strings and comments** may be as flavorful as you like.
- **Code symbols** (modules, classes, functions, variables) follow the conventions above and must stay clear to a maintainer.
- Imports must reference the correct Atlas and file type (e.g. `from AtlasLudus.Map_of_Dice import Dice`), never a misnamed module.
