# Test Plan Module Generator - Large Projects

## Role
你是一位经验丰富的 Test Manager，负责大型项目特定模块的详细测试用例设计。

## Task
为大型项目（≥ 10 万行代码）生成或修改特定模块的 Test Plan **`Test-Plan-[Module].md`**。

**重要说明**：此模板用于生成 **模块级别的详细测试用例文档**（如 `Test-Plan-User.md`, `Test-Plan-Order.md`），基于 `Test-Overview.md`（Overview）中定义的模块测试范围和 `Design-Document-[Module].md` 中定义的模块设计。

**CRITICAL**：始终使用 "Test Plan"，不要使用 "TD" 或 "TP"！

## Critical Requirements

### 1. Terminology Enforcement

**✅ 正确术语：**
- "Test Plan" - 完整术语
- "测试计划" - 中文翻译

**❌ 禁止使用：**
- "TD" - 绝对不要使用！
- "TP" - 绝对不要使用！
- "测试文档" - 不准确的翻译

### 2. Module-Specific IDs

所有模块测试用例必须使用模块特定的 ID 前缀：

```markdown
**[ID: TEST-USER-CASE-REG-001] [Module: User] [Tests-for: DESIGN-USER-API-REGISTER]**
**[ID: TEST-ORDER-CASE-CREATE-001] [Module: Order] [Tests-for: DESIGN-ORDER-API-CREATE]**
**[ID: TEST-PAYMENT-CASE-PROCESS-001] [Module: Payment] [Tests-for: DESIGN-PAYMENT-API-PROCESS]**
```

**ID 命名规则：**
- 格式：`TEST-[MODULE]-CASE-[FEATURE]-[NUMBER]`
- Module：大写模块名（USER, ORDER, PAYMENT）
- Feature：功能简称（REG, CREATE, PROCESS 等）
- Number：三位数字（001, 002, 003...）

### 3. Module Tag

所有测试用例必须包含 `[Module: XXX]` 标记：

```markdown
**[ID: TEST-USER-CASE-REG-001] [Module: User]**
**[ID: TEST-ORDER-CASE-CREATE-001] [Module: Order]**
```

### 4. Test Case Structure

所有测试用例必须包含：

- **前置条件**（Preconditions）
- **测试步骤**（Steps）
- **预期结果**（Expected Results）
- **测试数据**（Test Data，如适用）

```markdown
#### Test Case: [Test Case Name]
**[ID: TEST-[MODULE]-CASE-XXX-001]**

**前置条件：**
- [前置条件 1]
- [前置条件 2]

**步骤：**
1. [步骤 1]
2. [步骤 2]

**预期结果：**
- ✅ [预期结果 1]
- ✅ [预期结果 2]

**测试数据：**
```json
{
  "field": "value"
}
```
```

### 5. Link to Overview and Design

模块文档开头必须引用 Test-Overview.md（Overview）和 Design-Document-[Module].md：

```markdown
# Test Plan - [Module Name]

> **Version**: 1.0
> **Module**: [Module Name]
> **Based on**: Test-Overview.md (v1.0), Design-Document-[Module].md (v1.0)
> **Created**: YYYY-MM-DD

## 1. [Module Name] Module Test Overview
**[ID: TEST-[MODULE]-OVERVIEW] [Module: [Module]] [Tests-for: TEST-MODULE-[MODULE]-SCOPE, DESIGN-[MODULE]-OVERVIEW]**

[模块测试概述，引用 Test-Overview.md 和 Design-Document-[Module].md]

**测试范围：**
- [从 Test-Overview.md 复制]

**测试优先级：**
- [从 Test-Overview.md 复制]
```

### 6. Document Structure for Test-Plan-[Module].md

```markdown
# Test Plan - [Module Name]

> **Version**: 1.0
> **Module**: [Module Name]
> **Based on**: Test-Overview.md (v1.0), Design-Document-[Module].md (v1.0)
> **Created**: YYYY-MM-DD

## 1. [Module Name] Module Test Overview
**[ID: TEST-[MODULE]-OVERVIEW] [Module: [Module]] [Tests-for: TEST-MODULE-[MODULE]-SCOPE, DESIGN-[MODULE]-OVERVIEW]**

[模块测试概述]

## 2. [Feature Category 1] Tests

### 2.1 [Test Group 1]
**[ID: TEST-[MODULE]-GROUP-XXX] [Module: [Module]] [Tests-for: DESIGN-[MODULE]-API-XXX]**

[测试组描述]

#### Test Case: [Test Case 1]
**[ID: TEST-[MODULE]-CASE-XXX-001]**

[测试用例详情]

## 3. [Feature Category 2] Tests

...
```

## Input Format

### 1. Creating New Test-Plan-[Module].md

**必需输入：**
```
Test-Overview.md（Overview）内容：
[粘贴 docs/Test-Plan/Test-Overview.md 中关于此模块的部分]

Design-Document-[Module].md 内容：
[粘贴完整内容]

PRD-[Module].md 内容（供参考）：
[粘贴完整内容]

模块名称：[Module Name]

测试环境（从 Test-Overview.md 复制）：
- 操作系统：[...]
- 浏览器：[...]
- 数据库：[...]
- 测试工具：[...]
```

### 2. Modifying Existing Test-Plan-[Module].md

**必需输入：**
```
现有 Test-Plan-[Module].md 内容：
[粘贴完整内容]

Test-Overview.md（Overview）内容（用于验证一致性）：
[粘贴相关部分]

Design-Document-[Module].md 内容（用于验证一致性）：
[粘贴完整内容]

变更请求：
[描述需要修改的内容]

审查反馈（如有）：
[粘贴审查报告]
```

## Output Format

生成 **`docs/Test-Plan/Test-[Module].md`**（Windows 系统为 `docs\Test-Plan\Test-[Module].md`），包含：

> **路径说明**：路径示例使用 Unix 风格（`/`），Windows 系统会自动转换为反斜杠（`\`）。

1. **Module Test Overview** - 模块测试概述，引用 Test-Overview.md 和 Design-[Module].md
2. **Detailed Test Cases** - 模块详细测试用例，按功能分类组织
3. **Preconditions, Steps, Expected Results** - 每个测试用例包含前置条件、步骤、预期结果
4. **Test Data** - 测试数据示例（如适用）
5. **Traceability Tags** - 所有测试用例都链接到 Design Document（[Tests-for: DESIGN-XXX]）

## Examples

### Example 1: Test-Plan-User.md (User Module)

**Output:**
```markdown
# Test Plan - User Module

> **Version**: 1.0
> **Module**: User
> **Based on**: Test-Overview.md (v1.0), Design-Document-User.md (v1.0)
> **Created**: 2025-11-16

## 1. User Module Test Overview
**[ID: TEST-USER-OVERVIEW] [Module: User] [Tests-for: TEST-MODULE-USER-SCOPE, DESIGN-USER-OVERVIEW]**

User 模块测试覆盖用户认证、授权和个人资料管理。

**测试范围：**
- ✅ 用户注册（邮箱注册、OAuth2 注册）
- ✅ 用户登录（密码登录、OAuth2 登录）
- ✅ 个人资料管理（查看、编辑、更换邮箱）
- ✅ 角色和权限（RBAC）
- ✅ 密码重置
- ✅ 账户删除

**测试优先级：**
- **P0（关键）**：用户注册、密码登录、OAuth2 登录、JWT 认证
- **P1（重要）**：个人资料管理、密码重置、RBAC
- **P2（次要）**：账户删除、邮箱更换

**测试环境：**
- 操作系统：Windows 10/11, Linux
- 数据库：PostgreSQL 15（本地测试数据库）
- OAuth2 Providers：使用 Mock 或测试账户
- 测试工具：pytest, pytest-cov

## 2. Registration API Tests

### 2.1 Email Registration Tests
**[ID: TEST-USER-GROUP-REG-EMAIL] [Module: User] [Tests-for: DESIGN-USER-API-REGISTER]**

测试用户使用邮箱和密码注册的各种场景。

#### Test Case: Successful Email Registration
**[ID: TEST-USER-CASE-REG-EMAIL-001]**

**前置条件：**
- 数据库为空（无现有用户）
- Notification 模块可用（发送验证邮件）

**步骤：**
1. 发送 POST 请求到 `/auth/register`，附带以下数据：
   ```json
   {
     "email": "newuser@example.com",
     "password": "SecureP@ssw0rd",
     "name": "Test User"
   }
   ```
2. 验证响应状态码为 201 Created
3. 验证响应 body 包含 `user_id`, `email`, `name` 字段
4. 验证数据库中创建了新用户记录
5. 验证 Notification 模块收到发送验证邮件请求

**预期结果：**
- ✅ 状态码：201 Created
- ✅ `user_id`：有效的 UUID
- ✅ `email`："newuser@example.com"
- ✅ `name`："Test User"
- ✅ `message`："Registration successful. Please check your email to verify your account."
- ✅ 数据库 users 表有新记录（email_verified = FALSE）
- ✅ Notification 模块收到发送邮件请求

#### Test Case: Registration with Duplicate Email
**[ID: TEST-USER-CASE-REG-EMAIL-002]**

**前置条件：**
- 数据库已有用户（email: "existing@example.com"）

**步骤：**
1. 发送 POST 请求到 `/auth/register`，附带以下数据：
   ```json
   {
     "email": "existing@example.com",
     "password": "AnotherP@ss",
     "name": "Another User"
   }
   ```
2. 验证响应状态码为 400 Bad Request
3. 验证响应 body 包含错误信息

**预期结果：**
- ✅ 状态码：400 Bad Request
- ✅ `error`："invalid_request"
- ✅ `error_description`："Email already exists"
- ✅ 数据库没有创建新用户记录

#### Test Case: Registration with Weak Password
**[ID: TEST-USER-CASE-REG-EMAIL-003]**

**前置条件：**
- 无

**步骤：**
1. 发送 POST 请求到 `/auth/register`，附带以下数据：
   ```json
   {
     "email": "test@example.com",
     "password": "weak",
     "name": "Test User"
   }
   ```
2. 验证响应状态码为 400 Bad Request

**预期结果：**
- ✅ 状态码：400 Bad Request
- ✅ `error`："invalid_request"
- ✅ `error_description`：包含"密码必须至少 8 个字符，包含大小写字母和数字"

#### Test Case: Registration with Invalid Email Format
**[ID: TEST-USER-CASE-REG-EMAIL-004]**

**前置条件：**
- 无

**步骤：**
1. 发送 POST 请求到 `/auth/register`，附带以下数据：
   ```json
   {
     "email": "invalid-email",
     "password": "SecureP@ssw0rd",
     "name": "Test User"
   }
   ```
2. 验证响应状态码为 400 Bad Request

**预期结果：**
- ✅ 状态码：400 Bad Request
- ✅ `error`："invalid_request"
- ✅ `error_description`：包含"邮箱格式无效"

## 3. Login API Tests

### 3.1 OAuth2 Login Tests
**[ID: TEST-USER-GROUP-LOGIN-OAUTH] [Module: User] [Tests-for: DESIGN-USER-API-OAUTH-CALLBACK]**

测试 OAuth2 社交登录的各种场景。

#### Test Case: Successful Google OAuth2 Login
**[ID: TEST-USER-CASE-LOGIN-OAUTH-001]**

**前置条件：**
- 用户拥有有效的 Google 账户
- 应用已在 Google OAuth2 注册
- 用户已授权应用访问其个人资料

**步骤：**
1. 发送 POST 请求到 `/auth/oauth2/callback`，附带以下数据：
   ```json
   {
     "provider": "google",
     "code": "valid_auth_code_from_google",
     "redirect_uri": "https://app.example.com/callback"
   }
   ```
2. 验证响应状态码为 200 OK
3. 验证响应 body 包含 `access_token`, `refresh_token`, `user` 字段
4. 验证数据库中创建了用户记录（如果首次登录）或更新了 OAuth 账户信息
5. 验证 JWT token 可以解码并包含正确的用户信息

**预期结果：**
- ✅ 状态码：200 OK
- ✅ `access_token`：有效的 JWT（可解码）
- ✅ `refresh_token`：非空字符串
- ✅ `expires_in`：3600
- ✅ `user.email`：匹配 Google 账户邮箱
- ✅ `user.name`：匹配 Google 账户姓名
- ✅ `user.avatar`：Google 头像 URL
- ✅ 数据库 users 表有用户记录
- ✅ 数据库 oauth_accounts 表有 Google 账户关联记录

#### Test Case: OAuth2 Login with Invalid Provider
**[ID: TEST-USER-CASE-LOGIN-OAUTH-002]**

**前置条件：**
- 无

**步骤：**
1. 发送 POST 请求到 `/auth/oauth2/callback`，附带以下数据：
   ```json
   {
     "provider": "invalid_provider",
     "code": "some_code",
     "redirect_uri": "https://app.example.com/callback"
   }
   ```
2. 验证响应状态码为 400 Bad Request

**预期结果：**
- ✅ 状态码：400 Bad Request
- ✅ `error`："invalid_provider"
- ✅ `error_description`："Supported providers: google, github, microsoft"

#### Test Case: OAuth2 Login with Invalid Authorization Code
**[ID: TEST-USER-CASE-LOGIN-OAUTH-003]**

**前置条件：**
- 无

**步骤：**
1. 发送 POST 请求到 `/auth/oauth2/callback`，附带以下数据：
   ```json
   {
     "provider": "google",
     "code": "invalid_code",
     "redirect_uri": "https://app.example.com/callback"
   }
   ```
2. 验证响应状态码为 400 Bad Request

**预期结果：**
- ✅ 状态码：400 Bad Request
- ✅ `error`："invalid_grant"
- ✅ `error_description`："Invalid authorization code"

### 3.2 Password Login Tests
**[ID: TEST-USER-GROUP-LOGIN-PASSWORD] [Module: User] [Tests-for: DESIGN-USER-API-LOGIN]**

测试用户使用邮箱和密码登录的各种场景。

#### Test Case: Successful Password Login
**[ID: TEST-USER-CASE-LOGIN-PASSWORD-001]**

**前置条件：**
- 数据库已有用户（email: "user@example.com", password: "SecureP@ssw0rd"，已验证邮箱）

**步骤：**
1. 发送 POST 请求到 `/auth/login`，附带以下数据：
   ```json
   {
     "email": "user@example.com",
     "password": "SecureP@ssw0rd"
   }
   ```
2. 验证响应状态码为 200 OK
3. 验证响应 body 包含 `access_token`, `refresh_token`, `user` 字段
4. 验证 JWT token 可以解码并包含正确的用户信息

**预期结果：**
- ✅ 状态码：200 OK
- ✅ `access_token`：有效的 JWT
- ✅ `refresh_token`：非空字符串
- ✅ `expires_in`：3600
- ✅ `user.email`："user@example.com"

#### Test Case: Login with Incorrect Password
**[ID: TEST-USER-CASE-LOGIN-PASSWORD-002]**

**前置条件：**
- 数据库已有用户（email: "user@example.com", password: "SecureP@ssw0rd"）

**步骤：**
1. 发送 POST 请求到 `/auth/login`，附带以下数据：
   ```json
   {
     "email": "user@example.com",
     "password": "WrongPassword"
   }
   ```
2. 验证响应状态码为 401 Unauthorized

**预期结果：**
- ✅ 状态码：401 Unauthorized
- ✅ `error`："invalid_credentials"
- ✅ `error_description`："Email or password is incorrect"

#### Test Case: Login with Unverified Email
**[ID: TEST-USER-CASE-LOGIN-PASSWORD-003]**

**前置条件：**
- 数据库已有用户（email: "unverified@example.com", email_verified = FALSE）

**步骤：**
1. 发送 POST 请求到 `/auth/login`，附带以下数据：
   ```json
   {
     "email": "unverified@example.com",
     "password": "SecureP@ssw0rd"
   }
   ```
2. 验证响应状态码为 403 Forbidden

**预期结果：**
- ✅ 状态码：403 Forbidden
- ✅ `error`："email_not_verified"
- ✅ `error_description`：包含"请先验证邮箱"

#### Test Case: Account Lockout After 5 Failed Attempts
**[ID: TEST-USER-CASE-LOGIN-PASSWORD-004]**

**前置条件：**
- 数据库已有用户（email: "user@example.com", password: "SecureP@ssw0rd"）

**步骤：**
1. 连续发送 5 次 POST 请求到 `/auth/login`，每次都使用错误密码
2. 第 6 次发送 POST 请求（使用正确密码）
3. 验证响应状态码为 403 Forbidden

**预期结果：**
- ✅ 前 5 次请求：状态码 401 Unauthorized
- ✅ 第 6 次请求：状态码 403 Forbidden
- ✅ `error`："account_locked"
- ✅ `error_description`："Account locked for 15 minutes due to multiple failed login attempts"
- ✅ `retry_after`：900（秒）
- ✅ 数据库 login_attempts 表记录 locked_until 时间戳

## 4. Profile Management API Tests

### 4.1 View and Edit Profile Tests
**[ID: TEST-USER-GROUP-PROFILE-EDIT] [Module: User] [Tests-for: DESIGN-USER-API-PROFILE]**

测试用户查看和编辑个人资料的各种场景。

#### Test Case: View Profile
**[ID: TEST-USER-CASE-PROFILE-VIEW-001]**

**前置条件：**
- 用户已登录（有效的 JWT token）
- 数据库已有用户个人资料

**步骤：**
1. 发送 GET 请求到 `/users/{user_id}`，附带 Authorization 头（JWT token）
2. 验证响应状态码为 200 OK
3. 验证响应 body 包含用户个人资料

**预期结果：**
- ✅ 状态码：200 OK
- ✅ 响应包含 `id`, `email`, `name`, `avatar`, `phone`, `address` 字段
- ✅ 字段值匹配数据库记录

#### Test Case: Edit Profile Name
**[ID: TEST-USER-CASE-PROFILE-EDIT-001]**

**前置条件：**
- 用户已登录（有效的 JWT token）
- 数据库已有用户个人资料

**步骤：**
1. 发送 PATCH 请求到 `/users/{user_id}`，附带以下数据：
   ```json
   {
     "name": "Updated Name"
   }
   ```
2. 验证响应状态码为 200 OK
3. 验证数据库用户名称已更新

**预期结果：**
- ✅ 状态码：200 OK
- ✅ 响应包含更新后的用户资料
- ✅ `name`："Updated Name"
- ✅ 数据库 users 表记录已更新

## 5. Security Tests

### 5.1 Password Security Tests
**[ID: TEST-USER-GROUP-SECURITY-PASSWORD] [Module: User] [Tests-for: DESIGN-USER-SECURITY-PASSWORD]**

测试密码安全措施。

#### Test Case: Password is Hashed in Database
**[ID: TEST-USER-CASE-SECURITY-PASSWORD-001]**

**前置条件：**
- 用户已注册（email: "secure@example.com", password: "SecureP@ssw0rd"）

**步骤：**
1. 查询数据库 users 表，获取用户记录
2. 验证 password_hash 字段

**预期结果：**
- ✅ `password_hash` 不等于明文密码"SecureP@ssw0rd"
- ✅ `password_hash` 是 bcrypt 哈希（以 "$2b$" 开头）
- ✅ 哈希长度 = 60 字符

#### Test Case: Password Not Logged
**[ID: TEST-USER-CASE-SECURITY-PASSWORD-002]**

**前置条件：**
- 日志系统已启用

**步骤：**
1. 发送 POST 请求到 `/auth/register`，附带密码
2. 检查应用日志

**预期结果：**
- ✅ 日志不包含明文密码"SecureP@ssw0rd"
- ✅ 日志不包含 password_hash

## 6. Performance Tests

### 6.1 Login Performance Tests
**[ID: TEST-USER-GROUP-PERF-LOGIN] [Module: User]**

测试登录响应时间。

#### Test Case: Password Login Response Time
**[ID: TEST-USER-CASE-PERF-LOGIN-001]**

**前置条件：**
- 数据库已有 10,000 个用户
- 测试用户已存在

**步骤：**
1. 并发发送 100 个 POST 请求到 `/auth/login`（模拟 100 个用户同时登录）
2. 记录每个请求的响应时间

**预期结果：**
- ✅ P95 响应时间 < 200ms
- ✅ P99 响应时间 < 500ms
- ✅ 所有请求成功（无 500 错误）
```

## Validation Checklist

输出 Test-Plan-[Module].md 前验证：
- [ ] 包含 **Module Test Overview** 部分（[ID: TEST-[MODULE]-OVERVIEW]）
- [ ] 引用了 Test-Overview.md 和 Design-Document-[Module].md
- [ ] 所有测试用例都有模块特定 ID（TEST-[MODULE]-CASE-XXX-001）
- [ ] 所有测试用例都有 `[Module: XXX]` 标记
- [ ] 所有测试用例包含前置条件、步骤、预期结果
- [ ] 预期结果使用 ✅ 符号，清晰可验证
- [ ] 测试步骤具体且可操作
- [ ] 测试数据示例清晰（如适用）
- [ ] 所有测试用例都链接到 Design Document（[Tests-for: DESIGN-XXX]）
- [ ] 覆盖正常流程、错误处理、边缘情况
- [ ] 包含安全测试和性能测试
- [ ] 无占位符或 TODOs
- [ ] **始终使用 "Test Plan" 术语，绝不使用 "TD" 或 "TP"**

## Common Pitfalls

- ❌ 使用 "TD" 或 "TP" 而不是 "Test Plan"
- ❌ 忘记使用模块特定 ID 前缀（TEST-USER-CASE-XXX, TEST-ORDER-CASE-XXX）
- ❌ 忘记添加 `[Module: XXX]` 标记
- ❌ 测试步骤过于抽象，不可操作
- ❌ 预期结果模糊，不可验证
- ❌ 只测试正常流程，忽略错误处理
- ❌ 缺少性能测试或安全测试
- ❌ 前置条件不清晰
- ❌ 缺少测试数据说明

## Next Steps

✅ Test-Plan-[Module].md 完成后：
1. 审查模块测试文档（使用 `test-plan-reviewer.md`）
2. 验证与 Test-Overview.md（Overview）和 Design-Document-[Module].md 的一致性
3. 为其他模块生成 Test-Plan-[Module].md
4. 所有模块 Test Plan 完成后开始实现测试用例

---

**Tips**:
- 模块 ID 前缀必须与模块名称一致（User → TEST-USER-CASE-XXX）
- 测试用例必须具体、可操作、可验证
- 覆盖正常流程、错误处理、边缘情况、安全、性能
- 测试数据必须清晰，帮助测试执行
- **始终使用 "Test Plan" 术语，绝不使用 "TD" 或 "TP"！**
