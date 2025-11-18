# **📦 Product Requirements Document (PRD) - SpecGovernor**

> **Target User**: Super Individual (超级个体) using Claude Code
> **Product Type**: Toolkit (Prompt Templates + Workflow Documentation + Helper Scripts)

---

## **Architecture Notice (v3.0)**

**SDLC 流程**：SpecGovernor 采用 **4 阶段流程**

```
PRD → Design Document → Test Plan → Code
```

**v3.0 简化架构说明**：
- ✅ **原始需求收集**：产品经理收集离散、口语化的原始需求（存储在 `raw-requirements/`）
- ✅ **PRD 定义产品功能**：基于原始需求，直接定义产品功能（无需中间的"业务需求"层）
- ✅ **每个阶段使用 Generator-Reviewer 对模式**确保质量
- ✅ **通过可追溯性标记建立完整追踪链**

**与 v2.0 的主要变化**：
- ❌ 取消了独立的 RD（Requirements Document）
- ❌ 取消了 PRD Part 1（Business Requirements）层
- ✅ PRD 直接定义产品功能，可选引用原始需求 Entry

---

## **Traceability Declaration**

**[ID: PRD-TRACE-001]**

本文档采用**显式可追溯性标记 (Explicit Traceability Tagging)** 策略，建立：

```
原始需求（Raw Requirements）
  Entry 001, Entry 002, ... (离散、非结构化)
    ↓ [可选引用: Raw-Req: Entry-XXX]
PRD-FEAT-XXX (产品功能)
    ↓ [Designs-for: PRD-FEAT-XXX]
DESIGN-XXX (设计)
    ↓ [Tests-for: DESIGN-XXX]
TEST-XXX (测试)
    ↓ [Implements: DESIGN-XXX]
CODE-XXX (代码)
```

**标记说明**：
- **[ID: PRD-FEAT-XXX]**：产品功能唯一标识
- **[Raw-Req: Entry-XXX]**：可选，引用原始需求的 Entry 编号
- **[Designs-for: PRD-FEAT-XXX]**：设计实现某个产品功能
- **[Tests-for: DESIGN-XXX]**：测试验证某个设计
- **[Implements: DESIGN-XXX]**：代码实现某个设计

---

## **术语与缩略语 (Terminology and Glossary)**

**[ID: PRD-GLOSSARY-001]**

| 术语/缩略语 | 英文全称 | 解释说明 |
|:-----------|:--------|:--------|
| **SDLC** | Software Development Life Cycle | 软件开发生命周期 |
| **PRD** | Product Requirements Document | 产品需求文档（定义产品功能） |
| **Design Document** | Design Document | 设计文档（**必须使用完整名称，不缩写为 DD**） |
| **Test Plan** | Test Plan | 测试计划（**必须使用完整名称，不缩写为 TD/TP**） |
| **Claude Code** | Claude Code | Anthropic 的 AI 编程助手 |
| **Prompt Template** | 提示词模板 | 预定义的 AI 提示词，用于引导 Claude Code 生成特定内容 |
| **Traceability Tag** | 可追溯性标记 | 在文档或代码中嵌入的结构化标记，如 `[ID: PRD-FEAT-012]` |
| **Workflow** | 工作流程 | 标准化的开发流程步骤 |
| **Helper Script** | 辅助脚本 | 自动化处理某些任务的 Python 脚本 |
| **Epic** | Epic | 高层级任务，由项目经理管理 |
| **Module** | 模块 | 大型项目中的功能模块（如用户模块、支付模块） |
| **Raw Requirements** | 原始需求 | 人类提供的口语化、零散的需求输入 |
| **Entry** | Entry | 原始需求文档中的单个需求条目 |

**重要原则**：
- ✅ 文档文件名必须使用英文：`PRD.md`, `Design-Document.md`, `Test-Plan.md`
- ❌ 禁止缩写：不使用 `DD.md`, `TD.md`
- ✅ 文档内容中文为主，专业术语、代码使用英文

---

# **Product Features（产品功能）**

> 本部分基于原始需求，定义具体的产品功能和用户体验。每个功能可选地引用原始需求的 Entry 编号，建立追溯关系。

---

## **一、原始需求收集功能 (Raw Requirements Collection)**

### **1.1 原始需求记录功能**

**[ID: PRD-FEAT-001]**

#### **功能描述**

产品经理在生成 PRD 时，系统自动执行两步操作：
1. 询问并记录人类提供的原始需求（口语化）
2. 基于原始需求生成正式的 PRD 文档

#### **用户体验**

**小项目流程**：
```
用户: /specgov-prd-gen
  ↓
产品经理: 在生成正式 PRD 之前，请告诉我您的原始需求...
  ↓
用户: （口语化描述需求）
  ↓
产品经理:
  ├─ 记录到 docs/raw-requirements/inputs.md
  └─ 生成 docs/PRD.md
  ↓
完成
```

**大项目流程**：
```
用户: /specgov-prd-overview 或 /specgov-prd-module
  ↓
产品经理: 请告诉我项目级/模块级需求...
  ↓
用户: （口语化描述需求）
  ↓
产品经理:
  ├─ 记录到 docs/raw-requirements/overview.md 或 modules/{module}.md
  └─ 生成 docs/PRD/PRD-Overview.md 或 PRD-{Module}.md
  ↓
完成
```

#### **功能细节**

**Entry 格式**：
```markdown
### Entry XXX - YYYY-MM-DD HH:MM

**Source**: Chat / File / Email / Meeting Notes
**Topic**: [简短主题]

**Original Input**:
> [保持原始输入的口语化表达]

**PM Analysis**:
- **Category**: Functional / Non-Functional / UI/UX / Performance / Security
- **Priority**: High / Medium / Low
- **Related Modules**: [相关模块]
- **Initial Thoughts**: [初步想法]
- **Questions**: [需要澄清的问题]
- **Status**: New / Under Review / Converted to PRD / Rejected
```

### **1.2 统计分析功能**

**[ID: PRD-FEAT-002]**

#### **功能描述**

在原始需求文档底部，自动维护统计信息。

#### **统计内容**

```markdown
## 📊 Summary Statistics

**Last Updated**: YYYY-MM-DD

- **Total Entries**: X
- **By Priority**:
  - High: X
  - Medium: X
  - Low: X
- **By Status**:
  - New: X
  - Under Review: X
  - Converted to PRD: X
  - Rejected: X
```

### **1.3 追溯查询功能**

**[ID: PRD-FEAT-003]**

#### **功能描述**

在 PRD 中可选引用原始需求 Entry 编号，建立追溯关系。

#### **示例**

```markdown
### OAuth2 Login Feature
**[ID: PRD-FEAT-012]**
**[Raw-Req: Entry-003, Entry-007]**

基于用户的原始需求（见 docs/raw-requirements/inputs.md Entry-003）...
```

---

## **二、提示词模板功能 (Prompt Templates)**

### **2.1 PRD Generator 模板**

**[ID: PRD-FEAT-004]**

#### **功能描述**

提供 PRD 生成提示词模板，指导 Claude Code 生成符合规范的 PRD 文档。

#### **模板类型**

| 模板文件 | 用途 | 适用项目 |
|:--------|:-----|:--------|
| `prd-generator.md` | 生成或修改 PRD.md | 小项目 |
| `prd-overview-generator.md` | 生成 PRD-Overview.md | 大项目 |
| `prd-module-generator.md` | 生成 PRD-{Module}.md | 大项目 |

#### **模板内容**

- ✅ 集成原始需求收集工作流
- ✅ Step 1: 询问并记录原始需求
- ✅ Step 2: 基于原始需求生成正式 PRD
- ✅ 输出包含 Part 1（Business Requirements）和 Part 2（Product Features）
- ✅ 所有需求和功能都有可追溯性标记

### **2.2 PRD Reviewer 模板**

**[ID: PRD-FEAT-005]**

#### **功能描述**

提供 PRD 评审提示词模板，检查 PRD 的质量、完整性、可追溯性。

#### **检查项**

- ✅ 可追溯性标记完整性（所有需求都有 `[ID: PRD-REQ-XXX]`）
- ✅ 关系标记正确性（`[Implements: XXX]`, `[Decomposes: XXX]`）
- ✅ 文档结构规范性
- ✅ 验收标准可测试性
- ✅ 业务价值清晰性

### **2.3 Design Document Generator 模板**

**[ID: PRD-FEAT-006]**

#### **功能描述**

提供设计文档生成提示词模板，基于 PRD 生成技术设计。

#### **模板类型**

| 模板文件 | 用途 | 适用项目 |
|:--------|:-----|:--------|
| `design-generator.md` | 生成 Design-Document.md | 小项目 |
| `design-overview-generator.md` | 生成 Design-Overview.md | 大项目 |
| `design-module-generator.md` | 生成 Design-{Module}.md | 大项目 |

#### **输出内容**

- ✅ 架构设计（`[ID: DESIGN-ARCH-XXX]`）
- ✅ API 设计（`[ID: DESIGN-API-XXX]`）
- ✅ 数据库设计（`[ID: DESIGN-DB-XXX]`）
- ✅ 所有设计都有 `[Designs-for: PRD-FEAT-XXX]` 关系标记

### **2.4 Design Document Reviewer 模板**

**[ID: PRD-FEAT-007]**

#### **功能描述**

评审设计文档的技术合理性、可实现性、可追溯性。

### **2.5 Test Plan Generator 模板**

**[ID: PRD-FEAT-008]**

#### **功能描述**

提供测试计划生成提示词模板，基于 Design Document 生成测试用例。

#### **模板类型**

| 模板文件 | 用途 | 适用项目 |
|:--------|:-----|:--------|
| `test-plan-generator.md` | 生成 Test-Plan.md | 小项目 |
| `test-plan-overview-generator.md` | 生成 Test-Overview.md | 大项目 |
| `test-plan-module-generator.md` | 生成 Test-{Module}.md | 大项目 |

#### **输出内容**

- ✅ 测试用例（`[ID: TEST-CASE-XXX]`）
- ✅ 性能测试（`[ID: TEST-PERF-XXX]`）
- ✅ 所有测试都有 `[Tests-for: DESIGN-XXX]` 关系标记
- ✅ 包含前置条件、测试步骤、预期结果

### **2.6 Test Plan Reviewer 模板**

**[ID: PRD-FEAT-009]**

#### **功能描述**

评审测试计划的覆盖率、可执行性、可追溯性。

### **2.7 Code Generator 模板**

**[ID: PRD-FEAT-010]**

#### **功能描述**

提供代码生成提示词模板，基于 Design Document 生成代码实现。

#### **输出内容**

- ✅ 代码包含 `[ID: CODE-XXX]` 注释标记
- ✅ 代码包含 `[Implements: DESIGN-XXX]` 关系标记
- ✅ 遵循语言编码规范
- ✅ 包含单元测试

### **2.8 Code Reviewer 模板**

**[ID: PRD-FEAT-011]**

#### **功能描述**

评审代码的质量、安全性、可维护性、可追溯性。

#### **检查项**

- ✅ 代码安全性（OWASP Top 10）
- ✅ 代码质量（命名规范、注释完整性）
- ✅ 性能考虑
- ✅ 可追溯性标记完整性

### **2.9 一致性检查模板**

**[ID: PRD-FEAT-012]**

#### **功能描述**

检查 PRD、Design Document、Test Plan、Code 之间的一致性。

### **2.10 影响分析模板**

**[ID: PRD-FEAT-013]**

#### **功能描述**

分析文档或代码变更对下游的影响范围。

---

## **三、工作流程文档功能 (Workflow Documentation)**

### **3.1 工作流程总览**

**[ID: PRD-FEAT-014]**

#### **功能描述**

提供 `workflows/workflow-overview.md`，介绍完整的 4 阶段 SDLC 流程。

#### **内容**

- ✅ 4 阶段流程概览（PRD → Design → Test → Code）
- ✅ Generator-Reviewer 对模式说明
- ✅ 可追溯性标记说明
- ✅ Claude Code 集成说明

### **3.2 PRD 工作流程**

**[ID: PRD-FEAT-015]**

#### **功能描述**

提供 `workflows/workflow-prd.md`，详细说明 PRD 生成和评审流程。

#### **流程步骤**

1. 产品经理收集原始需求（自动完成）
2. 产品经理生成 PRD.md
3. 评审员审查 PRD.md
4. 产品经理根据评审反馈修改 PRD.md
5. 验收标准检查

### **3.3 Design Document 工作流程**

**[ID: PRD-FEAT-016]**

#### **功能描述**

提供 `workflows/workflow-design.md`。

### **3.4 Test Plan 工作流程**

**[ID: PRD-FEAT-017]**

#### **功能描述**

提供 `workflows/workflow-test-plan.md`。

### **3.5 Code 工作流程**

**[ID: PRD-FEAT-018]**

#### **功能描述**

提供 `workflows/workflow-code.md`。

### **3.6 任务管理工作流程**

**[ID: PRD-FEAT-019]**

#### **功能描述**

提供 `workflows/workflow-task-mgmt.md`，说明 Epic 和 Task 两层管理。

#### **两层管理**

- **High-level (Epic)**：项目经理管理整体进度
- **Low-level (Task)**：具体角色管理具体任务

### **3.7 大项目工作流程**

**[ID: PRD-FEAT-020]**

#### **功能描述**

提供 `workflows/workflow-large-project.md`，说明双层文档结构的使用方式。

---

## **四、辅助脚本功能 (Helper Scripts)**

### **4.1 项目初始化脚本**

**[ID: PRD-FEAT-021]**

#### **功能描述**

`scripts/init_project.py` - 初始化 SpecGovernor 项目结构。

#### **功能**

- ✅ 提示用户选择项目规模（小/大）
- ✅ 创建 `.specgov/` 目录结构
- ✅ 创建原始需求收集目录和模板
- ✅ 创建任务文件（6 个角色）
- ✅ 创建 docs/ 文档占位符
- ✅ 创建 Claude Code 斜杠命令
- ✅ 生成 `project-config.json`

### **4.2 标记解析脚本**

**[ID: PRD-FEAT-022]**

#### **功能描述**

`scripts/parse_tags.py` - 从文档和代码中解析可追溯性标记。

#### **功能**

- ✅ 扫描所有 `.md` 和代码文件
- ✅ 提取 `[ID: XXX]`, `[Implements: XXX]` 等标记
- ✅ 输出 JSON 格式（`.specgov/index/tags.json`）
- ✅ 统计标记类型和数量
- ✅ 自动提取模块信息（大项目）

### **4.3 依赖图构建脚本**

**[ID: PRD-FEAT-023]**

#### **功能描述**

`scripts/build_graph.py` - 从标记构建依赖图谱。

#### **功能**

- ✅ 读取 `tags.json`
- ✅ 创建节点（所有 ID）
- ✅ 创建边（所有关系）
- ✅ 检测循环依赖
- ✅ 输出 JSON 格式（`.specgov/index/dependency-graph.json`）

### **4.4 影响分析脚本**

**[ID: PRD-FEAT-024]**

#### **功能描述**

`scripts/impact_analysis.py` - 分析文档变更的影响范围。

#### **功能**

- ✅ 基于 Git diff 识别变更的文件
- ✅ 查询依赖图，找到下游节点
- ✅ 输出受影响的文档和代码清单
- ✅ 性能 < 10 秒

### **4.5 一致性检查脚本**

**[ID: PRD-FEAT-025]**

#### **功能描述**

`scripts/check_consistency.py` - 验证可追溯性链的完整性。

#### **功能**

- ✅ 定位指定 ID 的依赖链
- ✅ 提取依赖链涉及的文档和代码片段
- ✅ 构建上下文（< 5K tokens）
- ✅ 输出 context.md 供 Claude Code 使用

---

## **五、任务管理功能 (Task Management)**

### **5.1 任务文件**

**[ID: PRD-FEAT-026]**

#### **功能描述**

提供 6 个角色的任务文件，支持 Epic 和 Task 两层管理。

#### **文件列表**

| 文件 | 角色 | 管理内容 |
|:----|:-----|:--------|
| `tasks/project-manager.md` | 项目经理 | Epic 创建、整体进度、里程碑 |
| `tasks/product-manager.md` | 产品经理 | PRD 生成、原始需求收集 |
| `tasks/architect.md` | 架构师 | Design Document 生成 |
| `tasks/test-manager.md` | 测试经理 | Test Plan 生成 |
| `tasks/developer.md` | 开发工程师 | Code 实现 |

### **5.2 任务模板**

**[ID: PRD-FEAT-027]**

#### **任务文件结构**

```markdown
# [Role] Tasks

## Active Tasks
（当前正在进行的任务）

### Task 1: [任务标题]
- **Epic**: Epic 1
- **描述**: [任务描述]
- **状态**: 进行中
- **预估时间**: X 小时
- **输出**: [交付物]

## Completed Tasks
（已完成的任务）
```

---

## **六、Claude Code 集成功能 (Claude Code Integration)**

### **6.1 斜杠命令（小项目）**

**[ID: PRD-FEAT-028]**

#### **命令列表**

| 命令 | 功能 |
|:----|:-----|
| `/specgov-prd-gen` | 生成 PRD.md（包含原始需求收集） |
| `/specgov-prd-review` | 审查 PRD.md |
| `/specgov-design-gen` | 生成 Design-Document.md |
| `/specgov-design-review` | 审查 Design Document |
| `/specgov-test-gen` | 生成 Test-Plan.md |
| `/specgov-test-review` | 审查 Test Plan |
| `/specgov-code-gen` | 生成代码 |
| `/specgov-code-review` | 审查代码 |
| `/specgov-consistency` | 一致性检查 |
| `/specgov-impact` | 影响分析 |

### **6.2 斜杠命令（大项目）**

**[ID: PRD-FEAT-029]**

#### **Overview 命令**

| 命令 | 功能 |
|:----|:-----|
| `/specgov-prd-overview` | 生成 PRD-Overview.md |
| `/specgov-design-overview` | 生成 Design-Overview.md |
| `/specgov-test-overview` | 生成 Test-Overview.md |

#### **Module 命令**

| 命令 | 功能 |
|:----|:-----|
| `/specgov-prd-module` | 生成 PRD-{Module}.md |
| `/specgov-design-module` | 生成 Design-{Module}.md |
| `/specgov-test-module` | 生成 Test-{Module}.md |

---

## **七、可追溯性标记规范 (Traceability Tag Specification)**

**[ID: PRD-FEAT-030]**

### **7.1 标记类型**

| 标记类型 | 格式 | 示例 | 用途 |
|:--------|:-----|:-----|:-----|
| **ID** | `[ID: XXX]` | `[ID: PRD-REQ-001]` | 定义唯一标识符 |
| **Implements** | `[Implements: XXX]` | `[Implements: PRD-REQ-001]` | 实现关系 |
| **Decomposes** | `[Decomposes: XXX]` | `[Decomposes: PRD-REQ-001]` | 分解关系 |
| **Designs-for** | `[Designs-for: XXX]` | `[Designs-for: PRD-FEAT-012]` | 设计关系 |
| **Tests-for** | `[Tests-for: XXX]` | `[Tests-for: DESIGN-API-008]` | 测试关系 |

### **7.2 ID 前缀规范**

| 阶段 | 前缀 | 示例 | 说明 |
|:----|:-----|:-----|:-----|
| **PRD - 业务需求** | `PRD-REQ-` | `PRD-REQ-001` | 业务需求标识 |
| **PRD - 产品功能** | `PRD-FEAT-` | `PRD-FEAT-012` | 产品功能标识 |
| **PRD - 用户故事** | `PRD-US-` | `PRD-US-003` | 用户故事标识 |
| **PRD - 目标** | `PRD-GOAL-` | `PRD-GOAL-001` | 项目目标标识 |
| **PRD - 非功能需求** | `PRD-NFR-` | `PRD-NFR-001` | 非功能需求标识 |
| **Design - 架构** | `DESIGN-ARCH-` | `DESIGN-ARCH-001` | 架构设计标识 |
| **Design - API** | `DESIGN-API-` | `DESIGN-API-008` | API 设计标识 |
| **Design - 数据库** | `DESIGN-DB-` | `DESIGN-DB-005` | 数据库设计标识 |
| **Test - 测试用例** | `TEST-CASE-` | `TEST-CASE-015` | 测试用例标识 |
| **Test - 性能测试** | `TEST-PERF-` | `TEST-PERF-002` | 性能测试标识 |
| **Code** | `CODE-` | `CODE-API-008` | 代码标识 |

### **7.3 嵌入位置**

**PRD.md**:
```markdown
### OAuth2 Login Requirement
**[ID: PRD-REQ-005]**

系统需支持通过 OAuth2 协议进行用户登录...

---

### OAuth2 Social Login Feature
**[ID: PRD-FEAT-012]**

用户可以使用 Google、GitHub 账号登录...
```

**Design-Document.md**:
```markdown
### OAuth2 Authentication Service
**[ID: DESIGN-API-008] [Designs-for: PRD-FEAT-012]**

提供 OAuth2 认证服务...
```

**Test-Plan.md**:
```markdown
### OAuth2 Login Test
**[ID: TEST-CASE-015] [Tests-for: DESIGN-API-008]**

测试 OAuth2 登录流程...
```

**Code**:
```typescript
/**
 * OAuth2 Authentication Service
 * [ID: CODE-API-008] [Implements: DESIGN-API-008]
 */
export class OAuth2Service {
  // ...
}
```

---

## **八、目录结构规范 (Directory Structure)**

**[ID: PRD-STRUCTURE-001]**

### **8.1 小项目目录结构**

```
your-project/
├── .specgov/
│   ├── scripts/                    # Helper Scripts
│   │   ├── init_project.py
│   │   ├── parse_tags.py
│   │   ├── build_graph.py
│   │   ├── impact_analysis.py
│   │   └── check_consistency.py
│   ├── prompts/                    # Prompt Templates
│   │   ├── prd-generator.md
│   │   ├── prd-reviewer.md
│   │   ├── design-generator.md
│   │   ├── design-reviewer.md
│   │   ├── test-plan-generator.md
│   │   ├── test-plan-reviewer.md
│   │   ├── code-generator.md
│   │   ├── code-reviewer.md
│   │   ├── consistency-checker.md
│   │   └── impact-analyzer.md
│   ├── workflows/                  # Workflow Documentation
│   │   ├── workflow-overview.md
│   │   ├── workflow-prd.md
│   │   ├── workflow-design.md
│   │   ├── workflow-test-plan.md
│   │   ├── workflow-code.md
│   │   └── workflow-task-mgmt.md
│   ├── tasks/                      # Task Management
│   │   ├── project-manager.md
│   │   ├── product-manager.md
│   │   ├── architect.md
│   │   ├── test-manager.md
│   │   └── developer.md
│   ├── raw-requirements/           # Raw Requirements Collection
│   │   └── inputs.md               # Single aggregated file
│   ├── index/                      # Generated Indexes
│   │   ├── tags.json
│   │   └── dependency-graph.json
│   └── project-config.json
├── .claude/
│   └── commands/                   # Claude Code Slash Commands
│       ├── specgov-prd-gen.md
│       ├── specgov-prd-review.md
│       ├── specgov-design-gen.md
│       ├── specgov-design-review.md
│       ├── specgov-test-gen.md
│       ├── specgov-test-review.md
│       ├── specgov-code-gen.md
│       ├── specgov-code-review.md
│       ├── specgov-consistency.md
│       └── specgov-impact.md
├── docs/                           # Project Documents
│   ├── PRD.md
│   ├── Design-Document.md
│   └── Test-Plan.md
├── reviews/                        # Review Reports
│   ├── PRD-Review-Report-2025-11-17.md
│   └── ...
├── src/                            # Source Code
└── CLAUDE.md                       # Project Guide
```

### **8.2 大项目目录结构**

```
your-project/
├── .specgov/
│   ├── (same as small project)
│   ├── raw-requirements/
│   │   ├── overview.md             # Project-level requirements
│   │   └── modules/                # Module-level requirements
│   │       ├── user-module.md
│   │       ├── order-module.md
│   │       └── payment-module.md
│   └── project-config.json
├── .claude/
│   └── commands/
│       ├── specgov-prd-overview.md
│       ├── specgov-prd-module.md
│       ├── specgov-design-overview.md
│       ├── specgov-design-module.md
│       ├── specgov-test-overview.md
│       ├── specgov-test-module.md
│       └── (other commands)
├── docs/
│   ├── PRD/
│   │   ├── PRD-Overview.md
│   │   ├── PRD-User-Module.md
│   │   ├── PRD-Order-Module.md
│   │   └── PRD-Payment-Module.md
│   ├── Design-Document/
│   │   ├── Design-Overview.md
│   │   ├── Design-User-Module.md
│   │   ├── Design-Order-Module.md
│   │   └── Design-Payment-Module.md
│   └── Test-Plan/
│       ├── Test-Overview.md
│       ├── Test-User-Module.md
│       ├── Test-Order-Module.md
│       └── Test-Payment-Module.md
└── src/
```

---

## **九、成功指标 (Success Metrics)**

**[ID: PRD-METRICS-001]**

### **9.1 使用指标**

- **安装时间**: < 5 分钟
- **学习时间**: < 1 小时（通过快速开始指南）
- **首次生成 PRD 时间**: < 15 分钟

### **9.2 质量指标**

- **可追溯性覆盖率**: 100%（所有需求都有对应的设计、测试、代码）
- **文档一致性**: 0 断链（所有引用都能找到目标）
- **代码覆盖率**: > 80%（Helper Scripts）

### **9.3 性能指标**

- **标记解析时间**: < 1 分钟（100K LOC）
- **依赖图构建时间**: < 1 分钟
- **影响分析时间**: < 10 秒

---

## **十、总结 (Summary)**

**[ID: PRD-SUMMARY-001]**

SpecGovernor v3.0 是一个为超级个体设计的全流程可追溯性工具包，通过：

1. **4 阶段 SDLC 流程**：PRD → Design Document → Test Plan → Code
2. **原始需求收集功能**：产品经理自动收集和记录口语化原始需求
3. **16 个提示词模板**：覆盖生成和评审的所有场景
4. **8 个 Helper Scripts**：自动化标记解析、依赖图构建、影响分析
5. **Claude Code 深度集成**：20 个斜杠命令快速加载模板
6. **两种项目规模支持**：小项目（单层文档）和大项目（双层文档）
7. **100% 可追溯性**：通过嵌入式标记实现需求到代码的完整追踪

实现零成本、AI 驱动的软件开发全流程管理。

---

**文档结束**
