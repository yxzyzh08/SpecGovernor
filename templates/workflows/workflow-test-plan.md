# Test Plan Workflow

**[ID: WORKFLOW-TEST-001] [Implements: DESIGN-WORKFLOW-STAGES-001]**

## Prerequisites

- ✅ Design-Document.md 已完成并审查
- ✅ PRD.md 可供参考
- ✅ 已识别测试环境（操作系统、浏览器、数据库等）
- ✅ Project Manager 已分配 Test Plan 生成任务

## Role Perspective

切换到 **Test Manager** 角色。

## Step-by-Step Process

### Step 1: Review Design Document and Define Test Environment

1. 打开 `.specgov/tasks/test-manager.md` 查看分配的任务
2. 仔细阅读 `docs/Design-Document.md`，识别所有需要测试的功能
3. 定义测试环境：

**Example:**
```markdown
测试环境：
- 操作系统：Windows 10/11
- 浏览器：Chrome、Firefox、Edge（如有 UI）
- 数据库：PostgreSQL 15（本地测试环境）
- 第三方服务：
  - OAuth2 提供商：使用 Mock（单元测试）或实际服务（集成测试）
- 测试工具：
  - 单元测试：pytest（Python）
  - 集成测试：pytest + requests
  - 性能测试：k6 或 JMeter
```

### Step 2: Open Claude Code and Load Test Plan Generator Prompt

1. 打开 Claude Code
2. 加载 `.specgov/prompts/test-plan-generator.md`

### Step 3: Provide Context to Claude Code

向 Claude Code 提供以下输入：

**输入：**
```
请生成 Test Plan。

Design-Document.md 内容：
[粘贴 docs/Design-Document.md 完整内容]

PRD.md 内容（供参考）：
[粘贴 docs/PRD.md 完整内容]

测试环境：
- 操作系统：Windows 10/11
- 浏览器：Chrome、Firefox、Edge
- 数据库：PostgreSQL 15
- 第三方服务：OAuth2 提供商（使用 Mock 或实际服务）
- 测试工具：pytest、k6

项目上下文：
- 项目规模：小项目
- 测试优先级：功能 > 安全 > 性能
```

**重要**：始终使用 "Test Plan"，不要使用 "TD"！

### Step 4: Generate Test Plan

Claude Code 将生成 Test-Plan.md，包含：
- Test Strategy（测试策略概述）
- 详细测试用例，包含：
  - 前置条件
  - 测试步骤
  - 预期结果
  - 测试数据（如适用）
- `[Tests-for: DESIGN-XXX]` 或 `[Tests-for: PRD-XXX]` 链接
- Test Coverage Matrix（可选但推荐）

保存输出到 `docs/Test-Plan.md`。

**Example Output:**
```markdown
# Test Plan

> **Version**: 1.0
> **Based on**: Design-Document.md (v1.0), PRD.md (v1.0)
> **Created**: 2025-11-16

## 1. Test Strategy

### 1.1 Test Scope
**包含的功能：**
- OAuth2 社交登录（Google、GitHub、Microsoft）
- 用户会话管理
- 用户个人资料管理

**不包含的功能：**
- 第三方 OAuth2 提供商的内部实现（外部依赖）

### 1.2 Test Types
- **Unit Tests**：测试单个函数/方法
- **Integration Tests**：测试 API 端点和数据库交互
- **API Tests**：测试 API 端点的各种场景
- **Security Tests**：测试安全漏洞（SQL 注入、XSS 等）
- **Performance Tests**：测试响应时间和并发处理

### 1.3 Test Environment
- 操作系统：Windows 10/11
- 数据库：PostgreSQL 15（本地测试数据库）
- 第三方服务：OAuth2 提供商（使用 Mock 或测试账户）

## 5. Authentication API Tests

### 5.1 OAuth2 Callback Endpoint Tests
**[ID: TEST-CASE-015] [Tests-for: DESIGN-API-008]**

测试 OAuth2 回调端点的各种场景，包括成功登录、授权失败、无效提供商等。

#### Test Case: Successful Google OAuth2 Login
**[ID: TEST-CASE-015-001]**

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
2. 验证响应状态码为 200
3. 验证响应 body 包含 `access_token` 字段
4. 验证响应 body 包含 `user` 对象

**预期结果：**
- ✅ 状态码：200 OK
- ✅ `access_token`：有效的 JWT
- ✅ `user.email`：匹配 Google 账户邮箱
```

### Step 5: Review Test Plan

1. 切换视角（可以保持 Test Manager 或切换到另一个角色）
2. 在 Claude Code 中加载 `.specgov/prompts/test-plan-reviewer.md`
3. 提供以下输入：
   ```
   请审查以下 Test Plan：

   Test-Plan.md 内容：
   [粘贴 docs/Test-Plan.md 完整内容]

   Design-Document.md 内容（用于验证可追溯性）：
   [粘贴 docs/Design-Document.md 完整内容]

   PRD.md 内容（用于验证覆盖度）：
   [粘贴 docs/PRD.md 完整内容]
   ```
4. Claude Code 输出审查报告

### Step 6: Address Review Feedback

如果审查识别出问题：

1. 再次加载 `.specgov/prompts/test-plan-generator.md`
2. 提供以下输入：
   ```
   请修改现有 Test Plan。

   Design-Document.md 内容：
   [粘贴 docs/Design-Document.md]

   现有 Test-Plan.md 内容：
   [粘贴 docs/Test-Plan.md]

   审查反馈：
   [粘贴审查报告中的关键问题和重要问题]

   请根据审查反馈修改 Test-Plan.md。
   ```
3. Claude Code 修改文档
4. 如需要，重复审查

### Step 7: Verify Test Coverage

运行 helper scripts 验证覆盖度：

```powershell
# 解析标记
python scripts/parse_tags.py

# 构建依赖图谱
python scripts/build_graph.py

# 检查一致性
python scripts/check_consistency.py --scope DESIGN-API-008
```

**验证要点：**
- 所有设计功能都有测试用例
- 测试用例覆盖正常流程、错误处理、边缘情况
- 测试用例链接到设计（`[Tests-for: DESIGN-XXX]`）

### Step 8: Update Task Documents

1. 打开 `.specgov/tasks/test-manager.md`
2. 将 Test Plan 生成任务标记为完成：
   ```markdown
   ## Completed Tasks
   - ✅ 生成 Test-Plan.md v1.0 - 定义身份验证系统测试策略
   - ✅ 审查 Test Plan，处理反馈

   ## Test Coverage Summary
   - API Tests：15 个测试用例
   - Security Tests：5 个测试用例
   - Performance Tests：3 个测试用例
   - 总计：23 个测试用例
   ```
3. 切换到 Project Manager 视角
4. 打开 `.specgov/tasks/project-manager.md`
5. 更新 Epic 进度：
   ```markdown
   ## Active Epics

   ### Epic 1: 用户身份验证系统
   - 进度：80% → 90%
   - ✅ RD.md 完成
   - ✅ PRD.md 完成
   - ✅ Design Document 完成
   - ✅ Test Plan 完成
   - ⏳ 代码实现待开始
   ```
6. 提交到 Git：
   ```powershell
   git add docs/Test-Plan.md .specgov/tasks/
   git commit -m "Add authentication system test plan to Test-Plan.md"
   ```

## Common Pitfalls

- ❌ 使用 "TD" 而不是 "Test Plan"
- ❌ 忘记添加 `[Tests-for: XXX]` 标记
- ❌ 测试步骤过于抽象，不可操作
- ❌ 预期结果模糊，不可验证
- ❌ 只测试正常流程，忽略错误处理
- ❌ 缺少性能测试或安全测试
- ❌ 前置条件不清晰
- ❌ 缺少测试数据说明
- ❌ 设计功能未被测试用例覆盖

## Validation Checklist

进入代码实现阶段前，验证：

- [ ] 所有测试用例都有 `[ID: TEST-CASE-XXX]` 标记
- [ ] 所有测试用例都通过 `[Tests-for: XXX]` 链接到设计或 PRD
- [ ] 设计中的所有功能都有测试用例（测试覆盖率 100%）
- [ ] 测试用例包含前置条件、步骤、预期结果
- [ ] 测试步骤具体且可操作
- [ ] 预期结果可验证且使用 ✅ 符号
- [ ] 覆盖正常流程、错误处理、边缘情况
- [ ] 包含性能测试和安全测试
- [ ] Test Strategy 部分已填写
- [ ] 始终使用 "Test Plan" 术语（不是 "TD"）
- [ ] 审查已完成并处理反馈
- [ ] 任务文档已更新（test-manager.md + project-manager.md）
- [ ] 变更已提交到 Git
- [ ] Helper scripts 已运行，依赖图谱已更新

## Quick Reference Commands

```powershell
# 解析标记并构建图谱
python scripts/parse_tags.py
python scripts/build_graph.py

# 检查一致性
python scripts/check_consistency.py --scope DESIGN-API-008

# 提交到 Git
git add docs/Test-Plan.md .specgov/tasks/
git commit -m "Add test plan to Test-Plan.md"
```

## Next Steps

✅ Test-Plan.md 完成后，进入下一阶段：
- 切换到 Developer 角色
- 加载 `code-generator.md` 生成代码
- 开始实现系统

**后续开发流程：**
1. 实现代码（使用 `code-generator.md`）
2. 审查代码（使用 `code-reviewer.md`）
3. 运行单元测试
4. 运行集成测试
5. 修复发现的问题
6. 重复直到所有测试通过

---

**Estimated Time**: 2-4 hours (depending on test complexity)
**Estimated Cost**: $2-5 (Claude Code usage for generation + review)
