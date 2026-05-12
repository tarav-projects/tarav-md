# Design.Session

## Design.Session

- `Design.Session` is a scoped human-agent convergence surface for design work
- the session does real work (design, problem-solving, issue resolution) while progressively enriching alignment between user and agent
- the interview loop (`Design.Alignment.Question` → `Design.Enrichment.Discussion` → `Design.Consolidation`) is the fundamental strategy: direct questions produce evidence of alignment, consolidation makes it durable
- the agent maintains session progress and content; the user controls advancement and settles material
- session content aims to be `Hard.Evidence`-based as much as possible — evidence-based arguments have priority over agent assumptions
- the goal is to fill `Design.Alignment.Core` with evidence-based facts — more is welcome, but the core alignment space is the priority
- a staging area for `Stable.Surface` changes — session content is expected to become part of stable surfaces through implementation
- the move from design session state to stable surface is the implementation — can happen multiple ways: other agents read the artifact and implement in parallel, session emits `Impl.Req`s, direct surface updates from the session
- not a `Stable.Surface` itself — a strong signal for change that provides a clear substrate to align implementation against
- optimized for high-signal alignment data — can support operational work (migration, triage) when it produces alignment, but should not become a general-purpose work log
- does not replace index notes or skills — those are the destinations

****

## Session.Runtime.Loop

- `Session.Runtime.Loop` is the general workflow the agent tries to make the session follow
- main flow: `Design.Alignment.Question` → `Design.Enrichment.Discussion` → `Design.Consolidation` → ...
- interruptions are named branches that pause the main flow at any point
- `User.Assistant.Turn` — user drives, agent follows (`Design.Enrichment.Discussion` phase)
- `Session.Maintenance.Turn` — agent drives one session move (`Design.Alignment.Question`, `Design.Consolidation`, state update)
- mode switching is user-gated — agent may suggest, never silently switch
- `Design.Status.Report` — structured checkpoint that summarizes session state
    - delta-oriented: reactive to context, don't repeat still-valid reported state
    - serves multiple roles: status checkpoint, consolidation output, session state summary
    - works in both `InChat.Design.Session` and `Artifact.Design.Session`
    - used sparingly at natural consolidation points
    - in InChat sessions, `Design.Consolidation` = printing a `Design.Status.Report`
- `Session.Interruptions` — catalog of named branches the user can take:
    - `Capture.Audit`, `Consolidation.Plan`, `Artifact.Upgrade`, `Impl.Req.Handoff`, `Session.Split`, `Close.Topic`, `Park.Topic`
- the interruption catalog gives the user a vocabulary to communicate with the agent — each name triggers a known response shape
- after an interruption, return to the main flow unless the user chooses another move

****

## InChat.Design.Session

- `InChat.Design.Session` is the default `Design.Session` backend — state lives in chat
- the chat is the substrate, the agent organizes it into design-session form
- flexibility is the priority — no file overhead, no formal sections required every turn
- the agent must always track session state even when not printing it
- design state lives across explicit chat turns and strategic `Design.Status.Report` prints
- can't waste tokens on session organization overhead — the agent needs to actually work

****

## Artifact.Design.Session

- `Artifact.Design.Session` is the file-backed `Design.Session` backend — state lives in a `*-design-session.md` `Live.Note`
- durable, handoff-ready
- adds `Session.Notes` and `Session.Log` to `Session.Abstract` and `Design.Index`
- artifact writes are user-gated
- upgrade path: InChat → Artifact when state becomes too large, important, or needs future handoff — upgrade is user-gated, never automatic
- both backends run the same `Session.Runtime.Loop` — the backend doesn't change the workflow, only where consolidated state is captured
