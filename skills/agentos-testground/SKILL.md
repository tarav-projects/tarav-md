---
name: agentos-testground
description: "Testing subsystem for package skills — behavioral tests that measure how agents use a Package.Skill in a controlled project environment. Covers test format, runner isolation, trace capture, and behavior-tier evaluation. USE WHEN running, listing, designing, or evaluating testground tests for a package skill. Called like a terminal command: a `--run`/`--list`/`--design`/`--evaluate` subcommand on a target `--package`."
---

# agentos-testground

`Package.Aux.Skill` for testground-based package skill testing.

A testground is a controlled project that tests how an agent USES a `Package.Skill` — what it loaded, how it navigated, and what it produced — not just output correctness. Any package skill can have one: a separate project folder that imports the skill and holds test files under `testing/`. This skill runs, lists, designs, and evaluates those tests.

This is a `Batchy.Skill` — called like a terminal command. Load `agentos-skills-base` for the full convention.

- `-h` / `--help` prints usage and exits without running (`Batchy.Skill.Help`).
- every run prints a banner of the resolved arguments as its first step (`Batchy.Skill.Banner`).
- supplied flags resolve to the `Skill.Arg` names below; loose and positional forms resolve too (a bare package name is `--package`).
- pick a `--`subcommand for the operation; with no subcommand and no flags, this skill just loads its orientation context and performs nothing.

## Skill.Arg.Section

These arguments are shared across subcommands. Each subcommand states which it requires; `--package` is always required.

### Skill.Arg:Target.Package
- the package skill to test; locates its tests under `<package>/testing/`
- required: true
- help: "which package skill to test"
- examples: --package "stripe-pkg"

### Skill.Arg:Testground
- the controlled project to execute or operate from
- a package may declare a default testground, used when this is omitted
- required: false (required by `--run` when no default exists)
- help: "which testground environment to use"
- examples: --testground "stripe-pkg-testground"

### Skill.Arg:Test.Name
- a specific test to target; omitted means all tests
- required: false
- help: "a specific test; omitted -> all"
- examples: --test "entry-path-from-cold"

### Skill.Arg:Model
- the model for the tested agent
- required: false
- default: the runner default
- help: "model for the tested agent"
- examples: --model "claude-haiku-4-5"

### Skill.Arg:Report
- a completed run to evaluate: a report under `<testground>/.agentos/tests/reports/` or a captured transcript
- required: false (required by `--evaluate`)
- help: "the run report or transcript to evaluate"
- examples: --report "reports/entry-path-from-cold.md"

## SubCommands

Each `Batchy.SubCommand` inherits the arguments above and sets which are required. Activate by name; `<subcommand> -h` prints its own usage.

- `--run` — execute tests in a testground and capture traces. Requires `--package` and `--testground` (unless the package has a default); accepts `--test`, `--model`. Runs as fresh CLI sessions from the testground folder (runner isolation), captures each navigation trace from the transcript, and reports against the test's behavior tiers.
- `--list` — list the tests available for a package. Requires `--package`; accepts `--testground`.
- `--design` — design a new test or testground environment. Requires `--package`; accepts `--testground`, `--test`. See `agentos-pkg/references/testground-format.md` for the format.
- `--evaluate` — evaluate a completed run against behavior tiers. Requires `--package` and `--report`; accepts `--test`. The evaluator judges the tier match and writes the report.

Detailed run procedure, trace capture, and report format: `agentos-pkg/references/testground-runner.md`.

## Core Concepts

- **Testground** — a controlled project folder for testing a package skill. Has its own `AGENTS.md`, can control visible skills, fixture files, and task prompts.
- **Test file** — defines a subagent prompt, entry path, behavior tiers, and navigation trace expectations. Lives in `testing/` inside the testground.
- **Behavior tiers** — evaluation levels: minimal pass, expected behavior, above expected, overwork, failure. Measure what the agent did, not just what it produced.
- **Navigation trace** — the sequence of surfaces the agent loaded, captured from the session transcript. Diagnostic for entry-path quality.
- **Runner isolation** — tests run as fresh CLI sessions from the testground folder, not as subagents of the current session, giving authentic entry-path behavior.

## References

| Reference | Covers |
|---|---|
| `agentos-pkg/references/testground-format.md` | Test file format, behavior tiers, navigation trace, testground folder structure |
| `agentos-pkg/references/testground-runner.md` | How to run tests: CLI isolation, chatlas trace capture, evaluation procedure, test reports |

## Testground Discovery

Testgrounds are project folders whose purpose is testing a package skill. They follow the Agentos project model (`AGENTS.md`, optional index, `testing/` folder). To find them, look for project folders with a `testing/` directory containing test files in the expected format.
