# Alignment.Loop:What — appendix

Extended depth for `Alignment.Loop:What`. The index block is in `106-index.md`.

## Loop Schema

```txt
        ╭───────────────── Alignment.Loop:What ──────────────────╮
        │                                                        │
        ▼                                                        │
  Alignment.Question:What        ◀─ Alignment.Maintenance.Turn   │
        │   agent asks ONE highest-leverage question  (agent drives)
        ▼                                                        │
  Alignment.Discussion:What      ◀─ Alignment.User.Turn          │
        │   discuss → convergence / parking / rejection (user drives)
        ▼                                                        │
  Alignment.Consolidation:What   ◀─ Alignment.Maintenance.Turn   │
        │   settle + capture (user-gated) → emits Design.Status.Report
        ╰────────────────────────▶ repeat ───────────────────────╯

   ⤷ Alignment.Loop.Interruptions — branch at ANY point, then return to flow:
       Capture.Audit · Consolidation.Plan · Artifact.Upgrade ·
       Impl.Req.Handoff · Session.Split · Close.Topic · Park.Topic

   turn switching is user-gated — the agent may suggest, never silently switch
```

Reading it: the agent drives the two `Alignment.Maintenance.Turn` ends (ask a question, consolidate); the user drives the `Alignment.Discussion:What` middle; consolidation captures state as a `Design.Status.Report`. `Alignment.Loop.Interruptions` are side-branches off any point that return to the cycle.
