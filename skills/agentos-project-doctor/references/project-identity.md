# Project Identity Checks

Check whether the target should be treated as `Agentos.Project:<target>`.

## Deterministic Checks

- Check for `.agentos/project.json`.
- If present, validate that it is parseable JSON.
- Check for `.agentos/config.json` only as config evidence; it does not define project identity.

## Agentic Judgment

Missing `.agentos/project.json` is a finding only when the target claims or appears to adopt Agentos.

Signals that the target may be adopting Agentos:

- `AGENTS.md`
- `notes/index/`
- `notes/live/`
- `skills/`
- `.agentos/config.json`
- references to `Agentos.Stack`, `Agentos.Project`, or Agentos workflow surfaces

## Expected Findings

- `fail`: invalid `.agentos/project.json` in a target claiming to be an `Agentos.Project`.
- `warn`: Agentos surfaces exist but `.agentos/project.json` is missing.
- `info`: no identity marker and only weak adoption evidence.
- `pass`: `.agentos/project.json` exists and is parseable.

