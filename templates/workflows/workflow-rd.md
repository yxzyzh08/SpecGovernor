# Requirements Document (RD) Workflow

**[ID: WORKFLOW-RD-001] [Implements: DESIGN-WORKFLOW-STAGES-001]**

## Prerequisites

- ✅ 项目已初始化（运行了 `python scripts/init_project.py`）
- ✅ 已收集用户故事和业务需求
- ✅ Project Manager 已创建相关 Epic 并分配任务

## Role Perspective

切换到 **Requirements Analyst** 角色。

## Step-by-Step Process

### Step 1: Review Epic and Gather Requirements

1. 打开 `.specgov/tasks/rd-analyst.md` 查看分配的任务
2. 从 `.specgov/tasks/project-manager.md` 查看相关 Epic
3. 收集以下信息：
   - 用户故事（As [用户类型], I want [目标], so that [收益]）
   - 业务需求和痛点
   - 利益相关者的期望
   - 项目约束（如有）

**Example:**
```markdown
Epic: 用户身份验证系统

用户故事：
- As a new user, I want to log in with my Google account, so that I don't need to create a new password
- As a user, I want my session to persist for 24 hours, so that I don't need to log in frequently
- As an admin, I want to view all login activities, so that I can monitor security

业务需求：
- 降低用户注册门槛
- 提高安全性
- 支持主流 OAuth2 提供商
```

### Step 2: Open Claude Code and Load RD Generator Prompt

1. 打开 Claude Code
2. 加载 `.specgov/prompts/rd-generator.md`

### Step 3: Provide Input to Claude Code

向 Claude Code 提供以下输入：

**输入：**
```
请生成 Requirements Document (RD)。

项目上下文：
- 项目名称：[项目名称]
- 项目规模：小项目（< 10 万行代码）
- 目标用户：[描述目标用户]

用户故事：
[粘贴步骤 1 收集的用户故事]

业务需求：
[粘贴步骤 1 收集的业务需求]

技术约束：
- 操作系统：Windows 10/11
- Shell 环境：PowerShell 5.1+
- Python 版本：Python 3.8+
- AI 助手：Claude Code
- 版本控制：Git
```

### Step 4: Generate Requirements Document

Claude Code 将生成 RD.md，包含：
- 清晰的需求类别（## 标题）
- 具体需求（### 标题）
- 每个需求都有 `[ID: RD-REQ-XXX]` 标记
- 分层需求使用 `[Decomposes: RD-CATEGORY-XXX]`
- 每个需求都有验收标准

保存输出到 `docs/RD.md`。

**Example Output:**
```markdown
# Requirements Document (RD)

> **Version**: 1.0
> **Created**: 2025-11-16
> **Updated**: 2025-11-16

## 1. User Authentication Requirements
**[ID: RD-AUTH-001]**

本节定义所有身份验证和授权需求。系统必须支持多种身份验证方式，确保用户数据安全，同时提供便捷的登录体验。

### 1.1 OAuth2 Login Support
**[ID: RD-REQ-005] [Decomposes: RD-AUTH-001]**

系统必须支持通过 OAuth2 协议进行用户身份验证，允许用户使用其现有社交媒体账户登录，而无需创建新密码。

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
```

### Step 5: Review Requirements Document

1. 切换视角（可以保持 Requirements Analyst 或切换到另一个角色以保持独立性）
2. 在 Claude Code 中加载 `.specgov/prompts/rd-reviewer.md`
3. 提供 `docs/RD.md` 完整内容进行审查
4. Claude Code 输出审查报告

**Example Input to Reviewer:**
```
请审查以下 Requirements Document (RD)：

[粘贴 docs/RD.md 完整内容]

项目上下文：
- 项目规模：小项目
```

### Step 6: Address Review Feedback

如果审查识别出问题：

1. 再次加载 `.specgov/prompts/rd-generator.md`
2. 提供以下输入：
   ```
   请修改现有 Requirements Document (RD)。

   现有 RD.md 内容：
   [粘贴 docs/RD.md]

   审查反馈：
   [粘贴审查报告中的关键问题和重要问题]

   请根据审查反馈修改 RD.md。
   ```
3. Claude Code 修改文档
4. 如需要，重复审查（步骤 5）

### Step 7: Update Task Documents

1. 打开 `.specgov/tasks/rd-analyst.md`
2. 将 RD 生成任务标记为完成：
   ```markdown
   ## Completed Tasks
   - ✅ 生成 RD.md v1.0 - 定义用户身份验证需求
   ```
3. 切换到 Project Manager 视角
4. 打开 `.specgov/tasks/project-manager.md`
5. 更新 Epic 进度：
   ```markdown
   ## Active Epics

   ### Epic 1: 用户身份验证系统
   - 进度：20% → 40%
   - ✅ RD.md 完成
   - ⏳ PRD.md 待生成
   - ⏳ Design Document 待生成
   ```
6. 提交到 Git：
   ```powershell
   git add docs/RD.md .specgov/tasks/
   git commit -m "Add user authentication requirements to RD.md"
   ```

### Step 8: Run Helper Scripts (Optional but Recommended)

1. 解析标记：
   ```powershell
   python scripts/parse_tags.py
   ```
2. 构建依赖图谱：
   ```powershell
   python scripts/build_graph.py
   ```

## Common Pitfalls

- ❌ 忘记添加 `[ID: RD-XXX]` 标记
- ❌ 使用模糊的需求描述（如 "系统应该快"）
- ❌ 验收标准不可测试（如 "用户体验良好"）
- ❌ 遗漏 `[Decomposes: XXX]` 标记导致需求层级关系丢失
- ❌ 留下占位符或 TODOs
- ❌ 混淆需求和设计（RD 定义"什么"，不是"如何"）
- ❌ 跳过审查步骤

## Validation Checklist

进入 PRD 阶段前，验证：

- [ ] 所有主要需求类别都有 `[ID: RD-CATEGORY-XXX]` 标记
- [ ] 所有具体需求都有 `[ID: RD-REQ-XXX]` 标记
- [ ] 分层需求使用 `[Decomposes: XXX]` 链接到父级
- [ ] 所有需求都有清晰、可测试的验收标准
- [ ] 无占位符或 TODOs
- [ ] 审查已完成并处理反馈
- [ ] 任务文档已更新（rd-analyst.md + project-manager.md）
- [ ] 变更已提交到 Git
- [ ] Helper scripts 已运行（parse_tags.py + build_graph.py）

## Quick Reference Commands

```powershell
# 初始化项目（首次）
python scripts/init_project.py

# 解析标记并构建图谱
python scripts/parse_tags.py
python scripts/build_graph.py

# 提交到 Git
git add docs/RD.md .specgov/tasks/
git commit -m "Add requirements to RD.md"
```

## Next Steps

✅ RD.md 完成后，进入下一阶段：
- 查看 [PRD Workflow](workflow-prd.md)
- 切换到 Product Manager 角色
- 加载 `prd-generator.md` 生成 PRD.md

---

**Estimated Time**: 2-4 hours (depending on project complexity)
**Estimated Cost**: $2-5 (Claude Code usage for generation + review)
