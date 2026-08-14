# Project Support Chats - impl-req

## Impl.Abstract

- **goal:** materialize `009-SUPPORT-CHATS.md` for `tarav-pkg` and provide a reusable agentic workflow for deriving mandatory support-chat membership from Index anchors
- **status:** implemented and verified
- **scope:** add Chatlas-owned anchor-to-session extraction, an `tarav-pkg` auxiliary skill, root Package.Skill routing, and the first real `tarav-pkg/009-SUPPORT-CHATS.md`
- **authority:** the user authorized autonomous development of this slice ^c20260803-2u
- **owning projects:** `agentos-chatlas-py` owns Chatlas support-record interpretation and its CLI; `agentos-md` owns the Package.Aux.Skill and `tarav-pkg` Index surfaces
- **out of scope:** Git-derived chat candidates, automatic candidate approval, Chat.Index capture/regeneration, external Project or Package Index lookup during Chat.Index construction, and widening the reviewed Index floor parser
- **acceptance:** an agent can scan a file or directory with a caller-supplied regex, resolve every discovered Chatlas anchor to unique sessions, inspect unresolved/invalid findings, and maintain an identity-hash-based `009-SUPPORT-CHATS.md`

## Impl.Agendix

- **touched (chat):** `Project.Support.Chats` is the project-side bridge to stable Chat.Index surfaces; every chat referenced by an Index support anchor is a mandatory member
- **touched (chat):** `009-SUPPORT-CHATS.md` is the chosen materialized surface beside `000-INDEX.md`
- **touched (index):** `Package.Aux.Skill`, `Agentos.Index.System`, `Anchory.System`, `Support.Set`, and `Touched.Support.Network` constrain the workflow
- **structural:** generic `agentos.anchory.scan_anchory_source` already owns regex extraction and source coordinates
- **structural:** `agentos-chatlas-py` already owns `chatlas_anchory_depot`, support-record parsing, session-index lookup, Chat.Index discovery, and the `agentos chatlas anchory` command group
- **structural:** depot parsing ignores unknown router-adjacent Markdown, so `009-SUPPORT-CHATS.md` can remain a special stable surface without becoming reviewed ontology or appendix content
- **open space:** later heuristics may propose additional support chats, but agents must review those candidates before adding them

## Impl.Index

### Project.Support.Chats

- `Project.Support.Chats` is an Index-owned registry of chats relevant to one project or package Index
- `009-SUPPORT-CHATS.md` is its stable materialization and identifies chats by immutable Chatlas `identity_hash`; provider session ids, URIs, depot paths, Chat.Index state, and staleness are derived metadata
- sessions named by support members of any in-scope Index anchor are mandatory members
- explicit and heuristic candidates may extend the registry later, but do not weaken mandatory anchor closure
- the registry does not participate in Chat.Index construction; Chat.Index remains closed over the target chat content

### Anchor.Session.Extraction

- the public command is `agentos chatlas anchory sessions`
- generic Anchory owns regex extraction; Chatlas owns interpreting resolved records as session identities, preserving the foundation-package dependency direction
- `--source` is repeatable; a file is scanned directly and a directory expands recursively through a configurable Markdown glob
- `--regex` is required so callers control the anchor vocabulary; a named `anchor` group, first capture group, or whole match follows the existing generic Anchory contract
- extraction deduplicates source files, anchors, and sessions deterministically while retaining every source occurrence needed for review
- equivalent `Support.Set` contents across different anchors do not duplicate sessions
- unresolved anchors, tag-mismatched resolutions, non-Chatlas records, and malformed support records are reported explicitly rather than silently discarded
- each resolved session carries source anchors, support-member count, current Chatlas index metadata when available, and Chat.Index discovery state
- the command is read-only and emits stable JSON with `status=ok|needs-review`

### Agentos.Support.Chats.Skill

- `tarav-support-chats` is a hand-managed `Package.Aux.Skill` routed from `tarav-pkg`
- it accepts an Index target plus optional regex/glob overrides, discovers the target's router and Index-owned Markdown sources, runs the Chatlas extractor, reviews findings, and maintains `009-SUPPORT-CHATS.md`
- the initial tarav-pkg source set is `000-INDEX.md`, `design/`, `appendix/`, `agendix/`, and `poi/`; generated references and the support-chat registry itself are excluded
- the skill never treats unresolved or malformed anchors as successful closure
- the root `tarav-pkg` route is authored in `.skw/src/SKILL.skw.md`, declares the new dependency, and is compiled through Skillware

## Execution.Plan

### Slice 1 - Chatlas anchor-to-session extraction

- RED: add command-level tests covering repeatable file/directory sources, regex extraction, duplicate anchors, session deduplication, source occurrences, unresolved anchors, and indexed session metadata
- GREEN: implement the application API in `anchory.py`, add `chatlas anchory sessions`, and keep JSON deterministic and read-only
- update `agentos-chatlas-py/AGENTS.md` where its Chatlas Anchory ownership contract is extended
- **observable:** one command turns an arbitrary Markdown source set into a reviewable support-session inventory

### Slice 2 - Package auxiliary workflow

- add `skills/tarav-support-chats/SKILL.md` using Batchy Package.Aux.Skill conventions
- route the workflow from the Skillware source for `tarav-pkg`, declare the skill dependency, then build and check the compiled Package.Skill
- **observable:** `$tarav-pkg` can route support-chat discovery and maintenance without loading Chatlas implementation detail eagerly

### Slice 3 - tarav-pkg materialization

- run the new command over the complete `tarav-pkg` Index source set with the canonical Chatlas anchor regex
- resolve findings before claiming closure, then add `009-SUPPORT-CHATS.md` and a compact `000-INDEX.md` pointer
- list unique mandatory chats by `identity_hash` with useful derived metadata and extraction counts
- **observable:** the package has a durable, inspectable registry of every chat currently reachable from its Index support anchors

### Slice 4 - Verification

- run focused extraction tests, the full Chatlas test suite, Ruff, Skillware build/check, the live tarav-pkg extraction, and relevant Index lint
- cold-read the generated registry against the command output and update this artifact's ledger

## Implementation.Ledger

| Slice | State | Result | Verification |
|---|---|---|---|
| 1 | complete | `agentos chatlas anchory sessions` scans repeatable file/directory sources, resolves support records, deduplicates sessions, preserves source coordinates, and reports review findings | 35 focused Anchory tests pass; RED covers duplicates, unresolved anchors, invalid records, tag mismatch, unindexed members, metadata, and Chat.Index discovery |
| 2 | complete | `tarav-support-chats` Package.Aux.Skill added and routed from the Skillware-authored `tarav-pkg` root | Skill Creator validation passes; Skillware build and check report zero findings |
| 3 | complete | `tarav-pkg/009-SUPPORT-CHATS.md` materializes 31 mandatory chats from 1,309 resolved anchors across 96 Index files | live extraction reports `status=ok`, zero findings, and exact registry identity/order agreement |
| 4 | complete | scoped code, skill, registry, and Index verification pass | Ruff passes; Index lint reports zero findings; full Chatlas suite passes 330 / 330 tests |

## Impl.Log

- 2026-08-03: implementation route selected as Hugentics develop with autonomous alignment ^c20260803-2u
- 2026-08-03: ownership inspection placed source extraction in generic Anchory, record interpretation in Chatlas, and agentic maintenance in an `tarav-pkg` auxiliary skill
- 2026-08-03: parser inspection confirmed `009-SUPPORT-CHATS.md` remains outside reviewed ontology/appendix parsing while staying discoverable through the router
- 2026-08-03: checkpoints created before implementation edits: `agentos-md@91a6610` and `agentos-chatlas-py@a023f80`
- 2026-08-03: Slice 1 added the Chatlas-owned command and integrated it with the concurrently introduced `--text|--json` output contract; JSON remains the stable agent handoff requested by this design
- 2026-08-03: Slice 2 added the hand-managed Batchy auxiliary skill and the Skillware dependency/router row; the generic skill initializer was not used because repository editing is constrained to `apply_patch`, and the resulting skill passed the same validator
- 2026-08-03: live extraction closed 1,309 / 1,309 anchors into 31 sessions with no unresolved, malformed, or tag-mismatched records; one session currently has a materialized Chat.Index
- 2026-08-03: final verification passed after the concurrent output-normalization slice settled: 330 / 330 Chatlas tests, Ruff, Skillware check, skill validation, Index lint, and live registry comparison are green
