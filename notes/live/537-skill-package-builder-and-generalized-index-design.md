# Skill.Package.Builder + Generalized Index — Design Capture

> Live capture of a long design session. **Completeness > integration** — ideas are recorded even where not yet reconciled. Many are draft; some are written into the index, some are only discussed. Markers: ✅ written to index/skill, ◐ partially built, ⬜ idea only.

---

## 0. How this started — the index audit

- The session began as research on the "agentos agent run system," which surfaced that the `Agentos.Agent.Adapter` index block carried `status:`/`resolved:` meta lines.
- This was identified as a fundamental flaw: **the state of the index is the index itself**. The system is `Hard.Evidence`-based — you point at where evidence lives, you do not cache a status summary. To know status, go recompute it from the surface.
- This drove a full audit + cleanup of the index, then expanded into a much larger design arc about the builder and the generalized index.

### Audit ledger (all ✅ resolved)
- **#1** meta-status definition — `Meta.Unification` block eliminated.
- **#2** status/task dumps in `104` — `Agentos.Agent.Adapter` (kept only `aliases`) + `Account.Management` (whole `### meta` deleted). The headliner / loop-closer.
- **#3** "parameterized by surface" framing — `Universal.Block.Structure` deleted; `Index.Architecture` reworded to "surface-placement variants."
- **#4** raw `### grounding/appendix/meta` headings — `Index.Block` reworked; raw headings are just the inblock *form* of a section.
- **#5** grounding chat-coupling — `Grounding.History` + `Grounding.Context.Injection` generalized source-neutral.

---

## 1. Kernel.Writing / Kernel.Block family (✅ cleaned this session)

- **`Kernel.Writing`** — portable, surface-independent conceptual writing philosophy: orthogonal bullet lines, each a fundamental dimension; inline linking; direct language; coverage over compression. Source can be chat, code, docs, design, observation.
- **`Kernel.Block`** — the base writing object; **surface-neutral**: "the surface it lives on sets what a block may hold and how writing is gated." One block = one topic. Heading is a conceptual commitment.
- **`Kernel.Block.Section`** — a named part; two forms: `:Inblock` (`###` subsection) and `:Outblock` (external concept-named file, discovered by naming). The form is a placement choice; **inblock/outblock preference is a block-TYPE concern, not fixed at the Kernel.Block level.**
- **Section blocks**: `Kernel.Block.Fundamentals` (only required; always inblock), `Kernel.Block.Grounding`, `Kernel.Block.Appendix`, `Kernel.Block.Meta`.
- **Surface-placement variants** (renamed from old `Kernel.Block:Index/:Appendix/:Design`): `Index.Block`, `Appendix.Block`, `Design.Block` — `Kernel.Block` placed on a specific surface with that surface's constraints. NOT "parameterizations."
- **`Kernel.Block.Meta`** — non-conceptual data about the block-as-object; findability/convenience. The **strip-test**: remove the line; if conceptual load unchanged, it's meta. `alias` is paradigmatic. **No status** on a Stable.Surface.

### Naming notation (key discipline)
- `:` colon = inline instance/form (same concept, different target) — `Dotted.Parameterized.Notation`.
- `.Child` dot = part-of / namespace member.
- standalone flat name = distinct concept/kind.
- Rule: if a concept has its own block, don't write `<Concept>:<Concept>` — colon is for inline parameterization only.

---

## 2. Status / Stable.Surface principle (⬜ Computed.Status still unwritten)

- **`Computed.Status`** (designed, not written): on a `Stable.Surface`, status is NOT stored — it is computed by inspecting the surface. Escalation: recompute → pointer (only if super costly) → cache (only if super-super costly); **"for now, never."** A cached status is `Cited.Duplication` for state.
- This is a general agentos-surface pattern: **Stable Surfaces don't hold status; status comes from checking the surface itself.** A block on a *design* surface CAN hold status (design artifact ≠ Stable.Surface).
- `We.Distrust.Summaries` (✅ written) — a summary is low-confidence until it links to its source evidence; the link lets a reader recompute. This is why Stable.Surfaces prefer pointers + recomputation over cached summaries.
- `Hard.Evidence` (✅ generalized) — evidence beats assumption; concrete evidence: user instructions, inspected code, active session artifacts, stable surfaces, chat. Dropped the alignment-only scoping.

---

## 3. File.Mention + grounding generalization (✅)

- **`File.Mention`** (✅ written) — `@<path-hint>`: a neutral inline token bringing a file into a block's context. A mention does NOT confer aboutness (aboutness must be explicit), exactly like mentioning a concept doesn't make the block about it. Peer of `Inline.Relatedness`/`Concept.Cite`. Resolved by search, opportunistically.
- **Grounding generalized source-neutral**: `Kernel.Block.Grounding` = mechanical `Hard.Evidence` linking section; a source can be `Chat.Ref`, `File.Mention`, web, or another evidence surface. `Grounding.Entry` = one citation row → one evidence reference. `Chat.Grounding` = canonical (Hugentic surface), not the only one.

---

## 4. Agentos.Skillware + the build surfaces (✅ index 107)

- **`Agentos.Skillware`** — treat skills as software; the skill is the unit of software for agents. Supported by a development toolchain (linters, builders, compilers) spanning agentic + CPU work, moving maintenance off the human.
- **`Skill.Runnable.Surface`** — what the agent reads/runs; only executable substance, kept clean.
- **`Skill.Build.Surface`** — the complement; build-time material, never loaded at run time; an unconstrained workspace. Lives in a per-package **`build/`** folder, organized by capability (derivation, tests, lint, lineage), discovered by convention.
  - NOTE: `Derivation.Surface.Arch` block was created then **deleted** as over-specified; folded into `Skill.Build.Surface`.

### Skill.Package.Builder (✅ index 107)
- The **support system** for developing & maintaining a skill package's `Skill.Runnable.Surface`.
- A **bundle of agentic skills and CLI support tooling** (not a single CLI).
- Supports any build workflow over the package: derivation builds/drift-checks, tests, lint, lineage. Open-ended — derivation is one capability, not the whole system.
- The `Skill.Build.Surface` is its **workspace** — holds anything it needs that shouldn't be on a runnable surface.
- Realized as the `agentos-skill-pkg-builder` `Package.Aux.Skill`.

---

## 5. Derivation (✅ index 107 + ◐ skill)

- **`Derivation.Rule`** — relation `Dependencies + Context → Derived`. Run **forward** → (re)generate; run as **check** → drift question. Context spans **implicit → explicit** (this axis recurs everywhere). Maintenance becomes a query, not vigilance.
- **`Derived.Content`** — the derived side; granular (any span of a module). Tie to sources automates drift detection.
- **`Derivation.Manifest`** — explicit artifact carrying the parts of the rule not inline; lives on the build surface.
- **op vocabulary** (by how much the source is reshaped; = mechanizability signal): `copy` (verbatim) ⊂ `projection` (a structural part) ⊂ `transform` (reshaped by intent). (Renamed `project`→`projection`.)
- A **manifest = a `Kernel.Note` of `Derivation.Rule` blocks**, free-placed in `build/derivation/`. Folder is the unit, not the file; builder loads all, runs every rule.
- Rules are **soft mini-Kernel.Blocks** (`Index.Block` philosophy): relation + context + soft locator-hint + on-drift. The builder is smart — hints lower search cost, don't pin coordinates.

### Addressing discipline (hard-won)
- **Never plant markers/bookkeeping in the runnable surface** — addressing is the build side's job. Markers add noise + cost to what the agent reads. Rejected.
- Addressing reuses the surface's **own existing structure** (headings, code fences, `Dotted.Name`s), expressed from the build side; agent resolves by reading.
- **Never build a surface from scratch** — the builder maintains relations between existing surfaces.
- **One owner per target span.**
- Runnable writes are gated (`Content.Verbatim.Gated`-style).

---

## 6. The builder skill — check hierarchy (◐ built)

- **`--check`** = umbrella suite runner; read-only; aggregates every registered check.
  - **`--derived`** (was `--manifest-checks`) — declared-rule drift. (To rename.)
  - **`--inline-drift`** — implicit non-contradiction drift.
- **`--build`** — reconcile manifest rules (forward). **DECIDED: defer `--build`; read-only tests first.**
- Selectors (shared, scope every test): **`--skill`** (coarse — one skill surface) + **`--target`** (fine — file or block/concept) + **`--manifest`** + **`--since`** (recent-changes window). DRY note: `--manifest` can fold into `--target`.

### inline-drift (the implicit-context pole)
- No manifest needed. Index is the canonical definition surface; if a surface cites a concept, it must **not contradict** that concept. **Non-contradiction, not equality** — a mention may rephrase/simplify/scope (per `File.Mention`/`Inline.Relatedness`).
- Read-only; **candidates, not verdicts** — it has no rule for how a surface should restate a concept, so it never reconciles.
- **Default target = the recent-changes set** — surfaces touched in the current conversation ∪ git change window (`--since`, ~2-3 weeks). Makes it the **post-edit drift sweep**. **Promote git-seeded recent-changes scope to ALL tests** as the shared first exploration.
- **Bidirectional**: changed index block → sweep its mentions; changed non-index surface → check its citations.

### Proof results (✅)
- `--build` reconciled the stale `Hard.Evidence` example in `index-block-catalog.md` (a `projection` rule). End-to-end MVP worked.
- `--inline-drift` found + drove fixes of cross-skill contradictions: `hugentics-designer` refs (`index-view.md`, `writing-craft.md`) carried the exact framings we deleted (old colon names, `### meta covers status`, parameterized-by-surface). Refreshed + re-verified clean. `design-index.md` status-in-meta was KEPT — design surface allows status (judgment call inline-drift surfaces).

---

## 7. The general test model (⬜ design)

- **A check is a test; `--check` is the suite; the builder is the mechanized `Internal.Alignment` harness for stable surfaces.**
- A test = `Dependencies + Context → expected property` — same shape as `Derivation.Rule`. Tests live on the **same implicit↔explicit context axis**.
- **A test type is an interpreter; a manifest entry is an instance.** `From.Agentos.Pkg.Everything` is not a test — it's one coverage *entry*.
- **Folder = type = dispatch**: `build/<test>/` holds that test's entries. No new typing mechanism.
- **Loose composition**: a test may run general-only, registered-only, or weave general → registered → general — free. The only commitment: read-only module reporting candidates.
  - **general pass** — agent goes out and finds as much as possible (no infra).
  - **registered instances** — important places singled out as entries, with extra context.
- **Nothing is entry-required** — every test has a general mode; entries are universally optional enrichment.

### Test archetypes (three, enough to set precedent)
| archetype | property | entries | hardness | reconcile |
|---|---|---|---|---|
| derivation (`--derived`) | derived = source | registered-primary | hard | (deferred --build) |
| coverage (`--router-coverage`) | set ⊆ router | **registered-only** (no general) | hard | propose-entry |
| semantic (`--inline-drift`) | mention ⊬ contradicts def | general + optional | soft | none |
| (future) cite (`--cite-coverage`) | durable material cites origin | general + optional | soft | none |

- **Reconcilability tracks hardness, not test family**: hard/precise → pass-fail + reconcile; soft → candidates, read-only.
- **`Index.Linter` is one test family** within this suite — don't fork. "Sufficiently cited" = a `Placement.Balance`/`Cited.Duplication` test.
- **`--router-coverage` is registered-only**: register the skill **dependency structure**; the expected set isn't discoverable by sweeping.

---

## 8. Specified.By.Precedence (✅ index 107)

- Design pattern: when no explicit spec is in sight, **constrain new work by the shape of existing implementations**. Already-built instances are the `Reference.Implementation` for the not-yet-built. Format evolves and converges by imitation, no central definition.
- Use where a rigid spec would over-specify a still-soft pattern; an explicit spec, once it appears, supersedes precedent.
- **Governs the test framework**: no rigid contract needed — write a couple reference tests well, new ones imitate. Relieves the over-specification pressure (5-field contracts etc. were the anti-pattern this names).

---

## 9. The generalized index (⬜ big redesign)

- Realization: **Kernel.Writing is great for constraints/invariants/relationships, not just concept definitions.** Concepts want to stay short; invariants/relations need an extendable surface to accumulate.
- The index isn't overloaded — it's the only *developed* member of a **Kernel.Writing surface family**. It needs **peers**, not expansion.
- **N parallel namespace-folders**, each a flat-file block surface, **sharing one appendix**:
  - `design/` (= today's `index/`) — unprefixed, the global concept namespace, user-managed design.
  - `impl/` — `Impl/…` implementation + build-system design notes (e.g. "`--ground` imports `--search`").
  - `build/` — DECIDED to mean the **tool workspace** (`Skill.Build.Surface`), NOT a design namespace. Build-system *design* goes in `impl/`. (Collision resolved.)
  - `<anyone>/` — free to add.
  - `appendix/` — shared depth for every namespace; holds accumulated invariant lists.
- **`INDEX.md`** = the router/TOC / location hints (today's `000-index.md`), spanning all namespaces. This **splits "index" the router from "index" the concepts** — resolves the index→design rename tension without renaming.
- **Folder = namespace = prefix.** Folder IS the `Explicit.Namespace`; prefixing is automatic; manual `### meta namespace-members` lists largely disappear. `design/` is the unprefixed default. Reuses `Concept.B/Concept.A` scope notation.
- **Registered vs unregistered surfaces** (the key axis): registered (index/design — every heading a global `Name.As.Index` key, routed, gated) vs unregistered (`Kernel.Note`-style — local headings, no registry, can still cite global concepts). `Kernel.Note` already = "Kernel.Blocks outside index routing"; promote it to a developed first-class surface.
- Boundary to hold: **find-by-name-globally → design/; local structural wiring → unregistered notes.** That's `Natural.Placement` deciding "concept or note?" Don't let the registry bloat or the notes swallow concepts.
- **Catch-all appendix block**: every concept's appendix carries a default open block where invariants/relations/wiring accumulate freely.
- Refinements: don't rename `index/` (churn) — keep as default namespace, add siblings. Shared-appendix filename needs flattening (`Build/X` → `Build.X-appendix.md`, slash isn't filename-safe). The prefix convention is itself **lintable by this build system** (self-enforcing architecture).

---

## 10. Invariants — the unifying primitive (⬜ strong direction)

- An invariant is NOT a new primitive — it's a **recognized subset of Kernel.Block lines**: the **must-hold constraints** (must / always / never / only), as opposed to descriptions.
- One gradient: **descriptive → invariant → actionable invariant (test)**. The only difference between a design invariant and a test is **whether a checking procedure exists.** A test IS an invariant with a check attached. Same hardness gradient.
- **Design and verification are the same surface at two hardnesses.**
- **Invariant registry** = harvested must-hold lines (like `Name.As.Index` harvests names). Forks by checkability:
  - checkable → feed the test suite (a registered test can BE an invariant with a check).
  - not-yet-checkable → stand as the asserted design contract; harden later.
- **Invariants are the interface** between the writing surfaces and the build tool. Design authors them; the tool harvests + runs them. Tool never owns design content.
- Example design invariant: "`Account.Capture` is read-only on `Home.State`" — checkable against **code** (the conformance case). Same shape, code surface instead of md. Out of current scope but free later.
- Caution: hold the descriptive↔invariant line soft-but-real (the must-hold marker), else the registry = the whole index and you gain nothing.

---

## 11. The two machineries — producer / runner (⬜ key integration)

- The build tool has **two machineries** (a compiler/runtime split):
  - **Producer (compile)**: harvest invariants from the writing surfaces + read explicit manifests → produce & maintain the concrete test set.
  - **Runner (execute)**: run the test set → drift report. (`--check` = the runner; ✅ built.)
- **Writing surface ≠ build tool.** "Where we discuss build/impl" = block-writing surface (`impl/`). "The thing that runs tests" = the runnable builder skill. The `build/` workspace = tool state. Three distinct things; don't conflate.
- **The invariant is the interface** that lets them stay separate.
- Built so far = the **runner** + workspace + a couple test modules. The **producer** (invariant harvesting) is the new frontier — what makes "design → tests" real. For MVP the producer can be fully agentic, handling one invariant.

### Integrated picture (Package.Skill, .md only)
```
WRITING SURFACES (durable design)        THE BUILDER (runnable skill)
INDEX.md   router/TOC                     PRODUCER: harvest invariants + manifests → tests
design/    global concepts                RUNNER:   run tests → drift report  (= --check)
impl/      Impl/… impl+build design       WORKSPACE: build/<test>/ manifests, entries
appendix/  shared depth + invariants
   └─ invariants = the interface ────────► harvested, not duplicated
```

---

## 12. POC / MVP plan (⬜ next)

- **Target: `chatlas-pkg`** — isolated (not the canonical agentos index), cross-package validation (builder works on another package), real multi-aux-skill structure (~6 chatlas-* aux skills) for `--router-coverage`, real invariants (retention, session-model).
- **Keep additive** — don't restructure chatlas's index. Add one `impl/` namespace (1-2 invariant-bearing blocks) + a `build/` workspace. Leave existing concepts untouched.
- **Vertical slice touching both parts**:
  - **Test A — `--router-coverage`** (structural, no producer): registered chatlas aux-skill dependency structure → does `chatlas-pkg` router list all aux skills? Proves runner + registered + real package.
  - **Test B — one harvested invariant** (producer slice): author one real chatlas invariant in `impl/`; producer harvests it → runner checks against the relevant `.md` → drift report. Proves the `design → invariant → test → drift` loop.
- Excludes: code-conformance, `INDEX.md` split, full namespace generalization, invariant registry machinery, `--build`/reconcile.
- Pre-step: peek at chatlas-pkg's current surface layout to ground Test A's expected set + pick Test B's invariant.

---

## 13. Loose ends / parked
- `Computed.Status` block — designed, never written.
- The dropped "alignment sessions aim to be Hard.Evidence-based" line — to relocate into `Alignment.Session`.
- Cited.Duplication drift into the installed `.claude/skills/` copies (symlinks — mostly fine) and any other operational duplicates of the changed concepts.
- `Stable.Surface.Test` concept — discussed as the umbrella for the test framework; decision pending whether to index now or after the runner suite proves out.
- `--cite-coverage` + reshape `--manifest-checks`→`--derived` — the immediate concrete next builder work.
- Naming: `--inline-drift` vs `--derived` symmetry (could be `--inline`/`--derived`).

---

## 14. Recurring principles invoked
- `Hard.Evidence`, `We.Distrust.Summaries`, `Cited.Duplication`, `Placement.Balance`, `Natural.Placement`, `Reference.Implementation`, `Name.As.Index`, `Concept.Hardness`/`Spec.Hardness`, `Program.Hardness` (agentic→CPU), `Vertical.Slice`, `Flat.Index.Architecture`, `Explicit.Namespace`/`Concept.Scoping`, `Surface.Types`, `General.Avoids.Specific`, `Internal.Alignment`, `Design.Implementation.CoEvolution`.
- Working protocol throughout: draft → discuss → approve → write, one block at a time (`Content.Verbatim.Gated`).
