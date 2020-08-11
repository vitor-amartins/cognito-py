import botocore
import os

from get_secret_hash import get_secret_hash


def forgot_password(email: str, client: botocore.client.BaseClient):
    try:
        response = client.forgot_password(
            ClientId=os.environ['CLIENT_ID'],
            SecretHash=get_secret_hash(email),
            Username=email,
        )
        return {
            'success': True,
            'message': None,
            'data': response
        }
    except Exception as e:
        return {
            'success': False,
            'message': str(e),
            'data': None
        }
