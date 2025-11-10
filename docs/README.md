# Prompts Repository

> A curated collection of AI prompt templates, configurations, and utilities for software development and content generation

## 📋 Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Quick Start](#quick-start)
- [Template Categories](#template-categories)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This repository serves as a comprehensive collection of prompt engineering templates, AI assistant configurations, and automation utilities designed to enhance software development workflows. It includes templates for various AI models and use cases, from general-purpose development to specific project implementations.

### Key Features

- **General Purpose Prompts**: Reusable templates for common development tasks
- **Project-Specific Configurations**: Tailored prompts for specific applications
- **MCP Server Configurations**: Model Context Protocol server setups
- **Utility Scripts**: Automation tools for prompt generation and management
- **Archive**: Historical templates with clear deprecation notes

## 📁 Repository Structure

```
prompts/
├── prompts/          # General-purpose prompt templates
│   ├── AI_CTO.md           # CTO-level technical planning and architecture
│   ├── common.md           # Common prompt patterns and utilities
│   ├── gemini.md           # Google Gemini API specific prompts
│   ├── reactnative.md      # React Native development templates
│   ├── sprint.md           # Agile sprint planning prompts
│   └── ...                 # Additional general templates
│
├── specific/         # Project-specific prompt configurations
│   ├── aireply.md          # AI Reply extension prompts
│   ├── allpdftools.md      # PDF Tools project prompts
│   ├── qrcode.md           # QR Code generator prompts
│   ├── vscode.md           # VS Code extension prompts
│   └── ...                 # Additional project templates
│
├── other/            # Utility and miscellaneous prompts
│   ├── aug.md              # General augmentation guidelines
│   ├── grammarly.md        # Grammarly-related prompts
│   └── ...                 # Additional utilities
│
├── mcp/              # Model Context Protocol configurations
│   ├── main.md             # MCP server configurations
│   └── kiro.txt            # Kiro MCP settings
│
├── script/           # Automation and utility scripts
│   └── gi.js               # Gitignore generation script
│
├── archive/          # Deprecated templates and historical content
│   ├── README.md           # Archive documentation
│   └── ...                 # Archived templates
│
├── vscode/           # VS Code specific configurations
├── secrets/          # Secret management templates (not tracked)
├── gce.py            # Google Compute Engine utilities
├── gemini.py         # Gemini API interaction scripts
└── AGENTS.md         # AI agent configuration guide
```

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/chirag127/prompts.git
cd prompts
```

### 2. Browse Templates

Navigate to the appropriate directory based on your needs:

- **General development tasks**: Check `prompts/` directory
- **Specific project implementation**: Browse `specific/` directory
- **MCP server setup**: See `mcp/` directory
- **Utility configurations**: Explore `other/` directory

### 3. Use a Template

Copy the template content and customize it for your specific use case. See [USAGE_GUIDE.md](./USAGE_GUIDE.md) for detailed instructions.

## 📚 Template Categories

### General Purpose Prompts (`prompts/`)

Reusable templates for common development scenarios:

- **AI_CTO.md**: Comprehensive masterplan generation for technical architecture
- **common.md**: Shared prompt patterns and utilities
- **gemini.md**: Google Gemini API integration templates
- **reactnative.md**: React Native mobile development
- **sprint.md**: Agile sprint planning and management
- **permanent message.md**: Persistent AI assistant instructions

[See detailed usage guide](./USAGE_GUIDE.md#general-purpose-prompts)

### Project-Specific Prompts (`specific/`)

Tailored configurations for particular projects and applications:

- Browser extensions (AI Reply, YouTube Summarizer, Webpage Chat)
- PDF manipulation tools (allpdftools, pdf-toolkei)
- QR code applications (qrcode, qrsayapp)
- VS Code extensions and integrations
- Context management tools (Historical Context Tool, contextual sidebar)

[See detailed usage guide](./USAGE_GUIDE.md#project-specific-prompts)

### Utility Prompts (`other/`)

Helper templates and augmentation guidelines:

- **aug.md**: General development guidelines and best practices
- **grammarly.md**: Grammar and writing improvement prompts
- Context and quality assurance templates

[See detailed usage guide](./USAGE_GUIDE.md#utility-prompts)

### MCP Configurations (`mcp/`)

Model Context Protocol server configurations for various AI tools and services. These enable enhanced AI interactions with specific capabilities.

[See detailed usage guide](./USAGE_GUIDE.md#mcp-configurations)

## 💡 Usage

### Basic Usage

1. **Select a template** from the appropriate category
2. **Read the template** to understand its purpose and structure
3. **Customize** the template with your specific requirements
4. **Apply** the prompt to your AI assistant or development workflow

### Advanced Usage

For complex projects requiring multiple templates:

1. Start with a general template (e.g., `AI_CTO.md` for architecture)
2. Layer in project-specific configurations from `specific/`
3. Add utility guidelines from `other/` as needed
4. Configure MCP servers if using advanced AI tooling

See the comprehensive [USAGE_GUIDE.md](./USAGE_GUIDE.md) for detailed examples and best practices.

## 🔧 Utilities

### Python Scripts

- **gce.py**: Google Compute Engine interaction utilities
- **gemini.py**: Google Gemini API wrapper and helpers

### JavaScript Scripts

- **script/gi.js**: Automated gitignore file generation
- **a.js**: Additional automation utilities

### Usage Examples

```bash
# Generate a gitignore file
node script/gi.js

# Interact with Gemini API
python gemini.py
```

## 🤝 Contributing

Contributions are welcome! To contribute:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/new-template`)
3. **Add** your template following existing conventions
4. **Commit** with clear messages (`git commit -m "Add: New template for X"`)
5. **Push** to your fork (`git push origin feature/new-template`)
6. **Open** a Pull Request

### Guidelines

- Follow the existing directory structure
- Include clear documentation within templates
- Add examples where appropriate
- Update relevant USAGE_GUIDE.md sections
- Test templates before submitting

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📖 Additional Documentation

- [USAGE_GUIDE.md](./USAGE_GUIDE.md) - Comprehensive usage instructions
- [CHANGELOG.md](./CHANGELOG.md) - Version history and changes
- [AGENTS.md](./AGENTS.md) - AI agent configuration guide
- [archive/README.md](./archive/README.md) - Deprecated templates documentation

## 🔗 Related Resources

- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [Google Gemini API Documentation](https://ai.google.dev/)
- [Model Context Protocol](https://modelcontextprotocol.io/)

## 💬 Support

For questions, issues, or suggestions:

- Open an [Issue](https://github.com/chirag127/prompts/issues)
- Check existing documentation
- Review the archive for historical context

---

**Maintained by**: Chirag Singhal (@chirag127)
