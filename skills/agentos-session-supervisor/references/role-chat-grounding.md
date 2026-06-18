# Supervisor.Role: Chat Grounding

`role-chat-grounding` is an additive `Supervisor.Role` for mining `Chat.Grounding` material from an observed target session.

The role watches the transcript for turns that materially ground durable concepts, design blocks, index entries, implementation requests, or future alignment decisions. It proposes references and use-sites. When the user asks it to write, it may append `Grounding.Request` records to the global Chatlas grounding depot. It does not write the index, mutate the target session, or decide canonical design truth.

This role delegates grounding mechanics to `chatlas-grounding-agent`. Load that skill before producing or writing grounding output. Treat this file as the supervisor integration layer: it says when the supervisor applies the grounding lens and how it composes with the supervision brief; `chatlas-grounding-agent` owns `Chat.Ref`, `Grounding.Material`, `Grounding.Request`, L1/L2 boundaries, dedup, and output paths.

## Activation

Use this role when the user asks the supervisor to:

- collect grounding from a target chat
- propose `Chat.Ref` or turn references
- append session-level `Grounding.Request` records to the Chatlas grounding depot
- identify transcript evidence for related indexes or design blocks
- mine the observed session for future grounding
- run the `chat-grounding` supervisor role

Do not activate by default. The base supervisor can still mention an obvious grounding opportunity briefly, but this role runs only when requested.

## Contract

- The user's current supervision brief remains primary.
- Load `chatlas-grounding-agent` before using this role.
- This role is read-only by default.
- This role proposes grounding material by default.
- With explicit user instruction, this role may append to the global Chatlas grounding log for the observed session.
- The target workflow or index workflow owns acceptance and writes.
- Prefer high-signal evidence that changes future judgment.
- Do not dump every plausible reference.
- Distinguish observed evidence from inference.

## Write Boundary

Use `chatlas-grounding-agent` as the operational authority for every write.

This role's only permitted write is the session-level `Grounding.Request` log in the Chatlas depot:

```txt
~/Documents/chatlas/grounding/<identity_hash>-gr-req.jsonl
```

This is the global chat-grounding queue for the observed session. It is append-only candidate evidence, not accepted index truth.

Write rules:

- Write only after the user explicitly asks the supervisor to write grounding.
- Use the `Grounding.Request` JSONL shape from `chatlas-grounding-agent/references/gr-req-format.md`.
- Append only; never rewrite or delete existing records.
- Read existing records first and skip duplicate `ref`s.
- Create `~/Documents/chatlas/grounding/` if it does not exist.
- Report how many records were appended and the file path.
- Do not write block-level L2 requests from this role.
- Do not write index `### grounding` sections from this role.

## What To Notice

Good grounding candidates:

- user corrections that change a design boundary
- accepted decisions or explicit preferences
- concept definitions introduced or revised in chat
- scope boundaries, rejected alternatives, and parked questions
- workflow decisions that explain why a future artifact changed
- agent summaries that the user accepts or builds on
- turns that connect a concept to a source surface, codebase, or prior artifact

Weak grounding candidates:

- generic acknowledgements
- tool-progress updates
- transient phrasing that does not affect future judgment
- repeated summaries with no new decision
- agent assumptions not accepted by the user

## Reference Shape

Load `chatlas-grounding-agent` and use its `chatlas-surface.md` reference for `Chat.Ref` construction.

Preferred shape:

```md
- ref: `@<identity-hash-prefix>-<timetag>`
```

Range shape:

```md
- ref: `@<identity-hash-prefix>-<timetag1>..<timetag2>`
```

Whole-session fallback, only when the whole session is the evidence:

```md
- ref: `@<identity-hash-prefix>`
```

Use `zip-transcript.turns[<N>]` only as an explanatory note in a supervisor report, not as the grounding ref itself.

## Proposal Shape

Keep grounding proposals separate from the main supervision report unless the user asks for grounding only.

```md
## Grounding.Proposals

### Concept.Or.Block.Name
- ref: `@<identity-hash-prefix>-<timetag>`
- evidence: [brief observed evidence]
- use: [candidate block line, grounding note, or design/index target]
- status: proposed
```

For uncertain targets:

```md
### Unassigned
- ref: `@<identity-hash-prefix>-<timetag>`
- evidence: [brief observed evidence]
- use: candidate grounding; target block unclear
- open: [what needs user or index-workflow decision]
```

## Grounding.Request Shape

When writing, follow `chatlas-grounding-agent/references/gr-req-format.md`. The current record shape is one JSON object per line:

```json
{"ref": "@<hash>-<time>..<time>", "blocks": ["Concept.Name"], "grounding-why": "why this turn is Grounding.Material and what to weigh before pulling it"}
```

- `ref` is the smallest `Chat.Ref` range that preserves the decision.
- `blocks` contains only block names explicitly named in the turn or span.
- `grounding-why` describes why the material matters for later gated review.

## Applying The Role During Checks

When checking new turns:

1. Read the target turns using the base supervisor workflow.
2. Identify only turns that materially affect durable judgment.
3. Map each candidate to a concept, block, artifact, or `Unassigned`.
4. Produce concise proposals.
5. Keep normal supervision findings first when the user asked for process supervision.
6. Update the base supervisor cursor normally after reporting.

## Boundaries

- Do not claim a proposal is accepted grounding.
- Do not infer user acceptance from silence.
- Do not rewrite candidate evidence into stable index wording unless asked.
- Do not perform Agentos Index writes from this role.
- If the user wants grounding written, route through the relevant index or artifact workflow and respect its gates.
