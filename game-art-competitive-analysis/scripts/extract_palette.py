#!/usr/bin/env python3
"""Extract approximate color palettes from game screenshots.

Requires Pillow. Outputs Markdown by default, or JSON with --format json.
"""

from __future__ import annotations

import argparse
import colorsys
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError as exc:  # pragma: no cover
    print("Pillow is required. Install with: python -m pip install Pillow", file=sys.stderr)
    raise SystemExit(2) from exc


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff"}


def clamp(value: int) -> int:
    return max(0, min(255, value))


def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    return "#{:02X}{:02X}{:02X}".format(*rgb)


def quantize_rgb(rgb: tuple[int, int, int], step: int) -> tuple[int, int, int]:
    half = step // 2
    return tuple(clamp((channel // step) * step + half) for channel in rgb)


def hls_for_rgb(rgb: tuple[int, int, int]) -> tuple[float, float, float]:
    r, g, b = (channel / 255.0 for channel in rgb)
    hue, lightness, saturation = colorsys.rgb_to_hls(r, g, b)
    return hue * 360.0, lightness, saturation


def hue_name(hue: float, saturation: float) -> str:
    if saturation < 0.12:
        return "neutral"
    if hue < 15 or hue >= 345:
        return "red"
    if hue < 45:
        return "orange"
    if hue < 70:
        return "yellow"
    if hue < 155:
        return "green"
    if hue < 190:
        return "cyan"
    if hue < 255:
        return "blue"
    if hue < 290:
        return "purple"
    if hue < 345:
        return "magenta"
    return "neutral"


def temperature(hue: float, saturation: float) -> str:
    if saturation < 0.12:
        return "neutral"
    if hue < 70 or hue >= 330:
        return "warm"
    if 155 <= hue <= 275:
        return "cool"
    return "mixed"


def band(value: float, low: float, high: float, labels: tuple[str, str, str]) -> str:
    if value < low:
        return labels[0]
    if value > high:
        return labels[2]
    return labels[1]


def collect_image_paths(inputs: list[str]) -> list[Path]:
    paths: list[Path] = []
    for raw in inputs:
        path = Path(raw)
        if path.is_dir():
            paths.extend(
                p for p in sorted(path.rglob("*")) if p.suffix.lower() in IMAGE_EXTENSIONS
            )
        elif path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS:
            paths.append(path)
        else:
            print(f"Skipping unsupported path: {path}", file=sys.stderr)
    return paths


def summarize_bucket_map(
    counts: Counter[tuple[int, int, int]],
    sums: dict[tuple[int, int, int], list[int]],
    total: int,
    top: int,
) -> dict:
    if total == 0:
        return {
            "total_pixels": 0,
            "average_lightness": 0.0,
            "average_saturation": 0.0,
            "temperature_tendency": "unknown",
            "palette": [],
        }

    weighted_lightness = 0.0
    weighted_saturation = 0.0
    warm_weight = 0.0
    cool_weight = 0.0

    for bucket, count in counts.items():
        avg_rgb = tuple(round(channel_sum / count) for channel_sum in sums[bucket])
        hue, lightness, saturation = hls_for_rgb(avg_rgb)
        weighted_lightness += lightness * count
        weighted_saturation += saturation * count
        temp = temperature(hue, saturation)
        if temp == "warm":
            warm_weight += count * max(saturation, 0.05)
        elif temp == "cool":
            cool_weight += count * max(saturation, 0.05)

    if warm_weight + cool_weight == 0:
        temp_tendency = "neutral"
    else:
        temp_score = (warm_weight - cool_weight) / (warm_weight + cool_weight)
        if temp_score > 0.15:
            temp_tendency = "warm"
        elif temp_score < -0.15:
            temp_tendency = "cool"
        else:
            temp_tendency = "mixed"

    palette = []
    for rank, (bucket, count) in enumerate(counts.most_common(top), start=1):
        avg_rgb = tuple(round(channel_sum / count) for channel_sum in sums[bucket])
        hue, lightness, saturation = hls_for_rgb(avg_rgb)
        palette.append(
            {
                "rank": rank,
                "hex": rgb_to_hex(avg_rgb),
                "rgb": list(avg_rgb),
                "percent": round(count / total * 100.0, 2),
                "hue_degrees": round(hue, 1),
                "hue_name": hue_name(hue, saturation),
                "temperature": temperature(hue, saturation),
                "lightness": round(lightness, 3),
                "saturation": round(saturation, 3),
                "value_band": band(lightness, 0.32, 0.72, ("dark", "mid", "light")),
                "saturation_band": band(saturation, 0.22, 0.62, ("low", "medium", "high")),
            }
        )

    return {
        "total_pixels": total,
        "average_lightness": round(weighted_lightness / total, 3),
        "average_saturation": round(weighted_saturation / total, 3),
        "temperature_tendency": temp_tendency,
        "palette": palette,
    }


def analyze_image(path: Path, args: argparse.Namespace) -> tuple[dict, Counter, dict, int]:
    with Image.open(path) as image:
        image = ImageOps.exif_transpose(image)
        image.thumbnail((args.max_side, args.max_side))
        rgba = image.convert("RGBA")

    counts: Counter[tuple[int, int, int]] = Counter()
    sums: dict[tuple[int, int, int], list[int]] = defaultdict(lambda: [0, 0, 0])
    total = 0

    pixels = rgba.get_flattened_data() if hasattr(rgba, "get_flattened_data") else rgba.getdata()
    for red, green, blue, alpha in pixels:
        if alpha < args.alpha_threshold:
            continue
        rgb = (red, green, blue)
        bucket = quantize_rgb(rgb, args.quantize)
        counts[bucket] += 1
        sums[bucket][0] += red
        sums[bucket][1] += green
        sums[bucket][2] += blue
        total += 1

    summary = summarize_bucket_map(counts, sums, total, args.top)
    summary["path"] = str(path)
    summary["image_id"] = path.stem
    return summary, counts, sums, total


def combine_buckets(
    analyses: list[tuple[dict, Counter, dict, int]], top: int
) -> dict:
    combined_counts: Counter[tuple[int, int, int]] = Counter()
    combined_sums: dict[tuple[int, int, int], list[int]] = defaultdict(lambda: [0, 0, 0])
    combined_total = 0

    for _summary, counts, sums, total in analyses:
        combined_total += total
        for bucket, count in counts.items():
            combined_counts[bucket] += count
            combined_sums[bucket][0] += sums[bucket][0]
            combined_sums[bucket][1] += sums[bucket][1]
            combined_sums[bucket][2] += sums[bucket][2]

    return summarize_bucket_map(combined_counts, combined_sums, combined_total, top)


def markdown_palette(title: str, summary: dict) -> list[str]:
    lines = [
        f"## {title}",
        "",
        f"- Total sampled pixels: {summary['total_pixels']}",
        f"- Average lightness: {summary['average_lightness']}",
        f"- Average saturation: {summary['average_saturation']}",
        f"- Temperature tendency: {summary['temperature_tendency']}",
        "",
        "| Rank | Hex | Percent | Hue | Temp | Lightness | Saturation | RGB |",
        "|---:|---|---:|---|---|---:|---:|---|",
    ]
    for color in summary["palette"]:
        lines.append(
            "| {rank} | {hex} | {percent:.2f}% | {hue_name} ({hue_degrees}) | "
            "{temperature} | {lightness:.3f} | {saturation:.3f} | {rgb} |".format(
                **color
            )
        )
    lines.append("")
    return lines


def format_markdown(result: dict) -> str:
    lines = ["# Palette Extraction Report", ""]
    lines.extend(markdown_palette("Combined Palette", result["combined"]))
    for image in result["images"]:
        title = f"Image Palette: {Path(image['path']).name}"
        lines.extend(markdown_palette(title, image))
    return "\n".join(lines)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="+", help="Image files or directories")
    parser.add_argument("--top", type=int, default=8, help="Palette colors per image")
    parser.add_argument("--max-side", type=int, default=640, help="Resize max side before sampling")
    parser.add_argument("--quantize", type=int, default=24, help="RGB bucket size")
    parser.add_argument("--alpha-threshold", type=int, default=16, help="Ignore transparent pixels below this alpha")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--out", help="Optional output file")
    args = parser.parse_args(argv)
    args.quantize = max(4, min(64, args.quantize))
    args.max_side = max(64, args.max_side)
    return args


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    image_paths = collect_image_paths(args.inputs)
    if not image_paths:
        print("No supported image files found.", file=sys.stderr)
        return 1

    analyses = [analyze_image(path, args) for path in image_paths]
    result = {
        "inputs": [str(path) for path in image_paths],
        "combined": combine_buckets(analyses, args.top),
        "images": [summary for summary, _counts, _sums, _total in analyses],
    }

    if args.format == "json":
        output = json.dumps(result, indent=2, ensure_ascii=False)
    else:
        output = format_markdown(result)

    if args.out:
        Path(args.out).write_text(output, encoding="utf-8")
    else:
        print(output)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
