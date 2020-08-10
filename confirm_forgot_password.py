import botocore
import os

from get_secret_hash import get_secret_hash


def confirm_forgot_password(email: str, password: str, confirmation_code: str, client: botocore.client.BaseClient):
    try:
        response = client.confirm_forgot_password(
            ClientId=os.environ['CLIENT_ID'],
            SecretHash=get_secret_hash(email),
            Username=email,
            Password=password,
            ConfirmationCode=confirmation_code,
        )
        return {
            'error': False,
            'success': True,
            'message': None,
            'data': response
        }
    except Exception as e:
        return {
            'error': True,
            'success': False,
            'message': str(e),
            'data': None
        }
