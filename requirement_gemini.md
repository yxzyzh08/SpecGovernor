# **📝 需求规格概要：AI增强型研发流程治理系统 (Gemini 修订版)**

> **版本说明 (v-gemini)**
> 
> 本文档是基于原始需求的修订版，核心调整在于采纳了“**显式可追溯性标记 (Explicit Traceability Tagging)**”策略，以替代原方案中依赖 AI 进行隐式依赖推断的技术路径。此修订旨在大幅提升依赖关系构建的**可靠性、速度和成本效益**，使整个系统架构更为稳健。

## **一、术语与缩略语解释 (Terminology and Glossary)**

| 术语/缩略语 | 英文全称 | 解释说明 |
| :---- | :---- | :---- |
| **SDLC** | Software Development Life Cycle | 软件开发生命周期，指从规划、设计、编码、测试到部署的整个软件开发过程。 |
| **RD** | Requirements Document | 需求文档。侧重于**用户和业务目标**，描述**系统应该做什么**。 |
| **PRD** | Product Requirements Document | 产品需求文档。侧重于**产品功能**，描述**实现哪些功能来满足需求**，包含用户故事、功能清单等。 |
| **DD** | Design Document | 软件设计文档。侧重于**技术实现**，描述**如何构建系统**，包含系统架构、模块划分、API 接口定义、数据库设计等。 |
| **TD** | Test Document | 测试文档。侧重于**验证标准**，描述**如何测试**系统，包含测试策略、测试用例等。 |
| **Agent** | AI Agent | 具有特定目标和能力的、基于 **Claude Code** 或 **Gemini CLI** 等大模型的软件智能体。 |
| **Generator Agent** | Generator Agent | 负责生成文档或代码的 AI Agent（如 RD Generator, PRD Generator）。 |
| **Reviewer Agent** | Reviewer Agent | 负责评审文档或代码的 AI Agent（如 RD Reviewer, PRD Reviewer）。每个文档阶段都有对应的 Generator-Reviewer 对。 |
| **流程编排器** | Orchestrator | 负责定义、管理和执行 AI Agent 流程的软件核心组件。负责状态流转、上下文注入和流程强制执行。在本系统中表现为一组 CLI 命令和脚本。 |
| **项目索引** | Project Index | 预先构建的项目结构化元数据，包含模块划分、依赖关系图、文档与代码的映射关系等。存储在 `.specgov/index/` 目录。 |
| **依赖图** | Dependency Graph | 描述 RD → PRD → DD → TD → Code 之间依赖关系的有向图，支持快速影响分析。 |
| **可追溯性标记** | Traceability Tag | **[新增]** 在文档或代码中嵌入的、用于明确声明依赖关系的结构化标记（如 `[Implements: RD-REQ-005]`），是构建高精度依赖图的基础。 |
| **RAG** | Retrieval-Augmented Generation | 检索增强生成。**【注：本方案已明确约束，不采用此技术作为知识库】**。 |

## **二、用户角色与使用场景 (User Roles & Usage Scenarios)**

### **2.1 目标用户：超级个体 (Super Individual)**

本系统的目标用户是**超级个体**，即一人承担多个研发角色的技术专家：

| 角色组成 | 职责范围 |
| :---- | :---- |
| **需求分析师** | 分析业务需求，编写和审阅需求文档 (RD) |
| **产品经理** | 定义产品功能，包含原型图设计，编写和审阅产品需求文档 (PRD) |
| **架构师** | 设计系统架构，编写和审阅设计文档 (DD) |
| **开发经理** | 管理开发流程，编写和审阅代码 |
| **测试经理** | 设计测试策略，编写和审阅测试文档 (TD) |
| **项目经理** | 统筹项目进度，管理变更和一致性 |

**典型画像**：独立开发者、技术创业者、小团队核心负责人

### **2.2 核心使用场景**

#### **场景 1：生成-评审对模式 (Generator-Reviewer Pattern)**

超级个体通过多个 AI 客户端并行工作，每个文档阶段都采用"生成-评审"对模式：

```
RD 阶段：
  客户端 1: RD Generator Agent（生成需求文档，并为每个需求分配唯一ID标记，如 `[ID: RD-REQ-001]`）
  客户端 2: RD Reviewer Agent（评审需求文档）
  客户端 1: 根据评审结果修订文档

PRD 阶段：
  客户端 3: PRD Generator Agent（基于 RD 生成产品文档，并嵌入上游ID标记，如 `[Implements: RD-REQ-001]`）
  客户端 4: PRD Reviewer Agent（评审产品文档）

DD/TD/Code 阶段：依此类推...
```

**价值**：Generator 和 Reviewer 使用不同的 AI 实例，避免自我审查偏差，提高文档质量。

#### **场景 2：模块并行处理**

针对大型项目（如 50-100 万行代码），超级个体可以并行处理不同模块：

```
客户端 1: 处理用户模块的一致性检查
客户端 2: 处理订单模块的一致性检查
客户端 3: 处理支付模块的一致性检查
```

**价值**：将全项目验证时间从 30 分钟降低到 5-10 分钟。

#### **场景 3：影响分析与变更传播**

超级个体修改某个文档后，系统快速分析影响范围：

```
超级个体: 修改 RD 第 2.3 节（将认证方式从用户名密码改为 OAuth2）
系统: specgov analyze:impact --changed=docs/rd.md

输出:
  受影响的文档：
  - PRD 第 3.2 节（用户登录功能）
  - DD 第 4.1 节（认证服务设计）
  - TD 第 5.1 节（登录测试用例）
  受影响的代码：
  - src/auth/auth.service.ts
  - src/user/user.controller.ts

超级个体: 了解影响范围后，依次重新生成和评审受影响的文档
```

#### **场景 4：代码提交前的全链路验证**

超级个体完成代码开发后，提交前做最终验证：

```
超级个体: specgov check:consistency --scope=full

系统:
  [检查中] UserModule... ✓
  [检查中] OrderModule... ✓
  [检查中] PaymentModule... ✗

  发现 3 处不一致：
  1. DD 设计的 API 是 POST /payments，代码实现是 PUT /payments
  2. PRD 要求支持分页，代码未实现
  3. RD 禁止存储明文密钥，代码未加密

超级个体: 根据报告修复问题后重新验证
```

### **2.3 系统集成方式**

- **AI 后端**：支持 Claude Code、Gemini CLI 等多种大模型 CLI 工具
- **部署形态**：纯 CLI 工具，无需独立后台服务
- **状态管理**：通过 Git 仓库中的 `.specgov/` 目录管理流程状态和索引
- **触发方式**：超级个体主动调用 CLI 命令（半自动化），而非完全自动化的后台监听

### **2.4 项目规模支持**

- **目标规模**：中小型项目，代码量 ≤ 100 万行
- **典型项目**：10-20 个模块，每个模块 5-10 万行代码
- **性能保证**：通过索引机制和模块化检查，确保大型项目的可用性

## **三、项目目标 (Project Goals)**

| ID | 目标描述 | 达成标准 |
| :---- | :---- | :---- |
| **G-1** | **流程规范化与自动化** | 将人为定义的严格 SDLC 流程转化为可由软件工具和 AI Agent 自动执行的流程。通过 CLI 命令实现半自动化，超级个体主动控制关键节点。 |
| **G-2** | **文档代码持续一致性** | 通过"生成-评审"对机制和一致性检查，实现 RD/PRD/DD/TD/Code 之间的高质量一致性。不一致检测准确率 ≥ 85%（基于人工标注对比）。 |
| **G-3** | **提升研发效率** | 利用 AI Agent 自动生成文档、代码和测试用例。量化目标：文档生成时间减少 60%，评审时间减少 50%。 |
| **G-4** | **支持中小型复杂项目** | 系统需能应对代码量在 100 万行以下的中型复杂项目。性能保证：影响分析 < 10 秒，模块级一致性检查 < 2 分钟，全项目检查 < 10 分钟（10 个模块并行）。 |
| **G-5** | **成本可控** | 控制 AI 调用成本。预期：日常影响分析几乎免费（基于索引），单模块检查 < $0.05，全项目检查 < $2。 |

## **四、功能需求 (Functional Requirements - FR)**

### **4.1 文档与代码生成**

| ID | 需求描述 | 关键交互组件 |
| :---- | :---- | :---- |
| **FR-1.1** | 系统需支持**生成-评审对模式**：每个文档阶段都有独立的 Generator Agent 和 Reviewer Agent。Generator 基于上游文档生成新文档，Reviewer 评审生成质量并提出修改建议。 | RD/PRD/DD/TD Generator & Reviewer Agent 对 |
| **FR-1.2** | Generator Agent 的输入必须包含：(1) 上游文档内容（由编排器精准裁剪），(2) 生成提示词模板，(3) 项目上下文元数据。输出必须是结构化格式（Markdown + YAML Front Matter），**并包含指向其上游依赖的显式可追溯性标记**。 | 文档生成 Agent 族, 流程编排器 |
| **FR-1.3** | Reviewer Agent 的输入必须包含：(1) 待评审文档，(2) 上游文档（对照），(3) 评审检查清单。输出必须是结构化的评审报告（JSON 格式），包含问题列表、严重程度、建议修改。 | 文档评审 Agent 族 |
| **FR-1.4** | 代码与测试 Agent 需能基于 DD 和 PRD 的上下文，生成满足规范的测试用例和代码片段。同样采用 Generator-Reviewer 对模式，并**在代码注释中嵌入可追溯性标记**。 | 代码与测试 Agent 族 |

### **4.2 项目索引与依赖管理**

| ID | 需求描述 | 关键交互组件 |
| :---- | :---- | :---- |
| **FR-2.1** | 系统需提供**索引构建命令**（如 `specgov index:build`），用于**解析项目中的显式可追溯性标记**（如 `[Implements: RD-REQ-005]`），并构建结构化索引。索引内容包括：(1) 模块划分，(2) 文档章节映射，(3) 代码符号（API、类、函数），(4) 依赖关系图。 | 索引构建服务 (高速文本解析器) |
| **FR-2.2** | 索引需持久化到 `.specgov/index/` 目录，包含以下文件：`modules.json`（模块列表），`dependency-graph.json`（依赖图），`rd-map.json` / `prd-map.json` / `dd-map.json`（文档映射），`code-map.json`（代码符号映射）。 | 结构化文档管理服务 |
| **FR-2.3** | 系统需支持**增量索引更新**：当文档或代码变更时（通过 Git diff 检测），只重新解析变更文件中的标记并更新索引，避免全量重建。 | 索引更新服务 |

### **4.3 影响分析与一致性检查**

| ID | 需求描述 | 关键交互组件 |
| :---- | :---- | :---- |
| **FR-3.1** | 系统需提供**影响分析命令**（如 `specgov analyze:impact --changed=<file>`），基于**高精度**的依赖图快速定位受影响的下游文档和代码。响应时间 < 10 秒，无需调用 AI（纯图查询）。 | 影响分析服务 |
| **FR-3.2** | 影响分析输出必须是结构化的 JSON 格式，包含：`changed`（变更项列表），`affected`（受影响项列表，含文档位置和代码位置），`recommendation`（建议的后续操作）。 | 影响分析服务 |
| **FR-3.3** | 系统需提供**一致性检查命令**（支持多种作用域）：<br>- `--scope=<ID>`：检查单个需求/功能的全链路一致性<br>- `--scope=<module>`：检查单个模块的一致性<br>- `--scope=full`：检查全项目一致性（并行分解为多个模块检查） | 一致性检查服务 |
| **FR-3.4** | 一致性检查的实现策略：<br>(1) 基于**100%可靠的**索引定位相关依赖链<br>(2) 只加载依赖链涉及的文档和代码片段（通常 < 5000 行）<br>(3) 构造精准上下文发送给 AI Agent<br>(4) 输出结构化差异报告（JSON 格式） | 一致性守护 Agent, 流程编排器 |
| **FR-3.5** | 一致性检查需支持两种模式：<br>**快速模式**（用于影响分析）：基于元数据和关键词匹配，不做深度语义分析，< 10 秒<br>**深度模式**（用于最终验证）：深度语义分析，逐模块检查，5-10 分钟 | 一致性守护 Agent |

### **4.4 变更触发与流程控制**

| ID | 需求描述 | 关键交互组件 |
| :---- | :---- | :---- |
| **FR-4.1** | 系统需支持**主动触发检查**（超级个体手动调用 CLI 命令），而非被动的实时监听。可通过 Git Hooks 集成实现半自动化触发。 | 流程编排器 |
| **FR-4.2** | 系统需提供**状态管理机制**：通过 `.specgov/state.json` 记录当前流程状态、各文档的版本和状态、上次检查结果等。每次 CLI 命令执行前读取状态，执行后更新状态。 | 流程编排器, 状态管理服务 |
| **FR-4.3** | （可选）流程编排器可根据校验结果，通过集成连接器在外部工具（如 Jira）中创建同步任务，或通过 Git Hooks 阻塞不符合规范的提交。 | 流程编排器, 集成连接器 |

## **五、非功能需求与约束 (Non-Functional Requirements & Constraints - NFR)**

### **5.1 架构约束**

| ID | 约束描述 | 对设计的影响 |
| :---- | :---- | :---- |
| **NFR-1.1** | **禁止使用 RAG/向量数据库**：**禁止**使用统一的向量数据库 (RAG/Vector DB) 作为知识持久化层。 | 流程编排器必须通过**项目索引 + 依赖图**实现上下文检索和拼接。 |
| **NFR-1.2** | **纯 CLI 架构**：系统必须以纯 CLI 工具形式实现，无需独立的后台服务或数据库。状态通过文件系统（`.specgov/` 目录）管理。 | 简化部署和运维，但需要设计良好的文件状态管理机制。 |
| **NFR-1.3** | **多 AI 后端支持**：系统必须支持多种 AI CLI 工具（Claude Code、Gemini CLI 等），通过统一的接口调用。 | 需要设计抽象的 AI 调用层，支持配置切换不同后端。 |

### **5.2 性能需求**

| ID | 性能指标 | 验收标准 |
| :---- | :---- | :---- |
| **NFR-2.1** | **影响分析响应时间** | < 10 秒（基于索引的纯图查询，不调用 AI） |
| **NFR-2.2** | **单点一致性检查** | < 2 分钟（检查单个需求/功能的全链路一致性，上下文 < 5K tokens） |
| **NFR-2.3** | **模块级一致性检查** | < 2 分钟（检查单个模块，上下文 < 20K tokens） |
| **NFR-2.4** | **全项目一致性检查** | < 10 分钟（10 个模块并行检查，总上下文 < 200K tokens） |
| **NFR-2.5** | **索引构建时间** | < 1 分钟（100 万行代码项目，纯解析，无 AI 调用） |
| **NFR-2.6** | **增量索引更新** | < 5 秒（单个文件的重新解析） |

### **5.3 上下文管理**

| ID | 约束描述 | 对设计的影响 |
| :---- | :---- | :---- |
| **NFR-3.1** | 流程中的所有 AI Agent 必须通过**流程编排器**提供的**精准裁剪和拼接**的上下文来工作。 | 编排器必须具备基于索引的上下文裁剪能力：<br>(1) 根据依赖图定位相关节点<br>(2) 只加载相关文档和代码片段<br>(3) 控制上下文大小在 AI 窗口范围内 |
| **NFR-3.2** | 单次 AI 调用的上下文大小必须控制在合理范围内：<br>- 快速检查：< 5K tokens<br>- 深度检查：< 20K tokens<br>- 极限情况：< 50K tokens | 通过精准的依赖链定位和内容裁剪实现。如果超出限制，必须分解为多个子任务。 |

### **5.4 Agent 架构**

| ID | 约束描述 | 对设计的影响 |
| :---- | :---- | :---- |
| **NFR-4.1** | 必须采用**生成-评审对模式**：每个文档阶段都有独立的 Generator Agent 和 Reviewer Agent，使用不同的 AI 实例，避免自我审查偏差。 | 需要为每个阶段定义两套提示词模板和 Agent 配置。 |
| **NFR-4.2** | 必须采用**去中心化、多 Agent 族**的结构，支持同一文档层级拆分为多个子任务 Agent（如 PRD-A, PRD-B）。 | 需保证 Agent 间的接口协议（输入/输出 Schema）清晰、稳定。 |
| **NFR-4.3** | 所有关键的 AI Agent 输出（如影响分析报告、差异报告、评审报告）必须是**结构化数据**（JSON/YAML），以便编排器进行后续处理。 | 提示词中必须明确要求结构化输出，并进行格式验证。 |

### **5.5 可靠性与容错**

| ID | 约束描述 | 对设计的影响 |
| :---- | :---- | :---- |
| **NFR-5.1** | 流程的关键节点必须设置**人工仲裁 (Human-in-the-Loop)** 机制：当 AI 评审发现严重问题、或一致性检查失败率 > 20% 时，必须提示超级个体介入。 | CLI 命令需支持交互式确认和人工决策。 |
| **NFR-5.2** | 所有 AI 调用必须有**重试机制**：API 调用失败时自动重试最多 3 次，超时时间 120 秒。 | 需要封装统一的 AI 调用层，处理异常和重试。 |
| **NFR-5.3** | 系统必须支持**操作回滚**：通过 Git 版本控制，所有文档和索引变更都可以回滚到历史版本。 | 利用 Git 的天然版本控制能力，无需额外实现。 |

### **5.6 成本控制**

| ID | 约束描述 | 验收标准 |
| :---- | :---- | :---- |
| **NFR-6.1** | **影响分析成本** | 几乎免费（基于索引的纯图查询，不调用 AI） | $0 |
| **NFR-6.2** | **单点一致性检查成本** | 上下文 < 5K tokens | < $0.02 (Claude) 或 < $0.01 (Gemini) |
| **NFR-6.3** | **模块级检查成本** | 上下文 < 20K tokens | < $0.05 |
| **NFR-6.4** | **全项目检查成本** | 10 个模块，总上下文 < 200K tokens | < $2 |
| **NFR-6.5** | **索引构建成本** | 一次性操作，纯文本解析 | $0 |

## **六、关键交付流程：生成-评审-验证机制**

超级个体通过 CLI 命令主动驱动以下流程，系统通过**流程编排器**协调各 Agent 的执行：

### **6.1 标准文档生成流程（以 RD 为例）**

| 步骤 | CLI 命令 | 执行流程 | 涉及 Agent/服务 |
| :---- | :---- | :---- |
| **1. 生成** | `specgov rd:generate` | (1) 编排器读取项目上下文<br>(2) 调用 RD Generator Agent 生成初稿，**并嵌入唯一ID标记**<br>(3) 保存到 `docs/rd.md`<br>(4) 更新 `.specgov/state.json` | RD Generator Agent<br>流程编排器 |
| **2. 评审** | `specgov rd:review` | (1) 编排器读取生成的 RD<br>(2) 调用 RD Reviewer Agent 评审<br>(3) 输出结构化评审报告（JSON）<br>(4) 如发现严重问题，提示人工介入 | RD Reviewer Agent<br>流程编排器 |
| **3. 修订** | `specgov rd:revise` | (1) 编排器读取评审报告<br>(2) 调用 RD Generator Agent 根据评审意见修订<br>(3) 更新文档和状态 | RD Generator Agent<br>流程编排器 |
| **4. 索引更新** | `specgov index:update --scope=rd` | (1) **高速解析** RD 文档中的标记<br>(2) 更新依赖图中的 RD 节点<br>(3) 保存到 `.specgov/index/` | 索引更新服务 (解析器) |

**PRD/DD/TD/Code 阶段流程类似**，都遵循"生成 → 评审 → 修订 → 索引更新"的模式。

### **6.2 变更传播与影响分析流程**

| 触发场景 | CLI 命令 | 执行流程 | 输出 |
| :---- | :---- | :---- |
| **超级个体修改 RD** | `specgov analyze:impact --changed=docs/rd.md` | (1) Git diff 识别变更内容<br>(2) **从高精度依赖图中**查询下游节点<br>(3) 返回受影响的 PRD/DD/TD/Code 列表 | JSON 格式的影响范围报告 |
| **超级个体决定更新下游** | `specgov prd:regenerate --based-on=rd` | (1) 读取变更后的 RD<br>(2) 重新生成 PRD（**并自动嵌入新的可追溯性标记**）<br>(3) 自动触发 PRD 评审 | 更新后的 PRD 文档 |

### **6.3 一致性检查流程**

| 检查场景 | CLI 命令 | 执行流程 | 性能要求 |
| :---- | :---- | :---- |
| **检查单个需求的一致性** | `specgov check:consistency --scope=RD-REQ-005` | (1) 基于**高精度依赖图**定位依赖链<br>(2) 只加载相关文档和代码片段（< 5000 行）<br>(3) 调用一致性守护 Agent 深度分析<br>(4) 输出差异报告 | < 2 分钟 |
| **检查单个模块的一致性** | `specgov check:consistency --scope=UserModule` | (1) 加载该模块相关的所有文档和代码<br>(2) 调用一致性守护 Agent<br>(3) 输出差异报告 | < 2 分钟 |
| **全项目一致性检查** | `specgov check:consistency --scope=full` | (1) 分解为 10 个模块检查任务<br>(2) 超级个体启动多个 AI 客户端并行执行<br>(3) 汇总所有模块的差异报告 | < 10 分钟 |
| **代码提交前验证** | `specgov check:pre-commit` | (1) 检测本次提交涉及的代码文件<br>(2) 只检查相关模块的一致性<br>(3) 如发现不一致，阻止提交（通过 Git Hook） | < 2 分钟 |

### **6.4 完整的端到端流程示例**

**场景**：超级个体开发一个新功能（用户 OAuth2 登录）

```bash
# 1. 生成需求文档，自动包含ID
$ specgov rd:generate --feature="用户OAuth2登录"
生成完成: docs/rd.md (内容包含 "[ID: RD-REQ-005] ...")

# 2. 评审需求文档
$ specgov rd:review
评审报告: .specgov/rd/review-report.json

# 3. 修订 RD
$ specgov rd:revise
修订完成: docs/rd.md (v2)

# 4. 更新索引 (通过解析标记，秒级完成)
$ specgov index:update --scope=rd
索引更新完成

# 5. 基于 RD 生成 PRD，自动包含Implements标记
$ specgov prd:generate --based-on=rd
生成完成: docs/prd.md (内容包含 "[Implements: RD-REQ-005] ...")

# 6. 评审 PRD
$ specgov prd:review
评审报告: .specgov/prd/review-report.json

# 7. 继续生成 DD, TD, Code (过程中自动传递和嵌入标记)
...

# 8. 编写代码后，提交前检查一致性
$ specgov check:consistency --scope=UserModule
检查完成:
  ✓ RD ↔ PRD 一致
  ✓ PRD ↔ DD 一致
  ✗ DD ↔ Code 发现 1 处不一致
    - DD 设计的 API 是 POST /auth/oauth2，代码实现是 GET

# 9. 修复代码后重新检查
$ specgov check:consistency --scope=UserModule
检查完成: 全部一致 ✓

# 10. 提交代码
$ git commit -m "feat: add OAuth2 login"
[pre-commit hook 自动触发 specgov check:pre-commit]
一致性检查通过 ✓
提交成功
```

## **七、技术实现策略 (Technical Implementation Strategy)**

### **7.1 核心技术挑战与解决方案**

#### **挑战：如何在 100 万行代码的项目中进行一致性检查？**

**问题分析**：
- Claude Code / Gemini CLI 的上下文窗口有限（200K - 2M tokens）
- 100 万行代码约需 750 万 tokens，远超上下文窗口
- 直接加载所有代码进行检查是不可行的

**解决方案：显式标记 + 解析构建 + 按需加载**

```
核心思想：不依赖 AI 推断依赖关系，而是通过在文档和代码中嵌入显式标记，让依赖关系成为可直接解析的结构化数据。

实现步骤：
1. 在文档/代码中嵌入可追溯性标记 (如 `[Implements: RD-REQ-005]`)。
2. 通过高速解析器（非 AI）构建项目索引和 100% 可靠的依赖图。
3. 基于精准的依赖图进行影响分析和依赖链定位。
4. 只加载相关的文档和代码片段，将上下文控制在 AI 窗口范围内（< 20K tokens）。
```

### **7.2 项目索引机制**

#### **7.2.1 索引结构设计**

```
项目目录结构：
my-project/
├── .specgov/                      # 系统工作目录
│   ├── state.json                 # 流程状态
│   ├── index/                     # 项目索引
│   │   ├── modules.json           # 模块列表
│   │   ├── dependency-graph.json  # 依赖关系图
│   │   ├── rd-map.json            # RD 需求映射
│   │   ├── prd-map.json           # PRD 功能映射
│   │   ├── dd-map.json            # DD 设计映射
│   │   ├── code-map.json          # 代码符号映射
│   ├── rd/                        # RD 相关输出
│   │   ├── generated.md
│   │   └── review-report.json
│   ├── prd/
│   ├── dd/
│   └── consistency-reports/       # 一致性检查报告
├── docs/                          # 文档目录
│   ├── rd.md
│   ├── prd.md
│   └── dd.md
└── src/                           # 代码目录
```

#### **7.2.2 依赖图示例 (基于显式标记)**

```json
// .specgov/index/dependency-graph.json
{
  "nodes": [
    {
      "id": "RD-REQ-005",
      "type": "requirement",
      "summary": "用户必须支持OAuth2登录",
      "location": "docs/rd.md#L42"
    },
    {
      "id": "PRD-FEAT-012",
      "type": "feature",
      "summary": "实现OAuth2登录流程",
      "location": "docs/prd.md#L128"
    },
    {
      "id": "DD-API-008",
      "type": "api_design",
      "summary": "POST /auth/oauth2/callback",
      "location": "docs/dd.md#L234"
    },
    {
      "id": "CODE-API-008",
      "type": "api_impl",
      "summary": "AuthController.oauth2Callback",
      "location": "src/auth/auth.controller.ts#L89"
    }
  ],
  "edges": [
    // 这些边是通过解析 "[Implements: RD-REQ-005]" 等标记生成的
    {"from": "RD-REQ-005", "to": "PRD-FEAT-012", "type": "implements"},
    {"from": "PRD-FEAT-012", "to": "DD-API-008", "type": "designs"},
    {"from": "DD-API-008", "to": "CODE-API-008", "type": "implemented_by"}
  ]
}
```

#### **7.2.3 索引构建流程 (修订后)**

```python
# 伪代码：基于标记解析的索引构建逻辑 (非 AI)
import re
import os

TAG_REGEX = re.compile(r"[(ID|Implements|Designs-for|Tests-for):\s*([\w-]+)]")

def build_index(project_path):
    nodes = []
    edges = []

    # 1. 遍历所有相关文件
    for root, _, files in os.walk(project_path):
        for file in files:
            if not (file.endswith(".md") or file.endswith(".ts")):
                continue
            
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                for line_num, line in enumerate(f, 1):
                    # 2. 使用正则表达式查找所有标记
                    for match in TAG_REGEX.finditer(line):
                        tag_type, tag_id = match.groups()
                        
                        # 假设当前文件/符号的ID可以通过其他方式获得
                        current_id = get_id_for_location(file_path, line_num)

                        if tag_type == "ID":
                            # 定义一个新节点
                            nodes.append({"id": tag_id, "location": f"{file_path}#L{line_num}"})
                        else:
                            # 定义一条边
                            relation_map = {
                                "Implements": "implements",
                                "Designs-for": "designs",
                                "Tests-for": "tested_by"
                            }
                            edges.append({
                                "from": tag_id, 
                                "to": current_id, 
                                "type": relation_map.get(tag_type)
                            })

    # 3. 构建并保存依赖图
    dependency_graph = {"nodes": nodes, "edges": edges}
    save_json(dependency_graph, ".specgov/index/dependency-graph.json")

# 性能：纯文本解析，极快
# 成本：$0 (不调用 AI)
```

### **7.3 一致性检查实现**

#### **7.3.1 影响分析（快速模式，不调用 AI）**

```python
# 伪代码：影响分析逻辑

def analyze_impact(changed_file):
    # 1. 识别变更的节点 (通过解析文件中的ID标记)
    changed_nodes = identify_changed_nodes(changed_file)

    # 2. 基于高精度依赖图查询下游节点（图遍历）
    affected_nodes = []
    for node in changed_nodes:
        downstream = traverse_graph(node, direction="downstream")
        affected_nodes.extend(downstream)

    # 3. 返回影响报告
    return {
        "changed": [format_node(n) for n in changed_nodes],
        "affected": [format_node(n) for n in affected_nodes],
        "recommendation": generate_recommendation(affected_nodes)
    }

# 性能：纯图查询，< 10 秒
# 成本：$0（不调用 AI）
```

#### **7.3.2 一致性检查（深度模式，调用 AI）**

```python
# 伪代码：一致性检查逻辑

def check_consistency(scope):
    # 1. 基于 scope 和高精度依赖图定位依赖链
    if scope == "RD-REQ-005":
        dependency_chain = get_dependency_chain("RD-REQ-005")
    # ...

    # 2. 加载依赖链涉及的内容（精准裁剪）
    context = ""
    for node in dependency_chain:
        content = load_content(node.location)
        context += f"\n【{node.type} - {node.id}】\n{content}\n"

    # 3. 构造提示词并调用 AI
    prompt = f"""
请检查以下文档和代码的一致性：

{context}

请检查：
1. PRD 是否忠实反映了 RD 的需求？
2. DD 的设计是否满足 PRD 的功能要求？
3. 代码实现是否符合 DD 的设计？
4. 列出所有不一致之处，输出 JSON 格式。
"""
    response = call_ai_agent(prompt)

    # 4. 解析并返回差异报告
    return parse_consistency_report(response)

# 性能：< 2 分钟（单模块）
# 成本：< $0.05（上下文 < 20K tokens）
```

### **7.3.3 上下文裁剪策略**

#### **关键原则**：

1. **精准定位**：基于**100%可靠的**依赖图，只加载相关节点
2. **分层加载**：优先加载摘要，按需加载详细内容
3. **控制大小**：单次 AI 调用上下文 < 20K tokens（约 5000 行代码）
4. **分而治之**：大型检查任务分解为多个小任务

---

## **八、总结与下一步**

本需求文档（Gemini 修订版）定义了一个面向**超级个体**的 AI 增强型研发流程治理系统，其核心策略经过优化，特点更加突出：

1. ✅ **显式标记驱动的一致性**：通过在文档和代码中嵌入**可追溯性标记**，实现 100% 可靠的依赖图构建，为整个系统提供了坚实的基础。
2. ✅ **生成-评审对模式**：每个阶段都有独立的 Generator 和 Reviewer Agent，提高质量。
3. ✅ **纯 CLI 架构**：无需后台服务，部署简单，适合超级个体使用。
4. ✅ **极致的成本与性能控制**：通过将依赖发现转为零成本的本地解析，并结合精准的上下文裁剪，严格控制 AI 调用成本和响应时间。
5. ✅ **多 AI 后端支持**：灵活切换 Claude Code、Gemini CLI 等工具。

**建议的下一步工作**：

1. **编写 PRD（产品需求文档）**：详细描述每个 CLI 命令的功能特性和交互流程。
2. **设计 DD（软件设计文档）**：定义系统架构、模块划分、数据结构、API 接口。
3. **原型验证 (MVP)**：优先实现核心的**标记解析器** (`index:build`) 和**影响分析** (`analyze:impact`) 功能，以验证新策略的可行性。
4. **Agent 提示词设计**：为 Generator 和 Reviewer Agent 设计高质量的提示词模板，**强调对可追溯性标记的生成与处理**。
