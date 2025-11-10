# Archive

> Deprecated and historical prompt templates

## Overview

This directory contains prompt templates and configurations that are no longer actively maintained or have been superseded by newer versions. These files are preserved for historical reference and to maintain backward compatibility for existing projects.

## ⚠️ Deprecation Notice

**All templates in this directory are considered deprecated.** Please use the current templates from the main directories (`prompts/`, `specific/`, `other/`) for new projects.

## Archive Contents

### aictoold.md

**Status**: DEPRECATED  
**Deprecated Date**: 2025-01-XX  
**Reason**: Replaced by `prompts/AI_CTO.md`

**Original Purpose**: Early version of the AI CTO masterplan generation prompt.

**Migration Path**:
- Use `prompts/AI_CTO.md` instead
- The new version includes:
  - More structured clarifying questions
  - Enhanced output format
  - Better integration with modern tech stacks
  - Comprehensive implementation guidance
  - Improved architecture recommendations

**Key Differences**:
- **Old (aictoold.md)**: Basic masterplan structure, limited tech stack coverage
- **New (AI_CTO.md)**: Universal masterplan generator with comprehensive structure, modern tech recommendations, and detailed implementation plans

**Breaking Changes**:
- Output format has been standardized
- Clarifying questions are now consolidated
- Added support for multiple platform types

---

### aug.md

**Status**: DEPRECATED  
**Deprecated Date**: 2025-01-XX  
**Reason**: Consolidated into `other/aug.md` with enhancements

**Original Purpose**: General augmentation guidelines for AI development assistance.

**Migration Path**:
- Use `other/aug.md` instead
- The current version is identical to this archive version
- This archive copy exists for reference only

**Key Features** (preserved in current version):
- Complete A-to-Z implementation guidelines
- No placeholder or TODO requirements
- Industry-standard best practices enforcement
- GitHub configuration (username: chirag127)
- Web search enablement
- Comprehensive documentation requirements

**Note**: This template was moved to `other/` directory without changes. The archived version is kept as a historical reference point.

---

### augg.md

**Status**: DEPRECATED  
**Deprecated Date**: 2025-01-XX  
**Reason**: Duplicate of `aug.md`, consolidated into single guideline

**Original Purpose**: Duplicate copy of general augmentation guidelines.

**Migration Path**:
- Use `other/aug.md` instead
- This was an unintentional duplicate

**History**:
- Created as duplicate during template reorganization
- Content identical to `aug.md`
- Deprecated to eliminate redundancy

---

## Using Archived Templates

### When to Use Archived Templates

You might need to reference archived templates if:

1. **Maintaining Legacy Projects**: Your existing project uses an older template version
2. **Historical Context**: Understanding evolution of prompt engineering approaches
3. **Debugging**: Comparing old vs new behavior
4. **Research**: Studying prompt template design patterns

### How to Use Archived Templates

⚠️ **Not Recommended for New Projects**

If you must use an archived template:

1. **Understand the Risks**:
   - May not work with current AI models
   - Lacks modern best practices
   - No active maintenance or support
   - May contain outdated technology references

2. **Copy, Don't Reference**:
   ```bash
   # Don't do this in new projects
   # Instead, use current templates from prompts/, specific/, or other/
   
   # If you must use archived template:
   cp archive/aictoold.md my-project/legacy-template.md
   # Then customize as needed
   ```

3. **Document Your Usage**:
   ```markdown
   # In your project README
   
   ## Note on Template Usage
   This project uses an archived template (aictoold.md) from [date].
   Reason: [explain why]
   Migration plan: [outline upgrade path]
   ```

## Migration Guide

### From aictoold.md to AI_CTO.md

**Step 1: Review Current Implementation**

If your project uses `aictoold.md`:
```markdown
# Check your current prompt structure
- Identify which sections you're using
- Note any customizations you've made
- Document expected outputs
```

**Step 2: Map to New Structure**

| Old Section (aictoold.md) | New Section (AI_CTO.md) | Notes |
|---------------------------|-------------------------|-------|
| Basic idea input | RAW_IDEA | Same concept, enhanced format |
| Tech preferences | USER_PREFERENCES + Clarifying Questions | More structured approach |
| Output masterplan | Complete masterplan.md | Enhanced with more sections |
| - | STEP 1: Clarify | New consolidated questioning |
| - | Implementation Plan | New detailed task breakdown |

**Step 3: Update Your Workflow**

```markdown
# Old workflow (aictoold.md)
1. Provide basic idea
2. Get simple masterplan
3. Fill in details manually

# New workflow (AI_CTO.md)
1. Provide RAW_IDEA
2. Answer consolidated clarifying questions OR type "continue"
3. Receive comprehensive masterplan with:
   - Detailed architecture
   - Implementation tasks
   - API specifications
   - Testing strategies
   - Deployment plans
```

**Step 4: Test with Sample Input**

```markdown
# Test input
RAW_IDEA: "Browser extension for bookmark organization using AI"

# Compare outputs
- Old template output: Basic feature list and tech stack
- New template output: Complete 17-section masterplan with actionable tasks
```

### From aug.md (archived) to aug.md (current)

**Good News**: No migration needed! The templates are identical.

The archived version exists only as a historical reference point. Continue using `other/aug.md` without changes.

## Deprecation Timeline

| Template | Deprecated | Replacement | Breaking Changes |
|----------|-----------|-------------|------------------|
| aictoold.md | 2025-01-XX | prompts/AI_CTO.md | Yes - Output format, question structure |
| aug.md | 2025-01-XX | other/aug.md | No - Identical content |
| augg.md | 2025-01-XX | other/aug.md | No - Was duplicate |

## Future Deprecations

Templates are deprecated when:

1. **Better Alternative Exists**: A new template provides significantly improved functionality
2. **Technology Obsolescence**: Referenced technologies are no longer current
3. **Consolidation**: Multiple templates are merged into a more comprehensive version
4. **Quality Issues**: Template doesn't meet current quality standards
5. **Redundancy**: Duplicate or near-duplicate templates exist

### Deprecation Process

When a template is deprecated:

1. **Move to Archive**: File moved to `archive/` directory
2. **Update Documentation**: Add entry to this README with:
   - Deprecation date
   - Reason for deprecation
   - Migration path
   - Key differences from replacement
3. **Update CHANGELOG**: Document in root `CHANGELOG.md`
4. **Add Notice**: Place deprecation notice at top of archived file
5. **Update References**: Update any documentation referencing the old template

### Checking for Deprecations

Before using any template:

1. **Check Location**: Templates in `archive/` are deprecated
2. **Read CHANGELOG.md**: Lists all deprecations with dates
3. **Review Template Header**: Active templates note if they replace older versions

## Contributing to Archive Documentation

If you have historical knowledge about archived templates:

1. **Add Context**: Help document why changes were made
2. **Improve Migration Guides**: Share your migration experience
3. **Document Gotchas**: Note any issues you encountered during migration
4. **Suggest Improvements**: Recommend better deprecation practices

Submit contributions via Pull Request with clear documentation of changes.

## Questions About Archived Templates

### "Can I still use an archived template?"

Technically yes, but it's not recommended. Archived templates:
- May not work with current AI models
- Lack modern best practices
- Have no support or maintenance
- May reference obsolete technologies

### "Why aren't archived templates deleted?"

We preserve them for:
- Historical reference
- Legacy project support
- Understanding template evolution
- Research and learning

### "How do I request a template be un-deprecated?"

If you believe a template was deprecated in error:

1. Open an issue explaining:
   - Why the template is still valuable
   - What use cases it serves
   - Why current alternatives don't meet the need
2. Provide evidence of continued usage
3. Propose maintenance plan

### "When will archived templates be removed?"

No deletion timeline currently planned. Templates remain archived indefinitely unless:
- Explicitly harmful or misleading
- Contain sensitive information
- Violate current policies
- Community consensus for removal

---

## See Also

- [CHANGELOG.md](../CHANGELOG.md) - Version history and deprecation log
- [USAGE_GUIDE.md](../USAGE_GUIDE.md) - Current template usage instructions
- [README.md](../README.md) - Repository overview and structure

**Last Updated**: 2025-01-XX  
**Maintained By**: Repository contributors
