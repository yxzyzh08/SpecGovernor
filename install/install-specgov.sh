#!/bin/bash

# SpecGovernor Installation Script for Linux/Mac (Bash)
# This script installs SpecGovernor to an existing project

set -e

VERSION="${1:-main}"

echo "========================================"
echo "  SpecGovernor Installation Script"
echo "  Version: $VERSION"
echo "========================================"
echo

# Check if running in project root
if [ ! -d ".git" ]; then
    echo "⚠️  Warning: This directory doesn't appear to be a Git repository."
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Installation cancelled."
        exit 1
    fi
fi

# Configuration
REPO_URL="https://github.com/yxzyzh08/SpecGovernor"
RAW_URL="https://raw.githubusercontent.com/yxzyzh08/SpecGovernor/$VERSION"

echo "[1/6] Checking prerequisites..."

# Check Python
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1)
    echo "  [OK] Python found: $PYTHON_VERSION"
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_VERSION=$(python --version 2>&1)
    echo "  [OK] Python found: $PYTHON_VERSION"
    PYTHON_CMD="python"
else
    echo "  [FAIL] Python not found. Please install Python 3.8+ first."
    exit 1
fi

# Check Git
if command -v git &> /dev/null; then
    GIT_VERSION=$(git --version 2>&1)
    echo "  [OK] Git found: $GIT_VERSION"
else
    echo "  [FAIL] Git not found. Please install Git first."
    exit 1
fi

# Check curl
if ! command -v curl &> /dev/null; then
    echo "  [FAIL] curl not found. Please install curl first."
    exit 1
fi

echo
echo "[2/6] Creating directory structure..."

# Create directories
directories=(
    ".specgov/scripts"
    ".specgov/prompts"
    ".specgov/workflows"
    ".specgov/tasks"
    ".specgov/index"
    "docs"
    "docs/raw-requirements"
)

for dir in "${directories[@]}"; do
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
        echo "  [OK] Created $dir"
    else
        echo "  [SKIP] $dir already exists"
    fi
done

echo
echo "[3/6] Downloading helper scripts..."

# Download scripts
scripts=(
    "init_project.py"
    "parse_tags.py"
    "build_graph.py"
    "check_consistency.py"
    "impact_analysis.py"
)

for script in "${scripts[@]}"; do
    url="$RAW_URL/scripts/$script"
    output=".specgov/scripts/$script"

    echo "  Downloading $script..."
    if curl -sSL "$url" -o "$output" --max-time 30; then
        echo "  [OK] Downloaded $script"
    else
        echo "  [FAIL] Failed to download $script"
    fi
done

echo
echo "[4/6] Downloading prompt templates..."

# Download prompt templates (v3.0: 14 templates total)
prompts=(
    "prd-generator.md"
    "prd-reviewer.md"
    "design-generator.md"
    "design-reviewer.md"
    "test-plan-generator.md"
    "test-plan-reviewer.md"
    "code-generator.md"
    "code-reviewer.md"
    "consistency-checker.md"
    "impact-analyzer.md"
    "prd-overview-generator.md"
    "prd-module-generator.md"
    "design-overview-generator.md"
    "design-module-generator.md"
    "test-plan-overview-generator.md"
    "test-plan-module-generator.md"
)

prompt_count=0
prompt_total=${#prompts[@]}
for prompt in "${prompts[@]}"; do
    url="$RAW_URL/templates/prompts/$prompt"
    output=".specgov/prompts/$prompt"

    echo -n "  [$((prompt_count+1))/$prompt_total] Downloading $prompt... "
    if curl -sSL "$url" -o "$output" --max-time 30 2>/dev/null; then
        ((prompt_count++))
        echo "[OK]"
    else
        echo "[FAIL]"
    fi
done
echo "  [INFO] Downloaded $prompt_count/$prompt_total prompt templates"

echo
echo "[5/6] Downloading workflow documentation..."

# Download workflow documentation (v3.0: 6 workflows total)
workflows=(
    "workflow-overview.md"
    "workflow-prd.md"
    "workflow-design.md"
    "workflow-test-plan.md"
    "workflow-task-mgmt.md"
    "workflow-large-project.md"
)

workflow_count=0
workflow_total=${#workflows[@]}
for workflow in "${workflows[@]}"; do
    url="$RAW_URL/templates/workflows/$workflow"
    output=".specgov/workflows/$workflow"

    echo -n "  [$((workflow_count+1))/$workflow_total] Downloading $workflow... "
    if curl -sSL "$url" -o "$output" --max-time 30 2>/dev/null; then
        ((workflow_count++))
        echo "[OK]"
    else
        echo "[FAIL]"
    fi
done
echo "  [INFO] Downloaded $workflow_count/$workflow_total workflow docs"

echo
echo "[6/6] Downloading documentation..."

# Download documentation files
docs=(
    "QUICK-START.md"
)

doc_count=0
for doc in "${docs[@]}"; do
    url="$RAW_URL/$doc"
    output="$doc"

    if [ ! -f "$output" ]; then
        if curl -sSL "$url" -o "$output" --max-time 30 2>/dev/null; then
            ((doc_count++))
            echo "  [OK] Downloaded $doc"
        else
            echo "  [FAIL] Failed to download $doc"
        fi
    else
        echo "  [SKIP] $doc already exists"
    fi
done

echo
echo "========================================"
echo "  Installation Complete!"
echo "========================================"
echo

echo "Next steps:"
echo "  1. Run: $PYTHON_CMD .specgov/scripts/init_project.py"
echo "  2. Read: cat QUICK-START.md"
echo "  3. Start: code .specgov/tasks/project-manager.md"
echo

echo "For help, visit: $REPO_URL"
echo

# Ask if user wants to run init_project.py
read -p "Do you want to run '$PYTHON_CMD .specgov/scripts/init_project.py' now? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo
    echo "Running init_project.py..."
    echo
    $PYTHON_CMD .specgov/scripts/init_project.py
fi

echo
echo "SpecGovernor installation completed successfully!"
echo
