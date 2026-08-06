# Supervisor.Role: Chat Grounding

`role-chat-grounding` is an additive `Supervisor.Role` for spotting `Support.Reference` candidates in an observed target session.

The role watches the transcript for turns that materially ground durable concepts — evidence a grounding line should eventually anchor. It proposes anchor candidates: a turn locator plus a one-sentence hint, mapped to a target block. It does not mint anchors, write the index, mutate the target session, or decide canonical design truth.

Model context: grounding is a line property (`Index.Line`) — `Anchory.Anchor`s trail on the lines they support and resolve through `Chatlas.Anchory`. This role feeds the applicable capture or support-reference maintenance workflow; it never runs it.

## Activation

Use this role when the user asks the supervisor to:

- collect grounding candidates from a target chat
- propose anchor candidates or turn references
- identify transcript evidence for index blocks or design artifacts
- mine the observed session for future grounding
- run the `chat-grounding` supervisor role

Do not activate by default. The base supervisor can still mention an obvious grounding opportunity briefly, but this role runs only when requested.

## Contract

- The user's current supervision brief remains primary.
- This role is read-only: it proposes, the linking workflow writes.
- The target workflow or index workflow owns acceptance, anchor minting, and index writes.
- Prefer high-signal evidence that changes future judgment.
- Do not dump every plausible reference.
- Distinguish observed evidence from inference.

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

Grounding is primarily grounded in user turns (`Grounding.Hugentic.Authority`): assistant-authored material qualifies only when the user explicitly accepts, corrects toward, or acts on it.

## Proposal Shape

A candidate names where to land and what an agent should find there. An anchor points into an evidence neighborhood — the locator does not have to isolate one exact turn, only land inside the relevant discussion.

Keep grounding proposals separate from the main supervision report unless the user asked for grounding only.

```md
## Grounding.Proposals

### Concept.Or.Block.Name
- at: <session identity_hash> <ISO 8601 time of the landing turn>
- hint: [one sentence: what is at this location]
- grounds: [what this evidence supports in the target block]
- status: proposed
```

For uncertain targets:

```md
### Unassigned
- at: <session identity_hash> <ISO 8601 time>
- hint: [one sentence: what is at this location]
- grounds: candidate grounding; target block unclear
- open: [what needs user or index-workflow decision]
```

Use `zip-transcript.turns[<N>]` only as an explanatory note in a supervisor report, not as the locator itself.

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
- Do not mint anchors (`agentos anchory register`) from this role.
- Do not rewrite candidate evidence into stable index wording unless asked.
- Do not perform Agentos Index writes from this role.
- If the user wants grounding written, route through the applicable capture or support-reference maintenance workflow and respect its gates.

> $kw: --from Grounding.Hugentic.Authority
> $kw: --from Index.Line
