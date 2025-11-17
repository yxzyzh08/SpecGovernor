# **📦 Product Requirements Document (PRD) - SpecGovernor**

> **Version**: v3.0
> **Created**: 2025-11-16
> **Updated**: 2025-11-17
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

## **一、术语与缩略语 (Terminology and Glossary)**

| 术语/缩略语 | 英文全称 | 解释说明 |
| :---- | :---- | :---- |
| **SDLC** | Software Development Life Cycle | 软件开发生命周期 |
| **RD** | Requirements Document | 需求文档（行业标准术语） |
| **PRD** | Product Requirements Document | 产品需求文档（行业标准术语） |
| **Design Document** | Design Document | 设计文档（使用完整名字，不缩写为 DD） |
| **Test Plan** | Test Plan | 测试计划（使用完整名字，不缩写为 TD） |
| **Claude Code** | Claude Code | Anthropic 的 AI 编程助手 |
| **Prompt Template** | 提示词模板 | 预定义的 AI 提示词，用于引导 Claude Code 生成特定内容 |
| **Traceability Tag** | 可追溯性标记 | 在文档或代码中嵌入的结构化标记，如 `[ID: PRD-REQ-005]` |
| **Workflow** | 工作流程 | 标准化的开发流程步骤 |
| **Helper Script** | 辅助脚本 | 自动化处理某些任务的小型脚本 |
| **Epic** | Epic | 高层级任务，由项目经理管理 |
| **Module** | 模块 | 大型项目中的功能模块（如用户模块、支付模块） |
| **Project Size** | 项目规模 | 小项目（单层文档）或大项目（双层文档） |

---

## **二、项目目标 (Project Goals)**

**[ID: PRD-GOAL-001]**

| ID | 目标描述 | 达成标准 |
| :---- | :---- | :---- |
| **G-1** | **提供标准化提示词模板** | 覆盖 RD/PRD/Design Document/Test Plan/Code 生成和评审的所有场景 |
| **G-2** | **定义规范化开发流程** | 提供清晰的流程文档，人类开发者可以遵循 |
| **G-3** | **实现可追溯性** | 通过嵌入标记，建立 RD → PRD → Design Document → Test Plan → Code 的追溯链 |
| **G-4** | **提供辅助工具** | 简单的脚本帮助解析标记、构建依赖图、影响分析 |
| **G-5** | **易于使用** | 人类开发者可以直接使用，无需安装复杂软件 |

---

## **三、目标用户 (Target Users)**

### **3.1 超级个体 (Super Individual)**

**[ID: PRD-USER-001]**

目标用户是**超级个体**，即一人承担多个研发角色的技术专家：

| 角色 | 职责 | 任务视角 |
| :---- | :---- | :---- |
| **项目经理** | 创建 Epic，分解子任务，跟踪整体进度，协调各角色 | High-level（Epic 级别） |
| **需求分析师** | 使用 RD Generator 提示词生成需求文档 | Low-level（Task 级别） |
| **产品经理** | 使用 PRD Generator 提示词生成产品文档 | Low-level（Task 级别） |
| **架构师** | 使用 Design Document Generator 提示词生成设计文档 | Low-level（Task 级别） |
| **测试经理** | 使用 Test Plan Generator 提示词生成测试计划 | Low-level（Task 级别） |
| **开发工程师** | 使用 Code Generator 提示词生成代码 | Low-level（Task 级别） |

**说明**：
- 虽然使用者是同一个人（超级个体），但需要在**不同视角**间切换
- **项目经理视角**：关注整体进度、里程碑、交付物（High-level）
- **具体角色视角**：关注具体任务、技术细节、实现（Low-level）
- 每个角色完成任务后需要更新**两处**：自己的任务文档 + 项目经理的任务文档

### **3.2 使用方式**

**[ID: PRD-USER-002]**

1. 打开 **Claude Code**
2. 加载 SpecGovernor 提供的**提示词模板**
3. 提供项目上下文和输入
4. Claude Code 按照模板生成规范化的文档/代码
5. 使用 **Reviewer 提示词**进行评审
6. 使用**辅助脚本**解析标记、构建依赖图

---

## **四、项目规模与文档结构策略 (Project Size & Document Structure)**

### **4.1 项目初始化**

**[ID: PRD-INIT-001]**

在项目开始时，需要**初始化** SpecGovernor 结构，并让人类开发者选择项目规模。

**初始化流程**：

1. 创建 `.specgov/` 目录结构
2. 提示用户选择项目规模：
   ```
   请选择项目规模：
   1. 小项目（< 10 万行代码，单层文档结构）
   2. 大项目（≥ 10 万行代码，双层文档结构）

   您的选择：_
   ```
3. 根据选择创建相应的文档模板和目录结构
4. 生成 `.specgov/project-config.json` 记录项目配置

**配置文件示例**：
```json
{
  "project_name": "my-project",
  "project_size": "small",
  "document_structure": "single-tier",
  "created_at": "2025-11-16",
  "modules": []
}
```

或

```json
{
  "project_name": "large-e-commerce",
  "project_size": "large",
  "document_structure": "two-tier",
  "created_at": "2025-11-16",
  "modules": ["user", "order", "payment", "product", "cart"]
}
```

### **4.2 项目规模分类**

**[ID: PRD-SIZE-001]**

| 项目规模 | 代码量 | 模块数 | 文档结构 | 适用场景 |
| :---- | :---- | :---- | :---- | :---- |
| **小项目** | < 10 万行 | 1-3 个 | 单层文档 | 单体应用、小型工具、原型项目 |
| **大项目** | ≥ 10 万行 | 4+ 个 | 双层文档 | 企业级应用、微服务系统、复杂业务系统 |

### **4.3 文档结构策略**

#### **4.3.1 小项目：单层文档结构**

**[ID: PRD-STRUCTURE-SMALL-001]**

所有需求、设计、测试都写在单个文档中：

```
docs/
├── RD.md                    # 所有需求
├── PRD.md                   # 所有产品功能
├── Design-Document.md       # 所有设计
└── Test-Plan.md             # 所有测试用例
```

**优点**：
- 简单直接，易于导航
- 适合 AI 一次性处理（< 10K tokens）
- 无需管理模块间关系

#### **4.3.2 大项目：双层文档结构**

**[ID: PRD-STRUCTURE-LARGE-001]**

每个文档类型都有两层：**Overview**（总览）+ **Module**（模块详细）

**RD 层面**：
```
docs/RD/
├── RD-Overview.md           # High-level 需求总览
├── RD-User-Module.md        # 用户模块需求详细
├── RD-Order-Module.md       # 订单模块需求详细
├── RD-Payment-Module.md     # 支付模块需求详细
└── RD-Product-Module.md     # 产品模块需求详细
```

**PRD 层面**：
```
docs/PRD/
├── PRD-Overview.md          # 产品功能总览
├── PRD-User-Module.md       # 用户模块产品设计
├── PRD-Order-Module.md      # 订单模块产品设计
└── ...
```

**Design Document 层面**：
```
docs/Design/
├── Design-Overview.md       # 架构总览
├── Design-User-Module.md    # 用户模块设计
├── Design-Order-Module.md   # 订单模块设计
└── ...
```

**Test Plan 层面**：
```
docs/Test/
├── Test-Overview.md         # 测试策略总览
├── Test-User-Module.md      # 用户模块测试
├── Test-Order-Module.md     # 订单模块测试
└── ...
```

**优点**：
- 避免单个文档过大（每个模块 < 10K tokens）
- 模块化管理，职责清晰
- 支持模块并行开发
- AI 可以分别处理每个模块

### **4.4 文档生成策略**

**[ID: RD-GEN-STRATEGY-001]**

#### **小项目生成流程**

1. 使用 `rd-generator.md` 生成单个 `RD.md`
2. 使用 `prd-generator.md` 生成单个 `PRD.md`
3. 依此类推...

#### **大项目生成流程**

**两步生成**：

**Step 1: 生成 Overview**
1. 使用 `rd-overview-generator.md` 生成 `RD-Overview.md`（High-level）
2. Overview 定义：
   - 项目整体目标
   - 模块划分和职责
   - 模块间依赖关系
   - 整体约束和非功能需求

**Step 2: 生成各模块详细文档**
1. 使用 `rd-module-generator.md` 逐个生成：
   - `RD-User-Module.md`
   - `RD-Order-Module.md`
   - ...
2. 每个模块文档包含：
   - 模块内的详细需求
   - 嵌入 `[Module: User]` 标记
   - 引用 Overview 中的模块定义

**PRD/Design Document/Test Plan 同样采用两步生成**。

### **4.5 可追溯性标记扩展（大项目）**

**[ID: PRD-TRACE-MODULE-001]**

大项目的标记需要包含**模块信息**：

```markdown
## 用户登录需求
**[ID: RD-User-REQ-001]** **[Module: User]**

系统需支持用户通过 OAuth2 登录。
```

**标记格式**：
- `[ID: RD-{Module}-REQ-{Number}]` - 需求 ID 包含模块名
- `[Module: {ModuleName}]` - 明确模块归属
- `[Implements: PRD-REQ-User-REQ-001]` - 跨模块引用

**示例依赖链（大项目）**：
```
RD-User-REQ-001 (用户模块需求)
  └─ PRD-User-FEAT-001 (用户模块产品功能)
      └─ DESIGN-User-API-001 (用户模块 API 设计)
          └─ CODE-User-API-001 (用户模块代码)
```

---

## **五、功能需求 (Functional Requirements)**

### **4.1 提示词模板 (Prompt Templates)**

#### **FR-1.1 RD 阶段提示词**

**[ID: PRD-FR-1.1]**

需要提供以下提示词模板：

| 提示词 | 用途 | 输入 | 输出 |
| :---- | :---- | :---- | :---- |
| **rd-generator.md** | 生成或修改需求文档 | 用户故事、业务需求（或现有 RD.md） | RD.md（包含 `[ID: RD-XXX]` 标记） |
| **rd-reviewer.md** | 评审需求文档 | RD.md | 评审报告（问题列表、建议） |

**说明**：
- `rd-generator.md` 既能**创建新文档**，也能**修改现有文档**（不需要单独的 reviser）
- 当提供现有 RD.md 时，它会基于输入进行修订
- 当只提供用户故事时，它会创建全新的 RD.md

**提示词模板要求**：
- 清晰的角色定义（"你是一位需求分析师..."）
- 详细的任务指令
- 输出格式规范（包含可追溯性标记）
- 验收标准

#### **FR-1.2 PRD 阶段提示词**

**[ID: PRD-FR-1.2]**

| 提示词 | 用途 | 输入 | 输出 |
| :---- | :---- | :---- | :---- |
| **prd-generator.md** | 生成或修改产品文档 | RD.md（或 RD.md + 现有 PRD.md） | PRD.md（包含 `[ID: PRD-XXX]` 和 `[Implements: PRD-REQ-XXX]`） |
| **prd-reviewer.md** | 评审产品文档 | PRD.md + RD.md | 评审报告 |

#### **FR-1.3 Design Document 阶段提示词**

**[ID: PRD-FR-1.3]**

| 提示词 | 用途 | 输入 | 输出 |
| :---- | :---- | :---- | :---- |
| **design-generator.md** | 生成或修改设计文档 | PRD.md + RD.md（或 + 现有 Design Document） | Design Document（包含 `[ID: DESIGN-XXX]` 和 `[Designs-for: PRD-XXX]`） |
| **design-reviewer.md** | 评审设计文档 | Design Document + PRD.md | 评审报告 |

#### **FR-1.4 Test Plan 阶段提示词**

**[ID: PRD-FR-1.4]**

| 提示词 | 用途 | 输入 | 输出 |
| :---- | :---- | :---- | :---- |
| **test-plan-generator.md** | 生成或修改测试计划 | Design Document + PRD.md（或 + 现有 Test Plan） | Test Plan（包含 `[ID: TEST-XXX]` 和 `[Tests-for: DESIGN-XXX]`） |
| **test-plan-reviewer.md** | 评审测试计划 | Test Plan + Design Document | 评审报告 |

#### **FR-1.5 Code 阶段提示词**

**[ID: PRD-FR-1.5]**

| 提示词 | 用途 | 输入 | 输出 |
| :---- | :---- | :---- | :---- |
| **code-generator.md** | 生成或修改代码 | Design Document + PRD.md（或 + 现有代码） | 代码（包含 `[ID: CODE-XXX]` 注释） |
| **code-reviewer.md** | 评审代码 | 代码 + Design Document | 评审报告 |

#### **FR-1.6 一致性检查提示词**

**[ID: PRD-FR-1.6]**

| 提示词 | 用途 | 输入 | 输出 |
| :---- | :---- | :---- | :---- |
| **consistency-checker.md** | 检查 RD/PRD/Design Document/Code 一致性 | 依赖链涉及的文档和代码 | 不一致报告 |
| **impact-analyzer.md** | 分析变更影响 | 变更文件 + 依赖图 | 受影响的下游节点列表 |

---

### **4.2 工作流程文档 (Workflow Documentation)**

#### **FR-2.1 RD 工作流程**

**[ID: PRD-FR-2.1]**

提供 `workflows/rd-workflow.md`，包含：

1. **准备阶段**：收集用户故事、业务需求
2. **生成阶段**：
   - 打开 Claude Code
   - 加载 `prompts/rd-generator.md`
   - 提供输入（用户故事）
   - 生成 RD.md
3. **评审阶段**：
   - 打开新的 Claude Code 窗口（避免自我评审偏差）
   - 加载 `prompts/rd-reviewer.md`
   - 提供 RD.md
   - 生成评审报告
4. **修订阶段**：
   - 根据评审报告修订 RD.md
5. **验收标准**：
   - 所有需求都有 `[ID: RD-XXX-YYY]` 标记
   - 评审报告无严重问题

#### **FR-2.2 PRD/DD/TD/Code 工作流程**

**[ID: PRD-FR-2.2]**

类似 RD 工作流程，提供：
- `workflows/prd-workflow.md`
- `workflows/design-workflow.md`
- `workflows/test-plan-workflow.md`
- `workflows/code-workflow.md`

#### **FR-2.3 影响分析工作流程**

**[ID: PRD-FR-2.3]**

提供 `workflows/impact-analysis.md`，包含：

1. 修改某个文档（如 RD.md）
2. 运行辅助脚本：`python scripts/analyze-impact.py --changed=docs/RD.md`
3. 脚本输出受影响的下游节点（PRD、DD、Code）
4. 人类开发者根据输出，决定是否重新生成下游文档

#### **FR-2.4 一致性检查工作流程**

**[ID: PRD-FR-2.4]**

提供 `workflows/consistency-check.md`，包含：

1. 运行辅助脚本：`python scripts/check-consistency.py --scope=RD-REQ-005`
2. 脚本构建依赖链涉及的上下文（< 5K tokens）
3. 打开 Claude Code，加载 `prompts/consistency-checker.md`
4. 提供依赖链上下文
5. Claude Code 输出不一致报告
6. 人类开发者根据报告修复不一致

---

### **4.3 辅助脚本 (Helper Scripts)**

#### **FR-3.1 标记解析脚本**

**[ID: PRD-FR-3.1]**

提供 `scripts/parse-tags.py`，功能：

- 扫描项目中的所有 `.md` 和代码文件
- 提取所有可追溯性标记（`[ID: XXX]`, `[Implements: XXX]` 等）
- 输出结构化数据（JSON 格式）

**示例**：
```bash
python scripts/parse-tags.py --dir=. --output=.specgov/tags.json
```

**输出**：
```json
{
  "tags": [
    {
      "type": "ID",
      "id": "RD-REQ-005",
      "file": "docs/RD.md",
      "line": 42
    },
    {
      "type": "Implements",
      "source": "PRD-FEAT-012",
      "target": "RD-REQ-005",
      "file": "docs/PRD.md",
      "line": 128
    }
  ]
}
```

#### **FR-3.2 依赖图构建脚本**

**[ID: PRD-FR-3.2]**

提供 `scripts/build-dependency-graph.py`，功能：

- 读取 `parse-tags.py` 输出的标记数据
- 构建依赖图（有向图）
- 输出依赖图（JSON 格式）

**示例**：
```bash
python scripts/build-dependency-graph.py \
  --input=.specgov/tags.json \
  --output=.specgov/dependency-graph.json
```

**输出**：
```json
{
  "nodes": [
    {"id": "RD-REQ-005", "type": "requirement", "file": "docs/RD.md", "line": 42},
    {"id": "PRD-FEAT-012", "type": "feature", "file": "docs/PRD.md", "line": 128}
  ],
  "edges": [
    {"from": "PRD-FEAT-012", "to": "RD-REQ-005", "type": "implements"}
  ]
}
```

#### **FR-3.3 影响分析脚本**

**[ID: PRD-FR-3.3]**

提供 `scripts/analyze-impact.py`，功能：

- 读取依赖图
- 基于 Git diff 识别变更的文件
- 查询依赖图，找到下游节点
- 输出受影响的文档和代码

**示例**：
```bash
python scripts/analyze-impact.py --changed=docs/RD.md
```

**输出**：
```
受影响的文档：
  - PRD 第 3.2 节（用户登录功能）docs/PRD.md:128
  - DD 第 4.1 节（认证服务设计）docs/DD.md:234

受影响的代码：
  - src/auth/auth.service.ts:89
```

#### **FR-3.4 一致性检查脚本**

**[ID: PRD-FR-3.4]**

提供 `scripts/check-consistency.py`，功能：

- 读取依赖图
- 定位指定 ID 的依赖链
- 提取依赖链涉及的文档和代码片段
- 构建上下文（< 5K tokens）
- 输出上下文文件，供 Claude Code 使用

**示例**：
```bash
python scripts/check-consistency.py --scope=RD-REQ-005 --output=context.md
```

**输出**：生成 `context.md`，包含：
- RD-REQ-005 的内容
- PRD-FEAT-012 的内容（实现了 RD-REQ-005）
- DESIGN-API-008 的内容（设计了 PRD-FEAT-012）
- CODE-API-008 的代码片段（实现了 DESIGN-API-008）

人类开发者打开 Claude Code，加载 `prompts/consistency-checker.md`，提供 `context.md`，Claude Code 检查一致性。

---

### **4.4 文档模板 (Document Templates)**

#### **FR-4.1 提供标准文档模板**

**[ID: PRD-FR-4.1]**

提供以下模板：

| 模板文件 | 用途 |
| :---- | :---- |
| `templates/RD-template.md` | RD 文档结构模板 |
| `templates/PRD-template.md` | PRD 文档结构模板 |
| `templates/Design-Document-template.md` | Design Document 结构模板 |
| `templates/Test-Plan-template.md` | Test Plan 结构模板 |

**模板内容**：
- 文档结构（章节标题）
- 可追溯性标记位置示例
- 填写说明

---

### **4.5 任务管理文档 (Task Management Documents)**

#### **FR-5.1 两层任务管理**

**[ID: PRD-FR-5.1]**

提供两层任务管理文档：

**1. 项目经理层（High-level）**

文件：`.specgov/tasks/project-manager.md`

内容：
- Epic 列表（高层级任务）
- 每个 Epic 的状态、进度、负责角色
- 整体项目进度概览

**2. 角色层（Low-level）**

文件：
- `.specgov/tasks/rd-analyst.md` - 需求分析师任务
- `.specgov/tasks/product-manager.md` - 产品经理任务
- `.specgov/tasks/architect.md` - 架构师任务
- `.specgov/tasks/test-manager.md` - 测试经理任务
- `.specgov/tasks/developer.md` - 开发工程师任务

内容：
- 当前任务列表
- 任务状态（待办、进行中、已完成）
- 关联的 Epic
- 验收标准

#### **FR-5.2 任务工作流程**

**[ID: PRD-FR-5.2]**

**步骤 1：项目经理下达任务**

1. 使用者切换到**项目经理角色**
2. 在 `.specgov/tasks/project-manager.md` 创建 High-level 任务（Epic）
3. 示例：
   ```markdown
   ## Epic 1: OAuth2 登录功能
   - 状态：未开始
   - 优先级：高
   - 预计时间：5 天
   - 交付物：RD.md, PRD.md, Design-Document.md, Test-Plan.md, 代码
   - 子任务：
     - [ ] 1.1 需求分析（需求分析师）
     - [ ] 1.2 产品设计（产品经理）
     - [ ] 1.3 架构设计（架构师）
     - [ ] 1.4 测试设计（测试经理）
     - [ ] 1.5 代码实现（开发工程师）
   ```

**步骤 2：角色执行子任务**

1. 使用者切换到**具体角色**（如需求分析师）
2. 查看 `.specgov/tasks/rd-analyst.md`
3. 执行分配的任务
4. 完成后更新自己的任务文档：
   ```markdown
   ## 当前任务
   - [x] Task 1.1: 生成 RD（关联 Epic 1）
   - [x] Task 1.2: 评审 RD
   - [x] Task 1.3: 修订 RD
   ```

**步骤 3：完成后更新项目经理任务**

1. 角色完成所有子任务后
2. 切换回**项目经理角色**
3. 更新 `.specgov/tasks/project-manager.md`：
   ```markdown
   ## Epic 1: OAuth2 登录功能
   - 状态：进行中
   - 进度：20% (1/5 完成)
   - 子任务：
     - [x] 1.1 需求分析（需求分析师）✅ 已完成
     - [ ] 1.2 产品设计（产品经理）← 下一步
     - [ ] 1.3 架构设计（架构师）
     - [ ] 1.4 测试设计（测试经理）
     - [ ] 1.5 代码实现（开发工程师）
   ```

#### **FR-5.3 任务文档模板**

**[ID: PRD-FR-5.3]**

提供以下模板：

| 模板文件 | 用途 |
| :---- | :---- |
| `templates/project-manager-tasks.md` | 项目经理任务文档模板 |
| `templates/role-tasks.md` | 角色任务文档模板 |

---

### **4.6 示例项目 (Example Projects)**

#### **FR-6.1 提供完整示例**

**[ID: PRD-FR-6.1]**

提供 `examples/oauth2-login/`，包含：

- `docs/RD.md`：示例需求文档（OAuth2 登录）
- `docs/PRD.md`：示例产品文档
- `docs/Design-Document.md`：示例设计文档
- `docs/Test-Plan.md`：示例测试计划
- `src/auth.controller.ts`：示例代码
- `.specgov/dependency-graph.json`：示例依赖图
- `.specgov/tasks/project-manager.md`：示例项目经理任务文档
- `.specgov/tasks/rd-analyst.md`：示例需求分析师任务文档

人类开发者可以参考这个示例，理解如何使用 SpecGovernor。

---

## **五、可追溯性标记规范 (Traceability Tag Specification)**

### **5.1 标记类型**

**[ID: PRD-TRACE-001]**

| 标记 | 格式 | 说明 | 示例 |
| :---- | :---- | :---- | :---- |
| **ID** | `[ID: PREFIX-XXX-YYY]` | 定义当前内容的唯一标识 | `[ID: PRD-REQ-005]` |
| **Implements** | `[Implements: ID]` | 声明实现了上游需求 | `[Implements: PRD-REQ-REQ-005]` |
| **Designs-for** | `[Designs-for: ID]` | 声明是某功能的设计 | `[Designs-for: PRD-FEAT-012]` |
| **Tests-for** | `[Tests-for: ID]` | 声明是某设计的测试 | `[Tests-for: DD-API-008]` |

### **5.2 ID 前缀规范**

**[ID: PRD-TRACE-002]**

| 阶段 | 前缀 | 示例 |
| :---- | :---- | :---- |
| RD | `RD-REQ-`, `RD-GOAL-` | RD-REQ-001, RD-GOAL-001 |
| PRD | `PRD-FEAT-`, `PRD-US-` | PRD-FEAT-012, PRD-US-003 |
| Design Document | `DESIGN-API-`, `DESIGN-DB-`, `DESIGN-ARCH-` | DESIGN-API-008, DESIGN-DB-005 |
| Test Plan | `TEST-CASE-`, `TEST-PERF-` | TEST-CASE-015, TEST-PERF-003 |
| Code | `CODE-API-`, `CODE-SERVICE-` | CODE-API-008 |

### **5.3 嵌入位置**

**[ID: PRD-TRACE-003]**

**Markdown 文档**：
```markdown
## OAuth2 登录需求
**[ID: PRD-REQ-005]**

系统需支持 OAuth2 登录流程。
```

**代码文件**：
```typescript
// [ID: CODE-API-008] [Implements: DESIGN-API-008]
export class AuthController {
    async oauth2Callback(req: Request, res: Response) {
        // ...
    }
}
```

---

## **六、目录结构 (Directory Structure)**

**[ID: PRD-STRUCTURE-001]**

```
SpecGovernor/
├── README.md                   # 使用指南
├── prompts/                    # 提示词模板
│   ├── rd-generator.md         # 既能创建也能修改 RD
│   ├── rd-reviewer.md
│   ├── prd-generator.md        # 既能创建也能修改 PRD
│   ├── prd-reviewer.md
│   ├── design-generator.md     # 既能创建也能修改 Design Document
│   ├── design-reviewer.md
│   ├── test-plan-generator.md  # 既能创建也能修改 Test Plan
│   ├── test-plan-reviewer.md
│   ├── code-generator.md       # 既能创建也能修改代码
│   ├── code-reviewer.md
│   ├── consistency-checker.md
│   └── impact-analyzer.md
├── workflows/                  # 工作流程文档
│   ├── rd-workflow.md
│   ├── prd-workflow.md
│   ├── design-workflow.md
│   ├── test-plan-workflow.md
│   ├── code-workflow.md
│   ├── impact-analysis.md
│   └── consistency-check.md
├── scripts/                    # 辅助脚本
│   ├── parse-tags.py
│   ├── build-dependency-graph.py
│   ├── analyze-impact.py
│   └── check-consistency.py
├── templates/                  # 文档模板
│   ├── RD-template.md
│   ├── PRD-template.md
│   ├── Design-Document-template.md
│   ├── Test-Plan-template.md
│   ├── project-manager-tasks.md  # 项目经理任务模板
│   └── role-tasks.md              # 角色任务模板
├── examples/                   # 示例项目
│   └── oauth2-login/
│       ├── docs/
│       │   ├── RD.md
│       │   ├── PRD.md
│       │   ├── Design-Document.md
│       │   └── Test-Plan.md
│       ├── src/
│       │   └── auth.controller.ts
│       └── .specgov/
│           ├── dependency-graph.json
│           └── tasks/
│               ├── project-manager.md
│               ├── rd-analyst.md
│               ├── product-manager.md
│               ├── architect.md
│               ├── test-manager.md
│               └── developer.md
└── docs/                       # SpecGovernor 自身的设计文档
    ├── RD.md                   # 本文档
    ├── PRD.md
    ├── Design-Document.md
    └── Test-Plan.md
```

---

## **七、非功能需求 (Non-Functional Requirements)**

### **7.1 易用性**

**[ID: PRD-NFR-001]**

- 提示词模板应清晰易懂，人类开发者无需培训即可使用
- 工作流程文档应图文并茂，步骤明确
- 辅助脚本应提供 `--help` 选项，说明用法

### **7.2 可扩展性**

**[ID: PRD-NFR-002]**

- 人类开发者可以自定义提示词模板
- 人类开发者可以扩展辅助脚本

### **7.3 兼容性**

**[ID: PRD-NFR-003]**

- 提示词模板应兼容 Claude Code（主要）
- 辅助脚本应使用 Python 3.8+，无复杂依赖

### **7.4 性能**

**[ID: PRD-NFR-004]**

- `parse-tags.py`：100 万行代码 < 1 分钟
- `analyze-impact.py`：< 10 秒
- `check-consistency.py`：构建上下文 < 5 秒

---

## **八、验收标准 (Acceptance Criteria)**

**[ID: PRD-AC-001]**

| 交付物 | 验收标准 |
| :---- | :---- |
| **提示词模板** | ✅ 覆盖所有阶段（RD/PRD/Design Document/Test Plan/Code）<br>✅ 包含生成和评审模板（generator 既能创建也能修改）<br>✅ 输出包含可追溯性标记 |
| **工作流程文档** | ✅ 清晰的步骤说明<br>✅ 示例截图或命令<br>✅ 验收标准明确 |
| **辅助脚本** | ✅ 运行正常，无报错<br>✅ 性能达标<br>✅ 提供 `--help` |
| **文档模板** | ✅ 结构清晰<br>✅ 标记位置示例 |
| **任务管理文档** | ✅ 项目经理层（High-level）<br>✅ 角色层（Low-level）<br>✅ 任务流程清晰 |
| **示例项目** | ✅ 完整的 RD/PRD/Design Document/Test Plan/Code<br>✅ 可追溯性标记完整<br>✅ 任务文档示例完整 |

---

## **九、使用场景示例 (Usage Scenarios)**

### **9.1 场景 0：项目经理创建 High-level 任务**

**[ID: PRD-SCENARIO-000]**

**步骤**：

1. 使用者切换到**项目经理角色**
2. 打开 `.specgov/tasks/project-manager.md`
3. 创建新的 Epic：
   ```markdown
   # 项目任务进展

   ## Epic 1: OAuth2 登录功能

   **状态**: 未开始
   **优先级**: 高
   **创建时间**: 2025-11-16
   **预计完成**: 2025-11-21（5天）

   **交付物**:
   - [ ] RD.md
   - [ ] PRD.md
   - [ ] Design-Document.md
   - [ ] Test-Plan.md
   - [ ] 代码实现

   **子任务分解**:
   - [ ] 1.1 需求分析（需求分析师）- 预计 1 天
   - [ ] 1.2 产品设计（产品经理）- 预计 1 天
   - [ ] 1.3 架构设计（架构师）- 预计 1 天
   - [ ] 1.4 测试设计（测试经理）- 预计 1 天
   - [ ] 1.5 代码实现（开发工程师）- 预计 1 天

   **当前进度**: 0% (0/5)
   ```

4. 提交到 Git：`git add .specgov/tasks/project-manager.md && git commit -m "Create Epic 1"`

---

### **9.1 场景 1：生成 RD**

**[ID: PRD-SCENARIO-001]**

**步骤**：

1. 使用者切换到**需求分析师角色**
2. 查看 `.specgov/tasks/rd-analyst.md`，看到分配的任务
3. 打开 Claude Code
4. 复制 `prompts/rd-generator.md` 的内容
5. 粘贴到 Claude Code
6. 提供用户故事：
   ```
   用户需要通过 Google 账号登录系统
   ```
7. Claude Code 生成 `RD.md`：
   ```markdown
   ## OAuth2 登录需求
   **[ID: PRD-REQ-005]**

   系统需支持通过 Google OAuth2 进行用户登录。
   ```

8. 完成后，更新 `.specgov/tasks/rd-analyst.md`：
   ```markdown
   ## 当前任务
   - [x] Task 1.1: 生成 RD（关联 Epic 1）✅ 完成
   - [ ] Task 1.2: 评审 RD
   ```

9. 切换回**项目经理角色**，更新 `.specgov/tasks/project-manager.md`：
    ```markdown
    **子任务分解**:
    - [x] 1.1 需求分析（需求分析师）✅ 完成 - RD.md 已生成
    - [ ] 1.2 产品设计（产品经理）← 下一步

    **当前进度**: 20% (1/5)
    ```

### **9.2 场景 2：评审 RD**

**[ID: PRD-SCENARIO-002]**

**步骤**：

1. 打开**新的** Claude Code 窗口（避免自我评审偏差）
2. 复制 `prompts/rd-reviewer.md`
3. 提供 `RD.md` 内容
4. Claude Code 生成评审报告：
   ```
   **评审报告**

   问题：
   1. [严重] RD-REQ-005 缺少安全要求（如 CSRF 防护）
   2. [建议] 建议明确支持的 OAuth2 Provider 列表
   ```

### **9.3 场景 3：影响分析**

**[ID: PRD-SCENARIO-003]**

**步骤**：

1. 人类开发者修改 `RD.md`
2. 运行脚本：
   ```bash
   python scripts/analyze-impact.py --changed=docs/RD.md
   ```
3. 脚本输出：
   ```
   受影响的文档：
     - PRD-FEAT-012 (docs/PRD.md:128)
     - DESIGN-API-008 (docs/Design-Document.md:234)
   ```
4. 人类开发者决定重新生成 PRD

### **9.4 场景 4：一致性检查**

**[ID: PRD-SCENARIO-004]**

**步骤**：

1. 运行脚本：
   ```bash
   python scripts/check-consistency.py --scope=RD-REQ-005 --output=context.md
   ```
2. 脚本生成 `context.md`（包含依赖链的所有内容）
3. 打开 Claude Code
4. 复制 `prompts/consistency-checker.md`
5. 提供 `context.md` 内容
6. Claude Code 检查一致性，输出报告：
   ```
   **不一致检查报告**

   发现 1 处不一致：
   - Design Document 设计的 API 是 POST /auth/callback
   - 代码实现是 PUT /auth/callback
   ```

---

## **十、总结与下一步 (Summary & Next Steps)**

### **10.1 核心价值**

**[ID: PRD-SUMMARY-001]**

SpecGovernor 提供：

1. ✅ **标准化的提示词模板**，引导 Claude Code 生成规范文档/代码（generator 既能创建也能修改）
2. ✅ **清晰的工作流程**，指导人类开发者进行规范化开发
3. ✅ **可追溯性机制**，建立 RD → PRD → Design Document → Test Plan → Code 的追溯链
4. ✅ **两层任务管理**，项目经理视角（Epic）+ 角色视角（Task），跟踪整体进度和具体任务
5. ✅ **轻量级辅助脚本**，自动化解析、分析任务
6. ✅ **易于使用**，无需安装，直接配合 Claude Code 使用

### **10.2 下一步工作**

**[ID: PRD-NEXT-001]**

1. ⏳ **编写 PRD（产品需求文档）**：详细描述每个提示词模板的功能
2. ⏳ **编写 Design Document（设计文档）**：定义辅助脚本的实现细节
3. ⏳ **编写 Test Plan（测试计划）**：设计如何测试提示词模板和脚本
4. ⏳ **实现提示词模板**：编写所有提示词模板
5. ⏳ **实现辅助脚本**：编写 Python 脚本
6. ⏳ **创建示例项目**：提供完整的示例

---

**需求文档结束 (End of Requirements Document)**


---

# **Part 2: Product Features（产品功能设计）**

> 本部分包含原 PRD.md 的内容，定义产品功能、用户故事、验收标准等。

## **二、User Stories**

### **2.1 Epic 1: Project Initialization**

**[ID: PRD-EPIC-001] [Implements: PRD-REQ-INIT-001]**

> **As** 超级个体开发者
> **I want** 快速搭建 SpecGovernor toolkit 结构
> **So that** 可以开始使用标准化的开发流程

---

#### **US-001.1: Initialize Project Structure**

**[ID: PRD-US-001.1]**

**用户流程：**
```
1. 开发者下载 SpecGovernor toolkit 仓库
2. 运行：python scripts/init_project.py
3. 脚本提示：
   请选择项目规模：
   1. 小项目（< 10 万行代码，单层文档结构）
   2. 大项目（≥ 10 万行代码，双层文档结构）
   您的选择：_

4. 脚本创建目录结构：

小项目 (Small Project):
  .specgov/
    ├── prompts/              # 所有 prompt templates
    ├── workflows/            # 所有 workflow 文档
    ├── tasks/               # 任务跟踪文件
    │   ├── project-manager.md
    │   ├── rd-analyst.md
    │   ├── product-manager.md
    │   ├── architect.md
    │   └── test-manager.md
    └── project-config.json   # 项目配置

  docs/
    ├── RD.md
    ├── PRD.md
    ├── Design-Document.md
    └── Test-Plan.md

大项目 (Large Project):
  .specgov/
    └── (与小项目相同)

  docs/
    ├── RD/
    │   ├── RD-Overview.md
    │   └── (模块特定的 RD 文件)
    ├── PRD/
    │   ├── PRD-Overview.md
    │   └── (模块特定的 PRD 文件)
    ├── Design-Document/
    │   ├── Design-Overview.md
    │   └── (模块特定的 design 文件)
    └── Test-Plan/
        ├── Test-Overview.md
        └── (模块特定的 test 文件)

5. 脚本输出：
   ✓ SpecGovernor 项目结构创建完成

   📚 下一步：
     1. 查看 .specgov/workflows/workflow-overview.md
     2. 作为 Project Manager，在 .specgov/tasks/project-manager.md 中创建第一个 Epic
     3. 切换到 Requirements Analyst 角色，在 Claude Code 中加载 .specgov/prompts/rd-generator.md
```

**验收标准：**
- ✅ 创建包含所有模板和 workflow 的 `.specgov/` 目录
- ✅ 根据项目规模选择创建相应的文档结构
- ✅ 生成包含项目元数据的 `project-config.json`
- ✅ 输出清晰的下一步指导

---

### **2.2 Epic 2: Using Prompt Templates with Claude Code**

**[ID: PRD-EPIC-002] [Implements: RD-GOAL-001, RD-GOAL-002]**

> **As** 超级个体开发者
> **I want** 使用 prompt templates 配合 Claude Code 生成标准化文档
> **So that** 在所有产出物中保持一致性和可追溯性

---

#### **US-002.1: Generate Requirements Document (RD)**

**[ID: PRD-US-002.1]**

**用户流程：**
```
1. 开发者切换到 "Requirements Analyst" 角色视角

2. 打开 .specgov/tasks/rd-analyst.md 查看分配的任务

3. 打开 Claude Code

4. 加载 prompt template .specgov/prompts/rd-generator.md

5. 提供上下文：
   - 业务需求
   - 用户故事
   - 现有文档（如果是修改）

6. Claude Code（使用 prompt template）：
   - 生成结构正确的 RD.md
   - 嵌入可追溯性标记：[ID: RD-REQ-XXX]
   - 使用 [Decomposes: XXX] 表示层级需求
   - 遵循 markdown 格式标准

7. 输出保存到 docs/RD.md

8. 开发者更新 .specgov/tasks/rd-analyst.md：
   - 标记任务为完成
   - 添加备注

9. 开发者切换到 "Project Manager" 角色

10. 更新 .specgov/tasks/project-manager.md：
    - 更新 Epic 进度（例如：20% -> 40%）
    - 记录 RD 生成子任务的完成情况
```

**生成的 RD 示例：**
```markdown
## 1. User Authentication Requirements
**[ID: RD-AUTH-001]**

本节定义所有认证相关的需求。

### 1.1 OAuth2 Login
**[ID: RD-REQ-005] [Decomposes: RD-AUTH-001]**

系统必须支持通过 OAuth2 协议进行用户登录，包括：
- Google OAuth2
- GitHub OAuth2
- Microsoft OAuth2

...
```

**验收标准：**
- ✅ Prompt template (rd-generator.md) 指导 Claude Code 生成正确的 RD 结构
- ✅ 生成的 RD 包含嵌入式可追溯性标记
- ✅ 模板同时处理创建和修改场景
- ✅ 遵循 RD.md 中的命名规范
- ✅ 用户更新两个任务文档（角色特定文档和 project manager 文档）

---

#### **US-002.2: Review Requirements Document (RD)**

**[ID: PRD-US-002.2]**

**用户流程：**
```
1. 开发者保持 "Requirements Analyst" 角色或切换到不同视角进行独立审查

2. 打开 Claude Code

3. 加载审查 prompt template .specgov/prompts/rd-reviewer.md

4. 提供生成的 docs/RD.md 供审查

5. Claude Code（使用 reviewer template）：
   - 检查完整性
   - 验证可追溯性标记（所有需求都有 [ID: XXX]）
   - 检查 [Decomposes: XXX] 引用是否有效
   - 识别缺失的需求
   - 建议改进

6. 输出结构化的审查报告（JSON 或 Markdown）

7. 开发者使用 rd-generator.md 再次处理审查反馈（修改模式）
```

**审查报告示例：**
```markdown
# RD Review Report

## Summary
✓ 整体质量：良好
⚠️  发现 2 条建议，0 个关键问题

## Issues

### 1. [Suggestion] RD-REQ-005 (OAuth2 Login)
- 位置：Section 1.1
- 问题：缺少错误处理需求
- 建议：添加登录失败、token 过期场景的需求

### 2. [Suggestion] Traceability Tags
- 位置：Section 2.3
- 问题：缺少 [ID: XXX] 标记
- 建议：为 "Data Security Requirements" 添加标记

## Traceability Check
✓ 所有主要需求都有 [ID: XXX] 标记
✓ 所有 [Decomposes: XXX] 引用都指向现有的父 ID
```

**验收标准：**
- ✅ Reviewer template (rd-reviewer.md) 指导 Claude Code 检查完整性
- ✅ 验证可追溯性标记的正确性
- ✅ 输出结构化的反馈
- ✅ 区分问题严重程度（critical/warning/suggestion）

---

#### **US-002.3: Generate Product Requirements Document (PRD)**

**[ID: PRD-US-002.3]**

**用户流程：**
```
1. 开发者切换到 "Product Manager" 角色

2. 打开 .specgov/tasks/product-manager.md 查看分配的任务

3. 打开 Claude Code

4. 加载 prompt template .specgov/prompts/prd-generator.md

5. 提供上下文：
   - docs/RD.md（上一步生成的）
   - 产品愿景
   - 用户画像

6. Claude Code 生成 PRD.md，包含：
   - 产品功能：[ID: PRD-FEAT-XXX]
   - 用户故事：[ID: PRD-US-XXX]
   - 与 RD 的可追溯性：[Implements: PRD-REQ-REQ-XXX]

7. 输出保存到 docs/PRD.md

8. 更新 .specgov/tasks/product-manager.md 和 project-manager.md
```

**生成的 PRD 示例：**
```markdown
## 2. User Authentication Features

### 2.1 OAuth2 Login Feature
**[ID: PRD-FEAT-012] [Implements: PRD-REQ-REQ-005]**

#### User Story
> **As** 用户
> **I want** 使用我的 Google/GitHub/Microsoft 账号登录
> **So that** 无需创建新密码

#### Acceptance Criteria
- ✅ 支持 Google OAuth2 登录
- ✅ 支持 GitHub OAuth2 登录
- ✅ 支持 Microsoft OAuth2 登录
- ✅ 优雅地处理登录失败
- ✅ 处理 token 过期
```

**验收标准：**
- ✅ PRD generator template 创建正确的产品功能
- ✅ 嵌入链接到需求的 [Implements: PRD-REQ-XXX] 标记
- ✅ 遵循产品文档最佳实践
- ✅ 模板可以创建和修改 PRD

---

#### **US-002.4: Generate Design Document**

**[ID: PRD-US-002.4]**

**用户流程：**
```
1. 开发者切换到 "Architect" 角色

2. 在 Claude Code 中加载 .specgov/prompts/design-generator.md

3. 提供：
   - docs/RD.md
   - docs/PRD.md
   - 技术约束

4. Claude Code 生成 Design-Document.md，包含：
   - 架构设计：[ID: DESIGN-ARCH-XXX]
   - API 设计：[ID: DESIGN-API-XXX]
   - 数据库设计：[ID: DESIGN-DB-XXX]
   - 可追溯性：[Designs-for: PRD-FEAT-XXX]

5. 输出保存到 docs/Design-Document.md

6. 更新任务文档
```

**生成的 Design 示例：**
```markdown
## 3. API Design

### 3.1 OAuth2 Callback API
**[ID: DESIGN-API-008] [Designs-for: PRD-FEAT-012]**

**Endpoint**: POST /auth/oauth2/callback

**Request:**
```json
{
  "provider": "google",
  "code": "auth_code_from_provider",
  "redirect_uri": "https://app.example.com/callback"
}
```

**Response:**
```json
{
  "access_token": "...",
  "refresh_token": "...",
  "expires_in": 3600
}
```
```

**验收标准：**
- ✅ Design generator template 创建技术规范
- ✅ 嵌入 [Designs-for: PRD-XXX] 标记
- ✅ 使用 "Design Document" 术语（而非 "DD"）
- ✅ 处理创建和修改

---

#### **US-002.5: Generate Test Plan**

**[ID: PRD-US-002.5]**

**用户流程：**
```
1. 开发者切换到 "Test Manager" 角色

2. 在 Claude Code 中加载 .specgov/prompts/test-plan-generator.md

3. 提供：
   - docs/Design-Document.md
   - docs/PRD.md

4. Claude Code 生成 Test-Plan.md，包含：
   - 测试用例：[ID: TEST-CASE-XXX]
   - 可追溯性：[Tests-for: DESIGN-API-XXX]
   - 测试策略、覆盖率目标

5. 输出保存到 docs/Test-Plan.md

6. 更新任务文档
```

**生成的 Test Plan 示例：**
```markdown
## 5. API Test Cases

### 5.1 OAuth2 Callback API Tests
**[ID: TEST-CASE-015] [Tests-for: DESIGN-API-008]**

#### Test Case: Successful Google OAuth2 Login
**[ID: TEST-CASE-015-001]**

**前置条件：**
- 用户拥有有效的 Google 账户
- 应用已在 Google OAuth2 注册

**步骤：**
1. 发送 POST /auth/oauth2/callback，包含有效的 Google auth code
2. 验证响应状态为 200
3. 验证 access_token 存在
4. 验证 refresh_token 存在

**预期结果：**
- ✅ Status: 200 OK
- ✅ access_token: 有效的 JWT
- ✅ expires_in: 3600 秒
```

**验收标准：**
- ✅ Test Plan generator template 创建全面的测试用例
- ✅ 嵌入 [Tests-for: DESIGN-XXX] 标记
- ✅ 使用 "Test Plan" 术语（而非 "TD"）
- ✅ 处理创建和修改

---

### **2.3 Epic 3: Using Helper Scripts**

**[ID: PRD-EPIC-003] [Implements: PRD-REQ-GOAL-004]**

> **As** 超级个体开发者
> **I want** 使用 helper scripts 解析标记、构建图和分析影响
> **So that** 可以维护可追溯性而无需手动跟踪

---

#### **US-003.1: Parse Traceability Tags**

**[ID: PRD-US-003.1]**

**用户流程：**
```
1. 开发者运行：
   python scripts/parse_tags.py

2. 脚本扫描 docs/ 和 src/ 目录中的所有文件

3. 查找所有可追溯性标记：
   - [ID: XXX]
   - [Implements: XXX]
   - [Decomposes: XXX]
   - [Designs-for: XXX]
   - [Tests-for: XXX]

4. 将解析的标记输出到：
   .specgov/index/tags.json

5. 输出示例：
{
  "tags": [
    {
      "id": "RD-REQ-005",
      "type": "requirement",
      "file": "docs/RD.md",
      "line": 42,
      "decomposes": "RD-AUTH-001"
    },
    {
      "id": "PRD-FEAT-012",
      "type": "feature",
      "file": "docs/PRD.md",
      "line": 128,
      "implements": "RD-REQ-005"
    },
    ...
  ]
}

6. 控制台输出：
   ✓ 扫描了 125 个文件
   ✓ 发现 45 个 [ID: XXX] 标记
   ✓ 发现 38 个 [Implements: XXX] 标记
   ✓ 发现 12 个 [Decomposes: XXX] 标记
   ✓ 保存到 .specgov/index/tags.json

   ⏱️  时间：8 秒
   💰 成本：$0（本地解析）
```

**验收标准：**
- ✅ 扫描所有 Markdown 和代码文件
- ✅ 使用正则表达式解析所有标记类型
- ✅ 输出结构化 JSON
- ✅ 性能：100K+ 行代码 < 1 分钟
- ✅ 零 AI 成本（本地计算）

---

#### **US-003.2: Build Dependency Graph**

**[ID: PRD-US-003.2]**

**用户流程：**
```
1. 开发者运行：
   python scripts/build_graph.py

2. 脚本读取 .specgov/index/tags.json

3. 构建依赖图：
   - 节点：所有 [ID: XXX] 标记
   - 边：[Implements: XXX], [Decomposes: XXX] 等

4. 检测循环依赖

5. 将图输出到：
   .specgov/index/dependency-graph.json

6. 输出示例：
{
  "nodes": [
    {"id": "RD-REQ-005", "type": "requirement", "location": "docs/RD.md#L42"},
    {"id": "PRD-FEAT-012", "type": "feature", "location": "docs/PRD.md#L128"},
    {"id": "DESIGN-API-008", "type": "api_design", "location": "docs/Design-Document.md#L234"}
  ],
  "edges": [
    {"from": "PRD-FEAT-012", "to": "RD-REQ-005", "relation": "implements"},
    {"from": "DESIGN-API-008", "to": "PRD-FEAT-012", "relation": "designs-for"}
  ]
}

7. 控制台输出：
   ✓ 创建了 45 个节点
   ✓ 创建了 50 条边
   ✓ 检测到 0 个循环依赖
   ✓ 保存到 .specgov/index/dependency-graph.json

   📊 统计：
     - Requirements (RD): 15
     - Features (PRD): 12
     - Designs (Design Document): 10
     - Tests (Test Plan): 5
     - Code: 3
```

**验收标准：**
- ✅ 从解析的标记构建图
- ✅ 检测循环依赖
- ✅ 输出 JSON 格式
- ✅ 零 AI 成本

---

#### **US-003.3: Analyze Impact of Changes**

**[ID: PRD-US-003.3]**

**用户流程：**
```
1. 开发者修改 docs/RD.md

2. 运行：
   python scripts/impact_analysis.py --changed=docs/RD.md

3. 脚本：
   - 使用 git diff 识别变更的行
   - 解析变更部分的标记
   - 查询依赖图以找到下游节点

4. 输出影响报告：

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Impact Analysis Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

变更节点 (2):
  • RD-REQ-005 (requirement) at docs/RD.md#L42
  • RD-REQ-007 (requirement) at docs/RD.md#L85

受影响文档 (5):
  ⚠️  PRD-FEAT-012 (feature) at docs/PRD.md#L128
      原因：Implements RD-REQ-005

  ⚠️  DESIGN-API-008 (api_design) at docs/Design-Document.md#L234
      原因：Designs for PRD-FEAT-012

  ⚠️  TEST-CASE-015 (test) at docs/Test-Plan.md#L56
      原因：Tests DESIGN-API-008

  ...

受影响代码 (3):
  ⚠️  CODE-API-008 at src/auth/auth.controller.ts#L89
      原因：Implements DESIGN-API-008

  ...

建议操作：
  1. 审查并更新 PRD-FEAT-012 的 PRD 部分
  2. 审查并更新 DESIGN-API-008 的 Design Document
  3. 更新 Test Plan 中的测试用例

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ 报告保存到 .specgov/reports/impact-2025-11-16.json

⏱️  时间：6 秒
💰 成本：$0（仅图查询）
```

**验收标准：**
- ✅ 使用 git diff 检测变更
- ✅ 高效查询依赖图
- ✅ 输出清晰的影响报告
- ✅ 性能：< 10 秒
- ✅ 零 AI 成本

---

#### **US-003.4: Check Consistency with Context Preparation**

**[ID: PRD-US-003.4] [Implements: RD-FR-3.4]**

**用户流程：**
```
1. 开发者想要检查某个需求的一致性（例如 RD-REQ-005）

2. 运行：
   python scripts/check-consistency.py --scope=RD-REQ-005 --output=context.md

3. 脚本：
   - 读取 .specgov/index/dependency-graph.json
   - 定位 RD-REQ-005 的完整依赖链
   - 提取依赖链上所有相关内容：
     * RD-REQ-005 的原始需求描述
     * PRD-FEAT-012 的产品功能（如果实现了 RD-REQ-005）
     * DESIGN-API-008 的设计（如果为 PRD-FEAT-012 设计）
     * CODE-API-008 的代码片段（如果实现了 DESIGN-API-008）
   - 构建上下文文件，确保总 tokens < 5K

4. 输出示例 context.md：

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Consistency Check Context for RD-REQ-005
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 1. Requirement (RD-REQ-005)
**Source**: docs/RD.md#L42

### 1.1 OAuth2 Login Support
**[ID: RD-REQ-005] [Decomposes: RD-AUTH-001]**

系统必须支持通过 OAuth2 协议进行用户身份验证。

**支持的提供商：**
- Google OAuth2
- GitHub OAuth2
- Microsoft OAuth2

**验收标准：**
- ✅ 用户可以使用任何支持的 OAuth2 提供商登录
- ✅ 系统获取用户个人资料信息（姓名、邮箱、头像）
- ✅ 系统优雅地处理登录失败
- ✅ 系统处理 token 过期并刷新 token

---

## 2. Product Feature (PRD-FEAT-012)
**Source**: docs/PRD.md#L128
**[Implements: PRD-REQ-REQ-005]**

### 2.1 OAuth2 Social Login
**[ID: PRD-FEAT-012] [Implements: PRD-REQ-REQ-005]**

使用户能够使用其现有社交媒体账户登录。

#### User Story
> **As** 新用户
> **I want** 使用我的 Google/GitHub/Microsoft 账户登录
> **So that** 我不需要创建和记住另一个密码

#### Acceptance Criteria
- ✅ 为每个支持的 OAuth2 提供商显示登录按钮
- ✅ 点击按钮重定向到提供商的 OAuth2 授权页面
- ✅ 授权后，用户被重定向回来并登录
- ✅ 用户个人资料信息显示在应用中
- ✅ 如果登录失败，用户看到清晰的错误消息

---

## 3. API Design (DESIGN-API-008)
**Source**: docs/Design-Document.md#L234
**[Designs-for: PRD-FEAT-012]**

### 2.1 OAuth2 Callback Endpoint
**[ID: DESIGN-API-008] [Designs-for: PRD-FEAT-012]**

**Endpoint**: POST /auth/oauth2/callback

**Request:**
```json
{
  "provider": "google" | "github" | "microsoft",
  "code": "authorization_code_from_provider",
  "redirect_uri": "https://app.example.com/callback"
}
```

**Response (Success):**
```json
{
  "access_token": "eyJhbGc...",
  "refresh_token": "def50200...",
  "expires_in": 3600,
  "user": {
    "id": "user-uuid",
    "email": "user@example.com",
    "name": "John Doe"
  }
}
```

---

## 4. Code Implementation (CODE-API-008)
**Source**: src/auth/auth.controller.ts#L89
**[Implements: DESIGN-API-008]**

```typescript
// [ID: CODE-API-008] [Implements: DESIGN-API-008]
export class AuthController {
    async oauth2Callback(req: Request, res: Response) {
        const { provider, code, redirect_uri } = req.body;

        // Validate provider
        if (!['google', 'github', 'microsoft'].includes(provider)) {
            return res.status(400).json({ error: 'invalid_provider' });
        }

        // Exchange code for access token
        const tokens = await this.oauth2Service.exchangeCode(provider, code);

        // Get user profile
        const profile = await this.oauth2Service.getUserProfile(provider, tokens.access_token);

        // Create or update user
        const user = await this.userService.createOrUpdate(profile);

        // Generate JWT
        const jwt = this.authService.generateJWT(user);

        return res.json({
            access_token: jwt.access_token,
            refresh_token: jwt.refresh_token,
            expires_in: 3600,
            user: {
                id: user.id,
                email: user.email,
                name: user.name
            }
        });
    }
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5. 控制台输出：
   ✓ 收集了 RD-REQ-005 的依赖链
   ✓ 找到 1 个需求、1 个功能、1 个设计、1 个代码实现
   ✓ 生成上下文文件：context.md（约 1.2K tokens）
   ✓ 保存到 context.md

   📚 下一步：
     1. 打开 Claude Code
     2. 加载 .specgov/prompts/consistency-checker.md
     3. 提供 context.md 内容
     4. Claude Code 将检查一致性并输出报告

   ⏱️  时间：3 秒
   💰 成本：$0（本地上下文构建）

6. 开发者打开 Claude Code，使用 consistency-checker.md prompt

7. Claude Code 输出一致性检查报告：

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Consistency Check Report for RD-REQ-005
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Summary
✓ 整体一致性：良好
⚠️  发现 1 个轻微不一致

## Detailed Analysis

### RD-REQ-005 → PRD-FEAT-012
✓ **一致**：PRD 正确实现了 RD 需求
- RD 要求支持 Google/GitHub/Microsoft OAuth2
- PRD 功能包含所有三个提供商

### PRD-FEAT-012 → DESIGN-API-008
✓ **一致**：Design Document 正确设计了 PRD 功能
- PRD 要求显示登录按钮并处理回调
- API 设计了 POST /auth/oauth2/callback 端点

### DESIGN-API-008 → CODE-API-008
⚠️  **轻微不一致**：
- **问题**：设计文档要求处理 token 过期，但代码实现中未找到刷新 token 的逻辑
- **位置**：src/auth/auth.controller.ts#L89
- **建议**：添加 refreshToken() 方法来处理 token 刷新

## Recommendations
1. 在 AuthController 中添加 refreshToken() 方法
2. 更新代码注释以反映完整的错误处理
3. 考虑添加 token 过期的单元测试

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**验收标准：**
- ✅ 从依赖图构建完整的依赖链
- ✅ 提取所有相关文档和代码片段
- ✅ 生成的上下文文件 < 5K tokens
- ✅ 输出清晰的 context.md 文件
- ✅ 提供下一步指导（如何在 Claude Code 中使用）
- ✅ 性能：< 5 秒
- ✅ 零 AI 成本（仅本地文件操作）
- ✅ 与 consistency-checker.md prompt template 配合使用

---

### **2.4 Epic 4: Task Management Workflow**

**[ID: PRD-EPIC-004] [Implements: PRD-REQ-USER-001]**

> **As** 超级个体
> **I want** 管理高层级 Epic 和底层 Task
> **So that** 可以跟踪整体进度和具体工作项

---

#### **US-004.1: Create Epic as Project Manager**

**[ID: PRD-US-004.1]**

**用户流程：**
```
1. 开发者切换到 "Project Manager" 角色

2. 打开 .specgov/tasks/project-manager.md

3. 创建新 Epic：

## Epic 1: OAuth2 Authentication Feature
**状态**: 进行中
**进度**: 0% (0/5 subtasks)
**负责人**: 自己（佩戴不同帽子）

### 子任务：
- [ ] 1.1 需求分析 - Requirements Analyst（估计 1 天）
- [ ] 1.2 产品设计 - Product Manager（估计 1 天）
- [ ] 1.3 技术设计 - Architect（估计 2 天）
- [ ] 1.4 测试计划 - Test Manager（估计 1 天）
- [ ] 1.5 实现 - Developer（估计 3 天）

**总估计**: 8 天

4. 提交变更到 Git
```

**验收标准：**
- ✅ Project Manager 创建包含清晰子任务的 Epic
- ✅ 将子任务分配给不同角色视角
- ✅ 跟踪进度百分比
- ✅ 简单的 Markdown 格式

---

#### **US-004.2: Execute Task as Role**

**[ID: PRD-US-004.2]**

**用户流程：**
```
1. 开发者切换到 "Requirements Analyst" 角色

2. 打开 .specgov/tasks/rd-analyst.md

3. 看到从 Epic 1 分配的任务：
## Task: Epic 1.1 - OAuth2 Authentication Requirements
**分配人**: Project Manager
**截止日期**: Day 1
**状态**: 进行中

### 工作日志：
- [2025-11-16 09:00] 开始任务
- [2025-11-16 10:30] 在 Claude Code 中加载 rd-generator.md prompt
- [2025-11-16 11:45] 为 OAuth2 生成初始 RD.md 部分
- [2025-11-16 14:00] 使用 rd-reviewer.md 审查
- [2025-11-16 15:30] 整合反馈，完成 RD 部分

**状态**: ✅ 已完成

4. 保存 .specgov/tasks/rd-analyst.md

5. 切换到 "Project Manager" 角色

6. 更新 .specgov/tasks/project-manager.md：
## Epic 1: OAuth2 Authentication Feature
**状态**: 进行中
**进度**: 20% (1/5 subtasks)

### 子任务：
- [✅] 1.1 需求分析 - 已完成 2025-11-16
- [ ] 1.2 产品设计 - Product Manager（估计 1 天）
- ...

7. 提交两个文件到 Git
```

**验收标准：**
- ✅ 角色特定任务文件跟踪详细工作
- ✅ Project Manager 文件跟踪 Epic 进度
- ✅ 更新两个文件以保持视图同步
- ✅ Git 历史提供审计跟踪

---

## **三、Deliverables (Product Features)**

### **3.1 Prompt Templates**

**[ID: PRD-FEAT-TEMPLATES-001] [Implements: PRD-REQ-GOAL-001]**

| Template 文件 | 用途 | 输入 | 输出 |
|--------------|---------|-------|--------|
| **rd-generator.md** | 生成或修改 Requirements Document | 用户故事、业务需求、（现有 RD.md） | 带 [ID: RD-XXX] 标记的 RD.md |
| **rd-reviewer.md** | 审查 Requirements Document | RD.md | 审查报告 |
| **prd-generator.md** | 生成或修改 Product Requirements Document | RD.md、产品愿景 | 带 [ID: PRD-XXX]、[Implements: PRD-REQ-XXX] 的 PRD.md |
| **prd-reviewer.md** | 审查 Product Requirements Document | PRD.md | 审查报告 |
| **design-generator.md** | 生成或修改 Design Document | PRD.md、技术约束 | 带 [ID: DESIGN-XXX]、[Designs-for: PRD-XXX] 的 Design-Document.md |
| **design-reviewer.md** | 审查 Design Document | Design-Document.md | 审查报告 |
| **test-plan-generator.md** | 生成或修改 Test Plan | Design-Document.md、PRD.md | 带 [ID: TEST-XXX]、[Tests-for: DESIGN-XXX] 的 Test-Plan.md |
| **test-plan-reviewer.md** | 审查 Test Plan | Test-Plan.md | 审查报告 |
| **code-generator.md** | 生成或修改 Code | Design-Document.md、PRD.md | 带 [ID: CODE-XXX]、[Implements: DESIGN-XXX] 的代码文件 |
| **code-reviewer.md** | 审查 Code | 代码文件、Design-Document.md | 审查报告（代码质量、安全性、可追溯性） |

**注意：**
- 所有 generator templates 同时处理创建和修改（无单独的 reviser templates）
- 当向 generator template 提供现有文档时，它会修改而非创建
- 所有 templates 自动嵌入可追溯性标记
- Templates 使用正确的术语："Design Document" 和 "Test Plan"（而非 DD/TD）

---

### **3.2 Workflow Documentation**

**[ID: PRD-FEAT-WORKFLOWS-001] [Implements: PRD-REQ-GOAL-002]**

| Workflow 文件 | 内容 | 用途 |
|--------------|---------|---------|
| **workflow-overview.md** | 整体 SDLC 流程概览 | 指导开发者完成整个生命周期 |
| **workflow-rd.md** | 逐步 RD 生成流程 | 如何使用 rd-generator.md 和 rd-reviewer.md |
| **workflow-prd.md** | 逐步 PRD 生成流程 | 如何使用 prd-generator.md 和 prd-reviewer.md |
| **workflow-design.md** | 逐步 Design Document 流程 | 如何使用 design-generator.md 和 design-reviewer.md |
| **workflow-test-plan.md** | 逐步 Test Plan 流程 | 如何使用 test-plan-generator.md 和 test-plan-reviewer.md |
| **workflow-task-mgmt.md** | 任务管理流程 | 如何跨角色视角管理 Epic 和 Task |
| **workflow-large-project.md** | 大型项目流程 | 如何为大型项目使用双层文档 |

---

### **3.3 Helper Scripts**

**[ID: PRD-FEAT-SCRIPTS-001] [Implements: PRD-REQ-GOAL-004]**

| Script | 功能 | 性能目标 | 成本目标 |
|--------|--------------|-------------------|-------------|
| **init_project.py** | 初始化项目结构，提示选择规模，创建目录 | < 5 秒 | $0 |
| **parse_tags.py** | 扫描文件，解析可追溯性标记，输出 JSON | 100K LOC < 1 分钟 | $0 |
| **build_graph.py** | 从标记构建依赖图，检测循环依赖 | 100K LOC < 1 分钟 | $0 |
| **impact_analysis.py** | 使用 git diff 和图分析文件变更的影响 | < 10 秒 | $0 |
| **check-consistency.py** | 为指定需求收集完整依赖链上下文，输出 context.md 供 Claude Code 使用 | < 5 秒 | $0 |

**技术栈：**
- Python 3.8+
- 仅标准库（核心功能无需外部依赖）
- 通过 subprocess 集成 Git
- JSON 用于数据存储

**环境约束：**
- **操作系统**：Windows 10/11
- **Shell 环境**：PowerShell 5.1+
- **Python 版本**：Python 3.8+
- **AI 助手**：Claude Code（通过命令行调用）
- **版本控制**：Git（用于影响分析）

---

## **四、Project Size Support**

### **4.1 Small Project Support**

**[ID: PRD-FEAT-SMALL-001] [Implements: PRD-REQ-STRUCTURE-SMALL-001]**

**特征：**
- 代码：< 100K 行
- 模块：1-3 个
- 文档结构：单层

**交付物：**
- 单个 RD.md 包含所有需求
- 单个 PRD.md 包含所有功能
- 单个 Design-Document.md 包含所有设计
- 单个 Test-Plan.md 包含所有测试

**Prompt Templates：**
- 标准 templates 可以直接使用
- Claude Code 可以在一个上下文中处理整个文档

---

### **4.2 Large Project Support**

**[ID: PRD-FEAT-LARGE-001] [Implements: PRD-REQ-STRUCTURE-LARGE-001]**

**特征：**
- 代码：≥ 100K 行
- 模块：4+ 个
- 文档结构：双层（Overview + 模块）

**交付物：**
- RD-Overview.md + 每个模块的 RD-{Module}.md
- PRD-Overview.md + 每个模块的 PRD-{Module}.md
- Design-Overview.md + 每个模块的 Design-{Module}.md
- Test-Overview.md + 每个模块的 Test-{Module}.md

**特殊 Templates：**
- rd-overview-generator.md（生成高层概览）
- rd-module-generator.md（生成模块特定细节）
- PRD、Design Document、Test Plan 类似

**扩展标记：**
- **[Module: XXX]** - 表示模块归属
- 模块前缀的 ID：**RD-User-REQ-001**、**RD-Order-REQ-001**

**示例：**
```markdown
## User Login Requirements
**[ID: RD-User-REQ-001] [Module: User]**

...
```

---

## **五、Non-Functional Requirements**

### **5.1 Usability**

**[ID: PRD-NFR-001]**

- ✅ 零安装：只需下载 templates 和 scripts
- ✅ 每个阶段都有清晰的 workflow 文档
- ✅ Prompt templates 以详细说明指导 Claude Code
- ✅ Helper scripts 提供友好的控制台输出

---

### **5.2 Performance**

**[ID: PRD-NFR-002]**

- ✅ 标记解析：100K+ 行代码 < 1 分钟
- ✅ 图构建：100K+ 行代码 < 1 分钟
- ✅ 影响分析：< 10 秒
- ✅ 项目初始化：< 5 秒

---

### **5.3 Cost**

**[ID: PRD-NFR-003]**

- ✅ Helper scripts：$0（本地计算）
- ✅ 使用 prompt templates：仅支付 Claude Code API 使用费（用户现有成本）
- ✅ 无软件许可费
- ✅ 无订阅费用

---

### **5.4 Maintainability**

**[ID: PRD-NFR-004]**

- ✅ 所有 templates 都是纯 Markdown 文件（易于编辑）
- ✅ 所有 scripts 都是简单的 Python（易于理解和修改）
- ✅ Git 可追踪：所有变更都有版本控制
- ✅ 可扩展：用户可以创建自定义 templates

---

## **六、Success Metrics**

### **6.1 Adoption Metrics**

**[ID: PRD-METRICS-001]**

- 使用 SpecGovernor 初始化的项目数量
- 使用 prompt templates 生成的文档数量
- GitHub stars/forks（如果开源）

---

### **6.2 Quality Metrics**

**[ID: PRD-METRICS-002]**

- 可追溯性标记覆盖率：带标记的需求/功能/设计的百分比
- 循环依赖检测率
- 用户报告的 templates 问题

---

### **6.3 Efficiency Metrics**

**[ID: PRD-METRICS-003]**

- 使用 templates 生成 RD/PRD/Design Document/Test Plan 的时间
- 相比手动文档创建节省的时间
- 成本节省（相比付费工具）

---

## **七、Risks and Limitations**

### **7.1 Risks**

**[ID: PRD-RISK-001]**

| 风险 | 影响 | 缓解措施 |
|------|--------|-----------|
| 用户忘记嵌入可追溯性标记 | 依赖图不完整 | Reviewer templates 检查标记存在 |
| Claude Code 生成不一致的标记 | 图解析错误 | Reviewer templates 验证标记格式 |
| Helper scripts 对于超大型项目太慢 | 用户体验差 | 使用增量解析、缓存优化 |

---

### **7.2 Limitations**

**[ID: PRD-LIMIT-001]**

| 限制 | 说明 |
|-----------|-------------|
| 依赖 Claude Code | 用户必须有 Claude Code 访问权限 |
| 需要手动角色切换 | 超级个体必须有意识地切换视角 |
| Python 必需 | 用户需要安装 Python 3.8+ |
| Git 必需 | 项目必须 git 初始化（用于影响分析） |

---

## **八、Summary**

### **8.1 Core Value**

**[ID: PRD-SUMMARY-001]**

SpecGovernor 通过以下方式提供价值：

1. ✅ **即用 Prompt Templates**：可立即与 Claude Code 配合使用，无需设置
2. ✅ **显式可追溯性**：通过嵌入式标记实现 100% 可靠，无 AI 猜测
3. ✅ **双重质量保证**：每个阶段都有 Generator-Reviewer 对
4. ✅ **零成本基础设施**：只需 templates 和 scripts，无软件许可证

---

### **8.2 Comparison with Alternatives**

**[ID: PRD-SUMMARY-002]**

| 维度 | SpecGovernor | 传统文档管理 | AI 编码助手 |
|-----------|-------------|--------------------------|---------------------|
| **设置** | 下载 templates | 复杂的软件安装 | 需要订阅 |
| **可追溯性** | 显式标记，100% 可靠 | 手动维护 | 隐式，不可靠 |
| **成本** | $0（+ Claude API 使用） | 高许可费 | $20+/月 |
| **学习曲线** | 阅读 workflow 文档 | 陡峭 | 中等 |
| **灵活性** | 高（编辑 templates） | 低（供应商锁定） | 中等 |

---

### **8.3 Next Steps**

**[ID: PRD-NEXT-001]**

基于本 PRD，下一步是：

1. ✅ **编写 Design Document**：prompt templates 和 scripts 的详细设计
2. ✅ **编写 Test Plan**：验证 templates 和 scripts 的测试策略
3. ✅ **实现 Templates**：创建所有 prompt template .md 文件
4. ✅ **实现 Scripts**：开发 Python helper scripts
5. ✅ **编写 Workflow Docs**：记录逐步流程

---

**PRD Document Complete**


---

**PRD Document Complete (v3.0)**
