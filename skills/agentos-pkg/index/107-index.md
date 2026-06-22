> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Agentos.Skillware

- `Agentos.Skillware` is the discipline of treating skills as software — the skill is the unit of software for agents.
- "as software" means the artifacts agents run gain engineering structure — modules, dependencies, builds, versions, lineage — so they can be reused and evolved rather than written once and forked.
- a discipline realized by capabilities, not a single mechanism — it names the stance; specific members implement it.

### meta

- `Explicit.Namespace`; members: `Skill.Module`, `Skill.Runnable.Surface`, `Skill.Build.Surface`, `Derivation.Rule`, `Derived.Content`, `Module.Dependency.Management`, `Derived.Module`, `Derivation.Manifest`, `Derivation.Surface.Arch`, `Semantic.Router`, `Usage.Pattern.Routing`.

****

## Skill.Runnable.Surface

- `Skill.Runnable.Surface` is a surface whose purpose is to be run — loaded into agent context to do work; it carries only the executable substance.
- the system keeps it free of non-runnable artifacts, so nothing obscures or dilutes what runs.
- forced by context being executable — anything on it is read into context and shapes the run; non-runnable artifacts there are not inert, they interfere.

****

## Skill.Build.Surface

- `Skill.Build.Surface` is the complement of `Skill.Runnable.Surface` — it holds the artifacts that produce and maintain runnable content, and is never loaded at run time.
- it is the home for everything kept off the runnable surface: derivation context, dependency declarations, lineage, dev material.
- never run, it carries no "stay clean" constraint — an unconstrained workspace; that freedom is what the two-surface split buys.

****

## Derivation.Rule

- `Derivation.Rule` is the relation `Dependencies + Context → Derived` — the unit that produces a piece of derived content from declared dependencies, interpreted through a context.
- `Context` is everything informing the derivation other than the declared dependencies — case by case, from implicit (the derived surface itself + ambient knowledge) to explicit (written down).
- both dependencies and context span **inline + external** — carried inline in the derived surface, or external on a build surface; whatever isn't inline is written externally.
- run **forward** it (re)generates the derived; run as a **check** it answers the drift question — does the current derived still match what its dependencies + context would now produce?
- the check is the payoff: maintenance becomes a query the system runs, not vigilance the user keeps — and maintenance is derivation's main cost.

****

## Derived.Content

- `Derived.Content` is the *Derived* side of a `Derivation.Rule` — content produced from declared dependencies and a context, a projection of those sources rather than authored standalone.
- granular — any span of a module can be `Derived.Content`; the rest is original content, and the original/derived ratio is just how much of a module is derived.
- its tie to its sources automates drift detection and aids regeneration — drift is caught when sources change; regeneration is supported by the kept context.

****

## Module.Dependency.Management

- `Module.Dependency.Management` is the part of the Skillware module model that maintains a module's `Derivation.Rule`s — tracking dependencies and the context so derived content can be drift-checked and regenerated.
- it records, per derived span, the dependencies (by durable address) and the context, and re-runs the rule on demand.
- the more derived a module, the more its maintenance automates — derived spans re-project, while original content and the seams where it meets derived content stay manual.
- dependencies are addressed by the in-place linking mechanism — `Dotted.Names` for blocks, `Chat.Ref`/`Chat.Grounding` for chat fallback dependencies.

****

## Derived.Module

- `Derived.Module` is a `Skill.Module` whose content is mostly `Derived.Content` — the high-derivation pole.
- source-agnostic — its sources may be index blocks or other modules; derived-ness is the ratio, not the surface.
- the more derived it is, the more its maintenance automates — largely a projection of its sources, re-derived on change, with human work only at the seam with original content.

****

## Derivation.Surface.Arch

- `Derivation.Surface.Arch` is the layout of a skill's derivation surface — a `derivation/` folder (a `Skill.Build.Surface`) holding explicit `Derivation.Manifest`s, kept off the `Skill.Runnable.Surface`.
- per-file mirror — `derivation/<name>.md` mirrors the derived file's name and is discovered implicitly (check if it exists); the default, no registry needed.
- `derivation/002-index.md` routes the surface — listing is cheap, so it lists every derivation and carries the multi-output/subsystem cases a 1:1 mirror can't express.
- discovery is convention-based — a maintainer or agent always knows where a derivation's context lives, like `Appendix.Discovery`.

****

## Derivation.Manifest

- `Derivation.Manifest` is the explicit artifact for a `Derivation.Rule` — it carries the parts of the rule (declared dependencies + external context) not already inline in the derived surface.
- it lives on the derivation surface (`Derivation.Surface.Arch`), a `Skill.Build.Surface` kept off the runnable surface.
- it names each dependency by a durable address and holds the external context, so a maintainer or agent can re-derive and drift-check from one known place.

****

## Semantic.Router

- `Semantic.Router` is a Skillware primitive: a key:value table where keys are natural-language situation descriptions and values are linked resources (a prompt, a `Skill.Module`, content, or another `Semantic.Router`).
- routing is semantic and agentic — the agent matches the live situation against the key descriptions and selects; keys must be discriminative.
- it offers options, not an order — the rows are an unordered set of choices, not a sequence; `None.Is.An.Option` is stated explicitly, so the agent may select nothing.
- it composes — a value can be another `Semantic.Router`, giving progressive, multi-level selection.

****

## Usage.Pattern.Routing

- `Usage.Pattern.Routing` is `Semantic.Router` routing whose rows are usage patterns — keys are usage situations, values are the response for each (knowledge/surfaces to load, what to produce).
- its keys are mined from real usage — chats, repeated questions, observed friction — so the routing grows cheaply and stays reality-weighted.
- it optimizes frequent or important situations (a hot path); an unmatched situation selects nothing and falls back to the package's general routing.
