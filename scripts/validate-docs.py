from __future__ import annotations

import argparse
import sys
from pathlib import Path


REQUIRED_FILES = (
    "README.md",
    "ROADMAP.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "LICENSE",
    "AGENTS.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    ".github/FUNDING.yml",
    ".github/ISSUE_TEMPLATE/skill-request.md",
    ".github/ISSUE_TEMPLATE/bug-report.md",
    ".github/ISSUE_TEMPLATE/documentation-issue.md",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/pull_request_template.md",
    "docs/development/AL-00-baseline-audit.md",
    "docs/development/AL-24-public-readiness-audit.md",
    "docs/architecture/domain-contract.md",
    "docs/architecture/scope-boundaries.md",
    "docs/architecture/master-taxonomy-v1.md",
    "docs/architecture/taxonomy-audit.md",
    "docs/architecture/dependency-map.md",
    "docs/development/handoffs/AL-02-final-handoff.md",
    "docs/standards/skill-authoring-standard.md",
    "docs/standards/skill-naming-standard.md",
    "docs/standards/research-and-evidence-standard.md",
    "docs/standards/calculation-standard.md",
    "docs/standards/regulatory-content-standard.md",
    "docs/development/handoffs/AL-03-final-handoff.md",
    "docs/standards/testing-standard.md",
    "docs/standards/evaluation-standard.md",
    "docs/evaluation/before-after-report-template.md",
    "docs/development/handoffs/AL-04-final-handoff.md",
    "shared/README.md",
    "shared/glossaries/common-units.md",
    "shared/glossaries/inventory-state-terms.md",
    "shared/formulas/reorder-point.md",
    "shared/templates/calculation-output.md",
    "docs/development/handoffs/AL-05-final-handoff.md",
    "docs/development/handoffs/AL-06-final-handoff.md",
    "docs/development/handoffs/AL-07-final-handoff.md",
    "docs/development/handoffs/AL-08-final-handoff.md",
    "docs/development/handoffs/AL-09-final-handoff.md",
    "docs/development/handoffs/AL-10-final-handoff.md",
    "docs/development/handoffs/AL-11-final-handoff.md",
    "docs/development/handoffs/AL-12-final-handoff.md",
    "docs/development/handoffs/AL-13-final-handoff.md",
    "docs/development/handoffs/AL-14-final-handoff.md",
    "docs/development/handoffs/AL-15-final-handoff.md",
    "docs/development/handoffs/AL-16-final-handoff.md",
    "docs/development/handoffs/AL-17-final-handoff.md",
    "docs/development/handoffs/AL-18-final-handoff.md",
    "docs/architecture/specialization-roadmap.md",
    "docs/development/handoffs/AL-19-final-handoff.md",
    "docs/development/handoffs/AL-20-final-handoff.md",
    "docs/development/handoffs/AL-21-final-handoff.md",
    "docs/development/handoffs/AL-22-final-handoff.md",
    "docs/development/handoffs/AL-23-final-handoff.md",
    "docs/development/handoffs/AL-24-final-handoff.md",
    "skillsets/README.md",
    "specializations/canada/README.md",
    "specializations/canada/references/canadian-authority-map.md",
    "specializations/united-states/README.md",
    "specializations/united-states/references/us-authority-map.md",
    "specializations/food-cold-chain/README.md",
    "specializations/food-cold-chain/references/food-cold-chain-source-map.md",
    "specializations/dangerous-goods/README.md",
    "specializations/dangerous-goods/references/dangerous-goods-source-map.md",
    "specializations/international-logistics/README.md",
    "specializations/international-logistics/references/international-logistics-source-map.md",
)

REQUIRED_TOKENS = {
    "ROADMAP.md": (
        "AGENTLOGISTICS_AL_16_CANADA_COMPLIANCE_READY",
        "AGENTLOGISTICS_AL_18_PROFESSIONAL_SKILLSETS_READY",
        "AGENTLOGISTICS_AL_19_SPECIALIZATION_FRAMEWORK_READY",
        "AGENTLOGISTICS_AL_20_FOOD_COLD_CHAIN_READY",
        "AGENTLOGISTICS_AL_21_DANGEROUS_GOODS_READY",
        "AGENTLOGISTICS_AL_22_INTERNATIONAL_LOGISTICS_READY",
        "AGENTLOGISTICS_AL_23_INTEGRATION_VALIDATED",
        "AGENTLOGISTICS_AL_24_PUBLIC_READINESS_READY",
        "AGENTLOGISTICS_AL_25_V1_RC_AUDIT_COMPLETE",
        "Roadmap version: 0.1",
    ),
    "README.md": (
        "AGENTLOGISTICS_AL_24_PUBLIC_READINESS_READY",
    ),
    "docs/development/AL-00-baseline-audit.md": (
        "AGENTLOGISTICS_AL_00_BASELINE_READY",
    ),
    "docs/architecture/domain-contract.md": (
        "AGENTLOGISTICS_AL_01_DOMAIN_CONTRACT_READY",
    ),
    "docs/architecture/scope-boundaries.md": (
        "AGENTLOGISTICS_AL_01_DOMAIN_CONTRACT_READY",
    ),
    "docs/architecture/master-taxonomy-v1.md": (
        "AGENTLOGISTICS_AL_02_MASTER_TAXONOMY_READY",
    ),
    "docs/architecture/taxonomy-audit.md": (
        "AGENTLOGISTICS_AL_02_MASTER_TAXONOMY_READY",
    ),
    "docs/architecture/dependency-map.md": (
        "AGENTLOGISTICS_AL_02_MASTER_TAXONOMY_READY",
    ),
    "docs/development/handoffs/AL-02-final-handoff.md": (
        "AGENTLOGISTICS_AL_02_MASTER_TAXONOMY_READY",
    ),
    "docs/standards/skill-authoring-standard.md": (
        "AGENTLOGISTICS_AL_03_SKILL_STANDARD_READY",
    ),
    "docs/standards/skill-naming-standard.md": (
        "AGENTLOGISTICS_AL_03_SKILL_STANDARD_READY",
    ),
    "docs/standards/research-and-evidence-standard.md": (
        "AGENTLOGISTICS_AL_03_SKILL_STANDARD_READY",
    ),
    "docs/standards/calculation-standard.md": (
        "AGENTLOGISTICS_AL_03_SKILL_STANDARD_READY",
    ),
    "docs/standards/regulatory-content-standard.md": (
        "AGENTLOGISTICS_AL_03_SKILL_STANDARD_READY",
    ),
    "docs/development/handoffs/AL-03-final-handoff.md": (
        "AGENTLOGISTICS_AL_03_SKILL_STANDARD_READY",
    ),
    "docs/standards/testing-standard.md": (
        "AGENTLOGISTICS_AL_04_VALIDATION_FRAMEWORK_READY",
    ),
    "docs/standards/evaluation-standard.md": (
        "AGENTLOGISTICS_AL_04_VALIDATION_FRAMEWORK_READY",
    ),
    "docs/evaluation/before-after-report-template.md": (
        "AGENTLOGISTICS_AL_04_VALIDATION_FRAMEWORK_READY",
    ),
    "docs/development/handoffs/AL-04-final-handoff.md": (
        "AGENTLOGISTICS_AL_04_VALIDATION_FRAMEWORK_READY",
    ),
    "shared/README.md": (
        "AGENTLOGISTICS_AL_05_SHARED_FOUNDATIONS_READY",
    ),
    "shared/glossaries/common-units.md": (
        "AGENTLOGISTICS_AL_05_SHARED_FOUNDATIONS_READY",
    ),
    "shared/glossaries/inventory-state-terms.md": (
        "AGENTLOGISTICS_AL_05_SHARED_FOUNDATIONS_READY",
    ),
    "shared/formulas/reorder-point.md": (
        "AGENTLOGISTICS_AL_05_SHARED_FOUNDATIONS_READY",
    ),
    "shared/templates/calculation-output.md": (
        "AGENTLOGISTICS_AL_05_SHARED_FOUNDATIONS_READY",
    ),
    "docs/development/handoffs/AL-05-final-handoff.md": (
        "AGENTLOGISTICS_AL_05_SHARED_FOUNDATIONS_READY",
    ),
    "docs/development/handoffs/AL-06-final-handoff.md": (
        "AGENTLOGISTICS_AL_06_WAREHOUSE_CORE_READY",
    ),
    "docs/development/handoffs/AL-07-final-handoff.md": (
        "AGENTLOGISTICS_AL_07_INVENTORY_CONTROL_READY",
    ),
    "docs/development/handoffs/AL-08-final-handoff.md": (
        "AGENTLOGISTICS_AL_08_WAREHOUSE_PLANNING_READY",
    ),
    "docs/development/handoffs/AL-09-final-handoff.md": (
        "AGENTLOGISTICS_AL_09_FULFILLMENT_OPTIMIZATION_READY",
    ),
    "docs/development/handoffs/AL-10-final-handoff.md": (
        "AGENTLOGISTICS_AL_10_MATERIAL_HANDLING_READY",
    ),
    "docs/development/handoffs/AL-11-final-handoff.md": (
        "AGENTLOGISTICS_AL_11_TRANSPORTATION_CORE_READY",
    ),
    "docs/development/handoffs/AL-12-final-handoff.md": (
        "AGENTLOGISTICS_AL_12_SYSTEMS_DATA_READY",
    ),
    "docs/development/handoffs/AL-13-final-handoff.md": (
        "AGENTLOGISTICS_AL_13_CONTINUOUS_IMPROVEMENT_READY",
    ),
    "docs/development/handoffs/AL-14-final-handoff.md": (
        "AGENTLOGISTICS_AL_14_LABOR_PLANNING_READY",
    ),
    "docs/development/handoffs/AL-15-final-handoff.md": (
        "AGENTLOGISTICS_AL_15_REVERSE_LOGISTICS_READY",
    ),
    "docs/development/handoffs/AL-16-final-handoff.md": (
        "AGENTLOGISTICS_AL_16_CANADA_COMPLIANCE_READY",
    ),
    "specializations/canada/README.md": (
        "AGENTLOGISTICS_AL_16_CANADA_COMPLIANCE_READY",
    ),
    "specializations/canada/references/canadian-authority-map.md": (
        "AGENTLOGISTICS_AL_16_CANADA_COMPLIANCE_READY",
    ),
    "docs/development/handoffs/AL-17-final-handoff.md": (
        "AGENTLOGISTICS_AL_17_US_COMPLIANCE_READY",
    ),
    "specializations/united-states/README.md": (
        "AGENTLOGISTICS_AL_17_US_COMPLIANCE_READY",
    ),
    "specializations/united-states/references/us-authority-map.md": (
        "AGENTLOGISTICS_AL_17_US_COMPLIANCE_READY",
    ),
    "docs/development/handoffs/AL-18-final-handoff.md": (
        "AGENTLOGISTICS_AL_18_PROFESSIONAL_SKILLSETS_READY",
    ),
    "skillsets/README.md": (
        "AGENTLOGISTICS_AL_18_PROFESSIONAL_SKILLSETS_READY",
    ),
    "docs/architecture/specialization-roadmap.md": (
        "AGENTLOGISTICS_AL_19_SPECIALIZATION_FRAMEWORK_READY",
    ),
    "docs/development/handoffs/AL-19-final-handoff.md": (
        "AGENTLOGISTICS_AL_19_SPECIALIZATION_FRAMEWORK_READY",
    ),
    "docs/development/handoffs/AL-20-final-handoff.md": (
        "AGENTLOGISTICS_AL_20_FOOD_COLD_CHAIN_READY",
    ),
    "specializations/food-cold-chain/README.md": (
        "AGENTLOGISTICS_AL_20_FOOD_COLD_CHAIN_READY",
    ),
    "specializations/food-cold-chain/references/food-cold-chain-source-map.md": (
        "AGENTLOGISTICS_AL_20_FOOD_COLD_CHAIN_READY",
    ),
    "docs/development/handoffs/AL-21-final-handoff.md": (
        "AGENTLOGISTICS_AL_21_DANGEROUS_GOODS_READY",
    ),
    "specializations/dangerous-goods/README.md": (
        "AGENTLOGISTICS_AL_21_DANGEROUS_GOODS_READY",
    ),
    "specializations/dangerous-goods/references/dangerous-goods-source-map.md": (
        "AGENTLOGISTICS_AL_21_DANGEROUS_GOODS_READY",
    ),
    "docs/development/handoffs/AL-22-final-handoff.md": (
        "AGENTLOGISTICS_AL_22_INTERNATIONAL_LOGISTICS_READY",
    ),
    "specializations/international-logistics/README.md": (
        "AGENTLOGISTICS_AL_22_INTERNATIONAL_LOGISTICS_READY",
    ),
    "specializations/international-logistics/references/international-logistics-source-map.md": (
        "AGENTLOGISTICS_AL_22_INTERNATIONAL_LOGISTICS_READY",
    ),
    "docs/development/handoffs/AL-23-final-handoff.md": (
        "AGENTLOGISTICS_AL_23_INTEGRATION_VALIDATED",
    ),
    "docs/development/AL-24-public-readiness-audit.md": (
        "AGENTLOGISTICS_AL_24_PUBLIC_READINESS_READY",
    ),
    "docs/development/handoffs/AL-24-final-handoff.md": (
        "AGENTLOGISTICS_AL_24_PUBLIC_READINESS_READY",
    ),
}

README_PUBLIC_SECTIONS = (
    "## Who It Is For",
    "## What It Can Do",
    "## Quick Start",
    "## How To Use The Skills",
    "## Repository Layout",
    "## Skillsets",
    "## Limitations",
    "## Contributing",
    "## Security And Safety",
    "## License",
)

CONTRIBUTING_PUBLIC_SECTIONS = (
    "## Contribution Priorities",
    "## Skill Contributions",
    "## Evidence And Sources",
    "## Calculations",
    "## Safety Boundaries",
    "## Local Checks",
    "## Pull Request Checklist",
    "## Issues",
)

PUBLIC_READINESS_PHRASES = (
    "decision-support content",
    "Regulatory and safety-sensitive material is jurisdiction-specific",
    ".\\scripts\\validate-all.ps1",
    "AGENTLOGISTICS_AL_24_PUBLIC_READINESS_READY",
)

ISSUE_TEMPLATE_PHRASES = (
    "Evidence And Sources",
    "Safety Or Approval Boundaries",
    "Validation",
)

PR_TEMPLATE_PHRASES = (
    "Roadmap Wave",
    "Evidence And Sources",
    "Safety And Approval Boundaries",
    "Validation",
)

SPECIALIZATION_CANDIDATES = (
    "cold-chain",
    "food-logistics",
    "dangerous-goods",
    "ecommerce",
    "manufacturing",
    "retail-distribution",
    "automotive",
    "pharmaceuticals",
    "international-logistics",
)

SPECIALIZATION_FIELDS = (
    "domain need",
    "unique knowledge",
    "unique regulations",
    "unique workflows",
    "shared core skills",
    "new atomic skills required",
    "priority",
)

IGNORED_DIRS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}


def find_empty_dirs(repo_root: Path) -> list[Path]:
    empty_dirs: list[Path] = []
    for path in sorted(p for p in repo_root.rglob("*") if p.is_dir()):
        relative_parts = path.relative_to(repo_root).parts
        if any(part in IGNORED_DIRS for part in relative_parts):
            continue
        if not any(path.iterdir()):
            empty_dirs.append(path)
    return empty_dirs


def validate_specialization_roadmap(repo_root: Path) -> list[str]:
    errors: list[str] = []
    relative = "docs/architecture/specialization-roadmap.md"
    path = repo_root / relative
    if not path.is_file():
        return errors

    text = path.read_text(encoding="utf-8")
    lower_text = text.lower()
    for candidate in SPECIALIZATION_CANDIDATES:
        if candidate not in text:
            errors.append(f"{relative}: missing candidate {candidate}")
    for field in SPECIALIZATION_FIELDS:
        if field not in lower_text:
            errors.append(f"{relative}: missing candidate field {field}")
    for phrase in (
        "Universal core skills must not depend on specializations.",
        "Do not create industry specialization packages in AL-19.",
        "qualified review",
        "source maps",
    ):
        if phrase not in text:
            errors.append(f"{relative}: missing specialization boundary phrase {phrase}")
    return errors


def validate_public_readiness(repo_root: Path) -> list[str]:
    errors: list[str] = []

    readme = repo_root / "README.md"
    if readme.is_file():
        text = readme.read_text(encoding="utf-8")
        for section in README_PUBLIC_SECTIONS:
            if section not in text:
                errors.append(f"README.md: missing public-readiness section {section}")
        for phrase in PUBLIC_READINESS_PHRASES:
            if phrase not in text:
                errors.append(f"README.md: missing public-readiness phrase {phrase}")

    contributing = repo_root / "CONTRIBUTING.md"
    if contributing.is_file():
        text = contributing.read_text(encoding="utf-8")
        for section in CONTRIBUTING_PUBLIC_SECTIONS:
            if section not in text:
                errors.append(f"CONTRIBUTING.md: missing contributor section {section}")
        for phrase in (
            "Do not create empty folders",
            "authoritative sources",
            "Validate unit compatibility explicitly.",
            "Do not include secrets",
        ):
            if phrase not in text:
                errors.append(f"CONTRIBUTING.md: missing contributor phrase {phrase}")

    for relative in (
        ".github/ISSUE_TEMPLATE/skill-request.md",
        ".github/ISSUE_TEMPLATE/bug-report.md",
        ".github/ISSUE_TEMPLATE/documentation-issue.md",
    ):
        path = repo_root / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in ISSUE_TEMPLATE_PHRASES:
            if phrase not in text:
                errors.append(f"{relative}: missing issue-template phrase {phrase}")

    pr_template = repo_root / ".github/pull_request_template.md"
    if pr_template.is_file():
        text = pr_template.read_text(encoding="utf-8")
        for phrase in PR_TEMPLATE_PHRASES:
            if phrase not in text:
                errors.append(f".github/pull_request_template.md: missing PR-template phrase {phrase}")

    audit = repo_root / "docs/development/AL-24-public-readiness-audit.md"
    if audit.is_file():
        text = audit.read_text(encoding="utf-8")
        for phrase in (
            "Public Documentation Inventory",
            "Readiness Checklist",
            "GitHub repository description, topics",
            "AL-25 v1 release candidate audit",
        ):
            if phrase not in text:
                errors.append(f"docs/development/AL-24-public-readiness-audit.md: missing audit phrase {phrase}")

    return errors


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        path = repo_root / relative
        if not path.is_file():
            errors.append(f"Missing required file: {relative}")

    for relative, tokens in REQUIRED_TOKENS.items():
        path = repo_root / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for token in tokens:
            if token not in text:
                errors.append(f"{relative}: missing completion token {token}")

    for path in find_empty_dirs(repo_root):
        errors.append(f"Empty directory should not be committed: {path.relative_to(repo_root)}")

    errors.extend(validate_specialization_roadmap(repo_root))
    errors.extend(validate_public_readiness(repo_root))
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

    print("Validated AgentLogistics documentation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
