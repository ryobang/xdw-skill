# DocuWorks (.xdw) Skill

An [agent skill](https://skills.sh) that lets AI coding agents read and process
**DocuWorks** files (`.xdw` / `.xbd`). DocuWorks files cannot be read directly,
so this skill converts them to PDF first (via `xdwlib`), then hands off to your
normal PDF tooling.

## Install

```bash
npx skills add ryobang/xdw-skill
```

Works with Claude Code, Cursor, Codex, and every other agent supported by the
[`skills` CLI](https://github.com/vercel-labs/skills).

## What it does

- Triggers on any mention of `.xdw` / `.xbd` files or DocuWorks documents.
- Converts the file to PDF (default compression `MRC_NORMAL`).
- Lets the agent read or further process the resulting PDF.

## Requirements

- **Windows only** — DocuWorks (FUJIFILM Business Innovation) must be installed.
- `pip install xdwlib`

## Contents

```
skills/
  xdw/
    SKILL.md        # Skill definition (frontmatter + instructions)
    xdw_to_pdf.py   # Conversion helper
```

## License

[MIT](./LICENSE)
