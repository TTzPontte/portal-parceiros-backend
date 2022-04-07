import os
import boto3

ENV = os.getenv('ENV')
ssm = boto3.client('ssm')


def get_ssm_parameter_value(ssm_name):
    try:
        ssm_parameter = ssm.get_parameter(Name=ssm_name)
        return ssm_parameter['Parameter']['Value']
    except Exception as err:
        print(err)
        raise "Error capturing ssm parameters"


def get_user_invite_table_name():
    return get_ssm_parameter_value(ssm_name=f'/userInvite/{ENV}')


def get_cognito_user_pool_id():
    return get_ssm_parameter_value(ssm_name=f'/portalparceirofrontend/cognito/{ENV}')
