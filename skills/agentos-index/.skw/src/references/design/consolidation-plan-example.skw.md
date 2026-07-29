# Consolidation Plan Example

This detailed product-design module is owned by `agentos-index --design`.

> $kw: --dev-from references/index-context-assembly.skw.md

Use this example when the user asks how to capture, consolidate, or apply convergence from the current discussion.

The response should show what the user is being asked to approve. It should name files when files exist, name backend/surfaces when no file exists, list concepts or material to update, and explain why each target is appropriate.

## Example Shape

```md
Here is how I would consolidate the current alignment.

Consolidation plan:

- File: `notes/live/NNN-topic-design-session.md`
  Section: `Design.Index`
  Concepts to update:
  - `Concept.One`: update fundamentals with the boundary around [specific point].
  - `Concept.One` / `appendix`: add rationale for [decision] and pressure argument around [tradeoff].
  - `Concept.Two` / `meta`: mark [open question, stale assumption, or alignment issue].
  Why: these are concept-level results from the discussion.

- File: `notes/live/NNN-topic-design-session.md`
  Section: `Session.Notes`
  Material to park:
  - [open question]
  - [stale assumption]
  Why: useful, but not settled.

- File: none
  Surface: `Impl.Req`
  Action: do not create yet.
  Why: this is design convergence, not implementation handoff.

- File: none
  Surface: Agentos Index
  Action: no write.
  Why: possible promotion candidate only; index writes require the Agentos Index workflow.

Recommendation:
Approve the `Design.Index` update first.

Approval request:
OK to draft the exact update for:
- `notes/live/NNN-topic-design-session.md` / `Design.Index`
```

## InChat Variant

When no artifact exists, show backend/surface instead of file:

```md
Here is how I would consolidate the current alignment.

Consolidation plan:

- File: none
  Surface: `Alignment.Backend::InChat::What` / `Design.Index`
  Concepts to update:
  - `Concept.One`: refresh fundamentals around [specific point].
  - `Concept.One` / `appendix`: add rationale for [decision] and pressure argument around [tradeoff].
  Why: this is the conceptual result of the discussion.

- File: none
  Surface: `Alignment.Backend::Artifact::What`
  Action: optional upgrade.
  Why: use this only if the user wants the current alignment persisted.

- File: none
  Surface: `Impl.Req`
  Action: do not create yet.
  Why: this is design convergence, not implementation handoff.

Recommendation:
Refresh `Alignment.Backend::InChat::What` / `Design.Index` first.

Approval request:
OK to draft the exact in-chat consolidation?
```

## Approval Discipline

- A consolidation plan is not implementation.
- A consolidation plan is not permission to write artifacts.
- If exact wording has not been shown, approval authorizes drafting the update, not committing it.
- Artifact writes still require the active artifact user gate.

> $kw: --from Impl.Req
