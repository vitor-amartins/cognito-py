import botocore
import os


def admin_enable_user(email: str, client: botocore.client.BaseClient):
    try:
        response = client.admin_enable_user(
            UserPoolId=os.environ['USER_POOL_ID'],
            Username=email,
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
