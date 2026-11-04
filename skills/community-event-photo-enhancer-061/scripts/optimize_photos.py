#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Offline community photo optimizer using Pillow only.

The original files are never overwritten. Outputs are written to a separate
directory with an accompanying JSON processing record.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageStat


FORMATS = {".jpg", ".jpeg", ".png", ".webp"}


def apply_crop(image: Image.Image, aspect: str | None) -> Image.Image:
    if not aspect:
        return image
    ratios = {
        "16:9": 16 / 9,
        "4:3": 4 / 3,
        "1:1": 1,
        "3:4": 3 / 4,
    }
    if aspect not in ratios:
        raise ValueError(f"Unsupported crop aspect: {aspect}")
    target = ratios[aspect]
    width, height = image.size
    current = width / height
    if current > target:
        new_width = int(height * target)
        left = (width - new_width) // 2
        return image.crop((left, 0, left + new_width, height))
    new_height = int(width / target)
    top = (height - new_height) // 2
    return image.crop((0, top, width, top + new_height))


def neutral_white_balance(image: Image.Image) -> tuple[Image.Image, list[float] | None]:
    rgb = image.convert("RGB")
    array = np.asarray(rgb).astype(np.float32)
    luminance = (
        array[:, :, 0] * 0.299
        + array[:, :, 1] * 0.587
        + array[:, :, 2] * 0.114
    )
    threshold = float(np.percentile(luminance, 85))
    mask = luminance >= threshold
    neutral_pixels = array[mask]
    if len(neutral_pixels) < 20:
        return image, None
    channel_means = neutral_pixels.mean(axis=0)
    if float(channel_means.max() - channel_means.min()) < 6:
        return image, None
    target = float(channel_means.mean())
    scales = np.clip(target / np.maximum(channel_means, 1), 0.82, 1.18)
    corrected = np.clip(array * scales, 0, 255).astype(np.uint8)
    return Image.fromarray(corrected, "RGB"), [round(float(value), 4) for value in scales]


def optimize_one(
    source: Path,
    target: Path,
    max_width: int,
    quality: int,
    crop: str | None,
    rotate: float,
    auto_tone: bool,
    white_balance: bool,
) -> dict:
    record = {
        "source": str(source),
        "output": str(target),
        "source_bytes": source.stat().st_size,
        "applied": [],
    }
    with Image.open(source) as opened:
        opened.load()
        exif_orientation = opened.getexif().get(274)
        image = ImageOps.exif_transpose(opened)
        if exif_orientation:
            record["applied"].append("strip_and_apply_exif_orientation")
        record["source_format"] = opened.format
        record["source_size"] = list(opened.size)

        if rotate:
            image = image.rotate(-rotate, expand=True)
            record["applied"].append(f"rotate_{rotate:g}_degrees_clockwise")

        image = apply_crop(image, crop)
        if crop:
            record["applied"].append(f"crop_center_{crop}")

        if auto_tone:
            gray = ImageOps.grayscale(image)
            mean_luma = ImageStat.Stat(gray).mean[0]
            if mean_luma < 90:
                brightness = min(1.35, max(1.08, 110 / max(mean_luma, 1)))
                image = ImageEnhance.Brightness(image).enhance(brightness)
                record["applied"].append(f"brightness_{brightness:.2f}")
            elif mean_luma > 190:
                brightness = max(0.88, min(0.98, 180 / max(mean_luma, 1)))
                image = ImageEnhance.Brightness(image).enhance(brightness)
                record["applied"].append(f"brightness_{brightness:.2f}")

            if white_balance:
                image, scales = neutral_white_balance(image)
                if scales:
                    record["applied"].append(
                        "neutral_white_balance_rgb_" + "_".join(f"{value:.3f}" for value in scales)
                    )
            image = ImageEnhance.Contrast(image).enhance(1.06)
            image = ImageEnhance.Color(image).enhance(1.04)
            image = image.filter(ImageFilter.MedianFilter(size=3))
            image = image.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=3))
            record["applied"].extend(
                ["contrast_1.06", "color_1.04", "median_denoise_3", "unsharp_1.2_110_3"]
            )

        if max_width > 0 and image.width > max_width:
            original_width, original_height = image.size
            new_height = round(original_height * max_width / original_width)
            image = image.resize((max_width, new_height), Image.Resampling.LANCZOS)
            record["applied"].append(f"resize_{max_width}x{new_height}")

        target.parent.mkdir(parents=True, exist_ok=True)
        suffix = target.suffix.lower()
        if suffix in {".jpg", ".jpeg"}:
            image = image.convert("RGB")
            image.save(target, "JPEG", quality=quality, optimize=True, progressive=True)
        elif suffix == ".png":
            if image.mode not in {"RGB", "RGBA"}:
                image = image.convert("RGBA" if "A" in image.getbands() else "RGB")
            image.save(target, "PNG", optimize=True)
        elif suffix == ".webp":
            image = image.convert("RGB")
            image.save(target, "WEBP", quality=quality, method=6)
        else:
            raise ValueError(f"Unsupported output format: {target.suffix}")

        record["output_size"] = list(image.size)
        record["output_bytes"] = target.stat().st_size
        record["metadata_policy"] = "EXIF removed from output"
        record["status"] = "ok"
        return record


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", required=True, help="Directory containing source photos")
    parser.add_argument("--output-dir", required=True, help="Separate directory for optimized photos")
    parser.add_argument("--max-width", type=int, default=1280)
    parser.add_argument("--quality", type=int, default=88)
    parser.add_argument("--crop", choices=["16:9", "4:3", "1:1", "3:4"])
    parser.add_argument("--rotate", type=float, default=0)
    parser.add_argument("--no-auto-tone", action="store_true")
    parser.add_argument("--no-white-balance", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    source_dir = Path(args.input_dir).resolve()
    output_dir = Path(args.output_dir).resolve()
    if not source_dir.is_dir():
        raise SystemExit(f"Input directory not found: {source_dir}")
    if source_dir == output_dir:
        raise SystemExit("Output directory must differ from input directory")
    output_dir.mkdir(parents=True, exist_ok=True)

    results = []
    for source in sorted(path for path in source_dir.iterdir() if path.is_file() and path.suffix.lower() in FORMATS):
        target = output_dir / f"{source.stem}_optimized{source.suffix.lower()}"
        if target.exists() and not args.overwrite:
            results.append(
                {
                    "source": str(source),
                    "output": str(target),
                    "status": "skipped_existing",
                }
            )
            continue
        try:
            results.append(
                optimize_one(
                    source,
                    target,
                    max_width=args.max_width,
                    quality=args.quality,
                    crop=args.crop,
                    rotate=args.rotate,
                    auto_tone=not args.no_auto_tone,
                    white_balance=not args.no_white_balance,
                )
            )
        except Exception as exc:
            results.append(
                {
                    "source": str(source),
                    "output": str(target),
                    "status": "error",
                    "error": str(exc),
                }
            )

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_dir": str(source_dir),
        "output_dir": str(output_dir),
        "parameters": {
            "max_width": args.max_width,
            "quality": args.quality,
            "crop": args.crop,
            "rotate": args.rotate,
            "auto_tone": not args.no_auto_tone,
            "white_balance": not args.no_white_balance,
            "metadata_policy": "EXIF removed",
        },
        "results": results,
        "ok": sum(item["status"] == "ok" for item in results),
        "errors": sum(item["status"] == "error" for item in results),
    }
    report_path = output_dir / "processing_record.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if report["errors"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
