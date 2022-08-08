import json

import boto3

TABLE_NAME = "Lead-5wqmqox6yrcodgpnck4uzdl6by-prod"
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)


def lambda_handler(event, context):
    data = json.loads(event['body'])
    # data = event['body']

    response = table.put_item(Item=data)
    
    return {
        'statusCode': 201,
        'headers': {
            'Access-Control-Allow-Origin': '*',
        },
        'body': json.dumps({'id': data["id"]})
    }
