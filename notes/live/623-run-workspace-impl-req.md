# 623 — Run.Workspace And Its CLI

## Impl.Abstract

**Scope.** Implement `Run.Workspace` in `agentos-py`: a rooted directory of one-run agentic
workspaces at `~/.agentos/workspaces/<date>-<slug>/`, each defining itself in a required
`AGENTS.md`, each its own git repository, and none of them a `Stable.Surface`. Plus its CLI:
`agentos workspace guide|init|list|show|sweep`.

`init` is gated on a `Poi.Unlock.Token` receipt for the workspaces guide, so a workspace is never
created by an agent that has not read what a workspace is.

**Out of scope.** No `Improvement.Loop` — this is the container, not the kind. No structure below
`AGENTS.md`: the general form mandates nothing. No promotion tooling; taking content out of a
workspace onto a stable surface stays a manual, gated act. No cross-repo Wayfinder addressing of
the guide (see the decision below). No integration with the tournament engine.

**Status.** Designed, not executed.

**Source context.** `agentos-md/skills/agentos-pkg/design/100-design.md`: the new
`Volatile.Surface` and `Run.Workspace` blocks. `design/107-design.md`: `Skw.Surface.Token`,
`Poi.Unlock.Token`, `Poi.Unlock.Registry`. This `Impl.Req` realizes the `Run.Workspace` block and
nothing beyond it.

## Impl.Index

### The Guide Ships With The Code, Not With The Index

The index says creating a workspace is gated on a receipt for "the workspace documentation
surface". That surface does not exist, and where it lives is the one decision that sizes this
whole change.

The existing unlock machinery (`skillware/_build_core.py`, `<package>/.skw/unlock-tokens.json`)
is bound to Skillware packages, resolves surfaces as `.skw.md` sources with addressed
annotations, and is consumed only by `Poi.Bless` against POI kinds. Routing `workspace init`
through it would require authoring the guide in `agentos-md`, addressing it across repositories
through `Agentos.Wayfinder`, and generalizing receipt validation past POI kinds — substantial
machinery for one gate with one consumer.

**Decision: the guide is a package resource inside `agentos-py`,** `workspaces/GUIDE.md`, carrying
its token in a header line. `Skw.Surface.Token` explicitly permits a file surface to carry its
token in its header, and `^c20260730-51u` makes the token-bearing surface the authority rather
than any registry — so the gate's semantics are the index's, only its plumbing is local. Promoting
the guide to a Skillware-managed surface later changes where the token is read from, not what the
receipt means.

The consequence to accept: this is a second, smaller unlock path beside Skillware's. It is not a
generalization of that one and must not pretend to be. If a third consumer appears, that is the
signal to unify them, and the unification is a separate piece of work.

### The Gate Is A Speed Bump, Deliberately

`^c20260730-118u` is explicit that token satisfaction proves nothing about comprehension. The gate
exists so `init` cannot happen blind, not so it can happen only correctly. So:

- `agentos workspace guide` prints the guide and nothing else. The token is the **last** line, so
  an agent that read the output has the receipt and an agent that did not, does not.
- `init` without `--unlock`, or with a stale one, exits with an error naming the guide command and
  **never printing the token**, per `^c20260730-55u`.
- Rotation is what keeps this alive: the token changes when the guide changes materially, so every
  stale receipt forces a re-read. That also makes the token the migration lever for future changes
  to the workspace contract.

### The Manifest Lives In The One Required Surface

`AGENTS.md` is the only mandated file. It carries prose an agent landing cold needs — kind,
purpose, provenance, how to run it — and a machine-readable `### manifest` section of
`- key: value` lines, mirroring the `### meta` convention already used in index blocks. One
surface, so prose and machine state cannot drift; a sidecar JSON would be a second authority.

Machine-read keys: `kind`, `created`, `status`, `extracted`. `status` is one of `open`,
`harvested`, `abandoned`. `extracted` is free text, defaulting to `none`.

`status` and `extracted` are what make disposal decidable — nothing is deleted while nobody can
tell whether anything left. They are the fields `sweep` reads.

### Deletion Is Explicit, Because It Is Deletion

`sweep` lists candidates and deletes nothing. `sweep --apply` deletes. A workspace is a
`Volatile.Surface` and deleting one is routine by design, but "routine" is about the *decision*,
not about doing it without being asked.

Candidacy is age plus status: `harvested` or `abandoned` past a horizon, or `open` and untouched
past a longer one. The horizons are flags with defaults, not policy buried in code.

### Git Inside, Never Around

`init` runs `git init` in the new directory and makes one initial commit. No remote, no submodule,
no nesting inside a tracked repository. `init` refuses when the resolved root is itself inside a
git worktree — that is the failure the index line names, and it is cheap to detect.

## Impl.Agendix

**Index citations** — the lines this implementation must honor:

- `index://agentos-pkg/Run.Workspace` — the whole block, `^c20260809-86u` … `-93u`
- `index://agentos-pkg/Volatile.Surface` — `^c20260809-79u` … `-85u`, especially the one-way arrow
- `index://agentos-pkg/Skw.Surface.Token` — `^c20260730-100u`, `^c20260730-37u`, `^c20260730-38u`
- `index://agentos-pkg/Poi.Unlock.Token` — `^c20260730-99u`, `^c20260730-52u`, `^c20260730-118u`
- `index://agentos-pkg/Poi.Bless` — `^c20260730-55u`, refusal never discloses the token

**Chat grounding** — the design turns behind `^c20260809-79u` … `-93u`, minted this session.
Execution is authorized by `^c20260809-183u`, the `--impl --dev --exec` invocation.

## Execution.Plan

### Slice 1 — The guide and its token (RED first)

Add `src/agentos/workspaces/GUIDE.md` — what a workspace is, the one-way arrow, the required
`AGENTS.md` and its manifest keys, git inside never around, and how to dispose of one. Header line
carries `surface-token: aws-unlock:<hex>`. Add `guide_text()` and `guide_token()` readers.

- **Result:** a tokened surface exists and its token is parsable from it.
- **Check:** `guide_token()` returns the header's token; a guide whose header is missing or
  malformed raises a named error rather than returning an empty token that would gate nothing.

### Slice 2 — Workspace root and the manifest reader

Add `root.py`: resolve `~/.agentos/workspaces` with `AGENTOS_WORKSPACES_ROOT` then an explicit
`--root`, mirroring `Tournament.Depot`. Add `manifest.py`: parse `### manifest` `- key: value`
lines out of an `AGENTS.md`, returning a typed record with defaults for absent keys.

- **Result:** workspaces are locatable and their state is readable.
- **Check:** a manifest with every key round-trips; an `AGENTS.md` with no manifest section reads
  as `status: open, extracted: none` rather than failing, because a hand-written workspace is
  still a workspace; an unknown `status` value is an error naming the file.

### Slice 3 — `guide` and the gated `init`

Add `commands.py` with `workspace guide` (prints the guide, token last) and `workspace init
--slug <name> --kind <kind> --unlock <token> [--purpose ...] [--seed ...]`. `init` creates
`<date>-<slug>/`, writes `AGENTS.md` from a template, runs `git init` plus one commit.

- **Result:** a workspace can be created, and only after reading the guide.
- **Check:** RED first — `init` without `--unlock` errors, and the error text does **not** contain
  the token; a stale token errors the same way; the correct token succeeds; the created directory
  has `AGENTS.md` and `.git`; `init` inside a git worktree refuses; a duplicate slug on the same
  date errors rather than overwriting.

### Slice 4 — `list` and `show`

`workspace list [--json]` reads every manifest and prints slug, kind, status, extracted, and age.
`workspace show --slug <name> [--json]` prints one manifest plus its top-level file listing.

- **Result:** "what have I got lying around" is one command.
- **Check:** `list` on an empty root prints an empty result rather than failing; a workspace with
  an unreadable `AGENTS.md` appears in the listing marked unreadable rather than vanishing —
  silence is the one thing a disposal read must not do.

### Slice 5 — `sweep`

`workspace sweep [--harvested-days N] [--open-days N] [--json]` lists deletion candidates with the
reason each qualified. `sweep --apply` deletes them.

- **Result:** forgotten workspaces are findable and removable.
- **Check:** RED first — `sweep` without `--apply` deletes nothing, verified by the directories
  still existing after the call; `--apply` removes exactly the listed set; a workspace whose
  status is `open` and recently modified is never a candidate.

### Slice 6 — CLI registration and documentation

Register `register_workspace_commands` in `agentos-cli/src/agentos_cli/cli.py`. Reinstall the
executable per `AGENTS.md`. Add a Workspaces section to `agentos-py/AGENTS.md`. Add `$kw` headers
to the new modules.

- **Result:** the command exists on the installed CLI and the doc matches the code.
- **Check:** `agentos workspace guide` runs from a shell; read the doc back.

### Ordering and dependencies

1 → 2 → 3 → 4 → 5 → 6. Slice 3 needs both 1 and 2. Slices 4 and 5 both read manifests and could
swap order; 5 last because it is the destructive one.

### Deviation triggers

- **The gate turns out to want Skillware's registry after all** — for instance because a second
  act needs the same surface. Stop and raise it; do not build a half-generalization.
- **`AGENTS.md` parsing wants a real parser.** If `- key: value` scraping starts needing
  structure, that is a signal the manifest belongs in a different format, and the index line about
  one required surface needs revisiting rather than the parser growing.
- **`git init` is unavailable or refuses.** `init` must fail loudly and leave no partial
  directory; a workspace without its repository is not the object the index describes.

### Acceptance signals

- The full `agentos-py` suite passes.
- `agentos workspace guide` prints the guide with the token last.
- `agentos workspace init` refuses without a receipt and the refusal does not contain the token.
- A created workspace has `AGENTS.md` with a readable manifest and its own `.git`.
- `agentos workspace sweep` lists without deleting; `--apply` deletes exactly what it listed.

## Impl.Log

**Execution gate.** Authorized by `^c20260809-183u`.

**D1 — the guide's home is a deliberate narrowing.** The index says the gate is a
`Poi.Unlock.Token` for the workspace documentation surface; it does not say that surface is
Skillware-managed. Shipping it as a package resource satisfies the line and avoids cross-repo
addressing that has exactly one consumer today. Recorded because the alternative is the more
"correct-looking" one and a later reader deserves to know it was considered and declined.

**Concurrency note.** `agentos-py` carries in-flight work from another session in
`src/agentos/index/` and `src/agentos/anchory/`. This implementation adds `src/agentos/workspaces/`
and touches `agentos-cli`'s composition root; both are disjoint from that migration.
