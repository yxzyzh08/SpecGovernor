# **Test Plan - SpecGovernor**

> **Version**: v2.0
> **Based on**: Design-Document.md (v2.0) + PRD.md (v2.0)
> **Created**: 2025-11-16
> **Updated**: 2025-11-16
> **Test Goal**: 工具包组件的综合测试策略

---

## **Traceability Declaration**

本 Test Plan 覆盖以下 Design Document 组件：
- [Tests-for: DESIGN-TEMPLATE-STRUCT-001] Prompt Template Structure
- [Tests-for: DESIGN-TEMPLATE-RD-GEN-001] RD Generator Template
- [Tests-for: DESIGN-TEMPLATE-PRD-GEN-001] PRD Generator Template
- [Tests-for: DESIGN-TEMPLATE-DESIGN-GEN-001] Design Document Generator Template
- [Tests-for: DESIGN-TEMPLATE-TEST-GEN-001] Test Plan Generator Template
- [Tests-for: DESIGN-WORKFLOW-OVERVIEW-001] Workflow Overview Document
- [Tests-for: DESIGN-SCRIPT-INIT-001] Project Initialization Script
- [Tests-for: DESIGN-SCRIPT-PARSER-001] Tag Parser Script
- [Tests-for: DESIGN-SCRIPT-GRAPH-001] Dependency Graph Builder Script
- [Tests-for: DESIGN-SCRIPT-IMPACT-001] Impact Analysis Script

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
  - OAuth2 需求带 **[ID: RD-REQ-XXX]** 标记
  - 密码重置需求带 **[ID: RD-REQ-YYY]** 标记
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
  - 新的 2FA 需求添加了新的 **[ID: RD-REQ-ZZZ]** 标记
  - 正确集成到现有结构中

**验证清单：**
- [ ] 原有需求 ID 未改变
- [ ] 新需求有唯一 ID
- [ ] 没有断开的引用
- [ ] 格式一致

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
- [ ] 使用 **[Implements: RD-REQ-XXX]** 链接到 RD
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
   - PRD 使用 [Implements: RD-XXX] 链接到 RD
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
2. 运行：`python path/to/specgov/scripts/init_project.py`
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
2. 运行：`python path/to/specgov/scripts/init_project.py`
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
**[ID: RD-REQ-005] [Decomposes: RD-AUTH-001]**

System must support OAuth2 login.
```

**测试步骤：**
1. 创建包含上述内容的测试 RD.md
2. 运行：`python scripts/parse_tags.py`
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
**[ID: RD-REQ-005] [Decomposes: RD-AUTH-001]**
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
- RD.md 包含 `[ID: RD-REQ-001]`
- PRD.md 包含 `[ID: PRD-FEAT-001] [Implements: RD-REQ-001]`
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
1. 运行：`python scripts/build_graph.py`
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
1. 修改 RD.md（更改需求 [ID: RD-REQ-005]）
2. Git add 并 commit 更改
3. 运行：`python scripts/impact_analysis.py --changed=docs/RD.md`
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
    rd_file.write_text("**[ID: RD-REQ-005]** OAuth2 Login")
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
    rd_file.write_text("**[ID: RD-REQ-005]** OAuth2 Login MODIFIED")

    os.chdir(tmp_path)

    # Run impact analysis
    import impact_analysis
    # ... test analysis output
```

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
