# Structural Diversity Control

Use screenshot-grounded structural fingerprints to prevent a population from becoming several themed skins of one familiar layout. The demo remains the candidate; these records are private control metadata.

## Contents

- Domain archetype and content roles
- Exploration territories
- Observed style genome
- Population convergence audit
- AI-default evidence
- Diversity-aware survival

## Domain Archetype and Content Roles

Identify what kind of real artifact the demo must resemble before assigning visual directions. Record the domain archetype, audience relationship, trust mechanism, core task, content model, and conversion or reading flow. A commercial homepage, academic profile, publication, product tool, and cultural archive must not differ only in copy.

Separate required **content roles** from a fixed component checklist. Preserve roles such as identity, primary task, evidence, navigation, and action, but let candidates express them with different page structures and at different scroll depths. A shared screenshot viewport is a comparison frame, not a requirement to compress every role into the same first-screen grid.

Require every web demo to resemble a plausible page in its domain. Reject a design-system specimen, component board, or poster made of UI samples unless the brief calls for one.

## Exploration Territories

Before initial generation, derive one mutually exclusive territory per initial candidate from the brief and research. A territory is not a named preset style. It constrains a different generative route across at least three of:

- page archetype
- spatial topology
- content or reading flow
- navigation model
- container grammar
- whitespace and density curve
- typography system
- image medium and image role
- depth or material model
- interaction metaphor

Keep domain fidelity and hard constraints common to all territories. Do not assign every territory the same hero, input, card count, or above-the-fold checklist. Ensure the batch covers multiple structural families and, when assets and the brief permit, multiple media such as photography, generated imagery, illustration, collage, inline SVG, diagram, 3D render, or type-led composition.

Static web delivery does not mean CSS-only imagery. Use self-contained local assets, licensed local fonts, generated images, textures, or inline SVG when they materially establish a territory. Do not use remote runtime dependencies.

## Observed Style Genome

After rendering and inspecting a demo, write `style-genome.json` from visible evidence. Do not fill it from the intended label before rendering.

```json
{
  "candidate_id": "g0-c01",
  "domain_genre": "commercial research-and-product homepage",
  "artifact_archetype": "editorial narrative homepage",
  "spatial_topology": "continuous vertical field with full-bleed interruptions",
  "content_or_reading_flow": "mission to evidence to product action",
  "navigation_or_viewer_entry": "quiet global masthead with contextual section links",
  "container_or_grouping_grammar": "mostly containerless; framed evidence only",
  "whitespace_density_model": "large variable fields punctuated by dense evidence",
  "typography_or_text_system": "display serif narrative with utilitarian sans controls",
  "image_medium": ["documentary photography", "data annotation"],
  "image_role": "primary narrative evidence rather than decoration",
  "palette_distribution": "mostly neutral photography with sparse signal color",
  "geometry": "full-bleed crops and irregular annotation lines",
  "depth_material": "photographic depth with flat typographic overlays",
  "interaction_or_temporal_model": "editorial reading interrupted by direct product actions",
  "distinctive_signatures": ["caption rails", "edge-to-edge research scenes"],
  "ai_default_flags": []
}
```

Keep values concrete and artifact-grounded. Do not make every field unique by paraphrasing. Use the same phrase for materially equivalent mechanisms so recurrence can be detected.

For image-only candidates, use the same keys with image-appropriate values: `artifact_archetype` names the composition family, `content_or_reading_flow` names the eye path, `navigation_or_viewer_entry` names the framing and first visual entry, `container_or_grouping_grammar` names grouping and silhouette logic, and `interaction_or_temporal_model` names implied action, sequence, or stillness.

The deterministic survivor selector compares these fields with extra weight on artifact archetype, spatial topology, grouping grammar, content/reading flow, and image medium. Color and labels do not establish structural distance by themselves.

## Population Convergence Audit

After initial candidates render and after each offspring batch renders, inspect all relevant screenshots together before voting. Write a private `population-audit.md` containing:

1. one compact observed genome per candidate
2. repeated non-required mechanisms and their recurrence counts
3. structural clusters and the candidates in each cluster
4. shared compound grammars: combinations that recur together
5. underexplored structural and media territories
6. redundant candidates to regenerate before the population can be filled

A useful compound grammar is specific enough to reproduce the resemblance, for example:

```text
utility top bar + oversized hero + bordered prompt field + equal card row
+ one-pixel frames + flat CSS diagram + neutral ground with one signal color
```

Do not reduce the audit to a list of nouns such as `microfilm`, `ticket`, or `newspaper`. Explain the page skeleton, component relationships, medium, and density that make several differently named candidates look alike.

Treat a batch as converged when a non-required structural bundle dominates it, when multiple candidates could exchange labels without changing their layouts, or when most candidates use the same rendering medium despite open alternatives. Regenerate the most redundant candidates with new territories before voting. Allow one diversity-repair batch per evaluation stage by default; disclose unresolved convergence rather than looping indefinitely.

Pass an anonymous, candidate-ID-free version of the shared grammar and saturated bundles to mutation and crossover agents. Do not pass ranks or evaluator opinions.

## AI-Default Evidence

Look for contextual evidence of model-prior convergence, not a universal blacklist. Potential signals include repeated bento grids, centered giant headlines, floating prompt bars, equal card rows, generic dashboard chrome, gratuitous pills or status tags, uniform corner logic, black/off-white plus one neon accent, decorative orbital diagrams, generic grain, and every required item compressed above the fold.

Any one mechanism may be appropriate. Penalize an unrequested bundle when it recurs across candidates, does not arise from domain needs or references, and could be transplanted unchanged into an unrelated commercial, academic, or portfolio site.

## Diversity-Aware Survival

Keep jury ranking as the quality signal. Do not add a third jury criterion. After aggregation, select survivors with both quality and structural distance:

1. keep the aggregate winner as the quality champion
2. restrict remaining choices to candidates above the configured quality floor
3. greedily choose the candidate with the greatest minimum genome distance from already selected survivors, breaking ties by aggregate rank
4. require the configured minimum structural distance
5. if the population cannot be filled, regenerate a candidate in the missing territory and evaluate again

For the default population of two, this yields one quality champion and one structurally distinct diversity champion. Ranking still controls recommendation order; diversity controls who remains available for evolution.

Use:

```bash
python3 <skill-dir>/scripts/select_survivors.py \
  --aggregate aggregate.json \
  --genomes genomes.json \
  --population-size <N>
```

Defaults are a quality floor of `0.60` relative to the winner's Borda score and a minimum weighted genome distance of `0.35`. Treat `needs_regeneration: true` as an unfilled population, not permission to silently fall back to the next same-shaped candidate.
