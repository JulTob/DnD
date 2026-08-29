# Decree 0006 — The beta is the character generator

- **Issued by:** Julio, in chat, 2026-08-29 (the recovery session)
- **Recorded by:** Claude, same day
- **Related:** QST-0072 (post-accident recovery) · QST-0073 (beta entrypoint and scope) · QST-0074 · QST-0075

---

## The decision

The public beta launches as **a character generator, and nothing else**.

Julio's words, condensed: because of the accident (and partly thanks to it), the beta ships only the character generation service. Every other wing of the application (NonPlayer generation, lists, the Magistratum, the adventure tools) waits. The team focuses on three things:

1. **Aesthetics.** The sheet and the app must look like a work of craft.
2. **Brand.** One voice, one identity, recognizable at a glance.
3. **The service itself.** Character generation must be perfect, organized, and scalable.

## The method

- **No hacks, no tricks, no shortcuts.** Everything on the beta path gets reviewed. Improvement is welcome where the review finds the chance.
- **Short run: the app works as intended.** TOP/TagKit remains the design engine of the project, but the refactor toward it never blocks the beta. A dedicated refactorization follows the launch.
- **Design choices are stated in the project's files.** A choice that lives only in a chat log does not exist. Decrees record decisions; Questae record work and rationale.
- **Death of the Author stands** (see `Documenta/Canon/Elves-and-the-Dreaming.md`): the lore is for the design team, not for the user. User-facing text invites and inspires; it never lectures. The responsibility of making sense belongs to the user's imagination.

## Consequences

- The served entrypoint, page scope, and review priorities follow QST-0073.
- Restoring the modular composition root (`app.main`) is post-beta work: QST-0074.
- Restoring the NonPlayer public surface is post-beta work: QST-0075.
- Recovery of damaged modules (QST-0072) continues, prioritized by what the character generator actually imports.
