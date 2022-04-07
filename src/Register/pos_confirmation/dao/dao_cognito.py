
import boto3
from dao.dao_sam import SamDao


class CognitoDao:

    def __init__(self):
        dao_sam = SamDao()
        self.client = boto3.client('cognito-idp')
        self.USER_POOL_ID = dao_sam.get_cognito_user_pool_id()

    def update_user_group(self, username, group):
        return self.client.admin_add_user_to_group(
            UserPoolId=self.USER_POOL_ID,
            Username=username,
            GroupName=group
        )
