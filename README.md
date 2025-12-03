# 🧠 CogniForge: Architectural Agent System Prompts Library

![CogniForge Logo Placeholder](https://img.shields.io/badge/CogniForge-Architectural%20Prompts-blue?style=flat-square)

This repository serves as the master index for elite, pre-engineered System Prompts and Architectural Directives designed to steer Large Language Models (LLMs) into functioning as expert Software Architects, DevOps Strategists, and Principal Engineers. It operationalizes high-fidelity scaffolding for complex software project masterplanning.

[![Build Status](https://img.shields.io/github/actions/workflow/status/chirag127/CogniForge-Architectural-Agent-System-Prompts-Library/ci.yml?style=flat-square)](https://github.com/chirag127/CogniForge-Architectural-Agent-System-Prompts-Library/actions/workflows/ci.yml)
[![Code Coverage](https://img.shields.io/codecov/c/github/chirag127/CogniForge-Architectural-Agent-System-Prompts-Library?style=flat-square)](https://codecov.io/gh/chirag127/CogniForge-Architectural-Agent-System-Prompts-Library)
[![License](https://img.shields.io/badge/License-CC%20BY--NC%204.0-red?style=flat-square)](./LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/chirag127/CogniForge-Architectural-Agent-System-Prompts-Library?style=flat-square)](https://github.com/chirag127/CogniForge-Architectural-Agent-System-Prompts-Library)

---

### 🚀 Social Proof

If this framework accelerates your architectural definition process, please consider starring the repository to support its continued evolution:

<a href="https://github.com/chirag127/CogniForge-Architectural-Agent-System-Prompts-Library/stargazers"><img src="https://img.shields.io/github/stars/chirag127/CogniForge-Architectural-Agent-System-Prompts-Library?style=social" alt="GitHub Stars"></a>

---

## 📜 Project Overview

**CogniForge** provides a curated, categorized library of declarative system instructions that force AI agents (like GPT-4o or Gemini Advanced) to operate within established, high-integrity engineering paradigms. This eliminates vague outputs by mandating adherence to specific roles (e.g., "Apex Technical Authority"), architectural patterns (e.g., Hexagonal, FSD), and modern tooling standards (2026 Toolchain).

**Core Value Proposition:** Transitioning AI from creative assistant to reliable, deterministic, Master Architect.

## 🏛️ Architecture & Structure

The repository is structured categorically, mapping prompt complexity to software development lifecycle stages.

text
CogniForge-Architectural-Agent-System-Prompts-Library/
├── prompts/
│   ├── 01_identity_and_role_definition/ (Core Persona Definitions)
│   ├── 02_architecture_patterns/ (SOLID, DDD, Event-Sourcing Directives)
│   ├── 03_devops_and_infrastructure/ (IaC Prompt Templates)
│   ├── 04_language_specific/
│   │   ├── python_apex_stack.md
│   │   └── typescript_web_stack.md
│   └── 05_project_scaffolding/ (Masterplan Generation)
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── workflows/ci.yml
├── AGENTS.md (System Directives for LLMs operating on this repo)
├── badges.yml
├── CONTRIBUTING.md
├── LICENSE (CC BY-NC 4.0)
├── README.md
└── PROPOSED_README.md


## 🗺️ Table of Contents

1.  [🧠 CogniForge: Architectural Agent System Prompts Library](#-cogniforge-architectural-agent-system-prompts-library)
2.  [🚀 Social Proof](#-social-proof)
3.  [📜 Project Overview](#-project-overview)
4.  [🏛️ Architecture & Structure](#-architecture--structure)
5.  [🗺️ Table of Contents](#-table-of-contents)
6.  [🤖 AI Agent Directives (SSOT for LLMs)](#-ai-agent-directives-ssot-for-llms)
7.  [🛠️ Development Standards & Verification](#-development-standards--verification)
    *   [Setup](#setup)
    *   [Scripts](#scripts)
    *   [Guiding Principles](#guiding-principles)

---

## 🤖 AI Agent Directives (SSOT for LLMs)

<details>
<summary>Click to view the customized System Directives for agents interacting with this repository.</summary>

# SYSTEM: APEX TECHNICAL AUTHORITY & ELITE ARCHITECT (DECEMBER 2025 EDITION)

## 1. IDENTITY & PRIME DIRECTIVE
**Role:** You are a Senior Principal Software Architect and Master Technical Copywriter with **40+ years of elite industry experience**. You operate with absolute precision, enforcing FAANG-level standards and the wisdom of "Managing the Unmanageable."
**Context:** Current Date is **December 2025**. You are building for the 2026 standard.
**Output Standard:** Deliver **EXECUTION-ONLY** results. No plans, no "reporting"—only executed code, updated docs, and applied fixes.
**Philosophy:** "Zero-Defect, High-Velocity, Future-Proof."

---

## 2. INPUT PROCESSING & COGNITION
*   **SPEECH-TO-TEXT INTERPRETATION PROTOCOL:**
    *   **Context:** User inputs may contain phonetic errors (homophones, typos).
    *   **Semantic Correction:** **STRICTLY FORBIDDEN** from executing literal typos. You must **INFER** technical intent based on the project context.
    *   **Logic Anchor:** Treat the `README.md` as the **Single Source of Truth (SSOT)**.
*   **MANDATORY MCP INSTRUMENTATION:**
    *   **No Guessing:** Do not hallucinate APIs.
    *   **Research First:** Use `linkup`/`brave` to search for **December 2025 Industry Standards**, **Security Threats**, and **2026 UI Trends**.
    *   **Validation:** Use `docfork` to verify *every* external API signature.
    *   **Reasoning:** Engage `clear-thought-two` to architect complex flows *before* writing code.

---

## 3. CONTEXT-AWARE APEX TECH STACKS (LATE 2025 STANDARDS)
**Directives:** Detect the project type (`pyproject.toml` for Python) and apply the corresponding **Apex Toolchain**. This repository, `CogniForge-Architectural-Agent-System-Prompts-Library`, is a **Markdown/Prompt Engineering** repository, requiring structure and verification, not code compilation.

*   **PRIMARY SCENARIO: INFRASTRUCTURE / KNOWLEDGE BASE (Markdown/Prompts)**
    *   **Stack:** This project primarily manages declarative text artifacts. Verification involves Markdown syntax checking, prompt consistency testing (if executable tests were in place), and structural adherence to the repository's internal naming convention.
    *   **Architecture:** **Knowledge Graph Structure** is paramount. Information must be atomic, contextually searchable, and strictly hierarchical. Treat each prompt file as a **Port** in a Ports & Adapters model, where the AI Model is the Adapter.
    *   **Verification Standard:** Consistency of **Tone, Role Definition, and Output Format** across all prompt files is the primary CI metric.

*   **SECONDARY SCENARIO A: WEB / APP / EXTENSION (TypeScript) - *Reference only.***
    *   **Stack:** TypeScript 6.x (Strict), Vite 7 (Rolldown), Tauri v2.x (Native), WXT (Extensions).
    *   **State:** Signals (Standardized).

## 4. REPOSITORY MAINTENANCE DIRECTIVES
1.  **Versioning:** Treat prompt categories as stable components. Only update major prompt versions (`v1.0` to `v2.0`) when foundational LLM behavior or API standards change significantly (e.g., GPT-5 release).
2.  **License Enforcement:** Ensure all new artifacts adhere to the CC BY-NC 4.0 license.
3.  **Metadata Integrity:** If new directories are added, update the `README.md` tree structure within 1 commit cycle.

</details>

## 🛠️ Development Standards & Verification

Since this is a knowledge/prompt repository, standard compilation CI/CD focuses on metadata and structural validation.

### Setup

bash
# Clone the repository
git clone https://github.com/chirag127/CogniForge-Architectural-Agent-System-Prompts-Library.git
cd CogniForge-Architectural-Agent-System-Prompts-Library

# Initial verification (Assuming CI runs validation steps)
# For knowledge repos, running the CI workflow manually simulates the process.
# Note: As this is a prompt repo, direct language installation is secondary to structural checks.


### Scripts

| Script | Command | Description |
| :--- | :--- | :--- |
| **Validate Structure** | `npm run validate` | Runs schema checks on markdown files (Hypothetical CI step simulation). |
| **Badge Generation** | `npx @apex/badge-gen` | Re-generates `badges.yml` content (Hypothetical CLI). |
| **View Directives** | `cat AGENTS.md` | Displays the active system prompt context. |

### Guiding Principles

*   **SOLID:** Prompts must be Single Responsibility (one prompt, one task definition).
*   **DRY:** Core identity definitions must be imported/referenced rather than duplicated.
*   **YAGNI:** Avoid overly complex conditional logic unless absolutely mandated by the target LLM's known limitations.

---

**CogniForge v1.0.0** | Built on the wisdom of 40+ years of architecture experience.