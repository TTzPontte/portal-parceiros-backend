import os
from dataclasses import dataclass
from common.dao.ssm.ssm_dao import SsmDAO


@dataclass
class SSMParameters:
    ssm_dao = SsmDAO()
    ENV = os.getenv("ENV")

    def get_graphql_url_portal(self):
        return self.ssm_dao.get_ssm_parameter_value(ssm_name=f'/portalparceirofrontend/api/{self.ENV}')

    def get_user_invite_table_name(self):
        return self.ssm_dao.get_ssm_parameter_value(ssm_name=f'/userInvite/{self.ENV}')

    def get_cognito_user_pool_id(self):
        return self.ssm_dao.get_ssm_parameter_value(ssm_name=f'/portalparceirofrontend/cognito/{self.ENV}')
