#!/usr/bin/env python3
"""Probe the Chatlas raw archive for a native session concept and emit a `seen:` line.

The output is the hard-evidence pointer used by Session.Model.Map records:
a `<commit>/<file>:<line>` reference, a trimmed real record, and the corpus count.
Artifacts are the truth; this script just makes the reference format correct every time.

Usage:
    probe-archive.py <provider> <pattern> [--archive ROOT] [--max-scan N]

    <provider>   archive subdir, e.g. claude-code, codex, copilot-cli
    <pattern>    a substring to match per JSONL line, e.g. '"type":"attachment"'
                 or '"subtype":"compact_boundary"'

Examples:
    probe-archive.py claude-code '"type":"attachment"'
    probe-archive.py codex '"exec_command_end"'

Output is a ready-to-paste map record stub. Verify any reference with:
    git -C ~/Documents/chatlas show <commit>:<file> | sed -n '<line>p'
"""
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


def short_commit(root: Path) -> str:
    try:
        out = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, check=True,
        )
        return out.stdout.strip()
    except Exception:
        return "UNKNOWN"


def trunc(o, _depth=0):
    """Shrink a record for display: clip strings, summarize content arrays to block types."""
    if isinstance(o, str):
        return o[:50] + ("…" if len(o) > 50 else "")
    if isinstance(o, list):
        if o and isinstance(o[0], dict) and "type" in o[0]:
            return [f"<{i.get('type')}>" for i in o]
        return [trunc(x, _depth + 1) for x in o[:3]]
    if isinstance(o, dict):
        return {k: trunc(v, _depth + 1) for k, v in o.items()}
    return o


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("provider")
    ap.add_argument("pattern")
    ap.add_argument("--archive", default=os.path.expanduser("~/Documents/chatlas"))
    ap.add_argument("--max-scan", type=int, default=0, help="0 = full corpus (exact count)")
    args = ap.parse_args()

    root = Path(args.archive)
    provider_dir = root / "raw" / args.provider
    if not provider_dir.is_dir():
        print(f"error: no archive at {provider_dir}", file=sys.stderr)
        return 2

    commit = short_commit(root)
    files = sorted(provider_dir.rglob("*.jsonl"))
    total = len(files)

    hits = 0
    first = None  # (relpath, line_no, record_obj_or_rawline)
    for n, f in enumerate(files):
        if args.max_scan and n >= args.max_scan:
            break
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if args.pattern not in text:
            continue
        hits += 1
        if first is None:
            for i, line in enumerate(text.splitlines(), start=1):
                if args.pattern in line:
                    rel = f.relative_to(root).as_posix()
                    try:
                        first = (rel, i, json.loads(line))
                    except Exception:
                        first = (rel, i, line[:300])
                    break

    scanned = total if not args.max_scan else min(args.max_scan, total)
    scope = f"{hits}/{total}" if not args.max_scan else f"{hits}/{scanned} scanned (of {total})"

    print(f"# probe: provider={args.provider} pattern={args.pattern!r}")
    print(f"# archive commit: {commit}   present in {scope} sessions")
    if first is None:
        print("# ABSENT — record under '# Absent in dataset' with this probe as evidence:")
        print(f"#   `grep -rl '{args.pattern}' ~/Documents/chatlas/raw/{args.provider}` -> 0")
        return 0

    rel, line_no, rec = first
    shown = json.dumps(trunc(rec), ensure_ascii=False) if isinstance(rec, (dict, list)) else str(rec)
    if len(shown) > 700:
        shown = shown[:700] + "…"
    print()
    print("- seen: `{commit}/{rel}:{ln}` → `{rec}`. Present in {scope} sessions".format(
        commit=commit, rel=rel, ln=line_no, rec=shown, scope=scope))
    print("- native: <meaning — harness source file:line>")
    print("- neutral: `TBD: <candidate>`")
    print("- rationale: <what the artifact reveals; current normalizer behavior; the pressure>")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
