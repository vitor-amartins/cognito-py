import os
import hmac
import base64
import hashlib

def get_secret_hash(username: str):
    msg = username + os.environ['CLIENT_ID']
    dig = hmac.new(str(os.environ['CLIENT_SECRET']).encode('utf-8'), msg = str(msg).encode('utf-8'), digestmod=hashlib.sha256).digest()
    d2 = base64.b64encode(dig).decode()
    return d2
