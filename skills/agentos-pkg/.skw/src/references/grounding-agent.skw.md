> $kw: ^grounding-agent-direct-loading-path --context-loading-path
> --step SKILL.md
> --loading-dep SKILL.skw.md^agentos-pkg-batchy-runtime-contract
> --loading-dep SKILL.skw.md^driver-workspace-literacy
> --loading-dep SKILL.skw.md^driver-index-literacy
> --loading-dep SKILL.skw.md^driver-local-surfaces-literacy
> --loading-dep SKILL.skw.md^driver-cli-literacy

# Grounding.Agent.Workflow.Module

> $kw: --from Batchy.Skill.Banner --from Index.Presumption --from Line.Type --from Line.Type.Vocabulary --from Normal.Turn.Ref --from Support.Set --from Verbatim.User.Gated

Survey an Index depot, propose a useful grounding campaign, and supervise transcript-reading research agents without loading transcript content into the supervisor context.

Canonical call:

```text
$agentos-pkg --grounding-agent --depot <target-depot>
```

`--scope` is an optional override. Without it, compute the campaign scope from the depot's grounding deficit, block coherence, Git history, candidate-session strength, and the amount of useful work available for a bounded pass.

## Skill.Index.Section

### Grounding.Supervisor.Agent
- owns depot survey, Git archaeology, session hints, scope selection, work packets, structural validation, anchor registration, support attachment, and the campaign report
- uses only Index, Git, Chatlas session-query, worker-report, Anchory preview, and linter surfaces
- never loads transcript fragments, turn neighborhoods, transcript views, or raw provider artifacts

### Grounding.Research.Agent
- a read-only subagent that receives one session-centered work packet
- loads the assigned transcript deeply enough to judge support and returns one proposed `Support.Set` or an honest ambiguous result for each distinct line content
- when the packet carries explicit type-migration authority, also classifies legacy untyped bodies against the applicable `Line.Type.Vocabulary`
- never mutates the Index, registers anchors, or broadens its assigned depot/session boundary

### Grounding.Work.Packet
- one candidate session plus a group of exact Index lines likely grounded there
- carries stable typed content or exact legacy untyped bodies, content hashes, current locations and blocks, typing disposition, Git timing hints, cheap query hints, and the allowed session boundary
- is session-centered so one transcript load can research several lines

### Legacy.Type.Migration.Exception
- a narrow campaign authority for adding one `Line.Type` prefix to an existing untyped body and grounding the resulting typed content atomically
- exists only after `User.Command::StartCampaignWithTyping`; ordinary grounding campaigns never infer this authority
- preserves the legacy body byte-for-byte and cannot retype, rewrite, split, move, or delete a line
- is a workflow-specific exception to the normal verbatim gate, not a general relaxation of `Verbatim.User.Gated`

### Grounding.Campaign.Report
- the single durable live note for survey, dispatch, results, attachment, coverage, and resumability
- begins at `surveyed — campaign not started`; starting a campaign advances the same artifact instead of creating a second queue

## Invocation And Banner

Resolve `Skill.Arg::Target.Depot`; fail closed when it does not identify one writable Index depot. Resolve any explicit `Target.Scope` as a hard boundary. Then print the `Batchy.Skill.Banner` with:

- module: `Grounding.Agent.Workflow.Module`
- target depot and owning project
- scope: caller-supplied or `computed by supervisor`
- phase: `survey`
- transcript access: `research agents only`
- mutation before campaign start: `campaign report only`

## Survey Pass

The first invocation is always a cheap supervisor pass. Do not spawn agents, load transcripts, mint anchors, or edit Index lines.

1. Read the target's applicable `AGENTS.md`, router, and current Index surfaces.
2. Measure the whole permitted boundary with `agentos index linter --depot <depot> --coverage all --json` and rank blocks with `agentos index blocks --depot <depot> --sort gr-density --json`; separately count already typed lines and legacy untyped bodies.
3. For promising ungrounded blocks, use Git history to estimate content-bearing commits and discussion windows. Prefer line/block history over repository-wide archaeology.
4. Use only session-level Chatlas queries such as `--file-write`, `--tool-contains`, and `--message-contains`. Record candidate session identities and why each query nominated them; do not request turn detail or transcript views.
5. Partition candidate lines mechanically as `groundable` when already typed or `typing-required` when legacy untyped; only an authorized research result may later classify an untyped body as `residue`. Then cluster by candidate session first and line group second. A line may appear in several candidate clusters until research resolves it.
6. Compute the recommended bounded scope by preferring high grounding deficit, coherent blocks, strong session hints, and enough related lines to amortize one transcript load.
7. Create or refresh one `notes/live/NNN-<depot>-grounding-campaign.md` in the project that owns the target depot, using `agentos stdlib prefix next` and the live-surface conventions.

## Campaign Report

Keep the report compact and operational:

- `Grounding.Abstract` — depot, coverage before, explicit boundary, computed scope, typed/untyped/residue counts, state, and survey commands
- `Grounding.Clusters` — stable cluster ids, candidate session identities, exact target lines or legacy bodies with content hashes, typing disposition, cheap evidence hints, and selection rank
- `Grounding.Work` — packet state: `surveyed`, `queued`, `researching`, `supported`, `ambiguous`, `residue`, `attached`, or `stale`, plus the worker model class used
- `Grounding.Log` — structural failures, retries, model escalations, type migrations, scope changes, and coverage after completed passes

Never store transcript fragments in the report. Exact `Normal.Turn.Ref` coordinates, hints, and worker rationales are sufficient.

## Survey Checkpoint

After landing the report, return its path, coverage summary, readiness partition, recommended cluster set, expected packet count, and the commands currently available. Offer `::start-campaign-with-typing` only when the selected boundary contains eligible legacy untyped bodies. Stop until the user supplies a declared command. This checkpoint controls agent work and resource use; only the typing-capable command grants the narrow migration exception below.

## Campaign Execution

After `User.Command::StartCampaign`:

1. Re-read the report and revalidate that its target lines remain current.
2. Convert only `groundable` typed lines in the selected cluster set into session-centered work packets; leave `typing-required` and `residue` lines unchanged in the report.
3. Spawn read-only `Grounding.Research.Agent`s using `references/grounding-worker.md` and the worker-economics policy below; use available concurrency without placing multiple agents on the same packet.
4. Keep the supervisor transcript-blind. Consume only worker result objects and cheap command results.
5. Record every returned line result in `Grounding.Work`; `ambiguous` is a valid result and never becomes a weak anchor.
6. Structurally validate each `supported` result, register its anchor, append the trailing support reference, and lint the edited scope.
7. Refresh coverage, close the bounded pass, and survey the remaining boundary cheaply. Offer another campaign only when useful work remains.

Do not pause between valid packets for user approval. `::start-campaign` authorizes the bounded campaign; support-reference maintenance does not change line verbatim.

After `User.Command::StartCampaignWithTyping`, follow the same execution loop with these changes:

1. Include `groundable` and `typing-required` lines, mark the packet with explicit `Legacy.Type.Migration.Exception` authority, and supply the applicable `Line.Type.Vocabulary`.
2. Require the worker to return both an honest type classification and a nonempty `Support.Set` for every legacy untyped body it supports.
3. Treat type uncertainty as `residue` and support uncertainty as `ambiguous`; neither permits a file change.
4. For a successful legacy result, construct the exact typed candidate, preview and register support against that typed content, then land the type prefix and trailing support reference together.
5. Record the original body, resulting typed content, worker rationale, support members, and delegated command authority in `Grounding.Log` for later quality evaluation.

This is an atomic type-and-ground migration. Never leave a newly typed line ungrounded, and never use the exception to modify an existing type or any byte of the legacy body.

## Worker Economics

- dispatch transcript-research packets to the runtime's medium-size, context-efficient model class with medium reasoning by default
- treat the semantic model class as policy; resolve its current concrete model id at runtime rather than baking a provider-specific id into the skill
- never use a large or frontier model for ordinary packet work
- escalate only an unresolved packet whose strong session hints suggest that the medium worker's ambiguity is capability-limited rather than an honest absence of support
- record the original model class, escalation reason, and escalated model class in `Grounding.Log`
- avoid speculative duplicate workers and dispatch only the concurrency justified by the selected bounded campaign

## Structural Validation And Attachment

For each worker-proposed `Support.Set`:

- relocate an existing typed line by `Line.Type + body`, or a legacy line by its exact untyped body, rather than trusting a stale line number
- reject the result as `stale` if the dispatched typed content or legacy body changed
- for a legacy migration, require explicit packet authority, an allowed type code, an unchanged body, and no pre-existing type prefix
- run `agentos chatlas anchory preview --line-content <exact-line> --member <session>:<turn-id> ... --hint <hint>` without context detail
- require resolvable user turns, one exact line-bound relationship per distinct line content, and no conflicting equivalent anchor
- register only after preview succeeds; the supervisor owns all allocation so workers cannot race or create orphans
- for ordinary grounding, append only the trailing anchor while preserving `Line.Type + body` verbatim
- for an authorized legacy migration, replace the untyped line with exactly `Line.Type + unchanged body + trailing anchor` as one operation
- run focused provenance and coverage lint after attachment

Anchor registration and trailing `Support.Reference` maintenance are agent-owned metadata operations. The legacy type prefix is allowed only through the explicit exception above. If research implies any other material line change, leave the line untouched and route that separate edit through its normal verbatim gate.

## User.Command.Section

### User.Command::StartCampaign
- begin the bounded supervisor/agent campaign described by the current report
- triggers: `::start-campaign`
- available: after a survey report foregrounds one or more `groundable` typed lines, or after a completed pass finds another useful typed cluster set
- action: select the requested cluster or the report's recommendation, spawn research agents for already typed lines only, and autonomously attach structurally valid support

#### User.Command.Arg::Cluster
- the cluster id or set to execute
- required: false
- resolution: Defaulted
- default: the report's recommended cluster set

### User.Command::StartCampaignWithTyping
- begin a bounded type-and-ground migration over the current report
- triggers: `::start-campaign-with-typing`
- available: after a survey report foregrounds one or more `typing-required` legacy lines, or after a completed pass leaves an eligible typed-migration cluster
- action: grant `Legacy.Type.Migration.Exception` for the selected boundary, spawn research agents, and autonomously land only atomic type-plus-support results

#### User.Command.Arg::Cluster
- the cluster id or set to execute
- required: false
- resolution: Defaulted
- default: the report's recommended cluster set containing eligible typed or legacy-untyped lines

### User.Command::Resurvey
- refresh the cheap depot report without spawning agents or changing support
- triggers: `::resurvey`
- available: whenever a campaign report is foregrounded and no packet is being attached
- action: recompute coverage, session hints, clusters, and recommended scope

#### User.Command.Arg::Scope
- an optional replacement hard boundary for subsequent survey and campaign work
- required: false
- resolution: Contextual

### User.Command::CampaignStatus
- report current packet counts, attachments, ambiguity, and coverage without changing state
- triggers: `::campaign-status`
- available: whenever one foreground campaign report resolves uniquely
- action: read and summarize the campaign report

### User.Command::StopAfterCurrent
- stop dispatching new packets after already-running research agents return
- triggers: `::stop-after-current`
- available: while a campaign pass is active
- action: preserve returned results, finish safe structural checks already underway, and leave undispatched packets queued

## Discipline

- never let the supervisor inspect transcript content to double-check a worker; requeue uncertain work instead
- never let a worker register or attach an anchor
- never infer type-migration authority from a normal campaign command or from the presence of untyped lines
- never force a legacy body into the vocabulary; preserve honest `residue`
- never share one line-bound anchor across different line content, even when several lines use the same support members
- never treat Git timing or Chatlas query matches as semantic support
- never weaken the result merely to improve coverage; unresolved lines retain `Index.Presumption`
- preserve the campaign report as the only workflow ledger
