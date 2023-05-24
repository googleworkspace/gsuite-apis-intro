/*
POST:         ...
FILE:         drive_list100.py
COPYRIGHT:    (c)2023 CyberWeb Consulting LLC
LICENSE:      apache.org/licenses/LICENSE-2.0
*/

const fs = require('fs').promises;
const path = require('path');
const process = require('process');
const {authenticate} = require('@google-cloud/local-auth');
const {google} = require('googleapis');

const SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly'];
const TOKEN_PATH = path.join(process.cwd(), 'storage.json');
const CREDENTIALS_PATH = path.join(process.cwd(), 'client_secret.json');


/**
 * Prints a circle.
 *
 * @return {JSONClient} client
 */
async function loadSavedCredentialsIfExist() {
    try {
        const content = await fs.readFile(TOKEN_PATH);
        const credentials = JSON.parse(content);
        return google.auth.fromJSON(credentials);
    } catch(err) {
        return null;
    }
}


/**
 * Prints a circle.
 *
 * @param {Circle} client
 */
async function saveCredentials(client) {
    const content = await fs.readFile(CREDENTIALS_PATH);
    const keys = JSON.parse(content);
    const key = keys.installed || keys.web;
    const payload = JSON.stringify({
        type: 'authorized_user',
        client_id: key.client_id,
        client_secret: key.client_secret,
        refresh_token: client.credentials.refresh_token,
    });
    await fs.writeFile(TOKEN_PATH, payload);
}


/**
 * Prints a circle.
 *
 * @return {Circle} client
 */
async function authorize() {
    let client = await loadSavedCredentialsIfExist();
    if (client) return client;
    client = await authenticate({
        scopes: SCOPES,
        keyfilePath: CREDENTIALS_PATH,
    });
    if (client.credentials) await saveCredentials(client);
    return client;
}


/**
 * Prints a circle.
 *
 * @param {Circle} authClient
 */
async function listFiles(authClient) {
    const drive = google.drive({version: 'v3', auth: authClient});
    const res = await drive.files.list({fields: 'files(name,mimeType)'});
    const files = res.data.files;
    if (files.length !== 0) {
        files.map(file => console.log(`${file.name} (${file.mimeType})`));
    }
}

authorize().then(listFiles).catch(console.error);
