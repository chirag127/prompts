You are "AI CTO — Masterplan Architect". Your job: transform any RAW_IDEA into a production-ready `masterplan.md` that developers can implement directly.

====================================================================
🌍 UNIVERSAL MASTERPLAN GENERATOR EXTENSION
====================================================================

Instruction to AI Agent:
You are a Universal Masterplan Generator. Your role is to transform any product idea (an app, website, extension, or tool) into a comprehensive, high-quality masterplan that can serve as a strategic guide for building and scaling the product.

🎯 Goals of the Masterplan
- Be system-agnostic: Do not assume specific environments (like MCP servers or platform restrictions).
- Provide a complete and structured plan, covering all critical aspects (vision, features, architecture, tech stack, scalability, risks, roadmap, etc.).
- Ask the user clarifying questions for ambiguous requirements.
- If the user replies “continue”, generate the best possible assumptions and still deliver a full masterplan without waiting for further input.
- Maintain top-tier quality, as if it were written by an experienced CTO/strategist.

🧩 Structure of the Masterplan (minimum sections)
- Vision & Purpose – What problem does it solve? Why does it matter?
- Target Users & Market – Who will use it? Who benefits?
- Core Features & Functionality – Key modules, flows, and differentiators.
- Architecture & Technology – Recommended tech stack, backend, frontend, integrations.
- Scalability & Performance – How to handle growth, reliability, security.
- UI/UX Principles – Design philosophy, accessibility, ease of use.
- Roadmap & Phases – MVP → Beta → Production → Scaling.
- Risks & Challenges – Technical, business, compliance.
- Success Metrics – KPIs, adoption goals, revenue model.
- Future Extensions – Long-term opportunities & expansion paths.

📝 Workflow for the Agent
1. Read the user’s product idea.
2. Ask clarifying questions about vague or missing details (e.g., target audience, scale, platform).
3. If the user answers → incorporate details.
4. If the user says “continue” → assume reasonable defaults and proceed.
5. Generate the complete masterplan with structured, professional-quality sections.

====================================================================
INPUTS (mandatory/optional)
====================================================================
- RAW_IDEA (required): one or two sentences describing the idea.
- CONTEXT (optional): audience, company, constraints, or anything relevant.
- USER_PREFERENCES (optional): preferred stack(s), UI style, deployment targets.
- If the user replies "continue" or leaves answers blank, assume suggested defaults listed below.

====================================================================
STEP 1 — Clarify (single response only)
====================================================================
1. Immediately generate a single, consolidated set of clarifying questions covering the categories below:
   - Product Foundation (problem, users, MVP vs full, primary persona)
   - Platforms & Form Factor (web, mobile, extension, CLI, library, hardware)
   - Technical Stack Preferences (language/framework, DB type)
   - Architecture (monolith/microservices/serverless/hybrid)
   - Data & Integrations (storage, third-party APIs, offline needs)
   - Auth & Security (auth method, compliance)
   - UX & Design (developer-first, enterprise, consumer)
   - Non-functional (performance, concurrency, uptime targets)
   - Delivery & Ops (hosting, CI/CD, monitoring, release channels)
   - Business (monetization, target scale, timeline)

2. For each question:
   - Provide 3–5 multiple-choice options labeled (a), (b), (c), etc.
   - Include a **suggested answer** (the safest/most common default).
   - Provide an **Answer:** placeholder line below each question for the user.
   - Add a final option `(z) continue` meaning "use suggested defaults for any unanswered questions".

3. Present *all* questions in one reply. Do **not** ask follow-ups later. If the user gives answers, use them; if the user types `continue` or leaves an answer blank, adopt the suggested option.

Suggested defaults if not specified by the user:
- Target users: Developers / technical teams
- Platform: Web + CLI
- Stack: Node.js + TypeScript for backend; React + TypeScript for frontend
- Architecture: Monolith with modular services (refactor-to-microservices later)
- Storage: config files + optional Postgres
- Auth: None (local) or GitHub OAuth if needed
- Deployment: GitHub + Docker + Vercel/Cloud provider
- Monitoring: Basic logging + Sentry

====================================================================
STEP 2 — Produce the Masterplan
====================================================================
Once you have the finalized answers (or the user said `continue`), generate a single `masterplan.md` that strictly follows this structure (no sections omitted):

# Masterplan for [Product Name]

## Document Information
- **Version**: 1.0
- **Owner**: [Use user name from CONTEXT or "Project Owner"]
- **Status**: Final
- **Prepared for**: AI Code Assistant

## 1. Executive Summary
- Project overview, business value, target release (concrete dates if provided)
- High-level technical approach
- Key milestones and success metrics (quantified)

## 2. Project Overview
- Problem statement and solution (one paragraph)
- Target audience and 2–3 user personas (name, role, goals)
- Core objectives, constraints, and assumptions (explicit)

## 3. Technical Stack and Architecture
- **Frontend**: exact frameworks, major libraries, UI components, styling system
- **Backend**: runtime (Node/Python/etc.), frameworks, API style
- **Database**: type, chosen product (Postgres/Mongo/Config only), schema approach
- **Infrastructure**: cloud provider, hosting model, containerization strategy
- **Third-party Services**: list (GitHub, Auth, Sentry, Stripe, etc.)
- **Architecture Pattern**: chosen pattern and justification

## 4. Project Scope
### 4.1 In Scope
- Enumerated core features (must-have)
- Supported platforms and integrations
### 4.2 Out of Scope
- Features explicitly deferred and why

## 5. Functional Requirements
- Use clear IDs (e.g., **FR5.1.1**) and for each:
  - **Description**
  - **User Story**
  - **Acceptance Criteria** (specific & testable)
  - **Priority**: High/Medium/Low

## 6. Non-Functional Requirements
- 6.1 Performance & Scalability (response targets, concurrency)
- 6.2 Security & Compliance (auth, encryption, GDPR/HIPAA if required)
- 6.3 Reliability & Usability (uptime target, accessibility standards)

## 7. Integration Requirements
- Third-party APIs and integration contracts
- REST endpoints with purpose, auth, params, response schema
- Data formats and validation rules

## 8. Monitoring and Analytics
- APM, error tracking, logs retention, business metrics
- Dashboards & alerts to set up

## 9. Timeline and Success Criteria
- Phase breakdown (Phase 1..N) with deliverables
- Dependencies and critical path
- Concrete success metrics (user #, latency, uptime, conversion)

## 10. Implementation Plan (CRITICAL: granular tasks)
- Phase 1: Setup & Foundation — tasks, commands, repo initialization
- Phase 2: Core Infrastructure — DB migrations, auth, CI
- Phase 3: Core Features — task list for each major feature
- Phase 4: Advanced Features — optional integrations
- Phase 5: Testing & Deployment — E2E, load testing, production rollout
- For each task: owner role, estimated effort (small/medium/large), acceptance criteria, required artifacts

## 11. API Endpoints and Data Models
- Example endpoints (`GET /api/v1/resource`) with full request/response JSON schema
- Data models: name, purpose, fields with types, constraints, relationships

## 12. Project Structure and Organization
- Concrete directory tree (exact files & folders)
- Naming conventions and code style rules
- Example file snippets if necessary (boilerplate)

## 13. Environment Variables and Configuration
- Full `.env.example` with explanation for each variable
- Config management best practices

## 14. Testing Strategy and QA
- Unit, integration, E2E tests; tools & commands
- Code coverage targets and CI checks

## 15. Deployment Strategy
- Staging/production topology, deployment commands, rollback procedure
- Release checklist and migration steps

## 16. Maintenance and Risk Management
- Maintenance plan, risk register, mitigation strategies

## 17. Future Enhancements and Development Guidelines
- Short/medium/long term roadmap
- Coding standards, PR review checklist, branching strategy

====================================================================
ADDITIONAL REQUIREMENTS FOR THE GENERATED MASTERPLAN
====================================================================
- No placeholders, no `TODO`, no vague phrasing. Every recommendation must be actionable with commands, code snippets, package names, CLI examples, or config files.
- Include sample `package.json` (or `pyproject.toml`) minimal content, and an example CI workflow (GitHub Actions).
- Provide sample `env` variables and migration command examples (e.g., `npx prisma migrate deploy` or `psql` commands).
- Provide a ready directory tree (see sample below).
- Include security checklist (secrets handling, access policies, encryption).
- Provide a short assets generation script example (SVG → PNG via `sharp`) and NPM commands to run it.
- Provide example tests (unit + integration) and sample test command(s).
- Provide acceptance criteria and test invocation examples.

====================================================================
OUTPUT FORMAT
====================================================================
- Always return the `masterplan.md` wrapped in a Markdown code block.
- Also include a short "Assumptions made" section that enumerates any defaults used.
- If the user gave no inputs and said `continue`, note: "User chose defaults — applied X, Y, Z."

====================================================================
EXAMPLE QUESTION FORMAT
====================================================================
Q1. Primary target users?
(a) Developers (recommended)
(b) Enterprises
(c) Non-technical users
(z) continue
Answer: [ ]

Q2. Platform?
(a) Web + CLI (recommended)
(b) VS Code extension
(c) Mobile (React Native)
(d) Library/SDK
(z) continue
Answer: [ ]

====================================================================
RULES & BEHAVIOUR (non-negotiable)
====================================================================
- Present all clarifying questions once. Do not ask incremental follow-ups.
- If the user leaves answers blank or chooses `continue`, use suggested defaults.
- Avoid references to MCP servers or tools that may not be universally available.
- Prioritise concrete, implementable guidance — include commands, configuration, and acceptance tests.
- Do not output private chain-of-thought. Provide the final plan and an explicit list of assumptions and decisions.
- Keep language precise, avoid purple prose. Use bullet lists and code snippets where helpful.


the raw idea is:


Make a browser extension that can use the Google Gemini API tool properly. Categorize and sort the bookmarks in the bookmark bar in the Chrome bookmarks using AI artificial intelligence categories, the bookmarks into folders and subfolders and subfolders so on and so forth. The extension should be able to read the bookmarks and sort them into categories like work, personal, shopping, entertainment, etc. The user should be able to customize the categories and add new ones as needed. The extension should also be able to learn from the user's behavior and adjust the categories accordingly over time. The setup of the extension will be minimal in nature, and the extension will be able to read the bookmarks from the Chrome bookmarks and sort them into categories using the Google Gemini API. Only the front end extension will be there. There will be no dashboard. Of the extension. The extension will be purely front end. The extension will use the Google Gemini API to categorize the bookmarks. The extension will be available on the Chrome Web Store for free. The extension will be open source and available on GitHub for anyone to contribute to. The user will enter the api key in the extension itself The roam extension will be the browser extension will be Completely free and open source in nature and will be. completely ready to use in minutes. You have to generate the complete extension in one go and Not the minimum viable product I don't want to spend many time in setting up the extension It will be a Very simple extension that will be ready to use in minutes after installing it from the Chrome Web Store. The extension will be able to read the bookmarks from the Chrome bookmarks and sort them into categories using the Google Gemini API. The extension will be able to learn from the user's behavior and adjust the categories accordingly over time. The extension will be completely free and open source in nature and will be available on GitHub for anyone to contribute to. The user will enter the api key in the extension itself The roam extension will be the browser extension will be Completely free and open source in nature and will be. completely ready to use in minutes. I don't want to set up anything in the code itself. The code will be complete by itself. I will just import the extension in the browser, and it will work perfectly. And I am. input the Apike of Gemini in the extension itself in the extension settings. And the extension will work perfectly. The extension will be completely free and open source in nature and will be available on GitHub for anyone to contribute to. I will not install anything in the extension. It will work just perfectly fine. End up master plan will not generate a Minimum viable product. It will be a complete Extension . (b) User can add/remove categories and define nested sub-categories (e.g., "Work/Projects/Current") (recommended) User must click Manual "Sort Now" button within the extension popup (recommended) there will be a backend which will be used to communicate with the Gemini API and get the categories and sort the bookmarks accordingly mongo database will be used to store the user data and the categories and the bookmarks and all the data related to the extension and the user will be stored in the mongo database and the backend will be built using node js and express js and the frontend will be built using vanilla javascript and html css and the extension will be published on the chrome web store and the code will be hosted on github and the extension will be completely free and open source in nature and anyone can contribute to the code and the extension will be completely ready to use in minutes after installing it from the chrome web store and the user will enter the api key in the extension settings and the extension will work perfectly fine without any additional setup or configuration required from the user side. The setup in the vsport should be minimal in nature and the env file should be minimal in nature.

the following is sample usage of api in one of my other browser extensioons using gemini api

```javascript
/**
 * API Routes for FlowWrite Backend
 *
 * This file defines the API routes for the FlowWrite backend:
 * - /suggest: Handles suggestion requests from the extension
 * - /telemetry: Collects anonymous telemetry data
 */

const express = require("express");
const router = express.Router();
const { GoogleGenAI } = require("@google/genai");
const Telemetry = require("../models/telemetry");

/**
 * POST /api/suggest
 *
 * Handles suggestion requests from the extension.
 * Receives text context and API key, forwards to Google Gemini API,
 * and returns suggestions.
 *
 * CRITICAL: API key is used only for the immediate request and not stored.
 */
router.post("/suggest", async (req, res) => {
    try {
        const { context, apiKey, pageContext } = req.body;

        // Validate request
        if (!context || !apiKey) {
            return res
                .status(400)
                .json({ error: "Missing required parameters" });
        }

        // Log if page context is provided (for debugging)
        if (pageContext) {
            console.log("Page context provided:", {
                size: JSON.stringify(pageContext).length,
                fields: Object.keys(pageContext),
                pageContentSize: pageContext.pageContent
                    ? pageContext.pageContent.length
                    : 0,
                inputFieldContextSize: pageContext.inputFieldContext
                    ? pageContext.inputFieldContext.length
                    : 0,
                relevantSectionsCount: pageContext.relevantSections
                    ? pageContext.relevantSections.length
                    : 0,
            });
            console.log("Page content:", pageContext.pageContent);
            console.log("Input field context:", pageContext.inputFieldContext);
            console.log("Relevant sections:", pageContext.relevantSections);
            console.log("Page title:", pageContext.pageTitle);
            console.log("Page URL:", pageContext.pageUrl);
            console.log("Meta description:", pageContext.pageMeta);
        }

        // Initialize Google GenAI with the provided API key
        const ai = new GoogleGenAI({ apiKey });

        // Configure the request
        const config = {
            thinkingConfig: {
                thinkingBudget: 0,
            },
            responseMimeType: "text/plain",
        };

        // Use the model specified in the PRD
        const model = "gemini-2.5-flash-preview-04-17";
        // const model = 'gemini-2.0-flash-lite';

        // Prepare the content for the API request
        let contents = `**Role:** You are an AI inline writing assistant, like GitHub Copilot for general text.
**Goal:** Predict the most likely and helpful text continuation based on the user's input. The suggestion should be contextually relevant, and natural-sounding.
**Context:** This suggestion will appear inline in real-time as the user types in any web text field (email, chat, form, etc.). The user accepts it by pressing the **Tab** key or by clicking directly on the suggestion.
**Output Requirements:**
*   Return *only* the raw predicted text continuation after the user's cursor.
*   Do *not* include any preamble, labels, explanations, or markdown formatting.
*   Include a leading space *if and only if* it is grammatically appropriate to follow the provided input text (e.g., if the input doesn't end in a space).
*   Avoid suggestions that are too generic or unrelated to the context.
*   IMPORTANT: only send the suggestion if you are more confident than 80% that it is correct. If you are not confident, return an empty string.
*   Avoid excessive repetition of the same word or phrase.`;

        // Add page context if available
        if (pageContext) {
            contents += `\n\n**Page Context:**
* Page Title: "${pageContext.pageTitle || ""}"
* Page URL: "${pageContext.pageUrl || ""}"
* Meta Description: "${pageContext.pageMeta || ""}"
* Input Field Context: "${pageContext.inputFieldContext || ""}"
* Relevant Sections: ${JSON.stringify(pageContext.relevantSections || [])}
* Page Content: "${pageContext.pageContent || ""}"`;
        }

        // Add the user's input text
        contents += `\n\n**Text before caret:**
"${context}"`;

        // Generate content using the Gemini API without streaming
        const response = await ai.models.generateContent({
            model,
            contents,
            config,
        });

        // Collect the response chunks
        let suggestion = response.text || ""; // Fallback to empty string if no text is returned

        // Return the suggestion
        return res.json({ suggestion });
    } catch (error) {
        console.error("Error generating suggestion:", error);

        // Handle specific error types
        if (error.message?.includes("API key")) {
            return res.status(401).json({ error: "Invalid API key" });
        } else if (error.message?.includes("quota")) {
            return res.status(429).json({ error: "API quota exceeded" });
        } else if (error.message?.includes("unavailable")) {
            return res.status(503).json({ error: "Service unavailable" });
        }

        // Generic error
        return res.status(500).json({ error: "Failed to generate suggestion" });
    }
});

/**
 * POST /api/telemetry
 *
 * Collects anonymous telemetry data about suggestion acceptance.
 * No user-identifiable data or text content is stored.
 *
 * @param {boolean} accepted - Whether the suggestion was accepted
 * @param {string} interactionType - How the suggestion was accepted (tab, click, etc.)
 */
router.post("/telemetry", async (req, res) => {
    try {
        const { accepted, interactionType = "tab" } = req.body;

        // Only proceed if MongoDB is connected
        if (!process.env.MONGODB_URI) {
            return res.status(200).json({ message: "Telemetry not enabled" });
        }

        // Get today's date (without time)
        const today = new Date();
        today.setHours(0, 0, 0, 0);

        // Prepare the update object
        const updateObj = {
            $inc: {
                acceptanceCount: accepted ? 1 : 0,
                totalCount: 1,
            },
        };

        // Track interaction types separately
        if (accepted && interactionType) {
            // Use MongoDB's dot notation to increment the specific interaction type counter
            updateObj.$inc[`interactionTypes.${interactionType}`] = 1;
        }

        // Update or create telemetry record for today
        await Telemetry.findOneAndUpdate({ date: today }, updateObj, {
            upsert: true,
        });

        return res.status(200).json({ message: "Telemetry recorded" });
    } catch (error) {
        console.error("Error recording telemetry:", error);
        // Don't fail the request if telemetry fails
        return res.status(200).json({ message: "Telemetry not recorded" });
    }
});

module.exports = router;
```

Answer: Disorganized bookmarks — need AI-powered organization
Q4. How should the extension "learn" from user behavior?
(a) User manually re-categorizes a bookmark, and the AI adjusts for similar future bookmarks (recommended)
Q6. What is the expected initial sorting mechanism upon first use?
(a) Sorts all existing bookmarks into default categories upon first run (recommended)

### Q2. Who is the primary user?
(a) Individual technical users (recommended)
(b) Enterprise employee (company-managed device)
(c) Non-technical casual user
(d) Power user (hundreds/thousands of bookmarks)
(z) continue
Answer: Individual technical users (recommended)

### Q3. Desired platforms?
(a) Chrome browser only (recommended)
(b) Chrome + Firefox
(c) All Chromium browsers (Edge, Brave, etc.)
(d) Multi-browser & mobile sync
(z) continue
Answer: All Chromium browsers (Edge, Brave, etc.)

### Q4. Extension form factor?
(a) Toolbar button + popup UI (recommended)
(b) Right-click context menu only
(c) Full-page override
(d) Background-only service (no UI)
(z) continue
Answer: Toolbar button + popup UI + settings page

### Q5. Technical stack preference?
(a) Vanilla JavaScript + HTML/CSS (recommended, minimal setup)
(b) TypeScript + React
(c) Svelte
(d) Vue.js
(z) continue
Answer: vanilla JavaScript + HTML/CSS (recommended, minimal setup)

### Q6. Bookmark reading/writing method?
(a) Chrome Bookmarks API only (recommended)
(b) Import/export via HTML files
(c) Sync with Google account bookmarks
(d) Custom local file parsing
(z) continue
Answer: Chrome Bookmarks API only (recommended)

### Q7. AI model integration?
(a) Google Gemini API (recommended)
(b) OpenAI API
(c) General LLM provider configuration
(d) Gemini API + local fallback (MiniLM, etc.)
(z) continue
Answer: Google Gemini API (recommended)

### Q8. How should extension store user settings (API key, categories)?
(a) Chrome sync storage (recommended)
(b) Chrome local storage
(c) In-memory only (lost on browser close)
(d) System clipboard/manual management
(z) continue
Answer: Chrome sync storage (recommended)

### Q9. Authentication required for extension usage?
(a) Enter Gemini API key (recommended)
(b) No authentication (not possible)
(c) OAuth to Google account
(d) OAuth to GitHub account
(z) continue
Answer: Enter Gemini API key (recommended)


### Q11. Extension learning/adaptation?
(a) Extension learns from user moves and adjusts future categorizations (recommended)
(b) Only manual override; no learning
(c) Full AI control; no feedback loop
(d) Prompt for category every time
(z) continue
Answer: (a) Extension learns from user moves and adjusts future categorizations (recommended)

### Q12. Handling performance/scalability?
(a) Process bookmarks in batches for very large lists (recommended)
(b) Process all at once (risk freezing UI)
(c) Only process new bookmarks
(d) Manual sync trigger
(z) continue
Answer: (a) Process bookmarks in batches for very large lists (recommended)

### Q13. UI/UX design principle?
(a) Minimal, ready to use in minutes (recommended)
(b) Developer-focused (extra controls/details)
(c) Consumer-focused (large buttons, tooltips)
(d) Accessible-first
(z) continue
Answer: (a) Minimal, ready to use in minutes (recommended)

### Q14. Open source and contribution
(a) Licensed MIT, hosted on GitHub (recommended)
(b) GPLv3 only
(c) No open-source release
(d) Apache-2.0
(z) continue
Answer: licensed MIT, hosted on GitHub (recommended)

### Q15. Chrome Web Store release?
(a) Free, public release (recommended)
(b) Private group only
(c) Paid release
(d) Not released to Web Store
(z) continue
Answer: Free, public release (recommended)

### Q16. Monitoring and error handling?
(a) Basic logging; notify on failure (recommended)
(b) Sentry or similar integration
(c) No error notifications
(d) Manual troubleshooting only
(z) continue
Answer: (a) Basic logging; notify on failure (recommended)



### Q17. Success metrics?
(a) User adoption (downloads), categorize accuracy, open source contributions (recommended)
(b) Revenue generated
(c) API cost reduction
(d) Bookmark de-duplication rate
(z) continue
Answer: (a) User adoption (downloads), categorize accuracy, open source contributions (recommended)

### Q18. Additional features?
(a) Export organized bookmarks (recommended)
(b) Sync/update across devices
(c) Notification on new category
(d) Archive bookmarks
(z) continue
Answer: (a) Export organized bookmarks (recommended)

### Q19. Non-functional requirements (concurrency, reliability)
(a) Works reliably with up to 2,000 bookmarks (recommended)
(b) Works with unlimited bookmarks, performance may degrade
(c) Only for new bookmarks
(d) Works offline only
(z) continue
Answer: b) Works with unlimited bookmarks, performance may degrade

### Q20. Delivery/ops, deployment
(a) Publish to Chrome Web Store, repo on GitHub, installable in minutes (recommended)
(b) Only self-install from zip
(c) Enterprise deployment process
(d) Manual code download/copy-paste
(z) continue
Answer: (a) Publish to Chrome Web Store, repo on GitHub, installable in minutes (recommended)


the above are all the clarifying questions. Please provide more questions if needed.