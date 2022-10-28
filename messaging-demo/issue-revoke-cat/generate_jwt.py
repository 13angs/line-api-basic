import time
import jwt
from jwt.algorithms import RSAAlgorithm
import json, os

print('Loading private key...')

OUTPUT_PATH = './output'
private_path = os.path.join(OUTPUT_PATH, 'prt.json')
private_key = {}

with open(private_path, 'r', encoding='utf-8') as private_file:
    private_key = json.load(private_file)
# print(''+json.dumps(private_key, indent=2))

print('Loading setting...')
setting_path = os.path.join(OUTPUT_PATH, 'setting.json')
setting = {}
with open(setting_path, 'r', encoding='utf-8') as setting_file:
    setting = json.load(setting_file)
print(''+json.dumps(setting, indent=2))

headers = {
    "alg": "RS256",
    "typ": "JWT",
    "kid": setting["kid"]
}

payload = {
    "iss": setting["channel_id"],
    "sub": setting["channel_id"],
    "aud": "https://api.line.me/",
    "exp":int(time.time())+(60 * 30),
    "token_exp": 60 * 60 * 24 * 30
}

key = RSAAlgorithm.from_jwk(private_key)

JWT = jwt.encode(payload=payload, key=key, algorithm='RS256', headers=headers, json_encoder=None)
jwt_dic = {
    "jwt": JWT
}
jwt_path = os.path.join(OUTPUT_PATH, 'jwt.json')

with open(jwt_path, 'w', encoding='utf-8') as jwt_file:
    json.dump(jwt_dic, jwt_file, indent=4)