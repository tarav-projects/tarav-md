"""Read the Index.Line type tournament: did the registered type rank on top?

The engine records orderings and nothing else; every question below is a fold
over them. Two readings come out of the same verdicts and are deliberately kept
apart, because one match can never separate them:

- **per type** — a code that keeps losing across many lines indicts the *type's
  definition*, not those lines.
- **per line** — a line that loses while its own code wins elsewhere indicts
  *that line's typing*.

Rank is reported as a distribution rather than a win rate. Many index lines
legitimately fit two codes, so "was the registered type in the top two" is the
honest question and "did it win" overstates failure.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict

from agentos.tournament import TournamentStore


def fold(store: TournamentStore, tournament_id: str) -> dict[str, object]:
    verdicts = store.verdicts(tournament_id)

    ranks: list[int] = []
    per_type: dict[str, list[int]] = defaultdict(list)
    per_type_lines: dict[str, set[str]] = defaultdict(set)
    per_line: dict[str, list[int]] = defaultdict(list)
    winners: Counter[str] = Counter()
    beaten_by: Counter[tuple[str, str]] = Counter()
    refusals: list[str] = []
    arity = 0

    for verdict in verdicts:
        slot = verdict.slot or {}
        line = str(slot.get("line") or "?")
        registered = str(slot.get("registered") or "?")
        if verdict.outcome != "ordered":
            refusals.append(str(verdict.envelope.get("refusal_reason") or ""))
            continue
        ordering = verdict.ordering or ()
        arity = max(arity, len(ordering))
        codes = [player.split("@")[1] for player in ordering]
        if registered not in codes:
            continue
        rank = codes.index(registered) + 1
        ranks.append(rank)
        per_type[registered].append(rank)
        per_type_lines[registered].add(line)
        per_line[line].append(rank)
        winners[codes[0]] += 1
        if rank != 1:
            beaten_by[(registered, codes[0])] += 1

    return {
        "tournament_id": tournament_id,
        "verdicts": len(verdicts),
        "ordered": len(ranks),
        "no_contest": len(refusals),
        "arity": arity,
        "rank_histogram": dict(sorted(Counter(ranks).items())),
        "top1_rate": _rate(ranks, 1),
        "top2_rate": _rate(ranks, 2),
        "mean_rank": round(sum(ranks) / len(ranks), 2) if ranks else None,
        "chance_top1": round(1 / arity, 3) if arity else None,
        "chance_top2": round(2 / arity, 3) if arity else None,
        "by_registered_type": {
            code: {
                # Verdicts and lines are different denominators and were easy to
                # confuse: repeat runs accumulate against one line, so a type with
                # many verdicts may rest on very few lines.
                "verdicts": len(values),
                "lines": len(per_type_lines[code]),
                "top1_rate": _rate(values, 1),
                "top2_rate": _rate(values, 2),
                "mean_rank": round(sum(values) / len(values), 2),
            }
            for code, values in sorted(per_type.items())
        },
        "weak_lines": [
            {"line": line, "ranks": values}
            for line, values in sorted(per_line.items())
            if min(values) >= 3
        ],
        "winning_codes": dict(winners.most_common()),
        "beaten_by": {
            f"{registered}->{winner}": count
            for (registered, winner), count in beaten_by.most_common()
        },
        "refusal_samples": refusals[:5],
    }


def _rate(values: list[int], cutoff: int) -> float | None:
    if not values:
        return None
    return round(sum(1 for value in values if value <= cutoff) / len(values), 3)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tournament", required=True)
    parser.add_argument("--depot")
    args = parser.parse_args()
    store = TournamentStore(args.depot)
    print(json.dumps(fold(store, args.tournament), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
