---
name: xdw
description: Use this skill whenever the user wants to read, view, or process a DocuWorks file (.xdw or .xbd). Automatically convert it to PDF first, then read or process the PDF. Trigger on any mention of .xdw files or DocuWorks documents.
---

# DocuWorks (.xdw) File Handling

## Overview

DocuWorks files (`.xdw` / `.xbd`) cannot be read directly by agents or standard
tools. Always convert them to PDF first using `xdwlib`, then process the PDF with
your normal PDF tooling.

## Prerequisites

- **Windows only.** DocuWorks is Fuji Xerox / FUJIFILM Business Innovation software
  that runs on Windows, and `xdwlib` drives the installed DocuWorks engine.
- DocuWorks must be installed on the machine.
- Install xdwlib: `pip install xdwlib`

## Setup

`xdw_to_pdf.py` is included in this skill folder. Use it directly from the skill
directory, or copy it next to your working files.

## How to Convert and Read

### Step 1: Convert .xdw to PDF

```python
import sys
sys.path.insert(0, r"<path/to/the/folder/containing/xdw_to_pdf.py>")
from xdw_to_pdf import convert_xdw_to_pdf

pdf_path = convert_xdw_to_pdf(r"path/to/file.xdw")
# Returns the output PDF path (same location, .pdf extension)
```

Or run it directly from the command line:

```bash
python "<path/to/xdw_to_pdf.py>" "path/to/file.xdw"
# Optional second argument: explicit output path
python "<path/to/xdw_to_pdf.py>" "path/to/file.xdw" "path/to/out.pdf"
```

### Step 2: Read the PDF

After conversion, read the resulting `.pdf` with your normal PDF reader or PDF
skill.

## Key Details

- The output PDF is saved next to the source `.xdw` with a `.pdf` extension unless
  an explicit output path is given.
- Default compression: `MRC_NORMAL` (good balance of quality and file size).

## Compress Options

| Option            | Use case                  |
| ----------------- | ------------------------- |
| `MRC_NORMAL`      | Default, balanced         |
| `MRC_HIGHQUALITY` | When quality matters      |
| `MRC_HIGHCOMPRESS`| When file size matters    |
| `NORMAL`          | Simple raster, no MRC     |
