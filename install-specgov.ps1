# SpecGovernor Installation Script for Windows (PowerShell)
# This script installs SpecGovernor to an existing project

param(
    [string]$Version = "main"
)

$ErrorActionPreference = "Stop"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  SpecGovernor Installation Script" -ForegroundColor Cyan
Write-Host "  Version: $Version" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Check if running in project root
if (-not (Test-Path ".git")) {
    Write-Warning "This directory doesn't appear to be a Git repository."
    $continue = Read-Host "Continue anyway? (y/n)"
    if ($continue -ne "y") {
        Write-Host "Installation cancelled." -ForegroundColor Yellow
        exit 1
    }
}

# Configuration
$REPO_URL = "https://github.com/yxzyzh08/SpecGovernor"
$RAW_URL = "https://raw.githubusercontent.com/yxzyzh08/SpecGovernor/$Version"
$TEMP_DIR = ".specgov-temp"

Write-Host "[1/6] Checking prerequisites..." -ForegroundColor Green

# Check Python
try {
    $pythonVersion = python --version 2>&1
    Write-Host "  [OK] Python found: $pythonVersion" -ForegroundColor Gray
} catch {
    Write-Host "  [FAIL] Python not found. Please install Python 3.8+ first." -ForegroundColor Red
    exit 1
}

# Check Git
try {
    $gitVersion = git --version 2>&1
    Write-Host "  [OK] Git found: $gitVersion" -ForegroundColor Gray
} catch {
    Write-Host "  [FAIL] Git not found. Please install Git first." -ForegroundColor Red
    exit 1
}

Write-Host "`n[2/6] Creating directory structure..." -ForegroundColor Green

# Create directories
$directories = @(
    "scripts",
    "templates/prompts",
    "templates/workflows",
    ".specgov/prompts",
    ".specgov/workflows",
    ".specgov/tasks",
    ".specgov/index",
    "docs"
)

foreach ($dir in $directories) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
        Write-Host "  [OK] Created $dir" -ForegroundColor Gray
    } else {
        Write-Host "  [SKIP] $dir already exists" -ForegroundColor Gray
    }
}

Write-Host "`n[3/6] Downloading helper scripts..." -ForegroundColor Green

# Download scripts
$scripts = @(
    "init_project.py",
    "parse_tags.py",
    "build_graph.py",
    "check_consistency.py",
    "impact_analysis.py"
)

foreach ($script in $scripts) {
    $url = "$RAW_URL/scripts/$script"
    $output = "scripts/$script"

    try {
        Write-Host "  Downloading $script..." -ForegroundColor Gray
        Invoke-WebRequest -Uri $url -OutFile $output -ErrorAction Stop
        Write-Host "  [OK] Downloaded $script" -ForegroundColor Gray
    } catch {
        Write-Host "  [FAIL] Failed to download $script" -ForegroundColor Red
        Write-Host "    Error: $_" -ForegroundColor Red
    }
}

Write-Host "`n[4/6] Downloading prompt templates..." -ForegroundColor Green

# Download prompt templates
$prompts = @(
    "rd-generator.md",
    "rd-reviewer.md",
    "prd-generator.md",
    "prd-reviewer.md",
    "design-generator.md",
    "design-reviewer.md",
    "test-plan-generator.md",
    "test-plan-reviewer.md",
    "code-generator.md",
    "code-reviewer.md",
    "consistency-checker.md",
    "impact-analyzer.md",
    "rd-overview-generator.md",
    "rd-module-generator.md",
    "prd-overview-generator.md",
    "prd-module-generator.md",
    "design-overview-generator.md",
    "design-module-generator.md",
    "test-plan-overview-generator.md",
    "test-plan-module-generator.md"
)

$promptCount = 0
$promptTotal = $prompts.Count
foreach ($prompt in $prompts) {
    $url = "$RAW_URL/templates/prompts/$prompt"
    $output = "templates/prompts/$prompt"

    try {
        Write-Host "  [$($promptCount+1)/$promptTotal] Downloading $prompt..." -ForegroundColor Gray -NoNewline
        Invoke-WebRequest -Uri $url -OutFile $output -ErrorAction Stop -TimeoutSec 30
        $promptCount++
        Write-Host " [OK]" -ForegroundColor Green
    } catch {
        Write-Host " [FAIL]" -ForegroundColor Red
        Write-Host "    Error: $_" -ForegroundColor Red
    }
}
Write-Host "  [INFO] Downloaded $promptCount/$promptTotal prompt templates" -ForegroundColor Cyan

Write-Host "`n[5/6] Downloading workflow documentation..." -ForegroundColor Green

# Download workflow documentation
$workflows = @(
    "workflow-overview.md",
    "workflow-rd.md",
    "workflow-prd.md",
    "workflow-design.md",
    "workflow-test-plan.md",
    "workflow-task-mgmt.md",
    "workflow-large-project.md"
)

$workflowCount = 0
$workflowTotal = $workflows.Count
foreach ($workflow in $workflows) {
    $url = "$RAW_URL/templates/workflows/$workflow"
    $output = "templates/workflows/$workflow"

    try {
        Write-Host "  [$($workflowCount+1)/$workflowTotal] Downloading $workflow..." -ForegroundColor Gray -NoNewline
        Invoke-WebRequest -Uri $url -OutFile $output -ErrorAction Stop -TimeoutSec 30
        $workflowCount++
        Write-Host " [OK]" -ForegroundColor Green
    } catch {
        Write-Host " [FAIL]" -ForegroundColor Red
        Write-Host "    Error: $_" -ForegroundColor Red
    }
}
Write-Host "  [INFO] Downloaded $workflowCount/$workflowTotal workflow docs" -ForegroundColor Cyan

Write-Host "`n[6/6] Downloading documentation..." -ForegroundColor Green

# Download documentation files
$docs = @(
    "QUICK-START.md",
    "CLAUDE.md"
)

$docCount = 0
foreach ($doc in $docs) {
    $url = "$RAW_URL/$doc"
    $output = $doc

    try {
        if (-not (Test-Path $output)) {
            Invoke-WebRequest -Uri $url -OutFile $output -ErrorAction Stop -TimeoutSec 30
            $docCount++
            Write-Host "  [OK] Downloaded $doc" -ForegroundColor Gray
        } else {
            Write-Host "  [SKIP] $doc already exists" -ForegroundColor Gray
        }
    } catch {
        Write-Host "  [FAIL] Failed to download $doc" -ForegroundColor Red
        Write-Host "    Error: $_" -ForegroundColor Red
    }
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Installation Complete!" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Cyan

Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "  1. Run: python scripts/init_project.py" -ForegroundColor White
Write-Host "  2. Read: type QUICK-START.md" -ForegroundColor White
Write-Host "  3. Start: code .specgov/tasks/project-manager.md`n" -ForegroundColor White

Write-Host "For help, visit: $REPO_URL`n" -ForegroundColor Gray

# Ask if user wants to run init_project.py
$runInit = Read-Host "Do you want to run 'python scripts/init_project.py' now? (y/n)"
if ($runInit -eq "y") {
    Write-Host "`nRunning init_project.py...`n" -ForegroundColor Green
    python scripts/init_project.py
}

Write-Host "`nSpecGovernor installation completed successfully!`n" -ForegroundColor Green
