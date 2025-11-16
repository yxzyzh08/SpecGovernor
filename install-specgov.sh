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
    echo "  ✓ Python found: $PYTHON_VERSION"
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_VERSION=$(python --version 2>&1)
    echo "  ✓ Python found: $PYTHON_VERSION"
    PYTHON_CMD="python"
else
    echo "  ✗ Python not found. Please install Python 3.8+ first."
    exit 1
fi

# Check Git
if command -v git &> /dev/null; then
    GIT_VERSION=$(git --version 2>&1)
    echo "  ✓ Git found: $GIT_VERSION"
else
    echo "  ✗ Git not found. Please install Git first."
    exit 1
fi

# Check curl
if ! command -v curl &> /dev/null; then
    echo "  ✗ curl not found. Please install curl first."
    exit 1
fi

echo
echo "[2/6] Creating directory structure..."

# Create directories
directories=(
    "scripts"
    "templates/prompts"
    "templates/workflows"
    ".specgov/prompts"
    ".specgov/workflows"
    ".specgov/tasks"
    ".specgov/index"
    "docs"
)

for dir in "${directories[@]}"; do
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
        echo "  ✓ Created $dir"
    else
        echo "  • $dir already exists"
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
    output="scripts/$script"

    echo "  Downloading $script..."
    if curl -sSL "$url" -o "$output"; then
        echo "  ✓ Downloaded $script"
    else
        echo "  ✗ Failed to download $script"
    fi
done

echo
echo "[4/6] Downloading prompt templates..."

# Download prompt templates
prompts=(
    "rd-generator.md"
    "rd-reviewer.md"
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
    "rd-overview-generator.md"
    "rd-module-generator.md"
    "prd-overview-generator.md"
    "prd-module-generator.md"
    "design-overview-generator.md"
    "design-module-generator.md"
    "test-plan-overview-generator.md"
    "test-plan-module-generator.md"
)

prompt_count=0
for prompt in "${prompts[@]}"; do
    url="$RAW_URL/templates/prompts/$prompt"
    output="templates/prompts/$prompt"

    if curl -sSL "$url" -o "$output" 2>/dev/null; then
        ((prompt_count++))
    else
        echo "  ✗ Failed to download $prompt"
    fi
done
echo "  ✓ Downloaded $prompt_count/${#prompts[@]} prompt templates"

echo
echo "[5/6] Downloading workflow documentation..."

# Download workflow documentation
workflows=(
    "workflow-overview.md"
    "workflow-rd.md"
    "workflow-prd.md"
    "workflow-design.md"
    "workflow-test-plan.md"
    "workflow-task-mgmt.md"
    "workflow-large-project.md"
)

workflow_count=0
for workflow in "${workflows[@]}"; do
    url="$RAW_URL/templates/workflows/$workflow"
    output="templates/workflows/$workflow"

    if curl -sSL "$url" -o "$output" 2>/dev/null; then
        ((workflow_count++))
    else
        echo "  ✗ Failed to download $workflow"
    fi
done
echo "  ✓ Downloaded $workflow_count/${#workflows[@]} workflow docs"

echo
echo "[6/6] Downloading documentation..."

# Download documentation files
docs=(
    "QUICK-START.md"
    "CLAUDE.md"
)

doc_count=0
for doc in "${docs[@]}"; do
    url="$RAW_URL/$doc"
    output="$doc"

    if [ ! -f "$output" ]; then
        if curl -sSL "$url" -o "$output" 2>/dev/null; then
            ((doc_count++))
            echo "  ✓ Downloaded $doc"
        else
            echo "  ✗ Failed to download $doc"
        fi
    else
        echo "  • $doc already exists (skipped)"
    fi
done

echo
echo "========================================"
echo "  Installation Complete!"
echo "========================================"
echo

echo "Next steps:"
echo "  1. Run: $PYTHON_CMD scripts/init_project.py"
echo "  2. Read: cat QUICK-START.md"
echo "  3. Start: code .specgov/tasks/project-manager.md"
echo

echo "For help, visit: $REPO_URL"
echo

# Ask if user wants to run init_project.py
read -p "Do you want to run '$PYTHON_CMD scripts/init_project.py' now? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo
    echo "Running init_project.py..."
    echo
    $PYTHON_CMD scripts/init_project.py
fi

echo
echo "SpecGovernor installation completed successfully!"
echo
