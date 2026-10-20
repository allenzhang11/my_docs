#!/usr/bin/env python3
"""Convert a PDF document to Markdown with PyMuPDF4LLM.

Example:
    python pdf_to_md.py input.pdf -o output.md
    python pdf_to_md.py input.pdf --pages 1-20 --no-images
"""

from __future__ import annotations

import argparse
import os
import sys
import tempfile
from pathlib import Path


def parse_page_spec(spec: str | None, page_count: int) -> list[int] | None:
    """Parse a 1-based page specification into a sorted list of 0-based indexes."""
    if not spec or spec.strip().lower() == "all":
        return None

    pages: set[int] = set()
    for item in spec.split(","):
        item = item.strip()
        if not item:
            continue

        if "-" in item:
            start_text, end_text = item.split("-", 1)
            try:
                start = int(start_text)
                end = int(end_text)
            except ValueError as exc:
                raise ValueError(f"无效页码范围: {item!r}") from exc
            if start > end:
                raise ValueError(f"页码范围起点大于终点: {item!r}")
            selected = range(start, end + 1)
        else:
            try:
                selected = [int(item)]
            except ValueError as exc:
                raise ValueError(f"无效页码: {item!r}") from exc

        for page in selected:
            if not 1 <= page <= page_count:
                raise ValueError(f"页码 {page} 超出文档范围 1-{page_count}")
            pages.add(page - 1)

    if not pages:
        raise ValueError("没有解析到任何页码")
    return sorted(pages)


def split_pages(pages: list[int], chunk_size: int) -> list[list[int]]:
    if chunk_size <= 0:
        return [pages]
    return [pages[i : i + chunk_size] for i in range(0, len(pages), chunk_size)]


def make_relative_image_links(markdown: str, image_dir: Path, output_dir: Path) -> str:
    """Replace absolute image paths emitted by PyMuPDF4LLM with relative paths."""
    absolute = str(image_dir.resolve())
    relative = Path(os.path.relpath(image_dir.resolve(), output_dir.resolve())).as_posix()
    return markdown.replace(f"![]({absolute}/", f"![]({relative}/")


def convert(args: argparse.Namespace) -> Path:
    try:
        import pymupdf
        import pymupdf4llm
    except ImportError as exc:
        raise SystemExit(
            "缺少依赖。请在 learning_docs_env 环境中执行:\n"
            "  conda run -n learning_docs_env python -m pip install "
            "pymupdf4llm==1.28.2"
        ) from exc

    pdf_path = args.input.expanduser().resolve()
    if not pdf_path.is_file():
        raise SystemExit(f"PDF 文件不存在: {pdf_path}")

    output_path = (args.output or pdf_path.with_suffix(".md")).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    image_dir = (args.image_dir or output_path.with_name(f"{output_path.stem}_images")).expanduser()
    if not image_dir.is_absolute():
        image_dir = output_path.parent / image_dir
    image_dir = image_dir.resolve()

    with pymupdf.open(pdf_path) as document:
        page_count = document.page_count

    try:
        selected_pages = parse_page_spec(args.pages, page_count)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc

    if selected_pages is None:
        selected_pages = list(range(page_count))

    chunks = split_pages(selected_pages, args.chunk_size)
    if args.images:
        image_dir.mkdir(parents=True, exist_ok=True)

    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=output_path.parent,
            prefix=f".{output_path.name}.",
            suffix=".part",
            delete=False,
        ) as output_file:
            temporary_path = Path(output_file.name)

            for index, chunk in enumerate(chunks, start=1):
                first_page = chunk[0] + 1
                last_page = chunk[-1] + 1
                print(
                    f"[{index}/{len(chunks)}] 转换第 {first_page}-{last_page} 页...",
                    file=sys.stderr,
                )
                markdown = pymupdf4llm.to_markdown(
                    str(pdf_path),
                    pages=chunk,
                    header=False,
                    footer=False,
                    use_ocr=False,
                    write_images=args.images,
                    image_path=str(image_dir),
                    image_format="png",
                    dpi=args.dpi,
                    show_progress=False,
                )
                if isinstance(markdown, list):
                    markdown = "\n\n".join(str(part) for part in markdown)

                markdown = make_relative_image_links(
                    markdown, image_dir, output_path.parent
                )
                if index > 1 and markdown and not markdown.startswith("\n"):
                    output_file.write("\n\n")
                output_file.write(markdown.rstrip() + "\n")

        os.replace(temporary_path, output_path)
        temporary_path = None
        try:
            output_path.chmod(0o644)
        except OSError:
            pass
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)

    return output_path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="使用 PyMuPDF4LLM 将 PDF 转换为 Markdown"
    )
    parser.add_argument("input", type=Path, help="输入 PDF 文件")
    parser.add_argument("-o", "--output", type=Path, help="输出 Markdown 文件")
    parser.add_argument(
        "--pages",
        help="要转换的页码，例如 1-20,25,30-35；默认全部",
    )
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=32,
        help="每次转换的页数，0 表示一次转换全部（默认: 32）",
    )
    parser.add_argument(
        "--no-images",
        action="store_false",
        dest="images",
        help="不导出 PDF 中的图片",
    )
    parser.set_defaults(images=True)
    parser.add_argument(
        "--image-dir",
        type=Path,
        help="图片输出目录（默认: <Markdown 文件名>_images）",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=150,
        help="导出图片分辨率（默认: 150）",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.chunk_size < 0:
        raise SystemExit("--chunk-size 不能为负数")
    if args.dpi <= 0:
        raise SystemExit("--dpi 必须大于 0")

    output_path = convert(args)
    print(f"转换完成: {output_path}")


if __name__ == "__main__":
    main()
