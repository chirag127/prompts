

**Understanding Your QR Scanner App Idea**

1.  **The Core Idea:** At its heart, what is the main purpose of this QR code scanning app? What specific problem are you trying to solve or what need are you trying to fill for the end-user? What makes it unique or better than existing scanners (if applicable)?
answer: The main purpose of this QR code scanning app is to provide a simple and efficient way for users to scan QR codes and access the information they contain. It aims to be user-friendly and accessible, with a focus on speed and accuracy. It should be able to handle a wide variety of QR codes, including URLs, contact information, Wi-Fi networks, and more. The app should also have a clean and modern design, with a simple interface that makes it easy for users to navigate and utilize the features effectively.
2.  **Post-Scan Action:** This is key! What exactly should happen *right after* a QR code is successfully scanned?
    *   Just display the raw text/data found in the code?
    *   Automatically detect the type of data (URL, contact, Wi-Fi, text) and offer relevant actions? (e.g., 'Open URL', 'Add Contact', 'Connect to Wi-Fi')
    *   Automatically perform the primary action (like opening a URL in a browser)?
    *   Give the user a choice of actions?
    *   Copy the content to the clipboard automatically or provide a button?
answer: The main purpose of this QR code scanning app is to provide a simple and efficient way for users to scan QR codes and access the information they contain. It aims to be user-friendly and accessible, with a focus on speed and accuracy. It should be able to handle a wide variety of QR codes, including URLs, contact information, Wi-Fi networks, and more. The app should also have a clean and modern design, with a simple interface that makes it easy for users to navigate and utilize the features effectively.
answer: The target audience for this app includes the general public, professionals who frequently use QR codes, and event attendees who may need to scan codes for information or access.
 This helps shape the user experience.
4.  **User Interface (UI) & Experience (UX):**
    *   How do you imagine the app looking and feeling? Should it be super simple and minimalist, or have more features visible? Any specific branding, colors, or style in mind?
    
    *   What should the main scanning screen look like? (e.g., full camera view, a specific scanning window/reticle?)
    *   What kind of feedback should the user get during the process? (e.g., visual cues for aiming, sound/vibration on successful scan, clear error messages?)
    *   Do you have any sketches, wireframes, or even just a napkin drawing you could describe?
5.  **Scan History & Data:**
    *   Does the app need to keep a history of previously scanned QR codes?
    *   If yes, what information should be stored for each scan (e.g., content, date/time, type)? How should this history be presented to the user?
    *   Should this history be searchable or filterable?
    *   *(This impacts data storage choices. For simple history, **MMKV** is great for fast local storage. If data needs syncing, we'd need a different approach.)*
6.  **User Accounts & Authentication:**
    *   Do users need to create accounts or log in to use the app?
    *   If yes, what is the reason? (e.g., syncing scan history across devices, accessing premium features?)
    *   *(If accounts are needed, **Clerk** is an excellent option as you suggested, handling login, signup, social providers, etc. If not, we can skip this complexity.)*
7.  **QR Code Types:** Are there specific types of QR codes it absolutely *must* handle well (e.g., URLs, vCards, Wi-Fi)? Are there any it should ignore or handle differently?
8.  **Error Handling:** How should the app behave if:
    *   The camera can't read the QR code (blurry, damaged, poor lighting)?
    *   The QR code contains invalid or unexpected data?
    *   The user denies camera permission? (We'll need to guide them on how to enable it).
9.  **Permissions:** Besides camera permission, are there any other permissions needed? (e.g., location if you want to tag scans, contacts if adding contacts directly).
10. **Technical Stack Preferences:** You mentioned a specific stack (Expo, Expo Router, NativeWind, Reanimated, Maestro/RNTL, Sentry/Bugsnag, MMKV, React Hook Form, Expo Image, Zego, Clerk, Gesture Handler, Vision Camera).
    *   Are all these intended for the initial version, or are some for future plans? For example, is **React Hook Form** needed if there are no complex forms initially? Is **Clerk** needed if there are no user accounts? Is **Zego** needed if there aren't complex dropdowns/menus planned right away?
    *   *(This helps me tailor the PRD's recommendations realistically. For the core scanning, **Expo**, **Expo Router**, **React Native Vision Camera**, **NativeWind** (for styling), and **Sentry/Bugsnag** (for monitoring) seem most critical from your list. We can definitely include others if features warrant them.)*
11. **Performance & Reliability:** What are your expectations for speed? How quickly should the camera open and be ready to scan? How fast should the scan detection be? Is offline functionality important (beyond the scanning itself)?
12. **Third-Party Integrations:** Other than potentially opening links in a web browser or interacting with the OS (like adding contacts or Wi-Fi), does the app need to connect to any other external services or APIs?
13. **Scalability & Future:**
    *   Are you planning for a large number of users right away, or is it expected to grow over time? (The proposed Expo/React Native stack scales well).
    *   Do you have any future features in mind, even if they're not for the first version? (e.g., QR code generation, batch scanning, advanced data parsing, sharing scanned codes).
14. **Key Goal & Success:** If you could only pick one thing, what's the absolute most important goal for the *first* version of this app? How will you know if the app is successful?

---

Take your time answering these. The more detail you provide, the better I can understand your vision and the more accurate the resulting PRD blueprint will be. I'm excited to hear your thoughts! Once you've shared your answers, I'll confirm my understanding and then generate that PRD for you.