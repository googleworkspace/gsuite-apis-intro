# Copyright 2018-2020 Google LLC
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
import pickle

from googleapiclient import discovery
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

creds = None
SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
TOKENS = 'token.p' # where to store access & refresh tokens
if os.path.exists(TOKENS):
    with open(TOKENS, 'rb') as token:
        creds = pickle.load(token)
if not (creds and creds.valid):
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
        creds = flow.run_local_server()
with open(TOKENS, 'wb') as token:
    pickle.dump(creds, token)

DRIVE = discovery.build('drive', 'v3', credentials=creds)
files = DRIVE.files().list().execute().get('files', [])
for f in files:
    print(f['name'], f['mimeType'])
