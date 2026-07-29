# agentos-hugentics --design

Use this workflow module when the caller explicitly requests design or organic design work begins.

`--design` is the index-owned entry for a `Product.Design.Session`. The session advances a named `Target.Product`, exposes only unresolved What/How/Exec concerns, and applies `Touched.Decision.Cycle` inside every decision.

`What.Design.Session` remains the compatibility name for this design workflow; it does not define a separate owner or state model.

`Alignment.Mode` controls declared checkpoints, while `Alignment.Backend` selects in-chat or artifact-backed session state.

## Setup

Before the first design move:

1. Name the target product and current design concern.
2. Load `references/touched-data.md` and `references/decision-cycle.md`.
3. Run routing-first concept discovery over the owning touched index.
4. Load the relevant blocks, appendix depth, live agendix leads, and original support when needed.
5. Classify conflicts and missing design coverage as POIs rather than silently choosing one position.
6. Select the in-chat backend by default or the artifact backend when `--artifact` is explicit.

## Design Loop

- work one unresolved design question at a time
- write design state in `Design.Block` / `Kernel.Writing` form rather than free prose when a concept has stabilized enough to name
- let applicable touched constraints bound the answer and use open inference for the remaining design space
- reconcile each material decision against the target product and neighboring surfaces
- reopen an earlier concern when later evidence exposes a gap
- do not assume every session needs explicit What, How, and Exec stages

Design discussion itself is a qualifying authority-surface source only through the user turns that the current chat protocol recognizes as touched.

## Landing Boundary

- in-chat design state is not automatically an index edition
- artifact-backed session writes follow their artifact gate
- ontology, appendix, and agendix changes route through `--capture` or `--edit`
- implementation-ready handoff routes to `references/impl.md`

## Detailed Module Routing

Load only the detailed design modules needed for the current move:

- always load `references/design/writing-craft.md`, `references/design/index-view.md`, `references/design/design-anti-patterns.md`, `references/design/alignment-loop.md`, `references/design/interview.md`, and `references/design/discussion.md`
- concept discovery and setup → `references/design/concept-discovery.md`
- in-chat backend → `references/design/backend-inchat.md`
- artifact backend → `references/design/backend-artifact.md` plus `references/design/artifact.md`
- session state sections → `references/design/session-abstract.md`, `references/design/design-index.md`, `references/design/session-notes.md`, and `references/design/session-log.md`
- interruptions and consolidation → `references/design/session-interruptions.md`, `references/design/consolidation-plan-example.md`, and `references/design/uncommitted-work.md`
- status or capture audit → `references/design/status-report.md` or `references/design/capture-audit.md`
- implementation handoff → `references/design/impl-req.md`

These files are the canonical detailed implementation of `agentos-hugentics --design`.
