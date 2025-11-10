# AGENTS.md

## Commands

**Setup:** No package manager detected. This is a collection of scripts and prompts.

**Build:** N/A

**Lint:** N/A

**Tests:** N/A

**Dev Server:** N/A

## Tech Stack & Architecture

- **Languages:** Python 3, JavaScript
- **Key Scripts:** `script/gemini.py` (Gemini API client), `script/gce.py` (prompt combiner)
- **Structure:** `/prompts` - AI prompt templates, `/script` - utilities, `/docs` - documentation including specific project docs and MCP server configs

## Code Style & Conventions

- Python: Standard library focused, minimal dependencies (google-generativeai, requests, beautifulsoup4)
- No formal linting/testing framework in place
- Script-based workflow: combine prompts from `/prompts`, send to Gemini API
