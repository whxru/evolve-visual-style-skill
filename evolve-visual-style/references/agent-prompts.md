# Clean-Context Demo Agent Prompts

Use these contracts with raw task-local artifacts. Do not leak other candidates to initial generators. Do not leak labels, lineage, prompts, operators, or old ranks to judges.

## Contents

- Shared generator context
- Image demo generator
- Web demo generator
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

RESEARCH DIGEST
<facts, transferable observations, and URLs>

STYLE CONSIDERATIONS
<selected attention areas and preserve/reinterpret/explore status>

Treat these considerations as experienced guidance about areas a strong demo should address where relevant. They are not predetermined style values and not a form to fill.

HARD CONSTRAINTS
<immutable requirements and avoids>

EXPLORATION CUE
<one abstract direction used only to diversify search>

First choose one concrete primary style label and up to six compatible supporting noun phrases. Decide what visual content best proves that style. Create the actual demo. Only after the demo exists, write compact metadata and an objective fallback observation describing what is genuinely visible or implemented. Do not mention other candidates, genetic algorithms, voting, or lineage outside private metadata.
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

Render the page in a real browser at the agreed comparison viewport and save screenshot-primary.png. Create the agreed secondary viewport only when requested for every candidate. Inspect the screenshots and repair broken rendering, missing assets, clipping, unreadable required text, or unusable contrast. The rendered screenshot is the visual ballot artifact; the runnable page is the supporting deliverable. Write metadata.md and fallback.md only after the final render.
```

## Operator Novelty Rules

Insert this block into every mutation and crossover prompt:

```text
EXISTING STYLE AND FEATURE MAP
<artifact-grounded summary of every unique demo created so far, including eliminated demos; no IDs, ranks, scores, lineage, or evaluator comments>

Before creating the artifact, return a concise private NOVELTY CHECK with:
- ALREADY COVERED: the relevant existing style territories and visible feature bundles
- AVOID: the labels, compositions, and visual mechanisms the child must not resemble
- NEW GOVERNING LABEL: one concrete label absent from the map
- BOLD DEPARTURE: at least three high-impact axes that will visibly change, including at least one structural axis

High-impact axes are typography; palette/value structure; composition/grid/density; geometry/component silhouette; imagery/subject treatment; material/depth; and interaction/state presentation. Structural axes are composition/hierarchy, typography system, geometry/silhouette, and imagery/perspective.

Do not create a colorway, theme inversion, minor spacing change, radius adjustment, or component reskin. The child must be unmistakably different from every mapped demo at a glance while still satisfying the user brief and hard constraints. If the first render remains similar, regenerate it more boldly before returning it. Keep the NOVELTY CHECK out of user-facing files, fallback voting copy, and judge context.
```

## Mutation Prompt

```text
Create one substantial visual mutation for the same brief.

USER BRIEF
<brief>

RESEARCH DIGEST
<digest>

STYLE CONSIDERATIONS AND HARD CONSTRAINTS
<unchanged guidance and constraints>

PARENT ARTIFACT
<one image, or one screenshot set plus web demo source>

PARENT METADATA
<summary and labels only>

Apply the Operator Novelty Rules above before creation. Change the primary label or one coherent label bundle, then make that semantic change plainly observable in a newly generated image or newly rendered demo page. Preserve useful parent logic, every hard constraint, and deliberate treatment of the full consideration list, but depart substantially from both the parent and every style in the existing map. Clear the boldness floor; do not merely rename, recolor, or describe a variant. Return a new demo artifact, then new metadata and fallback text. Do not mention mutation, parentage, ranking, evaluation, or the novelty check in user-facing files.

For a web child, preserve the lightweight static-page contract: plain HTML/CSS, directly openable from disk, no framework, dependencies, build step, server, backend, deployment, or hosting. Keep JavaScript absent unless the user explicitly required real interaction; then use only minimal local vanilla JavaScript.
```

## Crossover Prompt

```text
Create one coherent new visual demo from two source candidates for the same brief.

USER BRIEF
<brief>

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

Apply the Operator Novelty Rules above before creation. Invent one new primary label that names a unified visual model and is absent from the existing map. Select compatible high-value logic from both sources, then generate/render an artifact that is unmistakably different from both parents and every mapped style. Clear the boldness floor. Do not collage parent screenshots, divide the page into parent halves, concatenate label lists, average values mechanically, or preserve contradictions. Reconsider every style consideration and preserve all hard constraints. Return the new demo first, then metadata and fallback text. Do not mention crossover, sources, lineage, ranking, evaluation, or the novelty check in user-facing files.

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
2. STRENGTH OF STYLIZATION — 50%. Judge whether the visible demo establishes a strong, coherent, recognizable visual language. Reward deliberate, mutually reinforcing choices across relevant considerations. Penalize generic templates, timid defaults, superficial recoloring, disconnected effects, and style names unsupported by visible evidence.

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

Use exactly the same two-part, 50/50 rubric as the visual jury: fidelity to the user's original input and strength of stylization. Treat feasibility, accessibility, composition, distinctiveness, and consideration coverage only as evidence inside those two criteria. Lower confidence when an important point is not evidenced. A material hard-constraint violation cannot outrank a compliant candidate merely for stronger styling. Return a strict RANKING line, then for every blind ID provide one `Original-input fidelity` reason and one `Stylization strength` reason. Use each ID once. Do not output extra scoring categories, scores, ties, revisions, labels, or authorship speculation.
```

## Blindness and Vote Validation

For every judge, create a fresh random permutation and temporary labels such as `Option K`, `Option R`, and `Option V`. Keep the mapping private. Strip candidate IDs, primary labels, label lists, lineage, exploration cues, parent IDs, prompts, filenames that reveal generation, and old ranks.

Before aggregation, verify that every vote contains every blind ID exactly once, has no ties or unknown IDs, and came from a fresh judge context. Rerun malformed votes with a fresh judge; never repair its ordering in the main context.
