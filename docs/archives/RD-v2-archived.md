# **📝 Requirements Document (RD) - SpecGovernor**

> **Version**: v2.0
> **Created**: 2025-11-16
> **Updated**: 2025-11-16
> **Target User**: Super Individual (超级个体) using Claude Code
> **Project Type**: Prompt Templates + Workflow Documentation + Helper Scripts (工具包)

---

## **重要说明 (Important Note)**

**SpecGovernor 是什么**：
- ✅ 一套**提示词模板集合**，用于引导 Claude Code 生成规范的 RD/PRD/Design Document/Test Plan/Code
- ✅ 一套**标准流程文档**，指导人类开发者如何使用 Claude Code 进行规范化开发
- ✅ 一些**辅助脚本**（Python/Shell），帮助解析可追溯性标记、构建依赖图、影响分析等

**SpecGovernor 不是什么**：
- ❌ 不是一个独立的 CLI 工具（不需要 `pip install specgov`）
- ❌ 不是一个需要运行的软件程序
- ❌ 不是一个复杂的代码系统

**使用方式**：
人类开发者使用 **Claude Code**，按照 SpecGovernor 提供的提示词模板和流程文档，进行规范化的软件开发。

**参考项目**：类似 [spec-kit](https://github.com/example/spec-kit)

---

## **可追溯性声明 (Traceability Declaration)**

本需求文档基于原始业务需求进行设计，采用**显式可追溯性标记 (Explicit Traceability Tagging)** 策略。

---

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
| **Traceability Tag** | 可追溯性标记 | 在文档或代码中嵌入的结构化标记，如 `[ID: RD-REQ-005]` |
| **Workflow** | 工作流程 | 标准化的开发流程步骤 |
| **Helper Script** | 辅助脚本 | 自动化处理某些任务的小型脚本 |
| **Epic** | Epic | 高层级任务，由项目经理管理 |
| **Module** | 模块 | 大型项目中的功能模块（如用户模块、支付模块） |
| **Project Size** | 项目规模 | 小项目（单层文档）或大项目（双层文档） |

---

## **二、项目目标 (Project Goals)**

**[ID: RD-GOAL-001]**

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

**[ID: RD-USER-001]**

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

**[ID: RD-USER-002]**

1. 打开 **Claude Code**
2. 加载 SpecGovernor 提供的**提示词模板**
3. 提供项目上下文和输入
4. Claude Code 按照模板生成规范化的文档/代码
5. 使用 **Reviewer 提示词**进行评审
6. 使用**辅助脚本**解析标记、构建依赖图

---

## **四、项目规模与文档结构策略 (Project Size & Document Structure)**

### **4.1 项目初始化**

**[ID: RD-INIT-001]**

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

**[ID: RD-SIZE-001]**

| 项目规模 | 代码量 | 模块数 | 文档结构 | 适用场景 |
| :---- | :---- | :---- | :---- | :---- |
| **小项目** | < 10 万行 | 1-3 个 | 单层文档 | 单体应用、小型工具、原型项目 |
| **大项目** | ≥ 10 万行 | 4+ 个 | 双层文档 | 企业级应用、微服务系统、复杂业务系统 |

### **4.3 文档结构策略**

#### **4.3.1 小项目：单层文档结构**

**[ID: RD-STRUCTURE-SMALL-001]**

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

**[ID: RD-STRUCTURE-LARGE-001]**

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

**[ID: RD-TRACE-MODULE-001]**

大项目的标记需要包含**模块信息**：

```markdown
## 用户登录需求
**[ID: RD-User-REQ-001]** **[Module: User]**

系统需支持用户通过 OAuth2 登录。
```

**标记格式**：
- `[ID: RD-{Module}-REQ-{Number}]` - 需求 ID 包含模块名
- `[Module: {ModuleName}]` - 明确模块归属
- `[Implements: RD-User-REQ-001]` - 跨模块引用

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

**[ID: RD-FR-1.1]**

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

**[ID: RD-FR-1.2]**

| 提示词 | 用途 | 输入 | 输出 |
| :---- | :---- | :---- | :---- |
| **prd-generator.md** | 生成或修改产品文档 | RD.md（或 RD.md + 现有 PRD.md） | PRD.md（包含 `[ID: PRD-XXX]` 和 `[Implements: RD-XXX]`） |
| **prd-reviewer.md** | 评审产品文档 | PRD.md + RD.md | 评审报告 |

#### **FR-1.3 Design Document 阶段提示词**

**[ID: RD-FR-1.3]**

| 提示词 | 用途 | 输入 | 输出 |
| :---- | :---- | :---- | :---- |
| **design-generator.md** | 生成或修改设计文档 | PRD.md + RD.md（或 + 现有 Design Document） | Design Document（包含 `[ID: DESIGN-XXX]` 和 `[Designs-for: PRD-XXX]`） |
| **design-reviewer.md** | 评审设计文档 | Design Document + PRD.md | 评审报告 |

#### **FR-1.4 Test Plan 阶段提示词**

**[ID: RD-FR-1.4]**

| 提示词 | 用途 | 输入 | 输出 |
| :---- | :---- | :---- | :---- |
| **test-plan-generator.md** | 生成或修改测试计划 | Design Document + PRD.md（或 + 现有 Test Plan） | Test Plan（包含 `[ID: TEST-XXX]` 和 `[Tests-for: DESIGN-XXX]`） |
| **test-plan-reviewer.md** | 评审测试计划 | Test Plan + Design Document | 评审报告 |

#### **FR-1.5 Code 阶段提示词**

**[ID: RD-FR-1.5]**

| 提示词 | 用途 | 输入 | 输出 |
| :---- | :---- | :---- | :---- |
| **code-generator.md** | 生成或修改代码 | Design Document + PRD.md（或 + 现有代码） | 代码（包含 `[ID: CODE-XXX]` 注释） |
| **code-reviewer.md** | 评审代码 | 代码 + Design Document | 评审报告 |

#### **FR-1.6 一致性检查提示词**

**[ID: RD-FR-1.6]**

| 提示词 | 用途 | 输入 | 输出 |
| :---- | :---- | :---- | :---- |
| **consistency-checker.md** | 检查 RD/PRD/Design Document/Code 一致性 | 依赖链涉及的文档和代码 | 不一致报告 |
| **impact-analyzer.md** | 分析变更影响 | 变更文件 + 依赖图 | 受影响的下游节点列表 |

---

### **4.2 工作流程文档 (Workflow Documentation)**

#### **FR-2.1 RD 工作流程**

**[ID: RD-FR-2.1]**

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

**[ID: RD-FR-2.2]**

类似 RD 工作流程，提供：
- `workflows/prd-workflow.md`
- `workflows/design-workflow.md`
- `workflows/test-plan-workflow.md`
- `workflows/code-workflow.md`

#### **FR-2.3 影响分析工作流程**

**[ID: RD-FR-2.3]**

提供 `workflows/impact-analysis.md`，包含：

1. 修改某个文档（如 RD.md）
2. 运行辅助脚本：`python scripts/analyze-impact.py --changed=docs/RD.md`
3. 脚本输出受影响的下游节点（PRD、DD、Code）
4. 人类开发者根据输出，决定是否重新生成下游文档

#### **FR-2.4 一致性检查工作流程**

**[ID: RD-FR-2.4]**

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

**[ID: RD-FR-3.1]**

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

**[ID: RD-FR-3.2]**

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

**[ID: RD-FR-3.3]**

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

**[ID: RD-FR-3.4]**

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

**[ID: RD-FR-4.1]**

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

**[ID: RD-FR-5.1]**

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

**[ID: RD-FR-5.2]**

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

**[ID: RD-FR-5.3]**

提供以下模板：

| 模板文件 | 用途 |
| :---- | :---- |
| `templates/project-manager-tasks.md` | 项目经理任务文档模板 |
| `templates/role-tasks.md` | 角色任务文档模板 |

---

### **4.6 示例项目 (Example Projects)**

#### **FR-6.1 提供完整示例**

**[ID: RD-FR-6.1]**

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

**[ID: RD-TRACE-001]**

| 标记 | 格式 | 说明 | 示例 |
| :---- | :---- | :---- | :---- |
| **ID** | `[ID: PREFIX-XXX-YYY]` | 定义当前内容的唯一标识 | `[ID: RD-REQ-005]` |
| **Implements** | `[Implements: ID]` | 声明实现了上游需求 | `[Implements: RD-REQ-005]` |
| **Designs-for** | `[Designs-for: ID]` | 声明是某功能的设计 | `[Designs-for: PRD-FEAT-012]` |
| **Tests-for** | `[Tests-for: ID]` | 声明是某设计的测试 | `[Tests-for: DD-API-008]` |

### **5.2 ID 前缀规范**

**[ID: RD-TRACE-002]**

| 阶段 | 前缀 | 示例 |
| :---- | :---- | :---- |
| RD | `RD-REQ-`, `RD-GOAL-` | RD-REQ-001, RD-GOAL-001 |
| PRD | `PRD-FEAT-`, `PRD-US-` | PRD-FEAT-012, PRD-US-003 |
| Design Document | `DESIGN-API-`, `DESIGN-DB-`, `DESIGN-ARCH-` | DESIGN-API-008, DESIGN-DB-005 |
| Test Plan | `TEST-CASE-`, `TEST-PERF-` | TEST-CASE-015, TEST-PERF-003 |
| Code | `CODE-API-`, `CODE-SERVICE-` | CODE-API-008 |

### **5.3 嵌入位置**

**[ID: RD-TRACE-003]**

**Markdown 文档**：
```markdown
## OAuth2 登录需求
**[ID: RD-REQ-005]**

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

**[ID: RD-STRUCTURE-001]**

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

**[ID: RD-NFR-001]**

- 提示词模板应清晰易懂，人类开发者无需培训即可使用
- 工作流程文档应图文并茂，步骤明确
- 辅助脚本应提供 `--help` 选项，说明用法

### **7.2 可扩展性**

**[ID: RD-NFR-002]**

- 人类开发者可以自定义提示词模板
- 人类开发者可以扩展辅助脚本

### **7.3 兼容性**

**[ID: RD-NFR-003]**

- 提示词模板应兼容 Claude Code（主要）
- 辅助脚本应使用 Python 3.8+，无复杂依赖

### **7.4 性能**

**[ID: RD-NFR-004]**

- `parse-tags.py`：100 万行代码 < 1 分钟
- `analyze-impact.py`：< 10 秒
- `check-consistency.py`：构建上下文 < 5 秒

---

## **八、验收标准 (Acceptance Criteria)**

**[ID: RD-AC-001]**

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

**[ID: RD-SCENARIO-000]**

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

**[ID: RD-SCENARIO-001]**

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
   **[ID: RD-REQ-005]**

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

**[ID: RD-SCENARIO-002]**

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

**[ID: RD-SCENARIO-003]**

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

**[ID: RD-SCENARIO-004]**

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

**[ID: RD-SUMMARY-001]**

SpecGovernor 提供：

1. ✅ **标准化的提示词模板**，引导 Claude Code 生成规范文档/代码（generator 既能创建也能修改）
2. ✅ **清晰的工作流程**，指导人类开发者进行规范化开发
3. ✅ **可追溯性机制**，建立 RD → PRD → Design Document → Test Plan → Code 的追溯链
4. ✅ **两层任务管理**，项目经理视角（Epic）+ 角色视角（Task），跟踪整体进度和具体任务
5. ✅ **轻量级辅助脚本**，自动化解析、分析任务
6. ✅ **易于使用**，无需安装，直接配合 Claude Code 使用

### **10.2 下一步工作**

**[ID: RD-NEXT-001]**

1. ⏳ **编写 PRD（产品需求文档）**：详细描述每个提示词模板的功能
2. ⏳ **编写 Design Document（设计文档）**：定义辅助脚本的实现细节
3. ⏳ **编写 Test Plan（测试计划）**：设计如何测试提示词模板和脚本
4. ⏳ **实现提示词模板**：编写所有提示词模板
5. ⏳ **实现辅助脚本**：编写 Python 脚本
6. ⏳ **创建示例项目**：提供完整的示例

---

**需求文档结束 (End of Requirements Document)**
