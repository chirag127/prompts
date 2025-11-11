# AI Prompts Repository

> A comprehensive collection of AI prompt templates, system prompts, and utility scripts for software development workflows

## 📁 Repository Structure

```
prompts-repository/
├── 📂 templates/          # Reusable project templates
│   ├── browser-extension-template.md
│   └── web-app-template.md
│
├── 📂 prompts/            # General-purpose AI prompts
│   ├── AI_CTO.md                    # Technical masterplan generation
│   ├── ai_to.md                     # Alternative masterplan generator
│   ├── aicon                        # Continue command handler
│   ├── common.md                    # Common prompt patterns
│   ├── gemini.md                    # Gemini API integration
│   ├── masterplan-generator.md      # Project masterplan creation
│   ├── generate master plan.md      # Additional planning prompt
│   ├── permanent message.md         # Persistent AI instructions
│   ├── reactnative.md               # React Native development
│   ├── sprint.md                    # Agile sprint planning
│   ├── seq.md                       # Sequential task processing
│   ├── mstemplate.md                # Masterplan template
│   ├── index.html.md                # Landing page generation
│   ├── convert icopn.md             # Icon conversion workflows
│   ├── vibe coding tutorial.md      # Coding tutorials
│   ├── auser guidelinesprompt.md    # User guidelines prompt
│   └── auser guidelised.md          # Comprehensive agent guidelines
│
├── 📂 projects/           # Project-specific PRDs and specifications
│   ├── qrsay-call-waiter.md
│   ├── quick-session-loader.md
│   ├── text-warden-extension.md
│   ├── webpage-chat-extension.md
│   ├── wordtune-extension.md
│   ├── youtube-summarizer-app.md
│   └── youtube-summarizer-app-prd.md
│
├── 📂 scripts/            # Automation and utility scripts
│   ├── gce.py              # Prompt combiner script
│   ├── gemini.py           # Gemini API utilities
│   └── gi.js               # Icon generation script
│
├── 📂 docs/               # Documentation and guides
│   ├── AGENTS.md           # Agent configuration
│   ├── LICENSE             # Repository license
│   ├── README.md           # Documentation index
│   ├── 📂 specific/        # Project-specific documentation
│   │   ├── Historical Context Tool.md
│   │   ├── aicto.md
│   │   ├── ai-reply-prd.md
│   │   ├── aiqa yt.md
│   │   ├── aireply.md
│   │   ├── all-pdf-tools-nextjs.md
│   │   ├── allpdf-python.md
│   │   ├── allpdf.md
│   │   ├── allpdftools.md
│   │   ├── ch.md
│   │   ├── commit.md
│   │   ├── contextual sidebar.md
│   │   ├── download file mcp.md
│   │   ├── md.md
│   │   ├── pdf other features.md
│   │   ├── pdf-toolkei.md
│   │   ├── pdft.md
│   │   ├── prompt boost.md
│   │   ├── proxy.md
│   │   ├── qrcode.md
│   │   ├── read-aloud.md
│   │   ├── vscode.md
│   │   ├── vscodespeak.md
│   │   ├── x.md
│   │   └── yt summarizer browser extension..md
│   └── 📂 vscode/          # VS Code specific configurations
│       └── setup.md
│
├── 📂 mcp/                # MCP server configurations
│   ├── main.md             # Comprehensive MCP configs
│   ├── kiro.txt            # Kiro MCP settings
│   └── servers-config.json # MCP server configuration
│
├── 📂 other/              # Miscellaneous utilities
│   ├── aug.md              # Augmentation guidelines
│   ├── cd.md
│   ├── ga.md
│   ├── gd.md
│   ├── grammarly.md
│   ├── qray.md
│   ├── qrsayapp.md
│   ├── uc.md
│   └── vct.md
│
├── 📂 archive/            # Deprecated templates and backups
│   ├── README.md           # Deprecation notices and migration guides
│   ├── aictoold.md         # Old AI CTO template
│   ├── aug.md              # Duplicate augmentation guidelines
│   ├── augg.md             # Duplicate augmentation guidelines
│   └── final_prompt.txt    # Archived combined prompt
│
├── 📄 AGENTS.md           # AI agent operational guidelines
├── 📄 CHANGELOG.md        # Version history and changes
├── 📄 USAGE_GUIDE.md      # Comprehensive usage documentation
├── 📄 agent-guidelines.md # Agent operational directives
└── 📄 .gitignore          # Git exclusions
```

## 🚀 Quick Start

### For General Development Tasks
Use prompts in the `/prompts` directory:
- **AI_CTO.md**: Generate comprehensive technical masterplans
- **gemini.md**: Integrate Google Gemini API
- **reactnative.md**: Build React Native applications
- **sprint.md**: Plan agile sprints

### For Specific Projects
Browse the `/projects` and `/docs/specific` directories for detailed PRDs and specifications.

### For Code Generation
Use templates in the `/templates` directory as starting points.

## 📚 Key Files

### Core Documentation
- **[REPOSITORY_INDEX.md](REPOSITORY_INDEX.md)** - **📑 Complete file reference and navigation guide**
- **[AGENTS.md](AGENTS.md)** - Configuration for AI coding agents
- **[USAGE_GUIDE.md](USAGE_GUIDE.md)** - Comprehensive usage instructions
- **[CHANGELOG.md](CHANGELOG.md)** - Version history and migration guides
- **[agent-guidelines.md](agent-guidelines.md)** - Detailed agent operational directives

### Templates
- **[browser-extension-template.md](templates/browser-extension-template.md)** - Browser extension boilerplate
- **[web-app-template.md](templates/web-app-template.md)** - Web application template

### Utility Scripts
- **[gce.py](scripts/gce.py)** - Combine prompt files
- **[gemini.py](scripts/gemini.py)** - Gemini API utilities
- **[gi.js](scripts/gi.js)** - Icon generation automation

## 🎯 Common Use Cases

### 1. Generate a Technical Masterplan
```
Use: prompts/AI_CTO.md
Purpose: Create comprehensive technical specifications for any project
Output: Complete masterplan.md with architecture, stack, and implementation plan
```

### 2. Build a Browser Extension
```
Use: templates/browser-extension-template.md + docs/specific/[relevant-extension].md
Purpose: Rapid browser extension development
Output: Production-ready extension code
```

### 3. Configure MCP Servers
```
Use: mcp/main.md or mcp/servers-config.json
Purpose: Set up Model Context Protocol servers
Output: Configured AI tool integrations
```

### 4. Plan Development Sprints
```
Use: prompts/sprint.md
Purpose: Organize agile development cycles
Output: Sprint plans with tasks and timelines
```

## 🔧 Configuration Files

- **mcp/servers-config.json** - MCP server configurations
- **.gitignore** - Git exclusion rules
- **pyproject.toml** - Python project configuration
- **package-lock.json** - Node.js dependencies

## 📖 Documentation

### Main Guides
- [Usage Guide](USAGE_GUIDE.md) - Detailed usage instructions for all templates
- [Agent Guidelines](agent-guidelines.md) - Operational directives for AI agents
- [Changelog](CHANGELOG.md) - Version history and migration guides

### Specific Documentation
- [MCP Configurations](mcp/main.md) - Model Context Protocol server setup
- [VS Code Setup](docs/vscode/setup.md) - VS Code integration instructions
- [Archive Documentation](archive/README.md) - Deprecated template information

## 🤝 Contributing

This repository is a personal collection of AI prompts and templates. Feel free to:
- Report issues with templates
- Suggest improvements
- Share your own prompt variations

## 👤 Author

**Chirag Singhal** ([@chirag127](https://github.com/chirag127))

## 📄 License

See [docs/LICENSE](docs/LICENSE) for details.

## 🗂️ Directory Purpose Guide

### `/prompts` - General Purpose Templates
System prompts and templates for common development tasks. Use these for:
- Project planning and architecture
- API integrations
- Development workflows
- Code generation guidelines

### `/projects` - Complete Project Specifications
Full PRDs and specifications for complete applications. Use these as:
- Reference implementations
- Project inspiration
- Complete specification examples

### `/templates` - Boilerplate Starting Points
Ready-to-use templates for common project types. Use these to:
- Kickstart new projects quickly
- Ensure consistent structure
- Follow best practices

### `/scripts` - Automation Utilities
Helper scripts for prompt management and asset generation. Use these to:
- Combine multiple prompts
- Generate icons and assets
- Automate repetitive tasks

### `/docs` - Extended Documentation
Detailed guides, configurations, and project-specific documentation. Use these for:
- In-depth learning
- Project-specific requirements
- Reference documentation

### `/mcp` - MCP Server Configurations
Model Context Protocol server setup and configuration files. Use these for:
- Configuring AI tool integrations
- Setting up context servers
- Managing MCP tools

### `/other` - Miscellaneous Utilities
Helper prompts and utilities that don't fit other categories. Use these for:
- Writing assistance
- Quality assurance
- General augmentation

### `/archive` - Deprecated Content
Old versions and deprecated templates. Check these for:
- Migration paths from old templates
- Historical reference
- Legacy project support

## 🔍 Finding What You Need

1. **Looking for a specific file?** → See [REPOSITORY_INDEX.md](REPOSITORY_INDEX.md) 📑
2. **Need to plan a project?** → Start with `/prompts/AI_CTO.md`
3. **Building a specific app type?** → Check `/projects` or `/docs/specific`
4. **Want a quick start?** → Use `/templates`
5. **Setting up tools?** → See `/mcp` directory
6. **Running automation?** → Execute scripts in `/scripts`
7. **Learning the system?** → Read [USAGE_GUIDE.md](USAGE_GUIDE.md)

## 🔄 Recent Updates

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

---

**Last Updated**: 2025-01-XX  
**Repository Version**: 2.0.0  
**Maintained by**: Chirag Singhal
