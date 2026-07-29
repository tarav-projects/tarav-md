---
name: agentos-skillware
description: "Workflow-neutral Package.Aux.Skill for the Skillware subsystem of agentos-pkg — skills developed as software, compiled from .skw/src sources. USE WHEN understanding Skillware, authoring or adopting .skw.md sources, building managed surfaces, maintaining edition history, or checking drift."
---

# agentos-skillware

Workflow-neutral `Package.Aux.Skill` for the Skillware subsystem — the center of all Skillware content: doctrine, language, authoring discipline, adoption, and toolchain operation.

This skill is the public Batchy router for Skillware work. It orients the caller by default and routes `--about`, `--dev`, `--edition-history`, and `--check` into named `Skill.Module`s; the agent selects the concrete module from the live situation (`Semantic.Router`).

This is a `Batchy.Skill`. Load `agentos-batchy-skills` for the full convention.

- `-h` / `--help` prints usage and the public args without running.

## What Skillware Is

- `Agentos.Skillware` is the discipline of treating skills as software — the skill is the unit of software for agents
- "as software" means the artifacts agents run gain engineering structure — modules, dependencies, builds, versions, lineage — so they are reused and evolved rather than written once and forked
- a development toolchain of builders and checkers, spanning agentic and `CPU.Impl` work, moves package maintenance off the human
- it is a discipline realized by capabilities, not a single mechanism — **skw**, the general annotation language and its backends, is the system realizing it; this skill carries the capabilities
- skw is the integration fabric: declared dependencies between project surfaces make maintenance and change propagation explicit
- touch is an orthogonal axis over skw objects; `Skw.Touched.Index` materializes grounded `Index.Line`s attached to `Skw.Annotation` instances without making every annotation touched

## Skill.Arg.Section

### Skill.Arg::About
- orientation, doctrine, and language questions — the read-to-understand side
- required: false
- aliases: --info, --doctrine
- help: "explain Skillware: doctrine, model, recipe language, locators"
- examples: --about, --about "how do derived recipes track staleness?"

### Skill.Arg::Dev
- authoring, adoption, and building — the general write side
- required: false
- help: "do Skillware development: write src, adopt a skill, or build managed surfaces"
- examples: --dev "add a derived section to ground.skw.md", --dev "adopt agentos-batchy-skills"

### Skill.Arg::Edition.History
- recover, record, amend, inspect, or lint the chat-supported Git edition history of managed files
- required: false
- help: "maintain file edition/chat history through Git, Chatlas, and the Skillware service"
- activates: `references/edition-history-developer.md`
- requires exactly one selection mode: `--target` or `--random`
- examples: --edition-history --target src/example.py, --edition-history --random

### Skill.Arg::Edition.History.Target
- flag: --target
- active only with: --edition-history
- value: one configured eligible file; repeatable for an explicit batch
- required: false
- mutually exclusive with: --random
- help: "maintain edition history for an explicit configured file"

### Skill.Arg::Edition.History.Random
- flag: --random
- active only with: --edition-history
- value: none
- required: false
- mutually exclusive with: --target
- help: "select one configured file, preferring missing then incomplete history"

### Skill.Arg::Check
- read-only POI report over a skill's managed surfaces, with per-kind prescriptions
- required: false
- help: "check managed surfaces for drift and prescribe responses (read-only)"
- examples: --check --skill skills/agentos-hugentics, --check

## Router Table

| Situation | Module |
|---|---|
| When the caller is new to Skillware, needs the mental model, or asks conceptual questions — what the system is, why two surfaces, how derivation works | `references/doctrine.md` |
| When the caller needs exact syntax — the construct grammar, commands, arg lines, owned ends, locator forms, `skw.json`, what the compiler does | `references/lang.md` |
| When the caller is writing or restructuring src — deciding roots vs derived consumers, declaring imports, crafting an `--intent`, judging whether a relation earns an import | `references/author.md` |
| When the caller wants an existing hand-owned skill brought under Skillware management | `references/adopt.md` |
| When the caller wants surfaces produced or refreshed from src, or asks about the lock or the build's mechanics | `references/build.md` |
| When the caller wants drift inspected — what changed, what each POI kind means, what response each demands (re-derive vs bless); read-only | `references/check.md` |
| When `--edition-history` is supplied, or the caller wants to recover, record, amend, inspect, or lint the chat sessions associated with a managed file's Git editions | `references/edition-history-developer.md` |
| When the caller needs the canonical index concepts behind all of this | `agentos-pkg/design/107-design.md` (the `Agentos.Skillware` namespace) |

## Boundary

- this skill is the canonical home of Skillware content; the index (`agentos-pkg` 107) owns the concepts, this skill owns the operation
- `--check` never writes: it reports and prescribes; acting on the report is a follow-up into `--dev`
- writing to src for a gated package still follows that package's own edit gates — propose, get approval, then derive and rebuild
- self-containment: an agent loading this skill has everything needed to be a competent Skillware user

## Skill Modules

- `references/doctrine.md` — the model: skills as software, the two surfaces, imports, recipes, derivation
- `references/lang.md` — the operational spec: src surface, construct grammar, primitives, structural commands, locators, compilation, settings
- `references/author.md` — writing src: graph discipline, roots vs derived, `--intent` craft, division of labor
- `references/adopt.md` — converting an existing skill to Skillware management
- `references/build.md` — producing surfaces: build and status mechanics, the lock model
- `references/check.md` — drift: the POI kinds, prescriptions, the re-derive pass, the bless act
- `references/edition-history-developer.md` — recover and maintain file edition/chat associations through Git, Chatlas, and the edition-history service

## When To Load This Skill

- when working on or inside any `.skw/` build surface
- when authoring, building, checking, or adopting Skillware-managed skills
- when maintaining or auditing a managed file's edition/chat history
- when a `check` POI needs interpreting or acting on
- when discussing or modifying the Skillware system design itself
