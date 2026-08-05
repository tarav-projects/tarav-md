# Touched.Index Full Line Lifecycle And Hugentics Pilot - impl-req

## Impl.Abstract

- **goal:** complete the new `Touched.Index` line lifecycle across Chat Indexes, Project Indexes, anchor dossiers, Issue.Blocks, documentation, Hugentics workflows, POI linting, migration, and end-to-end validation
- **status:** ready for implementation
- **source:** the maintained redesign in `notes/live/607-chat-project-index-redesign-design-req.md`, completed Chat.Index mechanics in `agentos-chatlas-py/notes/live/555-chat-index-capture-plan-audit-impl-req.md`, completed support-chat routing in `notes/live/606-project-support-chats-impl-req.md`, current repository inspection, and the implementation/pilot authorization in this session
- **authority:** the user requested the full implementation, required indexes/documentation/linting to close together, selected a deliberately minimal first Issue.Block format, defined issues as any temporary topic rather than only problems, and selected `agentos-hugentics` as the first migrated Index with a real bootstrap review issue ^c20260805-0u
- **first pilot:** initialize and migrate an independent `agentos-hugentics` Index depot, then leave `Issue.I0001.Bootstrap.Review` open for a later real user review
- **owning projects:** `agentos-py` owns generic Index parsing, surface policy, issue modeling, linter orchestration, POI adaptation, and CLI-neutral library seams; `agentos-chatlas-py` owns Chat.Index, Chatlas support/provenance records, cross-surface reconciliation, and Chatlas-backed checks; `agentos-cli` owns dependency injection and command composition; `agentos-md` owns the Hugentics Index, authored Skillware workflows, Agentos POI catalog, design documentation, and the pilot; `agentos-chatlas-md` owns Chatlas package documentation and capture workflow documentation
- **dirty baseline:** Impl.Req 555 is implemented and green but its owning Chatlas repositories contain uncommitted work; preserve and build on that state without resetting or rewriting unrelated product work
- **execution boundary:** this is one master request with ordered vertical slices; an executor may use focused subordinate implementation notes only when repository ownership genuinely requires a handoff, while this artifact remains the completion ledger

### Completed Prerequisites

- Impl.Req 555 supplies transcript-only capture evidence, exact-line anchor batching, `Capture.Plan`, deterministic rendering, staged/landed audit, recoverable apply, prefix stability, and medium-chat E2E; its recorded closeout is Ruff clean and 431 tests passing
- Impl.Req 606 supplies `009-SUPPORT-CHATS.md`, anchor-to-session extraction, the support-chat maintenance skill, and the first real registry
- Chat.Index v2 supplies ordered `deltas/`, `HEAD.md`, exact ordinary-HEAD-to-Delta coverage, oldest-Delta `Line.Home`, v1 readability, and linear-session behavior
- the existing Index parser and linter already model router, chapter, appendix, and agendix surfaces with parser-backed checks and Chatlas-injected grounding/review checks

### Scope

- add `issues/NNN-issues.md` as one built-in Project Index surface while preserving all existing chapter, appendix, agendix, POI-catalog, and router conventions
- implement a minimal, fully grounded `Issue.Block` capable of representing good, bad, exploratory, corrective, or administrative temporary topics
- make review and resolution standing derive from line-anchor evidence rather than folder placement or a manually cached status field
- make Project model editions issue-associated without creating a general line-to-line dependency graph
- complete the line-bound provenance dossier with first-known observations, issue context, optional Git observations, and derived Chat.Index home information
- add Project-to-support-Chat reconciliation, per-chat cursors, POI findings, and an agent-facing maintenance workflow
- update every owning Index, generated/hand-authored documentation surface, Package.Skill route, linter catalog, CLI help surface, and project guidance affected by the new model
- migrate `agentos-hugentics` into its own Index depot and exercise the implementation with one intentionally unresolved bootstrap issue
- prove both Chat-first and Project-first line propagation, reviewed issue resolution, and historical recoverability through automated fixtures

### Explicitly Out Of Scope

- no branch-aware Chat.Index capture; the first complete implementation continues to assume linear chats
- no generic CPU inference of natural-language contradiction, rejection, or semantic supersession
- no `open/` and `resolved/` issue directories and no Project-local history/archive folder
- no requirement that Issue.Blocks represent only failures or POIs
- no settled tag vocabulary; v1 may preserve tags as uninterpreted text or metadata but must not make completion depend on a tag taxonomy
- no migration of every Agentos Index in this request; the tooling is general, while `agentos-hugentics` is the only required real migration pilot
- no transactional prohibition on Project-first or Chat-first development; incomplete propagation remains a POI
- no autonomous crossing of the bootstrap issue's user-review gate

## Impl.Agendix

- **touched (chat):** every Project model evolution may be organized as an issue, `design` is only the default implemented ontology chapter, and chapters conceptually define their gates ^c20260805-0u
- **touched (chat):** issues represent any temporary topic, including useful opportunities and problems; all Issue.Block lines remain grounded Touched.Index material ^c20260805-0u
- **touched (chat):** implementation must close indexes, documentation, linting, and the complete line lifecycle rather than delivering only a folder/parser change ^c20260805-0u
- **touched (chat):** `agentos-hugentics` is the first migration target and must contain a bootstrap issue that remains available for later real user review ^c20260805-0u
- **touched (index):** `Touched.Index` is the global system and `Index.Line` is its atomic presentation unit — `agentos-pkg/design/107-design.md` (`Touched.Index`, `Index.Line`)
- **touched (index):** `POI.Line` is grounded maintenance interpretation with its own support, while `Index.HEAD.Reconciliation` makes cross-surface coverage eventual and POI-driven — `agentos-pkg/design/107-design.md`
- **touched (index):** `Reviewed.Content`, `Line.Verbatim.Gate`, and `Edition.Approval.Token` place review evidence in line-local support-reference metadata — `agentos-pkg/design/107-design.md`
- **structural:** `agentos-py/src/agentos/index/model/nodes.py` currently has no issues surface kind
- **structural:** `agentos-py/src/agentos/index/model/parser.py` currently classifies any `NNN-<folder>.md` directory as a generic chapter except appendix/agendix
- **structural:** `agentos-py/src/agentos/index/linter.py` derives chapter, appendix, and agendix surfaces; `issues/` must become explicit rather than accidentally inheriting chapter policy
- **structural:** `agentos-chatlas-py/src/agentos_chatlas/index_checks.py` already resolves grounding, approval, and tokenized verbatim evidence through external linter checks
- **structural:** `agentos-chatlas-py/src/agentos_chatlas/chat_index_audit.py` already computes exact line occurrences and oldest Delta homes in one pass
- **structural:** `agentos-md/skills/agentos-hugentics/.skw/skw.json` currently depends on `../agentos-pkg` but the package owns no `000-INDEX.md`, chapter, appendix, agendix, issues, POI catalog, or support-chat registry
- **structural:** Hugentics runnable documentation is generated from `.skw/src`; implementation edits authored sources and rebuilds, never hand-edits managed targets
- **open space:** the richer tag vocabulary and ergonomics of mature Issue.Blocks remain deliberately open for discussion after the bootstrap issue is used

## Impl.Index

### Completion.Model

The implementation is complete only when one line can traverse and be audited through the entire system:

```text
qualifying User.Turn
→ Chat.Index.Delta
→ Chat.Index.HEAD
→ Project Issue.Block
→ Agendix or accepted ontology/appendix edition
→ reviewed Resolution.Line
→ current Project model
→ retirement from Project HEAD with Chat.Index/Git recoverability
```

The reverse path is equally required:

```text
Project-first Issue.Block/model edition
→ missing-home POI
→ supporting Chat.Index.Delta
→ Chat.Index.HEAD when applicable
→ cleared reconciliation finding
```

### Project.Index.V1.Layout

Keep the low-migration layout:

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

- `Project.Index` is one complex current HEAD object
- ordinary chapters contain accepted ontology fundamentals; `design` remains only the default implemented chapter configuration
- appendix contains accepted depth, agendix contains current unreviewed capture, issues contain current temporary topics, and POI catalog files define reusable POI classes rather than issue instances
- review, grounding, issue association, provenance, and home remain independent line/anchor properties even when surface policy creates a common expected standing

### Issue.Block.V1

Use a deliberately small first format:

```markdown
****

## Issue.I0001.Bootstrap.Review

- [PR] validate the end-to-end review and resolution workflow of the first migrated Hugentics Index ^<grounded-anchor>
```

- identity is `Issue.I####` with a zero-padded rolling number; an optional descriptive dotted suffix may follow without changing the numeric identity
- issue files follow the ordinary chapter numbering rule as `NNN-issues.md`
- an issue may represent any temporary topic: feature, opportunity, question, migration, contradiction, defect, review request, or administrative work
- every Issue.Block line must be typed and grounded; no issue content gains authority merely from placement
- all existing two-character `Line.Type` acts are initially permitted; do not invent a tag or expanded type vocabulary merely to complete v1
- the first reviewed `[DC]` line whose tokenized approval resolves inside the block is a v1 `Resolution.Line`; several reviewed decision lines may participate in one resolution
- Issue.Block state is computed: no reviewed resolution line means open; at least one reviewed resolution line means resolved
- open/resolved are query projections, not directories or manually cached status lines
- resolving an issue normally changes one or more ordinary Design.Lines and adds one or more Resolution.Lines; these are different products of one edition
- a resolved block remains in the Project Index while its rationale conditions the current model and leaves the Project HEAD when it no longer does

### Surface.Policy.V1

- add one generic `Index.Surface.Policy` model consumed by parser/linter/workflow code rather than scattering folder-name conditionals
- built-in chapter policy covers `design` and current custom chapters as reviewed ontology surfaces
- appendix policy is reviewed depth
- agendix policy requires typed grounded lines without reviewed wording
- issues policy requires typed grounded lines and computes reviewed resolution standing line by line
- POI catalog remains a specialized chapter, not an Issue.Block store
- keep the policy API extensible for later chapter-specific gate/type configuration; no new mandatory per-chapter manifest is required for the v1 pilot
- existing depots remain readable without migration, while the new Hugentics depot adopts the complete policy from creation

### Issue.Edition.Closure

- every new Project model evolution is worked through at least one current Issue.Block
- ordinary model lines continue to live only on their natural chapter, appendix, or agendix surfaces; Issue.Blocks record the temporary work and decision, not a duplicate canonical model
- line-anchor dossier metadata may carry one or more Issue.Block identities as edition context; this block association is not a general line-to-line dependency graph
- reviewed model edits and their Issue.Block Resolution.Lines share the same `Edition.Approval.Token` when approved as one edition cluster
- the linter can therefore check that a new reviewed model edition has issue context and a corresponding reviewed resolution without interpreting prose
- pre-migration historical lines are review/migration debt rather than immediate errors; the first Hugentics depot is created under the invariant and must pass it from its first edition

### Line.Provenance.Dossier.V1

- evolve the current line-bound Chatlas support record through a new version rather than changing `chatlas.support-set.v4` meaning in place
- retain v3/v4 readability; new or materially changed Index lines use the new writer
- preserve immutable canonical line subject, ordered support members, member types, and predecessor semantics
- add line-local dossier metadata for Issue.Block context and monotonic provenance observations
- chat observations carry exact `Normal.Turn.Ref` or `Event.Ref` coordinates plus observer role/type; they do not confer authority unless separately selected into the support set
- Git observations may record repository identity, path, commit, and observed materialization when Git is available
- `Known.Origin` is derived as the earliest currently known observation inside the searched evidence set; it is never asserted as universal origin
- provenance enrichment appends observations and may move the derived known origin backward; it never changes line subject or silently replaces support
- `Line.Home` remains derived from exact Chat.Index.Delta containment; dossier metadata may cache/report the resolved coordinate but the audit recomputes it
- when several support chats provide candidate homes without a safe total ordering, report the candidates as a POI instead of inventing causality
- batch grounding, Capture.Plan rendering, audit, anchor amendment validation, and CLI inspection all understand the new record version

### Project.Chat.Reconciliation.V1

- parse `009-SUPPORT-CHATS.md` into exact support-chat identities while preserving the existing maintained Markdown registry
- include `issues/` in support-chat extraction and mandatory-anchor closure
- scan each available support Chat.Index once, reusing its descriptor, HEAD, Delta occurrence map, anchor cache, and audit primitives
- compare canonical `Line.Type + body` identity; attachment/block differences remain semantic agent concerns
- an ordinary live Project model line is covered when it occurs exactly in at least one registered supporting Chat.Index.HEAD and has an exact Delta home there
- Issue.Block/POI/Resolution lines follow their maintenance lifecycle but must still be grounded and materialized in a supporting Chat.Index.Delta; current lines may also participate in Chat.Index.HEAD
- unavailable registry entries, missing Chat.Indexes, missing homes, HEAD/content drift, ambiguous homes, and unsupported issue editions produce stable POI findings rather than write-time errors
- Project-first and Chat-first materialization both remain legal; reconciliation clears findings only after the missing lower/upper projection actually exists
- passive Project content loaded into a chat does not count as new touched Delta material merely because wording matches; the capture agent still selects qualifying user touch from the actual transcript

### Reconciliation.Cursor.And.Artifact

- cursors are machine state under the resolved Agentos project state boundary, never Project Index lines
- one cursor per Project Index/support-chat identity records the last inspected Delta horizon and source descriptor fingerprint
- append-only scans inspect only new or changed Delta units; expanded/revised/diverged source state reopens the affected range
- CPU reconciliation emits deterministic structured findings and candidates
- semantic comparison remains an agent step over the narrowed candidate set and produces a numbered live reconciliation artifact when durable review is useful
- worthwhile current findings become grounded Issue.Blocks; the report itself is not a parallel POI store

### Hugentics.Index.Pilot

- initialize `agentos-md/skills/agentos-hugentics/` as an independent Index depot with `000-INDEX.md`, a default `design/` chapter, `appendix/`, `agendix/`, `issues/`, optional `poi/`, and `009-SUPPORT-CHATS.md`
- keep its declared dependency on `agentos-pkg`; shared Agentos primitives remain there
- inventory blocks presently owned by `agentos-pkg` and migrate only those whose operational/design owner is Hugentics
- preserve exact line content and anchors when moving accepted blocks so line identity, support, and review standing do not churn
- move matching appendix/agendix depth and update both routers, depot dependencies, Wayfinder visibility, Skillware context paths, citations, and support-chat registries
- create `issues/100-issues.md` and route `Issue.I0001.Bootstrap.Review`
- ground the bootstrap issue on the user turn selecting this pilot, but deliberately leave it without a reviewed resolution line
- the real pilot is successful when the system reports one healthy open grounded issue and offers the later review/resolution path without treating openness as an error

### Documentation.And.Cutover

- update the owning Agentos and Chatlas Index blocks before claiming runtime completion
- update `agentos-hugentics` authored `.skw/src` modules for search, capture, edit, reconcile, check, touched-data, context assembly, and public routing as required; rebuild generated surfaces and run Skillware checks
- update `agentos-support-chats` to scan issues
- update CLI help, Package.Skill operational references, AGENTS guidance, POI catalog blocks, linter explanations, and examples
- remove stale four-HEAD or history-bearing Project Index descriptions from active documentation
- do not edit generated Skillware targets directly

## Execution.Plan

### Vertical.Slice 0 - Preserve And Verify The Base

**status:** not started

- checkpoint every owning repository without resetting dirty worktrees
- verify Impl.Req 555 focused/full Chatlas tests and inspect its generated Skillware drift
- verify Impl.Req 606 extraction over the existing agentos-pkg depot
- record any baseline deviation before touching shared seams

**observable:** the executor can distinguish pre-existing work from this request and the completed capture/support machinery is demonstrably usable.

**check:** recorded baseline commands and results; no unrelated diff removed or rewritten.

### Vertical.Slice 1 - First-Class Issues Surface

**status:** not started

- add the explicit issues surface kind across parser models, depot discovery, linter configuration/state, scopes, summaries, block statistics where applicable, and CLI help
- exclude `issues/` from accidental generic-chapter classification
- enforce `NNN-issues.md` filenames and `Issue.I####[.Dotted.Name]` block identities
- keep router participation and exact source locations
- add RED/GREEN parser, discovery, selector, and structural-linter tests

**observable:** `parse_depot` and `agentos index linter --depot` discover issues distinctly without changing existing chapter/appendix/agendix results.

**check:** focused `agentos-py` Index suites pass; existing depot fixtures retain identical inventories outside the added field.

### Vertical.Slice 2 - Surface Policies And Issue Standing

**status:** not started

- introduce the centralized surface-policy model and built-in v1 policies
- require typed grounded Issue.Block lines
- compute open/resolved state from token-reviewed `[DC]` resolution lines
- add importable issue inventory/query APIs and a thin `agentos index issues --depot ... --json` projection
- define/document stable POI classes for malformed identities, invalid files, ungrounded issue lines, unresolved review evidence, and issue-edition closure
- keep open issues healthy rather than lint failures

**observable:** one depot can list grounded open and resolved issues with line-level review evidence while an ordinary custom chapter remains an ontology chapter.

**check:** RED/GREEN tests cover good/bad topics, arbitrary existing line types, several resolution lines, missing grounding, review cargo, and no status-directory assumptions.

### Vertical.Slice 3 - Versioned Line Provenance Dossier

**status:** not started

- add the next versioned line-bound Chatlas support record with issue context and monotonic provenance observations
- update validation, preview/register batching, exact equivalence, amendment rules, Capture.Plan rendering, audit, and resolution
- add read/enrich APIs and thin CLI commands for dossier inspection and observation append
- derive Known.Origin and home reports without confusing them with touched authority
- preserve v3/v4 reads and prove old surfaces still audit

**observable:** resolving one new line anchor returns support, review, issue context, observations, Known.Origin, and recomputed/candidate home data as separate fields.

**check:** tests cover v3/v4 compatibility, subject immutability, monotonic append, earlier-origin discovery, user/assistant observation neutrality, optional Git evidence, and batch idempotency.

### Vertical.Slice 4 - Project Support And Coverage Audit

**status:** not started

- extend support-chat source closure to issues
- implement one bulk Project↔Chat audit using support registry identities and existing Chat.Index audit maps
- add Chatlas-owned external Index checks through the existing linter socket and `agentos-cli` composition boundary
- emit stable Project-line coverage, availability, home, and issue-edition POIs
- keep checks read-only and non-blocking for eventual coverage

**observable:** one command/linter pass replaces per-line/per-chat home probing and reports exact candidate homes with source coordinates.

**check:** fixtures cover missing registry, unavailable Chat.Index, exact coverage, line drift, multiple homes, issue-line Delta coverage, and the circular passive-import case remaining a semantic finding rather than false proof.

### Vertical.Slice 5 - Incremental Reconciliation Workflow

**status:** not started

- persist project-scoped per-chat cursors outside the Index HEAD
- inspect only unreconciled Delta tails by default and reopen changed ranges safely
- produce deterministic candidate JSON plus an optional numbered live reconciliation report
- update Hugentics reconciliation/capture modules to turn meaningful findings into grounded Issue.Blocks
- support both Chat-first promotion and Project-first backfill through `Capture.Plan`

**observable:** rerunning unchanged reconciliation is a no-op; appending one Delta inspects only that tail and returns bounded candidates.

**check:** E2E covers current, append-only, expanded, revised, unavailable, cursor-reset, idempotent, and no-silent-write behavior.

### Vertical.Slice 6 - Hugentics Index Migration

**status:** not started

- inventory and migrate Hugentics-owned blocks/depth from `agentos-pkg`
- initialize the independent Hugentics depot and preserve dependency direction to `agentos-pkg`
- preserve exact accepted line content/anchors during movement
- update routers, Wayfinder/depot configuration, citations, Skillware context loading, support-chat registries, and linter scope
- leave shared Agentos primitives in `agentos-pkg`

**observable:** a cold agent loading `agentos-hugentics` discovers its own routed design before following shared dependencies, with no duplicate concept ownership.

**check:** both depots lint clean; Wayfinder resolves moved and retained blocks uniquely; Skillware context witnesses and build/check pass.

### Vertical.Slice 7 - Bootstrap Issue

**status:** not started

- allocate `Issue.I0001.Bootstrap.Review` in `issues/100-issues.md`
- use the minimal grounded `[PR]` line from `Issue.Block.V1`
- attach exact issue context in the line dossier and include the supporting current chat in `009-SUPPORT-CHATS.md`
- verify the issue is open, grounded, current, and not review-debt
- do not add a Resolution.Line or simulate the real user's review

**observable:** `agentos index issues` reports exactly one healthy open bootstrap issue and exposes its future resolution workflow.

**check:** Hugentics depot lint, support-chat closure, anchor resolution, Project↔Chat audit, and issue query pass; the open state produces no error.

### Vertical.Slice 8 - Workflow And Documentation Closure

**status:** not started

- update all authored Hugentics Skillware modules and generated targets affected by issues, policies, dossiers, reconciliation, and edition closure
- update Agentos/Chatlas Index concepts, appendix depth, POI catalogs, command references, examples, AGENTS files, and support-chat workflow
- document the initial policy and explicitly mark tags/richer Issue.Block ergonomics as post-pilot design
- remove obsolete active guidance rather than adding compatibility prose around it

**observable:** a cold implementer/agent can discover, create, reconcile, review, resolve, and retire issues from maintained documentation without this chat.

**check:** Skillware build/check/context, Index lint including new checks, documentation searches for stale layout names, and package-skill behavioral tests pass.

### Vertical.Slice 9 - Synthetic Full-Lifecycle E2E

**status:** not started

- create a medium-chat fixture with Chat-first and Project-first lines
- create an issue, capture/project ordinary lines, simulate tokenized user approval, apply several model edits plus Resolution.Lines, and compute resolved standing
- retire the Issue.Block from Project HEAD while retaining its Chat Delta and Git fixture history
- rerun all audits and reconciliation to prove closure and idempotency

**observable:** the complete lifecycle is executable without manual JSON/JQ/file-copy mechanics and every state transition is inspectable.

**check:** boundary E2E is RED before the slices and GREEN afterward; focused/full Agentos and Chatlas suites plus Ruff pass.

### Vertical.Slice 10 - Real Pilot Readiness Gate

**status:** not started

- run a cold-read and maintenance pass over the real Hugentics depot
- confirm the bootstrap issue is the only intentionally open review checkpoint introduced by this request
- report the exact later user-review command/workflow without crossing it
- update this artifact and `607` with implementation evidence and remaining post-pilot design questions

**observable:** implementation can stop safely with the real issue open while the synthetic E2E proves resolution mechanics.

**check:** final acceptance checklist is complete except the deliberately future real-user resolution event, which remains named rather than hidden.

## Deviation.Triggers

- if the `issues/` surface cannot be distinguished without breaking custom chapter discovery, stop before adding folder-name special cases throughout the code and centralize classification first
- if Issue.Block resolution cannot be derived reliably from line-local approval evidence, keep the block open and surface a POI; do not add a mutable status cache
- if issue association cannot fit in the versioned line dossier without changing support meaning, introduce a separate versioned metadata field/record linked by exact line subject; do not overload support members or create a general dependency graph
- if v4-to-next-record migration would rewrite historical anchors, preserve old records and adopt the new writer only for new/changed lines
- if a candidate Hugentics block has ambiguous ownership with `agentos-pkg`, leave it in the shared depot and record the decision; do not duplicate the concept
- if current dirty Chatlas work diverges from Impl.Req 555's recorded green state, stop at Slice 0 and reconcile that baseline before extending shared files
- if the real bootstrap issue requires user review during execution, stop at the checkpoint and report it; never synthesize or infer the gate

## Acceptance.Checklist

- [ ] `issues/` is a first-class parsed/linted/routed surface, not an accidental chapter
- [ ] minimal Issue.Block identity and open/resolved projection are implemented
- [ ] issues accept any temporary topic and all Issue.Block lines are grounded
- [ ] review standing comes from anchor records
- [ ] model editions carry issue context without a general line dependency graph
- [ ] new line-bound records expose support, review, provenance, Known.Origin, issue context, and home as distinct axes
- [ ] Project Support Chats include issues and Project↔Chat coverage is bulk-auditable
- [ ] reconciliation cursors are external machine state and incremental scans are idempotent
- [ ] Chat-first and Project-first propagation both work
- [ ] `agentos-hugentics` owns an independent clean Index depot without duplicate concept ownership
- [ ] the real grounded bootstrap issue is open and awaiting later user review
- [ ] synthetic review/resolution/model-edit/retirement E2E passes
- [ ] Agentos/Chatlas indexes, docs, skills, AGENTS guidance, CLI help, POI catalogs, and linters agree
- [ ] full relevant test suites, Ruff, Skillware checks, Wayfinder resolution, support closure, and real pilot audits pass

## Impl.Log

- 2026-08-05 - implementation design authorized; user selected complete cross-surface closure rather than a partial parser or folder change ^c20260805-0u
- 2026-08-05 - user selected a minimal first Issue.Block, defined issues as any temporary topic, and deferred richer tags/ergonomics until real use ^c20260805-0u
- 2026-08-05 - user selected `agentos-hugentics` as the first migrated Index and requested one real bootstrap issue to remain for later review ^c20260805-0u
- 2026-08-05 - inspected the live baseline: Impl.Reqs 555 and 606 are implemented; Hugentics is Skillware-managed and currently depends on `agentos-pkg` without owning an Index depot; generic Index parsing currently lacks an issues surface kind
- 2026-08-05 - chose a versioned dossier extension, computed issue state, external cursor state, and an open real pilot plus resolved synthetic fixture so implementation can be complete without impersonating the user's future review
- 2026-08-05 - readiness check passed: scope/exclusions, current seams, dependency order, ownership, observable slices, RED/GREEN checks, deviation triggers, and the user-only bootstrap review checkpoint are explicit
