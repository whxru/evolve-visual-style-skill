#!/usr/bin/env python3
"""Install the canonical Skill for Codex, Claude Code, or both."""

from __future__ import annotations

import argparse
import shutil
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


SKILL_NAME = "evolve-visual-style"
SOURCE_DIR = Path(__file__).resolve().parent / SKILL_NAME


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install Evolve Visual Style for Codex, Claude Code, or both."
    )
    parser.add_argument("platform", choices=("codex", "claude", "both"))
    parser.add_argument(
        "--codex-root",
        type=Path,
        default=Path.home() / ".agents" / "skills",
        help="Codex skills root (default: ~/.agents/skills)",
    )
    parser.add_argument(
        "--claude-root",
        type=Path,
        default=Path.home() / ".claude" / "skills",
        help="Claude Code skills root (default: ~/.claude/skills)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing install after moving it to a timestamped backup.",
    )
    return parser.parse_args()


def claude_frontmatter(text: str) -> str:
    """Add Claude Code's native manual-only invocation field."""
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        raise ValueError("SKILL.md must start with YAML frontmatter")

    try:
        closing = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration as exc:
        raise ValueError("SKILL.md frontmatter is not closed") from exc

    field = "disable-model-invocation: true\n"
    for index in range(1, closing):
        if lines[index].startswith("disable-model-invocation:"):
            lines[index] = field
            return "".join(lines)

    lines.insert(closing, field)
    return "".join(lines)


def backup_path(target: Path) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    candidate = target.with_name(f"{target.name}.backup-{stamp}")
    suffix = 1
    while candidate.exists():
        candidate = target.with_name(f"{target.name}.backup-{stamp}-{suffix}")
        suffix += 1
    return candidate


def install_one(platform: str, root: Path, force: bool) -> tuple[Path, Path | None]:
    if not SOURCE_DIR.is_dir() or not (SOURCE_DIR / "SKILL.md").is_file():
        raise FileNotFoundError(f"canonical Skill source is missing: {SOURCE_DIR}")

    root = root.expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    target = root / SKILL_NAME
    if target.exists() and not force:
        raise FileExistsError(
            f"{target} already exists; rerun with --force to preserve it as a backup and update"
        )

    staging_parent = Path(tempfile.mkdtemp(prefix=f".{SKILL_NAME}-", dir=root))
    staging = staging_parent / SKILL_NAME
    preserved: Path | None = None
    try:
        shutil.copytree(SOURCE_DIR, staging)
        if platform == "claude":
            skill_md = staging / "SKILL.md"
            skill_md.write_text(
                claude_frontmatter(skill_md.read_text(encoding="utf-8")),
                encoding="utf-8",
            )

        if target.exists():
            preserved = backup_path(target)
            target.rename(preserved)
        staging.rename(target)
    except Exception:
        if preserved is not None and preserved.exists() and not target.exists():
            preserved.rename(target)
        raise
    finally:
        shutil.rmtree(staging_parent, ignore_errors=True)

    return target, preserved


def main() -> int:
    args = parse_args()
    requested = ("codex", "claude") if args.platform == "both" else (args.platform,)
    roots = {"codex": args.codex_root, "claude": args.claude_root}

    try:
        if not args.force:
            existing = [
                roots[platform].expanduser().resolve() / SKILL_NAME
                for platform in requested
                if (roots[platform].expanduser().resolve() / SKILL_NAME).exists()
            ]
            if existing:
                joined = ", ".join(str(path) for path in existing)
                raise FileExistsError(
                    f"existing install found: {joined}; rerun with --force to preserve backups and update"
                )
        for platform in requested:
            target, preserved = install_one(platform, roots[platform], args.force)
            print(f"Installed for {platform}: {target}")
            if preserved is not None:
                print(f"Previous install preserved at: {preserved}")
    except (OSError, ValueError) as exc:
        print(f"Installation failed: {exc}", file=sys.stderr)
        return 2

    print("Invoke with $evolve-visual-style in Codex or /evolve-visual-style in Claude Code.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
