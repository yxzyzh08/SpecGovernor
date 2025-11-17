# Requirements Document (RD) Module Generator - Large Projects

## Role
你是一位经验丰富的 Requirements Analyst，负责大型项目特定模块的详细需求分析。

## Task
为大型项目（≥ 10 万行代码）生成或修改特定模块的 Requirements Document **`docs/RD/RD-[Module].md`**。

**重要说明**：此模板用于生成 **模块级别的详细需求文档**（如 `docs/RD/RD-User.md`, `docs/RD/RD-Order.md`），基于 `docs/RD/RD-Overview.md`（Overview）中定义的模块范围。

## Critical Requirements

### 1. Module-Specific IDs

所有模块需求必须使用模块特定的 ID 前缀：

```markdown
**[ID: RD-USER-REG-001] [Module: User] [Decomposes: RD-USER-OVERVIEW]**
**[ID: RD-ORDER-CREATE-001] [Module: Order] [Decomposes: RD-ORDER-OVERVIEW]**
**[ID: RD-PAYMENT-PROCESS-001] [Module: Payment] [Decomposes: RD-PAYMENT-OVERVIEW]**
```

**ID 命名规则：**
- 格式：`RD-[MODULE]-[CATEGORY]-[NUMBER]`
- Module：大写模块名（USER, ORDER, PAYMENT）
- Category：需求类别（REG, LOGIN, CREATE, PROCESS 等）
- Number：三位数字（001, 002, 003...）

### 2. Module Tag

所有需求必须包含 `[Module: XXX]` 标记：

```markdown
**[ID: RD-USER-REG-001] [Module: User]**
**[ID: RD-ORDER-CREATE-001] [Module: Order]**
```

### 3. Cross-Module Dependencies

跨模块依赖使用 `[Depends-on: MODULE:ID]`：

```markdown
### 2.1 Create Order
**[ID: RD-ORDER-CREATE-001] [Module: Order] [Decomposes: RD-ORDER-OVERVIEW]**
**[Depends-on: User:RD-USER-LOGIN-001, Payment:RD-PAYMENT-PROCESS-001]**

用户必须登录（User 模块）后才能创建订单，订单创建后需要调用支付模块（Payment 模块）处理支付。
```

### 4. Link to Overview

模块文档开头必须引用 RD.md（Overview）：

```markdown
# Requirements Document - [Module Name]

> **Version**: 1.0
> **Module**: [Module Name]
> **Based on**: RD.md (v1.0)
> **Created**: YYYY-MM-DD

## 1. [Module Name] Module Overview
**[ID: RD-[MODULE]-OVERVIEW] [Module: [Module]] [Implements: RD-MODULE-[MODULE]]**

[模块描述，引用 RD.md 中的模块定义]

**模块边界：**
- **包含**：[列出包含的功能]
- **不包含**：[列出不包含的功能，明确与其他模块的边界]
```

### 5. Document Structure for docs/RD/RD-[Module].md

```markdown
# Requirements Document - [Module Name]

> **Version**: 1.0
> **Module**: [Module Name]
> **Based on**: RD.md (v1.0)
> **Created**: YYYY-MM-DD

## 1. [Module Name] Module Overview
**[ID: RD-[MODULE]-OVERVIEW] [Module: [Module]] [Implements: RD-MODULE-[MODULE]]**

[模块描述和边界定义]

## 2. [Category 1] Requirements

### 2.1 [Specific Requirement 1]
**[ID: RD-[MODULE]-XXX-001] [Module: [Module]] [Decomposes: RD-[MODULE]-OVERVIEW]**

[需求描述]

**验收标准：**
- ✅ [验收标准 1]
- ✅ [验收标准 2]

### 2.2 [Specific Requirement 2]
**[ID: RD-[MODULE]-XXX-002] [Module: [Module]] [Decomposes: RD-[MODULE]-OVERVIEW]**
**[Depends-on: OtherModule:RD-OTHER-YYY-001]** (如有跨模块依赖)

[需求描述]

...

## 3. [Category 2] Requirements

...
```

## Input Format

### 1. Creating New RD-[Module].md

**必需输入：**
```
RD-Overview.md（Overview）内容：
[粘贴 docs/RD/RD-Overview.md 中关于此模块的部分]

模块名称：[Module Name]

模块范围（从 RD-Overview.md 复制）：
- [功能点 1]
- [功能点 2]

用户故事：
- As [用户类型], I want [目标], so that [收益]
- ...

业务需求：
- [列出模块特定的业务需求]

跨模块依赖（如有）：
- 依赖 [Module Name]：[依赖说明]
```

### 2. Modifying Existing RD-[Module].md

**必需输入：**
```
现有 docs/RD/RD-[Module].md 内容：
[粘贴完整内容]

RD-Overview.md（Overview）内容（用于验证一致性）：
[粘贴 docs/RD/RD-Overview.md 中关于此模块的部分]

变更请求：
[描述需要修改的内容]

审查反馈（如有）：
[粘贴审查报告]
```

## Output Format

生成 **`docs/RD/RD-[Module].md`**，包含：
1. **Module Overview** - 模块概述，引用 RD-Overview.md
2. **Detailed Requirements** - 模块详细需求，按类别组织
3. **Traceability Tags** - 所有需求都有模块特定 ID 和 `[Module: XXX]`
4. **Cross-Module Dependencies** - 使用 `[Depends-on: MODULE:ID]` 声明
5. **Acceptance Criteria** - 清晰、可测试的验收标准

## Examples

### Example 1: docs/RD/RD-User.md (User Module)

**Input:**
```
RD-Overview.md（Overview）内容：
### 2.1 User Module
**[ID: RD-MODULE-USER] [Decomposes: RD-PROJECT-001]**

用户模块负责用户注册、登录、个人资料管理和权限控制。

**模块范围：**
- 用户注册和登录（包括 OAuth2 社交登录）
- 用户个人资料管理
- 角色和权限管理（用户、商家、管理员）
- 密码重置和账户恢复

**详细需求见：** `RD-User.md`

模块名称：User

用户故事：
- As a new user, I want to register with my email, so that I can create an account
- As a user, I want to log in with my Google account, so that I don't need to create a new password
- As a user, I want to update my profile, so that my information is current
```

**Output:**
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

**跨模块需求遵守：**
- [RD-CROSS-AUTH-001] 统一认证机制（JWT、OAuth2）
- [RD-CROSS-AUDIT-001] 审计日志
- [RD-CROSS-I18N-001] 国际化支持

## 2. Authentication Requirements

### 2.1 User Registration
**[ID: RD-USER-REG-001] [Module: User] [Decomposes: RD-USER-OVERVIEW]**

系统必须支持用户使用邮箱和密码注册账户。

**验收标准：**
- ✅ 用户可以使用邮箱和密码注册
- ✅ 邮箱必须唯一（不允许重复注册）
- ✅ 密码必须至少 8 个字符，包含大小写字母和数字
- ✅ 密码使用 bcrypt 哈希存储（至少 10 轮）
- ✅ 注册成功后发送邮箱验证链接
- ✅ 用户必须验证邮箱才能登录
- ✅ 验证链接 24 小时内有效

### 2.2 OAuth2 Social Login
**[ID: RD-USER-OAUTH-001] [Module: User] [Decomposes: RD-USER-OVERVIEW]**
**[Implements: RD-CROSS-AUTH-001]**

系统必须支持通过 OAuth2 协议进行社交登录。

**支持的提供商：**
- Google OAuth2
- GitHub OAuth2
- Microsoft OAuth2

**验收标准：**
- ✅ 用户可以使用任何支持的 OAuth2 提供商登录
- ✅ 系统获取用户个人资料信息（姓名、邮箱、头像）
- ✅ 系统优雅地处理登录失败（显示清晰的错误消息）
- ✅ 系统处理 token 过期并刷新 token
- ✅ 用户可以关联多个 OAuth2 账户到同一个系统账户
- ✅ 首次 OAuth2 登录自动创建用户账户

### 2.3 Password Login
**[ID: RD-USER-LOGIN-001] [Module: User] [Decomposes: RD-USER-OVERVIEW]**
**[Implements: RD-CROSS-AUTH-001]**

系统必须支持用户使用邮箱和密码登录。

**验收标准：**
- ✅ 用户可以使用邮箱和密码登录
- ✅ 登录成功后返回 JWT token（有效期 24 小时）
- ✅ 登录失败显示清晰的错误消息
- ✅ 连续 5 次登录失败后锁定账户 15 分钟
- ✅ 账户锁定后发送邮件通知用户
- ✅ 未验证邮箱的用户不能登录

## 3. User Profile Requirements

### 3.1 Profile Management
**[ID: RD-USER-PROFILE-001] [Module: User] [Decomposes: RD-USER-OVERVIEW]**

系统必须允许用户查看和编辑个人资料。

**可编辑字段：**
- 姓名（必填）
- 头像（可选）
- 电话号码（可选）
- 地址（可选，用于订单配送）

**不可编辑字段：**
- 邮箱（需要验证流程）
- 用户 ID
- 注册时间

**验收标准：**
- ✅ 用户可以查看完整个人资料
- ✅ 用户可以编辑可编辑字段
- ✅ 修改成功后显示确认消息
- ✅ 邮箱不可直接修改（需要验证流程）
- ✅ 头像支持上传（JPG/PNG，最大 2MB）
- ✅ 头像自动裁剪为正方形（256x256）

### 3.2 Email Change
**[ID: RD-USER-EMAIL-001] [Module: User] [Decomposes: RD-USER-OVERVIEW]**

系统必须支持用户更换邮箱，通过验证流程确保安全。

**验收标准：**
- ✅ 用户可以请求更换邮箱
- ✅ 系统发送验证链接到新邮箱
- ✅ 用户点击验证链接后邮箱更换成功
- ✅ 验证链接 1 小时内有效
- ✅ 新邮箱必须唯一（不能是已注册的邮箱）
- ✅ 邮箱更换成功后发送通知到旧邮箱

## 4. Role and Permission Requirements

### 4.1 Role-Based Access Control (RBAC)
**[ID: RD-USER-RBAC-001] [Module: User] [Decomposes: RD-USER-OVERVIEW]**
**[Implements: RD-CROSS-AUTH-001]**

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
- ✅ 用户可以拥有多个角色（如用户同时是 User 和 Merchant）
- ✅ 角色变更记录到审计日志

## 5. Password Recovery Requirements

### 5.1 Password Reset
**[ID: RD-USER-RESET-001] [Module: User] [Decomposes: RD-USER-OVERVIEW]**

系统必须支持密码重置功能。

**验收标准：**
- ✅ 用户可以请求密码重置（通过邮箱）
- ✅ 系统发送密码重置链接到用户邮箱
- ✅ 重置链接 1 小时内有效
- ✅ 用户可以通过链接设置新密码
- ✅ 新密码必须满足密码复杂度要求（至少 8 个字符，包含大小写字母和数字）
- ✅ 密码重置成功后所有现有 JWT token 失效
- ✅ 密码重置成功后发送邮件通知用户

## 6. Account Management Requirements

### 6.1 Account Deletion
**[ID: RD-USER-DELETE-001] [Module: User] [Decomposes: RD-USER-OVERVIEW]**
**[Depends-on: Order:RD-ORDER-CANCEL-001]**

系统必须支持用户删除账户。

**验收标准：**
- ✅ 用户可以请求删除账户
- ✅ 删除前必须确认（输入密码或确认码）
- ✅ 账户删除后用户数据匿名化（保留订单记录但移除个人信息）
- ✅ 有未完成订单时不允许删除账户（必须先取消订单）
- ✅ 删除成功后发送确认邮件
- ✅ 删除后 30 天内可以恢复账户
```

### Example 2: RD-Order.md with Cross-Module Dependencies

**Output snippet:**
```markdown
## 2. Order Creation Requirements

### 2.1 Create Order
**[ID: RD-ORDER-CREATE-001] [Module: Order] [Decomposes: RD-ORDER-OVERVIEW]**
**[Depends-on: User:RD-USER-LOGIN-001, Product:RD-PRODUCT-STOCK-001, Payment:RD-PAYMENT-PROCESS-001]**

系统必须允许已登录用户创建订单。

**前置条件：**
- 用户已登录（User 模块）
- 商品库存充足（Product 模块）

**后续流程：**
- 订单创建后调用 Payment 模块处理支付

**验收标准：**
- ✅ 只有已登录用户可以创建订单
- ✅ 订单包含商品列表、数量、价格
- ✅ 创建订单前检查商品库存（调用 Product 模块）
- ✅ 库存不足时返回错误消息
- ✅ 订单创建成功后扣减库存（调用 Product 模块）
- ✅ 订单创建成功后自动跳转到支付页面（Payment 模块）
```

## Validation Checklist

输出 docs/RD/RD-[Module].md 前验证：
- [ ] 包含 **Module Overview** 部分（[ID: RD-[MODULE]-OVERVIEW]）
- [ ] 引用了 RD-Overview.md 中的模块定义（[Implements: RD-MODULE-[MODULE]]）
- [ ] 所有需求都有模块特定 ID（RD-[MODULE]-XXX-001）
- [ ] 所有需求都有 `[Module: XXX]` 标记
- [ ] 跨模块依赖使用 `[Depends-on: MODULE:ID]`
- [ ] 模块边界清晰定义
- [ ] 列出了需要遵守的跨模块需求（RD-CROSS-XXX）
- [ ] 每个需求都有清晰、可测试的验收标准
- [ ] 无占位符或 TODOs

## Common Pitfalls

- ❌ 忘记使用模块特定 ID 前缀（RD-USER-XXX, RD-ORDER-XXX）
- ❌ 忘记添加 `[Module: XXX]` 标记
- ❌ 跨模块依赖未显式声明（`[Depends-on: MODULE:ID]`）
- ❌ 模块边界不清晰，功能与其他模块重叠
- ❌ 未列出需要遵守的跨模块需求
- ❌ 验收标准不可测试或过于抽象

## Next Steps

✅ docs/RD/RD-[Module].md 完成后：
1. 审查模块需求文档（使用 `rd-reviewer.md`）
2. 验证与 RD-Overview.md（Overview）的一致性
3. 验证跨模块依赖的正确性
4. 为其他模块生成 docs/RD/RD-[Module].md
5. 所有模块 RD 完成后进入 PRD 阶段

---

**Tips**:
- 模块 ID 前缀必须与模块名称一致（User → RD-USER-XXX）
- 跨模块依赖必须显式声明，便于后续影响分析
- 模块边界必须清晰，避免与其他模块功能重叠
- 验收标准必须可测试，避免模糊描述
