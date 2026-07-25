# agentos-skillware --check

Report whether a skill's Skillware-managed surfaces still hold, and prescribe the response each POI demands. **Read-only** — this module never writes; acting on the report is a follow-up into `--dev`.

## The Pass

1. Run the CPU linter and take its output as given:

   ```
   agentos skw check --skill <path> [--json]
   ```

2. The output is a POI report: a once-per-kind legend, then bare rows — `[kind] target :: key (hash)`. A POI marks a place worth attention, nothing more: it may be wrong, and the linter is deliberately cheap — inspect before acting.
3. Prescribe per kind (below) — proposals, not actions.
4. Exit state: the command exits non-zero on any POI; a clean run is the quiet norm.

## POI Kinds

Gating — checked first, never blessable:

- `parse-error` — the src is below the `Parse.Floor`: malformed machinery or an unclosed construct; the file's other checks do not run until it is fixed, and files importing it go `unresolvable`
- `unresolvable` — a materializing dependency, `--dev-from`, `--cite`, or context-assembly claim does not resolve at its address; fix the address or restore the target

Per compiled file:

- `ok` — surface matches src, lock, and dependencies; nothing to do
- `never-built` — src exists but no lock entry; run `build`
- `stale-build` — the on-disk target matches the lock but a recompile differs (src moved); run `build`
- `hand-edited` — the on-disk target differs from the lock: someone edited the compiled surface; a judgment call — sometimes noise to rebuild over, sometimes content that belongs in src (move it, then rebuild)

Per recipe:

- `copy-drift` — a copy body no longer equals its target's expansion; mechanical: `build` repairs it
- `derived-stale` — a dependency changed since the derived body was written; **agentic**: real drift → re-derive in src; benign change → bless (below). The only blessable kind.

Dependency sync — the declared graph vs the compiled text, blessable when the mismatch is deliberate:

- `undeclared-dependency` — a mention resolves to a block but no dependency declares it; declare it (`depends --from`) or accept the mismatch by blessing
- `unhonored-dependency` — a declared `depends` target resolves but is not mentioned in the compiled text; drop the stale declaration or bless a deliberately-silent binding
- `dangling-dependency` — a declared `--from` target no longer resolves in the configured depots: a rename-without-alias or a retirement broke the binding; fix or remove the stale `--from`, restore an alias on the target, or bless if the reference is deliberately kept
- `uncited-dependency` — a `--cite` target is absent from the compiled surface; cite it explicitly, change the role, or bless the intentional mismatch
- `context-assembly-bypass` — a surface uses an assembly-claimed source through any dependency role without a companion `--dev-from` to the assembly; load the whole assembly or bless the intentional bypass

Housekeeping:

- `legacy-callout` — a v2 `[!skw]` callout line survives outside a fence; it is inert prose to the parser — rewrite it in the `$kw` grammar

The no-silent-blessing rule: a rebuild carries a stale derivation's old dependency hashes forward while its body is unchanged — `derived-stale` survives any number of builds and clears only through a re-derive or an explicit bless. Dependency targets are `Skw.Address.Schema` names.

## The Re-Derive Pass

For each `derived-stale` POI where the drift is real:

1. Open the src file; read the recipe's `--from` and `--dev-from` targets (current state), its citations, and its `--intent`.
2. Re-derive the body in src: the intent is the rule, the fresh targets are the inputs.
3. `agentos skw build`, then `check` — the body change re-blesses the dependency hashes; a clean run ends the pass.
4. For a gated package, the re-derived wording passes the package's edit gates before landing.

## The Bless Act

When the dependency change is benign — the current body already transforms the new state faithfully — accept it explicitly instead of editing around the flag:

`Poi.Unlock.Token` makes any configured read-before-bless workflow concrete:

```
agentos skw bless --skill <path> --poi <hash> \
  --unlock <token> [--unlock <token> ...]
```

- the hash comes from the check row; it binds to the exact current situation — if the dependency moves again, that is a new POI with a new hash
- when the POI kind has configured unlock requirements, `check` names every represented context surface and registry without disclosing tokens; read each whole surface, retrieve its registry token, and provide every receipt with repeatable `--unlock`
- one context surface has one token; several registry entries may name the same POI kind, making all of their receipts mandatory; a missing receipt refuses before any lock mutation and names only the missing surfaces
- token values live only in their provider registry; the source carries an addressed `--unlock-surface` annotation whose single `--from` points back to that registry, so rotation does not touch the surface
- a POI kind absent from the target package's configured `unlock_registries` retains ordinary blessing behavior, allowing incremental adoption
- bless rewrites that recipe's locked dependency hashes to current; body and target stay untouched; the lock diff is the audit record
- only `derived-stale` is blessable; blessing anything else is refused — parse errors are not in the language, mechanical kinds have mechanical fixes

## Boundary

- this module reports and prescribes; it never applies — `--dev` owns src edits, rebuilds, and blesses
- a drift POI has no predefined winner: source, derivation, or hand edit may each be the truth — resolution is case-by-case
