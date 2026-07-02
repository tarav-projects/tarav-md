****

## Field.Scoped.Precedence

- `Field.Scoped.Precedence` is precedence lookup addressed by a `Normal.Model.Namespace` path — a normalizer asks how one field was normalized before, rather than comparing whole documents
- the namespace makes it possible — every datum has a canonical path, so a field's prior values are collectable across all previously normalized instances
- it narrows precedence to the decision at hand — a field's own history is the tightest `Specified.By.Precedence` reference for normalizing that field again
- relatedness composes with the path — prior values from instances sharing identifying context are the weightiest precedent for the same field

****

## Normal.Amendment.Precedence

- `Normal.Amendment.Precedence` is treating post-normalization edits to a normal file as precedent, alongside the original `raw → Model.Fragment` mapping
- the initial fragment records how a normalizer first read the raw; a later amendment records a decision that corrected or refined that reading
- amendments carry approved intent — a value changed after review is stronger evidence of the wanted normal form than the first pass
- field-scoped precedence therefore reads two signals — how raw was mapped, and how that mapping was later revised

****

## Version.History.Precedence.Store

- `Version.History.Precedence.Store` is the version history of the normal files serving as the precedence corpus a normalizer searches
- both precedent signals live there — the commit that first wrote a field and every later amendment to its value are recoverable by path from `git`
- it needs no separate store — because the normal files are versioned and namespace-addressed, precedence is a query over history, not a maintained side index
- it is a read surface for `Field.Scoped.Precedence` — the store holds the values; the field path and relatedness select which ones matter
