import base64, hashlib, hmac

def validate_signature(channel_secret: str, body: str, x_line_sig):
    new_hash = hmac.new(channel_secret.encode('utf-8'),
            body.encode('utf-8'), hashlib.sha256).digest()
    signature = base64.b64encode(new_hash).decode('utf-8')
    return x_line_sig == signature