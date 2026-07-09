> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Kernel.Block.Grounding

- `Kernel.Block.Grounding` is the grounding of a `Kernel.Block` — two appendix sections, `Concept.X/Grounding.Head` and `Concept.X/Grounding.Drift` ^20260707-0
- both hold grounding lines: an `Anchory.Anchor` plus a one-sentence explanation of what the anchored turn grounds ^20260707-0
- [DC] a grounding line is typed `[GR]` and reads sentence first, anchor trailing — the same tail position `Inline.Grounding` uses ^20260709-2
- [DC] `Grounding.Head` is the block's evidence board: noticeable grounding spots scoped to the block and its lines — append-friendly, no whole-block claim required ^20260709-0
- [DC] `Grounding.Drift` collects retired grounding — provenance, created on demand ^20260709-1
- state is positional: lines move from `Grounding.Head` to `Grounding.Drift` as the concept evolves ^20260707-0

****

## Inline.Grounding

- `Inline.Grounding` is grounding at `Kernel.Line` granularity — trailing `Anchory.Anchor`s on the line they ground ^20260709-2
- [DC] a line anchor answers: here is the best known place to look for user-touched evidence about this line — a curated pointer, upgraded when a better turn is found ^20260709-0
- [DC] the whole-block approval turn is the legitimate fallback pointer — stamped at gated landing on every line no more specific turn covers ^20260709-1
- [DC] anchors per line stay curated: up to 3, all high value — upgrading beats accumulating ^20260709-0

****

## Context.Hook

- `Context.Hook` is a harness-defined mechanism that inserts content into an agent context
- hooks may operate at different `Context.Loading.Path` tiers
- a surface may be loaded through a `Context.Hook`
- `Cold.Loading.Hook` is the cold-start specialization of `Context.Hook`
- `AGENTS.md` and skill surfaces can be loaded through `Context.Hook`s

****

## Index.AGENTS.MD

- `Index.AGENTS.MD` is a `Context.Hook` for the index surface
- its canonical artifact path is `design/AGENTS.md` relative to the `Index.Depot` root
- it injects index-usage context through the harness `AGENTS.md` loading mechanism
- `agentos-md/skills/agentos-pkg/design/AGENTS.md` is the `Reference.Implementation` for `Index.AGENTS.MD`

****

## Appendix.AGENTS.MD

- `Appendix.AGENTS.MD` is a `Context.Hook` for the appendix surface
- its canonical artifact path is `appendix/AGENTS.md` relative to the appendix root
- it injects appendix-usage context through the harness `AGENTS.md` loading mechanism
- `agentos-md/skills/agentos-pkg/appendix/AGENTS.md` is the `Reference.Implementation` for `Appendix.AGENTS.MD`

****

## Grounding.Retrieval.Boundary

- `Grounding.Retrieval.Boundary` separates finding candidate evidence from linking it
- retrieval finds candidates; `Index.Linking` selects, anchors, and cites accepted evidence on a block
- retrieval quality affects linking quality, but retrieval mechanics are not the definition of grounding
- search engines, vector databases, keyword indexes, and chatlas queries are candidate-discovery mechanisms
- neither `Index.Linking` nor `Context.Grounding` depends on a specific retrieval backend

****

## Chat.Grounding.Target.Block

- `Chat.Grounding.Target.Block` is the rule that chat grounding attaches to a kernel block, not to a loose topic
- the index is the entity inventory that answers what is being grounded
- every chat grounding target is a `Index.Block` or `Appendix.Block`
- if an issue or topic needs grounding, it must first resolve to an existing block or become a new block
- if a subtopic inside a block needs independent grounding, it should become its own kernel block
- a `Kernel.Block.Grounding` is scoped to its one target block
- other surfaces cite grounded blocks instead of inventing separate grounding targets

****

## Grounding.Hugentic.Authority

- `Grounding.Hugentic.Authority` is the rule that grounding lines primarily anchor user turns
- assistant turns provide context, reasoning trace, proposed wording, and forensic evidence
- assistant-authored material becomes normal grounding only when the user explicitly accepts, corrects toward, or acts on it
- [CT] index grounding anchors target user turns only — gating guarantees an approval turn exists; there is no assistant-only index evidence ^20260708-8
- grounding is a `Hugentic.Alignment` workflow: human/agent collaboration, not agent-only retrieval

****

## Designer.Turn.Kernel.Form

- `Designer.Turn.Kernel.Form` is how a `What.Design.Session` turn is shaped when working a defined subject
- the designer communicates in `Kernel.Writing` — orthogonal bullet lines, each an independent fundamental point, direct language
- a turn working a defined subject proposes a `Design.Block`: an H2 `Dotted.Notation` heading, orthogonal fundamentals, and an optional `### meta` for open items
- a question turn pairs the block with the question — the `Design.Block` as actionable intro, then `Question / Why-now / Recommended-answer / Evidence`
- every new question on a defined subject is accompanied by its block; pure openers are exempt because they create the first subject
- discussion rounds re-render the same block with the change; open points live under `### meta` as `open:` lines
- the in-chat block and the artifact's `Design.Index` block are one object — capture only adds gating

****

## RED.GREEN.Test.Suite

- `RED.GREEN.Test.Suite` is the set of RED/GREEN-style tests an `Impl.Req` calls for, written test-first to drive the implementation
- an `Impl.Exec` `Development.Principle`: the `Impl.Req` specifies the suite; the executer builds it test-first — each test goes RED (fails) then GREEN (minimal code passes), one at a time
- never write all tests up front: bulk tests assert imagined shape and pass when behavior breaks
- it is not the only tests — it is the implementation-driving core; more tests may be added later, including at the end
- `No.Regression.Tests.Allowed` governs all tests including this suite — keep it core-feature, e2e, and durable-contract focused, not regression slop
- `Test.At.Boundaries` governs what each test asserts — public behavior that survives a refactor
- rationale: writing the test before the code prevents retrofit tests that merely rubber-stamp the implementation

****

## Alignment.Mode

- `Alignment.Mode` is an argument accepted by hugentic skills: its name is `Alignment.Mode`, its type is the value enum below
- it governs one axis only — the `Alignment.Checkpoint` axis: who resolves each declared checkpoint
- `Interactive` (default) — checkpoints are alignment opportunities; the agent may prompt the user at each
- `Autonomous` — no user prompting; the agent carries the process and resolves every checkpoint itself
- it is one skill axis, not a global control model — a skill may carry other independent axes
- a caller wanting "autonomous within a phase, one confirm at a boundary" owns that boundary as its own declared `Alignment.Checkpoint` and invokes downstream skills in `Autonomous`

****

## Alignment.Checkpoint

- `Alignment.Checkpoint` is a declared point in a skill workflow where the agent checks something before proceeding
- it is a checkpoint because it can be an alignment opportunity — a place where the human could meaningfully weigh in
- a decision the agent always resolves alone is not a checkpoint; it is just a normal workflow step
- every checkpoint sits at an explicit declared position; it may carry an optional activation condition deciding whether it fires when reached (e.g. "design did not fit reality") — a gated positional checkpoint, not a separate kind
- the check always runs; `Alignment.Mode` decides who resolves it — `Interactive` may prompt the user, `Autonomous` resolves alone
- checkpoints are declared explicitly, so a skill's alignment surface is inspectable up front
- discipline: the agent must not invent checkpoints and must not stop execution outside a declared one — no ad-hoc halts
- deviation (design-reality mismatch) is handled at a declared checkpoint via an activation condition, not as an anywhere-interrupt
- `Alignment.Checkpoint:<Name>` names a specific checkpoint, such as `Alignment.Checkpoint:Readiness`

****

## Alignment.Checkpoint:Readiness

- `Alignment.Checkpoint:Readiness` is a named `Alignment.Checkpoint` placed right before the `Impl.Req` is written, after research and understanding
- its purpose is a final alignment pass at the point of maximum understanding: the agent asks for whatever it still needs to produce a good `Impl.Req` — design clarifications, missing feedback loops, missing inputs — not only design questions
- it is a gap-detector and needs gate, not a documentation mandate — it must not bloat the `Impl.Req`
- bounded: the user stays in-loop as long as they want; then the agent finishes the `Impl.Req` with all accumulated feedback
- governed by `Alignment.Mode` like any `Alignment.Checkpoint`
- its operational definition — the readiness checklist and the resolve-then-raise flow — lives by construction in the skill that declares the checkpoint, not here

****

## Alignment.Checkpoint:Executable

- `Alignment.Checkpoint:Executable` is a named `Alignment.Checkpoint` the executer runs at execution entry, before the git checkpoint and first edit
- it confirms the `Impl.Req` is still executable in the current environment: targeted files and symbols exist, named feedback loops run, the code matches the plan's assumptions, and the plan is followable cold
- it complements `Alignment.Checkpoint:Readiness` — readiness asks "is this a good plan to write?" at design time; executable asks "is this still runnable now?" at execution time, catching drift since the `Impl.Req` was written
- governed by `Alignment.Mode`: `Interactive` raises unresolved mismatches before editing; `Autonomous` records them and proceeds only if faithful, aborting if the plan is no longer executable
- it is a light "still executable?" gate, not a re-run of the readiness checklist; its operational definition lives in the executer skill that declares it

****

## Name.As.Index

- `Name.As.Index` is the property that a `Dotted.Name` is a bidirectional key across all surfaces, not only a forward pointer to a definition
- forward: name → its `Index.Block` definition
- reverse: name → every surface that mentions it — the mention registers that text as being about the concept
- makes natural-text surfaces findable and indexable by concept through plain search, with no hand-maintained concept→surface table
- makes `Cited.Duplication` maintainable: enumerate mentions to detect and align drift — the mechanism `Index.Editor.Maintenance.Pass` already relies on
- the `Index.Skillware` symbol resolves both ways: name→definition and name→usages
- depends on `Dotted.Notation` discipline — only named concepts are reverse-findable; casual prose is not

### meta

- related: `Dotted.Notation`, `Cited.Duplication`, `Inline.Relatedness`, `Index.Editor.Maintenance.Pass`, `Index.Skillware`

****

## Not.A.Wall.Of.Text

- `Not.A.Wall.Of.Text` is an alignment anti-pattern: presenting too much un-aligned content in one turn
- alignment is per-chunk — a wall forces the human to rubber-stamp or disengage (false convergence)
- soft budget ≈ 1–3 blocks / one decision per `Alignment.Maintenance.Turn`
- bounds breadth presented, not depth available — depth stays one pull away (`Appendix.Discovery`)
- exception: content the user explicitly pulls (a requested status print, async artifact) is not a wall

### meta

- related: `Alignment.Maintenance.Turn`, `Hugentic.Alignment`, `Appendix.Discovery`

****

## Independent.Reader.Block

- `Independent.Reader.Block` is a durable block whose full meaning is recoverable by an independent reader holding only the block and the index it cites
- it is a quality every `Kernel.Block` should hold: independence from the writer's context — the conversation that produced it — and from its position on the index surface
- it MAY inline existing blocks: `Dotted.Name` references are durable, resolvable anchors (`Name.As.Index`), not dependencies that break independence
- what breaks independence is deixis — a reference whose meaning depends on the authoring context instead of on a named, resolvable concept
- the writer's context is the primary hazard: distilling a live conversation tempts the author to carry its frame into a surface the reader meets cold
- the fix is positive statement — say what the concept is, not what it is instead of
- extended depth lives in `appendix/Independent.Reader.Block-appendix.md`

****

## Dangling.Cite

- `Dangling.Cite` is a `Concept.Cite` or inline `Dotted.Name` mention pointing to a concept that has no block yet — a valid, intentional forward reference
- it is a feature, not an error: it signals a block worth writing next, and the surrounding text already carries part of the concept's definition
- do NOT strip dangling cites to avoid a "broken reference" — stripping loses the signal and the partial grounding
- distinct from `Unresolved.Index.Name` (a name the agent cannot resolve while reading) — a `Dangling.Cite` is authored deliberately while writing
- offer to land the cited concept as its own block, but never silently remove the cite
