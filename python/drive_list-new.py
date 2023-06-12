# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function
import os.path

from google.auth.transport.requests import Request
from google.oauth2 import credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import discovery

creds = None
SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
TOKENS = 'storage.json'
if os.path.exists(TOKENS):
    creds = credentials.Credentials.from_authorized_user_file(TOKENS)
if not (creds and creds.valid):
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
        creds = flow.run_local_server()
with open(TOKENS, 'w') as token:
    token.write(creds.to_json())

DRIVE = discovery.build('drive', 'v3', credentials=creds)
files = DRIVE.files().list().execute().get('files', [])
for f in files:  # 4 fields returned: mimeType, kind, id, name
    print(f['name'], f['mimeType'])
