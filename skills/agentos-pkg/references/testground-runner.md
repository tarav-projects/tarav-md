# Testground Runner

Reference for running testground tests, capturing traces, and evaluating results.

## Runner Model

Testground tests run as isolated CLI sessions, not as subagents of the current session.

Why isolation matters:
- The tested agent gets only the testground's `AGENTS.md` and skill registry — no inherited context from the parent session.
- The entry path is authentic: the agent discovers the package skill the same way a real user's agent would.
- The session transcript is a clean, inspectable artifact.

## Running A Test

### 1. Launch

From the testground folder, start a fresh CLI session with the test prompt:

```bash
cd <testground-folder>
claude --model <model> -p "<subagent prompt from test file>"
```

Model selection:
- Default to a small/cheap model (Haiku-class for Claude, mini-class for others).
- Record the actual model used in the run log.
- Running the same test across models reveals model-dependent behavior differences.

### 2. Capture Trace

After the session completes, use chatlas to find and read the session transcript:

```bash
agentos chatlas query <selector>
agentos chatlas views inline <session-id>
```

The inline transcript contains the full tool call sequence — which files were read, in what order, and what the agent produced. This is the mechanical navigation trace.

### 3. Evaluate

Compare the session against the test's behavior tiers:

- Which tier does the agent's behavior match?
- What was the navigation trace? (from the transcript, not self-report)
- Was the cost proportional? (tool calls, tokens, duration)
- Any unexpected behaviors not covered by existing tiers?

### 4. Record

Write a run log entry in the test file's `## Run Log` section, or in a separate report file at `<testground>/.agentos/tests/reports/`.

## Run Log Format

Each run should record:

```markdown
### Run <N> — <date>

- **Model**: <model-id>
- **Tier**: <minimal-pass | expected | above-expected | overwork | failure>
- **Trace**: <surface loading sequence>
- **Tool calls**: <count>
- **Tokens**: <total>
- **Notes**: <unexpected behaviors, new failure modes, test enrichment ideas>
```

## Test Reports

Reports are written to `<testground>/.agentos/tests/reports/`.

Filename: `<test-name>_<ISO-date>.md`

Report format:

```markdown
# Test Report: <test-name>

- **Date**: YYYY-MM-DD
- **Target**: <package-skill>
- **Model**: <model-id>
- **Tier**: <result tier>
- **Tokens**: total token consumption
- **Tool calls**: number of tool calls
- **Duration**: wall-clock time in seconds

## Navigation Trace

<ordered list of surfaces loaded>

## Evaluation

<tier justification, unexpected behaviors, enrichment notes>
```

## Multiple Runs

Single runs are noisy. When evaluating a package skill's entry-path quality:

- Run the same test multiple times with the same model to check consistency.
- Run across different models to check model-dependent behavior.
- Accumulate run logs to build a reliability picture over time.

## Evaluator Role

The evaluator can be a human or an agent. When using an agent as evaluator:

- Give the evaluator the test file (with behavior tiers) and the session transcript.
- The evaluator should not have participated in the test run.
- The evaluator judges the tier match and writes the report.
