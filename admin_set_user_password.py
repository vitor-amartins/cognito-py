import botocore
import os


def admin_set_user_password(email: str, password: str, client: botocore.client.BaseClient):
    try:
        response = client.admin_set_user_password(
            UserPoolId=os.environ['USER_POOL_ID'],
            Username=email,
            Password=password,
            Permanent=True,
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
