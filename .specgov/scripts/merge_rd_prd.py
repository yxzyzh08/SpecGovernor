#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
合并 RD.md 和 PRD.md 为新的 PRD.md（v3.0）

[ID: CODE-SCRIPT-MERGE-001] [Implements: DESIGN-REFACTOR-MERGE-001]
"""
import os
import re
import sys
import shutil
from datetime import datetime
from pathlib import Path

# 设置 Windows 控制台编码为 UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')


def backup_old_files():
    """备份旧的 RD.md 和 PRD.md 文件。"""
    print("📦 备份旧文件...")

    os.makedirs('docs/archives', exist_ok=True)

    if os.path.exists('RD.md'):
        shutil.copy2('RD.md', 'docs/archives/RD-v2-archived.md')
        print("  ✓ 已备份 RD.md → docs/archives/RD-v2-archived.md")

    if os.path.exists('PRD.md'):
        shutil.copy2('PRD.md', 'docs/archives/PRD-v2-archived.md')
        print("  ✓ 已备份 PRD.md → docs/archives/PRD-v2-archived.md")

    print()


def read_file(filepath):
    """读取文件内容。"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"⚠️  警告：未找到文件 {filepath}")
        return ""


def replace_rd_tags(content):
    """将 RD- 标记替换为 PRD-REQ- 标记。"""
    replacements = {
        r'\[ID: RD-GOAL-': '[ID: PRD-GOAL-',
        r'\[ID: RD-USER-': '[ID: PRD-USER-',
        r'\[ID: RD-REQ-': '[ID: PRD-REQ-',
        r'\[ID: RD-NFR-': '[ID: PRD-NFR-',
        r'\[ID: RD-INIT-': '[ID: PRD-INIT-',
        r'\[ID: RD-SIZE-': '[ID: PRD-SIZE-',
        r'\[ID: RD-STRUCTURE-': '[ID: PRD-STRUCTURE-',
        r'\[ID: RD-FR-': '[ID: PRD-FR-',
        r'\[ID: RD-TRACE-': '[ID: PRD-TRACE-',
        r'\[ID: RD-AC-': '[ID: PRD-AC-',
        r'\[ID: RD-SCENARIO-': '[ID: PRD-SCENARIO-',
        r'\[ID: RD-SUMMARY-': '[ID: PRD-SUMMARY-',
        r'\[ID: RD-NEXT-': '[ID: PRD-NEXT-',
        r'\[Implements: RD-': '[Implements: PRD-REQ-',
        r'\[Decomposes: RD-': '[Decomposes: PRD-REQ-',
    }

    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content)

    return content


def update_prd_references(content):
    """更新 PRD 中对 RD 的引用。"""
    # 更新 Implements 关系
    content = re.sub(
        r'\[Implements: RD-([A-Z0-9-]+)\]',
        r'[Implements: PRD-REQ-\1]',
        content
    )

    # 删除 "Based on: RD.md" 的引用
    content = re.sub(
        r'> \*\*Based on\*\*: RD\.md \(v\d+\.\d+\).*?\n',
        '',
        content
    )

    return content


def extract_rd_content(rd_content):
    """从 RD.md 提取主要内容（去掉头部元数据）。"""
    # 找到第一个主要章节（## 开头）
    lines = rd_content.split('\n')
    start_idx = 0

    for i, line in enumerate(lines):
        if line.startswith('## **一、术语与缩略语'):
            start_idx = i
            break

    # 提取从术语部分开始的内容
    main_content = '\n'.join(lines[start_idx:])

    return main_content


def extract_prd_content(prd_content):
    """从 PRD.md 提取主要内容（从 "二、User Stories" 开始）。"""
    lines = prd_content.split('\n')
    start_idx = 0

    for i, line in enumerate(lines):
        if line.startswith('## **二、User Stories'):
            start_idx = i
            break

    # 提取从 User Stories 开始的内容
    main_content = '\n'.join(lines[start_idx:])

    return main_content


def create_new_prd(rd_content, prd_content):
    """创建新的 PRD.md（v3.0）。"""
    today = datetime.now().strftime('%Y-%m-%d')

    # 提取 RD 和 PRD 的主要内容
    rd_main = extract_rd_content(rd_content)
    prd_main = extract_prd_content(prd_content)

    # 替换标记
    rd_main = replace_rd_tags(rd_main)
    prd_main = update_prd_references(prd_main)

    # 构建新的 PRD.md
    new_prd = f"""# **📦 Product Requirements Document (PRD) - SpecGovernor**

> **Version**: v3.0
> **Created**: 2025-11-16
> **Updated**: {today}
> **Target User**: Super Individual (超级个体) using Claude Code
> **Product Type**: Toolkit (Prompt Templates + Workflow Documentation + Helper Scripts)

---

## **Architecture Change Notice (v3.0)**

**重大变更**：RD（需求文档）和 PRD（产品需求文档）已合并为单一 PRD 文档。

**理由**：
- 超级个体同时扮演需求分析师和产品经理角色
- 减少文档维护成本和流程步骤
- 消除 RD → PRD 转换的冗余工作

**新架构**：
```
旧流程：RD → PRD → Design Document → Test Plan → Code (5 阶段)
新流程：PRD → Design Document → Test Plan → Code (4 阶段)
```

**可追溯性变更**：
- 旧标记：`[ID: RD-REQ-001]` → 新标记：`[ID: PRD-REQ-001]`
- 旧标记：`[ID: RD-GOAL-001]` → 新标记：`[ID: PRD-GOAL-001]`

---

## **Traceability Declaration**

本文档采用**显式可追溯性标记 (Explicit Traceability Tagging)** 策略，建立：
- PRD-REQ-XXX（业务需求）→ PRD-FEAT-XXX（产品功能）→ DESIGN-XXX → TEST-XXX → CODE-XXX

---

# **Part 1: Business Requirements（业务需求）**

> 本部分包含原 RD.md 的内容，定义业务需求、目标用户、功能需求等。

{rd_main}

---

# **Part 2: Product Features（产品功能设计）**

> 本部分包含原 PRD.md 的内容，定义产品功能、用户故事、验收标准等。

{prd_main}

---

**PRD Document Complete (v3.0)**
"""

    return new_prd


def write_file(filepath, content):
    """写入文件。"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def update_design_document():
    """更新 Design-Document.md 中的标记引用。"""
    print("📝 更新 Design-Document.md...")

    if not os.path.exists('Design-Document.md'):
        print("  ⚠️  未找到 Design-Document.md，跳过")
        return

    content = read_file('Design-Document.md')

    # 备份
    shutil.copy2('Design-Document.md', 'docs/archives/Design-Document-v2-backup.md')

    # 替换标记
    content = replace_rd_tags(content)
    content = update_prd_references(content)

    # 更新头部信息
    content = re.sub(
        r'> \*\*Based on\*\*: RD\.md \(v\d+\.\d+\) \+ PRD\.md \(v\d+\.\d+\)',
        f'> **Based on**: PRD.md (v3.0)',
        content
    )

    write_file('Design-Document.md', content)
    print("  ✓ 已更新 Design-Document.md")
    print()


def update_test_plan():
    """更新 Test-Plan.md 中的标记引用。"""
    print("📝 更新 Test-Plan.md...")

    if not os.path.exists('Test-Plan.md'):
        print("  ⚠️  未找到 Test-Plan.md，跳过")
        return

    content = read_file('Test-Plan.md')

    # 备份
    shutil.copy2('Test-Plan.md', 'docs/archives/Test-Plan-v2-backup.md')

    # 替换标记
    content = replace_rd_tags(content)
    content = update_prd_references(content)

    # 更新头部信息
    content = re.sub(
        r'> \*\*Based on\*\*: .*? \+ PRD\.md.*?\n',
        f'> **Based on**: PRD.md (v3.0) + Design-Document.md\n',
        content
    )

    write_file('Test-Plan.md', content)
    print("  ✓ 已更新 Test-Plan.md")
    print()


def main():
    """主函数。"""
    print("=" * 60)
    print("SpecGovernor RD + PRD Merge Script (v2 → v3)")
    print("=" * 60)
    print()

    # Step 1: 备份
    backup_old_files()

    # Step 2: 读取文件
    print("📖 读取 RD.md 和 PRD.md...")
    rd_content = read_file('RD.md')
    prd_content = read_file('PRD.md')

    if not rd_content or not prd_content:
        print("❌ 错误：无法读取 RD.md 或 PRD.md")
        return 1

    print("  ✓ 已读取 RD.md")
    print("  ✓ 已读取 PRD.md")
    print()

    # Step 3: 合并
    print("🔄 合并 RD.md 和 PRD.md...")
    new_prd = create_new_prd(rd_content, prd_content)
    print("  ✓ 已创建新 PRD.md（v3.0）")
    print()

    # Step 4: 写入
    print("💾 保存新 PRD.md...")
    write_file('PRD.md', new_prd)
    print("  ✓ 已保存 PRD.md（v3.0）")
    print()

    # Step 5: 更新 Design-Document.md
    update_design_document()

    # Step 6: 更新 Test-Plan.md
    update_test_plan()

    # Step 7: 统计
    print("=" * 60)
    print("📊 合并统计：")
    print("=" * 60)

    rd_tags = len(re.findall(r'\[ID: RD-', rd_content))
    new_tags = len(re.findall(r'\[ID: PRD-REQ-', new_prd))

    print(f"  • 原 RD.md 标记数量：{rd_tags}")
    print(f"  • 新 PRD.md 标记数量（Part 1）：{new_tags}")
    print(f"  • 新 PRD.md 总行数：{len(new_prd.split(chr(10)))}")
    print()

    print("=" * 60)
    print("✅ 合并完成！")
    print("=" * 60)
    print()
    print("📚 下一步：")
    print("  1. 查看新的 PRD.md：type PRD.md")
    print("  2. 查看备份文件：dir docs\\archives")
    print("  3. 继续执行 Phase 3（重构 Prompt Templates）")
    print()

    return 0


if __name__ == '__main__':
    exit(main())
