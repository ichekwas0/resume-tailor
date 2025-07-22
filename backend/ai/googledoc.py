import asyncio
from asgiref.sync import sync_to_async

async def create_google_doc_async(message):
    result = await sync_to_async(create_google_doc_sync)(message)
    return result
    # return await asyncio.to_thread(create_google_doc_sync, message)

def create_google_doc_sync(message):
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
    import os
    import pickle

    SCOPES = ['https://www.googleapis.com/auth/documents']
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TOKEN_PATH = os.path.join(BASE_DIR, "token.pkl")
    CREDENTIALS_PATH = os.path.join(BASE_DIR, "credentials.json")

    creds = None
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, 'wb') as token:
            pickle.dump(creds, token)

    service = build('docs', 'v1', credentials=creds)
    doc = service.documents().create(body={'title': 'MARKDOWN TAILORED RESUME'}).execute()
    document_id = doc.get('documentId')
    update_doc_sync(document_id, service, message)
    print("Document created!")
    print("Document ID:", document_id)
    print("Open in browser:", f"https://docs.google.com/document/d/{document_id}/edit")
    return {
        'document_id': document_id,
        'url': f"https://docs.google.com/document/d/{document_id}/edit",
        'title': 'TAILORED RESUME'
    }

# DOCUMENT_ID = '16wOv4a8ZxnSZLDCbepzjCzl3zCKaz8XT_cBcwJK_NFA'
def update_doc_sync(document_id,service,message):
    requests = [
        {
        'insertText': {
            'location': {
                'index': 1,
            },
            'text': message
        }
    },
    ]
    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    print("Document updated successfully!")
    
