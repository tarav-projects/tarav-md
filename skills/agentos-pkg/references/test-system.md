# Index Test System (Deprecated)

> **Deprecated** — this reference is superseded by `agentos-testground` and its references:
> - `references/testground-format.md` — test file format, behavior tiers, testground structure
> - `references/testground-runner.md` — runner isolation, trace capture, evaluation

The original master/subagent testing pattern is preserved below for compatibility with `activation-recall-01.md` and similar legacy tests.

---

## How It Works

- **Pattern**: master agent + subagent
- **Subagent**: receives a natural prompt — activates the index, performs tasks, responds in a structured format. The subagent does not know it is being tested.
- **Master agent (reviewer)**: evaluates the subagent's responses against expected answers using semantic match.

## Test File Format (Legacy)

Each test file contains:

1. **Subagent Prompt** — the full prompt to give the subagent. Includes activation instructions, tasks, and response format. Must be self-contained.
2. **Expected Answers** — hints for the reviewer. These are correct-answer guides, not exact strings. The reviewer judges whether the subagent's response captures the same meaning.

## Test Location

- tests live in the package's `testing/` folder
- each package ships its own test suite
- the testground provides the execution environment

## Running a Test

1. Spawn a fresh CLI session from the testground folder with the prompt from the test file
2. Capture the session (Chatlas can be used for transcript access)
3. Compare responses against the expected answers — semantic match
4. Report: which answers passed, which failed, and why
