This is a website is called qrsay which offer the ordering food platform. The code for the user frontend is code in the digitalMenu\src\app\restaurant and the admin frontend code in the digitalMenu\src\app\admin, The back end is in qrsayBackend folder.


add a small button strictly called "call waiter" in the header(mat-toolbar) of the restaurant user frontend . the button should not have a icon only text "call waiter", when the user click on it, a modal should open with a form that has the following fields: name, select table number from the list of tables, and a optional message. The form should have a submit button that sends the data to the backend and closes the modal. The modal should be styled to match the rest of the app. call waiter button should only be visible when the user is on the restaurant page and only shown if the restaurant has tables. The modal should be responsive and work on both mobile and desktop devices. The form should validate the inputs and show an error message if any of the fields are empty. The form should also show a success message when the data is sent successfully. The data should be sent to the backend using axios and the endpoint should be /api/callWaiter. The backend should handle the request and send a response back to the frontend. The response should include a success message or an error message if something goes wrong. after the form is submitted, the backend should send a notification to the admin interface using socket.io and this should be shown in the My Orders dashboard.
I have attached the image where the button should be placed. The button should be styled to match the existing theme of the application and should include an icon for better visibility.

Okay, this is a well-defined feature request. Based on your description, here are some clarifications before implementing the "Call Waiter" feature in the restaurant user frontend:

**Backend & Core Functionality:**

1.  **Backend Action:** What exactly should happen on the backend when the `/api/callWaiter` endpoint receives a request?
    *   Should it store the request in a database table (e.g., `waiter_calls`)?
    ans : yes, it should store the request in a database table called `waiter_calls`.
    *   Should it trigger a real-time notification (e.g., using WebSockets, Pusher, Socket.IO) to a specific interface (e.g., the Admin frontend, a dedicated tablet app for waiters)?
    ans : yes, it should trigger a real-time notification to the Admin frontend via socket.io.
    *   Should it send an email or SMS notification? If so, to whom (e.g., a general restaurant email, a specific manager)?
    ans : yes, it should send a notification to the restaurant manager's email.
    *   What information needs to be included in the notification/stored record (Timestamp, Restaurant ID, Name, Table, Message)?
    ans : The notification should include Timestamp, Restaurant ID, Name, Table, and Message.
    *   How will the backend identify *which* restaurant the call is for? Will the frontend need to send the `restaurantId` along with the form data in the `/api/callWaiter` request? (This seems highly likely).
    ans : yes, the frontend should send the `restaurantId` along with the form data.
2.  **Waiter/Admin Interface:** How will the restaurant staff actually *see* these calls? Is there an existing admin panel section for this, or does a new view/notification system need to be built (potentially in the `digitalMenu\src\app\admin` part)?
- ans : yes, there is an existing admin panel section for this, and it should be integrated into that.

**Frontend Data & Logic:**

5.  **Table Value:** When submitting the form, should the frontend send the Table's `ID` or its `Name/Number` to the backend? (Using the `ID` is generally more robust)
- ans : The frontend should send the Table's `ID` to the backend.
6.  **Button Visibility Logic:** How should the frontend efficiently determine if a restaurant *has tables* to show/hide the button? Is this information already loaded with the main restaurant data, or does it require fetching the table list specifically for this check?
- ans : The frontend should check if the restaurant data includes a list of tables to determine visibility.
7.  **User Name:** Should the "Name" field be pre-filled if a user authentication system exists and the user is logged in? Or should it always be manually entered?
- ans : The "Name" field should always be manually entered.

**User Experience & Edge Cases:**

8.  **Loading/Feedback:** Should there be a loading indicator shown on the modal's submit button while the request is being sent to the backend?
- ans : yes, there should be a loading indicator shown on the modal's submit button while the request is being sent to the backend.

9.  **Success Feedback:** After a successful call, should the success message appear within the modal *before* it closes, or should the modal close immediately and a global notification (like a snackbar/toast) appear? If it stays open, should it close automatically after a few seconds or require manual closing?
- ans : The success message should appear within the modal before it closes, and it should close automatically after a few seconds.

10. **Rate Limiting:** Are there any concerns about users repeatedly clicking the button? Should any simple frontend or more robust backend rate limiting be implemented to prevent abuse?
- ans : Yes, there should be a rate limiting mechanism implemented to prevent abuse.



give me a prd for the above feature