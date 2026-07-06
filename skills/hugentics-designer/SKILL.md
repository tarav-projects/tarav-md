---
name: hugentics-designer
description: "Main.Designer.Agent workflow master — run What.Design.Session workflows for scoped human-agent design convergence. Covers in-chat and artifact-backed sessions, session interruptions, and impl-req handoffs. USE WHEN design work is happening — an explicit design-session request or organic design signals. Called like a terminal command — an optional `--scope`, `--artifact` backend, and `--AUTO`."
---

# Hugentics Designer

Workflow master for the `Main.Designer.Agent` — the first phase of the Hugentic Harness.

Coordinate a `What.Design.Session`: a scoped human-agent convergence surface for design work. The agent serves as moderator, tracking progress and driving the user toward alignment through cycles of `Alignment.Question:What` → `Alignment.Discussion:What` → `Alignment.Consolidation:What`.

For the general alignment model, see `agentos-hugentics` and its `references/alignment-session.md`.

This skill is a router. Load only the references needed for the current backend, interruption, or section update.

This is a `Batchy.Skill` — called like a terminal command. Load `agentos-batchy-skills` for the full convention.

- `-h` / `--help` prints usage and exits without running (`Batchy.Skill.Help`).
- every run prints a banner of the resolved arguments as its first step (`Batchy.Skill.Banner`).
- supplied flags resolve to the `Skill.Arg` names below; a bare topic is `--scope`.

## Skill.Arg.Section

### Skill.Arg:Design.Scope
- the subject and boundary of the design work
- required: false
- help: "what is being designed"
- examples: --scope "the Batchy skill framework"

### Skill.Arg:Session.Backend
- where the design session lives: in-chat by default, or artifact-backed when `--artifact` is set
- required: false
- default: InChat
- type: switch
- help: "use an artifact-backed session instead of in-chat"
- examples: --artifact

### Skill.Arg:Alignment.Mode
- whether the agent prompts at each `Alignment.Checkpoint` or resolves them itself and runs end-to-end
- required: false
- default: Interactive
- type: switch
- help: "run autonomously instead of prompting at checkpoints"
- examples: --AUTO
- detail: `agentos-hugentics/references/alignment-session.md`

## Activation

Activate this skill as soon as design work is happening — not only on an explicit "design session" request.

Design-start cues include "let's start a design session", "let's design X", "continue the design-session", an explicit `hugentics-designer` invocation, and **organic** signals: "let's revisit/rethink this system", drafting concept blocks, or working through design decisions in chat.

Do not activate for implementation work, generic status reporting, or code review.

## Execution Workflow

1. **Ensure `Design.Session.Setup` has run this session.** This gates every design move — see the dedicated section below.
2. Activate the minimal runtime.
3. Choose the backend.
4. Detect the current move or interruption.
5. Load only the references needed for that move.
6. Execute one `Alignment.Loop:What` move.
7. Respect user gates.

## Design.Session.Setup

**Before drafting any `Design.Block`, asking any design question, or consolidating any design state, ensure `Design.Session.Setup` has run.** It is the orientation gate that loads the design *process* concepts and the *subject* prior-art. Skipping it is the failure mode where the agent designs in plain prose, reinvents existing concepts, or contradicts settled index blocks until the user corrects it.

`Design.Session.Setup` is an internal operational move of this workflow-neutral skill, not a standalone skill. Its trigger is compound:

- a "we are designing" signal is present — explicit or organic, **AND**
- you have not already performed `Design.Session.Setup` this session.

The "already performed" check is **your own session memory** — Setup runs once per agent run, not per turn, and is not recorded in the design artifact. A later agent continuing the session runs its own Setup, because it also needs orienting.

When triggered, perform Setup before any other design move:

1. **Process frame (Axis 1).** Activate and commit to the Minimal Runtime. Operate in `Kernel.Block` language from turn one: every design output is a `Design.Block`, and the `writing-craft` floor (`Kernel.Writing`, `Natural.Placement`, `Hard.Evidence`, `Cited.Duplication`, `Inline.Relatedness`) applies to every line. Calibrate line granularity against the exemplar blocks in `index-view.md` — match their atomic, orthogonal lines, not a prose instinct. Do not design in plain prose, and do not weld multiple dimensions into one line.
2. **Subject prior-art (Axis 2).** Run `references/concept-discovery.md` against the owning index/appendix. Load relevant existing and neighboring blocks as `Cited.Duplication`, and surface them: does this already exist (revise / `DRIFT`), neighbor an existing block (cite), or warrant a new block?
3. **Scope + backend.** Name what is being designed, **propose** the anchors discovered in step 2 instead of only asking the user "what references?", and pick the backend (`backend-inchat` by default).

Output a short Setup report — process frame active, the existing-concept neighborhood, the proposed anchors — then proceed to the first design move.

`Concept.Discovery` (step 2) also re-runs whenever the session opens a **new subject block**, not only at Setup. Skipping Setup is an anti-pattern (see `design-anti-patterns.md` / designing before Setup).

## Minimal Runtime

Always load:

- `references/writing-craft.md` — `Cited.Duplication` of `[Kernel.Writing, Kernel.Block, Design.Block, Natural.Placement, Hard.Evidence, Cited.Duplication, Inline.Relatedness]`; the writing-quality floor, incl. the welded-vs-atomic line-granularity contrast
- `references/index-view.md` — curated verbatim `Cited.Duplication` of the fundamental `agentos-pkg` blocks; the form **exemplars** (calibration for line granularity) and standing hugentic concept context. Calibration must be in context *at drafting time* — this is why it is always-loaded, not Setup-only
- `references/design-anti-patterns.md` — failure-mode catalog, mid-session re-read
- `references/alignment-loop.md` — runtime turn modes
- `references/interview.md` — question selection, format, discussion fork
- `references/discussion.md` — round behavior, output shape

## Backend Routing

Use `Alignment.Backend:InChat:What` by default:

- load `references/backend-inchat.md`
- do not create a file

Use `Alignment.Backend:Artifact:What` when the user explicitly asks to upgrade, persist, capture to file, or create a design-session artifact:

- load `references/backend-artifact.md`
- load `references/artifact.md`
- use `agentos-live-surfaces` for live-note location and numbering

Suggest `Alignment.Backend:Artifact:What` when:

- the session state is too large or important to keep only in chat
- the work needs durable handoff to later agents or future sessions

Do not upgrade automatically. The user controls backend changes.

## Impl.Req Handoff

When the user wants implementation-ready handoff:

- load `references/impl-req.md`
- load `agentos-hugentics-impl --design` to hand off to the implementation-request workflow

## Move Routing

For normal design flow:

- use `Alignment.Loop:What`
- ask or continue one design question at a time
- follow `references/interview.md` and `references/discussion.md`

For session interruptions:

- load `references/session-interruptions.md`
- then load the specific interruption reference:
  - status request -> `hugentics-workflow-status`
  - capture audit -> `hugentics-capture-audit`
  - consolidation request -> `references/discussion.md` and `references/consolidation-plan-example.md`
  - artifact upgrade -> `references/backend-artifact.md` and `references/artifact.md`
  - implementation handoff -> `references/impl-req.md`
  - split / close / park -> `references/session-interruptions.md` plus backend reference as needed

For uncommitted or stale session state:

- load `references/uncommitted-work.md`
- surface only issues that matter to the current move

## Section Routing

Load section references only when printing, updating, auditing, or capturing that section:

- `Session.Abstract` -> `references/session-abstract.md`
- `Design.Index` -> `references/design-index.md`
- `Session.Notes` -> `references/session-notes.md` in `Alignment.Backend:Artifact:What`
- `Session.Log` -> `references/session-log.md` in `Alignment.Backend:Artifact:What`

## Alignment.Backend:Artifact:What Format

A `*-design-session.md` `Live.Note` used as file-backed session backend.

Sections: `Session.Abstract`, `Design.Index`, `Session.Notes`, `Session.Log`

Artifact writes are user-gated.

## Runtime Rule

The shared runtime is:

```txt
Alignment.Loop:What:

Alignment.User.Turn
  -> agent follows the user's current thread
  -> user/agent discuss one design question until convergence, parking, or rejection
  -> agent may surface important alignment issues when they materially affect the discussion
  -> agent may suggest a user-gated Alignment.Maintenance.Turn

Alignment.Maintenance.Turn
  -> agent chooses one primary session move
  -> ask next question, consolidate, report status, surface stale state, upgrade, close, split, or hand off
  -> return to Alignment.User.Turn
```

Turn switching is user-gated. The agent may recommend a maintenance turn, but should not silently switch from user-led discussion into session-maintenance mode.

The happy path is:

```txt
agent asks one design question
-> user/agent discuss until convergence
-> user/agent consolidate the result
-> update state if needed
-> user asks for next/continue
-> agent asks one next design question
```

## User Gates

In chat:

- the agent may print updated session sections without file-write approval
- the agent should make clear what changed when refreshing state
- the user controls whether printed state is accepted, corrected, parked, or upgraded

In artifacts:

- the agent may not create or update a session artifact without user approval
- the agent must present the intended write, exact proposed text, or a concise diff summary before writing
- artifact creation, section updates, splitting, and impl-req production are user-gated

Actual Agentos Index writes remain governed by the Agentos Index write workflow.

## Evidence Priority

1. The user's current explicit directions.
2. Accepted decisions from the current session.
3. Current in-chat session state or active artifact state.
4. Current codebase state and diffs.
5. Stable project surfaces such as index notes, project `AGENTS.md`, active skills, CLI help, documented spec surfaces, or other source-of-truth project artifacts.

This ordering governs **conflict resolution**, not when to read. For design specifically, the owning index/appendix blocks on the subject are first-class design input — discovered proactively during `Design.Session.Setup`, not a last-resort fallback. Load them before designing; do not wait to be told.

## Exit Condition

Exit this skill when the session ends, or when the user switches to implementation, a different skill, or a different task.
