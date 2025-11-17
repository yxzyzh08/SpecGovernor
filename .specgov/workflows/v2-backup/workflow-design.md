# Design Document Workflow

**[ID: WORKFLOW-DESIGN-001] [Implements: DESIGN-WORKFLOW-STAGES-001]**

## Prerequisites

- ✅ PRD.md 已完成并审查
- ✅ RD.md 可供参考
- ✅ 已识别技术约束（语言、框架、云等）
- ✅ Project Manager 已分配 Design Document 生成任务

## Role Perspective

切换到 **Architect** 角色。

## Step-by-Step Process

### Step 1: Review PRD and Technical Constraints

1. 打开 `.specgov/tasks/architect.md` 查看分配的任务
2. 仔细阅读 `docs/PRD.md`，识别所有需要技术设计的功能
3. 列出技术约束：

**Example:**
```markdown
技术约束：
- 编程语言：Python 3.11
- 框架：FastAPI
- 数据库：PostgreSQL 15
- 部署：AWS Lambda + RDS
- 身份验证：JWT
- ORM：SQLAlchemy
- 其他：
  - 必须支持 Windows 10/11
  - 响应时间 < 200ms（P95）
  - 支持 10,000 并发用户
```

### Step 2: Open Claude Code and Load Design Generator Prompt

1. 打开 Claude Code
2. 加载 `.specgov/prompts/design-generator.md`

### Step 3: Provide Context to Claude Code

向 Claude Code 提供以下输入：

**输入：**
```
请生成 Design Document。

PRD.md 内容：
[粘贴 docs/PRD.md 完整内容]

RD.md 内容（供参考）：
[粘贴 docs/RD.md 完整内容]

技术约束：
- 编程语言：Python 3.11
- 框架：FastAPI
- 数据库：PostgreSQL 15
- 部署：AWS Lambda + RDS
- 身份验证：JWT
- ORM：SQLAlchemy
- 其他约束：
  - 必须支持 Windows 10/11
  - API 响应时间 < 200ms（P95）
  - 支持 10,000 并发用户

项目上下文：
- 项目规模：小项目
```

**重要**：始终使用 "Design Document"，不要使用 "DD"！

### Step 4: Generate Design Document

Claude Code 将生成 Design-Document.md，包含：
- Architecture Design（系统架构）
  - 组件图、数据流图
  - 技术栈选择和理由
- API Design（API 规范）
  - 端点定义、请求/响应格式
  - 错误处理、实现说明
- Database Design（数据库模式）
  - 表定义、字段、索引、关系
- Service Design（服务设计，如适用）
- Security Design（安全设计）
- `[Designs-for: PRD-FEAT-XXX]` 将每个设计链接到 PRD

保存输出到 `docs/Design-Document.md`。

**Example Output:**
```markdown
# Design Document

> **Version**: 1.0
> **Based on**: PRD.md (v1.0)
> **Created**: 2025-11-16

## 1. Architecture Design

### 1.1 Overall System Architecture
**[ID: DESIGN-ARCH-001] [Designs-for: PRD-FEAT-001]**

系统采用三层架构：API 层、Service 层、Data 层，部署在 AWS Lambda + RDS。

**Architecture Diagram:**
```
┌─────────────────────────────────────────┐
│      Client (Browser)                    │
└───────────────┬─────────────────────────┘
                │ HTTPS
                ▼
┌─────────────────────────────────────────┐
│      API Gateway (AWS)                   │
└───────────────┬─────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────┐
│    API Layer (AWS Lambda)                │
│  AuthController │ UserController         │
└───────────────┬─────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────┐
│      Service Layer                       │
│  OAuth2Service │ UserService │ JWTService│
└───────────────┬─────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────┐
│      Data Layer                          │
│  UserRepository │ OAuthRepository        │
└───────────────┬─────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────┐
│  Database (PostgreSQL on RDS)            │
│  users │ oauth_accounts                  │
└─────────────────────────────────────────┘
```

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

**Response (Success - 200 OK):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "def50200...",
  "expires_in": 3600,
  "user": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "john.doe@gmail.com",
    "name": "John Doe"
  }
}
```
```

### Step 5: Review Design Document

1. 切换视角（可以保持 Architect 或切换到另一个角色以保持独立性）
2. 在 Claude Code 中加载 `.specgov/prompts/design-reviewer.md`
3. 提供以下输入：
   ```
   请审查以下 Design Document：

   Design-Document.md 内容：
   [粘贴 docs/Design-Document.md 完整内容]

   PRD.md 内容（用于验证可追溯性）：
   [粘贴 docs/PRD.md 完整内容]

   技术约束：
   [粘贴技术约束]
   ```
4. Claude Code 输出审查报告

### Step 6: Address Review Feedback

如果审查识别出问题：

1. 再次加载 `.specgov/prompts/design-generator.md`
2. 提供以下输入：
   ```
   请修改现有 Design Document。

   PRD.md 内容：
   [粘贴 docs/PRD.md]

   现有 Design-Document.md 内容：
   [粘贴 docs/Design-Document.md]

   审查反馈：
   [粘贴审查报告中的关键问题和重要问题]

   请根据审查反馈修改 Design-Document.md。
   ```
3. Claude Code 修改文档
4. 如需要，重复审查

### Step 7: Verify Traceability and Coverage

运行 helper scripts 验证：

```powershell
# 解析标记
python scripts/parse_tags.py

# 构建依赖图谱
python scripts/build_graph.py

# 检查一致性（可选）
python scripts/check_consistency.py --scope PRD-FEAT-012
```

**验证要点：**
- 所有 PRD 功能都有相应的设计
- 所有设计都链接到 PRD（`[Designs-for: PRD-XXX]`）
- 架构符合技术约束

### Step 8: Update Task Documents

1. 打开 `.specgov/tasks/architect.md`
2. 将 Design Document 生成任务标记为完成：
   ```markdown
   ## Completed Tasks
   - ✅ 生成 Design-Document.md v1.0 - 设计用户身份验证系统
   - ✅ 审查 Design Document，处理反馈

   ## Key Design Decisions
   - 选择 FastAPI：异步支持、高性能、类型安全
   - 选择 PostgreSQL：关系型数据、ACID 保证、成熟稳定
   - 选择 AWS Lambda：自动扩展、按使用付费、无服务器
   ```
3. 切换到 Project Manager 视角
4. 打开 `.specgov/tasks/project-manager.md`
5. 更新 Epic 进度：
   ```markdown
   ## Active Epics

   ### Epic 1: 用户身份验证系统
   - 进度：60% → 80%
   - ✅ RD.md 完成
   - ✅ PRD.md 完成
   - ✅ Design Document 完成
   - ⏳ Test Plan 待生成
   ```
6. 提交到 Git：
   ```powershell
   git add docs/Design-Document.md .specgov/tasks/
   git commit -m "Add authentication system design to Design-Document.md"
   ```

## Common Pitfalls

- ❌ 使用 "DD" 而不是 "Design Document"
- ❌ 忘记添加 `[Designs-for: PRD-XXX]` 标记
- ❌ API 规范缺少错误响应示例
- ❌ 数据库模式缺少索引或关系说明
- ❌ 架构设计过于抽象，缺少实现细节
- ❌ 设计未考虑部署约束（如 AWS Lambda 的限制）
- ❌ 安全设计缺失或不完整
- ❌ 技术栈选择没有理由说明
- ❌ PRD 功能未被设计覆盖

## Validation Checklist

进入 Test Plan 阶段前，验证：

- [ ] 所有设计都有 `[ID: DESIGN-XXX]` 标记（使用适当的前缀）
- [ ] 所有设计都通过 `[Designs-for: PRD-XXX]` 链接到 PRD
- [ ] PRD 中的所有功能都有相应的设计（设计覆盖率 100%）
- [ ] API 规范包含请求、成功响应、错误响应和实现说明
- [ ] 数据库模式显示所有字段、类型、约束、索引、关系
- [ ] 架构设计包含组件图和数据流图
- [ ] 技术栈选择有理由说明
- [ ] 安全设计覆盖认证、授权、加密
- [ ] 始终使用 "Design Document" 术语（不是 "DD"）
- [ ] 审查已完成并处理反馈
- [ ] 任务文档已更新（architect.md + project-manager.md）
- [ ] 变更已提交到 Git
- [ ] Helper scripts 已运行，依赖图谱已更新

## Quick Reference Commands

```powershell
# 解析标记并构建图谱
python scripts/parse_tags.py
python scripts/build_graph.py

# 检查一致性
python scripts/check_consistency.py --scope PRD-FEAT-012

# 提交到 Git
git add docs/Design-Document.md .specgov/tasks/
git commit -m "Add system design to Design-Document.md"
```

## Next Steps

✅ Design-Document.md 完成后，进入下一阶段：
- 查看 [Test Plan Workflow](workflow-test-plan.md)
- 切换到 Test Manager 角色
- 加载 `test-plan-generator.md` 生成 Test-Plan.md

---

**Estimated Time**: 3-6 hours (depending on system complexity)
**Estimated Cost**: $3-8 (Claude Code usage for generation + review)
