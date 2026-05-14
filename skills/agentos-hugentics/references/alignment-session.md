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
