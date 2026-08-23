> $kw: ^real-time-grounding-direct-loading-path --context-loading-path
> --step SKILL.md
> --loading-dep SKILL.skw.md^hugentics-authority-contract

# Real.Time.Grounding.Knowledge.Module

> $kw: --from Chat.Surface --from Index.Line --from Index.Line.Anchor --from Stable.Surface --from Touched.Data
> --dev-from references/index-context-assembly.skw.md

This is the internal Chatlas2 grounding primitive used by `Real.Time.Capture`; it is not a public workflow. It connects an exact newly landed `Index.Line` to qualifying current-chat `Touched.Data` through a Chatlas2 line dossier and returns the resulting `Index.Line.Anchor`.

The Index surface owns the line. The dossier owns its attachment assertion plus independent support, gate, and provenance relationships. A reference detects drift; it does not relocate or repair amended content.

## Grounding Pipeline

1. **Obtain the current session selector.** Use the exact provider-native session id supplied by the running harness or already present in the active workflow. Do not run a Chatlas1 recents, query, view, or file-touch fallback. When the selector is unavailable, stop this landing with `SESSION_SELECTOR_UNAVAILABLE` and leave the primary material unminted.
2. **Select evidence from loaded context.** Use the live conversation already available to the agent to choose substantive user support and, when applicable, the agent proposal plus user approval gate messages. Do not reread the transcript by default.
3. **Resolve exact messages.** Run `tarav chatlas messages find --session-id <id> --side user|agent --contains '<distinctive text>' [--exact] --json`. Refine ambiguity before widening. Hydrate only the containing turn with `tarav chatlas turns get --session-id <id> --message-address <address> --hydrate --json` when associated material is necessary.
4. **Author one manifest.** Put every final line, its target surface and block, and its relationships in one `tarav.index.capture-manifest.v1` document. Each message reference carries structured `session`, `message_address`, and `message_hash` fields; `hints.at` aids review, while `expect.contains_all` gives the agent a conjunctive content check. Do not author a `side` field: support and gate roles determine the allowed side and preflight verifies it.
5. **Stop at the manifest.** **Landing is blocked.** The `Capture.Manifest` pipeline ran on the Markdown realization and was removed with it. The recording kernel captures records (`tarav indexlab capture --library <root> --workspace <name> --manifest <records.json>`) but has no equivalent for anchor registration, gate evidence, or the landing audit. Until it does, produce the approved content and stop: report the blocked landing rather than inventing a placement.

## Relationship Discipline

- substantive user messages belong in `relationships.support`
- proposal and approval messages belong independently in `relationships.gates`; participation in a gate does not make them substantive support
- reviewed Index lines require `tokenized_verbatim_approval`; non-line implementation provenance uses `tarav chatlas anchory support preview|register`
- `relationships.provenance.predecessor_anchors` names editions replaced on HEAD; `issue_context` records applicable `Issue.Block` identities
- support order is meaningful and exact dossier equivalence is idempotent
- timestamps are diagnostic only; `Chat.Message.Ref` place plus hash is identity
- a `Stable.Surface` is maintained durable state, not undeletable state; capture may revise or remove it through its owning workflow. The referenced `Chat.Surface` is separately immutable.

## Boundary

- no public `--link` route exists
- no Chatlas1 session discovery, Normal Model, view, file-touch search, or anchor resolver is part of this primitive
- legacy anchors remain stored history but are not resolved by active Hugentics workflows
- provider raw artifacts remain a diagnostic fallback for agents, never the registration interface
