
# Prompt for Generating a Product Requirements Document (PRD)

Please create a comprehensive Product Requirements Document (PRD) for a cross-platform mobile application that summarizes YouTube videos using Gemini 2.0 Flash-Lite AI. The PRD should be professionally formatted with clear section headers, subsections, and numbered requirements following standard PRD conventions. The document should be suitable for presentation to development teams.

## Product Overview
Create a detailed overview section that describes:
- The purpose of the application (summarizing YouTube videos)
- Target platforms (iOS, Android, and web via React Native Expo)
- Key value proposition for users
- Primary user personas

## System Architecture
Detail the complete technical architecture including:
- Frontend: React Native Expo app using JavaScript
- Backend: FastAPI Python framework with RESTful endpoints
- AI Integration: Gemini 2.0 Flash-Lite for video content summarization
- Database: MongoDB for storing video summaries and user preferences
- External Services: YouTube data extraction using yt-dlp library

## Core Features and Functional Requirements
Please structure each feature with numbered requirements (e.g., FR1.1, FR1.2) with clear priority indicators:

### 1. YouTube Video Input and Processing
- Methods for providing YouTube links (direct paste, share from YouTube app)
- Link validation requirements and error handling
- Video metadata extraction (title, thumbnail, etc.)
- Handling videos without available transcripts
- Transcript language handling (supporting multiple languages, always providing English summaries)

### 2. Summary Generation and Display
- Summary types (Brief, Detailed, Key Points) with default settings
- Summary length options (Short, Medium, Long) with default configurations
- Gemini 2.0 Flash-Lite API integration details
- Summary display format (card layout with specific elements)
- Markdown formatting requirements
- Cancellation of in-progress summary generation

### 3. Text-to-Speech Functionality
- Read aloud feature implementation with text highlighting
- Word-by-word highlighting requirements
- Auto-scrolling text as it's being read
- TTS control options (start, pause, resume, stop)
- TTS settings customization (speed up to 16x, pitch, voice selection, volume)
- Handling of markdown symbols during reading

### 4. User Interface and Experience
- Overall design philosophy (modern, user-friendly)
- Dark/light mode support
- Summary card format and contents
- History view implementation
- Settings screen organization
- Accessibility considerations

### 5. Data Management
- MongoDB schema for storing summaries
- History management (viewing, deleting summaries)
- User preferences persistence

### 6. Sharing Functionality
- Methods for sharing generated summaries
- Format of shared content

## Non-Functional Requirements
Include sections on:
- Performance expectations
- Error handling approach
- Cross-platform compatibility requirements
- Security considerations
- Offline functionality (if any)

## API Integration Details
Provide the exact implementation details for:
- Gemini 2.0 Flash-Lite API integration
- YouTube data extraction using yt-dlp
- Any other external services

Include the provided code example for Gemini API integration as reference.

## UI/UX Specifications
Detail the exact user interface elements, flows, and interactions:
- Screen mockups or detailed descriptions
- Navigation patterns
- Input methods
- Feedback mechanisms

## Implementation Guidelines
- Frontend development standards and best practices
- Backend implementation requirements
- Testing requirements
- Documentation standards

## Delivery Requirements
Specify that this is a production-ready solution, not an MVP, with all features fully implemented and tested.

Please ensure the PRD is comprehensive, well-organized, and provides all the necessary details for the development team to create this application without requiring additional clarification.

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
