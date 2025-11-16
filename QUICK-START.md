# SpecGovernor 快速开始指南

5 分钟快速上手 SpecGovernor！

---

## 🎯 目标

完成本指南后，您将：
- ✅ 创建第一个 Epic
- ✅ 生成第一个 RD（Requirements Document）
- ✅ 理解基本工作流程
- ✅ 运行 Helper Scripts

**预计时间**: 5-10 分钟

---

## 📋 前提条件

- ✅ 已完成 SpecGovernor 安装（参见 [INSTALLATION.md](INSTALLATION.md)）
- ✅ 项目目录包含 `.specgov/` 文件夹
- ✅ 已安装 Claude Code

---

## 第1步: 创建您的第一个 Epic

### 1.1 打开 Project Manager 任务文件

```powershell
# 使用 VS Code 打开任务文件
code .specgov/tasks/project-manager.md
```

### 1.2 定义 Epic

在文件中添加以下内容：

```markdown
# Project Manager Tasks

## Active Epics

### Epic 1: 用户身份验证系统
- **目标**：实现一个安全、便捷的用户身份验证系统，支持 OAuth2 社交登录
- **进度**：0%
- **状态**：进行中
- **子任务**：
  - ⬜ RD.md（需求分析）
  - ⬜ PRD.md（产品规划）
  - ⬜ Design-Document.md（技术设计）
  - ⬜ Test-Plan.md（测试规划）
  - ⬜ 代码实现
- **预估时间**：20-30 小时
- **预估成本**：$15-25（Claude Code 使用）
```

### 1.3 保存文件

```powershell
# 提交到 Git（推荐）
git add .specgov/tasks/project-manager.md
git commit -m "Create Epic 1: User Authentication System"
```

---

## 第2步: 生成需求文档（RD）

### 2.1 切换到 Requirements Analyst 角色

打开 `.specgov/tasks/rd-analyst.md`，添加任务：

```markdown
# Requirements Analyst Tasks

## Active Tasks

### Task 1: 生成用户身份验证需求文档
- **Epic**：Epic 1 - 用户身份验证系统
- **状态**：进行中
- **预估时间**：3 小时
- **输出**：docs/RD.md
```

### 2.2 在 Claude Code 中加载 RD Generator Prompt

打开 Claude Code，输入以下内容：

```
请加载 .specgov/prompts/rd-generator.md 文件的内容。

然后，请生成 Requirements Document (RD)。

项目上下文：
- 项目名称：我的项目
- 项目规模：小项目（< 10 万行代码）
- 目标用户：Web 应用的终端用户

用户故事：
- As a new user, I want to register with my email, so that I can create an account
- As a new user, I want to log in with my Google account, so that I don't need to create a new password
- As a user, I want my session to persist for 24 hours, so that I don't need to log in frequently
- As an admin, I want to view all login activities, so that I can monitor security

业务需求：
- 降低用户注册门槛（支持社交媒体登录）
- 提高安全性（密码加密、账户锁定保护）
- 支持主流 OAuth2 提供商（Google、GitHub、Microsoft）

技术约束：
- 操作系统：Windows / Linux / macOS
- Shell 环境：PowerShell 5.1+ / Bash 4.0+
- Python 版本：Python 3.8+
- AI 助手：Claude Code
- 版本控制：Git
```

### 2.3 Claude Code 生成 RD

Claude Code 将生成 RD.md 内容。将输出保存到 `docs/RD.md`。

**示例输出片段**:

```markdown
# Requirements Document (RD)

> **Version**: 1.0
> **Created**: 2025-11-16

## 1. User Authentication Requirements
**[ID: RD-AUTH-001]**

本节定义所有身份验证和授权需求。

### 1.1 Email Registration
**[ID: RD-REQ-001] [Decomposes: RD-AUTH-001]**

系统必须支持用户使用邮箱和密码注册账户。

**验收标准：**
- ✅ 用户可以使用邮箱和密码注册
- ✅ 邮箱必须唯一
- ✅ 密码必须至少 8 个字符，包含大小写字母和数字
- ✅ 注册成功后发送邮箱验证链接

### 1.2 OAuth2 Login Support
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
```

### 2.4 保存 RD 到文件

```powershell
# 将 Claude Code 输出保存到 docs/RD.md
# 然后提交到 Git
git add docs/RD.md
git commit -m "Add user authentication requirements to RD.md"
```

---

## 第3步: 审查需求文档

### 3.1 在 Claude Code 中加载 RD Reviewer Prompt

```
请加载 .specgov/prompts/rd-reviewer.md 文件的内容。

请审查以下 Requirements Document (RD)：

[粘贴 docs/RD.md 完整内容]

项目上下文：
- 项目规模：小项目
```

### 3.2 Claude Code 输出审查报告

Claude Code 将输出审查报告，标识问题（如果有）：

**示例输出**:

```markdown
# RD Review Report

## Summary
- **Overall Quality**: Good
- **Critical Issues**: 0
- **Important Issues**: 2
- **Suggestions**: 3

## Important Issues

### 1. [重要-可追溯性] 缺少分层标记
- **位置**: RD-REQ-001
- **问题**: 没有 [Decomposes: RD-AUTH-001] 标记
- **建议**: 添加 [Decomposes: RD-AUTH-001]
```

### 3.3 根据审查报告修改 RD

如果有问题，再次使用 RD Generator 修改文档：

```
请加载 .specgov/prompts/rd-generator.md

请修改现有 Requirements Document (RD)。

现有 RD.md 内容：
[粘贴 docs/RD.md]

审查反馈：
[粘贴审查报告中的关键问题和重要问题]

请根据审查反馈修改 RD.md。
```

---

## 第4步: 运行 Helper Scripts

### 4.1 解析可追溯性标记

```powershell
# 解析 RD.md 中的标记
python scripts/parse_tags.py
```

**输出示例**:
```
Parsing docs/RD.md...
Found 5 tags:
- RD-AUTH-001
- RD-REQ-001
- RD-REQ-005
...

Tags saved to .specgov/index/tags.json
```

### 4.2 构建依赖图谱

```powershell
# 构建依赖图谱
python scripts/build_graph.py
```

**输出示例**:
```
Building dependency graph...
Nodes: 5
Edges: 4

Dependency graph saved to .specgov/index/dependency-graph.json
```

### 4.3 查看依赖图谱

```powershell
# 查看生成的图谱
type .specgov/index/dependency-graph.json
```

**示例内容**:
```json
{
  "nodes": [
    {"id": "RD-AUTH-001", "type": "RD", "label": "User Authentication Requirements"},
    {"id": "RD-REQ-001", "type": "RD", "label": "Email Registration"},
    {"id": "RD-REQ-005", "type": "RD", "label": "OAuth2 Login Support"}
  ],
  "edges": [
    {"from": "RD-REQ-001", "to": "RD-AUTH-001", "type": "decomposes"},
    {"from": "RD-REQ-005", "to": "RD-AUTH-001", "type": "decomposes"}
  ]
}
```

---

## 第5步: 更新任务状态

### 5.1 标记 RD 任务完成

编辑 `.specgov/tasks/rd-analyst.md`:

```markdown
## Completed Tasks
- ✅ 生成 RD.md v1.0 - 定义用户身份验证需求（2025-11-16完成）
```

### 5.2 更新 Epic 进度

编辑 `.specgov/tasks/project-manager.md`:

```markdown
### Epic 1: 用户身份验证系统
- **进度**：0% → 20%
- **状态**：进行中
- **子任务**：
  - ✅ RD.md（需求分析）- 完成于 2025-11-16
  - ⏳ PRD.md（产品规划）- 待开始
  - ⬜ Design-Document.md（技术设计）
  - ⬜ Test-Plan.md（测试规划）
  - ⬜ 代码实现
```

### 5.3 提交更改

```powershell
# 提交所有更改
git add .specgov/tasks/
git commit -m "Update task status: RD generation completed"
```

---

## 🎉 恭喜！

您已完成 SpecGovernor 快速开始教程！

### 您已经学会了：

- ✅ 创建和管理 Epic
- ✅ 使用 Prompt 模板生成文档（RD）
- ✅ 使用 Reviewer 审查文档质量
- ✅ 运行 Helper Scripts 构建依赖图谱
- ✅ 更新任务状态和 Epic 进度

---

## 📚 下一步

### 继续 SDLC 流程

按照以下顺序继续：

1. **生成 PRD（Product Requirements Document）**
   - 查看: `.specgov/workflows/workflow-prd.md`
   - 使用: `prd-generator.md` + `prd-reviewer.md`

2. **生成 Design Document**
   - 查看: `.specgov/workflows/workflow-design.md`
   - 使用: `design-generator.md` + `design-reviewer.md`

3. **生成 Test Plan**
   - 查看: `.specgov/workflows/workflow-test-plan.md`
   - 使用: `test-plan-generator.md` + `test-plan-reviewer.md`

4. **生成代码**
   - 使用: `code-generator.md` + `code-reviewer.md`

### 深入学习

- **完整工作流**: 阅读 `.specgov/workflows/workflow-overview.md`
- **任务管理**: 阅读 `.specgov/workflows/workflow-task-mgmt.md`
- **大项目**: 阅读 `.specgov/workflows/workflow-large-project.md`（如果项目 ≥ 10 万行代码）

### 使用 Helper Scripts

- **影响分析**: 修改 RD 后运行 `python scripts/impact_analysis.py --changed=docs/RD.md`
- **一致性检查**: 运行 `python scripts/check_consistency.py --scope=RD-REQ-005`

---

## 💡 提示和最佳实践

1. **定期运行 Helper Scripts**: 每次修改文档后运行 `parse_tags.py` 和 `build_graph.py`
2. **使用 Git 追踪变更**: 所有文档和任务文件都应该提交到 Git
3. **保持任务状态最新**: 及时更新 `.specgov/tasks/` 中的任务状态
4. **遵循工作流**: 参考 `.specgov/workflows/` 中的工作流文档
5. **双重质量保证**: 始终使用 Generator + Reviewer 模式

---

## ❓ 常见问题

### Q1: 我可以跳过某个阶段吗？

**A**: 不推荐。完整的 SDLC 流程确保需求到代码的完整可追溯性。如果跳过某个阶段（如 PRD），后续阶段的文档将缺少上游链接。

### Q2: 我可以同时进行多个 Epic 吗？

**A**: 可以。但建议一次专注于一个 Epic，确保质量。在 `.specgov/tasks/project-manager.md` 中可以定义多个 Epic。

### Q3: 如何处理大项目？

**A**: 对于 ≥ 10 万行代码的大项目，使用大项目变体模板：
- `rd-overview-generator.md` + `rd-module-generator.md`
- `prd-overview-generator.md` + `prd-module-generator.md`
- `design-overview-generator.md` + `design-module-generator.md`
- `test-plan-overview-generator.md` + `test-plan-module-generator.md`

详见 `.specgov/workflows/workflow-large-project.md`

### Q4: Helper Scripts 运行失败怎么办？

**A**: 检查以下几点：
- Python 版本是否 ≥ 3.8
- 文档中的标记格式是否正确（如 `[ID: RD-REQ-001]`）
- `.specgov/index/` 目录是否存在
- 查看错误消息，根据提示修复

---

## 📞 获取帮助

- **工作流文档**: 查看 `.specgov/workflows/` 中的相关文档
- **GitHub Issues**: https://github.com/yourname/SpecGovernor/issues
- **完整文档**: [README.md](README.md), [INSTALLATION.md](INSTALLATION.md)

---

**🚀 开始您的 SpecGovernor 之旅！**
