# Skill.Package

- a reusable packaging pattern for complex skill subsystems
- one `Main.Skill` with reference files, plus lightweight `Alias.Skills` as exported interfaces
- the main skill is self-contained and complete — loading it alone should be enough to operate the full system
- `Alias.Skills` are cheap entry points that hook into the skill routing system

****

## Structure

- the main skill contains all design truth and operational specs in `references/`
- `Alias.Skills` have a short intro (what it does, when to use it) then point to the relevant reference file
- `references/install.md` contains instructions for creating the `Alias.Skills` — making them reproducible

```
<package-name>/
  SKILL.md              ← Main.Skill (the full system)
  references/
    <topic-a>.md
    <topic-b>.md
    ...
    install.md          ← instructions for creating Alias.Skills

<package-name>-<alias-a>/
  SKILL.md              ← Alias.Skill: short intro + pointer to references/<topic-a>.md

<package-name>-<alias-b>/
  SKILL.md              ← Alias.Skill: short intro + pointer to references/<topic-b>.md
```

****

## Alias.Skill

- a lightweight skill that exists as an exported interface of a `Skill.Package`
- has a short introduction: what it does, when to use it
- points to the relevant `Main.Skill` reference file for the actual behavior
- exists because the skill system needs named, loadable entry points for specific operations
- is a derived artifact — can be auto-generated or regenerated from `install.md`

****

## Properties

- the `Main.Skill` is the primary source — `Alias.Skills` are derived
- any complex subsystem can be packaged this way
- the pattern separates completeness (main skill) from discoverability (aliases)
- `install.md` makes alias creation reproducible by agents or humans

****

## Canonical Example

`agentos-index` is a `Skill.Package`:

- `agentos-index` is the `Main.Skill`
- `agentos-index-activate`, `agentos-index-trigger`, `agentos-index-resolution`, `agentos-index-writer`, `agentos-index-doctor` are `Alias.Skills`
- each `Alias.Skill` points to the relevant `agentos-index/references/` file

### index

- findability: skill packaging, skill family, main skill, alias skills, skill bundle, skill export
- related: `Agentos.Skills`, `Main.Skill`, `Alias.Skill`
