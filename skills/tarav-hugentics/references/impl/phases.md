# Implementation Phases

Use this module for the phase selected by the implementation router. Read
[`request.md`](request.md) for the live-note Impl.Req,
[`code-engineering.md`](code-engineering.md) for every code-facing phase, the
active context backend [`context/wiki.md`](context/wiki.md),
[`../commit-evidence.md`](../commit-evidence.md) for repository commits, and
[`../inline-capture.md`](../inline-capture.md) for Product.Surface Breadcrumb
capture.

The phases read context from the backend and capture back to it; they do not
depend on which backend that is. Keep designer and executer responsibilities
distinct even when one Agent performs both.

## Design

Inspect the backend's context and current code, shape the change and plan its
vertical slices under the code-engineering module, formulate the live note,
and resolve material ambiguities interactively. Do not implement product code.
Before handoff, confirm the code-engineering readiness conditions and that the
note is understandable without the design chat; close gaps yourself where
possible. Capture supported discussion through the backend, then hand off the
note with ready, needs-alignment, or blocked status.

## Review

Require an existing note. Cold-read it completely before opening cited files,
and record first-pass confusion as evidence of what a fresh executer will
meet. Inspect the referenced backend context and code. Grade each load-bearing
claim about files, symbols, commands, tests, and behavior as verified, stale,
or unverifiable, sampling in proportion to risk. Rerun the code-engineering
readiness conditions from a cold executer's view, including whether the note
carries enough design context for a cross-session handoff. Lead the report
with ready, ready-with-notes, or not-ready, then give severity-ranked findings
that cite the evidence checked. Do not reopen the accepted design as a general
preference review. Use non-mutating inspection only: no note edits, capture,
Chatlas refresh, commits, or product mutation.

## Execute

Cold-read the existing note and current instructions before edits. Explicit
Execute with direct input first creates the live note; it does not bootstrap
Diagram artifacts. Recheck the plan against current code and restate the
implementation in design-level prose.

Before the first product edit, make the shared evidence-commit start
checkpoint in each repository, external work and this note included, empty
when the repository is clean, and record its hash in Impl.Log. Record
`skip: <reason>` only for the Git states that rule allows.

Run each slice through the code-engineering slice loop. At the end of every
slice, apply the shared Inlined Capture workflow to each Product.Surface
actually implemented by that slice, record slice status, checks, and outcomes
in the live note, and make the evidence-commit slice commit, committing stale
external work first when that rule applies. A slice whose product verification
fails is not presented as complete; a capture failure does not invalidate
verified product work.

Never silently adapt to a design-reality mismatch: Interactive mode describes
it with viable adjustments and waits; Autonomous mode records the deviation in
Impl.Log, takes the most faithful available path, and still cannot expand
authorization.

Finish with verification, the code-engineering evidence report, the
evidence-commit completion commit, and the backend's capture pass. Develop and
Harvest inherit this requirement through their Execute phase; no extra capture
flag is needed.

## Develop and Harvest

**Develop:** Design, then cold-reload the resulting live note and Execute.
Preserve backend, alignment mode, scope, and evidence across the boundary.

**Harvest:** inspect the discussion and relevant backend context, select one
coherent implementation unit, and present the choice in Interactive mode. Then
Develop that unit. Keep other candidates separate; do not silently implement
them.

## Impact and capture selectors

`--impact` is optional input assessment: compare the current discussion and
the backend's design context against code, separating aligned behavior from
actionable deltas. Feed that delta to the selected phase. It does not select
Execute, authorize writes in Review, or load the standalone Design Impact
module.

`--impl --capture` selects the backend's capture within the chosen mutating
phase; it is not another phase. Review remains read-only even when capture is
requested.

## Product.Surface Inlined Capture

Use the shared Inlined Capture workflow as the single Product.Surface
Breadcrumb path. At the end of each Execute slice, run its complete capture
path separately on every code, test, configuration, or documentation surface
actually implemented by that slice. Backend or Impl.Req references do not
substitute for this step. Stay within the implemented scope; do not annotate
every declaration or manufacture support. Design captures the live-note
surface only, and Review remains read-only.

Reuse exact session resolution across Impl.Req, product, and backend capture
within a pass. For generated files, capture on the authoritative source and
rebuild. After Inlined Capture replaces provisional markers, rerun affected
syntax or build checks and record files, Breadcrumb IDs, audits, and gaps in
Impl.Log. If no position has justified support, record that outcome without
inventing annotations. If mechanics fail, preserve the product and report the
pending capture separately; do not claim capture completed. Product commit
authority remains bounded by the shared evidence-commit scope.

If submission cannot register, typically because a sandbox prevents writing
to the Tarav data folder, leave the read-only trace. Keep the provisional
`tarav.context` markers where they are and keep their session resolvable.
Do not remove the markers or invent Breadcrumb labels, and report the
registration as pending, not as done. A later session that can write runs the
same `submit` and `audit` commands on the surface; nothing has to be guessed
while the declaration is intact.

## Completion

Completion reports the live note, implemented outcome, checks, Product.Surface
Breadcrumb results, commits, the backend's capture destinations, and
unresolved gaps. A verified implementation with pending backend capture must
report both statuses.

