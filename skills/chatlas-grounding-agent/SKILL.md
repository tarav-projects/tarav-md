---
name: chatlas-grounding-agent
description: Chat.Grounding workflow skill. Mine Chatlas sessions into Chat.Grounding.Request JSONL, or run git-grounding from a target block through chat evidence discussion and approved grounding writes. USE WHEN a caller wants chat-to-block grounding, block-to-chat grounding, or git-guided grounding for a kernel block. Called like a terminal command — `--mode l1|l2|git-grounding` plus `--target`.
---

# Chatlas Grounding Agent

Operational `Package.Aux.Skill` under `agentos-chatlas-pkg`.

`Chat.Grounding` workflow skill for the `Chat.Surface`: mine chat sessions for `Chat.Grounding.Material`, append `Chat.Grounding.Request` records for later gated review, or run a git-guided block grounding review through user-approved index writes.

L1/L2 mining **neither creates nor destroys information** — it surfaces high-signal turns and converges toward exhausting the design signal in the chats. `git-grounding` continues past mining into `Chat.Grounding.Candidate.Review`: it proposes candidate grounding lines, iterates with the user, and writes only after explicit approval.

This is a `Batchy.Skill` — called like a terminal command. Load `agentos-batchy-skills` for the full convention.

- `-h` / `--help` prints the help into the chat instead of running (`Batchy.Skill.Help`).
- every run prints a banner of the resolved arguments as its first step (`Batchy.Skill.Banner`).
- supplied flags resolve to the `Skill.Arg` names below.

## Skill.Arg.Section

### Skill.Arg:Mode
- the grounding workflow to run
- required: false
- default: L1
- help: "choose L1, L2, or git-grounding"
- examples: --l1, --l2, --git-grounding
- action: `--git-grounding` loads `references/git-grounding.md` and runs the review/approval loop inline

### Skill.Arg:Target
- what to mine: the chat sessions, scope, or kernel block(s) to ground
- required: false
- help: "the sessions or blocks to mine"
- examples: --target "agentos-pkg index blocks"

For the concept model, read the owning index blocks:

- `agentos-chatlas-pkg` index — `Chat.Grounding.Miner`, `Chat.Grounding.Miner.Locality`, `Chat.Grounding.Material`, `Chat.Grounding.Material.Catalog`, `Chat.Grounding.Request`
- `agentos-pkg` index — `Chat.Surface`, `Chat.Ref`, `Chat.Grounding`, `Chat.Grounding.Target.Block`, `Chat.Grounding.Ref.Resolution`, `Chat.Grounding.Candidate.Review`, `Chat.Grounding.Head.Audit`, `Active.Grounding`, `Grounding.Hugentic.Authority`

## Workflow Modes

- **L1 — chat→reqs.** Read one chat session, detect `Chat.Grounding.Material` turns, append session records. Reads only the `Chat.Surface`, never a project. Output lives in the `Chatlas.Depot`. See `references/l1-miner.md`.
- **L2 — block→reqs.** Target one kernel block, search the L1 session layer, confirm against the actual chat turn, append block records. Output lives in the target project. See `references/l2-miner.md`.
- **git-grounding — block→git hints→chat evidence→approved grounding.** Target one `Chat.Grounding.Target.Block`, use git history to find likely chat windows, review one candidate at a time with the user, then write approved `### grounding` entries. See `references/git-grounding.md`.

L1/L2 produce `Chat.Grounding.Request`s; neither writes the index. `git-grounding` may write index/appendix grounding only after explicit user approval of the grounding role, resolution shape, and candidate line.

## Routing

| Need | Load |
|---|---|
| record shape, file kinds, paths, dedup | `references/gr-req-format.md` |
| what counts as `Chat.Grounding.Material` | `references/grounding-material-catalog.md` |
| run L1 (mine a session) | `references/l1-miner.md` |
| run L2 (ground a block) | `references/l2-miner.md` |
| run git-guided block grounding and approval | `references/git-grounding.md` |
| query / export chat evidence | `references/chatlas-surface.md` |

## Pick The Mode

- caller gives a **session / `Chat.Ref` / transcript** and wants its design signal mined → **L1**.
- caller gives a **kernel block** and wants request candidates from the existing L1 layer → **L2**.
- caller gives a **kernel block** and wants to complete grounding in one session → **git-grounding**.
- no target → ask which: a session to mine, or a block to ground.

## Execution Mode

- L1/L2 may be delegated to a separate agent because they are mining-only and produce request artifacts.
- git-grounding runs inline in the caller conversation by default because the user must discuss and approve candidate grounding lines before any index write.

## Boundaries

This skill does not:

- write index or appendix files in L1/L2 modes
- decide final grounding authority from request records alone — `*HEAD*`, history, and `DRIFT:` classification happens through `Chat.Grounding.Candidate.Review`
- use or require vector search
- treat absence of search hits as absence of grounding
