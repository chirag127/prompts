# AGENTS.md

## Commands

### Initial Setup
No formal setup required. For Python scripts: ensure Python 3 is installed. For JavaScript scripts: ensure Node.js is installed and run `npm install` if needed.

### Build
No build process defined.

### Lint
No linter configured.

### Tests
No test suite configured.

### Dev Server
No dev server. Scripts are run individually (`python <script>.py` or `node <script>.js`).

## Tech Stack & Architecture

- **Languages**: Python 3, JavaScript (Node.js)
- **Purpose**: Prompt engineering templates and documentation repository
- **Key Scripts**: `script/gemini.py` (Gemini API client), `script/gce.py` (prompt combiner)
- **Structure**: 
  - `prompts/` - General purpose AI prompt templates
  - `specific/` - Project-specific configurations and prompts
  - `templates/` - Reusable masterplan templates organized by project type
  - `other/` - Utility templates
  - `mcp/` - MCP server configurations
  - `archive/` - Deprecated templates
  - `script/` - Utility scripts (icon generation using sharp)
  - Root-level Python scripts (`gce.py`, `gemini.py`) and JS files
- **Dependencies**: Python scripts use `google.generativeai`; JavaScript scripts may use Node.js libraries like `sharp`

## Code Style & Conventions

- Python files use standard library imports (google-generativeai, requests, beautifulsoup4 for key scripts)
- JavaScript files follow Node.js conventions with CommonJS modules
- Markdown files stored in categorized directories and serve as prompt templates and documentation
- No consistent code style enforced (no linter/formatter config)
- Files are self-contained utilities rather than integrated modules
- Script-based workflow: combine prompts from `/prompts`, send to Gemini API
