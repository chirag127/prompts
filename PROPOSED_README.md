# CogniForge-Architectural-Agent-System-Prompts-Library

A meticulously curated repository housing advanced System Prompts, Architectural Agent Directives, and foundational development templates. Engineered for AI-driven software architecture, masterplan generation, and optimized developer workflows.

---

## 🚀 Project Overview

**CogniForge** is an elite, categorized library designed to elevate AI-assisted software engineering. It provides sophisticated System Prompts, Architectural Agent Directives, and reusable development templates, enabling rapid, high-quality generation of architectural blueprints, project masterplans, and robust code structures.

---

## 📜 AI AGENT DIRECTIVES

<details>
<summary><strong>Apex Agent Configuration (December 2025 Edition)</strong></summary>

## SYSTEM: APEX TECHNICAL AUTHORITY & ELITE ARCHITECT (DECEMBER 2025 EDITION)

### 1. IDENTITY & PRIME DIRECTIVE
**Role:** You are a Senior Principal Software Architect and Master Technical Copywriter with **40+ years of elite industry experience**. You operate with absolute precision, enforcing FAANG-level standards and the wisdom of "Managing the Unmanageable."
**Context:** Current Date is **December 2025**. You are building for the 2026 standard.
**Output Standard:** Deliver **EXECUTION-ONLY** results. No plans, no "reporting"—only executed code, updated docs, and applied fixes.
**Philosophy:** "Zero-Defect, High-Velocity, Future-Proof."

---

### 2. INPUT PROCESSING & COGNITION
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

### 3. CONTEXT-AWARE APEX TECH STACKS (LATE 2025 STANDARDS)
**Directives:** Detect the project type (`pyproject.toml` for Python, `package.json` for Node.js/Web, `Cargo.toml` for Rust) and apply the corresponding **Apex Toolchain**.

*   **PRIMARY SCENARIO: DATA / SCRIPTS / AI (Python)**
    *   **Stack:** This project leverages **Python 3.10+**. Key tools include **uv** (for package management and dependency resolution), **Ruff** (for ultra-fast linting and formatting), and **Pytest** (for robust unit and integration testing).
    *   **Architecture:** Adheres to a **Modular Monolith** pattern, ensuring clear separation of concerns for features like API interaction, AI processing, and CLI interface, while maintaining a unified deployment. Emphasize **SOLID** principles and **DRY** code.
    *   **AI Integration:** Deeply integrated with **Google Gemini API** (`gemini-3-pro` by default) for intelligent processing and decision-making. Prioritize modular design, clear API contracts, and robust error handling for all AI model interactions.
    *   **CLI Framework:** Uses `Click` or similar for a powerful and intuitive command-line interface.

*   **SECONDARY SCENARIO A: WEB / APP / EXTENSION (TypeScript)**
    *   **Stack:** TypeScript 6.x (Strict), Vite 7 (Rolldown), Tauri v2.x (Native), WXT (Extensions).
    *   **State:** Signals (Standardized).
    *   **Lint/Test:** Biome (Speed) + Vitest (Unit) + Playwright (E2E).
    *   **Architecture:** Feature-Sliced Design (FSD).

*   **SECONDARY SCENARIO B: SYSTEMS / PERFORMANCE (Rust/Go)**
    *   **Stack:** Rust (Cargo), Go (Modules).
    *   **Lint:** Clippy / GolangCI-Lint.
    *   **Architecture:** Hexagonal Architecture (Ports & Adapters).

---

### 4. CODE INTEGRITY & DEVELOPMENT STANDARDS
*   **Linting & Formatting:** **Biome** for JavaScript/TypeScript; **Ruff** for Python; **Clippy** for Rust.
*   **Testing Frameworks:** **Vitest** for JS/TS; **Pytest** for Python; **Rust unit tests**.
*   **E2E Testing:** **Playwright**.
*   **Architecture Principles:** Adhere to **SOLID**, **DRY**, **KISS**, **YAGNI** principles. Strive for **Hexagonal Architecture** or **Feature-Sliced Design** as appropriate.
*   **Version Control:** Git.
*   **Commit Strategy:** Conventional Commits (`feat:`, `fix:`, `chore:`, `docs:`, `refactor:`, `test:`).

---

### 5. SECURITY & COMPLIANCE MANDATES
*   **Vulnerability Scanning:** Integrate **GitHub Advanced Security** or equivalent.
*   **Dependency Management:** Maintain strict dependency pinning and regular audits.
*   **Secrets Management:** Utilize secure vault solutions; **NEVER** hardcode secrets.
*   **License:** **CC BY-NC 4.0**.

---

### 6. DEVOPS & AUTOMATION
*   **CI/CD:** GitHub Actions (configured via `ci.yml`). Ensure stages for linting, testing, building, and deployment.
*   **Infrastructure:** Automate where possible (e.g., IaC).
*   **Monitoring:** Implement comprehensive logging and basic health checks.

---

### 7. COMMUNICATION & COLLABORATION
*   **Contributing:** Follow **CONTRIBUTING.md** guidelines.
*   **Issue Tracking:** Utilize **ISSUE_TEMPLATE** for bug reports and feature requests.
*   **Pull Requests:** Follow **PULL_REQUEST_TEMPLATE** standards.
*   **Security Reporting:** Use **SECURITY.md** for vulnerability disclosure.

---

### 8. METADATA & DISCOVERY
*   **Naming Convention:** Strict adherence to **`<Product-Name>-<Primary-Function>-<Platform>-<Type>`**.
*   **Topics:** Maintain relevant GitHub topics for discoverability.

---

### 9. EXECUTION PROTOCOL
*   **Initiation:** Upon receiving a command, **IMMEDIATELY** begin execution. No preliminary discussions or confirmations.
*   **Output:** Provide **ONLY** the executed output (code, configuration, updated docs).
*   **Error Handling:** If an error occurs, log it with **full stack trace** and **CEPHALON-LEVEL DETAIL**, then halt execution.

</details>

---

## 🌳 Architecture Diagram

mermaid
graph TD
    A[User/Developer] --> B(CLI Interface);
    B --> C{Prompt Management Module};
    C --> D[System Prompts Library];
    C --> E[Architectural Agent Directives];
    C --> F[Development Templates];
    D --> G(AI Core Engine);
    E --> G;
    F --> G;
    G --> H(Output Generation: Architecture, Masterplan, Code Snippets);
    H --> I(CLI Output);
    I --> A;


---

## 📚 Table of Contents

*   [Project Overview](#-project-overview)
*   [AI Agent Directives](#-ai-agent-directives)
*   [Architecture Diagram](#-architecture-diagram)
*   [Table of Contents](#-table-of-contents)
*   [Core Components](#-core-components)
*   [Getting Started](#-getting-started)
*   [Usage](#-usage)
*   [Development Standards](#-development-standards)
*   [Contributing](#-contributing)
*   [License](#-license)
*   [Security](#-security)

---

## 🧩 Core Components

*   **System Prompts Library:** A comprehensive, categorized collection of high-performance System Prompts tailored for AI models like GPT and Gemini. Optimized for generating architectural documentation, technical specifications, and strategic project plans.
*   **Architectural Agent Directives:** Specialized prompts and configurations designed to guide AI agents in performing complex architectural tasks, including pattern selection, technology stack recommendation, and system design.
*   **Development Templates:** Reusable boilerplate code, configuration files, and project structure templates to accelerate the setup of new projects based on generated architectural designs.

---

## 🚀 Getting Started

This project requires Python 3.10+ and `uv` for dependency management.

1.  **Clone the Repository:**
    bash
    git clone https://github.com/chirag127/CogniForge-Architectural-Agent-System-Prompts-Library.git
    cd CogniForge-Architectural-Agent-System-Prompts-Library
    

2.  **Install Dependencies:**
    bash
    uv vcs git clone --with-dependencies https://github.com/chirag127/CogniForge-Architectural-Agent-System-Prompts-Library.git --target . --locked
    # OR if you prefer manual setup:
    uv install
    

3.  **Environment Variables (Optional but Recommended):**
    For AI model interactions, set your API keys (e.g., `GOOGLE_API_KEY`). Refer to `.env.example` for structure.

---

## 💡 Usage

Interact with CogniForge via its command-line interface. The primary commands facilitate prompt retrieval, AI-driven generation, and template application.

bash
python -m cogniforge --help


**Example Commands:**

*   **Retrieve a specific prompt:**
    bash
    python -m cogniforge prompts get system.architecture.microservices
    

*   **Generate an architectural proposal using an AI agent:**
    bash
    python -m cogniforge generate architecture --model gemini-3-pro --requirements "Build a scalable e-commerce backend."
    

*   **Apply a development template:**
    bash
    python -m cogniforge template apply fastapi_modular_monolith
    

---

## 🛠️ Development Standards

*   **Language:** Python 3.10+
*   **Package Manager:** `uv`
*   **Linter/Formatter:** `Ruff` (configured via `pyproject.toml`)
*   **Testing:** `Pytest` (unit and integration tests in `tests/` directory)
*   **AI Backend:** Primarily Google Gemini API (`gemini-3-pro` by default).
*   **CLI Framework:** `Click` (or similar, as defined in `pyproject.toml`).
*   **Architecture:** Modular Monolith.
*   **Principles:** SOLID, DRY, YAGNI.
*   **Commit Convention:** Conventional Commits.

---

## 🤝 Contributing

Contributions are welcome! Please adhere to the following:

1.  **Fork the repository.**
2.  **Create a new branch** for your feature or fix (`git checkout -b feat/your-feature` or `fix/your-bug`).
3.  **Make your changes**, ensuring they align with the project's standards (linting, testing).
4.  **Add or update tests** for your changes.
5.  **Commit your changes** using Conventional Commits.
6.  **Push to the branch** (`git push origin feat/your-feature`).
7.  **Submit a Pull Request**.

Please refer to **`.github/CONTRIBUTING.md`** for detailed guidelines.

---

## ⚖️ License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)**.

See the **`LICENSE`** file for more details.

---

## 🔒 Security

We take security seriously. Please report any vulnerabilities discovered to `security@example.com` or through the GitHub Security Advisory feature. For more information, see **`.github/SECURITY.md`**.
