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
from flask import Flask
from slackeventsapi import SlackEventAdapter
import sys
import wait_response
from wait_response import wait_response_status



env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], '/slack/events', app)
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']


@slack_event_adapter.on('message')
def message(payload):
    """function"""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    event = payload.get('event', {})
    text = event.get('text')
    user_id = event.get('user')
    if text == "veronica":
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

        results = service.users().messages().list(userId='me',labelIds=['UNREAD', 'INBOX']).execute()
        messages = results.get('messages', [])
        
        channel_id = event.get('channel')
        user_id = event.get('user')
    
        if BOT_ID != user_id:            
            if not messages:
                client.chat_postMessage(channel=channel_id, text='Veronica has no pending messages 😎️')
                
            else:
                count_ = len(messages)
                if text == "veronica":
                    if count_ > 5 and count_ <= 9:
                        client.chat_postMessage(channel=channel_id, text="Veronica has {} unread messages 😥️".format(count_))
                    elif count_ <= 5:
                        client.chat_postMessage(channel=channel_id, text="Veronica has {} unread messages 🤔️".format(count_))
                    else:
                        client.chat_postMessage(channel=channel_id, text="Veronica has {} unread messages!!! 😭️".format(count_))


    elif text == "natalia":
            if os.path.exists('tokennatalia.json'):
                creds = Credentials.from_authorized_user_file('tokennatalia.json', SCOPES)
            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'credentials-natalia.json', SCOPES)
                    creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open('tokennatalia.json', 'w') as tokennatalia:
                    tokennatalia.write(creds.to_json())

            service = build('gmail', 'v1', credentials=creds)

            # Call the Gmail API
            #results = service.users().messages().list(userId='me', labelIds='INBOX', maxResults=1).execute()

            results = service.users().messages().list(userId='me',labelIds=['UNREAD', 'INBOX']).execute()
            messages = results.get('messages', [])
            
            channel_id = event.get('channel')
            user_id = event.get('user')
        
            if BOT_ID != user_id:            
                if not messages:
                    client.chat_postMessage(channel=channel_id, text='Natalia has no pending messages 😎️')
                    
                else:
                    count_ = len(messages)
                    if text == "natalia":
                        if count_ > 5 and count_ <= 9:
                            client.chat_postMessage(channel=channel_id, text="Natalia has {} unread messages 😥️".format(count_))
                        elif count_ <= 5:
                            client.chat_postMessage(channel=channel_id, text="Natalia has {} unread messages 🤔️".format(count_))
                        else:
                            client.chat_postMessage(channel=channel_id, text="Natalia has {} unread messages!!! 😭️".format(count_))


    elif text == "mathias":
                if os.path.exists('tokenmathias.json'):
                    creds = Credentials.from_authorized_user_file('tokenmathias.json', SCOPES)
                # If there are no (valid) credentials available, let the user log in.
                if not creds or not creds.valid:
                    if creds and creds.expired and creds.refresh_token:
                        creds.refresh(Request())
                    else:
                        flow = InstalledAppFlow.from_client_secrets_file(
                            'credentials-mathias.json', SCOPES)
                        creds = flow.run_local_server(port=0)
                    # Save the credentials for the next run
                    with open('tokenmathias.json', 'w') as tokenmathias:
                        tokenmathias.write(creds.to_json())

                service = build('gmail', 'v1', credentials=creds)

                # Call the Gmail API
                #results = service.users().messages().list(userId='me', labelIds='INBOX', maxResults=1).execute()

                results = service.users().messages().list(userId='me',labelIds=['UNREAD', 'INBOX']).execute()
                messages = results.get('messages', [])
                
                channel_id = event.get('channel')
                user_id = event.get('user')
            
                if BOT_ID != user_id:            
                    if not messages:
                        client.chat_postMessage(channel=channel_id, text='Mathias has no pending messages 😎️')
                        
                    else:
                        count_ = len(messages)
                        if text == "mathias":
                            if count_ > 5 and count_ <= 9:
                                client.chat_postMessage(channel=channel_id, text="Mathias has {} unread messages 😥️".format(count_))
                            elif count_ <= 5:
                                client.chat_postMessage(channel=channel_id, text="Mathias has {} unread messages 🤔️".format(count_))
                            else:
                                client.chat_postMessage(channel=channel_id, text="Mathias has {} unread messages!!! 😭️".format(count_))

    elif text == "todos":
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

        results = service.users().messages().list(userId='me',labelIds=['UNREAD', 'INBOX']).execute()
        messages = results.get('messages', [])
        
        channel_id = event.get('channel')
        user_id = event.get('user')
    
        if BOT_ID != user_id:            
            if not messages:
                client.chat_postMessage(channel=channel_id, text='Veronica has no pending messages 😎️')
                
            else:
                count_ = len(messages)
                if text == "todos":
                    if count_ > 5 and count_ <= 9:
                        client.chat_postMessage(channel=channel_id, text="Veronica has {} unread messages 😥️".format(count_))
                    elif count_ <= 5:
                        client.chat_postMessage(channel=channel_id, text="Veronica has {} unread messages 🤔️".format(count_))
                    else:
                        client.chat_postMessage(channel=channel_id, text="Veronica has {} unread messages!!! 😭️".format(count_))
        
        if os.path.exists('tokennatalia.json'):
            creds = Credentials.from_authorized_user_file('tokennatalia.json', SCOPES)
            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'credentials-natalia.json', SCOPES)
                    creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open('tokennatalia.json', 'w') as tokennatalia:
                    tokennatalia.write(creds.to_json())

            service = build('gmail', 'v1', credentials=creds)

            # Call the Gmail API
            #results = service.users().messages().list(userId='me', labelIds='INBOX', maxResults=1).execute()

            results = service.users().messages().list(userId='me',labelIds=['UNREAD', 'INBOX']).execute()
            messages = results.get('messages', [])
            
            channel_id = event.get('channel')
            user_id = event.get('user')
        
            if BOT_ID != user_id:            
                if not messages:
                    client.chat_postMessage(channel=channel_id, text='Natalia has no pending messages 😎️')
                    
                else:
                    count_ = len(messages)
                    if text == "todos":
                        if count_ > 5 and count_ <= 9:
                            client.chat_postMessage(channel=channel_id, text="Natalia has {} unread messages 😥️".format(count_))
                        elif count_ <= 5:
                            client.chat_postMessage(channel=channel_id, text="Natalia has {} unread messages 🤔️".format(count_))
                        else:
                            client.chat_postMessage(channel=channel_id, text="Natalia has {} unread messages!!! 😭️".format(count_))

        if os.path.exists('tokenmathias.json'):
            creds = Credentials.from_authorized_user_file('tokenmathias.json', SCOPES)
            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'credentials-mathias.json', SCOPES)
                    creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open('tokenmathias.json', 'w') as tokenmathias:
                    tokenmathias.write(creds.to_json())

            service = build('gmail', 'v1', credentials=creds)

            # Call the Gmail API
            #results = service.users().messages().list(userId='me', labelIds='INBOX', maxResults=1).execute()

            results = service.users().messages().list(userId='me',labelIds=['UNREAD', 'INBOX']).execute()
            messages = results.get('messages', [])
            
            channel_id = event.get('channel')
            user_id = event.get('user')
        
            if BOT_ID != user_id:            
                if not messages:
                    client.chat_postMessage(channel=channel_id, text='Mathias has no pending messages 😎️')
                    
                else:
                    count_ = len(messages)
                    if text == "todos":
                        if count_ > 5 and count_ <= 9:
                            client.chat_postMessage(channel=channel_id, text="Mathias has {} unread messages 😥️".format(count_))
                        elif count_ <= 5:
                            client.chat_postMessage(channel=channel_id, text="Mathias has {} unread messages 🤔️".format(count_))
                        else:
                            client.chat_postMessage(channel=channel_id, text="Mathias has {} unread messages!!! 😭️".format(count_))



    elif text == 'hola' or text == 'Hola':
        channel_id = event.get('channel')
        user_id = event.get('user')
        if BOT_ID != user_id:    
            client.chat_postMessage(channel=channel_id, text="Hola!")
    
    elif text == 'como estas?' or text == 'como estas':
        channel_id = event.get('channel')
        user_id = event.get('user')
        time.sleep(1)
        client.chat_postMessage(channel=channel_id, text="Muy bien! gracias por preguntar, y tu?")

    elif text == 'bien' or text == 'muy bien':
        channel_id = event.get('channel')
        user_id = event.get('user')
        client.chat_postMessage(channel=channel_id, text="Me alegra mucho!")
        client.chat_postMessage(channel=channel_id, text="En que te puedo ayudar?")
    
    elif text == 'Ayenda' or text == 'ayenda':
        channel_id = event.get('channel')
        user_id = event.get('user')
        client.chat_postMessage(channel=channel_id, text="Ayenda es la cadena de hoteles de mayor crecimiento en Latinoamérica que te ofrece justo lo que necesitas 🚀️")

    elif text == 'creador' or text == 'creadores':
        channel_id = event.get('channel')
        user_id = event.get('user')
        client.chat_postMessage(channel=channel_id, text="Mis creadores son Samuel Martinez, Sergio Urrego y Rubén Oliveros 🤖️")

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

if __name__ == '__main__':
    app.run(debug=True)
# [END gmail_quickstart and Slack API]
