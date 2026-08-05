#!/usr/bin/env python3
"""Update the local Yu-AI-OS handoff snapshot without changing Git state."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover - Python 3.8 compatibility
    ZoneInfo = None  # type: ignore[assignment]


CORE_FILES = (
    "00_System/AI_Constitution.md",
    "00_System/Identity.md",
    "00_System/Vision.md",
    "00_System/Strategic_Goals.md",
    "00_System/System_Design_Guide.md",
    "00_System/Workflow.md",
    "00_System/Decision_Log.md",
)
HANDOFF_PATH = "00_System/Handoff/Latest.md"
UNKNOWN = "Unknown"


def run_command(command: list[str], cwd: Path) -> tuple[bool, str]:
    try:
        completed = subprocess.run(
            command,
            cwd=cwd,
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=15,
        )
    except (OSError, subprocess.SubprocessError):
        return False, ""
    # Git porcelain uses leading spaces as status data; preserve them.
    output = completed.stdout.rstrip()
    return completed.returncode == 0, output


def git_command(repo_root: Path, *arguments: str) -> tuple[bool, str]:
    git = shutil.which("git")
    if not git:
        return False, ""
    return run_command(
        [git, "-c", f"safe.directory={repo_root}", "-C", str(repo_root), *arguments],
        repo_root,
    )


def single_line(value: str) -> str:
    return " ".join(value.replace("\x00", "").split())


def markdown_cell(value: str) -> str:
    return single_line(value).replace("|", r"\|") or UNKNOWN


def repository_name(remote: str) -> str:
    if not remote:
        return UNKNOWN
    cleaned = remote.rstrip("/").removesuffix(".git")
    match = re.search(r"(?:github\.com[/:])([^/]+/[^/]+)$", cleaned, re.IGNORECASE)
    return match.group(1) if match else cleaned


def changed_files(repo_root: Path) -> list[str]:
    ok, output = git_command(repo_root, "status", "--porcelain=v1", "--untracked-files=all")
    if not ok:
        return []
    paths: list[str] = []
    for line in output.splitlines():
        if len(line) < 4:
            continue
        path = line[3:]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        path = path.strip('"')
        if path and path not in paths:
            paths.append(path)
    return paths


def metadata_value(text: str, names: tuple[str, ...]) -> str:
    alternatives = "|".join(re.escape(name) for name in names)
    patterns = (
        rf"(?im)^\s*[-*]\s*(?:{alternatives})\s*[:：]\s*(.+?)\s*$",
        rf"(?im)^\s*(?:{alternatives})\s*[:：]\s*(.+?)\s*$",
        rf"(?im)^\s*\|\s*(?:{alternatives})\s*\|\s*(.+?)\s*\|",
    )
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            value = single_line(match.group(1).strip().strip("`*"))
            if value:
                return value
    return UNKNOWN


def core_file_details(repo_root: Path) -> list[tuple[str, str, str]]:
    details: list[tuple[str, str, str]] = []
    for relative_path in CORE_FILES:
        path = repo_root / relative_path
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            details.append((relative_path, UNKNOWN, UNKNOWN))
            continue
        status = metadata_value(
            text,
            ("Status", "Document Status", "Publication Status", "状态", "文档状态", "发布状态"),
        )
        version = metadata_value(text, ("Version", "Document Version", "版本", "文档版本"))
        details.append((relative_path, status, version))
    return details


def current_pr(repo_root: Path) -> dict[str, Any] | None:
    gh = shutil.which("gh")
    if not gh:
        possible = Path(r"C:\Program Files\GitHub CLI\gh.exe")
        if possible.is_file():
            gh = str(possible)
    if not gh:
        return None
    ok, output = run_command(
        [
            gh,
            "pr",
            "view",
            "--json",
            "number,title,state,isDraft,headRefName,baseRefName,url",
        ],
        repo_root,
    )
    if not ok or not output:
        return None
    try:
        value = json.loads(output)
    except json.JSONDecodeError:
        return None
    return value if isinstance(value, dict) else None


def tokyo_now() -> datetime:
    if ZoneInfo is not None:
        try:
            return datetime.now(ZoneInfo("Asia/Tokyo"))
        except Exception:
            pass
    return datetime.now(timezone(timedelta(hours=9), name="Asia/Tokyo"))


def format_snapshot(
    *,
    updated: str,
    repository: str,
    repo_root: Path,
    branch: str,
    head: str,
    files: list[str],
    result: str,
    next_action: str,
    risk: str,
    pr: dict[str, Any] | None,
    core_details: list[tuple[str, str, str]],
    commits: list[tuple[str, str]],
) -> str:
    clean = "Yes" if not files else "No"
    changed = "\n".join(f"- `{path}`" for path in files) if files else "- None"
    core_rows = "\n".join(
        f"| `{path}` | {markdown_cell(status)} | {markdown_cell(version)} |"
        for path, status, version in core_details
    )
    recent = (
        "\n".join(f"- `{commit[:12]}` {single_line(subject)}" for commit, subject in commits)
        if commits
        else "- Unknown"
    )
    if pr is None:
        pr_lines = "- Current PR: Unknown"
    else:
        draft = "Draft" if pr.get("isDraft") else "Ready for Review"
        pr_lines = "\n".join(
            (
                f"- Number: {pr.get('number', UNKNOWN)}",
                f"- Title: {single_line(str(pr.get('title', UNKNOWN)))}",
                f"- State: {pr.get('state', UNKNOWN)} ({draft})",
                f"- Head / Base: {pr.get('headRefName', UNKNOWN)} / {pr.get('baseRefName', UNKNOWN)}",
                f"- URL: {pr.get('url', UNKNOWN)}",
            )
        )
    return f"""# Latest Handoff

> Local dated snapshot for work resumption. This file is not a governance authority.

## Snapshot

- Updated: {updated}
- Repository: {repository}
- Repository Root: `{repo_root}`
- Branch: {branch}
- HEAD Commit: {head}
- Working Tree Clean: {clean}

## Task Outcome

- Result: {single_line(result)}
- Next: {single_line(next_action)}
- Risk: {single_line(risk)}

## Changed Files

{changed}

## Current Pull Request

{pr_lines}

## First-Layer Core Files

| File | Status | Version |
| --- | --- | --- |
{core_rows}

## Recent Commits

{recent}

## Automation Boundary

- Local update only.
- No automatic Commit, Push, PR creation, or Merge.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Update the local Yu-AI-OS handoff snapshot.")
    parser.add_argument("--result", required=True, help="Work actually completed.")
    parser.add_argument("--next", required=True, dest="next_action", help="Most important next action.")
    parser.add_argument("--risk", default="None identified", help="Current risk.")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    handoff_file = repo_root / HANDOFF_PATH

    remote_ok, remote = git_command(repo_root, "remote", "get-url", "origin")
    branch_ok, branch = git_command(repo_root, "branch", "--show-current")
    head_ok, head = git_command(repo_root, "rev-parse", "HEAD")
    log_ok, log_output = git_command(repo_root, "log", "-5", "--format=%H%x09%s")

    files = changed_files(repo_root)
    if HANDOFF_PATH not in files:
        files.append(HANDOFF_PATH)
    files.sort()

    commits: list[tuple[str, str]] = []
    if log_ok:
        for line in log_output.splitlines():
            commit, separator, subject = line.partition("\t")
            if separator and commit:
                commits.append((commit, subject))

    snapshot = format_snapshot(
        updated=tokyo_now().strftime("%Y-%m-%d %H:%M:%S Asia/Tokyo"),
        repository=repository_name(remote if remote_ok else ""),
        repo_root=repo_root,
        branch=branch if branch_ok and branch else UNKNOWN,
        head=head if head_ok and head else UNKNOWN,
        files=files,
        result=args.result,
        next_action=args.next_action,
        risk=args.risk,
        pr=current_pr(repo_root),
        core_details=core_file_details(repo_root),
        commits=commits,
    )

    try:
        handoff_file.parent.mkdir(parents=True, exist_ok=True)
        handoff_file.write_text(snapshot, encoding="utf-8", newline="\n")
    except OSError as exc:
        parser.error(f"could not write {handoff_file}: {exc}")

    print(f"Updated {handoff_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
