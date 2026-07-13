# Uploading Research Notes to the Public GitHub Repository

This guide is for maintainers who want to add new research notes without overwriting the existing foundation documents.

## Recommended repository structure

```text
ep-recursive-world-model/
├── README.md
├── README.zh-CN.md
├── LICENSE
├── docs/
│   ├── FOUNDATION.md
│   ├── FOUNDATION.zh-CN.md
│   ├── RESEARCH_ROADMAP.md
│   ├── RESEARCH_ROADMAP.zh-CN.md
│   ├── notes/
│   │   ├── Q001-2026-07-13-collision-statistics-and-scale-mapped-forces.md
│   │   └── Q001-2026-07-13-collision-statistics-and-scale-mapped-forces.zh-CN.md
│   ├── templates/
│   │   ├── NOTE_TEMPLATE.md
│   │   └── NOTE_TEMPLATE.zh-CN.md
│   └── guides/
│       ├── UPLOAD_GUIDE.md
│       └── UPLOAD_GUIDE.zh-CN.md
└── simulations/
```

## Upload through the GitHub website

1. Open the repository.
2. Select **Add file**.
3. Select **Upload files**.
4. Drag the prepared files or folders into the upload area.
5. Check the destination paths carefully.
6. Use a clear commit message, for example:

```text
docs: add bilingual roadmap and Q001 research note
```

7. Commit to the `main` branch if you are the maintainer and the files have already been reviewed.

If the web interface does not preserve folders when they are dragged in, create the folders first and upload each group into its intended folder.

## Upload with Git

After copying the files into a local clone of the repository:

```bash
git status
git add docs
git commit -m "docs: add bilingual roadmap and Q001 research note"
git push origin main
```

## Add links to the README files

Suggested entry for `README.md`:

```markdown
## Research notes

This project develops through public, testable research questions. Notes distinguish postulates, definitions, conjectures, derivations, numerical results, and failed routes.

- [Research roadmap](docs/RESEARCH_ROADMAP.md)
- [Q001: Can collision layers map to long-range attraction, boundary effects, and short-range repulsion?](docs/notes/Q001-2026-07-13-collision-statistics-and-scale-mapped-forces.md)
```

Suggested entry for `README.zh-CN.md`:

```markdown
## 研究笔记

本项目采用逐问题推进的公开研究方式。笔记区分公设、定义、猜想、推导、数值结果和失败路线。

- [研究路线图](docs/RESEARCH_ROADMAP.zh-CN.md)
- [Q001：碰撞层级能否统一映射长程吸引、边界作用与短程斥力？](docs/notes/Q001-2026-07-13-collision-statistics-and-scale-mapped-forces.zh-CN.md)
```

## Before making a public commit

Do not upload:

- passwords;
- personal access tokens;
- API keys;
- email authorization codes;
- private addresses or identity documents;
- copyrighted full texts without permission;
- personal information that should not be permanently public;
- very large raw result folders without a clear data policy.

Recommended public materials include:

- Markdown notes;
- reproducible source code;
- configuration files;
- small example datasets;
- failed-result reports;
- scripts used to generate figures;
- checksums and version information.

## Commit discipline

Each commit should have one clear purpose. Examples:

```text
docs: add Q001 Chinese note
docs: add English translation of Q001
docs: clarify momentum-flux definition
sim: add empty-background conservation audit
results: record failed F1 parameter scan
```

This makes the development of the model easy to review and discuss.

## Participation and permissions

This guide does not grant repository permissions.

Public visitors may read and fork the repository. Contributors should normally propose changes through Issues, Discussions, or Pull Requests. Direct write access to the main repository should be limited to trusted maintainers.
