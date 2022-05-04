from common.dao.graphql.gql_dao import GqlDAO
import json 

def lambda_handler(event, context):
    try:
        path_parameters = event.get('pathParameters', None)
        uuid = path_parameters.get('id')
 
        if not uuid:
            raise Exception("field 'id' not found in path parameters") 
       
        simulation = GqlDAO('Simulation')  
 
        simulation.delete(uuid) 
    
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
