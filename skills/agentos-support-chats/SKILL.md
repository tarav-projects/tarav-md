---
name: agentos-support-chats
description: Maintain an Index-owned `009-SUPPORT-CHATS.md` registry by extracting Chatlas support sessions from anchors found in Project or Package Index sources. USE WHEN discovering, auditing, or synchronizing Project.Support.Chats, checking mandatory chat closure from Index anchors, or producing support-chat candidates for a project/package Index. Called like a terminal command with `--extract` or `--sync` and `--target PATH`.
---

# Agentos Support Chats

Operational `Package.Aux.Skill` under `agentos-pkg`.

This is a `Batchy.Skill`. Load `agentos-batchy-skills` for the shared calling convention.

## Banner

On invocation, print:

```text
$agentos-support-chats
- mode: extract|sync
- target: <resolved Index root>
- registry: <target>/009-SUPPORT-CHATS.md
```

`-h` / `--help` prints the banner, modes, arguments, and examples without running.

## Modes

- `--extract`: read-only; return the resolved support-session inventory and every finding.
- `--sync`: extract, agent-review the result, then create or update `009-SUPPORT-CHATS.md`.
- If neither is supplied, use `--extract`.
- Reject both modes together.

## Arguments

### Skill.Arg::Target

- `--target <path>` resolves the Index depot root containing `000-INDEX.md`.
- required: true unless the current directory resolves uniquely to one Index depot.

### Skill.Arg::Anchor.Regex

- `--regex <python-regex>` overrides anchor extraction.
- default: `\^(?P<anchor>c\d{8}-\d+[a-z]?)`

### Skill.Arg::Source.Glob

- `--glob <pattern>` controls recursive directory expansion.
- default: `*.md`

## Workflow

1. Resolve the target and require `<target>/000-INDEX.md`.
2. Use only the existing target sources: `000-INDEX.md`, `design/`, `appendix/`, `agendix/`, `issues/`, and `poi/`. Never scan `009-SUPPORT-CHATS.md`, compiled skill references, or an external Index.
3. Run one extraction call with repeatable sources:

   ```bash
   agentos chatlas anchory sessions \
     --source <target>/000-INDEX.md \
     --source <each-existing-index-directory> \
     --regex '<regex>' \
     --glob '<glob>' \
     --json
   ```

4. Review `findings`. An unresolved, invalid, or tag-mismatched anchor prevents a clean closure claim. Do not guess a session or silently omit the finding.
5. Treat every returned session as mandatory. Session membership is keyed by `identity_hash`; provider session ids, URIs, depot paths, and Chat.Index state are derived metadata.
6. In `--extract`, report counts, sessions, and findings without writing.
7. In `--sync`, preserve hand-maintained accepted candidates outside the managed mandatory section, then update the registry from the reviewed extraction.

## Registry Contract

Keep `009-SUPPORT-CHATS.md` compact:

```markdown
# Project Support Chats

> Stable materialization of `Project.Support.Chats` for this Index.

## Mandatory Index Support

<!-- agentos-support-chats:mandatory:begin -->
- `<identity_hash>` — `<provider>` / `<session_id>` — `<uri>` — anchors: `<count>` — Chat.Index: `<state>`
<!-- agentos-support-chats:mandatory:end -->

## Accepted Candidates

- none

## Extraction Findings

- none
```

- Rewrite only the managed mandatory region automatically.
- Preserve accepted candidates unless the user explicitly removes them.
- Findings must name their anchor and source location.
- Report `closure: complete` only when extraction returned `status=ok`.

## Boundaries

- This workflow links an Index to chats after the fact. It never changes the chat-only construction boundary of Chat.Index.
- It does not capture, regenerate, or delete Chat.Index surfaces.
- It does not auto-accept heuristic candidates. Git and Chatlas project queries belong to later candidate-discovery slices and require agent review.
