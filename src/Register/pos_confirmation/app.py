from dao import userinvite_dao, cognito_dao

def lambda_handler(event, context):
    request = event.get('request', None)
    userAttributes = request.get('userAttributes', None)
    member_id = userAttributes.get('custom:memberId', None)
    username = userAttributes.get('sub', None)

    try:
        user_invite = userinvite_dao.get_user_invite_by_member_id(id=member_id)
        
        if not user_invite:
            raise Exception("User invite not found")
            
        authType = user_invite.get('authType', None)
        groups = []

        if authType == 'Pontte_Users':
            groups = ['Admin', 'Pontte_Users']

        for group in groups:
            cognito_dao.update_user_group(
                username=username, group=group)

        return event

    except Exception as err:
        print(err)
        return event