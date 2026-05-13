# Install — Alias.Skills for agentos-index

Instructions for creating the `Alias.Skills` that export specific operations from the `agentos-index` `Skill.Package`.

## Alias.Skills to create

Each alias skill is a directory under `skills/` with a single `SKILL.md` that:
- has a short intro (what it does, when to use it)
- points to the relevant `agentos-index/references/` file for full behavior

### agentos-index-activate

- **role**: bootstrap the index runtime for a session
- **reference**: `agentos-index/references/eval-loop.md` (Index.Activation section)
- **key constraint**: must inject enough inline guidance (detection rules, eval loop summary, footer format) that the agent can operate without loading more skills immediately
- **size target**: ~30 lines

### agentos-index-trigger

- **role**: lightweight always-on detection of Dotted.Names during conversation
- **reference**: `agentos-index/references/eval-loop.md` (Index.Call.Trigger + Index.Eval.Loop)
- **key constraint**: ultra-minimal prompt footprint — this is loaded in every conversation where the index is active
- **size target**: ~20-40 lines

### agentos-index-resolution

- **role**: resolve approximate or unknown names against the index
- **reference**: `agentos-index/references/gating.md` (Index.Name.Resolution section)
- **key constraint**: fully agentic for MVP — no special tooling, agent judgment + index scanning
- **size target**: ~40-60 lines

### agentos-index-writer

- **role**: user-gated write path to the index
- **reference**: `agentos-index/references/gating.md` (User.Gated.Index + Write Loop)
- **key constraint**: two explicit gates (Write.Trigger.Gated + Content.Verbatim.Gated), interactive per-block loop
- **size target**: ~50-70 lines

### agentos-index-doctor

- **role**: index health review and diagnosis
- **reference**: `agentos-index/references/maintenance.md` (Maintenance Model + Index.CLI)
- **key constraint**: diagnosis-first, reports issues with evidence, does not auto-fix
- **size target**: ~40-60 lines

### agentos-index-appendix-base

- **role**: define and operate the appendix surface protocol for `notes/appendix/`
- **reference**: `agentos-index/references/appendix.md`
- **key constraint**: appendix is stable opt-in depth, not a parallel concept authority
- **size target**: ~70-110 lines

## Regeneration

These alias skills are derived artifacts. If the reference files change, the alias skills can be regenerated from this install.md.
