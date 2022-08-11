from common.dao_pkg.graphql import SimulationDAO
import json 


def lambda_handler(event, _context):
    try:
        path_parameters = event.get('pathParameters', None)
        uuid = path_parameters.get('id')
        token = event["headers"]["Authorization"]

        body = event.get('body', None) 
        payload = json.loads(body) if isinstance(body, str) else body

        if not uuid:
            raise Exception("field 'id' not found in path parameters") 
       
        simulation = SimulationDAO(authorization=token)
 
        response = simulation.update(uuid, payload) 
    
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
            },
            'body': json.dumps(response)
        }
    except Exception as err:
        print(err)
        return {
            'statusCode': 500
        }
