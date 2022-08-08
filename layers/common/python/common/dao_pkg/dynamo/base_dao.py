from dataclasses import dataclass
import logging
import botocore

from boto3 import resource as boto_resource
from boto3.dynamodb.conditions import Key
from botocore import exceptions as boto_exceptions

dynamodb = boto_resource("dynamodb")

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name

def logger_warning(exc):
    logger.warning("não foi possivel recuperar o recurso: %s", exc, exc_info=1)

@dataclass
class BaseDAO:
    table_name: str

    def __post_init__(self):
        self._table = dynamodb.Table(name=self.table_name)

    def get(self, key, value):
        try:
            response = self._table.query(KeyConditionExpression=Key(key).eq(value))

            if not response["Items"]:
                return None

            return response["Items"][0]

        except boto_exceptions.ClientError as exc:
            logger_warning(exc)
            return None

    def scan(self, filter_expression, expression_attribute_values):
        try:
            response = self._table.scan(
                FilterExpression=filter_expression,
                ExpressionAttributeValues={**expression_attribute_values}
            )

            if not response["Items"]:
                return None

            return response["Items"]

        except boto_exceptions.ClientError as exc:
            logger_warning(exc)
            return None

    def create(self, item):
        try:
            return self._table.put_item(Item=item)
        except botocore.exceptions.ClientError as exc:
            logger.warning(
                'não foi possivel persistir o objeto no banco de dados: %s',
                exc, exc_info=1
            )

    def update(self, keys, update_expression, expression_attribute_values):
        try:
            response = self._table.update_item(
                Key={**keys},
                UpdateExpression="set " + ", ".join(update_expression),
                ExpressionAttributeValues={**expression_attribute_values},
                ReturnValues="UPDATED_NEW"
            )

            if not response["Attributes"]:
                return None

            return response["Attributes"]

        except boto_exceptions.ClientError as exc:
            logger_warning(exc)
            return None

    def delete(self, keys):
        try:
            return self._table.delete_item(Key={**keys})
        except botocore.exceptions.ClientError as exc:
            logger.warning(
                'não foi possivel persistir o objeto no banco de dados: %s',
                exc, exc_info=1
            )
