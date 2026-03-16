#!/usr/bin/env python3
"""Render vector PDF figures into high-resolution PNG images for the web page.

This script uses macOS Quick Look (`qlmanage`) to rasterize PDFs at a high size.
It is designed for this repository layout:
  - source PDFs: HEAR/images/*.pdf
  - output PNGs: web/HEAR-Web/static/images/*.png
"""

from __future__ import annotations

import argparse
import subprocess
import tempfile
from pathlib import Path

from PIL import Image


REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_SRC_DIR = REPO_ROOT / "HEAR" / "images"
DEFAULT_DST_DIR = REPO_ROOT / "web" / "HEAR-Web" / "static" / "images"


def render_pdf_to_png(pdf_path: Path, dst_path: Path, quicklook_size: int, max_side: int) -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_dir_path = Path(tmp_dir)
        cmd = [
            "qlmanage",
            "-t",
            "-s",
            str(quicklook_size),
            "-o",
            str(tmp_dir_path),
            str(pdf_path),
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        rendered = tmp_dir_path / f"{pdf_path.name}.png"
        if not rendered.exists():
            raise FileNotFoundError(f"Quick Look did not render output for: {pdf_path}")

        image = Image.open(rendered).convert("RGBA")

        width, height = image.size
        longest = max(width, height)
        if longest > max_side:
            scale = max_side / float(longest)
            new_size = (int(width * scale), int(height * scale))
            image = image.resize(new_size, resample=Image.Resampling.LANCZOS)

        dst_path.parent.mkdir(parents=True, exist_ok=True)
        image.save(dst_path, format="PNG", optimize=True, compress_level=3)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--src-dir",
        type=Path,
        default=DEFAULT_SRC_DIR,
        help="Directory containing source PDF figures.",
    )
    parser.add_argument(
        "--dst-dir",
        type=Path,
        default=DEFAULT_DST_DIR,
        help="Directory to write output PNG figures.",
    )
    parser.add_argument(
        "--quicklook-size",
        type=int,
        default=4800,
        help="Quick Look render size passed to qlmanage -s.",
    )
    parser.add_argument(
        "--max-side",
        type=int,
        default=3200,
        help="Maximum side length of output PNG after optional downscaling.",
    )
    parser.add_argument(
        "names",
        nargs="*",
        help=(
            "Optional figure base names (without extension). "
            "If omitted, all PDFs in src-dir are rendered."
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    src_dir = args.src_dir.resolve()
    dst_dir = args.dst_dir.resolve()

    if not src_dir.exists():
        raise FileNotFoundError(f"Source directory not found: {src_dir}")

    if args.names:
        pdf_paths = [src_dir / f"{name}.pdf" for name in args.names]
    else:
        pdf_paths = sorted(src_dir.glob("*.pdf"))

    if not pdf_paths:
        raise RuntimeError(f"No PDF files found in: {src_dir}")

    for pdf_path in pdf_paths:
        if not pdf_path.exists():
            raise FileNotFoundError(f"Missing PDF: {pdf_path}")
        dst_path = dst_dir / f"{pdf_path.stem}.png"
        render_pdf_to_png(
            pdf_path=pdf_path,
            dst_path=dst_path,
            quicklook_size=args.quicklook_size,
            max_side=args.max_side,
        )
        print(f"Rendered: {pdf_path.name} -> {dst_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()

