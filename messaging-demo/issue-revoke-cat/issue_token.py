import requests, os, json
from dotenv import load_dotenv

load_dotenv()
OUTPUT_PATH = './output'
CAT_ACTION = os.environ['CAT_ACTION'] # revoke or issue
url = "https://api.line.me/oauth2/v2.1/token"
headers = {
    'Content-type': 'application/x-www-form-urlencoded'
}

# issue the channel access token
if CAT_ACTION == 'issue':
    # loading jwt file
    jwt = {}
    jwt_path = os.path.join(OUTPUT_PATH, 'jwt.json')
    with open(jwt_path, 'r', encoding='utf-8') as jwt_file:
        jwt = json.load(jwt_file)

    data = {
        "grant_type": "client_credentials",
        "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
        "client_assertion": jwt['jwt']
    }
    url = "https://api.line.me/oauth2/v2.1/token"

    res = requests.post(url=url, headers=headers, data=data)
    print(res.status_code)
    print(res.content)

    cat = res.content.decode(encoding='utf-8')
    cat_path = os.path.join(OUTPUT_PATH, 'cat.json')
    if res.status_code == 200:
        with open(cat_path, 'w', encoding='utf-8') as cat_file:
            json.dump(json.loads(cat), cat_file, indent=4)

# revoke the channel access token
if CAT_ACTION == 'revoke':

    # loading setting and cat file
    setting = {}
    cat = {}
    setting_path = os.path.join(OUTPUT_PATH, 'setting.json')
    cat_path = os.path.join(OUTPUT_PATH, 'cat.json')
    with open(setting_path, 'r', encoding='utf-8') as setting_file:
        setting = json.load(setting_file)
    with open(cat_path, 'r', encoding='utf-8') as cat_file:
        cat = json.load(cat_file)

    url = "https://api.line.me/oauth2/v2.1/revoke"

    data = {
        "client_id": setting["channel_id"],
        "client_secret": setting["channel_secret"],
        "access_token": cat["access_token"]
    }

    res = requests.post(url=url, headers=headers, data=data)
    print(res.status_code)
    print(res.content)
    