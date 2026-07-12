# Hugentics Implementation Skills - design-session

## Session.Abstract

- intent: walk through the mined improvement proposal for `hugentics-impl-designer`, `hugentics-impl-executer`, and `hugentics-codebase-cleaner`, making explicit design decisions about each proposal area
- active focus: integrate converged concepts into the index and skills; clean up superseded session concepts
- references: [554-hugentics-implementation-skills-mining-report.md](554-hugentics-implementation-skills-mining-report.md); academy mining — Pocock "Workflow for AI Coding" (`~/projects/academy/workflow-for-ai-coding/working-summaries/001-agentic-development-workflows.md` + repo `.claude/skills/tdd`)
- state: active
- next: resume the decision queue at topic 4 (slice dependency semantics); pending integration: the executer's two-value `Alignment.Mode` + `Alignment.Checkpoint` rewrite

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

- status: gating axis converged; `Deviation.Policy` folds into a conditional `Alignment.Checkpoint`; `Reporting.Policy` is the only residual axis
- audit done: no double-defined gating remains

### Executable.Feedback.Loop

- **folded into the existing index concept `Test.At.Boundaries`**, which already states feedback loops are the quality ceiling and that every `Impl.Req` names what validates the work
- "feedback loop named" lives in `Alignment.Checkpoint::Readiness` (the readiness checklist) and the `Impl.Req`
- the signal-preference order (existing check > agent-built script > manual inspection) is execution guidance under `Test.At.Boundaries`, not a separate concept
- one surviving idea not in the cluster: establish the **baseline before editing** (run existing checks, record pre-existing failures) so introduced breakage is distinguishable — candidate one-liner addition to `Test.At.Boundaries`

#### meta

- status: folded into `Test.At.Boundaries` — not minted as a new concept

### Alignment.Checkpoint::Readiness

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
- resolved: keep both — the executer also runs a light `Alignment.Checkpoint::Executable` entry check ("still executable now?") before the git checkpoint

### RED.GREEN.Test.Suite

- `RED.GREEN.Test.Suite` is the set of RED/GREEN-style tests an `Impl.Req` calls for, written test-first to drive the implementation
- an `Impl.Exec` `Development.Principle`: the `Impl.Req` specifies the suite; the executer builds it test-first (each test goes RED → minimal code GREEN → next; never all tests up front)
- the *in-advance* part is naming the behaviors to test at `Alignment.Checkpoint::Readiness`; the actual tests are written test-first during execution
- **not the only tests** — it is the implementation-driving core; more tests may be added later, e.g. at the end
- `No.Regression.Tests.Allowed` governs **all** tests including this suite — keep it core-feature / e2e / durable-contract focused, not regression slop
- `Test.At.Boundaries` governs what each test asserts — public behavior that survives a refactor
- rationale: writing the test before the code prevents retrofit tests that merely rubber-stamp the implementation (anti-overfit, anti-cheat); all-tests-up-front is banned because bulk tests assert imagined shape and pass when behavior breaks

#### meta

- status: converged — landed in the index (`Development.Principles` member) and the designer/executer skills
- renamed from `Test.First`
- placement: `Development.Principles` member for `Impl.Exec`; the `Impl.Req` carries the suite, the executer builds it
- source: academy mining — Pocock `tdd` skill, reconciled with the existing test cluster (`No.Regression.Tests.Allowed`, `Test.At.Boundaries`)

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

1. Shared chain contract and ownership boundaries — ✅ `Impl.Req.Execution.Contract`, `Alignment.Checkpoint`, `Alignment.Mode`
2. Executable feedback loops — ⤵ folded into `Test.At.Boundaries`
3. `Impl.Req` readiness and reader testing — ✅ `Alignment.Checkpoint::Readiness`
4. Slice dependency semantics and vertical-slice quality — pending (next)
5. Verification ladder — ✖ dropped (≈ existing test cluster; only baseline-before-editing was new)
6. Deviation taxonomy — pending (deviation is now a conditional `Alignment.Checkpoint`)
7. `Impl.Req` state model — ✅ `Impl.Req.Lifecycle` (transient)
8. Canonical `Impl.Req` template and current-state evidence — pending
9. Executer baseline, slice entry/exit, final acceptance review — partly landed via `RED.GREEN.Test.Suite` + executer edits; pending consolidation
10. Git checkpoint boundary and caller consistency — pending
11. Cleanup candidate selection, evidence, deletion test, and cleanup classes — pending
12. Trigger descriptions, progressive disclosure, structural validation, and behavioral evaluation — pending
13. Avoid list and final upgrade ordering — pending

Also captured outside the original queue: `RED.GREEN.Test.Suite`, `Standards.Push.Pull`, `Designer.Turn.Kernel.Form` (all landed in the index/skills).

### Working Rules

- discuss one decision topic at a time
- record an explicit outcome for every major report topic
- keep shared contracts distinct from skill-local operational instructions
- avoid growing the skills with generic engineering material that does not improve the chain
- implementation has begun: converged concepts land incrementally in the index and skills (no single handoff document); keep each landing gated

### Immediate Known Correction — RESOLVED

- `hugentics-codebase-cleaner` previously claimed the executer owns per-slice commits, contradicting the executer's pre-execution-only git checkpoint contract
- fixed 2026-06-09 during the `Alignment.Mode` cascade: the cleaner now states the pre-execution checkpoint is the only commit phase

### Parking Lot

- exact reference-file names
- whether a deterministic `Impl.Req` structural validator is justified
- behavioral evaluation prompts for the full three-skill chain

## Session.Log

- 2026-06-06: Created the design session to walk through `554-hugentics-implementation-skills-mining-report.md` and make explicit decisions about each proposal area.
- 2026-06-06: Set the first active focus to the shared contract and ownership boundaries across the three-skill chain.
- 2026-06-06: Accepted `Impl.Req.Execution.Contract` as a shallow umbrella that forces pre-execution enrichment across smaller contract areas; separated runtime user gating into `Execution.Policy`.
- 2026-06-08: Collapsed the gating model to two `Alignment.Mode` values (`Interactive` default, `Autonomous`) and introduced `Alignment.Checkpoint` as the declared alignment-opportunity points a skill exposes. `Gated` and the `User.Gate.Policy` axis are superseded by checkpoints + mode; `Deviation.Policy` and `Reporting.Policy` remain separate skill axes. `Alignment.Mode` is one skill axis, not a global control model.
- 2026-06-08: Resolved the positional/conditional question — one `Alignment.Checkpoint` concept: a declared position optionally gated by an activation condition. Added discipline rules: the agent must not invent checkpoints and must not stop outside declared ones. Deviation is handled at a declared checkpoint via a condition, not an anywhere-interrupt.
- 2026-06-08: Decided topic 2 `Executable.Feedback.Loop`: a feedback loop is mandatory at both per-slice and per-Impl.Req altitudes; agent must construct a signal (scripts/partials) before falling back to manual inspection with explicit criteria. Signal ladder deferred to topic 5; "feedback loop named" routed to the `Readiness.Contract` (topic 3).
- 2026-06-08: Decided topic 3 as `Alignment.Checkpoint::Readiness` — a single named checkpoint right before the `Impl.Req` is written. A readiness checklist detects gaps; the agent resolves what it can and raises the rest as a final alignment pass (governed by `Alignment.Mode`). Deliberately light: a gap-detector and needs gate, not a documentation mandate. Establishes the `Alignment.Checkpoint:<Name>` convention. Open: whether the executer keeps a light entry readiness check.
- 2026-06-09: Mined academy / Pocock "Workflow for AI Coding". Captured `Test.First` (TDD at `Natural.Placement` — name behaviors at readiness, RED→GREEN per slice, ban all-tests-up-front to avoid imagined-shape tests), `Impl.Req.Lifecycle` (transient live-notes, resolves topic 7 doc-rot), and `Standards.Push.Pull` (implementer pulls, reviewer pushes). Dropped fresh-context review (user responsibility for now). Strong independent-convergence signal: grill-me≈design session, PRD≈Impl.Req, tracer-bullet slices≈topic 4, feedback-loops-as-quality-ceiling≈topic 2.
- 2026-06-09: Overlap check against the existing index test cluster (`Development.Principles` → `Vertical.Slice`, `No.Legacy.Allowed`, `No.Regression.Tests.Allowed`, `Test.At.Boundaries`). Found `Verification.Ladder` ~80% redundant (only baseline-ground-truth was new) — dropped. `Executable.Feedback.Loop` largely folds into `Test.At.Boundaries`. Renamed `Test.First` → `RED.GREEN.Test.Suite` and reconciled: not a conflict with `No.Regression.Tests.Allowed` — method (test-first) vs test-selection (no regression slop) are orthogonal. `RED.GREEN.Test.Suite` becomes a new `Impl.Exec` `Development.Principle`.
- 2026-06-09: Landed `Designer.Turn.Kernel.Form` and `RED.GREEN.Test.Suite` into the `agentos-pkg` index; wired `RED.GREEN.Test.Suite` into the designer/executer skills; updated the designer-skill `interview.md`/`discussion.md` for `Designer.Turn.Kernel.Form`. Cleaned this session: refreshed `Session.Abstract`, folded `Executable.Feedback.Loop` into `Test.At.Boundaries`, annotated the Decision Queue, resolved the `Alignment.Mode`-preset parking item, and updated the now-outdated "don't edit target skills" working rule.
