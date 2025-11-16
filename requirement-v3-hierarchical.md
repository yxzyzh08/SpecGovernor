# **📝 SpecGovernor 需求规格（层次化版本）**

> **版本**: v3.0-hierarchical
> **基于**: GitHub spec-kit 开源项目 + 两层需求结构
> **调整日期**: 2025-11-16
> **核心理念**: 利用大模型能力，支持层次化需求管理，解决跨模块场景

---

## **一、项目定位**

SpecGovernor 是一个**轻量级、AI 驱动的研发流程治理工具**，专为**超级个体**设计，帮助一人团队在中小型项目中实现高质量的文档-代码一致性管理。

**核心特点：**
- 🎯 **基于 spec-kit 架构**：复用成熟的 CLI 框架和 AI 集成机制
- 🔄 **Generator-Reviewer 对模式**：每个文档阶段都有双重验证（核心创新）
- 📋 **传统 SDLC 五阶段**：RD → PRD → DD → TD → Code（保留完整性）
- 🏗️ **两层需求结构**：支持 high-level 整体需求 + module-level 模块需求（**新增**）
- 🔗 **跨模块需求管理**：轻量级需求映射，支持 Epic 级需求追溯（**新增**）
- 🪶 **轻量级索引**：仅维护模块列表和需求映射，其他依赖 AI 实时分析
- 🚀 **手动并行优化**：用户控制并行检查，系统提供指导

---

## **二、核心问题与解决方案**

### **2.1 实际项目场景**

**问题：一个完整需求通常跨越多个模块**

```
示例：电商下单功能

High-level 需求 (Epic):
"用户能够在线下单并完成支付"

涉及的模块：
├── 用户模块（身份验证、收货地址）
├── 商品模块（库存查询、价格计算）
├── 订单模块（订单创建、状态管理）
├── 支付模块（支付处理、回调）
└── 物流模块（配送信息）

挑战：
1. 如何组织文档？（一个大文档 vs 多个小文档）
2. 如何追溯需求？（Epic → 模块实现）
3. 如何检查一致性？（跨模块接口是否一致）
```

### **2.2 SpecGovernor 的解决方案**

**采用两层需求结构：**

```
┌──────────────────────────────────────────────┐
│  High-level Artifacts（整体文档）             │
│  - 描述完整的业务需求和产品功能               │
│  - 提供系统级视图                            │
│  - 作为各模块的"契约"                        │
└────────────┬─────────────────────────────────┘
             │ 通过 requirements-map.json 映射
             ▼
┌──────────────────────────────────────────────┐
│  Module-level Artifacts（模块文档）           │
│  - 每个模块独立的需求、设计、测试文档         │
│  - 描述本模块负责的部分                      │
│  - 定义与其他模块的接口                      │
└──────────────────────────────────────────────┘
```

**支持灵活切换：**

| 项目规模 | 推荐结构 | 说明 |
|---------|---------|------|
| **小型（< 5 模块）** | **Flat 结构** | 所有内容在一个文档中，通过章节组织 |
| **中型（5-15 模块）** | **Hierarchical 结构** | 整体文档 + 模块文档分离 |
| **大型（> 15 模块）** | **Hierarchical 结构** + 需求映射 | 完整的两层管理 |

---

## **三、调整后的目录结构**

### **3.1 Flat 结构（小型项目）**

```
my-project/
├── .specgov/
│   ├── config.yml               # 配置文件
│   ├── state.json               # 流程状态
│   ├── index/
│   │   └── modules.json         # 模块定义
│   ├── artifacts/               # 文档制品（扁平）
│   │   ├── rd.md
│   │   ├── prd.md
│   │   ├── dd.md
│   │   └── td.md
│   ├── reviews/                 # 评审报告
│   │   ├── rd-review.json
│   │   └── ...
│   └── reports/                 # 分析和检查报告
├── src/                         # 源代码
└── tests/
```

### **3.2 Hierarchical 结构（中大型项目）**

```
my-project/
├── .specgov/
│   ├── config.yml
│   ├── state.json
│   ├── index/
│   │   ├── modules.json         # 模块定义
│   │   └── requirements-map.json # 需求映射（新增）
│   │
│   ├── artifacts/
│   │   ├── high-level/          # 整体文档（新增）
│   │   │   ├── rd.md            # 整体需求
│   │   │   ├── prd.md           # 整体产品设计
│   │   │   ├── dd.md            # 整体架构设计
│   │   │   └── td.md            # 整体测试策略
│   │   │
│   │   └── modules/             # 模块文档（新增）
│   │       ├── user/
│   │       │   ├── rd.md
│   │       │   ├── prd.md
│   │       │   ├── dd.md
│   │       │   └── td.md
│   │       ├── order/
│   │       │   └── ...
│   │       └── payment/
│   │           └── ...
│   │
│   ├── reviews/
│   │   ├── high-level/          # 整体文档评审
│   │   │   ├── rd-review.json
│   │   │   └── ...
│   │   └── modules/             # 模块文档评审
│   │       ├── user/
│   │       │   ├── rd-review.json
│   │       │   └── ...
│   │       └── ...
│   │
│   └── reports/
│       ├── impact/
│       └── consistency/
│           ├── module-user.json
│           └── requirement-REQ-001.json  # 跨模块检查报告
├── src/
└── tests/
```

---

## **四、核心数据结构**

### **4.1 requirements-map.json（需求映射）**

**作用：**
- 记录 high-level 需求与 module-level 实现的映射关系
- 支持需求追溯和跨模块一致性检查
- 轻量级，手动维护或辅助生成

**Schema：**

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
    "requirements": {
      "type": "array",
      "description": "高层需求列表（Epic/Feature 级别）",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "需求唯一标识（如 REQ-001）"
          },
          "title": {
            "type": "string",
            "description": "需求标题"
          },
          "type": {
            "type": "string",
            "enum": ["epic", "feature", "story"],
            "description": "需求类型"
          },
          "high_level_doc": {
            "type": "string",
            "description": "整体文档中的位置（如 .specgov/artifacts/high-level/rd.md#3.1-下单流程）"
          },
          "modules_involved": {
            "type": "array",
            "description": "涉及的模块列表",
            "items": {
              "type": "object",
              "properties": {
                "module_id": {
                  "type": "string",
                  "description": "模块 ID（对应 modules.json）"
                },
                "requirement_doc": {
                  "type": "string",
                  "description": "模块需求文档位置"
                },
                "description": {
                  "type": "string",
                  "description": "本模块负责的职责"
                }
              },
              "required": ["module_id", "description"]
            }
          },
          "status": {
            "type": "string",
            "enum": ["planned", "in_progress", "completed", "deprecated"],
            "description": "需求状态"
          },
          "priority": {
            "type": "string",
            "enum": ["P0", "P1", "P2", "P3"],
            "description": "优先级"
          }
        },
        "required": ["id", "title", "type", "modules_involved"]
      }
    }
  },
  "required": ["version", "requirements"]
}
```

**示例：**

```json
{
  "version": "1.0",
  "project": {
    "name": "E-Commerce Platform",
    "description": "电商平台后端服务"
  },
  "requirements": [
    {
      "id": "REQ-ORDER-001",
      "title": "用户在线下单",
      "type": "epic",
      "high_level_doc": ".specgov/artifacts/high-level/rd.md#3.1-下单流程",
      "modules_involved": [
        {
          "module_id": "user-module",
          "requirement_doc": ".specgov/artifacts/modules/user/rd.md#身份验证",
          "description": "用户登录验证和收货地址管理"
        },
        {
          "module_id": "order-module",
          "requirement_doc": ".specgov/artifacts/modules/order/rd.md#订单创建",
          "description": "订单创建、状态管理、订单查询"
        },
        {
          "module_id": "payment-module",
          "requirement_doc": ".specgov/artifacts/modules/payment/rd.md#支付处理",
          "description": "支付流程、支付回调、支付状态同步"
        },
        {
          "module_id": "inventory-module",
          "requirement_doc": ".specgov/artifacts/modules/inventory/rd.md#库存扣减",
          "description": "库存查询、库存锁定、库存扣减"
        }
      ],
      "status": "in_progress",
      "priority": "P0"
    },
    {
      "id": "REQ-ORDER-002",
      "title": "用户申请退款",
      "type": "feature",
      "high_level_doc": ".specgov/artifacts/high-level/rd.md#3.2-退款流程",
      "modules_involved": [
        {
          "module_id": "order-module",
          "requirement_doc": ".specgov/artifacts/modules/order/rd.md#退款申请",
          "description": "退款申请、退款审核、退款记录"
        },
        {
          "module_id": "payment-module",
          "requirement_doc": ".specgov/artifacts/modules/payment/rd.md#退款处理",
          "description": "退款到原支付渠道"
        }
      ],
      "status": "planned",
      "priority": "P1"
    }
  ]
}
```

### **4.2 modules.json（模块定义）**

保持与 v2 版本一致，无需修改。

---

## **五、调整后的命令体系**

### **5.1 项目初始化（支持结构选择）**

```bash
# 方式 1：自动判断（根据模块数量）
specgov init <project-name> --ai <backend>
# 如果检测到 < 5 个模块，使用 flat 结构
# 如果检测到 >= 5 个模块，使用 hierarchical 结构

# 方式 2：显式指定结构
specgov init <project-name> --ai <backend> --structure flat
specgov init <project-name> --ai <backend> --structure hierarchical

# 输出示例（hierarchical）：
# ✓ 项目初始化完成
# ✓ 结构类型：hierarchical（两层）
# ✓ 配置文件：.specgov/config.yml
# ✓ 模块索引：.specgov/index/modules.json
# ✓ 需求映射：.specgov/index/requirements-map.json（模板）
# ✓ 文档目录：.specgov/artifacts/high-level/ 和 .specgov/artifacts/modules/
```

**生成的 config.yml：**

```yaml
project:
  name: my-ecommerce
  structure: hierarchical  # flat | hierarchical

ai_backend:
  default: claude-code
  claude-code:
    command: claude-code execute
    model: claude-sonnet-4
  gemini-cli:
    command: gemini execute
    model: gemini-1.5-pro

features:
  requirements_mapping: true   # 是否使用需求映射
  cross_module_check: true     # 是否支持跨模块检查
```

### **5.2 文档生成命令（支持层次）**

#### **5.2.1 基础命令（适用于两种结构）**

**Flat 结构（单层）：**

```bash
# 生成需求文档
specgov rd:generate [--input=<file>] [--ai=<backend>]
# 输出：.specgov/artifacts/rd.md

# 评审需求文档
specgov rd:review [--ai=<backend>]
# 输出：.specgov/reviews/rd-review.json

# 修订需求文档
specgov rd:revise [--review=<file>]
# 输出：更新 .specgov/artifacts/rd.md
```

**Hierarchical 结构（两层）：**

```bash
# === High-level 文档（整体） ===
specgov rd:generate --level=high [--input=<file>]
# 输出：.specgov/artifacts/high-level/rd.md

specgov rd:review --level=high [--ai=<backend>]
# 输出：.specgov/reviews/high-level/rd-review.json

specgov rd:revise --level=high
# 更新：.specgov/artifacts/high-level/rd.md

# === Module-level 文档（模块） ===
specgov rd:generate --level=module --module=<module-id>
# 输出：.specgov/artifacts/modules/<module-id>/rd.md

specgov rd:review --level=module --module=<module-id>
# 输出：.specgov/reviews/modules/<module-id>/rd-review.json

# === 批量分解（新增）===
specgov rd:decompose
# 基于 high-level/rd.md 和 requirements-map.json
# 自动为每个涉及的模块生成 rd.md
```

#### **5.2.2 新增：rd:decompose（需求分解命令）**

**功能：**
- 读取整体需求文档（high-level/rd.md）
- 读取需求映射（requirements-map.json）
- 调用 AI 自动分解需求到各模块
- 生成各模块的 rd.md

**使用示例：**

```bash
# 分解所有模块的需求
$ specgov rd:decompose

正在分解需求...
  ✓ user-module: 已生成 .specgov/artifacts/modules/user/rd.md
  ✓ order-module: 已生成 .specgov/artifacts/modules/order/rd.md
  ✓ payment-module: 已生成 .specgov/artifacts/modules/payment/rd.md
  ✓ inventory-module: 已生成 .specgov/artifacts/modules/inventory/rd.md

总计：4 个模块需求文档已生成
建议：运行 specgov rd:review --level=module --module=<module> 进行评审

# 仅分解指定需求
$ specgov rd:decompose --requirement=REQ-ORDER-001
# 只分解 REQ-ORDER-001 涉及的模块
```

**实现逻辑（伪代码）：**

```python
def decompose_requirements(stage='rd', requirement_id=None):
    """
    将 high-level 文档分解为 module-level 文档
    """
    # 1. 读取整体文档
    high_level_doc = read_file('.specgov/artifacts/high-level/rd.md')

    # 2. 读取需求映射
    req_map = load_json('.specgov/index/requirements-map.json')

    # 3. 过滤需求（如果指定了 requirement_id）
    requirements = req_map['requirements']
    if requirement_id:
        requirements = [r for r in requirements if r['id'] == requirement_id]

    # 4. 对每个需求涉及的模块生成文档
    for req in requirements:
        for module_info in req['modules_involved']:
            module_id = module_info['module_id']

            # 构造提示词
            prompt = f"""
你是一位需求分析专家。请基于整体需求文档，生成 {module_id} 模块的需求文档。

【整体需求文档】
{high_level_doc}

【本模块信息】
- 需求 ID: {req['id']}
- 需求标题: {req['title']}
- 需求类型: {req['type']}
- 本模块职责: {module_info['description']}
- 相关章节: {req['high_level_doc']}

【其他关联模块】
{format_related_modules(req['modules_involved'], module_id)}

【任务】
请提取与 {module_id} 相关的需求，生成该模块的需求文档。

【要求】
1. 只包含本模块需要实现的功能
2. 明确定义与其他模块的接口（输入/输出）
3. 说明依赖的上游模块和下游模块
4. 包含本模块的非功能需求（性能、安全等）

【输出格式】
Markdown 格式，结构如下：
# {module_id} 模块需求文档

## 1. 模块概述
[描述本模块在整体需求中的角色]

## 2. 功能需求
[详细的功能需求列表]

## 3. 接口依赖
### 3.1 上游接口（本模块依赖的其他模块）
- 模块名: 接口定义
### 3.2 下游接口（本模块提供给其他模块）
- 接口定义

## 4. 非功能需求
[性能、安全、可靠性等]
"""

            # 调用 AI
            module_rd = call_ai(prompt)

            # 保存
            output_path = f'.specgov/artifacts/modules/{module_id}/rd.md'
            save_file(output_path, module_rd)
            print(f"  ✓ {module_id}: 已生成 {output_path}")
```

### **5.3 一致性检查（支持跨模块）**

#### **5.3.1 现有命令（保留）**

```bash
# 检查单个模块的一致性
specgov check --module=<module-id>
# 检查 RD ↔ PRD ↔ DD ↔ Code 的一致性

# 检查全项目（生成并行任务清单）
specgov check --scope=full
# 输出所有模块的检查任务，用户手动并行执行
```

#### **5.3.2 新增命令：跨模块一致性检查**

```bash
# 检查单个需求的跨模块一致性（核心场景）
specgov check --requirement=<requirement-id>
# 检查该需求涉及的所有模块之间的一致性

# 检查整体文档与模块文档的一致性
specgov check --level=cross-module
# 检查 high-level 文档是否与各 module-level 文档一致

# 检查模块间接口的一致性
specgov check --interface --between=<module1>,<module2>
# 检查两个模块之间的接口定义是否一致
```

**示例 1：检查单个需求的一致性**

```bash
$ specgov check --requirement=REQ-ORDER-001

正在检查需求 REQ-ORDER-001 的跨模块一致性...
  涉及模块：user-module, order-module, payment-module, inventory-module

[Consistency Agent 运行中...]

✓ 检查完成：.specgov/reports/consistency/requirement-REQ-ORDER-001.json

发现 2 处不一致：
  1. [接口不一致] order-module ↔ inventory-module
     - 位置：order-module 期望 inventory.lock(itemId, quantity)
     - 问题：inventory-module 提供的接口是 inventory.reserve(itemId, quantity)
     - 建议：统一接口名称为 reserve() 或在 order-module 中适配

  2. [数据结构不一致] order-module ↔ payment-module
     - 位置：订单金额字段
     - 问题：order-module 使用 totalAmount (integer, 分)
             payment-module 使用 amount (float, 元)
     - 建议：统一使用整数表示金额（分），避免浮点精度问题
```

**示例 2：检查整体与模块文档的一致性**

```bash
$ specgov check --level=cross-module

正在检查整体文档与模块文档的一致性...

[Consistency Agent 运行中...]

✓ 检查完成

覆盖度分析：
  ✓ REQ-ORDER-001: 完整覆盖（4/4 模块已实现）
  ⚠ REQ-ORDER-002: 部分覆盖（1/2 模块已实现）
    - 缺失：payment-module 的退款处理文档未生成

建议：
  - 运行 specgov rd:decompose --requirement=REQ-ORDER-002 生成缺失文档
```

**实现逻辑（伪代码）：**

```python
def check_requirement_consistency(requirement_id):
    """
    检查单个需求的跨模块一致性
    """
    # 1. 从 requirements-map.json 获取需求信息
    req_map = load_json('.specgov/index/requirements-map.json')
    req = find_requirement(req_map, requirement_id)

    if not req:
        raise ValueError(f"需求 {requirement_id} 不存在")

    # 2. 加载整体需求文档
    high_level_rd = load_doc_section(req['high_level_doc'])

    # 3. 加载所有涉及模块的文档（RD/PRD/DD）
    module_docs = []
    for module_info in req['modules_involved']:
        module_id = module_info['module_id']

        # 加载模块的所有文档
        module_rd = load_file(f'.specgov/artifacts/modules/{module_id}/rd.md')
        module_prd = load_file(f'.specgov/artifacts/modules/{module_id}/prd.md')
        module_dd = load_file(f'.specgov/artifacts/modules/{module_id}/dd.md')

        module_docs.append({
            'module_id': module_id,
            'description': module_info['description'],
            'rd': module_rd,
            'prd': module_prd,
            'dd': module_dd
        })

    # 4. 构造提示词
    prompt = f"""
你是一位软件质量专家。请检查跨模块需求的一致性。

【需求信息】
- ID: {req['id']}
- 标题: {req['title']}
- 类型: {req['type']}

【整体需求文档】
{high_level_rd}

【涉及的模块及其文档】
{format_module_docs_for_check(module_docs)}

【检查项】
1. **完整性检查**：各模块需求是否完整覆盖整体需求？是否有遗漏？
2. **接口一致性**：模块间的接口定义是否一致？
   - 接口名称、参数类型、返回值
   - 数据结构定义（字段名、类型、单位）
3. **职责边界**：各模块的职责划分是否清晰？是否有重叠或冲突？
4. **依赖关系**：模块间的依赖关系是否合理？是否有循环依赖？
5. **非功能需求**：性能、安全等非功能需求是否在各模块中得到体现？

【输出格式】
请以 JSON 格式输出检查结果：
{{
  "requirement_id": "{requirement_id}",
  "coverage": "完整|部分|缺失",
  "coverage_details": {{
    "total_modules": 4,
    "covered_modules": 4,
    "missing_aspects": ["..."]
  }},
  "inconsistencies": [
    {{
      "level": "critical|warning|info",
      "type": "接口不一致|数据结构不一致|职责冲突|需求遗漏|循环依赖",
      "modules": ["module1", "module2"],
      "location": "具体位置",
      "issue": "详细描述不一致之处",
      "suggestion": "修复建议"
    }}
  ],
  "summary": "总结性评价"
}}
"""

    # 5. 调用 AI
    response = call_ai(prompt, max_tokens=4000)

    # 6. 解析并保存报告
    report = parse_json(response)
    save_report(f'.specgov/reports/consistency/requirement-{requirement_id}.json', report)

    # 7. 格式化输出
    print_consistency_report(report)

    return report
```

### **5.4 影响分析（支持层次）**

```bash
# 分析整体文档变更的影响
specgov analyze --changed=.specgov/artifacts/high-level/rd.md
# 输出：影响的模块列表和下游文档

# 分析模块文档变更的影响
specgov analyze --changed=.specgov/artifacts/modules/user/rd.md
# 输出：影响的其他模块和上层文档

# 分析代码变更的影响（保留原功能）
specgov analyze --changed=src/order/order.service.ts
```

---

## **六、完整的工作流示例**

### **6.1 场景：开发电商下单功能（跨模块需求）**

**初始化项目（Hierarchical 结构）**

```bash
$ specgov init ecommerce-platform --ai claude-code --structure hierarchical

✓ 项目初始化完成
✓ 结构类型：hierarchical（两层）
✓ 配置文件：.specgov/config.yml
✓ 模块索引：.specgov/index/modules.json（包含 5 个模块）
✓ 需求映射：.specgov/index/requirements-map.json（模板）
```

**步骤 1：定义模块（编辑 modules.json）**

```json
{
  "version": "1.0",
  "modules": [
    {"id": "user-module", "name": "用户模块", ...},
    {"id": "order-module", "name": "订单模块", ...},
    {"id": "payment-module", "name": "支付模块", ...},
    {"id": "inventory-module", "name": "库存模块", ...}
  ]
}
```

**步骤 2：生成整体需求文档**

```bash
$ specgov rd:generate --level=high --input=user-stories/order-flow.md

[Generator Agent 运行中...]
✓ 生成完成：.specgov/artifacts/high-level/rd.md

$ specgov rd:review --level=high --ai=gemini-cli

[Reviewer Agent 运行中...]
✓ 评审完成：.specgov/reviews/high-level/rd-review.json
  发现 1 个建议，0 个严重问题

$ specgov rd:revise --level=high

[Generator Agent 运行中...]
✓ 修订完成：.specgov/artifacts/high-level/rd.md (v2)
```

**步骤 3：定义需求映射（编辑 requirements-map.json）**

```json
{
  "requirements": [
    {
      "id": "REQ-ORDER-001",
      "title": "用户在线下单",
      "type": "epic",
      "high_level_doc": ".specgov/artifacts/high-level/rd.md#3.1-下单流程",
      "modules_involved": [
        {"module_id": "user-module", "description": "用户身份验证"},
        {"module_id": "order-module", "description": "订单创建"},
        {"module_id": "payment-module", "description": "支付处理"},
        {"module_id": "inventory-module", "description": "库存扣减"}
      ],
      "status": "in_progress",
      "priority": "P0"
    }
  ]
}
```

**步骤 4：分解需求到各模块**

```bash
$ specgov rd:decompose --requirement=REQ-ORDER-001

正在分解需求 REQ-ORDER-001...
  [Generator Agent 运行中] user-module
  ✓ user-module: 已生成 .specgov/artifacts/modules/user/rd.md

  [Generator Agent 运行中] order-module
  ✓ order-module: 已生成 .specgov/artifacts/modules/order/rd.md

  [Generator Agent 运行中] payment-module
  ✓ payment-module: 已生成 .specgov/artifacts/modules/payment/rd.md

  [Generator Agent 运行中] inventory-module
  ✓ inventory-module: 已生成 .specgov/artifacts/modules/inventory/rd.md

总计：4 个模块需求文档已生成
```

**步骤 5：并行评审各模块需求**

```bash
# 启动 4 个终端，并行评审
终端 1: specgov rd:review --level=module --module=user-module --ai=gemini
终端 2: specgov rd:review --level=module --module=order-module --ai=gemini
终端 3: specgov rd:review --level=module --module=payment-module --ai=gemini
终端 4: specgov rd:review --level=module --module=inventory-module --ai=gemini

# 每个终端输出：
✓ 评审完成：.specgov/reviews/modules/<module>/rd-review.json
```

**步骤 6：检查跨模块一致性**

```bash
$ specgov check --requirement=REQ-ORDER-001

正在检查需求 REQ-ORDER-001 的跨模块一致性...
  涉及模块：user-module, order-module, payment-module, inventory-module

[Consistency Agent 运行中...]

✓ 检查完成：.specgov/reports/consistency/requirement-REQ-ORDER-001.json

发现 1 处不一致：
  1. [接口不一致] order-module ↔ inventory-module
     - 问题：order-module 期望同步库存扣减，inventory-module 设计为异步
     - 建议：统一为异步接口，order-module 监听库存扣减完成事件

请修复后重新检查。
```

**步骤 7：修复不一致并重新检查**

```bash
# 修改 order-module/rd.md 和 inventory-module/rd.md

$ specgov check --requirement=REQ-ORDER-001

✓ 检查完成：全部一致 ✓
```

**步骤 8：继续生成 PRD、DD、TD**

```bash
# 整体 PRD
$ specgov prd:generate --level=high --based-on=rd
$ specgov prd:review --level=high

# 分解到各模块
$ specgov prd:decompose --requirement=REQ-ORDER-001

# 检查一致性
$ specgov check --requirement=REQ-ORDER-001
```

---

## **七、非功能需求**

### **7.1 性能指标**

| 操作 | 时间 | 成本 | 说明 |
|------|------|------|------|
| 项目初始化 | < 1 分钟 | $0 | 创建目录和配置文件 |
| 整体文档生成 | < 5 分钟 | < $0.20 | 调用 AI 生成 high-level 文档 |
| 需求分解（4 模块） | < 8 分钟 | < $0.40 | 并行调用 AI 生成 4 个模块文档 |
| 跨模块一致性检查 | < 5 分钟 | < $0.15 | 检查单个需求涉及的 4 个模块 |
| 影响分析 | < 2 分钟 | < $0.05 | 基于 AI 分析 |
| 全项目检查（10 模块） | < 5 分钟 | < $1.00 | 手动并行检查 |

### **7.2 成本估算（月度）**

| 场景 | 频率 | 单次成本 | 月成本 |
|------|------|---------|--------|
| 整体文档生成和评审 | 2 次/月 | $0.40 | $0.80 |
| 需求分解（4 模块） | 2 次/月 | $0.40 | $0.80 |
| 跨模块一致性检查 | 10 次/月 | $0.15 | $1.50 |
| 单模块检查 | 20 次/月 | $0.10 | $2.00 |
| 影响分析 | 15 次/月 | $0.05 | $0.75 |
| 全项目检查 | 4 次/月 | $1.00 | $4.00 |
| **总计** | - | - | **< $10/月** |

**对比 v2 版本：**
- v2 版本估算：< $20/月
- v3 版本（层次化）：< $10/月（因为分模块后上下文更小）

---

## **八、实现优先级**

### **阶段 1: 基础框架（2-3 周）**
- Fork spec-kit 仓库
- 实现 `specgov init` 命令（支持 flat/hierarchical 结构选择）
- 实现 modules.json 和 requirements-map.json 的创建
- 实现单层结构的基础命令（rd:generate/review/revise）

### **阶段 2: 两层结构支持（2-3 周）**
- 实现 `--level=high` 和 `--level=module` 参数
- 实现 `rd:decompose` 命令（需求分解）
- 实现 high-level 和 module-level 的文档管理

### **阶段 3: 跨模块一致性检查（2-3 周）**
- 实现 `check --requirement` 命令
- 实现 `check --level=cross-module` 命令
- 实现跨模块一致性检查的 AI 提示词

### **阶段 4: 完整工作流（3-4 周）**
- 实现 PRD/DD/TD 的两层结构支持
- 实现各阶段的 decompose 命令
- 完善影响分析（支持层次结构）

### **阶段 5: 优化和测试（1-2 周）**
- 端到端测试（完整的跨模块需求场景）
- 性能优化和成本控制
- 编写用户文档和示例

---

## **九、与 v2 版本的对比**

| 维度 | v2（简化版） | v3（层次化版） | 变化 |
|------|-------------|---------------|------|
| **目录结构** | 单层（artifacts/） | 可选两层（high-level/ + modules/） | ✅ 灵活性 +50% |
| **需求管理** | 仅模块级 | 支持 Epic → Module 映射 | ✅ 功能 +100% |
| **跨模块检查** | 不支持 | 支持 `check --requirement` | ✅ 核心场景支持 |
| **需求分解** | 手动 | 支持 `rd:decompose` | ✅ 效率 +80% |
| **实现复杂度** | 低 | 中等 | ⚠️ 复杂度 +30% |
| **适用场景** | < 5 模块小项目 | 所有规模项目 | ✅ 适用性 +200% |
| **月成本** | < $20 | < $10 | ✅ 成本 -50% |

---

## **十、总结**

**SpecGovernor v3（层次化版本）的核心价值：**

1. ✅ **解决实际问题**：支持跨模块需求管理，符合真实项目场景
2. ✅ **灵活可扩展**：小项目用 flat，大项目用 hierarchical
3. ✅ **核心创新保留**：Generator-Reviewer 对 + 五阶段工作流
4. ✅ **成本更低**：分模块后上下文更小，成本降低 50%
5. ✅ **实现可控**：基于 spec-kit，复杂度增加有限（+30%）

**关键调整点：**
- 新增：requirements-map.json（需求映射）
- 新增：两层目录结构（high-level + modules）
- 新增：rd:decompose（需求分解命令）
- 新增：check --requirement（跨模块一致性检查）

**下一步：**
开始基于 spec-kit 实现 v3 版本的核心功能，优先实现两层结构和需求分解。
