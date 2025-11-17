#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
完成 v3.0 重构的最终步骤（Phase 5-6）

Phase 5: 更新 Workflow 文档
Phase 6: 更新配置文件和创建迁移指南
"""
import os
import re
import sys
import shutil
from pathlib import Path
from datetime import datetime

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')


def update_workflow_files():
    """Phase 5: 更新 Workflow 文档。"""
    print("=" * 60)
    print("Phase 5: 更新 Workflow 文档")
    print("=" * 60)
    print()

    workflows_dir = Path('.specgov/workflows')

    # 备份
    backup_dir = workflows_dir / 'v2-backup'
    os.makedirs(backup_dir, exist_ok=True)
    for wf_file in workflows_dir.glob('*.md'):
        shutil.copy2(wf_file, backup_dir / wf_file.name)
    print("✅ 已备份 workflow 文件")

    # 删除 workflow-rd.md
    rd_workflow = workflows_dir / 'workflow-rd.md'
    if rd_workflow.exists():
        rd_workflow.unlink()
        print("✅ 已删除 workflow-rd.md")

    # 更新其他 workflow 文件
    workflow_files = [
        'workflow-overview.md',
        'workflow-prd.md',
        'workflow-design.md',
        'workflow-test-plan.md',
        'workflow-task-mgmt.md',
        'workflow-large-project.md',
    ]

    for wf_name in workflow_files:
        wf_path = workflows_dir / wf_name
        if not wf_path.exists():
            continue

        with open(wf_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 更新引用
        content = re.sub(r'RD\.md', 'PRD.md', content)
        content = re.sub(r'RD-REQ-', 'PRD-REQ-', content)
        content = re.sub(r'RD-GOAL-', 'PRD-GOAL-', content)
        content = re.sub(r'RD → PRD → ', 'PRD → ', content)
        content = re.sub(r'Requirements Analyst', 'Product Manager', content)
        content = re.sub(r'/specgov-rd-gen', '/specgov-prd-gen', content)
        content = re.sub(r'/specgov-rd-review', '/specgov-prd-review', content)

        with open(wf_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ 已更新 {wf_name}")

    print()


def update_installation_guide():
    """更新 INSTALLATION.md。"""
    print("📝 更新 INSTALLATION.md...")

    inst_path = 'INSTALLATION.md'
    if not os.path.exists(inst_path):
        print("  ⚠️  未找到 INSTALLATION.md，跳过")
        return

    with open(inst_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 更新版本号和流程描述
    content = re.sub(r'RD → PRD → Design', 'PRD → Design', content)
    content = re.sub(r'RD\.md', 'PRD.md', content)

    with open(inst_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("  ✅ 已更新 INSTALLATION.md")


def update_quickstart_guide():
    """更新 QUICK-START.md。"""
    print("📝 更新 QUICK-START.md...")

    qs_path = 'QUICK-START.md'
    if not os.path.exists(qs_path):
        print("  ⚠️  未找到 QUICK-START.md，跳过")
        return

    with open(qs_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 更新第一个命令
    content = re.sub(r'/specgov-rd-gen', '/specgov-prd-gen', content)
    content = re.sub(r'RD\.md', 'PRD.md', content)
    content = re.sub(r'RD-REQ-', 'PRD-REQ-', content)

    with open(qs_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("  ✅ 已更新 QUICK-START.md")


def create_migration_guide():
    """创建 v2 → v3 迁移指南。"""
    print("📝 创建 MIGRATION-GUIDE.md...")

    migration_content = f"""# SpecGovernor Migration Guide: v2.0 → v3.0

**Generated**: {datetime.now().strftime('%Y-%m-%d')}

## 🎯 重大变更概述

### 架构变更

**RD（需求文档）和 PRD（产品需求文档）已合并为单一 PRD 文档。**

```
旧架构（v2.0）：
RD.md → PRD.md → Design-Document.md → Test-Plan.md → Code

新架构（v3.0）：
PRD.md → Design-Document.md → Test-Plan.md → Code
```

### 文档变更

| v2.0 | v3.0 | 说明 |
|------|------|------|
| RD.md | PRD.md (Part 1) | 业务需求移到 PRD Part 1 |
| PRD.md | PRD.md (Part 2) | 产品功能在 PRD Part 2 |
| Design-Document.md | Design-Document.md | 更新引用（RD-XXX → PRD-REQ-XXX） |
| Test-Plan.md | Test-Plan.md | 更新引用 |

### 标记变更

| v2.0 标记 | v3.0 标记 | 类型 |
|-----------|-----------|------|
| `[ID: RD-GOAL-001]` | `[ID: PRD-GOAL-001]` | 项目目标 |
| `[ID: RD-USER-001]` | `[ID: PRD-USER-001]` | 目标用户 |
| `[ID: RD-REQ-001]` | `[ID: PRD-REQ-001]` | 业务需求 |
| `[ID: RD-NFR-001]` | `[ID: PRD-NFR-001]` | 非功能需求 |
| `[ID: PRD-FEAT-001]` | `[ID: PRD-FEAT-001]` | 产品功能（不变） |

---

## 📋 迁移步骤

### Step 1: 备份现有项目

```bash
# 创建备份目录
mkdir -p project-backup

# 备份关键文档
cp docs/RD.md project-backup/RD-v2-backup.md
cp docs/PRD.md project-backup/PRD-v2-backup.md
cp docs/Design-Document.md project-backup/Design-v2-backup.md
cp docs/Test-Plan.md project-backup/Test-v2-backup.md

# 备份 .specgov 目录
cp -r .specgov project-backup/.specgov-backup
```

### Step 2: 合并 RD 和 PRD

**选项 A：使用自动化脚本（推荐）**

```bash
# 下载最新的 SpecGovernor
git clone https://github.com/yourname/SpecGovernor.git specgov-v3

# 复制合并脚本
cp specgov-v3/.specgov/scripts/merge_rd_prd.py .

# 运行合并脚本
python merge_rd_prd.py
```

**选项 B：手动合并**

1. 创建新的 PRD.md：

```markdown
# Product Requirements Document (PRD) - v3.0

## Architecture Change Notice (v3.0)
[说明 v3.0 变更]

## Part 1: Business Requirements（业务需求）
[复制 RD.md 的内容到这里]

## Part 2: Product Features（产品功能设计）
[复制 PRD.md 的内容到这里]
```

2. 手动替换标记（见 Step 3）

### Step 3: 更新标记引用

**全局搜索替换**（在所有文档中）：

```
查找: [ID: RD-GOAL-
替换: [ID: PRD-GOAL-

查找: [ID: RD-USER-
替换: [ID: PRD-USER-

查找: [ID: RD-REQ-
替换: [ID: PRD-REQ-

查找: [ID: RD-NFR-
替换: [ID: PRD-NFR-

查找: [Implements: RD-
替换: [Implements: PRD-REQ-

查找: [Decomposes: RD-
替换: [Decomposes: PRD-REQ-
```

**涉及的文件**：
- PRD.md
- Design-Document.md
- Test-Plan.md
- 所有代码文件中的注释

### Step 4: 更新 SpecGovernor 工具包

```bash
# 重新初始化项目（这会更新 prompt templates 和命令）
python specgov-v3/.specgov/scripts/init_project.py

# 选择项目规模（小项目或大项目）
# 这会更新：
#   - .specgov/prompts/ (16 个新 templates)
#   - .specgov/workflows/ (6 个新 workflows)
#   - .claude/commands/ (新命令，无 rd-* 命令)
```

### Step 5: 重新解析标记

```bash
# 解析新的 PRD-REQ-XXX 标记
python .specgov/scripts/parse_tags.py

# 构建新的依赖图
python .specgov/scripts/build_graph.py

# 验证输出
cat .specgov/index/tags.json
```

### Step 6: 更新任务文件

删除 Requirements Analyst 任务文件，合并到 Product Manager：

```bash
# 删除 rd-analyst.md
rm .specgov/tasks/rd-analyst.md

# 更新 product-manager.md
# 将原 rd-analyst.md 的任务合并到 product-manager.md
```

---

## 🧪 验证迁移

### 检查清单

- [ ] PRD.md 包含 Part 1（业务需求）和 Part 2（产品功能）
- [ ] Design-Document.md 中无 `RD-` 标记
- [ ] Test-Plan.md 中无 `RD-` 标记
- [ ] 代码注释中无 `RD-` 标记
- [ ] `.specgov/prompts/` 中无 rd-*.md 文件（应该只有 16 个 templates）
- [ ] `.claude/commands/` 中无 specgov-rd-*.md 命令
- [ ] `parse_tags.py` 正常识别 PRD-REQ-XXX
- [ ] `build_graph.py` 正常构建依赖图

### 测试命令

```bash
# 测试 PRD 生成（在 Claude Code 中）
/specgov-prd-gen

# 测试标记解析
python .specgov/scripts/parse_tags.py

# 测试依赖图构建
python .specgov/scripts/build_graph.py

# 测试影响分析
python .specgov/scripts/impact_analysis.py --changed=docs/PRD.md
```

---

## ⚠️ 常见问题

### Q1: 迁移后 Design-Document.md 中仍有 RD- 标记怎么办？

**A**: 运行全局替换：

```bash
# Linux/Mac
sed -i 's/RD-REQ-/PRD-REQ-/g' docs/Design-Document.md
sed -i 's/RD-GOAL-/PRD-GOAL-/g' docs/Design-Document.md

# Windows (PowerShell)
(Get-Content docs/Design-Document.md) -replace 'RD-REQ-', 'PRD-REQ-' | Set-Content docs/Design-Document.md
```

### Q2: 旧的 RD.md 还能保留吗？

**A**: 可以，但建议移到 `docs/archives/` 目录：

```bash
mkdir -p docs/archives
mv docs/RD.md docs/archives/RD-v2-archived.md
```

### Q3: 大项目（双层文档）如何迁移？

**A**: 对每个模块重复合并步骤：

```
docs/RD/RD-User-Module.md + docs/PRD/PRD-User-Module.md
→ docs/PRD/PRD-User-Module.md

docs/RD/RD-Order-Module.md + docs/PRD/PRD-Order-Module.md
→ docs/PRD/PRD-Order-Module.md
```

### Q4: 迁移需要多长时间？

**A**: 根据项目规模：
- 小项目（< 10 万行）：~30 分钟
- 大项目（≥ 10 万行）：~2 小时

---

## 📚 参考资源

- [v3.0 架构说明](REFACTORING-SUMMARY.md)
- [新的 PRD 模板](.specgov/prompts/prd-generator.md)
- [v3.0 README](README.md)

---

## 🆘 需要帮助？

如果迁移过程中遇到问题：
1. 查看 `REFACTORING-SUMMARY.md` 了解详细变更
2. 检查备份文件：`project-backup/` 或 `docs/archives/`
3. 提交 Issue：https://github.com/yourname/SpecGovernor/issues

---

**迁移指南结束**
"""

    with open('MIGRATION-GUIDE.md', 'w', encoding='utf-8') as f:
        f.write(migration_content)

    print("  ✅ 已创建 MIGRATION-GUIDE.md")


def update_configuration():
    """Phase 6: 更新配置文件。"""
    print()
    print("=" * 60)
    print("Phase 6: 更新配置文件")
    print("=" * 60)
    print()

    update_installation_guide()
    update_quickstart_guide()
    create_migration_guide()

    print()


def main():
    """主函数。"""
    print("=" * 60)
    print("SpecGovernor v3.0 重构最终步骤（Phase 5-6）")
    print("=" * 60)
    print()

    # Phase 5: 更新 Workflow 文档
    update_workflow_files()

    # Phase 6: 更新配置文件
    update_configuration()

    print("=" * 60)
    print("✅ Phase 5-6 完成！")
    print("=" * 60)
    print()
    print("📚 下一步：Phase 7 - 集成测试")
    print("  运行: python .specgov/scripts/parse_tags.py")
    print("  运行: python .specgov/scripts/build_graph.py")
    print()

    return 0


if __name__ == '__main__':
    exit(main())
