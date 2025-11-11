# Usage Guide

> Comprehensive guide for using prompt templates in this repository

## Table of Contents

- [Introduction](#introduction)
- [General Purpose Prompts](#general-purpose-prompts)
- [Project-Specific Prompts](#project-specific-prompts)
- [Utility Prompts](#utility-prompts)
- [MCP Configurations](#mcp-configurations)
- [Best Practices](#best-practices)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)

## Introduction

This guide provides detailed instructions for using the various prompt templates in this repository. Each section covers a specific category of prompts with practical examples and implementation guidelines.

### Template Structure

Most templates follow this general structure:

```markdown
# Template Title
[Description of purpose]

## Instructions
[How to use the template]

## Parameters
[Customizable parameters]

## Output Format
[Expected output structure]

## Examples
[Usage examples]
```

## General Purpose Prompts

Located in the `prompts/` directory, these templates are designed for broad applicability across different projects.

### AI_CTO.md - Technical Architecture & Masterplan Generation

**Purpose**: Generate comprehensive technical masterplans for any product idea.

**When to Use**:

- Starting a new project and need architecture guidance
- Creating technical specifications for development teams
- Planning scalability and infrastructure requirements
- Documenting system architecture

**How to Use**:

1. **Prepare Your Idea**:

   ```
   RAW_IDEA: "Build a browser extension that categorizes bookmarks using AI"
   ```

2. **Provide Context** (optional):

   ```
   CONTEXT: Target users are developers, open-source project, Chrome only
   ```

3. **Answer Clarifying Questions**:
   The prompt will ask about:
   - Target users and personas
   - Platform preferences (web, mobile, CLI, etc.)
   - Technology stack preferences
   - Architecture patterns
   - Authentication requirements
   - Deployment preferences

4. **Generate the Masterplan**:
   - Answer the questions or type "continue" to use defaults
   - Receive a complete `masterplan.md` document

**Output**: A comprehensive masterplan including:

- Executive summary
- Technical stack recommendations
- Functional and non-functional requirements
- API endpoints and data models
- Implementation timeline
- Project structure
- Testing and deployment strategy

**Example Usage**:

```markdown
Input: "Create a Chrome extension for bookmark organization using Google Gemini API"
Output: Complete masterplan with architecture, tech stack, API integration, etc.
```

### common.md - Shared Prompt Patterns

**Purpose**: Reusable prompt components and patterns.

**When to Use**:

- Building custom prompts
- Need consistent formatting across prompts
- Standardizing AI responses

**Components**:

- Response format templates
- Error handling patterns
- Output structure guidelines
- Common instruction sets

### gemini.md - Google Gemini API Integration

**Purpose**: Templates for interacting with Google Gemini API.

**When to Use**:

- Integrating Gemini API into applications
- Building Gemini-powered features
- Testing Gemini API capabilities

**Key Features**:

- API authentication patterns
- Request/response formatting
- Error handling strategies
- Rate limiting guidance

**Example Configuration**:

```javascript
const { GoogleGenAI } = require("@google/genai");
const ai = new GoogleGenAI({ apiKey: YOUR_API_KEY });

const config = {
  thinkingConfig: { thinkingBudget: 0 },
  responseMimeType: "text/plain"
};

const model = "gemini-2.5-flash-preview-04-17";
```

### reactnative.md - React Native Development

**Purpose**: Templates for React Native mobile application development.

**When to Use**:

- Building cross-platform mobile apps
- Setting up React Native projects
- Implementing mobile-specific features

**Covered Topics**:

- Project initialization
- Component structure
- Navigation setup
- API integration
- Platform-specific code

### sprint.md - Agile Sprint Planning

**Purpose**: Guide sprint planning and execution.

**When to Use**:

- Planning sprint cycles
- Breaking down user stories
- Estimating development effort
- Tracking sprint progress

**Structure**:

- Sprint goal definition
- User story templates
- Acceptance criteria formats
- Sprint retrospective guides

### permanent message.md - Persistent AI Instructions

**Purpose**: Define persistent behavior for AI assistants.

**When to Use**:

- Setting up long-term AI assistant behavior
- Defining coding standards
- Establishing communication protocols
- Creating custom AI personas

**Example**:

```markdown
- Always follow GitHub username: chirag127
- Use industry-standard best practices
- Perform web search when needed
- Complete projects A to Z
- No TODO notes or placeholders
```

## Project-Specific Prompts

Located in the `specific/` directory, these templates are tailored for particular applications.

### Browser Extension Prompts

#### aireply.md - AI Reply Extension

**Purpose**: Building AI-powered reply generation for web forms and social media.

**Use Cases**:

- Email composition assistance
- Social media comment generation
- Form auto-completion
- Context-aware text suggestions

#### yt summarizer browser extension.md

**Purpose**: YouTube video summarization extension development.

**Features**:

- Video transcript extraction
- AI-powered summarization
- Key points highlighting
- Time-stamped notes

#### webpage chat.md / webpage chater.md

**Purpose**: Chat interfaces for webpage content interaction.

**Capabilities**:

- Page content analysis
- Question-answering about page content
- Interactive documentation navigation
- Content search and retrieval

### PDF Tool Prompts

#### allpdftools.md / allpdf-python.md

**Purpose**: Comprehensive PDF manipulation tools.

**Features**:

- PDF merging and splitting
- Compression and optimization
- Conversion (PDF to images, Word, etc.)
- Text extraction and OCR
- Form filling and signing

**Tech Stack Variations**:

- **allpdftools.md**: JavaScript/TypeScript implementation
- **allpdf-python.md**: Python-based implementation

### QR Code Application Prompts

#### qrcode.md / qrsayapp.md

**Purpose**: QR code generation and management applications.

**Features**:

- QR code generation with customization
- Batch QR code creation
- QR code scanning
- Analytics and tracking
- Dynamic QR codes

### VS Code Extension Prompts

#### vscode.md

**Purpose**: VS Code extension development guidance.

**Covered Areas**:

- Extension API usage
- Command registration
- Settings and configuration
- WebView implementation
- Language server integration

### Context Management Tools

#### Historical Context Tool.md

**Purpose**: Managing and tracking project context across sessions.

**Features**:

- Context persistence
- Session history tracking
- Decision documentation
- Knowledge base building

#### contextual sidebar.md

**Purpose**: Building intelligent sidebar interfaces.

**Use Cases**:

- Context-aware suggestions
- Dynamic navigation
- Real-time information display
- Tool integration panels

### Development Workflow Prompts

#### commit.md

**Purpose**: Generating meaningful git commit messages.

**Structure**:

```
type(scope): subject

body

footer
```

**Types**: feat, fix, docs, style, refactor, test, chore

#### download file mcp.md

**Purpose**: MCP server for file download capabilities.

**Use Cases**:

- Automated file retrieval
- Resource downloading
- Asset management

## Utility Prompts

Located in the `other/` directory, these provide helper functionality.

### aug.md - General Augmentation Guidelines

**Purpose**: Universal development guidelines and best practices.

**Key Principles**:

- No placeholders or TODO notes
- Complete A-to-Z implementation
- Industry-standard practices
- Comprehensive documentation
- Web search for unknowns
- GitHub username: chirag127

**Usage**: Include as a foundation for any development prompt to ensure quality and completeness.

### grammarly.md

**Purpose**: Grammar checking and writing improvement prompts.

**Use Cases**:

- Code comment refinement
- Documentation review
- README polishing
- Error message clarity

### Context & Quality Assurance

#### qcw.md / qsl.md

**Purpose**: Quality control and assurance workflows.

**Areas Covered**:

- Code review guidelines
- Testing strategies
- Quality metrics
- Performance benchmarks

## MCP Configurations

Located in the `mcp/` directory, these configure Model Context Protocol servers.

### main.md - MCP Server Configurations

**Purpose**: Configure various MCP servers for enhanced AI capabilities.

**Available Servers**:

#### 1. Pieces MCP

```json
{
  "mcpServers": {
    "pieces mcp": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "mcp-remote",
        "http://localhost:39300/model_context_protocol/2024-11-05/sse"]
    }
  }
}
```

**Purpose**: Code snippet management and reuse

#### 2. Context7 MCP

```json
{
  "mcpServers": {
    "context7": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

**Purpose**: Context persistence and management

#### 3. Toolbox MCP (Smithery)

```json
{
  "mcpServers": {
    "toolbox": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@smithery/cli@latest", "run",
        "@smithery/toolbox", "--profile", "YOUR_PROFILE", "--key", "YOUR_KEY"]
    }
  }
}
```

**Purpose**: Multi-tool integration platform

#### 4. TypeScript SDK Docs MCP

```json
{
  "mcpServers": {
    "typescript-sdk Docs": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "mcp-remote",
        "https://gitmcp.io/modelcontextprotocol/typescript-sdk"]
    }
  }
}
```

**Purpose**: TypeScript SDK documentation access

#### 5. Date and Time MCP

```json
{
  "mcpServers": {
    "Date and Time": {
      "command": "node",
      "args": ["PATH_TO/date-and-time-mcp-server/dist/index.js"]
    }
  }
}
```

**Purpose**: Date/time utilities and scheduling

#### 6. Clear Thought MCP

```json
{
  "mcpServers": {
    "clear thought": {
      "command": "node",
      "args": ["PATH_TO/Clear-Thought-MCP-server/dist/index.js"]
    }
  }
}
```

**Purpose**: Enhanced reasoning and analysis

#### 7. URL Content Saver MCP

```json
{
  "mcpServers": {
    "URL Content Saver MCP Server": {
      "command": "node",
      "args": ["PATH_TO/URL-Content-Saver-MCP-Server/dist/index.js"]
    }
  }
}
```

**Purpose**: Web content archival and retrieval

### How to Use MCP Configs

1. **Install Required Dependencies**:

   ```bash
   npm install -g mcp-remote
   ```

2. **Update Configuration**:
   - Copy the desired server configuration
   - Replace placeholder paths/keys with actual values
   - Add to your AI tool's MCP configuration

3. **Test Connection**:
   - Restart your AI tool
   - Verify server connection in logs
   - Test server functionality

## Best Practices

### 1. Template Selection

**Choose the Right Template**:

- General task → Use `prompts/` directory
- Specific project → Check `specific/` directory
- Need guidelines → See `other/` directory
- Setting up MCP → Browse `mcp/` directory

### 2. Customization

**Adapt Templates to Your Needs**:

- Replace placeholders with actual values
- Adjust scope and detail level
- Add project-specific context
- Modify output formats as needed

**Example**:

```markdown
# Before
USER_NAME: [Your Name]

# After
USER_NAME: Chirag Singhal
```

### 3. Combining Templates

**Layer Multiple Templates**:

1. **Foundation**: Start with `other/aug.md` for base guidelines
2. **Architecture**: Add `prompts/AI_CTO.md` for structure
3. **Specifics**: Include relevant templates from `specific/`
4. **Enhancements**: Layer in MCP configurations

**Example Combination**:

```markdown
# Building a React Native App

1. Include: other/aug.md (base guidelines)
2. Include: prompts/reactnative.md (React Native specifics)
3. Include: specific/qrcode.md (if building QR feature)
4. Configure: mcp/main.md (for enhanced AI capabilities)
```

### 4. Version Control

**Track Your Customizations**:

- Keep original templates unchanged
- Create custom versions in a separate directory
- Document modifications in comments
- Use git branches for experiments

### 5. Documentation

**Document Your Usage**:

- Note which templates you used
- Record customization decisions
- Track results and effectiveness
- Share learnings with team

## Examples

### Example 1: Starting a New Browser Extension

**Goal**: Build a bookmark organizer Chrome extension using Gemini API

**Steps**:

1. **Use AI_CTO.md**:

   ```markdown
   RAW_IDEA: "Chrome extension that organizes bookmarks using Google Gemini API"
   CONTEXT: Open-source, free, minimal setup, front-end only
   ```

2. **Review Generated Masterplan**:
   - Check architecture recommendations
   - Verify tech stack (should suggest Chrome Extension APIs + Gemini)
   - Note project structure

3. **Apply Gemini Integration Template** (`prompts/gemini.md`):

   ```javascript
   // Use the Gemini API pattern
   const ai = new GoogleGenAI({ apiKey: userProvidedKey });
   const model = "gemini-2.5-flash-preview-04-17";
   ```

4. **Follow Development Guidelines** (`other/aug.md`):
   - Complete A-to-Z implementation
   - No placeholders
   - Full documentation
   - Production-ready code

5. **Configure Git** (`specific/commit.md`):

   ```bash
   git commit -m "feat(extension): Add bookmark categorization with Gemini AI"
   ```

### Example 2: Building a PDF Tool

**Goal**: Create a PDF manipulation web application

**Steps**:

1. **Generate Masterplan**:

   ```markdown
   Input to AI_CTO.md:
   RAW_IDEA: "Web app for PDF merging, splitting, compression, and conversion"
   Platform: Web application
   Stack: Next.js + TypeScript
   ```

2. **Use PDF Tool Template** (`specific/allpdftools.md`):
   - Review feature list (merge, split, compress, convert)
   - Check implementation patterns
   - Note library recommendations (pdf-lib, pdf.js)

3. **Structure Project**:

   ```
   pdf-tools/
   ├── src/
   │   ├── components/    # UI components
   │   ├── utils/         # PDF processing logic
   │   ├── api/           # API routes
   │   └── types/         # TypeScript definitions
   ├── public/
   └── tests/
   ```

4. **Implement Features**:
   - Follow patterns from template
   - Add error handling
   - Implement progress tracking
   - Test each feature

### Example 3: Setting Up MCP Servers

**Goal**: Configure AI assistant with enhanced capabilities

**Steps**:

1. **Choose Required MCP Servers**:
   - Context7: For context persistence
   - Clear Thought: For enhanced reasoning
   - URL Content Saver: For web research

2. **Install Dependencies**:

   ```bash
   npm install -g mcp-remote
   ```

3. **Configure Each Server** (from `mcp/main.md`):

   ```json
   {
     "mcpServers": {
       "context7": {
         "command": "cmd",
         "args": ["/c", "npx", "-y", "@upstash/context7-mcp@latest"]
       },
       "clear thought": {
         "command": "node",
         "args": ["D:/path/to/Clear-Thought-MCP-server/dist/index.js"]
       }
     }
   }
   ```

4. **Test Configuration**:
   - Restart AI tool
   - Verify server connections
   - Test capabilities

### Example 4: Sprint Planning

**Goal**: Plan a 2-week development sprint

**Steps**:

1. **Use Sprint Template** (`prompts/sprint.md`):

   ```markdown
   Sprint Goal: Implement user authentication and profile management
   Duration: 2 weeks
   Team: 3 developers
   ```

2. **Break Down User Stories**:

   ```markdown
   Story 1: As a user, I want to sign up with email/password
   - Acceptance Criteria:
     * Email validation
     * Password strength requirements
     * Confirmation email sent
   - Estimate: 5 points
   ```

3. **Plan Implementation**:
   - Day 1-3: Authentication backend
   - Day 4-6: Frontend forms
   - Day 7-8: Email integration
   - Day 9-10: Testing & bug fixes

4. **Track Progress**:
   - Daily standup notes
   - Blocker tracking
   - Sprint burndown

## Troubleshooting

### Common Issues

#### Issue 1: Template Not Producing Expected Results

**Symptoms**: AI output doesn't match template expectations

**Solutions**:

1. Check if all required parameters are provided
2. Verify template syntax is correct
3. Add more specific context
4. Try a different AI model
5. Review examples in the template

#### Issue 2: MCP Server Not Connecting

**Symptoms**: MCP server fails to initialize or connect

**Solutions**:

1. Verify paths are absolute and correct
2. Check if Node.js is installed and accessible
3. Ensure dependencies are installed (`npm install`)
4. Review server logs for errors
5. Test server independently before integration

#### Issue 3: Templates Too Generic

**Symptoms**: Generated output lacks specificity for your use case

**Solutions**:

1. Add detailed context to your input
2. Combine multiple templates
3. Provide examples of desired output
4. Include domain-specific terminology
5. Iterate and refine based on initial results

#### Issue 4: Conflicting Template Instructions

**Symptoms**: Templates have contradictory guidelines

**Solutions**:

1. Prioritize more specific templates over general ones
2. Create a custom template combining best parts
3. Document resolution decisions
4. Test with small examples first
5. Seek clarification in repository issues

### Getting Help

If you encounter issues not covered here:

1. **Check Documentation**:
   - Review template comments
   - Read related templates
   - Check archive for historical context

2. **Search Repository**:
   - Look for similar use cases
   - Check closed issues
   - Review commit history

3. **Open an Issue**:
   - Describe the problem clearly
   - Include relevant template names
   - Provide input and expected output
   - Share actual results

4. **Community Support**:
   - Share experiences with other users
   - Contribute solutions back to repository

## Advanced Topics

### Creating Custom Templates

**When to Create a Custom Template**:

- Repeating similar prompts frequently
- Need project-specific standardization
- Want to share patterns with team

**How to Create**:

1. **Start with Existing Template**:
   - Copy closest matching template
   - Note its structure and patterns

2. **Define Clear Purpose**:

   ```markdown
   # Template Name
   Purpose: [One-line description]
   When to Use: [Specific scenarios]
   ```

3. **Structure Sections**:
   - Instructions
   - Parameters
   - Output format
   - Examples
   - Edge cases

4. **Test Thoroughly**:
   - Try with various inputs
   - Verify consistency
   - Check edge cases
   - Get feedback

5. **Document Well**:
   - Add inline comments
   - Provide examples
   - List limitations
   - Include troubleshooting

### Template Maintenance

**Keep Templates Updated**:

- Review regularly for accuracy
- Update with new best practices
- Add learnings from usage
- Archive obsolete versions

**Version Control**:

- Track major changes in CHANGELOG.md
- Use semantic versioning concepts
- Document breaking changes
- Provide migration guides

### Performance Optimization

**Optimize Template Performance**:

- Remove redundant instructions
- Focus on clear, concise language
- Provide structured parameters
- Use examples effectively
- Test with different AI models

**Monitor Results**:

- Track quality of outputs
- Measure time to completion
- Gather user feedback
- Iterate improvements

---

**Questions or Suggestions?** Open an issue or contribute to improve this guide!
