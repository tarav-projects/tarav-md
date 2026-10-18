# SKW maintenance

This folder is the depot of the `skills/tarav-pkg` skill, a typed `SkwSkill`:
`main.json` declares its `skill_id`, its `product` folder, its sources and
consumer files. Markdown products are compiled from `src/`. The skill folder
keeps only the product and `.tarav/skill.json`, the skill's UUID.

Edit the corresponding `.skw.json` source and compile it rather than editing
the Markdown product directly. The Constitution and skill entry point have
separate section blocks; the skill's frontmatter is its own block. Other
documents retain their imported literal blocks. `loading.json` declares
the reading graph: maintain its block references and the source blocks' reading
annotations when reorganizing sections. Do not invent generation history for
imported text. The Constitution still governs changes to its source and product.

From the Project root:

```sh
tarav skw skills ls --skill skills/tarav-pkg --limit 5
tarav skw skills ls --skill skills/tarav-pkg --source SKILL.skw.json
tarav skw skills read --skill skills/tarav-pkg --source SKILL.skw.json --block introduction
tarav skw skills build --skill skills/tarav-pkg
tarav skw skills check --skill skills/tarav-pkg
```

`AGENTS.md` is developer guidance, not a deployed consumer file.
