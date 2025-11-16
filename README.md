# SpecGovernor

**Version**: 1.0.0
**Type**: Toolkit (Prompt Templates + Workflow Documentation + Helper Scripts)

SpecGovernor 是一个专为**超级个体** (Super Individuals) 设计的综合工具包，提供标准化的软件开发流程支持。

---

## 🎯 核心价值

- **🔄 显式可追溯性**：通过嵌入式标记实现 100% 可靠的追踪
- **📝 标准化流程**：RD → PRD → Design Document → Test Plan → Code
- **🤖 AI 驱动**：配合 Claude Code 使用 prompt templates 生成规范文档
- **💰 零成本基础**：无需软件许可证，只需 Python 和 Claude Code

---

## 📋 环境要求

| 组件 | 要求 | 说明 |
|------|------|------|
| **操作系统** | Windows 10/11 | 当前版本专为 Windows 设计 |
| **Shell** | PowerShell 5.1+ | 命令行环境 |
| **Python** | 3.8+ | 运行 helper scripts |
| **AI 助手** | Claude Code | 配合 prompt templates 使用 |
| **版本控制** | Git 2.x+ | 用于影响分析功能 |

验证环境：

\`\`\`powershell
# 验证 Python
python --version

# 验证 Git
git --version

# 验证 PowerShell
$PSVersionTable.PSVersion
\`\`\`

---

## 🚀 快速开始

### 1. 下载 SpecGovernor

\`\`\`powershell
git clone https://github.com/yourname/SpecGovernor.git
cd SpecGovernor
\`\`\`

### 2. 初始化项目（在您的项目目录中）

\`\`\`powershell
# 进入您的项目目录
cd path/to/your/project

# 运行初始化脚本
python path/to/SpecGovernor/scripts/init_project.py
\`\`\`

这将创建 `.specgov/` 目录结构和初始文档模板。

### 3. 开始使用

查看生成的工作流文档：

\`\`\`powershell
# 阅读整体流程概览
type .specgov/workflows/workflow-overview.md
\`\`\`

---

## 📚 Helper Scripts

SpecGovernor 提供 5 个 Python helper scripts：

| Script | 功能 | 用法 |
|--------|------|------|
| **init_project.py** | 初始化项目结构 | \`python scripts/init_project.py\` |
| **parse_tags.py** | 解析可追溯性标记 | \`python scripts/parse_tags.py\` |
| **build_graph.py** | 构建依赖图谱 | \`python scripts/build_graph.py\` |
| **impact_analysis.py** | 分析变更影响 | \`python scripts/impact_analysis.py --changed=docs/RD.md\` |
| **check_consistency.py** | 收集一致性检查上下文 | \`python scripts/check_consistency.py --scope=RD-REQ-001\` |

### 典型工作流

\`\`\`powershell
# 1. 生成文档后，解析标记
python scripts/parse_tags.py

# 2. 构建依赖图谱
python scripts/build_graph.py

# 3. 修改文档后，分析影响
python scripts/impact_analysis.py --changed=docs/RD.md

# 4. 检查特定需求的一致性
python scripts/check_consistency.py --scope=RD-REQ-005 --output=context.md
\`\`\`

---

## 🏗️ 项目结构

成功初始化后，您的项目将包含：

\`\`\`
your-project/
├── .specgov/
│   ├── prompts/              # Prompt templates（从 SpecGovernor 复制）
│   ├── workflows/            # Workflow 文档（从 SpecGovernor 复制）
│   ├── tasks/                # 任务跟踪文件
│   ├── index/                # 脚本生成的索引
│   │   ├── tags.json
│   │   └── dependency-graph.json
│   └── project-config.json   # 项目配置
│
├── docs/                     # 您的项目文档
│   ├── RD.md
│   ├── PRD.md
│   ├── Design-Document.md
│   └── Test-Plan.md
│
└── src/                      # 您的源代码
\`\`\`

---

## 📖 使用流程

### 角色视角切换

作为超级个体，您需要在以下角色之间切换：

1. **Project Manager** - 创建 Epic，跟踪整体进度
2. **Requirements Analyst** - 生成和审查 RD
3. **Product Manager** - 生成和审查 PRD
4. **Architect** - 生成和审查 Design Document
5. **Test Manager** - 生成和审查 Test Plan
6. **Developer** - 实现代码

### SDLC 流程

\`\`\`
RD (需求) → PRD (产品) → Design (设计) → Test Plan (测试) → Code (代码)
     ↓            ↓            ↓            ↓            ↓
  rd-generator  prd-generator  design-generator  test-generator  code-generator
     ↓            ↓            ↓            ↓            ↓
  rd-reviewer   prd-reviewer  design-reviewer  test-reviewer  code-reviewer
\`\`\`

---

## 🏷️ 可追溯性标记

SpecGovernor 使用嵌入式标记建立文档间的追溯链：

### 标记类型

\`\`\`markdown
[ID: RD-REQ-001]                  # 定义唯一标识
[Implements: RD-REQ-001]          # 声明实现了上游需求
[Designs-for: PRD-FEAT-012]       # 声明为某功能设计
[Tests-for: DESIGN-API-008]       # 声明测试某设计
[Decomposes: RD-AUTH-001]         # 分解父级需求
\`\`\`

### ID 前缀规范

| 阶段 | 前缀 | 示例 |
|------|------|------|
| RD | RD-REQ-, RD-GOAL- | RD-REQ-001 |
| PRD | PRD-FEAT-, PRD-US- | PRD-FEAT-012 |
| Design | DESIGN-API-, DESIGN-DB- | DESIGN-API-008 |
| Test | TEST-CASE-, TEST-PERF- | TEST-CASE-015 |
| Code | CODE-API-, CODE-SERVICE- | CODE-API-008 |

---

## 💡 示例

### 需求定义 (RD.md)

\`\`\`markdown
## OAuth2 登录需求
**[ID: RD-REQ-005]**

系统需支持通过 OAuth2 协议进行用户登录。
\`\`\`

### 产品功能 (PRD.md)

\`\`\`markdown
## OAuth2 Social Login
**[ID: PRD-FEAT-012] [Implements: RD-REQ-005]**

#### User Story
> **As** 新用户
> **I want** 使用我的 Google 账号登录
> **So that** 我不需要创建新密码
\`\`\`

### API 设计 (Design-Document.md)

\`\`\`markdown
## OAuth2 Callback API
**[ID: DESIGN-API-008] [Designs-for: PRD-FEAT-012]**

**Endpoint**: POST /auth/oauth2/callback
\`\`\`

### 代码实现

\`\`\`typescript
/**
 * [ID: CODE-API-008] [Implements: DESIGN-API-008]
 */
export class AuthController {
    async oauth2Callback(req, res) {
        // Implementation
    }
}
\`\`\`

---

## 📊 依赖图谱

运行 \`build_graph.py\` 后，会生成依赖图谱：

\`\`\`
RD-REQ-005
  └─ PRD-FEAT-012 (implements)
      └─ DESIGN-API-008 (designs-for)
          └─ CODE-API-008 (implements)
              └─ TEST-CASE-015 (tests-for)
\`\`\`

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## 📄 许可证

MIT License

---

## 📚 文档

- [Requirements Document (RD.md)](./RD.md)
- [Product Requirements Document (PRD.md)](./PRD.md)
- [Design Document](./Design-Document.md)
- [Test Plan](./Test-Plan.md)

---

**🤖 Generated with SpecGovernor**
