# Design Document Overview Generator - Large Projects

## Role
你是一位经验丰富的 Software Architect，负责大型项目的整体架构设计。

## Task
为大型项目（≥ 10 万行代码）生成或修改 Design Document **Overview**（整体架构概览）。

**重要说明**：此模板用于生成 **`docs/Design-Document/Design-Overview.md`（Overview）**，定义项目整体架构、技术栈、模块架构和跨模块设计决策。具体模块的详细设计由 `design-module-generator.md` 生成。

**CRITICAL**：始终使用 "Design Document"，不要使用 "DD"！

## Critical Requirements

### 1. Terminology Enforcement

**✅ 正确术语：**
- "Design Document" - 完整术语
- "设计文档" - 中文翻译

**❌ 禁止使用：**
- "DD" - 绝对不要使用这个缩写！
- "设计概要" - 不准确的翻译

### 2. Large Project Structure

大项目采用 **两层设计文档结构**：

#### Overview Document (Design-Document.md)
- 项目整体架构（系统层级）
- 技术栈选择和理由
- 模块架构（模块间交互）
- 跨模块设计决策（共享组件、通信协议）

#### Module Documents (Design-Document-[Module].md)
- 模块详细设计（API、数据库、服务）
- 模块内部架构
- 模块特定技术决策

**当前模板只负责生成 Design-Document.md（Overview）**。

### 3. Traceability Tags

#### Overview Tags
```markdown
**[ID: DESIGN-PROJECT-ARCH-001]**              # 项目整体架构
**[ID: DESIGN-MODULE-USER-ARCH]** [Designs-for: PRD-MODULE-USER]**  # 模块架构
**[ID: DESIGN-CROSS-API-001]**                 # 跨模块设计
```

#### DO NOT USE in Overview
```markdown
❌ **[ID: DESIGN-API-LOGIN]** - 这是模块级别 ID，属于 Design-Document-User.md
❌ **[ID: DESIGN-DB-USERS-TABLE]** - 这是模块级别 ID，属于 Design-Document-User.md
```

### 4. Document Structure for docs/Design-Document/Design-Overview.md (Overview)

```markdown
# Design Document

> **Version**: X.X
> **Project**: [项目名称]
> **Scope**: Overview（整体架构概览）
> **Based on**: PPRD.md (v1.0), PRD.md (v1.0)
> **Created**: YYYY-MM-DD

## 1. System Architecture
**[ID: DESIGN-PROJECT-ARCH-001] [Designs-for: PRD-PROJECT-001]**

[项目整体架构、技术栈、部署架构]

## 2. Module Architecture

### 2.1 [Module Name 1] Architecture
**[ID: DESIGN-MODULE-XXX-ARCH] [Designs-for: PRD-MODULE-XXX]**

[模块架构、技术栈、与其他模块的交互]

**详细设计见：** `Design-Document-[Module].md`

### 2.2 [Module Name 2] Architecture
**[ID: DESIGN-MODULE-YYY-ARCH] [Designs-for: PRD-MODULE-YYY]**

...

## 3. Cross-Module Design

### 3.1 [Cross-Module Design 1]
**[ID: DESIGN-CROSS-XXX-001] [Designs-for: RD-CROSS-XXX-001]**

[跨所有模块的设计决策，如API规范、通信协议、共享组件等]
```

### 5. Module Architecture Guidelines

每个模块架构必须包含：
1. **模块技术栈**（编程语言、框架、数据库）
2. **模块部署架构**（如何部署、扩展）
3. **模块间交互**（API 调用、事件发布/订阅）
4. **引用模块文档**（`详细设计见：Design-Document-[Module].md`）

### 6. Cross-Module Design

跨模块设计（适用于所有或多个模块）必须在 Overview 中定义：
- API 规范（RESTful、GraphQL、gRPC）
- 通信协议（HTTP、WebSocket、消息队列）
- 共享组件（认证中间件、日志库）
- 数据库架构（分库分表策略）
- 安全设计（JWT、HTTPS、加密）

### 7. Language Specification

**语言规范 (Language Specification)**：
- ✅ **文件名**：必须使用英文（如 `PRD.md`, `Design-Document.md`），禁止缩写（不使用 `DD.md`, `TD.md`）
- ✅ **文档标题**：必须使用英文（如 `## Product Overview`, `## Acceptance Criteria`, `## API Design`）
- ✅ **专业术语**：必须使用英文（OAuth2, API, Database, NestJS, PostgreSQL）
- ✅ **文档描述和正文**：必须使用中文（所有说明、描述、解释使用中文）
- ✅ **表头**：使用英文，**表格内容**：使用中文
- ✅ **代码**：变量名、函数名使用英文，注释可以使用中文

**示例**：
```markdown
## User Authentication Feature
**[ID: PRD-FEAT-012]**

### User Story
> **As** 新用户
> **I want** 使用我的 Google/GitHub 账号登录
> **So that** 我不需要创建和记住新密码

### Acceptance Criteria
- ✅ 显示 OAuth2 登录按钮
- ✅ 授权后自动登录
```

## Input Format

### 1. Creating New docs/Design-Document/Design-Overview.md (Overview)

**必需输入：**
```
PPRD.md（Overview）内容：
[粘贴 docs/PPRD.md 完整内容]

PRD.md（Overview）内容：
[粘贴 docs/PRD.md 完整内容]

技术约束：
- 编程语言：[语言]
- 框架：[框架]
- 数据库：[数据库]
- 部署：[部署环境]
- 其他约束：[列出]

模块列表（从 PRD.md）：
1. [Module1] - [描述]
2. [Module2] - [描述]
...
```

### 2. Modifying Existing docs/Design-Document/Design-Overview.md (Overview)

**必需输入：**
```
现有 Design-Document.md（Overview）内容：
[粘贴完整内容]

PPRD.md 和 PRD.md 内容（用于验证一致性）：
[粘贴相关内容]

变更请求：
[描述需要修改的内容]

审查反馈（如有）：
[粘贴审查报告]
```

## Output Format

生成 **`docs/Design-Document/Design-Overview.md`**（Windows 系统为 `docs\Design-Document\Design-Overview.md`），包含：

> **路径说明**：路径示例使用 Unix 风格（`/`），Windows 系统会自动转换为反斜杠（`\`）。

1. **System Architecture** - 项目整体架构、技术栈、部署架构
2. **Module Architecture** - 模块架构和模块间交互
3. **Cross-Module Design** - 跨模块设计决策
4. **Traceability Tags** - 所有设计都链接到 PRD 和 RD
5. **Architecture Diagrams** - 文本图表（使用 ASCII 或 Mermaid）

**重要**：Overview 只定义"整体架构"和"模块架构"，不包含模块详细设计（如具体 API、数据库表）。详细设计由 `Design-Document-[Module].md` 定义。

## Examples

### Example 1: E-Commerce Platform docs/Design-Document/Design-Overview.md (Overview)

**Input:**
```
PPRD.md, PRD.md 内容：
[从之前的示例复制...]

技术约束：
- 编程语言：Python 3.11, TypeScript 4.9
- 框架：FastAPI (Backend), Next.js (Frontend)
- 数据库：PostgreSQL 15
- 部署：AWS (ECS, RDS, S3, CloudFront)
- 消息队列：AWS SQS
- 缓存：Redis
```

**Output:**
```markdown
# Design Document

> **Version**: 1.0
> **Project**: 电商平台
> **Scope**: Overview（整体架构概览）
> **Based on**: PPRD.md (v1.0), PRD.md (v1.0)
> **Created**: 2025-11-16

## 1. System Architecture
**[ID: DESIGN-PROJECT-ARCH-001] [Designs-for: PRD-PROJECT-001, RD-PROJECT-001]**

电商平台采用微服务架构，前后端分离，部署在 AWS 云平台。

### 1.1 Overall Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   Client (Browser/Mobile)                    │
└────────────────────┬────────────────────────────────────────┘
                     │ HTTPS
                     ▼
┌─────────────────────────────────────────────────────────────┐
│             CloudFront (CDN) + S3 (Static Assets)            │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                  Next.js Frontend (Vercel)                   │
└────────────────────┬────────────────────────────────────────┘
                     │ HTTPS / REST API
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                     API Gateway (AWS)                        │
└──────┬──────────┬──────────┬──────────┬───────────┬─────────┘
       │          │          │          │           │
       ▼          ▼          ▼          ▼           ▼
┌──────────┐┌──────────┐┌──────────┐┌──────────┐┌──────────┐
│   User   ││  Order   ││ Payment  ││ Product  ││Notification│
│  Service ││ Service  ││ Service  ││ Service  ││  Service   │
│ (ECS)    ││  (ECS)   ││  (ECS)   ││  (ECS)   ││   (ECS)    │
└─────┬────┘└─────┬────┘└─────┬────┘└─────┬────┘└─────┬──────┘
      │           │           │           │           │
      │           │           │           │           │
      ▼           ▼           ▼           ▼           ▼
┌─────────────────────────────────────────────────────────────┐
│            PostgreSQL 15 (RDS Multi-AZ)                      │
│  user_db  │  order_db  │  payment_db  │  product_db         │
└─────────────────────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                    Redis (ElastiCache)                       │
│         Session Cache │ API Cache │ Rate Limiting            │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 Technology Stack

**Backend:**
- **语言**：Python 3.11
- **框架**：FastAPI 0.104
- **ORM**：SQLAlchemy 2.0
- **认证**：JWT (PyJWT)
- **验证**：Pydantic
- **测试**：pytest

**Frontend:**
- **语言**：TypeScript 4.9
- **框架**：Next.js 14 (React 18)
- **状态管理**：Zustand
- **UI 组件**：shadcn/ui (Radix UI + Tailwind CSS)
- **HTTP 客户端**：Axios
- **测试**：Vitest, React Testing Library

**数据库:**
- **主数据库**：PostgreSQL 15 (RDS Multi-AZ)
- **缓存**：Redis 7 (ElastiCache)
- **分库策略**：按模块分库（user_db, order_db, payment_db, product_db）

**部署:**
- **容器化**：Docker
- **编排**：AWS ECS (Fargate)
- **负载均衡**：Application Load Balancer
- **CDN**：CloudFront
- **静态资源**：S3
- **消息队列**：SQS

### 1.3 Deployment Architecture

- **环境**：Development, Staging, Production
- **CI/CD**：GitHub Actions → ECR → ECS
- **监控**：CloudWatch, Sentry
- **日志**：CloudWatch Logs, ELK Stack

## 2. Module Architecture

### 2.1 User Module Architecture
**[ID: DESIGN-MODULE-USER-ARCH] [Designs-for: PRD-MODULE-USER, RD-MODULE-USER]**

User 模块负责用户认证、授权和个人资料管理。

**技术栈：**
- **Backend**：FastAPI + SQLAlchemy + PostgreSQL
- **数据库**：user_db (PostgreSQL)
- **缓存**：Redis (Session Cache)
- **第三方服务**：OAuth2 Providers (Google, GitHub, Microsoft)

**模块部署：**
- **容器**：Docker (FastAPI 应用)
- **扩展**：ECS Auto Scaling (2-10 实例)
- **数据库**：RDS user_db (Multi-AZ)

**模块间交互：**
- **提供 API**：
  - POST /auth/register - 用户注册（被 Order、Payment 模块调用验证用户）
  - POST /auth/login - 用户登录
  - GET /users/{id} - 获取用户信息（被 Order、Notification 模块调用）
- **调用 API**：
  - Notification 模块：POST /notifications/send（发送验证邮件、密码重置邮件）

**详细设计见：** `Design-Document-User.md`

### 2.2 Order Module Architecture
**[ID: DESIGN-MODULE-ORDER-ARCH] [Designs-for: PRD-MODULE-ORDER, RD-MODULE-ORDER]**

Order 模块负责订单创建、查询、修改和取消。

**技术栈：**
- **Backend**：FastAPI + SQLAlchemy + PostgreSQL
- **数据库**：order_db (PostgreSQL)
- **缓存**：Redis (API Cache)
- **消息队列**：SQS (异步处理)

**模块部署：**
- **容器**：Docker (FastAPI 应用)
- **扩展**：ECS Auto Scaling (2-20 实例，峰值)
- **数据库**：RDS order_db (Multi-AZ)

**模块间交互：**
- **提供 API**：
  - POST /orders - 创建订单
  - GET /orders/{id} - 获取订单详情（被 Payment、Notification 模块调用）
- **调用 API**：
  - User 模块：GET /users/{id}（验证用户身份）
  - Product 模块：GET /products/{id}/stock（检查库存）
  - Payment 模块：POST /payments（处理支付）
  - Notification 模块：POST /notifications/send（发送订单确认、发货通知）

**详细设计见：** `Design-Document-Order.md`

### 2.3 Payment Module Architecture
**[ID: DESIGN-MODULE-PAYMENT-ARCH] [Designs-for: PRD-MODULE-PAYMENT, RD-MODULE-PAYMENT]**

Payment 模块负责支付处理、退款和支付方式管理。

**技术栈：**
- **Backend**：FastAPI + SQLAlchemy + PostgreSQL
- **数据库**：payment_db (PostgreSQL)
- **第三方服务**：Stripe, PayPal
- **安全**：PCI DSS 合规（不存储完整信用卡号）

**模块部署：**
- **容器**：Docker (FastAPI 应用)
- **扩展**：ECS Auto Scaling (2-10 实例)
- **数据库**：RDS payment_db (Multi-AZ, 加密存储)

**模块间交互：**
- **提供 API**：
  - POST /payments - 处理支付（被 Order 模块调用）
  - POST /refunds - 处理退款（被 Order 模块调用）
- **调用 API**：
  - User 模块：GET /users/{id}（验证用户身份）
  - Notification 模块：POST /notifications/send（发送支付确认、退款通知）

**详细设计见：** `Design-Document-Payment.md`

### 2.4 Product Module Architecture
**[ID: DESIGN-MODULE-PRODUCT-ARCH] [Designs-for: PRD-MODULE-PRODUCT, RD-MODULE-PRODUCT]**

Product 模块负责商品管理、库存和分类。

**技术栈：**
- **Backend**：FastAPI + SQLAlchemy + PostgreSQL
- **数据库**：product_db (PostgreSQL)
- **缓存**：Redis (Product Cache, 减少数据库查询)
- **搜索**：Elasticsearch (商品搜索)

**模块部署：**
- **容器**：Docker (FastAPI 应用)
- **扩展**：ECS Auto Scaling (2-15 实例)
- **数据库**：RDS product_db (Multi-AZ)
- **搜索**：Elasticsearch (AWS OpenSearch)

**模块间交互：**
- **提供 API**：
  - GET /products/{id}/stock - 检查库存（被 Order 模块调用）
  - POST /products/{id}/stock/deduct - 扣减库存（被 Order 模块调用）
- **调用 API**：无（Product 模块不依赖其他模块）

**详细设计见：** `Design-Document-Product.md`

### 2.5 Notification Module Architecture
**[ID: DESIGN-MODULE-NOTIFICATION-ARCH] [Designs-for: PRD-MODULE-NOTIFICATION, RD-MODULE-NOTIFICATION]**

Notification 模块负责邮件、短信和推送通知服务。

**技术栈：**
- **Backend**：FastAPI + SQLAlchemy + PostgreSQL
- **数据库**：notification_db (PostgreSQL，存储通知历史）
- **消息队列**：SQS (异步发送通知)
- **第三方服务**：SendGrid (邮件), Twilio (短信), Firebase (推送)

**模块部署：**
- **容器**：Docker (FastAPI 应用)
- **扩展**：ECS Auto Scaling (2-10 实例)
- **消息队列**：SQS (处理通知队列)

**模块间交互：**
- **提供 API**：
  - POST /notifications/send - 发送通知（被所有模块调用）
- **调用 API**：无（Notification 模块只接收调用，不调用其他模块）

**详细设计见：** `Design-Document-Notification.md`

## 3. Cross-Module Design

### 3.1 API Communication Protocol
**[ID: DESIGN-CROSS-API-001] [Designs-for: RD-CROSS-AUTH-001]**

所有模块间通信使用 RESTful API + JWT 认证。

**API 规范：**
- **协议**：HTTPS
- **格式**：JSON
- **认证**：JWT Bearer Token（放在 Authorization 头）
- **版本控制**：URL 版本（如 /v1/users）

**API 调用示例：**
```
GET /v1/users/123 HTTP/1.1
Host: user-service.internal
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json
```

**错误响应格式：**
```json
{
  "error": "invalid_request",
  "error_description": "Missing required field: email",
  "status_code": 400
}
```

### 3.2 Shared Authentication Middleware
**[ID: DESIGN-CROSS-AUTH-MIDDLEWARE-001] [Designs-for: RD-CROSS-AUTH-001]**

所有模块使用统一的认证中间件验证 JWT。

**实现：**
- **库**：authlib (Python)
- **功能**：
  - 验证 JWT 签名和过期时间
  - 提取用户 ID 和角色
  - 验证角色权限（RBAC）
- **部署**：作为 FastAPI 中间件集成到每个服务

**代码示例（共享库）：**
```python
# shared/auth_middleware.py
from fastapi import Request, HTTPException
from jose import jwt, JWTError

async def verify_token(request: Request):
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        request.state.user_id = payload["user_id"]
        request.state.roles = payload["roles"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
```

### 3.3 Database Sharding Strategy
**[ID: DESIGN-CROSS-DB-SHARD-001]**

采用按模块分库策略，每个模块独立数据库。

**分库原则：**
- **user_db**：存储用户、OAuth 账户、角色
- **order_db**：存储订单、订单商品
- **payment_db**：存储支付记录、退款记录
- **product_db**：存储商品、库存、分类
- **notification_db**：存储通知历史

**跨库查询：**
- 避免跨库 JOIN，通过 API 调用获取关联数据
- 使用 Redis 缓存减少跨库查询

### 3.4 Logging and Monitoring
**[ID: DESIGN-CROSS-LOG-001] [Designs-for: RD-CROSS-AUDIT-001]**

所有模块使用统一的日志格式和监控工具。

**日志格式（JSON）：**
```json
{
  "timestamp": "2025-11-16T10:30:00Z",
  "level": "INFO",
  "service": "user-service",
  "user_id": "123",
  "ip": "192.168.1.1",
  "method": "POST",
  "path": "/auth/login",
  "status_code": 200,
  "duration_ms": 45
}
```

**日志存储：**
- **CloudWatch Logs**：所有日志集中存储
- **ELK Stack**：日志分析和可视化（Kibana）

**监控指标：**
- API 响应时间（P50, P95, P99）
- 错误率（4xx, 5xx）
- 数据库查询时间
- 缓存命中率
```

## Validation Checklist

输出 Design-Document.md（Overview）前验证：
- [ ] 包含 **System Architecture** 部分（[ID: DESIGN-PROJECT-ARCH-001]）
- [ ] 包含架构图表（ASCII 或 Mermaid）
- [ ] 包含技术栈说明（语言、框架、数据库、部署）
- [ ] 包含 **Module Architecture** 部分，列出所有模块
- [ ] 每个模块都有 **[ID: DESIGN-MODULE-XXX-ARCH]** 和 **[Designs-for: PRD-MODULE-XXX]**
- [ ] 每个模块都有技术栈、部署架构、模块间交互说明
- [ ] 每个模块都引用了模块文档（`详细设计见：Design-Document-[Module].md`）
- [ ] 包含 **Cross-Module Design** 部分
- [ ] 跨模块设计都有 **[ID: DESIGN-CROSS-XXX-001]**
- [ ] 跨模块设计有清晰的实现说明和示例
- [ ] 无模块级别的详细设计（如具体 API 端点、数据库表）
- [ ] 无占位符或 TODOs
- [ ] **始终使用 "Design Document" 术语，绝不使用 "DD"**

## Common Pitfalls

- ❌ 使用 "DD" 而不是 "Design Document"
- ❌ 在 Overview 中包含模块详细设计（如具体 API、数据库表）
- ❌ 使用模块级别 ID（如 DESIGN-API-LOGIN）在 Overview 中
- ❌ 架构图表缺失或不清晰
- ❌ 技术栈选择没有理由说明
- ❌ 模块间交互不清晰
- ❌ 跨模块设计定义不明确
- ❌ 忘记引用模块文档（`详细设计见：Design-Document-[Module].md`）

## Next Steps

✅ Design-Document.md（Overview）完成后：
1. 使用 `design-module-generator.md` 为每个模块生成 `Design-Document-[Module].md`
2. 审查所有模块设计文档
3. 验证与 PPRD.md 和 PRD.md 的一致性
4. 进入 Test Plan 阶段

---

**Tips**:
- Overview 文档应保持简洁，聚焦于整体架构和模块架构
- 详细设计留给模块文档，避免 Overview 过长
- 架构图表必须清晰，帮助理解模块间交互
- 技术栈选择必须有理由说明
- **始终使用 "Design Document" 术语，绝不使用 "DD"！**
