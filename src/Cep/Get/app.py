from common.helpers import invoke_lambda
import json

def lambda_handler(event, context):
    try:
        path_parameters = event.get('pathParameters', None)
        cep = path_parameters.get('cep')
        
        if not cep:
            raise Exception("field 'cep' not found in path parameters")
        
        event = {
            "queryStringParameters": {
                "trackCode": ""
            },
            "pathParameters": {
                "cep": cep
            }
        }
        
        response = invoke_lambda(event, 'CepGetFn')

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
