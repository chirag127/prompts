Okay, here is the Product Requirements Document (PRD) for the "Call Waiter" feature in the qrsay platform, based on the provided specifications and clarifications.

---

## Product Requirements Document: Call Waiter Feature

**Version:** 1.0
**Date:** 2023-10-27
**Author:** [Your Name/Team]
**Status:** Proposed

**1. Introduction**

This document outlines the requirements for implementing a "Call Waiter" feature within the qrsay restaurant digital menu platform. This feature aims to enhance the customer experience by providing a simple and direct way for diners to request assistance from restaurant staff via the user-facing digital menu. Staff will receive these requests in real-time through the qrsay admin panel.

**2. Goals**

* Allow restaurant customers to easily request waiter assistance directly from the digital menu interface.
* Provide restaurant staff with real-time notifications of waiter requests via the admin panel.
* Improve customer service efficiency and responsiveness in restaurants using the qrsay platform.
* Seamlessly integrate the feature into the existing user and admin frontends and backend infrastructure.

**3. User Stories**

* **As a customer** using the qrsay digital menu at a restaurant, I want to tap a "Call Waiter" button, enter my name, select my table, and optionally add a message, so that I can quickly request assistance without needing to physically flag down staff.
* **As a restaurant staff member** monitoring the qrsay admin panel, I want to receive instant notifications for waiter calls, including the customer's name, table number, and any specific message, so that I can promptly attend to the customer's needs within the "My Orders" dashboard area.

**4. Functional Requirements**

**4.1. Restaurant Frontend (User Interface - `digitalMenu\src\app\restaurant`)**

* **4.1.1. "Call Waiter" Button:**
  * A new button labeled "Call Waiter" will be added to the main header (`mat-toolbar`).
  * The button must be positioned on the right side of the header, immediately to the left of the existing Cart button/icon.
  * The button should include a relevant icon (e.g., Material Icons `support_agent`, `pan_tool`, or `record_voice_over`) for better visibility alongside the text "Call Waiter".
  * The button's styling (color, size, font) must match the existing theme and header buttons.
* **4.1.2. Button Visibility:**
  * The "Call Waiter" button shall *only* be visible when the user is viewing a specific restaurant's menu page.
  * The button shall *only* be visible if the restaurant data loaded on the frontend contains a non-empty array of tables (e.g., `restaurant.tables && restaurant.tables.length > 0`).
* **4.1.3. Modal Trigger:**
  * Clicking the "Call Waiter" button shall open a modal dialog.
* **4.1.4. Modal Dialog:**
  * The modal must be responsive, displaying correctly on both desktop and mobile devices.
  * The modal styling must be consistent with the overall application theme (using Angular Material components like `MatDialog`).
  * The modal shall contain a form with the following elements:
    * **Title:** e.g., "Call Waiter"
    * **Name Field:** A required text input field (`mat-input`) labeled "Your Name".
    * **Table Number Field:** A required dropdown/select field (`mat-select`) labeled "Select Your Table".
      * This dropdown must be populated with the list of tables associated with the current restaurant.
      * The `value` for each option should be the unique Table ID.
      * The displayed text for each option should be the Table Name/Number.
    * **Message Field:** An optional multi-line text area (`mat-textarea`) labeled "Message (Optional)".
    * **Submit Button:** A button labeled "Call Waiter" or "Submit Request".
    * **Close Button:** A standard way to close the modal (e.g., 'X' icon button or a "Cancel" button).
* **4.1.5. Form Validation:**
  * Client-side validation must be implemented.
  * The "Name" field cannot be empty.
  * The "Table Number" field must have a selection.
  * Appropriate error messages (e.g., using `mat-error`) must be displayed beneath the respective fields if validation fails upon attempting to submit the form.
* **4.1.6. Form Submission:**
  * Upon clicking the Submit button and passing validation:
    * A loading indicator (e.g., `mat-spinner` overlay or button `disabled` state with spinner) must be displayed on the Submit button to indicate processing.
    * An asynchronous HTTP POST request must be sent to the backend API endpoint `/api/callWaiter` using `axios`.
    * The request payload must include:
      * `restaurantId`: The ID of the current restaurant.
      * `name`: The value entered in the Name field.
      * `tableId`: The selected Table ID from the dropdown.
      * `message`: The value entered in the Message field (or an empty string/null if left blank).
* **4.1.7. Submission Feedback:**
  * **On Success (Backend confirms):**
    * The loading indicator on the Submit button must be removed.
    * A success message (e.g., "Waiter has been called successfully!") shall be displayed *within* the modal.
    * The modal shall automatically close after a short delay (e.g., 2-3 seconds) after displaying the success message.
  * **On Error (Backend returns error or network issue):**
    * The loading indicator on the Submit button must be removed.
    * An appropriate error message (e.g., "Failed to call waiter. Please try again." or the specific error message from the backend) shall be displayed *within* the modal.
    * The modal shall *not* close automatically on error, allowing the user to correct input or retry.

**4.2. Backend (`qrsayBackend`)**

* **4.2.1. API Endpoint:**
  * Create a new API endpoint: `POST /api/callWaiter`.
* **4.2.2. Request Handling:**
  * The endpoint must receive the JSON payload containing `restaurantId`, `name`, `tableId`, and optional `message`.
* **4.2.3. Input Validation:**
  * Validate the incoming data:
    * `restaurantId` must exist and be valid.
    * `name` must be a non-empty string.
    * `tableId` must exist, be valid, and belong to the specified `restaurantId`.
    * `message` (if provided) should be a string.
  * Return appropriate HTTP status codes (e.g., 400 Bad Request) with clear error messages if validation fails.
* **4.2.4. Rate Limiting:**
  * Implement rate limiting on the `/api/callWaiter` endpoint to prevent abuse. This could be based on IP address, `restaurantId`, or `tableId` (e.g., max 1 call per table per 60 seconds).
  * Return an HTTP 429 Too Many Requests status code if the rate limit is exceeded.
* **4.2.5. Data Processing & Storage:**
  * Generate a timestamp for the call.
  * Retrieve the corresponding table name/number using the `tableId` and `restaurantId`.
  * Store the waiter call details in a new database table named `waiter_calls`.
* **4.2.6. Database Table (`waiter_calls`):**
  * Create a new table `waiter_calls` with at least the following columns:
    * `id` (Primary Key, Auto-increment)
    * `restaurant_id` (Foreign Key referencing `restaurants.id`)
    * `table_id` (Foreign Key referencing `tables.id`)
    * `customer_name` (VARCHAR, Not Null)
    * `table_name_at_call` (VARCHAR, Not Null - Stores the table name/number at the time of the call)
    * `message` (TEXT, Nullable)
    * `call_timestamp` (TIMESTAMP/DATETIME, Not Null, Default CURRENT_TIMESTAMP)
    * `status` (VARCHAR/ENUM, e.g., 'pending', 'acknowledged', 'resolved', Default 'pending' - For future use)
* **4.2.7. Real-time Notification (Socket.io):**
  * Upon successful storage of the waiter call in the database:
    * Emit a Socket.io event (e.g., `new_waiter_call`) to a specific room/namespace associated with the `restaurantId`.
    * The event payload must contain sufficient information for the admin frontend to display the call:

            ```json
            {
              "callId": /* new waiter_calls.id */,
              "restaurantId": /* restaurant_id */,
              "tableId": /* table_id */,
              "tableName": /* table_name_at_call */,
              "customerName": /* customer_name */,
              "message": /* message */,
              "timestamp": /* call_timestamp */
            }
            ```

* **4.2.8. API Response:**
  * **On Success:** Return an HTTP 200 OK or 201 Created status code with a JSON body: `{ "success": true, "message": "Waiter called successfully." }`.
  * **On Failure (Validation, DB Error, Rate Limit):** Return appropriate 4xx or 5xx status code with a JSON body: `{ "success": false, "message": "Specific error details here." }`.

**4.3. Admin Frontend (`digitalMenu\src\app\admin`)**

* **4.3.1. Socket.io Listener:**
  * The admin panel must listen for the `new_waiter_call` Socket.io event when connected for a specific restaurant.
* **4.3.2. UI Integration:**
  * Waiter calls must be displayed within the existing "My Orders" dashboard/page area.
  * A new section, column, or distinct visual element specifically for "Call Waiter" requests should be added to this area. If a column is used in a table view, it should be clearly labeled "Call Waiter". If a separate list/card view is used, it should be titled appropriately.
* **4.3.3. Displaying Calls:**
  * Each incoming waiter call notification should display:
    * Customer Name
    * Table Name/Number
    * Message (if provided)
    * Timestamp of the call (formatted appropriately)
* **4.3.4. Real-time Updates:**
  * New waiter calls must appear in the designated area in real-time without requiring a manual page refresh.
  * Consider a subtle visual indicator (e.g., brief highlight, unread marker) for newly arrived calls.

**5. Non-Functional Requirements**

* **5.1. Performance:**
  * The modal dialog on the user frontend must open quickly (< 500ms).
  * The backend API response time for `/api/callWaiter` should ideally be under 500ms under normal load.
  * Real-time notifications via Socket.io should appear on the admin panel within 1-2 seconds of successful backend processing.
  * The loading indicator must provide clear feedback during API calls.
* **5.2. Security:**
  * Backend API endpoint must be protected against unauthorized access if necessary (though likely public, rely on rate limiting).
  * Implement robust input sanitization and validation on the backend to prevent injection attacks (XSS, SQLi).
  * Implement effective rate limiting as specified in 4.2.4.
  * Ensure Socket.io events are broadcast only to the authenticated admin users belonging to the specific restaurant (`restaurantId`).
* **5.3. Usability:**
  * The "Call Waiter" button must be easily discoverable and understandable.
  * The modal form must be intuitive and easy to fill out.
  * Error and success messages must be clear and informative.
  * The feature must be fully responsive across common device sizes (desktop, tablet, mobile).
* **5.4. Reliability:**
  * The feature must handle backend API errors gracefully on the frontend.
  * Socket.io connections should be resilient, with mechanisms for reconnection if necessary.
  * Database transactions should ensure data integrity.
* **5.5. Maintainability:**
  * Code must adhere to existing project coding standards and best practices (Angular, Node.js/Express, etc.).
  * Code should be well-commented where necessary.
  * Consider adding unit and integration tests for the new API endpoint, frontend components, and validation logic.

**6. Design and UI/UX**

* Utilize Angular Material components (`MatToolbar`, `MatButton`, `MatIcon`, `MatDialog`, `MatFormField`, `MatInput`, `MatSelect`, `MatProgressSpinner`, `MatSnackBar` or inline modal messages) for consistency.
* Ensure visual design (colors, fonts, spacing) matches the existing qrsay application theme.
* Modal dialogs should follow accessibility best practices (ARIA attributes, keyboard navigation).
* The placement and appearance of the waiter calls on the admin dashboard should be clear and not obstruct the primary order management workflow.

**7. API Endpoint Specification**

* **Endpoint:** `/api/callWaiter`
* **Method:** `POST`
* **Request Body (JSON):**

    ```json
    {
      "restaurantId": "string", // Required
      "name": "string",         // Required, non-empty
      "tableId": "string",      // Required, valid table ID for the restaurant
      "message": "string"       // Optional
    }
    ```

* **Success Response (200 OK / 201 Created):**

    ```json
    {
      "success": true,
      "message": "Waiter called successfully."
    }
    ```

* **Error Responses:**
  * `400 Bad Request`: Invalid input data. `{ "success": false, "message": "Validation error details." }`
  * `429 Too Many Requests`: Rate limit exceeded. `{ "success": false, "message": "Rate limit exceeded. Please wait before trying again." }`
  * `404 Not Found`: Restaurant or Table ID not found. `{ "success": false, "message": "Resource not found." }`
  * `500 Internal Server Error`: Backend processing error. `{ "success": false, "message": "An internal server error occurred." }`

**8. Socket.io Event Specification**

* **Event Name:** `new_waiter_call`
* **Target:** Room/Namespace specific to `restaurantId` (e.g., `admin-restaurant-<restaurantId>`)
* **Payload (JSON):**

    ```json
    {
      "callId": number,         // ID from waiter_calls table
      "restaurantId": string,
      "tableId": string,
      "tableName": string,      // Name/number of the table
      "customerName": string,
      "message": string | null, // The optional message
      "timestamp": string       // ISO 8601 format timestamp
    }
    ```

**9. Future Considerations / Out of Scope (for this version)**

* Mechanism for admin staff to "acknowledge" or "resolve" waiter calls in the UI.
* Storing call status (`pending`, `acknowledged`, etc.) and filtering/sorting calls based on status.
* Push notifications for admins on mobile devices.
* Analytics/reporting on waiter call frequency and response times.
* Configuration options per restaurant (e.g., disable feature, customize button text/icon).

**10. Success Metrics**

* Number of successful "Call Waiter" requests initiated per day/week.
* Feedback from restaurant clients regarding the usefulness and usability of the feature.
* Reduction in customer complaints related to difficulty getting staff attention (qualitative).
* Admin panel stability and performance with real-time updates.

---
