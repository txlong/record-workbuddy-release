#!/usr/bin/env python3
"""Fetch and record WorkBuddy release metadata."""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


DEFAULT_URL_TEMPLATE = "https://www.codebuddy.cn/v2/update?platform={platform}"
DEFAULT_PLATFORMS = (
    "workbuddy-darwin-arm64",
    "workbuddy-darwin-x64",
    "workbuddy-win32-x64-user",
)
DEFAULT_RECORD_PATH = "data/releases.json"
DEFAULT_LATEST_PATH = "data/latest.json"
DEFAULT_README_PATH = "README.md"
REQUIRED_FIELDS = ("version", "url", "productVersion", "sha256hash", "timestamp")
README_START_MARKER = "<!-- workbuddy-latest:start -->"
README_END_MARKER = "<!-- workbuddy-latest:end -->"
README_HISTORY_START_MARKER = "<!-- workbuddy-history:start -->"
README_HISTORY_END_MARKER = "<!-- workbuddy-history:end -->"
PLATFORM_LABELS = {
    "workbuddy-darwin-arm64": "macOS Apple Silicon",
    "workbuddy-darwin-x64": "macOS Intel",
    "workbuddy-win32-x64-user": "Windows x64",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(payload, file, ensure_ascii=False, indent=2, sort_keys=True)
        file.write("\n")


def write_text_if_changed(path: Path, content: str) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def build_url(url_template: str, platform: str) -> str:
    if "{platform}" in url_template:
        return url_template.format(platform=platform)

    separator = "&" if "?" in url_template else "?"
    return f"{url_template}{separator}{urlencode({'platform': platform})}"


def parse_platforms(values: list[str]) -> list[str]:
    platforms: list[str] = []
    for value in values:
        for platform in value.split(","):
            platform = platform.strip()
            if platform and platform not in platforms:
                platforms.append(platform)
    return platforms


def fetch_release(url: str, timeout: int) -> dict[str, Any]:
    request = Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "record-workbuddy-release/1.0",
        },
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            payload = response.read().decode(charset)
    except HTTPError as exc:
        raise RuntimeError(f"HTTP {exc.code} while fetching {url}") from exc
    except URLError as exc:
        raise RuntimeError(f"Network error while fetching {url}: {exc.reason}") from exc

    try:
        release = json.loads(payload)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Response is not valid JSON: {exc}") from exc

    if not isinstance(release, dict):
        raise RuntimeError("Response JSON must be an object")

    missing = [field for field in REQUIRED_FIELDS if field not in release]
    if missing:
        raise RuntimeError(f"Response is missing required field(s): {', '.join(missing)}")

    return release


def release_key(platform: str, release: dict[str, Any]) -> str:
    sha256hash = str(release.get("sha256hash") or "").strip()
    if sha256hash:
        return f"{platform}|sha256:{sha256hash}"

    version = str(release.get("version") or "").strip()
    url = str(release.get("url") or "").strip()
    product_version = str(release.get("productVersion") or "").strip()
    return f"{platform}|release:{version}|{product_version}|{url}"


def legacy_release_key(release: dict[str, Any]) -> str:
    sha256hash = str(release.get("sha256hash") or "").strip()
    if sha256hash:
        return f"sha256:{sha256hash}"

    version = str(release.get("version") or "").strip()
    url = str(release.get("url") or "").strip()
    product_version = str(release.get("productVersion") or "").strip()
    return f"release:{version}|{product_version}|{url}"


def normalize_record(platform: str, release: dict[str, Any], source: str, now: str) -> dict[str, Any]:
    return {
        "firstSeenAt": now,
        "lastSeenAt": now,
        "platform": platform,
        "release": release,
        "releaseKey": release_key(platform, release),
        "source": source,
    }


def record_matches(record: dict[str, Any], platform: str, release: dict[str, Any]) -> bool:
    key = release_key(platform, release)
    if str(record.get("releaseKey")) == key:
        return True

    # Compatibility for records created before platform was stored in releaseKey.
    if "platform" not in record and str(record.get("releaseKey")) == legacy_release_key(release):
        return True

    return False


def upsert_record_metadata(
    record: dict[str, Any],
    platform: str,
    release: dict[str, Any],
    source: str,
) -> bool:
    changed = False
    desired = {
        "platform": platform,
        "releaseKey": release_key(platform, release),
        "source": source,
    }
    for key, value in desired.items():
        if record.get(key) != value:
            record[key] = value
            changed = True
    return changed


def record_timestamp(record: dict[str, Any]) -> int:
    release = record.get("release")
    if not isinstance(release, dict):
        return 0
    try:
        return int(release.get("timestamp") or 0)
    except (TypeError, ValueError):
        return 0


def latest_records_by_platform(records: list[Any]) -> dict[str, dict[str, Any]]:
    latest: dict[str, dict[str, Any]] = {}
    for record in records:
        if not isinstance(record, dict):
            continue
        platform = str(record.get("platform") or "").strip()
        if not platform:
            continue
        if platform not in latest or record_timestamp(record) >= record_timestamp(latest[platform]):
            latest[platform] = record
    return latest


def short_hash(value: Any) -> str:
    text = str(value or "").strip()
    if not text:
        return "-"
    return f"`{text[:12]}`"


def platform_label(platform: str) -> str:
    return PLATFORM_LABELS.get(platform, platform)


def release_version(release: dict[str, Any]) -> str:
    return str(release.get("version") or release.get("productVersion") or "").strip()


def markdown_link(label: str, url: str) -> str:
    if not url:
        return "-"
    return f"[{label}]({url})"


def render_latest_section(records: list[Any]) -> str:
    latest = latest_records_by_platform(records)
    valid_records = [record for record in latest.values() if isinstance(record.get("release"), dict)]
    if not valid_records:
        body = "_暂无版本记录。_"
    else:
        newest_timestamp = max(record_timestamp(record) for record in valid_records)
        newest_records = [
            record
            for record in valid_records
            if record_timestamp(record) == newest_timestamp
        ]
        newest_versions = sorted(
            {
                str(record["release"].get("version") or record["release"].get("productVersion") or "").strip()
                for record in newest_records
            }
        )
        newest_version = ", ".join(version for version in newest_versions if version) or "unknown"
        platform_names = ", ".join(platform_label(str(record.get("platform"))) for record in newest_records)

        rows = [
            "| 平台 | 最新版本 | 下载 | SHA256 | 首次记录 |",
            "| --- | --- | --- | --- | --- |",
        ]
        for platform in sorted(latest):
            record = latest[platform]
            release = record.get("release")
            if not isinstance(release, dict):
                continue
            version = release_version(release)
            url = str(release.get("url") or "").strip()
            link = markdown_link("下载", url)
            marker = " **最新**" if record_timestamp(record) == newest_timestamp else ""
            rows.append(
                "| {platform} | `{version}`{marker} | {link} | {sha256} | `{first_seen}` |".format(
                    platform=platform_label(platform),
                    version=version or "-",
                    marker=marker,
                    link=link,
                    sha256=short_hash(release.get("sha256hash")),
                    first_seen=record.get("firstSeenAt") or "-",
                )
            )

        body = "\n".join(
            [
                f"**当前最新版本：`{newest_version}`**",
                "",
                f"最新平台：{platform_names}",
                "",
                *rows,
            ]
        )

    return f"{README_START_MARKER}\n{body}\n{README_END_MARKER}"


def render_history_section(records: list[Any]) -> str:
    valid_records = [
        record
        for record in records
        if isinstance(record, dict) and isinstance(record.get("release"), dict)
    ]
    if not valid_records:
        body = "_暂无历史版本记录。_"
    else:
        rows = [
            "| 版本 | 平台 | 下载 | SHA256 | 接口时间戳 | 首次记录 |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
        for record in sorted(
            valid_records,
            key=lambda item: (
                record_timestamp(item),
                str(item.get("firstSeenAt") or ""),
                str(item.get("platform") or ""),
            ),
            reverse=True,
        ):
            release = record["release"]
            platform = str(record.get("platform") or "")
            version = release_version(release)
            url = str(release.get("url") or "").strip()
            rows.append(
                "| {version} | {platform} | {link} | {sha256} | `{timestamp}` | `{first_seen}` |".format(
                    version=f"`{version}`" if version else "-",
                    platform=platform_label(platform),
                    link=markdown_link("下载", url),
                    sha256=short_hash(release.get("sha256hash")),
                    timestamp=release.get("timestamp") or "-",
                    first_seen=record.get("firstSeenAt") or "-",
                )
            )
        body = "\n".join(rows)

    return f"{README_HISTORY_START_MARKER}\n{body}\n{README_HISTORY_END_MARKER}"


def replace_marked_section(
    content: str,
    start_marker: str,
    end_marker: str,
    heading: str,
    section: str,
    insert_after: str,
) -> str:
    if start_marker in content and end_marker in content:
        start = content.index(start_marker)
        end = content.index(end_marker, start) + len(end_marker)
        return f"{content[:start]}{section}{content[end:]}"

    insert_at = content.find(insert_after)
    if insert_at != -1:
        insert_at += len(insert_after)
        return f"{content[:insert_at]}\n\n## {heading}\n\n{section}{content[insert_at:]}"

    return f"{content.rstrip()}\n\n## {heading}\n\n{section}\n"


def update_readme(readme_path: Path, records: list[Any]) -> bool:
    if not readme_path.exists():
        return False

    content = readme_path.read_text(encoding="utf-8")
    latest_section = render_latest_section(records)
    history_section = render_history_section(records)

    first_block_end = content.find("\n\n")
    intro_end = content.find("\n\n", first_block_end + 2) if first_block_end != -1 else -1
    latest_insert_after = content[: intro_end + 2] if intro_end != -1 else content
    next_content = replace_marked_section(
        content,
        README_START_MARKER,
        README_END_MARKER,
        "最新版本",
        latest_section,
        latest_insert_after,
    )
    next_content = replace_marked_section(
        next_content,
        README_HISTORY_START_MARKER,
        README_HISTORY_END_MARKER,
        "历史版本",
        history_section,
        README_END_MARKER,
    )

    return write_text_if_changed(readme_path, next_content)


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch and record WorkBuddy release metadata.")
    parser.add_argument("--url-template", default=os.getenv("WORKBUDDY_UPDATE_URL_TEMPLATE", DEFAULT_URL_TEMPLATE))
    parser.add_argument(
        "--platform",
        action="append",
        default=[],
        help="Platform to check. Can be repeated or comma-separated.",
    )
    parser.add_argument("--record-path", default=os.getenv("WORKBUDDY_RECORD_PATH", DEFAULT_RECORD_PATH))
    parser.add_argument("--latest-path", default=os.getenv("WORKBUDDY_LATEST_PATH", DEFAULT_LATEST_PATH))
    parser.add_argument("--readme-path", default=os.getenv("WORKBUDDY_README_PATH", DEFAULT_README_PATH))
    parser.add_argument("--timeout", type=int, default=int(os.getenv("WORKBUDDY_TIMEOUT", "30")))
    args = parser.parse_args()

    platform_values = args.platform or [os.getenv("WORKBUDDY_PLATFORMS", ",".join(DEFAULT_PLATFORMS))]
    platforms = parse_platforms(platform_values)
    if not platforms:
        raise RuntimeError("At least one platform must be configured")

    record_path = Path(args.record_path)
    latest_path = Path(args.latest_path)
    readme_path = Path(args.readme_path)
    now = utc_now()

    records = read_json(record_path, [])
    if not isinstance(records, list):
        raise RuntimeError(f"{record_path} must contain a JSON array")

    latest_releases = {}
    changed = False
    new_count = 0

    for platform in platforms:
        source = build_url(args.url_template, platform)
        release = fetch_release(source, args.timeout)
        current_key = release_key(platform, release)
        latest_releases[platform] = {
            "release": release,
            "releaseKey": current_key,
            "source": source,
        }

        existing_record = next(
            (
                record
                for record in records
                if isinstance(record, dict) and record_matches(record, platform, release)
            ),
            None,
        )

        if existing_record is None:
            records.append(normalize_record(platform, release, source, now))
            changed = True
            new_count += 1
            print(f"Recorded new release: {current_key}")
        else:
            changed = upsert_record_metadata(existing_record, platform, release, source) or changed
            print(f"Already recorded: {current_key}")

    readme_changed = update_readme(readme_path, records)

    if not changed and not readme_changed:
        return 0

    if changed:
        latest = {
            "recordedAt": now,
            "platforms": latest_releases,
        }
        write_json(record_path, records)
        write_json(latest_path, latest)

    print(f"Updated release files; new releases: {new_count}; readme changed: {readme_changed}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
