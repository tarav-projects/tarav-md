---
name: agentos-pkgs-usage-pattern-miner
description: "Mines chatlas sessions for package skill usage patterns. USE WHEN you want to discover, validate, or refine usage patterns for a package by analyzing real agent sessions that used it. Requires a target package. Called like a terminal command — a `--discover`/`--compare`/`--suggest` command on a target `--package`. Uses chatlas transcripts to extract situation/response pairs and compare against existing usage-patterns/."
---

# agentos-pkgs-usage-pattern-miner

`Package.Aux.Skill` for mining real usage data from chatlas sessions to discover, validate, and refine `Package.Skill.UsagePattern` entries.

This skill closes the feedback loop between real agent usage and documented package hot paths. It reads organic sessions, extracts situation/response pairs, compares them against existing patterns, and suggests improvements or new patterns.

This is a `Batchy.Skill` — called like a terminal command. Load `agentos-batchy-skills` for the full convention.

- `-h` / `--help` prints usage and exits without running (`Batchy.Skill.Help`).
- every run prints a banner of the resolved arguments as its first step (`Batchy.Skill.Banner`).
- supplied flags resolve to the `Skill.Arg` names below; a bare package name is `--package`.
- pick a `--`command for the operation (the `Skill.Arg:Command` selector); with no command and no flags, this skill just loads orientation context and mines nothing.

## Skill.Arg.Section

`--package` is always required; the others are shared across commands.

### Skill.Arg:Command
- the operation to perform — a selector whose values each activate a command behavior (a `Skill.Module`)
- values: `Command:Discover`, `Command:Compare`, `Command:Suggest`; tokens `--discover` / `--compare` / `--suggest`
- required: false (omitted -> orient only, mines nothing)
- type: selector
- help: "which mining operation to perform"
- examples: --discover

### Skill.Arg:Target.Package
- the package skill whose usage patterns to mine; sets which `usage-patterns/` folder to compare against and which skill name to search in chatlas
- required: true
- help: "which package skill to mine usage patterns for"
- examples: --package "stripe-pkg"

### Skill.Arg:Session.Selector
- chatlas query filters that narrow the session pool, passed through to `agentos chatlas query`
- required: false
- help: "chatlas query filters to narrow the sessions mined"
- examples: --session-selector "--updated-after 2026-01-01 --provider claude-code --limit 50"

### Skill.Arg:Focus
- a specific pattern name or situation type to focus on; omitted means mine broadly
- required: false
- help: "a pattern name or situation type to focus on"
- examples: --focus "cold-entry navigation"

## Commands

The `Skill.Arg:Command` selector picks the operation; each value activates a command behavior and inherits the arguments above. They are stages of one pipeline but each is independently useful; activate the one you want (`--discover`).

- `--discover` — find sessions that loaded the target package and extract situation / navigation trace / outcome.
- `--compare` — match discovered sessions against existing `<package>/usage-patterns/` and surface follows, deviations, and gaps.
- `--suggest` — propose new patterns, refinements, test candidates, and router updates from discovery and comparison.

The command procedures are detailed below.

## Operations

### Discover

Find sessions where the target package skill was loaded. Extract the user's initial situation and the agent's navigation path.

```bash
agentos chatlas query --provider claude-code --updated-after <date>
agentos chatlas views inline <session-id> --view transcript
```

From the transcript, extract:
- **Situation** — what the user asked or needed (first user message + context)
- **Navigation trace** — which surfaces the agent loaded, in what order (from tool calls)
- **Outcome** — what the agent produced, whether the user was satisfied

### Compare

Against existing `<package>/usage-patterns/`:
- Does this session match an existing pattern? Did the agent follow the expected path?
- Did the agent deviate? Was the deviation better or worse than the documented path?
- Is there a recurring situation across sessions that no pattern captures yet?

### Suggest

Based on discovery and comparison, propose:
- **New patterns** — recurring situations not yet captured. Draft the situation/response pair.
- **Pattern refinements** — existing patterns where real usage shows a better path or reveals missing steps.
- **Test candidates** — patterns that should be verified via `agentos-testground`. The situation is the test prompt; the expected path becomes behavior tiers.
- **Router updates** — situations frequent enough to warrant a router entry in `Package.SKILL`.

## What This Skill Does NOT Do

- Write patterns directly — all mutations are user-gated
- Run tests — use `agentos-testground` for that
- Modify the target package — that's the user's job after reviewing suggestions
- Evaluate test runs — use the testground evaluation flow for that

## How To Identify Target Sessions

A session "uses" a package if the agent loaded the package's `SKILL.md` during the session. In the chatlas transcript, look for tool calls that read the package skill file.

For `agentos-pkg`, search for sessions that read `agentos-pkg/SKILL.md` or loaded skills that depend on it (aux skills like `agentos-index`, `agentos-hugentics`, etc.).

## Pattern Output Format

When suggesting a new pattern, use this shape:

```markdown
# Usage Pattern: <Pattern.Name>

## Situation

<What the user asks or needs. Natural language, 2-4 sentences.>

## Expected Behavior Path

<Ordered list of surfaces loaded and actions taken.>

1. Agent loads X
2. Agent checks Y
3. Agent produces Z

## Key Signals

- <What in the user's message triggers this pattern>
- <What distinguishes this from similar patterns>

## Related Patterns

- <Other patterns that could be confused with this one>
```

## Pipeline

The full cycle this skill participates in:

```
chatlas sessions → pattern miner (this skill) → usage-pattern file → testground test → test results → pattern refinement
```

Each stage is independently useful. A mined insight is valuable even without a test. A test is valuable even without mining. But the full cycle produces verified, reality-weighted package documentation.

## References

- `agentos-pkg/references/testground-format.md` — how tests are shaped (behavior tiers connect to expected behavior paths)
- `agentos-pkg/references/testground-runner.md` — how to run tests from mined patterns
- `Package.Skill.UsagePattern` — the concept being mined for (see `index/101-index.md`)
