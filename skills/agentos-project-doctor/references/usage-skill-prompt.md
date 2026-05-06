# Usage Skill Prompt Check

Check whether the project's `AGENTS.md` prompts agents to load the `agentos-usage` skill at the beginning of a session.

## Why

The `agentos-usage` skill is the curated entry point into the project's `Usage.Surface`. An agent arriving in the project should be directed to load it early so it understands the Agentos universe before acting.

## Check

Look for a note or instruction in the project root `AGENTS.md` that tells agents to load `agentos-usage` at session start.

Acceptable forms include:

- An explicit instruction to load the `agentos-usage` skill
- A reference to the skill by name with guidance to use it for orientation

The prompt does not need to use exact wording; any clear direction to load the skill counts.

## Expected Findings

- `pass`: `AGENTS.md` contains a prompt to load `agentos-usage`.
- `warn`: `AGENTS.md` exists but does not mention `agentos-usage`.
- `skip`: the project does not appear to adopt Agentos skills, or `AGENTS.md` absence has already been reported by the surface-presence check.
