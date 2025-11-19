# SpecGovernor 结构重组计划

## 问题诊断

**当前问题**：SpecGovernor 自身被当作"用户项目"来组织，导致结构混乱。

**核心原则**：
- SpecGovernor = 工具包（提供模板、脚本、文档）
- 用户项目 = 使用 SpecGovernor 的项目（安装后获得 `.specgov/` 目录）

---

## 新结构设计

```
SpecGovernor/                           # 工具包仓库
│
├── templates/                          # 📦 模板资源（复制到用户项目 .specgov/）
│   ├── prompts/                       # Prompt 模板
│   │   ├── prd-generator.md
│   │   ├── prd-reviewer.md
│   │   ├── prd-overview-generator.md
│   │   ├── prd-module-generator.md
│   │   ├── design-generator.md
│   │   ├── design-reviewer.md
│   │   ├── design-overview-generator.md
│   │   ├── design-module-generator.md
│   │   ├── test-plan-generator.md
│   │   ├── test-plan-reviewer.md
│   │   ├── test-plan-overview-generator.md
│   │   ├── test-plan-module-generator.md
│   │   ├── code-generator.md
│   │   ├── code-reviewer.md
│   │   ├── consistency-checker.md
│   │   └── impact-analyzer.md
│   │
│   ├── workflows/                     # 工作流文档模板
│   │   ├── workflow-overview.md
│   │   ├── workflow-prd.md
│   │   ├── workflow-design.md
│   │   ├── workflow-test-plan.md
│   │   ├── workflow-code.md
│   │   ├── workflow-task-mgmt.md
│   │   └── workflow-large-project.md
│   │
│   ├── tasks/                         # 任务文件模板
│   │   ├── project-manager.md
│   │   ├── product-manager.md
│   │   ├── architect.md
│   │   ├── test-manager.md
│   │   └── developer.md
│   │
│   ├── claude-commands/               # Claude Code 斜杠命令模板
│   │   ├── specgov-prd-gen.md
│   │   ├── specgov-prd-review.md
│   │   ├── specgov-prd-overview.md
│   │   ├── specgov-prd-module.md
│   │   ├── specgov-design-gen.md
│   │   ├── specgov-design-review.md
│   │   ├── specgov-design-overview.md
│   │   ├── specgov-design-module.md
│   │   ├── specgov-test-gen.md
│   │   ├── specgov-test-review.md
│   │   ├── specgov-test-overview.md
│   │   ├── specgov-test-module.md
│   │   ├── specgov-code-gen.md
│   │   ├── specgov-code-review.md
│   │   ├── specgov-consistency.md
│   │   └── specgov-impact.md
│   │
│   ├── raw-requirements/              # 原始需求模板
│   │   ├── inputs-template.md        # 小项目模板
│   │   ├── overview-template.md      # 大项目总览模板
│   │   └── module-template.md        # 大项目模块模板
│   │
│   └── index/                         # 索引目录占位符
│       └── .gitkeep
│
├── scripts/                            # 🛠️ Helper Scripts（复制到用户项目 .specgov/scripts/）
│   ├── init_project.py                # 项目初始化脚本
│   ├── parse_tags.py                  # 标记解析脚本
│   ├── build_graph.py                 # 依赖图构建脚本
│   ├── impact_analysis.py             # 影响分析脚本
│   └── check_consistency.py           # 一致性检查脚本
│
├── install/                            # 📥 安装脚本
│   ├── install-specgov.ps1           # Windows 安装脚本
│   └── install-specgov.sh            # Linux/Mac 安装脚本
│
├── docs/                               # 📚 SpecGovernor 自身文档
│   ├── PRD.md                         # SpecGovernor 产品需求
│   ├── Design-Document.md             # SpecGovernor 设计文档
│   ├── Test-Plan.md                   # SpecGovernor 测试计划
│   └── examples/                      # 示例项目（可选）
│       ├── small-project-example/
│       └── large-project-example/
│
├── README.md                           # 主说明文档
├── CLAUDE.md                           # Claude Code 项目指南
├── GEMINI.md                           # Gemini 项目指南
├── INSTALLATION.md                     # 安装指南
├── QUICK-START.md                      # 快速开始指南
├── LICENSE                             # 许可证
└── .gitignore                          # Git 忽略配置
```

---

## 重组操作清单

### 第一步：创建新目录结构

```bash
mkdir -p templates/prompts
mkdir -p templates/workflows
mkdir -p templates/tasks
mkdir -p templates/claude-commands
mkdir -p templates/raw-requirements
mkdir -p templates/index
mkdir -p scripts
mkdir -p install
mkdir -p docs
mkdir -p docs/examples
```

### 第二步：移动模板资源

```bash
# 移动 prompts
mv .specgov/prompts/* templates/prompts/

# 移动 workflows
mv .specgov/workflows/* templates/workflows/

# 移动 tasks
mv .specgov/tasks/* templates/tasks/
```

### 第三步：移动脚本

```bash
# 移动 helper scripts
mv .specgov/scripts/init_project.py scripts/
mv .specgov/scripts/parse_tags.py scripts/
mv .specgov/scripts/build_graph.py scripts/
mv .specgov/scripts/impact_analysis.py scripts/
mv .specgov/scripts/check_consistency.py scripts/

# 清理临时脚本（merge_rd_prd.py, refactor_templates.py, finalize_refactoring.py）
# 这些是一次性重构脚本，不需要保留
rm .specgov/scripts/merge_rd_prd.py
rm .specgov/scripts/refactor_templates.py
rm .specgov/scripts/finalize_refactoring.py
```

### 第四步：移动安装脚本

```bash
mv install-specgov.ps1 install/
mv install-specgov.sh install/
```

### 第五步：移动文档

```bash
mv PRD.md docs/
mv Design-Document.md docs/
mv Test-Plan.md docs/
```

### 第六步：清理 .specgov 目录

```bash
# 删除现在为空的 .specgov 目录
rm -rf .specgov
```

### 第七步：创建模板文件

需要创建以下模板文件：

1. `templates/raw-requirements/inputs-template.md` - 小项目原始需求模板
2. `templates/raw-requirements/overview-template.md` - 大项目总览需求模板
3. `templates/raw-requirements/module-template.md` - 大项目模块需求模板
4. `templates/claude-commands/*.md` - 16 个斜杠命令文件

### 第八步：更新引用

需要更新以下文件中的路径引用：

1. **scripts/init_project.py**：
   - 更新模板路径从 `.specgov/prompts/` → `templates/prompts/`
   - 更新脚本复制路径

2. **install/install-specgov.ps1**：
   - 更新下载路径

3. **install/install-specgov.sh**：
   - 更新下载路径

4. **README.md**：
   - 更新项目结构说明
   - 更新快速开始命令

5. **INSTALLATION.md**：
   - 更新安装脚本路径

6. **QUICK-START.md**：
   - 更新文件路径引用

---

## 变更影响分析

### 用户侧影响

✅ **无影响**：用户项目结构不变，仍然是：
```
user-project/
├── .specgov/
│   ├── prompts/
│   ├── workflows/
│   ├── tasks/
│   └── scripts/
└── docs/
```

### SpecGovernor 仓库侧影响

✅ **更清晰的职责**：
- `templates/` - 明确标识这些是要分发的模板
- `scripts/` - 明确标识这些是要复制的脚本
- `install/` - 明确标识这些是安装工具
- `docs/` - 明确标识这些是 SpecGovernor 自身的文档

✅ **更好的维护性**：
- 分离关注点：工具包资源 vs. 工具包自身文档
- 便于理解：新贡献者能立即理解项目结构

---

## 验证检查清单

重组完成后，验证以下内容：

- [ ] `templates/` 目录包含所有模板资源
- [ ] `scripts/` 目录包含所有 helper scripts
- [ ] `install/` 目录包含安装脚本
- [ ] `docs/` 目录包含 SpecGovernor 自身文档
- [ ] `.specgov/` 目录已删除
- [ ] `scripts/init_project.py` 路径引用已更新
- [ ] 安装脚本路径引用已更新
- [ ] README.md 结构说明已更新
- [ ] 运行 `python scripts/init_project.py` 能正确初始化测试项目
- [ ] Git commit 记录变更历史

---

## 优势总结

1. **符合 PRD 定义**：SpecGovernor 作为工具包，结构清晰明确
2. **分发友好**：`templates/` 和 `scripts/` 目录可以直接打包分发
3. **维护简单**：职责分离，修改模板不会影响文档，反之亦然
4. **扩展容易**：添加新模板或脚本只需放入对应目录
5. **理解直观**：新用户或贡献者能快速理解项目组织逻辑

---

**执行时机**：立即执行

**预计时间**：30 分钟

**风险等级**：低（所有变更通过 Git 可追溯和回滚）
