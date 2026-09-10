---
name: "google-drive"
description: "Access Google Drive files and folders via the Drive REST API with OAuth2 service-account or user-credential authentication."
---

# Google Drive API Access

Use for listing, searching, downloading, or uploading files in Google Drive. Prefer this over Playwright/ web scraping for Drive access — it is reliable, structured, and respects permissions cleanly.

## Setup

Packages installed:
```
pip3 install google-api-python-client google-auth-oauthlib google-auth-httplib2
```

### Authentication

Two options:

**Option A: Service Account (recommended for bot/automated access)**
1. Create a Google Cloud project, enable the Drive API.
2. Create a service account, download the JSON key.
3. Store the key at `~/.openclaw/google-drive-service-account.json` (never commit).
4. Share the target Drive folder with the service account email.
5. Use `google.oauth2.service_account.Credentials.from_service_account_file()`.

**Option B: User OAuth (for personal Drive access)**
1. Create OAuth 2.0 credentials (Desktop app type) in Google Cloud Console.
2. Store client secrets at `~/.openclaw/google-drive-oauth-client.json` (never commit).
3. First run opens a browser for consent; token is cached at `~/.openclaw/google-drive-token.json`.
4. Use `google_auth_oauthlib.flow.InstalledAppFlow`.

## Workflow

1. Authenticate (service account or OAuth).
2. Build the Drive service: `build('drive', 'v3', credentials=creds)`.
3. List files: `service.files().list(q=..., fields=...).execute()`.
4. Download: `service.files().get_media(fileId=id).execute()`.
5. Upload: `service.files().create(body=..., media_body=...).execute()`.
6. Search: use `q="name contains 'term' and mimeType='application/pdf'"`.

## Usage pattern

```python
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
creds = service_account.Credentials.from_service_account_file(
    '~/.openclaw/google-drive-service-account.json', scopes=SCOPES)
service = build('drive', 'v3', credentials=creds)

# List files in a folder
results = service.files().list(
    q="'FOLDER_ID' in parents",
    fields="files(id, name, mimeType, modifiedTime, size)"
).execute()
for f in results.get('files', []):
    print(f['name'], f['id'], f['mimeType'])

# Download a file
request = service.files().get_media(fileId='FILE_ID')
content = request.execute()
with open('/tmp/file.pdf', 'wb') as fh:
    fh.write(content)
```

## Running from the agent

Write a Python script to `scratch/`, run with `exec`, read output. For repeated operations, write a CLI script with subcommands.

## Notes

- Credential files live in `~/.openclaw/` and must never be committed to any repo.
- Service account email must be granted access (share the folder) before it can see files.
- Drive API has rate limits (~1000 requests/100s per user); batch when possible.
- For large files, use resumable uploads (`MediaFileUpload` with `resumable=True`).
- Export Google Docs/Sheets to PDF or other formats using `service.files().export(fileId, mimeType=...)`.
- Do not store credentials in scripts, environment dumps, logs, or memory files.
