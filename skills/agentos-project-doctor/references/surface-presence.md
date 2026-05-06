# Surface Presence Checks

Detect observed Agentos surfaces.

## Surfaces

- `AGENTS.md`
- `.agentos/`
- `notes/index/`
- `notes/live/`
- `skills/`
- `dev/live/`

## Rules

- Surface presence is evidence, not an automatic pass/fail.
- Compare observed surfaces to declared adoption and target context.
- `.agentos/project.json` is the mandatory identity surface.
- `AGENTS.md` should normally exist at the project root.
- Other Agentos surfaces are optional by capability adoption.
- Absence alone is not a warning for optional surfaces.
- Warn when a project appears to use a capability through a near-standard, overlapping, or off-protocol alternative instead of the canonical Agentos surface.
- Do not title findings as missing optional surfaces. Title the concrete diagnosis instead.

## Optional Surface Decision Table

Use this table for optional surfaces such as `notes/index/`, `notes/live/`, `skills/`, and `dev/live/`:

| Capability evidence | Canonical surface | Outcome |
|---|---|---|
| absent | absent | `skip` |
| absent | present | evaluate canonical surface protocol |
| present through near-standard alternative | absent or conflicting | `warn` |
| present | present | evaluate canonical surface protocol |

## Report Evidence

List checked surfaces in the summary.

For each important missing surface that actually matters in context, include:

- expected surface
- why it was expected
- observed related evidence
