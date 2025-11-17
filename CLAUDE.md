# SpecGovernor - 项目指南

## 项目概述

**项目名称**: SpecGovernor
**项目规模**: 小项目（< 10 万行代码）
**文档结构**: 单层（RD.md, PRD.md, ...）
**使用工具**: SpecGovernor + Claude Code

> 请在此处填写您的项目简介、目标用户、核心功能等信息。

---

## 🛠️ SpecGovernor 工作流

本项目使用 **SpecGovernor** 工具包进行需求到代码的全流程可追溯性管理。

### SDLC 五阶段流程

1. **RD** - Requirements Document（需求文档）
2. **PRD** - Product Requirements Document（产品需求文档）
3. **Design-Document** - 设计文档
4. **Test-Plan** - 测试计划
5. **Code** - 代码实现

### Claude Code 斜杠命令

在 Claude Code 中使用以下命令快速加载 prompt 模板：

**基础命令（小项目 - 单层文档结构）**：
- `/specgov-rd-gen` - 生成 RD.md
- `/specgov-rd-review` - 审查 RD
- `/specgov-prd-gen` - 生成 PRD.md（**自动收集原始需求**）
- `/specgov-prd-review` - 审查 PRD
- `/specgov-design-gen` - 生成 Design-Document.md
- `/specgov-design-review` - 审查 Design Document
- `/specgov-test-gen` - 生成 Test-Plan.md
- `/specgov-test-review` - 审查 Test Plan
- `/specgov-code-gen` - 生成代码
- `/specgov-code-review` - 审查代码

**工具命令**：
- `/specgov-consistency` - 检查可追溯性一致性
- `/specgov-impact` - 分析需求变更影响

> **提示**：小项目使用单层文档结构，所有需求都在一个 RD.md 文件中。

### 原始需求收集

**功能说明**：产品经理在生成 PRD 时，会自动收集和记录人类提供的原始需求（口语化输入）。

**工作流程**：
1. 执行 `/specgov-prd-gen` 命令
2. 产品经理询问并记录原始需求到 `.specgov/raw-requirements/inputs.md`
3. 基于原始需求生成正式的 `docs/PRD.md`

**目录结构**：
```
.specgov/
└── raw-requirements/
    └── inputs.md              # 原始需求汇总文档
```

**用途**：
- 保留人类的口语化需求输入
- 便于后期查询和追溯需求来源
- 仅供超级个体本地参考，不影响项目构建

**大项目**：使用 `/specgov-prd-overview` 和 `/specgov-prd-module` 命令时，原始需求会分别记录到 `overview.md` 和 `modules/{module-name}.md`

### Helper Scripts

```bash
# 解析可追溯性标记
python .specgov/scripts/parse_tags.py

# 构建依赖图谱
python .specgov/scripts/build_graph.py

# 一致性检查
python .specgov/scripts/check_consistency.py

# 影响分析
python .specgov/scripts/impact_analysis.py --changed=docs/RD.md
```

---

## 📋 文档命名与版本管理规范

### 1. 文档命名规范

**重要原则：所有文档文件名必须使用英文命名**

- ✅ 正确示例：`RD.md`, `PRD.md`, `Design-Document.md`, `Test-Plan.md`
- ❌ 错误示例：`需求文档.md`, `设计文档.md`, `DD.md`, `TD.md`

### 2. 文档内容语言规范

**混合语言原则：**
- **中文为主**：文档正文、说明、描述使用中文
- **英文使用场景**：
  - 章节标题（如 Product Overview, Architecture Design）
  - 专业术语（如 OAuth2, API, Database）
  - 代码片段（变量名、函数名、类名）
  - 技术栈名称（如 React, PostgreSQL, Docker）

### 3. 版本管理规范

**单一版本原则：所有文档只保留最新版本**

- ✅ 只保留一个需求文档：`RD.md`
- ❌ 不要创建：`RD-v1.md`, `RD-v2.md`, `需求补充.md`
- ✅ 新需求直接更新到 `RD.md` 中
- ✅ 使用 Git 版本控制来追踪历史变更

### 4. 可追溯性标记规范

文档中的可追溯性标记使用英文标识符：

```markdown
[ID: RD-REQ-001]           # Requirements Document
[ID: PRD-FEAT-012]         # Product Requirements Document
[ID: DESIGN-API-008]       # Design Document
[ID: TEST-CASE-015]        # Test Plan

[Implements: RD-REQ-001]   # PRD 实现 RD
[Decomposes: RD-AUTH-001]  # 分解父级需求
[Designs-for: PRD-FEAT-012] # Design Document 设计 PRD 功能
[Tests-for: DESIGN-API-008] # Test Plan 测试 Design
```

### 5. 术语强制规范

**CRITICAL：必须使用完整英文术语，禁止缩写**

- ✅ **正确**: "Design Document"
- ❌ **错误**: "DD", "设计文档"

- ✅ **正确**: "Test Plan"
- ❌ **错误**: "TD", "TP", "测试文档"

---

## 🏗️ 项目技术栈

> 请在此处填写您的项目技术栈信息

### 前端技术栈
- （请填写，如 React, Vue, Angular 等）

### 后端技术栈
- （请填写，如 Node.js, Python, Java 等）

### 数据库
- （请填写，如 PostgreSQL, MongoDB, Redis 等）

### 部署环境
- （请填写，如 Docker, Kubernetes, AWS 等）

---

## 📐 架构约束

> 请在此处填写项目的架构约束、设计原则等

### 设计原则
- （请填写项目的设计原则）

### 技术约束
- （请填写技术约束，如性能要求、兼容性要求等）

### 安全要求
- （请填写安全要求）

---

## 👥 团队协作规范

> 请在此处填写团队的协作规范

### Git 提交规范
- （请填写 Git commit message 规范）

### Code Review 流程
- （请填写 Code Review 流程）

### 文档更新规范
- （请填写文档更新规范）

---

## 📚 参考文档

- [SpecGovernor 快速开始](QUICK-START.md)
- [工作流概览](.specgov/workflows/workflow-overview.md)
- [任务管理](.specgov/workflows/workflow-task-mgmt.md)

