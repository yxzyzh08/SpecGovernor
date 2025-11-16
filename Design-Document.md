# **🏗️ SpecGovernor 设计文档 (DD)**

> **版本**: v1.0
> **基于**: PRD.md (v1.0) + 需求补充-任务管理.md (v1.1)
> **创建日期**: 2025-11-16
> **设计目标**: 基于 spec-kit 框架构建 AI 增强型研发流程治理工具

---

## **可追溯性声明**

本文档设计以下 PRD 功能：
- [Designs-for: PRD-EPIC-001] 项目初始化
- [Designs-for: PRD-EPIC-002] 文档生成-评审-修订循环
- [Designs-for: PRD-EPIC-003] 索引构建与依赖图管理
- [Designs-for: PRD-EPIC-004] 影响分析
- [Designs-for: PRD-EPIC-005] 一致性检查
- [Designs-for: RD-TASK-LAYER-001] 两层任务管理
- [Designs-for: RD-TASK-STATE-001] 无状态角色设计

---

## **一、系统架构**

### **1.1 整体架构**

**[ID: DD-ARCH-001]**

```
┌──────────────────────────────────────────────────────────────────┐
│                       SpecGovernor CLI                           │
│                     (基于 spec-kit 改造)                          │
│                                                                  │
│  用户输入：specgov rd:generate --input=user-stories.md          │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│                      CLI Commands Layer                          │
│                      (命令层 - 业务逻辑)                          │
├──────────────────────────────────────────────────────────────────┤
│  rd:generate  │  rd:review  │  prd:generate  │  index:build  │  │
│  check:consistency  │  analyze:impact  │  tasks:next  │  ...    │
│                                                                  │
│  职责：解析命令参数、协调各模块、控制执行流程                      │
└──────────────────────────────────────────────────────────────────┘
          │              │              │              │
          │              │              │              │
    ┌─────▼──────┐  ┌───▼────┐  ┌─────▼─────┐  ┌────▼──────┐
    │  Context   │  │ State  │  │   Core    │  │   Task    │
    │  Builder   │  │ Manager│  │  Engine   │  │   Mgmt    │
    ├────────────┤  ├────────┤  ├───────────┤  ├───────────┤
    │ • 加载背景  │  │ • 读取  │  │ • Tag     │  │ • Epic    │
    │ • 裁剪文档  │  │   状态  │  │   Parser  │  │   Tracker │
    │ • 构建     │  │ • 更新  │  │ • Graph   │  │ • Role    │
    │   提示词    │  │   进度  │  │   Builder │  │   Tasks   │
    │ • 控制     │  │ • 记录  │  │ • Impact  │  │ • Compl-  │
    │   大小     │  │   成本  │  │   Analyzer│  │   exity   │
    │   <5K      │  │        │  │ • Consist │  │   Check   │
    └────────────┘  └────────┘  │   Checker │  └───────────┘
                                └───────────┘
          │              │              │
          └──────────────┼──────────────┘
                         ▼
        ┌────────────────────────────────────┐
        │        Shared Services             │
        ├────────────────┬───────────────────┤
        │   AI Layer     │   Storage Layer   │
        ├────────────────┼───────────────────┤
        │ • Generator    │ • File I/O        │
        │ • Reviewer     │ • Git Ops         │
        │ • AI Backend   │ • JSON/MD         │
        │   (Claude Code)│   Serializer      │
        └────────────────┴───────────────────┘
```

**架构说明**：

1. **CLI Commands Layer（命令层）**
   - 每个命令独立实现业务逻辑
   - 负责协调各个模块完成任务
   - 无需独立的"流程编排器"
   - 直接调用下层服务

2. **Context Builder（上下文构建器）**
   - 加载项目背景（project-brief.md）
   - 从依赖图定位相关节点
   - 裁剪文档片段
   - 构建 AI 提示词（< 5K tokens）

3. **State Manager（状态管理器）**
   - 读写 `.specgov/state.json`
   - 记录任务进度、成本、时间
   - 管理文档版本状态

4. **Core Engine（核心引擎）**
   - Tag Parser: 解析可追溯性标记
   - Graph Builder: 构建依赖图
   - Impact Analyzer: 影响分析
   - Consistency Checker: 一致性检查

5. **Task Management（任务管理）**
   - Epic Tracker: 跟踪高层任务
   - Role Tasks: 管理角色任务
   - Complexity Check: 任务复杂度检查

---

### **1.2 与 spec-kit 的关系**

**[ID: DD-ARCH-002]**

| spec-kit 组件 | 复用策略 | 改造内容 |
|--------------|---------|---------|
| **CLI 框架** (Click) | ✅ 100% 复用 | 无 |
| **AI 抽象层** | ✅ 80% 复用 | 新增 Generator-Reviewer 对模式 |
| **文件操作** | ✅ 90% 复用 | 新增标记解析逻辑 |
| **配置管理** | ✅ 70% 复用 | 扩展配置项（任务管理、AI 后端） |
| **Git 集成** | ✅ 100% 复用 | 无 |

**新增模块（spec-kit 没有）：**
- 标记解析器 (Tag Parser)
- 依赖图引擎 (Dependency Graph)
- 影响分析引擎 (Impact Analyzer)
- 一致性检查引擎 (Consistency Checker)
- 任务管理系统 (Task Management)

---

### **1.3 目录结构设计**

**[ID: DD-ARCH-003]**

```
specgov/                           # 项目根目录
├── src/
│   ├── cli/                       # CLI 层（复用 spec-kit）
│   │   ├── __init__.py
│   │   ├── main.py                # 主入口
│   │   ├── commands/              # 命令实现
│   │   │   ├── init.py
│   │   │   ├── rd.py
│   │   │   ├── prd.py
│   │   │   ├── dd.py
│   │   │   ├── td.py
│   │   │   ├── index.py
│   │   │   ├── analyze.py
│   │   │   ├── check.py
│   │   │   ├── tasks.py           # 新增：任务管理命令
│   │   │   └── role.py            # 新增：角色切换命令
│   │   └── ui/
│   │       ├── formatter.py       # 输出格式化
│   │       └── progress.py        # 进度显示
│   │
│   ├── core/                      # 核心引擎（新增）
│   │   ├── parser/
│   │   │   ├── __init__.py
│   │   │   ├── tag_parser.py      # 标记解析器
│   │   │   └── tag_types.py       # 标记类型定义
│   │   ├── graph/
│   │   │   ├── __init__.py
│   │   │   ├── node.py            # 节点数据结构
│   │   │   ├── edge.py            # 边数据结构
│   │   │   ├── graph.py           # 依赖图
│   │   │   └── builder.py         # 图构建器
│   │   ├── analyzer/
│   │   │   ├── __init__.py
│   │   │   ├── impact.py          # 影响分析
│   │   │   └── consistency.py     # 一致性检查
│   │   └── index/
│   │       ├── __init__.py
│   │       ├── indexer.py         # 索引构建
│   │       └── scanner.py         # 文件扫描
│   │
│   ├── context/                   # 上下文构建器（新增）
│   │   ├── __init__.py
│   │   ├── builder.py             # Context Builder 主逻辑
│   │   ├── loader.py              # 文档加载器
│   │   └── slicer.py              # 文档裁剪器
│   │
│   ├── state/                     # 状态管理器（新增）
│   │   ├── __init__.py
│   │   ├── manager.py             # State Manager 主逻辑
│   │   └── state_types.py         # 状态数据结构
│   │
│   ├── tasks/                     # 任务管理系统（新增）
│   │   ├── __init__.py
│   │   ├── epic.py                # Epic 数据结构
│   │   ├── task.py                # Task 数据结构
│   │   ├── role.py                # Role 定义
│   │   ├── complexity.py          # 任务复杂度检查
│   │   └── decomposer.py          # 任务分解器
│   │
│   ├── ai/                        # AI 层（复用 + 扩展 spec-kit）
│   │   ├── __init__.py
│   │   ├── backend.py             # AI 后端抽象
│   │   ├── claude_code.py         # Claude Code 适配器
│   │   ├── generator.py           # Generator Agent
│   │   ├── reviewer.py            # Reviewer Agent
│   │   └── prompts/               # 提示词模板
│   │       ├── rd_generator.txt
│   │       ├── rd_reviewer.txt
│   │       ├── prd_generator.txt
│   │       └── ...
│   │
│   ├── storage/                   # 存储层（复用 spec-kit）
│   │   ├── __init__.py
│   │   ├── file_ops.py            # 文件操作
│   │   ├── git_ops.py             # Git 操作
│   │   └── serializer.py          # JSON/Markdown 序列化
│   │
│   ├── config/                    # 配置管理（复用 + 扩展）
│   │   ├── __init__.py
│   │   ├── config.py              # 配置加载
│   │   └── defaults.py            # 默认配置
│   │
│   └── utils/                     # 工具函数（复用 spec-kit）
│       ├── __init__.py
│       ├── logger.py
│       └── validators.py
│
├── templates/                     # 模板文件
│   ├── config.yml.template
│   ├── modules.json.template
│   ├── rd-review-checklist.md
│   └── ...
│
├── tests/                         # 测试（复用 spec-kit 框架）
│   ├── unit/
│   ├── integration/
│   └── fixtures/
│
├── pyproject.toml                 # 项目配置
├── README.md
└── LICENSE
```

---

## **二、新增架构模块设计**

### **2.1 CLI Commands Layer（命令层）**

**[ID: DD-MOD-CLI-001]**

#### **2.1.1 设计原则**

CLI Commands Layer 是用户与系统交互的入口，每个命令实现独立的业务逻辑，无需依赖"流程编排器"。

**职责**：
1. 解析命令行参数
2. 协调各模块完成任务
3. 控制执行流程
4. 输出结果给用户

**示例：rd:generate 命令实现**

```python
# src/cli/commands/rd.py

import click
from ...context.builder import ContextBuilder
from ...state.manager import StateManager
from ...ai.generator import GeneratorAgent
from ...ai.claude_code import ClaudeCodeBackend

@click.group()
def rd():
    """RD 阶段命令"""
    pass

@rd.command()
@click.option('--input', type=click.Path(exists=True), help='输入文件')
@click.option('--ai', default='claude-code', help='AI 后端')
@click.option('--output', default='docs/RD.md', help='输出路径')
def generate(input: str, ai: str, output: str):
    """生成需求文档 (RD)

    执行流程：
    1. CLI Command 读取输入文件
    2. 调用 Context Builder 构建 AI 提示词
    3. 调用 Generator Agent 生成文档
    4. 保存结果
    5. 调用 State Manager 更新状态
    """
    click.echo("🤖 RD Generator Agent 正在工作...")

    # 1. 读取输入（CLI Command 的职责）
    input_content = ""
    if input:
        click.echo(f"  读取输入：{input}")
        with open(input, 'r', encoding='utf-8') as f:
            input_content = f.read()

    # 2. 构建上下文（调用 Context Builder）
    click.echo("  构建 AI 上下文...")
    context_builder = ContextBuilder(project_dir='.')
    prompt = context_builder.build_for_rd_generation(input_content)

    # 3. 调用 AI（调用 Generator Agent）
    click.echo(f"  调用 AI：{ai} (claude-sonnet-4)")
    backend = ClaudeCodeBackend()
    generator = GeneratorAgent(backend, stage='rd')
    result = generator.generate(prompt)

    # 4. 保存结果（CLI Command 的职责）
    click.echo("  保存文档...")
    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.content, encoding='utf-8')

    # 5. 更新状态（调用 State Manager）
    state_mgr = StateManager(project_dir='.')
    state_mgr.update({
        'rd_generated': True,
        'rd_version': 1,
        'last_generation_time': datetime.now(),
        'tokens_used': result.tokens_input + result.tokens_output,
        'cost': result.cost
    })

    # 6. 输出统计信息
    click.echo(f"✓ 生成完成：{output}")
    click.echo(f"\n📊 统计：")
    click.echo(f"  - 生成时间：{result.generation_time}秒")
    click.echo(f"  - 成本：${result.cost:.2f}")
    click.echo(f"\n📚 下一步：")
    click.echo("  运行 specgov rd:review 进行评审")
```

**关键点**：
- ✅ 命令自己负责业务逻辑
- ✅ 调用其他模块作为服务
- ✅ 无需独立的"编排器"
- ✅ 清晰的职责划分

---

### **2.2 Context Builder（上下文构建器）**

**[ID: DD-MOD-CONTEXT-001]**

#### **2.2.1 设计目标**

Context Builder 负责为 AI Agent 构建精准的上下文，确保：
1. 上下文大小 < 5K tokens
2. 包含所有必要信息
3. 裁剪无关内容

#### **2.2.2 核心实现**

```python
# src/context/builder.py

from pathlib import Path
from typing import Dict, List
from ..core.graph.graph import DependencyGraph

class ContextBuilder:
    """上下文构建器

    负责：
    1. 加载项目背景
    2. 从依赖图定位相关节点
    3. 裁剪文档片段
    4. 构建 AI 提示词
    5. 控制上下文大小 < 5K tokens
    """

    # Token 估算（粗略）
    CHARS_PER_TOKEN = 4
    MAX_CONTEXT_TOKENS = 5000

    def __init__(self, project_dir: str | Path):
        self.project_dir = Path(project_dir)
        self.context_dir = self.project_dir / '.specgov' / 'context'

    def build_for_rd_generation(self, input_content: str) -> str:
        """为 RD 生成构建上下文"""

        # 1. 加载项目简介（永久背景）
        project_brief = self._load_project_brief()

        # 2. 加载 RD Generator 提示词模板
        template = self._load_prompt_template('rd_generator')

        # 3. 构建完整提示词
        prompt = template.format(
            project_brief=project_brief,
            input_content=input_content
        )

        # 4. 检查并裁剪（如果超出）
        prompt = self._ensure_token_limit(prompt)

        return prompt

    def build_for_prd_generation(self, rd_content: str) -> str:
        """为 PRD 生成构建上下文

        需要加载：
        1. 项目简介
        2. RD 文档（裁剪）
        3. PRD Generator 提示词模板
        """

        # 1. 加载项目简介
        project_brief = self._load_project_brief()

        # 2. 裁剪 RD 文档（智能提取相关部分）
        rd_excerpt = self._extract_relevant_sections(
            rd_content,
            max_tokens=2000  # RD 最多占 2K tokens
        )

        # 3. 加载提示词模板
        template = self._load_prompt_template('prd_generator')

        # 4. 构建提示词
        prompt = template.format(
            project_brief=project_brief,
            rd_content=rd_excerpt
        )

        # 5. 检查并裁剪
        prompt = self._ensure_token_limit(prompt)

        return prompt

    def build_for_consistency_check(
        self,
        scope_id: str,
        dependency_graph: DependencyGraph
    ) -> str:
        """为一致性检查构建上下文

        步骤：
        1. 从依赖图定位依赖链
        2. 加载依赖链涉及的文档和代码
        3. 智能裁剪（< 20K tokens for consistency check）
        """

        # 1. 获取依赖链
        chain = self._get_dependency_chain(scope_id, dependency_graph)

        # 2. 加载每个节点的内容
        context_parts = []
        for node in chain:
            content = self._load_node_content(node)
            context_parts.append(f"## {node.id} ({node.type})\n{content}")

        # 3. 合并并裁剪
        full_context = "\n\n".join(context_parts)
        full_context = self._ensure_token_limit(
            full_context,
            max_tokens=20000  # 一致性检查允许更多上下文
        )

        return full_context

    def _load_project_brief(self) -> str:
        """加载项目简介"""
        brief_file = self.context_dir / 'project-brief.md'
        if brief_file.exists():
            return brief_file.read_text(encoding='utf-8')
        return ""

    def _load_prompt_template(self, template_name: str) -> str:
        """加载提示词模板"""
        template_file = Path(__file__).parent.parent / 'ai' / 'prompts' / f'{template_name}.txt'
        return template_file.read_text(encoding='utf-8')

    def _extract_relevant_sections(self, content: str, max_tokens: int) -> str:
        """智能提取相关章节

        策略：
        1. 保留标题和第一段
        2. 保留所有可追溯性标记
        3. 裁剪详细描述
        """
        # 简化实现：直接截断
        max_chars = max_tokens * self.CHARS_PER_TOKEN
        if len(content) > max_chars:
            return content[:max_chars] + "\n\n[... 内容已裁剪 ...]"
        return content

    def _ensure_token_limit(self, text: str, max_tokens: int = None) -> str:
        """确保文本不超过 token 限制"""
        if max_tokens is None:
            max_tokens = self.MAX_CONTEXT_TOKENS

        max_chars = max_tokens * self.CHARS_PER_TOKEN
        if len(text) > max_chars:
            return text[:max_chars] + "\n\n[... 上下文已自动裁剪以适应 AI 窗口 ...]"
        return text

    def _get_dependency_chain(
        self,
        scope_id: str,
        graph: DependencyGraph
    ) -> List:
        """从依赖图获取依赖链"""
        # 使用依赖图的方法获取上游和下游节点
        upstream = graph.get_upstream_nodes(scope_id)
        downstream = graph.get_downstream_nodes(scope_id)
        current = [graph.nodes[scope_id]]
        return list(upstream) + current + list(downstream)
```

**关键点**：
- ✅ 独立的服务模块
- ✅ 负责所有上下文裁剪逻辑
- ✅ 确保 AI 调用的上下文大小在限制内
- ✅ 可被任何 CLI Command 调用

---

### **2.3 State Manager（状态管理器）**

**[ID: DD-MOD-STATE-001]**

#### **2.3.1 设计目标**

State Manager 负责管理系统的所有状态，包括：
1. 流程状态（RD 是否已生成）
2. 文档版本
3. 任务进度
4. 成本和时间统计

#### **2.3.2 核心实现**

```python
# src/state/manager.py

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional

class StateManager:
    """状态管理器

    负责：
    1. 读写 .specgov/state.json
    2. 记录任务进度
    3. 记录成本和时间
    4. 管理文档版本状态
    """

    def __init__(self, project_dir: str | Path):
        self.project_dir = Path(project_dir)
        self.state_file = self.project_dir / '.specgov' / 'state.json'
        self.state_file.parent.mkdir(parents=True, exist_ok=True)

    def get_state(self) -> Dict[str, Any]:
        """读取当前状态"""
        if not self.state_file.exists():
            return self._default_state()

        try:
            with open(self.state_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Warning: Could not load state: {e}")
            return self._default_state()

    def update(self, updates: Dict[str, Any]):
        """更新状态"""
        state = self.get_state()
        state.update(updates)
        state['last_update'] = datetime.now().isoformat()

        with open(self.state_file, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=2, ensure_ascii=False)

    def can_generate_prd(self) -> bool:
        """检查是否可以生成 PRD（RD 必须已生成）"""
        state = self.get_state()
        return state.get('rd_generated', False)

    def can_generate_dd(self) -> bool:
        """检查是否可以生成 DD（PRD 必须已生成）"""
        state = self.get_state()
        return state.get('prd_generated', False)

    def record_generation(
        self,
        stage: str,
        cost: float,
        tokens: int,
        time_seconds: float
    ):
        """记录生成操作的统计信息"""
        state = self.get_state()

        # 更新阶段状态
        state[f'{stage}_generated'] = True
        state[f'{stage}_version'] = state.get(f'{stage}_version', 0) + 1
        state[f'{stage}_last_generation'] = datetime.now().isoformat()

        # 累计统计
        state['total_cost'] = state.get('total_cost', 0) + cost
        state['total_tokens'] = state.get('total_tokens', 0) + tokens
        state['total_time_seconds'] = state.get('total_time_seconds', 0) + time_seconds

        self.update(state)

    def _default_state(self) -> Dict[str, Any]:
        """默认状态"""
        return {
            'version': '1.0',
            'created_at': datetime.now().isoformat(),
            'rd_generated': False,
            'prd_generated': False,
            'dd_generated': False,
            'td_generated': False,
            'total_cost': 0.0,
            'total_tokens': 0,
            'total_time_seconds': 0.0
        }
```

**关键点**：
- ✅ 简单的文件读写
- ✅ 提供状态查询和更新接口
- ✅ 可被任何 CLI Command 调用
- ✅ 支持流程验证（如 PRD 生成前必须先有 RD）

---

## **三、核心引擎模块设计**

### **3.1 标记解析器 (Tag Parser)**

**[ID: DD-MOD-PARSER-001] [Designs-for: PRD-CMD-006]**

#### **3.1.1 数据结构**

```python
# src/core/parser/tag_types.py

from enum import Enum
from dataclasses import dataclass
from typing import Optional

class TagType(Enum):
    """标记类型枚举"""
    ID = "ID"
    IMPLEMENTS = "Implements"
    DECOMPOSES = "Decomposes"
    DESIGNS_FOR = "Designs-for"
    TESTS_FOR = "Tests-for"

@dataclass
class Tag:
    """标记数据结构"""
    tag_type: TagType
    target_id: str
    file_path: str
    line_number: int
    context: Optional[str] = None  # 标记所在的上下文（如章节标题）

    def __str__(self):
        return f"[{self.tag_type.value}: {self.target_id}] at {self.file_path}#{self.line_number}"

@dataclass
class ParseResult:
    """解析结果"""
    tags: list[Tag]
    errors: list[str]
    warnings: list[str]
    file_path: str
    parse_time_ms: float
```

#### **2.1.2 核心实现**

```python
# src/core/parser/tag_parser.py

import re
from pathlib import Path
from typing import List, Optional
from .tag_types import Tag, TagType, ParseResult

class TagParser:
    """标记解析器

    负责从 Markdown 和代码文件中解析可追溯性标记
    """

    # 正则表达式：匹配 [TagType: ID]
    TAG_REGEX = re.compile(
        r'\[(ID|Implements|Decomposes|Designs-for|Tests-for):\s*([\w\-\.]+)\]',
        re.IGNORECASE
    )

    # 支持的文件扩展名
    SUPPORTED_EXTENSIONS = {
        '.md', '.markdown',           # Markdown
        '.py', '.js', '.ts', '.tsx',  # 代码
        '.java', '.go', '.rs',
        '.cpp', '.c', '.h'
    }

    def __init__(self):
        self.current_context = None

    def parse_file(self, file_path: str | Path) -> ParseResult:
        """解析单个文件

        Args:
            file_path: 文件路径

        Returns:
            ParseResult: 解析结果
        """
        import time
        start = time.time()

        file_path = Path(file_path)
        tags = []
        errors = []
        warnings = []

        try:
            # 检查文件扩展名
            if file_path.suffix not in self.SUPPORTED_EXTENSIONS:
                warnings.append(f"Unsupported file type: {file_path.suffix}")
                return ParseResult([], errors, warnings, str(file_path), 0)

            # 读取文件
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # 逐行解析
            for line_num, line in enumerate(lines, start=1):
                # 更新上下文（Markdown 标题）
                if file_path.suffix in {'.md', '.markdown'}:
                    if line.startswith('#'):
                        self.current_context = line.strip()

                # 查找标记
                for match in self.TAG_REGEX.finditer(line):
                    tag_type_str, target_id = match.groups()

                    try:
                        tag_type = TagType(tag_type_str)
                        tag = Tag(
                            tag_type=tag_type,
                            target_id=target_id.strip(),
                            file_path=str(file_path),
                            line_number=line_num,
                            context=self.current_context
                        )
                        tags.append(tag)
                    except ValueError:
                        errors.append(f"Invalid tag type '{tag_type_str}' at line {line_num}")

        except FileNotFoundError:
            errors.append(f"File not found: {file_path}")
        except UnicodeDecodeError:
            errors.append(f"File encoding error: {file_path}")
        except Exception as e:
            errors.append(f"Unexpected error: {str(e)}")

        parse_time = (time.time() - start) * 1000
        return ParseResult(tags, errors, warnings, str(file_path), parse_time)

    def parse_directory(self, dir_path: str | Path, exclude_dirs: Optional[List[str]] = None) -> List[ParseResult]:
        """递归解析目录

        Args:
            dir_path: 目录路径
            exclude_dirs: 排除的目录（如 node_modules, .git）

        Returns:
            List[ParseResult]: 所有文件的解析结果
        """
        if exclude_dirs is None:
            exclude_dirs = {'node_modules', '.git', '__pycache__', 'venv', '.venv', 'dist', 'build'}

        dir_path = Path(dir_path)
        results = []

        for file_path in dir_path.rglob('*'):
            # 跳过目录
            if file_path.is_dir():
                continue

            # 跳过排除目录中的文件
            if any(excluded in file_path.parts for excluded in exclude_dirs):
                continue

            # 解析文件
            if file_path.suffix in self.SUPPORTED_EXTENSIONS:
                result = self.parse_file(file_path)
                results.append(result)

        return results

    def validate_tag_id(self, tag_id: str) -> tuple[bool, Optional[str]]:
        """验证标记 ID 的格式

        Args:
            tag_id: 标记 ID

        Returns:
            (is_valid, error_message)
        """
        # ID 格式：PREFIX-CATEGORY-NUMBER
        # 例如：RD-REQ-005, PRD-FEAT-012
        pattern = r'^[A-Z]+-[A-Z]+-\d+$'

        if re.match(pattern, tag_id):
            return True, None
        else:
            return False, f"Invalid ID format: {tag_id}. Expected: PREFIX-CATEGORY-NUMBER"
```

---

### **2.2 依赖图引擎 (Dependency Graph)**

**[ID: DD-MOD-GRAPH-001] [Designs-for: PRD-US-003.1]**

#### **2.2.1 数据结构**

```python
# src/core/graph/node.py

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

class NodeType(Enum):
    """节点类型"""
    REQUIREMENT = "requirement"      # RD
    FEATURE = "feature"              # PRD
    API_DESIGN = "api_design"        # DD
    DATABASE = "database"            # DD
    TEST = "test"                    # TD
    CODE = "code"                    # Code

@dataclass
class Node:
    """依赖图节点"""
    id: str                          # 节点 ID（如 RD-REQ-005）
    type: NodeType                   # 节点类型
    file_path: str                   # 所在文件路径
    line_number: int                 # 行号
    context: Optional[str] = None    # 上下文（章节标题）
    metadata: dict = field(default_factory=dict)  # 额外元数据

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.id == other.id
        return False
```

```python
# src/core/graph/edge.py

from dataclasses import dataclass
from enum import Enum

class EdgeType(Enum):
    """边类型（对应标记类型）"""
    IMPLEMENTS = "implements"        # A implements B
    DECOMPOSES = "decomposes"        # A decomposes B
    DESIGNS_FOR = "designs_for"      # A designs for B
    TESTS_FOR = "tests_for"          # A tests for B

@dataclass
class Edge:
    """依赖图边"""
    source_id: str                   # 源节点 ID
    target_id: str                   # 目标节点 ID
    edge_type: EdgeType              # 边类型
    file_path: str                   # 边定义所在文件
    line_number: int                 # 行号

    def __str__(self):
        return f"{self.source_id} --[{self.edge_type.value}]--> {self.target_id}"
```

```python
# src/core/graph/graph.py

from typing import Dict, List, Set, Optional
from .node import Node
from .edge import Edge, EdgeType

class DependencyGraph:
    """依赖关系图

    使用邻接表表示的有向图
    """

    def __init__(self):
        self.nodes: Dict[str, Node] = {}           # id -> Node
        self.outgoing_edges: Dict[str, List[Edge]] = {}  # source_id -> [Edge]
        self.incoming_edges: Dict[str, List[Edge]] = {}  # target_id -> [Edge]

    def add_node(self, node: Node):
        """添加节点"""
        if node.id in self.nodes:
            # 更新已存在的节点
            self.nodes[node.id] = node
        else:
            self.nodes[node.id] = node
            self.outgoing_edges[node.id] = []
            self.incoming_edges[node.id] = []

    def add_edge(self, edge: Edge):
        """添加边"""
        # 确保节点存在
        if edge.source_id not in self.nodes:
            raise ValueError(f"Source node not found: {edge.source_id}")
        if edge.target_id not in self.nodes:
            raise ValueError(f"Target node not found: {edge.target_id}")

        # 添加边
        self.outgoing_edges[edge.source_id].append(edge)
        self.incoming_edges[edge.target_id].append(edge)

    def get_downstream_nodes(self, node_id: str, max_depth: Optional[int] = None) -> Set[Node]:
        """获取下游节点（依赖此节点的所有节点）

        Args:
            node_id: 节点 ID
            max_depth: 最大深度（None 表示无限）

        Returns:
            下游节点集合
        """
        visited = set()
        queue = [(node_id, 0)]

        while queue:
            current_id, depth = queue.pop(0)

            if current_id in visited:
                continue

            if max_depth is not None and depth > max_depth:
                continue

            visited.add(current_id)

            # 添加下游节点
            for edge in self.incoming_edges.get(current_id, []):
                queue.append((edge.source_id, depth + 1))

        # 移除起始节点
        visited.discard(node_id)

        return {self.nodes[nid] for nid in visited if nid in self.nodes}

    def get_upstream_nodes(self, node_id: str, max_depth: Optional[int] = None) -> Set[Node]:
        """获取上游节点（此节点依赖的所有节点）"""
        visited = set()
        queue = [(node_id, 0)]

        while queue:
            current_id, depth = queue.pop(0)

            if current_id in visited:
                continue

            if max_depth is not None and depth > max_depth:
                continue

            visited.add(current_id)

            # 添加上游节点
            for edge in self.outgoing_edges.get(current_id, []):
                queue.append((edge.target_id, depth + 1))

        visited.discard(node_id)
        return {self.nodes[nid] for nid in visited if nid in self.nodes}

    def detect_cycles(self) -> List[List[str]]:
        """检测循环依赖

        Returns:
            循环依赖列表，每个循环是一个节点 ID 列表
        """
        cycles = []
        visited = set()
        rec_stack = set()

        def dfs(node_id: str, path: List[str]) -> bool:
            """深度优先搜索检测循环"""
            if node_id in rec_stack:
                # 发现循环
                cycle_start = path.index(node_id)
                cycles.append(path[cycle_start:])
                return True

            if node_id in visited:
                return False

            visited.add(node_id)
            rec_stack.add(node_id)
            path.append(node_id)

            for edge in self.outgoing_edges.get(node_id, []):
                dfs(edge.target_id, path[:])

            rec_stack.remove(node_id)
            return False

        for node_id in self.nodes:
            if node_id not in visited:
                dfs(node_id, [])

        return cycles

    def to_json(self) -> dict:
        """序列化为 JSON"""
        return {
            "nodes": [
                {
                    "id": node.id,
                    "type": node.type.value,
                    "file_path": node.file_path,
                    "line_number": node.line_number,
                    "context": node.context,
                    "metadata": node.metadata
                }
                for node in self.nodes.values()
            ],
            "edges": [
                {
                    "source": edge.source_id,
                    "target": edge.target_id,
                    "type": edge.edge_type.value,
                    "file_path": edge.file_path,
                    "line_number": edge.line_number
                }
                for edges in self.outgoing_edges.values()
                for edge in edges
            ]
        }

    @classmethod
    def from_json(cls, data: dict) -> 'DependencyGraph':
        """从 JSON 反序列化"""
        graph = cls()

        # 加载节点
        from .node import NodeType
        for node_data in data['nodes']:
            node = Node(
                id=node_data['id'],
                type=NodeType(node_data['type']),
                file_path=node_data['file_path'],
                line_number=node_data['line_number'],
                context=node_data.get('context'),
                metadata=node_data.get('metadata', {})
            )
            graph.add_node(node)

        # 加载边
        for edge_data in data['edges']:
            edge = Edge(
                source_id=edge_data['source'],
                target_id=edge_data['target'],
                edge_type=EdgeType(edge_data['type']),
                file_path=edge_data['file_path'],
                line_number=edge_data['line_number']
            )
            graph.add_edge(edge)

        return graph
```

#### **2.2.2 图构建器**

```python
# src/core/graph/builder.py

from pathlib import Path
from typing import List
from ..parser.tag_parser import TagParser, ParseResult
from ..parser.tag_types import TagType
from .graph import DependencyGraph
from .node import Node, NodeType
from .edge import Edge, EdgeType

class GraphBuilder:
    """依赖图构建器"""

    # 标记类型 -> 节点类型映射
    ID_PREFIX_TO_NODE_TYPE = {
        'RD': NodeType.REQUIREMENT,
        'PRD': NodeType.FEATURE,
        'DD': NodeType.API_DESIGN,
        'TD': NodeType.TEST,
        'CODE': NodeType.CODE,
    }

    # 标记类型 -> 边类型映射
    TAG_TO_EDGE_TYPE = {
        TagType.IMPLEMENTS: EdgeType.IMPLEMENTS,
        TagType.DECOMPOSES: EdgeType.DECOMPOSES,
        TagType.DESIGNS_FOR: EdgeType.DESIGNS_FOR,
        TagType.TESTS_FOR: EdgeType.TESTS_FOR,
    }

    def __init__(self):
        self.parser = TagParser()

    def build_from_directory(self, project_dir: str | Path) -> DependencyGraph:
        """从项目目录构建依赖图

        Args:
            project_dir: 项目根目录

        Returns:
            DependencyGraph: 依赖图
        """
        # 解析所有文件
        parse_results = self.parser.parse_directory(project_dir)

        # 构建图
        graph = DependencyGraph()

        # 第一步：添加所有节点（从 [ID: XXX] 标记）
        for result in parse_results:
            for tag in result.tags:
                if tag.tag_type == TagType.ID:
                    node = self._create_node_from_tag(tag)
                    graph.add_node(node)

        # 第二步：添加所有边（从 Implements, Decomposes 等标记）
        for result in parse_results:
            for tag in result.tags:
                if tag.tag_type != TagType.ID:
                    # 查找源节点（同一文件中最近的 [ID: XXX]）
                    source_node_id = self._find_source_node_id(tag, result)
                    if source_node_id:
                        edge = self._create_edge_from_tag(tag, source_node_id)
                        try:
                            graph.add_edge(edge)
                        except ValueError as e:
                            # 目标节点不存在，记录警告
                            print(f"Warning: {e}")

        return graph

    def _create_node_from_tag(self, tag) -> Node:
        """从 [ID: XXX] 标记创建节点"""
        # 根据 ID 前缀推断节点类型
        prefix = tag.target_id.split('-')[0]
        node_type = self.ID_PREFIX_TO_NODE_TYPE.get(prefix, NodeType.REQUIREMENT)

        return Node(
            id=tag.target_id,
            type=node_type,
            file_path=tag.file_path,
            line_number=tag.line_number,
            context=tag.context
        )

    def _create_edge_from_tag(self, tag, source_node_id: str) -> Edge:
        """从 [Implements: XXX] 等标记创建边"""
        edge_type = self.TAG_TO_EDGE_TYPE[tag.tag_type]

        return Edge(
            source_id=source_node_id,
            target_id=tag.target_id,
            edge_type=edge_type,
            file_path=tag.file_path,
            line_number=tag.line_number
        )

    def _find_source_node_id(self, tag, parse_result: ParseResult) -> str | None:
        """查找源节点 ID

        规则：在同一文件中，查找当前标记之前最近的 [ID: XXX] 标记
        """
        candidates = [
            t for t in parse_result.tags
            if t.tag_type == TagType.ID and t.line_number < tag.line_number
        ]

        if candidates:
            # 返回最近的
            return max(candidates, key=lambda t: t.line_number).target_id

        return None
```

---

### **2.3 影响分析引擎**

**[ID: DD-MOD-ANALYZER-001] [Designs-for: PRD-US-004.1]**

```python
# src/core/analyzer/impact.py

from pathlib import Path
from typing import List, Set
from ..graph.graph import DependencyGraph
from ..graph.node import Node
from ..parser.tag_parser import TagParser
import subprocess

class ImpactAnalyzer:
    """影响分析引擎"""

    def __init__(self, graph: DependencyGraph, project_dir: Path):
        self.graph = graph
        self.project_dir = project_dir
        self.parser = TagParser()

    def analyze_file_change(self, changed_file: str | Path) -> dict:
        """分析单个文件变更的影响

        Args:
            changed_file: 变更的文件路径

        Returns:
            影响分析报告（字典）
        """
        changed_file = Path(changed_file)

        # 1. 使用 Git diff 获取变更内容
        changed_lines = self._get_changed_lines(changed_file)

        # 2. 解析变更文件，识别受影响的节点
        changed_nodes = self._identify_changed_nodes(changed_file, changed_lines)

        # 3. 查询依赖图，获取下游节点
        affected_nodes = set()
        for node_id in changed_nodes:
            downstream = self.graph.get_downstream_nodes(node_id)
            affected_nodes.update(downstream)

        # 4. 分类受影响的节点
        affected_docs = [n for n in affected_nodes if n.file_path.endswith('.md')]
        affected_code = [n for n in affected_nodes if not n.file_path.endswith('.md')]

        # 5. 生成建议的后续操作
        recommendations = self._generate_recommendations(affected_nodes)

        # 6. 构建报告
        report = {
            "changed_file": str(changed_file),
            "changed_nodes": [
                {
                    "id": nid,
                    "type": self.graph.nodes[nid].type.value,
                    "location": f"{self.graph.nodes[nid].file_path}#{self.graph.nodes[nid].line_number}"
                }
                for nid in changed_nodes
            ],
            "affected_documents": [
                {
                    "id": node.id,
                    "type": node.type.value,
                    "location": f"{node.file_path}#{node.line_number}",
                    "context": node.context
                }
                for node in affected_docs
            ],
            "affected_code": [
                {
                    "id": node.id,
                    "type": node.type.value,
                    "location": f"{node.file_path}#{node.line_number}",
                    "context": node.context
                }
                for node in affected_code
            ],
            "recommendations": recommendations
        }

        return report

    def _get_changed_lines(self, file_path: Path) -> Set[int]:
        """使用 Git diff 获取变更的行号"""
        try:
            # git diff HEAD <file> --unified=0
            result = subprocess.run(
                ['git', 'diff', 'HEAD', str(file_path), '--unified=0'],
                cwd=self.project_dir,
                capture_output=True,
                text=True
            )

            # 解析 diff 输出，提取行号
            changed_lines = set()
            for line in result.stdout.split('\n'):
                if line.startswith('@@'):
                    # 格式：@@ -old_start,old_count +new_start,new_count @@
                    import re
                    match = re.search(r'\+(\d+),?(\d+)?', line)
                    if match:
                        start = int(match.group(1))
                        count = int(match.group(2)) if match.group(2) else 1
                        changed_lines.update(range(start, start + count))

            return changed_lines
        except Exception as e:
            print(f"Warning: Could not get git diff: {e}")
            return set()

    def _identify_changed_nodes(self, file_path: Path, changed_lines: Set[int]) -> Set[str]:
        """识别变更文件中受影响的节点"""
        # 重新解析文件
        result = self.parser.parse_file(file_path)

        changed_nodes = set()
        for tag in result.tags:
            if tag.tag_type.value == "ID":
                # 检查此标记是否在变更范围内
                if tag.line_number in changed_lines:
                    changed_nodes.add(tag.target_id)

        return changed_nodes

    def _generate_recommendations(self, affected_nodes: Set[Node]) -> List[str]:
        """生成后续操作建议"""
        recommendations = []

        # 分组
        prd_nodes = [n for n in affected_nodes if n.id.startswith('PRD-')]
        dd_nodes = [n for n in affected_nodes if n.id.startswith('DD-')]
        code_nodes = [n for n in affected_nodes if n.id.startswith('CODE-')]

        if prd_nodes:
            recommendations.append(
                f"重新生成受影响的 PRD 部分: specgov prd:regenerate --scope={prd_nodes[0].id}"
            )

        if dd_nodes:
            recommendations.append(
                f"评审并更新 DD: specgov dd:review --scope={dd_nodes[0].id}"
            )

        if code_nodes:
            recommendations.append(
                f"检查代码一致性: specgov check:consistency --scope={code_nodes[0].id}"
            )

        return recommendations
```

---

### **2.4 任务管理系统**

**[ID: DD-MOD-TASK-001] [Designs-for: RD-TASK-LAYER-001]**

#### **2.4.1 数据结构**

```python
# src/tasks/epic.py

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from datetime import datetime

class EpicStatus(Enum):
    """Epic 状态"""
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    BLOCKED = "blocked"

@dataclass
class Epic:
    """Epic（高层级任务）"""
    id: str                          # Epic ID（如 EPIC-RD-001）
    title: str                       # Epic 标题
    status: EpicStatus               # 状态
    role: str                        # 负责角色
    subtasks: List[str] = field(default_factory=list)  # 子任务 ID 列表
    completed_subtasks: int = 0      # 已完成子任务数
    total_subtasks: int = 0          # 总子任务数
    estimated_time_minutes: int = 0  # 预计时间
    actual_time_minutes: int = 0     # 实际时间
    deliverables: List[str] = field(default_factory=list)  # 交付物
    summary: Optional[str] = None    # 总结
    created_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

    @property
    def progress(self) -> float:
        """进度百分比"""
        if self.total_subtasks == 0:
            return 0.0
        return self.completed_subtasks / self.total_subtasks * 100
```

```python
# src/tasks/task.py

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Dict
from datetime import datetime

class TaskStatus(Enum):
    """任务状态"""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    BLOCKED = "blocked"

class TaskComplexity(Enum):
    """任务复杂度"""
    SIMPLE = "simple"          # < 5K tokens
    MEDIUM = "medium"          # 5K - 10K tokens
    COMPLEX = "complex"        # 10K - 20K tokens
    TOO_COMPLEX = "too_complex"  # > 20K tokens

@dataclass
class Task:
    """角色级任务"""
    id: str                          # 任务 ID（如 TASK-RD-GEN-001）
    epic_id: str                     # 所属 Epic
    title: str                       # 任务标题
    status: TaskStatus               # 状态
    command: str                     # 执行命令
    context_files: List[str] = field(default_factory=list)  # 上下文文件
    acceptance_criteria: List[str] = field(default_factory=list)  # 验收标准
    complexity: Optional[TaskComplexity] = None  # 任务复杂度
    estimated_tokens: int = 0        # 预计 Token 数
    ai_backend: str = "claude-code"  # AI 后端
    estimated_cost: float = 0.0      # 预计成本
    actual_cost: float = 0.0         # 实际成本
    estimated_time_minutes: int = 0  # 预计时间
    actual_time_minutes: int = 0     # 实际时间
    outputs: List[str] = field(default_factory=list)  # 输出文件
    created_at: Optional[datetime] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None
```

```python
# src/tasks/role.py

from enum import Enum

class Role(Enum):
    """角色定义"""
    PROJECT_MANAGER = "project-manager"
    RD_ANALYST = "rd-analyst"
    PRODUCT_MANAGER = "product-manager"
    ARCHITECT = "architect"
    TEST_MANAGER = "test-manager"
    DEVELOPER = "developer"

    @property
    def display_name(self) -> str:
        """显示名称"""
        names = {
            Role.PROJECT_MANAGER: "项目经理",
            Role.RD_ANALYST: "需求分析师",
            Role.PRODUCT_MANAGER: "产品经理",
            Role.ARCHITECT: "架构师",
            Role.TEST_MANAGER: "测试经理",
            Role.DEVELOPER: "开发工程师",
        }
        return names[self]

    @property
    def responsibilities(self) -> str:
        """职责描述"""
        resp = {
            Role.RD_ANALYST: "分析业务需求，生成需求文档 (RD)，评审需求的完整性和合理性",
            Role.PRODUCT_MANAGER: "基于 RD 生成产品需求文档 (PRD)，定义产品功能和用户故事",
            Role.ARCHITECT: "基于 PRD 设计系统架构和技术方案 (DD)，定义 API 和数据结构",
            Role.TEST_MANAGER: "基于 DD 设计测试策略和测试用例 (TD)，确保质量覆盖",
            Role.DEVELOPER: "基于 DD 实现代码，确保符合设计规范",
            Role.PROJECT_MANAGER: "管理项目整体进度，协调各角色，跟踪 Epic 完成情况",
        }
        return resp.get(self, "")

    @property
    def task_file(self) -> str:
        """任务文件路径"""
        return f".specgov/tasks/{self.value}.md"
```

#### **2.4.2 任务复杂度检查器**

```python
# src/tasks/complexity.py

from typing import List, Optional
from pathlib import Path
from .task import Task, TaskComplexity

class ComplexityChecker:
    """任务复杂度检查器"""

    # Token 估算（粗略）
    CHARS_PER_TOKEN = 4

    # 复杂度阈值
    THRESHOLDS = {
        TaskComplexity.SIMPLE: 5000,
        TaskComplexity.MEDIUM: 10000,
        TaskComplexity.COMPLEX: 20000,
    }

    def check_task(self, task: Task) -> tuple[TaskComplexity, Optional[str]]:
        """检查任务复杂度

        Returns:
            (complexity, warning_message)
        """
        # 估算上下文大小
        total_tokens = self._estimate_context_size(task)

        # 判断复杂度
        if total_tokens > self.THRESHOLDS[TaskComplexity.COMPLEX]:
            return (
                TaskComplexity.TOO_COMPLEX,
                f"任务过于复杂（{total_tokens} tokens），建议分解为多个子任务"
            )
        elif total_tokens > self.THRESHOLDS[TaskComplexity.MEDIUM]:
            return (
                TaskComplexity.COMPLEX,
                f"任务较复杂（{total_tokens} tokens），建议仔细检查"
            )
        elif total_tokens > self.THRESHOLDS[TaskComplexity.SIMPLE]:
            return (
                TaskComplexity.MEDIUM,
                None
            )
        else:
            return (
                TaskComplexity.SIMPLE,
                None
            )

    def _estimate_context_size(self, task: Task) -> int:
        """估算任务的上下文大小（tokens）"""
        total_chars = 0

        # 1. 角色定义 + 职责（约 500 tokens）
        total_chars += 500 * self.CHARS_PER_TOKEN

        # 2. 项目背景（project-brief.md，约 500 tokens）
        total_chars += 500 * self.CHARS_PER_TOKEN

        # 3. 当前焦点（current-focus.md，约 300 tokens）
        total_chars += 300 * self.CHARS_PER_TOKEN

        # 4. 上下文文件
        for file_path in task.context_files:
            try:
                size = Path(file_path).stat().st_size
                total_chars += size
            except FileNotFoundError:
                pass

        # 5. 任务指令（约 200 tokens）
        total_chars += 200 * self.CHARS_PER_TOKEN

        return total_chars // self.CHARS_PER_TOKEN

    def suggest_decomposition(self, task: Task) -> List[str]:
        """建议任务分解方案

        Returns:
            分解后的子任务建议
        """
        suggestions = []

        # 基于任务类型的分解策略
        if "generate" in task.command:
            # 生成任务：建议按模块分解
            suggestions.append("按模块分解：--scope=ModuleName")
            suggestions.append("使用自动分解：--auto-decompose")

        elif "review" in task.command:
            # 评审任务：建议分段评审
            suggestions.append("分段评审：--section=1")

        elif "check:consistency" in task.command and "--scope=full" in task.command:
            # 全项目检查：建议并行检查
            suggestions.append("并行检查各模块")

        return suggestions
```

#### **2.4.3 上下文管理器**

```python
# src/tasks/context.py

from pathlib import Path
from typing import List, Dict, Optional
import json

class ContextManager:
    """上下文管理器

    负责管理和加载任务执行所需的上下文信息
    """

    def __init__(self, project_dir: Path):
        self.project_dir = project_dir
        self.context_dir = project_dir / '.specgov' / 'context'

    def load_project_brief(self) -> str:
        """加载项目简介"""
        brief_file = self.context_dir / 'project-brief.md'
        if brief_file.exists():
            return brief_file.read_text(encoding='utf-8')
        return ""

    def load_current_focus(self) -> str:
        """加载当前焦点"""
        focus_file = self.context_dir / 'current-focus.md'
        if focus_file.exists():
            return focus_file.read_text(encoding='utf-8')
        return ""

    def update_current_focus(self, content: str):
        """更新当前焦点"""
        focus_file = self.context_dir / 'current-focus.md'
        focus_file.write_text(content, encoding='utf-8')

    def load_roles_context(self) -> Dict:
        """加载角色上下文"""
        context_file = self.context_dir / 'roles-context.json'
        if context_file.exists():
            return json.loads(context_file.read_text(encoding='utf-8'))
        return {}

    def update_role_context(self, role: str, context: Dict):
        """更新角色上下文"""
        all_contexts = self.load_roles_context()
        all_contexts[role] = context

        context_file = self.context_dir / 'roles-context.json'
        context_file.write_text(
            json.dumps(all_contexts, indent=2, ensure_ascii=False),
            encoding='utf-8'
        )

    def build_task_prompt(self, role: 'Role', task: 'Task') -> str:
        """构建任务的 AI 提示词

        Args:
            role: 角色
            task: 任务

        Returns:
            完整的 AI 提示词
        """
        # 1. 角色定义
        role_prompt = f"""你是一位{role.display_name}。

你的职责：
{role.responsibilities}
"""

        # 2. 项目背景
        background = self.load_project_brief()

        # 3. 当前焦点
        focus = self.load_current_focus()

        # 4. 任务上下文
        task_context = self._load_task_context(task)

        # 5. 任务指令
        task_prompt = f"""当前任务：{task.title}

执行命令：
{task.command}

验收标准：
{self._format_criteria(task.acceptance_criteria)}
"""

        # 6. 组合
        full_prompt = f"""{role_prompt}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
项目背景
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{background}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
当前状态
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{focus}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
相关文档
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{task_context}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
当前任务
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{task_prompt}
"""

        return full_prompt

    def _load_task_context(self, task: 'Task') -> str:
        """加载任务的上下文文件"""
        context_parts = []

        for file_path in task.context_files:
            try:
                path = Path(file_path)
                if path.exists():
                    content = path.read_text(encoding='utf-8')
                    # 智能裁剪：只加载相关部分（这里简化处理，实际可以更智能）
                    context_parts.append(f"【{file_path}】\n{content[:2000]}")  # 限制每个文件最多2000字符
            except Exception as e:
                context_parts.append(f"【{file_path}】\n无法加载：{e}")

        return "\n\n".join(context_parts)

    def _format_criteria(self, criteria: List[str]) -> str:
        """格式化验收标准"""
        if not criteria:
            return "无"
        return "\n".join(f"- {c}" for c in criteria)
```

---

## **三、AI 集成层设计**

### **3.1 AI 后端抽象**

**[ID: DD-AI-001] [Designs-for: PRD-TECH-001]**

```python
# src/ai/backend.py

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

@dataclass
class AIResponse:
    """AI 响应"""
    content: str
    tokens_input: int
    tokens_output: int
    cost: float
    model: str
    backend: str

class AIBackend(ABC):
    """AI 后端抽象基类"""

    @abstractmethod
    def generate(self, prompt: str, max_tokens: int = 4000) -> AIResponse:
        """生成内容

        Args:
            prompt: 提示词
            max_tokens: 最大输出 tokens

        Returns:
            AIResponse: AI 响应
        """
        pass

    @abstractmethod
    def get_name(self) -> str:
        """获取后端名称"""
        pass

    @abstractmethod
    def get_model(self) -> str:
        """获取模型名称"""
        pass
```

```python
# src/ai/claude_code.py

import subprocess
import json
from .backend import AIBackend, AIResponse

class ClaudeCodeBackend(AIBackend):
    """Claude Code 后端适配器"""

    def __init__(self, model: str = "claude-sonnet-4"):
        self.model = model

        # 成本（每 1K tokens）
        self.cost_per_1k = {
            "input": 0.003,
            "output": 0.015
        }

    def generate(self, prompt: str, max_tokens: int = 4000) -> AIResponse:
        """调用 Claude Code 生成内容"""

        # 调用 claude-code CLI（假设有这样的命令）
        # 实际实现需要根据 Claude Code 的真实 API
        try:
            result = subprocess.run(
                [
                    'claude-code',
                    'execute',
                    '--model', self.model,
                    '--max-tokens', str(max_tokens),
                    '--prompt', prompt
                ],
                capture_output=True,
                text=True,
                timeout=300  # 5 分钟超时
            )

            # 解析输出（假设返回 JSON）
            output = json.loads(result.stdout)

            # 计算成本
            tokens_in = output.get('tokens_input', 0)
            tokens_out = output.get('tokens_output', 0)
            cost = (tokens_in / 1000 * self.cost_per_1k['input'] +
                    tokens_out / 1000 * self.cost_per_1k['output'])

            return AIResponse(
                content=output['content'],
                tokens_input=tokens_in,
                tokens_output=tokens_out,
                cost=cost,
                model=self.model,
                backend='claude-code'
            )

        except Exception as e:
            raise RuntimeError(f"Claude Code execution failed: {e}")

    def get_name(self) -> str:
        return "claude-code"

    def get_model(self) -> str:
        return self.model
```

### **3.2 Generator-Reviewer 模式**

**[ID: DD-AI-002] [Designs-for: PRD-US-002.1]**

```python
# src/ai/generator.py

from pathlib import Path
from .backend import AIBackend

class GeneratorAgent:
    """Generator Agent（生成器）"""

    def __init__(self, backend: AIBackend, stage: str):
        self.backend = backend
        self.stage = stage  # rd, prd, dd, td
        self.prompt_template = self._load_prompt_template()

    def generate(self, input_data: dict) -> str:
        """生成文档

        Args:
            input_data: 输入数据（依赖上游文档、用户输入等）

        Returns:
            生成的文档内容
        """
        # 构建提示词
        prompt = self._build_prompt(input_data)

        # 调用 AI
        response = self.backend.generate(prompt)

        return response.content

    def _load_prompt_template(self) -> str:
        """加载提示词模板"""
        template_file = Path(__file__).parent / 'prompts' / f'{self.stage}_generator.txt'
        if template_file.exists():
            return template_file.read_text(encoding='utf-8')
        return self._default_prompt_template()

    def _build_prompt(self, input_data: dict) -> str:
        """构建提示词"""
        # 填充模板
        prompt = self.prompt_template.format(**input_data)
        return prompt

    def _default_prompt_template(self) -> str:
        """默认提示词模板"""
        return f"""你是一位{self.stage.upper()}文档生成专家。

【重要要求】
1. 为每个需求/功能分配唯一 ID：[ID: {self.stage.upper()}-XXX-YYY]
2. 使用 [Implements: XXX] 标记实现关系
3. 输出 Markdown 格式

输入内容：
{{input_content}}

请生成规范的文档。
"""
```

```python
# src/ai/reviewer.py

from .backend import AIBackend
import json

class ReviewerAgent:
    """Reviewer Agent（评审器）"""

    def __init__(self, backend: AIBackend, stage: str):
        self.backend = backend
        self.stage = stage
        self.prompt_template = self._load_prompt_template()

    def review(self, document_content: str) -> dict:
        """评审文档

        Args:
            document_content: 文档内容

        Returns:
            评审报告（字典）
        """
        # 构建提示词
        prompt = self._build_prompt(document_content)

        # 调用 AI
        response = self.backend.generate(prompt)

        # 解析评审报告（假设 AI 返回 JSON）
        try:
            report = json.loads(response.content)
        except json.JSONDecodeError:
            # 如果不是 JSON，尝试解析 Markdown
            report = self._parse_markdown_review(response.content)

        return report

    def _load_prompt_template(self) -> str:
        """加载提示词模板"""
        template_file = Path(__file__).parent / 'prompts' / f'{self.stage}_reviewer.txt'
        if template_file.exists():
            return template_file.read_text(encoding='utf-8')
        return self._default_prompt_template()

    def _build_prompt(self, document_content: str) -> str:
        """构建提示词"""
        prompt = self.prompt_template.format(document=document_content)
        return prompt

    def _default_prompt_template(self) -> str:
        """默认提示词模板"""
        return f"""你是一位{self.stage.upper()}文档评审专家。

请评审以下文档，检查：
1. 可追溯性标记的完整性和正确性
2. 内容的完整性和合理性
3. 格式的规范性

文档内容：
{{document}}

请以 JSON 格式输出评审报告：
{{
  "summary": "总结",
  "issues": [
    {{
      "severity": "严重/警告/建议",
      "location": "位置",
      "description": "问题描述",
      "suggestion": "修改建议"
    }}
  ],
  "traceability_check": {{
    "all_have_id": true/false,
    "references_valid": true/false
  }}
}}
"""

    def _parse_markdown_review(self, content: str) -> dict:
        """解析 Markdown 格式的评审报告"""
        # 简化实现：提取关键信息
        return {
            "summary": "评审完成",
            "issues": [],
            "raw_content": content
        }
```

---

## **四、CLI 命令实现**

### **4.1 核心命令流程**

**[ID: DD-CLI-001] [Designs-for: PRD-CMD-001]**

#### **命令：specgov init**

```python
# src/cli/commands/init.py

import click
from pathlib import Path
import shutil
import yaml

@click.command()
@click.argument('project_name')
@click.option('--ai', default='claude-code', help='AI 后端')
@click.option('--no-git', is_flag=True, help='不初始化 Git')
def init(project_name: str, ai: str, no_git: bool):
    """初始化 SpecGovernor 项目"""

    click.echo(f"✓ 初始化项目: {project_name}")
    click.echo(f"✓ AI 后端: {ai}")

    # 1. 创建目录结构
    base_dir = Path('.specgov')
    base_dir.mkdir(exist_ok=True)

    (base_dir / 'artifacts').mkdir(exist_ok=True)
    (base_dir / 'reviews').mkdir(exist_ok=True)
    (base_dir / 'reports').mkdir(exist_ok=True)
    (base_dir / 'index').mkdir(exist_ok=True)
    (base_dir / 'context').mkdir(exist_ok=True)
    (base_dir / 'tasks').mkdir(exist_ok=True)

    click.echo("✓ 目录结构：")
    click.echo("  .specgov/")
    click.echo("    ├── config.yml")
    click.echo("    ├── state.json")
    click.echo("    ├── index/")
    click.echo("    ├── artifacts/")
    click.echo("    ├── context/")
    click.echo("    └── tasks/")

    # 2. 生成配置文件
    config = {
        'project_name': project_name,
        'ai_backend': {
            'default': ai,
            'claude-code': {
                'command': 'claude-code execute',
                'model': 'claude-sonnet-4',
                'max_tokens': 200000
            }
        },
        'task_management': {
            'complexity_thresholds': {
                'simple': 5000,
                'medium': 10000,
                'complex': 20000
            }
        }
    }

    config_file = base_dir / 'config.yml'
    with open(config_file, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)

    # 3. 生成 state.json
    state = {
        'current_role': None,
        'last_update': None
    }

    import json
    state_file = base_dir / 'state.json'
    with open(state_file, 'w') as f:
        json.dump(state, f, indent=2)

    # 4. 初始化 Git（如果需要）
    if not no_git:
        import subprocess
        try:
            subprocess.run(['git', 'init'], check=True, capture_output=True)
            click.echo("✓ Git 仓库初始化完成")
        except subprocess.CalledProcessError:
            click.echo("⚠️  Git 初始化失败（可能已存在）")

    # 5. 输出下一步指引
    click.echo("\n📚 下一步：")
    click.echo("  1. 编辑 .specgov/context/project-brief.md 添加项目背景")
    click.echo("  2. 运行 specgov rd:generate 开始生成需求文档")
```

#### **命令：specgov rd:generate**

```python
# src/cli/commands/rd.py

import click
from pathlib import Path
from ...ai.generator import GeneratorAgent
from ...ai.claude_code import ClaudeCodeBackend
from ...storage.file_ops import save_artifact

@click.group()
def rd():
    """RD 阶段命令"""
    pass

@rd.command()
@click.option('--input', type=click.Path(exists=True), help='输入文件')
@click.option('--ai', default='claude-code', help='AI 后端')
@click.option('--output', default='.specgov/artifacts/rd.md', help='输出路径')
def generate(input: str, ai: str, output: str):
    """生成需求文档 (RD)"""

    click.echo("🤖 RD Generator Agent 正在工作...")

    # 1. 读取输入
    input_content = ""
    if input:
        click.echo(f"  读取输入：{input}")
        input_content = Path(input).read_text(encoding='utf-8')

    # 2. 初始化 AI 后端
    click.echo(f"  调用 AI：{ai} (claude-sonnet-4)")
    backend = ClaudeCodeBackend()

    # 3. 创建 Generator Agent
    generator = GeneratorAgent(backend, stage='rd')

    # 4. 生成文档
    click.echo("  生成中...")
    result = generator.generate({'input_content': input_content})

    # 5. 保存文档
    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result, encoding='utf-8')

    click.echo(f"✓ 生成完成：{output}")

    # 6. 统计信息
    # TODO: 解析标记，输出统计

    click.echo("\n📚 下一步：")
    click.echo("  运行 specgov rd:review 进行评审")

@rd.command()
@click.option('--ai', default='gemini-cli', help='AI 后端（建议使用不同后端）')
def review(ai: str):
    """评审需求文档 (RD)"""

    click.echo("🔍 RD Reviewer Agent 正在评审...")

    # 1. 读取文档
    rd_file = Path('.specgov/artifacts/rd.md')
    if not rd_file.exists():
        click.echo("✗ 错误：RD 文档不存在，请先运行 specgov rd:generate")
        return

    click.echo(f"  读取文档：{rd_file}")
    document = rd_file.read_text(encoding='utf-8')

    # 2. 初始化 AI 后端
    click.echo(f"  调用 AI：{ai}")
    # TODO: 支持多后端
    from ...ai.claude_code import ClaudeCodeBackend
    backend = ClaudeCodeBackend()

    # 3. 创建 Reviewer Agent
    from ...ai.reviewer import ReviewerAgent
    reviewer = ReviewerAgent(backend, stage='rd')

    # 4. 评审
    click.echo("  评审中...")
    report = reviewer.review(document)

    # 5. 保存评审报告
    import json
    review_file = Path('.specgov/reviews/rd-review.json')
    review_file.parent.mkdir(parents=True, exist_ok=True)
    review_file.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')

    click.echo(f"✓ 评审完成：{review_file}")

    # 6. 输出摘要
    click.echo("\n📋 评审报告：")
    click.echo(f"总结：{report.get('summary', '')}")

    issues = report.get('issues', [])
    if issues:
        click.echo(f"\n⚠️  发现 {len(issues)} 个问题：")
        for i, issue in enumerate(issues, 1):
            click.echo(f"  {i}. [{issue['severity']}] {issue['description']}")
    else:
        click.echo("✓ 未发现问题")

    click.echo("\n📚 下一步：")
    click.echo("  运行 specgov rd:revise 根据评审意见修订")
```

---

## **五、数据存储设计**

### **5.1 文件格式**

**[ID: DD-STORAGE-001]**

#### **依赖图存储格式**

```json
// .specgov/index/dependency-graph.json
{
  "version": "1.0",
  "build_time": "2025-11-16T15:30:00Z",
  "nodes": [
    {
      "id": "RD-REQ-005",
      "type": "requirement",
      "file_path": "docs/rd.md",
      "line_number": 42,
      "context": "## 1.1 OAuth2 登录",
      "metadata": {}
    }
  ],
  "edges": [
    {
      "source": "PRD-FEAT-012",
      "target": "RD-REQ-005",
      "type": "implements",
      "file_path": "docs/prd.md",
      "line_number": 128
    }
  ]
}
```

#### **任务文件格式**

```markdown
// .specgov/tasks/project.md
# SpecGovernor 项目任务（项目经理视图）

> **项目**: OAuth2 登录功能
> **开始时间**: 2025-11-16 10:00

## Epic 概览

| Epic | 状态 | 进度 | 负责角色 | 预计时间 | 实际时间 |
|------|------|------|---------|---------|---------|
| Epic 1: RD 阶段 | ✅ 完成 | 3/3 (100%) | 需求分析师 | 30分钟 | 35分钟 |
| Epic 2: PRD 阶段 | ⏳ 进行中 | 1/3 (33%) | 产品经理 | 40分钟 | 15分钟 |

**总进度**: █████░░░░░░░░░░░ 27% (4/15)
```

---

## **六、性能优化设计**

### **6.1 索引构建优化**

**[ID: DD-PERF-001] [Designs-for: PRD-AC-002]**

**目标：100万行代码 < 1分钟**

策略：
1. **并行解析**：使用多进程解析多个文件
2. **增量更新**：基于 Git diff 只重新解析变更文件
3. **缓存机制**：缓存已解析的文件（基于文件哈希）

```python
# 伪代码
def build_index_parallel(files: List[Path], num_workers: int = 4):
    from multiprocessing import Pool

    with Pool(num_workers) as pool:
        results = pool.map(parse_file, files)

    return merge_results(results)
```

### **6.2 影响分析优化**

**[ID: DD-PERF-002] [Designs-for: PRD-US-004.1]**

**目标：< 10秒，$0成本**

策略：
1. **纯图查询**：无 AI 调用，只查询内存中的依赖图
2. **BFS 算法**：广度优先搜索下游节点
3. **索引优化**：使用哈希表加速查找

---

## **七、测试策略**

### **7.1 单元测试**

**[ID: DD-TEST-001]**

覆盖模块：
- Tag Parser（标记解析准确性 > 95%）
- Dependency Graph（图操作正确性）
- Impact Analyzer（影响分析准确性）
- Task Complexity Checker（复杂度判断准确性）

### **7.2 集成测试**

**[ID: DD-TEST-002]**

测试场景：
- 完整 RD → PRD → DD → TD → Code 流程
- 影响分析端到端测试
- 一致性检查端到端测试

### **7.3 性能测试**

**[ID: DD-TEST-003]**

性能基准：
- 索引构建：100万行代码 < 1分钟
- 影响分析：任意项目 < 10秒
- 一致性检查：单需求 < 2分钟

---

## **八、实现计划**

### **8.1 MVP（10-14周）**

**[ID: DD-IMPL-MVP]**

| 周次 | 模块 | 工作内容 |
|-----|------|---------|
| 1-2 | 基础框架 | Fork spec-kit，搭建项目结构 |
| 3-4 | Tag Parser | 实现标记解析器 + 单元测试 |
| 5-6 | Dependency Graph | 实现依赖图 + 图算法 |
| 7-8 | RD 阶段 | 实现 rd:generate/review/revise |
| 9-10 | Impact Analysis | 实现影响分析引擎 |
| 11-12 | Consistency Check | 实现一致性检查（单需求） |
| 13-14 | 集成测试 | 端到端测试 + Bug修复 |

### **8.2 V1.0（MVP + 6-8周）**

**[ID: DD-IMPL-V1]**

| 周次 | 模块 | 工作内容 |
|-----|------|---------|
| 15-16 | PRD/DD/TD 阶段 | 实现其他文档阶段 |
| 17-18 | 任务管理系统 | 实现两层任务管理 |
| 19-20 | 增量索引 | 实现增量更新 |
| 21-22 | 性能优化 | 并行化、缓存 |

---

## **九、风险缓解**

### **9.1 技术风险**

**[ID: DD-RISK-001]**

| 风险 | 缓解措施 |
|------|---------|
| AI 生成标记不准确 | Reviewer Agent 检查 + 手动修复工具 |
| 依赖图构建性能不足 | 并行解析 + 增量更新 |
| 上下文窗口超限 | 任务复杂度检查 + 自动分解 |

---

## **十、总结**

### **10.1 设计亮点**

**[ID: DD-SUMMARY-001]**

1. ✅ **复用 spec-kit**：60-70% 代码复用，节省 5-6 周开发时间
2. ✅ **显式追溯**：基于正则表达式解析，性能高、成本低
3. ✅ **两层任务管理**：项目经理管理 Epic，角色管理任务
4. ✅ **无状态设计**：所有状态存储在 Git，支持跨电脑工作
5. ✅ **AI 上下文控制**：任务复杂度检查，避免超出窗口

### **10.2 下一步**

**[ID: DD-NEXT-001]**

1. ✅ **编写 TD（测试文档）**：详细的测试用例和策略
2. ✅ **开始实现**：Fork spec-kit，开始编码

---

**设计文档结束**
