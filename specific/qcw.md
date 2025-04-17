Okay, here is a Product Requirements Document (PRD) for the "Call Waiter" feature, incorporating the details from your request and the clarified answers.

---

**Product Requirements Document: Call Waiter Feature**

**1. Introduction**

This document outlines the requirements for implementing a "Call Waiter" feature within the `qrsay` restaurant user frontend (`digitalMenu/src/app/restaurant`). This feature will allow customers viewing a specific restaurant's menu to request assistance from a waiter by submitting a simple form. The request will trigger notifications on the backend and admin interface.

**2. Goals**

*   Provide a convenient way for customers to request waiter assistance without leaving their table or interrupting their browsing experience.
*   Improve customer service responsiveness within restaurants using the platform.
*   Streamline the communication of service requests from customers to restaurant staff.
*   Provide restaurant staff (via the Admin interface) with real-time alerts for assistance requests.

**3. Target Audience**

*   **Restaurant Customers:** Users browsing the restaurant's menu on the `qrsay` platform who require assistance.
*   **Restaurant Staff/Managers:** Users monitoring the `qrsay` Admin interface (`digitalMenu/src/app/admin`) who need to be notified of customer requests.

**4. Requirements**

**4.1. User Frontend (Restaurant View - `digitalMenu/src/app/restaurant`)**

*   **4.1.1. Button Appearance & Placement:**
    *   A new button labeled **"Call Waiter"** shall be added to the main header (`mat-toolbar`) of the restaurant view.
    *   Placement: As indicated in the provided image (typically towards the right side of the header).
    *   Styling: The button's appearance (color, font, size, padding) must match the existing theme and style of other buttons in the `mat-toolbar`.
*   **4.1.2. Button Visibility:**
    *   The "Call Waiter" button shall **only** be visible when the user is actively viewing a specific restaurant's page/menu.
    *   The button shall **only** be visible if the currently viewed restaurant has one or more tables configured. The frontend should determine this by checking if the loaded restaurant data contains a non-empty list/array of tables.
*   **4.1.3. Modal Trigger:**
    *   Clicking the "Call Waiter" button shall open a modal dialog window.
*   **4.1.4. Modal Content & Form:**
    *   The modal shall contain a form with the following fields:
        *   **Name:** (Text Input) - Mandatory field. Label: "Your Name".
        *   **Table Number:** (Select Dropdown) - Mandatory field. Label: "Select Your Table".
            *   Options: Populated dynamically with the list of table names/numbers available for the current restaurant. The value associated with each option should be the Table `ID`.
        *   **Message:** (Text Area) - Optional field. Label: "Optional Message (e.g., need water, ready to order)".
    *   The modal shall have a clear title, e.g., "Call Waiter".
    *   The modal shall contain a "Submit" button to submit the form.
    *   The modal shall contain a "Cancel" button or a close icon (X) to dismiss the modal without submitting.
*   **4.1.5. Form Validation:**
    *   Client-side validation must be implemented.
    *   The "Name" and "Table Number" fields are required.
    *   If the user tries to submit with missing required fields, clear error messages shall be displayed beneath the respective fields, and the form submission should be prevented.
*   **4.1.6. Form Submission & API Interaction:**
    *   Upon clicking the "Submit" button (and successful validation):
        *   An HTTP POST request shall be made to the backend endpoint: `/api/callWaiter`.
        *   The request payload (body) must be JSON and include:
            *   `name` (String): Value from the Name field.
            *   `tableId` (String/Number): The `ID` of the selected table.
            *   `message` (String): Value from the Message field (send an empty string or omit if empty).
            *   `restaurantId` (String/Number): The ID of the current restaurant being viewed. This needs to be retrieved from the current application state/route.
        *   The request should be sent using `axios` (or the project's standard HTTP client).
*   **4.1.7. Loading State:**
    *   While the API request is in progress (after clicking "Submit" and before receiving a response), the "Submit" button should be disabled, and a visual loading indicator (e.g., spinner) should be displayed on or next to the button.
*   **4.1.8. Success Handling:**
    *   Upon receiving a successful response (e.g., HTTP 200/201) from the backend:
        *   A success message (e.g., "Waiter called successfully!") shall be displayed *within* the modal.
        *   The loading indicator shall disappear.
        *   The form fields might be cleared or disabled.
        *   The modal shall automatically close after a short delay (e.g., 3 seconds).
*   **4.1.9. Error Handling:**
    *   Upon receiving an error response from the backend (e.g., HTTP 4xx, 5xx):
        *   An informative error message (based on the backend response, or a generic one like "Failed to call waiter. Please try again.") shall be displayed *within* the modal.
        *   The loading indicator shall disappear, and the "Submit" button should become active again.
        *   The modal should remain open, allowing the user to correct potential issues or try again.
*   **4.1.10. Responsiveness:**
    *   The modal and its form elements must be responsive and display correctly on both desktop and mobile screen sizes.
*   **4.1.11. Styling:**
    *   The modal dialog (background, borders, fonts, colors) and its form elements (inputs, buttons, dropdown) must adhere to the overall visual theme and styling guidelines of the `qrsay` application. Use Angular Material components (`MatDialog`, `MatFormField`, `MatInput`, `MatSelect`, `MatButton`, etc.) appropriately.

**4.2. Backend (`qrsayBackend`)**

*   **4.2.1. API Endpoint:**
    *   Create a new API endpoint: `POST /api/callWaiter`.
*   **4.2.2. Request Handling & Validation:**
    *   The endpoint must expect a JSON request body containing `name`, `tableId`, `message` (optional), and `restaurantId`.
    *   Perform backend validation:
        *   Ensure `name`, `tableId`, and `restaurantId` are present and have valid formats.
        *   Verify that the `restaurantId` corresponds to an existing restaurant.
        *   Verify that the `tableId` corresponds to an existing table belonging to that `restaurantId`.
    *   If validation fails, return an appropriate HTTP error response (e.g., 400 Bad Request) with a descriptive error message.
*   **4.2.3. Data Storage:**
    *   Upon successful validation, store the waiter call request in the database.
    *   Create a new database table named `waiter_calls`.
    *   Required columns:
        *   `id` (Primary Key, Auto-increment)
        *   `restaurant_id` (Foreign Key to Restaurants table)
        *   `table_id` (Foreign Key to Tables table)
        *   `customer_name` (String)
        *   `message` (Text, Nullable)
        *   `status` (String, e.g., 'new', 'acknowledged', 'resolved' - default to 'new')
        *   `created_at` (Timestamp)
        *   `updated_at` (Timestamp)
    *   Insert a new record with the received data (`restaurant_id`, `table_id`, `customer_name`, `message`), setting `status` to 'new' and populating timestamps.
*   **4.2.4. Real-time Notification (Admin Interface):**
    *   After successfully saving the request to the database:
        *   Use `socket.io` to emit a real-time event.
        *   The event should be targeted specifically to the admin users connected for the relevant restaurant (e.g., emit to a room named `restaurant_{restaurantId}`).
        *   The event name should be descriptive (e.g., `new_waiter_call`).
        *   The event payload should include necessary details for the admin interface:
            *   `callId` (the ID of the newly created record in `waiter_calls`)
            *   `restaurantId`
            *   `tableId`
            *   `tableName` (Fetch the table name/number based on `tableId` for easier display)
            *   `customerName`
            *   `message`
            *   `timestamp` (`created_at`)
*   **4.2.5. Email Notification:**
    *   After successfully saving the request, retrieve the designated manager's email address associated with the `restaurantId`.
    *   Send an email notification to the manager's email address.
    *   The email subject should be clear (e.g., "Waiter Request at [Restaurant Name] - Table [Table Name]").
    *   The email body should contain the call details: Customer Name, Table Name, Message (if provided), Time of Request.
    *   Handle potential email sending failures gracefully (log the error but do not necessarily prevent the success response to the frontend if the primary actions succeeded).
*   **4.2.6. Response Handling:**
    *   If all steps (validation, DB save, notifications) are successful (or primary steps are successful even if email fails), return an HTTP 200 OK or 201 Created response to the frontend with a JSON body: `{ "success": true, "message": "Waiter called successfully." }`.
    *   If any critical step fails (validation, DB save), return an appropriate error response (e.g., 400, 500) with a JSON body: `{ "success": false, "message": "Error description..." }`.
*   **4.2.7. Rate Limiting:**
    *   Implement basic rate limiting on the `/api/callWaiter` endpoint to prevent abuse. For example, limit requests per IP address or user session (if applicable) within a specific time window (e.g., 3 calls per 5 minutes).
    *   If the rate limit is exceeded, return an HTTP 429 Too Many Requests status code.

**4.3. Admin Frontend (`digitalMenu/src/app/admin`)**

*   **4.3.1. Notification Reception:**
    *   The admin frontend must listen for the `new_waiter_call` event via its `socket.io` connection.
    *   Ensure the client joins the correct room (e.g., `restaurant_{restaurantId}`) upon loading the admin interface for a specific restaurant.
*   **4.3.2. Notification Display:**
    *   Upon receiving a `new_waiter_call` event:
        *   A real-time notification should be displayed within the "My Orders" dashboard section (or a more relevant section if "My Orders" is not suitable; potentially a dedicated notification area or panel).
        *   The notification should clearly indicate a new waiter call and display key information received in the event payload (Table Name, Customer Name, Message, Time).
        *   Consider adding a visual indicator (e.g., a badge count on a "Notifications" or "Waiter Calls" menu item) that increments with new, unread calls.
        *   (Future Enhancement: Allow staff to "Acknowledge" or "Resolve" the call via the UI, which would update the status in the backend and potentially remove the notification).

**5. Clarifications (Based on Q&A)**

*   **Backend Storage:** Waiter calls will be stored in a new `waiter_calls` database table.
*   **Backend Notification:** Real-time notification via `socket.io` to the Admin frontend is required. Email notification to the restaurant manager is also required.
*   **Notification Data:** Include Timestamp, Restaurant ID, Name, Table (ID and potentially Name), and Message.
*   **Restaurant Identification:** The frontend must send the `restaurantId` in the `/api/callWaiter` request.
*   **Admin Interface:** Notifications will be integrated into the existing Admin panel, specifically displayed within the "My Orders" dashboard area.
*   **Table Value:** The frontend will send the Table `ID` to the backend.
*   **Button Visibility Data:** Frontend checks if the loaded restaurant data object includes a list/array of tables.
*   **User Name Field:** The "Name" field will always be manually entered by the customer.
*   **Loading Indicator:** A loading indicator is required on the modal's submit button during the API call.
*   **Success Feedback:** The success message will appear within the modal, which will then auto-close after a few seconds.
*   **Rate Limiting:** Rate limiting is required to prevent abuse.

**6. Success Metrics**

*   Number of successful "Call Waiter" requests initiated per day/week/restaurant.
*   Successful delivery rate of `socket.io` notifications to the Admin interface (monitored via backend logs).
*   Successful delivery rate of email notifications (monitored via backend logs/email service).
*   Qualitative feedback from restaurant owners/managers on the usefulness and reliability of the feature.
*   Qualitative feedback from restaurant customers (if feedback mechanisms exist).

**7. Future Considerations / Potential Enhancements**

*   Admin UI for managing waiter calls (acknowledging, resolving, viewing history).
*   Push notifications to a dedicated staff mobile app.
*   Allowing pre-filling the "Name" field if a user authentication system is implemented.
*   More granular notification preferences for restaurant managers/staff.
*   Reporting on waiter call frequency and response times (requires tracking acknowledgment/resolution).

**8. Out of Scope (For this iteration)**

*   Building a full CRUD interface in the Admin panel for managing `waiter_calls` records (beyond displaying the initial notification).
*   Tracking the acknowledgment or resolution status of calls *in the UI*.
*   SMS notifications.
*   User authentication integration for pre-filling name.

---