# Batchy Skills — Designing One

How to *build* a `Batchy.Skill`. This is the designer-facing guide — best practices for authoring a skill. For operating one, see `batchy-skill-run.md`. Concepts are canonical in `agentos-pkg/index/101-index.md` (`Batchy.Skill`, `Batchy.Skill.Template`, `Batchy.Skill.Contract`, `Skill.Arg`, `Skill.Arg.Section`, `Batchy.Skill.Help`, `Batchy.Skill.Banner`, `Skill.Module`).

## The Skill Template

Every Batchy skill instantiates one `Batchy.Skill.Template` — the same skeleton — so all Agentos skills share a shape. Lay the body out in this order:

1. a one-paragraph description of what the skill is and does;
2. a `Batchy.Skill.Contract` block — the in-skill mini-course (below);
3. a `## Skill.Arg.Section` of `### Skill.Arg:<Name>` blocks — only when the skill takes arguments;
4. any `Skill.Module`s — named files or sections, optionally fronted by an arg.

Adapt the template to the skill: a zero-argument skill omits the `Skill.Arg.Section` (and its Contract carries only the help rule); a single-operation skill needs no extra modules. The `Batchy.Skill.Contract` and the frontmatter `Skill.Trigger.Clause` (a `USE WHEN` line) are always present.

## The Batchy.Skill.Contract Block

Carry a `Batchy.Skill.Contract` near the top of the skill body: a compact mini-course that restates the convention so the skill complies even when `agentos-batchy-skills` is not loaded. It is a `Cited.Duplication` — duplicate the few must-do behaviors, cite the base skill for depth.

```markdown
This is a `Batchy.Skill` — called like a terminal command. Load `agentos-batchy-skills`
for the full convention.

- `-h` / `--help` prints the help into the chat instead of running (`Batchy.Skill.Help`).
- every run prints a banner of the resolved arguments as its first step (`Batchy.Skill.Banner`).
- supplied flags resolve to the `Skill.Arg` names below; loose and positional forms resolve too.
```

A zero-argument skill carries only the help rule:

```markdown
This is a `Batchy.Skill`. Load `agentos-batchy-skills` for the full convention.

- `-h` / `--help` prints this skill's help into the chat instead of running; it takes no arguments.
```

## Skill.Arg.Section

Declare arguments in a `## Skill.Arg.Section`. Each argument is a `### Skill.Arg:<Name>` block nested in it, never a markdown table. The blocks are the single declaration of the skill's arguments: they teach the agent the arguments and render `Batchy.Skill.Help`.

Each `Skill.Arg` block has fundamentals (what the argument means) plus bullet settings:

- `required` — true/false.
- `default` — value filled when the flag is omitted.
- `type` — `switch` (boolean, no value) or `valued`. Default assumption: `valued`.
- `help` — one line of meaning; this is what `-h` prints.
- `examples` — the canonical flag spelling, e.g. `--project "stripe-pkg"`.
- `aliases` — only for non-obvious flags; the agent infers obvious ones.
- `action` — optional; the behavior the arg activates when set (see below).

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

## Skill.Module — Files and Sections as Addressable Parts

A `Skill.Module` is a named, on-demand-loadable part of the skill — a file or a section. This is **progressive disclosure made addressable-by-name**: any sub-file or section is implicitly a module, and mentioning its name reinforces loading it. It generalizes the old subcommand — no dedicated structure or `subcommands/` subfolder.

- **Placement is `Natural.Placement`** — an inline `##` section, a skill-root file, or a `references/` file. Never a mandated folder.
- **Implicit by default** — you do not need to declare an arg for a module. `examples.md` is already addressable as `--examples`; the agent maps the mention to the file.
- **Declare a `Skill.Arg` with an `action` only when you want more** — help text, parameters, or selector-exclusivity. The arg's `action` says "when set, activate this module/behavior."

### Subcommands are just arguments with an action

What used to be a subcommand is now an `action`-bearing `Skill.Arg`:

- a **switch** with an action layers a behavior — `--dry-run` activates a read-only "dry-run" module;
- a **selector** with an action picks one operation among enumerated values — `--run`/`--list`/`--evaluate` are values of one `Command` arg (`Command:Run`, `Command:List`…), each carrying an action; the `--run` token is sugar resolving to that value.

The action body lives wherever `Natural.Placement` puts it: inline in the arg block, a `##` section, or a file.

## Namespace Discipline (designer's responsibility)

Argument names, file names, and section names **share one resolution space** — they are all activatable handles. Keep them distinct and unambiguous so a mention maps to exactly one thing:

- `--examples` must unambiguously mean `examples.md` (or the `## Examples` section), not collide with an `examples` argument that means something else.
- name modules and args so loose forms (`--run`, `RUN`, `run`) resolve without contest.
- when two handles could collide, rename one — this is the skill designer's job, not the runner's.

## Batchy.Skill.Help

`-h` renders from the `Skill.Arg` blocks. Lead with one paragraph on what the skill is and does, then each argument's flag, meaning, default, and required state. A zero-argument skill's help is just the paragraph plus "takes no arguments."

```text
$my-skill — operate on an Agentos project. Runs the maintenance pass over the
target project's surfaces, asking for confirmation at each checkpoint unless told
to run autonomously. Read-only by default until a change is approved.

usage: $my-skill --project <name> [--AUTO]

  --project   the project this skill operates on   (required)
  --AUTO      run autonomously instead of asking    (default: Interactive)
```

## Batchy.Skill.Banner

Restate a short banner section in the target skill (a `Cited.Duplication` of the convention) so the run does not forget to print it — deliberate repetition for compliance. The banner echoes resolved flags → canonical args, marking supplied vs default values. See `batchy-skill-run.md` for the runtime behavior and an example.

## Authoring Checklist

- Body follows the `Batchy.Skill.Template`: description, `Batchy.Skill.Contract`, `Skill.Arg.Section` (if any args), modules (if any).
- A `Batchy.Skill.Contract` block near the top restates the `-h`, banner, and resolution rules standalone.
- Arguments declared as `### Skill.Arg:<Name>` blocks, never a table.
- Each argument advertised enough that `-h` is useful.
- Tokens written `--flag`-style.
- Subcommands expressed as `action`-bearing args (switch or selector), not a dedicated structure.
- Arg / file / section names share one namespace — keep them collision-free.
- `description` frontmatter carries a `Skill.Trigger.Clause` and names the key arguments.
- Missing-argument behavior stated: ask, orient, or noop — never guess.
