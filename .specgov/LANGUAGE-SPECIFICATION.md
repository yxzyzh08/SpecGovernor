# 语言规范 (Language Specification)

## 统一语言原则

**所有 SpecGovernor 生成的文档必须遵循以下语言规范：**

### 1. 文件名 (File Names)
- ✅ **必须使用英文**
- ✅ 使用完整名称，禁止缩写
- ✅ 示例：`PRD.md`, `Design-Document.md`, `Test-Plan.md`
- ❌ 错误：`DD.md`, `TD.md`, `需求文档.md`

### 2. 文档标题 (Headings)
- ✅ **必须使用英文**
- ✅ 使用标准化的英文标题
- ✅ 示例：
  - `## Product Overview`
  - `## Feature Requirements`
  - `## Acceptance Criteria`
  - `## API Design`
  - `## Test Cases`
- ❌ 错误：`## 产品概述`, `## 功能需求`

### 3. 专业术语 (Technical Terms)
- ✅ **必须使用英文**
- ✅ 技术术语、框架名称、工具名称保持英文
- ✅ 示例：OAuth2, API, Database, NestJS, PostgreSQL, Claude Code
- ❌ 错误：应用程序接口（应使用 API）

### 4. 文档描述和正文 (Content/Description)
- ✅ **必须使用中文**
- ✅ 所有说明、描述、解释使用中文
- ✅ 用户故事、验收标准、测试步骤使用中文
- ✅ 示例：
  ```markdown
  ## Product Overview

  本产品是一个为超级个体设计的软件开发流程管理工具包...

  ## User Authentication Feature
  **[ID: PRD-FEAT-012]**

  ### User Story
  > **As** 新用户
  > **I want** 使用我的 Google/GitHub 账号登录
  > **So that** 我不需要创建和记住新密码

  ### Acceptance Criteria
  - ✅ 显示 OAuth2 登录按钮（Google、GitHub、Microsoft）
  - ✅ 授权后自动登录并获取用户信息
  ```

### 5. 代码和命令 (Code & Commands)
- ✅ **代码、命令、路径使用英文**
- ✅ 变量名、函数名、类名使用英文
- ✅ 注释可以使用中文
- ✅ 示例：
  ```typescript
  /**
   * OAuth2 认证服务
   * [ID: CODE-API-008] [Implements: DESIGN-API-008]
   */
  export class OAuth2Service {
      async authenticate(provider: string): Promise<User> {
          // 调用第三方 OAuth2 提供商
          return await this.callProvider(provider);
      }
  }
  ```

### 6. 表格 (Tables)
- ✅ **表头使用英文**
- ✅ **表格内容使用中文**
- ✅ 示例：
  ```markdown
  | Feature | Description | Priority |
  |:--------|:-----------|:---------|
  | OAuth2 Login | 用户使用第三方账号登录 | High |
  | Email Verification | 验证用户邮箱地址 | Medium |
  ```

### 7. Glossary/术语表
- ✅ **术语/缩略语列使用英文**
- ✅ **英文全称列使用英文**
- ✅ **解释说明列使用中文**
- ✅ 示例：
  ```markdown
  | 术语/缩略语 | 英文全称 | 解释说明 |
  |:-----------|:--------|:--------|
  | **API** | Application Programming Interface | 应用程序编程接口 |
  | **OAuth2** | OAuth 2.0 | 开放授权协议第二版 |
  ```

---

## 完整示例

### PRD 示例

```markdown
# Product Requirements Document (PRD)

> **Version**: 1.0
> **Created**: 2025-11-18

## Terminology and Glossary

**[ID: PRD-GLOSSARY-001]**

| 术语/缩略语 | 英文全称 | 解释说明 |
|:-----------|:--------|:--------|
| **API** | Application Programming Interface | 应用程序编程接口 |
| **OAuth2** | OAuth 2.0 | 开放授权协议第二版 |

---

## Product Overview

本产品是一个现代化的用户认证系统，支持多种第三方登录方式。

### Target Users
- 企业用户：需要快速集成认证功能的开发团队
- 个人开发者：希望为自己的应用添加社交登录功能

---

## Authentication Features

### OAuth2 Social Login
**[ID: PRD-FEAT-012]** [Raw-Req: Entry-003]

#### User Story
> **As** 新用户
> **I want** 使用我的 Google/GitHub/Microsoft 账号登录
> **So that** 我不需要创建和记住新密码

#### Acceptance Criteria
- ✅ 显示 OAuth2 登录按钮（Google、GitHub、Microsoft）
- ✅ 点击按钮后跳转到对应的授权页面
- ✅ 授权成功后自动登录并获取用户信息
- ✅ 授权失败时显示清晰的错误消息

#### Technical Constraints
- 使用标准的 OAuth 2.0 协议
- 支持 PKCE (Proof Key for Code Exchange) 增强安全性
```

---

## 检查清单

生成文档前，请确认：

- [ ] 文件名使用英文（如 `PRD.md`, `Design-Document.md`）
- [ ] 所有章节标题使用英文（如 `## Product Overview`, `## Acceptance Criteria`）
- [ ] 专业术语保持英文（如 OAuth2, API, Database）
- [ ] 文档描述和正文使用中文
- [ ] 表头使用英文，表格内容使用中文
- [ ] 代码、变量名、函数名使用英文
- [ ] 注释可以使用中文帮助理解

---

**遵循此规范可确保文档的专业性、一致性和可读性。**
