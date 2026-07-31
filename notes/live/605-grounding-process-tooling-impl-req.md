# Grounding Process Tooling - impl-req

## Impl.Abstract

- **goal:** implement and continuously streamline the end-to-end process for grounding existing Index lines in historical Chatlas evidence
- **scope:** compose Git dating, Chatlas turn discovery, support-set registration, anchor landing, and focused Index validation into explicit Agentos tooling
- **status:** active implementation program; Slice 1 complete, Sidequest A ready for implementation
- **source:** the completed `Natural.Placement` stress test and the user's request for one durable file that accumulates the program's design and implementation state ^c20260731-11u
- **owning projects:** `agentos-chatlas-py`, `agentos-py`, `agentos-cli`, and the affected workflow surfaces in `agentos-md`
- **out of scope:** changing Index claims, automatically judging semantic support, reading provider-native stores directly, replacing `Event.Pattern`, or making a derived database authoritative
- **acceptance:** an agent can move from one ungrounded block to verified landed anchors without ad hoc `jq`, manual identity copying, partial-surface linter noise, or a second query model

## Impl.Agendix

- **touched (chat):** the user requested a durable implementation program whose goal is implementing and streamlining grounding ^c20260731-11u
- **touched (index):** `Touched.Index`, `Support.Set`, `Context.Grounding`, `Index.Linking`, `Git.Dating`, and `Index.Chat.Capture` define the evidence and linking workflow
- **touched (index):** `Chatlas.Query.Surface`, `Chatlas.Session.Model`, and `Chat.Support.Set` constrain Chatlas discovery and support records
- **structural:** `agentos-chatlas-py/src/agentos_chatlas/event_pattern.py` and `event_query.py` already provide the backend-neutral query model, authoritative scan evaluator, and disposable SQLite candidate backend
- **structural:** `agentos-chatlas-py/src/agentos_chatlas/anchory.py` already validates and registers ordered user-turn support sets
- **structural:** `agentos-py/src/agentos/index/commands.py` and the parser-backed Index model already expose linter scopes, block statistics, and resolvable support-reference checks
- **open space:** query sugar, focused report presentation, and campaign ergonomics remain implementation choices as long as they preserve the boundaries below

## Impl.Index

### Grounding.Process.Target

- the supported workflow is: inspect block -> date wording -> discover candidate turns -> inspect neighborhoods -> select user support -> preview and mint support set -> select supported lines -> land anchor -> lint focused result
- every stage emits structured output that the next stage can consume without reparsing presentation text
- stages remain independently callable so agents can replace heuristics or explore directly when a mechanical path is insufficient
- the workflow must support one line, one block, or a larger grounding campaign without changing evidence semantics

### Semantic.Judgment.Boundary

- tooling discovers candidates, validates coordinates, mutates explicit anchor suffixes, and reports deterministic POIs
- the agent decides whether a turn supports a statement, which user turns enter the ordered support set, and which lines the set supports
- assistant turns and tool events may participate in retrieval heuristics and neighborhoods but do not become ordinary `Chat.Support.Set` members
- no command automatically attaches one block-level anchor to every line

### Authoritative.Query.Boundary

- `Event.Pattern` remains the logical query model; ergonomic CLI flags compile into it rather than bypassing it
- scan and SQLite remain interchangeable candidate backends
- every public match is reloaded and re-evaluated against the current authoritative `Chatlas.Session.Model`
- SQLite remains disposable and may return only candidate coordinates; it never produces authoritative public events
- event-time constraints concern matched turns, not only a session's `last_activity_at`
- callers may bound verbatim discovery with matched-turn before/after dates derived from Git or other hints ^c20260731-12u

### Chatlas.Verbatim.Finder

- `Chatlas.Verbatim.Finder` is the first deterministic candidate heuristic for backward grounding: search for a line's alphanumeric material sequence inside Chatlas turns ^c20260731-12u
- canonicalization is `NFKC` -> casefold -> retain Unicode alphanumeric characters; capitalization, punctuation, and whitespace do not affect a match ^c20260731-12u
- Index machinery that is not line material, including trailing anchors, is removed before canonicalization
- matches are ordered oldest-first by default because the earliest occurrence is usually closer to content production, while remaining only a retrieval hint
- explicit event-time bounds narrow candidate discovery before authoritative normal-model evaluation ^c20260731-12u
- the finder is only a query: it returns matching `Normal.Turn` objects with their neutral session identity and never materializes neighborhoods ^c20260731-13u
- a separate Chatlas command consumes those coordinates when the agent wants the turn neighborhood ^c20260731-13u
- the finder may return assistant or user turns because an assistant proposal can contain the line before a user approval; only later agent selection establishes support members

### Grounding.Handoff

- turn-query results return authoritative `Normal.Turn` objects plus neutral session identity, without duplicating a second grounding-specific turn projection ^c20260731-12u
- turn-query results must identify the exact matched `Event.Ref` values inside each returned `Normal.Turn`; the grouping alone does not show which message satisfied the predicate
- the returned coordinates are sufficient to request a turn neighborhood or derive an Anchory `<identity-hash>:<turn-id>` member reference
- neighborhood retrieval belongs to another Chatlas command, not an option or projection of the finder query ^c20260731-13u
- Anchory accepts those member references in relevance order, previews their neighborhoods, and mints one immutable support-set meaning
- equivalent existing support sets surface a POI; tooling does not silently merge or rewrite anchors
- Index landing accepts explicit stable line identities and fails closed if line material changed after selection
- anchor-only maintenance does not reopen the line's verbatim-content gate

### Focused.Validation

- block-focused linting runs checks over the complete configured depot but reports only the selected block's findings, checks, and coverage
- partial grounding reports grounded and ungrounded lines, not only `Block.Ungrounded`
- campaign priority separates grounded-line coverage from support-reference diversity; a 6/6 block with one shared anchor is complete even though its `Grounding.Density` is only 1/6
- grounding provenance verifies every cited support reference and preserves the POI class/documentation path
- focused operation must not configure one chapter file as an incomplete depot and flood output with unrelated router findings

### Program.Artifact.Maintenance

- this Impl.Req is the working desk for the grounding-tooling program
- after each implemented slice, update its status, observable result, checks, implementation ledger, and any boundary-affecting deviation
- new design decisions enter `Design.Decisions`; implementation facts enter `Implementation.Ledger`; ordinary code diffs stay in Git
- when a later slice becomes concrete, refine that slice before execution instead of prematurely fixing all incidental interfaces now

### Tested.Baseline

- target: `Natural.Placement` in `agentos-pkg/design/100-design.md`
- Git isolated the May 2026 content-bearing history
- Chatlas session queries found historical sessions, while `views inline` plus local `jq` recovered exact human user turns
- five user turns across three sessions were manually assembled into `^c20260511-0u`
- the anchor was manually applied only to supported lines; focused block statistics reported 6/10 grounded kernel lines
- provenance lint passed with zero errors, but partial-file linter invocation emitted unrelated router warnings
- this baseline is a workflow acceptance fixture, not a requirement to reuse the operator's live anchor in automated tests

### Tested.Placement.Balance

- target: zero-grounding `Placement.Balance` in `agentos-pkg/design/100-design.md`
- Git isolated an original six-line draft and a later three-line vocabulary rewrite from authority language to neutral origin-surface language
- exact alphanumeric lookup found the three unchanged current lines immediately; the three rewritten lines correctly returned no exact current-wording match
- a broader concept-name query recovered the original user conception, the finalized draft/write sequence, and the later user correction across three sessions
- the ordered three-member support set was registered as `^c20260522-0u` and applied to all six jointly supported lines
- `agentos index blocks` reported 6/6 grounded lines and one unique anchor; `Grounding.Provenance` passed with zero findings
- manual glue remained: shell-safe line extraction, Git retrieval of historical wording, neighborhood lookup by identity plus timestamp, duplicate search, line mutation, and local filtering of file-scoped lint output

### Tested.Cited.Duplication

- target: zero-grounding `Cited.Duplication` in `agentos-pkg/design/100-design.md`
- Git placed the current block in the May 22 consolidation history, while literal block-name lookup found only assistant-side inspection of already-produced wording
- a session-first `--user-contains duplication` search located the relevant historical sessions; identity-scoped authoritative turn scans then returned candidate user turns quickly
- the selected two-member support set was registered as `^c20260516-0u`; its members establish limited duplication for surface self-sufficiency and explicit in-context concept citation
- the registered support is intentionally line-scoped: it supports the block's core cited-duplication frame, not the later maintenance and drift claims
- the anchor was applied directly to those two lines because anchor suffix maintenance is outside the verbatim Index gate; the grounding request supplied the write trigger without requiring an edition-approval token
- registration output verified that each selected `Normal.Turn` contains only the human user interaction while neighboring assistant messages use separate assistant turn annotations
- the run exposed a sequencing hazard: broader candidate archaeology found an additional strong user turn only after the immutable support set had been minted; non-mutating preview and duplicate detection should precede registration
- five concurrent corpus-wide SQLite turn queries stalled, while identity-scoped scans remained responsive; bounded parallel discovery needs a performance and lock-contention check
- the mutating register command emitted full neighborhoods and more than 10,000 output tokens, reinforcing the need for a compact preview command and on-demand neighborhood retrieval

### Design.Decisions

| Date | Decision | Status |
|---|---|---|
| 2026-07-31 | Reuse `Event.Pattern`; do not create a second turn-query model | accepted |
| 2026-07-31 | Keep normalized Chatlas JSON authoritative and SQLite disposable | accepted |
| 2026-07-31 | Keep semantic support selection agent-owned | accepted |
| 2026-07-31 | Make grounding stages composable instead of hiding them behind one opaque command | accepted |
| 2026-07-31 | Use this Impl.Req as the accumulating design and implementation ledger | accepted |
| 2026-07-31 | Use alphanumeric material equivalence for both review attention and verbatim candidate finding | accepted ^c20260731-12u |
| 2026-07-31 | Bound finder searches by matched-turn dates and return Normal.Turn candidates | accepted ^c20260731-12u |
| 2026-07-31 | Keep the verbatim finder a pure query; neighborhood retrieval is a separate Chatlas command | accepted ^c20260731-13u |
| 2026-07-31 | Treat exact current-line misses as retrieval findings, not evidence absence; Git-guided historical wording and broader concept phrases are required fallbacks | accepted from `Placement.Balance` E2E |
| 2026-07-31 | Support sets may intentionally compose user turns from several sessions when current wording combines an original design, an approval, and a later correction | accepted from `Placement.Balance` E2E |
| 2026-07-31 | Keep grounding coverage and support-reference diversity as separate campaign signals | accepted from `Placement.Balance` E2E |
| 2026-07-31 | Attach historical support only to the lines it actually establishes; partial block grounding is preferable to unsupported block-wide propagation | accepted from `Cited.Duplication` E2E |
| 2026-07-31 | Complete broad candidate discovery and non-mutating support-set preview before minting an immutable anchor | accepted from `Cited.Duplication` E2E |

## Execution.Plan

### Sidequest A - Alphanumeric review equivalence

- change the review-attention gate canonicalizer from casefolded non-whitespace text to casefolded Unicode alphanumeric text ^c20260731-12u
- share the canonical material-equivalence primitive with `Chatlas.Verbatim.Finder` so the gate and retrieval heuristic cannot drift
- keep the gate's existing proposal, token, ordering, role, and approval checks unchanged
- RED: punctuation-only changes currently fail material equivalence
- GREEN: capitalization, punctuation, and whitespace changes pass; any alphanumeric change still fails
- **observable:** review attention is treated as a robust signal rather than punctuation-sensitive proof
- **status:** not started; ready

### Slice 1 - Ergonomic authoritative turn query

- add `agentos chatlas turns query` as a named ergonomic surface compiled to `Event.Pattern`
- add `Chatlas.Verbatim.Finder` through an alphanumeric-material predicate and oldest-first selection ^c20260731-12u
- support human/producer and role filters, exact/contains/regex text predicates, matched-turn before/after windows, project/session selectors, and bounded result selection
- return authoritative `Normal.Turn` matches plus neutral session identity; a different Chatlas command owns neighborhood retrieval ^c20260731-13u
- extend the SQLite candidate schema only as needed for equivalent candidate discovery; retain authoritative normal-model re-evaluation
- RED: the Natural.Placement-style query requires session search, `views inline`, and local projection to obtain member references
- GREEN: one turn query returns candidate human turns and member references, with scan/SQLite agreement and stale-SQLite fallback tests
- **observable:** no ad hoc `jq` is needed between Chatlas discovery and Anchory selection
- **status:** complete

### Slice 2 - Git-guided Index grounding inspection

- add an Index grounding inspection command for an exact block path
- report current kernel lines, stable material identities, existing anchors, grounded state, Git blame/content commits, and suggested search windows and phrases
- include historical material variants for lines changed by later commits so the turn finder does not depend only on current wording
- emit a structured, shell-safe query handoff; agents should not have to interpolate backtick-bearing Index lines into shell source
- keep Git as a hint source; it never becomes grounding evidence
- RED: an agent manually combines block parsing, blame, log history, and line text
- GREEN: one structured inspection result provides the complete mechanical starting state
- **observable:** the agent can begin backward grounding from one command without manually reconstructing line history
- **status:** planned; refine before execution

### Slice 3 - Support-set preview and duplicate POI

- add a no-write preview path that validates selected member references and returns their ordered neighborhoods
- accept Anchory-ready `<session-identity>:<turn-id>` references directly; agents should not have to recover and pass a timestamp to inspect a candidate
- detect an equivalent existing support set and surface a structured POI naming the candidate and existing anchor
- preserve current immutable member meaning and application-owned validation
- RED: uncertain registration or output handling can mint an equivalent second anchor
- GREEN: preview is non-mutating and duplicate candidates are explicit without automatic merge
- **observable:** the agent verifies the exact support set before minting and can reason about duplicates deterministically
- **status:** planned; refine before execution

### Slice 4 - Explicit anchor landing

- add an Index grounding landing command accepting one anchor and repeatable stable line identities within one exact block
- verify the anchor and selected material before mutation, append only the support suffix, and fail closed on stale identities or ambiguous blocks
- return the changed lines and the focused validation command/result
- RED: landing requires manual text edits and manual post-edit targeting
- GREEN: selected lines receive the anchor without changing line material or reopening verbatim approval
- **observable:** semantic selection remains visible while mutation and stale-line protection are mechanical
- **status:** planned; refine before execution

### Slice 5 - Block-focused coverage and linting

- add exact block selection to `agentos index blocks` and `agentos index linter`
- run linter checks over the complete depot while filtering findings, check summaries, and coverage to selected block paths
- include stable identities and excerpts for grounded and ungrounded kernel lines in structured output
- expose grounded-line coverage and unique-support density independently, and let campaign worklists prioritize unresolved coverage
- RED: a single-file invocation emits unrelated router warnings and block coverage only summarizes the count
- GREEN: one focused command reports the target block's provenance and precise partial-grounding state
- **observable:** the Natural.Placement result reads as 6/10 with the four unsupported line identities and no unrelated router flood
- **status:** planned; refine before execution

### Slice 6 - Workflow integration and E2E regression

- update Hugentics `--back-link`, grounding survey, and review modules to prefer the new primitives while preserving agent judgment and direct exploration
- add an isolated fixture that executes inspect -> query -> preview/register -> land -> focused lint across the composed command boundary
- document the command sequence at the workflow surface rather than duplicating subsystem design
- compare command count, manual projection steps, and focused output against `Tested.Baseline`
- **observable:** the supported workflow completes without local parsing glue and retains the same evidence semantics
- **status:** planned; refine after Slices 1-5

## Implementation.Ledger

| Slice | State | Result | Verification |
|---|---|---|---|
| Baseline | complete | `Natural.Placement` grounded to `^c20260511-0u`; 6/10 kernel lines linked | anchor resolution and Index provenance lint passed |
| E2E 2 | complete | `Placement.Balance` grounded to `^c20260522-0u`; 6/6 kernel lines linked through a three-session support set | anchor resolution, block statistics, and Index provenance lint passed |
| E2E 3 | complete | `Cited.Duplication` partially grounded to `^c20260516-0u`; 2/7 kernel lines linked to the two-member support set | v3 record resolution, turn-boundary inspection, block coverage, and provenance lint passed |
| Sidequest A | not started | - | - |
| 1 | complete | `agentos chatlas turns query` returns authoritative `Normal.Turn` groupings and Anchory-ready member references through ergonomic Event.Pattern predicates | 22 focused tests pass; scan/SQLite real-corpus outputs agree; 12,062-session SQLite verbatim query completed in under 3 seconds while loading five candidate models |
| 2 | not started | - | - |
| 3 | not started | - | - |
| 4 | not started | - | - |
| 5 | not started | - | - |
| 6 | not started | - | - |

## Impl.Log

- 2026-07-31: program primed from a successful real-corpus E2E stress test
- 2026-07-31: execution of Slice 1 authorized ^c20260731-14u
- 2026-07-31: inspection confirmed Event.Pattern, scan/SQLite candidate backends, authoritative model re-evaluation, support-set registration, block statistics, and linter scopes already exist
- 2026-07-31: the main gaps are ergonomic turn-level projection, Git/block inspection, preview and duplicate reporting, safe landing, and block-focused validation
- 2026-07-31: the review gate and verbatim finder will share alphanumeric material equivalence; finder results are date-bounded Normal.Turn candidates ^c20260731-12u
- 2026-07-31: clarified that the finder never returns neighborhoods; agents pass its turn coordinates to a separate Chatlas neighborhood command ^c20260731-13u
- 2026-07-31: Slice 1 implemented `chatlas turns query` with exact, contains, regex, alphanumeric-verbatim, producer, role, matched-event time, session, project, ordering, and result-limit predicates
- 2026-07-31: SQLite schema v4 indexes producer, event time, exact/casefolded text, regex candidates, and alphanumeric material; it narrows sessions before loading models, while every public turn is reloaded and re-evaluated from the authoritative normal model
- 2026-07-31: real-corpus `Natural.Placement` discovery found five candidate sessions and eleven turns without neighborhood projection; a scoped scan/SQLite comparison returned identical turns
- 2026-07-31: second E2E grounded `Placement.Balance` with `^c20260522-0u`; exact lookup recovered unchanged lines while Git plus broader concept search recovered later semantic rewrites
- 2026-07-31: the second E2E exposed that full `Normal.Turn` output is large and does not identify the matching event, shell interpolation is unsafe for literal backtick-bearing lines, and exact-block validation still requires local filtering
- 2026-07-31: a fully grounded 6/6 block reported `gr_density=0.1667`, confirming that coverage and support diversity must not be conflated in campaign priority
- 2026-07-31: third E2E registered and landed `^c20260516-0u` for `Cited.Duplication`; evidence supports only the core cited-duplication frame, so landing remains deliberately partial
- 2026-07-31: third E2E confirmed human-only user turn groupings in real registration neighborhoods and exposed corpus-query contention, oversized mutating registration output, and the need to preview before minting
- execution should continue with Sidequest A or refine Slice 2; later slices remain intentionally less specified until earlier feedback changes their natural shape
