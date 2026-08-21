# Evolve Visual Style

An explicit-invocation-only Codex Skill for exploring, evolving, and visually ranking style directions for websites and images.

The Skill treats rendered artifacts as candidates: image tasks produce actual images, while web tasks produce lightweight static HTML/CSS demo pages and screenshots. It uses independent subagents for generation and judging, evolves the strongest directions with mutation and crossover, and builds a static gallery of every generated web demo.

## Highlights

- Extracts artifact-specific style considerations such as typography, color, composition, geometry, imagery, material, and interaction treatment.
- Searches for fresh references instead of forcing every request into a fixed preset style.
- Maintains concrete style labels and summaries as evolution metadata.
- Uses blind multi-agent ranking with two equally weighted criteria: fidelity to the original request and strength of stylization.
- Gives mutation and crossover agents an artifact-grounded map of every previously explored style so offspring avoid near-duplicates.
- Requires bold offspring that visibly change at least three high-impact visual axes, including one structural axis.
- Produces simple static web demos and a dependency-free static gallery rather than a production application.

## Default evolution settings

| Setting | Default |
| --- | ---: |
| Population size | 2 |
| Initial candidates | 4 |
| Evaluators per ranking | 3 |
| Evolution rounds | 2 |
| Offspring per round | 4 |

## Requirements

- Codex with true subagent support.
- Image-generation capability for image candidates.
- Local file creation, browser rendering, and screenshot capture for web candidates.
- Web or image search is recommended for live inspiration research.

## Install

```bash
git clone https://github.com/whxru/evolve-visual-style-skill.git
mkdir -p ~/.codex/skills
cp -R evolve-visual-style-skill/evolve-visual-style ~/.codex/skills/
```

Restart or reload Codex after installation if the Skill is not discovered immediately.

## Invoke

This Skill never activates implicitly. The current request must contain the exact token `$evolve-visual-style`:

```text
Use $evolve-visual-style to explore two bold visual directions for my portfolio homepage.
```

An ordinary request such as “redesign this page” does not activate it.

## Repository layout

```text
evolve-visual-style/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── agent-prompts.md
│   └── style-anchors.md
└── scripts/
    ├── aggregate_rankings.py
    ├── build_gallery.py
    └── sample_parents.py
```

No license has been specified yet.
