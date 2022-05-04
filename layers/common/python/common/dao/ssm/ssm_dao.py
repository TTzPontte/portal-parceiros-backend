import boto3
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name

@dataclass
class SsmDAO:
    SSM = boto3.client('ssm')

    def get_ssm_parameter_value(self, ssm_name):
        try:
            ssm_parameter = self.SSM.get_parameter(Name=ssm_name)
            return ssm_parameter['Parameter']['Value']
        except Exception as err:
            logger.warning(err)
            raise "Error capturing ssm parameters"
