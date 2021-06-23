from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import time
import slack
import os
from pathlib import Path
from dotenv import load_dotenv



# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    #results = service.users().messages().list(userId='me', labelIds='INBOX', maxResults=1).execute()
    
    
    results = service.users().messages().list(userId='me',labelIds=['UNREAD', 'INBOX'], q="category:primary", maxResults=5).execute()
    messages = results.get('messages', [])
    
    if not messages:
        print('No mensajes found.')
    else:
        count = 1
        lista = ["samuel", "noches", "descuento"]
        new_list = []
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            new = msg['snippet'].split(" ")

            for word in new:
                if word.lower() in lista:   
                    print("entro")     
                    # msg = service.users().messages().get(userId='me', id=message['id']).execute()
                    # print("\n")
                    # print("Message: {}".format(count))
                    # print(msg['snippet'])
                    # print("\n")
                    # time.sleep(2)
                    # count += 1
                
                    
        print("-------------------------------")
        print("Total messages extracted: {} 😀️".format(count - 1))
        print("-------------------------------")
        print("\n")

            


if __name__ == '__main__':
    main()
# [END gmail_quickstart]