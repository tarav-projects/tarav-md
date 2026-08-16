> $kw: ^real-time-grounding-direct-loading-path --context-loading-path
> --step SKILL.md
> --loading-dep SKILL.skw.md^hugentics-authority-contract

# Real.Time.Grounding.Knowledge.Module

> $kw: --from Index.Line --from Index.Line.Anchor --from Touched.Data
> --dev-from references/index-context-assembly.skw.md

This is the internal Chatlas2 grounding primitive used by `Real.Time.Capture`; it is not a public workflow. It connects an exact newly landed `Index.Line` to qualifying current-chat `Touched.Data` through a Chatlas2 line dossier and returns the resulting `Index.Line.Anchor`.

The Index surface owns the line. The dossier owns its attachment assertion plus independent support, gate, and provenance relationships. A reference detects drift; it does not relocate or repair amended content.

## Grounding Pipeline

1. **Obtain the current session selector.** Use the exact provider-native session id supplied by the running harness or already present in the active workflow. Do not run a Chatlas1 recents, query, view, or file-touch fallback. When the selector is unavailable, stop this landing with `SESSION_SELECTOR_UNAVAILABLE` and leave the primary material unminted.
2. **Select evidence from loaded context.** Use the live conversation already available to the agent to choose substantive user support and, when applicable, the agent proposal plus user approval gate messages. Do not reread the transcript by default.
3. **Resolve exact messages.** Run `tarav chatlas2 messages find --session-id <id> --side user|agent --text '<distinctive text>' [--exact] --json`. Refine ambiguity before widening. Hydrate only the containing turn with `tarav chatlas2 turns get --session-id <id> --message-address <address> --hydrate --json` when associated material is necessary.
4. **Preview and register.** For one line use `tarav chatlas2 anchory preview|register --line-content '<exact-line>' --member '<member-ref>'`. For several lines use one ordered `tarav.chatlas2.anchor-batch.v2` document and `tarav chatlas2 anchory batch preview|register --input <batch.json>`.
5. **Verify.** Run `tarav chatlas2 anchory resolve <anchor> [--radius N]`; every selected assertion must resolve with the expected side and `MATCHED` standing before the anchor is attached.
6. **Return the mapping.** Return the stable `client_id -> d… anchor` mapping to the landing target so it can patch the primary surface once and then invoke `Index.HEAD.Backpropagation`.

## Relationship Discipline

- substantive user messages belong in `relationships.support`
- proposal and approval messages belong independently in `relationships.gates`; participation in a gate does not make them substantive support
- reviewed Index lines require `tokenized_verbatim_approval`; non-line implementation provenance uses `tarav chatlas2 anchory support preview|register`
- `relationships.provenance.predecessor_anchors` names editions replaced on HEAD; `issue_context` records applicable `Issue.Block` identities
- support order is meaningful and exact dossier equivalence is idempotent
- timestamps are diagnostic only; `Chat.Message.Ref` place plus hash is identity

## Boundary

- no public `--link` route exists
- no Chatlas1 session discovery, Normal Model, view, file-touch search, or anchor resolver is part of this primitive
- legacy anchors remain stored history but are not resolved by active Hugentics workflows
- provider raw artifacts remain a diagnostic fallback for agents, never the registration interface
