> $kw: ^parking-note-direct-loading-path --context-loading-path
> --step SKILL.md
> --loading-dep SKILL.skw.md^hugentics-batchy-runtime-contract
> --loading-dep SKILL.skw.md^hugentics-skill-arg-contract

# Parking.Note.Operation.Module

> $kw: --dev-from references/index-context-assembly.skw.md

Short-lived interruption workflow for capturing a sidequest thought into a project `Parking.Note`.

The user presents an idea while another task is underway. The agent preserves the main-thread return context, discusses the idea lightly, drafts a `Kernel.Block`-style entry, gets explicit user approval of the exact text, grounds it in qualifying Chatlas2 user messages, writes the note, and reports how to resume the interrupted work.

The unified driver supplies the `Batchy.Skill` calling convention. Its `--park` route selects this module and binds any trailing idea to `Skill.Arg::Idea`.

- `-h` / `--help` prints the help into the chat instead of running (`Batchy.Skill.Help`).
- `--idea` binds `Skill.Arg::Idea`; a bare idea in the selected route binds the same input.

This module models that external idea as a `Skill.Arg`; it does not model the routing operation as an argument.

## Skill.Arg.Section

### Skill.Arg::Idea
- the thought to park: an idea, todo, issue, or observation
- required: false
- help: "the thought to capture; omitted, the skill asks for it"
- examples: --idea "revisit the retry backoff in the uploader"

## Activation

Use when the user wants to park an idea, todo, issue, or observation for later without switching the session's main task. Typical phrases: "park this", "capture this side idea", "parking note", "I want to capture an idea", or an explicit `$parking-note` invocation.

This skill is an `Alignment.Loop.Interruptions` workflow: it intentionally branches away from the main flow and must return the session to that flow after the write.

## Boundary

- this skill captures sidequest ideas; it does not execute them
- this skill enriches lightly; a growing design discussion should move to the relevant design workflow
- this module writes only `Parking.Note` files; index edits and agendix captures stay with their Index modules
- this module consumes the internal `Real.Time.Grounding.Knowledge.Module` in `references/link.md`, but the note file remains the landing surface
- this skill is user-gated: file writes require explicit approval of the exact text

## Parking.Note Files

Each project may have these reserved files under `notes/live/`:

| File | Role |
|---|---|
| `012.PARKING.md` | Catch-all — ideas, observations, design seeds, anything |
| `010.TODOS.md` | Something to do |
| `011.ISSUES.md` | Something wrong |

`012.PARKING.md` is the default. Nothing is out of place in PARKING.

DEPRECATED: `012.NOTEBOOK.md` was the former parking-note filename. Prefer `012.PARKING.md` for new notes.

## Workflow

1. The user presents whatever they have — a sentence, a paragraph, a vague notion.
2. The agent records the return context in chat: the interrupted task, the last concrete next step, and any active files or artifacts.
3. The agent discusses the idea lightly: ask at most one focused question at a time, enough to enrich the idea, not enough to start a full design session.
4. The agent drafts a block, picks a target file, and shows the exact proposed text with inert placeholder anchors such as `^<anchor-on-landing>`.
5. The user refines, redirects the target, rejects the note, or explicitly approves the exact block text for writing.
6. If the user rejects the note, the agent writes nothing, mints no anchor, and returns a rejection report with the compact resume point.
7. After approval, the agent mints one Chatlas2 line dossier through the internal Real.Time grounding primitive whose support contains the qualifying substantive user messages plus the approval message; one exact dossier may trail every line approved as a unit.
8. The agent replaces placeholder anchors with the minted anchor and writes the block to the target file.
9. The agent returns a close-out report: what was parked, where it was written, the anchor, and the compact resume point for the interrupted task.

The workflow is short-lived. It ends after the write report or rejection report.

## Block Format

Entries follow `Kernel.Writing` style with relaxed constraints:

- Heading uses `Dotted.Notation` based on the note content (e.g. `## Idea.About.Fish.Based.APIs`)
- Each line describes an independent facet — direct, orthogonal
- Lines carry `Line.Type` codes when the entry is concept-shaped enough to support them
- Each landed kernel line carries trailing `Anchory.Anchor` provenance; one exact support set may support the whole block when its final text was approved as a unit
- No space budget — write as much as the idea needs
- Free to include tags, links, context, or any useful material after the grounded kernel lines
- No required metadata fields beyond the anchors needed for chat provenance

Example:

```md
## Fish.Based.APIs

- [DF] `Fish.Based.APIs` is a sidequest idea for modeling service clients around domain species instead of raw endpoint groups ^d20260816-0u
- [PR] species-aware routing could make the gateway easier to reason about than scattered marine-data endpoints ^d20260816-0u
- [CT] simplifying the client SDK is the main motivation ^d20260816-0u
- [FR] the idea is parked for later and should not interrupt the current marine-data task ^d20260816-0u
```

## Anchory Requirement

Parking notes preserve the compact idea in the file and the full idea in the chat.

- Use `references/link.md`: obtain the current provider-native session selector, locate the explicit user approval as a `Chat.Message.Ref`, register the exact Chatlas2 line dossier, and verify the returned neighborhood.
- When the agent drafted the block, the user's explicit approval message joins the substantive support members; it is not modeled as a reviewed-Index gate.
- Do not write the block until the approval anchor is minted and verified. If anchoring is unavailable, stop before the file write and report the blocker.
- Exact dossier registration is idempotent. Wrong support or line content requires a corrected dossier rather than repurposing an unrelated anchor.

## Draft Presentation

When showing the draft to the user, include:

- The target file as a full path from `~` (e.g. `~/projects/agentos-project/agentos-py/notes/live/012.PARKING.md`) — removes ambiguity in multi-project workspaces
- The proposed block (heading + body) with placeholder anchors
- The anchor plan: usually "on approval, ground the block in its substantive and approval messages and stamp each line with that anchor"
- One follow-up question about something missing or unclear

The user may approve, edit the block, reject the note, redirect to a different target file, or keep discussing. The agent writes only after explicit approval of the exact text.

## Option Banner

While the parking note is unresolved, every assistant turn ends with a compact named-options banner.

The banner keeps the interruption easy to exit. It should stay at the bottom of the assistant message and use stable option names:

```text
Options: approve | discuss | reject
```

- `approve` means the user approves the exact block text for anchoring and writing
- `discuss` means the user wants one more light enrichment turn, wording change, or destination change
- `reject` means the user wants no write and no anchor

If no exact draft has been shown yet, omit `approve` from the banner. Terminal write and rejection reports do not need the banner because the interruption is already closed.

## Return Report

After writing, report:

- the parked concept name
- the target file path
- the minted anchor
- the short reason the idea was worth parking
- the interrupted task and the next concrete step to resume

After rejection, report:

- that nothing was written
- that no anchor was minted
- the rejected concept name or short idea label, if useful
- the interrupted task and the next concrete step to resume

## File Creation

If the target file does not exist, create it with a minimal header before writing:

- `010.TODOS.md` → `# TODOs`
- `011.ISSUES.md` → `# Live Issues`
- `012.PARKING.md` → `# Parking`

> $kw: --from Alignment.Loop.Interruptions
> $kw: --from Batchy.Skill
> $kw: --from Batchy.Skill.Help
> $kw: --from Dotted.Notation
> $kw: --from Kernel.Block
> $kw: --from Kernel.Writing
> $kw: --from Line.Type
> $kw: --from Parking.Note
> $kw: --from Skill.Arg
