# Product Requirements Document (PRD) Workflow

**[ID: WORKFLOW-PRD-001] [Implements: DESIGN-WORKFLOW-STAGES-001]**

## Prerequisites

- ✅ PRD.md 已完成并审查
- ✅ 已定义产品愿景和目标用户
- ✅ Project Manager 已分配 PRD 生成任务

## Role Perspective

切换到 **Product Manager** 角色。

## Step-by-Step Process

### Step 1: Review RD and Define Product Vision

1. 打开 `.specgov/tasks/product-manager.md` 查看分配的任务
2. 仔细阅读 `docs/PRD.md`，理解所有需求
3. 定义产品愿景：
   - 产品目标
   - 目标用户群体
   - 核心价值主张
   - 竞争优势

**Example:**
```markdown
产品愿景：
- 目标：构建一个安全、便捷的用户身份验证系统
- 目标用户：Web 应用的终端用户（新用户、注册用户）
- 核心价值：
  - 快速登录（使用现有社交媒体账户）
  - 安全可靠（OAuth2 标准）
  - 无需记住密码
- 竞争优势：支持多提供商、多账户关联
```

### Step 2: Open Claude Code and Load PRD Generator Prompt

1. 打开 Claude Code
2. 加载 `.specgov/prompts/prd-generator.md`

### Step 3: Provide Context to Claude Code

向 Claude Code 提供以下输入：

**输入：**
```
请生成 Product Requirements Document (PRD)。

PRD.md 内容：
[粘贴 docs/PRD.md 完整内容]

产品愿景：
[粘贴步骤 1 定义的产品愿景]

项目上下文：
- 项目规模：小项目
- 目标用户：Web 应用的终端用户

用户画像（如有）：
- 新用户：首次访问应用，希望快速注册
- 注册用户：已有账户，希望便捷登录
- 管理员：需要监控和管理用户账户
```

### Step 4: Generate Product Requirements Document

Claude Code 将生成 PPRD.md，包含：
- Product Overview
- 产品功能，带 `[ID: PRD-FEAT-XXX]`
- 用户故事，遵循 As/I want/So that 格式
- 验收标准（可测试、可衡量）
- `[Implements: PRD-REQ-XXX]` 将每个功能链接到需求
- UI/UX Notes（如适用）

保存输出到 `docs/PPRD.md`。

**Example Output:**
```markdown
# Product Requirements Document (PRD)

> **Version**: 1.0
> **Based on**: PRD.md (v1.0)
> **Created**: 2025-11-16

## 1. Product Overview

本产品是一个用户身份验证系统，允许用户使用其现有社交媒体账户（Google、GitHub、Microsoft）登录，而无需创建新密码。系统旨在提供安全、便捷的登录体验。

**目标用户：**
- 新用户：首次访问应用，希望快速注册
- 注册用户：已有账户，希望便捷登录

**核心价值：**
- 降低注册门槛（无需创建密码）
- 提高安全性（密码由第三方管理）
- 提升用户体验（快速登录）

## 2. Authentication Features

### 2.1 OAuth2 Social Login
**[ID: PRD-FEAT-012] [Implements: PRD-REQ-005]**

使用户能够使用其现有社交媒体账户登录，而无需创建新密码。支持 Google、GitHub 和 Microsoft 三种主流 OAuth2 提供商。

#### User Story
> **As** 新用户
> **I want** 使用我的 Google/GitHub/Microsoft 账户登录
> **So that** 我不需要创建和记住另一个密码

#### Acceptance Criteria
- ✅ 登录页面显示三个 OAuth2 登录按钮（Google、GitHub、Microsoft）
- ✅ 点击任一按钮，用户被重定向到相应提供商的授权页面
- ✅ 授权成功后，用户自动返回应用并登录
- ✅ 用户个人资料（姓名、邮箱、头像）自动填充到应用中
- ✅ 如果登录失败，用户看到清晰的错误消息
- ✅ 用户可以关联多个 OAuth2 账户到同一个应用账户

#### UI/UX Notes
- **登录按钮设计**：
  - 使用各提供商的官方品牌颜色和 logo
  - Google：白色背景，蓝色文字
  - GitHub：黑色背景，白色文字
  - Microsoft：蓝色背景，白色文字
- **错误处理**：
  - 授权失败时，在登录页面顶部显示红色错误提示条
```

### Step 5: Review Product Requirements Document

1. 切换视角（可以保持 Product Manager 或切换到另一个角色）
2. 在 Claude Code 中加载 `.specgov/prompts/prd-reviewer.md`
3. 提供以下输入：
   ```
   请审查以下 Product Requirements Document (PRD)：

   PPRD.md 内容：
   [粘贴 docs/PPRD.md 完整内容]

   PRD.md 内容（用于验证可追溯性）：
   [粘贴 docs/PRD.md 完整内容]

   项目上下文：
   - 项目规模：小项目
   ```
4. Claude Code 输出审查报告

### Step 6: Address Review Feedback

如果审查识别出问题：

1. 再次加载 `.specgov/prompts/prd-generator.md`
2. 提供以下输入：
   ```
   请修改现有 Product Requirements Document (PRD)。

   PRD.md 内容：
   [粘贴 docs/PRD.md]

   现有 PPRD.md 内容：
   [粘贴 docs/PPRD.md]

   审查反馈：
   [粘贴审查报告中的关键问题和重要问题]

   请根据审查反馈修改 PPRD.md。
   ```
3. Claude Code 修改文档
4. 如需要，重复审查

### Step 7: Verify Traceability

运行 helper scripts 验证可追溯性：

```powershell
# 解析标记
python scripts/parse_tags.py

# 构建依赖图谱
python scripts/build_graph.py

# 检查是否所有 RD 需求都被 PRD 覆盖
# （查看 dependency-graph.json 或使用 consistency checker）
```

### Step 8: Update Task Documents

1. 打开 `.specgov/tasks/product-manager.md`
2. 将 PRD 生成任务标记为完成：
   ```markdown
   ## Completed Tasks
   - ✅ 生成 PPRD.md v1.0 - 定义用户身份验证功能
   - ✅ 审查 PPRD.md，处理反馈
   ```
3. 切换到 Project Manager 视角
4. 打开 `.specgov/tasks/project-manager.md`
5. 更新 Epic 进度：
   ```markdown
   ## Active Epics

   ### Epic 1: 用户身份验证系统
   - 进度：40% → 60%
   - ✅ PRD.md 完成
   - ✅ PPRD.md 完成
   - ⏳ Design Document 待生成
   ```
6. 提交到 Git：
   ```powershell
   git add docs/PPRD.md .specgov/tasks/
   git commit -m "Add authentication features to PPRD.md"
   ```

## Common Pitfalls

- ❌ 忘记添加 `[Implements: PRD-REQ-XXX]` 标记
- ❌ 用户故事不遵循 "As/I want/So that" 格式
- ❌ 验收标准从技术角度描述，而非用户角度
- ❌ 验收标准不可测试（如 "界面美观"）
- ❌ 缺少 UI/UX 注意事项（对于面向用户的功能）
- ❌ PRD 包含技术实现细节（应该留给 Design Document）
- ❌ 未覆盖 RD 中的所有需求

## Validation Checklist

进入 Design Document 阶段前，验证：

- [ ] 每个功能都有 `[ID: PRD-FEAT-XXX]` 标记
- [ ] 每个功能都通过 `[Implements: PRD-REQ-XXX]` 链接到 RD
- [ ] RD 中的所有需求都被 PRD 覆盖（需求覆盖率 100%）
- [ ] 用户故事遵循 "As/I want/So that" 格式
- [ ] 验收标准可测试且从用户角度描述
- [ ] 面向用户的功能有 UI/UX 注意事项
- [ ] 无技术实现细节
- [ ] 审查已完成并处理反馈
- [ ] 任务文档已更新（product-manager.md + project-manager.md）
- [ ] 变更已提交到 Git
- [ ] Helper scripts 已运行，依赖图谱已更新

## Quick Reference Commands

```powershell
# 解析标记并构建图谱
python scripts/parse_tags.py
python scripts/build_graph.py

# 检查一致性（可选）
python scripts/check_consistency.py --scope PRD-REQ-005

# 提交到 Git
git add docs/PPRD.md .specgov/tasks/
git commit -m "Add features to PPRD.md"
```

## Next Steps

✅ PPRD.md 完成后，进入下一阶段：
- 查看 [Design Document Workflow](workflow-design.md)
- 切换到 Architect 角色
- 准备技术约束（语言、框架、部署环境等）
- 加载 `design-generator.md` 生成 Design-Document.md

---

**Estimated Time**: 2-4 hours (depending on project complexity)
**Estimated Cost**: $2-5 (Claude Code usage for generation + review)
