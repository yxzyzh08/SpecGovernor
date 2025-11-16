#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
初始化 SpecGovernor 项目结构。

[ID: CODE-SCRIPT-001] [Implements: DESIGN-SCRIPT-INIT-001]
"""
import os
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

# 设置 Windows 控制台编码为 UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')


def prompt_project_size():
    """提示用户选择项目规模。"""
    print("请选择项目规模：")
    print("1. 小项目（< 10 万行代码，单层文档结构）")
    print("2. 大项目（≥ 10 万行代码，双层文档结构）")

    while True:
        choice = input("您的选择 (1/2): ").strip()
        if choice in ['1', '2']:
            return 'small' if choice == '1' else 'large'
        print("无效选择，请输入 1 或 2")


def create_directory_structure(project_size):
    """根据项目规模创建目录结构。"""
    # 创建 .specgov/ 目录
    os.makedirs('.specgov', exist_ok=True)
    os.makedirs('.specgov/prompts', exist_ok=True)
    os.makedirs('.specgov/workflows', exist_ok=True)
    os.makedirs('.specgov/tasks', exist_ok=True)
    os.makedirs('.specgov/index', exist_ok=True)

    # 获取脚本所在目录（SpecGovernor 根目录）
    script_dir = Path(__file__).parent.parent
    templates_dir = script_dir / 'templates'

    # 从 templates/ 复制 prompts 和 workflows
    if (templates_dir / 'prompts').exists():
        shutil.copytree(
            templates_dir / 'prompts',
            '.specgov/prompts',
            dirs_exist_ok=True
        )
    else:
        print(f"⚠️  警告：未找到 {templates_dir / 'prompts'} 目录")

    if (templates_dir / 'workflows').exists():
        shutil.copytree(
            templates_dir / 'workflows',
            '.specgov/workflows',
            dirs_exist_ok=True
        )
    else:
        print(f"⚠️  警告：未找到 {templates_dir / 'workflows'} 目录")

    # 创建任务文件
    task_files = [
        'project-manager.md',
        'rd-analyst.md',
        'product-manager.md',
        'architect.md',
        'test-manager.md',
        'developer.md'
    ]
    for task_file in task_files:
        create_task_file(f'.specgov/tasks/{task_file}')

    # 创建 docs/ 结构
    if project_size == 'small':
        os.makedirs('docs', exist_ok=True)
        create_placeholder('docs/RD.md', 'Requirements Document')
        create_placeholder('docs/PRD.md', 'Product Requirements Document')
        create_placeholder('docs/Design-Document.md', 'Design Document')
        create_placeholder('docs/Test-Plan.md', 'Test Plan')
    else:  # large
        os.makedirs('docs/RD', exist_ok=True)
        os.makedirs('docs/PRD', exist_ok=True)
        os.makedirs('docs/Design-Document', exist_ok=True)
        os.makedirs('docs/Test-Plan', exist_ok=True)
        create_placeholder('docs/RD/RD-Overview.md', 'Requirements Overview')
        create_placeholder('docs/PRD/PRD-Overview.md', 'Product Overview')
        create_placeholder('docs/Design-Document/Design-Overview.md', 'Design Overview')
        create_placeholder('docs/Test-Plan/Test-Overview.md', 'Test Overview')

    # 创建项目配置
    config = {
        "project_name": os.path.basename(os.getcwd()),
        "project_size": project_size,
        "document_structure": "single-tier" if project_size == 'small' else "two-tier",
        "created_at": datetime.now().isoformat(),
        "modules": []
    }
    with open('.specgov/project-config.json', 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)


def create_task_file(filepath):
    """创建带有标题的空任务文件。"""
    role_name = os.path.basename(filepath).replace('.md', '').replace('-', ' ').title()
    content = f"""# {role_name} Tasks

## Active Tasks
（暂无分配的任务）

## Completed Tasks
（暂无完成的任务）
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def create_placeholder(filepath, doc_type):
    """创建占位符文档。"""
    content = f"""# {doc_type}

> **Version**: 1.0
> **Created**: {datetime.now().strftime('%Y-%m-%d')}

（此文档将使用 SpecGovernor prompt templates 生成）
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def create_claude_commands():
    """创建 Claude Code 斜杠命令。"""
    os.makedirs('.claude/commands', exist_ok=True)

    # 定义所有 prompt 模板到命令的映射
    prompt_commands = {
        # 小项目模板 (Small Project Templates)
        'rd-generator.md': ('specgov-rd-gen', 'Generate Requirements Document (RD)'),
        'rd-reviewer.md': ('specgov-rd-review', 'Review Requirements Document (RD)'),
        'prd-generator.md': ('specgov-prd-gen', 'Generate Product Requirements Document (PRD)'),
        'prd-reviewer.md': ('specgov-prd-review', 'Review Product Requirements Document (PRD)'),
        'design-generator.md': ('specgov-design-gen', 'Generate Design Document'),
        'design-reviewer.md': ('specgov-design-review', 'Review Design Document'),
        'test-plan-generator.md': ('specgov-test-gen', 'Generate Test Plan'),
        'test-plan-reviewer.md': ('specgov-test-review', 'Review Test Plan'),
        'code-generator.md': ('specgov-code-gen', 'Generate code implementation'),
        'code-reviewer.md': ('specgov-code-review', 'Review code implementation'),
        'consistency-checker.md': ('specgov-consistency', 'Check traceability consistency'),
        'impact-analyzer.md': ('specgov-impact', 'Analyze change impact'),

        # 大项目模板 (Large Project Templates)
        'rd-overview-generator.md': ('specgov-rd-overview', 'Generate RD Overview (large project)'),
        'rd-module-generator.md': ('specgov-rd-module', 'Generate RD Module (large project)'),
        'prd-overview-generator.md': ('specgov-prd-overview', 'Generate PRD Overview (large project)'),
        'prd-module-generator.md': ('specgov-prd-module', 'Generate PRD Module (large project)'),
        'design-overview-generator.md': ('specgov-design-overview', 'Generate Design Overview (large project)'),
        'design-module-generator.md': ('specgov-design-module', 'Generate Design Module (large project)'),
        'test-plan-overview-generator.md': ('specgov-test-overview', 'Generate Test Plan Overview (large project)'),
        'test-plan-module-generator.md': ('specgov-test-module', 'Generate Test Plan Module (large project)'),
    }

    command_count = 0
    for prompt_file, (command_name, description) in prompt_commands.items():
        command_content = f"""---
description: {description}
---

Please load and use the SpecGovernor prompt template: `.specgov/prompts/{prompt_file}`

Follow the instructions in the template to generate or review the document.
"""
        command_path = f'.claude/commands/{command_name}.md'
        with open(command_path, 'w', encoding='utf-8') as f:
            f.write(command_content)
        command_count += 1

    return command_count


def main():
    """主函数。"""
    print("=" * 60)
    print("SpecGovernor Project Initialization")
    print("=" * 60)
    print()

    # 检查是否已经初始化
    if os.path.exists('.specgov/project-config.json'):
        print("⚠️  项目已经初始化过了。")
        choice = input("是否重新初始化？(y/N): ").strip().lower()
        if choice != 'y':
            print("取消初始化。")
            return
        print()

    project_size = prompt_project_size()
    print(f"\n正在创建 {project_size} 项目结构...")
    print()

    try:
        create_directory_structure(project_size)

        # 创建 Claude Code 命令
        print()
        print("正在创建 Claude Code 斜杠命令...")
        command_count = create_claude_commands()
        print(f"✅ 已创建 {command_count} 个 Claude Code 命令！")

        print()
        print("✅ SpecGovernor 项目结构创建完成！")
        print()
        print("=" * 60)
        print("📁 已创建的目录和文件：")
        print("=" * 60)
        print("  .specgov/")
        print("    ├── scripts/      (5 个 helper scripts)")
        print("    ├── prompts/      (20 个 prompt 模板)")
        print("    ├── workflows/    (7 个工作流文档)")
        print("    ├── tasks/        (6 个任务文件)")
        print("    ├── index/        (索引目录)")
        print("    └── project-config.json")
        print("  .claude/")
        print("    └── commands/     (20 个斜杠命令)")
        print("  docs/             (项目文档目录)")
        print()
        print("=" * 60)
        print("📚 下一步指南：")
        print("=" * 60)
        print()
        print("🚀 快速开始（5分钟）：")
        if os.path.exists("QUICK-START.md"):
            print("  阅读快速开始指南：type QUICK-START.md")
        else:
            print("  1. 阅读工作流概览：type .specgov/workflows/workflow-overview.md")
            print("  2. 创建第一个 Epic：编辑 .specgov/tasks/project-manager.md")
            print("  3. 生成需求文档：在 Claude Code 中加载 .specgov/prompts/rd-generator.md")
        print()
        print("📖 详细文档：")
        print("  - 工作流概览：.specgov/workflows/workflow-overview.md")
        print("  - 任务管理：  .specgov/workflows/workflow-task-mgmt.md")
        if project_size == 'large':
            print("  - 大项目流程：.specgov/workflows/workflow-large-project.md")
        print()
        print("🛠️  Helper Scripts：")
        print("  - 解析标记：  python .specgov/scripts/parse_tags.py")
        print("  - 构建图谱：  python .specgov/scripts/build_graph.py")
        print("  - 一致性检查：python .specgov/scripts/check_consistency.py")
        print("  - 影响分析：  python .specgov/scripts/impact_analysis.py --changed=docs/RD.md")
        print()
        print("💬 Claude Code 斜杠命令：")
        print("  - 生成 RD：   /specgov-rd-gen")
        print("  - 审查 RD：   /specgov-rd-review")
        print("  - 生成 PRD：  /specgov-prd-gen")
        print("  - 查看全部：  .claude/commands/ 目录")
        print()
        print(f"📋 项目配置：")
        print(f"  - 配置文件：.specgov/project-config.json")
        print(f"  - 项目规模：{project_size} project")
        print(f"  - 文档结构：{'单层（RD.md, PRD.md, ...）' if project_size == 'small' else '双层（Overview + Module 文档）'}")
        print()
        print("=" * 60)
        print("🎉 SpecGovernor 初始化完成！开始您的开发之旅吧！")
        print("=" * 60)

    except Exception as e:
        print(f"❌ 错误：{e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0


if __name__ == '__main__':
    exit(main())
