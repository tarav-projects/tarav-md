# Wiki-backed implementation

Use this module by default for new implementation requests, for explicit
`--impl --wiki`, and for resuming a Wiki-backed Impl.Req.
This is an agent-operated implementation route, not a new Python runner.

## Surface and phase selection

`--wiki` selects the knowledge surface, not a phase or permission to execute.
It is optional: Wiki is the only active knowledge surface, and the Model-backed
route with its `--model` selector is parked. Defaults never migrate a note.
Keep existing shortcuts: `--design`, `--review`, `--execute`/`--exec`,
`--develop`/`--dev`, and `--harvest`. Explicit phase wins. Otherwise an
existing Impl.Req defaults to Execute; new actionable input defaults to Design.
Develop, Review, and Harvest require explicit selection. With no actionable
input, orient and stop. `--auto`/`--autonomous` selects autonomous alignment,
not broader execution authority.

Record `Knowledge.Surface: wiki` in the live note. A legacy note carrying
Impl.Req.Diagram belongs to the parked Model-backed route; report that and ask
before any mutation. Ask as well when a note has conflicting surface
declarations. Do not infer a migration or create replacement artifacts.

Print a compact banner with phase, Wiki surface, input, and Alignment.Mode.
Read [`code-engineering.md`](code-engineering.md) for every code-facing phase,
[`../commit-evidence.md`](../commit-evidence.md) for scoped repository bracketing, and [`../inline-capture.md`](../inline-capture.md) for
Product.Surface Breadcrumb capture.
No Model, Collection, Diagram View, Diagram Draft, authorization Gate, or
Model capture reconciliation is required or created by this route.

## Context and request

Resolve the product project and its instructions. Resolve documentation
ownership separately when project guidance assigns the Wiki elsewhere.
Use Project.from_path(path).docs.wiki from tarav.l2.project, or an explicitly
selected folder Wiki. For a minimal TaravProject, use
ProjectWiki(project).open() from tarav.l2.project.wiki.
Read relevant Wiki notes and follow evidence links as needed; do not read or
reconcile the entire Wiki. An absent Wiki is not a reason to bootstrap Models.
For read-only review, report missing context without creating anything.

Name new implementation-request live notes
`<number>-<descriptive-name>-impl-req.md` under the product's notes/live/.
Follow its numbering convention; preserve existing filenames on resume.
When one design changes several repositories, write one request per owning
repository, each in its own notes/live/, cross-referenced and executed in
dependency order; each repository keeps its own scoped evidence commits.

The live-note Impl.Req remains coordination outside notes/wiki/ and contains:

- Impl.Abstract: requested result, scope, explicit non-goals and status.
- Knowledge.Surface: wiki.
- Design narrative: requested behavior, rationale, relevant current behavior,
  decisions, constraints, informative alternatives, and open questions, with
  supporting Breadcrumbs beside the passages they contextualize.
- Impl.Req.Wiki: product project, Wiki owner/root, relevant note paths,
  available supporting chat references, and capture status.
- Execution.Plan: the core data shape and ordered vertical slices, each with
  its work kind, observable result, check, and status.
- Impl.Log: decisions, changes, checks, blockers, and capture outcomes.

Do not invent evidence or turn an agent plan into user-approved design.
Record user decisions, implementation observations, and proposals distinctly.
Do not copy the whole plan into the Wiki.

The Impl.Req must be sufficiently self-contained for another agent in another
session to understand and implement the request. Wiki links remain useful for
broader context and detail, but must not replace the explanation of what is
requested and why. Carry the necessary bounded narrative and evidence in the
note itself; neither copy the entire discussion nor require its reconstruction.

During Design, attach exact supporting Chatlas User Turns as Breadcrumbs in
the live note, even when the same turns also support Wiki passages. Apply the
shared Inlined Capture workflow to that Markdown surface; the Impl.Req is an
authorized Design output, not an implementation edit. Log evidence gaps rather
than fabricate support. On later execution,
preserve the original sessions and turns; a new session's invocation does not
replace design evidence. Add later clarifications and observations distinctly.

## Phases

Keep designer and executer responsibilities distinct even when one Agent
performs both.

**Design:** inspect Wiki context and current code, shape the change and plan
its vertical slices under the code-engineering module, formulate the live
note, and resolve material ambiguities interactively. Do not implement product
code. Before handoff, confirm the code-engineering readiness conditions and
that the note is understandable without the design chat; close gaps yourself
where possible. Capture supported discussion under the capture contract below,
then hand off the note with ready, needs-alignment, or blocked status.

**Review:** require an existing note. Cold-read it completely before opening
cited files, and record first-pass confusion as evidence of what a fresh
executer will meet. Inspect the referenced Wiki and code. Grade each
load-bearing claim about files, symbols, commands, tests, and behavior as
verified, stale, or unverifiable, sampling in proportion to risk. Rerun the
code-engineering readiness conditions from a cold executer's view, including
whether the note carries enough design context for a cross-session handoff.
Lead the report with ready, ready-with-notes, or not-ready, then give
severity-ranked findings that cite the evidence checked. Do not reopen the
accepted design as a general preference review. Use non-mutating inspection
only: no note edits, capture, Chatlas refresh, commits, or product mutation.

**Execute:** cold-read the existing note and current instructions before edits.
Explicit Execute with direct input first creates the Wiki-backed live note;
it does not bootstrap Diagram artifacts. Recheck the plan against current code
and restate the implementation in design-level prose.
Before the first product edit, use the shared evidence-commit workflow to
checkpoint only the declared work scope in each repository; an empty scoped
checkpoint is valid. Stop for conflicts or an impossible checkpoint.
Run each slice through the code-engineering slice loop. At the end of every
slice, apply the shared Inlined Capture workflow to each Product.Surface
actually implemented by that slice, then record slice status, checks, and
outcomes in the live note. A slice whose product verification fails is not
presented as complete; a capture failure does not invalidate verified product
work. Never silently adapt to a design-reality mismatch: Interactive mode
describes it with viable adjustments and waits; Autonomous mode records the
deviation in Impl.Log, takes the most faithful available path, and still
cannot expand authorization. Finish with verification, the code-engineering
evidence report, the scoped evidence completion commit, and selective Wiki
capture. Develop and Harvest inherit this requirement through their Execute
phase; no extra capture flag is needed.

**Develop:** Design, then cold-reload the resulting live note and Execute.
Preserve surface, alignment mode, scope, and evidence across the boundary.

**Harvest:** inspect the discussion and relevant Wiki, select one coherent
implementation unit, and present the choice in Interactive mode. Then Develop
that unit. Keep other candidates separate; do not silently implement them.

`--impact` is optional input assessment: compare the current discussion and
Wiki design against code, separating aligned behavior from actionable deltas.
Feed that delta to the selected phase. It does not select Execute, authorize
writes in Review, or load the standalone Design Impact module.
`--impl --wiki --capture` selects Wiki capture within the chosen mutating phase;
it is not another phase. Review remains read-only even when capture is requested.

## Product.Surface Inlined Capture

Use the shared Inlined Capture workflow as the single Product.Surface Breadcrumb
path. At the end of each Execute slice, run its complete capture path separately
on every code,
test, configuration, or documentation surface actually implemented by that
slice. Wiki or Impl.Req references do not substitute for this step. Stay within
the implemented scope; do not annotate every declaration or manufacture support.
Design captures the live-note surface only, and Review remains read-only.

Reuse exact session resolution across Impl.Req, product, and Wiki capture within
a pass. For generated files, capture on the authoritative source and rebuild.
After Inlined Capture replaces provisional markers, rerun affected syntax or
build checks and record files, Breadcrumb IDs, audits, and gaps in Impl.Log. If
no position has justified support, record that outcome without inventing
annotations. If mechanics fail, preserve the product and report the pending
capture separately; do not claim capture completed. Product commit authority
remains bounded by the shared evidence-commit scope.

If submission cannot register, typically because a sandbox prevents writing
to the Tarav data folder, leave the read-only trace. Keep the provisional
`tarav.context` markers where they are and keep their session resolvable.
Do not remove the markers or invent Breadcrumb labels, and report the
registration as pending, not as done. A later session that can write runs the
same `submit` and `audit` commands on the surface; nothing has to be guessed
while the declaration is intact.

## Wiki capture and closure

For mutating phases, compose [`../wiki-capture.md`](../wiki-capture.md) for one bounded capture pass at
handoff/completion; intermediate agent coordination stays in the live note.
The implementation invocation authorizes this scoped pass. Reuse its
Project.Wiki selection, mandatory daily narrative, useful topical integration,
Chatlas User-Turn grounding, Breadcrumb submission/audit, and scoped Wiki Git closure.
The product and Wiki evidence commits keep separate declared file scopes.

Capture relevant user decisions and discussion selectively. Implementation facts
must also cite inspected code or test evidence; user authorization is not proof
that code works. Keep unsupported agent interpretation and raw execution logs
in the live note. Preserve alternatives rather than force a canonical design.
Do not regenerate existing Wiki content merely to make it match the plan.

If Chatlas, Breadcrumb, or Wiki closure mechanics are unavailable, preserve
verified product work and log the precise capture gap for recovery. Do not
fabricate support or claim capture completed. Missing Model artifacts are not
a gap for this route. Review never runs this mutating capture procedure.
When the gap is Breadcrumb registration, the read-only trace above is the
recoverable form of that gap.

Completion reports the live note, implemented outcome, checks, Wiki daily and
topical destinations, Product.Surface Breadcrumb results, scoped capture commit
if any, and unresolved gaps.
A verified implementation with pending Wiki capture must report both statuses.
