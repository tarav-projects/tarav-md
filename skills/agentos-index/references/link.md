# agentos-index --link

Use this module when a caller needs an `Anchory.Anchor` minted for a chat context: the linking primitive behind grounding lines, inline grounding, and agendix provenance.

This module is `Workflow.Neutral`: it produces an anchor and returns it — it writes no index surface. Consumers decide where the anchor lands: `--edit` writes gated `[GR]` grounding lines and inline anchors; `--agendix` tags captured lines. Minting an anchor mutates only the anchory depot, which is register plumbing, not an index edit.

Authority lives in the index: `Anchory.System`, `Chatlas.Anchory`, `Index.Linking`, `Index.Line`, `Index.Chat.Capture`, `Edition.Approval.Token`, and `Line.Verbatim.Gate` own the concepts.

## Linking Pipeline

All steps run through `agentos chatlas` and `agentos anchory` commands — never provider raw files or transcript paths.

1. **Resolve the session.** Most linking happens on the edge — anchoring content produced in the *current* session, whose id the agent usually does not know. Discover yourself by content matching:
   - refresh and pull the recent candidates: `agentos chatlas recents` or `agentos chatlas query --active-after <recent> --update`
   - filter with verbatim user turns from your own context — the more distinctive the phrasing, the better: `agentos chatlas query --user-contains "<exact snippet>" --field identity_hash`
   - repeat with more snippets until exactly one candidate remains: that is you (the conversation is a fingerprint; chatlas has indexed it)
   - shortcuts: a native session id already in hand → `agentos chatlas query --session-id <native-id> --field identity_hash --update`; a past session → normal `query` filters
2. **Locate the evidence turns.** The agent chooses semantic support; Chatlas formalizes that choice against the authoritative event tape:
   - use `agentos chatlas events query --identity-hash <hash> --pattern-json '<Event.Pattern JSON>' --backend auto` to locate exact, adjacent, or distinctive turns
   - read `turn_id` off each returned event — that is the registration key. The pattern language and its `event_ids` projection still address *events*; a member addresses the `Normal.Turn` the matched event belongs to
   - for a proposal followed by token approval, query a two-step `next_turn` pattern with an assistant `text_contains` token predicate and a user `text_exact` approval predicate; select `latest` or require cardinality `one` when that matches the situation
   - assistant events may aid retrieval and their turns may be referenced by approval cargo, but only selected user turns become `Chat.Support.Set` members
   - reload enough normal-model context to judge the result; a derived query backend discovers candidates but never establishes support
3. **Register the anchor.** Register exact user turn members — never timestamps, never tape ordinals:
   - plain support: `agentos chatlas anchory register --member <identity-hash>:<user-turn-id> --hint "<one sentence: what this support set means>"`
   - tokenized approval: `agentos chatlas anchory register --member <identity-hash>:<approval-turn-id> --hint "<one sentence>" --member-types '{"<identity-hash>:<approval-turn-id>":{"tokenized.approval.turn":{"token":"<token>","verbatim_turn":"<identity-hash>:<proposal-turn-id>","approval_turn":"<identity-hash>:<approval-turn-id>"}}}'`
   - a proposal and the approval that answers it often share one turn, since the assistant reply belongs to the user turn that prompted it; identical `verbatim_turn` and `approval_turn` refs are legitimate
   - semantic approval is representable with `semantic.approval.turn` cargo containing `verbatim_turn` and `approval_turn`, but `agentos-index` workflows require tokenized approval
   - chatlas validates member coordinates, preserves member order, derives the `chatlas` namespace and user tag, registers through anchory, and returns the composed anchor (`c<YYYYMMDD>-<N>u`)
   - the raw plumbing remains available: `agentos anchory register --depot <chatlas-root>/anchory --namespace chatlas --alloc-prefix <YYYYMMDD> [--tag u|a] --record-json '…'`
4. **Verify.** Resolve the record and neighborhood after registration with `agentos chatlas anchory resolve <anchor> [--radius N]`. Confirm every member is the intended user turn and typed cargo references the intended proposal and approval turns.
5. **Return the anchor** to the caller, which tags its line: trailing position, `… ^c20260707-0u`.

## Code-Side Evidence

- file-touches are the code-side analogue of chat anchors: `agentos chatlas query --file-touched "<path>"` finds the sessions that actually read/wrote a file (mentions never match), and `views inline --file-write "<path>"` lands on the touching moments — the "find the evidence turn" step for code changes

## Anchor Discipline

- an anchor for index grounding targets a USER turn — touch is the landing point, assistant context is recovered by neighborhood reading; when the wording originated agent-side, anchor the approval turn
- member identity is `<session-identity>:<turn-id>` — the `Normal.Turn` identity, stable across re-materialization of an open session; timestamps are readability metadata and `event_id` is a tape-local join key, neither of which may be a registration key
- the model separates two kinds of address, and storing the wrong one is how anchors silently rot: `event_id`, `message_id`, `model_run_id` and their siblings are **section-local join keys**, valid only inside one materialization; `turn_id` and `Event.Ref` are **durable**, and only those may be written down
- a tokenized approval anchor has one user support member whose `tokenized.approval.turn` cargo points to the proposal and approval turns
- an anchor's meaning is immutable: no reuse; a wrong hint or wrong date means minting a new anchor, never repurposing
- `agentos anchory amend` exists only to correct an error or improve resolution of the same context
- the hint is the desync tripwire: write it so a reader can tell whether the resolved neighborhood matches
- the register is plumbing, not truth — the information lives on the surfaces; agents detect desync by reading them
- one anchor per claim: if two lines ground on the same neighborhood, they may share the anchor

## Addressing One Event

Anchors ground on turns, but some evidence is finer than a turn — a specific tool call, one event a pattern matched. That address is an `Event.Ref`, not an `event_id`.

- an `Event.Ref` is `<event_hash>:<index>` (schema `chatlas.event-ref.v1`): a minimal assertion that the event with this content hash sat at this tape index
- neither half stands alone — the index moves when the tape re-segments ahead of it, and event content genuinely repeats — so the index disambiguates the hash and the hash validates the index
- resolving one reports what it found: the assertion holds; the event drifted to a new index (repairable, and a repair is offered); the content is gone entirely (desync, never auto-repaired); or the hash occurs several times and the index decided
- a failed assertion is a POI to research, never an error to swallow and never an automatic rewrite — repair is an explicit act, like `agentos anchory amend`

## Resolution (reading an anchor)

- `agentos chatlas anchory resolve <anchor> [--radius N]` — resolves through the chatlas anchory depot and returns each member's landing turn with its neighborhood, already reduced to message turns; `--radius` counts visible turns either side (default 4)
- the landing turn is the member turn's own user message; assistant context is recovered by reading the neighborhood around it
- `agentos anchory resolve --anchor <anchor> [--depot …]` remains the record-level (plumbing) view
