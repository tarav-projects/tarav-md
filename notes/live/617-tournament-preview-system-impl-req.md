# Tournament Preview System - Impl.Req

## Impl.Abstract

- **Goal:** finish the tournament preview affordance — a way to render one real, answerable match without spawning a judge — and mark preview tickets so they stay distinguishable from the ones a judge failed to answer.
- **Status:** ready for execution; not started.
- **Starting state, stated plainly:** `agentos tournament preview` and `runner.preview_match` already exist and are green, but they were built ad hoc in conversation rather than through this workflow, and they are uncommitted. This request formalizes that work and closes the one defect it introduced.
- **Source design:** `agentos-pkg/design/111-design.md` — `Tournament.Ticket` (`^c20260806-64u`…`-68u`), `Tournament.Depot` (`^c20260806-69u`…`-71u`).
- **The defect:** a preview mints a ticket that will never be redeemed, which is indistinguishable on disk from a ticket a judge was given and failed to answer. Tune a question for an afternoon and the orphan pile is entirely previews, so the one place that records judge failure stops meaning anything.
- **In scope:** a `kind` field on the ticket separating `match` from `preview`; `gc` reporting the split; the preview command already built.
- **Out of scope:** any index capture — preview is a development affordance over the existing ticket lifecycle, not a design concept, and `^c20260806-64u` already covers what a ticket authorizes without requiring that a judge was spawned. Also out: a shorter horizon for preview tickets, since a preview ticket is deliberately answerable by hand and sweeping it early would defeat that.

## Impl.Index

### Why Preview Exists

- `run --dry-run` mints no ticket, so it renders a prompt with no submit instruction — roughly a third of what a judge actually reads is missing. It answers "what would run", not "what will the judge see".
- Iterating on a definition's `question` and `criteria` is the main development loop for any consumer of this engine, and it should not cost judge spawns.
- Preview mints a genuine ticket, so its output is byte-identical to what a judge receives and can be answered by hand with `tournament submit`. That round trip is the point: it exercises the frame, the ticket, the contract, and the store without a provider.

### Ticket Kind

- `Ticket` gains `kind`, one of `match` or `preview`, defaulting to `match` so an existing ticket file reads unchanged.
- `runner.run_match` mints `match`; `runner.preview_match` mints `preview`.
- Nothing about validation, redemption, or the cap varies by kind. A preview ticket is a real ticket — it is answerable, and answering it records a real verdict. The field says where it came from, not what it may do.
- `gc` reports removed counts split by kind, so a sweep says how much of the pile was development noise.
- The unredeemed-preview count is the useful read the field buys: unredeemed `match` tickets are judge failures, unredeemed `preview` tickets are just tuning.

## Impl.Agendix

- **Gate `^c20260806-126u`** — the `--impl --dev --AUTO` turn asking for the marker field and the formalization.
- **Touched — `agentos-pkg/design/111-design.md`**: `Tournament.Ticket` (`^c20260806-64u`, `-65u`, `-68u`), `Tournament.Depot` (`^c20260806-70u`, `-71u`).
- **Structural** — `notes/live/614-tournament-ticket-submit-impl-req.md` built the ticket lifecycle this extends.
- **Open.Space** — whether preview tickets deserve their own horizon has no index home and stays unanchored.

## Execution.Plan

### Slice 1 - Ticket kind

- Add `kind` to `Ticket` with a `match` default; thread it through `mint`, `as_dict`, and the payload reader.
- RED: prove a minted ticket defaults to `match`; prove `preview` round-trips; prove a ticket file written before this field still loads as `match`; prove kind does not change redemption, the cap, or validation.
- GREEN: implement.
- Check: `uv run pytest tests/test_tournament_tickets.py -q`.
- Observable: a ticket file carries its kind.

### Slice 2 - Minting sites and gc reporting

- `run_match` mints `match`, `preview_match` mints `preview`; `sweep` returns counts by kind and `gc` prints them.
- RED: prove a preview mints `preview` and a run mints `match`; prove a hand-submitted preview ticket still records an ordinary verdict; prove `gc` reports the split.
- GREEN: implement.
- Check: `uv run pytest tests/test_tournament_submit.py tests/test_tournament_runner.py -q`.
- Observable: `agentos tournament gc` distinguishes development noise from judge failure.
- Depends on Slice 1.

### Slice 3 - Docs and full-suite green

- Refresh the `Tournament System` section of `agentos-py/AGENTS.md`.
- Check: `uv run pytest -q`.
- Observable: the preview loop is documented as the way to tune a question without spending spawns.
- Depends on Slices 1-2.

## Impl.Log

### Blockers

- None.

### Decisions in open space

- **`kind` rather than a boolean.** `is_preview` would need a second field the moment a third origin appears; a small closed vocabulary costs the same today and does not.
- **Kind changes no behaviour.** Making a preview ticket unanswerable would remove the exact property that makes preview useful — that you can hand-run the whole loop.
- **One horizon for both.** A preview ticket is answerable by hand, so sweeping it faster would defeat its purpose; the field makes the pile readable without making it shorter-lived.

### Deviations

- Recorded during execution.
