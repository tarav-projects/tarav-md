# Alignment.Session.Knowledge.Module

> $kw: --dev-from references/index-context-assembly.skw.md

`Alignment.Session` is a shallow container for the general concepts that compose an alignment session. No behavioral protocol of its own — each workflow specialization defines its own axes and behavioral detail.

## Concepts

> $kw: --derived --from Alignment.Session --from Design.Space --from QA.Space --from Design.Variable --from Hugentic.Variable --from Touched.Space --from Agentic.Variable --from Open.Space --from Alignment.Loop --from Alignment.Checkpoint --from Alignment.Mode
> --intent the session vocabulary as one-line recalls with aliases;
> --cont shallow-container framing, no behavioral protocol at this level

- **Design.Space** — a `QA.Space` about artifact design: a vector space of `Design.Variable`s, each variable one axis
- **Hugentic.Variable** — a `Design.Variable` that needs human-agent convergence, collapsed inside the `Touched.Space` (alias `Touched.Variable`)
- **Agentic.Variable** — a `Design.Variable` the agent resolves autonomously; the variable form of `Open.Space`, provisional until touched (alias `Open.Variable`)
- **Alignment.Loop** — the machinery: `Alignment.Question` → `Alignment.Discussion` → `Alignment.Consolidation`; parameterized by workflow phase (`:What`, `:How`, `:Exec`)
- **Alignment.User.Turn** — user drives, agent follows
- **Alignment.Maintenance.Turn** — agent drives one session move
- **Alignment.Checkpoint** — a declared point in a workflow where the agent checks something; an alignment opportunity gated by `Alignment.Mode`
- **Alignment.Mode** — the caller argument setting who resolves each `Alignment.Checkpoint`: `Interactive` (default) or `Autonomous` (see below)

> $kw. end

## Alignment.Checkpoint and Alignment.Mode

> $kw: --derived --from Alignment.Checkpoint --from Alignment.Mode
> --intent the operational copy (Cited.Duplication): full checkpoint
> --cont definition, mode table, declaration discipline, deviation contract,
> --cont and boundary-gated autonomy

Both concepts are defined in the index (`Cited.Duplication`); this is the operational copy.

An **`Alignment.Checkpoint`** is a declared point in a skill workflow where the agent checks something before proceeding. It is a checkpoint because it *can* be an alignment opportunity — a place a human could meaningfully weigh in; a decision the agent always resolves alone is not a checkpoint, just a normal step. A checkpoint may carry an activation condition deciding whether it fires when reached (e.g. "design did not fit reality").

**`Alignment.Mode`** decides *who resolves* each declared checkpoint:

| Mode | Behavior | Use |
|---|---|---|
| `Alignment.Mode::Interactive` | At each declared checkpoint, the agent may prompt the user. | Default. Human in the chair. |
| `Alignment.Mode::Autonomous` | No prompting; the agent resolves every checkpoint itself. | End-to-end autonomous flows (cleanup, scheduled runs). |

When unspecified, default to `Interactive`. The mode is one skill axis, not a global control model — a skill may carry other axes.

**Discipline:** checkpoints are declared explicitly, so a skill's alignment surface is inspectable up front. The agent must not invent checkpoints and must not stop outside a declared one — no ad-hoc halts.

**Deviation contract** (deviation = design-reality mismatch, handled as a declared checkpoint with a "design did not fit reality" condition):

- `Interactive` — stop at the checkpoint and surface the mismatch to the user.
- `Autonomous` — record the deviation and continue with the most faithful corrective action; abort only on hard failure.

**Boundary-gated autonomy:** a caller wanting autonomous execution within a phase with a single confirmation at the artifact boundary owns that boundary as its own declared `Alignment.Checkpoint` and invokes downstream skills in `Alignment.Mode::Autonomous`.

> $kw. end

## Phase Semantic Roots

| Phase | Name | Description |
|---|---|---|
| 1 | `What.Design` | Working on the conceptual model |
| 2 | `How.Design` | Planning the path |
| 3 | `Impl.Exec` | Walking the path |

## Workflow Parameterization

> $kw: ^loop-params --derived --from Alignment.Loop
> --intent the phase parameterization spelled out for loop components;
> --cont storage and target selection belong to the owning workflow

The `Alignment.Loop` and its components are parameterized by phase:

- `Alignment.Loop::What` / `Alignment.Question::What` / `Alignment.Discussion::What` / `Alignment.Consolidation::What`
- `Alignment.Loop::How` / `Alignment.Question::How` / `Alignment.Discussion::How` / `Alignment.Consolidation::How`
- `Alignment.Loop::Exec` / `Alignment.Question::Exec` / `Alignment.Discussion::Exec` / `Alignment.Consolidation::Exec`

> $kw. end

> $kw: --from Cited.Duplication --from Open.Variable --from Touched.Variable
