#!/usr/bin/env python3
"""Sample one or two parent indices using the skill's rank-weight formula."""

from __future__ import annotations

import argparse
import json
import random
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Sample zero-based indices with weights proportional to "
            "1 / (rank + population_size)."
        )
    )
    parser.add_argument("--population-size", type=int, required=True)
    parser.add_argument("--count", type=int, choices=(1, 2), required=True)
    parser.add_argument("--seed", type=int)
    return parser.parse_args()


def weighted_pick(
    rng: random.Random, available: list[int], population_size: int
) -> int:
    weights = [1.0 / (rank + population_size) for rank in available]
    return rng.choices(available, weights=weights, k=1)[0]


def main() -> int:
    args = parse_args()
    if args.population_size < 1:
        print("population size must be at least 1", file=sys.stderr)
        return 2
    if args.count > args.population_size:
        print("count cannot exceed population size", file=sys.stderr)
        return 2

    rng = random.Random(args.seed)
    available = list(range(args.population_size))
    selected: list[int] = []
    for _ in range(args.count):
        picked = weighted_pick(rng, available, args.population_size)
        selected.append(picked)
        available.remove(picked)

    raw_weights = [
        1.0 / (rank + args.population_size)
        for rank in range(args.population_size)
    ]
    total = sum(raw_weights)
    probabilities = [weight / total for weight in raw_weights]
    print(
        json.dumps(
            {
                "indices": selected,
                "rank_base": 0,
                "population_size": args.population_size,
                "probabilities": probabilities,
                "seed": args.seed,
            },
            ensure_ascii=False,
            separators=(",", ":"),
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
