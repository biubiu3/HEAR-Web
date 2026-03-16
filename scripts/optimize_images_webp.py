#!/usr/bin/env python3
"""Generate optimized WebP assets for the project page images.

Default behavior:
1) Parse `index.html` and collect referenced images in `static/images`.
2) Convert referenced PNG/JPG files to `.webp`.
3) Keep important diagrams and logos in lossless mode for clarity.

Examples:
  python3 scripts/optimize_images_webp.py
  python3 scripts/optimize_images_webp.py --all
  python3 scripts/optimize_images_webp.py --max-side 2400
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from PIL import Image


REPO_ROOT = Path(__file__).resolve().parents[1]
INDEX_HTML = REPO_ROOT / "index.html"
IMAGE_DIR = REPO_ROOT / "static" / "images"

# Figures with text/lines and logos: keep lossless to avoid visible artifacts.
LOSSLESS_BASENAMES = {
    "headpic",
    "overview",
    "Historizer",
    "Envisioner",
    "Advancer",
    "logo2",
    "logo3",
}

# Do not convert browser tab icon via this script.
SKIP_NAMES = {"favicon.ico"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all", action="store_true", help="Convert all PNG/JPG files under static/images.")
    parser.add_argument("--max-side", type=int, default=2600, help="Downscale images whose longest side exceeds this value.")
    parser.add_argument("--lossy-quality", type=int, default=88, help="Quality for lossy WebP.")
    parser.add_argument("--lossless-quality", type=int, default=100, help="Effort/quality for lossless WebP.")
    return parser.parse_args()


def source_for_referenced(name: str) -> Path | None:
    referenced = IMAGE_DIR / name
    suffix = referenced.suffix.lower()
    if suffix in {".png", ".jpg", ".jpeg"}:
        return referenced
    if suffix == ".webp":
        # If page already uses WebP, regenerate from original raster sources when present.
        for ext in (".png", ".jpg", ".jpeg"):
            candidate = referenced.with_suffix(ext)
            if candidate.exists():
                return candidate
    return None


def collect_from_index(index_html: Path) -> list[Path]:
    content = index_html.read_text(encoding="utf-8")
    pattern = re.compile(r"static/images/([A-Za-z0-9_.-]+\.(?:png|jpg|jpeg|webp))", flags=re.IGNORECASE)
    names = sorted(set(pattern.findall(content)))
    sources: list[Path] = []
    for name in names:
        if name in SKIP_NAMES:
            continue
        src = source_for_referenced(name)
        if src is not None:
            sources.append(src)
    return sorted(set(sources))


def collect_all_images() -> list[Path]:
    files = sorted(
        list(IMAGE_DIR.glob("*.png"))
        + list(IMAGE_DIR.glob("*.jpg"))
        + list(IMAGE_DIR.glob("*.jpeg"))
    )
    return [p for p in files if p.name not in SKIP_NAMES]


def maybe_downscale(image: Image.Image, max_side: int) -> Image.Image:
    width, height = image.size
    longest = max(width, height)
    if longest <= max_side:
        return image
    scale = max_side / float(longest)
    new_size = (int(width * scale), int(height * scale))
    return image.resize(new_size, resample=Image.Resampling.LANCZOS)


def convert_one(src: Path, max_side: int, lossy_quality: int, lossless_quality: int) -> tuple[Path, float, float]:
    basename = src.stem
    lossless = basename in LOSSLESS_BASENAMES
    dst = src.with_suffix(".webp")

    with Image.open(src) as image:
        # Keep alpha when present.
        if image.mode not in ("RGB", "RGBA"):
            image = image.convert("RGBA" if "A" in image.getbands() else "RGB")
        image = maybe_downscale(image, max_side=max_side)
        image.save(
            dst,
            format="WEBP",
            method=6,
            lossless=lossless,
            quality=lossless_quality if lossless else lossy_quality,
            optimize=True,
        )

    before_mb = src.stat().st_size / (1024 * 1024)
    after_mb = dst.stat().st_size / (1024 * 1024)
    return dst, before_mb, after_mb


def main() -> None:
    args = parse_args()
    if args.all:
        sources = collect_all_images()
    else:
        sources = collect_from_index(INDEX_HTML)

    if not sources:
        print("No source images found.")
        return

    total_before = 0.0
    total_after = 0.0
    print(f"Converting {len(sources)} image(s) to WebP...")
    for src in sources:
        if not src.exists():
            print(f"[SKIP] Missing: {src.relative_to(REPO_ROOT)}")
            continue
        dst, before_mb, after_mb = convert_one(
            src=src,
            max_side=args.max_side,
            lossy_quality=args.lossy_quality,
            lossless_quality=args.lossless_quality,
        )
        total_before += before_mb
        total_after += after_mb
        ratio = (after_mb / before_mb) if before_mb > 0 else 1.0
        print(
            f"[OK] {src.name} -> {dst.name} | "
            f"{before_mb:.2f}MB -> {after_mb:.2f}MB ({ratio:.1%})"
        )

    if total_before > 0:
        print(
            f"Total: {total_before:.2f}MB -> {total_after:.2f}MB "
            f"({(total_after / total_before):.1%})"
        )


if __name__ == "__main__":
    main()
