import os
import boto3


class SamDao:

    def __init__(self):
        self.ENV = os.getenv('ENV')
        self.ssm = boto3.client('ssm')
        pass

    def get_ssm_parameter_value(self, ssm_name):
        try:
            ssm_parameter = self.ssm.get_parameter(Name=ssm_name)
            return ssm_parameter['Parameter']['Value']
        except Exception as err:
            print(err)
            raise "Error capturing ssm parameters"

    def get_user_invite_table_name(self):
        return self.get_ssm_parameter_value(ssm_name=f'/userInvite/{self.ENV}')

    def get_cognito_user_pool_id(self):
        return self.get_ssm_parameter_value(ssm_name=f'/portalparceirofrontend/cognito/{self.ENV}')
