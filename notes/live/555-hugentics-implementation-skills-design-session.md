# Hugentics Implementation Skills - design-session

## Session.Abstract

- intent: walk through the mined improvement proposal for `hugentics-impl-designer`, `hugentics-impl-executer`, and `hugentics-codebase-cleaner`, making explicit design decisions about each proposal area
- active focus: decide the shared contract that should connect cleanup candidate selection, `Impl.Req` design, and implementation execution
- references: [554-hugentics-implementation-skills-mining-report.md](554-hugentics-implementation-skills-mining-report.md)
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

### Execution.Policy

- `Execution.Policy` is runtime control for how autonomously an `Impl.Req.Execution.Contract` is walked
- it is separate from the execution contract: the contract describes what must be known, while policy describes how much user gating and reporting occurs during execution
- user checkpoints are tunable skill arguments, not fixed artifact structure
- the system should support a range from fully autonomous execution to checkpoint-driven execution
- avoid naming these runtime gates simply "checkpoints" because `Git.Checkpoint` already names the pre-execution rollback floor
- candidate gate policy values: `none`, `phase`, `slice`, and `custom`

#### appendix

- proposed conceptual split:

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

Execution.Policy
├── User.Gate.Policy
├── Deviation.Policy
└── Reporting.Policy
```

#### meta

- status: partially converged
- open question: should `Alignment.Mode` remain the public high-level preset with granular policy overrides, or should granular policies replace it entirely?

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
