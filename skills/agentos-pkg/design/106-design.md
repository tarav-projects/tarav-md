> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## What.Design.Session

- `What.Design.Session` is a scoped human-agent convergence surface for design work — the `What.Design` specialization of `Alignment.Session`, run through `Alignment.Loop:What`
- it does real design work (problem-solving, issue resolution) while progressively enriching alignment, aiming to fill `Hugentic.Variable:What` with `Hard.Evidence`-based facts
- a staging area for `Stable.Surface` changes — a strong, high-signal trigger for change, not a `Stable.Surface` itself
- the move from session state to stable surface is the implementation: other agents read the artifact and implement, the session emits `Impl.Req`s, or surfaces are updated directly
- the destinations are index notes and skills — the session does not replace them
- optimized for high-signal alignment data — it can carry operational work when that produces alignment, but is not a general-purpose work log

****

## Alignment.Loop:What

- `Alignment.Loop:What` is the `What.Design` specialization of `Alignment.Loop` — the flow the agent steers the session through
- main flow: `Alignment.Question:What` → `Alignment.Discussion:What` → `Alignment.Consolidation:What`, repeating
- runs as `Alignment.User.Turn` (discussion) and `Alignment.Maintenance.Turn` (one agent-driven move); switching is user-gated
- interruptions (`Alignment.Loop.Interruptions`) are sidequests that pause the main flow at any point and return to it
- consolidation output is a `Design.Status.Report`; in `Alignment.Backend:InChat:What`, a consolidation just prints one

****

## Design.Status.Report

- `Design.Status.Report` is a structured checkpoint that summarizes `What.Design.Session` state
- delta-oriented: reactive to context, does not repeat still-valid reported state
- serves multiple roles: status checkpoint, consolidation output, and session-state summary
- used sparingly, at natural consolidation points
- works in both `Alignment.Backend:InChat:What` and `Alignment.Backend:Artifact:What`; in InChat, an `Alignment.Consolidation:What` is printing one

****

## Alignment.Loop.Interruptions

- `Alignment.Loop.Interruptions` is the user taking a sidequest out of the `Alignment.Loop` — any branch away from the main flow
- it is fine and expected; the essential property is that the agent can always return to the session state afterward, in both `Alignment.Backend:InChat:What` and `Alignment.Backend:Artifact:What`
- some interruptions are themselves well-defined workflows; others are ad-hoc and fully user-driven

****

## Alignment.Backend:InChat:What

- `Alignment.Backend:InChat:What` is the default `What.Design.Session` backend — the `:What` specialization of `Alignment.Backend:InChat`
- the agent organizes the live chat into design-session form and tracks state across turns and `Design.Status.Report` prints
- flexibility is the priority — no formal sections required every turn; don't spend tokens on organization overhead

****

## Alignment.Backend:Artifact:What

- `Alignment.Backend:Artifact:What` is the file-backed `What.Design.Session` backend — state in a `*-design-session.md` `Live.Note`
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

## Design.Space

- `Design.Space` is the total decision space of an artifact — every choice its design comprises, centered on the user's input (renames `Conceptual.Space`)
- it partitions two orthogonal ways: by provenance (`Touched.Space` / `Untouched.Space`) and by constraint (`Open.Space` / fixed)
- it is a vector space of `Design.Variable`s — each variable one axis; `Design.Target.Model` is a point in this space
- the touched/open ratio is the control surface: the user tightens control by constraining more of the space, and delegates automation by leaving space open
- it is the object every surface nests over: the `Chat.Surface` records it, the index digests it, the codebase realizes it
- it is never required complete to proceed — the agent works `Open.Space` to keep moving, alignment catches up

### meta

- aliases: `Conceptual.Space`, `Alignment.Space`

****

## User.Touched

- `User.Touched` is a property of a fact: it was produced by a user-gated hugentic process — carrying evidence of user-agent collaboration, not agent invention
- the agent may construct and tag the fact; the user gates it — the gating is the touch, authorship is irrelevant
- it is general over the form of touch: stated, discussed, approved, co-drafted — any user-gated production qualifies
- it is a cross-surface predicate — the index is *a* `User.Touched` surface, the `Chat.Surface` is another
- it separates `Touched.Space` from `Untouched.Space` — untouched is always `Open.Space` and off-index (the `Index.Agendix` is its index-adjacent home); touched can be open (`FR`) or constrained

****

## Touched.Space

- `Touched.Space` is the region of the `Design.Space` carrying `User.Touched` evidence — what the hugentic process has reached
- the index is its primary alignment surface, but not the only one — the `Chat.Surface` is another hugentic surface that holds touch
- a touched decision may be constrained (`CT`/`DC`/`RJ`) or open (declared free, `FR`) — touch means *engaged*, not *decided*

****

## Untouched.Space

- `Untouched.Space` is the region of the `Design.Space` with no `User.Touched` evidence — the hugentic process has not reached it
- it is always `Open.Space`: with no touch there is no directive constraint, so the agent decides for itself
- it never becomes an index line — untouched material remains in the chat, the work, or the `Index.Agendix`, never the index proper
- the chats are mixed, touched and untouched; the index earns its keep by extracting the touched part worth keeping — not user filler — which is exactly `Line.Type`'s gate
- alignment is the shrinking of `Untouched.Space`: growing touch across the `Design.Space`

****

## Open.Space

- `Open.Space` is the uncollapsed region of the `Design.Space` — decisions not fixed by a user directive or its consequences, the agent's domain
- it is orthogonal to touch: it spans `Untouched.Space` (always open) and touched-open (`FR`, an explicit free declaration)
- consequences logically entailed by touched constraints are NOT open — the agent may fail to derive them, but is not free to decide against them
- in it the agent makes its own decisions to act — coherent, never random — but provisional and overwritable with good reason, off-index; they become directive constraints only once touched

****

## Line.Type

- `Line.Type` is the classification a `Kernel.Line` carries, written as a typed prefix from the `Line.Type.Vocabulary`
- classifying is the line-level gate — it forces significance the way naming gates a block; the small cost is the point, a cost-zero index overwhelms the user
- naming once bundled three filters — identification, boundary, significance; the line-level tests unbundle them: a crisp single point (`Kernel.Line`), attaching to a block (`Index.Edit.Append.Line`), and significance (`Line.Type`)
- syntax: a leading bracketed code — `- [CT] the anchor token stays small`; the type is read first and primes the line, the tail stays free for inline anchors
- every line is typed, the definition first line explicitly `[DF]` — untyped lines are mechanically detectable (no leading bracket), the pre-fence legacy the calibration passes work down

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

## Line.Type:DF

- `Line.Type:DF` marks a definition — the line fixes what a name means
- validation point: the line must bind a name to a meaning; a `DF` that introduces no name is mistyped
- lint: two `DF` lines binding the same name to different meanings, and a block whose first line is not a `DF`

****

## Line.Type:DC

- `Line.Type:DC` marks a decision — the line pins a `Design.Variable` to a value
- validation point: the line must name what was decided and the value it took; a `DC` that pins nothing is mistyped
- lint: two `DC` lines pinning the same variable to different values is a contradiction to surface

****

## Line.Type:CT

- `Line.Type:CT` marks a constraint — the line bounds a `Design.Variable` to a subset without picking a value
- validation point: the line must exclude something; a `CT` that rules nothing out is filler
- lint: constraints whose intersection is empty, and a `CT` silently violated by a later `DC`

****

## Line.Type:RJ

- `Line.Type:RJ` marks a rejection — the line excludes a considered alternative
- validation point: the line must name the rejected alternative, preferably with the reason
- lint: a rejected alternative later reintroduced without a new touch

****

## Line.Type:PR

- `Line.Type:PR` marks a principle — a generative orientation that spawns constraints across many variables
- validation point: the line must orient decisions beyond one variable; a `PR` scoped to a single variable is a `CT`
- lint: decisions or constraints that run against a standing principle

****

## Line.Type:FR

- `Line.Type:FR` marks a free declaration — the user explicitly leaves a `Design.Variable` agent-owned
- validation point: the line must name what is left open; freedom is a touched act, not an omission
- lint: a `FR` variable later constrained without retiring the declaration

****

## Line.Type:EX

- `Line.Type:EX` marks an example — the line illustrates another line's claim with a concrete case
- validation point: the line must exemplify something specific; an example that illustrates no claim is filler
- lint: an example inconsistent with the constraints and decisions it illustrates

****

## Line.Type:GR

- [DF] `Line.Type:GR` marks a grounding line — a one-sentence account of what an anchored evidence neighborhood grounds
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

## Alignment.Loop:How

- `Alignment.Loop:How` is the `How.Design` specialization of `Alignment.Loop` — convergence targeting implementation design
- targets mostly the runnable surfaces (code, skills), not the conceptual surface
- the discussion runs lower-level: coding best practices, codebase design considerations
- consolidation output is the `Impl.Req` fundamentals

****

## Alignment.Loop:Exec

- `Alignment.Loop:Exec` is the `Impl.Exec` specialization of `Alignment.Loop` — the lightest, no longer conceptual
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
- representation choices are `Content.Verbatim.Gated` — the agent proposes from precedence, the user settles the canonical form

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
- soft meaning surfaced as a chat sigil — rides `Concept.Hardness`, sibling to `Dotted.Parameterized.Notation` and the variable `<Concept>.Name` form

****

## General.Avoids.Specific

- a block's references tend to point up — a specialization references the general; a general block, as a rule of thumb, avoids reaching down into its specifics.
- the aim is to keep a fundamental independent of its specializations — guarding against overspecification, so a general block stays readable and reusable on its own.
- references then tend to run specific → general, keeping the graph stable toward the fundamentals.

### appendix

- the typical drift it guards against: specific detail accreting onto a general block.
- namespace exception: an umbrella/namespace concept may list its members in `meta` (membership is constitutive); ordinary blocks reach upward only.
