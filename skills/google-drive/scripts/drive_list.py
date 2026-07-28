#!/usr/bin/env python3
"""List or search files in Google Drive.

Usage:
  python3 drive_list.py [--folder FOLDER_ID] [--query QUERY] [--download FILE_ID]

Requires a service account key at ~/.openclaw/google-drive-service-account.json
or an OAuth client secret at ~/.openclaw/google-drive-oauth-client.json.
"""
import argparse
import os
import sys
from pathlib import Path

from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']


def get_credentials():
    sa_path = Path.home() / '.openclaw' / 'google-drive-service-account.json'
    oauth_path = Path.home() / '.openclaw' / 'google-drive-oauth-client.json'
    token_path = Path.home() / '.openclaw' / 'google-drive-token.json'

    if sa_path.exists():
        return service_account.Credentials.from_service_account_file(
            str(sa_path), scopes=SCOPES)

    if oauth_path.exists():
        import json
        from google.oauth2.credentials import Credentials
        if token_path.exists():
            creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
            if creds.valid:
                return creds
            if creds.expired and creds.refresh_token:
                creds.refresh(Request())
                token_path.write_text(creds.to_json())
                return creds
        flow = InstalledAppFlow.from_client_secrets_file(str(oauth_path), SCOPES)
        creds = flow.run_local_server(port=0)
        token_path.write_text(creds.to_json())
        return creds

    print("ERROR: No credentials found. Place service account key or OAuth client secret in ~/.openclaw/", file=sys.stderr)
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="List or search Google Drive files")
    parser.add_argument('--folder', default=None, help='Folder ID to list')
    parser.add_argument('--query', default=None, help='Drive query string')
    parser.add_argument('--download', default=None, help='File ID to download')
    parser.add_argument('--output', default=None, help='Output path for download')
    args = parser.parse_args()

    creds = get_credentials()
    service = build('drive', 'v3', credentials=creds)

    if args.download:
        out_path = args.output or '/tmp/drive_download'
        request = service.files().get_media(fileId=args.download)
        with open(out_path, 'wb') as fh:
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while not done:
                _, done = downloader.next_chunk()
        print(f"Downloaded to {out_path}")
        return

    q = None
    if args.folder:
        q = f"'{args.folder}' in parents"
    if args.query:
        q = f"{q and q + ' and ' or ''}{args.query}"

    results = service.files().list(
        q=q, pageSize=100, fields="files(id, name, mimeType, modifiedTime, size)"
    ).execute()
    files = results.get('files', [])
    if not files:
        print("No files found.")
        return
    for f in files:
        print(f"{f['name']}\t{f['id']}\t{f.get('mimeType', '?')}\t{f.get('size', '?')}\t{f.get('modifiedTime', '?')}")


if __name__ == '__main__':
    main()
