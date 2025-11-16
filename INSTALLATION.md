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

## 🚀 安装方式

SpecGovernor 提供两种安装方式，根据您的需求选择：

### 方式1: 新项目（推荐）

**适用场景**: 创建全新项目，SpecGovernor 作为项目模板

**优点**:
- ✅ 一步到位，包含所有文件
- ✅ 完整的 Git 历史
- ✅ 可以直接修改和扩展模板

**步骤**:

#### Step 1: 克隆仓库

```powershell
# 克隆 SpecGovernor 仓库到新项目目录
git clone https://github.com/yourname/SpecGovernor.git my-project

# 进入项目目录
cd my-project
```

#### Step 2: 配置远程仓库（可选）

```powershell
# 如果您想将项目推送到自己的 GitHub 仓库
# 1. 在 GitHub 上创建新仓库（如 my-project）
# 2. 更改远程 origin
git remote remove origin
git remote add origin https://github.com/yourusername/my-project.git

# 3. 推送到新仓库
git push -u origin main
```

#### Step 3: 初始化项目

```powershell
# 运行初始化脚本
python scripts/init_project.py
```

**初始化脚本会：**
- ✅ 创建 `.specgov/index/` 目录
- ✅ 创建 `.specgov/tasks/` 目录和任务文件
- ✅ 创建 `docs/` 目录和文档模板
- ✅ 创建 `.specgov/config.json` 配置文件
- ✅ 复制 prompt 模板到 `.specgov/prompts/`
- ✅ 复制工作流文档到 `.specgov/workflows/`

#### Step 4: 验证安装

```powershell
# 检查目录结构
ls .specgov/

# 应该看到：
# - config.json
# - prompts/      (20 个 .md 文件)
# - workflows/    (7 个 .md 文件)
# - tasks/        (6 个 .md 文件)
# - index/        (空目录，运行脚本后会生成文件)

# 检查文档目录
ls docs/

# 应该看到：
# - RD.md
# - PRD.md
# - Design-Document.md
# - Test-Plan.md
```

#### Step 5: 开始使用

```powershell
# 阅读快速开始指南
type QUICK-START.md

# 或在 VS Code 中打开
code QUICK-START.md
```

---

### 方式2: 集成到现有项目

**适用场景**: 为现有项目添加 SpecGovernor 工具包

**优点**:
- ✅ 不影响现有项目结构
- ✅ 可以与现有文档共存
- ✅ 灵活集成

**步骤**:

#### Step 1: 下载安装脚本

**Windows (PowerShell)**:

```powershell
# 在项目根目录下载安装脚本
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/yourname/SpecGovernor/main/install-specgov.ps1" -OutFile "install-specgov.ps1"
```

**Linux/Mac (Bash)**:

```bash
# 在项目根目录下载安装脚本
curl -O https://raw.githubusercontent.com/yourname/SpecGovernor/main/install-specgov.sh
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
- ✅ 复制 `scripts/` 目录到项目
- ✅ 复制 `templates/` 目录到项目
- ✅ 创建 `.specgov/` 基础结构
- ✅ 创建 `QUICK-START.md` 和 `CLAUDE.md`

#### Step 3: 初始化项目结构

```powershell
# 运行初始化脚本
python scripts/init_project.py
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

成功安装后，您的项目应该包含以下结构：

```
your-project/
├── .specgov/                   # SpecGovernor 配置和数据
│   ├── config.json             # 项目配置
│   ├── prompts/                # Prompt 模板（20 个）
│   │   ├── rd-generator.md
│   │   ├── rd-reviewer.md
│   │   ├── prd-generator.md
│   │   ├── prd-reviewer.md
│   │   ├── design-generator.md
│   │   ├── design-reviewer.md
│   │   ├── test-plan-generator.md
│   │   ├── test-plan-reviewer.md
│   │   ├── code-generator.md
│   │   ├── code-reviewer.md
│   │   ├── consistency-checker.md
│   │   ├── impact-analyzer.md
│   │   ├── rd-overview-generator.md      # 大项目
│   │   ├── rd-module-generator.md        # 大项目
│   │   ├── prd-overview-generator.md     # 大项目
│   │   ├── prd-module-generator.md       # 大项目
│   │   ├── design-overview-generator.md  # 大项目
│   │   ├── design-module-generator.md    # 大项目
│   │   ├── test-plan-overview-generator.md   # 大项目
│   │   └── test-plan-module-generator.md     # 大项目
│   ├── workflows/              # 工作流文档（7 个）
│   │   ├── workflow-overview.md
│   │   ├── workflow-rd.md
│   │   ├── workflow-prd.md
│   │   ├── workflow-design.md
│   │   ├── workflow-test-plan.md
│   │   ├── workflow-task-mgmt.md
│   │   └── workflow-large-project.md
│   ├── tasks/                  # 任务跟踪文件
│   │   ├── project-manager.md
│   │   ├── rd-analyst.md
│   │   ├── product-manager.md
│   │   ├── architect.md
│   │   ├── test-manager.md
│   │   └── developer.md
│   └── index/                  # 索引数据（由脚本生成）
│       ├── tags.json           # 可追溯性标记索引
│       └── dependency-graph.json   # 依赖图谱
├── docs/                       # 项目文档
│   ├── RD.md                   # Requirements Document
│   ├── PRD.md                  # Product Requirements Document
│   ├── Design-Document.md      # Design Document
│   └── Test-Plan.md            # Test Plan
├── scripts/                    # Helper Scripts
│   ├── init_project.py         # 项目初始化
│   ├── parse_tags.py           # 解析标记
│   ├── build_graph.py          # 构建图谱
│   ├── check_consistency.py    # 一致性检查
│   └── impact_analysis.py      # 影响分析
├── src/                        # 源代码（您的代码）
├── tests/                      # 测试代码（您的测试）
├── README.md                   # 项目 README
├── INSTALLATION.md             # 本文档
├── QUICK-START.md              # 快速开始指南
└── CLAUDE.md                   # Claude Code 项目指南
```

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
ls scripts/

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
python scripts/parse_tags.py

# 应该看到：
# Parsed 0 tags from 0 files

# 测试 build_graph.py
python scripts/build_graph.py

# 应该看到：
# Dependency graph saved to .specgov/index/dependency-graph.json
```

### 4. 检查文档模板

```powershell
# 检查 RD.md 模板
type docs/RD.md

# 应该看到 RD 模板内容
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

### 方式1 安装的更新方法

```powershell
# 1. 进入项目目录
cd my-project

# 2. 拉取最新更改
git pull origin main

# 3. 重新运行初始化（如有新功能）
python scripts/init_project.py
```

### 方式2 安装的更新方法

```powershell
# 1. 重新下载安装脚本
curl -O https://raw.githubusercontent.com/yourname/SpecGovernor/main/install-specgov.ps1

# 2. 重新运行安装脚本（会覆盖旧文件）
powershell -ExecutionPolicy Bypass -File install-specgov.ps1

# 3. 重新初始化
python scripts/init_project.py
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
