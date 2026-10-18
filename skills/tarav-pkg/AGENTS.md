# SKW maintenance

This package is a typed `SkwSkill`; `.skw/main.json` declares its sources and
consumer files. Markdown products are compiled from `.skw/src/`.

Edit the corresponding `.skw.json` source and compile it rather than editing
the Markdown product directly. The Constitution and skill entry point have
separate section blocks; the skill's frontmatter is its own block. Other
documents retain their imported literal blocks. `.skw/loading.json` declares
the reading graph: maintain its block references and the source blocks' reading
annotations when reorganizing sections. Do not invent generation history for
imported text. The Constitution still governs changes to its source and product.

From this directory:

```sh
tarav skw skills ls --limit 5
tarav skw skills ls --source SKILL.skw.json
tarav skw skills read --source SKILL.skw.json --block introduction
tarav skw skills build
tarav skw skills check
```

`AGENTS.md` is developer guidance, not a deployed consumer file.
