# Repository Index and Navigation Guide

> Complete reference guide for all files and their purposes in the AI Prompts Repository

## 📑 Table of Contents

- [Quick Reference](#quick-reference)
- [Templates](#templates)
- [Prompts](#prompts)
- [Projects](#projects)
- [Scripts](#scripts)
- [Documentation](#documentation)
- [Configuration](#configuration)
- [File Naming Conventions](#file-naming-conventions)

---

## Quick Reference

### Most Used Files

| File | Purpose | When to Use |
|------|---------|-------------|
| [prompts/AI_CTO.md](prompts/AI_CTO.md) | Generate technical masterplans | Starting any new project |
| [USAGE_GUIDE.md](USAGE_GUIDE.md) | Learn how to use templates | First-time repository users |
| [agent-guidelines.md](agent-guidelines.md) | AI agent configuration | Setting up AI coding assistants |
| [mcp/servers-config.json](mcp/servers-config.json) | MCP server setup | Configuring AI tool integrations |

---

## Templates

### Browser Extension Template

**File**: `templates/browser-extension-template.md`

**Purpose**: Generate comprehensive masterplans for browser extensions

**Use Case**: Building Chrome, Firefox, or Edge extensions

**Key Features**:

- Content script architecture
- Background/service worker configuration
- Popup and sidebar interfaces
- Browser API integration
- Manifest generation

---

### Web Application Template

**File**: `templates/web-app-template.md`

**Purpose**: Generate comprehensive masterplans for web applications

**Use Case**: Building full-stack web apps, SPAs, or PWAs

**Key Features**:

- Frontend/backend architecture
- Database design
- Authentication flows
- API specifications
- Deployment strategies

---

## Prompts

### Core Planning Prompts

#### AI_CTO.md

**Path**: `prompts/AI_CTO.md`

**Purpose**: Universal masterplan generator for any software project

**Usage**: Provide a RAW_IDEA, answer questions or type "continue", receive complete masterplan

**Output**: 17+ section masterplan including architecture, tech stack, implementation plan

**Best For**: Any software project (apps, extensions, tools, platforms)

---

#### ai_to.md

**Path**: `prompts/ai_to.md`

**Purpose**: Alternative masterplan generator with detailed question-based approach

**Usage**: Similar to AI_CTO but with more detailed questioning process

**Output**: Comprehensive masterplan.md with implementation phases

**Best For**: Projects requiring extensive planning and clarification

---

#### masterplan-generator.md

**Path**: `prompts/masterplan-generator.md`

**Purpose**: Generic masterplan generation framework

**Best For**: Creating custom masterplan templates

---

### Technology-Specific Prompts

#### gemini.md

**Path**: `prompts/gemini.md`

**Purpose**: Google Gemini API integration templates and patterns

**Usage**: Reference when integrating Gemini AI into projects

**Contains**:

- API configuration examples
- Authentication patterns
- Request/response formatting
- Error handling strategies

---

#### reactnative.md

**Path**: `prompts/reactnative.md`

**Purpose**: React Native development guidelines and 2025 stack recommendations

**Contains**:

- Expo framework setup
- Navigation patterns (Expo Router)
- UI/Styling libraries (NativeWind, Tamagui)
- State management (TanStack Query, Zustand)
- Essential packages and tooling

---

### Workflow Prompts

#### sprint.md

**Path**: `prompts/sprint.md`

**Purpose**: Agile sprint planning and execution guidance

**Contains**:

- Sprint goal definition
- User story templates
- Acceptance criteria formats
- Sprint retrospective guides

---

#### seq.md

**Path**: `prompts/seq.md`

**Purpose**: Sequential task processing and breakdown

**Usage**: Breaking complex problems into manageable steps

---

#### permanent message.md

**Path**: `prompts/permanent message.md`

**Purpose**: Define persistent behavior for AI assistants

**Contains**:

- Long-term AI assistant configuration
- Coding standards
- Communication protocols
- Custom AI personas

---

### Utility Prompts

#### common.md

**Path**: `prompts/common.md`

**Purpose**: Shared prompt patterns and reusable components

**Contains**:

- Response format templates
- Error handling patterns
- Output structure guidelines

---

#### aicon

**Path**: `prompts/aicon`

**Purpose**: Continue command handler snippet

**Usage**: Include in masterplan prompts to handle "continue" command from users

---

#### convert icopn.md

**Path**: `prompts/convert icopn.md`

**Purpose**: Icon conversion workflow instructions

**Usage**: Generating icon assets from SVG files

---

#### index.html.md

**Path**: `prompts/index.html.md`

**Purpose**: Landing page generation template

**Usage**: Creating landing pages for browser extensions or web apps

---

### Agent Configuration Prompts

#### auser guidelised.md

**Path**: `prompts/auser guidelised.md`

**Purpose**: Comprehensive agent operational guidelines (detailed version)

**Contains**: 1.11 sections covering all aspects of agent operation

---

#### auser guidelinesprompt.md

**Path**: `prompts/auser guidelinesprompt.md`

**Purpose**: Prompt for generating structured agent guidelines

---

---

## Projects

Complete PRD (Product Requirements Document) examples:

| File | Project Type | Key Features |
|------|--------------|--------------|
| [qrsay-call-waiter.md](projects/qrsay-call-waiter.md) | Mobile App | QR-based restaurant service |
| [quick-session-loader.md](projects/quick-session-loader.md) | Browser Extension | Session management |
| [text-warden-extension.md](projects/text-warden-extension.md) | Browser Extension | Text manipulation |
| [webpage-chat-extension.md](projects/webpage-chat-extension.md) | Browser Extension | AI chat on webpages |
| [wordtune-extension.md](projects/wordtune-extension.md) | Browser Extension | Writing enhancement |
| [youtube-summarizer-app.md](projects/youtube-summarizer-app.md) | Web/Mobile App | Video summarization |
| [youtube-summarizer-app-prd.md](projects/youtube-summarizer-app-prd.md) | Web/Mobile App | Detailed PRD version |

---

## Scripts

### gce.py

**Path**: `scripts/gce.py`

**Purpose**: Combine all prompt files into a single `final_prompt.txt`

**Usage**:

```bash
python scripts/gce.py
```

**Output**: `final_prompt.txt` in repository root

**Use Case**: Distributing combined prompts

---

### gemini.py

**Path**: `scripts/gemini.py`

**Purpose**: Google Gemini API utility script

**Usage**:

1. Set `GEMINI_API_KEY` environment variable
2. Modify the input placeholder
3. Run: `python scripts/gemini.py`

**Use Case**: Testing Gemini integrations

---

### gi.js

**Path**: `scripts/gi.js`

**Purpose**: Generate PNG icons from SVG source

**Usage**:

```bash
npm install sharp --save-dev
node scripts/gi.js
```

**Input**: `extension/icons/icon.svg`

**Output**: `icon16.png`, `icon48.png`, `icon128.png`

**Use Case**: Browser extension icon generation

---

## Documentation

### Core Documentation

#### AGENTS.md

**Path**: `AGENTS.md`

**Purpose**: Configuration guide for AI coding agents

**Contains**:

- Tech stack information
- Build/lint/test commands
- Architecture overview
- Code style conventions

---

#### USAGE_GUIDE.md

**Path**: `USAGE_GUIDE.md`

**Purpose**: Comprehensive usage guide for all repository templates

**Contains**:

- Template usage instructions
- Best practices
- Examples for common scenarios
- Troubleshooting guide

**Sections**: 18+ comprehensive sections

---

#### CHANGELOG.md

**Path**: `CHANGELOG.md`

**Purpose**: Version history and migration guides

**Contains**:

- Release notes
- Breaking changes
- Migration paths
- Deprecation notices

**Format**: Keep a Changelog standard

---

#### agent-guidelines.md

**Path**: `agent-guidelines.md`

**Purpose**: Detailed operational directives for AI agents

**Contains**:

- Execution workflow
- Code quality standards
- Tool usage protocols
- MCP server integration
- Error handling

---

### Specific Documentation

Located in `docs/specific/`:

| File | Topic | Purpose |
|------|-------|---------|
| Historical Context Tool.md | Context Management | Building context tracking tools |
| aicto.md | AI CTO Integration | CTO-level planning prompts |
| ai-reply-prd.md | Browser Extension | AI-powered reply generation |
| aiqa yt.md | YouTube Tools | YouTube QA integration |
| aireply.md | Browser Extension | Reply generation extension |
| all-pdf-tools-nextjs.md | Web App | PDF tools Next.js implementation |
| allpdf-python.md | Python App | PDF tools Python implementation |
| allpdf.md | Web App | Comprehensive PDF tools |
| allpdftools.md | General | PDF manipulation overview |
| ch.md | Unknown | Context handler |
| commit.md | Git Workflow | Commit message guidelines |
| contextual sidebar.md | UI Component | Context-aware sidebar |
| download file mcp.md | MCP Server | File download MCP server |
| md.md | Documentation | Markdown guidelines |
| pdf other features.md | PDF Tools | Additional PDF features |
| pdf-toolkei.md | React Native | PDF tools React Native |
| pdft.md | PDF Tools | PDF tool specifications |
| prompt boost.md | Prompt Engineering | Prompt enhancement |
| proxy.md | Configuration | Proxy setup |
| qrcode.md | QR Tools | QR code app specifications |
| read-aloud.md | Browser Extension | Text-to-speech extension |
| vscode.md | VS Code Extension | VS Code extension dev |
| vscodespeak.md | VS Code Extension | Voice-controlled VS Code |
| x.md | Unknown | Additional specs |
| yt summarizer browser extension..md | Browser Extension | YouTube summarizer |

---

### MCP Documentation

Located in `docs/mcp/` and `mcp/`:

#### main.md

**Path**: `mcp/main.md` (also `docs/mcp/main.md`)

**Purpose**: Comprehensive MCP server configuration guide

**Contains**:

- 7+ MCP server configurations
- Setup instructions
- Usage examples
- Integration patterns

**Servers Covered**:

1. Pieces MCP
2. Context7 MCP
3. Toolbox MCP (Smithery)
4. TypeScript SDK Docs MCP
5. Date and Time MCP
6. Clear Thought MCP
7. URL Content Saver MCP

---

#### kiro.txt

**Path**: `mcp/kiro.txt`

**Purpose**: Kiro MCP server specific configuration

---

#### servers-config.json

**Path**: `mcp/servers-config.json`

**Purpose**: MCP server configuration file (JSON format)

**Usage**: Copy to AI tool's configuration directory

---

### VS Code Documentation

#### setup.md

**Path**: `docs/vscode/setup.md`

**Purpose**: VS Code integration instructions

**Contains**: VS Code specific configuration and setup steps

---

## Configuration

### .gitignore

**Path**: `.gitignore`

**Purpose**: Git exclusion rules

**Contains**:

- Node.js exclusions
- Python exclusions
- Environment files
- Build outputs
- Temporary files
- OS-specific files

---

### pyproject.toml

**Path**: `pyproject.toml`

**Purpose**: Python project configuration

**Usage**: Python dependency and project metadata

---

### package-lock.json

**Path**: `package-lock.json`

**Purpose**: Node.js dependency lock file

**Usage**: Ensures consistent npm installations

---

### .flake8

**Path**: `.flake8`

**Purpose**: Python linting configuration

---

### .gitattributes

**Path**: `.gitattributes`

**Purpose**: Git attributes configuration

---

## File Naming Conventions

### Established Patterns

#### kebab-case (Preferred)

- `all-pdf-tools-nextjs.md`
- `read-aloud.md`
- `pdf-toolkei.md`
- `ai-reply-prd.md`

**Usage**: New files, renamed files, consistency

#### snake_case

- `AI_CTO.md` (legacy, kept for compatibility)
- `permanent message.md` (legacy)

#### No Extension

- `aicon` (small utility prompt)

### Recommendations

1. **New Files**: Use `kebab-case.md` format
2. **Directories**: Use `kebab-case` or `lowercase`
3. **Scripts**: Use `lowercase.py` or `lowercase.js`
4. **Important Files**: Can use `UPPERCASE.md` (README, LICENSE, CHANGELOG)

---

## Archive

### Purpose

Contains deprecated templates and old versions for reference and migration.

### Contents

| File | Status | Replacement |
|------|--------|-------------|
| aictoold.md | Deprecated | Use `prompts/AI_CTO.md` |
| aug.md | Duplicate | Use `other/aug.md` |
| augg.md | Duplicate | Use `other/aug.md` |
| final_prompt.txt | Archived | Regenerate with `scripts/gce.py` |

### README.md

**Path**: `archive/README.md`

**Purpose**: Deprecation notices and migration guides

**Contains**:

- Detailed deprecation information
- Migration paths
- Historical context

---

## Other Utilities

Located in `other/`:

| File | Purpose |
|------|---------|
| aug.md | General augmentation guidelines |
| cd.md | Unknown utility |
| ga.md | Unknown utility |
| gd.md | Unknown utility |
| grammarly.md | Writing improvement |
| qray.md | QR utility |
| qrsayapp.md | QR Say app specs |
| uc.md | Unknown utility |
| vct.md | Unknown utility |

---

## Search Strategies

### By Purpose

**Planning a Project**: `prompts/AI_CTO.md`, `templates/*.md`

**Building Browser Extension**: `templates/browser-extension-template.md`, `docs/specific/*extension*.md`

**Building Web App**: `templates/web-app-template.md`, `docs/specific/*app*.md`, `docs/specific/all*.md`

**Setting Up AI Tools**: `AGENTS.md`, `agent-guidelines.md`, `mcp/*.md`

**Learning the System**: `USAGE_GUIDE.md`, `CHANGELOG.md`

**Code Generation**: `scripts/*.py`, `scripts/*.js`

### By Technology

**React Native**: `prompts/reactnative.md`, `docs/specific/pdf-toolkei.md`

**Next.js**: `docs/specific/all-pdf-tools-nextjs.md`

**Python**: `scripts/*.py`, `docs/specific/allpdf-python.md`

**Gemini AI**: `prompts/gemini.md`, `scripts/gemini.py`

**PDF Tools**: `docs/specific/all*.md`, `docs/specific/pdf*.md`

---

## Quick Action Guide

### I want to

**...start a new project**

1. Read `prompts/AI_CTO.md`
2. Choose template from `templates/`
3. Follow output structure from template

**...build a browser extension**

1. Use `templates/browser-extension-template.md`
2. Reference similar projects in `docs/specific/`
3. Generate icons with `scripts/gi.js`

**...integrate Gemini AI**

1. Read `prompts/gemini.md`
2. Test with `scripts/gemini.py`
3. Reference integration examples

**...configure AI agents**

1. Read `AGENTS.md`
2. Study `agent-guidelines.md`
3. Configure MCP servers from `mcp/`

**...understand deprecated files**

1. Check `archive/README.md`
2. Find migration path
3. Use replacement files

---

## Maintenance Notes

### Adding New Files

1. **Choose appropriate directory**: `prompts/`, `projects/`, `docs/specific/`, etc.
2. **Use kebab-case naming**: `my-new-file.md`
3. **Add header comment**: Explain purpose and usage
4. **Update this index**: Add entry with description
5. **Update CHANGELOG.md**: Document the addition

### Updating Files

1. **Preserve backward compatibility**: When possible
2. **Update CHANGELOG.md**: Document changes
3. **Check dependencies**: Update related files
4. **Test thoroughly**: Verify no broken links

### Deprecating Files

1. **Move to archive/**: Don't delete
2. **Update archive/README.md**: Add deprecation notice
3. **Provide migration path**: Point to replacement
4. **Update CHANGELOG.md**: Document deprecation

---

## Version Information

**Index Version**: 1.0.0  
**Repository Version**: 2.0.0  
**Last Updated**: 2025-01-XX  
**Maintained by**: Chirag Singhal (@chirag127)
