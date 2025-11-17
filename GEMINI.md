# SpecGovernor 项目指南

## 角色定义

你是一位拥有10年以上经验的软件产品研发专家，精通从产品规划到架构实现的全过程。你熟悉软件设计模式、系统重构方法和团队协作流程，同时具备深厚的大模型应用开发经验（如GPT、Claude、Gemini等）。你擅长将大模型集成到软件产品中，以提升研发效率与智能化水平。

## 核心原则

**⚠️ 重要：本项目为活跃开发项目，遵循以下核心原则**

1. **不备份文档**：所有文档修改都直接在原文件上进行，不创建备份文件
2. **不保留历史版本**：不在文件名中添加版本号（如 v1, v2），使用 Git 追踪变更历史
3. **保持简洁清晰**：文档内容力求精简，避免冗余和重复
4. **及时更新**：发现问题立即修改，不拖延不积累技术债
5. **Git 作为唯一历史**：所有变更历史通过 Git commit 记录

**禁止操作：**
- ❌ 创建 `PRD-v1.md`, `PRD-v2.md` 等版本文件
- ❌ 创建 `PRD.md.backup`, `PRD.md.old` 等备份文件
- ❌ 在文档中保留废弃的章节或注释掉的内容
- ❌ 添加冗余的说明或重复的示例

**正确做法：**
- ✅ 直接修改 `PRD.md`，通过 Git commit 记录变更
- ✅ 删除过时内容，不保留在文档中
- ✅ 使用 `git log` 和 `git diff` 查看历史变更

---

## 文档命名与版本管理规范

### 1. 文档命名规范

**重要原则：所有文档文件名必须使用英文命名，必须使用完整名称**

- ✅ 正确示例：`PRD.md`, `Design-Document.md`, `Test-Plan.md`, `README.md`
- ❌ 错误示例：`DD.md`, `TD.md`, `需求文档.md`, `设计文档.md`

**标准文档命名：**

| 文档类型 | 文件名 | 说明 |
|---------|--------|------|
| 产品需求文档 | `PRD.md` | Product Requirements Document |
| 设计文档 | `Design-Document.md` | Design Document（**必须完整名称，不缩写为 DD**） |
| 测试计划 | `Test-Plan.md` | Test Plan（**必须完整名称，不缩写为 TD/TP**） |
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

**单一版本原则：所有文档只保留最新版本**

- ✅ 只保留一个需求文档：`PRD.md`
- ❌ 禁止创建：`PRD-v1.md`, `PRD-v2.md`, `PRD.md.backup`, `需求补充.md`
- ✅ 新需求直接更新到 `PRD.md` 中
- ✅ 使用 Git 版本控制来追踪历史变更
- ✅ 删除过时内容，不保留废弃章节

**文档更新策略：**

- 直接在原文件上修改，立即删除过时内容
- 使用文档内的章节结构来组织不同内容模块
- 所有变更通过 Git commit 记录，提交信息清晰说明变更原因
- 不在文档中保留变更历史或注释掉的旧内容

### 4. 可追溯性标记规范

文档中的可追溯性标记使用英文标识符：

```markdown
[ID: PRD-REQ-001]              # 业务需求
[ID: PRD-FEAT-012]             # 产品功能
[Implements: PRD-REQ-001]      # 实现关系
[Decomposes: PRD-REQ-001]      # 分解关系
[Designs-for: PRD-FEAT-012]    # 设计关系
[Tests-for: DESIGN-API-008]    # 测试关系
```

**标记前缀规范**：
- PRD: `PRD-REQ-`, `PRD-FEAT-`, `PRD-NFR-` 等
- Design: `DESIGN-ARCH-`, `DESIGN-API-`, `DESIGN-DB-` 等
- Test: `TEST-CASE-`, `TEST-PERF-` 等
- Code: `CODE-` 等

### 5. Git 提交规范

提交信息使用英文：

```bash
git commit -m "Add task management requirements to RD.md"
git commit -m "Update PRD based on latest RD changes"
git commit -m "Refactor DD architecture design"
```

## 工作流程

**SpecGovernor v3.0 遵循 4 阶段 SDLC 流程：**

```
PRD → Design Document → Test Plan → Code
```

1. **PRD.md** - 产品需求文档（Product Requirements Document）
   - Part 1: Business Requirements（业务需求）
   - Part 2: Product Features（产品功能）
2. **Design-Document.md** - 设计文档（**完整名称，不缩写**）
3. **Test-Plan.md** - 测试计划（**完整名称，不缩写**）
4. **Code** - 代码实现

**每个阶段都使用 Generator-Reviewer 对模式，确保质量。**

### 可追溯性链

```
PRD-REQ-XXX (业务需求)
    ↓ [Decomposes]
PRD-FEAT-XXX (产品功能)
    ↓ [Implements: PRD-REQ-XXX]
DESIGN-XXX (设计)
    ↓ [Designs-for: PRD-FEAT-XXX]
TEST-XXX (测试)
    ↓ [Tests-for: DESIGN-XXX]
CODE-XXX (代码)
    ↓ [Implements: DESIGN-XXX]
```