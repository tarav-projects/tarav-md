> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## What.Design.Session

- `What.Design.Session` is a scoped human-agent convergence surface for design work — the `What.Design` specialization of `Alignment.Session`, run through `Alignment.Loop:What`
- it does real design work (problem-solving, issue resolution) while progressively enriching alignment, aiming to fill `Alignment.Hugentic.Axis:What` with `Hard.Evidence`-based facts
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

- `Forward.Alignment` is moving the design point to a new place in the `Conceptual.Space` — adding features, evolving design, exploring new territory
- the creative act of development: deciding where to go next

****

## Internal.Alignment

- `Internal.Alignment` is keeping all surfaces in sync at the current design state
- for a given design point, moving all other surfaces to follow it
- the maintenance act of development: ensuring coherence across code, index, skills, docs

****

## Hugentic.Alignment

- `Hugentic.Alignment` is bringing human and agent to shared understanding of where they are and where they're going in the `Conceptual.Space`
- the convergence act: achieved through `Alignment.Loop` cycles

****

## Conceptual.Space

- `Conceptual.Space` is the abstract space where alignment occurs — the set of all possible design decisions
- `Alignment.Space` is a synonym
- `Design.Target.Model` is a point in this space

****

## Alignment.Hugentic.Axis

- `Alignment.Hugentic.Axis` is a dimension of the `Conceptual.Space` that needs human-agent convergence
- each workflow specialization defines its own set of axes
- the axes are the focus of the `Alignment.Loop`

****

## Alignment.Agentic.Axis

- `Alignment.Agentic.Axis` is a dimension the agent resolves autonomously without explicit human convergence

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
- distinct from `Soft.Programming.Language`: `Soft.Program` is program-as-behavior-pattern; `Soft.Programming.Language` is language-as-index/runtime semantics

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
