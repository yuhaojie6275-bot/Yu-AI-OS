#!/usr/bin/env python3
"""Run deterministic checks for the trusted base and proposed PR head."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import urllib.parse
from dataclasses import dataclass
from pathlib import PurePosixPath


class CheckError(Exception):
    """Expected error that should fail the workflow."""


@dataclass(frozen=True)
class Config:
    base_sha: str
    head_sha: str


@dataclass(frozen=True)
class CheckResult:
    compile: str
    format: str
    links: str
    yaml: str

    @property
    def failed(self) -> bool:
        return "FAIL" in (self.compile, self.format, self.links, self.yaml)


def required_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise CheckError(f"缺少环境变量：{name}")
    return value


def load_config() -> Config:
    return Config(base_sha=required_env("PR_BASE_SHA"), head_sha=required_env("PR_HEAD_SHA"))


def run_git(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        ["git", *args],
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if check and result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip() or "未知 Git 错误"
        raise CheckError(f"Git 命令失败：git {' '.join(args)}：{message}")
    return result


def changed_paths(base_sha: str, head_sha: str) -> list[str]:
    output = run_git("diff", "--name-only", "--diff-filter=ACMR", base_sha, head_sha).stdout
    return [line.strip().replace("\\", "/") for line in output.splitlines() if line.strip()]


def git_file_text(revision: str, path: str) -> str:
    result = run_git("show", f"{revision}:{path}", check=False)
    if result.returncode != 0:
        raise CheckError(f"读取变更文件失败：{path}")
    return result.stdout


def check_python_compile(paths: list[str], head_sha: str) -> str:
    python_paths = [path for path in paths if path.endswith(".py")]
    if not python_paths:
        return "SKIP（本次无 Python 变更）"
    failures: list[str] = []
    for path in python_paths:
        try:
            compile(git_file_text(head_sha, path), path, "exec")
        except (SyntaxError, UnicodeError, CheckError):
            failures.append(path)
    return "PASS" if not failures else f"FAIL（{len(failures)} 个文件）"


def check_diff(base_sha: str, head_sha: str) -> str:
    return "PASS" if run_git("diff", "--check", base_sha, head_sha, check=False).returncode == 0 else "FAIL"


MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def normalize_link(source_path: str, target: str) -> str | None:
    target = target.strip().split(maxsplit=1)[0].strip("<>")
    if not target or target.startswith(("#", "http://", "https://", "mailto:", "tel:")):
        return None
    target = urllib.parse.unquote(target.split("#", 1)[0].split("?", 1)[0])
    if not target:
        return None
    base = PurePosixPath(source_path).parent
    parts: list[str] = []
    for part in (base / target).parts:
        if part in ("", "."):
            continue
        if part == "..":
            if parts:
                parts.pop()
            continue
        parts.append(part)
    return "/".join(parts)


def check_markdown_links(paths: list[str], head_sha: str) -> str:
    markdown_paths = [path for path in paths if path.lower().endswith(".md")]
    if not markdown_paths:
        return "SKIP（本次无 Markdown 变更）"
    repository_paths = set(run_git("ls-tree", "-r", "--name-only", head_sha).stdout.splitlines())
    missing: set[str] = set()
    for source in markdown_paths:
        for match in MARKDOWN_LINK_RE.finditer(git_file_text(head_sha, source)):
            target = normalize_link(source, match.group(1))
            if target and target not in repository_paths:
                missing.add(target)
    return "PASS" if not missing else f"FAIL（{len(missing)} 个本地链接）"


def check_yaml(paths: list[str], head_sha: str) -> str:
    yaml_paths = [path for path in paths if path.lower().endswith((".yml", ".yaml"))]
    if not yaml_paths:
        return "SKIP（本次无 YAML 变更）"
    try:
        import yaml  # type: ignore[import-not-found]
    except ImportError:
        return "FAIL（缺少 YAML 解析器）"
    failures = 0
    for path in yaml_paths:
        try:
            yaml.safe_load(git_file_text(head_sha, path))
        except (yaml.YAMLError, CheckError):
            failures += 1
    return "PASS" if failures == 0 else f"FAIL（{failures} 个文件）"


def run_checks(config: Config) -> CheckResult:
    paths = changed_paths(config.base_sha, config.head_sha)
    return CheckResult(
        compile=check_python_compile(paths, config.head_sha),
        format=check_diff(config.base_sha, config.head_sha),
        links=check_markdown_links(paths, config.head_sha),
        yaml=check_yaml(paths, config.head_sha),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Yu-AI-OS PR 确定性检查")
    parser.parse_args()
    try:
        result = run_checks(load_config())
        for name, value in (
            ("Python 语法", result.compile),
            ("格式", result.format),
            ("Markdown 本地链接", result.links),
            ("YAML 解析", result.yaml),
        ):
            print(f"{name}: {value}")
        return 1 if result.failed else 0
    except (CheckError, ValueError) as exc:
        print(f"确定性检查失败：{exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
