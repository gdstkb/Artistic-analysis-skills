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

## 使用说明

完整使用说明见：

[game-art-competitive-analysis/README.md](game-art-competitive-analysis/README.md)

## 发布到 GitHub

如果这是一个新仓库，推荐流程：

```powershell
git init
git add README.md .gitignore game-art-competitive-analysis
git commit -m "Add game art competitive analysis skill"
git branch -M main
git remote add origin https://github.com/<your-github-user>/<your-repo>.git
git push -u origin main
```

如果本地仓库已经存在，只需要添加远程仓库并推送：

```powershell
git remote add origin https://github.com/<your-github-user>/<your-repo>.git
git add README.md .gitignore game-art-competitive-analysis
git commit -m "Add game art competitive analysis skill"
git push -u origin main
```

推送前请确认不要提交 `reports/` 目录。
