# agentos-skillware --dev (authoring)

Use this module when writing or restructuring `.skw.md` src: deciding the module graph, declaring imports, and crafting derivations. Syntax lives in `references/lang.md`; this module is the discipline.

## Graph Discipline

- declare an import only for a **real span-level relation** — a section whose content is a transformation (`derived`) or duplication (`copy`) of another surface
- one-line cross-references (`see references/type.md`, a `Dotted.Name` mention mid-sentence) are `Inline.Relatedness` — they stay plain prose, never forced into recipes
- no decorative imports: a copy that duplicates nothing real, or a derived whose "rule" is just a citation, adds maintenance surface without automating anything
- the honest graph is the payoff: when a source changes, `check` flags exactly the sections that can actually go stale — nothing more, nothing less

## Roots And Consumers

- a **root module** is recipe-free passthrough src: canonical home of its content, imported by others, importing nothing
- a **derived consumer** carries recipes: its flagged sections restate, adapt, or digest other surfaces
- keep each span's canonical home unambiguous — content lives in exactly one root; consumers project it
- mixed files are normal: hand sections and recipe sections interleave freely; the recipe governs only its own section

## Crafting The Intent

The `intent:` is the `Derivation.Rule` context — written so a cold agent can re-derive the body from the `from:` targets alone:

- name the transformation: *adapt X to scope Y*, *digest X to one paragraph*, *restate X as a checklist*
- state what must stay aligned and what must not happen (*do not collapse into a copy of search*)
- keep it a rule, not a description of the current body — the body is the rule's current solution, not its definition
- a weak derivation (mostly restating) is acceptable when parity or fidelity demands it — say so in the intent

## Division Of Labor

- the CPU materializes `copy` bindings and detects drift; the agent performs derivations — and performs them **in src**, where the `Derivation.Rule` and its current solution live side by side
- per import, the system records the target (by durable address), the binding, and the context, and re-runs the check or the materialization on demand — `lock.json` holds the record
- targets are addressed by legal block names: `Dotted.Name`s for index blocks, locators for files and regions
- the more imported a module's content, the more its maintenance automates — imported spans re-materialize, while original content and the seams where it meets them stay manual

## Workflow

1. Write or edit the src (`.skw.md`) — never the compiled target.
2. `agentos skillware build --skill <path>` — copy refresh, compile, lock, AGENTS.md stamp.
3. `agentos skillware check --skill <path>` — confirm all-ok; interpret verdicts per `references/check.md`.
4. For a gated package, src edits still pass the package's own edit gates before landing.
