# Impl.Req Example

> $kw: --derived --from references/design.skw.md#Impl.Req Artifact
> --intent one minimal concrete artifact instantiating the spec's
> --cont structure; adapt wording and section weight to the request

Adapt the wording and section weight to the current request.

```md
# Project Configuration - impl-req

## Impl.Abstract

- **scope:** add project-scoped configuration loading without changing global defaults
- **status:** ready for implementation
- **source:** direct user request plus current repository inspection
- **support set:** ordering turn ^c<YYYYMMDD>-<N>u, readiness approval ^c<YYYYMMDD>-<M>u (chatlas anchory)

## Impl.Index

### Project.Configuration.Scope

- project configuration is loaded from the resolved project root
- project values override global defaults only for the active command
- unrelated configuration behavior remains out of scope

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

- execution gate: `--exec` invocation anchored ^c<YYYYMMDD>-<K>u
- no deviations or blockers
```

> $kw. end
