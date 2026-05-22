# Index Test System

General mechanism for testing index activation and runtime behavior across any Agentos project.

## How It Works

- **Pattern**: master agent + subagent
- **Subagent**: receives a natural prompt — activates the index, performs tasks, responds in a structured format. The subagent does not know it is being tested.
- **Master agent (reviewer)**: evaluates the subagent's responses against expected answers using semantic match.

## Test File Format

Each test file contains:

1. **Subagent Prompt** — the full prompt to give the subagent. Includes activation instructions, tasks, and response format. Must be self-contained.
2. **Expected Answers** — hints for the reviewer. These are correct-answer guides, not exact strings. The reviewer judges whether the subagent's response captures the same meaning.

## Test Location

- tests live in the package index `testing/` folder
- each project ships its own test suite alongside its package index surface
- this reference file defines the general mechanism — the test files are project-specific

## Running a Test

1. Spawn a subagent with the prompt from the test file
2. Capture the session (Chatlas can be used for transcript access)
3. Compare responses against the expected answers — semantic match
4. Report: which answers passed, which failed, and why

## Test Reports

Reports are written to `<project>/.agentos/tests/reports/`. One file per test run.

Filename: `<test-name>_<ISO-date>.md` (e.g. `activation-recall-01_2026-05-19.md`)

Report format:

```markdown
# Test Report: <test-name>

- **Date**: YYYY-MM-DD
- **Target**: <project-name>
- **Result**: N/M PASS
- **Tokens**: total token consumption of the subagent
- **Tool calls**: number of tool calls made by the subagent
- **Duration**: wall-clock time in seconds

## Results

| # | Verdict | Detail |
|---|---------|--------|
| 1 | PASS/FAIL | brief explanation |
| ... | ... | ... |
```

## Writing Tests

- Keep prompts natural — the subagent should behave as it would in a real session
- Questions should be answerable from the index alone (after activation)
- Expected answers are reviewer hints, not grading keys — include enough context for the reviewer to judge correctness
- One test file per scenario — name files descriptively: `activation-recall-01.md`, `discovery-cascade-01.md`, etc.
