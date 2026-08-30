# Impl.Req Example

Adapt section weight to the implementation. The live note coordinates Agent
work; the referenced Diagram Block independently retains supported
User-Touched Lines.

```md
# Project Configuration — Impl.Req

## Impl.Abstract

- **scope:** add project-scoped configuration loading without changing global defaults
- **status:** ready for execution
- **source:** direct User request plus current repository inspection

## Impl.Req.Diagram

- **namespace:** User.Touched.Chatlas.Index / <namespace-uuid>
- **model:** Project.Model / <model-ship-uuid>
- **block:** 502.Impl.Req / <block-ship-uuid>
- **block type:** Impl.Req.Block

The Block contains the supported User-Touched constraints and decisions for
this request. Render it from the Diagram; do not duplicate its Lines here.

## Execution.Plan

### Slice 1 — Load project configuration

- add discovery through the existing project boundary
- observable: a command in a configured project receives the project value
- check: boundary test fails before implementation and passes afterward
- status: not started

### Slice 2 — Preserve default behavior

- verify commands outside configured projects retain global defaults
- observable: existing default behavior remains unchanged
- check: relevant existing tests pass
- status: not started

## Impl.Log

- no deviations or blockers
```

The associated `502.Impl.Req` Block may contain supported Lines such as:

```text
[CT] Project configuration is loaded from the resolved project root.
[DC] Project values override global defaults only for the active command.
[FR] Unrelated configuration behavior remains outside this request.
```

Those Lines are ordinary Diagram Annotations with producer, rooted Support.Set,
Line.Type, and Assertion state. They are not Markdown-owned Index records.

