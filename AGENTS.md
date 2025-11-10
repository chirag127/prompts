# AGENTS.md

## Commands

**Initial Setup:** No package manager or virtual environment needed - files are standalone scripts and markdown documents.

**Build:** No build step required.

**Lint:** No linter configured.

**Tests:** No test suite configured.

**Dev Server:** No dev server - scripts run independently.

## Tech Stack & Architecture

- **Languages:** Python 3, JavaScript (Node.js)
- **Purpose:** Prompt engineering templates and documentation repository
- **Key Scripts:** `script/gemini.py` (Gemini API client), `script/gce.py` (prompt combiner)
- **Structure:** 
  - `prompts/` - General purpose AI prompt templates
  - `specific/` - Project-specific configurations and prompts
  - `other/` - Utility templates
  - `mcp/` - MCP server configurations
  - `archive/` - Deprecated templates
  - `script/` - Utility scripts (icon generation using sharp)
  - Root-level Python scripts (`gce.py`, `gemini.py`) and JS files

## Code Style & Conventions

- Python files use standard library imports (google-generativeai, requests, beautifulsoup4 for key scripts)
- JavaScript files follow Node.js conventions with CommonJS modules
- Markdown files stored in categorized directories
- No consistent code style enforced (no linter/formatter config)
- Files are self-contained utilities rather than integrated modules
- Script-based workflow: combine prompts from `/prompts`, send to Gemini API
