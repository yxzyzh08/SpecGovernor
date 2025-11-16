# **📦 Product Requirements Document (PRD) - SpecGovernor**

> **Version**: v2.0
> **Based on**: RD.md (v2.0)
> **Created**: 2025-11-16
> **Updated**: 2025-11-16
> **Product Type**: Toolkit (Prompt Templates + Workflow Documentation + Helper Scripts)

---

## **Traceability Declaration**

This document implements the following requirements from RD.md:
- [Implements: RD-GOAL-001] 提供标准化提示词模板
- [Implements: RD-GOAL-002] 定义规范化开发流程
- [Implements: RD-GOAL-003] 实现可追溯性
- [Implements: RD-GOAL-004] 提供辅助工具
- [Implements: RD-USER-001] 服务超级个体用户

---

## **一、Product Overview**

### **1.1 Product Vision**

**[ID: PRD-VISION-001] [Implements: RD-GOAL-001]**

SpecGovernor is a **comprehensive toolkit** designed for **Super Individuals** (超级个体), providing:

- **Prompt templates** for generating standardized RD/PRD/Design Document/Test Plan/Code with Claude Code
- **Workflow documentation** guiding humans through structured development processes
- **Helper scripts** for parsing traceability tags, building dependency graphs, and impact analysis

**Core Value Proposition:**
- 🎯 **Explicit Traceability**: 100% reliable tracking through embedded tags, no AI inference needed
- 🔄 **Dual Quality Assurance**: Generator-Reviewer template pairs for each stage
- 📦 **Zero Installation**: Simple file templates you use directly with Claude Code
- 💰 **Cost-Effective**: No software license, just templates and scripts

---

### **1.2 Target User Profile**

**[ID: PRD-USER-001] [Implements: RD-USER-001]**

| User Type | Typical Scenario | Pain Point |
|---------|---------|------|
| **Independent Developer** | Building SaaS products | Documents out of sync with code, hard to track requirements changes |
| **Tech Entrepreneur** | MVP rapid iteration | Wearing multiple hats, high documentation cost |
| **Small Team Tech Lead** | Managing 5-10 person team | Need process but no dedicated PM/QA |

---

### **1.3 Product Structure**

**[ID: PRD-STRUCTURE-001]**

```
SpecGovernor Toolkit
├── Prompt Templates (提示词模板)
│   ├── rd-generator.md          # Generate/modify Requirements Document
│   ├── rd-reviewer.md           # Review Requirements Document
│   ├── prd-generator.md         # Generate/modify Product Requirements Document
│   ├── prd-reviewer.md          # Review Product Requirements Document
│   ├── design-generator.md      # Generate/modify Design Document
│   ├── design-reviewer.md       # Review Design Document
│   ├── test-plan-generator.md   # Generate/modify Test Plan
│   ├── test-plan-reviewer.md    # Review Test Plan
│   └── code-generator.md        # Generate/modify Code
│
├── Workflow Documentation (流程文档)
│   ├── workflow-overview.md     # Overall SDLC workflow
│   ├── workflow-rd.md           # RD generation workflow
│   ├── workflow-prd.md          # PRD generation workflow
│   ├── workflow-design.md       # Design Document workflow
│   ├── workflow-test-plan.md    # Test Plan workflow
│   └── workflow-task-mgmt.md    # Task management workflow
│
└── Helper Scripts (辅助脚本)
    ├── parse_tags.py            # Parse traceability tags from files
    ├── build_graph.py           # Build dependency graph
    ├── impact_analysis.py       # Analyze impact of changes
    └── init_project.py          # Initialize project structure
```

---

## **二、User Stories**

### **2.1 Epic 1: Project Initialization**

**[ID: PRD-EPIC-001] [Implements: RD-INIT-001]**

> **As** a Super Individual developer
> **I want** to quickly set up SpecGovernor toolkit structure
> **So that** I can start using standardized development workflows

---

#### **US-001.1: Initialize Project Structure**

**[ID: PRD-US-001.1]**

**User Flow:**
```
1. Developer downloads SpecGovernor toolkit repository
2. Runs: python scripts/init_project.py
3. Script prompts:
   请选择项目规模：
   1. 小项目（< 10 万行代码，单层文档结构）
   2. 大项目（≥ 10 万行代码，双层文档结构）
   您的选择：_

4. Script creates directory structure:

For Small Project:
  .specgov/
    ├── prompts/              # All prompt templates
    ├── workflows/            # All workflow docs
    ├── tasks/               # Task tracking files
    │   ├── project-manager.md
    │   ├── rd-analyst.md
    │   ├── product-manager.md
    │   ├── architect.md
    │   └── test-manager.md
    └── project-config.json   # Project configuration

  docs/
    ├── RD.md
    ├── PRD.md
    ├── Design-Document.md
    └── Test-Plan.md

For Large Project:
  .specgov/
    └── (same as small project)

  docs/
    ├── RD/
    │   ├── RD-Overview.md
    │   └── (module-specific RD files)
    ├── PRD/
    │   ├── PRD-Overview.md
    │   └── (module-specific PRD files)
    ├── Design-Document/
    │   ├── Design-Overview.md
    │   └── (module-specific design files)
    └── Test-Plan/
        ├── Test-Overview.md
        └── (module-specific test files)

5. Script outputs:
   ✓ SpecGovernor 项目结构创建完成

   📚 下一步：
     1. Review .specgov/workflows/workflow-overview.md
     2. As Project Manager, create your first Epic in .specgov/tasks/project-manager.md
     3. Switch to Requirements Analyst role, load .specgov/prompts/rd-generator.md in Claude Code
```

**Acceptance Criteria:**
- ✅ Creates `.specgov/` directory with all templates and workflows
- ✅ Creates appropriate document structure based on project size selection
- ✅ Generates `project-config.json` with project metadata
- ✅ Outputs clear next-step guidance

---

### **2.2 Epic 2: Using Prompt Templates with Claude Code**

**[ID: PRD-EPIC-002] [Implements: RD-GOAL-001, RD-GOAL-002]**

> **As** a Super Individual developer
> **I want** to use prompt templates with Claude Code to generate standardized documents
> **So that** I maintain consistency and traceability across all artifacts

---

#### **US-002.1: Generate Requirements Document (RD)**

**[ID: PRD-US-002.1]**

**User Flow:**
```
1. Developer switches to "Requirements Analyst" role perspective

2. Opens .specgov/tasks/rd-analyst.md to check assigned tasks

3. Opens Claude Code

4. Loads prompt template .specgov/prompts/rd-generator.md

5. Provides context:
   - Business requirements
   - User stories
   - Existing documents (if modifying)

6. Claude Code (using the prompt template):
   - Generates RD.md with proper structure
   - Embeds traceability tags: [ID: RD-REQ-XXX]
   - Uses [Decomposes: XXX] for hierarchical requirements
   - Follows markdown formatting standards

7. Output saved to docs/RD.md

8. Developer updates .specgov/tasks/rd-analyst.md:
   - Marks task as complete
   - Adds notes

9. Developer switches to "Project Manager" role

10. Updates .specgov/tasks/project-manager.md:
    - Updates Epic progress (e.g., 20% -> 40%)
    - Notes completion of RD generation subtask
```

**Example Generated RD Section:**
```markdown
## 1. User Authentication Requirements
**[ID: RD-AUTH-001]**

This section defines all authentication-related requirements.

### 1.1 OAuth2 Login
**[ID: RD-REQ-005] [Decomposes: RD-AUTH-001]**

The system must support user login via OAuth2 protocol, including:
- Google OAuth2
- GitHub OAuth2
- Microsoft OAuth2

...
```

**Acceptance Criteria:**
- ✅ Prompt template (rd-generator.md) guides Claude Code to generate proper RD structure
- ✅ Generated RD contains embedded traceability tags
- ✅ Template handles both creation and modification scenarios
- ✅ Follows naming conventions from RD.md
- ✅ User updates both task documents (role-specific and project manager)

---

#### **US-002.2: Review Requirements Document (RD)**

**[ID: PRD-US-002.2]**

**User Flow:**
```
1. Developer stays in "Requirements Analyst" role or switches to a different perspective for independent review

2. Opens Claude Code

3. Loads review prompt template .specgov/prompts/rd-reviewer.md

4. Provides the generated docs/RD.md for review

5. Claude Code (using the reviewer template):
   - Checks for completeness
   - Validates traceability tags (all requirements have [ID: XXX])
   - Checks [Decomposes: XXX] references are valid
   - Identifies missing requirements
   - Suggests improvements

6. Outputs structured review report (JSON or Markdown)

7. Developer addresses review feedback using rd-generator.md again (modification mode)
```

**Example Review Report:**
```markdown
# RD Review Report

## Summary
✓ Overall quality: Good
⚠️  Found 2 suggestions, 0 critical issues

## Issues

### 1. [Suggestion] RD-REQ-005 (OAuth2 Login)
- Location: Section 1.1
- Issue: Missing error handling requirements
- Recommendation: Add requirements for login failure, token expiration scenarios

### 2. [Suggestion] Traceability Tags
- Location: Section 2.3
- Issue: Missing [ID: XXX] tag
- Recommendation: Add tag for "Data Security Requirements"

## Traceability Check
✓ All major requirements have [ID: XXX] tags
✓ All [Decomposes: XXX] references point to existing parent IDs
```

**Acceptance Criteria:**
- ✅ Reviewer template (rd-reviewer.md) guides Claude Code to check completeness
- ✅ Validates traceability tag correctness
- ✅ Outputs structured feedback
- ✅ Distinguishes issue severity (critical/warning/suggestion)

---

#### **US-002.3: Generate Product Requirements Document (PRD)**

**[ID: PRD-US-002.3]**

**User Flow:**
```
1. Developer switches to "Product Manager" role

2. Opens .specgov/tasks/product-manager.md to check assigned tasks

3. Opens Claude Code

4. Loads prompt template .specgov/prompts/prd-generator.md

5. Provides context:
   - docs/RD.md (generated in previous step)
   - Product vision
   - User personas

6. Claude Code generates PRD.md with:
   - Product features: [ID: PRD-FEAT-XXX]
   - User stories: [ID: PRD-US-XXX]
   - Traceability to RD: [Implements: RD-REQ-XXX]

7. Output saved to docs/PRD.md

8. Updates both .specgov/tasks/product-manager.md and project-manager.md
```

**Example Generated PRD Section:**
```markdown
## 2. User Authentication Features

### 2.1 OAuth2 Login Feature
**[ID: PRD-FEAT-012] [Implements: RD-REQ-005]**

#### User Story
> **As** a user
> **I want** to log in using my Google/GitHub/Microsoft account
> **So that** I don't need to create a new password

#### Acceptance Criteria
- ✅ Support Google OAuth2 login
- ✅ Support GitHub OAuth2 login
- ✅ Support Microsoft OAuth2 login
- ✅ Handle login failures gracefully
- ✅ Handle token expiration
```

**Acceptance Criteria:**
- ✅ PRD generator template creates proper product features
- ✅ Embeds [Implements: RD-XXX] tags linking to requirements
- ✅ Follows product document best practices
- ✅ Template can both create and modify PRD

---

#### **US-002.4: Generate Design Document**

**[ID: PRD-US-002.4]**

**User Flow:**
```
1. Developer switches to "Architect" role

2. Loads .specgov/prompts/design-generator.md in Claude Code

3. Provides:
   - docs/RD.md
   - docs/PRD.md
   - Technical constraints

4. Claude Code generates Design-Document.md with:
   - Architecture design: [ID: DESIGN-ARCH-XXX]
   - API design: [ID: DESIGN-API-XXX]
   - Database design: [ID: DESIGN-DB-XXX]
   - Traceability: [Designs-for: PRD-FEAT-XXX]

5. Output saved to docs/Design-Document.md

6. Updates task documents
```

**Example Generated Design Section:**
```markdown
## 3. API Design

### 3.1 OAuth2 Callback API
**[ID: DESIGN-API-008] [Designs-for: PRD-FEAT-012]**

**Endpoint**: POST /auth/oauth2/callback

**Request:**
```json
{
  "provider": "google",
  "code": "auth_code_from_provider",
  "redirect_uri": "https://app.example.com/callback"
}
```

**Response:**
```json
{
  "access_token": "...",
  "refresh_token": "...",
  "expires_in": 3600
}
```
```

**Acceptance Criteria:**
- ✅ Design generator template creates technical specifications
- ✅ Embeds [Designs-for: PRD-XXX] tags
- ✅ Uses "Design Document" terminology (not "DD")
- ✅ Handles both creation and modification

---

#### **US-002.5: Generate Test Plan**

**[ID: PRD-US-002.5]**

**User Flow:**
```
1. Developer switches to "Test Manager" role

2. Loads .specgov/prompts/test-plan-generator.md in Claude Code

3. Provides:
   - docs/Design-Document.md
   - docs/PRD.md

4. Claude Code generates Test-Plan.md with:
   - Test cases: [ID: TEST-CASE-XXX]
   - Traceability: [Tests-for: DESIGN-API-XXX]
   - Test strategy, coverage goals

5. Output saved to docs/Test-Plan.md

6. Updates task documents
```

**Example Generated Test Plan Section:**
```markdown
## 5. API Test Cases

### 5.1 OAuth2 Callback API Tests
**[ID: TEST-CASE-015] [Tests-for: DESIGN-API-008]**

#### Test Case: Successful Google OAuth2 Login
**[ID: TEST-CASE-015-001]**

**Preconditions:**
- User has valid Google account
- Application registered with Google OAuth2

**Steps:**
1. Send POST /auth/oauth2/callback with valid Google auth code
2. Verify response status is 200
3. Verify access_token is present
4. Verify refresh_token is present

**Expected:**
- ✅ Status: 200 OK
- ✅ access_token: valid JWT
- ✅ expires_in: 3600 seconds
```

**Acceptance Criteria:**
- ✅ Test Plan generator template creates comprehensive test cases
- ✅ Embeds [Tests-for: DESIGN-XXX] tags
- ✅ Uses "Test Plan" terminology (not "TD")
- ✅ Handles both creation and modification

---

### **2.3 Epic 3: Using Helper Scripts**

**[ID: PRD-EPIC-003] [Implements: RD-GOAL-004]**

> **As** a Super Individual developer
> **I want** to use helper scripts to parse tags, build graphs, and analyze impacts
> **So that** I can maintain traceability without manual tracking

---

#### **US-003.1: Parse Traceability Tags**

**[ID: PRD-US-003.1]**

**User Flow:**
```
1. Developer runs:
   python scripts/parse_tags.py

2. Script scans all files in docs/ and src/ directories

3. Finds all traceability tags:
   - [ID: XXX]
   - [Implements: XXX]
   - [Decomposes: XXX]
   - [Designs-for: XXX]
   - [Tests-for: XXX]

4. Outputs parsed tags to:
   .specgov/index/tags.json

5. Example output:
{
  "tags": [
    {
      "id": "RD-REQ-005",
      "type": "requirement",
      "file": "docs/RD.md",
      "line": 42,
      "decomposes": "RD-AUTH-001"
    },
    {
      "id": "PRD-FEAT-012",
      "type": "feature",
      "file": "docs/PRD.md",
      "line": 128,
      "implements": "RD-REQ-005"
    },
    ...
  ]
}

6. Console output:
   ✓ Scanned 125 files
   ✓ Found 45 [ID: XXX] tags
   ✓ Found 38 [Implements: XXX] tags
   ✓ Found 12 [Decomposes: XXX] tags
   ✓ Saved to .specgov/index/tags.json

   ⏱️  Time: 8 seconds
   💰 Cost: $0 (local parsing)
```

**Acceptance Criteria:**
- ✅ Scans all Markdown and code files
- ✅ Uses regex to parse all tag types
- ✅ Outputs structured JSON
- ✅ Performance: < 1 minute for 100K+ lines of code
- ✅ Zero AI cost (local computation)

---

#### **US-003.2: Build Dependency Graph**

**[ID: PRD-US-003.2]**

**User Flow:**
```
1. Developer runs:
   python scripts/build_graph.py

2. Script reads .specgov/index/tags.json

3. Constructs dependency graph:
   - Nodes: All [ID: XXX] tags
   - Edges: [Implements: XXX], [Decomposes: XXX], etc.

4. Detects circular dependencies

5. Outputs graph to:
   .specgov/index/dependency-graph.json

6. Example output:
{
  "nodes": [
    {"id": "RD-REQ-005", "type": "requirement", "location": "docs/RD.md#L42"},
    {"id": "PRD-FEAT-012", "type": "feature", "location": "docs/PRD.md#L128"},
    {"id": "DESIGN-API-008", "type": "api_design", "location": "docs/Design-Document.md#L234"}
  ],
  "edges": [
    {"from": "PRD-FEAT-012", "to": "RD-REQ-005", "relation": "implements"},
    {"from": "DESIGN-API-008", "to": "PRD-FEAT-012", "relation": "designs-for"}
  ]
}

7. Console output:
   ✓ Created 45 nodes
   ✓ Created 50 edges
   ✓ Detected 0 circular dependencies
   ✓ Saved to .specgov/index/dependency-graph.json

   📊 Statistics:
     - Requirements (RD): 15
     - Features (PRD): 12
     - Designs (Design Document): 10
     - Tests (Test Plan): 5
     - Code: 3
```

**Acceptance Criteria:**
- ✅ Builds graph from parsed tags
- ✅ Detects circular dependencies
- ✅ Outputs JSON format
- ✅ Zero AI cost

---

#### **US-003.3: Analyze Impact of Changes**

**[ID: PRD-US-003.3]**

**User Flow:**
```
1. Developer modifies docs/RD.md

2. Runs:
   python scripts/impact_analysis.py --changed=docs/RD.md

3. Script:
   - Uses git diff to identify changed lines
   - Parses tags in changed sections
   - Queries dependency graph for downstream nodes

4. Outputs impact report:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Impact Analysis Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Changed Nodes (2):
  • RD-REQ-005 (requirement) at docs/RD.md#L42
  • RD-REQ-007 (requirement) at docs/RD.md#L85

Affected Documents (5):
  ⚠️  PRD-FEAT-012 (feature) at docs/PRD.md#L128
      Reason: Implements RD-REQ-005

  ⚠️  DESIGN-API-008 (api_design) at docs/Design-Document.md#L234
      Reason: Designs for PRD-FEAT-012

  ⚠️  TEST-CASE-015 (test) at docs/Test-Plan.md#L56
      Reason: Tests DESIGN-API-008

  ...

Affected Code (3):
  ⚠️  CODE-API-008 at src/auth/auth.controller.ts#L89
      Reason: Implements DESIGN-API-008

  ...

Recommended Actions:
  1. Review and update PRD section for PRD-FEAT-012
  2. Review and update Design Document for DESIGN-API-008
  3. Update test cases in Test Plan

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ Report saved to .specgov/reports/impact-2025-11-16.json

⏱️  Time: 6 seconds
💰 Cost: $0 (graph query only)
```

**Acceptance Criteria:**
- ✅ Uses git diff to detect changes
- ✅ Queries dependency graph efficiently
- ✅ Outputs clear impact report
- ✅ Performance: < 10 seconds
- ✅ Zero AI cost

---

### **2.4 Epic 4: Task Management Workflow**

**[ID: PRD-EPIC-004] [Implements: RD-USER-001]**

> **As** a Super Individual
> **I want** to manage high-level Epics and low-level Tasks
> **So that** I can track overall progress and specific work items

---

#### **US-004.1: Create Epic as Project Manager**

**[ID: PRD-US-004.1]**

**User Flow:**
```
1. Developer switches to "Project Manager" role

2. Opens .specgov/tasks/project-manager.md

3. Creates new Epic:

## Epic 1: OAuth2 Authentication Feature
**Status**: In Progress
**Progress**: 0% (0/5 subtasks)
**Owner**: Self (wearing different hats)

### Subtasks:
- [ ] 1.1 Requirements Analysis - Requirements Analyst (估计 1 天)
- [ ] 1.2 Product Design - Product Manager (估计 1 天)
- [ ] 1.3 Technical Design - Architect (估计 2 天)
- [ ] 1.4 Test Planning - Test Manager (估计 1 天)
- [ ] 1.5 Implementation - Developer (估计 3 天)

**总估计**: 8 天

4. Commits change to Git
```

**Acceptance Criteria:**
- ✅ Project Manager creates Epic with clear subtasks
- ✅ Assigns subtasks to different role perspectives
- ✅ Tracks progress percentage
- ✅ Simple Markdown format

---

#### **US-004.2: Execute Task as Role**

**[ID: PRD-US-004.2]**

**User Flow:**
```
1. Developer switches to "Requirements Analyst" role

2. Opens .specgov/tasks/rd-analyst.md

3. Sees task assigned from Epic 1:
## Task: Epic 1.1 - OAuth2 Authentication Requirements
**Assigned by**: Project Manager
**Deadline**: Day 1
**Status**: In Progress

### Work Log:
- [2025-11-16 09:00] Started task
- [2025-11-16 10:30] Loaded rd-generator.md prompt in Claude Code
- [2025-11-16 11:45] Generated initial RD.md section for OAuth2
- [2025-11-16 14:00] Reviewed with rd-reviewer.md
- [2025-11-16 15:30] Incorporated feedback, finalized RD section

**Status**: ✅ Completed

4. Saves .specgov/tasks/rd-analyst.md

5. Switches to "Project Manager" role

6. Updates .specgov/tasks/project-manager.md:
## Epic 1: OAuth2 Authentication Feature
**Status**: In Progress
**Progress**: 20% (1/5 subtasks)

### Subtasks:
- [✅] 1.1 Requirements Analysis - Completed 2025-11-16
- [ ] 1.2 Product Design - Product Manager (估计 1 天)
- ...

7. Commits both files to Git
```

**Acceptance Criteria:**
- ✅ Role-specific task file tracks detailed work
- ✅ Project Manager file tracks Epic progress
- ✅ Updating both files keeps views in sync
- ✅ Git history provides audit trail

---

## **三、Deliverables (Product Features)**

### **3.1 Prompt Templates**

**[ID: PRD-FEAT-TEMPLATES-001] [Implements: RD-GOAL-001]**

| Template File | Purpose | Input | Output |
|--------------|---------|-------|--------|
| **rd-generator.md** | Generate or modify Requirements Document | User stories, business requirements, (existing RD.md) | RD.md with [ID: RD-XXX] tags |
| **rd-reviewer.md** | Review Requirements Document | RD.md | Review report |
| **prd-generator.md** | Generate or modify Product Requirements Document | RD.md, product vision | PRD.md with [ID: PRD-XXX], [Implements: RD-XXX] |
| **prd-reviewer.md** | Review Product Requirements Document | PRD.md | Review report |
| **design-generator.md** | Generate or modify Design Document | PRD.md, technical constraints | Design-Document.md with [ID: DESIGN-XXX], [Designs-for: PRD-XXX] |
| **design-reviewer.md** | Review Design Document | Design-Document.md | Review report |
| **test-plan-generator.md** | Generate or modify Test Plan | Design-Document.md, PRD.md | Test-Plan.md with [ID: TEST-XXX], [Tests-for: DESIGN-XXX] |
| **test-plan-reviewer.md** | Review Test Plan | Test-Plan.md | Review report |
| **code-generator.md** | Generate or modify Code | Design-Document.md | Code files with [ID: CODE-XXX], [Implements: DESIGN-XXX] |

**Notes:**
- All generator templates handle both creation AND modification (no separate reviser templates)
- When existing document is provided to generator template, it modifies rather than creates
- All templates embed traceability tags automatically
- Templates use proper terminology: "Design Document" and "Test Plan" (not DD/TD)

---

### **3.2 Workflow Documentation**

**[ID: PRD-FEAT-WORKFLOWS-001] [Implements: RD-GOAL-002]**

| Workflow File | Content | Purpose |
|--------------|---------|---------|
| **workflow-overview.md** | Overall SDLC process overview | Guide developers through complete lifecycle |
| **workflow-rd.md** | Step-by-step RD generation process | How to use rd-generator.md and rd-reviewer.md |
| **workflow-prd.md** | Step-by-step PRD generation process | How to use prd-generator.md and prd-reviewer.md |
| **workflow-design.md** | Step-by-step Design Document process | How to use design-generator.md and design-reviewer.md |
| **workflow-test-plan.md** | Step-by-step Test Plan process | How to use test-plan-generator.md and test-plan-reviewer.md |
| **workflow-task-mgmt.md** | Task management process | How to manage Epics and Tasks across role perspectives |
| **workflow-large-project.md** | Large project workflow | How to use two-tier documentation for large projects |

---

### **3.3 Helper Scripts**

**[ID: PRD-FEAT-SCRIPTS-001] [Implements: RD-GOAL-004]**

| Script | Functionality | Performance Target | Cost Target |
|--------|--------------|-------------------|-------------|
| **init_project.py** | Initialize project structure, prompt for size selection, create directories | < 5 seconds | $0 |
| **parse_tags.py** | Scan files, parse traceability tags, output JSON | < 1 minute for 100K LOC | $0 |
| **build_graph.py** | Build dependency graph from tags, detect circular deps | < 1 minute for 100K LOC | $0 |
| **impact_analysis.py** | Analyze impact of file changes using git diff and graph | < 10 seconds | $0 |

**Technology:**
- Python 3.8+
- Standard library only (no external dependencies for core functionality)
- Git integration via subprocess
- JSON for data storage

---

## **四、Project Size Support**

### **4.1 Small Project Support**

**[ID: PRD-FEAT-SMALL-001] [Implements: RD-STRUCTURE-SMALL-001]**

**Characteristics:**
- Code: < 100K lines
- Modules: 1-3
- Document structure: Single-tier

**Deliverables:**
- Single RD.md for all requirements
- Single PRD.md for all features
- Single Design-Document.md for all designs
- Single Test-Plan.md for all tests

**Prompt Templates:**
- Standard templates work as-is
- Claude Code can handle entire document in one context

---

### **4.2 Large Project Support**

**[ID: PRD-FEAT-LARGE-001] [Implements: RD-STRUCTURE-LARGE-001]**

**Characteristics:**
- Code: ≥ 100K lines
- Modules: 4+
- Document structure: Two-tier (Overview + Modules)

**Deliverables:**
- RD-Overview.md + RD-{Module}.md for each module
- PRD-Overview.md + PRD-{Module}.md for each module
- Design-Overview.md + Design-{Module}.md for each module
- Test-Overview.md + Test-{Module}.md for each module

**Special Templates:**
- rd-overview-generator.md (generates high-level overview)
- rd-module-generator.md (generates module-specific details)
- Similar for PRD, Design Document, Test Plan

**Extended Tags:**
- **[Module: XXX]** - Indicates module affiliation
- Module-prefixed IDs: **RD-User-REQ-001**, **RD-Order-REQ-001**

**Example:**
```markdown
## User Login Requirements
**[ID: RD-User-REQ-001] [Module: User]**

...
```

---

## **五、Non-Functional Requirements**

### **5.1 Usability**

**[ID: PRD-NFR-001]**

- ✅ Zero installation: Just download templates and scripts
- ✅ Clear workflow documentation for each stage
- ✅ Prompt templates guide Claude Code with detailed instructions
- ✅ Helper scripts provide friendly console output

---

### **5.2 Performance**

**[ID: PRD-NFR-002]**

- ✅ Tag parsing: < 1 minute for 100K+ lines of code
- ✅ Graph building: < 1 minute for 100K+ lines of code
- ✅ Impact analysis: < 10 seconds
- ✅ Project initialization: < 5 seconds

---

### **5.3 Cost**

**[ID: PRD-NFR-003]**

- ✅ Helper scripts: $0 (local computation)
- ✅ Using prompt templates: Only pay for Claude Code API usage (user's existing cost)
- ✅ No software license fees
- ✅ No subscription costs

---

### **5.4 Maintainability**

**[ID: PRD-NFR-004]**

- ✅ All templates are plain Markdown files (easy to edit)
- ✅ All scripts are simple Python (easy to understand and modify)
- ✅ Git-trackable: All changes versioned
- ✅ Extensible: Users can create custom templates

---

## **六、Success Metrics**

### **6.1 Adoption Metrics**

**[ID: PRD-METRICS-001]**

- Number of projects initialized with SpecGovernor
- Number of documents generated using prompt templates
- GitHub stars/forks (if open-sourced)

---

### **6.2 Quality Metrics**

**[ID: PRD-METRICS-002]**

- Traceability tag coverage: % of requirements/features/designs with tags
- Circular dependency detection rate
- User-reported issues with templates

---

### **6.3 Efficiency Metrics**

**[ID: PRD-METRICS-003]**

- Time to generate RD/PRD/Design Document/Test Plan using templates
- Time saved vs. manual document creation
- Cost savings (vs. paid tools)

---

## **七、Risks and Limitations**

### **7.1 Risks**

**[ID: PRD-RISK-001]**

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Users forget to embed traceability tags | Dependency graph incomplete | Reviewer templates check for tag presence |
| Claude Code generates inconsistent tags | Graph parsing errors | Reviewer templates validate tag format |
| Helper scripts too slow for very large projects | Poor user experience | Optimize with incremental parsing, caching |

---

### **7.2 Limitations**

**[ID: PRD-LIMIT-001]**

| Limitation | Explanation |
|-----------|-------------|
| Depends on Claude Code | Users must have Claude Code access |
| Requires manual role-switching | Super Individual must consciously change perspectives |
| Python required for scripts | Users need Python 3.8+ installed |
| Git required for impact analysis | Project must be git-initialized |

---

## **八、Summary**

### **8.1 Core Value**

**[ID: PRD-SUMMARY-001]**

SpecGovernor provides value through:

1. ✅ **Ready-to-use Prompt Templates**: Immediately usable with Claude Code, no setup
2. ✅ **Explicit Traceability**: 100% reliable through embedded tags, no AI guesswork
3. ✅ **Dual Quality Assurance**: Generator-Reviewer pairs for each stage
4. ✅ **Zero Cost Infrastructure**: Just templates and scripts, no software licenses

---

### **8.2 Comparison with Alternatives**

**[ID: PRD-SUMMARY-002]**

| Dimension | SpecGovernor | Traditional Doc Management | AI Coding Assistants |
|-----------|-------------|--------------------------|---------------------|
| **Setup** | Download templates | Complex software install | Subscription required |
| **Traceability** | Explicit tags, 100% reliable | Manual maintenance | Implicit, unreliable |
| **Cost** | $0 (+ Claude API usage) | High license fees | $20+/month |
| **Learning Curve** | Read workflow docs | Steep | Medium |
| **Flexibility** | High (edit templates) | Low (vendor lock-in) | Medium |

---

### **8.3 Next Steps**

**[ID: PRD-NEXT-001]**

Based on this PRD, the next steps are:

1. ✅ **Write Design Document**: Detailed design for prompt templates and scripts
2. ✅ **Write Test Plan**: Test strategy for validating templates and scripts
3. ✅ **Implement Templates**: Create all prompt template .md files
4. ✅ **Implement Scripts**: Develop Python helper scripts
5. ✅ **Write Workflow Docs**: Document step-by-step processes

---

**PRD Document Complete**
