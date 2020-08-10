import botocore
import os
from get_secret_hash import get_secret_hash


def admin_initiate_auth(email: str, password: str, client: botocore.client.BaseClient):
    try:
        response = client.admin_initiate_auth(
            AuthFlow='ADMIN_NO_SRP_AUTH',
            AuthParameters={
                'USERNAME': email,
                'PASSWORD': password,
                'SECRET_HASH': get_secret_hash(email),
            },
            UserPoolId=os.environ['USER_POOL_ID'],
            ClientId=os.environ['CLIENT_ID'],
        )
        return {
            'error': False,
            'success': True,
            'message': None,
            'data': response,
        }
    except Exception as e:
        return {
            'error': True,
            'success': False,
            'message': str(e),
            'data': None
        }
