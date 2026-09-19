# Skillware development

Navigate without expanding context targets:

```sh
tarav skw skills ls --limit 5
tarav skw skills ls --source SKILL.skw.json --limit 5
tarav skw skills read --source SKILL.skw.json --block routing
```

Listings return `next_offset`; pass it as `--offset` for the next page.
`read` returns only the selected retained block and its source/product paths.
Use the existing document context commands below to follow its references.

Package checks emit bounded POI reports with class source paths. Use
`tarav skw skills poi --id <finding-id>` to inspect evidence, then decide
whether the current workflow should address it. Blessing is an explicit
recorded action, permitted only by the finding's class, stored under
`.skw/blessings/`. It does not remove the finding or change a check into a pass.

`.skw/loading.json` owns the declared consumer loading model. Nodes reference
source blocks; most within-file parents default to the predecessor. Cross-file
parents and consumer requirements are explicit. Keep the first metadata block
as the entry root. Link slots such as `{{skw:link-0}}` compile from declared
primitives; do not replace them with authored Markdown links.

Inspect one block without dumping the whole graph:

```sh
tarav skw skills context --block skill.routing --limit 2
```

Package checks report loading-path findings as well as document checks. Three
existing links to `tarav-pkg` remain unannotated external context and surface
`unannotated-output-link`; they do not silently satisfy block requirements.
The existing external package dependency remains declared. Adding cross-skill
block bindings requires an explicit modeling step, not output-link inference.

`.skw/main.json` is the typed directory-record entry declaring the skill,
its source/product files, and
developer/consumer dependencies. From this directory, use:

```sh
tarav skw skills check
tarav skw skills build
tarav skw skills deploy --destination /absolute/path/to/new-skill-directory
```

Deployment copies consumer files only and reports external skill dependencies.
Install those skills alongside this one; deployment does not copy them.
Package checks currently inspect inline Markdown file links, not fragments,
reference-style links, or prose mentions. Source context entries remain
developer context; dependency purposes do not replace their semantic roles.

`SKILL.md` and the Markdown files under `references/` are compiled products.
Their source Records are under `.skw/src/`, mirroring the product paths with
the `.skw.json` suffix. Edit retained block `output` lines in those sources.
Do not edit compiled Markdown as a substitute for editing its source.

From this skill directory:

```sh
tarav skw document context --source SKILL.skw.json --block routing
tarav skw document lint --source SKILL.skw.json
tarav skw document compile --source SKILL.skw.json
```

Context entries describe what a maintainer should consult. Relative reference
paths are relative to the containing source JSON, not to the product Markdown.
Existing Markdown links remain relative to their compiled products.

Read context and investigate findings before accepting a new baseline. Use
`tarav skw document observe-context --source <source> --block <block>` explicitly after review.
It records an observation, not a claim that a generation happened.
For a tracked generation, use `prepare --source <source> --block <block>`, edit source output,
then `record --source <source> --generation <generation-id>` and compile. Preparation exposes the
current output alongside its context. Empty prompt arrays are intentional for
imported sections whose maintenance guidance lives in context.

The original content was imported byte-for-byte. No original generation
history was invented. `.skw/lock.json` tracks compilation and context baselines.
Linting and compilation never accept changed context automatically.

Changes to dependencies may affect several sources. Lint each source under
`.skw/src/` after changes; review related sections and compile edited documents.
The runtime skill remains self-contained through its explicit Markdown links;
the `.skw` source is its development surface, not required runtime context.

CLI project selection: pass `--project <directory-containing-.skw>` or run
inside the project and let the CLI discover the nearest `.skw/` upward.
`--source` is relative to `.skw/src/`; absolute and escaping source paths are
rejected. Output paths remain project-relative, and context reference paths
remain relative to their containing source. All CLI inputs use named flags.
