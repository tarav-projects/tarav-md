---
name: chatlas-session-model-mapper
description: Operational workflow for the Session.Model.Map loop — mine a provider's native session concept from the Chatlas raw archive, ground it as a map row, pressure it across providers, and decide whether it becomes a neutral Chatlas.Session.Model concept or stays native. Use when adding or resolving session-model map rows, designing neutral session concepts from real provider data, or maintaining session-model-map-<provider>.md files.
---

# Chatlas Session Model Mapper

Operational `Package.Aux.Skill` under `agentos-chatlas-pkg`. It drives the
`Session.Model.Map` loop: turning what providers actually wrote into accepted
`Chatlas.Session.Model` neutral concepts, one concept at a time, under continuous
pressure from real data.

This skill owns the **workflow**. The **format and principles** live in
`agentos-chatlas-pkg/references/session-model-maps.md` — read it first; do not duplicate
it here. The worked example is `session-model-map-claude.md`.

## Core philosophy — artifacts over source

- the hard evidence is the raw archive at `~/Documents/chatlas/raw/<provider>` — what the
  provider *actually wrote* in this dataset
- provider harness source (`~/Documents/workspaces/main-workspace/harnesses/<provider>`) is
  interpretive only — what it *could* write and what fields *mean*
- when source and artifacts disagree, **artifacts win**
- we do not trust summaries: every claim is a pointer to a real record you can open. No
  passive states; a concept absent from the dataset is recorded as a verifiable zero-count

## Trigger Boundary

Use this skill to:

- mine a new native session concept from the raw archive and add a map row
- resolve a `TBD:` row — design its neutral concept or decide `→ native`
- run the cross-provider pressure check before accepting a neutral concept
- maintain `session-model-map-<provider>.md` files

Do not use this skill for:

- retention decisions (that is `agentos-chatlas-retention-audit`)
- normalizer or standard-model code changes — those are a deferred `Impl.Req`, not part of
  the design loop
- general session lookup, export, or transcript work

## Sources

- raw archive: `~/Documents/chatlas/raw/<provider>` (git-tracked; the hard evidence)
- harness source: `~/Documents/workspaces/main-workspace/harnesses/<provider>` (interpretive)
- stable surfaces: the chatlas index (`Chatlas.Session.Model`, `Session.Model.Map`, settled
  neutral concepts) and the map files under `agentos-chatlas-pkg/references/`
- the normalizer under audit: `agentos-chatlas-py/src/agentos_chatlas/session_model/_<provider>.py`

Use `scripts/probe-archive.py` to mine the archive — it emits a ready-made `seen:` line
(commit hash + file + line + trimmed record + corpus count) so the reference format is
correct every time.

## Workflow

The unit of work is **one map row → one decision**. Never batch.

### 1. Mine — ground a row in artifacts

- pick a native concept (a record kind, field, or marker)
- run `scripts/probe-archive.py <provider> <pattern>` to get its `seen:` line and count
- if present: write the row — `seen:` (the probe output), `native:` (harness source meaning,
  `file:line`), `neutral: TBD: <candidate>`
- if absent (zero-count): record it under `# Absent in dataset` with the probe, not as a row

### 2. Surface — pick one TBD row

- choose the highest-leverage unresolved row
- the row is the question; state it from its `seen:` evidence

### 3. Cross-provider pressure — the acceptance gate

- probe the *other* providers' archives for the same or analogous concept
- present in ≥2 providers → a neutral concept is justified
- single-provider only → likely `→ native`, or **hold** until a second provider appears
- this gate prevents overfitting the model to one provider

### 4. Discuss

- pressure the candidate against the real `seen:` records from every provider
- settle: definition, what it carries, boundaries, and the survival decision
- keep testing the concept against actual records, not source descriptions

### 5. Decide

- **accept neutral** → becomes an index concept
- **→ native** → no concept; stays provider-specific in `native`/`source_refs`
- **hold** → leave the row `TBD:`

### 6. Execute — gated writes to stable surfaces only

- if accepted: write the concept as a `Kernel.Block:Index` into the chatlas index, and
  update the routing table
- update **every provider map row** naming the candidate: `TBD: <candidate>` → the real
  index concept name — all maps in lockstep
- if `→ native`: set the row's `neutral:` to `→ native` with rationale; no index write
- show proposed text before writing; index and map writes are user-gated

### 7. Handoff — deferred code (separate phase)

- only after a concept is accepted, an `Impl.Req` (via `hugentics-impl-designer`) updates
  the normalizer + standard-model contract to emit it
- design acceptance and code implementation never fuse

### 8. Repeat

- new artifacts and providers add rows; resolved rows update map + index; the model stays
  under continuous pressure

## Constraints

- artifacts beat source; never assert a mapping the archive does not show
- references use `<commit>/<file>/<line>` against the `~/Documents/chatlas` git repo
- the map files are a `Stable.Surface` — they never reference a live-note; name candidate
  concepts (`TBD: <name>`), do not link a design-session file
- one concept at a time; run the cross-provider gate before accepting any neutral concept
- record absence as a verifiable zero-count, never as silence or a passive state
- do not touch normalizer code in this skill — that is a deferred `Impl.Req`
- index and map writes are user-gated; show exact proposed text first

## Response Shape

While running the loop:

- the row under work and its `seen:` evidence
- the cross-provider result (shared / single-provider / held)
- the decision and its rationale

At a write:

- the exact index block and/or map row changes proposed
- which provider maps update in lockstep
- whether a follow-on `Impl.Req` is now warranted
