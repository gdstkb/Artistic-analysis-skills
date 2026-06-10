---
name: game-art-competitive-analysis
description: Analyze game competitor art from multiple screenshots or video frames, including static visual style, color structure, UI/art direction, single-competitor deep dives, multi-competitor comparisons, adjustment guidance, differentiation risks, and AI art prompts. Use when the user provides competitor game screenshots/video frames or asks for game art competitive analysis, color palette analysis, art style analysis, visual direction adjustment, static art review, or AI prompt generation based on competitor art.
---

# Game Art Competitive Analysis

Use this skill to turn competitor game screenshots or video frames into a complete Markdown art analysis report with actionable art direction and AI art prompts.

## Core Rules

- Output Chinese by default unless the user requests another language.
- Always output a Markdown document, even when the user asks for PPT structure or an art execution brief.
- The report must be complete: competitor art analysis, color structure analysis, adjustment direction, tradeoff analysis, differentiation guidance, and AI prompts.
- Analyze static visuals only. Treat video frames as still images; do not analyze motion timing, animation rhythm, or VFX sequencing.
- Bind important conclusions to screenshot evidence whenever images are available.
- When producing a file-based report from local images, copy and classify the screenshots into an image folder beside the report, then insert Markdown image previews into the report.
- Explain specialist terms and abbreviations at first use, or add a glossary section. For example, write `CTA (Call To Action; primary action button)` instead of unexplained `CTA`.
- Do not directly clone competitor art or write prompts that ask for a specific competitor's exact look. Translate references into abstract art-direction language.
- Differentiation and collision-risk guidance is mandatory, but the user decides whether to follow it.

## Input Handling

1. Collect all screenshots/video frames and label them as `C01`, `C02`, etc.
2. If the images are local files, rename/copy them into a stable report image folder such as `<report-name>_images/` using descriptive names like `C01-gameplay.png`.
3. Do not leave a final report dependent on temporary clipboard paths when a workspace report file is being created.
4. Ask for missing critical context only when it blocks analysis:
   - competitor names or groups
   - interface type for each image
   - target game genre/platform/audience
   - the user's desired adjustment direction
5. If interface labels are missing, infer likely categories such as main screen, gameplay, result screen, shop, character, prop, icon, map, or ad creative.
6. Separate analysis into single-competitor deep dives first, then multi-competitor comparison.

## Workflow

1. **Prepare Evidence**
   - For file-based reports, create an adjacent image asset folder and copy the source images into it with stable `C01`, `C02` filenames.
   - Insert a screenshot preview gallery after the screenshot inventory section.
   - Use Markdown image tags that point to the archived report images. If the viewing environment requires it, use absolute filesystem paths in the image tags.
   - Insert or reference key screenshots in the Markdown report.
   - Use screenshot IDs in every major observation.

2. **Extract Color Data**
   - When local image files are available, run:
     `python scripts/extract_palette.py <image-or-directory> --format markdown`
   - Use the output to discuss dominant colors, accents, lightness, saturation, warm/cool tendency, and color-role structure.
   - If the script cannot run, estimate colors manually and mark them as visual estimates.

3. **Analyze Art Direction**
   - Use `references/analysis-framework.md` for the fixed static analysis dimensions.
   - For each competitor, produce a style DNA summary.
   - For multiple competitors, compare shared category conventions and differentiation opportunities.

4. **Evaluate Adjustment Direction**
   - Use `references/style-axis.md` to translate the user's direction into concrete visual axes.
   - Always state benefits, risks, tradeoffs, and a practical compromise.

5. **Generate AI Art Prompts**
   - Use `references/prompt-recipes.md`.
   - Provide universal English prompts, Chinese explanations, Midjourney variants, SDXL/ComfyUI positive and negative prompts, and DALL-E/ChatGPT natural-language prompts when useful.

6. **Write the Report**
   - Use `references/output-template.md`.
   - If the user asks for PPT structure, write a slide-by-slide Markdown report.
   - If the user asks for an art execution brief, write a Markdown brief while preserving full analysis depth.

## Output Modes

- **Full report**: default mode and always complete.
- **PPT structure**: Markdown organized by slide pages, still with full analysis content.
- **Art execution brief**: Markdown focused on team handoff, still with evidence and prompts.
- **Prompt sheet**: allowed only as an additional section, not as a replacement for the full report unless the user explicitly asks for prompt-only output.

## Required Final Sections

Every complete report must include:

1. Competitor and screenshot inventory with screenshot preview gallery
2. Single-competitor art deep dive
3. Multi-competitor comparison, when multiple competitors exist
4. Color palette and color-structure analysis
5. Style DNA summary
6. User adjustment direction interpretation
7. Professional adjustment guidance with tradeoffs
8. Differentiation and collision-risk guidance
9. AI art prompts
10. Glossary for specialist terms and abbreviations, when any are used
11. Next validation checklist
