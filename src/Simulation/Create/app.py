from common.dao_pkg.graphql import SimulationDAO
import json 


def lambda_handler(event, _context):
    try:
        body = event.get('body', None) 
        token = event["headers"]["Authorization"]

        payload = json.loads(body) if isinstance(body, str) else body
       
        simulation = SimulationDAO(authorization=token)
 
        response = simulation.create(payload) 
    
        return {
            'statusCode': 201,
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
