# Import Manifests

An `Import.Manifest` declares a module's `Module.Import`s — the dependencies between a consumer surface and the targets it imports. It is the declaration layer of the `Skill.Package.Builder`.

## What A Manifest Is

- a `Kernel.Note` of import blocks, living flat on the `Skill.Build.Surface` as `build/<expanded-relative-path>-<file-name>-imports.md`
- one manifest per consuming module; the filename encodes the consumer with `-` joining path segments — `references/gr-survey.md` → `build/references-gr-survey-imports.md`
- naming ambiguity is a non-problem: resolution is by existence over the package tree; a genuinely ambiguous expansion is reported as a finding, not escaped around
- absence of a manifest means the module declares no imports

## What An Import Block Is

One `Kernel.Block` per import. The heading is the target — any legal block name (`Block.Naming.Schema`), including `@path` file locators with optional `#region`, and bare `Dotted.Name`s resolved in an index depot. Field lines:

- `binding:` — `pointer` | `copy` | `derived`
  - `pointer` — the consumer depends on the target existing; the check resolves it
  - `copy` — the target lands verbatim in the consumer; the check compares content
  - `derived` — a semantic transformation of the target lands in the consumer; checked agentically
- `lands:` — region locator in the consumer (e.g. `#Grounding Model`); omit for whole-file
- `context:` — `derived` only, free depth: the intent a smart builder needs to regenerate or judge the derived span

Blocks are extensible by adding lines; unknown lines read as context.

## Worked Example

`build/references-gr-survey-imports.md`:

```md
## @pkg/docs/craft.md#Selector Rules

- binding: copy
- lands: #Selector

## Concept.Beta

- binding: derived
- lands: #Loop
- context: compress the beta vocabulary into one table
```

- `agentos skills imports --package <pkg> [--depot <index-depot>]...` runs the CPU checks: `pointer` targets resolve, `copy` regions compare verbatim, `derived` is inventoried as `skipped-agentic`
- a `--build` run reconciles `derived` imports forward from their targets, guided by `context:`

## Discipline

- never write addressing markers into the runnable surface — the locators live here, on the build side
- one owner per landing span — no two imports land on the same span
- a failed check is a drift finding with no predefined winner — resolution is case-by-case; a particular workflow may set auto-regeneration as its own rule
