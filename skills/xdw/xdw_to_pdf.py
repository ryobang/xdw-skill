"""
Convert a DocuWorks (.xdw) file to PDF.

Uses xdwlib: https://xdwlib.readthedocs.io/

Prerequisites:
  - DocuWorks must be installed (Windows only).
  - pip install xdwlib
"""

import xdwlib
from pathlib import Path


def convert_xdw_to_pdf(xdw_path: str, output_path: str | None = None) -> str:
    """
    Convert a .xdw file to PDF.

    Args:
        xdw_path: Path to the input .xdw file.
        output_path: Output PDF path. Defaults to the same name with a .pdf suffix.

    Returns:
        The output PDF path as a string.
    """
    xdw_path = Path(xdw_path)
    if output_path is None:
        output_path = xdw_path.with_suffix(".pdf")
    else:
        output_path = Path(output_path)

    with xdwlib.xdwopen(str(xdw_path)) as doc:
        total_pages = doc.pages
        print(f"Pages: {total_pages}")

        # Export every page into a single PDF (pos is a half-open slice range).
        result = doc.export_image(
            pos=(0, total_pages),
            path=str(output_path),
            format="PDF",
            compress="MRC_NORMAL",
        )

    print(f"Done: {result}")
    return result


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python xdw_to_pdf.py <input.xdw> [output.pdf]")
        sys.exit(1)

    src = sys.argv[1]
    dst = sys.argv[2] if len(sys.argv) >= 3 else None
    convert_xdw_to_pdf(src, dst)
