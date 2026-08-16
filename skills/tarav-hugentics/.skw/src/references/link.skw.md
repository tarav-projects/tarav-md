> $kw: ^link-direct-loading-path --context-loading-path
> --step SKILL.md
> --loading-dep SKILL.skw.md^hugentics-batchy-runtime-contract
> --loading-dep SKILL.skw.md^hugentics-skill-arg-contract
> --loading-dep SKILL.skw.md^driver-index-literacy
> --loading-dep SKILL.skw.md^hugentics-authority-contract

# Anchory.Link.Operation.Module

> $kw: --from Anchory.System --from Edition.Approval.Token --from Index.Chat.Capture --from Index.Line --from Index.Line.Anchor --from Line.Verbatim.Gate --from Support.Set --from Touch.Authority.Surface --from Touched.Data --from Touched.Support.Network --from Volatile.Surface --from Workflow.Neutral
> --dev-from references/index-context-assembly.skw.md

Use this module when a caller needs the current chat-backed `Support.Reference` minted for an index line: the linking primitive behind ontology, appendix, and agendix provenance.

This module is `Workflow.Neutral`: it produces an anchor and returns it without writing an index surface. Minting mutates only the Anchory depot; authority remains with the qualifying data on its source surface.

Anchory is the current realization of `Index.Line.Anchor`. Its Chatlas2 line dossier records the line's `Support.Set` as exact user `Chat.Message.Ref` members under `relationships.support`, review messages under `relationships.gates`, and provenance links under `relationships.provenance`.

This implementation composes `Anchory.System` and `Index.Chat.Capture` to connect an `Index.Line` to qualifying `Touched.Data` on `Touch.Authority.Surface`. The resulting edges participate in `Touched.Support.Network`; tokenized review metadata serves `Edition.Approval.Token` and `Line.Verbatim.Gate`.

## Linking Pipeline

All chat grounding steps run through `tarav chatlas2`; provider raw artifacts remain an explicit diagnostic fallback, never the registration interface.

For gated newly drafted content, this pipeline is landing work. Do not resolve proposal support or allocate an anchor before final token approval and the landing trigger. A draft may carry `^<anchor-on-landing>` only as an inert placeholder that the landing procedure replaces.

1. **Resolve the session.** Most linking happens on the edge — anchoring content produced in the *current* session, whose id the agent usually does not know. Invoke `tarav-chatlas-my-session-id` inline as the default path; it uses a provider-native id when trustworthy and otherwise refreshes Chatlas and matches the caller's own verbatim user turns without loading the candidate payload into context. It returns the native session id plus neutral Chatlas identity.
   - if the dedicated resolver cannot self-locate yet, refresh and pull recent candidates with `tarav chatlas recents` or `tarav chatlas query --active-after <recent> --update`, then filter with distinctive verbatim user fragments until exactly one identity remains
   - shortcuts: a native session id already in hand → `tarav chatlas query --session-id <native-id> --update --json`; a past session → normal current-Chatlas discovery filters
2. **Locate and qualify the evidence messages.** Read `tarav chatlas2 views get --session-id <id> --view user --json` for the compact user exchange or `--view transcript` when agent context matters. Use `tarav chatlas2 messages find --session-id <id> --side user|agent --text '<text>' [--exact] --json` to obtain exact `member_ref` values.
   - only selected qualifying user messages become support members
   - proposal and approval messages belong independently to gate relationships; the proposal is agent-side and the approval user-side
   - for reviewed new content, select substantive user messages for the claim; approval supplies review evidence and never replaces substantive grounding
   - exclude preset prompts, administrative invocations, and other user messages that do not materially touch the supported subject
   - disagreement, correction, rejection, delegation, and approval can all qualify; qualification does not certify factual truth
   - reload enough transcript neighborhood to judge the result; message lookup discovers candidates but never establishes semantic support
3. **Preview, then register the line dossier.** Validate exact `Chat.Message.Ref` members before allocation — never timestamps or tape ordinals:
   - preview: `tarav chatlas2 anchory preview --line-content '- [<Line.Type>] <body>' --member '<member-ref>'`
   - plain support: `tarav chatlas2 anchory register --line-content '- [<Line.Type>] <body>' --member '<member-ref>'`
   - tokenized approval adds `--gates '{"tokenized_verbatim_approval":[{"token":"<token>","proposal":"<agent-member-ref>","approval":"<user-member-ref>"}]}'`
   - a proposal and the approval that answers it are independent gate references; they do not become support members merely by participating in a gate
   - semantic approval uses `semantic_approval` with a user `approval` and optional agent `proposal`, but reviewed Index workflows require tokenized approval
   - Chatlas2 validates every message assertion and role, preserves support order, allocates the anchor, derives the attachment assertion over `Line.Type + body + Anchor.Id`, and returns `d<YYYYMMDD>-<N>u`
   - when two or more final lines are linked, write one ordered `tarav.chatlas2.anchor-batch.v2` input with stable `client_id`, exact `line_content`, ordered `members`, and optional `gates`, `predecessors`, and `issue_context`; run `tarav chatlas2 anchory batch preview|register --input <batch.json>`
   - batch preview validates every item before allocation; batch registration is idempotent, reuses exact equivalents, and returns a `client_id → anchor` mapping so the caller can attach the whole cluster in one Index patch
4. **Verify.** Registration returns the record plus current `MATCHED|AMENDED|MISSING` message standing. Escalate with `tarav chatlas2 anchory resolve <anchor> --radius N` when the neighborhood must be revisited.
5. **Return the support reference** to the caller, which materializes it as a trailing anchor: `… ^d20260816-0u`.

For non-line implementation provenance, use `tarav chatlas2 anchory support preview|register --member '<user-member-ref>'`. The resulting message-support record has no line attachment or review gate; cite it from Impl.Agendix or Impl.Log.

## Code-Side Evidence

- file-touches remain a current-Chatlas evidence-discovery specialization: `tarav chatlas query --file-touched "<path>"` finds sessions that actually read/wrote a file, and `tarav chatlas views get --file-write "<path>" --view events` lands on touching moments; this does not change the Chatlas2 grounding record

## Anchor Discipline

- a chat-backed Index anchor supports its line with qualifying user `Chat.Message.Ref` assertions; when wording originated agent-side, support comes from the user message that accepted, corrected, rejected, delegated, or acted on it
- `<session>:<message_address>:<message_hash>` is registration sugar; the stored member retains those identity fields plus diagnostic `at`
- a tokenized reviewed-content anchor has substantive support members and an independent gate pointing to agent proposal and user approval messages
- the Index surface owns the current `Line.Type + body + Anchor.Id` triplet; the dossier's attachment hash detects unmaintained drift without copying line content
- `tarav anchory amend` may preserve an anchor while application-owned relationships or attachment assertions are updated; never repurpose it for an unrelated line relationship
- the register is plumbing, not truth or authority — the information lives on the authority surfaces; agents detect desync by reading them
- exact dossier equivalence may reuse an existing anchor; content equality alone does not make two line relationships identical
- after a line amendment, the maintainer decides whether to retain and re-hash the anchor or assign a new one, then revisits every affected relationship

## Addressing One Event

Grounding normally names `Chat.Message.Ref`, but finer evidence may name one event. That address is an `Event.Ref`, not an `event_id`.

- an `Event.Ref` is the object `{event_address, event_hash}`: the address locates a stable provider-normalized event place and the hash asserts its current content; `schema`, `session`, and `at` are optional context fields
- the address is opaque to the normal model — each provider normalizer owns the raw coordinate recipe, with the rule that a content-only amendment cannot change the address or event count
- `<event_address>:<event_hash>` is CLI and log sugar only; stored references remain objects, with an 8-byte digest-prefix floor for the asserted hash
- resolution semantics are simple: the address and assertion match; the address exists with amended content; or the addressed place is absent from the declared tape scope. Consumers choose their own policy from those facts; Chatlas does not relocate or repair references by searching for matching content
- a failed assertion is a POI to research, never an error to swallow and never an automatic rewrite — repair is an explicit act, like `tarav anchory amend`

## Resolution (reading an anchor)

- `tarav chatlas2 anchory resolve <anchor> [--radius N]` — record, member standing, and bounded message neighborhood
- `tarav index line manifest show --depot <depot> --anchor <anchor> ...` — namespace-dispatches old and Chatlas2 dossiers while assembling selected lines and their relationships
- a line manifest is a `Volatile.Surface`: use it for line understanding and bounded relationship inspection, never as support authority or as a new relationship
- an `ambiguous` anchor occurrence standing makes the anchor unsuitable for line lookup until normal Index lint identifies and the maintainer resolves the disagreement
- `--verification stored` reads assertions without loading chats; `sampled` validates a bounded subset and `complete` validates every selected message reference. `--detail reference|turn|context` remains the derived manifest rendering vocabulary during migration
- `tarav anchory resolve --anchor <anchor> [--depot …]` remains the application-neutral record-level view
