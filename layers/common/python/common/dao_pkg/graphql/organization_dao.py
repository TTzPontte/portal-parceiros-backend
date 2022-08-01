

from dataclasses import dataclass


functions = {
        "get": """query getOrganization($id: ID!) {
                  getOrganization(id: $id) {
                    _deleted
                    _lastChangedAt
                    _version
                    documentNumber
                    createdAt
                    id
                    image
                    name
                    legalName
                    owner
                    phone
                    pipefyId
                    updatedAt
                  }
                }  
              """,
        "create": """mutation createOrganization($input: CreateOrganizationInput!) {
                      createOrganization(input: $input) {
                        _deleted
                        _lastChangedAt
                        _version
                        documentNumber
                        createdAt
                        id
                        image
                        name
                        legalName
                        owner
                        phone
                        pipefyId
                        updatedAt
                      }
                    }
                  """,
        "update": """mutation updateOrganization($input: UpdateOrganizationInput!) {
                      updateOrganization(input: $input) {
                        _deleted
                        _lastChangedAt
                        _version
                        documentNumber
                        createdAt
                        id
                        image
                        name
                        legalName
                        owner
                        phone
                        pipefyId
                        updatedAt
                      }
                    }""",
        "delete": """mutation deleteOrganization($input: DeleteOrganizationInput!) {
                    deleteOrganization(input: $input) {
                      _deleted
                      _lastChangedAt
                      _version
                      documentNumber
                      createdAt
                      id
                      image
                      name
                      legalName
                      owner
                      phone
                      pipefyId
                      updatedAt
                    }
                  }
                """
    }

from gql_client import GqlClient

@dataclass
class OrganizationDao():
  get: str
  create: str
  delete: str
  update: str
  _table: str = GqlClient("Organization")

  def __post_init__(self, params):
    self.get = _table.post(self.get, params)

  def 


organizationDao = OrganizationDao(**functions)

print(organizationDao.get)
