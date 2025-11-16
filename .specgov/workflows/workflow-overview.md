# SpecGovernor Workflow Overview

**[ID: WORKFLOW-OVERVIEW-001] [Implements: DESIGN-WORKFLOW-OVERVIEW-001]**

## 1. Introduction

SpecGovernor 是一个使用 Claude Code 和 prompt templates 的结构化 SDLC 工作流工具包。它通过显式的可追溯性标记和 AI 辅助的文档生成，帮助 Super Individual（一人承担多角色的开发者）高效完成从需求到代码的全流程。

**核心理念：**
- **显式可追溯性**：每个需求、功能、设计、测试、代码都有唯一 ID 并相互链接
- **双重质量保证**：生成 + 审查，确保文档质量
- **AI 辅助**：使用 Claude Code 和 prompt templates 自动化文档生成和审查
- **本地化成本**：Helper scripts 本地运行，只在生成/审查文档时使用 Claude Code

## 2. SDLC Stages

SpecGovernor 定义了 5 个 SDLC 阶段：

```
RD → PRD → Design Document → Test Plan → Code
```

### 2.1 RD (Requirements Document)
**目标**：定义需要构建什么

- **输入**：用户故事、业务需求、项目上下文
- **输出**：`docs/RD.md`（小项目）或 `docs/RD/RD-Overview.md`（大项目）
- **标记格式**：`[ID: RD-REQ-XXX]`, `[Decomposes: RD-CATEGORY-XXX]`
- **负责角色**：Requirements Analyst

### 2.2 PRD (Product Requirements Document)
**目标**：定义产品功能和用户故事

- **输入**：RD.md、产品愿景
- **输出**：`docs/PRD.md`（小项目）或 `docs/PRD/PRD-Overview.md`（大项目）
- **标记格式**：`[ID: PRD-FEAT-XXX]`, `[Implements: RD-REQ-XXX]`
- **负责角色**：Product Manager

### 2.3 Design Document
**目标**：定义技术架构和设计

- **输入**：PRD.md、技术约束
- **输出**：`docs/Design-Document.md`（小项目）或 `docs/Design-Document/Design-Overview.md`（大项目）
- **标记格式**：`[ID: DESIGN-API-XXX]`, `[Designs-for: PRD-FEAT-XXX]`
- **负责角色**：Architect
- **重要**：始终使用 "Design Document"，不是 "DD"

### 2.4 Test Plan
**目标**：定义测试策略和用例

- **输入**：Design-Document.md、PRD.md
- **输出**：`docs/Test-Plan.md`（小项目）或 `docs/Test-Plan/Test-Overview.md`（大项目）
- **标记格式**：`[ID: TEST-CASE-XXX]`, `[Tests-for: DESIGN-API-XXX]`
- **负责角色**：Test Manager
- **重要**：始终使用 "Test Plan"，不是 "TD"

### 2.5 Code
**目标**：实现系统

- **输入**：Design-Document.md、Test-Plan.md
- **输出**：代码文件（`src/`）
- **标记格式**：`[ID: CODE-XXX] [Implements: DESIGN-XXX]`（在代码注释中）
- **负责角色**：Developer

## 3. Role Perspectives

作为 Super Individual，你将在以下视角之间切换：

### 3.1 Project Manager
**职责**：
- 创建 Epics（史诗）
- 分解 Epics 为任务
- 追踪整体进度
- 协调各角色工作

**任务文件**：`.specgov/tasks/project-manager.md`

**关键活动**：
- 定义项目范围和目标
- 创建高层级的 Epic
- 分配任务到各角色
- 监控进度和风险

### 3.2 Requirements Analyst
**职责**：
- 收集和分析需求
- 生成 RD.md
- 审查 RD.md

**任务文件**：`.specgov/tasks/rd-analyst.md`

**使用的 Prompts**：
- `.specgov/prompts/rd-generator.md`
- `.specgov/prompts/rd-reviewer.md`

### 3.3 Product Manager
**职责**：
- 定义产品功能
- 编写用户故事
- 生成 PRD.md
- 审查 PRD.md

**任务文件**：`.specgov/tasks/product-manager.md`

**使用的 Prompts**：
- `.specgov/prompts/prd-generator.md`
- `.specgov/prompts/prd-reviewer.md`

### 3.4 Architect
**职责**：
- 设计系统架构
- 设计 API 和数据库
- 生成 Design Document
- 审查 Design Document

**任务文件**：`.specgov/tasks/architect.md`

**使用的 Prompts**：
- `.specgov/prompts/design-generator.md`
- `.specgov/prompts/design-reviewer.md`

### 3.5 Test Manager
**职责**：
- 定义测试策略
- 编写测试用例
- 生成 Test Plan
- 审查 Test Plan

**任务文件**：`.specgov/tasks/test-manager.md`

**使用的 Prompts**：
- `.specgov/prompts/test-plan-generator.md`
- `.specgov/prompts/test-plan-reviewer.md`

### 3.6 Developer
**职责**：
- 实现代码
- 编写单元测试
- 运行测试
- 修复 bug

**任务文件**：`.specgov/tasks/developer.md`

**使用的 Prompts**：
- `.specgov/prompts/code-generator.md`
- `.specgov/prompts/code-reviewer.md`

## 4. General Workflow for Each Stage

### Step 1: Switch to Role Perspective
打开 `.specgov/tasks/[role].md` 查看分配的任务。

### Step 2: Load Generator Prompt in Claude Code
在 Claude Code 中加载 `.specgov/prompts/[stage]-generator.md`。

### Step 3: Provide Context
提供上游文档和额外的需求或约束：
- 生成 PRD：提供 RD.md
- 生成 Design Document：提供 PRD.md + 技术约束
- 生成 Test Plan：提供 Design-Document.md
- 生成 Code：提供 Design-Document.md

### Step 4: Generate Document
Claude Code 生成带有嵌入式可追溯性标记的文档。

### Step 5: Review Document
切换视角（或使用同一角色），加载 reviewer prompt，审查生成的文档。

### Step 6: Revise Based on Feedback
如果审查发现问题，再次使用 generator prompt（修改模式）处理审查反馈。

### Step 7: Update Task Documents
- 更新你的角色特定任务文件（`.specgov/tasks/[role].md`）
- 切换到 Project Manager 视角
- 更新 `.specgov/tasks/project-manager.md`，记录 Epic 进度

### Step 8: Run Helper Scripts (Optional)
- **解析标记**：`python scripts/parse_tags.py`
- **构建图谱**：`python scripts/build_graph.py`
- **影响分析**：`python scripts/impact_analysis.py --changed docs/RD.md`
- **一致性检查**：`python scripts/check_consistency.py --scope RD-REQ-005`

## 5. Key Principles

### 5.1 Explicit Traceability（显式可追溯性）
- 始终嵌入标记：`[ID: XXX]`, `[Implements: XXX]`, `[Designs-for: XXX]`, `[Tests-for: XXX]`
- 每个文档节点都可追踪到上游和下游
- 使用 helper scripts 构建和查询依赖图谱

### 5.2 Dual Quality Assurance（双重质量保证）
- **生成 + 审查**：每个阶段都有 generator 和 reviewer prompts
- 生成文档后立即审查
- 根据审查反馈修改文档

### 5.3 Two-Tier Task Management（双层任务管理）
- **Epic Level**（Project Manager）：高层级目标和进度追踪
- **Task Level**（各角色）：具体任务和执行细节

### 5.4 Correct Terminology（正确术语）
- ✅ "Design Document" ❌ "DD"
- ✅ "Test Plan" ❌ "TD"
- ✅ "Requirements Document" ❌ "RD Document"

### 5.5 Local-First, AI-Assisted（本地优先，AI 辅助）
- Helper scripts 本地运行（$0 成本）
- 只在生成/审查文档时使用 Claude Code（按使用付费）
- 可追溯性图谱本地构建和查询

## 6. Helper Scripts Overview

### 6.1 init_project.py
**用途**：初始化 SpecGovernor 项目结构

**用法**：
```powershell
python scripts/init_project.py
```

**输出**：
- `.specgov/` 目录结构
- `docs/` 占位符文档
- `.specgov/project-config.json` 配置文件

### 6.2 parse_tags.py
**用途**：从所有文件中解析可追溯性标记

**用法**：
```powershell
python scripts/parse_tags.py
```

**输出**：`.specgov/index/tags.json`

### 6.3 build_graph.py
**用途**：从解析的标记构建依赖图谱

**用法**：
```powershell
python scripts/build_graph.py
```

**输出**：`.specgov/index/dependency-graph.json`

### 6.4 impact_analysis.py
**用途**：分析文件变更的影响

**用法**：
```powershell
python scripts/impact_analysis.py --changed docs/RD.md
```

**输出**：控制台输出影响分析报告

### 6.5 check_consistency.py
**用途**：为指定需求收集完整依赖链上下文

**用法**：
```powershell
python scripts/check_consistency.py --scope RD-REQ-005 --output context.md
```

**输出**：`context.md` 上下文文件（供 Claude Code 使用）

## 7. Typical Project Workflow

### Phase 1: Project Initialization
1. **As Project Manager**：运行 `python scripts/init_project.py`
2. **As Project Manager**：在 `.specgov/tasks/project-manager.md` 中创建第一个 Epic
3. **As Project Manager**：分解 Epic 为任务，分配到各角色

### Phase 2: Requirements Analysis
1. **As Requirements Analyst**：收集用户故事和业务需求
2. **As Requirements Analyst**：在 Claude Code 中加载 `rd-generator.md`
3. **As Requirements Analyst**：提供输入，生成 `RD.md`
4. **As Requirements Analyst**：加载 `rd-reviewer.md`，审查 `RD.md`
5. **As Requirements Analyst**：根据审查反馈修改 `RD.md`
6. **As Requirements Analyst**：更新 `.specgov/tasks/rd-analyst.md`

### Phase 3: Product Planning
1. **As Product Manager**：加载 `prd-generator.md`
2. **As Product Manager**：提供 `RD.md` 和产品愿景，生成 `PRD.md`
3. **As Product Manager**：加载 `prd-reviewer.md`，审查 `PRD.md`
4. **As Product Manager**：根据审查反馈修改 `PRD.md`
5. **As Product Manager**：更新 `.specgov/tasks/product-manager.md`

### Phase 4: Technical Design
1. **As Architect**：加载 `design-generator.md`
2. **As Architect**：提供 `PRD.md` 和技术约束，生成 `Design-Document.md`
3. **As Architect**：加载 `design-reviewer.md`，审查 `Design-Document.md`
4. **As Architect**：根据审查反馈修改 `Design-Document.md`
5. **As Architect**：更新 `.specgov/tasks/architect.md`

### Phase 5: Test Planning
1. **As Test Manager**：加载 `test-plan-generator.md`
2. **As Test Manager**：提供 `Design-Document.md`，生成 `Test-Plan.md`
3. **As Test Manager**：加载 `test-plan-reviewer.md`，审查 `Test-Plan.md`
4. **As Test Manager**：根据审查反馈修改 `Test-Plan.md`
5. **As Test Manager**：更新 `.specgov/tasks/test-manager.md`

### Phase 6: Implementation
1. **As Developer**：加载 `code-generator.md`
2. **As Developer**：提供 `Design-Document.md`，生成代码
3. **As Developer**：加载 `code-reviewer.md`，审查代码
4. **As Developer**：根据审查反馈修改代码
5. **As Developer**：运行测试
6. **As Developer**：更新 `.specgov/tasks/developer.md`

### Phase 7: Verification and Maintenance
1. **Run Helper Scripts**：
   - `python scripts/parse_tags.py`
   - `python scripts/build_graph.py`
2. **Check Consistency**：
   - `python scripts/check_consistency.py --scope RD-REQ-005`
   - 在 Claude Code 中加载 `consistency-checker.md`，审查一致性
3. **Analyze Impact**（当有变更时）：
   - `python scripts/impact_analysis.py --changed docs/RD.md`
   - 在 Claude Code 中加载 `impact-analyzer.md`，获得详细分析

## 8. Tips for Success

1. **保持可追溯性**：
   - 始终添加 `[ID: XXX]` 标记
   - 始终链接到上游（`[Implements: XXX]`, `[Designs-for: XXX]`, `[Tests-for: XXX]`）

2. **遵循双重质量保证**：
   - 生成后立即审查
   - 不要跳过审查步骤

3. **定期更新依赖图谱**：
   - 每次文档更新后运行 `parse_tags.py` 和 `build_graph.py`
   - 保持图谱最新，以便影响分析和一致性检查

4. **使用正确术语**：
   - "Design Document"（不是 "DD"）
   - "Test Plan"（不是 "TD"）

5. **记录进度**：
   - 更新 `.specgov/tasks/` 文件
   - 保持任务状态最新

6. **利用 Helper Scripts**：
   - 影响分析：了解变更影响
   - 一致性检查：确保文档一致
   - 本地运行，$0 成本

## 9. Next Steps

查看每个阶段的详细工作流：
- [RD Workflow](workflow-rd.md)
- [PRD Workflow](workflow-prd.md)
- [Design Document Workflow](workflow-design.md)
- [Test Plan Workflow](workflow-test-plan.md)
- [Task Management Workflow](workflow-task-mgmt.md)
- [Large Project Workflow](workflow-large-project.md)

---

**Ready to start?** 运行 `python scripts/init_project.py` 初始化项目，然后查看具体阶段的 workflow 文档！
