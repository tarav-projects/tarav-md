# Chatlas2 normalized Event.Hash and optional raw evidence - impl-req

## Impl.Abstract

- **scope:** make `Event.Hash` an assertion over deliberately selected provider-neutral Normal Event content; remove provider-native records from Normal Events; let each compatible normalizer optionally return opaque diagnostic `raw` evidence; omit that evidence by default; and correct the stale `agentos stdlib prefix` spelling in the Skillware-owned live-surface skill
- **status:** implementation-ready
- **source:** the current Chatlas2 design discussion and explicit autonomous develop invocation in Codex session `01a001c2-8fb1-72e0-8aa1-0bbc52c4b5e8`
- **target:** Chatlas2 mechanics in `tarav-py`, design audit in this artifact, and the canonical Skillware source for `tarav-live-surfaces` in `tarav-md`
- **out of scope:** streaming normalization; durable Normal Model caches; old-anchor migration mechanics; expanding event classes; requiring normalizers to read complete artifacts; standardizing the internal shape of normalizer-owned raw evidence
- **acceptance:** default Codex and Claude models contain no provider-native records; an explicit raw option returns source-associated normalizer evidence; default and raw-enriched runs produce identical event/message refs; amendments to selected normalized content change hashes; and the live-surface skill consistently invokes `tarav stdlib prefix`

## Impl.Agendix

- **touched (system boundary):** Chatlas2 keeps the Normal Model deliberately shallow while the retained Raw Archive remains the authority for deeper inspection (`527-chatlas2-normal-model-redesign-design-session.md`)
- **touched (event identity):** `Event.Hash` asserts current normalized content and excludes address, annotations, native identifiers, and provenance (`527-chatlas2-normal-model-redesign-design-session.md`, `Event.Ref`)
- **touched (current decision):** the fields participating in `Event.Hash` are chosen deliberately; optional raw evidence is independent from identity and hashing
- **touched (normalizer freedom):** a normalizer does whatever its supported `Raw.Model.Version` mapping requires; Chatlas2 imposes no complete-artifact inspection contract
- **touched (raw evidence):** `raw` is an optional place where a normalizer can collect diagnostic material it used to produce a fragment; it is not a completeness promise and need not have a provider-neutral internal shape
- **touched (CLI correction):** `tarav` is canonical and the `agentos` binary name is deprecated; `tarav-live-surfaces` must use `tarav stdlib prefix`
- **structural:** current Chatlas remains independent from Chatlas2; the Skillware-managed live-surface target is changed only through `.skw/src/SKILL.skw.md` and rebuilt

## Impl.Index

### Event normalized content and hash

- Normal Events expose an optional provider-neutral `content` object containing only event state that a compatible normalizer deliberately projects
- the current narrow mappings add `content.text` only for events participating in `Chat.Message`; event class, origin, start time, and normalized content form the complete Event.Hash input
- events without another reliable semantic projection omit `content`; changes visible only in provider-native evidence do not amend the Normal Event
- `Event.Hash` excludes address, observations/provenance, annotations, raw-model version, and optional raw evidence
- raw identifiers never need a generic stripping heuristic because raw provider objects are no longer hash inputs
- `Chat.Message.Hash` remains side plus ordered member Event.Hash values, so a normalized message-text amendment still produces `AMENDED`

### Optional normalizer raw evidence

- every normalizer accepts an `include_raw` choice, defaulting to false
- when false, no native `record` remains on an event and the assembled model has no `raw` member
- when true, the normalizer may return any JSON-compatible diagnostic evidence in `NormalFragment.raw`; current Codex and Claude normalizers return the native records they used
- assembly places returned evidence under one top-level `raw` list with a minimal source envelope: source id, recognized raw-model version, and normalizer-owned value
- the presence, absence, or shape of raw evidence cannot change events, annotations, addresses, hashes, ordering, or reference standing
- source references on event observations remain the durable route back to the authoritative archive

### Public inspection and model revision

- `build_normal_model` and `build_normal_model_from_row` expose `include_raw=False`
- `tarav chatlas2 normalize --include-raw` requests diagnostic evidence; message and Anchory consumers keep the default compact model
- advance the experimental Normal Model schema from v4 to v5 because event shape and hash semantics change
- simplify conformance checks to use the existing provider-neutral `Chat.Message.text` projection instead of decoding event-native records
- update maintained Chatlas2 guidance and exports only where the public contract changes

### Canonical Tarav live-surface command

- replace `agentos stdlib prefix` with `tarav stdlib prefix` in the canonical `tarav-live-surfaces` Skillware source
- rebuild the managed `SKILL.md` and run the package Skillware check
- do not reinterpret other historical prose or broaden this slice into a repository-wide naming migration

## Execution.Plan

### Vertical.Slice 1 - Hash contract and compact default model

- add RED boundary tests proving raw-only differences do not affect Event.Hash, normalized content amendments do, and default Codex/Claude events expose no native record/raw payload
- introduce normalized event content for `Chat.Message` members and compute Event.Hash only from the selected normal fields
- remove the obsolete native-identifier filtering hash path and update current-state tests to assert normalized projections
- check: event-ref plus Codex and Claude pipeline tests
- status: pending

### Vertical.Slice 2 - Optional fragment raw evidence

- add RED tests proving `include_raw=True` produces source-associated normalizer evidence while default/raw-enriched addresses, hashes, messages, and contexts remain identical
- add the optional `NormalFragment.raw` channel, pass the option through assembly and both Claude mapping families plus Codex, and expose `--include-raw` on normalize
- update corpus consumers to remain entirely on provider-neutral Normal Model fields
- check: focused pipeline, CLI, corpus, message, and Anchory tests
- status: pending

### Vertical.Slice 3 - Guidance, Skillware correction, and system verification

- update `tarav-py/AGENTS.md` and `ARCHITECTURE.md` for Normal Model v5 and the raw-evidence boundary
- change the live-surface `.skw.md` source, rebuild it, and verify the generated target uses only `tarav stdlib prefix`
- ground the execution gate after the new hash semantics are active so its stored Chat.Message.Ref is current rather than knowingly amended by this implementation
- run all Chatlas2 tests, corpus verification/check, architecture checks, focused Ruff, Skillware checks, and `git diff --check`; run broader repository tests proportionate to the result
- status: pending

## Impl.Log

- **2026-08-16 — design decision:** optional raw material belongs to a normalizer-owned fragment evidence channel, not to Normal Events; no normalizer is required to inspect a complete artifact
- **2026-08-16 — hash decision:** Event.Hash covers only class, origin, start time, and deliberately projected provider-neutral event content; optional raw evidence is identity-inert
- **2026-08-16 — naming correction:** the user corrected an inverted migration assumption: `tarav` is canonical and `agentos` is deprecated; the stale live-surface skill wording is included in scope
- **2026-08-16 — grounding timing:** the execution-gate Chat.Message address is known, but its current hash uses the superseded Event.Hash recipe; mint the durable support anchor after the new hash implementation rather than manufacturing an immediately amended assertion
