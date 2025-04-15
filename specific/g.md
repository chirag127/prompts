Okay, here is a comprehensive Product Requirements Document (PRD) based on your specifications.

---

## Product Requirements Document: YouTube Video Summarizer Mobile App

**Version:** 1.0
**Date:** 2024-07-25
**Author:** AI Assistant (Generated based on user prompt)
**Status:** Draft

**Table of Contents:**

1.  Introduction
    1.1. Purpose
    1.2. Goals
    1.3. Scope
    1.4. Document Conventions
2.  Product Overview
    2.1. Application Purpose
    2.2. Target Platforms
    2.3. Key Value Proposition
    2.4. Primary User Personas
3.  System Architecture
    3.1. Frontend
    3.2. Backend
    3.3. AI Integration
    3.4. Database
    3.5. External Services
    3.6. Conceptual Diagram
4.  Core Features and Functional Requirements
    4.1. YouTube Video Input and Processing
    4.2. Summary Generation and Display
    4.3. Text-to-Speech (TTS) Functionality
    4.4. User Interface and Experience (UI/UX)
    4.5. Data Management
    4.6. Sharing Functionality
5.  Non-Functional Requirements
    5.1. Performance
    5.2. Error Handling
    5.3. Cross-Platform Compatibility
    5.4. Security
    5.5. Scalability
    5.6. Accessibility
    5.7. Offline Functionality
6.  API Integration Details
    6.1. Gemini 2.0 Flash-Lite API
    6.2. YouTube Data Extraction (yt-dlp)
7.  UI/UX Specifications
    7.1. Key Screens & Flow
    7.2. Navigation
    7.3. Input Methods
    7.4. Feedback Mechanisms
    7.5. Design System/Style Guide
8.  Implementation Guidelines
    8.1. Frontend Development
    8.2. Backend Development
    8.3. Testing
    8.4. Documentation
9.  Delivery Requirements
10. Open Issues / Future Considerations

---

### 1. Introduction

#### 1.1. Purpose
This document outlines the product requirements for a cross-platform mobile application designed to generate concise summaries of YouTube videos using Google's Gemini 2.0 Flash-Lite AI model.

#### 1.2. Goals
*   Provide users with a quick and efficient way to understand the content of YouTube videos without watching them entirely.
*   Deliver accurate and coherent summaries in various formats and lengths.
*   Offer an accessible and user-friendly experience across iOS, Android, and Web platforms.
*   Ensure a robust and scalable technical architecture.

#### 1.3. Scope
This PRD covers the initial production-ready release of the YouTube Video Summarizer application. It includes core features such as video input, transcript extraction, AI-powered summarization, text-to-speech functionality, history management, and summary sharing. Future enhancements beyond this scope will be documented separately.

#### 1.4. Document Conventions
*   **Requirements:** Functional requirements are numbered (FRX.Y) and non-functional requirements are described in their respective sections.
*   **Priority:** Each functional requirement is assigned a priority:
    *   **P0 (Must-Have):** Essential for the product launch.
    *   **P1 (Should-Have):** Important but not critical for initial launch; highly desirable.
    *   **P2 (Could-Have):** Optional feature that can be added later if resources permit.
    *   *(Note: As this is defined as a production-ready solution, not an MVP, most core features are P0)*

### 2. Product Overview

#### 2.1. Application Purpose
The application allows users to input a YouTube video link and receive an AI-generated summary of its content. This enables users to quickly grasp the key information, arguments, or narrative of a video, saving time and improving information accessibility.

#### 2.2. Target Platforms
*   **Mobile:** iOS, Android (developed using React Native Expo)
*   **Web:** Accessible via web browsers (leveraging React Native Expo for Web capabilities)

#### 2.3. Key Value Proposition
*   **Time Saving:** Understand video content significantly faster than watching.
*   **Accessibility:** Provides text-based alternatives for video content, aiding users with hearing impairments or those in environments where audio playback is inconvenient.
*   **Efficiency:** Quickly evaluate if a video is relevant before investing time in watching it.
*   **Information Extraction:** Easily extract key points or detailed overviews from educational content, talks, news clips, etc.

#### 2.4. Primary User Personas
*   **Persona 1: The Student (e.g., Alex, 20)**
    *   *Needs:* Quickly summarize long lectures, tutorials, or research presentations found on YouTube. Needs key takeaways for notes. Uses both mobile and laptop.
    *   *Goals:* Improve study efficiency, quickly find relevant information within videos.
*   **Persona 2: The Busy Professional (e.g., Sarah, 35)**
    *   *Needs:* Stay updated on industry talks, webinars, or news segments shared via YouTube links during limited downtime. Often uses mobile during commutes.
    *   *Goals:* Absorb key information quickly, decide if a video warrants full viewing later.
*   **Persona 3: The Lifelong Learner (e.g., David, 55)**
    *   *Needs:* Explore various topics on YouTube but has limited time. Wants to get the essence of documentaries, interviews, or educational content.
    *   *Goals:* Broaden knowledge efficiently, easily digest complex topics.
*   **Persona 4: The Content Curator (e.g., Maria, 28)**
    *   *Needs:* Quickly assess YouTube videos for relevance before sharing or curating them.
    *   *Goals:* Streamline content discovery and evaluation workflow.

### 3. System Architecture

#### 3.1. Frontend
*   **Framework:** React Native Expo
*   **Language:** JavaScript / TypeScript
*   **Platform Targets:** iOS, Android, Web
*   **Key Libraries:** Expo SDK, React Navigation, State Management (e.g., Zustand, Redux Toolkit), UI Component Library (e.g., React Native Paper, NativeWind/Tailwind).

#### 3.2. Backend
*   **Framework:** FastAPI
*   **Language:** Python
*   **API Style:** RESTful
*   **Deployment:** Containerized (e.g., Docker) service hosted on a cloud platform (e.g., AWS, GCP, Azure).

#### 3.3. AI Integration
*   **Model:** Google Gemini 2.0 Flash-Lite
*   **Access:** Via Google AI Python SDK (`google-genai`) integrated into the FastAPI backend.

#### 3.4. Database
*   **Type:** NoSQL Document Database
*   **System:** MongoDB (e.g., MongoDB Atlas cloud service or self-hosted)
*   **Purpose:** Store generated summaries, video metadata, user history, and preferences.

#### 3.5. External Services
*   **YouTube Data Extraction:** `yt-dlp` library (or equivalent robust library) executed/managed by the FastAPI backend to fetch video metadata and transcripts.
*   **Google AI Platform:** Hosting and serving the Gemini 2.0 Flash-Lite model.

#### 3.6. Conceptual Diagram

```mermaid
graph LR
    User[User] --> App[React Native Expo App (iOS/Android/Web)];
    App --> Backend[FastAPI Backend (Python)];
    Backend --> YT[YouTube];
    Backend -- Request Transcript/Metadata --> YTDLP[yt-dlp Service/Library];
    YTDLP -- Fetch Data --> YT;
    YTDLP -- Return Data --> Backend;
    Backend -- Send Transcript --> Gemini[Gemini 2.0 Flash-Lite API];
    Gemini -- Return Summary --> Backend;
    Backend -- Store/Retrieve Data --> DB[MongoDB Database];
    Backend -- Return Summary/Data --> App;

    style App fill:#f9f,stroke:#333,stroke-width:2px
    style Backend fill:#ccf,stroke:#333,stroke-width:2px
    style Gemini fill:#fcc,stroke:#333,stroke-width:2px
    style DB fill:#cfc,stroke:#333,stroke-width:2px
    style YTDLP fill:#ffc,stroke:#333,stroke-width:2px
```

### 4. Core Features and Functional Requirements

#### 4.1. YouTube Video Input and Processing
*   **FR1.1 (P0):** The application MUST allow users to input a YouTube video URL via direct pasting into a text input field.
*   **FR1.2 (P0):** The application MUST allow users to share a video link directly from the native YouTube application (iOS/Android) into the summarizer app using the system's share sheet functionality.
*   **FR1.3 (P0):** The backend MUST validate the provided input to ensure it is a valid YouTube video URL format.
*   **FR1.4 (P0):** If the input is invalid, the application MUST display a user-friendly error message (e.g., "Invalid YouTube URL. Please check the link and try again.").
*   **FR1.5 (P0):** Upon receiving a valid URL, the backend MUST use the `yt-dlp` library (or equivalent) to attempt fetching the video's transcript and essential metadata (Title, Thumbnail URL, Channel Name, Video Duration, Original Language).
*   **FR1.6 (P0):** If `yt-dlp` fails to retrieve data (e.g., video unavailable, private, network error), the application MUST display an appropriate error message (e.g., "Could not retrieve video data. It might be private, unavailable, or requires login.").
*   **FR1.7 (P0):** The backend MUST check if a transcript is available for the video.
*   **FR1.8 (P0):** If a transcript is *not* available for the video, the application MUST inform the user clearly (e.g., "Sorry, a transcript is not available for this video, so it cannot be summarized."). Summarization process should halt.
*   **FR1.9 (P0):** The system SHOULD attempt to detect the primary language of the fetched transcript using metadata from `yt-dlp` if available.
*   **FR1.10 (P0):** Regardless of the original transcript language, the backend MUST instruct the Gemini API to generate the summary in **English**. The prompt sent to Gemini MUST include the full extracted transcript.
*   **FR1.11 (P0):** The application MUST display a loading indicator while the video data is being fetched and processed.

#### 4.2. Summary Generation and Display
*   **FR2.1 (P0):** The application MUST offer three types of summaries:
    *   **Brief:** A very short, concise overview (1-2 sentences).
    *   **Detailed:** A more comprehensive summary covering main sections/arguments (multiple paragraphs).
    *   **Key Points:** A bulleted list of the most important takeaways.
*   **FR2.2 (P0):** Users MUST be able to select the desired summary type before or after generation (if multiple types are generated simultaneously or cached). A default type MUST be configurable in settings (Default: Detailed).
*   **FR2.3 (P0):** The application MUST offer three summary length options, influencing the detail within the selected type (especially for 'Detailed'):
    *   **Short**
    *   **Medium**
    *   **Long**
*   **FR2.4 (P0):** Users MUST be able to select the desired summary length. A default length MUST be configurable in settings (Default: Medium).
*   **FR2.5 (P0):** The backend MUST construct appropriate prompts for the Gemini 2.0 Flash-Lite API based on the selected summary type and length, including the full video transcript.
*   **FR2.6 (P0):** The backend MUST handle the streaming response from the Gemini API (as shown in the example code) and assemble the complete summary text.
*   **FR2.7 (P0):** The application MUST display the generated summary clearly. Each summary display MUST be presented in a card layout containing:
    *   Video Thumbnail (fetched via `yt-dlp`).
    *   Video Title (fetched via `yt-dlp`).
    *   Generated Summary Text.
    *   Actions/Controls (e.g., Read Aloud, Share, Copy, Delete).
    *   Timestamp of generation.
*   **FR2.8 (P0):** The summary text MUST support basic Markdown formatting rendered correctly in the UI:
    *   Bold (`**text**` or `__text__`)
    *   Italics (`*text*` or `_text_`)
    *   Bulleted Lists (`*`, `-`, `+`)
    *   Numbered Lists (`1.`, `2.`)
*   **FR2.9 (P0):** The application MUST provide a mechanism for the user to cancel an in-progress summary generation request (e.g., a 'Cancel' button on the loading indicator/screen). The backend MUST handle cancellation requests gracefully, terminating the API call if possible.
*   **FR2.10 (P0):** The application MUST indicate which summary type and length settings were used to generate the displayed summary.

#### 4.3. Text-to-Speech (TTS) Functionality
*   **FR3.1 (P0):** The application MUST provide a 'Read Aloud' feature for the generated summary text.
*   **FR3.2 (P0):** While reading aloud, the application MUST visually highlight the word currently being spoken.
*   **FR3.3 (P0):** The application MUST automatically scroll the summary text view to keep the currently spoken word visible on the screen.
*   **FR3.4 (P0):** The application MUST provide standard TTS controls:
    *   Play/Start
    *   Pause
    *   Resume (from paused state)
    *   Stop (resetting playback position)
*   **FR3.5 (P0):** The application MUST allow users to customize TTS settings via a dedicated settings screen:
    *   **Speed:** Adjustable rate, up to 16x the normal speed (provide discrete steps or a slider, e.g., 0.5x, 1x, 1.5x, 2x, ... 16x). *Note: Test usability at very high speeds.*
    *   **Pitch:** Adjustable pitch of the voice.
    *   **Voice Selection:** Allow choosing from available system voices (iOS/Android/Web platform specific).
    *   **Volume:** Control TTS playback volume independently or link to system media volume.
*   **FR3.6 (P0):** User-selected TTS settings MUST be persisted across app sessions.
*   **FR3.7 (P1):** The TTS engine SHOULD intelligently handle common Markdown symbols (e.g., ignore `*`, `_`, `#` characters used for formatting rather than reading them aloud; potentially pause slightly at list item markers).

#### 4.4. User Interface and Experience (UI/UX)
*   **FR4.1 (P0):** The application MUST have a modern, clean, and user-friendly interface design.
*   **FR4.2 (P0):** The application MUST support both Dark Mode and Light Mode, automatically adapting to the user's system settings, with an option for manual override in the app settings.
*   **FR4.3 (P0):** Summaries MUST be displayed in a consistent card format as described in FR2.7.
*   **FR4.4 (P0):** The application MUST include a 'History' view where users can see a list of previously generated summaries, ordered chronologically (newest first).
*   **FR4.5 (P0):** Each item in the History view MUST display key information (e.g., Thumbnail, Title, Date/Time of summary) and allow tapping to view the full summary.
*   **FR4.6 (P0):** The application MUST have a dedicated 'Settings' screen allowing configuration of:
    *   Default summary type (Brief, Detailed, Key Points).
    *   Default summary length (Short, Medium, Long).
    *   TTS settings (Speed, Pitch, Voice, Volume).
    *   Dark/Light Mode override.
    *   Option to clear history.
*   **FR4.7 (P0):** The application MUST adhere to accessibility best practices (aiming for WCAG 2.1 Level AA compliance), including sufficient color contrast, touch target sizes, font scaling support, and compatibility with screen readers (e.g., VoiceOver, TalkBack).

#### 4.5. Data Management
*   **FR5.1 (P0):** The backend MUST use a MongoDB database to store summary data.
*   **FR5.2 (P0):** The MongoDB collection for summaries MUST include at least the following fields per document: `_id`, `userId` (if user accounts are implemented later, nullable for now), `youtubeVideoId`, `videoUrl`, `videoTitle`, `videoThumbnailUrl`, `originalTranscriptLanguage`, `summaryType` (Brief/Detailed/Key Points), `summaryLengthSetting` (Short/Medium/Long), `generatedSummaryText`, `generationTimestamp`, `isDeleted` (soft delete flag, optional).
*   **FR5.3 (P0):** Users MUST be able to view their summary history as described in FR4.4.
*   **FR5.4 (P0):** Users MUST be able to delete individual summaries from their history. This can be implemented as a soft delete (setting `isDeleted` to true) or hard delete.
*   **FR5.5 (P1):** Users SHOULD be able to delete all summaries from their history via an option in the Settings screen (with confirmation).
*   **FR5.6 (P0):** User preferences (default summary type/length, TTS settings, theme preference) MUST be persisted locally on the device using appropriate storage mechanisms (e.g., AsyncStorage in React Native).

#### 4.6. Sharing Functionality
*   **FR6.1 (P0):** Users MUST be able to share a generated summary.
*   **FR6.2 (P0):** Sharing options MUST include:
    *   Copying the summary text to the clipboard.
    *   Using the native platform share sheet to send the summary text to other apps (e.g., Mail, Messages, Notes).
*   **FR6.3 (P0):** The shared content MUST include the summary text and SHOULD preface it with context, e.g., "Summary of YouTube video '[Video Title]':\n\n[Generated Summary Text]\n\n(Generated by [App Name])".

### 5. Non-Functional Requirements

#### 5.1. Performance
*   **NFR1.1:** Video metadata and transcript retrieval should ideally complete within 5-10 seconds under normal network conditions.
*   **NFR1.2:** Summary generation time depends on the Gemini API and transcript length but should be clearly indicated to the user via loading states. Aim for completion within 15-30 seconds for typical video lengths (e.g., < 1 hour).
*   **NFR1.3:** The UI must remain responsive during background processing (fetching, summarizing). Use asynchronous operations and loading indicators.
*   **NFR1.4:** Application startup time should be within acceptable platform standards (e.g., < 3 seconds cold start).
*   **NFR1.5:** TTS playback should start promptly (< 1 second delay) after initiation.

#### 5.2. Error Handling
*   **NFR2.1:** All API calls (Backend, Gemini, yt-dlp interactions) must have robust error handling (timeouts, network errors, API errors, invalid data).
*   **NFR2.2:** User-facing errors must be presented clearly and concisely, avoiding technical jargon.
*   **NFR2.3:** Implement logging (client-side and server-side) to aid debugging and monitoring. Sensitive data should be excluded from logs.

#### 5.3. Cross-Platform Compatibility
*   **NFR3.1:** The application must provide a consistent user experience and feature set across iOS, Android, and Web platforms, accounting for platform-specific UI conventions where necessary.
*   **NFR3.2:** Utilize Expo and React Native APIs to maximize code sharing and ensure compatibility.

#### 5.4. Security
*   **NFR4.1:** API keys (Gemini API Key, potentially others) MUST be stored securely on the backend and never exposed in the frontend code.
*   **NFR4.2:** Communication between the frontend app and the backend API MUST use HTTPS.
*   **NFR4.3:** Implement input validation on the backend to prevent injection attacks or malformed requests.
*   **NFR4.4:** Consider rate limiting on backend endpoints to prevent abuse.

#### 5.5. Scalability
*   **NFR5.1:** The backend architecture (FastAPI, MongoDB) should be designed to handle a growing number of users and requests. Consider stateless backend instances and scalable database solutions (e.g., MongoDB Atlas).

#### 5.6. Accessibility
*   **NFR6.1:** Adhere to WCAG 2.1 Level AA guidelines as specified in FR4.7. This includes semantic HTML for web, appropriate ARIA roles/labels, and compatibility with assistive technologies.

#### 5.7. Offline Functionality
*   **NFR7.1:** Previously generated and viewed summaries stored in the history MUST be accessible offline.
*   **NFR7.2:** Generating new summaries requires an active internet connection. The app should gracefully handle offline scenarios when attempting to generate a new summary.

### 6. API Integration Details

#### 6.1. Gemini 2.0 Flash-Lite API
*   **Integration Point:** FastAPI Backend (Python Service)
*   **Library:** `google-genai` Python SDK.
*   **Authentication:** Use API Key authentication. The key must be securely managed (e.g., environment variables, secret manager).
*   **Model:** Specify `gemini-2.0-flash-lite`.
*   **Input:** The primary input (`contents`) will be the full text transcript obtained from `yt-dlp`. The prompt should clearly instruct the model on the desired action (summarize), the type of summary (Brief, Detailed, Key Points), and the desired length (Short, Medium, Long), and explicitly state the output language must be English.
*   **Configuration:**
    *   `response_mime_type="text/plain"` (or `application/json` if structured output is preferred, though text is simpler for summaries).
    *   Use streaming (`generate_content_stream`) for better perceived performance on the client-side (allows displaying text as it arrives, though requires frontend support). Alternatively, use non-streaming `generate_content` for simplicity if streaming UI is not implemented.
    *   Consider setting `temperature` and `top_p` for controlling creativity vs. factuality if needed (start with defaults).
    *   Implement error handling for API exceptions (e.g., `google.api_core.exceptions.GoogleAPICallError`).
*   **Reference Code (Backend Implementation Context):** The provided Python script serves as a basic example for calling the API within a FastAPI endpoint.

```python
# Example snippet within a FastAPI route handler
# Assuming 'transcript_text', 'summary_type', 'summary_length' are parameters

import os
from google import genai
from google.genai import types
import logging # Use proper logging

# Configure API Key securely (e.g., from env var)
try:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
except KeyError:
    logging.error("GEMINI_API_KEY environment variable not set.")
    # Raise appropriate HTTP exception in FastAPI
    raise HTTPException(status_code=500, detail="AI service configuration error.")
except Exception as e:
     logging.error(f"Error configuring GenAI: {e}")
     raise HTTPException(status_code=500, detail="AI service initialization error.")

async def generate_summary_from_gemini(transcript_text: str, summary_type: str, summary_length: str) -> str:
    model_name = "gemini-2.0-flash-lite" # Or the latest recommended equivalent
    model = genai.GenerativeModel(model_name)

    # Construct the prompt based on parameters
    prompt = f"""Please summarize the following YouTube video transcript.
Transcript:
\"\"\"
{transcript_text}
\"\"\"

Generate a summary that meets these criteria:
1. Summary Type: {summary_type} (Options: Brief, Detailed, Key Points)
2. Summary Length: {summary_length} (Options: Short, Medium, Long)
3. Output Language: English
4. Format: Use basic Markdown for structure (like bullet points for Key Points).

Summary:"""

    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=prompt)],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        # Add temperature, top_p etc. if needed
    )

    try:
        # Using non-streaming version for simplicity here,
        # but streaming is preferred for better UX if frontend supports it.
        response = await model.generate_content_async(
            contents=contents,
            generation_config=generate_content_config,
        )
        # Add robust checks for safety ratings and empty responses
        if not response.candidates or not response.candidates[0].content.parts:
             logging.warning(f"Gemini returned no content for prompt: {prompt[:100]}...")
             raise HTTPException(status_code=500, detail="AI model failed to generate summary.")

        summary_text = response.text
        return summary_text

    except Exception as e:
        logging.error(f"Error calling Gemini API: {e}")
        # Handle specific API errors (rate limits, invalid args, etc.)
        raise HTTPException(status_code=502, detail=f"AI service communication error: {e}")

# FastAPI endpoint would call this function
```

#### 6.2. YouTube Data Extraction (yt-dlp)
*   **Integration Point:** FastAPI Backend (Python Service)
*   **Method:** Use the `yt-dlp` Python library directly within the FastAPI application or execute `yt-dlp` as a subprocess. Using the library is generally preferred for better control and error handling.
*   **Functionality:**
    *   Fetch video metadata (title, thumbnail URL, duration, channel, language).
    *   Fetch available automatic speech recognition (ASR) transcripts (prefer English if available, otherwise take the primary available one).
    *   Specify transcript format (e.g., plain text, JSON).
*   **Error Handling:** Handle cases where `yt-dlp` fails (video not found, private, region-locked, no transcript available). Return appropriate error codes/messages to the frontend.
*   **Dependencies:** Ensure `yt-dlp` and its dependencies (like `ffmpeg` if needed for certain operations, though likely not for transcripts) are installed in the backend environment.

### 7. UI/UX Specifications

#### 7.1. Key Screens & Flow
1.  **Input Screen:**
    *   Prominent text input field for YouTube URL.
    *   Paste button (optional, convenience).
    *   "Summarize" button.
    *   Maybe options to select Summary Type/Length upfront (or set defaults in Settings).
    *   Access to History and Settings.
2.  **Loading/Processing State:**
    *   Displayed after pressing "Summarize".
    *   Clear indicator (e.g., spinner, progress bar).
    *   Text indicating status (e.g., "Fetching video info...", "Generating summary...").
    *   Cancel button (FR2.9).
3.  **Summary Display Screen:**
    *   Card layout (FR2.7) with Thumbnail, Title.
    *   Scrollable area for the generated summary text.
    *   Clearly indicated Summary Type/Length used.
    *   Action buttons: Read Aloud (Play/Pause/Stop controls appear), Copy Text, Share, Delete (if viewed from History).
    *   Option to re-generate with different Type/Length settings.
4.  **History Screen:**
    *   List of past summaries (Thumbnail, Title, Timestamp).
    *   Scrollable list.
    *   Tap item to navigate to Summary Display Screen for that item.
    *   Swipe-to-delete or Edit mode for deletion (FR5.4).
    *   Option to clear all history (likely in Settings or via an action button here).
5.  **Settings Screen:**
    *   Organized sections for:
        *   Default Summary Settings (Type, Length - using pickers/radio buttons).
        *   TTS Settings (Sliders for Speed/Pitch, Picker for Voice, Slider/Toggle for Volume).
        *   Appearance (Theme: System/Light/Dark).
        *   Data Management (Clear History button with confirmation).
        *   About/Help section (optional).

#### 7.2. Navigation
*   Use a standard mobile navigation pattern (e.g., Tab Bar for Input/History/Settings or a Stack Navigator). React Navigation library recommended.
*   Clear back navigation from Summary/Settings screens.

#### 7.3. Input Methods
*   Standard text input for URL pasting.
*   System Share Sheet integration for receiving URLs (iOS/Android).
*   Buttons, sliders, pickers for settings and controls.

#### 7.4. Feedback Mechanisms
*   **Loading:** Spinners, progress indicators.
*   **Success:** Display of summary, subtle confirmation messages (e.g., "Text Copied").
*   **Error:** User-friendly modal dialogs or inline messages explaining the issue (FR1.4, FR1.6, FR1.8).
*   **TTS:** Visual word highlighting, state changes on Play/Pause buttons.

#### 7.5. Design System/Style Guide
*   Leverage a React Native UI component library (e.g., React Native Paper, UI Kitten, or a custom setup with NativeWind/Tailwind) for consistency.
*   Define primary/secondary colors, typography (font sizes, weights), spacing, and iconography.
*   Ensure components adapt correctly to Dark/Light modes.

### 8. Implementation Guidelines

#### 8.1. Frontend Development (React Native Expo)
*   Use functional components and Hooks.
*   Employ strong typing with TypeScript.
*   Use a state management library (e.g., Zustand, Redux Toolkit) for managing global state like user preferences, history list, and current summary data.
*   Follow Expo best practices for build and deployment (EAS Build).
*   Implement platform-specific adaptations only where necessary.

#### 8.2. Backend Development (FastAPI)
*   Use asynchronous programming (`async`/`await`) extensively for I/O-bound operations (API calls, DB access).
*   Structure the project logically (e.g., routers, services, models).
*   Use Pydantic for data validation and serialization.
*   Implement dependency injection for managing resources like DB connections and API clients.
*   Follow Python best practices (e.g., PEP 8, type hinting).
*   Containerize the application using Docker for consistent deployment.

#### 8.3. Testing
*   **Unit Tests:** Cover critical functions/logic in both frontend (components, utils) and backend (API logic, data processing). Use frameworks like Jest (Frontend) and Pytest (Backend).
*   **Integration Tests:** Test interactions between components (e.g., frontend state <-> UI) and backend services (e.g., API endpoint -> service -> DB/external API call mocking).
*   **End-to-End (E2E) Tests:** Simulate user flows across the entire stack (App -> Backend -> DB/APIs). Frameworks like Detox or Maestro (Frontend) can be used. Test key scenarios like submitting a URL, viewing summary, using TTS, changing settings.
*   **Manual Testing:** Perform thorough manual testing on target devices (iOS/Android) and web browsers, focusing on usability, edge cases, and platform consistency. Test with various YouTube video types (long, short, different languages, unavailable transcripts).

#### 8.4. Documentation
*   **Code Comments:** Document complex logic, component props, and function signatures.
*   **API Documentation:** Auto-generate OpenAPI (Swagger) documentation for the FastAPI backend.
*   **README:** Include setup instructions, architecture overview, and deployment steps in project README files.

### 9. Delivery Requirements
*   This project requires the delivery of a **production-ready** solution.
*   All features defined in Section 4 (Core Features and Functional Requirements) marked as P0 MUST be fully implemented, functional, and tested across all target platforms (iOS, Android, Web).
*   Non-Functional Requirements (Section 5) must be met.
*   The application must be stable, performant, and provide a polished user experience.
*   Comprehensive testing (Unit, Integration, E2E, Manual) must be completed.
*   Required documentation (Code, API, READMEs) must be provided.
*   This is explicitly **not** an MVP (Minimum Viable Product); feature completeness and quality are paramount.

### 10. Open Issues / Future Considerations
*   **User Accounts:** Implement user accounts for syncing history and preferences across devices.
*   **Language Support:** Offer summary generation *in* other languages besides English (depends on Gemini capabilities and transcript availability).
*   **Transcript Display:** Option to view the full transcript alongside the summary.
*   **Advanced Summary Customization:** Allow users to provide custom prompts or tweak AI parameters.
*   **Batch Processing:** Allow summarizing multiple URLs at once.
*   **Cost Monitoring:** Implement monitoring for Gemini API usage costs. Set budget alerts if possible.
*   **yt-dlp Updates:** Plan for keeping the `yt-dlp` library updated as YouTube's internal structure changes frequently.
*   **TTS Voice Quality:** Explore premium TTS services if system voices are insufficient.
*   **Video Download:** (Out of Scope for now) Feature to download the video for offline viewing.

---
This PRD provides a comprehensive foundation for the development team. Further clarifications should be sought if any requirement is ambiguous.



pip install google-genai
```import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.0-flash-lite"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()

```
