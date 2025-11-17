#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
初始化 SpecGovernor 项目结构。

[ID: CODE-SCRIPT-001] [Implements: DESIGN-SCRIPT-INIT-001]
"""
import os
import json
import sys
from datetime import datetime

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


def prompt_project_info():
    """收集项目的行业和领域信息。"""
    print("\n" + "=" * 60)
    print("项目背景信息收集")
    print("=" * 60)
    print("这些信息将帮助产品经理生成符合行业特点的需求文档。")
    print()

    # 行业/领域
    print("1️⃣  项目所属行业/领域（如：电商、金融、医疗、教育、SaaS）")
    industry = input("   > ").strip() or "通用软件"

    # 项目类型
    print("\n2️⃣  项目类型（如：Web应用、移动应用、API服务、CLI工具）")
    project_type = input("   > ").strip() or "Web应用"

    # 目标用户
    print("\n3️⃣  目标用户群体（如：企业用户、个人用户、开发者）")
    target_users = input("   > ").strip() or "通用用户"

    # 核心业务场景
    print("\n4️⃣  核心业务场景（1-2句话描述项目的主要功能）")
    core_business = input("   > ").strip() or "待定义"

    return {
        'industry': industry,
        'project_type': project_type,
        'target_users': target_users,
        'core_business': core_business
    }


def create_directory_structure(project_size, project_info):
    """根据项目规模创建目录结构。"""
    # 创建 .specgov/ 目录
    os.makedirs('.specgov', exist_ok=True)
    os.makedirs('.specgov/prompts', exist_ok=True)
    os.makedirs('.specgov/workflows', exist_ok=True)
    os.makedirs('.specgov/tasks', exist_ok=True)
    os.makedirs('.specgov/index', exist_ok=True)
    os.makedirs('.specgov/raw-requirements', exist_ok=True)  # 原始需求目录

    # 注意：prompts 和 workflows 由安装脚本（install-specgov.ps1/sh）下载
    # 已经存在于 .specgov/prompts/ 和 .specgov/workflows/，无需复制

    # 注意：审查报告不需要专门的 reviews/ 目录
    # 由 reviewer 保存到文档同级目录，如 docs/PRD-Review-Report-YYYY-MM-DD.md

    # 创建任务文件
    task_files = [
        'project-manager.md',
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
        create_placeholder('docs/PRD.md', 'Product Requirements Document')
        create_placeholder('docs/Design-Document.md', 'Design Document')
        create_placeholder('docs/Test-Plan.md', 'Test Plan')
    else:  # large
        os.makedirs('docs/PRD', exist_ok=True)
        os.makedirs('docs/Design-Document', exist_ok=True)
        os.makedirs('docs/Test-Plan', exist_ok=True)
        create_placeholder('docs/PRD/PRD-Overview.md', 'Product Requirements Overview')
        create_placeholder('docs/Design-Document/Design-Overview.md', 'Design Overview')
        create_placeholder('docs/Test-Plan/Test-Overview.md', 'Test Plan Overview')

    # 创建原始需求收集文档（放在 docs/raw-requirements 更显眼）
    if project_size == 'small':
        os.makedirs('docs/raw-requirements', exist_ok=True)
        create_raw_requirements_template('docs/raw-requirements/inputs.md', project_size)
    else:  # large
        os.makedirs('docs/raw-requirements/modules', exist_ok=True)
        create_raw_requirements_template('docs/raw-requirements/overview.md', project_size, is_overview=True)
        # 模块文档将在后续按需创建

    # 创建项目配置
    config = {
        "project_name": os.path.basename(os.getcwd()),
        "project_size": project_size,
        "document_structure": "single-tier" if project_size == 'small' else "two-tier",
        "industry": project_info['industry'],
        "project_type": project_info['project_type'],
        "target_users": project_info['target_users'],
        "core_business": project_info['core_business'],
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

（此文档将使用 SpecGovernor v3.0 prompt templates 生成）
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def create_raw_requirements_template(filepath, project_size, is_overview=False):
    """创建原始需求收集文档模板。"""
    project_name = os.path.basename(os.getcwd())
    today = datetime.now().strftime('%Y-%m-%d')

    if project_size == 'small':
        # 小项目：单个汇总文档
        content = f"""# Raw Requirements - {project_name}

**Project Type**: Small Project

> **用途**：记录人类提供的原始需求输入（口语化、零散）
>
> 此文档仅供产品经理整理思路和后期追溯使用，不影响项目构建流程。

---

## 📝 Input Log

### 使用说明

使用 `/specgov-prd-gen` 命令生成 PRD 时，产品经理会自动询问并记录原始需求。

每个条目包含：
- 时间戳和来源（聊天、文件、邮件等）
- 原始输入（保持口语化，不修改）
- 产品经理的初步分析（分类、优先级、疑问）

---

### Entry 001 (示例)

**Source**: Chat
**Topic**: 示例需求

**Original Input**:
> （此处记录用户的原始输入，保持口语化表达）

**PM Analysis**:
- **Category**: Functional Requirement / Non-Functional Requirement / UI/UX / Performance / Security
- **Priority**: High / Medium / Low
- **Related Modules**: [相关模块]
- **Initial Thoughts**: [产品经理的初步想法]
- **Questions**: [需要澄清的问题]
- **Status**: New / Under Review / Converted to PRD / Rejected

---

## 📊 Summary Statistics

- **Total Entries**: 1 (示例)
- **By Priority**:
  - High: 0
  - Medium: 0
  - Low: 0
- **By Status**:
  - New: 1
  - Under Review: 0
  - Converted to PRD: 0
  - Rejected: 0

---

## 🔗 Related Documents

- **PRD**: docs/PRD.md (将基于这些原始需求生成)
- **Design**: docs/Design-Document.md
- **Workflow**: `.specgov/workflows/workflow-prd.md`

---

**提示**：使用 `/specgov-prd-gen` 命令基于这些原始需求生成正式的 PRD 文档。
"""
    elif is_overview:
        # 大项目：总览文档
        content = f"""# Raw Requirements Overview - {project_name}

**Project Type**: Large Project (Two-Tier)

> **用途**：记录项目级别的原始需求（跨模块、整体架构）
>
> 模块级需求记录在 `modules/` 目录下的各模块文档中。

---

## 📋 Project-Level Requirements

### 使用说明

使用 `/specgov-prd-overview` 命令生成项目级 PRD 时，产品经理会自动询问并记录项目级原始需求。

跨模块需求、整体架构需求、全局非功能需求应记录在此文档。

---

### Entry 001 (示例)

**Source**: Chat
**Topic**: 项目整体目标

**Original Input**:
> （此处记录跨模块的原始需求）

**PM Analysis**:
- **Scope**: Project-Level
- **Affects Modules**: [受影响的模块列表]
- **Priority**: High / Medium / Low
- **Initial Thoughts**: [产品经理的初步想法]
- **Questions**: [需要澄清的问题]
- **Status**: New

---

## 📦 Module-Specific Requirements

模块级需求请记录到各模块文档：

- `modules/[module-name].md` - 各模块的原始需求

使用 `/specgov-prd-module` 命令时，产品经理会自动选择或创建对应的模块文档并记录需求。

---

## 🔗 Related Documents

- **PRD Overview**: docs/PRD/PRD-Overview.md
- **Module PRDs**: docs/PRD/*.md
- **Workflow**: `.specgov/workflows/workflow-large-project.md`

---

**提示**：使用 `/specgov-prd-overview` 命令基于这些原始需求生成正式的 PRD Overview 文档。
"""
    else:
        # 大项目：模块文档
        module_name = os.path.basename(filepath).replace('.md', '').replace('-', ' ').title()
        content = f"""# Raw Requirements - {module_name}

**Module**: {module_name}

> **用途**：记录 {module_name} 模块的原始需求输入

---

## 📝 Input Log

### Entry 001 (示例)

**Source**: Chat
**Topic**: [主题]

**Original Input**:
> （此处记录用户的原始输入）

**PM Analysis**:
- **Category**: Functional Requirement / Non-Functional Requirement / UI/UX
- **Priority**: High / Medium / Low
- **Related PRD Tag**: [待生成，如 PRD-{module_name}-FEAT-001]
- **Initial Thoughts**: [产品经理的初步想法]
- **Questions**: [需要澄清的问题]
- **Status**: New

---

## 🔗 Related Documents

- **Module PRD**: docs/PRD/PRD-{module_name}-Module.md
"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def create_claude_md(project_name, project_size, project_info):
    """创建用户项目的 CLAUDE.md 文件。"""
    # 根据项目规模定制命令列表
    if project_size == 'small':
        commands_section = '''**基础命令（小项目 - 单层文档结构）**：
- `/specgov-prd-gen` - 生成 PRD.md
- `/specgov-prd-review` - 审查 PRD
- `/specgov-design-gen` - 生成 Design-Document.md
- `/specgov-design-review` - 审查 Design Document
- `/specgov-test-gen` - 生成 Test-Plan.md
- `/specgov-test-review` - 审查 Test Plan
- `/specgov-code-gen` - 生成代码
- `/specgov-code-review` - 审查代码

**工具命令**：
- `/specgov-consistency` - 检查可追溯性一致性
- `/specgov-impact` - 分析需求变更影响

> **提示**：小项目使用单层文档结构，所有产品需求都在一个 PRD.md 文件中。'''
    else:  # large
        commands_section = '''**第 1 步：生成 Overview 文档（每个阶段调用一次）**：
- `/specgov-prd-overview` - 生成 PRD-Overview.md（项目整体产品概览）
- `/specgov-design-overview` - 生成 Design-Overview.md（项目整体架构概览）
- `/specgov-test-overview` - 生成 Test-Overview.md（项目整体测试策略）

**第 2 步：生成 Module 文档（每个模块调用一次）**：
- `/specgov-prd-module` - 生成 PRD-{Module}.md（模块具体功能）
- `/specgov-design-module` - 生成 Design-{Module}.md（模块具体设计）
- `/specgov-test-module` - 生成 Test-{Module}.md（模块具体测试用例）

**审查命令（通用）**：
- `/specgov-prd-review` - 审查 PRD 文档
- `/specgov-design-review` - 审查 Design Document
- `/specgov-test-review` - 审查 Test Plan

**代码生成命令**：
- `/specgov-code-gen` - 生成代码
- `/specgov-code-review` - 审查代码

**工具命令**：
- `/specgov-consistency` - 检查可追溯性一致性
- `/specgov-impact` - 分析需求变更影响

> **提示**：大项目使用双层文档结构（Overview + Module），先生成 Overview，再为每个模块生成 Module 文档。'''

    large_project_ref = '- [大项目流程](.specgov/workflows/workflow-large-project.md)\n' if project_size == 'large' else ''

    claude_content = f'''# {project_name} - 项目指南

## 项目概述

**项目名称**: {project_name}
**项目规模**: {"小项目（< 10 万行代码）" if project_size == 'small' else "大项目（≥ 10 万行代码）"}
**文档结构**: {"单层（PRD.md, Design-Document.md, Test-Plan.md）" if project_size == 'small' else "双层（Overview + Module 文档）"}
**使用工具**: SpecGovernor v3.0 + Claude Code

---

## 项目背景

**所属行业**: {project_info['industry']}
**项目类型**: {project_info['project_type']}
**目标用户**: {project_info['target_users']}
**核心业务**: {project_info['core_business']}

> 💡 **上下文说明**：以上信息描述了项目的行业背景和核心业务，在生成各阶段文档（PRD、设计、测试）时，请参考这些信息以确保方案符合行业特点和业务需求。

---

## 🛠️ SpecGovernor 工作流

本项目使用 **SpecGovernor v3.0** 工具包进行需求到代码的全流程可追溯性管理。

### SDLC 4 阶段流程

```
PRD → Design Document → Test Plan → Code
```

1. **PRD{"" if project_size == "small" else " (Overview + Modules)"}** - Product Requirements Document（产品需求文档）
2. **Design-Document{"" if project_size == "small" else " (Overview + Modules)"}** - 设计文档
3. **Test-Plan{"" if project_size == "small" else " (Overview + Modules)"}** - 测试计划
4. **Code** - 代码实现

### Claude Code 斜杠命令

在 Claude Code 中使用以下命令快速加载 prompt 模板：

{commands_section}

### Helper Scripts

```bash
# 解析可追溯性标记
python .specgov/scripts/parse_tags.py

# 构建依赖图谱
python .specgov/scripts/build_graph.py

# 一致性检查
python .specgov/scripts/check_consistency.py

# 影响分析
python .specgov/scripts/impact_analysis.py --changed=docs/PRD.md
```

---

## 📖 文档规范参考

本项目的文档生成遵循 SpecGovernor v3.0 规范。详细的文档格式、命名、版本管理、可追溯性标记等规范，请参考：

- **工作流程**: `.specgov/workflows/workflow-overview.md`
- **Prompt 模板**: `.specgov/prompts/` 目录下的各个模板文件

> 💡 这些规范由 SpecGovernor 的 prompt 模板统一管理，确保在生成各阶段文档时自动遵循。如果您的项目需要特殊的命名或格式约定，请在下方"项目特殊要求"章节中说明。

---

## 📝 文档归属说明

为了避免信息重复和混淆，以下内容请在对应的文档中填写：

- **项目技术栈、架构约束、设计原则** → 请在 `docs/Design-Document.md` 中定义（由 Architect 角色负责）
- **团队协作规范、Git 提交规范、Code Review 流程** → 请创建 `CONTRIBUTING.md` 或在团队 Wiki 中定义
- **非功能性需求（性能、安全、兼容性等）** → 请在 `docs/PRD.md` 的 Non-Functional Requirements 章节定义（由 Product Manager 角色负责）

> 💡 **设计原则**：CLAUDE.md 只包含项目级的、稳定的、高层次的上下文信息。具体的技术决策、团队规范应该在各自负责的文档中维护。

---

## ⚙️ 项目特殊要求

> 如果您的项目需要覆盖 SpecGovernor 的默认规范，请在此处说明

### 文档命名约定
- （如有特殊要求，请在此说明。默认遵循 SpecGovernor 规范）

### 可追溯性标记自定义
- （如需自定义标记格式，请在此说明。默认使用 `[ID: XXX-YYY-###]` 格式）

### 其他特殊约定
- （请填写项目特有的其他约定）

---

## 📚 参考文档

- [SpecGovernor 快速开始](QUICK-START.md)
- [工作流概览](.specgov/workflows/workflow-overview.md)
- [任务管理](.specgov/workflows/workflow-task-mgmt.md)
{large_project_ref}
'''

    with open('CLAUDE.md', 'w', encoding='utf-8') as f:
        f.write(claude_content)


def create_claude_commands(project_size, project_info):
    """创建 Claude Code 斜杠命令。"""
    os.makedirs('.claude/commands', exist_ok=True)

    # 定义文档路径映射（小项目：单层结构）
    small_project_paths = {
        'prd': 'docs/PRD.md',
        'design': 'docs/Design-Document.md',
        'test-plan': 'docs/Test-Plan.md',
    }

    # 定义文档路径映射（大项目：双层结构）
    large_project_paths = {
        'prd-overview': 'docs/PRD/PRD-Overview.md',
        'prd-module': 'docs/PRD/PRD-{MODULE}.md',
        'design-overview': 'docs/Design-Document/Design-Overview.md',
        'design-module': 'docs/Design-Document/Design-{MODULE}.md',
        'test-overview': 'docs/Test-Plan/Test-Overview.md',
        'test-module': 'docs/Test-Plan/Test-{MODULE}.md',
    }

    # 定义小项目模板（单层文档结构）
    small_project_commands = {
        'prd-generator.md': ('specgov-prd-gen', 'Generate Product Requirements Document (PRD)', 'prd'),
        'prd-reviewer.md': ('specgov-prd-review', 'Review Product Requirements Document (PRD)', 'prd'),
        'design-generator.md': ('specgov-design-gen', 'Generate Design Document', 'design'),
        'design-reviewer.md': ('specgov-design-review', 'Review Design Document', 'design'),
        'test-plan-generator.md': ('specgov-test-gen', 'Generate Test Plan', 'test-plan'),
        'test-plan-reviewer.md': ('specgov-test-review', 'Review Test Plan', 'test-plan'),
        'code-generator.md': ('specgov-code-gen', 'Generate code implementation', None),
        'code-reviewer.md': ('specgov-code-review', 'Review code implementation', None),
        'consistency-checker.md': ('specgov-consistency', 'Check traceability consistency', None),
        'impact-analyzer.md': ('specgov-impact', 'Analyze change impact', None),
    }

    # 定义大项目模板（双层文档结构：Overview + Module）
    large_project_commands = {
        'prd-overview-generator.md': ('specgov-prd-overview', 'Generate PRD Overview (large project)', 'prd-overview'),
        'prd-module-generator.md': ('specgov-prd-module', 'Generate PRD Module (large project)', 'prd-module'),
        'prd-reviewer.md': ('specgov-prd-review', 'Review Product Requirements Document (PRD)', 'prd-overview'),
        'design-overview-generator.md': ('specgov-design-overview', 'Generate Design Overview (large project)', 'design-overview'),
        'design-module-generator.md': ('specgov-design-module', 'Generate Design Module (large project)', 'design-module'),
        'design-reviewer.md': ('specgov-design-review', 'Review Design Document', 'design-overview'),
        'test-plan-overview-generator.md': ('specgov-test-overview', 'Generate Test Plan Overview (large project)', 'test-overview'),
        'test-plan-module-generator.md': ('specgov-test-module', 'Generate Test Plan Module (large project)', 'test-module'),
        'test-plan-reviewer.md': ('specgov-test-review', 'Review Test Plan', 'test-overview'),
        'code-generator.md': ('specgov-code-gen', 'Generate code implementation', None),
        'code-reviewer.md': ('specgov-code-review', 'Review code implementation', None),
        'consistency-checker.md': ('specgov-consistency', 'Check traceability consistency', None),
        'impact-analyzer.md': ('specgov-impact', 'Analyze change impact', None),
    }

    # 根据项目规模选择命令集和路径映射
    prompt_commands = small_project_commands if project_size == 'small' else large_project_commands
    doc_paths = small_project_paths if project_size == 'small' else large_project_paths

    command_count = 0
    for prompt_file, command_info in prompt_commands.items():
        command_name, description, doc_type = command_info

        # 构建项目上下文信息
        context_section = f"""
## Project Context

- **Project Size**: {project_size} project
- **Document Structure**: {"Single-tier (one file per document type)" if project_size == 'small' else "Two-tier (Overview + Module files)"}
- **Configuration**: `.specgov/project-config.json`

## Project Background

- **Industry**: {project_info['industry']}
- **Project Type**: {project_info['project_type']}
- **Target Users**: {project_info['target_users']}
- **Core Business**: {project_info['core_business']}

> 💡 **重要提示**：生成文档时，请充分考虑项目所属行业的特点和目标用户的需求，确保设计的功能和方案符合行业规范和用户期望。
"""

        # 添加文档路径信息
        if doc_type and doc_type in doc_paths:
            doc_path = doc_paths[doc_type]
            is_reviewer = 'reviewer' in prompt_file
            is_generator = 'generator' in prompt_file

            if is_reviewer:
                # 为 reviewer 提供文档路径和评审报告保存路径
                # 审查报告保存在文档同级目录
                if project_size == 'small':
                    review_report_path = f"docs/{{DocumentType}}-Review-Report-{{YYYY-MM-DD}}.md"
                    review_report_example = f"{doc_path.replace('.md', '')}-Review-Report-2025-01-17.md"
                else:
                    # 大项目：在文档所在子目录中
                    review_report_path = f"{doc_path.rsplit('/', 1)[0]}/{{DocumentName}}-Review-Report-{{YYYY-MM-DD}}.md"
                    review_report_example = f"{doc_path.replace('.md', '')}-Review-Report-2025-01-17.md"

                context_section += f"""
## Document Paths

- **Document to Review**: `{doc_path}`
- **Review Report**: Save to document's directory with format `{{DocumentName}}-Review-Report-{{YYYY-MM-DD}}.md`
  - Example: `{review_report_example}`

**Instructions**:
1. Read the document from `{doc_path}`
2. Do NOT search for the document - use the path above directly
3. Generate review report following the template format
4. Save the report to the same directory as the document with today's date
"""
            elif is_generator:
                # 为 generator 提供文档路径和可能的评审报告位置
                if project_size == 'small':
                    review_reports_pattern = f"docs/*Review-Report-*.md"
                else:
                    review_reports_pattern = f"{doc_path.rsplit('/', 1)[0]}/*Review-Report-*.md"

                context_section += f"""
## Document Paths

- **Target Document**: `{doc_path}`
- **Review Reports**: Check document's directory for previous review reports
  - Pattern: `{review_reports_pattern}`

**Instructions**:
1. If creating new document: Write to `{doc_path}`
2. If updating existing document: Read from `{doc_path}`, then update it
3. Check document's directory for latest review report (if any)
4. Do NOT search for documents - use the paths above directly
"""
        else:
            # 对于通用命令（如 consistency-checker, impact-analyzer）
            context_section += f"""
## Document Locations

- **PRD**: `{"docs/PRD.md" if project_size == 'small' else "docs/PRD/"}`
- **Design Document**: `{"docs/Design-Document.md" if project_size == 'small' else "docs/Design-Document/"}`
- **Test Plan**: `{"docs/Test-Plan.md" if project_size == 'small' else "docs/Test-Plan/"}`
- **Source Code**: `src/`
- **Review Reports**: In document directories (e.g., `docs/*Review-Report-*.md`)
- **Traceability Index**: `.specgov/index/tags.json`
- **Dependency Graph**: `.specgov/index/dependency-graph.json`
"""

        command_content = f"""---
description: {description}
---
{context_section}
---

## Prompt Template

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
    project_info = prompt_project_info()

    print(f"\n正在创建 {project_size} 项目结构...")
    print()

    try:
        project_name = os.path.basename(os.getcwd())
        create_directory_structure(project_size, project_info)

        # 创建 Claude Code 命令
        print()
        print("正在创建 Claude Code 斜杠命令...")
        command_count = create_claude_commands(project_size, project_info)
        print(f"✅ 已创建 {command_count} 个 Claude Code 命令（{project_size} 项目）！")

        # 创建项目的 CLAUDE.md
        print()
        print("正在创建项目 CLAUDE.md 文件...")
        create_claude_md(project_name, project_size, project_info)
        print(f"✅ 已创建 CLAUDE.md 项目指南！")

        print()
        print("✅ SpecGovernor 项目结构创建完成！")
        print()
        print("=" * 60)
        print("📁 已创建的目录和文件：")
        print("=" * 60)
        print("  .specgov/")
        print("    ├── scripts/      (5 个 helper scripts)")
        print("    ├── prompts/      (14 个 prompt 模板)")
        print("    ├── workflows/    (7 个工作流文档)")
        print("    ├── tasks/        (5 个任务文件)")
        print("    ├── index/        (索引目录)")
        print("    ├── raw-requirements/ (原始需求收集)")
        print("    └── project-config.json")
        print("  .claude/")
        print(f"    └── commands/     ({command_count} 个斜杠命令)")
        print("  docs/             (项目文档目录，审查报告也保存在此)")
        print("  CLAUDE.md         (项目指南，请根据实际情况填写)")
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
            print("  3. 生成产品需求：在 Claude Code 中使用 /specgov-prd-gen")
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
        print("  - 影响分析：  python .specgov/scripts/impact_analysis.py --changed=docs/PRD.md")
        print()
        print("💬 Claude Code 斜杠命令：")
        if project_size == 'small':
            print("  [小项目 - 单层文档结构]")
            print("  - 生成 PRD：      /specgov-prd-gen")
            print("  - 审查 PRD：      /specgov-prd-review")
            print("  - 生成 Design：   /specgov-design-gen")
            print("  - 生成 Test：     /specgov-test-gen")
            print("  - 生成代码：      /specgov-code-gen")
        else:  # large
            print("  [大项目 - 双层文档结构]")
            print("  - 第 1 步（生成 Overview）：")
            print("    • /specgov-prd-overview    - 生成 PRD-Overview.md")
            print("    • /specgov-design-overview - 生成 Design-Overview.md")
            print("    • /specgov-test-overview   - 生成 Test-Overview.md")
            print("  - 第 2 步（生成 Module，每个模块调用一次）：")
            print("    • /specgov-prd-module      - 生成 PRD-Module.md")
            print("    • /specgov-design-module   - 生成 Design-Module.md")
            print("    • /specgov-test-module     - 生成 Test-Module.md")
            print("  - 审查命令（通用）：")
            print("    • /specgov-prd-review")
            print("    • /specgov-design-review")
        print("  - 查看全部：      .claude/commands/ 目录")
        print()
        print(f"📋 项目配置：")
        print(f"  - 配置文件：.specgov/project-config.json")
        print(f"  - 项目规模：{project_size} project")
        print(f"  - 文档结构：{'单层（PRD.md, Design-Document.md, Test-Plan.md）' if project_size == 'small' else '双层（Overview + Module 文档）'}")
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
