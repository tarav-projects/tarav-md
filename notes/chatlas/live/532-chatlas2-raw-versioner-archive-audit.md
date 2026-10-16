# Chatlas2 Raw Versioner Archive Audit

**Date:** 2026-08-15  
**Status:** point-in-time evidence note  
**Archive:** `/Users/pereiro/Documents/chatlas/raw`

## Question

How do the current Chatlas2 Codex and Claude `Raw.Model.Versioner`s behave when each is run against every artifact in the active Chatlas Raw Archive?

## Result

The Codex Versioner recognizes every Codex rollout transcript and rejects only four Codex sidecar indexes. The Claude Versioner is structurally sound but too strict: it rejects 1,955 otherwise compatible transcript artifacts because auxiliary records such as `file-history-snapshot` do not carry `sessionId`.

Neither Versioner recognized any artifact from the other provider or any of the 23,700 Copilot files. The two recognized sets never overlapped.

## Scope and method

- Scanned every file beneath each active provider partition's `home/` directory.
- Excluded Chatlas manifests and historical migration backups outside the active `raw/` tree.
- Used files as the scan unit because the Versioner interface accepts one raw artifact path.
- Ran `CodexRawModelVersioner.version()` and `ClaudeRawModelVersioner.version()` independently on every file; provider directory names did not gate dispatch.
- Imported the implementation directly from `tarav-py/src/tarav/chatlas2/`.
- `tarav-py` base commit: `faf646b4c569024d1eefff03e7762ace08b2711e`; the Chatlas2 implementation was in a dirty working tree.
- The archive remained live during the audit, so this is a non-atomic snapshot. File counts stayed stable; one Codex file grew between inventory passes. The byte counts below are from the definitive recognition pass.

The full double scan read about 10.78 GB twice and completed in about 116 seconds.

## Archive inventory

| Physical provider | Files | Bytes | Indexed sessions | Archive versions |
|---|---:|---:|---:|---:|
| Claude | 6,023 | 1,968,999,486 | 5,679 | 6,371 |
| Codex | 6,357 | 6,195,504,159 | 4,148 | 6,788 |
| Copilot | 23,700 | 2,618,068,484 | 3,807 | 3,807 |
| **Total** | **36,080** | **10,782,572,129** | **13,634** | **16,966** |

Physical file count and Chatlas archive-version count intentionally differ: a retained provider artifact may contain many files, especially for Copilot.

## Recognition matrix

| Physical provider | Codex only | Claude only | Both | Neither |
|---|---:|---:|---:|---:|
| Codex | 6,353 | 0 | 0 | 4 |
| Claude | 0 | 4,032 | 0 | 1,991 |
| Copilot | 0 | 0 | 0 | 23,700 |

Exact identifiers returned:

- `codex.rollout.v1`: 6,353 artifacts
- `claude.transcript.v1`: 4,032 artifacts

Across the two currently supported provider trees, the present Versioners recognize 10,385 of 12,380 files (83.89%). The lower 28.78% recognition rate across the entire archive simply reflects that Chatlas2 does not yet have a Copilot Versioner.

## Codex finding

Codex transcript coverage is complete for the observed archive:

- 6,353 of 6,353 rollout artifacts recognized: **100%**.
- 6,353 of 6,357 total Codex files recognized: **99.94%**.
- The four null results are small home-level `session_index.jsonl` sidecars, not rollout transcripts.

This is the desired recognition boundary: the Versioner accepts the raw model it promises and declines unrelated provider state.

## Claude finding

Current exact coverage is 4,032 of 6,023 files (**66.94%**) and 1,665,118,328 of 1,968,999,486 bytes (**84.57%**).

The 1,991 null results classify as follows:

| First decisive reason | Files | Interpretation |
|---|---:|---|
| Auxiliary record lacks `sessionId` | 1,970 | Current Versioner rejects the whole artifact before reaching otherwise valid transcript records |
| No `user` or `assistant` transcript records | 17 | Sidecar-only artifacts: 13 `ai-title`, 3 `system`, 1 `progress` |
| More than one session id | 2 | Two transcript-bearing files contain records from two native sessions |
| Malformed JSON | 2 | The same logical truncated artifact is retained in two raw partitions |

Of the 1,970 artifacts rejected for an absent `sessionId`, 1,955 contain structurally compatible transcript records. The remaining 15 are auxiliary-only files.

### Conservative prospective rule

A read-only simulation changed only the recognition rule:

> Require `sessionId` and transcript structure on `user` and `assistant` records; allow auxiliary records to omit `sessionId`; still require one session scope and at least one transcript record.

That rule classified the Claude tree as:

| Result | Files |
|---|---:|
| Recognized | 5,987 |
| No transcript records | 32 |
| Mixed session ids | 2 |
| Malformed JSON | 2 |

It would raise whole-file Claude coverage to **99.40%** without accepting a mixed-session, malformed, sidecar-only, Codex, or Copilot artifact.

This is strong evidence that the main gap is one over-strict Versioner condition, not 1,955 distinct Raw Model versions and not a missing Normal Model concept.

## Design evidence

The archive supports the current Chatlas2 design choices:

1. **Raw.Model.Version is Chatlas-assigned.** Recognized and rejected Claude artifacts have overlapping Claude CLI producer versions. Producer version is useful evidence, but it does not identify compatibility.
2. **Recognition belongs before normalization.** Sidecar-only, malformed, and mixed-session artifacts are cleanly separated without weakening the Normal Model.
3. **The smallest independently parseable fragment matters.** The two mixed-session files and the truncated artifact may contain recoverable transcript fragments, but should not be accepted as one whole-file `claude.transcript.v1` model.
4. **Null is meaningful.** The four Codex indexes and 32 Claude auxiliary-only files should remain unrecognized by transcript Versioners.
5. **Provider dispatch is safe on this archive.** There were zero cross-provider recognitions and zero ambiguous matches.

## Recommended next pass

1. Relax the Claude v1 Versioner exactly as simulated: auxiliary records may omit `sessionId`; transcript records may not.
2. Add one representative `file-history-snapshot` transcript artifact to the conformance corpus before changing the rule.
3. Keep auxiliary-only artifacts null.
4. Investigate the two mixed-session files and the one logical malformed artifact separately through fragment recognition or recovery. Do not broaden whole-file v1 recognition to admit them.
5. Re-run this archive audit after the change and preserve the result as the baseline for future Versioners.

No production code was changed by this audit.
