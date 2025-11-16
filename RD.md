# **📝 Requirements Document (RD) - SpecGovernor**

> **Version**: v1.0
> **Created**: 2025-11-16
> **Target User**: Super Individual (超级个体)
> **Project Type**: AI-Enhanced SDLC Governance System

---

## **可追溯性声明 (Traceability Declaration)**

本需求文档基于原始业务需求进行设计，采用**显式可追溯性标记 (Explicit Traceability Tagging)** 策略。

---

## **一、术语与缩略语 (Terminology and Glossary)**

| 术语/缩略语 | 英文全称 | 解释说明 |
| :---- | :---- | :---- |
| **SDLC** | Software Development Life Cycle | 软件开发生命周期，指从规划、设计、编码、测试到部署的整个软件开发过程 |
| **RD** | Requirements Document | 需求文档。侧重于**用户和业务目标**，描述**系统应该做什么** |
| **PRD** | Product Requirements Document | 产品需求文档。侧重于**产品功能**，描述**实现哪些功能来满足需求** |
| **DD** | Design Document | 设计文档。侧重于**技术实现**，描述**如何构建系统** |
| **TD** | Test Document | 测试文档。侧重于**验证标准**，描述**如何测试**系统 |
| **Agent** | AI Agent | 基于 Claude Code 或 Gemini CLI 等大模型的软件智能体 |
| **Generator Agent** | Generator Agent | 负责生成文档或代码的 AI Agent |
| **Reviewer Agent** | Reviewer Agent | 负责评审文档或代码的 AI Agent |
| **CLI Commands** | CLI 命令层 | 实现各个 CLI 命令的模块，直接处理用户请求和业务逻辑 |
| **State Manager** | 状态管理器 | 负责读写 `.specgov/state.json`，管理流程状态和任务进度 |
| **Context Builder** | 上下文构建器 | 负责加载项目背景、裁剪文档片段、构建 AI 提示词 |
| **Project Index** | 项目索引 | 预先构建的项目结构化元数据，包含依赖关系图等 |
| **Dependency Graph** | 依赖图 | 描述 RD → PRD → DD → TD → Code 之间依赖关系的有向图 |
| **Traceability Tag** | 可追溯性标记 | 在文档或代码中嵌入的结构化标记，如 `[ID: RD-REQ-005]` |
| **Epic** | Epic | 高层级任务，由项目经理管理 |
| **Task** | Task | 具体任务，由各角色管理 |

---

## **二、用户角色与使用场景 (User Roles & Usage Scenarios)**

### **2.1 目标用户：超级个体 (Super Individual)**

**[ID: RD-USER-001]**

本系统的目标用户是**超级个体**，即一人承担多个研发角色的技术专家：

| 角色组成 | 职责范围 |
| :---- | :---- |
| **需求分析师** | 分析业务需求，编写和审阅 RD |
| **产品经理** | 定义产品功能，编写和审阅 PRD |
| **架构师** | 设计系统架构，编写和审阅 DD |
| **开发工程师** | 实现代码 |
| **测试经理** | 设计测试策略，编写和审阅 TD |
| **项目经理** | 统筹项目进度，管理变更和一致性 |

**典型画像**：
- 独立开发者
- 技术创业者
- 小团队核心负责人

### **2.2 核心使用场景**

#### **场景 1：Generator-Reviewer 对模式**

**[ID: RD-SCENARIO-001]**

超级个体通过多个 AI 客户端并行工作，每个文档阶段都采用"生成-评审"对模式：

```
RD 阶段：
  客户端 1: RD Generator Agent（生成需求文档，分配唯一ID标记 `[ID: RD-REQ-001]`）
  客户端 2: RD Reviewer Agent（评审需求文档）
  客户端 1: 根据评审结果修订文档

PRD 阶段：
  客户端 3: PRD Generator Agent（基于 RD 生成，嵌入 `[Implements: RD-REQ-001]`）
  客户端 4: PRD Reviewer Agent（评审产品文档）

DD/TD/Code 阶段：依此类推...
```

**价值**：Generator 和 Reviewer 使用不同的 AI 实例，避免自我审查偏差。

#### **场景 2：模块并行处理**

**[ID: RD-SCENARIO-002]**

针对大型项目（50-100万行代码），超级个体可以并行处理不同模块：

```
客户端 1: 处理用户模块的一致性检查
客户端 2: 处理订单模块的一致性检查
客户端 3: 处理支付模块的一致性检查
```

**价值**：将全项目验证时间从 30 分钟降低到 5-10 分钟。

#### **场景 3：影响分析与变更传播**

**[ID: RD-SCENARIO-003]**

超级个体修改某个文档后，系统快速分析影响范围：

```bash
# 用户修改 RD
$ specgov analyze:impact --changed=docs/rd.md

# 系统输出
受影响的文档：
  - PRD 第 3.2 节（用户登录功能）
  - DD 第 4.1 节（认证服务设计）
  - TD 第 5.1 节（登录测试用例）
受影响的代码：
  - src/auth/auth.service.ts
  - src/user/user.controller.ts
```

#### **场景 4：代码提交前的全链路验证**

**[ID: RD-SCENARIO-004]**

```bash
$ specgov check:consistency --scope=full

系统输出:
  [检查中] UserModule... ✓
  [检查中] OrderModule... ✓
  [检查中] PaymentModule... ✗

  发现 3 处不一致：
  1. DD 设计的 API 是 POST /payments，代码实现是 PUT /payments
  2. PRD 要求支持分页，代码未实现
  3. RD 禁止存储明文密钥，代码未加密
```

### **2.3 系统集成方式**

**[ID: RD-INTEGRATION-001]**

- **AI 后端**：支持 Claude Code、Gemini CLI 等多种大模型 CLI 工具
- **部署形态**：纯 CLI 工具，无需独立后台服务
- **状态管理**：通过 Git 仓库中的 `.specgov/` 目录管理流程状态和索引
- **触发方式**：超级个体主动调用 CLI 命令（半自动化）

### **2.4 项目规模支持**

**[ID: RD-SCALE-001]**

- **目标规模**：中小型项目，代码量 ≤ 100 万行
- **典型项目**：10-20 个模块，每个模块 5-10 万行代码
- **性能保证**：通过索引机制和模块化检查，确保大型项目的可用性

---

## **三、项目目标 (Project Goals)**

**[ID: RD-GOALS-001]**

| ID | 目标描述 | 达成标准 |
| :---- | :---- | :---- |
| **G-1** | **流程规范化与自动化** | 将 SDLC 流程转化为可由软件工具和 AI Agent 自动执行的流程 |
| **G-2** | **文档代码持续一致性** | 实现 RD/PRD/DD/TD/Code 之间的高质量一致性，不一致检测准确率 ≥ 85% |
| **G-3** | **提升研发效率** | 文档生成时间减少 60%，评审时间减少 50% |
| **G-4** | **支持中小型复杂项目** | 影响分析 < 10秒，模块级检查 < 2分钟，全项目检查 < 10分钟 |
| **G-5** | **成本可控** | 影响分析 $0，单模块检查 < $0.05，全项目检查 < $2 |

---

## **四、功能需求 (Functional Requirements - FR)**

### **4.1 文档与代码生成**

#### **FR-1.1 Generator-Reviewer 对模式**
**[ID: RD-FR-1.1]**

系统需支持**生成-评审对模式**：每个文档阶段都有独立的 Generator Agent 和 Reviewer Agent。

**关键组件**：
- RD/PRD/DD/TD Generator & Reviewer Agent 对
- CLI Commands（命令层）
- Context Builder（上下文构建器）
- State Manager（状态管理器）

#### **FR-1.2 Generator Agent 规范**
**[ID: RD-FR-1.2]**

Generator Agent 的输入必须包含：
1. 上游文档内容（由 Context Builder 精准裁剪）
2. 生成提示词模板
3. 项目上下文元数据

输出要求：
- 结构化格式（Markdown + YAML Front Matter）
- 包含**所有相关**的显式可追溯性标记（如 `[Implements: ID]` 或 `[Decomposes: ID]`）

#### **FR-1.3 Reviewer Agent 规范**
**[ID: RD-FR-1.3]**

Reviewer Agent 的输入必须包含：
1. 待评审文档
2. 上游文档（对照）
3. 评审检查清单

输出要求：
- 结构化的评审报告（JSON 格式）
- 问题列表、严重程度、建议修改

#### **FR-1.4 代码与测试 Agent**
**[ID: RD-FR-1.4]**

代码与测试 Agent 需能基于 DD 和 PRD 的上下文，生成满足规范的测试用例和代码片段，并**在代码注释中嵌入可追溯性标记**。

### **4.2 项目索引与依赖管理**

#### **FR-2.1 索引构建命令**
**[ID: RD-FR-2.1]**

系统需提供**索引构建命令**（如 `specgov index:build`），用于**解析项目中的所有显式可追溯性标记**。

索引内容包括：
1. 模块划分
2. 文档章节映射
3. 代码符号（API、类、函数）
4. 依赖关系图

**关键技术**：高速文本解析器（非 AI）

#### **FR-2.2 索引持久化**
**[ID: RD-FR-2.2]**

索引需持久化到 `.specgov/index/` 目录，包含以下文件：
- `modules.json`（模块列表）
- `dependency-graph.json`（依赖图）
- `rd-map.json`（RD 映射）
- `prd-map.json`（PRD 映射）
- `dd-map.json`（DD 映射）
- `code-map.json`（代码符号映射）

#### **FR-2.3 增量索引更新**
**[ID: RD-FR-2.3]**

系统需支持**增量索引更新**：当文档或代码变更时（通过 Git diff 检测），只重新解析变更文件中的标记并更新索引。

### **4.3 影响分析与一致性检查**

#### **FR-3.1 影响分析命令**
**[ID: RD-FR-3.1]**

系统需提供**影响分析命令**（如 `specgov analyze:impact --changed=<file>`），基于依赖图快速定位受影响的下游文档和代码。

**性能要求**：
- 响应时间 < 10 秒
- 无需调用 AI（纯图查询）

#### **FR-3.2 影响分析输出格式**
**[ID: RD-FR-3.2]**

影响分析输出必须是结构化的 JSON 格式，包含：
- `changed`（变更项列表）
- `affected`（受影响项列表）
- `recommendation`（建议的后续操作）

#### **FR-3.3 一致性检查命令**
**[ID: RD-FR-3.3]**

系统需提供**一致性检查命令**（支持多种作用域）：
- `--scope=<ID>`：检查单个需求/功能的全链路一致性
- `--scope=<module>`：检查单个模块的一致性
- `--scope=full`：检查全项目一致性（并行分解为多个模块检查）

#### **FR-3.4 一致性检查实现策略**
**[ID: RD-FR-3.4]**

实现步骤：
1. 基于索引定位相关依赖链
2. 只加载依赖链涉及的文档和代码片段（< 5000 行）
3. 构造精准上下文发送给 AI Agent
4. 输出结构化差异报告（JSON 格式）

#### **FR-3.5 一致性检查模式**
**[ID: RD-FR-3.5]**

支持两种模式：
- **快速模式**：基于元数据和关键词匹配，< 10 秒
- **深度模式**：深度语义分析，5-10 分钟

### **4.4 变更触发与流程控制**

#### **FR-4.1 主动触发检查**
**[ID: RD-FR-4.1]**

系统需支持**主动触发检查**（超级个体手动调用 CLI 命令），可通过 Git Hooks 集成实现半自动化触发。

#### **FR-4.2 状态管理机制**
**[ID: RD-FR-4.2]**

系统需提供**状态管理机制**：通过 `.specgov/state.json` 记录当前流程状态、各文档的版本和状态、上次检查结果等。

#### **FR-4.3 外部工具集成（可选）**
**[ID: RD-FR-4.3]**

系统可根据校验结果，通过集成连接器在外部工具（如 Jira）中创建同步任务，或通过 Git Hooks 阻塞不符合规范的提交。

**实现方式**：
- CLI Commands 执行完成后调用集成连接器
- 通过配置文件定义集成规则
- 支持自定义 Hook 脚本

---

## **五、任务管理系统需求 (Task Management Requirements)**

### **5.1 两层任务管理架构**

#### **FR-5.1 Epic 层级管理**
**[ID: RD-TASK-LAYER-001]**

系统需支持**两层任务管理**：

```
项目经理（High-level）
    └── 管理 Epic 级别任务
        ├── Epic 1: RD 阶段
        ├── Epic 2: PRD 阶段
        ├── Epic 3: DD 阶段
        └── ...

角色层（Role-level）
    ├── 需求分析师
    │   ├── Task 1.1: 生成 RD
    │   ├── Task 1.2: 评审 RD
    │   └── Task 1.3: 修订 RD
    ├── 产品经理
    │   ├── Task 2.1: 生成 PRD
    │   └── ...
    └── ...
```

**关键设计**：
- 项目经理只看 Epic 级别进度
- 各角色独立管理自己的子任务
- 子任务完成后自动更新 Epic 进度

#### **FR-5.2 任务文件结构**
**[ID: RD-TASK-FILES-001]**

任务文件存储在 `.specgov/tasks/` 目录：

```
.specgov/
├── tasks/
│   ├── project.md              # 项目经理的 High-level 任务
│   ├── rd-analyst.md           # 需求分析师的任务
│   ├── product-manager.md      # 产品经理的任务
│   ├── architect.md            # 架构师的任务
│   └── test-manager.md         # 测试经理的任务
```

### **5.2 无状态角色设计**

#### **FR-5.3 跨设备状态同步**
**[ID: RD-TASK-STATE-001]**

**目标**：从任意电脑打开项目，AI 都能继续未完成的任务

**实现方式**：
- 所有状态存储在 `.specgov/` 目录（Git 仓库）
- 每个角色有独立的任务文件
- AI 启动时自动读取任务状态和背景

#### **FR-5.4 上下文管理文件**
**[ID: RD-TASK-CONTEXT-001]**

系统需提供以下上下文文件：

```
.specgov/
├── context/
│   ├── project-brief.md        # 项目简介（永久）
│   ├── current-focus.md        # 当前焦点（动态）
│   └── roles-context.json      # 各角色上下文状态
```

**挑战**：AI 需要了解项目背景才能继续任务，但不能每次都加载完整项目（超出上下文窗口）

**解决方案**：
- 分层上下文注入
- 智能裁剪

### **5.3 任务复杂度管理**

#### **FR-5.5 任务分解规则**
**[ID: RD-TASK-DECOMPOSE-001]**

**目标**：确保每个子任务简单明确，不超出 AI 上下文窗口

**规则**：
- 单个任务上下文 < 5K tokens
- 单个任务执行时间 < 5 分钟
- 单个任务成本 < $0.20

#### **FR-5.6 任务复杂度检查**
**[ID: RD-TASK-COMPLEXITY-001]**

系统需自动检测任务复杂度：

```yaml
任务复杂度级别:
  简单:
    上下文: < 5K tokens
    示例: "生成单个需求的文档"

  中等:
    上下文: 5K - 10K tokens
    示例: "评审整个 RD 文档（< 50 需求）"

  复杂:
    上下文: 10K - 20K tokens
    示例: "检查单个模块的一致性"
    注意: 需要分解为多个子任务

  过于复杂:
    上下文: > 20K tokens
    处理: 拒绝，强制分解
```

#### **FR-5.7 自动任务分解提示**
**[ID: RD-TASK-AUTO-DECOMPOSE-001]**

当检测到任务过大时，系统需提示用户：

```bash
$ specgov rd:generate --scope=full

⚠️  警告：任务过大

检测到需要生成完整的 RD 文档（预计 15 个需求）。
这会导致上下文过大（约 25K tokens），超出单次任务限制。

建议分解为以下子任务：
  1. specgov rd:generate --scope=auth-module
  2. specgov rd:generate --scope=user-module
  3. specgov rd:generate --scope=payment-module

是否继续？[y/N] _
```

### **5.4 AI 上下文注入**

#### **FR-5.8 上下文构建策略**
**[ID: RD-TASK-AI-CONTEXT-001]**

AI 提示词构建需包含以下层次：

1. **角色定义**：约 500 tokens
2. **项目背景**：`project-brief.md`，约 500 tokens
3. **当前焦点**：`current-focus.md`，约 300 tokens
4. **任务上下文**：相关文件（智能裁剪）
5. **任务指令**：约 200 tokens

**总计控制**：< 5K tokens

#### **FR-5.9 角色切换命令**
**[ID: RD-TASK-ROLE-SWITCH-001]**

系统需提供角色切换命令：

```bash
$ specgov role:switch <role>

# 示例
$ specgov role:switch product-manager

✓ 已切换到：产品经理
✓ 当前任务：Task 2.2: 评审 PRD
```

#### **FR-5.10 任务查询命令**
**[ID: RD-TASK-QUERY-001]**

系统需提供任务查询命令：

```bash
# 查看当前角色的任务
$ specgov tasks:show

# 查看指定角色的任务
$ specgov tasks:show --role=product-manager

# 查看项目经理的 High-level 任务
$ specgov tasks:show --level=high
```

#### **FR-5.11 下一个任务推荐**
**[ID: RD-TASK-NEXT-001]**

系统需提供任务推荐功能：

```bash
$ specgov tasks:next

🎯 你的下一个任务：

Task 2.2: 评审 PRD
执行者：产品经理
命令：specgov prd:review --ai=gemini-cli

预计时间：10 分钟
预计成本：$0.08

是否立即执行？[Y/n] _
```

### **5.5 AI 后端支持**

#### **FR-5.12 Claude Code 支持**
**[ID: RD-AI-BACKEND-001]**

系统当前只需支持 Claude Code 作为 AI 后端：

```yaml
# .specgov/config.yml
ai_backend:
  default: claude-code

  claude-code:
    command: "claude-code execute"
    model: "claude-sonnet-4"
    max_tokens: 200000
    cost_per_1k_tokens:
      input: 0.003
      output: 0.015
```

#### **FR-5.13 未来 AI 后端扩展（预留接口）**
**[ID: RD-AI-BACKEND-EXTENSIBLE-001]**

系统架构需支持未来扩展其他 AI 后端：

```yaml
# 未来支持
gemini-cli:
  command: "gemini execute"
  model: "gemini-1.5-pro"
  max_tokens: 2000000
  enabled: false  # 暂不启用
```

---

## **六、非功能需求与约束 (Non-Functional Requirements - NFR)**

### **6.1 架构约束**

#### **NFR-1.1 禁止使用 RAG/向量数据库**
**[ID: RD-NFR-1.1]**

**禁止**使用统一的向量数据库 (RAG/Vector DB) 作为知识持久化层。

**对设计的影响**：
- Context Builder 必须通过**项目索引 + 依赖图**实现上下文检索和拼接
- CLI Commands 负责协调各模块完成任务
- 所有上下文数据从文件系统读取，无需外部数据库

#### **NFR-1.2 纯 CLI 架构**
**[ID: RD-NFR-1.2]**

系统必须以纯 CLI 工具形式实现，无需独立的后台服务或数据库。状态通过文件系统（`.specgov/` 目录）管理。

#### **NFR-1.3 多 AI 后端支持（架构层面）**
**[ID: RD-NFR-1.3]**

系统必须支持多种 AI CLI 工具（Claude Code、Gemini CLI 等），通过统一的接口调用。当前只实现 Claude Code，但架构需为未来扩展预留接口。

### **6.2 性能需求**

#### **NFR-2.1 影响分析响应时间**
**[ID: RD-NFR-2.1]**

- **目标**：< 10 秒
- **实现**：基于索引的纯图查询，不调用 AI

#### **NFR-2.2 单点一致性检查**
**[ID: RD-NFR-2.2]**

- **目标**：< 2 分钟
- **场景**：检查单个需求/功能的全链路一致性
- **上下文**：< 5K tokens

#### **NFR-2.3 模块级一致性检查**
**[ID: RD-NFR-2.3]**

- **目标**：< 2 分钟
- **场景**：检查单个模块
- **上下文**：< 20K tokens

#### **NFR-2.4 全项目一致性检查**
**[ID: RD-NFR-2.4]**

- **目标**：< 10 分钟
- **场景**：10 个模块并行检查
- **总上下文**：< 200K tokens

#### **NFR-2.5 索引构建时间**
**[ID: RD-NFR-2.5]**

- **目标**：< 1 分钟
- **场景**：100 万行代码项目
- **实现**：纯解析，无 AI 调用

#### **NFR-2.6 增量索引更新**
**[ID: RD-NFR-2.6]**

- **目标**：< 5 秒
- **场景**：单个文件的重新解析

### **6.3 上下文管理**

#### **NFR-3.1 精准裁剪和拼接**
**[ID: RD-NFR-3.1]**

流程中的所有 AI Agent 必须通过 **Context Builder** 提供的**精准裁剪和拼接**的上下文来工作。

**Context Builder 必须具备的能力**：
1. 根据依赖图定位相关节点
2. 只加载相关文档和代码片段
3. 控制上下文大小在 AI 窗口范围内
4. 智能合并多个文档片段形成连贯上下文

**实现方式**：
- CLI Commands 调用 Context Builder 构建提示词
- Context Builder 从依赖图中查询相关节点
- 从文件系统读取并裁剪文档内容

#### **NFR-3.2 上下文大小控制**
**[ID: RD-NFR-3.2]**

单次 AI 调用的上下文大小必须控制在合理范围内：
- 快速检查：< 5K tokens
- 深度检查：< 20K tokens
- 极限情况：< 50K tokens

如果超出限制，必须分解为多个子任务。

### **6.4 Agent 架构**

#### **NFR-4.1 Generator-Reviewer 对模式**
**[ID: RD-NFR-4.1]**

必须采用**生成-评审对模式**：每个文档阶段都有独立的 Generator Agent 和 Reviewer Agent，使用不同的 AI 实例。

**对设计的影响**：需要为每个阶段定义两套提示词模板和 Agent 配置。

#### **NFR-4.2 去中心化、多 Agent 族结构**
**[ID: RD-NFR-4.2]**

必须采用**去中心化、多 Agent 族**的结构，支持同一文档层级拆分为多个子任务 Agent。

**对设计的影响**：需保证 Agent 间的接口协议（输入/输出 Schema）清晰、稳定。

#### **NFR-4.3 结构化输出**
**[ID: RD-NFR-4.3]**

所有关键的 AI Agent 输出（如影响分析报告、差异报告、评审报告）必须是**结构化数据**（JSON/YAML）。

**对设计的影响**：提示词中必须明确要求结构化输出，并进行格式验证。

### **6.5 可靠性与容错**

#### **NFR-5.1 人工仲裁机制**
**[ID: RD-NFR-5.1]**

流程的关键节点必须设置**Human-in-the-Loop** 机制：当 AI 评审发现严重问题、或一致性检查失败率 > 20% 时，必须提示超级个体介入。

**对设计的影响**：CLI 命令需支持交互式确认和人工决策。

#### **NFR-5.2 AI 调用重试机制**
**[ID: RD-NFR-5.2]**

所有 AI 调用必须有**重试机制**：API 调用失败时自动重试最多 3 次，超时时间 120 秒。

**对设计的影响**：需要封装统一的 AI 调用层，处理异常和重试。

#### **NFR-5.3 操作回滚支持**
**[ID: RD-NFR-5.3]**

系统必须支持**操作回滚**：通过 Git 版本控制，所有文档和索引变更都可以回滚到历史版本。

**对设计的影响**：利用 Git 的天然版本控制能力，无需额外实现。

### **6.6 成本控制**

#### **NFR-6.1 影响分析成本**
**[ID: RD-NFR-6.1]**

- **目标**：$0
- **实现**：基于索引的纯图查询，不调用 AI

#### **NFR-6.2 单点一致性检查成本**
**[ID: RD-NFR-6.2]**

- **上下文**：< 5K tokens
- **目标**：< $0.02 (Claude) 或 < $0.01 (Gemini)

#### **NFR-6.3 模块级检查成本**
**[ID: RD-NFR-6.3]**

- **上下文**：< 20K tokens
- **目标**：< $0.05

#### **NFR-6.4 全项目检查成本**
**[ID: RD-NFR-6.4]**

- **场景**：10 个模块，总上下文 < 200K tokens
- **目标**：< $2

#### **NFR-6.5 索引构建成本**
**[ID: RD-NFR-6.5]**

- **操作类型**：一次性操作，纯文本解析
- **目标**：$0

---

## **七、关键交付流程 (Key Delivery Workflows)**

### **7.1 标准文档生成流程（以 RD 为例）**

**[ID: RD-WORKFLOW-001]**

| 步骤 | CLI 命令 | 执行流程 | 涉及组件 |
| :---- | :---- | :---- | :---- |
| **1. 生成** | `specgov rd:generate` | (1) CLI Command 读取输入文件和项目上下文<br>(2) Context Builder 构建 AI 提示词（裁剪到 < 5K tokens）<br>(3) 调用 RD Generator Agent 生成初稿，嵌入ID标记<br>(4) 保存到 `docs/RD.md`<br>(5) State Manager 更新 `.specgov/state.json` | CLI Command<br>Context Builder<br>RD Generator Agent<br>State Manager |
| **2. 评审** | `specgov rd:review` | (1) CLI Command 读取生成的 RD<br>(2) Context Builder 构建评审提示词<br>(3) 调用 RD Reviewer Agent 评审<br>(4) 输出结构化评审报告（JSON）<br>(5) 如发现严重问题，CLI Command 提示人工介入 | CLI Command<br>Context Builder<br>RD Reviewer Agent |
| **3. 修订** | `specgov rd:revise` | (1) CLI Command 读取 RD 和评审报告<br>(2) Context Builder 构建修订提示词<br>(3) 调用 RD Generator Agent 根据评审意见修订<br>(4) 更新文档<br>(5) State Manager 更新状态 | CLI Command<br>Context Builder<br>RD Generator Agent<br>State Manager |
| **4. 索引更新** | `specgov index:update --scope=rd` | (1) Tag Parser 高速解析 RD 文档中的标记<br>(2) Graph Builder 更新依赖图中的 RD 节点<br>(3) 保存到 `.specgov/index/dependency-graph.json` | Tag Parser<br>Graph Builder |

### **7.2 变更传播与影响分析流程**

**[ID: RD-WORKFLOW-002]**

| 触发场景 | CLI 命令 | 执行流程 | 输出 |
| :---- | :---- | :---- | :---- |
| **修改 RD** | `specgov analyze:impact --changed=docs/rd.md` | (1) Git diff 识别变更内容<br>(2) 从依赖图中查询下游节点<br>(3) 返回受影响的 PRD/DD/TD/Code 列表 | JSON 格式的影响范围报告 |
| **更新下游** | `specgov prd:regenerate --based-on=rd` | (1) 读取变更后的 RD<br>(2) 重新生成 PRD（自动嵌入可追溯性标记）<br>(3) 自动触发 PRD 评审 | 更新后的 PRD 文档 |

### **7.3 一致性检查流程**

**[ID: RD-WORKFLOW-003]**

| 检查场景 | CLI 命令 | 执行流程 | 性能要求 |
| :---- | :---- | :---- | :---- |
| **单个需求** | `specgov check:consistency --scope=RD-REQ-005` | (1) 基于依赖图定位依赖链<br>(2) 只加载依赖链涉及的文档和代码片段<br>(3) 调用一致性守护 Agent<br>(4) 输出差异报告 | < 2 分钟 |
| **单个模块** | `specgov check:consistency --scope=UserModule` | (1) 加载该模块相关的所有文档和代码<br>(2) 调用一致性守护 Agent<br>(3) 输出差异报告 | < 2 分钟 |
| **全项目** | `specgov check:consistency --scope=full` | (1) 分解为 10 个模块检查任务<br>(2) 超级个体启动多个 AI 客户端并行执行<br>(3) 汇总所有模块的差异报告 | < 10 分钟 |
| **提交前验证** | `specgov check:pre-commit` | (1) 检测本次提交涉及的代码文件<br>(2) 只检查相关模块的一致性<br>(3) 如发现不一致，阻止提交（通过 Git Hook） | < 2 分钟 |

---

## **八、技术实现策略 (Technical Implementation Strategy)**

### **8.1 核心技术挑战与解决方案**

**[ID: RD-TECH-CHALLENGE-001]**

#### **挑战：如何在 100 万行代码的项目中进行一致性检查？**

**问题分析**：
- Claude Code / Gemini CLI 的上下文窗口有限（200K - 2M tokens）
- 100 万行代码约需 750 万 tokens，远超上下文窗口
- 直接加载所有代码进行检查是不可行的

**解决方案：显式标记 + 解析构建 + 按需加载**

```
核心思想：
不依赖 AI 推断依赖关系，而是通过在文档和代码中嵌入显式标记，
让依赖关系成为可直接解析的结构化数据。

实现步骤：
1. 在文档/代码中嵌入可追溯性标记 (如 [Implements: RD-REQ-005])
2. 通过高速解析器（非 AI）构建项目索引和依赖图
3. 基于依赖图进行影响分析和依赖链定位
4. 只加载相关的文档和代码片段（< 20K tokens）
```

### **8.2 项目索引机制**

**[ID: RD-TECH-INDEX-001]**

#### **8.2.1 索引结构设计**

```
项目目录结构：
my-project/
├── .specgov/                      # 系统工作目录
│   ├── state.json                 # 流程状态
│   ├── config.yml                 # 配置文件
│   ├── index/                     # 项目索引
│   │   ├── modules.json           # 模块列表
│   │   ├── dependency-graph.json  # 依赖关系图
│   │   ├── rd-map.json            # RD 需求映射
│   │   ├── prd-map.json           # PRD 功能映射
│   │   ├── dd-map.json            # DD 设计映射
│   │   └── code-map.json          # 代码符号映射
│   ├── context/                   # 上下文管理
│   │   ├── project-brief.md       # 项目简介
│   │   ├── current-focus.md       # 当前焦点
│   │   └── roles-context.json     # 角色上下文
│   ├── tasks/                     # 任务管理
│   │   ├── project.md             # 项目经理任务
│   │   ├── rd-analyst.md          # 需求分析师任务
│   │   ├── product-manager.md     # 产品经理任务
│   │   ├── architect.md           # 架构师任务
│   │   └── test-manager.md        # 测试经理任务
│   └── reports/                   # 报告输出
├── docs/                          # 文档目录
│   ├── RD.md
│   ├── PRD.md
│   └── DD.md
└── src/                           # 代码目录
```

#### **8.2.2 依赖图示例**

```json
// .specgov/index/dependency-graph.json
{
  "nodes": [
    {
      "id": "RD-REQ-005",
      "type": "requirement",
      "summary": "OAuth2 登录需求",
      "location": "docs/RD.md#L42"
    },
    {
      "id": "PRD-FEAT-012",
      "type": "feature",
      "summary": "实现 OAuth2 登录流程",
      "location": "docs/PRD.md#L128"
    },
    {
      "id": "DD-API-008",
      "type": "api_design",
      "summary": "POST /auth/oauth2/callback",
      "location": "docs/DD.md#L234"
    },
    {
      "id": "CODE-API-008",
      "type": "api_impl",
      "summary": "AuthController.oauth2Callback",
      "location": "src/auth/auth.controller.ts#L89"
    }
  ],
  "edges": [
    {"from": "PRD-FEAT-012", "to": "RD-REQ-005", "type": "implements"},
    {"from": "DD-API-008", "to": "PRD-FEAT-012", "type": "designs"},
    {"from": "CODE-API-008", "to": "DD-API-008", "type": "implemented_by"}
  ]
}
```

### **8.3 可追溯性标记规范**

**[ID: RD-TECH-TAG-001]**

#### **8.3.1 标记类型**

| 标记 | 格式 | 说明 | 示例 |
|------|------|------|------|
| **ID** | `[ID: PREFIX-XXX]` | 定义当前内容的唯一标识 | `[ID: RD-REQ-005]` |
| **Implements** | `[Implements: ID]` | 声明实现了上游需求 | `[Implements: RD-REQ-005]` |
| **Decomposes** | `[Decomposes: ID]` | 声明是上级需求的分解 | `[Decomposes: HL-AUTH-001]` |
| **Designs-for** | `[Designs-for: ID]` | 声明是某功能的设计 | `[Designs-for: PRD-FEAT-012]` |
| **Tests-for** | `[Tests-for: ID]` | 声明是某设计的测试 | `[Tests-for: DD-API-008]` |

#### **8.3.2 ID 前缀规范**

| 阶段 | 前缀 | 示例 |
|------|------|------|
| RD | `RD-REQ-` | RD-REQ-001 |
| PRD | `PRD-FEAT-`, `PRD-US-` | PRD-FEAT-012 |
| DD | `DD-API-`, `DD-DB-` | DD-API-008 |
| TD | `TD-CASE-` | TD-CASE-015 |
| Code | `CODE-API-`, `CODE-SERVICE-` | CODE-API-008 |
| Epic | `EPIC-` | EPIC-RD-001 |
| Task | `TASK-` | TASK-RD-GEN-001 |

---

## **九、验收标准 (Acceptance Criteria)**

### **9.1 功能验收**

**[ID: RD-AC-FUNC-001]**

| 功能 | 验收标准 |
|------|---------|
| **标记解析** | 准确率 > 95%<br>支持所有标记类型<br>处理边界情况 |
| **依赖图构建** | 检测循环依赖<br>100 万行代码 < 1 分钟<br>零 AI 成本 |
| **影响分析** | < 10 秒响应<br>$0 成本<br>准确识别下游节点 |
| **一致性检查** | 不一致检测准确率 > 85%<br>单需求 < 2 分钟<br>成本 < $0.05 |
| **任务管理** | 两层任务文件正常工作<br>无状态角色切换成功<br>任务复杂度检查准确 |

### **9.2 性能验收**

**[ID: RD-AC-PERF-001]**

已在 **NFR-2.1 ~ NFR-2.6** 中详细定义。

### **9.3 成本验收**

**[ID: RD-AC-COST-001]**

已在 **NFR-6.1 ~ NFR-6.5** 中详细定义。

---

## **十、总结与下一步 (Summary & Next Steps)**

### **10.1 核心价值**

**[ID: RD-SUMMARY-001]**

本需求文档定义了一个面向**超级个体**的 AI 增强型研发流程治理系统，核心特点：

1. ✅ **显式标记驱动**：100% 可靠的依赖图构建，支持复杂关系
2. ✅ **Generator-Reviewer 对模式**：每个阶段独立生成和评审，提高质量
3. ✅ **纯 CLI 架构**：无需后台服务，部署简单
4. ✅ **两层任务管理**：Epic 层 + 角色层，无状态设计
5. ✅ **极致性能与成本控制**：影响分析 < 10秒 $0，全项目检查 < 10分钟 < $2
6. ✅ **多 AI 后端支持**：当前支持 Claude Code，架构支持未来扩展

### **10.2 下一步工作**

**[ID: RD-NEXT-001]**

1. ✅ **编写 PRD（产品需求文档）**：详细描述每个 CLI 命令的功能特性和交互流程
2. ✅ **编写 DD（设计文档）**：定义系统架构、模块划分、数据结构、API 接口
3. ⏳ **编写 TD（测试文档）**：设计测试策略和测试用例
4. ⏸️ **原型验证 (MVP)**：优先实现标记解析器和影响分析功能
5. ⏸️ **Agent 提示词设计**：为 Generator 和 Reviewer Agent 设计提示词模板

---

**需求文档结束 (End of Requirements Document)**
