# Prompts

[![Stars](https://img.shields.io/github/stars/chirag127/prompts?style=flat-square)](https://github.com/chirag127/prompts/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

Live: **https://prompts.oriz.in**

Curated expert AI prompt library — software architecture, DevOps, app/extension specs, agent system prompts, and reusable templates.

---

## How to Use

Browse the catalog at [prompts.oriz.in](https://prompts.oriz.in) or navigate the [`library/`](library/) directory directly. Copy any prompt into your AI assistant or agent workflow.

---

## Library Structure

```
library/
  agents/       # AI CTO, agent guidelines, masterplan generators, sprint planner
  app-specs/    # Product specs and PRDs for PDF tools, YT summarizer, browser exts
  templates/    # Browser extension, web app, masterplan.md templates
  mcp/          # MCP server config prompts (keys redacted — replace with yours)
```

## Categorized Index

### Agent System Prompts (`library/agents/`)

| File | Description |
|------|-------------|
| [ai-cto.md](library/agents/ai-cto.md) | AI CTO — Masterplan Architect. Transforms a raw idea into a full `masterplan.md` |
| [ai-cto-simple.md](library/agents/ai-cto-simple.md) | Simpler AI CTO variant with question-first approach |
| [masterplan-generator.md](library/agents/masterplan-generator.md) | Masterplan generator with detailed structure guidelines |
| [agent-guidelines.md](library/agents/agent-guidelines.md) | Agent operational directives (identity, execution, tooling) |
| [augment-agent-guidelines.md](library/agents/augment-agent-guidelines.md) | Augment Agent specific guidelines |
| [augment-code-guidelines.md](library/agents/augment-code-guidelines.md) | Augment Code A-Z completion guidelines |
| [sprint-planner.md](library/agents/sprint-planner.md) | Sprint planning prompt for AI CTO |
| [react-native-stack-2025.md](library/agents/react-native-stack-2025.md) | Recommended React Native / Expo stack (2025) |
| [sequential-thinking.md](library/agents/sequential-thinking.md) | Sequential thinking + web search pattern |
| [common-patterns.md](library/agents/common-patterns.md) | Reusable prompt components and patterns |
| [gemini-agent.md](library/agents/gemini-agent.md) | Gemini-specific agent prompt |
| [vibe-coding-tutorial.md](library/agents/vibe-coding-tutorial.md) | Vibe coding tutorial prompt |

### App Specs & PRDs (`library/app-specs/`)

| File | Description |
|------|-------------|
| [all-pdf-tools-react-native.md](library/app-specs/all-pdf-tools-react-native.md) | All PDF Tools — React Native Expo app spec |
| [all-pdf-tools-nextjs.md](library/app-specs/all-pdf-tools-nextjs.md) | All PDF Tools — Next.js app spec |
| [youtube-summarizer-app.md](library/app-specs/youtube-summarizer-app.md) | YouTube Summarizer app spec |
| [youtube-summarizer-prd.md](library/app-specs/youtube-summarizer-prd.md) | YouTube Summarizer PRD |
| [youtube-summarizer-browser-ext.md](library/app-specs/youtube-summarizer-browser-ext.md) | YouTube Summarizer browser extension spec |
| [wordtune-extension.md](library/app-specs/wordtune-extension.md) | Wordtune-like browser extension spec |
| [webpage-chat-extension.md](library/app-specs/webpage-chat-extension.md) | Webpage chat browser extension spec |
| [qrsay-call-waiter.md](library/app-specs/qrsay-call-waiter.md) | QRSay call-waiter feature PRD |
| [text-warden-extension.md](library/app-specs/text-warden-extension.md) | Text Warden browser extension spec |
| [quick-session-loader-ext.md](library/app-specs/quick-session-loader-ext.md) | Quick Session Loader extension spec |
| [vscode-extension-spec.md](library/app-specs/vscode-extension-spec.md) | VS Code extension development spec |
| [git-commit-assistant.md](library/app-specs/git-commit-assistant.md) | Git commit message assistant spec |
| [historical-context-tool.md](library/app-specs/historical-context-tool.md) | Historical context MCP tool spec |
| [prompt-boost.md](library/app-specs/prompt-boost.md) | Prompt enhancement tool spec |

### Templates (`library/templates/`)

| File | Description |
|------|-------------|
| [browser-extension-template.md](library/templates/browser-extension-template.md) | Complete browser extension scaffold prompt |
| [web-app-template.md](library/templates/web-app-template.md) | Web application scaffold prompt |
| [masterplan-template.md](library/templates/masterplan-template.md) | masterplan.md document template |
| [browser-ext-landing-page.md](library/templates/browser-ext-landing-page.md) | Landing page + privacy policy prompt for browser extensions |

### MCP Server Configs (`library/mcp/`)

> Keys are redacted — replace `YOUR_SMITHERY_KEY`, `YOUR_SMITHERY_PROFILE`, `YOUR_BRIGHTDATA_TOKEN` with your own.

| File | Description |
|------|-------------|
| [mcp-servers-guide.md](library/mcp/mcp-servers-guide.md) | MCP server setup guide |
| [mcp-config-augment.json](library/mcp/mcp-config-augment.json) | MCP server config for Augment Code |
| [mcp-config-kiro.json](library/mcp/mcp-config-kiro.json) | MCP server config for Kiro |

---

## Contributing

Issues and PRs welcome. Keep prompts generic (no hardcoded secrets or personal credentials).

---

## License

MIT — see [LICENSE](LICENSE).
