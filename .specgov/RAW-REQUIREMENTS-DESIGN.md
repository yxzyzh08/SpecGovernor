# Raw Requirements Collection System - Design Document

**Version**: 1.0
**Date**: 2025-01-17
**Purpose**: 记录和整理人类原始需求输入（口语化、零散）

---

## 🎯 功能概述

### 目标

为产品经理提供一个系统化的方式来收集、整理和追溯人类的原始需求输入。

### 使用场景

1. **收集阶段**：人类通过聊天或文件提供零散的、口语化的需求
2. **记录阶段**：产品经理将原始输入记录到专门的文档中
3. **整理阶段**：产品经理对原始需求进行初步分类和标注
4. **生成阶段**：基于整理好的原始需求，产品经理生成正式的 PRD.md
5. **追溯阶段**：后期可以查询原始需求，了解需求来源和演化

---

## 📁 目录结构

### 小项目（< 10 万行代码）

```
.specgov/
└── raw-requirements/
    └── inputs.md              # 单个汇总文档
```

### 大项目（≥ 10 万行代码）

```
.specgov/
└── raw-requirements/
    ├── overview.md            # 总览：跨模块需求、整体目标
    └── modules/               # 模块级原始需求
        ├── user-module.md     # 用户模块原始需求
        ├── order-module.md    # 订单模块原始需求
        └── payment-module.md  # 支付模块原始需求
```

---

## 📄 文档格式

### 小项目文档模板 (inputs.md)

```markdown
# Raw Requirements - [Project Name]

**Project Type**: Small Project
**Created**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD

---

## 📝 Input Log

### Entry 001 - YYYY-MM-DD HH:MM

**Source**: Chat / File / Email / Meeting Notes
**Topic**: [简短主题，如 "用户登录功能"]

**Original Input**:
> [保持原始输入的口语化表达]
> 用户的原话，不做修改

**PM Analysis**:
- **Category**: 功能需求 / 非功能需求 / UI/UX / 性能 / 安全
- **Priority**: High / Medium / Low
- **Related Modules**: [相关模块]
- **Initial Thoughts**: [产品经理的初步想法]
- **Questions**: [需要澄清的问题]

---

### Entry 002 - YYYY-MM-DD HH:MM
...

---

## 📊 Summary Statistics

- Total Entries: X
- By Category:
  - Functional Requirements: X
  - Non-Functional Requirements: X
  - UI/UX: X
  - Others: X
- By Priority:
  - High: X
  - Medium: X
  - Low: X

---

## 🔗 Related Documents

- **PRD**: docs/PRD.md (generated from these raw requirements)
- **Design**: docs/Design-Document.md
```

### 大项目文档模板 (overview.md)

```markdown
# Raw Requirements Overview - [Project Name]

**Project Type**: Large Project (Two-Tier)
**Created**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD

---

## 📋 Project-Level Requirements

### Entry 001 - YYYY-MM-DD HH:MM

**Source**: Chat
**Topic**: 项目整体目标

**Original Input**:
> [跨模块需求、整体架构需求]

**PM Analysis**:
- **Scope**: Project-Level
- **Affects Modules**: [受影响的模块列表]
- **Priority**: High

---

## 📦 Module-Specific Requirements

See individual module files:
- [User Module](modules/user-module.md)
- [Order Module](modules/order-module.md)
- [Payment Module](modules/payment-module.md)

---

## 🔗 Related Documents

- **PRD Overview**: docs/PRD/PRD-Overview.md
- **Module PRDs**: docs/PRD/*.md
```

### 大项目模块文档模板 (modules/user-module.md)

```markdown
# Raw Requirements - User Module

**Module**: User
**Created**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD

---

## 📝 Input Log

### Entry 001 - YYYY-MM-DD HH:MM

**Source**: Chat
**Topic**: 用户注册登录

**Original Input**:
> 我想要用户能用手机号注册，然后用 Google 账号登录

**PM Analysis**:
- **Category**: 功能需求
- **Priority**: High
- **Related PRD Tag**: PRD-User-FEAT-001 (待生成)
- **Initial Thoughts**: 需要 OAuth2 集成
- **Questions**:
  - 是否支持其他 OAuth2 提供商？
  - 手机号注册是否需要短信验证？

---

## 🔗 Related Documents

- **Module PRD**: docs/PRD/PRD-User-Module.md
```

---

## 🔄 工作流程

### Step 1: 收集原始输入

**触发条件**: 人类提供需求（通过聊天、文件、邮件等）

**产品经理行为**:
1. 打开对应的原始需求文档（小项目用 `inputs.md`，大项目用 `overview.md` 或 `modules/xxx-module.md`）
2. 创建新的 Entry，记录：
   - 时间戳
   - 输入来源
   - 原始内容（保持口语化）
   - 初步分析

**使用命令**: `/specgov-collect-raw-req`

### Step 2: 定期整理

**触发条件**: 积累了一定数量的原始输入（如 5-10 条）

**产品经理行为**:
1. 回顾所有 Entries
2. 识别重复或相关的需求
3. 进行分类和优先级排序
4. 标注需要澄清的问题

### Step 3: 生成正式 PRD

**触发条件**: 原始需求收集完成，准备进入正式文档阶段

**产品经理行为**:
1. 基于原始需求，生成正式的 PRD.md
2. 在 PRD.md 中引用原始需求的 Entry 编号（可选）
3. 保留原始需求文档用于追溯

**使用命令**: `/specgov-prd-gen`

### Step 4: 追溯查询

**触发条件**: 需要了解某个需求的来源或演化过程

**产品经理行为**:
1. 打开原始需求文档
2. 搜索相关 Entry
3. 查看原始输入和初步分析

---

## 🏷️ 标记和追溯

### 可选：在 PRD 中引用原始需求

在生成 PRD 时，可以添加引用：

```markdown
### OAuth2 Login Feature

**[ID: PRD-FEAT-012]**
**[Raw-Req: Entry-003, Entry-007]**  ← 引用原始需求 Entry

基于用户的原始需求（见 .specgov/raw-requirements/inputs.md Entry-003），
我们设计了 OAuth2 登录功能...
```

这样可以建立 PRD 与原始需求之间的追溯关系。

---

## 📊 统计和分析

### 自动生成统计

在每个原始需求文档的底部，产品经理可以维护统计信息：
- 总条目数
- 按类别分类
- 按优先级分类
- 按状态分类（已转化为 PRD / 待处理 / 已废弃）

---

## 🔒 隐私和安全

**原始需求文档的特点**:
- ✅ **仅供超级个体使用**：不会影响项目构建、测试、部署
- ✅ **不包含在 Git 提交中**（可选）：可以添加到 `.gitignore`
- ✅ **本地存储**：存储在 `.specgov/raw-requirements/`
- ✅ **纯文本格式**：Markdown，便于搜索和版本控制

### 可选的 .gitignore 配置

如果不想提交原始需求到 Git：

```gitignore
# SpecGovernor - Raw Requirements (optional)
.specgov/raw-requirements/
```

---

## 🛠️ 实现计划

### 需要创建的文件

1. **Prompt Template**: `.specgov/prompts/raw-requirements-collector.md`
   - 角色：Product Manager
   - 任务：收集和整理原始需求
   - 输出：更新 raw-requirements/ 中的文档

2. **Slash Command**: `.claude/commands/specgov-collect-raw-req.md`
   - 加载 `raw-requirements-collector.md` prompt
   - 提供当前原始需求文档的路径
   - 指导产品经理添加新的 Entry

3. **Init Script 更新**: `.specgov/scripts/init_project.py`
   - 创建 `.specgov/raw-requirements/` 目录
   - 小项目：创建 `inputs.md` 模板
   - 大项目：创建 `overview.md` 和 `modules/` 目录

4. **Workflow 文档更新**: `.specgov/workflows/workflow-prd.md`
   - 添加"Step 0: 收集原始需求"步骤
   - 说明何时使用原始需求收集

5. **Task 文档更新**: `.specgov/tasks/product-manager.md`
   - 添加原始需求收集任务

---

## ✅ 验收标准

- [x] 设计完成目录结构
- [ ] 创建 Prompt Template
- [ ] 创建 Slash Command
- [ ] 更新 init_project.py
- [ ] 更新 Workflow 文档
- [ ] 更新 Task 文档
- [ ] 测试小项目场景
- [ ] 测试大项目场景

---

**设计完成日期**: 2025-01-17
