# Design Index Session Refactor - impl-req

## Impl-Req State

Implemented: active `agentos-design-session` references now use `Design.Index`; obsolete active `Session.Index` / `Session.Docs` references were removed.

## User Intent

Refactor the `agentos-design-session` skill so the conceptual surface is `Design.Index`, composed of H3 `Design.Index.Block`s.

Remove obsolete references rather than keeping legacy aliases or deprecated active files.

## Why This Exists

The design-session model now treats `Design.Index` as the conceptual background of the current design session.

`Design.Index.Block` captures the relevant conceptual value produced by session discussion about a subject concept. It is a session-local `Complete.Index.Block` with fundamentals, `### appendix`, and `### meta`.

## Current Situation

The active skill still uses the older split:

- `Session.Index` for compact conceptual fundamentals.
- `Session.Docs` for long-form conceptual explanation.

This no longer matches the indexed `Design.Index.Block` model.

## Requested Change

Update the active `agentos-design-session` skill package to replace `Session.Index` and `Session.Docs` with `Design.Index`.

Use H3 concept blocks under `## Design.Index`:

```md
## Design.Index

### Concept.Name

- fundamentals with the same semantic role as `Index.Block` fundamentals

#### appendix

- rationale, examples, pressure tests, tradeoffs, rejected alternatives, design depth

#### meta

- status, sources, open questions, promotion notes, stale or misaligned markers
```

Remove obsolete active reference files instead of preserving legacy compatibility.

## Constraints And Invariants

- `Design.Index` concept blocks use H3 under the H2 `## Design.Index` section.
- Do not leave active `Session.Index` or `Session.Docs` terminology.
- Remove `session-index.md` and `session-docs.md`; do not deprecate them in the active skill package.
- Keep `Session.Abstract`, `Session.Notes`, and `Session.Log`.
- Keep `InChat.Session` as the default backend.
- Keep `Artifact.Session` as a user-gated upgrade.
- Keep `Impl.Req` as an on-demand handoff.
- Do not describe promotion to the Agentos Index as the primary purpose of `Design.Index`.
- Preserve user-gated artifact writes and `agentos-index-writer` gates for index writes.

## Out Of Scope

- Do not implement broader Agentos Index changes.
- Do not create or update durable index notes unless a separate `agentos-index-writer` flow is explicitly triggered.
- Do not add legacy aliases for `Session.Index` or `Session.Docs`.
- Do not alter deprecated snapshots except if needed to keep repository mechanics clean.

## Acceptance Signals

- `rg "Session\\.Index|Session\\.Docs" skills/agentos-design-session` returns no active matches.
- `skills/agentos-design-session/references/session-index.md` is removed.
- `skills/agentos-design-session/references/session-docs.md` is removed.
- A new `skills/agentos-design-session/references/design-index.md` defines `Design.Index` and `Design.Index.Block`.
- `SKILL.md` routes `Design.Index` section work to `references/design-index.md`.
- In-chat and artifact session references show `Design.Index` instead of the old split.
- Consolidation and capture guidance target `Design.Index` blocks, fundamentals, `appendix`, and `meta`.

## Implementation Shape

Vertical slice 1: introduce `Design.Index` reference.

- Add `references/design-index.md`.
- Define `Design.Index` as the conceptual background of the current design session.
- Define `Design.Index.Block` structure and writing guidance.
- Check by reading the new reference in isolation.

Vertical slice 2: update backend shapes.

- Update `inchat-session.md` to print `Session.Abstract` and `Design.Index`.
- Update `artifact.md` and `artifact-session.md` to use `Session.Abstract`, `Design.Index`, `Session.Notes`, and `Session.Log`.
- Check by searching those files for `Session.Index` and `Session.Docs`.

Vertical slice 3: update router and behavior references.

- Update `SKILL.md` section routing from `Session.Index` / `Session.Docs` to `Design.Index`.
- Update `capture-audit.md`, `uncommitted-work.md`, `impl-req.md`, and `session-notes.md`.
- Check active skill package with `rg "Session\\.Index|Session\\.Docs"`.

Vertical slice 4: update consolidation guidance and remove old files.

- Rewrite `consolidation-plan-example.md` around `Design.Index.Block` targets.
- Remove `references/session-index.md` and `references/session-docs.md`.
- Check active file list and verify no references point to removed files.

## Relevant Files Or Surfaces

- `skills/agentos-design-session/SKILL.md`
- `skills/agentos-design-session/references/inchat-session.md`
- `skills/agentos-design-session/references/artifact-session.md`
- `skills/agentos-design-session/references/artifact.md`
- `skills/agentos-design-session/references/capture-audit.md`
- `skills/agentos-design-session/references/consolidation-plan-example.md`
- `skills/agentos-design-session/references/impl-req.md`
- `skills/agentos-design-session/references/session-notes.md`
- `skills/agentos-design-session/references/uncommitted-work.md`
- `skills/agentos-design-session/references/session-index.md` (remove)
- `skills/agentos-design-session/references/session-docs.md` (remove)
- `notes/index/114-Agentos.Index.Notes.md`

## Open Questions

- None for implementation. Use the model stated in this request.

## Related Impl-Reqs

- None.

## End Log

- 2026-05-12: Created from design-session discussion after settling that old `Session.Index` / `Session.Docs` surfaces should be replaced by `Design.Index`.
- 2026-05-12: Implemented in `skills/agentos-design-session`: added `references/design-index.md`, updated active router/backend/audit/consolidation/handoff guidance to `Design.Index`, and removed `references/session-index.md` and `references/session-docs.md`. No broader index-note changes were made.
