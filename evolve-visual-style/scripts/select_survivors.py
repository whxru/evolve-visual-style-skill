#!/usr/bin/env python3
"""Select quality-qualified survivors with structural genome diversity."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


FIELD_WEIGHTS = {
    "artifact_archetype": 2.0,
    "spatial_topology": 2.0,
    "content_or_reading_flow": 1.5,
    "navigation_or_viewer_entry": 1.0,
    "container_or_grouping_grammar": 1.5,
    "whitespace_density_model": 1.0,
    "typography_or_text_system": 1.0,
    "image_medium": 1.5,
    "depth_material": 0.75,
    "interaction_or_temporal_model": 0.75,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Select ranked candidates while preserving structural diversity."
    )
    parser.add_argument("--aggregate", type=Path, required=True)
    parser.add_argument("--genomes", type=Path, required=True)
    parser.add_argument("--population-size", type=int, required=True)
    parser.add_argument("--quality-floor", type=float, default=0.60)
    parser.add_argument("--min-distance", type=float, default=0.35)
    return parser.parse_args()


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read valid JSON from {path}: {exc}") from exc


def load_aggregate(path: Path) -> tuple[list[str], dict[str, float]]:
    payload = read_json(path)
    if not isinstance(payload, dict):
        raise ValueError("aggregate input must be a JSON object")
    ranking = payload.get("ranking")
    results = payload.get("results")
    if not isinstance(ranking, list) or not ranking:
        raise ValueError("aggregate input needs a non-empty ranking array")
    if len(set(ranking)) != len(ranking) or not all(
        isinstance(candidate_id, str) and candidate_id for candidate_id in ranking
    ):
        raise ValueError("ranking must contain unique non-empty candidate IDs")
    if not isinstance(results, list):
        raise ValueError("aggregate input needs a results array")
    scores: dict[str, float] = {}
    for result in results:
        if not isinstance(result, dict):
            raise ValueError("every aggregate result must be an object")
        candidate_id = result.get("candidate_id")
        score = result.get("score")
        if candidate_id in ranking and isinstance(score, (int, float)):
            scores[candidate_id] = float(score)
    if set(scores) != set(ranking):
        raise ValueError("aggregate results must provide a numeric score for every candidate")
    return ranking, scores


def load_genomes(path: Path, candidate_ids: list[str]) -> dict[str, dict[str, Any]]:
    payload = read_json(path)
    if isinstance(payload, dict):
        records = payload.get("genomes", payload.get("candidates"))
    else:
        records = payload
    if not isinstance(records, list):
        raise ValueError("genomes input must be an array or contain genomes/candidates array")

    genomes: dict[str, dict[str, Any]] = {}
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("every genome must be an object")
        candidate_id = record.get("candidate_id")
        genome = record.get("genome", record)
        if not isinstance(candidate_id, str) or not candidate_id:
            raise ValueError("every genome needs a non-empty candidate_id")
        if candidate_id in genomes:
            raise ValueError(f"duplicate genome for {candidate_id}")
        if not isinstance(genome, dict):
            raise ValueError(f"genome for {candidate_id} must be an object")
        missing = [field for field in FIELD_WEIGHTS if field not in genome]
        if missing:
            raise ValueError(f"genome for {candidate_id} lacks fields: {', '.join(missing)}")
        genomes[candidate_id] = genome

    missing_ids = sorted(set(candidate_ids) - set(genomes))
    if missing_ids:
        raise ValueError(f"missing genomes for ranked candidates: {', '.join(missing_ids)}")
    return genomes


def normalized_set(value: Any) -> set[str]:
    values = value if isinstance(value, list) else [value]
    normalized = {
        str(item).strip().casefold()
        for item in values
        if isinstance(item, (str, int, float)) and str(item).strip()
    }
    if not normalized:
        raise ValueError("genome comparison fields cannot be empty")
    return normalized


def value_distance(left: Any, right: Any) -> float:
    left_set = normalized_set(left)
    right_set = normalized_set(right)
    return 1.0 - len(left_set & right_set) / len(left_set | right_set)


def genome_distance(left: dict[str, Any], right: dict[str, Any]) -> float:
    weighted = sum(
        value_distance(left[field], right[field]) * weight
        for field, weight in FIELD_WEIGHTS.items()
    )
    return weighted / sum(FIELD_WEIGHTS.values())


def select(
    ranking: list[str],
    scores: dict[str, float],
    genomes: dict[str, dict[str, Any]],
    population_size: int,
    quality_floor: float,
    min_distance: float,
) -> dict[str, Any]:
    if population_size < 1:
        raise ValueError("population size must be at least 1")
    if population_size > len(ranking):
        raise ValueError("population size cannot exceed ranked candidate count")
    if not 0 <= quality_floor <= 1:
        raise ValueError("quality floor must be between 0 and 1")
    if not 0 <= min_distance <= 1:
        raise ValueError("minimum distance must be between 0 and 1")

    winner_score = scores[ranking[0]]
    threshold = winner_score * quality_floor
    eligible = [candidate_id for candidate_id in ranking if scores[candidate_id] >= threshold]
    rank_index = {candidate_id: index for index, candidate_id in enumerate(ranking)}
    selected = [ranking[0]]
    selected_details = [
        {
            "candidate_id": ranking[0],
            "role": "quality_champion",
            "aggregate_rank": 1,
            "score": scores[ranking[0]],
            "minimum_distance_to_selected": None,
        }
    ]

    while len(selected) < population_size:
        options: list[tuple[float, int, str]] = []
        for candidate_id in eligible:
            if candidate_id in selected:
                continue
            distance = min(
                genome_distance(genomes[candidate_id], genomes[kept]) for kept in selected
            )
            options.append((distance, -rank_index[candidate_id], candidate_id))
        if not options:
            break
        distance, _, candidate_id = max(options)
        if distance < min_distance:
            break
        selected.append(candidate_id)
        selected_details.append(
            {
                "candidate_id": candidate_id,
                "role": "diversity_champion",
                "aggregate_rank": rank_index[candidate_id] + 1,
                "score": scores[candidate_id],
                "minimum_distance_to_selected": round(distance, 6),
            }
        )

    matrix = {
        left: {
            right: round(genome_distance(genomes[left], genomes[right]), 6)
            for right in ranking
        }
        for left in ranking
    }
    needs_regeneration = len(selected) < population_size
    return {
        "selected": selected,
        "selected_details": selected_details,
        "needs_regeneration": needs_regeneration,
        "reason": (
            "population filled with quality-qualified structurally distinct candidates"
            if not needs_regeneration
            else "not enough quality-qualified candidates clear the structural distance floor"
        ),
        "population_size": population_size,
        "quality_floor": quality_floor,
        "quality_score_threshold": round(threshold, 6),
        "minimum_distance": min_distance,
        "eligible": eligible,
        "unselected": [candidate_id for candidate_id in ranking if candidate_id not in selected],
        "distance_matrix": matrix,
        "distance_fields": FIELD_WEIGHTS,
    }


def main() -> int:
    args = parse_args()
    try:
        ranking, scores = load_aggregate(args.aggregate)
        genomes = load_genomes(args.genomes, ranking)
        result = select(
            ranking,
            scores,
            genomes,
            args.population_size,
            args.quality_floor,
            args.min_distance,
        )
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
