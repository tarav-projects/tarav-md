# Numbering Checks

Check obvious `File.Numbering.Protocol` issues in active numbered surfaces. Range definitions and reserved prefixes come from the index itself.

## Active Surfaces

Initial scope:

- `notes/index/`
- `notes/live/`
- `dev/live/`

Do not include archived or migrated evidence unless the check is explicitly about migration state.

## Deterministic Checks

For active surfaces:

- find files beginning with `NNN-` or reserved `NNN.` forms
- identify active files that are not numbered and not clearly reserved
- detect duplicate numeric prefixes within each active surface
- flag files that fall outside the expected ranges defined in `File.Numbering.Protocol`

## Agentic Checks

- Decide whether a duplicate belongs to active surface conflict or harmless legacy evidence.
- Treat transitional migration evidence carefully.

## Expected Findings

- `fail`: duplicate numeric prefixes identify different active files in the same active surface.
- `warn`: active files are unnumbered without a clear reserved-role reason.
- `warn`: active files appear outside expected ranges.
- `info`: numbering is partially migrated but intentionally transitional.
- `pass`: no obvious duplicate or range issues in active surfaces checked.
