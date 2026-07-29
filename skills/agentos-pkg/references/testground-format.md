# Testground Format

Reference for testground structure and test file format.

## Testground Folder Structure

A testground is an Agentos project folder dedicated to testing a package skill.

```
<package>-testground/
├── AGENTS.md              — project guidance; routes to the tested package skill
├── .agentos/
│   ├── project.json       — Agentos project identity
│   └── tests/
│       └── reports/       — test run reports
├── testing/
│   ├── README.md          — overview of available tests
│   └── <test-name>.md     — individual test files
└── (optional fixtures, local index, etc.)
```

- `AGENTS.md` should route the agent to the tested package skill without mentioning that the project is a test environment.
- The `testing/` folder holds test files. Each file is one test scenario.
- Fixtures or local surfaces can be added when the test needs controlled project state beyond `AGENTS.md`.

## Test File Format

Each test file follows this structure:

```markdown
# Test: <test-name>

## Purpose

What this test evaluates. One or two sentences.

## Entry Path

The expected activation route, e.g.:
`AGENTS.md -> load <package-skill> -> Package.SKILL:<package>`

## How To Run

Model recommendations and runner instructions.
The tested agent should not know it is being tested.

## Subagent Prompt

The natural-language prompt given to the tested agent.
Must be self-contained — no hidden setup or prior context.

## Behavior Tiers

Evaluation criteria organized by what the agent did.

### Minimal Pass
- (minimum acceptable behavior)

### Expected Behavior
- (proportional, well-routed behavior)

### Above Expected
- (deeper work, useful but not required)

### Overwork
- (disproportionate cost — diagnostic signal for entry-path quality)

### Failure Signs
- (behaviors that indicate the test failed)

## Navigation Trace

How to capture and interpret the agent's surface-loading sequence.

## Evolution Notes

Space for enriching the test after real runs.
```

## Behavior Tiers

Behavior tiers evaluate what the agent did, not just what it produced.

- **Minimal pass** — the agent recognized the task type and produced acceptable output using package guidance.
- **Expected behavior** — the agent navigated proportionally. Used the right surfaces without excessive loading. Cost matches task complexity.
- **Above expected** — the agent went deeper than required and produced stronger results. Useful but not the target bar.
- **Overwork** — the agent produced good output but at disproportionate cost. This is a diagnostic signal: the package driver or routing surfaces may not be giving enough orientation.
- **Failure signs** — concrete behaviors that indicate the test failed. These should be specific and observable.

Tiers are not just output quality levels. They encode a judgment about navigation efficiency and behavioral proportionality.

## Navigation Trace

The navigation trace is the sequence of surfaces the agent loaded during the test. It makes each run diagnostic for entry-path quality, not just pass/fail.

Traces should come from the session transcript (via chatlas), not from the agent's self-report.

Example trace notation:
```
SKILL.md -> agentos-hugentics -> 000-INDEX.md -> proposed block    (expected)
SKILL.md -> agentos-hugentics -> 000-INDEX.md -> 100 -> 101 -> ... (overwork)
```

## Test Design Guidelines

- Keep prompts natural — the tested agent should behave as it would in a real session.
- Design prompts that exercise routing discrimination — the agent should go to the right subsystem, not just any subsystem.
- Include overlap traps when testing concept work — propose something that resembles existing content.
- One test file per scenario. Name files descriptively: `<package>-driver-<topic>-01.md`.
- Tests will be enriched over time as real runs reveal new failure modes.
