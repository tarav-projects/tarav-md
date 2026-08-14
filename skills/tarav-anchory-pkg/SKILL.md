---
name: tarav-anchory-pkg
description: "Universal anchor literacy for the Anchory subsystem. USE WHEN encountering a ^-anchor citation on any surface and needing to resolve it, when registering new anchors, or when working with anchory depots, namespaces, or the depot registry."
---

# Agentos Anchory

Depot-scoped stable anchor dictionaries. An anchor is a small stable key (`^c20260718-4u`) standing for an application-defined relationship or context — a support set, an Index line dossier, a document location, any addressable subject — with an application-owned JSON record behind it.

This is a CLI-first surface: use the installed `agentos anchory` commands directly.

## The Key Grammar

```text
^c20260718-4u
 │└───┬───┘│└─ tag: optional single letter, a caller-declared kind mark
 │ alloc-  └── counter: allocated by anchory, the identity spine
 │ prefix (caller convention; chatlas uses the YYYYMMDD date)
 └─ namespace prefix: one letter declared in the namespace's meta.json
```

- the caller supplies **meaning** (namespace, alloc-prefix, tag, hint, record); anchory supplies **identity** (the counter) and composes the key
- the tag never participates in allocation — `-4u` and `-5a` coexist, `-4` and `-4u` cannot both be allocated
- Chatlas currently uses `u` as a user-evidence tag. It describes the application record convention, not one singular target turn: a line dossier may contain several support members plus independent gate and provenance relationships
- bare citations (`^20260718-4`, no namespace letter) are banned on written surfaces; the index linter flags them (`Index.Linter/Anchor.Unprefixed`)

## Following an Anchor (no depot knowledge needed)

```sh
agentos anchory resolve --anchor c20260718-4u
```

Without `--depot` this runs `Pwd.Upward.Search`: registered depots nearest the working directory first, then the global depot (`~/.agentos/anchory/depot`). Every depot a command touches auto-registers in `~/.agentos/anchory/registry.json`.

- a mistagged citation still resolves: the output carries `tag_mismatch: true` and the stored key — the citation disagrees with the application's tag convention, but the record is real
- add `--meta` to include the namespace's `meta.json` (its intention text is the fallback context when you do not know what the namespace's anchors mean)
- for a Chatlas anchor, use the application resolver to validate its record and optionally recover exact member turns or neighborhoods:

  ```sh
  agentos chatlas anchory resolve c20260718-4u --detail context --radius 4
  ```

- a current Index-line anchor resolves to `chatlas.line-anchor-dossier.v1`: `attachment.triplet_hash` asserts the attached `Line.Type + body + Anchor.Id`, while `relationships.support`, `relationships.gates`, and `relationships.provenance` remain independently typed

## Registering

Through an owning application when one exists (preferred — it validates and derives the application record). Register a generic Chatlas support set with exact user-turn members and a hint:

```sh
agentos chatlas anchory register \
  --member <identity-hash>:<turn-id> \
  --hint "one sentence"
```

Register an Index-line dossier by supplying the canonical line content; repeat `--member` in relevance order and add `--gates` when review relationships apply:

```sh
agentos chatlas anchory register \
  --line-content '- [CT] <Index line body>' \
  --member <identity-hash>:<turn-id>
```

Raw, against an explicit depot:

```sh
agentos anchory register --depot <root> --namespace <ns> \
  --alloc-prefix 20260718 --tag u \
  --record-json '{"hint": "one sentence", ...}'
```

A named namespace needs its meta before allocation:

```sh
agentos anchory namespace set --depot <root> --namespace <ns> \
  --prefix <letter> --intention "what these anchors mean"
```

## Maintenance

- `agentos anchory amend --depot <root> --anchor <key> --record-json '{...}'` — records are amendable and there is no delete; the owning application defines and validates which amendments preserve the anchor's meaning
- `agentos anchory check --depot <root>` — structural check; tag-less keys in a prefixed namespace are warnings (an amendable backlog, not an error)
- `agentos anchory query --depot <root> [--namespace <ns>] [--prefix <text>]` — enumerate
- `agentos anchory scan --depot <root> --src-file <file> --regex <re>` — extract and resolve citations from a text file, read-only

## Ownership Split

Anchory owns persistence, locking, allocation, resolution, and the registry. Applications own record meaning, alloc-prefix conventions, tag alphabets, and their depot's git lifecycle. See `Anchory.System` in the tarav-pkg index for the design.
