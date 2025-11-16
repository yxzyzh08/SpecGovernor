# **📝 SpecGovernor 需求规格（基于 Spec-Kit 的简化版）**

> **版本**: v2.0-simplified
> **基于**: GitHub spec-kit 开源项目
> **调整日期**: 2025-11-16
> **核心理念**: 利用大模型能力，减少预构建索引，保留核心质量保证机制

---

## **一、项目定位**

SpecGovernor 是一个**轻量级、AI 驱动的研发流程治理工具**，专为**超级个体**设计，帮助一人团队在中小型项目中实现高质量的文档-代码一致性管理。

**核心特点：**
- 🎯 **基于 spec-kit 架构**：复用成熟的 CLI 框架和 AI 集成机制
- 🔄 **Generator-Reviewer 对模式**：每个文档阶段都有双重验证（核心创新）
- 📋 **传统 SDLC 五阶段**：RD → PRD → DD → TD → Code（保留完整性）
- 🪶 **轻量级索引**：仅维护模块列表，其他依赖 AI 实时分析
- 🚀 **手动并行优化**：用户控制并行检查，系统提供指导

---

## **二、与原需求的关键调整**

### **2.1 删除的复杂功能**

| 删除项 | 原因 | 替代方案 |
|--------|------|---------|
| **复杂依赖图** (dependency-graph.json) | 构建和维护成本高 | AI 实时分析依赖关系 |
| **代码符号映射** (code-map.json) | 需要 AST 解析，复杂 | 利用 AI 的代码理解能力 |
| **快速检查模式** | 实现复杂，收益有限 | 统一使用深度检查 |
| **自动增量索引更新** | 实现复杂 | 手动触发 `specgov index:update` |
| **自动并行编排** | 需要复杂的任务调度 | 生成并行任务清单，用户手动执行 |

### **2.2 保留的核心功能**

| 保留项 | 价值 | 对比 spec-kit 的优势 |
|--------|------|---------------------|
| **Generator-Reviewer 对** | 避免自我审查偏差，提高质量 | spec-kit 没有此机制 |
| **五阶段 SDLC** | 符合传统研发流程 | spec-kit 只有 Spec/Plan/Tasks |
| **影响分析** | 快速定位变更影响范围 | spec-kit 的 analyze 功能较弱 |
| **模块化检查** | 支持大型项目 | spec-kit 不支持模块级检查 |

### **2.3 简化后的架构**

```
┌─────────────────────────────────────────────────────────┐
│                  SpecGovernor CLI                       │
│  (基于 spec-kit 的 CLI 框架)                            │
└────────────┬────────────────────────────────────────────┘
             │
    ┌────────┴────────┐
    │  轻量级索引层    │
    │  modules.json   │  ← 仅模块列表和文档位置
    └────────┬────────┘
             │
    ┌────────┴────────────────────────────┐
    │         AI Agent 层                 │
    ├─────────────────────────────────────┤
    │  RD Generator   │  RD Reviewer      │
    │  PRD Generator  │  PRD Reviewer     │
    │  DD Generator   │  DD Reviewer      │
    │  TD Generator   │  TD Reviewer      │
    │  Impact Analyzer                    │
    │  Consistency Checker                │
    └─────────────────────────────────────┘
             │
    ┌────────┴────────┐
    │   AI 后端层      │
    │  Claude Code    │
    │  Gemini CLI     │
    │  ...            │
    └─────────────────┘
```

---

## **三、功能需求（简化版）**

### **3.1 项目初始化**

| 命令 | 功能 | 输出 |
|------|------|------|
| `specgov init <name> --ai <backend>` | 初始化项目结构 | `.specgov/config.yml`<br>`.specgov/index/modules.json`<br>`.specgov/artifacts/` |

**modules.json 初始化方式：**
- 用户手动编写（推荐）
- 或通过 `specgov index:scan` 自动扫描项目结构生成

### **3.2 五阶段工作流**

每个阶段都支持三个命令：

```bash
# 生成
specgov <stage>:generate [--based-on=<upstream>] [--ai=<backend>]

# 评审（可指定不同 AI 后端）
specgov <stage>:review [--ai=<backend>]

# 修订
specgov <stage>:revise [--review=<review-file>]
```

**阶段列表：**
- `rd` - 需求文档 (Requirements Document)
- `prd` - 产品需求文档 (Product Requirements Document)
- `dd` - 设计文档 (Design Document)
- `td` - 测试文档 (Test Document)

**输入输出：**
- 生成输出：`.specgov/artifacts/<stage>.md`
- 评审输出：`.specgov/reviews/<stage>-review.json`

**评审报告 Schema：**
```json
{
  "stage": "rd|prd|dd|td",
  "reviewer": "gemini-cli",
  "timestamp": "2025-11-16T10:30:00Z",
  "summary": {
    "total_issues": 3,
    "critical": 0,
    "warnings": 2,
    "suggestions": 1
  },
  "issues": [
    {
      "level": "warning|critical|info",
      "location": "第 3.2 节",
      "issue": "缺少具体的性能指标",
      "suggestion": "建议补充：响应时间 < 500ms，并发支持 1000 用户"
    }
  ],
  "overall_assessment": "通过|需修订|不通过"
}
```

### **3.3 影响分析**

**命令：**
```bash
specgov analyze --changed=<file>
```

**实现方式：**
- 读取 Git diff 获取变更内容
- 加载 modules.json 和所有 artifacts
- 构造提示词，调用 AI 分析影响范围
- **不依赖预构建依赖图**

**输出示例：**
```json
{
  "changed": {
    "file": "docs/rd.md",
    "type": "requirement",
    "sections": ["2.3 用户认证"]
  },
  "affected_docs": [
    {
      "doc": "prd",
      "section": "3.2 登录功能",
      "reason": "需要从用户名密码改为 OAuth2"
    },
    {
      "doc": "dd",
      "section": "4.1 认证服务设计",
      "reason": "API 设计需要调整"
    }
  ],
  "affected_code": [
    {
      "file": "src/auth/auth.service.ts",
      "symbol": "AuthService.login()",
      "reason": "登录逻辑需要重构"
    }
  ],
  "recommendations": [
    "重新生成 PRD 第 3.2 节",
    "评审 DD 第 4.1 节",
    "运行认证模块的一致性检查"
  ]
}
```

**性能和成本：**
- 时间：< 2 分钟（调用 AI）
- 成本：< $0.05（上下文约 5-10K tokens）

### **3.4 一致性检查**

**命令：**
```bash
# 检查单个模块
specgov check --module=<module-id>

# 检查全项目（生成并行任务清单）
specgov check --scope=full

# 合并并行检查结果
specgov check:merge
```

**实现方式（单模块）：**
1. 从 `modules.json` 定位模块
2. 加载相关文档片段（基于 `doc_sections` 字段）
3. 加载相关代码文件（基于 `code_paths` glob 匹配）
4. 构造提示词，调用 AI 深度分析
5. 输出结构化差异报告

**检查项：**
- RD ↔ PRD：PRD 是否忠实反映 RD 的需求
- PRD ↔ DD：DD 的设计是否满足 PRD 的功能要求
- DD ↔ Code：代码实现是否符合 DD 的设计
- DD ↔ TD：TD 的测试用例是否覆盖 DD 的关键设计

**输出示例：**
```json
{
  "module": "user-module",
  "timestamp": "2025-11-16T10:45:00Z",
  "inconsistencies": [
    {
      "level": "critical",
      "from": "DD",
      "to": "Code",
      "location": "src/auth/auth.controller.ts:89",
      "issue": "DD 设计的 API 是 POST /auth/oauth2，代码实现是 GET",
      "suggestion": "修改代码为 POST 方法"
    }
  ],
  "summary": "发现 1 处严重不一致，需修复"
}
```

**全项目检查（手动并行）：**
```bash
$ specgov check --scope=full

检测到 10 个模块，建议并行检查以提升效率：
╔═════════════════════════════════════════════════╗
║  终端 1: specgov check --module=user-module     ║
║  终端 2: specgov check --module=order-module    ║
║  终端 3: specgov check --module=payment-module  ║
║  ...                                            ║
╚═════════════════════════════════════════════════╝

完成后运行：specgov check:merge
```

**性能和成本：**
- 单模块：< 3 分钟，< $0.10
- 全项目（10 模块并行）：< 5 分钟，< $1

---

## **四、非功能需求**

### **4.1 性能指标（调整后）**

| 操作 | 时间 | 成本 | 对比原需求 |
|------|------|------|-----------|
| 项目初始化 | < 1 分钟 | $0 | ✅ 快 20 倍（原 20 分钟） |
| 影响分析 | < 2 分钟 | < $0.05 | ⚠️ 慢但可接受（原 < 30 秒，$0） |
| 单模块一致性检查 | < 3 分钟 | < $0.10 | ≈ 相当（原 < 2 分钟） |
| 全项目检查（10 模块并行） | < 5 分钟 | < $1 | ✅ 快 2 倍（原 < 10 分钟） |
| 索引更新 | < 1 分钟 | $0 | ✅ 快 20 倍（原增量更新 < 1 分钟，全量 20 分钟） |

### **4.2 架构约束**

| ID | 约束 | 说明 |
|----|------|------|
| **NFR-1** | 纯 CLI 架构 | 无后台服务，状态通过 `.specgov/` 目录管理 |
| **NFR-2** | 基于 spec-kit | 复用 spec-kit 的 CLI 框架、AI 抽象层、模板系统 |
| **NFR-3** | 多 AI 后端支持 | Claude Code、Gemini CLI、GitHub Copilot 等 |
| **NFR-4** | Git 集成 | 依赖 Git 进行版本控制和 diff 分析 |
| **NFR-5** | 禁止 RAG/向量数据库 | 不使用向量数据库，依赖 AI 实时分析 |

### **4.3 成本控制目标**

| 场景 | 频率 | 单次成本 | 月成本估算 |
|------|------|---------|-----------|
| 日常影响分析 | 5 次/天 | $0.05 | $7.5 |
| 模块级检查 | 2 次/天 | $0.10 | $6 |
| 全项目检查 | 1 次/周 | $1 | $4 |
| **总计** | - | - | **< $20/月** |

**对比原需求：**
- 原需求目标：< $10/月（依赖免费的图查询）
- 调整后：< $20/月（依赖 AI 分析，但实现简单）
- **结论：成本增加可接受，换来 70% 的实现复杂度降低**

---

## **五、轻量级索引设计**

### **5.1 modules.json Schema**

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "version": {
      "type": "string",
      "default": "1.0"
    },
    "project": {
      "type": "object",
      "properties": {
        "name": {"type": "string"},
        "description": {"type": "string"}
      }
    },
    "modules": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "模块唯一标识（kebab-case）"
          },
          "name": {
            "type": "string",
            "description": "模块中文名称"
          },
          "description": {
            "type": "string",
            "description": "模块功能描述"
          },
          "code_paths": {
            "type": "array",
            "items": {"type": "string"},
            "description": "代码路径（支持 glob 模式）"
          },
          "doc_sections": {
            "type": "object",
            "properties": {
              "rd": {"type": "string", "description": "RD 文档位置"},
              "prd": {"type": "string", "description": "PRD 文档位置"},
              "dd": {"type": "string", "description": "DD 文档位置"},
              "td": {"type": "string", "description": "TD 文档位置"}
            }
          }
        },
        "required": ["id", "name", "code_paths"]
      }
    }
  },
  "required": ["version", "modules"]
}
```

### **5.2 示例**

```json
{
  "version": "1.0",
  "project": {
    "name": "E-Commerce Platform",
    "description": "电商平台后端服务"
  },
  "modules": [
    {
      "id": "user-module",
      "name": "用户模块",
      "description": "用户注册、登录、个人信息管理",
      "code_paths": [
        "src/user/**/*.ts",
        "src/auth/**/*.ts"
      ],
      "doc_sections": {
        "rd": ".specgov/artifacts/rd.md#用户管理需求",
        "prd": ".specgov/artifacts/prd.md#用户功能",
        "dd": ".specgov/artifacts/dd.md#用户服务设计",
        "td": ".specgov/artifacts/td.md#用户模块测试"
      }
    },
    {
      "id": "order-module",
      "name": "订单模块",
      "description": "订单创建、支付、物流跟踪",
      "code_paths": [
        "src/order/**/*.ts",
        "src/payment/**/*.ts"
      ],
      "doc_sections": {
        "rd": ".specgov/artifacts/rd.md#订单管理需求",
        "prd": ".specgov/artifacts/prd.md#订单功能",
        "dd": ".specgov/artifacts/dd.md#订单服务设计",
        "td": ".specgov/artifacts/td.md#订单模块测试"
      }
    }
  ]
}
```

### **5.3 维护方式**

**手动维护（推荐）：**
- 用户在项目初始化时编写 `modules.json`
- 新增模块时手动添加条目
- 优点：精准、可控
- 缺点：需要手动维护

**自动扫描（可选）：**
```bash
specgov index:scan
```
- 扫描项目目录结构，根据文件夹命名推断模块
- 生成初始的 `modules.json`
- 用户再手动调整

---

## **六、基于 Spec-Kit 的开发路线**

### **6.1 复用策略**

| Spec-Kit 组件 | 复用程度 | 说明 |
|--------------|---------|------|
| CLI 框架 | 100% | 直接复用 `src/specify_cli/` 的命令行框架 |
| AI 抽象层 | 80% | 复用 AI 调用接口，扩展 Generator-Reviewer 对 |
| 配置管理 | 100% | 复用配置文件读写逻辑 |
| Git 集成 | 100% | 复用 Git 状态检测和 diff 分析 |
| 模板系统 | 50% | 参考 slash 命令模板，新增 RD/PRD/DD/TD 模板 |

### **6.2 新增组件**

| 组件 | 说明 |
|------|------|
| Generator-Reviewer 协调器 | 管理双 Agent 协作流程 |
| 轻量级索引管理器 | modules.json 的创建、读取、更新 |
| 影响分析引擎 | 基于 AI 的实时影响分析 |
| 一致性检查引擎 | 多阶段一致性深度分析 |
| 并行任务生成器 | 生成并行检查指令 |

### **6.3 开发阶段（预计 12-14 周）**

**阶段 1: 基础框架（2-3 周）**
- Fork spec-kit 仓库
- 重命名为 `specgov`，调整 CLI 入口
- 实现 `modules.json` 的创建和读取
- 实现 `specgov init` 命令

**阶段 2: 单阶段工作流（3-4 周）**
- 实现 `rd:generate` / `rd:review` / `rd:revise` 命令
- 设计 RD 的提示词模板
- 实现评审报告的 JSON Schema 验证
- 添加双 AI 后端配置支持

**阶段 3: 完整工作流（3-4 周）**
- 实现 `prd/dd/td` 的生成-评审-修订命令
- 实现各阶段的提示词模板
- 实现文档之间的依赖传递（`--based-on` 参数）

**阶段 4: 分析和检查（3-4 周）**
- 实现 `analyze` 命令（影响分析）
- 实现 `check --module` 命令（单模块一致性检查）
- 实现 `check --scope=full` 和 `check:merge`（并行检查）

**阶段 5: 优化和测试（1-2 周）**
- 性能优化和成本控制
- 端到端测试
- 编写用户文档和示例

---

## **七、关键技术决策**

### **7.1 为什么删除预构建依赖图？**

**原需求的依赖图：**
- 需要 AST 解析提取代码符号
- 需要关键词匹配建立依赖关系
- 需要增量更新机制
- 实现复杂度高（~ 2000 行代码）

**基于 AI 的替代方案：**
- 直接加载相关文档和代码，让 AI 分析
- 利用大模型的代码理解能力（Claude Code、Gemini）
- 实现简单（~ 200 行代码）
- 成本可接受（$0.05-0.10/次）

**权衡：**
- ❌ 失去：影响分析的即时响应（原 < 30 秒，$0）
- ✅ 获得：70% 的实现复杂度降低
- ✅ 获得：90% 的维护成本降低
- ✅ 结论：**值得**（对超级个体而言，简单性 > 极致性能）

### **7.2 为什么保留五阶段而非简化为三阶段？**

**Spec-Kit 的三阶段：**
- Specification → Plan → Tasks
- 优点：简洁
- 缺点：不符合传统 SDLC，缺少 PRD 和 TD 的独立性

**SpecGovernor 的五阶段：**
- RD → PRD → DD → TD → Code
- 优点：符合传统研发流程，文档职责清晰
- 缺点：阶段较多

**结论：**
- 目标用户是**超级个体**，但可能在传统企业环境中工作
- 保留传统阶段有助于与现有流程对接
- **保留五阶段**

### **7.3 为什么使用手动并行而非自动编排？**

**自动编排（原需求）：**
- 系统自动分解任务，分发给多个 AI 客户端
- 需要实现任务调度器、进度监控、结果汇总
- 实现复杂度高

**手动并行（调整后）：**
- 系统生成并行任务清单，用户手动在多个终端执行
- 用户保持控制权
- 实现简单

**结论：**
- 对于**超级个体**，手动控制并行度更灵活
- 避免过度自动化的复杂性
- **手动并行 + 系统指导**

---

## **八、下一步行动**

### **立即开始：**

1. **克隆 spec-kit 仓库**
   ```bash
   git clone https://github.com/github/spec-kit.git
   cd spec-kit
   ```

2. **分析源代码结构**
   - 重点关注 `src/specify_cli/` 目录
   - 理解 AI 调用抽象层
   - 理解 slash 命令的模板系统

3. **Fork 并重命名**
   ```bash
   # 创建新分支
   git checkout -b specgov-foundation

   # 重命名入口
   mv src/specify_cli src/specgov_cli

   # 修改 pyproject.toml
   # 将 name = "specify-cli" 改为 name = "specgov-cli"
   ```

4. **实现第一个命令**
   - 实现 `specgov init` 命令
   - 生成 `.specgov/config.yml` 和 `modules.json`

### **需要的文档：**

- [ ] PRD（产品需求文档）：详细描述每个命令的交互流程
- [ ] DD（设计文档）：定义模块划分、数据结构、API 接口
- [ ] 提示词模板库：RD/PRD/DD/TD 的 Generator 和 Reviewer 提示词

---

## **九、总结**

**SpecGovernor v2（简化版）的核心价值：**

1. ✅ **基于成熟框架**：复用 spec-kit 的 70% 代码，快速迭代
2. ✅ **核心创新保留**：Generator-Reviewer 对 + 五阶段工作流
3. ✅ **大幅简化**：删除复杂索引，利用大模型能力
4. ✅ **成本可控**：< $20/月，对超级个体可接受
5. ✅ **开发周期短**：12-14 周完成 MVP

**与原需求的权衡：**
- 🔽 影响分析速度：从 < 30s 降至 < 2min（但仍可接受）
- 🔽 成本增加：从 $10/月 增至 $20/月（但换来简单性）
- ✅ 实现复杂度：降低 70%
- ✅ 维护成本：降低 90%
- ✅ 开发周期：缩短 50%

**建议：**
立即开始基于 spec-kit 的开发，优先实现单阶段工作流（RD 的 generate-review-revise），验证可行性后再扩展至完整五阶段。