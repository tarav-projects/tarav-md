# Archive DOI contracts and maintenance authority

<!-- tarav.sessions
0f5bad01 = codex:01a15483-94e8-7fe0-86ad-ddd83e2bae52 @0f5bad0131260477b4cf3d712a95871496c3db92d67eaa7910243e312f7b552a
-->

## Impl.Abstract

Status: ready for implementation; design only. Knowledge.Surface: wiki.

Clarify Archive's maintenance boundary in the Constitution and align the Archive
candidate design with the minimal typed DOI registry. This is the Markdown-owned
companion to [Python request 942](../../../tarav-py/notes/live/942-archive-doi-registry-impl-req.md).
<!-- tarav.breadcrumb 4567ca40d078 -->

## Design

External Artifacts are immutable from Archive's maintenance perspective: Archive
does not own or mutate their shape. Their owners may change them while a DOI
continues identifying the same resource under its declared Type contract. Archive
does own and maintain DOI Records, locators, hints and schemas. Stricter exact-state
Types remain possible; do not weaken existing exact-commit reference contracts.
<!-- tarav.breadcrumb 68f78b984c61 -->

DOI lookup returns a typed maintained object. Locators are information about where
to reach its resource; compact hints help assess identity. Maintainers explicitly
declare location changes. Consumers perform access and decide what observations
mean. This first implementation excludes artifact hosting, fetching, automatic
recovery and a universal identity-validation service.
<!-- tarav.breadcrumb 44f9bafff952 -->
<!-- tarav.breadcrumb eb8d8f246b5b -->

Update authoritative sources in `.tarav/skillware/skills/tarav-pkg/src/`, then
rebuild the deployed skill products. The Constitution source is
`CONSTITUTION.skw.json`, block `tarav-archive`
(`38446ee9-911e-44c3-a85f-74bdfa5ab8dd`). It currently says changed Artifacts
always require another Artifact; clarify that assertion in terms of declared
identity contracts and Archive's maintenance authority. Preserve the rule against
silently substituting an unrelated resource or violating a strict contract.

The candidate `tarav-archive.skw.json` currently describes hosted repositories,
append-only locator sidecars, raw Git commit metadata, automatic exact-file
materialization and derived identities. Replace those current implementation
claims with the bounded registry design specified in request 942. Retain older
discussion in Git and Wiki; no parallel legacy product or fallback reader.

## Impl.Req.Wiki

Owner: `tarav-md`; Wiki: `notes/wiki/`. Existing topic:
`archive-doi-registry.md`; daily: `daily/2026-10-22.md`. The current pass appends
the supported discussion and cross-links these requests. Exact session identity
and provisional support are declared above; submit/audit through the shared
Breadcrumb workflow. Do not present a proposed code schema as verbatim User review.

## Execution.Plan

- [ ] Documentation change: edit the constitutional Archive block through SKW,
  preserving unrelated constitutional content. Check: compiled diff expresses
  maintenance authority and typed identity contracts, without weakening strict
  references or authorizing artifact mutation.
- [ ] Documentation change: replace the candidate Archive description with the
  registry scope, typed DOI semantics, locators/hints, and consumer boundary.
  Check: source/product rebuild, SKW checks and generated-product diff.
- [ ] Capture/verification: attach justified source Breadcrumbs, run skill checks
  and capture the actual implemented outcome to Wiki. Check: Breadcrumb audit and
  focused generated-product consistency checks; report observed results.

No Python implementation, artifact migration or Notebook commit automation is
part of this companion request. Execute it before request 942's Python replacement.

## Impl.Log

- Design prepared from the current user discussion. Authoritative source block
  and candidate document inspected. No Constitution or skill product edited.
- Markdown start checkpoint: `f1b094513253de84ec23b12d400db1d27b582193`.
- Four request Breadcrumbs submitted and audited without POIs. The topical
  and daily Wiki additions were also submitted and audited successfully.
  Relative links resolve; the Markdown diff whitespace check passes.
- Companion ready for execution; no authoritative source or product changed.
