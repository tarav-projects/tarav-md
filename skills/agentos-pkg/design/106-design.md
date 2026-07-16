> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## What.Design.Session

- `What.Design.Session` is a scoped human-agent convergence surface for design work — the `What.Design` specialization of `Alignment.Session`, run through `Alignment.Loop::What`
- it does real design work (problem-solving, issue resolution) while progressively enriching alignment, aiming to fill `Hugentic.Variable::What` with `Hard.Evidence`-based facts
- a staging area for `Stable.Surface` changes — a strong, high-signal trigger for change, not a `Stable.Surface` itself
- the move from session state to stable surface is the implementation: other agents read the artifact and implement, the session emits `Impl.Req`s, or surfaces are updated directly
- the destinations are index notes and skills — the session does not replace them
- optimized for high-signal alignment data — it can carry operational work when that produces alignment, but is not a general-purpose work log

****

## Alignment.Loop::What

- `Alignment.Loop::What` is the `What.Design` specialization of `Alignment.Loop` — the flow the agent steers the session through
- main flow: `Alignment.Question::What` → `Alignment.Discussion::What` → `Alignment.Consolidation::What`, repeating
- runs as `Alignment.User.Turn` (discussion) and `Alignment.Maintenance.Turn` (one agent-driven move); switching is user-gated
- interruptions (`Alignment.Loop.Interruptions`) are sidequests that pause the main flow at any point and return to it
- consolidation output is a `Design.Status.Report`; in `Alignment.Backend::InChat::What`, a consolidation just prints one

****

## Design.Status.Report

- `Design.Status.Report` is a structured checkpoint that summarizes `What.Design.Session` state
- delta-oriented: reactive to context, does not repeat still-valid reported state
- serves multiple roles: status checkpoint, consolidation output, and session-state summary
- used sparingly, at natural consolidation points
- works in both `Alignment.Backend::InChat::What` and `Alignment.Backend::Artifact::What`; in InChat, an `Alignment.Consolidation::What` is printing one

****

## Alignment.Loop.Interruptions

- `Alignment.Loop.Interruptions` is the user taking a sidequest out of the `Alignment.Loop` — any branch away from the main flow
- it is fine and expected; the essential property is that the agent can always return to the session state afterward, in both `Alignment.Backend::InChat::What` and `Alignment.Backend::Artifact::What`
- some interruptions are themselves well-defined workflows; others are ad-hoc and fully user-driven

****

## Alignment.Backend::InChat::What

- `Alignment.Backend::InChat::What` is the default `What.Design.Session` backend — the `:What` specialization of `Alignment.Backend::InChat`
- the agent organizes the live chat into design-session form and tracks state across turns and `Design.Status.Report` prints
- flexibility is the priority — no formal sections required every turn; don't spend tokens on organization overhead

****

## Alignment.Backend::Artifact::What

- `Alignment.Backend::Artifact::What` is the file-backed `What.Design.Session` backend — state in a `*-design-session.md` `Live.Note`
- adds `Session.Notes` and `Session.Log` to `Session.Abstract` and `Design.Index`; writes are user-gated
- upgrade path: InChat → Artifact when state grows large, important, or needs handoff — user-gated, never automatic

****

## Forward.Alignment

- `Forward.Alignment` is moving the design point to a new place in the `Design.Space` — adding features, evolving design, exploring new territory
- the creative act of development: deciding where to go next

****

## Internal.Alignment

- `Internal.Alignment` is keeping all surfaces in sync at the current design state
- for a given design point, moving all other surfaces to follow it
- the maintenance act of development: ensuring coherence across code, index, skills, docs

****

## Hugentic.Alignment

- `Hugentic.Alignment` is bringing human and agent to shared understanding of where they are and where they're going in the `Design.Space`
- the convergence act: achieved through `Alignment.Loop` cycles

****

## QA.Space

- [DF] `QA.Space` is the implicit space of questions and possible answers that define a topic, artifact, task, source, or user model
- [PR] alignment is the progressive conditioning of a `QA.Space` through agent/user interaction
- [DC] a `QA.Space` is a model, not a requirement that agents mechanically enumerate every question and answer
- [DC] any state of a `QA.Space` can be described as answer regions that are open, constrained, fixed, touched, or untouched
- [PR] the touched/open ratio is the control surface: the user tightens control by constraining more of the space, and delegates automation by leaving space open
- [DC] hugentic surfaces nest over `QA.Space`: the `Chat.Surface` records it, the index digests it, and implementation surfaces realize it
- [PR] `QA.Space` is never required complete to proceed; the agent works `Open.Space` to keep moving, and alignment catches up

****

## User.Model.Space

- [DF] `User.Model.Space` is a `QA.Space` about the user
- [DC] it models what the system knows about the user: what they said, wanted, rejected, approved, left open, or asked to process
- [CT] `User.Model.Space` is evidence-scoped; user claims belong there only to the extent that a surface grounds them
- [PR] growing `Touched.Space` improves the user model because more of it is backed by user-grounded interaction

****

## Work.Space

- [DF] `Work.Space` is a `QA.Space` about the work at hand
- [DC] it models what is true, needed, selected, excluded, available, blocked, open, constrained, or fixed in the work
- [PR] agents act in the `Open.Space` of `Work.Space` and obey the `Constrained.Space` of `Work.Space`
- [CT] touch is not an action gate for `Work.Space`; openness governs whether the agent decides

****

## Source.Space

- [DF] `Source.Space` is a `QA.Space` about a source surface or source artifact
- [DC] it can model whatever matters about a source: what it says, contains, implies, connects to, supports, contradicts, enables, or raises as a point of interest
- [CT] source-local signals do not by themselves establish current `User.Model.Space` claims unless they are grounded through a user-touched process
- [PR] source surfaces feed alignment by surfacing candidate questions and points of interest for later touch

****

## Design.Space

- [DF] `Design.Space` is a `QA.Space` about artifact design
- [DC] it scopes `QA.Space` to design questions whose answers shape an artifact
- [DC] it is a vector space of `Design.Variable`s; each variable one axis, and `Design.Target.Model` is a point in this space

****

## User.Touched

- [DF] `User.Touched` is a property of a fact produced by a user-gated hugentic process
- [DC] it carries evidence of user-agent collaboration, not agent ONLY invention
- [DC] the agent may construct and tag the fact; the user gates it, so authorship is not the touch boundary
- [CT] touch is general over stated, discussed, approved, corrected, rejected, co-drafted, or explicitly delegated material
- [DC] it is a cross-surface predicate; the index is a `User.Touched` surface, and the `Chat.Surface` is another
- [CT] `User.Touched` separates `Touched.Space` from `Untouched.Space`; it does not decide whether a region is open, constrained, or fixed

****

## Touched.Space

- [DF] `Touched.Space` is the region of a `QA.Space` carrying `User.Touched` evidence
- [DC] it is the part of the modeled space that the hugentic process has reached
- [DC] the index is its primary alignment surface, but not the only one; the `Chat.Surface` is another hugentic surface that holds touch
- [CT] a touched region may be open or constrained; touch means engaged, not decided

****

## Untouched.Space

- [DF] `Untouched.Space` is the region of a `QA.Space` with no `User.Touched` evidence
- [DC] it is the part of the modeled space the hugentic process has not reached
- [CT] touch does not decide whether the agent may act; the `Open.Space` / `Constrained.Space` axis decides action
- [DC] untouched material never becomes an index line directly; and touch alone lands nothing — material, touched or not, remains in chat, work surfaces, source surfaces, or `Index.Agendix` until landed through the gate ^20260716-0
- [PR] alignment grows by moving important regions from `Untouched.Space` into `Touched.Space`

****

## Open.Space

- [DF] `Open.Space` is the region of a `QA.Space` where meaningful agent choice remains
- [DC] in `Open.Space`, the agent makes its own decisions to act: coherent, never random, and provisional
- [CT] `Open.Space` is orthogonal to touch: it may be untouched, or it may be touched by an explicit free declaration (`FR`)
- [CT] consequences logically entailed by constraints are not open; the agent may fail to derive them, but is not free to decide against them
- [DC] open resolutions become directive constraints only once touched

****

## Constrained.Space

- [DF] `Constrained.Space` is the region of a `QA.Space` where possible answers have been narrowed below total freedom
- [DC] constraint can come from user directives, grounded arguments, formal implications, code reality, physical reality, or consequences of prior constraints
- [CT] in `Constrained.Space`, the agent does not choose outside the remaining valid answer region
- [PR] constraint strength varies; `Fixed.Space` is the maximally constrained endpoint

****

## Fixed.Space

- [DF] `Fixed.Space` is the region of `Constrained.Space` narrowed to one valid answer
- [DC] it is the 0%-free endpoint of the freedom axis
- [CT] a fixed region is not a decision point for the agent; the agent's job is to recognize and obey the fixed answer

****

## Touched.Authority

- [DF] `Touched.Authority` is the rule that content's authority flows from its grounding, not from its writer — agent-written material carries whatever its evidence supports ^20260711-6
- the gradient: **untouched** — agent-generated, user-untouched, no grounding: zero authority of its own, rewritable only within `Open.Space` — the complement of the span of grounded constraints, never against them; **grounded** — linked to a `User.Turn`: second-order authority through the link, and rewriting must answer to that evidence; **`User.Turn`** — the grounding itself: the user's touch, first-order authority ^20260711-6
- lower tiers are bound by the span of the higher ones: untouched content moves in what grounded statements leave open; grounded content moves in what its `User.Turn`s leave open ^20260711-6
- linkability fences by surface, not by gradient: stable surfaces link only into touched surfaces — grounded content on an untouched surface may be authoritative yet stays unlinkable-into ^20260711-6
- no authority status is stored — authority is read from provenance on the surface: types, anchors, the gate trail ^20260711-6

****

## Line.Type

- `Line.Type` is the classification a `Kernel.Line` carries, written as a typed prefix from the `Line.Type.Vocabulary`
- classifying is the line-level gate — it forces significance the way naming gates a block; the small cost is the point, a cost-zero index overwhelms the user
- naming once bundled three filters — identification, boundary, significance; the line-level tests unbundle them: a crisp single point (`Kernel.Line`), attaching to a block (`Index.Edit.Append.Line`), and significance (`Line.Type`)
- syntax: a leading bracketed code — `- [CT] the anchor token stays small`; the type is read first and primes the line, the tail stays free for inline anchors
- every line is typed, the definition first line explicitly `[DF]` — untyped lines are mechanically detectable (no leading bracket), the pre-fence legacy the calibration passes work down
- [DC] the act axis (`CT`, `DC`, …) is the type — the assistant-grounded source marker (`[AS:XX]`) is retired: all typed lines are user-grounded on every surface ^20260716-0

- [PR] typing makes the index computable — backward, lint for coherence; forward, agents derive their bounds and freedoms mechanically instead of interpreting prose ^20260707-1
****

## Line.Type.Vocabulary

- `Line.Type.Vocabulary` is the controlled set of `Line.Type`s an index uses — small, curated, soft (`Concept.Hardness`); extensible, not a hard enum
- each type is a verb on the `Design.Space` — types sort by how a line acts on the space: collapsing it, describing it, or declaring it open
- a type earns its place when a recurring line-act has no home; a type that attracts filler is a smell
- each type creates a validation point: a typed line must perform its act — a constraint line must constrain something; a typed line that performs nothing is mistyped filler
- the vocabulary is the fence of the index: index content is what the vocabulary can express — a line that can take no type belongs elsewhere; developing the vocabulary is deciding what the index is for
- scope widens only by widening the vocabulary — a visible, gated act, instead of line-by-line scope creep
- calibration: type the live index against a candidate vocabulary and inspect what remains untyped — each residue is a discussion: out of the index, or a vocabulary extension

****

## Line.Type::DF

- `Line.Type::DF` marks a definition — the line fixes what a name means
- validation point: the line must bind a name to a meaning; a `DF` that introduces no name is mistyped
- lint: two `DF` lines binding the same name to different meanings, and a block whose first line is not a `DF`

****

## Line.Type::DC

- `Line.Type::DC` marks a decision — the line pins a `Design.Variable` to a value
- validation point: the line must name what was decided and the value it took; a `DC` that pins nothing is mistyped
- lint: two `DC` lines pinning the same variable to different values is a contradiction to surface

****

## Line.Type::CT

- `Line.Type::CT` marks a constraint — the line bounds a `Design.Variable` to a subset without picking a value
- validation point: the line must exclude something; a `CT` that rules nothing out is filler
- lint: constraints whose intersection is empty, and a `CT` silently violated by a later `DC`

****

## Line.Type::RJ

- `Line.Type::RJ` marks a rejection — the line excludes a considered alternative
- validation point: the line must name the rejected alternative, preferably with the reason
- lint: a rejected alternative later reintroduced without a new touch

****

## Line.Type::PR

- `Line.Type::PR` marks a principle — a generative orientation that spawns constraints across many variables
- validation point: the line must orient decisions beyond one variable; a `PR` scoped to a single variable is a `CT`
- lint: decisions or constraints that run against a standing principle

****

## Line.Type::FR

- `Line.Type::FR` marks a free declaration — the user explicitly leaves a `Design.Variable` agent-owned
- validation point: the line must name what is left open; freedom is a touched act, not an omission
- lint: a `FR` variable later constrained without retiring the declaration

****

## Line.Type::EX

- `Line.Type::EX` marks an example — the line illustrates another line's claim with a concrete case
- validation point: the line must exemplify something specific; an example that illustrates no claim is filler
- lint: an example inconsistent with the constraints and decisions it illustrates

****

## Line.Type::GR

- [DF] `Line.Type::GR` marks a grounding line — a one-sentence account of what an anchored evidence neighborhood grounds
- [CT] validation point: the line must carry a trailing anchor and state what the evidence grounds; a `GR` without an anchor is mistyped
- [DC] lint: an anchor that does not resolve, and a `GR` account contradicted by its anchored neighborhood

****

## Design.Variable

- `Design.Variable` is one axis of the `Design.Space` — a question a design must resolve on its way to implementation
- a design is a vector of `Design.Variable`s; resolving every one yields a `Design.Target.Model`, a point in the space
- each variable carries a set of possible values — the candidate solutions for that axis; spanning all variables and their values spans the whole space
- an abstract design constrains axes to subsets of their values — a region of the space, not yet a point
- a design may deliberately leave a variable unresolved — bound case by case at implementation rather than fixed as a rule; an unbound axis is a degree of freedom the design hands down, not one it forgot
- `Hugentic.Variable` is its specialization: a `Design.Variable` whose resolution needs human-agent convergence

****

## Hugentic.Variable

- `Hugentic.Variable` is a `Design.Variable` that needs human-agent convergence — meant to be collapsed inside the `Touched.Space`
- for a given design, some variables should be prioritized as hugentic — each type of system has its own set worth identifying
- the current default is precedence (`Specified.By.Precedence`): agents visit the indexes of previously implemented similar systems, see which variables were specified there, and extract both the variables and their variable space
- each workflow specialization defines its own variable set — these variables are the focus of the `Alignment.Loop`

### meta

- aliases: `Touched.Variable`

****

## Agentic.Variable

- `Agentic.Variable` is a `Design.Variable` the agent resolves autonomously, without explicit human convergence
- it is the variable form of `Open.Space` — left to the agent by delegation (a touched free declaration) or simply untouched
- its resolutions stay provisional and overwritable — they become directive constraints only once touched

### meta

- aliases: `Open.Variable`

****

## Alignment.Loop::How

- `Alignment.Loop::How` is the `How.Design` specialization of `Alignment.Loop` — convergence targeting implementation design
- targets mostly the runnable surfaces (code, skills), not the conceptual surface
- the discussion runs lower-level: coding best practices, codebase design considerations
- consolidation output is the `Impl.Req` fundamentals

****

## Alignment.Loop::Exec

- `Alignment.Loop::Exec` is the `Impl.Exec` specialization of `Alignment.Loop` — the lightest, no longer conceptual
- it is the practice of designing and walking implementation plans: `Vertical.Slice`, TDD, execution discipline
- targets the least-stable surfaces — code plus ephemeral ones like progress tracking and logs

****

## Alignment.Loop.Gradient

- `Alignment.Loop.Gradient` orders the three `Alignment.Loop` phases by the shape-distance between their staging state and the `Stable.Surface` they target
- all three are non-`Stable.Surface` staging that lands on a `Stable.Surface`; the route and timing are not fixed
- `:What` has low shape-distance — its state is already nearly index-shaped, so little translation is needed
- `:How`/`:Exec` have high shape-distance — they target code and runnable surfaces their state is not shaped like; closing that distance is the convergence work
- flow is bidirectional — content can also be promoted up-gradient, a `:How` insight landing in the index

****

## Program.Hardness

- `Program.Hardness` is `Spec.Hardness` applied to executed behavior — how much of a program is fixed vs left to its interpreter
- its interpreter is an executor; the executor's intelligence sets the achievable hardness

****

## Soft.Program

- `Soft.Program` is an adaptive natural-language behavioral program for agent-human work
- a `Soft.Program` is an `Agentic.Program` whose behavior is soft/adaptive
- preserves continuity across turns without becoming a rigid execution script
- interprets `Soft.State`, user directives, current evidence, and common sense together
- guides agent behavior inside declared behavioral boundaries
- adapts to user correction, new context, and changing focus
- does not erase explicit gates, checkpoints, or `Hard.Evidence`

****

## Agentic.Program

- `Agentic.Program` is a program whose interpreter is an **Agent** — the agent executes the steps, deciding what runs next and when to branch
- one side of the executor-axis split: the interpreter is either an Agent (`Agentic.Program`) or a CPU (`CPU.Program`)
- the agent's judgment is the control flow — sequencing, branching, and adaptation come from the agent
- an agent interpreter opens the full `Program.Hardness` continuum — its programs can run hard or soft, softer the more capable the agent
- the medium is open — natural language, code, or mixed; what makes it agentic is the agent deciding flow, not the medium
- natural language is a common and important medium, worth its own treatment, but not the defining feature
- its implementation-level form is `Agentic.Impl`

****

## CPU.Program

- `CPU.Program` is a program whose interpreter is a **CPU** — code executed deterministically by an interpreter or compiler
- the other side of the executor-axis split from `Agentic.Program`
- control flow is fixed by the code — no judgment decides what runs next
- it is the hard endpoint of `Program.Hardness` — a CPU interpreter admits no softness
- it cannot improvise — it runs declared paths and errors hard outside them
- its implementation-level form is `CPU.Impl`

****

## Supervisor.Agent

- `Supervisor.Agent` is a `Soft.Program` for observing another agent session
- follows a `Target.Session` without replacing or controlling it
- is an observer: it never mutates the target session
- keeps a separate context budget for supervision-specific knowledge
- lets `Worker.Agent`s stay focused on task execution
- reads new target-session turns from an `Observation.Cursor`
- reports against an evolving `Supervisor.Brief`
- produces `Supervisor.Report` output for the user
- may include copyable intervention text inside `Supervisor.Report`
- remains conversational with the user during supervision
- treats the human as the transfer gate between supervision and target-session correction
- uses `Hard.Evidence` from target-session turns, user directives, and stable project surfaces
- does not turn observation into automatic control

****

## Normalization.Pipeline

- `Normalization.Pipeline` is a general design pattern for turning native source data into one canonical model — defined by its constraints, not a fixed topology; variants are acceptable
- canonical shape: `Raw.Sources → Raw.Normalizers → Model.Fragments → Normal.Assembler → Normal.Model` — plural stages mark the degrees of freedom: many sources, many normalizers, many fragments, converging on one model
- constraint — raw boundary: only a `Raw.Normalizer` (data) or `Raw.Adapter` (functionality) touches raw — reads native formats or invokes native operations; no other stage does
- constraint — `Normal.Model.Closure`: every stage outputs within the `Normal.Model.Namespace` — fragments are subpaths of it, assembled objects are instances of it; nothing leaves the namespace
- constraint — normalization is separate from integration: normalizers only produce fragments; merging, placing, and reconciling them is the `Normal.Assembler`'s job, never a normalizer's
- the many-normalizers freedom is the point of fragments — native extraction splits into independent, additive pieces the assembler integrates
- what may vary: normalizer count and granularity, assembler merge policy, assembled depth — free, as long as the three constraints hold

****

## Delta.Normalization

- [DF] `Delta.Normalization` is incremental derivation in a `Normalization.Pipeline`: normalize only source records added since the last pass plus the model's volatile tail, instead of re-deriving the whole `Normal.Model` ^20260712-14
- [PR] it applies better to append-friendly target models — an append-only body with per-line provenance and finality; the `Normalization.Pipeline` does not require its targets to be append-friendly ^20260712-13
- [DC] the unit of work is the stable-prefix / volatile-tail split — content whose derivation is final is frozen and skipped; only the volatile tail and new source records are recomputed ^20260712-14
- [DC] resume state persists in a `Normalization.Delta.Checkpoint`; a checkpoint that fails validation discards itself and the pass falls back to full derivation ^20260712-14
- [CT] full derivation from raw sources remains always available and authoritative — delta passes are an optimization, never a new source of truth ^20260712-14

****

## Normalization.Delta.Checkpoint

- [DF] `Normalization.Delta.Checkpoint` is the persisted resume state of `Delta.Normalization` for one source — whatever the producer needs to continue derivation from the recorded source position ^20260712-15
- [DC] the checkpoint is producer-private — only the pipeline that wrote it reads it; it is never a consumer surface of the `Normal.Model` ^20260712-15
- [DC] it validates before use: the source must still extend the position it recorded; a failed validation discards the checkpoint and the pass re-derives fully ^20260712-15
- [CT] the checkpoint is disposable at any time with no data loss — deleting it costs one full derivation, nothing else ^20260712-15

****

## Normalization.Trust.Tier

- [DF] `Normalization.Trust.Tier` is the verification level a caller selects for a `Delta.Normalization` pass — how much of the existing `Normal.Model` is re-checked against source before being trusted ^20260712-16
- [DC] three tiers: trust-append assumes the source only grew and resumes blindly from the checkpoint; verify re-checks provenance over the frozen content and recomputes from the first divergence; rebuild re-derives everything from source ^20260712-16
- [PR] staleness is a price point, not a defect — when raw sources are preserved and authoritative, a wrong cheap pass is always recoverable by a more expensive one ^20260712-16
- [CT] tier selection changes cost and staleness risk only, never the model contract — every tier produces the same model shape ^20260712-16

****

## Comparative.Normalization

- `Comparative.Normalization` is normalizing a source by reading it alongside previously normalized instances rather than from the source and specs in isolation — an instantiation of `Normalization.Pipeline` that consults precedent
- canonical shape: `Content + Specs + Precedence → Normal.Model` — content is sourced from the raw, specs are explicit guidance, precedence is prior instances; the three combine into the normalized value
- specs are always incomplete — a stated ruleset leaves representation gaps it does not decide
- precedence fills the gaps specs leave — an unspecified representation choice is settled by what was approved on prior instances, not invented fresh
- it splits authority by question: the source is the sole authority for content; specs and precedence are the authority for representation
- content authority sits at the raw boundary — only a `Raw.Normalizer` reads the source, and each normalized value can carry its `Inline.Raw.Source` as canonical-content evidence
- representation authority follows `Specified.By.Precedence` — prior normalized instances set the converging shape (spelling, format, convention) a new instance imitates
- specs supersede precedence — an explicit rule settles representation over any precedent, matching `Specified.By.Precedence`'s spec-over-imitation rule
- precedence never overrides source content — it decides how a value is written, never what the value is
- precedence is weighted by relatedness — instances sharing identifying context (same party, project, or scope) carry more weight than distant ones
- representation choices are `Verbatim.User.Gated` — the agent proposes from precedence, the user settles the canonical form

****

## Fuzzy.Dotted.Name

- `Fuzzy.Dotted.Name` is a `Dotted.Name` marked approximate with a leading tilde: `~Concept.Partial`
- the tilde is a softness operator on the name — it declares the name uncommitted, to be read in context
- a chat-side device for the user (and agent); never written into the index, which stays canonical and strict
- matching is fuzzy: order-independent, partial, word-subset — not a prefix
- the softness is flow-agnostic — context selects the workflow, the sigil names no flow
    - recall miss → resolve to an existing canonical block
    - near-variant → naming review: existing concept, sibling/refinement, or rename
    - seed → a gesture toward a new concept to coin
- invariant across all outcomes: the agent surfaces its interpretation and makes the resolved canonical name(s) explicit before building on it
- ambiguity → surface the top candidates and confirm; unresolvable → degrade to `Unresolved.Index.Name`
- direction is symmetric: the user emits `~` to ask; the agent emits `~` to flag an unverified, approximate recall
- soft meaning surfaced as a chat sigil — rides `Concept.Hardness`, sibling to `::` type statements (`Addressing.Sigil.Vocabulary`) and the variable `<Concept>.Name` form ^20260712-6

****

## General.Avoids.Specific

- a block's references tend to point up — a specialization references the general; a general block, as a rule of thumb, avoids reaching down into its specifics.
- the aim is to keep a fundamental independent of its specializations — guarding against overspecification, so a general block stays readable and reusable on its own.
- references then tend to run specific → general, keeping the graph stable toward the fundamentals.

### appendix

- the typical drift it guards against: specific detail accreting onto a general block.
- namespace exception: an umbrella/namespace concept may list its members in `meta` (membership is constitutive); ordinary blocks reach upward only.
