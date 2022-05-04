from common.dao.graphql.gql_dao import GqlDAO
import json 

def lambda_handler(event, context):
    try:
        body = event.get('body', None) 

        payload = json.loads(body) if isinstance(body, str) else body
       
        simulation = GqlDAO('Simulation')  
 
        response = simulation.create(payload) 
    
        return {
            'statusCode': 201,
            'headers': {},
            'body': json.dumps(response)
        }
    except Exception as err:
        print(err)
        return {
            'statusCode': 500
        }
