# Chat.Grounding.Material.Catalog

The maintained, ever-growing list of criteria for detecting `Chat.Grounding.Material` — the core L1 job. `Cited.Duplication` of `[Chat.Grounding.Material, Chat.Grounding.Material.Catalog]` from `agentos-chatlas-pkg/design`; the index owns authority.

`Chat.Grounding.Material` is a chat turn (or turn span) carrying durable design signal worth grounding. Detection requires no named block; block-agnostic material is still recorded, because it may ground blocks discovered later. One turn can yield multiple records.

This catalog is **never assumed complete**. It refines from a high-signal feedback sample: turns actually approved into a `### grounding` section show what real grounding material looked like — fold those back into the positives below.

## Positive criteria — record it

A turn is `Chat.Grounding.Material` when the user (priority) or agent:

- adds durable design information
- makes or accepts a decision
- corrects direction or an agent's framing
- rejects an approach or idea
- names or renames a concept
- states a stable requirement or preference
- says something should be reused later
- explains why a block should exist or split
- marks current behavior as drift (a `Grounding.DRIFT` candidate)

User turns are primary signal. Assistant turns are context, reasoning trace, and forensic detail; unaccepted assistant-only grounding must be labeled `ASSISTANT` under `Grounding.Hugentic.Authority`.

## Negative criteria — skip it

- pure mechanics: tool invocations, status pings, "ok", "continue", "next"
- agent narration the user never engaged with
- material already recorded for the same turn `ref` — dedup, do not re-append
- transient scaffolding: planning chatter that later turns superseded without a decision
- a turn that only *mentions* a concept without establishing anything about it

## Judgment

- detection is heuristic, not exhaustive: a miss is a recoverable gap, never corruption — chats stay the SSOT.
- when unsure, lean toward recording with a candid `grounding-why` (e.g. `weak: ...`) rather than dropping; the reviewer is the gate.
- the goal is coverage convergence across passes, not a perfect single sweep — `Chat.Surface.Closure`.
