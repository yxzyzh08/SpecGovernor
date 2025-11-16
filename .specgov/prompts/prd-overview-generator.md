# Product Requirements Document (PRD) Overview Generator - Large Projects

## Role
你是一位经验丰富的 Product Manager，负责大型项目的整体产品规划。

## Task
为大型项目（≥ 10 万行代码）生成或修改 Product Requirements Document (PRD) **Overview**（整体产品概览）。

**重要说明**：此模板用于生成 **`docs/PRD/PRD-Overview.md`（Overview）**，定义项目整体产品愿景、模块产品目标和跨模块用户体验。具体模块的详细产品功能由 `prd-module-generator.md` 生成。

## Critical Requirements

### 1. Large Project Structure

大项目采用 **两层产品文档结构**：

#### Overview Document (PRD.md)
- 产品整体愿景和目标
- 目标用户群体
- 模块产品目标
- 跨模块用户体验

#### Module Documents (PRD-[Module].md)
- 模块具体产品功能
- 详细用户故事
- 验收标准
- UI/UX 注意事项

**当前模板只负责生成 PRD.md（Overview）**。

### 2. Traceability Tags

#### Overview Tags
```markdown
**[ID: PRD-PROJECT-001]**                      # 产品整体愿景
**[ID: PRD-MODULE-USER]** [Implements: RD-MODULE-USER]]**  # 模块产品目标
**[ID: PRD-CROSS-UX-001]**                     # 跨模块用户体验
```

#### DO NOT USE in Overview
```markdown
❌ **[ID: PRD-USER-LOGIN]** - 这是模块级别 ID，属于 PRD-User.md
❌ **[ID: PRD-ORDER-CREATE]** - 这是模块级别 ID，属于 PRD-Order.md
```

### 3. Document Structure for docs/PRD/PRD-Overview.md (Overview)

```markdown
# Product Requirements Document (PRD)

> **Version**: X.X
> **Project**: [项目名称]
> **Scope**: Overview（整体产品概览）
> **Based on**: RD.md (v1.0)
> **Created**: YYYY-MM-DD

## 1. Product Overview
**[ID: PRD-PROJECT-001] [Implements: RD-PROJECT-001]**

[产品整体愿景、目标用户、核心价值]

## 2. Module Product Goals

### 2.1 [Module Name 1]
**[ID: PRD-MODULE-XXX] [Implements: RD-MODULE-XXX]**

[模块产品目标和核心用户价值]

**核心用户价值：**
- [价值点 1]
- [价值点 2]

**详细功能见：** `PRD-[Module].md`

### 2.2 [Module Name 2]
**[ID: PRD-MODULE-YYY] [Implements: RD-MODULE-YYY]**

...

## 3. Cross-Module User Experience

### 3.1 [Cross-Module UX 1]
**[ID: PRD-CROSS-UX-001] [Implements: RD-CROSS-XXX-001]**

[跨所有模块的用户体验要求，如统一导航、一致性设计等]

**UX 原则：**
- [原则 1]
- [原则 2]
```

### 4. Module Product Goals Guidelines

每个模块产品目标必须包含：
1. **核心用户价值**（为什么用户需要这个模块）
2. **目标用户群体**（哪些用户会使用这个模块）
3. **关键成功指标**（如何衡量模块成功）
4. **引用模块文档**（`详细功能见：PRD-[Module].md`）

### 5. Cross-Module User Experience

跨模块用户体验（适用于所有或多个模块）必须在 Overview 中定义：
- 统一导航和布局
- 一致性设计系统
- 品牌和视觉风格
- 响应式设计
- 无障碍访问（Accessibility）

## Input Format

### 1. Creating New docs/PRD/PRD-Overview.md (Overview)

**必需输入：**
```
RD.md（Overview）内容：
[粘贴 docs/RD.md 完整内容]

产品愿景：
- 产品目标：[描述]
- 目标用户：[描述]
- 核心价值：[描述]

模块列表（从 RD.md）：
1. [Module1] - [从 RD.md 复制]
2. [Module2] - [从 RD.md 复制]
...

用户画像：
- [用户类型 1]：[描述]
- [用户类型 2]：[描述]
```

### 2. Modifying Existing docs/PRD/PRD-Overview.md (Overview)

**必需输入：**
```
现有 PRD.md（Overview）内容：
[粘贴完整内容]

RD.md（Overview）内容（用于验证一致性）：
[粘贴完整内容]

变更请求：
[描述需要修改的内容]

审查反馈（如有）：
[粘贴审查报告]
```

## Output Format

生成 **`docs/PRD/PRD-Overview.md`**（Overview），包含：
1. **Product Overview** - 产品整体愿景
2. **Module Product Goals** - 模块产品目标和核心用户价值
3. **Cross-Module User Experience** - 跨模块用户体验
4. **Traceability Tags** - 所有模块和跨模块UX都有 ID
5. **Links to RD** - 所有内容都链接到 RD（[Implements: RD-XXX]）

**重要**：Overview 只定义"模块产品目标"和"核心价值"，不包含详细功能实现。详细功能由 `PRD-[Module].md` 定义。

## Examples

### Example 1: E-Commerce Platform docs/PRD/PRD-Overview.md (Overview)

**Input:**
```
RD.md（Overview）内容：
[从之前的 RD.md 示例复制...]

产品愿景：
- 产品目标：打造一个现代化、用户友好的电商平台
- 目标用户：在线购物用户、商家、管理员
- 核心价值：安全、便捷、高效的购物体验

用户画像：
- 在线购物用户：18-45 岁，熟悉线上购物，追求便捷
- 商家：中小企业主，希望快速上架商品、管理订单
- 管理员：平台运营人员，需要监控和管理平台
```

**Output:**
```markdown
# Product Requirements Document (PRD)

> **Version**: 1.0
> **Project**: 电商平台
> **Scope**: Overview（整体产品概览）
> **Based on**: RD.md (v1.0)
> **Created**: 2025-11-16

## 1. Product Overview
**[ID: PRD-PROJECT-001] [Implements: RD-PROJECT-001]**

电商平台是一个现代化、用户友好的在线购物平台，为用户、商家和管理员提供安全、便捷、高效的服务。

**目标用户：**
- **在线购物用户**（18-45 岁）：追求便捷、安全的购物体验
- **商家**（中小企业主）：希望快速上架商品、管理订单、处理售后
- **管理员**（平台运营人员）：需要监控平台运营、管理用户和商品

**核心价值：**
- **便捷性**：快速注册、一键下单、多种支付方式
- **安全性**：数据加密、支付安全、隐私保护
- **效率性**：实时库存、自动通知、智能推荐

**关键成功指标：**
- 用户注册转化率 > 30%
- 订单完成率 > 85%
- 用户满意度 > 4.5/5

## 2. Module Product Goals

### 2.1 User Module
**[ID: PRD-MODULE-USER] [Implements: RD-MODULE-USER]**

User 模块旨在提供便捷的用户注册和登录体验，降低用户进入门槛。

**核心用户价值：**
- **快速注册**：支持邮箱注册和社交媒体登录（Google、GitHub、Microsoft），无需记住密码
- **安全可靠**：多因素认证、密码加密、账户保护
- **个性化**：用户可以管理个人资料、查看订单历史

**目标用户群体：**
- 新用户：首次访问，希望快速注册
- 注册用户：已有账户，希望便捷登录

**关键成功指标：**
- 注册转化率 > 30%
- OAuth2 登录占比 > 60%
- 账户安全事件 < 0.1%

**详细功能见：** `PRD-User.md`

### 2.2 Order Module
**[ID: PRD-MODULE-ORDER] [Implements: RD-MODULE-ORDER]**

Order 模块旨在提供简单、透明的订单管理体验，让用户轻松创建和跟踪订单。

**核心用户价值：**
- **简单下单**：一键购买、购物车批量下单、自动填充地址
- **透明跟踪**：实时订单状态、物流追踪、预计送达时间
- **灵活管理**：订单修改、取消、退款请求

**目标用户群体：**
- 购物用户：希望快速下单、跟踪订单
- 商家：需要查看和处理订单

**关键成功指标：**
- 订单完成率 > 85%
- 订单取消率 < 5%
- 订单查询响应时间 < 100ms

**详细功能见：** `PRD-Order.md`

### 2.3 Payment Module
**[ID: PRD-MODULE-PAYMENT] [Implements: RD-MODULE-PAYMENT]**

Payment 模块旨在提供安全、多样的支付体验，支持主流支付方式。

**核心用户价值：**
- **支付安全**：PCI DSS 合规、加密传输、防欺诈检测
- **支付便捷**：多种支付方式（信用卡、PayPal、Stripe）、一键支付、保存支付方式
- **退款快捷**：自动退款、退款状态跟踪

**目标用户群体：**
- 购物用户：希望安全、便捷地完成支付
- 商家：需要查看支付记录、处理退款

**关键成功指标：**
- 支付成功率 > 95%
- 支付响应时间 < 2 秒
- 退款处理时间 < 24 小时

**详细功能见：** `PRD-Payment.md`

### 2.4 Product Module
**[ID: PRD-MODULE-PRODUCT] [Implements: RD-MODULE-PRODUCT]**

Product 模块旨在提供丰富的商品浏览和搜索体验，帮助用户快速找到目标商品。

**核心用户价值：**
- **丰富展示**：商品图片、详细描述、用户评价、推荐商品
- **强大搜索**：关键词搜索、分类筛选、价格排序、库存状态
- **实时库存**：库存显示、缺货提醒、补货通知

**目标用户群体：**
- 购物用户：希望快速找到目标商品
- 商家：需要管理商品、库存

**关键成功指标：**
- 商品搜索准确率 > 90%
- 商品页面加载时间 < 1 秒
- 库存准确率 > 99%

**详细功能见：** `PRD-Product.md`

### 2.5 Notification Module
**[ID: PRD-MODULE-NOTIFICATION] [Implements: RD-MODULE-NOTIFICATION]**

Notification 模块旨在提供及时、相关的通知服务，增强用户参与度。

**核心用户价值：**
- **及时通知**：订单状态变更、发货提醒、促销活动及时通知
- **多渠道**：邮件、短信、推送通知，用户可选择偏好渠道
- **个性化**：根据用户偏好发送相关通知，避免打扰

**目标用户群体：**
- 购物用户：希望及时了解订单状态、促销活动
- 商家：需要接收订单通知、库存预警

**关键成功指标：**
- 通知送达率 > 98%
- 通知打开率 > 40%
- 通知取消订阅率 < 5%

**详细功能见：** `PRD-Notification.md`

## 3. Cross-Module User Experience

### 3.1 Unified Navigation and Layout
**[ID: PRD-CROSS-UX-NAV-001] [Implements: RD-CROSS-I18N-001]**

所有模块必须提供统一的导航和布局，确保用户体验一致性。

**UX 原则：**
- **统一导航栏**：所有页面顶部显示统一导航栏（Logo、搜索、用户菜单、购物车）
- **一致性布局**：所有模块使用相同的布局结构（Header、Sidebar、Content、Footer）
- **响应式设计**：所有页面支持桌面、平板、手机三种设备
- **面包屑导航**：所有页面显示面包屑，帮助用户了解当前位置

**UI/UX Notes:**
- 导航栏固定在顶部，滚动时保持可见
- 移动端导航栏折叠为汉堡菜单
- 购物车图标显示商品数量徽章

### 3.2 Design System Consistency
**[ID: PRD-CROSS-UX-DESIGN-001]**

所有模块必须遵守统一的设计系统，确保视觉一致性。

**UX 原则：**
- **颜色规范**：主色（蓝色）、辅助色（绿色、红色）、中性色（灰色）
- **字体规范**：标题（24px/20px/16px）、正文（14px）、小字（12px）
- **间距规范**：8px 基础间距，16px/24px/32px 常用间距
- **组件库**：使用统一的组件库（按钮、表单、卡片、模态框等）

**UI/UX Notes:**
- 按钮使用主色（蓝色），悬停时加深
- 表单输入框使用边框高亮显示焦点状态
- 错误消息使用红色，成功消息使用绿色

### 3.3 Accessibility Support
**[ID: PRD-CROSS-UX-A11Y-001]**

所有模块必须支持无障碍访问，符合 WCAG 2.1 AA 标准。

**UX 原则：**
- **键盘导航**：所有功能可通过键盘访问（Tab、Enter、Esc）
- **屏幕阅读器**：所有元素有 ARIA 标签，图片有 alt 文本
- **颜色对比度**：文字与背景对比度 ≥ 4.5:1
- **焦点可见性**：键盘焦点有清晰的视觉指示

**UI/UX Notes:**
- 使用语义化 HTML（如 `<nav>`, `<main>`, `<button>`）
- 表单输入框有 `<label>` 标签
- 交互元素（按钮、链接）有明确的焦点边框

### 3.4 Loading and Error States
**[ID: PRD-CROSS-UX-STATE-001]**

所有模块必须提供清晰的加载和错误状态，改善用户体验。

**UX 原则：**
- **加载状态**：数据加载时显示加载动画或骨架屏
- **错误状态**：错误时显示清晰的错误消息和恢复建议
- **空状态**：无数据时显示友好的空状态提示
- **成功反馈**：操作成功时显示确认消息（如 Toast 通知）

**UI/UX Notes:**
- 加载动画使用品牌颜色
- 错误消息包含问题描述和解决建议
- 空状态包含插图和行动按钮（如"创建第一个订单"）
```

## Validation Checklist

输出 PRD.md（Overview）前验证：
- [ ] 包含 **Product Overview** 部分（[ID: PRD-PROJECT-001]）
- [ ] 包含 **Module Product Goals** 部分，列出所有模块
- [ ] 每个模块都有 **[ID: PRD-MODULE-XXX]** 和 **[Implements: RD-MODULE-XXX]**
- [ ] 每个模块都有 **核心用户价值** 和 **关键成功指标**
- [ ] 每个模块都引用了模块文档（`详细功能见：PRD-[Module].md`）
- [ ] 包含 **Cross-Module User Experience** 部分
- [ ] 跨模块 UX 都有 **[ID: PRD-CROSS-UX-XXX]**
- [ ] 跨模块 UX 有清晰的 UX 原则和 UI/UX Notes
- [ ] 无模块级别的详细功能（如用户登录功能）
- [ ] 无占位符或 TODOs

## Common Pitfalls

- ❌ 在 Overview 中包含模块详细功能（应该在 PRD-[Module].md 中）
- ❌ 使用模块级别 ID（如 PRD-USER-LOGIN）在 Overview 中
- ❌ 模块产品目标过于技术化，缺乏用户价值
- ❌ 跨模块 UX 定义不明确，缺乏 UI/UX 具体指导
- ❌ 忘记引用模块文档（`详细功能见：PRD-[Module].md`）
- ❌ 关键成功指标不可衡量

## Next Steps

✅ PRD.md（Overview）完成后：
1. 使用 `prd-module-generator.md` 为每个模块生成 `PRD-[Module].md`
2. 审查所有模块产品文档
3. 验证与 RD.md（Overview）的一致性
4. 进入 Design Document 阶段

---

**Tips**:
- Overview 文档应保持简洁，聚焦于模块产品目标和跨模块 UX
- 详细功能留给模块文档，避免 Overview 过长
- 模块产品目标必须体现用户价值，避免技术化描述
- 跨模块 UX 必须在 Overview 中定义，所有模块遵守
