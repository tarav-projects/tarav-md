# Usage Pattern: Package.Skill.Bootstrap

## Situation

The user wants to create a `Package.Skill` for a project or subsystem. They reference `agentos-pkg` as the framework and expect the agent to set up the canonical structure.

The agent discovers which sub-situation applies by inspecting the target:

### :New

The target has no existing Package.Skill structure. The agent creates it from scratch — SKILL.md, package.md, folder layout.

Signals: empty or minimal project folder, user says "start the Package.Skill for X", "create a Package.Skill."

### Package.Skill.Bootstrap:Migrate

- `Package.Skill.Bootstrap:Migrate` is the situation where an existing project with content adopts the Package.Skill framework
- the core constraint is content preservation — the agent relocates, it does not rewrite or drop
- conservative by default, not by rule: if something maps cleanly (existing index-like files → `index/`), do it now; if it's ambiguous or high friction, move it close and flag it for later
- the principle is: do the easy moves now, flag the hard moves for later
- the agent inventories existing content first: what files exist, what they contain, how they're currently organized
- content moves into the new folder structure by proximity to its natural place — not by full Package.Skill role assignment, which happens in later sessions
- the migration produces a live-note artifact (`*-pkgskill-migration.md`) that captures:
    - inventory of what existed and where it went
    - flagged items: content that doesn't fit cleanly, pending user decisions
    - post-migration TODO: what needs revisiting (role assignment, index population, driver refinement)
- the migration creates only the minimal scaffolding: `SKILL.md` as driver, `package.md` as router — no aux skills, no index pages, no references, unless they map trivially from existing content
- content that doesn't fit cleanly is never silently dropped — the agent flags it in the migration artifact and asks
- the migration may include structural changes beyond Package.Skill (splitting folders, renaming subprojects) — these should be scoped with the user, not assumed
- after migration the project is in an explicit non-stable state: it works (SKILL.md routes, content is accessible), but it is not refined — the migration artifact makes this explicit
- the project graduates to stable through subsequent sessions: driver refinement, design sessions, index population
- `SKILL.md` can temporarily link to the migration artifact as a "current state" reference until the package matures

Signals: existing project with scattered content, user says "migrate into Package.Skill framework", "restructure into Package.Skill", "setup Package.Skill — don't drop content."

## Expected Behavior Path

1. Load `agentos-pkg` SKILL.md for orientation.
2. Check index concepts: `Package.Skill`, `Package.Aux.Skill`, `Package.Skill.Router`, `Package.Skill.Install`.
3. Inspect the target project's current state.
   - If `:New` — note what exists (AGENTS.md? any skills? any notes?).
   - If `:Migrate` — inventory existing content that needs to be absorbed or relocated.
4. Ask about or confirm: package name, ownership boundary, which existing content gets absorbed vs. stays independent.
5. Propose the folder structure:
   - `SKILL.md` — workflow-neutral driver
   - `package.md` — full router
   - `index/` — if the package will have durable concepts
   - `references/` — if the package needs operational references
   - `usage-patterns/` — if the package has known hot paths
   - `testing/` — if the package needs behavioral tests
6. Wait for user approval before writing.
7. After structure is approved, create the files.
8. Common exit: user may launch a design session to populate the index.

### :Migrate additional steps

Between steps 3 and 5:
- Inventory all existing content.
- Classify by proximity: what maps cleanly into the Package.Skill structure, what is ambiguous, what needs user decision.
- Do the easy moves: relocate content that has an obvious natural place.
- Flag the hard moves: document ambiguous or high-friction items in the migration artifact.
- Create the migration artifact (`*-pkgskill-migration.md`) as a live note.
- Principle: relocate first, revise later. Do not rewrite content during migration.

## Key Signals

- "setup Package.Skill for X"
- "start the Package.Skill"
- "analogous to agentos-pkg"
- "migrate into Package.Skill framework"
- "create a Package.Skill"
- User references `agentos-pkg` concepts by name

## Observed Friction (from real sessions)

- **Agent confused about target location** — in `019e5277`, agent tried to implement elsewhere. User had to correct twice: "implement the framework HERE." The agent should confirm the target path early.
- **Content loss during migration** — in `52362a37`, user had to explicitly say "don't drop content." The `:Migrate` path must default to preserve-everything.
- **Agent assumes agentos-pkg structure verbatim** — each project has its own needs. The agent should propose structure based on what the project actually has, not copy agentos-pkg's layout 1:1.
- **Bootstrap → design-session transition** — in 3/6 sessions, user immediately launched a design session after bootstrap. The agent should recognize this as a natural next step but not pre-empt it.

## Related Patterns

- `Design.Session.Launch` — often the next step after bootstrap completes
- `Index.Block.Authoring` — populating the new package's index
- `Package.Skill.Driver.Refinement` — improving the SKILL.md after initial bootstrap

## Source Sessions

- `f870a478` — Chatlas Package.Skill bootstrap (:New, then design session)
- `52362a37` — Simuleos Package.Skill bootstrap (:Migrate, with restructuring)
- `a83b7666` — Chatlas Package.Skill in md-library (:New, long session with index writing)
- `019e5277` — Iterante Package.Skill migration (:Migrate, agent confusion about target)
- `258b002c` — PaperSON Package.Skill bootstrap (:New, then design session)
- `f6688049` — Canvas Package.Skill bootstrap (:New, embedded in larger impl session)
