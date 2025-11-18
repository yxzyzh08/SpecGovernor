# Task Management Workflow

**[ID: WORKFLOW-TASK-001] [Implements: DESIGN-WORKFLOW-STAGES-001]**

## Overview

SpecGovernor 使用双层任务管理系统：
- **Epic Level**（Project Manager）：高层级目标和进度追踪
- **Task Level**（各角色）：具体任务和执行细节

## Role Perspective

主要由 **Project Manager** 负责，但所有角色都需要更新各自的任务文件。

## Task File Structure

### `.specgov/tasks/project-manager.md`

Project Manager 的任务文件包含：

```markdown
# Project Manager Tasks

## Active Epics

### Epic 1: [Epic Name]
- **目标**：[Epic 的高层级目标]
- **进度**：[X]%
- **状态**：[进行中 / 已完成 / 已暂停]
- **子任务**：
  - ✅ [已完成的子任务]
  - ⏳ [进行中的子任务]
  - ⬜ [待开始的子任务]

### Epic 2: [Epic Name]
...

## Completed Epics

### Epic X: [Epic Name]
- **完成日期**：YYYY-MM-DD
- **成果**：[简要说明]
```

### `.specgov/tasks/[role].md`

各角色的任务文件包含：

```markdown
# [Role Name] Tasks

## Active Tasks

### Task 1: [Task Name]
- **Epic**：Epic X - [Epic Name]
- **描述**：[详细描述]
- **状态**：[待开始 / 进行中 / 已完成]
- **预估时间**：[X] 小时
- **实际时间**：[X] 小时（完成后填写）

## Completed Tasks

### Task X: [Task Name]
- **完成日期**：YYYY-MM-DD
- **Epic**：Epic X - [Epic Name]
- **成果**：[简要说明]
```

## Step-by-Step Process

### Phase 1: Create Epic (As Project Manager)

#### Step 1: Define Epic

1. 打开 `.specgov/tasks/project-manager.md`
2. 在 "Active Epics" 部分添加新 Epic：

**Example:**
```markdown
## Active Epics

### Epic 1: 用户身份验证系统
- **目标**：实现一个安全、便捷的用户身份验证系统，支持 OAuth2 社交登录
- **进度**：0%
- **状态**：进行中
- **子任务**：
  - ⬜ 需求分析（RD）
  - ⬜ 产品规划（PRD）
  - ⬜ 技术设计（Design Document）
  - ⬜ 测试规划（Test Plan）
  - ⬜ 代码实现
- **预估时间**：20-30 小时
- **预估成本**：$15-25（Claude Code 使用）
```

#### Step 2: Decompose Epic into Tasks

分解 Epic 为具体任务，分配到各角色：

**Example:**
```markdown
Epic 1 任务分解：
- Product Manager：
  - 收集用户故事和业务需求
  - 生成 PRD.md
  - 审查 PRD.md
- Product Manager：
  - 定义产品愿景
  - 生成 PPRD.md
  - 审查 PPRD.md
- Architect：
  - 识别技术约束
  - 生成 Design-Document.md
  - 审查 Design Document
- Test Manager：
  - 定义测试环境
  - 生成 Test-Plan.md
  - 审查 Test Plan
- Developer：
  - 实现代码
  - 编写单元测试
  - 运行测试
```

#### Step 3: Assign Tasks to Roles

在各角色的任务文件中添加任务。

**Example: `.specgov/tasks/rd-analyst.md`**
```markdown
## Active Tasks

### Task 1: 生成用户身份验证需求文档
- **Epic**：Epic 1 - 用户身份验证系统
- **描述**：
  - 收集用户故事和业务需求
  - 使用 rd-generator.md 生成 PRD.md
  - 使用 rd-reviewer.md 审查 PRD.md
  - 根据审查反馈修改 PRD.md
- **状态**：待开始
- **预估时间**：3 小时
- **输出**：docs/PRD.md
```

### Phase 2: Execute Tasks (As Individual Roles)

#### Step 1: Switch to Role Perspective

1. 切换到分配的角色（如 Product Manager）
2. 打开 `.specgov/tasks/rd-analyst.md`
3. 查看 "Active Tasks"

#### Step 2: Update Task Status

开始任务前，更新状态：

```markdown
### Task 1: 生成用户身份验证需求文档
- **Epic**：Epic 1 - 用户身份验证系统
- **状态**：待开始 → 进行中
- **开始时间**：2025-11-16 10:00
```

#### Step 3: Execute Task

按照相应的 workflow 执行任务：
- RD 生成：查看 [RD Workflow](workflow-rd.md)
- PRD 生成：查看 [PRD Workflow](workflow-prd.md)
- Design 生成：查看 [Design Document Workflow](workflow-design.md)
- Test Plan 生成：查看 [Test Plan Workflow](workflow-test-plan.md)

#### Step 4: Mark Task as Completed

任务完成后，更新状态：

```markdown
## Completed Tasks

### Task 1: 生成用户身份验证需求文档
- **完成日期**：2025-11-16
- **Epic**：Epic 1 - 用户身份验证系统
- **成果**：docs/PRD.md v1.0（定义了 5 个身份验证需求）
- **实际时间**：3.5 小时（略超预估）
- **备注**：审查发现 2 个问题，已修复
```

### Phase 3: Update Epic Progress (As Project Manager)

#### Step 1: Switch Back to Project Manager Perspective

1. 切换到 Project Manager 角色
2. 打开 `.specgov/tasks/project-manager.md`

#### Step 2: Update Epic Progress

更新 Epic 的进度和子任务状态：

```markdown
### Epic 1: 用户身份验证系统
- **目标**：实现一个安全、便捷的用户身份验证系统，支持 OAuth2 社交登录
- **进度**：0% → 20%
- **状态**：进行中
- **子任务**：
  - ✅ 需求分析（RD）- 完成于 2025-11-16
  - ⏳ 产品规划（PRD）- 进行中
  - ⬜ 技术设计（Design Document）
  - ⬜ 测试规划（Test Plan）
  - ⬜ 代码实现
- **预估时间**：20-30 小时
- **已用时间**：3.5 小时
```

#### Step 3: Identify Blockers or Risks

如果有阻塞或风险，记录在 Epic 中：

```markdown
### Epic 1: 用户身份验证系统
...
- **风险**：
  - ⚠️  OAuth2 提供商限流（需要申请更高配额）
  - ⚠️  AWS Lambda 冷启动时间可能超过 200ms（需要性能测试验证）
- **阻塞**：
  - 无
```

### Phase 4: Complete Epic (As Project Manager)

#### Step 1: Verify All Sub-Tasks Completed

确认 Epic 的所有子任务都已完成：

```markdown
### Epic 1: 用户身份验证系统
- **子任务**：
  - ✅ 需求分析（RD）
  - ✅ 产品规划（PRD）
  - ✅ 技术设计（Design Document）
  - ✅ 测试规划（Test Plan）
  - ✅ 代码实现
```

#### Step 2: Run Final Verification

运行 helper scripts 验证可追溯性：

```powershell
# 解析标记
python scripts/parse_tags.py

# 构建依赖图谱
python scripts/build_graph.py

# 检查所有测试是否通过
pytest

# 检查一致性
python scripts/check_consistency.py --scope RD-AUTH-001
```

#### Step 3: Mark Epic as Completed

将 Epic 移到 "Completed Epics" 部分：

```markdown
## Completed Epics

### Epic 1: 用户身份验证系统
- **完成日期**：2025-11-20
- **成果**：
  - docs/PRD.md v1.0（5 个身份验证需求）
  - docs/PPRD.md v1.0（3 个产品功能）
  - docs/Design-Document.md v1.0（API、数据库、服务设计）
  - docs/Test-Plan.md v1.0（23 个测试用例）
  - src/ 代码实现（全部测试通过）
- **实际时间**：28 小时
- **实际成本**：$22（Claude Code 使用）
- **经验教训**：
  - OAuth2 提供商限流需要提前申请配额
  - AWS Lambda 冷启动时间可接受（< 200ms）
  - 双重质量保证（生成+审查）非常有效，发现了 15 个问题
```

## Best Practices

### 1. Keep Tasks Up-to-Date

- 每次开始或完成任务都更新状态
- 定期（每天或每周）审查任务文件

### 2. Use Descriptive Task Names

- ✅ "生成用户身份验证需求文档"
- ❌ "生成 RD"

### 3. Link Tasks to Epics

- 每个任务都应该链接到一个 Epic
- 方便追踪 Epic 进度

### 4. Record Actual Time

- 记录实际花费的时间
- 帮助改进未来的时间估算

### 5. Document Lessons Learned

- 在 Epic 完成后记录经验教训
- 分享给团队（如果不是 Super Individual）

### 6. Commit Task Updates to Git

```powershell
git add .specgov/tasks/
git commit -m "Update task status: RD generation completed"
```

## Common Pitfalls

- ❌ 忘记更新任务状态
- ❌ Epic 过大，难以追踪进度
- ❌ 任务描述不清晰
- ❌ 不记录实际时间和经验教训
- ❌ 不提交任务文件到 Git

## Quick Reference Commands

```powershell
# 查看 Project Manager 任务
cat .specgov/tasks/project-manager.md

# 查看 Product Manager 任务
cat .specgov/tasks/rd-analyst.md

# 提交任务更新
git add .specgov/tasks/
git commit -m "Update task status"
```

## Task File Templates

### Epic Template

```markdown
### Epic [N]: [Epic Name]
- **目标**：[高层级目标]
- **进度**：[X]%
- **状态**：[进行中 / 已完成 / 已暂停]
- **子任务**：
  - ✅ [已完成的子任务]
  - ⏳ [进行中的子任务]
  - ⬜ [待开始的子任务]
- **预估时间**：[X] 小时
- **已用时间**：[X] 小时
- **风险**：[列出风险]
- **阻塞**：[列出阻塞]
```

### Task Template

```markdown
### Task [N]: [Task Name]
- **Epic**：Epic X - [Epic Name]
- **描述**：[详细描述]
- **状态**：[待开始 / 进行中 / 已完成]
- **预估时间**：[X] 小时
- **实际时间**：[X] 小时
- **输出**：[预期输出]
```

---

**Tips**: 使用 Project Manager 视角追踪整体进度，使用各角色视角执行具体任务。定期更新任务文件，保持可见性。
