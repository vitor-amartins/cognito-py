import boto3
from dotenv import load_dotenv
from admin_delete_user import admin_delete_user
from sign_up_and_auth import sign_up_and_auth
load_dotenv()


if __name__ == '__main__':
    email = 'contato@vitormartins.dev'
    password = 'tz%RN@bjZ8YVk'
    name = 'Vitor Matheus'
    client = boto3.client('cognito-idp', region_name='us-east-2')
    admin_delete_user(email, client)
    response = sign_up_and_auth(email, password, name, client)
