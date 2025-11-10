# AGENTS.md

## Commands

**Initial Setup:** No package manager or virtual environment needed - files are standalone scripts and markdown documents.

**Build:** No build step required.

**Lint:** No linter configured.

**Tests:** No test suite configured.

**Dev Server:** No dev server - scripts run independently.

## Tech Stack & Architecture

- **Languages:** Python 3, JavaScript (Node.js)
- **Key Scripts:** `script/gemini.py` (Gemini API client), `script/gce.py` (prompt combiner)
- **Structure:** 
  - `prompts/` - AI prompt templates and guidelines
  - `docs/specific/` - Project-specific configurations and docs
  - `script/` - Utility scripts (icon generation using sharp)
  - Root-level Python scripts (`gce.py`, `gemini.py`) and JS files

## Code Conventions

- Python: Standard library focused, minimal dependencies (google-generativeai, requests, beautifulsoup4)
- Python scripts use standard formatting, no external dependencies visible
- No consistent code style enforced (no linter/formatter config)
- Files are self-contained utilities rather than integrated modules
- Script-based workflow: combine prompts from `/prompts`, send to Gemini API
