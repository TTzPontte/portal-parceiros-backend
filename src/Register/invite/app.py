from common.dao_pkg.graphql import UserInviteDAO, MemberDAO
import json


def update_status_userinvite(token, uuid, status):
    user_invite_dao = UserInviteDAO(authorization=token)

    return user_invite_dao.update(uuid, {"status": status})


def update_user_id_member(token, uuid, user_id):
    member_dao = MemberDAO(authorization=token)

    return member_dao.update(uuid, {"userId": user_id})


def lambda_handler(event, _context):
    try:
        body = event.get('body')
        request_context = event.get('requestContext')
        token = event["headers"]["Authorization"]

        payload = json.loads(body) if isinstance(body, str) else body

        action = payload.get('action')
        user_invite_id = payload.get('userInviteId')
        user_id = request_context["authorizer"]["claims"]["sub"]

        user_invite = update_status_userinvite(token, user_invite_id, action)

        if user_invite["status"] == "registered":
            update_user_id_member(token, user_invite["guestId"], user_id)

        return {
            'statusCode': 204,
            'headers': {
                'Access-Control-Allow-Origin': '*',
            },
            'body': json.dumps({})
        }
    except Exception as err:
        print(err)
        return {
            'statusCode': 500
        }
