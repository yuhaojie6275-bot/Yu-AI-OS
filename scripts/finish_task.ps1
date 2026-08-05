[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$Result,

    [Parameter(Mandatory = $true)]
    [string]$Next,

    [string]$Risk = "None identified"
)

$ErrorActionPreference = "Stop"
$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$updateScript = Join-Path $scriptRoot "update_handoff.py"

if ($env:YU_AI_OS_PYTHON -and (Test-Path -LiteralPath $env:YU_AI_OS_PYTHON)) {
    & $env:YU_AI_OS_PYTHON $updateScript --result $Result --next $Next --risk $Risk
}
elseif (Get-Command python -ErrorAction SilentlyContinue) {
    & python $updateScript --result $Result --next $Next --risk $Risk
}
elseif (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3 $updateScript --result $Result --next $Next --risk $Risk
}
else {
    $codexPython = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
    if (-not (Test-Path -LiteralPath $codexPython)) {
        throw "Python 3 was not found. Install Python or set YU_AI_OS_PYTHON to python.exe."
    }
    & $codexPython $updateScript --result $Result --next $Next --risk $Risk
}

if ($LASTEXITCODE -ne 0) {
    throw "update_handoff.py failed with exit code $LASTEXITCODE."
}
