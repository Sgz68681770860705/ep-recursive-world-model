# 上传到公开GitHub仓库

## 推荐目录

```text
ep-recursive-world-model/
├── README.md
├── README.zh-CN.md
├── FOUNDATION.zh-CN.md
├── docs/
│   ├── RESEARCH_ROADMAP.zh-CN.md
│   └── notes/
│       ├── NOTE_TEMPLATE.zh-CN.md
│       └── 2026-07-13-collision-statistics-and-scale-mapped-forces.zh-CN.md
└── simulations/
```

## 网页上传

1. 打开仓库主页。
2. 点击 **Add file**。
3. 选择 **Upload files**。
4. 上传本包中的 `docs` 文件夹。
5. 提交说明填写：

```text
docs: add research roadmap and Q001 collision-stress note
```

6. 提交到 `main` 分支。

## Git命令上传

把 `docs` 文件夹复制到本地仓库后运行：

```bash
git status
git add docs
git commit -m "docs: add research roadmap and Q001 collision-stress note"
git push origin main
```

## README入口

在 `README.zh-CN.md` 中加入：

```markdown
## 研究笔记

本项目采用逐问题推进的公开研究方式。笔记区分公设、定义、猜想、推导、数值结果和失败路线。

- [研究路线图](docs/RESEARCH_ROADMAP.zh-CN.md)
- [Q001：碰撞层级能否统一映射长程吸引、边界作用与短程斥力？](docs/notes/2026-07-13-collision-statistics-and-scale-mapped-forces.zh-CN.md)
```

## 上传前检查

不要上传密码、API密钥、授权码、私人地址、证件或不希望永久公开的个人资料。

建议上传Markdown笔记、配置文件、可复现代码、小型示例数据、失败报告和图表生成脚本。
