---
name: agentos-anchory-pkg
description: "Universal anchor literacy for the Anchory subsystem. USE WHEN encountering a ^-anchor citation on any surface and needing to resolve it, when registering new anchors, or when working with anchory depots, namespaces, or the depot registry."
---

# Agentos Anchory

Depot-scoped stable anchor dictionaries. An anchor is a small stable key (`^c20260718-4u`) standing for a context somewhere — a chat turn, a document location, any addressable moment — with a JSON record and a curator hint behind it.

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
- chatlas tags: `u` = user turn, `a` = assistant turn — a cheap double-check on the citation
- bare citations (`^20260718-4`, no namespace letter) are banned on written surfaces; the index linter flags them (`Index.Linter/Anchor.Unprefixed`)

## Following an Anchor (no depot knowledge needed)

```sh
agentos anchory resolve --anchor c20260718-4u
```

Without `--depot` this runs `Pwd.Upward.Search`: registered depots nearest the working directory first, then the global depot (`~/.agentos/anchory/depot`). Every depot a command touches auto-registers in `~/.agentos/anchory/registry.json`.

- a mistagged citation still resolves: the output carries `tag_mismatch: true` and the stored key — the citation lies about the turn kind, the record is real
- add `--meta` to include the namespace's `meta.json` (its intention text is the fallback context when you do not know what the namespace's anchors mean)
- chat anchors (`c…`) resolve to a session identity + timestamp; read the neighborhood with `agentos chatlas views inline --anchor <key>`

## Registering

Through an owning application when one exists (preferred — it derives everything):

```sh
agentos chatlas anchory register --session-id <id> --at <ISO-ts> --hint "one sentence"
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

- `agentos anchory amend --depot <root> --anchor <key> --record-json '{...}'` — records are amendable (there is no delete; void by amending the hint)
- `agentos anchory check --depot <root>` — structural check; tag-less keys in a prefixed namespace are warnings (an amendable backlog, not an error)
- `agentos anchory query --depot <root> [--namespace <ns>] [--prefix <text>]` — enumerate
- `agentos anchory scan --depot <root> --src-file <file> --regex <re>` — extract and resolve citations from a text file, read-only

## Ownership Split

Anchory owns persistence, locking, allocation, resolution, and the registry. Applications own record meaning, alloc-prefix conventions, tag alphabets, and their depot's git lifecycle. See `Anchory.System` in the agentos-pkg index for the design.

> $kw: --from Anchory.System
