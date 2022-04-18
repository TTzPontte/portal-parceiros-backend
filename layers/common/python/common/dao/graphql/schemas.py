
schemas = {
    "UserInvite": {
        "get":  """query getUserInvite($id: ID!) {
                    getUserInvite(id: $id) {
                      authType
                      guestId
                      hostId
                      id
                      organizationId
                      status
                      createdAt
                      _version
                      _deleted
                    }
                  }
                """,
        "create": """mutation createUserInvite($input: CreateUserInviteInput!) {
                      createUserInvite(input: $input) {
                        authType
                        guestId
                        hostId
                        id
                        organizationId
                        status
                      }
                    }
                  """,
        "update": """mutation updateUserInvite($input: UpdateUserInviteInput!) {
                      updateUserInvite(input: $input) {
                        authType
                        guestId
                        hostId
                        id
                        organizationId
                        status
                      }
                    }
                """,
        "delete": """mutation MyMutation($input: DeleteUserInviteInput!) {
                      deleteUserInvite(input: $input) {
                        status
                        organizationId
                        id
                        hostId
                        guestId
                        createdAt
                        updatedAt
                        _version
                        _deleted
                      }
                    }
                """
    },
    "Organization": {
        "get": """query getOrganization($id: ID!) {
                  getOrganization(id: $id) {
                    _deleted
                    _lastChangedAt
                    _version
                    createdAt
                    documentNumber
                    id
                    legalName
                    name
                    phone
                    updatedAt
                    pipefyId
                  }
                }  
              """,
        "create": """mutation createOrganization($input: CreateOrganizationInput!) {
                      createOrganization(input: $input) {
                        phone
                        pipefyId
                        updatedAt
                        name
                        legalName
                        id
                        documentNumber
                        createdAt
                        _version
                        _lastChangedAt
                        _deleted
                      }
                    }
                  """,
        "update": """mutation updateOrganization($input: UpdateOrganizationInput!) {
                      updateOrganization(input: $input) {
                        name
                        legalName
                        id
                        documentNumber
                        createdAt
                        _version
                        _lastChangedAt
                        _deleted
                        updatedAt
                        pipefyId
                        phone
                      }
                    }""",
        "delete": """mutation deleteOrganization($input: DeleteOrganizationInput!) {
                    deleteOrganization(input: $input) {
                      id
                      documentNumber
                      createdAt
                      _version
                      updatedAt
                      pipefyId
                      phone
                      legalName
                      _lastChangedAt
                      _deleted
                    }
                  }
                """
    },
    "Lead": {
        "get": """query getLead($id: ID!) {
                getLead(id: $id) {
                  _deleted
                  _lastChangedAt
                  _version
                  createdAt
                  documentNumber
                  email
                  id
                  name
                  organizationId
                  phone
                  pipefyId
                  updatedAt
                  userId
                  value
                }
              }""",
        "create": """mutation createLead($input: CreateLeadInput!) {
                    createLead(input: $input) {
                      _deleted
                      _lastChangedAt
                      _version
                      email
                      documentNumber
                      createdAt
                      id
                      name
                      organizationId
                      phone
                      pipefyId
                      updatedAt
                      userId
                      value
                    }
                  }""",
        "update": """mutation updateLead($input: UpdateLeadInput!) {
                  updateLead(input: $input) {
                    value
                    userId
                    pipefyId
                    updatedAt
                    phone
                    name
                    organizationId
                    email
                    id
                    documentNumber
                    createdAt
                    _version
                    _lastChangedAt
                    _deleted
                  }
                }""",
        "delete": """mutation deleteLead($input: DeleteLeadInput!) {
                    deleteLead(input: $input) {
                      _deleted
                      _version
                      createdAt
                      _lastChangedAt
                      documentNumber
                      name
                      organizationId
                      phone
                      pipefyId
                      updatedAt
                      userId
                      value
                      id
                      email
                    }
                  }"""
    },
    "Member": {
        "get": """query getMember($id: ID!) {
                  getMember(id: $id) {
                    _deleted
                    _lastChangedAt
                    _version
                    birthDate
                    createdAt
                    documentNumber
                    email
                    id
                    name
                    organizationId
                    phone
                    updatedAt
                  }
                }
                """,
        "create": """mutation createMember($input: CreateMemberInput!) {
                      createMember(input: $input) {
                        _deleted
                        _lastChangedAt
                        _version
                        birthDate
                        createdAt
                        documentNumber
                        email
                        id
                        name
                        organizationId
                        phone
                        updatedAt
                      }
                    }""",
        "update": """mutation updateMember($input: UpdateMemberInput!) {
                    updateMember(input: $input) {
                      updatedAt
                      phone
                      organizationId
                      name
                      id
                      email
                      documentNumber
                      createdAt
                      birthDate
                      _version
                      _lastChangedAt
                      _deleted
                    }
                  }""",
        "delete": """mutation deleteMember($input: DeleteMemberInput!) {
                deleteMember(input: $input) {
                  _deleted
                  _lastChangedAt
                  _version
                  createdAt
                  birthDate
                  documentNumber
                  email
                  id
                  name
                  organizationId
                  phone
                  updatedAt
                }
              }"""
    }
}
