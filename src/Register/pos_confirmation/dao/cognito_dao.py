
import boto3
client = boto3.client('cognito-idp')

def update_user_group(username, group):
    return client.admin_add_user_to_group(
        UserPoolId='us-east-1_HzohDCg3k',
        Username=username,
        GroupName=group
    )
