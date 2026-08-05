# Agentos.Pkg Delta-Home Backfill Supervisor

## Goal

Give every grounded `agentos-pkg` Project `Index.Line` an exact `Chat.Index.Delta` home by returning to its supporting chat and extracting only the semantic region needed for the assigned Project block.

This is a targeted Project-to-Chat reconciliation campaign, not a requirement to complete every source chat's semantic index in one pass.

## Verified Baseline

Checked on 2026-08-05:

- Project lines: 2,846
- `Project.Line.Home.Missing`: 2,846
- `Project.Line.Head.Missing`: 2,846
- mandatory Project support chats: 31
- Chat.Indexes missing: 30
- Chat.Indexes available as valid v2: 0
- legacy-v1 Chat.Indexes requiring explicit replacement: 1
- total reconciliation findings: 5,723

The regular Index linter already runs the external check `Project lines are represented by registered support Chat.Indexes`; it currently fails with all 5,723 advisory findings. `agentos-chatlas-py/tests/test_project_index_reconciliation.py` already proves that Project-first lines produce `Project.Line.Home.Missing` and that the finding clears after Delta materialization. No new linter check is required for this campaign.

Reproduce the baseline:

```sh
agentos index linter --depot agentos-md/skills/agentos-pkg --json
agentos chatlas project-index audit --depot agentos-md/skills/agentos-pkg --json
```

The work queue begins in `agentos-md/skills/agentos-pkg/009-SUPPORT-CHATS.md`.

## Campaign Invariants

- The Project line is a reconciliation candidate, not evidence that proves itself.
- Read the authoritative Chatlas transcript data exposed by `chat-index scaffold` as `evidence.json`. Do not use a transcript summary, another Chatlas product, or the Project Index as semantic evidence.
- Materialize the exact canonical Project line only when the source-chat prefix supports that extraction.
- If the transcript does not support the line, leave the missing-home finding open and report support drift; do not force a match to silence the linter.
- A Delta may interpret only evidence at or before its `Delta.Horizon.Turn`.
- Prefer the user turn that actually touches the line. Assistant content may inform interpretation but cannot independently ground it.
- Use the existing line anchor when validation accepts it as exact and line-bound. Otherwise propose support from the qualifying source turn and let Chatlas ensure the line anchor.
- Set `status` to `partial` and record the bounded block-reconciliation scope in `findings` unless the agent genuinely captures the complete chat prefix.
- An ordinary Project line enters `Chat.Index.HEAD` only when it remains current in the inspected chat prefix. Delta containment proves historical home; it does not prove present agreement.
- A remaining `Project.Line.Head.Missing` finding may therefore reveal real model drift and must not be cleared mechanically.

## Parallel Work Unit

The discovery unit is one randomly selected Project block. The exclusive mutation unit is one support-chat identity.

One supervisor owns scheduling and coordination state while several subagents perform bounded transcript review and Chat.Index capture. Different subagents may process different chat identities concurrently. The supervisor never dispatches two live workers against the same chat, even when their Project blocks differ. Chatlas locking and base-fingerprint checks remain final safety nets rather than the scheduler.

Random block selection supplies breadth. Once the supervisor assigns a worker under a chat lease, anchor-based discovery supplies locality by exposing additional unclaimed blocks that can be landed in the same Chat.Index pass. The identity `fb3b...ab38` is the legacy-v1 exception and must use explicit `replace-legacy-v1` mode.

A worker receives one bounded `(Project block, support chat)` slice:

```text
coordination note: agentos-md/notes/live/609-agentos-pkg-delta-home-backfill.md
project block: <exact block_path>
support chat: <full identity hash>
candidate lines: <exact audit findings assigned to this slice>
scope: verify and land supported Delta homes, then report chat-local block candidates
```

Workers do not select or claim work, edit this note, or mutate coordination state. They return structured results to the supervisor, which alone advances claims and leases.

## Coordination Surface

Use one shared, disposable coordination root:

```text
agentos-md/.agentos/state/delta-home-backfill/
├── blocks/       # one atomic WIP or done claim per Project block
├── chat-leases/  # one exclusive writer lease per Chat.Index identity
└── reports/      # append-only worker completion reports
```

The coordination state is operational rather than Project Index truth. The Project audit and the materialized Chat.Indexes remain authoritative for actual completion. The supervisor is its only writer; filesystem claims still protect against another independently launched supervisor.

### Block Claim

1. The supervisor chooses a random block that still has `Project.Line.Home.Missing` findings.
2. It derives a stable filename-safe key from the exact `block_path`.
3. It atomically creates the WIP claim under `blocks/`; success grants ownership, while an existing claim causes another selection.
4. It records the exact block path, supervisor/session identity, claim timestamp, pending support chats, and dispatched workers.
5. It keeps the block WIP while its lines are processed across support chats.
6. It marks the block done only when every candidate line has a Delta home or the report records each inspected support-drift remainder.

A stale WIP claim is never stolen automatically. The supervisor decides whether to release or reassign it after inspecting its owner and timestamp.

### Chat Lease

- The supervisor atomically acquires `chat-leases/<full-identity-hash>/` before dispatching a worker that may scaffold or apply that Chat.Index.
- One lease names exactly one assigned worker; a supervisor may hold several leases only when they belong to concurrently running workers on distinct chats.
- A worker handles only its assigned chat and never acquires another lease itself.
- The supervisor releases the lease after accepting the worker report and confirming the Chat.Index and follow-up Project audits.
- A fingerprint conflict still requires a fresh scaffold even when the lease appears valid.
- Read-only inspection does not require a lease; mutation always does.

### Locality Loop

After landing the assigned block's lines for one chat, the worker uses the resolved anchor-to-session mapping to discover other Project blocks supported by that same chat. This inspection is free. The worker reports candidates but does not claim them.

While retaining the chat lease, the supervisor:

1. filters the returned candidates against current missing-home findings
2. skips blocks already WIP or done
3. atomically claims one or more available blocks
4. sends a follow-up task to the same worker for another chat-local batch
5. repeats while useful work remains on that chat

The supervisor then confirms the final audits, releases the chat lease, finishes or retains each block claim according to its remaining support chats, and fills the free worker slot from another random unclaimed block. This combines random breadth with chat-local extraction efficiency.

## Supervisor Procedure

1. Read applicable project guidance and this complete note.
2. Initialize the coordination root and run the Project reconciliation audit.
3. Build the current candidate set by `block_path`, anchors, and supporting chat identities.
4. Fill available subagent slots by randomly claiming blocks and leasing distinct chats.
5. Give each subagent one explicit block/chat slice and the Worker Procedure below.
6. Continue doing mechanical scheduling and audit work while subagents run.
7. On each result, verify the landed Chat.Index audit and Project-audit change before accepting it.
8. Prefer a chat-local follow-up for newly discovered blocks; otherwise release the lease and dispatch fresh random work.
9. Persist accepted reports and update block state itself. Workers never touch coordination state.
10. Continue until no claimable work remains, all subagent slots are blocked, or the campaign completion condition is met.

The supervisor must remain responsive: do not wait on one worker while another slot can make progress. Never invent completion from a worker narrative when the read-only audits disagree.

## Worker Procedure

### 1. Select Candidate Lines

Use only the supervisor-assigned block/chat slice. Confirm its `Project.Line.Home.Missing` findings and anchor membership before semantic work; report assignment drift instead of silently expanding scope.

```sh
agentos chatlas project-index audit \
  --depot agentos-md/skills/agentos-pkg \
  --json

agentos chatlas anchory resolve <anchor> --detail context --json
```

Preserve the exact `Line.Type + body`; omit the Project line's trailing anchor when authoring `plan.json` because the renderer owns Delta anchors.

### 2. Scaffold From The Actual Transcript

Use a fresh temporary directory and the full assigned identity hash:

```sh
agentos chatlas chat-index scaffold \
  --identity-hash <identity-hash> \
  --stage <empty-stage-directory> \
  --json
```

- `create`: first partial materialization for a missing Chat.Index.
- `maintain-v2`: preserve untouched Deltas and add or replace only the assigned horizons.
- `replace-legacy-v1`: pass this mode explicitly only for `fb3b...ab38`; it replaces the old resolved layout rather than editing it in place.

Read all transcript context needed to decide the assigned lines. Group supported lines by a qualifying user horizon. Several lines may share one Delta; several Deltas may represent one Project block.

### 3. Author The Partial Capture Plan

Edit only the semantic region of scaffolded `plan.json`:

- add assigned horizon-based `delta_edits`
- use exact typed line content without trailing anchors
- reuse exact accepted support anchors or propose qualifying support members
- author the partial present-facing `head.blocks`
- set `status` to `partial`
- add a concrete finding such as `Targeted reconciliation of <Project.Block>; other chat semantics remain uninspected.`

For `maintain-v2`, omitted Deltas are preserved. Preserve the old HEAD only when the pass adds historical homes without making any current-model judgment; otherwise replace HEAD with the complete resulting partial HEAD, retaining all still-current prior lines.

### 4. Validate, Apply, Audit

```sh
agentos chatlas chat-index validate --plan <stage>/plan.json --json
agentos chatlas chat-index apply --plan <stage>/plan.json --json
agentos chatlas chat-index audit --identity-hash <identity-hash> --json
agentos chatlas project-index audit --depot agentos-md/skills/agentos-pkg --json
```

Do not apply until validation succeeds. If another writer changed the same Chat.Index, discard the stale scaffold, scaffold again, and reapply the semantic edit to the fresh plan.

### 5. Report

Return:

```text
chat identity: <hash>
project blocks inspected: <paths>
candidate lines: <count>
Delta homes added: <count>
Chat HEAD occurrences added: <count>
unsupported/drifted lines: <count + exact findings>
Deltas created/edited: <horizon turns>
Chat.Index audit: <ok + finding counts>
Project audit change: Home.Missing <before -> after>; Head.Missing <before -> after>
materialized path: <path>
other blocks discovered on this chat: <block paths + candidate counts>
```

## Supervisor Completion Loop

1. Keep distinct-chat subagents busy while claimable work remains.
2. Rerun the Project audit after each accepted landing and mark only mechanically cleared exact-line findings as done.
3. Requeue remaining blocks within already materialized chats through `maintain-v2`.
4. Escalate stale claims, unsupported lines, and HEAD disagreement as explicit reconciliation work.
5. Finish when `Project.Line.Home.Missing` is zero or every remainder has an inspected support-drift report.

## Progress Ledger

| Support chat | Assigned blocks | Owner/session | State | Homes added | Notes |
|---|---|---|---|---:|---|
| _derived_ | _see coordination state_ | — | ready | 0 | The table is a human projection; claims and audits decide state. |
