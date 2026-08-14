# Project.Chat.Reconciliation.Operation.Module

Use this module to compare a current Project Index with the Chat.Index surfaces named by its `009-SUPPORT-CHATS.md` registry.

## Mechanical Pass

- `agentos chatlas project-index audit --depot <depot> --json` is read-only and scans each available support Chat.Index once
- ordinary current Project lines seek exact `Chat.Index.HEAD` presence plus an exact Delta home
- `Issue.Block` and other maintenance lines require an exact Delta home; Chat HEAD participation is optional
- missing registries, unavailable Chat.Indexes, missing or ambiguous homes, content drift, absent issue context, and insufficient origin evidence remain advisory POIs
- exact copied wording does not prove itself: absent a matching dossier chat observation, retain semantic review for possible passive import

## Cursor Pass

- `agentos chatlas project-index reconcile --depot <depot> --json` performs the same audit and advances one machine cursor per registered chat
- cursors live under project `.agentos/state/index-reconciliation/`, never inside Project HEAD
- unchanged reruns return no candidate lines; append-only growth returns only new Delta candidates; revised ranges reopen from their first changed Delta
- `--reset` discards prior cursor positions before a full inspection

The CPU pass only narrows candidates. An agent evaluates semantic contradictions or relevance and routes worthwhile current work into grounded `Issue.Block`s. Project-first and Chat-first edits are both legal; use the Chat.Index Capture.Plan workflow to backfill missing Deltas or HEAD projections without bypassing transcript evidence.
