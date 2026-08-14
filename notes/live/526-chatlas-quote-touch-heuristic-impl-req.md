# 526 — Chatlas quote touch heuristic

## Impl.Abstract

- **Scope:** add `tarav chatlas touch-heuristics quotes --session <selector> --min-length 40 --threshold 0.75 --lookback 5` as a read-only tool over one authoritative `Chatlas.Session.Model`.
- **Status:** ready for autonomous execution.
- **Source:** the user identified a significant user quotation of preceding visible assistant text as `Touch.Evidence`, accepted bounded predecessor search plus configurable length/alignment gates, and authorized autonomous development. ^c20260814-11u
- **Out of scope:** changing normalization, annotating or persisting findings, interpreting agreement/approval/truth, indexing the corpus, or adding touch heuristics other than quotations.

## Impl.Index

### Touch.Evidence

- A qualifying quotation in a normalized `User.Turn` proves touch under this heuristic.
- Detection is deliberately false-positive tolerant: the command returns every turn-pair alignment crossing both configurable gates and exposes its evidence and score.
- The tool performs no semantic adjudication and writes no finding or relationship back into Chatlas.

### Turn projection

- Operate only on transcript-visible message events grouped by normalization-owned `Normal.Turn` annotations.
- A user turn compares only with earlier visible assistant turns in tape order.
- `lookback` counts predecessor assistant turns, not raw events or timestamps; distance `1` is the nearest qualifying assistant predecessor.
- Concatenate the visible message text inside each turn in tape order and return durable `Normal.Turn.Ref`s for both sides.

### Quote alignment

- Normalize text into case-folded Unicode alphanumeric tokens, ignoring whitespace, punctuation, control characters, and other non-token material while retaining token-to-original offsets.
- First detect normalized exact substrings. When none reaches `min_length`, use token-level local sequence alignment so omissions, insertions, and changed words can still match.
- `min_length` is the minimum normalized-character length on both aligned sides.
- `threshold` is a closed `[0,1]` score: matched aligned tokens divided by the larger aligned token span.
- Emit at most the best alignment for each user/assistant turn pair. Prefer longer qualifying evidence, then the higher score, with deterministic tape-order output.

### Result contract

- The top-level result identifies the command, selected session, effective parameters, and finding count.
- Every finding carries `class: Touch.Evidence`, `heuristic: quotes`, user and assistant `Normal.Turn.Ref`s, original-text spans with offsets and text, both normalized aligned texts, alignment score, predecessor distance, and `exact|fuzzy` match kind.
- `--session` accepts a provider-native session id, canonical session URI, or full/prefix neutral identity hash; zero and ambiguous matches fail clearly.
- Chatlas shared output handling supplies human-readable output by default and raw JSON under `--json`.

## Impl.Agendix

- **Chat → touched:** command shape, heuristic semantics, defaults, result evidence, and autonomous implementation authority. ^c20260814-11u
- **Index → touched:** `Chatlas.Query.Surface`, `Normal.Turn`, `User.Turn.Purity`, `Normal.Turn.Ref`, and `Chat.Touched.Index` in `tarav-chatlas-pkg/design/100-design.md`.
- **Structural:** `tarav-py/src/tarav/chatlas/commands.py` composes the public parser; `_command_support.py` owns handlers; `session_cache.py` loads authoritative models; `normal_turn.py` constructs durable turn references.

## Execution.Plan

### Vertical.Slice 1 — Alignment engine and evidence projection

- **Status:** pending.
- **RED:** focused tests establish exact normalized substring detection, fuzzy local alignment, original spans, turn refs, threshold/minimum-length exclusion, and bounded predecessor distance.
- **GREEN:** add one focused Chatlas module that projects visible normal turns, aligns each user turn against its bounded assistant predecessors, and returns the evidence contract.
- **Check:** `uv run pytest tests/chatlas/test_touch_heuristics.py`.

### Vertical.Slice 2 — Single-session CLI

- **Status:** pending.
- **RED:** command tests require the accepted parser shape, selector resolution, shared `--json` output, validation failures, and an end-to-end quotation finding from a normalized Codex session.
- **GREEN:** register `touch-heuristics quotes`, add the command handler, and resolve `--session` against session id, URI, or identity hash before loading the authoritative model.
- **Check:** focused CLI/output tests plus `tarav chatlas touch-heuristics quotes --help` after editable reinstall.

### Vertical.Slice 3 — Documentation and regression verification

- **Status:** pending.
- Update `tarav-py/AGENTS.md` because the public Chatlas CLI surface changes.
- Run focused Chatlas tests, the complete Chatlas test directory, Ruff on touched Python files, strict project Skw checks where applicable, and `git diff --check` in both repositories.
- Inspect a real session result without treating its FPAO findings as persisted truth.

## Acceptance.Signals

- The accepted command works with defaults `40`, `0.75`, and `5` and exposes all three parameters in output.
- Exact copied text and lightly edited quotations are detected; short/common fragments and alignments below threshold are excluded.
- Findings use only prior visible assistant turns and carry verifiable refs plus inspectable spans.
- The tool mutates neither the Normal Model nor any Chatlas relationship/finding store.
- Relevant and complete Chatlas tests pass with no unrelated diff.

## Deviation.Triggers

- Record and adapt if current Normal Model surfaces cannot produce stable original-text spans without changing normalization.
- Stop rather than weakening `User.Turn.Purity` if a candidate user event is not positively grouped as a normalized user turn.
- Do not add a third-party alignment dependency unless the standard-library implementation cannot satisfy bounded-session behavior.

## Impl.Log

- 2026-08-14 — design and autonomous execution authorized by ^c20260814-11u.
- 2026-08-14 — tooling-name drift: the live-surface and workflow references still say `agentos`; the installed and repository-owned CLI is `tarav`, whose equivalent prefix/query/Anchory commands were used.

