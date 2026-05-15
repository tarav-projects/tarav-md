# Alignment.Model

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
- see also `124-Development.Model.md` for `Design.Target.Model` as a point in this space

****

## Alignment.Hugentic.Axis

- `Alignment.Hugentic.Axis` is a dimension of the `Conceptual.Space` that needs human-agent convergence
- each workflow specialization defines its own set of axes
- the axes are the focus of the `Alignment.Loop`

****

## Alignment.Agentic.Axis

- `Alignment.Agentic.Axis` is a dimension the agent resolves autonomously without explicit human convergence

****

## Alignment.Loop

- `Alignment.Loop` is the general workflow machinery for human-agent convergence
- sequence: `Alignment.Question` → `Alignment.Discussion` → `Alignment.Consolidation`
- parameterized by phase: `Alignment.Loop:What` (design), `Alignment.Loop:How` (impl design), `Alignment.Loop:Exec` (impl execution, light)
- see `121-Design.Session.md` for `What.Design` specialization
- see `123-Impl.Req.md` for `How.Design` specialization

****

## Alignment.User.Turn

- `Alignment.User.Turn` is the turn mode where the user drives and the agent follows
- the agent follows the user's current thread, discusses one topic until convergence, parking, or rejection

****

## Alignment.Maintenance.Turn

- `Alignment.Maintenance.Turn` is the turn mode where the agent drives one session move
- ask next question, consolidate, report status, surface stale state, upgrade, close, split, or hand off
- mode switching is user-gated — the agent may suggest, never silently switch

****

## Alignment.Backend

- `Alignment.Backend` is where session state lives
- `Alignment.Backend:InChat` — state lives in chat, no file overhead
- `Alignment.Backend:Artifact` — state lives in a file-backed artifact, durable and handoff-ready
- parameterized by phase: `Alignment.Backend:InChat:What`, `Alignment.Backend:Artifact:What`, etc.

****

## Hard.Evidence

- `Hard.Evidence` is the principle that evidence-based arguments have priority over agent assumptions during alignment work
- concrete evidence: user instructions, inspected codebase state, active session artifacts, stable project surfaces
- alignment sessions aim to be `Hard.Evidence`-based — more is welcome, but the core alignment axes are the priority

****

## Alignment.Session

- `Alignment.Session` is a shallow container — when these concepts run together in a session, that's an Alignment.Session
- no behavioral protocol of its own — each workflow specialization defines its own `Alignment.Hugentic.Axes` and behavioral detail
- lists and relates the general concepts that compose an alignment session

### concepts

- `Conceptual.Space`, `Alignment.Hugentic.Axis`, `Alignment.Agentic.Axis`, `Alignment.Loop`, `Alignment.User.Turn`, `Alignment.Maintenance.Turn`, `Alignment.Backend`

### phase semantic roots

- `What.Design` — phase 1, working on the conceptual model
- `How.Design` — phase 2, planning the path
- `Impl.Exec` — phase 3, walking the path
