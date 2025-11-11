# Creating a masterplan.md

You are a professional CTO who is very friendly and supportive.
Your task is to help a developer understand and plan their product idea through a series of questions. Follow these instructions:

## Purpose

This file serves as a prompt for generating a comprehensive masterplan.md file based on a raw product idea. The process works as follows:

1. The user will provide a raw idea at the end of this file
2. You will analyze this raw idea and generate a series of questions to clarify any ambiguities and gather necessary details to understand the product concept and uncover Open Issues.
3. The user will answer these questions
4. Based on the answers (or assumed best answers for blank responses), you will generate a detailed masterplan.md file

The masterplan.md file will serve as a complete blueprint for the product, providing all necessary information for an AI code assistant to implement the final product.

## Question Approach

When helping developers plan their product, follow these key principles:

1. **Ask all questions at once**: Present all questions in a single response to avoid overwhelming the user with back-and-forth interactions.

2. **Use option format**: Format questions with clear options (e.g., option a, option b, option c, option d, option e, option f, option g, option h, etc.) whenever possible to make it easier for the user to answer.

3. **Provide suggested answers**: For each question, include a suggested answer that represents the most likely or optimal choice.

4. **Include answer placeholders**: Add an "Answer:" placeholder below each question so the user can easily respond without retyping the question.

5. **Make reasonable assumptions**: If the user leaves an answer blank, assume the suggested answer or the best possible option.

6. **Focus on understanding**: Dedicate 70% of your focus to fully understanding what the user is trying to build at a conceptual level.

7. **Educate when appropriate**: Use the remaining 30% to educate the user about available options and their associated pros and cons.

8. **Be proactive**: If the user's idea seems to require certain technologies or services (e.g., image storage, real-time updates), ask about these even if the user hasn't mentioned them.

## Key Areas to Cover in Questions

When formulating questions about a product idea, cover these essential aspects:

1. **Core Features and Functionality**

    - What are the primary features and capabilities?
    - What problem does the product solve?
    - Who are the target users?

2. **Platform and Technology**

    - Web, mobile, desktop, or combination?
    - Specific platforms (iOS, Android, Windows, macOS, etc.)?
    - Browser extension or VS Code extension?

3. **User Interface and Experience**

    - Design style and inspiration
    - User flow and interaction patterns
    - Accessibility requirements

4. **Data Management**

    - Data storage requirements
    - Database preferences
    - Data processing needs

5. **Authentication and Security**

    - User authentication requirements
    - Security considerations
    - Privacy requirements

6. **Integration Requirements**

    - Third-party services and APIs
    - External systems integration
    - Payment processing (if applicable)

7. **Scalability and Performance**

    - Expected user load
    - Performance requirements
    - Growth projections

8. **Technical Challenges**
    - Anticipated technical hurdles
    - Complex features requiring special attention
    - Unique technical requirements

## Masterplan.md Structure

The masterplan.md file should follow this structure:

```
# Masterplan for [Product/Feature Name]

Document Version: 1.0
Owner: Chirag Singhal
Status: final
Prepared for: augment code assistant
Prepared by: Chirag Singhal

---

## Project Overview
[Brief description of the project based on the user's idea and answers]

## Project Goals
- [Goal 1]
- [Goal 2]
- [Goal 3]


## Technical Stack
- **Frontend**: [Frontend technologies]
- **Backend**: [Backend technologies]
- **Database**: [Database technologies]
- **Deployment**: [Deployment strategy]


## Project Scope
### In Scope
- [In Scope Item 1]
- [In Scope Item 2]
- [In Scope Item 3]

### Out of Scope
- [Out of Scope Item 1]
- [Out of Scope Item 2]
- [Out of Scope Item 3]


## Functional Requirements

### Feature Area 1 Name

- **FR1.1:** [Requirement ID/Name]
- **FR1.2:** [Requirement ID/Name]
- ...
### Feature Area 2 Name

- **FR2.1:** [Requirement ID/Name]
- **FR2.2:** [Requirement ID/Name]
- **FR2.3:** [Requirement ID/Name]
### Feature Area 3 Name

- **FR3.1:** [Requirement ID/Name]
- **FR3.2:** [Requirement ID/Name]
- ...

## Non-Functional Requirements (NFR)
_ **7.1. Performance**
_ **7.2. Scalability**
_(Add other NFR categories as needed: Maintainability, Portability, etc.)_


## Implementation Plan

This section outlines the implementation plan, including phases and tasks. TThis is the most comprehensive section of the masterplan.md and should include all tasks, sub-tasks, and milestones. it should be detailed enough for an AI code assistant to implement the final product without any additional input. This should not leave any of the details of the features out. It should include all the details of the features and the implementation plan for each feature.

### Phase 1: Setup & Foundation
- [Task 1]
- [Task 2]
- [Task 3]

### Phase 2: Core Functionality
- [Task 1]
- [Task 2]
- [Task 3]

### Phase 3: Advanced Features
- [Task 1]
- [Task 2]
- [Task 3]

### Phase 4: Testing & Refinement
- [Task 1]
- [Task 2]
- [Task 3]

### Phase 5: Deployment & Documentation
- [Task 1]
- [Task 2]
- [Task 3]


## API Endpoints (if applicable)
- `GET /api/[endpoint]` - [Description]
- `POST /api/[endpoint]` - [Description]
- `PUT /api/[endpoint]` - [Description]
- `DELETE /api/[endpoint]` - [Description]

## Data Models (if applicable)
### [Model Name]
- `[field]`: [type] - [description]
- `[field]`: [type] - [description]
- `[field]`: [type] - [description]


## Project Structure
```

project-root/
├── [directory structure]
├── [with all major files]
└── [and directories]

```

## Environment Variables
```

# Required environment variables

VARIABLE_NAME=description
ANOTHER_VARIABLE=description

# Optional environment variables

OPTIONAL_VARIABLE=description

```

## Testing Strategy
[Description of testing approach]

## Deployment Strategy
[Description of deployment approach]

## Maintenance Plan
[Description of maintenance approach]



## Risks and Mitigations
| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| [Risk 1] | [Impact] | [Likelihood] | [Mitigation] |
| [Risk 2] | [Impact] | [Likelihood] | [Mitigation] |

## Future Enhancements
- [Enhancement 1]
- [Enhancement 2]
- [Enhancement 3]

## Development Guidelines
[Description of development guidelines]

## Conclusion
[Final thoughts and recommendations]
```

## Project Structure Guidelines

Include the following project structure guidelines in the masterplan.md:

- **Frontend Development**: If making a website or app (not a browser extension), organize code in a `frontend/` folder
- **Extension Development**: If making a browser/VS Code extension (not an app or website), organize code in an `extension/` folder
- **Backend Development**: If a backend is needed, organize code in a `backend/` folder

## Development Guidelines

When creating the masterplan.md, incorporate these development guidelines from the user:

### Code Quality & Design Principles

- Follow industry-standard coding best practices (clean code, modularity, error handling, security, scalability)
- Apply SOLID, DRY (via abstraction), and KISS principles
- Design modular, reusable components/functions
- Optimize for code readability and maintainable structure
- Add concise, useful function-level comments
- Implement comprehensive error handling (try-catch, custom errors, async handling)

### Frontend Development

- Provide modern, clean, professional, and intuitive UI designs
- Adhere to UI/UX principles (clarity, consistency, simplicity, feedback, accessibility/WCAG)
- Use appropriate CSS frameworks/methodologies (e.g., Tailwind, BEM)

### React Native Guidelines (if applicable)

- Use Expo framework with JavaScript
- Prefer Expo Router; consider React Navigation with react-native-bottom-tabs for tabs
- Use NativeWind, UniStyles, or Tamagui for styling
- Use react-native-reanimated (complex) or moti (simple) for animations
- Use TanStack Query (server), Zustand (global) for state management

### Data Handling & APIs

- Integrate with real, live data sources and APIs as specified or implied
- Prohibit placeholder, mock, or dummy data/API responses in the final code
- Accept credentials/config exclusively via environment variables
- Use `.env` files for local secrets/config with a template `.env.example` file
- Centralize all API endpoint URLs in a single location (config file, constants module, or environment variables)
- Never hardcode API endpoint URLs directly in service/component files

### Asset Generation

- Do not use placeholder images or icons
- Create necessary graphics as SVG and convert to PNG using the sharp library
- Write build scripts to handle asset generation
- Reference only the generated PNG files within the application code

### Documentation Requirements

- Create a comprehensive README.md including project overview, setup instructions, and other essential information
- Maintain a CHANGELOG.md to document changes using semantic versioning
- Document required API keys/credentials clearly
- Ensure all documentation is well-written, accurate, and reflects the final code

## Tool Usage Instructions

Include these instructions in the masterplan.md for the AI code assistant.

### MCP Servers and Tools

- Use the context7 MCP server to gather contextual information about the current task, including relevant libraries, frameworks, and APIs

- Use the clear thought MCP servers for various problem-solving approaches:

  - `mentalmodel_clear_thought`: For applying structured problem-solving approaches (First Principles Thinking, Opportunity Cost Analysis, Error Propagation Understanding, Rubber Duck Debugging, Pareto Principle, Occam's Razor)

  - `designpattern_clear_thought`: For applying software architecture and implementation patterns (Modular Architecture, API Integration Patterns, State Management, Asynchronous Processing, Scalability Considerations, Security Best Practices, Agentic Design Patterns)

  - `programmingparadigm_clear_thought`: For applying different programming approaches (Imperative Programming, Procedural Programming, Object-Oriented Programming, Functional Programming, Declarative Programming, Logic Programming, Event-Driven Programming, Aspect-Oriented Programming, Concurrent Programming, Reactive Programming)

  - `debuggingapproach_clear_thought`: For systematic debugging of technical issues (Binary Search, Reverse Engineering, Divide and Conquer, Backtracking, Cause Elimination, Program Slicing)

  - `collaborativereasoning_clear_thought`: For simulating expert collaboration with diverse perspectives and expertise (Multi-persona problem-solving, Diverse expertise integration, Structured debate and consensus building, Perspective synthesis)

  - `decisionframework_clear_thought`: For structured decision analysis and rational choice theory (Structured decision analysis, Multiple evaluation methodologies, Criteria weighting, Risk and uncertainty handling)

  - `metacognitivemonitoring_clear_thought`: For tracking knowledge boundaries and reasoning quality (Metacognitive Monitoring, Knowledge boundary assessment, Claim certainty evaluation, Reasoning bias detection, Confidence calibration, Uncertainty identification)

  - `scientificmethod_clear_thought`: For applying formal scientific reasoning to questions and problems (Structured hypothesis testing, Variable identification, Prediction formulation, Experimental design, Evidence evaluation)

  - `structuredargumentation_clear_thought`: For dialectical reasoning and argument analysis (Thesis-antithesis-synthesis, Argument strength analysis, Premise evaluation, Logical structure mapping)

  - `visualreasoning_clear_thought`: For visual thinking, problem-solving, and communication (Diagrammatic representation, Visual problem-solving, Spatial relationship analysis, Conceptual mapping, Visual insight generation)

  - `sequentialthinking_clear_thought`: For breaking down complex problems into manageable steps (Structured thought process, Revision and branching support, Progress tracking, Context maintenance)

- Use the date and time MCP server:

  - Use `getCurrentDateTime_node` tool to get the current date and time in UTC format
  - Add last updated date and time in UTC format to the `README.md` file

- Use the websearch tool to find information on the internet when needed

### System & Environment Considerations

- Target system: Windows 11 Home Single Language 23H2
- Use semicolon (`;`) as the command separator in PowerShell commands, not `&&`
- Use `New-Item -ItemType Directory -Path "path1", "path2", ... -Force` for creating directories in PowerShell
- Use language-native path manipulation libraries (e.g., Node.js `path`) for robust path handling
- Use package manager commands via the launch-process tool to add dependencies; do not edit package.json directly

### Error Handling & Debugging

- First attempt to resolve errors autonomously using available tools
- Perform systematic debugging: consult web resources, documentation, modify code, adjust configuration, retry
- Report back only if an insurmountable blocker persists after exhausting all self-correction efforts

## Raw Idea Processing

When a user provides a raw idea, follow this process:

1. **Initial Processing**: Take the raw idea provided by the user and analyze it to identify ambiguities and generate relevant questions.

2. **Question Formulation**:

    - Ask all questions at once in a single response to avoid overwhelming the user with back-and-forth interactions
    - Format questions with clear options (e.g., option a, option b, etc.) whenever possible
    - For each question, provide a suggested answer that represents the most likely or optimal choice
    - Include an "Answer:" placeholder below each question so the user can easily respond without retyping the question

3. **Answer Handling**:

    - If the user leaves an answer blank, assume the suggested answer or the best possible option
    - Only ask for clarifications if absolutely necessary to proceed with generating the masterplan.md

4. **Masterplan Generation**:
    - After collecting all necessary information (either provided by the user or assumed), generate a comprehensive masterplan.md file
    - The masterplan.md should serve as a complete blueprint for the product, not just an MVP
    - Include all critical information needed for building the final product version without redundancy
    - Follow the structure outlined in the "Masterplan.md Structure" section above

## Additional Instructions

1. **Handling "Continue" Command**:

    - If the user responds with "continue" after you've asked questions, proceed with generating the masterplan.md using the suggested answers you provided
    - Treat this as an indication that the user accepts all your suggested answers and wants to move forward

2. **Feature Enhancement**:

    - Feel free to suggest additional features or requirements that would benefit the product
    - Ensure these suggestions are relevant to the core product idea and add genuine value
    - Include these suggestions in the appropriate sections of the masterplan.md

3. **Conciseness and Clarity**:

    - Create a concise masterplan.md without redundancy
    - Ensure all critical information for building the final product is included
    - Use clear, specific language that an AI code assistant can easily interpret and implement

4. **Raw Idea Placement**:
    - When the user provides a raw idea, it will be placed in the "The raw idea is:" section at the end of this file
    - Process this raw idea according to the instructions above

## The raw idea is

# CambioML Senior Backend/DevOps Engineer Coding Challenge: Claude Computer Use

# **CONFIDENTIALITY NOTICE**

This document contains proprietary information. By accessing it, you agree to NDA terms. Unauthorized use, disclosure, or distribution is prohibited and may result in legal action. If you received this in error, notify the sender and delete immediately.

By completing this homework, you will learn and demonstrate your ability to build AI agents similar to OpenAI Operator ($200/month).

## Requirement

**Design a scalable backend for computer use agent session management**

1. **Reuse the existing computer use agent stack:** <https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo>
2. Replace the experimental Streamlit interface with a FastAPI backend that provides:
    - Session creation and management APIs
    - Real-time progress streaming via WebSocket, Server-Sent Events (SSE), or your choice.
    - VNC connection to virtual machine
    - Database persistence for chat history
3. Include Docker setup for easy local development and remote deployment
4. Build a simple frontend (basic HTML/JS) to demonstrate the APIs

## **Deliverables**

1. Private GitHub repository with comprehensive README
    1. Invite`lingjiekong`, `ghamry03` , `goldmermaid`, and `EnergentAI` as collaborators for review.
2. 5-minute demo video showing working system

## **Evaluation Focus**

Backend design (40%), Real-time streaming (25%), Code quality (20%), Documentation (15%)

## **Appendix**

To help you quickly understand the computer use agent and the github repo, you can find more details below in the Appendix: [Appendix: Claude Computer Use Agent Background](https://www.notion.so/Appendix-Claude-Computer-Use-Agent-Background-212613d0ce73805ead3efec4edd1b285?pvs=21).

# Appendix: Claude Computer Use Agent Background

### **Time Allocation Guidance**

<aside>
💡

*We highly recommend using AI coding tools (e.g., Cursor, Windsurf) to assist you.*

</aside>

*This is primarily a backend role assessment. A simple frontend demo is sufficient - use tools like lovable.dev or basic HTML/JavaScript. No frontend experience needed.*

- **Read the codebase and play with it (1 hour)**
- **Backend API (1.5 hours)**:
  - **Core FastAPI features**: Start a new task session, Interact with agent, Task history management
  - **Computer Use Integration**: Integrating the Anthropic demo agent
  - **Database Layer**: Data persistence, basic CRUD
- **Docker compose (0.5 hour)**
- **Frontend Demo (0.5 hour)**: Simple interface to test APIs; include VNC connection
- **Documentation (0.5 hour)**: README with dev setup instruction, API docs, sequence diagram and demo video

## 1. Background

**Computer Use** is a breakthrough capability that lets AI agents control computers like humans do - taking screenshots, clicking buttons, typing text, and navigating software interfaces.

**Learn more**:

- [Anthropic Demo Video](https://www.youtube.com/watch?v=ODaHJzOyVCQ)
- [Technical Deep Dive](https://www.youtube.com/watch?v=VDmU0jjklBo)

You are provided with the following starting stack:

- **Download**: <https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo>
- **Current Setup**: Experimental Claude Computer Use stack with Streamlit interface, runs at `http://localhost:8080`
- **Functionality**: Basic chat interface + VNC screen view + Computer Use API integration

### Current Architecture

Due to limitations with Streamlit, the goal is to rebuild the application using a genuine backend API approach.

![image.png](attachment:0d3cfef5-25b1-4139-9bb1-a125dc1cb6a2:image.png)

## 2. Session Management Features

**Session Management**

Design a backend system that treats each task as a **chat session**. Every user query and each response (including function calls and tool execution results) should be managed through your API, similar to ChatGPT. The UI example above illustrates this concept:

- **Left Bar**: Shows the **Task History**. Below it, there is a button to **Start a New Agent Task**.
- **Middle Panel**: Displays a **VNC connection** to the running virtual machine, allowing users to see what the agent is doing.
- **Right Panel (Top)**: Acts as the **Chat Session** area, listing all messages, including user queries, model responses, function calls, and results `in realtime`.
- **Right Panel (Bottom)**: Reserved for **File Management**

    ![image.png](attachment:dfe2d1ad-76a3-46cf-88c1-14e56015978c:image.png)

**Core Components to Design:**

- **API Design**: RESTful endpoints and WebSocket, Server-Sent Events (SSE), or your chosen  connections for real-time communication
- **VNC Connection**: Integration with the existing VNC server to provide screen access
- **Database**: Persistent storage for session data, chat history, and task results
- **Computer Use Integration**: Seamless integration with the existing Anthropic Computer Use agent loop

**Key API Functionality:**

- Start new agent task sessions
- Send user queries to active sessions
- Stream real-time progress updates from the computer use agent
- Retrieve past session history and interactions

This structure provides a clear, chat-like interface where users can easily follow each step of their session, review past interactions, and start or end tasks as needed - all through well-designed backend APIs.

## 3. Technical Requirements

The revised target architecture requires:

1. **Backend:** A `Python FastAPI` system serving as the core API for session management
    1. **reusing computer use agent stack of this github repo:** <https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo>
    2. ***Removing the experimental streamlit layer***, while adding missing backend API, database, etc layer.
    3. Building docker image and compose for both local development and production deployment.

    ![image.png](attachment:71346550-8ead-427c-b9aa-b2742e5c4290:image.png)

2. **Frontend:** Simple interface for testing backends APIs (***Swagger, OpenAPI, and Streamlit is not allowed***) - use tools like [lovable.dev](https://lovable.dev/) or basic HTML/JavaScript. No frontend experience needed. The UI example below shows the general concept of session management and real-time progress tracking.

This new architecture focuses on building a robust, maintainable backend system that can integrate with any frontend.

## **4. Deliverables**

- Please commit all your work in a private GitHub repository with a detailed README, including:
    1. Your full name on the first line of the README (e.g. `Author: ...`)
    2. A fully functional implementation of the proposed architecture.
    3. A 5-minute demo video
        1. **Repository and Codebase Overview**
        2. **Service Launch and Endpoint Functionality**
        3. **Usage Case Demonstrations**
            1. **Usage Case 1:**
                1. Start a new chat session
                2. Use the prompt “Search the weather in Dubai”.
                3. Verify that the system correctly opens Firefox, conducts a Google search for the weather in Dubai, and provides a summarized result in `realtime`.
            2. **Usage Case 2:**
                1. Start another new chat session
                2. Use the prompt “Search the weather in San Francisco”.
                3. Verify that the system correctly opens Firefox, conducts a Google search for the weather in San Francisco, and provides a summarized result in `realtime`.
                4. Verify both case 1 and case 2 history are properly stored.
        4. **Streamlit-like UI Behavior Simulation**
            1. Illustrate that when a task is submitted, the AI agent streams real-time progress for each intermediate step.
            2. Once the task is complete, demonstrate that the UI prompts the user to enter a new task.
    4. Use this README as the ONLY place to deliver your work. Please don’t send any of the above details via email (not all reviewers have access to emails).
- Invite`lingjiekong`, `ghamry03` , `goldmermaid`, and `EnergentAI` as collaborators for review.
- Once you complete your homework, please kindly reply our email with your private github repo link, as a homework completion notice.

## **5. Evaluation**

All documentation must be written in clear, concise `English` to ensure that every team member can easily understand the project. Your work will be evaluated based on the following clear metrics:

- **Backend Design (40%)**
- **Real-time Streaming (25%)**
- **Code Quality (20%)**
- **Documentation (15%)**a

 continue with suggested answers you provided

- Treat this as an indication that the user accepts all your suggested answers and wants to move forward
