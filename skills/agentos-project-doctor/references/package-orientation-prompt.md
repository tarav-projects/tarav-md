# Package Orientation Prompt Check

Check whether the project's `AGENTS.md` prompts agents to load the package-root orientation skill at the beginning of a session.

## Why

The package root skill is the workflow-neutral entry point into the project's agentic package surface. An agent arriving in the project should be directed to load it early so it understands the relevant package before acting.

## Check

Look for a note or instruction in the project root `AGENTS.md` that tells agents to load the package root, such as `agentos-pkg`, at session start.

Acceptable forms include:

- An explicit instruction to load the package-root skill
- A reference to the package orientation surface with guidance to use it for orientation

The prompt does not need to use exact wording; any clear direction to load the package orientation surface counts.

## Expected Findings

- `pass`: `AGENTS.md` contains a prompt to load the package-root orientation skill.
- `warn`: `AGENTS.md` exists but does not mention package-root orientation.
- `skip`: the project does not appear to adopt Agentos skills, or `AGENTS.md` absence has already been reported by the surface-presence check.
