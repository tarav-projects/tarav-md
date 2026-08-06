> $kw: ^index-retrofit-direct-loading-path --context-loading-path
> --step SKILL.md
> --loading-dep SKILL.skw.md^agentos-pkg-batchy-runtime-contract
> --loading-dep SKILL.skw.md^driver-workspace-literacy
> --loading-dep SKILL.skw.md^driver-index-literacy
> --loading-dep SKILL.skw.md^driver-local-surfaces-literacy
> --loading-dep SKILL.skw.md^driver-cli-literacy

# Index.Retrofit.Workflow.Module

> $kw: --from Batchy.Skill.Banner --from Index.Presumption --from Line.Type --from Normal.Turn.Ref --from POI.Instance --from Reviewed.Content --from Support.Set --from Verbatim.User.Gated

Survey an Index depot, propose a bounded retrofit campaign, and supervise transcript-reading research agents that type and ground eligible lines without loading transcript content into the supervisor context.

Canonical call:

```text
$agentos-pkg --index-retrofit --depot <target-depot>
```

`--scope` is an optional override. Without it, compute the campaign scope from the depot's readiness partition, block coherence, `Session.Nomination` strength, and the amount of useful work available for a bounded pass.

## Skill.Index.Section

### Index.Retrofit.Supervisor
- owns depot survey, session nomination, scope selection, work packets, structural validation, anchor registration, support attachment, and the campaign report
- uses only Index, Git, Chatlas session-query, worker-report, Anchory preview, and linter surfaces
- never loads transcript fragments, turn neighborhoods, transcript views, or raw provider artifacts

### Index.Retrofit.Research.Agent
- a read-only subagent that receives one session-centered work packet
- loads the assigned transcript deeply enough to judge typing, current support, or candidate support as selected by the packet action
- returns explicit per-line type and support dispositions without treating a small `Support.Set` as defective by cardinality alone
- never mutates the Index, registers anchors, or broadens its assigned depot/session boundary

### Index.Retrofit.Packet
- one candidate session plus a group of exact Index lines likely grounded there
- carries one action (`retrofit-type`, `retrofit-grounding`, or `full-retrofit`), stable content, content hashes, current locations and blocks, review state, type and support dispositions, current support reference and members when present, nomination evidence, and the allowed session boundary
- is session-centered so one transcript load can research several lines
- its materialized manifest is persisted in the report at dispatch, not held only in the worker prompt

### Session.Nomination
- the act of choosing which session a packet researches; the single highest-leverage decision in a campaign
- signals are not equal, and a wrong nomination costs a whole packet while returning a result that looks like honest absence of support
- ranked by demonstrated reliability in `Session.Nomination.Ladder`; corroborate before dispatch rather than trusting one signal

### Compaction.Boundary
- the point in a `/compact`-continued session before which turns are not indexed and cannot serve as `Support.Set` members
- a session can only ground material authored **after** its boundary, regardless of how strongly it is otherwise nominated
- proven prior authorship does not transfer across it: the same session may land a whole cluster and then return nothing for material authored earlier
- its summary text recaps pre-boundary content and therefore contains the target vocabulary, which makes phrase queries match a session that cannot actually support the lines

### Unreachable.Cluster
- a cluster whose lines have been researched to exhaustion and cannot be grounded from the current corpus
- distinct from `ambiguous`, which means one session failed; unreachable means the candidate set is exhausted or the vocabulary appears in no user turn at all
- known causes: content authored before a `Compaction.Boundary` and never revisited, or agent-authored vocabulary the user never spoke
- retire it in the report with the queries that proved it, so later campaigns do not re-dispatch the same emptiness
- retiring is a reporting act only; the lines keep `Index.Presumption` and are never deleted, weakened, or force-grounded

### Type.Divergence
- two independent research results that agree a legacy body is supported but propose different `Line.Type` codes for it
- neither `residue` (a type does fit) nor `ambiguous` (support exists) — it is a genuine two-candidate typing choice
- a type prefix permanently changes line content, so the supervisor holds the line rather than picking a winner
- record both candidates with their rationales and route the choice to the user as an Index content decision

### Index.Retrofit.Type.Exception
- a narrow workflow authority for adding or replacing one `Line.Type` prefix on an unreviewed line
- exists only after `User.Command::RetrofitType` or `User.Command::FullRetrofit`; grounding-only work never infers this authority
- preserves the body byte-for-byte and cannot type or retype `Reviewed.Content`, rewrite, split, move, or delete a line
- a type change creates new line content; an existing support reference belongs to the old content and cannot remain attached unchanged
- is a workflow-specific exception to the normal verbatim gate, not a general relaxation of `Verbatim.User.Gated`

### Index.Retrofit.Support.Action
- `ground` creates support for typed content with no current `Support.Reference`
- `keep` records that a nominated small set remains sufficient; one decisive user turn may be ideal support
- `expand` mints a successor support reference with additional honest members and the current anchor as predecessor
- `replace` mints a successor when honest review changes the member set without changing line content
- `concern` records a `POI.Instance` when current support appears weak or mismatched but no honest successor is ready; it never silently strips authority

### Index.Retrofit.Campaign.Report
- the single durable live note for survey, dispatch, results, attachment, coverage, and resumability
- begins at `surveyed — campaign not started`; starting a campaign advances the same artifact instead of creating a second queue
- must remain sufficient to resume the campaign in a fresh session with no conversation context

## Invocation And Banner

Resolve `Skill.Arg::Target.Depot`; fail closed when it does not identify one writable Index depot. Resolve any explicit `Target.Scope` as a hard boundary. Then print the `Batchy.Skill.Banner` with:

- module: `Index.Retrofit.Workflow.Module`
- target depot and owning project
- scope: caller-supplied or `computed by supervisor`
- phase: `survey`
- transcript access: `research agents only`
- mutation before campaign start: `campaign report only`

## Survey Pass

The first invocation is always a cheap supervisor pass. Do not spawn agents, load transcripts, mint anchors, or edit Index lines.

1. Read the target's applicable `AGENTS.md`, router, and current Index surfaces.
2. Measure the whole permitted boundary with `agentos index linter --depot <depot> --coverage all --json` and rank blocks with `agentos index blocks --depot <depot> --sort gr-density --json`.
3. Compute two independent readiness axes. Type is `missing`, `revisitable`, `reviewed-frozen`, `adequate`, or worker-returned `residue`; support is `missing`, `thin`, `established`, or `concern`. Determine `Reviewed.Content` through the existing review checks, not by guessing from prose.
4. Scope existing support cheaply with `agentos chatlas anchory sessions` over the selected Index sources. Member cardinality nominates `thin` support for research but never proves weakness.
5. Nominate candidate sessions per cluster using `Session.Nomination.Ladder` below. Record which signals fired and which did not.
6. Run the cheap exhaustion sweep before scoping — see `Cluster Exhaustion Sweep`. Retire zero-signal clusters as `Unreachable.Cluster` instead of scoping them into a pass.
7. Cluster by candidate session first and line group second. A line may appear in several candidate clusters until research resolves it.
8. Compute separate recommended scopes for type work, grounding work, and their full composition; prefer coherent blocks, surviving nomination evidence, and enough related lines to amortize one transcript load.
9. Create or refresh one `notes/live/NNN-<depot>-index-retrofit-campaign.md` in the project that owns the target depot, using `agentos stdlib prefix next` and the live-surface conventions.

## Session.Nomination.Ladder

Ranked by demonstrated reliability. Prefer higher rungs; corroborate a lower rung with a higher one before spending a packet.

1. **User-text phrase query** — the primary signal. `agentos chatlas query --project-base <base> --user-contains '<distinctive phrase>'`. Only user text can become an anchorable member, so only user text predicts support. Query a phrase distinctive to the line, not just the concept name.
2. **Compaction-boundary check** — not a nomination signal but a mandatory filter on every candidate; see below. A candidate that fails it cannot succeed no matter what else fired.
3. **Anchor neighbourhood** — resolve an already-grounded neighbouring block's anchor to its session. Useful, but **corroborate before use**: file adjacency is not authorship, and interleaved blocks are frequently ungrounded precisely because they came from a different session than their grounded neighbours.
4. **Git history** — weak corroboration only. It dates commits, not conversations. **Checkpoint commits ("checkpoint before…", "worktree as found") capture pre-existing working trees and can postdate the authoring by weeks.** Never nominate on a git date alone; use it to rank candidates that a phrase query already produced.

Explicitly weaker than they look:

- `--message-contains` matches assistant text and compaction summaries, so it nominates sessions that cannot support the line. Prefer `--user-contains` for nomination.
- `--file-write` and `--tool-contains` find sessions that *edited* the file, which is often an agent applying an edit whose authorizing conversation happened elsewhere.

Record the nomination evidence in the report. When a packet fails, the evidence is what tells the next pass which signal misled.

## Compaction Boundary Check

Mandatory before dispatching any packet. One query, seconds:

```text
agentos chatlas turns query --identity-hash <session> --sort oldest --limit 1 --json
```

Compare the earliest indexed turn against the target's authoring window. **If the earliest indexed turn postdates the target's introduction, do not dispatch** — the packet cannot succeed. Move to the fallback candidate first.

Skipping this check costs a full packet and returns a result indistinguishable from honest absence of support.

## Cluster Exhaustion Sweep

Before committing a cluster to a pass, run one user-text query per distinctive concept name in it. A concept returning **zero sessions corpus-wide** has no user-touch evidence anywhere and no packet can ground it.

Retire such clusters as `Unreachable.Cluster` with the queries that proved it. The sweep costs a few queries and can retire an entire cluster that would otherwise consume several worker dispatches to disprove.

## Campaign Report

Keep the report compact and operational, and sufficient to resume cold:

- `Index.Retrofit.Abstract` — depot, coverage before and after each pass, explicit boundary, per-action computed scopes, both readiness axes, state, and the survey commands actually run
- `Index.Retrofit.Clusters` — stable cluster ids, candidate session identities with their nomination evidence, exact target lines or bodies with content hashes, review state, type disposition, support disposition and member count, and selection rank
- `Index.Retrofit.Work` — one row per packet plus, for every dispatched packet, its **materialized manifest**: packet-local line ids, block, file line, content hash, typed marker, and exact content. Packet state is `surveyed`, `queued`, `researching`, `supported`, `held`, `ambiguous`, `residue`, `unreachable`, `attached`, or `stale`, plus the worker model class used
- `Index.Retrofit.Log` — nomination outcomes, structural failures, retries, model escalations, type migrations, held divergences, scope changes, infrastructure interruptions, and coverage after completed passes

Persist the manifest at dispatch, not after. Once a packet is dispatched, its exact identity otherwise exists only inside the worker prompt, and the campaign stops being resumable.

Never store transcript fragments in the report. Exact `Normal.Turn.Ref` coordinates, hints, and worker rationales are sufficient.

Record coverage denominators with their meaning. The linter meter counts all index lines and coverage-eligible blocks; the blocks meter counts kernel lines. Reporting both unlabeled reads as a contradiction.

## Survey Checkpoint

After landing the report, return its path, coverage summary, both readiness axes, retired clusters, per-action recommended cluster sets, expected packet counts, and the commands currently available. Offer only commands that have eligible work in the selected boundary. Stop until the user supplies a declared command; that command selects the retrofit authority and resource boundary.

## Retrofit Execution

Every action command uses the same supervisor loop:

1. Re-read the report and revalidate exact content, current support reference, and review state; drop drifted lines as `stale`.
2. Select only lines eligible for the commanded action and chosen cluster boundary.
3. Run the `Compaction Boundary Check` on every candidate session; reorder to the fallback when the primary fails.
4. Persist each packet's action and materialized manifest, then spawn read-only `Index.Retrofit.Research.Agent`s using `references/index-retrofit-worker.md` and the worker-economics policy below.
5. Keep the supervisor transcript-blind. Consume only worker result objects and cheap command results.
6. Aggregate session-local results per line, hold `Type.Divergence`, and preserve honest `ambiguous`, `residue`, `unreachable`, and `concern` outcomes.
7. Apply only structurally valid results allowed by the selected action, lint the edited scope, refresh coverage, and survey the remaining boundary cheaply.

### Retrofit Type Action

- `User.Command::RetrofitType` grants `Index.Retrofit.Type.Exception` for missing or revisitable types on unreviewed lines
- skip `Reviewed.Content` as `reviewed-frozen`; a suspected type problem there becomes a POI for the normal gated edit path
- preserve the body byte-for-byte; allow only adding one prefix or replacing the existing prefix
- when type changes, detach any support reference bound to the old typed content and mark the resulting line `support: missing`; preserve the old anchor record for later predecessor-aware recovery
- hold `Type.Divergence` and `residue` without mutation

### Retrofit Grounding Action

- `User.Command::RetrofitGrounding` never changes `Line.Type` or body and may operate on reviewed or unreviewed lines
- `missing` support may become `ground`; `thin` or nominated existing support may become `keep`, `expand`, `replace`, or `concern`
- use current members and assigned-session research to judge support; cardinality is only a nomination signal
- for `expand` or `replace`, batch-preview and mint a successor anchor with the current anchor in `predecessors`, then replace only the trailing support reference
- preserve every gate-evidence member and its member types when operating on `Reviewed.Content`
- a `concern` without an honest successor records a POI and leaves the current reference unchanged pending the later evaluation mechanism

### Full Retrofit Action

- `User.Command::FullRetrofit` composes type work first and grounding work second against the resulting exact content
- reviewed lines are type-frozen but remain eligible for grounding work
- when both results succeed, land the type delta and final support reference together
- when type succeeds but support remains ambiguous, land only the authorized type delta, detach support belonging to the old content, and record the honest partial state as `support: missing`
- `full` means all currently implemented type and support retrofit work, not future semantic validation or reconciliation

Do not pause between valid packets for user approval. The selected action command authorizes its bounded retrofit work; no action may infer the authority of another.

## Worker Economics

- dispatch transcript-research packets to the runtime's medium-size, context-efficient model class with medium reasoning by default
- treat the semantic model class as policy; resolve its current concrete model id at runtime rather than baking a provider-specific id into the skill
- never use a large or frontier model for ordinary packet work
- escalate only an unresolved packet whose strong nomination evidence suggests that the medium worker's ambiguity is capability-limited rather than an honest absence of support
- record the original model class, escalation reason, and escalated model class in `Index.Retrofit.Log`
- avoid speculative duplicate workers and dispatch only the concurrency justified by the selected bounded campaign
- packets targeting different files and different sessions may run concurrently; they cannot interfere with each other's relocation or attachment
- never place two packets on the same file concurrently — the second would relocate against content the first is mutating

## Structural Validation And Attachment

For each worker result:

- relocate the current line by exact `Line.Type + body` or exact untyped body rather than trusting a stale line number
- reject the result as `stale` if content, support reference, or review state changed after dispatch
- for a type delta, require `Index.Retrofit.Type.Exception`, prove the line is not `Reviewed.Content`, require an allowed type code, and verify body identity after removing the old and proposed prefixes
- for support work, run Anchory preview or batch preview against the exact final typed content without context detail
- require resolvable user turns, one exact line-bound relationship per distinct line content, and no conflicting equivalent anchor
- register only after preview succeeds; the supervisor owns all allocation so workers cannot race or create orphans
- register every anchor in a packet before writing any line, and abort the whole packet on the first registration failure — a partial write leaves the file inconsistent with the report
- for grounding-only work, replace only the trailing reference while preserving `Line.Type + body` verbatim
- for type-only work, change only the prefix and detach any support reference bound to the prior content
- for full work, materialize exactly the authorized prefix delta, unchanged body, and final trailing support reference
- verify unlanded lines were left untouched, then run focused provenance and coverage lint after attachment

Two mechanics the gate enforces, worth knowing before scoping:

- `--line-content` accepts only a **typed** Index line. An untyped body cannot receive a line-bound anchor at all, which is why its type disposition is `missing` rather than merely unresearched.
- anchor members must be **resolvable user turns**. Assistant drafts and tool or apply turns are rejected by preview, so a result whose support collapses to "the agent drafted it and the patch applied it" cannot land.

Anchor registration and trailing `Support.Reference` maintenance are agent-owned metadata operations. A type prefix delta is allowed only through `Index.Retrofit.Type.Exception`. If research implies any body change, leave the line untouched and route that separate edit through its normal verbatim gate.

## User.Command.Section

### User.Command::RetrofitType
- execute type gap-fill or type review over an eligible bounded cluster
- triggers: `::retrofit-type`
- available: when the foreground report contains `missing` or `revisitable` type work on unreviewed lines
- action: grant `Index.Retrofit.Type.Exception`, dispatch type research, and land only structurally valid prefix deltas

#### User.Command.Arg::Cluster
- the cluster id or set to execute
- required: false
- resolution: Defaulted
- default: the report's recommended type cluster set

### User.Command::RetrofitGrounding
- execute missing-support recovery, existing-support review, or support expansion over a bounded cluster
- triggers: `::retrofit-grounding`
- available: when the foreground report contains `missing`, `thin`, or `concern` support work
- action: dispatch support research and autonomously keep, ground, expand, replace, or report concern without changing line content

#### User.Command.Arg::Cluster
- the cluster id or set to execute
- required: false
- resolution: Defaulted
- default: the report's recommended grounding cluster set

### User.Command::FullRetrofit
- compose all eligible type and support work over one bounded cluster
- triggers: `::full-retrofit`
- available: when the foreground report contains any current retrofit work
- action: grant the union of type and grounding authority, execute in content-dependency order, and preserve honest partial states

#### User.Command.Arg::Cluster
- the cluster id or set to execute
- required: false
- resolution: Defaulted
- default: the report's recommended full-retrofit cluster set

### User.Command::Resurvey
- refresh the cheap depot report without spawning agents or changing Index content or support
- triggers: `::resurvey`
- available: whenever a foreground campaign report resolves uniquely and no packet is attaching
- action: recompute readiness, support cardinality, nomination, clusters, and per-action recommendations

### User.Command::CampaignStatus
- report current packet counts, action states, attachments, concerns, and coverage without changing state
- triggers: `::campaign-status`
- available: whenever one foreground campaign report resolves uniquely
- action: read and summarize the campaign report

### User.Command::StopAfterCurrent
- stop dispatching new packets after already-running research agents return
- triggers: `::stop-after-current`
- available: while a retrofit action is active
- action: preserve returned results, finish safe structural checks already underway, and leave undispatched packets queued

## Known Failure Modes

Each of these has cost a real packet. Recognize them by shape rather than rediscovering them.

- **Checkpoint-commit dating** — a commit message like "checkpoint before X" captures a working tree as found; its date can postdate the authoring conversation by weeks. Symptom: a confidently nominated session returns all-ambiguous.
- **Compaction boundary** — the authoring turns sit before the session's indexed window. Symptom: the only hits for the target vocabulary are inside an auto-generated summary. Prevented by the boundary check.
- **Adjacency mistaken for authorship** — a session nominated because neighbouring blocks resolve to it. Symptom: the neighbours are grounded and the targets are not, which is itself evidence they came from different sessions.
- **Shared-turn stretching** — a family of lines all resting on one broad user turn. Symptom: identical member sets across lines making materially different claims. Reject at the gate.
- **Stage-mismatched support** — a turn that discusses the subject before the line's terms were coined. Symptom: the worker's own rationale concedes the terms are not yet present. Reject; adjacency in time is not support for this line's content.
- **Agent-authored vocabulary** — the concept exists only in agent output. Symptom: zero user-text hits corpus-wide. Retire as `Unreachable.Cluster`.
- **Infrastructure interruption** — a worker dies mid-research. A partial run returns no result contract and must never be mined for findings; its observations are search hints only.

## Discipline

- never let the supervisor inspect transcript content to double-check a worker; requeue uncertain work instead
- never let a worker register or attach an anchor
- never infer type authority from grounding work, review state from typography, or full-retrofit authority from either narrower command
- never force a legacy body into the vocabulary; preserve honest `residue`
- never resolve a `Type.Divergence` by supervisor preference; hold it for the user
- never share one line-bound anchor across different line content, even when several lines use the same support members
- never treat Git timing, Chatlas query matches, or compaction-summary text as semantic support
- never accept a partial or interrupted worker run as a finding; only a returned result contract counts
- never weaken the result merely to improve coverage; unresolved lines retain `Index.Presumption`
- treat an all-ambiguous packet as a correct result — the deliverable is accuracy, not landing rate
- preserve the campaign report as the only workflow ledger, and keep it resumable without conversation context
