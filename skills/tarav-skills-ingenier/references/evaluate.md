# Skill.Evaluation.Operation.Module

Use this module to pressure-test an existing or newly developed skill without changing it.

## Evaluation Pass

1. Derive 2–3 realistic calls from the skill's trigger boundary and public routes, including one adjacent case that should not select it when useful.
2. Check explicit flags, semantic discovery, required argument resolution, aliases, defaults, module selection, and command availability that matter to those calls.
3. Check that loaded context is proportionate: the driver orients, selected modules supply depth, and unrelated modules remain unloaded.
4. Check the promised output shape and mutation boundary.
5. For substantial or high-consequence package skills, route to `tarav-testground` for controlled traces and behavioral evaluation rather than simulating confidence from prose review alone.

Return the scenarios, expected route, observed or reasoned behavior, and remaining POIs. This module is read-only; fixes route back through `Skill.Develop.Workflow.Module`.
