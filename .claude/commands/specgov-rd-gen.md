---
description: Generate Requirements Document (RD)
---

## Project Context

- **Project Size**: small project
- **Document Structure**: Single-tier (one file per document type)
- **Configuration**: `.specgov/project-config.json`

## Document Paths

- **Target Document**: `docs/RD.md`
- **Review Reports**: Check `reviews/` directory for previous review reports
  - Pattern: `reviews/{DocumentType}-Review-Report-*.md`

**Instructions**:
1. If creating new document: Write to `docs/RD.md`
2. If updating existing document: Read from `docs/RD.md`, then update it
3. Check `reviews/` directory for latest review report (if any)
4. Do NOT search for documents - use the paths above directly

---

## Prompt Template

Please load and use the SpecGovernor prompt template: `.specgov/prompts/rd-generator.md`

Follow the instructions in the template to generate or review the document.
