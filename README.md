# SpecGovernor

**Type**: Toolkit (Prompt Templates + Workflow Documentation + Helper Scripts)

SpecGovernor 4.0 是一个专为**超级个体** (Super Individuals) 设计的综合工具包，提供标准化的软件开发流程支持 ，它是基于SpecGovernor 3.0 自我迭代的新版本

> **v3.0 重大更新**：RD 和 PRD 已合并为单一 PRD 文档，简化流程，提高效率！

---

## 🎯 核心价值

- **🔄 显式可追溯性**：通过嵌入式标记实现 100% 可靠的追踪
- **📝 精简流程**：PRD → Design Document → Test Plan → Code（4 阶段）
- **🤖 AI 驱动**：配合 Claude Code 使用 prompt templates 生成规范文档
- **💰 零成本基础**：无需软件许可证，只需 Python 和 Claude Code
- **⚡ 超级个体优化**：消除 RD→PRD 转换的冗余工作

---

## 📋 环境要求

| 组件 | 要求 | 说明 |
|------|------|------|
| **操作系统** | Windows / Linux / macOS | 跨平台支持 |
| **Shell** | PowerShell 5.1+ / Bash 4.0+ | 命令行环境 |
| **Python** | 3.8+ | 运行 helper scripts |
| **AI 助手** | Claude Code | 配合 prompt templates 使用 |
| **版本控制** | Git 2.x+ | 用于影响分析功能 |

验证环境：

**Windows (PowerShell)**:
\`\`\`powershell
python --version
git --version
$PSVersionTable.PSVersion
\`\`\`

**Linux/Mac (Bash)**:
\`\`\`bash
python3 --version
git --version
bash --version
\`\`\`

---

## 🚀 快速开始

### 1. 下载安装脚本

**Windows (PowerShell)**:
\`\`\`powershell
# 在您的项目根目录
cd your-project
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/yxzyzh08/SpecGovernor/main/install/install-specgov.ps1" -OutFile "install-specgov.ps1"
\`\`\`

**Linux/Mac (Bash)**:
\`\`\`bash
# 在您的项目根目录
cd your-project
curl -O https://raw.githubusercontent.com/yxzyzh08/SpecGovernor/main/install/install-specgov.sh
chmod +x install-specgov.sh
\`\`\`

### 2. 运行安装脚本

**Windows**:
\`\`\`powershell
powershell -ExecutionPolicy Bypass -File install-specgov.ps1
\`\`\`

**Linux/Mac**:
\`\`\`bash
./install-specgov.sh
\`\`\`

安装脚本会自动下载所有必要文件并运行 `init_project.py`。

### 3. 开始使用

查看快速开始指南：

\`\`\`powershell
# Windows
type QUICK-START.md

# Linux/Mac
cat QUICK-START.md
\`\`\`

或阅读工作流概览：

\`\`\`powershell
# Windows
type .specgov/workflows/workflow-overview.md

# Linux/Mac
cat .specgov/workflows/workflow-overview.md
\`\`\`

> 📖 **完整安装指南**: [INSTALLATION.md](INSTALLATION.md)

---

## 📚 Helper Scripts

SpecGovernor 提供 5 个 Python helper scripts：

| Script | 功能 | 用法（在用户项目中） |
|--------|------|------|
| **init_project.py** | 初始化项目结构 | \`python .specgov/scripts/init_project.py\` |
| **parse_tags.py** | 解析可追溯性标记 | \`python .specgov/scripts/parse_tags.py\` |
| **build_graph.py** | 构建依赖图谱 | \`python .specgov/scripts/build_graph.py\` |
| **impact_analysis.py** | 分析变更影响 | \`python .specgov/scripts/impact_analysis.py --changed=docs/PRD.md\` |
| **check_consistency.py** | 收集一致性检查上下文 | \`python .specgov/scripts/check_consistency.py --scope=PRD-REQ-001\` |

### 典型工作流（在用户项目中）

\`\`\`powershell
# 0. 项目规划（Project Manager 角色）
# 编辑 .specgov/tasks/project-manager.md 创建 Epic

# 1. 生成 PRD（Product Manager 角色）
# 在 Claude Code 中使用 /specgov-prd-gen 命令

# 2. 生成文档后，解析标记
python .specgov/scripts/parse_tags.py

# 3. 构建依赖图谱
python .specgov/scripts/build_graph.py

# 4. 更新任务进度
# 编辑 .specgov/tasks/product-manager.md 和 project-manager.md

# 5. 修改文档后，分析影响
python .specgov/scripts/impact_analysis.py --changed=docs/PRD.md

# 6. 检查特定需求的一致性
python .specgov/scripts/check_consistency.py --scope=PRD-REQ-005 --output=context.md
\`\`\`

---

## 🏗️ 项目结构

### SpecGovernor 工具包仓库结构

\`\`\`
SpecGovernor/                    # 工具包仓库
├── templates/                   # 📦 模板资源（分发到用户项目）
│   ├── prompts/                # Prompt 模板（16 个）
│   ├── workflows/              # 工作流文档（6 个）
│   ├── tasks/                  # 任务文件模板（5 个）
│   ├── claude-commands/        # Claude Code 命令模板（预留）
│   └── raw-requirements/       # 原始需求模板
│
├── scripts/                    # 🛠️ Helper Scripts（分发到用户项目）
│   ├── init_project.py        # 项目初始化脚本
│   ├── parse_tags.py          # 标记解析脚本
│   ├── build_graph.py         # 依赖图构建脚本
│   ├── impact_analysis.py     # 影响分析脚本
│   └── check_consistency.py   # 一致性检查脚本
│
├── install/                    # 📥 安装脚本
│   ├── install-specgov.ps1   # Windows 安装脚本
│   └── install-specgov.sh    # Linux/Mac 安装脚本
│
├── docs/                       # 📚 SpecGovernor 自身文档
│   ├── PRD.md                 # SpecGovernor 产品需求
│   ├── Design-Document.md     # SpecGovernor 设计文档
│   └── Test-Plan.md          # SpecGovernor 测试计划
│
├── README.md                   # 主说明文档
├── CLAUDE.md                   # Claude Code 项目指南
├── INSTALLATION.md             # 安装指南
└── QUICK-START.md              # 快速开始指南
\`\`\`

### 用户项目结构（使用 SpecGovernor 后）

成功初始化后，您的项目将包含：

\`\`\`
your-project/
├── .specgov/                   # SpecGovernor 资源（从工具包复制）
│   ├── prompts/               # Prompt templates
│   ├── workflows/             # Workflow 文档
│   ├── scripts/               # Helper scripts
│   ├── tasks/                 # 任务跟踪文件
│   ├── index/                 # 脚本生成的索引
│   │   ├── tags.json
│   │   └── dependency-graph.json
│   └── project-config.json    # 项目配置
│
├── .claude/commands/           # Claude Code 斜杠命令
│
├── docs/                       # 您的项目文档
│   ├── PRD.md                 # 产品需求文档
│   ├── Design-Document.md
│   ├── Test-Plan.md
│   └── raw-requirements/      # 原始需求收集
│
└── src/                        # 您的源代码
\`\`\`

---

## 📖 使用流程

### 角色视角切换

作为超级个体，您需要在以下角色之间切换：

1. **Project Manager** - 创建 Epic，跟踪整体进度
2. **Product Manager** - 生成和审查 PRD（包含需求和产品功能）
3. **Architect** - 生成和审查 Design Document
4. **Test Manager** - 生成和审查 Test Plan
5. **Developer** - 实现代码

### SDLC 流程（v3.0 精简版）

\`\`\`
PRD (需求+产品) → Design (设计) → Test Plan (测试) → Code (代码)
        ↓               ↓              ↓             ↓
  prd-generator   design-generator test-generator code-generator
        ↓               ↓              ↓             ↓
  prd-reviewer    design-reviewer  test-reviewer  code-reviewer
\`\`\`

---

## 🏷️ 可追溯性标记

SpecGovernor 使用嵌入式标记建立文档间的追溯链：

### 标记类型

\`\`\`markdown
[ID: PRD-FEAT-012]                # 定义产品功能
[Raw-Req: Entry-003]              # 可选引用原始需求
[Designs-for: PRD-FEAT-012]       # 设计某功能
[Tests-for: DESIGN-API-008]       # 测试某设计
\`\`\`

### ID 前缀规范

| 阶段 | 前缀 | 示例 |
|------|------|------|
| 原始需求 | Entry-XXX | Entry-003（离散、非结构化） |
| PRD (产品功能) | PRD-FEAT-, PRD-US- | PRD-FEAT-012 |
| Design | DESIGN-API-, DESIGN-DB- | DESIGN-API-008 |
| Test | TEST-CASE-, TEST-PERF- | TEST-CASE-015 |
| Code | CODE-API-, CODE-SERVICE- | CODE-API-008 |

---

## 💡 示例

### 原始需求 (raw-requirements/inputs.md)

\`\`\`markdown
### Entry 003 - 2025-11-18 14:30

**Source**: Chat
**Topic**: 用户登录

**Original Input**:
> 我希望用户可以用 Google、GitHub 或者 Microsoft 账号登录，
> 这样他们就不用记另一个密码了。

**PM Analysis**:
- **Category**: Functional Requirement
- **Priority**: High
- **Status**: New
\`\`\`

### 产品功能 (PRD.md)

\`\`\`markdown
## 2. Authentication Features

### 2.1 OAuth2 Social Login Feature
**[ID: PRD-FEAT-012]** [Raw-Req: Entry-003]

#### User Story
> **As** 新用户
> **I want** 使用我的 Google/GitHub/Microsoft 账号登录
> **So that** 我不需要创建和记住新密码

#### Acceptance Criteria
- ✅ 显示 OAuth2 登录按钮（Google、GitHub、Microsoft）
- ✅ 授权后自动登录并获取用户信息
- ✅ 失败时显示清晰的错误消息
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
Entry-003 (原始需求 - 离散、非结构化)
  ↓ [可选引用]
PRD-FEAT-012 (产品功能)
  └─ DESIGN-API-008 (designs-for) (API 设计)
      └─ TEST-CASE-015 (tests-for) (测试用例)
          └─ CODE-API-008 (implements) (代码实现)
\`\`\`

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## 📄 许可证

MIT License

---

## 📚 文档

- [安装指南 (INSTALLATION.md)](./INSTALLATION.md)
- [快速开始 (QUICK-START.md)](./QUICK-START.md)
- [项目指南 (CLAUDE.md)](./CLAUDE.md)
- [GitHub Issues](https://github.com/yourname/SpecGovernor/issues)

---

**🤖 Generated with SpecGovernor**
