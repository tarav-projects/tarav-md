# Impl.Req Example

> $kw: --derived --from references/impl/design.skw.md#Impl.Req Artifact --from references/impl/design.skw.md#Impl.Agendix
> --intent one minimal concrete artifact instantiating the spec's
> --cont structure, including the Impl.Agendix reservoir; adapt wording and weight to the request

Adapt the wording and section weight to the current request.

```md
# Project Configuration - impl-req

## Impl.Abstract

- **scope:** add project-scoped configuration loading without changing global defaults
- **status:** ready for implementation
- **source:** direct user request plus current repository inspection
- **support set:** ordering turn ^c<YYYYMMDD>-<N>u, readiness approval ^c<YYYYMMDD>-<M>u (chatlas anchory)

## Impl.Agendix

- **touched (index):** `Project.Boundary` — the resolution seam the loader must honor ^c<YYYYMMDD>-<N>u
- **touched (chat):** override-scope decision — project values win only for the active command ^c<YYYYMMDD>-<P>u
- **structural:** none — no surface is derived from another in this change
- **open space:** cache/reload behavior has no index home yet — left provisional, unanchored

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
