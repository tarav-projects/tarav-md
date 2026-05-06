# Project Identity Checks

Check whether the target should be treated as `Agentos.Project:<target>`.

## Deterministic Checks

- Check for `.agentos/project.json`.
- If present, validate that it is parseable JSON.
- Check for `.agentos/config.json` only as config evidence; it does not define project identity.

## Agentic Judgment

`.agentos/project.json` is mandatory for any target being evaluated as `Agentos.Project:<target>`.

If the user asks for an Agentos project doctor pass, treat the target as an `Agentos.Project` target unless the user explicitly asks for a looser adoption scan. In that mode, missing `.agentos/project.json` is a failure.

For a loose adoption scan, missing `.agentos/project.json` is still a finding when the target claims or appears to adopt Agentos.

Signals that the target may be adopting Agentos:

- `AGENTS.md`
- `notes/index/`
- `notes/live/`
- `skills/`
- `.agentos/config.json`
- references to `Agentos.Stack`, `Agentos.Project`, or Agentos workflow surfaces

## Expected Findings

- `fail`: `.agentos/project.json` is missing from a target evaluated as `Agentos.Project:<target>`.
- `fail`: invalid `.agentos/project.json` in a target claiming to be an `Agentos.Project`.
- `warn`: Agentos surfaces exist but `.agentos/project.json` is missing.
- `info`: no identity marker and only weak adoption evidence.
- `pass`: `.agentos/project.json` exists and is parseable.
