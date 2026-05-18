# Install — Alias.Skills for agentos-index

Instructions for creating the `Alias.Skills` that export specific operations from the `agentos-index` `Skill.Package`.

## Alias.Skills to create

Each alias skill is a directory under `skills/` with a single `SKILL.md` that:
- has a short intro (what it does, when to use it)
- points to the relevant `agentos-index/references/` file for full behavior

### agentos-index-activate

- **role**: bootstrap the index runtime for a session
- **reference**: `agentos-index/references/runtime.md` (load-runtime sequence)
- **key constraint**: delegates to runtime.md bootstrap — minimal inline content
- **size target**: ~30 lines

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

## Regeneration

These alias skills are derived artifacts. If the reference files change, the alias skills can be regenerated from this install.md.
