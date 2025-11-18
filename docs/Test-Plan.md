# **Test Plan - SpecGovernor**

> **Test Goal**: 工具包组件的综合测试策略

---

## **Traceability Declaration**

本 Test Plan 覆盖以下 Design Document 组件：
- [Tests-for: DESIGN-TEMPLATE-STRUCT-001] Prompt Template Structure
- [Tests-for: DESIGN-TEMPLATE-RD-GEN-001] RD Generator Template
- [Tests-for: DESIGN-TEMPLATE-PRD-GEN-001] PRD Generator Template
- [Tests-for: DESIGN-TEMPLATE-DESIGN-GEN-001] Design Document Generator Template
- [Tests-for: DESIGN-TEMPLATE-TEST-GEN-001] Test Plan Generator Template
- [Tests-for: DESIGN-TEMPLATE-CODE-GEN-001] Code Generator Template
- [Tests-for: DESIGN-TEMPLATE-CODE-REV-001] Code Reviewer Template
- [Tests-for: DESIGN-WORKFLOW-OVERVIEW-001] Workflow Overview Document
- [Tests-for: DESIGN-SCRIPT-INIT-001] Project Initialization Script
- [Tests-for: DESIGN-SCRIPT-PARSER-001] Tag Parser Script
- [Tests-for: DESIGN-SCRIPT-GRAPH-001] Dependency Graph Builder Script
- [Tests-for: DESIGN-SCRIPT-IMPACT-001] Impact Analysis Script
- [Tests-for: DESIGN-SCRIPT-CONSISTENCY-001] Consistency Check Script

---

## **零、Test Environment Setup**

### **0.1 Testing Approach**

**[ID: TEST-ENV-001]**

SpecGovernor 是一个工具包产品，测试需要在**独立的测试项目**中进行，而不是在 SpecGovernor 开发项目本身中测试。

**测试策略：**

1. 在 SpecGovernor 项目**外部**创建独立的测试项目
2. 按照 `INSTALLATION.md` 安装 SpecGovernor 工具包到测试项目
3. 在测试项目中执行所有测试用例
4. 发现问题后，返回 SpecGovernor 项目修复
5. 重新安装工具包到测试项目，继续测试

**目录结构示例：**

```
D:\test_workspace\                 # 测试工作区
│
├── SpecGovernor\                  # 工具包开发项目（本项目）
│   ├── .specgov/                  # 产品：所有 SpecGovernor 文件
│   │   ├── scripts/               # Helper Scripts
│   │   ├── prompts/               # Prompt Templates
│   │   └── workflows/             # Workflow 文档
│   ├── install-specgov.ps1        # 安装脚本
│   ├── install-specgov.sh         # 安装脚本
│   ├── docs/
│   │   ├── RD.md                  # SpecGovernor 的需求文档
│   │   ├── PRD.md                 # SpecGovernor 的产品文档
│   │   ├── Design-Document.md     # SpecGovernor 的设计文档
│   │   └── Test-Plan.md           # SpecGovernor 的测试计划（本文档）
│   └── INSTALLATION.md
│
└── TestProject-TodoApp\           # 独立的测试项目
    ├── .specgov/                  # 由 init_project.py 创建
    │   ├── scripts/               # 从 SpecGovernor/.specgov/scripts/ 下载
    │   │   ├── init_project.py
    │   │   ├── parse_tags.py
    │   │   ├── build_graph.py
    │   │   ├── check_consistency.py
    │   │   └── impact_analysis.py
    │   ├── prompts/               # 从 SpecGovernor/.specgov/prompts/ 下载
    │   ├── workflows/             # 从 SpecGovernor/.specgov/workflows/ 下载
    │   ├── tasks/
    │   ├── index/
    │   └── project-config.json
    ├── .claude/                   # Claude Code 命令集成
    │   └── commands/              # 20 个斜杠命令
    ├── docs/                      # TodoApp 的文档（由测试生成）
    │   ├── RD.md                  # TodoApp 的需求文档
    │   ├── PRD.md                 # TodoApp 的产品文档
    │   ├── Design-Document.md     # TodoApp 的设计文档
    │   └── Test-Plan.md           # TodoApp 的测试计划
    └── src/                       # TodoApp 的代码
```

---

### **0.2 Test Project Preparation**

**[ID: TEST-ENV-002]**

在执行测试前，需要准备测试项目。

#### **步骤 1：创建测试项目目录**

**Windows (PowerShell)**:
```powershell
# 在 SpecGovernor 项目外部创建测试项目
cd D:\test_workspace\
mkdir TestProject-TodoApp
cd TestProject-TodoApp

# 初始化 Git 仓库（推荐）
git init
```

**Linux/Mac (Bash)**:
```bash
# 在 SpecGovernor 项目外部创建测试项目
cd ~/test_workspace/
mkdir TestProject-TodoApp
cd TestProject-TodoApp

# 初始化 Git 仓库（推荐）
git init
```

#### **步骤 2：安装 SpecGovernor 工具包**

按照 `INSTALLATION.md` 的指引安装：

**Windows (PowerShell)**:
```powershell
# 下载安装脚本
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/yourname/SpecGovernor/main/install-specgov.ps1" -OutFile "install-specgov.ps1"

# 或从本地复制（如果在离线环境）
Copy-Item D:\test_workspace\SpecGovernor\install-specgov.ps1 .

# 运行安装脚本
powershell -ExecutionPolicy Bypass -File install-specgov.ps1
```

**Linux/Mac (Bash)**:
```bash
# 下载安装脚本
curl -O https://raw.githubusercontent.com/yourname/SpecGovernor/main/install-specgov.sh
chmod +x install-specgov.sh

# 或从本地复制（如果在离线环境）
cp ~/test_workspace/SpecGovernor/install-specgov.sh .
chmod +x install-specgov.sh

# 运行安装脚本
./install-specgov.sh
```

安装脚本会自动：
- ✅ 下载所有 scripts 和 templates
- ✅ 创建 `.specgov/` 目录结构
- ✅ 运行 `init_project.py`（会提示选择项目规模）
- ✅ 创建 `docs/` 目录

#### **步骤 3：验证安装**

检查以下目录和文件是否已创建：

```powershell
# Windows
ls .specgov\prompts\ | Measure-Object
# 应该显示 20 个 .md 文件

ls .specgov\workflows\ | Measure-Object
# 应该显示 7 个 .md 文件

ls .specgov\scripts\ | Measure-Object
# 应该显示 5 个 .py 文件

# Linux/Mac
ls .specgov/prompts/ | wc -l
# 应该显示 20

ls .specgov/workflows/ | wc -l
# 应该显示 7

ls .specgov/scripts/ | wc -l
# 应该显示 5
```

**验证清单：**
- [ ] `.specgov/prompts/rd-generator.md` 存在
- [ ] `.specgov/workflows/workflow-overview.md` 存在
- [ ] `.specgov/scripts/parse_tags.py` 存在
- [ ] `.specgov/project-config.json` 存在
- [ ] `.claude/commands/` 目录已创建
- [ ] `docs/` 目录已创建

---

### **0.3 Testing Execution Context**

**[ID: TEST-ENV-003]**

**重要说明：本测试计划中的所有测试用例，除非特别说明，都应该在独立的测试项目中执行（如 `TestProject-TodoApp/`），而不是在 SpecGovernor 开发项目中。**

**路径引用约定：**

本文档中的路径引用默认指测试项目（如 `TestProject-TodoApp/`）中的路径：

| 路径引用 | 实际路径（示例） |
|---------|----------------|
| `.specgov/prompts/rd-generator.md` | `D:\test_workspace\TestProject-TodoApp\.specgov\prompts\rd-generator.md` |
| `docs/RD.md` | `D:\test_workspace\TestProject-TodoApp\docs\RD.md` |
| `python .specgov/scripts/parse_tags.py` | 在 `TestProject-TodoApp/` 目录下运行 `python .specgov\scripts\parse_tags.py` |

**当前工作目录：**

所有测试用例默认在测试项目根目录（`TestProject-TodoApp/`）下执行，除非特别说明。

**SpecGovernor 项目路径：**

当需要修复问题时，返回 SpecGovernor 项目：
- Windows: `D:\test_workspace\SpecGovernor\`
- Linux/Mac: `~/test_workspace/SpecGovernor/`

---

### **0.4 Test Data Preparation**

**[ID: TEST-ENV-004]**

某些测试用例需要预先准备的测试数据。

#### **小项目测试数据**

在 `TestProject-TodoApp/` 中创建示例需求：

```markdown
# docs/RD.md（部分内容，用于测试）

## 1. Todo Management Requirements
**[ID: RD-TODO-001]**

### 1.1 Create Todo Item
**[ID: PRD-REQ-001] [Decomposes: PRD-REQ-TODO-001]**

用户必须能够创建待办事项。

### 1.2 Mark Todo as Complete
**[ID: PRD-REQ-002] [Decomposes: PRD-REQ-TODO-001]**

用户必须能够标记待办事项为完成状态。
```

这些测试数据将用于测试 `parse_tags.py`, `build_graph.py` 等脚本。

---

### **0.5 VS Code Workspace Setup (Recommended)**

**[ID: TEST-ENV-005]**

为了提高测试效率，**强烈建议**使用 VS Code 工作区（Workspace）同时打开 SpecGovernor 开发项目和测试项目。

#### **为什么使用工作区？**

- ✅ 快速在两个项目之间切换
- ✅ 并排对比文件（开发项目 vs. 测试项目）
- ✅ 跨项目搜索
- ✅ 统一的集成终端管理
- ✅ 修复问题时无需切换窗口

#### **创建工作区**

**方式1：使用提供的工作区文件**

SpecGovernor 项目根目录提供了 `SpecGovernor-Testing.code-workspace` 工作区配置文件。

```powershell
# 打开工作区
code D:\test_workspace\SpecGovernor\SpecGovernor-Testing.code-workspace
```

**注意**：打开前请先创建测试项目（`TestProject-TodoApp`），否则工作区会显示文件夹缺失。

**方式2：手动创建工作区**

1. 打开 SpecGovernor 项目
2. **File** → **Add Folder to Workspace...**
3. 选择 `TestProject-TodoApp` 目录
4. **File** → **Save Workspace As...** → 保存为 `SpecGovernor-Testing.code-workspace`

#### **工作区界面**

打开后，VS Code 侧边栏会显示两个项目根目录：

```
📁 SPECGOVERNOR (DEV)
  ├── templates/prompts/
  │   ├── rd-generator.md          ← 开发中的模板
  │   └── ...
  ├── scripts/
  │   ├── parse_tags.py            ← 开发中的脚本
  │   └── ...
  └── docs/
      ├── RD.md                     ← SpecGovernor 的需求文档
      └── ...

📁 TESTPROJECT-TODOAPP
  ├── .specgov/prompts/
  │   ├── rd-generator.md          ← 安装的模板（副本）
  │   └── ...
  ├── .specgov/scripts/
  │   ├── parse_tags.py            ← 安装的脚本（副本）
  │   └── ...
  └── docs/
      ├── RD.md                     ← 测试生成的文档
      └── ...
```

#### **典型测试流程（使用工作区）**

```
1. 在 TestProject 中打开 Claude Code
2. 使用 .specgov/prompts/rd-generator.md 生成 RD.md
3. 发现生成的 RD.md 有问题 ❌
4. 在同一个 VS Code 窗口中：
   - 切换到 SpecGovernor (Dev) 项目
   - 修改 templates/prompts/rd-generator.md
   - 保存
5. 重新安装工具包到 TestProject：
   cd TestProject
   powershell -ExecutionPolicy Bypass -File ..\SpecGovernor\install-specgov-local.ps1
6. 在 TestProject 中重新生成 RD.md
7. 验证修复 ✅
```

#### **工作区终端管理**

在 VS Code 集成终端中：

```
终端1 (SpecGovernor 开发):
  PS D:\test_workspace\SpecGovernor>
  # 修改代码、运行单元测试

终端2 (TestProject 测试):
  PS D:\test_workspace\TestProject-TodoApp>
  # 运行测试用例、生成文档
```

---

### **0.6 Environment Cleanup**

**[ID: TEST-ENV-006]**

测试完成后，可以选择清理测试环境：

```powershell
# 删除整个测试项目
cd D:\test_workspace\
rm -r -Force TestProject-TodoApp
```

或保留测试项目用于回归测试。

---

## **一、Test Strategy**

### **1.1 Overall Approach**

**[ID: TEST-STRATEGY-001]**

SpecGovernor 是一个**工具包**（不是软件），因此测试重点聚焦于三个方面：

1. **Prompt Template 验证**：验证模板能够指导 Claude Code 生成符合规范的文档
2. **Workflow 文档审查**：验证工作流程清晰完整
3. **Helper Script 测试**：Python 脚本的单元测试和集成测试

**测试级别：**

| 级别 | 重点 | 覆盖范围 |
|-------|-------|----------|
| **Manual Testing** | Prompt templates, workflows | 人工评估生成的文档质量 |
| **Unit Testing** | Python scripts | pytest 测试每个函数 |
| **Integration Testing** | End-to-end workflows | 完整的 SDLC 周期 |
| **Acceptance Testing** | Real-world usage | Dog-fooding 用 SpecGovernor 本身测试 |

---

### **1.2 Testing Tools**

**[ID: TEST-STRATEGY-002]**

| 工具 | 用途 | 使用方式 |
|------|---------|-------|
| **Claude Code** | 执行 prompt templates | 手动测试模板 |
| **pytest** | Python 单元/集成测试 | 自动化测试脚本 |
| **pytest-cov** | 代码覆盖率测量 | 确保 > 80% 覆盖率 |
| **Git** | 版本控制, diff 测试 | 测试 impact analysis 脚本 |
| **Manual Review** | Workflow 文档 | 通读和执行测试 |

---

## **二、Prompt Template Testing**

### **2.1 RD Generator Template Tests**

**[ID: TEST-CASE-001] [Tests-for: DESIGN-TEMPLATE-RD-GEN-001]**

#### **Test Case: Generate RD from User Stories**

**[ID: TEST-CASE-001-001]**

**前置条件：**
- Claude Code 已安装且可访问
- rd-generator.md 模板可用

**测试步骤：**
1. 打开 Claude Code
2. 加载 `.specgov/prompts/rd-generator.md`
3. 提供示例用户故事：
   ```
   - As a user, I want to log in with OAuth2 so I don't need a password
   - As a user, I want to reset my password if I forget it
   ```
4. 执行 prompt

**预期结果：**
- ✅ 生成的 RD.md 包含：
  - 正确的文档头（Version, Created date）
  - 身份认证需求章节
  - OAuth2 需求带 **[ID: PRD-REQ-XXX]** 标记
  - 密码重置需求带 **[ID: PRD-REQ-YYY]** 标记
  - 每个需求的验收标准
  - 使用 **[Decomposes: XXX]** 的层级结构（如适用）

**验证清单：**
- [ ] 所有需求都有 [ID: RD-XXX] 标记
- [ ] 没有占位符或 TODO
- [ ] 验收标准可测试
- [ ] 使用正确的格式

---

#### **Test Case: Modify Existing RD**

**[ID: TEST-CASE-001-002]**

**前置条件：**
- 前一个测试中生成的 RD.md 已存在
- rd-generator.md 模板可用

**测试步骤：**
1. 打开 Claude Code
2. 加载 `.specgov/prompts/rd-generator.md`
3. 提供：
   - 现有 RD.md 内容
   - 变更请求："Add requirement for 2FA (two-factor authentication)"
4. 执行 prompt

**预期结果：**
- ✅ 修改后的 RD.md 包含：
  - 原有需求保留（保持原有 ID）
  - 新的 2FA 需求添加了新的 **[ID: PRD-REQ-ZZZ]** 标记
  - 正确集成到现有结构中

**验证清单：**
- [ ] 原有需求 ID 未改变
- [ ] 新需求有唯一 ID
- [ ] 没有断开的引用
- [ ] 格式一致

---

#### **Test Case: Generate RD for Large Project**

**[ID: TEST-CASE-001-003]**

**前置条件：**
- 项目已初始化为大型项目（Two-Tier）
- rd-overview-generator.md 和 rd-module-generator.md 可用

**测试步骤：**
1. 使用 rd-overview-generator.md 生成 RD-Overview.md
2. 使用 rd-module-generator.md 生成 RD-User-Module.md
3. 验证模块文档

**预期结果：**
- ✅ RD-Overview.md 包含高层概览
- ✅ RD-User-Module.md 包含 **[Module: User]** 标记
- ✅ 模块 ID 使用模块前缀：**[ID: RD-User-REQ-001]**
- ✅ Overview 和 Module 文档相互引用

---

### **2.2 RD Reviewer Template Tests**

**[ID: TEST-CASE-002] [Tests-for: DESIGN-TEMPLATE-RD-GEN-001]**

#### **Test Case: Review Complete RD**

**[ID: TEST-CASE-002-001]**

**前置条件：**
- RD.md 已生成（带正确标记）
- rd-reviewer.md 模板可用

**测试步骤：**
1. 打开 Claude Code
2. 加载 `.specgov/prompts/rd-reviewer.md`
3. 提供 RD.md 进行审查
4. 执行 prompt

**预期结果：**
- ✅ 审查报告包含：
  - 摘要（质量评级、问题数量）
  - 可追溯性检查（所有需求都有 ID，没有断开的引用）
  - 完整性检查（所有章节都存在）
  - 质量评估（可测试性、清晰度）
  - 具体的改进建议

**验证清单：**
- [ ] 报告格式符合模板
- [ ] 所有可追溯性标记已验证
- [ ] 问题按严重程度分类
- [ ] 建议可执行

---

#### **Test Case: Review RD with Missing Tags**

**[ID: TEST-CASE-002-002]**

**前置条件：**
- RD.md 故意缺少 [ID: XXX] 标记
- rd-reviewer.md 模板可用

**测试步骤：**
1. 创建测试 RD.md，有 3 个需求，但只有 2 个有 [ID: XXX] 标记
2. 在 Claude Code 中加载 rd-reviewer.md
3. 提供测试 RD.md
4. 执行 prompt

**预期结果：**
- ✅ 审查报告识别出缺失的标记：
  - 问题严重程度：Critical 或 Warning
  - 位置：Section X.X（缺失标记的具体位置）
  - 建议："Add [ID: RD-XXX] tag to requirement"

**验证清单：**
- [ ] 检测到缺失的标记
- [ ] 提供具体位置
- [ ] 给出清晰的建议

---

### **2.3 PRD, Design Document, Test Plan Template Tests**

**[ID: TEST-CASE-003] [Tests-for: DESIGN-TEMPLATE-PRD-GEN-001, DESIGN-TEMPLATE-DESIGN-GEN-001, DESIGN-TEMPLATE-TEST-GEN-001]**

与上述 RD templates 类似的测试用例，重点关注：

#### **PRD Generator Tests:**
- [ ] 生成带 **[ID: PRD-FEAT-XXX]** 的功能
- [ ] 使用 **[Implements: PRD-REQ-REQ-XXX]** 链接到 RD
- [ ] 创建格式正确的用户故事
- [ ] 使用正确的 "PRD" 术语（不是 product requirements）

#### **Design Document Generator Tests:**
- [ ] 生成带 **[ID: DESIGN-ARCH-XXX]** 的架构
- [ ] 生成带 **[ID: DESIGN-API-XXX]** 的 API
- [ ] 使用 **[Designs-for: PRD-FEAT-XXX]** 链接到 PRD
- [ ] **始终使用 "Design Document"（不是 "DD"）**

#### **Test Plan Generator Tests:**
- [ ] 生成带 **[ID: TEST-CASE-XXX]** 的测试用例
- [ ] 使用 **[Tests-for: DESIGN-API-XXX]** 链接到 Design Document
- [ ] 包含前置条件、步骤、预期结果
- [ ] **始终使用 "Test Plan"（不是 "TD"）**

---

### **2.4 Code Template Tests**

**[ID: TEST-CASE-CODE] [Tests-for: DESIGN-TEMPLATE-CODE-GEN-001, DESIGN-TEMPLATE-CODE-REV-001]**

#### **Test Case: Generate Code from Design Document**
**[ID: TEST-CASE-CODE-GEN-001]**

**前置条件：**
- Claude Code 已安装且可访问
- code-generator.md 模板可用
- Design-Document.md 已生成

**测试步骤：**
1. 打开 Claude Code
2. 加载 `.specgov/prompts/code-generator.md`
3. 提供示例 Design Document 片段（API 设计）
4. 执行 prompt

**预期结果：**
- ✅ 生成的代码包含：
  - **[ID: CODE-XXX]** 标记
  - **[Implements: DESIGN-XXX]** 可追溯性标记
  - 符合设计规范的代码结构
  - 适当的注释和文档字符串
  - 遵循语言编码规范（如 Python 的 PEP 8）

**验证清单：**
- [ ] 所有代码单元都有 [ID: CODE-XXX] 标记
- [ ] 有 [Implements: DESIGN-XXX] 链接到设计
- [ ] 代码可编译/运行
- [ ] 符合编码规范

---

#### **Test Case: Review Code for Quality**
**[ID: TEST-CASE-CODE-REV-001]**

**测试步骤：**
1. 使用 code-reviewer.md 审查一段高质量代码
2. 验证审查报告给出正面评价

**预期结果：**
- ✅ 报告确认代码质量良好
- ✅ 无重大问题

---

#### **Test Case: Review Code with Security Issues**
**[ID: TEST-CASE-CODE-REV-002]**

**测试步骤：**
1. 准备包含安全漏洞的代码（如 SQL 注入、XSS）
2. 使用 code-reviewer.md 审查
3. 验证审查报告是否识别安全问题

**预期结果：**
- ✅ 报告标记安全漏洞（Critical）
- ✅ 提供修复建议
- ✅ 包含安全最佳实践引用

---

## **三、Workflow Documentation Testing**

### **3.1 Workflow Documentation Review**

**[ID: TEST-CASE-004] [Tests-for: DESIGN-WORKFLOW-OVERVIEW-001, DESIGN-WORKFLOW-STAGES-001]**

#### **Test Case: Execute Complete RD Workflow**

**[ID: TEST-CASE-004-001]**

**前置条件：**
- 全新的 SpecGovernor 项目已初始化
- workflow-rd.md 可用

**测试步骤：**
1. 逐步阅读 workflow-rd.md
2. 精确遵循每个步骤：
   - 切换到 Requirements Analyst 角色
   - 打开任务文件
   - 在 Claude Code 中加载 rd-generator.md
   - 提供示例输入
   - 生成 RD.md
   - 使用 rd-reviewer.md 审查
   - 更新任务文档
3. 记录任何不清楚的步骤或缺失信息

**预期结果：**
- ✅ 工作流清晰完整
- ✅ 所有步骤都可以无困惑地执行
- ✅ RD.md 成功生成
- ✅ 任务文档正确更新

**验证清单：**
- [ ] 没有模糊的步骤
- [ ] 没有缺失的前置条件
- [ ] 示例有帮助且准确
- [ ] Common pitfalls 章节准确

---

#### **Test Case: Execute Complete SDLC Workflow**

**[ID: TEST-CASE-004-002]**

**前置条件：**
- 全新项目已初始化
- workflow-overview.md 可用

**测试步骤：**
1. 执行完整工作流：RD → PRD → Design Document → Test Plan → Code
2. 遵循每个阶段的工作流文档
3. 验证可追溯性链：
   - PRD 使用 [Implements: PRD-REQ-XXX] 链接到 RD
   - Design Document 使用 [Designs-for: PRD-XXX] 链接到 PRD
   - Test Plan 使用 [Tests-for: DESIGN-XXX] 链接到 Design Document

**预期结果：**
- ✅ 建立完整的可追溯性链
- ✅ 所有文档成功生成
- ✅ 所有文档使用正确的术语（Design Document, Test Plan）
- ✅ 任务跟踪在所有角色间工作正常

**验证清单：**
- [ ] RD → PRD → Design Document → Test Plan 链完整
- [ ] 没有断开的可追溯性引用
- [ ] 术语在整个流程中一致
- [ ] 任务文档在每个阶段更新

---

### **3.2 Task Management Workflow Tests**

**[ID: TEST-CASE-TASK-MGMT] [Tests-for: DESIGN-WORKFLOW-TASK-001]**

#### **Test Case: Create Epic as Project Manager**
**[ID: TEST-CASE-TASK-MGMT-001]**

**前置条件：**
- workflow-task-mgmt.md 可用
- .specgov/tasks/ 目录已创建

**测试步骤：**
1. 阅读 workflow-task-mgmt.md
2. 作为 "Project Manager" 角色
3. 在 .specgov/tasks/project-manager.md 中创建新 Epic
4. 分解为 5 个子任务，分配给不同角色

**预期结果：**
- ✅ Epic 包含清晰的描述和目标
- ✅ 所有子任务都有估计工时
- ✅ 子任务分配到适当的角色
- ✅ Markdown 格式正确

---

#### **Test Case: Execute Task and Update Progress**
**[ID: TEST-CASE-TASK-MGMT-002]**

**测试步骤：**
1. 切换到 "Requirements Analyst" 角色
2. 打开 .specgov/tasks/rd-analyst.md
3. 完成一个子任务，记录工作日志
4. 标记任务为完成
5. 切换回 "Project Manager" 角色
6. 更新 project-manager.md 中的 Epic 进度

**预期结果：**
- ✅ 角色特定任务文件包含详细工作日志
- ✅ Project Manager 文件正确更新进度百分比
- ✅ 两个文件保持同步
- ✅ 流程顺畅，无混淆

---

## **四、Helper Script Testing**

### **4.1 Project Initialization Script Tests**

**[ID: TEST-CASE-005] [Tests-for: DESIGN-SCRIPT-INIT-001]**

#### **Test Case: Initialize Small Project**

**[ID: TEST-CASE-005-001]**

**前置条件：**
- Python 3.8+ 已安装
- SpecGovernor 仓库已克隆
- 空的目标目录

**测试步骤：**
1. 导航到空目录
2. 运行：`python .specgov/scripts/init_project.py`
3. 选择选项 1（small project）
4. 验证创建的结构

**预期结果：**
- ✅ `.specgov/` 目录创建，包含：
  - `prompts/`（所有模板文件已复制）
  - `workflows/`（所有工作流文件已复制）
  - `tasks/`（5 个任务文件：project-manager.md, rd-analyst.md 等）
  - `index/`（空的，用于生成的文件）
  - `project-config.json`（带正确的元数据）
- ✅ `docs/` 目录创建，包含：
  - `RD.md`（占位符）
  - `PRD.md`（占位符）
  - `Design-Document.md`（占位符）
  - `Test-Plan.md`（占位符）

**验证清单：**
- [ ] 所有目录都存在
- [ ] 所有模板文件正确复制
- [ ] project-config.json 有 `"project_size": "small"` 和 `"document_structure": "single-tier"`
- [ ] 脚本在 < 5 秒内完成

**测试代码（pytest）：**

```python
def test_init_small_project(tmp_path):
    os.chdir(tmp_path)

    # Run init script
    import init_project
    with mock.patch('builtins.input', return_value='1'):
        init_project.main()

    # Verify structure
    assert (tmp_path / '.specgov').exists()
    assert (tmp_path / '.specgov' / 'prompts').exists()
    assert (tmp_path / '.specgov' / 'workflows').exists()
    assert (tmp_path / '.specgov' / 'tasks' / 'project-manager.md').exists()
    assert (tmp_path / 'docs' / 'RD.md').exists()
    assert (tmp_path / 'docs' / 'PRD.md').exists()
    assert (tmp_path / 'docs' / 'Design-Document.md').exists()
    assert (tmp_path / 'docs' / 'Test-Plan.md').exists()

    # Verify config
    with open(tmp_path / '.specgov' / 'project-config.json') as f:
        config = json.load(f)
    assert config['project_size'] == 'small'
    assert config['document_structure'] == 'single-tier'
```

---

#### **Test Case: Initialize Large Project**

**[ID: TEST-CASE-005-002]**

**前置条件：**
- 与 Test Case 005-001 相同

**测试步骤：**
1. 导航到空目录
2. 运行：`python .specgov/scripts/init_project.py`
3. 选择选项 2（large project）
4. 验证创建的结构

**预期结果：**
- ✅ `.specgov/` 目录（与 small project 相同）
- ✅ `docs/` 目录采用双层结构：
  - `RD/` 目录，包含 `RD-Overview.md`
  - `PRD/` 目录，包含 `PRD-Overview.md`
  - `Design-Document/` 目录，包含 `Design-Overview.md`
  - `Test-Plan/` 目录，包含 `Test-Overview.md`

**验证清单：**
- [ ] 双层目录结构已创建
- [ ] project-config.json 有 `"project_size": "large"` 和 `"document_structure": "two-tier"`
- [ ] 脚本在 < 5 秒内完成

**测试代码（pytest）：**

```python
def test_init_large_project(tmp_path):
    os.chdir(tmp_path)

    with mock.patch('builtins.input', return_value='2'):
        init_project.main()

    # Verify two-tier structure
    assert (tmp_path / 'docs' / 'RD' / 'RD-Overview.md').exists()
    assert (tmp_path / 'docs' / 'PRD' / 'PRD-Overview.md').exists()
    assert (tmp_path / 'docs' / 'Design-Document' / 'Design-Overview.md').exists()
    assert (tmp_path / 'docs' / 'Test-Plan' / 'Test-Overview.md').exists()

    with open(tmp_path / '.specgov' / 'project-config.json') as f:
        config = json.load(f)
    assert config['project_size'] == 'large'
    assert config['document_structure'] == 'two-tier'
```

---

### **4.2 Tag Parser Script Tests**

**[ID: TEST-CASE-006] [Tests-for: DESIGN-SCRIPT-PARSER-001]**

#### **Test Case: Parse Tags from Single File**

**[ID: TEST-CASE-006-001]**

**测试数据：**
```markdown
# Requirements Document

## 1. Authentication
**[ID: RD-AUTH-001]**

### 1.1 OAuth2 Login
**[ID: PRD-REQ-005] [Decomposes: PRD-REQ-AUTH-001]**

System must support OAuth2 login.
```

**测试步骤：**
1. 创建包含上述内容的测试 RD.md
2. 运行：`python .specgov/scripts/parse_tags.py`
3. 验证输出

**预期结果：**
- ✅ `.specgov/index/tags.json` 创建，包含：
```json
{
  "tags": [
    {
      "id": "RD-AUTH-001",
      "type": "requirement",
      "file": "docs/RD.md",
      "line": 4
    },
    {
      "id": "RD-REQ-005",
      "type": "requirement",
      "file": "docs/RD.md",
      "line": 7,
      "decomposes": "RD-AUTH-001"
    }
  ]
}
```

**验证清单：**
- [ ] 所有标记都找到
- [ ] 行号正确
- [ ] 关系已捕获（decomposes）
- [ ] 类型正确推断
- [ ] 脚本在 < 1 秒内完成

**测试代码（pytest）：**

```python
def test_parse_tags_single_file(tmp_path):
    # Create test file
    rd_file = tmp_path / 'docs' / 'RD.md'
    rd_file.parent.mkdir(parents=True)
    rd_file.write_text("""# Requirements Document

## 1. Authentication
**[ID: RD-AUTH-001]**

### 1.1 OAuth2 Login
**[ID: PRD-REQ-005] [Decomposes: PRD-REQ-AUTH-001]**
""")

    os.chdir(tmp_path)

    # Run parser
    import parse_tags
    parse_tags.main()

    # Verify output
    with open(tmp_path / '.specgov' / 'index' / 'tags.json') as f:
        data = json.load(f)

    assert len(data['tags']) == 2
    assert data['tags'][0]['id'] == 'RD-AUTH-001'
    assert data['tags'][1]['id'] == 'RD-REQ-005'
    assert data['tags'][1]['decomposes'] == 'RD-AUTH-001'
```

---

#### **Test Case: Parse Tags from Multiple Document Types**

**[ID: TEST-CASE-006-002]**

**测试数据：**
- RD.md 包含 `[ID: PRD-REQ-001]`
- PRD.md 包含 `[ID: PRD-FEAT-001] [Implements: PRD-REQ-REQ-001]`
- Design-Document.md 包含 `[ID: DESIGN-API-001] [Designs-for: PRD-FEAT-001]`
- Test-Plan.md 包含 `[ID: TEST-CASE-001] [Tests-for: DESIGN-API-001]`

**预期结果：**
- ✅ 从所有文件中找到所有标记
- ✅ 正确捕获关系：
  - PRD implements RD
  - Design designs-for PRD
  - Test tests-for Design
- ✅ 每种类型都正确推断

**验证清单：**
- [ ] 捕获跨文档关系
- [ ] 识别所有标记类型
- [ ] 对于 100K LOC 性能 < 1 分钟

---

### **4.3 Dependency Graph Builder Tests**

**[ID: TEST-CASE-007] [Tests-for: DESIGN-SCRIPT-GRAPH-001]**

#### **Test Case: Build Graph from Tags**

**[ID: TEST-CASE-007-001]**

**前置条件：**
- tags.json 存在（来自 parse_tags.py）

**测试步骤：**
1. 运行：`python .specgov/scripts/build_graph.py`
2. 验证输出

**预期结果：**
- ✅ `.specgov/index/dependency-graph.json` 创建，包含：
```json
{
  "nodes": [
    {"id": "RD-REQ-001", "type": "requirement", "location": "docs/RD.md#L5"},
    {"id": "PRD-FEAT-001", "type": "feature", "location": "docs/PRD.md#L10"},
    {"id": "DESIGN-API-001", "type": "api_design", "location": "docs/Design-Document.md#L15"}
  ],
  "edges": [
    {"from": "PRD-FEAT-001", "to": "RD-REQ-001", "relation": "implements"},
    {"from": "DESIGN-API-001", "to": "PRD-FEAT-001", "relation": "designs-for"}
  ]
}
```

**验证清单：**
- [ ] 所有节点已创建
- [ ] 所有边已创建
- [ ] 关系正确表示
- [ ] 脚本在 < 1 分钟内完成

**测试代码（pytest）：**

```python
def test_build_graph(tmp_path):
    # Create tags.json
    tags_file = tmp_path / '.specgov' / 'index' / 'tags.json'
    tags_file.parent.mkdir(parents=True, exist_ok=True)
    tags_file.write_text(json.dumps({
        "tags": [
            {"id": "RD-REQ-001", "type": "requirement", "file": "docs/RD.md", "line": 5},
            {"id": "PRD-FEAT-001", "type": "feature", "file": "docs/PRD.md", "line": 10, "implements": "RD-REQ-001"}
        ]
    }))

    os.chdir(tmp_path)

    # Run graph builder
    import build_graph
    build_graph.main()

    # Verify output
    with open(tmp_path / '.specgov' / 'index' / 'dependency-graph.json') as f:
        graph = json.load(f)

    assert len(graph['nodes']) == 2
    assert len(graph['edges']) == 1
    assert graph['edges'][0]['from'] == 'PRD-FEAT-001'
    assert graph['edges'][0]['to'] == 'RD-REQ-001'
    assert graph['edges'][0]['relation'] == 'implements'
```

---

#### **Test Case: Detect Circular Dependencies**

**[ID: TEST-CASE-007-002]**

**测试数据：**
- A implements B
- B designs-for C
- C implements A（循环！）

**预期结果：**
- ✅ 检测到循环依赖
- ✅ 控制台输出显示：`⚠️  Detected 1 circular dependencies: A → B → C → A`

**验证清单：**
- [ ] 识别循环依赖
- [ ] 路径清晰显示
- [ ] 脚本不崩溃

---

### **4.4 Impact Analysis Script Tests**

**[ID: TEST-CASE-008] [Tests-for: DESIGN-SCRIPT-IMPACT-001]**

#### **Test Case: Analyze Impact of RD Change**

**[ID: TEST-CASE-008-001]**

**前置条件：**
- Dependency graph 存在
- RD.md 已提交到 Git
- Git 工作目录

**测试步骤：**
1. 修改 RD.md（更改需求 [ID: PRD-REQ-005]）
2. Git add 并 commit 更改
3. 运行：`python .specgov/scripts/impact_analysis.py --changed=docs/RD.md`
4. 验证输出

**预期结果：**
- ✅ 控制台输出显示：
```
🔍 Analyzing impact...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Impact Analysis Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Changed Nodes (1):
  • RD-REQ-005 (requirement) at docs/RD.md#L10

Affected Nodes (3):
  ⚠️  PRD-FEAT-012 (feature) at docs/PRD.md#L50
      Reason: Implements RD-REQ-005

  ⚠️  DESIGN-API-008 (api_design) at docs/Design-Document.md#L100
      Reason: Designs-for PRD-FEAT-012

  ⚠️  TEST-CASE-015 (test) at docs/Test-Plan.md#L200
      Reason: Tests-for DESIGN-API-008

Recommended Actions:
  1. Review and update affected documents
  2. Run tests for affected code
  3. Update dependency graph

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⏱️  Time: < 10 seconds
💰 Cost: $0 (graph query only)
```

**验证清单：**
- [ ] 正确识别已更改节点
- [ ] 找到所有下游节点
- [ ] 关系解释清晰
- [ ] 性能 < 10 秒
- [ ] 成本 = $0（无 AI 调用）

**测试代码（pytest）：**

```python
def test_impact_analysis(tmp_path):
    # Setup git repo
    repo = git.Repo.init(tmp_path)

    # Create and commit RD.md
    rd_file = tmp_path / 'docs' / 'RD.md'
    rd_file.parent.mkdir(parents=True)
    rd_file.write_text("**[ID: PRD-REQ-005]** OAuth2 Login")
    repo.index.add([str(rd_file)])
    repo.index.commit("Initial commit")

    # Create graph
    graph = {
        "nodes": [
            {"id": "RD-REQ-005", "type": "requirement", "location": "docs/RD.md#L1"},
            {"id": "PRD-FEAT-012", "type": "feature", "location": "docs/PRD.md#L10"}
        ],
        "edges": [
            {"from": "PRD-FEAT-012", "to": "RD-REQ-005", "relation": "implements"}
        ]
    }
    graph_file = tmp_path / '.specgov' / 'index' / 'dependency-graph.json'
    graph_file.parent.mkdir(parents=True, exist_ok=True)
    graph_file.write_text(json.dumps(graph))

    # Modify RD.md
    rd_file.write_text("**[ID: PRD-REQ-005]** OAuth2 Login MODIFIED")

    os.chdir(tmp_path)

    # Run impact analysis
    import impact_analysis
    # ... test analysis output
```

---

### **4.5 Consistency Check Script Tests**

**[ID: TEST-CASE-CONSISTENCY] [Tests-for: DESIGN-SCRIPT-CONSISTENCY-001]**

#### **Test Case: Build Complete Dependency Chain**
**[ID: TEST-CASE-CONSISTENCY-001]**

**测试目标：** 验证 `check-consistency.py` 能够为给定的 scope ID 构建完整的上游和下游依赖链。

**前置条件：**
- dependency-graph.json 已生成
- 测试项目包含完整的依赖链（RD -> PRD -> Design -> Test -> Code）

**测试步骤：**
```python
def test_build_dependency_chain():
    """测试构建完整依赖链"""
    from .specgov.scripts.check_consistency import build_dependency_chain

    # 给定中间节点 PRD-FEAT-012
    scope_id = "PRD-FEAT-012"

    # 执行
    chain = build_dependency_chain(scope_id, graph_file=".specgov/index/dependency-graph.json")

    # 验证
    assert "RD-REQ-005" in chain["upstream"]  # 上游需求
    assert "DESIGN-API-008" in chain["downstream"]  # 下游设计
    assert "TEST-CASE-015" in chain["downstream"]  # 下游测试
    assert len(chain["upstream"]) >= 1
    assert len(chain["downstream"]) >= 2
```

**预期结果：**
- ✅ 返回包含上游和下游节点的字典
- ✅ 上游包含所有依赖的 RD 需求
- ✅ 下游包含所有相关的 Design、Test、Code
- ✅ 依赖链完整，无断链

---

#### **Test Case: Generate Context File**
**[ID: TEST-CASE-CONSISTENCY-002]**

**测试步骤：**
```python
def test_generate_context_md():
    """测试生成 context.md 文件"""
    import os
    from .specgov.scripts.check_consistency import generate_context

    scope_id = "PRD-FEAT-012"
    output_file = ".specgov/context/PRD-FEAT-012-context.md"

    # 执行
    generate_context(scope_id, output_file)

    # 验证文件存在
    assert os.path.exists(output_file)

    # 验证内容
    with open(output_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 必须包含 scope 节点本身
    assert "PRD-FEAT-012" in content
    # 必须包含上游需求
    assert "RD-REQ-005" in content
    # 必须包含下游设计
    assert "DESIGN-API-008" in content
    # 必须包含文件路径引用
    assert "docs/RD.md" in content
    assert "docs/PRD.md" in content
```

**预期结果：**
- ✅ 生成 context.md 文件
- ✅ 文件包含依赖链上所有节点的内容片段
- ✅ 每个片段包含文件路径和行号
- ✅ 格式清晰，便于 Claude Code 理解

---

#### **Test Case: Handle Missing Scope ID**
**[ID: TEST-CASE-CONSISTENCY-003]**

**测试步骤：**
```python
def test_handle_missing_scope():
    """测试不存在的 scope ID"""
    from .specgov.scripts.check_consistency import build_dependency_chain
    import pytest

    # 不存在的 ID
    scope_id = "NONEXISTENT-ID-999"

    # 应该抛出明确的异常
    with pytest.raises(ValueError, match="Scope ID .* not found"):
        build_dependency_chain(scope_id)
```

**预期结果：**
- ✅ 抛出 ValueError 异常
- ✅ 错误消息清晰："Scope ID 'NONEXISTENT-ID-999' not found in dependency graph"

---

#### **Test Case: Warn on Large Context**
**[ID: TEST-CASE-CONSISTENCY-004]**

**测试步骤：**
```python
def test_warn_large_context():
    """测试超大上下文警告"""
    from .specgov.scripts.check_consistency import generate_context
    import logging

    # 假设有一个超长依赖链（> 5K tokens）
    scope_id = "DESIGN-LARGE-MODULE-001"

    with pytest.warns(UserWarning, match="Context size exceeds"):
        generate_context(scope_id, max_tokens=5000)
```

**预期结果：**
- ✅ 输出警告信息
- ✅ 警告包含当前 token 数和建议
- ✅ 仍然生成完整的 context.md

---

## **五、Acceptance Testing (Dog-fooding)**

### **5.1 Use SpecGovernor to Manage SpecGovernor**

**[ID: TEST-CASE-009]**

**目标**：使用 SpecGovernor 工具包管理 SpecGovernor 项目本身（dog-fooding）。

**测试步骤：**
1. 在 SpecGovernor 仓库内初始化 SpecGovernor 结构
2. 使用 rd-generator.md 优化 RD.md
3. 使用 prd-generator.md 优化 PRD.md
4. 使用 design-generator.md 优化 Design-Document.md
5. 使用 test-plan-generator.md 优化 Test-Plan.md
6. 运行 parse_tags.py 从 SpecGovernor 文档中提取所有可追溯性标记
7. 运行 build_graph.py 构建依赖图
8. 对 RD.md 进行更改
9. 运行 impact_analysis.py 查看受影响的文档

**预期结果：**
- ✅ 所有 prompts 按预期工作
- ✅ 所有工作流清晰易懂
- ✅ 所有脚本成功运行
- ✅ 所有 SpecGovernor 文档之间的可追溯性链完整
- ✅ Impact analysis 正确识别受影响的文档

**验证清单：**
- [ ] Dog-fooding 过程中未发现问题
- [ ] 发现的问题已记录并修复
- [ ] SpecGovernor 文档符合其自身的质量标准

---

## **六、Performance Testing**

### **6.1 Performance Benchmarks**

**[ID: TEST-CASE-010] [Tests-for: DESIGN-NFR-PERF-001]**

| 操作 | 目标 | 测试方法 | 验收标准 |
|-----------|--------|------------|-------------------|
| Tag parsing | < 1 分钟处理 100K LOC | 创建 100K 行测试项目，运行 parse_tags.py | ✅ 在 < 60 秒内完成 |
| Graph building | < 1 分钟处理 100K LOC | 使用 100K LOC 项目的 tags，运行 build_graph.py | ✅ 在 < 60 秒内完成 |
| Impact analysis | < 10 秒 | 在大型图上运行 impact_analysis.py | ✅ 在 < 10 秒内完成 |
| Project initialization | < 5 秒 | 运行 init_project.py | ✅ 在 < 5 秒内完成 |

**测试代码（pytest with benchmarks）：**

```python
@pytest.mark.benchmark
def test_parse_tags_performance(benchmark, large_test_project):
    """测试解析 100K LOC 项目。"""
    result = benchmark(parse_tags.main)
    assert result is not None
    # pytest-benchmark 将自动验证时间

@pytest.mark.benchmark
def test_graph_build_performance(benchmark, parsed_tags):
    """测试从 100K LOC tags 构建图。"""
    result = benchmark(build_graph.main)
    assert result is not None
```

---

## **七、Test Coverage Goals**

### **7.1 Coverage Targets**

**[ID: TEST-STRATEGY-003]**

| 组件 | 行覆盖率目标 | 分支覆盖率目标 |
|-----------|---------------------|----------------------|
| **init_project.py** | ≥ 90% | ≥ 85% |
| **parse_tags.py** | ≥ 95% | ≥ 90% |
| **build_graph.py** | ≥ 95% | ≥ 90% |
| **impact_analysis.py** | ≥ 90% | ≥ 85% |
| **Overall Scripts** | ≥ 90% | ≥ 85% |

**测量方法：**
```bash
pytest --cov=scripts --cov-report=html --cov-report=term
```

---

## **八、Test Automation**

### **8.1 CI/CD Integration**

**[ID: TEST-STRATEGY-004]**

**GitHub Actions Workflow (.github/workflows/test.yml):**

```yaml
name: SpecGovernor Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          pip install pytest pytest-cov pytest-benchmark
      - name: Run unit tests
        run: pytest tests/ --cov=scripts --cov-report=xml
      - name: Check coverage
        run: |
          coverage report --fail-under=90
```

---

## **九、Test Environment**

### **9.1 Test Data**

**[ID: TEST-STRATEGY-005]**

**测试项目：**

1. **Minimal Project**：1 个需求，1 个功能，1 个设计，1 个测试
   - 用途：基本功能测试
   - 位置：`tests/fixtures/minimal-project/`

2. **Small Project**：10 个需求，8 个功能，6 个设计，15 个测试
   - 用途：真实小型项目测试
   - 位置：`tests/fixtures/small-project/`

3. **Large Project**：100K LOC，50 个需求，40 个功能，多个模块
   - 用途：性能和可扩展性测试
   - 位置：`tests/fixtures/large-project/`

---

## **十、Risk-Based Testing**

### **10.1 High-Risk Areas**

**[ID: TEST-STRATEGY-006]**

| 风险 | 影响 | 测试优先级 | 缓解措施 |
|------|--------|--------------|-----------|
| Prompt templates 生成不一致的标记 | High | P0 | 广泛的手动测试，reviewer templates 验证标记 |
| Tag parser 遗漏标记或行号错误 | High | P0 | 全面的单元测试，edge case 测试 |
| 循环依赖检测失败 | Medium | P1 | 使用已知循环案例的单元测试 |
| Impact analysis 发现太多误报 | Medium | P1 | 使用真实场景的集成测试 |
| Workflows 不清晰或不完整 | High | P0 | Dog-fooding，用户测试 |

---

## **十一、Summary**

### **11.1 Test Deliverables**

**[ID: TEST-SUMMARY-001]**

1. **Manual Test Suite**：所有 prompt templates 和 workflows 的测试用例
2. **Automated Test Suite**：所有 Python scripts 的 pytest 测试
3. **Performance Benchmarks**：性能关键操作的 benchmark suite
4. **CI/CD Pipeline**：自动化测试的 GitHub Actions workflow
5. **Test Coverage Report**：显示 > 90% 覆盖率的 HTML 报告

---

### **11.2 Exit Criteria**

**[ID: TEST-SUMMARY-002]**

测试完成的标准：
- ✅ 所有 prompt templates 生成正确的文档（手动验证）
- ✅ 所有 workflows 清晰可执行（通过 dog-fooding 验证）
- ✅ 所有 Python scripts 通过单元测试，覆盖率 > 90%
- ✅ 性能 benchmarks 达到目标（100K LOC < 1 分钟）
- ✅ Dog-fooding 成功（SpecGovernor 管理自身）
- ✅ Helper scripts 零 critical bugs
- ✅ 所有测试用例已记录并执行

---

**Test Plan Document Complete**
