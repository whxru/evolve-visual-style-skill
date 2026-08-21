#!/usr/bin/env python3
"""Aggregate strict candidate rankings with deterministic Borda scoring."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Aggregate multiple best-to-worst rankings from a JSON file."
    )
    parser.add_argument(
        "input",
        type=Path,
        help=(
            "JSON array of ranking arrays, or an object with a 'rankings' array; "
            "each ranking must contain the same unique candidate IDs"
        ),
    )
    return parser.parse_args()


def load_rankings(path: Path) -> list[list[str]]:
    try:
        payload: Any = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read valid JSON: {exc}") from exc

    rankings = payload.get("rankings") if isinstance(payload, dict) else payload
    if not isinstance(rankings, list) or not rankings:
        raise ValueError("rankings must be a non-empty array")
    if not all(isinstance(ranking, list) for ranking in rankings):
        raise ValueError("every ranking must be an array")
    if not all(
        isinstance(candidate_id, str) and candidate_id
        for ranking in rankings
        for candidate_id in ranking
    ):
        raise ValueError("candidate IDs must be non-empty strings")
    return rankings


def validate_rankings(rankings: list[list[str]]) -> list[str]:
    canonical = rankings[0]
    if not canonical:
        raise ValueError("rankings cannot be empty")
    if len(set(canonical)) != len(canonical):
        raise ValueError("the first ranking contains duplicate candidate IDs")
    expected = set(canonical)
    for index, ranking in enumerate(rankings, start=1):
        if len(ranking) != len(canonical):
            raise ValueError(f"ranking {index} has the wrong candidate count")
        if len(set(ranking)) != len(ranking):
            raise ValueError(f"ranking {index} contains duplicate candidate IDs")
        if set(ranking) != expected:
            missing = sorted(expected - set(ranking))
            unknown = sorted(set(ranking) - expected)
            raise ValueError(
                f"ranking {index} candidate mismatch; missing={missing}, unknown={unknown}"
            )
    return sorted(expected)


def aggregate(rankings: list[list[str]], candidate_ids: list[str]) -> dict[str, Any]:
    candidate_count = len(candidate_ids)
    scores = Counter({candidate_id: 0 for candidate_id in candidate_ids})
    first_place_votes = Counter({candidate_id: 0 for candidate_id in candidate_ids})
    rank_sums = Counter({candidate_id: 0 for candidate_id in candidate_ids})

    for ranking in rankings:
        first_place_votes[ranking[0]] += 1
        for position, candidate_id in enumerate(ranking, start=1):
            scores[candidate_id] += candidate_count - position + 1
            rank_sums[candidate_id] += position

    ordered = sorted(
        candidate_ids,
        key=lambda candidate_id: (
            -scores[candidate_id],
            -first_place_votes[candidate_id],
            rank_sums[candidate_id],
            candidate_id,
        ),
    )
    return {
        "ranking": ordered,
        "results": [
            {
                "candidate_id": candidate_id,
                "score": scores[candidate_id],
                "first_place_votes": first_place_votes[candidate_id],
                "rank_sum": rank_sums[candidate_id],
            }
            for candidate_id in ordered
        ],
        "judge_count": len(rankings),
        "candidate_count": candidate_count,
        "scoring": "Borda: candidate_count - one_based_position + 1",
        "tie_breaks": ["first_place_votes", "lower_rank_sum", "candidate_id"],
    }


def main() -> int:
    args = parse_args()
    try:
        rankings = load_rankings(args.input)
        candidate_ids = validate_rankings(rankings)
        result = aggregate(rankings, candidate_ids)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
