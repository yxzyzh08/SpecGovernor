# Large Project Workflow

**[ID: WORKFLOW-LARGE-001] [Implements: DESIGN-WORKFLOW-STAGES-001]**

## When to Use This Workflow

使用此工作流当：
- **项目规模** ≥ 10 万行代码
- **功能模块** ≥ 5 个独立模块
- **团队规模** ≥ 3 人（或 Super Individual 管理复杂项目）
- **文档复杂度**：单一文档难以维护（如 RD.md > 500 行）

## Large Project Structure

大项目采用 **两层文档结构**：

### Overview Documents (概览文档)
- `RD.md` - 项目整体需求概览
- `PRD.md` - 项目整体产品概览
- `Design-Document.md` - 项目整体架构概览
- `Test-Plan.md` - 项目整体测试策略概览

### Module Documents (模块文档)
- `RD-[Module].md` - 模块具体需求（如 `RD-User.md`, `RD-Order.md`）
- `PRD-[Module].md` - 模块具体产品功能
- `Design-Document-[Module].md` - 模块具体设计
- `Test-Plan-[Module].md` - 模块具体测试用例

## Document Organization

```
docs/
├── RD.md                          # Overview: 整体需求
├── RD-User.md                     # Module: 用户模块需求
├── RD-Order.md                    # Module: 订单模块需求
├── RD-Payment.md                  # Module: 支付模块需求
├── PRD.md                         # Overview: 整体产品
├── PRD-User.md                    # Module: 用户模块产品功能
├── PRD-Order.md                   # Module: 订单模块产品功能
├── PRD-Payment.md                 # Module: 支付模块产品功能
├── Design-Document.md             # Overview: 整体架构
├── Design-Document-User.md        # Module: 用户模块设计
├── Design-Document-Order.md       # Module: 订单模块设计
├── Design-Document-Payment.md     # Module: 支付模块设计
├── Test-Plan.md                   # Overview: 测试策略
├── Test-Plan-User.md              # Module: 用户模块测试
├── Test-Plan-Order.md             # Module: 订单模块测试
└── Test-Plan-Payment.md           # Module: 支付模块测试
```

## Workflow Overview

### Phase 1: Define Modules (As Project Manager)

#### Step 1: Identify Modules

识别项目的主要功能模块：

**Example:**
```markdown
项目：电商平台

功能模块：
1. User（用户）- 用户注册、登录、个人资料管理
2. Order（订单）- 订单创建、查询、修改、取消
3. Payment（支付）- 支付处理、退款、支付方式管理
4. Product（商品）- 商品管理、库存、分类
5. Notification（通知）- 邮件、短信、推送通知
```

#### Step 2: Create Epic per Module

在 `.specgov/tasks/project-manager.md` 为每个模块创建 Epic：

```markdown
## Active Epics

### Epic 1: User Module Implementation
- **目标**：实现完整的用户管理系统
- **模块**：User
- **进度**：0%
- **子任务**：
  - ⬜ RD-User.md（需求分析）
  - ⬜ PRD-User.md（产品规划）
  - ⬜ Design-Document-User.md（技术设计）
  - ⬜ Test-Plan-User.md（测试规划）
  - ⬜ 代码实现

### Epic 2: Order Module Implementation
- **目标**：实现完整的订单管理系统
- **模块**：Order
- **进度**：0%
- **子任务**：
  - ⬜ RD-Order.md（需求分析）
  - ⬜ PRD-Order.md（产品规划）
  - ⬜ Design-Document-Order.md（技术设计）
  - ⬜ Test-Plan-Order.md（测试规划）
  - ⬜ 代码实现
```

### Phase 2: Generate Overview Documents

#### Step 1: Generate RD.md (Overview)

1. 切换到 Requirements Analyst 角色
2. 加载 `.specgov/prompts/rd-overview-generator.md`（大项目变体）
3. 提供以下输入：

```
请生成 RD.md（项目整体需求概览）。

项目上下文：
- 项目名称：电商平台
- 项目规模：大项目（> 10 万行代码）
- 目标用户：在线购物用户、商家、管理员

模块列表：
1. User - 用户注册、登录、个人资料管理
2. Order - 订单创建、查询、修改、取消
3. Payment - 支付处理、退款、支付方式管理
4. Product - 商品管理、库存、分类
5. Notification - 邮件、短信、推送通知

跨模块需求：
- 所有模块必须使用统一的认证机制（JWT）
- 所有模块必须记录审计日志
- 所有模块必须支持国际化（i18n）
```

**Output: `docs/RD.md`**

```markdown
# Requirements Document (RD)

> **Version**: 1.0
> **Project**: 电商平台
> **Scope**: Overview（整体需求概览）
> **Created**: 2025-11-16

## 1. Project Overview
**[ID: RD-PROJECT-001]**

本项目是一个完整的电商平台，包含用户管理、订单管理、支付处理、商品管理和通知服务五个核心模块。

**目标用户：**
- 在线购物用户
- 商家/卖家
- 平台管理员

**核心价值：**
- 提供安全、便捷的在线购物体验
- 支持多种支付方式
- 实时库存管理
- 自动化通知服务

## 2. Module Requirements

### 2.1 User Module
**[ID: RD-MODULE-USER] [Decomposes: RD-PROJECT-001]**

用户模块负责用户注册、登录、个人资料管理和权限控制。

**模块范围：**
- 用户注册和登录（包括 OAuth2 社交登录）
- 用户个人资料管理
- 角色和权限管理（用户、商家、管理员）
- 密码重置和账户恢复

**详细需求见：** `RD-User.md`

### 2.2 Order Module
**[ID: RD-MODULE-ORDER] [Decomposes: RD-PROJECT-001]**

订单模块负责订单创建、查询、修改、取消和履行流程。

**模块范围：**
- 订单创建（购物车结算）
- 订单查询和列表
- 订单修改（地址、商品）
- 订单取消和退款
- 订单状态跟踪

**详细需求见：** `RD-Order.md`

### 2.3 Payment Module
**[ID: RD-MODULE-PAYMENT] [Decomposes: RD-PROJECT-001]**

支付模块负责支付处理、退款和支付方式管理。

**模块范围：**
- 支付处理（信用卡、PayPal、Stripe）
- 退款处理
- 支付方式管理
- 支付安全（PCI DSS 合规）

**详细需求见：** `RD-Payment.md`

### 2.4 Product Module
**[ID: RD-MODULE-PRODUCT] [Decomposes: RD-PROJECT-001]**

商品模块负责商品管理、库存和分类。

**模块范围：**
- 商品创建和编辑
- 商品分类和标签
- 库存管理
- 商品搜索和筛选

**详细需求见：** `RD-Product.md`

### 2.5 Notification Module
**[ID: RD-MODULE-NOTIFICATION] [Decomposes: RD-PROJECT-001]**

通知模块负责邮件、短信和推送通知服务。

**模块范围：**
- 邮件通知（订单确认、发货提醒）
- 短信通知（验证码、订单状态）
- 推送通知（促销活动）
- 通知模板管理

**详细需求见：** `RD-Notification.md`

## 3. Cross-Cutting Requirements

### 3.1 Authentication and Authorization
**[ID: RD-CROSS-AUTH-001]**

所有模块必须使用统一的认证和授权机制。

**要求：**
- 使用 JWT（JSON Web Token）进行认证
- 支持 OAuth2 社交登录（Google、GitHub、Microsoft）
- 基于角色的访问控制（RBAC）
- Session 有效期 24 小时

**验收标准：**
- ✅ 所有 API 端点验证 JWT token
- ✅ 未授权请求返回 401 Unauthorized
- ✅ 权限不足请求返回 403 Forbidden

### 3.2 Audit Logging
**[ID: RD-CROSS-AUDIT-001]**

所有模块必须记录审计日志，用于安全监控和故障排查。

**要求：**
- 记录所有 API 请求（用户 ID、IP、时间戳、操作）
- 记录所有数据修改（创建、更新、删除）
- 日志保留 90 天

**验收标准：**
- ✅ 所有 API 请求被记录到日志系统
- ✅ 日志包含用户 ID、IP、时间戳、操作类型
- ✅ 敏感数据（密码、支付信息）不被记录

### 3.3 Internationalization (i18n)
**[ID: RD-CROSS-I18N-001]**

所有模块必须支持国际化，允许用户选择语言。

**要求：**
- 支持英文（默认）、中文、西班牙文
- 所有用户界面文本可翻译
- 日期、时间、货币格式本地化

**验收标准：**
- ✅ 用户可以选择界面语言
- ✅ 所有界面文本根据选择的语言显示
- ✅ 日期、时间、货币格式正确本地化
```

#### Step 2: Repeat for PRD.md, Design-Document.md, Test-Plan.md

遵循相同流程，使用相应的 overview generator prompts：
- `.specgov/prompts/prd-overview-generator.md`
- `.specgov/prompts/design-overview-generator.md`
- `.specgov/prompts/test-plan-overview-generator.md`

### Phase 3: Generate Module Documents

#### Step 1: Generate Module RD (RD-User.md)

1. 切换到 Requirements Analyst 角色
2. 加载 `.specgov/prompts/rd-module-generator.md`（大项目变体）
3. 提供以下输入：

```
请生成 RD-User.md（User 模块需求文档）。

RD.md（Overview）内容：
[粘贴 docs/RD.md 中关于 User 模块的部分]

模块名称：User

模块范围：
- 用户注册和登录（包括 OAuth2 社交登录）
- 用户个人资料管理
- 角色和权限管理（用户、商家、管理员）
- 密码重置和账户恢复

用户故事：
- As a new user, I want to register with my email, so that I can create an account
- As a user, I want to log in with my Google account, so that I don't need to create a new password
- As a user, I want to update my profile, so that my information is current
- As an admin, I want to manage user roles, so that I can control access
```

**Output: `docs/RD-User.md`**

```markdown
# Requirements Document - User Module

> **Version**: 1.0
> **Module**: User
> **Based on**: RD.md (v1.0)
> **Created**: 2025-11-16

## 1. User Module Overview
**[ID: RD-USER-OVERVIEW] [Module: User] [Implements: RD-MODULE-USER]**

User 模块负责用户注册、登录、个人资料管理和权限控制。

**模块边界：**
- **包含**：用户注册、登录、OAuth2、个人资料、角色管理
- **不包含**：订单管理（属于 Order 模块）、支付管理（属于 Payment 模块）

## 2. Authentication Requirements

### 2.1 User Registration
**[ID: RD-USER-REG-001] [Module: User] [Decomposes: RD-USER-OVERVIEW]**

系统必须支持用户使用邮箱和密码注册账户。

**验收标准：**
- ✅ 用户可以使用邮箱和密码注册
- ✅ 邮箱必须唯一（不允许重复注册）
- ✅ 密码必须至少 8 个字符，包含大小写字母和数字
- ✅ 注册成功后发送邮箱验证链接
- ✅ 用户必须验证邮箱才能登录

### 2.2 OAuth2 Social Login
**[ID: RD-USER-OAUTH-001] [Module: User] [Decomposes: RD-USER-OVERVIEW] [Implements: RD-CROSS-AUTH-001]**

系统必须支持通过 OAuth2 协议进行社交登录。

**支持的提供商：**
- Google OAuth2
- GitHub OAuth2
- Microsoft OAuth2

**验收标准：**
- ✅ 用户可以使用任何支持的 OAuth2 提供商登录
- ✅ 系统获取用户个人资料信息（姓名、邮箱、头像）
- ✅ 系统优雅地处理登录失败
- ✅ 用户可以关联多个 OAuth2 账户到同一个系统账户

### 2.3 Password Login
**[ID: RD-USER-LOGIN-001] [Module: User] [Decomposes: RD-USER-OVERVIEW]**

系统必须支持用户使用邮箱和密码登录。

**验收标准：**
- ✅ 用户可以使用邮箱和密码登录
- ✅ 登录失败显示清晰的错误消息
- ✅ 连续 5 次登录失败后锁定账户 15 分钟
- ✅ 登录成功后返回 JWT token

## 3. User Profile Requirements

### 3.1 Profile Management
**[ID: RD-USER-PROFILE-001] [Module: User] [Decomposes: RD-USER-OVERVIEW]**

系统必须允许用户查看和编辑个人资料。

**可编辑字段：**
- 姓名
- 头像
- 电话号码
- 地址

**验收标准：**
- ✅ 用户可以查看完整个人资料
- ✅ 用户可以编辑个人资料字段
- ✅ 修改成功后显示确认消息
- ✅ 邮箱不可直接修改（需要验证流程）

## 4. Role and Permission Requirements

### 4.1 Role-Based Access Control (RBAC)
**[ID: RD-USER-RBAC-001] [Module: User] [Decomposes: RD-USER-OVERVIEW] [Implements: RD-CROSS-AUTH-001]**

系统必须支持基于角色的访问控制。

**角色定义：**
- **User**（普通用户）：可以浏览商品、创建订单、查看个人订单
- **Merchant**（商家）：可以管理自己的商品、查看订单、处理退款
- **Admin**（管理员）：可以管理所有用户、商品、订单

**验收标准：**
- ✅ 用户注册时默认角色为 User
- ✅ Admin 可以修改用户角色
- ✅ API 端点根据角色验证权限
- ✅ 权限不足时返回 403 Forbidden

## 5. Password Recovery Requirements

### 5.1 Password Reset
**[ID: RD-USER-RESET-001] [Module: User] [Decomposes: RD-USER-OVERVIEW]**

系统必须支持密码重置功能。

**验收标准：**
- ✅ 用户可以请求密码重置（通过邮箱）
- ✅ 系统发送密码重置链接到用户邮箱
- ✅ 重置链接 1 小时内有效
- ✅ 用户可以通过链接设置新密码
- ✅ 新密码必须满足密码复杂度要求
```

#### Step 2: Repeat for Other Modules

为每个模块生成模块文档：
- RD-Order.md（Order 模块）
- RD-Payment.md（Payment 模块）
- RD-Product.md（Product 模块）
- RD-Notification.md（Notification 模块）

#### Step 3: Generate Module PRD, Design, Test Plan

对每个模块，依次生成：
1. PRD-[Module].md - 使用 `prd-module-generator.md`
2. Design-Document-[Module].md - 使用 `design-module-generator.md`
3. Test-Plan-[Module].md - 使用 `test-plan-module-generator.md`

## Traceability Tags for Large Projects

### Module Tag

所有模块文档使用 `[Module: XXX]` 标记：

```markdown
**[ID: RD-USER-REG-001] [Module: User] [Decomposes: RD-USER-OVERVIEW]**
**[ID: PRD-ORDER-CREATE] [Module: Order] [Implements: RD-ORDER-CREATE-001]**
**[ID: DESIGN-PAYMENT-API-001] [Module: Payment] [Designs-for: PRD-PAYMENT-PROCESS]**
**[ID: TEST-PRODUCT-SEARCH] [Module: Product] [Tests-for: DESIGN-PRODUCT-SEARCH-001]**
```

### Cross-Module Dependencies

跨模块依赖使用 `[Depends-on: MODULE:ID]`：

```markdown
### 2.1 Create Order
**[ID: PRD-ORDER-CREATE] [Module: Order] [Implements: RD-ORDER-CREATE-001]**
**[Depends-on: User:RD-USER-LOGIN-001, Payment:RD-PAYMENT-PROCESS-001]**

用户必须登录后才能创建订单，订单创建后需要调用支付模块处理支付。
```

## Task Management for Large Projects

### Epic per Module

在 `.specgov/tasks/project-manager.md` 为每个模块创建独立 Epic：

```markdown
## Active Epics

### Epic 1: User Module Implementation
- **模块**：User
- **进度**：40%
- ✅ RD-User.md 完成
- ✅ PRD-User.md 完成
- ⏳ Design-Document-User.md 进行中
- ⬜ Test-Plan-User.md
- ⬜ 代码实现

### Epic 2: Order Module Implementation
- **模块**：Order
- **进度**：20%
- ✅ RD-Order.md 完成
- ⏳ PRD-Order.md 进行中
- ⬜ Design-Document-Order.md
- ⬜ Test-Plan-Order.md
- ⬜ 代码实现
```

### Role Tasks per Module

在各角色的任务文件中按模块组织任务：

**`.specgov/tasks/rd-analyst.md`**
```markdown
## Active Tasks

### Task 1: 生成 RD-User.md
- **Epic**：Epic 1 - User Module
- **模块**：User
- **状态**：已完成

### Task 2: 生成 RD-Order.md
- **Epic**：Epic 2 - Order Module
- **模块**：Order
- **状态**：已完成

### Task 3: 生成 RD-Payment.md
- **Epic**：Epic 3 - Payment Module
- **模块**：Payment
- **状态**：进行中
```

## Helper Scripts for Large Projects

### Parse Tags with Module Filter

```powershell
# 解析所有标记
python scripts/parse_tags.py

# 只解析特定模块
python scripts/parse_tags.py --module User
```

### Build Graph with Module Scope

```powershell
# 构建完整依赖图谱
python scripts/build_graph.py

# 只构建特定模块的依赖图谱
python scripts/build_graph.py --module User
```

### Check Consistency per Module

```powershell
# 检查特定模块的一致性
python scripts/check_consistency.py --module User

# 检查跨模块依赖
python scripts/check_consistency.py --cross-module
```

### Impact Analysis per Module

```powershell
# 分析特定需求的影响（限定模块范围）
python scripts/impact_analysis.py --id RD-USER-REG-001 --module User

# 分析跨模块影响
python scripts/impact_analysis.py --id RD-CROSS-AUTH-001 --cross-module
```

## Best Practices for Large Projects

### 1. Start with Overview Documents

- 首先生成 RD.md, PRD.md, Design-Document.md, Test-Plan.md（Overview）
- 定义模块边界和跨模块需求
- 确保所有模块对整体架构有统一理解

### 2. One Module at a Time

- 一次专注于一个模块
- 完成一个模块的所有 SDLC 阶段后再开始下一个模块
- 避免多个模块并行导致混乱

### 3. Define Module Boundaries Clearly

- 明确定义每个模块的范围
- 使用 `[Module: XXX]` 标记所有模块内容
- 跨模块依赖必须显式声明（`[Depends-on: MODULE:ID]`）

### 4. Use Consistent Naming Conventions

- 模块名称使用 PascalCase（User, Order, Payment）
- 文件名使用 kebab-case（RD-User.md, Design-Document-Order.md）
- ID 前缀包含模块名（RD-USER-XXX, PRD-ORDER-XXX）

### 5. Review Cross-Cutting Requirements Regularly

- 定期审查跨模块需求（RD-CROSS-XXX）
- 确保所有模块遵守跨模块需求
- 使用 consistency checker 验证跨模块一致性

### 6. Maintain Traceability Across Modules

- 跨模块依赖必须使用 `[Depends-on: MODULE:ID]`
- 使用 impact analyzer 分析跨模块影响
- 定期运行 `build_graph.py --cross-module` 验证依赖图谱

## Common Pitfalls

- ❌ 模块边界不清晰，导致职责重叠
- ❌ 跨模块依赖未显式声明
- ❌ 忘记使用 `[Module: XXX]` 标记
- ❌ 多个模块并行开发导致依赖混乱
- ❌ 跨模块需求定义不明确
- ❌ 未定期运行 helper scripts 验证一致性

## Validation Checklist

- [ ] 已定义所有功能模块
- [ ] 已生成 Overview 文档（RD.md, PRD.md, Design-Document.md, Test-Plan.md）
- [ ] 每个模块都有独立的模块文档（RD-[Module].md 等）
- [ ] 所有模块内容都有 `[Module: XXX]` 标记
- [ ] 跨模块依赖已显式声明（`[Depends-on: MODULE:ID]`）
- [ ] 跨模块需求已定义并被所有模块遵守
- [ ] Helper scripts 可以正确解析模块标记
- [ ] 依赖图谱包含跨模块依赖
- [ ] 每个模块都有对应的 Epic
- [ ] 任务文档按模块组织

## Quick Reference Commands

```powershell
# 解析特定模块标记
python scripts/parse_tags.py --module User

# 构建特定模块依赖图谱
python scripts/build_graph.py --module User

# 检查跨模块一致性
python scripts/check_consistency.py --cross-module

# 分析跨模块影响
python scripts/impact_analysis.py --id RD-CROSS-AUTH-001 --cross-module

# 提交模块文档
git add docs/RD-User.md docs/PRD-User.md
git commit -m "Add User module requirements and product features"
```

## Example: E-Commerce Platform Workflow

### Step 1: Define Modules

```markdown
模块：
1. User - 用户注册、登录、个人资料管理
2. Order - 订单创建、查询、修改、取消
3. Payment - 支付处理、退款
4. Product - 商品管理、库存
5. Notification - 邮件、短信、推送通知
```

### Step 2: Generate Overview Documents

1. 生成 RD.md（整体需求概览）
2. 生成 PRD.md（整体产品概览）
3. 生成 Design-Document.md（整体架构概览）
4. 生成 Test-Plan.md（整体测试策略）

### Step 3: Implement User Module

1. 生成 RD-User.md
2. 审查 RD-User.md
3. 生成 PRD-User.md
4. 审查 PRD-User.md
5. 生成 Design-Document-User.md
6. 审查 Design-Document-User.md
7. 生成 Test-Plan-User.md
8. 审查 Test-Plan-User.md
9. 实现代码（用户注册、登录、个人资料）
10. 运行测试
11. 标记 Epic 1 完成

### Step 4: Implement Order Module

重复 User 模块的流程...

### Step 5: Implement Remaining Modules

重复流程直到所有模块完成。

---

**Estimated Time per Module**: 10-20 hours (depending on complexity)
**Estimated Cost per Module**: $8-15 (Claude Code usage)
**Total Project Time**: 50-100 hours (5 modules)
**Total Project Cost**: $40-75

**Tips**:
- 大项目需要良好的模块划分和清晰的边界定义
- 使用 Overview 文档确保所有模块对整体架构有统一理解
- 定期运行 helper scripts 验证跨模块一致性
- 一次专注于一个模块，避免并行导致混乱
