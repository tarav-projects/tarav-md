# Index.Edit.Session

## Context

The current public distinction between `--capture`, `--enrich`, and `--edit` asks the user to select implementation-level behavior that the agent can infer from the conversation and the state of the `Touched.Index`.

The user should not need to decide whether relevant material already exists in the chat, further discussion is needed, or a concrete edit is ready. These are axes of the same Index-related workflow rather than separate workflow identities.

## Working Design

`Index.Edit.Session` is the single Hugentic workflow for discussing, designing, grounding, and landing an Index update.

Its canonical public entry is:

```text
/tarav-hugentics --index [optional focus]
```

On entry, the agent becomes an expert on Index writing, grounds the current conversation against relevant Index state, and uses a semantic router to choose the appropriate direction. When several coherent targets or directions exist, it may begin with a compact routing report; when the next move is evident, it should proceed without adding routing ceremony.

The session may operate across several orthogonal axes:

- material source: existing chat content, newly elicited content, or adjacent evidence
- intent: understand, discuss, design, reconcile, or update
- change: add, revise, remove, demote, or ground
- target: existing block, new block, appendix, or agendix
- standing: grounded, presumed, contradictory, or stale
- maturity: exploring, drafting, approval-ready, approved, or landed

The session can cross these axes continuously without switching workflows.

## Focus Directives

`--capture`, `--enrich`, and `--edit` are optional focus directives under `--index`, not aliases and not independent workflows:

```text
/tarav-hugentics --index --capture [optional focus]
/tarav-hugentics --index --enrich [optional block]
/tarav-hugentics --index --edit [optional target]
```

- `--capture` emphasizes material already produced in the conversation.
- `--enrich` emphasizes generating further touched material around an Index block.
- `--edit` indicates that a concrete change is already understood.

Absent a directive, the semantic router infers the appropriate combination from the conversation and Index state. Directives establish starting focus but do not bypass contextualization, grounding, discussion, approval, landing, reconciliation, or lint gates.

No compatibility aliases are required. Additional directives may be introduced later when they express useful axes without creating new workflow identities.

## Boundary

This consolidation concerns Index edition work. Read-only research and deterministic checks have materially different intent and may remain separate calls such as `--search` and `--check`.

