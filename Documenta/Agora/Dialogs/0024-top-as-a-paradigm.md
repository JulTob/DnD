# Dialog 0024 — TOP as a paradigm: the recovery's verdict, and the paths forward

- **Convened:** 2026-08-31, commissioned by Julio ("evaluate TOP as a design
  paradigm and start designing paths for it")
- **Status:** evaluation and proposed roadmap; every path awaits Julio's word
- **Related:** Canon/TagKit-Doctrine.md · QST-0016 · QST-0018 · QST-0020 ·
  QST-0027 · QST-0031 · QST-0035 · QST-0036 · QST-0042 · QST-0047 · QST-0072

---

## Why this evaluation is unusually well-evidenced

The catastrophe was, accidentally, a controlled experiment on the paradigm.
Reconstruction forced a reading of nearly every TOP surface in the project at
bytecode depth, and the paradigm's properties showed up as measurable facts
rather than aesthetic preferences.

## The Dialog

> Architecture Consul (Druid): Begin with the strongest evidence. When the
> tree burned, what survived best was what TOP made declarative. Ten of the
> thirteen guild kits were restored byte-identical to their last working
> bytecode, because a kit is four Build_Specialization declarations: data
> wearing a thin coat of syntax. The imperative legacy Maps were where every
> vintage seam and every recovery bug lived. A paradigm that turns design
> into declarations turns catastrophe into transcription.

> Contracts Consul (Warlock): And the contracts fought back during the
> recovery itself. When the verification harness loaded a kit twice in one
> process, the Guild registry refused the duplicate Specialization by
> Precondition: the system defended its own invariants against its own
> rescuers. AlignmentKit's axis Preconditions encode a design truth (Good
> refuses a bearer of Evil) that no string check would have kept honest.
> Contract orientation is a Canon principle; TOP is where this codebase
> actually practices it.

> Workshop Consul (Artificer): The same event exposes the paradigm's tax.
> Global registries mean a module cannot be imported twice, so tests and
> tooling must isolate processes; the working gate for kits is now static
> bytecode comparison precisely because execution is not repeatable in one
> process. Import order is load-bearing: AtlasActorLudi's package init
> carries a lazy-import dance with a comment admitting it closes a cycle.
> These are real engineering costs, and they are payable: the static gate
> exists, and the cycle is documented. But a paradigm whose modules are
> world-mutating must ship its own test harness, and ours has not yet.

> Lorekeeper Consul: The composed type names earned their keep in the logs.
> `Character__Player__Good__Chaotic__Orc__Female__OpenHand__Exorcist` is a
> character sheet in a class name; during the crisis the Minion reports were
> self-describing because identity is composition made visible. No debugging
> session in the recovery ever had to ask "what is this object?"

> Methods Consul (Wizard): One drift finding, minted before this dialog
> closes: Canon/TagKit-Doctrine.md still speaks the pre-resync vocabulary
> (Expectation, Condition, Exclusion, Augmentation/Extension/Mutation) while
> every living kit speaks the current one (@Pre, Reports, @Underlay,
> extends/crunches). QST-0036 called this drift; its resync evidently did
> not survive the wipe. A settling paradigm plus a stale doctrine equals
> agents citing law that the code has outgrown. The doctrine file needs
> Julio's re-ratification against the pinned Guide.

> Architecture Consul (Druid): The extension-point promise also verified.
> Current-State records it for Backgrounds: one Build_Background call, no
> parallel registries to update. The guild kits repeat the shape. And the
> class-description commission slots into Describe_Layer's extends/crunches
> algebra with zero new machinery. Doctrine rule six (new content slots in
> the way existing content does) is not aspiration; it is measured.

> Contracts Consul (Warlock): Against that, name the sharpest counter-case
> from the crisis. The Ranger crash lived in activate_expertise: skills as
> string-keyed dictionary surgery, recursion by list mutation, a draw before
> a guard. That is exactly the code TOP exists to delete. QST-0047 (skills
> and tools as Tags) is not a stylistic wish; it is the elimination of the
> bug class we just paid for.

**Weighting:** reach 3 × severity 2 = **6** · council leaning: `build`
(keep TOP, finish the migration; a paradigm half-adopted is where the seams
live, and the seams are where the bugs lived)

## Verdict offered to Julio

TOP fits this domain the way the Vademecum claims: a D&D character IS layered
semantics, and the recovery measured the fit. The costs are real but
concentrated in tooling and in the unfinished migration, not in the paradigm
itself. The recommendation is not "adopt TOP" (done) but "stop straddling":
every remaining legacy seam is rent paid twice.

## The paths (proposed sequencing, QST-0035 refined)

1. **Ship the beta on the seam we have** (Decree 0006, running): finish the
   bootstrap exit; wire the class descriptions through Describe_Layer.
2. **Re-ratify the doctrine** (QST-0036 residue, small): resync
   TagKit-Doctrine.md to the pinned Guide's vocabulary; Julio ratifies.
3. **Audit the kits against the Guide** (QST-0042, claimed by Claude): every
   `*Kit` checked for pre-sync assumptions; `Kit_of_*` modules that are not
   TOP kits renamed or documented; findings as a report, not silent edits.
4. **Skills and tools become Tags** (QST-0047, promoted by the Ranger crash):
   deletes the string-surgery bug class; unlocks per-skill contracts.
5. **Features, then Spells, on TOP** (QST-0020, QST-0031): the trains exist;
   the universal Chip/Entry grant contract in Current-State is the bridge.
6. **Character root and composition root** (QST-0016, QST-0027/0074): one
   Character substrate, one Summoning API as the public algebra, `app.main`
   as its one composition root. This is where "API-like architecture" lands.
7. **TOP tooling as a standing citizen**: the static bytecode gate and a
   process-isolated self-test runner graduate from recovery scratch tools to
   `scripts/`; if kit re-registration in one process is ever needed, that is
   a Suggest-to-TagKit questa, never a local patch.

## Open questions for Julio (Vox)

1. Does the doctrine resync (path 2) get its own decree, or ride QST-0042?
2. QST-0018 wants AtlasTOP removed; the doctrine calls AtlasTOP our layer on
   top of TagKit. Which is current law? (The accident resurrected an
   AtlasTOP directory in the main checkout as debris, so the answer decides
   a deletion.)
3. Is path 4 (skills as Tags) beta-blocking in your judgment, or the first
   post-launch train? The crash it prevents is already patched point-wise.
