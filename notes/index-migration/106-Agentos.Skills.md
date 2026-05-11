# Agentos.Skills

`Agentos.Skills` defines skill selection, routing, and import behavior for Agentos projects.

It is the contract between global routing config, project-local profile selection, source expansion, selected skills, and imported skill depots.

## Core Terms

- `source`: a direct skill root or package-like expansion that contributes discoverable skills
- `source entry`: an object in a profile, package, or export package that resolves one source contribution
- `project-backed source`: a global source whose root is an `Agentos.Project`
- `export package`: a named skill package published by a project-backed source
- `profile`: an ordered selection of sources plus one or more local depots
- `depot`: a project-local directory where imported skill symlinks are materialized
- `selected skills`: the catalog computed from the resolved profile before depot sync
- `imported skills`: selected skills after import syncs depots

## Project Boundary

`agentos skills ...` is a project command and uses `Agentos.Project` targeting.

The resolved project target must already be an existing project when the command needs project-local depots or config.

Local skill depots do not define project existence by themselves.

## Source Model

A source is one of:

- direct path source: `{ "path": "/repo/skills" }`
- project-backed source: `{ "project": "/repo" }`
- package source: `{ "package": [...] }`

Project-backed sources scan `<project>/skills` and may publish export packages from `<project>/.agentos/config.json`.

Direct path sources point directly at a directory containing skill folders. This is useful when the markdown skill surface exists outside an initialized `Agentos.Project`.

Current migration example:

- global `agentos` source points directly at `agentos-md/skills`
- this avoids requiring `agentos-md` to be initialized as an `Agentos.Project` before its skill surface can be imported

## Profile Resolution

Profile selection resolves in this order:

- local `.agentos/config.json` override at `skills.routing.profile`
- global `skills.routing.default_profile`
- hardcoded default

Profiles are defined in global config under `skills.routing.profiles`.

Registry sources are defined once in global config under `skills.routing.sources`.

## Import Model

The selected catalog is config-derived. Importing materializes the selected skills into configured depots as managed symlinks.

Command roles:

- `list` previews selected skills
- `path` previews load paths
- `import` syncs selected skills into depots
- `import --force` rebuilds the managed symlink layer without deleting conflicting non-symlink entries
- `status` compares depots against selected skills

## Usage.Surface

`Usage.Surface` is the usage-useful subset of `Public.Surface`: the surfaces that help external agents and humans understand how to use a project. It includes skills, CLI help, index notes, and other documentation surfaces.

## Usage.Skill

`Usage.Skill` is a special-purpose, usage-centric skill designed primarily as documentation. Skills exist on a spectrum of how usage-centric they were designed to be; a `Usage.Skill` is at the documentation end.

- It is an independent documentation surface, not the design SSOT.
- Its hard facts derive from `Agentos.Index.Notes`.
- No project-design-relevant fact should live only in a `Usage.Skill`.
- It may organize usage around practical questions, workflows, examples, commands, and safe operating boundaries rather than mirroring the index structure.
- It can explain, summarize, and compile index truth for practical use.

The master `Usage.Skill` of a project coordinates and curates its `Usage.Surface`. It routes to whichever surface best answers a given question: skills, CLI help, or index notes. It is the opinionated entry point for external agents.

## Boundaries

`Agentos.Skills` is not:

- a bootstrap skill
- a compatibility layer for arbitrary skill discovery
- a global public skill dump
- direct discovery from raw source roots during normal skill loading

## Related Concepts

- `Agentos.Project`
- `Usage.Skill`
- `Public.Surface`
- `Md.Surface`
- `Project.CLI`

## Legacy Source

Promoted from `../live/migrated-agentos-index/005-Agentos.Skills.md`.
