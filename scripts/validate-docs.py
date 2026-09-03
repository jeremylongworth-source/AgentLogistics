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
    "docs/development/AL-00-baseline-audit.md",
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
)

REQUIRED_TOKENS = {
    "ROADMAP.md": (
        "AGENTLOGISTICS_AL_16_CANADA_COMPLIANCE_READY",
        "AGENTLOGISTICS_AL_25_V1_RC_AUDIT_COMPLETE",
        "Roadmap version: 0.1",
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
}

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
