# SpecGovernor 快速开始指南

5 分钟快速上手 SpecGovernor - 使用待办事项管理应用作为示例！

---

## 🎯 学习目标

完成本指南后，您将：
- ✅ 了解 SpecGovernor v3.0 的 4 阶段工作流
- ✅ 使用 Claude Code 生成第一个产品需求文档（PRD）
- ✅ 使用 Claude Code 审查文档质量
- ✅ 运行 Helper Scripts 构建依赖图谱
- ✅ 理解可追溯性标记的工作原理

**预计时间**: 5-10 分钟

---

## 🛠️ 工具要求

本指南假设您使用以下工具：

| 工具 | 版本要求 | 用途 |
|------|----------|------|
| **Claude Code** | 最新版 | AI 编程助手，执行所有文档生成任务 |
| **VS Code** | 推荐 | 代码编辑器（可选） |
| **Python** | 3.8+ | 运行 Helper Scripts |
| **Git** | 2.0+ | 版本控制 |

**重要说明**：
- ✅ 所有文件操作都由 **Claude Code** 自动完成
- ✅ 您**无需手动编辑文件**
- ✅ 只需复制粘贴命令到 Claude Code 即可

---

## 📏 项目规模与命令选择

SpecGovernor 根据项目规模提供不同的命令集，以适应不同的文档组织方式。

### 小项目（< 10 万行代码）- 单层文档结构

**使用命令**：
- `/specgov-prd-gen` - 生成 PRD.md（包含业务需求和产品功能）
- `/specgov-design-gen` - 生成 Design-Document.md（所有设计在一个文件）
- `/specgov-test-gen` - 生成 Test-Plan.md（所有测试用例在一个文件）

**特点**：
- ✅ 一个命令生成完整文档
- ✅ 所有内容集中在一个文件中
- ✅ 适合 5-50 个需求项的项目
- ✅ **本快速开始指南使用小项目示例**

---

### 大项目（≥ 10 万行代码）- 双层文档结构

**两步生成流程**：

**第 1 步：生成 Overview 文档**（每个阶段调用一次）
- `/specgov-prd-overview-gen` - 生成 PRD-Overview.md（项目整体需求和产品概览）
- `/specgov-design-overview-gen` - 生成 Design-Overview.md（项目整体架构概览）
- `/specgov-test-overview-gen` - 生成 Test-Overview.md（项目整体测试策略）

**第 2 步：生成 Module 文档**（每个模块调用一次）
- `/specgov-prd-module-gen` - 生成 PRD-{Module}.md（模块具体需求和功能）
- `/specgov-design-module-gen` - 生成 Design-{Module}.md（模块具体设计）
- `/specgov-test-module-gen` - 生成 Test-{Module}.md（模块具体测试用例）

**特点**：
- ✅ 文档分层管理（Overview + 多个 Module）
- ✅ 适合 50+ 需求项、多个子系统/模块的项目
- ✅ 每个模块独立文档，便于团队协作
- ✅ 详见 `.specgov/workflows/workflow-large-project.md`

---

### 如何选择？

**在运行 `python .specgov/scripts/init_project.py` 时，您会被询问项目规模**：

```
请选择项目规模:
1. 小项目（< 10 万行代码，使用单层文档结构）
2. 大项目（≥ 10 万行代码，使用双层文档结构）
```

**初始化脚本会根据您的选择显示对应的命令列表**：

- 小项目：显示 `/specgov-prd-gen`, `/specgov-design-gen` 等单层命令
- 大项目：显示 `/specgov-prd-overview-gen` + `/specgov-prd-module-gen` 等两步命令

> **提示**：您生成的 `CLAUDE.md` 文件中也会包含您项目规模对应的命令列表，随时可查阅。

---

## 📋 前提条件

- ✅ 已完成 SpecGovernor 安装（参见 [INSTALLATION.md](INSTALLATION.md)）
- ✅ 项目目录包含 `.specgov/` 文件夹
- ✅ Claude Code 已启动并可访问
- ✅ 已运行 `python .specgov/scripts/init_project.py` 初始化项目

验证安装：
```bash
# 检查目录结构
ls .specgov/prompts/     # 应该有 20 个 .md 文件
ls .specgov/scripts/     # 应该有 5 个 .py 文件
ls .claude/commands/     # 应该有 20 个 .md 文件
```

---

## 📖 示例项目：待办事项管理应用

本指南使用一个简单的**待办事项管理应用（To-Do List App）**作为示例，带您完整体验 SpecGovernor 工作流。

**项目特点**：
- ✅ 小巧简单（适合 5-10 分钟快速上手）
- ✅ 功能清晰（创建、完成、删除任务）
- ✅ 涵盖完整 SDLC 流程（PRD → Design → Test → Code）

---

## 第 0 步：项目规划（Project Management）

### 0.1 切换到项目经理角色

在开始技术工作之前，作为 **Project Manager** 创建项目的整体规划：

**创建第一个 Epic**：

1. 打开 `.specgov/tasks/project-manager.md`
2. 在 "Active Epics" 部分添加：

```markdown
## Active Epics

### Epic 1: To-Do List App 核心功能开发
- **目标**：构建一个功能完整的待办事项管理应用
- **进度**：0%
- **状态**：进行中
- **子任务**：
  - ⬜ 需求分析（Requirements Analyst）- 预计 1 小时
  - ⬜ 产品规划（Product Manager）- 预计 1 小时  
  - ⬜ 技术设计（Architect）- 预计 2 小时
  - ⬜ 测试规划（Test Manager）- 预计 1 小时
  - ⬜ 代码实现（Developer）- 预计 3 小时
- **预估时间**：8 小时
- **预估成本**：$5-10（Claude Code 使用）
```

3. 保存文件

**为什么这样做？**
- 明确项目目标和范围
- 分解工作为可管理的任务
- 追踪整体进度
- 估算时间和成本

> **💡 提示**：如需详细的任务管理指导，请查看 [任务管理工作流](.specgov/workflows/workflow-task-mgmt.md)

---

## 第 1 步：生成产品需求文档（PRD）

### 1.1 切换到产品经理角色

现在切换到 **Product Manager** 角色开始执行第一个子任务：

1. 打开 `.specgov/tasks/product-manager.md`
2. 添加分配的任务：

```markdown
## Active Tasks

### Task 1: 生成 To-Do List App 产品需求文档
- **Epic**：Epic 1 - To-Do List App 核心功能开发
- **描述**：收集原始需求并生成 Product Requirements Document（包含业务需求和产品功能）
- **状态**：进行中
- **预估时间**：1 小时
- **输出**：docs/PRD.md
- **开始时间**：[当前时间]
```

3. 保存文件

### 1.2 在 Claude Code 中生成 PRD

**在 Claude Code 对话框中，复制粘贴以下完整内容**（一次性发送）：

```
/specgov-prd-gen

请生成待办事项管理应用（To-Do List App）的需求文档。

**项目信息**：
- 项目名称：To-Do List App
- 项目规模：小项目（< 10 万行代码）
- 目标用户：个人用户（学生、职场人士、自由职业者）
- 部署平台：Web 应用（浏览器访问）

**用户故事**：
1. As a user, I want to create a new task with title and description, so that I can track what I need to do
2. As a user, I want to mark tasks as completed, so that I can see my progress
3. As a user, I want to delete tasks, so that I can remove tasks I no longer need
4. As a user, I want to filter tasks by status (all/active/completed), so that I can focus on relevant tasks
5. As a user, I want tasks to persist after refreshing the page, so that I don't lose my data
6. As a user, I want to edit existing tasks, so that I can update task details

**业务需求**：
- 简单直观的用户界面（扁平化设计）
- 无需注册登录（本地存储，保护隐私）
- 响应式设计（支持桌面和移动端）
- 快速加载（< 1 秒首屏渲染）
- 离线可用（PWA 支持）

**技术约束**：
- 前端框架：React 18 + TypeScript
- 状态管理：React Hooks (useState, useEffect)
- 存储方案：localStorage
- 构建工具：Vite
- 样式方案：Tailwind CSS
- 部署平台：Vercel / GitHub Pages
```

### 1.2 Claude Code 自动生成 PRD

Claude Code 将：
1. ✅ 询问您的原始需求（口语化输入）
2. ✅ 记录原始需求到 `docs/raw-requirements/inputs.md`
3. ✅ 加载 `.specgov/prompts/prd-generator.md` 模板
4. ✅ 根据您的需求生成完整的 PRD.md（包含可追溯性标记）
5. ✅ 自动写入 `docs/PRD.md` 文件
6. ✅ 显示生成的文档内容

**生成的 PRD.md 示例片段**：

```markdown
# Product Requirements Document (PRD)

## Part 1: Business Requirements

### 1.1 Task Management Requirements
**[ID: PRD-REQ-SECTION-001]**

本章节定义待办事项管理的核心业务需求。

**验收标准**：
- ✅ 用户能够完整管理待办任务的生命周期
- ✅ 任务数据能够持久化保存
- ✅ 界面简洁直观，易于使用

## Part 2: Product Features

### 2.1 Create Task Feature
**[ID: PRD-FEAT-001] [Implements: PRD-REQ-SECTION-001]**

#### User Story
> **As** 用户
> **I want** 创建新的待办任务
> **So that** 我可以记录需要完成的事项

#### Acceptance Criteria
- ✅ 用户可以输入任务标题（必填，最多 100 字符）
- ✅ 用户可以输入任务描述（可选，最多 500 字符）
- ✅ 任务创建后立即显示在任务列表中
- ✅ 任务状态默认为 "active"（未完成）

### 2.2 Mark Task as Completed Feature
**[ID: PRD-FEAT-002] [Implements: PRD-REQ-SECTION-001]**

#### User Story
> **As** 用户
> **I want** 标记任务为完成状态
> **So that** 我可以追踪已完成的工作

#### Acceptance Criteria
- ✅ 用户可以点击任务旁的复选框标记为完成
- ✅ 已完成任务显示删除线样式
- ✅ 完成状态持久化到 localStorage

...
```

### 1.3 验证生成结果

检查生成的文档：
```bash
# 查看 PRD.md
cat docs/PRD.md

# 验证文件已创建
ls docs/
```

您应该看到：
- ✅ `docs/PRD.md` 文件已创建
- ✅ 包含 Part 1（业务需求）和 Part 2（产品功能）两部分
- ✅ 业务需求使用 `[ID: PRD-REQ-XXX]` 标记
- ✅ 产品功能使用 `[ID: PRD-FEAT-XXX]` 标记
- ✅ 使用 `[Implements: PRD-REQ-XXX]` 表示功能实现需求

---

## 第 2 步：审查产品需求文档

### 2.1 在 Claude Code 中审查 PRD

**复制粘贴以下内容到 Claude Code**：

```
/specgov-prd-review

请审查以下 Product Requirements Document (PRD)：

[粘贴 docs/PRD.md 的完整内容]

项目规模：小项目
```

> **提示**：您可以使用 `cat docs/PRD.md` 查看文档内容，然后复制粘贴到 Claude Code。

### 2.2 Claude Code 输出审查报告

Claude Code 将输出审查报告，例如：

```markdown
# PRD Review Report

## Summary
- **Overall Quality**: Good
- **Critical Issues**: 0
- **Important Issues**: 1
- **Suggestions**: 2

## Important Issues

### 1. [重要-可追溯性] 缺少实现关系标记
- **位置**: PRD-FEAT-006（编辑任务功能）
- **问题**: 没有 [Implements: PRD-REQ-SECTION-001] 标记
- **建议**: 添加 [Implements: PRD-REQ-SECTION-001]，因为它属于 Task Management Requirements

## Suggestions

### 1. [建议-完整性] 考虑添加性能需求
- **建议**: 在 Non-functional Requirements 章节中，添加响应时间要求（< 200ms）

...
```

### 2.3 保存审查报告

**重要**：将审查报告保存为文件，以便追溯质量保证过程：

> **说明**：Reviewer 会自动使用 Write 工具将报告保存到文档同级目录（`docs/PRD-Review-Report-2025-11-17.md`）。

**添加到版本控制**（可选）：
```bash
git add docs/PRD-Review-Report-*.md
git commit -m "Add PRD review report 2025-11-17"
```

> **💡 提示**：保存审查报告有助于：
> - 追踪质量改进历史
> - 为团队提供审查参考
> - 支持后续的影响分析

### 2.4 根据审查反馈修改 PRD（如需要）

如果有问题，再次使用 `/specgov-prd-gen` 修改：

```
/specgov-prd-gen

请修改现有 Product Requirements Document (PRD)。

现有 PRD.md 内容：
[粘贴 docs/PRD.md 内容]

审查反馈：
- PRD-FEAT-006 缺少 [Implements: PRD-REQ-SECTION-001] 标记

请根据审查反馈修改 PRD.md。
```

---

## 第 3 步：更新项目进度

### 3.1 更新产品经理任务状态

PRD 生成和审查完成后，更新任务状态：

1. 打开 `.specgov/tasks/product-manager.md`
2. 将任务移到 "Completed Tasks" 部分：

```markdown
## Completed Tasks

### Task 1: 生成 To-Do List App 需求文档
- **完成日期**：[当前日期]
- **Epic**：Epic 1 - To-Do List App 核心功能开发
- **成果**：docs/PRD.md v1.0（定义了 6 个核心需求）
- **实际时间**：[实际花费时间]
- **备注**：已通过审查，质量良好
```

### 3.2 更新项目经理 Epic 进度

切换回 **Project Manager** 角色，更新整体进度：

1. 打开 `.specgov/tasks/project-manager.md`
2. 更新 Epic 1 的进度：

```markdown
### Epic 1: To-Do List App 核心功能开发
- **进度**：0% → 25%
- **子任务**：
  - ✅ 产品规划（Product Manager）- 已完成
  - ⬜ 技术设计（Architect）- 下一步
  - ⬜ 测试规划（Test Manager）
  - ⬜ 代码实现（Developer）
- **已用时间**：[实际花费时间]
```

**为什么要更新进度？**
- 保持项目透明度
- 追踪实际 vs 预估时间
- 为下一个任务做准备
- 建立工作习惯

---

## 第 4 步：运行 Helper Scripts

### 4.1 解析可追溯性标记

```bash
# 解析 PRD.md 中的标记
python .specgov/scripts/parse_tags.py
```

**输出示例（小项目）**：
```
Parsing docs/PRD.md...
Found 12 tags:
- PRD-REQ-SECTION-001 (business requirement section)
- PRD-FEAT-001 (feature, implements: PRD-REQ-SECTION-001)
- PRD-FEAT-002 (feature, implements: PRD-REQ-SECTION-001)
- PRD-FEAT-003 (feature, implements: PRD-REQ-SECTION-001)
- PRD-FEAT-004 (feature, implements: PRD-REQ-SECTION-001)
- PRD-FEAT-005 (feature, implements: PRD-REQ-SECTION-001)
- PRD-FEAT-006 (feature, implements: PRD-REQ-SECTION-001)
- PRD-REQ-NFR-001 (non-functional requirement)
- PRD-REQ-NFR-002 (non-functional requirement)

Tags saved to .specgov/index/tags.json
```

**输出示例（大项目，生成 PRD-Overview.md 后）**：
```
Parsing docs/PRD/PRD-Overview.md...
Found 5 tags:
- PRD-REQ-PROJECT-001 (business requirement)
- PRD-MODULE-USER (module, implements: PRD-REQ-PROJECT-001)
- PRD-MODULE-ORDER (module, implements: PRD-REQ-PROJECT-001)
- PRD-MODULE-PAYMENT (module, implements: PRD-REQ-PROJECT-001)
- PRD-REQ-CROSS-AUTH-001 (cross-cutting requirement)

Tags saved to .specgov/index/tags.json

📦 Updated project modules:
  - User (USER) in docs/PRD/PRD-Overview.md:25
  - Order (ORDER) in docs/PRD/PRD-Overview.md:35
  - Payment (PAYMENT) in docs/PRD/PRD-Overview.md:45
✓ Updated 3 modules in .specgov/project-config.json
```

> **大项目提示**：`parse_tags.py` 会自动从 `PRD-Overview.md` 中提取模块定义（`[ID: PRD-MODULE-XXX]`）并更新 `.specgov/project-config.json` 中的 `modules` 字段。这样后续脚本和工具就能知道项目有哪些模块了。

### 4.2 构建依赖图谱

```bash
# 构建依赖图谱
python .specgov/scripts/build_graph.py
```

**输出示例**：
```
Building dependency graph...
Nodes: 9
Edges: 6

Dependency graph saved to .specgov/index/dependency-graph.json
```

### 4.3 查看依赖图谱

```bash
# 查看生成的图谱
cat .specgov/index/dependency-graph.json
```

**示例内容**：
```json
{
  "nodes": [
    {"id": "PRD-REQ-SECTION-001", "type": "business_requirement", "label": "Task Management Requirements", "location": "docs/PRD.md:10"},
    {"id": "PRD-FEAT-001", "type": "feature", "label": "Create Task Feature", "location": "docs/PRD.md:25"},
    {"id": "PRD-FEAT-002", "type": "feature", "label": "Mark Task as Completed Feature", "location": "docs/PRD.md:40"}
  ],
  "edges": [
    {"from": "PRD-FEAT-001", "to": "PRD-REQ-SECTION-001", "type": "implements"},
    {"from": "PRD-FEAT-002", "to": "PRD-REQ-SECTION-001", "type": "implements"}
  ]
}
```

---

## 第 5 步：继续 SDLC 流程（可选）

您已经完成了 PRD 生成！现在可以继续：

### 5.1 生成 Design Document

```
/specgov-design-gen

请基于以下 PRD 生成 Design Document。

PRD 内容：
[粘贴 docs/PRD.md 内容]

技术选型：
- 前端：React 18 + TypeScript + Vite
- 状态管理：React Hooks
- 存储：localStorage
- 样式：Tailwind CSS

请生成 Design Document，包含架构设计、数据模型、API 设计。
```

### 5.2 生成 Test Plan

```
/specgov-test-gen

请基于以下 Design Document 生成 Test Plan。

Design Document 内容：
[粘贴 docs/Design-Document.md 内容]

测试策略：
- 单元测试：Jest + React Testing Library
- E2E 测试：Playwright
- 覆盖率目标：> 80%

请生成 Test Plan，包含测试用例和验收标准。
```

---

## 🎉 恭喜！

您已完成 SpecGovernor 快速开始教程！

### 您已经学会了：

- ✅ **项目规划**：作为 Project Manager 创建 Epic 和任务分解
- ✅ **角色切换**：在不同视角间切换（Project Manager → Product Manager → Project Manager）
- ✅ 使用 Claude Code 斜杠命令（`/specgov-prd-gen`、`/specgov-prd-review`）
- ✅ 生成带可追溯性标记的产品需求文档（PRD）
- ✅ 使用 Reviewer 审查文档质量
- ✅ **任务管理**：更新任务状态和 Epic 进度
- ✅ 运行 Helper Scripts 构建依赖图谱
- ✅ 理解 SpecGovernor 的完整工作流（项目管理 + 技术实现）

### 完整的文件结构：

```
your-project/
├── .specgov/
│   ├── scripts/              # Helper Scripts
│   ├── prompts/              # Prompt 模板
│   ├── workflows/            # 工作流文档
│   ├── tasks/                # ✅ 任务跟踪文件（项目管理）
│   │   ├── project-manager.md    # ✅ 您创建的 Epic
│   │   ├── product-manager.md    # ✅ 您更新的任务状态
│   │   ├── architect.md
│   │   ├── test-manager.md
│   │   └── developer.md
│   └── index/
│       ├── tags.json         # ✅ 可追溯性标记索引
│       └── dependency-graph.json  # ✅ 依赖图谱
├── .claude/
│   └── commands/             # 小项目：10 个斜杠命令，大项目：13 个斜杠命令
├── docs/
│   ├── PRD.md                            # ✅ 您生成的产品需求文档
│   └── PRD-Review-Report-2025-11-17.md  # ✅ Reviewer 自动保存的审查报告
└── CLAUDE.md                 # 项目指南（请填写）
```

---

## 📚 下一步

### 继续完整的 SDLC 流程

按照以下顺序继续：

1. **生成 Design Document**
   - 使用: `/specgov-design-gen`
   - 审查: `/specgov-design-review`
   - 工作流: `.specgov/workflows/workflow-design.md`

2. **生成 Test Plan**
   - 使用: `/specgov-test-gen`
   - 审查: `/specgov-test-review`
   - 工作流: `.specgov/workflows/workflow-test-plan.md`

3. **生成代码**
   - 使用: `/specgov-code-gen`
   - 审查: `/specgov-code-review`

### 深入学习

- **完整工作流**: 阅读 `.specgov/workflows/workflow-overview.md`
- **任务管理**: 阅读 `.specgov/workflows/workflow-task-mgmt.md`
- **大项目**: 阅读 `.specgov/workflows/workflow-large-project.md`（如果项目 ≥ 10 万行代码）

### 使用 Helper Scripts

```bash
# 影响分析：修改 PRD 后运行
python .specgov/scripts/impact_analysis.py --changed=docs/PRD.md

# 一致性检查：验证可追溯性链
python .specgov/scripts/check_consistency.py --scope=PRD-FEAT-001
```

---

## 💡 提示和最佳实践

1. **使用 Claude 斜杠命令**：在 Claude Code 中使用 `/specgov-xx-gen` 命令，无需手动打开 prompt 文件
2. **一次性提供完整上下文**：将需求、约束、示例等信息一次性粘贴到 Claude Code，生成质量更好
3. **定期运行 Helper Scripts**：每次修改文档后运行 `parse_tags.py` 和 `build_graph.py`
4. **大项目模块管理**：生成 PRD-Overview.md 后立即运行 `parse_tags.py`，它会自动提取模块信息到 `project-config.json`
5. **使用 Git 追踪变更**：所有文档都应该提交到 Git，便于团队协作和版本追溯
6. **双重质量保证**：始终使用 Generator + Reviewer 模式（生成 + 审查）
7. **填写 CLAUDE.md**：根据您的项目实际情况填写 `CLAUDE.md` 中的技术栈、架构约束等信息

**可用的 Claude 斜杠命令（小项目）**：
- `/specgov-prd-gen` - 生成 PRD
- `/specgov-prd-review` - 审查 PRD
- `/specgov-design-gen` - 生成 Design Document
- `/specgov-design-review` - 审查 Design Document
- `/specgov-test-gen` - 生成 Test Plan
- `/specgov-test-review` - 审查 Test Plan
- `/specgov-code-gen` - 生成代码
- `/specgov-code-review` - 审查代码
- `/specgov-consistency` - 检查一致性
- `/specgov-impact` - 分析变更影响

> **注意**：大项目使用不同的命令集（Overview + Module 两步流程），详见 [📏 项目规模与命令选择](#-项目规模与命令选择) 章节。

> **完整命令列表**：查看 `.claude/commands/` 目录或您的 `CLAUDE.md` 文件。

---

## ❓ 常见问题

### Q1: 斜杠命令不工作怎么办？

**A**: 检查以下几点：
- `.claude/commands/` 目录是否存在
- 是否运行了 `python .specgov/scripts/init_project.py`
- Claude Code 是否已重启（有时需要重启加载新命令）

### Q2: 生成的文档没有可追溯性标记怎么办？

**A**: 检查：
- 是否使用了正确的 prompt 模板（`/specgov-prd-gen`）
- 是否在提示中明确要求包含标记
- 使用 `/specgov-prd-review` 审查，它会检测缺失的标记

### Q3: Helper Scripts 运行失败怎么办？

**A**: 检查：
- Python 版本是否 ≥ 3.8
- 是否在项目根目录运行（包含 `.specgov/` 目录）
- 文档中的标记格式是否正确（如 `[ID: PRD-REQ-001]`）
- 查看错误消息，根据提示修复

### Q3a: 大项目中 project-config.json 的 modules 字段为什么是空的？

**A**: `modules` 字段会在您生成 PRD-Overview.md 后自动更新。

**解决步骤**：
1. 使用 `/specgov-prd-overview-gen` 生成 `docs/PRD/PRD-Overview.md`
2. 确保 Overview 中包含模块定义（如 `[ID: PRD-MODULE-USER]`, `[ID: PRD-MODULE-ORDER]`）
3. 运行 `python .specgov/scripts/parse_tags.py`
4. 脚本会自动提取模块信息并更新 `project-config.json`

**验证**：
```bash
cat .specgov/project-config.json
```
应该看到 `modules` 字段包含了您定义的所有模块。

### Q4: 我可以跳过某个阶段吗？

**A**: 不推荐。完整的 SDLC 流程确保需求到代码的完整可追溯性。如果跳过某个阶段（如 Design Document），后续阶段的文档将缺少上游链接，可追溯性链会断裂。

### Q5: 如何处理大项目？

**A**: 对于 ≥ 10 万行代码的大项目，SpecGovernor 使用双层文档结构（Overview + Module）。

在运行 `python .specgov/scripts/init_project.py` 时选择"大项目"，初始化脚本会为您显示正确的命令列表。

**详细说明**：
- 参见本文档的 [📏 项目规模与命令选择](#-项目规模与命令选择) 章节
- 工作流文档：`.specgov/workflows/workflow-large-project.md`
- 您的 `CLAUDE.md` 文件中也包含大项目专用命令列表

---

## 📞 获取帮助

- **工作流文档**: 查看 `.specgov/workflows/` 中的相关文档
- **GitHub Issues**: https://github.com/yxzyzh08/SpecGovernor/issues
- **完整文档**: [README.md](README.md), [INSTALLATION.md](INSTALLATION.md)

---

**🚀 开始您的 SpecGovernor 之旅！**
