from common.dao.graphql.gql_dao import GqlDAO
import json 


def updateStatusUserInvite(uuid, status):
    simulation = GqlDAO('UserInvite')  

    response = simulation.update(uuid, { "status": status }) 
    
    return response
    

def lambda_handler(event, context):
    try:
        body = event.get('body', None) 
        
        payload = json.loads(body) if isinstance(body, str) else body
        
        action = payload.get('action')
        user_invite_id = payload.get('userInviteId')
        
        response = updateStatusUserInvite(user_invite_id, action)

        return {
            'statusCode': 200,
            'headers': {},
            'body': json.dumps(response)
        }
    except Exception as err:
        print(err)
        return {
            'statusCode': 500
        }