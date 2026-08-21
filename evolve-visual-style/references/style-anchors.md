# Style Consideration Framework

Use this framework to extract experienced attention areas that should be sent to every demo creator. These are not a document schema and do not prescribe values. They help an agent decide which visual mechanisms deserve deliberate treatment in the actual demo.

## Contents

- Core considerations
- Website considerations
- Image considerations
- Existing-artifact status
- Demo artifact contract
- Metadata contract
- Fallback description schema
- Existing-style map and boldness floor
- Mutation and crossover semantics
- Web gallery ledger and manifest

## Core Considerations

Always consider these areas and select the ones that materially affect the artifact.

1. **Domain archetype** — The real-world kind of artifact, its audience relationship, trust mechanism, task, content model, and reading or conversion flow.
2. **Page or composition archetype** — The structural family, spatial topology, navigation or reading model, content flow, and viewport relationship.
3. **Typography** — Family/classification, roles, weights, scale, casing, tracking, line height, text density, fallback, and multilingual behavior.
4. **Color system** — Role-based colors, contrast polarity, distribution, state colors, material relationship, and accessibility.
5. **Composition and hierarchy** — Focal order, grid or compositional skeleton, alignment, density curve, negative-space topology, crop, and dominant/subordinate ratios.
6. **Shape and geometry** — Corner logic, edge character, silhouette language, proportions, repetition, container grammar, and framing.
7. **Imagery or subject treatment** — Photography, illustration, diagrams, texture, crop, lighting, perspective, abstraction, medium, narrative role, and relation to text or UI.
8. **Material and surface** — Paper, glass, ink, grain, pixels, gloss, textile, paint, collage edges, shadows, borders, or deliberate cleanliness.
9. **Visual intent and asset strategy** — The design thesis, subject-specific brand idea, concept spine, primary medium, asset role, framing, and one optional second-read moment.
10. **Distinctive signatures** — Recurring visible motifs that make the direction recognizable without its name.
11. **Avoidances** — Clichés, conflicting treatments, inaccessible patterns, model-prior defaults, and mechanisms that would erase distinction or domain credibility.

Send selected considerations to agents with this framing:

> These are experienced attention areas that a strong demo should address where relevant. Use them to make deliberate visual decisions. They are guidance, not predetermined style values and not a form to fill.

## Website Considerations

Select relevant items for a webpage, site, interface, landing page, or product surface.

- **Genre authenticity:** make the result first read as a plausible commercial site, academic profile, publication, product surface, archive, or other brief-specific domain—not as a generic design board with replaced copy.
- **Demo content choice:** choose the page, section mix, content density, scroll depth, and interaction state that best proves the proposed style. Preserve required content roles without forcing identical components or first-screen placement across candidates.
- **Page archetype and content flow:** decide whether the proof is narrative, editorial, transactional, spatial, indexical, tool-centered, archival, or another domain-appropriate form; define how identity, task, evidence, and action unfold.
- **Layout and spatial topology:** page shell, continuous or segmented space, widths, columns, gutters, layers, breakpoints, section rhythm, asymmetry, and relationship to the viewport.
- **Spacing and density:** base unit, compact/comfortable policy, vertical rhythm, information density, and empty-space budget.
- **Section rhythm:** the sequence of composition families, density, image-to-text ratio, focal scale, material/background mode, and transitions across major zones.
- **Component and container grammar:** navigation, buttons, cards, forms, tables, charts, modals, filters, states, container dependence, repetition, and edge relationships. Do not assume cards, bars, or equal grids.
- **Depth and boundaries:** borders, shadows, elevation, overlap, dividers, translucency, or deliberate flatness.
- **Image medium and role:** photography, generated imagery, illustration, collage, inline SVG, diagrams, 3D, texture, or type-only composition; decide whether imagery is evidence, atmosphere, explanation, navigation, or ornament.
- **Iconography and marks:** stroke/fill, optical size, metaphor family, diagrams, patterns, ornaments, and badges.
- **Motion and interaction:** hover/focus/press behavior, transitions, scrolling, timing, easing, and reduced-motion fallback.
- **Responsive transformation:** what reflows, collapses, crops, scrolls, or changes hierarchy.
- **Content voice:** label length, capitalization, punctuation, numeric treatment, and copy rhythm.
- **Accessibility and usability:** contrast, focus, text sizing, target sizes, reading order, chart differentiation, and motion limits.
- **Implementation tokens:** variables for type, color, spacing, radius, border, shadow, and motion when they help keep the demo coherent.

The demo creator chooses what to build. Require an isolated, self-contained static demonstration page rather than a complete project. The page may be a narrative homepage, representative product/detail view, editorial landing page, spatial composition, index, dashboard slice, or another domain-authentic page that makes the style legible. Do not default to a hero-plus-components board. It is a visual proof, not a functioning product prototype.

## Image Considerations

Select relevant items for a generated image, illustration, poster, or visual composition.

- **Canvas and framing:** aspect ratio, orientation, margins, bleed, safe zones, and framing device.
- **Subject hierarchy:** roster, focal point, relative scale, occlusion, gesture, and directional flow.
- **Camera and perspective:** distance, angle, lens character, vanishing behavior, distortion, and depth compression.
- **Lighting and value:** key/fill relationship, shadow hardness, value grouping, highlight policy, and atmosphere.
- **Rendering grammar:** photographic, vector, painterly, bitmap, low-poly, ink, collage, 3D, or mixed media.
- **Text-image relationship:** placement, overlap, masks, caption behavior, and reading sequence.
- **Output constraints:** resolution, display/print context, color space, transparency, and legibility distance.

Require an actually generated image. A prompt, blueprint, or written specification is not a candidate.

## Existing-Artifact Status

For a restyle, mark each selected consideration:

- `preserve` — fixed identity or hard constraint
- `reinterpret` — preserve the role but allow a new treatment
- `explore` — open visual search axis

Do not mistake implementation accidents for identity. Pass these statuses to every agent.

## Demo Artifact Contract

### Image candidate

- Save one generated image in a standard format.
- Use the same requested ratio and comparable resolution across candidates.
- Inspect the output when visual inspection is available.
- Repair only objective failures such as missing required subjects, unreadable required text, corrupt output, or broken framing.

### Web candidate

- Save one lightweight static demo that opens directly from disk, normally one `index.html` plus embedded or minimal local CSS and local assets.
- Use plain HTML/CSS. Do not use frontend frameworks, package managers, dependency manifests, build tools, local servers, routing, APIs, backends, authentication, databases, analytics, deployment, hosting, or production integrations.
- Treat static delivery as a runtime boundary, not a CSS-only visual limitation. Use self-contained local photography, generated imagery, illustration, textures, licensed local fonts, or inline SVG when they materially establish the direction.
- Do not add JavaScript by default. Show representative interaction states statically or with CSS hover/focus states. Add only minimal local vanilla JavaScript when the user explicitly requires real interaction.
- Let the agent choose representative content and components. Preserve required content roles without requiring every candidate to use the same component inventory, card count, or above-the-fold compression.
- Make the result resemble a plausible page in the requested domain. Do not deliver a component specimen or posterized dashboard unless requested.
- Render the page in a real browser and capture a primary screenshot at the comparison viewport.
- Capture the same secondary viewport for every candidate only when responsive transformation materially anchors the style.
- Fix broken layout, missing assets, clipping, or unusable contrast before voting.
- Complete the screenshot-grounded finish audit in [visual-finish.md](visual-finish.md) before the population convergence audit.

## Metadata Contract

Keep metadata separate from the primary demo:

```markdown
## Style summary
<one concrete sentence>

## Design thesis
<what the visitor should first notice or feel and how the artifact causes it>

## Brand idea
<why this visual argument belongs to this entity, subject, or product>

## Label list
1. <primary concrete noun or noun phrase>
2. <optional supporting label>

## Demo choice
<what was built and why it exposes the style>

## Asset strategy
<primary medium, role, crop/framing, and treatment>

## Concept spine and second-read moment
<one governing idea and at most one subtle supporting detail>

## Section rhythm
<observed major-zone rhythm for web; omit for a single image>

## Lineage
<private stable IDs; never send to judges>
```

Labels are compressed hypotheses. Prefer `railway timetable`, `lacquered control panel`, `tabloid masthead`, `risograph overprint`, or `museum specimen drawer` over adjective-only phrases. One precise label may be sufficient. Every label must have a visible consequence in the demo.

After rendering, also write the observed `style-genome.json` defined in [diversity-control.md](diversity-control.md). The label may summarize the result but never proves novelty or structural distance.

## Fallback Description Schema

Create this only after the demo exists. It is not the candidate representation and must never contain intended features missing from the artifact.

```markdown
# Anonymous demo observation

## Visible overview
<literal description of the rendered image or screenshot>

## Evidence by style consideration
- <consideration>: <visible or implemented evidence>

## Composition and focal order
<what is dominant, secondary, and tertiary>

## Color, type, geometry, imagery, and surface
<specific observed treatment>

## Interaction and responsive evidence
<only what the web demo actually implements; use not shown when absent>

## Hard-constraint check
<pass/fail with visible evidence>

## Apparent strengths and risks
<observations, not sales language>
```

Do not include style labels, candidate ID, lineage, parentage, exploration cue, generator rationale, or aspirational implementation notes in the voting copy.

## Existing-Style Map and Boldness Floor

Before each evolution round, inspect all unique artifacts created so far, not only the surviving population. Build one concise map of already-covered style territory. For each artifact, summarize only observable features across the relevant anchors: domain/page archetype, spatial topology, content flow, navigation, container grammar, whitespace/density, typography, palette/value distribution, image medium and role, geometry, material/depth, interaction treatment, and distinctive signatures. Group near-duplicates and name their shared compound grammar. Do not include rank, score, recommendation, lineage, or evaluator comments.

Give the same map to every mutation and crossover agent in that round. Require each agent to return a private `NOVELTY CHECK` before generation that identifies the existing territories it will avoid, its new governing label, and its intended departures. Keep this check out of candidate metadata, fallback voting text, gallery content, and judge context.

Require every offspring to break the relevant shared compound grammar and visibly change at least three high-impact axes. It must change a page-level structural axis—page archetype, spatial topology, or content flow—plus container grammar, and at least one of typography system, image medium/role, depth/material, or interaction model. Palette-only changes, theme inversion, minor spacing changes, small radius adjustments, and component reskins do not satisfy this floor. If the child could be confused with an existing demo at a glance or could exchange its label with one, regenerate it more boldly before voting.

## Mutation and Crossover Semantics

Mutation changes a coherent generative bundle and makes that change visible in a newly generated/rendered artifact. It must use a new governing label, clear the structural boldness floor, and depart from both its parent and the complete existing-style map. Useful bundles include page archetype+content flow+container grammar, spatial topology+image medium+whitespace model, or navigation model+typography system+interaction metaphor.

Crossover creates a new governing label and coherent visual system from compatible parent logic. It must synthesize principles rather than average surfaces, clear the structural boldness floor, and remain visibly distinct from both parents and the complete existing-style map. It must not collage parent images, split a page into two parent zones, alternate styles section by section, or concatenate label lists. Preserve all hard constraints and reconsider every selected attention area.

## Web Gallery Ledger and Manifest

Record every unique web demo exactly once. Assign immutable values when it is created:

- `index`: global 1-based integer shown to the user
- `candidate_id`: stable internal ID
- `generation`: generation in which the artifact was first created
- `created_order`: global monotonic creation order
- `thumbnail`: relative path to its real rendered screenshot
- `href`: relative path to its runnable `index.html`

After the candidate's first evaluation, record `rank`, `score`, `first_place_votes`, and `rank_sum`. Append subsequent results to `rank_history` rather than replacing creation metadata. Add a human-readable `recommendation` status at completion.

Use this gallery manifest shape:

```json
{
  "title": "Visual Style Evolution",
  "subtitle": "All generated web demos",
  "candidates": [
    {
      "index": 1,
      "candidate_id": "g0-c01",
      "generation": 0,
      "created_order": 1,
      "label": "primary style label",
      "summary": "compact visible summary",
      "rank": 2,
      "score": 16,
      "first_place_votes": 1,
      "recommendation": "Eliminated",
      "thumbnail": "candidates/g0-c01/screenshot-primary.png",
      "href": "candidates/g0-c01/index.html"
    }
  ]
}
```

Keep paths relative to the gallery homepage. Do not place lineage, prompts, evaluator reasons, or hidden candidate IDs beyond the stable public index in the visible card.

Build the gallery itself as one dependency-free static HTML/CSS page that opens directly from disk. Do not add JavaScript, a framework, a build step, a local server, deployment, or hosting work.
