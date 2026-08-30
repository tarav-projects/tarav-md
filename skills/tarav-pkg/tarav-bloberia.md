# Tarav.Bloberia

This document describes the current candidate design of `Tarav.Bloberia`.
It is subordinate to the Tarav Constitution and remains amendable.

## Purpose

`Tarav.Bloberia` is a global, low-commitment JSON registry managed by Agents.
It is a place for Agents and workflows to retain useful material without first
creating a Diagram model, defining a mechanical schema, or attaching the
material to another Tarav object.

Typical uses resemble live notes: retaining observations, workflow state, and
findability material so an Agent can search for and reuse them later.

This material is useful without being trusted contextualization. A Bloberia
record is not a Diagram Annotation, is not automatically grounded or Asserted,
and gains no authority merely from being stored.

## Record contract

Tarav.Bloberia stores arbitrary JSON exactly as supplied. It adds no envelope,
identifier, timestamp, or other field. No key or value is mechanically
privileged, and duplicate or contradictory records may coexist.

Skills and consumers may establish their own record conventions. If code begins
depending on such a convention, that data has graduated into a mechanical
schema owned by that consumer; it does not become a universal Bloberia schema.

`Agent.Hint` names one workflow that uses Tarav.Bloberia:

> Store useful JSON about other things so Agents can find and reuse it later.

`Agent.Hint` is not a Bloberia record type. A workflow may choose fields that
improve its own findability, including an identifier when it needs one.

Querying performs case-insensitive text matching over each complete JSON value.
Results are candidates for Agent interpretation. They do not imply authority,
correctness, grounding, uniqueness, or semantic agreement.

## Storage

The default root is `~/Documents/tarav/bloberia/`. It is an independent Git
repository inside Tarav's physical data root.

Tarav.Bloberia hosts the generic `tarav.bloberia` record-depot primitive.
Bloberia owns locking, JSON durability, private physical placement, and Git
checkpointing. Consumers must not depend on its physical filenames or layout.

The repository contains a small `bloberia.json` host definition, Bloberia's
storage metadata, and privately placed records. Git provides inspectable
history without adding semantics to the stored JSON.

## CLI

```text
tarav tarav2 bloberia init [--bloberia <root>]
tarav tarav2 bloberia write (--record-json <json> | --record-file <file>) [--bloberia <root>]
tarav tarav2 bloberia query [--text <text>] [--bloberia <root>]
```

`write` initializes a missing root as a convenience. `query` without `--text`
returns every record. The CLI emits JSON for reuse by Agent workflows.
