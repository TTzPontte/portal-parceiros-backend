from common.dao.graphql.gql_dao import GqlDAO
import json


def update_status_userinvite(token, uuid, status):
    simulation = GqlDAO(authorization=token, table_name='UserInvite')

    return simulation.update(uuid, {"status": status})


def update_user_id_member(token, uuid, user_id):
    simulation = GqlDAO(authorization=token, table_name='Member')

    return simulation.update(uuid, {"userId": user_id})


def lambda_handler(event, context):
    try:
        body = event.get('body')
        requestContext = event.get('requestContext')
        token = event["headers"]["Authorization"]

        payload = json.loads(body) if isinstance(body, str) else body

        action = payload.get('action')
        user_invite_id = payload.get('userInviteId')
        user_id = requestContext["authorizer"]["claims"]["sub"]

        user_invite = update_status_userinvite(token, user_invite_id, action)

        if user_invite["status"] == "registered":
            update_user_id_member(token, user_invite["guestId"], user_id)

        return {
            'statusCode': 204,
            'headers': {},
            'body': json.dumps({})
        }
    except Exception as err:
        print(err)
        return {
            'statusCode': 500
        }
