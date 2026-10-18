# Skillware development

<!-- tarav.sessions
1f561f5d = codex:01a0b984-4664-7871-934a-89cf92595b64 @1f561f5d8db849a3a445b83a91a5e94acbb80927f9c332d45322ac70f8705a74
-->

This folder is the depot of the `skills/tarav-hugentics` skill: tarav-md
builds it. The skill folder keeps only the product and `.tarav/skill.json`,
the skill's UUID, which `main.json` names as `skill_id`. Run the commands below
from the Project root.

Navigate without expanding context targets:

```sh
tarav skw skills ls --skill skills/tarav-hugentics --limit 5
tarav skw skills ls --skill skills/tarav-hugentics --source SKILL.skw.json --limit 5
tarav skw skills read --skill skills/tarav-hugentics --source SKILL.skw.json --block routing
```

Listings return `next_offset`; pass it as `--offset` for the next page.
`read` returns only the selected retained block and its source/product paths.
Use the existing document context commands below to follow its references.

Package checks emit bounded POI reports with class source paths. Use
`tarav skw skills poi --skill skills/tarav-hugentics --id <finding-id>` to
inspect evidence, then decide whether the current workflow should address it.
Blessing is an explicit operator exit on the finding's action in tarav-md
(`tarav action list --project`), permitted only by the finding's class. It does
not remove the finding or change a check into a pass.

`loading.json` owns the declared consumer loading model. Nodes reference
source blocks; most within-file parents default to the predecessor. Cross-file
parents are explicit. Block `contains` declares output content claims,
`reading_deps` declares reader requirements, and `links` declares references.
Reading paths can also be derived from document position without a loading
file; this package retains one for its explicit cross-file routes.
Block `id` is a UUID Ship; its
separate `label` is the readable local selector. Keep the first metadata block
as the entry root. A link is written in the block's text as ordinary Markdown
and declared beside it; the reading graph uses only the declaration. A
declaration with `"prose": {"type": "Tarav.SKW.Reading.MarkdownProse"}` is
checked against the text and raises `Tarav.SKW.POI.MissingMarkdownLink` when the
text lacks it; declare that part on every link you write. Typed `SkillLink`
blocks retain produced Markdown in `output` and declare their own target;
refresh one explicitly with `tarav skw document produce --source SKILL.skw.json
--depot .tarav/skillware/skills/tarav-hugentics --block design-impact-link`.
<!-- tarav.breadcrumb 3385f03b3e0f -->
<!-- tarav.breadcrumb a2993b23b3ca -->
<!-- tarav.breadcrumb 6e446d50cb88 -->

Inspect one block without dumping the whole graph:

```sh
tarav skw skills context --skill skills/tarav-hugentics --block skill.routing --limit 2
```

Package checks report loading-path findings as well as document checks. The
links to `tarav-pkg` are written in the text without a declaration: a link can
only declare a target inside the package, so the graph does not know them and
they satisfy no block requirement. The external package dependency remains
declared. Adding cross-skill
block bindings requires an explicit modeling step, not output-link inference.
<!-- tarav.breadcrumb 578b5d7f39e8 -->

`main.json` is the typed directory-record entry declaring the skill (its
`skill_id` and `product` folder), its source/product files, and
developer/consumer dependencies. Use:

```sh
tarav skw skills check --skill skills/tarav-hugentics
tarav skw skills build --skill skills/tarav-hugentics
tarav skw skills deploy --skill skills/tarav-hugentics --destination /absolute/path/to/new-skill-directory
```

Deployment copies consumer files and `.tarav/skill.json`, so the copy is the
same skill, and reports external skill dependencies.
Install those skills alongside this one; deployment does not copy them.
Package checks currently inspect inline Markdown file links, not fragments,
reference-style links, or prose mentions. Source context entries remain
developer context; dependency purposes do not replace their semantic roles.

`SKILL.md` and the Markdown files under `references/` are compiled products.
Their source Records are under this depot's `src/`, mirroring the product paths with
the `.skw.json` suffix. Edit retained block `output` lines in those sources.
Do not edit compiled Markdown as a substitute for editing its source.

With `--depot .tarav/skillware/skills/tarav-hugentics` (written `D` here):

```sh
tarav skw document context --source SKILL.skw.json --depot D --block routing
tarav skw document lint --source SKILL.skw.json --depot D
tarav skw document compile --source SKILL.skw.json --depot D
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
history was invented. `lock.json` tracks compilation and context baselines.
Linting and compilation never accept changed context automatically.

Changes to dependencies may affect several sources. Lint each source under
`src/` after changes; review related sections and compile edited documents.
The runtime skill remains self-contained through its explicit Markdown links;
this depot is its development surface, not required runtime context.

CLI selection: `tarav skw skills` takes `--skill <skill-folder>`; `tarav skw
document` takes `--depot` relative to the Project, discovered upward from the
current directory or given with `--project`.
`--source` is relative to the depot's `src/`; absolute and escaping source paths are
rejected. Output paths remain project-relative, and context reference paths
remain relative to their containing source. All CLI inputs use named flags.
