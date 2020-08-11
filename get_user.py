import botocore
import os


def get_user(access_token: str, client: botocore.client.BaseClient):
    try:
        response = client.get_user(
            AccessToken=access_token,
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
