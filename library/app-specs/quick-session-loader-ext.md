give me a prd to be given to ai agent that will be used for building a browser extension that

I want to make a browser extension that can store the session for the particular website and provide the option to restore the session in an easy manner possibly in one click. It will have a sign up  & in option so that the cookies can be synced across devices.

To help refine the implementation plan, here are some questions and answers to consider:

**I. Core Functionality (Session Saving & Restoring):**

1. **What constitutes a "session"?** Are you planning to store *only* cookies, or also other session-related data like `localStorage` or `sessionStorage` for the specific website? (Restoring `localStorage`/`sessionStorage` is more complex than cookies).
answer: I am planning to store all the session related data like cookies, localStorage and sessionStorage for the specific website.
2. **How granular is the storage?** Will it save the session for the exact domain (e.g., `app.example.com`) or for the entire base domain (e.g., all of `*.example.com`)?
answer: I am planning to store all the session related data like cookies for the specific website only and not for the entire base domain.
3. **How is a session saved?** Will the user manually click a "Save Session" button in the extension's popup/interface when they are on the target website? Or is there any automatic saving logic?
answer: I am planning to allow the user to manually click a "Save Session" button in the extension's popup/interface when they are on the target website.
4. **How are saved sessions identified/named?** Does the user provide a custom name for each saved session (e.g., "Work Account," "Test User Login")? Or is it just timestamped?
answer: I am planning to allow users to provide a custom name for each saved session.
5. **How is a session restored?** Does the user navigate to the website first and *then* click a "Restore" button for a specific saved session? What happens if they are already logged in with a *different* session on that site when they try to restore?
answer: when the user clicks on the restore button and if they are already logged in with a different session on that site then the extension will ask the user if they want to replace the current session with the saved one.
6. **What happens to existing cookies when restoring?** Does restoring *replace* all current cookies for that domain with the saved ones, or does it try to merge/add them? (Replacing is usually simpler and more effective for login sessions).
answer: restoring will replace all current cookies for that domain with the saved ones.
7. **HttpOnly Cookies:** Are you aware that browser extensions often cannot *read* `HttpOnly` cookies (a common security measure for session cookies)? They *can* usually set/delete them with the right permissions. How will your extension handle situations where it might not be able to fully "see" the session it's trying to save?
answer: choose appropriate answer for this question. Please ensure that the extension handles this limitation effectively and informs the user accordingly. Additionally, consider providing alternative methods for session management if necessary.

**II. User Interface & Experience:**

8. **Where will the user interact with the extension?** (e.g., Browser action popup? Context menu on the page? A sidebar?)
answer: The user will interact with the extension through a browser action popup and also a context menu on the page.
9. **How will saved sessions be presented for restoration?** A simple list? Grouped by website? Searchable?
answer: Saved sessions will be presented in a simple list format, grouped by website for easier navigation and selection.
10. **How will the user know *which* website a saved session belongs to when viewing the list?**
answer: Each saved session will display the website's name and logo for easy identification.
11. **What feedback does the user get after saving or restoring a session?** (Success message? Error message if it fails?)
answer: The user will receive a success message upon saving or restoring a session, and an error message if the operation fails, ensuring they are informed of the outcome.
12. **Does the extension need to reload the page after restoring a session for the changes to take effect?** Will it do this automatically or prompt the user?
answer: ask the user.

**III. Authentication & Synchronization:**

13. **What method will be used for Sign Up/Sign In?** (Email/Password? Google Sign-In? Other OAuth providers?)
answer: The extension will support Email/Password for Sign Up/Sign In only.
14. **Where will the user data (including the sensitive cookies) be stored for synchronization?** (Firebase? AWS DynamoDB/RDS? A custom backend?)

- mongodb will be used

15. **How will the cookies/session data be stored securely in the backend database?** Will they be encrypted at rest? What encryption methods? (This is CRITICAL - storing cookies plaintext is extremely risky).
answer: The cookies/session data will not be encrypted at rest.
16. **How will data be secured during transit between the extension and the backend?**.
answer: HTTP/HTTPS will be used to secure data during transit between the extension and the backend.
17. **How often will the extension sync with the backend?** (On every save/restore? Periodically? Only on login?)
answer: The extension will sync with the backend on every save/restore.
18. **What happens if the user is offline?** Can they still save/restore sessions locally? How is syncing handled when they come back online?
answer: The user can still save/restore sessions locally when offline. When they come back online, the extension will automatically sync the local data with the backend.

19. what happens if the user does not have an account?
answer: The user can still save/restore sessions locally, but they will not be able to sync the data with the backend until they create an account.

the sign up and sign in button will be available in the extension popup and the user can create an account or sign in to their existing account.
only the buttons will be shown not the form.

20 . will user be able to see the saved sessions in the extension popup without signing in?
answer: yes the user will be able to see the saved sessions in the extension popup without signing in, but they will not be able to sync the data with the backend until they create an account.

21. **How will the extension handle session expiration?** (e.g., if a session is no longer valid, will it notify the user?)
answer: The extension will notify the user if a session is no longer valid and provide options to refresh or re-authenticate as needed.
22. **Will the user be able to disable the extension for specific websites?** (e.g., a whitelist/blacklist feature?)
answer: The user will be able to disable the extension for specific websites using a whitelist/blacklist feature.

**IV. Security & Permissions:**

19. **What browser permissions will the extension require?** (`cookies`, `storage`, `activeTab`, access to specific URLs or `<all_urls>`? `identity` for auth?) You'll need to justify these to users.
answer: The extension will require all necessary permissions including `cookies`, `storage`, `activeTab`, and access to `<all_urls>` for full functionality and user experience. and any other permissions that are required for the extension to work properly.
20. **How will you prevent one user's synced data from being accessed by another user on the backend?** (Robust authentication and authorization logic).
answer: Robust authentication and authorization logic will be implemented to ensure that one user's synced data cannot be accessed by another user on the backend.
21. **Considering you're storing potentially sensitive login cookies, what measures are in place to protect the user's account for *your* service?** (Password hashing, rate limiting, etc.).
answer: Password hashing will be implemented for user accounts, along with rate limiting to prevent brute force attacks and ensure account security.

**V. Edge Cases & Scope:**

22. **Is there a limit to the number of sessions or websites a user can save?**
answer: There will be no limit to the number of sessions or websites a user can save, allowing for maximum flexibility and usability.
23. **How will the extension handle websites that heavily use techniques other than cookies for session management (e.g., JWTs in `localStorage`)?** (If you decide to support more than cookies).
answer: The extension will be designed to handle various session management techniques, including JWTs in `localStorage`, by implementing appropriate storage and retrieval methods.
24. **What happens if a website changes its cookie structure or login mechanism after a session was saved?** (The restored session might simply not work).
answer: The extension will be designed to handle changes in cookie structure or login mechanisms by implementing fallback methods to ensure session restoration is as seamless as possible.

give me the prd in a markdown format with the following sections:

# Product Requirements Document (PRD) for Browser Extension

1. **Overview**
   - The goal is to create a browser extension that allows users to save and restore sessions for specific websites, including cookies, `localStorage`, and `sessionStorage``. The extension will support user authentication for syncing sessions across devices.
    - The extension will provide a user-friendly interface for saving and restoring sessions, with options for custom naming of sessions.
    - The extension will also ensure secure handling of session data, including encryption and robust authentication mechanisms.

### 4. Core Features and Functional Requirements

#### 4.1
- **FR1.1 (P0):**

Is building a browser extension with the following setup:

- Frontend: Browser Extension (Manifest V3) using HTML, CSS, and JS.
- Backend: Express.js + mongodb for storage.
- Project Structure:
  - extension/ folder for browser extension code.
  - backend/ folder for backend code.
  - Storage: MongoDB for storage.

the name of the browser extension will be "Session Sync Pro".

- don't leave anything for future , this is a prd for final product not a mvp

assure that the agent will follow the above instructions and provide a complete and production-ready solution. The agent should also ensure that the code is well-documented, follows best practices, and is easy to maintain.
give the prd as concise as necessary and in a markdown format.
