# Chatlas Anchor Integration — Impl.Req

## Impl.Abstract

- **Goal**: make chatlas the application layer of the anchor system — event-level selection for finding evidence turns, `--anchor` as a first-class reference across the query language, chatlas-owned minting that returns the landing turns, and full `Chat.Ref` retirement.
- **Scope**: `views inline` event filters (`--contains`, `--role`, `--around`); `--anchor`/`--radius` windowing; `agentos chatlas anchory register`; removal of `chat_ref.py` and every `--ref` surface.
- **Out of scope**: a general time-softener flag for all filters (deferred — implement what actual workflows demand, same principle as anchory `next`); anchory-core changes (allocation is `568-anchory-prefix-allocation-impl-req.md`, in execution); namespaces; view classes beyond the existing projection set; the agendix/index write side.
- **Repos**: `agentos-chatlas-py` (`inline.py`, `query.py`, `chat_ref.py`, `anchory.py`, `commands.py`, `normalization/session_model/_views.py`, tests); e2e parser coverage in `agentos-cli` if chatlas e2e tests exist there (inspect; add alongside). Reinstall note: `agentos` executable owned by `agentos-cli`, `uv tool install --reinstall --editable .` after CLI changes.
- **Source**: this design session (first end-to-end linking run + chatlas co-design discussion); `notes/live/567` items 2–3; index concepts `Chatlas.Anchory`, `Anchory.System/Chat.Application`, `Chatlas.Session.Model`, `Session.Event.Tape`, `Chatlas.Query.Envelope`, `Index.Linking`.
- **Status**: ready for implementation (blocked only on 568 for S3's registration call)

## Impl.Index

### Design.Principle:Model.Closed.Output
- every chatlas output is a fragment of the `Chatlas.Session.Model` — the output vocabulary stays closed on the model space (user constraint, this session)
- turn search results, anchor neighborhoods, and mint echoes are all tape projections through the existing view machinery, never ad-hoc row shapes
- the `Chatlas.Query.Envelope` continues to separate query accounting from row projection

### Design.Principle:One.System
- chatlas anchory and the chatlas query language are the same system, co-designed: an anchor is a session/window selector the query language accepts natively, and query surfaces are how anchor records are validated and read back
- `Anchory.System/Integration` split holds: chatlas owns record meaning and traversal; anchory stays plumbing — chatlas never touches register files directly, always through the anchory library

### Current.State *(inspected, cited)*
- `views inline` (`inline.py:12`) selects one session, loads the model, projects via `project_chatlas_session_model_view(view, window, range_spec)` — windowing today comes from `chat_ref.window_bounds()` (`inline.py:60`): the `Chat.Ref` grammar is the current window source and the socket anchors replace
- `chat_ref.py` (131 lines) implements the retired `@<hash>-<timetag>` grammar; `--ref` flags ride `query` and `views inline`
- view projections live in `normalization/session_model/_views.py`; `range_spec` is zip-transcript-only (`_views.py:56`)
- `anchory.py` currently only wires the depot (`chatlas_anchory_depot()`); the 568 executer may extend it — rebase on whatever it lands
- events on the tape carry `event_id`, `timestamp`, `kind`, `payload`, `interaction_ref` (verified live, schema v3)

### Event.Selection
- `views inline` gains event-level selection flags: `--contains <text>` (payload text match), `--role <role>` (producer/message role), `--around <ISO time>` (proximity ordering: closest events to the time)
- selection composes with the existing `--view` projections: the output is the same model fragment shape, filtered — a "search result" IS a tape fragment
- `--around` without other filters returns the nearest events window; with filters, it orders/limits matches by proximity
- selection flags apply to the single-session inline surface; session discovery stays in `query`

### Anchor.Reference
- `--anchor <key>` on `views inline`: resolve through the chatlas anchory depot → record (`app`, `session`, `at`, `hint`) → select the session by record, window the tape around `at` — `--radius N` sets the neighborhood size in events (default small, e.g. 4)
- `--anchor` conflicts with explicit session selectors only when they disagree (the record names the session; passing both is a consistency check, mismatch is an error)
- resolution output is a normal view projection of the neighborhood — the reading rule ("land and read around") as one command
- unresolvable anchor → clean error naming the depot and key; a resolvable anchor whose session is not in the chatlas index → error that names the desync

### Anchory.Mint
- new command: `agentos chatlas anchory register --identity-hash <H> --at <ISO> --hint "<one sentence>"` (session selectors beyond identity-hash accepted like other single-session commands)
- validation before registration: the session exists in the chatlas index; `at` falls within the session's time bounds; the nearest event to `at` exists — the record must point at real turns
- builds the `Chatlas.Anchory` record `{app:"chatlas", session, at, hint}`, derives the date prefix from `at` (`YYYYMMDD`), registers through anchory's atomic prefix allocation (568), depot `<chatlas-root>/anchory/`
- output: the allocated anchor PLUS the landing neighborhood as a model fragment (reuse the `--around` selection) — the agent double-checks the anchor points where intended before tagging lines
- `Impl.Req` boundary: chatlas validates at mint time but the register stays plumbing — desync detection remains a reader concern

### Chat.Ref.Retirement
- delete `chat_ref.py`; remove `--ref` flags from `query`, `views inline`, and any other surface; drop `ChatRef` imports and window plumbing
- `No.Legacy.Allowed`: no compatibility shim, no deprecation period — anchors are the only chat reference
- sweep `agentos-chatlas-md` skill/reference surfaces for `Chat.Ref`/`--ref` mentions; update the `Chatlas.Anchory` index block only via the gated path (propose, do not self-write)

## Execution.Plan

### S1 — Event selection on `views inline` (test-first)
- what changes: selection flags `--contains`/`--role`/`--around` filter/order the event tape before projection
- RED: filtered `events` view returns only matching events with their model envelope intact; `--around` returns nearest-first; filters compose; non-matching filter returns an empty but well-formed fragment
- check: suite green; live: locating the "two different sections" turn in session `9d194db7…` is one command
- observable: turn search without client-side payload scanning

### S2 — `--anchor` windowing
- what changes: anchor resolution as window source in `inline.py`; `--radius`
- RED: minted test anchor resolves to the right neighborhood fragment; unresolvable anchor errors cleanly; session-mismatch errors name the desync; radius bounds respected
- check: suite green; live: `views inline --anchor 20260708-0` returns the CT-constraint turn neighborhood
- observable: the grounding reading rule is one command

### S3 — `chatlas anchory register` *(depends on 568 landing)*
- what changes: mint command with validation + landing-turn echo; `anchory.py` grows the record builder
- RED: mint returns anchor + neighborhood; `at` outside session bounds rejected; unknown session rejected; record shape matches `Chatlas.Anchory`; prefix derived from `at` date
- check: suite green; live: re-mint an anchor for a known turn and verify the echo shows that turn
- observable: the full linking pipeline (locate → mint → verify) is two chatlas commands

### S4 — Nuke `Chat.Ref`
- what changes: `chat_ref.py` deleted, `--ref` flags removed, dead window plumbing dropped, chatlas-md surface sweep
- RED→GREEN: existing `--ref` tests deleted (not ported); remaining suite green proves nothing else depended on it
- check: `grep -r "ChatRef\|chat_ref\|--ref" src/` clean; CLI help shows no ref surfaces; `agentos-md`/`agentos-chatlas-md` skill surfaces carry no live `Chat.Ref` operational references
- observable: anchors are the only chat reference in the codebase

### Acceptance signals
- locate-evidence-turn, read-anchor-neighborhood, and mint-with-echo are each a single chatlas command returning model fragments
- `chat_ref.py` gone; full `agentos-chatlas-py` suite green; `No.Regression.Tests.Allowed` respected
- `agentos-index` `link.md` pipeline steps 1–4 map one-to-one onto chatlas/anchory commands (update `link.md` in the S4 sweep)

### Risks / deviation triggers
- 568 slips: S1/S2/S4 proceed; S3 blocks — do not reimplement allocation chatlas-side
- event-payload text matching may need a payload-walk helper: keep it a projection-side utility, never a new output shape
- if `--around` semantics get contentious mid-implementation (ordering vs windowing), stop and surface — that is a design decision, not open space

## Impl.Log

- (empty — populated by the executer)
