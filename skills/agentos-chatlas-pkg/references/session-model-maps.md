# Session.Model.Maps — format & principles

The authoring and reading guide for `Session.Model.Map` files (see index concept
`Session.Model.Map`). One map per provider: `session-model-map-<provider>.md`.

A map records how a provider's native session concepts reach `Chatlas.Session.Model`
neutral concepts — and, crucially, keeps the neutral model under constant pressure
against the provider's real data. The map is where each native structure is tested:
*can `Chatlas.Session.Model` encode this with equivalent semantics, or not yet?*

## What a map is (and is not)

- it maps native → neutral; it does **not** define neutral concepts (those live in the
  index — one-directional: index is SSOT, the map cites and maps, never redefines)
- it is an **index into evidence**, not a body of claims. Every mapping points at a real
  artifact you can open and verify; the map's prose only tells you where to look
- it is decision-and-rationale-centric, not a restatement of the normalizer code. If the
  field mapping is obvious and the code already does it, no row — restating code is
  redundant placement and drifts
- it is a current-truth document. Freshness comes from re-checking against evidence, not
  from annotations. Git holds history; no version/status metadata blobs in the file
- it is a `Stable.Surface` — it never references a live-note (local, non-stable). The
  dependency is one-directional: a design session (a live-note) references the maps, never
  the reverse. Open concepts are named (`TBD: <candidate>`), not linked to a session file

## Evidence philosophy — artifacts over source

Priority: **raw artifacts > source code.**

- the raw artifacts in `~/Documents/chatlas/raw/<provider>` are the hard evidence — what
  the provider *actually wrote* in this dataset
- provider source code (the harness) is interpretive only — what it *could* write and what
  the fields *mean*. Use it to understand the artifacts, never as the primary claim
- when source and artifacts disagree, **artifacts win**. Repeated lesson: source said
  Codex stopped persisting `exec_command_end` (archive had 422 sessions of it); source
  lists Claude `agentId`/`isSidechain` record fields (archive has 0)

We do not trust summaries. A summary is an index telling you where the evidence is — it is
never the evidence. "Give me the evidence; I check it myself if I want to know."

- no passive states — never "ok", "validated", "pending". A claim is a pointer to data
- a mapping exists only when grounded in a real artifact
- a concept the source describes but the dataset lacks is recorded as a **verifiable
  zero-count** in `# Absent in dataset`, with the probe to reproduce it — absence is
  evidence, not silence

## Reference format

Form: `<commit>/<artifact-file>/<line-range>` within the `~/Documents/chatlas` git repo.

- the archive is git-tracked; raw artifacts are overwritten in place, so the **commit
  short-hash pins the version** — a path + line alone is not reproducible
- define file anchors once in `# Index` → `## Sources`, each `<anchor> = <commit>/<path>`,
  then cite as `<anchor>:<line>` (e.g. `S1:6`, `S2:467`)
- verify any reference with `git -C ~/Documents/chatlas show <commit>:<path>` at the line
- quote the actual record inline (long strings truncated with `…`, content arrays
  summarized as block types) so the reader sees the data, then can open the source for full

## File structure

Section-based and append-friendly — never a table (tables are unreadable in raw markdown
and hostile to appends). Two parts: an `# Index` of reusable blocks, then an append-only
`# Mappings` tail, then `# Absent in dataset`.

```
# Session.Model.Map — <Provider>
<header: provider/normalizer, evidence priority, archive root>

# Index
## Legend            — neutral-target notation; the "only non-obvious" rule
## Sources           — file anchors (commit + path), referenced by seen: lines
## <Provider>.<Entity>   — reusable native-entity envelopes (e.g. the record envelope,
                           the system-record shape) that mapping records reference

# Mappings           — append-only; one section per native concept
## <native concept>
- seen:     <anchor:line> → <real record, trimmed> [+ corpus count]   ← hard evidence
- native:   <semantic meaning, source cite>                           ← interpretive
- neutral:  <mapping, per the controlled vocabulary>
- rationale: <the decision and why; version nuance as prose when it carries weight>

# Absent in dataset  — source-described concepts with verifiable 0-counts + the probe
```

Subtyped native records use `## <record> / <subtype>` (e.g. `## system / compact_boundary`).

## The record schema

Four lines, in evidence order:

- **seen:** the pointer + data. `<anchor:line> → <trimmed record>`, plus a corpus count
  (`present in N/<total> sessions`) when it adds weight. This line is the hard evidence
- **native:** what the native concept means, with a source-code cite (`file:line`).
  Interpretive — ranked below `seen:`
- **neutral:** the mapping, using the controlled vocabulary (below)
- **rationale:** the decision and its reasoning — why this neutral target or `→ native`,
  what the artifact reveals that the source name obscured, any version nuance as prose

## Controlled vocabulary (neutral column)

The neutral side is constrained so the cross-provider slice is pivotable (one neutral
concept → every provider's source for it):

- `Concept` — a settled index concept (e.g. `Session.Lineage`, `Session.Identity`)
- *proposed* — a neutral concept not yet designed; pending the session-model design
- `→ native` — survival decision: stays provider-specific in `native` / `source_refs`,
  recoverable but never canonical
- `TBD: <candidate>` — open gap; names the candidate neutral concept to be designed and
  promoted to the index (a stable concept name, never a live-note reference)

The survival rule (from `Chatlas.Session.Model`): a native concept survives canonically
iff it maps to a neutral concept; otherwise it goes to `native`. The map is where that
rule is applied, one native concept at a time.

## Only non-obvious mappings

A record exists only for a non-obvious or decision-bearing mapping. State the omitted
obvious 1:1s once in the `## Legend` (role user/assistant, plain text content, basic
tool-call/tool-result, visible reasoning) so the omission is deliberate, not a gap.

## The map drives the design

The map's `TBD` rows are the live question queue for the session-model design: bottom-up,
each unresolved native concept raises a design question; top-down, each settled neutral
concept fills the neutral column across every provider map. The map and the model
co-evolve, and the map's `# Absent in dataset` section keeps the design honest about what
provider data actually exists versus what a source merely describes.

See `session-model-map-claude.md` for the worked example.
