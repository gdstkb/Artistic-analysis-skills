# AI Art Prompt Recipes

Generate prompts as art-direction translations, not competitor clones. Avoid naming a competitor as the desired target style unless the user explicitly asks for riskier wording; even then, include a safer abstract alternative.

## Prompt Construction

Build prompts from these blocks:

1. subject: what is being generated
2. game genre and camera/interface context
3. style positioning
4. shape language
5. color structure
6. material and lighting
7. composition and hierarchy
8. production constraints
9. exclusions and collision-risk avoidance

## Universal English Prompt

```text
[Subject] for a [game genre] mobile game, [style positioning], [shape language], [material language], using a color structure of [dominant colors], [secondary colors], and [accent colors], [lighting and rendering], clear gameplay readability, strong silhouette, polished casual game art direction, [composition requirements], avoid direct copying of any existing game's recognizable UI or characters.
```

## Chinese Explanation

```text
目标：生成[对象]，用于[游戏类型/界面]。
风格：强调[风格定位]。
颜色：主色为[主色]，辅助色为[辅助色]，强调色为[强调色]。
造型：使用[圆润/厚重/简洁/尖锐/夸张]的形状语言。
材质：采用[塑料/糖果/黏土/扁平/卡通厚涂]质感。
避撞：不要复刻竞品的角色、UI 布局、图标组合或标志性造型。
```

## Midjourney Variant

```text
[Subject], [game genre] mobile game art, [style positioning], [shape language], [material language], [dominant palette], [accent palette], clean readable composition, strong silhouette, polished casual UI/game asset design, high clarity, no text, no logo, no recognizable existing game character --ar [ratio] --stylize [value] --v 6
```

Use lower stylize values for production-like assets and higher values for mood exploration.

## SDXL Or ComfyUI Variant

Positive:

```text
[subject], [game genre], [style positioning], [shape language], [material], [dominant color], [secondary color], [accent color], clean silhouette, readable mobile game asset, polished casual game art, controlled detail density, consistent lighting, high-quality concept art
```

Negative:

```text
copyrighted character, existing game logo, exact copy, cluttered UI, unreadable icon, muddy colors, over-detailed background, low contrast, noisy texture, distorted text, watermark, realistic photo unless requested
```

## DALL-E Or ChatGPT Image Variant

```text
Create a polished static art direction concept for [subject] in a [game genre] mobile game. Use [style positioning] with [shape language]. The color structure should use [dominant colors] as the main field, [secondary colors] for support, and [accent colors] for rewards or calls to action. The rendering should feel like [material and lighting]. Keep the design readable on a small phone screen. Do not copy any existing game's characters, UI layout, icons, or branded visual identity.
```

## Category Recipes

### Character Or Unit

Include:

- body proportion
- face/eye expression
- silhouette
- costume detail density
- faction/team color coding
- target emotion

### UI Button Or Panel

Include:

- button shape
- corner radius impression
- fill color
- stroke/shadow/highlight
- icon/text hierarchy
- clickability
- reward or monetization emphasis

### Icon Or Prop

Include:

- object function
- silhouette readability
- material
- color role
- outline or shadow rule
- scale readability

### Scene Or Level

Include:

- camera angle
- background complexity
- playable area clarity
- theme
- depth layering
- color separation between interaction and decoration

### Style Exploration Board

Ask for 4 to 8 variations along one axis:

- cuteness
- premium feeling
- color warmth
- detail density
- material richness
- UI depth
- age impression
- genre intensity

## Prompt Quality Checklist

- Does the prompt express the user's adjustment direction?
- Does it use abstract visual language instead of competitor names?
- Does it include color structure?
- Does it include shape and material language?
- Does it specify mobile readability when relevant?
- Does it include negative terms for collision-risk avoidance?
- Does it produce a testable visual direction, not a vague mood?
