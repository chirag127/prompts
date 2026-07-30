This is a website is called qrsay which offer the ordering food platform. The code for the user frontend is code in the digitalMenu\src\app\restaurant and the admin frontend code in the digitalMenu\src\app\admin, The back end is in qrsayBackend folder.

add a small button strictly called "call waiter" in the header(mat-toolbar) at the top right side of the restaurant user frontend . the button should not have a icon. The button should be in the left side of the cart button.
when the user click on it, a modal should open with a form that has the following fields: name, select table number from the list of tables, and a optional message. The form should have a submit button that sends the data to the backend and closes the modal. The modal should be styled to match the rest of the app. call waiter button should only be visible when the user is on the restaurant page and only shown if the restaurant has tables. The modal should be responsive and work on both mobile and desktop devices. The form should validate the inputs and show an error message if any of the fields are empty. The form should also show a success message when the data is sent successfully. The data should be sent to the backend using axios and the endpoint should be /api/callWaiter. The backend should handle the request and send a response back to the frontend. The response should include a success message or an error message if something goes wrong. after the form is submitted, the backend should send the request to the admin frontend using socket.io  should be shown in the My Orders dashboard in a column labeled "Call Waiter".
I have attached the image where the button should be placed. The button should be styled to match the existing theme of the application and should include an icon for better visibility. don't send the notification. don't add any sound or vibration at admin frontend.

Okay, this is a well-defined feature request. here are some clarifications before implementing the "Call Waiter" feature in the restaurant user frontend.

* **Backend Storage:** Waiter calls will be stored in a new `waiter_calls` database table.
* **required Data:** Include Timestamp, Restaurant ID, Name, Table (ID and potentially Name), and Message.
* **Restaurant Identification:** The frontend must send the Restaurant `ID` to the backend.
* **Admin Interface:** the calls to the admin frontend will be integrated into the existing Admin panel, specifically displayed within the "My Orders" dashboard area in a column labeled "Call Waiter".
* **Table Value:** The frontend will send the Table `ID` to the backend.
* **Button Visibility Data:** Frontend checks if the loaded restaurant data object includes a list/array of tables.
* **User Name Field:** The "Name" field will always be manually entered by the customer.
* **Loading Indicator:** A loading indicator is required on the modal's submit button during the API call.
* **Success Feedback:** The success message will appear within the modal, which will then auto-close after a few seconds.
* **Rate Limiting:** Rate limiting is required to prevent abuse.
* **Form Validation:** The form should validate the inputs and show an error message if any of the fields are empty.

give me the prd in a markdown format for the above feature request. The PRD should be for final product and not for MVP. The PRD should be in a markdown format.
