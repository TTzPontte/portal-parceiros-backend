import json

import boto3

TABLE_NAME = "Organization-aou76nv52bapbebq3uxerkfcce-staging"
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)


def lambda_handler(event, context):
    data = json.loads(event['body'])
    # data = event['body']

    response = table.put_item(Item=data)
    return {
        'statusCode': 201,
        'headers': {},
        'body': json.dumps({'id': response["id"]})
    }
