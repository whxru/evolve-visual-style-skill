---
name: evolve-visual-style
description: Explicit-invocation-only visual style evolution that creates and ranks actual visual demos for websites, web pages, product interfaces, landing pages, posters, illustrations, and other images. Invoke only when the current user request explicitly contains `$evolve-visual-style`. Never activate implicitly from a natural-language request about visual design, website creation or restyling, image creation or editing, mood boards, art direction, or adjacent work. When explicitly invoked, research style possibilities, extract relevant style considerations, generate demo images or simple static demo pages, evolve them with mutation and crossover, rank them visually when evaluators support vision, and for web tasks build a simple static gallery containing every generated demo. Create proofs of style, not a production website or complete application.
---

# Evolve Visual Style

Evolve actual visual demos with fresh subagents. Make the rendered artifact—not a proposal document—the candidate representation. Preserve compact labels and summaries as evolution metadata, and create text descriptions only as an evaluation fallback.

## Invocation Gate

Run this workflow only when the **current user request explicitly contains** `$evolve-visual-style`. Do not infer activation from topic similarity, an ordinary request to design or restyle a website or image, or an invocation in an earlier turn. Mentioning, documenting, reviewing, or quoting the Skill without asking to use it does not activate the workflow. When the explicit token is absent, ignore this Skill entirely.

## Defaults

- `population_size = 2`
- `initial_candidates = 2 * population_size`
- `evaluator_count = 3` and never fewer than 3
- `evolution_rounds = 2` after initialization
- `offspring_per_round = 2 * population_size`
- Alternate `mutation, crossover, mutation, crossover, ...`, starting with mutation.

Honor explicit user overrides. Warn before execution when the requested configuration would require unusually many expensive demo-generation turns. The default run uses 21 subagent turns before any optional fallback describers: 4 initial generators, 3 initial evaluators, then 2 rounds of 4 offspring generators and 3 evaluators.

## Capability Gates

Require true subagent contexts. Do not simulate independent generators or judges in the main context.

Require the capability needed to create the candidate artifact:

- For an image task, require actual image generation. Never substitute a prompt or document for a generated image.
- For a web task, require local file creation, browser rendering, and screenshot capture. Create files that open directly from disk; do not require a build step or local server. Never substitute a design specification for a rendered demo page.

Resolve evaluator capability from advertised features before spawning it. Give images directly to an evaluator that can inspect attached or local images. Give `fallback.md` instead only when that evaluator lacks visual understanding. Never call an unavailable vision tool merely to test it.

Use browsing or image search for live inspiration research when available. If unavailable, work from user-provided and local references and disclose that limitation. Never claim to have searched when no search occurred.

## Candidate Contract

Treat each candidate as three separate layers:

1. **Demo artifact — primary representation**
   - Image task: one actually generated image.
   - Web task: one runnable standalone demo page plus one or more screenshots captured from the real render.
2. **Style metadata — evolution control only**
   - one-sentence summary
   - ordered list of 1-7 concrete noun or noun-phrase labels
   - stable candidate ID and private lineage
3. **Fallback description — nonvisual voting only**
   - an objective description of what the finished demo visibly contains
   - evidence for each selected style consideration
   - no aspirational choices that are absent from the demo

Never rank an unrendered plan as though it were a demo. Never show fallback text to a visual evaluator.

## Core Invariants

1. Preserve the user's goals, audience, content, brand constraints, accessibility needs, required assets, and explicit dislikes throughout every generation.
2. Pass the full selected style-consideration list to every initial, mutation, and crossover agent. Present it as experienced guidance about areas worth addressing, not as predetermined values or a form to fill mechanically.
3. Preserve consideration names across the run so variants remain comparable. Candidate values and visual solutions may change.
4. Keep initial candidates blind and independent. Give each the same brief, research digest, style considerations, hard constraints, and artifact contract—but no other candidate.
5. Use fresh subagents for every candidate and every judge. Do not ask one agent to create multiple candidates or cast multiple votes.
6. Keep ballots blind. Strip stable IDs, labels, lineage, prompts, operator history, and old ranks. Randomize order independently for every judge.
7. Generate style systems, not near-copies. Extract transferable principles from multiple references; never reproduce a living designer's signature style or one source's distinctive composition.
8. Every candidate must be an inspectable finished demo. Repair broken rendering, missing assets, or unreadable output before voting; do not retry merely because the aesthetic is surprising.
9. Do not modify the user's existing site or build a complete project. Create isolated demos only, unless the user separately requests production implementation.
10. Keep every web candidate and the final gallery simple and static. Use plain HTML/CSS and local assets. Do not turn a style proof into an application, development project, or hosted service.

## Working Files

Use an isolated scratch directory during evolution:

```text
brief.md
research.md
style-considerations.md
candidate-ledger.json
novelty/
  g1-existing-styles.md
  g1-c01-check.md
candidates/
  g0-c01/
    demo.png                  # image task
    index.html                # web task
    screenshot-primary.png   # web task
    screenshot-secondary.png # only when needed
    metadata.md
    fallback.md
rankings/
finalists/
gallery.json
```

Use stable internal IDs such as `g0-c01`. Give every newly created demo one immutable global integer `index` and `created_order`, and record `generation_created`, operator, private lineage, evaluation history, selection status, thumbnail path, and full-demo path in `candidate-ledger.json`.

For web tasks, preserve every unique generated demo—not only finalists—and copy all candidate directories into a stable `visual-style-demos/candidates/` output directory. Each candidate must remain directly openable as a static page. For image tasks, preserve finalists unless the user requests a gallery. Never leave final links pointing into temporary storage.

## Workflow

### 1. Resolve the Brief

Inspect the request and any existing website, code, screenshot, image, brand guide, or reference. For an existing site, inspect the rendered result and relevant implementation constraints without editing it.

Record artifact type, audience, desired response, content priorities, brand continuity, hard constraints, accessibility needs, explicit avoidances, and evolution configuration. Ask only for a missing fact that would materially change the search space.

### 2. Research the Search Space

Search the web and image results with 3-5 queries covering adjacent domains, historical or cultural precedents, typography or material references, and comparable contexts. Prefer primary sources, portfolios, museums or archives, foundries, official design systems, or original artifact pages. Gather 6-12 useful references from at least 3 sources when possible.

Write `research.md` with links and one transferable observation per reference. Separate observation from inference. Widen the search space instead of preselecting a style.

### 3. Extract Style Considerations

Read [references/style-anchors.md](references/style-anchors.md) completely. Select the components that can materially anchor this artifact's style. Record each as `preserve`, `reinterpret`, or `explore` when modifying an existing artifact.

Write `style-considerations.md` with:

- selected consideration names and practical advice for each
- hard constraints in a separate section
- artifact-specific visual checks
- consistent render viewports or image ratio for fair comparison

Pass this file unchanged to every generator. Phrase it as: `These are experienced attention areas that a strong demo should address where relevant. They are guidance, not predetermined style values.`

### 4. Initialize Demo Candidates

Read [references/agent-prompts.md](references/agent-prompts.md) completely. Spawn `2 * population_size` fresh generator subagents, one candidate per agent, in parallel batches within the concurrency limit. Add a different abstract exploration cue to each prompt.

Require each generator to:

1. choose a concrete primary style label and a compatible ordered label list
2. decide what image composition or demo-page content best proves the style
3. create the actual artifact
4. for web, render the page and capture the agreed screenshot set
5. visually inspect the result when capable and repair only objective failures
6. write metadata and an evidence-based fallback description after the demo exists

For images, call the available image-generation capability and save the returned image. For web, build an isolated static page that opens directly from the filesystem—normally one `index.html` with embedded or minimal local CSS and local assets. Use plain HTML/CSS. Do not use React, Vue, Svelte, Next.js, Nuxt, Vite, Webpack, package installation, dependency manifests, build steps, local servers, routing, APIs, backends, authentication, databases, analytics, deployment, or production integrations. Do not write JavaScript by default. When interaction character matters, show representative states in the page or use CSS hover/focus states. Only when the user explicitly requires real interaction may the agent add the smallest possible amount of local vanilla JavaScript. The agent decides which page, section mix, or state best demonstrates its direction.

Reject a candidate only when no demo exists, rendering is broken, hard constraints fail, or fallback text describes features absent from the artifact.

### 5. Rank the Demos

Spawn at least `evaluator_count` fresh judges and independently shuffle/relabel the candidates for each.

- **Vision-capable judge:** provide the user brief, hard constraints, style considerations, and the anonymous generated images or screenshots directly. Do not include fallback descriptions, style labels, or implementation source.
- **Nonvisual judge:** provide the same brief, constraints, and considerations plus anonymous `fallback.md` files. State that these are fallback observations of completed demos. Do not provide candidate labels or lineage.

Use the visual path whenever supported. Use an identical image count, viewport set, ordering convention, and display size for every candidate in one ballot.

Require every judge to use exactly two top-level criteria with equal weight:

1. **Fidelity to the user's original input — 50%**: Does the demo satisfy the user's requested goal, audience, content, functional scope, mood, references, constraints, required elements, and explicit avoidances? Treat the original user input as authoritative; do not replace it with the research digest, style labels, or the judge's personal taste.
2. **Strength of stylization — 50%**: Does the demo establish a strong, coherent, recognizable visual language across the relevant style considerations? Reward deliberate and mutually reinforcing typography, color, composition, geometry, imagery, material, and interaction choices. Penalize generic templates, timid default styling, superficial recoloring, disconnected effects, and an attractive label unsupported by the visible demo.

Use feasibility, accessibility, composition, distinctiveness, and consideration coverage only as evidence inside those two criteria, not as additional top-level scoring categories. A material hard-constraint violation is a gate: a violating candidate cannot outrank a compliant candidate merely because it is more stylized.

Require one strict best-to-worst ranking with no ties. Convert blind labels back to stable IDs, save the rankings as JSON, and call:

```bash
python3 <skill-dir>/scripts/aggregate_rankings.py rankings.json
```

Use the returned aggregate order. Keep the first `population_size` candidates as generation 0. For every newly created candidate, record the rank, Borda score, first-place votes, and rank sum from the first evaluation in which it participates. Append later evaluations to `rank_history` without changing its immutable index or creation generation.

### 6. Evolve Each Round

For each round from 1 through `evolution_rounds`:

1. Order the current population by the latest aggregate rank, best first. Treat list index as zero-based `rank`.
2. Inspect **every unique demo created before this round**, including eliminated candidates. Write `novelty/g<round>-existing-styles.md` as a compact existing-style map. For each demo, summarize its primary label and observable typography, palette/value structure, composition and density, geometry, imagery, material/depth, interaction treatment, and distinctive signatures where relevant. Group near-duplicates and identify already-saturated combinations. Derive observations from the artifact or screenshot, not aspirational metadata. Exclude ranks, scores, recommendation status, candidate IDs, lineage, and evaluator comments.
3. Pass that existing-style map unchanged to every mutation and crossover agent. Require the agent to begin with a concise private `NOVELTY CHECK` that:
   - summarizes the already-covered style territory most relevant to its parent or parents
   - names the specific resemblance patterns it will avoid
   - states its new governing label and the high-impact visual axes it will change
   Save this check under `novelty/`; never include it in demo pages, metadata shown to users, fallback voting copy, or judge context.
4. For each of `2 * population_size` offspring, alternate mutation and crossover. Before spawning the child, call:

   ```bash
   python3 <skill-dir>/scripts/sample_parents.py \
     --population-size <N> --count <1-or-2> [--seed <integer>]
   ```

   Use `--count 1` for mutation and `--count 2` for crossover. The sampler uses normalized weights proportional to `1 / (rank + population_size)` and samples two parents without replacement.
5. Give the child agent the unchanged brief, research digest, full style considerations, hard constraints, existing-style map, and parent artifacts:
   - Image mutation: one parent image.
   - Image crossover: two parent images.
   - Web mutation: one parent screenshot set plus its demo source.
   - Web crossover: two parent screenshot sets plus both demo sources.
6. Enforce a boldness floor. Every child must use a primary label not already present in the existing-style map and visibly change at least three high-impact axes: typography; palette/value structure; composition/grid/density; geometry/component silhouette; imagery/subject treatment; material/depth; or interaction/state presentation. At least one changed axis must be structural: composition/hierarchy, typography system, geometry/silhouette, or imagery/perspective. If the child could be mistaken for a colorway, light theme, spacing tweak, or minor component reskin of any existing demo, require a stronger regeneration before voting.
7. Require a newly generated or newly rendered child artifact:
   - **Mutation:** preserve useful parent logic and hard constraints, but replace the governing label or coherent label bundle and make a substantial visual departure from both its parent and the full existing-style map.
   - **Crossover:** create a new governing label and one coherent visual system from compatible parent logic while remaining visibly distinct from both parents and the full existing-style map. Never collage screenshots, split the page into parent halves, or concatenate label lists.
   - **Web offspring:** preserve the same simple static-page boundary as initialization. Do not introduce frameworks, dependencies, build tooling, servers, backends, or deployment.
8. Create metadata and fallback text only after the child demo exists.
9. Form the survival pool from the current `population_size` parents plus all `2 * population_size` offspring. Rank the `3 * population_size` demos with fresh judges using Step 5 and keep the top `population_size`.

Do not carry previous scores into a new round. Rerank the current visual competition from scratch.

### 7. Build the Web Demo Gallery and Present Results

When the run produced web demo pages, build one simple static gallery containing **every unique demo created across initialization and all evolution rounds**, including eliminated candidates. Do not show the same surviving parent more than once. The gallery is an index of visual proofs, not an application.

1. Copy every candidate directory into `visual-style-demos/candidates/<candidate-id>/`, preserving its runnable `index.html`, local assets, and screenshots.
2. Create `visual-style-demos/gallery.json` from the candidate ledger. Give each candidate:
   - immutable global `index`
   - candidate ID and `generation_created`
   - `created_order`
   - primary style label and compact summary
   - rank from its first evaluation after creation, when available
   - Borda score and first-place votes from that evaluation
   - recommendation/selection status such as `Finalist`, `Survived`, or `Eliminated`
   - relative thumbnail path and relative full-demo `href`
   - optional rank history
3. Build the gallery deterministically:

   ```bash
   python3 <skill-dir>/scripts/build_gallery.py \
     visual-style-demos/gallery.json \
     --output visual-style-demos/index.html
   ```

4. Use this exact ordering:
   - group by `generation_created` descending, so the most recently produced demos appear first
   - within each generation, put ranked demos first by aggregate rank ascending, then Borda score descending, first-place votes descending, and newest creation order first
   - put unranked demos after ranked demos, newest creation order first
5. Show each card's global Index, generation, rank or `Unranked`, recommendation status, Borda score, first-place votes, primary label, and thumbnail.
6. Make the entire card clickable. Link directly to `candidates/<candidate-id>/index.html` so the complete runnable demo opens. Use a consistent thumbnail frame and a visually neutral gallery treatment that does not favor one candidate.
7. Keep the gallery dependency-free and directly openable from disk: plain HTML/CSS, relative local paths, no framework, JavaScript, package installation, build step, server, API, backend, deployment, or hosting work.

The gallery homepage is the primary final output for web tasks. Also identify the current `population_size` finalists in compact text and provide a direct link to the gallery.

For an image task, render each final image directly in the response. For a web task, render each final screenshot and link its runnable `index.html` or demo directory. For each finalist include only compact supporting text: primary label, ordered label list, one-sentence summary, why it fits, main tradeoff, and relevant research links.

Do not replace demos with component documents. End with a comparison and a recommendation tied to the user's priorities. State that ranking is a search aid, not objective truth, and ask which demo or cross-demo traits should proceed to production implementation.

## Label Rules

- Use 1-7 concrete archetypes, artifacts, systems, materials, techniques, eras, or places with visual mechanics. One precise primary label may stand alone.
- Reject isolated modifiers such as `modern`, `premium`, `cool`, `bold`, `dynamic`, or `clean`.
- Avoid copyrighted franchise names and imitation of a living designer. Translate references into observable principles.
- A label is valid only when its visual consequence is observable in the demo.

## Quality Gate

Before delivery, verify:

- every candidate and finalist has a real generated image or a real rendered demo page
- screenshots come from the supplied demo source and use consistent comparison viewports
- selected style considerations reached every generator and operator
- every mutation and crossover agent received the complete existing-style map and produced a private novelty check before generating
- every offspring has a new primary label, visibly changes at least three high-impact axes including one structural axis, and is not a near-duplicate of any earlier demo
- labels, summary, fallback text, and source describe what is actually visible
- visual judges received visuals without fallback prose; nonvisual judges received fallback prose
- every judge evaluated both original-input fidelity and stylization strength, with neither replaced by personal taste or extra scoring categories
- finalists differ in structural visual decisions, not only labels or color
- hard constraints survived every operator
- no production project was built or existing site modified without separate authorization
- every web demo is a simple static page that opens directly from disk without a framework, dependency install, build step, or server
- for web tasks, every unique generated demo appears exactly once in the gallery, newest generation first and ranked within its generation
- every gallery card has an immutable Index, recommendation/rank information, a real thumbnail, and a working relative link to the complete demo
- the final gallery is also a simple static HTML/CSS page with no JavaScript, framework, server, or deployment requirement

If the population converges into near-duplicates, disclose it. Run an extra round only with user approval when it exceeds the configured rounds.

## Resources

- [references/style-anchors.md](references/style-anchors.md): style-consideration guidance, demo contract, and fallback schema
- [references/agent-prompts.md](references/agent-prompts.md): demo-generation, mutation, crossover, and dual-mode judging prompts
- `scripts/sample_parents.py`: rank-weighted parent sampling
- `scripts/aggregate_rankings.py`: deterministic multi-judge aggregation
- `scripts/build_gallery.py`: deterministic all-generation web demo gallery builder
