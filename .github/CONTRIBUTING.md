# Contributing to CogniForge-Architectural-Agent-System-Prompts-Library

Thank you for considering contributing to the `CogniForge-Architectural-Agent-System-Prompts-Library` repository! We welcome contributions that enhance the quality, scope, and utility of our AI system prompts and architectural agent directives.

## 1. Code of Conduct

This project adheres to the Contributor Covenant Code of Conduct. Please review the [CODE_OF_CONDUCT.md](https://github.com/chirag127/CogniForge-Architectural-Agent-System-Prompts-Library/blob/main/CODE_OF_CONDUCT.md) file for details on expected behavior.

## 2. How to Contribute

We support the following contribution methods:

*   **Reporting Bugs:** If you find a bug, please open an issue. Provide a clear and concise description, steps to reproduce, and expected vs. actual results.
*   **Suggesting Enhancements:** To suggest a new prompt category, architectural pattern, or agent directive, please open an issue. Describe the enhancement and its potential benefits.
*   **Submitting Pull Requests (PRs):** For code or prompt contributions:
    1.  **Fork the repository.**
    2.  **Create a new branch** for your feature or fix.
    3.  **Make your changes.** Ensure they align with the project's architectural principles and the 'Apex Technical Authority' standards.
    4.  **Test your changes.** If applicable, add new tests or ensure existing ones pass.
    5.  **Update documentation** if your changes affect it (e.g., add new prompt usage examples).
    6.  **Submit a PR** to the `main` branch.

## 3. Contribution Guidelines

### 3.1. Prompt Quality & Structure

*   **Clarity and Specificity:** Prompts should be unambiguous and guide the AI towards a precise output.
*   **Context:** Provide sufficient context for the AI to understand the task.
*   **Role Definition:** Clearly define the AI agent's role, persona, and objectives.
*   **Structure:** Utilize Markdown formatting for readability (headings, lists, code blocks).
*   **Categorization:** Ensure new prompts are placed in the most appropriate existing category or suggest a new one.

### 3.2. Architectural Standards

This project operates under the `Apex Technical Authority` principles. Contributions should reflect:

*   **Zero-Defect:** Aim for high-quality, well-tested contributions.
*   **High-Velocity:** Keep PRs focused and concise for rapid integration.
*   **Future-Proof:** Consider scalability and maintainability.

### 3.3. Testing

While this repository primarily stores prompts and templates, any executable code (e.g., utility scripts) must be accompanied by appropriate tests (Pytest). The prompt quality itself is validated through rigorous review and iterative refinement.

### 3.4. Development Environment

*   **Python:** Ensure your local environment uses Python 3.10+.
*   **Package Management:** Use `uv` for installing dependencies (`uv pip install -r requirements.txt`).
*   **Linting/Formatting:** Use `Ruff` to ensure code adheres to standards (`ruff check .` and `ruff format .`).

## 4. Pull Request Process

*   **Descriptive Title:** Clearly state the purpose of the PR.
*   **Detailed Description:** Explain the problem, your solution, and any impact on existing functionality.
*   **Link to Issue:** Reference any related issues using `#issue-number`.
*   **Self-Review:** Before submitting, review your own PR against these guidelines.
*   **CI/CD:** Ensure all automated checks (linting, testing) pass.

## 5. Repository Structure

*   **Prompts:** Categorized Markdown files containing system prompts.
*   **Templates:** Directory for reusable templates (e.g., architectural blueprints, agent directives).
*   **Utilities:** Executable Python scripts for managing or analyzing prompts (if any).

## 6. Communication

*   **GitHub Issues:** Primary channel for bug reports, feature requests, and discussions.
*   **GitHub Discussions:** For broader conversations about AI agent architecture and prompt engineering best practices.

We look forward to your contributions!

---*

*This `CONTRIBUTING.md` is dynamically generated and maintained by the `Apex Technical Authority`. Adherence to these guidelines ensures the highest standard of quality and velocity for the `CogniForge-Architectural-Agent-System-Prompts-Library`.*