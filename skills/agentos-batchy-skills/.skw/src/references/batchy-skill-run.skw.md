# Batchy Skills — Running One

How to *operate* a `Batchy.Skill`. This is the runner-facing convention — what you need to correctly invoke a skill. For building one, see `batchy-skill-designer.md`. Skill concepts are canonical in `agentos-pkg/design/101-design.md`; routing concepts are canonical in `agentos-pkg/design/107-design.md`.

Every Agentos skill is a `Batchy.Skill` — called like a terminal command and resolved by one `Batchy.Router`. The convention is agent-interpreted rather than a Bash parser: explicit flags are the crisp configuration path, while clear natural-language calls remain valid wherever the applicable rows permit automatic discovery.

## The Call

- A skill is invoked like a CLI command: a name, optional flags, optional a value or two.
- `-h` / `--help` is universal and always available, even on a skill that takes no arguments.
- A written `--<flag>` is intentional run configuration and must be resolved as such.
- Flags may carry values (`--project "stripe-pkg"`) or act as switches (`--AUTO`), according to their configured row.
- Only the `--<flag>` form carries explicit flag semantics. Bare prose may contribute conversational discovery, but it is not silently treated as a flag.

## `-h` / `--help` (always)

- Short-circuits the skill: print the help into the chat and stop. `-h` wins over any other supplied flags.
- It is a deliberate help *output to the user* — distinct from silently loading the skill to orient the agent.
- The help leads with one paragraph on what the skill is and does, then callable usage assembled from reachable argument, module, and routing-table configuration. A skill with no custom run configuration says so.

## The Run Banner (when it has custom configuration)

- On a real run (anything but `-h`), the first step is to print a `Batchy.Skill.Banner`: a short echo of how the flags resolved.
- It shows each supplied flag with its resolved effect: argument binding, module selection, or contributed routing context.
- It distinguishes caller-supplied configuration, semantically discovered configuration, and filled defaults; resolved argument values use their canonical `Skill.Arg` names.
- Informational, not a checkpoint — it prints, it does not ask — and it runs even under `Alignment.Mode::Autonomous`. A zero-argument skill has no banner.

```text
$my-skill — banner
  --project        → Skill.Arg::Target.Project = stripe-pkg
  --scan           → Skill.Module::Scan
  Alignment.Mode   = Autonomous                    (from --AUTO)
```

## Batchy.Router Resolution

`Batchy.Router` resolves one run from three input classes:

1. explicit `Batchy.Skill.Flag`s;
2. the live conversation, for rows permitting automatic discovery;
3. declared defaults.

Each `Batchy.Router.Row` determines the accepted inputs and one destination. A resolved route may:

- bind external data to a canonical `Skill.Arg` and validate its contract;
- select and load a `Skill.Module`;
- contribute or continue routing through a `Routing.Table`.

Explicit configuration takes precedence over inferred or default configuration for the same route. Exact keys, aliases, and semantic keyword families apply only when the row declares them. A bare value may bind an argument only when a positional or conversational extraction path is configured. Missing required arguments follow `Skill.Explicit.Args`: ask or orient, never guess; declared defaults fill silently.

## Activating a Module

- A `Skill.Module` is a named, on-demand-loadable part of the skill — a file or section. Mentioning it (e.g. `--examples`, `examples`) loads it into context.
- An explicit flag, conversationally discovered row, or another `Routing.Table` may select it directly; module selection does not require a `Skill.Arg`.
- Load only the modules the current call needs — progressive disclosure keeps context lean.

## User Commands During A Workflow

- Read the active skill's `User.Command.Section` as the authoritative command inventory.
- A `User.Command` is an explicit `::<command line>` inside a user turn; it may appear anywhere in that turn.
- Resolve the written `User.Command.Trigger` to the canonical command declared by the active skill. Equivalent triggers execute the same action and carry no trigger-specific meaning.
- Treat quoted examples and discussion about command syntax as ordinary conversation unless the user's intent to invoke the command is clear.
- Execute only when the command is available at the foreground workflow checkpoint and every required `User.Command.Arg` resolves under its declared policy.
- An `Explicit` argument must be present in the command turn. A `Contextual` argument may come from the conversation or foreground workflow only when unique. A `Defaulted` argument uses its declared default.
- If the target, availability, or a required argument is ambiguous, ask for the missing input and do not advance any workflow.
- Natural conversation may interrupt or reshape the workflow, but it does not cross an unresolved explicit command gate. If the underlying proposal changes, invalidate any approval that no longer addresses its current form.
- Print the commands currently available when the workflow pauses or when status is requested, not after ordinary conversational turns.

> $kw: --from Batchy.Router
> $kw: --from Batchy.Router.Row
> $kw: --from Batchy.Skill
> $kw: --from Batchy.Skill.Banner
> $kw: --from Batchy.Skill.Flag
> $kw: --from Routing.Table
> $kw: --from Skill.Arg
> $kw: --from Skill.Explicit.Args
> $kw: --from Skill.Module
> $kw: --from User.Command
> $kw: --from User.Command.Arg
> $kw: --from User.Command.Section
> $kw: --from User.Command.Trigger
