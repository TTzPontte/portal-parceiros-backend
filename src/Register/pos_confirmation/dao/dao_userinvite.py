import boto3
from dao.dao_sam import SamDao


class UserInviteDao:

    def __init__(self):
        sam = SamDao()
        dynamodb = boto3.resource("dynamodb")
        USERINVITE_TABLE_NAME = sam.get_user_invite_table_name()
        self.table = dynamodb.Table(USERINVITE_TABLE_NAME)

    def get_user_invite_by_member_id(self, id):
        response = self.table.scan(
            FilterExpression='guestId = :guestId',
            ExpressionAttributeValues={
                ':guestId': id,
            }
        )
        if not response["Items"]:
            return None
        return response["Items"][0]
