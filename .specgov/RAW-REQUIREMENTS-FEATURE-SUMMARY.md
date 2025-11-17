# 原始需求收集功能 - 实现总结

**Version**: 1.0 (调整后)
**Date**: 2025-01-17
**Status**: ✅ 已完成

---

## 🎯 用户需求

用户希望产品经理能够：
1. 记录人类提供的原始需求（口语化、零散的输入）
2. 在生成 PRD 的**同时**完成这项工作，而不是单独的命令
3. 使用现有的产品经理角色（`/specgov-prd-gen`），不需要新增命令
4. 便于后期查询和追溯原始需求

---

## ✅ 调整后的设计

### 核心思路

**产品经理在生成 PRD 时，自动执行两步操作**：

```
用户: 提供原始需求（口语化）
  ↓
/specgov-prd-gen (产品经理角色)
  ↓
  ├─ Step 1: 收集并记录原始需求 → .specgov/raw-requirements/
  └─ Step 2: 基于原始需求生成正式 PRD → docs/PRD.md
  ↓
完成：原始需求已记录 + 正式 PRD 已生成
```

### 关键优势

✅ **无需额外命令** - 使用现有的 `/specgov-prd-gen`
✅ **流程自然** - 收集需求和生成 PRD 合二为一
✅ **角色一致** - 都是产品经理的工作，不需要切换
✅ **自动化** - 产品经理主动询问并记录原始需求

---

## 📁 目录结构（保留）

原始需求收集目录结构**保持不变**：

### 小项目
```
.specgov/
└── raw-requirements/
    └── inputs.md              # 单个汇总文档
```

### 大项目
```
.specgov/
└── raw-requirements/
    ├── overview.md            # 项目级需求
    └── modules/               # 模块级需求
        ├── user-module.md
        ├── order-module.md
        └── ...
```

---

## 🔄 工作流程详解

### 小项目工作流

#### 首次生成 PRD

```bash
# 用户执行
/specgov-prd-gen
```

**产品经理自动执行**：

1. **询问原始需求**：
   ```
   在生成正式 PRD 之前，我需要先了解您的原始需求。

   请告诉我：
   - 您想实现什么功能？
   - 为什么需要这个功能？
   - 您期望的用户体验是什么样的？
   - 有没有参考的产品或案例？

   您可以用口语化的方式描述，不需要太正式。
   ```

2. **用户回复** (口语化)：
   ```
   我想要一个登录功能，最好能用 Google 账号登录，因为我不想记密码。
   另外，能不能也支持手机号登录？我看很多 app 都有这个。
   ```

3. **产品经理记录到 `.specgov/raw-requirements/inputs.md`**：
   ```markdown
   ### Entry 001 - 2025-01-17 14:30

   **Source**: Chat
   **Topic**: 用户登录功能

   **Original Input**:
   > 我想要一个登录功能，最好能用 Google 账号登录，因为我不想记密码。
   > 另外，能不能也支持手机号登录？我看很多 app 都有这个。

   **PM Analysis**:
   - **Category**: Functional Requirement
   - **Priority**: High
   - **Related Modules**: Authentication
   - **Initial Thoughts**:
     - Need OAuth2 integration for Google login
     - Phone login requires SMS verification
   - **Questions**:
     - Do we need email/password login as fallback?
     - SMS provider preference?
   - **Status**: New
   ```

4. **产品经理基于原始需求生成正式 `docs/PRD.md`**：
   ```markdown
   ## Part 1: Business Requirements

   ### OAuth2 Authentication Requirement
   **[ID: PRD-REQ-005]**

   系统需支持通过 OAuth2 协议进行用户登录...

   ## Part 2: Product Features

   ### OAuth2 Social Login Feature
   **[ID: PRD-FEAT-012] [Implements: PRD-REQ-005]**

   #### User Story
   > As a new user, I want to login with my Google account...
   ```

#### 后续更新 PRD

再次执行 `/specgov-prd-gen` 时：
- 产品经理会读取现有的 PRD 和原始需求文档
- 如果有新需求，添加新 Entry 到原始需求文档
- 更新 PRD.md

### 大项目工作流

#### 项目级需求 (`/specgov-prd-overview`)

1. 产品经理询问项目整体目标
2. 记录到 `.specgov/raw-requirements/overview.md`
3. 生成 `docs/PRD/PRD-Overview.md`

#### 模块级需求 (`/specgov-prd-module`)

1. 产品经理询问该模块的具体需求
2. 记录到 `.specgov/raw-requirements/modules/{module-name}.md`
3. 如果模块文档不存在，自动创建
4. 生成 `docs/PRD/PRD-{Module}.md`

---

## 🛠️ 已完成的实现

### 1. ✅ 更新了 `init_project.py`

**删除了**：
- `/specgov-collect-raw-req` 命令（不再需要）
- 相关的路径映射和上下文处理

**保留了**：
- `.specgov/raw-requirements/` 目录创建
- 小项目：`inputs.md` 模板生成
- 大项目：`overview.md` 和 `modules/` 目录生成

### 2. ✅ 更新了 PRD Generator 模板

**prd-generator.md** (小项目):
- 添加了 "Workflow: Raw Requirements Collection + PRD Generation" 部分
- Step 1: 收集原始需求（首次生成时）
- Step 2: 基于原始需求生成正式 PRD

**prd-overview-generator.md** (大项目 - Overview):
- 添加了项目级原始需求收集工作流
- 记录到 `.specgov/raw-requirements/overview.md`

**prd-module-generator.md** (大项目 - Module):
- 添加了模块级原始需求收集工作流
- 记录到 `.specgov/raw-requirements/modules/{module-name}.md`

### 3. ✅ 删除了单独的收集器

- ❌ 删除了 `.specgov/prompts/raw-requirements-collector.md`
- 原因：功能已整合到 PRD Generator 中

---

## 📄 Entry 格式规范

### 小项目 (inputs.md)

```markdown
### Entry XXX - YYYY-MM-DD HH:MM

**Source**: Chat / File / Email / Meeting Notes
**Topic**: [简短主题，如 "用户登录功能"]

**Original Input**:
> [保持原始输入的口语化表达]
> 用户的原话，不做修改

**PM Analysis**:
- **Category**: Functional Requirement / Non-Functional Requirement / UI/UX / Performance / Security
- **Priority**: High / Medium / Low
- **Related Modules**: [相关模块]
- **Initial Thoughts**: [产品经理的初步想法]
- **Questions**: [需要澄清的问题]
- **Status**: New / Under Review / Converted to PRD / Rejected
```

### 大项目 - Overview (overview.md)

```markdown
### Entry XXX - YYYY-MM-DD HH:MM

**Source**: Chat / File
**Topic**: 项目整体目标

**Original Input**:
> [跨模块需求、整体架构需求]

**PM Analysis**:
- **Scope**: Project-Level
- **Affects Modules**: [受影响的模块列表]
- **Priority**: High / Medium / Low
- **Initial Thoughts**: [初步想法]
- **Questions**: [需要澄清的问题]
- **Status**: New
```

### 大项目 - Module (modules/{module}.md)

```markdown
### Entry XXX - YYYY-MM-DD HH:MM

**Source**: Chat / File
**Topic**: [模块功能主题]

**Original Input**:
> [用户的原始输入]

**PM Analysis**:
- **Category**: Functional Requirement / Non-Functional Requirement / UI/UX
- **Priority**: High / Medium / Low
- **Related PRD Tag**: [待生成，如 PRD-User-FEAT-001]
- **Initial Thoughts**: [初步想法]
- **Questions**: [需要澄清的问题]
- **Status**: New
```

---

## 🎯 使用示例

### 示例 1：小项目首次生成 PRD

**用户操作**：
```
/specgov-prd-gen
```

**产品经理交互**：
```
📋 在生成正式 PRD 之前，我需要先了解您的原始需求。

请告诉我：
- 您想实现什么功能？
- 为什么需要这个功能？
- 您期望的用户体验是什么样的？
- 有没有参考的产品或案例？

您可以用口语化的方式描述，不需要太正式。
```

**用户回复** (口语化)：
```
我想做一个任务管理应用，用户可以创建任务、设置截止日期、
标记完成状态。主要是给自己用的，界面要简洁，不要太复杂。
参考 Todoist 和 Microsoft To Do。
```

**产品经理自动完成**：
1. ✅ 记录到 `.specgov/raw-requirements/inputs.md` (Entry 001)
2. ✅ 生成正式的 `docs/PRD.md`，包含：
   - Part 1: Business Requirements (任务管理需求)
   - Part 2: Product Features (任务 CRUD 功能、截止日期、状态管理)

### 示例 2：大项目生成模块 PRD

**用户操作**：
```
/specgov-prd-module
```

**产品经理询问**：
```
请告诉我这个模块需要什么功能？

模块名称：[等待用户输入]
模块需求：[等待用户输入]
```

**用户回复**：
```
模块：User
需求：用户注册、登录、个人资料管理、头像上传
```

**产品经理自动完成**：
1. ✅ 记录到 `.specgov/raw-requirements/modules/user-module.md`
2. ✅ 生成 `docs/PRD/PRD-User-Module.md`

---

## 🔍 查询和追溯

### 查看收集的原始需求

**小项目**：
```bash
# Windows
type .specgov\raw-requirements\inputs.md

# Linux/Mac
cat .specgov/raw-requirements/inputs.md
```

**大项目**：
```bash
# 项目级需求
cat .specgov/raw-requirements/overview.md

# 模块级需求
cat .specgov/raw-requirements/modules/user-module.md
```

### 追溯需求演化

1. 打开原始需求文档
2. 查看 Entry 列表，按时间顺序排列
3. 查看每个 Entry 的 Status 字段：
   - `New` - 新收集的需求
   - `Converted to PRD` - 已转化为正式 PRD
   - `Under Review` - 正在分析中
   - `Rejected` - 决定不实现

---

## 📊 统计功能

原始需求文档底部自动维护统计信息：

```markdown
## 📊 Summary Statistics

**Last Updated**: 2025-01-17

- **Total Entries**: 5
- **By Priority**:
  - High: 3
  - Medium: 1
  - Low: 1
- **By Status**:
  - New: 2
  - Under Review: 1
  - Converted to PRD: 2
  - Rejected: 0
```

---

## 🆚 调整前后对比

### 调整前（初始设计）

```
Step 0: /specgov-collect-raw-req (单独收集命令)
  ↓ 产品经理收集原始需求
  ↓ 记录到 .specgov/raw-requirements/
  ↓
Step 1: /specgov-prd-gen (生成 PRD)
  ↓ 基于原始需求生成 PRD
  ↓
完成
```

**问题**：
- ❌ 需要两个命令，流程繁琐
- ❌ 用户可能忘记先收集需求
- ❌ 产品经理角色分散

### 调整后（当前设计）

```
/specgov-prd-gen (产品经理一步完成)
  ↓ Step 1: 收集原始需求（首次）
  ↓ Step 2: 生成正式 PRD
  ↓
完成：原始需求 + 正式 PRD
```

**优势**：
- ✅ 一个命令完成所有工作
- ✅ 流程自然，不会遗漏
- ✅ 产品经理角色统一

---

## 🔒 隐私和版本控制

### 可选：不提交原始需求到 Git

如果不想将原始需求提交到版本控制：

```gitignore
# .gitignore
.specgov/raw-requirements/
```

**原因**：
- 原始需求可能包含不太正式的讨论
- 仅供超级个体本地参考
- 正式的 PRD 已足够记录需求

---

## ✅ 验收标准

- [x] 删除了 `/specgov-collect-raw-req` 命令
- [x] 更新了 `prd-generator.md` 添加原始需求收集工作流
- [x] 更新了 `prd-overview-generator.md` (大项目)
- [x] 更新了 `prd-module-generator.md` (大项目)
- [x] 保留了 `.specgov/raw-requirements/` 目录结构
- [x] 保留了自动创建模板文档的功能
- [x] 产品经理在生成 PRD 时自动收集原始需求
- [ ] 测试功能（待完成）

---

## 🎉 总结

这个调整后的设计**完全符合用户需求**：

1. ✅ **产品经理角色** - 使用现有的 `/specgov-prd-gen` 命令
2. ✅ **一步完成** - 收集原始需求 + 生成 PRD 合二为一
3. ✅ **自动化** - 产品经理主动询问并记录
4. ✅ **可追溯** - 原始需求妥善保存，便于查询

**用户体验**：
- 简单：只需要一个命令 `/specgov-prd-gen`
- 自然：产品经理会引导你提供需求
- 完整：原始需求和正式 PRD 都会生成

---

**功能状态**: ✅ 已完成实现，待测试验证
**文档日期**: 2025-01-17
