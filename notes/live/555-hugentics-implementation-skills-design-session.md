# Hugentics Implementation Skills - design-session

## Session.Abstract

- intent: walk through the mined improvement proposal for `hugentics-impl-designer`, `hugentics-impl-executer`, and `hugentics-codebase-cleaner`, making explicit design decisions about each proposal area
- active focus: decide the shared contract that should connect cleanup candidate selection, `Impl.Req` design, and implementation execution
- references: [554-hugentics-implementation-skills-mining-report.md](554-hugentics-implementation-skills-mining-report.md); academy mining — Pocock "Workflow for AI Coding" (`~/projects/academy/workflow-for-ai-coding/working-summaries/001-agentic-development-workflows.md` + repo `.claude/skills/tdd`)
- state: active
- next: decide whether the upgrade should be organized around one shared `Impl.Req` execution contract before discussing skill-specific improvements

## Design.Index

### Hugentics.Implementation.Skill.Chain

- the active design target is the three-skill chain: `hugentics-codebase-cleaner` -> `hugentics-impl-designer` -> `hugentics-impl-executer`
- the mining report proposes strengthening the contracts between these phases rather than adding broad generic engineering advice
- the session must decide which concepts are shared chain-level contracts and which remain owned by one skill
- the session will walk through every major proposal area before producing implementation guidance

#### meta

- status: open
- source: `554-hugentics-implementation-skills-mining-report.md`
- active question: should one shared `Impl.Req` execution contract organize the upgrade?

### Impl.Req.Execution.Contract

- candidate shared contract connecting implementation design and execution
- accepted as a shallow umbrella composed of smaller contracts rather than one monolithic section
- the contract should force enrichment before execution: every key aspect is either filled in or explicitly marked not applicable with a reason
- candidate responsibilities include scope, evidence, readiness, slices, dependencies, feedback loops, verification, deviation handling, and completion
- the designer would produce the contract in the `Impl.Req`
- the executer would validate and walk the contract
- outer workflows such as the cleaner would shape their handoff around the same contract

#### meta

- status: accepted direction
- unresolved: exact contract section names and field structure

### Alignment.Checkpoint

- a declared point in a skill workflow where the agent checks something before proceeding
- it is a checkpoint **because it can be an alignment opportunity** — a place where the human could meaningfully weigh in
- a decision the agent *always* resolves alone is **not** a checkpoint; it is just a normal workflow step
- every checkpoint sits at an **explicit declared position**; it may carry an optional **activation condition** that decides whether it fires when reached (e.g. "design did not fit reality") — not a separate kind, just a gated positional checkpoint
- the check always runs; `Alignment.Mode` only decides **who resolves it**:
  - `Interactive` → the agent may spawn an `Alignment.Turn` and prompt the user
  - `Autonomous` → the agent resolves the checkpoint itself, no prompting
- checkpoints are declared explicitly, so a skill's alignment surface is inspectable up front

#### discipline

- the agent must not invent new checkpoints
- the agent must not stop execution outside a declared checkpoint — no ad-hoc halts
- deviation (design-reality mismatch) is handled at a declared checkpoint via an activation condition, not as an anywhere-interrupt

#### meta

- status: converged

### Alignment.Mode

- an argument accepted by hugentic skills: its name is `Alignment.Mode`, its type is the value enum below
- governs only the `Alignment.Checkpoint` axis — who resolves each checkpoint
- values:
  - `Interactive` (default) → checkpoints are alignment opportunities, well-defined in the skill
  - `Autonomous` → no user prompting; the agent carries the process and resolves every checkpoint itself
- supersedes the earlier three-value model: `Gated` merges into `Interactive`; the `none`/`phase`/`slice`/`custom` `User.Gate.Policy` axis is dropped — granularity now lives in which points a skill declares as checkpoints

#### meta

- status: converging
- scope note: this is one skill axis, not a global control model; a skill may carry other independent axes

### Execution.Policy

- after the gating split, `Execution.Policy` is NOT a control model and does not own gating
- the gating axis (`User.Gate.Policy`) is superseded by `Alignment.Checkpoint` + `Alignment.Mode`
- the remaining candidate axes stay separate and must not be folded into `Alignment.Mode`:
  - `Deviation.Policy` — how design-reality mismatch is handled during execution
  - `Reporting.Policy` — output cadence during execution (not a gate)

#### appendix

- updated conceptual split:

```txt
Impl.Req.Execution.Contract
├── Scope.Contract
├── Evidence.Contract
├── Readiness.Contract
├── Slice.Contract
├── Dependency.Contract
├── Feedback.Loop.Contract
├── Verification.Contract
├── Deviation.Contract
└── Completion.Contract

Alignment.Checkpoint (gating axis) ──governed by──> Alignment.Mode { Interactive | Autonomous }

Execution.Policy (residual, non-gating)
├── Deviation.Policy
└── Reporting.Policy
```

#### meta

- status: gating axis converged; residual axes open
- todo: audit earlier sections for overlap with `Alignment.Checkpoint` and remove any double-defined gating

### Executable.Feedback.Loop

- the `Impl.Req` **must** name an executable signal answering "did this work?" — required, not optional
- two altitudes, both wanted: **per-slice** (tight, primary) and **per-Impl.Req** (aggregate acceptance)
- pick the best available signal; "no reliable loop" is atypical and to be actively avoided, not a default
- signal preference (ladder detail belongs to topic 5):
  1. existing reliable check (test / CLI / type check / linter / artifact diff)
  2. agent-constructed signal (throwaway script, printed partials, ad-hoc comparison)
  3. manual inspection with explicit criteria — fallback floor only
- executer: confirm the loop is available, establish the **baseline before editing**, record pre-existing failures or unavailable checks

#### meta

- status: converging
- overlap: signal ladder == topic 5 `Verification.Ladder` (define once)
- readiness: "feedback loop named" is a `Readiness.Contract` requirement (topic 3)

### Alignment.Checkpoint:Readiness

- a named `Alignment.Checkpoint`, **right before the `Impl.Req` is written**, after research/understanding
- establishes the `Alignment.Checkpoint:<Name>` naming convention (parallels `Alignment.Mode:<Value>`)
- backed by a **readiness checklist** the agent uses to detect what's missing for a good `Impl.Req`:
  - scope / out-of-scope explicit
  - current state inspected & cited
  - every slice has an observable result + check
  - feedback loop named (topic 2)
  - dependencies / ordering explicit
  - no unresolved decision hidden inside an execution step
  - understandable without chat context
- flow:
  1. run the checklist → find gaps
  2. the agent **tries to resolve each gap itself** (research, construct a feedback loop, decide)
  3. whatever it **can't** resolve alone → raise it here as a final alignment question
- governed by `Alignment.Mode`: `Interactive` may raise unresolved needs; the agent may find nothing to raise; `Autonomous` must self-resolve everything
- **bounded:** user in-loop as long as they want; then the agent finishes the `Impl.Req` with all accumulated feedback
- the checklist **drives the checkpoint; it does not bloat the `Impl.Req`** — it is a gap-detector, not a documentation mandate

#### meta

- status: converged
- open: keep a light executer-side entry readiness check, or trust this pre-write gate?

### Test.First

- TDD is integrated at its `Natural.Placement` in the framework, not bolted on:
  - **topic 3 `Alignment.Checkpoint:Readiness`** → the `Impl.Req` names the **behaviors / acceptance to test** (behaviors, not implementation steps) — this is "design tests in advance" done right, the anchor against overfitting
  - **topic 5 per-slice rung** → **RED → GREEN test-first**, one behavior at a time: failing behavior test, then minimal code to pass
- the *in-advance* part is **naming behaviors**; the *actual tests* are written per slice during execution
- **banned: all-tests-up-front** — writing every test before any implementation produces tests of *imagined* behavior/shape that pass when behavior breaks
- anti-cheating rationale: the test instruments behavior *before* the implementation exists, so the agent cannot retrofit a test that merely rubber-stamps what it built
- per-cycle test guard: describes behavior not implementation · public interface only · would survive an internal refactor · minimal code · no speculative features

#### meta

- status: accepted direction
- placement: spans topic 3 (name behaviors) + topic 5 (RED→GREEN per slice)
- source: academy mining — Pocock `tdd` skill

### Impl.Req.Lifecycle

- `Impl.Req` artifacts are **transient** — that is why they live on the `Live.Note` surface
- maintained only around the time of the implementation, not kept as long-lived repo docs
- this sidesteps the doc-rot failure (stale planning docs misleading future agents): there is nothing durable to rot
- resolves the lifecycle aspect of parked topic 7 for our case

#### meta

- status: converged
- source: existing `Live.Note` transient model + academy doc-rot warning

### Standards.Push.Pull

- coding standards load differently by role:
  - **implementer → pull**: standards available as skills/docs the agent reads when relevant
  - **reviewer → push**: standards injected into context so the review explicitly checks against them
- rationale: a reviewer must actively measure against the standard; an implementer can fetch on need

#### meta

- status: accepted direction
- source: academy mining — Pocock push/pull framing
- note: our chain has no explicit reviewer skill yet; applies if/when a review checkpoint exists

### Report.Walkthrough

- each major report topic should receive an explicit outcome: adopt, adapt, reject, park, or merge into another concept
- discussion should begin with shared chain-level decisions, then move through designer, executer, cleaner, packaging, and evaluation topics
- the report remains proposal evidence; accepted session decisions belong in this artifact

#### meta

- status: accepted session method

## Session.Notes

### Decision Queue

1. Shared chain contract and ownership boundaries
2. Executable feedback loops
3. `Impl.Req` readiness and reader testing
4. Slice dependency semantics and vertical-slice quality
5. Verification ladder
6. Deviation taxonomy
7. `Impl.Req` state model
8. Canonical `Impl.Req` template and current-state evidence
9. Executer baseline, slice entry/exit, and final acceptance review
10. Git checkpoint boundary and caller consistency
11. Cleanup candidate selection, evidence, deletion test, and cleanup classes
12. Trigger descriptions, progressive disclosure, structural validation, and behavioral evaluation
13. Avoid list and final upgrade ordering

### Working Rules

- discuss one decision topic at a time
- record an explicit outcome for every major report topic
- keep shared contracts distinct from skill-local operational instructions
- avoid growing the skills with generic engineering material that does not improve the chain
- do not edit the target skills until the session produces an implementation handoff

### Immediate Known Correction

- `hugentics-codebase-cleaner` still claims the executer owns per-slice commits
- this contradicts the executer's accepted pre-execution-only git checkpoint contract
- correction is expected, but its exact placement should follow the checkpoint-boundary discussion

### Parking Lot

- exact reference-file names
- whether a deterministic `Impl.Req` structural validator is justified
- behavioral evaluation prompts for the full three-skill chain
- whether `Alignment.Mode` remains a preset layer over granular execution policy arguments

## Session.Log

- 2026-06-06: Created the design session to walk through `554-hugentics-implementation-skills-mining-report.md` and make explicit decisions about each proposal area.
- 2026-06-06: Set the first active focus to the shared contract and ownership boundaries across the three-skill chain.
- 2026-06-06: Accepted `Impl.Req.Execution.Contract` as a shallow umbrella that forces pre-execution enrichment across smaller contract areas; separated runtime user gating into `Execution.Policy`.
- 2026-06-08: Collapsed the gating model to two `Alignment.Mode` values (`Interactive` default, `Autonomous`) and introduced `Alignment.Checkpoint` as the declared alignment-opportunity points a skill exposes. `Gated` and the `User.Gate.Policy` axis are superseded by checkpoints + mode; `Deviation.Policy` and `Reporting.Policy` remain separate skill axes. `Alignment.Mode` is one skill axis, not a global control model.
- 2026-06-08: Resolved the positional/conditional question — one `Alignment.Checkpoint` concept: a declared position optionally gated by an activation condition. Added discipline rules: the agent must not invent checkpoints and must not stop outside declared ones. Deviation is handled at a declared checkpoint via a condition, not an anywhere-interrupt.
- 2026-06-08: Decided topic 2 `Executable.Feedback.Loop`: a feedback loop is mandatory at both per-slice and per-Impl.Req altitudes; agent must construct a signal (scripts/partials) before falling back to manual inspection with explicit criteria. Signal ladder deferred to topic 5; "feedback loop named" routed to the `Readiness.Contract` (topic 3).
- 2026-06-08: Decided topic 3 as `Alignment.Checkpoint:Readiness` — a single named checkpoint right before the `Impl.Req` is written. A readiness checklist detects gaps; the agent resolves what it can and raises the rest as a final alignment pass (governed by `Alignment.Mode`). Deliberately light: a gap-detector and needs gate, not a documentation mandate. Establishes the `Alignment.Checkpoint:<Name>` convention. Open: whether the executer keeps a light entry readiness check.
- 2026-06-09: Mined academy / Pocock "Workflow for AI Coding". Captured `Test.First` (TDD at `Natural.Placement` — name behaviors at readiness, RED→GREEN per slice, ban all-tests-up-front to avoid imagined-shape tests), `Impl.Req.Lifecycle` (transient live-notes, resolves topic 7 doc-rot), and `Standards.Push.Pull` (implementer pulls, reviewer pushes). Dropped fresh-context review (user responsibility for now). Strong independent-convergence signal: grill-me≈design session, PRD≈Impl.Req, tracer-bullet slices≈topic 4, feedback-loops-as-quality-ceiling≈topic 2.
