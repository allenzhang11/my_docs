#!/usr/bin/env python3
"""Check structural invariants between a Markdown source and its translation."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


FENCE_RE = re.compile(r"^( {0,3})(`{3,}|~{3,})(.*)$")
HEADING_RE = re.compile(r"^ {0,3}(#{1,6})(?:[ \t]+|$)")
SETEXT_RE = re.compile(r"^ {0,3}(=+|-+)[ \t]*$")
INLINE_CODE_RE = re.compile(r"(?<!`)`([^`\n]+)`(?!`)")
LINK_RE = re.compile(
    r"(?<!!)\[[^\]\n]*\]\(\s*(?:<([^>\n]+)>|([^)\s]+))"
    r"(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)"
)
IMAGE_RE = re.compile(
    r"!\[[^\]\n]*\]\(\s*(?:<([^>\n]+)>|([^)\s]+))"
    r"(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)"
)
URL_RE = re.compile(r"https?://[^\s<>\"']+")
BULLET_RE = re.compile(r"^[ \t]{0,3}[-+*][ \t]+")
ORDERED_RE = re.compile(r"^[ \t]{0,3}\d+[.)][ \t]+")


@dataclass(frozen=True)
class CodeBlock:
    info: str
    body: str
    line: int


@dataclass(frozen=True)
class Occurrence:
    value: str
    line: int


@dataclass
class Extracted:
    headings: list[Occurrence]
    code_blocks: list[CodeBlock]
    inline_code: list[Occurrence]
    links: list[Occurrence]
    images: list[Occurrence]
    urls: list[Occurrence]
    bullet_items: int
    ordered_items: int


def _is_fence_close(line: str, fence_char: str, fence_length: int) -> bool:
    stripped = line.lstrip(" ")
    if len(line) - len(stripped) > 3:
        return False
    if not stripped.startswith(fence_char * fence_length):
        return False
    marker = stripped.rstrip()
    return bool(marker) and set(marker) == {fence_char}


def _occurrences(regex: re.Pattern[str], text: str, group: int = 1) -> list[Occurrence]:
    found: list[Occurrence] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        for match in regex.finditer(line):
            value = match.group(group)
            if value:
                found.append(Occurrence(value.strip(), line_number))
    return found


def _link_occurrences(regex: re.Pattern[str], text: str) -> list[Occurrence]:
    found: list[Occurrence] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        for match in regex.finditer(line):
            target = match.group(1) or match.group(2)
            if target:
                found.append(Occurrence(target.strip(), line_number))
    return found


def _mask_inline_code(line: str) -> str:
    return INLINE_CODE_RE.sub(lambda match: " " * len(match.group(0)), line)


def _url_occurrences(text: str) -> list[Occurrence]:
    found: list[Occurrence] = []
    trailing_punctuation = ".,;:!?，。；：！？、"
    closing_punctuation = ")]}）】」』"
    for line_number, line in enumerate(text.splitlines(), start=1):
        for match in URL_RE.finditer(line):
            value = match.group(0).rstrip(trailing_punctuation)
            while value and value[-1] in closing_punctuation:
                opener = {
                    "(": ")",
                    "[": "]",
                    "{": "}",
                    "）": "（",
                    "】": "【",
                    "」": "「",
                    "』": "『",
                }.get(value[-1])
                if opener is None or value.count(opener) >= value.count(value[-1]):
                    break
                value = value[:-1].rstrip(trailing_punctuation)
            if value:
                found.append(Occurrence(value, line_number))
    return found


def extract(text: str) -> Extracted:
    headings: list[Occurrence] = []
    code_blocks: list[CodeBlock] = []
    prose_lines: list[str] = []
    active_fence: tuple[str, int, str, int] | None = None
    body_lines: list[str] = []

    for line_number, line in enumerate(text.splitlines(), start=1):
        if active_fence:
            fence_char, fence_length, info, start_line = active_fence
            if _is_fence_close(line, fence_char, fence_length):
                code_blocks.append(
                    CodeBlock(info=info, body="\n".join(body_lines), line=start_line)
                )
                active_fence = None
                body_lines = []
                prose_lines.append("")
            else:
                body_lines.append(line)
                prose_lines.append("")
            continue

        fence_match = FENCE_RE.match(line)
        if fence_match:
            indent, marker, info = fence_match.groups()
            active_fence = (marker[0], len(marker), info.strip(), line_number)
            body_lines = []
            prose_lines.append("")
            continue

        heading_match = HEADING_RE.match(line)
        if heading_match:
            headings.append(
                Occurrence(str(len(heading_match.group(1))), line_number)
            )
        else:
            setext_match = SETEXT_RE.match(line)
            previous = prose_lines[-1] if prose_lines else ""
            if (
                setext_match
                and previous.strip()
                and not HEADING_RE.match(previous)
            ):
                level = "1" if setext_match.group(1).startswith("=") else "2"
                headings.append(Occurrence(level, line_number - 1))

        prose_lines.append(line)

    if active_fence:
        _, _, info, start_line = active_fence
        code_blocks.append(
            CodeBlock(info=info, body="\n".join(body_lines), line=start_line)
        )

    prose = "\n".join(prose_lines)
    prose_without_code = "\n".join(_mask_inline_code(line) for line in prose.splitlines())

    inline_code = _occurrences(INLINE_CODE_RE, prose)
    links = _link_occurrences(LINK_RE, prose_without_code)
    images = _link_occurrences(IMAGE_RE, prose_without_code)
    urls = _url_occurrences(prose_without_code)

    bullet_items = 0
    ordered_items = 0
    for line in prose.splitlines():
        if BULLET_RE.match(line):
            bullet_items += 1
        elif ORDERED_RE.match(line):
            ordered_items += 1

    return Extracted(
        headings=headings,
        code_blocks=code_blocks,
        inline_code=inline_code,
        links=links,
        images=images,
        urls=urls,
        bullet_items=bullet_items,
        ordered_items=ordered_items,
    )


def _counter(occurrences: list[Occurrence]) -> Counter[str]:
    return Counter(item.value for item in occurrences)


def _first_lines(occurrences: list[Occurrence]) -> dict[str, int]:
    lines: dict[str, int] = {}
    for item in occurrences:
        lines.setdefault(item.value, item.line)
    return lines


def _compare_values(
    label: str,
    source: list[Occurrence],
    translated: list[Occurrence],
    errors: list[str],
    warnings: list[str],
) -> None:
    source_counts = _counter(source)
    translated_counts = _counter(translated)
    source_lines = _first_lines(source)
    translated_lines = _first_lines(translated)

    missing = source_counts - translated_counts
    added = translated_counts - source_counts
    for value, count in sorted(missing.items()):
        errors.append(
            f"missing {label} at source line {source_lines[value]}: "
            f"{value!r} ({count} occurrence(s) missing)"
        )
    for value, count in sorted(added.items()):
        warnings.append(
            f"extra {label} at translated line {translated_lines[value]}: "
            f"{value!r} ({count} occurrence(s) added)"
        )


def check_texts(source_text: str, translated_text: str) -> tuple[list[str], list[str]]:
    source = extract(source_text)
    translated = extract(translated_text)
    errors: list[str] = []
    warnings: list[str] = []

    source_levels = [item.value for item in source.headings]
    translated_levels = [item.value for item in translated.headings]
    if source_levels != translated_levels:
        errors.append(
            "heading level sequence differs: "
            f"source={source_levels}, translated={translated_levels}"
        )

    source_blocks = Counter((block.info, block.body) for block in source.code_blocks)
    translated_blocks = Counter(
        (block.info, block.body) for block in translated.code_blocks
    )
    for block, count in (source_blocks - translated_blocks).items():
        source_line = next(
            item.line
            for item in source.code_blocks
            if (item.info, item.body) == block
        )
        errors.append(
            f"code block at source line {source_line} is missing or changed "
            f"({count} occurrence(s), info={block[0]!r})"
        )
    for block, count in (translated_blocks - source_blocks).items():
        translated_line = next(
            item.line
            for item in translated.code_blocks
            if (item.info, item.body) == block
        )
        errors.append(
            f"translated code block at line {translated_line} is added or changed "
            f"({count} occurrence(s), info={block[0]!r})"
        )

    _compare_values("inline code", source.inline_code, translated.inline_code, errors, warnings)
    _compare_values("link target", source.links, translated.links, errors, warnings)
    _compare_values("image target", source.images, translated.images, errors, warnings)
    _compare_values("URL", source.urls, translated.urls, errors, warnings)

    if source.bullet_items != translated.bullet_items:
        warnings.append(
            f"bullet item count differs: source={source.bullet_items}, "
            f"translated={translated.bullet_items}"
        )
    if source.ordered_items != translated.ordered_items:
        warnings.append(
            f"ordered item count differs: source={source.ordered_items}, "
            f"translated={translated.ordered_items}"
        )

    return errors, warnings


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(f"{path} is not valid UTF-8: {exc}") from exc
    except OSError as exc:
        raise ValueError(f"cannot read {path}: {exc}") from exc


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Check headings, code blocks, inline code, links, image targets, "
            "URLs, and list counts between a Markdown source and translation."
        )
    )
    parser.add_argument("source", type=Path, help="source Markdown file")
    parser.add_argument("translated", type=Path, help="translated Markdown file")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="treat warnings such as added links or list-count differences as failures",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)

    try:
        source_text = _read(args.source)
        translated_text = _read(args.translated)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    errors, warnings = check_texts(source_text, translated_text)
    for message in warnings:
        print(f"warning: {message}")
    for message in errors:
        print(f"error: {message}")

    if errors:
        print(
            f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)",
            file=sys.stderr,
        )
        return 1
    if warnings and args.strict:
        print(
            f"FAILED (--strict): {len(warnings)} warning(s)",
            file=sys.stderr,
        )
        return 1

    print(f"OK: 0 errors, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
