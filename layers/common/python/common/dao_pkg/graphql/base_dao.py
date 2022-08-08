from dataclasses import dataclass
from common.dao_pkg.graphql.schemas import schemas
from common.dao_pkg.graphql.gql_client import GqlClient


@dataclass
class BaseDAO:
    authorization: str
    table_name: str

    def __post_init__(self):
        self._client = GqlClient(self.authorization)
        self._schema = schemas[self.table_name]

    def get(self, id):
        response = self._client.post(self._schema["get"], {"id": id})

        if not response:
            return None

        if "_deleted" not in response:
            raise Exception("get feature needs '_deleted' field")

        if response["_deleted"]:
            return None

        return response

    def get_all(self):
        response = self._client.post(self._schema["list"], {})
        
        return response

    def create(self, input):
        return self._client.post(self._schema["create"], {"input": input})

    def update(self, id, input):
        data_object = self.get(id)

        if not data_object:
            raise Exception("register not found")

        if "_version" not in data_object:
            raise Exception("update feature needs '_version' field")

        return self._client.post(self._schema["update"], {"input": {**input, "id": id, "_version": data_object["_version"]}})

    def delete(self, id):
        data_object = self.get(id)

        if not data_object:
            raise Exception("register not found")

        if "_version" not in data_object:
            raise Exception("delete feature needs '_version' field")

        return self._client.post(self._schema["delete"], {"input": {"id": id, "_version": data_object["_version"]}})
