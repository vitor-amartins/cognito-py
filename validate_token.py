import os
import json
import time
import urllib.request
from jose import jwk, jwt
from jose.utils import base64url_decode
from dotenv import load_dotenv
load_dotenv()


def validate_token(id_token: str):
    url = f"https://cognito-idp.{os.environ['REGION']}.amazonaws.com/{os.environ['USER_POOL_ID']}/.well-known/jwks.json"

    with urllib.request.urlopen(url) as f:
        response = f.read()
    keys = json.loads(response.decode('utf-8'))['keys']

    headers = jwt.get_unverified_headers(id_token)

    kid = headers['kid']

    key_index = -1
    for i in range(len(keys)):
        if kid == keys[i]['kid']:
            key_index = i
            break
    if key_index == -1:
        # Public key not found in jwks.json
        return False

    public_key = jwk.construct(keys[key_index])

    message, encoded_signature = str(id_token).rsplit('.', 1)

    decoded_signature = base64url_decode(encoded_signature.encode('utf-8'))

    if not public_key.verify(message.encode("utf8"), decoded_signature):
        # Signature verification failed
        return False

    # Signature successfully verified

    claims = jwt.get_unverified_claims(id_token)

    if time.time() > claims['exp']:
        # Token is expired
        return False

    return claims
