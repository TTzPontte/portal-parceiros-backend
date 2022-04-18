import requests
import json
import logging
from common.parameters.ssm_parameters import SSMParameters

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name

def logger_warning(exc):
    logger.warning("não foi possivel manipular o recurso: %s", exc, exc_info=1)


class GqlClient():
    ssm_parameters = SSMParameters()
    
    url: str = ssm_parameters.get_graphql_url_portal()

    headers: str = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "x-api-key": ssm_parameters.get_graphql_api_key_portal()
    }

    def post(self, query, variables):
        try:
            request = requests.post(self.url, json={'query': query, 'variables': json.dumps(variables)}, headers=self.headers)

            response = json.loads(request.text)
        
            if "errors" in response:
                raise Exception(response["errors"])

            if not response["data"]:
                return None 
                
            formatData = lambda data : data[list(data.keys())[0]]
            
            return formatData(response["data"])
            
        except Exception as err:
            logger_warning(f'GqlClient: {err}')
