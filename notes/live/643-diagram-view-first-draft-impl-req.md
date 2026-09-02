# Diagram.View First Draft — Impl.Req

## Impl.Abstract

- Status: Implemented and verified; post-checkpoint product changes remain uncommitted for review.
- Intent: implement and progressively specialize the usable `Diagram.View` surface.
- Scope: the `tarav-py` Diagram domain, its CLI surface, and focused tests.
- Included: a Git-backed View repository, self-contained `view.json` materialization, Model and Block scope, idempotent disclosure expansion and collapse, synchronization, checks, rendering, retained View typing, and bounded Session attention hints.
- Deferred: generalized Annotation Sources, projection caches, semantic recommendation algorithms, and sophisticated dependency inference.
- Acceptance: an Agent can create, inspect, mutate, synchronize, check, and render a retained View without manually editing its files or querying the Diagram again merely to understand visible material.

## Impl.Req.Diagram

- Namespace: `User.Touched.Chatlas.Index` / `1c99092c-ba46-4006-adc3-9ada50c00abd`.
- Model: `Tarav` / `b7b78eab-e5c2-4610-9bf5-1b704a106f34`.
- Block: `643.Impl.Req` / `8ceabdae-a2ea-4117-aa49-6d4ea915c4f5`.
- Bootstrap capture commit: `c402588115908b54436ec5763965764390069617`.

## Execution.Plan

1. Define retained View data and repository contracts.
2. Implement Diagram projection, self-contained materialization, and the disclosure ladder.
3. Expose create, inspect, expand/collapse, synchronize, check, and render operations through the CLI.
4. Verify the vertical slice with focused tests and maintained project checks.
5. Add retained `view_type` specialization with base, Session, and Project runtime classes.
6. Add Session peer-View discovery as mechanical attention hints.
7. Add bounded Diagram mention metadata and POIs without claiming relevance or Production.Context.
8. Verify the specialized slice through focused, distribution, CLI, and diff checks.

## Impl.Log

- Bootstrapped the Impl.Req directly from the current chat under Autonomous Execute alignment.
- Established the required clean Git checkpoint before product edits at `792cf93`.
- Added `tarav.diagram.views` as the retained View repository and materialization domain.
- Added `tarav diagram view create|list|show|sync|expand|collapse|include-line|exclude-line|check|render`.
- Kept disclosure ladders and inline dependency discovery on projected Diagram object classes; the View applies those mechanics without choosing semantic relevance.
- Verified focused Diagram behavior (`45 passed`), the complete Python distribution (`1484 passed`), Ruff, diff hygiene, and the reinstalled public CLI.
- Checkpointed the complete first draft at `30969ae` before the idempotence correction.
- Captured the repeated-expansion constraint as Line ship `0f195169-3fe0-49af-9b09-0fdefbaa0adb` in this Impl.Req Block.
- Made the View Git writer reuse the current edition when its exact target paths are unchanged, so no-op operations never invoke `git commit`.
- Added regressions for repeated full expansion and unchanged target commits; verified `7` focused tests, `1487` distribution tests, Ruff, and two live repeated expansions with the edition fixed at `f98316c0098ada4f611cd6a1c885eef6ab0a5585`.
- Checkpointed the idempotence correction at `8274355` before starting compact contextual rendering.
- Captured the compact-rendering constraint as Line ship `20b980d2-b88a-4a62-a605-3f3e4db42676`; its capture commit is `f6ede573c6039377c22f40d94b44978e3b786d12`.
- Reworked View disclosure so Lines render with short ships and Type codes, support disclosure contains compact statistics, and deep disclosure contains selected Chatlas text without raw support/reference JSON.
- Added unambiguous short-prefix operation for View Block and Line selectors and compacted human-facing View, commit, mutation, and about-surface identities while retaining exact machine data.
- Deduplicated deep support neighborhoods across the rendered View. The live session View fell from `329230` bytes to `75977` bytes while retaining its selected context; its synchronized edition is `441fc1a5515e78ef3271f201abb47111e323c212`.
- Removed producer and raw Chatlas reference objects from deep `view.json` materialization; retained support content now carries only a compact source pointer plus exact selected turn text.
- Verified `8` focused View tests, `1488` distribution tests, Ruff, diff hygiene, the reinstalled CLI, and the live retained View.
- Captured the typed View execution request into this Block as Line ships `949c394b-104b-4e84-86e1-5a20654ff21d` and `9313c65e-f00e-4cbd-9ece-b4ece860ff43`; capture commit `2c96d45a337cda6611100449e9a5b594fa24aad7`.
- Cold-reloaded the request and established the typed-View slice checkpoint at `df925e47b738c20fbf2037bd42a63de62466ea70` after `14` focused tests, Ruff, and diff checks passed.
- Added retained `Diagram.View`, `Session.Diagram.View`, and `Project.Diagram.View` Type selection; repository loading now instantiates the registered runtime class and rejects unknown Types.
- Added bounded Session attention mechanics: related Session View selections through `diagram view peers`, and exact Block-label/ship mentions through `diagram view mentions` and View checks. These signals do not select relevance or claim `Production.Context`.
- Migrated the live grounding View `cbcf6eeb-c2f3-483a-8225-eea44ae8bbec` to `Session.Diagram.View` at Views commit `c1eccdf`, then synchronized it at `3912a268d31fe31edca44dd9851d7724e1d9643e`.
- The live audit found `65` mentioned Diagram Blocks and surfaced `23` outside-View attention POIs; synchronization cleared the independent stale-Namespace POI.
- Verified `63` Diagram/core CLI tests and all `1495` distribution tests, Ruff, Python compilation, diff hygiene, editable installation, and live `list`, `peers`, `mentions`, `sync`, and `check` operations.
- Product.Surface context annotation remains unavailable in the current Diagram mechanics; exact implementation files and verification evidence are retained here instead of inventing that relation.
- Slice-close capture found no additional qualifying User-Touched implementation requirements after the opening two-Line capture.
