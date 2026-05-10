# Introduce `agentos stdlib` namespace - impl-req

## Impl-Req State

Implemented and verified — infrastructure commands now live under `agentos stdlib`, active references are updated, and old top-level command paths fail at parser level.

## User Intent

Move infrastructure primitives out of the top-level CLI namespace into a new `agentos stdlib` grouping. Clean up the primary command surface so only user-facing operations are top-level.

## Why This Exists

The `agentos` CLI has grown to 17+ top-level commands. Several are infrastructure primitives used by other commands or agents, not primary user workflows. Mixing them with primary surfaces (`index`, `skills`, `agent`) creates namespace pollution and makes the CLI harder to navigate.

The `stdlib` framing maps naturally to the `Soft.Programming.Language` model: the index is the language, `stdlib` provides the standard library of reusable primitives it's built on.

## Current Situation

Top-level commands include both primary surfaces and infrastructure:

```
Primary:        agent, skills, index, doctor, canvas, mission, chatlas, forum, codex
Project setup:  init, rev-parse, test
Infrastructure: mdblocks, prefix, git-refs, utils
Niche:          tara-tapes
```

Infrastructure commands work fine but clutter `agentos --help` and create a flat namespace where everything looks equally important.

### Consumers of infrastructure commands

- `agentos index doctor` — imports `mdblocks.core` Python API
- `AGENTS.md` (agentos-py) — documents `agentos mdblocks` preference
- Skills (agentos-md) — reference `agentos mdblocks lint/find/blocks`
- Agents — use `agentos prefix next` for file numbering
- Agents — use `agentos git-refs` for line-span references
- Tests (agentos-py) — invoke the current top-level command argv directly
- Project command logs and diagnostics — may include user-facing command names such as `agentos prefix next` and `agentos utils tmp-folder new`

## Requested Change

### 1. Create `agentos stdlib` top-level command

A new namespace that groups infrastructure primitives:

```
agentos stdlib mdblocks blocks ...
agentos stdlib mdblocks lint ...
agentos stdlib mdblocks find ...
agentos stdlib mdblocks links ...
agentos stdlib prefix next ...
agentos stdlib git-refs ...
agentos stdlib utils uuid ...
agentos stdlib utils tmp-folder ...
agentos stdlib utils cmd-logger ...
```

### 2. Register subcommands under stdlib

- Move `register_mdblocks_commands` → register under `stdlib` subparser
- Move `register_prefix_commands` → register under `stdlib` subparser
- Move `register_refs_commands` → register under `stdlib` subparser
- Move `register_utils_commands` → register under `stdlib` subparser

### 3. Remove old top-level registrations

Remove `mdblocks`, `prefix`, `git-refs`, `utils` from the top-level `build_parser()` subparsers.

### 4. Update internal consumers

- `agentos/index/doctor.py` — no change needed (uses Python API, not CLI)
- Active skills and docs referencing `agentos mdblocks ...`, `agentos prefix ...`, `agentos git-refs ...`, or `agentos utils ...` — update to `agentos stdlib ...`
- `AGENTS.md` (agentos-py) — update documented preference
- Tests that call `main([...])` with moved top-level commands — update expected argv to include `stdlib`
- Project command logging/diagnostic labels for moved commands — update labels where they describe the user-facing CLI path

## Constraints And Invariants

- **No backward-compatibility aliases.** Per `AGENTS.md` compatibility policy: "Do not add backward-compatibility aliases or compatibility layers unless explicitly requested."
- **Python API unchanged.** `from agentos.mdblocks.core import ...` stays as-is. Only the CLI routing changes.
- **Module locations unchanged.** `agentos/mdblocks/`, `agentos/prefix/`, `agentos/refs/`, `agentos/utils/` stay where they are. Only CLI registration moves.
- **All existing functionality preserved.** Same flags, same output, same behavior — just under `stdlib`.
- **`agentos stdlib --help` should list all grouped subcommands clearly.**
- **Historical surfaces are not rewritten by default.** Update active skills, current docs, tests, and operational instructions. Do not churn archived, deprecated, or historical discussion notes unless a current active surface depends on them.

## Out Of Scope

- Renaming Python modules or moving source files
- Adding new functionality to any of the moved commands
- Changing command output format or behavior
- Moving `tara-tapes` (niche, but not infrastructure)
- Moving `rev-parse`, `init`, `test` (project setup, different category)

## Acceptance Signals

1. `agentos stdlib --help` shows: `mdblocks`, `prefix`, `git-refs`, `utils`
2. `agentos stdlib mdblocks lint notes/index/ --json` works identically to current `agentos mdblocks lint notes/index/ --json`
3. `agentos stdlib prefix next --project --target notes/live` works
4. `agentos stdlib git-refs --help` works
5. `agentos stdlib utils uuid` works
6. Old paths (`agentos mdblocks`, `agentos prefix`, etc.) no longer exist — they fail at parser level and do not dispatch handlers
7. `agentos --help` no longer shows `mdblocks`, `prefix`, `git-refs`, `utils`
8. `agentos index doctor` still works (uses Python API)
9. All existing tests pass

## Relevant Files Or Surfaces

| Path | Role |
|---|---|
| `agentos-py/src/agentos/cli.py` | Top-level parser — remove old registrations, add stdlib |
| `agentos-py/src/agentos/mdblocks/commands.py` | `register_mdblocks_commands` — reuse as-is |
| `agentos-py/src/agentos/prefix/commands.py` | `register_prefix_commands` — reuse as-is; update command labels if needed |
| `agentos-py/src/agentos/refs/__init__.py` or similar | `register_refs_commands` — reuse as-is |
| `agentos-py/src/agentos/utils/__init__.py` or similar | `register_utils_commands` — reuse as-is; update command labels if needed |
| `agentos-py/src/agentos/index/doctor.py` | Consumer — uses Python API, no change |
| `agentos-py/tests/test_mdblocks_commands.py` | Update moved command argv and parser-failure expectations |
| `agentos-py/tests/test_prefix_commands.py` | Update moved command argv, command-log expectations, and parser-failure expectations |
| `agentos-py/tests/test_utils_commands.py` | Update moved command argv, diagnostics, and parser-failure expectations |
| `agentos-py/tests/test_tmp_folder_commands.py` | Update moved command argv and command-log expectations |
| `agentos-py/tests/*refs*` | Update moved `git-refs` command tests if present |
| `agentos-py/AGENTS.md` | Documentation — update command references |
| `agentos-md/skills/agentos-live-note-base/SKILL.md` | Skill — update `agentos prefix next` references |
| `agentos-md/skills/agentos-live-scripts-base/SKILL.md` | Skill — update `agentos prefix next` references |
| `agentos-md/skills/agentos-file-numbering-base/SKILL.md` | Skill — update `agentos prefix next` references |
| `agentos-md/skills/agentos-canvas-base/SKILL.md` | Skill — update `agentos prefix next` references |
| `agentos-md/skills/agentos-index-writer/SKILL.md` | Skill — update `agentos prefix next` references |
| `agentos-md/skills/agentos-index/references/maintenance.md` | Skill — update `mdblocks` and `prefix` CLI references |
| `agentos-md/skills/agentos-index/references/block-syntax.md` | Skill — update `mdblocks` CLI references |
| `agentos-md/skills/agentos-index-doctor/SKILL.md` | Skill — already uses `agentos index doctor` (ok) |

## Open Questions

None blocking implementation.

One explicit implementation policy decision: update active operational surfaces only. Leave archived/deprecated notes and historical design-session prose unchanged unless they are still loaded as active instructions.

## Related Impl-Reqs

- Follows from the Agentos Index MVP build (this session)
- The `agentos index` command was the first to build on `mdblocks` as infrastructure

## End Log

- 2026-05-10: impl-req created after design discussion. All 4 commands identified for migration. No backward-compat aliases per policy.
- 2026-05-10: Review pass tightened target paths, active documentation scope, parser-failure wording, test coverage expectations, and command-label/logging considerations.
- 2026-05-10: Implemented in `agentos-py` by adding `agentos stdlib`, moving `mdblocks`, `prefix`, `git-refs`, and `utils` under it, updating command log path derivation for nested commands, updating active command references in `agentos-py` and `agentos-md`, and adding stdlib parser coverage. Verified with targeted stdlib tests, full `agentos-py` pytest suite, installed CLI refresh, and acceptance command checks. Archived/deprecated/historical references were intentionally left unchanged.
