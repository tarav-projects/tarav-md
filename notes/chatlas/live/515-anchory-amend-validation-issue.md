# `anchory amend` Silently Breaks Chatlas Support Sets — issue

## Session.Abstract

- **Type:** Issue / gap report — `agentos anchory amend` accepts records that `agentos chatlas anchory register` would never produce, and nothing catches it until resolve time.
- **Intent:** Correcting an anchor's hint is a sanctioned, routine act. Today the only way to do it silently corrupts the record unless the caller happens to reproduce fields they were never asked for.
- **State:** Resolved — application-owned validation now runs inside atomic generic amendment; implementation record: note 516.
- **Scope:** the `anchory amend` CLI surface and chatlas-side record validation. NOT the anchor model, not `Support.Set` semantics.
- **Found by:** an agendix capture pass in `g70203-md`, correcting five hints written as `"probe"` during registration.

## Motivation

`references/link.md` establishes both that the hint matters and that amending it is legitimate:

> "the hint is the desync tripwire: write it so a reader can tell whether the
> resolved neighborhood matches"

> "`agentos anchory amend` exists only to correct an error or improve
> resolution of the same context"

So "fix a bad hint on an anchor whose members are correct" is exactly the supported case. It cannot currently be done safely.

## Evidence

Three facts, each reproduced directly.

**1. There is no hint-level amend.** `amend` takes only `--depot`, `--namespace`, `--anchor`, and a mutually exclusive `--record-json` / `--record-file`. Correcting one string requires restating the whole record:

```
$ agentos anchory amend --depot … --anchor c20260730-4u --hint "…"
error: one of the arguments --record-json --record-file is required
```

**2. `amend` accepts a record `register` would have rejected or completed.** `chatlas anchory register` fills each member's `at` itself — the caller never supplies it and has no reason to know it is mandatory. A hand-written replacement record therefore omits it, and `amend` takes it without complaint:

```
$ agentos anchory amend --depot ~/Documents/chatlas/anchory --anchor c20260730-13u \
    --record-json '{"app":"chatlas","schema":"chatlas.support-set.v2","hint":"corrected hint",
                    "members":[{"session":"<hash>","turn_id":"<turn>"}]}'
"anchor": "c20260730-13u"          # accepted
```

The same asymmetry applies to a *wrong* `at`: supplying a plausible-but-incorrect timestamp (registration time rather than the turn's event time) is also accepted.

**3. Nothing notices until someone reads the anchor.** The depot's own checker passes:

```
$ agentos anchory check --depot ~/Documents/chatlas/anchory
"error_count": 0, "warning_count": 0
```

The breakage surfaces only at resolve:

```
$ agentos chatlas anchory resolve c20260730-13u --radius 0
error: chatlas support-set member 0 requires non-empty 'at'
```

and, with a wrong-but-present timestamp:

```
error: chatlas support-set member 0 timestamp mismatch for <hash>:<turn>:
       record='2026-07-30T20:53:39.646Z', event='2026-07-30T10:52:54.531Z'
```

Between the amend and the next resolve, the anchor is live on an index surface and looks fine. In this case five anchors on a freshly landed agendix were broken and only caught because the index linter resolves anchors.

**Conclusion:** the write path validates less than the read path. `amend` is a raw record overwrite with no knowledge of the chatlas schema it is overwriting, while `register` and `resolve` both understand it.

## Silver lining worth keeping

The resolve error is genuinely good: it names the member, the recorded value, and the true value. Recovery was possible only because of that message. Whatever the fix, that diagnostic should survive.

## Resolution

`AnchoryDepot.amend` now accepts an application validator that runs under the mutation lock with the current and proposed records. The generic command registrar carries that hook, `agentos-cli` injects Chatlas's implementation, and Chatlas rejects both unresolvable replacements and changes to ordered member identity or typed roles before anything is written.

A corrected `hint` succeeds when support meaning and live resolution remain valid. A missing or wrong `at`, changed member, reordered set, or changed `types` fails at amend time and leaves the current record intact.

## Remaining proposals

These improve ergonomics or depot-wide detection; they are no longer required to close the write-path validation hole.

- **A field-level amend.** `agentos anchory amend --anchor X --hint "…"` — read-modify-write the existing record, touching only the named field. This is the common case and removes the class of error entirely.
- **Chatlas-side amend.** `agentos chatlas anchory amend`, symmetric with `chatlas anchory register`: it knows the schema, can re-derive `at` from the turn, and keeps callers out of raw record JSON — the same reason `register` exists at that level.
- **Make `anchory check` resolve-aware**, so a corrupted record is caught by a depot sweep rather than by whoever reads the anchor next.

## Non-goals

- Not changing `at`'s status. It is documented as "readability or ordering data, never registration key", and that stays true — but it is *validated*, so a write path that lets callers get it wrong is a footgun regardless of its semantic weight.
- Not relaxing resolve's strictness. The strictness is the feature; the write path should match it.

## Open questions

- Should a future field-level or Chatlas-side amend derive `at`, making it optional on that higher-level input? Raw record replacement intentionally remains complete-record input.
- Should `anchory check` resolve every anchor by default, or behind a flag, given the cost on a large depot?

## Housekeeping

This investigation minted throwaway anchors in the chatlas depot that carry no index reference and should be retired if a retirement path exists: `c20260730-9u` and `c20260730-11u` … `c20260730-13u` (hints `repro single`, `repro two`, `repro three`, `repro colon`, `corrected hint`). `c20260730-13u` is currently left deliberately broken as a live reproduction; repair or drop it once this is designed. There is no `anchory` delete or retire subcommand today — possibly its own gap.

## Not filed: multi-member register

An earlier failure in the same session — `chatlas anchory register` rejecting repeated `--member` with
`error: chatlas anchory --member must have the form <session-identity>:<turn-id>` while each member registered fine alone — **could not be reproduced afterward**. Two- and three-member registrations both succeed. Recorded here only so the observation is not lost; it is not a claim.
