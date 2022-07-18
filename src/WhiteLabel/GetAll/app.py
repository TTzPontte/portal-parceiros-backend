from common.dao.graphql.gql_dao import GqlDAO
import json 

def lambda_handler(event, context):
    try:
        token = event["headers"]["Authorization"]
       
        whitelabel = GqlDAO(authorization=token, table_name='WhiteLabel')   
 
        response = whitelabel.getAll()
    
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
