import json
import logging
import os
from boto3 import client as boto_client

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name


def invoke_lambda(invoke_event, func_name):
    logger.debug("invoke_lambda event %s", invoke_event)

    env = os.getenv('ENV')
    function = f'{func_name}-{env}'

    lambda_fn = boto_client('lambda')

    response = lambda_fn.invoke(
        FunctionName=f'{function}',
        InvocationType="RequestResponse",
        Payload=json.dumps(invoke_event).encode('utf-8')
    )

    encoded_payload = response["Payload"]

    payload = json.loads(encoded_payload.read().decode("utf-8"))

    return json.loads(payload["body"])
