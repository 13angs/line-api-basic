import os
from dotenv import load_dotenv
from google.cloud import dialogflow_v2

load_dotenv('../.env')

DF_PROJECT_ID=os.environ['DF_PROJECT_ID']
LANGUAGE_CODE='en'
SESSION_ID="room-agent-bot"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./key.json"

session_client = dialogflow_v2.SessionsClient()
session = session_client.session_path(DF_PROJECT_ID, SESSION_ID)

req_body = {
  "session": session,
  "query_params": {},
  "query_input": {
    "text": {
      "text": "สวัสดีครับ",
      "language_code": "en-US"
    }
  }
}

res = session_client.detect_intent(request=req_body)
print(res)