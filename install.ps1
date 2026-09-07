# Script d'installation globale des skills pour Windows (Antigravity & Gemini)
$ErrorActionPreference = "Stop"

$targetDir = "$env:USERPROFILE\.gemini\config\skills"
if (!(Test-Path -Path $targetDir)) {
    New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
}

$sourceDir = Join-Path $PSScriptRoot "skills"
Write-Host "📦 Installation des compétences dans $targetDir..." -ForegroundColor Cyan

Get-ChildItem -Path $sourceDir -Directory | ForEach-Object {
    $dest = Join-Path $targetDir $_.Name
    Copy-Item -Path $_.FullName -Destination $dest -Recurse -Force
    Write-Host "  ✓ Skill installé : $($_.Name)" -ForegroundColor Green
}

Write-Host "`n✨ Tous les skills sont installés et immédiatement disponibles globalement !" -ForegroundColor Yellow
