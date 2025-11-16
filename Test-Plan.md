# **🧪 Test Plan - SpecGovernor**

> **Version**: v2.0
> **Based on**: Design-Document.md (v2.0) + PRD.md (v2.0)
> **Created**: 2025-11-16
> **Updated**: 2025-11-16
> **Test Goal**: Comprehensive testing strategy for toolkit components

---

## **Traceability Declaration**

This Test Plan covers the following Design Document components:
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

SpecGovernor is a **toolkit** (not software), so testing focuses on three aspects:

1. **Prompt Template Validation**: Verify templates guide Claude Code to generate proper documents
2. **Workflow Documentation Review**: Verify workflows are clear and complete
3. **Helper Script Testing**: Unit tests and integration tests for Python scripts

**Test Levels:**

| Level | Focus | Coverage |
|-------|-------|----------|
| **Manual Testing** | Prompt templates, workflows | Human evaluation of generated documents |
| **Unit Testing** | Python scripts | pytest for each function |
| **Integration Testing** | End-to-end workflows | Complete SDLC cycle |
| **Acceptance Testing** | Real-world usage | Dog-fooding with SpecGovernor itself |

---

### **1.2 Testing Tools**

**[ID: TEST-STRATEGY-002]**

| Tool | Purpose | Usage |
|------|---------|-------|
| **Claude Code** | Execute prompt templates | Manual testing of templates |
| **pytest** | Python unit/integration tests | Automated testing of scripts |
| **pytest-cov** | Code coverage measurement | Ensure > 80% coverage |
| **Git** | Version control, diff testing | Test impact analysis script |
| **Manual Review** | Workflow documentation | Read-through and execution testing |

---

## **二、Prompt Template Testing**

### **2.1 RD Generator Template Tests**

**[ID: TEST-CASE-001] [Tests-for: DESIGN-TEMPLATE-RD-GEN-001]**

#### **Test Case: Generate RD from User Stories**

**[ID: TEST-CASE-001-001]**

**Preconditions:**
- Claude Code installed and accessible
- rd-generator.md template available

**Test Steps:**
1. Open Claude Code
2. Load `.specgov/prompts/rd-generator.md`
3. Provide sample user stories:
   ```
   - As a user, I want to log in with OAuth2 so I don't need a password
   - As a user, I want to reset my password if I forget it
   ```
4. Execute prompt

**Expected Result:**
- ✅ Generated RD.md contains:
  - Proper header (Version, Created date)
  - Section for authentication requirements
  - OAuth2 requirement with **[ID: RD-REQ-XXX]** tag
  - Password reset requirement with **[ID: RD-REQ-YYY]** tag
  - Acceptance criteria for each requirement
  - Hierarchical structure using **[Decomposes: XXX]** if applicable

**Validation:**
- [ ] All requirements have [ID: RD-XXX] tags
- [ ] No placeholders or TODOs
- [ ] Acceptance criteria are testable
- [ ] Uses proper formatting

---

#### **Test Case: Modify Existing RD**

**[ID: TEST-CASE-001-002]**

**Preconditions:**
- Existing RD.md generated in previous test
- rd-generator.md template available

**Test Steps:**
1. Open Claude Code
2. Load `.specgov/prompts/rd-generator.md`
3. Provide:
   - Existing RD.md content
   - Change request: "Add requirement for 2FA (two-factor authentication)"
4. Execute prompt

**Expected Result:**
- ✅ Modified RD.md contains:
  - Original requirements preserved (with original IDs)
  - New 2FA requirement added with new **[ID: RD-REQ-ZZZ]** tag
  - Proper integration into existing structure

**Validation:**
- [ ] Original requirement IDs unchanged
- [ ] New requirement has unique ID
- [ ] No broken references
- [ ] Formatting consistent

---

### **2.2 RD Reviewer Template Tests**

**[ID: TEST-CASE-002] [Tests-for: DESIGN-TEMPLATE-RD-GEN-001]**

#### **Test Case: Review Complete RD**

**[ID: TEST-CASE-002-001]**

**Preconditions:**
- RD.md generated (with proper tags)
- rd-reviewer.md template available

**Test Steps:**
1. Open Claude Code
2. Load `.specgov/prompts/rd-reviewer.md`
3. Provide RD.md for review
4. Execute prompt

**Expected Result:**
- ✅ Review report contains:
  - Summary (quality rating, issue count)
  - Traceability check (all requirements have IDs, no broken references)
  - Completeness check (all sections present)
  - Quality assessment (testability, clarity)
  - Specific recommendations for improvements

**Validation:**
- [ ] Report format matches template
- [ ] All traceability tags validated
- [ ] Issues categorized by severity
- [ ] Recommendations actionable

---

#### **Test Case: Review RD with Missing Tags**

**[ID: TEST-CASE-002-002]**

**Preconditions:**
- RD.md with intentionally missing [ID: XXX] tags
- rd-reviewer.md template available

**Test Steps:**
1. Create test RD.md with 3 requirements, but only 2 have [ID: XXX] tags
2. Load rd-reviewer.md in Claude Code
3. Provide test RD.md
4. Execute prompt

**Expected Result:**
- ✅ Review report identifies missing tag:
  - Issue severity: Critical or Warning
  - Location: Section X.X (specific location of missing tag)
  - Recommendation: "Add [ID: RD-XXX] tag to requirement"

**Validation:**
- [ ] Missing tag detected
- [ ] Specific location provided
- [ ] Clear recommendation given

---

### **2.3 PRD, Design Document, Test Plan Template Tests**

**[ID: TEST-CASE-003] [Tests-for: DESIGN-TEMPLATE-PRD-GEN-001, DESIGN-TEMPLATE-DESIGN-GEN-001, DESIGN-TEMPLATE-TEST-GEN-001]**

Similar test cases as RD templates above, focusing on:

#### **PRD Generator Tests:**
- [ ] Generates features with **[ID: PRD-FEAT-XXX]**
- [ ] Links to RD with **[Implements: RD-REQ-XXX]**
- [ ] Creates user stories with proper format
- [ ] Uses proper "PRD" terminology (not product requirements)

#### **Design Document Generator Tests:**
- [ ] Generates architecture with **[ID: DESIGN-ARCH-XXX]**
- [ ] Generates APIs with **[ID: DESIGN-API-XXX]**
- [ ] Links to PRD with **[Designs-for: PRD-FEAT-XXX]**
- [ ] **ALWAYS uses "Design Document" (NOT "DD")**

#### **Test Plan Generator Tests:**
- [ ] Generates test cases with **[ID: TEST-CASE-XXX]**
- [ ] Links to Design Document with **[Tests-for: DESIGN-API-XXX]**
- [ ] Includes preconditions, steps, expected results
- [ ] **ALWAYS uses "Test Plan" (NOT "TD")**

---

## **三、Workflow Documentation Testing**

### **3.1 Workflow Documentation Review**

**[ID: TEST-CASE-004] [Tests-for: DESIGN-WORKFLOW-OVERVIEW-001, DESIGN-WORKFLOW-STAGES-001]**

#### **Test Case: Execute Complete RD Workflow**

**[ID: TEST-CASE-004-001]**

**Preconditions:**
- Fresh SpecGovernor project initialized
- workflow-rd.md available

**Test Steps:**
1. Read workflow-rd.md step-by-step
2. Follow each step precisely:
   - Switch to Requirements Analyst role
   - Open task file
   - Load rd-generator.md in Claude Code
   - Provide sample input
   - Generate RD.md
   - Review with rd-reviewer.md
   - Update task documents
3. Record any unclear steps or missing information

**Expected Result:**
- ✅ Workflow is clear and complete
- ✅ All steps can be executed without confusion
- ✅ RD.md generated successfully
- ✅ Task documents updated correctly

**Validation:**
- [ ] No ambiguous steps
- [ ] No missing prerequisites
- [ ] Examples are helpful and accurate
- [ ] Common pitfalls section is accurate

---

#### **Test Case: Execute Complete SDLC Workflow**

**[ID: TEST-CASE-004-002]**

**Preconditions:**
- Fresh project initialized
- workflow-overview.md available

**Test Steps:**
1. Execute complete workflow: RD → PRD → Design Document → Test Plan → Code
2. Follow each stage workflow document
3. Verify traceability chain:
   - PRD links to RD with [Implements: RD-XXX]
   - Design Document links to PRD with [Designs-for: PRD-XXX]
   - Test Plan links to Design Document with [Tests-for: DESIGN-XXX]

**Expected Result:**
- ✅ Complete traceability chain established
- ✅ All documents generated successfully
- ✅ All documents use proper terminology (Design Document, Test Plan)
- ✅ Task tracking works across all roles

**Validation:**
- [ ] RD → PRD → Design Document → Test Plan chain intact
- [ ] No broken traceability references
- [ ] Terminology consistent throughout
- [ ] Task documents updated at each stage

---

## **四、Helper Script Testing**

### **4.1 Project Initialization Script Tests**

**[ID: TEST-CASE-005] [Tests-for: DESIGN-SCRIPT-INIT-001]**

#### **Test Case: Initialize Small Project**

**[ID: TEST-CASE-005-001]**

**Preconditions:**
- Python 3.8+ installed
- SpecGovernor repository cloned
- Empty target directory

**Test Steps:**
1. Navigate to empty directory
2. Run: `python path/to/specgov/scripts/init_project.py`
3. Select option 1 (small project)
4. Verify created structure

**Expected Result:**
- ✅ `.specgov/` directory created with:
  - `prompts/` (all template files copied)
  - `workflows/` (all workflow files copied)
  - `tasks/` (5 task files: project-manager.md, rd-analyst.md, etc.)
  - `index/` (empty, for generated files)
  - `project-config.json` (with correct metadata)
- ✅ `docs/` directory created with:
  - `RD.md` (placeholder)
  - `PRD.md` (placeholder)
  - `Design-Document.md` (placeholder)
  - `Test-Plan.md` (placeholder)

**Validation:**
- [ ] All directories exist
- [ ] All template files copied correctly
- [ ] project-config.json has `"project_size": "small"` and `"document_structure": "single-tier"`
- [ ] Script completes in < 5 seconds

**Test Code (pytest):**

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

**Preconditions:**
- Same as Test Case 005-001

**Test Steps:**
1. Navigate to empty directory
2. Run: `python path/to/specgov/scripts/init_project.py`
3. Select option 2 (large project)
4. Verify created structure

**Expected Result:**
- ✅ `.specgov/` directory (same as small project)
- ✅ `docs/` directory with two-tier structure:
  - `RD/` directory with `RD-Overview.md`
  - `PRD/` directory with `PRD-Overview.md`
  - `Design-Document/` directory with `Design-Overview.md`
  - `Test-Plan/` directory with `Test-Overview.md`

**Validation:**
- [ ] Two-tier directory structure created
- [ ] project-config.json has `"project_size": "large"` and `"document_structure": "two-tier"`
- [ ] Script completes in < 5 seconds

**Test Code (pytest):**

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

**Test Data:**
```markdown
# Requirements Document

## 1. Authentication
**[ID: RD-AUTH-001]**

### 1.1 OAuth2 Login
**[ID: RD-REQ-005] [Decomposes: RD-AUTH-001]**

System must support OAuth2 login.
```

**Test Steps:**
1. Create test RD.md with above content
2. Run: `python scripts/parse_tags.py`
3. Verify output

**Expected Result:**
- ✅ `.specgov/index/tags.json` created with:
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

**Validation:**
- [ ] All tags found
- [ ] Line numbers correct
- [ ] Relationships captured (decomposes)
- [ ] Type inferred correctly
- [ ] Script completes in < 1 second

**Test Code (pytest):**

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

**Test Data:**
- RD.md with `[ID: RD-REQ-001]`
- PRD.md with `[ID: PRD-FEAT-001] [Implements: RD-REQ-001]`
- Design-Document.md with `[ID: DESIGN-API-001] [Designs-for: PRD-FEAT-001]`
- Test-Plan.md with `[ID: TEST-CASE-001] [Tests-for: DESIGN-API-001]`

**Expected Result:**
- ✅ All tags from all files found
- ✅ Relationships correctly captured:
  - PRD implements RD
  - Design designs-for PRD
  - Test tests-for Design
- ✅ Types correctly inferred for each

**Validation:**
- [ ] Cross-document relationships captured
- [ ] All tag types recognized
- [ ] Performance < 1 minute for 100K LOC

---

### **4.3 Dependency Graph Builder Tests**

**[ID: TEST-CASE-007] [Tests-for: DESIGN-SCRIPT-GRAPH-001]**

#### **Test Case: Build Graph from Tags**

**[ID: TEST-CASE-007-001]**

**Preconditions:**
- tags.json exists (from parse_tags.py)

**Test Steps:**
1. Run: `python scripts/build_graph.py`
2. Verify output

**Expected Result:**
- ✅ `.specgov/index/dependency-graph.json` created with:
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

**Validation:**
- [ ] All nodes created
- [ ] All edges created
- [ ] Relationships correctly represented
- [ ] Script completes in < 1 minute

**Test Code (pytest):**

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

**Test Data:**
- A implements B
- B designs-for C
- C implements A (circular!)

**Expected Result:**
- ✅ Circular dependency detected
- ✅ Console output shows: `⚠️  Detected 1 circular dependencies: A → B → C → A`

**Validation:**
- [ ] Circular dependency identified
- [ ] Path clearly shown
- [ ] Script doesn't crash

---

### **4.4 Impact Analysis Script Tests**

**[ID: TEST-CASE-008] [Tests-for: DESIGN-SCRIPT-IMPACT-001]**

#### **Test Case: Analyze Impact of RD Change**

**[ID: TEST-CASE-008-001]**

**Preconditions:**
- Dependency graph exists
- RD.md committed to Git
- Git working directory

**Test Steps:**
1. Modify RD.md (change requirement [ID: RD-REQ-005])
2. Git add and commit change
3. Run: `python scripts/impact_analysis.py --changed=docs/RD.md`
4. Verify output

**Expected Result:**
- ✅ Console output shows:
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

**Validation:**
- [ ] Changed node identified correctly
- [ ] All downstream nodes found
- [ ] Relationships explained clearly
- [ ] Performance < 10 seconds
- [ ] Cost = $0 (no AI calls)

**Test Code (pytest):**

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

**Objective**: Use SpecGovernor toolkit to manage the SpecGovernor project itself (dog-fooding).

**Test Steps:**
1. Initialize SpecGovernor structure within SpecGovernor repo
2. Use rd-generator.md to refine RD.md
3. Use prd-generator.md to refine PRD.md
4. Use design-generator.md to refine Design-Document.md
5. Use test-plan-generator.md to refine Test-Plan.md
6. Run parse_tags.py to extract all traceability tags from SpecGovernor docs
7. Run build_graph.py to build dependency graph
8. Make a change to RD.md
9. Run impact_analysis.py to see affected documents

**Expected Result:**
- ✅ All prompts work as intended
- ✅ All workflows are clear and easy to follow
- ✅ All scripts run successfully
- ✅ Traceability chain is intact across all SpecGovernor documents
- ✅ Impact analysis correctly identifies affected docs

**Validation:**
- [ ] No issues found during dog-fooding
- [ ] Discovered issues are documented and fixed
- [ ] SpecGovernor documentation meets its own quality standards

---

## **六、Performance Testing**

### **6.1 Performance Benchmarks**

**[ID: TEST-CASE-010] [Tests-for: DESIGN-NFR-PERF-001]**

| Operation | Target | Test Method | Acceptance Criteria |
|-----------|--------|------------|-------------------|
| Tag parsing | < 1 min for 100K LOC | Create 100K line test project, run parse_tags.py | ✅ Completes in < 60 seconds |
| Graph building | < 1 min for 100K LOC | Use tags from 100K LOC project, run build_graph.py | ✅ Completes in < 60 seconds |
| Impact analysis | < 10 seconds | Run impact_analysis.py on large graph | ✅ Completes in < 10 seconds |
| Project initialization | < 5 seconds | Run init_project.py | ✅ Completes in < 5 seconds |

**Test Code (pytest with benchmarks):**

```python
@pytest.mark.benchmark
def test_parse_tags_performance(benchmark, large_test_project):
    """Test parsing 100K LOC project."""
    result = benchmark(parse_tags.main)
    assert result is not None
    # pytest-benchmark will verify time automatically

@pytest.mark.benchmark
def test_graph_build_performance(benchmark, parsed_tags):
    """Test building graph from 100K LOC tags."""
    result = benchmark(build_graph.main)
    assert result is not None
```

---

## **七、Test Coverage Goals**

### **7.1 Coverage Targets**

**[ID: TEST-STRATEGY-003]**

| Component | Line Coverage Target | Branch Coverage Target |
|-----------|---------------------|----------------------|
| **init_project.py** | ≥ 90% | ≥ 85% |
| **parse_tags.py** | ≥ 95% | ≥ 90% |
| **build_graph.py** | ≥ 95% | ≥ 90% |
| **impact_analysis.py** | ≥ 90% | ≥ 85% |
| **Overall Scripts** | ≥ 90% | ≥ 85% |

**Measurement:**
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

**Test Projects:**

1. **Minimal Project**: 1 requirement, 1 feature, 1 design, 1 test
   - Purpose: Basic functionality testing
   - Location: `tests/fixtures/minimal-project/`

2. **Small Project**: 10 requirements, 8 features, 6 designs, 15 tests
   - Purpose: Realistic small project testing
   - Location: `tests/fixtures/small-project/`

3. **Large Project**: 100K LOC, 50 requirements, 40 features, multiple modules
   - Purpose: Performance and scalability testing
   - Location: `tests/fixtures/large-project/`

---

## **十、Risk-Based Testing**

### **10.1 High-Risk Areas**

**[ID: TEST-STRATEGY-006]**

| Risk | Impact | Test Priority | Mitigation |
|------|--------|--------------|-----------|
| Prompt templates generate inconsistent tags | High | P0 | Extensive manual testing, reviewer templates validate tags |
| Tag parser misses tags or gets wrong line numbers | High | P0 | Comprehensive unit tests, edge case testing |
| Circular dependency detection fails | Medium | P1 | Unit tests with known circular cases |
| Impact analysis finds too many false positives | Medium | P1 | Integration tests with real-world scenarios |
| Workflows are unclear or incomplete | High | P0 | Dog-fooding, user testing |

---

## **十一、Summary**

### **11.1 Test Deliverables**

**[ID: TEST-SUMMARY-001]**

1. **Manual Test Suite**: Test cases for all prompt templates and workflows
2. **Automated Test Suite**: pytest tests for all Python scripts
3. **Performance Benchmarks**: Benchmark suite for performance-critical operations
4. **CI/CD Pipeline**: GitHub Actions workflow for automated testing
5. **Test Coverage Report**: HTML report showing > 90% coverage

---

### **11.2 Exit Criteria**

**[ID: TEST-SUMMARY-002]**

Testing is complete when:
- ✅ All prompt templates generate proper documents (verified manually)
- ✅ All workflows are clear and executable (verified by dog-fooding)
- ✅ All Python scripts pass unit tests with > 90% coverage
- ✅ Performance benchmarks meet targets (< 1 min for 100K LOC)
- ✅ Dog-fooding successful (SpecGovernor manages itself)
- ✅ Zero critical bugs in helper scripts
- ✅ All test cases documented and executed

---

**Test Plan Document Complete**
