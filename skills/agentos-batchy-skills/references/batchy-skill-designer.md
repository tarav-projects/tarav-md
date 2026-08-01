# Batchy Skills — Designing One

How to *build* a `Batchy.Skill`. This is the designer-facing guide — best practices for authoring a skill. For operating one, see `batchy-skill-run.md`. The skill primitives are canonical in `agentos-pkg/design/101-design.md`; the runtime routing model is canonical in `agentos-pkg/design/107-design.md`.

## The Skill Template

Every Batchy skill instantiates one `Batchy.Skill.Template` — the same skeleton — so all Agentos skills share a shape. Lay the body out in this order:

1. a one-paragraph description of what the skill is and does;
2. a `Batchy.Skill.Contract` block — the in-skill mini-course (below);
3. a `## Skill.Index.Section` defining the skill's own key concepts — only when the skill hinges on a few defined terms;
4. a `## Skill.Arg.Section` of `### Skill.Arg:<Name>` blocks — only when the skill takes arguments;
5. any `Routing.Table`s needed for prompt context, module selection, or multi-level routing;
6. a `## User.Command.Section` of `### User.Command::<Name>` blocks — only when the skill exposes explicit workflow transitions;
7. any `Skill.Module`s — named files or sections selected by the router when applicable.

Adapt the template to the skill: a zero-argument skill omits the `Skill.Arg.Section` (and its Contract carries only the help rule); a single-operation skill needs no extra modules; most skills omit the `Skill.Index.Section`. The `Batchy.Skill.Contract` and the frontmatter `Skill.Trigger.Clause` (a `USE WHEN` line) are always present.

## The Batchy.Skill.Contract Block

Carry a `Batchy.Skill.Contract` near the top of the skill body: a compact mini-course that restates the convention so the skill complies even when `agentos-batchy-skills` is not loaded. It is a `Cited.Duplication` — duplicate the few must-do behaviors, cite the base skill for depth.

```markdown
This is a `Batchy.Skill` — called like a terminal command. Load `agentos-batchy-skills`
for the full convention.

- `-h` / `--help` prints the help into the chat instead of running (`Batchy.Skill.Help`).
- a written `--<flag>` is intentional run configuration and must be resolved by `Batchy.Router`.
- without an explicit route, conversational discovery remains available only where the applicable row permits it.
- every non-help run with custom configuration prints its resolved configuration first (`Batchy.Skill.Banner`).
```

A zero-argument skill carries only the help rule:

```markdown
This is a `Batchy.Skill`. Load `agentos-batchy-skills` for the full convention.

- `-h` / `--help` prints this skill's help into the chat instead of running; it takes no arguments.
```

A command-bearing skill also carries the workflow-gate rule:

```markdown
- declared `User.Command`s are the only way to cross their explicit workflow gates.
- when the workflow pauses, print only the commands available at that checkpoint.
```

## Skill.Index.Section

Most skills skip this. Include a `## Skill.Index.Section` only when the skill hinges on a few defined concepts the rest of the body leans on — for example a two-agent skill that keeps referring to `Caller.Agent` and `Master.Agent`. It is a `Skill.Arg.Section` sibling: a named section holding one kind of block, scoped to this one skill, with no local router (distinct from the package-wide `Package.Skill.Index`).

Write each concept as a compact block — a `Dotted.Name` heading plus a few orthogonal lines, like a tiny `Kernel.Block::Index` entry. Define, do not narrate.

```markdown
## Skill.Index.Section

### Caller.Agent
- the agent that invokes this skill; owns the caller conversation and context
- distills the relevant context and hands it to the `Master.Agent`

### Master.Agent
- the read-only research agent the caller spawns
- researches the sources and returns the answer, keeping that context off the caller
```

## Skill.Arg.Section

Declare arguments in a `## Skill.Arg.Section`. Each argument is a `### Skill.Arg:<Name>` block nested in it, never a markdown table. The blocks are the single declaration of the skill's arguments: they teach the agent the arguments and render `Batchy.Skill.Help`.

Each `Skill.Arg` block has fundamentals (what the external data means) plus bullet settings:

- `required` — true/false.
- `default` — value filled when the flag is omitted.
- `type` — `switch` (boolean, no value) or `valued`. Default assumption: `valued`.
- `help` — one line of meaning; this is what `-h` prints.
- `examples` — the canonical flag spelling, e.g. `--project "stripe-pkg"`.
- `flags` or `examples` — the explicit flag spellings that route values to this argument.
- `aliases` — additional exact flag keys when the route deliberately supports them.

```markdown
## Skill.Arg.Section

### Skill.Arg::Target.Project
- the project this skill operates on
- required: true
- help: "the project this skill operates on"
- examples: --project "my-project"

### Skill.Arg::Alignment.Mode
- whether the skill asks at checkpoints or runs autonomously
- required: false
- default: Interactive
- type: switch
- help: "run autonomously instead of asking at checkpoints"
- examples: --AUTO
- aliases: --autonomous, --auto
```

`Skill.Arg` owns this data identity and contract. `Batchy.Router` owns extracting, defaulting, validating, and binding its value. Do not model an operation, module, or workflow selection as a `Skill.Arg` merely because a flag can select it.

## Batchy.Router

Every call is resolved by one `Batchy.Router`. Its resolution inputs are:

- explicit `Batchy.Skill.Flag`s written as `--<flag>`;
- the live conversation, when a row permits automatic discovery;
- declared defaults, when a row supplies one.

Every `Batchy.Router.Row` relates its permitted resolution inputs to one destination. A resolved row may bind a `Skill.Arg`, select a `Skill.Module`, or contribute or continue routing through a `Routing.Table`. Explicit configuration takes precedence when several permitted inputs resolve the same row.

Declare each custom flag with the primitive or row that owns its effect. There is no separate flag section. Exact and alias keys are appropriate for strict routes; a semantic keyword family is appropriate only when the row deliberately accepts that softer key model.

Use a `Routing.Table` when the skill needs declarative routing. In Skillware, declare one addressed `--routing-table` annotation and give every `Batchy.Router.Row` its own address plus explicit `--table` membership. A row declares its canonical flags, aliases, resolution policy, defaults, routed destinations, load targets, and optional `--when`/`--then` prompts. The table declares whether resolution may select none, one, or several rows.

Treat the table as the canonical router model. Place `--routing-view calls`, `--routing-view modules`, and `--routing-view full` annotations where the runnable skill needs its public call surface, module catalog, or complete semantic table; Skillware derives those views rather than asking authors to keep parallel tables aligned.

`Usage.Pattern.Routing` is one row style, not another router. Its `--when` body describes a recurring usage situation and its `--then` body describes the response, surface, behavior, or further route that situation needs.

## Skill.Module — Encapsulated Routing Targets

A `Skill.Module` is a named, encapsulated subsystem of the skill — a file or a section. This is **progressive disclosure made addressable-by-name**: the module owns its boundary and content while `Batchy.Router` owns selecting and loading it.

- **Placement is `Natural.Placement`** — an inline `##` section, a skill-root file, or a `references/` file. Never a mandated folder.
- **Addressable by default** — files and sections provide stable module targets without requiring an argument declaration.
- **Explicit or automatic selection** — a row may require a flag, permit conversational discovery, accept a route contributed by another table, or combine those paths.
- **Not an argument** — a flag selecting a module routes directly to the module. Declare a separate `Skill.Arg` only for external data the loaded subsystem consumes.

## User.Command.Section

Declare explicit workflow transitions in a `## User.Command.Section`. Each canonical command is a `### User.Command::<Name>` block. A command declaration states:

`User.Command.Section` owns the inventory, `User.Command.Trigger` owns each accepted invocation spelling, and `User.Command.Arg` owns each transition input and its resolution policy.

- `triggers` — one or more accepted `::`-prefixed spellings; aliases remain semantically identical.
- `available` — the workflow checkpoints where the command may execute.
- `action` — the single transition the command performs.
- nested `#### User.Command.Arg::<Name>` blocks — inputs required by the transition.

Each command argument states what it means, whether it is required, and one `resolution` policy: `Explicit`, `Contextual`, or `Defaulted`. A contextual required argument may be omitted from the command line only when the foreground workflow resolves it uniquely.

```markdown
## User.Command.Section

### User.Command::Approve
- accept the selected draft without writing it
- triggers: `::approve`, `::approved`
- available: when an approval-ready draft is foregrounded
- action: mark the resolved draft approved and unlanded

#### User.Command.Arg::Target
- the draft to approve
- required: true
- resolution: Contextual
```

At every declared pause, print the commands available there. Do not append command menus to ordinary conversational turns. Keep the gate unresolved through free-form discussion, fail closed on ambiguous targets or arguments, and invalidate commands whose underlying proposal has changed.

## Namespace Discipline (designer's responsibility)

Flag keys and routing destinations participate in one run-configuration space. Keep strict keys, aliases, arguments, module names, and table routes distinguishable enough that the applicable row can resolve them coherently:

- `--examples` may select `examples.md`; it must not also bind unrelated external data unless one row explicitly defines that combined effect.
- only `--<flag>` carries explicit flag semantics; bare prose may still discover an automatic route but is not silently reclassified as a flag.
- when two strict routes collide, rename or scope one — this is the skill designer's job, not the runner's.

## Batchy.Skill.Help

`-h` renders callable help from the `Batchy.Router` configuration reachable through `Skill.Arg` blocks, `Skill.Module` targets, and `Routing.Table`s. Lead with one paragraph on what the skill is and does, then show the explicit flags and value shapes the caller may configure. A skill with no custom flags or arguments says so.

```text
$my-skill — operate on an Agentos project. Runs the maintenance pass over the
target project's surfaces, asking for confirmation at each checkpoint unless told
to run autonomously. Read-only by default until a change is approved.

usage: $my-skill --project <name> [--AUTO]

  --project   the project this skill operates on   (required)
  --AUTO      run autonomously instead of asking    (default: Interactive)
```

## Batchy.Skill.Banner

Restate a short banner section in the target skill (a `Cited.Duplication` of the convention) so the run does not forget to print it — deliberate repetition for compliance. The banner reports every supplied flag with its resolved effect, resolved argument values, declared defaults, and semantically discovered configuration. See `batchy-skill-run.md` for the runtime behavior and an example.

## Authoring Checklist

- Body follows the `Batchy.Skill.Template`: description, `Batchy.Skill.Contract`, optional index and argument sections, applicable routing tables, optional command section, and naturally placed modules.
- A `Batchy.Skill.Contract` block near the top restates help, explicit-flag, automatic-discovery, banner, and command-gate rules that apply.
- Arguments declared as `### Skill.Arg::<Name>` blocks, never a table.
- Each argument advertised enough that `-h` is useful.
- Every operation flag routes to its actual destination; it is not modeled as an argument unless its effect is external-data binding.
- Explicit tokens use `--<flag>`; bare or loose prose is available only through rows that permit automatic discovery.
- Each router row declares whether explicit flags, conversation, defaults, or a combination may resolve it.
- Module selection targets `Skill.Module` directly; argument binding targets `Skill.Arg`; prompt composition targets `Routing.Table`.
- Strict keys and destinations remain collision-free.
- `description` frontmatter carries a `Skill.Trigger.Clause` and names the key arguments.
- Missing-argument behavior stated: ask, orient, or noop — never guess.
- Commands declare canonical identity, triggers, availability, action, and argument resolution; equivalent triggers never fork semantics.
- Command-bearing workflows print available commands only at pauses or on status requests.
