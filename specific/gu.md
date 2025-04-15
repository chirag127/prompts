

**Prompt for AI Agent: Generate PRD for YouTube Video Summarizer App**

**Objective:** Generate a detailed Product Requirements Document (PRD) for a cross-platform (iOS, Android, Web) React Native Expo application. This application allows users to get summaries of YouTube videos, store them, and listen to them using Text-to-Speech (TTS) with specific interactive features.

**Target Audience for this PRD:** The AI agent (you) who will subsequently use this PRD to build the application.

**Instructions for PRD Generation:**

1.  **Structure:** Organize the PRD with clear headings and subheadings (e.g., 1. Introduction, 2. Goals, 3. Target Audience, 4. Functional Requirements, 5. Non-Functional Requirements, 6. Technical Specifications, 7. Data Management, 8. Future Considerations (explicitly state none if applicable, as per 'final product' requirement), 9. Open Issues (if any)). Follow the numbering convention shown in the example (e.g., 4.1, FR1.1).
2.  **Completeness:** Ensure all requirements listed below are captured accurately within the PRD.
3.  **Clarity:** Use precise and unambiguous language. Define terms where necessary.
4.  **Format:** Present the final PRD in a clean, well-formatted document structure.
5.  **No Implementation:** This prompt is for generating the *PRD document only*. Do not generate code at this stage.

**Core Application Concept:**

The application enables users to input YouTube video links (via pasting or sharing) to generate text summaries using the Gemini 2.0 Flash-Lite model. Summaries are stored in MongoDB, displayed with video metadata, and can be read aloud using a highly controllable TTS engine with visual feedback (highlighting, scrolling). Users can manage their summary history and customize summary generation and TTS playback settings.

**Detailed Requirements to Include in the PRD:**

**1. Introduction**
    *   Brief overview of the application: "YouTube Summarizer."
    *   Purpose: To provide users with concise summaries of YouTube videos and an accessible read-aloud feature.
    *   Target Platforms: iOS, Android, Web.

**2. Goals**
    *   Provide quick understanding of YouTube video content without watching the entire video.
    *   Offer accessible content consumption through integrated TTS.
    *   Allow customization of summary detail and TTS playback.
    *   Enable easy management and sharing of generated summaries.
    *   Deliver a seamless, modern, and user-friendly experience across platforms.

**3. Target Audience**
    *   Users seeking quick information from videos (students, researchers, professionals).
    *   Users with limited time for video consumption.
    *   Users who prefer auditory learning or require accessibility features.
    *   General YouTube users looking for content digests.

**4. Functional Requirements (FR)**

    **4.1. Video Link Input & Processing**
        *   **FR1.1 Paste Link:** Users must be able to paste a YouTube video URL (e.g., `https://www.youtube.com/watch?v=...`, `https://youtu.be/...`) into a designated text input field on the main screen.
        *   **FR1.2 Share-to-App:** Users must be able to use the native 'Share' functionality from the YouTube app (iOS/Android) or a web browser to send a YouTube link directly to this application, initiating the summarization process.
        *   **FR1.3 Client-Side Validation:** Implement initial client-side URL validation. This validation should primarily check for the presence of `youtube.com` or `youtu.be` domains within the input string. More robust validation will occur on the backend.
        *   **FR1.4 Backend Interaction:** Valid links (client-side check passed) are sent to the backend API for processing.
        *   **FR1.5 Transcript Fetching:** The backend (using `yt-dlp` or similar) must attempt to fetch the video transcript/captions.
            *   **FR1.5.1 Language Preference:** Prioritize fetching English transcripts/captions if available.
            *   **FR1.5.2 Language Flexibility:** If English is unavailable, fetch transcripts/captions in *any* available language. The transcript language does *not* need to be English.
        *   **FR1.6 Metadata Fetching:** The backend must attempt to fetch the video's Title and Thumbnail URL.
        *   **FR1.7 Fetching Fallback (Metadata):** Summary generation *must not* fail solely because the Title or Thumbnail could not be retrieved. Default placeholders or indicators should be used in the UI if metadata is missing.
        *   **FR1.8 No Transcript Fallback:** If no transcripts or captions are available for the video in any language, the backend must inform the frontend, and the app *must* display a clear message to the user indicating that the video cannot be summarized due to the lack of transcripts/captions.
        *   **FR1.9 Cancellation:** Users *must* have a way to cancel a summary generation request while it is in progress (e.g., a 'Cancel' button visible during the loading/processing state).

    **4.2. Summary Generation**
        *   **FR2.1 AI Model:** Use the Gemini 2.0 Flash-Lite model via API calls for generating summaries. (Reference the provided Python example code snippet structure for backend implementation guidance).
        *   **FR2.2 Summary Prompt:** The prompt sent to the Gemini model must explicitly instruct it to:
            *   Generate a summary based on the provided transcript.
            *   **Always generate the summary in the English language**, regardless of the transcript's original language.
            *   Adhere to the user-selected Summary Type and Length.
            *   Format the output using Markdown.
        *   **FR2.3 Summary Types:** Provide options for summary type:
            *   Brief
            *   Detailed
            *   Key Point
        *   **FR2.4 Default Summary Type:** The default summary type must be set to "Brief".
        *   **FR2.5 Summary Lengths:** Provide options for summary length:
            *   Short
            *   Medium
            *   Long
        *   **FR2.6 Default Summary Length:** The default summary length must be set to "Medium".
        *   **FR2.7 User Selection:** Users must be able to select the desired Summary Type and Length *before* initiating the summarization process. These selections should also be editable for existing summaries (triggers regeneration).

    **4.3. Summary Display**
        *   **FR3.1 Card Format:** Display each generated summary within a distinct card component.
        *   **FR3.2 Card Contents:** Each summary card must display:
            *   Video Title (or placeholder if unavailable).
            *   Video Thumbnail (or placeholder if unavailable).
            *   Summary Text (rendered correctly from Markdown format, displaying formatting like headings, bold, italics, lists, but *not* the raw Markdown symbols like `#`, `*`).
            *   Summary Type (e.g., "Type: Brief").
            *   Summary Length (e.g., "Length: Medium").
            *   Read Aloud Button.
            *   Share Button.
            *   Delete Button.
            *   Edit Button (allows changing Summary Type/Length and regenerating).
        *   **FR3.3 Markdown Rendering:** Implement a component capable of parsing and displaying Markdown content correctly within the summary text area.

    **4.4. Text-to-Speech (TTS) Functionality**
        *   **FR4.1 Activation:** A dedicated "Read Aloud" button on each summary card initiates TTS playback for that summary.
        *   **FR4.2 Start Point:** Playback must always start from the beginning of the summary text when the "Read Aloud" button is initially pressed.
        *   **FR4.3 Word-by-Word Highlighting:** **Crucially**, as the TTS engine reads the text, the *specific word* currently being spoken must be visually highlighted within the summary text display.
        *   **FR4.4 Auto-Scrolling:** As playback progresses, the application must automatically scroll the summary text view so that the line containing the currently spoken word is positioned near the top of the visible screen area, ensuring the user can follow along without manual scrolling.
        *   **FR4.5 Ignore Markdown Symbols:** The TTS engine *must not* read aloud any Markdown syntax characters (e.g., '#', '*', '_', '`', etc.). Only the textual content should be vocalized.
        *   **FR4.6 Playback Controls:** Provide persistent UI controls (visible during playback) for:
            *   Pause: Temporarily halt playback.
            *   Resume: Continue playback from the paused position.
            *   Stop: End playback completely and reset playback position to the beginning.
        *   **FR4.7 Volume Control:** Provide a slider or similar control (likely in Settings, potentially also accessible during playback) to adjust the TTS volume independently of the device's media volume.
        *   **FR4.8 Applicability:** TTS functionality must be available for all generated summaries, regardless of type or length.

    **4.5. TTS Settings Customization (Settings Screen)**
        *   **FR5.1 Access:** Provide a dedicated 'Settings' screen accessible from the main navigation (e.g., tab bar, hamburger menu).
        *   **FR5.2 Speed Control:** Allow users to adjust the TTS playback speed. Provide a range of options, including speeds up to **16x** the normal rate (ensure the TTS engine supports this range; define specific steps like 0.5x, 1x, 1.5x, 2x, ... 16x).
        *   **FR5.3 Pitch Control:** Allow users to adjust the pitch of the TTS voice. Provide a range of adjustments (e.g., low, normal, high, or a slider).
        *   **FR5.4 Voice Selection:** Allow users to select from available TTS voices installed on the device or provided by the TTS library.
        *   **FR5.5 Persistence:** TTS settings (speed, pitch, voice, volume) must be saved persistently on the device and applied to all subsequent playback sessions until changed by the user.

    **4.6. History Management**
        *   **FR6.1 History Screen:** Implement a dedicated 'History' screen displaying a list of all previously generated and saved summaries.
        *   **FR6.2 History List Format:** Each entry in the history list must display:
            *   Video Thumbnail (or placeholder).
            *   Video Title (or placeholder).
        *   **FR6.3 Accessing Summary:** Tapping an entry in the history list must navigate the user to the full summary display card for that video.
        *   **FR6.4 Deletion:** Users must be able to delete individual summaries from their history (e.g., via a swipe action or a delete button on the history entry or summary card). Confirmation should be requested before deletion.
        *   **FR6.5 Hamburger Menu Link:** Include the original YouTube video link associated with a summary, accessible perhaps within a context menu (like a hamburger menu or 'details' section) on the summary card display.

    **4.7. Sharing**
        *   **FR7.1 Share Functionality:** The 'Share' button on the summary card must allow users to share the *generated summary text* (and potentially the original video link) using the native OS sharing capabilities.

    **4.8. Theme Support**
        *   **FR8.1 Light Mode:** The app must have a default light theme.
        *   **FR8.2 Dark Mode:** The app must support a dark theme.
        *   **FR8.3 Theme Switching:** Provide an option (likely in Settings) for the user to manually select Light Mode, Dark Mode, or follow the system theme setting. The chosen theme must be applied consistently across the entire application.

**5. Non-Functional Requirements (NFR)**

    *   **NFR1. User Interface (UI):** Implement a modern, clean, and intuitive user interface. Focus on ease of use.
    *   **NFR2. User Experience (UX):** Ensure a smooth and responsive user experience. Provide clear feedback for actions (e.g., loading indicators during summarization, success/error messages).
    *   **NFR3. Accessibility (A11y):** Design with accessibility in mind. Ensure adequate color contrast, support for dynamic font sizes where feasible, and logical navigation for screen readers (especially for TTS controls and highlighted text).
    *   **NFR4. Performance:** Optimize for fast loading times and efficient resource usage (CPU, memory, network) on mobile devices and web. Ensure smooth scrolling and responsiveness, especially during TTS playback with highlighting/scrolling.
    *   **NFR5. Error Handling:** Implement robust error handling for API calls (network errors, Gemini API errors, YouTube data fetching errors), invalid inputs, and unexpected scenarios. Provide user-friendly error messages.
    *   **NFR6. Cross-Platform Consistency:** While adapting to platform conventions, maintain a consistent core experience and visual identity across iOS, Android, and Web.
    *   **NFR7. Security:** Backend API endpoints should be secured. Sensitive information like API keys must not be exposed in the frontend code. Backend validation of YouTube URLs is crucial.

**6. Technical Specifications**

    *   **TS1. Frontend Framework:** React Native with Expo.
    *   **TS2. Frontend Language:** JavaScript.
    *   **TS3. Backend Framework:** FastAPI.
    *   **TS4. Backend Language:** Python.
    *   **TS5. AI Model Integration:** Backend interacts with Google Gemini 2.0 Flash-Lite API. Use the `google-genai` Python library.
    *   **TS6. YouTube Data Retrieval:** Backend uses the `yt-dlp` Python library (or a similarly robust alternative) to fetch transcripts/captions, video titles, and thumbnail URLs.
    *   **TS7. Database:** MongoDB for storing summary data (video link, title, thumbnail URL, summary text, type, length, user ID if applicable, timestamps).
    *   **TS8. Text-to-Speech Engine:** Utilize an Expo-compatible TTS library (e.g., `expo-speech`) capable of providing word-level timing information (required for highlighting) and supporting adjustments for speed (up to 16x), pitch, voice selection, and volume. Investigate library capabilities thoroughly to ensure highlighting and high-speed playback are achievable.
    *   **TS9. Markdown Rendering:** Use a suitable React Native Markdown rendering library (e.g., `react-native-markdown-display` or similar) that allows customization and integrates well with text components.
    *   **TS10. Project Structure:**
        *   `/frontend`: Contains all React Native Expo app code.
        *   `/backend`: Contains all FastAPI backend code.
    *   **TS11. State Management (Frontend):** Choose a suitable state management library if needed (e.g., Zustand, Redux Toolkit, React Context API) for managing application state, especially for TTS playback state and settings.

**7. Data Management**

    *   **DM1. Schema:** Define a MongoDB collection schema for summaries, including fields for:
        *   `_id` (MongoDB ObjectId)
        *   `userId` (if user accounts are planned, otherwise optional)
        *   `videoUrl` (String, Indexed)
        *   `videoTitle` (String, optional)
        *   `thumbnailUrl` (String, optional)
        *   `summaryText` (String)
        *   `summaryType` (String: 'Brief', 'Detailed', 'Key Point')
        *   `summaryLength` (String: 'Short', 'Medium', 'Long')
        *   `transcriptLanguage` (String, optional - language code of the source transcript)
        *   `createdAt` (Date)
        *   `updatedAt` (Date)
    *   **DM2. Storage:** All generated summaries are stored persistently in the MongoDB database, associated with the user (implicitly by device or explicitly if accounts are added later).
    *   **DM3. Retrieval:** The app fetches the history list and individual summaries from the backend API, which queries the MongoDB database.

**8. Production Readiness & Delivery Expectations (Instructions for the Agent Building the App)**

    *   **DEV1. Final Product Focus:** This PRD describes the *final, production-ready* application. Do not scope it as an MVP; implement all specified features.
    *   **DEV2. Proactive Research:** Do not withhold from searching the web. If you suspect APIs, library features (especially TTS capabilities for highlighting/speed), or best practices might have changed or are unclear, perform necessary research to ensure correct and modern implementation.
    *   **DEV3. Code Quality:** Deliver well-documented, clean, maintainable, and robust code following industry best practices for both frontend (React Native/JS) and backend (FastAPI/Python).
    *   **DEV4. Error-Free Frontend:** Ensure the frontend application is rigorously tested and free from functional errors and crashes. Pay special attention to the TTS synchronization (highlighting, scrolling) and state management.
    *   **DEV5. Testing:** Implement unit and integration tests where appropriate. Perform thorough manual testing across target platforms (simulators/emulators and, ideally, real devices) to verify all functional and non-functional requirements.
    *   **DEV6. Dependency Management:** Use up-to-date and well-maintained libraries.
    *   **DEV7. Strict Adherence:** Follow all requirements outlined in this PRD meticulously.

---

**Final Instruction:** Now, based on the detailed requirements and structure outlined above, please generate the comprehensive Product Requirements Document (PRD) for the YouTube Summarizer application.