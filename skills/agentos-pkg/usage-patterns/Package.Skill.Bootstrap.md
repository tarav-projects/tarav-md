# Usage Pattern: Package.Skill.Bootstrap

## Situation

The user wants to create a `Package.Skill` for a project or subsystem. They reference `agentos-pkg` as the framework and expect the agent to set up the canonical structure.

The agent discovers which sub-situation applies by inspecting the target:

### Package.Skill.Bootstrap:New

- `Package.Skill.Bootstrap:New` is the situation where there is no existing Package.Skill structure
- the agent reads what `agentos-pkg` says about Package.Skill structure and creates the scaffolding
- ask the user about naming and ownership boundary, then propose the structure for approval

Signals: empty or minimal project folder, user says "start the Package.Skill for X", "create a Package.Skill."

### Package.Skill.Bootstrap:Migrate

- `Package.Skill.Bootstrap:Migrate` is the situation where existing content needs to be organized into the Package.Skill framework
- fundamental principles:
    - never drop content — everything is accounted for, even if its placement is approximate
    - never duplicate content — relocate means move, not copy. No parallel copies unless the user explicitly asks for a backup
    - conservative by default, not by rule — if something maps cleanly, move it now; if it's ambiguous or high friction, move it close and flag it for later
- the agent inventories existing content, classifies by proximity to natural place, and proposes a relocation plan
- the migration creates only the minimal scaffolding: `SKILL.md` as driver, `package.md` as router — the rest comes from relocated content or later sessions
- the result is not a finished Package.Skill — it is something that looks like one. A first pass.
- if the migration is complex (many files, cross-package content, structural splits), propose an `Impl.Req` to the user to scope the work across slices
- the project graduates to stable through subsequent work: driver refinement, design sessions, index population

Signals: existing content that needs restructuring, user says "migrate into Package.Skill framework", "restructure into Package.Skill", "setup Package.Skill — don't drop content."

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
- Inventory existing content — what exists, where, what role it serves.
- Classify by proximity: what maps cleanly, what is ambiguous, what needs user decision.
- Do the easy moves now. Flag the hard moves for user decision.
- If the migration is complex, propose an `Impl.Req` to the user to scope the work across slices.
- Relocate first, revise later. Do not rewrite content during migration.

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
