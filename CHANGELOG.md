# Changelog

All notable changes to this repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to documentation versioning principles.

## [2.0.0] - 2025-01-XX

### 🎉 Major Repository Reorganization

This release represents a comprehensive restructuring of the repository to improve organization, discoverability, and usability.

### Added

#### Documentation
- **README.md**: Complete rewrite with comprehensive structure overview
  - Added repository structure diagram
  - Included quick start guide
  - Added template categories explanation
  - Included usage examples
  - Added contribution guidelines
  - Linked to all supporting documentation

- **USAGE_GUIDE.md**: New comprehensive usage guide (18+ sections)
  - General purpose prompts guide
  - Project-specific prompts documentation
  - Utility prompts explanation
  - MCP configurations guide
  - Best practices section
  - Troubleshooting guide
  - Advanced topics (custom templates, maintenance, optimization)
  - Real-world examples for common scenarios

- **CHANGELOG.md**: This file - documenting all repository changes
  - Version history
  - Detailed change descriptions
  - Migration guides
  - Breaking changes documentation

- **archive/README.md**: Archive documentation with deprecation notices
  - Detailed deprecation information for each archived template
  - Migration paths from old to new templates
  - Historical context and rationale
  - Guidelines for using archived content

#### Directory Structure
- Maintained clear separation of concerns:
  - `prompts/` - General purpose templates
  - `specific/` - Project-specific configurations
  - `other/` - Utility templates
  - `mcp/` - MCP server configurations
  - `archive/` - Deprecated templates
  - `script/` - Automation utilities
  - `vscode/` - VS Code configurations

### Changed

#### Template Organization
- Clarified purpose of each directory through documentation
- Established clear naming conventions
- Documented all template types comprehensively

#### Documentation Quality
- Enhanced all documentation with proper markdown formatting
- Added table of contents to major documents
- Included cross-references between related documents
- Added practical examples throughout

#### README.md
- Transformed from command list to comprehensive project guide
- Added visual structure representation
- Included quick start instructions
- Added template category overviews
- Improved navigation with sections and links

### Deprecated

#### Templates Moved to Archive

**aictoold.md** → Replaced by `prompts/AI_CTO.md`
- **Reason**: New version provides:
  - More structured clarifying questions
  - Enhanced output format with 17+ comprehensive sections
  - Better integration with modern tech stacks
  - Detailed implementation guidance
  - Universal platform support
- **Migration**: Use `prompts/AI_CTO.md` for all new projects
- **Breaking Changes**: 
  - Output format restructured
  - Clarifying questions consolidated
  - Added comprehensive implementation plans

**aug.md** (archived copy) → Consolidated to `other/aug.md`
- **Reason**: Eliminate duplicate, single authoritative source
- **Migration**: Use `other/aug.md` (content identical)
- **Breaking Changes**: None - files identical

**augg.md** → Removed duplicate
- **Reason**: Unintentional duplicate of `aug.md`
- **Migration**: Use `other/aug.md`
- **Breaking Changes**: None

### Fixed

#### Documentation Issues
- Corrected inconsistent template references
- Fixed broken internal links
- Standardized markdown formatting
- Improved code block syntax highlighting

#### Repository Structure
- Clarified purpose of each directory
- Documented relationships between templates
- Established clear template hierarchy

### Documentation Structure

#### New Documentation Hierarchy
```
Repository Root
├── README.md (Main entry point)
├── USAGE_GUIDE.md (Comprehensive usage instructions)
├── CHANGELOG.md (Version history - this file)
├── AGENTS.md (AI agent configuration)
├── LICENSE (MIT License)
└── archive/
    └── README.md (Deprecation notices and migration guides)
```

### Migration Guide for v2.0.0

#### For Existing Users

**If you're using aictoold.md:**
1. Review `archive/README.md` for detailed migration instructions
2. Switch to `prompts/AI_CTO.md` for new projects
3. Note breaking changes in output format
4. Test with sample inputs to understand new structure

**If you're using aug.md from archive:**
1. Update references to point to `other/aug.md`
2. No code changes needed (content identical)

**If you're using augg.md:**
1. Update references to point to `other/aug.md`
2. No code changes needed (was duplicate)

#### For New Users

1. Start with [README.md](./README.md) for overview
2. Review [USAGE_GUIDE.md](./USAGE_GUIDE.md) for detailed instructions
3. Browse template directories based on your needs:
   - General tasks → `prompts/`
   - Specific projects → `specific/`
   - Guidelines → `other/`
   - MCP setup → `mcp/`
4. Check [archive/README.md](./archive/README.md) only if working with legacy projects

### Template Categories Established

#### General Purpose (`prompts/`)
- AI_CTO.md - Technical masterplan generation
- common.md - Shared prompt patterns
- gemini.md - Google Gemini API templates
- reactnative.md - React Native development
- sprint.md - Agile sprint planning
- permanent message.md - Persistent AI instructions
- And more...

#### Project-Specific (`specific/`)
- Browser extensions (aireply, yt summarizer, webpage chat)
- PDF tools (allpdftools, allpdf-python)
- QR code apps (qrcode, qrsayapp)
- VS Code extensions (vscode)
- Context management (Historical Context Tool, contextual sidebar)
- Development workflows (commit, download file mcp)
- And more...

#### Utilities (`other/`)
- aug.md - General augmentation guidelines
- grammarly.md - Writing improvement
- Quality assurance templates (qcw, qsl)
- And more...

#### MCP Configurations (`mcp/`)
- main.md - Comprehensive MCP server configurations
- kiro.txt - Kiro MCP settings

### Breaking Changes

#### Output Formats

**AI_CTO.md (formerly aictoold.md)**
- **Old Format**: Simple masterplan with basic sections
- **New Format**: 17-section comprehensive masterplan including:
  1. Document Information
  2. Executive Summary
  3. Project Overview
  4. Technical Stack and Architecture
  5. Project Scope
  6. Functional Requirements
  7. Non-Functional Requirements
  8. Integration Requirements
  9. Monitoring and Analytics
  10. Timeline and Success Criteria
  11. Implementation Plan (with granular tasks)
  12. API Endpoints and Data Models
  13. Project Structure and Organization
  14. Environment Variables and Configuration
  15. Testing Strategy and QA
  16. Deployment Strategy
  17. Maintenance and Risk Management
  18. Future Enhancements and Development Guidelines

**Impact**: Projects expecting old format will need to adjust parsing/processing logic

#### Question Flow

**AI_CTO.md**
- **Old**: Incremental follow-up questions
- **New**: Single consolidated set of clarifying questions with:
  - Multiple choice options (a, b, c, etc.)
  - Suggested defaults
  - "continue" option to use all defaults
  - No follow-up questions

**Impact**: Automation relying on old question flow needs updates

### Technical Details

#### Files Added
- `USAGE_GUIDE.md` (new, ~800 lines)
- `CHANGELOG.md` (this file)
- `archive/README.md` (comprehensive deprecation guide)

#### Files Modified
- `README.md` (complete rewrite, transformed from ~40 lines to ~250+ lines)
- All documentation structure improved

#### Files Moved
- `aictoold.md` → `archive/aictoold.md`
- `aug.md` → `archive/aug.md` (duplicate copy)
- `augg.md` → `archive/augg.md`

#### Files Unchanged (Location)
- All active templates remain in original locations
- `prompts/` directory structure maintained
- `specific/` directory structure maintained
- `other/` directory structure maintained
- `mcp/` directory structure maintained

### Statistics

- **Documentation Pages**: 4 major documentation files
- **Total Documentation Lines**: 1,500+ lines of comprehensive guides
- **Templates Documented**: 40+ templates across all categories
- **Archived Templates**: 3 (with detailed migration paths)
- **MCP Configurations**: 7 server configs documented
- **Examples Provided**: 10+ real-world usage examples

### Quality Improvements

#### Documentation Quality
- Added table of contents to all major docs
- Consistent markdown formatting throughout
- Code blocks with proper syntax highlighting
- Clear section hierarchy
- Comprehensive cross-referencing

#### Usability Enhancements
- Clear navigation from README to all docs
- Quick start guide for new users
- Detailed examples for common use cases
- Troubleshooting section
- Best practices documented

#### Maintainability
- Established clear deprecation process
- Version history tracking (this file)
- Migration guides for breaking changes
- Clear contribution guidelines

### Acknowledgments

This reorganization establishes a strong foundation for:
- New contributors to understand the repository
- Users to find and use appropriate templates
- Maintainers to track changes and deprecations
- Long-term evolution of the prompt collection

---

## [1.0.0] - 2024-XX-XX (Historical Baseline)

### Initial Repository State

This version represents the repository state before the comprehensive reorganization.

#### Structure
- Mixed organization of templates
- Basic README with command examples
- No formal documentation structure
- No usage guides
- No deprecation process
- No changelog

#### Contents
- Various prompt templates in multiple directories
- Python utilities (gce.py, gemini.py)
- JavaScript utilities (a.js, script/gi.js)
- MCP configurations
- VS Code settings

#### Notable Templates (Pre-reorganization)
- aictoold.md (later deprecated)
- AI_CTO.md (enhanced in v2.0.0)
- Various project-specific prompts
- Utility templates

### Issues Addressed in v2.0.0
- Lack of clear documentation
- No usage instructions
- Unclear template organization
- No deprecation tracking
- Difficult to find appropriate templates
- No examples or best practices

---

## Versioning Strategy

### Version Number Format

This documentation repository uses semantic versioning concepts adapted for documentation:

**[MAJOR].[MINOR].[PATCH]**

- **MAJOR**: Significant reorganization, breaking changes to template structure
- **MINOR**: New templates, new documentation sections, enhanced guides
- **PATCH**: Bug fixes, typo corrections, clarifications

### What Constitutes a Breaking Change?

- Template output format changes
- Required parameter modifications
- Deprecated templates with no backward compatibility
- Directory structure reorganization
- MCP configuration format changes

### Deprecation Policy

1. **Deprecation Notice**: Template moved to `archive/` with clear notice
2. **Migration Guide**: Detailed instructions in `archive/README.md`
3. **CHANGELOG Entry**: Documented in this file
4. **Transition Period**: Minimum 3 months before any removal consideration
5. **Support**: Questions answered, migration assistance provided

---

## Future Plans

### Planned for v2.1.0
- [ ] Additional project-specific templates
- [ ] Video tutorials for complex templates
- [ ] Interactive examples
- [ ] Template testing framework
- [ ] Community contribution templates

### Under Consideration
- [ ] Template versioning within files
- [ ] Automated template testing
- [ ] Template effectiveness metrics
- [ ] Community showcase section
- [ ] Integration with popular AI tools

### Long-term Vision
- Comprehensive prompt engineering library
- Industry-standard template collection
- Active community contributions
- Regular updates reflecting AI advancements
- Educational resources for prompt engineering

---

## Contributing to This Changelog

When making changes to the repository:

1. **Update This File**: Add entry to "Unreleased" section
2. **Categorize Changes**: Use Added/Changed/Deprecated/Removed/Fixed/Security
3. **Be Specific**: Include file names, clear descriptions, impact notes
4. **Link Issues**: Reference related issues/PRs if applicable
5. **Date Format**: Use ISO format (YYYY-MM-DD)

### Changelog Entry Template

```markdown
## [Unreleased]

### Added
- Feature description with file references

### Changed
- Modification description with rationale

### Deprecated
- Deprecated item with migration path

### Removed
- Removed item with justification

### Fixed
- Bug fix description with impact

### Security
- Security update description
```

---

## Questions or Feedback?

- **Issues**: Open an issue for questions about changes
- **Discussions**: Use GitHub Discussions for general feedback
- **PRs**: Submit pull requests for changelog improvements

**Maintained by**: Chirag Singhal (@chirag127)  
**Last Updated**: 2025-01-XX
