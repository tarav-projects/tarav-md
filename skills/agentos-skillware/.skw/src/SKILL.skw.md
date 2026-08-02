> $kw: ^agentos-root-reachability --reachable-from @<agentos-pkg>/SKILL.md

---
name: agentos-skillware
description: "Workflow-neutral Package.Aux.Skill for the Skillware subsystem of agentos-pkg — skills developed as software, compiled from .skw/src sources. USE WHEN understanding Skillware, authoring or adopting .skw.md sources, building managed surfaces, maintaining edition history, or checking drift."
---

# agentos-skillware

Workflow-neutral `Package.Aux.Skill` for the Skillware subsystem — the center of all Skillware content: doctrine, language, authoring discipline, adoption, and toolchain operation.

This skill is the public Batchy router for Skillware work. `Batchy.Router` resolves explicit flags, the live situation, and declared defaults against the `Routing.Table` below, then loads only the selected `Skill.Module`s.

This is a `Batchy.Skill`. Load `agentos-batchy-skills` for the full convention.

- `-h` / `--help` prints usage and the public args without running.
- a written `--<flag>` is intentional run configuration and must be resolved as such.
- without an explicit route, conversational discovery remains available wherever the applicable row permits it.
- every non-help run with custom configuration prints its resolved configuration first (`Batchy.Skill.Banner`).

## What Skillware Is

> $kw: --derived
> --from Agentos.Skillware
> --from Index.Line
> --from Skw.Annotation
> --from Skw.Touched.Index
> --intent orientation blurb — restate the discipline block for a caller
> --cont meeting the subsystem cold; keep it to the stance, not the mechanics

- `Agentos.Skillware` is the discipline of treating skills as software — the skill is the unit of software for agents
- "as software" means the artifacts agents run gain engineering structure — modules, dependencies, builds, versions, lineage — so they are reused and evolved rather than written once and forked
- a development toolchain of builders and checkers, spanning agentic and `CPU.Impl` work, moves package maintenance off the human
- it is a discipline realized by capabilities, not a single mechanism — **skw**, the general annotation language and its backends, is the system realizing it; this skill carries the capabilities
- skw is the integration fabric: declared dependencies between project surfaces make maintenance and change propagation explicit
- touch is an orthogonal axis over skw objects; `Skw.Touched.Index` materializes grounded `Index.Line`s attached to `Skw.Annotation` instances without making every annotation touched

> $kw. end

## Skill.Arg.Section

Only external data consumed by the selected module is a `Skill.Arg`. Operation and selection flags belong to `Batchy.Router`.

### Skill.Arg::Main.Prompt
- the caller-supplied Skillware question, development request, or check focus consumed by the selected module
- required: false
- default: the caller's current explicit request or applicable conversation context
- help: "the question or task for the selected Skillware operation"
- examples: --about "how do derived recipes track staleness?", --dev "adopt agentos-batchy-skills"

### Skill.Arg::Target.Skill
- the package skill whose managed surfaces are being developed or checked
- required: false
- default: the skill resolved from the current project and request when unique
- flags: --skill
- help: "the package skill to develop or check"
- examples: --skill skills/agentos-hugentics

### Skill.Arg::Edition.History.Target
- one or more configured eligible files whose edition history should be maintained
- required: false
- flags: --target
- repeatable: true
- active only with: --edition-history
- help: "maintain edition history for an explicit configured file"
- examples: --edition-history --target src/example.py

## Batchy.Router

The public flags below configure the single running `Batchy.Router`. A trailing value binds `Skill.Arg::Main.Prompt`; data flags bind their named argument without independently selecting a module.

| Explicit configuration | Routed effect |
|---|---|
| `--about`, `--info`, `--doctrine` | contribute orientation routing through the doctrine and language rows |
| `--dev` | contribute development routing through the author, adopt, and build rows |
| `--edition-history` | select `references/edition-history-developer.md` |
| `--check` | select `references/check.md` |
| `--skill` | bind `Skill.Arg::Target.Skill` |
| `--target` | bind `Skill.Arg::Edition.History.Target` |
| `--random` | configure edition-history selection to choose one eligible file, preferring missing then incomplete history; mutually exclusive with `--target` |

## Routing.Table

This table may select the one or several modules needed by a composed request. Explicit operation flags constrain the applicable family; conversational discovery selects within that family or routes a clear unflagged call.

> $kw: ^skillware-router

> $kw: --when
When `--about`, `--info`, or `--doctrine` is supplied, or the caller is new to Skillware, needs its mental model, or asks what the system is, why two surfaces exist, or how derivation works.

> $kw: --then
Load `references/doctrine.md`; also load `references/lang.md` when the question requires exact syntax.

> $kw: --when
When the caller needs exact syntax: construct grammar, flags, owned ends, locator forms, `skw.json`, or compiler behavior.

> $kw: --then
Load `references/lang.md`.

> $kw: --when
When `--dev` is supplied or the caller is writing or restructuring src: deciding roots versus derived consumers, declaring imports, crafting an `--intent`, or judging whether a relation earns an import.

> $kw: --then
Load `references/author.md`.

> $kw: --when
When `--dev` is supplied with an adoption request, or the caller wants an existing hand-owned skill brought under Skillware management.

> $kw: --then
Load `references/adopt.md`.

> $kw: --when
When `--dev` is supplied with a build request, or the caller wants managed surfaces produced or refreshed or asks about the lock and build mechanics.

> $kw: --then
Load `references/build.md`.

> $kw: --when
When `--check` is supplied or the caller wants read-only drift inspection, POI interpretation, or prescriptions such as re-derive versus bless.

> $kw: --then
Load `references/check.md`.

> $kw: --when
When `--edition-history` is supplied, or the caller wants to recover, record, amend, inspect, or lint the chat sessions associated with managed-file Git editions.

> $kw: --then
Load `references/edition-history-developer.md`; require exactly one selection mode, `--target` or `--random`.

> $kw: --when
When the caller needs the canonical index concepts behind Skillware.

> $kw: --then
Load `agentos-pkg/design/107-design.md` under the `Agentos.Skillware` namespace.

> $kw. end

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

> $kw: --from Batchy.Router --from Batchy.Skill --from Batchy.Skill.Banner --from Package.Aux.Skill --from Routing.Table --from Skill.Arg --from Skill.Module
