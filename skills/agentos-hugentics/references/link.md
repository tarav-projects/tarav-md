# Anchory.Link.Operation.Module

Use this module when a caller needs the current chat-backed `Support.Reference` minted for an index line: the linking primitive behind ontology, appendix, and agendix provenance.

This module is `Workflow.Neutral`: it produces an anchor and returns it without writing an index surface. Minting mutates only the Anchory depot; authority remains with the qualifying data on its source surface.

Anchory is the current realization of `Index.Line.Anchor`. Its Chatlas line dossier records the line's `Support.Reference` and exact `Support.Set` members under `relationships.support`, review gates under `relationships.gates`, and provenance links under `relationships.provenance`.

This implementation composes `Anchory.System` and `Index.Chat.Capture` to connect an `Index.Line` to qualifying `Touched.Data` on `Touch.Authority.Surface`. The resulting edges participate in `Touched.Support.Network`; tokenized review metadata serves `Edition.Approval.Token` and `Line.Verbatim.Gate`.

## Linking Pipeline

All steps run through `agentos chatlas` and `agentos anchory` commands — never provider raw files or transcript paths.

For gated newly drafted content, this pipeline is landing work. Do not resolve proposal support or allocate an anchor before final token approval and the landing trigger. A draft may carry `^<anchor-on-landing>` only as an inert placeholder that the landing procedure replaces.

1. **Resolve the session.** Most linking happens on the edge — anchoring content produced in the *current* session, whose id the agent usually does not know. Invoke `agentos-chatlas-my-session-id` inline as the default path; it uses a provider-native id when trustworthy and otherwise refreshes Chatlas and matches the caller's own verbatim user turns without loading the candidate payload into context. It returns the native session id plus neutral Chatlas identity.
   - if the dedicated resolver cannot self-locate yet, refresh and pull recent candidates with `agentos chatlas recents` or `agentos chatlas query --active-after <recent> --update`, then filter with distinctive verbatim user fragments until exactly one identity remains
   - shortcuts: a native session id already in hand → `agentos chatlas query --session-id <native-id> --field identity_hash --update`; a past session → normal `query` filters
2. **Locate and qualify the evidence turns.** Chatlas locates observable editions; the agent chooses semantic support and applies the current chat authority-surface protocol:
   - use compact `agentos chatlas turns query --identity-hash <hash> --contains '<text>' --turn-kind user` for normalized User.Turn discovery; escalate with `--detail turn` only when the complete grouping is needed
   - use `agentos chatlas events query --identity-hash <hash> --pattern-json '<Event.Pattern JSON>' --backend auto` for adjacent or relational turn patterns
   - read `matched_events[].event_ref` for the exact matching events and `turn_ref` for the verified `Normal.Turn`
   - for a proposal followed by token approval, query a two-step `next_turn` pattern with an assistant `text_contains` token predicate and a user `text_exact` approval predicate; select `latest` or require cardinality `one` when that matches the situation
   - assistant events may aid retrieval and may be addressed by gate relationships, but only selected qualifying user turns become support members
   - for reviewed new content, select qualifying substantive user turns for the claim plus the approval turn; approval supplies review evidence and never replaces substantive grounding
   - exclude preset prompts, administrative invocations, and other user turns that do not materially touch the supported subject
   - disagreement, correction, rejection, delegation, and approval can all qualify; qualification does not certify factual truth
   - reload enough normal-model context to judge the result; a derived query backend discovers candidates but never establishes support
3. **Preview, then register the line dossier.** Validate exact qualifying user-turn members before allocation — never timestamps, never tape ordinals:
   - preview: `agentos chatlas anchory preview --line-content '- [<Line.Type>] <body>' --member <identity-hash>:<user-turn-id>`; inspect equivalent anchors and use `--detail context --radius N` only when more context is required
   - plain support: `agentos chatlas anchory register --line-content '- [<Line.Type>] <body>' --member <identity-hash>:<user-turn-id>`
   - tokenized approval adds `--gates '{"semantic_approval":[],"tokenized_verbatim_approval":[{"token":"<token>","proposal_turn":<Normal.Turn.Ref JSON>,"approval_turn":<Normal.Turn.Ref JSON>}]}'`
   - a proposal and the approval that answers it are independent gate references; they do not become support members merely by participating in a gate
   - semantic approval is represented under `semantic_approval` with an `approval_turn` and optional `proposal_turn`, but Hugentics reviewed Index workflows require tokenized approval
   - Chatlas validates every reference, preserves support order, allocates the anchor, derives the attachment assertion over `Line.Type + body + Anchor.Id`, and returns the composed anchor (`c<YYYYMMDD>-<N>u`)
   - the raw plumbing remains available: `agentos anchory register --depot <chatlas-root>/anchory --namespace chatlas --alloc-prefix <YYYYMMDD> [--tag u|a] --record-json '…'`
   - when two or more final lines are being linked, do not repeat these commands: write one ordered `chatlas.anchor-batch.v2` input with a stable `client_id`, exact `line_content`, ordered `members`, and optional `gates`, `predecessors`, and `issue_context` per item; run `agentos chatlas anchory batch preview --input <batch.json> --json`, then `agentos chatlas anchory batch register --input <batch.json> --json`
   - batch preview validates every item before allocation; batch registration is idempotent, reuses exact equivalents, and returns a `client_id → anchor` mapping so the caller can attach the whole cluster in one Index patch
4. **Verify.** Registration returns the compact minted record. Escalate with `agentos chatlas anchory resolve <anchor> --detail context [--radius N]` only when the neighborhood must be revisited.
5. **Return the current support reference** to the caller, which materializes it as a trailing anchor: `… ^c20260707-0u`.

## Code-Side Evidence

- file-touches are the code-side analogue of chat anchors: `agentos chatlas query --file-touched "<path>"` finds the sessions that actually read/wrote a file (mentions never match), and `agentos chatlas views get --file-write "<path>" --view events` lands on the touching moments — the "find the evidence turn" step for code changes

## Anchor Discipline

- a chat-backed index anchor targets a qualifying user turn — the observable touch materialization; when wording originated agent-side, anchor the user turn that accepted, corrected, rejected, delegated, or acted on it
- `<session-identity>:<turn-id>` is registration CLI sugar; the stored member is a `Normal.Turn.Ref` carrying `session`, `turn_id`, `turn_hash`, and `at`
- the model separates local IDs from durable assertions: `message_id`, `model_run_id`, and their siblings are **section-local join keys**; a bare `turn_id` only locates a grouping, while `Normal.Turn.Ref` and `Event.Ref` verify the content they address
- a tokenized reviewed-content anchor has qualifying substantive support members and an independent `tokenized_verbatim_approval` gate pointing to the proposal and approval turns
- the Index surface owns the current `Line.Type + body + Anchor.Id` triplet; the dossier's attachment hash detects unmaintained drift without copying line content
- `agentos anchory amend` may preserve an anchor while the application normalizer updates its valid relationships or attachment assertion; never repurpose it for an unrelated line relationship
- the register is plumbing, not truth or authority — the information lives on the authority surfaces; agents detect desync by reading them
- exact dossier equivalence may reuse an existing anchor; content equality alone does not make two line relationships identical
- after a line amendment, the maintainer decides whether to retain and re-hash the anchor or assign a new one, then revisits every affected relationship

## Addressing One Event

Anchors ground on turns, but some evidence is finer than a turn — a specific tool call, one event a pattern matched. That address is an `Event.Ref`, not an `event_id`.

- an `Event.Ref` is the object `{event_address, event_hash}`: the address locates a stable provider-normalized event place and the hash asserts its current content; `schema`, `session`, and `at` are optional context fields
- the address is opaque to the normal model — each provider normalizer owns the raw coordinate recipe, with the rule that a content-only amendment cannot change the address or event count
- `<event_address>:<event_hash>` is CLI and log sugar only; stored references remain objects, with an 8-byte digest-prefix floor for the asserted hash
- resolution semantics are simple: the address and assertion match; the address exists with amended content; or the addressed place is absent from the declared tape scope. Consumers choose their own policy from those facts; Chatlas does not relocate or repair references by searching for matching content
- a failed assertion is a POI to research, never an error to swallow and never an automatic rewrite — repair is an explicit act, like `agentos anchory amend`

## Resolution (reading an anchor)

- `agentos chatlas anchory resolve <anchor>` — compact record and member summary
- `agentos chatlas anchory resolve <anchor> --detail turn|context [--radius N]` — explicitly escalates to exact turns or bounded message-turn neighborhoods
- `agentos index line manifest show --depot <depot> --anchor <anchor> ...` — assembles selected lines, their parsed block-bounded Index context, and independently typed relationships in one process; `materialize` writes the same derived payload beneath ignored `<chatlas-root>/workspace/`
- a line manifest is a `Volatile.Surface`: use it for line understanding and bounded relationship inspection, never as support authority or as a new relationship
- `--verification stored` reads dossier assertions without loading chats; `sampled` validates a deterministic bounded subset and `complete` validates every selected turn reference. `--detail reference|turn|context` controls evidence rendering independently of verification breadth
- the landing turn is the member turn's own user message; assistant context is recovered by reading the neighborhood around it
- `agentos anchory resolve --anchor <anchor> [--depot …]` remains the record-level (plumbing) view
