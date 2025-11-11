# Browser Extension Masterplan Template

"""
Browser Extension Masterplan Template

Purpose:
    Specialized template for generating comprehensive masterplans for browser extensions
    (Chrome, Firefox, Edge, etc.). Covers extension-specific requirements like content
    scripts, background workers, popup interfaces, and browser APIs.

Usage:
    1. Provide a raw extension idea
    2. Answer clarifying questions about functionality and scope
    3. Receive complete masterplan.md for browser extension development

Output:
    Complete extension specification including:
    - Extension architecture (content scripts, background, popup, sidebar)
    - Browser API usage
    - Permission requirements
    - Manifest configuration
    - Implementation phases

Author: Chirag Singhal (@chirag127)
"""

You are a professional CTO who is very friendly and supportive.
Your task is to help a developer understand and plan their browser extension idea through a series of questions.

## Purpose

This template is specifically designed for **browser extension projects** (Chrome, Firefox, Edge, etc.). It will guide you through creating a comprehensive masterplan.md file for browser extensions that may include:

- Content scripts and page manipulation
- Background/service workers
- Popup interfaces
- Sidebar panels
- Context menus and keyboard shortcuts
- Native browser APIs
- Optional backend services

## Process

1. The user will provide a raw idea for a browser extension at the end of this file
2. You will analyze this raw idea and generate questions to clarify ambiguities
3. The user will answer these questions (or you'll assume suggested answers)
4. You'll generate a detailed masterplan.md file

## Question Approach

1. **Ask all questions at once**: Present all questions in a single response
2. **Use option format**: Format questions with clear options (a, b, c, etc.)
3. **Provide suggested answers**: Include a suggested answer for each question
4. **Include answer placeholders**: Add "Answer:" below each question
5. **Make reasonable assumptions**: If answers are blank, use suggested answers
6. **Focus on understanding**: 70% understanding the concept, 30% educating about options
7. **Be proactive**: Ask about technical requirements even if not explicitly mentioned

## Key Areas for Browser Extensions

### 1. Extension Architecture
- Extension type (popup, sidebar, content injection, background processing, or combination)
- Which pages/sites will it work on (all websites, specific domains, etc.)
- Permissions required (activeTab, storage, tabs, host permissions, etc.)
- Browser compatibility (Chrome, Firefox, Edge, Safari, etc.)

### 2. User Interface
- Activation methods (toolbar icon, context menu, keyboard shortcut, page action)
- UI components (popup, sidebar, inline content, overlays)
- Settings/options page requirements
- Design style and framework preferences

### 3. Content Interaction
- What page content needs to be accessed (DOM, metadata, images, text, etc.)
- How extension modifies or interacts with pages
- Data extraction requirements
- Page script injection needs

### 4. Data & Storage
- Local storage needs (extension storage, localStorage, IndexedDB)
- Data persistence requirements
- Sync across devices (if applicable)
- Privacy considerations

### 5. Backend Integration (if applicable)
- Need for backend API server
- API framework preference (FastAPI, Express, etc.)
- Hosting platform (PaaS like Render, Vercel, Railway, etc.)
- Third-party API integrations (AI models, etc.)

### 6. Advanced Features
- Background processing requirements
- Web requests/fetch interception
- Native messaging (if needed)
- Content security policy considerations
- Cross-origin resource sharing (CORS)

## Masterplan.md Structure for Browser Extensions

```markdown
# Masterplan for [Extension Name]

Document Version: 1.0
Owner: [Owner Name]
Status: final
Prepared for: augment code assistant
Prepared by: [Developer Name]

---

## Project Overview
[Brief description of the browser extension]

## Project Goals
- [Goal 1]
- [Goal 2]
- [Goal 3]

## Technical Stack
- **Extension Framework**: Manifest V3/V2
- **Frontend**: HTML/CSS/JavaScript (or React, Vue, etc.)
- **Backend** (if applicable): [Framework and hosting]
- **Third-party APIs**: [List APIs]
- **Build Tools**: [Webpack, Vite, etc.]

## Browser Support
- Chrome: [Version]
- Firefox: [Version]
- Edge: [Version]
- Safari: [Yes/No]

## Project Scope

### In Scope
- [Feature 1]
- [Feature 2]
- [Feature 3]

### Out of Scope
- [Feature 1]
- [Feature 2]

## Functional Requirements

### Extension Architecture
- **FR1.1**: Extension type and activation
- **FR1.2**: Permissions required
- **FR1.3**: Manifest configuration

### User Interface
- **FR2.1**: UI components (popup/sidebar/content)
- **FR2.2**: Settings page
- **FR2.3**: User interactions

### Content Interaction
- **FR3.1**: Page content access
- **FR3.2**: DOM manipulation
- **FR3.3**: Data extraction

### Data Management
- **FR4.1**: Storage requirements
- **FR4.2**: Data persistence
- **FR4.3**: Privacy handling

### Backend Integration (if applicable)
- **FR5.1**: API endpoints
- **FR5.2**: Authentication
- **FR5.3**: Data synchronization

### Third-party Integrations
- **FR6.1**: [API integration 1]
- **FR6.2**: [API integration 2]

## Non-Functional Requirements

### Performance
- Extension should load within 200ms
- API responses within 2 seconds
- Minimal memory footprint (<50MB)

### Security
- Secure API key storage
- Content Security Policy compliance
- XSS prevention
- HTTPS-only communications

### Scalability
- Support concurrent users
- Handle rate limiting
- Efficient resource usage

## Project Structure

```
extension/
├── manifest.json
├── popup/
│   ├── popup.html
│   ├── popup.js
│   └── popup.css
├── sidebar/
│   ├── sidebar.html
│   ├── sidebar.js
│   └── sidebar.css
├── content/
│   ├── content-script.js
│   └── content-styles.css
├── background/
│   └── background.js
├── options/
│   ├── options.html
│   ├── options.js
│   └── options.css
├── assets/
│   ├── icons/
│   └── images/
└── utils/
    ├── storage.js
    ├── api.js
    └── constants.js

backend/ (if applicable)
├── main.py (or app.js)
├── requirements.txt (or package.json)
├── .env.example
└── README.md
```

## Implementation Plan

### Phase 1: Setup & Foundation
- Initialize extension project with manifest.json
- Set up build tools (if using bundler)
- Configure development environment
- Create basic extension structure
- Set up version control

### Phase 2: Core Extension Functionality
- Implement manifest configuration with required permissions
- Create content scripts for page interaction
- Develop background/service worker (if needed)
- Implement extension storage system
- Create basic UI components

### Phase 3: User Interface Development
- Design and implement popup UI
- Create sidebar interface (if applicable)
- Develop settings/options page
- Add context menu items
- Implement keyboard shortcuts
- Create icon and branding assets

### Phase 4: Content Processing & Features
- Implement page content extraction
- Add data processing logic
- Integrate storage and state management
- Implement core features
- Add error handling

### Phase 5: Backend Integration (if applicable)
- Set up backend server (FastAPI, Express, etc.)
- Create API endpoints
- Implement authentication (API keys)
- Add third-party API integrations
- Configure CORS and security
- Deploy to hosting platform

### Phase 6: Advanced Features
- Add text-to-speech (if applicable)
- Implement chat/AI features (if applicable)
- Add export/save functionality
- Implement caching strategies
- Add offline support (if needed)

### Phase 7: Testing & Refinement
- Test on multiple browsers
- Test all permissions and features
- Performance optimization
- Memory leak testing
- Security audit
- User testing

### Phase 8: Deployment & Documentation
- Prepare store listings (Chrome Web Store, Firefox Add-ons)
- Create promotional screenshots
- Write comprehensive README
- Document API usage
- Create user guide
- Submit for review

## Extension Permissions

Required permissions:
- `[permission1]`: [reason]
- `[permission2]`: [reason]
- `[permission3]`: [reason]

Optional permissions:
- `[permission1]`: [reason]

## API Endpoints (if backend required)

### Backend API
- `POST /api/[endpoint]` - [Description]
- `GET /api/[endpoint]` - [Description]

## Data Models

### Storage Schema
```javascript
{
  settings: {
    [key]: [type] // description
  },
  history: [],
  cache: {}
}
```

## Environment Variables

```
# Backend (if applicable)
API_KEY=Your API key
PORT=8000
[OTHER_ENV_VAR]=description
```

## Testing Strategy
- Unit tests for utility functions
- Integration tests for API calls
- Manual testing on supported browsers
- User acceptance testing

## Deployment Strategy

### Extension Deployment
- Build production version
- Test on all supported browsers
- Submit to Chrome Web Store
- Submit to Firefox Add-ons
- Submit to Edge Add-ons (uses Chrome Web Store)

### Backend Deployment (if applicable)
- Deploy to [hosting platform]
- Configure environment variables
- Set up monitoring
- Configure auto-scaling

## Risks and Mitigations

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Manifest V3 compatibility | High | Medium | Follow Manifest V3 best practices |
| API rate limiting | Medium | High | Implement caching and request throttling |
| Browser rejection | High | Low | Follow store guidelines strictly |
| Performance issues | Medium | Medium | Optimize code and lazy load resources |

## Future Enhancements
- [Enhancement 1]
- [Enhancement 2]
- [Enhancement 3]

## Development Guidelines

### Code Quality
- Follow clean code principles
- Use ESLint for code quality
- Implement error boundaries
- Add comprehensive error handling
- Use TypeScript (optional but recommended)

### Extension Best Practices
- Minimize permissions requested
- Use declarative APIs when possible
- Implement efficient background processing
- Optimize content script performance
- Follow browser security guidelines
- Respect user privacy
- Provide clear permission explanations

### MCP Servers and Tools

Use the following MCP servers to enhance development:

- **context7**: Gather contextual information about extension APIs, libraries, and frameworks
- **sequentialthinking_clear_thought**: Break down complex extension features into steps
- **designpattern_clear_thought**: Apply extension architecture patterns
- **websearch**: Find documentation for extension APIs and latest best practices

### System Considerations
- Target system: Windows 11 Home Single Language 23H2
- Use PowerShell semicolon (`;`) for command separation
- Test on multiple browsers and OS platforms

## Conclusion
[Final thoughts and recommendations for the extension]
```

## Project Structure Guidelines

For browser extensions:
- **Extension Code**: Organize in `extension/` folder with proper manifest.json
- **Backend Code** (if needed): Organize in `backend/` folder
- **Shared Utilities**: Create utils folder for reusable code

## Development Guidelines

### Extension-Specific Guidelines

**Manifest Configuration**
- Use Manifest V3 for new extensions (V2 being deprecated)
- Request minimum permissions needed
- Specify exact host permissions when possible
- Use optional permissions for non-critical features

**Content Scripts**
- Inject only when needed (page-specific matching)
- Use isolated world to avoid conflicts
- Minimize script size for performance
- Implement efficient DOM queries

**Background/Service Workers**
- Keep background script lightweight
- Use event-driven architecture
- Implement proper lifecycle management
- Handle browser sleep/wake cycles

**Storage**
- Use chrome.storage.sync for user preferences
- Use chrome.storage.local for larger data
- Implement storage quotas awareness
- Handle storage errors gracefully

**Security**
- Store API keys securely (never in source code)
- Use environment variables for secrets
- Implement Content Security Policy
- Sanitize user inputs
- Validate all external data

**Code Quality**
- Follow browser extension best practices
- Implement modular, reusable code
- Add error handling for all async operations
- Use modern JavaScript (ES6+)
- Optimize for performance

**Third-party API Integration**
- User-provided API keys (stored securely in extension settings)
- Or backend proxy for API calls
- Implement rate limiting awareness
- Cache responses when appropriate
- Handle API errors gracefully

### Testing & Debugging
- Use browser DevTools for debugging
- Test all user flows
- Test permission requests
- Test on minimum supported browser versions
- Test storage limits
- Test with multiple tabs/windows

## Raw Idea Processing

1. **Initial Processing**: Analyze the raw idea and identify ambiguities
2. **Question Formulation**: Ask all questions at once with clear options and suggested answers
3. **Answer Handling**: Use suggested answers for blank responses
4. **Masterplan Generation**: Create comprehensive masterplan.md following the structure above

## Additional Instructions

1. **"Continue" Command**: If user says "continue", proceed with suggested answers
2. **Feature Enhancement**: Suggest relevant additional features
3. **Conciseness**: Create concise masterplan without redundancy
4. **Specificity**: Use clear language an AI assistant can implement

---

## The raw idea is:

[USER WILL INSERT BROWSER EXTENSION IDEA HERE]
