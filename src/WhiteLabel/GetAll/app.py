from common.dao_pkg.dynamo import WhiteLabelDAO
import json 


def lambda_handler(event, _context):
    try:
       
        whitelabel = WhiteLabelDAO()
 
        response = whitelabel.scan("active = :active", {":active": True})

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
            },
            'body': json.dumps(response, default=str)
        }
    except Exception as err:
        print(err)
        return {
            'statusCode': 500
        }
