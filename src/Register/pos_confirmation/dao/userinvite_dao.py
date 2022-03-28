import os
import boto3
client = boto3.client('cognito-idp')
dynamodb = boto3.resource("dynamodb")

TABLE_USERINVITE = os.getenv('USERINVITE_DB')

table_user_invite = dynamodb.Table(TABLE_USERINVITE)


def get_user_invite_by_member_id(id):
    response = table_user_invite.scan(
        TableName=TABLE_USERINVITE,
        FilterExpression='guestId = :guestId',
        ExpressionAttributeValues={
            ':guestId': id,
        }
    )
    if not response["Items"]:
        return None
    return response["Items"][0]
