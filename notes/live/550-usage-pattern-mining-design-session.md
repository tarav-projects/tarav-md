# 550 — Usage Pattern Mining Design Session

## Goal

Mine real chatlas sessions for `Package.Skill.UsagePattern` candidates for `agentos-pkg`. Identify recurring usage situations, extract situation/response pairs, validate against existing patterns, and propose new ones.

## Source Query

```bash
agentos chatlas query --updated-after 2026-05-17 --min-user-turns 3 --user-contains "agentos-pkg" --sort newest --limit 20
```

11 sessions matched. Each gets a section below for evaluation.

---

## Session: ac16fc98 (claude-code, Obsidian/notebook)

- **Turns**: 22u / 20a
- **Project**: Obsidian/notebook
- **First user**: "find `notes/index/daily-routine-design.md` - check `notebook/notes/daily` for the current notes - lets work on this"
- **Topic signal**: Daily routine design, external project using agentos-pkg

### Pattern: External.Project.Index.Work

- User is in a non-agentos project but uses agentos index concepts (kernel blocks, design sessions) to organize design knowledge there.
- Agent needed to apply index conventions without treating the external project as `agentos-pkg` itself.
- Session shows the "general tool" framing in action — agentos concepts used in a foreign project.

### Pattern: Design.Session.Launch

- User says "lets start a design-session" after initial exploration.
- Routed through hugentics-designer.

---

## Session: 019e5b0f (codex, agentos-project)

- **Turns**: 4u / 9a
- **Project**: agentos-project
- **First user**: "lets do some nice work on chatlas - a problem Im having is that the main way to update is a bulk update - I want to implement a more granular update path"
- **Topic signal**: Chatlas design, Provider.Instance concept work

### Pattern: Index.Block.Authoring

- User proposes new concepts (`Provider.Instance`) and iterates on block wording with the agent.
- Short session, focused on concept refinement.

---

## Session: f870a478 (claude-code, agentos-project)

- **Turns**: 52u / 59a
- **Project**: agentos-project
- **First user**: "Goal: start the Package.Skill for Chatlas in `agentos-chatlas-md`, analogous to the new `agentos-pkg` work in `agentos-md`."
- **Topic signal**: Package.Skill bootstrap for a new subsystem (Chatlas)

### Pattern: Package.Skill.Bootstrap

- Explicit goal statement referencing agentos-pkg as the template.
- Included index migration (moving blocks from agentos-pkg to the new chatlas package).
- Transitioned mid-session into a design-session for the chatlas model.
- Shows bootstrap → design-session pipeline.

### Pattern: Design.Session.Launch

- After structure was in place, user said "lets start a design-session to revisit the chatlas model."
- Natural transition: bootstrap completes → design begins.

---

## Session: a4fbafa7 (claude-code, agentos-project)

- **Turns**: 64u / 69a
- **Project**: agentos-project
- **First user**: "check `548-package-skill-testing-design-session.md` - check `agentos-md/skills/agentos-pkg/SKILL.md` - we are working on `agentos-pkg/SKILL.md`"
- **Topic signal**: SKILL.md improvement, testground design, usage pattern miner design (this session)

### Pattern: Package.Skill.Driver.Refinement

- User points at the SKILL.md and says "make it a better entry point."
- Agent reads, gives feedback, proposes diffs.
- Iterative: feedback → apply → test → feedback cycle.

### Pattern: Test.Design

- From the driver refinement, naturally transitioned to designing tests for the driver.
- Created test files, ran tests, evaluated, refined the test format itself.

---

## Session: 019e4c30 (codex, agentos-project)

- **Turns**: 276u / 442a
- **Project**: agentos-project
- **First user**: "$agentos-session-zip-transcript 19602318..."
- **Topic signal**: Mega session — index linter, test runs, live-note test execution

### Pattern: Design.To.Implementation

- Started with impl-req execution for the index linter.
- Shows the full hugentics pipeline: design artifact → impl execution.

### Pattern: Test.Execution

- Ran testground tests (live-note test) within the session.
- Shows the test runner flow: spawn subagent, capture output, evaluate.

### Pattern: Index.Block.Authoring

- Multiple blocks written/refined during the session as part of linter design convergence.

---

## Session: 019e5152 (codex, agentos-project)

- **Turns**: 38u / 111a
- **Project**: agentos-project
- **First user**: "I think we have sufficient design maturity about the index/appendix that we should start implementing a linter"
- **Topic signal**: Index linter implementation (design → impl transition)

### Pattern: Design.To.Implementation

- User explicitly states "sufficient design maturity" as the trigger.
- Deleted old implementation, started fresh.
- Designed the linter architecture (battery of checks, gating, sequential execution).
- Ended with hugentics impl-req handoff.

---

## Session: 52362a37 (claude-code, simuleos-project)

- **Turns**: 47u / 56a
- **Project**: simuleos-project
- **First user**: "I want to split Simuleos into several subfolders... setup the Package.Skill for the canvas system"
- **Topic signal**: Package.Skill setup for a different project (Simuleos)

### Pattern: Package.Skill.Bootstrap

- Combined with project restructuring (split into subfolders).
- User had to correct the agent multiple times (interrupted requests).
- Key instruction: "the current restructuring should not drop content — just relocate stuff around close to its natural place."
- Shows that bootstrap often comes alongside a structural migration.

---

## Session: a83b7666 (claude-code, md-library)

- **Turns**: 79u / 137a
- **Project**: md-library
- **First user**: "Goal: start the Package.Skill for Chatlas in `agentos-chatlas-md`, analogous to the new `agentos-pkg` work"
- **Topic signal**: Chatlas Package.Skill design, index writing

### Pattern: Package.Skill.Bootstrap

- Same prompt as `f870a478` — appears to be a continuation or retry.
- Long session: bootstrap → index writing → maintenance passes.
- Shows the full lifecycle: bootstrap → populate index → refine.

---

## Session: f6688049 (claude-code, agentos-project)

- **Turns**: 48u / 66a
- **Project**: agentos-project
- **First user**: (local-command-caveat, then hugentics impl execution)
- **Topic signal**: Hugentics impl execution, appendix rewrite

### Pattern: Impl.Execution

- Triggered via `$hugentics-impl-executer` with an impl-req artifact.
- Agent executed implementation slices, rewrote appendix content.
- Shows the disciplined impl execution flow from the hugentics harness.

### Pattern: Package.Skill.Bootstrap

- Mid-session, set up `agentos-canvas-pkg` as a new package skill.
- User said "setup the Package.Skill for the canvas system - check `agentos-pkg`."
- Bootstrap embedded within a larger impl execution session.

---

## Session: 019e5277 (codex, agentos-iterante-py)

- **Turns**: 3u / 14a
- **Project**: agentos-iterante-py
- **First user**: "You are helping migrate this project into the Agentos `Package.Skill` framework"
- **Topic signal**: Package.Skill migration for Iterante

### Pattern: Package.Skill.Bootstrap

- User provided a reusable welcome prompt as a migration template.
- Agent initially confused (tried to implement elsewhere) — user corrected twice.
- Very short session — shows that bootstrap can be fast when the user has a clear template.
- Friction point: agent didn't understand "implement the framework HERE" on first try.

---

## Session: 258b002c (claude-code, paperson-project)

- **Turns**: 74u / 63a
- **Project**: paperson-project
- **First user**: (local-command-caveat, then PaperSON Package.Skill design)
- **Topic signal**: PaperSON Package.Skill design session

### Pattern: Package.Skill.Bootstrap

- Bootstrapped the PaperSON package skill.
- Immediately transitioned into a design session for the bootstrap workflow concept itself.

### Pattern: Design.Session.Launch

- After bootstrap structure was in place, design session for `Package.Bootstrap`, `Extraction.Focus`, and `PaperSON.Data.Specs`.
- Shows again: bootstrap → design session is a natural pipeline.

### Pattern: Index.Block.Authoring

- Multiple blocks authored during the design session (Publication.Source, PaperSON.Data.Specs, etc.).

---

## Candidate Patterns (Global)

### 1. Package.Skill.Bootstrap

**Sessions**: `f870a478`, `52362a37`, `a83b7666`, `019e5277`, `258b002c`, `f6688049`

**Situation**: User wants to create a Package.Skill for a new project or subsystem. They reference `agentos-pkg` as the template and expect the agent to set up the canonical structure.

**Expected behavior path**:
1. Load `agentos-pkg` for Package.Skill concepts
2. Check index: `Package.Skill`, `Package.Aux.Skill`, `Package.Skill.Router`, `Package.Skill.Install`
3. Inspect the target project's existing content
4. Propose folder structure (SKILL.md, package.md, index/, references/, etc.)
5. Ask about naming, ownership boundary, what gets absorbed
6. Do not write until user approves structure

**Key signals**: "setup Package.Skill for X", "start the Package.Skill", "migrate into Package.Skill framework", "analogous to agentos-pkg"

**Observed friction**:
- Agent sometimes doesn't understand "implement HERE" (019e5277)
- Bootstrap often comes with structural migration — agent must preserve content
- User often transitions to design-session immediately after bootstrap

**Frequency**: 6/11 sessions. Highest priority pattern.

---

### 2. Design.Session.Launch

**Sessions**: `f870a478`, `258b002c`, `ac16fc98`, `019e5152`

**Situation**: User has enough context on a topic and wants to start a structured design session. They say "lets design" or "lets start a design-session."

**Expected behavior path**:
1. Recognize design-session intent
2. Route to `hugentics-designer`
3. Clarify scope, goal, and target artifact
4. Begin What.Design flow

**Key signals**: "lets start a design-session", "lets design", "revisit completely", "redesign"

**Observed friction**:
- Often emerges naturally after bootstrap or exploration — not always the first user intent
- Agent should recognize the transition signal even mid-session

**Frequency**: 4/11 sessions.

**Note**: May already be fully covered by `hugentics-designer` skill. Pattern value is in the *transition detection* — recognizing when a conversation has shifted from exploration to design intent.

---

### 3. Index.Block.Authoring

**Sessions**: `019e5b0f`, `019e4c30`, `258b002c`, `ac16fc98`

**Situation**: User proposes a concept and asks for an index block. Or user says "make this into a kernel-block" after discussion converges.

**Expected behavior path**:
1. Load routing table (`000-index.md`)
2. Check for existing overlap
3. If overlap: flag, suggest merge/complement/cited-dup
4. If new: draft in Kernel.Block::Index format (dash-list)
5. Ask for target index
6. Propose router update

**Key signals**: "propose an index block", "make this into a kernel-block", "write the blocks", concept name in `Dotted.Notation`

**Observed friction**:
- Agents sometimes use prose format instead of dash-list
- Agents sometimes skip overlap check (see test run 2)
- Agents sometimes hallucinate related concepts instead of citing real ones

**Frequency**: 4/11 sessions. **Already has a test** (`guidance-locality-01`).

---

### 4. Design.To.Implementation

**Sessions**: `019e5152`, `f6688049`

**Situation**: Design maturity reached, user wants to produce an impl-req or start implementation. The signal is often explicit: "sufficient design maturity", or the user triggers `$hugentics-impl-designer` or `$hugentics-impl-executer`.

**Expected behavior path**:
1. Recognize impl-readiness signal
2. Route to `hugentics-impl-designer` (if designing the impl-req) or `hugentics-impl-executer` (if executing)
3. Check existing design artifacts
4. Produce or load impl-req artifact
5. Begin execution if impl-executer

**Key signals**: "sufficient design maturity", "lets implement", "$hugentics-impl-executer", "$hugentics-impl-designer", explicit impl-req reference

**Observed friction**:
- Sometimes the user wants to delete old implementation first — agent should ask, not assume
- The transition from "discussing" to "implementing" needs a clear gate

**Frequency**: 2/11 sessions.

**Note**: Mostly covered by hugentics skills. Pattern value is in recognizing the *transition moment*.

---

### 5. Package.Skill.Driver.Refinement

**Sessions**: `a4fbafa7`

**Situation**: User is improving an existing Package.Skill's entry surface. They point at SKILL.md and ask for feedback, then iterate.

**Expected behavior path**:
1. Read current SKILL.md
2. Evaluate against driver expectations (orientation, routing, non-redundancy, general-tool framing)
3. Give structured feedback
4. Propose improvements as diffs
5. Apply on user approval
6. Optionally run testground tests to validate

**Key signals**: "make it a better entry point", "give me feedback on SKILL.md", "check the driver", "improve the router"

**Observed friction**:
- Agent can dump too much feedback at once instead of prioritizing
- Diffs are the best format for proposals

**Frequency**: 1/11 sessions. Will grow as more packages mature.

---

### 6. External.Project.Index.Work

**Sessions**: `ac16fc98`

**Situation**: User is in a non-agentos-pkg project but uses agentos index concepts to organize knowledge there.

**Expected behavior path**:
1. Load `agentos-pkg` for index concepts and conventions
2. Apply conventions to the external project's local index
3. Do NOT assume the target index is `agentos-pkg`
4. Adapt block style to the project's existing conventions

**Key signals**: External project path + index/block work requests. AGENTS.md routes to agentos-pkg but the project is not agentos-md.

**Observed friction**:
- Agent might assume all index work targets `agentos-pkg`
- The "general tool" framing in SKILL.md should prevent this

**Frequency**: 1/11 sessions. Architecturally important — validates the general-tool claim.

---

### 7. Test.Design.And.Execution

**Sessions**: `a4fbafa7`, `019e4c30`

**Situation**: User wants to design or run testground tests for a package skill.

**Expected behavior path**:
1. Load `agentos-testground`
2. If designing: create test file with behavior tiers format
3. If running: launch fresh CLI session from testground, capture via chatlas, evaluate
4. Report against behavior tiers

**Key signals**: "run the test", "design a test", "check the testground", references to testground tests

**Observed friction**:
- Test format was evolving during these sessions (the system was being designed)
- Runner isolation is critical — subagent ≠ fresh CLI session

**Frequency**: 2/11 sessions. New system, will grow.

---

## Next Steps

- [ ] Draft `usage-patterns/Package.Skill.Bootstrap.md` as first full usage pattern file
- [ ] Generate testground test from Package.Skill.Bootstrap
- [ ] Decide if Design.Session.Launch and Design.To.Implementation are distinct patterns or just "hugentics skill already covers this"
- [ ] Create `agentos-pkg/usage-patterns/` folder
