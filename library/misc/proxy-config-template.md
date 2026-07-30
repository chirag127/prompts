# Proxy Configuration Template

Rotating proxy setup template. Replace all `<your-*>` placeholders with real credentials from your proxy provider.

```env
PROXY_URL='http://<your-proxy-user>:<your-proxy-pass>@<proxy-ip>:<proxy-port>/'

USER_PASS1='<your-proxy-user>:<your-proxy-pass>'
USER_PASS_ROTATE1='<your-proxy-user>-rotate:<your-proxy-pass>'

IP_PORT1='<proxy-ip-1>:<proxy-port-1>/'
IP_PORT2='<proxy-ip-2>:<proxy-port-2>/'

PROXY_URL1='http://<your-proxy-user>:<your-proxy-pass>@<proxy-ip-1>:<proxy-port-1>/'
PROXY_URL2='http://<your-proxy-user>:<your-proxy-pass>@<proxy-ip-2>:<proxy-port-2>/'
```

## Firebase Service Account Template

```env
FIREBASE_TYPE=service_account
FIREBASE_PROJECT_ID=<your-firebase-project-id>
FIREBASE_PRIVATE_KEY_ID=<your-firebase-private-key-id>
FIREBASE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n<your-firebase-private-key>\n-----END PRIVATE KEY-----\n"
FIREBASE_CLIENT_EMAIL=firebase-adminsdk@<your-project>.iam.gserviceaccount.com
FIREBASE_CLIENT_ID=<your-firebase-client-id>
FIREBASE_AUTH_URI=https://accounts.google.com/o/oauth2/auth
FIREBASE_TOKEN_URI=https://oauth2.googleapis.com/token
FIREBASE_AUTH_PROVIDER_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
FIREBASE_CLIENT_CERT_URL=https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk%40<your-project>.iam.gserviceaccount.com
```
