# SpecGovernor Local Installation Script for Windows (PowerShell)
# This script installs SpecGovernor from a local source directory

param(
    [string]$SourceDir = "D:\github_projects\SpecGovernor"
)

$ErrorActionPreference = "Stop"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  SpecGovernor Local Installation" -ForegroundColor Cyan
Write-Host "  Source: $SourceDir" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Check if source directory exists
if (-not (Test-Path $SourceDir)) {
    Write-Host "[ERROR] Source directory not found: $SourceDir" -ForegroundColor Red
    Write-Host "Please specify the correct path using -SourceDir parameter" -ForegroundColor Yellow
    Write-Host "Example: .\install-specgov-local.ps1 -SourceDir 'D:\path\to\SpecGovernor'" -ForegroundColor Yellow
    exit 1
}

# Check if running in project root
if (-not (Test-Path ".git")) {
    Write-Host "[WARNING] This directory doesn't appear to be a Git repository." -ForegroundColor Yellow
    $continue = Read-Host "Continue anyway? (y/n)"
    if ($continue -ne "y") {
        Write-Host "Installation cancelled." -ForegroundColor Yellow
        exit 1
    }
}

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

Write-Host "`n[3/6] Copying helper scripts..." -ForegroundColor Green

# Copy scripts
$scripts = @(
    "init_project.py",
    "parse_tags.py",
    "build_graph.py",
    "check_consistency.py",
    "impact_analysis.py"
)

$scriptCount = 0
foreach ($script in $scripts) {
    $source = Join-Path $SourceDir "scripts\$script"
    $dest = "scripts\$script"

    if (Test-Path $source) {
        Copy-Item $source $dest -Force
        Write-Host "  [OK] Copied $script" -ForegroundColor Gray
        $scriptCount++
    } else {
        Write-Host "  [FAIL] Source not found: $script" -ForegroundColor Red
    }
}
Write-Host "  [INFO] Copied $scriptCount/$($scripts.Count) scripts" -ForegroundColor Cyan

Write-Host "`n[4/6] Copying prompt templates..." -ForegroundColor Green

# Copy prompt templates
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
foreach ($prompt in $prompts) {
    $source = Join-Path $SourceDir "templates\prompts\$prompt"
    $dest = "templates\prompts\$prompt"

    if (Test-Path $source) {
        Copy-Item $source $dest -Force
        $promptCount++
    } else {
        Write-Host "  [WARN] Template not found: $prompt" -ForegroundColor Yellow
    }
}
Write-Host "  [INFO] Copied $promptCount/$($prompts.Count) prompt templates" -ForegroundColor Cyan

Write-Host "`n[5/6] Copying workflow documentation..." -ForegroundColor Green

# Copy workflow documentation
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
foreach ($workflow in $workflows) {
    $source = Join-Path $SourceDir "templates\workflows\$workflow"
    $dest = "templates\workflows\$workflow"

    if (Test-Path $source) {
        Copy-Item $source $dest -Force
        $workflowCount++
    } else {
        Write-Host "  [WARN] Workflow not found: $workflow" -ForegroundColor Yellow
    }
}
Write-Host "  [INFO] Copied $workflowCount/$($workflows.Count) workflow docs" -ForegroundColor Cyan

Write-Host "`n[6/6] Copying documentation..." -ForegroundColor Green

# Copy documentation files
$docs = @(
    "QUICK-START.md",
    "CLAUDE.md"
)

$docCount = 0
foreach ($doc in $docs) {
    $source = Join-Path $SourceDir $doc
    $dest = $doc

    if (Test-Path $source) {
        if (-not (Test-Path $dest)) {
            Copy-Item $source $dest -Force
            $docCount++
            Write-Host "  [OK] Copied $doc" -ForegroundColor Gray
        } else {
            Write-Host "  [SKIP] $doc already exists" -ForegroundColor Gray
        }
    } else {
        Write-Host "  [WARN] Doc not found: $doc" -ForegroundColor Yellow
    }
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Installation Complete!" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Cyan

Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "  1. Run: python scripts\init_project.py" -ForegroundColor White
Write-Host "  2. Read: type QUICK-START.md" -ForegroundColor White
Write-Host "  3. Start: code .specgov\tasks\project-manager.md`n" -ForegroundColor White

# Ask if user wants to run init_project.py
$runInit = Read-Host "Do you want to run 'python scripts\init_project.py' now? (y/n)"
if ($runInit -eq "y") {
    Write-Host "`nRunning init_project.py...`n" -ForegroundColor Green
    python scripts\init_project.py
}

Write-Host "`nSpecGovernor installation completed successfully!`n" -ForegroundColor Green
