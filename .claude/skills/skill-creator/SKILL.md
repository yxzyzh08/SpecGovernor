---
name: skill-creator
description: Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.
---

# Skill Creator

这个 skill 提供创建高质量 skills 的完整指南。

## 关于 Skills

Skills 是模块化、自包含的扩展包，通过提供专业知识、工作流程和工具来扩展 Claude 的能力。可以将它们视为特定领域或任务的"入职指南"——它们将 Claude 从通用代理转变为配备了模型无法完全掌握的程序化知识的专业代理。

### Skills 提供什么

1. **专业工作流程** - 特定领域的多步骤流程
2. **工具集成** - 处理特定文件格式或 API 的说明
3. **领域专业知识** - 公司特定知识、架构、业务逻辑
4. **捆绑资源** - 用于复杂和重复任务的脚本、参考资料和资产

## 核心原则

### 语言要求

**创建的 skill 必须使用中文输出文档内容。**

所有 skill 的输出文档（包括 SKILL.md、references/ 中的参考文档、以及生成的任何文档）都应该使用中文编写，以确保本项目团队成员能够轻松理解和使用。

**例外情况**：
- **专业术语和行业术语**可以使用英文（如：Campaign Proposal、KPI、API、RESTful 等）
- **代码、变量名、函数名**必须使用英文（遵循编程规范）
- **技术关键词**可以保留英文（如：Vue.js、React、LocalStorage、Vuex 等）
- **YAML frontmatter 字段**必须使用英文（如：name、description 等，这是系统要求）

**示例**：
```markdown
# Campaign Proposal 管理模块

本模块提供营销活动策划案的创建和管理功能。

## 数据模型

Campaign Proposal 实体包含以下字段：
- id: 唯一标识符
- title: 策划案标题
- strategies: 营销策略列表
```

**不正确的示例**：
```markdown
# Campaign Proposal Management Module

This module provides creation and management functionality for campaign proposals.

## Data Model

The Campaign Proposal entity includes the following fields:
- id: Unique identifier
- title: Proposal title
- strategies: Marketing strategy list
```

### 简洁至上

上下文窗口是公共资源。Skills 与 Claude 需要的其他所有内容共享上下文窗口：系统提示、对话历史、其他 Skills 的元数据以及实际的用户请求。

**默认假设：Claude 已经非常聪明。** 只添加 Claude 还没有的上下文。挑战每条信息："Claude 真的需要这个解释吗？"和"这段话值得它的 token 成本吗？"

优先使用简洁的示例而不是冗长的解释。

### 设置适当的自由度

根据任务的脆弱性和可变性匹配具体程度：

**高自由度（基于文本的说明）**：当多种方法都有效、决策取决于上下文或启发式指导方法时使用。

**中等自由度（带参数的伪代码或脚本）**：当存在首选模式、可以接受一些变化或配置影响行为时使用。

**低自由度（特定脚本、少量参数）**：当操作脆弱且容易出错、一致性至关重要或必须遵循特定顺序时使用。

将 Claude 想象成探索一条路径：有悬崖的狭窄桥梁需要特定的护栏（低自由度），而开阔的田野允许多条路线（高自由度）。

### Skill 的结构

每个 skill 由必需的 SKILL.md 文件和可选的捆绑资源组成：

```
skill-name/
├── SKILL.md (必需)
│   ├── YAML frontmatter 元数据（必需）
│   │   ├── name: (必需)
│   │   └── description: (必需)
│   └── Markdown 说明（必需）
└── 捆绑资源（可选）
    ├── scripts/          - 可执行代码（Python/Bash/等）
    ├── references/       - 需要时加载到上下文中的文档
    └── assets/           - 输出中使用的文件（模板、图标、字体等）
```

#### SKILL.md（必需）

每个 SKILL.md 包含：

- **Frontmatter**（YAML）：包含 `name` 和 `description` 字段。这些是 Claude 用来决定何时使用该 skill 的唯一字段，因此清楚全面地描述 skill 是什么以及何时使用它非常重要。
- **Body**（Markdown）：使用 skill 的说明和指导。仅在 skill 触发后加载（如果有的话）。

#### 捆绑资源（可选）

##### Scripts（`scripts/`）

用于需要确定性可靠性或反复重写的任务的可执行代码（Python/Bash/等）。

- **何时包含**：当相同的代码被反复重写或需要确定性可靠性时
- **示例**：用于 PDF 旋转任务的 `scripts/rotate_pdf.py`
- **优势**：token 高效、确定性、可以在不加载到上下文中的情况下执行
- **注意**：脚本可能仍需要被 Claude 读取以进行修补或环境特定的调整

##### References（`references/`）

旨在根据需要加载到上下文中以告知 Claude 的流程和思考的文档和参考资料。

- **何时包含**：用于 Claude 在工作时应该参考的文档
- **示例**：用于财务架构的 `references/finance.md`、用于公司 NDA 模板的 `references/mnda.md`、用于公司政策的 `references/policies.md`、用于 API 规范的 `references/api_docs.md`
- **使用场景**：数据库架构、API 文档、领域知识、公司政策、详细的工作流程指南
- **优势**：保持 SKILL.md 精简，仅在 Claude 确定需要时加载
- **最佳实践**：如果文件很大（>10k 字），在 SKILL.md 中包含 grep 搜索模式
- **避免重复**：信息应该存在于 SKILL.md 或 references 文件中，而不是两者都有。对于详细信息，优先使用 references 文件，除非它对 skill 真正核心——这样可以保持 SKILL.md 精简，同时使信息可发现而不占用上下文窗口。仅在 SKILL.md 中保留基本的程序指令和工作流程指导；将详细的参考资料、架构和示例移至 references 文件。

##### Assets（`assets/`）

不打算加载到上下文中，而是在 Claude 生成的输出中使用的文件。

- **何时包含**：当 skill 需要将在最终输出中使用的文件时
- **示例**：用于品牌资产的 `assets/logo.png`、用于 PowerPoint 模板的 `assets/slides.pptx`、用于 HTML/React 样板的 `assets/frontend-template/`、用于排版的 `assets/font.ttf`
- **使用场景**：模板、图像、图标、样板代码、字体、被复制或修改的样本文档
- **优势**：将输出资源与文档分开，使 Claude 能够使用文件而无需将它们加载到上下文中

#### 不要在 Skill 中包含什么

一个 skill 应该只包含直接支持其功能的基本文件。不要创建多余的文档或辅助文件，包括：

- README.md
- INSTALLATION_GUIDE.md
- QUICK_REFERENCE.md
- CHANGELOG.md
- 等等

skill 应该只包含 AI 代理完成手头工作所需的信息。它不应该包含有关创建它的过程、设置和测试程序、面向用户的文档等的辅助上下文。创建额外的文档文件只会增加混乱和困惑。

### 渐进式披露设计原则

Skills 使用三级加载系统来有效管理上下文：

1. **元数据（name + description）** - 始终在上下文中（~100 字）
2. **SKILL.md body** - 当 skill 触发时（<5k 字）
3. **捆绑资源** - 根据 Claude 的需要（无限制，因为脚本可以在不读取到上下文窗口的情况下执行）

#### 渐进式披露模式

将 SKILL.md body 保持在要点并在 500 行以下以最小化上下文膨胀。接近此限制时将内容拆分为单独的文件。将内容拆分到其他文件时，从 SKILL.md 中引用它们并清楚地描述何时阅读它们非常重要，以确保 skill 的阅读者知道它们存在以及何时使用它们。

**关键原则：** 当一个 skill 支持多个变体、框架或选项时，在 SKILL.md 中只保留核心工作流程和选择指导。将特定于变体的详细信息（模式、示例、配置）移至单独的参考文件中。

**模式 1：带参考的高级指南**

```markdown
# PDF 处理

## 快速开始

使用 pdfplumber 提取文本：
[代码示例]

## 高级功能

- **表单填充**：完整指南见 [FORMS.md](FORMS.md)
- **API 参考**：所有方法见 [REFERENCE.md](REFERENCE.md)
- **示例**：常见模式见 [EXAMPLES.md](EXAMPLES.md)
```

Claude 仅在需要时加载 FORMS.md、REFERENCE.md 或 EXAMPLES.md。

**模式 2：特定领域组织**

```markdown
# 数据库查询

使用时根据数据库类型阅读相应的参考文件：
- PostgreSQL：[POSTGRES.md](POSTGRES.md)
- MySQL：[MYSQL.md](MYSQL.md)
- MongoDB：[MONGODB.md](MONGODB.md)
```

## 创建 Skill 的流程

### 六步流程

1. 通过具体示例理解 skill
2. 规划可重用的 skill 内容
3. 初始化 skill
4. 编辑 skill（实现资源并编写 SKILL.md）
5. 打包 skill（运行 package_skill.py）
6. 基于实际使用迭代

按顺序遵循这些步骤，仅在有明确理由不适用时才跳过。

### 步骤 1：通过具体示例理解 Skill

仅当已经清楚理解 skill 的使用模式时才跳过此步骤。即使在处理现有 skill 时，它仍然有价值。

要创建有效的 skill，需要清楚理解如何使用该 skill 的具体示例。这种理解可以来自直接的用户示例或通过用户反馈验证的生成示例。

例如，在构建图像编辑器 skill 时，相关问题包括：

- "图像编辑器 skill 应该支持什么功能？编辑、旋转、还有其他吗？"
- "你能给一些如何使用这个 skill 的示例吗？"
- "我可以想象用户要求诸如'从这张图片中去除红眼'或'旋转这张图片'之类的事情。你还能想象这个 skill 被以其他方式使用吗？"
- "用户会说什么来触发这个 skill？"

为避免让用户不知所措，避免在单个消息中问太多问题。从最重要的问题开始，根据需要跟进以提高有效性。

当清楚了解 skill 应该支持的功能时，结束此步骤。

### 步骤 2：规划可重用的 Skill 内容

要将具体示例转化为有效的 skill，通过以下方式分析每个示例：

1. 考虑如何从头执行示例
2. 识别在反复执行这些工作流程时有用的脚本、参考和资产

示例：当构建 `pdf-editor` skill 以处理诸如"帮我旋转这个 PDF"之类的查询时，分析显示：

1. 旋转 PDF 需要每次重写相同的代码
2. `scripts/rotate_pdf.py` 脚本将有助于存储在 skill 中

示例：当设计 `frontend-webapp-builder` skill 以处理诸如"构建一个待办事项应用"或"构建一个仪表板来跟踪我的步数"之类的查询时，分析显示：

1. 编写前端 webapp 每次都需要相同的样板 HTML/React
2. 包含样板 HTML/React 项目文件的 `assets/hello-world/` 模板将有助于存储在 skill 中

示例：当构建 `big-query` skill 以处理诸如"今天有多少用户登录？"之类的查询时，分析显示：

1. 查询 BigQuery 需要每次重新发现表架构和关系
2. 记录表架构的 `references/schema.md` 文件将有助于存储在 skill 中

要建立 skill 的内容，分析每个具体示例以创建要包含的可重用资源列表：脚本、参考和资产。

### 步骤 3：初始化 Skill

此时，是时候实际创建 skill 了。

仅当正在开发的 skill 已经存在并且需要迭代或打包时，才跳过此步骤。在这种情况下，继续下一步。

从头创建新 skill 时，始终运行 `init_skill.py` 脚本。该脚本方便地生成一个新的模板 skill 目录，自动包含 skill 所需的所有内容，使 skill 创建过程更加高效和可靠。

用法：

```bash
scripts/init_skill.py <skill-name> --path <output-directory>
```

脚本：

- 在指定路径创建 skill 目录
- 生成带有适当 frontmatter 和 TODO 占位符的 SKILL.md 模板
- 创建示例资源目录：`scripts/`、`references/` 和 `assets/`
- 在每个目录中添加可以自定义或删除的示例文件

初始化后，根据需要自定义或删除生成的 SKILL.md 和示例文件。

### 步骤 4：编辑 Skill

编辑（新生成或现有的）skill 时，请记住正在为另一个 Claude 实例创建 skill。包括对 Claude 有益且非显而易见的信息。考虑哪些程序化知识、特定领域的详细信息或可重用资产将帮助另一个 Claude 实例更有效地执行这些任务。

#### 学习已验证的设计模式

根据你的 skill 需求咨询这些有用的指南：

- **多步骤流程**：有关顺序工作流程和条件逻辑，请参阅 references/workflows.md
- **特定输出格式或质量标准**：有关模板和示例模式，请参阅 references/output-patterns.md

这些文件包含有效 skill 设计的既定最佳实践。

#### 从可重用的 Skill 内容开始

要开始实施，从上面识别的可重用资源开始：`scripts/`、`references/` 和 `assets/` 文件。请注意，此步骤可能需要用户输入。例如，在实施 `brand-guidelines` skill 时，用户可能需要提供要存储在 `assets/` 中的品牌资产或模板，或要存储在 `references/` 中的文档。

添加的脚本必须通过实际运行来测试，以确保没有错误并且输出与预期匹配。如果有许多类似的脚本，只需要测试代表性样本以确保它们都能正常工作，同时平衡完成时间。

不需要的任何示例文件和目录都应该删除。初始化脚本在 `scripts/`、`references/` 和 `assets/` 中创建示例文件以演示结构，但大多数 skills 不需要所有这些文件。

#### 更新 SKILL.md

**写作指南：**
- 始终使用祈使句/不定式形式
- **必须使用中文编写**（除了专业术语、代码、技术关键词和 YAML frontmatter 字段）

##### Frontmatter

编写带有 `name` 和 `description` 的 YAML frontmatter：

- `name`：skill 名称
- `description`：这是你的 skill 的主要触发机制，帮助 Claude 理解何时使用该 skill。
  - 包括 Skill 的功能和使用时机的具体触发器/上下文。
  - 在此处包含所有"何时使用"信息 - 不在正文中。正文仅在触发后加载，因此正文中的"何时使用此 Skill"部分对 Claude 没有帮助。
  - `docx` skill 的描述示例："全面的文档创建、编辑和分析，支持跟踪更改、注释、格式保留和文本提取。当 Claude 需要处理专业文档（.docx 文件）时使用：（1）创建新文档，（2）修改或编辑内容，（3）处理跟踪更改，（4）添加注释，或任何其他文档任务"

不要在 YAML frontmatter 中包含任何其他字段。

##### Body

编写使用 skill 及其捆绑资源的说明。

### 步骤 5：打包 Skill

skill 开发完成后，必须将其打包成可分发的 .skill 文件与用户共享。打包过程会自动首先验证 skill 以确保它满足所有要求：

```bash
scripts/package_skill.py <path/to/skill-folder>
```

可选输出目录规范：

```bash
scripts/package_skill.py <path/to/skill-folder> ./dist
```

打包脚本将：

1. **验证** skill，自动检查：

   - YAML frontmatter 格式和必需字段
   - Skill 命名约定和目录结构
   - 描述完整性和质量
   - 文件组织和资源引用

2. **打包** skill（如果验证通过），创建以 skill 命名的 .skill 文件（例如 `my-skill.skill`），其中包括所有文件并维护适当的目录结构以进行分发。.skill 文件是具有 .skill 扩展名的 zip 文件。

如果验证失败，脚本将报告错误并退出而不创建包。修复任何验证错误并再次运行打包命令。

### 步骤 6：迭代

测试 skill 后，用户可能会请求改进。这通常发生在使用 skill 之后，对 skill 的表现有新的上下文。

**迭代工作流程：**

1. 在实际任务上使用 skill
2. 注意困难或低效之处
3. 识别应如何更新 SKILL.md 或捆绑资源
4. 实施更改并再次测试

## 最佳实践总结

### 编写高质量的 SKILL.md

1. **使用中文编写**：所有文档内容必须使用中文（专业术语、代码、技术关键词除外）
2. **保持简洁**：只包含 Claude 不知道的信息
3. **使用示例**：优先使用简洁的代码示例而不是长篇解释
4. **结构化内容**：使用清晰的标题和部分组织信息
5. **引用资源**：清楚地引用 references/ 和 scripts/ 中的文件
6. **避免重复**：不要在 SKILL.md 和 references 文件中重复信息

### 组织捆绑资源

1. **Scripts**：存储需要确定性执行的代码
2. **References**：存储详细的文档和参考资料
3. **Assets**：存储输出中使用的模板和文件
4. **删除未使用的文件**：清理初始化时创建的示例文件

### 编写有效的 Description

description 字段是触发 skill 的关键。包括：

- **功能说明**：skill 做什么
- **使用场景**：何时使用（具体触发器）
- **文件类型**：如果相关，明确提及文件扩展名
- **关键功能**：列出主要能力

示例：
```yaml
description: Comprehensive spreadsheet creation, editing, and analysis with support for formulas, formatting, data analysis, and visualization. When Claude needs to work with spreadsheets (.xlsx, .xlsm, .csv, .tsv, etc) for: (1) Creating new spreadsheets with formulas and formatting, (2) Reading or analyzing data, (3) Modify existing spreadsheets while preserving formulas, (4) Data analysis and visualization in spreadsheets, or (5) Recalculating formulas
```

## 常见问题

**Q: SKILL.md 应该多长？**
A: 保持在 500 行以下。如果更长，将内容拆分为 references/ 文件。

**Q: 何时使用 scripts/ vs references/?**
A: 使用 scripts/ 存储需要执行的代码，使用 references/ 存储 Claude 应该阅读的文档。

**Q: 如何测试 skill？**
A: 在实际任务上使用它，注意 Claude 在哪里遇到困难，并相应地迭代。

**Q: 是否应该包含 README.md？**
A: 不应该。仅包含 SKILL.md 和必要的资源文件。

**Q: 如何处理多个变体或选项？**
A: 在 SKILL.md 中保留核心工作流程和选择指导，将特定于变体的详细信息移至 references/ 文件。
