# Agentos Reference and POI Documentation

## Desk

- purpose: integrate Agentos project infrastructure, Skw resolution, and cross-project references through concrete usage cases
- state: active
- current focus: POI documentation discovery
- related design: `notes/live/596-poi-linter-system-design-session.md`
- durable targets: `skills/agentos-pkg/design/107-design.md` and the owning subsystem indexes

## Design Principle

> `Agentos.Reference` performs deterministic lookup through local and global registrations. Failure or ambiguity produces a structured POI, after which an agent may discover the target and repair the registry.

- registry resolution is shared Agentos infrastructure
- domain systems decide which resolved targets are engaged or visible for an operation
- agents may repair missing mechanical knowledge by registering discovered relationships
- deterministic failure must remain inspectable rather than falling through to an implicit filesystem search

## MVP Usage Cases

1. **POI documentation**: resolve `POI.Class` to its owning package and then to its documentation through `Skw.Address.Schema`
2. **Cross-package Skw address**: resolve `@chatlas-pkg/Some.Block` from one package into another registered package
3. **Index dependency**: resolve `Index.Depot.Dependency: agentos-pkg` to its registered depot without hardcoded filesystem knowledge
4. **Agentos project reference**: resolve a registered `Agentos.Project` across projects while preserving the nearest project as local context
5. **Mechanical failure and repair**: surface missing, stale, or ambiguous references as POIs carrying the attempted identity, search scope, and registries checked

## Usage Case 1: POI Documentation

### Target Journey

```text
POI.Instance
  -> POI.Class identity
  -> owning Package.Skill
  -> package POI.Catalog
  -> POI.Class block
  -> POI.Documentation entrypoint
  -> linked Skw surfaces
```

### Working Statements

- [PR] every `POI.Class` and its documentation are owned by the natural `Package.Skill`
- [CT] every `POI.Documentation` entrypoint is contained in the owning `Package.Skill` index
- [CT] the package index exposes POI classes through its dedicated `poi` chapter
- [CT] the `POI.Class` block is the canonical indexed entrypoint for the class description and evaluation protocol
- [FR] deeper documentation may span additional Skw-addressable surfaces explicitly linked from that entrypoint
- [PR] package ownership keeps domain knowledge in its natural placement while common Agentos tooling handles discovery
- [RJ] a linter does not own or hardcode the filesystem location of the documentation for the classes it emits

### Resolution Boundary

- `Agentos.Reference` resolves the owning package through local and global registrations
- package and index machinery determines the engaged catalog and resolves the class block
- Skw machinery follows documentation addresses from the class block
- POI tooling composes those results but introduces no separate package, depot, or address resolver

### Questions To Revisit

- what stable identity names the owning `Package.Skill` in a `POI.Class` reference?
- which local and global surfaces register package identity to location?
- how does a command establish the set of engaged package catalogs?
- which resolution failures become distinct `POI.Class` values?
