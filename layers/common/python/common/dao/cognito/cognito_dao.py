import boto3
from common.parameters.ssm_parameters import SSMParameters


class CognitoDao:

    def __init__(self):
        ssm_params = SSMParameters()
        self.client = boto3.client('cognito-idp')
        self.USER_POOL_ID = ssm_params.get_cognito_user_pool_id()

    def update_user_group(self, username, group):
        return self.client.admin_add_user_to_group(
            UserPoolId=self.USER_POOL_ID,
            Username=username,
            GroupName=group
        )
