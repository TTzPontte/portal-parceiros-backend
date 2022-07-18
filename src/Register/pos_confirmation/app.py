from common.dao.dynamo.dynamo_dao import DynamoDAO
from common.parameters.ssm_parameters import SSMParameters
from common.dao.cognito.cognito_dao import CognitoDao


def lambda_handler(event, context):

    try:
        
        request = event.get('request', None)
        user_attributes = request.get('userAttributes')
        client_metadata = request.get('clientMetadata')
    
        user_invite_id = client_metadata.get('userInviteId', None)
        username = user_attributes.get('sub', None)
      
        sam = SSMParameters()
        user_invite_table_name = sam.get_user_invite_table_name()

        user_invite_dao = DynamoDAO(user_invite_table_name)

        user_invite = user_invite_dao.get(key="id", value=user_invite_id)

        if not user_invite:
            raise Exception("User invite not found")

        auth_type = user_invite.get('authType', None)
        groups = []

        if auth_type == 'Pontte_Users':
            groups = ['Admin', 'Pontte_Users']

        dao_cognito = CognitoDao()

        for group in groups:
            dao_cognito.update_user_group(username=username, group=group)

        return event

    except Exception as err:
        print(err)
        return event
