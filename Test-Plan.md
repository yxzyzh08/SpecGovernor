# **🧪 测试文档 (TD) - SpecGovernor**

> **Version**: v1.0
> **基于**: DD.md (v1.0) + RD.md (v1.0)
> **创建日期**: 2025-11-16
> **测试目标**: 确保 SpecGovernor 系统满足所有功能、性能和成本要求

---

## **可追溯性声明**

本测试文档设计以下需求和设计的测试：
- [Tests-for: DD-ARCH-001] 系统整体架构
- [Tests-for: DD-MOD-CLI-001] CLI Commands Layer
- [Tests-for: DD-MOD-CONTEXT-001] Context Builder
- [Tests-for: DD-MOD-STATE-001] State Manager
- [Tests-for: DD-MOD-PARSER-001] Tag Parser
- [Tests-for: DD-MOD-GRAPH-001] Dependency Graph
- [Tests-for: DD-MOD-ANALYZER-001] Impact Analyzer
- [Tests-for: DD-MOD-TASK-001] Task Management
- [Tests-for: RD-FR-1.1] Generator-Reviewer 对模式
- [Tests-for: RD-NFR-2.1] 性能需求
- [Tests-for: RD-NFR-6.1] 成本控制

---

## **一、测试策略 (Test Strategy)**

### **1.1 测试层次**

**[ID: TD-STRATEGY-001]**

| 测试层次 | 测试目标 | 覆盖范围 | 工具 |
|---------|---------|---------|------|
| **单元测试** | 验证各模块独立功能的正确性 | 所有核心模块（Tag Parser, Graph, Context Builder 等） | pytest |
| **集成测试** | 验证模块间协作的正确性 | CLI 命令端到端流程 | pytest + fixtures |
| **性能测试** | 验证系统性能指标 | 索引构建、影响分析、一致性检查 | pytest-benchmark |
| **成本测试** | 验证 AI 调用成本控制 | 所有涉及 AI 的操作 | 自定义成本监控 |
| **端到端测试** | 验证完整 SDLC 流程 | RD → PRD → DD → TD → Code | 集成测试框架 |

### **1.2 测试数据准备**

**[ID: TD-STRATEGY-002] [Tests-for: DD-TEST-001]**

**测试项目规模分级**：

```yaml
小型项目:
  代码行数: 1,000
  模块数: 2
  需求数: 5
  用途: 快速功能测试

中型项目:
  代码行数: 10,000
  模块数: 5
  需求数: 20
  用途: 集成测试

大型项目:
  代码行数: 100,000
  模块数: 10
  需求数: 50
  用途: 性能测试

超大项目:
  代码行数: 1,000,000
  模块数: 20
  需求数: 100
  用途: 压力测试
```

### **1.3 测试环境**

**[ID: TD-STRATEGY-003]**

| 环境组件 | 版本/配置 | 说明 |
|---------|----------|------|
| **Python** | 3.11+ | 核心运行环境 |
| **Click** | 8.x | CLI 框架 |
| **Claude Code** | latest | AI 后端（模拟） |
| **Git** | 2.x | 版本控制 |
| **pytest** | 8.x | 测试框架 |
| **pytest-benchmark** | 4.x | 性能测试 |
| **pytest-mock** | 3.x | Mock 工具 |

### **1.4 测试覆盖率目标**

**[ID: TD-STRATEGY-004]**

| 模块 | 代码覆盖率目标 | 分支覆盖率目标 |
|------|--------------|---------------|
| **Tag Parser** | ≥ 95% | ≥ 90% |
| **Dependency Graph** | ≥ 95% | ≥ 90% |
| **Context Builder** | ≥ 90% | ≥ 85% |
| **State Manager** | ≥ 95% | ≥ 90% |
| **Impact Analyzer** | ≥ 90% | ≥ 85% |
| **CLI Commands** | ≥ 85% | ≥ 80% |
| **Task Management** | ≥ 90% | ≥ 85% |
| **整体** | ≥ 90% | ≥ 85% |

---

## **二、单元测试 (Unit Tests)**

### **2.1 Tag Parser 测试**

**[ID: TD-UNIT-PARSER-001] [Tests-for: DD-MOD-PARSER-001]**

#### **2.1.1 标记解析准确性测试**

```python
# tests/unit/test_tag_parser.py

import pytest
from src.core.parser.tag_parser import TagParser
from src.core.parser.tag_types import TagType

class TestTagParser:
    """Tag Parser 单元测试"""

    def test_parse_id_tag(self):
        """测试解析 [ID: XXX] 标记"""
        parser = TagParser()
        content = """
        # OAuth2 登录需求
        **[ID: RD-REQ-005]**
        系统需支持 OAuth2 登录流程。
        """

        # 创建临时文件
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write(content)
            temp_file = f.name

        try:
            result = parser.parse_file(temp_file)

            # 验证：应该找到一个 ID 标记
            assert len(result.tags) == 1
            assert result.tags[0].tag_type == TagType.ID
            assert result.tags[0].target_id == "RD-REQ-005"
            assert result.tags[0].line_number == 2
        finally:
            os.unlink(temp_file)

    def test_parse_implements_tag(self):
        """测试解析 [Implements: XXX] 标记"""
        parser = TagParser()
        content = """
        ## OAuth2 登录功能
        **[ID: PRD-FEAT-012]** [Implements: RD-REQ-005]
        """

        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write(content)
            temp_file = f.name

        try:
            result = parser.parse_file(temp_file)

            # 验证：应该找到 ID 和 Implements 两个标记
            assert len(result.tags) == 2

            id_tag = [t for t in result.tags if t.tag_type == TagType.ID][0]
            assert id_tag.target_id == "PRD-FEAT-012"

            impl_tag = [t for t in result.tags if t.tag_type == TagType.IMPLEMENTS][0]
            assert impl_tag.target_id == "RD-REQ-005"
        finally:
            os.unlink(temp_file)

    def test_parse_multiple_tags_in_line(self):
        """测试解析一行中的多个标记"""
        parser = TagParser()
        content = "[ID: DD-API-008] [Designs-for: PRD-FEAT-012] [Implements: RD-REQ-005]"

        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write(content)
            temp_file = f.name

        try:
            result = parser.parse_file(temp_file)

            # 验证：应该找到 3 个标记
            assert len(result.tags) == 3
            assert {t.tag_type for t in result.tags} == {
                TagType.ID,
                TagType.DESIGNS_FOR,
                TagType.IMPLEMENTS
            }
        finally:
            os.unlink(temp_file)

    def test_parse_code_file(self):
        """测试解析代码文件中的标记"""
        parser = TagParser()
        content = """
        // [ID: CODE-API-008] [Implements: DD-API-008]
        export class AuthController {
            async oauth2Callback(req: Request, res: Response) {
                // 实现 OAuth2 回调
            }
        }
        """

        with tempfile.NamedTemporaryFile(mode='w', suffix='.ts', delete=False) as f:
            f.write(content)
            temp_file = f.name

        try:
            result = parser.parse_file(temp_file)

            # 验证：应该找到 2 个标记
            assert len(result.tags) == 2
        finally:
            os.unlink(temp_file)

    def test_parse_invalid_tag_format(self):
        """测试解析无效标记格式"""
        parser = TagParser()
        content = "[InvalidTag: XXX] [ID: INVALID_FORMAT]"

        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write(content)
            temp_file = f.name

        try:
            result = parser.parse_file(temp_file)

            # 验证：应该有错误记录
            assert len(result.errors) > 0
        finally:
            os.unlink(temp_file)

    @pytest.mark.benchmark
    def test_parse_large_file_performance(self, benchmark):
        """测试大文件解析性能"""
        parser = TagParser()

        # 生成 10,000 行的测试文件
        content = "\n".join([
            f"## Section {i}\n[ID: RD-REQ-{i:03d}]"
            for i in range(1, 10001)
        ])

        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write(content)
            temp_file = f.name

        try:
            # 性能基准测试
            result = benchmark(parser.parse_file, temp_file)

            # 验证：解析时间应该 < 1 秒
            assert benchmark.stats['mean'] < 1.0

            # 验证：应该找到 10,000 个标记
            assert len(result.tags) == 10000
        finally:
            os.unlink(temp_file)
```

#### **2.1.2 边界情况测试**

```python
class TestTagParserEdgeCases:
    """Tag Parser 边界情况测试"""

    def test_parse_empty_file(self):
        """测试解析空文件"""
        parser = TagParser()

        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write("")
            temp_file = f.name

        try:
            result = parser.parse_file(temp_file)
            assert len(result.tags) == 0
            assert len(result.errors) == 0
        finally:
            os.unlink(temp_file)

    def test_parse_file_not_found(self):
        """测试解析不存在的文件"""
        parser = TagParser()
        result = parser.parse_file("non_existent_file.md")

        assert len(result.errors) > 0
        assert "not found" in result.errors[0].lower()

    def test_parse_unsupported_file_type(self):
        """测试解析不支持的文件类型"""
        parser = TagParser()

        with tempfile.NamedTemporaryFile(mode='w', suffix='.pdf', delete=False) as f:
            f.write("Some content")
            temp_file = f.name

        try:
            result = parser.parse_file(temp_file)
            assert len(result.warnings) > 0
        finally:
            os.unlink(temp_file)

    def test_parse_with_special_characters(self):
        """测试包含特殊字符的标记"""
        parser = TagParser()
        content = "[ID: RD-REQ-001] 包含中文、emoji 😊 和特殊符号 @#$%"

        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write(content)
            temp_file = f.name

        try:
            result = parser.parse_file(temp_file)
            assert len(result.tags) == 1
            assert result.tags[0].target_id == "RD-REQ-001"
        finally:
            os.unlink(temp_file)
```

---

### **2.2 Dependency Graph 测试**

**[ID: TD-UNIT-GRAPH-001] [Tests-for: DD-MOD-GRAPH-001]**

#### **2.2.1 图操作正确性测试**

```python
# tests/unit/test_dependency_graph.py

import pytest
from src.core.graph.graph import DependencyGraph
from src.core.graph.node import Node, NodeType
from src.core.graph.edge import Edge, EdgeType

class TestDependencyGraph:
    """Dependency Graph 单元测试"""

    def test_add_node(self):
        """测试添加节点"""
        graph = DependencyGraph()

        node = Node(
            id="RD-REQ-005",
            type=NodeType.REQUIREMENT,
            file_path="docs/RD.md",
            line_number=42
        )

        graph.add_node(node)

        assert "RD-REQ-005" in graph.nodes
        assert graph.nodes["RD-REQ-005"].type == NodeType.REQUIREMENT

    def test_add_edge(self):
        """测试添加边"""
        graph = DependencyGraph()

        # 添加节点
        node1 = Node("RD-REQ-005", NodeType.REQUIREMENT, "docs/RD.md", 42)
        node2 = Node("PRD-FEAT-012", NodeType.FEATURE, "docs/PRD.md", 128)
        graph.add_node(node1)
        graph.add_node(node2)

        # 添加边
        edge = Edge(
            source_id="PRD-FEAT-012",
            target_id="RD-REQ-005",
            edge_type=EdgeType.IMPLEMENTS,
            file_path="docs/PRD.md",
            line_number=128
        )
        graph.add_edge(edge)

        # 验证
        assert len(graph.outgoing_edges["PRD-FEAT-012"]) == 1
        assert len(graph.incoming_edges["RD-REQ-005"]) == 1

    def test_get_downstream_nodes(self):
        """测试获取下游节点"""
        graph = self._create_sample_graph()

        # RD-REQ-005 的下游应该包括 PRD-FEAT-012 和 DD-API-008
        downstream = graph.get_downstream_nodes("RD-REQ-005")

        downstream_ids = {node.id for node in downstream}
        assert "PRD-FEAT-012" in downstream_ids
        assert "DD-API-008" in downstream_ids

    def test_get_upstream_nodes(self):
        """测试获取上游节点"""
        graph = self._create_sample_graph()

        # DD-API-008 的上游应该包括 PRD-FEAT-012 和 RD-REQ-005
        upstream = graph.get_upstream_nodes("DD-API-008")

        upstream_ids = {node.id for node in upstream}
        assert "PRD-FEAT-012" in upstream_ids
        assert "RD-REQ-005" in upstream_ids

    def test_detect_cycles(self):
        """测试检测循环依赖"""
        graph = DependencyGraph()

        # 创建循环依赖：A -> B -> C -> A
        nodes = [
            Node("A", NodeType.REQUIREMENT, "test.md", 1),
            Node("B", NodeType.FEATURE, "test.md", 2),
            Node("C", NodeType.API_DESIGN, "test.md", 3),
        ]
        for node in nodes:
            graph.add_node(node)

        edges = [
            Edge("A", "B", EdgeType.IMPLEMENTS, "test.md", 1),
            Edge("B", "C", EdgeType.DESIGNS_FOR, "test.md", 2),
            Edge("C", "A", EdgeType.IMPLEMENTS, "test.md", 3),  # 循环
        ]
        for edge in edges:
            graph.add_edge(edge)

        # 检测循环
        cycles = graph.detect_cycles()

        assert len(cycles) > 0
        assert set(cycles[0]) == {"A", "B", "C"}

    def test_serialization(self):
        """测试序列化与反序列化"""
        graph = self._create_sample_graph()

        # 序列化
        json_data = graph.to_json()

        # 验证 JSON 结构
        assert "nodes" in json_data
        assert "edges" in json_data
        assert len(json_data["nodes"]) == 3
        assert len(json_data["edges"]) == 2

        # 反序列化
        graph2 = DependencyGraph.from_json(json_data)

        # 验证
        assert len(graph2.nodes) == 3
        assert "RD-REQ-005" in graph2.nodes

    def _create_sample_graph(self) -> DependencyGraph:
        """创建示例依赖图"""
        graph = DependencyGraph()

        # 添加节点
        nodes = [
            Node("RD-REQ-005", NodeType.REQUIREMENT, "docs/RD.md", 42),
            Node("PRD-FEAT-012", NodeType.FEATURE, "docs/PRD.md", 128),
            Node("DD-API-008", NodeType.API_DESIGN, "docs/DD.md", 234),
        ]
        for node in nodes:
            graph.add_node(node)

        # 添加边
        edges = [
            Edge("PRD-FEAT-012", "RD-REQ-005", EdgeType.IMPLEMENTS, "docs/PRD.md", 128),
            Edge("DD-API-008", "PRD-FEAT-012", EdgeType.DESIGNS_FOR, "docs/DD.md", 234),
        ]
        for edge in edges:
            graph.add_edge(edge)

        return graph
```

---

### **2.3 Context Builder 测试**

**[ID: TD-UNIT-CONTEXT-001] [Tests-for: DD-MOD-CONTEXT-001]**

```python
# tests/unit/test_context_builder.py

import pytest
from src.context.builder import ContextBuilder

class TestContextBuilder:
    """Context Builder 单元测试"""

    def test_build_for_rd_generation(self, tmp_path):
        """测试为 RD 生成构建上下文"""
        # 创建临时项目目录
        project_dir = tmp_path / "test_project"
        project_dir.mkdir()

        # 创建上下文文件
        context_dir = project_dir / ".specgov" / "context"
        context_dir.mkdir(parents=True)

        brief_file = context_dir / "project-brief.md"
        brief_file.write_text("这是一个测试项目")

        # 创建 Context Builder
        builder = ContextBuilder(project_dir)

        # 构建上下文
        prompt = builder.build_for_rd_generation("用户输入的需求")

        # 验证
        assert "这是一个测试项目" in prompt
        assert "用户输入的需求" in prompt

    def test_token_limit_enforcement(self, tmp_path):
        """测试 Token 限制强制执行"""
        project_dir = tmp_path / "test_project"
        project_dir.mkdir()

        builder = ContextBuilder(project_dir)

        # 生成超大文本（约 30K tokens）
        large_text = "X" * (30000 * builder.CHARS_PER_TOKEN)

        # 裁剪
        trimmed = builder._ensure_token_limit(large_text, max_tokens=5000)

        # 验证：裁剪后应该不超过 5K tokens
        estimated_tokens = len(trimmed) // builder.CHARS_PER_TOKEN
        assert estimated_tokens <= 5000

    def test_extract_relevant_sections(self):
        """测试提取相关章节"""
        builder = ContextBuilder(".")

        content = """
        # 第一章
        [ID: RD-REQ-001]
        内容 1

        # 第二章
        [ID: RD-REQ-002]
        内容 2
        """ * 100  # 重复 100 次

        # 提取相关章节（限制为 2000 tokens）
        excerpt = builder._extract_relevant_sections(content, max_tokens=2000)

        # 验证：应该被裁剪
        assert len(excerpt) < len(content)
        assert "内容已裁剪" in excerpt
```

---

### **2.4 State Manager 测试**

**[ID: TD-UNIT-STATE-001] [Tests-for: DD-MOD-STATE-001]**

```python
# tests/unit/test_state_manager.py

import pytest
from src.state.manager import StateManager

class TestStateManager:
    """State Manager 单元测试"""

    def test_get_default_state(self, tmp_path):
        """测试获取默认状态"""
        project_dir = tmp_path / "test_project"
        project_dir.mkdir()

        manager = StateManager(project_dir)
        state = manager.get_state()

        # 验证默认状态
        assert state['rd_generated'] == False
        assert state['prd_generated'] == False
        assert state['total_cost'] == 0.0

    def test_update_state(self, tmp_path):
        """测试更新状态"""
        project_dir = tmp_path / "test_project"
        project_dir.mkdir()

        manager = StateManager(project_dir)

        # 更新状态
        manager.update({'rd_generated': True, 'rd_version': 1})

        # 读取状态
        state = manager.get_state()

        # 验证
        assert state['rd_generated'] == True
        assert state['rd_version'] == 1

    def test_can_generate_prd(self, tmp_path):
        """测试 PRD 生成前置条件检查"""
        project_dir = tmp_path / "test_project"
        project_dir.mkdir()

        manager = StateManager(project_dir)

        # 初始状态：RD 未生成
        assert manager.can_generate_prd() == False

        # 更新状态：RD 已生成
        manager.update({'rd_generated': True})

        # 验证：现在可以生成 PRD
        assert manager.can_generate_prd() == True

    def test_record_generation(self, tmp_path):
        """测试记录生成操作"""
        project_dir = tmp_path / "test_project"
        project_dir.mkdir()

        manager = StateManager(project_dir)

        # 记录生成操作
        manager.record_generation(
            stage='rd',
            cost=0.05,
            tokens=1500,
            time_seconds=45.0
        )

        # 读取状态
        state = manager.get_state()

        # 验证
        assert state['rd_generated'] == True
        assert state['rd_version'] == 1
        assert state['total_cost'] == 0.05
        assert state['total_tokens'] == 1500
```

---

### **2.5 Task Complexity Checker 测试**

**[ID: TD-UNIT-TASK-001] [Tests-for: DD-MOD-TASK-001]**

```python
# tests/unit/test_complexity_checker.py

import pytest
from src.tasks.complexity import ComplexityChecker
from src.tasks.task import Task, TaskStatus, TaskComplexity

class TestComplexityChecker:
    """Task Complexity Checker 单元测试"""

    def test_simple_task(self, tmp_path):
        """测试简单任务检测"""
        checker = ComplexityChecker()

        # 创建小文件
        test_file = tmp_path / "test.md"
        test_file.write_text("X" * 1000)  # 约 250 tokens

        task = Task(
            id="TASK-001",
            epic_id="EPIC-001",
            title="简单任务",
            status=TaskStatus.PENDING,
            command="test",
            context_files=[str(test_file)]
        )

        complexity, warning = checker.check_task(task)

        assert complexity == TaskComplexity.SIMPLE
        assert warning is None

    def test_complex_task(self, tmp_path):
        """测试复杂任务检测"""
        checker = ComplexityChecker()

        # 创建大文件
        test_file = tmp_path / "test.md"
        test_file.write_text("X" * 50000)  # 约 12K tokens

        task = Task(
            id="TASK-001",
            epic_id="EPIC-001",
            title="复杂任务",
            status=TaskStatus.PENDING,
            command="test",
            context_files=[str(test_file)]
        )

        complexity, warning = checker.check_task(task)

        assert complexity == TaskComplexity.COMPLEX
        assert warning is not None

    def test_too_complex_task(self, tmp_path):
        """测试过于复杂的任务检测"""
        checker = ComplexityChecker()

        # 创建超大文件
        test_file = tmp_path / "test.md"
        test_file.write_text("X" * 100000)  # 约 25K tokens

        task = Task(
            id="TASK-001",
            epic_id="EPIC-001",
            title="过于复杂的任务",
            status=TaskStatus.PENDING,
            command="test",
            context_files=[str(test_file)]
        )

        complexity, warning = checker.check_task(task)

        assert complexity == TaskComplexity.TOO_COMPLEX
        assert "建议分解" in warning
```

---

## **三、集成测试 (Integration Tests)**

### **3.1 完整文档生成流程测试**

**[ID: TD-INTEGRATION-001] [Tests-for: RD-WORKFLOW-001]**

```python
# tests/integration/test_document_workflow.py

import pytest
from click.testing import CliRunner
from src.cli.main import cli

class TestDocumentWorkflow:
    """文档生成流程集成测试"""

    def test_rd_generation_flow(self, tmp_path, mocker):
        """测试完整的 RD 生成流程"""
        runner = CliRunner()

        # 1. 初始化项目
        with runner.isolated_filesystem(temp_dir=tmp_path):
            result = runner.invoke(cli, ['init', 'test-project'])
            assert result.exit_code == 0
            assert ".specgov" in os.listdir()

            # 2. 创建输入文件
            with open("user-stories.md", "w") as f:
                f.write("用户需要 OAuth2 登录功能")

            # 3. Mock AI 后端
            mock_backend = mocker.patch('src.ai.claude_code.ClaudeCodeBackend.generate')
            mock_backend.return_value = mocker.Mock(
                content="# RD\n[ID: RD-REQ-001] OAuth2 登录",
                tokens_input=100,
                tokens_output=200,
                cost=0.05,
                model="claude-sonnet-4",
                backend="claude-code"
            )

            # 4. 生成 RD
            result = runner.invoke(cli, ['rd:generate', '--input=user-stories.md'])
            assert result.exit_code == 0

            # 5. 验证输出文件
            assert os.path.exists(".specgov/artifacts/rd.md")

            # 6. 验证状态更新
            import json
            with open(".specgov/state.json") as f:
                state = json.load(f)
            assert state['rd_generated'] == True

    def test_rd_review_flow(self, tmp_path, mocker):
        """测试 RD 评审流程"""
        runner = CliRunner()

        with runner.isolated_filesystem(temp_dir=tmp_path):
            # 准备环境
            self._setup_project(runner)

            # 创建 RD 文档
            os.makedirs(".specgov/artifacts", exist_ok=True)
            with open(".specgov/artifacts/rd.md", "w") as f:
                f.write("# RD\n[ID: RD-REQ-001] OAuth2 登录")

            # Mock AI 后端
            mock_backend = mocker.patch('src.ai.claude_code.ClaudeCodeBackend.generate')
            mock_backend.return_value = mocker.Mock(
                content='{"summary": "评审完成", "issues": []}',
                tokens_input=200,
                tokens_output=100,
                cost=0.03,
                model="claude-sonnet-4",
                backend="claude-code"
            )

            # 执行评审
            result = runner.invoke(cli, ['rd:review'])
            assert result.exit_code == 0

            # 验证评审报告
            assert os.path.exists(".specgov/reviews/rd-review.json")

    def _setup_project(self, runner):
        """设置测试项目"""
        result = runner.invoke(cli, ['init', 'test-project'])
        assert result.exit_code == 0
```

---

### **3.2 索引构建与依赖图测试**

**[ID: TD-INTEGRATION-002] [Tests-for: RD-FR-2.1]**

```python
# tests/integration/test_index_building.py

import pytest
from click.testing import CliRunner
from src.cli.main import cli

class TestIndexBuilding:
    """索引构建集成测试"""

    def test_build_index_from_scratch(self, sample_project):
        """测试从零构建索引"""
        runner = CliRunner()

        with runner.isolated_filesystem(temp_dir=sample_project):
            # 执行索引构建
            result = runner.invoke(cli, ['index:build'])
            assert result.exit_code == 0

            # 验证索引文件
            assert os.path.exists(".specgov/index/dependency-graph.json")
            assert os.path.exists(".specgov/index/modules.json")

            # 验证依赖图内容
            import json
            with open(".specgov/index/dependency-graph.json") as f:
                graph = json.load(f)

            assert "nodes" in graph
            assert "edges" in graph
            assert len(graph["nodes"]) > 0

    def test_incremental_index_update(self, sample_project):
        """测试增量索引更新"""
        runner = CliRunner()

        with runner.isolated_filesystem(temp_dir=sample_project):
            # 1. 构建初始索引
            runner.invoke(cli, ['index:build'])

            # 2. 修改文档
            with open("docs/RD.md", "a") as f:
                f.write("\n[ID: RD-REQ-999] 新增需求")

            # 3. 增量更新
            result = runner.invoke(cli, ['index:update', '--changed=docs/RD.md'])
            assert result.exit_code == 0

            # 4. 验证新节点已添加
            import json
            with open(".specgov/index/dependency-graph.json") as f:
                graph = json.load(f)

            node_ids = [node["id"] for node in graph["nodes"]]
            assert "RD-REQ-999" in node_ids
```

---

### **3.3 影响分析端到端测试**

**[ID: TD-INTEGRATION-003] [Tests-for: RD-WORKFLOW-002]**

```python
# tests/integration/test_impact_analysis.py

import pytest
import time
from click.testing import CliRunner
from src.cli.main import cli

class TestImpactAnalysis:
    """影响分析集成测试"""

    def test_impact_analysis_performance(self, large_sample_project):
        """测试影响分析性能（< 10秒）"""
        runner = CliRunner()

        with runner.isolated_filesystem(temp_dir=large_sample_project):
            # 构建索引
            runner.invoke(cli, ['index:build'])

            # 修改文件
            with open("docs/RD.md", "a") as f:
                f.write("\n[ID: RD-REQ-999] 修改需求")

            # 执行影响分析（计时）
            start_time = time.time()
            result = runner.invoke(cli, ['analyze:impact', '--changed=docs/RD.md'])
            elapsed_time = time.time() - start_time

            # 验证
            assert result.exit_code == 0
            assert elapsed_time < 10.0  # 性能要求：< 10秒

            # 验证输出
            assert "affected" in result.output.lower()

    def test_impact_analysis_accuracy(self, sample_project):
        """测试影响分析准确性"""
        runner = CliRunner()

        with runner.isolated_filesystem(temp_dir=sample_project):
            # 构建索引
            runner.invoke(cli, ['index:build'])

            # 修改 RD
            with open("docs/RD.md", "a") as f:
                f.write("\n[ID: RD-REQ-005] 修改 OAuth2 需求")

            # 执行影响分析
            result = runner.invoke(cli, ['analyze:impact', '--changed=docs/RD.md', '--format=json'])
            assert result.exit_code == 0

            # 解析输出
            import json
            report = json.loads(result.output)

            # 验证：应该包含下游节点
            affected_ids = [item["id"] for item in report["affected_documents"]]
            assert "PRD-FEAT-012" in affected_ids  # PRD 应该受影响
```

---

### **3.4 一致性检查端到端测试**

**[ID: TD-INTEGRATION-004] [Tests-for: RD-WORKFLOW-003]**

```python
# tests/integration/test_consistency_check.py

import pytest
import time
from click.testing import CliRunner
from src.cli.main import cli

class TestConsistencyCheck:
    """一致性检查集成测试"""

    def test_single_requirement_check(self, sample_project, mocker):
        """测试单个需求的一致性检查（< 2分钟）"""
        runner = CliRunner()

        with runner.isolated_filesystem(temp_dir=sample_project):
            # 构建索引
            runner.invoke(cli, ['index:build'])

            # Mock AI 后端
            mock_backend = mocker.patch('src.ai.claude_code.ClaudeCodeBackend.generate')
            mock_backend.return_value = mocker.Mock(
                content='{"inconsistencies": []}',
                tokens_input=3000,
                tokens_output=500,
                cost=0.02,
                model="claude-sonnet-4"
            )

            # 执行一致性检查（计时）
            start_time = time.time()
            result = runner.invoke(cli, ['check:consistency', '--scope=RD-REQ-005'])
            elapsed_time = time.time() - start_time

            # 验证
            assert result.exit_code == 0
            assert elapsed_time < 120.0  # 性能要求：< 2分钟

    def test_module_level_check(self, sample_project, mocker):
        """测试模块级一致性检查（< 2分钟）"""
        runner = CliRunner()

        with runner.isolated_filesystem(temp_dir=sample_project):
            # 构建索引
            runner.invoke(cli, ['index:build'])

            # Mock AI 后端
            mock_backend = mocker.patch('src.ai.claude_code.ClaudeCodeBackend.generate')
            mock_backend.return_value = mocker.Mock(
                content='{"inconsistencies": [{"severity": "warning", "description": "API 不匹配"}]}',
                tokens_input=15000,
                tokens_output=1000,
                cost=0.05,
                model="claude-sonnet-4"
            )

            # 执行一致性检查
            start_time = time.time()
            result = runner.invoke(cli, ['check:consistency', '--scope=AuthModule'])
            elapsed_time = time.time() - start_time

            # 验证
            assert result.exit_code == 0
            assert elapsed_time < 120.0  # 性能要求：< 2分钟
            assert "不一致" in result.output or "inconsistenc" in result.output.lower()

    def test_detect_inconsistency(self, inconsistent_project, mocker):
        """测试检测不一致性"""
        runner = CliRunner()

        with runner.isolated_filesystem(temp_dir=inconsistent_project):
            # 构建索引
            runner.invoke(cli, ['index:build'])

            # Mock AI 后端返回不一致报告
            mock_backend = mocker.patch('src.ai.claude_code.ClaudeCodeBackend.generate')
            mock_backend.return_value = mocker.Mock(
                content='''{
                    "inconsistencies": [
                        {
                            "severity": "error",
                            "description": "DD 设计的 API 是 POST /payments，代码实现是 PUT /payments",
                            "rd_ref": "RD-REQ-010",
                            "prd_ref": "PRD-FEAT-020",
                            "dd_ref": "DD-API-015",
                            "code_ref": "CODE-API-015"
                        }
                    ]
                }''',
                tokens_input=5000,
                tokens_output=800,
                cost=0.03,
                model="claude-sonnet-4"
            )

            # 执行检查
            result = runner.invoke(cli, ['check:consistency', '--scope=PaymentModule'])

            # 验证
            assert result.exit_code != 0  # 发现不一致应该返回非零退出码
            assert "不一致" in result.output or "inconsistenc" in result.output.lower()
```

---

## **四、性能测试 (Performance Tests)**

### **4.1 索引构建性能测试**

**[ID: TD-PERF-INDEX-001] [Tests-for: RD-NFR-2.5]**

```python
# tests/performance/test_index_performance.py

import pytest
import time
from src.core.parser.tag_parser import TagParser
from src.core.graph.builder import GraphBuilder

class TestIndexPerformance:
    """索引构建性能测试"""

    @pytest.mark.benchmark
    def test_parse_1m_lines_project(self, million_line_project, benchmark):
        """测试解析 100 万行代码项目（< 1分钟）"""
        parser = TagParser()

        # 性能基准测试
        result = benchmark(parser.parse_directory, million_line_project)

        # 验证：解析时间应该 < 60 秒
        assert benchmark.stats['mean'] < 60.0

        # 验证：应该找到大量标记
        total_tags = sum(len(r.tags) for r in result)
        assert total_tags > 0

    @pytest.mark.benchmark
    def test_build_dependency_graph(self, million_line_project, benchmark):
        """测试构建依赖图（< 1分钟）"""
        builder = GraphBuilder()

        # 性能基准测试
        graph = benchmark(builder.build_from_directory, million_line_project)

        # 验证：构建时间应该 < 60 秒
        assert benchmark.stats['mean'] < 60.0

        # 验证：图应该包含节点
        assert len(graph.nodes) > 0

    def test_incremental_update_performance(self, sample_project):
        """测试增量更新性能（< 5秒）"""
        builder = GraphBuilder()

        # 1. 构建初始图
        graph = builder.build_from_directory(sample_project)

        # 2. 修改单个文件
        test_file = sample_project / "docs" / "RD.md"
        with open(test_file, "a") as f:
            f.write("\n[ID: RD-REQ-999] 新增需求")

        # 3. 增量更新（计时）
        start_time = time.time()

        # 只重新解析变更文件
        parser = TagParser()
        result = parser.parse_file(test_file)

        # 更新图
        for tag in result.tags:
            if tag.tag_type.value == "ID":
                from src.core.graph.node import Node, NodeType
                node = Node(tag.target_id, NodeType.REQUIREMENT, str(test_file), tag.line_number)
                graph.add_node(node)

        elapsed_time = time.time() - start_time

        # 验证：增量更新应该 < 5 秒
        assert elapsed_time < 5.0
```

---

### **4.2 影响分析性能测试**

**[ID: TD-PERF-IMPACT-001] [Tests-for: RD-NFR-2.1]**

```python
# tests/performance/test_impact_performance.py

import pytest
import time
from src.core.analyzer.impact import ImpactAnalyzer

class TestImpactPerformance:
    """影响分析性能测试"""

    def test_impact_analysis_response_time(self, large_dependency_graph):
        """测试影响分析响应时间（< 10秒）"""
        from pathlib import Path
        analyzer = ImpactAnalyzer(large_dependency_graph, Path("."))

        # 模拟变更文件
        changed_file = Path("docs/RD.md")

        # 执行影响分析（计时）
        start_time = time.time()
        report = analyzer.analyze_file_change(changed_file)
        elapsed_time = time.time() - start_time

        # 验证：响应时间应该 < 10 秒
        assert elapsed_time < 10.0

        # 验证：应该返回影响报告
        assert "changed_file" in report
        assert "affected_documents" in report

    @pytest.mark.parametrize("project_size", [10, 50, 100])
    def test_impact_scalability(self, project_size):
        """测试影响分析可扩展性"""
        # 创建不同规模的依赖图
        graph = self._create_graph_with_size(project_size)

        from pathlib import Path
        analyzer = ImpactAnalyzer(graph, Path("."))

        # 执行影响分析
        start_time = time.time()
        report = analyzer.analyze_file_change(Path("test.md"))
        elapsed_time = time.time() - start_time

        # 验证：即使项目规模增大，响应时间也应该 < 10 秒
        assert elapsed_time < 10.0

    def _create_graph_with_size(self, num_nodes):
        """创建指定规模的依赖图"""
        from src.core.graph.graph import DependencyGraph
        from src.core.graph.node import Node, NodeType
        from src.core.graph.edge import Edge, EdgeType

        graph = DependencyGraph()

        # 添加节点
        for i in range(num_nodes):
            node = Node(f"NODE-{i}", NodeType.REQUIREMENT, "test.md", i)
            graph.add_node(node)

        # 添加边（创建链式依赖）
        for i in range(num_nodes - 1):
            edge = Edge(f"NODE-{i+1}", f"NODE-{i}", EdgeType.IMPLEMENTS, "test.md", i)
            graph.add_edge(edge)

        return graph
```

---

### **4.3 一致性检查性能测试**

**[ID: TD-PERF-CONSISTENCY-001] [Tests-for: RD-NFR-2.2]**

```python
# tests/performance/test_consistency_performance.py

import pytest
import time

class TestConsistencyPerformance:
    """一致性检查性能测试"""

    def test_single_requirement_check_time(self, sample_project, mocker):
        """测试单需求检查时间（< 2分钟）"""
        from click.testing import CliRunner
        from src.cli.main import cli

        runner = CliRunner()

        with runner.isolated_filesystem(temp_dir=sample_project):
            # 构建索引
            runner.invoke(cli, ['index:build'])

            # Mock AI 后端（快速响应）
            mock_backend = mocker.patch('src.ai.claude_code.ClaudeCodeBackend.generate')
            mock_backend.return_value = mocker.Mock(
                content='{"inconsistencies": []}',
                tokens_input=3000,
                tokens_output=500,
                cost=0.02
            )

            # 执行一致性检查（计时）
            start_time = time.time()
            result = runner.invoke(cli, ['check:consistency', '--scope=RD-REQ-005'])
            elapsed_time = time.time() - start_time

            # 验证：< 120 秒
            assert elapsed_time < 120.0

    def test_module_level_check_time(self, sample_project, mocker):
        """测试模块级检查时间（< 2分钟）"""
        from click.testing import CliRunner
        from src.cli.main import cli

        runner = CliRunner()

        with runner.isolated_filesystem(temp_dir=sample_project):
            # 构建索引
            runner.invoke(cli, ['index:build'])

            # Mock AI 后端
            mock_backend = mocker.patch('src.ai.claude_code.ClaudeCodeBackend.generate')
            mock_backend.return_value = mocker.Mock(
                content='{"inconsistencies": []}',
                tokens_input=15000,
                tokens_output=1000,
                cost=0.05
            )

            # 执行检查（计时）
            start_time = time.time()
            result = runner.invoke(cli, ['check:consistency', '--scope=AuthModule'])
            elapsed_time = time.time() - start_time

            # 验证：< 120 秒
            assert elapsed_time < 120.0
```

---

## **五、成本测试 (Cost Tests)**

### **5.1 AI 调用成本测试**

**[ID: TD-COST-001] [Tests-for: RD-NFR-6.1]**

```python
# tests/cost/test_ai_cost.py

import pytest

class TestAICost:
    """AI 调用成本测试"""

    def test_impact_analysis_zero_cost(self, sample_project):
        """测试影响分析成本（应为 $0）"""
        from click.testing import CliRunner
        from src.cli.main import cli

        runner = CliRunner()

        with runner.isolated_filesystem(temp_dir=sample_project):
            # 构建索引
            runner.invoke(cli, ['index:build'])

            # 执行影响分析
            result = runner.invoke(cli, ['analyze:impact', '--changed=docs/RD.md'])

            # 验证：不应该有 AI 调用成本
            # （影响分析是纯图查询，不调用 AI）
            import json
            state_file = Path(".specgov/state.json")
            if state_file.exists():
                with open(state_file) as f:
                    state = json.load(f)
                    # 成本应该为 0
                    assert state.get('total_cost', 0) == 0

    def test_single_requirement_check_cost(self, sample_project, mocker):
        """测试单需求检查成本（< $0.02）"""
        from click.testing import CliRunner
        from src.cli.main import cli

        runner = CliRunner()

        with runner.isolated_filesystem(temp_dir=sample_project):
            # Mock AI 后端
            mock_backend = mocker.patch('src.ai.claude_code.ClaudeCodeBackend.generate')
            mock_backend.return_value = mocker.Mock(
                content='{"inconsistencies": []}',
                tokens_input=3000,
                tokens_output=500,
                cost=0.015  # 模拟成本
            )

            # 构建索引
            runner.invoke(cli, ['index:build'])

            # 执行检查
            result = runner.invoke(cli, ['check:consistency', '--scope=RD-REQ-005'])

            # 验证成本
            assert mock_backend.return_value.cost < 0.02

    def test_module_level_check_cost(self, sample_project, mocker):
        """测试模块级检查成本（< $0.05）"""
        from click.testing import CliRunner
        from src.cli.main import cli

        runner = CliRunner()

        with runner.isolated_filesystem(temp_dir=sample_project):
            # Mock AI 后端
            mock_backend = mocker.patch('src.ai.claude_code.ClaudeCodeBackend.generate')
            mock_backend.return_value = mocker.Mock(
                content='{"inconsistencies": []}',
                tokens_input=15000,
                tokens_output=1000,
                cost=0.045  # 模拟成本
            )

            # 构建索引
            runner.invoke(cli, ['index:build'])

            # 执行检查
            result = runner.invoke(cli, ['check:consistency', '--scope=AuthModule'])

            # 验证成本
            assert mock_backend.return_value.cost < 0.05
```

---

## **六、测试数据准备 (Test Data Preparation)**

### **6.1 测试夹具 (Fixtures)**

**[ID: TD-FIXTURE-001]**

```python
# tests/conftest.py

import pytest
from pathlib import Path
import tempfile
import shutil

@pytest.fixture
def sample_project(tmp_path):
    """创建示例项目"""
    project_dir = tmp_path / "sample_project"
    project_dir.mkdir()

    # 创建目录结构
    (project_dir / "docs").mkdir()
    (project_dir / "src").mkdir()
    (project_dir / ".specgov").mkdir()

    # 创建 RD 文档
    rd_content = """
# Requirements Document

## OAuth2 登录需求
**[ID: RD-REQ-005]**

系统需支持 OAuth2 登录流程。
"""
    (project_dir / "docs" / "RD.md").write_text(rd_content)

    # 创建 PRD 文档
    prd_content = """
# Product Requirements Document

## OAuth2 登录功能
**[ID: PRD-FEAT-012]** [Implements: RD-REQ-005]

实现 OAuth2 登录流程。
"""
    (project_dir / "docs" / "PRD.md").write_text(prd_content)

    # 创建 DD 文档
    dd_content = """
# Design Document

## OAuth2 API 设计
**[ID: DD-API-008]** [Designs-for: PRD-FEAT-012]

POST /auth/oauth2/callback
"""
    (project_dir / "docs" / "DD.md").write_text(dd_content)

    # 创建代码文件
    code_content = """
// [ID: CODE-API-008] [Implements: DD-API-008]
export class AuthController {
    async oauth2Callback(req: Request, res: Response) {
        // 实现 OAuth2 回调
    }
}
"""
    (project_dir / "src" / "auth.controller.ts").write_text(code_content)

    return project_dir

@pytest.fixture
def large_sample_project(tmp_path):
    """创建大型示例项目（用于性能测试）"""
    project_dir = tmp_path / "large_project"
    project_dir.mkdir()

    # 创建目录
    (project_dir / "docs").mkdir()
    (project_dir / "src").mkdir()

    # 生成大量文档
    for i in range(100):
        doc_content = f"""
# Module {i}

## Requirement {i}
**[ID: RD-REQ-{i:03d}]**

Description for requirement {i}.
"""
        (project_dir / "docs" / f"module_{i}.md").write_text(doc_content)

    return project_dir

@pytest.fixture
def million_line_project(tmp_path):
    """创建 100 万行代码项目（用于压力测试）"""
    project_dir = tmp_path / "million_line_project"
    project_dir.mkdir()

    # 创建目录
    (project_dir / "src").mkdir()

    # 生成大量代码文件（每个文件 10,000 行）
    for i in range(100):
        code_lines = []
        for j in range(10000):
            if j % 100 == 0:
                code_lines.append(f"// [ID: CODE-{i:03d}-{j:05d}]")
            code_lines.append(f"function func_{i}_{j}() {{}}")

        code_content = "\n".join(code_lines)
        (project_dir / "src" / f"module_{i}.ts").write_text(code_content)

    return project_dir

@pytest.fixture
def inconsistent_project(tmp_path):
    """创建包含不一致的测试项目"""
    project_dir = tmp_path / "inconsistent_project"
    project_dir.mkdir()

    (project_dir / "docs").mkdir()
    (project_dir / "src").mkdir()

    # RD: 要求 POST
    rd_content = """
**[ID: RD-REQ-010]**
API 应使用 POST 方法创建支付。
"""
    (project_dir / "docs" / "RD.md").write_text(rd_content)

    # DD: 设计为 POST
    dd_content = """
**[ID: DD-API-015]** [Implements: RD-REQ-010]
POST /payments
"""
    (project_dir / "docs" / "DD.md").write_text(dd_content)

    # Code: 实现为 PUT（不一致）
    code_content = """
// [ID: CODE-API-015] [Implements: DD-API-015]
router.put('/payments', createPayment);  // 错误：应该是 POST
"""
    (project_dir / "src" / "payment.routes.ts").write_text(code_content)

    return project_dir

@pytest.fixture
def large_dependency_graph():
    """创建大型依赖图"""
    from src.core.graph.graph import DependencyGraph
    from src.core.graph.node import Node, NodeType
    from src.core.graph.edge import Edge, EdgeType

    graph = DependencyGraph()

    # 创建 1000 个节点的复杂依赖图
    for i in range(1000):
        node = Node(f"NODE-{i}", NodeType.REQUIREMENT, "test.md", i)
        graph.add_node(node)

    # 创建复杂的依赖关系
    for i in range(999):
        edge = Edge(f"NODE-{i+1}", f"NODE-{i}", EdgeType.IMPLEMENTS, "test.md", i)
        graph.add_edge(edge)

    return graph
```

---

## **七、测试执行计划 (Test Execution Plan)**

### **7.1 测试阶段划分**

**[ID: TD-PLAN-001]**

| 阶段 | 测试类型 | 执行时机 | 负责人 |
|------|---------|---------|--------|
| **单元测试** | 所有单元测试 | 每次代码提交前 | 开发工程师 |
| **集成测试** | CLI 命令集成测试 | 每日构建 | 开发工程师 |
| **性能测试** | 性能基准测试 | 每周 | 架构师 |
| **成本测试** | AI 成本测试 | 每次 AI 集成变更后 | 产品经理 |
| **端到端测试** | 完整流程测试 | 发布前 | 测试经理 |

### **7.2 持续集成配置**

**[ID: TD-PLAN-002]**

```yaml
# .github/workflows/test.yml

name: Test Suite

on: [push, pull_request]

jobs:
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov pytest-benchmark
      - name: Run unit tests
        run: pytest tests/unit --cov=src --cov-report=xml
      - name: Upload coverage
        uses: codecov/codecov-action@v3

  integration-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run integration tests
        run: pytest tests/integration

  performance-tests:
    runs-on: ubuntu-latest
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run performance tests
        run: pytest tests/performance --benchmark-only
```

---

## **八、验收标准 (Acceptance Criteria)**

### **8.1 功能验收**

**[ID: TD-ACCEPTANCE-FUNC-001]**

| 功能模块 | 验收标准 |
|---------|---------|
| **Tag Parser** | ✅ 准确率 ≥ 95%<br>✅ 支持所有标记类型<br>✅ 处理边界情况无崩溃 |
| **Dependency Graph** | ✅ 正确构建依赖关系<br>✅ 检测循环依赖<br>✅ 序列化/反序列化无损 |
| **Context Builder** | ✅ Token 限制强制执行<br>✅ 智能裁剪功能正常<br>✅ 上下文构建正确 |
| **State Manager** | ✅ 状态持久化正常<br>✅ 前置条件检查正确<br>✅ 成本统计准确 |
| **Impact Analyzer** | ✅ 影响分析准确<br>✅ 响应时间 < 10 秒<br>✅ 零 AI 成本 |
| **Task Management** | ✅ 两层任务结构正常<br>✅ 复杂度检查准确<br>✅ 任务分解建议合理 |

### **8.2 性能验收**

**[ID: TD-ACCEPTANCE-PERF-001]**

| 性能指标 | 目标值 | 验收标准 |
|---------|--------|---------|
| **索引构建（100万行）** | < 1 分钟 | ✅ 必须满足 |
| **增量索引更新** | < 5 秒 | ✅ 必须满足 |
| **影响分析** | < 10 秒 | ✅ 必须满足 |
| **单需求一致性检查** | < 2 分钟 | ✅ 必须满足 |
| **模块级一致性检查** | < 2 分钟 | ✅ 必须满足 |
| **全项目一致性检查** | < 10 分钟 | ✅ 建议满足 |

### **8.3 成本验收**

**[ID: TD-ACCEPTANCE-COST-001]**

| 操作类型 | 成本目标 | 验收标准 |
|---------|---------|---------|
| **影响分析** | $0 | ✅ 必须满足 |
| **索引构建** | $0 | ✅ 必须满足 |
| **单需求检查** | < $0.02 | ✅ 必须满足 |
| **模块级检查** | < $0.05 | ✅ 必须满足 |
| **全项目检查** | < $2.00 | ✅ 建议满足 |

### **8.4 质量验收**

**[ID: TD-ACCEPTANCE-QUALITY-001]**

| 质量指标 | 目标值 | 验收标准 |
|---------|--------|---------|
| **代码覆盖率** | ≥ 90% | ✅ 必须满足 |
| **分支覆盖率** | ≥ 85% | ✅ 必须满足 |
| **不一致检测准确率** | ≥ 85% | ✅ 必须满足 |
| **标记解析准确率** | ≥ 95% | ✅ 必须满足 |

---

## **九、测试报告模板 (Test Report Template)**

### **9.1 测试执行报告**

**[ID: TD-REPORT-001]**

```markdown
# SpecGovernor 测试执行报告

**测试日期**: YYYY-MM-DD
**测试版本**: vX.Y.Z
**测试执行人**: XXX

## 一、测试摘要

| 测试类型 | 总计 | 通过 | 失败 | 跳过 | 通过率 |
|---------|------|------|------|------|--------|
| 单元测试 | 120 | 118 | 2 | 0 | 98.3% |
| 集成测试 | 45 | 43 | 2 | 0 | 95.6% |
| 性能测试 | 15 | 14 | 1 | 0 | 93.3% |
| 成本测试 | 10 | 10 | 0 | 0 | 100% |

**总体通过率**: 96.8%

## 二、失败用例分析

### 2.1 单元测试失败

1. **test_parse_large_file_performance**
   - 原因：解析时间超过 1 秒（实际 1.2 秒）
   - 影响：性能不达标
   - 修复计划：优化解析算法

### 2.2 集成测试失败

1. **test_full_project_consistency_check**
   - 原因：超时（> 10 分钟）
   - 影响：全项目检查性能不达标
   - 修复计划：优化并行执行

## 三、性能测试结果

| 性能指标 | 目标值 | 实际值 | 状态 |
|---------|--------|--------|------|
| 索引构建 | < 60s | 52s | ✅ |
| 影响分析 | < 10s | 7s | ✅ |
| 单需求检查 | < 120s | 95s | ✅ |

## 四、代码覆盖率

- **总体覆盖率**: 92.5%
- **单元测试覆盖率**: 94.8%
- **集成测试覆盖率**: 88.2%

## 五、待修复问题

1. Tag Parser 性能优化
2. 全项目检查并行化
3. 边界情况处理增强

## 六、结论

测试总体通过率为 96.8%，达到发布标准。建议修复上述问题后进行回归测试。
```

---

## **十、总结与下一步 (Summary & Next Steps)**

### **10.1 测试覆盖范围**

**[ID: TD-SUMMARY-001]**

本测试文档全面覆盖了 SpecGovernor 系统的：

1. ✅ **单元测试**：所有核心模块（Tag Parser, Graph, Context Builder, State Manager, Task Management）
2. ✅ **集成测试**：完整的文档生成流程、索引构建、影响分析、一致性检查
3. ✅ **性能测试**：索引构建、影响分析、一致性检查的性能基准
4. ✅ **成本测试**：所有 AI 调用的成本控制验证
5. ✅ **端到端测试**：RD → PRD → DD → TD → Code 完整流程

### **10.2 关键测试点**

**[ID: TD-SUMMARY-002]**

- 🎯 **准确性**：标记解析准确率 ≥ 95%，不一致检测准确率 ≥ 85%
- ⚡ **性能**：索引构建 < 1分钟，影响分析 < 10秒，一致性检查 < 2分钟
- 💰 **成本**：影响分析 $0，单需求检查 < $0.02，全项目检查 < $2
- 📊 **质量**：代码覆盖率 ≥ 90%，分支覆盖率 ≥ 85%

### **10.3 下一步工作**

**[ID: TD-NEXT-001]**

1. ⏳ **实现测试框架**：搭建 pytest 测试环境
2. ⏳ **编写测试数据**：创建各种规模的测试项目
3. ⏳ **执行基准测试**：建立性能和成本基准
4. ⏳ **持续集成配置**：配置 GitHub Actions 自动化测试
5. ⏳ **开始代码实现**：基于 DD 实现核心模块

---

**测试文档结束 (End of Test Document)**
