
import boto3
from helpers import sam
client = boto3.client('cognito-idp')
    
USER_POOL_ID = sam.get_cognito_user_pool_id()

def update_user_group(username, group):
    return client.admin_add_user_to_group(
        UserPoolId=USER_POOL_ID,
        Username=username,
        GroupName=group
    )
