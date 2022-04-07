import boto3
from helpers import sam

dynamodb = boto3.resource("dynamodb")

USERINVITE_TABLE_NAME = sam.get_user_invite_table_name()

userinvite_table = dynamodb.Table(USERINVITE_TABLE_NAME)

def get_user_invite_by_member_id(id):
    response = userinvite_table.scan(
        FilterExpression='guestId = :guestId',
        ExpressionAttributeValues={
            ':guestId': id,
        }
    )
    if not response["Items"]:
        return None
    return response["Items"][0]
