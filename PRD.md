# **📦 Product Requirements Document (PRD) - SpecGovernor**

> **Version**: v2.0
> **Based on**: RD.md (v2.0)
> **Created**: 2025-11-16
> **Updated**: 2025-11-16
> **Product Type**: Toolkit (Prompt Templates + Workflow Documentation + Helper Scripts)

---

## **Traceability Declaration**

本文档实现了 RD.md 中的以下需求：
- [Implements: RD-GOAL-001] 提供标准化提示词模板
- [Implements: RD-GOAL-002] 定义规范化开发流程
- [Implements: RD-GOAL-003] 实现可追溯性
- [Implements: RD-GOAL-004] 提供辅助工具
- [Implements: RD-USER-001] 服务超级个体用户

---

## **一、Product Overview**

### **1.1 Product Vision**

**[ID: PRD-VISION-001] [Implements: RD-GOAL-001]**

SpecGovernor 是一个专为**超级个体** (Super Individuals) 设计的**综合工具包** (comprehensive toolkit)，提供：

- **Prompt templates** 用于使用 Claude Code 生成标准化的 RD/PRD/Design Document/Test Plan/Code
- **Workflow documentation** 指导人类通过结构化的开发流程
- **Helper scripts** 用于解析可追溯性标记、构建依赖图和影响分析

**核心价值主张：**
- 🎯 **显式可追溯性**：通过嵌入式标记实现 100% 可靠的追踪，无需 AI 推断
- 🔄 **双重质量保证**：每个阶段都有 Generator-Reviewer 模板对
- 📦 **零安装**：简单的文件模板，可直接与 Claude Code 配合使用
- 💰 **成本效益高**：无需软件许可证，只需模板和脚本

---

### **1.2 Target User Profile**

**[ID: PRD-USER-001] [Implements: RD-USER-001]**

| 用户类型 | 典型场景 | 痛点 |
|---------|---------|------|
| **独立开发者** (Independent Developer) | 构建 SaaS 产品 | 文档与代码不同步，需求变更难以追踪 |
| **技术创业者** (Tech Entrepreneur) | MVP 快速迭代 | 身兼多职，文档成本高 |
| **小团队技术负责人** (Small Team Tech Lead) | 管理 5-10 人团队 | 需要流程但没有专职 PM/QA |

---

### **1.3 Product Structure**

**[ID: PRD-STRUCTURE-001]**

```
SpecGovernor Toolkit
├── Prompt Templates (提示词模板)
│   ├── rd-generator.md          # 生成/修改 Requirements Document
│   ├── rd-reviewer.md           # 审查 Requirements Document
│   ├── prd-generator.md         # 生成/修改 Product Requirements Document
│   ├── prd-reviewer.md          # 审查 Product Requirements Document
│   ├── design-generator.md      # 生成/修改 Design Document
│   ├── design-reviewer.md       # 审查 Design Document
│   ├── test-plan-generator.md   # 生成/修改 Test Plan
│   ├── test-plan-reviewer.md    # 审查 Test Plan
│   └── code-generator.md        # 生成/修改 Code
│
├── Workflow Documentation (流程文档)
│   ├── workflow-overview.md     # 整体 SDLC 流程概览
│   ├── workflow-rd.md           # RD 生成流程
│   ├── workflow-prd.md          # PRD 生成流程
│   ├── workflow-design.md       # Design Document 流程
│   ├── workflow-test-plan.md    # Test Plan 流程
│   └── workflow-task-mgmt.md    # 任务管理流程
│
└── Helper Scripts (辅助脚本)
    ├── parse_tags.py            # 从文件中解析可追溯性标记
    ├── build_graph.py           # 构建依赖图
    ├── impact_analysis.py       # 分析变更影响
    └── init_project.py          # 初始化项目结构
```

---

## **二、User Stories**

### **2.1 Epic 1: Project Initialization**

**[ID: PRD-EPIC-001] [Implements: RD-INIT-001]**

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
   - 与 RD 的可追溯性：[Implements: RD-REQ-XXX]

7. 输出保存到 docs/PRD.md

8. 更新 .specgov/tasks/product-manager.md 和 project-manager.md
```

**生成的 PRD 示例：**
```markdown
## 2. User Authentication Features

### 2.1 OAuth2 Login Feature
**[ID: PRD-FEAT-012] [Implements: RD-REQ-005]**

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
- ✅ 嵌入链接到需求的 [Implements: RD-XXX] 标记
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

**[ID: PRD-EPIC-003] [Implements: RD-GOAL-004]**

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
**[Implements: RD-REQ-005]**

### 2.1 OAuth2 Social Login
**[ID: PRD-FEAT-012] [Implements: RD-REQ-005]**

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

**[ID: PRD-EPIC-004] [Implements: RD-USER-001]**

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

**[ID: PRD-FEAT-TEMPLATES-001] [Implements: RD-GOAL-001]**

| Template 文件 | 用途 | 输入 | 输出 |
|--------------|---------|-------|--------|
| **rd-generator.md** | 生成或修改 Requirements Document | 用户故事、业务需求、（现有 RD.md） | 带 [ID: RD-XXX] 标记的 RD.md |
| **rd-reviewer.md** | 审查 Requirements Document | RD.md | 审查报告 |
| **prd-generator.md** | 生成或修改 Product Requirements Document | RD.md、产品愿景 | 带 [ID: PRD-XXX]、[Implements: RD-XXX] 的 PRD.md |
| **prd-reviewer.md** | 审查 Product Requirements Document | PRD.md | 审查报告 |
| **design-generator.md** | 生成或修改 Design Document | PRD.md、技术约束 | 带 [ID: DESIGN-XXX]、[Designs-for: PRD-XXX] 的 Design-Document.md |
| **design-reviewer.md** | 审查 Design Document | Design-Document.md | 审查报告 |
| **test-plan-generator.md** | 生成或修改 Test Plan | Design-Document.md、PRD.md | 带 [ID: TEST-XXX]、[Tests-for: DESIGN-XXX] 的 Test-Plan.md |
| **test-plan-reviewer.md** | 审查 Test Plan | Test-Plan.md | 审查报告 |
| **code-generator.md** | 生成或修改 Code | Design-Document.md | 带 [ID: CODE-XXX]、[Implements: DESIGN-XXX] 的代码文件 |

**注意：**
- 所有 generator templates 同时处理创建和修改（无单独的 reviser templates）
- 当向 generator template 提供现有文档时，它会修改而非创建
- 所有 templates 自动嵌入可追溯性标记
- Templates 使用正确的术语："Design Document" 和 "Test Plan"（而非 DD/TD）

---

### **3.2 Workflow Documentation**

**[ID: PRD-FEAT-WORKFLOWS-001] [Implements: RD-GOAL-002]**

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

**[ID: PRD-FEAT-SCRIPTS-001] [Implements: RD-GOAL-004]**

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

**[ID: PRD-FEAT-SMALL-001] [Implements: RD-STRUCTURE-SMALL-001]**

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

**[ID: PRD-FEAT-LARGE-001] [Implements: RD-STRUCTURE-LARGE-001]**

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
