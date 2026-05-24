---
name: agentos-testground
description: "Testing subsystem for package skills. Load when running, designing, listing, or evaluating testground tests — behavioral tests that measure how agents use a package skill in a controlled project environment. Covers test format, runner isolation, trace capture, and behavior-tier evaluation."
---

# agentos-testground

`Package.Aux.Skill` for testground-based package skill testing.

A testground is a controlled project that tests how agents use a `Package.Skill`. It evaluates agent behavior — what the agent did, how it navigated, and what it produced — not just output correctness.

Any package skill can have a testground. The testground is a separate project folder that imports the package skill and contains test files.

## When To Load This Skill

- When running testground tests against a package skill
- When designing new tests or testground environments
- When evaluating a completed test run
- When listing available tests in a package

## Arguments

`Skill.Explicit.Args` — this skill needs data from the caller to operate.

- **Target package** (required) — which package skill to test. Determines where to find test files (`<package>/testing/`).
- **Testground** (required for run) — which controlled environment to execute from. A package may have a default testground.
- **Test name** (optional) — specific test to run. If omitted, list or run all.
- **Model** (optional) — which model to use for the tested agent.

Zero-arg behavior: the skill loads its orientation context. No operation is performed.

## Core Concepts

- **Testground** — a controlled project folder for testing a package skill. Has its own `AGENTS.md`, can control visible skills, fixture files, and task prompts.
- **Test file** — defines a subagent prompt, entry path, behavior tiers, and navigation trace expectations. Lives in `testing/` inside the testground.
- **Behavior tiers** — evaluation levels: minimal pass, expected behavior, above expected, overwork, failure. Measure what the agent did, not just what it produced.
- **Navigation trace** — the sequence of surfaces the agent loaded. Captured from the session transcript. Diagnostic for entry-path quality.
- **Runner isolation** — tests run as fresh CLI sessions from the testground folder, not as subagents of the current session. This gives authentic entry-path behavior.

## References

| Reference | Covers |
|---|---|
| `agentos-pkg/references/testground-format.md` | Test file format, behavior tiers, navigation trace, testground folder structure |
| `agentos-pkg/references/testground-runner.md` | How to run tests: CLI isolation, chatlas trace capture, evaluation procedure, test reports |

## Testground Discovery

Testgrounds are project folders whose purpose is testing a package skill. They follow the Agentos project model (`AGENTS.md`, optional index, `testing/` folder).

To find testgrounds, look for project folders with a `testing/` directory containing test files in the expected format.

## Compatibility

`agentos-index-test` is the deprecated standalone skill for index activation/recall tests. Its scope is absorbed by `agentos-testground` — existing index recall tests can migrate to testground format as tests with simpler behavior tiers.
