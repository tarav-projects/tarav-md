# Tournament Match.Frame — Impl.Req

## Impl.Abstract

- **Scope**: give a `Tournament.Definition` a typed, composable, content-addressed
  description of its match prompt — a `Match.Frame` — replacing the engine's fixed
  three-section template with an open composition over a closed set of node types
  and a closed set of engine-owned operations.
- **Status**: designed, ready for execution.
- **Source**: design conversation in this session (Improvement.Loop workspace,
  typing tournament). The immediate consumer is the index `Line.Type` tournament,
  which needs the seven type definitions rendered **once per match** as shared
  reference material that player cards cite into — something today's template
  cannot express at all.
- **Out of scope**: rewriting the loop workspace's tournament definitions to use
  the frame (a follow-on); adaptive sampling; the match cache; any change to the
  verdict record shape beyond the template address it already carries.

## Impl.Index

### Current.State

- `src/agentos/tournament/template.py` builds a `Match.Template` —
  `{template_version: 1, sections: [...]}` — with exactly three section kinds:
  `brief` (question + criteria, origin `definition`), `candidates` (one
  presentation address per player, origin `engine`), `footnote` (origin `engine`).
  `render_template` renders those three kinds and raises on any other.
- `src/agentos/tournament/components.py` is the depot-wide content-addressed
  registry: `put(bytes) -> "sha256:…"`, sharded, atomic, idempotent.
- `src/agentos/tournament/hooks.py` declares seven hooks. `present_player`
  returns **a string**; the module attributes `question` and `criteria` are the
  only other definition-supplied prompt material.
- `runner._composed` calls `build_template`, renders, registers, and returns
  `(verbatim, template_address, bindings)`. `run_match` and `preview_match` both
  route through it.
- `tests/test_tournament_template.py` pins the pre-template frame as a byte-equality
  oracle across arities 2/4/26.

Consequences that motivate this work:

- There is **nowhere to put shared match material**. The typing tournament's type
  vocabulary must be duplicated into every player presentation, five times per
  match, or omitted — and it is currently omitted in truncated form inside each
  card.
- **The definition renders its own text.** Because `present_player` returns
  opaque bytes, the engine can neither validate what it holds nor apply any
  generic operation to it (shuffle, cite-resolution, redaction).
- **Randomization inside a definition is invisible.** A definition that calls
  `random.shuffle` produces a match the engine cannot reproduce or explain; the
  realized order is recorded nowhere.

### Design.Decisions

- **A `Match.Frame` is the single composition surface.** The definition returns
  one frame; the engine renders it. Two requirements are structural: the frame
  must carry the question, and it must carry exactly one `Players` placeholder.
- **The engine owns the roster; the definition owns the card.** `Players` is a
  placeholder node, never a list the definition fills. Control substitution,
  sampling, and position labelling stay engine work — the definition declares
  only how one player renders.
- **Content is open; operations are closed.** New content shapes compose from
  the node types without engine change. Operations must be enumerated because
  each one needs engine machinery — seeding, recording, reproducibility. An
  operation the engine cannot record is a hole in the instrument.
- **Node types are structural, not domain-named.** `Text`, `Table`, `Sequence`,
  `Section`, `Players`, `Raw`. "Question", "criteria", "reference", "glossary"
  are *labels on sections*, not types. Naming instances as types is what made the
  current template inextensible.
- **Every node is hashed under `(type, version, payload)`.** The version is
  inside the hash because a node type whose rendering changes must not rebuild
  an old verdict into text the judge never saw.
- **Two hash layers.** A node address is content only, so identical material
  dedups across matches and tournaments. The match's template address covers the
  composed structure; the realized order of any shuffle rides `template_bindings`
  beside the ticket id, because a permutation is per-match and would defeat dedup
  if it lived in the template.
- **`Raw` is the named escape hatch.** Without one, material the vocabulary
  cannot express gets smuggled into a `Text` node and looks structured when it
  is not. Leaving the language must be visible.
- **Shuffle is refused on ordered nodes.** A `Sequence` is ordered by
  construction and shuffling it destroys content; a `Table` is a lookup keyed by
  its entries and shuffling it only removes a positional hint. The engine raises
  rather than silently obeying.
- **`Cite` resolves at frame build, before any judge spend.** A card citing a
  key no table defines is a definition bug that must not cost a spawn.
- **Backward compatibility is a byte-equality obligation, not a courtesy.** A
  definition with no `match_frame` hook must produce the exact bytes it produces
  today, and `template_version: 1` must keep rendering. A verbatim that cannot be
  rebuilt exactly cannot be checked against `verbatim_hash`.

### Open.Space

- Whether the frame should be built once per tournament rather than once per
  match. Per-match is implemented here because it matches every other hook and
  because content addressing makes an unchanging frame free. If frames are later
  observed to vary within a tournament for no good reason, that is a lint, not a
  redesign.
- Whether `hide` belongs in the operation set. Labels are already reader-side by
  construction, so nothing needs it yet.
- Whether a future node type should carry its own renderer version independently
  of `TEMPLATE_VERSION`. Today one bump covers both.

## Execution.Plan

### Slice 1 — `frame.py`: the typed node model

- New module `src/agentos/tournament/frame.py`.
- Frozen dataclasses: `Text(body)`, `Table(entries, ordered=False)`,
  `Sequence(items)`, `Section(label, body)`, `Players()`, `Raw(body)`, and the
  `Cite(table, key)` marker usable inside a card.
- Each node serializes canonically to `{"type", "version", ...payload}` via
  `json.dumps(sort_keys=True, separators=(",", ":"), ensure_ascii=False)`; the
  address is `sha256:` over those bytes.
- Deterministic `render_node(node) -> str` for every type.
- **Check**: `uv run pytest tests/test_tournament_frame.py`. Tests assert
  canonical serialization is order-independent for dict payloads, that two equal
  nodes share an address, that a version change changes the address, and that
  every node type renders.

### Slice 2 — the `match_frame` hook

- Add `MATCH_FRAME = "match_frame"` to `DEFAULTED_HOOKS`.
- `TournamentDefinition.match_frame(players, presentations)` returns a validated
  `Frame` or `None`. `None` means the legacy frame.
- Validation at return: exactly one `Players` node; a question present; every
  `Cite` resolves against some `Table` in the frame; unknown objects rejected
  with a `HookReturnError` naming the offending node.
- `present_player` accepts a node **or** a string; a string wraps as `Text` so
  every existing definition keeps working.
- **Check**: `uv run pytest tests/test_tournament_hooks.py -k frame`. RED first:
  a definition citing a missing table must fail at frame build, not at render.

### Slice 3 — template v2 renders a frame

- `build_template` gains a `frame` argument. With a frame it emits
  `template_version: 2` and one section per frame node, each naming its component
  address, with `origin` `definition` or `engine` as before. `Players` expands to
  the existing `candidates` section so position labelling is untouched.
- `render_template` dispatches on `template_version`: v1 keeps its current code
  path verbatim; v2 renders nodes.
- `register_template` unchanged in shape — it already writes every named
  component.
- **Check**: `uv run pytest tests/test_tournament_template.py`. The existing
  byte-equality oracle must still pass unmodified — that is the load-bearing
  assertion of this slice. New tests assert a v2 template round-trips through
  `reassemble` to identical bytes.

### Slice 4 — the `shuffle` operation

- `shuffle(node)` marks a node for engine-applied permutation. Applied in
  `runner._composed` with a `random.Random` seeded from the match, exactly as
  presentation order already is.
- The realized permutation is recorded in `template_bindings` under
  `frame_operations`, keyed by the node's position in the frame.
- `shuffle` on a `Sequence`, or on a `Table(ordered=True)`, raises at frame
  validation.
- **Check**: `uv run pytest tests/test_tournament_frame.py -k shuffle`. A
  reassembled verdict must reproduce the shuffled order byte-for-byte from
  `frame_operations` alone.

### Slice 5 — wiring and documentation

- `runner._composed` and `compose_verbatim` pass the frame through; `run_match`
  and `preview_match` both obtain it from the definition.
- Export the frame vocabulary from `agentos/tournament/__init__.py` so a
  definition can `from agentos.tournament import Text, Table, Section, ...`.
  (Note `Issue.I0001`: the snapshot freezes the definition file, not its imports.
  This widens that surface and does not resolve it.)
- Update `AGENTS.md`'s Tournament System section: the frame, the node types, the
  operation set, the two hash layers, and the v1/v2 rendering split.
- **Check**: `uv run pytest tests/ -k tournament` green; `uv run ruff check src tests`.

### Acceptance

- A definition can render shared reference material once per match, with player
  cards citing into it.
- Every definition that does not define `match_frame` produces byte-identical
  prompts to today.
- A v1 verdict still reassembles; a v2 verdict reassembles including its
  shuffled order.
- A frame with an unresolvable cite fails before any judge spawn.
- `AGENTS.md` documents the frame.

## Impl.Log

- **Slice 1 — Done.** `src/agentos/tournament/frame.py`, 30 tests in
  `tests/test_tournament_frame.py`. Node vocabulary landed as designed.
- **Slice 2 — Done.** `match_frame` added to `DEFAULTED_HOOKS`.
  **Deviation**: the plan implied `present_player` would keep one return path.
  It grew a sibling, `present_card(player) -> (text, node | None)`, and
  `present_player` delegates to it. The reason is that the card's node must reach
  the composition point for cite validation, and the alternative — caching the
  node on the definition — is shared mutable state across the `run_pool` threads.
  Returning it is the only version with no race in it.
- **Slice 3 — Done.** `TEMPLATE_VERSION = 2`, `LEGACY_TEMPLATE_VERSION = 1`, both
  rendered. The pre-existing byte-equality oracle passes unmodified, which is the
  assertion this slice was for. **Deviation from the plan's "one section per frame
  node"**: the whole frame is a *single* component instead. The frame is constant
  across a run, so per-node sectioning would multiply addresses without dedupping
  anything the presentations do not already dedup, and it would have split the
  render across two ordering authorities.
- **Slice 4 — Done.** `plan_operations` draws from the match rng in
  `runner._composed`, beside the presentation shuffle. Permutations land in
  `template_bindings["frame_operations"]`, keyed by depth-first shuffle-site index.
- **Slice 5 — Done.** Frame vocabulary exported from `agentos.tournament`;
  `AGENTS.md` Tournament System section extended with eight entries covering the
  node vocabulary, the open-content/closed-operation split, the shuffle refusals,
  the roster boundary, cite resolution, node addressing, the two template
  versions, and permutations-as-bindings.

**Verification**

- `uv run pytest tests/` — 1876 passed.
- `uv run ruff check src tests` — clean.
- End-to-end preview against the real index surfaces
  (`agentos-pkg/design/111-design.md` typed against `106-design.md`): a five-line
  match rendered the seven type definitions **once**, shuffled, with each card
  citing its code. The material a card used to duplicate five times per match now
  appears once.

**Finding from first use.** A player card wants inline `label: value`
composition, which no node appeared to offer — the first card built from
`Section` rendered its label and its cite as two paragraphs. An unnamed
`Table("", {...})` produces exactly the right shape, so the vocabulary already
covers it and no node type was added. Worth remembering before the next request
to grow the vocabulary: the pressure to add a type is usually pressure to
compose the existing ones differently.

**Not done, deliberately.** The loop workspace's three scorers still use the v1
path. Rewriting them is the named follow-on, and it is where the truncated
type definition (`_load_vocabulary` taking only each block's first line) gets
fixed — the frame makes the whole block affordable because it is rendered once.
