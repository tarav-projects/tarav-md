> $kw: ^skill-develop-direct-loading-path --context-loading-path
> --step SKILL.md
> --loading-dep SKILL.skw.md^skills-ingenier-batchy-runtime-contract

# Skill.Develop.Workflow.Module

Use this module when the caller explicitly asks to create, apply, update, or upgrade a skill. The selected development route is authorization to mutate only the resolved target and its justified supporting stack.

## Preparation

1. Resolve one `Skill.Arg::Target.Skill` and read its owning `AGENTS.md` before editing.
2. Inspect the target, nearby maintained skills, applicable custom recommendations, and current worktree state.
3. Load `tarav-batchy-skills` for Agentos skill conventions.
4. When the target has `.skw/`, load `tarav-skillware`, read `.skw/AGENTS.md`, edit only `.skw/src/` for managed files, and identify the exact build/check commands before mutation.
5. Respect target-local approval gates and preserve unrelated user changes.

Do not force source mining into an obvious direct edit. Research only where it changes the valid implementation region.

## Implementation

- implement the smallest complete target stack justified by the request: `SKILL.md`, metadata, references, scripts, assets, tests, and Skillware configuration as applicable
- keep `Skill.Arg`s limited to external data; route operations and module selection through one `Batchy.Router`
- use the canonical Batchy runtime contract; on Skillware surfaces, materialize it mechanically from `tarav-batchy-skills`
- keep one canonical `Routing.Table`; derive runnable call and module views instead of maintaining parallel hand-written inventories
- declare `User.Command`s for explicit mid-workflow gates; do not use informal approval phrases to cross them
- keep modules addressable and selectively loaded; do not bury every behavior in the driver
- declare only real Skillware dependencies and write derivation intents as repeatable transformations
- update the authored source first, then build managed runnable surfaces; never repair a compiled target by hand

## Validation

Run validation in proportion to the change:

1. build managed surfaces when applicable; for Tarav Skillware use `tarav skw build --skill <package-root>`
2. run `tarav skw check --skill <package-root>` and inspect every POI rather than blessing automatically
3. run target-native validators or structural checks
4. exercise 2–3 representative calls for material routing changes; use `tarav-testground` when controlled behavioral evaluation is warranted
5. review the final diff for accidental scope, stale identities, broken paths, and generated/source disagreement

Report the changed surfaces, decisive design choices, sources used, validation results, and any remaining POIs. Do not commit unless separately instructed.

> $kw: --from Batchy.Router --from Routing.Table --from Skill.Arg --from User.Command
