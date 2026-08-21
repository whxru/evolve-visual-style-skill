#!/usr/bin/env python3
"""Build a neutral, dependency-free static HTML/CSS demo gallery."""

from __future__ import annotations

import argparse
import html
import json
import sys
from collections import defaultdict
from pathlib import Path, PurePosixPath
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a static gallery for all generated web demo candidates."
    )
    parser.add_argument("manifest", type=Path, help="Path to gallery.json")
    parser.add_argument("--output", type=Path, required=True, help="Output index.html")
    return parser.parse_args()


def relative_path(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be a non-empty relative path")
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"{field} must stay inside the gallery directory")
    return value


def optional_int(value: Any, field: str) -> int | None:
    if value is None:
        return None
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        raise ValueError(f"{field} must be a non-negative integer or null")
    return value


def load_manifest(path: Path) -> tuple[str, str, list[dict[str, Any]]]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read valid manifest JSON: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValueError("manifest must be a JSON object")
    raw_candidates = payload.get("candidates")
    if not isinstance(raw_candidates, list) or not raw_candidates:
        raise ValueError("manifest candidates must be a non-empty array")

    title = str(payload.get("title") or "Visual Style Evolution")
    subtitle = str(payload.get("subtitle") or "All generated web demos")
    candidates: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    seen_indices: set[int] = set()
    seen_orders: set[int] = set()

    for position, raw in enumerate(raw_candidates, start=1):
        if not isinstance(raw, dict):
            raise ValueError(f"candidate {position} must be an object")
        candidate_id = raw.get("candidate_id")
        if not isinstance(candidate_id, str) or not candidate_id.strip():
            raise ValueError(f"candidate {position} has invalid candidate_id")
        index = raw.get("index")
        generation = raw.get("generation")
        created_order = raw.get("created_order")
        for value, field in (
            (index, "index"),
            (generation, "generation"),
            (created_order, "created_order"),
        ):
            if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                raise ValueError(f"candidate {candidate_id} has invalid {field}")
        if index < 1 or created_order < 1:
            raise ValueError(f"candidate {candidate_id} index/order must start at 1")
        if candidate_id in seen_ids or index in seen_indices or created_order in seen_orders:
            raise ValueError("candidate IDs, indices, and creation orders must be unique")
        seen_ids.add(candidate_id)
        seen_indices.add(index)
        seen_orders.add(created_order)

        candidates.append(
            {
                "candidate_id": candidate_id,
                "index": index,
                "generation": generation,
                "created_order": created_order,
                "label": str(raw.get("label") or "Untitled direction"),
                "summary": str(raw.get("summary") or ""),
                "rank": optional_int(raw.get("rank"), f"{candidate_id}.rank"),
                "score": optional_int(raw.get("score"), f"{candidate_id}.score"),
                "first_place_votes": optional_int(
                    raw.get("first_place_votes"), f"{candidate_id}.first_place_votes"
                ),
                "recommendation": str(raw.get("recommendation") or "Candidate"),
                "thumbnail": relative_path(raw.get("thumbnail"), "thumbnail"),
                "href": relative_path(raw.get("href"), "href"),
            }
        )
    return title, subtitle, candidates


def sort_key(candidate: dict[str, Any]) -> tuple[int, int, int, int, int]:
    rank = candidate["rank"]
    return (
        1 if rank is None else 0,
        rank if rank is not None else sys.maxsize,
        -(candidate["score"] or 0),
        -(candidate["first_place_votes"] or 0),
        -candidate["created_order"],
    )


def render_card(candidate: dict[str, Any]) -> str:
    rank = candidate["rank"]
    rank_text = f"Rank #{rank}" if rank is not None else "Unranked"
    score = candidate["score"]
    votes = candidate["first_place_votes"]
    metrics = [rank_text]
    if score is not None:
        metrics.append(f"Borda {score}")
    if votes is not None:
        metrics.append(f"1st-place votes {votes}")
    metric_text = " · ".join(metrics)
    summary = html.escape(candidate["summary"])
    summary_html = f'<p class="summary">{summary}</p>' if summary else ""
    return f"""
      <a class="card" href="{html.escape(candidate['href'], quote=True)}" target="_blank" rel="noopener">
        <div class="thumb"><img src="{html.escape(candidate['thumbnail'], quote=True)}" alt="Thumbnail for demo {candidate['index']}" loading="lazy"></div>
        <div class="body">
          <div class="eyebrow"><span>Index #{candidate['index']:03d}</span><span>Generation {candidate['generation']}</span></div>
          <h3>{html.escape(candidate['label'])}</h3>
          {summary_html}
          <div class="meta"><span class="status">{html.escape(candidate['recommendation'])}</span><span>{html.escape(metric_text)}</span></div>
        </div>
      </a>"""


def render_page(title: str, subtitle: str, candidates: list[dict[str, Any]]) -> str:
    grouped: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for candidate in candidates:
        grouped[candidate["generation"]].append(candidate)
    sections = []
    for generation in sorted(grouped, reverse=True):
        cards = "\n".join(render_card(item) for item in sorted(grouped[generation], key=sort_key))
        sections.append(
            f'<section><header class="generation"><h2>Generation {generation}</h2>'
            f'<span>{len(grouped[generation])} demos</span></header><div class="grid">{cards}</div></section>'
        )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>
    :root {{ color-scheme: light; --bg:#f4f4f1; --panel:#fff; --ink:#181816; --muted:#666660; --line:#d8d8d2; --accent:#2457d6; }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; background:var(--bg); color:var(--ink); font:15px/1.5 ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }}
    main {{ width:min(1400px,calc(100% - 32px)); margin:0 auto; padding:56px 0 80px; }}
    .hero {{ display:flex; justify-content:space-between; gap:24px; align-items:end; border-bottom:1px solid var(--line); padding-bottom:24px; margin-bottom:40px; }}
    h1 {{ margin:0; font-size:clamp(32px,5vw,64px); line-height:1; letter-spacing:-.04em; }}
    .hero p {{ max-width:520px; margin:0; color:var(--muted); }}
    section + section {{ margin-top:56px; }}
    .generation {{ display:flex; justify-content:space-between; align-items:baseline; margin-bottom:16px; }}
    h2 {{ margin:0; font-size:24px; }} .generation span,.eyebrow,.meta {{ color:var(--muted); }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(280px,1fr)); gap:18px; }}
    .card {{ display:block; min-width:0; overflow:hidden; color:inherit; text-decoration:none; background:var(--panel); border:1px solid var(--line); border-radius:12px; transition:transform 140ms ease,border-color 140ms ease; }}
    .card:hover {{ transform:translateY(-2px); border-color:#9a9a92; }} .card:focus-visible {{ outline:3px solid var(--accent); outline-offset:3px; }}
    .thumb {{ aspect-ratio:16/10; overflow:hidden; background:#e5e5df; border-bottom:1px solid var(--line); }}
    .thumb img {{ width:100%; height:100%; object-fit:cover; object-position:top; display:block; }}
    .body {{ padding:16px; }} .eyebrow,.meta {{ display:flex; flex-wrap:wrap; justify-content:space-between; gap:8px 16px; font-size:12px; }}
    h3 {{ margin:12px 0 6px; font-size:20px; line-height:1.2; }} .summary {{ margin:0 0 18px; color:#44443f; }}
    .meta {{ border-top:1px solid var(--line); padding-top:12px; }} .status {{ color:var(--accent); font-weight:700; }}
    @media (max-width:700px) {{ main {{ width:min(100% - 20px,1400px); padding-top:28px; }} .hero {{ display:block; }} .hero p {{ margin-top:16px; }} }}
    @media (prefers-reduced-motion:reduce) {{ .card {{ transition:none; }} }}
  </style>
</head>
<body>
  <main>
    <header class="hero"><h1>{html.escape(title)}</h1><p>{html.escape(subtitle)}. Newest generation first; ranked within each generation. Select any card to open the complete demo.</p></header>
    {''.join(sections)}
  </main>
</body>
</html>
"""


def main() -> int:
    args = parse_args()
    try:
        title, subtitle, candidates = load_manifest(args.manifest)
        output = render_page(title, subtitle, candidates)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
