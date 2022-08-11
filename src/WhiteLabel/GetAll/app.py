from common.dao_pkg.graphql import WhiteLabelDAO
import json 


def lambda_handler(event, _context):
    try:
        token = event["headers"]["Authorization"]
       
        whitelabel = WhiteLabelDAO(authorization=token)
 
        response = whitelabel.get_all()
    
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
