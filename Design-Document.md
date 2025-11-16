# **🏗️ Design Document - SpecGovernor**

> **Version**: v2.0
> **Based on**: PRD.md (v2.0) + RD.md (v2.0)
> **Created**: 2025-11-16
> **Updated**: 2025-11-16
> **Design Goal**: 工具箱组件（Prompt Templates、Workflows、Helper Scripts）的详细设计

---

## **Traceability Declaration**

本文档为以下 PRD 功能提供设计：
- [Designs-for: PRD-FEAT-TEMPLATES-001] Prompt Templates
- [Designs-for: PRD-FEAT-WORKFLOWS-001] Workflow Documentation
- [Designs-for: PRD-FEAT-SCRIPTS-001] Helper Scripts
- [Designs-for: PRD-FEAT-SMALL-001] Small Project Support
- [Designs-for: PRD-FEAT-LARGE-001] Large Project Support

---

## **一、Toolkit Architecture**

### **1.1 Overall Structure**

**[ID: DESIGN-ARCH-001] [Designs-for: PRD-STRUCTURE-001]**

```
SpecGovernor Repository/
├── .specgov/                     # 初始化时生成（不在 repo 中）
│   ├── prompts/                  # 从 templates/ 复制
│   ├── workflows/                # 从 templates/ 复制
│   ├── tasks/                    # 生成的任务文件
│   ├── index/                    # 脚本生成的索引
│   │   ├── tags.json
│   │   └── dependency-graph.json
│   └── project-config.json       # 生成的配置
│
├── templates/                    # 源模板（在 repo 中）
│   ├── prompts/                  # 所有 prompt template .md 文件
│   │   ├── rd-generator.md
│   │   ├── rd-reviewer.md
│   │   ├── prd-generator.md
│   │   ├── prd-reviewer.md
│   │   ├── design-generator.md
│   │   ├── design-reviewer.md
│   │   ├── test-plan-generator.md
│   │   ├── test-plan-reviewer.md
│   │   ├── code-generator.md
│   │   ├── code-reviewer.md
│   │   ├── consistency-checker.md        # 一致性检查
│   │   ├── impact-analyzer.md            # 影响分析
│   │   ├── rd-overview-generator.md      # 大项目使用
│   │   ├── rd-module-generator.md        # 大项目使用
│   │   └── ... (其他阶段类似)
│   │
│   └── workflows/                # 所有 workflow 文档
│       ├── workflow-overview.md
│       ├── workflow-rd.md
│       ├── workflow-prd.md
│       ├── workflow-design.md
│       ├── workflow-test-plan.md
│       ├── workflow-task-mgmt.md
│       └── workflow-large-project.md
│
├── scripts/                      # Helper Python 脚本
│   ├── init_project.py
│   ├── parse_tags.py
│   ├── build_graph.py
│   ├── impact_analysis.py
│   └── check_consistency.py
│
├── docs/                         # 生成的文档（用户项目）
│   ├── RD.md                     # （大项目使用 RD/ 目录）
│   ├── PRD.md                    # （大项目使用 PRD/ 目录）
│   ├── Design-Document.md        # （大项目使用 Design-Document/ 目录）
│   └── Test-Plan.md              # （大项目使用 Test-Plan/ 目录）
│
└── README.md                     # SpecGovernor 工具箱文档
```

**核心原则：**
- **Templates 是源头** - 存储在 repo 的 `templates/` 目录中
- **`.specgov/` 是生成的** - 项目初始化时创建
- **无需安装软件** - 只需下载 repo 并运行脚本
- **Git 可追踪** - 所有 templates、workflows、scripts 的变更都有版本控制

---

### **1.2 Component Design**

**[ID: DESIGN-COMP-001]**

| 组件类型 | 格式 | 存储位置 | 用途 |
|---------|------|---------|------|
| **Prompt Templates** | Markdown (.md) | `templates/prompts/` | 引导 Claude Code 生成/审查文档 |
| **Workflow Docs** | Markdown (.md) | `templates/workflows/` | 为人类提供分步指南 |
| **Helper Scripts** | Python (.py) | `scripts/` | 自动化标记解析、图谱构建、影响分析 |
| **Task Files** | Markdown (.md) | `.specgov/tasks/` | 追踪 Epics 和 Tasks（生成，用户编辑） |
| **Index Files** | JSON (.json) | `.specgov/index/` | 存储解析的标记和依赖图谱（生成） |

---

## **二、Prompt Template Design**

### **2.1 General Template Structure**

**[ID: DESIGN-TEMPLATE-STRUCT-001] [Designs-for: PRD-FEAT-TEMPLATES-001]**

所有 prompt templates 遵循以下结构：

```markdown
# [Document Type] Generator / Reviewer

## Role
你是一位 [角色名称]（例如：Requirements Analyst、Architect、Test Manager）。

## Task
[生成/审查] [文档类型]，基于提供的输入。

## Critical Requirements

### 1. Traceability Tags
- 必须在每个章节嵌入标记：
  - [ID: XXX] - 唯一标识符
  - [Implements: XXX] / [Designs-for: XXX] / [Tests-for: XXX] - 链接到上游

### 2. Document Structure
[该文档类型的具体结构]

### 3. Naming Conventions
- 使用正确术语："Design Document"（不是 "DD"）、"Test Plan"（不是 "TD"）
- ID 前缀：RD-XXX、PRD-XXX、DESIGN-XXX、TEST-XXX、CODE-XXX

## Input Format
[用户应提供的输入]

## Output Format
[详细结构，附带示例]

## Examples
[展示正确标记用法的具体示例]

## Validation Checklist
- [ ] 所有主要章节都有 [ID: XXX] 标记
- [ ] 所有对上游文档的引用都使用正确标记
- [ ] 全文使用正确术语
- [ ] ...（特定于文档类型）
```

---

### **2.2 RD Generator Template**

**[ID: DESIGN-TEMPLATE-RD-GEN-001] [Designs-for: PRD-FEAT-TEMPLATES-001]**

**文件**: `templates/prompts/rd-generator.md`

**关键章节：**

```markdown
# Requirements Document (RD) Generator

## Role
你是一位经验丰富的 Requirements Analyst。

## Task
根据用户故事、业务需求或现有 RD.md 生成或修改 Requirements Document (RD)。

## Critical Requirements

### 1. Traceability Tags
- 每个需求必须有：**[ID: RD-REQ-XXX]** 或 **[ID: RD-{CATEGORY}-XXX]**
- 分层需求使用：**[Decomposes: PARENT-ID]**

### 2. Document Structure
# Requirements Document (RD)

> **Version**: X.X
> **Created**: YYYY-MM-DD
> **Updated**: YYYY-MM-DD

## 1. [Category] Requirements
**[ID: RD-CATEGORY-001]**

### 1.1 [Specific Requirement]
**[ID: RD-REQ-001] [Decomposes: RD-CATEGORY-001]**

[需求描述，附带清晰的验收标准]

### 3. Large Project Support
- 对于大项目（≥ 10 万行代码），使用模块特定 ID：
  - **[ID: RD-User-REQ-001] [Module: User]**
  - **[ID: RD-Order-REQ-001] [Module: Order]**

## Input Format
1. 如果创建新 RD：
   - 用户故事
   - 业务需求
   - 项目上下文

2. 如果修改现有 RD：
   - 现有 RD.md 内容
   - 变更请求
   - 审查反馈

## Output Format
Markdown 文件，包含：
- 清晰的分层结构
- 每个需求都有 [ID: XXX] 标记
- 适当位置的分解标记
- 每个需求的验收标准

## Examples

### Example 1: User Authentication Requirement

## 1. User Authentication Requirements
**[ID: RD-AUTH-001]**

本节定义所有身份验证和授权需求。

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

## Validation Checklist
输出前验证：
- [ ] 每个主要需求都有 [ID: RD-XXX]
- [ ] 分层需求使用 [Decomposes: XXX]
- [ ] 验收标准清晰定义
- [ ] 无占位符或 TODOs
- [ ] 对于大项目，存在 [Module: XXX] 标记
```

---

### **2.3 PRD Generator Template**

**[ID: DESIGN-TEMPLATE-PRD-GEN-001] [Designs-for: PRD-FEAT-TEMPLATES-001]**

**文件**: `templates/prompts/prd-generator.md`

**关键章节：**

```markdown
# Product Requirements Document (PRD) Generator

## Role
你是一位经验丰富的 Product Manager。

## Task
根据 RD.md 和产品愿景生成或修改 Product Requirements Document (PRD)。

## Critical Requirements

### 1. Traceability Tags
- 每个功能必须有：**[ID: PRD-FEAT-XXX]**
- 每个用户故事必须有：**[ID: PRD-US-XXX]**
- 必须链接到 RD：**[Implements: RD-REQ-XXX]**

### 2. Document Structure
# Product Requirements Document (PRD)

> **Version**: X.X
> **Based on**: RD.md (vX.X)

## 1. Product Features

### 1.1 [Feature Name]
**[ID: PRD-FEAT-XXX] [Implements: RD-REQ-XXX]**

#### User Story
> **As** [用户类型]
> **I want** [目标]
> **So that** [收益]

#### Acceptance Criteria
- ✅ [标准 1]
- ✅ [标准 2]

## Input Format
1. RD.md（需求文档）
2. 产品愿景声明
3. 用户画像（如有）
4. 现有 PRD.md（如果修改）

## Output Format
Markdown 文件，包含：
- 产品功能，带 [ID: PRD-FEAT-XXX]
- 用户故事，带 [ID: PRD-US-XXX]
- [Implements: RD-REQ-XXX] 将每个功能链接到需求

## Examples

### Example: OAuth2 Login Feature

## 2. Authentication Features

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

## Validation Checklist
- [ ] 每个功能都有 [ID: PRD-FEAT-XXX]
- [ ] 每个功能都通过 [Implements: RD-REQ-XXX] 链接到 RD
- [ ] 用户故事遵循 As/I want/So that 格式
- [ ] 验收标准可测试
```

---

### **2.4 Design Document Generator Template**

**[ID: DESIGN-TEMPLATE-DESIGN-GEN-001] [Designs-for: PRD-FEAT-TEMPLATES-001]**

**文件**: `templates/prompts/design-generator.md`

**关键章节：**

```markdown
# Design Document Generator

## Role
你是一位经验丰富的 Software Architect。

## Task
根据 PRD.md 和技术约束生成或修改 Design Document。

## Critical Requirements

### 1. Traceability Tags
- 架构设计：**[ID: DESIGN-ARCH-XXX]**
- API 设计：**[ID: DESIGN-API-XXX]**
- 数据库设计：**[ID: DESIGN-DB-XXX]**
- 必须链接到 PRD：**[Designs-for: PRD-FEAT-XXX]**

### 2. Terminology
- 始终使用 "Design Document"（绝不使用 "DD"）
- 文件名：Design-Document.md（不是 DD.md）

### 3. Document Structure
# Design Document

> **Version**: X.X
> **Based on**: PRD.md (vX.X)

## 1. Architecture Design

### 1.1 [Component Name]
**[ID: DESIGN-ARCH-XXX] [Designs-for: PRD-FEAT-XXX]**

[架构描述，附带图表]

## 2. API Design

### 2.1 [API Endpoint]
**[ID: DESIGN-API-XXX] [Designs-for: PRD-FEAT-XXX]**

**Endpoint**: [METHOD] /path

**Request:**
```json
{...}
```

**Response:**
```json
{...}
```

## 3. Database Design

### 3.1 [Table/Collection Name]
**[ID: DESIGN-DB-XXX] [Designs-for: PRD-FEAT-XXX]**

## Input Format
1. PRD.md（产品需求）
2. 技术约束（语言、框架、云平台等）
3. 现有 Design-Document.md（如果修改）

## Output Format
Markdown 文件，包含：
- 架构图和描述
- API 规范
- 数据库模式
- [Designs-for: PRD-XXX] 将每个设计链接到功能

## Examples

### Example: OAuth2 API Design

## 2. API Design

### 2.1 OAuth2 Callback Endpoint
**[ID: DESIGN-API-008] [Designs-for: PRD-FEAT-012]**

处理用户授权应用后的 OAuth2 回调。

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

**Response (Error):**
```json
{
  "error": "invalid_grant",
  "error_description": "Invalid authorization code"
}
```

**实现说明：**
- 验证提供商是否支持
- 使用提供商的 OAuth2 API 将授权码交换为访问令牌
- 在数据库中创建或更新用户
- 为会话管理生成 JWT

## Validation Checklist
- [ ] 所有设计都有 [ID: DESIGN-XXX]
- [ ] 所有设计都通过 [Designs-for: PRD-XXX] 链接到 PRD
- [ ] API 规范包含请求/响应示例
- [ ] 数据库模式显示所有字段
- [ ] 始终使用 "Design Document" 术语
```

---

### **2.5 Test Plan Generator Template**

**[ID: DESIGN-TEMPLATE-TEST-GEN-001] [Designs-for: PRD-FEAT-TEMPLATES-001]**

**文件**: `templates/prompts/test-plan-generator.md`

**关键章节：**

```markdown
# Test Plan Generator

## Role
你是一位经验丰富的 Test Manager / QA Engineer。

## Task
根据 Design Document 和 PRD 生成或修改 Test Plan。

## Critical Requirements

### 1. Traceability Tags
- 测试用例：**[ID: TEST-CASE-XXX]**
- 必须链接到设计：**[Tests-for: DESIGN-API-XXX]**
- 也可以链接到 PRD：**[Tests-for: PRD-FEAT-XXX]**

### 2. Terminology
- 始终使用 "Test Plan"（绝不使用 "TD"）
- 文件名：Test-Plan.md（不是 TD.md）

### 3. Document Structure
# Test Plan

> **Version**: X.X
> **Based on**: Design-Document.md (vX.X)

## 1. Test Strategy

[整体测试方法]

## 2. Test Cases

### 2.1 [Feature/Component] Tests
**[ID: TEST-CASE-XXX] [Tests-for: DESIGN-API-XXX]**

#### Test Case: [Scenario Name]
**[ID: TEST-CASE-XXX-001]**

**前置条件：**
- [前置条件 1]

**步骤：**
1. [步骤 1]
2. [步骤 2]

**预期结果：**
- ✅ [预期结果 1]

## Input Format
1. Design-Document.md（技术设计）
2. PRD.md（产品需求）
3. 现有 Test-Plan.md（如果修改）

## Output Format
Markdown 文件，包含：
- 测试策略概述
- 详细测试用例，附带步骤和预期结果
- [Tests-for: DESIGN-XXX] 将每个测试链接到设计

## Examples

### Example: OAuth2 API Test Cases

## 5. Authentication API Tests

### 5.1 OAuth2 Callback Endpoint Tests
**[ID: TEST-CASE-015] [Tests-for: DESIGN-API-008]**

#### Test Case: Successful Google OAuth2 Login
**[ID: TEST-CASE-015-001]**

**前置条件：**
- 用户拥有有效的 Google 账户
- 应用已在 Google OAuth2 注册
- 用户已授权应用

**步骤：**
1. 发送 POST /auth/oauth2/callback，附带有效的 Google 授权码：
   ```json
   {
     "provider": "google",
     "code": "valid_auth_code",
     "redirect_uri": "https://app.example.com/callback"
   }
   ```
2. 验证响应状态为 200
3. 验证响应包含 access_token
4. 验证响应包含 refresh_token
5. 验证响应包含用户对象，带有 id、email、name

**预期结果：**
- ✅ 状态：200 OK
- ✅ access_token：有效的 JWT（可解码，未过期）
- ✅ refresh_token：有效字符串
- ✅ expires_in：3600 秒
- ✅ user.email：匹配 Google 账户邮箱

#### Test Case: Invalid Authorization Code
**[ID: TEST-CASE-015-002]**

**前置条件：**
- 无

**步骤：**
1. 发送 POST /auth/oauth2/callback，附带无效的授权码：
   ```json
   {
     "provider": "google",
     "code": "invalid_code",
     "redirect_uri": "https://app.example.com/callback"
   }
   ```
2. 验证响应状态为 400
3. 验证错误消息清晰

**预期结果：**
- ✅ 状态：400 Bad Request
- ✅ error：\"invalid_grant\"
- ✅ error_description：\"Invalid authorization code\"

## Validation Checklist
- [ ] 所有测试用例都有 [ID: TEST-CASE-XXX]
- [ ] 所有测试用例都通过 [Tests-for: DESIGN-XXX] 链接到设计
- [ ] 前置条件清晰说明
- [ ] 步骤可操作且具体
- [ ] 预期结果可衡量
- [ ] 始终使用 "Test Plan" 术语
```

---

### **2.6 Code Generator Template**

**[ID: DESIGN-TEMPLATE-CODE-GEN-001] [Designs-for: PRD-FEAT-TEMPLATES-001]**

**文件**: `templates/prompts/code-generator.md`

**关键章节：**

```markdown
# Code Generator

## Role
你是一位经验丰富的 Software Developer / Engineer。

## Task
根据 Design Document 和 PRD 生成或修改代码实现。

## Critical Requirements

### 1. Traceability Tags
- 代码注释中必须包含：**[ID: CODE-XXX] [Implements: DESIGN-XXX]**
- 每个主要类、函数、API endpoint 都应有标记
- 标记应放在代码注释中（根据语言使用适当的注释格式）

### 2. Code Quality Standards
- **可读性**：清晰的变量命名、适当的注释
- **可维护性**：模块化设计、单一职责原则
- **错误处理**：完善的异常处理和错误日志
- **性能**：考虑时间和空间复杂度
- **安全性**：防止常见漏洞（SQL 注入、XSS、CSRF 等）

### 3. Language-Specific Standards
根据项目技术栈遵循相应的编码规范：
- **Python**: PEP 8
- **TypeScript/JavaScript**: ESLint + Prettier
- **Java**: Google Java Style Guide
- **Go**: Effective Go
- **C#**: Microsoft C# Coding Conventions

### 4. Documentation Requirements
- 每个函数/方法都有文档注释
- API endpoints 有完整的参数和返回值说明
- 复杂逻辑有行内注释解释

## Input Format
1. 如果创建新代码：
   - Design Document（技术设计）
   - PRD（产品功能，供参考）
   - 技术栈和框架要求
   - 项目编码规范

2. 如果修改现有代码：
   - 现有代码文件
   - Design Document（更新的设计）
   - 变更请求或 bug 修复说明

## Output Format
代码文件，包含：
- 可追溯性标记（代码注释中的 [ID: CODE-XXX] [Implements: DESIGN-XXX]）
- 遵循项目编码规范
- 完善的错误处理
- 适当的日志记录
- 文档注释

## Examples

### Example 1: TypeScript API Controller

\```typescript
/**
 * OAuth2 Authentication Controller
 * Handles OAuth2 callback and user authentication
 *
 * [ID: CODE-API-008] [Implements: DESIGN-API-008]
 */
import { Request, Response } from 'express';
import { OAuth2Service } from '../services/oauth2.service';
import { UserService } from '../services/user.service';
import { AuthService } from '../services/auth.service';
import { Logger } from '../utils/logger';

const logger = new Logger('AuthController');

export class AuthController {
    constructor(
        private oauth2Service: OAuth2Service,
        private userService: UserService,
        private authService: AuthService
    ) {}

    /**
     * Handle OAuth2 callback
     * POST /auth/oauth2/callback
     *
     * @param req Express request with provider, code, redirect_uri
     * @param res Express response
     * @returns JWT access token and user info
     */
    async oauth2Callback(req: Request, res: Response): Promise<void> {
        try {
            const { provider, code, redirect_uri } = req.body;

            // Validate provider
            const validProviders = ['google', 'github', 'microsoft'];
            if (!validProviders.includes(provider)) {
                logger.warn(`Invalid OAuth2 provider: ${provider}`);
                res.status(400).json({
                    error: 'invalid_provider',
                    error_description: 'Supported providers: google, github, microsoft'
                });
                return;
            }

            // Validate required fields
            if (!code || !redirect_uri) {
                res.status(400).json({
                    error: 'invalid_request',
                    error_description: 'Missing required fields: code, redirect_uri'
                });
                return;
            }

            // Exchange authorization code for access token
            logger.info(`Exchanging OAuth2 code for provider: ${provider}`);
            const tokens = await this.oauth2Service.exchangeCode(
                provider,
                code,
                redirect_uri
            );

            // Get user profile from provider
            const profile = await this.oauth2Service.getUserProfile(
                provider,
                tokens.access_token
            );

            // Create or update user in database
            const user = await this.userService.createOrUpdate({
                email: profile.email,
                name: profile.name,
                avatar: profile.avatar,
                provider: provider,
                providerId: profile.id
            });

            // Generate JWT tokens
            const jwt = this.authService.generateJWT({
                userId: user.id,
                email: user.email
            });

            logger.info(`User ${user.email} authenticated successfully via ${provider}`);

            res.json({
                access_token: jwt.access_token,
                refresh_token: jwt.refresh_token,
                expires_in: 3600,
                user: {
                    id: user.id,
                    email: user.email,
                    name: user.name,
                    avatar: user.avatar
                }
            });

        } catch (error) {
            logger.error('OAuth2 callback failed:', error);

            // Handle specific errors
            if (error.code === 'INVALID_GRANT') {
                res.status(400).json({
                    error: 'invalid_grant',
                    error_description: 'Invalid authorization code'
                });
            } else if (error.code === 'PROVIDER_ERROR') {
                res.status(502).json({
                    error: 'provider_error',
                    error_description: 'OAuth2 provider error'
                });
            } else {
                res.status(500).json({
                    error: 'server_error',
                    error_description: 'Internal server error'
                });
            }
        }
    }
}
\```

### Example 2: Python Service Class

\```python
"""
OAuth2 Service - Handles OAuth2 provider interactions

[ID: CODE-SERVICE-009] [Implements: DESIGN-SERVICE-009]
"""
import requests
from typing import Dict, Any
from .exceptions import OAuth2Error, InvalidGrantError
from .logger import get_logger

logger = get_logger(__name__)


class OAuth2Service:
    """Service for OAuth2 authentication with multiple providers"""

    PROVIDER_CONFIG = {
        'google': {
            'token_url': 'https://oauth2.googleapis.com/token',
            'user_info_url': 'https://www.googleapis.com/oauth2/v2/userinfo'
        },
        'github': {
            'token_url': 'https://github.com/login/oauth/access_token',
            'user_info_url': 'https://api.github.com/user'
        },
        'microsoft': {
            'token_url': 'https://login.microsoftonline.com/common/oauth2/v2.0/token',
            'user_info_url': 'https://graph.microsoft.com/v1.0/me'
        }
    }

    def __init__(self, client_secrets: Dict[str, Dict[str, str]]):
        """
        Initialize OAuth2 service

        Args:
            client_secrets: Dict mapping provider name to client_id and client_secret
                           Example: {'google': {'client_id': '...', 'client_secret': '...'}}
        """
        self.client_secrets = client_secrets

    def exchange_code(
        self,
        provider: str,
        code: str,
        redirect_uri: str
    ) -> Dict[str, Any]:
        """
        Exchange authorization code for access token

        Args:
            provider: OAuth2 provider name (google/github/microsoft)
            code: Authorization code from provider
            redirect_uri: Redirect URI used in authorization request

        Returns:
            Dict containing access_token, refresh_token, expires_in

        Raises:
            InvalidGrantError: If authorization code is invalid
            OAuth2Error: If provider returns an error
        """
        if provider not in self.PROVIDER_CONFIG:
            raise ValueError(f"Unsupported provider: {provider}")

        config = self.PROVIDER_CONFIG[provider]
        secrets = self.client_secrets.get(provider)

        if not secrets:
            raise OAuth2Error(f"No client secrets configured for {provider}")

        # Prepare token request
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': redirect_uri,
            'client_id': secrets['client_id'],
            'client_secret': secrets['client_secret']
        }

        try:
            logger.info(f"Exchanging code with {provider}")
            response = requests.post(
                config['token_url'],
                data=data,
                headers={'Accept': 'application/json'},
                timeout=10
            )

            if response.status_code != 200:
                error_data = response.json()
                if error_data.get('error') == 'invalid_grant':
                    raise InvalidGrantError("Invalid authorization code")
                raise OAuth2Error(f"Token exchange failed: {error_data}")

            tokens = response.json()
            logger.info(f"Successfully exchanged code for {provider}")

            return {
                'access_token': tokens['access_token'],
                'refresh_token': tokens.get('refresh_token'),
                'expires_in': tokens.get('expires_in', 3600)
            }

        except requests.RequestException as e:
            logger.error(f"HTTP error during token exchange: {e}")
            raise OAuth2Error(f"Provider communication error: {e}")

    def get_user_profile(self, provider: str, access_token: str) -> Dict[str, Any]:
        """
        Get user profile from OAuth2 provider

        Args:
            provider: OAuth2 provider name
            access_token: Valid access token

        Returns:
            Dict containing user profile (id, email, name, avatar)

        Raises:
            OAuth2Error: If profile fetch fails
        """
        if provider not in self.PROVIDER_CONFIG:
            raise ValueError(f"Unsupported provider: {provider}")

        config = self.PROVIDER_CONFIG[provider]

        try:
            logger.info(f"Fetching user profile from {provider}")
            response = requests.get(
                config['user_info_url'],
                headers={'Authorization': f'Bearer {access_token}'},
                timeout=10
            )

            if response.status_code != 200:
                raise OAuth2Error(f"Profile fetch failed: {response.status_code}")

            profile = response.json()

            # Normalize profile across providers
            return self._normalize_profile(provider, profile)

        except requests.RequestException as e:
            logger.error(f"HTTP error during profile fetch: {e}")
            raise OAuth2Error(f"Provider communication error: {e}")

    def _normalize_profile(self, provider: str, raw_profile: Dict) -> Dict[str, Any]:
        """Normalize profile data across different providers"""
        if provider == 'google':
            return {
                'id': raw_profile['id'],
                'email': raw_profile['email'],
                'name': raw_profile['name'],
                'avatar': raw_profile.get('picture')
            }
        elif provider == 'github':
            return {
                'id': str(raw_profile['id']),
                'email': raw_profile['email'],
                'name': raw_profile['name'] or raw_profile['login'],
                'avatar': raw_profile.get('avatar_url')
            }
        elif provider == 'microsoft':
            return {
                'id': raw_profile['id'],
                'email': raw_profile['userPrincipalName'],
                'name': raw_profile['displayName'],
                'avatar': None  # Microsoft Graph doesn't provide avatar in basic profile
            }
        else:
            raise ValueError(f"Unknown provider: {provider}")
\```

## Validation Checklist
输出前验证：
- [ ] 所有主要类/函数都有 [ID: CODE-XXX] [Implements: DESIGN-XXX] 标记
- [ ] 代码遵循项目编码规范
- [ ] 所有函数都有文档注释
- [ ] 错误处理完善（try-catch, 错误日志）
- [ ] 输入验证完整（防止注入攻击）
- [ ] 敏感信息不硬编码（使用环境变量或配置）
- [ ] 适当的日志记录（info, warn, error）
- [ ] 无明显的性能问题（如 N+1 查询）
- [ ] 无安全漏洞（OWASP Top 10）
```

---

### **2.7 Code Reviewer Template**

**[ID: DESIGN-TEMPLATE-CODE-REV-001] [Designs-for: PRD-FEAT-TEMPLATES-001]**

**文件**: `templates/prompts/code-reviewer.md`

**关键章节：**

```markdown
# Code Reviewer

## Role
你是一位经验丰富的 Senior Developer / Code Reviewer，专注于代码质量、安全性和最佳实践。

## Task
审查代码的质量、安全性、性能和可追溯性。

## Critical Requirements

### 1. Review Dimensions
必须从以下维度审查代码：
- **可追溯性**：是否有正确的标记
- **代码质量**：可读性、可维护性、模块化
- **安全性**：是否存在常见漏洞
- **性能**：是否有性能瓶颈
- **错误处理**：是否完善
- **测试覆盖**：是否需要更多测试
- **文档**：注释是否充分

### 2. Security Checklist (OWASP Top 10)
- [ ] **注入攻击**：SQL、NoSQL、OS 命令注入
- [ ] **身份验证失效**：密码存储、会话管理
- [ ] **敏感数据暴露**：加密、HTTPS
- [ ] **XXE（XML 外部实体）**
- [ ] **访问控制失效**：权限检查
- [ ] **安全配置错误**：默认密码、调试模式
- [ ] **XSS（跨站脚本）**
- [ ] **不安全的反序列化**
- [ ] **使用含有已知漏洞的组件**
- [ ] **日志和监控不足**

### 3. Code Quality Checklist
- [ ] 变量命名清晰且符合规范
- [ ] 函数/方法职责单一
- [ ] 避免重复代码（DRY 原则）
- [ ] 适当的抽象和封装
- [ ] 遵循项目编码规范

## Input Format
1. 代码文件（需要审查的代码）
2. Design Document（了解设计意图）
3. 编码规范（项目特定的规范）

## Output Format
结构化的审查报告：

\```markdown
# Code Review Report

## Summary
✓ 总体质量：[优秀/良好/一般/需改进]
⚠️  发现 [N] 个问题（[X] 关键，[Y] 重要，[Z] 建议）

## Critical Issues (必须修复)
### 1. [安全性/性能/错误] - [文件名:行号]
- **问题**：[描述]
- **风险**：[影响]
- **建议**：[具体修复方案]

## Important Issues (应该修复)
### 1. [代码质量/可维护性] - [文件名:行号]
- **问题**：[描述]
- **建议**：[改进建议]

## Suggestions (可选改进)
### 1. [性能优化/代码风格] - [文件名:行号]
- **建议**：[改进建议]

## Traceability Check
✓ 所有主要类/函数都有 [ID: CODE-XXX] 标记
✓ 所有标记都正确引用 [Implements: DESIGN-XXX]
✗ 发现 2 个缺失的可追溯性标记

## Security Analysis
✓ 无明显的注入漏洞
✓ 输入验证完善
⚠️  建议：敏感数据（access_token）应加密存储

## Performance Analysis
✓ 无明显性能瓶颈
✓ 数据库查询已优化
⚠️  建议：考虑为用户查询添加缓存

## Test Coverage Recommendations
建议添加以下测试：
1. 单元测试：OAuth2Service.exchange_code() 的错误处理
2. 集成测试：完整的 OAuth2 登录流程
3. 安全测试：无效 token 的处理

## Overall Recommendations
1. 修复 2 个关键安全问题
2. 添加缺失的可追溯性标记
3. 改进错误日志（添加上下文信息）
4. 考虑添加单元测试
\```

## Review Examples

### Example: Security Issue

\```markdown
### 1. [关键-安全性] SQL 注入风险 - user_service.py:45
- **问题**：直接拼接 SQL 查询，存在 SQL 注入风险
  \```python
  query = f"SELECT * FROM users WHERE email = '{email}'"
  \```
- **风险**：攻击者可以通过构造特殊的 email 值来执行任意 SQL 命令
- **建议**：使用参数化查询
  \```python
  query = "SELECT * FROM users WHERE email = ?"
  cursor.execute(query, (email,))
  \```
\```

### Example: Code Quality Issue

\```markdown
### 1. [重要-代码质量] 函数过长 - auth_controller.ts:50
- **问题**：oauth2Callback() 函数有 150 行，职责过多
- **建议**：拆分为多个小函数
  - validateOAuth2Request()
  - exchangeCodeForTokens()
  - createOrUpdateUser()
  - generateJWTResponse()
\```

## Validation Checklist
审查报告必须包含：
- [ ] 总体质量评分
- [ ] 按严重程度分类的问题列表
- [ ] 每个问题都有具体的修复建议
- [ ] 可追溯性检查结果
- [ ] 安全性分析
- [ ] 性能分析（如适用）
- [ ] 测试覆盖建议
```

---

### **2.8 Reviewer Templates Summary**

**[ID: DESIGN-TEMPLATE-REVIEWERS-001] [Designs-for: PRD-FEAT-TEMPLATES-001]**

所有 reviewer templates 遵循与 generators 类似的结构，但专注于：

1. **完整性检查**：所有章节都存在吗？
2. **可追溯性验证**：所有标记都存在并引用有效 ID 吗？
3. **质量评估**：内容清晰、无歧义、可测试吗？
4. **一致性检查**：内容与上游文档一致吗？

**示例结构** (`templates/prompts/rd-reviewer.md`)：

```markdown
# Requirements Document (RD) Reviewer

## Role
你是一位独立的 Requirements Review 专家。

## Task
审查 RD.md 的完整性、可追溯性和质量。

## Review Checklist

### 1. Traceability Tags
- [ ] 每个需求都有 [ID: RD-XXX]
- [ ] 所有 [Decomposes: XXX] 引用都指向现有的父级 ID
- [ ] 无重复 ID

### 2. Completeness
- [ ] 所有需求都有清晰的描述
- [ ] 所有需求都有验收标准
- [ ] 无 TODOs 或占位符

### 3. Quality
- [ ] 需求可测试
- [ ] 需求无歧义
- [ ] 需求使用一致的术语

## Output Format
```markdown
# RD Review Report

## Summary
✓ 总体质量：[良好/一般/较差]
⚠️  发现 [N] 条建议，[M] 个关键问题

## Issues

### 1. [严重程度] [章节/ID]
- 位置：[章节 X.X]
- 问题：[描述]
- 建议：[具体修复]

### 2. ...

## Traceability Check
✓ 所有需求都有 [ID: XXX]
✗ 发现 2 个损坏的 [Decomposes: XXX] 引用
```
```

---

## **三、Workflow Documentation Design**

### **3.1 Workflow Overview Document**

**[ID: DESIGN-WORKFLOW-OVERVIEW-001] [Designs-for: PRD-FEAT-WORKFLOWS-001]**

**文件**: `templates/workflows/workflow-overview.md`

**内容结构：**

```markdown
# SpecGovernor Workflow Overview

## 1. Introduction
SpecGovernor 使用 Claude Code 和 prompt templates 提供结构化的 SDLC 工作流。

## 2. SDLC Stages

1. **RD (Requirements Document)**：定义需要构建什么
2. **PRD (Product Requirements Document)**：定义产品功能和用户故事
3. **Design Document**：定义技术架构和设计
4. **Test Plan**：定义测试策略和用例
5. **Code**：实现系统

## 3. Role Perspectives

作为 Super Individual，你将在以下视角之间切换：

- **Project Manager**：创建 Epics，追踪整体进度
- **Requirements Analyst**：生成和审查 RD
- **Product Manager**：生成和审查 PRD
- **Architect**：生成和审查 Design Document
- **Test Manager**：生成和审查 Test Plan
- **Developer**：实现代码

## 4. General Workflow for Each Stage

### Step 1: Switch to Role Perspective
打开 `.specgov/tasks/[role].md` 查看分配的任务。

### Step 2: Load Generator Prompt in Claude Code
打开 Claude Code，加载 `.specgov/prompts/[stage]-generator.md`。

### Step 3: Provide Context
- 上游文档（例如，生成 PRD 时提供 RD.md）
- 额外的需求或约束

### Step 4: Generate Document
Claude Code 生成带有嵌入式可追溯性标记的文档。

### Step 5: Review Document
切换视角（或使用同一角色），加载 reviewer prompt，审查生成的文档。

### Step 6: Revise Based on Feedback
再次使用 generator prompt（修改模式）处理审查反馈。

### Step 7: Update Task Documents
- 更新你的角色特定任务文件（`.specgov/tasks/[role].md`）
- 切换到 Project Manager 视角
- 更新 `.specgov/tasks/project-manager.md`，记录 Epic 进度

## 5. Key Principles
- **显式可追溯性**：始终嵌入标记
- **双重质量保证**：生成 + 审查
- **双层任务**：Epic (PM) + Tasks (Roles)
- **正确术语**：Design Document、Test Plan（不是 DD、TD）

## 6. Next Steps
查看每个阶段的详细工作流：
- [RD Workflow](workflow-rd.md)
- [PRD Workflow](workflow-prd.md)
- [Design Document Workflow](workflow-design.md)
- [Test Plan Workflow](workflow-test-plan.md)
```

---

### **3.2 Stage-Specific Workflows**

**[ID: DESIGN-WORKFLOW-STAGES-001] [Designs-for: PRD-FEAT-WORKFLOWS-001]**

每个阶段特定的工作流（`workflow-rd.md`、`workflow-prd.md` 等）提供：

1. **前置条件**：需要哪些文档/输入
2. **角色视角**：切换到哪个角色
3. **分步流程**：详细指引
4. **示例**：具体示例，附带截图/代码块
5. **常见陷阱**：避免什么
6. **检查清单**：进入下一阶段前的最终验证

**示例** (`templates/workflows/workflow-design.md`)：

```markdown
# Design Document Workflow

## Prerequisites
- ✅ PRD.md 已完成并审查
- ✅ RD.md 可供参考
- ✅ 已识别技术约束（语言、框架、云等）

## Role Perspective
切换到 **Architect** 角色。

## Step-by-Step Process

### Step 1: Review PRD and Technical Constraints
打开 PRD.md，识别所有需要技术设计的功能。
列出技术约束（例如，"必须使用 Python/FastAPI，部署在 AWS Lambda"）。

### Step 2: Open Claude Code and Load Prompt
1. 打开 Claude Code
2. 加载 `.specgov/prompts/design-generator.md`

### Step 3: Provide Context
向 Claude Code 提供以下输入：

**输入：**
- docs/PRD.md 的完整内容
- docs/RD.md 的完整内容（供参考）
- 技术约束：
  - 编程语言：Python 3.11
  - 框架：FastAPI
  - 数据库：PostgreSQL
  - 部署：AWS Lambda + RDS
  - 身份验证：JWT

### Step 4: Generate Design Document
Claude Code 将生成 Design-Document.md，包含：
- 架构设计 [ID: DESIGN-ARCH-XXX]
- API 规范 [ID: DESIGN-API-XXX]
- 数据库模式 [ID: DESIGN-DB-XXX]
- 每个章节都用 [Designs-for: PRD-FEAT-XXX] 标记

保存输出到 `docs/Design-Document.md`。

### Step 5: Review Design Document
1. 切换视角（可以保持 Architect 或切换到另一个角色以保持独立性）
2. 在 Claude Code 中加载 `.specgov/prompts/design-reviewer.md`
3. 提供 docs/Design-Document.md 进行审查
4. Claude Code 输出审查报告

### Step 6: Address Review Feedback
如果审查识别出问题：
1. 再次加载 `.specgov/prompts/design-generator.md`
2. 提供现有 Design-Document.md + 审查反馈
3. Claude Code 修改文档
4. 如需要，重复审查

### Step 7: Update Task Documents
1. 打开 `.specgov/tasks/architect.md`
2. 将 Design Document 生成任务标记为完成
3. 添加关键设计决策的笔记
4. 切换到 Project Manager 视角
5. 打开 `.specgov/tasks/project-manager.md`
6. 更新 Epic 进度（例如，60% → 80%）
7. 将两个文件都提交到 Git

## Example Output

## 2. API Design

### 2.1 OAuth2 Callback Endpoint
**[ID: DESIGN-API-008] [Designs-for: PRD-FEAT-012]**

**Endpoint**: POST /auth/oauth2/callback

**Request:**
```json
{
  "provider": "google",
  "code": "4/0AY0e-g7...",
  "redirect_uri": "https://app.example.com/callback"
}
```

**Response (Success):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "def50200...",
  "expires_in": 3600,
  "user": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "john.doe@gmail.com",
    "name": "John Doe",
    "avatar": "https://lh3.googleusercontent.com/..."
  }
}
```

**实现：**
1. 验证提供商（google/github/microsoft）
2. 通过提供商的 OAuth2 API 将授权码交换为访问令牌
3. 从提供商获取用户个人资料
4. 在 PostgreSQL users 表中创建或更新用户
5. 生成 JWT access_token 和 refresh_token
6. 返回令牌和用户信息

## Common Pitfalls
- ❌ 忘记添加 [Designs-for: PRD-XXX] 标记
- ❌ 使用 "DD" 而不是 "Design Document"
- ❌ API 规范中缺少足够细节（缺少错误响应）
- ❌ 设计时未考虑部署约束

## Validation Checklist
进入 Test Plan 阶段前：
- [ ] 所有设计都有 [ID: DESIGN-XXX] 标记
- [ ] 所有设计都通过 [Designs-for: PRD-XXX] 链接到 PRD
- [ ] API 规范包含请求、响应（成功 + 错误）和实现说明
- [ ] 数据库模式显示所有字段、索引、关系
- [ ] 架构符合技术约束
- [ ] 审查已完成并处理反馈
- [ ] 任务文档已更新（architect.md + project-manager.md）
- [ ] 变更已提交到 Git
```

---

## **四、Helper Scripts Design**

### **4.1 Project Initialization Script**

**[ID: DESIGN-SCRIPT-INIT-001] [Designs-for: PRD-FEAT-SCRIPTS-001]**

**文件**: `scripts/init_project.py`

**用途**：为用户项目初始化 SpecGovernor 结构

**算法：**

```python
#!/usr/bin/env python3
"""
初始化 SpecGovernor 项目结构。
"""
import os
import json
import shutil
from datetime import datetime

def prompt_project_size():
    """提示用户选择项目规模。"""
    print("请选择项目规模：")
    print("1. 小项目（< 10 万行代码，单层文档结构）")
    print("2. 大项目（≥ 10 万行代码，双层文档结构）")

    while True:
        choice = input("您的选择 (1/2): ").strip()
        if choice in ['1', '2']:
            return 'small' if choice == '1' else 'large'
        print("无效选择，请输入 1 或 2")

def create_directory_structure(project_size):
    """根据项目规模创建目录结构。"""
    # 创建 .specgov/ 目录
    os.makedirs('.specgov', exist_ok=True)
    os.makedirs('.specgov/prompts', exist_ok=True)
    os.makedirs('.specgov/workflows', exist_ok=True)
    os.makedirs('.specgov/tasks', exist_ok=True)
    os.makedirs('.specgov/index', exist_ok=True)

    # 从 templates/ 复制 prompts
    shutil.copytree('templates/prompts', '.specgov/prompts', dirs_exist_ok=True)
    shutil.copytree('templates/workflows', '.specgov/workflows', dirs_exist_ok=True)

    # 创建任务文件
    task_files = [
        'project-manager.md',
        'rd-analyst.md',
        'product-manager.md',
        'architect.md',
        'test-manager.md'
    ]
    for task_file in task_files:
        create_task_file(f'.specgov/tasks/{task_file}')

    # 创建 docs/ 结构
    if project_size == 'small':
        os.makedirs('docs', exist_ok=True)
        create_placeholder('docs/RD.md', 'Requirements Document')
        create_placeholder('docs/PRD.md', 'Product Requirements Document')
        create_placeholder('docs/Design-Document.md', 'Design Document')
        create_placeholder('docs/Test-Plan.md', 'Test Plan')
    else:  # large
        os.makedirs('docs/RD', exist_ok=True)
        os.makedirs('docs/PRD', exist_ok=True)
        os.makedirs('docs/Design-Document', exist_ok=True)
        os.makedirs('docs/Test-Plan', exist_ok=True)
        create_placeholder('docs/RD/RD-Overview.md', 'Requirements Overview')
        create_placeholder('docs/PRD/PRD-Overview.md', 'Product Overview')
        create_placeholder('docs/Design-Document/Design-Overview.md', 'Design Overview')
        create_placeholder('docs/Test-Plan/Test-Overview.md', 'Test Overview')

    # 创建项目配置
    config = {
        "project_name": os.path.basename(os.getcwd()),
        "project_size": project_size,
        "document_structure": "single-tier" if project_size == 'small' else "two-tier",
        "created_at": datetime.now().isoformat(),
        "modules": []
    }
    with open('.specgov/project-config.json', 'w') as f:
        json.dump(config, f, indent=2)

def create_task_file(filepath):
    """创建带有标题的空任务文件。"""
    role_name = os.path.basename(filepath).replace('.md', '').replace('-', ' ').title()
    content = f"""# {role_name} Tasks

## Active Tasks
（暂无分配的任务）

## Completed Tasks
（暂无完成的任务）
"""
    with open(filepath, 'w') as f:
        f.write(content)

def create_placeholder(filepath, doc_type):
    """创建占位符文档。"""
    content = f"""# {doc_type}

> **Version**: 1.0
> **Created**: {datetime.now().strftime('%Y-%m-%d')}

（此文档将使用 SpecGovernor prompt templates 生成）
"""
    with open(filepath, 'w') as f:
        f.write(content)

def main():
    print("SpecGovernor Project Initialization")
    print("=" * 50)

    project_size = prompt_project_size()
    print(f"\n正在创建 {project_size} 项目结构...")

    create_directory_structure(project_size)

    print("\n✓ SpecGovernor 项目结构创建完成")
    print("\n📚 下一步：")
    print("  1. Review .specgov/workflows/workflow-overview.md")
    print("  2. As Project Manager, create your first Epic in .specgov/tasks/project-manager.md")
    print("  3. Switch to Requirements Analyst role, load .specgov/prompts/rd-generator.md in Claude Code")

if __name__ == '__main__':
    main()
```

---

### **4.2 Tag Parser Script**

**[ID: DESIGN-SCRIPT-PARSER-001] [Designs-for: PRD-FEAT-SCRIPTS-001]**

**文件**: `scripts/parse_tags.py`

**用途**：从所有文件中解析可追溯性标记

**算法：**

```python
#!/usr/bin/env python3
"""
从 Markdown 和代码文件中解析可追溯性标记。
"""
import os
import re
import json
from pathlib import Path

TAG_PATTERNS = {
    'id': r'\[ID:\s*([A-Z0-9-]+)\]',
    'implements': r'\[Implements:\s*([A-Z0-9-]+)\]',
    'decomposes': r'\[Decomposes:\s*([A-Z0-9-]+)\]',
    'designs_for': r'\[Designs-for:\s*([A-Z0-9-]+)\]',
    'tests_for': r'\[Tests-for:\s*([A-Z0-9-]+)\]',
    'module': r'\[Module:\s*([A-Za-z0-9-]+)\]'
}

def scan_files(root_dirs=['docs', 'src']):
    """扫描所有 Markdown 和代码文件。"""
    files = []
    for root_dir in root_dirs:
        if not os.path.exists(root_dir):
            continue
        for filepath in Path(root_dir).rglob('*'):
            if filepath.is_file() and (
                filepath.suffix in ['.md', '.py', '.ts', '.tsx', '.js', '.jsx', '.java', '.go']
            ):
                files.append(str(filepath))
    return files

def parse_file(filepath):
    """从单个文件中解析可追溯性标记。"""
    tags = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                # 查找 ID 标记
                id_match = re.search(TAG_PATTERNS['id'], line)
                if id_match:
                    tag_id = id_match.group(1)
                    tag_entry = {
                        'id': tag_id,
                        'file': filepath,
                        'line': line_num,
                        'type': infer_type(tag_id)
                    }

                    # 在同一行查找关系标记
                    for rel_type, pattern in TAG_PATTERNS.items():
                        if rel_type in ['id', 'module']:
                            continue
                        match = re.search(pattern, line)
                        if match:
                            tag_entry[rel_type] = match.group(1)

                    # 查找模块标记
                    module_match = re.search(TAG_PATTERNS['module'], line)
                    if module_match:
                        tag_entry['module'] = module_match.group(1)

                    tags.append(tag_entry)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")

    return tags

def infer_type(tag_id):
    """从 ID 前缀推断标记类型。"""
    if tag_id.startswith('RD-'):
        return 'requirement'
    elif tag_id.startswith('PRD-FEAT-'):
        return 'feature'
    elif tag_id.startswith('PRD-US-'):
        return 'user_story'
    elif tag_id.startswith('DESIGN-ARCH-'):
        return 'architecture'
    elif tag_id.startswith('DESIGN-API-'):
        return 'api_design'
    elif tag_id.startswith('DESIGN-DB-'):
        return 'database_design'
    elif tag_id.startswith('TEST-CASE-'):
        return 'test_case'
    elif tag_id.startswith('CODE-'):
        return 'code'
    else:
        return 'unknown'

def main():
    print("Parsing traceability tags...")

    files = scan_files()
    print(f"✓ Scanning {len(files)} files")

    all_tags = []
    for filepath in files:
        tags = parse_file(filepath)
        all_tags.extend(tags)

    # 统计标记
    id_count = len(all_tags)
    implements_count = sum(1 for t in all_tags if 'implements' in t)
    decomposes_count = sum(1 for t in all_tags if 'decomposes' in t)
    designs_for_count = sum(1 for t in all_tags if 'designs_for' in t)
    tests_for_count = sum(1 for t in all_tags if 'tests_for' in t)

    # 保存到 JSON
    output = {'tags': all_tags}
    os.makedirs('.specgov/index', exist_ok=True)
    with open('.specgov/index/tags.json', 'w') as f:
        json.dump(output, f, indent=2)

    print(f"✓ Found {id_count} [ID: XXX] tags")
    print(f"✓ Found {implements_count} [Implements: XXX] tags")
    print(f"✓ Found {decomposes_count} [Decomposes: XXX] tags")
    print(f"✓ Found {designs_for_count} [Designs-for: XXX] tags")
    print(f"✓ Found {tests_for_count} [Tests-for: XXX] tags")
    print(f"✓ Saved to .specgov/index/tags.json")

if __name__ == '__main__':
    main()
```

---

### **4.3 Dependency Graph Builder Script**

**[ID: DESIGN-SCRIPT-GRAPH-001] [Designs-for: PRD-FEAT-SCRIPTS-001]**

**文件**: `scripts/build_graph.py`

**用途**：从解析的标记构建依赖图谱

**算法：**

```python
#!/usr/bin/env python3
"""
从解析的标记构建依赖图谱。
"""
import json
import os

def load_tags():
    """从 tags.json 加载标记。"""
    with open('.specgov/index/tags.json', 'r') as f:
        data = json.load(f)
    return data['tags']

def build_graph(tags):
    """从标记构建依赖图谱。"""
    nodes = []
    edges = []

    # 创建节点
    for tag in tags:
        node = {
            'id': tag['id'],
            'type': tag['type'],
            'location': f"{tag['file']}#L{tag['line']}"
        }
        if 'module' in tag:
            node['module'] = tag['module']
        nodes.append(node)

    # 创建边
    for tag in tags:
        source_id = tag['id']

        # Implements 关系
        if 'implements' in tag:
            edges.append({
                'from': source_id,
                'to': tag['implements'],
                'relation': 'implements'
            })

        # Decomposes 关系
        if 'decomposes' in tag:
            edges.append({
                'from': source_id,
                'to': tag['decomposes'],
                'relation': 'decomposes'
            })

        # Designs-for 关系
        if 'designs_for' in tag:
            edges.append({
                'from': source_id,
                'to': tag['designs_for'],
                'relation': 'designs-for'
            })

        # Tests-for 关系
        if 'tests_for' in tag:
            edges.append({
                'from': source_id,
                'to': tag['tests_for'],
                'relation': 'tests-for'
            })

    return {'nodes': nodes, 'edges': edges}

def detect_circular_dependencies(graph):
    """使用 DFS 检测循环依赖。"""
    # 构建邻接表
    adj = {}
    for edge in graph['edges']:
        if edge['from'] not in adj:
            adj[edge['from']] = []
        adj[edge['from']].append(edge['to'])

    visited = set()
    rec_stack = set()
    cycles = []

    def dfs(node, path):
        visited.add(node)
        rec_stack.add(node)

        if node in adj:
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor, path + [neighbor])
                elif neighbor in rec_stack:
                    # 发现循环
                    cycle_start = path.index(neighbor)
                    cycles.append(path[cycle_start:] + [neighbor])

        rec_stack.remove(node)

    for node_data in graph['nodes']:
        node = node_data['id']
        if node not in visited:
            dfs(node, [node])

    return cycles

def count_by_type(graph):
    """按类型统计节点。"""
    counts = {}
    for node in graph['nodes']:
        node_type = node['type']
        counts[node_type] = counts.get(node_type, 0) + 1
    return counts

def main():
    print("Building dependency graph...")

    tags = load_tags()
    graph = build_graph(tags)

    print(f"✓ Created {len(graph['nodes'])} nodes")
    print(f"✓ Created {len(graph['edges'])} edges")

    # 检测循环依赖
    cycles = detect_circular_dependencies(graph)
    if cycles:
        print(f"⚠️  Detected {len(cycles)} circular dependencies:")
        for cycle in cycles:
            print(f"   {' → '.join(cycle)}")
    else:
        print("✓ Detected 0 circular dependencies")

    # 保存图谱
    with open('.specgov/index/dependency-graph.json', 'w') as f:
        json.dump(graph, f, indent=2)
    print("✓ Saved to .specgov/index/dependency-graph.json")

    # 统计信息
    counts = count_by_type(graph)
    print("\n📊 Statistics:")
    for node_type, count in sorted(counts.items()):
        print(f"  - {node_type}: {count}")

if __name__ == '__main__':
    main()
```

---

### **4.4 Impact Analysis Script**

**[ID: DESIGN-SCRIPT-IMPACT-001] [Designs-for: PRD-FEAT-SCRIPTS-001]**

**文件**: `scripts/impact_analysis.py`

**用途**：分析文件变更的影响

**算法：**

```python
#!/usr/bin/env python3
"""
使用 git diff 和依赖图谱分析文件变更的影响。
"""
import json
import subprocess
import argparse
import re

TAG_PATTERN = r'\[ID:\s*([A-Z0-9-]+)\]'

def get_changed_lines(filepath):
    """使用 git diff 获取变更的行号。"""
    try:
        result = subprocess.run(
            ['git', 'diff', 'HEAD', filepath],
            capture_output=True,
            text=True
        )
        diff = result.stdout

        # 解析 diff 以查找变更的行
        changed_lines = []
        current_line = 0
        for line in diff.split('\n'):
            if line.startswith('@@'):
                # 从 @@ -a,b +c,d @@ 中提取行号
                match = re.search(r'\+(\d+)', line)
                if match:
                    current_line = int(match.group(1))
            elif line.startswith('+') and not line.startswith('+++'):
                changed_lines.append(current_line)
                current_line += 1
            elif not line.startswith('-'):
                current_line += 1

        return changed_lines
    except Exception as e:
        print(f"Error running git diff: {e}")
        return []

def find_changed_tags(filepath, changed_lines):
    """在变更的行中查找标记。"""
    changed_tags = []

    try:
        with open(filepath, 'r') as f:
            for line_num, line in enumerate(f, 1):
                if line_num in changed_lines:
                    match = re.search(TAG_PATTERN, line)
                    if match:
                        changed_tags.append(match.group(1))
    except Exception as e:
        print(f"Error reading file: {e}")

    return changed_tags

def load_graph():
    """加载依赖图谱。"""
    with open('.specgov/index/dependency-graph.json', 'r') as f:
        return json.load(f)

def find_downstream(graph, source_ids):
    """查找所有下游节点（BFS）。"""
    # 构建邻接表（反向，用于下游）
    adj = {}
    for edge in graph['edges']:
        # 下游：如果 A implements B，则 B 影响 A
        target = edge['from']
        source = edge['to']
        if source not in adj:
            adj[source] = []
        adj[source].append((target, edge['relation']))

    # 从 source_ids 开始 BFS
    queue = [(sid, None) for sid in source_ids]
    visited = set(source_ids)
    affected = []

    while queue:
        node_id, reason = queue.pop(0)

        if node_id in adj:
            for neighbor, relation in adj[node_id]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    affected.append((neighbor, f"{relation.capitalize()} {node_id}"))
                    queue.append((neighbor, f"{relation} {node_id}"))

    return affected

def get_node_info(graph, node_id):
    """获取节点信息。"""
    for node in graph['nodes']:
        if node['id'] == node_id:
            return node
    return None

def main():
    parser = argparse.ArgumentParser(description='分析文件变更的影响')
    parser.add_argument('--changed', required=True, help='变更的文件路径')
    args = parser.parse_args()

    print("🔍 Analyzing impact...")

    # 获取变更的行
    changed_lines = get_changed_lines(args.changed)
    if not changed_lines:
        print(f"No changes detected in {args.changed}")
        return

    # 查找变更的标记
    changed_tags = find_changed_tags(args.changed, changed_lines)
    if not changed_tags:
        print("No traceability tags found in changed lines")
        return

    # 加载图谱
    graph = load_graph()

    # 查找下游节点
    affected = find_downstream(graph, changed_tags)

    # 打印报告
    print("\n" + "━" * 50)
    print("📊 Impact Analysis Report")
    print("━" * 50)

    print(f"\n变更的节点 ({len(changed_tags)}):")
    for tag_id in changed_tags:
        node = get_node_info(graph, tag_id)
        if node:
            print(f"  • {tag_id} ({node['type']}) at {node['location']}")

    print(f"\n受影响的节点 ({len(affected)}):")
    for node_id, reason in affected:
        node = get_node_info(graph, node_id)
        if node:
            print(f"  ⚠️  {node_id} ({node['type']}) at {node['location']}")
            print(f"      原因：{reason}")

    print("\n建议的行动：")
    print("  1. Review and update affected documents")
    print("  2. Run tests for affected code")
    print("  3. Update dependency graph (python scripts/parse_tags.py && python scripts/build_graph.py)")

    print("\n" + "━" * 50)
    print(f"\n⏱️  Time: < 10 seconds")
    print("💰 Cost: $0 (graph query only)")

if __name__ == '__main__':
    main()
```

---

### **4.5 Consistency Check Script**

**[ID: DESIGN-SCRIPT-CONSISTENCY-001] [Designs-for: PRD-US-003.4]**

**文件**: `scripts/check-consistency.py`

**用途**：为指定需求收集完整依赖链上下文，输出 context.md 供 Claude Code 使用

**算法：**

```python
#!/usr/bin/env python3
"""
为指定需求收集完整依赖链上下文。
"""
import json
import argparse
import re
from pathlib import Path

def load_graph():
    """加载依赖图谱。"""
    with open('.specgov/index/dependency-graph.json', 'r') as f:
        return json.load(f)

def find_dependency_chain(graph, scope_id):
    """找到指定 ID 的完整依赖链（上游和下游）。"""
    chain = {'upstream': [], 'downstream': []}

    # 构建邻接表
    downstream_adj = {}  # id -> [依赖它的节点]
    upstream_adj = {}    # id -> [它依赖的节点]

    for edge in graph['edges']:
        source = edge['from']
        target = edge['to']
        relation = edge['relation']

        # 下游：source 依赖 target，所以 target 的下游包含 source
        if target not in downstream_adj:
            downstream_adj[target] = []
        downstream_adj[target].append((source, relation))

        # 上游：source 依赖 target，所以 source 的上游包含 target
        if source not in upstream_adj:
            upstream_adj[source] = []
        upstream_adj[source].append((target, relation))

    # BFS 查找上游（scope_id 实现了哪些节点）
    visited_up = set()
    queue_up = [scope_id]
    while queue_up:
        node_id = queue_up.pop(0)
        if node_id in visited_up:
            continue
        visited_up.add(node_id)

        if node_id in upstream_adj:
            for target, relation in upstream_adj[node_id]:
                if target not in visited_up:
                    chain['upstream'].append((target, relation))
                    queue_up.append(target)

    # BFS 查找下游（哪些节点实现了 scope_id）
    visited_down = set()
    queue_down = [scope_id]
    while queue_down:
        node_id = queue_down.pop(0)
        if node_id in visited_down:
            continue
        visited_down.add(node_id)

        if node_id in downstream_adj:
            for source, relation in downstream_adj[node_id]:
                if source not in visited_down:
                    chain['downstream'].append((source, relation))
                    queue_down.append(source)

    return chain

def get_node_info(graph, node_id):
    """获取节点信息。"""
    for node in graph['nodes']:
        if node['id'] == node_id:
            return node
    return None

def extract_content(filepath, line_num, context_lines=20):
    """从文件中提取内容，以 line_num 为中心。"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # 查找包含标记的区域（向前向后扩展）
        start = max(0, line_num - context_lines)
        end = min(len(lines), line_num + context_lines)

        # 尝试找到章节边界（以 ## 开头）
        for i in range(line_num - 1, max(0, line_num - 50), -1):
            if lines[i].startswith('##'):
                start = i
                break

        for i in range(line_num, min(len(lines), line_num + 50)):
            if lines[i].startswith('##') and i > line_num:
                end = i
                break

        content = ''.join(lines[start:end])
        return content.strip()

    except Exception as e:
        return f"Error reading file: {e}"

def build_context(graph, scope_id, chain):
    """构建上下文文件内容。"""
    context = []

    context.append("━" * 50)
    context.append(f"# Consistency Check Context for {scope_id}")
    context.append("━" * 50)
    context.append("")

    # 添加上游节点（scope_id 实现了什么）
    if chain['upstream']:
        context.append("## Upstream Dependencies (What this implements)")
        context.append("")
        for i, (node_id, relation) in enumerate(chain['upstream'], 1):
            node = get_node_info(graph, node_id)
            if node:
                context.append(f"### {i}. {node_id} ({node['type']})")
                context.append(f"**Source**: {node['location']}")
                context.append(f"**Relation**: {scope_id} {relation} {node_id}")
                context.append("")

                # 提取内容
                file_path, line_str = node['location'].split('#L')
                line_num = int(line_str)
                content = extract_content(file_path, line_num)
                context.append(content)
                context.append("")
                context.append("---")
                context.append("")

    # 添加当前节点
    current_node = get_node_info(graph, scope_id)
    if current_node:
        context.append(f"## Current Node: {scope_id} ({current_node['type']})")
        context.append(f"**Source**: {current_node['location']}")
        context.append("")

        file_path, line_str = current_node['location'].split('#L')
        line_num = int(line_str)
        content = extract_content(file_path, line_num)
        context.append(content)
        context.append("")
        context.append("---")
        context.append("")

    # 添加下游节点（谁实现了 scope_id）
    if chain['downstream']:
        context.append("## Downstream Dependencies (What implements this)")
        context.append("")
        for i, (node_id, relation) in enumerate(chain['downstream'], 1):
            node = get_node_info(graph, node_id)
            if node:
                context.append(f"### {i}. {node_id} ({node['type']})")
                context.append(f"**Source**: {node['location']}")
                context.append(f"**Relation**: {node_id} {relation} {scope_id}")
                context.append("")

                # 提取内容
                file_path, line_str = node['location'].split('#L')
                line_num = int(line_str)
                content = extract_content(file_path, line_num)
                context.append(content)
                context.append("")
                context.append("---")
                context.append("")

    context.append("━" * 50)

    return '\n'.join(context)

def estimate_tokens(text):
    """粗略估计 token 数（1 token ≈ 4 字符）。"""
    return len(text) // 4

def main():
    parser = argparse.ArgumentParser(
        description='为指定需求收集完整依赖链上下文'
    )
    parser.add_argument('--scope', required=True, help='要检查的需求 ID（如 RD-REQ-005）')
    parser.add_argument('--output', default='context.md', help='输出文件路径')
    args = parser.parse_args()

    print(f"🔍 收集 {args.scope} 的依赖链上下文...")

    # 加载图谱
    graph = load_graph()

    # 验证 scope_id 存在
    node = get_node_info(graph, args.scope)
    if not node:
        print(f"❌ 错误：找不到 {args.scope}")
        return

    # 查找依赖链
    chain = find_dependency_chain(graph, args.scope)

    # 构建上下文
    context_content = build_context(graph, args.scope, chain)

    # 估计 tokens
    token_count = estimate_tokens(context_content)

    # 检查 token 限制
    if token_count > 5000:
        print(f"⚠️  警告：上下文过大（约 {token_count} tokens），超过 5K 限制")
        print("   考虑使用更具体的 scope 或减少 context_lines")

    # 保存到文件
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(context_content)

    # 统计信息
    print(f"✓ 收集了 {args.scope} 的依赖链")
    print(f"✓ 找到 {len(chain['upstream'])} 个上游依赖")
    print(f"✓ 找到 {len(chain['downstream'])} 个下游依赖")
    print(f"✓ 生成上下文文件：{args.output}（约 {token_count} tokens）")
    print(f"✓ 保存到 {args.output}")
    print()
    print("📚 下一步：")
    print("  1. 打开 Claude Code")
    print("  2. 加载 .specgov/prompts/consistency-checker.md")
    print(f"  3. 提供 {args.output} 内容")
    print("  4. Claude Code 将检查一致性并输出报告")
    print()
    print("⏱️  时间：< 5 秒")
    print("💰 成本：$0（本地上下文构建）")

if __name__ == '__main__':
    main()
```

**设计要点：**

1. **依赖链查找**：
   - 双向 BFS：既查找上游（scope_id 实现了什么），也查找下游（谁实现了 scope_id）
   - 构建邻接表以提高查询效率

2. **内容提取**：
   - 从文件中提取标记周围的上下文（默认 20 行）
   - 智能查找章节边界（以 `##` 开头的 Markdown 标题）
   - 确保提取的内容有意义且完整

3. **Token 控制**：
   - 估计 tokens（1 token ≈ 4 字符）
   - 警告如果超过 5K tokens
   - 可通过 `context_lines` 参数调整

4. **输出格式**：
   - 清晰的 Markdown 格式
   - 分为上游、当前节点、下游三部分
   - 每个节点包含：ID、类型、位置、关系、内容

5. **用户体验**：
   - 详细的控制台输出
   - 明确的下一步指导
   - 性能和成本信息

---

## **五、Environment Requirements**

### **5.1 Operating Environment**

**[ID: DESIGN-ENV-001] [Designs-for: PRD-NFR-001]**

**支持的环境：**

| 组件 | 要求 | 说明 |
|------|------|------|
| **操作系统** | Windows 10/11 | 工具包专为 Windows 环境设计 |
| **Shell 环境** | PowerShell 5.1+ | 所有命令行操作使用 PowerShell |
| **Python 版本** | Python 3.8+ | 用于运行 helper scripts |
| **AI 助手** | Claude Code | 必须安装并配置 Claude Code CLI |
| **版本控制** | Git 2.x+ | 用于 impact_analysis.py 的 git diff 功能 |

**环境验证：**

用户可以运行以下命令验证环境：

```powershell
# 验证 Python 版本
python --version
# 应输出：Python 3.8.x 或更高

# 验证 Git 版本
git --version
# 应输出：git version 2.x.x 或更高

# 验证 PowerShell 版本
$PSVersionTable.PSVersion
# 应输出：5.1.x 或更高

# 验证 Claude Code 是否可用
claude --version
# 或者检查 Claude Code 是否已安装
```

**不支持的环境：**
- ❌ macOS / Linux（当前版本不支持，未来可能扩展）
- ❌ Windows PowerShell 5.0 或更早版本
- ❌ Python 2.x 或 Python 3.7 及更早版本
- ❌ 其他 AI 助手（如 GitHub Copilot、GPT-4 API）

**Windows-specific 设计决策：**

1. **路径处理**：
   - 使用 `pathlib.Path` 处理路径（跨平台兼容）
   - 但优化为 Windows 路径分隔符 `\`

2. **命令执行**：
   - 使用 `subprocess.run()` 调用 Git
   - 在 PowerShell 环境中执行

3. **文件编码**：
   - 所有文件使用 UTF-8 编码
   - 明确指定 `encoding='utf-8'` 避免 Windows 默认编码问题

4. **Claude Code 集成**：
   - 假设 Claude Code 已通过 CLI 安装
   - 用户手动在 Claude Code 中加载 prompt templates
   - 未来版本可能支持自动化调用

---

## **五、Non-Functional Requirements**

### **5.1 Performance**

**[ID: DESIGN-NFR-PERF-001] [Designs-for: PRD-NFR-002]**

| 操作 | 目标 | 实现策略 |
|-----|------|---------|
| Tag 解析 | < 1 分钟（10 万行代码） | 使用 regex，并行扫描文件（Python multiprocessing） |
| Graph 构建 | < 1 分钟（10 万行代码） | 内存中的图谱构建，简单邻接表 |
| Impact 分析 | < 10 秒 | 使用 BFS 的图谱查询，无 AI 调用 |
| 项目初始化 | < 5 秒 | 简单的文件/目录创建 |

---

### **5.2 Cost**

**[ID: DESIGN-NFR-COST-001] [Designs-for: PRD-NFR-003]**

| 组件 | 成本 | 原因 |
|-----|------|------|
| Helper scripts | $0 | 纯 Python，本地执行，无外部 API |
| Prompt templates | $0 | 只是 markdown 文件 |
| 使用 templates 与 Claude | 用户的 Claude API 成本 | 用户为自己的 Claude Code 使用付费 |

---

### **5.3 Maintainability**

**[ID: DESIGN-NFR-MAINT-001] [Designs-for: PRD-NFR-004]**

- 所有 templates：纯 markdown（无专有格式）
- 所有 scripts：Python 3.8+，仅使用标准库
- 核心功能无外部依赖
- Git 可追踪：所有变更都有版本控制
- 可扩展：用户可以编辑 templates，添加自定义 scripts

---

## **六、Summary**

### **6.1 Deliverables**

**[ID: DESIGN-SUMMARY-001]**

基于此 Design Document，将实现以下内容：

1. **Prompt Templates**（`templates/prompts/` 中的 12+ markdown 文件）
   - rd-generator.md、rd-reviewer.md
   - prd-generator.md、prd-reviewer.md
   - design-generator.md、design-reviewer.md
   - test-plan-generator.md、test-plan-reviewer.md
   - code-generator.md、code-reviewer.md
   - consistency-checker.md、impact-analyzer.md
   - 大项目变体（overview/module generators）

2. **Workflow Documentation**（`templates/workflows/` 中的 7 个 markdown 文件）
   - workflow-overview.md
   - workflow-rd.md、workflow-prd.md、workflow-design.md、workflow-test-plan.md
   - workflow-task-mgmt.md
   - workflow-large-project.md

3. **Helper Scripts**（`scripts/` 中的 5 个 Python 文件）
   - init_project.py
   - parse_tags.py
   - build_graph.py
   - impact_analysis.py
   - check_consistency.py

---

### **6.2 Next Steps**

**[ID: DESIGN-NEXT-001]**

1. ✅ **Write Test Plan**：所有组件的测试策略
2. ✅ **Implement Prompt Templates**：创建所有 .md 文件，附带详细 prompts
3. ✅ **Implement Workflow Docs**：编写分步指南
4. ✅ **Implement Python Scripts**：开发并测试所有 helper scripts
5. ✅ **Integration Testing**：端到端测试完整工作流

---

**Design Document Complete**
