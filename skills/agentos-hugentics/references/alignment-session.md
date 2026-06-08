# Alignment.Session — Reference

`Alignment.Session` is a shallow container for the general concepts that compose an alignment session. No behavioral protocol of its own — each workflow specialization defines its own axes and behavioral detail.

## Concepts

- **Conceptual.Space** — the abstract space where alignment occurs; the set of all possible design decisions (`Alignment.Space` is a synonym)
- **Alignment.Hugentic.Axis** — a dimension that needs human-agent convergence; each workflow defines its own set
- **Alignment.Agentic.Axis** — a dimension the agent resolves autonomously
- **Alignment.Loop** — the machinery: `Alignment.Question` → `Alignment.Discussion` → `Alignment.Consolidation`; parameterized by workflow phase (`:What`, `:How`, `:Exec`)
- **Alignment.User.Turn** — user drives, agent follows
- **Alignment.Maintenance.Turn** — agent drives one session move
- **Alignment.Backend** — where session state lives: `InChat` or `Artifact`
- **Alignment.Mode** — how much human gating the loop carries; set by the caller, respected by the workflow (see below)

## Alignment.Mode

`Alignment.Mode` tunes the amount of human-in-the-loop gating a hugentic skill applies. One concept, three values, applied uniformly across phases.

| Mode | Gates | Use |
|---|---|---|
| `Alignment.Mode:Interactive` | Full loop. Every `Alignment.Question` / `Consolidation` confirmed with the user. | Default. Human in the chair. |
| `Alignment.Mode:Gated` | Autonomous within each phase. One confirmation at phase boundaries (e.g. `What.Design` → `Impl.Req` → `Impl.Exec`). | Mostly-autonomous flows that still want a sanity gate at the artifact handoff. |
| `Alignment.Mode:Autonomous` | No gates. Artifacts still produced as the audit trail. | End-to-end autonomous flows (e.g. cleanup, scheduled runs). |

The mode is selected by the caller or outer skill. When unspecified, default to `Alignment.Mode:Interactive`. Each workflow master spells out what the mode means for its loop and, importantly, for its **deviation contract**:

- `Interactive` — stop and ask the user.
- `Gated` — log the deviation; continue if reversible; abort if not.
- `Autonomous` — log and continue; abort only on hard failure.

A skill that does not name an `Alignment.Mode` is assumed `Interactive`.

## Phase Semantic Roots

| Phase | Name | Description |
|---|---|---|
| 1 | `What.Design` | Working on the conceptual model |
| 2 | `How.Design` | Planning the path |
| 3 | `Impl.Exec` | Walking the path |

## Workflow Parameterization

The `Alignment.Loop` and its components are parameterized by phase:

- `Alignment.Loop:What` / `Alignment.Question:What` / `Alignment.Discussion:What` / `Alignment.Consolidation:What`
- `Alignment.Loop:How` / `Alignment.Question:How` / `Alignment.Discussion:How` / `Alignment.Consolidation:How`
- `Alignment.Loop:Exec` / `Alignment.Question:Exec` / `Alignment.Discussion:Exec` / `Alignment.Consolidation:Exec`

Similarly for backends: `Alignment.Backend:InChat:What`, `Alignment.Backend:Artifact:What`, etc.
