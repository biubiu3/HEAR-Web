#!/usr/bin/env python3
"""
Compress oversized MP4 files for GitHub Pages hosting.

Usage examples:
  python3 scripts/compress_videos.py
  python3 scripts/compress_videos.py --max-mb 48 --target-mb 42
  python3 scripts/compress_videos.py --files static/videos/alarm_all.mp4 static/videos/telephone_all.mp4
"""

from __future__ import annotations

import argparse
import json
import math
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Iterable


VIDEO_DIR = Path("static/videos")


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, check=True, text=True, capture_output=True)


def ffprobe_json(path: Path) -> dict:
    result = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-print_format",
            "json",
            "-show_format",
            "-show_streams",
            str(path),
        ]
    )
    return json.loads(result.stdout)


def seconds_of(path: Path) -> float:
    probe = ffprobe_json(path)
    duration = probe.get("format", {}).get("duration")
    if duration is None:
        raise RuntimeError(f"Cannot read duration from {path}")
    return float(duration)


def size_mb(path: Path) -> float:
    return path.stat().st_size / (1024 * 1024)


def even(value: int) -> int:
    return value if value % 2 == 0 else value - 1


def estimate_video_bitrate_kbps(duration_s: float, target_mb: float, audio_kbps: int) -> int:
    target_bits = target_mb * 1024 * 1024 * 8
    total_kbps = target_bits / duration_s / 1000
    overhead_kbps = 96
    video_kbps = int(total_kbps - audio_kbps - overhead_kbps)
    return max(video_kbps, 450)


def encode_once(
    input_path: Path,
    output_path: Path,
    video_kbps: int,
    audio_kbps: int,
    max_width: int,
    preset: str,
) -> None:
    scale = f"scale='min({max_width},iw)':-2"
    cmd = [
        "ffmpeg",
        "-y",
        "-hide_banner",
        "-loglevel",
        "error",
        "-i",
        str(input_path),
        "-vf",
        scale,
        "-r",
        "30",
        "-c:v",
        "libx264",
        "-preset",
        preset,
        "-profile:v",
        "high",
        "-pix_fmt",
        "yuv420p",
        "-b:v",
        f"{video_kbps}k",
        "-maxrate",
        f"{int(video_kbps * 1.20)}k",
        "-bufsize",
        f"{int(video_kbps * 2.0)}k",
        "-c:a",
        "aac",
        "-b:a",
        f"{audio_kbps}k",
        "-movflags",
        "+faststart",
        str(output_path),
    ]
    run(cmd)


def iter_targets(initial_kbps: int, attempts: int) -> Iterable[int]:
    factors = [1.00, 0.88, 0.78, 0.68, 0.58]
    for idx in range(attempts):
        factor = factors[idx] if idx < len(factors) else factors[-1] * (0.93 ** (idx - len(factors) + 1))
        yield max(int(initial_kbps * factor), 380)


def compress_video(
    path: Path,
    max_mb: float,
    target_mb: float,
    audio_kbps: int,
    max_width: int,
    preset: str,
    attempts: int,
) -> tuple[bool, str]:
    original_size = size_mb(path)
    duration_s = seconds_of(path)
    initial_kbps = estimate_video_bitrate_kbps(duration_s, target_mb, audio_kbps)
    tmp_dir = Path(tempfile.mkdtemp(prefix="video-compress-"))
    best_out: Path | None = None
    best_size = math.inf

    try:
        for attempt, bitrate_kbps in enumerate(iter_targets(initial_kbps, attempts), start=1):
            out_path = tmp_dir / f"{path.stem}.attempt{attempt}.mp4"
            encode_once(
                input_path=path,
                output_path=out_path,
                video_kbps=bitrate_kbps,
                audio_kbps=audio_kbps,
                max_width=max_width,
                preset=preset,
            )
            out_size = size_mb(out_path)
            if out_size < best_size:
                best_size = out_size
                best_out = out_path

            print(
                f"[{path.name}] attempt {attempt}/{attempts} "
                f"v={bitrate_kbps}k -> {out_size:.2f} MB"
            )
            if out_size <= max_mb:
                break

        if best_out is None:
            return False, f"{path.name}: no output generated"

        backup = path.with_suffix(path.suffix + ".bak")
        if backup.exists():
            backup.unlink()
        path.rename(backup)
        shutil.move(str(best_out), str(path))
        backup.unlink(missing_ok=True)
        final_size = size_mb(path)
        ratio = final_size / original_size
        return True, f"{path.name}: {original_size:.2f} MB -> {final_size:.2f} MB ({ratio:.2%})"
    except Exception as exc:  # pragma: no cover - runtime tool errors
        return False, f"{path.name}: failed ({exc})"
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


def pick_files(video_dir: Path, explicit: list[str], max_mb: float) -> list[Path]:
    if explicit:
        return [Path(p) for p in explicit]
    candidates = sorted(video_dir.glob("*.mp4"))
    return [p for p in candidates if size_mb(p) > max_mb]


def main() -> int:
    parser = argparse.ArgumentParser(description="Compress oversized MP4 videos.")
    parser.add_argument("--max-mb", type=float, default=48.0, help="Maximum allowed size per file after compression.")
    parser.add_argument("--target-mb", type=float, default=42.0, help="Target size used to estimate bitrate.")
    parser.add_argument("--audio-kbps", type=int, default=96, help="AAC audio bitrate.")
    parser.add_argument("--max-width", type=int, default=1600, help="Downscale wider videos to this width.")
    parser.add_argument("--preset", type=str, default="slow", help="x264 preset.")
    parser.add_argument("--attempts", type=int, default=4, help="Maximum encoding attempts per file.")
    parser.add_argument("--files", nargs="*", default=[], help="Optional explicit file paths.")
    args = parser.parse_args()

    for tool in ("ffmpeg", "ffprobe"):
        if shutil.which(tool) is None:
            raise RuntimeError(f"{tool} is required but not found in PATH")

    files = pick_files(VIDEO_DIR, args.files, args.max_mb)
    if not files:
        print("No videos exceed the size threshold. Nothing to do.")
        return 0

    print(f"Found {len(files)} video(s) to compress.")
    failures = 0
    for file_path in files:
        ok, msg = compress_video(
            path=file_path,
            max_mb=args.max_mb,
            target_mb=args.target_mb,
            audio_kbps=args.audio_kbps,
            max_width=even(args.max_width),
            preset=args.preset,
            attempts=max(args.attempts, 1),
        )
        print(msg)
        if not ok:
            failures += 1

    if failures:
        print(f"Done with {failures} failure(s).")
        return 1

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
