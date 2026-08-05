# Chat.Index ↔ Project.Index Redesign - design-req

status: Open

## Session.Abstract

- **target:** complete the chronological `Chat.Index`, integrate it with Project Indexes, and evolve the Project Index into a complex HEAD projection
- **current concern:** close the Project Index surface model while the Chat Index capture-plan implementation proceeds in another session
- **settled frame:** Chat Indexes preserve complete touched reasoning evolution; Project Indexes contain only currently relevant model and issue state
- **rollout order:** Chat Index → Project integration → Project Index migration
- **next useful move:** define the `Issue.Block` format, surface-specific line-type sets, and anchor gates; then incorporate feedback from the capture-plan implementation

## Design.Index

### Redesign.Program

- `Chat.Index` redesign and Project integration are prerequisites for reconsidering the Project Index structure
- the Project Index redesign is deliberately last because it is the broadest and most expensive migration
- the intermediate product keeps the current Project Index layout while adding Chat homes, support-chat routing, reconciliation state, and POI feedback
- each phase must produce a usable system; no phase exists only as scaffolding for a later rewrite
- the program is one design lifecycle tracked in this artifact; implementation requests may split by owning project and executable slice

### Authority.And.Projection.Stack

```text
Live.Chat
→ Project.Index
→ Project.Support.Chats
→ Chat.Indexes
→ Chat.Transcripts
→ qualifying User.Turns
```

- qualifying `User.Turn`s remain the present first-order `Touched.Data` authority units
- `Chat.Transcript` is the preserved source evidence; assistant turns provide reasoning context and provenance without independently conferring touched authority
- `Chat.Index` is the canonical indexed home closest to the source evidence, not the authority source itself
- `Project.Index` is an independently editable current projection; it may develop before or after its Chat home and is reconciled eventually rather than transactionally constrained
- `Project.Support.Chats` is the routing boundary defining the project's relevant session universe

### Chat.Index.Target

- `Chat.Index` preserves the complete evolution of one chat's indexed reasoning rather than flattening the session into one ontology-shaped summary
- its chronological unit has the working name `User.Turn.Index`
- a `User.Turn.Index` is attached to one qualifying user turn; that turn marks the end of its evidence scope
- the evidence horizon is fixed, but the maintained extraction is mutable: agents may extend, correct, reorganize, or amend it using only evidence inside its causal horizon
- scope follows the user turn's visible causal ancestry; it does not indiscriminately include abandoned branches merely because their events have smaller tape sequence values
- each unit focuses on the anchoring user turn, interprets relevant preceding context, attaches preferentially to the ontology visible at that time, and avoids unnecessary repetition
- later turns may refine or reject earlier positions without rewriting the earlier reasoning history
- the Chat Index may expose a current/head projection, but its defining product is the maintained reasoning tape

### Line.Home

- every indexed line may have one canonical `Line.Home` in a Chat Index, identified by session and turn-index coordinates
- the issuing/capturing agent defaults the home to the active chat because it holds fresh `User.Attention` and the richest semantic neighborhood
- a line may accumulate support and provenance observations from many chats while retaining one home
- `Line.Home` is independent from `Known.Origin`, `Support.Set`, review standing, and Project Index membership
- a Project-only line is valid intermediate state; missing Chat home is a reconciliation `POI.Instance`, never an authoring error
- a Chat-only line is normal reasoning-tape content and does not imply Project promotion

### Line.Provenance

- `Line.Provenance` is a line-content dossier independent from touched authority
- `Known.Origin` is the earliest currently known observation of canonical line content within the searched evidence scope
- discovering older evidence extends the dossier and moves the derived known-origin claim backward; observations are appended rather than overwritten
- Chatlas may contribute exact chat observations; Git may contribute first-known tracked materialization and write-commit evidence when available
- an origin observation may be a user or assistant turn and does not confer authority
- passive contextual loading, first observation, user support, canonical home, and review standing remain separate judgments

### Project.Chat.Integration

- the desired steady-state relation is that every live Project Index line has a canonical home in one of the project's support Chat Indexes
- this relation is a maintenance assertion, not a development constraint: either surface may advance first
- the `POI.Linter` surfaces structural divergence such as missing home, unavailable support chat, unavailable Chat Index, unresolved provenance, or home/content drift
- POIs direct attention and reconciliation; they do not automatically block edits or dictate which surface must change
- reconciliation is incremental: maintain a cursor per Project Support Chat and inspect unreconciled `User.Turn.Index` tails by default
- maintenance agents produce live artifacts with findings and route worthwhile unresolved material into the current Project Index's agendix during the compatibility phase
- explicit rejection/supersession relationships may make some semantic POIs CPU-detectable; otherwise agents perform semantic comparison over the narrowed new-line set

### Contradiction.Router

- a contradiction router states: "These grounded positions appear incompatible and require attention."
- it is an agent-authored indexed interpretation over two or more grounded lines and their underlying user-turn evidence
- it identifies its target lines, remains unresolved until user review, and does not prescribe which target or projection must change
- during the compatibility phase it remains active in the existing Project Agendix and permanent in its Chat Index home
- user resolution changes the current Project model and produces a decision line; the original reasoning history remains in Chat Index

### Project.Index.Target

- `Project.Index` is one complex HEAD object: everything it contains is currently relevant, while review, grounding, and authority remain line-anchor properties
- the accepted ontology is organized into configurable `Index.Chapter`s; each chapter defines its applicable gates and surface policy
- `design` is the default chapter and the only chapter configuration implemented initially, not the semantic boundary of accepted fundamentals
- `Index.Appendix` preserves accepted depth outside chapter fundamentals
- `Index.Agendix` preserves current agentic and unreviewed model capture
- `issues/` is a built-in ontology surface containing current `Issue.Block`s
- `poi/` remains the catalog of POI classes and documentation; concrete project problems live in `issues/`
- support and reconciliation mechanics remain intentionally outside this initial folder decision

```text
<Index.Depot>/
├── 000-INDEX.md
├── 009-SUPPORT-CHATS.md
├── <chapter>/
│   └── NNN-<chapter>.md
├── appendix/
├── agendix/
├── issues/
│   └── NNN-issues.md
└── poi/
    └── NNN-poi.md
```

### Issue.Block

- every Project model evolution is represented through an `Issue.Block`, analogous to a GitHub issue
- an issue has a stable rolling numeric identity and may add an optional descriptive `Dotted.Name`
- an `Issue.Block` may contain every Index.Line needed to state, investigate, and resolve its subject
- resolving an issue may produce multiple edits: normal Design.Line changes on their natural ontology or appendix surfaces and gated Resolution.Lines recording the decision inside the issue
- POI.Lines and Resolution.Lines are special-purpose Index.Lines; their permitted surfaces and type sets remain open design work
- review standing is recorded by each line’s anchor record rather than inferred from its folder

### Project.Index.Target.Lifecycle

```text
Change, problem, or request detected → Issue.Block
Unreviewed model capture             → Agendix
User resolution                      → accepted model edits + Resolution.Lines
Resolution remains relevant          → Issue.Block remains in Project.Index
Resolution ceases to matter          → leaves Project.Index; remains in Chat.Index and Git
```

### Rollout.Principles

- preserve source authority and provenance while allowing projections to be maintained and corrected
- prefer foreground capture by the agent with fresh context; retrospective mining is repair, enrichment, and migration fallback
- keep automatic Chat Index capture separate from reviewed Project Index landing
- treat structural divergence as POIs and expected intermediate state, not as transactional failure
- keep every phase reversible at the projection layer; do not destroy Chatlas source data or Git history
- preserve the low-migration chapter, appendix, agendix, issues, and POI-catalog layout as the current Project Index target; defer deeper syntax, support placement, and migration mechanics until the intermediate integration has been exercised

## Rollout.Plan

### Phase 0 - Baseline And Design Closure

- map the current `Chat.Index` capture product, stored session-index corpus, capture skill, anchory records, and consumers
- identify the smallest schema evolution that can coexist with current `ontology/` and `appendix/` products during migration
- settle the WIP names and semantic boundaries needed for implementation: turn-index unit, causal horizon, Chat head projection, line home, and provenance dossier
- define compatibility and migration invariants before mutating stored Chat Indexes

### Phase 1 - Redesign Chat.Index

- define and materialize the ordered user-turn-anchored reasoning units
- retain mutable extraction with fixed causal horizons and lineage-aware scope
- add line-home and line-provenance records without conflating them with support or authority
- evolve foreground capture so the current agent can maintain the active Chat Index while context is fresh
- preserve a retrospective capture/rebuild path for closed and legacy sessions
- expose incremental query/read operations over new reasoning units and optional current/head projection
- validate against representative sessions containing loaded indexes, new lines, revisions, rejections, branches, and repeated wording

### Phase 2 - Integrate With The Existing Project.Index

- keep the existing ontology/appendix/agendix structure and its gates unchanged
- complete `Project.Support.Chats` as the explicit project-to-session routing surface
- allow Project lines to declare or resolve a Chat home; emit missing-home and availability POIs without blocking Project-first development
- maintain per-chat reconciliation cursors and scan only new Chat Index units by default
- produce agent-maintained live reconciliation reports and capture selected candidates or contradiction routers into the existing agendix
- exercise both directions: Chat-first promotion and Project-first home reconciliation
- pilot the complete loop on `agentos-pkg` before generalizing the workflow

### Phase 2A - Learning Gate

- operate the compatibility system long enough to observe capture cost, POI noise, reconciliation frequency, home assignment, provenance usefulness, and real loading patterns
- record which current Project Index mechanics remain useful and which create friction
- do not begin Project Index migration until the pilot demonstrates that Chat Index homes and incremental reconciliation are trustworthy and useful

### Phase 3 - Redesign Project.Index

- retain the existing chapter, appendix, agendix, POI-catalog, and router conventions
- add `issues/` as the single new core surface
- define `Project.Index` as one complex HEAD containing the current ontology, unreviewed capture, and current Issue.Blocks
- define the `Issue.Block` identity, content model, resolution lifecycle, and routing rules
- define the permitted and preferred Index.Line types for chapters, appendix, agendix, and issues
- keep review and grounding standing in line-anchor records rather than deriving them from placement
- migrate the current live model without importing obsolete history merely to preserve the old shape
- update capture, grounding, routing, and POI linting around the new Issue.Block workflow
- run a cold-read and maintenance pilot before declaring the old structure retired

## Progress.Ledger

States: `planned`, `in-progress`, `blocked`, `done`.

| Slice | Outcome | Owning surface | Depends on | State | Evidence / notes |
|---|---|---|---|---|---|
| 0.1 | Current Chat Index implementation and corpus map | chatlas md/py | - | done | v1 corpus and all capture/consumer surfaces inspected |
| 0.2 | Redesigned Chat Index concept and compatibility contract | chatlas md + agentos md | 0.1 | done | Delta/HEAD v2 contract landed |
| 0.3 | Migration and validation fixture plan | chatlas md/py | 0.1, 0.2 | done | v1 compatibility plus medium-chat v2 fixtures |
| 1.1 | User-turn-anchored reasoning-unit storage | chatlas py | 0.2, 0.3 | done | `capture.json` v2, `deltas/`, and `HEAD.md` |
| 1.2 | Line home and provenance dossier | chatlas py + anchory | 0.2 | done | v5 line dossier, monotonic observations/context, Known.Origin, and recomputed oldest-Delta home |
| 1.3 | Foreground incremental Chat Index capture | chatlas skill/py | 1.1, 1.2 | done | Capture.Plan apply plus real Delta-only maintenance preserve complete HEAD |
| 1.4 | Retrospective rebuild and legacy compatibility | chatlas skill/py | 1.1, 1.2 | done | v1 remains readable; v2 is the only write target |
| 1.5 | Chat Index query, validation, and behavioral tests | chatlas py + testground | 1.1-1.4 | done | 382-test suite; medium-session growth/revision/idempotency E2E |
| 2.1 | Project Support Chats registry and maintenance workflow | agentos md + chatlas py | existing 606 Impl.Req | done | `notes/live/606-project-support-chats-impl-req.md` |
| 2.2 | Project-line Chat-home POI checks | agentos md/py + chatlas py | 1.2, 2.1 | done | one bulk advisory HEAD/Delta/home/dossier coverage audit |
| 2.3 | Per-chat reconciliation cursors and incremental scan | agentos/chatlas | 1.5, 2.1 | done | project-local current/append-only/revised/reset cursor model |
| 2.4 | Live reconciliation report and agendix capture workflow | agentos md | 2.2, 2.3 | done | structured candidates plus grounded Issue.Block routing |
| 2.5 | Hugentics compatibility pilot | agentos-hugentics | 2.1-2.4 | done | real open bootstrap issue and current-chat Delta backfill |
| 2A.1 | Compatibility-system observation report | agentos md | 2.5 | done | Impl.Req 608 records pilot debt/noise and the low-migration cutover decision |
| 3.1 | Final Project Index product and file-format contract | agentos md | 2A.1 | done | existing layout retained with one first-class `issues/` surface |
| 3.2 | Project Index migration workflow | agentos md/py | 3.1 | done | Hugentics pilot preserves exact moved line content and anchors |
| 3.3 | Capture, grounding, and linter cutover | agentos md/py/cli | 3.2 | done | issue policy, review resolution, dossier context, and reconciliation checks composed |
| 3.4 | Cold-read and maintenance validation | tests + pilot project | 3.3 | done | synthetic lifecycle plus real Hugentics issue/audit/Skillware pass |
| 3.5 | Retire old Project Index structure | agentos md | 3.4 | done | obsolete multi-HEAD proposal rejected; compatible chapters/appendix/agendix retained with `issues/` added |

## Decision.Gates

| Gate | Required evidence | State |
|---|---|---|
| Chat.Index.Design.Ready | current implementation map, settled semantic unit, compatibility/migration contract | met |
| Chat.Index.Pilot.Ready | foreground and retrospective capture pass representative behavioral tests | met |
| Project.Integration.Proven | support-chat routing, home POIs, incremental reconciliation, useful pilot reports | met |
| Project.Index.Redesign.Ready | compatibility observation report shows the provisional target solves observed needs | met |
| Old.Project.Index.Retirable | migrated current model, cold-read success, capture/grounding/linter cutover verified | met — the compatible structure was extended rather than replaced |

## Session.Notes

### Settled

- `Project.Index` is one complex HEAD object rather than several independent HEADs
- `design` is the default implemented `Index.Chapter`, not the boundary of the ontology
- Project model evolution is organized through current `Issue.Block`s
- resolved issues remain only while their decision rationale conditions the current model
- complete evolution belongs in Chat Indexes and Git, not in a Project-local historical archive
- complete reasoning history belongs in the Chat Index layer; the Project Index should not carry history merely to preserve provenance
- Project-first development remains legal; Chat-home completeness is maintained through POIs and reconciliation
- `Known.Origin` helps distinguish first-known occurrence from loaded context but does not confer authority or select the canonical home
- line support, provenance, home, review standing, and Project membership are orthogonal
- contradiction detection is normally semantic agent work over incremental new lines; explicit relations can make selected cases CPU-checkable
- unresolved contradiction routers are appropriate agent captures because checking and surfacing incoherence is part of index maintenance

### Open Design Questions

- exact causal-scope rule over branch and fork lineage; the first implementation deliberately assumes linear chats
- richer Issue.Block rendering, tags, and surface-specific preferred line-type vocabularies after the bootstrap issue is used
- qualification of Issue identities if one line dossier participates in identically numbered Issue.Blocks from several Project Index namespaces

### Explicitly Deferred

- final `[+TYPE]` or other novelty syntax
- generic CPU inference of semantic contradiction from natural-language lines
- immediate migration of ontology/appendix/agendix
- treating Project↔Chat divergence as an error or write-time gate

## Session.Log

- 2026-08-03: created the consolidated redesign and rollout tracker from the Chat Index / Project Index design discussion
- 2026-08-03: selected staged rollout—Chat Index redesign, compatibility integration with the existing Project Index, learning gate, Project Index redesign last
- 2026-08-03: linked the active `Project.Support.Chats` implementation as an in-progress dependency rather than duplicating its execution plan
- 2026-08-04: implemented and verified the chronological Delta/HEAD v2 surface, oldest-Delta Line.Home, v1 read compatibility, and medium-session E2E coverage
- 2026-08-04: implemented read-only incremental tail maintenance with current, append-only, expanded, revised, diverged, and blocked states; active-session smoke found 11 pending turns and left the retained surface unchanged
- 2026-08-05: Impl.Req 608 completed v5 line dossiers, bulk Project/Chat coverage, incremental reconciliation, first-class Issue.Blocks, and the low-migration Project Index cutover
- 2026-08-05: migrated the first independent `agentos-hugentics` Index, left one healthy grounded bootstrap issue open, and backfilled the real supporting chat through a Delta-only Capture.Plan that preserved Chat HEAD
