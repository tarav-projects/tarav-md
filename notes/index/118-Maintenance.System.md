# Maintenance.System

## Maintenance.System

- `Maintenance.System` defines how a project surface is diagnosed over time
- diagnosis-first, not fix-first — report issues with evidence, then the user decides on follow-up
- checks can be agentic (judgment-based), CLI-supported (deterministic), or mixed
- usually has two aligned surfaces: a doctor skill for agentic diagnosis, a project CLI for deterministic checks
- parameterized: `Maintenance.System:Agentos` is the Agentos instance
- reports must be evidence-based — the agent declares the evidence for each finding
    - suggestions without evidence are valid, but must be explicitly marked as such
- boundary: finds and reports issues — not primarily a fixer, progress tracker, or background automation
    - fixes are separate, explicit workflows — maintenance findings often require design judgment
