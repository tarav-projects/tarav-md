# Implementation Capture Module

Load this module only for `Workflow:Capture` (`impl-capture`).

`impl-capture` banks the implementation work that is *ready now* and parks what still needs design. It scans the live conversation and the current implementation for touched, implementation-ready drift, ranks the candidates, proposes its best pick behind the standard `Alignment.Mode` gate, and hands the chosen one to `references/develop.md`.

> $kw: --from Touched.Authority --from Hugentic.Variable --from Agentic.Variable --from Impl.Req --from Open.Space --from Internal.Alignment --from Progress.Gradient --from Design.Implementation.CoEvolution --from Hard.Evidence --from We.Distrust.Summaries --from Touched.Surface.Index --from Chat.Grounding

## What It Is For

The Hugentic Harness leaves a mix at the end of a working session: some threads are decided and clear, others still carry open design questions. `impl-capture` is the "bank the ready work, park the rest" move — the implementation-side dual of a capture audit. It does not design; it *selects* what is ready to be developed and routes it through the normal design-and-execution workflow.

In harness terms it is an `Internal.Alignment` move: it advances the `Progress.Gradient` by syncing the implementation surfaces to the touched decisions the session already produced — the `Design.Implementation.CoEvolution` rhythm, applied one ready unit at a time.

## The Readiness Judgment

There is no a-priori set of gated variables. Readiness is a **ranking, not a classifier**:

- **touched** — the work rests on `Hard.Evidence`: decisions the user actually made in the conversation (`Touched.Authority`), the claims that survive into the `Touched.Surface.Index` — not an agent summary (`We.Distrust.Summaries`).
- **clear** — the implementation path is largely determined; what remains are `Agentic.Variable`s (implementation details the agent resolves), not open `Hugentic.Variable`s (axes still needing human convergence).
- **grounded drift** — the change is a concrete gap between a touched decision and the current implementation, not a speculative improvement.

An item where an open design question still sits is **not ready** — it is parked, becoming a design backlog. When uncertain whether a decision is still open, treat it as open: **bias toward parking.** The human gate, not a perfect judgment, is what keeps this safe.

## The Scan

Assemble candidates from the intersection of two sources:

- **the conversation** — the touched decisions, corrections, and requests the user made this session.
- **the current implementation** — the code, skills, index, and drift signals (e.g. `agentos skw check`, a drift audit) that show where those decisions are not yet reflected.

Each candidate is a coherent unit of implementation work with one observable result — the shape a single `Impl.Req` covers.

## Alignment.Checkpoint::Candidate

> $kw: --derived --from Alignment.Checkpoint --from Alignment.Mode
> --intent the selection gate: what the report shows and how each mode
> --cont resolves it — the human veto that absorbs ranking error

Before any implementation, run the candidate-selection checkpoint:

- **`Interactive`** (default) — render a short report and stop for the user:
  - the **best-ready candidate**, its observable result, and *why* it ranks highest (touched + clear + grounded);
  - the **parked** runners-up, each with the open question that defers it.

  The user approves the pick, redirects to another candidate, or reshapes it. The report is the value of the gate — it makes the approval informed and turns the parked set into a visible design backlog.
- **`Autonomous`** (`--auto`) — no stop: select the top-ranked candidate and proceed, recording the ranking and the parked set in the produced `Impl.Req`.

> $kw. end

## Delegation

Once a candidate is selected, hand it to `references/develop.md` as the resolved `Input`:

1. Load `references/develop.md`.
2. Run the full `Workflow:Develop` — design the `Impl.Req`, then execute it — under the same resolved `Alignment.Mode`.
3. The chosen candidate is develop's input; `impl-capture` adds no implementation logic of its own.

Only the *selection* is new; the design and execution are the existing harness workflow.

The candidate carries its **provenance**, not just its description. The touched decisions the ranking rested on become develop's grounding: its design phase seeds the `Impl.Agendix` from those surfaces through `Chat.Grounding` — anchors on the deciding turns — and execution carries that grounding onto the code. The chat → grounding → implementation chain starts at this scan; impl-capture hands develop the touched surfaces, not a re-summary of them.

## Boundary Contract

- `impl-capture` selects and routes; it never designs or edits directly.
- One candidate per run — a heterogeneous ready set is banked one coherent `Impl.Req` at a time; re-invoke for the next.
- The parked set is an output, not a loss — surface it so the deferred design work is recorded; unresolved candidates stay `Open.Space`, not silent drops.
- Preserve the resolved `Alignment.Mode` into the delegated develop workflow.

## Completion

Return one concise report:

- the selected candidate and why it was ready;
- the delegated `Impl.Req` path and implemented result (from develop);
- the parked candidates and their open questions — the design backlog.
