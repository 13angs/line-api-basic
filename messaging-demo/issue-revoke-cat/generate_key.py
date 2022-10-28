from jwcrypto import jwk
import json, os


key = jwk.JWK.generate(kty='RSA', alg="RS256", use="sig", size=2048)

private_key = key.export_private()
public_key = key.export_public()

# print("=== private key ===\n"+json.dumps(json.loads(private_key), indent=2))
# print("=== public key ===\n"+json.dumps(json.loads(public_key), indent=2))
print('====================================================================')
print('Generating public and private key...')

OUT_PUT = './output'
private_path = os.path.join(OUT_PUT, 'prt.json')
public_path = os.path.join(OUT_PUT, 'pub.json')

with open(private_path, 'w', encoding='utf-8') as private_file:
    json.dump(json.loads(private_key), private_file, indent=4)

with open(public_path, 'w', encoding='utf-8') as public_file:
    json.dump(json.loads(public_key), public_file, indent=4)



