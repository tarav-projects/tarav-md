---
name: chatlas-session-continue
description: Resolve a prior Chatlas session from a session id, session URI, or provider-agnostic query, source its conversation from the `zip-transcript-summary` product (producing it when missing), and return a continuation handoff artifact for resuming the discussion here. USE WHEN the goal is to continue work from another chat while keeping all user turns verbatim. Called like a terminal command — `--session <id|uri|query>`.
---

# Chatlas Session Continue

Operational `Package.Aux.Skill` under `tarav-chatlas-pkg`.

Return a continuation handoff for a prior chat session so the discussion can resume in the current chat.

This skill must run as an agent by default, not inline in the caller context. `agentos chatlas` handles deterministic resolution and extraction from the maintained chat dataset. The agent always returns a handoff artifact oriented toward continuation, not just transcript recovery.

This is a `Batchy.Skill` — called like a terminal command. Load `tarav-batchy-skills` for the full convention.

- `-h` / `--help` prints the help into the chat instead of running (`Batchy.Skill.Help`).
- a bare session id, URI, or query resolves to `--session`.

## Skill.Arg.Section

### Skill.Arg::Session
- the prior session to continue: a session id, a session URI, or a provider-agnostic query
- required: true
- help: "the session to continue (id, URI, or query)"
- examples: --session "agentos://chat-session/..."

### Skill.Arg::Produce
- whether a missing or stale `zip-transcript-summary` product may be produced during this run
- required: false
- default: true
- type: flag
- flags: --no-produce
- help: "skip production and read the raw transcript view instead"

## Trigger Boundary

Use this skill when the user wants to continue a discussion from another session in the current chat.

Do not use it for:

- recapping the current live chat inline
- quote-accurate archival output
- generic session management unrelated to continuing the discussion here
- transcript compression when no continuation handoff is needed

## Execution Mode

- Run this skill in a separate agent by default.
- Do not perform the extraction and handoff compression inline in the caller context unless the user explicitly asks for that fallback.
- The point of this skill is to keep transcript-processing work and handoff synthesis out of the caller context.

## Use This Skill When

- The user gives a session id, session URI, or session query and wants to continue that discussion here.
- The caller needs the prior session turned into a handoff artifact optimized for resumption.
- The caller wants all user turns preserved exactly while assistant turns are compressed.

## Continuation Quality Bar

Hold the output to this quality bar:

1. **Zero user-turn loss**: preserve every user turn in full and verbatim.
2. **Continuation-first output**: make it obvious what the current goal, accepted decisions, constraints, unresolved issues, and best next move are.
3. **Minimal assistant redundancy**: compress assistant content aggressively when it repeats or adds no new state.
4. **Maximum scannability**: make the artifact easy to continue from quickly without pretending it is the original transcript.

## Workflow

1. Resolve the session.
2. Source the conversation, preferring the `zip-transcript-summary` product and
   producing it when it is missing or stale.
3. Derive continuation state from the session.
4. Compress the assistant turns — fallback path only.
5. Return only the continuation handoff artifact.

## Missing Input

If the user provides neither:

- a session id
- a session URI
- nor a provider-agnostic session query

stop and return this short failure shape:

```text
Could not resolve a prior session because no session identifier or query was provided.
Provide one of:
- a session id
- an agentos://chat-session/... URI
- an identity hash
- another Chatlas index selector that resolves exactly one session
```

## Step 1: Resolve The Session

Use option-based selectors only. Chatlas has no positional session argument.

If the input is already an `agentos://chat-session/...` URI, use `--uri <uri>`.
If it is a session id, use `--session-id <id>`. If it is an identity hash or a
hash prefix, use `--identity-hash <hash>`.

Otherwise resolve a free-text query with the content filters:

```bash
agentos chatlas query --message-contains "<text>" --sort newest --limit 10 --json
```

Related filters worth reaching for: `--user-contains`, `--assistant-contains`,
`--display-name`, `--project-base`, `--file-touched`, `--tool-name`,
`--min-user-turns`, `--active-after`. Repeat a filter to AND it.

Chatlas renders human-readable text by default, so pass `--json` on every step
whose output you parse.

Resolution rules:

- If exactly one row matches, use its `uri` and `identity_hash`.
- If no row matches, fail clearly and say the session could not be found.
- If more than one row matches, do not guess. Return this short ambiguity report shape:

```text
Multiple prior sessions matched the query. I did not choose one automatically.

Candidates:
- provider: <provider> | session_id: <session-id> | uri: <uri>
- provider: <provider> | session_id: <session-id> | uri: <uri>

Reply with the exact `session_id` or `uri` to continue.
```

## Step 2: Source The Conversation

Prefer the retained `zip-transcript-summary` product. It already applies the same
compression policy this skill needs, so reusing it avoids compressing the same
session twice.

```bash
agentos chatlas products status --product zip-transcript-summary --identity-hash <hash> --json
```

Branch on `product.state`:

- **`fresh`** — read the artifact and use it as the transcript source:

  ```bash
  agentos chatlas products path --product zip-transcript-summary --identity-hash <hash>
  ```

  Its user turns are already verbatim and its assistant turns are already
  compressed. Skip Step 4 entirely.

- **`production_required`** — produce it, then use it. Follow
  `tarav-chatlas-pkg/references/producer-zip-transcript-summary.md` and run its
  four-step loop: `produce` → `scaffold` → fill → `check` → `commit`. Do not
  hand-build the artifact and do not write your own verification script. Then
  read the committed artifact as above.

Fall back to the raw view and compress it yourself with Step 4 when any of these
holds:

```bash
agentos chatlas views get --identity-hash <hash> --view zip-transcript --json
```

This is the same input view the product is built from: turn-aligned, user turns
verbatim, assistant turns uncompressed.

- `--no-produce` was passed
- the session is still being worked in, so a product would go stale immediately.
  Check with `agentos chatlas query --identity-hash <hash> --idle-for 30m --json`;
  an empty result means the session is still active
- production failed, or the transcript is small enough that producing it costs
  more than compressing it inline

Producing is the expensive path — it is a full compression pass over the whole
session. That is the intended trade when the artifact will be reused; say so in
the run rather than doing it silently, and honor `--no-produce` when the caller
wants the cheap path.

The final artifact remains a plain turn-based handoff, not raw JSON.

## Step 3: Derive Continuation State

Before writing the transcript section, derive the session state that matters for continuing here.

Include only items supported by the session. Omit unknown items instead of inventing them.

When the source is a `zip-transcript-summary` artifact, `recommended-next-step`
and `open-threads` are the fields most exposed to compression loss — they usually
hinge on detail in the last few turns. Read the tail of the raw view directly
before writing them:

```bash
agentos chatlas views get --identity-hash <hash> --view zip-transcript --range=-10: --json
```

`--range` is supported only on the `zip-transcript` view, and the `=` form is
required for a negative spec or argparse reads it as a flag.

Preferred continuation-state fields:

- `current-goal`
- `accepted-decisions`
- `active-constraints`
- `important-artifacts`
- `open-threads`
- `recommended-next-step`

Interpretation rules:

- `current-goal`: the main objective the session was converging on or actively pursuing near the end.
- `accepted-decisions`: decisions the user accepted or that the session clearly committed to.
- `active-constraints`: requirements, prohibitions, environment constraints, or style constraints that still govern the work.
- `important-artifacts`: commands, paths, identifiers, files, branches, URLs, counts, or names that matter for continuation.
- `open-threads`: unresolved questions, blockers, pending edits, missing validation, or follow-up work.
- `recommended-next-step`: the single best next move for resuming in the current chat.

## Step 4: Compress Assistant Turns

Skip this step when Step 2 sourced a `zip-transcript-summary` artifact — its
assistant turns are already compressed under the same policy, and compressing
them again only loses detail.

This step applies on the fallback path only. Its rules are the same policy as
`tarav-chatlas-pkg/references/producer-zip-transcript-summary.md`; when the two
disagree, that reference wins.

Always compress the assistant turns. Do not switch behavior based on transcript length.

Hard rules:

- Preserve every user turn in full.
- Preserve every user turn verbatim.
- Preserve chronological order.
- Compress every assistant turn to the shortest direct form that keeps new information.
- Short high-signal command outputs may be kept verbatim.
- High-signal but long outputs must be compressed structurally, not copied wholesale.
- Do not keep progress chatter, repeated framing, or filler.
- Do not pretend the output is the original transcript.

Keep assistant content only when it carries session state that matters later, such as:

- decisions
- accepted plans
- constraints
- concrete results
- failures
- warnings
- unresolved issues
- commands, paths, flags, identifiers, or counts that matter for continuation

Usually drop assistant content that is only:

- speculative framing
- unaccepted suggestions
- process narration
- repeated summaries
- tone-only filler
- status chatter that did not change the outcome

Compression checklist:

1. Preserve every user turn fully and verbatim.
2. Preserve accepted decisions and concrete outcomes.
3. Preserve failures and unresolved issues.
4. Drop chatter and repeated framing.
5. Compress long outputs structurally instead of copying them wholesale.

Keep in assistant turns:

- answers
- decisions
- constraints
- concrete facts
- command names, flags, identifiers, and counts when they matter
- failures, warnings, and unresolved issues
- code-change outcomes or test results when they matter

Drop or compress aggressively:

- progress updates
- statements about what the agent is about to do
- statements that a run is in progress
- repeated summaries
- apology or filler language
- redundant caveats
- verbose prose that adds no new information

Preferred assistant rewrite shape:

- result
- evidence
- decision
- unresolved issue, only if one remains

If a long structured output matters, compress it into a short factual summary instead of pasting the full block.

## Step 5: Return The Handoff Artifact

The returned artifact must be self-describing. Start it with this notice or equivalent wording:

```text
[session continuation handoff]
User turns are preserved verbatim.
Assistant turns are compressed for brevity and may not match the original wording.
Continuation state is derived to help resume the discussion in this chat.
Do not treat this artifact as the original transcript.
```

Add a short provenance header before the continuation state when the information is available:

```text
source-session-id: <session-id>
source-session-uri: <resolved-uri>
source-identity-hash: <identity-hash>
resolved-via: agentos chatlas query --message-contains
sourced-via: agentos chatlas products path --product zip-transcript-summary
product-state: fresh | produced-this-run | fallback-raw-view
```

When both a session id and URI are available, include both. Treat these as first-class provenance data, not optional decoration.

`product-state` matters to the reader: `fallback-raw-view` means the assistant
turns were compressed inline for this handoff only, while the other two mean they
came from a retained artifact that other callers share.

Then emit the continuation state in a stable shape:

```text
[continuation-state]
current-goal: <text>

accepted-decisions:
- <decision>

active-constraints:
- <constraint>

important-artifacts:
- <artifact>

open-threads:
- <open thread>

recommended-next-step:
- <next step>
```

After that, emit the transcript in a stable turn-based format:

```text
[transcript]

[user]
<full user content>

[assistant]
<compressed assistant content>
```

## Output Requirements

- Return the continuation handoff artifact itself, not a prose summary about it.
- Keep the artifact plain and readable.
- If extraction fails, report the failure briefly instead of fabricating output.
- If resolution is ambiguous, stop before extraction.
- The artifact must make continuation easier than reading the raw transcript.

## Session Content Sensitivity

- Treat the returned artifact as sensitive prior-session content.
- Do not broaden or remix it with unrelated repository discovery or external context.
- Do not present the artifact as a casual recap when it is actually a derived continuation handoff.

## Notes

- This skill is for continuation and context recovery, not quote-accurate archival use.
- The caller must be aware that the transcript portion is compressed and not original.
- The user turns are still required to remain verbatim.
- Prefer Chatlas dataset resolution over `agentos chat debug ...`; the debug surface is for live connector diagnostics, not normal prior-session recovery.
