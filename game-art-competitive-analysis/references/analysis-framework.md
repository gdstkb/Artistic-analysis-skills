# Static Game Art Analysis Framework

Use this framework for competitor screenshots and video frames. Analyze only static visual evidence.

## Evidence Rules

- Number images as `C01`, `C02`, etc.
- For file-based reports, archive local screenshots beside the report in a stable image folder before referencing them.
- Insert screenshot previews in the report so visual evidence can be reviewed inline.
- Avoid final Markdown reports that depend on temporary clipboard image paths.
- Record competitor name, interface type, and visible subject for each image.
- Tie major conclusions to screenshot IDs.
- If evidence is missing, write `evidence insufficient` instead of guessing.
- Separate observable facts from professional interpretation.

## Single-Competitor Deep Dive

### 1. Style Positioning

Identify the visual market position:

- casual, hyper-casual, midcore, hardcore, premium, toy-like, cartoon, realistic, stylized 3D, anime, low-poly, flat 2D, painterly
- target age impression
- emotional tone: cute, energetic, relaxing, tense, luxurious, funny, chaotic, clean
- production impression: lightweight, boutique, mass-market, ad-driven, live-ops heavy

### 2. Color System

Analyze color by structure, not only impression:

- dominant background colors
- primary gameplay/object colors
- secondary support colors
- accent and reward colors
- functional UI colors
- warning/negative/action colors
- saturation range
- lightness range
- warm/cool tendency
- contrast strategy
- palette consistency across screens

Use script data when available:

- dominant Hex values
- color percentages
- average lightness
- average saturation
- warm/cool tendency

### 3. Shape Language

Look for repeated form grammar:

- round vs angular
- thick vs thin
- soft vs sharp
- chunky vs elegant
- toy-like vs realistic
- exaggerated proportions
- silhouette readability
- outline usage
- corner radius and bevel patterns

### 4. Composition And Visual Hierarchy

Analyze how the screen guides attention:

- focal point placement
- foreground/midground/background separation
- information density
- contrast hierarchy
- reward/CTA emphasis
- gameplay readability
- empty space usage
- whether UI competes with gameplay content

### 5. Material And Lighting

Identify rendering language:

- flat color
- gradient volume
- toon shading
- plastic, clay, jelly, candy, metal, glass, wood, fabric, stone
- outline/shadow/highlight usage
- ambient occlusion
- rim light
- specular highlights
- softness or hardness of light

### 6. Character Or Unit Design

Use when screenshots include characters, enemies, units, avatars, mascots, or living objects:

- proportion
- face/eye/mouth language
- expression intensity
- costume and accessory detail
- silhouette clarity
- team/faction color coding
- emotional readability

### 7. Scene Or Level Visuals

Use for maps, boards, levels, background scenes, and gameplay spaces:

- camera angle
- terrain/block/grid readability
- depth layering
- background complexity
- theme consistency
- object placement density
- playable vs decorative separation

### 8. UI, Icons, And Buttons

Analyze interface craft:

- button shape, size, depth, and clickability
- icon silhouette and readability
- text contrast
- panel style
- stroke, shadow, glow, bevel, highlight
- color coding
- currency/reward display
- screen flow clarity
- monetization element prominence

### 9. Differentiation And Collision Risk

Identify what is safe to learn and what is risky:

- safe abstract principles
- risky near-copy elements
- distinctive competitor identifiers
- IP-sensitive motifs
- visual combinations that create a too-similar impression
- recommended ways to diverge

## Multi-Competitor Comparison

After deep-diving each competitor, compare:

- shared category conventions
- strongest visual differentiators
- color-positioning map
- style maturity level
- UI density and monetization emphasis
- readability vs richness tradeoff
- production-cost implications
- whitespace in the market: underused colors, themes, materials, or UI approaches

## Style DNA Summary

Write each competitor's style DNA as a compact formula:

`audience tone + color structure + shape language + material language + UI hierarchy + differentiator`

Example:

`young casual + high-lightness candy palette + rounded chunky shapes + glossy plastic highlights + oversized CTA buttons + strong reward color concentration`
