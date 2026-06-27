# Derivation Manifests

A derivation manifest declares how derived content stays in sync with its sources. It is the agentic core of the `Skill.Package.Builder`.

## What A Manifest Is

- a `Kernel.Note` of `Derivation.Rule` blocks, living on the `Skill.Build.Surface` under `build/derivation/`
- placement is free — the folder is the unit, not the file; the builder loads all manifests and runs every rule
- group rules however helps: by target file, by source concept, by subsystem

## What A Rule Is

A rule is a soft mini-`Kernel.Block` — `Index.Block` philosophy, not a character-precise spec. It carries:

- an **op** tag: `copy` (verbatim) · `projection` (a structural part of the source) · `transform` (reshaped by a stated intent)
- the **source**: a `Dotted.Name` block, or a file span
- the **target**: which runnable file, with a soft locator-hint (where it sits, and why)
- the **context**: enough for a smart builder to understand and maintain the relation
- **on drift**: what to preserve when reconciling

The builder is smart: the hint lowers its search cost, it does not pin coordinates. Most of the time it reads the file and realizes the situation.

## Worked Example

`build/derivation/catalog.md`:

```md
## Catalog/Hard.Evidence.Example
- `projection`: the `Hard.Evidence` positive example in `references/index-block-catalog.md` is the fundamentals of the `Hard.Evidence` index block
- the `### meta` section is not part of the example — it shows the block's body
- placement hint: first example under `## Positive` / `### Definition-first, atomic lines` (~line 14)
- why it exists: it is the canonical "imitate this" example — it must not drift from the live definition
- on drift: refresh the example to the current fundamentals; leave the surrounding "Why it works" notes intact
```

- a `--check` run reads the `Hard.Evidence` block, compares it to the catalog example, and reports drift.
- a `--build` run refreshes the example to the current fundamentals, leaving the surrounding notes intact.

## Discipline

- never write addressing markers into the runnable surface — the locator lives here, on the build side
- one owner per target span — no two rules derive the same span
