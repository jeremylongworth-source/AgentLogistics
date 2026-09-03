$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot

python "$PSScriptRoot\validate-docs.py" --repo-root "$RepoRoot"

Write-Host "All AgentLogistics validation checks passed."
