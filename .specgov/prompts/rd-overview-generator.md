# Requirements Document (RD) Overview Generator - Large Projects

## Role
你是一位经验丰富的 Requirements Analyst，负责大型项目的整体需求规划。

## Task
为大型项目（≥ 10 万行代码）生成或修改 Requirements Document (RD) **Overview**（整体需求概览）。

**重要说明**：此模板用于生成 **`docs/RD/RD-Overview.md`（Overview）**，定义项目整体需求、模块划分和跨模块需求。具体模块的详细需求由 `rd-module-generator.md` 生成。

## Critical Requirements

### 1. Large Project Structure

大项目采用 **两层需求文档结构**：

#### Overview Document (docs/RD/RD-Overview.md)
- 项目整体概述
- 模块划分和边界定义
- 跨模块需求（Cross-Cutting Requirements）
- 每个模块的高层级范围说明

#### Module Documents (docs/RD/RD-[Module].md)
- 模块具体需求
- 详细验收标准
- 模块内部分解
- 模块间依赖声明

**当前模板只负责生成 docs/RD/RD-Overview.md（Overview）**。

### 2. Traceability Tags

#### Overview Tags
```markdown
**[ID: RD-PROJECT-001]**                        # 项目级别
**[ID: RD-MODULE-USER] [Decomposes: RD-PROJECT-001]**  # 模块定义
**[ID: RD-CROSS-AUTH-001]**                     # 跨模块需求
```

#### DO NOT USE in Overview
```markdown
❌ **[ID: RD-USER-REG-001]** - 这是模块级别 ID，属于 docs/RD/RD-User.md
❌ **[ID: RD-ORDER-CREATE-001]** - 这是模块级别 ID，属于 docs/RD/RD-Order.md
```

### 3. Document Structure for docs/RD/RD-Overview.md (Overview)

```markdown
# Requirements Document (RD)

> **Version**: X.X
> **Project**: [项目名称]
> **Scope**: Overview（整体需求概览）
> **Created**: YYYY-MM-DD

## 1. Project Overview
**[ID: RD-PROJECT-001]**

[项目整体描述、目标用户、核心价值]

## 2. Module Requirements

### 2.1 [Module Name 1]
**[ID: RD-MODULE-XXX] [Decomposes: RD-PROJECT-001]**

[模块高层级范围说明]

**模块范围：**
- [功能点 1]
- [功能点 2]

**详细需求见：** `RD-[Module].md`

### 2.2 [Module Name 2]
**[ID: RD-MODULE-YYY] [Decomposes: RD-PROJECT-001]**

...

## 3. Cross-Cutting Requirements

### 3.1 [Cross-Cutting Requirement 1]
**[ID: RD-CROSS-XXX-001]**

[跨所有模块的需求，如认证、日志、国际化等]

**验收标准：**
- ✅ [验收标准 1]
- ✅ [验收标准 2]
```

### 4. Module Definition Guidelines

每个模块定义必须包含：
1. **模块名称**（使用 PascalCase：User, Order, Payment）
2. **模块范围**（明确包含和不包含的功能）
3. **模块边界**（与其他模块的交互点）
4. **引用模块文档**（`详细需求见：RD-[Module].md`）

### 5. Cross-Cutting Requirements

跨模块需求（适用于所有或多个模块）必须在 Overview 中定义：
- 认证和授权（Authentication & Authorization）
- 审计日志（Audit Logging）
- 国际化（Internationalization）
- 性能要求（Performance Requirements）
- 安全要求（Security Requirements）

## Input Format

### 1. Creating New RD.md (Overview)

**必需输入：**
```
项目上下文：
- 项目名称：[名称]
- 项目规模：大项目（> 10 万行代码）
- 目标用户：[描述]

模块列表：
1. [Module1] - [高层级描述]
2. [Module2] - [高层级描述]
...

跨模块需求：
- [列出所有模块共同的需求]

技术约束：
- [操作系统、技术栈等]
```

### 2. Modifying Existing RD.md (Overview)

**必需输入：**
```
现有 RD.md（Overview）内容：
[粘贴完整内容]

变更请求：
[描述需要修改的内容]

审查反馈（如有）：
[粘贴审查报告]
```

## Output Format

生成 **`docs/RD/RD-Overview.md`**（Overview），包含：
1. **Project Overview** - 项目整体描述
2. **Module Requirements** - 模块划分和高层级范围
3. **Cross-Cutting Requirements** - 跨模块需求
4. **Traceability Tags** - 所有模块和跨模块需求都有 ID

**重要**：Overview 只定义"是什么模块"和"模块边界"，不包含详细需求实现。详细需求由 `docs/RD/RD-[Module].md` 定义。

## Examples

### Example 1: E-Commerce Platform docs/RD/RD-Overview.md

**Input:**
```
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

**Output:**
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

**模块边界：**
- **包含**：用户认证、授权、个人资料
- **不包含**：订单管理（属于 Order 模块）、支付管理（属于 Payment 模块）

**详细需求见：** `RD-User.md`

### 2.2 Order Module
**[ID: RD-MODULE-ORDER] [Decomposes: RD-PROJECT-001]**

订单模块负责订单创建、查询、修改、取消和履行流程。

**模块范围：**
- 订单创建（购物车结算）
- 订单查询和列表
- 订单修改（地址、商品）
- 订单取消和退款请求
- 订单状态跟踪

**模块边界：**
- **包含**：订单生命周期管理
- **不包含**：支付处理（调用 Payment 模块）、商品库存（查询 Product 模块）

**详细需求见：** `RD-Order.md`

### 2.3 Payment Module
**[ID: RD-MODULE-PAYMENT] [Decomposes: RD-PROJECT-001]**

支付模块负责支付处理、退款和支付方式管理。

**模块范围：**
- 支付处理（信用卡、PayPal、Stripe）
- 退款处理
- 支付方式管理
- 支付安全（PCI DSS 合规）

**模块边界：**
- **包含**：支付交易处理、支付方式管理
- **不包含**：订单创建（属于 Order 模块）

**详细需求见：** `RD-Payment.md`

### 2.4 Product Module
**[ID: RD-MODULE-PRODUCT] [Decomposes: RD-PROJECT-001]**

商品模块负责商品管理、库存和分类。

**模块范围：**
- 商品创建和编辑
- 商品分类和标签
- 库存管理（库存追踪、补货提醒）
- 商品搜索和筛选

**模块边界：**
- **包含**：商品信息管理、库存管理
- **不包含**：订单处理（属于 Order 模块）

**详细需求见：** `RD-Product.md`

### 2.5 Notification Module
**[ID: RD-MODULE-NOTIFICATION] [Decomposes: RD-PROJECT-001]**

通知模块负责邮件、短信和推送通知服务。

**模块范围：**
- 邮件通知（订单确认、发货提醒）
- 短信通知（验证码、订单状态）
- 推送通知（促销活动、价格变动）
- 通知模板管理

**模块边界：**
- **包含**：通知发送、模板管理
- **不包含**：通知触发逻辑（由各模块调用）

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
- Token 刷新机制

**验收标准：**
- ✅ 所有 API 端点验证 JWT token
- ✅ 未授权请求返回 401 Unauthorized
- ✅ 权限不足请求返回 403 Forbidden
- ✅ Token 过期前 5 分钟可刷新

### 3.2 Audit Logging
**[ID: RD-CROSS-AUDIT-001]**

所有模块必须记录审计日志，用于安全监控和故障排查。

**要求：**
- 记录所有 API 请求（用户 ID、IP、时间戳、操作）
- 记录所有数据修改（创建、更新、删除）
- 日志保留 90 天
- 日志集中存储（如 ELK Stack）

**验收标准：**
- ✅ 所有 API 请求被记录到日志系统
- ✅ 日志包含用户 ID、IP、时间戳、操作类型
- ✅ 敏感数据（密码、支付信息）不被记录
- ✅ 日志可通过 Kibana 查询和可视化

### 3.3 Internationalization (i18n)
**[ID: RD-CROSS-I18N-001]**

所有模块必须支持国际化，允许用户选择语言。

**要求：**
- 支持英文（默认）、中文、西班牙文
- 所有用户界面文本可翻译
- 日期、时间、货币格式本地化
- 使用 i18n 库（如 i18next、react-intl）

**验收标准：**
- ✅ 用户可以选择界面语言
- ✅ 所有界面文本根据选择的语言显示
- ✅ 日期、时间、货币格式正确本地化
- ✅ 新增文本时自动添加到翻译文件

### 3.4 Performance Requirements
**[ID: RD-CROSS-PERF-001]**

所有模块必须满足性能要求，确保良好的用户体验。

**要求：**
- API 响应时间 < 200ms（P95）
- 支持 10,000 并发用户
- 数据库查询优化（使用索引、缓存）
- 静态资源 CDN 加速

**验收标准：**
- ✅ P95 API 响应时间 < 200ms
- ✅ 系统支持 10,000 并发用户无降级
- ✅ 数据库查询时间 < 50ms（P95）
- ✅ 静态资源通过 CDN 分发

### 3.5 Security Requirements
**[ID: RD-CROSS-SEC-001]**

所有模块必须遵守安全最佳实践，防止常见漏洞。

**要求：**
- 防止 OWASP Top 10 漏洞（SQL 注入、XSS、CSRF 等）
- HTTPS 加密传输
- 敏感数据加密存储
- 定期安全审计和漏洞扫描

**验收标准：**
- ✅ 所有 API 使用 HTTPS
- ✅ 密码使用 bcrypt 哈希（至少 10 轮）
- ✅ SQL 查询使用参数化查询
- ✅ XSS 防护（输出转义）
- ✅ CSRF 防护（CSRF token）
```

## Validation Checklist

输出 RD.md（Overview）前验证：
- [ ] 包含 **Project Overview** 部分（[ID: RD-PROJECT-001]）
- [ ] 包含 **Module Requirements** 部分，列出所有模块
- [ ] 每个模块都有 **[ID: RD-MODULE-XXX]** 和 **[Decomposes: RD-PROJECT-001]**
- [ ] 每个模块都有 **模块范围** 和 **模块边界** 说明
- [ ] 每个模块都引用了模块文档（`详细需求见：RD-[Module].md`）
- [ ] 包含 **Cross-Cutting Requirements** 部分
- [ ] 跨模块需求都有 **[ID: RD-CROSS-XXX-001]**
- [ ] 跨模块需求有清晰的验收标准
- [ ] 无模块级别的详细需求（如 RD-USER-REG-001）
- [ ] 无占位符或 TODOs

## Common Pitfalls

- ❌ 在 Overview 中包含模块详细需求（应该在 RD-[Module].md 中）
- ❌ 使用模块级别 ID（如 RD-USER-REG-001）在 Overview 中
- ❌ 模块边界不清晰，导致职责重叠
- ❌ 跨模块需求定义不明确
- ❌ 忘记引用模块文档（`详细需求见：RD-[Module].md`）
- ❌ 模块范围过于详细，失去 Overview 的简洁性

## Next Steps

✅ RD.md（Overview）完成后：
1. 使用 `rd-module-generator.md` 为每个模块生成 `RD-[Module].md`
2. 审查所有模块需求文档
3. 验证模块边界和跨模块依赖
4. 进入 PRD 阶段

---

**Tips**:
- Overview 文档应保持简洁，聚焦于模块划分和跨模块需求
- 详细需求留给模块文档，避免 Overview 过长
- 模块边界必须清晰定义，防止职责重叠
- 跨模块需求必须在 Overview 中定义，所有模块遵守
