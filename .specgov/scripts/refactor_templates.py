#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
重构 Prompt Templates（v2 → v3）

删除 RD templates，重写 PRD templates，更新其他 templates

[ID: CODE-SCRIPT-REFACTOR-001] [Implements: DESIGN-REFACTOR-TEMPLATES-001]
"""
import os
import re
import sys
import shutil
from pathlib import Path

# 设置 Windows 控制台编码为 UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')


def backup_templates():
    """备份现有 templates。"""
    print("📦 备份现有 Prompt Templates...")

    backup_dir = Path('.specgov/prompts/v2-backup')
    os.makedirs(backup_dir, exist_ok=True)

    templates_dir = Path('.specgov/prompts')
    backup_count = 0

    for template_file in templates_dir.glob('*.md'):
        shutil.copy2(template_file, backup_dir / template_file.name)
        backup_count += 1

    print(f"  ✓ 已备份 {backup_count} 个 template 文件到 {backup_dir}")
    print()


def delete_rd_templates():
    """删除 RD-related templates。"""
    print("🗑️  删除 RD-related templates...")

    rd_templates = [
        '.specgov/prompts/rd-generator.md',
        '.specgov/prompts/rd-reviewer.md',
        '.specgov/prompts/rd-overview-generator.md',
        '.specgov/prompts/rd-module-generator.md',
    ]

    deleted = 0
    for template_path in rd_templates:
        if os.path.exists(template_path):
            os.remove(template_path)
            print(f"  ✓ 已删除 {template_path}")
            deleted += 1

    print(f"  总计：删除 {deleted} 个 RD template 文件")
    print()


def update_template_references(content):
    """更新 template 中的标记引用。"""
    replacements = {
        # 标记替换
        r'\[ID: RD-': '[ID: PRD-REQ-',
        r'\[Implements: RD-': '[Implements: PRD-REQ-',
        r'\[Decomposes: RD-': '[Decomposes: PRD-REQ-',

        # 文本引用替换
        r'RD\.md': 'PRD.md',
        r'RD-REQ-': 'PRD-REQ-',
        r'RD-GOAL-': 'PRD-GOAL-',
        r'RD-USER-': 'PRD-USER-',
        r'RD-NFR-': 'PRD-NFR-',

        # 流程描述替换
        r'RD → PRD → Design': 'PRD → Design',
        r'RD/PRD/Design': 'PRD/Design',
        r'Requirements Document \(RD\)': 'Product Requirements Document (PRD) - Part 1 (Business Requirements)',
    }

    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content)

    return content


def update_design_templates():
    """更新 Design templates。"""
    print("📝 更新 Design templates...")

    design_templates = [
        '.specgov/prompts/design-generator.md',
        '.specgov/prompts/design-reviewer.md',
        '.specgov/prompts/design-overview-generator.md',
        '.specgov/prompts/design-module-generator.md',
    ]

    updated = 0
    for template_path in design_templates:
        if not os.path.exists(template_path):
            continue

        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 更新引用
        content = update_template_references(content)

        # 更新输入说明（删除 RD.md，只保留 PRD.md）
        content = re.sub(
            r'- RD\.md.*?\n',
            '',
            content
        )
        content = re.sub(
            r'\*\*输入文档\*\*:.*?RD\.md.*?\n',
            '**输入文档**: PRD.md\n',
            content
        )

        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  ✓ 已更新 {template_path}")
        updated += 1

    print(f"  总计：更新 {updated} 个 Design template 文件")
    print()


def update_test_templates():
    """更新 Test Plan templates。"""
    print("📝 更新 Test Plan templates...")

    test_templates = [
        '.specgov/prompts/test-plan-generator.md',
        '.specgov/prompts/test-plan-reviewer.md',
        '.specgov/prompts/test-plan-overview-generator.md',
        '.specgov/prompts/test-plan-module-generator.md',
    ]

    updated = 0
    for template_path in test_templates:
        if not os.path.exists(template_path):
            continue

        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 更新引用
        content = update_template_references(content)

        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  ✓ 已更新 {template_path}")
        updated += 1

    print(f"  总计：更新 {updated} 个 Test Plan template 文件")
    print()


def update_code_templates():
    """更新 Code templates。"""
    print("📝 更新 Code templates...")

    code_templates = [
        '.specgov/prompts/code-generator.md',
        '.specgov/prompts/code-reviewer.md',
    ]

    updated = 0
    for template_path in code_templates:
        if not os.path.exists(template_path):
            continue

        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 更新引用
        content = update_template_references(content)

        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  ✓ 已更新 {template_path}")
        updated += 1

    print(f"  总计：更新 {updated} 个 Code template 文件")
    print()


def update_utility_templates():
    """更新工具类 templates（consistency-checker, impact-analyzer）。"""
    print("📝 更新工具类 templates...")

    utility_templates = [
        '.specgov/prompts/consistency-checker.md',
        '.specgov/prompts/impact-analyzer.md',
    ]

    updated = 0
    for template_path in utility_templates:
        if not os.path.exists(template_path):
            continue

        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 更新引用
        content = update_template_references(content)

        # 更新文档列表（删除 RD）
        content = re.sub(
            r'- RD\.md.*?\n',
            '',
            content
        )
        content = re.sub(
            r'RD → ',
            '',
            content
        )

        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  ✓ 已更新 {template_path}")
        updated += 1

    print(f"  总计：更新 {updated} 个工具类 template 文件")
    print()


def update_prd_templates():
    """更新 PRD templates（合并 RD 和 PRD 逻辑）。"""
    print("📝 更新 PRD templates...")

    # prd-generator.md 需要重写（合并 RD 和 PRD 生成逻辑）
    prd_generator_path = '.specgov/prompts/prd-generator.md'

    if os.path.exists(prd_generator_path):
        with open(prd_generator_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 添加 v3.0 说明
        intro_text = """
## Version Notice

**v3.0 重大变更**：PRD 现在包含两部分：
- **Part 1: Business Requirements（业务需求）**：原 RD.md 内容
- **Part 2: Product Features（产品功能设计）**：原 PRD.md 内容

本 generator 负责生成完整的 PRD，包括业务需求和产品功能两部分。

---
"""

        # 在 ## Role 之前插入说明
        content = re.sub(
            r'(## Role)',
            intro_text + r'\1',
            content,
            count=1
        )

        # 更新 Task 部分
        content = re.sub(
            r'(## Task\n\n).*?(?=\n## )',
            r'\1根据用户故事、业务需求或现有 PRD.md 生成或修改 Product Requirements Document (PRD)。\n\nPRD 包含：\n- **Part 1: Business Requirements**（业务需求，原 RD 内容）\n- **Part 2: Product Features**（产品功能设计，原 PRD 内容）\n\n',
            content,
            flags=re.DOTALL
        )

        with open(prd_generator_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  ✓ 已更新 {prd_generator_path}")

    # prd-reviewer.md 更新
    prd_reviewer_path = '.specgov/prompts/prd-reviewer.md'

    if os.path.exists(prd_reviewer_path):
        with open(prd_reviewer_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 添加 v3.0 说明
        intro_text = """
## Version Notice

**v3.0 重大变更**：PRD 现在包含两部分：
- **Part 1: Business Requirements（业务需求）**
- **Part 2: Product Features（产品功能设计）**

审查时需要检查两部分的完整性和一致性。

---
"""

        content = re.sub(
            r'(## Role)',
            intro_text + r'\1',
            content,
            count=1
        )

        # 更新引用
        content = update_template_references(content)

        with open(prd_reviewer_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  ✓ 已更新 {prd_reviewer_path}")

    # Overview 和 Module templates
    prd_overview_path = '.specgov/prompts/prd-overview-generator.md'
    prd_module_path = '.specgov/prompts/prd-module-generator.md'

    for template_path in [prd_overview_path, prd_module_path]:
        if not os.path.exists(template_path):
            continue

        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 添加 v3.0 说明并更新引用
        intro_text = """
## Version Notice

**v3.0 重大变更**：PRD 包含业务需求和产品功能两部分。

---
"""

        content = re.sub(
            r'(## Role)',
            intro_text + r'\1',
            content,
            count=1
        )

        content = update_template_references(content)

        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  ✓ 已更新 {template_path}")

    print(f"  总计：更新 4 个 PRD template 文件")
    print()


def main():
    """主函数。"""
    print("=" * 60)
    print("SpecGovernor Prompt Templates Refactoring (v2 → v3)")
    print("=" * 60)
    print()

    # Step 1: 备份
    backup_templates()

    # Step 2: 删除 RD templates
    delete_rd_templates()

    # Step 3: 更新 PRD templates
    update_prd_templates()

    # Step 4: 更新 Design templates
    update_design_templates()

    # Step 5: 更新 Test Plan templates
    update_test_templates()

    # Step 6: 更新 Code templates
    update_code_templates()

    # Step 7: 更新工具类 templates
    update_utility_templates()

    # 统计
    print("=" * 60)
    print("📊 重构统计：")
    print("=" * 60)

    templates_dir = Path('.specgov/prompts')
    remaining_templates = list(templates_dir.glob('*.md'))

    print(f"  • 删除 RD templates：4 个")
    print(f"  • 更新 PRD templates：4 个")
    print(f"  • 更新 Design templates：4 个")
    print(f"  • 更新 Test templates：4 个")
    print(f"  • 更新 Code templates：2 个")
    print(f"  • 更新工具类 templates：2 个")
    print(f"  • 剩余 templates 总数：{len(remaining_templates)} 个")
    print()

    print("=" * 60)
    print("✅ Prompt Templates 重构完成！")
    print("=" * 60)
    print()
    print("📚 下一步：")
    print("  1. 检查重构后的 templates：dir .specgov\\prompts")
    print("  2. 继续执行 Phase 4（更新 Helper Scripts）")
    print()

    return 0


if __name__ == '__main__':
    exit(main())
