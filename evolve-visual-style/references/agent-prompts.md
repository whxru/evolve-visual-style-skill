# Clean-Context Demo Agent Prompts

Use these contracts with raw task-local artifacts. Do not leak other candidates to initial generators. Do not leak labels, lineage, prompts, operators, or old ranks to judges.

## Contents

- Shared generator context
- Image demo generator
- Web demo generator
- Population convergence auditor
- Operator novelty rules
- Mutation
- Crossover
- Visual judge
- Nonvisual fallback judge
- Blindness and vote validation

## Shared Generator Context

```text
Create one independent visual-style demo for the brief below. The finished demo artifact is the candidate; a written proposal is not a candidate.

USER BRIEF
<brief>

DOMAIN ARCHETYPE AND CONTENT ROLES
<real artifact type, audience relationship, trust mechanism, core task, content model, and required roles without a fixed component layout>

RESEARCH DIGEST
<facts, transferable observations, and URLs>

STYLE CONSIDERATIONS
<selected attention areas and preserve/reinterpret/explore status>

Treat these considerations as experienced guidance about areas a strong demo should address where relevant. They are not predetermined style values and not a form to fill.

HARD CONSTRAINTS
<immutable requirements and avoids>

EXPLORATION CUE
<one mutually exclusive structural and media territory derived for this candidate>

First choose one concrete primary style label and up to six compatible supporting noun phrases. Decide what domain-authentic visual content best proves that style within the assigned territory. Create the actual demo. Only after rendering and visually inspecting it, write compact metadata, an observed style-genome.json, and an objective fallback observation describing what is genuinely visible or implemented. The label does not prove novelty. Do not mention other candidates, genetic algorithms, voting, or lineage outside private metadata.
```

## Image Demo Generator

Append to the shared context:

```text
Use the available image-generation capability to create one finished image at the agreed ratio. Return and save the actual generated image; do not return only a prompt, specification, or mood board. Make the selected style considerations visibly consequential. Inspect the result when capable and repair only objective failures against hard constraints. Save metadata.md and fallback.md beside the image after generation.
```

## Web Demo Generator

Append to the shared context:

```text
Build one isolated, lightweight static demo page that shows the proposed visual system. Decide which page type, content, components, and representative state best demonstrate it. Normally use one index.html with embedded or minimal local CSS and local assets. The file must open directly from disk.

Use plain HTML/CSS. Do not use React, Vue, Svelte, Next.js, Nuxt, Vite, Webpack, package managers, dependency manifests, build steps, local servers, routing, APIs, backend services, authentication, databases, analytics, deployment, hosting, or production integrations. Do not add JavaScript by default. If interaction character matters, depict the relevant states in the static composition or use CSS hover/focus states. Add only the smallest amount of local vanilla JavaScript when the user explicitly requires real interaction. This is a visual proof, not a product prototype.

Static delivery is not a CSS-only visual limitation. Use self-contained local photography, generated images, illustration, collage, textures, licensed local fonts, or inline SVG when they materially establish the assigned territory. Do not load remote runtime assets. Make one plausible page in the requested domain; do not default to a component specimen, bento board, or posterized dashboard. Preserve required content roles without forcing every role, card, or link into the first screenshot.

Render the page in a real browser at the agreed comparison viewport and save screenshot-primary.png. Create the agreed secondary viewport only when requested for every candidate. Inspect the screenshots and repair broken rendering, missing assets, clipping, unreadable required text, or unusable contrast. The rendered screenshot is the visual ballot artifact; the runnable page is the supporting deliverable. Write metadata.md and fallback.md only after the final render.
```

## Population Convergence Auditor

Give a fresh auditor every relevant generated image or screenshot at the same display size plus the brief, domain archetype, content roles, hard constraints, and observed genomes. Prefer a vision-capable auditor. When vision is unavailable, give anonymous fallback observations and observed genomes, state that visual similarity confidence is lower, and never imply direct image inspection. This is an internal diversity gate, not a jury ballot.

```text
Inspect the completed demos together for structural convergence. Do not rank their quality and do not propose cosmetic restyles.

For each demo, verify or correct its observed genome using visible evidence. Then report:

SHARED NON-REQUIRED MECHANISMS
- <mechanism>: <recurrence count and visible evidence>

STRUCTURAL CLUSTERS
- <cluster>: <members and the page skeleton, content flow, container grammar, medium, and density that make them similar>

SATURATED COMPOUND GRAMMARS
- <reproducible bundle of mechanisms that recur together>

UNDEREXPLORED TERRITORIES
- <structural or media route, not merely a new theme noun>

REGENERATE BEFORE VOTING
- <redundant demos, if any, and which missing territory each replacement must occupy>

Treat differently named demos as duplicates when they could exchange labels without changing their layouts. Look for contextual AI-default bundles such as the same top bar, oversized hero, prompt field, equal card row, uniform framing, flat diagram, accent color, or above-the-fold compression. Any one mechanism may be appropriate; flag unrequested recurrence, not universal style crimes. Do not use ranks, authorship, lineage, or personal taste.
```

## Operator Novelty Rules

Insert this block into every mutation and crossover prompt:

```text
EXISTING STYLE AND FEATURE MAP
<artifact-grounded structural and visual summary of every unique demo created so far, including eliminated demos; include shared compound grammars and saturated bundles; no IDs, ranks, scores, lineage, or evaluator comments>

Before creating the artifact, return a concise private NOVELTY CHECK with:
- ALREADY COVERED: the relevant existing style territories and visible feature bundles
- AVOID: the labels, page skeletons, content flows, container grammars, media choices, and compound mechanisms the child must not resemble
- NEW GOVERNING LABEL: one concrete label absent from the map
- STRUCTURAL REWRITE: the new page archetype/spatial topology/content flow and container grammar
- SUPPORTING DEPARTURES: at least one typography, image-medium, depth/material, or interaction change

The child must change a page-level structural axis—page archetype, spatial topology, or content flow—plus container grammar, and at least one supporting system: typography, image medium/role, depth/material, or interaction. A new label and palette do not establish novelty.

Do not create a colorway, theme inversion, minor spacing change, radius adjustment, themed skin, or component reskin. The child must be unmistakably different from every mapped demo at a glance while still satisfying the user brief, domain archetype, content roles, and hard constraints. If it could exchange labels with an existing demo without changing its page skeleton, regenerate it before returning. Keep the NOVELTY CHECK out of user-facing files, fallback voting copy, and judge context.
```

## Mutation Prompt

```text
Create one substantial visual mutation for the same brief.

USER BRIEF
<brief>

DOMAIN ARCHETYPE AND CONTENT ROLES
<unchanged domain guidance>

RESEARCH DIGEST
<digest>

STYLE CONSIDERATIONS AND HARD CONSTRAINTS
<unchanged guidance and constraints>

PARENT ARTIFACT
<one image, or one screenshot set plus web demo source>

PARENT METADATA
<summary and labels only>

Apply the Operator Novelty Rules above before creation. Change the governing generative bundle, then make the structural rewrite plainly observable in a newly generated image or newly rendered demo page. Preserve useful parent logic, every hard constraint, and deliberate treatment of the full consideration list, but depart substantially from both the parent and every style in the existing map. Clear the structural boldness floor; do not merely rename, recolor, or describe a variant. Return a new demo artifact, then observed genome, metadata, and fallback text. Do not mention mutation, parentage, ranking, evaluation, or the novelty check in user-facing files.

For a web child, preserve the lightweight static-page contract: plain HTML/CSS, directly openable from disk, no framework, dependencies, build step, server, backend, deployment, or hosting. Keep JavaScript absent unless the user explicitly required real interaction; then use only minimal local vanilla JavaScript.
```

## Crossover Prompt

```text
Create one coherent new visual demo from two source candidates for the same brief.

USER BRIEF
<brief>

DOMAIN ARCHETYPE AND CONTENT ROLES
<unchanged domain guidance>

RESEARCH DIGEST
<digest>

STYLE CONSIDERATIONS AND HARD CONSTRAINTS
<unchanged guidance and constraints>

SOURCE ARTIFACT A
<image, or screenshot set plus source>

SOURCE ARTIFACT B
<image, or screenshot set plus source>

SOURCE METADATA
<summaries and labels only>

Apply the Operator Novelty Rules above before creation. Invent one new primary label that names a unified visual model and is absent from the existing map. Select compatible generative principles from both sources, then create a new page archetype, spatial organization, and component relationship rather than averaging their surfaces. The result must be unmistakably different from both parents and every mapped style. Clear the structural boldness floor. Do not collage parent screenshots, divide the page into parent halves, concatenate label lists, average values mechanically, or preserve contradictions. Reconsider every style consideration and preserve all hard constraints. Return the new demo first, then observed genome, metadata, and fallback text. Do not mention crossover, sources, lineage, ranking, evaluation, or the novelty check in user-facing files.

For a web child, preserve the lightweight static-page contract: plain HTML/CSS, directly openable from disk, no framework, dependencies, build step, server, backend, deployment, or hosting. Keep JavaScript absent unless the user explicitly required real interaction; then use only minimal local vanilla JavaScript.
```

## Visual Judge Prompt

Attach anonymous images or screenshots directly. Use the same number, viewport convention, order, and display size per candidate. Do not attach fallback text.

```text
Act as an independent visual-design juror. Rank every anonymous completed demo from best to worst for the brief. Judge what is visibly present; do not imagine repairs or hidden implementation. No ties.

USER BRIEF
<brief>

HARD CONSTRAINTS
<constraints>

STYLE CONSIDERATIONS
<attention areas>

ANONYMOUS VISUAL DEMOS
<blind labels with directly attached generated images or rendered screenshots>

Use exactly two top-level criteria:
1. FIDELITY TO THE USER'S ORIGINAL INPUT — 50%. Judge whether the demo satisfies the requested goal, audience, content, functional scope, mood, references, required elements, constraints, and explicit avoidances. The original input is authoritative; do not replace it with your taste, the research digest, or inferred trends.
2. STRENGTH OF STYLIZATION — 50%. Judge whether the visible demo establishes a strong, coherent, recognizable visual language that remains credible for the requested domain. Reward deliberate, mutually reinforcing choices across page archetype, spatial topology, content flow, typography, imagery, container grammar, color, geometry, material, and interaction. Penalize generic templates, design-system specimen boards presented as real sites, domain-agnostic AI-default bundles, timid defaults, superficial recoloring, disconnected effects, and style names unsupported by visible evidence.

Treat feasibility, accessibility, composition, distinctiveness, and consideration coverage only as evidence within those two criteria, never as extra scoring categories. A material hard-constraint violation is a gate: a violating candidate cannot outrank a compliant candidate merely for being more stylized. Return:

RANKING: <blind-id-1> > <blind-id-2> > ...
REASONS:
- <blind-id>:
  - Original-input fidelity: <concise evidence>
  - Stylization strength: <concise visible evidence>
...

Use every blind ID exactly once. Do not output scores, ties, revised designs, style-name guesses, or authorship speculation.
```

## Nonvisual Fallback Judge Prompt

Use only when the evaluator lacks visual understanding. Give anonymous fallback observations, never screenshots it cannot inspect.

```text
Act as an independent design juror using objective fallback observations of completed demos. Rank every candidate from best to worst for the brief. Do not treat unreported features as present and do not repair candidates. No ties.

USER BRIEF
<brief>

HARD CONSTRAINTS
<constraints>

STYLE CONSIDERATIONS
<attention areas>

ANONYMOUS FALLBACK OBSERVATIONS
<blind labels and fallback.md contents>

Use exactly the same two-part, 50/50 rubric as the visual jury: fidelity to the user's original input and strength of stylization. Within stylization, require domain credibility and penalize generic templates, specimen boards presented as sites, and domain-agnostic AI-default bundles when the observations support them. Treat feasibility, accessibility, composition, distinctiveness, and consideration coverage only as evidence inside those two criteria. Lower confidence when an important point is not evidenced. A material hard-constraint violation cannot outrank a compliant candidate merely for stronger styling. Return a strict RANKING line, then for every blind ID provide one `Original-input fidelity` reason and one `Stylization strength` reason. Use each ID once. Do not output extra scoring categories, scores, ties, revisions, labels, or authorship speculation.
```

## Blindness and Vote Validation

For every judge, create a fresh random permutation and temporary labels such as `Option K`, `Option R`, and `Option V`. Keep the mapping private. Strip candidate IDs, primary labels, label lists, lineage, exploration cues, parent IDs, prompts, filenames that reveal generation, and old ranks.

Before aggregation, verify that every vote contains every blind ID exactly once, has no ties or unknown IDs, and came from a fresh judge context. Rerun malformed votes with a fresh judge; never repair its ordering in the main context.
