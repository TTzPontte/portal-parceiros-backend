import json

import boto3

# db = os.getenv("PAERTNERS_DB")
client = boto3.client('dynamodb')

TABLE_NAME = "Organization-5wqmqox6yrcodgpnck4uzdl6by-prod"


def lambda_handler(event, context):
    data = client.scan(TableName=TABLE_NAME)
    response = json.dumps(data)
    print(response)
    response = {
        'statusCode': 200,
        'body': response,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }

    return response
