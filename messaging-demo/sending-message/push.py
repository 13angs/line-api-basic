import requests
import os
from dotenv import load_dotenv

load_dotenv('../.env')

URL='https://api.line.me/v2/bot/message/push'
USER_ID = os.environ['USER_ID']
ACCESS_TOKEN=os.environ['ACCESS_TOKEN']

headers = {
    'Content-Type': "application/json",
    'Authorization': f"Bearer {ACCESS_TOKEN}"
}

body = {
    'to': USER_ID,
    'messages': [
        {
            "type": "text",
            "text": "From python!!"
        },
        # {
        #     "type": "text",
        #     "text": "$ Is there anything I can help?🐱",
        #     "emojis": [
        #         {
        #             "index": 0,
        #             "productId": "5ac1bfd5040ab15980c9b435",
        #             "emojiId": "001"
        #         }
        #     ]
        # },
        # {
        #     "type": "sticker",
        #     "packageId": "446",
        #     "stickerId": "1988"
        # }
    ]
}
res = requests.post(url=URL, headers=headers, json=body)
print(res.status_code)
print(res.content)