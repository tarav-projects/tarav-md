# Impl.Req Example

Adapt the wording and section weight to the current request. Placeholder anchors below become exact grounded anchors through the normal one-manifest capture workflow; do not hand-author its intermediate records.

```md
# Project Configuration - impl-req

## Impl.Abstract

- **scope:** add project-scoped configuration loading without changing global defaults
- **status:** ready for implementation
- **source:** direct user request plus current repository inspection
- **support set:** exact typed lines in `Impl.Index`; the artifact does not maintain a second grounding reservoir

## Impl.Index

### Project.Configuration.Scope

- [CT] Project configuration is loaded from the resolved project root. ^d<YYYYMMDD>-<N>u
- [DR] Project values override global defaults only for the active command. ^d<YYYYMMDD>-<P>u
- [BL] Unrelated configuration behavior remains out of scope. ^d<YYYYMMDD>-<M>u

## Execution.Plan

### Slice 1 - Load project configuration

- add project-root configuration discovery through the existing project boundary
- observable: a command run in a configured project receives the project value
- check: boundary test fails before implementation and passes afterward
- status: not started

### Slice 2 - Preserve default behavior

- verify commands outside configured projects retain global defaults
- observable: existing default behavior is unchanged
- check: relevant existing tests pass
- status: not started

## Impl.Log

- [TS] Execution was authorized by the cited `--exec` invocation. ^d<YYYYMMDD>-<K>u
- no deviations or blockers
```
