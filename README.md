# Evolve Visual Style

An explicit-invocation-only Agent Skill for exploring, evolving, and visually ranking style directions for websites and images. One canonical workflow supports both Codex and Claude Code through thin installation-time adapters.

The Skill treats rendered artifacts as candidates: image tasks produce actual images, while web tasks produce lightweight static HTML/CSS demo pages and screenshots. It uses independent subagents for generation and judging, commits each direction to a design thesis and asset strategy, audits each render for finish and contextual AI tells, audits cross-candidate visual grammar, preserves both quality and structural diversity during evolution, and builds a static gallery of every generated web demo.

## Highlights

- Extracts domain archetypes, content roles, and artifact-specific style considerations such as page structure, typography, color, geometry, imagery, material, and interaction treatment.
- Searches for fresh references instead of forcing every request into a fixed preset style.
- Assigns mutually exclusive structural and media search territories to initial candidates.
- Derives screenshot-grounded style genomes after rendering instead of treating labels as novelty evidence.
- Audits shared page skeletons, component grammar, rendering media, and AI-default bundles before voting.
- Uses blind multi-agent ranking with two equally weighted criteria: fidelity to the original request and strength of stylization.
- Preserves a quality champion plus structurally distinct diversity champions through deterministic genome-distance selection.
- Gives mutation and crossover agents an artifact-grounded map of every previously explored style and its saturated compound grammar.
- Requires offspring to rewrite page-level structure and container grammar, not merely labels, color, or decoration.
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

- Codex or Claude Code with true subagent support.
- Image-generation capability for image candidates.
- Local file creation, browser rendering, and screenshot capture for web candidates.
- Web or image search is recommended for live inspiration research.

## Install

```bash
git clone https://github.com/whxru/evolve-visual-style-skill.git
cd evolve-visual-style-skill

# Install for Codex
python3 install.py codex

# Install for Claude Code
python3 install.py claude

# Or install both from the same canonical source
python3 install.py both
```

The installer copies the same workflow, references, and scripts to each host. For Claude Code only, it adds `disable-model-invocation: true` to the installed `SKILL.md`; Codex keeps its native invocation policy in `agents/openai.yaml`. Existing installations are never overwritten unless `--force` is supplied, and forced updates preserve the old directory as a timestamped backup.

Restart the host if a newly created top-level Skill directory is not detected immediately.

## Invoke

This Skill never activates implicitly.

Codex:

```text
Use $evolve-visual-style to explore two bold visual directions for my portfolio homepage.
```

Claude Code:

```text
/evolve-visual-style Explore two bold visual directions for my portfolio homepage.
```

An ordinary request such as “redesign this page” does not activate it on either host.

## Cross-host architecture

- `evolve-visual-style/` is the single canonical Skill source.
- Codex reads its explicit-only policy from `agents/openai.yaml`.
- Claude Code requires one additional frontmatter field; `install.py` adds it only to the installed Claude copy.
- All workflow logic, style considerations, Subagent prompts, and deterministic scripts remain identical across hosts.

## Repository layout

```text
install.py
evolve-visual-style/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── agent-prompts.md
│   ├── diversity-control.md
│   ├── style-anchors.md
│   └── visual-finish.md
└── scripts/
    ├── aggregate_rankings.py
    ├── build_gallery.py
    ├── sample_parents.py
    └── select_survivors.py
```

No license has been specified yet.
