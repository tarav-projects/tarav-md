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

- [DF] `User.Model.Space` is a `QA.Space` about the user ^c20260729-277u
- [DC] it models what the system knows about what the user said, wanted, rejected, approved, left open, or delegated ^c20260729-217u
- [CT] its claims are evidence-scoped and belong only to the extent that a touched surface grounds them ^c20260729-114u
- [PR] `Hugentic.Chat.Surface` is its natural placement because repeated dialogue records changing judgment and context ^c20260729-323u
- [CT] non-chat `User.Touch` may also condition the model when its provenance is available ^c20260729-122u
- [PR] growing `Touched.Space` improves the user model by increasing its grounded interaction evidence ^c20260729-335u

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

- [DF] `User.Touched` is the property of data carrying evidence of `User.Touch` ^c20260729-279u
- [DF] `User.Touch` is an event in which the user engages a subject, providing the primitive evidence that the subject entered `Touched.Space` ^c20260729-278u
- [CT] the system does not observe `User.Touch` directly; it reaches touch only through its materialization on a `Touch.Authority.Surface` ^c20260729-155u
- [CT] touch is general over stated, discussed, approved, corrected, rejected, co-drafted, or explicitly delegated material ^c20260729-160u
- [DC] authorship is not the touch boundary: an agent may construct the data while its touch comes from user evidence ^c20260729-198u
- [CT] `User.Touched` separates `Touched.Space` from `Untouched.Space`; it does not decide whether a region is open, constrained, or fixed ^c20260729-52u
- [DC] `User.Touched` is derived per datum from touch provenance rather than stored as membership in a surface category ^c20260729-176u

****

## Touch.Authority.Surface

- [DF] `Touch.Authority.Surface` is a registered surface that serves as an inbox for direct `Touched.Data` ^c20260729-268u
- [DF] a qualifying edition is a change that the surface recognizes as materializing `User.Touch` ^c20260729-292u
- [CT] the system observes qualifying surface editions, not the underlying `User.Touch` itself ^c20260729-156u
- [DC] data materialized by a qualifying edition is considered first-order `Touched.Data` by default ^c20260729-204u
- [CT] first-order touch classification is defeasible: later evidence may disqualify the edition or exclude particular data from its touched extent ^c20260729-102u
- [DC] each `Touch.Authority.Surface` defines which editions qualify and which data within them was touched ^c20260729-206u
- [CT] registration does not make every edition touched; a nonqualifying edition carries no direct touch ^c20260729-129u
- [CT] disqualification concerns touch provenance; factual error, staleness, or contradiction alone does not mean the data was never touched ^c20260729-87u
- [DC] a qualifying `User.Turn` is presently the only registered realization of `Touch.Authority.Surface` ^c20260729-187u
- [PR] `Chat.Surface` is the natural container and context surface for that realization ^c20260729-321u

****

## Touched.Data

- [DF] `Touched.Data` is data whose provenance reaches `User.Touch` through a qualifying `Touch.Authority.Surface` edition or through grounding ^c20260729-270u
- [DC] data materialized on the authority surface has defeasible first-order provenance; a grounded projection carries second-order provenance ^c20260729-205u
- [CT] touch provenance does not certify factual truth, internal consistency, or currentness ^c20260729-161u
- [PR] touched data conditions agent action according to what its evidence supports ^c20260729-357u

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
- [DC] untouched material never becomes an index line directly; and touch alone lands nothing — material, touched or not, remains in chat, work surfaces, source surfaces, or `Index.Agendix` until landed through the gate ^c20260716-63u
- [PR] alignment grows by moving important regions from `Untouched.Space` into `Touched.Space`

****

## Open.Space

- [DF] `Open.Space` is the region of a `QA.Space` where meaningful agent choice remains
- [DC] in `Open.Space`, the agent makes its own decisions to act: coherent, never random, and provisional
- [CT] `Open.Space` is orthogonal to touch: it may be untouched, or it may be touched by an explicit free declaration (`FR`)
- [CT] consequences logically entailed by constraints are not open; the agent may fail to derive them, but is not free to decide against them
- [DC] open resolutions become directive constraints only once touched

****

## Open.Inference

- [DF] `Open.Inference` is an agent conclusion or decision made where applicable `Touched.Data` leaves the answer unresolved ^c20260729-262u
- [CT] an answer may remain unresolved because touched data is absent, incomplete, ambiguous, or contradictory ^c20260729-69u
- [DC] the agent evaluates provenance, applicability, currentness, support strength, and consequences before selecting an answer ^c20260729-234u
- [DC] open inference selects a coherent provisional action within the answer region left available by touched constraints ^c20260729-223u
- [CT] its conclusion carries no `Touched.Authority` of its own ^c20260729-115u
- [CT] it does not silently rewrite or discard touched positions that remain unresolved ^c20260729-110u
- [FR] the agent may act on open inference without waiting for additional `User.Touch` ^c20260729-318u
- [CT] changing a gated touched surface remains a separate reconciliation action even when open inference permits other work to proceed ^c20260729-76u

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

- [DF] `Touched.Authority` is the precedence rule by which `Touched.Data` conditions `Open.Inference` according to its provenance and meaning ^c20260729-269u
- [CT] touched authority is relative to `Open.Inference`; it is not a certificate of truth ^c20260729-162u
- [CT] touched data may be incomplete, stale, false, or mutually contradictory ^c20260729-163u
- [CT] an agent may not silently replace coherent touched data with its own `Open.Inference` ^c20260729-67u
- [CT] an agent must not blindly follow touched data whose applicable claims are incoherent ^c20260729-68u
- [DC] every `Touched.Surface` maintains a coherent live projection; detected incoherence is a `Point.Of.Interest` ^c20260729-210u
- [PR] resolution descends through provenance and may create new `User.Touch` while preserving the contradictory history ^c20260729-346u
- [DC] authority status is derived from provenance on the surface rather than stored ^c20260729-197u

****

## Touched.Decision.Cycle

- [DF] `Touched.Decision.Cycle` is the decision discipline repeated within product design and realization ^c20260729-271u
- [DC] contextualization loads the `Touched.Data` relevant to the active decision ^c20260729-203u
- [DC] incoherent touched constraints become `Point.Of.Interest` instances before they are treated as guidance ^c20260729-212u
- [CT] coherent touched constraints condition the valid answer region ^c20260729-79u
- [FR] regions not determined by touched constraints are completed through `Open.Inference` ^c20260729-315u
- [DC] action advances the current `Target.Product` ^c20260729-192u
- [DC] reconciliation compares the changed product with its touched design and adjacent surfaces ^c20260729-225u
- [PR] reconciliation may expose another decision and begin a nested cycle ^c20260729-342u

****

## Constraint.Steering

- [DF] `Constraint.Steering` is the design principle that we steer agent work by designing constraints — saturating surfaces with checkable assertions so that consistency pressure pulls the work in the designed direction ^c20260719-45u
- [DC] mint-time test: a finite vocabulary forces commitment at write time — confused content fails to type, the earliest and cheapest drift detection ^c20260719-29u
- [DC] standing test: the assertion rides next to the content forever; every later pass has a small, local, closed-set claim to check against ^c20260719-33u
- [DC] graded checkability: part of each assertion is CPU-checkable (presence, vocabulary membership, resolution), the rest agent-checkable — design pushes each assertion down the gradient; agent-checkable is the floor, never zero ^c20260719-26u
- [DC] direction-forcing: designing the constraint vocabulary IS steering the system — assertions encode what better looks like, so many small consistency checks pull the surfaces toward it ^c20260719-22u
- [DC] stability: an assertion is a semantic invariant a rewrite must preserve — constraints make a surface stable under agent rewriting; the agent may rephrase, never drop the pinned semantics ^c20260719-32u
- [PR] the compiler loop: agent-generated code must compile, and that feedback loop bounds generation — it either never converges or converges at least to compilable output; assertions + linting generalize the loop to text: the generated surface must comply with many tests, it is never "generate what you like" ^c20260719-50u
- [DC] instances: `Line.Type`, anchors + support sets (`Touched.Support.Network`), skw claims (`Skw.Ann.Dependency`), the annotation↔generated-surface sync (`Skw.Annotation`), gates, bless records ^c20260719-28u

****

## Accountable.Assertion

- [DF] an `Accountable.Assertion` is the unit `Constraint.Steering` deposits: a recorded claim carrying frozen judgment (the stamp) and its audit path, so any agent can call it to account on demand ^c20260719-47u
- [DC] a stamp is judgment cached at mint time, never truth — checking recomputes the claim against its evidence ^c20260719-18u
- [DC] the trail has two realizations — integrated on-surface (for example an `Index.Line`'s type tag: evidence local to the value) or held in an external general schema (for example an `Anchory` dossier: audit requires descent); the axis between them is audit cost ^c20260719-42u
- [DC] the frozen judgment is someone's — user or agent — and the stamp says whose; accountability is the general property, authority stays read from provenance (`Touched.Authority`) ^c20260719-38u
- [DC] the audit path can accumulate evaluation records — verdicts by any evaluator, appended openly, folded on read; a second record family beside the gated evidence dossier ^c20260720-44u
- [CT] evaluation is confidence, never authority — no fold of verdicts changes what the assertion's evidence supports ^c20260720-32u

****

## Producer.Aids.Checker

- [DF] `Producer.Aids.Checker` is the principle that the capable producer bears the structuring burden so the verifier can stay simple — complexity moves to the producer, not the checker ^c20260726-39u
- [PR] in an agent–CPU pair the `Agentic.Program` produces and shapes its output so the verifying `CPU.Program`'s job is trivial ^c20260726-44u
- [DC] it is a division of labor, not redundancy: the producer deposits the claim and its audit path (`Accountable.Assertion`), the checker only walks that path ^c20260726-24u
- [CT] the checker judges form and audit-path, never meaning — semantic judgment stays with the human or the producer ^c20260726-20u
- [PR] prefer it whenever richer producer output would simplify a check: structuring is paid once by the producer, the check then runs cheaply and lowers audit cost (`Index.Line`) ^c20260726-45u
- [EX] `Line.Verbatim.Gate` applies it: the agent emits the verbatim line plus an `Edition.Approval.Token` so the linter verifies review by a deterministic token walk, not semantic inspection ^c20260726-41u

****

## Line.Type

- `Line.Type` is the classification a `Kernel.Line` carries, written as a typed prefix from the `Line.Type.Vocabulary`
- classifying is the line-level gate — it forces significance the way naming gates a block; the small cost is the point, a cost-zero index overwhelms the user
- naming once bundled three filters — identification, boundary, significance; the line-level tests unbundle them: a crisp single point (`Kernel.Line`), attaching to a block (`Index.Edit.Append.Line`), and significance (`Line.Type`)
- syntax: a leading bracketed code — `- [CT] the anchor token stays small`; the type is read first and primes the line, the tail stays free for inline anchors
- every line is typed, the definition first line explicitly `[DF]` — untyped lines are mechanically detectable (no leading bracket), the pre-fence legacy the calibration passes work down
- [DC] the act axis (`CT`, `DC`, …) is the type — the assistant-grounded source marker (`[AS:XX]`) is retired: all typed lines are user-grounded on every surface ^c20260716-60u

- [PR] typing makes the index computable — backward, lint for coherence; forward, agents derive their bounds and freedoms mechanically instead of interpreting prose ^c20260707-8u
- [PR] static typing for agent-produced surfaces: the type disciplines the content, not describes it — most of its value is paid at write time ^c20260719-48u
- [DC] the type adds stability: it pins what any rewrite must preserve — an agent cannot rewrite a line "just because"; the rewrite must still satisfy the tag ^c20260719-43u

****

## Line.Type.Vocabulary

- `Line.Type.Vocabulary` is the controlled set of `Line.Type`s an index uses — small, curated, soft (`Concept.Hardness`); extensible, not a hard enum
- each type is a verb on the `Design.Space` — types sort by how a line acts on the space: collapsing it, describing it, or declaring it open
- a type earns its place when a recurring line-act has no home; a type that attracts filler is a smell
- [PR] each type creates a validation point: a typed line must perform its act — a constraint line must constrain something; a typed line that performs nothing is mistyped filler ^c20260707-9u
- [PR] the vocabulary is the fence of the index: index content is what the vocabulary can express — a line that can take no type belongs elsewhere; developing the vocabulary is deciding what the index is for ^c20260707-10u
- [CT] scope widens only by widening the vocabulary — a visible, gated act, instead of line-by-line scope creep ^c20260707-11u
- [DC] calibration: type the live index against a candidate vocabulary and inspect what remains untyped — each residue is a discussion: out of the index, or a vocabulary extension ^c20260707-12u

****

## Line.Type::DF

- [DF] `Line.Type::DF` marks a definition — the line fixes what a name means ^c20260708-21u
- [CT] validation point: the line must bind a name to a meaning; a `DF` that introduces no name is mistyped ^c20260708-22u
- [DC] lint: two `DF` lines binding the same name to different meanings, and a block whose first line is not a `DF` ^c20260708-23u

****

## Line.Type::DC

- [DF] `Line.Type::DC` marks a decision — the line pins a `Design.Variable` to a value ^c20260707-13u
- [CT] validation point: the line must name what was decided and the value it took; a `DC` that pins nothing is mistyped ^c20260707-14u
- [DC] lint: two `DC` lines pinning the same variable to different values is a contradiction to surface ^c20260707-15u

****

## Line.Type::CT

- [DF] `Line.Type::CT` marks a constraint — the line bounds a `Design.Variable` to a subset without picking a value ^c20260707-16u
- [CT] validation point: the line must exclude something; a `CT` that rules nothing out is filler ^c20260707-17u
- [DC] lint: constraints whose intersection is empty, and a `CT` silently violated by a later `DC` ^c20260707-18u

****

## Line.Type::RJ

- [DF] `Line.Type::RJ` marks a rejection — the line excludes a considered alternative ^c20260707-19u
- [CT] validation point: the line must name the rejected alternative, preferably with the reason ^c20260707-20u
- [DC] lint: a rejected alternative later reintroduced without a new touch ^c20260707-21u

****

## Line.Type::PR

- [DF] `Line.Type::PR` marks a principle — a generative orientation that spawns constraints across many variables ^c20260707-22u
- [CT] validation point: the line must orient decisions beyond one variable; a `PR` scoped to a single variable is a `CT` ^c20260707-23u
- [DC] lint: decisions or constraints that run against a standing principle ^c20260707-24u

****

## Line.Type::FR

- [DF] `Line.Type::FR` marks a free declaration — the user explicitly leaves a `Design.Variable` agent-owned ^c20260707-25u
- [CT] validation point: the line must name what is left open; freedom is a touched act, not an omission ^c20260707-26u
- [DC] lint: a `FR` variable later constrained without retiring the declaration ^c20260707-27u

****

## Line.Type::EX

- [DF] `Line.Type::EX` marks an example — the line illustrates another line's claim with a concrete case ^c20260707-28u
- [CT] validation point: the line must exemplify something specific; an example that illustrates no claim is filler ^c20260707-29u
- [DC] lint: an example inconsistent with the constraints and decisions it illustrates ^c20260707-30u

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

- [DF] `Alignment.Loop.Gradient` orders `What.Design`, `How.Design`, and `Impl.Exec` by their abstraction and distance from concrete realization ^c20260729-250u
- [CT] the ordering is not a mandatory workflow sequence; a `Product.Design.Session` may expose any subset of the concerns ^c20260729-148u
- [DC] concerns already resolved by touched data, skill contracts, or stable surfaces remain implicit ^c20260729-200u
- [CT] every exposed loop is non-stable staging that advances a `Target.Product` ^c20260729-98u
- [DC] `What.Design` works closest to the abstract ontology ^c20260729-179u
- [DC] `How.Design` contextualizes that design against implementation concerns and plans a path ^c20260729-166u
- [DC] `Impl.Exec` works closest to concrete implementation surfaces ^c20260729-167u
- [FR] movement is bidirectional; later concerns may reopen earlier design or land insights into the `Touched.Index` ^c20260729-313u

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

- [DF] `Delta.Normalization` is incremental derivation in a `Normalization.Pipeline`: normalize only source records added since the last pass plus the model's volatile tail, instead of re-deriving the whole `Normal.Model` ^c20260712-69u
- [PR] it applies better to append-friendly target models — an append-only body with per-line provenance and finality; the `Normalization.Pipeline` does not require its targets to be append-friendly ^c20260712-93u
- [DC] the unit of work is the stable-prefix / volatile-tail split — content whose derivation is final is frozen and skipped; only the volatile tail and new source records are recomputed ^c20260712-55u
- [DC] resume state persists in a `Normalization.Delta.Checkpoint`; a checkpoint that fails validation discards itself and the pass falls back to full derivation ^c20260712-47u
- [CT] full derivation from raw sources remains always available and authoritative — delta passes are an optimization, never a new source of truth ^c20260712-31u

****

## Normalization.Delta.Checkpoint

- [DF] `Normalization.Delta.Checkpoint` is the persisted resume state of `Delta.Normalization` for one source — whatever the producer needs to continue derivation from the recorded source position ^c20260712-71u
- [DC] the checkpoint is producer-private — only the pipeline that wrote it reads it; it is never a consumer surface of the `Normal.Model` ^c20260712-51u
- [DC] it validates before use: the source must still extend the position it recorded; a failed validation discards the checkpoint and the pass re-derives fully ^c20260712-43u
- [CT] the checkpoint is disposable at any time with no data loss — deleting it costs one full derivation, nothing else ^c20260712-35u

****

## Normalization.Trust.Tier

- [DF] `Normalization.Trust.Tier` is the verification level a caller selects for a `Delta.Normalization` pass — how much of the existing `Normal.Model` is re-checked against source before being trusted ^c20260712-73u
- [DC] three tiers: trust-append assumes the source only grew and resumes blindly from the checkpoint; verify re-checks provenance over the frozen content and recomputes from the first divergence; rebuild re-derives everything from source ^c20260712-56u
- [PR] staleness is a price point, not a defect — when raw sources are preserved and authoritative, a wrong cheap pass is always recoverable by a more expensive one ^c20260712-98u
- [CT] tier selection changes cost and staleness risk only, never the model contract — every tier produces the same model shape ^c20260712-37u

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
- soft meaning surfaced as a chat sigil — rides `Concept.Hardness`, sibling to `::` type statements (`Addressing.Sigil.Vocabulary`) and the variable `<Concept>.Name` form ^c20260712-21u

****

## General.Avoids.Specific

- a block's references tend to point up — a specialization references the general; a general block, as a rule of thumb, avoids reaching down into its specifics.
- the aim is to keep a fundamental independent of its specializations — guarding against overspecification, so a general block stays readable and reusable on its own.
- references then tend to run specific → general, keeping the graph stable toward the fundamentals.

### appendix

- the typical drift it guards against: specific detail accreting onto a general block.
- namespace exception: an umbrella/namespace concept may list its members in `meta` (membership is constitutive); ordinary blocks reach upward only.
