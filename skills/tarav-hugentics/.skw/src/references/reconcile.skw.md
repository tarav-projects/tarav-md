# Parked.Project.Chat.Reconciliation

This file is not a runnable Hugentics module and no public router selects it.

The former Project/Chat reconciliation workflow was retired while `Real.Time.Capture` is rebuilt incrementally around Chatlas2. Its potentially valuable design—background gap filling, incremental cursors, drift detection, and agent review of cross-surface candidates—is parked in the workflow-retirement issue at `issues/100-issues.md`.

Git retains the former implementation. Reintroduction requires a fresh design against the current partial-receipt Chat.Index model; do not revive the Chatlas1 workflow or its exact-Delta-home assumptions by copying this file's history forward.
