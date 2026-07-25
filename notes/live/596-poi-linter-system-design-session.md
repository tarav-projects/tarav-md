# POI Linter System - design-session

## Session.Abstract

- intent: establish a common conceptual model for parser-backed POI systems used by Skw, md-library, and future Agentos linters
- active focus: define the system boundary and integrate POIs with their authoritative documentation surfaces
- references: `skills/agentos-pkg/design/107-design.md`, `notes/live/590-skw-v3-impl-req.md`, and the md-library `Transcript.Linter` design and implementation
- state: active
- next: model the complete journey from source parsing through POI evaluation and instance resolution

## Design.Index

### Skw.Kernel.Index

- [DF] a `Skw.Kernel.Index` is a Skw data structure that applies `Kernel.Writing` through routed `Kernel.Block`s organized into selectively loadable chapters
- [CT] each chapter may declare the gate policy governing its content
- [CT] authority and review are properties of content provenance, not consequences of index membership
- [EX] the `Agentos.Index.System` is a `Skw.Kernel.Index` application whose curated chapters require user gates
- [EX] a `POI.Catalog` is a `Skw.Kernel.Index` application whose `poi` chapter registers `POI.Class` blocks

#### appendix

- historically, the Index originated as a hugentic user-touched surface before its reusable structure was separated into `Skw.Kernel.Index`

#### meta

- status: approved
- durable-source: `skills/agentos-pkg/design/108-design.md#Skw.Kernel.Index`

### Skw.Gate

- [DF] a `Skw.Gate` is a declared condition that should control whether a named act occurs
- [CT] every `Skw.Gate` has a `Skw.Gate.Directive` and a `Skw.Gate.Audit`
- [DF] a `Skw.Gate.Directive` instructs the agent to defend the condition before performing the protected act
- [DF] a `Skw.Gate.Audit` defines how the condition is verified afterward from the `Chat.Surface`
- [PR] gate defense is best-effort and may leak
- [PR] simplicity and manageability take priority over eliminating every possible leak
- [CT] auditability is mandatory: the protected act and the evidence relevant to its gate must be recoverable from chat
- [DC] gate satisfaction is recomputed from chat evidence and is never stored as authoritative state
- [DF] a `Skw.Gate.Violation` occurs when the protected act happened but its audit condition is not satisfied
- [EX] `User.Gate` is a `Skw.Gate` whose condition requires evidence of a user act
- [EX] `Poi.Unlock.Token` participates in a `Skw.Gate` requiring context receipts before `Poi.Bless`

#### meta

- status: approved
- pending-durable: revise `User.Gate` under the new `Skw.Gate` root

### Skw.Context.Gate

- [DF] a `Skw.Context.Gate` is a `Skw.Gate` that controls and audits whether required context is available to the agent performing a protected act
- [CT] it enforces that the agent cannot complete the protected act without satisfying every required context checkpoint
- [PR] its gold standard is evidence that the required context was loaded and understood sufficiently for the protected act
- [PR] when that standard cannot be established practically, weaker evidence mechanisms may provide partial robustness
- [CT] each mechanism must make its evidence strength explicit
- [FR] several context-gating mechanisms may compose to increase confidence

#### meta

- status: approved

### Skw.Pull

- [DF] a `Skw.Pull` is a challenge-response mechanism that requests evidence from an agent before a protected act
- [CT] each pull defines what must be returned and how the response is evaluated
- [PR] a pull makes satisfaction of an instruction mechanically inspectable
- [CT] the evidence strength of a pull depends on what its response demonstrates
- [RJ] a `Skw.Pull` does not itself define the protected act or its acceptance condition
- [FR] a `Skw.Gate` may require one or more pulls
- [EX] an unlock-token pull requests a literal obtained through a context surface
- [EX] a semantic pull requests an answer derived from the meaning of loaded context
- [EX] a session-id pull lets tooling inspect the agent's `Chat.Surface` independently

#### meta

- status: approved

### Skw.Gate.Policy

- [DF] a `Skw.Gate.Policy` binds one or more `Skw.Gate`s to named acts within an addressable scope
- [CT] the policy names its scope through `Skw.Address.Schema`
- [CT] gate definitions remain independent and reusable across policies
- [CT] each protected act resolves to the gates that should defend and audit it
- [EX] a `Skw.Kernel.Index` chapter may apply different gates to editing, publishing, or blessing its content
- [RJ] a `Skw.Gate.Policy` does not store gate satisfaction or audit evidence

#### meta

- status: approved

### Skw.Gate.Composition

- [DF] `Skw.Gate.Composition` defines how several `Skw.Gate`s protect the same act
- [DC] gates bound independently to the same act compose conjunctively: every gate should be satisfied
- [CT] the directive surfaces every required gate before the protected act
- [DC] the audit evaluates each gate independently against the `Chat.Surface`
- [DC] the protected act violates its `Skw.Gate.Policy` when any required gate is unsatisfied
- [PR] independent evaluation allows missing or violated gates to be reported individually
- [RJ] declaration order does not imply gate execution order

#### meta

- status: approved

### POI.Catalog

- [DF] a `POI.Catalog` is a `Skw.Kernel.Index` application that registers `POI.Class` blocks
- [DC] `POI.Class` blocks live in a dedicated `poi` chapter
- [CT] every registered `POI.Class` is routed and machine-addressable
- [CT] each class points to its required documentation through `Skw.Address.Schema`
- [PR] linters, blessing machinery, and gates consume the same catalog
- [CT] authority and review follow the chapter's declared `Skw.Gate.Policy`
- [RJ] a `POI.Catalog` contains class declarations, not `POI.Instance` occurrences
- [RJ] the catalog routes documentation but does not replace it

#### meta

- status: approved

### Poi.System

- [DF] a `Poi.System` is the common composition that produces, documents, presents, and resolves points of interest
- [BD] `Poi.System` does not make `Poi.Linter` the owner of parsing, documentation, or resolution
- [REL] a `Poi.System` may consume a `Closure.Parser` model without becoming the parser's only consumer
- [REL] `Poi.System` coordinates `Poi.Linter`, `Poi.Documentation`, `Poi.Instance`, and the available resolution acts

#### meta

- status: working
- open: determine whether checks, kinds, catalogs, dispositions, and gates warrant independent concepts

### Point.Of.Interest

- [DF] a `Point.Of.Interest` is a machine-produced pointer from an observed situation to the documentation required for agent evaluation
- [PR] a `Point.Of.Interest` requests agent attention without prescribing the agent's conclusion
- [CT] a `Point.Of.Interest` carries a documentation identifier and enough occurrence evidence to locate and identify the observed situation
- [DC] authoritative meaning and evaluation protocol live on the resolved `POI.Documentation` surfaces, not in linter output
- [RJ] a `Point.Of.Interest` is not a parser error, verdict, or repair command

#### meta

- aliases: `POI` (prose abbreviation only; not a `Skw.Address.Schema` address)
- status: approved

### POI.Documentation

- [DF] `POI.Documentation` is the set of Skw-addressable surfaces that define a `POI.Class` and how its instances should be evaluated
- [CT] each `POI.Class` points from the `POI.Catalog` to one or more documentation entrypoints through `Skw.Address.Schema`
- [CT] documentation may span several surfaces connected through `Skw.Annotation` relationships
- [CT] Skw tooling checks that declared documentation relationships resolve and remain aligned
- [DC] authoritative meaning and evaluation protocol live on the documentation surfaces, not in linter output
- [PR] a `Point.Of.Interest` carries the class and occurrence evidence needed to reach the relevant documentation
- [CT] a `Skw.Gate` protecting a POI act may require evidence from designated documentation surfaces
- [RJ] `POI.Documentation` is not the `POI.Catalog` and is not duplicated into each `POI.Instance`

#### meta

- status: approved

### Poi.Instance

- [DF] a `Poi.Instance` is one identified occurrence of a POI kind in a particular source state
- [CT] instance identity must distinguish separate occurrences of the same POI kind
- [REL] resolution acts target a `Poi.Instance`, not every instance of its kind
- [REL] `Poi.Bless` accepts exactly one current `Poi.Instance`

#### meta

- status: working
- open: define which situation facts participate in stable identity

### Floor.Model

- [DF] a `Floor.Model` is a structured representation whose declared minimum guarantees support dependable downstream interpretation
- [CT] its floor identifies the structural facts consumers may rely on
- [RJ] it does not promise semantic resolution or completeness beyond its declared floor
- [PR] a `Floor.Model` decouples consumers from the mechanism that produced their input
- [FR] a parser, normalization pipeline, or another model producer may provide a `Floor.Model`
- [EX] a `Closure.Parser` AST is a `Floor.Model` when its source satisfies the `Parse.Floor`
- [EX] `Chatlas.Session.Model` is a `Floor.Model` produced through normalization

#### meta

- status: approved
- durable-source: `skills/agentos-pkg/design/107-design.md#Floor.Model`

### Closure.Parser

- [DF] a `Closure.Parser` enforces a `Parse.Floor`, the minimum source structure required to produce a dependable `Floor.Model`
- [PR] the `Parse.Floor` stays minimal: only structurally certain failures belong below it
- [DC] below the `Parse.Floor`, the source is unprocessable and the parser is not required to return an AST
- [DC] at or above the `Parse.Floor`, the parser returns an AST that is a `Floor.Model`
- [CT] the AST contains every detectable parsable element from the source
- [CT] unresolved regions above the floor are preserved as fallback structure
- [RJ] unresolved detail above the floor does not produce parser errors or warnings
- [RJ] a `Closure.Parser` does not emit `Point.Of.Interest` instances
- [PR] its AST may serve `POI.Linter` and other model consumers

#### meta

- status: approved
- durable-source: `skills/agentos-pkg/design/107-design.md#Closure.Parser`

### POI.Linter

- [DF] a `POI.Linter` consumes a `Floor.Model` and evaluates it for situations that require agent judgment
- [CT] it emits `Point.Of.Interest` instances attached to a `POI.Class`
- [CT] each emitted instance carries enough occurrence evidence to identify the observed situation
- [PR] heuristic and policy concerns become reviewable POIs rather than failures of the model producer
- [RJ] a `POI.Linter` does not produce its input model
- [RJ] it does not own authoritative documentation or resolution policy
- [PR] a `POI.Linter` is one producer within a broader `POI.System`

#### meta

- status: approved
- durable-source: `skills/agentos-pkg/design/107-design.md#POI.Linter`

### Chat.POI.Linter

- [DF] a `Chat.POI.Linter` is a `POI.Linter` that consumes a full `Chatlas.Session.Model` as its `Floor.Model`
- [CT] it consumes normalized session data, never provider-native data
- [DC] its rules inspect facts represented by the `Session.Event.Tape`
- [CT] each emitted POI identifies the relevant session state and routes to its `POI.Documentation`
- [RJ] a `Chat.POI.Linter` does not modify the session or determine how its POIs are resolved

#### meta

- status: approved
- durable-source: `skills/agentos-pkg/design/107-design.md#Chat.POI.Linter`

### POI.Class

- [DF] a `POI.Class` is the stable documented category assigned to a reviewable situation recognized by a `POI.Linter`
- [CT] a `POI.Class` points to the documentation that defines the situation's meaning and evaluation protocol
- [CT] multiple `POI.Instance` occurrences may belong to the same `POI.Class`
- [PR] a `POI.Class` remains stable across occurrences so documentation, reporting, and resolution can refer to a common concept
- [RJ] a `POI.Class` is not a concrete occurrence, an agent verdict, or a resolution

#### meta

- status: approved

### POI.Instance

- [DF] a `POI.Instance` is one concrete occurrence of a `POI.Class` identified by a `POI.Linter`
- [CT] a `POI.Instance` carries enough source identity and occurrence evidence to distinguish it from other occurrences
- [PR] a `POI.Instance` is the unit of `POI.Blessing`
- [PR] blessing a `POI.Instance` does not bless its `POI.Class` or any other instance of that class
- [PR] the same unresolved occurrence should retain a stable identity across repeated linter runs
- [RJ] a `POI.Instance` is not its documentation, evaluation verdict, or blessing

#### meta

- status: approved

### POI.Blessing

- [DF] a `POI.Blessing` is the explicit act of accepting the current state represented by one `POI.Instance`
- [CT] every blessing targets exactly one `POI.Instance`
- [RJ] blessing an instance does not bless its `POI.Class`, another instance, or a future occurrence
- [CT] only `POI.Class`es that declare blessing as an allowed act may be blessed
- [CT] the applicable `Skw.Gate.Policy` determines which gates defend and audit the blessing
- [DC] missing or unsatisfied gates prevent acceptance and are reported individually
- [PR] blessing is loud and auditable; it never occurs as a side effect of rebuilding or unrelated changes
- [FR] the owning `POI.System` defines how an accepted instance is recorded or materialized

#### meta

- status: approved

## Session.Notes

### Open Questions

- What is the complete lifecycle from parser output to a resolved POI instance?
- Is POI documentation discovered through a central catalog, derived from Skw annotations, or composed from both?
- Which distinctions require first-class concepts: check, POI class, instance identity, disposition, and gate?
- How should definite parser errors be presented alongside heuristic POIs without redefining them as parser-produced POIs?
- Which resolution acts are common across systems, and which remain package-specific?
- How do unlock tokens attach to documentation surfaces and to the exact resolution acts they gate?

### References

- `skills/agentos-pkg/design/107-design.md` - current `Floor.Model`, `Closure.Parser`, `POI.Linter`, `Poi.Bless`, and unlock-token concepts
- `notes/live/590-skw-v3-impl-req.md` - current Skw realization and md-library-derived output model
- `/Users/pereiro/Documents/workspaces/main-workspace/md-library-project/md-library/skills/md-library-pkg/design/101-design.md` - `Transcript.Linter`, check taxonomy, parser diagnostics, and resolution semantics
- `/Users/pereiro/Documents/workspaces/main-workspace/md-library-project/md-library/skills/md-library-pkg/appendix/Transcript.Linter-appendix.md` - repair protocols and enrichment surfaces
- `/Users/pereiro/Documents/workspaces/main-workspace/md-library-project/md-library-py/src/md_library/lint2/runner.py` - concrete check, finding, blocker, and report state
- `/Users/pereiro/Documents/workspaces/main-workspace/md-library-project/md-library-py/src/md_library/lint2/resolves.py` - instance suppression and resolution-feedback mechanics

### Parking Lot

- `Poi.Bless.Question` - revisit after the simpler documentation and unlock-token relationships are stable
- resolution feedback datasets - revisit when modeling how real outcomes improve checks and documentation

## Session.Log

- 2026-07-23: Session opened using `Alignment.Backend::Artifact::What`; common model draws prior art from Skw and md-library.
- 2026-07-23: Rejected framing parser diagnostics as parser-produced POIs; the parser owns definite errors and remains independently consumable.
