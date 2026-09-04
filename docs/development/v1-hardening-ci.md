# v1 Hardening: CI Validation

Status: READY

## Purpose

This hardening step adds visible GitHub Actions validation for AgentLogistics.
It reduces the AL-25 public-usability and release-mechanics gap by making the
existing repository validator run on pushes, pull requests, and manual
dispatches.

## Workflow

```text
.github/workflows/validate.yml
```

The workflow:

- runs on `push` to `main`;
- runs on pull requests targeting `main`;
- supports manual `workflow_dispatch`;
- uses read-only `contents: read` permissions;
- runs on `windows-latest` because the repository validation entry point is a
  PowerShell wrapper;
- pins Python through `actions/setup-python`;
- runs `.\scripts\validate-all.ps1`.

## Sources Checked

- GitHub Actions Python guide:
  `https://docs.github.com/en/actions/tutorials/build-and-test-code/python`
- `actions/checkout` documentation:
  `https://github.com/actions/checkout`
- `actions/setup-python` documentation:
  `https://github.com/actions/setup-python`

## Remaining v1 Release Conditions

CI visibility is no longer a repository-file gap after this workflow is
published and a run passes. AL-25 still requires:

- live model response scoring;
- external source freshness and reachability checks;
- expanded numerical fixtures for calculation-heavy skills;
- release notes and release tagging after gates pass;
- repository-setting review outside the version-controlled file tree.
