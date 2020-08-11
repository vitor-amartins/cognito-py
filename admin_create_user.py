import botocore
import botocore.exceptions
import os


def admin_create_user(email: str, name: str, client: botocore.client.BaseClient):
    try:
        response = client.admin_create_user(
            UserPoolId=os.environ['USER_POOL_ID'],
            Username=email,
            UserAttributes=[
                {
                    'Name': 'name',
                    'Value': name,
                },
                {
                    'Name': 'email',
                    'Value': email,
                },
                {
                    'Name': 'email_verified',
                    'Value': 'true',
                },
            ],
            ValidationData=[
                {
                    'Name': 'email',
                    'Value': email,
                },
            ],
            ForceAliasCreation=True,
            MessageAction='SUPPRESS',
        )
        return {
            'success': True,
            'message': None,
            'data': response
        }
    except client.exceptions.UsernameExistsException as e:
        return {
            'success': False,
            'message': 'This username already exists',
            'data': None,
        }

    except Exception as e:
        return {
            'success': False,
            'message': str(e),
            'data': None
        }
