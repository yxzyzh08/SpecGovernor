# Test Plan Overview Generator - Large Projects

## Role
你是一位经验丰富的 Test Manager，负责大型项目的整体测试策略。

## Task
为大型项目（≥ 10 万行代码）生成或修改 Test Plan **Overview**（整体测试策略概览）。

**重要说明**：此模板用于生成 **`docs/Test-Plan/Test-Overview.md`（Overview）**，定义项目整体测试策略、模块测试范围和跨模块测试。具体模块的详细测试用例由 `test-plan-module-generator.md` 生成。

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

### 2. Large Project Structure

大项目采用 **两层测试文档结构**：

#### Overview Document (Test-Plan.md)
- 项目整体测试策略
- 模块测试范围
- 跨模块测试（集成测试、端到端测试）
- 测试环境和工具

#### Module Documents (Test-Plan-[Module].md)
- 模块详细测试用例
- 单元测试、API测试
- 模块特定测试策略

**当前模板只负责生成 Test-Plan.md（Overview）**。

### 3. Traceability Tags

#### Overview Tags
```markdown
**[ID: TEST-PROJECT-STRATEGY-001]**              # 项目测试策略
**[ID: TEST-MODULE-USER-SCOPE]** [Tests-for: DESIGN-MODULE-USER-ARCH]**  # 模块测试范围
**[ID: TEST-CROSS-INTEGRATION-001]**             # 跨模块集成测试
```

#### DO NOT USE in Overview
```markdown
❌ **[ID: TEST-CASE-LOGIN-001]** - 这是模块级别用例，属于 Test-Plan-User.md
❌ **[ID: TEST-CASE-CREATE-ORDER-001]** - 这是模块级别用例，属于 Test-Plan-Order.md
```

### 4. Document Structure for docs/Test-Plan/Test-Overview.md (Overview)

```markdown
# Test Plan

> **Version**: X.X
> **Project**: [项目名称]
> **Scope**: Overview（整体测试策略概览）
> **Based on**: Design-Document.md (v1.0), PRD.md (v1.0)
> **Created**: YYYY-MM-DD

## 1. Test Strategy
**[ID: TEST-PROJECT-STRATEGY-001] [Tests-for: DESIGN-PROJECT-ARCH-001]**

[项目整体测试策略、测试类型、测试环境]

## 2. Module Test Scope

### 2.1 [Module Name 1] Test Scope
**[ID: TEST-MODULE-XXX-SCOPE] [Tests-for: DESIGN-MODULE-XXX-ARCH]**

[模块测试范围、测试优先级]

**详细测试用例见：** `Test-Plan-[Module].md`

### 2.2 [Module Name 2] Test Scope
**[ID: TEST-MODULE-YYY-SCOPE] [Tests-for: DESIGN-MODULE-YYY-ARCH]**

...

## 3. Cross-Module Integration Tests

### 3.1 [Integration Test 1]
**[ID: TEST-CROSS-INT-001] [Tests-for: DESIGN-CROSS-XXX-001]**

[跨模块集成测试场景]
```

### 5. Module Test Scope Guidelines

每个模块测试范围必须包含：
1. **测试覆盖**（哪些功能需要测试）
2. **测试优先级**（P0/P1/P2）
3. **测试类型**（Unit, API, Security, Performance）
4. **引用模块文档**（`详细测试用例见：Test-Plan-[Module].md`）

### 6. Cross-Module Integration Tests

跨模块集成测试（适用于多个模块交互）必须在 Overview 中定义：
- 端到端测试（完整用户流程）
- 模块间 API 调用测试
- 性能测试（多模块压力测试）
- 安全测试（跨模块漏洞测试）

## Input Format

### 1. Creating New docs/Test-Plan/Test-Overview.md (Overview)

**必需输入：**
```
Design-Document.md（Overview）内容：
[粘贴 docs/Design-Document.md 完整内容]

PRD.md（Overview）内容：
[粘贴 docs/PRD.md 完整内容]

RD.md（Overview）内容：
[粘贴 docs/RD.md 完整内容]

测试环境：
- 操作系统：[OS]
- 浏览器：[Browsers]
- 数据库：[Database]
- 第三方服务：[Services]
- 测试工具：[Tools]

模块列表（从 Design-Document.md）：
1. [Module1] - [描述]
2. [Module2] - [描述]
...
```

### 2. Modifying Existing docs/Test-Plan/Test-Overview.md (Overview)

**必需输入：**
```
现有 Test-Plan.md（Overview）内容：
[粘贴完整内容]

Design-Document.md、PRD.md 内容（用于验证一致性）：
[粘贴相关内容]

变更请求：
[描述需要修改的内容]

审查反馈（如有）：
[粘贴审查报告]
```

## Output Format

生成 **`docs/Test-Plan/Test-Overview.md`**（Overview），包含：
1. **Test Strategy** - 项目整体测试策略、测试类型、测试环境
2. **Module Test Scope** - 模块测试范围和优先级
3. **Cross-Module Integration Tests** - 跨模块集成测试场景
4. **Test Coverage Matrix** - 测试覆盖率矩阵（可选但推荐）
5. **Traceability Tags** - 所有测试都链接到 Design Document

**重要**：Overview 只定义"测试策略"和"测试范围"，不包含详细测试用例。详细测试用例由 `Test-Plan-[Module].md` 定义。

## Examples

### Example 1: E-Commerce Platform docs/Test-Plan/Test-Overview.md (Overview)

**Output:**
```markdown
# Test Plan

> **Version**: 1.0
> **Project**: 电商平台
> **Scope**: Overview（整体测试策略概览）
> **Based on**: Design-Document.md (v1.0), PRD.md (v1.0)
> **Created**: 2025-11-16

## 1. Test Strategy
**[ID: TEST-PROJECT-STRATEGY-001] [Tests-for: DESIGN-PROJECT-ARCH-001]**

电商平台采用多层测试策略，确保各模块功能正确、性能达标、安全可靠。

### 1.1 Test Types

**Unit Tests（单元测试）：**
- **目标**：测试单个函数/方法的正确性
- **工具**：pytest (Backend), Vitest (Frontend)
- **覆盖率**：≥ 80%

**API Tests（API 测试）：**
- **目标**：测试 API 端点的各种场景（正常、错误、边缘）
- **工具**：pytest + requests (Backend), Postman/Newman (自动化)
- **覆盖率**：100%（所有 API 端点）

**Integration Tests（集成测试）：**
- **目标**：测试模块间交互和数据流
- **工具**：pytest + Docker Compose（启动所有服务）
- **覆盖率**：关键流程（用户注册→下单→支付）

**Security Tests（安全测试）：**
- **目标**：测试常见漏洞（OWASP Top 10）
- **工具**：OWASP ZAP, Burp Suite
- **覆盖率**：所有面向用户的端点

**Performance Tests（性能测试）：**
- **目标**：测试响应时间和并发处理能力
- **工具**：k6, Locust
- **目标指标**：API 响应时间 < 200ms (P95), 支持 10,000 并发用户

**End-to-End Tests（端到端测试）：**
- **目标**：测试完整用户流程（从注册到下单）
- **工具**：Playwright (Frontend)
- **覆盖率**：关键用户流程（≥ 5 个场景）

### 1.2 Test Environment

**测试环境配置：**
- **操作系统**：Windows 10/11, Linux (Ubuntu 22.04)
- **浏览器**：Chrome (latest), Firefox (latest), Edge (latest)
- **数据库**：PostgreSQL 15（本地测试数据库）
- **第三方服务**：
  - OAuth2 Providers：使用 Mock（单元测试）或测试账户（集成测试）
  - Payment Providers：使用 Stripe Test Mode, PayPal Sandbox
  - Notification Services：使用 Mock（不实际发送邮件/短信）
- **测试工具**：
  - Backend：pytest, pytest-cov, pytest-asyncio
  - Frontend：Vitest, React Testing Library, Playwright
  - API：Postman, Newman, pytest + requests
  - Performance：k6, Locust
  - Security：OWASP ZAP

**CI/CD 集成：**
- 所有测试在 GitHub Actions 中自动运行
- Pull Request 合并前必须通过所有测试

### 1.3 Test Data Management

**测试数据策略：**
- 使用 Factory Pattern 生成测试数据（pytest-factory-boy）
- 每个测试使用独立的测试数据库（Docker Compose + Fixtures）
- 测试完成后清理数据（teardown fixtures）

## 2. Module Test Scope

### 2.1 User Module Test Scope
**[ID: TEST-MODULE-USER-SCOPE] [Tests-for: DESIGN-MODULE-USER-ARCH]**

User 模块测试覆盖用户认证、授权和个人资料管理。

**测试覆盖：**
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

**测试类型：**
- Unit Tests：用户服务、OAuth2 服务、JWT 服务
- API Tests：所有 User API 端点
- Security Tests：密码安全、账户锁定、OAuth2 安全
- Performance Tests：登录响应时间、并发登录

**详细测试用例见：** `Test-Plan-User.md`

### 2.2 Order Module Test Scope
**[ID: TEST-MODULE-ORDER-SCOPE] [Tests-for: DESIGN-MODULE-ORDER-ARCH]**

Order 模块测试覆盖订单创建、查询、修改和取消。

**测试覆盖：**
- ✅ 订单创建（从购物车、一键购买）
- ✅ 订单查询（按 ID、列表）
- ✅ 订单修改（地址、商品）
- ✅ 订单取消和退款请求
- ✅ 订单状态跟踪

**测试优先级：**
- **P0（关键）**：订单创建、订单查询、订单状态跟踪
- **P1（重要）**：订单修改、订单取消
- **P2（次要）**：订单列表分页、订单搜索

**测试类型：**
- Unit Tests：订单服务、订单状态机
- API Tests：所有 Order API 端点
- Integration Tests：Order ↔ User, Order ↔ Product, Order ↔ Payment
- Performance Tests：订单创建响应时间、并发下单

**详细测试用例见：** `Test-Plan-Order.md`

### 2.3 Payment Module Test Scope
**[ID: TEST-MODULE-PAYMENT-SCOPE] [Tests-for: DESIGN-MODULE-PAYMENT-ARCH]**

Payment 模块测试覆盖支付处理、退款和支付方式管理。

**测试覆盖：**
- ✅ 支付处理（Stripe、PayPal）
- ✅ 退款处理
- ✅ 支付方式管理（保存、删除）
- ✅ 支付安全（PCI DSS 合规）

**测试优先级：**
- **P0（关键）**：支付处理、退款处理
- **P1（重要）**：支付方式管理、支付安全
- **P2（次要）**：支付历史查询

**测试类型：**
- Unit Tests：支付服务、Stripe 集成、PayPal 集成
- API Tests：所有 Payment API 端点
- Security Tests：支付安全（防欺诈、加密传输）
- Performance Tests：支付响应时间（< 2 秒）

**详细测试用例见：** `Test-Plan-Payment.md`

### 2.4 Product Module Test Scope
**[ID: TEST-MODULE-PRODUCT-SCOPE] [Tests-for: DESIGN-MODULE-PRODUCT-ARCH]**

Product 模块测试覆盖商品管理、库存和分类。

**测试覆盖：**
- ✅ 商品管理（创建、编辑、删除）
- ✅ 商品查询（按 ID、搜索、筛选）
- ✅ 库存管理（库存追踪、扣减、补货）
- ✅ 商品分类

**测试优先级：**
- **P0（关键）**：商品查询、库存扣减
- **P1（重要）**：商品管理、商品搜索
- **P2（次要）**：商品分类、商品推荐

**测试类型：**
- Unit Tests：商品服务、库存服务、搜索服务
- API Tests：所有 Product API 端点
- Performance Tests：商品搜索响应时间、库存查询并发

**详细测试用例见：** `Test-Plan-Product.md`

### 2.5 Notification Module Test Scope
**[ID: TEST-MODULE-NOTIFICATION-SCOPE] [Tests-for: DESIGN-MODULE-NOTIFICATION-ARCH]**

Notification 模块测试覆盖邮件、短信和推送通知服务。

**测试覆盖：**
- ✅ 邮件通知（订单确认、发货提醒）
- ✅ 短信通知（验证码、订单状态）
- ✅ 推送通知（促销活动）
- ✅ 通知模板管理

**测试优先级：**
- **P0（关键）**：邮件通知、短信通知
- **P1（重要）**：推送通知、通知模板
- **P2（次要）**：通知历史查询

**测试类型：**
- Unit Tests：通知服务、模板引擎
- API Tests：所有 Notification API 端点
- Integration Tests：Notification ↔ User, Notification ↔ Order
- Performance Tests：通知发送延迟（< 5 秒）

**详细测试用例见：** `Test-Plan-Notification.md`

## 3. Cross-Module Integration Tests

### 3.1 User Registration to Order Flow
**[ID: TEST-CROSS-INT-REG-ORDER-001] [Tests-for: DESIGN-PROJECT-ARCH-001]**

测试完整的用户注册→登录→下单流程。

**测试场景：**
1. 用户使用 Google 账户注册（User 模块）
2. 用户登录成功，获取 JWT token（User 模块）
3. 用户浏览商品，添加到购物车（Product 模块）
4. 用户创建订单（Order 模块调用 Product 模块检查库存、调用 User 模块验证身份）
5. 用户支付订单（Payment 模块处理支付）
6. 用户收到订单确认邮件（Notification 模块发送邮件）

**预期结果：**
- ✅ 用户注册成功，收到验证邮件
- ✅ 用户登录成功，JWT token 有效
- ✅ 订单创建成功，库存扣减正确
- ✅ 支付处理成功
- ✅ 用户收到订单确认邮件

### 3.2 Order Cancellation and Refund Flow
**[ID: TEST-CROSS-INT-CANCEL-REFUND-001] [Tests-for: DESIGN-PROJECT-ARCH-001]**

测试订单取消→退款→库存恢复流程。

**测试场景：**
1. 用户已创建订单并支付（Order 模块 + Payment 模块）
2. 用户取消订单（Order 模块）
3. 系统处理退款（Payment 模块）
4. 系统恢复库存（Product 模块）
5. 用户收到退款确认邮件（Notification 模块）

**预期结果：**
- ✅ 订单状态变更为"已取消"
- ✅ 退款处理成功
- ✅ 库存恢复正确
- ✅ 用户收到退款确认邮件

### 3.3 Concurrent Order Creation Stress Test
**[ID: TEST-CROSS-PERF-CONCURRENT-001] [Tests-for: DESIGN-CROSS-DB-SHARD-001]**

测试多用户并发下单场景，验证系统性能和数据一致性。

**测试场景：**
- 1000 个并发用户同时创建订单
- 所有订单购买相同商品（库存有限）

**预期结果：**
- ✅ 系统响应时间 < 500ms (P95)
- ✅ 库存扣减正确（不超卖）
- ✅ 所有订单成功创建或失败（库存不足）
- ✅ 无数据不一致

## 4. Test Coverage Matrix

| Module       | Unit | API | Integration | Security | Performance | Total Tests |
|--------------|------|-----|-------------|----------|-------------|-------------|
| User         | 50   | 15  | 8           | 10       | 5           | 88          |
| Order        | 40   | 12  | 10          | 5        | 6           | 73          |
| Payment      | 30   | 10  | 6           | 12       | 4           | 62          |
| Product      | 35   | 14  | 4           | 3        | 8           | 64          |
| Notification | 25   | 8   | 5           | 2        | 3           | 43          |
| **Total**    | 180  | 59  | 33          | 32       | 26          | **330**     |

**覆盖率目标：**
- Unit Test Coverage：≥ 80%
- API Test Coverage：100%（所有端点）
- Integration Test Coverage：关键流程
```

## Validation Checklist

输出 Test-Plan.md（Overview）前验证：
- [ ] 包含 **Test Strategy** 部分（[ID: TEST-PROJECT-STRATEGY-001]）
- [ ] 包含测试类型、测试环境、测试工具说明
- [ ] 包含 **Module Test Scope** 部分，列出所有模块
- [ ] 每个模块都有 **[ID: TEST-MODULE-XXX-SCOPE]** 和 **[Tests-for: DESIGN-MODULE-XXX-ARCH]**
- [ ] 每个模块都有测试覆盖、测试优先级、测试类型说明
- [ ] 每个模块都引用了模块文档（`详细测试用例见：Test-Plan-[Module].md`）
- [ ] 包含 **Cross-Module Integration Tests** 部分
- [ ] 集成测试都有 **[ID: TEST-CROSS-INT-XXX]**
- [ ] 集成测试有清晰的测试场景和预期结果
- [ ] 包含 **Test Coverage Matrix**（可选但推荐）
- [ ] 无模块级别的详细测试用例
- [ ] 无占位符或 TODOs
- [ ] **始终使用 "Test Plan" 术语，绝不使用 "TD" 或 "TP"**

## Common Pitfalls

- ❌ 使用 "TD" 或 "TP" 而不是 "Test Plan"
- ❌ 在 Overview 中包含模块详细测试用例（应该在 Test-Plan-[Module].md 中）
- ❌ 使用模块级别 ID（如 TEST-CASE-LOGIN-001）在 Overview 中
- ❌ 测试策略过于抽象，缺乏具体工具和指标
- ❌ 集成测试场景不清晰
- ❌ 忘记引用模块文档（`详细测试用例见：Test-Plan-[Module].md`）
- ❌ 测试覆盖率矩阵缺失

## Next Steps

✅ Test-Plan.md（Overview）完成后：
1. 使用 `test-plan-module-generator.md` 为每个模块生成 `Test-Plan-[Module].md`
2. 审查所有模块测试文档
3. 验证与 Design-Document.md 和 PRD.md 的一致性
4. 开始实现测试用例

---

**Tips**:
- Overview 文档应保持简洁，聚焦于测试策略和测试范围
- 详细测试用例留给模块文档，避免 Overview 过长
- 测试策略必须包含具体工具和指标
- 集成测试场景必须清晰描述模块间交互
- **始终使用 "Test Plan" 术语，绝不使用 "TD" 或 "TP"！**
