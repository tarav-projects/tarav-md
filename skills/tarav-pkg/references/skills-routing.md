# Agentos Skills Routing

Reference for agents that need to inspect, configure, or sync project-local skills through the `agentos skills` command.

## Model

Agentos skills routing computes a selected skill catalog for an Agentos project, then imports that catalog into one or more project-local depots.

- A **skill source** contributes discoverable skill directories. A skill directory is any directory containing `SKILL.md`.
- A **profile** is an ordered list of sources plus configured depots.
- A **selected catalog** is the profile-resolved list before import.
- An **imported catalog** is the selected catalog after `agentos skills import` materializes depot symlinks.
- A **depot** is a project-local load directory, usually `.agents/skills` and `.claude/skills`.

The CLI command is plural: `agentos skills`.

## Project Targeting

Skills commands are project-aware and require explicit project targeting.

Use one of:

```bash
agentos skills list --project .
agentos skills status --project .
agentos skills import --project .
agentos skills path <skill-name> --project .
agentos skills path --depot --project .
```

Because `--project` accepts an optional value, prefer putting skill names before `--project .` for `path`:

```bash
agentos skills path tarav-pkg --project .
```

## Configuration

Global routing lives at:

```text
~/.agentos/config.json
```

Project-local routing selection lives at:

```text
<project>/.agentos/config.json
```

Profile resolution order:

```text
project-local .agentos/config.json profile
global skills.routing.default_profile
hardcoded default profile name
```

Project-local config usually selects a global profile:

```json
{
  "class": "agentos.project.config",
  "schema_version": 1,
  "skills": {
    "routing": {
      "profile": "my-profile"
    }
  }
}
```

## Source Types

Routing supports three source forms.

Direct skill root scan:

```json
{
  "path": "/absolute/or/relative/path/to/skills"
}
```

Project-backed scan:

```json
{
  "project": "/path/to/agentos-project"
}
```

Project-backed sources scan the project's `skills/` directory and require the target to be an Agentos project.

Package source:

```json
{
  "package": [
    { "name": "agentos" },
    { "name": "chatlas" }
  ]
}
```

Package sources are source bundles. They let a profile include a named group of sources without duplicating the full list.

## Common Pattern: Default Plus Project Skill

To add a project package skill while preserving the normal default catalog, add a global source and profile:

```json
{
  "skills": {
    "routing": {
      "sources": {
        "my-project": {
          "project": "/path/to/my-project-md"
        }
      },
      "profiles": {
        "my-project": {
          "sources": [
            { "name": "default" },
            { "name": "my-project" }
          ]
        }
      }
    }
  }
}
```

Then select that profile in the target project's `.agentos/config.json`.

There is no separate profile-inheritance field. Referencing the existing `default` package source first is the supported merge pattern.

## Skill Names

Discovered skill names come from directory names, with source-prefixing when needed.

- If the skill directory name equals the source name, the imported name is unchanged.
- If the skill directory name already starts with `<source>-`, the imported name is unchanged.
- Otherwise the imported name becomes `<source>-<skill-directory-name>`.

Example: a `miacad` source scanning `skills/miacad-pkg/` imports `miacad-pkg`, because the skill directory already starts with `miacad-`.

## Filters

Sources can include `include` and `exclude` arrays to limit selected skills:

```json
{
  "name": "agentos",
  "include": ["tarav-pkg", "tarav-hugentics"]
}
```

Filter entries may reference either the raw skill directory name or the mapped imported name. Unknown filter names are errors.

## Import Modes

Default import mode is `depot-linking`:

```bash
agentos skills import --project .
```

This creates or updates project depot links so they point at a shared global depot under:

```text
~/.agentos/skills/depots/
```

Alternative mode:

```bash
agentos skills import --mode flat-linking --project .
```

`flat-linking` writes per-skill symlinks directly into each project depot.

Use `--force` only when replacing managed symlinks intentionally:

```bash
agentos skills import --force --project .
```

Conflicting non-symlink entries still error.

## Operational Checks

Preview selected skills without changing depots:

```bash
agentos skills list --project .
agentos skills list --json --project .
```

Inspect current depot state:

```bash
agentos skills status --project .
agentos skills status --json --project .
```

Resolve depot roots:

```bash
agentos skills path --depot --project .
```

Resolve a skill's project-local load paths:

```bash
agentos skills path tarav-pkg --project .
```

After editing routing config, run:

```bash
agentos skills list --project .
agentos skills import --project .
agentos skills status --project .
```

Treat `status` as clean only when every configured depot reports no missing, broken, unsynced, conflicting, or extra entries.
