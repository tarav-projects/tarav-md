> $kw: ^link-direct-loading-path --context-loading-path
> --step SKILL.md
> --loading-dep SKILL.skw.md^hugentics-batchy-runtime-contract
> --loading-dep SKILL.skw.md^hugentics-skill-arg-contract
> --loading-dep SKILL.skw.md^driver-index-literacy
> --loading-dep SKILL.skw.md^hugentics-authority-contract

# Anchory.Link.Operation.Module

> $kw: --from Anchory.System --from Edition.Approval.Token --from Index.Chat.Capture --from Index.Line --from Index.Linking --from Line.Verbatim.Gate --from Support.Set --from Touch.Authority.Surface --from Touched.Data --from Touched.Support.Network --from Workflow.Neutral
> --dev-from references/index-context-assembly.skw.md

Use this module when a caller needs the current chat-backed `Support.Reference` minted for an index line: the linking primitive behind ontology, appendix, and agendix provenance.

This module is `Workflow.Neutral`: it produces an anchor and returns it without writing an index surface. Minting mutates only the Anchory depot; authority remains with the qualifying data on its source surface.

Anchory is the current realization of `Support.Reference`; its Chatlas record realizes `Support.Set`, and typed record cargo realizes `Support.Reference.Metadata`.

This implementation composes `Anchory.System`, `Index.Linking`, and `Index.Chat.Capture` to connect an `Index.Line` to qualifying `Touched.Data` on `Touch.Authority.Surface`. The resulting edges participate in `Touched.Support.Network`; tokenized review metadata serves `Edition.Approval.Token` and `Line.Verbatim.Gate`.

## Linking Pipeline

All steps run through `agentos chatlas` and `agentos anchory` commands — never provider raw files or transcript paths.

For gated newly drafted content, this pipeline is landing work. Do not resolve proposal support or allocate an anchor before final token approval and the landing trigger. A draft may carry `^<anchor-on-landing>` only as an inert placeholder that the landing procedure replaces.

1. **Resolve the session.** Most linking happens on the edge — anchoring content produced in the *current* session, whose id the agent usually does not know. Discover yourself by content matching:
   - refresh and pull the recent candidates: `agentos chatlas recents` or `agentos chatlas query --active-after <recent> --update`
   - filter with verbatim user turns from your own context — the more distinctive the phrasing, the better: `agentos chatlas query --user-contains "<exact snippet>" --field identity_hash`
   - repeat with more snippets until exactly one candidate remains: that is you (the conversation is a fingerprint; chatlas has indexed it)
   - shortcuts: a native session id already in hand → `agentos chatlas query --session-id <native-id> --field identity_hash --update`; a past session → normal `query` filters
2. **Locate and qualify the evidence turns.** Chatlas locates observable editions; the agent chooses semantic support and applies the current chat authority-surface protocol:
   - use compact `agentos chatlas turns query --identity-hash <hash> --contains '<text>' --human` for one-turn discovery; escalate with `--detail turn` only when the complete grouping is needed
   - use `agentos chatlas events query --identity-hash <hash> --pattern-json '<Event.Pattern JSON>' --backend auto` for adjacent or relational turn patterns
   - read `matched_events[].event_ref` for the exact matching events and `turn_ref` for the verified `Normal.Turn`
   - for a proposal followed by token approval, query a two-step `next_turn` pattern with an assistant `text_contains` token predicate and a user `text_exact` approval predicate; select `latest` or require cardinality `one` when that matches the situation
   - assistant events may aid retrieval and their turns may be referenced by approval cargo, but only selected qualifying user turns become `Chat.Support.Set` members
   - for reviewed new content, select qualifying substantive user turns for the claim plus the approval turn; approval supplies review evidence and never replaces substantive grounding
   - exclude preset prompts, administrative invocations, and other user turns that do not materially touch the supported subject
   - disagreement, correction, rejection, delegation, and approval can all qualify; qualification does not certify factual truth
   - reload enough normal-model context to judge the result; a derived query backend discovers candidates but never establishes support
3. **Preview, then register the support reference.** Validate exact qualifying user-turn members before allocation — never timestamps, never tape ordinals:
   - preview: `agentos chatlas anchory preview --member <identity-hash>:<user-turn-id> --hint "<one sentence>"`; inspect equivalent anchors and use `--detail context --radius N` only when more context is required
   - plain support: `agentos chatlas anchory register --member <identity-hash>:<user-turn-id> --hint "<one sentence: what this support set means>"`
   - tokenized approval: `agentos chatlas anchory register --member <identity-hash>:<substantive-turn-id> --member <identity-hash>:<approval-turn-id> --hint "<one sentence>" --member-types '{"<identity-hash>:<approval-turn-id>":{"tokenized.approval.turn":{"token":"<token>","verbatim_turn":"<identity-hash>:<proposal-turn-id>","approval_turn":"<identity-hash>:<approval-turn-id>"}}}'`
   - a proposal and the approval that answers it are independent turns: `verbatim_turn` references the assistant turn and `approval_turn` references the user turn
   - semantic approval is representable with `semantic.approval.turn` cargo containing `verbatim_turn` and `approval_turn`, but Hugentics Index workflows require tokenized approval
   - chatlas validates member coordinates, preserves member order, derives the `chatlas` namespace and user tag, registers through anchory, and returns the composed anchor (`c<YYYYMMDD>-<N>u`)
   - the raw plumbing remains available: `agentos anchory register --depot <chatlas-root>/anchory --namespace chatlas --alloc-prefix <YYYYMMDD> [--tag u|a] --record-json '…'`
4. **Verify.** Registration returns the compact minted record. Escalate with `agentos chatlas anchory resolve <anchor> --detail context [--radius N]` only when the neighborhood must be revisited.
5. **Return the current support reference** to the caller, which materializes it as a trailing anchor: `… ^c20260707-0u`.

## Code-Side Evidence

- file-touches are the code-side analogue of chat anchors: `agentos chatlas query --file-touched "<path>"` finds the sessions that actually read/wrote a file (mentions never match), and `views inline --file-write "<path>"` lands on the touching moments — the "find the evidence turn" step for code changes

## Anchor Discipline

- a chat-backed index anchor targets a qualifying user turn — the observable touch materialization; when wording originated agent-side, anchor the user turn that accepted, corrected, rejected, delegated, or acted on it
- `<session-identity>:<turn-id>` is registration CLI sugar; the stored member is a `Normal.Turn.Ref` carrying `session`, `turn_id`, `turn_hash`, and `at`
- the model separates local IDs from durable assertions: `message_id`, `model_run_id`, and their siblings are **section-local join keys**; a bare `turn_id` only locates a grouping, while `Normal.Turn.Ref` and `Event.Ref` verify the content they address
- a tokenized reviewed-content anchor has qualifying substantive user support members plus the approval member whose `tokenized.approval.turn` cargo points to the proposal and approval turns
- an anchor's meaning is immutable: no reuse; a wrong hint or wrong date means minting a new anchor, never repurposing
- `agentos anchory amend` exists only to correct an error or improve resolution of the same context
- the hint is the desync tripwire: write it so a reader can tell whether the resolved neighborhood matches
- the register is plumbing, not truth or authority — the information lives on the authority surfaces; agents detect desync by reading them
- one anchor per claim: if two lines ground on the same neighborhood, they may share the anchor

## Addressing One Event

Anchors ground on turns, but some evidence is finer than a turn — a specific tool call, one event a pattern matched. That address is an `Event.Ref`, not an `event_id`.

- an `Event.Ref` is the object `{event_hash, sequence}`: a minimal assertion that an event with this digest occupied this tape position; `schema`, `session`, and `at` are optional context fields
- neither half stands alone — the sequence moves when the tape re-segments ahead of it, and event content genuinely repeats — so the sequence disambiguates the hash and the hash validates the sequence
- `<event_hash>:<sequence>` is CLI and log sugar only; stored references remain objects, with an 8-byte digest-prefix floor
- resolving one reports what it found: the assertion holds; the event drifted to a new index (repairable, and a repair is offered); the content is gone entirely (desync, never auto-repaired); or the hash occurs several times and the index decided
- a failed assertion is a POI to research, never an error to swallow and never an automatic rewrite — repair is an explicit act, like `agentos anchory amend`

## Resolution (reading an anchor)

- `agentos chatlas anchory resolve <anchor>` — compact record and member summary
- `agentos chatlas anchory resolve <anchor> --detail turn|context [--radius N]` — explicitly escalates to exact turns or bounded message-turn neighborhoods
- the landing turn is the member turn's own user message; assistant context is recovered by reading the neighborhood around it
- `agentos anchory resolve --anchor <anchor> [--depot …]` remains the record-level (plumbing) view
