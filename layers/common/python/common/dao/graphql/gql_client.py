import requests
import json
import logging
from common.parameters.ssm_parameters import SSMParameters
from dataclasses import dataclass

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name


def logger_warning(exc):
    logger.warning("não foi possivel manipular o recurso: %s", exc, exc_info=1)

@dataclass
class GqlClient():
    ssm_parameters = SSMParameters()
    authorization: str

    def post(self, query, variables):
        try:
            url: str = self.ssm_parameters.get_graphql_url_portal()

            headers: str = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": self.authorization
            }

            request = requests.post(
                url, json={'query': query, 'variables': json.dumps(variables)}, headers=headers)

            response = json.loads(request.text)

            if "errors" in response:
                raise Exception(response["errors"])

            if not response["data"]:
                return None

            def formatData(data): return data[list(data.keys())[0]]

            return formatData(response["data"])

        except Exception as err:
            logger_warning(f'GqlClient: {err}')
