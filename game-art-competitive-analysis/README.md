# Game Art Competitive Analysis 使用说明

这是一个用于游戏竞品美术分析的 Codex skill。它会基于多张竞品截图或视频帧，分析竞品的静态美术风格、颜色结构、UI/图标/场景/角色等视觉特点，并结合你的调整方向，输出完整的 Markdown 分析报告、专业调整建议和 AI 美术提示词。

## 适合什么场景

- 分析单个竞品的美术风格特点
- 对比多个竞品的视觉差异
- 拆解竞品的颜色结构、造型语言、UI 风格
- 根据竞品基础制定自己的美术调整方向
- 给美术团队整理执行 Brief
- 生成用于 AI 生图的提示词
- 准备 PPT 汇报结构，但仍以 Markdown 文档输出

## 你需要准备什么

建议准备这些输入：

1. 多张竞品截图或视频帧
2. 每张图对应的界面类型，例如主界面、关卡内、结算页、商店页、角色页
3. 竞品名称，单个或多个都可以
4. 你的目标项目类型、平台和用户群
5. 你的调整方向，例如“更年轻”“更精品”“更清晰”“更差异化”

如果没有完整信息，skill 会先根据已有截图做判断，并标记证据不足的地方。

## 图片归档规则

生成文件型报告时，skill 应该把输入截图复制到报告同级图片目录，并按分析编号重命名，例如：

```text
reports/
  arrow_kinesic_paths_art_analysis_report.md
  arrow_kinesic_paths_images/
    C01-gameplay.png
    C02-congratulations-cashout.png
    C03-extra-rewards.png
```

Markdown 报告需要在截图清单后插入图片预览，直接调用这些归档后的图片显示。不要让最终报告依赖临时剪贴板路径。

## 推荐使用方式

在 Codex 中可以这样说：

```text
使用 $game-art-competitive-analysis 分析这些竞品截图。
目标品类：休闲消除
调整方向：希望在竞品基础上更年轻、更清晰，同时避免和竞品撞脸。
请输出完整 Markdown 报告，并附带 AI 美术提示词。
```

如果要做多个竞品对比，可以这样说：

```text
使用 $game-art-competitive-analysis 对比这三组竞品截图。
请先做单竞品深拆，再做多竞品横向对比。
最后给出我的项目可以采用的差异化美术方向。
```

如果要 PPT 汇报结构：

```text
使用 $game-art-competitive-analysis 分析这些截图。
输出 PPT 汇报结构，但最终仍然生成 Markdown 文档。
```

## 输出内容

默认输出一份完整 Markdown 报告，包含：

1. 竞品与截图清单
2. 单竞品美术深拆
3. 多竞品横向对比
4. 色彩结构分析
5. 风格 DNA 总结
6. 用户调整方向解读
7. 专业调整建议与取舍
8. 差异化与避撞建议
9. AI 美术提示词
10. 下一轮验证清单

报告会尽量把结论绑定到具体截图，例如 `C01 主界面`、`C03 结算页`，避免只做主观评价。

如果报告中出现专业名词或缩写，skill 应当在首次出现时解释，或增加术语说明表。例如：

- CTA：Call To Action，行动召唤/主行动按钮
- HUD：Head-Up Display，游戏主界面上的常驻状态信息
- UI：User Interface，用户界面
- Prompt：给 AI 工具的提示词

## 色彩分析

skill 内置了色板提取脚本：

```powershell
python scripts/extract_palette.py <截图文件或目录> --format markdown
```

脚本会输出：

- 主色 Hex
- 颜色占比
- 平均明度
- 平均饱和度
- 冷暖倾向
- 单图色板
- 多图综合色板

这些数据会用于进一步分析主色、辅助色、强调色、功能色和背景色之间的结构关系。

## AI 美术提示词

报告会提供多种提示词形式：

- 通用英文 Prompt
- 中文解释版
- Midjourney 版本
- SDXL/ComfyUI 正向词和负向词
- DALL-E/ChatGPT 生图版本

提示词会避免直接要求复刻竞品，而是把竞品特征转译成抽象美术语言，例如颜色结构、形状语言、材质光影和 UI 层级。

## 注意事项

- 这个 skill 只分析静态视觉，不分析动画节奏或动效时序。
- 视频帧会被当作静态截图处理。
- 避撞建议是固定输出，但是否执行由使用者决定。
- 如果用户要求 `.pptx` 文件，需要额外说明；默认只输出 Markdown。
- 如果截图数量较多，建议先按竞品和界面类型分文件夹整理。

## 建议文件组织

```text
input/
  competitor-a/
    C01-main.png
    C02-gameplay.png
    C03-result.png
  competitor-b/
    C01-main.png
    C02-gameplay.png
    C03-shop.png
```

这样可以让截图编号、证据引用和横向对比更清晰。

## 安装方法

### Quickstart（30 秒安装）

1. 运行 skills.sh 安装器：

```bash
npx skills@latest add gdstkb/Artistic-analysis-skills
```

2. 选择要安装的 skill：`game-art-competitive-analysis`。

3. 选择要安装到的 coding agent，例如 Codex。

4. 重启 Codex，或开启一个新会话，然后调用：

```text
使用 $game-art-competitive-analysis 分析这些竞品截图。
```

### 手动安装

如果无法使用 `npx skills@latest`，可以从 GitHub 仓库手动复制到本地 skills 目录。

#### Windows PowerShell

```powershell
git clone https://github.com/gdstkb/Artistic-analysis-skills.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".\Artistic-analysis-skills\game-art-competitive-analysis" "$env:USERPROFILE\.codex\skills\"
```

#### macOS / Linux

```bash
git clone https://github.com/gdstkb/Artistic-analysis-skills.git
mkdir -p ~/.codex/skills
cp -R ./Artistic-analysis-skills/game-art-competitive-analysis ~/.codex/skills/
```

如果只需要安装单个 skill，请确认最终目录是 `~/.codex/skills/game-art-competitive-analysis`。
