# Batchy Skills — Running One

How to *operate* a `Batchy.Skill`. This is the runner-facing convention — what you need to correctly invoke a skill. For building one, see `batchy-skill-designer.md`. Concepts are canonical in `agentos-pkg/design/101-design.md`.

Every Agentos skill is a `Batchy.Skill` — called like a terminal command. The convention is a convention the agent knows, not a parser: a clear natural prompt always works, and flags are the crisp path as parameter count grows.

## The Call

- A skill is invoked like a CLI command: a name, optional flags, optional a value or two.
- `-h` / `--help` is universal and always available, even on a skill that takes no arguments.
- Arguments come as bash-like flags — **valued** (`--project "stripe-pkg"`) or **switch** (`--AUTO`).
- Tokens are written `--flag`-style by preference so they read as commands inside prose (`do a --run on stripe-pkg`); the agent still resolves bare and loose forms.

## `-h` / `--help` (always)

- Short-circuits the skill: print the help into the chat and stop. `-h` wins over any other supplied flags.
- It is a deliberate help *output to the user* — distinct from silently loading the skill to orient the agent.
- The help leads with one paragraph on what the skill is and does, then the usage rendered from the skill's `Skill.Arg` blocks. A zero-argument skill states it takes none.

## The Run Banner (when it has arguments)

- On a real run (anything but `-h`), the first step is to print a `Batchy.Skill.Banner`: a short echo of how the flags resolved.
- It shows each supplied flag mapped to its canonical argument and the value used, and distinguishes supplied values from filled defaults.
- Informational, not a checkpoint — it prints, it does not ask — and it runs even under `Alignment.Mode:Autonomous`. A zero-argument skill has no banner.

```text
$my-skill — banner
  Target.Project   = stripe-pkg     (from --project)
  Alignment.Mode   = Autonomous     (from --AUTO)
  Verbose          = false          (default)
```

## Resolving Flags, Values, and Modules

- Map every supplied flag to a canonical `Skill.Arg` (or `Skill.Module`) name from the skill body.
- Accept loose forms: case variants, abbreviations, obvious synonyms (`--proj` ≈ `--project`).
- A bare value with no flag may resolve to an obvious positional argument.
- Switch values use `Dotted.Parameterized.Notation`: `--AUTO` → `Alignment.Mode:Autonomous`.
- A **selector** argument picks one operation among enumerated values (`--run` → `Command:Run`); a **switch** layers an additive behavior (`--dry-run`).
- Fill declared `default`s silently for omitted arguments.
- For a missing `required` argument, follow `Skill.Explicit.Args`: ask or orient — never guess a value.

## Activating a Module

- A `Skill.Module` is a named, on-demand-loadable part of the skill — a file or section. Mentioning it (e.g. `--examples`, `examples`) loads it into context.
- An argument may carry an `action` that activates a module when set; otherwise the module's name is itself the handle.
- Load only the modules the current call needs — progressive disclosure keeps context lean.
