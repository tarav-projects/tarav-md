---
name: agentos-index-test
description: "Run index activation and runtime tests for any project's index skill. Spawns subagents with test prompts and evaluates responses against expected answers."
---

# agentos-index-test

Test the index activation and runtime behavior of a project's `Project.Index.Skill`.

This is an `Alias.Skill` of the `agentos-index` `Skill.Package`.

Each project ships test files in its `<Project.Index.Skill>/testing/` folder. This skill runs those tests using the master agent + subagent pattern.

For the full testing mechanism: `agentos-index/references/test-system.md`

## Arguments

All subcommands accept these arguments as natural language in the invocation:

- **`on <project>`** (required) — the target project to test. Can be a project name, a path, or anything the agent can resolve to an Agentos project root.
  - Resolution: use `agentos projects list --root <search-path>` to discover projects, or `agentos projects test-resolve --project <name> --project-base <path>` to verify a match.
  - If the project cannot be resolved unambiguously, **fail and explain** — do not guess.
- **`[test-name]`** (optional, `run` only) — the specific test file to run. If omitted, run all tests.

Examples:

```
agentos-index-test list on agentos-md
agentos-index-test run activation-recall-01 on agentos-md
agentos-index-test run on agentos-md
```

## Subcommands

### `agentos-index-test list`

List all available tests in the target project's index skill `testing/` folder. For each test file:

1. Read the file
2. Show the test name (from `# Test:` heading)
3. Show how many questions it contains
4. Show a one-line summary of what it tests (from context — activation recall, discovery cascade, etc.)

Output format:

```
Tests in <Project.Index.Skill>/testing/:

  activation-recall-01.md
    "activation-recall-01" — 5 questions — tests basic index recall after activation

  (more tests...)

Total: N tests
```

### `agentos-index-test run [test-name]`

Run one or all tests.

1. Resolve the target project
2. Locate test files in `<Project.Index.Skill>/testing/`
3. If `test-name` is given, run only that file — otherwise run all
4. For each test file:
   - Extract the **Subagent Prompt** section
   - Spawn a subagent with that prompt
   - Collect the subagent's structured response
5. Evaluate each response against the **Expected Answers** section — semantic match, not verbatim
6. Write a test report to `<project>/.agentos/tests/reports/`
7. Report results to the user

### After Testing

- Report a summary: total tests, pass count, fail count
- For failures, include the subagent's answer and explain why it didn't match
- If activation itself failed, report that separately — it blocks all downstream questions
