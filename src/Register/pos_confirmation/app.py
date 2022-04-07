from dao.dao_userinvite import UserInviteDao
from dao.dao_cognito import CognitoDao

def lambda_handler(event, context):
    request = event.get('request', None)
    userAttributes = request.get('userAttributes', None)
    member_id = userAttributes.get('custom:memberId', None)
    username = userAttributes.get('sub', None)

    try:
        dao_user_invite= UserInviteDao()

        user_invite = dao_user_invite.get_user_invite_by_member_id(id=member_id)
        
        if not user_invite:
            raise Exception("User invite not found")
            
        authType = user_invite.get('authType', None)
        groups = []

        if authType == 'Pontte_Users':
            groups = ['Admin', 'Pontte_Users']

        dao_cognito = CognitoDao()

        for group in groups:
            dao_cognito.update_user_group(
                username=username, group=group)

        return event

    except Exception as err:
        print(err)
        return event
