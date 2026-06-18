# Batchy Skills — Authoring Guide

How to build a `Batchy.Skill`: a skill interpreted as a CLI-style command. The concepts are canonical in `agentos-pkg/index/101-index.md` (`Batchy.Skill`, `Batchy.Skill.Template`, `Batchy.Skill.Contract`, `Skill.Arg`, `Skill.Arg.Section`, `Batchy.Skill.Help`, `Batchy.Skill.Banner`, `Batchy.SubCommand`). This is the author-facing depth.

The Batchy framework is a convention the agent knows, not a parser. The agent stays smart: clear natural prompts still work, and named flags are the crisp path that matters most as parameter count grows.

## The Model

- A skill that takes arguments is a `Batchy.Skill`.
- Arguments are passed as bash-like flags — **valued** (`--project "BlaBla"`) or **switch** (`--AUTO`).
- Each argument is a `Skill.Arg` block with a canonical name used unambiguously in the skill body.
- The loose flag the user types maps to that canonical name; the agent resolves synonyms, abbreviations, and positionals (`--proj` ≈ `--project`).
- Switch values use `Dotted.Parameterized.Notation`: `--AUTO` → `Alignment.Mode:Autonomous`.

**Write tokens `--flag`-style.** Both arguments and `Batchy.SubCommand`s are written with the `--` prefix by preference — `--run`, `--project`, `--AUTO` — even when describing a call in prose. The `--` makes the token legible as a command inside natural text (`do a --run on stripe-pkg` reads as an invocation, `do a run on stripe-pkg` does not). This is a writing preference, not a parser rule: the agent still resolves bare and loose forms (`run`, `RUN`, a positional package name) to the canonical name.

## The Skill Template

Every Batchy skill instantiates one `Batchy.Skill.Template` — the same skeleton — so all Agentos skills share a shape. Lay the skill body out in this order:

1. a one-paragraph description of what the skill is and does;
2. a `Batchy.Skill.Contract` block — the in-skill mini-course (below);
3. a `## Skill.Arg.Section` holding one `### Skill.Arg:<Name>` block per argument;
4. optional `## SubCommands` listing the skill's `Batchy.SubCommand`s.

The frontmatter `description` carries a `Skill.Trigger.Clause` (a `USE WHEN` line) so an agent knows when to load the skill.

## The Batchy.Skill.Contract Block

Carry a `Batchy.Skill.Contract` near the top of the skill body: a compact mini-course that restates the convention so the skill complies even when `agentos-skills-base` is not loaded. It is a `Cited.Duplication` — duplicate the few must-do behaviors, cite the base skill for depth. Paste a block like:

```markdown
This is a `Batchy.Skill` — called like a terminal command. Load `agentos-skills-base`
for the full convention.

- `-h` / `--help` prints usage and exits without running (`Batchy.Skill.Help`).
- every run prints a banner of the resolved arguments as its first step (`Batchy.Skill.Banner`).
- supplied flags resolve to the `Skill.Arg` names below; loose and positional forms resolve too.
```

## Skill.Arg.Section

Declare arguments in a `Skill.Arg.Section` — the `## Skill.Arg.Section` section of the skill. Each argument is a `### Skill.Arg:<Name>` block nested in it, never a markdown table. The blocks are the single declaration of the skill's arguments: they teach the agent the arguments and render `Batchy.Skill.Help`.

Each `Skill.Arg` block has fundamentals (what the argument means) plus bullet settings:

- `required` — true/false.
- `default` — value filled when the flag is omitted.
- `help` — one line of meaning; this is what `-h` prints.
- `examples` — the canonical flag spelling, e.g. `--project "BlaBla"`. Carries the expected flag form.
- `type` — `switch` (boolean, no value) or `valued`. Default assumption: `valued`.
- `aliases` — only for non-obvious flags; the agent infers obvious ones.

Example:

```markdown
## Skill.Arg.Section

### Skill.Arg:Target.Project
- the project this skill operates on
- required: true
- help: "the project this skill operates on"
- examples: --project "my-project"

### Skill.Arg:Alignment.Mode
- whether the skill asks at checkpoints or runs autonomously
- required: false
- default: Interactive
- type: switch
- help: "run autonomously instead of asking at checkpoints"
- examples: --AUTO
- aliases: --autonomous, --auto
```

## Resolution Rules

- Map every supplied flag to a canonical `Skill.Arg` name from the skill's `Skill.Arg.Section`.
- Accept loose forms: case variants, abbreviations, and obvious synonyms.
- A bare value with no flag may resolve to an obvious positional argument.
- Fill declared `default`s silently for omitted arguments.
- For a `required` argument that is missing, follow `Skill.Explicit.Args`: ask or orient — never guess a value.
- On a real run, echo the resolved arguments through `Batchy.Skill.Banner` (below) before acting.

## Batchy.Skill.Help

`-h` / `--help` is a non-executing call: print terminal-style usage from the skill's `Skill.Arg` blocks, then stop. It short-circuits execution and wins over any other supplied flags.

Lead with a one-paragraph explanation of what the skill is and does, then render each argument's flag, meaning, default, and required state. The paragraph orients a caller who has never run the skill; the argument list tells them how to invoke it. Example output:

```text
$my-skill — operate on an Agentos project. Runs the maintenance pass over the
target project's surfaces, asking for confirmation at each checkpoint unless told
to run autonomously. Read-only by default until a change is approved.

usage: $my-skill --project <name> [--AUTO]

  --project   the project this skill operates on   (required)
  --AUTO      run autonomously instead of asking    (default: Interactive)
```

## Batchy.Skill.Banner

On a real run (anything but `-h`), the skill prints a `Batchy.Skill.Banner` as its first step: a short banner echoing how the arguments resolved. It is informational, not a checkpoint — it prints, it does not ask — and it runs even under `Alignment.Mode:Autonomous`.

- Show the mapping from supplied flags to canonical arguments and the values used.
- Distinguish supplied values from filled defaults, so the caller sees what was inferred.
- Keep it short; it is the first line of output, not a report.

The banner is mostly derived from the skill's `Skill.Arg` blocks and the resolved values. Restate a short banner section in the target skill (a `Cited.Duplication` of this convention) so the run does not forget it — deliberate repetition for compliance.

Example:

```text
$my-skill — banner
  Target.Project   = my-project        (from --project)
  Alignment.Mode   = Autonomous        (from --AUTO)
  Verbose          = false             (default)
```

## Batchy.SubCommand

A skill may expose subroutines as `Batchy.SubCommand`s — `Dotted.Name` subparts activated explicitly by name.

- Placement by `Natural.Placement`: a small subcommand is a section in `SKILL.md`; a large one is its own file (e.g. `references/subcommands/<name>.md`).
- Activation is lazy: the agent loads only the invoked subcommand's section or file, keeping context lean.
- A subcommand is selected like an argument that activates a subroutine rather than passing data (`--index-write` ≈ activate `Index.Write`). The agent resolves loose forms (`--index-write`, `INDEX-WRITE`, `index-write`).
- Each subcommand is itself a `Batchy.Skill`: its own `Skill.Arg.Section` and `Batchy.Skill.Help`.
- A subcommand inherits the container skill's arguments and adds its own on top.
- Help composes: top-level `-h` lists the subcommands; `<subcommand> -h` renders that subcommand's `Skill.Arg` blocks.
- The skill designer keeps argument and subcommand names sufficiently distinct so activation is unambiguous.

## Authoring Checklist

- Body follows the `Batchy.Skill.Template`: description, `Batchy.Skill.Contract`, `Skill.Arg.Section`, optional `SubCommands`.
- A `Batchy.Skill.Contract` block near the top restates the `-h`, banner, and resolution rules standalone.
- Arguments declared as `### Skill.Arg:<Name>` blocks in a `Skill.Arg.Section`.
- Each argument advertised enough that `-h` is useful.
- Tokens written `--flag`-style — arguments and subcommands alike.
- `description` frontmatter carries a `Skill.Trigger.Clause` and names the key arguments so an agent knows what to provide before loading.
- Missing-argument behavior stated: ask, orient, or noop — never guess.
- Subcommands, if any, named in `Dotted.Notation` and distinct from argument names.
