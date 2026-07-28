# agentos-index --link

> $kw: --from Anchory.System --from Edition.Approval.Token --from Index.Chat.Capture --from Index.Line --from Index.Linking --from Line.Verbatim.Gate --from Workflow.Neutral
> --dev-from references/index-context-assembly.skw.md

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
2. **Locate the evidence events.** The agent chooses semantic support; Chatlas formalizes that choice against the authoritative event tape:
   - use `agentos chatlas events query --identity-hash <hash> --pattern-json '<Event.Pattern JSON>' --backend auto` to locate exact, adjacent, or distinctive turns and return authoritative event coordinates
   - for a proposal followed by token approval, query a two-step `next_turn` pattern with an assistant `text_contains` token predicate and a user `text_exact` approval predicate; select `latest` or require cardinality `one` when that matches the situation
   - assistant events may aid retrieval and may be referenced by approval cargo, but only selected user turns become `Chat.Support.Set` members
   - reload enough normal-model context to judge the result; a derived query backend discovers candidates but never establishes support
3. **Register the anchor.** Register exact user event members — never timestamps:
   - plain support: `agentos chatlas anchory register --member <identity-hash>:<user-event-id> --hint "<one sentence: what this support set means>"`
   - tokenized approval: `agentos chatlas anchory register --member <identity-hash>:<approval-event-id> --hint "<one sentence>" --member-types '{"<identity-hash>:<approval-event-id>":{"tokenized.approval.turn":{"token":"<token>","verbatim_turn":"<identity-hash>:<proposal-event-id>","approval_turn":"<identity-hash>:<approval-event-id>"}}}'`
   - semantic approval is representable with `semantic.approval.turn` cargo containing `verbatim_turn` and `approval_turn`, but `agentos-index` workflows require tokenized approval
   - chatlas validates member coordinates, preserves member order, derives the `chatlas` namespace and user tag, registers through anchory, and returns the composed anchor (`c<YYYYMMDD>-<N>u`)
   - the raw plumbing remains available: `agentos anchory register --depot <chatlas-root>/anchory --namespace chatlas --alloc-prefix <YYYYMMDD> [--tag u|a] --record-json '…'`
4. **Verify.** Resolve the record and neighborhood after registration. Confirm every member is the intended user event and typed cargo references the intended proposal and approval events; for later re-checks, `agentos chatlas views inline --anchor <anchor> [--radius N] --filter turns` returns the neighborhood.
5. **Return the anchor** to the caller, which tags its line: trailing position, `… ^c20260707-0u`.

## Code-Side Evidence

- file-touches are the code-side analogue of chat anchors: `agentos chatlas query --file-touched "<path>"` finds the sessions that actually read/wrote a file (mentions never match), and `views inline --file-write "<path>"` lands on the touching moments — the "find the evidence turn" step for code changes

## Anchor Discipline

- an anchor for index grounding targets a USER turn — touch is the landing point, assistant context is recovered by neighborhood reading; when the wording originated agent-side, anchor the approval turn
- event identity is `<session-identity>:<event-id>`; timestamps are readability metadata and never the registration key
- a tokenized approval anchor has one user support member whose `tokenized.approval.turn` cargo points to the assistant proposal and user approval events
- an anchor's meaning is immutable: no reuse; a wrong hint or wrong date means minting a new anchor, never repurposing
- `agentos anchory amend` exists only to correct an error or improve resolution of the same context
- the hint is the desync tripwire: write it so a reader can tell whether the resolved neighborhood matches
- the register is plumbing, not truth — the information lives on the surfaces; agents detect desync by reading them
- one anchor per claim: if two lines ground on the same neighborhood, they may share the anchor

## Resolution (reading an anchor)

- `agentos chatlas views inline --anchor <anchor> [--radius N] --filter turns` — resolves through the chatlas anchory depot and returns the landing-turn neighborhood as a clean model fragment; read the landing turn and around it
- `Chatlas.Filter` presets tune the noise: `turns` (message turns, plumbing stripped) is the grounding reader's default; drop the flag when you need full envelopes (`source_refs`, event ids)
- `agentos anchory resolve --depot … --anchor <anchor>` remains the record-level (plumbing) view
