from common.dao_pkg.cognito.cognito_dao import CognitoDao
from common.dao_pkg.dynamo import UserInviteDAO


def lambda_handler(event, _context):

    try:
        
        request = event.get('request', None)
        user_attributes = request.get('userAttributes')
        client_metadata = request.get('clientMetadata')
    
        user_invite_id = client_metadata.get('userInviteId', None)
        username = user_attributes.get('sub', None)

        user_invite_dao = UserInviteDAO()

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
