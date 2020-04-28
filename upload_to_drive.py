from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.http import MediaFileUpload


SCOPES = ['https://www.googleapis.com/auth/drive']

def upload_csv(filename):

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    # Upload  the csv file 
    file_metadata = {
        'name': filename.replace(".csv", ""),
        'mimeType': 'application/vnd.google-apps.spreadsheet'
    }
    media = MediaFileUpload(filename,
                            mimetype='text/csv'
                            )
    file = service.files().create(body=file_metadata,
                                  media_body=media,
                                  fields='id').execute()
    print("{} was uploaded to Google Drive!".format(filename))