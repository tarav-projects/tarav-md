# 645 - trackagents Depot -> Chatlas Migration Coverage (LIVE)

Status: live / open investigation
Date: 2026-08-31
Companion to: `644-the-tara-project-notes-inventory.md`
Question: **are the `trackagents` depot sessions present in Chatlas?**

Answer: **partially. 1554 of 2166 depot sessions are not indexed by Chatlas.
Of those, 313 Claude sessions exist NOWHERE ELSE — including all 83 Tara
Project monorepo sessions.**

---

## 0. Method

The Chatlas CLI has no list/query verb, so this used two passes:

1. **Index compare** — session IDs from
   `~/Documents/tarav/chatlas/index/sessions/*/*/sessions.index.jsonl`
   vs. session IDs harvested from the depot.
2. **CLI verification** — `tarav chatlas raw sources --session-id <id>` run
   against samples and against all 83 Tara sessions.

3. **Whole-root re-test** — session IDs harvested directly from
   `~/Documents/tarav/chatlas/raw/` (4.2 GB, the actual retention surface),
   then a literal `grep -rl <session-id>` over the entire Chatlas root.

All three agree. The CLI matched the index compare exactly (0 resolved / 40
missing on both a Claude sample and a Codex sample; 0/83 on the Tara set), and
the raw re-test reproduced every figure unchanged. This is CLI-confirmed and
raw-confirmed, not index-only inference.

### Why the third pass mattered

The first pass read only `index/`, which is a *derived* index — it could in
principle under-report what Chatlas retains. It does not:

| Chatlas subdir | Size | Files | Session IDs |
|---|---:|---:|---:|
| `raw/` | 4.2 G | 7744 | **7730** (5787 claude + 1943 codex) |
| `index/` | 13 M | 511 | **7733** |
| `session-models/` | 234 M | 70 | derived, keyed by identity_hash |
| `normal-model/` | 152 M | 120 | derived, keyed by identity_hash |
| `chatlas2/model-cache/` | 2.2 M | 12 | derived |
| `cache/` | 3.6 M | 9 | derived |

`raw` vs `index` differ by **2 ids in raw not indexed** and **5 indexed not in
raw** — noise. Union = **7735**. `session-models/`, `normal-model/`,
`chatlas2/`, and `cache/` are all *derived caches keyed by identity_hash*, so
they cannot contain a session absent from `raw`.

Re-testing the gap against the union changed nothing:

```
depot claude missing: 313   (unchanged)
depot codex  missing: 1241  (unchanged)
TARA missing:         83    (unchanged)
```

---

## 1. The depot

`~/Documents/workspaces/trackagents/depot/` — **3.0 GB**, 8 provider trees.

| Tree | Artifacts | A Chatlas provider? |
|---|---|---|
| `claude/` | 1082 sessions (40 project dirs) | yes (`claude-code`) |
| `codex-tk/` | 1161 rollouts | yes (`codex`) |
| `codex-jp/` | 104 rollouts | yes (`codex`) |
| `codex/` | 0 | yes (`codex`) |
| `copilot/` | 3620 session-state dirs | **NO** |
| `gemini/` | 543 files | **NO** |
| `openclaw/` | 8 jsonl | **NO** |
| `agents/` | skills, CLIs, hook-scripts (not sessions) | n/a |

Date span: **2025-11-06 → 2026-04-02**.

### Session-identity caveat

Depot Claude sessions appear in **two shapes**:

- `<project>/<uuid>.jsonl` — full transcript (857 ids)
- `<project>/<uuid>/subagents/*.jsonl` — **subagent transcripts only, parent
  transcript absent** (270 ids)

Union = **1082** distinct Claude session ids.

> **Correction to note 644.** I described the Tara monorepo as holding
> "164 Claude session transcripts". That count was `.jsonl` files, and those
> files are **subagent** transcripts. The correct figure is **83 parent
> sessions** (plus 2 in the vscode-puller project), whose **main transcripts
> are not in the depot** — only their 164 subagent transcripts are.

---

## 2. Chatlas current state

Root: `~/Documents/tarav/chatlas/`

```
index/sessions/claude-code/**   5790 records
index/sessions/codex/**         1948 records
                                ----
                                7738 records / 7733 distinct session ids
```

Configured sources (`~/.tarav/config.json` -> `chatlas.sources`) are **live
provider homes only**:

```
claude-code  ~/.claude          scannable: true
codex        ~/.codex           scannable: true
codex        ~/.codex-br        scannable: false
codex        ~/.codex-jp        scannable: false
codex        ~/.codex-mm        scannable: false
codex        ~/.codex-tk        scannable: false
```

**The trackagents depot is not a Chatlas source.** No `copilot`, `gemini`, or
`openclaw` provider exists in the config at all.

---

## 3. Coverage result

| Set | Depot | In Chatlas | Missing |
|---|---:|---:|---:|
| Claude | 1082 | 769 | **313** |
| Codex  | 1264 | 23 | **1241** |
| **Total (dedup)** | **2166** | **792** | **1554** |
| Copilot / Gemini / openclaw | 4171 | 0 | **4171** |

CLI verification samples: 40/40 Claude missing, 40/40 Codex missing — matches.

---

## 4. Where the gap actually lives — the decisive split

Cross-checking the gap against the **Archive.Attic chatlas deposit**
(`20260826T030536Z-chatlas`, uuid `d3d9c3bb-3f13-4058-b52b-29397fd72dab`),
which retains 9934 distinct session ids:

| Gap | Count | Recoverable from Attic | **Depot-only** |
|---|---:|---:|---:|
| Codex missing | 1241 | **1241 (100%)** | 0 |
| Claude missing | 313 | **0 (0%)** | **313** |

**This is the whole finding.**

- The **Codex gap is not data loss.** Those 1241 sessions were captured by the
  old Chatlas depot and conserved in the Attic. They are simply not in the
  *current* index, because `~/.codex-jp` and `~/.codex-tk` are now **empty
  (0 rollouts each)** while remaining `scannable: false` — the current Chatlas
  can never re-derive them.
- The **Claude gap is real and unique.** 313 sessions exist only in the
  trackagents depot. Not in Chatlas, not in the Attic, not in `~/.claude`.

### Depot-only Claude sessions by project (top 20 of 227 dir-form; 86 more in file-form)

```
  82  -Users-pereiro-Documents-js-taraproject-js-monorepo         <- THE TARA PROJECT
  68  -Users-pereiro--julia-dev-Simuleos
  18  -Users-pereiro-Library-Application-Support-CodexBar-ClaudeProbe
   8  -Users-pereiro--julia-dev-Auxotrophs-CoCultures-20251109
   8  -Users-pereiro-Documents-workspaces-20260206-simuleos
   6  -Users-pereiro-Documents-Obsidian-notebook
   5  -Users-pereiro-University-Teaching-...-Computacio-n-2025-SEM1-EXTRA
   4  -Users-pereiro--julia-dev-SDLProcessing
   3  -Users-pereiro-University-CODE-PaperSON
   3  -Users-pereiro--julia-dev-ContextBundler
   2  -Users-pereiro-University-CODE-Simuleos-workspace
   2  -Users-pereiro-projects-obacli
   2  -Users-pereiro-University-CODE-claude-playground
   2  -Users-pereiro-University-CODE-Meta
   1  -Users-pereiro-Documents-js-taraproject-js-monorepo-packages-vscode-tara-puller-extenssion
   1  -Users-pereiro--julia-dev
   1  -Users-pereiro--julia-dev-UXLayers
   1  -Users-pereiro--julia-dev-UXLayer
   1  -Users-pereiro--julia-dev-EColi-Coexistence-2024
   1  -Users-pereiro-University-CODE-Workflows-Notes
```

The two largest blocks are **The Tara Project** and **Simuleos** — precisely
the two predecessor systems traced in note 644.

---

## 5. The Tara Project sessions specifically

```
~/Documents/workspaces/trackagents/depot/claude/projects/
  -Users-pereiro-Documents-js-taraproject-js-monorepo/                  83 sessions
  -Users-pereiro-Documents-js-taraproject-js-monorepo-packages-
    vscode-tara-puller-extenssion/                                       2 sessions
```

Span **2026-01-12 → 2026-02-05** — exactly the window in which the
`notes-inbox/` / `notes-index/` flat layout existed and
`The.Tara.Project.Full.Stack.md` was last committed (`3371d94`, 2026-01-21).

CLI sweep over all 83:

```
CLI-resolved:  0
CLI-missing:  83
```

Example:

```
$ tarav chatlas raw sources --session-id 01a9d5f3-9e2e-4c2a-876a-785bef9d3bc5
error: no indexed Chatlas session matched the exact reference
```

### Literal grep over the whole Chatlas root

`grep -rl <session-id> ~/Documents/tarav/chatlas/` returns 1-3 hits per Tara
session id. **All are false positives** — the ids appear as text inside *other*
sessions' transcripts, never as session data:

- `raw/claude-code/.../-Users-pereiro-projects-taravangian-project/b2b9f038-...jsonl`
  — **this very investigation session**, capturing its own `ls` output.
- two `agentos` codex sessions (2026-04-20, 2026-05-12) that happened to have a
  directory listing of the depot in context during unrelated work.

No Tara session payload exists anywhere under the Chatlas root.

**Status: the source repo `~/Documents/js/taraproject-js-monorepo` is deleted,
these sessions are absent from Chatlas (index *and* raw) and from the Attic,
and only their subagent transcripts survive.** The parent transcripts are gone
everywhere.

---

## 6. Root causes

1. **Chatlas only scans live provider homes.** The depot is an out-of-band
   archive, so nothing in it is reachable by `tarav chatlas update`.
2. **`scannable: false` + emptied homes.** `~/.codex-jp` and `~/.codex-tk`
   hold 0 rollouts today. Their 1265 depot rollouts have no live source.
3. **Copilot / Gemini / openclaw are not modelled.** 4171 artifacts sit
   outside Chatlas's provider vocabulary entirely.
4. **The Attic deposit is broader than the current index.** It holds 2213 ids
   Chatlas does not (and only 12 the other way) — the Chatlas2 rebootstrap
   from "supported raw artifacts" narrowed the corpus.

---

## 7. Open threads

1. **Rescue the 313 depot-only Claude sessions** — they have no second copy.
   The 83 Tara + 68 Simuleos sessions are the historically significant core.
2. **Decide the depot's conservation status.** Per `attic.md`, a 3.0 GB
   disconnected archive with unique material is a textbook Archive.Attic
   Deposit. It currently has none.
3. **Reconcile Attic vs Chatlas.** 2213 ids live only in the Attic deposit.
   Run `chatlas-tarav-chatlas-retention-audit --provider codex` to decide
   whether they are retained, telemetry, or excluded.
4. **Decide on copilot/gemini/openclaw.** 4171 artifacts are outside the
   Normal Model. Either model them or explicitly exclude them.
5. **Missing parent transcripts.** Depot Claude sessions in `<uuid>/subagents/`
   form have no parent transcript. Determine whether that was a capture bug or
   deliberate, since it affects 270 sessions.

---

## 8. Reproduce

```bash
# chatlas indexed ids
cat ~/Documents/tarav/chatlas/index/sessions/*/*/sessions.index.jsonl \
  | python3 -c "import sys,json;print('\n'.join(sorted({json.loads(l)['session_id'] for l in sys.stdin if l.strip()})))" \
  > /tmp/chatlas_ids.txt

# depot claude ids (both shapes)
cd ~/Documents/workspaces/trackagents/depot
find claude -name "*.jsonl" | sed 's|.*/||;s|\.jsonl$||' | grep -E "^[0-9a-f-]{36}$" | sort -u  > /tmp/a
find claude/projects -mindepth 2 -maxdepth 2 -type d | sed 's|.*/||' | grep -E "^[0-9a-f-]{36}$" | sort -u >> /tmp/a
sort -u /tmp/a > /tmp/depot_claude_all.txt

# depot codex ids
find codex codex-jp codex-tk -name "rollout-*.jsonl" \
  | sed 's|.*/rollout-||;s|\.jsonl$||' \
  | sed -E 's/^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}-[0-9]{2}-[0-9]{2}-//' \
  | grep -E "^[0-9a-f-]{36}$" | sort -u > /tmp/depot_codex_ids.txt

# chatlas RAW ids (the actual retention surface, not the derived index)
cd ~/Documents/tarav/chatlas/raw
find claude-code -name "*.jsonl" | sed 's|.*/||;s|\.jsonl$||' \
  | grep -E "^[0-9a-f-]{36}$" | sort -u > /tmp/raw_claude.txt
find codex -name "rollout-*.jsonl" | sed 's|.*/rollout-||;s|\.jsonl$||' \
  | sed -E 's/^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}-[0-9]{2}-[0-9]{2}-//' \
  | grep -E "^[0-9a-f-]{36}$" | sort -u > /tmp/raw_codex.txt
cat /tmp/chatlas_ids.txt /tmp/raw_claude.txt /tmp/raw_codex.txt \
  | sort -u > /tmp/chatlas_full.txt      # 7735

# the gap
comm -23 /tmp/depot_claude_all.txt /tmp/chatlas_full.txt | wc -l   # 313
comm -23 /tmp/depot_codex_ids.txt  /tmp/chatlas_ids.txt | wc -l   # 1241

# CLI confirmation for one session
tarav chatlas raw sources --session-id 01a9d5f3-9e2e-4c2a-876a-785bef9d3bc5
```
