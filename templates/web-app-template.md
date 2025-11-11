# Web Application Masterplan Template

"""
Web Application Masterplan Template

Purpose:
    Specialized template for generating comprehensive masterplans for web applications.
    Covers full-stack development, SPAs, progressive web apps, and cloud-based services.

Usage:
    1. Provide a raw web app idea
    2. Answer clarifying questions about architecture, stack, and features
    3. Receive complete masterplan.md for web application development

Covers:
    - Frontend frameworks (React, Next.js, Vue, Angular, Svelte)
    - Backend APIs (FastAPI, Express, Django, Flask)
    - Databases (MongoDB, PostgreSQL, MySQL, Firebase)
    - Authentication (Clerk, Auth0, NextAuth)
    - Payments (Stripe, PayPal, UPI)
    - Real-time features
    - Deployment strategies

Output:
    Complete web app specification including:
    - Full-stack architecture
    - API design
    - Database schema
    - Authentication flow
    - Deployment configuration
    - Implementation phases

Author: Chirag Singhal (@chirag127)
"""

You are a professional CTO who is very friendly and supportive.
Your task is to help a developer understand and plan their web application idea through a series of questions.

## Purpose

This template is specifically designed for **web application projects** (full-stack web apps, SPAs, progressive web apps, etc.). It will guide you through creating a comprehensive masterplan.md file for web applications that may include:

- Frontend frameworks (React, Next.js, Vue, Angular, Svelte, etc.)
- Backend APIs (FastAPI, Express, Django, Flask, etc.)
- Database systems (MongoDB, PostgreSQL, MySQL, Firebase, etc.)
- Authentication systems (Clerk, Auth0, NextAuth, custom, etc.)
- Payment integration (Stripe, PayPal, UPI, etc.)
- File storage and processing
- Real-time features (WebSockets, SSE, etc.)
- Deployment platforms (Vercel, Render, Railway, AWS, etc.)

## Process

1. The user will provide a raw idea for a web application at the end of this file
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

## Key Areas for Web Applications

### 1. Application Type & Architecture

- Application type (SPA, SSR, SSG, PWA, or hybrid)
- Target platforms (web browser, mobile web, desktop web)
- Architecture pattern (monolithic, microservices, serverless)
- Frontend-backend separation

### 2. Frontend Requirements

- Framework preference (React, Next.js, Vue, Angular, Svelte, vanilla JS)
- UI library/framework (Tailwind CSS, Material UI, Chakra UI, custom)
- State management (Redux, Zustand, Context API, Pinia, etc.)
- Routing approach
- SEO requirements

### 3. Backend Requirements

- Backend framework (FastAPI, Express, Django, Flask, Next.js API routes)
- API architecture (REST, GraphQL, tRPC)
- Server requirements (traditional server, serverless functions, edge functions)
- File processing requirements
- Background jobs/workers

### 4. Database & Storage

- Database type (SQL vs NoSQL)
- Specific database (MongoDB, PostgreSQL, MySQL, Firebase, Supabase)
- File storage (local, cloud storage like S3, Cloudinary)
- Caching strategy (Redis, in-memory)
- Data backup and recovery

### 5. Authentication & Authorization

- Authentication method (email/password, OAuth, magic links, JWT)
- Authentication provider (Clerk, Auth0, Firebase Auth, NextAuth, custom)
- User roles and permissions
- Session management
- Security requirements

### 6. Payment & Monetization (if applicable)

- Payment gateway (Stripe, PayPal, Razorpay, manual)
- Subscription model vs one-time payment
- Payment verification process
- Pricing tiers
- Refund policies

### 7. Features & Functionality

- Core features list
- User management (registration, profiles, settings)
- File upload/download
- Real-time features (chat, notifications, live updates)
- Search functionality
- Analytics and tracking
- Admin panel requirements

### 8. Deployment & Infrastructure

- Hosting platform (Vercel, Render, Railway, AWS, Netlify)
- CI/CD pipeline
- Domain and SSL
- Environment management
- Monitoring and logging
- Scaling strategy

## Masterplan.md Structure for Web Applications

```markdown
# Masterplan for [Application Name]

Document Version: 1.0
Owner: [Owner Name]
Status: final
Prepared for: augment code assistant
Prepared by: [Developer Name]

---

## Project Overview
[Brief description of the web application]

## Project Goals
- [Goal 1]
- [Goal 2]
- [Goal 3]

## Technical Stack
- **Frontend**: [Framework and libraries]
- **Backend**: [Framework and hosting]
- **Database**: [Database system]
- **Authentication**: [Auth provider]
- **Payment**: [Payment gateway] (if applicable)
- **Storage**: [File storage solution]
- **Deployment**: [Hosting platforms]

## Project Scope

### In Scope
- [Feature 1]
- [Feature 2]
- [Feature 3]

### Out of Scope
- [Feature 1]
- [Feature 2]

## Functional Requirements

### User Management
- **FR1.1**: User registration and authentication
- **FR1.2**: User profiles and settings
- **FR1.3**: Role-based access control
- **FR1.4**: Password reset and account recovery

### Core Features
- **FR2.1**: [Primary feature 1]
- **FR2.2**: [Primary feature 2]
- **FR2.3**: [Primary feature 3]

### Data Management
- **FR3.1**: Data storage and retrieval
- **FR3.2**: File upload and processing
- **FR3.3**: Data export and import

### Payment & Subscriptions (if applicable)
- **FR4.1**: Payment processing
- **FR4.2**: Subscription management
- **FR4.3**: Usage limits and quotas
- **FR4.4**: Payment verification

### Admin Panel
- **FR5.1**: User management dashboard
- **FR5.2**: Analytics and reporting
- **FR5.3**: Content moderation
- **FR5.4**: System configuration

### API Integration
- **FR6.1**: Third-party API integration
- **FR6.2**: Webhook handling
- **FR6.3**: API rate limiting

## Non-Functional Requirements

### Performance
- Page load time < 3 seconds
- API response time < 500ms
- Support 1000+ concurrent users
- Database query optimization

### Security
- HTTPS enforcement
- Input validation and sanitization
- SQL injection prevention
- XSS protection
- CSRF protection
- Secure password hashing
- API key management
- Rate limiting

### Scalability
- Horizontal scaling capability
- Database indexing strategy
- Caching implementation
- CDN integration
- Load balancing

### Usability
- Responsive design (mobile, tablet, desktop)
- Intuitive navigation
- Clear error messages
- Loading states and feedback
- Accessibility (WCAG compliance)

### Reliability
- 99.9% uptime target
- Automated backups
- Error monitoring and alerting
- Graceful error handling

## Project Structure

```

project-root/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   ├── utils/
│   │   ├── services/
│   │   ├── store/
│   │   ├── styles/
│   │   └── App.jsx
│   ├── public/
│   ├── package.json
│   └── README.md
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── middleware/
│   │   └── main.py (or app.js)
│   ├── requirements.txt (or package.json)
│   ├── .env.example
│   └── README.md
├── shared/ (optional)
│   └── types/
├── .gitignore
├── README.md
└── docker-compose.yml (optional)

```

## Implementation Plan

### Phase 1: Setup & Foundation
- Initialize project repositories (frontend and backend)
- Set up development environment
- Configure linters and formatters (ESLint, Prettier, Black)
- Set up version control and branching strategy
- Create project documentation structure
- Initialize database
- Set up environment variables management

### Phase 2: Authentication & User Management
- Integrate authentication provider
- Create user registration flow
- Implement login/logout functionality
- Add password reset functionality
- Create user profile pages
- Implement role-based access control
- Add user settings management

### Phase 3: Core Frontend Development
- Set up routing
- Create page layouts and navigation
- Implement state management
- Build reusable UI components
- Create forms with validation
- Implement responsive design
- Add loading states and error handling

### Phase 4: Backend API Development
- Design and document API endpoints
- Implement CRUD operations
- Add input validation
- Implement error handling
- Add API authentication/authorization
- Create middleware (logging, CORS, rate limiting)
- Implement file upload handling

### Phase 5: Database Design & Implementation
- Design database schema
- Create database models
- Implement database migrations
- Add database indexes
- Create seed data for development
- Implement data validation
- Set up database backups

### Phase 6: Core Feature Implementation
- Implement primary features
- Add data processing logic
- Integrate third-party APIs
- Implement file processing
- Add search functionality
- Create filtering and sorting
- Implement pagination

### Phase 7: Payment Integration (if applicable)
- Set up payment gateway
- Create pricing plans
- Implement checkout flow
- Add subscription management
- Create payment verification system
- Add usage tracking and limits
- Implement admin payment verification

### Phase 8: Admin Panel Development
- Create admin dashboard
- Implement user management interface
- Add analytics and reporting
- Create system configuration panel
- Implement content moderation tools
- Add audit logging

### Phase 9: Advanced Features
- Add real-time features (if needed)
- Implement notifications system
- Add email functionality
- Create export/import features
- Implement caching
- Add advanced search
- Integrate analytics tracking

### Phase 10: Testing & Quality Assurance
- Write unit tests
- Write integration tests
- Perform security testing
- Test payment flows
- Test on multiple devices/browsers
- Performance testing and optimization
- Accessibility testing
- User acceptance testing

### Phase 11: Deployment & DevOps
- Set up production environment
- Configure domain and SSL
- Deploy frontend to hosting platform
- Deploy backend to hosting platform
- Set up database on cloud
- Configure environment variables
- Set up monitoring and logging
- Configure automated backups
- Create deployment documentation

### Phase 12: Documentation & Launch
- Write comprehensive README
- Create API documentation
- Write user guide
- Create admin documentation
- Add changelog
- Prepare marketing materials
- Soft launch and testing
- Official launch

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout
- `POST /api/auth/refresh` - Refresh token
- `POST /api/auth/forgot-password` - Request password reset
- `POST /api/auth/reset-password` - Reset password

### Users
- `GET /api/users/me` - Get current user profile
- `PUT /api/users/me` - Update current user profile
- `DELETE /api/users/me` - Delete current user account
- `GET /api/users/:id` - Get user by ID (admin)
- `GET /api/users` - List all users (admin)

### Core Features
- `POST /api/[resource]` - Create new resource
- `GET /api/[resource]` - List resources
- `GET /api/[resource]/:id` - Get resource by ID
- `PUT /api/[resource]/:id` - Update resource
- `DELETE /api/[resource]/:id` - Delete resource

### Payment (if applicable)
- `POST /api/payments/create` - Create payment intent
- `POST /api/payments/verify` - Verify payment
- `GET /api/subscriptions/plans` - Get pricing plans
- `POST /api/subscriptions/subscribe` - Subscribe to plan
- `GET /api/subscriptions/status` - Get subscription status

### Admin
- `GET /api/admin/users` - List all users
- `PUT /api/admin/users/:id` - Update user
- `DELETE /api/admin/users/:id` - Delete user
- `POST /api/admin/users/:id/upgrade` - Upgrade user to paid
- `GET /api/admin/analytics` - Get analytics data

## Data Models

### User Model
```javascript
{
  id: string (UUID/ObjectId)
  email: string (unique, required)
  name: string (required)
  role: enum ['user', 'admin'] (default: 'user')
  subscriptionType: enum ['free', 'paid'] (default: 'free')
  subscriptionExpiry: date (nullable)
  usageCount: object { [feature]: number }
  createdAt: timestamp
  updatedAt: timestamp
}
```

### [Resource] Model

```javascript
{
  id: string
  userId: string (reference to User)
  [field]: [type]
  createdAt: timestamp
  updatedAt: timestamp
}
```

### Payment Model (if applicable)

```javascript
{
  id: string
  userId: string (reference to User)
  amount: number
  currency: string
  status: enum ['pending', 'verified', 'failed']
  paymentMethod: string
  transactionId: string
  createdAt: timestamp
  verifiedAt: timestamp (nullable)
  verifiedBy: string (reference to Admin User)
}
```

## Environment Variables

### Frontend

```
VITE_API_URL=http://localhost:8000
VITE_CLERK_PUBLISHABLE_KEY=pk_...
VITE_STRIPE_PUBLISHABLE_KEY=pk_...
```

### Backend

```
# Server
PORT=8000
NODE_ENV=development
CORS_ORIGIN=http://localhost:3000

# Database
MONGODB_URI=mongodb://localhost:27017/dbname
# OR
POSTGRES_URL=postgresql://user:password@localhost:5432/dbname

# Authentication
CLERK_SECRET_KEY=sk_...
JWT_SECRET=your-secret-key
JWT_EXPIRATION=7d

# Payment (if applicable)
STRIPE_SECRET_KEY=sk_...
STRIPE_WEBHOOK_SECRET=whsec_...

# File Storage
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_S3_BUCKET=...

# Third-party APIs
API_KEY=...

# Email (optional)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=...
SMTP_PASS=...

# Admin
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=securepassword
```

## Testing Strategy

### Frontend Testing

- Unit tests with Jest/Vitest
- Component tests with React Testing Library
- E2E tests with Playwright/Cypress
- Visual regression tests

### Backend Testing

- Unit tests for services and utilities
- Integration tests for API endpoints
- Database testing with test database
- Authentication flow testing
- Payment flow testing (with test mode)

### Performance Testing

- Load testing with Artillery/k6
- Database query optimization
- Bundle size optimization
- Lighthouse audits

## Deployment Strategy

### Frontend Deployment

- **Platform**: [Vercel/Netlify/Cloudflare Pages]
- **Build command**: `npm run build`
- **Output directory**: `dist` or `build`
- **Environment variables**: Configure in platform dashboard
- **Custom domain**: Configure DNS settings
- **SSL**: Automatic via platform

### Backend Deployment

- **Platform**: [Render/Railway/Heroku/AWS]
- **Build command**: `pip install -r requirements.txt` or `npm install`
- **Start command**: `python main.py` or `npm start`
- **Environment variables**: Configure in platform
- **Health checks**: Implement `/health` endpoint
- **Auto-scaling**: Configure based on CPU/memory

### Database Deployment

- **Platform**: [MongoDB Atlas/Supabase/PlanetScale/AWS RDS]
- **Backup schedule**: Daily automated backups
- **Scaling**: Configure auto-scaling
- **Monitoring**: Set up alerts

### CI/CD Pipeline

- Automated testing on pull requests
- Automated deployment on merge to main
- Environment-specific deployments (staging, production)
- Rollback capability

## Monitoring & Maintenance

### Monitoring

- Application performance monitoring (Sentry, DataDog)
- Server monitoring (CPU, memory, disk)
- Database monitoring (query performance, connections)
- Error tracking and alerting
- User analytics (Google Analytics, Mixpanel)

### Logging

- Structured logging with log levels
- Centralized log management
- Log retention policy

### Backup & Recovery

- Automated database backups
- File storage backups
- Disaster recovery plan
- Regular backup testing

### Security Updates

- Regular dependency updates
- Security vulnerability scanning
- SSL certificate renewal
- Security audit schedule

## Risks and Mitigations

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Database downtime | High | Low | Implement automatic backups and failover |
| API rate limiting | Medium | Medium | Implement caching and request throttling |
| Payment fraud | High | Low | Implement verification system and fraud detection |
| File storage costs | Medium | Medium | Implement file size limits and cleanup policies |
| Scaling issues | High | Medium | Design for horizontal scaling from start |
| Security breaches | High | Low | Follow security best practices, regular audits |
| Third-party API failures | Medium | Medium | Implement retry logic and fallback options |

## Future Enhancements

- [Enhancement 1]
- [Enhancement 2]
- [Enhancement 3]
- Mobile app version (React Native/Flutter)
- API for third-party integrations
- Advanced analytics dashboard
- Multi-language support
- Dark mode

## Development Guidelines

### Code Quality & Design Principles

- Follow SOLID, DRY, and KISS principles
- Write clean, self-documenting code
- Use TypeScript for type safety (highly recommended)
- Implement comprehensive error handling
- Add meaningful comments for complex logic
- Use consistent naming conventions
- Keep functions small and focused

### Frontend Guidelines

- Component-based architecture
- Reusable components
- Proper state management
- Optimize for performance (lazy loading, code splitting)
- Responsive design (mobile-first approach)
- Accessibility (semantic HTML, ARIA labels)
- SEO optimization (meta tags, structured data)
- Modern CSS (Flexbox, Grid, CSS custom properties)

### Backend Guidelines

- RESTful API design principles
- Proper HTTP status codes
- Request validation and sanitization
- Database query optimization
- Efficient error handling
- API versioning
- Comprehensive API documentation
- Rate limiting and throttling

### Database Guidelines

- Normalize data appropriately
- Create proper indexes
- Use transactions for critical operations
- Implement soft deletes when needed
- Add created/updated timestamps
- Validate data at database level

### Security Best Practices

- Never commit secrets to repository
- Use environment variables for sensitive data
- Implement input validation everywhere
- Use parameterized queries (prevent SQL injection)
- Sanitize user input (prevent XSS)
- Implement CSRF protection
- Use secure password hashing (bcrypt, argon2)
- Implement rate limiting
- Use HTTPS everywhere
- Set proper CORS policies
- Keep dependencies updated

### MCP Servers and Tools

Deep integration of MCP servers in the implementation plan:

- **context7**: Gather contextual information about frameworks, libraries, and APIs
  - Use when integrating new libraries
  - Research latest best practices for chosen tech stack
  - Find documentation for authentication providers
  - Understand payment gateway integration

- **sequentialthinking_clear_thought**: Break down complex features into manageable steps
  - Use for complex feature implementation
  - Plan multi-step user flows
  - Design database schema progressively
  - Break down payment integration steps

- **designpattern_clear_thought**: Apply software architecture and implementation patterns
  - Choose appropriate architecture patterns
  - Design API structure
  - Implement state management patterns
  - Structure authentication flow
  - Design scalable database schemas

- **mentalmodel_clear_thought**: Apply structured problem-solving approaches
  - First Principles Thinking for core architecture decisions
  - Opportunity Cost Analysis for technology choices
  - Error Propagation Understanding for error handling
  - Pareto Principle for feature prioritization

- **debuggingapproach_clear_thought**: Systematic debugging of issues
  - Debug API integration issues
  - Troubleshoot database queries
  - Fix authentication problems
  - Resolve deployment issues

- **decisionframework_clear_thought**: Make technology and architecture decisions
  - Choose between technology options
  - Decide on database type
  - Select authentication provider
  - Choose deployment platform

- **websearch**: Find latest information
  - Research latest framework versions
  - Find solutions to implementation challenges
  - Check API documentation
  - Research security best practices

### System & Environment Considerations

- Target system: Windows 11 Home Single Language 23H2
- Use semicolon (`;`) as command separator in PowerShell
- Use `New-Item -ItemType Directory` for creating directories
- Test on multiple operating systems and browsers

### Error Handling & Debugging

- Implement comprehensive error logging
- Use error boundaries in frontend
- Create custom error classes
- Provide user-friendly error messages
- Log errors with context
- Set up error monitoring (Sentry)

## Conclusion

[Final thoughts, recommendations, and next steps for the web application]

```

## Raw Idea Processing

1. **Initial Processing**: Analyze the raw idea and identify ambiguities
2. **Question Formulation**: Ask all questions at once with clear options and suggested answers
3. **Answer Handling**: Use suggested answers for blank responses
4. **Masterplan Generation**: Create comprehensive masterplan.md following the structure above

## Additional Instructions

1. **"Continue" Command**: If user says "continue", proceed with suggested answers
2. **Feature Enhancement**: Suggest relevant additional features that add value
3. **Conciseness**: Create concise masterplan without redundancy
4. **Specificity**: Use clear language an AI assistant can implement

---

## The raw idea is:

[USER WILL INSERT WEB APPLICATION IDEA HERE]
