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

1. **Typography** — Family/classification, roles, weights, scale, casing, tracking, line height, text density, fallback, and multilingual behavior.
2. **Color system** — Role-based colors, contrast polarity, distribution, state colors, material relationship, and accessibility.
3. **Composition and hierarchy** — Focal order, grid or compositional skeleton, alignment, density, negative space, crop, and dominant/subordinate ratios.
4. **Shape and geometry** — Corner logic, edge character, silhouette language, proportions, repetition, containers, and framing.
5. **Imagery or subject treatment** — Photography, illustration, diagrams, texture, crop, lighting, perspective, abstraction, and relation to text or UI.
6. **Material and surface** — Paper, glass, ink, grain, pixels, gloss, textile, paint, collage edges, shadows, borders, or deliberate cleanliness.
7. **Distinctive signatures** — Recurring visible motifs that make the direction recognizable without its name.
8. **Avoidances** — Clichés, conflicting treatments, inaccessible patterns, and defaults that would erase distinction.

Send selected considerations to agents with this framing:

> These are experienced attention areas that a strong demo should address where relevant. Use them to make deliberate visual decisions. They are guidance, not predetermined style values and not a form to fill.

## Website Considerations

Select relevant items for a webpage, site, interface, landing page, or product surface.

- **Demo content choice:** choose the page, section mix, content density, and interaction state that best proves the proposed style.
- **Layout system:** page shell, widths, columns, gutters, breakpoints, section rhythm, and asymmetry.
- **Spacing and density:** base unit, compact/comfortable policy, vertical rhythm, information density, and empty-space budget.
- **UI components:** navigation, buttons, cards, forms, tables, charts, modals, filters, and states that belong in the chosen demo.
- **Depth and boundaries:** borders, shadows, elevation, overlap, dividers, translucency, or deliberate flatness.
- **Iconography and marks:** stroke/fill, optical size, metaphor family, diagrams, patterns, ornaments, and badges.
- **Motion and interaction:** hover/focus/press behavior, transitions, scrolling, timing, easing, and reduced-motion fallback.
- **Responsive transformation:** what reflows, collapses, crops, scrolls, or changes hierarchy.
- **Content voice:** label length, capitalization, punctuation, numeric treatment, and copy rhythm.
- **Accessibility and usability:** contrast, focus, text sizing, target sizes, reading order, chart differentiation, and motion limits.
- **Implementation tokens:** variables for type, color, spacing, radius, border, shadow, and motion when they help keep the demo coherent.

The demo creator chooses what to build. Require an isolated, self-contained static demonstration page rather than a complete project. The page may be a hero-plus-components composition, a representative product/detail view, an editorial landing page, a dashboard slice, or another page that makes the style legible. It is a visual proof, not a functioning product prototype.

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
- Do not add JavaScript by default. Show representative interaction states statically or with CSS hover/focus states. Add only minimal local vanilla JavaScript when the user explicitly requires real interaction.
- Let the agent choose representative content and components.
- Render the page in a real browser and capture a primary screenshot at the comparison viewport.
- Capture the same secondary viewport for every candidate only when responsive transformation materially anchors the style.
- Fix broken layout, missing assets, clipping, or unusable contrast before voting.

## Metadata Contract

Keep metadata separate from the primary demo:

```markdown
## Style summary
<one concrete sentence>

## Label list
1. <primary concrete noun or noun phrase>
2. <optional supporting label>

## Demo choice
<what was built and why it exposes the style>

## Lineage
<private stable IDs; never send to judges>
```

Labels are compressed hypotheses. Prefer `railway timetable`, `lacquered control panel`, `tabloid masthead`, `risograph overprint`, or `museum specimen drawer` over adjective-only phrases. One precise label may be sufficient. Every label must have a visible consequence in the demo.

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

Before each evolution round, inspect all unique artifacts created so far, not only the surviving population. Build one concise map of already-covered style territory. For each artifact, summarize only observable features across the relevant anchors: primary label, typography, palette/value structure, composition and density, geometry, imagery, material/depth, interaction treatment, and distinctive signatures. Group near-duplicates and call out saturated combinations. Do not include rank, score, recommendation, lineage, or evaluator comments.

Give the same map to every mutation and crossover agent in that round. Require each agent to return a private `NOVELTY CHECK` before generation that identifies the existing territories it will avoid, its new governing label, and its intended departures. Keep this check out of candidate metadata, fallback voting text, gallery content, and judge context.

Require every offspring to visibly change at least three high-impact axes, including at least one structural axis such as composition/hierarchy, typography system, geometry/silhouette, or imagery/perspective. Palette-only changes, theme inversion, minor spacing changes, small radius adjustments, and component reskins do not satisfy this floor. If the child could be confused with an existing demo at a glance, regenerate it more boldly before voting.

## Mutation and Crossover Semantics

Mutation changes a coherent semantic bundle and makes that change visible in a newly generated/rendered artifact. It must use a new governing label, clear the boldness floor, and depart from both its parent and the complete existing-style map. Useful bundles include typography+density+grid rhythm, palette polarity+material+depth, crop+focal hierarchy+text-image relationship, or geometry+iconography+motion.

Crossover creates a new governing label and coherent visual system from compatible parent logic. It must clear the boldness floor and remain visibly distinct from both parents and the complete existing-style map. It must not collage parent images, split a page into two parent zones, alternate styles section by section, or concatenate label lists. Preserve all hard constraints and reconsider every selected attention area.

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
