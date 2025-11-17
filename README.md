# SpecGovernor

**Type**: Toolkit (Prompt Templates + Workflow Documentation + Helper Scripts)

SpecGovernor 是一个专为**超级个体** (Super Individuals) 设计的综合工具包，提供标准化的软件开发流程支持。

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

Windows (PowerShell): 
```powershell

#在您的项目根目录
cd your-project
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/yxzyzh08/SpecGovernor/main/install-specgov.ps1" -OutFile "install-specgov.ps1" 
```

# 在您的项目根目录
cd your-project
curl -O https://raw.githubusercontent.com/yxzyzh08/SpecGovernor/main/install-specgov.sh
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

| Script | 功能 | 用法 |
|--------|------|------|
| **init_project.py** | 初始化项目结构 | \`python scripts/init_project.py\` |
| **parse_tags.py** | 解析可追溯性标记 | \`python scripts/parse_tags.py\` |
| **build_graph.py** | 构建依赖图谱 | \`python scripts/build_graph.py\` |
| **impact_analysis.py** | 分析变更影响 | \`python scripts/impact_analysis.py --changed=docs/PRD.md\` |
| **check_consistency.py** | 收集一致性检查上下文 | \`python scripts/check_consistency.py --scope=PRD-REQ-001\` |

### 典型工作流

\`\`\`powershell
# 0. 项目规划（Project Manager 角色）
# 编辑 .specgov/tasks/project-manager.md 创建 Epic

# 1. 生成 PRD（Product Manager 角色）
# 在 Claude Code 中使用 /specgov-prd-gen 命令

# 2. 生成文档后，解析标记
python scripts/parse_tags.py

# 3. 构建依赖图谱
python scripts/build_graph.py

# 4. 更新任务进度
# 编辑 .specgov/tasks/product-manager.md 和 project-manager.md

# 5. 修改文档后，分析影响
python scripts/impact_analysis.py --changed=docs/PRD.md

# 6. 检查特定需求的一致性
python scripts/check_consistency.py --scope=PRD-REQ-005 --output=context.md
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
│   ├── PRD.md                # 产品需求文档（包含业务需求和产品功能）
│   ├── Design-Document.md
│   └── Test-Plan.md
│
├── reviews/                  # 审查报告（质量保证）
│   ├── PRD-Review-Report-YYYY-MM-DD.md
│   ├── Design-Review-Report-YYYY-MM-DD.md
│   └── Test-Review-Report-YYYY-MM-DD.md
│
└── src/                      # 您的源代码
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
[ID: PRD-REQ-001]                 # 定义业务需求（Part 1）
[ID: PRD-FEAT-012]                # 定义产品功能（Part 2）
[Implements: PRD-REQ-001]         # 功能实现需求
[Designs-for: PRD-FEAT-012]       # 设计某功能
[Tests-for: DESIGN-API-008]       # 测试某设计
[Decomposes: PRD-REQ-001]         # 分解父级需求
\`\`\`

### ID 前缀规范

| 阶段 | 前缀 | 示例 |
|------|------|------|
| PRD (Part 1: 业务需求) | PRD-REQ-, PRD-GOAL-, PRD-USER- | PRD-REQ-001 |
| PRD (Part 2: 产品功能) | PRD-FEAT-, PRD-US- | PRD-FEAT-012 |
| Design | DESIGN-API-, DESIGN-DB- | DESIGN-API-008 |
| Test | TEST-CASE-, TEST-PERF- | TEST-CASE-015 |
| Code | CODE-API-, CODE-SERVICE- | CODE-API-008 |

---

## 💡 示例

### 业务需求 (PRD.md - Part 1)

\`\`\`markdown
## Part 1: Business Requirements

### OAuth2 Authentication Requirement
**[ID: PRD-REQ-005]**

系统需支持通过 OAuth2 协议进行用户登录。

**验收标准：**
- ✅ 支持 Google/GitHub/Microsoft OAuth2
- ✅ 安全处理 token
\`\`\`

### 产品功能 (PRD.md - Part 2)

\`\`\`markdown
## Part 2: Product Features

### OAuth2 Social Login Feature
**[ID: PRD-FEAT-012] [Implements: PRD-REQ-005]**

#### User Story
> **As** 新用户
> **I want** 使用我的 Google 账号登录
> **So that** 我不需要创建新密码

#### Acceptance Criteria
- ✅ 显示 OAuth2 登录按钮
- ✅ 授权后自动登录
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
PRD-REQ-005 (业务需求)
  └─ PRD-FEAT-012 (implements) (产品功能)
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
