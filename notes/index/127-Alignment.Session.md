# Alignment.Session

## Alignment.Session

- `Alignment.Session` is a shallow container — when these concepts run together in a session, that's an Alignment.Session
- no behavioral protocol of its own — each workflow specialization defines its own `Alignment.Hugentic.Axes` and behavioral detail
- lists and relates the general concepts that compose an alignment session

### concepts

- `Conceptual.Space` — the abstract space where alignment occurs; the set of all possible design decisions (`Alignment.Space` is a synonym)
- `Alignment.Hugentic.Axis` — a dimension that needs human-agent convergence; each workflow defines its own set
- `Alignment.Agentic.Axis` — a dimension the agent resolves autonomously
- `Alignment.Loop` — the machinery: `Alignment.Question` → `Alignment.Discussion` → `Alignment.Consolidation`; parameterized by workflow phase (`:What`, `:How`, `:Exec`)
- `Alignment.User.Turn` — user drives, agent follows
- `Alignment.Maintenance.Turn` — agent drives one session move
- `Alignment.Backend` — where session state lives: `InChat` or `Artifact`

### phase semantic roots

- `What.Design` — phase 1, working on the conceptual model
- `How.Design` — phase 2, planning the path
- `Impl.Exec` — phase 3, walking the path

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
