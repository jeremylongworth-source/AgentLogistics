from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


DEFAULT_SOURCE_FILES = (
    "specializations/canada/references/canadian-authority-map.md",
    "specializations/united-states/references/us-authority-map.md",
    "specializations/food-cold-chain/references/food-cold-chain-source-map.md",
    "specializations/dangerous-goods/references/dangerous-goods-source-map.md",
    "specializations/international-logistics/references/international-logistics-source-map.md",
)

URL_RE = re.compile(r"https?://[^\s<>)`\"']+")
ACCEPTED_RESTRICTED_STATUSES = {401, 403, 405, 429}
BROKEN_STATUSES = {404, 410}
FATAL_STATUSES = {"BROKEN", "CHECK"}
TRANSIENT_STATUSES = {"ERROR", "TLS_ERROR"}


@dataclass(frozen=True)
class LinkResult:
    url: str
    status: str
    detail: str


def normalize_url(raw_url: str) -> str:
    return raw_url.rstrip(".,;:]}")


def source_files(repo_root: Path, selected_files: list[str] | None) -> list[Path]:
    if selected_files:
        return [repo_root / selected for selected in selected_files]
    return [repo_root / selected for selected in DEFAULT_SOURCE_FILES]


def extract_urls(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return sorted({normalize_url(match.group(0)) for match in URL_RE.finditer(text)})


def request_url(url: str, method: str, timeout: int) -> int:
    request = Request(
        url,
        method=method,
        headers={
            "User-Agent": "AgentLogistics-source-link-audit/1.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        },
    )
    with urlopen(request, timeout=timeout) as response:
        return int(response.status)


def check_url(url: str, timeout: int) -> LinkResult:
    try:
        status = request_url(url, "HEAD", timeout)
    except HTTPError as exc:
        try:
            status = request_url(url, "GET", timeout)
        except HTTPError as get_exc:
            status = int(get_exc.code)
        except URLError as get_exc:
            reason = str(get_exc.reason)
            if "CERTIFICATE_VERIFY_FAILED" in reason:
                return LinkResult(url, "TLS_ERROR", reason)
            return LinkResult(url, "ERROR", reason)
        except TimeoutError:
            return LinkResult(url, "ERROR", "timeout")
    except URLError as exc:
        reason = str(exc.reason)
        if "CERTIFICATE_VERIFY_FAILED" in reason:
            return LinkResult(url, "TLS_ERROR", reason)
        return LinkResult(url, "ERROR", reason)
    except TimeoutError:
        return LinkResult(url, "ERROR", "timeout")

    if 200 <= status < 400:
        return LinkResult(url, "OK", str(status))
    if status in ACCEPTED_RESTRICTED_STATUSES:
        return LinkResult(url, "RESTRICTED", str(status))
    if status in BROKEN_STATUSES:
        return LinkResult(url, "BROKEN", str(status))
    if 500 <= status:
        return LinkResult(url, "ERROR", str(status))
    return LinkResult(url, "CHECK", str(status))


def validate(
    repo_root: Path,
    selected_files: list[str] | None,
    timeout: int,
    allow_tls_errors: bool,
    strict_transient: bool,
) -> list[str]:
    errors: list[str] = []
    seen_urls: set[str] = set()
    results: list[LinkResult] = []

    for path in source_files(repo_root, selected_files):
        if not path.is_file():
            errors.append(f"Missing source file: {path.relative_to(repo_root)}")
            continue
        for url in extract_urls(path):
            if url in seen_urls:
                continue
            seen_urls.add(url)
            results.append(check_url(url, timeout))

    for result in results:
        print(f"{result.status}\t{result.detail}\t{result.url}")
        if result.status == "TLS_ERROR" and allow_tls_errors:
            continue
        if result.status in FATAL_STATUSES:
            errors.append(f"{result.url}: {result.status.lower()} ({result.detail})")
        if strict_transient and result.status in TRANSIENT_STATUSES:
            errors.append(f"{result.url}: {result.status.lower()} ({result.detail})")

    if not seen_urls:
        errors.append("No source URLs found.")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=Path(__file__).resolve().parents[1])
    parser.add_argument("--timeout", type=int, default=15)
    parser.add_argument("--file", action="append", dest="files")
    parser.add_argument(
        "--allow-tls-errors",
        action="store_true",
        help="Report TLS certificate failures without failing a strict transient audit.",
    )
    parser.add_argument(
        "--strict-transient",
        action="store_true",
        help="Fail on transient network and TLS errors instead of reporting them.",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    errors = validate(
        repo_root,
        args.files,
        args.timeout,
        args.allow_tls_errors,
        args.strict_transient,
    )
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("Validated AgentLogistics source links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
