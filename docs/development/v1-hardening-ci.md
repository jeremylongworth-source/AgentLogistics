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
.github/workflows/source-links.yml
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

The source-link workflow:

- runs weekly and by manual dispatch;
- uses read-only `contents: read` permissions;
- runs on `windows-latest`;
- runs `python scripts\validate-source-links.py`;
- retries `GET` when a source rejects or mishandles `HEAD` requests;
- fails on confirmed broken links such as 404 or 410 responses;
- reports transient network and TLS failures without failing the scheduled CI
  run by default;
- reports access-restricted official sites separately when they return statuses
  such as 401, 403, 405, or 429.

For local networks that intercept TLS, maintainers can run a strict transient
audit while allowing local certificate-chain failures:

```powershell
python scripts\validate-source-links.py --strict-transient --allow-tls-errors
```

Use those options only to separate local certificate-chain issues from broken
source URLs. Run `python scripts\validate-source-links.py --strict-transient`
when investigating whether reported transient source failures are repeatable.

## Sources Checked

- GitHub Actions Python guide:
  `https://docs.github.com/en/actions/tutorials/build-and-test-code/python`
- `actions/checkout` documentation:
  `https://github.com/actions/checkout`
- `actions/setup-python` documentation:
  `https://github.com/actions/setup-python`
- GitHub Actions workflow syntax:
  `https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax`

## Remote Verification

Verified on GitHub Actions on 2026-09-04:

- `Validate` push run `33860184054` passed for commit `31a0cf5`.
- `Source Link Audit` manual run `33860220295` passed for `main`.

The source-link run reported no confirmed broken links. It did report transient
timeouts for two `canada.ca` pages and expected access restrictions from some
official sites; those are visible in workflow logs for maintenance review.

## Remaining v1 Release Conditions

CI visibility is no longer a repository-file gap. Source-link audit visibility
is available through a manual and scheduled GitHub Actions workflow, and both
remote workflows have passing run evidence. AL-25 still requires:

- live model response scoring;
- review of source freshness audit results over time;
- expanded numerical fixtures for calculation-heavy skills;
- v1 release notes and v1 release tagging after gates pass;
- repository-setting review outside the version-controlled file tree.
