from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


CANADA_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_16_CANADA_COMPLIANCE_READY"
US_COMPLETION_TOKEN = "AGENTLOGISTICS_AL_17_US_COMPLIANCE_READY"
PACKAGE_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
PLACEHOLDER_RE = re.compile(r"\b(TODO|TBD|FIXME|PLACEHOLDER)\b", re.IGNORECASE)

REQUIRED_CANADA_PACKAGES = {
    "identify-canadian-logistics-jurisdiction",
    "research-canadian-workplace-safety",
    "research-canadian-material-handling-safety",
    "research-canadian-powered-equipment-safety",
    "research-canadian-transportation-rules",
    "research-canadian-dangerous-goods-rules",
    "research-canadian-commercial-vehicle-safety",
    "research-canadian-loading-security",
    "research-canadian-logistics-documents",
    "research-canadian-import-export-controls",
    "research-canadian-storage-requirements",
}
REQUIRED_US_PACKAGES = {
    "identify-us-logistics-jurisdiction",
    "research-us-workplace-safety",
    "research-us-material-handling-safety",
    "research-us-powered-equipment-safety",
    "research-us-transportation-rules",
    "research-us-hazardous-materials-rules",
    "research-us-commercial-vehicle-safety",
    "research-us-loading-security",
    "research-us-logistics-documents",
    "research-us-import-export-controls",
    "research-us-storage-requirements",
}

REQUIRED_SECTIONS = (
    "Overview",
    "Triggers",
    "Non-Triggers",
    "Required Inputs",
    "Optional Inputs",
    "Assumptions",
    "Core Workflow",
    "Calculations",
    "Validation",
    "Exception Handling",
    "Source Usage",
    "Output Contract",
    "Safety Requirements",
    "References",
    "Examples",
    "Testing",
)

REQUIRED_AUTHORITY_MAP_PHRASES = (
    CANADA_COMPLETION_TOKEN,
    "Do not invent a single unified Canadian warehouse law.",
    "Access date for the AL-16 source list: 2026-09-03.",
    "federal workplace safety",
    "provincial and territorial workplace safety",
    "WHMIS hazardous product communication",
    "TDG dangerous goods transportation",
    "commercial vehicle and motor carrier safety",
    "import and export border controls",
    "qualified-review handoffs",
)
REQUIRED_US_AUTHORITY_MAP_PHRASES = (
    US_COMPLETION_TOKEN,
    "Do not invent a single unified US warehouse law.",
    "Access date for the AL-17 source list: 2026-09-03.",
    "federal workplace safety",
    "OSHA-approved state-plan workplace safety",
    "Hazard Communication hazardous chemical communication",
    "PHMSA hazardous materials transportation",
    "FMCSA commercial vehicle and motor carrier safety",
    "import and export border controls",
    "qualified-review handoffs",
)

REQUIRED_SOURCE_URLS = (
    "https://www.ccohs.ca/oshanswers/legisl/legislation/intro.html",
    "https://www.canada.ca/en/employment-social-development/services/health-safety/workplace-safety.html",
    "https://laws-lois.justice.gc.ca/eng/regulations/Sor-86-304/index.html",
    "https://www.canada.ca/en/health-canada/services/environmental-workplace-health/occupational-health-safety/workplace-hazardous-materials-information-system/roles-responsibilities-whmis.html",
    "https://tc.canada.ca/en/dangerous-goods/transportation-dangerous-goods-canada",
    "https://tc.canada.ca/en/dangerous-goods/safety-awareness-materials-faq",
    "https://tc.canada.ca/en/road-transportation/motor-carriers-commercial-vehicles-drivers",
    "https://tc.canada.ca/en/road-transportation/motor-vehicle-safety/commercial-vehicle-safety",
    "https://www.cbsa-asfc.gc.ca/import/guide-eng.html",
    "https://www.cbsa-asfc.gc.ca/services/export/menu-eng.html",
)
REQUIRED_US_SOURCE_URLS = (
    "https://www.osha.gov/warehousing",
    "https://www.osha.gov/stateplans",
    "https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.1200",
    "https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.178",
    "https://www.phmsa.dot.gov/standards-rulemaking/hazmat/hazardous-materials-regulations",
    "https://www.fmcsa.dot.gov/regulations/hours-of-service",
    "https://www.fmcsa.dot.gov/regulations/cargo-securement/cargo-securement-rules",
    "https://www.cbp.gov/trade/basic-import-export",
    "https://www.cbp.gov/trade/automated/how-to-use-ace/introduction",
    "https://www.epa.gov/hw/hazardous-waste-transportation",
    "https://www.ecfr.gov/current/title-49",
)

BLOCKED_OUTPUT_PHRASES = (
    "legal advice",
    "compliance declarations",
    "safety approvals",
    "certifications",
    "customs approvals",
    "dangerous-goods classification approvals",
    "live system changes",
)
US_BLOCKED_OUTPUT_PHRASES = (
    "legal advice",
    "compliance declarations",
    "safety approvals",
    "certifications",
    "customs approvals",
    "hazardous-materials classification approvals",
    "environmental determinations",
    "live system changes",
)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}

    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def package_paths(repo_root: Path) -> list[Path]:
    specializations_root = repo_root / "specializations"
    if not specializations_root.is_dir():
        return []
    return sorted(specializations_root.glob("*/*/SKILL.md"))


def check_required_sections(relative: Path, text: str) -> list[str]:
    errors: list[str] = []
    positions: list[int] = []

    for section in REQUIRED_SECTIONS:
        match = re.search(rf"^## {re.escape(section)}\s*$", text, re.MULTILINE)
        if not match:
            errors.append(f"{relative}: missing required section ## {section}")
            continue
        positions.append(match.start())

    if len(positions) == len(REQUIRED_SECTIONS) and positions != sorted(positions):
        errors.append(f"{relative}: required sections are not in standard order")

    return errors


def validate_package(repo_root: Path, path: Path) -> list[str]:
    errors: list[str] = []
    relative = path.relative_to(repo_root)
    package_dir = path.parent
    package_name = package_dir.name
    specialization = path.relative_to(repo_root).parts[1]
    text = path.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(text)

    if specialization == "canada":
        completion_token = CANADA_COMPLETION_TOKEN
        country_boundary = "no single unified Canadian warehouse law"
        reference_name = "canada-compliance-checklist.md"
        source_urls = REQUIRED_SOURCE_URLS
        label = "Canada"
    elif specialization == "united-states":
        completion_token = US_COMPLETION_TOKEN
        country_boundary = "no single unified US warehouse law"
        reference_name = "us-compliance-checklist.md"
        source_urls = REQUIRED_US_SOURCE_URLS
        label = "United States"
    else:
        return [f"{relative}: unexpected specialization {specialization}"]

    if PLACEHOLDER_RE.search(text):
        errors.append(f"{relative}: unresolved placeholder marker")
    if not PACKAGE_NAME_RE.match(package_name):
        errors.append(f"{relative}: invalid package directory name {package_name}")
    if frontmatter.get("name") != package_name:
        errors.append(f"{relative}: frontmatter name must match directory {package_name}")
    if len(frontmatter.get("description", "")) < 60:
        errors.append(f"{relative}: frontmatter description is missing or too weak")
    if frontmatter.get("license") != "MIT":
        errors.append(f"{relative}: frontmatter license must be MIT")

    errors.extend(check_required_sections(relative, text))

    for phrase in (
        "Use current official sources",
        country_boundary,
        "qualified-review",
        "Do not state that",
    ):
        if phrase not in text:
            errors.append(f"{relative}: missing {label} specialization boundary phrase {phrase}")

    agent_config = package_dir / "agents" / "openai.yaml"
    if not agent_config.is_file():
        errors.append(f"{relative}: missing agents/openai.yaml")
    else:
        config_text = agent_config.read_text(encoding="utf-8")
        config_relative = agent_config.relative_to(repo_root)
        for required in ("interface:", "display_name:", "short_description:", "default_prompt:"):
            if required not in config_text:
                errors.append(f"{config_relative}: missing {required}")
        if f"${package_name}" not in config_text:
            errors.append(f"{config_relative}: default prompt must mention ${package_name}")
        if PLACEHOLDER_RE.search(config_text):
            errors.append(f"{config_relative}: unresolved placeholder marker")

    reference_path = package_dir / "references" / reference_name
    if not reference_path.is_file():
        errors.append(f"{relative}: missing references/{reference_name}")
    else:
        reference_text = reference_path.read_text(encoding="utf-8")
        reference_relative = reference_path.relative_to(repo_root)
        if completion_token not in reference_text:
            errors.append(f"{reference_relative}: missing specialization completion token")
        for url in source_urls:
            if url not in reference_text:
                errors.append(f"{reference_relative}: missing official source URL {url}")
        if PLACEHOLDER_RE.search(reference_text):
            errors.append(f"{reference_relative}: unresolved placeholder marker")

    return errors


def validate_canada_root(repo_root: Path) -> list[str]:
    errors: list[str] = []
    canada_root = repo_root / "specializations" / "canada"
    if not canada_root.is_dir():
        return ["Missing Canada specialization directory: specializations/canada"]

    readme_path = canada_root / "README.md"
    if not readme_path.is_file():
        errors.append("Missing Canada specialization README: specializations/canada/README.md")
    else:
        readme_text = readme_path.read_text(encoding="utf-8")
        if CANADA_COMPLETION_TOKEN not in readme_text:
            errors.append("specializations/canada/README.md: missing AL-16 completion token")
        for package_name in REQUIRED_CANADA_PACKAGES:
            if package_name not in readme_text:
                errors.append(f"specializations/canada/README.md: missing package {package_name}")
        for phrase in BLOCKED_OUTPUT_PHRASES:
            if phrase not in readme_text:
                errors.append(f"specializations/canada/README.md: missing boundary phrase {phrase}")

    authority_path = canada_root / "references" / "canadian-authority-map.md"
    if not authority_path.is_file():
        errors.append("Missing Canadian authority map: specializations/canada/references/canadian-authority-map.md")
    else:
        authority_text = authority_path.read_text(encoding="utf-8")
        for phrase in REQUIRED_AUTHORITY_MAP_PHRASES:
            if phrase not in authority_text:
                errors.append(f"{authority_path.relative_to(repo_root)}: missing {phrase}")
        for url in REQUIRED_SOURCE_URLS:
            if url not in authority_text:
                errors.append(f"{authority_path.relative_to(repo_root)}: missing official source URL {url}")

    return errors


def validate_us_root(repo_root: Path) -> list[str]:
    errors: list[str] = []
    us_root = repo_root / "specializations" / "united-states"
    if not us_root.is_dir():
        return ["Missing United States specialization directory: specializations/united-states"]

    readme_path = us_root / "README.md"
    if not readme_path.is_file():
        errors.append("Missing United States specialization README: specializations/united-states/README.md")
    else:
        readme_text = readme_path.read_text(encoding="utf-8")
        if US_COMPLETION_TOKEN not in readme_text:
            errors.append("specializations/united-states/README.md: missing AL-17 completion token")
        for package_name in REQUIRED_US_PACKAGES:
            if package_name not in readme_text:
                errors.append(f"specializations/united-states/README.md: missing package {package_name}")
        for phrase in US_BLOCKED_OUTPUT_PHRASES:
            if phrase not in readme_text:
                errors.append(f"specializations/united-states/README.md: missing boundary phrase {phrase}")

    authority_path = us_root / "references" / "us-authority-map.md"
    if not authority_path.is_file():
        errors.append("Missing US authority map: specializations/united-states/references/us-authority-map.md")
    else:
        authority_text = authority_path.read_text(encoding="utf-8")
        for phrase in REQUIRED_US_AUTHORITY_MAP_PHRASES:
            if phrase not in authority_text:
                errors.append(f"{authority_path.relative_to(repo_root)}: missing {phrase}")
        for url in REQUIRED_US_SOURCE_URLS:
            if url not in authority_text:
                errors.append(f"{authority_path.relative_to(repo_root)}: missing official source URL {url}")

    return errors


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    paths = package_paths(repo_root)

    errors.extend(validate_canada_root(repo_root))
    errors.extend(validate_us_root(repo_root))

    found_canada_packages = {
        path.parent.name for path in paths if path.relative_to(repo_root).parts[1] == "canada"
    }
    found_us_packages = {
        path.parent.name for path in paths if path.relative_to(repo_root).parts[1] == "united-states"
    }
    for package_name in sorted(REQUIRED_CANADA_PACKAGES - found_canada_packages):
        errors.append(f"Missing Canada specialization package: specializations/canada/{package_name}")
    for package_name in sorted(REQUIRED_US_PACKAGES - found_us_packages):
        errors.append(f"Missing United States specialization package: specializations/united-states/{package_name}")

    for path in paths:
        specialization = path.relative_to(repo_root).parts[1]
        if specialization == "canada" and path.parent.name not in REQUIRED_CANADA_PACKAGES:
            errors.append(f"{path.relative_to(repo_root)}: unexpected Canada specialization package")
        if specialization == "united-states" and path.parent.name not in REQUIRED_US_PACKAGES:
            errors.append(f"{path.relative_to(repo_root)}: unexpected United States specialization package")
        errors.extend(validate_package(repo_root, path))

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    errors = validate(repo_root)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"Validated {len(package_paths(repo_root))} specialization package(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
