import botocore
import os

from admin_create_user import admin_create_user
from admin_delete_user import admin_delete_user
from admin_initiate_auth import admin_initiate_auth
from admin_set_user_password import admin_set_user_password


def sign_up_and_auth(email: str, password: str, name: str, client: botocore.client.BaseClient):
    result = admin_create_user(email, name, client)
    if not result['success']:
        # Failed in create the user
        return result
    # User is created
    result = admin_set_user_password(email, password, client)
    if not result['success']:
        # Failed in set user's password
        admin_delete_user(email, client)
        return result
    # Password was succesfully set
    return admin_initiate_auth(email, password, client)
