# **📦 SpecGovernor 产品需求文档 (PRD)**

> **版本**: v1.0-gemini
> **基于**: requirement_gemini.md (v-gemini)
> **创建日期**: 2025-11-16
> **产品定位**: AI 增强型研发流程治理工具 - 基于显式可追溯性标记

---

## **可追溯性声明**

本文档实现以下需求文档的功能需求：
- [Implements: RD-FR-1.1] 生成-评审对模式
- [Implements: RD-FR-2.1] 项目索引构建
- [Implements: RD-FR-3.1] 影响分析
- [Implements: RD-FR-3.3] 一致性检查
- [Implements: RD-FR-4.1] 主动触发检查

---

## **一、产品概述**

### **1.1 产品愿景**

**[ID: PRD-VISION-001]**

SpecGovernor 是一个专为**超级个体**设计的 CLI 工具，通过**显式可追溯性标记**和 **AI Agent 协作**，实现文档-代码全链路一致性管理，让一人团队也能高效管理复杂项目。

**核心价值主张：**
- 🎯 **100% 可靠追溯**：基于显式标记，无需依赖 AI 推断
- 🔄 **双重质量保证**：Generator-Reviewer 对模式


---

### **1.2 目标用户画像**

**[ID: PRD-USER-001] [Implements: RD-2.1]**

| 用户类型 | 典型场景 | 痛点 |
|---------|---------|------|
| **独立开发者** | 开发 SaaS 产品 | 文档与代码不一致，需求变更难追踪 |
| **技术创业者** | MVP 快速迭代 | 一人身兼多职，文档成本高 |
| **小团队 Tech Lead** | 管理 5-10 人团队 | 需要规范流程但没有专职 PM/QA |

---

### **1.3 产品架构**

**[ID: PRD-ARCH-001]**

```
SpecGovernor CLI
├── 项目初始化 (specgov init)
├── 五阶段文档工作流
│   ├── RD (需求文档)
│   ├── PRD (产品文档)
│   ├── DD (设计文档)
│   ├── TD (测试文档)
│   └── Code (代码)
├── 核心引擎
│   ├── 标记解析器
│   ├── 依赖图构建
│   ├── 影响分析引擎
│   └── 一致性检查引擎
└── AI Agent 集成
    ├── Generator Agents (生成器)
    └── Reviewer Agents (评审器)
```

---

## **二、用户故事 (User Stories)**

### **2.1 Epic 1：项目初始化**

**[ID: PRD-EPIC-001] [Implements: RD-FR-4.2]**

> **作为** 超级个体开发者
> **我希望** 能够快速初始化 SpecGovernor 项目
> **以便** 开始使用文档-代码一致性管理

**子故事：**

#### **US-001.1：初始化项目结构**
**[ID: PRD-US-001.1]**

```bash
# 用户输入
$ specgov init my-ecommerce --ai claude-code

# 系统输出
✓ 项目初始化完成
✓ AI 后端：claude-code
✓ 目录结构：
  .specgov/
    ├── config.yml
    ├── state.json
    ├── index/
    │   ├── modules.json
    │   └── dependency-graph.json
    └── artifacts/
        ├── rd.md
        ├── prd.md
        ├── dd.md
        └── td.md

📚 下一步：
  1. 编辑 .specgov/index/modules.json 定义模块
  2. 运行 specgov rd:generate 开始生成需求文档
```

**验收标准：**
- ✅ 创建 `.specgov/` 目录及所有子目录
- ✅ 生成默认配置文件
- ✅ 支持 `--ai` 参数选择后端（claude-code, gemini-cli 等）
- ✅ 初始化 Git 仓库（如果不存在）
- ✅ 输出友好的下一步指引

---

### **2.2 Epic 2：文档生成-评审-修订循环**

**[ID: PRD-EPIC-002] [Implements: RD-FR-1.1, RD-FR-1.2, RD-FR-1.3]**

> **作为** 超级个体开发者
> **我希望** 通过 AI Agent 自动生成高质量文档
> **并且** 通过独立的 Reviewer Agent 进行评审
> **以便** 避免自我审查偏差，提高文档质量

---

#### **US-002.1：生成需求文档 (RD)**
**[ID: PRD-US-002.1]**

```bash
# 用户输入
$ specgov rd:generate --input=user-stories/oauth2-login.md

# 系统输出
🤖 RD Generator Agent 正在工作...

  读取输入：user-stories/oauth2-login.md
  调用 AI：claude-code (claude-sonnet-4)
  生成中...

✓ 生成完成：.specgov/artifacts/rd.md

📄 预览：
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 需求文档 (RD)

## 1. 用户认证需求
[ID: RD-AUTH-001]

### 1.1 OAuth2 登录
[ID: RD-REQ-005] [Decomposes: RD-AUTH-001]

系统必须支持用户通过 OAuth2 进行登录，支持的
提供商包括 Google、GitHub、Microsoft...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 统计：
  - 生成的需求数量：3
  - 可追溯性标记：5 个 [ID: XXX]
  - 依赖关系标记：2 个 [Decomposes: XXX]
  - 生成时间：45 秒
  - 成本：$0.15

📚 下一步：
  运行 specgov rd:review 进行评审
```

**验收标准：**
- ✅ 支持 `--input` 参数加载用户输入
- ✅ 调用 Generator Agent 生成 Markdown 文档
- ✅ **自动嵌入可追溯性标记**（[ID: XXX]）
- ✅ 支持层次化需求（[Decomposes: XXX]）
- ✅ 输出统计信息（标记数量、成本、时间）
- ✅ 保存到 `.specgov/artifacts/rd.md`

---

#### **US-002.2：评审需求文档 (RD)**
**[ID: PRD-US-002.2]**

```bash
# 用户输入（使用不同的 AI 后端）
$ specgov rd:review --ai gemini-cli

# 系统输出
🔍 RD Reviewer Agent 正在评审...

  读取文档：.specgov/artifacts/rd.md
  调用 AI：gemini-cli (gemini-1.5-pro)
  评审中...

✓ 评审完成：.specgov/reviews/rd-review.json

📋 评审报告：
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
总结：
  ✓ 整体质量：良好
  ⚠️  发现 2 个建议，0 个严重问题

问题清单：
  1. [建议] RD-REQ-005 (OAuth2 登录)
     - 位置：第 1.1 节
     - 问题：缺少具体的错误处理要求
     - 建议：补充登录失败、token 过期等场景

  2. [建议] 可追溯性标记
     - 位置：第 2.3 节
     - 问题：缺少 [ID: XXX] 标记
     - 建议：为"数据安全需求"添加标记

可追溯性检查：
  ✓ 所有主要需求都有 [ID: XXX] 标记
  ✓ [Decomposes: XXX] 引用的父 ID 都存在
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 下一步：
  运行 specgov rd:revise 根据评审意见修订
```

**验收标准：**
- ✅ 调用 Reviewer Agent（可指定不同 AI 后端）
- ✅ 输出结构化评审报告（JSON 格式）
- ✅ **检查可追溯性标记的完整性和正确性**
- ✅ 区分问题等级（严重/警告/建议）
- ✅ 提供具体的修改建议
- ✅ 保存到 `.specgov/reviews/rd-review.json`

---

#### **US-002.3：修订需求文档 (RD)**
**[ID: PRD-US-002.3]**

```bash
# 用户输入
$ specgov rd:revise

# 系统输出
🔧 RD Generator Agent 正在修订...

  读取原文档：.specgov/artifacts/rd.md
  读取评审报告：.specgov/reviews/rd-review.json
  调用 AI：claude-code
  修订中...

✓ 修订完成：.specgov/artifacts/rd.md (v2)

📝 变更摘要：
  - 修复问题 1：补充了 OAuth2 错误处理场景
  - 修复问题 2：为第 2.3 节添加了 [ID: RD-SEC-001]

📚 下一步：
  运行 specgov index:update 更新索引
```

**验收标准：**
- ✅ 基于评审报告自动修订
- ✅ 保留原文档的可追溯性标记
- ✅ 输出变更摘要
- ✅ 版本号递增（v1 → v2）

---

### **2.3 Epic 3：索引构建与依赖图管理**

**[ID: PRD-EPIC-003] [Implements: RD-FR-2.1, RD-FR-2.2, RD-FR-2.3]**

> **作为** 超级个体开发者
> **我希望** 系统能够自动解析文档中的可追溯性标记
> **并构建** 高精度的依赖关系图
> **以便** 快速进行影响分析和一致性检查

---

#### **US-003.1：构建项目索引**
**[ID: PRD-US-003.1]**

```bash
# 用户输入
$ specgov index:build

# 系统输出
🔨 构建项目索引...

  扫描项目文件...
    ✓ docs/rd.md
    ✓ docs/prd.md
    ✓ docs/dd.md
    ✓ src/auth/auth.controller.ts
    ✓ src/user/user.service.ts
    (扫描 125 个文件)

  解析可追溯性标记...
    ✓ 发现 45 个 [ID: XXX] 标记
    ✓ 发现 38 个 [Implements: XXX] 标记
    ✓ 发现 12 个 [Decomposes: XXX] 标记

  构建依赖图...
    ✓ 创建 45 个节点
    ✓ 创建 50 条边
    ✓ 检测到 0 个循环依赖

✓ 索引构建完成：.specgov/index/dependency-graph.json

📊 统计：
  - 需求 (RD): 15 个
  - 功能 (PRD): 12 个
  - 设计 (DD): 10 个
  - 测试 (TD): 5 个
  - 代码 (Code): 3 个

⏱️  耗时：8 秒（100 万行代码项目）
💰 成本：$0（本地解析，无 AI 调用）

📚 下一步：
  运行 specgov analyze:impact 进行影响分析
```

**验收标准：**
- ✅ 扫描所有 Markdown 和代码文件
- ✅ 正则表达式解析所有标记类型
- ✅ 构建节点和边的数据结构
- ✅ 检测循环依赖并警告
- ✅ 保存到 `.specgov/index/dependency-graph.json`
- ✅ **性能：100 万行代码 < 1 分钟**
- ✅ **成本：$0（本地计算）**

---

#### **US-003.2：增量更新索引**
**[ID: PRD-US-003.2]**

```bash
# 用户修改文档后
$ specgov index:update --scope=rd

# 系统输出
🔄 增量更新索引...

  检测变更（Git diff）：
    M docs/rd.md

  重新解析变更文件...
    ✓ docs/rd.md (新增 2 个标记，删除 1 个标记)

  更新依赖图...
    + 新增节点：RD-REQ-008
    + 新增边：RD-REQ-008 → PRD-FEAT-015
    - 删除节点：RD-REQ-006

✓ 索引更新完成

⏱️  耗时：2 秒
💰 成本：$0
```

**验收标准：**
- ✅ 基于 Git diff 检测变更文件
- ✅ 只重新解析变更文件
- ✅ 增量更新依赖图（添加/删除节点和边）
- ✅ **性能：单文件更新 < 5 秒**

---

### **2.4 Epic 4：影响分析**

**[ID: PRD-EPIC-004] [Implements: RD-FR-3.1, RD-FR-3.2]**

> **作为** 超级个体开发者
> **我希望** 修改文档后能立即知道影响范围
> **以便** 决定哪些下游文档和代码需要更新

---

#### **US-004.1：分析单个文件变更的影响**
**[ID: PRD-US-004.1]**

```bash
# 用户修改 RD 后
$ specgov analyze:impact --changed=docs/rd.md

# 系统输出
🔍 分析影响范围...

  识别变更的节点（基于 Git diff + 标记解析）：
    - RD-REQ-005 (OAuth2 登录需求)
    - RD-REQ-007 (数据加密需求)

  查询依赖图（下游节点）...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 影响分析报告
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

变更节点 (2):
  • RD-REQ-005 (requirement) at docs/rd.md#L42
  • RD-REQ-007 (requirement) at docs/rd.md#L85

受影响的文档 (5):
  ⚠️  PRD-FEAT-012 (feature) at docs/prd.md#L128
      原因：实现了 RD-REQ-005

  ⚠️  DD-API-008 (api_design) at docs/dd.md#L234
      原因：设计了 PRD-FEAT-012

  ⚠️  TD-CASE-015 (test) at docs/td.md#L56
      原因：测试了 DD-API-008

  ⚠️  PRD-FEAT-020 (feature) at docs/prd.md#L256
      原因：实现了 RD-REQ-007

  ⚠️  DD-DB-003 (database) at docs/dd.md#L89
      原因：设计了 PRD-FEAT-020

受影响的代码 (3):
  ⚠️  CODE-API-008 (api_impl) at src/auth/auth.controller.ts#L89
      原因：实现了 DD-API-008

  ⚠️  CODE-SERVICE-005 (service) at src/user/user.service.ts#L45
      原因：实现了 DD-API-008

  ⚠️  CODE-CRYPTO-001 (crypto) at src/utils/crypto.ts#L12
      原因：实现了 DD-DB-003

建议的后续操作：
  1. 重新生成受影响的 PRD 部分
     $ specgov prd:regenerate --scope=PRD-FEAT-012

  2. 评审并更新 DD
     $ specgov dd:review --scope=DD-API-008

  3. 检查代码一致性
     $ specgov check:consistency --scope=CODE-API-008

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ 报告已保存：.specgov/reports/impact-2025-11-16-14-30.json

⏱️  耗时：6 秒
💰 成本：$0（纯图查询，无 AI 调用）
```

**验收标准：**
- ✅ 基于 Git diff 识别变更的标记
- ✅ 查询依赖图的下游节点
- ✅ 输出清晰的影响范围（文档 + 代码）
- ✅ 提供具体的后续操作建议
- ✅ 保存 JSON 格式的报告
- ✅ **性能：< 10 秒**
- ✅ **成本：$0**

---

### **2.5 Epic 5：一致性检查**

**[ID: PRD-EPIC-005] [Implements: RD-FR-3.3, RD-FR-3.4, RD-FR-3.5]**

> **作为** 超级个体开发者
> **我希望** 提交代码前能检查文档-代码的一致性
> **以便** 避免需求遗漏或实现偏差

---

#### **US-005.1：检查单个需求的全链路一致性**
**[ID: PRD-US-005.1]**

```bash
# 用户输入
$ specgov check:consistency --scope=RD-REQ-005

# 系统输出
🔍 检查一致性...

  定位依赖链（基于依赖图）：
    RD-REQ-005 → PRD-FEAT-012 → DD-API-008 → CODE-API-008

  加载相关内容...
    ✓ docs/rd.md#L42-L45 (4 行)
    ✓ docs/prd.md#L128-L156 (29 行)
    ✓ docs/dd.md#L234-L256 (23 行)
    ✓ src/auth/auth.controller.ts#L89-L112 (24 行)
    (总计 80 行，约 2K tokens)

  调用一致性 Agent 深度分析...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 一致性检查报告 (RD-REQ-005)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ RD ↔ PRD：一致
  PRD-FEAT-012 完整实现了 RD-REQ-005 的需求

✓ PRD ↔ DD：一致
  DD-API-008 的 API 设计满足 PRD-FEAT-012 的功能要求

✗ DD ↔ Code：发现 1 处不一致

  问题 #1 [严重]
  ────────────────────────────────────
  位置：src/auth/auth.controller.ts#L95

  期望（DD-API-008）：
    API 路径：POST /auth/oauth2/callback

  实际（CODE-API-008）：
    代码实现：GET /auth/oauth2/callback

  影响：HTTP 方法不匹配，可能导致安全问题

  建议：修改代码为 POST 方法
  ────────────────────────────────────

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

总结：发现 1 处严重不一致，需修复后重新检查

✓ 报告已保存：.specgov/reports/consistency-RD-REQ-005.json

⏱️  耗时：1 分 35 秒
💰 成本：$0.03（上下文 2K tokens）
```

**验收标准：**
- ✅ 基于依赖图定位全链路（RD → PRD → DD → Code）
- ✅ 只加载相关内容（< 5K tokens）
- ✅ 调用 AI Agent 进行深度语义分析
- ✅ 输出结构化的差异报告
- ✅ 区分严重程度（严重/警告/建议）
- ✅ **性能：< 2 分钟**
- ✅ **成本：< $0.05**

---

#### **US-005.2：检查单个模块的一致性**
**[ID: PRD-US-005.2]**

```bash
# 用户输入
$ specgov check:consistency --scope=AuthModule

# 系统输出（类似 US-005.1，但检查整个模块）
🔍 检查模块一致性...

  定位模块相关节点（基于 modules.json）：
    - RD-REQ-005 (OAuth2 登录)
    - RD-REQ-006 (密码登录)
    - RD-REQ-007 (数据加密)
    (共 8 个需求)

  加载相关内容（约 15K tokens）...
  调用一致性 Agent...

✓ 检查完成：发现 2 处不一致

⏱️  耗时：1 分 58 秒
💰 成本：$0.08
```

**验收标准：**
- ✅ 基于 `modules.json` 定位模块
- ✅ 加载模块相关的所有文档和代码
- ✅ **性能：< 2 分钟**
- ✅ **成本：< $0.10**

---

#### **US-005.3：全项目一致性检查（并行）**
**[ID: PRD-US-005.3]**

```bash
# 用户输入
$ specgov check:consistency --scope=full

# 系统输出
🔍 检测到 10 个模块，建议并行检查

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
并行检查指南
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

请在多个终端/AI 客户端中并行执行以下命令：

  终端 1: specgov check:consistency --scope=UserModule
  终端 2: specgov check:consistency --scope=AuthModule
  终端 3: specgov check:consistency --scope=OrderModule
  终端 4: specgov check:consistency --scope=PaymentModule
  终端 5: specgov check:consistency --scope=InventoryModule
  ...（共 10 个模块）

完成后运行：
  $ specgov check:merge

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

提示：如果顺序执行，预计耗时 20 分钟
      并行执行，预计耗时 5 分钟
```

**合并报告：**

```bash
$ specgov check:merge

# 系统输出
🔄 合并一致性检查报告...

  读取报告：
    ✓ .specgov/reports/consistency-UserModule.json
    ✓ .specgov/reports/consistency-AuthModule.json
    ✓ .specgov/reports/consistency-OrderModule.json
    (共 10 个模块)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 全项目一致性检查报告
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

总结：
  ✓ 通过：8 个模块
  ⚠️  警告：1 个模块 (InventoryModule - 2 处警告)
  ✗ 失败：1 个模块 (PaymentModule - 3 处严重问题)

详细问题列表：
  [严重] PaymentModule - DD ↔ Code 不一致
    位置：src/payment/payment.service.ts#L45
    问题：DD 设计使用整数（分），代码使用浮点（元）

  [严重] PaymentModule - PRD ↔ DD 不一致
    位置：docs/dd.md#L234
    问题：PRD 要求分页，DD 未设计分页参数

  ... (共 5 处问题)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ 合并报告已保存：.specgov/reports/consistency-full-2025-11-16.json

总耗时：5 分 12 秒（10 个模块并行）
总成本：$0.80
```

**验收标准：**
- ✅ 检测模块数量，输出并行任务清单
- ✅ 提供合并命令
- ✅ 汇总所有模块的检查结果
- ✅ **性能：< 10 分钟（并行）**
- ✅ **成本：< $2**

---

## **三、功能列表与命令设计**

### **3.1 CLI 命令架构**

**[ID: PRD-FEAT-CLI-001]**

```
specgov
├── init                    # 项目初始化
├── rd:*                    # RD 阶段命令
│   ├── generate
│   ├── review
│   └── revise
├── prd:*                   # PRD 阶段命令
│   ├── generate
│   ├── review
│   └── revise
├── dd:*                    # DD 阶段命令
├── td:*                    # TD 阶段命令
├── index:*                 # 索引管理
│   ├── build
│   └── update
├── analyze:*               # 分析命令
│   └── impact
├── check:*                 # 检查命令
│   ├── consistency
│   └── merge
└── config:*                # 配置管理
    ├── show
    └── set
```

---

### **3.2 核心命令详细设计**

#### **命令：specgov init**
**[ID: PRD-CMD-001]**

**语法：**
```bash
specgov init <project-name> [options]
```

**参数：**
| 参数 | 类型 | 必需 | 默认值 | 说明 |
|------|------|------|--------|------|
| `<project-name>` | string | ✅ | - | 项目名称 |
| `--ai` | string | ❌ | claude-code | AI 后端（claude-code, gemini-cli 等） |
| `--no-git` | boolean | ❌ | false | 不初始化 Git 仓库 |

**输出：**
- 创建 `.specgov/` 目录结构
- 生成 `config.yml`、`state.json`、`modules.json`
- 输出下一步指引

---

#### **命令：specgov rd:generate**
**[ID: PRD-CMD-002] [Implements: RD-FR-1.2]**

**语法：**
```bash
specgov rd:generate [options]
```

**参数：**
| 参数 | 类型 | 必需 | 默认值 | 说明 |
|------|------|------|--------|------|
| `--input` | string | ❌ | - | 输入文件路径（用户故事、业务需求等） |
| `--ai` | string | ❌ | 默认 AI | AI 后端 |
| `--output` | string | ❌ | .specgov/artifacts/rd.md | 输出路径 |

**核心功能：**
1. 读取输入文件（如果提供）
2. 调用 RD Generator Agent
3. **Agent 必须在输出中嵌入可追溯性标记**
4. 保存到 `.specgov/artifacts/rd.md`
5. 输出统计信息

**Agent 提示词要点：**
```
你是一位需求分析师。请生成需求文档。

【重要要求】
1. 为每个需求分配唯一 ID：[ID: RD-REQ-XXX]
2. 如果需求有层次结构，使用 [Decomposes: PARENT-ID]
3. 输出 Markdown 格式

【输出示例】
## 1. 用户认证需求
[ID: RD-AUTH-001]

### 1.1 OAuth2 登录
[ID: RD-REQ-005] [Decomposes: RD-AUTH-001]

系统必须支持...
```

---

#### **命令：specgov index:build**
**[ID: PRD-CMD-006] [Implements: RD-FR-2.1]**

**语法：**
```bash
specgov index:build [options]
```

**参数：**
| 参数 | 类型 | 必需 | 说明 |
|------|------|------|------|
| `--force` | boolean | ❌ | 强制重建（忽略缓存） |

**核心功能：**
1. 扫描项目文件（Markdown + 代码）
2. 正则表达式解析所有标记
3. 构建依赖图（节点 + 边）
4. 检测循环依赖
5. 保存到 `.specgov/index/dependency-graph.json`

**性能要求：**
- ✅ 100 万行代码 < 1 分钟
- ✅ 纯本地计算，$0 成本

---

#### **命令：specgov analyze:impact**
**[ID: PRD-CMD-008] [Implements: RD-FR-3.1]**

**语法：**
```bash
specgov analyze:impact --changed=<file>
```

**核心功能：**
1. Git diff 识别变更内容
2. 解析变更文件中的标记
3. 查询依赖图的下游节点
4. 输出影响范围（文档 + 代码）
5. 提供后续操作建议

**性能要求：**
- ✅ < 10 秒
- ✅ $0 成本（纯图查询）

---

#### **命令：specgov check:consistency**
**[ID: PRD-CMD-010] [Implements: RD-FR-3.3, RD-FR-3.4]**

**语法：**
```bash
specgov check:consistency --scope=<scope>
```

**参数：**
| 参数 | 类型 | 说明 | 示例 |
|------|------|------|------|
| `--scope` | string | 检查范围 | `RD-REQ-005`（单个需求）<br>`AuthModule`（单个模块）<br>`full`（全项目） |

**核心功能：**
1. 基于依赖图定位依赖链
2. 加载相关文档和代码（< 20K tokens）
3. 调用一致性 Agent
4. 输出差异报告

**性能要求：**
- ✅ 单需求：< 2 分钟
- ✅ 单模块：< 2 分钟
- ✅ 全项目（并行）：< 10 分钟

---

## **四、交互设计规范**

### **4.1 CLI 输出格式标准**

**[ID: PRD-UI-001]**

#### **成功消息**
```
✓ 操作成功
```

#### **错误消息**
```
✗ 操作失败：<原因>
```

#### **进度指示**
```
🔨 正在构建索引...
  ✓ 步骤 1 完成
  ⏳ 步骤 2 进行中...
```

#### **分隔线**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
标题
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

#### **统计信息**
```
📊 统计：
  - 项目 1：值 1
  - 项目 2：值 2
```

#### **性能和成本**
```
⏱️  耗时：X 秒
💰 成本：$X
```

---

### **4.2 JSON 输出格式**

**[ID: PRD-UI-002]**

所有报告（影响分析、一致性检查、评审报告）都必须输出 JSON 格式，便于程序化处理。

**示例：影响分析报告**
```json
{
  "version": "1.0",
  "timestamp": "2025-11-16T14:30:00Z",
  "changed_file": "docs/rd.md",
  "changed_nodes": [
    {
      "id": "RD-REQ-005",
      "type": "requirement",
      "location": "docs/rd.md#L42"
    }
  ],
  "affected_nodes": [
    {
      "id": "PRD-FEAT-012",
      "type": "feature",
      "location": "docs/prd.md#L128",
      "reason": "Implements RD-REQ-005"
    }
  ],
  "recommendations": [
    "运行 specgov prd:regenerate --scope=PRD-FEAT-012"
  ]
}
```

---

## **五、功能优先级与迭代计划**

### **5.1 MVP（最小可行产品）- 优先级 P0**

**[ID: PRD-PRIORITY-MVP]**

**目标：10-14 周完成，验证核心价值**

| 功能 | PRD ID | 优先级 |
|------|--------|--------|
| 项目初始化 | PRD-US-001.1 | P0 |
| RD 生成-评审-修订 | PRD-US-002.1-002.3 | P0 |
| 标记解析器 | PRD-CMD-006 | P0 |
| 依赖图构建 | PRD-CMD-006 | P0 |
| 影响分析 | PRD-CMD-008 | P0 |
| 单需求一致性检查 | PRD-CMD-010 | P0 |

**不包含在 MVP：**
- PRD/DD/TD 阶段（只实现 RD）
- 全项目一致性检查
- 增量索引更新

---

### **5.2 V1.0（第一个完整版本）- 优先级 P1**

**[ID: PRD-PRIORITY-V1]**

**目标：MVP + 6-8 周**

| 功能 | PRD ID | 优先级 |
|------|--------|--------|
| PRD/DD/TD 阶段 | PRD-EPIC-002 | P1 |
| 增量索引更新 | PRD-US-003.2 | P1 |
| 模块级一致性检查 | PRD-US-005.2 | P1 |
| 全项目并行检查 | PRD-US-005.3 | P1 |

---

### **5.3 V2.0（生产级）- 优先级 P2**

**[ID: PRD-PRIORITY-V2]**

**目标：V1.0 + 4-6 周**

| 功能 | 优先级 |
|------|--------|
| Git Hooks 集成 | P2 |
| 性能优化（缓存、并行） | P2 |
| Web UI（可选） | P2 |
| 多项目支持 | P2 |

---

## **六、验收标准 (Acceptance Criteria)**

### **6.1 功能验收**

**[ID: PRD-AC-001]**

| 功能 | 验收标准 |
|------|---------|
| **标记解析** | ✅ 准确率 > 95%<br>✅ 支持所有标记类型<br>✅ 处理边界情况（多标记、嵌套） |
| **依赖图构建** | ✅ 检测循环依赖<br>✅ 100 万行代码 < 1 分钟<br>✅ 零 AI 成本 |
| **影响分析** | ✅ < 10 秒响应<br>✅ $0 成本<br>✅ 准确识别下游节点 |
| **一致性检查** | ✅ 不一致检测准确率 > 85%<br>✅ 单需求 < 2 分钟<br>✅ 成本 < $0.05 |

---

### **6.2 性能验收**

**[ID: PRD-AC-002]**

| 场景 | 目标 | 验收标准 |
|------|------|---------|
| 索引构建 | < 1 分钟 | ✅ 100 万行代码项目 |
| 影响分析 | < 10 秒 | ✅ 任意规模项目 |
| 单需求检查 | < 2 分钟 | ✅ 上下文 < 5K tokens |
| 模块检查 | < 2 分钟 | ✅ 上下文 < 20K tokens |
| 全项目检查 | < 10 分钟 | ✅ 10 模块并行 |

---

### **6.3 成本验收**

**[ID: PRD-AC-003]**

| 场景 | 目标 | 验收标准 |
|------|------|---------|
| 索引构建 | $0 | ✅ 本地解析 |
| 影响分析 | $0 | ✅ 纯图查询 |
| 单需求检查 | < $0.05 | ✅ 小上下文 |
| 全项目检查 | < $2 | ✅ 10 模块 |
| 月度总成本 | < $2 | ✅ 日常使用 |

---

## **七、技术约束与依赖**

### **7.1 技术栈**

**[ID: PRD-TECH-001]**

| 组件 | 技术选型 | 理由 |
|------|---------|------|
| CLI 框架 | Python (Click) | 复用 spec-kit |
| 标记解析 | 正则表达式 | 高性能，零依赖 |
| 依赖图 | 内存图数据结构 + JSON | 简单高效 |
| AI 集成 | spec-kit 的抽象层 | 支持多后端 |

---

### **7.2 外部依赖**

**[ID: PRD-TECH-002]**

| 依赖 | 必需性 | 说明 |
|------|--------|------|
| Git | ✅ 必需 | 变更检测、版本控制 |
| AI CLI 工具 | ✅ 必需 | Claude Code / Gemini CLI 等 |
| Python 3.8+ | ✅ 必需 | 运行环境 |
| spec-kit | ✅ 必需 | 基础框架 |

---

## **八、非功能需求**

### **8.1 可用性**

**[ID: PRD-NFR-001]**

- ✅ 用户无需学习复杂配置，`specgov init` 即可开始
- ✅ 所有命令提供 `--help` 文档
- ✅ 错误消息清晰，提供修复建议

---

### **8.2 可扩展性**

**[ID: PRD-NFR-002]**

- ✅ 支持任意规模项目（通过模块化检查）
- ✅ 支持自定义标记类型（配置文件）
- ✅ 支持多种 AI 后端（插件机制）

---

### **8.3 可维护性**

**[ID: PRD-NFR-003]**

- ✅ 代码模块化，职责清晰
- ✅ 单元测试覆盖率 > 80%
- ✅ 详细的开发者文档

---

## **九、风险与限制**

### **9.1 风险**

**[ID: PRD-RISK-001]**

| 风险 | 影响 | 缓解措施 |
|------|------|---------|
| AI 生成的标记不准确 | 依赖图不完整 | 1. Reviewer Agent 检查标记<br>2. 提供手动修复工具 |
| 用户忘记更新索引 | 影响分析不准确 | 1. Git Hooks 自动触发<br>2. 检测索引过期并警告 |
| 大型项目性能问题 | 索引构建慢 | 1. 增量更新<br>2. 并行解析 |

---

### **9.2 限制**

**[ID: PRD-LIMIT-001]**

| 限制 | 说明 |
|------|------|
| 依赖显式标记 | 如果用户不嵌入标记，依赖图不完整 |
| 纯文本分析 | 无法理解复杂的代码逻辑（依赖 AI 补偿） |
| CLI only | MVP 阶段不提供 Web UI |

---

## **十、总结**

### **10.1 核心价值**

**[ID: PRD-SUMMARY-001]**

SpecGovernor 通过以下方式为超级个体创造价值：

1. ✅ **极速影响分析**：< 10 秒，$0 成本（vs 传统方案 2 分钟，$0.05）
2. ✅ **100% 可靠追溯**：基于显式标记，避免 AI 推断错误
3. ✅ **双重质量保证**：Generator-Reviewer 对，避免自我审查偏差
4. ✅ **成本极低**：< $2/月（vs 传统方案 $20+/月）

---

### **10.2 与竞品对比**

**[ID: PRD-SUMMARY-002]**

| 维度 | SpecGovernor | 传统文档管理 | AI 编码助手 |
|------|-------------|-------------|-----------|
| 影响分析 | < 10s, $0 | 手动，数小时 | 不支持 |
| 一致性检查 | 自动化 | 人工 Code Review | 无结构化检查 |
| 可追溯性 | 显式标记，100% | 依赖人工维护 | 隐式，不可靠 |
| 成本 | < $2/月 | 人力成本高 | $20+/月 |

---

### **10.3 下一步**

**[ID: PRD-NEXT-001]**

基于本 PRD，下一步工作：

1. ✅ **编写 DD（设计文档）**：spec-kit 改造的技术设计
2. ✅ **编写 TD（测试文档）**：测试策略和用例
3. ✅ **开始实现**：Fork spec-kit，开始改造

---

## **附录 A：可追溯性标记规范**

**[ID: PRD-APPENDIX-A]**

### **标记类型**

| 标记 | 格式 | 说明 | 示例 |
|------|------|------|------|
| **ID** | `[ID: PREFIX-XXX]` | 定义当前内容的唯一标识 | `[ID: RD-REQ-005]` |
| **Implements** | `[Implements: ID]` | 声明实现了上游需求 | `[Implements: RD-REQ-005]` |
| **Decomposes** | `[Decomposes: ID]` | 声明是上级需求的分解 | `[Decomposes: HL-AUTH-001]` |
| **Designs-for** | `[Designs-for: ID]` | 声明是某功能的设计 | `[Designs-for: PRD-FEAT-012]` |
| **Tests-for** | `[Tests-for: ID]` | 声明是某设计的测试 | `[Tests-for: DD-API-008]` |

### **ID 前缀规范**

| 阶段 | 前缀 | 示例 |
|------|------|------|
| RD | `RD-REQ-` | RD-REQ-001, RD-AUTH-001 |
| PRD | `PRD-FEAT-`, `PRD-US-` | PRD-FEAT-012, PRD-US-001.1 |
| DD | `DD-API-`, `DD-DB-` | DD-API-008, DD-DB-003 |
| TD | `TD-CASE-` | TD-CASE-015 |
| Code | `CODE-API-`, `CODE-SERVICE-` | CODE-API-008 |

---

**PRD 文档结束**
