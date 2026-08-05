#!/usr/bin/env python3
"""Generate a short Chinese PR executive summary without calling an LLM."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import PurePosixPath
from typing import Any, Callable

SUMMARY_MARKER = "<!-- yu-ai-os-automatic-review -->"
EXPECTED_AUTHOR = "github-actions[bot]"
HTTP_TIMEOUT_SECONDS = 30
MAX_COMMENTS_TO_SCAN = 300
MAX_ITEMS = 5


class SummaryError(Exception):
    """Expected error that should fail the workflow."""


@dataclass(frozen=True)
class Config:
    github_token: str
    repository: str
    api_url: str
    pr_number: int
    base_sha: str
    head_sha: str
    marker: str


@dataclass(frozen=True)
class CheckResult:
    compile: str
    tests: str
    format: str
    links: str
    yaml: str

    @property
    def failed(self) -> bool:
        return "❌" in (self.compile, self.tests, self.format, self.links, self.yaml)


def required_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise SummaryError(f"缺少环境变量：{name}")
    return value


def load_config() -> Config:
    return Config(
        github_token=required_env("GITHUB_TOKEN"),
        repository=required_env("GITHUB_REPOSITORY"),
        api_url=os.environ.get("GITHUB_API_URL", "https://api.github.com").rstrip("/"),
        pr_number=int(required_env("PR_NUMBER")),
        base_sha=required_env("PR_BASE_SHA"),
        head_sha=required_env("PR_HEAD_SHA"),
        marker=os.environ.get("SUMMARY_MARKER", SUMMARY_MARKER),
    )


def github_request(config: Config, method: str, path: str, body: dict[str, Any] | None = None) -> Any:
    request = urllib.request.Request(
        f"{config.api_url}{path}",
        data=None if body is None else json.dumps(body).encode("utf-8"),
        method=method,
    )
    request.add_header("Accept", "application/vnd.github+json")
    request.add_header("Authorization", f"Bearer {config.github_token}")
    request.add_header("X-GitHub-Api-Version", "2022-11-28")
    if body is not None:
        request.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(request, timeout=HTTP_TIMEOUT_SECONDS) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        raise SummaryError(f"GitHub API 请求失败：{method} {path}，HTTP {exc.code}") from exc
    except urllib.error.URLError as exc:
        raise SummaryError(f"GitHub API 请求失败：{method} {path}，{exc.reason}") from exc
    if not raw:
        return None
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise SummaryError(f"GitHub API 返回了无效 JSON：{method} {path}") from exc


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
        raise SummaryError(f"Git 命令失败：git {' '.join(args)}：{message}")
    return result


def changed_paths(base_sha: str, head_sha: str) -> list[str]:
    output = run_git("diff", "--name-only", "--diff-filter=ACMR", base_sha, head_sha).stdout
    return [line.strip().replace("\\", "/") for line in output.splitlines() if line.strip()]


def git_file_text(revision: str, path: str) -> str:
    result = run_git("show", f"{revision}:{path}", check=False)
    if result.returncode != 0:
        raise SummaryError(f"读取变更文件失败：{path}")
    return result.stdout


def check_python_compile(paths: list[str], head_sha: str) -> str:
    python_paths = [path for path in paths if path.endswith(".py")]
    if not python_paths:
        return "未配置（本次无 Python 变更）"
    failures: list[str] = []
    for path in python_paths:
        try:
            compile(git_file_text(head_sha, path), path, "exec")
        except (SyntaxError, UnicodeError, SummaryError):
            failures.append(path)
    return "✅" if not failures else f"❌（{len(failures)} 个文件）"


def check_diff(base_sha: str, head_sha: str) -> str:
    return "✅" if run_git("diff", "--check", base_sha, head_sha, check=False).returncode == 0 else "❌"


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
        return "未配置（本次无 Markdown 变更）"
    repository_paths = set(run_git("ls-tree", "-r", "--name-only", head_sha).stdout.splitlines())
    missing: set[str] = set()
    for source in markdown_paths:
        for match in MARKDOWN_LINK_RE.finditer(git_file_text(head_sha, source)):
            target = normalize_link(source, match.group(1))
            if target and target not in repository_paths:
                missing.add(target)
    return "✅" if not missing else f"❌（{len(missing)} 个本地链接）"


def check_yaml(paths: list[str], head_sha: str) -> str:
    yaml_paths = [path for path in paths if path.lower().endswith((".yml", ".yaml"))]
    if not yaml_paths:
        return "未配置（本次无 YAML 变更）"
    try:
        import yaml  # type: ignore[import-not-found]
    except ImportError:
        return "❌（缺少 YAML 解析器）"
    failures = 0
    for path in yaml_paths:
        try:
            yaml.safe_load(git_file_text(head_sha, path))
        except (yaml.YAMLError, SummaryError):
            failures += 1
    return "✅" if failures == 0 else f"❌（{failures} 个文件）"


def run_checks(base_sha: str, head_sha: str) -> CheckResult:
    paths = changed_paths(base_sha, head_sha)
    return CheckResult(
        compile=check_python_compile(paths, head_sha),
        tests="✅（执行摘要脚本自测）",
        format=check_diff(base_sha, head_sha),
        links=check_markdown_links(paths, head_sha),
        yaml=check_yaml(paths, head_sha),
    )


HEADING_ALIASES = {
    "本次做了什么": ("本次做了什么", "做了什么", "what changed", "changes"),
    "本次没做什么": ("本次没做什么", "没做什么", "范围边界", "out of scope", "not changed"),
    "需要 Human 注意": ("需要 human 注意", "human 注意", "风险", "risks"),
    "下一步": ("下一步", "next steps", "next step"),
}


def normalize_heading(text: str) -> str:
    return re.sub(r"[：:*_`\s]+", " ", text.strip().lower()).strip()


def extract_sections(body: str) -> dict[str, list[str]]:
    sections = {name: [] for name in HEADING_ALIASES}
    current: str | None = None
    for raw_line in body.splitlines():
        heading = re.match(r"^#{1,6}\s+(.+?)\s*$", raw_line)
        if heading:
            normalized = normalize_heading(heading.group(1))
            current = next(
                (
                    name
                    for name, aliases in HEADING_ALIASES.items()
                    if any(normalized == normalize_heading(alias) for alias in aliases)
                ),
                None,
            )
            continue
        if current is None:
            continue
        item = re.match(r"^\s*[-*+]\s+(.*\S)\s*$", raw_line)
        if item and len(sections[current]) < MAX_ITEMS:
            sections[current].append(item.group(1).strip())
    return sections


def bullets(items: list[str], *, limit: int, missing: str = "PR 正文未提供") -> str:
    selected = [item for item in items if item][:limit]
    return "\n".join(f"- {item}" for item in selected) if selected else f"- {missing}"


def format_summary(pr: dict[str, Any], checks: CheckResult, marker: str) -> str:
    body = str(pr.get("body") or "")
    sections = extract_sections(body)
    changed_files = pr.get("changed_files")
    conclusion = "⚠ 建议修改后再合并" if checks.failed else "✅ 可以进入 Human 审阅"
    human_attention = sections["需要 Human 注意"][:3]
    if checks.failed:
        human_attention.insert(0, "存在失败的确定性检查，请先查看 Actions 日志。")
    attention = bullets(human_attention, limit=3, missing="无")
    next_steps = sections["下一步"][:3]
    if not next_steps:
        next_steps = ["Human 阅读本摘要并审阅实际变更。"]
    changed_note = f"（GitHub 记录变更文件：{changed_files}）" if isinstance(changed_files, int) else ""
    return f"""{marker}
# Yu-AI-OS 执行摘要

## 结论
{conclusion}

> 自动检查通过不代表 Human 已批准 Merge。

## 本次做了什么
{bullets(sections['本次做了什么'], limit=5)}
{changed_note}

## 本次没做什么
{bullets(sections['本次没做什么'], limit=5)}

## 自动检查
- 编译：{checks.compile}
- 测试：{checks.tests}
- 格式检查：{checks.format}
- 链接检查：{checks.links}
- YAML：{checks.yaml}

## 需要 Human 注意
{attention}

## 下一步
{bullets(next_steps, limit=3)}

预计阅读时间：约 20 秒
"""


def list_comments(config: Config) -> list[dict[str, Any]]:
    comments: list[dict[str, Any]] = []
    page = 1
    while len(comments) < MAX_COMMENTS_TO_SCAN:
        data = github_request(
            config,
            "GET",
            f"/repos/{config.repository}/issues/{config.pr_number}/comments?per_page=100&page={page}",
        )
        if not data:
            break
        if not isinstance(data, list):
            raise SummaryError("GitHub 评论列表不是数组")
        comments.extend(item for item in data if isinstance(item, dict))
        if len(data) < 100:
            break
        page += 1
    return comments[:MAX_COMMENTS_TO_SCAN]


def marker_comment_id(comments: list[dict[str, Any]], marker: str) -> int | None:
    matches: list[tuple[str, int]] = []
    for comment in comments:
        user = comment.get("user")
        comment_id = comment.get("id")
        if (
            marker in str(comment.get("body", ""))
            and isinstance(user, dict)
            and user.get("login") == EXPECTED_AUTHOR
            and isinstance(comment_id, int)
        ):
            matches.append((str(comment.get("created_at", "")), comment_id))
    return sorted(matches)[-1][1] if matches else None


def post_or_update_comment(config: Config, body: str) -> None:
    comment_id = marker_comment_id(list_comments(config), config.marker)
    if comment_id is None:
        github_request(
            config,
            "POST",
            f"/repos/{config.repository}/issues/{config.pr_number}/comments",
            {"body": body},
        )
    else:
        github_request(config, "PATCH", f"/repos/{config.repository}/issues/comments/{comment_id}", {"body": body})


def run_self_test() -> int:
    body = """## 本次做了什么
- 替换旧审查
## 本次没做什么
- 未批准 Merge
## 下一步
- Human 审阅
"""
    sections = extract_sections(body)
    assert sections["本次做了什么"] == ["替换旧审查"]
    assert sections["本次没做什么"] == ["未批准 Merge"]
    passing = CheckResult("✅", "✅", "✅", "✅", "✅")
    summary = format_summary({"body": body, "changed_files": 3}, passing, SUMMARY_MARKER)
    assert "✅ 可以进入 Human 审阅" in summary
    assert "不代表 Human 已批准 Merge" in summary
    assert "Payload limits" not in summary
    assert "HIGH" not in summary
    failing = CheckResult("❌", "✅", "✅", "✅", "✅")
    assert "⚠ 建议修改后再合并" in format_summary({"body": body}, failing, SUMMARY_MARKER)
    comments = [
        {"id": 1, "created_at": "2026-01-01", "body": SUMMARY_MARKER, "user": {"login": EXPECTED_AUTHOR}},
        {"id": 2, "created_at": "2026-01-02", "body": SUMMARY_MARKER, "user": {"login": EXPECTED_AUTHOR}},
        {"id": 3, "created_at": "2026-01-03", "body": SUMMARY_MARKER, "user": {"login": "human"}},
    ]
    assert marker_comment_id(comments, SUMMARY_MARKER) == 2
    assert normalize_link("docs/a.md", "../README.md#top") == "README.md"
    print("SELF_TEST_OK")
    return 0


def run() -> int:
    config = load_config()
    pr = github_request(config, "GET", f"/repos/{config.repository}/pulls/{config.pr_number}")
    if not isinstance(pr, dict):
        raise SummaryError("GitHub PR 元数据不是对象")
    checks = run_checks(config.base_sha, config.head_sha)
    post_or_update_comment(config, format_summary(pr, checks, config.marker))
    if checks.failed:
        print("确定性检查失败；执行摘要已更新。", file=sys.stderr)
        return 1
    print("确定性检查通过；执行摘要已更新。")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Yu-AI-OS PR 执行摘要")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return run_self_test()
    try:
        run_self_test()
        return run()
    except (SummaryError, AssertionError, ValueError) as exc:
        print(f"执行摘要失败：{exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
