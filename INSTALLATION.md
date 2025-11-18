# SpecGovernor 安装指南

本文档提供 SpecGovernor 的详细安装步骤。

---

## 📋 前置要求

### 必需组件

| 组件 | 最低版本 | 推荐版本 | 验证命令 |
|------|----------|----------|----------|
| **Python** | 3.8 | 3.11+ | `python --version` |
| **Git** | 2.0 | 2.40+ | `git --version` |
| **PowerShell** (Windows) | 5.1 | 7.3+ | `$PSVersionTable.PSVersion` |
| **Bash** (Linux/Mac) | 4.0 | 5.1+ | `bash --version` |

### 推荐组件

- **Claude Code** - Anthropic 的 AI 编程助手（配合 prompt 模板使用）
- **VS Code** - 推荐的代码编辑器

### 验证环境

```powershell
# Windows (PowerShell)
python --version          # 应该显示 Python 3.8+
git --version            # 应该显示 git version 2.x
$PSVersionTable.PSVersion  # 应该显示 5.1+
```

```bash
# Linux/Mac (Bash)
python3 --version  # 应该显示 Python 3.8+
git --version      # 应该显示 git version 2.x
bash --version     # 应该显示 4.0+
```

---

## 🚀 安装步骤

SpecGovernor 使用自动化安装脚本，将工具包集成到您的项目中。安装脚本会自动下载所有必要的文件并设置项目结构。

#### Step 1: 下载安装脚本

**Windows (PowerShell)**:

```powershell
# 在项目根目录下载安装脚本
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/yxzyzh08/SpecGovernor/main/install/install-specgov.ps1" -OutFile "install-specgov.ps1"
```

**Linux/Mac (Bash)**:

```bash
# 在项目根目录下载安装脚本
curl -O https://raw.githubusercontent.com/yxzyzh08/SpecGovernor/main/install/install-specgov.sh
chmod +x install-specgov.sh
```

#### Step 2: 运行安装脚本

**Windows (PowerShell)**:

```powershell
# 运行安装脚本
powershell -ExecutionPolicy Bypass -File install-specgov.ps1
```

**Linux/Mac (Bash)**:

```bash
# 运行安装脚本
./install-specgov.sh
```

**安装脚本会：**
- ✅ 从 GitHub 下载 SpecGovernor 最新版本
- ✅ 下载 Helper Scripts 到 `.specgov/scripts/`
- ✅ 下载 Prompt 模板到 `.specgov/prompts/`
- ✅ 下载 Workflow 文档到 `.specgov/workflows/`
- ✅ 创建 `.specgov/` 完整结构
- ✅ 创建 `.claude/commands/` 目录（运行 init_project.py 后）
- ✅ 创建 `QUICK-START.md` 和 `CLAUDE.md`

#### Step 3: 初始化项目结构

```powershell
# 运行初始化脚本
python .specgov/scripts/init_project.py
```

#### Step 4: 验证安装

```powershell
# 检查目录结构
ls

# 应该看到新增的目录：
# - scripts/        (5 个 Python 脚本)
# - templates/      (prompts/ 和 workflows/)
# - .specgov/       (配置和任务文件)
# - docs/           (文档目录，如果之前没有)
```

#### Step 5: 清理安装文件（可选）

```powershell
# 删除安装脚本
rm install-specgov.ps1  # Windows
rm install-specgov.sh   # Linux/Mac
```

---

## 📁 安装后的目录结构

成功安装后，您的项目将新增以下 SpecGovernor 相关目录和文件：

```
your-project/                   # 您的项目根目录
│
├── .specgov/                   # ✨ SpecGovernor 所有文件
│   ├── scripts/                # Helper Scripts（5 个）
│   │   ├── init_project.py         # 项目初始化
│   │   ├── parse_tags.py           # 解析标记
│   │   ├── build_graph.py          # 构建图谱
│   │   ├── check_consistency.py    # 一致性检查
│   │   └── impact_analysis.py      # 影响分析
│   ├── prompts/                # Prompt 模板（14 个，v3.0）
│   │   ├── prd-generator.md            # 小项目
│   │   ├── prd-reviewer.md
│   │   ├── design-generator.md
│   │   ├── design-reviewer.md
│   │   ├── test-plan-generator.md
│   │   ├── test-plan-reviewer.md
│   │   ├── code-generator.md
│   │   ├── code-reviewer.md
│   │   ├── consistency-checker.md
│   │   ├── impact-analyzer.md
│   │   ├── prd-overview-generator.md     # 大项目
│   │   ├── prd-module-generator.md
│   │   ├── design-overview-generator.md
│   │   ├── design-module-generator.md
│   │   ├── test-plan-overview-generator.md
│   │   └── test-plan-module-generator.md
│   ├── workflows/              # 工作流文档（6 个）
│   │   ├── workflow-overview.md
│   │   ├── workflow-prd.md
│   │   ├── workflow-design.md
│   │   ├── workflow-test-plan.md
│   │   ├── workflow-task-mgmt.md
│   │   └── workflow-large-project.md
│   ├── tasks/                  # 任务跟踪文件（5 个）
│   │   ├── project-manager.md
│   │   ├── product-manager.md
│   │   ├── architect.md
│   │   ├── test-manager.md
│   │   └── developer.md
│   ├── index/                  # 索引数据（由脚本生成）
│   │   ├── tags.json           # 可追溯性标记索引
│   │   └── dependency-graph.json   # 依赖图谱
│   └── project-config.json     # 项目配置
│
├── .claude/                    # ✨ Claude Code 命令集成
│   └── commands/               # 斜杠命令（小项目 10 个，大项目 13 个）
│       ├── specgov-prd-gen.md
│       ├── specgov-prd-review.md
│       ├── specgov-design-gen.md
│       ├── specgov-design-review.md
│       ├── specgov-test-gen.md
│       ├── specgov-test-review.md
│       ├── specgov-code-gen.md
│       ├── specgov-code-review.md
│       ├── specgov-consistency.md
│       ├── specgov-impact.md
│       └── ...                 # 大项目还有 overview/module 命令
│
├── docs/                       # ✨ 您的项目文档目录
│   ├── raw-requirements/        # 原始需求收集
│   │   └── inputs.md           # 小项目：单个文件
│   │                           # 大项目：overview.md + modules/*.md
│   ├── PRD.md                   # 您的 Product Requirements Document
│   ├── Design-Document.md      # 您的 Design Document
│   └── Test-Plan.md            # 您的 Test Plan
│
├── src/                        # 您的源代码
├── tests/                      # 您的测试代码
├── README.md                   # 您的项目 README
│
├── QUICK-START.md              # ✨ SpecGovernor 快速开始指南
└── CLAUDE.md                   # ✨ Claude Code 项目指南

✨ = 由 SpecGovernor 安装脚本创建或下载的文件
```

**说明：**
- `.specgov/` 和 `.claude/` 目录由安装脚本自动创建
- 所有 SpecGovernor 文件都在 `.specgov/` 目录中，保持项目根目录整洁
- `docs/` 目录会被创建，但文档内容由您使用 SpecGovernor 工具生成
- `src/`, `tests/`, `README.md` 等是您项目原有的文件，不受影响

---

## 🔧 配置

### 项目配置文件

`.specgov/config.json` 包含项目配置：

```json
{
  "project_name": "my-project",
  "project_scale": "small",
  "docs_dir": "docs",
  "src_dir": "src",
  "tests_dir": "tests",
  "created_at": "2025-11-16"
}
```

**配置项说明：**
- `project_name`: 项目名称
- `project_scale`: 项目规模（"small" 或 "large"）
- `docs_dir`: 文档目录路径
- `src_dir`: 源代码目录路径
- `tests_dir`: 测试代码目录路径

### 自定义配置

您可以手动编辑 `.specgov/config.json` 来自定义配置：

```powershell
# 使用编辑器打开配置文件
code .specgov/config.json
```

---

## ✅ 验证安装

运行以下命令验证 SpecGovernor 是否正确安装：

### 1. 检查目录结构

```powershell
# 检查 .specgov 目录
ls .specgov/

# 应该看到：
# - config.json
# - prompts/ (20 个文件)
# - workflows/ (7 个文件)
# - tasks/ (6 个文件)
# - index/ (目录)
```

### 2. 检查 Python 脚本

```powershell
# 检查脚本目录
ls .specgov/scripts/

# 应该看到：
# - init_project.py
# - parse_tags.py
# - build_graph.py
# - check_consistency.py
# - impact_analysis.py
```

### 3. 测试 Helper Scripts

```powershell
# 测试 parse_tags.py（应该正常运行，即使没有标记）
python .specgov/scripts/parse_tags.py

# 应该看到：
# Parsed 0 tags from 0 files

# 测试 build_graph.py
python .specgov/scripts/build_graph.py

# 应该看到：
# Dependency graph saved to .specgov/index/dependency-graph.json
```

### 4. 检查文档模板

```powershell
# 检查 PRD.md 占位符
type docs/PRD.md

# 应该看到 PRD 占位符内容（提示使用 SpecGovernor v3.0 生成）
```

---

## 🐛 故障排除

### 问题1: `python` 命令未找到

**症状**:
```
python: command not found
```

**解决方案**:

Windows:
```powershell
# 检查 Python 是否安装
where python

# 如果未找到，从 python.org 下载安装
# https://www.python.org/downloads/
```

Linux/Mac:
```bash
# 使用 python3 而不是 python
python3 --version

# 或创建别名
alias python=python3
```

### 问题2: 权限错误（PowerShell 执行策略）

**症状**:
```
install-specgov.ps1 cannot be loaded because running scripts is disabled
```

**解决方案**:
```powershell
# 临时允许脚本执行
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# 或使用 -ExecutionPolicy 参数
powershell -ExecutionPolicy Bypass -File install-specgov.ps1
```

### 问题3: Git 未安装

**症状**:
```
git: command not found
```

**解决方案**:

Windows:
```powershell
# 从 git-scm.com 下载安装
# https://git-scm.com/download/win
```

Linux:
```bash
# Ubuntu/Debian
sudo apt install git

# CentOS/RHEL
sudo yum install git
```

Mac:
```bash
# 使用 Homebrew
brew install git

# 或使用 Xcode Command Line Tools
xcode-select --install
```

### 问题4: 网络问题（无法下载）

**症状**:
```
curl: Failed to connect to raw.githubusercontent.com
```

**解决方案**:

1. 检查网络连接
2. 尝试使用代理：
```powershell
# 设置代理（如果需要）
$env:HTTP_PROXY = "http://proxy.example.com:8080"
$env:HTTPS_PROXY = "http://proxy.example.com:8080"
```

3. 或手动下载文件到项目目录

---

## 🔄 更新 SpecGovernor

### 更新到最新版本

```powershell
# 1. 重新下载安装脚本
curl -O https://raw.githubusercontent.com/yourname/SpecGovernor/main/install-specgov.ps1

# 2. 重新运行安装脚本（会覆盖旧文件）
powershell -ExecutionPolicy Bypass -File install-specgov.ps1

# 3. 重新初始化
python .specgov/scripts/init_project.py
```

---

## 📚 下一步

安装完成后，建议按以下顺序学习：

1. **阅读快速开始指南**: `QUICK-START.md`
2. **了解工作流概览**: `.specgov/workflows/workflow-overview.md`
3. **查看任务管理流程**: `.specgov/workflows/workflow-task-mgmt.md`
4. **开始第一个 Epic**: 编辑 `.specgov/tasks/project-manager.md`

---

## 💡 提示

- **定期运行 Helper Scripts**: 在修改文档后运行 `parse_tags.py` 和 `build_graph.py`
- **使用 Git 追踪变更**: 所有文档和配置都应该提交到 Git
- **参考工作流文档**: 遇到问题时查看 `.specgov/workflows/` 中的相关文档
- **保持模板更新**: 定期检查 SpecGovernor 仓库的更新

---

**安装遇到问题？** 请在 GitHub 上提交 Issue: https://github.com/yourname/SpecGovernor/issues
