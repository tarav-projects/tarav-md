# 622 — Tournament.Label And Run Parameters

## Impl.Abstract

**Scope.** Two narrow additions to the `agentos-py` tournament engine, both landed today on the
index and both absent from the code:

- **`Tournament.Label`** — an optional opaque grouping string a definition may attach to a
  player and to a match. The engine records it on the verdict and never interprets it. It never
  reaches the judge.
- **Run parameters** — consumer key/value pairs supplied per run, reaching every hook through
  its `HookContext`. The engine carries them and never branches on them.

**Out of scope.** No change to what a judge is shown — the rendered prompt bytes must stay
identical. No change to identity, controls, tickets, the answer contract, the template and
component registry, or the read side (`report.py`, `poi.py`). Labels do not participate in match
identity. Run parameters are not written to the verdict envelope (see `Impl.Index`).

**Status.** Executed. All six slices are implemented and the full `agentos-py` suite passes at
897 tests. Changes are uncommitted for review.

**Source context.** `agentos-md/skills/agentos-pkg/design/111-design.md`: the new
`Tournament.Label` block, the `Tournament.Player` and `Tournament.Match` label lines, and the
three run-parameter lines on `Tournament.Hook`. This `Impl.Req` realizes those lines and nothing
beyond them.

## Impl.Index

### Labels Are A Third Recorded Fact, Shaped Like Controls

The envelope already carries a per-player engine-written mapping: `controls`, player → declared
band. A player label is the same shape — player → opaque string — and is recorded the same way.
The match label is a single optional string beside it.

Field names are `player_labels` and `match_label` rather than a bare `labels`/`label` pair.
`controls` gets away with a bare name because there is only one kind of control; here two fields
would sit adjacent with names distinguished only by plurality, which reads as a typo.

Both join `ENVELOPE_FIELDS`, so a consumer slot cannot shadow them.

### Labels Are Hooks, Because Everything Consumer-Owned Is

`player_label` mirrors `present_player`: called per player, receives that player on the context,
returns a string or `None`. `match_label` mirrors `verdict_slot`: called once per match with the
players and their presentations, returns a string or `None`. Both are defaulted hooks — a
definition that supplies neither behaves exactly as today.

Returning `None` means unlabeled and is the default, per the index line that a label is optional
and that absence reads as one undifferentiated population. An empty or whitespace-only string is
a `HookReturnError`: it is not a label and silently recording it as one would put an invisible
group in the fold.

**Labels do not vary-check.** The index explicitly frees a label to differ across the matches a
player appears in, so the engine must not compare a player's label against a previous verdict's.
That freedom is what makes the read group over label occurrences rather than over players.

### The Load-Bearing Negative: A Label Never Reaches The Judge

A label is reader-side, like a control's declared band. If `player_label` returned
`"registered"` and that string appeared in the prompt, it would be the strongest signal in the
match and every verdict carrying it would be void.

Mechanically this is already true — `build_template` receives only the question, criteria, and
presentations — so the risk is not the current code but a later edit. The defense is a test that
pins it: compose a match whose labels are lurid, unmistakable strings, and assert the rendered
verbatim is byte-identical to the same match with no label hooks at all.

### Run Parameters Ride On The Context And Stop There

`HookContext` gains `params`, a read-only string→string mapping, populated identically for every
hook call of a run. The CLI accepts repeatable `--param key=value` on `run` and `preview`.

`HookContext` is a frozen dataclass whose purity is verified after each hook call, so `params`
must not be a bare `dict` a hook could mutate into the next call's view. Store it as a
`MappingProxyType` over a copied dict.

**The engine never reads a key.** No engine code path may branch on `params` content; its own
knobs stay named CLI parameters with their own validation. A malformed `--param` (no `=`, empty
key) is a `CliError` at parse time, which is the boundary the index line points at — the engine's
surface stays enumerable, and a typo inside a *value* remains the definition's problem.

**Parameters are deliberately not recorded.** A verdict already carries its players, presented
order, verbatim hash, and template address, so a parameter that only selects which matches are
produced needs no record; the produced match is self-describing. A parameter that changes what a
given match identity *means* is the existing consumer obligation to make it a different match.
This was argued and settled in the source discussion; do not add an envelope field for it.

## Impl.Agendix

**Index citations** — the lines this implementation must honor:

- `index://agentos-pkg/Tournament.Label` — the whole block
- `index://agentos-pkg/Tournament.Player` — `^c20260809-178u`
- `index://agentos-pkg/Tournament.Match` — `^c20260809-179u`
- `index://agentos-pkg/Tournament.Hook` — `^c20260809-180u`, `^c20260809-181u`, `^c20260809-182u`
- `index://agentos-pkg/Tournament.Verdict` — envelope ownership and slot shadowing
- `index://agentos-pkg/Judge.Blinding` — `^c20260809-41u`, the test that decides reader-side content

**Chat grounding** — the design turns are the support sets behind
`^c20260809-171u` … `-182u`, minted this session. The ordering turn for this implementation is
the `--impl --dev` invocation that produced this artifact.

## Execution.Plan

### Slice 1 — The label hooks exist and validate (RED first) — **Done**

Add `PLAYER_LABEL` and `MATCH_LABEL` to `hooks.py` as defaulted hooks with accessors beside
`present_player` and `verdict_slot`. Write the validation tests first: absent hook yields `None`;
a returned string passes through; a non-string, empty, or whitespace-only return raises
`HookReturnError` naming the hook.

- **Result:** a definition can declare labels; nothing consumes them yet.
- **Check:** new hook tests pass; the existing suite is untouched and green.

### Slice 2 — Labels reach the verdict — **Done**

Thread through `MatchResult`, `run_match`, `preview_match`, `store.append_verdict`, and
`ENVELOPE_FIELDS`. `player_labels` omits unlabeled players entirely rather than storing nulls.

- **Result:** a verdict records what its players and its match were labeled.
- **Check:** an end-to-end `preview` + hand `submit` puts both fields on the verdict; a
  definition with no label hooks writes an empty mapping and no match label; a consumer slot
  naming either field raises `EnvelopeShadowedError`.

### Slice 3 — Labels never reach the judge (RED first) — **Done**

Add the blinding test described in `Impl.Index`: identical matches, one with deliberately
conspicuous labels and one with none, must render byte-identical verbatims.

- **Result:** the reader/judge boundary is pinned by a test rather than by the current call graph.
- **Check:** RED before slice 1's wiring is referenced by the renderer, GREEN after; the assertion
  is on bytes, not on absence of a substring.

### Slice 4 — `params` on the hook context — **Done**

Add `params` to `HookContext` as a `MappingProxyType`, populated in `_context` and passed down
from the definition accessors. Every hook sees the same mapping.

- **Result:** a definition may branch on run parameters.
- **Check:** a definition whose `match_players` reads `params` observes what the caller supplied;
  a hook attempting to mutate `params` raises; purity verification still passes after each call.

### Slice 5 — `--param` on the CLI — **Done**

Add repeatable `--param key=value` to the `run` and `preview` subparsers, parsed into a dict and
threaded through `run_pool` → `run_match` / `preview_match` → definition accessors.

- **Result:** parameters are supplied from the shell.
- **Check:** a malformed `--param` exits with a `CliError` naming the offending value; repeated
  keys resolve last-wins; a run with no `--param` behaves exactly as before.

### Slice 6 — Documentation — **Done**

Update the Tournament System section of `agentos-py/AGENTS.md`: labels as recorded, uninterpreted,
judge-invisible grouping; run parameters as consumer-owned and engine-opaque; the two new envelope
fields. Update `$kw` headers on touched modules.

- **Result:** the doc matches the code in the same unit of work, per `AGENTS.md`'s own rule.
- **Check:** read back; every claim traceable to a slice above.

### Ordering and dependencies

1 → 2 → 3 → 4 → 5 → 6. Slice 3 depends on 1 and 2 existing to be meaningful. Slices 4–5 are
independent of 1–3 and could run first; the given order keeps one concern finished before the
next starts.

### Deviation triggers

- **The blinding test cannot be made to pass byte-identically.** Stop. It means something in the
  render path already reads consumer data it should not, which is a finding larger than this
  change.
- **`params` cannot be made immutable without breaking purity verification.** Record why and stop
  before the CLI slice; a mutable shared mapping across hook calls is not acceptable.
- **A label turns out to be wanted inside match identity.** That contradicts
  `^c20260809-174u`. Do not implement it; record it and raise it.

### Acceptance signals

- The full `agentos-py` suite passes with no existing assertion edited to accommodate the change.
- A verdict produced through `preview` + `submit` carries `player_labels` and `match_label`.
- The rendered verbatim for a labeled match is byte-identical to its unlabeled twin.
- `agentos tournament run --param shape=mixed` reaches a definition hook that reads it.

## Impl.Log

**Execution gate.** Authorized by `^c20260809-183u`, the `--impl --dev --exec` invocation turn.

**D1 — the blinding test passed on first write, so it was proved falsifiable.** Slice 3's guard
went GREEN immediately, because the render path never received labels. A test that cannot fail is
not evidence, so the leak was injected deliberately — labels appended to
`presented_presentations` — the test observed to fail, and the injection reverted. Recorded because
the plan called for RED-then-GREEN and the honest sequence here was GREEN-then-proved-RED.

**D2 — the CLI acceptance test needed the real create handler.** The first `_created` helper wrote
a definition snapshot by hand; `open_definition` rejected it, correctly, as having no authorized
version on record. The helper now creates through the `tournament create` handler, which is also a
truer boundary test.

**D3 — the checkpoint's known-failing test now passes.** The plan warned that
`test_index_linter_reports_anchor_collision_across_depots` was red from another session's anchor
migration. It is green at 897, because the checkpoint commit captured that session's later state.
No action taken; noted so the discrepancy against the plan is not read as drift.

**Concurrency note.** `agentos-py` has uncommitted in-flight work from another session in
`src/agentos/index/` and `src/agentos/anchory/`, and its suite currently carries one failing test
(`test_index_linter_reports_anchor_collision_across_depots`) belonging to that migration. This
implementation touches only `src/agentos/tournament/`, which is disjoint. Read the acceptance
signal "full suite passes" against that known-failing test rather than treating it as a
regression from this work.
