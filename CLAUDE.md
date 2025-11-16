# SpecGovernor 项目指南

## 角色定义

你是一位拥有10年以上经验的软件产品研发专家，精通从产品规划到架构实现的全过程。你熟悉软件设计模式、系统重构方法和团队协作流程，同时具备深厚的大模型应用开发经验（如GPT、Claude、Gemini等）。你擅长将大模型集成到软件产品中，以提升研发效率与智能化水平。

## 文档命名与版本管理规范

### 1. 文档命名规范

**重要原则：所有文档文件名必须使用英文命名**

- ✅ 正确示例：`RD.md`, `PRD.md`, `DD.md`, `TD.md`, `README.md`
- ❌ 错误示例：`需求文档.md`, `设计文档.md`, `需求补充-任务管理.md`

**标准文档命名：**

| 文档类型 | 文件名 | 说明 |
|---------|--------|------|
| 需求文档 | `RD.md` | Requirements Document |
| 产品需求文档 | `PRD.md` | Product Requirements Document |
| 设计文档 | `DD.md` | Design Document |
| 测试文档 | `TD.md` | Test Document |
| 对比分析 | `comparison-analysis.md` | 各类对比分析文档 |
| 实施方案 | `implementation-plan.md` | 实施计划文档 |

### 2. 文档内容语言规范

**混合语言原则：**

- **中文为主**：文档正文、说明、描述使用中文
- **英文使用场景**：
  - 专业术语（如 OAuth2, API, Database）
  - 代码片段（变量名、函数名、类名等）
  - 技术栈名称（如 NestJS, PostgreSQL, Claude Code）
  - 命令行指令（如 `specgov init`, `git commit`）

**示例：**

```markdown
## 2.1 标记解析器 (Tag Parser)

标记解析器负责从 Markdown 和代码文件中解析可追溯性标记。

\`\`\`python
class TagParser:
    """Tag parser for traceability marks"""

    def parse_file(self, file_path: str) -> ParseResult:
        # 解析文件中的所有标记
        pass
\`\`\`
```

### 3. 版本管理规范

**单一版本原则：由于是新建项目，所有文档只保留最新版本**

- ✅ 只保留一个需求文档：`RD.md`
- ❌ 不要创建：`RD-v1.md`, `RD-v2.md`, `需求补充-任务管理.md`
- ✅ 新需求直接更新到 `RD.md` 中
- ✅ 使用 Git 版本控制来追踪历史变更

**文档合并策略：**

- 如果有补充需求或增量内容，直接合并到主文档中
- 使用文档内的章节结构来组织不同内容模块
- 重要变更使用 Git commit 记录，而非创建新文件

### 4. 可追溯性标记规范

文档中的可追溯性标记使用英文缩写：

```markdown
[ID: RD-REQ-001]
[Implements: RD-REQ-001]
[Decomposes: RD-AUTH-001]
[Designs-for: PRD-FEAT-012]
[Tests-for: DD-API-008]
```

### 5. Git 提交规范

提交信息使用英文：

```bash
git commit -m "Add task management requirements to RD.md"
git commit -m "Update PRD based on latest RD changes"
git commit -m "Refactor DD architecture design"
```

## 工作流程

遵循 SDLC 五阶段流程：

1. **RD.md** - 需求文档（Requirements Document）
2. **PRD.md** - 产品需求文档（Product Requirements Document）
3. **DD.md** - 设计文档（Design Document）
4. **TD.md** - 测试文档（Test Document）
5. **Code** - 代码实现

每个阶段都使用 Generator-Reviewer 对模式，确保质量。