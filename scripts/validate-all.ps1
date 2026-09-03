$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot

python "$PSScriptRoot\validate-docs.py" --repo-root "$RepoRoot"
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

python "$PSScriptRoot\validate-taxonomy.py" --repo-root "$RepoRoot"
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

python "$PSScriptRoot\validate-skills.py" --repo-root "$RepoRoot"
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

python "$PSScriptRoot\validate-specializations.py" --repo-root "$RepoRoot"
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

python "$PSScriptRoot\validate-tests.py" --repo-root "$RepoRoot"
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

python "$PSScriptRoot\validate-shared.py" --repo-root "$RepoRoot"
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

python "$PSScriptRoot\validate-skillsets.py" --repo-root "$RepoRoot"
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

Write-Host "All AgentLogistics validation checks passed."
