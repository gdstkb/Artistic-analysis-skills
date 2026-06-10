<<<<<<< HEAD
# Game Art Competitive Analysis Skill

这是一个用于游戏竞品美术分析的 Codex skill。它可以基于多张竞品截图或视频帧，输出完整 Markdown 报告，包括静态美术风格、颜色结构、UI/图标/场景/角色分析、调整方向建议、避撞建议和 AI 美术提示词。

## 仓库内容

```text
game-art-competitive-analysis/
  SKILL.md
  README.md
  agents/openai.yaml
  references/
  scripts/extract_palette.py
```

`reports/` 是本地分析输出目录，通常不建议推送到公开仓库，因为里面可能包含竞品截图、内部分析和项目资料。

## 安装方法

### Windows PowerShell

```powershell
git clone https://github.com/<your-github-user>/<your-repo>.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".\<your-repo>\game-art-competitive-analysis" "$env:USERPROFILE\.codex\skills\"
```

### macOS / Linux

```bash
git clone https://github.com/<your-github-user>/<your-repo>.git
mkdir -p ~/.codex/skills
cp -R ./<your-repo>/game-art-competitive-analysis ~/.codex/skills/
```

安装后重启 Codex，或开启一个新会话，然后使用：

```text
使用 $game-art-competitive-analysis 分析这些竞品截图。
```


推送前请确认不要提交 `reports/` 目录。
=======
# Artistic-analysis-skills
>>>>>>> f7d32fb39bfda5fa18015746df4eba7044ed4d98
